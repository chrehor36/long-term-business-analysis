"""Measure waterfall bar extents in pixels (no labels in FY2022-24 chart images). Scale from the two
filed endpoint values. OUTPUT IS AN ESTIMATE FROM A PICTURE, not a filed figure."""
from PIL import Image
import sys
known = {"NA_2022v2021PF": (11342, 13987), "NA_2023v2022": (13987, 13298), "NA_2024v2023": (13298, 2660),
         "NA_2025v2024": (2660, -1892), "EE_2022v2021PF": (5324, 6218), "EE_2023v2022": (6218, 6519),
         "EE_2024v2023": (6519, 2419), "EE_2025v2024": (2419, -651), "MEA_2024v2023": (2503, 1901),
         "MEA_2025v2024": (1901, 1429), "SA_2024v2023": (2369, 2272), "SA_2025v2024": (2272, 1963)}
for name, (a, b) in known.items():
    im = Image.open(name + ".gif").convert("RGBA")
    W, H = im.size
    px = im.load()
    # find axis line: gray row; bar columns at 8 evenly spaced centers
    centers = [int(W * (0.076 + i * 0.1215)) for i in range(8)]
    bars = []
    for cx in centers:
        ys = [y for y in range(H) if px[cx, y][3] > 0 and not (abs(px[cx, y][0] - px[cx, y][1]) < 20 and abs(px[cx, y][1] - px[cx, y][2]) < 20)]
        if not ys:
            bars.append(None); continue
        col = px[cx, ys[len(ys) // 2]]
        kind = "blue" if col[2] > 150 and col[0] < 100 else ("red" if col[0] > 180 and col[1] < 120 else ("green" if col[1] > 150 and col[0] < 180 else str(col[:3])))
        bars.append((min(ys), max(ys), kind))
    s, e = bars[0], bars[-1]
    # start bar spans value a; assume zero line = bottom of start bar if a>0
    scale = abs(a) / (s[1] - s[0] + 1)
    out = []
    for bb in bars[1:-1]:
        if bb is None:
            out.append("n/a"); continue
        v = (bb[1] - bb[0] + 1) * scale * (1 if bb[2] == "green" else -1)
        out.append(f"{bb[2]}:{v:,.0f}")
    endv = (e[1] - e[0] + 1) * scale
    print(name, "scale %.1f/px" % scale, out, "end bar est %s vs filed %s" % (f"{endv:,.0f}", b))
