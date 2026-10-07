# CB Chubb Limited - all arithmetic for the run of 2026-09-19.
# Every input is hand-read from a filed statement; the source is in the comment.
# Filings: FY2025 10-K acc 0000896159-26-000005 (cb-20251231.htm)
#          FY2023 10-K acc 0000896159-24-000003 (cb-20231231.htm)
#          FY2021 10-K acc 0000896159-22-000005 (cb-20211231.htm)
#          FY2018 10-K acc 0000896159-19-000005 (cb-12312018x10k.htm)
#          Q2 2026 10-Q acc 0000896159-26-000017 (cb-20260630.htm)
P = print
# ---------- price / cap ----------
PRICE = 340.64; PDATE = "2026-09-18"     # aggregator via tools/sources.py, FLAGGED
SH = 385799859                           # 10-Q cover 2026-07-20, OUTSTANDING (net of treasury)
CAP = PRICE * SH / 1e6
P("cap $%.0fM at $%.2f on %s on %d shares" % (CAP, PRICE, PDATE, SH))
SOV = 5.34                               # US Treasury daily par yield curve 30Y, 2026-09-18

# ---------- Total P&C reconciliation table, 2019-2025 ($M) ----------
# A=losses&LAE  CATg=cat losses gross of related adj  PPDg=PPD gross, favourable
# B=CAY loss ex CAT  C=acq+admin  D=acq+admin adjusted  E=NPE  F=NPE ex adjustments
# RPden = reinstatement premiums on cats added in the denominator
R = {
 2019: dict(A=17981, CATg=1175, PPDg=845,  B=17651, C=8240,  D=8257,  E=28947, F=29029, RPden=12),
 2020: dict(A=20985, CATg=3249, PPDg=414,  B=18150, C=8440,  D=8437,  E=30635, F=30661, RPden=10),
 2021: dict(A=21248, CATg=2411, PPDg=986,  B=19823, C=9009,  D=9006,  E=33953, F=34000, RPden=-10),
 2022: dict(A=22856, CATg=2231, PPDg=1153, B=21778, C=9439,  D=9416,  E=36850, F=37055, RPden=-49),
 2023: dict(A=24448, CATg=1828, PPDg=882,  B=23502, C=10406, D=10387, E=40314, F=40404, RPden=0),
 2024: dict(A=26323, CATg=2401, PPDg=991,  B=24913, C=11400, D=11400, E=43573, F=43694, RPden=-14),
 2025: dict(A=27077, CATg=2863, PPDg=1132, B=25346, C=12185, D=12201, E=45790, F=45863, RPden=58),
}
P("\n== CHECK B = A - CATgross + PPDgross, and the independently built series ==")
P("year | reported CR | CAY incl CAT (built) | PPD pts (built) | UW income $M | expense ratio")
for y in sorted(R):
    d = R[y]
    assert d["B"] == d["A"] - d["CATg"] + d["PPDg"], y
    G = d["F"] - d["RPden"]
    cay = (d["B"] + d["CATg"] + d["D"]) / G * 100
    rep = (d["A"] + d["C"]) / d["E"] * 100
    uw = d["E"] - d["A"] - d["C"]
    exp = d["C"] / d["E"] * 100
    P(" %d | %.1f | %.2f | %.2f | %d | %.1f" % (y, rep, cay, cay - rep, uw, exp))

