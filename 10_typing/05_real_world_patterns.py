"""
실전 타입 힌트 패턴 — Callable / Literal / Final / cast
고급 타입 힌트 도구들을 활용해 더 정확한 타입 명세를 작성하는 법을 배운다.
모두 typing 모듈에서 임포트하며 런타임 동작에는 영향을 주지 않는다.
"""

from typing import Callable, Literal, Final, cast

# ──── 1. Callable — 함수 타입 ────

# Callable[[인자1타입, 인자2타입, ...], 반환타입]
def apply(fn: Callable[[int, int], int], a: int, b: int) -> int:
    """두 정수를 받는 함수 fn 을 a, b 에 적용한다."""
    return fn(a, b)


def apply_unary(fn: Callable[[str], str], text: str) -> str:
    """문자열을 받아 문자열을 반환하는 함수를 적용한다."""
    return fn(text)


def make_multiplier(factor: int) -> Callable[[int], int]:
    """factor 를 곱하는 함수를 반환한다 (클로저 + Callable 힌트)."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


# ──── 2. Literal — 문자열/값 enum 식 제한 ────

# 특정 값만 허용하도록 제한한다 — 오타 등을 정적으로 잡아준다.
HttpMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
Direction = Literal["north", "south", "east", "west"]
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def send_request(url: str, method: HttpMethod) -> str:
    """HTTP 메서드는 정해진 문자열만 허용한다."""
    return f"{method} {url}"


def move(direction: Direction, steps: int) -> str:
    """방향과 걸음 수를 받아 이동 문자열 반환."""
    return f"{direction} 방향으로 {steps}걸음"


def log(level: LogLevel, message: str) -> None:
    """로그 레벨과 메시지를 출력한다."""
    print(f"[{level}] {message}")


# ──── 3. Final — 재할당 금지 상수 ────

# Final 로 선언한 변수는 mypy 가 재할당을 오류로 검사한다.
MAX_RETRY: Final = 3                      # 최대 재시도 횟수
DEFAULT_TIMEOUT: Final = 30.0             # 기본 타임아웃(초)
APP_NAME: Final = "파이썬 타입 힌트 튜토리얼"
PI: Final = 3.14159265358979


def retry_with_limit(fn: Callable[[], bool], limit: int = MAX_RETRY) -> bool:
    """최대 limit 번 fn 을 시도한다. 한 번이라도 성공하면 True."""
    for _ in range(limit):
        if fn():
            return True
    return False


# ──── 4. cast — 타입 단언 (런타임 영향 없음) ────

# cast(타입, 값) — mypy 에게 "이 값을 이 타입으로 취급해라"고 알린다.
# 런타임에는 아무 변환도 하지 않는다 (identity 함수와 동일).
def process_input(raw: object) -> int:
    """외부에서 받은 raw 값을 int 로 캐스팅해 사용한다."""
    # raw 가 실제로 int 임을 확신할 때만 cast 를 사용한다.
    value = cast(int, raw)   # 런타임: value is raw (변환 없음)
    return value * 2


if __name__ == "__main__":
    # Callable 시연
    print("=== Callable ===")
    print(f"apply(lambda a,b: a+b, 3, 4) = {apply(lambda a, b: a + b, 3, 4)}")
    print(f"apply(lambda a,b: a*b, 3, 4) = {apply(lambda a, b: a * b, 3, 4)}")
    print(f"apply_unary(str.upper, 'hello') = {apply_unary(str.upper, 'hello')}")

    triple = make_multiplier(3)
    print(f"make_multiplier(3)(7) = {triple(7)}")

    # Literal 시연
    print("\n=== Literal ===")
    print(send_request("https://api.example.com/users", "GET"))
    print(send_request("https://api.example.com/users", "POST"))
    print(move("north", 5))
    log("INFO", "서버 시작됨")
    log("WARNING", "메모리 사용률 80% 초과")

    # Final 시연
    print("\n=== Final ===")
    print(f"MAX_RETRY = {MAX_RETRY}")
    print(f"DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}s")
    print(f"APP_NAME = {APP_NAME}")
    # MAX_RETRY = 5  # ← 이 줄을 활성화하면 mypy 가 오류를 보고한다

    # cast 시연
    print("\n=== cast ===")
    raw_value: object = 21
    print(f"process_input(21) = {process_input(raw_value)}")
    print("→ cast 는 런타임에 아무것도 하지 않는다 — mypy 에게만 알려주는 힌트")
