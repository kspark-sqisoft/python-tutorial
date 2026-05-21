"""
풀이 04: 집합 연산.

set() 으로 리스트를 집합으로 변환한 뒤 &, |, - 연산자를 사용한다.
집합 연산자는 메서드(intersection, union, difference)와 동일하지만
연산자 표기가 수학적 의미를 더 직관적으로 드러낸다.
결과는 항상 새 집합이므로 원본 리스트는 변경되지 않는다.
"""

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

inter = set(a) & set(b)
union_ = set(a) | set(b)
diff = set(a) - set(b)

assert inter == {3, 4}
assert union_ == {1, 2, 3, 4, 5, 6}
assert diff == {1, 2}
print("OK")
