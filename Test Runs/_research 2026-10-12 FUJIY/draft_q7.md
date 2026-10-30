
## Q7 COMPUTATION, NOT A CLEARANCE (the operator's two reporting figures; the file closed at Q2)
Every figure in this section is arithmetic on the filed statements, reported at the owner's request under Part VII, The owner's
price. It is not a clearance, carries no entry language, and does not change the box (operator rules 2 and 3). Script:
`Test Runs/_research 2026-10-12 FUJIY/scripts/q7.py`; output: `extracts/q7_output.txt`.

**Owner cash, ¥ million, from the cash-flow statements** (operating cash flow less purchases of PP&E and software, net of the
investing "Other" line, which holds sales of PP&E; never a net-income proxy, operator rule 5). Purchases of businesses are net of
disposals and include buy-outs of minority holders ("capital transactions with noncontrolling interests").

| FY | Operating cash flow | Capital spending | D&A | Net purchases of businesses | Owner cash, all spending | Owner cash, maintenance only (OCF less D&A) | Spending above D&A |
|---|---|---|---|---|---|---|---|
| FY2016 | 288,619 | 114,735 | 117,635 | 1,334 | 173,884 | 170,984 | -2,900 |
| FY2017 | 261,152 | 90,363 | 127,642 | 127,269 | 170,789 | 133,510 | -37,279 |
| FY2018 | 249,343 | 89,385 | 129,932 | 162,861 | 159,958 | 119,411 | -40,547 |
| FY2019 | 255,667 | 118,471 | 122,653 | 362,996 | 137,196 | 133,014 | -4,182 |
| FY2020 | 420,861 | 139,092 | 123,423 | 157,390 | 281,769 | 297,438 | 15,669 |
| FY2021 | 323,934 | 174,149 | 132,999 | -9,914 | 149,785 | 190,935 | 41,150 |
| FY2022 | 210,452 | 331,440 | 142,215 | 28,435 | -120,988 | 68,237 | 189,225 |
| FY2023 | 407,941 | 449,299 | 150,014 | 149,328 | -41,358 | 257,927 | 299,285 |
| FY2024 | 428,162 | 546,578 | 163,567 | 4,544 | -118,416 | 264,595 | 383,011 |
| FY2025 | 410,555 | 580,140 | 172,371 | -1,780 | -169,585 | 238,184 | 407,769 |

**How the range was built, specific by specific (Q7's range convention; the text of Q7 governs).**
- *Window and base.* Five years, FY2021 to FY2025. Neither end year is aberrational on the filer's own description (FY2021 and
  FY2025 are ordinary years in the releases; the mid-window FY2022 working-capital draw stays inside the average), so (a) does not
  move the base. The literal window is shown beside.
