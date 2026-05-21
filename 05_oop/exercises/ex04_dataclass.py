"""
연습 04 — dataclass
frozen=True 불변 dataclass Pt 를 완성하세요.
"""

from dataclasses import dataclass

# TODO: @dataclass(frozen=True) 로 Pt 클래스를 작성하세요.
# - 필드: x (float 또는 int), y (float 또는 int)
# - frozen=True 이므로 __hash__ 가 자동 생성되어 set 에 넣을 수 있습니다.

# 아래 assert 가 모두 통과해야 합니다.
# p1 = Pt(1, 2)
# p2 = Pt(1, 2)
# p3 = Pt(3, 4)
# assert p1 == p2
# assert p1 != p3
# pt_set = {p1, p2, p3}
# assert len(pt_set) == 2   # p1 과 p2 는 중복
# print("OK")

raise NotImplementedError("TODO: Pt dataclass 를 구현하세요.")
