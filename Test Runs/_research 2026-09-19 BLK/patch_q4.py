import io, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "2026-09-19 Run - BLK BlackRock.md")
s = io.open(P, encoding="utf-8").read()

OLD = """## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**"""
NEW = """## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**

### Owner earnings — the one number **[E2-23]**"""
assert OLD in s
s = s.replace(OLD, NEW, 1)

OLD2 = """**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
- **Short-window mean** (window: ____ ): ____
- **Long-window mean** (window: ____ ): ____
- **Spread, conservative end:** ____ %
- **Combined range** (window spread × capex band): ____ to ____
- *Is that range too wide to reach a conclusion? If yes, **that is the verdict** **[E4-25]** —
  close the file, do not resolve it by preference:* ____
- *A wide spread is also a Q4 finding: a distorted year sits in the window (a pandemic year, an
  acquisition, a disposal), which bears on earnings reliability **[E5-11]**. Name it: ____*
- Owner earnings by year: ____
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default proxy
  **[E3-44, E2-41]**; for capital-intensive businesses the D&A end is INVALID and (c) is judged
  up from total capex **[E5-20]**. Which case is this, and why: ____
- Band used ____ ; where in
  the band it sits and the reason cited from the filing: ____
- Stock compensation subtracted in full **[E5-06]**: ____
- *If the capex band changes the verdict → **UNKNOWABLE**.*

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- Evidence: ____

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings ____
- (2) massive liquid assets ____
- (3) **no significant near-term cash requirements** ____  ← *the one that usually kills*
- Leverage, named and quantified **[E4-16, E3-29]** — *there is no ratio ceiling in this
  framework and the corpus supplies none*: ____

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: ____
- Quantified from filed figures, and the resulting outcome: ____
- Likelihood: [ ] likely [ ] a real possibility [ ] a low-level possibility
- *If no mechanism can be named at all → consider **UNKNOWABLE**.*
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**"""

