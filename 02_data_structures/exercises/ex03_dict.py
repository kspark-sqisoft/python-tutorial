"""
연습문제 03: 딕셔너리 단어 빈도 세기.
주어진 문장의 각 단어 등장 횟수를 딕셔너리로 만들어라.
"""

sentence = "the quick brown fox jumps over the lazy dog"

# TODO: sentence 를 단어로 분리하고, 각 단어가 몇 번 등장하는지
#       딕셔너리 freq 로 만드세요.
#       힌트: str.split(), dict.get(key, default)
freq = None

# ── 검증 ──
assert freq is not None, "freq 를 구현하세요"
assert freq["the"] == 2, f"'the' 의 빈도가 올바르지 않습니다: {freq.get('the')}"
assert freq["fox"] == 1, f"'fox' 의 빈도가 올바르지 않습니다: {freq.get('fox')}"
assert freq["dog"] == 1, f"'dog' 의 빈도가 올바르지 않습니다: {freq.get('dog')}"
assert len(freq) == 8, f"고유 단어 수가 올바르지 않습니다: {len(freq)}"
print("OK")
