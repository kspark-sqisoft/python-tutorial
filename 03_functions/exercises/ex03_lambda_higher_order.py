"""
연습문제 03 — lambda / 고차함수
TODO: 아래 people 리스트를 age 오름차순으로 정렬한 sorted_people 을 만드세요.
- sorted() 와 lambda 를 사용하세요.
- 원본 리스트 people 은 변경하지 마세요.
"""

people = [
    {"name": "서연", "age": 28},
    {"name": "민준", "age": 22},
    {"name": "지수", "age": 35},
    {"name": "현우", "age": 19},
]

# TODO: sorted_people 을 완성하세요
sorted_people = None  # 이 줄을 수정하세요


# ── 검증 (수정하지 마세요) ──
ages = [p["age"] for p in sorted_people]
assert ages == [19, 22, 28, 35], f"정렬 순서 오류: {ages}"
assert len(people) == 4, "원본 리스트가 변경됨"
print("OK")
