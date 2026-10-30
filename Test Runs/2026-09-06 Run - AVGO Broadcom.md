# Company Run — Broadcom Inc. (AVGO) — 2026-09-06
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  fetched direct from home.treasury.gov (the issuing authority; not FRED)**. 2026-09-04 is
  the most recent published date; 09-05 was not yet posted at the time of the strike.
- FX: none. Broadcom reports and earns in USD. No ADR ratio.

**Shares — Stage 0, BY HAND off the cover (not tagged data):**
> *"As of May 29, 2026, there were **4,757,580,198** shares of our common stock outstanding."*
> — Q2 FY2026 10-Q cover page, accession **0001730168-26-000054**, doc `avgo-20260503.htm`

- **Single class.** Common stock, $0.001 par, 29,000M authorised, one line on the balance
  sheet. Preferred: *"100 shares authorized; none issued and outstanding."* No super-voting
  class, no A/B structure.
- **SPLIT GUARD — 10-for-1 split, July 2024, VERIFIED.** The FY2025 balance sheet shows
  4,741M shares issued and outstanding at 2025-11-02 and 4,686M at 2024-11-03, and the
  FY2023 comparative in the same equity statement reads 4,139M at 2023-10-29. Broadcom's
  pre-split count was ~464M. **Every vintage in the window is stated on the post-split
  scale, so the count and the per-share figures are on the same basis** (FY2023 EPS $3.39
  basic × 4,149M weighted shares = $14,065M ≈ the $14,082M net income — the split guard
  cross-check passes to 0.1%).

**Price** (aggregator, flagged per operator rule 5 — live quotes only):
- **$357.90**, close of **2026-09-04**, Yahoo Finance. Five-day tape 370.34 / 369.68 /
  367.24 / 357.16 / 357.90.

