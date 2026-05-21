"""
함수 기본 (Function Basics)
- def 키워드로 함수를 정의하고 return 으로 값을 돌려준다.
- 기본 인자(default argument)로 선택적 매개변수를 만들 수 있다.
- 가변 기본 인자(mutable default) 함정을 주의해야 한다.
- Java/C++ 과 달리 반환 타입 선언이 없고, 함수 자체가 일급 객체다.
"""

# ──── 1. 기본 def / return ────

def add(a, b):
    """두 수를 더해 반환한다."""  # docstring — help(add) 로 볼 수 있다
    return a + b


def greet(name, greeting="안녕"):   # greeting 에 기본값 지정
    """이름과 인사말로 문자열을 만들어 반환한다."""
    return f"{greeting}, {name}!"


# ──── 2. 가변 기본 인자 함정 ────

# 위험한 패턴: 기본값 lst=[] 는 함수 정의 시 딱 한 번만 생성된다.
# 호출할 때마다 같은 리스트 객체를 재사용하므로 값이 쌓인다.
def append_to_bad(item, lst=[]):    # 위험: 공유 리스트
    lst.append(item)
    return lst


# 권장 패턴: None 을 기본값으로 두고 함수 내부에서 새 리스트를 만든다.
def append_to_good(item, lst=None): # 안전: 매 호출마다 새 리스트
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# ──── 3. 키워드 인자로 호출 ────

def describe(name, age, city="서울"):
    """인물 정보를 문자열로 반환한다."""
    return f"{name}, {age}세, {city} 거주"


# ──── 4. docstring 확인 ────

# help(add) 를 실행하면 docstring 이 터미널에 출력된다.
# 여기서는 __doc__ 속성으로 간단히 확인한다.


if __name__ == "__main__":
    # ── 기본 add / greet ──
    print(add(3, 4))                        # 7
    print(add(10, 20))                      # 30
    print(greet("지수"))                    # 안녕, 지수!
    print(greet("민준", greeting="반가워")) # 반가워, 민준!

    # ── 가변 기본 인자 함정 시연 ──
    print(append_to_bad(1))   # [1]
    print(append_to_bad(2))   # [1, 2]  ← 1 이 남아 있다!
    print(append_to_bad(3))   # [1, 2, 3]  ← 계속 쌓인다

    print(append_to_good(1))  # [1]
    print(append_to_good(2))  # [2]   ← 독립적
    print(append_to_good(3))  # [3]   ← 독립적

    # ── 키워드 인자 ──
    print(describe("서연", 25))                        # 서울 (기본값)
    print(describe(age=30, name="현우", city="부산"))  # 순서 무관

    # ── docstring ──
    print(add.__doc__)        # '두 수를 더해 반환한다.'
