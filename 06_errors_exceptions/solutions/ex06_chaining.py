"""
풀이 06: 예외 chaining.

- `raise New from orig` 은 e.__cause__ 를 채워 "직접적 원인" 으로 트레이스백에 표시한다.
- `raise New from None` 은 e.__suppress_context__ = True 로 만들어 내부 트레이스백 노이즈를 숨긴다.
- `ExceptionGroup` + `except*` 는 여러 부분 실패를 한 번에 묶어 다루는 3.11+ 도구.
"""


class ConfigError(RuntimeError):
    pass


def load(config: dict, key: str) -> int:
    try:
        return config[key]
    except KeyError as orig:
        raise ConfigError("로드 실패") from orig


try:
    load({"a": 1}, "missing")
except ConfigError as e:
    assert isinstance(e.__cause__, KeyError)


def parse(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        raise LookupError("잘못된 형식") from None


try:
    parse("not a number")
except LookupError as e:
    assert e.__cause__ is None
    assert e.__suppress_context__ is True


def parse_many(items: list[str]) -> list[int]:
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
    assert len(eg.exceptions) == 2


print("OK")
