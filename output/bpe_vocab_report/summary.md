# BPE Vocabulary Inspection Summary

## Files

- `tokens.csv`: full token table
- `length_distribution.png`: byte and character length histograms
- `category_distribution.png`: token category counts
- `long_tokens.md`: longest token samples
- `invalid_tokens.md`: invalid UTF-8 and control-character samples
- `sample_tokens.md`: samples by token ID region
- `structure_issues.md`: structure validation details

## Size

- restored vocab size: 10000
- merge count: 9740
- base special+byte tokens: 260
- filename expected vocab size: 3000

Category counts are non-exclusive because one token can contain multiple character types.
Invalid UTF-8 counts include byte-level pieces that are expected in a byte BPE vocab.

## Warnings

- structure errors: 0
- structure warnings: 1
- duplicate merge pairs: 0
- invalid UTF-8 tokens: 830
- control-character tokens: 609
- long byte tokens: 3
- long character tokens: 6
- repeated-run tokens: 172

## Token Kinds

- merge: 9740 (97.4%)
- byte: 256 (2.6%)
- special: 4 (0.0%)

## Token Categories

- hangul: 8707 (87.1%)
- whitespace: 5200 (52.0%)
- invalid_utf8: 830 (8.3%)
- punct_symbol: 711 (7.1%)
- control: 609 (6.1%)
- english: 184 (1.8%)
- digit: 158 (1.6%)
- special: 4 (0.0%)

## Longest Tokens Preview

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 4529 | merge | 48 | 16 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3  ...</code> | long_bytes, long_chars, repeated_run |
| 7119 | merge | 48 | 16 | <code>&quot;ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3  ...</code> | long_bytes, long_chars, repeated_run |
| 9404 | merge | 32 | 32 | <code>&quot;................................&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e</code> | long_bytes, long_chars, repeated_run |
| 6603 | merge | 28 | 12 | <code>&quot;강추@강추@강추@강추@&quot;</code> | <code>ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40</code> | - |
| 3466 | merge | 25 | 9 | <code>&quot; ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>20 e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | contains_whitespace, repeated_run |
| 7835 | merge | 25 | 11 | <code>&quot;tv 전기세가 아깝다&quot;</code> | <code>74 76 20 ec a0 84 ea b8 b0 ec 84 b8 ea b0 80 20 ec 95 84 ea b9 9d eb 8b a4</code> | contains_whitespace |
| 1282 | merge | 24 | 8 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 3594 | merge | 24 | 8 | <code>&quot;ㅠㅠㅠㅠㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0</code> | repeated_run |
| 8323 | merge | 24 | 10 | <code>&quot; 여운이 남는 영화&quot;</code> | <code>20 ec 97 ac ec 9a b4 ec 9d b4 20 eb 82 a8 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 5486 | merge | 23 | 9 | <code>&quot; 처음부터 끝까지&quot;</code> | <code>20 ec b2 98 ec 9d 8c eb b6 80 ed 84 b0 20 eb 81 9d ea b9 8c ec a7 80</code> | contains_whitespace |
