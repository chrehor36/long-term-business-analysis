- **IHG (InterContinental Hotels Group PLC), 2026-09-13 - FAIL at Q2 (OUT, ON THE BUSINESS, ON [E3-03] CRITERION 2 AS [E2-44](1) AND [E4-37] TEST IT:
  hotel owners have close substitutes, and IHG's filed conduct is that of a seller facing them). Q1 IN; Q3, Q4, Q5 and Q6 RECORDED, NOT GOVERNING under
  explicit banners (Q3 IN on the binary with a live buyback flag and converging flags [E4-52]; Q4 would read IN on survival, great in structure, [E5-11] 1 of 3,
  THE FLAG proposed; price headed COMPUTATION - NOT A CLEARANCE; Q6 records reopening conditions in words and arms nothing). WAVE 5, the last of the eleven
  foreign 20-F filers.** `Test Runs/2026-09-13 Run - IHG InterContinental Hotels.md` (@@COMMITS@@), `check_framework.py` PASS.
  Price **US$153.83** (IHG ADS, NYSE, 2026-09-11 close, Yahoo, aggregator flagged; ADS ratio 1:1 from the 20-F, *"Each ADS represents one ordinary share"*; London
  line US$153.50 the same day - **the London line trades in US dollars since 2026-01-02**, 6-K 2025-12-17 `0001654954-25-014037`, so no FX enters the cap) x
  **146,997,788 shares** = cap **US$22,613M**. **Count by hand:** **147,858,757 ordinary shares in issue excluding 5,431,782 held in treasury at 2026-09-03**
  (buyback report in 6-K batch 2026-09-04, accession `0001654954-26-008134`; walk from 157,126,590 issued incl. 5,481,782 treasury at 2025-12-31, 20-F FY2025
  Directors' Report, accession `0000858446-26-000010`, through 131 daily purchase reports, 3,836,051 shares for ~US$579M, reconciled to the share after a
  50,000-share treasury transfer to the trust; Total Voting Rights 6-K at 2026-08-31, `0001654954-26-008027`, 148,162,113) **less 860,969 held by the ESOT**
  (Note 10 excludes *"other shares that do not receive dividends"* from basic shares; 178,309 nominee shares allocated to participants kept in).
  **The ERIC trap FIRES on the cover:** the 20-F cover "outstanding" figure **164,711,854** is the **2024** issued count **including** 6,241,782 treasury shares,
  repeated unchanged in FY2025 (dei also repeats 187,717,720 for 2020 and 2021): **12.1% too high**. Share consolidations accompanied nine special returns,
  the last January 2019; none after the measurement date. **Sovereign USD 30-year 5.35%** (US Treasury daily par yield curve, **09/11/2026**, `tools/sources.py`);
  USD argued from [E4-15, E3-32] (US-dollar presentation since 2008, dividends declared in cents, US 56.6% of non-fund revenue, Americas 66% of segment profit,
  both quotes in dollars); beside it GBP 20-year 5.65% (Bank of England `IUDLNPY`, 2026-09-09, a rung below the DMO, flagged) and EUR 30-year 3.83% (ECB);
  the ~10% floor governs above it. **The skip reason, tested:** IFRS in USD; companyfacts carries `ifrs-full` only, **unit USD, eleven annual periods 2015-2025,
  FY2025 ingested** - not short history, not the unit filter, not lag: **`tools/run.py IHG` fails on its US-GAAP tag names alone** (the GFS diagnosis).
  **Q1 IN:** Note 3 separates the streams - fee business $1,897M (op. profit $1,231M, margin 64.8%), owned & leased $544M (17 hotels), **System Fund $1,717M and
  reimbursables $1,004M** of $5,189M; rooms 73% franchised, 27% managed; owners pay ~5.4% of system gross revenue in fees and ~4.9% into the fund; key money
  inside cash flow from operations. **Q2 OUT:** key money **$61M (2019) → $237M (2024) → $179M (2025)**; *"fee relief and flexible payment options"* (2020) and a
  2024 cut to *"our standard loyalty assessment fee for owners"* and the Ignite marketing fee in a +3.0% RevPAR year; fee-business gains negotiated out of the
  owners' fund with the IHG Owners Association twice (co-brand licence revenue 2020, points revenue 2024-25); risk factor: renewals may not be *"on similarly
  favourable terms, or at all"*; core toll proxy (franchise and base management fees ÷ system gross revenue) **4.21% → 3.89%** (2019-25, arithmetic, mix limit
  stated); share of six branded systems' rooms **18.1% → 16.9%**. **Row (10-Ks, companyfacts cross-checks matched):** rooms CAGR 2019-25 IHG 2.5%, Marriott 4.3%,
  Hilton 5.7%, Hyatt 8.9% (with acquisitions), Wyndham 0.8%, Choice 1.8%; fee revenue 2020/2019 IHG 0.545, MAR 0.440, HLT 0.493, H 0.393, WH 0.648, CHH 0.678;
  **filed royalty rates: Choice US 4.86% → 4.94% (2020) → 5.14% (2025, US RevPAR −3.0%)**, Wyndham US 4.5% → 4.5% → 4.76%; Hilton raised in-place rates in 2025;
  IHG discloses no rate. Accor not an SEC filer, stated. **Class NONE at the owner level, direction narrowing.**
  **Q3 (recorded):** gate case (daily execution, [E3-43] after a Q2 OUT); binary IN (franchisee class action dismissed with prejudice 2025-05-20; industry antitrust
  suits pending; no restatement); **flags:** two critical audit matters (loyalty breakage; System Fund expense allocation), the cover count, adjusted EBITDA as the
  leverage policy [E4-29], TGR removed from the LTIP after 2020 and adjusted FCF re-presented upward [E2-49], APP pays on signings, adjusted EPS targets *"incorporate
  assumed share buybacks"* [E4-27], 2025 pay policy 69.5% support; **buybacks US$143-165 a share in 2026, executed by GSI *"independently of, and uninfluenced
  by, the Company"*, ~47% debt-funded 2023-H1 2026 (net debt $1,851M → $3,663M against $3.8bn returned)** [E5-08, E5-24]; guidance: fee margin promise kept,
  "industry-leading" net system growth missed; [E4-52] convergence. **Q4 (recorded):** owner earnings with the **System Fund separated** (its result, non-cash
  add-backs and deferred-revenue float removed, its capex not charged; the fund supplied $118-182M a year of consolidated cash in 2023-25) and **SBC complete in
  both places** (2025 $72M = $47M operating + $25M fund; the ifrs tag carries only the first; grant value ~$17-19M a year above the charge, displayed):
  **5-yr 2021-25 $468M (key money = maintenance) / $555M (central, 30% of key money judged maintenance from the ~30% removals replacement ratio) / $593M (key money
  = growth)**; **$339-673M across nine windows**, 2020-21 shown in and out (6-yr incl. 2020 $382-496M; 4-yr ex-trough $481-626M; 2020 alone −$50M to +$14M);
  great in structure; [E5-11] 1 of 3; coverage 6.6x (2.0x in 2020); the 2020 rehearsal (7.7x leverage, covenant waivers, BoE CCFF, dividend withdrawn a year
  after a $500M special); negative equity from the 2005 reorganisation reserve and £8.9bn of returns; **THE FLAG proposed** (a brand flown over a building
  someone else owns, re-flown at term; the inverse of SPOT's THE TENANT and the opposite of MCD, which keeps the land) - **flagged to the operator, register
  unchanged.** **COMPUTATION - NOT A CLEARANCE:** yield **1.5-3.0%** (2.07-2.62% on the default window) against USD 5.35%; **~7.4% perpetual growth needed for the 10%
  floor**; floor range **roughly US$25-90 a share** (0-10% growth for a decade across every base); **price above the whole range.** No band armed, no PORTFOLIO row
  (FOLD step 4). **PASS/FAIL: FAIL at Q2.**