- *(e) The maintenance case is central.* The filing allows the guess **[M2000-144]**, **[L1999-024]**: the company separates its
  growth investment (¥1.9 trillion of R&D and capital spending over FY2024 to FY2026, "primarily in the Healthcare and Electronics
  segments", chiefly Bio CDMO plants) and depreciation is taken as the proxy for what must be spent to stand still
  **[M1998-127]**. Maintenance-only owner cash averaged ¥203,976 million. The all-spending case is shown beside (average
  ¥-60,112 million). The spending above depreciation, ¥264,088 million a year on average, is charged against the growth it buys
  in the growth case, never also capped.
- *(c) Acquisitions.* Net purchases over the window ¥170,613 million. Default pair: purchases deducted (maintenance owner cash after
  purchases averaged ¥169,853 million) and the total growth credited. Serial-acquirer test: purchases (¥170.6 billion) are below half
  of owner cash before purchases on the maintenance basis (half of ¥1,031 billion), so the default pair is central. (On the
  all-spending basis owner cash before purchases is negative and the test is meaningless; said so.) The filer reports no organic
  growth of cash, so the "organic pair" beside is maintenance owner cash before purchases with its own growth, a substitute
  confessed as mine. No merger (deal paid in shares) inside the window. Signed, unclosed deal: the graphic-communications plate
  transfer (agreement 2026-08-28; under 1% of revenue, operating profit "immaterial", price undisclosed), valued beside at nil.
  The Business Innovation spin-off is an assessment, not a signed deal, and is left out.
- *(d) Working capital* is inside operating cash flow, counted.
- *All-equity basis.* Interest paid is inside operating cash flow, so after-tax interest is added back: average interest expense
  FY2021 to FY2025 ¥5,910 million x (1 - 0.306) = ¥4,102 million. CONVENTION of this run: 30.6% as the Japanese statutory
  effective rate, used only for this add-back; rationale: the release gives no statutory rate and the effective rate (24.9% in
  FY2025) would overstate the add-back only trivially. Stock pay: a guess of ¥1,800 million a year deducted (treasury shares
  disposed as share-based pay were ¥2,237 million in FY2024 and ¥1,399 million in FY2025 in the equity statements), since stock
  pay is a real cost and the cash-flow statement does not show it separately.
- *Growth.* Total growth of maintenance owner cash after purchases, end year to end year: 4.55% a year (¥200,849 million to
  ¥239,964 million). Organic, before purchases: 5.68%. Sales growth over the same window: 7.37%. (f): neither rate is above the
  discount rate or above sales growth, so no cut.
- *Rate.* 30-year JGB 4.14% (MOF, 2026-10-08). Ten years of growth, then zero nominal growth.
- *Net debt* at 2026-06-30 (Q1 FY2026 release; no subsequent events stated): borrowings ¥975,602 million less cash ¥150,651
  million and investment securities ¥45,026 million = **¥779,925 million**; operating leases (¥134.8 billion) left out.
- *Tax.* Owner cash is after the company's own income tax (operating cash flow is after taxes paid); no conversion; no expiring
  carryforward shelter found in the documents read.

**Results (¥ a share, all-equity basis, enterprise value less net debt, 1,195,607,779 shares):**

| Case | Base cash (¥ m) | Growth | Value at 4.14% | Value at 10% |
|---|---|---|---|---|
| **Top: no growth, maintenance only, purchases deducted (default)** | 172,155 | 0 | **¥2,826** | ¥788 |
| **Bottom: growth case, total growth credited, spending above D&A charged for ten years** | 172,155 | 4.55% | **¥2,657** | ¥-43 |
| beside: organic pair, no growth | 206,277 | 0 | ¥3,515 | ¥1,073 |
| beside: organic pair, growth case | 206,277 | 5.68% | ¥4,269 | ¥540 |
| beside: literal window, all spending, no growth | -57,811 | n/a | ¥-1,820 | ¥-1,136 |

The growth case is worth less than the no-growth case: the growth bought is worth less than its cost at the window's spending, so
by (e) the maintenance-only no-growth case is the top and the growth case the bottom; "growth can destroy value if it requires
cash inputs in the early years [...] that exceed the discounted value of the cash that those assets will generate in later years"
**[L2000-023]**. That inversion rests on carrying the window's average growth spending for all ten years; the company says
Healthcare capital spending peaked in FY2024 (Integrated Report 2025, page 37), so the bottom is the harsher reading of the window,
written down as such.

**VALUE RANGE: ¥2,657 to ¥2,826 a share** (per ADS, at one-half share and ¥158.44: **$8.38 to $8.92**), against ¥3,402 ($10.74
per ADS by the ratio; ADR close $10.77). Width 1.06 to 1.

**How Q7 would close, had it been reached (stated for the record only).** The floor is tested first: at the price the enterprise is
valued at ¥4,847 billion (market cap ¥4,067.5 billion plus net debt ¥779.9 billion); the default no-growth case's cash is 3.55% of
that, and the organic no-growth case's 4.26%; no case in the range earns the floor of about ten percent **[M2003-149]**, and the
price is above the top of the range even at the government rate. That is an OUT on the floor, whatever the width. A research pass
is therefore not warranted on the commodity-business case's convention (Part VII, When a research pass is run): no case earns the
floor at the price, and in any case the cause here is NATURE.

**FAIR PRICE (reporting convention, Part VII: each end case valued at ten percent, the two averaged; not a verdict, not entry
language):**
- **Central, all-equity basis** (owner cash before interest, after the company's tax, enterprise value less net debt):
  (¥1,721,545 m + ¥728,495 m) / 2 - ¥779,925 m = ¥445,095 m, **¥372 a share, $1.17 per ADS** (one ADS = one-half share; ¥158.44 =
  $1, 2026-10-13, aggregator).
- **Beside it, equity-only basis** (owner cash after interest, against the market value, no debt deducted): **¥984 a share, $3.11
  per ADS.** The equity-only figure is higher because the company borrows at about 0.6% (¥5.0 billion of interest on about ¥900
  billion of debt) while net debt is deducted at its face; it never decides alone.
- Against the price ¥3,402 ($10.77 ADR close).

**Q6's buyback line, written back as a fact (Q6 not reached).** The April 2026 repurchase paid an average ¥3,084 a share, above the
bottom of the computed range (¥2,657) and above its top (¥2,826); under the buyback-with-no-stated-price convention that would weigh
against at Q6. Recorded, not weighed.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 0721e8ce); written question by question; committed after Step 0 to Q1
      (8afe52e5), after Q2 and the facts (6ff0f9f3), and after this section.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten).
