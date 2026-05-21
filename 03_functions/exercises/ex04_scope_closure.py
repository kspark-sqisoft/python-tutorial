"""
연습문제 04 — 스코프 / 클로저
TODO: make_adder(n) 클로저를 완성하세요.
- make_adder(n) 은 "x 에 n 을 더하는 함수"를 반환해야 합니다.
- 예: add_5 = make_adder(5) 후 add_5(3) == 8
"""


def make_adder(n):
    # TODO: 내부 함수를 정의하고 반환하세요
    pass


# ── 검증 (수정하지 마세요) ──
add_5 = make_adder(5)
add_10 = make_adder(10)

assert add_5(3)   == 8,  "add_5(3) 실패"
assert add_5(0)   == 5,  "add_5(0) 실패"
assert add_10(7)  == 17, "add_10(7) 실패"
assert add_5(3) != add_10(3), "독립성 실패"
print("OK")
