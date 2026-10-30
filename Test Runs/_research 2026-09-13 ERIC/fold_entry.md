- **ERIC (Telefonaktiebolaget LM Ericsson), 2026-09-13 - FAIL at Q2 (OUT, ON THE BUSINESS AS CONSTITUTED, ON [E3-03] CRITERION 2 AND
  [E4-04]). Q1 IN; Q3, Q4, Q5 and Q6 RECORDED, NOT GOVERNING under explicit banners (Q3 UNKNOWABLE on the honesty binary with a live
  capital-allocation flag and converging flags; Q4 would be IN on survival with the owner's return as the named death; price headed
  COMPUTATION - NOT A CLEARANCE; Q6 records reopening conditions in words and arms nothing). WAVE 5, the fifth of the eleven foreign
  20-F filers.**
  `Test Runs/2026-09-13 Run - ERIC Ericsson.md` (@@COMMITS@@), `check_framework.py` PASS.
  Price **SEK 98.66** (ERIC-B.ST, Nasdaq Stockholm, 2026-09-11 close, Yahoo, aggregator flagged; ERIC-A.ST SEK 99.00; Nasdaq ADR
  $10.31 the same day, **1 ADS = 1 Class B share** per the 20-F cover, SEK 99.95 at the Riksbank USD/SEK fixing 9.69401; the local B
  quote used) x **3,265,683,059 shares** = cap **SEK 322.2bn**. **Count by hand:** 20-F cover **3,371,351,735 is the ISSUED count**
  (A 261,755,983 + B 3,109,595,752; accession `0001193125-26-104149`), less treasury 38,002,276 at 2025-12-31 (Note E1) = 3,333,349,459;
  **70,349,695 B shares bought back for SEK 7,299.1m (avg SEK 103.75)** under the SEK 15bn program to 2026-09-04 (18 weekly 6-Ks); latest
  6-K 2026-09-08 (`0001628280-26-060848`): treasury **105,668,676** -> **3,265,683,059 outstanding**; the 2,683,295 difference is LTV 2023
  delivery (6-K 2026-05-13). **A and B share economics equally** (Exhibit 2.3: *"the same right to dividends"*; Note E1: *"the same rights
  of participation in the net assets and earnings"*; 1 vote vs 1/10 vote), so they are summed; no C shares; no split. **Sovereign SEK 10-year
  3.227%** (Sveriges Riksbank SWEA `SEGVB10YC`, **2026-09-11**), confirmed at the issuer by the Debt Office's SGB 1068 (2037) auction at
  **3.0909%** on 2026-09-09; **the longest tenor either authority publishes as a daily yield is 10 years, shorter than 30** (SGB 1063
  2045 and 1064 2071 exist, SEK 19.0bn and 10.75bn of SEK 699bn, no daily yield); fetched by hand, **not added to `tools/sources.py`**.
  SEK argued from [E4-15, E3-32] on the filing (reporting, dividend, buyback and quote currency) against a sales base **~99% outside
  Sweden** (US 40.8%, Sweden 1.4%; USD-priced sales SEK 136.9bn of 236.7bn); **USD 30-year 5.35%** and **EUR 3.83%** shown; the ~10% floor
  governs above all three. **The skip reason, tested, and it is NOT the SONY/TM/HMC/TSM cause:** `companyfacts` holds 11 IFRS annual
  periods (2015-2025) **and has ingested the FY2025 20-F**; `tools/run.py ERIC` fails because its tag lists carry **only US-GAAP element
  names** while `sources.annual()` searches `ifrs-full` with those names - every IFRS 20-F filer is unpriceable by construction.
  **Q1 IN:** Networks 64% of sales (radio hardware, software and deployment to ~500 operators; ten largest 46%, largest ~14%; *"do not
  contain committed purchase volumes or prices and may include commitments to future price reductions"*), EBIT 19.7% in 2025 and 11.3% in
  2023; IPR licensing SEK 14.5bn (6.1%); Cloud Software and Services 26%; Enterprise 9% = Vonage (consideration SEK 53.3bn plus SEK 5.9bn
  debt repaid; SEK 31.9bn goodwill impaired 2023, SEK 14.7bn 2024; SEK 9.1bn goodwill left with SEK 2.7bn headroom) and Cradlepoint;
  iconectiv sold August 2025 for a SEK 7.6bn gain. **Q2 OUT:** competitor row, radio segment margin ex-restructuring 2014-2025 - Ericsson
  11.9 / 12.8 / 8.1 / 11.6 / 15.3 / 16.0 / 19.0 / 22.4 / 20.0 / 13.9 / 17.4 / **20.4%** against Nokia's radio segment 11.3 / 10.0 / 8.6 /
  8.7 / 5.9 / 3.4 / 7.9 / 7.9 / 8.8 / 7.4 / 5.3 / **2.8%** (boundaries named each year) - **even through late 4G, 6-18 points ahead in every
  5G year**; Huawei (carrier revenue only, no segment profit), ZTE (carriers' network gross margin 48.09% and an ex-R&D segment result),
  Samsung Networks (not separately disclosed; inside DX and "MX / Networks"), Ciena and Cisco (no radio). **[E3-03](2) fails on both vendors' filings:** Nokia FY2021 *"Almost all CSPs dual source,
  giving vendors no pricing power unless they offer some technology advantage"*; Ericsson 2013 and 2016 *"opened up on a yearly basis to
  renegotiate the price … do not contain committed purchase volumes"*; European installed base bought in the modernisation swap wave (both
  vendors, FY2013); Nokia's filed 4G-to-5G *"conversion rate … 93.5%"*; AT&T *"decided to proceed with an alternative RAN vendor"* (Nokia
  FY2024). **[E2-44](1) fails** (*"continuous price erosion"*, *"continuous price pressure"*; *"the RAN market has been largely flat over
  time but with cyclicality"*). **[E4-04]:** 6G *"expected to begin before 2030"*; the spending (R&D SEK 48.9bn, 20.6% of sales) buys the
  next generation - the excluded class, a surfing run [E3-51]; the 5G-era widening coincides with restrictions on Chinese vendors
  [E2-59]. Patent leg franchise-like but FRAND-priced and under SAMR review (criterion 3). CSS and Enterprise NONE.
  **Q3 (recorded) UNKNOWABLE on the binary:** DPA 2019-12-06 (DOJ USD 520,650,432; SEC USD 458,380,000 + 81,540,000; conduct 2010-2016);
  DOJ breach determinations **2021-10-22** (*"failing to provide certain documents and factual information"*) and **2022-03-02** (Iraq
  disclosure *"insufficient"*, *"failing to make subsequent disclosure"*); the 2019 Iraq report of *"serious breaches"* made public
  2022-02-15 after media reports; guilty plea **2023-03-02**, USD 206,728,848; monitorship concluded June 2024; Nasdaq Stockholm and the
  Swedish FSA closed disclosure reviews in 2023; **open:** DOJ Iraq investigation, three ATA suits naming the CEO, 93 Solna claimants,
  CFIUS NSA (Vonage) investigation. CEO Ekholm leaves 2026-09-30 (internal successor Narvinger). Flags: restructuring charges in every
  year 2012-2025 (SEK 55.4bn) excluded from every headline, target and LTV metric [E3-53, E5-33]; *"Excluding Vonage and previously
  announced charges … reaching the 2022 target"* against a reported 10.0% [E2-57]; EBITA 15-18% by 2024 missed (8.1%, 11.0%); **EBITDA
  zero mentions** in the annual report and three quarterly reports; buyback at ~SEK 342bn implied value against a 4.6-7.0% owner-earnings
  yield - capital-allocation flag; STV on Economic Profit (a capital charge; CEO STV 2025 SEK 22.4m, 183% of target).
  **Q4 (recorded):** owner earnings SEK bn (OCF less share-settled SBC less leases from 2019 less the lower of capex+capitalised development
  or their D&A), **5-yr 2021-25 23.4 (20.2 with the working-capital release removed); 10-yr 15.7 (10.6); 15-yr 13.7; 2016-20 trough 7.5
  (0.4)**; SBC resolves and is complete (share-settled every year; cash-settled plans already in OCF); D&A default valid (capex 1.03-1.15x
  D&A over ten and fifteen years); net cash SEK 61.2bn; SEK 72.7bn of dividends 2016-25 against ~SEK 27bn of net income; **survives;
  named death TM's PASS-THROUGH in an expensed-R&D form with SONY's CAMOUFLAGE in the enterprise leg - no new shape.** **COMPUTATION -
  NOT A CLEARANCE:** yield **3.3-7.4%** against SEK 3.23% (+0.1 to +4.2 points; 4.1-9.2% with net cash netted); 2.6-6.7% perpetual growth
  needed for 10% against 0.3% a year of filed sales growth 2011-2025; floor range **roughly SEK 30-75 a share without growth, SEK 50-90
  with net cash**; **price above the whole no-growth range.** No band armed, no PORTFOLIO row (FOLD step 4). **PASS/FAIL: FAIL at Q2.**
