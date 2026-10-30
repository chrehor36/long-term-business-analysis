# Company Run — Companhia Paranaense de Energia - COPEL (NYSE: ELPC; B3: CPLE3) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (3c51c8f3):** not held; neither ELPC, CPLE3, COPEL nor Paranaense appears in `PORTFOLIO.md`.

**Contamination, declared (seen by accident, not used).** (1) Listing `Test Runs/` to check for a same-day clash showed the
names of other run files dated 2026-10-18 (US and foreign utilities, among them "AXIAY AXIA Energia", plus an ADDENDUM of
2026-10-18 on the overnight runs) and their research folders; none was opened. AXIA is also a rival this run uses for Q2,
from its own SEC filing only. (2) The session context carried recent commit subjects of a CMS Energy run (box and
figures) and memory-index lines on the queue state; not used. (3) `python tools/run.py ELPC` printed only
"UNRESEARCHED" (no IFRS facts it could read), so no v4 material from it entered this file.

Units: R$ millions unless stated (the statements are in R$ thousands; figures here are rounded from them).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price (aggregator, flagged, operator rule 5):** CPLE3 R$ 17.70 (B3 close 2026-10-16); ELPC US$ 13.97 (NYSE close
  2026-10-16); source Yahoo Finance chart API via `tools/sources.py`. **Exchange rate:** PTAX R$ 5.0826 per US$ (Banco
  Central do Brasil, PTAX selling rate, 2026-10-16, Olinda service). ADS ratio: one ELPC ADS = four common shares (brief;
  the 20-F's Item 12D). Cross-check: US$ 13.97 / 4 x 5.0826 = R$ 17.75 a share, against R$ 17.70 on B3.
- **Shares by class** from the latest filing's cover: 2,982,810,590 common shares and one special-class preferred share
  (the State of Parana's golden share), as of 2025-12-31; 20-F for FY2025, filed 2026-04-16, accession
  `0002070979-26-000155`; `python Screens/cover_shares.py ELPC` returned the same two counts. The charter note (20-F note
  27.1, Item 16E): after the Novo Mercado migration every preferred share was converted into a common share on
  2025-12-22; the special-class share carries only vetoes (Copel DIS annual investments, name, seat, the 10% vote cap) and
  no economic claim beyond one share, so it is not added. **Treasury: 12,740,266 common shares** (note 27.1 table and
  Item 16E). **Shares outstanding: 2,970,070,324.** No share issue is stated after the 20-F in the 6-Ks read (the
  ILP deliveries are from treasury). Per ADS = 4 shares.
- **Market cap:** 2,970.07M x R$ 17.70 = **R$ 52,570M** (about US$ 10.34 billion at PTAX).
- **Sovereign for the earnings currency (BRL):** **12.87%**, Tesouro Prefixado com Juros Semestrais (NTN-F) maturing
  2037-01-01, the longest fixed-rate nominal federal bond offered, buying rate ("Taxa Compra Manha") of 2026-10-15, the
  latest date in the Tesouro Nacional's own file `PrecoTaxaTesouroDireto.csv` (Tesouro Transparente, the issuing
  authority's open-data portal). The selling rate that day was 12.99%. **CONVENTION of this run:** the protocol's table
  covers USD, JPY and EUR only; for BRL the series is the longest-dated fixed-rate nominal NTN-F at the Tesouro
  Nacional's quoted buying rate; rationale: it is the issuing authority's own quote of the longest nominal government rate,
  which is what the speakers' "long-term" government rate is. Annual averages of the same series (longest NTN-F each
  day, same file): 2016 13.00, 2017 10.25, 2018 10.59, 2019 7.85, 2020 7.34, 2021 9.69, 2022 12.31, 2023 11.79,
  2024 11.85, 2025 14.14 (percent); ten-year average 10.9%, 2021 to 2025 average 12.0%.
- **Filings read** (operator rule 4): 20-F FY2025 (filed 2026-04-16, `0002070979-26-000155`): Items 3.D, 4, 5, 6, 7,
  16E and the audited statements and notes 1, 2, 9, 10, 15, 16, 19, 20, 27, 31, 32, 37 in part. 20-F FY2024
  (2025-04-17, `0001628280-25-018102`), FY2023 (2024-04-11, `0001292814-24-001329`), FY2022 (2023-04-27,
  `0001292814-23-001843`), FY2020 (2021-04-20, `0001292814-21-001623`), FY2018 (2019-04-26, `0001292814-19-001487`)
  and FY2016 (2017-04-28, `0001292814-17-001079`), for the balance sheets and cash-flow statements. 2Q26 results release
  furnished on 6-K 2026-08-06 (`0001292814-26-004089`; its tables are text, the slide decks of `0001292814-26-004097`
  are images and were not read). Material fact of 2026-07-15 on the capital structure and dividend policy (6-Ks of
  2026-07-16: `elp20260715_6k`, `_6k1`, `_6k2`). There is no proxy; the 20-F's Items 6 and 7 stand for it. No
  interim financial statements were found furnished beside the 2Q26 release (the 6-K index lists only the release and
  images), so the latest filed balance sheet is 2025-12-31 and the latest stated net debt is the release's 2026-06-30
  figure.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2024, XBRL
  `CashFlowsFromUsedInOperatingActivities` R$ 3,394M against the filed cash-flow statement R$ 3,393,536 thousand (20-F
  FY2025, F-pages); total equity FY2024 XBRL R$ 25,637M against R$ 25,636,935 thousand filed. Both agree.
- `python tools/run.py ELPC`: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool failed on the IFRS
  20-F; every figure below is taken from the filed statements.
- **The lines of evidence chosen, and why** (derived from Items 4, 3.D and 5, as the brief asks): (1) the parts: the
  filer reports GET (with GER generation and TRA transmission shown as separate columns), DIS distribution, COM trading
  (note 31), so the parts table comes first; (2) the concession regime, because every asset is a concession that the
  grantor re-prices or re-tenders at expiry (Item 4, Concessions; note 1; note 32.2.7 and the new-framework paragraph);
  (3) hydrology, curtailment and market prices, because generation is the largest part and the 20-F names them as its
  key risks (Item 3.D); (4) the 2025 sector laws (15,235/2025 and 15,269/2025), because the filer says they "materially
  altered competitive dynamics across the industry" (Item 4); (5) the debt, because it has risen faster than equity and
  is CDI- and IPCA-indexed (Item 3.D; 2Q26 release).

### The balance sheets, ten of them, read before the income account **[M2025-032]**
(R$ millions, as filed in the 20-F named for the year; 2018 as restated in the FY2020 20-F; cash 2015 to 2017 from the
XBRL tags of those filings; "debt" is loans and financing plus debentures, current and non-current.)

| Dec 31 | Total assets | Cash | Trade receivables (current) | Net revenue | Debt | Equity (incl. NCI) | Intangibles | Contract assets | PP&E |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 28,948 | 1,481 | not extracted | 14,946 | 7,761 | 14,480 | 6,145 | (none; concession receivables) | 8,693 |
| 2016 | 30,434 | 982 | not extracted | 13,102 | 8,837 | 14,978 | 6,460 | (none) | 8,934 |
| 2017 | 33,162 | 1,040 | not extracted | 14,025 | 9,830 | 15,346 | 6,453 | (none) | 9,829 |
| 2018 | 36,048 | 1,948 | 2,944 | 14,935 | 11,566 | 16,336 | 6,029 | 3,348 | 10,841 |
| 2019 | 38,313 | 2,942 | 3,120 | 16,244 | 11,572 | 17,598 | 6,333 | 4,629 | 10,592 |
| 2020 | 46,785 | 3,223 | 3,768 | 18,633 | 9,946 | 20,251 | 6,929 | 5,207 | 9,495 |
| 2021 | 49,538 | 3,473 | 4,433 | 20,976 | 11,826 | 22,175 | 9,216 | 6,888 | 10,143 |
| 2022 | 49,704 | 2,678 | 3,342 | 20,535 | 12,454 | 21,131 | 10,278 | 7,673 | 10,069 |
| 2023 | 55,819 | 5,635 | 3,761 | 21,479 | 14,962 | 24,192 | 11,170 | 7,605 | 10,825 |
| 2024 | 57,384 | 4,162 | 3,963 | 22,651 | 17,246 | 25,637 | 16,624 | 7,211 | 8,517 |
| 2025 | 60,414 | 3,130 | 4,301 | 26,117 | 20,015 | 23,092 | 19,207 | 9,595 | 8,146 |

What moved and why, in "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**:
- **Debt rose 2.6 times (R$ 7.8bn to R$ 20.0bn) while equity rose 1.6 times (R$ 14.5bn to R$ 23.1bn), and equity
  includes R$ 2.0bn of new shares sold in August 2023.** Revenue rose 1.75 times. By 2026-06-30 total debt was
  R$ 23,484M including swaps (2Q26 release), and the company's own target is 2.9 times net debt to EBITDA (material fact
  2026-07-15). The business is being financed more and more by lenders; the equity's growth since 2023 came from the
  offering, not from retention, and fell in 2025 (dividends and interest on equity of R$ 2,450M declared plus the
  R$ 1,298M Novo Mercado premium, against net income of R$ 2,688M).
