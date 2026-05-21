"""Book API 통합 테스트 (TestClient)."""

from fastapi.testclient import TestClient


def test_post_creates_book(client: TestClient) -> None:
    """POST /books 가 책을 생성하고 id 를 반환해야 한다."""
    resp = client.post("/books", json={"title": "파이썬", "pages": 300})
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert "id" in data
    assert data["title"] == "파이썬"
    assert data["pages"] == 300


def test_get_lists_books(client: TestClient) -> None:
    """2건 생성 후 GET /books 가 길이 2인 목록을 반환해야 한다."""
    client.post("/books", json={"title": "책A", "pages": 100})
    client.post("/books", json={"title": "책B", "pages": 200})
    resp = client.get("/books")
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_get_single(client: TestClient) -> None:
    """GET /books/{id} 가 동일한 데이터를 반환해야 한다."""
    created = client.post("/books", json={"title": "단일책", "pages": 50}).json()
    book_id = created["id"]
    resp = client.get(f"/books/{book_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == book_id
    assert data["title"] == "단일책"
    assert data["pages"] == 50


def test_delete_then_404(client: TestClient) -> None:
    """DELETE 후 동일 id 로 GET 하면 404 를 반환해야 한다."""
    book_id = client.post("/books", json={"title": "삭제될책", "pages": 10}).json()["id"]
    del_resp = client.delete(f"/books/{book_id}")
    assert del_resp.status_code == 204
    get_resp = client.get(f"/books/{book_id}")
    assert get_resp.status_code == 404


def test_invalid_pages_422(client: TestClient) -> None:
    """pages=0 이면 422 Unprocessable Entity 를 반환해야 한다."""
    resp = client.post("/books", json={"title": "x", "pages": 0})
    assert resp.status_code == 422
