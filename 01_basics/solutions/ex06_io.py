"""
정답 06 — f-string 정렬 포맷팅

f-string 의 정렬 지정자 :<너비> (왼쪽), :>너비 (오른쪽) 를 조합해
고정 너비 열 정렬을 한 줄로 표현한다.
name 은 5칸 왼쪽 정렬이므로 "Kee  " (뒤 공백 2개),
score 는 3칸 오른쪽 정렬이므로 " 95" (앞 공백 1개) 가 된다.
이 패턴은 터미널 표, 로그 출력, 보고서 등에서 자주 쓰인다.
"""

name  = "Kee"
score = 95

result = f"이름: {name:<6}| 점수: {score:>3}"

assert isinstance(result, str)
assert result == "이름: Kee   | 점수:  95"

print("OK")
