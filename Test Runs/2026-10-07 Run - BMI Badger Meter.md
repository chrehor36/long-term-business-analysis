# Company Run — Badger Meter, Inc. (NYSE: BMI) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`, as amended to 2026-10-07). Governing rules: `Framework/OPERATOR-PROTOCOL.md`.
Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Working folder: `Test Runs/_research 2026-10-07 BMI/` (filings saved there as text, with the scripts that read them).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared:** (1) The brief says earlier run files on Badger Meter exist; none was opened, listed or searched,
and their verdicts are unknown to me. (2) `git log` on the framework file showed commit subjects naming other companies' runs
(ATR OUT at Q7, ACNB OUT at Q2, ACLS and AMAT TOO HARD at Q1, LMT, ABG, PBH); the lock file in `Screens/_daily/` reads
"interactive v5 re-runs batch 2"; the session's start-up git status listed research folders for AYI, BDC, CHD and ARCB; the
memory index loaded with the session carries portfolio-level lines (counts of gate-clearers, holding reviews owed) that name no
company. None of this bears on Badger Meter and none of it is used. (3) `tools/run.py` printed its arithmetic only; no verdict
line about BMI was printed. (4) Added at the close: `git log` after the final commit showed other analysts' commit subjects from
the same batch (CB: Q1 IN, Q2 IN; CHD: Q4, Q5). Seen after every BMI question had closed; not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $123.73 (close 2026-10-06, the quote `tools/run.py` fetched; aggregator, flagged per operator rule 5, live quote only).
  The company's own buyback prices bracket it: $119.61 to $128.57 a share paid April to June 2026 (10-Q, 0001193125-26-313981).
- **Shares by class** from the latest filing's cover: one class, common, **28,986,847** (10-Q for the quarter to 2026-06-30, filed
  2026-07-23, accession `0001193125-26-313981`; `python Screens/cover_shares.py BMI`). Checked: issued 37,221,098 less treasury
  8,234,251 at 2026-06-30 = 28,986,847, the same figure (10-Q balance sheet). No 8-K or prospectus after the 10-Q issues shares;
  the 8-Ks since (0001193125-26-311374, earnings; none later in the index) carry no issuance.
- **Market cap:** 28.987M × $123.73 = **$3,586.5M**.
- **Net debt at the latest filed date (2026-06-30, 10-Q 0001193125-26-313981):** no borrowings; cash $95.7M; the UDlive earn-out
  liability at fair value $12.0M (the 10-Q: up to $50.0M on EBITDA targets, payable 2028) counted as deal financing.
  Net debt **−$83.7M** (net cash). Operating leases left out (rental expense $5.1M in 2025, 10-K Note 6), said so. The revolving
  facility ($150M, extended to 2031 on 2026-06-05, 8-K 0001193125-26-267194) was undrawn. Enterprise value **$3,502.8M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 10/06/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-17, `0001193125-26-054739`): Items 1, 1A, 3, 7, 7A, 8 and Notes 1,
  3, 6; 10-Q Q2 2026 (`0001193125-26-313981`) and Q1 2026 (`0001193125-26-163625`); proxy DEF 14A 2026 (`0001193125-26-106185`);
  8-Ks of 2025-12-11 (`0001193125-25-316007`, officer changes and change-in-control agreements), 2026-04-28 (`0001193125-26-187791`),
  2026-05-21 (`0001193125-26-233404`, Investor Day presentation, ex. 99.1), 2026-06-11 (`0001193125-26-267194`, credit facility),
  2026-07-22 (`0001193125-26-311374`, Q2 release, ex. 99.1). For the cycles: 10-Ks FY2005 (`0000950137-06-002572`, ten-year table
  1996-2005), FY2010 (`0000950123-11-019728`, ten-year table 2001-2010), FY2011 (`0001193125-12-103471`), FY2019
  (`0001564590-20-005707`, ten-year table 2010-2019), FY2021 (`0001564590-22-006284`), FY2022 (`0000950170-23-003676`), FY2023
  (`0000950170-24-016245`); XBRL company facts for 2009-2025 (transcription; checked against the filed statements where used).
- **One figure cross-checked against the filed statement:** net cash provided by operations 2025, **$183,698 thousand** on the filed
  cash-flow statement (10-K FY2025, p. 35) against $183.7M in `tools/run.py`'s XBRL line. They agree. Also checked: 2025 net sales
  $916,663 thousand (filed income statement) against XBRL $916.7M.
- `python tools/run.py BMI`, arithmetic lines only (saved as `run_py_output.txt`): OCF 2023-2025 $110.1M, $155.0M, $183.7M; stock
  pay $5.2M, $6.2M, $9.2M; capex $12.0M, $12.8M, $14.0M; depreciation and amortization $19.5M, $20.2M, $25.8M. Its rule lines,
  ids and floor are v4 material and are not used (Part VII). Owner cash is recast at Q4 from the filed cash-flow statements.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the meters, radios and software will earn over the years, not where the quotation
goes **[M1997-109]**, **[M1994-038]**. The market serves and does not instruct: the stock has fallen from the $181-182 the company
itself paid in October and November 2025 to $123.73, and that fall says nothing about value until the reasoning does
**[M2006-077]**. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**. Who is paid to tell you: the Investor Day deck of 2026-05-21 is a seller's projection of what it sells ("high
single digit 5-Year Organic Revenue Growth Outlook", "10-15% EPS Growth"); it is read as the company's claim, never as an input
**[M2011-083]**, **[M1995-050]**. The analyst's habits: look for "what’s wrong" and "what you’re missing" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**:
- Sales fell 7.8% in the first half of 2026 against 2025 and operating earnings fell 21% (10-Q 0001193125-26-313981); the company
  calls it "uneven AMI project pacing". The record year 2025 may be the top of a conversion wave, not a base.
- About 40% of US water connections are already on AMI (10-K FY2025, Item 1 and Item 7); the cellular conversion that drove
  2021-2025 is a wave with an end, and the filer's own deck dates "technology traction" for cellular AMI to "late 2019".
- The filer's own risk factor: "Static water metering has lower barriers to entry than mechanical metering that could affect the
  competitive landscape in North America" (10-K FY2025, Item 1A).
- The ORION Cellular endpoint rides carriers' networks; "the sun-setting of a network may have an adverse impact on the Company"
  (10-K FY2025, Item 1A).
- Acquisitions are now a stated strategy ("~$500M of M&A 'Dry Powder'", "leverage comfort zone of 1.5-2.5X of EBITDA", Investor
  Day deck): SmartCover $184.0M in 2025 and UDlive $94.4M plus up to $50.0M earn-out in 2026, after fifteen years of small deals.
- Before the radio era the business earned thin margins: earnings from continuing operations 2.4% to 7.4% of sales in 2001-2005
  (ten-year table, 10-K FY2010), and in 2011 the filer named "continued intense price competition on government bid contracts
  for lower cost, manually read meters" (10-K FY2011, forward-looking factors).
- Gross margin fell from 37.2% to 34.2% in 2011 on volume and copper (10-K FY2011, MD&A).

