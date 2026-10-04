# Company Run - Lucid Group, Inc. (LCID) - 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
Lucid designs and builds large, fast, long-range battery cars (the Air sedan since late 2021 and the Gravity SUV since late 2024) in
one plant it owns in Casa Grande, Arizona (installed capacity *"90,000 vehicles per year"*, FY2025 10-K Item 1), finishes kits in a
second plant in Saudi Arabia, and sells them itself through its own studios, with no dealers. **About half the revenue is cars a bank
buys and leases to the driver, with Lucid guaranteeing the bank a resale value**: *"Vehicle sales with RVG represented approximately 51
%, 55 %, and 32 % of total revenue during the years ended December 31, 2025, 2024, and 2023"*, with the guarantee's unrecorded maximum
exposure at **$705.9M** (FY2025 10-K Note 2). **A large single buyer is the controlling shareholder's own government**: the Saudi
Ministry of Finance's EV Purchase Agreement (*"may purchase up to 100,000 vehicles, with a minimum purchase quantity of 50,000 vehicles"*
over ten years), which paid **$144.0M, $174.2M and $43.7M** of revenue in FY2025-23 and **$134.6M of the $687.8M in H1 2026 (19.6%)**
(related-party lines on the income-statement face). Beside the cars it sells three small things: **regulatory credits** (permissions
other carmakers buy because the rules fine fleets that pollute): *"Regulatory credit revenue totaled $ 96.0 million and $ 30.4 million"*
(FY2025, FY2024; FY2023 *"not material"*), falling by $24.8M in H1 2026; **powertrain and battery parts and "technology access" for Aston
Martin**, itself *"a related party of the PIF"*, paid in 28,352,273 Aston Martin shares (worth $73.2M at receipt, $24.3M at 2025-12-31),
$33.0M in cash and *"remaining cash payments of $ 99 million phased over a period of three years"* (Note 16); and repairs, parts and
used cars. From the filed faces (FY2022, FY2023, FY2025 10-Ks; Q2 2026 10-Q; deliveries from the year-end EX-99.1 releases), $M:

| line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Vehicles produced (release) | 400+ to date | 7,180 | 8,428 | 9,029 | 17,840 (revised) | 10,274 |
| Vehicles delivered (release) | 125 in Q4 | 4,369 | 6,001 | 10,241 | 15,841 | 7,046 |
| Revenue | 27.1 | 608.2 | 595.3 | 807.8 | 1,353.8 | 687.8 |
| of which vehicle sales (Note 2) | | | 581.4 | 752.8 | 1,183.8 | |
| Cost of revenue | 154.9 | 1,646.1 | 1,936.1 | 1,730.9 | 2,610.2 | 1,426.2 |
| of which inventory and purchase-commitment write-downs (cash-flow face) | | | 906.1 | 590.2 | 799.1 | |
| **Gross profit** | **(127.8)** | **(1,037.9)** | **(1,340.8)** | **(923.1)** | **(1,256.4)** | **(738.4)** |
| revenue per vehicle delivered ($000) | | 139.2 | 99.2 | 78.9 | 85.5 | 97.6 |
| vehicle-sales revenue per vehicle delivered ($000) | | | 96.9 | 73.5 | 74.7 | |
| cost of revenue per vehicle delivered ($000) | | 376.8 | 322.6 | 169.0 | 164.8 | 202.4 |
| R&D plus SG&A | 1,402.7 | 1,556.1 | 1,734.2 | 2,077.4 | 2,245.4 | 1,261.6 |
| **Loss from operations** | **(1,530.4)** | **(2,594.0)** | **(3,099.6)** | **(3,020.8)** | **(3,501.8)** | **(2,071.7)** |

Read as a carmaker:
1. **Every car has cost more to build than it sold for, in every year, and the gap is not closing on the latest figures.** The cost of
   revenue per car delivered fell from $377k (FY2022) to $165k (FY2025) and **rose again to $202k in H1 2026**, while revenue per car is
   $75-98k. The write-downs are the accounting admission of the same thing: inventory is marked to *"the estimated selling prices ...
   less the estimated cost to convert"* (FY2025 10-K, KPMG's critical audit matter), $799.1M of it in FY2025. **Even before the
   write-downs the gross line is negative every year shown**: -$434.7M (FY2023), -$332.9M (FY2024), -$457.3M (FY2025).
2. **The plant runs at about a fifth of what it was built for.** 17,840 produced against 90,000 installed; the FY2025 MD&A: *"In the
   near term, we expect our production volume of vehicles to continue to be less than our manufacturing capacity."* Fixed cost is
   spread over too few cars.
3. **Below the gross line it spends $2.2bn a year** (R&D $1,211.4M and SG&A $1,034.0M in FY2025) and has lost money at the operating
   line in every year of its existence, FY2020-25 and H1 2026.
4. **The non-vehicle revenue the brief asked about is small and mostly from the controlling holder's circle.** Regulatory credits are
   7.1% of FY2025 revenue and shrinking with the rules (*"the recent proposal to lower the U.S. federal fuel economy standards and
   eliminate CAFE EV credit trading may create uncertainties regarding our ability to generate future regulatory credit sales"*, Q2
   2026 10-Q MD&A); the one technology licensee (Aston Martin) and the largest identifiable buyer (the Saudi government) are both
   PIF-related; Uber, the robotaxi buyer, is also a shareholder (SMB, 24,038,462 shares at $8.32 in April 2026 on top of the 2025
   placement). **No technology-licensing revenue from an unrelated party appears in any filing read.**

### The scarce input this business controls
**Not the plant, not the category, not a patent.** The 10-K's own claim is engineering: *"The Lucid Air Pure is the most efficient vehicle
in the world (as measured by U.S. Environmental Protection Agency ...)"* and *"Our proprietary EV technology delivers outstanding range,
charging, and driver-oriented performance, all while achieving higher efficiency ratings than other EVs as measured by miles of range per
kilowatt hour of energy consumed"* (Item 1); it also says *"many of our current and potential competitors have substantially greater
financial, technical, manufacturing, marketing and other resources than us"* (Item 1, Competition). **The one input the filings show
Lucid controls that no rival has is access to a sovereign fund's capital**: $1.0bn of Series A (2024), $750M of Series B (2024), $1,025.7M
of common (2024), $1,812.6M of common (2023), $550M of Series C (April 2026) and a DDTL now at $2.48bn of commitments, all from Ayar
(10-K and 10-Q Notes 1, 7, 15). That is a funding source, not a business advantage; whether the engineering is a position is Q2's
question.

### Will the fundamentals look broadly the same in ten years?
**The company says not, and it keeps changing what it is building.** In eighteen months: a new chief executive
(Silvio Napoli, CEO from 2026-06-01, after an interim CEO from February 2025), an *"Operational Reset"* (EX-99.1 of 2026-08-04: *"potential
is not performance"*), two workforce reductions (February and June 2026), a *"Midsize platform"* for *"some of the world's highest volume
segments"*, *"expansion into the robotaxi market"* with Uber and Nuro (Uber's minimum of 35,000 Gravity and Midsize robotaxis over six
years, *"conditioned on Lucid's ability to ... meet certain volume and other requirements"*, 8-K of 2026-04-14), and a full-build
plant in Saudi Arabia still being commissioned. **The business in ten years is meant to be a different product, at a different price,
from a different plant, partly for a different customer.**

