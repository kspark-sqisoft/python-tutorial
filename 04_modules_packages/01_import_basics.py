"""import 의 4가지 형태를 익힌다.
모듈을 불러오는 방법은 여러 가지이며,
각각 장단점이 있다. 관례적으로 import 문은 파일 상단에 작성한다.
"""

# ──── 1. 기본 import ────
import math  # math 모듈 전체를 가져온다

# ──── 2. from ... import ────
from math import sqrt, pi  # 특정 이름만 직접 가져온다

# ──── 3. 별칭 import (as) ────
import math as m  # 모듈에 짧은 이름을 붙인다 (numpy as np 처럼)

# ──── 4. from ... import ... as ────
from math import sqrt as root  # 이름 충돌 방지나 축약 목적 (권장은 영어 식별자 유지)

# ──── 5. __name__ 과 import ────
# 이 파일을 import 할 때 if __name__ == "__main__": 블록은 실행되지 않는다.
# import 시 __name__ 은 모듈 이름(문자열)이 되어 "__main__" 과 달라지기 때문이다.

if __name__ == "__main__":
    # 4가지 방식으로 sqrt(16) 을 호출 — 모두 4.0
    result1 = math.sqrt(16)      # 방식 1: 모듈명.함수명
    result2 = sqrt(16)           # 방식 2: 직접 이름
    result3 = m.sqrt(16)         # 방식 3: 별칭.함수명
    result4 = root(16)           # 방식 4: 함수 별칭

    print(f"math.sqrt(16)  = {result1}")
    print(f"sqrt(16)       = {result2}")
    print(f"m.sqrt(16)     = {result3}")
    print(f"root(16)       = {result4}")
    print(f"모두 같은 결과: {result1 == result2 == result3 == result4}")
    print(f"pi = {pi:.6f}")
