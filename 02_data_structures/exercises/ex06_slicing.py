"""
연습문제 06: 슬라이싱으로 회문 검사.
문자열이 앞뒤로 같은지(회문인지) 슬라이싱만으로 판별하라.
"""

s = "racecar"

# TODO: s 가 회문인지 슬라이싱으로 검사한 bool 값 is_palindrome 을 만드세요.
#       회문 조건: 문자열이 뒤집어도 같다 → s == s[::-1]
is_palindrome = None

# ── 검증 ──
assert is_palindrome is True, f"is_palindrome 이 올바르지 않습니다: {is_palindrome}"
assert "racecar"[::-1] == "racecar", "슬라이싱 역순 로직을 확인하세요"
print("OK")
