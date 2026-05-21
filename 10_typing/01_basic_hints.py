"""
기본 타입 힌트 (Type Hints)
Python 3.5+ 부터 도입된 타입 힌트는 정적 분석 도구(mypy)가 버그를 찾도록 돕는다.
런타임에는 강제되지 않으며, 코드 가독성과 IDE 지원을 크게 향상시킨다.
"""

# ──── 1. 변수 힌트 ────

name: str = "Kee"          # 문자열 변수
age: int = 30              # 정수 변수
height: float = 1.75       # 실수 변수
active: bool = True        # 불리언 변수

# ──── 2. 함수 시그니처 힌트 ────

def add(a: int, b: int) -> int:
    """두 정수를 더한다."""
    return a + b


def greet(name: str) -> str:
    """이름을 받아 인사 문자열을 반환한다."""
    return f"안녕하세요, {name}님!"


def is_even(n: int) -> bool:
    """짝수 여부를 반환한다."""
    return n % 2 == 0


# ──── 3. 컨테이너 힌트 (Python 3.9+) ────

def sum_list(numbers: list[int]) -> int:
    """정수 리스트의 합을 반환한다."""
    return sum(numbers)


def word_count(text: str) -> dict[str, int]:
    """단어별 등장 횟수를 딕셔너리로 반환한다."""
    result: dict[str, int] = {}
    for word in text.split():
        result[word] = result.get(word, 0) + 1
    return result


def first_three(items: list[str]) -> tuple[str, str, str]:
    """리스트의 첫 세 원소를 튜플로 반환한다."""
    return (items[0], items[1], items[2])


def unique_tags(tags: list[str]) -> set[str]:
    """중복을 제거한 태그 집합을 반환한다."""
    return set(tags)


# ──── 4. X | None (Python 3.10+, Optional 대체) ────

def find_user(user_id: int) -> str | None:
    """사용자를 찾으면 이름, 없으면 None 반환."""
    db: dict[int, str] = {1: "Alice", 2: "Bob"}
    return db.get(user_id)  # 없으면 None


def safe_divide(a: float, b: float) -> float | None:
    """0으로 나누면 None, 아니면 결과 반환."""
    if b == 0:
        return None
    return a / b


# ──── 5. 런타임 강제 없음 — 주의 ────

def double(n: int) -> int:
    """정수를 두 배로 반환한다."""
    return n * 2  # type: ignore[operator]  # 런타임엔 문자열도 통과함


if __name__ == "__main__":
    # 기본 힌트 시연
    print("=== 기본 타입 힌트 ===")
    print(f"add(3, 4) = {add(3, 4)}")
    print(f"greet('파이썬') = {greet('파이썬')}")
    print(f"is_even(7) = {is_even(7)}")

    # 컨테이너 힌트
    print("\n=== 컨테이너 ===")
    print(f"sum_list([1,2,3]) = {sum_list([1, 2, 3])}")
    counts = word_count("사과 배 사과 귤")
    print(f"word_count('사과 배 사과 귤') = {counts}")

    # X | None 패턴
    print("\n=== X | None ===")
    print(f"find_user(1) = {find_user(1)}")
    print(f"find_user(99) = {find_user(99)}")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

    # 런타임 강제 없음 — 잘못된 타입도 실행은 됨 (정적 검사기가 잡아줌)
    print("\n=== 런타임 강제 없음 ===")
    result = double("ha")  # type: ignore[arg-type]  # mypy는 에러 → 런타임은 "haha"
    print(f"double('ha') 런타임 결과: {result!r}  ← 타입 힌트 위반이지만 실행됨")
    print("→ mypy로 정적 검사해야 이런 버그를 잡을 수 있다.")