- **Intangibles jumped R$ 11.2bn to R$ 19.2bn between 2023 and 2025.** Of it, R$ 4,074M is the grant bonus paid on
  2024-11-21 to renew Foz do Areia, Segredo and Salto Caxias for 30 years (note 16; 20-F FY2024 cash-flow note), and
  the rest is the distribution concession's infrastructure transferred from contract assets as it enters service. These
  are rights the grantor leased, not assets the company owns outright; the bonus is a price paid to keep the right to
  operate plants the company built.
- **PP&E fell from R$ 10.8bn (2023) to R$ 8.1bn (2025)** as the renewed hydro plants moved into intangibles and the
  small hydros and Baixo Iguacu were sold (note 1).
- **Total assets jumped R$ 8.5bn in 2020** with PIS/Cofins tax credits recognised (the ICMS-exclusion case) and an
  equal liability "PIS and Cofins to be refunded to consumers" (R$ 3,928M at 2020); the credit belongs to the customers,
  not to the owners, and runs off through tariffs and a provision (R$ 1,851M in 2022; R$ 781M at 2025).
- **Receivables against sales are steady to falling** (19.7% of revenue in 2018, 16.5% in 2025); no build-up of the kind
  **[M1995-064]** warns of. Overdue receivables R$ 605.5M net of R$ 245.6M expected credit losses (Item 3.D).
