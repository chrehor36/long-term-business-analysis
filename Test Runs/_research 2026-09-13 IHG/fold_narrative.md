
## UPDATE 2026-09-13 - IHG: Q2 OUT, a hotel flag that pays owners more each year to fly it
`Test Runs/2026-09-13 Run - IHG InterContinental Hotels.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded (no disqualifier, gate case, buyback flag,
converging flags); Q4 recorded (would read IN on survival; THE FLAG proposed); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing
armed.** Price **US$153.83** x **146,997,788 shares** = cap **US$22.6bn**; sovereign **USD 30-year 5.35%** (US Treasury, 09/11/2026). **The first hotel
company run in this project, and the last of the eleven foreign 20-F filers in wave 5.** @@COUNT@@

### THE SKIP REASON, TESTED - TAG NAMES, AND A COVER COUNT THAT WOULD HAVE MISPRICED IT ANYWAY
- IFRS in US dollars; companyfacts holds eleven annual USD periods to FY2025. **Not short history, not the unit filter, not lag: `run.py`'s US-GAAP tag
  names**, exactly as at GFS.
- **Had the tags resolved, the cap would still have been 12.1% too high.** The 20-F cover "outstanding" figure is the prior year's issued count including
  treasury shares, repeated unchanged (164,711,854 for FY2024 and FY2025; 187,717,720 for FY2020 and FY2021 in dei). **ERIC's trap, in a worse form: issued, and a
  year stale.** The true count comes from the Total Voting Rights 6-Ks and the daily buyback reports, less the employee trust.
- **The brief's premise that the London line trades in pence is out of date:** it has traded in US dollars since 2026-01-02.

### THE BRIEF'S QUESTIONS, ANSWERED FROM THE FILED RECORD
- **System Fund separation:** the fund's cash sits in consolidated operating cash flow in three places (its result, its non-cash add-backs, its deferred-revenue
  float) and its capex in investing; IHG even pays the fund interest on the cash it holds (*"System Fund interest | 20 | 25"*, H1 2026). **Separated, the fund
  supplied $118-182M a year of the consolidated cash in 2023-25.**
- **SBC resolves in two places:** operating and System Fund lines; the ifrs companyfacts tag carries only the operating line (47 of 72 in 2025).
- **Key money:** inside operating cash flow at IHG and at all five peers. $61M (2019) to $237M (2024) to $179M (2025). Judged ~30% maintenance of unit volume
  from the removals replacement ratio; both ends displayed.
- **Owner earnings, five-year default:** $468M / $555M central / $593M; $339-673M across nine windows with and without 2020-21.
- **Competitor row:** Marriott, Hilton, Hyatt, Wyndham, Choice from their 10-Ks, companyfacts cross-checks matched; Accor not an SEC filer.

### WHY OUT AND NOT UNKNOWABLE
- **For IN:** removals of ~1.5% underlying imply hotels stay in the system for decades; 66% of room nights come through the loyalty programme; the system grew
  through 2020; fee revenue fell less than RevPAR.
- **Against, and decisive:** the customer is the hotel owner, who owns the building and can re-flag it at term; IHG's own risk factor says renewals may be on
  worse terms; IHG pays rising key money, cut owners' loyalty assessment in a good year, and grew its fee business partly by negotiating revenue out of the
  owners' fund; its share of the branded systems' rooms fell for six years; a peer (Choice) raised its filed royalty rate through 2020 and 2025. **The documents
  that decide criterion 2 exist and were read; they agree.**

### REFUTED OR NARROWED PRIORS
- **"Asset-light franchisor = MCD-class franchise" is refuted as a transferable prior.** McDonald's passed Q2 because it keeps the land at the end of every term;
  IHG owns 17 of 6,963 hotels. **The land, not the franchise contract, carried MCD's criterion 2.** Any future franchisor run should ask who owns the site first.
- **"Fee resilience in 2020 shows pricing power" is narrowed:** fee revenue fell less than RevPAR at every hotel company in the row by a similar ratio (0.87-0.93
  of the RevPAR decline for IHG, Hilton, Wyndham, Marriott); fixed per-room technology fees, not a price rise, are the cushion.
- **The [E2-49] metric-withdrawal prior fired here** (TGR removed from the LTIP after 2020; adjusted FCF re-presented upward). The running tally is not
  restated: the reading list records it as stale, and later folds have moved it.

### NEW FOR THE OPERATOR
- **A proposed survival shape, THE FLAG** (it would be the sixteenth, after THE TENANT, THE PATRON and THE DOWRY, none registered): a brand flown over a building
  someone else owns, re-flown at term, whose take is set by rivals bidding for the same buildings and whose leverage is sized on the EBITDA that rivalry permits.
  **The register is unchanged.**
- **No single list of registered survival shapes exists on disk** (GFS noted it; this run rebuilt it again from the register and found ACMR's run numbering a
  shape "fifth" that the reading list numbers differently). A one-page shape register would stop every run rebuilding it.
- **The hotel row is now on disk** (`Test Runs/_research 2026-09-13 IHG/peers/`): five 10-K rows with royalty rates, contract terms, key money, loyalty and
  verbatim competition language, for any later run on MAR, HLT, H, WH or CHH.

### TOOLING AND SOURCE DEFECTS FOUND
- **`run.py` / `sources.annual()` US-GAAP tag names** block every IFRS filer, USD or not (confirmed on two USD filers, GFS and IHG, where no other cause is present).
- **`dei:EntityCommonStockSharesOutstanding` can be stale and can include treasury shares on a 20-F cover**; a screen should never take it as outstanding for a
  foreign private issuer without the Total Voting Rights or share-capital note.
- **The ifrs SBC tag misses System Fund (or any segregated-fund) share-based cost**; SBC "resolves" in the tag and is still incomplete.
- **The BoE database has no 30-year par gilt series in the codes tried** (`IUDLNPY` is 20-year); GBP 30-year from the DMO was not fetched, and did not matter
  because the earnings currency is USD.
