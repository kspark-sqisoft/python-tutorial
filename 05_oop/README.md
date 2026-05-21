# 05_oop — 객체지향 프로그래밍

## 배우는 것
- 클래스/인스턴스/메서드/self, 클래스 속성 vs 인스턴스 속성
- 상속, super(), 메서드 오버라이드, isinstance/issubclass, 다형성
- 매직 메서드 (`__init__`, `__repr__`/`__str__`, `__eq__`/`__hash__`, `__add__`, `__len__`/`__iter__`/`__contains__`)
- `@dataclass` — boilerplate 제거 (필드 선언에 타입 힌트 필수이므로 이 폴더에서 유일하게 사용)
- `@property` — 캡슐화 (자바 getter/setter 와 비교)

## 학습 순서
1. `01_classes.py`
2. `02_inheritance.py`
3. `03_magic_methods.py`
4. `04_dataclass.py`
5. `05_property.py`

## 실행 방법
```bash
uv run python 05_oop/01_classes.py
```

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
- 막히면 `solutions/` 같은 번호 파일과 비교한다.
