"""정답 01 — argparse CLI"""

import argparse

parser = argparse.ArgumentParser(description="이름과 나이를 받는 CLI")
parser.add_argument("--name", default="World", help="이름")
parser.add_argument("--age", type=int, default=0, help="나이")

args = parser.parse_args(["--name", "Kee", "--age", "30"])

assert args.name == "Kee"
assert args.age == 30
assert isinstance(args.age, int)
print("OK")
