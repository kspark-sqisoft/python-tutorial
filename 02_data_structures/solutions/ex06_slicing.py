"""
풀이 06: 슬라이싱으로 회문 검사.

s[::-1] 은 step=-1 슬라이싱으로 문자열을 역순으로 복사한다.
s == s[::-1] 비교 한 줄이 회문 여부를 완전히 결정한다.
별도 루프나 reversed() 변환 없이 파이썬 슬라이싱만으로 가장 간결하게 표현한 방식이다.
"""

s = "racecar"
is_palindrome = s == s[::-1]

assert is_palindrome is True
assert "racecar"[::-1] == "racecar"
print("OK")
