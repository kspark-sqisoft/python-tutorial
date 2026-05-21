"""
연습문제 05 — 제너레이터 파이프라인
주어진 문장 리스트를 단어 분리 → 짝수 길이 필터 → 대문자 변환
순서로 처리해 result 리스트를 만든다.
"""

sentences = ["Hello Python", "Go home now", "the big red fox"]

# ──── TODO ────
# 아래 세 단계를 제너레이터 체인 또는 리스트 컴프리헨션으로 구현하라.
# 단계 1: 각 문장을 단어로 분리 (split)
# 단계 2: 짝수 길이(len % 2 == 0)인 단어만 통과
# 단계 3: 대문자(upper)로 변환
# 최종 결과를 result 리스트에 저장

result = []  # TODO

# ──── 검증 (수정 금지) ────
expected = ["PYTHON", "GO", "HOME"]
assert result == expected, \
    f"결과가 올바르지 않습니다.\n기대: {expected}\n실제: {result}"
print("OK")
