# Company Run — Nucor Corporation (NUE) — 2026-09-27
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.49%** · date **09/25/2026** (the latest published row; 09/26 and 09/27 are a weekend) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr column**, struck fresh on 2026-09-27 by `Test Runs/_research 2026-09-27 NUE/strike.py` (raw CSV `treasury_2026.csv`; 09/24 5.47%, 09/23 5.40%). `python tools/sources.py` returned the same 5.49% for the same date.
- FX if the quote and the earnings differ in currency: **none**. Nucor earns in US dollars (operations mainly in the United States, Canada and Mexico) and the share is quoted in US dollars on the NYSE. ADR ratio: not an ADR.

**PRICE AND SHARES (dated):**
- Price **$247.25**, NYSE close **2026-09-25** (Yahoo chart endpoint, an AGGREGATOR, used for the live quote only and flagged; raw response `price_raw_NUE.json`; the five closes 09-21 to 09-25 were $242.40, $245.66, $246.98, $247.96, $247.25).
- Shares **226,875,676**, read off the cover of the **10-Q for the quarter ended 2026-07-04, filed 2026-08-12, accession `0001193125-26-345891`**: *"226,875,676 shares of the registrant’s common stock were outstanding at July 4, 2026."* `python Screens/cover_shares.py NUE` returned the same figure from the same accession. **One class** (Common Stock, par value $0.40, NYSE: NUE); nothing summed. Limit stated: the cover's as-of date is the quarter end, not a date near filing, so any shares bought back between 2026-07-04 and today are not reflected (the direction is a slightly overstated cap).
- **Market cap $56,095.0M** (247.25 x 226,875,676). The screen row carried $56,996M at an older price.

