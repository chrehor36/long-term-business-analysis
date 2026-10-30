# Company Run — Honeywell International Inc. / Honeywell Technologies (HON) — 2026-09-01
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**POSITION NOTE, declared before any verdict:** the operator holds **no HON position**. This
was opened as a fresh entry run from the corrected floor screen
(`Screens/2026-09-01 FLOOR SCREEN.csv`, COMPUTATION only), which put HON at a **6.36%
bottom-boundary owner-earnings yield against a 5.18% sovereign, needing ~3.64% perpetual
growth** to reach the [E4-28] floor, on a 6.9% window spread. The operator's instruction was
to find out first whether an artifact the screen cannot see had destroyed that number, as it
did for HOG (segment mixing), VZ (indefinite-lived intangibles) and WGO (boom backlog).
**It had. The run stops at Stage 0.** Format precedent read: `Test Runs/2026-08-31 Run - ITW
(Illinois Tool Works) v4.1.md` only.

**BIAS DECLARATION [rule 9, E4-27, E4-26, E3-41].** Three pulls, named before the work started.
(1) **The brief itself framed HON as a name that might survive.** A screen row that reads
"+1.18 points over the sovereign" invites the analyst to look for reasons it is real. The
antidote applied was to compute the market cap and the owner earnings from **the same
perimeter** before anything else, which is where the whole file turned.
(2) **"Mid-breakup" is a story, and stories are where windage hides.** The operator's brief said
HON "has announced separation into Aerospace, Automation and Advanced Materials." The filed
record says the separation is **finished** — Solstice spun 2025-10-30, Aerospace spun
2026-06-29 — and I had to correct the brief's premise before I could use any of it. Recording
that here rather than quietly, because a run that silently repairs its instructions is a run
whose reader cannot check it.
(3) **A "no" is a fully successful run.** So is a "yes." Neither was decided in advance, and
the corrected arithmetic below was computed once, from the company's own filed guidance and
from two independent routes, and not re-cut when it came out badly.

Analyst inputs beyond the filings: `Test Runs/_research 2026-08-26/HON evidence pack +
competitor row (RTX, GE, EMR, ABB).md` (built alongside this file; **not load-bearing on any
finding below, because the run stops before Q2 opens**).

---
# STAGE 0 — FIVE-MINUTE ARTIFACT CHECK
*Reported before the framework opens, per the operator's instruction. Three legs; if any fails,
record it and stop without the full run.*

## THE HEADLINE, BEFORE THE THREE LEGS

**The company the screen measured no longer exists.** On **2026-06-29** Honeywell International
Inc. completed the spin-off of Honeywell Aerospace Inc. (Nasdaq: **HONA**), distributing one
HONA share for every two HON shares held at the 2026-06-15 record date, and on the same day
effected a **one-for-two reverse stock split**. Honeywell International Inc. now operates as
**Honeywell Technologies**, a three-segment automation company. Verbatim, from the newest filed
document (Form 10-Q, quarter ended 2026-06-30, filed 2026-07-23, accession
**0000773840-26-000124**):

> "In the third quarter, Honeywell International Inc. (we, us, our, Honeywell Technologies, or
> the Company) completed the previously-announced separation (the "Aerospace Spin-Off") of
> Honeywell Aerospace Inc. … **Following the Aerospace Spin-Off, Honeywell International Inc.
> now operates as Honeywell Technologies.** … Following the Aerospace Spin-Off, the historical
> financial results of Honeywell Aerospace **will be reflected in Honeywell Technologies'
> consolidated financial statements as discontinued operations**."

**The screen's numerator is the old company and its denominator is the new one.** The
owner-earnings figure of $4,384M is the FY2021–FY2025 mean of consolidated Honeywell —
including Aerospace Technologies (spun 2026-06-29), Advanced Materials / Solstice (spun
2025-10-30), Quantinuum (deconsolidated at IPO 2026-06-04) and the PPE business (sold 2025).
The market cap of $68,912M is Honeywell **Technologies**, on 2026-09-01, after all four left.
That is not a distortion inside a number. It is two different companies on either side of a
division sign.

## (a) TOTAL economic shares, from the NEWEST filed cover — **PASSES on the cap; and the 10-K cover is 100.5% wrong**

- **Q2 2026 10-Q cover (filed 2026-07-23):** "There were **316,940,010 shares of Common Stock
  outstanding at June 30, 2026**." **This is the figure used.**
- **FY2025 10-K cover (filed 2026-02-17, accession 0000773840-26-000013):** "There were
  **635,675,701 shares of Common Stock outstanding at January 23, 2026**." Note 22:
  "As of December 31, 2025, and 2024, the total shares outstanding were 635.3 million and
  649.8 million."
- **The gap is not drift; it is the reverse split.** Note 1 to the 10-Q: "During the second
  quarter of 2026, the Company's Board of Directors approved a **one-for-two reverse stock
  split** … In the third quarter on **June 29, 2026**, following the Aerospace Spin-Off …
  the Reverse Stock Split became effective. … **All share and per share amounts have been
  retrospectively adjusted.**" The 8-K of 2026-06-29 (accession 0000773840-26-000084, Exhibit
  99.1) states it in cash terms: "**reduced the number of issued and outstanding shares … from
  approximately 634 million as of March 31, 2026 to approximately 317 million.**"
- **Single class confirmed.** Preferred stock is authorised and unissued. Note 14 to the 10-Q is
  a plain two-line basic/diluted EPS computation with no two-class method, no participating
  securities, no tracking stock, no convertible. Securities registered under 12(b): Common Stock
  (HON) plus five series of Euro notes.
- **Total economic shares = 316,940,010. Market cap = 316,940,010 × $213.22 = $67,577M**
  (price 2026-09-01, aggregator, live quote only, flagged; prior closes $213.53 on 08-31,
  $220.39 on 08-27).
- **Why this leg still passes.** The screen's `shares_asof` resolved to **(2026-06-30,
  316,940,010)** — the correct post-split count from the correct cover — and the split guard
  correctly declined to apply the 2026-06-29 event because it precedes the measurement date. The
  screen's $68,912M cap is right, to within the price used. **Three runs have now found stale
  10-K covers; this is the first to find a cover that is stale by a factor of two, and the
  house rule caught it.** Recorded as a pass with the mechanism named, because an analyst who
  had taken the 10-K cover at face value would have doubled the market cap and halved every
  yield in this file.