- **Cash is not piling up:** R$ 3.1bn at 2025 against R$ 20.0bn of debt; the dividend payable of R$ 2,326M at
  2025-12-31 was paid in June 2026.
- **Retained profit reserves** went R$ 7.8bn (2021), 7.9 (2022), 9.0 (2023), 9.4 (2024), 8.2 (2025): five years of
  profits were paid out or offset, not compounded.
- What they cannot say: the concession assets (contract assets, concession receivables, intangibles) are measured by
  IFRIC 12 and by the regulator's replacement values (the "VNR" re-measurement that the 2Q26 release strips out of its
  recurring figures), so the book does not tell what the assets will earn; that is set by tariff reviews, auctions and
  the grantor at each renewal.

---
## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own a piece of a Parana utility if the market closed for five years
**[M1997-109]**; the question is the business, not the quotation. The foundation that bears hardest is the foreign one:
"So, Brazil would not be off limits at all, but we’d have to be able to get a lot of money into a business we understood
at an attractive price. We would want it to be cheaper than if it were in the United States." **[M2006-021]**, which
asks a lower price, not a pass. The margin asked grows with uncertainty: "the more volatile the business is [...] the
larger the margin of safety" **[M1997-080]**. No macro forecast enters (the 2026 election, the SELIC), except as a
property of the business. Who is paid to tell you: the 2Q26 release leads with "Recurring Ebitda" and "Recurring Net
Income", the company's own adjusted figures; this run works from the filed statements. **Contrary evidence, written
down as found** **[M1997-127]**: (1) the castle's rent belongs to the grantor: the three big hydro concessions were
renewed in 2024 only after a bonus of R$ 3,719.4M (set by MME/MF ordinance, paid as R$ 4,073.9M with SELIC), and the
2025 law lets the grantor "extend or tender" each old hydro concession "establishing the estimated value of the
concession, 50% of which will be allocated to the CDE" (20-F note on the new framework); (2) wind curtailment rose from
15.7% (2Q25) to 23.7% (2Q26) (2Q26 release), and the 20-F names "Excess supply of energy in the market" as a price risk;
(3) the filer's own five-year return on equity from continuing operations is about 10.6%, below the 12.0% average of
its own government's long bond over the same years; (4) owner cash after all spending was negative in 2024 and 2025.

## THE STANDING RULE
The buyer's own conduct: a purchase for cash, unlevered, sized so that a 50% fall changes nothing, puts the buyer at no
risk of ruin; "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and "We are never going to risk
what we have and need for what we don’t have and don’t need." **[M2012-081]**. A BRL asset adds a currency the buyer
does not spend; that is weighed in sizing, not here. Not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The company is a holding of four parts
  (note 31): GER, 7 hydro plants and 42 wind farms, 5,961 MW wholly owned; TRA, 4,594 km of lines plus SPC stakes; DIS,
  the concession for 394 of Parana's 399 municipalities to 2045-07-07 (note 2, contract 046/1999, fifth addendum);
  COM, free-market trading for 1,537 customers. Q1's holding-company paragraph reads it by the parts that matter.
- **The key variables and whether they are foreseeable** **[M1998-044]**. DIS: the regulated asset base (net RAB set at
  R$ 19.9bn in the sixth periodic review of 2026-06-23), the X factor (0.95%), losses against the regulatory limit, the
  volume billed through the grid; a free customer still pays the grid tariff (Item 4, Competition). TRA: annual
  permitted revenue (RAP), fixed by contract and indexed. GER: the price of energy under the company's bilateral and
  auction contracts (average R$ 198.99/MWh in 2Q26), hydrology (GSF 99.6% in 2Q26, 95.55% in 2Q25), wind curtailment
  ordered by the ONS, and the concession terms (Foz do Areia, Segredo, Salto Caxias to November 2054; Capivari Cachoeira
  under quota to 2046; Maua to 2049; Item 4). Each is a known variable, and the filings state each of them; the
  past statements tell me what the future ones are made of **[M2008-033]**.
- **The commodity price.** Generation sells a commodity at a price the market sets. "We don’t think we can predict
  commodity prices." **[M2016-025]**; the business is read "off the figures" **[M2008-069]**. The framework's commodity
  paragraph makes the price dependence no STOP at Q1 or Q2 by itself; whether it is the low-cost producer is Q2's
  question.
- **Abroad.** "where we think we understand the nuances of the corporate governance system and taxation" **[M2000-141]**.
  The governance is legible from the 20-F: no controller since August 2023 (State of Parana 15.91%, BNDESPAR 21.99%,
  others 61.67% after the Novo Mercado migration, note 27.1), a 10% cap on any holder's votes, and a golden share whose
  vetoes are listed. The tax is legible: 34% statutory, interest on equity deductible, the JCP risk named (Item 3.D).
  For Brazil the rows ask a lower price rather than a pass **[M2006-021]**.
- **Change.** The 2025 laws (15,235 and 15,269) open the low-voltage market by November 2027 and 2028, reallocate
  sector charges, set rules for storage and curtailment compensation, and change how old hydro concessions are renewed;
  the filer says they "materially altered competitive dynamics across the industry" (Item 4). This is change in the
  rules of a regulated industry, not a technology the forecast cannot follow: the wires, the dams and the lines stay,
  and the filer can state what each law does to each part. "we see lots of change coming, 9 times out of 10, we’re going
  to pass on that" **[M1999-063]** is weighed, and the change is carried to Q2, where change and the castle are judged.
