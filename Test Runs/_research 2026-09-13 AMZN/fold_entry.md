- **AMZN (Amazon.com, Inc.), 2026-09-13 - FAIL at Q2 (OUT, ON THE BUSINESS AS CONSTITUTED, ON [E3-03] CRITERION 2 AS [E3-03]'S OWN PRICING SENTENCE, [E2-44](1)
  AND [E4-04] TEST IT: the AWS leg, 58% of operating income on 76% of H1 2026 net plant additions, has had price move against its sales in every filed year
  2013 to H1 2026 and sells what three filed rivals sell; the stores compete on price by their own description; advertising files no price and does not carry the
  weight). Q1 IN; Q3, Q4, Q5 and Q6 RECORDED, NOT GOVERNING under explicit banners (Q3 IN on the binary, gate case on daily execution, capital-allocation flag on the
  2022 repurchase, soft [E2-49] fire; Q4 would read UNKNOWABLE on the level of owner earnings, [E5-11] 1.5 of 3, THE ROUND TRIP proposed; price headed COMPUTATION -
  NOT A CLEARANCE; Q6 records reopening conditions in words and arms nothing). WAVE 5, the second of the eight "capex unresolved [E5-20]" names; resumed from disk
  after the first session was killed by a session limit.**
  `Test Runs/2026-09-13 Run - AMZN Amazon.md` (Step 0 and Q1 `1327743`, Q2 `006a110`, Q3-Q6 and audit `a30a6cb`), `check_framework.py` PASS.
  Price **US$256.78** (2026-09-11 close, `tools/run.py` chart feed, aggregator flagged) x **10,786,313,572 shares** = cap **US$2,769.7bn**. **Count:** 10-Q cover
  (accession `0001018724-26-000026`) *"outstanding as of July 22, 2026"*, single class; balance sheet 10,783M at 2026-06-30; no split after the measurement date (last
  20-for-1 in 2022). **Sovereign USD 30-year 5.35%** (US Treasury daily par yield curve, **09/11/2026**), struck at Step 0 and re-struck unchanged at the resume.
  **Live deal: Amazon is the ACQUIRER** of Globalstar (~$10.9bn including debt, cash or 0.3210 shares, close expected 2027; ~0.2-0.4% dilution); the quote is not a
  spread. **$50.0bn of OpenAI Series C bought in 2026** ($21.3bn after June 30).
  **The skip reason, tested - it was a TOOLING ARTEFACT, not a capex finding:** `Screens/floor_screen.py` at `a8bc84f` (the commit that wrote the "capex unresolved"
  row) returns `CAPEX_UNRESOLVED` for Amazon because its `annual()` read only the first capex tag with data (`PaymentsToAcquirePropertyPlantAndEquipment`, ending
  FY2016) and never `PaymentsToAcquireProductiveAssets`; the union fix `dff6ab6` landed fourteen hours later and the row was never re-triaged. The current screen
  prices Amazon (5y capex end -13,770; 3y 961) and reproduces to the dollar as gross capex plus finance-lease additions. **Whether [E5-20] applies is a separate
  question, answered on the filing: yes, for the plant that is most of the spending** - *"Effective January 1, 2025 we changed our estimate of the useful lives of a
  subset of our servers and networking equipment from six years to five years ... due to the increased pace of technology development, particularly in the area of
  artificial intelligence and machine learning"* - so the D&A end is INVALID and (c) is judged upward. **The other six names in the row should be re-run through the
  current `owner_earnings()` before their runs.**
  **Owner earnings, audited (`oe.py` inputs re-read against every filed cash-flow statement FY2016-TTM; one unused input wrong, corrected in `oe2.py`):** 5-yr 2021-25
  **-$10.8bn to -$14.8bn on every capex construction** (gross capex, + finance-lease additions, net + lease and build-to-suit additions, cash plant with lease
  principal, total net additions), **+$27.6bn at (c) = 1.3x P&E depreciation** (renewal at current scale ~1.21x, CONVENTION), +$36.7bn at the INVALID D&A end; TTM
  **-$28.8bn to -$60.7bn** capex ends, +$77.4bn at 1.3x; 8 years excluding 2021-22 -$2.0bn to +$7.4bn capex ends. **SBC resolves and is complete** (20.9% of OCF
  2016-25, 12.0% TTM; equity-statement line within 1.6%). Working-capital flag fires 2017 (AP +38.7% of OCF), 2021 (-39.2%), 2022 (-46.8%). Marks removed inside OCF
  (-$79.8bn non-operating, +$41.4bn deferred tax, TTM). **The band changes the sign: Q4 recorded UNKNOWABLE on the level.**
  **Q1 IN** (killed session): AWS 58% of TTM operating income, 36.8% margin, return on average segment assets 25.0% / 30.1% / 22.3% / 18.1% TTM; advertising $76.1bn
  TTM; ~$240bn carried in two private AI laboratories, kept out of owner earnings. **Q2 OUT:** AWS MD&A *"partially offset by pricing changes"* every year FY2013-H1
  2026 (*"driven largely by our continued efforts to reduce prices"* to FY2021, *"primarily driven by long-term customer contracts"* since); FY growth AWS +19.7% vs
  Intelligent Cloud +29.7%, Google Cloud +35.8%, OCI +76.9%; margin AWS 35.4% vs IC 41.3%, GC 23.7%; backlog AWS $496bn vs MSFT $678bn, ORCL $664bn, GC $513.9bn;
  Microsoft books $24.1bn a year from OpenAI, AWS's largest new committer; Oracle *"multicloud services ... work with ... Amazon Web Services"*; server lives shortened
  for AI [E4-04]. Stores: *"principal competitive factors ... selection, price, and convenience"*; Walmart eCommerce +24.4% on ~$150bn against Amazon North America
  +10.0%. Marketplace: no seller or Prime fee change in any Amazon filing; seller unit mix flat 60-62%. Advertising: +22.1% / +25.1%, no price, unit or margin figure
  filed. **Row (peers/competitor_row.md, tableB_retail.md, tableC_ads_and_cloud_text.md, 9 companies with accessions).** **Class NARROW, direction MIXED, the capital
  going into the narrowing leg.** **Q3 (recorded):** EBITDA absent; guidance met or beaten 6 of 6; $6.7bn of "special" charges in two quarters, disclosed; shares
  +6.0% since 2021; cash taxes 29.8% -> 3.8% of pre-tax, explained; lease-adjusted FCF measures dropped as FCF fell [E2-49, soft]; $6.0bn repurchase in 2022's
  negative-FCF year [E5-08 flag]; pay is time-vested RSUs, $365,000 salaries, no bonus. **Q4 (recorded):** good, travelling (AWS ~12.5% pre-tax on incremental
  segment assets); [E5-11] 1.5 of 3: $123.0bn liquidity less $21.3bn to OpenAI; commitments $439.7bn -> $650.0bn in six months; long-term debt face $68.8bn ->
  $133.0bn in six months; [E2-54] not met on TTM FCF of -$7.6bn. **THE ROUND TRIP proposed as the eighteenth shape** (Amazon funds its largest cloud customers,
  books their commitments as backlog - at least $200bn of the $252bn six-month increase - marks their equity up at rounds its own cash joins, and borrows to build
  the capacity; beside #1 CONTRACTED NOT TO STOP and #8 THE EQUITY IS THE REVENUE; a later instance of #11 THE PASS-THROUGH).
  **COMPUTATION - NOT A CLEARANCE:** yield -0.5% to +2.8% (3.3% at the INVALID end) vs 5.35%; 7.0-8.9% perpetual growth needed for the 10% floor from a judged base,
  refused from the negative ones (DCF engine 15.0% a year for ten years, then 3%, from the best judged year); value at the floor roughly $25-40 (five-year judged)
  to $150-190 (5-6% forever on the best judged year) a share; price above the whole range. **Reversal conditions, in words:** AWS's MD&A stops citing pricing
  changes against sales for a full year; AWS leads the row on both growth and margin with lower capital intensity; a filed advertising price or margin series with
  advertising and marketplace carrying most of operating income; the antitrust suits resolved without structural relief. **No alert, no PORTFOLIO row (Q2 OUT).**
  **Defects found:** the wave 5 "capex unresolved" label is a pre-`dff6ab6` tag-union artefact for AMZN and may be for others in the row; the current screen's D&A
  end reads the broad cash-flow D&A line (57% above P&E depreciation for Amazon); the killed session's Table A pricing sweep omitted the subject's own filings; brief
  errors: WMT filings were already on disk, "AWS's lead in Table A" (AWS leads no Table A measure), and "sellers pay rising fees" (no fee change is filed).
