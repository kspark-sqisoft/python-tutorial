"""
연습문제 03 — 문자열 메서드

주어진 문자열 "  Hello, World  " 를 아래 순서로 처리하세요:
  1. strip() 으로 양쪽 공백 제거
  2. lower() 로 소문자 변환
  3. split(", ") 으로 ", " 기준 분리 → 리스트

결과를 result 에 대입하세요.
모든 assert 가 통과되면 "OK" 가 출력됩니다.
"""

original = "  Hello, World  "

# TODO: strip → lower → split(", ") 을 순서대로 적용해 result 에 대입하세요
result = ...

# ── 채점 (수정 금지) ──
assert isinstance(result, list),        f"result 는 list 이어야 합니다. 현재: {type(result).__name__}"
assert len(result) == 2,               f"리스트 길이는 2 이어야 합니다. 현재: {result!r}"
assert result[0] == "hello",           f"result[0] 은 'hello' 이어야 합니다. 현재: {result[0]!r}"
assert result[1] == "world",           f"result[1] 은 'world' 이어야 합니다. 현재: {result[1]!r}"

print("OK")