- **Routing.** Not a bank; not a business whose ten-year economics a fast-moving technology hides. A doubt about the
  perimeter would close it **[M2002-092]**; the doubt here is about the returns, not about what drives them, and that is
  Q2's question.
- **VERDICT: IN.** The economics of each part are set by stated contracts, tariff formulas and concession terms that the
  20-F lays out **[M2012-065]**, **[M2008-033]**; the commodity price is not a Q1 stop **[M2016-025]**; Brazil asks a
  lower price, not a pass **[M2006-021]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

### The parts table (note 31, profit before financial results and taxes, R$ millions; 2021 and 2022 as restated in the 20-F FY2023, 2023 to 2025 from the 20-F FY2025)

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share of the four | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| GER generation (hydro, wind) | 2,890 | 1,354 | 1,823 | 1,144 | 2,134 | 9,345 | 42.1% | standing, protects ordinary returns (below) | **yes, the largest part** |
| DIS distribution | 1,167 | 485 | 1,103 | 1,982 | 2,078 | 6,815 | 30.7% | regulated monopoly to 2045; return set by ANEEL | no |
| TRA transmission | 1,424 | 1,288 | 906 | 1,112 | 960 | 5,690 | 25.6% | contracted RAP; return set at auction and review | no |
| COM trading | 58 | 124 | 109 | 15 | 53 | 359 | 1.6% | none; a middleman in a commodity | no |

No part carries more than half, so the largest decides: GER, by the business-of-parts convention, which reads the parts
separately because "lumping them together [...] impedes analysis" **[L2008-005]**. Read at the filer's coarser
segment level (GET = GER + TRA, 67.7% of the four), GET decides, and GER is 62% of GET, so the reading is the same:
generation decides. The GER figures carry one-offs in both directions: 2021 includes the R$ 1,570.5M GSF compensation
(Item 4, the 2021 MRE law); 2023 an impairment reversal of R$ 285.8M; 2025 the gains on the Baixo Iguacu sale and the
Maua step acquisition (R$ 335.6M and R$ 141.7M in the cash-flow reconciliation). Without them the five-year GER average
is about R$ 1,400M a year, not R$ 1,869M.

### The castle tests, on the deciding part
- **What keeps it standing, and how permanent** **[M1995-038]**. The three plants that are 82.8% of hydro capacity (Foz do
  Areia, Segredo, Salto Caxias) hold concessions to November 2054; no attacker can build another dam on the same reach of
  the Iguacu. The money test **[M2011-015]** passes for the dams. But the castle is the grantor's, not the company's:
  "Brazilian law requires that all of our generation, transmission and distribution concessions be subject to a
  competitive bidding process upon their expiration" (Item 4, Competition). COPEL kept the three plants in 2024 only by
  paying a grant bonus set by the government (R$ 3,719.4M by MME/MF Interministerial Ordinance No. 01 of 2023-03-30,
  paid as R$ 4,073.9M on 2024-11-21, Item 4 and note 16), and the 2025 framework lets the grantor "extend or tender" the
  remaining old plants, "establishing the estimated value of the concession, 50% of which will be allocated to the CDE",
  with the concessionaire to "assume the hydrological risk" (note on Law No. 15,269/2025). At each renewal the State
  charges for the castle what the castle is worth; what is left to the operator is a return on that price.
- **The rival named by the filer did the same.** AXIA (formerly Eletrobras) received new 30-year concessions for 22
  hydro plants on 2022-06-17 as part of its privatization, conditioned on CDE contributions, with the energy moved from
  the regulated price to "freely negotiated in the market" and the hydrological risk carried by AXIA (AXIA 20-F FY2025,
  filed 2026-04-24, `0001439124-26-000013`, Item 4, New Concession Agreements). The renewal-at-a-price is the field's rule,
  not one company's bargain.
- **Pricing power and the agony before a rise** **[M2005-020]**. None: the price is the market's. GER's average selling
  price rose 6.4% in 2Q26 to R$ 198.99/MWh while volume sold fell 7.8% (2Q26 release); the 20-F's risk factors name the
  PLD, the free market and "Excess supply of energy in the market, particularly as a result of new energy projects,
  incentivized renewable energy projects, including distributed generation" as forces that "may cause a decrease in the
  energy prices" (Item 3.D).
- **The customer and the low bid** **[L2004-003]**. Electricity has no brand; a free customer "may seek other energy
  suppliers upon the expiration of their contracts with us" (Item 3.D); COM's 1,537 free customers buy on price.
- **The low-cost position** **[L2004-007]**, **[M1997-010]**. Old hydro runs at low operating cost (GER's 2025 operating
  costs excluding energy bought were about R$ 57 per MWh generated: R$ 1,797.8M less R$ 518.9M over 22,450 GWh, note 31
  and Item 4), but every hydro in the MRE shares the same GSF, and the wind farms are being curtailed: 15.7% of output in
  2Q25 and 23.7% in 2Q26, by order of the ONS (2Q26 release). Whatever cost advantage the dams have is priced into the
  bonus at renewal; it does not stay with the owner. The filings read do not state a rival's cost per MWh, and the
  returns below are the evidence used instead.
- **Widening or narrowing** **[M1999-108]**. Narrowing for wind (curtailment rising, compensation still being
  regulated under Public Consultation No. 210/2025); for hydro, the renewal terms got harder (the 2025 law adds the
  hydrological risk and the CDE share).