# ---------- the FILER own published points (the primary series) ----------
FILER = {  # year: (CAY loss ex CAT, cat pts, favourable PPD pts, acq pts, admin pts, reported P&C CR)
 2016: (58.0,  4.0, 4.3, 20.2, 10.4, 88.3),
 2017: (58.8, 10.2, 3.2, 19.5,  9.4, 94.7),
 2018: (59.6,  5.8, 3.3, 19.2,  9.3, 90.6),
 2019: (60.8,  4.1, 2.8, 19.1,  9.4, 90.6),
 2020: (59.2, 10.6, 1.3, 18.9,  8.7, 96.1),
 2021: (58.3,  7.1, 2.8, 18.3,  8.2, 89.1),
 2022: (58.8,  6.0, 2.8, 17.8,  7.8, 87.6),
 2023: (58.2,  4.5, 1.9, 17.8,  8.1, 86.5),  # PPD 2.1 in FY2023 10-K, restated to 1.9 in FY2025 10-K
 2024: (57.0,  5.5, 2.0, 18.1,  8.1, 86.6),
 2025: (55.3,  6.3, 2.5, 18.6,  8.0, 85.7),
}
P("\n== THE DECISIVE SERIES, from the filer own published points ==")
P("year | CAY ex CAT CR | cats | CAY INCL CAT CR | fav PPD | reported CR | expense ratio")
cay_s = []; rep_s = []; ppd_s = []; exp_s = []
for y in sorted(FILER):
    l, c, p, a, ad, rep = FILER[y]
    cayx = l + a + ad; cay = cayx + c
    P(" %d | %.1f | %.1f | **%.1f** | %.1f | %.1f | %.1f" % (y, cayx, c, cay, p, rep, a + ad))
    cay_s.append(cay); rep_s.append(rep); ppd_s.append(p); exp_s.append(a + ad)
P("10-yr mean: CAY incl CAT %.1f | reported %.1f | fav PPD %.2f | expense %.1f"
  % (sum(cay_s) / 10, sum(rep_s) / 10, sum(ppd_s) / 10, sum(exp_s) / 10))
P("5-yr (2021-25) mean: CAY incl CAT %.1f | reported %.1f | fav PPD %.2f"
  % (sum(cay_s[-5:]) / 5, sum(rep_s[-5:]) / 5, sum(ppd_s[-5:]) / 5))
P("worst CAY incl CAT year: %.1f (%d)" % (max(cay_s), sorted(FILER)[cay_s.index(max(cay_s))]))

# ---------- float, CONVENTION 4 ----------
BS = {  # year: (unpaid L&LAE, unearned prem, reins recov on losses, ins&reins receivable, DAC,
        #        prepaid reins, total investments, cash, Chubb equity, AOCI, NCI)
 2020: (67811, 17652, 15592, 10480,  5402, 2769, 118669, 1836, 57691,   1067,    0),
 2021: (72943, 19101, 17366, 11322,  5513, 3028, 122323, 1811, 58328,  -1074,    0),
 2022: (75747, 19713, 18859, 11933,  6031, 3136, 113551, 2127, 50519, -10185,    0),
 2023: (80122, 22051, 19952, 13379,  7152, 3221, 136735, 2621, 59507,  -6809, 4184),
 2024: (84004, 23504, 19777, 14426,  8358, 3378, 150650, 2549, 64021,  -8644, 4373),
 2025: (88018, 26279, 20338, 15944, 10008, 3874, 168720, 2470, 73757,  -4975, 6022),
}
P("\n== FLOAT (CONVENTION 4) AND BOTH STAGE 0(b) RATIOS ==")
fl = {}
for y in sorted(BS):
    u, up, rr, ar, dac, pre, inv, cash, eq, aoci, nci = BS[y]
    f = u + up - rr - ar - dac
    fl[y] = f
    P(" %d float %d ( less prepaid reins %d ) | float/inv %.1f%% | inv/equity %.2fx | float/equity %.2fx | equity %d"
      % (y, f, f - pre, f / inv * 100, inv / eq, f / eq, eq))
P(" calibration: BRK 2010 [E5-46] 41.8%% / 0.45x | BRK 6/30/26 24.6%% / 0.96x | MKL 50.3%% / 2.01x | WTM 22.0%% | L consol 41.8%% / 2.96x")

# ---------- cost of float [E3-69] ----------
UW = {}
for y in R:
    UW[y] = R[y]["E"] - R[y]["A"] - R[y]["C"]
