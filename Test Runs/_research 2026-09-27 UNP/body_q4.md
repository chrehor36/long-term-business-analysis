## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

*From the filed consolidated cash-flow statements FY2003-FY2025, newest filed vintage per year (each year's figure as last restated two 10-Ks later; `cfs2.py` → `cfs_blocks.txt`, `oe.py` → `oe_out.txt`). No net-income proxy (operator rule 5). FY2000-FY2002 are left out: those statements consolidate the Overnite trucking business, sold in 2003, so they are a different perimeter. SBC: the note table from FY2008 on (the face line FY2006-FY2008 agrees: 35, 44, 65); FY2003-FY2005 carry no expense line (APB 25), so the FY2005 10-K's pro forma fair-value totals are used ($50M, $35M, $50M, after tax, so slightly understated). **Acquisitions: none of any size in the record**; the investing line "Acquisition of equipment pending financing" (FY2004-FY2012) is matched in every year by "Proceeds from completed equipment financings" of the same amount and is a financing round-trip, not a purchase. **Non-cash capital-lease financings** (equipment acquired with debt, outside "Capital investments") are shown in their own column and in a third construction.*

| FY | OCF | SBC | capex | depreciation | capital leases, non-cash | **OE capex end** | **OE depreciation end** | capex / depreciation |
|---|---|---|---|---|---|---|---|---|
| 2003 | 2,443 | 50 | 1,752 | 1,067 | - | **641** | **1,326** | 1.64 |
| 2004 | 2,257 | 35 | 1,876 | 1,111 | - | **346** | **1,111** | 1.69 |
| 2005 | 2,595 | 50 | 2,169 | 1,175 | - | **376** | **1,370** | 1.85 |
| 2006 | 2,880 | 35 | 2,242 | 1,237 | 16 | **603** | **1,608** | 1.81 |
| 2007 | 3,277 | 44 | 2,496 | 1,321 | 82 | **737** | **1,912** | 1.89 |
| 2008 | 4,044 | 65 | 2,754 | 1,366 | 175 | **1,225** | **2,613** | 2.02 |
| 2009 | 3,204 | 58 | 2,354 | 1,427 | 842 | **792** | **1,719** | 1.65 |
| 2010 | 4,105 | 74 | 2,482 | 1,487 | - | **1,549** | **2,544** | 1.67 |
| 2011 | 5,873 | 82 | 3,176 | 1,617 | 154 | **2,615** | **4,174** | 1.96 |
| 2012 | 6,161 | 93 | 3,738 | 1,760 | 290 | **2,330** | **4,308** | 2.12 |
| 2013 | 6,823 | 98 | 3,496 | 1,777 | 39 | **3,229** | **4,948** | 1.97 |
| 2014 | 7,385 | 112 | 4,346 | 1,904 | - | **2,927** | **5,369** | 2.28 |
| 2015 | 7,344 | 98 | 4,650 | 2,012 | 13 | **2,596** | **5,234** | 2.31 |
| 2016 | 7,525 | 82 | 3,505 | 2,038 | - | **3,938** | **5,405** | 1.72 |
| 2017 | 7,230 | 103 | 3,238 | 2,105 | 19 | **3,889** | **5,022** | 1.54 |
| 2018 | 8,686 | 96 | 3,437 | 2,191 | 12 | **5,153** | **6,399** | 1.57 |
| 2019 | 8,609 | 93 | 3,453 | 2,216 | - | **5,063** | **6,300** | 1.56 |
| 2020 | 8,540 | 73 | 2,927 | 2,210 | - | **5,540** | **6,257** | 1.32 |
| 2021 | 9,032 | 88 | 2,936 | 2,208 | - | **6,008** | **6,736** | 1.33 |
| 2022 | 9,362 | 99 | 3,620 | 2,246 | - | **5,643** | **7,017** | 1.61 |
| 2023 | 8,379 | 107 | 3,606 | 2,318 | - | **4,666** | **5,954** | 1.56 |
| 2024 | 9,346 | 118 | 3,452 | 2,398 | - | **5,776** | **6,830** | 1.44 |
| 2025 | 9,290 | 142 | 3,791 | 2,465 | - | **5,357** | **6,683** | 1.54 |

($M. SBC for FY2003-05 after tax, pro forma. TTM to 2026-06-30 from the 10-Q: OCF $10,263M, SBC $131M, capex $3,759M, depreciation $2,513M: **$6,373M capex end, $7,619M depreciation end**; H1 2026 operating cash rose to $5,516M from $4,543M, on the tax timing named at Q3.)

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** Every trailing window ending FY2025 against the cap of $162,651.9M (all 23 in `oe_out.txt`):

| window | capex end | depreciation end | capex end with capital leases |
|---|---|---|---|
| 1y 2025 | $5,357.0M (3.29%) | $6,683.0M (4.11%) | $5,357.0M |
| 3y 2023-25 | **$5,266.3M (3.24%)** | $6,489.0M (3.99%) | $5,266.3M |
| 5y 2021-25 | $5,490.0M (3.38%) | **$6,644.0M (4.08%)** | $5,490.0M |
| 10y 2016-25 | $5,103.3M (3.14%) | $6,260.3M (3.85%) | $5,100.2M |
| 15y 2011-25 | $4,315.3M (2.65%) | $5,775.7M (3.55%) | $4,280.2M |
| 20y 2006-25 | $3,481.8M (2.14%) | $4,851.6M (2.98%) | $3,399.7M |
| 23y 2003-25 | $3,086.9M (1.90%) | $4,384.3M (2.70%) | $3,015.5M |

- **Short-window mean** (window: 3y 2023-25): **$5,266.3M capex end, $6,489.0M depreciation end**
- **Long-window mean** (window: 23y 2003-25): **$3,086.9M capex end, $4,384.3M depreciation end**
- **Spread, conservative end:** the 3y and 5y capex ends differ by **4.2%**; the 10y is 3.1% below the 3y; the 23y is **41.4% below**.
- **Combined range** (window spread x capex band): **$3,086.9M to $6,644.0M (1.90% to 4.08%)** across every window of 1-23 years at both ends; **$5,103.3M to $6,644.0M (3.14% to 4.08%) across the windows of 1-10 years.** No year in the record is negative at either end; the one negative figure is FY2009 with the $842M of capital-lease equipment counted (-$50M).
- *Is that range too wide to reach a conclusion? **No, because every construction in it sits below the 5.49% bond**: the width cannot change a Q5 answer that every point of it gives the same way.*
- **The spread is not a cycle; it is a change in the business, and the long windows are not the normal.** Rolling five-year capex-end means rose in every window from $540.6M (2003-07) to $5,481.4M (2018-22), then flattened ($5,384.0M, $5,526.6M, $5,490.0M for 2019-23, 2020-24, 2021-25). What rose was the margin: operating ratio 81.5% (2003) to 59.8% (2025), on the repricing era and then the cost programme (Q2). The early years are a different, worse-run railroad; averaging them in would understate today's earning power, and **[E4-41]'s instruction runs the other way here: there is no lucky year to strip out of the recent window, but there is a tax-timing flatterer in 2025-2026** (cash taxes 9.6% of pretax in 2025 against 18.0% in 2023; the TTM figure is carried as a ceiling, not a base).
- *A wide spread is also a Q4 finding: a distorted year sits in the window? Named:* **FY2017** (a $5.9bn non-cash tax credit in net income; operating cash unaffected), **FY2009** (the $842M capital-lease year), **FY2003-04** ($100M a year of pension funding inside operating cash), **FY2025-26** (bonus depreciation and purchased tax credits lowering cash tax). Working-capital swings are small (the largest, -$324M in FY2002, sits outside the window).
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default proxy **[E3-44, E2-41]**; for capital-intensive businesses the D&A end is INVALID and (c) is judged up from total capex **[E5-20]**. **This is the named case, and the brief's hypothesis was tested, not assumed.** [E5-20] is said of *"all railroads"*: *"merely spending their depreciation expense will not keep them in the same place ... the true maintenance capex, if you're looking at 4.3 billion, is higher than 60 percent of that number."* **The filings agree three ways.** (1) Capital investments exceeded depreciation **in every one of 23 years, by 1.32x at the lowest (2020) and 1.72x cumulatively** ($71,496M against $41,656M). (2) The filer's own inflation note: *"assuming that we replace all operating assets at current price levels, depreciation charges (on an inflation-adjusted basis) would be substantially greater than historically reported amounts."* (3) The filer's capital table: in 2025, *"Total road infrastructure replacements"* alone were **$1,987M**, locomotives and freight cars **$810M** (of which $311M lease buyouts), technology $377M, and *"Total capacity and commercial facilities"* **$617M**; **capex less capacity-and-commercial less lease buyouts was $2,863M in 2025, $2,809M in 2024, $2,885M in 2023, above depreciation in every year** ($2,465M, $2,398M, $2,318M) and at **75-81% of total capex**, inside [E5-20]'s *"higher than 60 percent"*. **What I hunted for against it** [E4-26]: a year in which capex fell below depreciation (none), a filer statement that part of the excess is pure expansion (the capacity-and-commercial line, 14-18% of capex, is removed in the middle construction), and lease buyouts that move a rent into capex ($57M-$311M, removed). The hypothesis survives: **the depreciation end is not a maintenance figure for this business; it is a lower limit that the filings say is never reached.**
- Band used: **capex end ($5,266.3M, 3y) as the conservative figure; the filer-split construction (operating cash less SBC less capex net of capacity-and-commercial and lease buyouts: $5,387M, $6,419M, $6,285M; 3y mean $6,030.3M, 3.71%) as the optimistic figure; the depreciation end ($6,489.0M, 3.99%) displayed as the limit only.** Where in the band it sits and the reason cited from the filing: capacity spending is how a network keeps *"its long-term competitive position"* against a parallel rival and the truck [E2-23], so the whole of it is not growth; the capex end is the default this business's corpus passage directs.
- Stock compensation subtracted in full **[E5-06]**: yes, every year; resolves and is complete (Step 0: $142M = options $24M + retention awards $102M + ESPP $16M).
- *If the capex band changes the verdict → **UNKNOWABLE**.* It does not: both ends and every window are below the bond (Q5).

**THE COMBINED PERIMETER, same construction (COMPUTATION — NOT A CLEARANCE, and not a forecast of the closing).** Norfolk Southern's filed cash-flow statements (FY2025 10-K, accession `0001628280-26-006268`; FY2024 10-K, accession `0000702165-25-000008`; cross-checked: *"Net cash provided by operating activities 4,361 4,052 3,179"*, *"Property additions (2,204) (2,381) (2,327)"*), SBC from its expense tag ($40M, $40M, $63M): three-year owner earnings **$1,512.3M capex end, $2,468.3M depreciation end**, and **$964.7M with the $1,643M 2024 purchase of the CSR assets counted** (2023 is the East Palestine year). Combined, after-tax interest on $20bn of new debt at the coupons of Union Pacific's 2025 issues (5.100% and 5.600%; 22% tax): **$5,944.0M capex end, $8,122.7M depreciation end, on about 819.1M shares ($7.26 and $9.92 a share against $8.86 and $10.92 standalone)**; with every dollar of the claimed $2.75bn pre-tax synergies realised after tax, $8,089.0M and $10,267.7M ($9.88 and $12.54 a share). `q5.py` → `q5_out.txt`.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [x] **good** — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- Evidence: return on invested capital 13.9-17.3% in every year 2018-2025 (filer's own, Q3), about **20% on the roughly $15.4bn of capital added since 2015** (Q3), against [E5-40]'s *"cash retained to perhaps earn an average of 12 percent or something like that, which we regard as quite satisfactory"*. Capital-hungry by construction (1.72x depreciation), so not great [E4-43]: *"A company that needs large increases in capital to engender its growth may well prove to be a satisfactory investment."* **On the combined perimeter the added capital is the $81.6bn purchase, which buys 1.85-3.02% before synergies and 5.2-5.7% with all of them (Q3)**: the incremental dollar there earns about the bond, not [E5-40]'s 12%.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **yes.** Operating cash $8.4-9.4bn in every year 2018-2025; one net loss year in the record read (1998, the Southern Pacific integration, return on equity -8.1%); a profit in 2004 at an 89.4% operating ratio and in 2009 at a 16% volume fall.
- (2) massive liquid assets: **no, and it does not need them.** At 2026-06-30: cash $1.6bn, short-term investments $0.5bn, $2.0bn undrawn revolver, $600M undrawn receivables facility (10-Q), about **$4.7bn** against 2026 maturities of $1,521M.
- (3) **no significant near-term cash requirements**: **standalone yes; combined no, and it is known.** Standalone debt maturities are laddered: $1,521M (2026), $1,291M, $1,239M, $1,276M, $753M (2030), $27,412M thereafter out to 2072. **The merger is a significant near-term cash requirement by contract**: about **$20bn of cash consideration at closing (expected 2027), to be *"funded through a combination of new debt and cash accumulated"***, with a *"leverage covenant"* the 10-K expects the financing to carry; if the STB refuses, a **$2.5bn fee**.
- Leverage, named and quantified **[E4-16, E3-29]** — *there is no ratio ceiling in this framework and the corpus supplies none*: total debt **$31,814M** (2025) against operating income $9,846M; the joint release states **debt to EBITDA of about 3.3x at closing**. **Coverage [E2-54]** (interest *"comfortably met out of current cash flow net of ample capital expenditures"*): 2025 operating cash plus interest paid less all capex, $6,810M, against interest expense $1,309M = **5.2x standalone**; on the combined perimeter (Norfolk Southern $4,361M + $765M - $2,204M = $2,922M; interest $1,309M + $792M + about $1,070M on the new debt) **about 3.1x**. Comfortably met on both perimeters at capex, not at depreciation, which is the corpus's own form of the test.
- Other claims on the cash, named: personal-injury liability **$413M** and environmental liability **$259M** (2025-12-31, Note 17); 83% of the workforce in 13 unions, with the merger's labour pledge that *"every union employee who wants a job in the combined company will have one"* (joint release); Norfolk Southern's Eastern Ohio (East Palestine) liabilities travel with it ($15M of further expense in Q2 2026, its 10-Q). Pension overfunded (Q3).

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: **#11 THE PASS-THROUGH** (`Screens/SURVIVAL SHAPES - index.md`): the company survives, and the gains of its own productivity programme go partly to the shippers as falling real price while the other western network and the truck set the price of the next carload; **with #24 THE BOUGHT AVERAGE as a feature** (a business whose real price per car has fallen since 2019 buys a lower-return network with 225M of its own shares and $20bn of debt, so that the headline grows while owner earnings per share fall about 18% at closing before synergies), **and [E2-59]'s regime cap as a feature** (the STB's revenue-adequacy and switching rulemakings, and the conditions of the merger approval). No new shape is argued.
- Quantified from filed figures, and the resulting outcome: real revenue per car at fixed 2018 mix **-12.4% over 2018-2025**; each 1% of 2025 freight revenue is **$232M** before tax; the operating-ratio lead the cost programme built was given back in part at once (2022: 60.1%, 2023: 62.3%). If price keeps pace with cost and no more, owner earnings grow with nominal revenue, **about 3% a year over 1997-2025 (freight revenue $9,712M to $23,220M, carloads 8,453,000 to 8,447,000, flat over 28 years)**. **Outcome: the company lives and earns about the bond on today's price; the owner's return is compressed, not destroyed.** Solvency: interest covered 5.2x (3.1x combined) at full capex.
- Likelihood: [ ] likely [x] **a real possibility** (the compression is already in the 2019-2025 record; a solvency death is a low-level possibility)
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____** — **IN on both perimeters: a good-class business [E4-43, E5-40] that survives its named death; the merger turns a laddered balance sheet into one with a $20bn near-term requirement and about 3.1x coverage, which is survivable and is carried to Q5 and Q6.**
