import io
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-21 Run - BELFB Bel Fuse.md"
s = io.open(p, encoding='utf-8').read()
start = s.index("## STEP 0 \u2014 THE RATE, AND THE FILING")
end = s.index("## Q2 \u2014 IS IT A FRANCHISE?")
new = u"""## STEP 0 \u2014 THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** \u2014 the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** \u00b7 date **2026-09-18** \u00b7 source **US Treasury daily par yield curve, 30-year,
  the issuing authority** (`tools/sources.py`, Treasury CSV for 2026; FRED is the fallback and was
  not used). 2026-09-18 is the latest published business day as at 2026-09-21.
- FX: **none needed.** Bel Fuse is a New Jersey registrant reporting in USD. It manufactures in the
  PRC, Mexico, the Dominican Republic, Slovakia, Israel, India and the UK and its labour costs are
  in local currency, but the **earnings currency is USD** and the quote is USD. No ADR.

**THE CAP, STRUCK BY HAND BEFORE ANY YIELD EXISTS** \u2014 ordered by the brief because the screen row's
own `cap_flag` said the cap was smaller than a filed public float. Full workpaper:
`Test Runs/_research 2026-09-21 BELFB/WORKPAPER - the cap, struck by hand.md`.

| class | shares outstanding | where the count comes from | close 2026-09-18 | cap |
|---|---|---|---|---|
| Class A (BELFA, voting) | 2,115,263 | cover of the 10-Q for the quarter ended 2026-06-30, accession `0001437749-26-025619`, "as of July 31, 2026" | $198.83 | **$420.6M** |
| Class B (BELFB, non-voting) | 12,324,187 | same cover, same date | $241.97 | **$2,982.1M** |
| **total** | **14,439,450** | | | **$3,402.7M** |

Prices are **aggregator, live quote only, flagged** (operator rule 5). Split factor after the
measurement date 2026-07-31 is **1.0** for both tickers, so `close x shares x splits-after` reduces
to the product shown. The cover count is cross-checked against the filed balance sheet in the same
10-Q: *"12,324,187 and 10,543,368 shares outstanding at June 30, 2026 and December 31, 2025,
respectively (net of 3,218,307 restricted treasury shares)"*. They agree.

**THE SCREEN'S CAP WAS $541M. THE HAND-STRUCK CAP IS $3,402.7M \u2014 6.29x LARGER.**
**The brief's prior, that the defect was a stale price (which is what BLMN's was), is REFUTED.**
`dei:EntityCommonStockSharesOutstanding` resolves **undimensioned exactly once in the whole
companyfacts file**: `end 2011-08-01, val 2,174,912, form 10-Q/A, frame CY2011Q2I`. Every filing
since tags it **dimensioned by class**, so an undimensioned fetch falls back on a **fifteen-year-old
Class A count**. Arithmetic: **$248.69 (BELFB close 2026-08-28) x 2,174,912 = $540.85M**, the
screen's figure to the dollar. **The price was three weeks old and immaterial; the share count was
both the wrong class and fifteen years stale.** Every per-cap figure on screen line 34 is therefore
void: `yield_bottom 7.43%`, `vs_sovereign 2.08%`, `growth_required 2.57%`, and the `acq_note`'s
"62% of cap" (true share: **9.9%**).

**The filing was read** \u2014 not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Anchor document: Form 10-K for the fiscal year ended 2025-12-31, filed 2026-02-24, accession
  `0001437749-26-005354`** (`belfb20251231d_10k.htm`).
- Also read: **10-Q for the quarter ended 2026-06-30, accession `0001437749-26-025619`** (filed
  2026-08-04); **10-K for FY2021, accession `0001437749-22-006139`** (filed 2022-03-14), pulled to
  settle the screen's working-capital note; the **8-K of 2026-07-29 EX-99.1 Q2 2026 earnings
  release, accession `0001437749-26-024893`**; the **8-K of 2025-12-10 Item 4.01, accession
  `0001437749-25-037380`**; the **8-K of 2026-05-14 Items 1.01/8.01, accession
  `0001213900-26-056732`**; the **DEF 14A filed 2026-04-10, accession `0001437749-26-011998`**.
- **Figure cross-checked by hand against the filed statement:** the FY2025 consolidated statement of
  cash flows shows **Net cash provided by operating activities $80,612** thousand, against
  `NetCashProvidedByUsedInOperatingActivities` $80,612,000 in companyfacts. Agrees.
- **Second hand cross-check, on the year the screen flagged:** the FY2021 10-K
  (`0001437749-22-006139`) consolidated statement of cash flows shows **Accounts payable +$23,961**
  thousand against **Net cash provided by operating activities $4,632** thousand = **517.3%**. The
  screen's `wc_note` arithmetic is correct. **Its reading is not \u2014 see Q4.**

---
## Q1 \u2014 CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** Bel Fuse makes small physical parts
  that sit inside other people's electronic equipment. Three families: things that convert and
  supply electrical power (AC/DC and DC/DC converters, front-end supplies, fuses), things that join
  one wire or fibre to another in a place where vibration, heat or salt would break an ordinary
  joint (connectors, cable assemblies), and wound magnetic components (transformers, inductors, and
  RJ45 jacks with the magnetics built in). It buys copper, gold, silver, ferrite and integrated
  circuits, adds hand and machine labour in fifteen factories across the PRC, Mexico, the Dominican
  Republic, Slovakia, Israel, India, the UK and the US, and sells the finished part to an equipment
  maker either directly, through a sales representative, or through a distributor. Revenue less the
  bill of materials, direct labour and factory overhead is gross margin: **39.1% of $675.5M in
  2025, 37.8% in 2024, 33.7% in 2023** (10-K Item 7, filed statement). Out of that come R&D
  (**$30.9M in 2025**) and selling and administrative costs. The cost line is explicit in the
  filing: **material 31.3% of sales, labour 7.7%, other 21.9% in 2025**.
- The mechanism that makes a part sticky is design-in: an engineer at the customer selects a part
  number while designing a new router, aircraft subsystem or rail traction unit; once it is
  qualified into that platform, replacing it means requalifying. That is why the filing can report a
  **$452.2M backlog at 2026-01-31** against $675.5M of annual sales, and why 2025 bookings ran
  **$732.9M, up 75.8%**.
- **The scarce input this business controls:** the run's answer and the company's differ, and the
  company's is the honest one. My answer would be qualified positions on long-lived platforms (a
  defence or commercial-aerospace part number outlives several product cycles). **The company's own
  answer is its people.** 10-K Item 1, Intellectual Property: *"It is management's opinion that the
  successful continuation and operation of our business does not depend upon the ownership of
  patents or the granting of pending patent applications, but upon the innovative skills, technical
  competence and marketing and managerial abilities of our personnel."* That sentence is not
  boilerplate for this run; it is carried to Q2, where **[E4-23]** and **[E4-04]** decide what it
  means.
- **Will the fundamentals look broadly the same in ten years?** Yes. The company was incorporated in
  1949 and has sold parts that power, protect and connect circuits for more than 75 years. The end
  markets rotate (networking down in 2024, defence up in 2025, eMobility down 41.6% in 2025), and
  individual part families come and go, but the economic shape is stable: buy metal and silicon, add
  labour and application engineering, sell a catalogued part into someone else's bill of materials
  at a gross margin in the thirties. **[E3-31]**'s test is *"relatively simple and stable in
  character"* and this clears it. Nothing here needs a prediction about a technology I cannot judge;
  the volatility is in volume, not in the mechanism.
- **What I am NOT claiming at Q1.** Understanding the mechanism is not understanding the
  *consolidated series*. **The perimeter moves:** 80% of Enercon was bought for **$325.6M cash in
  November 2024**, EOS Power for **$7.8M in 2021**, rms Connectors for **$9.0M in 2021**, a
  one-third stake in innolectric for **EUR 8.0M in 2023**, and the Czech Republic business was sold
  in 2023. Enercon alone contributed **$136.6M of 2025 sales against $20.8M of 2024 sales**. That is
  a Q4 problem about what the owner-earnings series is a series *of*, and it is named there, not
  resolved here.
- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED \u2192 ____  [ ] UNKNOWABLE \u2192 ____
  *IN on the mechanism. The business is legible from its own Item 1 and Item 7, the cost structure
  is disclosed line by line, and nothing about how the money is made requires a forecast I cannot
  make. **[E4-46]**'s test is passed the right way round: this is a business understood in five
  minutes, not one that would need five months.*

"""
io.open(p, 'w', encoding='utf-8').write(s[:start] + new + s[end:])
print("Q1 written")
