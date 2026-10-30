## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**. Optex sells to the US government, US primes and a few foreign buyers, in dollars; *"Approximately
94 % of the total company revenue is generated from domestic customers and 6 % is derived from foreign customers, primarily in Canada
and Israel"* (10-K FY2025, Note 1). Earnings currency **USD**; no FX step.
- rate **5.49%** · date **09/25/2026** (the last posted business day; 09/26 and 09/27 are a weekend) · source **US Treasury daily
  par yield curve, 30-year, from the issuing authority**. `tools/_cache/sov_USD_treasury.csv` was deleted before
  `tools/sources.sovereign()` ran, so the rate was fetched, not served from cache (`step0.py`, output `step0_out.txt`). FRED not used.
  Struck fresh; not inherited from the brief or from the DTM run.
- FX / ADR: not applicable.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes  [x] Item 1  [x] Item 1A
- **Annual report: Form 10-K for the fiscal year ended 2025-09-28, filed 2025-12-17, accession 0001493152-25-028071**
  (`form10-k.htm`). Also read: the 10-Ks for FY2024 (0001493152-24-050771) and FY2023 (0001493152-23-045259), the latter for the
  screen's `wc_note`.
- **Newest periodic: Form 10-Q for the quarter to 2026-06-28, filed 2026-08-11, accession 0001493152-26-037119.**
- **Fiscal calendar, confirmed from Note 2**: *"Optex System Holdings’ fiscal year ends on the Sunday nearest September 30. Fiscal year
  2025 ended on September 28, 2025 and included 52 weeks."* The FY2026 10-K (year to 2026-09-27) is not yet due. **Filer status**: the
  FY2025 cover ticks *"Non-accelerated filer ☒ | Smaller reporting company ☒"*; the EDGAR filer record reads "Non-accelerated filer,
  Smaller reporting company". Registrant **CIK 0001397016**, Delaware, Richardson, Texas; formerly Sustut Exploration Inc (a shell, reverse
  merger March 2009). Listed on the Nasdaq Capital Market from 2023-03-14 (Form 8-A12B, accession 0001493152-23-007551, and the
  exchange certification the same day; Commission File Number 001-41644); registered under Section 12(g) from 2010 (8-A12G).
- **Figures cross-checked against the filed statement.** The tagged `NetCashProvidedByUsedInOperatingActivities` for FY2025 is 6,931,000
  and for FY2023 is −296,000; the 10-K statements print *"Net Cash provided by Operating Activities | 6,931 | 1,781"* (FY2025, FY2024) and
  *"Net Cash (used in) provided by Operating Activities | ( 296 | ) | 2,042"* (FY2023, FY2022). Also checked line by line against the tags:
  depreciation and amortization 515 / 487 / 345 / 307, stock compensation 383 / 425 / 247 / 162, purchases of property and equipment 494 /
  681 / 376 / 257, accounts payable and accrued expenses 725 / 359 / 411 / 313, inventory 541 / (2,710) / (2,941) / (1,629). Every tag equals
  the printed figure.

**Price and shares.**
- Price **$10.42**, Nasdaq Capital Market close **2026-09-25** (Friday), Yahoo chart endpoint via `tools/sources.price`, `regularMarketTime`
  2026-09-25 checked. **Aggregator, used for the live quote only, flagged.**
- Shares **6,959,873**: the cover of the **10-Q for the quarter to 2026-06-28, filed 2026-08-11, accession 0001493152-26-037119**, reads
  *"Indicate the number of shares outstanding of each of the issuer’s classes of common stock, as of August 10, 2026: 6,959,873 shares of
  common stock."* The balance sheet of the same filing: *"Common Stock – ($ 0.001 par, 2,000,000,000 authorized, and issued and outstanding
  shares of 6,959,873 and 6,920,658 as of June 28, 2026 and September 28, 2025, respectively)"*. `python Screens/cover_shares.py OPXS`
  returned the same count from the same accession. **One class; no preferred stock on the balance sheet; no warrants or convertibles
  outstanding found in either filing.** Dilution not in the count, from the 10-Q's EPS note: 63,500 unvested restricted stock units and
  67,500 unvested market-based shares (the CEO and CFO grants of 2025-12-18), about 1.9% together; recorded, not added. Nothing summed.
- **Market cap: $10.42 x 6,959,873 = $72.5M.**

**Deal check (the screen's `deal_note`).** The filer list since 2025-12-17 carries one Item 1.01 8-K, filed 2026-07-20 (accession
0001493152-26-033931), and no S-4, DEFM14A, SC TO-T, SC 13E3 or 425. Its Item 1.01 reads: *"On July 14, 2026, Optex Systems Holdings, Inc.
[...] and its subsidiary, Optex Systems, Inc. [...] entered into a master equipment finance loan and security agreement (the “Master
Agreement”) with Texas Capital Bank [...] the Bank provided interim funding of $246,783 (the “First Interim Loan”) to cover the first
installment of an installment purchase of an approximately $2.1 million high vacuum coating system."* The exhibits are the Master Agreement
(EX-10.1) and the Interim Funding Addendum (EX-10.2); no EX-2.1. **It is an equipment loan, as the screen guessed; the quote is an
owner-earnings price, not a spread.** The only deal-shaped filings in the history are the issuer's own tender offer of 2022 (SC TO-I
filed 2022-08-18; 1,603,773 shares bought at $2.65) and the Speedtracker product-line purchase of 2024-01-18 (Item 1.01 not needed; $1.03M
cash, below).

