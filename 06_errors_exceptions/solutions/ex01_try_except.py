"""
해설 — parse_numbers

핵심 이유:
  int() 변환을 시도하고 ValueError 가 나면 continue 로 건너뛴다.
  변환 가능한 항목만 결과 리스트에 추가하는 전형적인 EAFP 패턴이다.
  변환 불가 항목을 미리 검사(LBYL)하는 것보다 try/except 가 더 파이썬답다.
"""


def parse_numbers(strings):
    result = []
    for s in strings:
        try:
            result.append(int(s))
        except ValueError:
            # 변환할 수 없는 항목은 조용히 건너뜀
            continue
    return result


# ── 검증 ──
result = parse_numbers(["1", "2", "abc", "3"])
assert result == [1, 2, 3], f"예상 [1, 2, 3], 실제 {result}"

result2 = parse_numbers(["hello", "world"])
assert result2 == [], f"예상 [], 실제 {result2}"

result3 = parse_numbers(["-5", "0", "10", "xyz", "7"])
assert result3 == [-5, 0, 10, 7], f"예상 [-5, 0, 10, 7], 실제 {result3}"

print("OK")
