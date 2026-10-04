# Company Run — Costco Wholesale Corporation (COST) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**POSITION NOTE, declared before any verdict:** the operator holds **no Costco position**.
This is a fresh entry run: Q1→Q5 in hard sequence, stop at the first non-IN. Q6 is still
answered (pre-committed yardsticks, entry bands, catalysts) but there is no [E2-28] hold
read, because there is nothing held.

Analyst inputs beyond the filings: `Test Runs/_research 2026-08-26/COST competitor row
(BJ-Sams).md` (the Q2 row, committed alongside this file) and
`Test Runs/2026-08-28 Run - ASML v4.1.md` (format precedent only).

**Freshness note:** Costco's fiscal 2026 ended 2026-08-30; its 10-K will not be filed
until roughly October 2026. The freshest filed set is therefore the **FY2025 10-K plus the
Q3 FY2026 10-Q**, and that is what this run uses, said here plainly.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** [E4-15, E3-32]:
- rate **5.22%** · date **2026-08-28** · source: **U.S. Treasury daily yield curve, 30 Yr
  column (home.treasury.gov)** — the issuing authority itself. Costco earns and reports
  in USD (majority; FX effects disclosed and quantified in the filing).
- *Route note:* FRED DGS30 (the CLAUDE.md mirror) was unreachable from this machine on
  2026-08-30 (connection timeout, two independent routes). The Treasury's own daily curve
  outranks the FRED mirror on the evidence ladder, so no UNRESEARCHED arises; `tools/run.py`
  arithmetic was reproduced locally with the Treasury rate passed in.
- FX: none required. Quote currency = earnings currency = USD.
- Price: **$945.47, close 2026-08-28, via aggregator — live quote only, flagged.**
- Market cap: 444.8M weighted diluted shares (FY2025 10-K; 443.2M issued and outstanding
  at 2025-08-31) × $945.47 = **$420.5B**.

**The filing was read** — not tagged data [E3-27]:
- [x] MD&A (overview, results of operations, membership fees, gross margin, SG&A,
  liquidity, capex plans, dividends, buyback)
- [x] cash-flow statement incl. detail lines (D&A, SBC, inventory/payables swings,
  buyback, dividend, debt lines, supplemental cash-tax and interest-paid lines)
- [x] footnotes (Note 1 policies incl. LIFO and R&M expensing; Note 4 debt and maturity
  table; Note 10 commitments and contingencies / legal proceedings; Note 11 segments)
- documents:
  - **Form 10-K FY2025 (52 weeks ended 2025-08-31), filed 2025-10-08, accession
    0000909832-25-000101**, primary document cost-20250831.htm, US GAAP, USD.
  - **Form 10-Q Q3 FY2026 (12/36 weeks ended 2026-05-10), filed 2026-06-03, accession
    0000909832-26-000051** — for freshness (renewal rate, member counts, comps).
  - Form 10-K FY2024, accession **0000909832-24-000049** — one figure only (the prior-year
    renewal rate, for the fee-increase trend).
- figures cross-checked against the filed statement: **FY2025 operating cash flow
  $13,335M** — identical in the XBRL tag, the filed consolidated statement of cash flows
  ("Net cash provided by operating activities | 13,335"), and the MD&A liquidity text
  ("Net cash provided by operating activities totaled $13,335 in 2025"); and **net sales
  $269,912M**, identical in the income statement, the MD&A highlights, and Note 11.
- **52/53-week flag:** Costco reports on a 52/53-week year. **FY2023 was 53 weeks**
  (FY2025 and FY2024 were 52). FY2023 revenue/OCF carry roughly a +2% extra-week benefit
  inside the 5-year window; the filing itself calculated FY2024 comparable sales on
  comparable retail weeks. Flagged wherever it bears below.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? [E3-31]

