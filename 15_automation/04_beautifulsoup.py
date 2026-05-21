"""
BeautifulSoup 으로 HTML 을 파싱하고 원하는 요소를 추출하는 방법을 학습한다.
네트워크 요청 없이 코드 내 HTML 문자열을 파싱 대상으로 사용한다.
find/find_all, CSS 선택자(select), 텍스트·속성 추출을 다룬다.
"""

from bs4 import BeautifulSoup

# ──── 1. 파싱할 HTML 문자열 (네트워크 X — 로컬 내장) ────

HTML = """
<html>
  <head><title>학습용 페이지</title></head>
  <body>
    <h1 id="main-title">파이썬 자동화</h1>
    <p class="intro">BeautifulSoup 으로 HTML 을 파싱합니다.</p>

    <ul id="link-list">
      <li><a href="https://a.example">사이트 A</a></li>
      <li><a href="https://b.example">사이트 B</a></li>
      <li><a href="https://c.example" class="external">사이트 C (외부)</a></li>
    </ul>

    <ul id="item-list">
      <li>항목 x</li>
      <li>항목 y</li>
      <li>항목 z</li>
    </ul>

    <table>
      <tr><th>이름</th><th>점수</th></tr>
      <tr><td>Alice</td><td>95</td></tr>
      <tr><td>Bob</td><td>87</td></tr>
    </table>
  </body>
</html>
"""

# ──── 2. BeautifulSoup 객체 생성 ────

# "html.parser" : 표준 라이브러리 내장 파서 (lxml 없이 사용 가능)
soup = BeautifulSoup(HTML, "html.parser")

# ──── 3. find — 첫 번째 일치 요소 반환 ────

first_a = soup.find("a")   # 문서에서 첫 번째 <a> 태그
print("=== find('a') ===")
print(f"  태그     : {first_a}")
print(f"  텍스트   : {first_a.get_text()}")          # 태그 내 텍스트
print(f"  href     : {first_a.attrs['href']}")        # 속성 접근

# ──── 4. find_all — 모든 일치 요소 리스트 반환 ────

all_links = soup.find_all("a")
print("\n=== find_all('a') — 모든 링크 ===")
for link in all_links:
    print(f"  href={link.attrs['href']!r:30s}  텍스트={link.get_text()}")

# ──── 5. CSS 선택자 — select ────

# "#link-list li a" : id=link-list 하위 li 안의 a 태그
items = soup.select("#link-list li a")
print("\n=== select('#link-list li a') ===")
for item in items:
    print(f"  {item.get_text()}")

# "ul li" : 모든 ul 의 li 항목
all_li = soup.select("ul li")
print(f"\n  ul li 총 개수: {len(all_li)}")

# ──── 6. 속성으로 필터링 ────

external = soup.find("a", class_="external")   # class 속성으로 검색
print("\n=== class='external' 링크 ===")
print(f"  {external.get_text()} — {external['href']}")

# ──── 7. 테이블 데이터 추출 ────

rows = soup.select("table tr")
print("\n=== 테이블 행 파싱 ===")
for row in rows:
    cells = [cell.get_text() for cell in row.find_all(["th", "td"])]
    print(f"  {cells}")

# ──── 8. .get_text() 와 .attrs 요약 ────

h1 = soup.find("h1")
print("\n=== h1 요소 ===")
print(f"  get_text() : {h1.get_text()}")
print(f"  attrs      : {h1.attrs}")   # {'id': 'main-title'}


if __name__ == "__main__":
    # 모든 <a> href 와 텍스트를 한눈에 출력
    print("\n=== 전체 링크 요약 ===")
    for a in soup.find_all("a"):
        print(f"  [{a.get_text()}] → {a.get('href', '없음')}")
