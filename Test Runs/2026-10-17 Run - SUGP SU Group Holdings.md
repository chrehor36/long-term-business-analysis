# Company Run — SU Group Holdings Limited (Nasdaq: SUGP) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template before any fetch, 2026-10-17. A dispatched blind run; working folder `Test Runs/_research 2026-10-17 SUGP/`, raw filings in its gitignored `cache/`; arithmetic in `calc.py`, citation check in `check_cites.py`.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (2026-10-17): not held (`PORTFOLIO.md` does not name SUGP).*

**CONTAMINATION, declared:** before any work, the session's start-up context showed the subjects of the five latest commits
in the repository, all about another company's run (KAZR): a box (OUT at Q1), a COMPUTATION range ("nil to nil, fair price
nil against $1.96") and an HKD sovereign figure (4.519%). Not used: the sovereign below was fetched independently from the
HKSAR Government's own file and happens to be the same closing yield of the same day for the same bond. The start-up context
also showed the memory index (lines about the queue's state and counts of gate-clearers; nothing about this name) and file
names of other runs' research folders (AYI, ARCB) in the git status. None of the blind-listed files was opened, listed or
searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** US$1.76 (close 2026-10-16; the aggregator quote printed by `tools/run.py`, flagged per operator rule 5: a
  live quote only). The quote is after the 1-for-6 consolidation of 2026-10-07.
- **Shares by class.** `python Screens/cover_shares.py SUGP` prints 1,464,772 from the cover of the 20-F filed 2026-01-16
  (accession `0001753926-26-000125`): that is 563,092 Class A plus 901,680 Class B as of the 20-F's date (Item 7 table:
  "563,092 Class A ordinary shares and 901,680 Class B ordinary shares outstanding"), on the basis before three later
  changes. The count is stale and was rebuilt by hand from the later filings:
  | date | event (filing) | Class A | Class B |
  |---|---|---|---|
  | 2025-09-30 | 20-F balance sheet (`0001753926-26-000125`) | 563,092 | 901,680 |
  | 2026-05-13 | 3,000,000 units at US$2.00, each a pre-funded warrant and two warrants at US$5.50 (6-K `0001753926-26-000859`) | | |
  | 2026-06-12 | F-1 cover count, the pre-funded warrants exercised (F-1 `0001753926-26-001005`) | 3,563,092 | 901,680 |
  | 2026-06-17 | warrant exercise price cut US$5.50 to US$0.87 (6-K `0001753926-26-001019`) | | |
  | 2026-08-04 | "approximately 7,124,092" before a 1-for-5 consolidation effective 2026-08-06, "approximately 1,424,819" after (6-K `0001753926-26-001314`) | 1,424,819 | 180,336 (the interim's own retroactive Class B count, 6-K `0001753926-26-001875`) |
  | 2026-08-21 | warrants cut to US$0.70, warrant shares raised to "approximately 42,717,046" to preserve the aggregate exercise proceeds (6-K/A `0001753926-26-001582`; 424B3 `0001753926-26-001633`) | | |
  | 2026-10-02 | "approximately 9,010,733" before a 1-for-6 consolidation effective 2026-10-07, "approximately 1,501,789" after (6-K `0001753926-26-001886`) | 1,501,789 | 30,056 (180,336 / 6; the articles combine the other class proportionately, 20-F Item 10.B; no filing states the post-October Class B count, so this line is computed, said so) |
  **Count used: 1,531,845** (1,501,789 Class A + 30,056 Class B). Whether the October announcement's 9,010,733 already
  includes Class B is not stated; if it does, the count is 1,501,789. The difference is 2% and changes no conclusion. No
  treasury shares are reported. **Overhang:** the warrants outstanding after the October consolidation are estimated at
  about 5.86 million warrant shares at US$4.20 (42,717,046 less the 7,585,914 shares issued 2026-08-06 to 2026-10-02,
  divided by six; exercise price and floor US$0.70 times six), about 3.8 times the shares outstanding. Estimate, not a
  filed figure; the warrant form (exhibit 4.2 of 6-K/A `0001753926-26-000940`, section 3(f)) resets the exercise price and
  raises the warrant share count at each share combination, subject to the floor of section 3(j).
- **Market cap:** US$2.70M (1,531,845 × US$1.76).
- **Sovereign for the earnings currency (HKD):** **4.519%**, the closing reference yield of the HKSAR Government's 20-year
  institutional bond 20GB4503001 (coupon 3.99%), 2026-10-16, from the Government's own file
  `https://www.hkgb.gov.hk/en/others/documents/HKD_DailyClosingReferencePricings_IBPandGSBP.xls` (Infrastructure Bond
  Programme / Government Sustainable Bond Programme benchmark table, "Daily HKD Institutional Government Bond Closing
  Reference Pricings"; the file names Bloomberg as the calculator and the Government as owner). **Gap recorded:** the
  protocol's table has no HKD row; `tools/sources.py` has no HKD source (`tools/run.py` printed "NO ISSUING-AUTHORITY SOURCE
  configured for HKD"); the HKMA's API refused the request (HTTP 405 from its firewall); the longest HKD government tenor is
  20 years, not 30, so the rate is the longest sovereign the issuer has, taken from the issuer's programme site.
- **Filings read** (operator rule 4): 20-F for FY2025 (filed 2026-01-16, `0001753926-26-000125`): Items 3.D, 4.A, 4.B,
  5, 7, 10.B, the audited statements and notes; 20-F for FY2024 (`0001213900-25-007523`) and FY2023
  (`0001213900-24-008504`); the IPO prospectus 424B4 of 2024-01-23 (`0001213900-24-005750`) for the FY2021 balance
  sheet; the unit-offering prospectus 424B3 of 2026-05-12 (`0001753926-26-000819`); the resale F-1 of 2026-06-12
  (`0001753926-26-001005`); the 424B3 of 2026-08-26 (`0001753926-26-001633`); the interim 6-K of 2026-09-29
  (`0001753926-26-001875`, exhibits 99.1 statements "unaudited and unreviewed", 99.2 press release); the 6-Ks of 2026-05-13,
  05-28, 06-16, 06-30 (EGM), 07-16 (auditor change), 08-03, 08-04, 08-20, 08-21 (and /A), 09-15 (two), 10-02 (two), and the
  warrant and pre-funded warrant forms. A foreign private issuer files no proxy; Item 6 and Item 7 of the 20-F stand in
  for it. **Cross-check:** FY2025 revenue HK$192,386,583 on the filed statement of operations (F-4) equals the Item 5
  table and the segment note (HK$111,862,812 engineering + HK$80,523,771 guarding); FY2025 net cash used in operating
  activities HK$(15,456,974) on F-6 equals the Item 5.B cash-flow table.
- **`tools/run.py`:** refused (earnings in HKD, quote in USD: "Refusing to convert"). **Arithmetic by hand** from the filed
  statements, in `calc.py`. Owner cash = net cash from operations less purchases of property, equipment and intangibles,
  less the stock pay the cash-flow statement adds back (the "amortization of service fee", which is shares issued to
  consultants, and "share-based compensation", restricted shares to directors). Proceeds from asset sales are not counted
  (FY2021's HK$17.76M disposal, with a HK$3.93M gain, is a one-off property sale, left out and said so). HK$ millions:

  | FY (Sept) | operating cash | capex + intangibles | stock pay added back | **owner cash** | net income attributable |
  |---|---|---|---|---|---|
  | 2021 | 18.58 | 2.89 | 0 | **15.69** | 5.80 |
  | 2022 | 4.45 | 2.30 | 0 | **2.16** | 7.76 |
  | 2023 | (13.54) | 0.78 | 0 | **(14.32)** | 9.70 |
  | 2024 | 14.10 | 3.25 | 1.37 | **9.48** | 10.65 |
  | 2025 | (15.46) | 1.64 | 8.47 | **(25.57)** | (18.48) |
  | five-year average | | | | **(2.51)** | 3.09 |

  On the all-equity basis (interest paid added back and interest income taken out, both after the 16.5% profits tax) the
  average is **HK$(2.73)M**. Depreciation and amortisation ran HK$2.8M, 2.3M, 2.0M, 2.0M, 1.8M against the capex above;
  stock pay is resolved (no other stock pay is in the cash-flow statement). The six months to 2026-03-31 (unaudited and
  unreviewed) show a net loss of HK$4.24M; the interim furnishes no cash-flow statement.

- **The balance sheets, read first** **[M2025-032]**. The filer has filed balance sheets for 2021 to 2025 and 2026-03-31
  only (it registered with the SEC in 2023; the FY2020 equity of HK$44.4M appears only in the statement of changes in
  equity); eight to ten years do not exist. HK$ millions, at 30 September:

  | | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-03-31 |
  |---|---|---|---|---|---|---|
  | cash | 31.1 | 25.2 | 16.4 | 52.3 | 25.4 (+9.9 restricted) | 28.7 (+10.1 restricted) |
  | trade receivables + contract assets | 32.6 | 28.3 | 38.2 | 28.3 | 38.0 | 34.2 (reclassified) |
  | inventories | 17.9 | 22.7 | 40.9 | 47.6 | 25.8 | 18.6 |
  | contract liabilities (customer money in advance) | 30.1 | 27.2 | 22.7 | 27.8 | 11.3 | 9.9 |
  | notes payable (the only borrowing) | 2.0 | 2.9 | 3.5 | 2.4 | 2.0 | 1.5 |
  | goodwill + intangibles | 1.4 | 1.5 | 1.4 | 1.5 | 1.5 | 1.9 |
  | equity | 41.5 | 41.7 | 56.4 | 97.7 | 86.2 | 83.7 |
  | retained earnings | 32.3 | 32.1 | 41.8 | 51.3 | 32.8 | 28.6 |
  | revenue (year) | 117.6 | 136.4 | 163.7 | 182.2 | 192.4 | 86.3 (half) |

  What the figures say: no debt of size in any year, and none needed. What they also say: the equity was built by the
  owner and the market, not kept from earnings. HK$25.0M of dividends went to the pre-IPO owner in FY2021 and FY2022, he
  put HK$5.7M back in FY2023 and FY2024, the IPO added HK$24.3M net and shares issued to consultants HK$6.6M (FY2024);
  retained earnings stand below their 2021 level. Working capital is the business's real capital: inventory more than
  doubled with revenue in FY2023 and FY2024 and was then run down, and customer money held in advance fell from HK$27.8M
  to HK$9.9M in eighteen months, a source of cash that has reversed. The IPO cash (HK$52.3M at September 2024) was down
  to HK$38.8M including restricted deposits by March 2026 with no dividend, buyback or acquisition paid. The restricted
  HK$9.9M secures bank guarantees for one customer's contracts (Item 5.B), with a HK$9.0M company guarantee behind it.
  What the figures cannot say: anything after 2026-03-31, the date of the last balance sheet, although the share count has
  since risen more than thirtyfold on a like-for-like basis.

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. The
question bites here, because what the Class A holder owns has changed under him four times in fourteen months
(three consolidations and a warrant reset that raises the warrant count at each one); a holder locked in for five years
owns a claim whose size is set by warrant holders, not by the business. Who is paid to tell you: the filings were
written for an offering programme, by an issuer that paid consultants in shares for "market research" and "investor-searching
services" (20-F note 19), and "you do not get impartial advice [...] when there’s (an) enormous amount of fees possible from
one action" **[M2020-037]**. The analyst's habits: look for "what’s wrong in things" **[M2025-013]**, and write the
contrary evidence down as it is found **[M1997-127]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the IPO cost HK$14.7M against US$5.0M gross (20-F note
15); (2) the May 2026 units: US$6.0M gross, net estimated US$3.6M (424B3 `0001753926-26-000819`); (3) the warrant price was
cut by 84% one month after issue and again in August, with more warrant shares granted to keep the holders' aggregate
proceeds; (4) the interim press release's "Recent Developments" lists awards and distributorships and none of the offering,
the repricings or the consolidations; (5) FY2025 gross margin 16.0% against 26.1%; (6) the interim statements were
furnished "unaudited and unreviewed" on the last days of the six-month window, after the auditor was replaced.
Evidence for the business, also written down: no borrowing, 80.7% of FY2025 customers recurring (Item 5.A), on the
approved lists of more than 13 Hong Kong government departments (Item 4.B), a hospital contract the company puts at
HK$107.3M in total (6-K `0001753926-26-001875`, exhibit 99.2).

## THE STANDING RULE
A cash purchase of a listed share, unlevered, cannot ruin the buyer; the rule binds how it would be financed and sized:
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**; "borrowed money
has no place in the investor's tool kit" **[L2014-005]**. Nothing in this name requires borrowing. Not engaged.

**The lines of evidence, chosen here and why** (the brief leaves them to the analyst). From Item 4.B: what the two
subsidiaries sell, how they win the work (quotation and tender), whose products they install (other firms' brands under
distribution agreements), the customers and their concentration, the suppliers and theirs. From Item 3.D: the risk
factors the filer itself writes about competition, entry barriers, pricing and labour. From Item 5: the gross margin by
service line over FY2023 to FY2025, the segment operating profit, the cash flows and what the filer says moved them. To
these the run adds the capital record from the 6-Ks of 2025 and 2026, because the question of what a Class A share is a
claim on cannot be answered from the 20-F alone. Chosen because Q1 and Q2 turn on how the work is won and kept, and the
filer's own words on that are in Items 3.D and 4.B; Q4 to Q6, if reached, turn on Item 5, the notes and the 6-Ks.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
"the first question is, can I understand it?" **[M1995-051]**; understanding is "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**.

- **What it is (20-F Item 4.B, `0001753926-26-000125`).** Two Hong Kong operating companies. **Shine Union** (from 1998)
  designs, supplies, installs and maintains security systems made by others: threat detection (X-ray machines, metal
  detectors; exclusive distributor of two brands), traffic and pedestrian control (turnstiles, automatic doors, fare
  gates) and extra-low-voltage systems (CCTV, access control); one small own-brand car-park system, SUNGATE (HK$4.6M,
  4.1% of engineering revenue in FY2025); some equipment leasing. Work is won "through direct invitation for quotation
  from customers, or through a competitive tendering process of the project employers or their main contractors", often
  as a subcontractor, with labour-heavy work subcontracted again. **Fortune Jet** (acquired 2019) supplies security
  guards and air-cargo screeners, full- and part-time, and runs the mandatory training courses. FY2025 revenue HK$192.4M:
  engineering HK$111.9M (58.1%), guarding and screening HK$80.5M.
- **The key variables, and whether they are foreseeable** (test 2). Engineering: the volume of Hong Kong public and
  private fit-out and infrastructure work let by tender, the margin each tender leaves, and the continuance of the
  distribution agreements. Guarding: headcount billed against the statutory minimum wage. None of these is a technology
  forecast: Shine Union "does not participate in the product design or development of security systems save for its
  “SUNGATE” carpark systems" (Item 4.B); the machines' makers carry the technology, the installer carries the labour and
  the tender. The chemistry need not be understood if "I understand the economic dynamics of the industry" **[M2011-014]**.
- **Do the past statements tell me the future ones?** (test 3, "do I understand enough about this business so that the
  financial statements will tell me the information that’s useful to me" **[M2008-033]**). In kind, yes: five years of
  statements show a contractor whose revenue moves with the projects in hand (the filer names them by size, Item 5.A),
  whose margin moves with the subcontracting share and the minimum wage, and whose cash moves with inventory and with
  customer money held in advance. In amount, no, year by year; Q1 does not ask the amount to that precision.
- **Routing.** No fast-moving technology at the company's own level; not a bank; the holding company is read by its parts
  (section B of the gaps case): engineering carries 74% of five-year gross profit (HK$149.9M of HK$201.6M, FY2021 to FY2025)
  and 86% of the segment operating profit the filer discloses (FY2023 to FY2025, the only years it is given by segment:
  HK$38.6M of HK$44.7M before unallocated costs). Both parts are understood by the same tests.
- **The doubt test** ("if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**).
  The doubt that exists here is not about what the business does or how it earns, but about what a share of it will be a
  claim on, given the warrant structure; that is a question for Q5 and Q6, not for Q1, and it is carried there.
- **VERDICT: IN.** The business is a tendered installer of other firms' security equipment and a labour-hire guarding
  service in one city; its ten-year economics can be foreseen in the sense **[M2012-065]** gives the word: the competitive
  position of a price-taking contractor in a field with many rivals, which is what Q2 must now test. Filing fact: Item 4.B
  of the 20-F (`0001753926-26-000125`).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**; a moat is what "protects excellent returns on invested capital"
**[L2007-004]**. The question is asked of the deciding part, engineering, and of the guarding part beside it.

**The parts table** (section B of the gaps case; segment note 24 of the FY2025 20-F and note 22 of the FY2023 20-F):

| part | five-year gross profit FY2021-25 | segment operating profit FY2023-25 (only years given) | castle | decides |
|---|---|---|---|---|
| security-related engineering (Shine Union) | HK$149.9M (74%) | HK$38.6M (86% of the parts' total) | open, below | **yes** |
| guarding, screening, training (Fortune Jet) | HK$51.7M (26%) | HK$6.2M (14%) | open, below | no |
| unallocated head-office costs | | HK$(43.0)M (FY2025 alone HK$(23.1)M) | | |

**The castle tests, each with its filing fact** (20-F `0001753926-26-000125` unless stated):
1. **The attacker with money** ("if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I
   do it?" **[M2011-015]**). The filer answers it: "There are a substantial number of security-related engineering
   services providers, security guarding and screening services providers, and related vocational training course operators
   in Hong Kong. Entry barriers and set up costs are considered to be moderate." (Item 3.D, repeated in Item 4.B,
   Competition.) The field is one where "there are some industries that are just never going to have barriers to entry"
   **[M2012-106]**.
2. **Pricing power, and the agony before a rise** ("a prayer session before you raise your prices a penny" **[M2005-020]**).
   The filer: "Due to the large number of competitors, we face significant downward pricing pressure thereby reducing our
   profit margins. Furthermore, if we do not provide a competitive quote relative to our competitors, our services may not
   be attractive to prospective customers" (Item 3.D). Equipment-leasing renewals were given "more competitive prices"
   (FY2025, Item 5.A) and "rental terms more preferential to the customers" (interim, `0001753926-26-001875`). The
   minimum-wage rise was not passed through: guarding gross margin 15.2%, 15.1%, 12.6% (FY2023-25), "an increasing labor
   cost triggered by a rise in statutory minimum wage" (Item 5.A).
3. **Would the customer still choose it over the low bid** ("it wouldn’t be a question of people buying candy for the low
   bid" **[M2017-009]**). The work is won by quotation and "competitive tendering" (Item 4.B); the filer must "estimate"
   its tender prices against rivals (Item 3.D). The customer who tenders is, in the rows' words, one of those who "don't
   care from whom they buy" **[L2004-003]**.
4. **The brand in the customer's mind.** The brands are the makers': over 10 brands distributed, two exclusively, under
   agreements with "minimum purchase requirements and exclusive distribution provisions", whose breach "may entitle
   suppliers to terminate the distribution agreements" (Item 3.D); the five largest suppliers were 52.7% of FY2025
   purchases, the largest 20.2% (Item 4.B). The only own brand, SUNGATE, is 4.1% of engineering revenue. Whatever loyalty
   the X-ray machine commands belongs to its maker, who can choose another distributor.
5. **The low-cost position.** No filing claims it. The filer lists "cost management and efficiency" among seven competitive
   factors and claims differentiation by "comprehensive range", "reputation" and "access to skilled professionals"
   (Item 4.B). In a field of commodity-like characteristics the rows' warning is "you just can’t take labor costs that are
   materially higher than your competitor" **[M2001-013]**; nothing in the filings shows Shine Union's costs below its
   rivals'.
6. **High labour content.** Fortune Jet sells labour by the hour, and Shine Union subcontracts "labor-intensive" work
   (Item 4.B). The row against "a business that has a very high labor content" **[M2007-116]** is written of goods shipped
   in from abroad; guarding cannot be imported, so the row is weighed for the labour half only.
7. **Widening or narrowing** ("how wide the moat is and whether it’s likely to widen further or shrink on you"
   **[M1999-108]**). Narrowing on every measure the filings give: group gross margin 30.6%, 28.7%, 29.3%, 26.1%, 16.0%
   (FY2021-25) and 20.7% in the half to March 2026; project-and-maintenance margin 36.4%, 32.1%, 17.0% (FY2023-25), the fall
   put down to "larger extent of use of subcontracting services"; engineering segment operating profit HK$12.7M, 23.4M,
   2.5M; half-year project-and-maintenance revenue down 32.3% on fewer large projects (interim). The management's answer,
   in 2026, is to add more distributed products (GEZE doors, HDX portable X-ray, Seetrue AI screening) and to buy a
   two-year distribution right (KM Safety Solution, HK$5.6M cash, 6-K `0001753926-26-001888`): more of the same kind of
   position, not a deeper one.
8. **What could destroy it** **[M2000-014]**. The loss of an exclusive distributorship; a lower tender price from a rival;
   the next minimum-wage rise. The filer names all three (Item 3.D).
9. **Ask the competitors.** Not on the public record.

**The competitor row.** The 20-F names two: "Our principal competitors include Manifest Marketing Limited and ECI
Technology Holdings Ltd." (Item 4.B). **Neither files with the SEC; flagged.** Manifest Marketing Limited: no public filing
found by a web search; not read. ECI Technology Holdings Limited (HKEX GEM 8013; "the provision of ELV solutions primarily
on central control monitoring system in Hong Kong", with some security services) files its own annual reports with the
Hong Kong exchange. **CONVENTION of this run:** where a named rival files only with its home exchange, its own filing there
is read as "the competitor's own filing" the brief asks for; rationale: it is the rival's primary document, and an
aggregator's figures are the only alternative. Read: ECI's annual results announcement for the year to 31 August 2025,
HKEXnews document `2025112601566` (dated 2025-11-26), its five-year financial summary and statement of financial position:

| year (ECI to August; SUGP to September) | 2021 | 2022 | 2023 | 2024 | 2025 | five-year profit over five-year equity |
|---|---|---|---|---|---|---|
| ECI revenue (HK$M) | 138.2 | 130.4 | 174.0 | 200.3 | 195.0 | |
| ECI gross margin | 22.4% | 24.5% | 23.3% | 24.9% | 25.6% | |
| ECI profit / year-end equity (HK$M) | 8.7 / 64.5 | 6.3 / 70.7 | 5.6 / 75.6 | 8.9 / 84.7 | 2.6 / 87.4 | **8.4%** |
| SUGP revenue (HK$M) | 117.6 | 136.4 | 163.7 | 182.2 | 192.4 | |
| SUGP gross margin | 30.6% | 28.7% | 29.3% | 26.1% | 16.0% | |
| SUGP profit attributable / year-end equity attributable (HK$M) | 5.8 / 40.3 | 7.8 / 40.1 | 9.7 / 56.4 | 10.7 / 97.7 | (18.5) / 86.2 | **4.8%** |

**The field's returns over the span, judged in words** (section C; "ordinary" carries no figure). The rival the filer itself
names is the same size, sells the same kind of work in the same city, and over five years that include a downturn (ECI's
revenue fell in its 2022; SUGP's engineering revenue fell in FY2022, HK$81.5M to HK$77.2M) and a recovery, earned an
ordinary return on its equity with a lower gross margin; SUGP earned less, and its best years were earned on an equity
reduced by HK$25.0M of pre-IPO dividends. Neither shows the "excellent returns" a moat exists to protect **[L2007-004]**; the
rows' case is "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. The guarding part,
at 12.6% to 15.2% gross margin on resold labour, is plainer still.

**VERDICT: OUT.** The castle is shown open on the evidence of the filer's own words (moderate entry barriers, a substantial
number of competitors, downward pricing pressure, work won by competitive quote) and of the figures (margins narrowing for
four years; a field whose durable players earn ordinary returns). A castle shown open closes OUT, not TOO HARD: "If the
answer had been yes, we wouldn’t have done it." **[M2011-015]**; the standing castle that protects only ordinary returns
is OUT by the list under Q2 (section C), because the tenuous-moat reason for TOO HARD, "We don’t know how to valuate
that" **[M2000-019]**, does not apply where the returns are known. The deciding part closes the file; the guarding part,
which does not decide, is open too. **Q3 to Q12: NOT REACHED.**

## Q3 — NOT REACHED.
## Q4 — NOT REACHED. (The balance sheets were read in Step 0, as the template asks when the file closes before Q4.)
## Q5 — NOT REACHED.
## Q6 — NOT REACHED.
## Q7 — NOT REACHED as a question. The reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — NOT REACHED.
## Q9 — NOT REACHED.
## Q10 — NOT REACHED.
## Q12 (optional) — NOT REACHED.

---
## THE BOX
**OUT at Q2** (the castle shown open: moderate entry barriers and a substantial number of competitors in the filer's own
words, work won by competitive quote and tender, gross margin narrowing from 30.6% to 16.0% over five years, and a named
rival earning ordinary returns over the same span); **integrity facts recorded, not judged.** COMPUTATION range nil to
nil, fair price nil, against US$1.76.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2. Each with its source **[M1997-127]**. A later
run that reaches Q5 must answer the integrity facts **[M2013-088]**.)*

**Bearing on Q3 (the capital).** Owner cash over FY2021-25 sums to HK$(12.6)M against HK$15.4M of attributable net
income: the difference is working capital, chiefly inventory bought ahead of projects (FY2023 +HK$18.2M) and customer
money in advance running off (FY2025 HK$(16.5)M) (cash-flow statements, 20-Fs `0001213900-24-008504`,
`0001753926-26-000125`). Capex is close to depreciation each year (HK$0.8M to HK$3.0M a year against HK$1.8M to HK$2.8M).
FY2025 losses on disposal of leased X-ray machines HK$2.0M (Item 5.A).

**Bearing on Q4 (the accounts).** (1) Three material weaknesses: lack of U.S. GAAP staff and policies, no formal risk
assessment or control framework, weak IT general controls (20-F, risk factors and controls; repeated in the auditor-change 6-K
`0001753926-26-001196`). (2) Marcum Asia dismissed 2026-07-06, Guangdong Prouden CPAs appointed; "no disagreements"; Marcum's
letter agrees (6-K `0001753926-26-001196`). (3) The interim statements to 2026-03-31 were furnished on 2026-09-29 as
"unaudited and unreviewed" (6-K `0001753926-26-001875`); they carry a balance sheet and income statement and no cash-flow
statement, and reclassify unbilled receivables from contract assets to trade receivables for the prior year. (4) The credit-loss
line moves: provision HK$8.6M (FY2023), reversal HK$(3.2)M (FY2024), provision HK$2.4M (FY2025) (cash-flow statements).
(5) The Item 5.A sentence on SG&A for FY2025 says "The decrease was mainly due to the net impact of" an item list, for an
expense that rose 35.2%; the list does not name the HK$5.5M of consultant fees paid in shares, and the segment note books
HK$6.29M of "advertising and promotion" at head office (unallocated) that year; whether the share-paid fees sit in that line
is not stated. (6) Stock pay (shares to consultants and restricted shares to directors) was HK$1.4M in FY2024 and HK$8.5M in
FY2025, against a FY2024 net income of HK$10.7M; the interim names "non-employee share-based compensation" of HK$2.0M "since
the Company carried out less marketing research and investor-searching activities". Stock pay is a real cost
**[L2015-003]**; owner cash above deducts it.

**Bearing on Q5 (the people) — integrity facts.** (1) Control: Mr. Chan Ming Dave, chairman and chief executive, held
"98.8% of the total voting power" through Class B shares with fifty votes each (20-F Item 3.D); 92.69% after the pre-funded
warrants were exercised (F-1 `0001753926-26-001005`); by the run's arithmetic about half of all votes after October
(30,056 Class B × 50 against about 1.50M Class A), before any Class A he holds. The consolidations of August and October
2026 were approved "by written resolution of the Company’s majority shareholders" (6-Ks `0001753926-26-001314`,
`0001753926-26-001886`). (2) Shares issued for services: 397,500 pre-consolidation shares (HK$6.57M) to Chengdu Xiaohou
Information Technology Limited for "market research consultancy services" (2024-04-26), against an IPO of 1,250,000 shares
raising HK$24.3M net; 80,000 shares to VBG Asia Limited for "investor-searching services" (2025-09-16) (20-F note 15 and
note 19). (3) The interim press release's "Recent Developments" (exhibit 99.2, `0001753926-26-001875`) lists contract
awards, distributorships and training approvals and does not mention the May 2026 offering, the two warrant repricings or
the two 2026 consolidations, all of which preceded it. (4) Nasdaq: bid-price deficiency (2025-03-20), public-float
deficiency (2025-08-27), delisting determinations (2025-09-17, stayed; 2026-08-03, cured by the 1-for-5 consolidation)
(20-F Item 4.A; 6-Ks `0001753926-26-001306`, `0001753926-26-001570`). (5) Form 144 notices were filed under four insider filer
ids in 2024 to 2026 (EDGAR index); not read. (6) Pre-IPO, HK$25.0M of dividends were paid to the owners in FY2021 and FY2022
(statements of changes in equity, 20-F FY2023). The rows that would weigh these, if Q5 is ever reached: "hell-bent on
issuing shares" **[L2014-015]**; "things that they do in public in relation to their investors and the promises they
make" **[M2004-067]**; "Sincerity and empathy can easily be faked." **[L2023-003]**.

**Bearing on Q6 (the money and the owners).** (1) Issuance record: IPO January 2024 at US$4.00 (gross US$5.0M, offering
costs HK$14.7M, 20-F note 15); shares to consultants 2024 and 2025; the 2024 equity plan; the unit offering of May 2026 at
US$2.00 (gross US$6.0M; the prospectus estimates net proceeds of "approximately US$3.6 million", with offering expenses of
"approximately US$2.0 million", 424B3 `0001753926-26-000819`), each unit carrying two warrants at US$5.50 with
"Ratchet Anti-Dilution Protection" and a share-combination reset (warrant form, section 3(f)). (2) The warrant price was
cut to US$0.87 on 2026-06-17, a month after issue, the board citing "the potential opportunity to generate additional capital
through warrant exercises" (6-K `0001753926-26-001019`), then to US$0.70 on 2026-08-21 with the warrant share count raised
from 34,370,035 to about 42,717,046 so that the holders' aggregate exercise proceeds "are substantially preserved"
(6-K/A `0001753926-26-001582`). (3) Three consolidations: 1-for-10 (2025-08-25), 1-for-5 (2026-08-06), 1-for-6
(2026-10-07); a capital reduction to HK$0.000001 par approved 2026-06-25 so that shares can be issued below the old par
(6-K `0001753926-26-001111`). (4) Shares outstanding, like-for-like after all consolidations: about 48,829 at 2026-03-31
(the interim's 292,972 divided by six) and about 1,531,845 on 2026-10-07. (5) Stated uses of the money: "strategic
acquisitions and investment opportunities" and working capital (6-K `0001753926-26-000859`); the first acquisition, KM
Safety Solution Company Limited, HK$5.616M cash from Lead New Limited, its main asset a 24-month distribution agreement
(6-Ks `0001753926-26-001776`, `0001753926-26-001888`); no earnings of KM are filed. The rows that would weigh these:
issuing "shares beneath" intrinsic value harms the owners **[M1996-013]**; "We will issue common stock only when we receive
as much in business value as we give." **[R1995-010]**.

**Bearing on Q9 (exposures).** No borrowing beyond HK$1.5M of notes payable; HK$10.1M of deposits pledged for bank guarantees
on one customer's contracts, "used to cover any potential liquidated damages", with a HK$9.0M company guarantee (20-F Item
5.B). The warrant overhang (about 5.86M warrant shares at US$4.20, estimated in Step 0) is a dilution exposure to the
holder, not a demand for cash on the company.

**Bearing on Q12.** Security engineering and guarding is not among the businesses the rows name.

---
## COMPUTATION, NOT A CLEARANCE
*(The reporting figures the operator asks for, built as Q7 builds its range. Not a clearance, no entry language; operator
rule 3. Arithmetic in `calc.py`.)*

- **Cash input:** owner cash after every real cost, all-equity basis, five-year average FY2021-25: **HK$(2.73)M** a year
  (equity-only basis HK$(2.51)M). Series by year (all-equity, HK$M): 15.86, 2.19, (14.44), 8.83, (26.08).
- **Specific (a), cycles:** neither end year is aberrational on the filer's own description (FY2025's margin fall is put
  down to subcontracting and wages, not to a one-off event, and the loss continued into the half to March 2026); no cycle
  base. The literal window is the base, so the literal window and the central figure are the same.
- **Specific (b), decline:** the series changes sign, the compound rate between the end years is meaningless, and the
  halves (FY2021-22 average HK$9.0M, FY2024-25 average HK$(8.6)M) are of opposite sign, so the range is **the no-growth case
  alone**, said so.
- **Specific (c), acquisitions:** none in the window. KM (HK$5.616M cash, closed 2026-10-02, after the window and before the
  price date) is credited at nothing, no earnings being filed, and its price is added to net debt.
- **Specific (d), working capital:** counted, as the rule requires; the FY2025 draw is not tied by the filer to one contract,
  so no aberrational-year adjustment. Shown beside: owner cash before working-capital changes (attributable net income plus
  depreciation and amortisation less capex, FY2021's gain on the property sale removed), HK$2.11M a year all-equity.
- **Specific (e), growth spending:** capex runs at about depreciation; no growth spending to separate. **(f), the cap:** not
  engaged (no growth carried).
- **Rate:** 4.519% (HKSAR 20-year, 2026-10-16). Ten years then zero nominal growth at no growth is a perpetuity at the rate.
- **Net debt** (all-equity basis, at the latest filed balance sheet, 2026-03-31, interim 6-K `0001753926-26-001875`): cash
  HK$28.65M less notes payable HK$1.48M = net cash **HK$27.17M** (restricted deposits of HK$10.11M left out, pledged; shown
  beside: HK$37.28M); less the KM price, HK$21.55M. Operating leases left out, said so. The interim states no other
  subsequent event.
- **Value, central (all-equity):** business HK$(60.3)M at the sovereign; with net cash, HK$(38.8)M: **negative; nil per
  share.** **The range: nil to nil** (one case, no growth). Equity-only beside: HK$(55.6)M, nil.
- **The floor, tested first:** no case earns the floor at any positive price; the file would close OUT at Q7 by the floor,
  whatever the width.
- **Fair price** (each end case valued at 10%, the two averaged; the one case here): HK$(27.3)M plus net cash HK$21.55M =
  HK$(5.7)M: **nil**, on the all-equity basis; equity-only beside, nil. After the company's own tax (16.5% Hong Kong profits
  tax, no conversion; no carryforward shelter is relied on).
- **Against the price:** US$1.76 a share, market cap US$2.70M.
- **What the central figure leaves out, written down because it cuts both ways.** The last balance sheet is dated before
  the share count rose about thirtyfold, like-for-like. Cash raised after 2026-03-31 is stated by no balance sheet: the
  prospectus's net-proceeds estimate for the units (US$3.6M) is filed; the warrant cash is only inferable (shares issued
  between the dated counts times the stated exercise prices: about US$3.1M at US$0.87 and US$5.3M at US$0.70, gross,
  if every new share was a cash exercise, which no filing confirms). On those inferences net cash would be about HK$115M,
  and the central owner-cash case would leave a positive equity value; the before-working-capital case more. Both are shown
  in `calc.py` and **decide nothing**: the cash is not on any filed balance sheet, part of it may already be spent (the
  operating loss continued, KM was bought), and about 5.86M further warrant shares stand against 1.53M shares outstanding,
  under a contract that resets their price at each consolidation and has twice been amended downward by agreement. The
  market's US$2.70M against an inferred US$14.8M of cash is itself evidence that the inference, or the claim of the Class A
  shares on that cash, should not be trusted. No other price figure is reported.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): step 0,
      Q1, Q2, and this close, each a pathspec commit of the run file and research folder only.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (not written by this
      analyst); the fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident at
      start-up (another run's commit subjects, a memory index, two research-folder names) is declared under CONTAMINATION
      and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is in that row (`check_cites.py`,
      0 problems); no E-ids. Every filing fact carries its accession or HKEXnews document number.
- [x] The order was kept; Q2 was the first STOP that failed and closed the run; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE; nothing after Q2 is a clearance.
- [x] Owner cash after every real cost, stock pay deducted, never a net-income proxy (operator rule 5; the
      before-working-capital line is shown beside only and is labelled so); the sovereign from the issuing government's own
      file, dated; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (foundations); the facts found for later questions are under AFTER THE STOP,
      with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` refused the currency pair and printed nothing used; no rule, id or verdict it prints was read.
- [x] `python tools/check_framework.py` PASS before the final commit (run below).
- **Weaknesses of this run, said plainly.** (1) Only five years of balance sheets exist, not eight to ten. (2) The segment
  operating profit is filed for three years only, so the parts' five-year operating-profit shares are partly gross-profit
  shares. (3) The second named rival (Manifest Marketing) could not be read, and the one rival read is read from its home
  exchange, by a convention of this run. (4) The post-October Class B count and the post-March cash are computed or
  inferred, not filed. (5) Q1 IN is a judgment that the business is understood in kind; a stricter reader could hold that
  the year-to-year margin cannot be foreseen; the file closes at Q2 either way, OUT on the evidence rather than TOO HARD.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The net-debt date against a moving share count.** Q7's basis takes net debt "at the latest filed balance-sheet date
with the subsequent events that filing itself states added". Here the latest balance sheet (2026-03-31) predates a
thirtyfold rise in shares and an unknown cash raise, and the filing that carries it states none of the raises; the rule as
written pairs pre-issuance cash with post-issuance shares. The run kept the rule for the central figure (which is negative
either way on the business) and showed the inferred cash beside; the text needs a line for a share count that moves after
the balance sheet, for instance pairing cash and shares at the same date, or adding raises stated in later 6-Ks. (2) **No
HKD sovereign** in the protocol's table or in `tools/sources.py`; the issuer's longest tenor is 20 years, and the HKMA API
refuses scripted requests; the run used the HKSAR Government's own closing-pricing file. (3) **Rivals that file only at
home.** The brief asks for rivals that file with the SEC; for a Hong Kong contractor none does. The run confessed a
convention reading the named rival's HKEX filing; the framework has no line on it. (4) **What a share is a claim on.** No
STOP before Q5 and Q6 owns the case where the per-share claim itself is unstable (reset warrants several times the share
count, repeated consolidations); the foundations' "a share is a business" names the problem and admits nothing, by design.
Had Q2 passed, the file would have carried this to Q5 and Q6 as a weighing with a candidate STOP (serial issuance, still
OPEN in section VI). (5) **A negative no-growth case.** Q7's specific (b) gives the no-growth case alone when the series
changes sign; it does not say what the per-share value is when that case is negative. The run wrote "nil" and showed the
negative figure. (6) **"Full cycle" for a contractor.** Section C asks for the field's returns over the last full cycle;
for a project contractor there is no defined cycle, and the run judged the five filed years, which hold a fall and a rise.
