"""合并 Elysiasd + yujiezhang-ops 两个账号的贡献日历，生成自托管 SVG。

输出：
  contrib-light.svg / contrib-dark.svg   近一年贡献热力图
用于 GitHub Profile README，配合 .github/workflows/profile.yml 每日重建。
"""

import datetime as dt
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"

CELL, GAP = 11, 3
LEFT, TOP = 46, 44
MONTH_LABELS = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
WEEKDAYS = ["一", "", "三", "", "五", "", "日"]


def load() -> dict[str, int]:
    merged: dict[str, int] = {}
    for name in ("ely.json", "ops.json"):
        path = DATA / name
        if not path.exists():
            continue
        for day in json.loads(path.read_text()):
            d = day["date"]
            merged[d] = merged.get(d, 0) + day["contributionCount"]
    return merged


def level(count: int, buckets: list[int]) -> int:
    if count == 0:
        return 0
    for i, edge in enumerate(buckets, start=1):
        if count <= edge:
            return i
    return len(buckets)


def buckets_for(values: list[int]) -> list[int]:
    """按分位数定档，避免个别爆量日把其他天压成全空。"""
    nz = sorted(v for v in values if v > 0)
    if not nz:
        return [1, 2, 3, 4]
    q = lambda p: nz[min(len(nz) - 1, int(len(nz) * p))]
    return [max(1, q(0.25)), max(2, q(0.5)), max(3, q(0.75)), nz[-1]]


def svg(merged: dict[str, int], dark: bool) -> str:
    days = sorted(merged)
    first = dt.date.fromisoformat(days[0])
    last = dt.date.fromisoformat(days[-1])
    # 对齐到周一
    start = first - dt.timedelta(days=first.weekday())
    weeks = ((last - start).days // 7) + 1

    bg = "#0B0B0D" if dark else "#FBFAF7"
    ink = "#F7F4EE" if dark else "#141414"
    dim = "#918B82" if dark else "#6A655E"
    empty = "#1A1A20" if dark else "#EDE9E1"
    ramp = ["#5A2A16", "#8E3B1D", "#C9501C", "#FF7A45"] if dark else ["#F3D9C9", "#EBAE8C", "#DE7A4B", "#C9501C"]
    accent = "#FF7A45" if dark else "#C9501C"

    b = buckets_for(list(merged.values()))
    width = LEFT + weeks * (CELL + GAP) + 24
    height = TOP + 7 * (CELL + GAP) + 54

    cells = []
    month_marks = []
    seen_month = set()

    for i, day_s in enumerate(days):
        d = dt.date.fromisoformat(day_s)
        offset = (d - start).days
        col, row = offset // 7, offset % 7
        x = LEFT + col * (CELL + GAP)
        y = TOP + row * (CELL + GAP)
        lv = level(merged[day_s], b)
        fill = empty if lv == 0 else ramp[lv - 1]
        cells.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" fill="{fill}">'
            f"<title>{day_s} · {merged[day_s]} 次</title></rect>"
        )
        if d.month not in seen_month and d.day <= 7:
            seen_month.add(d.month)
            month_marks.append(
                f'<text x="{x}" y="{TOP - 12}" font-size="11" fill="{dim}">{MONTH_LABELS[d.month - 1]}</text>'
            )

    weekday_marks = [
        f'<text x="{LEFT - 12}" y="{TOP + r * (CELL + GAP) + CELL - 2}" font-size="10" '
        f'fill="{dim}" text-anchor="end">{WEEKDAYS[r]}</text>'
        for r in range(7)
        if WEEKDAYS[r]
    ]

    total = sum(merged.values())
    active = sum(1 for v in merged.values() if v)

    legend_x = width - 24 - 5 * (CELL + GAP)
    legend = [
        f'<text x="{legend_x - 8}" y="{height - 22}" font-size="11" fill="{dim}" text-anchor="end">少</text>'
    ]
    legend.append(
        f'<rect x="{legend_x}" y="{height - 30}" width="{CELL}" height="{CELL}" rx="2.5" fill="{empty}"/>'
    )
    for i, c in enumerate(ramp, start=1):
        legend.append(
            f'<rect x="{legend_x + i * (CELL + GAP)}" y="{height - 30}" width="{CELL}" height="{CELL}" '
            f'rx="2.5" fill="{c}"/>'
        )
    legend.append(
        f'<text x="{legend_x + 5 * (CELL + GAP) + 6}" y="{height - 22}" font-size="11" fill="{dim}">多</text>'
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="合并贡献图：近一年 {total} 次贡献，{active} 天有提交">
  <title>近一年 {total} 次贡献 · {active} 天活跃</title>
  <rect width="{width}" height="{height}" fill="{bg}"/>

  <g font-family="'PingFang SC','Hiragino Sans GB','Noto Sans SC','Microsoft YaHei',sans-serif">
{chr(10).join("    " + m for m in month_marks)}
{chr(10).join("    " + m for m in weekday_marks)}
  </g>

  <g>
{chr(10).join("    " + c for c in cells)}
  </g>

  <text x="{LEFT}" y="{height - 22}" font-size="12.5" fill="{ink}">
    <tspan font-weight="700">{total}</tspan><tspan fill="{dim}"> 次贡献 · </tspan><tspan font-weight="700">{active}</tspan><tspan fill="{dim}"> 天活跃 · 两个账号合并</tspan>
  </text>
  <g font-family="'PingFang SC',sans-serif">
{chr(10).join("    " + l for l in legend)}
  </g>
  <circle cx="{width - 20}" cy="{height - 40}" r="0" fill="{accent}"/>
</svg>
'''


def main() -> int:
    merged = load()
    if not merged:
        print("没有贡献数据，先运行 fetch.sh", file=sys.stderr)
        return 1
    (HERE / "contrib-light.svg").write_text(svg(merged, False))
    (HERE / "contrib-dark.svg").write_text(svg(merged, True))
    total = sum(merged.values())
    active = sum(1 for v in merged.values() if v)
    print(f"ok: {total} 次贡献 / {active} 天活跃 / {len(merged)} 天")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
