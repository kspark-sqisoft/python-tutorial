"""자체 패키지를 만들고 import 하는 방법을 익힌다.
같은 폴더의 mypkg/ 패키지에서 함수를 가져와 사용한다.
__init__.py 가 있어야 Python 이 해당 폴더를 패키지로 인식한다.
"""

# ──── 1. 패키지 import ────
from mypkg.greet import hello       # mypkg 패키지의 greet 모듈에서 hello 함수
from mypkg.calc import add, multiply  # mypkg 패키지의 calc 모듈에서 두 함수

# ──── 2. __init__.py 의 역할 ────
# 폴더 안에 __init__.py 파일이 있으면 그 폴더가 '패키지'로 취급된다.
# __init__.py 는 패키지가 처음 import 될 때 한 번 실행된다.
# 패키지 수준 공개 API 를 여기에 모아 두기도 한다.

if __name__ == "__main__":
    # hello 함수 호출
    greeting = hello("파이썬")
    print(greeting)

    # 산술 함수 호출
    total = add(2, 3)
    product = multiply(4, 5)
    print(f"add(2, 3)      = {total}")
    print(f"multiply(4, 5) = {product}")
