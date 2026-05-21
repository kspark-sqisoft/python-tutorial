"""정답: date + timedelta 로 날짜 산술을 한 뒤 strftime 으로 문자열로 변환한다.
timedelta(days=30) 은 30일을 나타내는 기간(duration) 객체이다.
strftime('%Y-%m-%d') 는 날짜를 'YYYY-MM-DD' 형식 문자열로 만든다."""

from datetime import date, timedelta

start = date(2026, 1, 1)
result = (start + timedelta(days=30)).strftime("%Y-%m-%d")

assert result == "2026-01-31", f"기댓값 '2026-01-31', 실제: {result}"
print("OK")
