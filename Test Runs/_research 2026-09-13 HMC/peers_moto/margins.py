# Arithmetic only: margin = operating profit / revenue; return on segment assets = op profit / assets (year-end, and avg where 2 ends).
import sys
DATA = {}
# Harley-Davidson HDMC segment, USD thousands, FY Dec. Revenue & operating income from segment note (FY2023 10-K for 2021-2023; FY2025 10-K for 2024-2025).
DATA["HOG HDMC"] = dict(unit="USD k",
    years=[2021, 2022, 2023, 2024, 2025],
    rev=[4504434, 4887672, 4844594, 4121906, 3578308],
    op=[476807, 677087, 661151, 277844, -28731],
    assets=[3246340, 3254309, 3644016, 3630710, 3866701],
    assets_prior=2440775)  # HDMC assets 2020 (FY2022 10-K)
DATA["HOG LiveWire"] = dict(unit="USD k", years=[2021, 2022, 2023, 2024, 2025],
    rev=[35806, 46833, 38298, 26358, 25671], op=[-68182, -85315, -116809, -109639, -75016])

# Yamaha Motor Land mobility segment, JPY millions, FY Dec. Basis changes: 2021-2023 J-GAAP (incl RV); 2023-2024 IFRS old basis (incl RV); 2024-2025 IFRS new basis (excl RV).
DATA["YAM LandMob JGAAP (incl RV)"] = dict(unit="JPY m", years=[2021, 2022, 2023],
    rev=[1179736, 1468244, 1581848], op=[68727, 87409, 124347], assets=[899465, 1029737, 1190336])
DATA["YAM LandMob IFRS old (incl RV)"] = dict(unit="JPY m", years=[2023, 2024],
    rev=[1585304, 1715384], op=[127519, 85476], assets=[1210775, 1202951])
DATA["YAM LandMob IFRS new (excl RV)"] = dict(unit="JPY m", years=[2024, 2025],
    rev=[1609568, 1615138], op=[103811, 108693], assets=[1099843, 1271415])
# Yamaha Motorcycle BUSINESS (sub-segment, earnings presentations), JPY 100m (bil. to 1 dp x10)
DATA["YAM MC business JGAAP"] = dict(unit="JPY 0.1bn", years=[2022, 2023], rev=[12917, 14081], op=[847, 1222])
DATA["YAM MC business IFRS"] = dict(unit="JPY 0.1bn", years=[2023, 2024, 2025], rev=[14133, 15711, 15781], op=[1255, 1265, 1235])

def show(name, d):
    print("==", name, d["unit"])
    for i, y in enumerate(d["years"]):
        r, o = d["rev"][i], d["op"][i]
        s = "%s: %s / %s = %.1f%%" % (y, f"{o:,}", f"{r:,}", 100.0 * o / r)
        if "assets" in d and d["assets"][i]:
            a = d["assets"][i]
            s += " | op/YE assets %s / %s = %.1f%%" % (f"{o:,}", f"{a:,}", 100.0 * o / a)
            prev = d["assets"][i-1] if i > 0 else d.get("assets_prior")
            if prev:
                s += " | op/avg assets = %.1f%%" % (100.0 * o / ((a + prev) / 2))
        print(s)

if __name__ == "__main__":
    for k in DATA:
        if len(sys.argv) == 1 or any(a in k for a in sys.argv[1:]):
            show(k, DATA[k])
