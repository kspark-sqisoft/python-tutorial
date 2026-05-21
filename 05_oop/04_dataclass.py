"""
dataclass — @dataclass 데코레이터로 boilerplate 제거.
dataclass 는 필드 선언에 타입 힌트가 필수이므로 여기서만 사용합니다.
타입 힌트 자체는 10_typing 에서 다룹니다.
"""

from dataclasses import dataclass, field

# ──── 1. @dataclass 기본 ────

# @dataclass 는 __init__, __repr__, __eq__ 를 자동 생성한다.
# 타입 힌트(name: str)는 dataclass 필드 선언에 필수다. (이 파일에서 유일한 예외)
# 일반 클래스로 같은 것을 만들면 __init__, __repr__, __eq__ 를 모두 직접 써야 해서
# 코드량이 3~4배 늘어난다.

@dataclass
class User:
    """사용자 정보를 담는 데이터 클래스."""
    name: str
    age: int
    email: str = ""   # 기본값 있는 필드


# ──── 2. frozen=True — 불변 dataclass ────

# frozen=True 로 만들면 생성 후 필드를 변경할 수 없다.
# 불변이므로 __hash__ 가 자동 생성되어 dict 키나 set 원소로 사용 가능하다.

@dataclass(frozen=True)
class Point:
    """불변 2차원 좌표."""
    x: float
    y: float


# ──── 3. field(default_factory=...) — 가변 기본값 함정 회피 ────

# 기본값으로 [] 를 직접 쓰면 모든 인스턴스가 같은 리스트를 공유하는 버그가 생긴다.
# field(default_factory=list) 로 인스턴스마다 새 리스트를 생성한다.

@dataclass
class Team:
    """팀 이름과 멤버 목록."""
    name: str
    members: list = field(default_factory=list)  # 인스턴스마다 새 리스트


# ──── 4. 데모 ────

if __name__ == "__main__":
    print("=== User dataclass ===")
    u1 = User("홍길동", 30, "hong@example.com")
    u2 = User("홍길동", 30, "hong@example.com")
    u3 = User("김철수", 25)

    print(u1)                           # __repr__ 자동 생성
    print(f"u1 == u2: {u1 == u2}")      # True, __eq__ 자동 생성
    print(f"u1 == u3: {u1 == u3}")      # False

    print()
    print("=== frozen Point (불변 + 해시 가능) ===")
    p1 = Point(1.0, 2.0)
    p2 = Point(1.0, 2.0)
    p3 = Point(3.0, 4.0)
    print(f"p1 == p2: {p1 == p2}")       # True
    point_set = {p1, p2, p3}
    print(f"set 에 넣으면 중복 제거: {point_set}")  # {Point(1.0, 2.0), Point(3.0, 4.0)}

    # frozen 이므로 변경 시 예외 발생
    try:
        p1.x = 99
    except Exception as e:
        print(f"불변 위반 → {type(e).__name__}: {e}")

    print()
    print("=== Team — default_factory ===")
    t1 = Team("알파팀")
    t2 = Team("베타팀")
    t1.members.append("홍길동")
    print(f"t1.members: {t1.members}")   # ['홍길동']
    print(f"t2.members: {t2.members}")   # [] — 공유 안 됨
