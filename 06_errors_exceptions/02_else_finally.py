"""
try / except / else / finally 4단 구조.
else 는 예외 없이 성공했을 때만, finally 는 항상 실행된다.
자원 정리에 finally 를 쓰지만, with 문이 더 간결한 경우가 많다.
"""

# ──── 1. 4단 구조 기본 ────

def four_clause(a, b):
    # 각 절이 언제 실행되는지 print 로 추적
    print(f"  [호출] four_clause({a}, {b})")
    try:
        print("  [try] 나눗셈 시도")
        result = a / b
    except ZeroDivisionError as e:
        # try 블록에서 예외가 발생했을 때
        print(f"  [except] ZeroDivisionError: {e}")
        result = None
    else:
        # try 가 예외 없이 끝났을 때만 실행 — except 와 함께 쓸 때 의미 있음
        print(f"  [else] 성공! result = {result}")
    finally:
        # 예외 발생 여부와 관계없이 항상 실행
        print("  [finally] 항상 실행됨")
    return result

# ──── 2. else 의 역할 ────

def read_integer(text):
    # else: 변환이 성공했을 때만 "다음 처리"를 수행
    try:
        value = int(text)
    except ValueError:
        print(f"  '{text}' 는 정수로 변환할 수 없습니다.")
        return None
    else:
        # 변환 성공 시에만 실행 — try 블록을 짧게 유지하는 데 도움
        doubled = value * 2
        print(f"  변환 성공: {value}, 두 배: {doubled}")
        return doubled

# ──── 3. finally 로 자원 정리 ────

def read_file_manual(path):
    # finally 를 이용한 수동 자원 정리 예시
    # 실무에서는 with open(...) as f: 가 훨씬 간결하다
    f = None
    try:
        f = open(path, "r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        print(f"  파일 없음: {path}")
        return None
    finally:
        # f 가 열렸든 아니든 항상 닫기 시도
        if f is not None:
            f.close()
            print("  [finally] 파일 닫힘")

# ──── 4. finally 는 return 보다 먼저 정리된다 ────

def finally_with_return(x):
    try:
        return x * 2   # 이 return 직전에 finally 가 먼저 실행됨
    finally:
        print("  [finally] return 전에도 실행됨")


if __name__ == "__main__":
    print("=== 1. 4단 구조 — 예외 없을 때 ===")
    four_clause(10, 2)

    print("\n=== 2. 4단 구조 — 예외 있을 때 ===")
    four_clause(10, 0)

    print("\n=== 3. else 의 역할 ===")
    read_integer("42")
    read_integer("hello")

    print("\n=== 4. finally 와 return ===")
    result = finally_with_return(5)
    print(f"  반환값: {result}")

    print("\n=== 5. finally 로 파일 정리 ===")
    read_file_manual("/tmp/존재하지않는파일.txt")
