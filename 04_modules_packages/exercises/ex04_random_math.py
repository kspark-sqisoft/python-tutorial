"""연습: random — seed 고정 후 randint 3번 호출."""

import random

# TODO: random.seed(7) 로 시드를 고정하라
# random.seed(7)

# TODO: randint(1, 100) 을 3번 호출해 리스트 picks 에 담아라
# picks = [random.randint(1, 100) for _ in range(3)]

expected = [42, 20, 51]
assert picks == expected, f"기댓값 {expected}, 실제: {picks}"
print("OK")
