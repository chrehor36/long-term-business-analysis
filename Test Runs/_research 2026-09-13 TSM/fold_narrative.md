## UPDATE 2026-09-13 - TSM: Q2 OUT, the dominant foundry on every filed metric, ruled out by the criterion its own 20-F describes
`Test Runs/2026-09-13 Run - TSM Taiwan Semiconductor.md`. **Q1 IN, Q2 OUT on [E4-04], file closed; Q3 recorded (no integrity
disqualifier; guidance-culture, pay-on-price and capacity-enthusiasm prompts converging); Q4 recorded (financially impregnable; would be
UNKNOWABLE on the address); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing armed.** Price **NT$2,410** x
**25,932,364,992 shares** = cap **NT$62,497bn**; sovereign **TWD 30-year 1.886%** (TPEx, 2026-09-11; CBC auction for the MOF 1.814%,
2026-05-26). **The fourth WAVE 5 name.**

### THE SKIP REASON, TESTED
*"Foreign 20-F filer ... too few annual periods because their XBRL history is short."* **Wrong in cause.** `companyfacts` holds
`ifrs-full` facts FY2015-FY2024; **the FY2025 20-F (filed 2026-04-16 under a new filing-agent prefix) was not ingested.** Fourth 20-F
filer in a row with this lag (SONY, TM, HMC, TSM).

### THE SOVEREIGN, THE HARD INPUT - AND HOW TO REPEAT IT FOR UMC
- The **Ministry of Finance** issues; the **Central Bank of the R.O.C. runs the auctions "on behalf of the Ministry of Finance"** and
  publishes each result (`cbc.gov.tw/en/cp-448-...`; the 30-year A15105 on 2026-05-26 at 1.8140% weighted average). That is the issuing
  authority's print, but it exists only on auction days.
- **The Taipei Exchange publishes the daily Treasury Yield Curve**: POST `https://www.tpex.org.tw/www/en-us/bond/govDaily2` with
  `date=YYYY/MM/DD&fileCode=Curve&response=json` lists the month's files; each `Curve.YYYYMMDD-E.xls` carries the 2/5/10/20/30-year EBTS
  benchmarks and fitted zero curves. 2026-09-11: 30-year 1.886% (below the 20-year's 2.101%), fitted 30-year zero 2.18-2.19%.
- **The CBC's NT$/US$ closing rate** (`cbc.gov.tw/en/lp-700-2.html`) is the issuing-authority FX. **Nothing was added to
  `tools/sources.py`.** The gap to USD is ~3.5 points, the widest in the queue; the floor makes it decision-irrelevant.

### THE QUESTION THE BRIEF ASKED: DID SHARE AND MARGIN HOLD THROUGH THE NODE TRANSITIONS?
- **Yes, tested and not assumed.** Gross margin 48.7% (2015) -> 59.9% (2025), operating margin 37.9% -> 50.8%, revenue x4.5 against UMC's
  x1.6 and GlobalFoundries' x1.17 (2019-25); 54.4% gross margin in the 2023 downturn (units -21%) above every peer's best year; revenue
  per wafer +21% that year (mix-confounded, stated). **Customers' filings carry the substitute test**: Broadcom ~95% of wafers, AMD all
  of 7nm and below, Intel's own leading products *"exclusively manufactured by TSMC"*. The attacker's test [E2-45] has been run and filed:
  Intel Foundry -58% operating margin in 2025.
- **And the record does not overturn [E4-04].** The full row reads *"rule out companies in industries prone to rapid and continuous
  change"*; TSMC's own 20-F uses that description of its industry and says its position depends on remaining *"a technology leader"*;
  capex exceeded depreciation in every year including the 2023 downturn; and the last leading-edge incumbent's filed margin fell 26 points
  in nine years after a lapse. **A ten-year record of staying on the wave is [E3-51]'s surfing run at its best.** This is consistent with
  the INTC run (the process node wholly replaced every generation) and SONY's I&SS leg, and it is the line the KLAC run drew between
  defending a platform and re-buying a node.

### THE CORPUS TENSION - FLAGGED FOR THE OPERATOR (prime rules 2 and 5)
`Annual Meetings/2023 Annual Meeting.txt`, section 26: Berkshire *"bought a substantial position in Taiwan Semiconductor, and ... sold
almost the entire position within a few short months"*; Buffett: *"one of the best managed companies and important companies in the
world"*, *"there's nobody in the chip industry that's in their league"*, and the exit ground *"I don't like its location. And I've
reevaluated that."* **The corpus authors did not treat [E4-04] as a bar at the purchase and left for a Q4 reason.** The run carries this
as a rule-against-practice tension (like Open Question 3), does not resolve it, and records that re-scoping [E4-04] for leading-edge
manufacturers would be a structural change requiring a written case. **It is the single most relevant corpus passage for this name and
no brief mentioned it; future briefs for any name Berkshire has owned should point to the transcript.**

### PRIORS REFUTED OR CONFIRMED
- **"Employee profit-sharing may sit outside the SBC tags"** (the brief): confirmed and resolved. NT$103.1bn of profit sharing for 2025 is
  cash, expensed and inside operating cash; equity-settled SBC is tiny (NT$1.2bn) and resolves every year; [E3-70]'s grant-value measure
  is 0.07% of operating cash.
- **The [E4-29] EBITDA prior:** clean. Once in the 20-F (a subsidiary-loan covenant), zero in twelve decks and releases.
- **The [E3-48] guidance prior:** the record is beaten-guidance, not missed-guidance: 12 of 12 quarters at or above range. The flag stays a
  prompt because of the 2024-2029 multi-year target.
- **The overseas-fab margin question** (the brief): the 20-F and the decks' text give **no site margin** (recorded sweep: no instance of
  "overseas fab" or "dilution"), but **the Q2 2026 consolidated report's investee table gives TSMC Arizona's half-year net income,
  NT$36.1bn on NT$759.6bn invested**, and JASM's NT$1.7bn.
