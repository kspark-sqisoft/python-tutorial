"""
풀이 04 — dataclass

왜 이렇게 풀었나:
frozen=True 를 사용하면 생성 후 필드 변경이 차단되고, Python 이 자동으로 __hash__ 를
생성해 준다. 덕분에 Pt 인스턴스를 set 원소나 dict 키로 사용할 수 있다.
값이 같은 두 인스턴스(p1, p2)는 == True 이고 hash 도 같으므로 set 에서 하나로 합쳐진다.
dataclass 필드 선언에 타입 힌트(int)는 필수다 — 타입 힌트 자체는 10_typing 에서 다룬다.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Pt:
    x: int
    y: int


p1 = Pt(1, 2)
p2 = Pt(1, 2)
p3 = Pt(3, 4)
assert p1 == p2
assert p1 != p3
pt_set = {p1, p2, p3}
assert len(pt_set) == 2
print("OK")