- **What is NOT current:** the balance sheet. The 10-Q balance sheet at 2026-06-30 (total assets
  $77,344M, equity $18,857M) still consolidates Aerospace, because the fiscal quarter closed
  **June 27** and the spin was **June 29**. The only post-spin balance sheet in the filed record
  is the **unaudited Article 11 pro forma at 2026-03-31** (8-K 2026-06-29, Exhibit 99.3).

## (b) Dividend, regular versus special, DECOMPOSED — **FAILS the mandate test, and it is the most extreme result of the eleven names run through this decomposition**

**Declared dividends per share, from each year's own filed Statement of Shareowners' Equity**
(pre-reverse-split basis, as filed; FY2021 10-K accession 0000773840-22-000018, FY2023 10-K
0000773840-24-000014, FY2025 10-K 0000773840-26-000013):

| 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 rate |
|---|---|---|---|---|---|---|---|
| 3.36 | 3.63 | 3.77 | 3.97 | 4.17 | 4.37 | **4.58** | 4.76 |

- **No special dividend anywhere in the filed record. No cut. No flat year.** Successive raises
  +8.0%, +3.9%, +5.3%, +5.0%, +4.8%, +4.8%, then +3.9% for 2026. Cash dividends paid rose every
  year: $2,442M (2019) to **$2,976M (2025)**. The record is clean and it is long.
- **The screen's 3.86% five-year rate is not reproducible from the filings and is understated.**
  The filed five-year rate is **+4.76%/yr** (2020 $3.63 → 2025 $4.58) and the six-year rate is
  **+5.30%/yr** (2019 $3.36 → 2025 $4.58). Likewise the screen's 2.04% dividend yield pairs a
  **pre**-split annual rate (~$4.44) with a **post**-split price; on a like-for-like basis the
  pre-spin yield was ~4.2%. Both discrepancies are recorded and neither is load-bearing, because
  the forward rate is the live question (below).

**The decomposition, 2019 → 2025 — six years, avoiding the 2020 trough as base.** Diluted EPS
and diluted share counts are as originally filed in each year's 10-K.

| driver | rate | share of the +5.30%/yr dividend growth |
|---|---|---|
| Net income $6,143M → $4,729M | **−4.27%/yr** | **−84%** |
| Share retirement, diluted 730.3M → 642.8M | **+2.15%/yr** | **+41%** |
| Payout-ratio expansion, 40.0% → 62.2% of diluted EPS | **+7.66%/yr** | **+143%** |

Diluted EPS went **$8.41 → $7.36, −2.20%/yr**, while the dividend grew +5.30%/yr. On the
five-year window the answer is the same shape and only slightly kinder: earnings **−4%** of the
growth, share retirement **+43%**, payout expansion **+61%**.

**So: every cent of Honeywell's dividend growth over six years came from buying back stock and
raising the payout ratio. Earnings contributed negatively.** Eight of the previous ten names
tested had the compounder label overturned by this decomposition and two (RPM, SHW) had it
confirmed. **HON is the first where the earnings term is not merely small but negative over a
six-year window that contains no pandemic base.** The label is overturned.

**Cash dividends as a share of owner earnings, then and now** (screen construction, old
perimeter: OCF − SBC − D&A):

| | owner earnings | cash dividends | payout | + buybacks |
|---|---|---|---|---|
| FY2019 | $5,656M | $2,442M | **43.2%** | 121% |
| FY2025 | $4,824M | $2,976M | **61.7%** | 141% |
| **Honeywell Technologies today, unchanged rate** | **$1,330M (bottom boundary, below)** | **$3,017M** | **227%** | — |

