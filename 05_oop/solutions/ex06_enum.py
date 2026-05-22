"""
풀이 06: enum 기본기.

- 기본 Enum 은 클래스 본문에 `NAME = value` 형태로 멤버를 선언한다. `auto()` 는 1부터 증가하는 int 를 부여한다.
- `IntEnum` / `StrEnum` 은 각각 int / str 의 서브타입처럼 동작해, 외부 표현(JSON·DB 등)이 정수/문자열일 때 자연스럽다.
- enum 은 패턴 매칭과 잘 어울린다 — `case Color.RED:` 처럼 점이 포함된 이름을 써야 캡처가 아닌 상수 비교가 된다.
"""

from enum import Enum, IntEnum, StrEnum, auto


class Light(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()


assert Light.RED.value == 1
assert Light.GREEN.value == 3
assert Light.RED is Light.RED


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 5
    HIGH = 10


assert Priority.LOW == 1
assert Priority.HIGH + 1 == 11
assert isinstance(Priority.MEDIUM, int)


class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"


assert Role.ADMIN == "admin"
assert f"role={Role.USER}" == "role=user"


def next_action(light: Light) -> str:
    match light:
        case Light.RED:    return "stop"
        case Light.YELLOW: return "slow"
        case Light.GREEN:  return "go"


assert next_action(Light.RED) == "stop"
assert next_action(Light.YELLOW) == "slow"
assert next_action(Light.GREEN) == "go"


print("OK")
