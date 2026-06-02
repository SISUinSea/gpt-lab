# BPE vocab 검증/시각화 프로그램 구현 계획

## 1. 목표

`data/bpe_tokenizer_vocab3000.json`에 저장된 byte-level BPE merge rule을 복원해서 실제 vocab token을 사람이 확인할 수 있게 만든다.

검증할 질문은 다음과 같다.

- vocab 파일 구조가 `src/bpe.py`의 저장/로드 규칙과 일치하는가?
- 생성된 token이 UTF-8 문자열로 정상 복원되는가?
- token 길이가 과도하게 긴 항목은 없는가?
- 한글/영문/숫자/기호/공백/제어문자 token 비율은 적절한가?
- 사람이 보기에 의미 있는 조각 또는 단어에 가까운 token이 어느 정도인가?
- 파일명은 `vocab3000`이지만 실제 merge 수와 vocab 크기가 기대와 일치하는가?

## 2. 프로그램 형태

우선 CLI 기반 리포트 생성 프로그램으로 만든다.

- 파일 위치: `scripts/inspect_bpe_vocab.py`
- 기본 입력: `data/bpe_tokenizer_vocab3000.json`
- 기본 출력 디렉터리: `output/bpe_vocab_report/`
- 실행 예:

```bash
python3 scripts/inspect_bpe_vocab.py \
  --vocab data/bpe_tokenizer_vocab3000.json \
  --out output/bpe_vocab_report
```

프로그램은 터미널 요약을 출력하고, 자세한 결과는 파일로 저장한다.

## 3. 입력 데이터 해석 방식

현재 vocab JSON은 다음 구조다.

```json
{
  "merges": [
    {"type": "tuple", "value": [36, 240]}
  ]
}
```

복원 규칙은 `src/bpe.py`와 맞춘다.

- ID `0~3`: `<pad>`, `<unk>`, `<bos>`, `<eos>`
- ID `4~259`: 원본 byte `0~255`
- ID `260 + merge_index`: 해당 순서의 merge token
- merge token은 왼쪽/오른쪽 token ID를 재귀적으로 byte sequence로 펼친다.
- byte sequence는 마지막에 한 번만 UTF-8 decode를 시도한다.

## 4. 1차 검증 항목

### 파일 구조 검증

- JSON 파싱 가능 여부
- 최상위 `merges` 필드 존재 여부
- 각 merge 항목이 `{"type": "tuple", "value": [int, int]}` 형태인지 확인
- merge에서 참조하는 token ID가 해당 시점에 이미 존재하는지 확인
- 중복 merge pair 개수 확인
- 실제 vocab 크기 계산: `260 + len(merges)`
- 파일명/기대값 `3000`과 실제 vocab 크기 차이 표시

### UTF-8 복원 검증

- 각 token을 byte sequence로 재귀 복원
- UTF-8 decode 성공/실패 개수 집계
- 실패 token은 `hex`와 참조 ID를 함께 저장
- decode는 되지만 제어문자만 있거나 화면 표시가 어려운 token을 별도 분류

### token 품질 지표

- byte 길이 분포
- 글자 수 분포
- 한글 포함 token 비율
- 영문 포함 token 비율
- 숫자 포함 token 비율
- 기호/문장부호 포함 token 비율
- 공백/개행 포함 token 비율
- 제어문자 포함 token 비율
- 긴 token 상위 목록
- 반복 문자 token 목록 예: `ㅋㅋㅋㅋ`, `!!!!!`, `...`
- 의미 해석이 어려운 깨진 조각 후보 목록

## 5. 시각화 산출물

`matplotlib`만 사용해서 정적 이미지와 Markdown 리포트를 만든다.

- `summary.md`
  - 전체 vocab 크기
  - merge 수
  - 오류/경고 요약
  - 카테고리별 비율
  - 사람이 직접 봐야 할 token 샘플
- `tokens.csv`
  - `id`
  - `kind`
  - `text`
  - `repr`
  - `byte_len`
  - `char_len`
  - `byte_hex`
  - `left_id`
  - `right_id`
  - `flags`
- `length_distribution.png`
  - byte 길이와 글자 수 히스토그램
- `category_distribution.png`
  - 한글/영문/숫자/기호/공백/제어문자 카테고리 막대그래프
- `long_tokens.md`
  - 긴 token 상위 N개
- `invalid_tokens.md`
  - UTF-8 decode 실패 token과 제어문자 token
- `sample_tokens.md`
  - ID 구간별 token 샘플: byte token, 초기 merge, 중간 merge, 후반 merge
- `structure_issues.md`
  - 구조 오류, 파일명/실제 vocab 크기 불일치, 중복 merge pair 목록

## 6. 사람이 보는 화면 구성

Markdown 리포트는 다음 순서로 읽히게 만든다.

1. 전체 요약: vocab 크기, merge 수, 경고 개수
2. 구조 문제: 참조 오류, 중복 merge, 기대 vocab 크기 불일치
3. 품질 문제: 너무 긴 token, 표시 불가 token, 제어문자 token
4. 분포 차트: 길이/카테고리별 편향 확인
5. 샘플 검토: 정상으로 보이는 token과 의심 token을 나란히 확인

## 7. 구현 순서

1. JSON 로더 작성
   - `--vocab`, `--out`, `--top-n` CLI 옵션을 받는다.
   - 출력 디렉터리를 생성한다.

2. vocab 복원기 작성
   - special token과 byte token을 초기화한다.
   - merge 순서대로 token ID를 생성한다.
   - 각 token의 원본 byte sequence를 재귀적으로 계산한다.

3. 구조 검증 작성
   - merge 형식 오류, 참조 오류, 중복 merge를 수집한다.
   - 실제 vocab 크기와 파일명 기대값을 비교한다.

4. token 분석기 작성
   - UTF-8 decode 결과, byte 길이, 글자 수, 문자 카테고리, 위험 flag를 계산한다.
   - `tokens.csv`로 모든 token을 저장한다.

5. 리포트 작성기 구현
   - `summary.md`, `long_tokens.md`, `invalid_tokens.md`, `sample_tokens.md`를 생성한다.
   - 경고가 있으면 터미널 출력에도 요약한다.

6. 차트 생성기 구현
   - `matplotlib`으로 길이 분포와 카테고리 분포 이미지를 저장한다.
   - GUI 없이 실행되도록 `Agg` backend를 사용한다.

7. 검증 실행
   - 실제 `data/bpe_tokenizer_vocab3000.json`에 대해 실행한다.
   - 생성된 리포트에서 즉시 눈에 띄는 문제를 확인한다.
   - 필요하면 긴 token 기준값과 샘플 개수를 조정한다.

## 8. 구현 시 주의점

- byte-level BPE이므로 token이 항상 완성된 한국어 단어일 필요는 없다.
- UTF-8 byte 조각은 초기 merge 단계에서 decode가 실패할 수 있으므로, 실패 자체를 무조건 오류로 보지 않고 "표시 불가 token"으로 분류한다.
- 최종 품질 판단은 자동 점수만으로 확정하지 않고, 의심 목록을 사람이 검토할 수 있게 만든다.
- 외부 tokenizer 라이브러리는 사용하지 않는다.
- 프로젝트 허용 라이브러리 범위에 맞춰 표준 라이브러리와 `matplotlib`만 사용한다.

## 9. 다음 단계

이 계획대로 `scripts/inspect_bpe_vocab.py`를 구현한 뒤, 실제 vocab 파일을 분석해서 `output/bpe_vocab_report/summary.md`를 기준으로 vocab 품질을 판단한다.