**MARKET CAPITALISATION = 4,757,580,198 × $357.90 = $1,702,738M — $1.70 TRILLION.**
*(The 2026-09-04 FLOOR SCREEN carried $1,754,548M on an earlier quote. The hand figure governs.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **FY2025 10-K · period 2025-11-02 · filed 2025-12-18 · accession 0001730168-25-000121**
  (`avgo-20251102.htm`) — the document of record.
- Also read: **Q2 FY2026 10-Q**, acc. 0001730168-26-000054 (period 2026-05-03, filed
  2026-06-09 — *the Q3 FY2026 10-Q does not yet exist; on the FY2025 cadence it is due
  ~2026-09-09, three days after this run*); **FY2023 10-K**, acc. 0001730168-23-000096 (the
  pre-VMware perimeter); FY2024 10-K acc. 0001730168-24-000139; VMware's own FY2021–FY2023
  10-Ks (CIK 1124610) — see `_research 2026-09-06 AVGO/01`.
- **Figure cross-checked against the filed statement:** the XBRL `ShareBasedCompensation`
  of $7,568M for FY2025 was checked against the filed CONSOLIDATED STATEMENTS OF CASH FLOWS
  (p.50) — agrees. It does **not** agree with the equity statement in the same filing, which
  shows **$7,570M** ($5,747M vs $5,741M in FY2024). A $2M presentation difference, recorded
  because it is the likely source of the small residual against the screen row below.
- **Balance-sheet integrity check [E5-32]:** assets 171,092 − liabilities 89,800 = 81,292 =
  the stated total stockholders' equity, exactly.

---
## THE PERIMETER — READ THIS BEFORE ANY NUMBER BELOW

**Broadcom is a serial acquirer and the largest deal in the queue's history sits inside
every owner-earnings window.** VMware closed **2023-11-22**, three weeks into fiscal 2024.
So **FY2023 and earlier are one company; FY2024 and FY2025 are a different one.** This is
the DKS/Foot Locker shape at roughly 27× the size.

**The consideration, filed (FY2025 10-K, Note 3):**

| | $M |
|---|---|
| **Total purchase consideration** | **86,290** |
| less cash acquired | (6,642) |
| **Net of cash acquired** | **79,648** |
| — Goodwill | 54,206 |
| — Intangible assets | 45,572 |
| — **Property, plant and equipment acquired** | **531** |

**$100bn of goodwill-plus-intangibles was bought, and $531M of physical plant came with it.**
That single line is the whole of the (c) question, and it is answered below.

**The intangible schedule and its lives, verbatim from the same note:**

| Class | Fair value $M | Weighted-average life |
|---|---|---|
| Developed technology | 24,156 | **8 years** |
| Customer contracts and related relationships | 15,239 | **8 years** |
| Trade name ("VMware") | 1,205 | 14 years |
| Off-market component of customer contracts | 242 | 2 years |
| **Total finite-lived** | **40,842** | |
| IPR&D (indefinite until released) | 4,730 | n/a |
| **Total** | **45,572** | |

Straight-lined, that schedule alone throws off **~$5,131M of amortisation a year**, against
**$623M of total company capital expenditure**.

### THE PRO FORMA IS FILED, AND IT IS THE FINDING

The DKS standing instruction says: build owner earnings pro forma, or state why not.
**Broadcom filed the combined table itself** (FY2025 10-K, Note 3, "Unaudited Pro Forma
Information", *"as if VMware had been acquired as of the beginning of fiscal year 2023"*):

| | FY2024 | FY2023 |
|---|---|---|
| **Pro forma net revenue** | **52,188** | **48,227** |
| **Pro forma net income** | **6,473** | **8,215** |

**On a like-for-like combined basis, revenue grew 8.2% and net income FELL 21.2%.** The
headline "+44% revenue" from FY2023 ($35,819M) to FY2024 ($51,574M) is the acquisition,
not the business. FY2025 actual revenue of $63,887M against the FY2024 pro forma of
$52,188M is **+22.4%** — that is the honest growth number for the combined perimeter's
first clean year, and it is a real number.

**Owner earnings pro forma — built, and its limit stated.** VMware's own standalone series
(from its filed 10-Ks, CIK 1124610; full working in
`_research 2026-09-06 AVGO/01 - VMware perimeter and purchase accounting.md`):

| VMware standalone, $M | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Net cash provided by operating activities | 4,409 | 4,357 | 4,300 |
| less stock-based compensation | (1,122) | (1,075) | (1,290) |
| less additions to property and equipment | (329) | (386) | (450) |
| **= Owner earnings** | **2,958** | **2,896** | **2,560** |
| Revenue | 11,767 | 12,851 | 13,350 |
| Operating margin | 20.3% | 18.6% | **15.1%** |

**So the pro-forma pre-deal combined owner earnings are constructible for FY2021–FY2023 and
they are: 14,575 / 17,675 / 18,022** (Broadcom standalone + VMware standalone, no
elimination — VMware's revenue from Broadcom was immaterial and no inter-company line is
disclosed either side). Against Broadcom's *actual* post-deal 13,673 (FY2024) and 19,346
(FY2025).

**THE PRO-FORMA RESULT, STATED PLAINLY: on the combined perimeter, owner earnings went
18,022 (FY2023 pro forma) → 13,673 (FY2024) → 19,346 (FY2025). Two years after paying
$86.3bn, owner earnings are 7.3% above where the two companies stood together before the
deal.** $86.3bn bought $1,324M of incremental annual owner earnings on that comparison — a
**1.5% return on the purchase price** — and the FY2026 half-year (below) is where the case
for the deal actually lives.

**Two honest limits on that construction, stated rather than smoothed:**
1. **The fiscal calendars do not align.** VMware's FY2023 ended 2023-02-03 (a 53-week year);
   Broadcom's ended 2023-10-29. The combination is a sum of two different twelve-month
   periods, nine months offset. It is directionally right and it is not an audited figure.
2. **The EUC disposal.** *"On July 1, 2024, we sold the EUC business to KKR & Co. Inc. for
   cash consideration of $3.5 billion"* — held for sale at $5,206M of assets / $1,901M of
   liabilities at close, and reported in discontinued operations. So the FY2025 perimeter is
   VMware **minus** end-user computing, and the standalone VMware series above includes it.
   The pro-forma comparison is therefore, if anything, **generous to Broadcom on revenue and
   harsh on it in nothing** — I have not adjusted for it, and say so.

**And the one thing the filing refuses to give, quoted because the refusal is the finding:**
> *"It is **impracticable to determine the effect on net income attributable to VMware** as
> we immediately integrated VMware into our ongoing operations."*

Broadcom disclosed VMware's revenue for FY2024 ($12,384M) and **has never disclosed VMware's
profit, in any vintage.** That is a filed refusal, not an omission I can research away — no
document exists that would resolve it. It is recorded at Q3 as a candour item and it bounds
what the segment analysis below can claim.

**`acquisition_flag()` — run, and it does NOT fire, which is itself a tool defect.**
The 2026-09-02 MASTER RUN QUEUE row for AVGO carries an **empty `acq_note`** while CERT
(35%), HAS (34%), AATC (27%) and EFX (16%) are flagged. The reason is arithmetic: the flag
scales acquisition spend against market capitalisation, and $79.6bn against a $1.75tn cap is
4.5% — under the 15% threshold. **The largest software acquisition in history is invisible
to the guard because the acquirer is too big.** Recorded as a defect against the tool, not
against the run; the perimeter was found by reading the filing, which is what operator
rule 4 exists for.

**Contingent-liability persistence check — run, and it does not fire, for the AAPL reason.**
Note 14 "Commitments and Contingencies" carries no accrued amount for any named matter in
FY2025, FY2024 or FY2023, so there is no carried-forward balance whose persistence could be
tested. There is nothing to persist. Recorded as an absence, not a pass.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Broadcom is two businesses
stapled together by a balance sheet, and they make money in opposite ways.

**One — the semiconductor half ($36,858M of FY2025 revenue).** Broadcom designs chips and
has almost nobody else make them. It owns essentially no factories: $2,530M of property,
plant and equipment against $63,887M of revenue, and $623M of annual capital spending —
**under one percent of sales.** The economics are: spend $3.4bn a year of segment R&D on
designs, win a socket inside somebody else's product, and then collect for the life of that
product at a 57% operating margin because the customer cannot re-lay their board. The
biggest and newest slice is custom AI accelerators — Broadcom co-designs a chip with a
hyperscaler who wants an alternative to buying merchant GPUs, and sells it to them for
years. The scarce input is **the incumbency of a design win**: once a chip is inside a
switch or a phone or a rack, replacing it costs the customer a redesign cycle, not a
purchase order.

**Two — the software half ($27,029M of FY2025 revenue).** Broadcom buys mature enterprise
infrastructure software companies whose products are already installed in the world's
largest data centres — CA (2018), Symantec's enterprise business (2019), VMware (2023) —
fires much of the cost base, narrows the product line to a bundle, and raises the price to
the customers who cannot leave quickly. It then earns a **76.8% operating margin** on the
result. The scarce input here is not technology. It is **the switching cost of an installed
base**: an enterprise running its private cloud on VMware cannot move off it in a renewal
cycle, and Broadcom prices against that fact.

**So: how does Broadcom make money? It buys or wins positions that customers cannot cheaply
exit, and then charges what the exit cost is worth.** Both halves are the same idea applied
to two different kinds of lock-in. That is a simple sentence and I can write it without
using a word of the company's own vocabulary.

**Will the fundamentals look broadly the same in ten years?** This is where Q1 gets
uncomfortable and I will not paper over it. Three facts are in tension:
- The **software** half is about as predictable as enterprise businesses get. The
  mainframe software Broadcom bought with CA is still being paid for by banks. Ten years is
  a reasonable horizon for that revenue existing.
- The **semiconductor** half's largest and fastest-growing line is custom AI accelerators,
  and the filing itself says the customers *"may make and have made greater demands on us
  with regards to pricing and contractual terms, such as seeking to lease AI racks or
  systems based on our XPUs instead of purchasing."* That is a two-year-old revenue line
  growing at 65% whose customers are three or four companies with their own silicon teams.
- The **company** is a serial acquirer whose shape has changed materially three times in
  eight years. Predicting Broadcom-in-2036 requires predicting what it will buy.

**I can nonetheless describe how each dollar of today's revenue is earned, from the filed
statements, without needing to know what it buys next** — and that is what Q1 asks
**[E3-31]**. The business is not complex. What it *owns* changes; how it makes money does
not. It is not the ATLKY class (a structure I could not describe) and it is not [E4-46]'s
five-months-of-study class. I understand it.

- **The scarce input this business controls:** *the cost to the customer of leaving* — a
  board redesign on the chip side, a data-centre migration on the software side. Broadcom
  does not control a fab, a mine, a spectrum licence or a brand; it controls positions
  inside other people's products and prices against the switching cost.
- **VERDICT: [x] IN**

---
## COMPUTATION — NOT A CLEARANCE
*(operator rule 3: this arithmetic is produced before Q2–Q4 have closed. It carries no
entry language and it is not a Q5 output.)*

### THE SCREEN ROW — REPRODUCED, AND THE FOURTH SPREAD DEFECT REBUILT

Screen row, `Screens/2026-09-04 FLOOR SCREEN.csv`:
`AVGO,Broadcom Inc.,1754548,14926,16145,0.082,0.0085,0.0092,-0.044,0.0915,0.0069,0.0034`

**Reproduced by hand, from the filed cash-flow statements (OCF − SBC − capex), $M:**

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| OCF | 3,411 | 6,551 | 8,880 | 9,697 | 12,061 | 13,764 | 16,736 | 18,085 | 19,962 | **27,537** |
| SBC | 679 | 921 | 1,227 | 2,185 | 1,976 | 1,704 | 1,533 | 2,171 | 5,741 | **7,568** |
| capex | 723 | 1,069 | 635 | 432 | 463 | 443 | 424 | 452 | 548 | **623** |
| **OE** | **2,009** | **4,561** | **7,018** | **7,080** | **9,622** | **11,617** | **14,779** | **15,462** | **13,673** | **19,346** |

- screen `oe_top` **16,145** = the **3-year FY2023–25 capex-end mean**; my hand figure
  **16,160.3**. Difference **$15M**.
- screen `oe_bottom` **14,926** = the **5-year FY2021–25 capex-end mean**; my hand figure
  **14,975.4**. Difference **$49M**.
- **The row reproduces.** The residual is the $2M/$6M SBC presentation difference between the
  cash-flow statement and the equity statement noted at Step 0, compounded over the window.

**AND IT IS THE AAPL DEFECT AGAIN, IN ITS SHARPEST FORM: the row reproduces exactly and
still misleads, because BOTH of its "ends" are the same end.** The screen's
`spread` of **0.082 (8.2%)** is the gap between two *capex-end* constructions three and five
years long. It is not a capex band at all — the `DepreciationDepletionAndAmortization` tag
is **absent from Broadcom's XBRL**, so the screen never built a D&A end and had nothing to
put on the other side. And AVGO is the exact shape the brief predicted would break it:
**VMware closed inside the window and revenue stepped from $35,819M to $63,887M in two
years.**

**Rebuilt over my own windows [E4-25], both ends:**

D&A from the filed cash-flow statements — and Broadcom states the two components
**separately**, which is the whole finding:

| $M | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Amortization of intangible and right-of-use assets | 5,502 | 4,455 | 3,333 | 9,417 | **8,201** |
| **Depreciation** (physical assets) | 539 | 529 | 502 | 593 | **574** |
| **Total D&A** | 6,041 | 4,984 | 3,835 | 10,010 | **8,775** |
| OE at the **D&A end** (OCF − SBC − D&A) | 6,019 | 10,219 | 12,079 | **4,211** | **11,194** |

| Construction | window | $M | yield on $1,702,738M cap |
|---|---|---|---|
| capex end, 3-yr (FY2023–25) | 3 | **16,160** | 0.949% |
| capex end, 5-yr (FY2021–25) — **the corpus default [E2-42]** | 5 | **14,975** | 0.879% |
| capex end, 8-yr (FY2018–25) | 8 | **12,325** | 0.724% |
| capex end, 10-yr (FY2016–25) | 10 | **10,517** | 0.618% |
| D&A end, 3-yr (FY2023–25) | 3 | **9,161** | 0.538% |
| D&A end, 5-yr (FY2021–25) | 5 | **8,744** | 0.514% |
| FY2025 alone, capex end (best full year filed) | 1 | **19,346** | 1.136% |
| **TTM to 2026-05-03, capex end** *(FY2025 + H1 FY2026 − H1 FY2025)* | 1 | **23,977** | **1.408%** |
| TTM to 2026-05-03, D&A end | 1 | **16,084** | 0.945% |

**THE TRUE SPREAD IS 84.8% (8,744 → 16,160 across the multi-year constructions), NOT 8.2%.
The screen understated the width of this business's owner earnings by roughly ten times.**
`spread_caveat` fires correctly on the shape; the caveat is not the fix — rebuilding the
windows is, and it is done above.

**A wide spread is also a Q4 finding [E5-11], and the distorted years are named both ways:**
- **FY2024 is DEPRESSED and it is the acquisition**: SBC leapt from $2,171M to $5,741M
  (assumed VMware retention awards), amortisation from $3,335M to $9,417M, restructuring
  from $248M to $1,787M, and acquisition costs to $549M. Owner earnings fell $1,789M in the
  year Broadcom's revenue rose 44%.
- **FY2025 is ELEVATED, and partly for a reason that will not repeat**: the FY2025 income
  statement carries a **tax BENEFIT of $397M** against pre-tax income of $22,729M, while
  cash taxes paid were $2,589M. The deferred-tax line in the cash-flow statement swung
  −$4,008M in FY2025 against +$1,965M in FY2024, a $5,973M year-on-year swing **that does
  not touch owner earnings in either year** — which is precisely why [E2-23] refuses the
  net-income proxy. Recorded so no reader mistakes the $23,126M of net income for the
  business.
- **FY2016 is DEPRESSED**: the Avago/Broadcom Corporation merger year, operating income
  −$409M.
- **[E4-41] normalisation DOWN for luck:** the FY2025–26 AI-accelerator surge is a
  favourable exogenous break of exactly the class [E4-41] says to strip before trusting a
  mean. It is not stripped from the table above — it is named here, and the ranking below
  is run on the *unstripped, most generous* figure so the conclusion cannot be accused of
  it.

### THE (c) JUDGMENT — AND THE CVX INVERSION IS LIVE, AT THE LARGEST SCALE THE QUEUE HAS SEEN

**The brief said: do not default. Here is why the default is not merely wrong here, it is
backwards.**

At Broadcom the **D&A end is the CONSERVATIVE end and the capex end is the GENEROUS end** —
the reverse of every ordinary filer and of the way [E3-44] is usually applied. FY2025 D&A of
**$8,775M is 14.1× total capital expenditure of $623M**, because $8,062M of it is
amortisation of acquisition-related intangibles from deals whose cash left the building in
FY2024 and earlier.

**What does that amortisation renew?** The QCOM run ruled that acquired-intangible
amortisation *"renews nothing"* for a fabless licensor. Here the question has to be asked
again, because Broadcom's business model IS acquisition, and the answer is **more nuanced
and lands in the same place, for a reason that must be written down:**

1. **The physical half of (c) is settled and it is tiny.** Broadcom's own separately-stated
   depreciation is **$574M** against **$623M** of capex — a ratio of **1.09×**. Ten-year
   capex/depreciation runs close to 1. On the physical assets this is squarely the
   **[E3-44]/[E2-41] DEFAULT class**, not the **[E5-20]** railroad exception, and the filing
   supports it: buildings depreciated over 15–40 years, machinery 3–10 years, total
   long-lived assets $2,530M on $63,887M of revenue. There is no hidden physical renewal
   bill.
2. **The intangible half is a cost already paid, and the renewal it stands for is already
   inside operating cash flow.** The amortisation of VMware's developed technology is the
   unwinding of a purchase price settled in FY2024 with $25,978M of cash and $53,421M of
   stock. What actually keeps that technology current is **research and development, which
   is expensed above the OCF line** — $10,977M consolidated in FY2025, 17.2% of revenue. To
   deduct $8,062M of amortisation *as well* would charge the renewal twice: once as R&D in
   operating cash flow, once as (c). That is the QCOM shape and the answer is the same.
3. **But there is a real version of the objection and it must be stated, because it is the
   [E2-23] question:** if Broadcom's *unit volume and long-term competitive position*
   require it to keep buying franchises — because the ones it owns are being harvested
   rather than renewed — then acquisition spending IS maintenance capital and (c) is
   enormous. **The evidence for that reading is the R&D trend inside the software segment,
   and it is not weak**: software-segment R&D went **$2,707M (FY2024) → $2,550M (FY2025)**
   while software revenue rose 25.8%, i.e. from 12.6% to **9.4% of segment revenue**, and
   fell again to $1,178M in H1 FY2026 from $1,317M. **VMware standalone spent far more than
   that on a business half the size.** This is [E2-60]'s third dimension — maintenance
   includes *"its long-term competitive position"* — and it is the strongest live argument
   for a (c) above capex.

**(c) JUDGED — a disclosed judgment, per [E2-23] "must be a guess":** **(c) = total capital
expenditure, ~$623M**, i.e. the generous end, **because the physical ratio is 1.09× and the
technology renewal is already borne inside OCF as R&D.** The D&A end is carried in the range
above but it is the **pessimistic** end here, and the run states the direction explicitly so
that no later reader inverts it. **The [E2-60] R&D-intensity concern is not priced into (c);
it is carried to Q2 as a moat-direction finding and to Q4 as the named way this dies**,
because it is a question about whether the software franchise is being *harvested*, not
about how much plant costs to replace.

**Stock compensation subtracted in full [E5-06]: $7,568M, 11.8% of revenue** — the highest
proportion in this queue's history for a company of this size. **[E3-70] recorded and NOT
stacked:** the market-value measure would be higher still; the reported charge is used as
the floor of the subtraction, and $3,860M of shares were additionally repurchased for tax
withholding on vesting in FY2025 (a further real cash cost sitting in financing). Windage is
not spent here.

### THE PRICE — the number the queue's output contract requires

- **Price $357.90** (2026-09-04, Yahoo, aggregator, flagged) · **cap $1,702,738M**
- **Owner-earnings yield: 0.51% to 1.41%** across every construction that exists, including
  the trailing twelve months at the most generous (c).
- **Sovereign 5.24%.** **Every construction, on every window, at both ends, including the
  best twelve months in the company's history, is between 3.83 and 4.73 points BELOW a
  government bond.**

*Nothing in this block is a clearance. Q2, Q3 and Q4 follow.*

---
## Q2 â€” IS IT A FRANCHISE? **[E3-03]**

### THE PROFIT-MIX TEST â€” the HAS precedent, run, and it does NOT give a clean answer

The HAS run settled its gate because WotC was 46.5% of revenue and **92â€“97% of segment
profit** â€” one tail unambiguously wagged. **Broadcom's mix is genuinely split, and it is
moving.** Filed segment figures (FY2025 10-K Note 13; FY2023 10-K for the pre-VMware base;
Q2 FY2026 10-Q; and the Q3 FY2026 release, 8-K acc. 0001730168-26-000076, **furnished**):

| $M | FY2023 | FY2024 | FY2025 | H1 FY2025 | H1 FY2026 |
|---|---|---|---|---|---|
| **Semiconductor solutions** revenue | 28,182 | 30,096 | 36,858 | 16,620 | **27,524** |
| Semiconductor operating income | 16,486 | 16,759 | 21,232 | 9,512 | **16,784** |
| *margin* | *58.5%* | *55.7%* | *57.6%* | *57.2%* | ***61.0%*** |
| **Infrastructure software** revenue | 7,637 | 21,478 | 27,029 | 13,300 | **13,974** |
| Infrastructure software operating income | 5,639 | 13,977 | 20,765 | 10,109 | **10,970** |
| *margin* | *73.8%* | *65.1%* | **76.8%** | *76.0%* | ***78.5%*** |
| **Total segment operating income** | 22,125 | 30,736 | 41,997 | 19,621 | 27,754 |
| **Software share of REVENUE** | 21.3% | 41.6% | **42.3%** | 44.5% | **33.7%** |
| **Software share of SEGMENT PROFIT** | 25.5% | 45.5% | **49.4%** | 51.5% | **39.5%** |

**The answer to "which tail wags" is: it changed hands twice in two years and the
semiconductor half has just taken it back.** Software crossed above half of segment profit
in H1 FY2025 (51.5%) and is back to 39.5% one year later. On the Q3 FY2026 release
semiconductor solutions is **70% of revenue** ($20,839M of $29,591M, +127% year on year)
against software's 30% (+29%).

**And the segment measure Broadcom uses is not a profit measure.** $16,513M of FY2025 cost â€”
acquisition amortisation $8,062M, SBC $7,568M, restructuring $667M, acquisition costs $216M
â€” is **unallocated**, i.e. 39.3% of segment operating income never reaches a segment. The
segment margins above are effectively adjusted EBITA. They are the only split Broadcom
files, so the test is run on them, and the caveat is recorded rather than smoothed.

### THE VMWARE REPRICING â€” this IS the criterion-3 evidence, and it is emphatic

FY2024 to FY2025, infrastructure software segment, filed:

| $M | FY2024 | FY2025 | change |
|---|---|---|---|
| Net revenue | 21,478 | 27,029 | **+5,551 (+25.8%)** |
| Cost of revenue | 2,306 | 1,902 | âˆ’404 (âˆ’17.5%) |
| Research and development | 2,707 | 2,550 | âˆ’157 (âˆ’5.8%) |
| Selling, general and administrative | 2,488 | 1,812 | âˆ’676 (âˆ’27.2%) |
| **Total segment cost** | **7,501** | **6,264** | **âˆ’1,237 (âˆ’16.5%)** |
| **Operating income** | **13,977** | **20,765** | **+6,788 (+48.6%)** |

**Revenue rose a quarter while the entire cost base fell a sixth.** Broadcom's own MD&A
gives the mechanism verbatim: *"strong demand for our VCF product, including license revenue
recognized on contracts where customers do not have the right to terminate and the
transition to a subscription license model. In addition, labor costs were lower following
our integration of the VMware business."*

**Against what it bought:** VMware standalone earned a **15.1% operating margin** in its last
year as a public company (FY2023: $2,022M on $13,350M). Two years later the segment
containing it earns **76.8%**. **[E3-03] criterion 3 does not merely pass â€” this is the
clearest demonstration of unregulated pricing power in the queue's history**, and [E4-37]'s
inverse metric is at the pure yawn end: no prayer session, no agony, a 48.6% profit increase
on a shrinking cost base.

**[E2-44], both characteristics, on the software half:** (1) raise prices with flat volume â€”
**passes**, that is exactly the table above; (2) grow dollar volume on minor additional
capital â€” **passes**, consolidated capex is 0.98% of revenue.

### WHAT CUSTOMERS DID â€” and here the filings run out, which is itself the finding

The brief asked what customers did: renewal, churn. **This cannot be answered from
Broadcom's filings, and I can name no document that would resolve it.**

**[E4-55] recorded sweep of the FY2025 10-K â€” there is no physical series of any kind:**

| term | hits |
|---|---|
| "units shipped" / "unit volume" / "number of units" | **0 / 0 / 0** |
| "seats" / "cores" (as a metric) / "sockets" | **0 / 0 / 0** |
| "installed base" / "subscribers" (as a metric) | **0 / 0** |
| "ARR" (word-boundary) / "annual recurring revenue" | **0 / 0** |
| "net retention" / "renewal rate" / "attach rate" / "bookings" | **0 / 0 / 0 / 0** |

*Precision Steel's pounds fell 69M to 46M while price rises held dollar revenue level*
**[E4-55]** â€” Broadcom publishes no pounds. For the software half specifically, where the
entire thesis is "reprice an installed base," **the size of that installed base is not a
filed number in any vintage.** The only proxies that exist point mildly the wrong way:
**contract liabilities FELL from $14,495M to $13,016M** while revenue rose 25.8%, and RPO is
**$33.3bn with 35% inside twelve months** â€” of which *"approximately 67% of contract
liabilities related to contracts subject to termination for convenience."*

This sub-question is **UNKNOWABLE, not UNRESEARCHED** â€” no filed document contains it â€” and
it is recorded as a bound on what the gate can claim, not as the gate's verdict.

### THE DISCLOSURE RECORD â€” [E2-49] fires, dated, and it is a pattern of three

1. **Apple's percentage was withdrawn.** FY2023 10-K (acc. 0001730168-23-000096, filed
   2023-12-14), three separate places, verbatim: *"We believe aggregate sales to **Apple
   Inc.**, through all channels, accounted for approximately **20% of our net revenue** for
   each of fiscal years 2023 and 2022."* **"Apple" appears ZERO times in the FY2024 10-K
   (acc. 0001730168-24-000139, filed 2024-12-20) and ZERO times in the FY2025 10-K.**
2. **The distributor's name was withdrawn in the same document.** FY2023: *"Direct sales to
   **WT Microelectronics Co., Ltd.**, a distributor, accounted for 21% and 20% of our net
   revenue."* FY2025: *"Direct sales to **one semiconductor solutions customer, which is a
   distributor**, accounted for 32% and 28%."* "WT Microelectronics" = **0 hits** in FY2024
   and FY2025.
3. **In the very same filing that dropped both names, the concentration rose**: top five end
   customers **35% to 40%**.

**No reason is filed for either removal.** And the concentration series that survives, in
anonymised form, is the one that matters: **one customer = 18% (FY2021), 20%, 21%, 28%, then
32% (FY2025) of net revenue, and 44% of net accounts receivable at FY2025 against 18% a year
earlier.**

**Fourth, and the largest: the number the whole equity story rests on has NEVER been filed.**
"AI revenue" and "AI semiconductor revenue" return **0 hits in the FY2025 10-K and 0 in the
Q2 FY2026 10-Q.** The $16.7bn Q3 figure (+221% y/y) and the $21.7bn Q4 forecast exist only
in a press release the 8-K itself states is *"**furnished and shall not be treated as
filed** for purposes of the Securities Exchange Act of 1934."* Broadcom files "XPU" (19
hits) and "custom AI accelerator" (7 hits) as product descriptions and **no dollar figure for
the line that is now the majority of its revenue.** This is the AAPL "active installed base"
shape precisely.

