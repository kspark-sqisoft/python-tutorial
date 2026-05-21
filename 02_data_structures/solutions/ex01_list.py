"""
풀이 01: 리스트 생성과 필터링.

list(range(1, 11)) 은 1 이상 11 미만의 정수를 순서대로 담은 리스트를 만드는
가장 간결한 파이썬 관용구다. 컴프리헨션 [x for x in nums if x % 2 == 0] 은
for 루프 + append 패턴을 한 줄로 압축하여 의도를 명확히 드러낸다.
"""

nums = list(range(1, 11))
evens = [x for x in nums if x % 2 == 0]

assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert evens == [2, 4, 6, 8, 10]
print("OK")