P("\n== COST OF FLOAT [E3-69] - DIAGNOSTIC, NOT ADDITIVE ==")
tot_uw = 0; tot_f = 0
for y in range(2021, 2026):
    avg = (fl[y - 1] + fl[y]) / 2
    P(" %d | P&C underwriting income $%dM | average float $%dM | cost of float %.2f%%"
      % (y, UW[y], avg, -UW[y] / avg * 100))
    tot_uw += UW[y]; tot_f += avg
P(" 5-yr (2021-25): underwriting $%dM on mean float $%dM -> %.2f%%" % (tot_uw, tot_f / 5, -tot_uw / tot_f * 100))
P(" BRK on the SAME five years, from this project BRK run: -3.6%%/yr on ~$162bn")

# ---------- component 2 [E5-48] ----------
IS = {  # IBT, net investment income, net realized gains(losses), MRB gains(losses), Other (income) expense, private-equity MTM
 2021: (9794,  3456,  1030,   91, -2367, 2115),
 2022: (6485,  3742, -1085,   80,    89, -250),
 2023: (9526,  4937,  -607, -307,  -836,  504),
 2024: (11455, 5930,   117, -140, -1023,  661),
 2025: (13044, 6465,   211, -288, -1297,  809),
}
NCI = {2021: 0, 2022: 0, 2023: -13, 2024: 368, 2025: 312}
P("\n== COMPONENT 2 - pre-tax earnings of everything else, dividends/interest REMOVED [E5-48] ==")
c2 = {}; opinc = {}
for y in sorted(IS):
    ibt, nii, nrg, mrb, oth, pe = IS[y]
    c2[y] = ibt - nii - nrg - mrb + oth
    opinc[y] = ibt - nrg - mrb - pe   # pre-tax OPERATING income (portfolio INCOME kept - the Q5 yield base)
    P(" %d | component 2 $%dM | pre-tax operating income $%dM | less NCI $%dM -> $%dM"
      % (y, c2[y], opinc[y], NCI[y], opinc[y] - NCI[y]))
P(" component 2: 5-yr mean $%dM | 3-yr mean $%dM" % (sum(c2.values()) / 5, (c2[2023] + c2[2024] + c2[2025]) / 3))
att = dict((y, opinc[y] - NCI[y]) for y in opinc)
P(" pre-tax operating attributable: 5-yr mean $%dM | 3-yr mean $%dM | 2025 $%dM"
  % (sum(att.values()) / 5, (att[2023] + att[2024] + att[2025]) / 3, att[2025]))
op19 = 5249 + 530; op20 = 4162 + 498
P(" 2019 $%dM  2020 $%dM (pre-LDTI; private-equity marks NOT separately disclosed for those years - stated)" % (op19, op20))
seven = [op19, op20] + [att[y] for y in range(2021, 2026)]
P(" 7-yr (2019-25) mean pre-tax operating $%dM" % (sum(seven) / 7))
# bottom-up cross-check of component 2, 2025
P(" 2025 bottom-up cross-check: P&C UW 6528 + Life UW -12 - interest 764 - amort 301 - integration 79 = %d vs top-down %d"
  % (6528 - 12 - 764 - 301 - 79, c2[2025]))

# ---------- Q5 yields ----------
P("\n== Q5 - THE YIELD; THE WINDOW SPREAD IS PART OF THE RANGE [E4-25, E4-38] ==")
wins = [("2025 only", att[2025]), ("3-yr 2023-25", (att[2023] + att[2024] + att[2025]) / 3.0),
        ("5-yr 2021-25", sum(att.values()) / 5.0), ("7-yr 2019-25", sum(seven) / 7.0)]
for lab, v in wins:
    P(" %-14s pre-tax $%6dM -> yield %.2f%% | sovereign %.2f%% | %+.2f pts over" % (lab, v, v / CAP * 100, SOV, v / CAP * 100 - SOV))