**DEAL CHECK (the screen's `deal_note` is blank; checked, not trusted).** Every filing since 2025-01-01 in `submissions.json` was listed: no Form 425, S-4, SC TO or merger 8-K. The 8-Ks carry Items 2.02/7.01 (quarterly earnings), 5.07 (annual meeting votes), 1.05 (a cybersecurity incident, 2025-05-13, with an amendment 2025-06-20), 1.01/2.03 (the March 2025 notes that refinanced the two 2025 maturities, confirmed in the 10-K's liquidity section) and 5.02 (succession: Stephen Laxton to President and COO from 2026-01-01 with Leon Topalian continuing as Chair and CEO; John Sullivan to CFO from 2026-03-01; Daniel Needham's voluntary retirement, all read in `8k_2512.txt`, `8k_2602.txt`, `8k_2603.txt`). **No live deal; the quote is an owner-earnings price, not a spread.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (read as each question needs them; the notes on segments, debt, noncontrolling interests and stock compensation are cited where used)
- document · date · accession no.: **Form 10-K for fiscal 2025, filed 2026-02-25, accession `0001193125-26-071575`** (`tenk_2025.txt`); **Form 10-Q for the quarter ended 2026-07-04, filed 2026-08-12, accession `0001193125-26-345891`** (`q2606.txt`); 8-K earnings release of 2026-07-27, accession `0001193125-26-318190`; DEF 14A filed 2026-03-27, accession `0001193125-26-127739`; and every annual cash-flow statement FY1999-FY2025 from the filed annual reports (EX-13 of the 10-Ks for FY2001-FY2018; the 10-K body for FY2019-FY2025; accessions listed in `submissions.json` and fetched by `getex13.py` and `getk.py`).
- figure cross-checked against the filed statement: the FY2025 Consolidated Statement of Cash Flows in the 10-K reads *"Cash provided by operating activities | 3,234 | 3,979 | 7,112"*, *"Capital expenditures | ( 3,422 ) | ( 3,173 ) | ( 2,214 )"*, *"Stock-based compensation | 133 | 132 | 130"*, and depreciation 1,226 plus amortization 254 = 1,480; `tools/run.py`'s XBRL figures for FY2023-FY2025 agree to the million on all four lines.
- Tooling note, reported not patched: companyfacts carries **no** `NetCashProvidedByUsedInOperatingActivities` value for FY2014 or FY2015 (a tag hole), so any screen construction over those years is short two years; the filed statements supply them (FY2014 $1,342.9M, FY2015 $2,168.8M in the newest vintage).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: Nucor buys scrap steel (and makes or buys the substitutes: direct reduced iron from its plants in Trinidad and Louisiana, and pig iron), melts it in electric arc furnaces with electricity and natural gas, casts and rolls it into sheet, bar, beams and plate, and sells the ton, mostly to service centers, fabricators and manufacturers in North America. About a fifth of the mills' tons go to its own downstream shops (joists and deck, tubing, rebar fabrication, metal buildings, racking, doors, towers) which sell to non-residential construction. It earns the spread between the selling price per ton and the metallic cost per ton (about 1.1 tons of scrap and substitutes per ton of steel, at $392 a gross ton in 2025), times the tons it ships, less a mostly variable conversion cost. **Profit is price minus scrap, times utilization.** In 2025: 26,615,000 tons shipped to outside customers at an average $1,221 a ton; mills ran at 83% of capacity.
- The scarce input this business controls: **no input it controls is scarce.** Scrap is bought *"from numerous other sources"* in a market the filer calls *"highly fragmented"*; the furnaces, casters and rolling mills are bought from equipment vendors by every rival; the sites and permits are real but are not exclusive: the 10-K says *"additional capacity continues to come online"* (globally), and the domestic rivals' own new mills are evidenced from their filings in the competitor row at Q2. What Nucor has that is hard to copy is organisational: a decentralised structure (*"Approximately 200 teammates work in our principal executive offices"*) and a pay system in which *"Production teammates work under group incentives that provide increased earnings for increased production"* and *"10% of earnings before federal taxes"* goes to profit sharing. That is a cost culture, not a controlled input, and Q2 tests whether it is wide enough to count.
- Will the fundamentals look broadly the same in ten years? **Yes.** Steel made from scrap in electric furnaces and sold by the ton into construction, autos, energy and machinery has been Nucor's business since the 1970s and the filing describes no change of character. The price per ton will not look the same; it never has. The instability is in the price and the margin, not in how the business works, and that is a Q2 and Q4 matter, not a Q1 one. Two things are changing at the edges and are recorded, not scored here: the "Expand Beyond" acquisitions into non-steel products (racking, doors, insulated panels) and the decarbonisation spending.
- The corpus's test **[E3-31]** asks for businesses *"relatively simple and stable in character"*. Nucor is simple; its character is stable though its earnings are not. I can state what drives the result in one line (spread times tons), which is what the test asks.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] · no close substitute [ ] · not price-regulated [~] *(no price is set by a regulator, but the floor under the domestic price is administered by trade law; see [E2-59] below)*
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** The [E4-04] competence branch (UNKNOWABLE at Q2) is for names that PASS [E3-03] and whose durability cannot be judged; Nucor fails criterion (2) on the filer's own words, so the branch does not arise, and I considered and refused it. **Key-person dependence [E4-23]: none found.** What the filings describe as the advantage is a culture and a pay system (*"Production teammates work under group incentives"*, profit sharing of *"10% of earnings before federal taxes"*, *"Approximately 200 teammates"* at headquarters), not a person; the 2025-2026 succession (Laxton to President and COO, Sullivan to CFO) is ordinary. Recorded, not a defect.
- Primary moat metric, filing-sourced, and its trend: **return on average stockholders' equity as the filer itself states it**, every year FY1998-FY2025 (the multi-year tables of the FY2003, FY2008, FY2013 and FY2018 annual reports, and the MD&A sentence *"Return on average stockholders’ equity was ..."* in each 10-K FY2019-FY2025):

| FY | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROE % | 13.4 | 11.3 | 14.2 | 5.2 | 7.2 | 2.7 | 38.2 | 33.8 | 38.3 | 29.5 | 28.1 | -3.8 | 1.8 | 10.7 |

| FY | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROE % | 6.7 | 6.4 | 8.4 | 1.0 | 10.4 | 15.9 | 25.5 | 12.6 | 6.8 | 55.0 | 46.9 | 23.0 | 9.8 | 8.5 |

  **28 years, two full steel cycles and more: mean 16.7%, median 11.0%; below 10% in 12 of the 28 years; at or above 20% in 9 (2004-2008, 2018, 2021-2023).** Take out the eight boom years 2004-2008 and 2021-2023 and the other twenty average **8.7%** (median 8.45%). Every high-return stretch is a supply-tight stretch, and every one was followed by a fall: 38.3% (2006) to -3.8% (2009); 25.5% (2018) to 6.8% (2020); 55.0% (2021) to 8.5% (2025). **This is [E2-58]'s equation in the filer's own numbers:** long-term profitability set by *"the ratio of supply-tight to supply-ample years"*.

**THE PHYSICAL SERIES [E4-55] AND THE PRICE CONDUCT [E2-44, E4-37].** From each year's MD&A (`units.py`, transcription only):

| FY | 1998 | 2001 | 2003 | 2006 | 2008 | 2009 | 2011 | 2014 | 2015 | 2016 | 2018 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| average sales price per ton, $ | 448 | 354 | 359 | 667 | 940 | 637 | 869 | 830 | 725 | 667 | 899 | 789 | 1,292 | 1,626 | 1,377 | 1,241 | 1,221 |
| tons to outside customers, M | 9.6 | 12.2 | 17.5 | 22.1 | n/r | -30% | n/r | 25.4 | 22.7 | 24.3 | 27.9 | 25.5 | 28.2 | 25.5 | 25.2 | 24.8 | 26.6 |
| steel-mill utilization, % | | | | | | 54 | 74 | 78 | 68 | 80 | 91 | 82 | 94 | 77 | 78 | 76 | 83 |

  (n/r = not stated in a comparable sentence; 2009's tons are the filer's *"decreased 30%"*; 1998-2006 tons are "total tons sold", the later series "tons shipped to outside customers"; the 2015 utilization is 68% in the FY2015 report and 73% as restated in the FY2016 report.) **The price follows utilization down in every downturn of the record**: -32% in 2009 at 54% utilization; -13% and -8% in 2015-2016; -15% and -10% in 2023-2024 **with Section 232 in force**. **One year runs the other way and is recorded, not smoothed: 2022**, when steel-mill utilization fell from 94% to 77% and the steel mills' average price per ton still rose 11% ($1,195 to $1,324; the consolidated figure +26% on mix), with scrap up 5% ($469 to $492 a gross ton) and outside steel shipments down 10% (FY2022 10-K MD&A). It is answered as item 6 of the evidence against, below. The price per ton was lower in 2003 than in 1998 ($359 against $448). **Tons to outside customers were 25.4M in 2014 and 26.6M in 2025**, a 5% rise across eleven years in which Nucor spent **$18,477.5M on capital expenditures and $7,821.2M on acquisitions** (filed cash-flow statements, FY2014-FY2025) against $9,322.1M of depreciation.
  **[E2-44] asks whether a business can raise prices *"even when product demand is flat and capacity is not fully utilized"*. The 10-K answers in its own words, no:** *"During periods of weaker or rapidly deteriorating steel market conditions, weak steel demand, low industry utilization rates and the impact of imports create an even more intensified competitive environment and increased pricing pressure."* The contracts are indexed: *"The vast majority of our contracts include a method of adjusting prices on a periodic basis to reflect changes in the market pricing for steel and/or scrap"*, and *"during periods of steel market weakness, the more intensified competitive steel market environment can cause the sales price indices to decrease"*. **[E4-37]'s agony test does not even arise**: the price is not decided, it is read off an index.

**[E3-03] criterion by criterion.**
- **(2) no close substitute: FAILS on the filer's words.** Item 1: *"These markets are highly competitive with many domestic and foreign firms participating, and, as a result of this highly competitive environment, we find that we primarily compete on price and service."* The mills face *"domestic integrated steel producers ..., other domestic EAF steel mills, steel imports and alternative materials"*; imports supplied *"approximately 18% of U.S. demand in 2025"*; and other materials substitute: *"Increased use or availability of these materials in substitution for steel products could have a material adverse effect on prices and demand for our steel products."* Downstream is the same: joists and deck are sold on *"firm, fixed-price contracts that are, in most cases, competitively bid against other suppliers"*, and the steel products segment's price per ton fell 6% in 2025 ($2,510 to $2,348) while its volume rose 9%.
- **(3) not subject to price regulation: passes in form, and the regime is the floor [E2-59].** No regulator sets the price. But the 10-K says *"There are currently 142 AD/CVD orders in place on core steel product lines made by Nucor"*, that trade remedies *"play a key role in allowing the American steel industry to compete on a level playing field against unfairly traded imports"*, that Section 232 was *"fully reinstated in 2025 without exceptions or exclusions"*, and that *"No assurance can be given as to the timing or extent of any of these changes."* That is [E2-59]'s administered floor, *"legally through government intervention"*: what the owner keeps in weak years belongs partly to the regime, not to the business. (Shelf context, not a ledger row: Munger at the 2018 meeting, `Annual Meetings/2018 Annual Meeting.txt` line 341, *"the conditions in steel were almost unbelievably adverse to the American steel industry."*)
- **[E3-43]'s demonstration is absent**: *"a company's ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."* The price is indexed and the return is high only in supply-tight years (the table above).

**THE ONE DOOR: [E2-58]'s EXCEPTION, TESTED.** *"A few producers in such industries may consistently do well if they have a cost advantage that is both wide and sustainable. By definition such exceptions are few."* And [E3-43] names this class: *"'a business' earns exceptional profits only if it is the low-cost operator or if supply of its product or service is tight ... With superior management, a company may maintain its status as a low-cost operator for a much longer time, but even then unceasingly faces the possibility of competitive attack."* Nucor's case for the door is real and is set out as its holders would state it below. **It fails on "wide", measured company to company [E4-08]:**

**THE COMPETITOR ROW [E3-28]**: each filer's own 10-K or 20-F facts (companyfacts, newest vintage; `peerrow.py`, `peerrow_out.txt`). Metric A: net income attributable to the parent on average parent equity, %. (Nucor's own computed figures agree with its stated ROE to within half a point in every overlapping year; 2014 8.8 against 8.4 stated.)