NEW2 = r"""### FIRST — HOW THE CONSOLIDATED FUNDS WERE SEPARATED, because the reported line is unusable

**The GAAP operating cash flow of this company is not the owner's cash and the filer says so.**
Funds BlackRock seeds or controls are consolidated line by line ("CIPs"), and **the funds' own
securities purchases sit inside OPERATING activities** while **the money the outside investors put
in to buy them sits inside FINANCING**. The two halves of one transaction are in different
sections, so the reported number moves with fund seeding rather than with the business:

| ($M) | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| **Operating cash flow, GAAP, as filed** | 4,165 | 4,956 | **3,927** | 236 | **247** |
| of which: "Net (purchases) proceeds within CIPs" | (1,780) | (2,672) | **(4,214)** | — | — |
| financing: "Net subscriptions received … from noncontrolling interest holders" | +1,627 | +2,405 | **+3,827** | — | — |
| **Impact on cash flows of CIPs (filer's own column)** | (1,519) | (2,311) | **(3,536)** | (1,743) | **(2,859)** |
| **Operating cash flow EXCLUDING CIPs (filer's own column)** | **5,684** | **7,267** | **7,463** | **1,979** | **3,106** |

**In 2025 the reported figure understates the owner's operating cash by $3,536M — 47% of the
truth.** This run therefore uses the filer's own **"Cash Flows Excluding Impact of CIPs"**
reconciliation, published in the 10-K MD&A for 2024 and 2025 (`0001193125-26-071966`), in the
FY2023 10-K for 2022 and 2023 (`0000950170-24-019271`), in the FY2022 10-K for 2021
(`0000950170-23-004343`), and in the 10-Qs for the half-years. It is a non-GAAP measure and it is
flagged as one — but it is a *reconciliation*, quantified at every line, and the same separation is
published on the balance sheet, where a CIPs column of **$3,215M of assets and $2,757M of the
noncontrolling interests** is struck out alongside **$68,020M of separate-account assets matched
dollar for dollar by an identical liability**. **Total assets go from $169,998M to $98,763M once
what is not the owner's is removed. This is the insurer and Up-C treatment applied to a fund
consolidator, and here the filer did the arithmetic for us [E2-26].**

*Two further separations, recorded:* **[E3-04]** look-through — equity-method investees produced
$51M of earnings in 2025 and paid $429M of distributions, so there is nothing to add back; the
yield is not understated on that account. **[E2-23] constraint 3** — the working-capital increment
is netted inside operating cash flow from one audited line, which is why the CONVENTION uses cash
flow at all; the largest single swings were accrued compensation **+$659M (2025)** and **−$711M
(2022)**, which broadly cancel across the window.

**A seasonality warning that no annualisation may ignore.** Year-end incentive compensation is
accrued through the year and paid in the first quarter, so **H1 ex-CIP operating cash was $1,979M
in 2025 against $7,463M for the full year — 26.5%.** H1 2026 was $3,106M. **A trailing-twelve-month
figure built from a half-year is wrong by a factor of nearly two in either direction.** The TTM to
2026-06-30 is $7,463 − $1,979 + $3,106 = **$8,590M**, which is reported below as a fact and is
**not** used as the mean.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."*
Arithmetic: `Test Runs/_research 2026-09-19 BLK/oe.py` and `oe2.py`, outputs in `oe.txt`, `oe2.txt`.

- **Long-window mean (2021-2025, the corpus default [E2-42, E1-03]):** ex-CIP operating cash
  **$6,450.0M**, less stock pay at the larger of charge and grant value **$1,101.0M**, less (c) →
  **$4,756.0M** at the D&A end, **$4,979.4M** at the capex end.
- **Short-window mean (2023-2025):** ex-CIP operating cash **$6,804.7M**, less stock pay
  **$1,297.7M**, less (c) → **$4,796.3M** at the D&A end, **$5,182.3M** at the capex end.
- **Spread, conservative end:** the two conservative ends are **$4,756.0M** and **$4,796.3M** —
  **0.8%.** The window choice barely matters, which is itself worth recording: there is no
  distorted year doing the work.
- **Combined range (window spread × capex band × SBC measure): $4,756M to $5,583M**, a width of
  **17.4%** around the midpoint. **Is that too wide to conclude [E4-25]? No.** Every end of it
  produces the same Q5 answer by a wide margin, and the framework's instruction is to close the
  file when the range cannot decide — here it decides at every end.
- **A wide spread is also a Q4 finding [E5-11] — and there is no wide spread here.** The window
  spread is 0.8%. What IS distorted is the *per-share* series, below, and the distortion is the
  acquisition programme, not a pandemic or a disposal.

**Owner earnings by year, and per share — the series the total hides:**

| ($M unless stated) | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Operating cash flow excluding CIPs | 6,168 | 5,668 | 5,684 | 7,267 | **7,463** |
| Stock pay, the larger of charge and grant value **[E3-70]** | 786 | 826 | 707 | 1,379 | **1,807** |
| (c) at the capex end | 341 | 533 | 344 | 255 | 375 |
| (c) at the D&A end | 415 | 418 | 427 | 579 | **1,126** |
| **Owner earnings, c = capex** | 5,041 | 4,309 | 4,633 | 5,633 | **5,281** |
| **Owner earnings, c = D&A** | 4,967 | 4,424 | 4,550 | 5,309 | **4,530** |
| Diluted weighted-average shares incl. Subco Units (millions) | 154.4 | 152.4 | 150.7 | 151.6 | **160.9** |
| **Owner earnings PER SHARE, c = capex** | 32.65 | 28.27 | 30.74 | **37.16** | 32.82 |
| **Owner earnings PER SHARE, c = D&A** | 32.17 | 29.03 | 30.19 | **35.02** | **28.15** |

**The per-share read is the one that matters and it is the DIS-style finding.** On the D&A end,
owner earnings per share **peaked at $35.02 in 2024, fell 19.6% to $28.15 in 2025, and are 12.5%
BELOW where they were in 2021.** On the capex end they are **flat over four years: $32.65 →
$32.82, +0.5%.** Assets under management rose **40.3%** over the same four years. **Whichever end
of the band you take, four years of forty-per-cent asset growth produced no growth at all in owner
earnings per share.** That is the Q2 finding arriving in the cash: the price fell, the share count
rose, and the volume made up the difference in dollars but not per share.

- **Maintenance capex — a DISCLOSED JUDGMENT, and here the corpus default runs BACKWARDS.
  Stated openly, because [E2-23] says "(c) must be a guess."**
  The corpus default is D&A **[E3-44, E2-41]**, and the named exception class is the
  capital-intensive filer where D&A *understates* renewal **[E5-20, E4-47]**. **BlackRock is the
  mirror image of that exception: D&A OVERSTATES required maintenance, because $775M of the
  $1,126M of 2025 D&A — 68.8% — is amortisation of intangibles acquired in the GIP, Preqin and HPS
  deals**, and none of that is a capital expenditure the business must make to hold its position
  and volume. It is the write-off of a purchase price already paid — paid in shares and units that
  are **already in the 160.9M denominator above**. Deducting it in (c) as well would charge the
  same cost twice.
  **The judgment, stated: (c) is judged at the capex end — total purchases of property and
  equipment, five-year mean $369.6M — and the acquisition cost enters through the share count and
  the goodwill wedge, not through (c).** The D&A end is carried as the display of the alternative,
  not because it is invalid but because it double-counts. Note that even the capex end is already
  conservative: it uses *total* capex, with no maintenance/growth split, because the filing
  discloses none.
  **Band used: $369.6M to $593.0M (five-year means).** Property and equipment net is $1,256M
  against $24,216M of revenue; this is not a capital-intensive business by any reading.
- **THE THIRD END, disclosed rather than folded into the band, because it is the real (c) question
  for this company.** [E2-23]'s (c) is what the business *requires* to *"fully maintain its
  long-term competitive position"*. Q2 established that BlackRock's blended fee rate held only
  because it bought GIP, Preqin and HPS. **If the acquisition programme is maintenance, then (c)
  includes it**, and the arithmetic is brutal: five-year mean cash paid for acquisitions $1,545.4M
  plus five-year mean stock and units issued for acquisitions $2,919.6M = **$4,465.0M a year**,
  which takes five-year owner earnings from $4,756M to **$291M.**
  **This run does NOT adopt that end, and says why.** Unit volume does not require it: AUM grew
  $698,261M organically in 2025 against $120,961M from acquisitions, and the filer's own
  roll-forward keeps the two apart. The acquisitions bought a *new, higher-priced product line*,
  which is growth, not maintenance. **But the third end is recorded because it is the honest
  statement of what the reader is being asked to believe: that $28.3 billion in twenty-one months
  was optional.** If a future reader concludes it was not optional, owner earnings are an order of
  magnitude smaller, and that judgment is where this file would be reopened.
- **Stock compensation subtracted in full [E5-06], and at the [E3-70] measure, not the charge.**
  The corpus requires *"an amount equal to what the company could have realized by publicly
  selling options of like quantity and structure"*; the reported charge is *"the floor of the
  subtraction, not the measure."* From the stock-compensation note: **grant-date fair market value
  of RSUs granted was $1.7bn (2025), $1.1bn (2024), $565M (2023), $662M (2022), $664M (2021)**,
  plus performance-based RSUs granted of **$107M, $279M, $142M, $164M, $122M**. Totals **$1,807M,
  $1,379M, $707M, $826M, $786M** against charges of **$1,307M, $753M, $630M, $708M, $734M**:
  **grant value exceeds the charge in all five years, by 38% in 2025 and 83% in 2024.** The larger
  figure is used throughout. **SBC RESOLVES and is COMPLETE**: `ShareBasedCompensation` is present
  on the face of the cash-flow statement in every year of both windows, and the grant-value
  disclosure covers every year — neither `SBC_UNRESOLVED` nor `SBC_PARTIAL` applies.
- *If the capex band changes the verdict → **UNKNOWABLE**.* **It does not.** Both ends produce the
  same Q5 answer and the same Q4 answer.
- **Windage count: ONE at Q4** — the SBC measure is taken at the larger of two disclosed figures,
  which is conservative; the (c) judgment is *not* a second application, because it was argued from
  the composition of the D&A line rather than chosen for conservatism, and the conservative
  alternative is displayed beside it. **[E4-11, E4-48]**: the margin is applied once, at the end,
  and Q5 below never reaches a margin because it fails at the floor.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [x] **good — attractive return, earned also on added capital**
- [ ] gruesome — grows, eats capital, earns little
- **Evidence, and the word that decides it is "rising".** *"The great one pays an extraordinarily
  high interest rate **that will rise as the years pass**. The good one pays an attractive rate of
  interest that will be earned also on deposits that are added."* BlackRock is unambiguously the
  second and unambiguously not the first: the return is attractive and it is earned on every dollar
  of added AUM with almost no incremental capital ($375M of capex on $24.2bn of revenue), **and the
  rate is falling, not rising — 16.29bp to 15.22bp blended, and down in every organic line.**
  **[E4-43] governs the consequence: the good class PASSES.** *"nothing shabby about earning $82
  million pre-tax on $400 million of net tangible assets."* Only gruesome fails Q4. **This is
  nowhere near gruesome**: it consumes no capital to grow and it earns a high return on the
  tangible capital it uses. It ranks below great at Q5, and that is all [E4-20] does here.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — PASS, and it is the most reliable revenue line in
  this queue.** $19,179M of base fees billed as a percentage of a $14 trillion balance, monthly,
  under contracts that renew by default. The reliability is qualified by market level, not by
  customer decision: in the worst recent year (2022, global equities down roughly a fifth) base
  fees fell only **5.3%**, from $15,260M to $14,451M, and operating income stayed above $6.3bn.
  **[E3-55]** applies: volatility with a certain mechanism is not a defect.
- **(2) massive liquid assets — PASS, with the bank line NOT counted [E5-39].** Own cash
  **$11,007M** after removing the CIPs' $461M. Investments ex-CIP $10,704M, of which an unknown
  part is illiquid seed and co-investment capital, so it is not counted as liquid either. The
  filer's own "total liquidity resources" of $16,907M includes **$5,900M of undrawn revolver**,
  which *"the kindness of strangers"* rule excludes. **$11.0bn of unencumbered cash against
  $12.8bn of long-term debt and $614M of annual interest.**
- **(3) no significant near-term cash requirements — PASS, and this is the one that usually kills,
  so the detail matters.** Long-term borrowings **$12,875M at maturity value, carrying $12,768M,
  with the earliest maturity $700M in March 2027 and $800M in July 2027**, and the ladder running
  to 2055. No commercial paper outstanding at either 2025-12-31 or 2026-06-30 against a $5bn
  programme. The obligations that could bite:
  - **$2.4bn of unfunded capital commitments to sponsored products, "callable on demand at any
    time"** — the only genuinely on-demand item, and it is a third of one year's owner earnings.
  - **$8,429M of contingent consideration — and it is payable in SHARES AND UNITS, not cash.**
    GIP 4.0-5.2M shares, HPS 2.8-4.4M Subco Units. **This is [E3-52]'s animal turned into an
    earn-out: a very large liability with no cash due date and no covenant.** It is a severe
    dilution item and a trivial solvency item, and the two must not be confused.
  - Dividends and Subco distributions **$3,347M in 2025**, with the 2026 dividend raised 10%
    ($5.73 a quarter × 4 × ~162.5M ≈ $3.7bn), plus a **$2.0bn announced 2026 buyback**.
    Both discretionary.
- **[E2-54]'s coverage test, run as written:** *"all interest, both payable and accrued,
  comfortably met out of current cash flow net of ample capital expenditures."* Ex-CIP operating
  cash $7,463M less capex $375M = **$7,088M against $614M of interest expense — 11.5x**; cash
  interest paid was $482M, so 14.7x on cash. **Zips no wallet.**
- **Leverage, named and quantified [E4-16, E3-29]** — *no ratio ceiling exists in this framework
  and the corpus supplies none for subject companies*: borrowings **$12,768M** against total
  BlackRock, Inc. stockholders' equity **$55,888M = 0.23x**, and against ex-CIP operating cash
  **1.7x**. Against **negative** net tangible equity the ratio is undefined, which is the honest
  statement of where the debt sits: **it is secured by a fee stream, not by assets.** Note the
  structural point recorded at Step 0: the notes are issued by New BlackRock and guaranteed by Old
  BlackRock, or the reverse, with combined Obligor Group financials published — so the debt sits
  at the top of the house and is not ring-fenced away from the fee stream.
- **[E2-60]'s third dimension of maintenance — RECORDED AS A CAUTION, not a failure.** Restricted
  earnings are those whose payout costs *"its financial strength"*. In 2025 dividends and Subco
  distributions $3,347M plus share and unit repurchases $1,951M = **$5,298M against owner earnings
  of $4,530M (D&A end) to $5,281M (capex end)**, with net new borrowing of $284M and $167M of
  option proceeds making up the rest. **The company distributed essentially all of its owner
  earnings, and slightly more than the conservative measure of them, and has announced a larger
  distribution for 2026.** That is not oblivion — the balance sheet absorbed it easily — but it
  means the acquisition programme is funded by paper because the cash is committed.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**

**First, the honest framing. This company does not die; the owner's return does.** [E4-51]
requires the argument against my position stated better than its opponents would state it, so:
**a holder would say BlackRock is the most survivable business in this queue, and on Q4's own three
tests they are right.** It has no plant, no inventory, no leverage worth the name, no near-term
cash call, and a revenue line that fell 5.3% in the worst equity market in fifteen years.

**Mechanism 1 — THE PASS-THROUGH, shape #11, and it is the death of the return, not of the
company.** The scale gains of index management flow to the buyer, not to the owner **[E3-62]**:
*"how much is going to stay home and how much is just going to flow through to the customer."*
Quantified from the filings and already shown at Q2: **ETF average AUM +60.3% from 2021 to 2025
while the ETF fee rate fell 17.1%; total AUM +40.3% while base fees rose 25.7%; owner earnings per
share flat to −12.5% over the same four years.** Extend the trend and the arithmetic is simple:
at the observed rate of compression (−1.6% a year blended, −4.6% a year on ETFs), AUM must compound
at roughly 5% a year merely to hold base fees level. **Likelihood: already happening — this is not
a forecast, it is the filed record.**

**Mechanism 2 — the market, which is the same mechanism with a shorter fuse.** 57.9% of the
$15,344,624M of AUM at 2026-06-30 is equity. Modelled at the 2025 blended rate of 15.22bp:

| scenario | AUM after | change | base fees at 15.22bp | vs 2025 actual $19,179M |
|---|---|---|---|---|
| equity −30%, everything else −5% | $12,355,334M | −19.5% | $18,805M | −2.0% |
| equity −40%, everything else −10% | $11,143,691M | −27.4% | $16,961M | −11.6% |
| equity −50%, everything else −15% | $9,932,048M | −35.3% | $15,117M | −21.2% |

*(Limit stated: applying the blended rate understates the hit, because equity prices above the
blend and the mix would shift toward lower-fee fixed income and cash. Directionally the model is
conservative in the wrong direction and is shown anyway rather than tuned.)* **Even the worst row
leaves base fees above their 2021 level and interest covered many times over. Likelihood of the
middle row over a decade: a real possibility. Consequence: a poor decade for the owner, not an
impairment.**

**Mechanism 3 — the one place a real balance-sheet loss lives, and it is the securities-lending
indemnity. Consider some mathematics [E3-24].** From Note 16: *"The amount of securities on loan
as of December 31, 2025 and subject to this type of indemnification was approximately **$353
billion**"*, against *"cash and securities totaling approximately **$375 billion**"* held as
collateral — **106.2%**, and the filing states minimum collateral *"generally ranging from
approximately 102% to 112%"*. The filer's conclusion: *"The fair value of these indemnifications
was not material at December 31, 2025."*

| if borrowers holding … | default with a collateral shortfall of … | loss | = % of $55,888M equity | = % of 2025 net income |
|---|---|---|---|---|
| 5% of the loaned book ($17.7bn) | 15% | **$2,648M** | 4.7% | 48% |
| 20% of the loaned book ($70.6bn) | 15% | **$10,590M** | 18.9% | 191% |
| 20% of the loaned book ($70.6bn) | 30% | **$21,180M** | 37.9% | 381% |

**[E4-40] is the governing instruction here: model exposure, not experience.** *"all of us in the
industry made a fundamental underwriting mistake by focusing on experience, rather than exposure."*
The experience is spotless and the framework says a benign loss history is *"not only useless, but
actually dangerous"* as a guide. A 2-12% collateral buffer against a portfolio of equities lent to
banks and broker-dealers is a buffer against ordinary volatility, not against a simultaneous
counterparty failure and a gap-down. **Likelihood: [x] a low-level possibility** — the collateral
is marked daily, borrowers are *"primarily … highly rated banks and broker-dealers"*, and the
middle row would require a systemic event. **But it is the only mechanism in this file that can
take a fifth of the equity, and it is the one an investor in a "capital-light" asset manager would
not think to look for.**

**Mechanism 4 — dilution, which is a certainty rather than a risk.** $8,429M of contingent
consideration payable in **4.0-5.2M shares plus 2.8-4.4M Subco Units**: up to **9.6M more units on
162.5M, +5.9%**, and the earn-out was revalued **upward by $720M in 2025**, meaning it is tracking
toward the top of the range. **Likelihood: likely.** It costs the owner ~6% of everything and
appears nowhere in the adjusted earnings.

- **VERDICT: [x] IN — RECORDED, NOT GOVERNING** (the file closed at Q2).
  All three staying-power strengths pass, interest is covered 11.5x out of cash flow net of capex,
  the earliest maturity is March 2027, and the largest liability on the balance sheet is payable in
  paper. Owner earnings are **$4,756M to $5,583M** across two windows and both ends of (c), a
  17.4% band that decides the same way at every end, with **SBC resolved, complete, and taken at
  the grant-value measure [E3-70]**. The business survives every mechanism this run can name.
  **The finding that matters is not about survival: owner earnings PER SHARE are flat to 12.5%
  lower than four years ago on 40.3% more assets.** The survival shape is **#11 THE PASS-THROUGH**,
  with a proposed feature recorded at the register below."""

assert OLD2 in s, "Q4 anchor not found"
s = s.replace(OLD2, NEW2, 1)
io.open(P, "w", encoding="utf-8").write(s)
print("Q4 written")
