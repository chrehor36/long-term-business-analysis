
## UPDATE 2026-09-21 — FC (Franklin Covey): Q1 IN, Q2 OUT. Wave 7, name 12; register entry 144.

**Register counted before and after by line-start regex inside the slice from the `## COMPLETED FROM
THE QUEUE` heading line (502) to `## THE WRITE-EARLY PROTOCOL`: 143 before, 144 after, 144 distinct
tickers, no duplicate.** Price **US$17.27**, close of 2026-09-18, Yahoo chart endpoint, flagged,
raw response on disk. Shares **11,293,873** from the Q3 FY2026 10-Q cover (accession
`0001193125-26-297572`, as of 2026-06-30). **Cap re-struck by hand: US$195.0M against the screen's
$231M.** Sovereign **5.34%, 09/18/2026, US Treasury daily par yield curve**, struck fresh.
`tools/check_framework.py` **PASS before the commit**.

### The gate, in the filer's own words

Q2 fails **[E3-03]** criterion 2, and the strongest evidence is Franklin Covey's own 10-K. It names
**twenty-four competitors across nine categories** without being asked — McKinsey, Deloitte,
Accenture, Korn Ferry, Heidrick & Struggles, DDI, LHH, Blanchard, BetterUp, CoachHub, Ezra, RAIN
Group, Sandler, Challenger, Workboard, Amplify, Cornerstone, Udemy Business, LinkedIn Learning, and
five Education names. **A competitor list is not by itself a finding** — Coca-Cola names Pepsi — so
the run did not stop there. What makes it a finding is that FC's own ten *"principal competitive
factors"* include **"Competitive pricing"**, and that the customers then behaved like customers with
substitutes: *"many of our clients and prospective clients have sought to reduce their spending to
maintain profitability, which led to delayed decision making, decreased contract expansion, and
**lower client retention**."*

**[E2-44] fails on filed conduct.** In a year when demand was flat and capacity under-utilised, FC
did not raise price. It restructured — **$6,723k against $3,008k the year before** — while income
from operations fell from **$33,042k to $5,704k**, a 2.1% operating margin on $267.1M of revenue.
And **[E4-37]'s agony metric is filed as a risk factor in FC's own words**: *"we may shift the type
and pricing of our offerings, which may adversely impact client renewal rates."*

### The competitor row, and what it settles

EBIT ÷ (total assets − current liabilities), each from the peer's own 10-K, twelve years where
reachable. **The peer set is derived from FC's own competition disclosure**; of its twenty-four
names only four file with the SEC, and Skillsoft and Coursera are added as the listed form of the
learning-library class FC does name, with that said rather than hidden.

| | 12-year mean EBIT/capital employed |
|---|---|
| **FRANKLIN COVEY** | **10.9%** (four years below 3.1%, two negative) |
| Accenture | **33.9%**, never negative in twelve years |
| Korn Ferry | **10.1%** |
| Heidrick & Struggles | **7.8%** |
| Udemy / Coursera / Skillsoft | **negative in every filed year** |

**FC's twelve-year return on capital employed is Korn Ferry's, and a third of Accenture's.** The
loss-making library class is the other half of the answer: it says the content library alone is
worth nothing and **the consultants are what is being sold** — which is why FC's economics are a
consulting firm's economics and not a franchise's. And the FY2022–FY2024 run of 22.5 / 28.0 / 33.3%
is partly denominator, not business: **capital employed fell from $162.3M (FY2014) to $85.6M
(FY2025), −47%**, on $289,933k of treasury stock against $66,911k of equity — **[E2-47]**'s carve-out
applied rather than cited.

### Direction, on four independent filed series [E4-32]

1. **Revenue** $287,233 → $267,067 (−7.0%), with FY2026 guidance **cut** on 2026-07-01 to
   *"$260 million to $267 million"*. From FY2019's $225.4M to the FY2026 midpoint is **16.9%
   nominal over seven years, below CPI — in real terms this business has not grown since 2019.**
2. **Units, where units exist [E4-55].** New Leader in Me schools: **739 (FY2022, which the FY2022
   10-K calls "a record") → 728 (FY2024) → 624 (FY2025), −14%.** Enterprise publishes **no unit
   metric at all** — only the dollar word *"invoiced"*, which is exactly the substitution [E4-55]
   warns about.
3. **Operating margin** 11.5% → 2.1% on a 7% revenue fall. **[E2-58]**'s shape.
4. **The retention metric was withdrawn.** FY2021: *"annual AAP revenue retention remained above 90
   percent for the year."* FY2022: *"remained well above 90 percent."* FY2024: *"greater than
   90%."* **FY2025: no number**, replaced by *"the majority of our clients are renewing"* — in the
   same document that concedes *"lower client retention."*

