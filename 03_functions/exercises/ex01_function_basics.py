"""
연습문제 01 — 함수 기본
TODO: abs_value(x) 함수를 완성하세요.
- x 가 음수이면 -x 를 반환
- x 가 0 이면 0 을 반환
- x 가 양수이면 x 를 반환
- 내장 abs() 사용 금지, 조건 분기만 사용
"""


def abs_value(x):
    # TODO: 구현하세요
    pass


# ── 검증 (수정하지 마세요) ──
assert abs_value(-5) == 5,  "음수 테스트 실패"
assert abs_value(0)  == 0,  "0 테스트 실패"
assert abs_value(7)  == 7,  "양수 테스트 실패"
assert abs_value(-0.5) == 0.5, "소수 음수 테스트 실패"
print("OK")
