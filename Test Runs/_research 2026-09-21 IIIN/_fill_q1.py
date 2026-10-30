import io
p = "Test Runs/2026-09-21 Run - IIIN Insteel Industries.md"
t = io.open(p, encoding='utf-8').read()
lines = t.split('\n')
head = '\n'.join(lines[:40])
rest = '\n'.join(lines[61:])
new = r'''## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** (the newest published print; 2026-09-21 is a Monday) ·
  source (issuing authority) **US Treasury daily par yield curve, 30-year par yield**, struck
  fresh this run through `tools/sources.py`. **FRED DGS30 was not used and is the fallback,
  not the source.**
- FX: none. Insteel earns in USD. The FY2025 10-K, Item 1: *"We sell our products nationwide
  across the U.S. and, to a much lesser extent, into Canada, Mexico and Central and South
  America."* Non-US sales are disaggregated in Note 15 and are immaterial to the currency choice.

**THE PRICE — AGGREGATOR, FLAGGED, LIVE QUOTE ONLY (operator rule 5).**
- **$29.66**, close of **2026-09-18**, Yahoo Finance chart API via `tools/sources.py`. Raw
  response saved to `Test Runs/_research 2026-09-21 IIIN/price_raw_aggregator.json`
  (`regularMarketPrice 29.66`, `currency USD`, `fullExchangeName NYSE`). **This is the only
  number in the file that comes from an aggregator.**

**THE SHARE COUNT AND THE CAP — STRUCK BY HAND OFF THE COVER OF THE NEWEST PERIODIC FILING.**
- Cover of the **Form 10-Q for the quarterly period ended June 27, 2026**, filed 2026-07-16,
  **accession 0001437749-26-023682**, verbatim: *"Common Stock (No Par Value)"* …
  **"19,358,247"** … *"Number of Shares Outstanding as of July 15, 2026"*.
- **ONE CLASS ONLY.** The FY2025 balance sheet reads *"Preferred stock, no par value Authorized
  shares: 1,000 None Issued"* and *"Common stock, $ 1 stated value Authorized shares: 50,000
  Issued and outstanding shares: 2025, 19,420 ; 2024, 19,452"* (thousands). **Insteel is the ADM
  shape, not the BELFB shape**: single class, current cover, count falling slowly on buybacks.
  The dual-class cover-tag defect that made BELFB's screen cap wrong by 6.29x cannot arise here,
  and it was checked rather than assumed.
- **Splits after the measurement date: none.** `split_factor_after('IIIN','2026-07-15')` returns
  **1.0**. `cap = close(anchor) × shares(measurement) × splits AFTER measurement`
  = 29.66 × 19,358,247 × 1.0 = **$574.2M**, on `close`, never `adjclose`.
- **Against the screen's 588, the screen is 2.4% high.** This is not the BELFB or FC defect
  class — it is a stale price, not a wrong count: 588 ÷ 19,358,247 implies $30.37, which sits
  inside the range the 10-K itself discloses, *"During fiscal 2025 our common stock traded as
  high as $41.64 and as low as $22.49."* **The cap used everywhere below is the hand-struck
  $574.2M.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **Form 10-K for the fiscal year ended September 27, 2025**, filed 2025-10-23,
    **accession 0001437749-25-031597** (`iiin20250927_10k.htm`) — the newest ANNUAL filing.
  - **Form 10-Q for the quarter ended June 27, 2026**, filed 2026-07-16,
    **accession 0001437749-26-023682** — the newest PERIODIC filing.
  - **DEF 14A filed 2026-01-02, accession 0001308179-26-000001** (read at Q3).
  - **8-K / EX-99.1 earnings releases** of 2025-10-16 (acc. 0001437749-25-031106), 2026-01-15
    (0001437749-26-001309), 2026-04-16 (0001437749-26-012485) and 2026-07-16
    (0001437749-26-023670); plus the EX-99.1 of **2026-08-21** (0001437749-26-028729, the Upper
    Sandusky closure) and **2026-08-11** (0001437749-26-027019, the dividend declaration).
- **FY2026 HAS NOT CLOSED AND NO 10-K FOR IT EXISTS.** Insteel's year ends on the Saturday
  nearest 30 September; FY2025 ended 2025-09-27 and FY2026 ends **2026-10-03**, twelve days
  after this run. The newest periodic filing is therefore the **third quarter of FY2026** (period
  ended 2026-06-27), exactly as the screen row's `newest_periodic` says. Checked against the
  submissions index, not assumed.
- **figure cross-checked against the filed statement — three, by hand, against the filed
  statements and not against XBRL:**
  1. **FY2025 operating cash flow $27,163 thousand**, read off the filed Consolidated Statements
     of Cash Flows (*"Net cash provided by operating activities 27,163"*), equal to the
     companyfacts figure used in the series below.
  2. **Shareholders' equity recomputed from A − L** *(the [E5-32] cross-check: Salomon's books
     carried an invented number for twelve audited years, so audited does not mean true)*: total
     assets **$462,650** less total current liabilities **$66,009** less other liabilities
     **$25,109** = **$371,532**, which is the filed *"Total shareholders' equity 371,532"* to
     the dollar.
  3. **FY2025 net sales $647,706 thousand** on the filed Consolidated Statements of Operations,
     against the MD&A's *"Net sales increased 22.4% to $647.7 million in 2025 from $529.2 million
     in 2024"* — the two agree and the percentage is arithmetic on them.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** Insteel buys hot-rolled carbon
  steel wire rod by the ton, draws and welds it into two products — seven-wire prestressing
  strand, and welded wire sheets and rolls — and sells them by the ton to the people who cast
  concrete. **The whole business is one arithmetic line: tons shipped × (price per ton less rod
  cost per ton), less conversion cost, less freight.** Nothing else moves the result. The filing
  writes the same equation without disguising it (FY2025 10-K, Item 1, Raw Materials):
  *"Selling prices for our products tend to be correlated with changes in wire rod prices.
  However, the timing and magnitude of the relative price changes vary depending upon market
  conditions and competitive factors. Ultimately, the relative supply - demand balance in our
  markets and competitive dynamics determine whether our margins expand or contract during
  periods of rising or falling wire rod prices."* FY2025 is that equation worked: gross profit
  rose $43.8M, and the MD&A attributes *"higher spreads between average selling prices and raw
  material costs ($36.1 million)"* — **82% of the improvement was spread, not volume.**
- **The scarce input this business controls:** **on the evidence, none.** The rod is bought, not
  made — *"which we purchase from both domestic and foreign suppliers and can generally be
  characterized as a commodity product"* — and imports were *"approximately 27% and 15%"* of
  total wire rod purchases in FY2025 and FY2024. What Insteel actually holds is **freight
  geometry**: eleven owned plants *"all located in the U.S. in close proximity to our customers
  and raw material suppliers"*, in a product whose value-to-weight ratio makes long hauls
  uneconomic. It claims its buying scale as an advantage — *"We believe that our substantial
  wire rod requirements, desirable mix of sizes and grades and strong financial condition
  represent a competitive advantage by making us a relatively more attractive customer to our
  suppliers"* — and that claim is tested at Q2 against the vertically integrated competitors the
  same section names. It is not a scarce input owned, and Q1 does not credit it as one.
- **Will the fundamentals look broadly the same in ten years?** Yes. Concrete has been reinforced
  with drawn steel wire for a century, the product is written into building codes and into
  *"Buy America"* melt-and-cast rules, and the 10-K's own list of what moves the result — rod
  price, construction activity, import competition, freight — is the same list it would have
  carried in 2009. This is **[E3-31]**'s *"relatively simple and stable in character"*, not a
  business *"complex or subject to constant change"*. **The volatility is in the numbers, not in
  the character of the business**, which is the distinction **[E3-55]** draws: *"If we have a
  business about which we're extremely confident as to the business result, we would prefer that
  it have high volatility than low volatility."*
- **The five-minute test [E4-46]:** *"if we can't make a decision in five minutes, we can't make
  it in five months. We're not going to learn enough in the following five months to make up for
  the fact that we went in deficient in the first place."* Nothing here needed five months: one
  reportable segment, two product lines, no debt, no float, no equity-method stakes, no foreign
  subsidiaries of substance, and a cash-flow statement of sixteen lines.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____
  *IN on understanding only. Understanding a commodity converter is not a finding that it is a
  good business — that is Q2's question, and the commodity doctrine at **[E2-58]** is where it
  gets asked.*

'''
io.open(p, 'w', encoding='utf-8').write(head + '\n' + new + rest)
print("ok")
