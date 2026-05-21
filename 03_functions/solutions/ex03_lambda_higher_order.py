"""
정답 03 — lambda / 고차함수
왜 이렇게 구현하나:
- sorted() 는 원본을 변경하지 않고 새 리스트를 반환하므로 immutable 원칙에 부합한다.
- key=lambda p: p["age"] 로 각 dict 에서 age 값을 추출해 비교 기준으로 삼는다.
"""

people = [
    {"name": "서연", "age": 28},
    {"name": "민준", "age": 22},
    {"name": "지수", "age": 35},
    {"name": "현우", "age": 19},
]

sorted_people = sorted(people, key=lambda p: p["age"])

ages = [p["age"] for p in sorted_people]
assert ages == [19, 22, 28, 35], f"정렬 순서 오류: {ages}"
assert len(people) == 4
print("OK")