### THE COMPETITOR ROW â€” required **[E3-28]**

Same metric, same window, filing-sourced. Operating margin on the most recent full fiscal
year, from each company's own 10-K via SEC XBRL, with the balance-sheet acquirer tell beside
it.

| Company | operating margin | revenue $M | R&D % rev | SBC % rev | goodwill+intangibles % of assets | period | source |
|---|---|---|---|---|---|---|---|
| **AVGO â€” Infrastructure Software** | **76.8%** | 27,029 | 9.4% | n/a (unallocated) | â€” | FY2025 | 10-K 0001730168-25-000121 |
| **AVGO â€” Semiconductor Solutions** | **57.6%** *(61.0% H1 FY26)* | 36,858 | 9.2% | n/a (unallocated) | â€” | FY2025 | same |
| *AVGO consolidated (GAAP)* | *39.9%* | *63,887* | *17.2%* | **11.8%** | **76.0%** | FY2025 | same |
| **NVIDIA** | **60.4%** | **215,938** | 8.6% | 3.0% | **11.7%** | FY to 2026-01-25 | 10-K, XBRL |
| **Texas Instruments** | 34.1% | 17,682 | 11.8% | 2.4% | 12.5% | FY2025 | 10-K, XBRL |
| **Oracle** | 30.6% | 67,357 | 15.2% | 7.1% | 23.8% | FY to 2026-05-31 | 10-K, XBRL |
| **Qualcomm** *(consolidated)* | 27.9% | 44,284 | 20.4% | 6.3% | 24.9% | FY2025 | 10-K 0000804328-25-000085 |
| â€” *QCOM QTL (licensing)* | *72.4%* | *5,582* | â€” | â€” | â€” | FY2025 | same, Note 8 |
| â€” *QCOM QCT (chips)* | *30.4%* | *38,367* | â€” | â€” | â€” | FY2025 | same, Note 8 |
| **Marvell** | 16.1% | 8,195 | 25.3% | 7.2% | 57.5% | FY to 2026-01-31 | 10-K, XBRL |
| **AMD** | 10.7% | 34,639 | 23.4% | 4.7% | 54.4% | FY2025 | 10-K, XBRL |
| **VMware standalone â€” what Broadcom bought** | **15.1%** | **13,350** | â€” | â€” | â€” | FY to 2023-02-03 | 10-K 0001124610-23-000015 |
| IBM | not obtained â€” `OperatingIncomeLoss` absent from IBM's XBRL | 67,535 | 12.3% | â€” | â€” | FY2025 | 10-K |

**Peers: 8 obtained on the same metric, plus VMware standalone as the before-and-after. One
(IBM) partially obtained and said so.** The row does **not** hold the moat class provisional
â€” the verdict below rests on Broadcom's own filed segment figures, not on the row.

**What the row shows, including the parts that cut against my conclusion [E4-26]:**

1. **The VMware line is the most striking number in this run.** Broadcom bought a business
   earning **15.1%** and it now sits inside a segment earning **76.8%**. Nothing else in the
   row comes close to that transformation, and it is a genuine, filed, repeatable
   demonstration of the thing [E3-03] criterion 3 asks about.
2. **The semiconductor segment is the second-best chip business in the row.** 57.6% (61.0%
   in H1 FY2026) against QCT's 30.4%, TXN's 34.1%, MRVL's 16.1% and AMD's 10.7%. **Stated
   plainly because [E4-26] requires it: I expected the AI business to be a thin design-win
   shop and it is not â€” it out-earns every merchant peer except one.**
3. **And that one is the row's decisive fact against Broadcom.** **NVIDIA earns a 60.4%
   operating margin on $215,938M of revenue â€” 3.4x Broadcom's whole company and 5.9x its
   semiconductor segment â€” and does it with 11.7% of its balance sheet in goodwill and
   intangibles against Broadcom's 76.0%.** The incumbent Broadcom's XPU customers are paying
   it to escape is larger, more profitable, and less acquisition-dependent than Broadcom.
   [E2-45]'s attacker test answers itself: the attacker already exists, at six times the
   scale.
4. **Broadcom is the most purchase-accounting-dependent balance sheet in the row and the most
   SBC-intensive company in it** â€” 76.0% goodwill+intangibles (NVDA 11.7%, TXN 12.5%) and
   11.8% of revenue in stock compensation (NVDA 3.0%, TXN 2.4%). Both are structural facts
   about how this record was produced.
5. **[E3-61]'s limit, stated:** the row shows position, not conduct. It cannot show what
   Google, Meta or OpenAI's silicon teams do in 2028, and **those customers are not in the
   row at all** â€” the same defect the QCOM run recorded about Apple.

**[E2-45] recorded sweep â€” BROADCOM NAMES ZERO COMPETITORS BY COMPANY NAME.** Word-boundary
count in the FY2025 10-K: NVIDIA 0, AMD 0, Marvell 0, Qualcomm 0, MediaTek 0, Intel 0,
Cisco 0, Arista 0, Nutanix 0, IBM 0, Oracle 0, Microsoft 0, Amazon 0, Google 0, Apple 0. The
Competition section runs to two sentences and describes categories only: *"Competitors in
semiconductor solutions include integrated device manufacturers, fabless semiconductor
companies and the internal resources of large integrated OEMs."* (The five "Dell" hits are
the VMware related-party history, not competition.)

### THE TWO HALVES AGAINST [E3-03] AND [E4-04]

**Infrastructure Software â€” (1) yes; (2) yes, for the installed base inside a renewal window,
proven by the repricing table; (3) yes.** And on **[E4-04]**: does a lapse in spending
destroy the structure or merely narrow it? A mainframe bank still pays for CA software bought
in 2018. The advantage is **defended**, not replaced â€” the permitted class. **The moat is
WIDE, and it is being narrowed on purpose:** segment R&D fell from **12.6% to 9.4% of segment
revenue** in one year and to 8.4% in H1 FY2026. That is [E2-60]'s third dimension â€” the
payout is partly funded by under-spending on renewal â€” and it is carried to Q4, not priced
away here. The subject's own filing names the substitute: *"If businesses build new or shift
existing compute workloads off-premises to public cloud providers, this could limit the
market for on-premises deployments of our data center virtualization portfolio."*

**Semiconductor Solutions â€” (1) yes; (3) yes; (2) is where it fails to reach WIDE.**
- **[E4-04]'s excluded class applies to the AI half.** Every XPU generation is a new design
  win competed for afresh. **The moat's basis must be periodically replaced, not merely
  defended** â€” and that is the one thing [E4-04] excludes. **[E3-51] is the honest
  description: this is a surfing run.** *"when a surfer gets up and catches the wave and just
  stays there, he can go a long, long time. But if he gets off the wave, he becomes mired in
  shallows."* The wave is hyperscaler capital spending. Broadcom is a superb surfer; the
  advantage lives substantially in the wave. **[E4-36]**: the record comes from a nonlinear
  combination (which is ownable) *and* from wave-riding (which is not).
- **The customers are the substitute, and the filing says so:** *"We expect competition in
  these markets to continue to increase as existing competitors improve or expand their
  product offerings and as new companies, **including some of our customers**, enter the
  markets."*
- **[E4-37]'s inverse metric FIRES on this half, in Broadcom's own risk factors:** *"our top
  customers, **including our AI customers, may make and have made greater demands on us with
  regards to pricing and contractual terms**, such as seeking to lease AI racks or systems
  based on our XPUs instead of purchasing, as well as alternative financings for such leases
  or other novel or deferred payment modelsâ€¦ which could have a material adverse effect on
  our revenue, free cash flow and gross margin and expose us to credit or customer default
  risks."* **The company is disclosing that its largest and fastest-growing customers are
  dictating terms to it.** The agony is on the half that is taking over the profit mix.
