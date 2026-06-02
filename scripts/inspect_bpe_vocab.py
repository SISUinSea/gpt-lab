#!/usr/bin/env python3
"""Inspect and visualize a byte-level BPE vocabulary JSON file."""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import tempfile
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


SPECIAL_TOKENS = ["<pad>", "<unk>", "<bos>", "<eos>"]
BYTE_OFFSET = len(SPECIAL_TOKENS)
NUM_BYTES = 256
BASE_VOCAB_SIZE = BYTE_OFFSET + NUM_BYTES


@dataclass
class TokenRecord:
    token_id: int
    kind: str
    byte_value: bytes | None
    text: str
    decode_ok: bool
    decode_error: str = ""
    left_id: int | None = None
    right_id: int | None = None
    flags: set[str] = field(default_factory=set)
    categories: set[str] = field(default_factory=set)

    @property
    def byte_len(self) -> int:
        return len(self.byte_value or b"")

    @property
    def char_len(self) -> int:
        return len(self.text) if self.decode_ok else 0

    @property
    def byte_hex(self) -> str:
        return (self.byte_value or b"").hex(" ")


@dataclass
class VocabInspection:
    records: list[TokenRecord]
    merges_count: int
    expected_vocab_size: int | None
    structure_errors: list[str]
    structure_warnings: list[str]
    duplicate_pairs: list[tuple[tuple[int, int], int, int]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect byte-level BPE vocab JSON and generate reports."
    )
    parser.add_argument(
        "--vocab",
        type=Path,
        default=Path("data/bpe_tokenizer_vocab3000.json"),
        help="Path to the BPE vocab JSON file.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("output/bpe_vocab_report"),
        help="Directory where report files will be written.",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="Number of sample rows to include in markdown reports.",
    )
    parser.add_argument(
        "--long-byte-threshold",
        type=int,
        default=32,
        help="Flag tokens whose byte length is at least this value.",
    )
    parser.add_argument(
        "--long-char-threshold",
        type=int,
        default=16,
        help="Flag tokens whose character length is at least this value.",
    )
    return parser.parse_args()


