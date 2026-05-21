"""
정답 03 — 문자열 메서드

메서드 체이닝(chaining)으로 strip → lower → split 을 한 줄에 표현한다.
각 메서드는 새 문자열(또는 리스트)을 반환하므로 원본을 변경하지 않는다.
split(", ") 은 정확히 ", " 구분자를 기준으로 나누기 때문에
공백이 포함된 구분자를 그대로 넘겨야 결과가 깔끔하게 분리된다.
"""

original = "  Hello, World  "

result = original.strip().lower().split(", ")

assert isinstance(result, list)
assert len(result) == 2
assert result[0] == "hello"
assert result[1] == "world"

print("OK")