---
## THE SCREEN ROW — carried UNLABELLED, a set of claims and not a finding

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`: `cap_m 70 · oe_bottom_m 1 · oe_top_m 2 · spread 0.397 · deal_note "1 8-K
Item 1.01 filing(s) since 2025-12-17, none carrying a merger agreement" · wc_note "ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities
moved 139% of 2023 OCF" · yield_bottom 0.0198 · vs_sovereign −0.0337 · growth_required 0.0802 · level_shift 2.2 "STEP UP - normalize down
[E4-41]" · best_year_dep 0.36 · level_shift_oe n/a "EARLY HALF STRADDLES ZERO" · best_year_dep_oe 0.481 · flags_disagree · years_filed 16 ·
window_disagree · spread_caveat "4-construction width only [...] rebuild it [E4-25]" · newest_filing 2025-09-28 · newest_periodic
2026-06-28`. Each field used is reproduced or refuted in this file; the list is gathered at the end.

**The `wc_note` is refuted at Step 0, from the filed FY2023 statement: the payables line did not make the cash, because there was no
cash.** FY2023 operating cash was **negative, $(296)K**. The accounts payable and accrued expenses line was **+$411K**, which is 139% of
the ABSOLUTE value of $296K; that is the whole of the screen's arithmetic. The line that decided the year was the other way round:
*"Inventory | ( 2,941 | )"*, an inventory build of $2.9M (inventory $9,212K to $12,153K) against net income of $2,263K. The FY2023 10-K
says why: the delays in key components *"combined with labor shortages experienced in fiscal year 2023, negatively impacted our production
levels and pushed the delivery dates of several of our contracts"* (quoted from the FY2025 10-K, which carries the same history). The
flag's ratio has no sign, so on a year of negative operating cash it reports the payables line as having "made" a cash figure that does
not exist. **Screen error, and a tooling defect in `working_capital_flag()` (reported, not patched).**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words.** Optex is a job shop for military optics with two plants in the Dallas area and 132 people. It is
handed a drawing and a quantity, buys the glass, acrylic, aluminium castings, steel and gold coating material, grinds, coats, bonds and
assembles the parts, puts a sample through the customer's first-article and life tests, and ships. The filer's own words, twice in
the 10-K: *"Our products consist primarily of build-to-customer print products that are delivered both directly to the armed services and
to other defense prime contractors."*
- **Optex Richardson (FY2025 revenue $23.8M, 57%; operating income $3.6M).** Periscopes (laser-protected and plain, glass and acrylic;
  $19.2M), sighting systems ($1.5M), howitzer sights (nil delivered), and spares (mirrors, prisms, collimators). Fitted to the Abrams,
  Bradley, Stryker, XM30 and M10 Booker vehicles. Sold to the government direct (DLA Land and Maritime under multi-year IDIQ contracts, the
  Army) and to the primes that build the vehicles (General Dynamics Land Systems, BAE Systems).
- **Applied Optics Center, Dallas (FY2025 external revenue $17.6M, 43%; operating income $3.9M).** Bought in November 2014. Thin-film
  coatings: laser interference filters and laser filter units for night-vision and weapon sights (the XM157 fire-control scope), day
  windows, specialty coatings; plus commercial optical assemblies for rifle-scope makers (Nightforce, Lightforce). It is also the coating
  supplier to Richardson's periscopes.
- Revenue = units ordered x a unit price fixed at award for the life of the contract (*"The majority of the Company’s contracts and
  customer orders originate with fixed determinable unit prices for each deliverable quantity of goods defined by the customer order line
  item"*, 10-Q Note 2). Cost = materials (*"The largest portion of our costs is materials"*), direct labour, and a fixed plant overhead that
  is spread over whatever volume arrives. Profit is therefore a function of volume against a price that was fixed before the costs were
  known: FY2025's 25.5% Richardson gross margin came, in the filer's words, from *"improved manufacturing overhead rates as the fixed
  costs were spread across a higher revenue base"*.
- Customers, FY2025: *"U.S. government agencies (29%) and four U.S. defense contractors (19%, 10%, 6% and 6%)"*; by channel, the
  government 28%, US primes 61%, foreign military 6%, commercial 5%.

**The scarce input this business controls.** Not a design and not a brand. What it holds is **qualification**: approved-source status on
drawings it already builds, first articles already accepted, an ITAR registration, a government-approved accounting system, and the
coating know-how of the Dallas plant. The filer names these as the entry barrier (*"an entrant would need to prove to the government agency
in question the existence of a government approved accounting system for larger contracts. Second, the entrant would need to develop the
processes required to produce the product. Third, the entrant would then need to produce the product and submit successful test
requirements"*). Whether that barrier holds prices up is the Q2 question.

**Will the fundamentals look broadly the same in ten years?** The mechanism will: drawings in, qualified parts out, priced per contract.
The filer expects the vehicle fleet it serves to last (*"We expect that these tanks will continue to be used through approximately 2040"*).
The volumes are not stable (orders for periscopes fell 42.2% in FY2025; backlog fell from $44.2M to $39.1M to $30.1M between 2024-09 and
2026-06) and depend on appropriations the filer does not control, but that is a question for Q2 and Q4, not for whether the business can
be understood. The business is *"relatively simple and stable in character"* **[E3-31]** in its mechanism.

**VERDICT: [x] IN**

---
