"""
requests 라이브러리를 이용한 HTTP 클라이언트 패턴 학습.
실제 네트워크 호출 없이 unittest.mock.patch 로 응답을 모킹하여
GET / POST 요청 패턴을 안전하게 시연한다.
"""

import requests
from unittest.mock import patch, MagicMock

# ──── 1. 가짜 GET 응답 만들기 ────

def fetch_user(user_id: int) -> dict:
    """사용자 정보를 GET 으로 가져온다."""
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)          # 실제 호출 — mock 으로 대체됨
    response.raise_for_status()           # 4xx/5xx → HTTPError 발생
    return response.json()


# ──── 2. 가짜 POST 응답 만들기 ────

def create_user(name: str, age: int) -> dict:
    """새 사용자를 POST 로 생성한다."""
    url = "https://api.example.com/users"
    payload = {"name": name, "age": age}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


# ──── 3. mock 헬퍼 ────

def make_mock_response(status_code: int, json_data: dict) -> MagicMock:
    """재사용 가능한 가짜 응답 객체를 반환한다."""
    mock_response = MagicMock()
    mock_response.status_code = status_code
    mock_response.json.return_value = json_data
    # raise_for_status() 는 2xx 일 때 아무 일도 하지 않아야 함
    mock_response.raise_for_status.return_value = None
    return mock_response


# ──── 4. 에러 응답 처리 ────

def safe_fetch(url: str) -> dict | None:
    """요청 실패 시 None 을 반환하는 안전한 래퍼."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"  HTTP 에러: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"  네트워크 에러: {e}")
        return None


if __name__ == "__main__":
    print("=== 01_requests_client.py 데모 ===\n")

    # 데모 1: GET 모킹
    print("1) GET 요청 모킹")
    mock_get_data = {"id": 1, "name": "홍길동", "email": "hong@example.com"}
    with patch("requests.get") as mock_get:
        mock_get.return_value = make_mock_response(200, mock_get_data)
        result = fetch_user(1)
        print(f"   status_code : {mock_get.return_value.status_code}")
        print(f"   응답 JSON   : {result}")

    # 데모 2: POST 모킹
    print("\n2) POST 요청 모킹")
    mock_post_data = {"id": 42, "name": "이순신", "age": 35, "created": True}
    with patch("requests.post") as mock_post:
        mock_post.return_value = make_mock_response(201, mock_post_data)
        result = create_user("이순신", 35)
        print(f"   status_code : {mock_post.return_value.status_code}")
        print(f"   응답 JSON   : {result}")

    # 데모 3: 에러 처리
    print("\n3) 4xx 에러 처리")
    with patch("requests.get") as mock_get:
        err_mock = MagicMock()
        err_mock.status_code = 404
        err_mock.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = err_mock
        data = safe_fetch("https://api.example.com/users/999")
        print(f"   반환값: {data}")

    print("\n완료!")
