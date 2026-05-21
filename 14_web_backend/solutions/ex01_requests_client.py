"""정답 01: requests mock 으로 GET 요청 검증."""

import requests
from unittest.mock import patch, MagicMock


def make_mock_response(status_code: int, json_data: dict) -> MagicMock:
    mock_response = MagicMock()
    mock_response.status_code = status_code
    mock_response.json.return_value = json_data
    mock_response.raise_for_status.return_value = None
    return mock_response


def fetch_data(url: str) -> tuple[int, dict]:
    response = requests.get(url)
    return response.status_code, response.json()


if __name__ == "__main__":
    fake_data = {"id": 1, "title": "첫 번째 포스트", "body": "내용입니다."}

    with patch("requests.get") as mock_get:
        mock_get.return_value = make_mock_response(200, fake_data)
        status, data = fetch_data("https://api.example.com/posts/1")

    assert status == 200, f"status_code 가 200 이어야 합니다. 실제: {status}"
    assert "title" in data, f"JSON 에 'title' 키가 있어야 합니다. 실제: {data}"

    print("OK")
