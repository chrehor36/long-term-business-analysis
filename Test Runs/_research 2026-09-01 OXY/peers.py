import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = print

# All figures from each filer's OWN FY2025 Form 10-K supplemental oil and gas disclosures.
# prod / ext(+improved recovery) / revisions, MMBoe;  expl+dev, $M;  PD and total proved, MMBoe.
D = {
    "OXY": dict(  # accn 0001628280-26-009059
        prod=[446.3, 486.2, 523.2], ext=[175.5, 372.8, 399.8], rev=[406.2, 169.5, 161.3],
        ed=[5393, 5808, 6134], pd=3294, tot=4603, dda=7115),
    "FANG": dict(  # Diamondback, FY2025 10-K
        prod=[163.4, 219.0, 336.2], ext=[355.9, 278.8, 578.9], rev=[-54.5, -129.1, -304.1],
        ed=[2730, 3186, 3825], pd=2521, tot=3618, dda=4943),
    "DVN": dict(  # Devon, FY2025 10-K
        prod=[240.0, 270.0, 307.0], ext=[322.0, 340.0, 443.0], rev=[-79.0, 21.0, 134.0],
        ed=[3694, 3546, 3638], pd=1844, tot=2428, dda=None),
    "EOG": dict(  # EOG, FY2025 10-K
        prod=[361.0, 391.0, 452.0], ext=[607.0, 580.0, 336.0], rev=[29.0, 69.0, 133.0],
        ed=[5795, 5371, 6024], pd=3346, tot=5514, dda=None),
    "COP": dict(  # ConocoPhillips, FY2025 10-K, CONSOLIDATED operations only
        prod=[596.0, 649.0, 796.0], ext=[381.0, 96.0, 189.0], rev=[276.0, 590.0, 613.0],
        ed=[10489, 11530, 12102], pd=4239, tot=6506, dda=None),
}

P("{:<6} {:>9} {:>9} {:>10} {:>10} {:>10} {:>10} {:>8} {:>8}".format(
    "", "prod25", "org25%", "org3y%", "allsrc25%", "allsrc3y%", "F&D-bit3y", "F&D-all3y", "PDlife"))
for k, d in D.items():
    p3 = sum(d["prod"]); e3 = sum(d["ext"]); r3 = sum(d["rev"]); c3 = sum(d["ed"])
    org25 = d["ext"][2] / d["prod"][2]
    org3 = e3 / p3
    all25 = (d["ext"][2] + d["rev"][2]) / d["prod"][2]
    all3 = (e3 + r3) / p3
    fdbit = c3 / e3
    fdall = c3 / (e3 + r3)
    P("{:<6} {:>9.1f} {:>9.1%} {:>10.1%} {:>10.1%} {:>10.1%} {:>10.2f} {:>8.2f} {:>8.2f}".format(
        k, d["prod"][2], org25, org3, all25, all3, fdbit, fdall, d["pd"] / d["prod"][2]))

P("\nDD&A per Boe, FY2025, where the filer discloses oil-and-gas-activity DD&A separately:")
for k, d in D.items():
    if d["dda"]:
        P("  {:<6} ${:.2f}/Boe   ({:,}M / {:.1f} MMBoe)".format(k, d["dda"] / d["prod"][2], d["dda"], d["prod"][2]))

P("\nTotal proved reserve life, YE2025 (years):")
for k, d in D.items():
    P("  {:<6} {:.2f}".format(k, d["tot"] / d["prod"][2]))

P("\nOXY: DD&A/Boe $13.60 vs its own 3-yr F&D range ${:.2f} (all-sources) to ${:.2f} (drill-bit only)".format(
    sum(D["OXY"]["ed"]) / (sum(D["OXY"]["ext"]) + sum(D["OXY"]["rev"])),
    sum(D["OXY"]["ed"]) / sum(D["OXY"]["ext"])))
mid = (sum(D["OXY"]["ed"]) / (sum(D["OXY"]["ext"]) + sum(D["OXY"]["rev"])) + sum(D["OXY"]["ed"]) / sum(D["OXY"]["ext"])) / 2
P("  midpoint of the two constructions = ${:.2f}/Boe; x 523.2 MMBoe = ${:,.0f}M/yr to replace one year of production".format(mid, mid * 523.2))
P("  FY2025 capex as spent 6,427 / consolidated D&A 7,533 = {:.2f}x   (the screen said 0.77x)".format(6427 / 7533))
P("  FY2025 capex as spent 6,427 / oil-and-gas segment DD&A 7,115 = {:.2f}x".format(6427 / 7115))
