"""
click 라이브러리로 데코레이터 기반 CLI를 만드는 방법을 학습한다.
argparse 보다 간결하고 테스트하기 쉬운 CliRunner 를 함께 다룬다.
명령 그룹(group)으로 서브커맨드를 구성하는 패턴도 소개한다.
"""

import click
from click.testing import CliRunner

# ──── 1. 기본 명령 정의 — 데코레이터 방식 ────

# @click.command() 한 줄로 함수를 CLI 명령으로 변환한다
@click.command()
@click.option("--name", default="World", help="인사할 대상 이름")
@click.option("--count", default=1, type=int, help="반복 횟수")
def hello(name: str, count: int) -> None:
    """인사를 출력하는 명령."""
    for i in range(count):
        click.echo(f"[{i+1}] 안녕하세요, {name}!")  # click.echo = print + 파일 출력 지원


# ──── 2. argparse 와 click 비교 (한 줄 요약) ────

# argparse : parser.add_argument("--name", ...) → args = parser.parse_args(...)
# click    : @click.option("--name", ...) → def hello(name): ...  ← 훨씬 간결

# ──── 3. CliRunner 로 테스트 — 실제 터미널 없이 호출 ────

runner = CliRunner()

# 정상 호출
result = runner.invoke(hello, ["--name", "Kee", "--count", "3"])

print("=== CliRunner 호출 결과 ===")
print(f"  exit_code : {result.exit_code}")   # 0 = 정상
print(f"  output    :\n{result.output}")

# ──── 4. 두 번째 명령 정의 ────

@click.command()
@click.option("--text", required=True, help="대문자로 변환할 문자열")
def shout(text: str) -> None:
    """입력 텍스트를 대문자로 출력하는 명령."""
    click.echo(text.upper())


result2 = runner.invoke(shout, ["--text", "hello python"])
print("=== shout 명령 결과 ===")
print(f"  output: {result2.output.strip()}")

# ──── 5. 명령 그룹 (서브커맨드 구조) — 한 줄 언급 ────

# click.group() 으로 그룹을 만들고 @cli.add_command(hello) 또는
# @cli.command() 데코레이터로 서브커맨드를 등록할 수 있다

@click.group()
def cli() -> None:
    """자동화 도구 모음."""
    pass

cli.add_command(hello, name="greet")
cli.add_command(shout, name="shout")

# 그룹 명령 테스트
result3 = runner.invoke(cli, ["greet", "--name", "그룹테스트"])
print("=== 그룹 서브커맨드 결과 ===")
print(f"  exit_code : {result3.exit_code}")
print(f"  output    : {result3.output.strip()}")


if __name__ == "__main__":
    # 직접 실행 시 hello 명령을 기본값으로 호출
    result_main = runner.invoke(hello, [])
    print("\n=== 기본값으로 호출 ===")
    print(result_main.output)