- Concentration: top five end customers **40%**; one distributor **32% of revenue and 44% of
  receivables**.

**[E3-33] untapped pricing power â€” the class is NOT claimable here, and the reason matters
for Q5.** [E3-33]'s "ultimate no-brainer" is a business that *has not* raised prices. Broadcom
has just raised them as hard as any company in the corpus's reach. **The pricing power is
tapped, and a tapped one-time re-rating cannot be a perpetual growth term [E4-44].** The
H1 FY2026 software line â€” **+5.1%** â€” is what the second year after a repricing looks like.

- Class: [ ] WIDE  **[x] NARROW**  [ ] NONE  [ ] PROVISIONAL
- **Direction: the profit mix is migrating OUT of the wide half and INTO the narrow one** â€”
  software 49.4% of segment profit (FY2025) to 39.5% (H1 FY2026); semiconductor 70% of
  revenue by Q3 FY2026. **[E4-32] asks whether the moat widened; here one moat widened
  spectacularly and briefly, and the company's centre of gravity moved off it.**
- **VERDICT: [x] IN (NARROW)** â€” not OUT, because unlike QCOM there is no filed admission
  that the franchise half is expiring, and the software franchise is real, large and
  demonstrated ($20,765M of segment operating income at 76.8%, five times QTL's entire EBT);
  not WIDE, because the majority of the business and effectively all of the growth now sits
  in the class [E4-04] excludes.


---
## Q3 â€” ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 â€” THE WEIGHT CASE, DECLARED. Nothing below counts until this is filled in.**

- [ ] **Daily execution [E3-38, E3-43, E2-70]** â€” **refused.** [E3-38]'s magnifier is an
  undifferentiated product whose *"only products are promises."* Broadcom's revenue is
  contracted: $33.3bn of firmly committed remaining performance obligations, design wins
  fixed years ahead of shipment, and software on multi-year licences. This is
  have-to-be-smart-*periodically* â€” at each acquisition and each design-win cycle â€” not
  every day.
- [ ] **Control [E1-16]** â€” refused. Public-market minority; exit is a market order.
- [ ] **Leverage [E3-29]** â€” **argued at length and refused, and the argument is close
  enough to record.** *For:* total debt **$67,120M**, and **tangible book equity is NEGATIVE
  $48,782M** (equity $81,292M less goodwill $97,801M less intangibles $32,273M). Three
  quarters of the balance sheet is purchase accounting. *Against, and it governs:* [E3-29]'s
  test is whether **small asset errors destroy equity**, and its calibration is a bank at
  twenty to one. Broadcom's assets-to-equity is **2.1Ã—**; debt to trailing operating cash
  flow is **1.65Ã—** ($67,120M Ã· $40,653M); **[E2-54]'s coverage test passes at 10.1Ã—** â€”
  operating cash flow net of ample capital expenditure ($27,537M âˆ’ $623M = $26,914M) against
  cash interest paid of $2,672M. A goodwill impairment would erase book equity and **would
  not be a cash event or a covenant event**: *"We are not subject to any financial covenants
  under the notes."* The debt is serviced out of cash flow, not out of asset values.

**NONE TICKED â†’ Q3 IS A QUALITATIVE OVERLAY.** Findings are recorded; manager quality alone
does not stop this run, and â€” per the guardrail â€” **nothing in this section may promote the
name.**

### STEP 2 â€” THE FLAGS. *Each is a prompt to READ, never a verdict.*

**Recorded sweep of the FY2025 10-K (accession 0001730168-25-000121), word counts:**

| term | hits | reading |
|---|---|---|
| **EBITDA** | **0** | **[E4-29] does not fire in any filing** |
| **non-GAAP** | **0** | zero management-defined non-GAAP measures in the 10-K |
| "adjusted" | 11 | incidental (working-capital adjustments, purchase-price adjustments) |
| "except for" | 1 | incidental; **[E2-57] does not fire** |
| "consecutive" | 0 | Broadcom does not boast of its dividend streak |
| "restructuring" | 29 | **see [E3-53] below** |

- [ ] **weak accounting â€” does not fire.** Stock compensation is expensed in full and is the
  largest single line of its kind in the competitor row (11.8% of revenue). The pension note
  discloses a *"fully-matched, liability-driven investment strategy"* with *"The U.S.
  expected rate of return on plan assetsâ€¦ set equal to the discount rate"* â€” the opposite of
  the fanciful-assumption tell.
- [ ] **unintelligible footnotes â€” does not fire, and the opposite is true.** The VMware
  purchase-price allocation is given in full: consideration, allocation, **intangibles by
  class with weighted-average lives**, the valuation method named for each class
  (multi-period excess earnings, with-and-without, relief-from-royalty), and an **IPR&D table
  by project with percentage of completion, cost to complete and expected release date.**
  That is more disclosure than the corpus usually gets and it is recorded as a candour point.
- [x] **TRUMPETED EARNINGS PROJECTIONS â€” FIRES, and it is the loudest flag in this file.**
  Broadcom guides publicly every quarter, in dollars, and forecasts a **single product line's
  revenue** one quarter ahead: *"In Q4 the momentum continues, and **we expect AI
  semiconductor revenue to accelerate to $21.7 billion, up 236% year-over-year**"* (8-K acc.
  0001730168-26-000076, 2026-09-02). **[E5-30] is the governing quote â€” the behaviour is a
  ratchet:** *"once you start it, it's all over. You can't quitâ€¦ And forecasting earnings, I
  can't imagine anything more destructive."*
- [ ] **serial share issuance [E5-15] â€” does not fire, and the arithmetic is why.** Shares
  went 4,139M (FY2023) â†’ 4,741M (FY2025), **+14.5%** â€” of which **544M (13.1%) is the single
  VMware share issuance**, acquisition currency, not promotion. Ex-VMware the two-year
  dilution is +58M, **+1.4%**: stock compensation is being offset by repurchase. Proceeds
  from stock issuance are trivial ($221M in FY2025).
- [ ] **filed-figure tells [E4-30] â€” do not fire, and one runs the wrong way for the fraud
  shape.** Cash taxes paid as a share of pre-tax income: **11.8% (FY2023) â†’ 31.8% (FY2024) â†’
  11.4% (FY2025)** â€” volatile, not the smooth decline [E4-30] looks for. Reported growth is
  emphatically **not** smooth: operating income $16,207M â†’ $13,463M â†’ $25,484M and net income
  $14,082M â†’ $5,895M â†’ $23,126M in three years. A filer engineering smoothness does not print
  that series.
- [x] **[E3-53] RESTRUCTURING â€” FIRES, as a recurring "one-time" charge.** $248M (FY2023),
  **$1,787M (FY2024)**, $667M (FY2025), plus $216Mâ€“$549M of acquisition-related costs. These
  are the running cost of an acquire-and-cut model, taken **every single year**. **[E5-33]
  governs and is satisfied at the consolidated level** â€” they are cash costs inside operating
  cash flow and they are therefore *inside* every owner-earnings figure in this run. **But the
  segment measure excludes them**, along with all SBC and all acquisition amortisation:
  **$16,513M, or 39.3% of segment operating income, never reaches a segment.** That is the
  *"don't count this"* pattern [E5-33] warns about, applied at the segment line.
- [x] **[E2-49] METRIC-SWITCHING â€” FIRES, three withdrawals, all dated to one document.**
  Recorded in full at Q2: Apple's ~20% figure and the WT Microelectronics name both removed
  in the **FY2024 10-K (acc. 0001730168-24-000139, filed 2024-12-20)**, in the same filing
  that raised the top-five concentration from 35% to 40%; and the AI revenue line has never
  been filed at all. **No reason is filed for any of it.**
- [ ] **[E2-52] dividends funded by issuance â€” does not fire.** FY2025 dividends of $11,142M
  against $221M of stock-issuance proceeds; the dividend is 50Ã— the issuance. Ten consecutive
  annual increases, $716M (FY2016) to $11,142M (FY2025).

**[E3-48] â€” THE ACTION REQUIRED ON THE PROJECTIONS FLAG: past guidance against outturn.**
The corpus says *"about nine cases out of ten"* of projections exist to justify a decided
course, and the remedy is to demand *"the record of the people who made the projections."*
Here is that record, from the furnished 8-K releases:

| Guided in | For | Revenue guidance | Actual | Result |
|---|---|---|---|---|
| Q4 FY2025 release, 2025-12-11 | Q1 FY2026 | $19.1bn (+28%) | $19,311M | beat **+1.1%** |
| Q1 FY2026 release, 2026-03-04 | Q2 FY2026 | $22.0bn (+47%) | $22,187M | beat **+0.85%** |
| Q2 FY2026 release, 2026-06-03 | Q3 FY2026 | $29.4bn (+84%) | $29,591M | beat **+0.65%** |
| Q3 FY2026 release, 2026-09-02 | Q4 FY2026 | $34.8bn (+93%) | pending 2026-12 | â€” |

**Three for three, every beat between 0.65% and 1.1%, on a business growing 84â€“93%.** The
honest reading runs both ways and both are recorded: it is either exceptional forward
visibility (which the $33.3bn of committed RPO supports) or careful sandbagging. **It is not
the [E4-30] fraud shape** â€” that shape smooths *results*, and Broadcom's results are among
the lumpiest in the queue. What it is, unambiguously, is [E5-30]'s ratchet: a company that
now has to produce a number every ninety days.

**And a genuine candour point against my own reading, stated because [E4-26] requires it.**
The Q3 FY2026 release says, of its own non-GAAP measures: *"**The exclusion of these and
other similar items from Broadcom's non-GAAP financial results should not be interpreted as
implying that these items are non-recurring, infrequent or unusual.**"* A company telling
readers that its own adjustments are recurring is doing the opposite of the [E4-29] sin.
Set against that: the Q4 guidance is given **only** as *"non-GAAP operating income guidance
of approximately 66 percent of projected revenue"* with the statement that the company *"is
not readily able to provide a reconciliationâ€¦ without unreasonable effort."* **The wedge is
not small: Q3 FY2026 GAAP operating income was $15,955M (53.9% of revenue) against $20,095M
non-GAAP (67.9%) â€” $4,140M and fourteen margin points.** So the guided "66%" corresponds to
a GAAP figure near 54%, and no filed document says so.

### STEP 3 â€” THE PRIMARY TEST [E2-01], AND ITS DENOMINATOR MUST BE REFUSED

> *"The primary test of managerial economic performance is the achievement of a high earnings
> rate on equity capital employed (**without undue leverage, accounting gimmickry, etc.**)"*

**Return on book equity is unusable here, and for two corporate actions rather than one.**

| FY | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Equity (assets âˆ’ liabilities) $M | 24,970 | 23,901 | 24,989 | 22,709 | 23,988 | **67,678** | **81,292** |
| Net income $M | 2,736 | 2,961 | 6,736 | 11,495 | 14,082 | 5,895 | 23,126 |
| **ROE** | 11.0% | 12.4% | 27.0% | 50.6% | **58.7%** | **8.7%** | 28.4% |

Equity was held flat at $23â€“25bn for five years because dividends plus buybacks exceeded
earnings, which manufactured the 50â€“59% readings of FY2022â€“23; then it **tripled in one year**
because $53,421M of stock was issued for VMware, which manufactured the 8.7% reading of
FY2024. **[E2-47]** carves out exactly this case (*"unusual debt-equity ratios"*) and
**[E2-43]** supplies the replacement: unleveraged net tangible assets, **with the goodwill
wedge reported separately, never hidden in book equity.**

**[E2-43], run, FY2025:**
- Total assets $171,092M âˆ’ goodwill $97,801M âˆ’ intangibles $32,273M = **$41,018M tangible**
- less non-interest-bearing current liabilities ($1,560M + $2,129M + $11,673M = $15,362M)
- **= net tangible operating assets $25,656M**; **excluding $16,178M of cash, $9,478M**
- Pre-tax operating income $25,484M Ã· **$25,656M = 99.3%**; **Ã· $9,478M = 269%**
- **And the wedge, reported separately as [E2-43] demands: tangible book equity is NEGATIVE
  $48,782M.**

**On the underlying assets this is one of the two or three best businesses this queue has
measured** (AAPL 333%, GRMN ~48%, CTAS ~51%, WMT ~22%). **[E2-73] is the sentence that
keeps that from being the answer:** *"the managers of the units should be judged by the
returns they achieve on the underlying assets; **what we pay for a business does not affect
the amount of capital its manager has to work with.**"* Measured on **what was paid** â€”
$130,074M of goodwill and acquired intangibles â€” FY2025 operating income of $25,484M is a
**19.6% pre-tax return on the acquisition book.** Good. Not 269%. And the second number is
the one a buyer of the shares is buying.

