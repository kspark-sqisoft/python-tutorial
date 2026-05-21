"""datetime 모듈로 날짜와 시간을 다루는 방법을 익힌다.
날짜 산술, 포맷 변환(strftime/strptime), 타임존 기초를 다룬다.
시간 관련 작업에서 가장 자주 쓰이는 표준 라이브러리 중 하나이다.
"""

from datetime import datetime, date, timedelta, timezone  # 필요한 클래스만 가져온다

# ──── 1. 현재 날짜·시간 ────
now = datetime.now()    # 현재 로컬 날짜+시간
today = date.today()    # 오늘 날짜만 (시간 없음)

# ──── 2. 포맷 변환 ────
# strftime — datetime → 문자열 (format: str → formatted str)
# strptime — 문자열 → datetime (parse: str → datetime)
fmt = "%Y-%m-%d %H:%M:%S"  # 자주 쓰이는 포맷 지정자

formatted = now.strftime(fmt)                          # datetime → 문자열
parsed = datetime.strptime("2026-01-01", "%Y-%m-%d")  # 문자열 → datetime

# ──── 3. 날짜 산술 ────
# timedelta 로 날짜를 더하거나 뺄 수 있다
week_later = now + timedelta(days=7)       # 7일 후
hundred_later = now + timedelta(days=100)  # 100일 후
yesterday = today - timedelta(days=1)     # 어제

# ──── 4. 타임존 ────
utc_now = datetime.now(tz=timezone.utc)  # UTC 기준 현재 시각

if __name__ == "__main__":
    print(f"지금 (datetime.now): {now.strftime(fmt)}")
    print(f"오늘 (date.today):   {today}")
    print()
    print(f"파싱 결과 (strptime): {parsed}")
    print()
    print(f"일주일 후:  {week_later.strftime('%Y-%m-%d')}")
    print(f"100일 후:   {hundred_later.strftime('%Y-%m-%d')}")
    print(f"어제:       {yesterday}")
    print()
    print(f"UTC 현재: {utc_now.strftime(fmt)} UTC")
