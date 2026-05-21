"""연습: import 기초 — math 모듈로 원의 둘레 계산."""

# TODO: math 에서 sqrt 와 pi 를 import 하라
# from math import ...

# TODO: 반지름 5인 원의 둘레를 circumference 변수에 저장하라
# circumference = ...

assert abs(circumference - 2 * 3.141592653589793 * 5) < 1e-9, "원의 둘레 계산이 틀렸습니다"
print("OK")