**[E4-36]/[E3-51]: the FY2022–FY2024 run reads as wave-riding**, not position — a subscription
conversion, a shift to digital delivery and suppressed travel cost arriving together, with the
deferred-revenue increment at its filed maximum in FY2021. FY2025 and three quarters of FY2026 are
the shallows: operating cash $60.3M → $29.0M → **$17.5M for nine months**.

### THE SCREEN'S BAND WAS THE WINDOW, NOT THE CONSTRUCTION — eighteen years rebuilt

`spread_caveat` said the $24–31M band was a four-construction width over five years and *"cannot
see variation older than the 5-year window."* **Rebuilt FY2008–FY2025 — eighteen consecutive fiscal
years — by hand from the cash-flow statements of eight 10-Ks**, overlaps agreeing year by year.

| window | OE, (c)=D&A | OE, (c)=capex |
|---|---:|---:|
| FY2021–FY2025 (the screen's) | $22.8M | **$25.4M** — reproduces the screen's $24M bottom |
| FY2016–FY2025 | $15.6M | $19.2M |
| FY2008–FY2025 (everything filed) | **$9.5M** | $13.3M |

**The construction was never in dispute; the window was.** Two of the screen's five years are the
two best in eighteen and a third carries the largest deferred-revenue increment ever filed. Combined
range carried as **$9.5M to $25.4M, a factor of 2.7** — and **`level_shift 1.31 (no step)` and
`best_year_dep 0.09 ("no single-year dependence")` are both false on the rebuilt series**: the step
is FY2020→FY2021 at **1.79x** and it did not hold, and **FY2024 alone is 30.6% of the five-year
owner-earnings sum.**

### Tooling defects found — three, and two are new classes for this project's record

**1. THE CAPEX IS SPLIT ACROSS A US-GAAP TAG AND A COMPANY EXTENSION, AND `companyfacts` CARRIES
ONLY THE FIRST.** FC's investing section has three capitalised lines; only *Purchases of property
and equipment* is `PaymentsToAcquirePropertyPlantAndEquipment`. *Capitalized curriculum development
costs* is **`fc:PaymentsForCurriculumDevelopmentCosts`**, and **SEC companyfacts carries no custom
taxonomy namespace at all** — FC's file has none. **Measured: FY2025 capex is $16,888k filed against
$8,253k visible (49%); FY2023 $13,550k against $4,515k (33%); over eighteen years the screen sees
$67.4M of $149.1M — 45%.** Same class as the Marvell capitalised-IP-licence limit already on the
record: **a source limit, not a bug** — no tag rule recovers a number the filer did not tag to a
standard element. **The company's own Free Cash Flow definition agrees with the reader and not with
the screen**: *"cash flows from operating activities less capitalized expenditures for purchases of
property and equipment, **curriculum development**, and content or license rights."* **The class to
watch for is any content, media, publishing or curriculum business that capitalises its product
development under an extension element.**

**2. THE D&A TAGS RESOLVE TO A THIRD OF THE FILED CHARGE.** `DepreciationDepletionAndAmortization`
and its siblings return **$4.1M for FY2025** against a filed **$8,458 + $4,440 = $12,898k**, because
FC splits *Depreciation* and *Amortization* on the face of the income statement and tags the
cash-flow add-backs separately. **A run using the undimensioned fetch would have set (c) at a third
of its true default and overstated owner earnings by roughly $8M a year** — the same shape as the
SBC-of-zero defect, in the (c) input rather than the SBC input, and pointing the same dangerous way.

**3. THE CAP IS STRUCK OFF THE ANNUAL COVER SHARE COUNT WHEN A NEWER 10-Q COVER COUNT EXISTS.**
The screen used 12,155,832 (FY2025 cover, as of 2025-10-31) when the Q3 FY2026 cover carried
**11,293,873 as of 2026-06-30 — 7.1% lower**. The `newest_periodic` column already knew the later
periodic existed. On a filer retiring ~5% of its shares a year this overstates the cap on every row.
**The error points the wrong way — it makes names look dearer than they are — so it will have
suppressed candidates rather than promoted them**, which is the benign direction but still a wrong
number in a ranking.

### Screen flags — one right, three wrong or incomplete

- **`cap_flag` WRONG BY 18%, and it is the CALM / EMBC / BRBR branch, not a fifth.** Float $349.5M
  at $31.98 on 2025-02-28 is right (the aggregator reproduces that close to the cent, which is an
  independent check **on the filing**); the affiliate block is only ~8–10% and there is no control
  block. **The whole of the 1.51x is nineteen months of price: −46%.** The MGPI run's proposed
  rewording is seconded: the diagnostic should say *"or the two dates differ."*
- **`wc_note` RIGHT — the first time in four runs.** Every FY2021 working-capital line was ranked
  with its sign: deferred revenue **+$19,788k, +42.9% of OCF, and it genuinely PRODUCED the cash**;
  the next largest are accounts payable +31.1% and receivables −30.9%. **The EMBC / MCFT / BRBR
  inversion pattern does not reproduce.** The honest standing instruction is to rank every line
  every time, not to expect inversion — a prior corrected in the direction of less confidence.
- **`acq_note` empty is FALSE; the diagnostic is now 0 for 4** (CGNX, CE, MGPI, FC). **Nine
  acquisitions in the filed window totalling ~$41.6M** against a $195M cap.
- **`deal_note` empty is TRUE for a live deal but INCOMPLETE for the perimeter.** No merger form
  anywhere, and the five Item 8.01 8-Ks of the last year are **conference-call scheduling
  notices** — one was opened rather than assumed. But two perimeter events sit inside the window
  that no flag saw: the **FY2008 sale of the Consumer Solutions business unit** ($28,241k proceeds,
  $9,131k gain — which is why FY2008 owner earnings are near zero and the eighteen-year series is
  not like-for-like at its left edge) and the **FY2025 conversion of the France licensee to a
  directly owned office**.
- **`name_change_note` empty is GENUINELY CORRECT, and was checked in the filing history rather
  than the field.** `formerNames` is **not** empty (*FRANKLIN QUEST CO*, to 1997-02-11) but falls
  outside the detector's 2017 window. **CIK 0000886206 and file number 001-11107 carry unbroken
  through the 1997 Covey Leadership Center merger — a rebrand, not a Rule 12g-3(a) successor
  substitution — and eleven years before the earliest year in the series. The BRBR defect class
  does not reproduce here**, which is the first negative result recorded against it.

### The refuted and confirmed priors

- **CONFIRMED:** FC sells corporate training and leadership development and has moved to a
  subscription form. **CONFIRMED and larger than briefed:** the `ContractWithCustomerLiability`
  flag and the deferred-revenue-funded operating cash line **are the same fact**, and the
  subscription transition **did** produce the predicted non-GAAP shape — *"subscription revenue
  invoiced"*, *"deferred subscription revenue"*, *"unbilled deferred revenue"*, and an Adjusted
  EBITDA headline.
- **REFUTED:** that a 16-year filing history with a $231M cap implies concentrated ownership. The
  proxy shows no control block and the float is ~90% of the shares.
- **REFUTED:** `years_filed: 16`. **Eighteen consecutive 10-Ks are on the index (FY2008–FY2025)**
  and eighteen fiscal years of cash-flow statements are reachable from eight of them.

### Beneath the close, seen and not scored

**[E4-29] fires at a scale worth recording, and ONLY the EX-99.1 shows it.** The Q3 FY2026 release
headline block is five bullets in ascending order of goodness, ending *"**Adjusted EBITDA Increases
14% to $8.3 Million**"*. The CFO's quote leads with it. **The guidance is given in it.** The segment
note reports in it. **And management is paid on it** — the proxy names *"Qualified Adjusted EBITDA"*
as the Company-Selected Measure and says it *"comprises the largest portion of the performance
metrics for determining our LTIP and STIP awards."* **FC's definition deletes depreciation and
amortisation, stock-based compensation AND restructuring — three things the corpus names as real
expenses in three separate places [E4-29, E5-06, E3-53/E5-33] — a ~$25.4M wedge between FY2025
Adjusted EBITDA of $28.8M and income from operations of $5,704k.** And the mechanism the flag exists
to catch sits in the same release: **while Adjusted EBITDA rose 14%, operating cash fell to $1.1M
from $6.3M, free cash flow was $(1.0)M against $2.8M, and cash fell to $12.0M from $33.7M.** A run
that read only the annual report would have missed the headline block entirely — **the standing rule
to pull the latest EX-99.1 earned its keep here.**

**[E2-49] fires, and my prior now stands at SEVEN FIRES AND FIVE FAILURES** (SHOP, MRVL, PAY, ARM,
CALX, BE, FC against QLYS, CRM, CORT, PLTR, INOD). **The candor case of the same family is recorded
beside it [E4-26], because hunting disconfirming evidence is the rule**: PSUs vested through FY2024
on *"the highest rolling four-quarter Adjusted EBITDA performance within the three-year cycle"* — a
**high-water mark**, so the FY2023–25 cycle paid against **$56.0M while FY2025 actual was $28.8M** —
and **FC redesigned it ahead of the deterioration** to cumulative revenue and EBITDA over FY2025–27.
Further evidence against the harsh reading: **the bad year was not paid** (*"resulting in no payout
for the financial component of the STIP for the NEOs"*), **upside was cut in advance** from 200% to
150% of target with reasons given, and **[E4-30] does not fire in either direction** — reported
growth is conspicuously *un*smooth and **cash taxes are rising** ($3,308 → $4,205 → $7,693) against
falling pretax income.

**The buyback is the largest decision this management makes, and both [E5-08] conditions are live.**
FY2023 through three quarters of FY2026: **$120,796k gross, less $5,422k of reissue proceeds =
$115,374k net, for a share count from 13,853k to 11,293,873 — 2,559k net shares, $45.09 of net cash
per net share retired, against $17.27 on 2026-09-18** [E5-24]. On condition (1): in nine months FC
generated $17,476k of operating cash and $8,477k of free cash flow and spent **$28,118k** on
buybacks; **cash fell $31,698k → $11,972k**; [E5-39] refuses to count the $62.5M revolver and **FC
has published no liquidity floor** [E5-25]. The Board replenished the $50.0M authorisation on
2025-08-11 and **three days later**, on 2025-08-14, FC *"initiated a 10b5-1 plan to purchase up to
$10.0 million of our common stock through daily purchases."* Humility clause attached [E4-13].

**The named death, quantified [E2-27, E3-24, E4-40].** One hundred percent of revenue is a
discretionary line in somebody else's budget, sold by a fixed salesforce against twenty-four named
alternatives and a zero-marginal-cost substitute. **SG&A is 89.7% of gross profit. A second −7.0%
year removes $14.3M of gross profit against $5.7M of operating income — an $8.6M operating loss
unless costs come out first — and a −2.8% year takes operating income to zero.** Not hypothetical:
**FY2017–FY2020 were four consecutive net-loss years in this same filing history.** **Likelihood: a
real possibility.** It does not kill the company — no debt, no maturity, customers prepay — **it
returns FC to what it was between 2017 and 2020: a going concern earning nothing for its owners for
several years at a stretch.**

**And the uncomfortable part, written down rather than hedged, as the MGPI fold did: THE PRICE WAS
NEVER THE PROBLEM AT THE TOP OF THE RANGE.** On the re-struck $195.0M cap, owner earnings of
$9.5M–$25.4M are a **4.9% to 13.0%** yield against a **5.34%** sovereign. **The screen's own
five-year window clears the ~10% floor at 13.0%**; the ten-year (8.0–9.8%) and the eighteen-year
(4.9%) do not. **The file closed anyway, and it closed on the business** — which is the framework
working in the order it is written [E5-42, E2-31]. Had the gates cleared, a range straddling the
floor by a factor of 2.7 is **[E4-25]**'s *"no useful conclusion"* and that would itself have been
the verdict. No bar chosen, no margin applied, **windage count 0**.

### What was NOT done, and why

- **No `tools/alerts.json` band and no `PORTFOLIO.md` row.** The QLYS ruling: a name that failed on
  the business does not get a price alert. **The reversal condition is recorded in words instead**:
  (1) a filed price increase taken and held with retention intact; (2) AAP revenue retention
  published as a number again above 90%; (3) two consecutive years of revenue growth above CPI;
  (4) EBIT on capital employed durably above Korn Ferry's and Heidrick's across a full cycle rather
  than for the three years of a wave. **The way back in is a franchise finding, not a cheaper
  price** — carried openly against **[E3-47]**, because FC is squarely inside the circle of
  competence and a wrongly-closed file there is the expensive error class.
- **No survival shape counted in `Screens/SURVIVAL SHAPES - index.md`.** The run's reading is the
  wave shape with a customer-funded balance sheet, but **the file closed at Q2 and Q4 was never
  reached as a gate**, so on the PAGP precedent of 2026-09-20 and the MGPI fold of 2026-09-20/21
  this is **the signature without the verdict** and is deliberately not counted as an instance.
- **Nothing in `Framework/`, `CLAUDE.md` or `principle_ledger.csv` was edited by this run.**
- **No tool was changed.** The three defects above are recorded, not patched: two are source limits
  that no tag rule can repair, and the third (the share-count vintage) touches the pricing of every
  row in the queue and is therefore the operator's call, not a run's.

### Acceptance test and the pointer

`python tools/check_framework.py` **PASS before the commit** — 0 phantom citations, 0 unlabelled
numbers, every ledger row verbatim against its cited source. **Every ledger id cited in the run file
was then checked directly against `principle_ledger.csv`: 93 distinct ids, 0 phantom.** Two quotes
were tightened to the ledger's own wording before the commit rather than left as the framework
renders them — **[E5-39]**'s *"available cash or credit is a lot like oxygen"* and **[E4-20]**'s
*"grows rapidly, requires significant capital to engender the growth, and then earns little or no
money"* — PRIME RULE 1 and PRIME RULE 2, the text wins. **`CLAUDE.md` still says the ledger is 267
rows; the file is 311 data rows. Ninth consecutive wave-7 fold to record that stale pointer, which
remains the operator's call and not a run's.**
