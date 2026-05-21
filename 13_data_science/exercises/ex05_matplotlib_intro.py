"""
연습문제 05: matplotlib 헤드리스
sin 곡선을 그려 tempfile PNG 로 저장하고
파일 크기가 0보다 큰지 확인하세요.
"""

import matplotlib
matplotlib.use("Agg")  # 화면 표시 없이 파일 저장만

import os
import tempfile
import matplotlib.pyplot as plt
import numpy as np

# ──── TODO ────
with tempfile.TemporaryDirectory() as tmpdir:
    png_path = f"{tmpdir}/plot.png"

    # 1. x = 0 ~ 2π 구간, 100개 점 생성 (np.linspace 사용)
    x = None  # TODO

    # 2. y = sin(x) 계산
    y = None  # TODO

    # 3. fig, ax = plt.subplots() 로 Figure 생성 후
    #    ax.plot(x, y) 로 선 그래프를 그리세요
    # TODO

    # 4. fig.savefig(png_path) 로 PNG 저장 후 plt.close(fig) 하세요
    # TODO

    file_size = os.path.getsize(png_path)

    # ──── 검증 (수정 금지) ────
    assert file_size > 0, f"PNG 파일이 비어 있습니다 (size={file_size})"
    print(f"OK (파일 크기: {file_size:,} bytes)")
