## UPDATE 2026-09-13 - UMC: Q2 OUT, the best mature-node foundry in the row, and still a commodity producer on its customers' filings
`Test Runs/2026-09-13 Run - UMC United Microelectronics.md`. **Q1 IN, Q2 OUT on [E3-03] criterion 2 and [E2-44](1), file closed; Q3 recorded
(the binary reads OUT on the company's 2020 US guilty plea and 2022 Taiwan conviction, scope flagged); Q4 recorded (UNKNOWABLE on THE ADDRESS,
THE PASS-THROUGH likely); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing armed.** Price **NT$140.5** x **12,539,542,899
shares** = cap **NT$1,761.8bn**; sovereign **TWD 30-year 1.886%** (TPEx, 2026-09-11; CBC auction for the MOF 1.814%, 2026-05-26). **The fifth
WAVE 5 foreign 20-F filer.**

### THE SKIP REASON, TESTED
*"Foreign 20-F filer ... short XBRL history."* **Wrong in cause, and one precedent explanation refuted.** `companyfacts` holds `ifrs-full`
FY2015-FY2024; the FY2025 20-F is absent. **TSM's run suggested a new filing-agent prefix as the cause; UMC's FY2025 20-F used the same prefix as
its FY2024 20-F and is equally absent, so the prefix is not it.** Measured against the 10:05 handoff note: UMC's IFRS operating-cash element
carries TWD and eight years of USD convenience translations, so a USD-only reader given the IFRS name would price it on convenience-rate
dollars rather than skip it.

### THE TAIWAN SOVEREIGN, REPEATED - AND ONE DEFECT IN THE RECORDED METHOD
The TSM run's recorded path `.../bond/tradeinfo/govDaily2` returns **HTTP 404**. **The working endpoint is `https://www.tpex.org.tw/www/en-us/bond/govDaily2`**
(POST `date=YYYY/MM/DD&fileCode=Curve&response=json`), read from the page's own `API_PATTERN`. The `.xls` needs `xlrd` (not installed); TPEx's
`/www/en-us/api/convertToOds?f=bond_zone/...` returns an ODS the standard library parses. The rate re-fetched matched TSM's to the basis point
(same 2026-09-11 file). **Nothing added to `tools/sources.py`.**

### THE QUESTIONS THE BRIEF ASKED, ANSWERED FROM THE FILED RECORD
- **At mature nodes, is there filed evidence customers have no close substitute? No, the opposite.** Himax names eight foundries for its
  high-voltage process, UMC one of them; Lattice runs 130nm and 40nm at both UMC and TSMC; Allegro and AMD multi-source. UMC's own 20-F, every year
  FY2016-FY2025: pricing *"comparable to that of other leading foundries in each respective geometry"*.
- **What did UMC's pricing do when Chinese mature-node capacity grew? It fell, and the record before China is worse.** Filed ASP: -1.8, -4.9,
  -3.4, -2.9, -0.5% (2016-20, at 88.6-96.9% utilisation), +14.6, +21.3, +6.3% (the shortage), -5.0, -5.4% (2024-25, guided in advance as *"Will
  decrease by 5%"* and *"decrease by mid-single digit %"*). SMIC and Hua Hong added 49% to year-end capacity 2022-25 on their own releases (SMIC
  capex 87-91% of revenue; Hua Hong 11.8% gross margin at 106% utilisation); GlobalFoundries' 20-F names the mechanism (*"China's foundry capacity
  is expected to grow faster than expected demand at those nodes"*). **UMC's filings never attribute a cut to a Chinese competitor**, and **the
  named-competitor paragraph (TSMC, SMIC, GF, Hua Hong...) present in every 20-F FY2016-FY2023 is gone from FY2024-25.** The filings do not
  separate Chinese capacity from the demand trough as causes; the file says so.
- **Perimeter:** Intel 12nm collaboration (2024-01-25) in force, production 2027, no equity; no foundry combination agreed, completed or abandoned
  (sweep); the June 2026 press report of 3nm work with Intel answered *"does not comment on speculative reports"*; USJC (2019) and USCXM
  minority buy-out (2023) inside the window, displayed outside (c).
- **Listed stakes:** ~NT$231bn at quotes, 13% of the cap, Unimicron NT$200bn of it; kept out of owner earnings by stripping dividends received;
  associates' share-price gains lifted H1 2026 net income to NT$58.4bn against NT$26.2bn of operating income.

### REFUTED OR NARROWED PRIORS
- **"UMC is TSM's OUT with worse numbers" - refuted as a description.** TSMC passed [E3-03] at the leading edge and failed only [E4-04]; **UMC fails
  the franchise definition itself**, on different evidence (customer sourcing, filed ASP), and its relative position is genuinely good.
- **"2026 is a new regime" - not refuted, not established.** Utilisation 85% and 90%+ guided, ASP guided up; the test [E2-44] sets is the trough,
  and Q6 records the full-cycle evidence that would reopen it.
- **The TSM prepayment strip does not transfer:** UMC's capacity-reservation deposits run through financing, not operating cash.

### NEW FOR THE OPERATOR
1. **Honesty binary on a corporate plea (prime rule 2, scope).** First run whose Q3 binary rests on a company's criminal plea and conviction
   (US 2020, Taiwan 2022) rather than a named individual; [E5-16] says "personal misconduct". Recorded as OUT with the scope question stated;
   not governing here because Q2 closed the file. **A written ruling would settle how future runs score this class.**
2. **Circular board seats (a [E3-66] read worth standardising for Taiwanese filers):** UMC's CEO and COO sit as representatives of associates
   (SIS, Hsun Chieh) that hold UMC shares.
3. **No new survival shape; the register of shapes stays at twelve** (PASS-THROUGH primary, ADDRESS secondary).

### TOOLING AND SOURCE DEFECTS FOUND
1. The TSM run's recorded TPEx endpoint path is wrong (404); corrected path above.
2. `fts_count("UMC", cik=GFS, forms="10-K,20-F")` returned HTTP 500 once; recorded as an error, not a zero.
3. Vanguard International's English press pages return HTTP 403 to both urllib and WebFetch (company-IR rung blocked); MOPS not attempted.
4. `companyfacts` depreciation for UMC (NT$45,337M for 2024) is not the cash-flow add-back (NT$45,472M); the run used the filed line.
