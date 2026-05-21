"""
정답 05 — 제어흐름 (for + if)

빈 리스트를 만들고 range(1, 21) 을 순회하며 짝수만 append 하는 것이
가장 명시적인 방법이다. 같은 결과를 리스트 컴프리헨션
[n for n in range(1, 21) if n % 2 == 0] 으로도 쓸 수 있지만,
이 단계에서는 for + if 의 흐름을 직접 체험하는 것이 목적이다.
"""

evens = []
for n in range(1, 21):
    if n % 2 == 0:
        evens.append(n)

assert isinstance(evens, list)
assert len(evens) == 10
assert evens[0] == 2
assert evens[-1] == 20
assert all(n % 2 == 0 for n in evens)

print("OK")
