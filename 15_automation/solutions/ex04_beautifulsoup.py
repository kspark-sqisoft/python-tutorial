"""정답 04 — BeautifulSoup"""

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

soup = BeautifulSoup(HTML, "html.parser")
hrefs = [a.attrs["href"] for a in soup.find_all("a")]

assert hrefs == expected
print("OK")
