# Q4 (recorded, not governing) look-through owner earnings for BN, built from each leg's own filed cash-flow statement.
# $M. Years FY2023, FY2024, FY2025. Sources in the run file. Arithmetic only; every judgment is in the run file.
Y = [2023, 2024, 2025]
legs = {
 # OCF as filed; D&A as filed; total capex line(s) as filed; common-group share of total equity YE2025 (YE2024); BN economic %
 "BIP":  dict(ocf=[4078, 4653, 5971], da=[2739, 3644, 4024], capex=[2487, 4975, 6024], cg=8432/35540, cg24=8074/29853, bn=0.27,
              note="Purchase of long lived assets"),
 "BEP":  dict(ocf=[1865, 1274, 1147], da=[1852, 2010, 2425], capex=[2809, 3733, 6587], cg=8876/34974, cg24=8380/36456, bn=0.47,
              note="Investment in property, plant and equipment"),
 "BBU":  dict(ocf=[2130, 3281, 3230], da=[3592, 3204, 3030], capex=[2288, 2520, 2060], cg=5451/15311, cg24=5117/17308, bn=0.68,
              note="Property, plant and equipment and intangible assets; filer maintenance capex 833/853/868", maint=[833, 853, 868]),
 "BPY":  dict(ocf=[-670, 1018, -595], da=[440, 418, 269], capex=[529, 403, 758], cg=23206/42574, cg24=21528/38249, bn=1.00,
              note="PP&E acquisitions only; investment-property spending sits inside 'Investment properties' acquisitions (4,807/9,053/4,078) and is not separable"),
}
def mean(xs): return sum(xs) / len(xs)
out = {}
for k, d in legs.items():
    row = {}
    for wname, idx in [("3yr FY2023-25", [0, 1, 2]), ("2yr FY2024-25", [1, 2])]:
        o = mean([d["ocf"][i] for i in idx]); da = mean([d["da"][i] for i in idx]); cx = mean([d["capex"][i] for i in idx])
        ends = {"(c)=D&A": o - da, "(c)=total capex": o - cx}
        if "maint" in d: ends["(c)=filer maintenance capex"] = o - mean([d["maint"][i] for i in idx])
        if k == "BPY": ends["(c)=0 (ceiling)"] = o
        share = d["cg"] * d["bn"]
        row[wname] = {e: (round(v), round(v * share)) for e, v in ends.items()}
        row[wname]["_ocf_mean"] = round(o); row[wname]["_share"] = round(share, 4)
    out[k] = row
    print(k, "| common-group share YE2025 %.1f%% (YE2024 %.1f%%) x BN %.0f%% = %.1f%%" % (100*d["cg"], 100*d["cg24"], 100*d["bn"], 100*d["cg"]*d["bn"]))
    for w, r in row.items():
        print("   ", w, "OCF mean", r["_ocf_mean"], {e: v for e, v in r.items() if not e.startswith("_")}, "  (100% basis, BN share)")
    print("    OCF < D&A in years:", [Y[i] for i in range(3) if d["ocf"][i] < d["da"][i]])

# BAM, from the committed BAM run (Q4), 100% of BAM common; BN holds 1,193.0M of 1,597.25M
bn_bam = 1193.0 / 1597.251633
bam = {"3yr FY2023-25": (1670, 1792), "2yr FY2024-25": (1862, 2024)}
print("\nBAM share %.2f%%" % (100 * bn_bam), {w: (round(a * bn_bam), round(b * bn_bam)) for w, (a, b) in bam.items()})
carry = [570, 403, 560]
print("Realized carried interest, net (BN):", carry, "3yr mean", round(mean(carry)), "2yr mean", round(mean(carry[1:])))
corp_cash = [131, 44, 155]; corp_int = [-596, -727, -742]; pref = [-176, -176, -177]; ebc = [-108, -109, -110]
corp = [corp_cash[i] + corp_int[i] + pref[i] + ebc[i] for i in range(3)]
print("Corporate (cash&other FFO + borrowings FFO + preferred + equity comp):", corp, "3yr", round(mean(corp)), "2yr", round(mean(corp[1:])))

print("\n== BN LOOK-THROUGH (excludes BWS and the direct fund stakes, valued as investments; see run file) ==")
res = {}
for w, idx in [("3yr FY2023-25", [0, 1, 2]), ("2yr FY2024-25", [1, 2])]:
    c = mean([corp[i] for i in idx]); ca = mean([carry[i] for i in idx])
    lo_b, hi_b = bam[w]
    L = lambda k, e: out[k][w][e][1]
    # conservative: BAM conservative, carry at the lowest year in the window, BIP/BEP at total capex, BBU at D&A, BPY at total capex
    cons = lo_b * bn_bam + min(carry[i] for i in idx) + c + L("BIP", "(c)=total capex") + L("BEP", "(c)=total capex") + L("BBU", "(c)=D&A") + L("BPY", "(c)=total capex")
    # judged top: BAM generous, carry window mean, BIP/BEP at total capex (their D&A end is INVALID, E5-20),
    # BBU at filer maintenance capex (management's figure, flagged), BPY at D&A (investment property is not depreciated, so this still flatters)
    top = hi_b * bn_bam + ca + c + L("BIP", "(c)=total capex") + L("BEP", "(c)=total capex") + L("BBU", "(c)=filer maintenance capex") + L("BPY", "(c)=D&A")
    # display ceiling only: BIP/BEP at D&A (INVALID), BPY at (c)=0 (impossible for real estate)
    disp = hi_b * bn_bam + ca + c + L("BIP", "(c)=D&A") + L("BEP", "(c)=D&A") + L("BBU", "(c)=filer maintenance capex") + L("BPY", "(c)=0 (ceiling)")
    res[w] = (cons, top, disp)
    print(w, "conservative %d | judged top %d | display ceiling (INVALID ends) %d" % (cons, top, disp))

print("\n== COMPUTATION - NOT A CLEARANCE ==")
shares = 2297.678581
bws_ex = 13139 - 65.0 * 47.26 - 53.6 * 26.41   # BWS book less BAM shares and BBUC units already inside the BAM and BBU lines, at 2026-09-11 quotes
direct = 10876
inv = bws_ex + direct
print("investments component: BWS ex double count %d + direct fund stakes %d = %d" % (bws_ex, direct, inv))
lo = min(v[0] for v in res.values()); hi = max(v[1] for v in res.values()); dc = max(v[2] for v in res.values())
print("OE range: conservative low %d, judged top %d, display ceiling %d" % (lo, hi, dc))
for r, lab in [(0.0535, "sovereign 5.35%"), (0.10, "floor 10%")]:
    print(lab, "value/share at zero growth: %.1f to %.1f (display ceiling %.1f)" % ((lo / r + inv) / shares, (hi / r + inv) / shares, (dc / r + inv) / shares))
cap = 38.22 * shares
print("cap %d" % cap)
for oe in (lo, hi, dc):
    y = oe / (cap - inv)
    print("OE %d: yield on whole cap %.2f%%; on cap less investments %.2f%%; perpetual growth needed at sovereign %.2f%%, at floor %.2f%%" % (oe, 100 * oe / cap, 100 * y, 100 * (0.0535 - y) / (1 + y), 100 * (0.10 - y) / (1 + y)))
marks = 1193.0 * 47.26 + 207.1 * 36.88 + 309.4 * 30.39 + 142.5 * 26.41 + bws_ex + 26706 + direct - 20172
print("cross-check, parts at their own marks: $%.1fbn = $%.1f/share" % (marks / 1000, marks / shares))
