"""
matplotlib 입문 (헤드리스 모드): line/bar/scatter 플롯 생성,
제목·레이블 설정, PNG 저장을 다룬다.
모든 그래프는 Agg 백엔드로 렌더링하고 tempfile 에만 저장한다.
"""

import matplotlib
matplotlib.use("Agg")  # 반드시 pyplot import 전에 설정 — 화면 표시 없음

import tempfile
import matplotlib.pyplot as plt
import numpy as np

# ──── 1. 선 그래프 (line plot) ────

def section_line(save_dir: str) -> None:
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, color="steelblue", linewidth=2, label="sin(x)")
    ax.set_title("사인 곡선")
    ax.set_xlabel("x (라디안)")
    ax.set_ylabel("sin(x)")
    ax.legend()

    path = f"{save_dir}/line.png"
    fig.savefig(path, dpi=100)
    plt.close(fig)
    print(f"선 그래프 저장: {path}")
    return path


# ──── 2. 막대 그래프 (bar chart) ────

def section_bar(save_dir: str) -> None:
    teams = ["Team A", "Team B", "Team C"]
    scores = [88.5, 76.2, 92.0]

    fig, ax = plt.subplots()
    ax.bar(teams, scores, color=["#4C72B0", "#DD8452", "#55A868"])
    ax.set_title("팀별 평균 점수")
    ax.set_xlabel("팀")
    ax.set_ylabel("점수")
    ax.set_ylim(0, 100)

    path = f"{save_dir}/bar.png"
    fig.savefig(path, dpi=100)
    plt.close(fig)
    print(f"막대 그래프 저장: {path}")
    return path


# ──── 3. 산점도 (scatter plot) ────

def section_scatter(save_dir: str) -> None:
    rng = np.random.default_rng(seed=0)
    x = rng.normal(0, 1, 50)
    y = x * 1.5 + rng.normal(0, 0.5, 50)  # y = 1.5x + 노이즈

    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.7, edgecolors="white", linewidths=0.5)
    ax.set_title("산점도 예시")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    path = f"{save_dir}/scatter.png"
    fig.savefig(path, dpi=100)
    plt.close(fig)
    print(f"산점도 저장: {path}")
    return path


if __name__ == "__main__":
    import os

    with tempfile.TemporaryDirectory() as tmpdir:
        print("=" * 45)
        print("1. 선 그래프")
        print("=" * 45)
        p1 = section_line(tmpdir)
        print(f"  파일 크기: {os.path.getsize(p1):,} bytes")

        print("\n" + "=" * 45)
        print("2. 막대 그래프")
        print("=" * 45)
        p2 = section_bar(tmpdir)
        print(f"  파일 크기: {os.path.getsize(p2):,} bytes")

        print("\n" + "=" * 45)
        print("3. 산점도")
        print("=" * 45)
        p3 = section_scatter(tmpdir)
        print(f"  파일 크기: {os.path.getsize(p3):,} bytes")

    print("\ntmpdir 정리 완료 — 저장소에 PNG 없음")
