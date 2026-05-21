"""
연습문제 05: 컴프리헨션으로 구구단 딕셔너리 만들기.
(i, j) → i*j 매핑 딕셔너리를 컴프리헨션 한 줄로 만들어라.
"""

# TODO: 딕셔너리 컴프리헨션을 사용해 1~9 구구단 전체를
#       {(i, j): i*j} 형태의 딕셔너리 table 로 만드세요.
#       힌트: {(i, j): i*j for i in range(1, 10) for j in range(1, 10)}
table = None

# ── 검증 ──
assert table is not None, "table 을 구현하세요"
assert table[(3, 4)] == 12, f"(3,4) 항목이 올바르지 않습니다: {table.get((3,4))}"
assert table[(9, 9)] == 81, f"(9,9) 항목이 올바르지 않습니다: {table.get((9,9))}"
assert table[(1, 1)] == 1,  f"(1,1) 항목이 올바르지 않습니다: {table.get((1,1))}"
assert len(table) == 81, f"항목 수가 올바르지 않습니다: {len(table)}"
print("OK")
