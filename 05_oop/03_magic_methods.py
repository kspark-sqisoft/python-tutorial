"""
매직 메서드 — __init__, __repr__, __str__, __eq__, __hash__,
__len__, __iter__, __contains__, __add__ 등 연산자 오버로딩.
"""

# ──── 1. __repr__ 과 __str__ 차이 ────

# __repr__: 디버그·개발용 — 객체를 재현할 수 있는 명확한 문자열 (eval 가능하면 이상적)
# __str__:  사용자용 — print() 나 str() 호출 시 사용
# __repr__ 만 정의하면 __str__ 도 같이 동작한다 (fallback)

class Vector:
    """2차원 벡터. 매직 메서드로 연산자 오버로딩을 시연한다."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 디버그용: eval(repr(v)) 로 복원 가능한 형태
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        # == 연산자 오버로딩
        if not isinstance(other, Vector):
            return NotImplemented  # 다른 타입과는 비교 안 함
        return self.x == other.x and self.y == other.y

    # __eq__ 를 정의하면 기본 __hash__ 가 None 이 되므로 같이 정의해야 한다.
    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        # + 연산자 오버로딩 — 새 Vector 를 반환 (불변 패턴)
        return Vector(self.x + other.x, self.y + other.y)


# ──── 2. 컬렉션 매직 메서드 ────

# __len__:      len(obj) 호출 시
# __iter__:     for x in obj / iter(obj) 호출 시
# __contains__: in 연산자 사용 시

class Bag:
    """간단한 컬렉션 클래스. 컬렉션 매직 메서드를 구현한다."""

    def __init__(self, *items):
        self._items = list(items)  # 내부 저장소

    def add(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # 내부 리스트의 이터레이터를 그대로 위임
        return iter(self._items)

    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        return f"Bag({self._items})"


# ──── 3. 데모 ────

if __name__ == "__main__":
    print("=== Vector 연산 ===")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(f"v1 = {v1!r}")           # repr 명시적 호출
    print(f"v2 = {v2!r}")
    print(f"v1 + v2 = {v3!r}")      # Vector(4, 6)
    print(f"v3 == Vector(4, 6): {v3 == Vector(4, 6)}")  # True
    print(f"hash(Vector(1,2)): {hash(Vector(1,2))}")

    print()
    print("=== Bag 컬렉션 ===")
    bag = Bag("사과", "바나나", "체리")
    print(f"len(bag) = {len(bag)}")          # 3

    print("bag 안의 항목:")
    for item in bag:                          # __iter__ 사용
        print(f"  {item}")

    print(f"'사과' in bag: {'사과' in bag}")   # True, __contains__ 사용
    print(f"'포도' in bag: {'포도' in bag}")   # False
