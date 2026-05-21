"""
파이썬 예외 계층 구조와 자주 만나는 예외들.
BaseException → Exception → 각종 구체 예외 순으로 상속된다.
자식 예외는 부모 except 절로도 잡히므로 넓은 except 는 신중하게 써야 한다.
"""

# ──── 1. 예외 계층 개요 ────
#
# BaseException
# ├── SystemExit            (sys.exit() 호출 시)
# ├── KeyboardInterrupt     (Ctrl+C)
# ├── GeneratorExit         (제너레이터 종료)
# └── Exception             ← 일반 코드에서 잡는 최상위
#     ├── ArithmeticError
#     │   └── ZeroDivisionError
#     ├── LookupError
#     │   ├── KeyError
#     │   └── IndexError
#     ├── OSError
#     │   └── FileNotFoundError
#     ├── AttributeError
#     ├── TypeError
#     ├── ValueError
#     ├── NameError
#     └── ImportError / ModuleNotFoundError

# ──── 2. 자주 보는 예외 데모 ────

def trigger(kind):
    # 의도적으로 각 예외를 발생시키는 함수
    if kind == "zero_div":
        return 1 / 0                   # ZeroDivisionError
    elif kind == "key":
        return {}["없는키"]             # KeyError
    elif kind == "index":
        return [][0]                   # IndexError
    elif kind == "file":
        open("/없는/경로/파일.txt")      # FileNotFoundError
    elif kind == "attr":
        return None.존재하지않는속성    # AttributeError
    elif kind == "type":
        return "문자" + 1              # TypeError
    elif kind == "value":
        return int("abc")              # ValueError
    elif kind == "name":
        # NameError 는 exec 로 격리해서 발생
        exec("print(존재하지않는변수)")  # NameError
    elif kind == "import":
        import 존재하지않는모듈          # ModuleNotFoundError (ImportError 하위)

# ──── 3. 자식은 부모로 잡힌다 ────

def catch_with_parent():
    # LookupError 로 KeyError / IndexError 둘 다 잡기
    cases = [
        (lambda: {}["x"],  "KeyError"),
        (lambda: [][0],    "IndexError"),
    ]
    for fn, name in cases:
        try:
            fn()
        except LookupError as e:
            # LookupError 가 부모이므로 두 자식 모두 잡힌다
            print(f"  LookupError 로 잡힘 — 실제 타입: {type(e).__name__} ({name})")

# ──── 4. except Exception 까지만 권장 ────

def safe_run(fn):
    # BaseException 은 잡지 않는 것이 원칙
    try:
        fn()
    except Exception as e:
        print(f"  Exception 계열: {type(e).__name__}: {e}")


if __name__ == "__main__":
    kinds = [
        ("zero_div",  "ZeroDivisionError"),
        ("key",       "KeyError"),
        ("index",     "IndexError"),
        ("file",      "FileNotFoundError"),
        ("attr",      "AttributeError"),
        ("type",      "TypeError"),
        ("value",     "ValueError"),
    ]

    print("=== 1. 자주 보는 예외 각각 잡기 ===")
    for kind, expected in kinds:
        try:
            trigger(kind)
        except Exception as e:
            print(f"  [{expected:25s}] 잡힘: {type(e).__name__}: {e}")

    print("\n=== 2. 자식 예외는 부모로 잡힌다 ===")
    catch_with_parent()

    print("\n=== 3. except Exception: 안전 패턴 ===")
    safe_run(lambda: 1 / 0)
    safe_run(lambda: int("nope"))

    print("\n=== 4. 예외 계층 확인 (issubclass) ===")
    for exc in [ZeroDivisionError, KeyError, IndexError, FileNotFoundError,
                AttributeError, TypeError, ValueError]:
        is_exception = issubclass(exc, Exception)
        is_base = issubclass(exc, BaseException)
        print(f"  {exc.__name__:25s} Exception={is_exception}, BaseException={is_base}")