**And the forward rate is not in the filed record.** The last declared quarterly rate is **$2.38
per post-split share** (10-Q Statement of Shareowners' Equity, three months ended 2026-06-30),
which annualises to $9.52 per share, **$3,017M a year on 316.94M shares**. That rate was set by
the pre-spin company and is **227% of Honeywell Technologies' bottom-boundary owner earnings and
147% of its entire guided operating cash flow.** It cannot be paid. Neither the 2026-06-29
spin-completion 8-K, the 2026-07-23 Q2 8-K, nor the 2026-08-19 8-K declares a post-spin rate,
and no 8-K has been filed between 2026-08-19 and 2026-09-01.
**UNRESEARCHED at the metric level. Artifact: the Board's Q3 2026 dividend declaration
(HON has historically declared with the late-September board meeting and files it on Form 8-K
Item 8.01), and failing that the Q3 2026 Form 10-Q, due approximately 2026-10-22.**
**Leg (b) fails: the mandate is "a dividend payer that compounds," and what the filed record
shows is a payer whose growth was 100% levers and whose current rate is about to be cut by an
amount nobody has yet published.**

## (c) Boom/bust-window artifact [E4-41], and the separation treatment — **FAILS, and this is the leg that closes the file**

### The screen's number, reproduced exactly, so the failure is checkable

Five-year window FY2021–FY2025, SEC companyfacts, each figure as originally filed:

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | 5y mean | 3y mean |
|---|---|---|---|---|---|---|---|
| Operating cash flow (total, incl. discontinued) | 6,038 | 5,274 | 5,340 | 6,097 | 6,408 | 5,831.4 | 5,948.3 |
| Stock compensation | 217 | 188 | 202 | 194 | 196 | 199.4 | 197.3 |
| D&A | 1,138 | 1,204 | 1,176 | 1,334 | 1,388 | 1,248.0 | 1,299.3 |
| Capital expenditures | 895 | 766 | 1,039 | 1,164 | 986 | 970.0 | 1,063.0 |

- OE (5-year, D&A end) = 5,831.4 − 199.4 − 1,248.0 = **$4,384M** ← the screen's bottom boundary
- OE (3-year, capex end) = 5,948.3 − 197.3 − 1,063.0 = **$4,688M** ← the screen's top boundary
- 4,384 ÷ 68,912 = **6.36%**; spread 6.9%. **Both boundaries reproduce to the dollar.** The
  screen did its arithmetic correctly. The inputs were the wrong company's.

### Three defects, in ascending order of size

**1. One-time cash items inside the window [E4-41], all disclosed and all large.** The FY2025
10-K's own cash-flow statement carries them as named reconciling lines:
- **+$1,590M, FY2025** — MD&A: "**receipt of the Resideo indemnification and reimbursement
  agreement termination payment of $1,590 million**." The note is explicit about what was sold:
  "the Company received a one-time cash payment of $1,590 million **in lieu of all future
  payments** … As a result of the termination agreement, **Resideo no longer has any obligation
  to make cash payments to Honeywell** in respect of Honeywell's net spending for environmental
  matters." Reimbursements had been running **$105M in 2025**. So the window contains a
  $1.59bn inflow **and** the permanent loss of a ~$100M-a-year recurring one.
- **−$1,428M, FY2025** — "**On September 29, 2025, the Company permanently divested all of its
  legacy Bendix asbestos liabilities and certain non-Bendix asbestos liabilities, contributing
  $1.4 billion in cash** and transferring asbestos liabilities to a third party entity. As part
  of the agreement, the Company will be indemnified from future asbestos claims."
- **−$1,325M, FY2023** — the NARCO Buyout payment.

Net across the window: **−$1,163M**, so on the five-year mean these items **depress** the
screen's figure by ~$233M/yr. Stripping them raises the old-perimeter number. **They are named
here rather than used, because the perimeter defect below makes the old-perimeter number
irrelevant either way.**

**2. The window mixes perimeters even within the old company.** FY2021 and FY2022 operating cash
flow as originally filed consolidates Advanced Materials; FY2023 and FY2024 as originally filed
also consolidate it (Solstice became discontinued only from Q4 2025); the FY2025 10-K then
restates 2023 and 2024 downward. A five-year mean built from as-filed vintages therefore adds
years whose contents differ. The restated continuing-operations series in the FY2025 10-K is
**$4,459M (2023) · $5,112M (2024) · $6,075M (2025)** against total-including-discontinued of
**$5,340M · $6,097M · $6,408M** — a difference of $881M, $985M and $333M.

**3. The perimeter defect that decides the file.** Both the above are second-order. The
first-order fact is that **Aerospace is gone**, and Aerospace was the majority of the earnings.
From the Article 11 pro formas filed as Exhibit 99.3 to the 8-K of 2026-06-29:

| $M | FY2023 | FY2024 | FY2025 | Q1 2026 |
|---|---|---|---|---|
| Net sales, as reported | 33,009 | 34,717 | 37,442 | 9,143 |
| less Aerospace discontinued operations | (13,602) | (15,436) | (17,497) | (4,320) |
| **Net sales, pro forma (Honeywell Technologies)** | **19,407** | **19,281** | **19,945** | **4,823** |
| Pre-tax income from continuing ops, as reported | 6,191 | 6,244 | 5,476 | 886 |
| less Aerospace | (4,163) | (4,363) | (4,172) | (983) |
| **Pre-tax income, pro forma** | **2,028** | **1,881** | **1,686** | **(17)** |
| **Net income from continuing ops attributable to Honeywell, pro forma** | **1,236** | **1,302** | **1,368** | **120** |

**Aerospace was 67% to 76% of consolidated pre-tax income in every year of the window.** The
screen's $4,384M of owner earnings was earned mostly by a business that HON shareholders no
longer own through HON — they own it directly, as HONA.

### How this run treats separation cash flows, gains and stranded costs

Stated explicitly, per the operator's instruction, with the CSL divestiture run as precedent:
1. **No gain on separation or deconsolidation is treated as earnings.** The $6,629M gain on the
   Quantinuum deconsolidation (Q2 2026) is non-cash, is removed on the cash-flow statement, and
   is excluded from every figure here. So is the $724M goodwill impairment and the $270M
   held-for-sale impairment (2025), and the $1,651M spin-off charge to retained earnings.
2. **Pre-separation funding is financing, not earnings.** $1,962M in FY2025 (Solstice) and
   $15,835M in H1 2026 (Aerospace's $16.0bn note issue, of which $9.1bn of cash and $6.0bn of
   exchange notes came to Honeywell Technologies, which used $13.0bn to repay third-party debt).
   None of it is in owner earnings; the interest saved **is**, and the pro forma quantifies it at
   **$212M a year**.
3. **Separation cost payments are real costs and are counted [E5-33].** The company guides
   **~$0.4bn** of spin-off and separation-related cash cost payments in FY2026 and adds them back
   to its "free cash flow." This run reports owner earnings **both ways** — as-guided (the
   conservative end) and with the separation payments added back (the normalized end) — and
   carries the difference as part of the range [E4-25] rather than choosing.
4. **Stranded cost is not an estimate I am entitled to make, and the company has published one.**
   Corporate expense in the recast Honeywell Technologies statements runs **$884M (FY2025)** and
   **$935M (FY2024)**, and the recast footnote says why it is that large: "Corporate expenses
   **historically allocated to the Aerospace Technologies and AM businesses and not eligible to be
   part of discontinued operations are included in Corporate**." Management's FY2026 guidance
   embeds the removal of that stranded cost as **+250 to +290bp of segment margin in a single
   year**. That promise is recorded at Stage 0 and would have been a Q3 [E4-22]/[E3-48] item.

### What CONTINUING operations actually earn

**Recast segment data, Honeywell Technologies only** (8-K 2026-06-29, Exhibit 99.2; quarterly
figures summed):

| $M | FY2024 sales | FY2024 profit | margin | FY2025 sales | FY2025 profit | margin |
|---|---|---|---|---|---|---|
| Building Automation | 6,540 | 1,681 | 25.7% | 7,367 | 1,953 | 26.5% |
| Process Automation and Technology | 5,919 | 1,464 | 24.7% | 6,437 | 1,542 | 24.0% |
| Industrial Automation | 6,798 | 1,117 | 16.4% | 6,111 | 896 | 14.7% |
| Corporate | — | (935) | | — | (884) | |
| **Total continuing** | **19,281** | **3,327** | **17.3%** | **19,945** | **3,507** | **17.6%** |

**Cash, from the company's own filed FY2026 guidance** (8-K 2026-07-23, Exhibit 99, the
"Reconciliation of Cash Provided by Operating Activities to Free Cash Flow", Honeywell
Technologies column, twelve months ended 2026-12-31 estimate):

| | Honeywell Technologies, FY2026E |
|---|---|
| Cash provided by operating activities from continuing operations | **$1.9bn – $2.2bn** |
| Capital expenditures | **~$(0.6)bn** |
| add back: spin-off and separation-related cost payments | ~$0.4bn |
| add back: Quantinuum | ~$0.1bn |
| **"Free cash flow" as the company defines it** | **~$1.8bn – $2.1bn** |