- **A new filing class:** 42 Forms 3 from 2026-03-18 and 226 Forms 4 since, mostly ESPP and LTI-trust purchases; two sales. Worth
  knowing for every foreign private issuer in wave 5.

### Q4, RECORDED - (c) FOR A FOUNDRY
The filing gives no maintenance/growth split. It gives a 5-year machinery life, capex above depreciation in all eleven years **including
the downturn year**, and Q2's finding that holding position means re-buying the node, which is [E2-23]'s *"fully maintain its long-term
competitive position"*. **So the D&A end is INVALID [E5-20]** and the band runs from total net capex (after grants) to **1.336x D&A**, the
ratio in the flattest revenue years on file (2017-2019). Customer capacity prepayments (NT$186bn inflow in 2021, NT$101bn outflow in 2025)
are stripped from operating cash. **Owner earnings NT$411-970bn across valid windows and ends; 588-842 on the five-year default.**

### THE SURVIVAL SHAPE - A TWELFTH: THE ADDRESS
Not one of the eleven (ORCL, ARM, BE, BA, SWK, ACVA/FLNC/NEGG with the treadmill and pendulum variants, CNR, RGTI, BAM's WAREHOUSE, SONY's
CAMOUFLAGE, TM's PASS-THROUGH). **A business that wins its race, keeps its gains and is financially impregnable (net cash ~NT$2.65tn,
near-term requirements covered ~2.7x), whose earning plant sits at one address inside a disputed jurisdiction:** 80.0% of noncurrent
assets in Taiwan, the non-Taiwan earning base on file on the order of 0.1-0.2% of the cap, and a contractual right for the R.O.C.
Government to use up to 35% of capacity. **The death is not in the accounts; the accounts show only where the assets are.** It is the
opposite of TM's PASS-THROUGH (the savings stay home) and is the corpus's own stated exit reason for this company. **The likelihood
cannot be read from any document, so the file assigns none and Q4 would be UNKNOWABLE.** **The register now stands at TWELVE.**

### THE STRONGEST SINGLE FACT AGAINST THE VERDICT [E4-51]
Every leading-edge designer on file, including both funded attackers, buys from TSMC, and its margin rose through five node transitions and
a 21% unit decline, while the corpus authors themselves bought it and called it peerless. The file's answer: the record establishes
position, scale and direction, all granted; it does not establish that the premium-earning asset is anything but the current node, which
the filer says must be re-won. **And the price fails the floor from every multi-year base whichever way Q2 is read.**

### TOOLING AND DOCUMENT DEFECTS
1. **`companyfacts` had not ingested the FY2025 20-F** (a new filing-agent prefix; fourth 20-F filer in a row).
2. **No TWD sovereign in `tools/sources.py`**; left alone; the by-hand method is recorded above for UMC.
3. **The Q2 2025 earnings deck strips to 80 characters** (image-only); that quarter's guidance was read from the Q1 2025 release.
4. **The framework/corpus disagreement on [E4-04] for leading-edge manufacturers** is flagged for a written case, not resolved.