**The half-owner test [E2-26].** Does this reporting tell me what I would want to know if
the positions were reversed? **Split, and the split is the finding.** On the acquisition:
outstandingly â€” lives, methods, IPR&D by project, a filed pro forma. On the *business*:
no. The largest revenue line is unnamed in any filing, the largest customer is anonymised
after having been named, and the profit of the $86bn acquisition is declared *"impracticable
to determine."* A half-owner would want all three.

### THE INSTITUTIONAL IMPERATIVE â€” score all four [E2-30]

*Not a fraud test: "institutional dynamics, not venality or stupidity."*

- [ ] **resists any change in current direction** â€” **no.** Broadcom has re-shaped itself
  three times in eight years (CA 2018, Symantec 2019, VMware 2023) and **sold** the VMware
  EUC business to KKR within eight months of acquiring it. It also walked away from the
  Qualcomm bid when blocked. This is the opposite of the flag.
- [x] **projects/acquisitions materialise to soak up available funds** â€” **fires on the
  form, and the substance is arguable both ways.** $86.3bn deployed on a single acquisition
  is by definition funds being soaked up; the counter is that Broadcom paid down **$30,390M
  of VMware term loans in full** and terminated the facility rather than rolling into the
  next deal, and made **no acquisitions at all in FY2025** ($0 on the cash-flow line).
- [ ] **staff studies to justify the leader's craving** â€” no evidence in the filings either
  way. Recorded as not observable.
- [ ] **peer behaviour mindlessly imitated** â€” **no, and emphatically.** While NVIDIA, AMD,
  Marvell and Oracle raised capital intensity, Broadcom's capex is **0.98% of revenue** and
  it built no fabs and no data centres. Broadcom is the least imitative company in its row.

### CAPITAL ALLOCATION â€” the buyback conditions [E5-08]

- **(1) ample funds for operations and liquidity â€” YES.** $24.0bn of cash at Q3 FY2026,
  $40.7bn of trailing operating cash flow, an undrawn $7.5bn revolver and an unused $4.0bn
  commercial-paper programme (neither counted, per [E5-39]).
- **(2) repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value â€”
  FAILS, and the series is the evidence:**

| period | spent $M | shares retired (M) | **average price** |
|---|---|---|---|
| FY2023 | 5,824 | 91 | **~$64** |
| FY2024 (Q1) | 7,176 | 67 | **~$107** |
| FY2025 | 2,450 | 16 | **~$153** |
| **H1 FY2026** | **8,450** | **25** | **~$338** |

**The average repurchase price has risen 5.3Ã— in three years with no change in behaviour,
and the largest buyback in the company's history was executed at the highest price it has
ever paid** â€” against a judged value range at Q5 below that does not reach $338 on any
construction. **[E5-24] observed inside one company's own record:** *"what is smart at one
price is dumb at another."* The FY2023 and FY2024 repurchases at $64 and $107 look
excellent; the H1 FY2026 repurchase at $338 does not.
- **â†’ CAPITAL-ALLOCATION FLAG, raised with the humility clause [E4-13]:** this rests on my
  own IV range, and *"it is natural for CEOs to be optimistic about their own businesses.
  They also know a whole lot more about them than I do."* **It binds position size, never the
  discount rate.**

**[E5-44] â€” the stock deal, and it is the largest single allocation decision in the file.**
*"The intrinsic value of the shares you give in an acquisition must not be greater than the
intrinsic value of the business you receive."* Broadcom paid $86,290M for VMware, of which
**$53,421M was 544 million of its own shares.** Those 544 million shares are worth
**$194,698M at today's $357.90.** Measured in what shareholders actually gave up rather than
in the accounting figure, the consideration was far larger than $86.3bn â€” **which is exactly
[E5-44]'s point: a premium paid in undervalued shares is larger than it looks.** Whether the
paper was undervalued *at the close* cannot be settled from filings, and I do not settle it;
the 3.7Ã— subsequent move is evidence, not proof. **Recorded as the honest counterweight to
the "the VMware deal was brilliant" reading that the segment margins invite.**

**[E2-39]/[E2-56] PRO-AM TEST â€” judge retention segment by segment, never on the blended
return.** The blended incremental return since FY2023 is flattering because it mixes a
capital-free semiconductor ramp with an $86bn purchase. Split:
- **Semiconductor solutions added $4,746M of operating income (FY2023 â†’ FY2025) on
  essentially no incremental capital** â€” capex across those two years totalled $1,171M. That
  is the Pro half, and it is exceptional.
- **Infrastructure software added $15,126M of operating income on $79,648M of net purchase
  price** â€” **19.0% pre-tax on the money actually spent.** Above [E5-40]'s ~12%
  return-on-retention benchmark, and nowhere near the 269% the underlying assets earn.
**The consolidated figure hides that the good return was bought and the spectacular return
was free.**

### THE GUARDRAIL â€” checked before the verdict

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The VMware execution is
  the strongest managerial record in this queue and **[E2-37] governs** â€” *"a textile company
  that allocates capital brilliantly within its industry is a remarkable textile company â€”
  but not a remarkable business."* A strong Q3 cannot repair Q2's NARROW or substitute for
  Q5's arithmetic.
- [x] **Does this business require a great manager?** **Partly yes, and it is recorded at Q2
  as a moat defect per [E4-23], not here as a strength.** The infrastructure-software
  franchise's *economics* â€” a 15.1% margin becoming 76.8% â€” were produced by a specific
  management method, not by the position alone. **[E4-23]:** *"if a business requires a
  superstar to produce great results, the business itself cannot be deemed greatâ€¦ The
  partnership's moat will go when the surgeon goes."* Broadcom's software returns are closer
  to the surgeon than to the Mayo Clinic. This is a real key-person exposure and it is why
  Q2 came back NARROW rather than WIDE.
- [x] Is the franchise intact and the damage excisable, or is the manager the plan? **Not
  applicable â€” there is no damage to excise.** No turnaround is being underwritten here.

**[E4-52] â€” DO THE FLAGS CONVERGE?** Three fire: trumpeted projections, recurring
restructuring excluded from the segment measure, and three dated disclosure withdrawals. **I
looked hard for the lollapalooza and I do not find one, and the reason is directional.** The
AAPL case converged because metric withdrawal, undisclosed sub-lines and price-indifferent
buybacks all pushed *one way* â€” reducing the shareholder's ability to price the company while
buying him out. Here the disclosure record runs **both ways at once**: the same management
that withdrew Apple's percentage published a full purchase-price allocation with lives and
methods, an IPR&D table by project, a filed pro forma, and an express statement that its own
non-GAAP adjustments recur. **That is not a reinforcing system; it is a company that
discloses transactions exceptionally and operations poorly.** Recorded as a two-sided finding
per [E2-30]'s *"institutional dynamics, not venality or stupidity"* and [E5-38].


### STEP 4 â€” PAY VERSUS PERFORMANCE, AND IT REVERSES TWO OF MY OWN FINDINGS ABOVE

*Written after the proxies were read. **Two conclusions recorded earlier in this Q3 are
wrong and are corrected here rather than silently edited** â€” the [E4-52] lollapalooza
paragraph and the [E2-30](4) peer-imitation score. Both were written from the 10-K alone;
the proxy overturns both. Full working:
`_research 2026-09-06 AVGO/02 - proxy, pay versus performance, ownership.md`.*

**Sources: DEF 14A filed 2026-03-02, accession 0001193125-26-085691 (`d49254ddef14a.htm`,
FY2025 compensation); DEF 14A filed 2025-03-03, acc. 0001193125-25-044112; DEF 14A filed
2024-02-26, acc. 0001140361-24-009541.**

**The size, filed:**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Hock Tan, Summary Compensation Table total | $161,826,161 | $2,634,542 | **$205,278,006** |
| **Compensation Actually Paid (402(v))** | $768M | $1,150M | **$2,268M** |
| CEO pay ratio | â€” | 8 : 1 | **543 : 1** |

**Compensation actually paid to one person in fiscal 2025 was $2,268 million â€” 11.7% of the
year's entire owner earnings ($19,346M) and 9.8% of net income.** $2,045M of it is the
year-over-year mark-to-market on the 2023 award as the share price ran; it is not a new
grant, and the run says so.

**Pay versus performance, both columns, as filed** â€” $100 invested 2020-10-30:

| FY | AVGO TSR | NASDAQ 100 TSR | verdict |
|---|---|---|---|
| 2021 | 156.83 | 144.43 | **BEAT** |
| 2022 | 143.70 | 106.05 | **BEAT** |
| 2023 | 261.58 | 131.38 | **BEAT** |
| 2024 | 535.10 | 187.18 | **BEAT** |
| 2025 | **1,182.35** | 243.37 | **BEAT by 4.86Ã—** |

**Broadcom beat its stated comparator in all five years by a widening margin, and this is the
opposite of the AAPL finding, where the company printed its own underperformance and paid on
a different index anyway.** Stated plainly because [E4-26] requires the disconfirming fact
first: **the pay tracked the performance, the performance was real, and it was extraordinary.**
*(The 402(v) comparator is the NASDAQ 100 **index**, not the 16-company compensation peer
group â€” a weaker comparator in principle, and immaterial here given the margin.)*

**The 2023 Tan PSU Award â€” the target-setting test, and it passes.** Granted 2022-10-31: up
to 1,000,000 pre-split shares on **absolute stock-price hurdles of $825 / $950 / $1,125**
against a $470.12 grant-date price â€” *"a 75.5%, 102.1% and 139.3% increaseâ€¦ over a five-year
period"* â€” measured on a 20-day average, **no interpolation between hurdles**, earnable only
after the third anniversary, vesting 2027-10-31. It covers five years of bonus and five years
of equity. **Those were demanding bars honestly set in advance, which is [E2-49]'s
"pre-set, long-lived and small bullseyes" satisfied.** They were then cleared: performance is
*"tracking above target."* And Tan gave consideration for the next award â€” a **post-vesting
holding requirement** on the after-tax shares through fiscal 2030, extending to fiscal 2032 on
a voluntary resignation. The 2025 award is **forfeited in its entirety** on a change of
control before Q1 FY2028: no single-trigger acceleration. Those are genuine
shareholder-aligned terms and they are recorded as such.

### AND THEN THE FINDING THAT CHANGES THE READ

**The 2025 Tan PSU Award â€” granted 2025-09-03, target 610,521 shares, payout 0â€“300%,
grant-date fair value $202,351,080 at target and $607,053,241 at maximum â€” vests against a
metric called "AI Revenue".**

| Achievement | Applicable AI Revenue | Payout |
|---|---|---|
| Maximum | â‰¥ **$120 billion** | 300% |
| Stretch | $105 billion | 200% |
| Target | **$90 billion** | 100% |
| Threshold | â‰¤ $60 billion | 0% |

measured as *"the highest aggregate AI Revenue for a period of any four consecutive fiscal
quarters within the Performance Period"* (fiscal 2028 through fiscal 2030).

**"AI Revenue" IS NOT A FILED METRIC. It appears ZERO times in the FY2025 10-K and ZERO times
in the Q2 FY2026 10-Q.** It exists only in press releases that the covering 8-K states are
*"furnished and shall not be treated as filed for purposes of the Securities Exchange Act of
1934."* The proxy says attainment *"will be determinedâ€¦ under GAAP reporting"* â€” but there is
no GAAP line, no segment and no filed definition called AI Revenue anywhere in Broadcom's
periodic reports.

**[E4-52] THEREFORE FIRES, AND MY EARLIER PARAGRAPH SAYING IT DOES NOT IS WITHDRAWN.** The
convergence is not a sum of prompts; it is one reinforcing system, and every arrow points the
same way:
1. **The largest revenue line in the company is never filed** â€” only furnished.
2. **The CEO's largest-ever award, worth up to $607M at grant-date fair value, pays out on
   that same unfiled line.**
3. **Management forecasts that same unfiled line, in dollars, one quarter ahead, every
   quarter** â€” *"we expect AI semiconductor revenue to accelerate to $21.7 billion"* â€” in the
   same furnished document.
