"""
제너레이터 파이프라인 — 제너레이터를 다른 제너레이터에 연결해
데이터 처리 단계를 구성한다. 각 단계는 한 줄씩 데이터를 흘려
메모리를 효율적으로 사용한다.
"""

# ──── 1. 파이프라인 개념 ────

# 파이프라인: 여러 처리 단계를 체인으로 연결
# 각 제너레이터는 앞 단계에서 값을 하나씩 받아 처리 후 다음 단계로 넘긴다
# 전체 데이터를 한 번에 메모리에 올리지 않는다

# ──── 2. 단계별 제너레이터 함수 ────

def read_lines(lines):
    """소스: 줄 리스트를 하나씩 yield."""
    for line in lines:
        yield line

def filter_empty(lines):
    """빈 줄(공백만 있는 줄)을 제거한다."""
    for line in lines:
        if line.strip():       # 공백 제거 후 내용이 있으면
            yield line

def split_words(lines):
    """각 줄을 단어로 분리해 하나씩 yield."""
    for line in lines:
        for word in line.split():
            yield word

def filter_long(words, min_len=3):
    """최소 길이 이상인 단어만 통과시킨다."""
    for word in words:
        if len(word) >= min_len:
            yield word

def to_upper(words):
    """단어를 모두 대문자로 변환해 yield."""
    for word in words:
        yield word.upper()

# ──── 3. 파이프라인 조립 ────

# 각 단계를 앞 단계의 출력에 연결 — 데이터가 필요할 때만 흐른다
raw_text = [
    "파이썬은 배우기 쉬운 언어입니다",
    "   ",                            # 빈 줄 — 필터 단계에서 제거
    "제너레이터는 메모리를 아낍니다",
    "",                               # 빈 줄
    "이터레이터 프로토콜을 이해하면 좋습니다",
]

stage1 = read_lines(raw_text)         # 소스
stage2 = filter_empty(stage1)         # 빈 줄 제거
stage3 = split_words(stage2)          # 단어 분리
stage4 = filter_long(stage3, 2)       # 짧은 단어 제거
stage5 = to_upper(stage4)             # 대문자 변환

print("파이프라인 결과:")
result_words = list(stage5)
print(result_words)
print(f"총 단어 수: {len(result_words)}")

# ──── 4. 함수로 파이프라인 구성 ────

def build_pipeline(lines):
    """파이프라인을 한 함수에서 조립해 반환한다."""
    lines   = filter_empty(lines)
    words   = split_words(lines)
    words   = filter_long(words, min_len=3)
    words   = to_upper(words)
    return words

print("\nbuild_pipeline 사용:")
pipeline = build_pipeline(iter(raw_text))
for w in pipeline:
    print(" ", w, end="")
print()

# ──── 5. 집계로 마무리 ────

# 파이프라인 끝에 집계 함수를 붙이면 결과 하나로 요약된다
total_chars = sum(
    len(word)
    for word in build_pipeline(iter(raw_text))
)
print(f"\n모든 단어 문자 수 합계: {total_chars}")


if __name__ == "__main__":
    print("\n=== 데모: 가짜 텍스트 파이프라인 ===")

    fake_text = [
        "Hello world this is Python",
        "",
        "Generators save memory",
        "   ",
        "the quick brown fox jumps",
    ]

    # 파이프라인: 빈 줄 제거 → 단어 분리 → 길이 4 이상 → 대문자
    pipeline = to_upper(
        filter_long(
            split_words(
                filter_empty(iter(fake_text))
            ),
            min_len=4,
        )
    )

    words = list(pipeline)
    print("결과 단어:", words)
    print("단어 수:", len(words))