def load_merges(path: Path) -> list[Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Top-level JSON value must be an object.")
    if "merges" not in data:
        raise ValueError("Top-level JSON object must contain a 'merges' field.")
    if not isinstance(data["merges"], list):
        raise ValueError("'merges' must be a list.")
    return data["merges"]


def expected_vocab_size_from_filename(path: Path) -> int | None:
    match = re.search(r"vocab[_-]?(\d+)", path.stem)
    if not match:
        return None
    return int(match.group(1))


def decode_bytes(byte_value: bytes | None) -> tuple[str, bool, str]:
    if byte_value is None:
        return "", False, "missing bytes"
    try:
        return byte_value.decode("utf-8"), True, ""
    except UnicodeDecodeError as exc:
        return "", False, str(exc)


def has_hangul(text: str) -> bool:
    for ch in text:
        code = ord(ch)
        if (
            0xAC00 <= code <= 0xD7A3
            or 0x1100 <= code <= 0x11FF
            or 0x3130 <= code <= 0x318F
            or 0xA960 <= code <= 0xA97F
            or 0xD7B0 <= code <= 0xD7FF
        ):
            return True
    return False


def has_repeated_run(text: str, run_len: int = 3) -> bool:
    if len(text) < run_len:
        return False
    current = ""
    count = 0
    for ch in text:
        if ch == current:
            count += 1
        else:
            current = ch
            count = 1
        if count >= run_len:
            return True
    return False


def classify_record(
    record: TokenRecord,
    long_byte_threshold: int,
    long_char_threshold: int,
) -> None:
    if record.kind == "special":
        record.categories.add("special")
        return

    if not record.decode_ok:
        record.flags.add("invalid_utf8")
        record.categories.add("invalid_utf8")
    else:
        text = record.text
        if has_hangul(text):
            record.categories.add("hangul")
        if any(("a" <= ch <= "z") or ("A" <= ch <= "Z") for ch in text):
            record.categories.add("english")
        if any(ch.isdigit() for ch in text):
            record.categories.add("digit")
        if any(ch.isspace() for ch in text):
            record.categories.add("whitespace")
            record.flags.add("contains_whitespace")
        if any(unicodedata.category(ch)[0] in {"P", "S"} for ch in text):
            record.categories.add("punct_symbol")
        if any(unicodedata.category(ch)[0] == "C" for ch in text):
            record.categories.add("control")
            record.flags.add("control_char")
        if has_repeated_run(text):
            record.flags.add("repeated_run")
        if not record.categories:
            record.categories.add("other")

    if record.byte_len >= long_byte_threshold:
        record.flags.add("long_bytes")
    if record.decode_ok and record.char_len >= long_char_threshold:
        record.flags.add("long_chars")


def parse_merge_pair(item: Any) -> tuple[int, int] | None:
    if not isinstance(item, dict):
        return None
    value = item.get("value")
    if not isinstance(value, list) or len(value) != 2:
        return None
    left, right = value
    if not isinstance(left, int) or not isinstance(right, int):
        return None
    return left, right


def inspect_vocab(
    vocab_path: Path,
    long_byte_threshold: int,
    long_char_threshold: int,
) -> VocabInspection:
    merges = load_merges(vocab_path)
    expected_size = expected_vocab_size_from_filename(vocab_path)
    structure_errors: list[str] = []
    structure_warnings: list[str] = []
    duplicate_pairs: list[tuple[tuple[int, int], int, int]] = []
    seen_pairs: dict[tuple[int, int], int] = {}
    records_by_id: dict[int, TokenRecord] = {}
    records: list[TokenRecord] = []

    for token_id, token in enumerate(SPECIAL_TOKENS):
        record = TokenRecord(
            token_id=token_id,
            kind="special",
            byte_value=None,
            text=token,
            decode_ok=True,
        )
        classify_record(record, long_byte_threshold, long_char_threshold)
        records_by_id[token_id] = record
        records.append(record)

    for byte_value in range(NUM_BYTES):
        token_id = BYTE_OFFSET + byte_value
        raw = bytes([byte_value])
        text, decode_ok, decode_error = decode_bytes(raw)
        record = TokenRecord(
            token_id=token_id,
            kind="byte",
            byte_value=raw,
            text=text,
            decode_ok=decode_ok,
            decode_error=decode_error,
        )
        classify_record(record, long_byte_threshold, long_char_threshold)
        records_by_id[token_id] = record
        records.append(record)

    for index, item in enumerate(merges):
        token_id = BASE_VOCAB_SIZE + index
        pair = parse_merge_pair(item)

        if not isinstance(item, dict):
            structure_errors.append(f"id {token_id}: merge item is not an object")
        elif item.get("type") != "tuple":
            structure_warnings.append(
                f"id {token_id}: merge type is {item.get('type')!r}, expected 'tuple'"
            )

        if pair is None:
            structure_errors.append(
                f"id {token_id}: merge value must be a two-item integer list"
            )
            record = TokenRecord(
                token_id=token_id,
                kind="merge",
                byte_value=None,
                text="",
                decode_ok=False,
                decode_error="invalid merge pair",
            )
            record.flags.add("invalid_merge")
            record.categories.add("invalid_merge")
            records_by_id[token_id] = record
            records.append(record)
            continue

        left_id, right_id = pair
        if pair in seen_pairs:
            duplicate_pairs.append((pair, seen_pairs[pair], token_id))
        else:
            seen_pairs[pair] = token_id

        missing_ids = [part for part in pair if part not in records_by_id]
        if missing_ids:
            structure_errors.append(
                f"id {token_id}: references unknown token id(s) {missing_ids}"
            )
            byte_value = None
        elif left_id < BYTE_OFFSET or right_id < BYTE_OFFSET:
            structure_errors.append(
                f"id {token_id}: references special token id(s) {pair}"
            )
            byte_value = None
        else:
            left_bytes = records_by_id[left_id].byte_value
            right_bytes = records_by_id[right_id].byte_value
            if left_bytes is None or right_bytes is None:
                structure_errors.append(
                    f"id {token_id}: cannot resolve bytes from pair {pair}"
                )
                byte_value = None
            else:
                byte_value = left_bytes + right_bytes

        text, decode_ok, decode_error = decode_bytes(byte_value)
        record = TokenRecord(
            token_id=token_id,
            kind="merge",
            byte_value=byte_value,
            text=text,
            decode_ok=decode_ok,
            decode_error=decode_error,
            left_id=left_id,
            right_id=right_id,
        )
        classify_record(record, long_byte_threshold, long_char_threshold)
        records_by_id[token_id] = record
        records.append(record)

    actual_vocab_size = len(records)
    if expected_size is not None and expected_size != actual_vocab_size:
        structure_warnings.append(
            f"filename suggests vocab size {expected_size}, "
            f"but restored size is {actual_vocab_size}"
        )

    return VocabInspection(
        records=records,
        merges_count=len(merges),
        expected_vocab_size=expected_size,
        structure_errors=structure_errors,
        structure_warnings=structure_warnings,
        duplicate_pairs=duplicate_pairs,
    )


def compact_json_string(text: str, limit: int = 96) -> str:
    dumped = json.dumps(text, ensure_ascii=False)
    if len(dumped) <= limit:
        return dumped
    return dumped[: limit - 4] + '..."'


def markdown_code(text: str) -> str:
    escaped = html.escape(text).replace("|", "&#124;")
    return f"<code>{escaped}</code>"


def display_record(record: TokenRecord, limit: int = 96) -> str:
    if record.kind == "special":
        return markdown_code(record.text)
    if not record.decode_ok:
        hex_text = record.byte_hex or "unresolved"
        return markdown_code(f"<invalid utf-8: {hex_text}>")
    return markdown_code(compact_json_string(record.text, limit=limit))


def csv_safe_text(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)[1:-1]


def markdown_table(records: list[TokenRecord], include_flags: bool = True) -> str:
    headers = ["id", "kind", "byte_len", "char_len", "token", "hex"]
    if include_flags:
        headers.append("flags")
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for record in records:
        row = [
            str(record.token_id),
            record.kind,
            str(record.byte_len),
            str(record.char_len),
            display_record(record),
            markdown_code(record.byte_hex[:120] + (" ..." if len(record.byte_hex) > 120 else "")),
        ]
        if include_flags:
            row.append(", ".join(sorted(record.flags)) or "-")
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def write_tokens_csv(records: list[TokenRecord], out_path: Path) -> None:
    fieldnames = [
        "id",
        "kind",
        "text",
        "repr",
        "byte_len",
        "char_len",
        "byte_hex",
        "left_id",
        "right_id",
        "flags",
        "categories",
        "decode_ok",
        "decode_error",
    ]
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "id": record.token_id,
                    "kind": record.kind,
                    "text": csv_safe_text(record.text) if record.decode_ok else "",
                    "repr": repr(record.text) if record.decode_ok else repr(record.byte_value),
                    "byte_len": record.byte_len,
                    "char_len": record.char_len,
                    "byte_hex": record.byte_hex,
                    "left_id": "" if record.left_id is None else record.left_id,
                    "right_id": "" if record.right_id is None else record.right_id,
                    "flags": ";".join(sorted(record.flags)),
                    "categories": ";".join(sorted(record.categories)),
                    "decode_ok": record.decode_ok,
                    "decode_error": record.decode_error,
                }
            )


