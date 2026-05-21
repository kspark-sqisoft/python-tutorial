"""
연습문제 02: 튜플 정렬.
좌표 점 5개를 y 좌표 오름차순으로 정렬하라.
"""

# 주어진 좌표 점 (변경하지 마세요)
points = [(1, 5), (3, 2), (7, 8), (2, 4), (5, 1)]

# TODO: sorted() 와 key=lambda 를 사용해 y 좌표(인덱스 1) 기준
#       오름차순으로 정렬한 새 리스트 sorted_pts 를 만드세요.
#       힌트: sorted(points, key=lambda p: p[...])
sorted_pts = None

# ── 검증 ──
assert sorted_pts is not None, "sorted_pts 를 구현하세요"
assert sorted_pts == [(5, 1), (3, 2), (2, 4), (1, 5), (7, 8)], (
    f"sorted_pts 가 올바르지 않습니다: {sorted_pts}"
)
print("OK")
