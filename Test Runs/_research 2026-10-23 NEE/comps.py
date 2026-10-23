# Q2 comparator row: return on average book equity and on average tangible equity (equity less goodwill), 2021-2025.
# Inputs: XBRL companyfacts (filer-tagged 10-K data), transcription only; equity as tagged (may include preferred).
C = {
 "Duke Energy (DUK)":  dict(ni=[3802, 2444, 2735, 4402, 4912], eq=[47964, 49296, 49322, 49112, 50127, 51842], gw=[19303]*5 + [19010]),
 "Southern (SO)":      dict(ni=[2393, 3524, 3976, 4401, 4341], eq=[27972, 27874, 30408, 31444, 33208, 36016], gw=[5280, 5280, 5161, 5161, 5161, 5161]),
 "Dominion (D)":       dict(ni=[1973, 176, 2006, 1759, 2968], eq=[26117, 27308, 27659, 27567, 26863, 29083], gw=[7381, 4253, 4143, 4143, 4143, 4143]),
 "FPL (NEE segment)":  dict(ni=[3206, 3701, 4552, 4543, 5012], eq=[29228, 33594, 38920, 38835, 43076, 46986], gw=[0]*6),
 "NEE consolidated (attrib.)": dict(ni=[3573, 4147, 7310, 6946, 6835], eq=[36513, 37202, 39229, 47468, 50101, 54608], gw=[4254, 4844, 4854, 5091, 4866, 4849]),
 "NEE consolidated (before NCI allocation, on equity+NCI)": dict(ni=[2827, 3246, 6282, 5698, 5332], eq=[36513+8416, 37202+8222, 39229+9097, 47468+10300, 50101+10359, 54608+11871], gw=[4254, 4844, 4854, 5091, 4866, 4849]),
}
for k, d in C.items():
    ae = [(d["eq"][i] + d["eq"][i+1]) / 2 for i in range(5)]
    at = [((d["eq"][i]-d["gw"][i]) + (d["eq"][i+1]-d["gw"][i+1])) / 2 for i in range(5)]
    yr = [f"{n/e:.1%}" for n, e in zip(d["ni"], ae)]
    print(f"{k}: by year {yr}; five-year on book {sum(d['ni'])/sum(ae):.1%}; on tangible {sum(d['ni'])/sum(at):.1%}")