**Independent cross-check, by subtraction from two filed sets of audited-perimeter statements.**
HON continuing-operations OCF (FY2025 10-K, restated for Solstice) less the Aerospace carve-out
combined OCF from the Honeywell Aerospace Inc. Form 10-12B/A information statement (CIK
0002089271, filed 2026-06-08, accession 0001628280-26-041399):

| $M | 2023 | 2024 | 2025 |
|---|---|---|---|
| HON continuing-ops OCF | 4,459 | 5,112 | 6,075 |
| less Aerospace carve-out OCF | (2,984) | (2,538) | (3,705) |
| **implied Honeywell Technologies OCF** | **1,475** | **2,574** | **2,370** |

Three-year mean **$2,140M**. **The subtraction understates Honeywell Technologies and I say so:**
the Aerospace carve-out paid only **$206M / $161M / $84M** of cash income taxes because taxes
were settled through the parent, so Aerospace's carve-out OCF is flattered and the residual is
depressed. **Two independent routes bracket Honeywell Technologies' operating cash flow at
roughly $2.0bn to $2.4bn, against the screen's $5.8bn five-year mean for the old company.**

**STAGE 0 VERDICT: leg (a) passes with the mechanism recorded; legs (b) and (c) FAIL. Per the
operator's instruction, the finding is recorded and the run stops. The framework does not
open past Step 0.**

---
# THE METHOD QUESTION — DOES THE SCREEN'S 6.36% SURVIVE?

> **COMPUTATION — NOT A CLEARANCE** (operator rule 3). Every number in this section is
> Q5-shaped and is produced **before** Q1–Q4 have been asked. It carries no entry language and
> no clearance of any kind. It exists to answer one question the operator posed directly.

**No. The screen's 6.36% does not survive. The corrected bottom-boundary yield is 1.97%.**

## The four sub-questions, answered from the filings

**(a) Does HON's D&A contain large acquired-intangible amortisation that renews nothing (the
LOW/UNH pattern)? YES — and the D&A end of the range is refused.**
The FY2025 cash-flow statement splits the line, which most filers do not:

| $M | 2023 | 2024 | 2025 |
|---|---|---|---|
| Depreciation | 490 | 493 | **546** |
| Amortization | 514 | 659 | **842** |
| Total D&A | 1,004 | 1,152 | **1,388** |

**Amortisation is 61% of D&A and it is rising twice as fast as depreciation.** The reason is
visible one statement over: cash paid for acquisitions was **$718M (2023), $8,880M (2024),
$2,211M (2025)**, the 2024 figure carrying the $4.95bn Access Solutions purchase, CAES at
~$1.9bn and Civitanavi, and a further **$1,750M** was paid for Johnson Matthey's Catalyst
Technologies on 2026-07-17. Amortising a purchase-price allocation is not a maintenance
expenditure and renews nothing. The corpus's D&A default exists for a stated reason —
*"capital expenditures that over time roughly approximate **depreciation** are a necessity"*
**[E2-41]** — and that reason does not reach acquired-intangible amortisation. **The D&A end is
refused, exactly as the operator directed and as LOW and UNH established.**
*The refusal runs in HON's favour, so the counter-case is stated [E4-26]:* HON's revenue growth
in FY2025 decomposes, in its own MD&A, as **volume +3%, price +4%, acquisitions +4%,
divestitures −2%, other −1%**. A business getting a quarter of its growth from deals has an
argument that some deal spend is (c). This run does **not** charge it, because organic growth is
positive without it, but the judgment is disclosed and its direction is upward.

**(b) Is capex understated by vendor financing? NO material effect found.** HON runs supply-chain
finance programs with confirmed obligations outstanding of **$1,141M (2025), $1,150M (2024),
$1,112M (2023)** — essentially flat, so no year-over-year working-capital boost, and the
company states "The impact of these programs is not material to the Company's overall
liquidity." These are payables programs, not equipment financing. No finance-lease or
vendor-financed capital program of size was found in the debt note. **Recorded as "no
instance found," not "does not exist," per the absence-claim rule.**

**(c) Does the pension/OPEB position flatter operating cash flow? NO — it flatters EARNINGS, by
a great deal, and the cash-flow statement is clean of it.**
The operating cash flow reconciliation removes it explicitly: **"Pension and other postretirement
income (396) / (477) / (408)"** with cash benefit payments of only **$20M / $32M / $35M**. So OCF
is not flattered. But the income statement is: HON's critical accounting estimates state
*"Pension ongoing income for our world-wide pension plans is **expected to be approximately $665
million in 2026** compared with Pension ongoing income of $544 million in 2025."* Essentially all
of it stays with Honeywell Technologies — the pro forma removes only $114M of "other income"
with Aerospace. **$665M of pre-tax non-cash pension income is roughly 40% of Honeywell
Technologies' entire FY2025 pro forma pre-tax income of $1,686M, and roughly $1.68 of the guided
$8.05–$8.35 of adjusted EPS.** And the assumption behind it is aggressive: **"We plan to use an
expected rate of return on plan assets of 7.25% for 2026, which is the same assumption used for
2025,"** against a 5.25% discount rate and a 5.25% 30-year Treasury. **ITW's comparable
assumption was 5.39%, below the long bond. HON's is 200bp above it.** That is the [E4-22]
"fanciful pension assumptions" prompt, and it would have been read in full at Q3.

**(d) Is Bendix asbestos or other legacy liability funded out of operating cash flow? YES, and
it is very large — but the tail is now closed.**
Through operating cash flow: **$1,428M (2025) asbestos liabilities divestiture payment**,
**$1,325M (2023) NARCO Buyout payment**, plus ongoing net asbestos payments of **$155M (2025),
$209M (2024), $109M (2023)**. That is **$3.2bn of legacy-liability cash through OCF in three
years.** As of 2025-09-29 the Bendix and certain non-Bendix liabilities are permanently
transferred with indemnification. **What replaces it is smaller but permanent:** environmental
accruals of $443M, payments of ~$180M expected in 2026, stated to be met "from operating cash
flows," and now with **no Resideo reimbursement at all** because that stream was sold for the
$1,590M lump sum.

## The corrected number

**Owner earnings, [E2-23] convention (OCF − SBC − (c)), for the entity that exists.**
- **OCF:** the company's own guided range, $1.9bn–$2.2bn, midpoint **$2,050M**; normalized for
  the ~$400M of one-time separation cost payments, **$2,450M**. Cross-checked by subtraction at
  a $2,140M three-year mean.
