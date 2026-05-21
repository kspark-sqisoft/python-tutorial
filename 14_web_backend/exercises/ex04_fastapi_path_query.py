"""
연습문제 04: FastAPI 경로/쿼리 파라미터 라우트 작성.

TODO:
1. GET /items/{item_id} — item_id(int) 를 받아 {"id": item_id} 를 반환한다.
2. GET /search?q=... — q(str, 기본값 "") 를 받아 {"query": q} 를 반환한다.
3. TestClient 로 두 라우트를 호출해 assert 를 통과시켜라.
4. GET /items/abc (잘못된 타입) 가 422 를 반환하는지 확인하라.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient


# TODO: 앱과 라우트를 정의하라.
# app = FastAPI()


if __name__ == "__main__":
    # TODO: 아래 assert 를 모두 통과하도록 위 코드를 완성하라.
    client = None  # TestClient(app) 으로 교체하라

    # 경로 파라미터
    r1 = None  # client.get("/items/42") 으로 교체하라
    assert r1 is not None, "GET /items/42 를 호출하라"
    assert r1.status_code == 200
    assert r1.json()["id"] == 42

    # 쿼리 파라미터
    r2 = None  # client.get("/search", params={"q": "파이썬"}) 으로 교체하라
    assert r2 is not None, "GET /search?q=파이썬 를 호출하라"
    assert r2.status_code == 200
    assert r2.json()["query"] == "파이썬"

    # 타입 오류 → 422
    r3 = None  # client.get("/items/abc") 으로 교체하라
    assert r3 is not None, "GET /items/abc 를 호출하라"
    assert r3.status_code == 422, f"422 이어야 합니다. 실제: {r3.status_code}"

    print("OK")
