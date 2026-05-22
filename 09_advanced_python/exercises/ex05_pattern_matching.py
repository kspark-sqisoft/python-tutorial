"""
연습문제 05: match / case — 구조적 패턴 매칭.

4개 TODO 를 채워 'OK' 가 출력되게 만드세요.
정답은 `solutions/ex05_pattern_matching.py`.
"""

from dataclasses import dataclass


# ──── TODO 1: 리터럴 + OR + 와일드카드 ────
# 주말은 "weekend", 평일은 "weekday", 그 외 입력은 "?" 를 반환하세요.

def day_kind(name: str) -> str:
    match name:
        # TODO: "Sat" | "Sun" → weekend, "Mon" | "Tue" | "Wed" | "Thu" | "Fri" → weekday, _ → "?"
        pass


assert day_kind("Mon") == "weekday"
assert day_kind("Sat") == "weekend"
assert day_kind("???") == "?"


# ──── TODO 2: 시퀀스 패턴 ────
# 리스트가 비었으면 "empty", 한 개면 그 값을 문자열로, 두 개 이상이면 "{first}+{rest_len}" 형태.

def summarize(seq: list) -> str:
    match seq:
        # TODO
        pass


assert summarize([]) == "empty"
assert summarize([7]) == "7"
assert summarize([1, 2, 3, 4]) == "1+3"


# ──── TODO 3: 매핑 패턴 ────
# 이벤트 dict 에서 type 별로 다른 문자열을 반환하세요.
#   {"type": "login", "user": u}  → f"login:{u}"
#   {"type": "logout"}            → "logout"
#   그 외                         → "unknown"

def event(e: dict) -> str:
    match e:
        # TODO
        pass


assert event({"type": "login", "user": "ks"}) == "login:ks"
assert event({"type": "logout"}) == "logout"
assert event({"type": "click"}) == "unknown"


# ──── TODO 4: 클래스 패턴 + 가드 ────
# Point 가 원점이면 "origin", x>0 이고 y>0 이면 "Q1"(1사분면), 그 외엔 "elsewhere".

@dataclass
class Point:
    x: int
    y: int


def quadrant(p: Point) -> str:
    match p:
        # TODO: Point(0, 0) → "origin", Point(x, y) if x > 0 and y > 0 → "Q1", _ → "elsewhere"
        pass


assert quadrant(Point(0, 0)) == "origin"
assert quadrant(Point(3, 4)) == "Q1"
assert quadrant(Point(-1, 2)) == "elsewhere"


print("OK")
