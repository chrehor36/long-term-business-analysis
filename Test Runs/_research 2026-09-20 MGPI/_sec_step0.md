
---
## STEP 0 — THE RATE, THE FILING, AND THE SIX FLAGS THE BRIEF SENT ME TO RESOLVE

**Sovereign, for the currency the business EARNS in** -- the currently observed rate, never a
forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck fresh in this run with `python tools/sources.py` on
  2026-09-20. FRED DGS30 is the documented fallback and was not used. (The same call returned
  JPY 4.05% and EUR 3.75%, both 2026-09-17; neither is used.)
- **The currency is argued, not assumed.** FY2025 10-K Note 14, footnote (a), verbatim:
  *"Sales from foreign sources totaled $ 36,497 , $ 36,240 , and $ 49,822 for the years ended
  December 31, 2025, 2024, and 2023, respectively, and are largely derived from the United
  Kingdom, Japan, Canada, Mexico, and Australia. The balance of total sales is from domestic
  sources."* Against FY2025 sales of $536,375k that is **6.8% foreign, 93.2% domestic**. The
  same note reports long-lived assets in Northern Ireland of **$5,120k** out of $327,987k of
  net PP&E (1.6%). The registrant reports in USD, the quote is USD on Nasdaq, the excise-tax
  and three-tier distribution regime it sells into is domestic, and the grain it buys is priced
  in USD. **USD is the earnings currency on the filed evidence, not by default.** Disclosed
  limit: USD at 5.34% is also the HIGHEST of the three sovereigns, so the choice cannot flatter
  this name; and the ~10% floor **[E4-28]** does not move with the sovereign in any case.

**The filing was read** -- not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended 2025-12-31, filed
  2026-02-25, accession 0000835011-26-000031.** Superseded in part by the **Form 10-Q for the
  quarter ended 2026-06-30, filed 2026-07-29, accession 0000835011-26-000103** -- which the
  screen could not see and which is the source of the current share count, the H1 2026 cash
  flows, and the receivable matter at flag (ii). Also read: the **FY2024 10-K** (accession
  0001628280-25-007962), the **FY2023 10-K** (0001628280-24-006149), the **FY2021 10-K**
  (0001628280-22-003647, the Luxco perimeter); the **Q2 2025 10-Q** (0001628280-25-036842);
  **DEF 14A** filings of 2026-04-09 (0000835011-26-000058), 2025-04-21 (0001628280-25-018635),
  2024-04-09 (0001628280-24-015469) and 2023-04-12 (0001628280-23-011403); the 8-K EX-99.1
  earnings releases of 2026-07-29 (0000835011-26-000101), 2026-04-29 (0000835011-26-000066)
  and 2026-02-25 (0000835011-26-000029); the 8-K of **2026-08-07 Item 1.01**
  (0000835011-26-000108) **and both of its exhibits in full**; the 8-K of 2026-04-07 Item 7.01
  (0000835011-26-000052); and the Item 5.02 8-Ks of 2024-12-20 (0001628280-24-052151),
  2025-07-21 (0001628280-25-035386), 2025-12-16 (0000835011-25-000105) and 2026-02-17
  (0000835011-26-000006).
- **figure cross-checked against the filed statement:** XBRL
  `NetCashProvidedByUsedInOperatingActivities` for FY2025 returns **121,528,000**. The filed
  Consolidated Statements of Cash Flows in the FY2025 10-K reads, verbatim, *"Net cash provided
  by operating activities | 121,528 | 102,278 | 83,783"* in $ thousands. They agree. Second
  cross-check: XBRL `InventoryNet` at 2025-12-31 returns **382,741,000**; the filed
  Consolidated Balance Sheet reads *"Inventory | 382,741 | 364,944"*. They agree. **Both
  figures are load-bearing below and neither is taken from the tags alone.**

### FLAG (i) — `cap_flag`. RESOLVED, and it is a THIRD branch: neither number is wrong.

The screen said: *"CAP BELOW FILED PUBLIC FLOAT - cap $362M against a filed float of $423M
(1.17x) as of 2025-06-30. A cap cannot be smaller than a subset of itself. One of the two is
wrong - RE-STRIKE THE CAP BY HAND before using any yield on this row [operator rule 4]."*
**The screen's data are right and the screen's imperative is wrong on this name.** Both figures
are correct and they are not comparable, because they are struck fourteen months apart across a
collapse in the share price.

- **The float figure, verbatim off the FY2025 10-K cover** (accession 0000835011-26-000031):
  *"The aggregate market value of the voting and non-voting common equity held by non-affiliates
  of the registrant computed by reference to the closing price at which the common equity was
  sold, as reported by Nasdaq, on June 30, 2025, was approximately $ 423 million."*
- **The branch test the brief set.** MGPI's close on **2025-06-30 was $29.97** (aggregator,
  flagged; raw response `quote_MGPI_10y_raw.json`). $423,000,000 / $29.97 = **14,114,782
  implied non-affiliate shares.** Shares outstanding at the nearest cover date, the Q2 2025
  10-Q (accession 0001628280-25-036842): *"21,292,736 shares of Common Stock, no par value, as
  of July 25, 2025"*. **Float is therefore 66.3% of the shares, and an affiliate block of about
  7.18 million shares (33.7%) is real.** This is the **MCFT branch, not the CE branch** -- the
  float is a genuine subset and the ratio is informative. It is corroborated inside the 10-K's
  own risk factors: *"a group of stockholders beneficially owning appro ximately 20 percent of
  our Common Stock as of December 31, 2025 (excluding shares controlled by certain other
  stockholders) have a right to nominate up to two of the four directors to be elected by our
  Common Stockholders pursuant to a shareholders' agreement … and two other individuals who
  beneficially own approximately 9 percent of our Common Stock as of December 31, 2025 have
  agreed to vote in favor of those nominees"* (the spacing artifact *"appro ximately"* is the
  filed text and is left unsmoothed, PRIME RULE 1).
