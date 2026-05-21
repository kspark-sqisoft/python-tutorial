"""
dict — 파이썬의 해시맵(hash map) 자료구조.
Java의 HashMap, JavaScript의 Object/Map과 유사.
키-값 쌍을 저장하며, 키는 불변(hashable) 타입만 가능.
Python 3.7+ 부터 삽입 순서가 보장된다.
"""

# ──── 1. 딕셔너리 생성 ────

empty = {}                              # 빈 딕셔너리 (set()과 구분!)
person = {"name": "철수", "age": 25}   # 키-값 쌍으로 직접 생성
from_kwargs = dict(name="영희", age=30) # dict() + 키워드 인수
from_pairs = dict([("a", 1), ("b", 2)]) # (키, 값) 튜플 리스트로 생성

# ──── 2. 값 접근 ────

name = person["name"]               # 키로 직접 접근 → "철수"
age = person.get("age")             # get()으로 접근 (키 없어도 안전)
missing = person.get("email", "없음")  # 없으면 기본값 반환
exists = "name" in person           # 키 존재 여부 → True
not_exists = "email" not in person  # → True

# ──── 3. 값 변경·추가·삭제 ────

d = {"x": 1, "y": 2}

d["z"] = 3          # 새 키-값 추가
d["x"] = 10         # 기존 키의 값 변경
d.update({"y": 20, "w": 4})  # 여러 키-값 한 번에 갱신
del d["w"]          # 키 삭제 (없으면 KeyError)
val = d.pop("z")    # 키를 삭제하고 값을 반환
val2 = d.pop("없는키", 0)  # 없는 키는 기본값 반환

# ──── 4. 유용한 메서드 ────

info = {"a": 1, "b": 2, "c": 3}

keys = list(info.keys())     # 키 목록 → ['a', 'b', 'c']
values = list(info.values()) # 값 목록 → [1, 2, 3]
items = list(info.items())   # (키, 값) 튜플 목록

size = len(info)             # 키-값 쌍 개수 → 3

# ──── 5. 딕셔너리 순회 ────

scores = {"수학": 85, "영어": 92, "과학": 78}

# 키만 순회
for subject in scores:
    pass  # subject = "수학", "영어", "과학"

# 값만 순회
for score in scores.values():
    pass

# 키-값 동시 순회 (가장 많이 쓰는 패턴)
for subject, score in scores.items():
    pass  # subject="수학", score=85 ...

# ──── 6. 삽입 순서 보장 (Python 3.7+) ────

ordered = {}
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3
# list(ordered.keys()) → ['first', 'second', 'third']  (삽입 순서 유지)

# ──── 7. setdefault — 키 없을 때만 설정 ────

counter = {}
word = "hello"
counter.setdefault(word, 0)   # 없으면 0으로 초기화
counter[word] += 1            # 이후에 증가


def count_words(sentence):
    """문장에서 각 단어의 빈도를 딕셔너리로 반환."""
    result = {}
    for word in sentence.split():
        result[word] = result.get(word, 0) + 1  # 없으면 0, 있으면 기존값에 +1
    return result


if __name__ == "__main__":
    # 데모: 5개 단어 빈도 세기
    sentence = "사과 바나나 사과 오렌지 바나나 사과 포도 오렌지"
    freq = count_words(sentence)

    print("단어 빈도:")
    for word, count in freq.items():
        print(f"  {word}: {count}회")

    print("\n가장 많이 나온 단어:", max(freq, key=freq.get))
    print("전체 단어 종류:", len(freq), "가지")
