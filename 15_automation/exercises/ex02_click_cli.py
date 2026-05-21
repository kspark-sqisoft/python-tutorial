"""
연습문제 02 — click CLI + CliRunner

TODO:
1. @click.command() 와 @click.option("--msg", default="hello") 로 echo_msg 함수를 정의하라.
   함수 본문: click.echo(msg)
2. CliRunner().invoke(echo_msg, ["--msg", "python"]) 로 호출하라.
3. result.exit_code == 0 임을 assert 로 검증하라.
4. result.output.strip() == "python" 임을 assert 로 검증하라.
"""

import click
from click.testing import CliRunner

# ── 여기에 코드를 작성하세요 ──


# 검증 (수정하지 마세요)
# assert result.exit_code == 0
# assert result.output.strip() == "python"
# print("OK")