- **SBC subtracted in full [E5-06]:** consolidated SBC was $196M (FY2025) and $108M (H1 2026);
  Honeywell Technologies' share is not separately disclosed. **Disclosed judgment: $120M**, on
  its share of segment profit. *[E3-70] applies and is not satisfied: the market-value measure
  is not obtainable, so the accounting charge is the floor of the subtraction, not the measure.*
- **(c), a disclosed judgment [E2-23]:** the **D&A end is refused** per (a) above. (c) is taken
  from capital expenditure at the company's guided **~$600M**, consistent with the FY2025
  arithmetic ($986M consolidated less $504M Aerospace carve-out = $482M) plus the Johnson Matthey
  addition. **Judged at $600M and not judged upward**, with the acquisition question disclosed
  above as the direction of error.

| construction | OCF | − SBC | − (c) | **owner earnings** | yield on $67,577M |
|---|---|---|---|---|---|
| as-guided, capex end | 2,050 | 120 | 600 | **$1,330M** | **1.97%** ← bottom boundary |
| normalized for separation payments, capex end | 2,450 | 120 | 600 | **$1,730M** | **2.56%** ← top boundary |
| subtraction route, 3-year mean, capex end | 2,140 | 120 | 600 | $1,420M | 2.10% |
| *D&A end — computed and REFUSED* | *2,050* | *120* | *~950* | *$980M* | *1.45%* |

**Triangulation, three ways, all independent of the above:**
- **GAAP pro forma FY2025 net income from continuing operations attributable to Honeywell:
  $1,368M → a 2.02% earnings yield.** Within 3% of the bottom-boundary owner-earnings figure.
- **The company's own guided adjusted EPS of $8.05–$8.35** × 316.94M shares = $2,552M–$2,646M →
  **3.78%–3.92%**. That is the single most generous construction available, it deletes
  acquisition amortisation, separation costs, impairments and the Quantinuum equity losses, and
  **it still does not reach the sovereign.**
- **The entire guided operating cash flow, with nothing subtracted at all: $2.2bn → 3.26%.**

**There is no construction, however generous, that puts this price at or above a government
bond.**

| | the screen, 2026-09-01 | this run, corrected |
|---|---|---|
| market cap | $68,912M | $67,577M (316,940,010 × $213.22) |
| bottom-boundary owner earnings | $4,384M | **$1,330M** |
| **bottom-boundary yield** | **6.36%** | **1.97%** |
| sovereign | 5.18% | **5.25%** (2026-08-31) |
| vs sovereign | **+1.18 pts** | **−3.28 pts** |
| perpetual growth needed for the [E4-28] 10% floor | **3.64%** | **8.03%** (7.44% at the top boundary) |

**The screen's number was 439 basis points too high, and the growth the price requires more
than doubles.** Against [E4-35] — *"fewer than 10 of the 200 most profitable companies in 2000
will attain 15% annual growth in earnings-per-share over the next 20 years"* — an 8%/yr
perpetual requirement is not a burden this file can discharge, and the company's own guidance
of 3%–4% organic growth does not attempt it.

**Dividend coverage against bottom-boundary owner earnings, stated explicitly:** the last
declared rate of $2.38 per quarter is **$3,017M a year against $1,330M — 227% coverage, or 44
cents of owner earnings per dollar of dividend.** Against the whole guided operating cash flow
it is 147%. At a 50% payout of bottom-boundary owner earnings the sustainable dividend is about
**$2.10 a share, a 0.98% yield at $213.22**; at 100% of the top boundary it is **$5.46, a 2.56%
yield.**

**One asset is excluded from the above and is named rather than netted [E3-71].** Honeywell
Technologies holds **48% of Quantinuum Inc.**, carried at **$7,260M** at 2026-06-30 after an
initial fair value of $7,525M at the 2026-06-04 IPO — **10.7% of the market cap** — and it is
currently a **loss**, at $265M of equity losses in one quarter. It is neither valued at zero nor
at face here. If it were subtracted from the market cap the operating business would yield
2.21%–2.87%, which changes nothing.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.25%** · date **2026-08-31** · source **U.S. Department of the Treasury, Daily
  Treasury Par Yield Curve Rates, 30-year constant maturity** (`home.treasury.gov`, the issuing
  authority, retrieved 2026-09-01). Adjacent observations 5.22% (08-28), 5.19% (08-27), 5.18%
  (08-26), 5.17% (08-25). *The FRED DGS30 route named in CLAUDE.md timed out twice on
  2026-09-01; the Treasury's own daily file is the same series one rung higher on the ladder and
  is used instead. The operator's brief quoted 5.18%, which is the 08-26 observation.*
- **Currency.** Honeywell Technologies reports, distributes and repurchases in USD. Non-US
  manufactured products and services were 42% of FY2025 sales and US exports 21%; the company
  borrows in Euro (five series of registered Euro notes) as a net-investment hedge. **USD is the
  sovereign.** A revenue-weighted blend would be lower and would flatter HON at the ranking
  stage; it would not move anything, because **the floor does not move with the sovereign
  [E4-28]**.
- **Price: $213.22, 2026-09-01, via aggregator — live quote only, flagged.** Prior closes
  $213.53 (08-31), $220.39 (08-27), $220.67 (08-26). HONA, for reference, $157.66 (2026-09-01).
- Market cap: **316,940,010 shares (10-Q cover, 2026-06-30) × $213.22 = $67,577M.**

**The filing was read** — not tagged data **[E3-27, protocol 4]**:
- [x] MD&A — FY2025 10-K: the separation disclosures; the segment realignment; consolidated
  results for both comparison years; the Net sales bridge (volume / price / FX / acquisitions /
  divestitures); gross margin; impairment of goodwill and of assets held for sale; other
  (income) expense; liquidity and capital resources including the full operating-cash-flow
  bridge; asbestos matters; environmental matters and the Resideo termination; supply-chain
  finance; financial instruments; critical accounting estimates including the pension
  assumptions and their sensitivity table. Q2 2026 10-Q: business update, results of operations,
  liquidity, the separation and reverse-split disclosures, subsequent events.