P(" perpetual growth needed to reach the ~10%% floor [E4-28] from each window:")
for lab, v in wins:
    P("   %-14s %.2f%%/yr" % (lab, 10.0 - v / CAP * 100))

# ---------- the Loews test ----------
P("\n== THE LOEWS TEST - what an OCF-based owner-earnings number would have claimed ==")
OCF = 12816; SBC = 400
resg = 69672 - 66270; uepg = 26279 - 23504
P(" OCF 2025 $%dM less SBC $%dM = $%dM -> %.2f%% of cap  (WRONG: double-counts the portfolio, counts reserve growth as cash)"
  % (OCF, SBC, OCF - SBC, (OCF - SBC) / CAP * 100))
P(" strip net reserve growth $%dM and unearned-premium growth $%dM -> $%dM (%.2f%% of cap): a %.0f%% collapse"
  % (resg, uepg, OCF - SBC - resg - uepg, (OCF - SBC - resg - uepg) / CAP * 100, (resg + uepg) * 100.0 / (OCF - SBC)))

# ---------- ROE [E2-01] and the tangible denominator [E2-43] ----------
NI = {2021: 8525, 2022: 5246, 2023: 9028, 2024: 9272, 2025: 10310}
TANG = {2023: 59507 - (19686 + 6775 + 3674), 2024: 64021 - (19579 + 6377 + 3223), 2025: 73757 - (20207 + 6241 + 2975)}
P("\n== Q3 PRIMARY TEST [E2-01] - earnings rate on equity capital employed ==")
eq = dict((y, BS[y][8]) for y in BS); ao = dict((y, BS[y][9]) for y in BS)
exa = dict((y, eq[y] - ao[y]) for y in eq)
t1 = []; t2 = []
for y in range(2021, 2026):
    r = NI[y] / ((eq[y - 1] + eq[y]) / 2.0) * 100
    r2 = NI[y] / ((exa[y - 1] + exa[y]) / 2.0) * 100
    t1.append(r); t2.append(r2)
    P(" %d ROE %.2f%% | ROE on equity EX-AOCI %.2f%%" % (y, r, r2))
P(" 5-yr mean ROE %.2f%% | ex-AOCI %.2f%%" % (sum(t1) / 5, sum(t2) / 5))
P(" 2025 return on TANGIBLE equity ([E2-43] unleveraged net tangible denominator) %.1f%%  (tangible equity 2025 $%dM, 2024 $%dM)"
  % (NI[2025] / ((TANG[2024] + TANG[2025]) / 2.0) * 100, TANG[2025], TANG[2024]))
P(" the goodwill wedge, reported separately and not hidden in book equity: $%dM = %.0f%% of Chubb equity"
  % (20207 + 6241 + 2975, (20207 + 6241 + 2975) * 100.0 / 73757))

# ---------- [E3-54] retention test ----------
P("\n== [E3-54] $1 of market value per $1 retained, five-year rolling ==")
sh20 = 450732625; p20 = 153.92; sh25 = 391101227; p25 = 312.12
mc20 = sh20 * p20 / 1e6; mc25 = sh25 * p25 / 1e6
divs = 1392 + 1379 + 1401 + 1455 + 1520; ni5 = sum(NI.values()); bb5 = 4861 + 3014 + 2478 + 2024 + 3387
P(" cap 12/31/20 $%.0fM (%d sh @ $%.2f) -> cap 12/31/25 $%.0fM (%d sh @ $%.2f): %+.0fM"
  % (mc20, sh20, p20, mc25, sh25, p25, mc25 - mc20))