- **Why the 1.17x is not an error in the data.** The float is measured at 2025-06-30 ($29.97);
  the screen struck its cap on 2026-09-02. $362M / 21,363,225 shares implies a strike price of
  about **$16.95**. The same 14,114,782 float shares at $16.95 are worth **$239M against a cap
  of $362M** -- the subset is a subset. **The whole of the 1.17x is the price: $29.97 to about
  $16.95 is a 43% fall, and $29.97 to Friday's $14.13 is a 53% fall.**
- **TWO CLASSES — verified from the filing, and the answer is not quite the one the brief
  expected.** Section 12(b) of the FY2025 10-K cover lists exactly one security: *"Common Stock,
  no par value | MGPI | Nasdaq Global Select Market"*, with *"Securities registered pursuant to
  Section 12(g) of the Act: None"*. But the **balance sheet carries a second class outstanding**:
  *"Preferred, 5 % non-cumulative; $ 10 par value; authorized 1,000 shares; issued and
  outstanding 437 shares"*, carried at **$4 thousand**. The brief's recollection of a small
  preferred issue is **CONFIRMED, and it is smaller than small: 437 shares, $4,370 of par, about
  $219 a year of dividend.** It is unlisted and has no quote; adding it to the cap at par changes
  the cap by 0.0014%. **The cap is the common alone. The preferred's significance is entirely at
  Q3, where it is enormous** -- see the control finding there.
- **THE CAP, RE-STRUCK BY HAND.** `cap = close(anchor) x shares(measurement) x splits AFTER
  measurement`; `close`, never `adjclose`.
  - shares(measurement): **21,414,076**, from the cover of the newest periodic filing, the 10-Q
    for the quarter ended 2026-06-30, accession **0000835011-26-000103**: *"21,414,076 shares of
    Common Stock, no par value, as of July 24, 2026"*.
  - splits effective after 2026-07-24: **none.** The chart endpoint returns an empty splits map
    over the full available history; raw response saved to `quote_MGPI_10y_raw.json`.
  - close(anchor): **$14.13 on 2026-09-18** -- the last close before this run; today is Sunday
    2026-09-20. **AGGREGATOR (Yahoo Finance chart endpoint), flagged as such per operator rule
    5, permitted for live quotes only**; raw JSON written to the research folder.
  - **cap = 21,414,076 x $14.13 = $302,580,894 ≈ $303 million.**
  - **The screen's $362M is 20% too high because it is sixteen trading days stale.** Every yield
    below uses **$303M**.

### FLAG (ii) — `deal_note`. The "probably a credit facility" 8-K is the sharpest document in this file. THIRD TIME.

The screen said: *"1 8-K Item 1.01 filing(s) since 2026-02-25, none carrying a merger agreement
(EX-2.1) - most likely a credit facility or offering; **open them only if something else is
odd**."* The brief ordered it opened anyway. It was opened, and so were both exhibits.

**8-K filed 2026-08-07 for an event of 2026-08-06, accession 0000835011-26-000108, Item 1.01.**
Two exhibits, not one: EX-10.1 *Amendment No. 2 to Amended and Restated Credit Agreement* (Wells
Fargo as administrative agent) and EX-10.2 *Eighth Amendment to Note Purchase and Private Shelf
Agreement* (PGIM). Verbatim from the filed Item 1.01:

> *"Pursuant to Amendment No. 2, the definition of Consolidated EBITDA was modified to permit
> the Company to add back, for any period on or prior to December 31, 2027, **aggregate losses up
> to $20,000,000 related to accounts receivable from specific customers**, subject to disclosure
> of such customers in writing to the Administrative Agent. … As a result of Amendment No. 2,
> such uncollected receivables will not negatively impact the calculation of the financial
> covenants which the Company must comply with under the A&R Credit Agreement, including (i) a
> consolidated fixed charge coverage ratio covenant of not less than 1.25 to 1.00 and (ii) a
> consolidated net leverage ratio covenant of no greater than 4.00 to 1.00, as may be increased
> to 4.50 to 1.00 in any fiscal quarter in which a permitted acquisition is consummated and for
> the three consecutive fiscal quarters thereafter … **The Company has exercised its option for
> an Elevated Ratio Period, commencing with the fiscal quarter ended June 30, 2026 and for the
> three fiscal quarters thereafter, in connection with the earnout obligations for the
> acquisition of Penelope Bourbon LLC.**"*

and, on the reason, in the filer's own words:

> *"The Company undertook the Amendments described above as **precautionary measures**. The
> Company continues to believe that **the third fiscal quarter of 2026 will represent its peak
> leverage**, after which it expects leverage to decline. The Amendments were supported by the
> full participation of the banking group."*

**Three facts the screen could not have produced:**
1. **Up to $20 million of customer receivables is being pre-emptively excluded from covenant
   EBITDA** -- a named, bounded, disclosed-to-the-agent credit loss, with the exclusion running
   to 2027-12-31. This is the exact subject matter of [E2-54]'s coverage test.
2. **The net leverage covenant has been stepped up from 4.00x to 4.50x** for four quarters, and
   the mechanism invoked to do it is a clause written for *"any fiscal quarter in which a
   permitted acquisition is consummated"* -- used here for an **earnout payment on a 2023
   acquisition**, not for a new one.
3. **The filer itself says Q3 2026 is peak leverage.** That is a forward statement about its own
   balance sheet made six weeks ago, and it frames Q4.

**The screen's advice would have missed all three**, exactly as at CGNX and at CE. Recorded as a
standing tooling finding: **`deal_note`'s closing clause should be deleted, not merely ignored.**