- [x] cash-flow statement including its detail lines — FY2025 10-K, all three years, every
  reconciling line including Depreciation and Amortization separately, the goodwill and
  held-for-sale impairments, repositioning, the **NARCO Buyout payment**, the **Resideo
  termination receipt**, the **asbestos liabilities divestiture payment**, pension income and
  benefit payments, SBC, deferred taxes, all six working-capital lines, capex, acquisitions,
  divestiture proceeds, pre-separation funding, spin-off cash, buybacks and dividends; and the
  Q2 2026 10-Q six-month statement.
- [x] footnotes — Note 1 Basis of Presentation (the Reverse Stock Split); Note 3 Acquisitions,
  Divestitures and Discontinued Operations (Solstice, Quantinuum, Sundyne, PSS/WWS held for
  sale, the Aerospace Spin-Off); Note 9 Debt and Credit Agreements including the maturity ladder
  and the pre-separation funding; Note 14 Earnings Per Share; Note 18 Segment Financial Data;
  Note 19 Subsequent Events; Note 20 Pension; the commitments-and-contingencies and asbestos
  disclosures; Item 3 / Part II Item 1 Legal Proceedings; the exhibit index (which is where the
  Elliott cooperation agreement is).
- documents, with accession numbers:
  - **Form 10-K FY2025 (year ended 2025-12-31), filed 2026-02-17, accession
    0000773840-26-000013**, primary document hon-20251231.htm, US GAAP, USD.
  - **Form 10-Q Q2 2026 (quarter ended 2026-06-30), filed 2026-07-23, accession
    0000773840-26-000124.**
  - **Form 8-K filed 2026-06-29, accession 0000773840-26-000084** — Aerospace Spin-Off
    completion. **Exhibit 99.3, the unaudited Article 11 pro forma condensed consolidated
    financial statements**; Exhibit 99.2, the recast supplemental quarterly segment information;
    Exhibit 99.1, the press release; Exhibit 2.1, the separation and distribution agreement.
  - **Form 8-K filed 2026-07-23, accession 0000773840-26-000120**, Exhibit 99 — Q2 2026 earnings
    release with the **Honeywell Technologies-only FY2026 guidance and free-cash-flow
    reconciliation**.
  - Form 8-K filed 2026-01-29, accession 0000773840-26-000006 (Q4 2025 release and 2026
    outlook); Form 8-K filed 2026-08-19, accession 0000773840-26-000130 (leadership).
  - **Honeywell Aerospace Inc. Form 10-12B/A, CIK 0002089271, filed 2026-06-08, accession
    0001628280-26-041399**, Exhibit 99.1 information statement — the Aerospace carve-out combined
    financial statements including the combined statements of cash flows.
  - Prior 10-Ks for the series: FY2023 (0000773840-24-000014), FY2021 (0000773840-22-000018).
  - DEF 14A filed 2026-04-10, accession 0000773840-26-000029.
- **Figure cross-checked against the filed statement:** **operating cash flow from continuing
  operations, FY2025, $6,075M** — identical in (a) the filed Consolidated Statement of Cash
  Flows, (b) the MD&A liquidity bridge, and (c) the XBRL tag
  `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`. Second check: **FY2025 net
  sales $37,442M**, identical in the income statement, the Article 11 pro forma "As Reported"
  column, and the segment reconciliation.
- **Perimeter flag, stated because it governs everything above:** the FY2025 10-K, the Q2 2026
  10-Q and the FY2026 guidance are **three different perimeters**. The 10-K consolidates
  Aerospace; the 10-Q consolidates Aerospace (fiscal quarter closed 2026-06-27, spin 2026-06-29);
  only the pro formas, the recast Exhibit 99.2 and the guidance describe Honeywell Technologies.
  **No filed document yet contains a Honeywell Technologies statement of cash flows.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

*Answered because Step 0 was completed and because a file that stops without any verdict is
harder to re-open than one that says where it stopped. The gates below Q1 are not opened.*

- **Unit economics in my own words, no management language.** Honeywell Technologies sells the
  control layer of other people's physical infrastructure. Three businesses: **Building
  Automation** ($7,367M, 26.5% segment margin) sells fire panels, detection, building
  management systems and the service contracts around them, into buildings that must keep them
  working to be occupied and insured. **Process Automation and Technology** ($6,437M, 24.0%)
  sells UOP process technology and catalysts to refiners and LNG plants, plus distributed
  control systems for process plants, on a project-then-aftermarket shape. **Industrial
  Automation** ($6,111M, 14.7%) sells sensing, smart energy, thermal solutions, process
  measurement, warehouse automation and productivity devices, and it is the weak leg — sales
  down 10% and segment profit down 20% in FY2025, with two of its businesses (Productivity
  Solutions and Services, Warehouse and Workflow Solutions) written down $724M of goodwill and
  $270M of other assets and put up for sale. Corporate takes $884M off the top. About **$20bn
  of backlog**, versus $37.5bn for the old combined company at 2025 year-end of which Aerospace
  was $18.4bn. Roughly $2.0bn to $2.4bn of operating cash a year, $0.6bn of capex, against
  $20.9bn of pro forma total debt.
