# 14_web_backend — 웹 백엔드

## 사전 준비
```bash
uv pip install -e ".[web]"
```

## 배우는 것
- requests — mock 응답으로 HTTP 클라이언트 패턴 시연
- pydantic — 데이터 모델 검증·직렬화
- FastAPI — TestClient 로 실제 서버 없이 검증
- 경로 / 쿼리 / 바디 매개변수 (자동 캐스팅·유효성·OpenAPI)
- SQLAlchemy 2.x in-memory SQLite 맛보기

## 학습 순서
1. `01_requests_client.py`
2. `02_pydantic_models.py`
3. `03_fastapi_intro.py`
4. `04_fastapi_path_query_body.py`
5. `05_sqlalchemy_basics.py`

## 실행 방법
```bash
uv run python 14_web_backend/03_fastapi_intro.py
```

## 연습문제
- 모든 검증은 TestClient / in-memory DB / mock 으로 — 외부 네트워크 X.
- `exercises/` 의 TODO 를 채우고, `solutions/` 와 비교한다.
