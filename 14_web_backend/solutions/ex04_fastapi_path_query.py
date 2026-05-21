"""정답 04: FastAPI 경로/쿼리 파라미터 라우트 작성."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}


@app.get("/search")
def search(q: str = ""):
    return {"query": q}


if __name__ == "__main__":
    client = TestClient(app)

    r1 = client.get("/items/42")
    assert r1.status_code == 200
    assert r1.json()["id"] == 42

    r2 = client.get("/search", params={"q": "파이썬"})
    assert r2.status_code == 200
    assert r2.json()["query"] == "파이썬"

    r3 = client.get("/items/abc")
    assert r3.status_code == 422, f"422 이어야 합니다. 실제: {r3.status_code}"

    print("OK")