4. **The named-customer disclosures that would let an outsider check it were withdrawn** in
   the FY2024 10-K (Apple's ~20%; the WT Microelectronics name), while concentration rose.
5. **Buybacks ran to a record $8,450M at a record average price of ~$338** in H1 FY2026.

**[E4-27] is the governing line and operator rule 9 makes it binding on me as well as on
them:** *"Never, ever, think about something else when you should be thinking about the power
of incentives."* A company that defines a metric itself, publishes it only where it is not
legally "filed", guides on it quarterly, and pays its chief executive up to $607 million
against it, has built the incentive and removed the audit surface in the same motion.

**Stated with the corpus's own restraints, because they matter here.** **[E2-30]**: this is
*"institutional dynamics, not venality or stupidity."* **[E5-38]**: a fired flag is not a
venality finding â€” people Buffett would trust with his wallet *"would play games with any
number that came to them."* **[E5-16]'s binary is not triggered**: there is no personal
misconduct in the record, the bars were set high and disclosed in advance, the performance
was delivered, and Broadcom disclosed the award on an 8-K and then *"held 16 meetings with
stockholders representing 38% of common stock outstanding."* **This is a structural
observation about where the metric lives, not an accusation.**

**[E2-30](4) IS ALSO CORRECTED â€” peer behaviour mindlessly imitated FIRES, in the company's
own words, and my "no, and emphatically" above was scored on operations only.** The proxy
states how the *size* of the award was set, verbatim:

> *"the independent directors **aligned the annual target value of the 2025 Tan PSU Award with
> the top decile of current chief executive officer compensation for similarly-situated large
> technology peer companies based in the Silicon Valley region**"*

The *performance bar* is set against the business ($90bn of AI revenue). The *prize* is set
against what other chief executives are paid. That is [E2-30](4) exactly, and it is disclosed
rather than hidden â€” which is the candour case and the flag at the same time.

**One further disclosure item, recorded because it is the proxy-level version of a non-GAAP
measure.** Alongside the mandated Summary Compensation Table, Broadcom prints a
**"Supplemental Fiscal 2025 Summary Compensation Table"** â€” labelled *"provided for
informational purposes only and does not form part of our disclosures required by the SEC"* â€”
which removes the 2025 award and substitutes one-fifth of the 2023 award, restating Tan's
FY2025 total from **$205,278,006 to $35,034,926**, and a **"Supplemental CEO Pay Ratio"** of
**93 : 1** in place of the filed **543 : 1**. The labelling is candid; the purpose is plain.

### VERDICT

- **VERDICT: [x] IN** â€” *no disqualifier found.* **This is NOT a finding that the managers are
  honest [E5-17]:** *"People are not that easy to read. Sincerity and empathy can easily be
  faked."* It is a finding that the record contains no integrity failure, no restatement, no
  10-K/A, no EBITDA promotion, no smoothed earnings series, and no dividend funded by
  issuance â€” set against a live **capital-allocation flag** (buybacks at $338), a live
  **[E4-52] convergence** around an unfiled metric, a live **[E5-30] guidance ratchet**, and
  **[E2-30](2) and (4)** firing. **IN never promotes [E2-37, E2-38, E3-39]**, and the
  guardrail is the operative rule here more than anywhere else in this file: Broadcom's
  management record is the best operational-and-allocation record this queue has examined,
  and **it cannot repair Q2's NARROW or move one dollar of Q5's arithmetic** â€” *"betting on
  the quality of a business is better than betting on the quality of management."*


---
## Q4 â€” WILL IT SURVIVE?

### Owner earnings â€” the one number **[E2-23]**

The full construction, both ends and six windows, is in the COMPUTATION block above and is
not repeated. The summary:

- **Short-window mean** (3-yr FY2023â€“25, capex end): **$16,160M**
- **Long-window mean** (10-yr FY2016â€“25, capex end): **$10,517M**
- **Corpus default** (5-yr FY2021â€“25, capex end) **[E2-42]**: **$14,975M**
- **D&A end** (5-yr): **$8,744M** â€” and at Broadcom **this is the CONSERVATIVE end**
- **TTM to 2026-05-03, capex end, entirely from filed documents:** **$23,977M**
- **TTM to 2026-08-02** *(adds the Q3 FY2026 furnished release)*: **$30,921M**
- **Combined range: $8,744M to $30,921M â€” a 3.5Ã— band, 254% wide.**

**Is that range too wide to reach a conclusion [E4-25]? No â€” and the reason is the MSFT
adjudication, not a preference.** [E4-25] closes a file when the range **straddles the
answer**. This one straddles nothing: **every construction, at both ends, on every window,
including the trailing twelve months and including the single best quarter in company
history annualised, yields between 0.51% and 2.74% against a 5.24% sovereign.** The width is
enormous and it is decision-irrelevant, so the file stays open to a verdict.

**A wide spread is also a Q4 finding [E5-11], and the distorted years are named in the
computation block above**: FY2024 depressed by the acquisition (SBC $2,171M â†’ $5,741M,
amortisation $3,335M â†’ $9,417M, restructuring $248M â†’ $1,787M); FY2025 elevated by a
**negative book tax rate of âˆ’1.7%** whose filed cause â€” *"recognition of uncertain tax
benefits from expiration of statutes of limitations and audit settlements, and excess tax
benefits from stock-based awards"* â€” will not repeat; FY2016 depressed by the Avago/Broadcom
merger. **[E4-41] normalisation DOWN for luck is named and NOT applied**, deliberately: the
AI-accelerator surge is exactly the favourable exogenous break [E4-41] says to strip, and I
have left it in so that the Q5 conclusion cannot be accused of having been manufactured by
stripping it.

- **Maintenance capex (c) â€” the disclosed judgment, and the CVX inversion is live.** Judged
  at **total capital expenditure**, currently ~$623Mâ€“$1,250M TTM. **The physical ratio is
  1.09Ã—** (capex $623M against separately-stated depreciation of $574M), which is squarely
  [E3-44]/[E2-41]'s DEFAULT class and not [E5-20]'s railroad exception. The $8,062M of
  acquisition-related amortisation renews nothing that is not already renewed by **$10,977M
  of R&D expensed above the operating-cash-flow line**; deducting both would charge the
  renewal twice. **Full reasoning, including the [E2-60] counter-argument that the software
  franchise's renewal spend is being cut, is in the COMPUTATION block.**
- **Stock compensation subtracted in full [E5-06]: $7,568M (FY2025), $8,482M TTM â€” 11.8% of
  revenue, the highest in the competitor row.** [E3-70] recorded and **not** stacked.
- **[E2-60], the third dimension of maintenance, scored both ways.** FY2025 dividends
  $11,142M + buybacks $6,310M = **$17,452M against $19,346M of owner earnings, a 90.2%
  payout** â€” and total debt nonetheless **FELL** from $69,847M to $67,120M, with the entire
  $30,390M of VMware term loans repaid and the facility terminated. **Financial strength was
  not spent to fund the payout, so [E2-60] does not fire on the balance sheet.** It fires,
  partially, on the competitive position: **infrastructure-software R&D fell from 12.6% to
  9.4% of segment revenue and to 8.4% in H1 FY2026**, while consolidated R&D rose to
  $10,977M with all of the increase in semiconductors. **The honest statement: consolidated
  renewal spend is rising; the acquired software franchise's renewal spend is falling.**

### Great, good, or gruesome? **[E4-20]**

- **[x] GREAT** â€” high return, rising, little capital needed. On **[E2-43]**'s denominator,
  pre-tax operating income of $25,484M on **$25,656M of unleveraged net tangible operating
  assets = 99.3%**, and **269% excluding cash**. Capital expenditure is **0.98% of revenue**.
  Growth in FY2025â€“26 consumed essentially no incremental physical capital: the semiconductor
  segment added $4,746M of operating income over two years on $1,171M of total company capex.
- **And the [E2-63] ceiling stated in the same breath, because it is the whole Q5 problem.**
  There is nowhere to redeploy at 269%. The marginal retained dollar has three destinations
  and all are bounded: **acquisitions at ~19â€“20% pre-tax** on money actually spent (the
  infrastructure-software segment added $15,126M of operating income on $79,648M of net
  purchase price = **19.0%**, above [E5-40]'s ~12% benchmark but a twelfth of the underlying
  return); **buybacks capped arithmetically at the earnings yield of 1.4â€“2.7%**, and being
  executed at ~$338; and **dividends**, now $11,142M a year. **[E4-43] warns against
  over-reading the classification and it applies: GREAT is the right class, and the class
  does not price the shares.**

### Staying power â€” score all three **[E5-11]**

- **(1) A large and reliable stream of earnings â€” PASS.** $40,653M of trailing operating cash
  flow; $33.3bn of firmly committed remaining performance obligations; two segments both at
  57%+ operating margins.
- **(2) Massive liquid assets â€” PASS.** Cash and equivalents **$16,178M** at 2025-11-02,
  **$19,628M** at 2026-05-03 and **$24.0bn** at 2026-08-02 (Q3 release). Rising every quarter
  while the largest buyback in company history was executed.
- **(3) No significant near-term cash requirements â€” PASS, and this is the one that usually
  kills.** Twelve-month fixed claims, from the filed contractual-obligations table and the
  balance sheet: **current portion of debt $3,152M + purchase commitments $106M + other
  contractual commitments $777M = $4,035M.** Against **$24.0bn of cash** that is **5.9Ã—
  coverage on liquid assets alone**, and 10.1Ã— on a single year's operating cash flow.
  **[E5-39] observed: no bank line is counted.** The undrawn **$7.5bn revolver** (2025 Credit
  Agreement, expires 2030-01-13) and the unused **$4.0bn commercial-paper programme** are
  recorded as existing and are given **zero** weight â€” *"We will never be dependent on the
  kindness of strangers."*
- **Leverage, named and quantified â€” there is no ratio ceiling in this framework and the
  corpus supplies none.** Total debt principal **$67,120M**, down from $69,847M. Assets to
  equity **2.1Ã—**. Debt to trailing operating cash flow **1.65Ã—**. **[E2-54]'s coverage test
  â€” the one the corpus actually supplies â€” passes at 10.1Ã—:** operating cash flow net of
  ample capital expenditure ($26,914M) against cash interest paid ($2,672M). **[E3-52] read
  on terms, not quantity:** *"We are not subject to any financial covenants under the notes
  nor any covenants that would prohibit us from incurring additional indebtedness"* (the
  revolver alone carries an interest-coverage test); and **$13,016M of contract liabilities
  are customer-prepaid, covenant-free, due-date-free money** â€” the [E3-52] animal.
  **The deleveraging is the fact: $30,390M of acquisition term loans repaid in full inside
  two years and the credit agreement terminated.**
- **And the offsetting negative, stated: tangible book equity is NEGATIVE $48,782M.** It is
  recorded and it is **not** a solvency finding, because nothing in the capital structure is
  secured on, or tested against, asset values.
- **ASC 842 â€” IMMATERIAL, and measured rather than assumed.** Operating lease expense
  **$182M** (0.29% of revenue); cash paid for leases $277M; ROU additions $220M; weighted
  average term 11 years at 4.78%. **Finance lease liabilities are ZERO** at 2025-11-02 (they
  were $39M in total a year earlier). Nothing resembling the MSFT problem, where finance
  leases exceeded all bonded debt.
- **Software-capex line â€” an absence, recorded.** *"capitalized software"* **0 hits**,
  *"internal-use software"* **0 hits**, *"software development costs"* **0 hits** in the
  FY2025 10-K. The HAS defect cannot bite because no such line is disclosed; R&D of $10,977M
  is expensed. The composition is opaque and that is stated, not resolved.
- **Contingent-liability persistence â€” does not fire, for the AAPL reason.** *"During the
  periods presented, **no material amounts have been accrued or disclosed** â€¦ with respect to
  loss contingencies."* There is no carried-forward balance whose persistence could be
  tested. The one named matter, the VMware backlog securities class action, **settled and was
  approved by the court in March 2025.**

### Name the specific way THIS business dies **[E2-27, E3-24]**

**[E4-40] observed: this list is built from what the filings show the business is EXPOSED to,
not from what has recently happened** â€” and what has recently happened is 86% revenue growth,
which [E4-40] calls *"not only useless, but actually dangerous"* as a guide.

**Mechanism 1 â€” the AI design wins go elsewhere, and they are now the majority of the
company. A REAL POSSIBILITY.** Q3 FY2026 AI semiconductor revenue was **$16.7bn â€” 56% of
consolidated revenue** â€” from a line that did not meaningfully exist three years ago, sold to
a handful of customers whom Broadcom's own risk factors describe as competitors: *"new
companies, **including some of our customers**, enter the markets."* **Quantified:** if the
guided Q4 FY2026 AI run-rate of $21.7bn/quarter halves, that removes **~$43.4bn of annualised
revenue**; at the semiconductor segment's 61% margin, **~$26.5bn of operating income â€”
more than Broadcom's entire FY2025 operating income of $25,484M.** Not a solvency event; a
complete removal of the Q5 case.

