"""
풀이 05: match / case.

- 리터럴/OR/와일드카드 패턴은 `switch` 의 직관적 대체.
- 시퀀스 패턴은 `[head, *rest]` 처럼 분해 + 캡처를 한 번에 한다.
- 매핑 패턴은 dict 의 일부 키만 골라 매칭하므로 외부 필드가 늘어나도 깨지지 않는다.
- 클래스 패턴은 dataclass 와 잘 어울리며, `case Point(0, 0)` 처럼 위치 인자도 받는다.
- 가드는 패턴에 추가 boolean 조건을 거는 도구다 — 캡처한 변수를 가드에서 그대로 쓸 수 있다.
"""

from dataclasses import dataclass


def day_kind(name: str) -> str:
    match name:
        case "Sat" | "Sun":                                return "weekend"
        case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":        return "weekday"
        case _:                                            return "?"


assert day_kind("Mon") == "weekday"
assert day_kind("Sat") == "weekend"
assert day_kind("???") == "?"


def summarize(seq: list) -> str:
    match seq:
        case []:                       return "empty"
        case [only]:                   return str(only)
        case [first, *rest]:           return f"{first}+{len(rest)}"


assert summarize([]) == "empty"
assert summarize([7]) == "7"
assert summarize([1, 2, 3, 4]) == "1+3"


def event(e: dict) -> str:
    match e:
        case {"type": "login", "user": u}:   return f"login:{u}"
        case {"type": "logout"}:             return "logout"
        case _:                              return "unknown"


assert event({"type": "login", "user": "ks"}) == "login:ks"
assert event({"type": "logout"}) == "logout"
assert event({"type": "click"}) == "unknown"


@dataclass
class Point:
    x: int
    y: int


def quadrant(p: Point) -> str:
    match p:
        case Point(0, 0):                       return "origin"
        case Point(x, y) if x > 0 and y > 0:    return "Q1"
        case _:                                 return "elsewhere"


assert quadrant(Point(0, 0)) == "origin"
assert quadrant(Point(3, 4)) == "Q1"
assert quadrant(Point(-1, 2)) == "elsewhere"


print("OK")
