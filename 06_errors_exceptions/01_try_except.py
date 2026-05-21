"""
try / except 기본 — 예외를 잡는 여러 방법.
except 절에 예외 종류를 지정하거나, 여러 예외를 한 번에 묶을 수 있다.
빈 except: 는 KeyboardInterrupt 까지 잡아 프로그램을 죽기 힘들게 만드니 쓰지 않는다.
"""

# ──── 1. try/except 기본 형태 ────

def divide(a, b):
    # b 가 0 이면 ZeroDivisionError 발생
    try:
        result = a / b
    except ZeroDivisionError:
        print("0 으로 나눌 수 없습니다.")
        return None
    return result

# ──── 2. 여러 예외를 한 번에 잡기 ────

def safe_convert_and_divide(text, divisor):
    # ValueError (변환 실패) 와 ZeroDivisionError 를 동시에 처리
    try:
        number = int(text)
        result = number / divisor
    except (ValueError, ZeroDivisionError) as e:
        # e.args: 예외 메시지 튜플, str(e): 문자열 표현
        print(f"오류 발생 — 종류: {type(e).__name__}, 메시지: {str(e)}, args: {e.args}")
        return None
    return result

# ──── 3. except 예외 as e: 로 예외 객체 받기 ────

def show_exception_info(func, *args):
    # 예외 객체의 속성을 상세히 출력
    try:
        func(*args)
    except Exception as e:
        print(f"  type    : {type(e).__name__}")
        print(f"  str(e)  : {str(e)}")
        print(f"  e.args  : {e.args}")

# ──── 4. 빈 except: 가 위험한 이유 ────

# 아래처럼 쓰면 Ctrl+C (KeyboardInterrupt) 까지 잡혀 프로그램을 멈출 수 없다.
# try:
#     ...
# except:          # 절대 금지
#     pass
#
# 대신 except Exception: 까지만 — BaseException 하위이지만
# KeyboardInterrupt/SystemExit 는 Exception 을 상속하지 않는다.

def safe_catch_all(func, *args):
    # 권장: except Exception: 까지만
    try:
        func(*args)
    except Exception as e:
        print(f"Exception 계열 오류 잡힘: {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("=== 1. 기본 ZeroDivisionError ===")
    print(divide(10, 2))   # 5.0
    print(divide(10, 0))   # None, 메시지 출력

    print("\n=== 2. 여러 예외 한 번에 ===")
    print(safe_convert_and_divide("abc", 2))   # ValueError
    print(safe_convert_and_divide("10", 0))    # ZeroDivisionError
    print(safe_convert_and_divide("10", 2))    # 5.0

    print("\n=== 3. 예외 객체 상세 정보 ===")
    print("int('abc') 예외:")
    show_exception_info(int, "abc")
    print("[][0] 예외:")
    show_exception_info(lambda: [][0])

    print("\n=== 4. except Exception: 권장 패턴 ===")
    safe_catch_all(int, "hello")
    safe_catch_all(lambda: 1 / 0)