def category_counts(records: list[TokenRecord]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for record in records:
        for category in record.categories:
            counts[category] += 1
    return counts


def kind_counts(records: list[TokenRecord]) -> Counter[str]:
    return Counter(record.kind for record in records)


def render_count_lines(counts: Counter[str], total: int) -> list[str]:
    lines: list[str] = []
    for key, count in counts.most_common():
        pct = (count / total * 100.0) if total else 0.0
        lines.append(f"- {key}: {count} ({pct:.1f}%)")
    return lines


def write_summary(inspection: VocabInspection, out_dir: Path) -> None:
    records = inspection.records
    total = len(records)
    non_special = [record for record in records if record.kind != "special"]
    invalid = [record for record in non_special if "invalid_utf8" in record.flags]
    control = [record for record in non_special if "control_char" in record.flags]
    long_bytes = [record for record in non_special if "long_bytes" in record.flags]
    long_chars = [record for record in non_special if "long_chars" in record.flags]
    repeated = [record for record in non_special if "repeated_run" in record.flags]
    cats = category_counts(records)
    kinds = kind_counts(records)

    lines = [
        "# BPE Vocabulary Inspection Summary",
        "",
        "## Files",
        "",
        "- `tokens.csv`: full token table",
        "- `length_distribution.png`: byte and character length histograms",
        "- `category_distribution.png`: token category counts",
        "- `long_tokens.md`: longest token samples",
        "- `invalid_tokens.md`: invalid UTF-8 and control-character samples",
        "- `sample_tokens.md`: samples by token ID region",
        "- `structure_issues.md`: structure validation details",
        "",
        "## Size",
        "",
        f"- restored vocab size: {total}",
        f"- merge count: {inspection.merges_count}",
        f"- base special+byte tokens: {BASE_VOCAB_SIZE}",
    ]
    if inspection.expected_vocab_size is not None:
        lines.append(f"- filename expected vocab size: {inspection.expected_vocab_size}")
    lines.extend(
        [
            "",
            "Category counts are non-exclusive because one token can contain multiple character types.",
            "Invalid UTF-8 counts include byte-level pieces that are expected in a byte BPE vocab.",
            "",
            "## Warnings",
            "",
            f"- structure errors: {len(inspection.structure_errors)}",
            f"- structure warnings: {len(inspection.structure_warnings)}",
            f"- duplicate merge pairs: {len(inspection.duplicate_pairs)}",
            f"- invalid UTF-8 tokens: {len(invalid)}",
            f"- control-character tokens: {len(control)}",
            f"- long byte tokens: {len(long_bytes)}",
            f"- long character tokens: {len(long_chars)}",
            f"- repeated-run tokens: {len(repeated)}",
            "",
            "## Token Kinds",
            "",
        ]
    )
    lines.extend(render_count_lines(kinds, total))
    lines.extend(["", "## Token Categories", ""])
    lines.extend(render_count_lines(cats, total))

    top_long = sorted(non_special, key=lambda record: record.byte_len, reverse=True)[:10]
    lines.extend(["", "## Longest Tokens Preview", ""])
    lines.append(markdown_table(top_long))

    out_path = out_dir / "summary.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_long_tokens(inspection: VocabInspection, out_dir: Path, top_n: int) -> None:
    non_special = [record for record in inspection.records if record.kind != "special"]
    by_bytes = sorted(non_special, key=lambda record: record.byte_len, reverse=True)[:top_n]
    by_chars = sorted(non_special, key=lambda record: record.char_len, reverse=True)[:top_n]
    repeated = [
        record for record in non_special if "repeated_run" in record.flags
    ][:top_n]

    lines = [
        "# Long Token Report",
        "",
        f"Showing up to {top_n} rows per section. See `tokens.csv` for the full table.",
        "",
        "## Longest By Byte Length",
        "",
        markdown_table(by_bytes),
        "",
        "## Longest By Character Length",
        "",
        markdown_table(by_chars),
        "",
        "## Repeated Character Runs",
        "",
        markdown_table(repeated),
    ]
    (out_dir / "long_tokens.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_invalid_tokens(inspection: VocabInspection, out_dir: Path, top_n: int) -> None:
    non_special = [record for record in inspection.records if record.kind != "special"]
    invalid = [record for record in non_special if "invalid_utf8" in record.flags][:top_n]
    control = [record for record in non_special if "control_char" in record.flags][:top_n]
    whitespace = [
        record for record in non_special if "contains_whitespace" in record.flags
    ][:top_n]

    lines = [
        "# Invalid and Hard-To-Display Tokens",
        "",
        f"Showing up to {top_n} rows per section. See `tokens.csv` for the full table.",
        "",
        "## Invalid UTF-8",
        "",
        markdown_table(invalid),
        "",
        "## Control Characters",
        "",
        markdown_table(control),
        "",
        "## Whitespace Tokens",
        "",
        markdown_table(whitespace),
    ]
    (out_dir / "invalid_tokens.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def sample_ranges(records: list[TokenRecord], top_n: int) -> list[tuple[str, list[TokenRecord]]]:
    by_id = {record.token_id: record for record in records}
    merge_ids = [record.token_id for record in records if record.kind == "merge"]
    samples: list[tuple[str, list[TokenRecord]]] = []

    byte_sample_ids = list(range(BYTE_OFFSET, min(BASE_VOCAB_SIZE, BYTE_OFFSET + top_n)))
    samples.append(("Byte Tokens", [by_id[token_id] for token_id in byte_sample_ids]))

    if merge_ids:
        first = merge_ids[:top_n]
        middle_start = max(0, len(merge_ids) // 2 - top_n // 2)
        middle = merge_ids[middle_start : middle_start + top_n]
        last = merge_ids[-top_n:]
        samples.append(("Early Merge Tokens", [by_id[token_id] for token_id in first]))
        samples.append(("Middle Merge Tokens", [by_id[token_id] for token_id in middle]))
        samples.append(("Late Merge Tokens", [by_id[token_id] for token_id in last]))

    return samples


def write_sample_tokens(inspection: VocabInspection, out_dir: Path, top_n: int) -> None:
    lines = [
        "# Token Samples By ID Region",
        "",
        f"Showing up to {top_n} rows per section.",
    ]
    for title, rows in sample_ranges(inspection.records, top_n):
        lines.extend(["", f"## {title}", "", markdown_table(rows)])
    (out_dir / "sample_tokens.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def write_structure_issues(inspection: VocabInspection, out_dir: Path, top_n: int) -> None:
    lines = [
        "# Structure Issues",
        "",
        "## Errors",
        "",
    ]
    if inspection.structure_errors:
        lines.extend(f"- {error}" for error in inspection.structure_errors[:top_n])
        if len(inspection.structure_errors) > top_n:
            lines.append(f"- ... {len(inspection.structure_errors) - top_n} more")
    else:
        lines.append("- none")

    lines.extend(["", "## Warnings", ""])
    if inspection.structure_warnings:
        lines.extend(f"- {warning}" for warning in inspection.structure_warnings[:top_n])
        if len(inspection.structure_warnings) > top_n:
            lines.append(f"- ... {len(inspection.structure_warnings) - top_n} more")
    else:
        lines.append("- none")

    lines.extend(["", "## Duplicate Merge Pairs", ""])
    if inspection.duplicate_pairs:
        lines.append("| pair | first_id | duplicate_id |")
        lines.append("| --- | --- | --- |")
        for pair, first_id, duplicate_id in inspection.duplicate_pairs[:top_n]:
            lines.append(f"| `{pair}` | {first_id} | {duplicate_id} |")
        if len(inspection.duplicate_pairs) > top_n:
            lines.append(
                f"| ... | ... | {len(inspection.duplicate_pairs) - top_n} more |"
            )
    else:
        lines.append("- none")

    (out_dir / "structure_issues.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def write_charts(inspection: VocabInspection, out_dir: Path) -> list[str]:
    try:
        os.environ.setdefault(
            "MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "bpe_vocab_mplconfig")
        )
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as exc:
        return [f"matplotlib is unavailable: {exc}"]

    records = [record for record in inspection.records if record.kind != "special"]
    byte_lengths = [record.byte_len for record in records]
    char_lengths = [record.char_len for record in records if record.decode_ok]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].hist(byte_lengths, bins=50, color="#3b82f6", edgecolor="white")
    axes[0].set_title("Byte Length Distribution")
    axes[0].set_xlabel("byte length")
    axes[0].set_ylabel("token count")
    axes[1].hist(char_lengths, bins=50, color="#16a34a", edgecolor="white")
    axes[1].set_title("Character Length Distribution")
    axes[1].set_xlabel("character length")
    axes[1].set_ylabel("token count")
    fig.tight_layout()
    fig.savefig(out_dir / "length_distribution.png", dpi=160)
    plt.close(fig)

    cats = category_counts(inspection.records)
    ordered_categories = [
        "hangul",
        "english",
        "digit",
        "punct_symbol",
        "whitespace",
        "control",
        "invalid_utf8",
        "other",
        "special",
    ]
    labels = [category for category in ordered_categories if cats.get(category, 0)]
    values = [cats[category] for category in labels]

    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.bar(labels, values, color="#0f766e")
    ax.set_title("Token Category Counts")
    ax.set_xlabel("category")
    ax.set_ylabel("token count")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    fig.savefig(out_dir / "category_distribution.png", dpi=160)
    plt.close(fig)
    return []


def write_reports(inspection: VocabInspection, out_dir: Path, top_n: int) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    write_tokens_csv(inspection.records, out_dir / "tokens.csv")
    write_summary(inspection, out_dir)
    write_long_tokens(inspection, out_dir, top_n)
    write_invalid_tokens(inspection, out_dir, top_n)
    write_sample_tokens(inspection, out_dir, top_n)
    write_structure_issues(inspection, out_dir, top_n)
    return write_charts(inspection, out_dir)


def print_terminal_summary(
    inspection: VocabInspection, out_dir: Path, chart_warnings: list[str]
) -> None:
    records = inspection.records
    invalid_count = sum(1 for record in records if "invalid_utf8" in record.flags)
    control_count = sum(1 for record in records if "control_char" in record.flags)
    long_count = sum(1 for record in records if "long_bytes" in record.flags)

    print("BPE vocab inspection complete")
    print(f"- restored vocab size: {len(records)}")
    print(f"- merge count: {inspection.merges_count}")
    if inspection.expected_vocab_size is not None:
        print(f"- filename expected vocab size: {inspection.expected_vocab_size}")
    print(f"- structure errors: {len(inspection.structure_errors)}")
    print(f"- structure warnings: {len(inspection.structure_warnings)}")
    print(f"- duplicate merge pairs: {len(inspection.duplicate_pairs)}")
    print(f"- invalid UTF-8 tokens: {invalid_count}")
    print(f"- control-character tokens: {control_count}")
    print(f"- long byte tokens: {long_count}")
    for warning in chart_warnings:
        print(f"- chart warning: {warning}")
    print(f"- report directory: {out_dir}")
    print(f"- summary: {out_dir / 'summary.md'}")


def main() -> int:
    args = parse_args()
    try:
        inspection = inspect_vocab(
            args.vocab,
            long_byte_threshold=args.long_byte_threshold,
            long_char_threshold=args.long_char_threshold,
        )
        chart_warnings = write_reports(inspection, args.out, args.top_n)
        print_terminal_summary(inspection, args.out, chart_warnings)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