| FY | **NUE** | STLD | CMC | X | CLF | MTUS | RDUS | MT |
|---|---|---|---|---|---|---|---|---|
| 2009 | **-3.8** | -0.5 | n/f | -29.3 | (ore) | n/f | n/f | n/f |
| 2010 | **1.8** | 6.9 | n/f | -11.3 | (ore) | n/f | n/f | n/f |
| 2011 | **10.7** | 12.7 | -10.8 | -1.4 | (ore) | n/f | 11.4 | n/f |
| 2012 | **6.7** | 7.0 | 17.2 | -3.6 | (ore) | n/f | 2.5 | n/f |
| 2013 | **6.4** | 7.8 | 6.1 | -48.0 | (ore) | n/f | -30.3 | n/f |
| 2014 | **8.8** | 5.8 | 8.6 | 2.8 | (ore) | 11.5 | 0.8 | n/f |
| 2015 | **1.1** | -4.7 | 5.8 | -52.7 | (ore) | n/f | -30.2 | n/f |
| 2016 | **10.4** | 13.6 | 4.0 | -18.7 | (ore) | n/f | -3.8 | n/f |
| 2017 | **15.9** | 25.9 | 3.3 | 13.8 | (ore) | n/f | 8.6 | 13.3 |
| 2018 | **25.5** | 34.5 | 9.6 | 29.6 | (ore) | -1.6 | 26.1 | 12.7 |
| 2019 | **12.6** | 16.8 | 12.7 | -15.2 | (ore) | -18.7 | 8.3 | -6.1 |
| 2020 | **6.8** | 13.1 | 15.9 | -29.6 | -10.3 | -11.6 | -0.6 | -1.9 |
| 2021 | **55.0** | 60.4 | 19.7 | 65.2 | 79.6 | 29.2 | 21.8 | 34.2 |
| 2022 | **46.9** | 53.5 | 43.6 | 26.3 | 20.1 | 9.6 | 18.9 | 18.2 |
| 2023 | **23.0** | 28.8 | 23.2 | 8.4 | 4.9 | 9.8 | -2.8 | 1.7 |
| 2024 | **9.8** | 17.3 | 11.5 | 3.4 | -10.5 | 0.2 | -34.8 | 2.6 |
| 2025 | **8.5** | 13.3 | 2.0 | delisted | -23.2 | -0.2 | n/f | 6.1 |

  Metric B, pre-tax income on revenue, FY2009-FY2025, same construction: **NUE mean 8.6%, STLD 8.35%**; NUE ahead in 9 of 17 years, STLD in 8. At the troughs: NUE -3.7% / 1.5% / 4.1% (2009 / 2015 / 2020) against U.S. Steel -16.7% / -12.6% / -13.4%.
  **What the row shows.** Against the integrated mills Nucor's cost position is wide: it lost money in one year of the twenty-eight, U.S. Steel in nine of its eighteen in the row. **Against the other electric-arc producers it is not wide at all**: Steel Dynamics earned more on its equity than Nucor in **15 of the 17 years** and a pre-tax margin within a quarter of a point of sales on average; CMC's return is lower, not by a gap that changes the class. The advantage belongs to the **technology class** (scrap-fed electric furnaces against blast furnaces), which Nucor shares with every EAF rival, and which the rivals are adding to: CMC's FY2025 10-K, *"There are a number of ongoing EAF projects in the U.S., with additional capacity expected to come online at various times over the next one to three years. The addition of new mill production and decreased domestic demand could lead to domestic overcapacity"*, while *"We are currently constructing a fourth EAF micro mill in Berkeley County, West Virginia"*; Steel Dynamics' FY2025 10-K names *"an abundance of competition in the carbon steel industry from North American and foreign integrated and mini-mill steelmaking and processing operations"* and ships sheet from its *"Butler, Columbus, and Sinton Flat Roll Divisions"*. Nucor is building its own three-million-ton sheet mill in West Virginia (about $4 billion). **That is [E2-27] in three filers' own words** (each capital decision rational, together they neutralise) **and [E2-58]'s "nothing fails like success"** (the 2021-2022 prosperity, the capacity wave, the 2023-2025 price fall). **The attacker's test [E2-45]** is answered by the attackers themselves: with capital and people, they build the same furnace.
  **Notes on the row.** CLF was an iron-ore miner until 2020 and is shown as "(ore)" before it; its equity was negative in 2015-2018. MT's XBRL row begins in FY2017 (IFRS, USD). U.S. Steel was delisted 2025-06-18 on its merger (25-NSE; 8-K Items 2.01 and 3.01). CMC's FY2011 figure is carried as tagged. CMC's pre-tax row is not tagged under the same element after FY2017 and is left out of Metric B rather than rebuilt.