- **What could destroy or reduce it** **[M2000-014]**: a renewal not granted or priced higher; a drought (2021's GSF
  crisis); oversupply. All three are named in Item 3.D.

### The field's returns over the last full cycle (judged in words, by the CONVENTION of section C: no figure)
Net income over year-end equity, R$ millions, from each company's own 20-F (COPEL: the FY2016 to FY2025 20-Fs; CEMIG:
20-F FY2025, filed 2026-04-17, `0001554855-26-000648`, and earlier years' XBRL from its 20-Fs, 2024 cross-checked to the
filed statement, R$ 7,119M and R$ 27,382M; AXIA: 20-F FY2025 `0001439124-26-000013`, earlier years' XBRL from its
20-Fs, 2024 cross-checked, R$ 10,381M and R$ 122,000M):

| | 2016 to 2025, NI / equity summed | 2021 to 2025 | Basis |
|---|---|---|---|
| COPEL | 23,421 / 200,736 = 11.7% | 10.6% (continuing operations; 12.1% with the 2021 telecom sale) | levered: debt 87% of equity at 2025 |
| CEMIG (named, Item 4) | 34,792 / 198,794 = 17.5% | 25,632 / 121,865 = 21.0% | levered; its own 20-F names a gain on the disposal of Alianca Geracao (2024) and PIS/Pasep-Cofins credit income among the items |
| AXIA (named, Item 4) | 64,711 / 828,847 = 7.8% | 30,688 / 540,413 = 5.7% | levered |
| Brazil's long fixed-rate bond (Tesouro, longest NTN-F, annual averages) | 10.9% | 12.0% | no risk, no leverage |

CELESC (named, Item 4) and Neoenergia (named as the seller of Ceu Azul) do not file with the SEC; flagged, not used.
**CONVENTION of this run:** the 20-F names no direct competitor that files with the SEC (its Competition section names
none by name); the rivals used are the two SEC filers the 20-F itself names among the industry's main participants
(Item 4, The Brazilian Electric Power Industry); rationale: they hold the same kind of hydro, transmission and
distribution concessions under the same grantor and regulator.

**The judgment.** Over ten years that take in the 2017 to 2018 and 2021 droughts and the wet years between, the filer
earned on its levered equity about what its own government's long bond paid with no risk and no leverage; over the last
five it earned less. The largest rival earned well below the bond in both spans. The one rival above it carries
disposal gains and tax-credit income its own filing names. On its unlevered capital the deciding part earns less still:
GER's profit before financial results, about R$ 1,400M to R$ 1,870M a year, against roughly R$ 13bn to R$ 14bn of plant
and concession rights (GET's PP&E and intangibles, note 31.2), is about 10% to 14% before tax and about 7% to 9% after
the 34% statutory rate, below the 12.0% bond average. That is a standing castle that protects ordinary returns, and the
reason is structural, in the filings: the grantor re-prices the castle at each renewal and the product is a commodity
sold at the market's price. "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**;
the moat must protect "excellent returns on invested capital" **[L2007-004]**, and this one does not. A return set by a
regulator is the framework's exception, which Q2's list carries to Q3 as a second best; it covers DIS and TRA, whose
castles stand on allowed returns: "there’s no way we get rich on our utility investments. But there’s no way we get
poor, either." **[M2009-104]**, **[L2009-012]**, and "You can't expect to earn outsized profits in regulated
utilities" **[L2005-005]**; but they do not decide. Generation is priced by a market, not allowed a return.

Not TOO HARD: the castle's future can be judged from the filings, because the concession terms, the renewal mechanism
and the field's returns are all stated; the tenuous-moat row sends a castle to TOO HARD because "We don’t know how to
valuate that" **[M2000-019]**, which does not apply where the returns are known.

- **VERDICT: OUT.** The deciding part, generation, is a standing castle that protects only ordinary returns: the grantor
  sells the right to the dams at its estimated value at each renewal and the energy is sold at the market's price, and
  over the full span the field's durable players, the filer among them, earned about the long government rate or less
  **[L2007-004]**, **[M2013-052]**, **[M2011-015]**; the regulated parts that are the exception **[M2009-104]** do not
  decide **[L2008-005]**.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2).
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the ten balance sheets were read in Step 0).
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED as a verdict; the figures are under COMPUTATION, NOT A CLEARANCE below.
## Q8, Q9, Q10, Q12. NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part, generation, is a standing castle that protects only ordinary returns (the grantor
re-prices the concessions at renewal; the energy is a commodity at the market's price; the field earned about the long
government rate or less over ten years). Computed value range, not a clearance: R$ -0.35 to R$ 2.31 a share on the
central all-equity basis (R$ 3.82 to R$ 7.95 equity-only) against R$ 17.70. Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*

**Bearing on Q3 (capital).** Capital spending (contract assets, PP&E, intangibles, the 2024 bonus excluded) averaged
R$ 2,350M a year over 2021 to 2025 against depreciation and amortization of R$ 1,316M, about 1.8 times; it rose to
R$ 3,110M in 2025. DIS's net regulatory asset base was set at R$ 19.9bn in the sixth periodic review (2026-06-23; X
factor 0.95%; a R$ 1.3bn tariff deferral applied; 2Q26 release). New growth spending began in 2Q26 on the capacity
reserve auction (LRCAP) at Foz do Areia and Segredo (R$ 317.9M in the quarter). The 2024 grant bonus spread over its 30
years is R$ 135.8M a year. Maintenance-only owner cash fell every year from 2022 to 2025 (table below) while revenue rose
5.6% a year.

