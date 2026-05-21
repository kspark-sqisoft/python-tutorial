"""
연습문제 06 — f-string 정렬 포맷팅

f-string 한 줄로 아래 형식의 문자열을 만드세요:
  "이름: Kee   | 점수:  95"
  - "이름: " 다음에 name 을 5칸 왼쪽 정렬
  - "| 점수: " 다음에 score 를 3칸 오른쪽 정렬

name = "Kee", score = 95 로 고정합니다.

모든 assert 가 통과되면 "OK" 가 출력됩니다.
"""

name  = "Kee"
score = 95

# TODO: f-string 한 줄로 result 를 만드세요
# 형식: "이름: {name을 6칸 왼쪽 정렬}| 점수: {score를 3칸 오른쪽 정렬}"
result = ...

# ── 채점 (수정 금지) ──
expected = "이름: Kee   | 점수:  95"
assert isinstance(result, str),   f"result 는 str 이어야 합니다. 현재: {type(result).__name__}"
assert result == expected,        f"결과가 다릅니다.\n  기대: {expected!r}\n  실제: {result!r}"

print("OK")
