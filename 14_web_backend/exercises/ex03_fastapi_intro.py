"""
연습문제 03: FastAPI 앱 생성 및 TestClient 검증.

TODO:
1. FastAPI 앱을 생성하라.
2. GET "/" 라우트를 추가하고 {"message": "hello"} 를 반환하라.
3. TestClient 로 호출해 status_code == 200 이고 JSON 이 올바른지 assert 하라.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient


# TODO: FastAPI 앱을 생성하라.
# app = FastAPI()


# TODO: GET "/" 라우트를 정의하라.
# @app.get("/")
# def root():
#     ...


if __name__ == "__main__":
    # TODO: TestClient 를 생성하고 GET "/" 를 호출하라.
    client = None  # 이 줄을 수정하라
    r = None       # client.get("/") 으로 교체하라

    assert r is not None, "TestClient 로 요청을 보내라"
    assert r.status_code == 200, f"200 이어야 합니다. 실제: {r.status_code}"
    assert r.json() == {"message": "hello"}, f"응답이 올바르지 않습니다: {r.json()}"

    print("OK")
