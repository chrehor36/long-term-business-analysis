- **SGC (Superior Group of Companies, Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 21 of 218. Register entry 153** (re-derived, not inherited: line-start
  `^- \*\*` counted **by index** in the slice from this file's `## COMPLETED FROM THE QUEUE`
  heading LINE (index 501, i.e. line 502 - the string occurs about a dozen times as an inline
  mention and a bare search lands on the wrong one) to the `## THE WRITE-EARLY PROTOCOL` heading
  LINE (index 12367, i.e. line 12368). **152 entries stood above this one**, which is exactly
  what the dispatch brief predicted, and **SGC appeared NOWHERE else in the file**. After
  insertion: 153.)
  **Price US$12.36**, the live quote at **2026-09-21 09:44 ET**, aggregator (Yahoo Finance chart
  endpoint), **flagged as an aggregator, live quote only**; raw metadata saved to
  `Test Runs/_research 2026-09-21 SGC/price_raw_aggregator.json`. The five prior closes were
  12.47 / 12.57 / 12.40 / 12.45 / 12.40, so the quote is not an outlier print.
  **Shares 15,945,201, a SINGLE class of common stock, $.001 par**, read off the cover of the
  **10-Q for the quarterly period ended 2026-06-30, accession `0001437749-26-025511`, filed
  2026-08-04**, as-of date 2026-07-30, verbatim: *"The number of shares of common stock of the
  registrant outstanding as of July 30, 2026 was 15,945,201 shares."* No split after the
  measurement date (`split_factor_after('SGC','2026-07-30')` = 1.0); no second class (the FY2025
  balance sheet reads *"Preferred stock, $.001 par value - authorized 300,000 shares (none
  issued)"*).
  **CAP, STRUCK BY HAND: 15,945,201 x $12.36 = $197.1M.** The screen carried **$196M**.
  **+0.6%, and the screen cap REPRODUCES**: 196 implies $12.29, a stale-price difference and not
  a count error. This is the ADM and IIIN shape, not the BELFB (6.29x) or FC (18%) shape.
  **Sovereign 5.34%, US Treasury daily par yield curve, 30-year par yield, 2026-09-18** (the
  newest published print; 2026-09-21 is a Monday), struck fresh from the issuing authority
  through `tools/sources.py`. **FRED DGS30 not used.** Not inherited from the brief, which
  deliberately supplied none.
  **PASS/FAIL LINE: Q1 IN, Q2 OUT. Q2 closed the file, on [E3-03] criterion 2 - the product has
  close substitutes, and the registrant says so itself.** The FY2025 10-K calls the Branded
  Products market *"a multitude of national and regional companies"* plus *"local firms in most
  major metropolitan areas"*; the Contact Centers market *"highly competitive and fragmented"*,
  where *"Nearshore operators can provide comparable service to their U.S. counterparts at a
  fraction of the price"*; and its own inputs are *"widely available"* with substitutable
  alternatives. The furnished Q2 2026 earnings release calls all three markets *"large,
  fragmented and growing"*. **[E4-04] did NOT decide this file and was not used to** - under the
  ruling of 2026-09-20 it is a competence limit, and durability here is judgeable from the
  filings, so this is an OUT on the business, not the perimeter close.
  **COMPETITOR ROW: ten named rivals, specification stated in advance, every ratio computed in
  session from each filer's own SEC annual filing.** Superior consolidated: operating margin
  **2.36%**, ROCE **4.27%**. Cintas 23.14% / 33.24% · IBEX 24.58% ROCE · Cimpress 6.72% /
  17.59% · TaskUs 11.88% / 15.85% · Lands' End 3.32% / 8.40% · FIGS 6.04% / 7.79% · UniFirst
  7.59% / 7.42% · Vestis 2.36% / 2.58% · Concentrix -9.34% · TTEC -5.48%. **Superior is last or
  joint-last of the ten.** Fifteen private rivals named as unseen; 4imprint plc files in the UK
  and was not fetched, and that limit is named in the run file.
  **THE HARDEST FACT, and it is the company's own accounting:** goodwill ran $4.1M (2015) to
  $39.4M (2021) to **ZERO at 2022-12-31** on a *"non-cash goodwill impairment charge of $45.9
  million"*, plus $5.6M of trade names, plus a further **$2.6M tradename impairment in Q2 2026**.
  **$172.9M of acquisition cash over sixteen filed years - 88% of today's market capitalisation -
  and the premium is written off.**
  **THE SCREEN ROW'S [E4-25] REBUILD, DONE.** The published band $13M-$35M is the 3-year and
  5-year corner of the table. Rebuilt over all sixteen filed years the owner-earnings mean is
  **$9.4M-$10.5M**; the combined range across five windows and the capex band is **$9.4M to
  $35.1M**, a 3.7x width, and **$0.5M to $35.1M** once FY2023's $24.7M inventory release is
  normalized out under [E4-41]. Under [E4-25] that width would itself have been the Q4 verdict.
  **Carried as COMPUTATION - NOT A CLEARANCE; Q4 was never reached and no verdict is entered
  against it.**
  **NO PRICE BAND, and no `tools/alerts.json` entry** - the QLYS ruling of 2026-09-07: a name
  that failed on the BUSINESS gets no price alert, because a price alert on it is a category
  error. **Reversal condition in words:** two consecutive years of rising gross margin rate in
  Branded Products AND Healthcare Apparel while input costs rise, in the 10-K's own MD&A
  language, together with organic segment revenue growth above 5%. Price is not a reopening
  condition at any level.
  Run file: `Test Runs/2026-09-21 Run - SGC Superior Group of Companies.md`. Research:
  `Test Runs/_research 2026-09-21 SGC/`.
