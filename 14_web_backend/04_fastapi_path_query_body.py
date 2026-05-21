"""
FastAPI 경로·쿼리·바디 매개변수 학습.
타입 힌트만으로 자동 캐스팅·유효성 검사·OpenAPI 문서가 생성된다.
TestClient 로 정상/비정상 요청을 모두 검증한다.
"""

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

# ──── 1. 앱 및 데이터 모델 ────

app = FastAPI(title="Path/Query/Body 예제")

# 인메모리 아이템 저장소
_items_db: dict[int, dict] = {
    1: {"id": 1, "name": "사과", "price": 1500},
    2: {"id": 2, "name": "바나나", "price": 800},
}


class ItemCreate(BaseModel):
    """아이템 생성 요청 바디 — pydantic 모델로 자동 검증된다."""
    name: str = Field(min_length=1, description="아이템 이름")
    price: int = Field(gt=0, description="가격은 0 초과이어야 한다")


class ItemResponse(BaseModel):
    """아이템 응답 모델."""
    id: int
    name: str
    price: int


# ──── 2. 경로 파라미터 ────

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    """경로 파라미터: item_id 는 int 로 자동 캐스팅된다.
    문자열이 들어오면 FastAPI 가 자동으로 422 를 반환한다."""
    if item_id not in _items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    return _items_db[item_id]


# ──── 3. 쿼리 파라미터 ────

@app.get("/items")
def list_items(q: str = "", limit: int = 10, offset: int = 0):
    """쿼리 파라미터: 함수 기본값이 있으면 선택적 쿼리 파라미터가 된다.
    예) GET /items?q=사과&limit=5"""
    results = list(_items_db.values())
    if q:
        results = [item for item in results if q in item["name"]]
    return {
        "items": results[offset : offset + limit],
        "total": len(results),
        "q": q,
        "limit": limit,
        "offset": offset,
    }


# ──── 4. 요청 바디 (POST) ────

@app.post("/items", status_code=201, response_model=ItemResponse)
def create_item(item: ItemCreate):
    """요청 바디: pydantic 모델로 선언하면 JSON 바디를 자동 파싱·검증한다.
    유효하지 않은 데이터는 422 Unprocessable Entity 로 거부된다."""
    new_id = max(_items_db.keys(), default=0) + 1
    new_item = {"id": new_id, **item.model_dump()}
    _items_db[new_id] = new_item
    return new_item


# ──── 5. TestClient 검증 ────

def run_tests() -> None:
    client = TestClient(app)

    # 경로 파라미터 — 정상
    r = client.get("/items/1")
    assert r.status_code == 200
    assert r.json()["name"] == "사과"
    print(f"  GET /items/1           : {r.status_code} → {r.json()}")

    # 경로 파라미터 — 존재하지 않는 ID
    r = client.get("/items/999")
    assert r.status_code == 404
    print(f"  GET /items/999         : {r.status_code} (404 예상)")

    # 경로 파라미터 — 타입 오류 (422)
    r = client.get("/items/abc")
    assert r.status_code == 422
    print(f"  GET /items/abc         : {r.status_code} (422 예상 — 타입 오류)")

    # 쿼리 파라미터
    r = client.get("/items", params={"q": "사과", "limit": 5})
    assert r.status_code == 200
    print(f"  GET /items?q=사과      : {r.status_code} → total={r.json()['total']}")

    # 요청 바디 — 정상
    r = client.post("/items", json={"name": "포도", "price": 2500})
    assert r.status_code == 201
    print(f"  POST /items (포도)     : {r.status_code} → {r.json()}")

    # 요청 바디 — 유효성 실패 (422)
    r = client.post("/items", json={"name": "", "price": -100})
    assert r.status_code == 422
    print(f"  POST /items (잘못된 값) : {r.status_code} (422 예상 — 유효성 실패)")


if __name__ == "__main__":
    print("=== 04_fastapi_path_query_body.py 데모 ===\n")

    print("1) 라우트 목록")
    for route in app.routes:
        if hasattr(route, "methods"):
            print(f"  {list(route.methods)} {route.path}")

    print("\n2) TestClient 로 각 패턴 검증")
    run_tests()

    print("\n3) OpenAPI 자동 문서 안내")
    print("  실제 서버 실행 시 http://localhost:8000/docs 에서 Swagger UI 제공")
    print("  http://localhost:8000/redoc 에서 ReDoc 제공")

    print("\n완료!")
