"""
풀이 05: 컴프리헨션으로 구구단 딕셔너리 만들기.

딕셔너리 컴프리헨션에 이중 for 절을 사용하면 중첩 루프를 한 줄로 표현할 수 있다.
튜플 (i, j) 를 키로 쓸 수 있는 이유는 튜플이 불변(hashable)이기 때문이다.
range(1, 10) 이 1~9 를 생성하므로 9×9=81 개의 항목이 만들어진다.
"""

table = {(i, j): i * j for i in range(1, 10) for j in range(1, 10)}

assert table[(3, 4)] == 12
assert table[(9, 9)] == 81
assert table[(1, 1)] == 1
assert len(table) == 81
print("OK")