- Peers named: **7** (Steel Dynamics, Commercial Metals, U.S. Steel, Cleveland-Cliffs, Metallus, Radius Recycling, ArcelorMittal) of the industry's roughly a dozen real competitors in North American steel. **Not obtainable on the same metric:** Gerdau (20-F in Brazilian reais), BlueScope's North Star (Australian, not an SEC filer), Charter Steel (private), Big River Steel (inside U.S. Steel), and the importers. **The class does not turn on them**: the finding rests on the filer's own description of price competition and its own price-per-ton record, which no missing peer can reverse, so the class is **NONE, not PROVISIONAL**.
- **Untapped pricing power** [E3-33]: **none.** The price is indexed to market steel and scrap and falls with utilization; [E5-28] would require near-monopoly, and the row shows an industry of many producers plus imports.
- **Direction [E4-32]:** not widening. Tons to outside customers +5% in eleven years on $26.3bn of capital; return on equity 55.0% (2021) to 8.5% (2025); price per ton down in 2023, 2024 and 2025 under what the 10-K itself calls fully reinstated tariffs.

### THE STRONGEST EVIDENCE AGAINST THIS VERDICT, stated as its holders would state it [E4-51, E4-26, E3-47]
1. *"Nucor IS the corpus's low-cost operator. One loss year in twenty-eight, and that at -3.8% when U.S. Steel lost 29.3% of its equity; at the 2015 trough it earned 1.0% while U.S. Steel lost 52.7%. A cost advantage that survives three troughs is 'wide and sustainable' by any reading of [E2-58]."* **Answer:** wide against blast furnaces, yes; the exception asks for producers who *"consistently do well"*, and the width that sets the price in weak years is against the next EAF ton and the next import ton, where Steel Dynamics out-earned Nucor on equity in 15 of 17 years. And [E3-43] rules on the class directly: the low-cost operator is *"a business"*, which *"unceasingly faces the possibility of competitive attack"*, not a franchise. A cost lead shared with the rest of the EAF class, and being built by that class, is not the exception [E2-58] calls *"few"*.
2. *"Buffett named Nucor as a model."* The 1992 letter, `Shareholder Letters/1992 Letter.txt` line 1224: *"We're admirers of the Wal-Mart, Nucor, Dover, GEICO, Golden West Financial and Price Co. models."* **Answer:** the passage is about headquarters cost (*"Charlie and I have observed no correlation between high corporate costs and good corporate performance"*), not about franchise; it is not a ledger row and I cite it as shelf context only. It supports Nucor's operating culture, which this file does not dispute; the guardrail [E2-37] says a brilliant operator in a commodity industry is *"a remarkable textile company - but not a remarkable business"*.
3. *"Nucor leads its niches: 'the leading supplier' of structural steel, merchant bar, joist and deck, metal buildings; Nucor-Yamato is 'the only North American producer of high-strength, low-alloy beams'; the AEOS, ECONIQ and ELCYON brands."* **Answer:** leadership in share is not pricing; the joists are *"competitively bid"*, the segment price per ton fell 6% on rising volume in 2025, and the filer's single sentence on how it competes is *"primarily ... on price and service."* The high-strength beam is one product inside a two-mill structural group; no filed figure separates its margin.
4. *"The long average, 16.7% on equity over 28 years, is not the 'poor profitability' of [E2-58]."* **Answer:** the average is made by the supply-tight years; the twenty years outside the two booms (2004-2008, 2021-2023) average 8.7%. That is the supply-tight to supply-ample ratio the equation names, and the 2025 figure (8.5%) sits at that level with Section 232 and 142 duty orders in force.
5. *"Vertical integration (DRI plants, the DJJ scrap network), the A-/A3 ratings and the downstream products make it different in kind from a single mill."* **Answer:** these reduce cost volatility and support survival, which is Q4's question; the filer itself says its scrap is bought *"from numerous other sources"* and that *"Competition in our scrap and raw materials business is also vigorous."*
6. *"In 2022 Nucor raised its mill price 11% while its mills ran 17 points emptier and shipped 10% fewer outside tons. That is [E2-44]'s test passed: price up, capacity not fully used."* **Answer:** it is the one such year in the record, it came directly after the tightest year in the series (94% utilization in 2021), on contracts the 10-K says run *"six to 12 months"* with *"a timing difference"* in price adjustment, and it was given back at once (the price per ton fell 15% in 2023 and 10% in 2024). [E2-44] asks for the ability to raise prices *"rather easily ... without fear of significant loss of either market share or unit volume"*; the 2022 rise came with a 10% loss of outside tons. That is [E3-43]'s other door, *"if supply of its product or service is tight. Tightness in supply usually does not last long"*, not a franchise.

