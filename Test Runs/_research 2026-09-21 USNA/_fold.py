import io
P="Screens/WATCHLIST RUN QUEUE.md"
s=io.open(P,encoding="utf-8").read()
assert "USNA" not in s, "USNA already present - abort"
entry = """## COMPLETED FROM THE QUEUE
- **USNA (USANA Health Sciences, Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. `Test Runs/2026-09-21 Run - USNA USANA Health Sciences.md`. Price **$14.40**
  (2026-09-21, aggregator, flagged) x **18,476,534 shares** of common stock, **one class**, from
  the **10-Q cover at 2026-08-11, filed 2026-08-13, accession `0000896264-26-000056`** = cap
  **$266.1M**. Sovereign **5.34% USD** (US Treasury daily par yield curve, 30 Yr, 09/18/2026).
  Filing read: **10-K FY ended 2026-01-03, filed 2026-03-16, accession `0000896264-26-000021`**,
  plus that 10-Q, the **DEF 14A `0000896264-26-000026`** and the three 8-K EX-99.1 earnings
  releases (`...-26-000014`, `...-26-000030`, `...-26-000050`). FY2025 OCF **$22,349**, SBC
  **$13,828**, D&A **$32,562** and capex **$13,823** each cross-checked against the filed
  cash-flow statement; net sales $925,257 and operating earnings $37,432 against the filed
  income statement.
  **THE SCREEN'S CAP FLAG IS A FALSE POSITIVE AND THE DEFECT IS OURS.** The row said *"CAP BELOW
  FILED PUBLIC FLOAT - cap $263M against a filed float of $328M (1.25x) as of 2025-06-27. A cap
  cannot be smaller than a subset of itself."* **Neither input was wrong: the comparison was.**
  The $328M is the cover-page non-affiliate market value struck *at a $31.13 close on 2025-06-27*
  - which the price series matches to the cent - while the cap is struck at $14.40 fifteen months
  later, a **53.7% fall**. Implied non-affiliate count 10.5M shares against ~19M outstanding,
  consistent with **Gull Global (the founder Dr Myron Wentz) at 40.1%** per the proxy. `cap_flag`
  compares a live cap with a figure the SEC requires to be struck at the last business day of the
  prior second fiscal quarter, so it can be **eighteen months stale**; in a halved stock it prints
  arithmetic impossibility. **It still did its job** - it sent the run to the cover page.
  **Q2 OUT, and the registrant says it twice in its own 10-K.** Item 1 Competition: *"Our business
  through USANA, Hiya, and Rise is **very competitive and the barriers to entry are not
  significant** ... many of our competitors are significantly larger ... and greater financial
  resources."* Item 1A: *"Entry to market is **not particularly capital intensive or otherwise
  subject to high barriers** and as a result, **new competitors can enter easily and compete with
  us for customers and distributors**."* **[E3-03] condition (2) is denied by the subject**, and
  the row's own demonstration test - aggressive pricing producing high returns on capital - fails
  in **both** halves: average spend rose **4.4%** on FY2025 price increases while **active
  Customers fell 14.8%** ([E2-44] first characteristic), and return on equity went **28-33% every
  year FY2010-FY2021 to 16.0 / 12.8 / 7.9 / 2.0%**, operating margin **15.6% (FY2020) to 4.0%**.
  **[E4-55], the units series, read from each year's own 10-K:** active Customers **616,000
  (FY2018) -> 387,000 (FY2025) -> 384,000 (2026-07-04), minus 37%**, down in all four regions in
  FY2025. Consolidated net sales nonetheless *rose* 8.3% in FY2025 - **only because $130.0M of
  purchased Hiya revenue was added.** Dollar revenue flattered by price and by an acquisition is
  Precision Steel's shape exactly.
  **THE COMPETITOR ROW - 7 listed peers, same metric, same window, each from its own SEC-filed
  accounts** (HLF, NUS, MED, NHTC, MTEX, LFVN, BODI; Amway, Mary Kay and Melaleuca are private and
  file nothing, and are the larger rivals USANA names against itself). **Seven of seven are below
  their in-window peak**: NUS -45%, MED -76%, NHTC -79%, BODI -71%, MTEX -38%, HLF -13%, LFVN -21%,
  USNA core -35%. Three of seven lost money at the operating line in FY2025. Peer unit series agree
  from their own filings - Nu Skin *"Customers decreased 10%, Paid Affiliates decreased 11% and
  Sales Leaders decreased 19%"*; NHTC *"14% fewer active members"*; Medifast *"a decrease in the
  number of active earning coaches"*. **That is [E3-51]'s broken wave, not a moat** - USANA led the
  row on margin in FY2018 (15.8%) and now sits below Herbalife (9.5%). **[E4-36]**'s fourth cause,
  wave-riding, is the honest account of the 2010-2021 record; a surfing run is not ownable.
  **PERIMETER (the screen's $210M note): TWO events, not one.** Rise and Oola, FY2022,
  **$6,532 thousand** - immaterial. **Hiya Health Products LLC, closed 2024-12-23, $206,074
  thousand cash for 78.85%** (Note B), of which intangibles $124,200 and **goodwill $127,264**.
  $209.9M total = **78.9% of the re-struck cap**. **One real break in the series, at FY2025** (first
  full Hiya year; D&A $14,539 -> $32,562 almost entirely on acquired-intangible amortisation), plus
  a 53rd week in the same year. **$29,137 of the Hiya goodwill was impaired in Q2 2026, eighteen
  months after closing.**
  **SPREAD REBUILT ACROSS ALL 17 FILED YEARS AND BOTH (c) ENDS** - the row's `spread_caveat` asked
  for it: **owner earnings $17.0M to $79.0M, a 4.6-fold range, 6.40% to 29.67% on the cap.** The
  screen's 3y/5y-only construction saw $17M-$49M; **the rebuild widens the top end by 61%**. 5-yr
  (the [E2-42] default) $44.4-49.4M; 3-yr $17.0-24.2M, **below the [E4-28] floor at both ends**;
  **FY2025 alone is negative at both ends, $(24.1)M to $(5.3)M**. [E4-25]: a range that wide *is*
  the conclusion.
  **THE "STEP DOWN" IS A SIX-YEAR SLIDE, NOT A STEP.** The three level flags (0.39 / 0.23 / 0.48)
  are numerically right and mis-captioned. Rolling 5-year owner-earnings mean: **$108M -> $105M ->
  $89M -> $77M -> $44M**, falling at every anchor. Two hinges with filed reasons: **FY2022** (post-
  pandemic normalisation; sales -15.8%, units -12.5%) and **FY2025** (units -14.8%, first Hiya year,
  $6,463 cost realignment plus $6,967 impairment, and a **72.4% effective tax rate** because foreign
  losses earn no benefit - the valuation allowance went $156.1M to $178.7M).
  **RECORDED BENEATH THE CLOSE, GOVERNING NOTHING.** **[E4-29] and the projections flag fire in the
  furnished 8-Ks, not the 10-K** (the standing CGNX rule): Adjusted EBITDA and Adjusted diluted EPS
  head the Key Results table of all three releases - **FY2025 GAAP net earnings $10.8M against a
  headline Adjusted EBITDA of $101.3M; GAAP diluted EPS $0.58 against Adjusted $1.93** - and the
  **Hiya put price is contractually set on Hiya's Adjusted EBITDA** (Note O). FY2026 guidance issued
  2026-02-17 at **net earnings $20.3-26.6M**, *"reaffirming ... across all metrics"* on 2026-05-05,
  **cut to $(11)M on 2026-08-04** ([E3-48] performed on the record). **[E5-08]/[E5-24]: $281.7M of
  buybacks in six years, $177.8M of it in FY2021 when the stock closed at $101.20, and $27.5M in
  FY2025 at $29.92 a share against $14.40 today** - against a whole company now worth $266.1M.
  **[E3-54] retention: $302.4M of earnings retained FY2021-FY2025 while market value went from
  ~$1.94bn to $266.1M** - negative market value per dollar retained. **[E4-30]'s cash-tax tell does
  NOT fire and is recorded as not firing** - cash taxes *rose* to 89.5% of pretax. **No integrity
  finding of any kind**; no verdict taken at Q3 (operator rule 2). Balance sheet at 2026-07-04:
  **cash $168,560 thousand - 63% of the market cap - zero drawn debt**, redeemable NCI $44,667 in
  the mezzanine, puttable from 2028-04-30 and 2030-04-30 and shrinking as Hiya shrinks. **The named
  death is not insolvency but the arrival at net cash**: on the company's own core guidance plus the
  filed SG&A stickiness, consolidated operating earnings cross zero around FY2027-FY2028 - **a real
  possibility**, with the counter-case ([E4-51]) stated in the run: it is a balance-sheet case, and
  Q2 is a business gate. **No band armed and no PORTFOLIO row** (the QLYS ruling); the reversal
  condition is in words at Q6.
  **Register entry 156**, counted from this file at fold, never carried forward."""
s=s.replace("## COMPLETED FROM THE QUEUE",entry,1)
io.open(P,"w",encoding="utf-8").write(s)
print("register written")

# step 2
W="Screens/_daily/_wave7_done.txt"
t=io.open(W,encoding="utf-8").read()
assert "USNA" not in t
if not t.endswith("\n"): t+="\n"
t+="USNA\n"
io.open(W,"w",encoding="utf-8").write(t)
print("wave7_done lines:",len([x for x in t.split("\n") if x.strip()]))