## THE STANDING RULE
A part-interest bought for cash, with no borrowing and no position size set by this run, puts the buyer at no risk of ruin; the
rule binds the buyer's financing and sizing, which this run does not touch **[M2012-081]**, **[L2014-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business, from the filing.** Badger Meter sells water meters (mechanical and ultrasonic), the radio endpoints that read
them (ORION: mobile AMR and cellular AMI), and the cloud software that receives the readings (BEACON, sold as SaaS), mainly to
US water utilities; utility water was about 89% of 2025 sales, flow instrumentation for industrial users about 11% (10-K FY2025,
Item 1). "Water meter replacement and the adoption and deployment of new technologies comprise the majority of smart water
product sales [...] Housing starts have only a minimal impact on annual sales." (same). No customer is over 10% of sales. One
reportable segment.

**The key variables** **[M1998-044]**: (1) the flow of meter replacements at more than 50,000 US utilities, set by the meter's
life (the Investor Day deck says "replacement cycle avg of 12-15 yrs") and by regulation; (2) the share of those replacements
Badger wins, which turns on incumbency at each utility; (3) the price and mix per connection (radio, ultrasonic, software
attached); (4) the cost of brass, resins and electronic components. Of these, (1) is about as foreseeable as a variable gets: a
meter installed in 2015 will be replaced around 2027-2030, and the utility's rate base and bonds pay for it (deck, slide on
funding sources). (2) and (3) are where the forecast can go wrong, and that is Q2's question.

**Is the forecast about customers or about technology?** **[M2017-019]**, **[M2023-030]**. Mostly customers: municipal utilities
replacing a mandated, revenue-generating instrument on a schedule, buying through bids and consultants, and, in the filer's
words, a "Risk-averse customer base [that] prefers incumbent providers, with platform changes infrequent" (deck, 2026-05-21). The
technology moves (manual, then drive-by AMR, then fixed-network AMI, then cellular AMI; mechanical to static meters), but it has
moved over decades, not quarters: the company launched cellular AMI in 2014 and the deck says traction "began in late 2019
(indicative of slow moving/risk averse utilities)". The 2011 10-K already described the same move "toward AMR" and away from
manual meters. Over the thirty years of filed tables (1996-2025) the business has sold the same thing to the same customers.

**Do the past statements tell me the future ones?** **[M2008-033]** Yes in kind: sales rose in 24 of the 29 years from 1997 to
2025, falling in 2000, 2001, 2009, 2011 and 2019, and are falling again in 2026 (ten-year tables, as each was restated, and 10-Ks); the falls are utility project
timing and stimulus pauses, each named by the filer. What the statements do not tell me is how far the 2021-2025 margin step is
a wave; that is a question of the castle and of the value, not of whether the economics can be pictured.

