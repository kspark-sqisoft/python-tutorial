"""
정답 03 — JSON 왕복과 ensure_ascii=False 검증
json.dumps(ensure_ascii=False) 는 한글을 유니코드 이스케이프 없이 그대로 저장한다.
dumps → loads 왕복 후 원본 dict 와 동일성을 assert 한다.
"""

import json

def exercise():
    data = {"name": "Kee", "scores": [90, 85]}

    # ensure_ascii=False: 한글·한자 등 비ASCII 문자를 그대로 유지
    json_str = json.dumps(data, ensure_ascii=False)

    # 문자열 → 객체로 역직렬화
    loaded = json.loads(json_str)

    assert data == loaded, f"왕복 후 값이 달라졌습니다: {loaded}"

    # 한글이 이스케이프되지 않았는지 확인
    korean_data = {"메시지": "안녕"}
    korean_str = json.dumps(korean_data, ensure_ascii=False)
    assert "\\u" not in korean_str, f"한글이 이스케이프됐습니다: {korean_str}"

    print("OK")

if __name__ == "__main__":
    exercise()
