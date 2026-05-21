"""
정답 04 — 동적 클래스 생성

핵심 아이디어:
  type(이름, 베이스 튜플, 속성 딕트) 는 클래스를 런타임에 생성한다.
  이것은 class 문이 내부적으로 하는 일과 정확히 동일하다.

왜 동적 생성이 유용한가?
  플러그인 시스템, ORM, API 클라이언트 등에서
  실행 시점에 스키마나 설정을 읽어 클래스를 자동으로 만들 때 활용된다.
  예: Django 의 모델 메타클래스, dataclasses.make_dataclass().
"""

# type(이름, 베이스 튜플, 속성 딕트)
Dynamic = type(
    "Dynamic",                              # 클래스 이름
    (),                                     # 베이스 없음 → object 상속
    {"greet": lambda self: "hi"},           # greet 메서드
)


# ──── 검증 ────

assert Dynamic is not None
assert Dynamic.__name__ == "Dynamic"

obj = Dynamic()
assert hasattr(obj, "greet")
assert obj.greet() == "hi"

obj2 = Dynamic()
assert obj2.greet() == "hi"

print("OK")