**The analyst's own incentives [E4-27], stated (operator rule 9).** This is an unattended overnight cycle with a budget; closing at Q2 is the cheapest outcome, so I have an incentive toward OUT. Against that, the corpus's own admiration for Nucor and the name's reputation pull toward IN. I tried hardest to refute the OUT reading [E4-26]: I built the company's own return series back to 1998 instead of the five-year window, went looking for a year in which Nucor's price rose while its utilization fell (I found one, 2022, and set it out as item 6 below rather than leave the table to hide it), and ran the row in Nucor's favour against the integrated mills before running it against the EAF peers. The six answers above are what survived.

- Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: **not widening** (flat units, falling price per ton, a capacity wave in rivals' own filings)
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____** — **OUT, on the business.** A steelmaker in a commodity industry by the filer's own words (*"we primarily compete on price and service"*), whose price follows utilization and an index, whose weak-year floor is administered by trade law [E2-59], and whose cost advantage is wide only against a shrinking integrated class and not against the EAF rivals who set the next ton's price [E2-58, E3-43]. **The file closes at Q2. Q3 to Q6 carry no verdict; the owner-earnings arithmetic the queue owes is written beneath the close, headed as computation.**

## RECORDED BENEATH THE CLOSE, NOT VERDICTS
*The file closed at Q2 (OUT, on the business). Nothing below is a verdict, and nothing below reopens Q2. It is recorded because the queue owes the owner-earnings arithmetic for every closed name, because the screen row's figures must be checked rather than carried, and because a later reader should not have to rebuild the series.*

### Q3 material, recorded and not scored (the weight case is not declared because the question did not open)
- **[E4-29] fires in the earnings release, not in the 10-K.** The word EBITDA appears nowhere in the FY2025 10-K, the Q2 2026 10-Q or the 2026 proxy; the Q2 2026 release (8-K EX-99.1 of 2026-07-27, accession `0001193125-26-318190`) carries it as a highlight bullet, *"Net earnings before noncontrolling interests of $1.28 billion; EBITDA of $2.02 billion"*, after GAAP net earnings and an "adjusted" figure. A prompt to read, never a verdict [E5-36, E5-38]; for a business whose depreciation is $1.5bn a year, it is the flag the corpus names.
- **Buybacks**: $700M in 2025, $2.22bn in 2024, $1.55bn in 2023, $3.28bn in 2021; 1.53 million shares in Q2 2026 *"at an average price of $228.76 per share"*. The share count on the 10-K covers fell from 319,046,902 (as of 2015-02-20) and 301,000,375 (2020-02-21) to 227,774,615 (2026-02-18) (dei cover facts, companyfacts; the latest 10-Q cover reads 226,875,676). The [E5-08] second condition would be tested against the value range, which is not built here because Q5 did not open.
- Stated policy: *"We intend to return at least 40% of our net income to stockholders over time"*; returned *"approximately 73% of our net income"* over three years. Profit sharing *"10% of earnings before federal taxes"* for most non-officer teammates. None of this is scored.

### Q4 material: OWNER EARNINGS — COMPUTATION — NOT A CLEARANCE
*Arithmetic only, from the filed consolidated cash-flow statements FY2000-FY2025, newest filed vintage per year (`cfs.py` → `cfs_raw.json`, `oe.py` → `oe_out.txt`). No net-income proxy (operator rule 5). (c) is displayed at both ends and not chosen, because no verdict needs it. SBC: the face line from FY2004 (the FY2006 statement restates FY2004-05); FY2000-03 carry no SBC line (APB 25), so the SFAS 123 pro forma fair-value totals from the notes are used ($4.3M, $4.5M, $6.1M, $7.7M, after tax, so slightly understated). **SBC resolves and is complete on the face**: FY2025's $133M equals options $5M + RSUs $87M + AIP/LTIP awards $41M, each stated in Note 16; FY2024 $5M + $106M + $21M = $132M. The minority partners (51%-owned Nucor-Yamato, CSI, NJSM and others) take their share in cash; OCF is consolidated, so an "attributable" column deducts distributions to noncontrolling interests, a disclosed judgment displayed beside the consolidated figure.*

| FY | OCF | SBC | capex | D&A | acquisitions + affiliates | NCI distributions | **OE capex end** | **OE D&A end** | capex end with acquisitions |
|---|---|---|---|---|---|---|---|---|---|
| 2000 | 820.8 | 4.3 | 415.4 | 259.4 | 0.0 | 119.9 | **401.1** | **557.1** | 401.1 |
| 2001 | 495.1 | 4.5 | 261.1 | 289.1 | 121.9 | 120.5 | **229.5** | **201.6** | 107.6 |
| 2002 | 497.2 | 6.1 | 243.6 | 307.1 | 652.7 | 146.7 | **247.5** | **184.0** | -405.2 |
| 2003 | 493.8 | 7.7 | 215.4 | 364.1 | 34.9 | 63.3 | **270.7** | **122.0** | 235.8 |
| 2004 | 1,024.8 | 18.6 | 285.9 | 383.3 | 169.6 | 84.9 | **720.2** | **622.9** | 550.6 |
| 2005 | 2,136.6 | 16.8 | 331.5 | 376.1 | 154.9 | 89.9 | **1,788.4** | **1,743.7** | 1,633.5 |
| 2006 | 2,251.2 | 40.1 | 338.4 | 365.3 | 223.9 | 174.7 | **1,872.7** | **1,845.9** | 1,648.8 |
| 2007 | 1,935.3 | 44.0 | 520.4 | 427.6 | 1,574.1 | 263.1 | **1,371.0** | **1,463.7** | -203.1 |
| 2008 | 2,502.1 | 49.9 | 1,019.0 | 548.9 | 2,546.7 | 275.1 | **1,433.2** | **1,903.3** | -1,113.5 |
| 2009 | 1,173.2 | 54.7 | 390.5 | 566.4 | 96.3 | 190.2 | **728.0** | **552.1** | 631.7 |
| 2010 | 866.8 | 43.0 | 338.7 | 582.6 | 498.8 | 55.4 | **485.1** | **241.2** | -13.7 |
| 2011 | 1,031.1 | 49.0 | 438.9 | 590.4 | 99.9 | 61.7 | **543.1** | **391.7** | 443.2 |
| 2012 | 1,200.4 | 50.7 | 947.6 | 607.0 | 941.3 | 74.8 | **202.0** | **542.6** | -739.3 |
| 2013 | 1,077.9 | 47.5 | 1,197.0 | 610.2 | 85.1 | 76.8 | **-166.5** | **420.3** | -251.5 |
| 2014 | 1,342.9 | 46.4 | 668.0 | 724.4 | 866.4 | 63.7 | **628.5** | **572.1** | -237.9 |
| 2015 | 2,168.8 | 45.8 | 374.1 | 700.0 | 99.5 | 71.9 | **1,748.8** | **1,423.0** | 1,649.3 |
| 2016 | 1,750.0 | 56.5 | 604.8 | 687.1 | 538.0 | 99.6 | **1,088.7** | **1,006.4** | 550.7 |
| 2017 | 1,055.3 | 64.2 | 448.6 | 727.1 | 603.0 | 91.0 | **542.6** | **264.1** | -60.4 |
| 2018 | 2,394.0 | 73.4 | 982.5 | 719.6 | 154.5 | 56.2 | **1,338.0** | **1,600.9** | 1,183.5 |
| 2019 | 2,809.4 | 90.4 | 1,477.3 | 734.7 | 128.9 | 76.3 | **1,241.8** | **1,984.4** | 1,112.8 |
| 2020 | 2,696.9 | 73.9 | 1,543.2 | 785.5 | 132.5 | 115.5 | **1,079.8** | **1,837.6** | 947.3 |
| 2021 | 6,230.8 | 135.8 | 1,622.0 | 864.6 | 1,426.7 | 150.7 | **4,473.0** | **5,230.4** | 3,046.4 |
| 2022 | 10,072.0 | 137.0 | 1,948.0 | 1,062.0 | 3,553.0 | 332.0 | **7,987.0** | **8,873.0** | 4,434.0 |
| 2023 | 7,112.0 | 130.0 | 2,214.0 | 1,169.0 | 106.0 | 435.0 | **4,768.0** | **5,813.0** | 4,662.0 |
| 2024 | 3,979.0 | 132.0 | 3,173.0 | 1,356.0 | 758.0 | 352.0 | **674.0** | **2,491.0** | -84.0 |
| 2025 | 3,234.0 | 133.0 | 3,422.0 | 1,480.0 | 3.0 | 249.0 | **-321.0** | **1,621.0** | -324.0 |

($M. D&A = the depreciation and amortization lines. Acquisitions + affiliates = "Acquisitions (net of cash acquired)" plus "Investment in and advances to affiliates", which carried the JV investments of 2008 and 2010.)

**Every trailing window ending FY2025, against the cap of $56,095.0M** (selected; all 26 in `oe_out.txt`):

| window | capex end | D&A end | capex end with acquisitions | attributable, capex end | attributable, D&A end |
|---|---|---|---|---|---|
| 1y 2025 | **-$321.0M (-0.57%), negative** | $1,621.0M (2.89%) | -$324.0M (-0.58%) | -$570.0M (-1.02%) | $1,372.0M (2.45%) |
| 2y 2024-25 | $176.5M (0.31%), near zero | $2,056.0M (3.67%) | -$204.0M (-0.36%) | -$124.0M (-0.22%) | $1,755.5M (3.13%) |
| 3y 2023-25 | $1,707.0M (3.04%) | $3,308.3M (5.90%) | $1,418.0M (2.53%) | $1,361.7M (2.43%) | $2,963.0M (5.28%) |
| 5y 2021-25 | $3,516.2M (6.27%) | $4,805.7M (8.57%) | $2,346.9M (4.18%) | $3,212.5M (5.73%) | $4,501.9M (8.03%) |
| 10y 2016-25 | $2,287.2M (4.08%) | $3,072.2M (5.48%) | $1,546.8M (2.76%) | $2,091.5M (3.73%) | $2,876.5M (5.13%) |
| 15y 2011-25 | $1,721.9M (3.07%) | $2,271.4M (4.05%) | $1,088.8M (1.94%) | $1,568.1M (2.80%) | $2,117.7M (3.78%) |
| 20y 2006-25 | $1,585.9M (2.83%) | $2,003.9M (3.57%) | $864.1M (1.54%) | $1,422.7M (2.54%) | $1,840.6M (3.28%) |
| 26y 2000-25 | $1,360.6M (2.43%) | $1,673.4M (2.98%) | $761.8M (1.36%) | $1,211.0M (2.16%) | $1,523.8M (2.72%) |
| TTM to 2026-07-04 | $1,437M (2.56%) | $2,765M (4.93%) | about the same (acquisitions $1M) | $1,120M (2.00%) | n/c |

- **Combined range, every trailing window of 3 to 26 years at both (c) ends: $1,360.6M to $4,805.7M, a yield of 2.43% to 8.57%** against the sovereign's 5.49%; attributable to Nucor's holders, **$1,211.0M to $4,501.9M (2.16% to 8.03%)**; with acquisitions and affiliate investments counted, the 26-year capex end is **$761.8M (1.36%)**. **Every window longer than ten years sits below the bond at every end.** The only windows above the bond are the ones that contain the 2021-2023 boom and not much else.
- **Near or below zero, in dollars and a word:** FY2025 alone is **negative at the capex end (-$321.0M)** and FY2013 was **negative (-$166.5M)**; the two-year window 2024-25 is **near zero ($176.5M)**. With acquisitions counted, ten of the twenty-six years are negative (2002, 2007, 2008, 2010, 2012, 2013, 2014, 2017, 2024, 2025) and the rolling five-year windows 2007-2011, 2008-2012 and 2010-2014 are **negative** (-$51.1M, -$158.3M, -$159.8M).
- **Which (c) end, as a judgment (displayed, not used):** capex ran 1.47x depreciation and amortization cumulatively over FY2000-FY2025 ($25,420.9M against $17,287.3M), and the 10-K says *"Our business requires substantial expenditures for routine maintenance and to remain competitive."* Much of the excess is new mills (the West Virginia sheet mill, about $4bn; the Kentucky plate mill; the Lexington micro mill), which is growth by the filer's description, so the D&A end is not declared INVALID by the filer's own words the way [E5-20]'s railroads are; but new capacity in this industry is also how the cost position is defended against rivals building the same furnaces (Q2), so the maintenance share of the excess is not zero. **The honest band is the whole of it, and the 26-year spread between the ends is small ($1,360.6M to $1,673.4M) because the long window averages the build cycles out.**
- **Normalise for luck [E4-41]:** the five-year window 2021-2025 is the screen's top ($4,806M, reproduced to the dollar at $4,805.7M) and it carries FY2021-2023, whose three capex-end years ($17,228M) are 98% of the window's five-year sum ($17,581M). That is the supply-tight window [E2-58] names, and it is the one window that clears the bond.
- **Great, good or gruesome [E4-20]** (recorded, not ruled): over twenty-six years the owner has received about 2.4-3.0% of today's price a year, while the business retained and reinvested far more than its depreciation. That is the account [E4-20] calls gruesome, *"requires you to keep adding money at those disappointing returns"*, in all but the boom years; not ruled, because Q4 did not open.
- **Staying power (recorded)**: A-/A-/A3 ratings, debt to total capital about 24% at year-end 2025, cash and short-term investments $2.70bn (of which about $931M held by majority-owned joint ventures), capex guided to about $2.50bn for 2026. **No coverage test is scored.**

### Survival shape, as a signature WITHOUT a verdict (Q4 did not open)
**#11 THE PASS-THROUGH** as the mechanism: the company survives every trough (one loss year in twenty-eight) but the gains of its own and its rivals' investment pass to customers ([E2-27], [E3-62]'s second step): $26.3bn of capex and acquisitions over FY2014-FY2025, tons to outside customers +5%, price per ton down in 2023, 2024 and 2025, owner earnings at 2.4-3.0% of the price over 26 years. **#14 THE PATRON** as a feature: the weak-year floor is administered by trade law (142 AD/CVD orders, Section 232 *"fully reinstated in 2025"*, *"No assurance can be given"*), a regime that can be withdrawn [E2-59]. **No new shape.** Not to be entered in either instances column, for the reason the earlier wave 7 folds gave.

## Q6: WHAT WOULD REVERSE THIS, IN WORDS (the QLYS ruling: no alert, no PORTFOLIO row)
*Pre-committed [E1-02]. For a name closed at Q2 these are the conditions under which the business question is reopened, each a filed document; the thresholds are the company's own filed record or the peers', not invented numbers.*
1. **Price held in a weak market.** A 10-K whose MD&A reports the steel mills' average sales price per ton flat or up in a year when steel-mill utilization falls below the prior year's, without a scrap-cost increase to explain it. The one such year in the filed record, 2022 (mill price +11% as utilization fell from 94% to 77%), followed the tightest year in the series and was given back in 2023-2024, so the condition is two consecutive such years, or one that does not follow a supply-tight year; either would reopen [E2-44].
2. **A cost gap that is wide against the EAF class, not just the blast furnaces.** Five consecutive years in which Nucor's pre-tax margin exceeds Steel Dynamics' and CMC's by a gap larger than the FY2009-FY2025 average difference (about a quarter of a point of sales against STLD) and holds through a year of falling utilization.
3. **The filer's words change.** A 10-K that drops *"we primarily compete on price and service"* and the substitution risk for a filed, measured reason.
4. **The downstream segment prices.** The steel products segment's price per ton rising in a year of falling non-residential construction volume, with the joist and deck contracts no longer described as *"competitively bid"*.
- **What would confirm the OUT**: a fourth year of falling price per ton; the West Virginia sheet mill and the rivals' announced EAF projects starting while domestic demand is flat (CMC's own *"domestic overcapacity"* sentence); a narrowing or withdrawal of Section 232 or the duty orders with a price response in the next MD&A.
- **Dates**: the Q3 2026 10-Q (the Q3 2025 10-Q was filed 2025-11-12); the FY2026 10-K (February 2027); the West Virginia start-up (the 10-K says *"expected to be completed by the end of 2026"*); the five-yearly sunset reviews of the duty orders. **None is a reason to re-run by itself**; only the filed conditions above are.

