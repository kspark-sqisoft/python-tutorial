"""
이터레이터 프로토콜 — iter()와 next() 함수의 동작 방식.
이터러블(iterable)과 이터레이터(iterator)의 차이,
StopIteration 예외, 이터레이터 소진 개념을 다룬다.
"""

# ──── 1. 이터러블 vs 이터레이터 ────

# 이터러블: __iter__() 를 가진 객체 — list, str, tuple, range 등
fruits = ["사과", "바나나", "포도"]

# iter() 에 이터러블을 넘기면 이터레이터 객체가 반환된다
it = iter(fruits)
print("이터레이터 객체:", it)  # list_iterator

# ──── 2. next() — 한 번에 하나씩 꺼내기 ────

# next() 는 이터레이터에서 다음 항목을 하나 꺼낸다
first = next(it)   # 첫 번째
second = next(it)  # 두 번째
third = next(it)   # 세 번째
print("순서대로:", first, second, third)

# ──── 3. StopIteration — 이터레이터가 소진되면 발생 ────

# 더 꺼낼 항목이 없으면 StopIteration 예외가 발생한다
try:
    next(it)  # 이미 세 개를 모두 꺼냈으므로 예외 발생
except StopIteration:
    print("StopIteration 발생 — 이터레이터가 소진됨")

# ──── 4. 이터레이터는 한 번만 순회 가능 ────

# 소진된 이터레이터를 다시 for 로 순회해도 아무것도 나오지 않는다
print("소진 후 for 루프 결과:", list(it))  # 빈 리스트

# 반면 이터러블(list 자체)은 몇 번이든 새 이터레이터를 만들 수 있다
print("fruits 다시 순회:", list(fruits))  # 정상 출력

# ──── 5. for 루프의 내부 동작 ────

# for x in seq: 는 내부적으로 iter(seq) 후 next() 를 반복 호출한다
# StopIteration 을 만나면 루프가 종료된다
print("for 루프 내부 동작 재현:")
it2 = iter([10, 20, 30])
while True:
    try:
        value = next(it2)
        print(" ", value)
    except StopIteration:
        break  # 루프 종료 조건


if __name__ == "__main__":
    print("\n=== 데모: iter / next / StopIteration ===")

    nums = [100, 200, 300]
    demo_it = iter(nums)

    print("next() 3번:")
    print(" ", next(demo_it))  # 100
    print(" ", next(demo_it))  # 200
    print(" ", next(demo_it))  # 300

    print("4번째 next() — StopIteration 잡기:")
    try:
        next(demo_it)
    except StopIteration:
        print("  예외 포착 완료")