**Mechanism 2 â€” the tax holidays expire, on a published schedule. LIKELY, because it is
already written down.** Verbatim: *"These Singapore tax incentives are **scheduled to expire
through November 2030**. We have also obtained a tax holiday on our qualifying income in
Malaysia, which is **scheduled to expire in fiscal year 2028**â€¦ the effect of these tax
incentives and tax holiday was to **decrease the provision for income taxes by approximately
$2,709 million, $2,261 million and $2,104 million** for fiscal years 2025, 2024 and 2023."*
**$2,709M a year, with dates on it â€” 8.8% of trailing owner earnings, scheduled.** This is
the QTL expiry shape and it is the most certain negative in the file.

**Mechanism 3 â€” the software franchise is harvested rather than renewed. A REAL
POSSIBILITY.** Segment R&D at 9.4% of segment revenue and falling; contract liabilities down
from $14,495M to $13,016M; the repricing complete (+5.1% in H1 FY2026). **Quantified:** if
software growth goes to zero and margin reverts to FY2024's 65.1%, segment operating income
falls from $20,765M to ~$17,600M, **âˆ’$3,165M**.

**Mechanism 4 â€” the receivable concentration becomes a credit event. A LOW-LEVEL POSSIBILITY
for solvency, real for a quarter.** **One customer is 44% of net accounts receivable** (up
from 18%), i.e. ~$3,144M of $7,145M, and Broadcom's own words name the exposure: AI customers
*"seeking to lease AI racks or systems based on our XPUs instead of purchasing, as well as
alternative financings for such leases or other novel or deferred payment modelsâ€¦ may
increase our exposure to **credit or customer default risks**."*

**Solvency â€” essentially unnameable, and I tried. A LOW-LEVEL POSSIBILITY.** To kill Broadcom
the AI line and the software annuity would have to fail together while $67bn of debt came
due; the maturity ladder is long, current maturities are $3,152M, there are no financial
covenants on the notes, and there is $24bn of cash against $4,035M of twelve-month fixed
claims. **[E2-55]'s standard â€” acceptable results under extraordinarily adverse conditions â€”
is met on the balance sheet.**

**THE COMBINED CASE, PUT AS ITS HOLDERS WOULD PUT IT [E4-51].** Broadcom has been the best
capital allocator in this queue's experience: it bought a business earning 15.1% and made it
earn 76.8%, it repaid $30bn of acquisition debt in two years, it beat its comparator index in
all five 402(v) years by a widening margin, its owner earnings have compounded at roughly
**32% a year for nine years**, and its most recent quarter grew operating cash flow 98%. **The
bear case is not that this business fails. It survives comfortably; Q4 is an easy pass.** The
bear case is that **the majority of today's earnings comes from a two-year-old revenue line
sold to three or four customers who are each building the substitute, that the software half
has already been repriced once and is growing at 5%, that $2,709M a year of tax benefit
expires on a filed schedule between FY2028 and FY2030, and that the price capitalises all of
it as a permanent, still-compounding perpetuity.** That is the case its holders would accept
as fairly stated, and it is a **price** case, not a survival case.

- Likelihood: **[x] likely** (mechanism 2, which the filing dates) Â· **[x] a real
  possibility** (mechanisms 1 and 3) Â· **[x] a low-level possibility** (mechanism 4 and
  solvency)
- **VERDICT: [x] IN** â€” **GREAT on [E4-20], 3 of 3 on [E5-11], and the named deaths are
  specific, dated and quantified without any of them being a solvency event.**

---
â›” **Q1â€“Q4 each show IN. Q5 opens.**


---
## Q5 â€” WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Price $357.90** (2026-09-04, Yahoo, aggregator, flagged) Â· **shares 4,757,580,198** (hand-read
off the Q2 FY2026 10-Q cover) Â· **market capitalisation $1,702,738M** Â· **sovereign 5.24%**
(US Treasury 30-year, 2026-09-04, struck from the issuing authority).

**Judged owner earnings: $24,000M**, being the trailing twelve months to 2026-05-03 built
entirely from filed documents (FY2025 10-K + Q2 FY2026 10-Q; hand figure $23,977M). **Band
carried: $8,744M to $30,921M.** The judgment is disclosed and it is **generous**: it sits
above every multi-year window including the corpus's own five-year default ($14,975M),
because the five-year mean averages a company that no longer exists â€” pre-VMware and
pre-AI â€” with the one being priced.

**THE FLOOR, BEFORE THE RANKING [E4-28, E3-13].** *"that's the figure we quit on."*

**1. THE YIELD**

| construction | owner earnings $M | yield | vs sovereign |
|---|---|---|---|
| 5-yr D&A end (the conservative end) | 8,744 | **0.514%** | âˆ’4.73 pts |
| 10-yr capex end | 10,517 | 0.618% | âˆ’4.62 pts |
| **5-yr capex end â€” the corpus default [E2-42]** | **14,975** | **0.879%** | **âˆ’4.36 pts** |
| 3-yr capex end | 16,160 | 0.949% | âˆ’4.29 pts |
| FY2025 alone, capex end | 19,346 | 1.136% | âˆ’4.10 pts |
| **TTM to 2026-05-03, capex end â€” JUDGED** | **23,977** | **1.408%** | **âˆ’3.83 pts** |
| TTM to 2026-08-02 *(adds the furnished Q3)* | 30,921 | 1.816% | âˆ’3.42 pts |
| **Q3 FY2026 annualised â€” the most generous number constructible** | **46,584** | **2.736%** | **âˆ’2.50 pts** |

**There is no construction, on any window, at either end of the capex band, including the
single best quarter in this company's history annualised, that pays what a government bond
pays. The gap ranges from 2.50 to 4.73 percentage points.**

**2. WHAT THE PRICE ALREADY ASSUMES**

- To be worth $1,702,738M at the **bare sovereign** with no growth, owner earnings must be
  **$89,224M**. Against the judged $24,000M that is **3.72Ã—** â€” the price assumes a **272%**
  one-step increase.
- To clear the **[E4-28] 10% floor** with no growth, owner earnings must be **$170,274M** â€”
  **7.10Ã—**, a 610% increase.
- Stated as perpetual growth in owner earnings, which is the honest form:

| starting construction | g needed to be worth the price at the **5.24% bond** | g needed to deliver the **10% floor** |
|---|---|---|
| 5-yr capex end ($14,975M) | 4.36% forever | **9.12% forever** |
| **judged ($24,000M)** | **3.83% forever** | **8.59% forever** |
| fullest TTM ($30,921M) | 3.42% forever | 8.18% forever |
| Q3 annualised ($46,584M) | 2.50% forever | **7.26% forever** |

- **What the business has actually done: owner earnings grew from $2,009M (FY2016) to
  $30,921M (TTM to 2026-08-02) â€” roughly +32% a year for nine and three-quarter years**, with
  share count up 14.9% over the same span and almost all of that the single VMware issuance.
  **This is the fourth name after CTAS, GRMN and AAPL whose filed record exceeds its required
  rate, and here it exceeds it by roughly four times over. [E4-26] requires that to be the
  first sentence of the verdict, not a footnote.**

**3. WHAT YOU ARE PAID**

**âˆ’3.83 points versus the sovereign** at the judged figure; **âˆ’2.50 points** at the single
most generous construction that can be built from any document, filed or furnished.

### THE HONEST PRE-TAX EXPECTANCY, AND IT IS THE CLOSEST CALL IN THIS QUEUE

Expectancy is the starting yield plus sustainable growth. Building the growth from the parts
rather than extrapolating the past, which is what [E4-40] and [E4-41] require:

| component | share of the business | evidence | growth judged |
|---|---|---|---|
| Infrastructure software | 42% of revenue, 39% of segment profit | **+5.1% in H1 FY2026** after the repricing; R&D cut to 8.4% of segment revenue | **4â€“5%** |
| Semiconductor solutions | 58% / 61% | +127% now; arithmetically impossible to sustain â€” at +221% for three more years the AI line exceeds total world data-centre capital spending | **high, decaying, unknowable beyond a few years** |
| Tax holidays | â€” | **filed and dated: Malaysia FY2028, Singapore through Nov 2030, $2,709M/yr** | **âˆ’8.8% one-off â‰ˆ âˆ’1.5%/yr over five years** |
| Buyback lever | â€” | arithmetically capped at the earnings yield, **1.4â€“2.7%**, executed at ~$338 | small and shrinking |
| Acquisition lever | â€” | 19.0% pre-tax on the VMware money; the next deal must be ~$200bn to move the needle equally | bounded by target availability |

**Honest pre-tax expectancy: ~7.5%, range 6.5% to 9.2%.** And the precise statement of the
boundary matters more than the point estimate:

> **The [E4-28] floor is reachable at this price ONLY by stacking two generous assumptions:
> annualising the single best quarter in the company's history AND assuming 7.26% perpetual
> growth from that peak. Either one alone leaves the expectancy below 10%.** That is
> [E4-11]'s windage rule run in reverse â€” and the corpus's answer is [E4-18]: *"a conclusion
> that required fighting for it is worth less, not more."*

**Below roughly 10%, the name is not ranked â€” it is quit on, whatever the sovereign is
[E4-28].** The ranking lines below are therefore **not filled in**.

### THE CEILING, AND WHY THE GROWTH CASE CANNOT BE BOUGHT AT THIS PRICE [E4-44, E2-63]

At a 1.4â€“2.7% starting yield, **roughly 97% of what is being paid is terminal value.**
**[E4-44]:** *"the value of an asset, whatever its character, cannot over the long term grow
faster than its earnings doâ€¦ The Tinker Bell approach â€” clap if you believe â€” just won't cut
it."* The price does not merely require growth. **It requires that a revenue line barely
three years old â€” 56% of consolidated revenue in Q3 FY2026 â€” sold to a handful of customers
whom Broadcom's own risk factors identify as prospective competitors, and which sits squarely
in [E4-04]'s excluded class (a moat whose basis must be periodically replaced) and [E3-51]'s
surfing run, be capitalised as a permanent and still-compounding perpetuity.**

**And a filed fact that bounds the growth case from the company's own proxy.** The 2025 Tan
PSU Award, granted 2025-09-03, set *"formidable"* AI-revenue bars for **fiscal 2028â€“2030**:
threshold **$60bn** (pays zero), target **$90bn**, maximum **$120bn** â€” described then as
*"an increase of $100 billion over the forecasted fiscal 2025 AI Revenue"* of roughly $20bn.
**Twelve months later, fiscal 2026 AI semiconductor revenue is running near $57.7bn** ($10.8bn
in Q2, $16.7bn in Q3, $21.7bn guided for Q4) **and the guided Q4 exit rate annualises to
$86.8bn â€” 96% of the fiscal 2028â€“2030 TARGET, two full years before the performance period
opens, and 45% above the level at which the award pays nothing.** Two readings, both
recorded: the business has grown far faster than its own board forecast a year ago (real, and
bullish), **and** [E2-49]'s *"pre-set, long-lived and small bullseyes"* standard is not met by
a target nearly attained before its measurement window begins.

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]

*A discounted cash flow is run below purely as an **engine** to convert growth into a rate.
**It casts no vote** [E3-34].*

| construction | value | per share |
|---|---|---|
| judged OE, zero growth, at the 10% floor | ~$240,000M | **~$50** |
| fullest TTM OE, zero growth, at the 10% floor | ~$309,000M | ~$65 |
| judged OE, zero growth, at the 5.24% sovereign | ~$458,000M | ~$96 |
| fullest TTM OE, zero growth, at the sovereign | ~$590,000M | ~$124 |
| **engine: $30,921M growing 12%/yr for ten years, then 4% perpetual, discounted at the 10% floor** | ~$984,000M | **~$207** |
| **engine: the same at 15%/yr for ten years â€” a rate [E4-35] says fewer than 10 of the 200 most profitable companies achieve over 20 years** | ~$1,235,000M | **~$260** |

- **conservative ~$50â€“100 Â· optimistic ~$210â€“260 Â· JUDGED RANGE ~$100 to $260, centre ~$180**
- **CURRENT PRICE $357.90 â€” 1.99Ã— the judged centre and 1.38Ã— the most generous engine output
  the corpus's own base rate permits.**

**WHICH BAR:** **[x] Screamer test [E4-01].** Does the price already clear the **conservative**
case? **No â€” it is above the whole range**, which is outcome three. **No margin is added on
top; "startlingly low" is what you observe, not what you subtract.**
**Windage count: 1.** Conservatism is spent once, and it is spent **against** my own
conclusion: every figure above was run on the most generous owner-earnings construction
available, including a furnished quarter and an annualised peak.

- **VERDICT: [x] IN as an analysis, FAIL on price â€” the name is QUIT ON at the [E4-28] floor,
  not ranked.** Ranking position: **none â€” a name below the floor does not enter the
  ranking** [E4-28], so no comparison against the rest of the opportunity set is made.

## Q6 â€” WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*No position is taken, so this section is the pre-committed re-look, written now so it cannot
be rationalised later **[E1-02]** â€” *"I believe in establishing yardsticks prior to the act."*

