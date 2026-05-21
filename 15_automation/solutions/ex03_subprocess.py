"""정답 03 — subprocess"""

import subprocess

result = subprocess.run(
    ["python", "-c", "print('hi')"],
    capture_output=True,
    text=True,
)

assert result.returncode == 0
assert result.stdout.strip() == "hi"
print("OK")
