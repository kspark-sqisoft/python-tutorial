"""
정답 05 — 제너레이터 파이프라인

각 처리 단계를 제너레이터로 구성해 파이프라인을 만든다.
1단계: split() 으로 단어 분리
2단계: len(word) % 2 == 0 으로 짝수 길이 필터
3단계: upper() 로 대문자 변환
마지막에 list() 로 수집한다.
"""

sentences = ["Hello Python", "Go home now", "the big red fox"]

# 제너레이터 파이프라인으로 구현
def split_sentences(sents):
    for sent in sents:
        for word in sent.split():
            yield word

def filter_even_len(words):
    for word in words:
        if len(word) % 2 == 0:
            yield word

def to_upper(words):
    for word in words:
        yield word.upper()

result = list(to_upper(filter_even_len(split_sentences(sentences))))

# ──── 검증 (수정 금지) ────
expected = ["PYTHON", "GO", "HOME"]
assert result == expected, \
    f"결과가 올바르지 않습니다.\n기대: {expected}\n실제: {result}"
print("OK")
