"""정답 02 — click CLI + CliRunner"""

import click
from click.testing import CliRunner


@click.command()
@click.option("--msg", default="hello", help="출력할 메시지")
def echo_msg(msg: str) -> None:
    """메시지를 출력하는 명령."""
    click.echo(msg)


runner = CliRunner()
result = runner.invoke(echo_msg, ["--msg", "python"])

assert result.exit_code == 0
assert result.output.strip() == "python"
print("OK")
