"""
property 와 캡슐화 — @property, setter, 단일/이중 언더스코어 관례.
자바의 getter/setter 와 달리 외부에서는 일반 속성처럼 보인다.
"""

# ──── 1. @property 기본 ────

# _attr  : 단일 언더스코어 = "내부 구현 세부사항이니 건드리지 말라"는 약속 (강제 아님)
# __attr : 이중 언더스코어 = 네임 맹글링(_클래스명__attr) 으로 외부 접근을 어렵게 만든다

class Temperature:
    """섭씨 온도를 관리하는 클래스. property 로 검증과 계산을 캡슐화한다."""

    def __init__(self, celsius):
        # setter 를 통해 초기화 — 검증 로직이 한 곳에만 있다
        self.celsius = celsius  # property setter 호출

    # ── getter ──
    @property
    def celsius(self):
        """섭씨 온도를 반환한다."""
        return self._celsius   # 실제 값은 _celsius 에 저장

    # ── setter ──
    @celsius.setter
    def celsius(self, value):
        """섭씨 온도를 설정한다. 절대영도 미만은 거부한다."""
        if value < -273.15:
            raise ValueError("절대영도 미만은 불가")
        self._celsius = value  # 검증 통과 후 저장

    # ── 계산된 read-only 프로퍼티 ──
    @property
    def fahrenheit(self):
        """섭씨 → 화씨 변환 (setter 없음 = read-only)."""
        return self._celsius * 9 / 5 + 32


# ──── 2. 자바 getter/setter 와 비교 ────

# 자바 스타일 (Python 에서도 작동하지만 비관용적):
#   temp.getCelsius()        → Python: temp.celsius
#   temp.setCelsius(100)     → Python: temp.celsius = 100
#
# @property 덕분에 외부 코드는 temp.celsius 처럼 일반 속성을 다루듯 쓰면서도
# 내부에서는 검증·변환 로직이 투명하게 실행된다.


# ──── 3. 데모 ────

if __name__ == "__main__":
    t = Temperature(100)
    print(f"섭씨: {t.celsius} °C")           # 100
    print(f"화씨: {t.fahrenheit} °F")         # 212.0

    t.celsius = 0
    print(f"변경 후 섭씨: {t.celsius} °C")    # 0
    print(f"변경 후 화씨: {t.fahrenheit} °F") # 32.0

    # 절대영도 미만 → ValueError
    try:
        t.celsius = -300
    except ValueError as e:
        print(f"예외 발생: {e}")

    # read-only 프로퍼티에 쓰기 시도 → AttributeError
    try:
        t.fahrenheit = 100
    except AttributeError as e:
        print(f"읽기 전용 속성: {e}")
