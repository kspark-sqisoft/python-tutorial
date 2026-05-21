"""
정답 02 — 숫자와 연산자

** 연산자는 거듭제곱이며 Python int 의 임의 정밀도 덕분에 큰 수도 정확히 계산된다.
divmod(a, b) 는 (a // b, a % b) 튜플을 한 번의 연산으로 반환해
몫과 나머지를 동시에 구할 때 나눗셈을 두 번 수행하는 비용을 줄여준다.
"""

power = 2 ** 10
q, r = divmod(17, 5)

assert power == 1024
assert q == 3
assert r == 2

print("OK")
