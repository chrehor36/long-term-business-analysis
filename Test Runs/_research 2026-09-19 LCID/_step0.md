## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (from about 04:05 local); the template was copied and committed before any fetch
(`2f51254`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the second name in
the "cap rejected as a broken input: read the cover" row (HBB, LCID, SOUN, BIRD). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-19 LCID/` (scripts copied from the HBB folder with the CIK and ticker changed). **No LCID row exists in
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, in `Screens/2026-09-01 WATCHLIST TRIAGE.csv`, or in any CSV under `Screens/`**
(grepped). Every figure below is from Lucid's own filings, fetched by this run, with the accession, unless marked otherwise.

### The entity, in every year used
CIK 0001811210, `submissions.json` (fetched by this run, `subs.py`): *"Lucid Group, Inc."*, SIC 3711 *"Motor Vehicles & Passenger Car
Bodies"*, `stateOfIncorporation` **"DE"**, `fiscalYearEnd` **1231**, ticker LCID on Nasdaq. **Former names:** *"Churchill Capital Corp
IV"* (2020-06-23 to 2021-07-23) and *"Annetta Acquisition Corp"* (2020-05-27 to 2020-06-25): the registrant is the SPAC shell into
which the operating company ("Legacy Lucid") merged in July 2021. The 2021 10-K/A (`0001104659-21-067004`, 2021-05-14) and the NT 10-Q
of 2021-05-17 are the shell's (carried to Q3 and dated). Every annual year used here (FY2021-FY2025) is the combined company.
**Controlling holder:** Ayar Third Investment Company, *"a single shareholder limited liability company organized under the laws of the
Kingdom of Saudi Arabia"*, *"an affiliate of the Public Investment Fund ("PIF") and the Company's majority shareholder"* (8-K of
2026-04-29, `0001104659-26-051606`); measured below and at Q3.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"cap rejected as a broken input: read the cover."* The triage narrative (reading list line 1429-1434): the sanity guard, *"a
yield outside -100% to +50%, or a cap under $5M, is **a broken input and never a finding**. It immediately caught four more - **BRK-B**
... plus LCID, SOUN and BIRD."* **A prompt to read, never a verdict.** The brief set three hypotheses; each was tested against the
filing and companyfacts (`_probe_screen.py`, `triage_repro.py`, outputs beside them).

**(a) The HBB two layers (a per-class dimensioned cover and/or a stale undimensioned fact): REFUTED for LCID.** Lucid has **one class**
of common stock. The inline XBRL of the Q2 2026 10-Q (`0001628280-26-052606`, raw `10Q_2026Q2_raw.htm`, `dei_out.txt`) tags
`dei:EntityCommonStockSharesOutstanding` **once, undimensioned** (context c-2, instant 2026-07-29, only the entity identifier):
**394,070,176**. companyfacts therefore carries the element (six recent facts, 2025-04-30 to 2026-07-29), and both the `a8bc84f`
`shares_outstanding()` and `Backtests/scripts/bt17_microcap.py` `shares_asof(…, 2026-09-01)` return **(2026-07-29, 394,070,176)**, the
current cover count. No fallback to a stale fact is reached.

**(b) The reverse split: CONFIRMED AS A FACT, and it is not what tripped the guard.** 8-K of 2025-09-02 (`0001811210-25-000022`),
Item 5.03: *"to effect a reverse stock split (the " Reverse Stock Split ") at a ratio of one-for-ten (1:10)"*, *"The Amendment became
effective at 5:00 p.m. Eastern Time on August 29, 2025"*, *"expected to commence trading on a reverse split-adjusted basis at market open
on September 2, 2025"*; *"The Reverse Stock Split will reduce the number of shares outstanding from approximately 3,072.6 million to
approximately 307.3 million"*; authorised shares 15 billion to 1.5 billion. Approved by stockholders at the special meeting of
2025-08-18 (DEF 14A `0001104659-25-071213`). **The brief's memory was right on the fact; the ratio and dates are now from the filing.**
Where it bites: companyfacts' dei series carries the **unadjusted** pre-split counts (3,050,262,035 at 2025-04-30; **3,072,494,911 at
2025-07-30**) beside the post-split ones (324,168,457 at 2025-10-30 onward), so the `a8bc84f` `share_count_shift()`, which did not
divide out splits, returns **0.1308** on facts filed by 2026-09-01: outside 0.75-1.50, it would have returned the name unpriced as a
"corporate action". The current screen, told the ticker, divides out the split and returns **1.308** (real issuance, below).
**The split-invariance rule in CLAUDE.md is in play for the price series, not for this count:** the count used here post-dates the
split (factor after 2026-07-29: **1.0**, `sources.split_factor_after`), and Yahoo's `close` series is split-adjusted backwards
(its two-year high prints **$36.10 on 2024-09-19**, which is the pre-split $3.61 times ten), so any pre-2025-09-02 close from that
feed must not be multiplied by a pre-split count. None is used for the cap.

**(c) The guard fired on the YIELD, not the cap: CONFIRMED, reproduced.** On facts filed by 2026-09-01 the `a8bc84f`
`owner_earnings()` returns **{5y_capex: -$3,368.8M, 3y_da: -$3,078.6M, 3y_capex: -$3,676.4M}** (no 5y_da: companyfacts carries D&A
under the screen's tags for FY2022-25 only). With the correct post-split cover count and the anchor close of **$4.85 (2026-08-31)** the
cap is **$1,911.2M**, and the three yields are **-176.3%, -161.1% and -192.4%**: every one below the guard's -100% bound; on the
2026-09-01 close ($4.55) they are -187.9%, -171.7% and -205.0%. The cap is far above $5M. **So the guard's bound that tripped was the
lower yield bound, and the input that tripped it was correct.** The price at which the five-year figure would have cleared -100% is
$8.55; LCID last closed above that in April 2026. **The label "cap rejected as a broken input" was WRONG for LCID in both words**: the
cap was not rejected and nothing was broken; the guard caught a real finding, **owner earnings more negative each year than the whole
common equity is quoted at.** The counterfactual is the instructive part: had the triage divided by the stale pre-split fact
(3,072,494,911 x $4.85 = $14.9bn), the yields would have been -22.6%, -20.7% and -24.7%, **inside the guard, and the broken input would
have passed as a plausible number.** A guard on the quotient's range cannot tell a broken denominator from a business that consumes
more than its market value; for LCID it fired on the second. **The code that wrote the triage row is not on disk** (the HBB run's
finding: the watchlist pricing script was never committed), so which count it divided by is reconstructed, not read; what is proven is
that the only count any `a8bc84f` or `bt17` reader returns on facts filed by 2026-09-01 is the correct one, and that it trips the lower
bound on every window. Whether the triage script also ran `share_count_shift()` (which would have fired first under the SNOW guard
order, 0.1308) cannot be settled from disk; the narrative names the sanity guard, and both would have kept the name unpriced.

**The other guards** (`_probe_screen_output.txt`): `scale_shift` **22.43** on the current screen (revenue $4.0M in FY2020 to $1,353.8M
in FY2025: the start of production, a real organic step of the RIVN kind), 1.68 at `a8bc84f` on the cut facts; `restatement_shift`
(1.0, FY2023), none; `working_capital_flag`, `acquisition_flag`, `da_discontinuity_flag` none; `stale_filer` 262 days since the FY2025
10-K with two later 10-Qs on file. `sbc_annual` resolves for every year (FY2019-25), so the SBC-of-zero defect does not arise. **Not a
verdict**: Q4 rebuilds owner earnings from the filed faces.

**Restatement check.** Since the merger: **no Item 4.02 filing by the combined company** in the filings list (`filings_list.txt`, 562
filings). The one amendment of statements is the shell's 10-K/A for FY2020 (2021-05-14), with the shell's own Item 4.02 8-K the same day
(`0001104659-21-066993`), filed in the SPAC-warrant restatement wave, and
an 8-K/A of 2021-07-26 completing the merger items. **Auditor:** KPMG LLP (FY2025 10-K, ICFR opinion included, Item 9A); Q2 2026 10-Q
Item 4: disclosure controls *"effective"*, no changes in ICFR.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run at
  04:02 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.34, '09/18/2026', 'US Treasury daily par yield curve')** in the same minute
  (`step0_out.txt`). FRED not used. Struck by this run, not inherited from the HBB run (which read the same row an hour earlier).
- **Earnings currency: USD.** Vehicles are built in Casa Grande, Arizona (AMP-1) and assembled from kits in Saudi Arabia (AMP-2); the
  statements are in US dollars; the Saudi subsidiary's riyal is pegged. No ADR or FX conversion of the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$4.09, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("LCID", rng="1mo", max_age_h=0)`
  (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 4.09, `regularMarketTime` 1789761602 =
  16:00:02 EDT, exchange NMS; the day's bar $4.06-$4.31 on 15.1M shares. `tools/sources.price()` returned the same 4.09 stamped 2026-09-18.
- **The month and the two years, recorded rather than choosing a day** (`price2y_out.txt`, `price2y_daily.txt`; all split-adjusted):
  $19.80 on 2025-08-29 (the last pre-split session, adjusted), $17.66 on 2025-09-02, $10.57 at 2025-12-31, $9.92 on 2026-02-24 (FY2025
  10-K), $8.80 on 2026-04-14 (the financing day), $5.87 on 04-28, $7.78 on 08-04 (the Q2 release) and $6.70 the next day, **$4.85 on
  08-31**, and **$4.04 on 2026-09-16, the two-year low**; the two-year high is $36.10 on 2024-09-19. **The price has fallen about 80% in
  a year and about 47% since the Q2 release.**
- **Primary-filing cross-check:** the Q2 2026 10-Q, Note 8: the April 2026 underwritten offering, *"the Company issued the shares to the
  Underwriter pursuant to the 2026 Underwriting Agreement at a price per share of $ 8.11"* (36,057,692 shares), and Note 15, Uber's
  placement *"issued 24,038,462 shares at a price per share of $ 8.32"*. Yahoo's closes: $9.24 (04-13), **$8.80 (04-14), $8.21
  (04-15)**. **The aggregator's series is corroborated on the post-split basis at the April financing**; the September close itself
  rests on the aggregator alone, as every run's live quote does.
- **Split factor after the count's date (2026-07-29): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **394,070,176 shares of Class A common stock**, from the cover of the **Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-04,
  accession `0001628280-26-052606`**, the latest periodic filing: *"Number of shares of the registrant's common stock outstanding on July
  29, 2026: 394,070,176"*. Re-verified from the raw inline XBRL (one undimensioned fact).
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's balance sheet: *"394,155,958 and 327,451,844 shares issued
  and 394,070,176 and 327,366,062 shares outstanding as of June 30, 2026 and December 31, 2025"*: **identical** to the cover at
  2026-06-30 (the cover date is a month later with the same figure).
- **What moved the count +20.4% in six months** (Q2 statement of equity): *"Issuance of common stock under 2026 Underwriting Agreement"*
  **36,057,692**, *"under 2026 Subscription Agreement ... (related party)"* (Uber's SMB) **24,038,462**, RSU vesting 2,058,113, ESPP
  1,768,507 in Q2 alone. Two years: 1.308x split-adjusted (the current screen).
- **What sits beside the common, and is NOT in the count:** three series of **redeemable convertible preferred stock, all held by Ayar**
  (Series A 100,000, Series B 75,000, Series C 55,000 shares), *"liquidation preference of $ 1,470,165"*, *"$ 1,032,889"* and *"$
  566,859"* thousand at 2026-06-30: **$3,069.9M in all, compounding** (the Series A and B preferences rose $203.4M in six months).
  Convertible into **103.9M** common shares (13D/A of 2026-04-30: 33,258,443 + 19,794,423 + 50,850,591), and they **vote as converted**
  (*"Each Holder is entitled to the number of votes equal to the number of whole shares of common stock into which the aggregate shares
  of the Redeemable Convertible Preferred Stock held by such Holder are convertible"*, 10-Q Note 7). At $4.09 the conversion value is
  about $425M against a $3.07bn preference, so **economically the preferred is a senior, growing claim ahead of the common, not common
  equity**. It is left out of the count and carried as a claim at Q4 and Q5. **CONVENTION:** the yield denominator stays the common cap,
  as in every run in this queue; the preferred and debt are shown beside it.

### THE PAIR
**US$4.09 x 394,070,176 x 1.0 = market cap US$1,611.7M.** Beside it, at 2026-06-30: the preferred's liquidation preference **$3,069.9M**;
convertible notes **$2,279.3M principal** (2026 Notes $204.3M, 2030 Notes $1,100.0M, 2031 Notes $975.0M), whose own filed fair value is
**$1,229.0M** (the 2030 Notes at $517.0M and the 2031 Notes at $515.5M, **about 47 and 53 cents on the dollar**); the PIF-affiliate DDTL
$500M drawn at 06-30, **$1.7bn after the July and August draws** (8-K of 2026-08-28, `0001628280-26-059385`); the SIDF loan (current and
non-current debt $3,253.7M in all at 06-30); cash and investments **$775.5M** at 06-30. **The common is the thinnest slice of the capital
structure**: total stockholders' equity is **-$1,058.0M** at 2026-06-30.

### The deal check
`sources.deal_filings("0001811210")` returned **no** SC TO, SC 13E-3, DEFM14A or 425 (`step0_out.txt`). Two 8-K Item 1.01 filings since
the 10-K (2026-04-14 and 2026-04-29) are the Series C preferred, the Uber placement and second vehicle agreement, and the DDTL amendment,
read in full (below and at Q3). **No live offer.**

### The perimeter
- **Assets of Nikola Corporation** bought in April 2025 (*"select facilities and assets in Arizona previously belonging to Nikola
  Corporation, including Nikola's former Coolidge manufacturing facility"*, FY2025 10-K Item 1A): facilities and leases, not a business;
  $95.3M of finance-lease assets assumed. The 2025 investing line carries $109.6M under an acquisition tag (`capital_acquired`).
- **AMP-2 in Saudi Arabia**: kit assembly (SKD) since September 2023, the full-build (CBU) portion under construction. Inside the
  perimeter throughout.
- **Honest windows:** FY2022-25 (four years of production at scale, one perimeter), FY2021-25 (five years, the default, with FY2021 the
  first year of deliveries), and the twelve months to 2026-06-30.

### The filing was read (rule 4)
- [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
- **Documents:** FY2025 10-K filed 2026-02-24 (`0001628280-26-011053`); Q2 2026 10-Q filed 2026-08-04 (`0001628280-26-052606`); Q1 2026
  10-Q (`0001628280-26-030517`); 10-Ks FY2021-24 (`0001628280-22-004253`, `-23-005540`, `-24-007209`, `-25-007725`); 10-Qs Q2 and Q3
  2025; DEF 14A 2026 (`0001628280-26-026842`) and the 2025 special-meeting DEF 14A; the 8-Ks and Schedule 13D/As named in this file;
  the EX-99.1 releases 2024-01 to 2026-08. Raw text in the research folder (`*.txt`, `.flat.txt`).
- **Figure cross-checked against the filed statement:** FY2025 net cash used in operating activities, *"Net cash used in operating
  activities | ( 2,931,912 ) | ( 2,019,674 ) | ( 2,489,753 )"* (FY2025 10-K cash-flow face) against companyfacts' -2,931,912,000,
  -2,019,674,000 and -2,489,753,000: **identical**. Capex *"Purchases of property, plant and equipment ... ( 868,158 ) | ( 883,841 ) |
  ( 910,644 )"* against the tag: identical.