**Bearing on Q4 (the accounts).** IFRIC 12 concession accounting: construction revenue and cost (R$ 3,272.8M in 2025),
contract assets, "Result of transmission concession contracts" (R$ -867.8M non-cash in the 2025 cash-flow
reconciliation), the regulator's replacement-value re-measurement (VNR) of the distribution assets; sectorial financial
assets and liabilities (CVA) of R$ -2,587.5M non-cash in 2025; PIS/Cofins credits owed to consumers. Each is explained
in the notes; no confusion was found in the notes read, but the reading stopped at Q2. The 2Q26 release headlines
"Recurring Ebitda R$ 1,612.6 million" and "Recurring Net Income R$ 645.1 million" against reported R$ 1,993.8M and
R$ 1,047.5M (here the recurring figures are lower than reported); the leverage target is stated on EBITDA (2.9 times
net debt to EBITDA). These are the habits that Q4 records as a weighing and carries to Q5 (an adjusted figure featured,
**[L2016-006]**; "a negative" and not "a total exclusionary factor" **[M1994-018]**). Cash taxes paid (R$ 198M in 2025)
are well below the book charge (R$ 578M), the gap being mainly deferred tax (R$ 381M); the book charge is itself
below 34% because of the interest-on-equity deduction (R$ 374M of tax effect, note 12.4); the JCP deduction is permanent law today and the 20-F names its possible repeal.

**Bearing on Q5 (integrity, recorded not judged).** (1) The adjusted "recurring" figures featured first in the results
release (above). (2) Executive Board compensation was R$ 10.0M in 2023, R$ 40.3M in 2024 and R$ 41.9M in 2025, the
"Others" line (bonuses, long-term incentives, pension) going from R$ 3.7M to R$ 32.1M and R$ 31.3M, after the company
ceased to be state-controlled (Item 6). (3) The performance-share programs vest on total shareholder return, a market
condition (Item 6, ILP). (4) The CEO, Daniel Pimentel Slaviero, is not on the Board; the chairman is Marcel Martins
Malczewski (Item 16G for the first; the board minutes on the 6-K of 2026-07-16 for the second). No search was made for earnings guidance or for a record of meeting targets;
the habit test of **[L2002-041]** was not run. Any later run that reaches Q5 must answer these **[M2013-088]**.

**Bearing on Q6 (the money and the owners).** Buybacks: 2,623,800 common at R$ 8.28 average (Dec 2024) and 3,544,700 at
R$ 8.52 (Jan 2025), plus preferred at R$ 8.66 and R$ 9.42, bought through B3 at market price (Item 16E). The program
named no price, which **[L2016-002]** weighs against unless the prices paid sit at or below the bottom of the Q7 range
**[L1999-023]**; every price paid is above the bottom of every computed case below (central bottom R$ -0.35,
equity-only bottom R$ 3.82). Dividends and interest on equity declared R$ 2,450M in 2025, plus a R$ 1,298M premium paid
to shareholders on the Novo Mercado migration (note 27.7), against net income of R$ 2,688M; the new dividend policy of
2026-07-15 ties payout to a leverage band of 2.6 to 3.2 times net debt to EBITDA. R$ 2.0bn of new shares were sold in the
2023 offering that ended state control.

**Bearing on Q9 (debt).** Total debt R$ 23,484.2M including swaps and net debt R$ 19,651.2M at 2026-06-30 (2Q26
release); no US-dollar debt (Item 5); average nominal cost 12.92%, 91.33% of the CDI; average term 5.2 years; CDI- and
IPCA-indexed (Item 3.D). Coverage on the speakers' definition, pre-tax earnings over interest **[L2012-002]**:
2025 profit before tax R$ 3,246.7M plus interest paid R$ 2,006.7M, over R$ 2,006.7M, is about 2.6 times. The distribution
concession's fifth addendum carries economic-financial efficiency covenants whose breach can end the concession (note
32.2.7). Provisions for legal claims rose from R$ 956.7M to R$ 1,934.0M non-current in 2025. Dam failure and strict
liability for outages are named risks (Item 3.D).

---
## COMPUTATION, NOT A CLEARANCE
*(The file closed at Q2. These figures are the owner's two reporting figures, built by Q7's text; no entry language,
no verdict.)*

**The owner cash, by year** (R$ millions; continuing operations; filed cash-flow statements: 2021 and 2022 from the
20-F FY2023, 2023 to 2025 from the 20-F FY2025; net cash from operating activities is after interest and income tax
paid, so it is the equity-only figure).

| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Net cash from operations, continuing | 2,859 | 3,725 | 3,393 | 3,390 | 3,028 | |
| less the CRC transfer to the State (one-off inside 2021) | -1,647 | | | | | |
| = operating cash used | 1,212 | 3,725 | 3,393 | 3,390 | 3,028 | 2,950 |
| capital spending (contract assets, PP&E, intangibles; 2024 bonus excluded) | 1,811 | 2,300 | 2,191 | 2,337 | 3,110 | 2,350 |
| lease principal | 49 | 57 | 69 | 71 | 70 | 63 |
| grant bonus spread, R$ 4,073.9M / 30 | 136 | 136 | 136 | 136 | 136 | 136 |
| **owner cash after all spending (equity-only)** | -783 | 1,232 | 997 | 846 | -286 | **401** |
| the same with the bonus charged in full in 2024 (literal window) | -648 | 1,368 | 1,132 | -3,092 | -151 | -278 |
| depreciation and amortization (the maintenance guess) | 1,017 | 1,233 | 1,382 | 1,465 | 1,482 | 1,316 |
| **owner cash after maintenance only (equity-only)**, D&A + leases + bonus spread (2025's D&A already amortizes it) | 10 | 2,299 | 1,806 | 1,718 | 1,477 | **1,462** |
| interest paid (loans, debentures, leases) | 542 | 1,247 | 1,673 | 1,594 | 2,007 | 1,412 |
| **maintenance-only, all-equity** (interest added back after 34% tax) | 368 | 3,122 | 2,910 | 2,769 | 2,801 | **2,394** |
| net revenue | 20,976 | 20,535 | 21,479 | 22,651 | 26,117 | |

How each specific was applied. **The four of the PG re-test:** growth on aggregate owner cash; all spending deducted,
with the maintenance case beside it and, here, central (specific (e)); zero nominal growth after year ten; a price above
the top closes OUT through the floor. **(a) cycle:** 2021 is aberrational on the filer's own description (the
hydrological crisis that created the Water Scarcity Account, Item 4) and carries the one-off CRC transfer; the five-year
average is kept as the base because the window runs from that drought through wet years and is the only cycle the
filings give, and the literal window is shown beside. **(b) decline and meaningless end years:** the end-year rate on the
maintenance series (10 to 1,477) is meaningless **[L2005-003]**, so growth is measured between the halves of the window
(average of 2021 and 2022 against 2024 and 2025): +11.4% a year equity-only, +16.9% all-equity. Beside it: from 2022 to
2025, the years after the trough, the same series fell 13.7% a year (equity-only) and 3.6% (all-equity); carried as the
bottom it gives R$ 1.75 a share equity-only and R$ -1.56 all-equity. **(c) acquisitions:** net deals over the window
(acquisitions of Aventura and SRMN, Ceu Azul and the Maua swap against the Baixo Iguacu and small-hydro sales) average
+R$ 5M a year, so deducting them changes nothing; not a serial acquirer. Discontinued operations (Copel Telecom sold
2021, Compagas and UEG Araucaria sold 2024) are left out of both the series and the deals. **(d) working capital:**
inside operating cash, counted. **(e) maintenance:** the filing states no maintenance figure; depreciation is used as
the guess **[M1998-127]**, the owner being "entitled to my best guess" **[M2000-144]**; the all-spending case is beside.
**(f) the cap:** all-equity growth of 16.9% exceeds the discount rate and, carried ten years, would need owner cash of
25.2% of sales against the highest 15.2% earned, so it is cut to the business's own sales growth, 5.6% a year
(2021 to 2025) **[M1999-067]**, **[M1997-095]**; the equity-only 11.4% passes both tests (9.5% of sales in year ten
against 11.2% earned) and is kept. **Whose tax:** cash tax as paid; the shelter is mainly the permanent JCP deduction,
not a carryforward running out inside ten years, so no statutory-rate recomputation.

**The basis, decided from the filing.** Q7's regulated-utility paragraph rests on the row's own exception, debt
"dedicated [...] to the fixed-asset commitments at our regulated utilities" **[L2017-012]**, and on the allowed return:
"when you get an allowed return in the electric utility you’re almost certain of earning it" **[M2010-037]**. The
paragraph puts the equity-only basis central where the deciding part earns a return a regulator allows on its invested
capital, and keeps merchant generation and unregulated renewables, priced by a market, on the all-equity basis. DIS and
TRA earn allowed returns; the deciding part, GER, does not: its energy is sold under bilateral contracts and auctions at
market prices, with hydrological risk and curtailment. So the central figure is the all-equity basis, "we evaluate
acquisitions on an all-equity basis" **[L2017-004]**, equity-only beside, and the regulated-utility credit is shown as a
third figure for the regulated parts' sake. Net debt: R$ 19,651.2M at 2026-06-30 (2Q26 release: total debt with swaps
R$ 23,484.2M less cash and securities R$ 3,833.0M); leases left out of net debt because their principal is charged in
owner cash; the R$ 706M interest on equity payable 2026-09-30 was declared before that date and is not borrowing.

**The rate and the floor.** Discounted at 12.87%, the long NTN-F **[L2000-021]**, **[M1996-025]**; the floor of about
ten percent **[M2003-149]**, tested first.