- **The scarce input this business controls: the installed base and the specified position in a
  running plant or building.** A fire panel or a distributed control system is a small part of a
  building's or a refinery's cost, it is qualified into the design and the operating procedures,
  and swapping it is disproportionately expensive relative to its price. That is a real source
  of pricing tolerance and it shows in the filed price/volume split — **FY2025 revenue growth was
  +4% price on +3% volume; FY2024 was +2% on +1%.** Six filed years, from the same MD&A bridge,
  **on the pre-spin consolidated perimeter and therefore including Aerospace**: volume
  **−12, +1, −4, 0, +1, +3** and price **+1, +3, +10, +4, +2, +4** (FY2020 to FY2025). Chained
  across shifting bases, roughly **−11% of cumulative volume against +26% of cumulative price**,
  with FY2025 the best volume year of the six.
  *(Recorded because [E4-55] asks for the physical series and **HON is the first name in this
  queue that publishes it**; COLM, RPM, CSL, ALG and ITW disclosed nothing comparable. It is
  banked, not used: the series belongs to the combined company, and no Honeywell
  Technologies-only split exists in any filed document. The warning [E4-55] attaches to it is the
  one to carry into the re-read: "Dollar revenue flattered by pricing is how a shrinking
  franchise hides.")*
- **Will the fundamentals look broadly the same in ten years? The businesses, probably yes. The
  company, no — and that is the finding.** [E3-31] asks for a business "relatively simple and
  stable in character" and says that "if a business is complex or **subject to constant change**,
  we're not smart enough to predict future cash flows." The filed record for the last fourteen
  months is: Sundyne acquired (2025-06-06); the PPE business sold (2025); Bendix asbestos
  divested (2025-09-29); the Resideo indemnification monetised (2025); **Solstice Advanced
  Materials spun (2025-10-30)**; PSS and WWS classified held for sale (2025-12-31) with sale
  agreements announced April 2026 and closings expected in Q3 2026; a **four-segment realignment
  effective Q1 2026**; $16.0bn of Aerospace notes issued and $13.0bn of Honeywell debt repaid
  (March 2026); **Quantinuum deconsolidated at IPO (2026-06-04)**; **Aerospace spun and a
  one-for-two reverse split (2026-06-29)**; **Johnson Matthey Catalyst Technologies acquired for
  $1,750M (2026-07-17)**; and two segment CEOs replaced effective 2026-10-01. Eleven perimeter
  changes in fourteen months.
- **[E4-46] check, run honestly in both directions.** *"If we can't make a decision in five
  minutes, we can't make it in five months."* The **businesses** are inside the circle: fire
  panels, catalysts and control systems are understandable, and nothing here is a
  five-months-of-study problem. What is missing is not competence, it is **documents that do not
  exist yet** — and the rule is that UNRESEARCHED is for documents. **I can name them, and their
  dates.**
- **VERDICT: [ ] IN  [ ] OUT  [x] UNRESEARCHED  [ ] UNKNOWABLE**
  **THE WORK ORDER.** The artifact is **Honeywell Technologies' Form 10-Q for the quarter ended
  2026-09-30, expected on or about 2026-10-22**, which will be the first filed document
  presenting Aerospace as discontinued operations for all periods and therefore the **first
  Honeywell Technologies statement of cash flows** — nine months of 2026 against nine months of
  2025. The complete artifact is the **FY2026 Form 10-K, expected February 2027**, which gives
  FY2026, FY2025 and FY2024 on the new perimeter, audited. Ladder rung: SEC EDGAR primary
  documents. Blocked by: **nothing except the calendar.** A second, smaller artifact is the
  **Board's Q3 2026 dividend declaration**, which sets the rate on which the mandate turns.
  A third is the **2026 investor day materials** referenced in the Q2 release ("the long-term
  targets that we shared at our recent investor day"), which are on the IR site and were not
  pulled because nothing in this run rests on them.

## Q2 — Q6: **NOT OPENED.**

**The hard sequence binds** (operator protocol 2, and Framework §III): the run stops at the
first verdict that is not IN, and Stage 0 had already stopped it. No moat class is assigned, no
competitor row is adjudicated, no manager verdict is written, no staying-power score is given,
and **no Q5 verdict exists** — the arithmetic above is headed COMPUTATION — NOT A CLEARANCE and
is there only because the operator asked whether the screen's number survived.

**Recorded for the re-read, as evidence and not as verdicts.** These are the things the operator
asked for at Q2–Q6 that the filed record already answers. They are banked so the October re-read
starts further along; each is a fact, none is a finding.

- **Q2, the segment point the operator raised, is now moot in its original form.** The brief
  asked whether Aerospace's installed base and aftermarket made it "a different animal" from
  Building Automation and Advanced Materials. **All three animals are now separate listed
  companies.** The [E3-03] test at HON is a test of three automation segments only, and the
  competitor row named in the brief splits accordingly: **RTX and GE Aerospace are competitors of
  HONA, not of HON.** The industrial half of the row (Emerson, ABB or Siemens) is the whole row
  now, and Rockwell Automation, Schneider Electric, Johnson Controls and Carrier belong in it —
  HON's own Item 1 competition table names **Emerson Electric, Rockwell Automation, TE
  Connectivity, Zebra Technologies, Itron, MSA Safety, Dematic, Clariant, Flowserve and Topsoe.**
  Its Item 1 aerospace list is Garmin, L3Harris, Rolls-Royce, RTX, Safran and Thales, and three
  of those four peers file nothing with the SEC. **HON's own filing does not name GE Aerospace or
  ABB as competitors anywhere.**
  The evidence pack in `_research 2026-08-26` carries what was gathered, **on the pre-spin
  perimeter, and it is not adjudicated here and no moat class is assigned.** Its headline row,
  recorded as data: return on total operating capital **including goodwill**, most recent fiscal
  year, one uniform construction, is HON (combined) **16.5%**, RTX **7.8%**, GE Aerospace
  **22.1%**, Emerson **10.3%**, ABB **17.6%**, against ITW's **34.3%** from the prior pack; and
  goodwill plus intangibles as a share of total assets is HON **37.8%**, RTX **49.8%**, GE
  **10.2%**, Emerson **65.9%**, ABB **28.8%**, ITW **35%**. **The row's two named gaps:** ABB
  filed Form 25 on 2023-05-12 and Form 15F-12B on 2024-06-10, so its last SEC filing is the
  **FY2023 20-F (accession 0001104659-24-026633), two years stale** — the route to close it is
  ABB's own Integrated Report on its IR site, and its post-deregistration accounting basis is not
  established from anything read here. **Siemens AG is fully deregistered** (last 20-F
  2013-11-27, Form 25 2014-05-05, Form 15F-12B 2014-05-16); it is not obtainable through the
  ladder at all.
- **Q2, goodwill and intangibles as a share of assets** — the metric that decided ITW, CSL and
  HD. On the pro forma balance sheet at 2026-03-31: goodwill $18,056M plus other intangibles
  $5,012M = **$23,068M against $52,879M of total assets, 43.6%.** For scale, ITW was 35% and
  Danaher 73%. The FY2026 return on total invested capital including goodwill is not computable
  until the Q3 10-Q gives a post-spin balance sheet, and the pro forma is unaudited and dated.
- **Q3, Elliott, recorded as a dated fact and nothing more.** FY2025 10-K exhibit index, item
  10.67: **"Cooperation Agreement, by and among Elliott Investment Management L.P., Elliott
  Associates, L.P., Elliott International, L.P. and Honeywell International Inc., dated as of
  May 28, 2025"** (incorporated by reference to the Form 8-K filed 2025-05-28). The risk factors
  refer to "**actions or challenges from shareowners, including activist shareowners**." **No
  characterisation of the separation as value creation or as [E2-30] behaviour is made here; that
  is a Q3 judgment and Q3 is not open.**
- **Q3, the guidance-versus-outturn record [E3-48] is live and one item is already fired.**
  Honeywell Technologies guides FY2026 **segment margin of 20.1%–20.5%, up 250 to 290 basis
  points in a single year** off a 17.6% FY2025 base, on 3%–4% organic growth. Guidance was raised
  at Q2 rather than trimmed. The outturn is not knowable until February 2027. **Recorded as the
  thing to check, not scored.**
- **Q3, the fifth flag [E4-29] has an unusually clean test available.** The Q2 2026 release
  guides **adjusted** EPS of $8.05–$8.35 while stating that management "cannot reliably predict
  or estimate, without unreasonable effort" the GAAP reconciling items and therefore **publishes
  no GAAP EPS guidance at all**, and its "free cash flow" adds back separation payments and
  Quantinuum. The FY2025 GAAP pro forma figure is $2.14 of basic EPS from continuing operations.
  **A gap between $2.14 filed and $8.05–$8.35 guided is a prompt to read, and the reading belongs
  at Q3 with the pension income and the acquisition amortisation quantified against it.**
- **Q4, the [E2-54] coverage test, computed because it is cheap and it is not encouraging.**
  Pro forma FY2025 interest and other financial charges **$788M** (after the $212M saved by
  repaying $13.0bn with Aerospace's money). *"all interest, both payable and accrued, to be
  comfortably met out of current cash flow net of ample capital expenditures."*
  (OCF $2,050M + cash interest $788M − capex $600M) ÷ $788M = **2.84x**; normalized for the
  separation payments, **3.35x**. **ITW, the diversified-industrial precedent, was 10.15x.**
  Pro forma total debt at 2026-03-31 was **$20,888M** ($13,164M long-term, $3,094M current
  maturities, $4,630M commercial paper) against $10,977M of cash and $413M of short-term
  investments. **Recorded; not scored, because Q4 is not open.**
- **Q6, the never-switch test the operator asked for, answered as a fact rather than a
  judgment.** A company that has just split into three is by construction not a
  never-switch holding, and the record shows why: an owner of one HON share in June 2025 now
  holds HON, HONA and Solstice, has had a reverse split applied, and holds a 48% quoted stake in
  a quantum-computing IPO inside the HON share. **[E2-39]'s permanent designation is made "in
  writing, in advance" [E1-02]; it cannot be made about a perimeter that changes eleven times in
  fourteen months.** For a taxable account, the switching bar is **tax + friction + a material
  gap [E4-45, E2-46, E3-64, E3-67]** — and none of that arithmetic is reached, because no
  position exists and no entry case survives Stage 0.
- **The catalyst dates, pre-committed for the re-read:** Q3 2026 dividend declaration (late
  September 2026) · **Form 10-Q for Q3 2026, on or about 2026-10-22 — the first Honeywell
  Technologies cash-flow statement** · closing of the PSS and WWS sales (guided Q3 2026) ·
  Q4 2026 earnings release and FY2027 outlook (late January 2027) · **FY2026 Form 10-K,
  February 2027 — the first audited multi-year continuing-operations series.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Stage 0 stopped the run per the
      operator's instruction; Step 0 and Q1 were completed; Q2–Q6 are explicitly NOT OPENED.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — no question is
      marked IN.
- [x] The one non-IN verdict (Q1, UNRESEARCHED) names the artifact, where it lives, the ladder
      rung and the date.
- [x] Step 0: the filing was read, with six accession numbers; two figures were cross-checked
      against the filed statements.
- [x] Owner earnings computed on a multi-year basis where the data exists, and on the company's
      own filed forward guidance where it does not; both windows shown; **the capex band
      disclosed as a judgment and the D&A end explicitly refused with its reason.**
- [x] Competitor row: **not filled and not needed**, because Q2 did not open. The evidence pack
      is committed alongside and is marked non-load-bearing.
- [x] Sovereign is for the earnings currency, from the issuing authority (U.S. Treasury), dated
      2026-08-31; the CLAUDE.md FRED route failed and the substitution is recorded.
- [x] All Q5-shaped arithmetic is headed **COMPUTATION — NOT A CLEARANCE** and carries no entry
      language. No value range and no bar is stated, because Q5 did not open.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git.

## REGISTER
- Verdict: [ ] IN  [ ] OUT (about the business)  **[x] UNRESEARCHED (about my evidence)**
  [ ] UNKNOWABLE
- One line: **The screen measured a company that no longer exists — Honeywell spun Aerospace on
  2026-06-29 and reverse-split one-for-two the same day, and the 6.36% bottom-boundary yield
  paired the old company's cash flow with the new company's market cap; corrected to the entity
  that exists, the bottom boundary is 1.97% against a 5.25% sovereign, the price needs 8.03%
  perpetual growth to reach the [E4-28] floor, and the last declared dividend is 227% of owner
  earnings.**
- **THE WORK ORDER:** artifact **Honeywell Technologies Form 10-Q for the quarter ended
  2026-09-30 (the first filed Honeywell Technologies statement of cash flows), and then the
  FY2026 Form 10-K** · where it lives **SEC EDGAR, CIK 0000773840** · ladder rung **2, EDGAR
  primary documents** · blocked by **the calendar: expected on or about 2026-10-22 and February
  2027 respectively**. Second artifact: **the Board's Q3 2026 dividend declaration**, Form 8-K
  Item 8.01, expected late September 2026.
- **Priority of the work order: LOW, and the reason is stated so the file is not re-opened by
  habit.** The gap is not a rounding question. On the company's own guidance, with nothing
  subtracted at all, the yield is 3.26%; on its own most generous adjusted measure it is 3.92%;
  on owner earnings it is 1.97%. **Every one of those is below the 30-year Treasury, and the
  floor is 10% [E4-28] whatever the Treasury does.** The October filing would have to reveal
  operating cash flow roughly three times the company's own guidance to change the answer. The
  file re-opens on **price**, not on the filing: a re-read is warranted if HON trades below
  roughly **$70** (at which the top-boundary owner-earnings yield reaches ~2.5x the current
  level and the arithmetic becomes worth redoing), or if the Q3 10-Q shows continuing-operations
  operating cash flow above **$3.0bn annualised**, which would mean the guidance was materially
  wrong in the owner's favour.
