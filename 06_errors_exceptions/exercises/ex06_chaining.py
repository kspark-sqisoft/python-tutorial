"""
연습문제 06: 예외 chaining — `raise X from Y`, `from None`, ExceptionGroup.

3개 TODO 를 채워 'OK' 가 출력되게 만드세요.
정답은 `solutions/ex06_chaining.py`.
"""


# ──── TODO 1: 명시적 chaining ────
# load() 가 KeyError 를 받으면, 그것을 원인으로 하는 새 RuntimeError("로드 실패") 를 던지세요.
# 힌트: `raise RuntimeError(...) from orig`

class ConfigError(RuntimeError):
    pass


def load(config: dict, key: str) -> int:
    try:
        return config[key]
    except KeyError as orig:
        # TODO: orig 를 원인으로 명시한 ConfigError("로드 실패") 를 던지세요.
        raise


try:
    load({"a": 1}, "missing")
except ConfigError as e:
    assert isinstance(e.__cause__, KeyError), "__cause__ 가 KeyError 여야 합니다 (from 누락?)"


# ──── TODO 2: 원인 숨기기 — from None ────
# parse() 가 ValueError 를 받으면, 내부 원인을 숨기고 LookupError("잘못된 형식") 만 노출하세요.

def parse(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        # TODO: 내부 ValueError 를 숨기고 LookupError 만 노출하세요. `from None` 사용.
        raise


try:
    parse("not a number")
except LookupError as e:
    assert e.__cause__ is None, "__cause__ 는 None 이어야 합니다"
    assert e.__suppress_context__ is True, "from None 이 누락된 것 같습니다"


# ──── TODO 3: ExceptionGroup + except* ────
# 여러 입력을 한꺼번에 파싱하다가 발생한 ValueError 들을 모아 ExceptionGroup 으로 던지는 함수를 완성하세요.

def parse_many(items: list[str]) -> list[int]:
    ok: list[int] = []
    errors: list[Exception] = []
    for x in items:
        try:
            ok.append(int(x))
        except ValueError as e:
            errors.append(e)
    if errors:
        # TODO: ExceptionGroup("parse 실패", errors) 를 던지세요.
        raise NotImplementedError
    return ok


try:
    parse_many(["1", "a", "2", "b"])
except* ValueError as eg:
    assert len(eg.exceptions) == 2, "ValueError 가 정확히 2개 모여 있어야 합니다"


print("OK")