**Pre-committed re-look level.** Judged value ~$180/share at a 5.24% sovereign, recomputed at
the rate of the day. **RE-OPEN BELOW ~$210** (a ~41% decline). **But the file is far likelier
to re-open on earnings than on price:** at $357.90 the floor requires **$170,274M** of owner
earnings against **$24,000M** judged â€” a **7.1Ã— gap** â€” and Broadcom is compounding owner
earnings fast enough that the arithmetic could close from the numerator.

**THESIS-CONFIRMING METRIC (pre-registered, so a bull outcome cannot be dismissed):**
**AI semiconductor revenue sustaining above a $60bn annual run-rate through fiscal 2028** â€”
the level the board itself set as the zero-payout threshold â€” **together with infrastructure
software returning to double-digit growth.** If both hold, the 8.59% perpetual requirement
stops looking heroic and this file should be re-run, not defended.

**THESIS-BREAKING METRICS AND THEIR THRESHOLDS:**
- **Semiconductor segment operating margin below 55%** for two consecutive quarters â€” the
  filed sign that the AI customers' *"greater demandsâ€¦ with regards to pricing and
  contractual terms"* have landed. (FY2023 58.5% Â· FY2025 57.6% Â· H1 FY2026 61.0%.)
- **AI semiconductor revenue growth turning negative sequentially** in any two consecutive
  quarters.
- **Infrastructure software revenue growth below 3%** year on year, or **segment R&D below 8%
  of segment revenue** â€” the harvest confirmed rather than suspected.
- **Contract liabilities falling for a third consecutive year** (14,495 â†’ 13,016 â†’ ?).
- **Any further [E2-49] withdrawal** â€” and specifically, if the **segment split itself** were
  ever consolidated or the top-five-customer percentage dropped, **Q2 moves to OUT, not
  NARROW.**
- **Buybacks continuing above ~$300/share.**
- **A new acquisition above ~$50bn**, which would restart the whole perimeter problem and
  reset every owner-earnings window.

**THE STRONGEST BULL SIGNAL, PRE-REGISTERED:** **if Broadcom begins FILING an AI revenue
line, or a unit/customer series, in a 10-K or 10-Q**, the [E4-52] convergence recorded at Q3
substantially dissolves and the disclosure half of the Q2 finding reverses.

**The monitoring question [E3-30, E4-17]:** is the software half's +5.1% an aberrational
pause after a step-change in pricing, or has the franchise slipped in a way that permanently
reduces intrinsic value? **One year of data cannot answer it and I do not pretend otherwise.**
*"beliefs change quite gradually"* **[E4-17]**.

**Position size [E3-45]: ZERO.** No position is taken. A capital-allocation flag is live
(buybacks at ~$338 against a judged ~$180), which would bind size downward even if the price
case cleared, which it does not.

**Catalysts:** the **Q3 FY2026 10-Q, due ~2026-09-09 â€” three days after this run** and the
first filed document to carry the quarter whose press release this file has had to rely on;
the **Q4 FY2026 results (~December 2026)**, which test the $34.8bn guidance; the **FY2026
10-K (~mid-December 2026)**, the single most informative document that will exist and the
place to check whether an AI revenue line is finally filed; the **Malaysia tax holiday expiry
in fiscal 2028**; and the opening of the 2025 Tan PSU Award performance period at the start
of **fiscal 2028**.

- **VERDICT: [ ] IN â€” not reached. The file closes at Q5, on price.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN Â· Q2 IN (NARROW) Â· Q3 IN
      (OVERLAY) Â· Q4 IN (GREAT) Â· **Q5 FAIL on price at the [E4-28] floor** Â· Q6 not reached.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The moat
      class is NARROW, not PROVISIONAL â€” the competitor row was obtained for 8 peers plus
      VMware standalone.
- [x] Every UNKNOWABLE states what specifically cannot be known: **VMware customer
      churn/renewal** (no filed metric exists in any vintage â€” no unit, seat, core, ARR,
      retention or renewal series), and **VMware's post-acquisition profit** (Broadcom states
      it is *"impracticable to determine"*).
- [x] Step 0: the filing was read, with accession numbers; SBC of $7,568M was cross-checked
      against the filed cash-flow statement and the $2M disagreement with the equity
      statement recorded.
- [x] Owner earnings on a multi-year mean; **six windows** stated; capex band disclosed as a
      judgment **with its direction named as INVERTED** (the D&A end is the conservative end).
- [x] Competitor row filled â€” 8 peers on the same metric, one (IBM) partially obtained and
      said so.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority, dated.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test), not both; windage count stated as 1.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git after every question.
- [x] **Operator rule 6 observed inside the run: two Q3 findings were reversed by the proxy
      and are corrected IN PLACE with the reversal stated, not silently edited.**

## REGISTER
- **Verdict: FAIL at Q5, ON PRICE, at the [E4-28] floor. All four business gates IN.**
- **One line: the best capital-allocation record this queue has examined, attached to a
  business that must compound owner earnings at 7.3â€“9.1% forever to pay 10% at $357.90, whose
  majority revenue line is three years old, unfiled, and sold to customers building the
  substitute.**
- **PRICE: $357.90** (2026-09-04). **Judged value ~$100â€“260, centre ~$180.**
- **PASS/FAIL: FAIL.** Q1 IN Â· Q2 IN Â· Q3 IN Â· Q4 IN Â· **Q5 FAIL (price)**.


---
## ADDENDUM TO Q3 â€” the second proxy sweep, 2026-09-06

*Added after Q3, Q4 and Q5 were written and committed. **It does not change the Q3 verdict
(IN, overlay, no disqualifier found) and it does not change Q5.** It is recorded as an
addendum rather than folded back into the Q3 section above, per operator rule 6: violations
and additions are corrected in an addendum, never by editing history. Source:
`_research 2026-09-06 AVGO/02`, DEF 14A accessions 0001193125-26-085691 / -25-044112 /
0001140361-24-009541, and the Item 5.07 8-Ks named below.*

### 1. SAY-ON-PAY â€” the largest single fact I did not have, and it is a shareholder verdict

From the Item 5.07 8-Ks reporting annual-meeting voting results:

| Meeting | For | Against | **For %** |
|---|---|---|---|
| **2024-04-22** (acc. 0001730168-24-000055) | 229,311,363 | 142,648,227 | **61.7%** |
| 2025-04-21 (acc. 0001730168-25-000037) | 3,387,380,526 | 274,703,048 | **92.5%** |
| **2026-04-20** (acc. 0001730168-26-000039) | 2,433,503,375 | **1,232,879,962** | **66.4%** |

**Two say-on-pay results in the sixties are a severe rebuke by any reading, and the pattern
is exact: the two low years are the two years that followed a mega-grant, and the quiet year
in between hit 92.5%.** Director Harry L. You drew **954,686,330 against-votes** in 2026
(74.0% for). **Hock Tan was re-elected with 99.7%.** *Shareholders are objecting to the pay,
not to the operator* â€” which is the same distinction [E5-38] draws and it is the right one.

This does **not** trip [E5-16]'s binary â€” an advisory vote on compensation is not personal
misconduct â€” but it is direct evidence on **[E3-59]'s second yardstick**, *"how well they
treat their owners"*, and it belongs beside the capital-allocation flag already raised.

### 2. THE BONUS PLAN â€” half the corporate goal is a company-defined non-GAAP measure

The APB Plan corporate goal is **50% revenue and 50% "Adjusted non-GAAP operating income (as
a % of revenue)"**, plus division metrics the proxy withholds as *"confidential and
proprietary"* and an individual multiplier of 50â€“150%.

**And it paid at the cap.** Revenue target **$57,294M** against actual **$63,887M**; adjusted
non-GAAP operating margin target 63.7%, **maximum 67.7%**, actual **68.0%**. Both components
**150%, capped** â€” the proxy states the actuals exceeded the pre-established target *and
maximum*. The maximum revenue bar was set at **+16.6%** over the prior year; the business
delivered **+23.9%**. NEO payouts 145% / 169% / 188% of target; the legacy relative-TSR PSUs
earned **200%** (above the 75th percentile of the S&P 500).

**This sharpens the Q3 finding rather than changing it, and the precise formulation is the
research file's:** *"non-GAAP" appears **0 times** and *"Adjusted EBITDA"* **0 times** in the
audited 10-K â€” **the non-GAAP apparatus lives in the proxy and the earnings 8-K, not in the
audited book.** [E4-29] does not fire on the filings and it does fire on the pay plan. Both
halves are true and both are stated.

### 3. ALIGNMENT â€” two facts that pull in opposite directions

- **Hock Tan owns 908,474 shares â€” approximately 0.019% of the company** â€” after grants whose
  aggregate grant-date fair value exceeds $400M, and while the 2023 award tracks at
  **maximum: 10,000,000 post-split shares, worth $3,696,300,000 at the FY2025 closing price
  of $369.63.** A chief executive being paid in options-like exposure while holding
  essentially none of the equity outright is a real observation about where the alignment
  sits â€” and it is precisely why the post-vesting holding requirement extracted for the 2025
  award (recorded at Q3) matters.
- **PLEDGING â€” a flag the FY2025 10-K sweep could not see.** Chairman **Henry Samueli pledged
  16,175,000 shares, worth roughly $2.7bn**, on 2024-11-15, for a property development, with
  board approval. Broadcom prohibits hedging; pledging is permitted by exception and this is
  the exception. Recorded as a flag, dated to when it became public, per the Q3 standard.
  It is not a disqualifier and it is not nothing.

### 4. WHAT THE SWEEP CLEARED â€” recorded because the negatives count too

- **Broadcom Inc. has NEVER filed a 10-K/A.** Two independent sweeps: the submissions JSON
  (988 filings, `filings.files` empty so `recent` is the complete record â€” eight 10-Ks, no
  amendments) and EDGAR browse by type. It does file 8-K/A, 3/A and 4/A, so the absence is
  not an artifact of the query.
- **Both FY2025 cover-page checkboxes are UNCHECKED** â€” error correction, and clawback
  recovery analysis.
- **PwC, auditor since 2006 (twenty years).** FY2025 fees: $18,093k audit, $0 audit-related,
  $1,994k tax, $10k other â€” **non-audit 10.0%**. Dual opinion on the statements and on ICFR,
  clean and unqualified. **One critical audit matter: VMware software and support revenue
  recognition on $27,029M of segment revenue, turning on the termination-for-convenience
  judgment** â€” the auditor independently identified the same line this run identified at Q2.
- **"except for" â€” one occurrence, and it is an ASC 805 policy clause, not an audit
  qualification. "adjusted" â€” eleven occurrences, all incidental** (split-adjusted,
  unadjusted quoted prices, adjusted career-average-pay pension, ASC 606 standalone selling
  price). **[E2-57] does not fire.**
- **Governance: eight directors, seven of eight independent, no classified board (all elected
  annually), and Tan is NOT Chairman** â€” Samueli holds an independent chair and CEO pay is
  set by the independent directors rather than the committee alone. **No excise-tax gross-ups,
  no single-trigger change-of-control, no option repricing or exchange (no options granted at
  all), hedging prohibited, 10D-1 clawback in place.** These are good and they are recorded.
- **Ownership: Vanguard 9.9%, BlackRock 7.3%; single class, one vote per share; 4,735,602,612
  shares outstanding at the record date. Berkshire Hathaway does not appear in the 2024, 2025
  or 2026 proxies.**

### 5. ONE FIGURE NOT OBTAINED, STATED AS UNRESEARCHED RATHER THAN INFERRED

The **post-split dollar levels of the 2023 award's stock-price hurdles**. Neither recent proxy
restates $825 / $950 / $1,125 on the post-split scale; a sweep for `82.50`, `95.00`, `112.50`,
`$825`, `$950`, `$1,125` and `470.12` returned **zero hits** in both. Rather than divide by ten
and present the result as filed, the run records what Broadcom does file on a split-invariant
basis: **CAGR Milestones of 11.9% / 15.1% / 19.1%.** *(Artifact that would resolve it: none
identified â€” the company appears simply not to have restated them, which makes this
UNKNOWABLE rather than UNRESEARCHED.)*

**The Q3 verdict is unchanged: IN, as a qualitative overlay, being the absence of found
disqualifiers and not a finding that the managers are honest [E5-17].** The flag list is now
heavier by two â€” **two say-on-pay votes in the sixties, and a $2.7bn Chairman pledge** â€” and
lighter by several â€” **no 10-K/A ever, a twenty-year auditor at 10% non-audit fees, an
independent chairman, no gross-ups, no single trigger, and a critical audit matter aimed at
exactly the revenue line this run questioned.**