### The case for UNKNOWABLE, recorded and not taken
[E3-31] asks for businesses *"relatively simple and stable in character"*: *"If a business is complex or subject to constant change,
we're not smart enough to predict future cash flows."* Lucid is subject to constant change, which argues UNKNOWABLE here. **Not taken,
for the same reason as the RIVN and BZFD runs**: Q1 asks whether I can understand how the money is made, and the filings make that plain:
cars sold below their cost, a plant a fifth used, a small credit stream, and the gap filled by a shareholder. The unpredictability is a
fact about the future business (Midsize, robotaxi, AMP-2), which I keep **outside the circle [E3-31, E4-46]**; the business the filings
show can be judged at Q2 on evidence already in. Writing UNKNOWABLE here would avoid the finding Q2 can make on the record, which is the
error [E3-47] warns of in reverse. **No degree-of-difficulty credit is claimed [E4-18]**: nothing here needed narrowing.

- **VERDICT: [x] IN** on the business the filings show (luxury battery cars built in Arizona and finished in Saudi Arabia, sold direct,
  half through banks with residual-value guarantees, a fifth of recent revenue to the Saudi government; regulatory credits; parts and
  technology access for Aston Martin). The Midsize platform, the robotaxi programme and the AMP-2 full build are kept **outside the
  circle** and carry no weight at any later question. [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE

---
## Q2 - IS IT A FRANCHISE? **[E3-03]**

### The three conditions **[E3-03]**, on Lucid's own filings
- **Needed or desired: [x] yes.** 15,841 buyers took delivery in FY2025 and 7,046 in H1 2026; the Gravity *"has a higher average selling
  price"* (Q2 2026 10-Q MD&A).
- **No close substitute: [ ] FAILS.** The filer names the substitutes itself: the cars *"are expected to compete with both traditional
  luxury internal combustion vehicles from established automotive OEMs and electric and other alternative fuel vehicles from both new
  manufacturers and established automotive OEMs"*; *"Many major automobile manufacturers, including luxury automobile manufacturers, have
  EVs available today"*; *"many of our current and potential competitors have substantially greater financial, technical, manufacturing,
  marketing and other resources than us"*, with *"greater name recognition, longer operating histories"* (FY2025 10-K Item 1,
  Competition). **The buyers' own vote is on the revenue line**: in FY2023 deliveries rose 37% (4,369 to 6,001) and **revenue fell 2%**,
  *"primarily driven by change in product mix, pricing and incentives offered"* (FY2023 10-K MD&A); in FY2024 revenue rose on 4,240 more
  Airs *"partially offset by a lower average selling price of vehicles"* (FY2024 10-K MD&A); vehicle-sales revenue per delivery fell
  **$96.9k (FY2023) to $73.5k (FY2024)** and was $74.7k in FY2025 with the dearer Gravity in the mix. A product with no close substitute
  does not have to be cut by a quarter in price to move a few thousand more units.
- **Not price-regulated: [x] yes**, but part of the revenue and much of the demand sit on a regime: regulatory credits (7.1% of FY2025
  revenue) and consumer and lease tax credits (*"the availability of tax credits and other incentives to consumers, without which the net
  cost to consumers of our vehicles could increase, reducing demand for our products"*, Q2 2026 10-Q Item 1A). **[E2-59]: the regime can
  floor a line; it does not create the class.**

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04, E4-23, E5-23]**
**The claimed advantage is engineering, and the spending buys its replacement, not its defence.** Air (deliveries from late 2021), Gravity
(late 2024), the *"Midsize platform"* (*"our planned entry into some of the world's highest volume segments"*), the robotaxi variant and
the AMP-2 full build are each a new product or plant, each funded before the last earned a gross profit. The [E5-23] test (does a lapse
in spending destroy the structure, or merely narrow it; does the spending defend the same advantage or buy its replacement?) answers
**replacement**, which is [E4-04]'s excluded class. **Key person, recorded here as a moat defect [E4-23]:** the engineering claim was
personified in Peter Rawlinson, CEO and *"Chief Technology Officer"*, who *"resigned from his positions and the Company's board"* on
2025-02-21 (8-K `0001628280-25-007722`, *"not related to any disagreements"*) and is retained as *"Strategic Technical Advisor to the
Chairman of the Board ... through February 21, 2027"*. The company then went sixteen months under an interim CEO and in 2026 hired an
outside industrial CEO whose first public words were *"potential is not performance"* (EX-99.1 of 2026-08-04). Whether the efficiency
lead survives its architect is not something the filings can show, and a moat that goes when the engineer goes is [E4-23]'s partnership,
not its Mayo Clinic.

### Primary moat metric, filing-sourced, and its trend
**Pre-tax return on capital employed net of cash [E3-46]** (`roc.py`, `roc_out.txt`; total assets less cash and investments less accounts
payable and other current liabilities, FY2025 inputs checked to the 10-K balance sheet): **-101%, -94%, -88%, -80%** (FY2022-25), on
capital employed of $2.57bn rising to $4.37bn. *"The best businesses, by definition, are going to be businesses that earn very high
returns on capital employed over time"*; this one has not earned a positive return in any year. **Gross margin**: **-471.3%, -170.7%,
-225.2%, -114.3%, -92.8%** (FY2021-25) and **-107.4% in H1 2026**: improving to FY2025, worse again in 2026.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
**Lucid recomputed by this run from its own 10-K and 10-Q faces** (FY2022 10-K `0001628280-23-005540` for FY2021-22; FY2023 10-K
`0001628280-24-007209`; FY2025 10-K `0001628280-26-011053` for FY2023-25; Q2 2026 10-Q `0001628280-26-052606`): loss from operations
over revenue, same arithmetic the RIVN run used. **Rivian, Ford's Model e segment, Tesla, GM and Ford are carried from the RIVN run's row**
(`Test Runs/2026-09-18 Run - RIVN Rivian.md`, Q2, which recomputed each from its own 10-K faces with accessions recorded there; Rivian
FY2025 `0001874178` series, Tesla `0001628280-26-003952`, GM `0001467858-26-000013`, Ford via `Test Runs/_research 2026-09-13 TM/peers/`);
**Toyota, Stellantis and Honda are carried from the TM run's accessioned row** as the RIVN run carried them (transcription, a prompt).
**My Lucid figures reproduce the RIVN run's Lucid row to the decimal in every year**, which is the check on both runs. Same window,
calendar 2021-25.