---
## SELF-AUDIT
- [x] Questions answered in order; **stopped at the first non-IN verdict** (Step 0; Q1 IN; Q2 OUT). Q3-Q6 carry no verdicts; material beneath the close is labelled as such and the owner-earnings arithmetic is headed COMPUTATION — NOT A CLEARANCE with no entry language.
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 rests on Item 1's own description of the segments, the raw-material mix and the pricing mechanism).
- [x] Every UNRESEARCHED verdict names the artifact (none issued). Every UNKNOWABLE verdict states what cannot be known (none issued; **the [E4-04] perimeter branch was considered and refused in writing**, because it is for names that pass [E3-03]).
- [x] **The cycle was read over the full filed record, not five years**: the filer's own return on equity every year FY1998-FY2025, the price per ton, tons and utilization from each year's MD&A, and the cash-flow statement of every year FY2000-FY2025.
- [x] **The strongest evidence against the verdict was hunted and answered** (six items, Q2, including the one year, 2022, that runs against the reading), and the analyst's own incentives were stated (operator rule 9, [E4-27], [E4-26]).
- [x] Step 0: the filing was read, with accession numbers (10-K FY2025 `0001193125-26-071575`, 10-Q `0001193125-26-345891`, 8-K `0001193125-26-318190` with EX-99.1, DEF 14A `0001193125-26-127739`, every annual cash-flow statement from FY2001's report on); FY2025 OCF, capex, SBC and D&A cross-checked to the filed statement.
- [x] **The deal check was done before any price was used**: no 425, S-4, SC TO or merger 8-K since 2025-01-01; the 5.02s are ordinary succession.
- [x] **One share class; nothing summed**; the cover count's as-of date (the quarter end) is stated.
- [x] **SBC resolves and is complete**: the face line equals the three plan captions in Note 16 for FY2024-25; FY2000-03 use the SFAS 123 pro forma totals, disclosed.
- [x] Owner earnings on a multi-year mean, both (c) ends, **every trailing window 1-26 years and every rolling five-year window**, acquisitions and affiliate investments counted, the minority's cash share displayed, **no net-income proxy**; the dollars and a word given wherever the bottom is near or below zero.
- [x] Competitor row filled (seven peers, same construction and window, filing-sourced; Gerdau, North Star, Charter, Big River and importers named as unobtainable, class NONE not PROVISIONAL because the finding rests on the filer's own words).
- [x] Sovereign for the earnings currency, from the issuing authority, dated (USD 5.49%, US Treasury par curve, 09/25/2026, struck fresh).
- [x] Prices dated; aggregator used for live quotes only and flagged (NUE $247.25, NYSE close 2026-09-25, Yahoo chart endpoint).
- [x] Value range, bar and windage: not applicable (Q5 did not open).
- [x] Run committed to git (commits `80b53d56` claim, `997efc18` Step 0 and Q1, `5605b001` Q2, then this section and the fold).

## REGISTER
- Verdict: [ ] IN **[x] OUT (Q2, on the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **FAIL at Q2 (OUT, ON THE BUSINESS).** A well-run steelmaker in a commodity industry by its own 10-K (*"we primarily compete on price and service"*), whose average price per ton has fallen in every downturn of the filed record since 1998 (-32% in 2009 at 54% utilization; down again in 2023-2025 under Section 232; the one rise in a year of falling utilization, 2022, followed the 2021 shortage and was given back), whose weak-year floor is administered by trade law (142 duty orders) [E2-59], and whose cost advantage is wide against the blast furnaces but not against the electric-arc rivals who set the next ton's price: Steel Dynamics out-earned it on equity in 15 of 17 years, and CMC's own 10-K describes *"a number of ongoing EAF projects in the U.S."* [E2-58, E3-43]. The filer's own return on equity averages 16.7% over 1998-2025 but 8.7% outside the two booms. Owner earnings, computation only: 2.43% to 8.57% of the price over every window of 3-26 years, every window longer than ten years below the 5.49% bond.
- **Brief and screen errors found (every brief has had one):**
  1. **`cap_m` $56,996M** was struck at an older price; today's cap is $56,095.0M. `yield_bottom` 2.92% and `vs_sovereign` -2.43% follow from it and from an older sovereign.
  2. **`oe_bottom_m` $1,666M does not reproduce**: the three-year capex end from the filed statements (and from `tools/run.py`) is $1,707.0M; `oe_top_m` $4,806M reproduces to the dollar ($4,805.7M, five-year D&A end).
  3. **`spread_caveat` said the 4-construction width "CANNOT see variation older than the 5-year window"**, and it could not: the 26-year record puts the bottom at **$1,360.6M (2.43%)**, and **$761.8M (1.36%)** with acquisitions and affiliate investments counted, below every figure in the row.
  4. **`years_filed` 19** is the XBRL depth; the filed record read here runs FY1998-FY2025 (returns) and FY2000-FY2025 (cash flows).
  5. **companyfacts has no operating-cash value for FY2014 or FY2015** (a tag hole); any tag-built multi-year figure across those years is short two years.
  6. **`acq_note` "$5,810M, 10% of cap, inside the window"** reproduces exactly (FY2021-25: $1,426M + $3,553M + $71M + $758M + $2M) and is counted above.
  7. **The brief's commit trailer** (`Claude Opus 5 (1M context)`) differs from the attribution this session's environment supplies (`Claude Opus 5.5`); the brief's line was used, as the dispatcher's written instruction, and the difference is recorded (the BUKS, BR, MRK and NGVC precedent).
- **Tooling, reported, not patched:** (a) the screen's width is four constructions over five years and could not see the lower long-window level (item 3), the same class of limit its own caveat names; (b) the companyfacts OCF hole (item 5). `tools/run.py` was run and its FY2023-25 figures agree with the filed statement.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
