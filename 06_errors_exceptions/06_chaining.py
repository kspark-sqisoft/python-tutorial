"""
예외 chaining — `raise X from Y`, `__cause__`, `__context__`, `except*` (3.11+).

다른 언어와의 차이점:
- Java 의 `new IOException("msg", cause)`, Dart 의 `Error` + stackTrace,
  TypeScript / ES2022 의 `new Error("...", { cause })` 와 같은 자리의 도구.
- `raise New from Original` 은 "원본 예외 때문에 새 예외를 던졌다" 는 인과 관계를 **명시**한다.
- 명시하지 않아도 except 블록 안에서 다른 예외를 던지면 파이썬이 자동으로 `__context__` 를 채운다.
- `raise New from None` 으로 원본 체인을 의도적으로 숨길 수 있다 (내부 구현 노출 방지).
- 자세한 언어 비교는 파일 끝 섹션.
"""

import sys
import traceback


# ──── 1. 자연스러운 chaining — __context__ ────

def load_config(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        # 새 예외를 그냥 던지면 파이썬이 자동으로 e.__context__ 를 채운다.
        raise RuntimeError("설정을 로드할 수 없습니다")


try:
    load_config("/__nonexistent__/config.txt")
except RuntimeError as e:
    assert isinstance(e.__context__, FileNotFoundError)
    assert e.__cause__ is None              # 명시적 cause 는 비어 있음


# ──── 2. 명시적 chaining — raise X from Y ────

class ConfigError(Exception):
    """애플리케이션 도메인의 설정 오류."""


def load_config2(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as orig:
        # `from orig` → e.__cause__ 가 설정되고, 트레이스백에 "직접적 원인" 으로 표시된다.
        raise ConfigError(f"설정 누락: {path}") from orig


try:
    load_config2("/__nonexistent__/config.txt")
except ConfigError as e:
    assert isinstance(e.__cause__, FileNotFoundError)
    # 트레이스백 출력 예:
    #   FileNotFoundError: ...
    #   The above exception was the direct cause of the following exception:
    #   ConfigError: ...


# ──── 3. raise X from None — 원인 숨기기 ────

def public_api(key: str) -> int:
    """외부에 공개되는 API. 내부 KeyError 같은 구현 디테일은 숨기는 게 깔끔."""
    table = {"a": 1, "b": 2}
    try:
        return table[key]
    except KeyError:
        # `from None` → __cause__ = None, __suppress_context__ = True
        # 트레이스백에 KeyError 가 표시되지 않는다.
        raise ValueError(f"알 수 없는 키: {key!r}") from None


try:
    public_api("missing")
except ValueError as e:
    assert e.__cause__ is None
    assert e.__suppress_context__ is True


# ──── 4. except* — ExceptionGroup (Python 3.11+) ────

def parse_many(items: list[str]) -> list[int]:
    """여러 입력을 한 번에 파싱 — 부분 실패를 모아 ExceptionGroup 으로 던진다."""
    ok: list[int] = []
    errors: list[Exception] = []
    for x in items:
        try:
            ok.append(int(x))
        except ValueError as e:
            errors.append(e)
    if errors:
        raise ExceptionGroup("parse 실패", errors)
    return ok


try:
    parse_many(["1", "a", "2", "b"])
except* ValueError as eg:
    # `except*` 는 그룹에서 ValueError 만 골라 받는다 (다른 종류가 섞여 있다면 별도 except* 로 처리).
    assert len(eg.exceptions) == 2


# ──── 5. 트레이스백 디버깅 팁 ────

def deep_fail():
    try:
        int("not a number")
    except ValueError as e:
        raise ConfigError("설정 값 변환 실패") from e


# 트레이스백 문자열로 받기 (로깅에 유용)
try:
    deep_fail()
except ConfigError:
    tb_text = traceback.format_exc()
    # 트레이스백에는 "ValueError ... direct cause ... ConfigError ..." 가 모두 나타난다.
    assert "direct cause" in tb_text
    assert "ValueError" in tb_text and "ConfigError" in tb_text


# ──── 6. 다른 언어와의 비교 — Dart / TypeScript ────
#
# 작업                        | Python                              | Dart                                       | TypeScript / ES2022+
# --------------------------- | ----------------------------------- | ------------------------------------------ | ---------------------------------------------
# 새 예외에 원본 첨부         | `raise New(...) from orig`          | `Error.throwWithStackTrace(new, orig.stackTrace)` | `throw new Error("...", { cause: orig })`
# 자동 chaining(except 블록)  | `__context__` 자동 설정             | (직접 보관 필요)                           | (직접 보관 필요)
# 원인 숨기기                 | `raise X from None`                 | (그냥 새 예외만 던지면 됨)                 | (cause 옵션 생략)
# 원인 접근                   | `e.__cause__`, `e.__context__`      | (catch 한 변수에 직접 보관)                | `e.cause` (ES2022)
# 여러 예외 묶기              | `ExceptionGroup`, `except*` (3.11+) | (직접 list 로 보관)                        | `AggregateError` (`Promise.any` 실패 등)
#
# 핵심 차이
# - 파이썬의 자동 `__context__` 는 다른 언어엔 없는 편리 기능 — except 안에서 다른 예외만 던져도 인과가 살아남는다.
# - TS 의 `Error.cause` 는 ES2022 에 와서야 표준화됐다. 파이썬은 PEP 3134(2005) 부터 존재.
# - `except*` + ExceptionGroup 은 비동기 코드(`asyncio.TaskGroup`)에서 자연스럽게 등장한다 —
#   여러 자식 task 가 동시에 실패한 상황을 한 번에 받기 위함.


if __name__ == "__main__":
    print("=== 1. 자동 chaining (__context__) ===")
    try:
        load_config("/__nonexistent__/config.txt")
    except RuntimeError:
        traceback.print_exc(file=sys.stdout)

    print("\n=== 2. 명시적 chaining (from) ===")
    try:
        load_config2("/__nonexistent__/config.txt")
    except ConfigError:
        traceback.print_exc(file=sys.stdout)

    print("\n=== 3. 원인 숨김 (from None) ===")
    try:
        public_api("missing")
    except ValueError:
        traceback.print_exc(file=sys.stdout)

    print("\n=== 4. ExceptionGroup + except* ===")
    try:
        parse_many(["1", "a", "2", "b"])
    except* ValueError as eg:
        print(f"  ValueError 그룹 size = {len(eg.exceptions)}")
