"""정답 03: FastAPI 앱 생성 및 TestClient 검증."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello"}


if __name__ == "__main__":
    client = TestClient(app)
    r = client.get("/")

    assert r.status_code == 200, f"200 이어야 합니다. 실제: {r.status_code}"
    assert r.json() == {"message": "hello"}, f"응답이 올바르지 않습니다: {r.json()}"

    print("OK")