| GAAP operating margin, % | CY21 | CY22 | CY23 | CY24 | CY25 | 5-yr pooled | H1 2026 | measure · source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **LUCID** | **(5,645)** | **(426.5)** | **(520.7)** | **(373.9)** | **(258.7)** | **(405.2)** | **(301.2)** | loss from operations / revenue · Lucid 10-Ks, 10-Q (this run) |
| Lucid gross margin | (471.3) | (170.7) | (225.2) | (114.3) | (92.8) | | (107.4) | revenue less cost of revenue · same |
| Rivian | (7,673) | (413.5) | (129.4) | (94.3) | (66.5) | (152.0) | | RIVN run row |
| Rivian gross margin | (845.5) | (188.4) | (45.8) | (24.1) | 2.7 | | | RIVN run row |
| Ford Model e (EV segment) | | | (73.2) | (124.1) | (67.1) | (82.5), 3 yrs | | RIVN run row, Ford segment note |
| Tesla consolidated | 12.1 | 16.8 | 9.2 | 7.2 | 4.6 | 9.5 | | RIVN run row |
| GM consolidated | 7.3 | 6.6 | 5.4 | 6.8 | 1.6 | 5.4 | | RIVN run row |
| Ford consolidated | 3.3 | 4.0 | 3.1 | 2.8 | (4.9) | 1.5 | | RIVN run row |
| Toyota automotive | 7.99 | 6.45 | 11.20 | 9.12 | 6.11 | 8.22 | | TM run row |
| Stellantis (vehicle segments, AOI) | 12.54 | 13.67 | 13.65 | 5.90 | 0.49 | 9.61 | | TM run row |
| Honda automobile | 2.52 | (0.15) | 4.07 | 1.69 | (9.96) | (0.62) | | TM run row |
| Mercedes-Benz Cars, BMW Automotive, Porsche AG | not pulled | | | | | | | not SEC registrants; see below |

| Other same-window facts | Lucid | Rivian | Ford Model e |
|---|---|---|---|
| Revenue CY25 | $1,354M | $5,387M | $7,166M |
| Operating (or segment) loss CY25 | $(3,502)M | $(3,585)M | $(4,806)M |
| Deliveries CY25 | 15,841 | 42,247 | |
| Operating loss per vehicle delivered CY25 | **about $221k** | about $85k | |
| Pre-tax return on capital employed net of cash | **(101)% / (94)% / (88)% / (80)%** FY2022-25 | (117)% / (86)% / (70)% FY2023-25 | |

- **Peers taken: 11 named, 8 with figures** (Rivian, Ford Model e, Tesla, GM, Ford, Toyota, Stellantis, Honda), of an industry whose
  competitors are, in Lucid's words, *"traditional luxury internal combustion vehicles from established automotive OEMs and electric
  and other alternative fuel vehicles from both new manufacturers and established automotive OEMs"*. **Lucid's closest luxury
  competitors (Mercedes-Benz, BMW, Porsche) are not pulled.** Can I name the document? **Yes**: the Mercedes-Benz Group, BMW Group and
  Porsche AG 2025 annual reports on their investor-relations sites (evidence-ladder rung 3; not SEC registrants, the MBGL run's finding
  for Mercedes). It is a work order for any future upgrade of this row and **not for this verdict**, for the RIVN and TSLA runs'
  directional reason: an absent competitor, however it performs, cannot turn a subject whose cars cost twice what they sell for into a
  franchise. **The moat class is therefore not PROVISIONAL**: the missing peers could only lengthen the list of those Lucid trails.
- **The row's limit [E3-61]:** it shows position, not conduct.

**WHAT THE ROW ESTABLISHES, in both directions.**
1. **For Lucid first [E4-26]: its operating margin improved every year from FY2023 to FY2025** (-520.7% to -258.7%), and its cars are, on
   the filer's EPA claim, the most efficient on sale. That is the strongest case, and it is stated first.
2. **Against it: Lucid is last in the row in every year, and by a wide margin.** Its FY2025 operating loss per car delivered (about
   $221k) is two and a half times Rivian's (about $85k) on a car that sells for a similar price (Lucid vehicle revenue $74.7k a delivery;
   Rivian automotive revenue $90.7k); its FY2025 gross margin (-92.8%) is the worst in the row and **worsened again in H1 2026 (-107.4%)**.
   Every profitable maker in the row is a volume maker; the two pure battery makers under 50,000 units a year lost 67 and 259 cents of
   operating profit on each dollar of FY2025 revenue.

### THE OTHER Q2 TESTS
- **[E3-43], the franchise demonstration, fails on both legs**: the conditions *"will be demonstrated by a company's ability to regularly
  price its product or service aggressively and thereby to earn high rates of return on capital."* Prices were cut (FY2023, FY2024), and
  the return on capital has been about -80% to -100% every year.
- **The two-characteristic test [E2-44], both legs fail.** (1) Price rises *"even when product demand is flat and capacity is not fully
  utilized"*: capacity is about a fifth used (17,840 of 90,000) and the price per car went **down** by a quarter; (2) growth *"with only
  minor additional investment of capital"*: capex **$1,074.9M, $910.6M, $883.8M, $868.2M** (FY2022-25, cash-flow faces) on revenue of
  $0.6-1.35bn, a second plant being built, and a Midsize platform and robotaxi programme to fund.
- **Untapped pricing power [E3-33]: none.** [E5-28] scopes it to near-monopoly, which the row refutes.
- **The inverse metric [E4-37]**, *"the agony they go through in determining whether a price increase can be sustained"*: the agony here
  runs the other way, in the write-downs to *"estimated selling prices"* ($906.1M, $590.2M, $799.1M FY2023-25) and in a sales-incentive
  accrual that nearly doubled (*"Sales incentive accrual | 34,626 | 18,336"*, FY2025 10-K, $000).
- **The attacker's test [E2-45]:** with ample capital and skilled people, how would one compete with Lucid? **Lucid is itself the test
  run backwards**: about $16.6bn of paid-in common capital and $2.9bn of preferred, most of it from the richest shareholder in the row,
  plus skilled engineers, have produced a maker last in the row; the incumbents it names already sell luxury battery cars from larger
  bases.
- **Direction [E4-32] and units [E4-55]: units up, position not.** Deliveries 4,369, 6,001, 10,241, 15,841 (FY2022-25) and 7,046 in H1
  2026 against 6,418 in H1 2025 (+9.8%); but the units were bought with price in FY2023-24, and in 2026 *"production intentionally
  reduced to lower inventory and free up cash"* (EX-99.1 of 2026-08-04) after Q1 built 5,500 cars and delivered 3,093. **The physical
  series says demand at a price that covers cost has not been found.**
- **The commodity end [E2-58]:** *"persistent over-capacity without administered prices (or costs) equals poor profitability"*: a plant
  run at a fifth of capacity in an industry where every maker in the row is adding battery capacity.
- **Which of the four causes of extreme success [E4-36] could this record come from?** None yet: there is no success in the record to
  attribute. The one extreme variable (efficiency) has not produced a price.

### CLASS AND VERDICT
- **Class: [x] NONE** · Direction: operating loss narrowing FY2023-25, gross margin worse in H1 2026; price per car down a quarter since
  FY2023; no year of positive gross profit.
- **Asked aloud: "Can I name the document that would resolve this?"** The luxury peers' annual reports can be named, but they cannot
  resolve a franchise question the subject's own faces answer: no document can show pricing power in a record where every car cost more
  than it sold for and prices were cut to sell more. **UNRESEARCHED is refused.** **UNKNOWABLE is refused** too: the evidence is in and
  it is a finding about the business as it exists; the future programmes that might change it were put outside the circle at Q1 and
  cannot be used to rescue it here.

**VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
**OUT on [E3-03] criterion 2 (a close substitute, shown by prices cut to move units and the filer's own list of better-resourced luxury
and EV rivals), with [E3-43], [E2-44], [E3-46], [E4-37], [E4-04], [E4-23], [E2-45], [E4-55] and [E2-58]. The file closes here.** Q3-Q6
below are recorded because the operator's instruction asks every run to end with a price and because the controlling holder's funding is
the sharpest fact in the file; **none of them governs the verdict.**

---
## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL? *(recorded, not governing: the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### STEP 1 - THE WEIGHT CASE: a GATE, on two determinants
- [x] **Daily execution [E3-38, E3-43, E2-70]**: *"a business, unlike a franchise, can be killed by poor management"*; Q2 found no
  franchise, and the 2026 record is an execution record (a seat-supplier problem that *"significantly affected Lucid Gravity deliveries
  in February"*, EX-99.1 of 2026-05-05; production cut to *"align output with anticipated demand"*).
- [ ] **Control [E1-16]**: a minority buyer of the common would own no control; the control belongs to someone else (below).
- [x] **Leverage [E3-29]**: total stockholders' equity **-$1,058.0M** at 2026-06-30 behind $3,253.7M of debt (current and non-current)
  and a $3,069.9M preferred preference growing about 18% a year (below): small errors in the assets fall entirely on the common.

**Case declared: GATE. No price compensates [E1-16, E3-29, E5-35].**

### Who governs: the controlling holder, measured from the filings
- **Ayar Third Investment Company (PIF) holds 280,188,185 shares as converted, "approximately 56.69%"** (Schedule 13D/A of 2026-04-30,
  `0001104659-26-053223`): 176,284,728 common shares (44.7% of the 394,070,176 outstanding, by subtraction) plus 103,903,457 as-converted
  from the three preferred series, which vote as converted (10-Q Note 7). The DEF 14A (`0001628280-26-026842`): *"As Ayar controls more
  than 50% of our combined voting power, we are a "controlled company"*; Ayar *"has the right to designate the Chairman of our Board"* at
  20% and a director on every committee at one-third; **five of nine directors were designated by Ayar**, and the chairman (Turqi
  Alnowaiser) is a co-manager of Ayar. **Every dilutive common raise in 2026 has lowered Ayar's common stake while its as-converted vote
  stays above half through the preferred.**
- **The controller is on every side of the business** (10-K FY2025 Note 16; 10-Q Note 15): **lender** (the DDTL, unsecured, *"5.75% for
  Term SOFR Loans"* over SOFR, EX-10.2 of 2024-08-05; commitments raised to $1.98bn in November 2025 and $2.48bn in April 2026; **$1.7bn
  drawn by 2026-08-24**; its *"minimum liquidity covenant ... was eliminated under the DDTL Amendment"*); **senior equity holder** (Series
  A $1.0bn, B $750M, C $550M, dividends *"at a rate of 9 % per annum"* compounding quarterly in kind, and a liquidation and
  fundamental-change claim of the greater of the as-converted value and a **"Minimum Consideration"**: the accrued value times a
  *"Relevant Percentage"* that steps up from **100.0% at issue to 150.4% at 60 months and 208.4% at 108 months** (Series C Certificate of
  Designations, EX-3.1 of 2026-04-29, `0001104659-26-051606`); the Series A and B preferences rose **$203.4M in six months (8.8%, about
  18% a year)** on the filed figures, which is that escalator at work); **common buyer** ($1,812.6M in 2023, $1,025.7M at $25.91 in 2024); **backstop of the
  converts** (prepaid forwards to buy about $430.0M and $636.7M of stock at the 2030 and 2031 maturities, for *"a periodic cash fee to
  Ayar ... 0.5 % per annum"* paid by Lucid); **customer** through the Government of Saudi Arabia ($144.0M of FY2025 revenue); **lender and
  grantor in Saudi Arabia** (SIDF, GIB at SAR 1,890.0M drawn, grants for AMP-2); and **shareholder of the one technology licensee**
  (Aston Martin, *"a related party of the PIF"*).
- **Were the terms extractive, on the evidence?** Not on the day they were set, by the company's own accounting: the Series C, bought for
  $550.0M, was *"initially recognized at fair value of $ 292.4 million"* with *"a gain of $ 142.2 million"* to Lucid on the subscription
  contract (10-Q Note 7), so the controller paid more than Lucid's valuation of what it received; and the DDTL is unsecured with its
  liquidity covenant removed. **But the structure is the [E2-68] asymmetry in full**: the party that holds the information advantage (it
  chairs the board) sets the price of each round, and each round has put a senior, compounding claim ahead of the common. **No filing
  shows a term I can call unfair on the day it was set; but the escalator means the preferred's floor claim more than doubles in about
  five years (9% compounded quarterly for five years is 1.56, times 150.4%, about 2.35 times the purchase price), and the common's position behind that claim is the finding.**

### Honesty - binary, permanent, filings-based **[E5-16]**, each matter dated to when it became public
- **SEC investigation of the SPAC merger and its projections**: subpoena of 2021-12-03, disclosed in the FY2021 and FY2022 10-Ks; the
  FY2023 10-K: *"On April 27, 2023, SEC staff informed the Company that the SEC has concluded this matter and it does not intend to
  recommend an enforcement action"*. **Closed without action.**
- **In re Lucid Group, Inc. Securities Litigation** (class actions of 2022-04-01 and 2022-05-31): alleges *"false or misleading
  statements about the Company's 2022 production targets"*; pending, unadjudicated; nine derivative suits, stayed (10-Q Note 11).
- **Eke v. Lucid Group** (2026-05-29): alleges the interim CEO and CFO failed to disclose *"that a supplier quality issue had
  significantly disrupted deliveries of the Lucid Gravity"*; a derivative suit followed (2026-06-16). Pending. **Its timing is on the
  record** (below, [E2-49]).
- **The shell's Item 4.02** (8-K of 2021-05-14, `0001104659-21-066993`) and 10-K/A are Churchill's SPAC-warrant restatement before the
  merger. **No Item 4.02 by the combined company.**
- **The production-count revision, February 2026**: *"management determined that 538 vehicles had not completed certain internal
  procedures required under its final validation process to be classified as produced. As a result, the Company is revising its reported
  production totals to 17,840 vehicles for full year 2025"* (EX-99.1 of 2026-02-24). **A deviation toward candor [E2-69]**: an operating
  figure corrected downward, voluntarily, with the reason and the effect (*"does not affect previously reported financial results"*).
- **Verdict on the binary: no disqualifier found.** Allegations are not findings, and the one completed regulatory inquiry closed without
  action. Written as [E5-17] requires: **the absence of found disqualifiers, not a finding that the managers are honest.**

### STEP 2 - THE FLAGS **[E4-22, E5-15, E4-29]**, each a prompt to read
- [ ] **weak accounting**: not fired. KPMG's opinion includes ICFR; no restatement by the combined company. The auditor's critical audit
  matter is net realizable value of inventory, which is where the write-downs live.
- [x] **unintelligible footnotes, mildly**: the 2025 bonus scored *"Free Cash Flow, reporting $(4,400) million (target: $(4,730)
  million)"*, while the same proxy's Annex B reconciles 2025 free cash flow to **$(3,800,070)** thousand; the scored figure is defined as
  cash from operations less capex *"subject to any cash balance adjustments not connected to operations"* and the $600M difference is not
  explained. **The difference runs against the executives** (a worse figure), so it is a reading problem, not a pay flag.
- [x] **trumpeted projections [E3-48, E5-30]: FIRES, the strongest flag in the file.** The SPAC forecasts of February 2021 (S-4/A
  `0001104659-21-080354`, *"Volume (units in thousands)"*): **20.2, 48.9, 89.8, 135.3** thousand for 2022-25, revenue **$13,985M** and net
  income **$632M** for 2025. Outturn: **7,180, 8,428, 9,029, 17,840** produced; FY2025 revenue $1,353.8M (9.7% of the forecast) and a
  net loss of $2,698.1M. Annual production guidance since listing: 2022 *"updated ... to a range of 12,000 to 14,000"* from the SPAC's 20,200 (EX-99.1 of 2022-02-28), later 6,000-7,000,
  outturn 7,180; 2023 set at 10,000-14,000 (EX-99.1 of 2023-02-22), later 8,000-8,500, outturn 8,428; 2024 about 9,000, outturn 9,029;
  2025 set at about 20,000 (EX-99.1 of 2025-02-25), cut to 18,000-20,000 (EX-99.1 of 2025-08-05), called *"approximately 18,000"* by
  February 2026, outturn 17,840 after the revision. **The first guide of the year was missed in 2022, 2023 and 2025 and met in 2024; the
  last revision was met every year.** The 2025 delivery target in the pay plan was 20,000 against 15,841 delivered. [E3-48]'s base rate,
  *"about nine cases out of ten"*, is the right prior here, and the record is consistent with it.
- [x] **serial share issuance [E5-15]: FIRES.** Common outstanding, split-adjusted: **164.8M (2021), 182.9M, 229.9M, 303.1M, 327.4M
  (2025), 394.1M (2026-06-30)**, 2.39 times in four and a half years, plus 103.9M shares as converted in the preferred and $2,279.3M of
  convertible notes. Each raise is disclosed in full; the flag reads the frequency, not the candour.
- [x] **EBITDA / adjusted earnings [E4-29]: FIRES, mildly.** Every quarterly earnings release read (FY2021 year-end through Q2 2026)
  defines and reconciles *"Adjusted EBITDA"*, which adds back depreciation, stock-based compensation and restructuring charges: FY2025
  **$(2,787.9)M** against a GAAP operating loss of $(3,501.8)M. It is not the headline bullet (the headline is production, deliveries,
  revenue and *"total liquidity"*), which keeps the flag mild. **[E2-57] and [E3-53]** ride with it: *"Workforce reduction charges"*
  ($71.6M in H1 2026) are shown on the face, which passes [E2-26], and excluded from the adjusted figures, which is the except-for habit;
  Q4 counts them.
- [ ] **filed-figure tells [E4-30]**: not applicable (no taxable profit; cash taxes $4.5M in FY2025).
- [x] **metric withdrawal [E2-49]: FIRES.** The 2026 production guidance of **25,000-27,000** was set on 2026-02-24, *"reaffirming"* on
  2026-04-03 (EX-99.1: *"These issues have now been addressed, and the company is reaffirming its previously shared production guidance
  of 25,000-27,000 vehicles"*) and repeated in the 8-K of 2026-04-14, the day of the $1.05bn raise. **No instance of the guidance, or of a
  withdrawal of it, was found in the EX-99.1 of 2026-05-05, the EX-99.1 of 2026-08-04, or either 2026 10-Q** (the absence-claim rule: a
  recorded sweep of those four documents for "25,000", "27,000", "guidance" and "outlook"); the May release says instead *"Lucid is
  taking further steps to align production with anticipated deliveries and customer demand"*, and the August release that production was
  *"intentionally reduced"*. H1 2026 production was 10,274. **A bullseye set, reaffirmed on a financing day, and then no longer mentioned
  after the result deteriorated is the disposition of the yardstick.** Limit: the earnings-call transcripts and slide decks on
  ir.lucidmotors.com were not read; they are the named documents that could show a spoken withdrawal.
- **[E4-27], the pay plan**: the 2025 bonus paid at a 68.7% factor although the gross-margin threshold was missed (-92.8% against a
  -55.0% target) and deliveries only reached threshold; the Midsize milestone, due *"by end of September 30, 2025"*, was met on 2026-01-15
  and **credited at 85%** because *"the production validation release was planned for January 15, 2026, and the milestone was met as
  planned on that date"*: the bullseye moved to where the arrow landed. The new CEO's 2026 bonus pays *"the greater of (x) target
  performance or (y) actual performance"* (8-K of 2026-04-14). **Prompts, not findings of venality [E5-38].**

### STEP 3 - THE PRIMARY TEST **[E2-01]**, balance sheet first
Common plus preferred equity: $3,909.4M (2021), $4,349.7M, $4,851.7M, $5,172.6M (2024, incl. $1,299.8M preferred), $3,000.8M (2025, incl.
$2,283.5M), $1,848.3M (2026-06-30, incl. $2,906.3M; common -$1,058.0M). **Net loss over average equity: -31.6% (FY2022, flattered by a
$1,254.2M warrant gain), -61.5%, -54.1%, -66.0% (FY2025).** Refilled by about **$7.8bn** of common and preferred raised, net, in FY2023-H1 2026 alone ($2,996.9M in 2023, $3,491.1M in 2024,
$299.7M in 2025, $1,040.8M in H1 2026, financing sections of the cash-flow faces), most of it from the controller. On [E3-59]'s first
yardstick, judged against *"the hand they were dealt"*: the hand was a sovereign-fund patron and a clean-sheet plant; the row at Q2
shows the result.

**The half-owner test [E2-26]:** mixed. For: related-party amounts on the face of every statement; restructuring on its own line; the RVG
maximum exposure ($724.5M) disclosed; the production revision volunteered. Against: the 2026 production guidance allowed to lapse in
silence; the adjusted-EBITDA habit; *"total liquidity"* as a headline that adds undrawn loans from the controller to cash.

**The institutional imperative [E2-30]:**
- [ ] resists change: no; the company has changed chief executive, structure and plan repeatedly.
- [x] projects soak up funds: a Midsize platform, a robotaxi programme, the AMP-2 full build and the Nikola facilities, all started while
  the one product line on sale lost money on every car.
- [x] staff studies for the leader's craving: the SPAC forecast table is the type specimen (135.3 thousand units in 2025).
- [ ] peers imitated: not scored; whether the 2025 robotaxi entry followed peers is not something Lucid's filings show.

**Capital allocation [E5-08, E4-31]:** no buybacks. $118.3M spent on capped calls with the 2030 Notes (a hedge against dilution bought by a
company issuing shares every year); the 2026 Notes bought back below par ($931.4M for $1,052.5M and $748.2M for $755.7M, a $121.8M gain),
which is sensible. **The capital-allocation question is the decision to keep funding a product line with negative gross margin while
starting three more; [E4-13]'s humility clause applies: management knows the programmes far better than a reader of the filings.**

**THE GUARDRAIL:**
- [x] Nothing in this Q3 promotes the name.
- [x] Key-person dependence is recorded at Q2 as a moat defect (Rawlinson) [E4-23].
- [x] Is a great manager the plan? **The company says so in words**: the 2026 release frames the CEO's reset as the path (*"potential is
  not performance"*), which is [E2-36]'s *"corporate Pygmalion"*, not an excisable cancer in an intact franchise; Q2 found no franchise to
  be intact.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary** (no disqualifier found; GATE case) [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE.
  **The flags converge [E4-52]**: projections missed, issuance serial, a guidance bullseye dropped in silence, an adjusted-EBITDA habit
  and a pay plan that moved its target, all pointing the same way; under a GATE weight this would weigh heavily on any later reopening.
  *IN = no disqualifier found. NOT a finding that the managers are honest [E5-17]. IN never promotes.*

---
## Q4 - WILL IT SURVIVE? *(recorded, not governing: the file closed at Q2)*

### Owner earnings **[E2-23]** - from the filed cash-flow faces (`oe.py`, output `oe_out.txt`), $M
Operating cash flow less stock compensation in full [E5-06] less (c), at the capex end and the D&A end (CONVENTION, section VI of v4).
Sources: FY2025 10-K cash-flow face (FY2023-25), FY2023 10-K face (FY2021-22), Q2 2026 10-Q face (H1 2026 and H1 2025).

| year | OCF | SBC | capex | D&A | **OE, capex end** | OE, D&A end |
|---|---:|---:|---:|---:|---:|---:|
| FY2021 | (1,058.1) | 516.8 | 421.2 | 62.9 | **(1,996.1)** | (1,637.8) |
| FY2022 | (2,226.3) | 423.5 | 1,074.9 | 186.6 | **(3,724.6)** | (2,836.3) |
| FY2023 | (2,489.8) | 257.3 | 910.6 | 233.5 | **(3,657.7)** | (2,980.6) |
| FY2024 | (2,019.7) | 285.9 | 883.8 | 295.3 | **(3,189.4)** | (2,600.9) |
| FY2025 | (2,931.9) | 271.3 | 868.2 | 451.2 | **(4,071.3)** | (3,654.4) |
| H1 2026 | (2,407.9) | 107.6 | 507.0 | 238.6 | **(3,022.5)** | (2,754.2) |
| twelve months to 2026-06-30 | (4,080.9) | 295.1 | 1,031.2 | 480.8 | **(5,407.3)** | (4,856.9) |

- **Five-year mean (FY2021-25, the default [E2-42]): -$3,327.8M (capex end), -$2,742.0M (D&A end).**
- **Four-year (FY2022-25, production at scale): -$3,660.8M / -$3,018.1M. Three-year (FY2023-25): -$3,639.5M / -$3,078.6M.**
- **Twelve months to 2026-06-30: -$5,407.3M / -$4,856.9M**: the worst window, and the most recent. H1 2026 operating cash (-$2,407.9M)
  exceeded the whole of FY2024's (-$2,019.7M).
- **Spread and range [E4-25]:** -$1,996M to -$5,407M a year across every window and both (c) ends. **Every figure is negative, so the
  range is wide but not inconclusive**: no window and no (c) guess produces a positive number, and the verdict does not depend on the
  band. The spread is not luck to normalise away [E4-41]: the favourable exogenous items in the window (regulatory credits $96.0M in
  FY2025; the Saudi government's purchases) would make the mean worse if removed.
- **(c), a disclosed judgment:** Lucid is capital-intensive and still building (AMP-2's full build, AMP-1 expansion, Midsize tooling), so
  much of the capex is growth, and D&A ($233-451M) is the corpus default [E3-44, E2-41]. **The [E5-20] exception class applies** (a
  carmaker whose own filing records *"significant personnel and overhead costs to operate our large-scale manufacturing facilities"* at a
  fifth of capacity), so the D&A end is not a valid owner-earnings figure for this class; it is shown only because **even it is -$2.7bn
  a year**. The verdict does not move with the band.
- **Stock compensation subtracted in full [E5-06]:** $257-517M a year on the charge. [E3-70]'s grant-value measure was not computed; it
  could only make the figure more negative.
- **Working capital [E2-23]:** carried inside operating cash; the inventory build is large (-$1,449.1M in FY2025, -$845.6M in H1 2026)
  and part of the write-down cycle, so it is not a one-off to add back.
- **Beside owner earnings, the claim that accrues ahead of the common:** the preferred's preference grows by the 9% in-kind dividend times a
  step-up schedule (Q3); the Series A and B preferences rose $203.4M in six months, about 18% a year, which on the $3,069.9M preference
  is **about $550M a year**, and none of it is in operating cash. **Owner earnings to the common are lower still by that amount.**
- **Restructuring counted [E5-33]:** the workforce-reduction charges ($71.6M, H1 2026) are inside operating cash; nothing is added back.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome**: *"grows rapidly, requires significant capital to engender the growth, and then earns little or
  no money"*. Revenue rose from $27.1M (FY2021) to $1,353.8M (FY2025) while owner earnings went from -$2.0bn to -$4.1bn and -$5.4bn in the
  latest twelve months. *"Investors have poured money into a bottomless pit, attracted by growth when they should have been repelled by
  it."* [E4-43]'s carve-out does not apply: nothing here earns *"a reasonable return"* on the cash it consumes.

### Staying power **[E5-11]** - scored on the worst case [E2-55]
- **(1) A large and reliable stream of earnings: NONE.** Operating losses every year since FY2020.
- **(2) Massive liquid assets: NO.** Cash and investments **$775.5M** at 2026-06-30 (cash $732.6M, short-term $28.7M, long-term $14.2M),
  down from $2,141.2M at 2025-12-31 and $5,043.2M at 2024-12-31; since the quarter end the DDTL was drawn $800M (July) and $400M
  (August), leaving *"approximately $800 million of additional borrowing capacity"* (8-K of 2026-08-28). The company's *"$3.0 billion in
  total liquidity"* (EX-99.1 of 2026-08-04) counts undrawn loans from the controller as liquidity.
- **(3) No significant near-term cash requirements: FAILS, and it is the killer.** H1 2026 used **$2,914.9M** (operating cash plus
  capex), about **$1.46bn a quarter**; the 2026 Notes ($204.3M) mature 2026-12-15; the GIB borrowings ($503.1M) sit in current debt with
  maturities of *"no more than 12 months"*; the ABL matures 2027-06-09. The company's own going-forward statement is conditional in its
  words: *"Based on available liquidity and projected operating cash flows, future capital expenditure requirements, existing funding
  arrangements, and the anticipated benefits of operational initiatives implemented or underway, management believes it is probable that
  the Company will have sufficient liquidity to meet its obligations as they become due for at least one year"* (10-Q Note 1), and the
  release's *"sufficient liquidity runway well into 2027"*. (No instance of "substantial doubt" was found in the FY2025 10-K or either
  2026 10-Q.) **This is the dependence the corpus names [E5-39]: "the kindness of strangers", here one stranger.**
- **Leverage, named and quantified [E4-16, E3-29]:** debt $3,253.7M at 2026-06-30 ($4.45bn after the July and August draws, before any
  repayment), the preferred's $3,069.9M preference, the RVG maximum of $724.5M, against total stockholders' equity of -$1,058.0M. **The
  coverage test [E2-54]** (*"all interest, both payable and accrued, to be comfortably met out of current cash flow net of ample capital
  expenditures"*): contractual convert interest $62.9M in H1 2026, the DDTL at SOFR plus 5.75% on $1.7bn, the GIB at 6.18%, and the
  preferred's accruing claim (about 18% a year), all against operating cash of -$2.4bn in the half. **Fails absolutely.** The terms [E3-52]: the preferred has no
  due date but carries a fundamental-change repurchase right at the greater of its accrued value and its conversion value; the DDTL is
  unsecured and its liquidity covenant was removed by the lender that controls the board.

### The specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **The mechanism: shape #8, THE EQUITY IS THE REVENUE, with #14's feature (THE PATRON)** (`Screens/SURVIVAL SHAPES - index.md`; the
  same pairing the RIVN run named for Rivian). **A later instance, not a new shape.** Customers pay a part of the cost (FY2025 revenue
  $1,353.8M against costs and expenses of $4,855.5M) and new capital pays the rest ($887.3M net financing in FY2025 on top of running down
  $2.3bn of investments net; $1.04bn of equity and $1.7bn of DDTL in 2026); and the one party that supplies most of that capital also chairs
  the board, sets each round's terms and sits senior to the common. **Why not #14 as the mechanism:** GFS's patron sets the terms of a
  plant grant; here the patron's money is the whole of the survival, and it arrives as ownership and seniority, which is #8's
  mechanism. **Why not a new shape:** the only difference from RIVN's instance is degree (Rivian's patron is a strategic partner buying
  architecture; Lucid's is a sovereign fund buying chiefly the claim itself, and through its government some cars), which is not a new mechanism.
- **Quantified from filed figures:** the pool at 2026-06-30 was $775.5M of cash and investments plus about $1.98bn undrawn on the DDTL
  (of which $1.2bn has since been drawn) plus ABL availability of $413.3M, of which $142.9M is cash already counted: **about $3.0bn**,
  the company's own figure. At the H1 2026 rate (-$2.9bn a half, $1.46bn a quarter) that is **about two quarters**; if the $1.4bn
  improvement plan came off the twelve-month rate in full (operating cash plus capex $5,112.1M, less $1.4bn = about $3.7bn a year,
  though the plan counts $600-800M of inventory release, which does not recur) it is **about three quarters**. The company's own words
  are *"well into 2027"*. **Every path in the filings requires another raise
  by 2027.** Two outcomes are then on the record's terms: (a) **the patron funds again**: the common is diluted or subordinated further
  (each 2026 round did both: 60.1M new common at $8.11-8.32 and a $550M preferred senior to it; the preference grows by about $550M a
  year); (b) **the patron stops**: $3.25bn of debt (at 2026-06-30) and $3.07bn of preference stand ahead of a common with negative book
  equity, and the converts already trade at about half their face (the company's own fair value, $1,229.0M for $2,279.3M).
- **Likelihood, in the corpus's vocabulary:** *"likely"* that the common suffers further dilution or subordination on the next raise
  (the filings name no path without one); *"a real possibility"* that the business fails as an owner's asset outright, a likelihood set
  by one holder's willingness, which no document states, and which is exactly why [E5-39] refuses to count it.
- **Stated as its holders would state it [E4-51]:** a sovereign fund with the means has funded every shortfall for five years, paid above
  Lucid's own fair value for the latest preferred, removed a covenant rather than enforce it, and owns more than half the vote; a new
  CEO has cut $1.4bn; the Gravity and the Uber programme add volume; the Midsize platform, at a lower cost, is the plan to fill the plant.
  **All of that is either a promise about the future business, outside the circle at Q1, or a statement about the patron's intentions,
  which is not evidence about the business.** The exposure [E4-40] is on the balance sheet today.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN [x] OUT** on [E4-20]'s gruesome leg and on all three of [E5-11]'s strengths, with [E2-54]'s
  coverage test failed absolutely. Not UNKNOWABLE: every window and every (c) end is negative [E4-25], so the band does not change the
  verdict. [ ] UNRESEARCHED [ ] UNKNOWABLE

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? *(COMPUTATION - NOT A CLEARANCE)*

**Q5 does not open: Q2 is OUT.** What follows is arithmetic reported because the operator's instruction asks every run to end with a
price; it carries no entry language (operator rule 3).

**COMPUTATION - NOT A CLEARANCE**
- **The pair:** US$4.09 (2026-09-18 close, Yahoo, aggregator flagged) x 394,070,176 (10-Q cover, `0001628280-26-052606`) x 1.0 =
  **US$1,611.7M**. Sovereign **5.34%** (US Treasury par yield curve, 30-year, 09/18/2026).
- **The yield** (`oe_out.txt`): five-year owner earnings -$3,327.8M (capex end) and -$2,742.0M (D&A end) over $1,611.7M = **-206.5% and
  -170.1%**; three-year -225.8% and -191.0%; twelve months to 2026-06-30 **-335.5%** and -301.3%. Against 5.34%, and against a ~10% floor
  [E4-28] that would need **+$161.2M a year** of owner earnings, the gap is about $3.5bn a year on the five-year default.
- **What the price already assumes:** not a growth rate. From a base below zero, the growth needed to reach the floor is not a number (the
  `growth_required` refusal the screen already makes). **The price is an option on two things outside the circle**: programmes that do not
  yet sell (Midsize, robotaxi) and the controlling holder's continued funding.
- **The value, as a range [E4-01]:** on owner earnings, **no positive value on any window or (c) end**. The common is also the last claim
  behind $3.25bn of debt (at 2026-06-30, $4.45bn after the July and August draws) and a $3.07bn preference growing about 18% a year; the converts'
  own filed fair value (about 50 cents on the dollar) is the market's view of the claim ahead of the common. **Bar 2 [E4-01]: the price is
  above the whole range** (the range is below zero). No margin of safety is computed because there is no value to discount.
- **Ceiling [E2-63]:** not reached; there is no earning power to bound.
- **VERDICT: not applicable. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a negative yield on every window
  and the floor would have quit the name [E4-28]. **Windage count: zero** (no conservatism was applied anywhere; every end reported).

## Q6 - WHAT WOULD PROVE ME WRONG? *(recorded; reversal condition in words, no band)*

**A Q2 OUT is a finding about the business, so no price alert is armed and no `PORTFOLIO.md` row is added** (the QLYS ruling,
2026-09-07; the FOLD rule 4). **The reversal condition, in words, pre-committed [E1-02]:** reopen Q2 only if, on the filed faces,
1. **gross profit is positive before write-downs and after them** for four consecutive quarters, with revenue per vehicle delivered level
   or rising (the price leg of [E2-44]);
2. **vehicle-sales revenue per delivery rises in a year when deliveries also rise**, with no MD&A sentence attributing revenue to
   *"pricing and incentives offered"* or a *"lower average selling price"* ([E3-03] criterion 2, [E4-37]);
3. **operating profit is positive for a full fiscal year** on the business then sold, and the pre-tax return on capital employed net of
   cash is positive in two consecutive 10-Ks ([E3-46], [E3-43]);
4. **the business funds its own capex from operating cash** for two years without a new raise from the controlling holder ([E4-20], [E5-11]
   strength 3);
5. and the Q2 row still shows Lucid at or above the luxury peers' operating margins once those peers' annual reports are pulled (the work
   order named at Q2).

**Q3 conditions that would matter at any reopening** (GATE weight): an explicit account of the 2026 production guidance; a year in which the
first guidance of the year is met; the preferred's compounding claim resolved on terms a minority owner can evaluate.

**The monitoring question [E3-30]** does not arise for a name not owned. **Position size: none.**

- **VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the file stopped at Q2 (OUT) and Q3-Q6 are labelled recorded, not governing.
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 IN rests on the filed faces; Q3's IN is the binary only).
- [x] No UNRESEARCHED verdict. The one named work order (the Mercedes-Benz, BMW and Porsche 2025 annual reports, rung 3) is recorded at
      Q2 as an upgrade of the row, and the reason it does not govern is stated.
- [x] No UNKNOWABLE verdict; the case for it at Q1 is recorded and the reason it was not taken is stated; at Q4 every window is negative.
- [x] Step 0: the filing was read (10-K FY2025 `0001628280-26-011053`, 10-Q Q2 2026 `0001628280-26-052606`, and the others listed), and
      FY2025 operating cash and capex were cross-checked against the filed face: identical to companyfacts.
- [x] Owner earnings on multi-year means (five-year default, four, three, twelve months), both (c) ends shown, (c) disclosed as a judgment.
- [x] Competitor row filled: Lucid recomputed from its own faces; eight peers with figures carried with citation from the RIVN and TM runs;
      the luxury peers named and not pulled, with the document named.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/18/2026.
- [x] Value stated as a range: no positive value on any window; not a point estimate.
- [x] One bar only (Bar 2, the price is above the whole range); windage count zero.
- [x] Price dated (2026-09-18 close), aggregator flagged, corroborated on the post-split basis by the April 2026 offering prices in the 10-Q.
- [x] Run committed to git (template `2f51254`, Step 0 `785ebac`, Q1-Q2 `47b0c6d`, Q3-Q6 with audit and register in the commit that
      carries this line; the fold in the fold commit).
- [x] No em dashes written by this run.

### CORRECTIONS MADE BEFORE CLOSE (my own errors, caught before commit of the section that carried them)
1. **The runway arithmetic** in the Q4 draft said the pool covered "about one more year" and put the post-plan burn at "$4.4bn a year";
   recomputed from the filed pool ($3.0bn) and rates: about two quarters at the H1 2026 rate, about three on the plan-adjusted rate
   ($5,112.1M less $1.4bn is $3.7bn, not $4.4bn).
2. **The preferred's growth** was first written as "9% compounding", about $276M a year. Reading the Series C Certificate of Designations
   (EX-3.1 of 2026-04-29) found the *"Relevant Percentage"* step-up (100.0% to 150.4% at 60 months, 208.4% at 108 months); the filed
   movement of the A and B preferences ($203.4M in six months) confirms about 18% a year, about $550M a year. Corrected in Q3, Q4 and Q5.
3. **A figure I had not computed**: the Q3 draft said "$13.6bn of equity and preferred raised FY2021-H1 2026". Replaced by the sum I did
   compute from the cash-flow financing sections, $7.8bn net for FY2023-H1 2026.
4. **A misattributed quotation**: the Q3 draft put *"Buffett's stated base rate"* inside quotation marks, which is the framework's
   paraphrase, not corpus text; rewritten as [E3-48]'s base rate with only the verbatim words quoted.
5. **An unsourced tick**: "peers imitated: the robotaxi entry, after peers'" was not in any Lucid filing; unticked and said so.
6. **Two small figures**: the investments run down in FY2025 were $2.3bn net, not $2.9bn; the A and B preference rise was $203.4M, not
   $203.2M.

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **Hypothesis (a) did not apply**: Lucid has one class of common stock and one undimensioned dei fact; neither HBB layer exists here.
2. **The split was real (the brief's memory was right on the fact, 1:10 effective 2025-08-29) but it was not the cause.** The triage
   guard fired on the yield from the correct post-split count; the brief's hypothesis (c) was the right one, and the wave table's label
   "cap rejected as a broken input" was wrong in both words for LCID.
3. **"The RIVN run's row (Rivian, Lucid, Ford Model e, Tesla, GM, Ford; FY2025 operating margins)"** undersold it: the row is a five-year
   series with Toyota, Stellantis and Honda carried from the TM run, and my recomputation of Lucid reproduced it to the decimal.
4. **"Read the subscription or investment agreements as filed"**: done for the Series C Certificate of Designations and subscription
   agreement and the DDTL credit agreement; the Series A and B certificates were **not** opened, and their step-up is inferred from the
   filed six-month movement, not read. Recorded as a limit.
5. **The prior the brief flagged as most likely wrong** (a pre-profit carmaker is an easy close) was half right: the close came at Q2, on
   Lucid's own pricing record, not at Q4 on the losses; and the Q1 question about non-vehicle revenue turned up something the prior did
   not anticipate: **the one technology licensee and the largest identifiable customer are both in the controlling holder's circle**.
6. **Not in the brief, found by the run:** the 2026 production guidance of 25,000-27,000, reaffirmed on the financing day, is absent from
   every later document read; and `Screens/SURVIVAL SHAPES - index.md` does not list the RIVN run's instance of #8 or the TSLA run's of
   #11, although both run files name them.

### LIMITS OF THIS RUN
- The earnings-call transcripts and slide decks on ir.lucidmotors.com were not read; they are where a spoken withdrawal of the 2026
  guidance, if any, would be.
- The luxury peers' annual reports were not pulled (Q2).
- [E3-70]'s grant-value measure of stock compensation was not computed (it could only lower owner earnings further).
- The watchlist pricing script that wrote the triage row is not on disk (the HBB run's finding); the triage inputs are reconstructed.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business), at Q2** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Lucid sells luxury battery cars that have cost more to build than they sold for in every year, cut prices to sell more
  (FY2023 deliveries +37% on revenue -2%; vehicle revenue per car $96.9k to $73.5k), and sits last in an eleven-name row; the file closes
  at Q2 on [E3-03] criterion 2. Recorded, not governing: Q3 IN on the binary with converging flags (projections, serial issuance, a
  guidance bullseye dropped, adjusted EBITDA, a moved pay target); Q4 OUT, gruesome, owner earnings -$3.3bn (five-year) to -$5.4bn
  (twelve months), shape #8 with #14's feature; price US$4.09 x 394,070,176 = US$1,611.7M, headed COMPUTATION - NOT A CLEARANCE, above
  a range that lies wholly below zero. **FAIL at Q2.**

