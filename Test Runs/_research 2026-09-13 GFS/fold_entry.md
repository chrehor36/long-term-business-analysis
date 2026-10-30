- **GFS (GLOBALFOUNDRIES Inc.), 2026-09-13 - FAIL at Q2 (OUT, ON THE BUSINESS, ON [E3-03] CRITERION 2 AS [E3-43] DEMONSTRATES IT, AND
  [E2-44](1)). Q1 IN; Q3, Q4, Q5 and Q6 RECORDED, NOT GOVERNING under explicit banners (Q3 IN on the binary, no integrity disqualifier, with the
  weak-accounting, EBITDA and metric-switching flags, a live buyback flag on US$500M paid to the controlling shareholder, and seven converging
  prompts; Q4 would be OUT on [E4-20], gruesome, with THE PASS-THROUGH likely and THE PATRON proposed as a new shape; price headed COMPUTATION -
  NOT A CLEARANCE; Q6 records reopening conditions in words and arms nothing). WAVE 5, the ninth of the eleven foreign 20-F filers.**
  `Test Runs/2026-09-13 Run - GFS GlobalFoundries.md` (@@COMMITS@@), `check_framework.py` PASS.
  Price **US$46.95** (GFS, Nasdaq, 2026-09-11 close, Yahoo, aggregator flagged; ordinary shares listed directly, **no ADR**) x **558,658,481 shares**
  = cap **US$26,229M**. **Count by hand:** **548,751,082 issued and outstanding at 2026-06-30** (Q2 2026 interim statements, 6-K filed 2026-08-05,
  accession `0001709048-26-000219`) **plus 9,907,399 shares agreed to be issued to the U.S. Department of Commerce at US$37.85 on 2026-09-03** (6-K
  2026-09-08, `0001709048-26-000234`; completion not confirmed in any filing, included so the cap is not understated by 1.8%; 9,907,399 x US$37.85 =
  US$375.0M, the amount of an announced DOC quantum grant, a link that is arithmetic only). Walk: 20-F FY2025 cover **555,888,455 outstanding**
  (`0001709048-26-000022`) -> 7,344,840 bought from Mubadala at US$40.845 (2026-03-13) -> ~2.3M bought in the open market at US$43.88 (H1 2026).
  **The ERIC trap checked and it does NOT fire:** the cover says outstanding, the balance sheet says the same number is *"issued and outstanding"*,
  and repurchased shares are cancelled, not held in treasury. No split. **Sovereign USD 30-year 5.35%** (US Treasury daily par yield curve,
  **09/11/2026**, struck via `tools/sources.py`); USD argued from [E4-15, E3-32] (*"The majority of our sales are denominated in U.S. dollars"*,
  statements and quote in dollars); the ~10% floor governs above it. **The skip reason, tested:** GFS reports **IFRS in US dollars**;
  companyfacts carries `ifrs-full` only (no `us-gaap`), **unit USD, seven annual periods 2019-2025, the FY2025 20-F ingested**; so neither the
  USD-unit filter nor ingestion lag is the cause - **`tools/run.py GFS` fails on its US-GAAP tag names alone** (ERIC's diagnosis, on a USD filer).
  The short history is real but not the reason: five comparable years (post-IPO, post-2021 useful-life change) consume the whole default window.
  **Controlling shareholder:** Mubadala **81.0% (2025-12-31) -> 72.82% (2026-06-30)** (Schedule 13G/A No. 3, `0001140361-26-032099`); Form 144 of
  2026-05-26 for 22,000,000 shares at US$89.96; consent rights over equity issuance, M&A above US$300M, debt above US$200M and the CEO, CFO and CLO;
  majority board designation; auditor aligned to Mubadala's (KPMG -> PwC, 2024); Nasdaq 5605(e) and 5635 home-country exemptions.
  **Perimeter, from the filings:** EFK to onsemi closed 2022-12-31 (not separately disclosed; the 3-yr window is post-EFK); SMP 2025-01-02 US$64M;
  MIPS 2025-08-13 US$226M; InfiniLink 2025-11-14 US$48M; AMF 2025-11-18 US$453M; Synopsys ARC 2026-06-01 US$455M; no foundry combination filed.
  **Q1 IN:** specialty (not leading-edge) foundry paid per wafer; Smart Mobile 39%, Automotive 21%, Home and Industrial IoT 18%, Communications
  Infrastructure & Data Center 11%, non-wafer 11% (2025); shipments **2,472k / 2,211k / 2,124k / 2,345k** (2022-25) at utilisation **101 / 81 / 77 / 86%**;
  top ten 63% of volume, Customer A 16.4% and C 13.9% of wafer revenue; single-sourced **63% of volume** (company belief, volume not revenue).
  **Q2 OUT:** filed ASP **+17% (2022), flat (2023, with underutilization payments inside wafer revenue), -3% (2024), -10.4% (2025, as utilisation rose)**,
  Smart Mobile down on *"pricing adjustments where customers are dual sourced"*; ROE **-3.4 / 16.2 / 9.7 / -2.4 / 7.8% (2021-25, mean 5.6%)**; LTA book
  ~$22bn -> ~$11bn; prepayments US$1,983M -> US$1,230M. Customers' filings both ways (Cirrus Logic: transfer *"may not be possible"*; AMD: 12/14nm
  *"primarily"* GF through a WSA priced to 2026 - against: Cirrus and AMD also at TSMC, Qualcomm names TSMC, Samsung and GF, Himax names eight, Navitas
  qualifies GF as the US substitute for TSMC GaN, Tower names *"GlobalFoundries (mainly in the RF space)"* its most direct competitor). **Row, gross
  margin 2025:** TSMC 59.9, UMC 29.0, **GFS 24.9**, Tower 23.2, SMIC 21.0, Hua Hong 11.8; **ROE 5-yr:** TSMC 32.3, UMC 18.8, Tower 13.0, **GFS 5.6**
  (Tower recomputed; others cited from the TSM and UMC runs). GF sued Tower at the ITC in March 2026. Location advantage recorded as a regime
  [E2-59]. **Class NONE.**
  **Q3 (recorded):** weight case daily execution (gate); binary IN (IBM fraud claim reinstated on appeal, settled confidentially 2025-01-02; export
  breaches self-disclosed); **flags:** material weaknesses at the 2023, 2024 and 2025 year-ends; useful lives 5/8 -> 10 years in the IPO year
  (US$628M); US$935M Q4 2024 impairment before the CEO change; adjusted EBITDA in every release; **PSU yardsticks (absolute ROIC, relative TSR vs
  SOX) modified September 2023 and replaced from 2024** by revenue, adjusted FCF % revenue (OCF less capex plus grants, no SBC) and absolute TSR set
  annually [E2-49, E4-27]; **buybacks US$200M at US$50.75 (2024) and US$300M at US$40.845 (2026) from Mubadala, US$100M at US$43.88 open market**,
  all above the floor range [E5-08]; first dividend (July 2026) in the year shares were issued to the DOC [E2-52]; guidance beaten 18 of 18 quarters;
  CEO, CFO and COO changed in eleven months; [E4-52] convergence recorded. **Q4 (recorded):** owner earnings US$M (OCF - SBC at grant value [E3-70]
  - change in contract liabilities (prepayments in operating cash, TSM's strip) - (c), grants in (c), acquisitions displayed): **5-yr 2021-25
  234-248; 4-yr 484-519; 3-yr 396 (capex end invalid, trough under-spend); TTM 1,072 display**; 98 with acquisitions; 453-467 without the strip;
  only five comparable annual periods; net cash ~US$2.2bn; **gruesome [E4-20], OUT**; **THE PASS-THROUGH (likely); THE PATRON proposed as a
  fourteenth shape** (the regime that funds the plant sets and changes the terms: CHIPS restrictions on dividends, buybacks and change of control;
  a US$375M grant followed by US$375M of shares to the DOC at US$37.85) - **flagged to the operator, register unchanged.** **COMPUTATION - NOT A
  CLEARANCE:** yield **0.9-2.0%** on valid bases against USD 5.35%; 7.9-9.0% perpetual growth needed for 10%; floor range **roughly US$5-25 a share**
  (0-10% growth for a decade; ~US$9-27 with net cash); **price above the whole range.** No band armed, no PORTFOLIO row (FOLD step 4).
  **PASS/FAIL: FAIL at Q2.**
