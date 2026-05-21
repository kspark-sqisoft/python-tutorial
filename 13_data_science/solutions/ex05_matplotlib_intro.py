"""
정답 05: matplotlib 헤드리스
"""

import matplotlib
matplotlib.use("Agg")

import os
import tempfile
import matplotlib.pyplot as plt
import numpy as np

with tempfile.TemporaryDirectory() as tmpdir:
    png_path = f"{tmpdir}/plot.png"

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    fig.savefig(png_path)
    plt.close(fig)

    file_size = os.path.getsize(png_path)
    assert file_size > 0, f"PNG 파일이 비어 있습니다 (size={file_size})"
    print(f"OK (파일 크기: {file_size:,} bytes)")
