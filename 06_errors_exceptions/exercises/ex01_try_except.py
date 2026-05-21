"""
연습문제 01 — try/except 로 안전한 변환

parse_numbers(strings) 함수를 완성하세요.
- 문자열 리스트를 받아 int 로 변환 가능한 것만 골라 리스트로 반환합니다.
- 변환할 수 없는 항목은 조용히 건너뜁니다.
- 예: parse_numbers(["1", "2", "abc", "3"]) == [1, 2, 3]
"""


def parse_numbers(strings):
    # TODO: 구현하세요
    pass


# ── 검증 ──
result = parse_numbers(["1", "2", "abc", "3"])
assert result == [1, 2, 3], f"예상 [1, 2, 3], 실제 {result}"

result2 = parse_numbers(["hello", "world"])
assert result2 == [], f"예상 [], 실제 {result2}"

result3 = parse_numbers(["-5", "0", "10", "xyz", "7"])
assert result3 == [-5, 0, 10, 7], f"예상 [-5, 0, 10, 7], 실제 {result3}"

print("OK")
