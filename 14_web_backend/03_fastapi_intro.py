"""
FastAPI 기초 — 라우트 정의와 TestClient 로 서버 없이 검증.
실제 uvicorn 서버를 띄우지 않고 TestClient 를 이용해
HTTP 요청/응답을 인메모리에서 처리한다.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

# ──── 1. 앱 생성 ────

app = FastAPI(title="FastAPI 튜토리얼", version="1.0.0")

# ──── 2. 라우트 정의 ────

@app.get("/")
def root() -> dict:
    """루트 엔드포인트 — 환영 메시지를 반환한다."""
    return {"message": "안녕하세요, FastAPI!"}


@app.get("/health")
def health_check() -> dict:
    """헬스 체크 — 서버 상태를 확인한다."""
    return {"status": "ok", "service": "python-tutorial"}


@app.get("/items")
def list_items() -> dict:
    """아이템 목록 — 하드코딩된 샘플 데이터를 반환한다."""
    items = [
        {"id": 1, "name": "사과", "price": 1500},
        {"id": 2, "name": "바나나", "price": 800},
        {"id": 3, "name": "체리", "price": 3000},
    ]
    return {"items": items, "total": len(items)}


@app.get("/echo/{text}")
def echo(text: str) -> dict:
    """에코 — 입력 문자열을 그대로 돌려준다."""
    return {"echo": text, "length": len(text)}


# ──── 3. TestClient 로 검증 ────

def run_tests() -> None:
    """TestClient 를 사용해 각 라우트를 호출하고 응답을 확인한다."""
    client = TestClient(app)

    # GET /
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "안녕하세요, FastAPI!"
    print(f"  GET /         : {r.status_code} → {r.json()}")

    # GET /health
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    print(f"  GET /health   : {r.status_code} → {r.json()}")

    # GET /items
    r = client.get("/items")
    assert r.status_code == 200
    assert r.json()["total"] == 3
    print(f"  GET /items    : {r.status_code} → total={r.json()['total']}")

    # GET /echo/{text}
    r = client.get("/echo/hello")
    assert r.status_code == 200
    assert r.json()["echo"] == "hello"
    print(f"  GET /echo/hello : {r.status_code} → {r.json()}")


if __name__ == "__main__":
    print("=== 03_fastapi_intro.py 데모 ===\n")

    print("1) 앱 정보")
    print(f"  title   : {app.title}")
    print(f"  version : {app.version}")
    print(f"  라우트 수 : {len(app.routes)}")

    print("\n2) TestClient 로 각 라우트 호출")
    run_tests()

    print("\n3) OpenAPI 문서")
    client = TestClient(app)
    r = client.get("/openapi.json")
    schema = r.json()
    print(f"  /openapi.json 상태코드: {r.status_code}")
    print(f"  정의된 경로들: {list(schema['paths'].keys())}")

    print("\n완료! (실제 서버 없이 TestClient 로 모두 검증)")
