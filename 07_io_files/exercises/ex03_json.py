"""
연습 03 — JSON 왕복과 ensure_ascii=False 검증
dict 를 json.dumps(ensure_ascii=False) → json.loads 왕복 후 동일성을 확인하고,
한글이 유니코드 이스케이프 없이 그대로 유지되는지 검증한다.
"""

import json

def exercise():
    data = {"name": "Kee", "scores": [90, 85]}

    # TODO: json.dumps(data, ensure_ascii=False) 로 JSON 문자열을 만든다
    json_str = None

    # TODO: json.loads(json_str) 로 다시 객체로 변환한다
    loaded = None

    # TODO: data == loaded 인지 assert 한다
    assert data == loaded, f"왕복 후 값이 달라졌습니다: {loaded}"

    # 한글 키/값이 있을 때 ensure_ascii=False 효과 확인
    korean_data = {"메시지": "안녕"}
    # TODO: json.dumps(korean_data, ensure_ascii=False) 결과에
    #       "\u" 가 포함되지 않는지 assert 한다
    korean_str = None
    assert korean_str is not None, "korean_str 을 구현하세요"
    assert "\\u" not in korean_str, f"한글이 이스케이프됐습니다: {korean_str}"

    print("OK")

if __name__ == "__main__":
    exercise()