**Would the insiders write it down?** **[M2000-105]** The filer does, in the plain form of a replacement schedule ("Know the
end-of-life window for all utilities", deck) and in the 10-K's estimate that about 40% of US connections are on AMI. The
rival's filing says the same of the market's habits: "many end users are slow to transition to new products or new brands"
(Mueller Water Products 10-K FY2025, 0001350593-25-000066, risk factors). This is not a field whose insiders decline to forecast.

**Can I name the winner, not just the industry?** **[M2012-067]** The rivals named by the filer are Sensus (Xylem), Neptune
(Roper), Itron, Aclara (Hubbell), Mueller, Kamstrup, Hach (10-K FY2025, Item 1). Whether Badger stays among the incumbents is
the castle question; the shape of the industry ten years out (the same utilities, more AMI, more static meters, more software
per connection) can be stated.

**Doubt test** **[M2002-092]**. The doubt I carry is not whether the economics can be pictured but at what level: a meter maker
earning 2.4% to 7.4% after tax on sales in 2001-2005 now earns 15% (2025: $141.6M on $916.7M). That is a question about the castle and
the price, which Q2 and Q7 exist to answer. The product can stay technical so long as "I understand the economic dynamics of
the industry" **[M2011-014]**. This is not a fast-moving technology business in the sense of **[L1993-023]**: the technology
cycle is set by a 12-15 year meter life and the purchasing habits of municipal utilities.

**VERDICT: IN.** The ten-year economics can be pictured: a replacement-driven sale to a slow, regulated customer base, with the
key variables named and their predictability stated from the filings **[M2012-065]**, **[M1998-044]**, **[M2000-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**

**The parts table.** One reportable segment (10-K FY2025, Note 9). Product lines: utility water about 89% of 2025 sales, flow
instrumentation about 11% (Item 1). The filer does not report operating profit by line; utility water carries well over half of
sales and decides. Flow instrumentation, if open, would be carried to Q7 as ordinary; it is small and does not change the box.

**1. The castle questions: what keeps it standing, and how permanent?** **[M1995-038]**, **[M1998-147]** The reason a utility
buys from Badger rather than another vendor, in the filer's own words: "Risk-averse customer base prefers incumbent providers,
with platform changes infrequent absent strong references, proven performance and longstanding customer relationships" and
"Incumbency advantage shared by long-standing peers in a rational market" (Investor Day deck, 8-K 0001193125-26-233404). The
lock is the installed endpoint base and the software: BEACON "is the system of record" and "Interfaces with Utility customer
information system (CIS) and billing vendors" (same deck); "100% software connection to endpoint sale". A utility changes
platform at its meter-replacement cycle, "avg of 12-15 yrs" (deck). The reason lasts as long as municipal utilities stay
risk-averse buyers of a revenue meter, which is the customer habit the rows ask about, not a technology **[M2017-019]**.
Contrary, written down: incumbency is re-won at each replacement. The same deck says Badger has grown by "competitive conversions"
and by "replacing early fixed networks within the AMI category", so the lock is real but not permanent; it is defended once
every 12-15 years per utility, and Badger has been on the winning side of that defence since cellular AMI.

**2. Would it stand without the lord?** **[M1995-038]**, **[L2007-006]** The company was incorporated in 1905 and has passed
through several chief executives; the present one has been chief executive "for more than five years" (10-K Item 1). The
advantage sits in the installed base and the utilities' habits, not in a person. Passes.

**3. The money test: could a well-funded attacker take it?** **[M2011-015]**, **[M2000-077]** The record has the attacker.
Mueller Water Products, a waterworks maker with about $0.8-1.0B of sales and the same distributor channel to the same utilities,
reported its metering business as a segment ("Mueller Technologies"; metering 83%, 88% and 90% of its sales in 2016, 2015 and
2014) and that segment lost money in every year read: operating loss $4.4M (FY2014), $12.9M (FY2015), $11.1M (FY2016), $8.7M
(FY2019), $13.1M (FY2020) (MWA 10-K FY2016 `0001350593-16-000118`; FY2020 `0001350593-20-000066`). Its 2025 10-K still says:
"The United States markets for water metering products and systems are highly competitive. Our primary competitors benefit from
strong market positions and many end users are slow to transition to new products or new brands." (`0001350593-25-000066`). An
attacker with money, a brand in waterworks and the channel could not earn a profit against the incumbents in any of the five
years read. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**

**4. Pricing power, and the agony before a price rise.** **[M2005-020]**, **[M2005-017]** Two cost shocks in the record:
- 2010-2011, copper: gross margin 38.8% (2009), 37.2% (2010), 34.2% (2011), "continuing higher prices for commodities,
  particularly copper, mitigated somewhat by higher prices charged for the Company’s products" (10-K FY2011, MD&A); back to 38.2%
  in 2012 ($122.2M on $319.7M, XBRL). Pass-through, with a lag.
- 2021-2023, components and metals: 40.7% (2021, "strategic pricing actions that offset inflationary cost pressures"), 38.9%
  (2022, "inflationary cost pressures, coupled with production volatility"), 39.3% (2023), 39.8% (2024), 41.7% (2025) (10-Ks
  FY2022, FY2023, FY2025). The 2025 tariffs: "we have enacted certain price increases to offset tariff costs that we are not
  able to mitigate" (10-K FY2025, MD&A), and gross margin rose that year.

"over time the businesses with strong competitive positions manage to pass through increases in raw material costs"
**[M2005-017]**: the record shows that, each time within one to two years. Against: the 2011 10-K names "continued intense price
competition on government bid contracts for lower cost, manually read meters", so the plain meter is sold on a bid; the price
power sits in the radio-and-software system, not in the brass.

**5. Unit volume.** No unit counts are filed. Utility water sales rose from $344.3M (2020) to $816.1M (2025) (10-Ks FY2021,
FY2025), of which SmartCover was $39.7M in 2025. The deck claims a "7% BMI CAGR" in meter units and "21% BMI CAGR" in cellular
endpoints; these are the filer's own figures, unaudited, read as claims **[M2011-083]**.

**6-8. Low cost; the brand; the low bid.** Badger does not claim to be the low-cost producer. The customer is a utility buying
through consultants' specifications and requests for proposal (deck: "Consultant relationships/RFI activity preview to upcoming
projects and influence specs"). The plain manual meter goes to the low bid (2011 10-K, above), the failing form of test 8
**[M2017-009]**; the AMI system, which carries the endpoint and the software for 15-20 years, is chosen on references and proven
performance (deck), the passing form: "people don’t simply just take the low bid in order to get this gadget" **[M2016-006]**.
Half the business passes, half fails; the half that passes is the half that has grown.

**9. Ask the competitors.** **[M1999-130]** No competitor can be interviewed; the nearest is a rival's own filing, quoted at
test 3: Mueller names the incumbents' "strong market positions" and end users "slow to transition to new products or new brands".

**10. Is the moat widening or narrowing?** **[M1999-108]**, **[L2005-010]** Gross margin across the record: 32.9% (2003, 2004),
34.1% (2005), 35.2% (2008), 37-39% (2009-2020, with dips to 34.2% in 2011 and 35.0% in 2013), 39-42% (2021-2025), 41.2% in the
first half of 2026 with sales down 8% (10-K tables FY2005, FY2010; XBRL; 10-Q). Pre-tax earnings as a share of sales: 3.6% (2001)
to 12.6% (2005) in 1996-2007 (computed from the ten-year tables' pre-tax lines), 14-17% in 2008-2010, 8.3% (2018, a year with a
pension charge below operating earnings) to 15.6% in 2011-2022, 16.8%, 19.1%, 20.0% (operating) in 2023-2025, 17.6% in the first half of 2026. Pre-tax operating
earnings on tangible operating capital (primary working capital plus net plant): 31% (2010: $44.8M on $77.6M + $66.1M), 19%
(2011: $27.5M on $79.2M + $66.1M), 20% (2015: $42.4M on $116.1M + $90.9M), 31% (2019: $62.1M on $111.8M + $85.8M), 68% (2025:
$183.4M on $192.0M + $79.6M) (ten-year table FY2019; MD&A FY2025; XBRL net plant). The gross-margin step came with radio
reading (2005-2009) and has held since through two downturns and two cost shocks. Widening.

**11. What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]** Three things, from the filer:
(a) static meters, which have "lower barriers to entry than mechanical metering" (10-K Item 1A), so new meter makers can enter;
the filer's answer is that they "lack brand recognition and product breadth and do not have extensive water utility channel
distribution" to reach "more than 50,000 water utilities" (same); Badger itself has sold ultrasonic meters for "over a decade"
(Item 7). (b) Cellular AMI runs on carriers' networks, and a network sunset "may have an adverse impact" (Item 1A); cellular also
removes the utility-owned radio network that locked a fixed-network AMI customer, which is how Badger took share from fixed
networks and how a rival could take share from Badger. (c) The end of the conversion wave: about 40% of connections are on AMI
(Item 7). (a) and (b) are slow; (c) bears on earnings, not on the castle, and goes to Q7.

**The competitor row** (operating earnings as a share of sales, from their own filings; the whole span read, not one year):

| Filer | What is measured | Years | Margin | Source |
|---|---|---|---|---|
| Badger Meter | whole company | 2010, 2011, 2015, 2019, 2022, 2025 | 16.2%, 10.5%, 11.2%, 14.6%, 15.4%, 20.0% | XBRL operating income over sales; 10-K FY2025 `0001193125-26-054739` |
| Xylem, Measurement and Control Solutions (Sensus with other instruments and services) | segment, GAAP | 2017, 2018, 2019, 2023, 2024, 2025 | 8.6%, 7.9%, -4.4% (8.5% adjusted), 8.3%, 13.2%, 11.7% | XYL 10-K FY2019 `0001524472-20-000006`; FY2025 `0001524472-26-000012` |
| Itron (electricity, gas and water) | whole company | 2008 to 2025 | 5.7% (2008), 8.2% (2010), -18.9% (2011), 6.9% (2012), -7.2% (2013), 0.0% (2014), 2.8% (2015), 5.0% (2016), 7.7% (2017), -2.1% (2018), 5.3% (2019), -0.5% (2020), -4.0% (2021), -0.4% (2022), 5.9% (2023), 10.8% (2024), 13.2% (2025) | XBRL; ITRI 10-K FY2019 `0000780571-20-000004`; FY2025 `0000780571-26-000033` |
| Mueller Water Products, Technologies (83-90% metering) | segment | FY2014, FY2015, FY2016, FY2019, FY2020 | operating losses of $4.4M, $12.9M, $11.1M, $8.7M, $13.1M | MWA 10-K FY2016 `0001350593-16-000118`; FY2020 `0001350593-20-000066`; metering folded into Water Management Solutions from FY2021, not separable |
| Neptune (Roper) | NOT SEPARABLE: inside Roper's Technology Enabled Products segment with CIVCO, Verathon, Northern Digital and others; that segment's operating margin was 33.4%, 33.9%, 34.5% (2023-2025) | | | ROP 10-K FY2025 `0000882835-26-000009`; flagged |
| Kamstrup (Denmark), Aclara (inside Hubbell), Hach (inside Veralto) | non-filer, or not separable | | | flagged |

**The field's returns over the last full cycle, judged in words.** The field is not one of ordinary returns for the incumbent:
Badger earned 10-20% of sales before tax across 2010-2025, through the 2011 and 2019 troughs, on tangible operating capital that
returned 19% to 68% before tax. The returns are not shared by the field as a whole: the entrant with money (Mueller) lost money
in every year read, Itron's whole-company record is thin and often negative, Xylem's segment ran 8-13%. That is the pattern of a
castle that "protects excellent returns" **[L2007-004]** for the long-standing incumbents (the filer's own phrase: "shared by
long-standing peers in a rational market") and not for whoever arrives. The convention on "ordinary" returns does not close it.

**A change for the better, and the full-cycle convention.** The step in gross margin to the high 30s came with radio reading in
2005-2009 and has held through two full sales cycles (peak 2008 to peak 2018; peak 2018 to peak 2025), the copper squeeze of
2010-2011, the cost shock of 2021-2022 and the decline of 2026; that step is credited. The step in operating margin to 19-20% in
2024-2025 is volume leverage at the top of a cellular conversion wave and has not been through a trough; it is not credited as
the castle's level, and Q7 takes the cycle up **[M2005-020]**, **[L1995-022]**.

**What the rows set against it.** "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**
Badger re-wins each utility once every 12-15 years and spends on R&D ($21.6M in 2025, 10-K Item 1) to keep its radio and
software current. The record so far is of widening (test 10), not of rebuilding against loss; the rows give no test that
separates the two beyond that **[L2005-010]**.

**VERDICT: IN.** The castle stands on a risk-averse customer's preference for its incumbent and on an installed endpoint and
software base that is changed only at a 12-15 year cycle; an attacker with money and the channel lost money in every year read;
costs have been passed through each time; the gross margin has widened over twenty years **[M1995-038]**, **[M2011-015]**,
**[M2005-017]**, **[M1999-108]**. Carried forward: the conversion wave and the 2024-2025 margin peak, to Q7.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**What it earns on the capital it needs.** "we’re defining it in terms of the capital actually needed in the business"
**[M2010-090]**; the measure is the return on tangible assets **[M2011-060]**. Tangible operating capital (primary working capital
plus net plant) was $271.6M at the end of 2025 against operating earnings of $183.4M, 68% before tax; it was 19% in the trough
year 2011 and 20-31% in 2010, 2015 and 2019 (the figures and sources are under Q2, test 10). Before crediting it, the rows'
three checks **[L1994-009]**: (a) a cyclical peak: yes in part, 2025 is the top of the conversion wave (Q2, test 11), which is why
the trough-year figures are given beside it; (b) a monopolistic position: no, the filer names seven rivals; (c) leverage: none,
there has been no borrowing since 2020 (ten-year table FY2019; 10-K FY2025, "The Company had no borrowings as of the end of 2025
or 2024"). The equity is not shrunk by buybacks: shares outstanding were 29.1M in 2016-2019 and 29.0M now.

**How much to stand still, how much to grow.** "Every year we spend amounts equal to our depreciation charge simply to stay in
the same economic place" **[L2000-035]**. Capital spending was $12.0M, $12.8M, $14.0M in 2023-2025 against depreciation of
$10.9M, $11.1M, $11.1M (10-K FY2025, cash-flow statement); 2026 capex is expected at $15.0-19.0M (MD&A). So plant needs about its
depreciation and a little more, about 1.5% of sales; the filing does not split maintenance from growth spending, so no
maintenance guess is made **[M2000-144]** and the whole of capex is charged. Working capital is the larger need: primary working
capital ran 26-31% of sales in 2010-2019 (ten-year table FY2019) and 20.9% at the end of 2025 (MD&A FY2025), 22.9% at June 2026
(10-Q). Customers' prepayments fund part of it: contract liabilities were $97.0M at the end of 2025 against $78.3M a year before
(10-K FY2025, revenue note). Does the profit end the year as cash, or is it "sitting in the yard" **[M2008-036]**? operating cash exceeded net earnings in each
of 2023-2025 ($110.1M against $92.6M; $155.0M against $124.9M; $183.7M against $141.6M).

**The growth arithmetic.** From 2019 to 2025 operating earnings rose $121.3M (from $62.1M to $183.4M). The capital that went in:
primary working capital up $80.2M (from $111.8M to $192.0M), net plant down $6.2M, and $278.5M paid for businesses (2020
$29.1M, 2021 $45.3M, 2023 $17.1M, 2024 $3.0M, 2025 $184.0M; cash-flow statements). Counting the acquisitions at what was paid,
as the rows require when judging the capital allocation, "because we paid for it" **[M2011-060]**: about $121M of added pre-tax
earnings on about $352M of added capital, some 34% before tax, of which most came from the organic business (the acquired
SmartCover added $39.7M of sales in 2025 and $19.4M of selling, engineering and administration cost including $5.8M of
amortization; its gross margin is not stated, 10-K FY2025 MD&A). The organic business is close to the rows' best kind, one that
"gives you more and more money every year without putting up anything to get it, or very little" **[M1998-081]**. The price paid
for the acquired growth is the question: SmartCover $184.0M for about $43M of annualised sales, goodwill $118.3M; UDlive $94.4M
plus an earn-out of up to $50.0M for sales of $2.0M in its first two months, goodwill $69.9M (10-Q 0001193125-26-313981). What
those dollars earn is not yet shown in any filing; it is weighed at Q6.

**The caps for Q7.** Owner cash grew 18.9% a year from 2021 to 2025 (Q4). The rows forbid a growth rate that traces to an
absurdity **[M1999-067]** or runs past the discount rate for ever **[M1997-095]**. The 2021-2025 rate is the rate of a conversion
wave plus a $184M acquisition, measured from a year (2021) when supply shortages "limited sales of certain products" (10-K FY2022,
on 2021) to the record year. Q7 tests it against the business's two-cycle sales record.

**WEIGHS FOR.** High returns on the tangible capital the business needs, little plant, falling working-capital intensity, cash
earnings above book earnings **[M1995-047]**, **[M1998-081]**, **[M2010-090]**; the one caution is that growth is now partly bought
at full prices, and what it earns is unproven **[M2011-060]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** ($M; year-end; `tools/run.py`'s first-filed
XBRL table, read against the filed balance sheets of FY2019, FY2022 and FY2025; cash for 2016 and 2022-2025 from the filed
statements, where the XBRL tag is missing):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Jun 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 349.7 | 391.7 | 392.7 | 421.9 | 468.4 | 530.8 | 603.0 | 716.9 | 816.4 | 973.6 | n/r |
| Equity | 256.2 | 277.5 | 303.5 | 331.1 | 361.3 | 403.1 | 442.4 | 516.5 | 606.2 | 713.3 | 682.9 |
| Goodwill + intangibles | 101.2 | 126.8 | 126.7 | 119.4 | 142.3 | 168.5 | 154.9 | 166.9 | 156.8 | 354.1 | n/r |
| Cash | n/r | 11.2 | 13.1 | 48.9 | 72.3 | 87.2 | 138.1 | 191.8 | 295.3 | 226.0 | 95.7 |
| Receivables | 59.8 | 58.2 | 66.3 | 61.4 | 61.7 | 65.9 | 76.7 | 83.5 | 84.3 | 112.4 | 121.2 |
| Inventories | 77.7 | 85.2 | 80.8 | 81.9 | 81.6 | 99.6 | 119.9 | 153.7 | 143.4 | 151.9 | 178.1 |
| Short-term debt | 38.0 | 44.6 | 18.1 | 4.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Reinvested earnings | 223.9 | 244.2 | 257.3 | 285.9 | 314.9 | 353.5 | 395.2 | 458.7 | 547.8 | 645.9 | n/r |

(n/r: not read for this run. 2022 and 2023 cash from the beginning balances on the FY2024 and FY2025 cash-flow statements.)

What moved, and why. Equity nearly trebled from retained earnings; the company paid out about a third of earnings as dividends
and bought back little until 2025. Debt was repaid by 2020 and none has been drawn since. Cash built to $295.3M at the end of
2024 and was then spent: $184.0M on SmartCover (2025), $94.4M on UDlive and $63.5M on its own shares (first half of 2026), leaving
$95.7M. Goodwill and intangibles were stable at $100-170M for nine years and more than doubled in 2025 on SmartCover; they are 50%
of equity at the end of 2025. Receivables fell from 15.2% of sales (2016) to 12.3% (2025), inventories from 19.7% to 16.6%; the
filer's own primary-working-capital ratio fell from 30.3% (2016) to 20.9% (2025) and rose to 22.9% at June 2026 as inventory
built while sales fell (10-Q: "timing of inventory receipts and sales pacing"). Long-term deferred revenue rose to $72.8M (2025)
and $78.8M (June 2026): customers prepay, a source of cash that would reverse if the prepaid software and service book shrank.
The warranty reserve rose from $9.6M (start of 2023) to $21.6M (end of 2025), provisions running ahead of claims paid ($12.9M
against $8.7M in 2025; 10-K Note 1); the filer says its electronic products "have generally caused our annual warranty claims
rates to increase over time". "what the figures are saying and what they don’t say" **[M2025-032]**: they say a business that
funds its growth from its own cash and has no debt; they do not say what the 20-year batteries in the endpoints will cost in
warranty when the cellular fleet ages, which the reserve trend leaves open.

**The real costs.**
- Depreciation **[R1996-023]**: $11.1M a year, below capital spending ($14.0M); capital spending is the larger and is charged.
- Stock pay **[L2015-003]**, **[L2021-003]**: $5.2M, $6.2M, $9.2M in 2023-2025, rising fast; deducted in owner cash. Shares
  outstanding have not risen (29.1M in 2016-2019; 29.0M now), so the dilution has been bought back, which is a cash cost already
  in the figures.
- Amortization **[L2012-003]**: the cash-flow statement's amortization ($23.5M in 2025) is larger than the two amortizations the
  notes itemize (acquired intangibles $14.7M, capitalized software and hardware $3.5M); about $5.3M is not itemized in the notes
  read. It is not added back in owner cash: owner cash starts from operating cash, which already contains it, and acquisitions are
  charged as capital spending at Q7.
- Restructurings: none recurring. One pension termination charge of $19.9M in 2018 ("Following the pension termination charges
  taken in 2018, the pension termination was complete", 10-K FY2019). Postretirement medical is small ($0.2M expected in 2026).
- EBITDA in the filer's mouth: not in the 10-K, the 10-Q's results discussion or the quarterly release; it is the annual bonus
  metric ("adjusted EBITDA (50% weighting)", proxy 0001193125-26-106185), the covenant (8-K 0001193125-26-267194), and the Investor
  Day's "25-30% EBITDA Incrementals" and "1.5-2.5X Net Debt to EBITDA leverage". "Earnings before what really counts in costs"
  **[M2012-035]**. The rows count managements that talk EBITDA as ones they will almost never buy into **[M2002-026]**; this one
  does not report it as its earnings, and pays and borrows on it. Weighs against.

**The tells** **[M1995-064]**. Prepaid and other assets: $16.8M at the end of 2025, about 1.8% of sales, not building. Inventories
in line with sales over the decade, with the 2026 build explained. No reserve released into earnings found; the warranty reserve
moved up, not down. No securitization, no gains on both sides of a contract. Clear speech **[M1994-018]**: the MD&A separates
SmartCover's sales, costs and amortization from the base business, and the Q2 2026 release says plainly that revenue "declined
against the highest quarterly revenue in Badger Meter history".

**The habits carried to Q5** (section A of the gaps case): (1) a featured adjusted figure: the Q2 2026 release puts "Base" sales
and operating earnings (excluding UDlive) in its highlights beside the GAAP figures, which come first **[L2016-006]**; (2)
guidance **[L2019-006]**: the company gives "full-year revenue, excluding acquisitions, flattish versus 2025" (8-K
0001193125-26-311374); (3) a declared growth target **[L2000-037]**: "high single digit 5-Year Organic Revenue Growth Outlook"
and "10-15% EPS Growth" (Investor Day deck). No record of making or beating such targets over years was assembled in this run.

**Owner cash, recast** (owner cash = operating cash less stock pay less capital spending, less the after-tax net interest income
so that the figure is before interest for the all-equity basis; tax at 25%, the company's own rate of 24.1-25.0% in 2023-2025;
$M; script and output in `q7_calc.py`, `q7_calc_output.txt`):

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Operating cash | 80.7 | 89.6 | 87.5 | 82.5 | 110.1 | 155.0 | 183.7 |
| Stock pay | 1.2 | 1.4 | 2.3 | 3.1 | 5.2 | 6.2 | 9.2 |
| Capital spending | 7.5 | 9.1 | 6.7 | 5.9 | 12.0 | 12.8 | 14.0 |
| Net interest income after tax (removed) | -0.2 | 0.0 | 0.0 | 0.4 | 3.0 | 6.5 | 3.8 |
| **Owner cash, all-equity** | **72.2** | **79.1** | **78.5** | **73.1** | **89.9** | **129.6** | **156.6** |
| Paid for businesses, net of cash | 0 | 29.1 | 45.3 | 0 | 17.1 | 3.0 | 184.0 |

Earlier years on the same basis without the interest line: 2011 $24.5M, 2012 $25.3M, 2013 $19.1M, 2014 $22.0M, 2015 $14.5M,
2016 $44.1M, 2017 $33.5M, 2018 $48.4M. Never a net-income proxy (operator rule 5).

**VERDICT on the accounts: IN** (no confusion, no suspicion; the accounts are plain and the cash is real) **[M1995-063]**,
**[M2003-029]**. **WEIGHS FOR** on the whole, with three items weighed against and carried to Q5: EBITDA in pay and borrowing,
the featured "Base" figure, and the declared growth targets **[M2002-026]**, **[L2016-006]**, **[L2000-037]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
"do we really want to be in partnership with this person and count on them to behave in the future [...] as they behaved in
the past" **[M2015-005]**. For a marketable stock the rows read rather than meet **[M2007-081]**: the proxy, the letters and
reports, the record.

**The people.** Kenneth C. Bockhorst joined as chief operating officer in October 2017, became president in April 2018, chief
executive in 2019 and chairman in January 2020 (proxy 0001193125-26-106185); before that Actuant and IDEX. The finance chief of
2019-2025 (Robert Wrocklage) moved to run the North American utility business on 2026-01-01 and the controller since 2019
(Daniel Weltzien) became finance chief (8-K 0001193125-25-316007). The general counsel and the head of human resources have
served more than five years (10-K Item 1).

**Ability, the first yardstick, against the hand dealt** **[M1994-008]**. The hand was a tide: the cellular conversion and the
utilities' spending after the pandemic. Against the same tide the rivals' own figures show how it was played: Badger's utility
water sales rose from $344.3M (2020) to $816.1M (2025), 137%, while Xylem's Measurement and Control Solutions segment rose from
$1,531M (2019) to $2,086M (2025), 36%, and Itron's total revenue fell from $2,502M (2019) to $2,367M (2025) (the filings in the Q2
row). Badger took share. Operating margin rose from 14.6% (2019) to 20.0% (2025); the 2026 decline was met with "cost containment
actions" and lower incentive pay, and SEA fell 6% on the base business in the second quarter (release, 8-K 0001193125-26-311374).
The record is made of products launched before this team (ultrasonic meters "over a decade", cellular AMI launched 2014, per the
deck) and pushed hard by it; "a product of sound thinking rather than simply being in tune with a trend" **[M2013-068]** cannot
be separated cleanly from the trend here. Weighs FOR.

**Integrity, read on doubt** **[M2013-088]**.
- The accounts (Q4): no tell of the accounting kind; reserves that move did so upward; the 2018 pension charge was stated and
  ended. "accounting can offer you a lot of insight into the character of management" **[M1995-064]**: what it shows here is
  plain.
- Candour on bad news **[M1998-039]**: the Q2 2026 release says revenue "declined against the highest quarterly revenue in Badger
  Meter history"; the 10-Q names the cause ("uneven AMI project pacing"). It does not dress the decline, though it does call it
  "temporary" and "expected", which is a claim about the future the reader cannot check.
- The habits carried from Q4: the "Base" figure (ex-UDlive) beside GAAP, GAAP first; revenue guidance for the year; the Investor
  Day's five-year framework of "high single digit" organic revenue growth and "10-15% EPS Growth". The rows condemn predictions
  of growth as "deceptive and dangerous" **[L2000-037]** and earnings guidance as a sign of a culture that wants "to "hit the
  number."" **[L2019-006]**. Read with the rest of the record: no instance found, in the filings read, of a figure changed, a
  reserve released or a target met by accounting; the adjusted figure is a narrow one (an acquisition's two months) and is
  reconciled. The habit is the industry's investor-relations manner, which the rows call a turnoff **[M1998-038]**; it raises no
  doubt about honesty in the record read.
- Legal: "There are currently no material legal proceedings pending" (10-K FY2025, Item 3). No restatement found in the filings
  read.
- The proxy, how they treat themselves against the owners **[M1994-009]**: weighed at Q6, Part B. Nothing there is concealed.

**Love of the business, and after the cheque** **[M2000-098]**. The executives were hired managers, not sellers; the after-sale
test applies to whole-business purchases **[M2007-081]**. The chief executive holds 33,228 shares directly plus options and
units, 105,465 in all (about $13.0M at $123.73), against a salary of $880,000 (proxy); officers and directors as a group hold
1.0%. No instance found of share sales by him in the documents read (Forms 4 were not read).

**VERDICT on integrity: IN** (no doubt raised by the record read; the Q4 habits weighed and found to be manner, not deceit)
**[M2013-088]**, **[M2004-067]**. **Ability WEIGHS FOR** **[M1994-008]**, **[M1999-104]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
**The retention test** **[R1995-009]**, **[M1998-110]**. From mid-2021 to mid-2026 the company earned about $515M, paid about
$168M in dividends and $79M in buybacks, and kept about $266M (sums of the filed annual and half-year figures; the second half of
2021 taken as half the year). Market leg: the share price was $98.12 on 2021-06-30 (10-K FY2021, cover) and is $123.73, a rise of
$25.61 a share on about 29.0M shares, some $740M against $266M kept. Intrinsic leg **[R2009-002]**: all-equity owner cash rose
from $78.5M (2021) to $156.6M (2025) (Q4), while about $250M went into businesses bought and the rest into working capital and
cash; per dollar kept, the yearly owner cash rose by about 29 cents, though much of that rise is the conversion wave and is not
yet shown to last (Q7). Forward: "Can you keep using all of the capital you generate, effectively, for a very long time?"
**[M2010-097]** The organic business cannot (capex 1.5% of sales); the company's answer is acquisitions ("~$500M of M&A 'Dry
Powder'", deck). Passes on both legs over this span; the forward question is open.

**Buybacks** **[L1999-023]**, **[L2011-003]**, **[L2016-002]**. The authorizations name an amount, not a price: $75M (November
2025) plus $75M (February 2026) through November 2028 (10-Q 0001193125-26-313981); the deck calls them "Flexible and
Opportunistic – valuation driven" and names no value. Prices paid: $181.50 and $182.15 (October and November 2025, $15.0M; 10-K
FY2025, Item 5), $146.23 to $148.39 (first quarter 2026), $119.61 to $128.57 (second quarter 2026); $63.5M in the first half of
2026 (10-Qs). In 2019 the 10-K described "$5.2 million in share repurchases to offset equity compensation dilution" (10-K FY2019,
MD&A), the motive ruled out by name: "dilution by itself is a negative and buying back your stock at too high a price is another
negative. So it has to be related to valuation." **[M2016-049]**. The convention for a programme with no stated price: it weighs
against unless the prices paid sit at or below the bottom of the Q7 range. **Recorded back from Q7:** the bottom of the central
range is $36.93 a share (all-equity, acquisitions deducted; the cycle variant's bottom is $37.88); every purchase since October
2025 was made at three to five times that bottom. Weighs AGAINST. The cash used was not needed by the business (no debt; $95.7M
left), so the first condition of **[L1999-023]** held; the second, a price "below its intrinsic value, conservatively-calculated",
did not, by this run's arithmetic.

**Issuance and deals** **[M1995-001]**, **[L2014-012]**. No shares issued for deals; every deal paid in cash, so the one STOP of
Part A **[L2009-019]** does not arise. Value given against value got: SmartCover, $184.0M for a sewer-monitoring business with
$39.7M of sales in its first eleven months, goodwill $118.3M (64% of the price); UDlive, $94.4M plus up to $50.0M on "established
EBITDA targets in the 24 month period following the acquisition", goodwill $69.9M (10-K FY2025; 10-Q). No post-mortem of either
has been published, and the rows ask for one **[L2014-013]**; the earn-out is paid on EBITDA, the figure the rows call
"bullshit earnings" **[M2003-109]**. What the dollars will earn is unknown; the price paid is a high multiple of sales for small
businesses, and the rows warn of buyers "attracted by growth when they should have been repelled by it" where the added capital
earns little **[L2007-009]**. Weighed, not decided.

**Dividends and cash** **[M2004-089]**, **[M2000-051]**. The stated policy is to grow the dividend "annually in line with
earnings"; 33 consecutive years of increases (deck). Paid out about 31% of 2025 earnings ($43.5M of $141.6M). A policy tied to
earnings rather than to whether the dollar can be used is the ratio thinking the rows call "nuts" **[M2000-051]**, but it is
"clear, consistent" **[L2012-015]**. Cash was let build to $295M (2024) before SmartCover; idle, not spent on a marginal deal
at once **[L1993-007]**.

**Part A: UNDECIDED.** Retention has passed over five years; buybacks at prices far above this run's value weigh against; the
deals are paid in cash at full prices, unproven **[M1998-033]**, **[L2016-002]**, **[M2016-049]**.

### Part B: the pay, the board and the owners
- **The bar** **[M2004-097]**, **[M2004-095]**. The performance shares for 2023-2025 vested at 190.5% of target: return on
  invested capital came in at 37.0% against a target of 18.5% and a maximum of 20.5%; free-cash conversion 113.6% against 107.5%
  (proxy 0001193125-26-106185). The company's own measure (after-tax operating income over equity plus debt less cash) was already
  about 21% in 2022, the year before the targets were set ($87.3M × 0.75 on $442.4M of equity less $138.1M of cash; Q4 table), so
  the target sat below what the business was earning when it was set. "a chimpanzee could run the place [...] And a lousy manager
  will always suggest an arrangement like that." **[M2004-097]** The annual bonus paid 179.8% of target for 2025, on adjusted
  EBITDA and free cash flow, maximum on cash.
- **What is measured** **[M2003-019]**: free cash and return on capital are in the managers' control and are the right objects;
  EBITDA is not a measure of earnings **[M1998-086]**. Mixed.
- **How much.** Chief executive $5.93M (2025), $5.08M (2024), $4.54M (2023); the five named officers $10.6M in 2025, about 7.5%
  of net earnings (proxy). A peer group and a compensation consultant (WTW) set the market reference **[L2005-015]**, **[M2004-016]**.
- **Upside only?** **[L1994-020]** Restricted stock and performance units, no options since 2020, a clawback, hedging and pledging
  barred, ownership guidelines of three times salary for the chief executive (proxy). Shares granted, not bought **[L2019-008]**.
  Change-in-control agreements amended for all officers in December 2025 (8-K 0001193125-25-316007), double-trigger.
- **The board** **[M2007-120]**, **[L2014-026]**. The chief executive is also chairman, with a lead director; directors are paid
  $170,595 to $191,595 each in cash and stock (2025), rising for 2026 ($76,000 retainer, $125,000 stock); they hold 2,285 to
  10,226 shares each, largely grants (proxy). "Does he think like an intelligent owner?" **[L2006-014]** cannot be read from these
  documents.
- **The owners as partners** **[L1994-023]**: annual guidance and a five-year framework are given **[M2022-054]**; the 10-K and the
  release are otherwise plain.

**Part B: WEIGHS AGAINST.** Targets set below the return already being earned, an EBITDA bonus, rising pay benchmarked to peers,
a combined chairman and chief executive, directors who own granted rather than bought shares **[M2004-097]**, **[L2005-015]**,
**[L2014-026]**, **[L2019-008]**. None of it is concealed, and none of it is large against the business; the rows rank it below
the manager **[M2007-006]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**. Value is "the discounted value of the cash that can be taken out of a business during
its remaining life" **[R1996-018]**, credited only "for whatever net cash is left every year" **[M1998-080]**, net of what must
be put back in **[M2014-068]**. All figures $M unless a share; script `q7_calc.py`, output `q7_calc_output.txt`.

**The inputs.** Owner cash, all-equity basis, as recast at Q4: 2021-2025 = $78.5M, $73.1M, $89.9M, $129.6M, $156.6M; average
$105.5M. Paid for businesses 2021-2025: $45.3M, $0, $17.1M, $3.0M, $184.0M; average $49.9M. Growth shown on aggregate owner cash,
2021 to 2025: 18.9% a year. Rate: 5.64% (Step 0). Ten years at the growth, then zero nominal growth (Q7's specifics). Market cap
$3,586.5M, net debt -$83.7M (Step 0), enterprise value $3,502.8M; per-share figures are (value less net debt) over 28.987M shares.

**Specific (a), cycles.** The last year of the window is a peak on the filer's own description: the Q2 2026 release measures the
2026 decline "against the highest quarterly revenue in Badger Meter history" and calls the fall "temporary sales pacing effects";
first-half 2026 sales fell 7.8% and operating earnings 21% (10-Q). The first year, 2021, is depressed on the filer's description
("supply chain shortages of certain components which limited sales of certain products throughout 2021", 10-K FY2022). The
whole-cycle variant is therefore shown beside the literal window **[L2005-003]**, **[M2011-101]**, **[M2021-039]**. The cycle is
taken peak to peak on sales (2010 to 2018, 2018 to 2025), because owner cash, the series the convention names, has no clean
peaks: it moves with working capital (troughs in 2010, 2015, 2017 and 2022, a near-continuous rise since 2018). Cycle variant:
owner cash averaged over 2019-2025, $97.0M, less acquisitions averaged $39.8M; growth between the cycle averages (2011-2018
average $28.9M, 2019-2025 average $97.0M, 7.5 years apart) 17.5% a year. Saying so: the choice of sales to date the cycle is mine,
made because the named series gives no peaks to count from.

**Specific (c), acquisitions.** Default pair: acquisitions deducted, total growth credited. Organic pair beside it: acquisitions
left out, organic growth as the filer reports it (sales excluding acquired businesses: 9.2%, 12.0%, 24.4%, 17.5%, 6.1% in
2021-2025; 2023 and 2024 include the small Syrinix and Telog/Unity purchases, whose sales are not stated; compound 14.8%) **[M1998-080]**,
**[M2023-081]**. UDlive closed after the window (May 2026): its price is already out of the June 2026 cash, its earn-out is in net
debt, and with no earnings filed it is credited at nothing.

**Specific (f), the cap, and the absurdity test** **[M1999-067]**, **[M1997-096]**, **[M2003-120]**. The shown rates (18.9%
literal, 17.5% between cycles) are the rate of a conversion wave and of a margin that rose from 14.6% (2019) to 20.0% (2025).
Traced out for ten years: owner cash of $105.5M growing 18.9% a year is $596M in year ten. The business's sales grew 7.2% a year
from the 2008 peak to the 2025 peak ($279.6M to $916.7M; two full cycles) and 7.4% a year from 1996 to 2025. At 7.2% sales growth,
owner cash growing 18.9% would be 47.8% of sales in year ten, above the gross margin of 41.7% (2025), which the filer itself
calls the top of a "Normalized Range of 39-42%" (deck): owner cash cannot exceed gross margin. To avoid that, sales would have to
grow at roughly twice their two-cycle rate for ten more years, from the top of a wave whose end the filer dates by the 40% of
connections already converted. That traces to an absurdity, and the rows require it cut back. **CONVENTION of this run:** the cut-
back rate is the sales growth shown peak to peak over the last two full cycles, 2008-2025, 7.2%; rationale: owner cash can
outgrow sales only while the margin rises, the margin is already at the top of its thirty-year record, and the two-cycle sales
rate is the longest growth the filings show that is not measured from a trough or to a peak. The rows give the cut and no figure
for it; the figure is mine.

**The ranges** (bottom = no growth; top = the growth case; the central case is the first row):

| Case | Base | Growth | Value, $M | Per share | Top / bottom |
|---|---|---|---|---|---|
| **Central: window, acquisitions deducted, growth cut back** | 55.6 | 7.2% | 987 to 1,751 | **$36.93 to $63.29** | 1.77 |
| Whole-cycle variant (2019-2025), acquisitions deducted, cut back | 57.2 | 7.2% | 1,014 to 1,800 | $37.88 to $64.99 | 1.77 |
| Organic pair: acquisitions left out, cut back | 105.5 | 7.2% | 1,871 to 3,321 | $67.44 to $117.45 | 1.77 |
| Uncut, literal window, acquisitions deducted | 55.6 | 18.9% | 987 to 4,334 | $36.93 to $152.39 | 4.39 |
| Uncut, whole-cycle variant | 57.2 | 17.5% | 1,014 to 4,014 | $37.88 to $141.37 | 3.96 |
| Uncut, organic pair | 105.5 | 14.8% | 1,871 to 6,005 | $67.44 to $210.06 | 3.21 |
| Depreciation variant, window, acquisitions deducted, uncut | 54.8 | 21.2% | 972 to 5,111 | $36.42 to $179.21 | 5.26 |

Equity-only beside the central case (owner cash after interest, interest income kept, against market value alone): $35.72 to
$63.39 a share. It does not decide.

**How sure** **[M1999-104]**. The castle is sound (Q2) and the people capable (Q5); the doubt is the level of earnings after the
wave, which the cycle base and the cut carry. The width of the uncut ranges is itself the finding: "Usually, the range must be so
wide that no useful conclusion can be reached." **[L2000-025]**; and a wide range is not cured by demanding a bigger discount
**[M2007-022]**.

**The floor** (CONVENTION, about ten percent, after the company's own tax, on the all-equity basis) **[M2003-149]**, **[M1994-004]**,
**[L2017-004]**. At $3,502.8M of enterprise value: 2025's owner cash, the best year in the record, is a 4.47% yield; the 2021-2025
average 3.01%; the average less the acquisitions it took 1.59%. To earn 10% at today's price, owner cash after acquisitions would
have to grow about 26% a year for ten years; on 2025's peak figure with no acquisition ever again, about 11.6% a year. The two-
cycle sales record is 7.2%.

**Where the price sits.** $123.73 against a central range of $36.93 to $63.29: the price is 1.95 times the top. It is above the
top of every cut-back case, including the organic pair ($117.45), and above the whole-cycle variant ($64.99). A price above the
top of the range closes OUT "however wide the range, by the floor convention" (Q7, specific (f)); the expected return at the price
is below the minimum, "a point at which we drop out of the game" **[M2003-149]**. On the uncut ranges the price sits inside, at
0.81 to 0.87 of the top for the deducted cases, and those ranges are wider than three to one, which by themselves would close
TOO HARD; the cut is what the rows require of a result that traces to an absurdity, and with it the case is not close.

**Fair price** (reporting figure, Part VII; never a verdict, no entry language). This run reads "the price at which the midpoint
of the range earns the floor" as the price at which the average of the two end cases' cash streams earns 10% a year, which equals
the average of the two ends' prices at 10%. Central, all-equity: **$28.29 a share** (enterprise value $736M). Equity-only beside
it: $26.66. Whole-cycle variant: $29.01. For scale only: uncut literal $48.37; uncut cycle $46.27; organic pair cut back $51.07;
organic pair uncut $72.13. The price is 4.4 times the central fair price and 1.7 times the highest fair price shown.

**Q6's buyback test, run here and recorded at Q6:** the bottom of the central range is $36.93; purchases since October 2025 were
made at $119.61 to $182.15.

**VERDICT: OUT.** Valued, and the price does not clear the floor: $123.73 against a central range of $36.93 to $63.29 (whole-cycle
variant $37.88 to $64.99), above the top of every case once the wave's growth is cut back to the two-cycle record **[M2003-149]**,
**[M1999-067]**, **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (the file closed OUT at Q7).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (and not asked by the operator for this run).

---
## THE BOX
**OUT at Q7.** Price $123.73 against a value range of $36.93 to $63.29 a share (central: all-equity, five-year window,
acquisitions deducted, growth cut back to the two-cycle sales record; whole-cycle variant $37.88 to $64.99); fair price $28.29
(all-equity; equity-only $26.66). Q1 IN, Q2 IN, Q3 weighs for, Q4 IN and weighs for, Q5 IN on integrity, Q6 Part A undecided and
Part B against. Not TOO HARD: the castle and the people were judged; what failed is the price. On the uncut growth rates the
ranges are wider than three to one (TOO HARD by the width convention) with the price inside them; the run cuts the growth back
because ten years at the wave's rate traces to an owner-cash margin above the gross margin (Q7). Either way the price is not a
screamer and needs a pencil **[M2009-005]**, **[M1996-084]**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(written down, not weighed; no verdict; the box unchanged)* **[M1997-127]**
- **Q8 (the bond):** the 30-year Treasury yields 5.64% (Step 0); BMI's best-year owner cash is 4.47% of enterprise value, the
  2021-2025 average 3.01%, the average less acquisitions 1.59% (Q7).
- **Q9 (debt and exposures):** no borrowings at 2026-06-30; the $150M revolver, undrawn, extended to 2031, carries covenants of
  consolidated net debt to EBITDA of at most 3.00 and interest cover of at least 3.00 (8-K 0001193125-26-267194); the Investor Day
  names a "leverage comfort zone of 1.5-2.5X of EBITDA" for acquisitions and "~$500M of M&A 'Dry Powder'" (deck); the UDlive
  earn-out of up to $50.0M falls due in 2028 (10-Q). Single suppliers for "most brass castings and certain resin and electronic
  subassemblies" (10-K Note 6) and for microprocessors (Item 1A); electronic components tightened by data-centre demand in 2026
  (10-Q, "longer lead times, reduced component availability, and increased procurement costs"). Warranty reserve $21.6M, rising,
  on products with warranties of "one to twenty years" (10-K, critical estimates). No material litigation (Item 3).
- **Q10:** nothing.
- No integrity facts were found that the run did not weigh at Q5; no integrity flag.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Commits:
      Step 0 to Q1, Q2 (and one correction of a margin span in Q2, committed separately), Q3, Q4, Q5, Q6, Q7, the close.
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was present and held by the
      dispatching session ("interactive v5 re-runs batch 2"); folding is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; no text search across `Test Runs/`
      was made; the research folder was created by a direct path. What was seen by accident is declared under CONTAMINATION.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the script `check_ids.py` in the research folder (no E-ids; every
      id present; every quoted fragment beside an id found in that row). Every filing fact carries its document and accession.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from operating cash, stock pay and capital spending, never a net-income proxy; the
      sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (Foundations; Q2 tests 1, 4, 6-8, 11; Q4 warranty and EBITDA; Q6 buybacks and deal
      prices). Facts for later questions are under AFTER THE STOP.
- [x] Not a point-in-time run; rows of any date cited.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the final commit: PASS (2026-10-07); `check_ids.py`: 121 ids, 0 problems. It was not
      run before each per-question commit; the template's line asks for it before "the commit", and the brief asks for a commit per
      question, so the check was run once, at the end.
- Departures, said plainly: (1) the cycle for specific (a) is dated on sales, not on owner cash, because owner cash shows no
  clean peaks (Q7); (2) the growth cut-back figure (7.2%) is this run's CONVENTION (Q7); (3) the fair price's "midpoint" is read
  as the average of the two end streams at 10% (Q7); (4) the research folder holds the filings as converted text, committed with
  the scripts that read them, so another analyst can check every figure without a fetch.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. **(1) The absurdity cut has no figure, and on this name it decides the box.** Specific (f) says the shown rate is
the cap and "any result that traces to an absurdity is cut back", but not to what. With the shown 18.9% the ranges are 4.4 to 1
and close TOO HARD by the width rule with the price inside them; cut back to the two-cycle sales record (7.2%) the range is 1.8 to
1 and the price is twice its top, OUT. A different cut gives the same box: at 12% the top is $90.74 (window) or $93.27 (cycle), at 14% $105.59 or
$108.54, and only a rate above about 16% puts the top above the price; so the box is robust to the figure once a cut is made, but whether to cut at all is a judgment the text leaves to the analyst. A stated test (owner cash
cannot exceed gross margin; growth no faster than the business's record across two cycles) would make two analysts agree.
**(2) Specific (a) names owner cash as the series that defines the cycle**, but a business whose owner cash moves with working
capital has no clean peaks; I dated the cycle on sales and said so. **(3) "The price at which the midpoint of the range earns the
floor" admits two readings**: the midpoint value (computed at the long rate) bought at a price that yields 10%, or the average of
the two cases' cash streams valued at 10%. They differ; I used the second and said so. **(4) Specific (c) credits "organic growth,
as the filer reports it"**, but filers report organic growth of sales, not of owner cash; I used the sales figure, which is the
only one filed. Also noted, not a fault of the text: the convention on a change for the better (credited only on a full cycle)
fits gross margin, which has been through two cycles here, but not the operating-margin step of 2024-2025, which has not; the run
credited the first at Q2 and handled the second at Q7 through the cycle base and the cut, which seems the intended division.
