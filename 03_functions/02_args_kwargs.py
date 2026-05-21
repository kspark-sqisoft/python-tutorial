"""
가변 인자 *args / **kwargs
- *args 는 위치 인자를 튜플로 수집하고, **kwargs 는 키워드 인자를 dict 로 수집한다.
- 호출 시 *리스트 / **딕셔너리 로 언패킹해서 전달할 수 있다.
- def f(a, *, b) 형태로 키워드 전용 매개변수를 강제할 수 있다.
- Java 의 varargs(...)와 비슷하지만 키워드 인자 수집은 파이썬 고유 기능이다.
"""

# ──── 1. *args — 임의 개수의 위치 인자 ────

def sum_all(*args):
    """전달받은 모든 숫자를 합산한다. args 는 튜플."""
    total = 0
    for n in args:  # args 는 일반 튜플처럼 순회 가능
        total += n
    return total


def show_args(*args):
    """args 타입과 내용을 출력한다."""
    print(f"args 타입: {type(args)}, 값: {args}")


# ──── 2. **kwargs — 임의 개수의 키워드 인자 ────

def show_kwargs(**kwargs):
    """kwargs 타입과 내용을 출력한다. kwargs 는 dict."""
    print(f"kwargs 타입: {type(kwargs)}, 값: {kwargs}")


def build_profile(**kwargs):
    """키워드 인자로 받은 정보를 한 줄 문자열로 반환한다."""
    parts = [f"{k}={v}" for k, v in kwargs.items()]
    return ", ".join(parts)


# ──── 3. 혼합 시그니처 ────

def mixed(a, b, *args, **kwargs):
    """고정 인자 + 가변 위치 + 가변 키워드를 모두 받는다."""
    print(f"a={a}, b={b}, args={args}, kwargs={kwargs}")


# ──── 4. 호출 시 언패킹 ────

def add3(x, y, z):
    """세 수의 합을 반환한다."""
    return x + y + z


# ──── 5. 키워드 전용 매개변수 ────

def connect(host, port, *, timeout=30, retry=3):
    """* 뒤의 timeout, retry 는 반드시 키워드로만 전달해야 한다."""
    return f"{host}:{port} timeout={timeout} retry={retry}"


# ──── 6. 위치 전용 매개변수 (간단 언급) ────
# def f(a, /, b): 에서 a 는 위치 인자로만, b 는 어느 방식으로도 전달 가능
# Python 3.8+ 문법


if __name__ == "__main__":
    # ── *args ──
    print(sum_all(1, 2, 3))           # 6
    print(sum_all(10, 20, 30, 40))    # 100
    show_args(1, "안녕", True)        # 튜플 확인

    # ── **kwargs ──
    show_kwargs(이름="지수", 나이=25)
    print(build_profile(이름="민준", 도시="부산", 직업="개발자"))

    # ── 혼합 ──
    mixed(1, 2, 3, 4, 색="빨강", 크기=10)

    # ── 언패킹으로 호출 ──
    nums = [10, 20, 30]
    print(add3(*nums))                # 리스트 언패킹 → 60

    info = {"x": 1, "y": 2, "z": 3}
    print(add3(**info))               # dict 언패킹 → 6

    # ── 키워드 전용 매개변수 ──
    print(connect("localhost", 5432, timeout=10))
    # connect("localhost", 5432, 10)  # TypeError — timeout 은 키워드 필수
