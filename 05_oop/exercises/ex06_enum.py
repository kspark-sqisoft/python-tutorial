"""
연습문제 06: enum 기본기.

4개 TODO 를 채워 모든 assert 를 통과하고 'OK' 가 출력되게 만드세요.
정답은 `solutions/ex06_enum.py`.
"""

from enum import Enum, IntEnum, StrEnum, auto


# ──── TODO 1: 기본 Enum ────
# 신호등 상태(RED, YELLOW, GREEN)를 표현하는 Light Enum 을 만드세요.
# 값은 자동(auto())을 사용합니다.

class Light(Enum):
    # TODO: RED, YELLOW, GREEN 멤버 작성
    pass


assert Light.RED.value == 1
assert Light.GREEN.value == 3
assert Light.RED is Light.RED                  # 싱글톤 확인


# ──── TODO 2: IntEnum — int 의 서브타입 ────
# 우선순위(LOW=1, MEDIUM=5, HIGH=10)를 IntEnum 으로 정의하세요.

class Priority(IntEnum):
    # TODO
    pass


assert Priority.LOW == 1
assert Priority.HIGH + 1 == 11                 # int 처럼 연산 가능
assert isinstance(Priority.MEDIUM, int)


# ──── TODO 3: StrEnum — str 의 서브타입 ────
# 권한 레벨(ADMIN="admin", USER="user")을 StrEnum 으로 정의하세요.

class Role(StrEnum):
    # TODO
    pass


assert Role.ADMIN == "admin"                   # str 과 직접 비교
assert f"role={Role.USER}" == "role=user"


# ──── TODO 4: match 와 결합 ────
# Light 를 받아 다음 행동을 반환하는 함수 next_action 을 작성하세요.
#   RED    → "stop"
#   YELLOW → "slow"
#   GREEN  → "go"

def next_action(light: Light) -> str:
    # TODO: match / case 로 작성
    pass


assert next_action(Light.RED) == "stop"
assert next_action(Light.YELLOW) == "slow"
assert next_action(Light.GREEN) == "go"


print("OK")
