# Company Run — H World Group Limited (Nasdaq: HTHT; HKEX: 1179) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for HTHT, H World or Huazhu).

**CONTAMINATION, declared before any fetch (seen by accident, not opened, not used):** (1) the session context showed the
repository's recent commit subjects, which are the fold of a v5 run of Hyatt (H) dated 2026-10-14 with its box and figures;
Hyatt is a hotel company and a possible rival, and nothing from that commit subject is used here. (2) A directory listing of
`Test Runs/` made to check that this run's file name was free showed file and folder names of other runs dated 2026-10-14
(CHH, H, HGV, HLT, MAR, WH and four steel names); none was opened. (3) The session's memory index lines name the queue state
and counts of gate-clearers in general terms; nothing about this company. Competitors are read from their own SEC filings only.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** US$44.17 per ADS, close 2026-10-13 (Nasdaq: HTHT; Yahoo Finance chart feed, an aggregator, live quote only, flagged per
  operator rule 5). One ADS is ten ordinary shares, so US$4.417 per ordinary share. The Hong Kong line (1179) was not used.
- **Shares by class:** one class of ordinary shares (no class with different voting rights, 20-F Item 6.E). Cover of the 20-F for FY2025
  (filed 2026-04-24, accession `0001104659-26-048058`): 3,071,525,690 shares outstanding at 2025-12-31; `python Screens/cover_shares.py HTHT`
  returns the same figure. Check against the balance sheet: 3,098,323,810 issued less 26,798,120 treasury = 3,071,525,690, agrees.
  **A later count governs:** the interim report furnished on 6-K on 2026-09-23 (accession `0001104659-26-109789`, Exhibit 99.1) states
  3,233,044,130 issued and 78,984,260 treasury, 3,154,059,870 outstanding at 2026-06-30 (check: 3,233,044,130 less 78,984,260 =
  3,154,059,870, agrees). The rise is the conversion of the US$500 million 3% convertible notes due 2026 at maturity: "an aggregate
  principal of US$499.6 million under the notes was converted into 13 million ADSs" (same exhibit, Note on Convertible Senior Notes
  due 2026; 133,496,890 ordinary shares in the statement of changes in equity), less 61,598,060 shares repurchased in Q2 2026.
  No later count is filed (6-Ks of 2026-09-04 to 2026-09-23 read). **Count used: 3,154,059,870 ordinary shares = 315,405,987 ADS.**
