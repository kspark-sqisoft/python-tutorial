"""정답: from math import 로 특정 이름만 가져오면
모듈 접두사 없이 바로 사용할 수 있어 코드가 짧아진다.
pi 는 상수이므로 별도 계산 없이 그대로 쓴다."""

from math import sqrt, pi

circumference = 2 * pi * 5

assert abs(circumference - 2 * 3.141592653589793 * 5) < 1e-9
print("OK")