P(" net income to Chubb 2021-25 $%dM less dividends declared $%dM = retained $%dM" % (ni5, divs, ni5 - divs))
P(" -> $%.2f of market value per $1 retained (dividends only as distribution)" % ((mc25 - mc20) / (ni5 - divs)))
P(" -> $%.2f if buybacks $%dM are also treated as distributions" % ((mc25 - mc20) / (ni5 - divs - bb5), bb5))
P(" book value per share 12/31/20 $%.2f -> 12/31/25 $%.2f = %+.1f%% (%.2f%%/yr); price %+.1f%% (%.2f%%/yr)"
  % (eq[2020] * 1e6 / sh20, eq[2025] * 1e6 / sh25, (eq[2025] / sh25) / (eq[2020] / sh20) * 100 - 100,
     (((eq[2025] / sh25) / (eq[2020] / sh20)) ** 0.2) * 100 - 100, p25 / p20 * 100 - 100, ((p25 / p20) ** 0.2) * 100 - 100))
P(" price/book now %.2fx | price/TANGIBLE book %.2fx | BVPS 12/31/25 $%.2f | TBVPS $%.2f"
  % (CAP / eq[2025], CAP / TANG[2025], eq[2025] * 1e6 / sh25, TANG[2025] * 1e6 / sh25))
for y, pr, shy in [(2023, 209.52, 405269637), (2024, 269.23, 400703663), (2025, 282.57, 391101227)]:
    bvps = eq[y] * 1e6 / shy
    P("   %d buybacks executed at $%.2f avg = %.2fx that year-end book value per share ($%.2f)" % (y, pr, pr / bvps, bvps))

# ---------- Q4 named death ----------
P("\n== Q4 NAMED DEATH, QUANTIFIED FROM FILED FIGURES [E3-24, E4-40] ==")
sens = [("NA Comm workers comp, 1pt tail factor", 1100, 10015),
        ("NA Comm US excess/umbrella, 5pt tail factor", 900, 4900),
        ("Overseas General long-tail, 6-month lengthening", 540, 5600),
        ("Global Reinsurance, 20% pattern change", 224, 1040)]
s = 0
for n, d, base in sens:
    P(" %-48s +/- $%4dM on $%6dM of net reserves (%.1f%%)" % (n, d, base, d * 100.0 / base))
    s += d
P(" sum of the filer OWN reasonably likely deviations: $%dM = %.1f%% of Chubb equity, %.0f%% of 2025 pre-tax operating income"
  % (s, s * 100.0 / 73757, s * 100.0 / att[2025]))
adv = 2000
newcr = 85.7 + adv / 45790.0 * 100 + 2.5
newuw = 45790 * (100 - newcr) / 100.0
P(" scenario: long-tail PPD flips from +$61M favourable to $%dM adverse AND the 2.5 pts of favourable PPD is lost:" % adv)
P("   P&C combined ratio 85.7 -> %.1f | underwriting income $6,528M -> $%.0fM | pre-tax operating $%dM -> $%.0fM | yield %.2f%% -> %.2f%%"
  % (newcr, newuw, att[2025], att[2025] - (6528 - newuw), att[2025] / CAP * 100, (att[2025] - (6528 - newuw)) / CAP * 100))
P(" filed natural-cat PML (net, pre-tax, 10-K p.73): 1-in-10 $3,003M (4.1%% of equity) | 1-in-100 $5,862M (7.9%%) | 1-in-250 $9,285M (12.6%%)")
cats = [1175, 3249, 2411, 2231, 1828, 2401, 2863]
P(" realised catastrophe losses 2019-25: %s -> mean $%dM, i.e. AT the modelled 1-in-10, on a book whose premium was 58%% smaller at the start of the window"
  % (" ".join(str(c) for c in cats), int(sum(cats) / 7)))

# ---------- per-share, for the record ----------
P("\n== PER SHARE, AT THE CURRENT COUNT (385,799,859) ==")
for lab, v in wins:
    P(" %-14s pre-tax operating per share $%.2f" % (lab, v * 1e6 / SH))
P(" dividend declared 2025 $3.82/share; shareholder-approved ceiling $3.88 for the year to the 2026 AGM")
