"""
연습문제 04 — BeautifulSoup

아래 HTML 에서 모든 <a> 태그의 href 값을 리스트로 추출하라.

TODO:
1. BeautifulSoup(HTML, "html.parser") 로 파싱하라.
2. find_all("a") 로 모든 앵커 태그를 찾아라.
3. 각 태그의 href 속성 값을 리스트로 수집하라.
4. hrefs 가 아래 expected 와 같은지 assert 로 검증하라.
"""

from bs4 import BeautifulSoup

HTML = """
<html>
  <body>
    <a href="https://first.example">첫 번째</a>
    <a href="https://second.example">두 번째</a>
    <a href="https://third.example">세 번째</a>
  </body>
</html>
"""

expected = [
    "https://first.example",
    "https://second.example",
    "https://third.example",
]

# ── 여기에 코드를 작성하세요 ──


# 검증 (수정하지 마세요)
# assert hrefs == expected
# print("OK")
