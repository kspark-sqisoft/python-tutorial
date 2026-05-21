"""
정답 01 — 함수 기본 / abs_value
왜 이렇게 구현하나:
- 조건 분기(if/elif/else)로 음수·0·양수 세 경우를 명시적으로 처리한다.
- 내장 abs() 대신 직접 구현해 함수 정의와 return 흐름을 연습한다.
"""


def abs_value(x):
    if x < 0:
        return -x
    return x   # 0 과 양수는 그대로 반환


assert abs_value(-5)  == 5
assert abs_value(0)   == 0
assert abs_value(7)   == 7
assert abs_value(-0.5) == 0.5
print("OK")
