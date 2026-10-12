"""Writes Q7 into the run file, the buyback line back into Q6, and marks Q8 to Q12 NOT REACHED."""
p = "Test Runs/2026-10-11 Run - UNP Union Pacific.md"
s = open(p, encoding="utf-8").read()

old_q7 = """## Q7 — WHAT IS IT WORTH? STOP.
*(not yet written)*"""
new_q7 = """## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; worked "with a range of possibilities" **[L2000-024]** by Q7's range
convention, at the sovereign of Step 0, 5.60%. Arithmetic in `_research 2026-10-11 UNP/scripts/q7.py`, output in
`q7_output.txt`; every input a filed figure named below.

**The cash input, owner cash after every real cost** **[L2021-003]** (Q4's recast; $M; each year's 10-K; interest after
the company's own effective tax rate, which ran 22.1% to 23.3%):

| FY | OCF | Stock pay | Capex | Finance-lease principal | Owner cash (equity basis) | After-tax interest | Before interest (all-equity basis) | Growth capex (capacity and commercial) | Maintenance-only, before interest |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 9,032 | 88 | 2,936 | 106 | 5,902 | 890 | 6,792 | 527 | 7,319 |
| 2022 | 9,362 | 99 | 3,620 | 91 | 5,552 | 980 | 6,532 | 584 | 7,116 |
| 2023 | 8,379 | 107 | 3,606 | 65 | 4,601 | 1,038 | 5,639 | 664 | 6,303 |
| 2024 | 9,346 | 118 | 3,452 | 47 | 5,729 | 974 | 6,703 | 500 | 7,203 |
| 2025 | 9,290 | 142 | 3,791 | 36 | 5,321 | 1,019 | 6,340 | 617 | 6,957 |
| **Mean** | | | | | **5,421** | | **6,401** | | **6,980** |
| Growth, 2021 to 2025, compound | | | | | **-2.56%** | | **-1.71%** | | -1.26% |

**The window and the specifics.** (a) *Cycles:* the literal five-year window FY2021 to FY2025 is the central figure.
Neither end year is aberrational on the filer's own description: FY2021's capital plan was "approximately $2.9 billion,
essentially flat with 2020" because "Implementation of our new transportation plan has generated capacity" (FY2020 10-K,
`0000100885-21-000068`), a plan, not an event; FY2025 had $0.3B of bonus-depreciation cash (10-K MD&A), kept because it
recurs while the spending does. The year the filer does describe as hit by one-time items is FY2023 ("$454 million of
payments related to the 2022 one-time charge for agreements reached with our labor unions and the ratification charge";
FY2023 10-K, `0001437749-24-003599`), inside the window, so it stays in the average and no cycle base is used. A
sensitivity is shown beside: the five-year averages 2016 to 2020 and 2021 to 2025 (before interest; finance leases not
tagged before 2019 and so left out of both) grew 3.82% a year. (b) *Decline:* the growth shown between the end years is
negative on every series, so it is carried as negative and makes the bottom; the no-growth case is the top. (c)
*Acquisitions:* none inside the window; the Norfolk Southern deal is signed, not closed, and is valued beside the
central figure, not in it. (d) *Working capital:* inside cash from operations; no single-year draw tied to one contract
(FY2023's labour payments are one-time by the filer's description but are cash the owner did not get, and stay). (e)
*Growth spending:* the filing allows the maintenance guess (Q3: "capacity and commercial facilities" is the filer's
growth line). The growth that spending bought, measured on owner cash, is negative, so it was worth less than its cost
and the inversion applies: the top of the range is the maintenance-only case at no growth, the bottom the all-spending
case at the growth shown, since "growth can destroy value" **[L2000-023]**. (f) *The cap:* no positive growth is carried,
so no cap binds; the 3.82% sensitivity, carried ten years, would put owner cash at 28% of sales against a highest share
of 31% in the filings read (FY2021), so it too stands uncut. Zero nominal growth after year ten; nothing above the
discount rate is carried after year ten **[M1997-095]**.

**Whose tax and on what the floor is earned.** Owner cash is after the company's own income tax, no conversion; no
carryforward or credit that runs out inside ten years (purchased tax credits and bonus depreciation are disclosed, not
expiring shelters). Central figure on the **all-equity basis**: owner cash before interest against the market value plus
net debt. Net debt at 2026-06-30 (10-Q): debt due within one year $1,288M plus debt due after one year $29,039M (finance
leases inside these lines) less cash $1,614M and short-term investments $500M = **$28,213M**; operating leases ($609M
non-current) left out, and said so; no subsequent event in the 10-Q changes it. Enterprise value at the price:
$165,355M + $28,213M = **$193,568M**.

**The value range** (all specifics applied; $ a share):

| Case | Base $M | Growth carried | Value at 5.60% $M | Per share, all-equity (less net debt, / 594.075M) | Equity-only per share |
|---|---|---|---|---|---|
| Top: maintenance-only, no growth | 6,980 (equity basis 5,999) | 0% | 124,639 | **$162.31** | $180.33 |
| Middle reference: all spending, no growth | 6,401 (5,421) | 0% | 114,310 | $144.93 | $162.95 |
| Bottom: all spending, growth shown | 6,401 (5,421) | -1.71% (-2.56%) | 99,884 | **$120.64** | $133.15 |
| Sensitivity beside: all spending, cycle-average growth | 6,401 | +3.82% | 154,832 | $213.14 | not computed |

**VALUE RANGE: $120.64 to $162.31 a share (all-equity basis, central); $133.15 to $180.33 equity-only; against $278.34.**
The literal window is the central window here, so it is the figure shown; the cycle-average sensitivity beside it is
$213.14. Width 1.35 to 1.

**The floor, tested first** (CONVENTION, Q7, adopted 2026-10-10): the expected return at $278.34 (the discount rate at
which each case's cash equals the price paid; all-equity against $193,568M, equity-only against $165,355M): top case
3.61% (equity-only 3.63%); no-growth all-spending 3.31% (3.28%); bottom 2.84% (2.61%); the cycle sensitivity 4.53%. **No
case earns the floor of about ten percent, nor half of it**: "we don’t want to buy equities where our real expectancy is
below 10 percent" **[M2003-149]**. Even the most generous case this run could construct, growth of 3.82% a year for ten
years, earns less than the long Treasury's 5.60%.

**The merger, valued beside as if closed** (specific (c), adopted 2026-10-10; the box is decided on the central
figure). NSC's own filed record (10-Ks FY2021 to FY2025, accession `0001628280-26-006268` for FY2025, XBRL with
accessions in `notes_nsc_series.txt`): owner cash before interest 3,232; 2,769; 1,359 (2023, the East Palestine year);
2,267; 2,715; mean **$2,468M**. Combined mean $8,869M; combined growth 2021 to 2025 -2.51%. Net debt as if closed: UNP
$28,213M + NSC $15,547M (NSC 10-Q 2026-06-30: $649M current and $15,967M long-term debt less $1,069M cash) + the $20B
cash consideration = $63,760M; shares 594.075M + 224.6M issued (one for each NSC share outstanding, NSC 10-Q cover) =
818.7M. **As if closed: $80.81 to $115.58 a share (all-equity basis; all-spending cases, since NSC's growth-spending
split was not read), no synergy counted** **[L2016-008]**. Like for like with the standalone all-spending cases ($120.64
at the growth shown, $144.93 at no growth), the value per UNP share falls by a fifth to a third on the deal's filed
terms and the two companies' filed cash; the $2.75B of stated "annualized synergies" would have to be real, and after
tax, to close the gap.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged.
All-equity: top $70.00, bottom $48.59, **fair price $59.30 a share** (central); equity-only: top $100.99, bottom $76.89,
**$88.94 a share** beside it. Tax: the company's own, as above. No cheap price is reported.

- **VERDICT: OUT.** No case in the range earns the floor at the price **[M2003-149]**: the price, $278.34, is 1.7 times the
  top of the range, and the expected return on every case is between 2.6% and 4.5%, below the long government bond.
  Closed OUT by the floor convention, tested before the width; the range itself is narrow (1.35 to 1), so the file is
  not TOO HARD on this question. Q8 to Q10 and Q12 are NOT REACHED."""