- [ ] **The blind rule was breached once**: a `ls "Test Runs" | grep -i fuji` at the start listed two file names (a 2026-07-15 FUJIY
      run and a 2026-07-15 FJTSY run). Neither was opened, searched or used; declared under CONTAMINATION at the top. No other run
      file, holding review, `PORTFOLIO.md` or blind-listed file was opened.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `scripts/check_ids.py`, output below). Every filing fact names its document and date (no accession exists for TSE
      disclosures; the brief's departure 3); the two SEC filings used carry accessions.
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash from the cash-flow statements, never a net-income proxy (operator rule 5); the sovereign from the Ministry of
      Finance; the two quotes and the exchange rate are aggregator figures, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, five items); integrity facts flagged in the box line and under
      AFTER THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` and `Screens/cover_shares.py` printed nothing usable for a non-SEC filer; nothing of theirs used.
- [x] `python tools/check_framework.py` run before the final commit (result below).
- Limits, stated plainly: the Japanese annual securities report (business risks, management analysis, the full notes) was not read;
  the English results releases and Integrated Report stand in for it. No instax unit series exists in the documents read, so
  volume is proxied by segment revenue, which carries the yen. Only one rival's segment figures were read, and only to 2022.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The business-of-parts threshold decided this file, and it is fragile here.** Section B's "largest part decides" made Imaging,
31% of five-year segment profit, the deciding part over Healthcare at 27%, though Imaging was the smallest segment in every year from
FY2014 to FY2020 and Healthcare, Electronics and Business Innovation together carry more than two-thirds of the profit and nearly
all of the capital. The convention closes the file on the castle of a consumer camera business for a company whose balance sheet is
mostly Bio CDMO plant. I applied it as written; the framework does not say what to do when the largest part is a minority and only
recently the largest. (2) **Q1 against Q2 for a change for the better.** Q1's definition of understanding includes "earning power
[...] in five or 10 years", and the doubt about Imaging's earning power is exactly section C's question at Q2. I took the business as
understood at Q1 and sent the durability question to Q2's specific rule; a reader applying Q1's doubt row could close at Q1 TOO HARD
on the same facts. The box is the same; the door is not fixed. (3) **Section C's re-look condition assumes a volume series**; this
company publishes none for instax in the documents read, and segment revenue mixes volume, price and the yen. I wrote the condition
on revenue or the company's own statement of unit decline. (4) **Q7 (e) with growth spending this large** inverts the range (the
growth case below the no-growth case) only because the window's spending above depreciation is carried for all ten years; the rule
does not say whether growth spending, like acquisitions in (c), stops when growth stops or tapers as the filer plans. (5) **The
serial-acquirer test is undefined when owner cash before purchases is negative**, as it is on the all-spending basis here; I ran it on
the maintenance basis, which is the central case under (e).
