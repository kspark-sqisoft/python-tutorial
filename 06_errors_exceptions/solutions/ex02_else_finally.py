"""
해설 — safe_divide

핵심 이유:
  else 절은 try 가 예외 없이 성공했을 때만 실행된다.
  finally 절은 예외 발생 여부와 무관하게 항상 실행된다.
  이 두 절의 조합으로 "성공 후 처리"와 "항상 정리"를 명확히 분리할 수 있다.
  실무에서는 DB 커넥션·파일 핸들 등의 자원 정리에 finally 를 쓰거나,
  더 간결하게 with 문을 사용한다.
"""

log = {"cleaned": False}


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        # try 가 성공했을 때만 — 결과값을 여기서 반환
        return result
    finally:
        # 항상 실행 — 자원 정리 or 상태 기록
        log["cleaned"] = True


# ── 검증 ──
log["cleaned"] = False
result = safe_divide(10, 2)
assert result == 5.0, f"예상 5.0, 실제 {result}"
assert log["cleaned"] is True, "finally 가 실행되지 않았습니다 (cleaned=False)"

log["cleaned"] = False
result2 = safe_divide(10, 0)
assert result2 is None, f"예상 None, 실제 {result2}"
assert log["cleaned"] is True, "finally 가 실행되지 않았습니다 (cleaned=False)"

print("OK")
