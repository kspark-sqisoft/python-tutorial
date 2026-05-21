"""정답: Path(__file__).parent 는 '현재 스크립트가 위치한 디렉터리'를 반환한다.
__file__ 은 Python 이 실행 중인 파일의 경로를 담은 내장 변수이다.
.parent 속성으로 한 단계 위 디렉터리를 얻는다."""

from pathlib import Path

here = Path(__file__).parent

assert here.name in ("exercises", "solutions"), f"폴더 이름이 'exercises' 또는 'solutions' 여야 합니다. 현재: {here.name}"
print("OK")
