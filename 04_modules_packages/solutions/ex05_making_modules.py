"""정답: from _my_module import 으로 같은 폴더의 모듈을 가져온다.
언더스코어(_) 로 시작하는 모듈은 '내부용' 관례이지만 import 자체는 가능하다.
패키지 없이 단순 .py 파일도 모듈로 import 할 수 있다."""

from _my_module import double, triple

assert double(5) == 10
assert triple(4) == 12
print("OK")
