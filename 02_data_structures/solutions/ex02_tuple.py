"""
풀이 02: 튜플 정렬.

sorted() 는 원본을 변경하지 않고 새 리스트를 반환한다. key=lambda p: p[1] 로
각 튜플의 y 좌표(인덱스 1)를 정렬 기준으로 지정한다. 람다는 간단한 키 추출에
적합하며, operator.itemgetter(1) 로 대체해도 동일하게 동작한다.
"""

points = [(1, 5), (3, 2), (7, 8), (2, 4), (5, 1)]
sorted_pts = sorted(points, key=lambda p: p[1])

assert sorted_pts == [(5, 1), (3, 2), (2, 4), (1, 5), (7, 8)]
print("OK")