| Case | Owner cash base | Growth carried 10 years | Range a share at 12.87% | Fair price a share (ends at 10%, averaged) | Per ADS | Expected return at R$ 17.70, no growth / growth |
|---|---|---|---|---|---|---|
| **All-equity, maintenance-only (CENTRAL)** | 2,394 | 5.6% (cut from 16.9%) | **R$ -0.35 to R$ 2.31** | **R$ 3.35** | R$ 13.40 (US$ 2.64) | 3.3% / 5.2% |
| Equity-only, maintenance-only (beside) | 1,462 | 11.4% | R$ 3.82 to R$ 7.95 | **R$ 7.90** | R$ 31.62 (US$ 6.22) | 2.8% / 6.7% |
| Equity-only, all spending | 401 | 7.7% | R$ 1.05 to R$ 1.71 | R$ 1.82 | R$ 7.28 | 0.8% / 1.5% |
| All-equity, all spending | 1,333 | 5.6% (cut from 21.7%) | R$ -3.13 to R$ -1.64 | R$ -1.07 | R$ -4.27 | 1.9% / 3.0% |
| Equity-only, all spending plus the regulated-utility debt credit (net new debt R$ 793M a year credited, capped at the 50.4% debt share of capital) | 1,194 | 8.4% | R$ 3.12 to R$ 5.32 | R$ 5.59 | R$ 22.38 | 2.3% / 4.5% |
| Literal window, bonus charged in full in 2024 | -278 | none (negative base) | R$ -0.73 | R$ -0.94 | | none |

Shares 2,970.07M; ADS = 4 shares; US$ at PTAX 5.0826. The debt share for the credit is the business's own (debt
R$ 23,484M at 2026-06-30 over that plus equity R$ 23,092M at 2025-12-31), since the filings read state no allowed
regulatory debt share.

**What the computation shows.** No case earns the floor at the price: the best, equity-only maintenance-only with 11.4%
growth for ten years, returns about 6.7% at R$ 17.70, below both the ten percent floor and the 12.87% bond. Q7 would
close OUT on the floor test first, whatever the width **[M2003-149]**. The price is above the top of every case; on the
central basis it is more than seven times the top. Owner cash after maintenance is 2.8% of the market value
(equity-only) and 3.3% of the enterprise value (all-equity, R$ 72,221M). **The two reporting figures (COMPUTATION, NOT A
CLEARANCE):** (a) **value range R$ -0.35 to R$ 2.31 a share** (all-equity, maintenance-only, central), R$ 3.82 to
R$ 7.95 equity-only beside; (b) **fair price R$ 3.35 a share, R$ 13.40 an ADS** (all-equity, central), **R$ 7.90 a share,
R$ 31.62 an ADS** equity-only beside, after the company's own tax; against CPLE3 R$ 17.70 and ELPC US$ 13.97 (R$ 71.0 an
ADS).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      template copy, Q1, Q2, and the close, each a pathspec commit of the two paths only.
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was present (held by the
      dispatching session, pid 12768, 2026-10-18T15:16) and was not touched; the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` filtered
      to today's date showed other runs' names; declared under contamination at the top, not used. AXIA's and CEMIG's
      own 20-Fs were read as rivals' filings; the AXIAY run file was not opened.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `_research 2026-10-18 ELPC/check_ids.py`); every
      filing fact has its document and accession; numbers without a filing are labelled CONVENTION.
- [x] The order was kept; Q2's STOP closed the run; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from the filed cash-flow statements after every real cost, never a net-income proxy (operator rule 5);
      the sovereign from the Tesouro Nacional, dated; aggregator quotes flagged; PTAX from the Banco Central.
- [x] Contrary evidence written down as found (foundations line); facts for later questions under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` printed only UNRESEARCHED; nothing from it was used.
- [x] `python tools/check_framework.py` PASS before the closing commit; `check_ids.py`: 51 ids cited, 0 problems.
- Shortfalls, stated: trade receivables for 2015 to 2017 were not extracted; cash for 2015 to 2017 is from the XBRL tags
  of those filings, not read off the statements; CEMIG's and AXIA's figures before 2025 are their XBRL tags, with one year
  each cross-checked; GER's capital base is approximated from GET's segment assets (the note does not split GER from
  TRA); the 2Q26 interim financial statements were not found on EDGAR, so net debt is the release's figure; no search for
  earnings guidance was made.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The floor sits below the sovereign.** In BRL the long government rate (12.87%) is above the ten percent floor, so
the fair price (ends valued at 10%) is higher than the value range (ends at 12.87%), and a price could clear the floor
while losing to the government bond. The floor's rows tie the figure to a bond rate ("in a world of 7 percent
long-term bond rates" **[M1994-004]**), and Q8 would catch a loss to the bond, but Q7's convention says nothing for a
currency whose bond yields more than the floor. Here it did not matter (no case reaches even ten percent). (2) **(a) and
(b) collide on a drought trough.** When the first year of the window is a trough, (b)'s halves measure credits the
recovery as growth (+11.4% here) while the years after the trough show a decline (-13.7% a year); (a) asks for a cycle
base and growth between cycles, which one window cannot give. I kept the five-year base, used the halves rate as the
text directs, and showed the decline beside. (3) **The regulated-utility paragraph and the business of parts.** It
names "the deciding part"; when the filer's coarse segment (GET) mixes a regulated part (TRA) with a market-priced one
(GER), the paragraph does not say which reading of the parts governs the basis. Both readings made generation decide
here. (4) **The renewal bonus** is a once-in-thirty-years payment to keep a concession; the five-year window either
charges it all (owner cash negative) or none of it. I spread it over the term as a CONVENTION of this run; the framework
has no rule for a concession fee. (5) **The all-equity add-back** says "owner cash before interest and after the
company's tax" but not whether the interest tax shield is removed; I added interest back at (1 - 34%) and said so.
(6) **Rivals for a foreign filer.** The brief's rule (rivals the filing names, that file with the SEC) met a filing whose
competition section names no company; I used the SEC filers named among the industry's participants and confessed it.