assert old_q7 in s
s = s.replace(old_q7, new_q7)

old_bb = """**Against the bottom of the Q7 range (written back from
  Q7):** *(see the line after Q7 is closed)*."""
new_bb = """**Against the bottom of the Q7 range (written back from
  Q7):** the bottom is $120.64 a share on the all-equity basis ($133.15 equity-only); every year's average price,
  $143.70 (2018) to $240.51 (2024), sits above it, and from 2021 on the prices sit above the top ($162.31). The rows read
  such purchases by what they did: "if you buy it for $1.10, you are doing them no favor at all" **[M2014-008]**. (Today's
  range rests on FY2021 to FY2025 cash, at least as high as the earlier years' cash, so the earlier purchases are not
  made to look worse by the comparison.) **Weighs against.**"""
assert old_bb in s
s = s.replace(old_bb, new_bb)

nr = [
    ("""## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
*(not yet written)*""", """## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (closed at Q7). See AFTER THE STOP."""),
    ("""## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
*(not yet written)*""", """## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (closed at Q7). See AFTER THE STOP."""),
    ("""## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
*(not yet written)*""", """## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed at Q7)."""),
    ("""## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
*(not yet written)*""", """## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed at Q7)."""),
]
for a, b in nr:
    assert a in s, a[:40]
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