- **Market cap:** 315,405,987 x US$44.17 = **US$13,931.5 million**; at the PBOC central parity of 6.7298 RMB per US$ on 2026-10-13
  (China Foreign Exchange Trade System, chinamoney.com.cn, the central bank's publishing agent for the parity) = **RMB 93,757 million**.
- **Sovereign for the earnings currency (RMB):** **2.0600%**, the 30-year point of the China government bond yield curve published on
  the Ministry of Finance page "财政部-中国国债收益率曲线" through ChinaBond (China Central Depository & Clearing), the curve's
  compiler for the MOF; data for 2026-10-14 (`yield.chinabond.com.cn/cbweb-czb-web/czb/czbChartSearch`, saved as
  `_research 2026-10-14 HTHT/sovereign_CNY_chinabond_mof_2026-10-14.json`). The MOF's own `gks.mof.gov.cn` curve page returned
  "page does not exist" and HTTP 502 on four tries. `tools/sources.py` has no RMB source; the rate was fetched by hand and the
  tool's refusal is recorded below. The curve is dated one day after the price; the move is not material to any conclusion here.
  **Euro earnings of Deutsche Hospitality** (the HWI segment): reported by the filer in RMB; legacy DH's adjusted EBITDA summed
  to a loss of RMB 144 million over 2021 to 2025 against RMB 23,890 million for legacy Huazhu (Q2 parts table). They are carried in
  RMB as filed and discounted at the RMB rate, with no separate euro rate (CONVENTION of this run; rationale: the part is below
  zero over the window and cannot move the box). The ECB 30-year rate was not fetched for that reason.
- **Filings read** (operator rule 4): the 20-F for FY2025 (filed 2026-04-24, `0001104659-26-048058`) Items 3.D, 4, 5, 6, 7, 16E and
  the financial statements; the 20-Fs for FY2023 (`0001104659-24-050202`), FY2021 (`0001104659-22-050640`), FY2019
  (`0001193125-20-113650`) and FY2017 (`0001104659-18-025415`) for the statements of 2015 to 2022 and the balance sheets of 2016 to
  2023; the Q2 2026 results 6-K of 2026-08-17 (`0001104659-26-097496`), the Q1 2026 results 6-K of 2026-05-15 (`0001104659-26-061705`),
  the interim report 6-K of 2026-09-23 (`0001104659-26-109789`), the AGM notice and proxy materials 6-K of 2026-05-11
  (`0001104659-26-058221`), the AGM results 6-K of 2026-06-26 (`0001104659-26-077948`), the director appointment 6-K of 2026-07-28
  (`0001104659-26-087286`), and the bond 6-Ks of 2026-09-04, 2026-09-10 and 2026-09-16 (`0001104659-26-105180`,
  `0001104659-26-106470`, `0001104659-26-108062`). The proxy furnished on 6-K carries the agenda (auditor, two director
  re-elections) and no pay table; pay is read from the 20-F, Item 6.B.
  **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, RMB 8,379 million in the
  filed consolidated statement of cash flows (20-F, page F-8) against RMB 8,379 million in the XBRL `NetCashProvidedByUsedInOperatingActivities`
  fact for FY2025; agrees. Also 2017: RMB 2,452,596 thousand filed (FY2017 20-F) against 2,453 million in the FY2019 20-F; agrees.
- `python tools/run.py HTHT` **refused**: "NO ISSUING-AUTHORITY SOURCE configured for CNY" and "CURRENCY MISMATCH: earnings in CNY,
  quote in USD. Refusing to convert." (output saved in the research folder). By the brief, the figures are taken from the filed 20-Fs
  by hand (`_research 2026-10-14 HTHT/scripts/owner_cash.py`, every input a line of a filed cash-flow statement).
  **Owner cash after every real cost, RMB millions** (operating cash flow, less share-based compensation, less purchases of property
  and equipment and of intangibles, less finance-lease principal, less dividends to noncontrolling holders; rent is inside operating
  cash flow in every year, before and after the 2019 lease standard):

  | Year | OCF | SBC | capex | fin-lease principal | owner cash | pre-interest (net interest after 25% tax added back) | acquisitions paid | OC / revenue |
  |---|---|---|---|---|---|---|---|---|
  | 2015 | 1,763 | 53 | 649 | 0 | 1,056 | 1,039 | 19 | 17.3% |
  | 2016 | 2,066 | 55 | 517 | 0 | 1,490 | 1,446 | (132) | 22.4% |
  | 2017 | 2,453 | 66 | 828 | 0 | 1,556 | 1,612 | 3,746 | 18.9% |
  | 2018 | 3,049 | 83 | 1,119 | 0 | 1,842 | 1,910 | 496 | 18.3% |
  | 2019 | 3,293 | 110 | 1,532 | 0 | 1,646 | 1,836 | 244 | 14.7% |
  | 2020 | 609 | 122 | 1,773 | 23 | (1,313) | (1,045) | 5,060 | (12.9%) |
  | 2021 | 1,342 | 109 | 1,675 | 28 | (474) | (318) | 742 | (3.7%) |
  | 2022 | 1,564 | 87 | 1,053 | 40 | 378 | 505 | 57 | 2.7% |
  | 2023 | 7,674 | 143 | 901 | 82 | 6,546 | 6,557 | 0 | 29.9% |
  | 2024 | 7,518 | 322 | 898 | 65 | 6,229 | 6,196 | 0 | 26.1% |
  | 2025 | 8,379 | 420 | 838 | 57 | 7,060 | 7,020 | 0 | 27.9% |

  Five-year average (literal window 2021 to 2025): RMB 3,948 million (pre-interest 3,992). Depreciation and amortization 2025 RMB
  1,257 million against capex 838: spending ran below the depreciation charge in 2023 to 2025 (the depreciation variant of owner cash,
  2025: 6,641). Stock pay is resolved: it is the filed "Share-based compensation" line and it is deducted. Interest paid 2025: 169;
  interest income 223. The 25% rate on the interest add-back is a CONVENTION of this run (the PRC statutory rate, 20-F Item 5.A;
  rationale: the add-back needs a rate and the statutory one is the filer's own).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the buyer would be "happy buying this stock if the market closed for five years"
**[M1997-109]**, which for a Cayman holding company of a Chinese hotel franchisor turns on the cash its subsidiaries can send up
(the filer's own waterfall: 67.5% to 71.25% of PRC pre-tax earnings reaches the holding company as dividends, 20-F Item 5.B).
The margin asked rises as understanding falls and volatility rises, "the larger the margin of safety" **[M1997-080]**; and for a
business understood in a less familiar country the rows ask a lower price rather than a pass, "We wanted to get paid more for
going into China" **[M2006-021]**. No macro view enters, "macro conclusions are — just never enter into the discussion"
**[M2000-094]**: China's travel demand and the PRC policy climate are read only as properties of this business in its own filings.
Who is paid to tell you: the 2026 results releases carry raised revenue guidance and feature adjusted EBITDA; read as the
company's own selling, carried to Q4 and Q5. **Contrary evidence, written down as found** **[M1997-127]**: (1) same-hotel RevPAR
for legacy Huazhu fell year on year in seven of the eight quarters of 2024 and 2025, to (10.3)% in Q3 2024 and (8.3)% in Q1 2025,
and again (3.0)% in Q2 2026, the filer saying RevPAR was lower "primarily due to an increase in supply in 2025" (20-F Item 5.A);
(2) the filer sets room rates "primarily based on the location of a hotel, room rates charged by our competitors within the same
locality, and our relative brand and product strength" (20-F Item 5.A); (3) owner cash was negative in 2020 and 2021, and the
FY2021 20-F (Item 3.D) says hotel closures "may amount to an event of default under certain of our banking arrangements. We have
managed to obtain the required waiver"; (4) Atour, a rival the 20-F names, grew revenue from RMB 4,666 million to RMB 9,790
million between 2023 and 2025 (its own XBRL facts) while H World grew 16%; (5) the 2020 purchase of Deutsche Hospitality for
RMB 5,060 million cash has produced adjusted EBITDA summing to a loss of RMB 144 million over 2021 to 2025, a goodwill impairment
of RMB 437 million in 2020 and a brand impairment of RMB 391 million in 2024 (20-F Items 5.A and 5.E; FY2021 20-F); (6) options
were granted to the founder and the CEO on 2023-05-31 at US$2.8 per share, US$28 per ADS, when the ADS closed at US$36.62
(aggregator, flagged), a strike about 24% below the market (20-F Item 6.B); (7) H World runs part of its business through a VIE
structure (under 1% of revenue) and states that PRC regulatory developments may "expose us to government influence" (20-F Item
3.D summary). Each is weighed where its question falls.

## THE STANDING RULE
The buyer's conduct: the purchase is made from cash with no borrowed money, "borrowed money has no place in the investor's tool
kit" **[L2014-005]**, and in no form where "the other fellow can call your tune" **[M2006-079]**. Nothing in owning a listed ADS
puts the buyer at risk of ruin if it is so bought and sized; sizing is Q10's and is not reached unless Q7 passes **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five
  or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular business, and evaluating
  how predictable they were" **[M1998-044]**.
- **The business, from Item 4.B.** H World is a franchisor and operator of hotels: at 2025-12-31 it had 12,858 hotels, 573 leased
  and owned (4.5%) and 12,285 manachised and franchised, 1,264,419 rooms, in 1,222 cities, 12,736 of them in greater China (20-F
  Item 4.B). It earns (i) the whole revenue of the leased and owned hotels, against fixed rents (RMB 4,179 million of rent in 2025,
  16.5% of revenue) and (ii) fees from franchisees: an upfront fee of RMB 80,000 to RMB 1,000,000 per hotel, "a monthly franchise
  fee of approximately 3% to 6.5% of the gross revenues generated by each manachised hotel", reservation, membership, IT and
  hotel-manager fees; franchisees bear the building and operating costs, and H World states it does "not bear loss incurred by our
  franchisees" (Item 4.B). Revenue 2025: leased and owned RMB 12,943 million (51.1%), manachised and franchised RMB 11,696 million
  (46.2%), other RMB 668 million (Item 5.A). Two reported segments: legacy Huazhu and legacy DH (Europe), renamed HWC (China) and
  HWI (outside China) in the 2026 releases.
- **The key variables:** (1) the number of hotels in the system (openings less closures); (2) fees per hotel, which move with
  RevPAR because the fee is a share of hotel revenue; (3) the leased-and-owned book, shrinking by policy (691 to 573 hotels,
  2023 to 2025) and carrying fixed rents; (4) the cash the PRC subsidiaries can send up after PRC tax and withholding. All four are
  stated in the filings, and the first three are about customers and franchisees, not technology: the forecast is "what we think we
  can project out in terms of consumer behavior and threats to a business" **[M2023-030]**, the consumer kind of analysis
  **[M2017-019]**. Read through the COVID trough, the statements of 2015 to 2025 show the shape of future ones: fee revenue held
  (RMB 3,342 million in 2019, 3,136 in 2020, 4,404 in 2021) while the leased book swung to losses, so the statements are useful
  for "a judgment about what the future financial statements are going to look like" **[M2008-033]**.
- **What is hard.** The ten-year level of Chinese travel demand is not forecast (no macro, **[M2000-094]**). The foreign
  governance: a Cayman holding company, a founder with 23.5% (Item 6.E), PRC rules on cash leaving the country (RMB 4,269 million
  not distributable at 2025-12-31, Item 5.B), a VIE structure under 1% of revenue, the PCAOB and HFCA Act risk (Item 3). The rows
  ask that "we think we understand the nuances of the corporate governance system and taxation" **[M2000-141]**: the tax path is
  stated by the filer (25% PRC rate, 5% or 10% withholding, Item 5.B) and the governance is a disclosed structure, so the
  economics are understood and the jurisdiction asks a lower price, "We wanted to get paid more for going into China"
  **[M2006-021]**, not a pass. The doubt rule was put honestly: "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]**; the doubt here is about the size of a risk (government influence, cash repatriation),
  which Q9 weighs, not about what the business is or how it earns. Another analyst could close here on that row; that is recorded.
- **Routing:** not a fast-changing industry (no Q1 TOO HARD routing); not a bank; not a holding company of unlike parts (the
  parts are two hotel segments, read at Q2).
- **VERDICT: IN.** The economics (a fee on hotel revenue across a growing system, and a shrinking leased book) and the key
  variables can be stated and roughly foreseen ten years out **[M2000-037]**, **[M2012-065]**; filing facts: Item 4.B fee terms
  and network table, Item 5.A revenue by model, 2015 to 2025.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, and why these** (the brief's departure): from Item 4.B, the fee terms, the network table 2015 to 2025, H
Rewards and the direct-channel shares, and the Competition paragraph; from Item 3.D, the competition, franchisee-dispute and
supply risk factors; from Item 5.A, revenue by model, same-hotel RevPAR, the pricing sentence and the segment table. These are the
places where the filer itself says what keeps hotels and franchisees with it and what takes them away. Each test below cites them.

- **The parts table** (segments as reported; adjusted EBITDA is the filer's segment measure, read here only to rank the parts, not
  as earnings; FY2023 20-F for 2021 and 2022, FY2025 20-F for 2023 to 2025, `0001104659-26-048058`):

  | Part | Adjusted EBITDA 2021-2025, RMB m | Share | Castle | Decides |
  |---|---|---|---|---|
  | Legacy Huazhu (HWC and Asia) | 2,032 + 725 + 6,185 + 6,974 + 7,974 = 23,890 | over 100% | the franchise system (below) | **yes** |
  | Legacy DH (Europe) | (461) + (112) + 84 + (154) + 499 = (144) | below zero | leased hotels in Germany; no castle found: adjusted EBITDA negative in three of five years, brand impaired RMB 391 million in 2024 | no; carried to Q7 as an ordinary business at no growth |

  The file closes on legacy Huazhu **[L2008-005]**. Inside it, the filer reports revenue but not profit by model (leased and owned
  against manachised and franchised), so the two models cannot be ranked from the filing; they share the brands and the loyalty
  programme, and the castle is read for the system, with the leased book's fixed rents weighed at Q3 and Q9.
- **What the castle is, in the filer's words.** Scale (12,740 legacy Huazhu hotels, 1,239,397 rooms), brands across the segments,
  and the loyalty programme: "H Rewards covers all of our brands and had more than 311 million members as of December 31, 2025",
  "approximately 73% of our room nights under legacy Huazhu were sold to customers who were individual or corporate H Rewards
  members" and "approximately 77% of our room nights under legacy Huazhu were sold through our own sales channels" (Item 4.B). The
  franchisee buys that traffic; the 20-F calls it sharing "our vast customers base" (Item 4.B).
- **The money test** **[M2011-015]**, **[M2012-106]**. Could an attacker with money build a rival system? One did, in the
  upper-midscale band: Atour had 2,015 hotels and 224,423 rooms at 2025-12-31 and RMB 5,309 million of manachised-hotel revenue
  (Atour 20-F FY2025, `0001104659-26-044551`, Item 5), up from 1,210 hotels at 2023-12-31. But it grew beside H World, not by
  taking its hotels: H World's own system grew from 9,394 to 12,858 hotels in the same two years (Item 4.B). The 20-F names three
  large domestic chains (BTG, Jinjiang, Atour) and four international groups; "one competitor is frequently enough to ruin a
  business" **[M2012-108]**, and the evidence here is of a field of several large systems taking share from independents, "A
  significant majority of the room supply has come from independent hotels" (Item 4.B), rather than of one system taking another's.
- **Pricing power and the agony before a rise** **[M2005-020]**. Against: room rates are set "primarily based on the location of a
  hotel, room rates charged by our competitors within the same locality, and our relative brand and product strength" (Item 5.A),
  which is in part the gas-station case, "whatever he charged for gas was my price" **[M2012-109]**; legacy Huazhu's ADR fell from
  RMB 299 (2023) to 289 (2024) and 290 (2025); same-hotel RevPAR fell year on year in seven of the eight quarters of 2024 and 2025
  and was (3.0)% in Q2 2026. The franchise fee itself, the franchisor's own price, widened downward: "approximately 5% of the gross
  revenues" (FY2016 and FY2017 20-Fs), "approximately 4% to 6.5%" (FY2019), "approximately 3% to 6.5%" (FY2021 to FY2025). For:
  fee revenue per average manachised and franchised hotel rose from about RMB 0.59 million (2016) to 0.79 million (2019) and 1.03
  million (2025), arithmetic on Item 5.A revenue and the Item 4.B hotel counts, which includes hotel-manager fees and a richer brand
  mix; and blended HWC ADR rose 2.6% in Q2 2026 (6-K 2026-08-17). The field shows the same fall: Atour's same-hotel RevPAR fell
  from RMB 380.6 to 365.4 (2024 against 2023) and from 356.7 to 341.0 (2025 against 2024), on its own 20-F; by both filers'
  account it is supply in the field, not H World alone.
- **Unit volume and share of mind** **[M1997-099]**. Rooms in the system rose to 1,264,419 at 2025-12-31 from 912,444 at 2023-12-31
  (Item 5.A table); members from 150 million (2019, Item 4.A) to over 311 million (2025); 2,906 hotels in the pipeline and 2,200 to
  2,300 gross openings guided for 2026 (6-K 2026-08-17). Volume is the strongest evidence for the castle.
- **The low-cost position** **[M2018-043]**. The loyalty programme and own channels mean 77% of room nights pay no travel agent,
  against 23% through intermediaries (Item 4.B); one intermediary, Trip.com, is a principal shareholder and was paid RMB 307
  million of commissions in 2025 (Item 7.B). "the brand is our protection against the intermediaries making all the money"
  **[M2019-041]**: at 77% direct, the brand is doing that work today.
- **Would the customer choose it over the low bid; ask the competitors.** The traveller in economy and midscale China is
  price-aware, and the filer warns that guests may "choose to stay in other kinds of hotels, especially given the increase in our
  hotel room rates to keep pace with inflation" (Item 3.D). The franchisee is the second customer: some "were not satisfied with the
  performance of the hotel managers we appointed", some "complained that our loyalty program and other marketing efforts did not
  bring sufficient customers for their hotels" (Item 3.D), and Q2 2026 saw 157 manachised and franchised closures against 497
  openings in China (6-K 2026-08-17). Competitors' words about H World are not on the public record read; their filings were read
  for their numbers.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening in scale and direct share; narrowing at the bottom of the fee
  band and in same-hotel RevPAR. Through the COVID trough, the full downturn in the filings read, the fee business held:
  manachised and franchised revenue RMB 3,342 million (2019), 3,136 (2020), 4,404 (2021), 4,405 (2022), 7,694 (2023), and the system
  grew from 5,618 to 8,543 hotels (2019 to 2022), while the leased book carried the losses. That is a castle that stood through a
  downturn on the record, not a change for the better still awaiting one.
- **What could destroy, modify or reduce it** **[M2000-014]**. Supply growth that franchisees cannot fill (named by the filer for
  2024 and 2025); franchisees leaving at the end of eight-to-ten-year terms, the risk factor headed "We may have disputes with our
  franchisees, and they may terminate the franchise agreements with us earlier if the franchised hotels’ performance is worse than
  they expected" (Item 3.D); intermediaries; and the state (Item 3.D summary, "expose us to government influence").
- **The competitor row** (one metric from each filer's own cash-flow statement: owner cash = operating cash flow less stock pay
  less capital spending, over revenue, summed over each filer's span, which includes the COVID trough; Marriott's and Hilton's
  revenue lines include cost reimbursements, so their ratios read low against the Chinese filers and are compared on trend):

  | Company | Filing | Span | Owner cash / revenue, summed | Owner cash in 2020 |
  |---|---|---|---|---|
  | H World | 20-Fs FY2019 to FY2025 (accessions in Step 0) | 2019-2025 | 20,072 / 119,935 = 16.7% (2023-2025: 28.0%) | RMB (1,313) million |
  | Atour | 20-F FY2025 `0001104659-26-044551`, XBRL facts | 2020-2025 | about 20% (stock pay for 2020 and 2021 not tagged, not deducted) | about RMB 6 million |
  | Hilton | 10-K FY2025 `0001585689-26-000007`, XBRL facts | 2019-2025 | 8,300 / 61,768 = 13.4% | US$565 million |
  | Marriott | 10-K FY2025 `0001048286-26-000007`, XBRL facts | 2019-2025 | 11,446 / 141,172 = 8.1% | US$1,303 million |

  Named in the 20-F and not filing with the SEC: BTG Hotels, Jinjiang, Accor. InterContinental (IHG) files with the SEC but was not
  taken, the brief allowing three. Read: the asset-light franchisors stayed cash-positive through 2020; H World went negative
  because of its leased book, and since 2023 its owner cash margin is higher than any rival's on this measure. Atour's revenue is
  37.5% retail in 2025 (its 20-F), so its ratio is not a pure hotel figure.
- **The field's returns over the last full cycle** (CONVENTION of section C: "ordinary" judged in words). The field's durable
  players are franchisors with little capital of their own: H World's equity less goodwill and intangibles was RMB 2.5 billion at
  2025-12-31 against owner cash of RMB 7.1 billion that year, and Hilton and Marriott report negative equity. Across 2019 to 2025,
  the trough included, they earned well above ordinary returns on the capital they own, because the franchisees and the lessors put
  up the buildings. This is not the standing castle with ordinary returns.
- **VERDICT: IN, narrowly.** The castle is the franchise system of legacy Huazhu: the largest network in a fragmented field, a
  loyalty programme that sells three quarters of its room nights, and a fee business that held through the worst downturn in the
  record. The moat is judged, not measured, "You have to understand the businesses" **[M1999-108]**, and the reason it stands is
  stated and has lasted **[M1995-038]**. **The evidence against, carried and not explained away:** the franchisee's room price is
  set against the neighbours' **[M2012-109]**; same-hotel RevPAR has fallen for two years on supply; the bottom of the fee band fell
  from about 5% to 3%; and a rival built a large system in about a decade **[M2012-106]**. A moat "tenuous in any way" goes to TOO
  HARD **[M2000-019]**; this one is judged standing because the fee business held through 2020 to 2022 and kept growing, not
  because the room price is protected.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **The capital actually needed** **[M2010-090]**, read on tangible assets with goodwill set aside **[M2011-060]**: at 2025-12-31,
  property and equipment RMB 5,230 million, finance-lease right-of-use assets 2,394, land use rights 155, against working capital
  that is negative (deferred revenue 3,425, accrued expenses 4,902, salary payables 1,188 against receivables 723 and inventories
  57; 20-F balance sheet). Owner cash in 2025 was RMB 7,060 million: on the tangible operating assets of about RMB 7.8 billion, net
  of a negative working capital, the return is of the order of 90%, and the equity less goodwill and intangibles was RMB 2.5
  billion. The franchise model is the reason: "Our franchisees lease or own their hotel properties and are responsible for the
  costs of developing and operating the manachised or franchised hotels" (Item 4.B). That is close to "more and more money every
  year without putting up anything to get it, or very little" **[M1998-081]** for the fee business.
- **The capital that is not on the asset side.** The leased book needs capital in another form: operating-lease liabilities of RMB
  27,131 million (current 3,478, non-current 23,653) and rent of RMB 4,179 million a year (2025), for 573 hotels. The rent is a real
  cost inside owner cash; the liability is a fixed claim weighed at Q9.
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending was RMB 901, 898 and 838 million (2023 to 2025)
  against depreciation and amortization of 1,414, 1,332 and 1,257: below depreciation while the leased book shrinks (691 to 573
  hotels). The filer's own guess at growth spending: "approximately RMB693 million (US$99 million) of capital expenditures in
  connection with (i) certain recently completed leasehold improvements and installation of equipment and (ii) the funding of the
  leasehold improvements and installation of equipment of these 19 leased and owned hotels, which is expected to be incurred within
  one to two years" (Item 5.B). Maintenance guess, CONVENTION of this run: 2025 capital spending less half of RMB 693 million, about
  RMB 490 million (rationale: the filer gives the growth amount over one to two years and no split by year; half is the middle).
  The system's growth is paid for by franchisees: 3,582 net manachised and franchised additions in 2024 and 2025 with capital
  spending below depreciation.
- **What the added capital earned** **[M2001-019]**. From 2019 to 2025 owner cash rose from RMB 1,646 million to 7,060 million. The
  capital put in over the span was the acquisitions, RMB 6,103 million (Deutsche Hospitality RMB 5,060 million in 2020, RMB 742 million in
  2021, the year CitiGO was bought), and no net capital spending above depreciation (capex 2020 to 2025 RMB 7,138 million against depreciation of
  8,324). The rise came from legacy Huazhu's franchise growth; the largest purchase, Deutsche Hospitality, has returned adjusted
  EBITDA summing to a loss over 2021 to 2025 (parts table, Q2). The incremental return on the organic capital is very high; on the
  acquired capital it is at or below zero.
- **The growth arithmetic and its caps** **[M1999-067]**. The highest share of revenue earned as owner cash in the filings read is
  29.9% (2023); revenue grew 7.5% a year from 2023 to 2025 and legacy Huazhu revenue 10.6% a year from 2019 to 2025. Q7 carries no
  growth after year ten and checks every growth case against the 29.9% share of revenue.
- **WEIGHS FOR**, one sentence: the fee business needs almost no capital of its own and grows on franchisees' money, the "best
  business" end of **[M1998-081]**, while the capital H World did put in, chiefly Deutsche Hospitality, earned little or nothing,
  which is carried to Q6 as the record of the allocator **[L2009-012]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (RMB millions; 20-Fs FY2017, FY2019, FY2021, FY2023, FY2025, each
  year from the later filing that carries it; 2016 and 2017 filed in thousands and rounded; "cash" is cash, restricted cash and
  short-term investments; leases from 2019 under the new standard):

  | Dec 31 | Cash | Receivables | PP&E | Goodwill | Intangibles | Total assets | Debt | Op. lease liab. | Fin. lease liab. | Total equity | Retained earnings | Revenue (year) |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | 2016 | 3,236 | 142 | 3,710 | 172 | 343 | 9,993 | 298 | n/a | n/a | 5,416 | 1,812 | 6,655 |
  | 2017 | 4,086 | 163 | 4,523 | 2,265 | 1,644 | 17,427 | 5,053 | n/a | n/a | 6,474 | 2,754 | 8,229 |
  | 2018 | 4,973 | 195 | 5,018 | 2,630 | 1,834 | 23,993 | 9,760 | n/a | n/a | 6,319 | 2,610 | 10,063 |
  | 2019 | 16,907 | 218 | 5,854 | 2,657 | 1,662 | 52,983 | 16,583 | 21,578 | n/a | 7,500 | 3,701 | 11,212 |
  | 2020 | 10,993 | 404 | 6,682 | 4,988 | 5,945 | 65,155 | 11,998 | 30,454 | 2,528 | 11,432 | 1,502 | 10,196 |
  | 2021 | 7,730 | 521 | 7,056 | 5,132 | 5,385 | 63,269 | 9,797 | 31,640 | 2,725 | 11,044 | 1,037 | 12,785 |
  | 2022 | 6,874 | 1,113 | 6,784 | 5,195 | 5,278 | 61,507 | 9,923 | 31,410 | 2,554 | 8,803 | (1,200) | 13,862 |
  | 2023 | 9,899 | 755 | 6,097 | 5,318 | 5,280 | 63,532 | 5,314 | 27,824 | 2,742 | 12,249 | 794 | 21,882 |
  | 2024 | 11,127 | 817 | 5,682 | 5,221 | 4,776 | 62,552 | 5,426 | 27,126 | 2,893 | 12,271 | 2,449 | 23,891 |
  | 2025 | 15,426 | 723 | 5,230 | 5,428 | 5,028 | 64,774 | 5,816 | 27,131 | 3,122 | 12,958 | 3,614 | 25,307 |
  | Jun 2026 | 15,706 | 839 | 4,989 | 5,291 | 4,821 | 63,615 | 4,226 | 27,015 | 2,993 | 14,235 | 3,133 | (H1 13,117) |

  What moved and why. **Goodwill and intangibles** rose from RMB 0.5 billion (2016) to 10.5 billion (2025) on the purchases of
  Crystal Orange (2017), Blossom (2018) and Deutsche Hospitality (2020), and now exceed four fifths of equity: tangible equity was
  RMB 2.5 billion at 2025-12-31. **Debt** rose to RMB 16.6 billion at 2019-12-31 (the year-end cash of 16.9 billion included RMB
  10,765 million of restricted cash, paid out on 2020-01-02 for Deutsche Hospitality) and has been paid down to 5.8 billion
  (2025) and 4.2 billion (June 2026, after the 2026 convertible notes converted into shares); a CNY 3.35 billion bond due 2031 was
  added in September 2026 (6-K 2026-09-16). **Cash** reached RMB 15.4 billion; RMB 1,406 million of it was pledged against the
  RMB 1,400 million loan (Item 5.A), and RMB 4,269 million of PRC net assets could not be paid up as dividends (Item 5.B), so not
  all the cash is free; the rows' point that trapped cash is worth less, "off-shore cash is simply not worth as much as cash held at
  home" **[L2016-009]**, applies here to PRC cash held for a Cayman parent. **Receivables** fell from RMB 1,113 million (2022) to 723 million
  (2025) as revenue rose 83%; inventories are RMB 57 million; no prepaid or deferred asset is building **[M1995-064]**. **Deferred
  revenue** (membership fees and upfront franchise fees) rose from RMB 0.9 billion (2016) to 3.4 billion (2025): customers' and
  franchisees' money held in advance. **Retained earnings** went negative in 2022 after the COVID losses and recovered as dividends
  of RMB 3.5 to 3.9 billion a year were paid out of earnings; treasury shares are cancelled against paid-in capital. **What the
  figures cannot say:** the operating-lease liabilities of RMB 27.1 billion are fixed rent claims that are not debt in net debt but
  were the cause of the 2020 to 2021 cash losses; the balance sheet cannot show franchisee economics, which carry the system.
- **The real costs.** Depreciation (RMB 1,257 million in 2025) is above capital spending (838) while the leased book shrinks;
  owner cash deducts the cash spent, not the charge. **Stock pay** rose from RMB 143 million (2023) to 322 (2024) and 420 (2025),
  which the filer attributes in 2024 to "an increase in share-based compensation to attract and retain core employees" (Item 5.A);
  it is deducted. **The recurring one-time:** impairment losses of RMB 709, 380, 491, 516, 537 and 242 million (2020 to 2025),
  mostly on leased hotels "due to the sequential underperformance relative to the projected operating results" (Note 2): non-cash,
  and the cash was the earlier capital spending already charged in those years' owner cash; restructuring at legacy DH in 2024
  (Item 5.A); none is added back here **[L2016-007]**. Foreign-exchange gains and losses on internal euro loans (a gain of RMB 569
  million in 2025, a loss of 272 million in 2024) are not cash and are outside operating cash flow.
- **EBITDA in the filer's own mouth.** Adjusted EBITDA is the segment profit measure and the second headline of every results
  release; it excludes "share-based compensation expenses" among other items (Item 5.A reconciliation), the cost the rows call "the
  most egregious example" **[L2015-003]**, and EBITDA itself is "utter nonsense" in the rows **[M1998-086]**. The 20-F reconciles it
  to GAAP net income line by line and gives GAAP first in Item 5.A; the 2026 releases give GAAP net income, EBITDA and adjusted
  EBITDA in the same bullets. A featured adjusted figure is "a management that regularly attempts to wave away very real costs"
  **[L2016-006]**: recorded as a WEIGHING against and carried to Q5. **Guidance:** "We have raised our guidance for the full year of
  2026, expecting Group revenue growth to be in the range of 4%-8%" (6-K 2026-08-17), revenue guidance, not earnings guidance, and
  a gross-opening target of 2,200 to 2,300 hotels; carried to Q5 as the habit **[L2019-006]** names.
- **What the accounts say of management.** The statements are clear and complete: cash flows reconcile, the VIE share is stated
  (under 1%), the tax waterfall is illustrated, the share count in the equity statement agrees with the cover, "we were not required
  to prepare an accounting restatement" (Item 6, clawback). No confusing item was found; the one item that needed the earlier
  filings, the 2019 restricted cash, is explained in them.
- **VERDICT on the accounts: no STOP; WEIGHS AGAINST** on the featured adjusted EBITDA and the revenue guidance, both carried to Q5
  **[M1994-018]**. The recast earnings for Q7 are the owner-cash series in Step 0, after stock pay, all capital spending,
  finance-lease principal and minority dividends.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Qi Ji, founder (2005), executive chairman since 2009 and chief executive in three spells, beneficially 23.5% through
  the Ji Family Trust's Winner Crown and his own shares (Item 6.E); he co-founded Home Inns and Trip.com. Hui Jin, chief executive
  since September 2021, with the company since 2005 (development director, vice president, president). Arthur Yu, chief financial
  officer since March 2026, from Baozun and Jaguar Land Rover. A company of this kind needs management in place, and it has it.
- **The first yardstick, the record against the hand dealt** **[M1994-008]**. The system grew from 2,763 hotels (2015) to 12,858
  (2025) while the leased share fell from 22% to 4.5% of hotels (Item 4.B table); through COVID the system kept growing and the
  fee business held (Q2), and the company kept its lenders by waiver; debt is down from RMB 16.6 billion (2019) to 4.2 billion (June
  2026) and cash is up. Against: the Deutsche Hospitality purchase (RMB 5,060 million, 2020), whose adjusted EBITDA sums to a loss
  over five years, with goodwill and brand impairments of RMB 437 and 391 million; and owner cash per share has risen less than
  owner cash, because shares outstanding went from 3,112 million (2022) to 3,154 million (June 2026) after the 2023 offering and
  the 2026 conversion. Competitors: Atour has grown faster from a smaller base in a higher band (Q2).
- **The second yardstick, how they treat the owners** **[M1994-009]**, read in the 20-F (the proxy furnished on 6-K carries no
  pay table). Aggregate cash pay to all directors and officers RMB 28 million in 2025 (Item 6.B), modest for the size. But: on
  2023-05-31 the founder and the chief executive were granted 7,240,910 and 7,913,300 options at US$2.8 a share, US$28 an ADS,
  when the ADS closed at US$36.62 that day (aggregator, flagged), a strike about 24% below the market; the founder received
  28,963,620 restricted shares on 2024-01-17 (ADS close US$30.93, about US$90 million of value at grant, arithmetic); the share
  plan's administration committee for grants below the board is "currently comprised solely of Mr. Qi Ji" (Item 6.B). Weighed at Q6
  Part B as pay; read here for what it says of the treatment of owners: they "have gotten rich with their shareholders and not off
  their shareholders" **[M2003-055]** is not what a below-market strike shows.
- **The habits carried from Q4.** Revenue and opening guidance, raised in August 2026; adjusted EBITDA, which leaves out stock pay,
  featured in every release. Read with the rest of the record: the 20-F puts GAAP first and reconciles every adjusted line; it says
  plainly that "we have experienced data incidents from time to time" (Item 3.D) and that its RevPAR fell on supply; no restatement
  (Item 6, clawback note), controls concluded effective (Item 15), no change of auditor (Item 16F), and pending proceedings are
  lease, franchise and labor disputes with RMB 16 million accrued (Item 4.B, Legal and Administrative Proceedings). The
  guidance is of revenue and openings, not of earnings per share; no instance was found in the filings read of a pattern of
  beating declared targets (the 2025 guidance against its outcome was not read, which is recorded as not done).
- **How they talk about mistakes** **[L2024-003]**. No admission of a mistake about Deutsche Hospitality was found in the 20-F's
  Items 4 and 5 or the 2026 releases read (a text search of the FY2025 20-F for "mistake", "lesson", "regret" and "we were wrong"
  found none); its losses are described as restructuring costs, headcount and impairments. The releases' language ("brand-led
  high-quality hotel network expansion") reads as written for investor relations **[M2007-083]**.
- **Love of the business.** The founder has built hotel and travel companies for 25 years and holds 23.5% of this one, not sold
  down in the filings read; the chief executive has spent his career inside it. That reads as love of the business **[M2000-098]**,
  with the grants above as the counterweight.
- **VERDICT on integrity: IN.** No dishonesty was found: the accounts are complete and plain, the bad news (RevPAR, data incidents,
  impairments) is in the filing, and the habits from Q4 are disclosed, reconciled and of revenue rather than earnings. Applied on
  doubt alone, "If you’ve got doubts, forget it." **[M2013-088]**: the doubt raised here is about pay, how insiders treat
  themselves, which the rows weigh as owner treatment and Q6 carries, not about whether the figures or statements can be trusted;
  "trustworthiness is more important than the brains" **[M2015-047]** is not contradicted by a fact found. **Ability WEIGHS FOR**:
  the record against the hand dealt is strong in the business that decides, with the Deutsche Hospitality purchase as the large
  error and the per-share record diluted, both carried to Q6.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. Over 2016 to 2025 net income attributable to the company summed to about
  RMB 12.3 billion (20-Fs), and the company paid out more than that: dividends RMB 9.7 billion and repurchases RMB 3.8 billion
  (including the RMB 710 million prepaid put of 2024), RMB 13.6 billion in all (cash-flow statements). It also raised equity: Accor
  China paid in shares in 2016 (RMB 1,144 million, non-cash), the Hong Kong offering of 2020 (RMB 6,018 million) and the 2023
  follow-on at US$42.0 per ADS (RMB 1,973 million); and in 2026 the convertible notes turned into 133,496,890 shares (RMB 3,428
  million). The money kept and raised went chiefly into Crystal Orange (RMB 3,746 million, 2017), Deutsche Hospitality (RMB 5,060
  million, 2020) and the 2020 to 2022 losses. The one large retained-dollar test that can be read, Deutsche Hospitality, failed:
  value given RMB 5,060 million in cash, value got a segment whose adjusted EBITDA sums to a loss over 2021 to 2025, "If we give 200
  million of cash for a business that’s worth a 150 million, we are worse off" **[M1995-001]**. Since 2023 almost nothing is
  retained: the dividend policy was "no less than 60% of our net income" (Item 5.B), replaced on 2026-08-17 by a three-year
  "shareholder return plan in the aggregate amount of US$2.5 billion" of dividends or ADS repurchases at the board's discretion
  (6-K 2026-08-17). For a business that needs little capital, paying out is the right default; a payout set as a share of earnings
  is the ratio of which the rows say it "strikes us as nuts" **[M2000-051]**, but it is now a sum, not a ratio.
- **Buybacks** **[L1999-023]**, **[L2016-002]**. The programmes name no price: "at prevailing market prices or privately negotiated
  transaction" (US$750 million, 2019 to 2024) and "through open market transactions at prevailing market prices" (US$1,000
  million from 2024-08-21, five years; Item 16E). Prices paid: US$32.00 per ADS (January 2025, 1,874,950 ADS), US$32.96 (April),
  US$36.60 (September), US$37.72 (October 2025, 1,261,664 ADS) (Item 16E); RMB 1,857 million for 61,598,060 shares in the first
  half of 2026 (interim report, statement of changes in equity), RMB 30.15 a share, about US$44.4 per ADS at the period's 6.7851.
  The 2026 purchases followed by weeks the conversion of the 2026 notes at US$41.72 per ADS: shares issued at US$41.72 and bought
  back at about US$44, "they sell low and then they buy high" **[M1998-027]**; and the net share count rose from 3,112 million
  (2022) to 3,154 million (June 2026) despite about RMB 5.7 billion of repurchases from 2022 to June 2026, so the buying has mostly absorbed
  issuance, which "has nothing to do with preventing dilution" in the rows' test **[M2016-049]**.
  **The test against the bottom of the Q7 range** (written back from Q7 and committed with it): the bottom of the central range is
  US$37.59 per ADS. The 2025 purchases, at US$32.00 to 37.72 (RMB 783 million), sat at or below it; the first-half 2026 purchases,
  about US$44.4 per ADS (RMB 1,857 million, the largest), sat above it. Read by what they did, the larger part of the buying was above
  the bottom of the range, so the programme with no stated price weighs against, as the rule sets it **[L2016-002]**.
- **Issuance and deals.** The deals in the window were paid in cash (Deutsche Hospitality 2020, CitiGO 2021), so the one STOP of
  Part A, an all-stock deal in undervalued stock **[L2009-019]**, does not arise for them. The Accor China deal of 2016 was paid in
  shares (FY2017 20-F, non-cash disclosure), a merger by the speakers' usage; whether the stock then sat below its value was not
  computed (it lies outside every window used here), recorded and not applied. Serial issuance (2017 and 2020 convertibles, 2020
  Hong Kong offering, 2023 follow-on) is carried, as the framework carries it, as a candidate concern and not a STOP.
- **Part A WEIGHS AGAINST**: the free cash is now paid out, which is right for this business, but the money the company kept and
  raised in the decade went mostly into a purchase that returned nothing, and the buybacks name no price and were largest above
  the bottom of the Q7 range (below).

**Part B, the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: the 20-F gives aggregate cash pay (RMB 28 million for all directors and
  officers, 2025) and no performance metric for it; hotel managers' pay is "directly linked to its performance against the annual
  budget" (Item 4.B). **Options and their strike:** the 2023 options of the founder and the chief executive were struck at US$2.8 a
  share when the share traded at about US$3.66 (US$36.62 per ADS, aggregator), and "They should not be granted at below the
  intrinsic value of the company" **[M2002-071]**; the founder's 28,963,620 restricted shares of January 2024 carry no stated
  performance condition for him in the table (the footnote's performance conditions are attached to the chief executive's and the
  group's awards). Stock pay tripled from RMB 143 million (2023) to 420 million (2025).
- **Who designs the plan** **[M1997-041]**: the compensation committee is the co-founder John Jiong Wu and Lei Cao; the delegated
  administration committee, empowered to grant up to 5,000,000 shares a year under the 2023 plan "to any of our directors, senior
  management, employees and consultants", is "currently comprised solely of Mr. Qi Ji" (Item 6.B).
- **The board.** Seven directors: the founder as executive chairman, an executive director, a former fund manager (called an executive
  director in his biography and a director in the table), and four independents including the co-founder; no nominations committee, by home-country practice (Item
  6.C). The chairman is not the chief executive, which avoids the case "how hard it is to replace a mediocre CEO if that person is
  also Chairman" **[L2014-026]**, but the founder controls 23.5% of the votes. Related-party dealings with Trip.com, a principal
  shareholder co-founded by the chairman: commissions RMB 307 million, rent RMB 19 million, technical services sold RMB 116 million
  (Item 7.B).
- **Part B WEIGHS AGAINST**: modest cash pay, but options struck below the market, a large founder grant and a grant committee of
  one, the founder, are how insiders treat themselves rather than the owners **[M1994-009]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, at the
long government rate, here the RMB 30-year at 2.06% (Step 0) **[L2000-021]**, with no risk premium in the rate **[M1996-025]**.
All arithmetic is in `_research 2026-10-14 HTHT/scripts/q7.py`; every input is a filed line (Step 0 table).

- **The window and the cycle, specific (a)** **[L2005-003]**. The literal five-year window is 2021 to 2025. Its first year is
  aberrational on the filer's own description: "Due to the global outbreak of COVID-19, our business was significantly impacted and
  we experienced operating losses in 2021 and 2022" (FY2023 20-F, Item 3.D). So the base is the average over the last full cycle,
  peak to peak, on the owner-cash series: peaks in 2018 (RMB 1,842 million) and 2023 (6,546), trough in 2020 (1,313 negative).
  CONVENTION of this run: the cycle's years are 2019 to 2023, the year after one peak through the next (rationale: one full turn,
  each peak counted once; 2018 to 2023 is shown beside). Cycle average, pre-interest owner cash: **RMB 1,507 million** (equity-only
  1,357; with 2018 included, 1,574). Growth "between the averages of successive cycles" cannot be measured: the filings read
  (2015 to 2025) hold no earlier full cycle, owner cash having risen from 2015 to 2018 with no trough. That is said, and the growth
  case is built as below.
- **Acquisitions, specific (c), and the serial-acquirer rule.** Cash paid for businesses in the cycle window was RMB 6,103 million
  (Deutsche Hospitality 5,060 in 2020; 742 in 2021; 244 in 2019; 57 in 2022) against owner cash before purchases of RMB 7,535
  million over the same years: more than half, so the central figure is the **organic pair** (purchases left out, organic growth
  as the filer reports it), with the default pair beside. The rule is triggered here by one large deal rather than by a habit,
  and is applied as written. The filer reports organic growth only as segment revenue: legacy Huazhu, which in 2019 was the whole
  group, grew revenue from RMB 11,212 million (2019) to RMB 20,535 million (2025), **10.61% a year**; CONVENTION of this run, that
  rate is carried as the organic growth of owner cash (rationale: it is the only organic growth figure the filer reports, and it
  is lower than the rise of owner cash from the cycle average to 2025, so it does not flatter the case). **Cap (f):** at that rate, owner cash in year ten
  is RMB 4,132 million against revenue of RMB 56,301 million at the same rate, 7.3% of revenue, below the 29.9% high (2023): no cut.
  No growth after year ten; zero nominal growth then (the PG specific).
- **Working capital, (d):** inside operating cash flow, counted. **Maintenance, (e):** the filer states a growth-spending figure only
  for 2025 to 2026 (RMB 693 million over one to two years, Item 5.B), not for the cycle years, so the all-spending case is central
  and the maintenance variant is shown with the sensitivity below. **Decline, (b):** not shown on the cycle base. **Whose tax:** owner
  cash is after the company's own tax, PRC withholding on internal dividends included (income taxes paid RMB 1,632 million, 2025).
  Two subsidiaries' 15% high-tech rates (an aggregate tax holiday of RMB 60, 47 and 98 million in 2023 to 2025, Item 5.D) end in
  2026 and 2027 unless renewed; computed at the statutory rate with the shelter's present value added, the base moves by under RMB
  60 million a year and the whole-business value by under 1%: no figure below changes at the precision shown. **Legacy DH** is
  inside the consolidated owner cash and carried at the group's rate; with its five-year adjusted EBITDA below zero, carrying it at
  no growth instead lowers the figures slightly.
- **Net debt, all-equity basis** **[L2017-004]**, at the latest filed balance sheet (2026-06-30, 6-K of 2026-08-17): borrowings RMB
  4,226 million (911 short, 3,315 long) plus finance-lease liabilities 2,993, less cash 14,249, restricted cash 142 and short-term
  investments 1,315: **net cash RMB 8,487 million**; the subsequent event that filing states, the US$275 million dividend declared
  2026-08-17 and paid in September (RMB 1,866 million at the filing's 6.7851), reduces it to **net cash RMB 6,621 million**. The
  CNY 3.35 billion bond of September 2026 adds equal cash and debt, no change. Operating-lease liabilities (RMB 27,015 million at
  2026-06-30) are left out of net debt, said so; their rent is inside owner cash. Long-term investments (RMB 1,352 million, equity
  stakes) are not counted as cash. Market value RMB 93,756 million; **enterprise value RMB 87,135 million**.

- **The floor, tested first** (CONVENTION, about 10% pre-tax as Q7 states it, after the company's own tax, "there’s just a point
  at which we drop out of the game" **[M2003-149]**). Each case valued at 10% against the enterprise value of RMB 87,135 million:

  | Case | Base, RMB m | Growth, years 1-10 | Worth at 10% (RMB m) | Earns the floor at the price? | Return at the price |
  |---|---|---|---|---|---|
  | Central, organic pair, no growth | 1,507 | 0 | 15,070 | no | |
  | Central, organic pair, growth | 1,507 | 10.61% | 31,470 | **no** | 4.2% |
  | Default pair (purchases deducted, base 286; growth not measurable) | 286 | 0 | 2,865 | no | |
  | Literal window 2021-2025, beside (sign change, halves meaningless, so no-growth alone, by (b)) | 3,992 | 0 | 39,919 | no | 4.6% |

  **No case of the range earns the floor at the price: the file closes OUT here, whatever the width.**
- **The value range, central (organic pair, at 2.06%):** whole business RMB 73,158 to 187,670 million; less net debt (net cash
  added), **RMB 25.29 to 61.60 per ordinary share, US$3.759 to 9.153 per ordinary share, US$37.59 to 91.53 per ADS**, against
  US$44.17. Width 2.4 to 1 per share (below three to one). The price sits inside the range: on the width test too this is not a
  screamer, "it’s too close to think about" **[M1996-084]**. Literal window beside: a single no-growth value of US$94.41 per ADS at
  2.06%, which does not earn the floor at the price (4.6%).
- **Sensitivity, COMPUTATION, NOT A CLEARANCE, and not a case of the range** (shown because it is the most generous reading an
  analyst could put forward, and the evidence against the OUT must be written down **[M1997-127]**): on the post-COVID years alone
  (2023 to 2025, pre-interest owner cash 6,591, growth 3.46% a year from 2023 to 2025), the expected return at the price is 9.6%; with
  the filer's growth spending added back (about RMB 347 million a year, half of RMB 693 million), 10.1%. Even the reading that sets
  aside the cycle rule clears the floor by a tenth of a point, which is the case of "the discount rate is 9.6 percent instead of 9.8
  percent — forget about the whole exercise" **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end of the central range valued at 10% and the two averaged,
  after the company's own tax. **All-equity basis (central): US$14.08 per ADS, US$1.408 per ordinary share** (RMB 9.48 per ordinary
  share; whole business RMB 23,270 million plus net cash 6,621). **Equity-only beside: US$9.87 per ADS, US$0.987 per ordinary
  share** (owner cash after interest, base 1,357). The central figure is positive, so the alert can sit on it. No cheap price is
  reported.
- **VERDICT: OUT.** Valued, and no case earns the floor at US$44.17 **[M2003-149]**; the price is inside a range of under three to
  one, not "startlingly low in relation to value" **[L2000-025]**; and the one reading that reaches the floor needs a calculator to
  find it **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. Inaction is the default the draft gives a file closed at Q7.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor of about ten percent at US$44.17 per ADS (central growth case 4.2% at the
price); central value range US$37.59 to 91.53 per ADS (US$3.759 to 9.153 per ordinary share) at the 2.06% RMB 30-year, the price
inside it; fair price US$14.08 per ADS all-equity (US$9.87 equity-only). Q1 IN, Q2 IN narrowly, Q3 for, Q4 no STOP and against,
Q5 integrity IN and ability for, Q6 against on both parts.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond and the alternatives).** The RMB 30-year was 2.06% on 2026-10-14 (Step 0). Owner cash before interest on the
  enterprise value of RMB 87,135 million: 1.7% on the cycle average (1,507), 4.6% on the literal five-year average (3,992), 8.1% on
  2025 alone (7,020). The company's own repurchases in 2026 were made at about US$44.4 per ADS (Q6).
- **Q9 (debt and exposures).** Borrowings RMB 4,226 million at 2026-06-30, plus the CNY 3,350 million 2.25% bonds due 2031 issued in
  September 2026 (6-K 2026-09-16, `0001104659-26-108062`); finance-lease liabilities RMB 2,993 million; cash, restricted cash and
  short-term investments RMB 15,706 million, of which RMB 1,406 million was pledged against a RMB 1,400 million one-year loan at
  2025-12-31 (20-F Item 5.A). Operating-lease liabilities RMB 27,015 million; rent RMB 4,179 million in 2025 (16.5% of revenue);
  584 leases, 68 of them expiring in 2026 (Item 4.B). In 2020 to 2021 hotel closures "may amount to an event of default under
  certain of our banking arrangements. We have managed to obtain the required waiver" (FY2021 20-F, Item 3.D): the one time the
  lenders could have called the tune, they were asked and agreed. A RMB 400 million syndicated loan carries "financial covenants
  including revenue and profit related to this facility" (Item 5.A). In 2026 the group undertook, with another shareholder of Azure
  Capital, to "provide funding support" for a repurchase of the units of a REIT of about RMB 1,239 million if the originator is
  found to have committed material violations in the issuance documents (interim report 6-K 2026-09-23, related-party note). The
  holding company depends on PRC subsidiaries' dividends; RMB 4,269 million of PRC net assets were not distributable (Item 5.B);
  the PCAOB inspection and HFCA Act risk and the PRC regulators' "authority to exert influence" are stated in Item 3.D.
- **Q12 (how the money is made).** Hotels under the group's brands; none of the businesses the rows name (casinos, tobacco,
  distributor-loading schemes, gambling dressed as investing, promotion on a borrowed reputation) was found in Item 4.B.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Declared: the
      first commit (the copy, the position note and the contamination line) was made after `tools/run.py` and
      `Screens/cover_shares.py` had run and the first filings had been fetched; the copy itself was made before any fetch. Step 0 was
      committed with Q1, and the Q6 buyback line with Q7, as the brief asks.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and named the dispatching session as holder of the
      lock; I did not write or check the lock. The run binds only once folded into the register.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Breach, declared:** to check that this
      run's file name was free I ran a listing of `Test Runs/` filtered to the date 2026-10-14, which showed the names of other runs
      of that date (CHH, H, HGV, HLT, MAR, WH and four steel names) and their research folders; none was opened or searched, and
      nothing from them is used. The commit subjects of the H (Hyatt) run seen in the session context are declared under
      contamination at the top. Marriott's and Hilton's figures were taken from their own 10-K XBRL facts on EDGAR.
- [x] Every v5 id resolves (`_research 2026-10-14 HTHT/scripts/check_cites.py`: no E-ids, every M, L and R id found in
      `principle_ledger_v5.csv`, every attached quoted fragment found in its row); every filing fact has its accession; the
      numbers without a row are filed figures or are labelled CONVENTION of this run (the 25% interest add-back rate, the euro
      earnings carried in RMB, the maintenance guess, the cycle years, segment revenue growth as organic growth).
- [x] The order was kept; Q7, the first STOP that failed, closed the run; the sensitivity under Q7 is headed COMPUTATION, NOT A
      CLEARANCE and is not a case of the range.
- [x] Owner cash after every real cost, from operating cash flow less stock pay, all capital spending, finance-lease principal
      and minority dividends, never a net-income proxy; the sovereign from the Ministry of Finance's curve as published through
      ChinaBond, its compiler, because the MOF's own page failed (Step 0); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found (foundations, Q2, Q7 sensitivity); facts for later questions are under
      AFTER THE STOP. Q5 was reached and answered, so no integrity flag is owed in the box line.
- [x] Not a point-in-time run; no anchor-date restriction applies.
- [x] `tools/run.py` refused the name (no RMB source, currency mismatch); none of its output was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (run 2026-10-14, all checks PASS).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **Specific (a) with one cycle.** The window's first year is aberrational (COVID), so the base is a cycle average,
but the filings hold only one full cycle, so "the growth is measured between the averages of successive cycles" cannot be done,
and the text gives no fallback for that case; I built the growth case on the organic rate (the serial-acquirer rule required the
organic pair anyway) and said so. The cycle average also mixes a business a third of today's size (2019) with today's, after a
structural shift to franchising and a doubling of revenue; the text has no way to scale a cycle base for such a change, and the
choice swings the fair price from US$14 (cycle) to about US$38 (post-COVID sensitivity), though not the box, since every rule case
and the literal window fail the floor. (2) **"Peak to peak"** does not say whether both peak years are in the average; I used the
years after one peak through the next and showed the other reading. (3) **The serial-acquirer rule** is named for a habit but is
triggered by a single deal (Deutsche Hospitality was 83% of the window's purchases); I applied it as written. (4) **The sovereign
table and `tools/sources.py` have no RMB source**, the Ministry of Finance's own curve page was dead, and the curve was taken from
ChinaBond's MOF page; a RMB row in the protocol's table would fix the source for the next Chinese filer. At 2.06%, the range at the
sovereign sits far above every case valued at the floor, so for low-rate currencies the width test and the floor test point in
different directions; the floor-first rule decided it, as written. (5) **`tools/run.py` cannot take an ADS quoted in US dollars
for an RMB earner** (it refuses to convert and the home line is in HKD); all arithmetic was done by hand from the filings, which
the brief anticipated.
