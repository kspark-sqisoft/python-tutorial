"""
연습문제 01: requests mock 으로 GET 요청 검증.

TODO:
1. make_mock_response() 를 완성해 status_code 와 json_data 를 가진 MagicMock 을 반환하라.
2. fetch_data() 에서 patch 를 이용해 requests.get 을 모킹하고 결과를 반환하라.
3. main 블록에서 status_code == 200 이고 JSON 에 "title" 키가 있음을 assert 하라.
"""

import requests
from unittest.mock import patch, MagicMock


def make_mock_response(status_code: int, json_data: dict) -> MagicMock:
    """가짜 응답 객체를 반환한다."""
    # TODO: MagicMock 을 만들어 status_code 와 json() 반환값을 설정하고 반환하라.
    pass


def fetch_data(url: str) -> tuple[int, dict]:
    """url 에 GET 요청을 보내고 (status_code, json) 을 반환한다.
    실제 호출이 일어나지 않도록 호출하는 쪽에서 patch 를 적용한다."""
    response = requests.get(url)
    return response.status_code, response.json()


if __name__ == "__main__":
    fake_data = {"id": 1, "title": "첫 번째 포스트", "body": "내용입니다."}

    # TODO: patch("requests.get") 컨텍스트 매니저를 사용해 mock 을 주입하고
    #       fetch_data() 를 호출한 뒤 아래 assert 를 통과시켜라.
    status, data = None, {}  # 이 줄을 수정하라

    assert status == 200, f"status_code 가 200 이어야 합니다. 실제: {status}"
    assert "title" in data, f"JSON 에 'title' 키가 있어야 합니다. 실제: {data}"

    print("OK")
