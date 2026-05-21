"""
정답 04 — 스코프 / 클로저
왜 이렇게 구현하나:
- make_adder 는 n 을 캡처한 내부 함수 adder 를 반환한다.
- 각 make_adder 호출마다 독립적인 n 이 캡처되므로 add_5 와 add_10 은 서로 영향을 주지 않는다.
- nonlocal 없이도 n 을 읽기만 하므로 단순 클로저로 충분하다.
"""


def make_adder(n):
    def adder(x):
        return x + n   # 둘러싼 함수의 n 을 캡처해 사용
    return adder


add_5  = make_adder(5)
add_10 = make_adder(10)

assert add_5(3)   == 8
assert add_5(0)   == 5
assert add_10(7)  == 17
assert add_5(3) != add_10(3)
print("OK")
