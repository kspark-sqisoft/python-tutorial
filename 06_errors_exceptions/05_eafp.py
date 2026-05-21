"""
EAFP(Easier to Ask Forgiveness than Permission) vs LBYL(Look Before You Leap).
파이썬은 EAFP 를 관용적으로 선호하며, 경쟁 상황에서 EAFP 가 더 안전하다.
두 방식 모두 이해하고 상황에 맞게 선택한다.
"""

import os

# ──── 1. dict 접근 비교 ────

SCORES = {"alice": 95, "bob": 82}

def get_score_lbyl(name):
    # LBYL: 먼저 키가 있는지 확인 후 접근
    if name in SCORES:
        return SCORES[name]
    return 0  # 기본값

def get_score_eafp(name):
    # EAFP: 그냥 접근하고 KeyError 가 나면 처리
    try:
        return SCORES[name]
    except KeyError:
        return 0  # 기본값

def get_score_get(name):
    # dict.get() 은 LBYL 과 EAFP 사이의 편의 메서드
    return SCORES.get(name, 0)

# ──── 2. 파일 열기 비교 ────

def read_file_lbyl(path):
    # LBYL: 파일 존재 여부를 먼저 확인
    # 문제: exists() 와 open() 사이에 파일이 삭제될 수 있다 (경쟁 상황)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

def read_file_eafp(path):
    # EAFP: 그냥 열고 없으면 FileNotFoundError 처리
    # 경쟁 상황에서도 안전 — 파일이 사라져도 예외로 처리됨
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

# ──── 3. 타입 변환 비교 ────

def to_int_lbyl(value):
    # LBYL: str 인지, 숫자 형태인지 미리 확인
    if isinstance(value, str) and value.strip().lstrip("-").isdigit():
        return int(value)
    if isinstance(value, int):
        return value
    return None

def to_int_eafp(value):
    # EAFP: 변환 시도 후 실패하면 None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# ──── 4. 언제 어느 방식을? ────
#
# EAFP 선호 상황:
#   - 성공이 기대값이고 실패가 예외적인 경우
#   - 경쟁 상황(파일·소켓·DB) 처리
#   - 파이썬다운 코드를 원할 때
#
# LBYL 도 괜찮은 상황:
#   - 검사 비용이 낮고 실패가 흔한 경우
#   - 예외를 생성하는 비용을 줄이고 싶은 고성능 루프
#   - 코드 의도가 "사전 검증"임을 명확히 해야 할 때


if __name__ == "__main__":
    print("=== 1. dict 접근 — 세 방식 비교 ===")
    for name in ["alice", "charlie"]:
        lbyl = get_score_lbyl(name)
        eafp = get_score_eafp(name)
        via_get = get_score_get(name)
        print(f"  {name:10s} | LBYL={lbyl}, EAFP={eafp}, .get={via_get}")

    print("\n=== 2. 파일 열기 — 존재하지 않는 경로 ===")
    path = "/tmp/존재하지않는파일_eafp.txt"
    print(f"  LBYL 결과: {read_file_lbyl(path)}")
    print(f"  EAFP 결과: {read_file_eafp(path)}")

    print("\n=== 3. 타입 변환 — 여러 입력 ===")
    samples = ["42", "  -7  ", "abc", 10, None, 3.14]
    for v in samples:
        lbyl = to_int_lbyl(v)
        eafp = to_int_eafp(v)
        print(f"  {str(v):10s} | LBYL={lbyl}, EAFP={eafp}")

    print("\n=== 4. 핵심 정리 ===")
    print("  - 파이썬은 EAFP 선호 (예외는 비정상이 아니라 흐름 제어 수단)")
    print("  - 경쟁 상황에서는 EAFP 가 더 안전")
    print("  - 단순 딕셔너리 접근엔 .get() 도 좋은 선택")
