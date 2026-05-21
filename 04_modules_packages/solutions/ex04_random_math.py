"""정답: random.seed(7) 로 시드를 고정하면 같은 코드를 실행할 때마다
동일한 난수 시퀀스가 재현된다. 테스트나 디버깅에서 유용하다.
seed(7) 후 randint(1,100) × 3 의 결과는 [42, 20, 51] 이다."""

import random

random.seed(7)
picks = [random.randint(1, 100) for _ in range(3)]

expected = [42, 20, 51]
assert picks == expected, f"기댓값 {expected}, 실제: {picks}"
print("OK")
