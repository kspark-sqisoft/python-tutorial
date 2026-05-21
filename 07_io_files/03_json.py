"""
JSON 직렬화/역직렬화 — json 모듈
dumps/loads 는 문자열 변환, dump/load 는 파일 IO.
ensure_ascii=False 로 한글을 그대로 저장한다.
"""

import json
import tempfile
import os

# ──── 1. dumps — 객체 → JSON 문자열 ────

def demo_dumps():
    # indent=2: 읽기 좋게 들여쓰기, ensure_ascii=False: 한글 유지
    data = {
        "이름": "홍길동",
        "나이": 30,
        "점수": [95, 87, 91],
        "활성": True,
        "메모": None,
    }
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    return json_str


# ──── 2. loads — JSON 문자열 → 객체 ────

def demo_loads(json_str):
    # JSON 타입 → Python 타입 매핑
    # object → dict, array → list, string → str
    # number → int/float, true/false → True/False, null → None
    obj = json.loads(json_str)
    return obj


# ──── 3. ensure_ascii 비교 ────

def demo_ensure_ascii():
    sample = {"메시지": "안녕하세요"}
    escaped   = json.dumps(sample, ensure_ascii=True)   # \uXXXX 이스케이프
    preserved = json.dumps(sample, ensure_ascii=False)  # 한글 그대로
    return escaped, preserved


# ──── 4. dump / load — 파일 IO ────

def demo_file_io(path):
    data = {
        "언어": "Python",
        "버전": 3,
        "특징": ["동적 타입", "인터프리터", "오픈소스"],
    }
    # dump: 파일에 직접 쓰기
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # load: 파일에서 직접 읽기
    with open(path, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    return data, loaded


# ──── 5. 직렬화 불가 타입 ────

def demo_custom_default():
    # dict/list/str/int/float/bool/None 외 타입은 기본적으로 직렬화 불가
    # default= 인자로 변환 함수를 전달하면 커스텀 객체도 처리할 수 있다
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def point_to_dict(obj):
        if isinstance(obj, Point):
            return {"x": obj.x, "y": obj.y}
        raise TypeError(f"직렬화 불가: {type(obj)}")

    p = Point(3, 4)
    return json.dumps(p, default=point_to_dict)


if __name__ == "__main__":
    print("=== dumps (ensure_ascii=False) ===")
    json_str = demo_dumps()
    print(json_str)

    print("=== loads 왕복 ===")
    obj = demo_loads(json_str)
    print(f"이름: {obj['이름']}, 점수 합계: {sum(obj['점수'])}")

    print("\n=== ensure_ascii 비교 ===")
    escaped, preserved = demo_ensure_ascii()
    print(f"True  → {escaped}")
    print(f"False → {preserved}")

    print("\n=== 파일 dump / load ===")
    tmp = tempfile.NamedTemporaryFile(
        delete=False, suffix=".json", mode="w", encoding="utf-8"
    )
    tmp_path = tmp.name
    tmp.close()

    original, loaded = demo_file_io(tmp_path)
    print(f"동일한가: {original == loaded}")

    with open(tmp_path, "r", encoding="utf-8") as f:
        print(f.read())

    print("=== 커스텀 default ===")
    print(demo_custom_default())

    os.unlink(tmp_path)
    print("임시 파일 정리 완료.")
