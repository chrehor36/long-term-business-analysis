
## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business" **[R1996-018]**, held as a range
**[L2000-024]**. All arithmetic is in `scripts/value.py` (inputs `data_filed.csv`); figures in £m unless stated.

**The cash input.** Owner cash after every real cost, recast at Q4: Step 0's "tax-charge basis" column, with the pension
deficit-repair cash added back after tax because the deficit is treated as debt-like (the £16.9m deficit at 13 June 2026
is in net debt below; no contributions are now payable). **CONVENTION of this run**, rationale: deficit repair is the
paying-down of a past liability, not a cost of running the business forward, and counting both the payments and the
deficit would charge it twice. The series (FY2015 to FY2025): 127.2, 141.8, 135.9, 125.2, 172.0, 180.8, 265.8, 190.3,
121.7, 112.7, 139.6.

**The specifics, in order.**
- **(a) Cycles.** The first window year, FY2021, is aberrational on the filer's own description: "the Company achieved
  exceptional financial results through satisfying unprecedented demand" and "a period of exceptional trading conditions"
  (AR2021) **[L2005-003]**. The base is the last full cycle of the series, trough FY2018 to trough FY2024, averaged over
  FY2018 to FY2023: **£176.0m**, less acquisitions in those years (£14.6m, 2022) spread over six years: **£173.5m**. The
  earlier cycle is not complete in the reports read (FY2015 is the first year), so growth is measured between the two
  halves of the eleven-year record, FY2015 to FY2019 (avg £140.4m) and FY2021 to FY2025 (avg £166.0m), six years apart:
  **2.83% a year** (the halves method of specific (b), used here because no earlier cycle can be closed; **CONVENTION of
  this run**, rationale: it is the text's own fallback where an end-to-end rate misleads). **The literal window, shown
  beside:** FY2021 to FY2025 average £166.0m, less acquisitions £163.1m; end-to-end FY2021 to FY2025 growth −14.9% a year.
- **(b) Decline.** The literal window's decline is shown beside as its bottom (below); it is not the central case because
  (a) governs an aberrational first year.
- **(c) Acquisitions.** Sheridan (£14.6m) deducted from the base as above; organic growth is not reported separately
  ("same depot" sales only), so the default pair stands. Net purchases are far below half of owner cash: not a serial
  acquirer. **DIY Kitchens, closed 23 June 2026, after the window and before the price date, is valued on its own filed
  record** (announcement of 3 June 2026: 2025 revenue £136m, EBIT £37m, revenue growth over 17% a year for five years) with
  its financing in net debt. No owner-cash figure is filed for it; **a disclosed guess, not a substitute number:** owner cash
  = EBIT after 25% UK tax, £27.75m, assuming capital spending equal to depreciation and no working-capital draw (the
  announcement cites "customer prepayment"). Its two ends: no growth, and 17% for ten years then none.
- **(d) Working capital** is inside owner cash (operating cash after working-capital movements).
- **(e) The maintenance case.** Owned depreciation is the maintenance guess (Q3, **[M1998-127]**): over FY2018 to FY2023
  capital spending averaged £86.8m and owned depreciation £39.1m, so maintenance-only owner cash is **£221.2m**. Valued at
  the sovereign, maintenance-only with no growth (£3,866m) is worth more than all spending with the 2.83% growth it bought
  (£3,793m): **the growth bought is worth less than its cost**, so by (e) the maintenance no-growth case is the top of the
  Howdens range and the growth case its bottom; "growth can destroy value" **[L2000-023]** is the finding, not an error.
  The all-spending no-growth case (£3,032m) is shown beside.
- **(f) The cap.** 2.83% is below the discount rate and needs no more than the share of sales already earned (owner cash
  was 12.7% of sales in FY2021; the growth case reaches about 9.5% of FY2025 sales by year ten even at no sales growth). DIY
  Kitchens at 17% for ten years needs no rise in its share of sales but carries its revenue from £136m to about £654m;
  that is optimistic and is kept only because the box does not turn on it (see the floor test).
- **The rate:** 5.7225% (Step 0), zero nominal growth after year ten.
- **Net debt (all-equity basis)**, at the latest filed balance sheet (13 June 2026) with the subsequent events that filing
  states: cash £332.8m, less the DIY Kitchens cash outflow of "c.£300m", plus the £240m term loan drawn, less buybacks after
  13 June estimated at about £66m (8.65m fewer voting shares between the June figures and 9 October at about 765p;
  **CONVENTION of this run**, rationale: the share count is taken at 9 October, so the cash that bought those shares must
  leave the balance on the same date); borrowings £240m; net debt **£33.4m**, plus the pension deficit £16.9m: **£50.3m**.
  Lease liabilities (£712.9m at 13 June 2026) are left out because rent is charged inside owner cash; said so.
- **Shares:** 541.95m (Step 0), including the 12.7m issued for DIY Kitchens.

**The value range (at the sovereign, all-equity basis, less net debt):**

| Case | Howdens | DIY Kitchens | Whole less net debt | Per share | Per ADS (US$, at 1.3253) |
|---|---|---|---|---|---|
| Bottom: all spending, 2.83% growth; DIY no growth | 3,793 | 485 | 4,228 | **780p** | **$41.35** |
| Top: maintenance only, no growth; DIY 17% | 3,866 | 1,842 | 5,657 | **1,044p** | **$55.33** |
| Beside: all spending, no growth; DIY no growth | 3,032 | 485 | 3,467 | 640p | $33.91 |
| Beside: literal window £163.1m, no growth / decline −14.9% (DIY no growth) | | | | 606p / 251p | |

Width 1.34 to 1 (well inside three to one). Price **788p** (ADS **US$40.02**, aggregator, flagged): inside the range, just
above its bottom.

**The floor, tested first** **[M2003-149]**. Each case valued at ten percent instead of the sovereign: bottom 430p, top
**567p**; the beside cases 362p (all spending, no growth) to 547p (all spending with growth and DIY at 17%). **No case of
the range earns ten percent at 788p.** Sensitivities written down so the close does not rest on one choice: the literal
window base with the halves growth, 524p; the as-filed cash-tax series without the pension add-back, 522p; the
all-spending base carried at the business's own sales growth of 8.5% a year (the most generous growth in the record) with
DIY at 17%, **735p**; none reaches 788p. The price would need the business to grow owner cash faster than it has grown
sales over eleven years.

**Reporting figures (a reporting convention, not a verdict or entry language; Part VII):**
- **(a) VALUE RANGE:** **780p to 1,044p** a share (**US$41.35 to US$55.33** an ADS), all-equity basis, company's own tax
  (tax charge excluding prior-year credits), against 788p (US$40.02 an ADS, aggregator, flagged).
- **(b) FAIR PRICE:** each end valued at ten percent and averaged, all-equity basis: **499p a share, US$26.43 an ADS**
  (central figure). **Equity-only, beside:** 503p, US$26.66 (owner cash after net interest: interest received on cash,
  after tax, less about £9m a year of term-loan interest the H1 2026 guidance names; no net debt deducted). The price is
  about 58% above the fair price.

**Q6's buyback test** is written back into Q6 (bottom of the range: 780p).

**VERDICT: OUT.** No case in the range earns the floor of about ten percent at 788p: "there’s just a point at which we
drop out of the game" **[M2003-149]**. Nor would it be a screamer if it did: the price sits just above the bottom of a
narrow range, the case that needs a pencil **[M2009-005]**.
