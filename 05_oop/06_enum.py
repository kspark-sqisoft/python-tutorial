"""
enum — 이름 붙은 상수 집합 (PEP 435, Python 3.4+).

다른 언어와의 차이점:
- Java/Dart 의 `enum`, TypeScript 의 `enum` 또는 유니언과 매핑되는 일급 타입.
- 파이썬 enum 멤버는 **싱글톤** — `Color.RED is Color.RED` 가 항상 True.
- 메서드/속성을 가질 수 있고, 멤버 값에 부가 데이터를 담아 작은 도메인 객체처럼 쓸 수 있다.
- `IntEnum`, `StrEnum` 으로 int·str 의 서브타입처럼 동작시킬 수 있다 (DB·JSON 호환에 유리).
- 자세한 언어 간 매핑은 파일 끝의 "다른 언어와의 비교" 섹션 참고.
"""

from enum import Enum, IntEnum, StrEnum, auto


# ──── 1. 기본 Enum ────

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


assert Color.RED.name == "RED"
assert Color.RED.value == "red"

# 싱글톤이므로 `is` 비교가 안전하고 권장된다
assert Color.RED is Color.RED
assert Color("red") is Color.RED            # 값으로 역조회
assert Color["RED"] is Color.RED            # 이름으로 역조회

# 반복 가능
assert [c.name for c in Color] == ["RED", "GREEN", "BLUE"]

# ──── 2. auto() — 값을 자동 부여 ────

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()


assert Status.PENDING.value == 1            # auto() 는 1부터 증가하는 int 반환

# ──── 3. IntEnum — int 의 서브타입 ────

class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


# IntEnum 멤버는 그 자체로 int — 비교/연산이 자유롭다
assert HttpStatus.OK == 200
assert HttpStatus.OK + 1 == 201
assert isinstance(HttpStatus.OK, int)
# → DB 칼럼이나 JSON 같이 정수로만 표현되는 환경과 잘 맞물린다.

# ──── 4. StrEnum (Python 3.11+) — str 의 서브타입 ────

class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


assert Role.ADMIN == "admin"                # str 과 직접 비교 가능
assert f"role={Role.ADMIN}" == "role=admin" # 포맷팅 시 value 사용

# ──── 5. 메서드 + 값 외 부가 정보 ────

class Planet(Enum):
    # value 자리에 튜플을 넣고, __init__ 에서 풀어서 속성으로 보관한다.
    MERCURY = (3.303e23, 2.4397e6)
    EARTH   = (5.976e24, 6.37814e6)

    def __init__(self, mass: float, radius: float):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self) -> float:
        G = 6.67430e-11
        return G * self.mass / (self.radius ** 2)


assert round(Planet.EARTH.surface_gravity, 2) == 9.80

# ──── 6. match 와 잘 어울림 — 구조적 패턴 매칭 + enum ────

def label(status: Status) -> str:
    match status:
        case Status.PENDING: return "대기 중"
        case Status.RUNNING: return "실행 중"
        case Status.DONE:    return "완료"


assert label(Status.RUNNING) == "실행 중"

# ──── 7. 자주 만나는 함정 ────

# (a) 일반 Enum 은 int/str 와 직접 비교하면 False — IntEnum/StrEnum 이 아니면 캐스팅 필요.
assert (Color.RED == "red") is False
assert Color.RED.value == "red"             # 명시적 .value 사용

# (b) Enum 안에서 같은 value 를 두 번 쓰면 **별칭(alias)** 이 된다 — 두 이름이 같은 멤버를 가리킨다.
class Priority(Enum):
    LOW = 1
    HIGH = 10
    URGENT = 10        # HIGH 의 alias

assert Priority.URGENT is Priority.HIGH
assert [p.name for p in Priority] == ["LOW", "HIGH"]   # alias 는 반복에 포함되지 않음


# ──── 8. 다른 언어와의 비교 — Dart / TypeScript ────
#
# 작업                          | Python                            | Dart                                | TypeScript
# ----------------------------- | --------------------------------- | ----------------------------------- | -----------------------------------
# 단순 enum                     | `class C(Enum): RED = "red"`      | `enum Color { red, green, blue }`   | `enum Color { Red, Green, Blue }`
# int 호환 enum                 | `class C(IntEnum): ...`           | (그냥 index 사용 — `Color.red.index`)| `enum Color { Red = 200, ... }`
# 문자열 호환 enum              | `class C(StrEnum): ...`           | `enum Color { red, green }` + `name`| `enum Color { Red = "red", ... }`
# 멤버에 메서드/필드             | `def __init__(self, ...): ...`    | `enum Planet { earth(mass: ...); }` | union + `as const` + 별도 helper
# 멤버 반복                     | `for c in Color: ...`             | `Color.values`                      | `Object.values(Color)`
# 값으로 역조회                 | `Color("red")`                    | `Color.values.firstWhere(...)`      | 직접 매핑 객체 필요
# 패턴 매칭과 결합              | `match c: case Color.RED: ...`    | `switch (c) { case Color.red: ... }`| switch-case 또는 narrowing
#
# 핵심 차이
# - Dart 의 enhanced enum (2.17+) 은 파이썬 Enum 메서드 패턴과 거의 1:1.
# - TS enum 은 컴파일 후 객체로 변환되어 트리쉐이킹·역조회 등에서 미묘한 함정이 있어,
#   "string literal union + as const + helper" 패턴이 모던 TS 의 사실상 대안.
# - 파이썬은 enum 자체가 클래스라 어떤 메서드든 추가 가능 — 가장 유연하다.


if __name__ == "__main__":
    print("=== Color ===")
    for c in Color:
        print(f"  {c.name} = {c.value!r}")

    print("\n=== HttpStatus (IntEnum) ===")
    print(f"  OK + 1 = {HttpStatus.OK + 1}")

    print("\n=== Planet - 멤버에 부가 정보 ===")
    print(f"  Earth gravity ~ {Planet.EARTH.surface_gravity:.2f} m/s^2")

    print("\n=== Status + match ===")
    for s in Status:
        print(f"  {s.name} → {label(s)}")

    print("\n=== Alias ===")
    print(f"  Priority.URGENT is Priority.HIGH → {Priority.URGENT is Priority.HIGH}")