- **Unit economics in my own words:** Costco charges 81 million households and businesses
  $65–$130 a year for the right to shop in 914 no-frills warehouses that carry fewer than
  4,000 items each, priced at an 11.1% gross margin — roughly a third of a conventional
  retailer's markup. The merchandise operation exists to make the membership worth
  renewing: merchandise, gas, and ancillary sales of $269.9B produced only $5.1B of the
  $10.4B operating income; **the other $5.3B — half the profit pool — is the membership
  fee itself**, a deferred-revenue annuity renewed at 92.3% in the US/Canada. Volume per
  item is the engine: an average warehouse does $272M a year (1.8x Sam's Club, 3.4x
  BJ's), which buys goods cheaper per unit than anyone, which keeps the price gap, which
  keeps the renewal. Suppliers finance the inventory (payables $19.8B vs inventories
  $18.1B — "We often sell inventory before we are required to pay for it").
- **The scarce input the business controls:** the largest paid-membership base in retail
  (81.0M paid, 145.2M cardholders) and the per-warehouse volume it generates — scale per
  SKU that no attacker can replicate without first having the members, whom it cannot get
  without first having the prices. The flywheel is the scarce input.
- **Ten years:** the format is unchanged in its essentials since 1983 and the model
  survived three CEO transitions; members aged into e-commerce without leaving (e-comm
  comps +16%, digitally-enabled sales ~10% of total). The honest residual — substitution
  by delivery-first retail — is named and carried to Q4 as the slow death and to Q6 as
  the monitoring question. The money-making is intelligible today and its fundamentals
  should look broadly the same in ten years.
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? [E3-03]

- Needed or desired **[x]** (81M households pay in advance for access; paid members +6.3%
  in FY2025, +4.1% y/y at Q3 FY2026) · no close substitute **[x]** (see row — nobody else
  delivers the price gap; the two US peers trail on every same-metric row) · not
  price-regulated **[x]**.
- **Must the moat be continuously rebuilt? [E4-04]** No — it must be continuously
  *defended*, which [E5-23] prescribes for every moat. The basis (scale per warehouse →
  lowest price → renewal) is the *same* advantage defended every day, not a depleting
  asset periodically replaced. The daily-discipline character of that defence is recorded
  as the Q3 weight case, where it belongs. **Does success depend on a great manager?**
  The Mayo test [E4-23]: no single surgeon. Three CEO transitions (Sinegal → Jelinek
  2012, Jelinek → Vachris January 2024) with no visible strategy break; the FY2025 10-K
  under the new CEO reads like every prior one. The dependence is on an institutional
  culture of cost discipline — monitored at Q6 under the ABCs [E5-45] — not on a person.
- **Primary moat metric, filing-sourced, and its trend:** membership economics.
  Paid members 71.0M → 76.2M → 81.0M (FY2023→25) → 82.9M (Q3 FY2026); membership fee
  income $4,580M → $4,828M → $5,323M, +12.7% YTD FY2026; renewal 92.3% US/Canada, 89.8%
  worldwide — **held through a fee increase** (92.9%/90.5% at FY2024, the drift attributed
  by the filing to online-sold membership mix). Warehouse productivity $272M average and
  rising every cohort year (Item 5 graph). Trend: **widening**.
- **The units monitor [E4-55]:** the physical series here is members and visits, not
  dollars — paid members +6.3%, shopping frequency +5% in FY2025 (comps are
  frequency-led, not ticket-led). The honest series confirms the dollar series.
- **The dominance class [E2-53] / second question as a number [E3-46]:** ROE ~31% on a
  net-cash balance sheet (series at Q3); the position, once built, carries the economics.
- **The two-characteristic test [E2-44]:** (1) can it raise prices with demand flat? The
  *fee*: yes, demonstrated — Sept 2024 increase ($60→$65 base, $120→$130 executive),
  renewal held at 92%+, no member-growth stall; the [E4-37] no-agony test passes (the fee
  rise was routine, disclosed, and quantified at ~40% of FY2025 fee-income growth).
  (2) dollar volume growth with only minor capital? Half-and-half: fee revenue grows
  nearly capital-free and working capital is supplier-financed, but warehouse growth
  consumes real capex — which is why Q4 classes this GOOD rather than great.
- **Untapped pricing power [E3-33]: present, and deliberately unspent.** The filing's own
  words: *"We do not focus in the short-term on maximizing prices charged, but instead
  seek to maintain … 'pricing authority' — consistently providing the most competitive
  values."* An 11.1% gross margin where conventional retail runs 25%+ is enormous unexercised
  price room, held back on purpose to widen the moat. This is Munger's named exemplar:
  *"Extreme maximization or minimization of one or two variables. Example, Costco"*
  [E4-36]. **Scope check [E5-28]:** claiming the [E3-33] class claims near-monopoly, and
  Costco is not one — three clubs plus Amazon compete. The claim is therefore scoped
  narrowly: the *proven* untapped power is the fee (raised ~every 5–7 years, renewal
  insensitive both times it is filed, at Costco and at BJ's); the merchandise-price room
  is real but *spending it would narrow the moat* — it is the moat's funding, not free
  upside. No part of the Q5 case below rests on it.
- **The attacker's test [E2-45]:** with ample capital and skilled personnel, the attack
  requires selling at Costco's prices without Costco's volume per SKU — a decade of
  losses to build member density market by market, against an incumbent whose members
  have prepaid and whose renewal sits above 90%. The best-capitalized attacker on earth
  has run exactly this play for forty years: Sam's Club, inside Walmart, holds 601 clubs
  at 57% of Costco's per-club volume and a 2.6% segment margin. The attack has been made,
  continuously, by the strongest possible attacker, and the gap in the row has not closed.

**THE COMPETITOR ROW [E3-28]** — built and committed as `Test Runs/_research 2026-08-26/
COST competitor row (BJ-Sams).md`; same metrics, nearest filed annual windows, all three
filings primary-sourced. Summary:

| Metric | **Costco** FY2025 | BJ's FY2025 | Sam's Club US (WMT FY2026) |
|---|---|---|---|
| Membership fee income | **$5,323M** (+10%) | $499.8M (+9.5%) | $2,525M (memb.+other) |
| Renewal rate | **92.3% US/Can · 89.8% ww** | 90% | not disclosed |
| Warehouses | **914** | 263 | 601 |
| Paid members | **81.0M** | "over 8 million" | not disclosed |
| Comparable sales | **+6% (+8% ex gas/FX)** | +1.0% (+2.6% merch) | +2.9% incl fuel |
| Operating margin (net sales) | **3.85%** | 3.90% | 2.6% |
| Net sales per warehouse | **$272M** | ~$80M | ~$155M |
| Fee income per warehouse | **$5.8M** | $1.9M | $4.2M |

- Peers named: **2 of the industry's 2** US membership-warehouse competitors — the count
  is the issuer's own filed competition disclosure ("Walmart's Sam's Club and BJ's
  Wholesale Club"). Both peers' filings were pulled; neither is unavailable, so the moat
  class is **not provisional**. Two peer metrics do not exist publicly (Sam's renewal
  rate and member count — Walmart does not publish them); named as disclosure limits, and
  the moat class rests on the metrics all three do file.
- **The row's limit [E3-61]:** it shows position, not conduct — stated in the row file.
- Class: **[x] WIDE** · Direction: **widening** (members, fee income, productivity, and
  renewal all rising or holding through a price increase; [E4-32] direction outranks
  existence, and the direction is the strongest fact in the row)
- **VERDICT: [x] IN**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, declared first.**
- [x] **Daily execution [E3-38] — TICKED. Q3 is a BINARY GATE and no price compensates.**
  Costco is a retailer — the corpus's own named example of the class: *"For a retailer,
  hiring that nephew would be an express ticket to bankruptcy"* [E3-38]. And here the
  moat's basis *is* execution: the price gap exists only because costs are held down
  every day at 914 warehouses; the [E4-36] "extreme maximization" is a maximization of
  operating discipline. The honest tension is recorded: the membership annuity and
  net-cash balance sheet give this retailer more capacity to stand a stumble [E5-18] than
  HRB or a grocer — but a decade of eroded discipline erodes the price gap, and the price
  gap is the franchise. Gate declared, per the precedent set on HRB and NCLTY.
- [ ] Control [E1-16] — marketable minority position; exit exists.
- [ ] Leverage [E3-29] — the reverse: net cash $9.5B ($15,284M cash+STI vs $5,805M total
  debt).

**Honesty — binary [E5-16], filings-based, dated.** The sweep, named: 10-K FY2025 Note 10
(Item 3 incorporates it), read in full. What it contains: California wage/hour class and
PAGA actions (filed Nov 2023 / Aug 2024); the opioid MDL (Costco among many retail
pharmacy defendants, consolidations from Dec 2017); pixel-tracker privacy class actions
(Sept–Oct 2023) plus related Washington AG civil investigative demands; a Kirkland baby-
wipes PFAS labeling class action (June 2024); a DOJ False Claims Act investigation
regarding prescription-medication claims (CID received January 2023, open); an EPA FIFRA
matter settled for an immaterial amount. **None is financial dishonesty toward owners;
none alleges management self-dealing or concealment; accruals are stated as immaterial.**
Per the worked TJX precedent, product/employment/privacy matters are not the [E5-16]
binary. The open DOJ FCA investigation is carried as a Q6 watch item under [E5-22] —
penalty size will not be the test; *acting on what they learn* will be. Worded per the
absence-claim rule: **no disqualifier found** — not "none exists."

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E2-52, E3-50, E2-57, E3-53].**
- [ ] weak accounting — not fired. SBC expensed in full ($860M, cash-flow statement); no
  fanciful pension assumption possible — retirement plans are 401(k)/defined-contribution,
  with the only defined-benefit plans (certain Other International subsidiaries) stated
  "immaterial" (Note 1, Retirement Plans); LIFO election disclosed with the charge
  quantified ($142M, FY2025) and consistently applied.
- [ ] unintelligible footnotes — not fired. The notes are short and unusually legible;
  the deferred-fee, member-reward, and renewal-rate mechanics are each explained.
- [ ] trumpeted projections [E4-22] — **not fired, and the contrast is the finding.**
  Costco issues **no earnings or revenue guidance at all**. The only forward numbers in
  the 10-K are a capex plan ($6.0–6.5B for FY2026) and warehouse openings ("up to 35").
  It publishes *monthly sales actuals* instead — outturn before narrative. The risk
  factors even state, candidly: *"We believe that the price of our stock currently
  reflects high market expectations for our future operating results"* — a management
  telling owners the quote is optimistic is the opposite pole from [E3-50]
  stock-price-targeting.
- [ ] serial share issuance [E5-15] — not fired. Diluted shares 444.2M (FY2008) → 444.8M
  (FY2025): flat for eighteen years; buybacks retire RSU issuance.
- [ ] EBITDA / adjusted-earnings promotion [E4-29] — not fired: **zero occurrences of
  "EBITDA" in the entire 10-K** (checked mechanically). No adjusted-EPS bridge exists.
  (BJ's, same industry, leads its summary table with Adjusted EBITDA — the practice is a
  choice, not an industry necessity.)
- [ ] filed-figure tells [E4-30] — not fired as a pair. Reported growth is steady but its
  mechanism is externally visible (members, fees, monthly sales); cash taxes paid are
  **rising** as a share of pretax (24.9% → 19.6% → 22.9% → 24.7% → 26.3% → 23.8% → 27.0%,
  FY2019→25) — the tell points the honest way.
- [ ] metric-switching [E2-49] — not fired. Comps, renewal-rate, and membership
  definitions are stable across the filed decade; the 53-week adjustment was disclosed
  and applied, not used.
- [ ] dividends funded by issuance [E2-52] — not fired: no share issuance; regular
  dividend $2,183M against $13,335M OCF. **Noted for the record:** the December 2012
  special dividend was substantially debt-funded (long-term debt stepped $1.4B → $5.0B in
  FY2013); leverage stayed under ~0.5x OCF and later specials (FY2015/17/21/24, the last
  $6.7B at $15/sh) were paid from cash. A one-time structure choice, read and recorded,
  not the [E2-52] pattern (no equity replaced the capital).
- [ ] except-for [E2-57] — not fired. Gas-deflation and FX effects are quantified line by
  line and labelled "supplemental … not a substitute for" GAAP — all nine innings counted.
- [ ] restructuring [E3-53] — none in the filed years.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, without
undue leverage or gimmickry — balance sheet first [E5-27], then the income series.
- Balance sheet, FY2016→FY2025 (10-K series): equity $12.3B → $29.2B with three visible
  drawdowns (FY2017, FY2021, FY2024) — each a **special dividend**, not a loss; cash+STI
  $4.7B → $15.3B; long-term debt flat at $5–6.5B; payables ≥ inventories in every year
  (109% coverage at FY2025). Nothing hides here.
- ROE series (NI ÷ average equity, XBRL from the 10-K series): FY2016→25:
  **20.3%, 22.9%, 25.9%, 25.5%, 23.3%, 27.2%, 30.2%, 27.5%, 30.3%, 30.7%** — rising for a
  decade while leverage *fell* to net cash, so no [E2-47] carve-out bites. Honesty note in
  the flattering direction: the special dividends thin the denominator; even granting
  that, ~31% on a net-cash book passes richly.
- **The half-owner test [E2-26]: passes.** What a half-owner needs is here: renewal rates
  with their unflattering methodology and mix-drift named twice; the fee increase's
  contribution quantified (≈40% of FY2025 fee growth; 25%/35% in Q3/YTD FY2026); member
  counts by tier; warehouse economics by cohort year; gas/FX effects at every line; the
  LIFO charge in dollars; monthly sales published all year. The candor is above any
  retailer this project has run.

**The institutional imperative [E2-30]** — scored, all four:
- [ ] resists change in current direction — the direction has been held for forty years,
  but as doctrine, not drift: e-commerce and digital membership were adopted (e-comm
  comps +16%, digitally-enabled ~10% of sales). No finding.
- [ ] projects/acquisitions soak up available funds — **the anti-pattern**: no material
  M&A in the filed decade; surplus cash is *returned* (five special dividends since
  2012) rather than empire-built. Not fired.
- [ ] staff studies for the leader's craving — not observable from filings; no finding.
- [ ] peer imitation — the reverse: no guidance while peers guide, no adjusted metrics
  while the peer leads with them, wages deliberately above market ("our philosophy is
  not to seek to minimize their wages and benefits"). Not fired.

**Capital allocation — the two buyback conditions [E5-08, E4-31]:**
- (1) ample funds: **yes** — net cash $9.5B, OCF $13.3B.
- (2) material discount to conservative IV: **no.** FY2025 repurchases: 943,000 shares at
  an average **$957.66** (~$903M) — a price this run's Q5 places far above the
  conservative value range and roughly 53x that year's EPS. → **CAPITAL-ALLOCATION
  FLAG**, stated with the humility clause [E4-13]: management knows this business far
  better than I do, and "many CEOs never stop believing their stock is cheap" [E5-08].
  Two mitigants recorded: the program is small (≈7% of owner earnings, sized to offset
  RSU dilution — share count flat, not shrinking) and the board's main
  return-of-capital tool has been the special dividend, which prices nothing. **The flag
  binds position size, never the discount rate** — moot here (no position), carried to Q6.
- Retention test [E3-54]: retained capital compounds — incremental NI ÷ incremental
  equity FY2021→25 ≈ $3.1B ÷ $11.1B ≈ **28%** on the added deposits. Passes.
- Guidance-vs-outturn [E3-48], run on the only forward numbers that exist: FY2025 10-K
  planned "up to 35" FY2026 openings; the Q3 FY2026 10-Q now shows 16 opened + 13 planned
  = 29. A shortfall against an "up to" ceiling — logged as this year's outturn entry, to
  be scored again at the FY2026 10-K.

**THE GUARDRAIL:**
- [x] Nothing in this Q3 promotes the name; the franchise, not the manager, is the thesis
  [E2-37, E2-38, E3-39].
- [x] Key-person dependence was tested at Q2 ([E4-23]) and found absent (three CEO
  transitions, no strategy break); the *culture* dependence is recorded there and
  monitored at Q6 [E5-45], not read here as a compliment to any person.
- [x] No excisable-cancer case is argued; the manager is not the plan [E2-35, E2-36].

- **VERDICT: [x] IN** — gate passed: no disqualifier found; one live flag (buyback price,
  E5-08 condition 2) and one watch item (DOJ FCA investigation, [E5-22]). *This is the
  absence of found disqualifiers, not a finding that the managers are honest [E5-17].
  IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number [E2-23]
Convention applied: multi-year mean of (OCF − SBC) − (c), capex band displayed, both
windows shown [E2-42, E4-25].

- Owner earnings by year (USD M, tools arithmetic against the filed statements):

  | FY end | weeks | OCF | SBC | D&A | capex | NI | OE lo | OE hi |
  |---|---|---|---|---|---|---|---|---|
  | 2021-08-29 | 52 | 8,958 | 665 | 1,781 | 3,588 | 5,007 | 4,705 | 6,512 |
  | 2022-08-28 | 52 | 7,392 | 724 | 1,900 | 3,891 | 5,844 | 2,777 | 4,768 |
  | 2023-09-03 | **53** | 11,068 | 774 | 2,077 | 4,323 | 6,292 | 5,971 | 8,217 |
  | 2024-09-01 | 52 | 11,339 | 818 | 2,237 | 4,710 | 7,367 | 5,811 | 8,284 |
  | 2025-08-31 | 52 | 13,335 | 860 | 2,426 | 5,498 | 8,099 | 6,977 | 10,049 |

- **Long-window mean** (5-yr, FY2021–25, the corpus default [E2-42]): **$5,248M .. $7,566M**
- **Short-window mean** (3-yr, FY2023–25): **$6,253M .. $8,850M**
- **Spread, conservative end: +19.2%** (3-yr above 5-yr) — above the 15% display
  threshold; **the spread is part of the range [E4-25]**, carried, not resolved.
- Distorted years, named [E5-11]: **FY2022** (the industry-wide inventory glut: a ~$4.1B
  working-capital absorption took OCF to $7,392M below net income — the only such year in
  the filed decade) and **FY2023** (53 weeks, ~+2% extra-week revenue/OCF; and the FY2022
  inventory swing partly reversing through it). The two distortions point in opposite
  directions across the 5-year mean; the OCF convention nets both from one audited line.
- **Combined range (window spread × capex band): $5.2B to $8.9B.** Wide (1.7x end to
  end) — but **the verdict does not change anywhere inside it** (every point yields
  1.25%–2.10% on the market cap, far below both the sovereign and the floor), so a
  conclusion can be reached and no [E4-25] close is forced.
- **Maintenance capex — the DISCLOSED JUDGMENT.** This is the [E2-41] 95% class, not the
  [E5-20] capital-intensive exception: nothing in the filing says depreciation
  understates renewal; repairs and maintenance are expensed as incurred (Note 1); land
  ($10.3B, undepreciated) does not wear out. But the D&A end is not taken raw either:
  Costco added 24–30 net new warehouses a year (growth capex), while remodels,
  refurbishments, logistics, and IT renewal are capitalized and sit above D&A charged on
  decades-old cost bases [E4-47 — construction-cost inflation makes old-dollar D&A light].
  **Judgment, disclosed: (c) ≈ D&A + $1.0–1.5B ≈ $3.4–3.9B on the FY2025 base — the
  upper-middle of the band, nearer the D&A end.** Judged owner earnings: **5-yr ≈
  $5.7–6.2B; 3-yr ≈ $7.1–7.6B.** The full computed band is carried everywhere below; the
  verdict is unchanged across it, so no UNKNOWABLE arises.
- Working-capital increment [E2-23]: the source's own LIFO carve-out applies literally —
  U.S. inventories are on LIFO, and payables exceed inventories, so unit growth *releases*
  working capital rather than consuming it; the OCF line nets it in any case.
- Stock compensation subtracted in full [E5-06]: yes ($860M FY2025; RSUs, no options —
  the reported charge is the floor of the subtraction [E3-70] and no repricing exists to
  hide behind).
- Look-through [E3-04]: no material equity-method or unconsolidated stakes. Not applicable.

### Great, good, or gruesome? [E4-20]
- **[x] GOOD — at the upper boundary.** The savings account pays an attractive and rising
  rate on added deposits: ~31% ROE, ~28% on the *incremental* equity retained FY2021→25 —
  far above the [E5-40] calibration (12% on retained utility capital = "quite
  satisfactory"). It is not the *great* class only because growth consumes real capital
  ($5.5B capex, 24–30 new boxes a year); the membership-fee annuity inside it is the
  near-great component (fee income grows nearly capital-free). Gruesome is excluded on
  every row of the table. Good **passes** Q4 [E4-43]; it simply ranks below great at Q5.

### Staying power — score all three [E5-11]
- (1) large and reliable stream of earnings: **pass.** Net income positive in every year
  of the 18-year XBRL series (FY2008 $1,283M → FY2025 $8,099M) with only two dips —
  FY2009 (−15%) and FY2016 (−1%); half the profit pool is deferred-fee annuity renewed
  at 92%+.
- (2) massive liquid assets: **pass.** $15,284M cash + short-term investments vs $5,805M
  total debt: **net cash ≈ $9.5B**, invested per policy in Treasuries/agency paper.
- (3) no significant near-term cash requirements: **pass.** Debt maturities: FY2026 $75M,
  FY2027 $2,250M, FY2028 zero — the 2027 tower alone is covered ~6.8x by cash on hand;
  regular dividend $2.2B covered ~6x by OCF; the buyback and specials are discretionary;
  no commercial paper reliance ("short-term borrowings … immaterial"); the kindness of
  strangers is not required [E5-39].
- Leverage, named and quantified [E4-16, E3-29] — no ratio ceiling exists in this
  framework and none is used: gross debt $5,805M = 0.44x OCF, fixed-rate, semi-annual
  coupons; interest expense $154M vs OCF net of full capex $7.8B → **coverage ≈ 50x by
  the [E2-54] test** (all interest, out of current cash flow, net of ample capex — passes
  without strain). Terms read [E3-52]: deferred membership fees ($2,854M) and accrued
  member rewards ($2,677M) are covenant-free, customer-prepaid liabilities — the benign
  animal; the Senior Notes carry no maintenance covenants disclosed.

### Name the specific ways THIS business dies [E2-27, E3-24] — exposure, not experience [E4-40]
The iron prescription [E4-51], stated as the bears would state it, then quantified:

1. **The renewal is the whole company (the slow death).** Membership fees are $5,323M of
   $10,818M pretax income — **49%** — and the 38.7M Executive members drive 73.6% of
   worldwide net sales. The entire merchandising machine earns a 3.85% operating margin
   whose purpose is to protect one annually-renewed $65 decision by 83 million
   households. The bear mechanism: delivery-first retail (Amazon, quick commerce,
   Walmart's price investment) thins the *perceived* value gap before it ever shows in
   comps; renewal drifts 92% → high-80s; member growth (+6.3%) stalls; the fee annuity
   flattens; and the P&L has no second engine. Quantified per [E3-24]: a sustained
   5-point renewal decline removes ~4M renewals a year — roughly the whole current member
   *growth* — turning fee income flat-to-declining (a ~$500M+/yr swing against the growth
   path) and unwinding the multiple long before solvency is touched. Filed evidence
   against it *today*: renewal 92.2/89.7 at Q3 FY2026 *through* a fee increase; frequency
   +5%; e-comm comps +16–21%. Likelihood, in the corpus vocabulary: **a low-level
   possibility** near-term; the permanently monitored question at Q6.
2. **The labor-cost squeeze (the margin death).** 341,000 employees; average U.S. hourly
   wage ≈ $32 held deliberately above market; SG&A 9.25% of sales against a 3.85%
   operating margin. A structural +100bp SG&A shock (wage legislation, unionization
   beyond today's ~5%, healthcare inflation — all named in the filing) is ≈ $2.7B ≈ 25%
   of pretax income. **A real possibility** across a decade; survivable without leverage
   strain (net cash), and partially self-correcting through the fee lever — but it is the
   named repricer of the equity.
3. **A Kirkland/food-safety trust event (the fast reputational wound).** The private
   label is "a growing portion of our overall sales" (share not quantified in the
   filing) and carries the membership's trust; the baby-wipes PFAS suit shows the vector.
   A sustained trust break would hit renewal and margin together. **A low-level
   possibility**; severity capped by the diversity of the assortment.
4. **Culture decay under scale [E5-45] (the ABCs).** The moat's defence is daily expense
   discipline by 341,000 people; arrogance, bureaucracy and complacency are how "even the
   strongest of companies can falter." No filed evidence today (the wage philosophy, the
   no-guidance stance, and flat share count argue the culture holds). **A low-level
   possibility per decade; the Q3 gate and Q6 tripwires exist for it.**
5. **The shareholder's death that is not the company's: the multiple.** At ~52x earnings
   / a 1.3–2.1% owner-earnings yield, a de-rating to 25–30x over a decade costs ≈ −6 to
   −7%/yr — more than the business's own growth can replace. This is Q5's finding, named
   here because the bears are right about it: **the price, not the business, is where the
   risk of permanent capital loss lives.**
- **VERDICT: [x] IN** — the business survives every named mechanism; none touches
  solvency at any plausible severity.

---
⛔ Q1–Q4 each show IN. Q5 opens legitimately.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28].** Honest pre-tax expectancy at $945.47:
- Owner-earnings yield: **1.25%–1.80%** (5-yr band), **1.49%–2.10%** (3-yr band); at the
  judged (c): **≈1.4% (5-yr) / ≈1.7–1.8% (3-yr)**. All under half the sovereign before a
  cent of growth.
- Expectancy = yield + honest growth. The record is real and long: revenue +9.8%/yr
  (FY2016→25), net income +13.0%/yr (FY2015→25), +11.4%/yr over seventeen years —
  **Costco is one of the rare [E4-35] compounders, and that is said plainly.** But the
  arithmetic at this price is merciless: the run.py engine (10-yr fade to a 2.5%
  terminal, discounted at the bare sovereign — no risk premium in the rate [E3-42])
  returns a pre-tax IRR of **4.1%–5.5%** across the *entire* OE band and growth starts
  up to 10%. Even the most generous defensible stack — 3-yr window, (c) at bare D&A
  ($8,850M), **10%** year-1 growth — pays **5.5%** at this price. The only route to 10%
  is holding ≥8% growth *in perpetuity with no fade and the ~52x multiple held forever*,
  which [E4-44] names as the Tinker Bell approach and [E4-35] prices at longer than
  1-in-20 odds even among the best businesses.
- **The floor fails — not marginally at the honest center. The name is not ranked; it is
  quit on at this price.** The floor does not move with the sovereign [E4-28].

**One book. Owner earnings against the bond.** The DCF ran as an engine only; it casts no
vote [E3-34].

**1. THE YIELD**
- $5,248–8,850M ÷ $420,545M = **1.25% .. 2.10%** · sovereign **5.22%**

**2. WHAT THE PRICE ALREADY ASSUMES**
- run.py engine (10-yr fade to 2.5% terminal, discounted at the bare 5.22% sovereign):
  year-1 OE growth of **19.8%** (5-yr conservative end), **11.2%** (5-yr D&A end),
  **15.7%** (3-yr conservative end), **7.7%** (3-yr D&A end) is needed to reproduce the
  $420.5B market cap. At the [E3-13]-spread engine rate (8.22%): 26.6%–40.6%.
- what the business has actually done: revenue **+9.8%/yr**, NI **+13.0%/yr** (ten
  years). On every base except the single most generous corner, the price assumes more
  growth than the business — one of the best compounders alive — has actually delivered.
- The ceiling stated [E2-63, E4-44]: value cannot outgrow earnings over the long term;
  the upside is bounded by earnings growth from a 1.3–2.1% starting yield, with no
  multiple term available above ~52x.

**3. WHAT YOU ARE PAID**
- run.py engine (growth fading to 2.5%, IRR at the current price): 3% start →
  **−1.41 .. −0.83** points over the sovereign; 7% start → **−1.14 .. −0.46**; 10% start
  on the most generous base → **+0.29**. Bond-minus pay for equity risk, on nearly every
  honest input.

**Certainty:** not priced in any rate [E3-42]. The template's certainty-spread block is
superseded by v4.1; the document governs. Certainty was spent at Q1 and is spent once in
the bar below.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:**
- conservative: **≈$230–330/sh** (the 5-yr mean-OE band capitalized at the bare
  sovereign, zero growth)
- judged middle: **≈$300/sh** zero-growth; the judged-(c) OE at the sovereign
- generous: **≈$1,050–1,190/sh** (3-yr D&A-end OE $8.85B, 10–13% year-1 growth fading to
  2.5%, discounted at the bare sovereign — zero conservatism spent anywhere: most
  generous window, most generous (c), the business's own best-decade growth, no risk
  premium)
- **current price: $945.47 — roughly 3–4x the conservative case; inside the full range,
  below its zero-conservatism top.**

**WHICH BAR: [x] Screamer test [E4-01]** — outcome: **price inside the range → no useful
conclusion from the bar — move on.** That middle outcome is a finished answer, and it
never overrides the floor, which already closed entry above. No margin was added on top.
**Windage count: one** (the conservative end of the OE band; the generous end
deliberately spends zero, which is what makes the floor finding robust).

- **VERDICT: evidence IN — and BELOW THE FLOOR [E4-28]: NOT RANKED. Entry is closed at
  this price.** This is a price verdict, not a business verdict; it re-opens on the Q6
  bands below.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*No position exists; there is no [E2-28] hold read to run. Everything below is
pre-committed now, prior to any act [E1-02], and converts to watch-list items.*

**Thesis-confirming metrics** (the franchise is intact while):
- US/Canada renewal ≥ 92%, worldwide ≥ 89% (10-K/10-Q, each filing)
- paid members growing ≥ 4%/yr; Executive penetration rising (38.7M / 47.8% of paid at
  FY2025)
- comps frequency-led and positive ex-gas/FX; e-comm comps positive
- membership fee income growing high-single-digit or better ($5,323M FY2025; +12.7% YTD
  FY2026)
- the next fee increase (~2029–31 on the historical 5–7 year cadence) landing with
  renewal flat — the [E4-37] no-agony test, live

**Thesis-breaking metrics and thresholds** (a moat downgrade forming [E4-17, E3-30] —
slow to conclude, fast once concluded [E2-40]):
- US/Canada renewal **below 90% in two consecutive annual filings** (not one online-mix
  wobble)
- paid-member growth **below 2%/yr**, or fee income declining year over year
- frequency comps negative ex-gas/FX for a full fiscal year while e-comm also decelerates
  (the substitution signature)
- Executive penetration falling two filings running
- a [E5-45] ABCs signature: guidance culture appearing, adjusted metrics appearing,
  wage-philosophy language weakening, or a material acquisition outside the club model
  (loss of focus [E3-40] — and the corpus's remedy is exit, not engagement [E4-24])
- any integrity matter public; on the open DOJ FCA investigation, the [E5-22] test is
  whether they acted when they learned, not the fine

**Entry bands — the price at which this file re-opens** (computed from this run's OE;
both bands grow with owner earnings and are recomputed at each 10-K):
- **Full re-run triggers below roughly $600–650** (3-yr judged OE yield ≈ 2.5–3.0%; there
  the honest expectancy — yield plus the growth the business has *actually done*, faded —
  reaches ~10% [E4-28] and the floor comes into play rather than closing the file on
  arrival)
- **The name would rank near roughly $250–330** (the judged-OE yield reaches the 5.22%
  sovereign across the two windows; Bar-1 arithmetic then applies with margin)
- These are review triggers, not auto-executions; all six gates re-run at entry.
- **tools/alerts.json candidates (listed only — NOT edited, per instruction):**
  COST price < 650; COST price < 330; US/Can renewal < 90.0 (any filing); paid-member
  growth < 2% y/y (any 10-K); membership fee income down y/y (any 10-K); FY2026 10-K
  filed (re-run the OE table).

**Next catalyst dates:**
- FY2026 fourth-quarter and full-year results + September sales release: **late September
  2026**
- **FY2026 10-K: ~early-to-mid October 2026** (FY ended 2026-08-30; prior-year filing came
  38 days after year-end) — refresh the OE table, the renewal print, and both entry bands
- monthly sales releases (first week of each month) — the traffic/frequency series
- January 2027: the $4.0B buyback authorization expires; the renewal terms are an [E5-08]
  condition-2 data point

**Position size — a judgment, stated [E3-45 direction]:** zero. The framework's answer at
this price is no entry (Q5 floor), and the E5-08 flag would bind size if entry were ever
taken near the current multiple. Capital goes to rank #1, and at a 1.3–2.1% yield against
a 5.22% bond this name does not rank at all.

- **VERDICT: [x] IN** — the question "what would prove me wrong, and when would I act" is
  answered with pre-committed, filing-sourced yardsticks.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped; Q5 opened only after Q1–Q4 showed IN
- [x] No question marked IN carries an "unverified" or "provisional" caveat (the two
  non-disclosed Sam's Club metrics are named as disclosure limits; the moat class rests
  on filed rows only)
- [x] No UNRESEARCHED verdicts issued — every gate closed on documents in hand (FRED's
  block was routed around via the issuing authority itself, a higher rung)
- [x] No UNKNOWABLE verdicts issued (the OE band is wide but the verdict is invariant
  across it, so [E4-25] does not force a close)
- [x] Step 0: the filing was read; accession 0000909832-25-000101 (10-K FY2025), plus
  10-Q accession 0000909832-26-000051; OCF $13,335M and net sales $269,912M cross-checked
  against the filed statement text, not tags
- [x] Owner earnings on multi-year means; both windows stated (5-yr default [E2-42], 3-yr
  shown); the +19.2% window spread carried as part of the range [E4-25]; capex band
  displayed with (c) disclosed as a judgment (D&A + $1.0–1.5B, reasons cited from Note 1
  and the capex-plan text); 53-week FY2023 flagged
- [x] Competitor row filled (separate committed file, 2 of 2 peers, filing-sourced); moat
  class not provisional
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury
  daily yield curve), dated 2026-08-28
- [x] Value stated as a round-number range ($230–330 conservative; $1,050–1,190 generous)
- [x] One bar (screamer); windage count stated: one
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git

## REGISTER
- Verdict: **[x] IN (about the business) — and the price fails the [E4-28] floor; entry
  closed. No position exists; Q6 bands armed as watch-list items.**
- One line: **The strongest membership franchise in retail — renewal held at 92% through
  a fee increase, warehouse productivity 1.8x Sam's and 3.4x BJ's, half the profit pool a
  prepaid annuity, ROE rising for a decade on a net-cash book — priced at a 1.3–2.1%
  owner-earnings yield against a 5.22% bond, where the honest pre-tax expectancy is
  4–5.5% and even management says the quote "reflects high market expectations." A
  wonderful business, quit on at the price; re-run below roughly $600–650.**
- Biggest single concern: **the multiple** — at ~52x earnings the price already assumes
  more growth than this rare compounder has ever delivered, and a de-rating to an
  ordinary premium multiple costs more per year than the business earns; second, and far
  behind, the fee-dependence concentration (49% of pretax from one annually renewed $65
  decision), which is also the moat's own measure.
