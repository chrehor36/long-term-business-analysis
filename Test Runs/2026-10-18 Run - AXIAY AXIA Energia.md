# Company Run — AXIA Energia S.A. (B3: AXIA3 / AXIA7; OTC ADS: AXIAY / AXICY) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to its dated name before any fetch.**

Formerly Centrais Elétricas Brasileiras S.A. - Eletrobras (renamed by the shareholders on 2026-04-15; brand AXIA from
2025-10-22). Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the one departure the brief states (the
lines of evidence are derived from the 20-F's Items 3.D, 4 and 5; see Step 0).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (1d2b382d):** not held; AXIA Energia (AXIAY, AXICY, AXIA3, AXIA7, formerly Eletrobras, EBR) does not appear in `PORTFOLIO.md`.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check that my own file name was
free showed the names of fifteen other run files and research folders dated 2026-10-18 (other utilities and gas companies:
AEE, AEP, AES, AQN, AVA, HOKCY, LNT, MDU, NJR, NWN, OGS, SR, SWX, UGI, XNGSY); no file of them was opened. (2) The session's
opening git status and recent commit subjects named research folders of other companies (AYI, ARCB) and one other run's
box line (AVA, OUT at Q7 on the floor). (3) The memory index loaded with the session carries general lines about the queue
(counts of gate-clearers, owed holding reviews); none names this company. (4) The `Screens/_daily/` listing showed the lock
file present (the dispatcher's). Nothing about AXIA, Eletrobras, EBR or AXICY in any other run file was seen. None of this
is used below.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price (primary market B3, reais):** AXIA3 (common) R$ 59.49, AXIA7 (class C preferred, PNC) R$ 59.99, closes
  2026-10-16 (last B3 session before this run's date); source: Yahoo Finance chart API, **an aggregator, flagged** (operator
  rule 5: aggregators for live quotes only). Beside it: OTC ADS AXIAY US$ 11.63 and AXICY US$ 11.64 (close 2026-10-16, same
  aggregator, flagged). Exchange rate: **PTAX selling rate 5.0826 BRL per USD for 2026-10-16, Banco Central do Brasil**
  (Olinda PTAX service, CotacaoDolarPeriodo). Check: R$ 59.49 / 5.0826 = US$ 11.70 per common share against US$ 11.63 for the ADS.
- **Shares by class.** 20-F cover (FY2025, filed 2026-04-24, accession `0001439124-26-000013`), outstanding at
  2025-12-31: 1,975,377,219 common; 142,559 class A1 preferred; 266,462,114 class B1 preferred; 589,277,795 class C
  preferred (PNC); 1 golden share (`python Screens/cover_shares.py AXIAY` printed the same lines and refused to add them).
  Issued at 2025-12-31 (20-F Item 10): 2,915,428,717 shares (2,028,544,286 common, 146,920 PNA1, 279,941,393 PNB1,
  606,796,117 PNC). **Later events:** the PNA1 and PNB1 were converted into common at 1.1 common each on the migration to
  B3's Novo Mercado (completed June 2026; Form 15F of 2026-08-07, accession `0001292814-26-004140`; 2Q26 release on 6-K of
  2026-08-06, accession `0001292814-26-004087`); PNC must be converted 1:1 into common or redeemed by the end of 2031, at
  least 4% of the original volume a year from 2026 (20-F Item 3.D). **The count used** is the company's own "Social capital,
  September 2026" table on its investor-relations site (https://ri.axia.com.br/en/axia/shareholding-structure-shareholding-composition/,
  read 2026-10-18; the company's own document in place of an accession, the company having ended SEC reporting):
  2,441,805,426 common of which 45,638,483 in treasury, and 386,839,004 PNC of which 7,053,382 in treasury, so
  **2,396,166,943 common + 379,785,622 PNC = 2,775,952,565 shares outstanding**. Both classes share in the earnings (the
  income statement reports one basic EPS for ON and PNC, R$ 2.29 for 2025), so both are counted. *Unreconciled:* the
  issued count after a 1.1 conversion of the year-end preferred would be about 2,943 million; the September table's issued
  total is 2,828.6 million. The gap (about 115 million shares, about 4% of the count) is not explained in any document read
  (sweep: the 2Q26 release for "outstanding", "share capital", "treasury", "PNC"; the IR PNC page carries no figures); the
  likeliest reading, a cancellation of treasury shares or PNC redemptions, is not confirmed. The September table is used
  because it is the latest the company states.
- **Market cap:** 2,396.17 million × R$ 59.49 + 379.79 million × R$ 59.99 = **R$ 165,331 million** (about US$ 32.5 billion
  at PTAX 5.0826).
- **Sovereign for the earnings currency (BRL):** **12.87%**, Tesouro Prefixado com Juros Semestrais (NTN-F) maturing
  2037-01-01, purchase rate ("Taxa Compra Manhã") of base date 2026-10-15, **Tesouro Nacional**, from the Tesouro
  Transparente dataset "Taxas dos Títulos Ofertados pelo Tesouro Direto" (PrecoTaxaTesouroDireto.csv, downloaded
  2026-10-18). Chosen because it is the longest-dated **nominal** fixed-rate bond the issuing authority offers and quotes;
  Q7's discount rate is nominal and "no real growth" after year ten is computed as zero nominal growth, so a nominal rate is
  the matching one. Beside it, not used: the longest inflation-linked bond, Tesouro IPCA+ com Juros Semestrais 2060-08-15,
  real 6.73%; the US 30-year is the wrong currency. `tools/sources.py` carries no BRL series.
- **Filings read** (operator rule 4): the FY2025 20-F (filed 2026-04-24, `0001439124-26-000013`: cover, Items 3.D, 4, 5,
  6B, 6C, 7B, 9, 10, the consolidated statements and Notes 12, 25, 27, 36); the FY2024 20-F (filed 2025-04-17,
  `0001410578-25-000792`, the SEC-investigation passage); the FY2023 20-F (filed 2024-04-25, `0001104659-24-052084`: the
  cash flow statements for 2023, 2022 and 2021 as restated, the segment note for 2022 and 2021, the privatization note on the
  new concessions); the FY2021 20-F (filed 2022-05-06, `0001104659-22-057076`, downloaded, consulted only through the XBRL
  figures it carries); the 2Q26 results release (6-K, 2026-08-06, `0001292814-26-004087`: balance sheet, income statement
  at 2026-06-30, events); the 1Q26 and 4Q25 releases (6-Ks `0001292814-26-002854` and `0001292814-26-000554`, downloaded,
  not relied on); the Form 15F (`0001292814-26-004140`). The SEC XBRL company facts (CIK 0001439124) were used for the
  2015 to 2024 balance-sheet and income series and checked against the filed statements. **Cross-check against the filed
  statement:** operating cash flow 2024 R$ 12,385,583 thousand in the FY2025 20-F's cash flow statement against
  R$ 12,386 million in XBRL; equity attributable to owners 2024 R$ 121,863,225 thousand against R$ 121,863 million: both
  agree. No proxy exists for a Brazilian foreign private issuer; pay is read from Item 6B.
- **`python tools/run.py AXIAY`** printed "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (the brief foresaw this
  for a 20-F filer in reais). **Every figure below is taken from the filed statements**, in R$ million.
- **Lines of evidence (the brief's stated departure):** derived from the 20-F's Item 4 (two segments, generation and
  transmission, plus "other activities"; the 2022 privatization and new 30-year concessions; the quota phase-out; the
  settlement with the Federal Government), Item 3.D (free-market price risk, hydrology, ANEEL regulation and the five-year
  review of assured capacity, the RBSE payments under TCU review, compulsory-loan litigation, SPE guarantees, Eletronuclear,
  the Novo Mercado migration and PNC conversion, the 10% voting cap and the golden share) and Item 5 (segment results,
  liquidity, capex split). Chosen lines: segments and margins 2021 to 2025; realized energy prices 2023 to 2025; the
  transmission regulatory remeasurements; the concession terms and the Law 14,182/2021 obligations; litigation and
  contingencies; debt, leases and the CDE obligations; buybacks, issuance and the PNC; pay; the Federal Government's
  remaining rights.

**Owner cash by year** (R$ million; continuing operations; all-equity basis = net cash from operating activities, plus the
marketable-securities purchases that 2021 and 2022 carried inside operating cash as restated, plus interest paid, less
property and equipment, intangible assets and transmission contract-asset construction, less lease principal, less
acquisitions and capital injections; equity-only basis = the same after interest paid other than the CDE interest, after
every CDE and river-basin payment, plus interest received on cash and securities, which the filer reports in investing):

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Net cash from operating activities, continuing | 7,566 | 8,104 | 8,235 | 12,386 | 14,510 |
| Capex (PP&E + intangibles + transmission construction) | 2,488 | 35,277 | 7,391 | 7,812 | 7,424 |
| of which the 2022 concession payment (intangibles; grant bonus R$ 26,623 million per the FY2023 20-F) | | ~31,935 | | | |
| Depreciation and amortization | 1,443 | 2,690 | 3,621 | 3,988 | 4,577 |
| Interest paid | 2,176 | 3,211 | 5,512 | 6,651 | 5,832 |
| Judicial-contingency payments (inside operating cash, kept as a cost) | 6,229 | 4,223 | 2,673 | 3,776 | 5,272 |
| **Owner cash, all-equity** | 6,521 | **-23,257** | 4,152 | 10,290 | 12,299 |
| **Owner cash, equity-only** | 5,606 | **-22,388** | 1,445 | 2,252 | 4,842 |
| Same, with the 2022 concession payment left out (all-equity / equity-only) | 6,521 / 5,606 | 8,678 / 9,547 | 4,152 / 1,445 | 10,290 / 2,252 | 12,299 / 4,842 |
| Net operating revenue | 34,627 | 34,074 | 37,159 | 40,182 | 41,282 |

Five-year averages: all-equity **2,001** (literal) and **8,388** (2022 payment left out); equity-only **-1,649** and
**4,738**. Stock pay is small and runs through equity (share remuneration program R$ 13.6 million in 2023, R$ 6.3 million in
2024, R$ 2.0 million in 2025, statement of changes in equity); options outstanding 10,592,687 at 2025-12-31 (Item 6B),
about 0.4% of the count, left in the share count's margin of error rather than added. Arithmetic in
`Test Runs/_research 2026-10-18 AXIAY/owner_cash.py`.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own this "if the market closed for five years" **[M1997-109]**, and for a
company that has just left the NYSE for an over-the-counter ADS and a B3 listing that question is close to literal. The
market serves and does not instruct; "It just tells us prices." **[M2006-077]**; the 2022 offering price of R$ 42 and
today's R$ 59.49 are prices, not evidence of value. Margin of safety: if the case needs pencil and paper "it ought to just
kind of scream at you" **[M1996-084]**. No macro enters: the Brazilian election of October 2026, the Selic rate and the
real are not forecast here, "macro conclusions are" set aside **[M2000-094]**; they enter only as the sovereign rate the
filing's currency carries and as properties of the business (inflation-indexed transmission revenue). Who is paid to tell
you: the company's own releases feature "Regulatory EBITDA" and "Adjusted Regulatory EBITDA" (Q4), and the shareholders
who sold in 2022 included the Federal Government, which is still the largest holder; neither is "impartial advice"
**[M2020-037]**. The analyst's habit: contrary evidence is written down "in the first 30 minutes" **[M1997-127]**.
**Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**): (1) owner cash in the equity-only basis averaged negative
over the literal window and was R$ 1.4 to 4.8 billion a year since the privatization, against a market value of
R$ 165 billion; (2) realized prices on contracted energy fell from about R$ 245/MWh (2023) to R$ 207 (2024) to R$ 181 (2025)
while Brazilian inflation ran positive; (3) the regulator cut transmission revenue already booked by R$ 4.1 billion in 2025;
(4) R$ 55.6 billion of contingencies rated "possible" and R$ 19.9 billion provisioned at 2025-12-31; (5) the chairman's own
companies hold service contracts with the company, amount not disclosed; (6) the BRL long sovereign, 12.87%, is above the
framework's 10% floor, so the bond itself clears the floor.

## THE STANDING RULE
The rule binds the buyer's conduct: "never going to risk what we have and need" **[M2012-081]**; "borrowed money has no
place in the investor's tool kit" **[L2014-005]**. A cash purchase of a listed share, unlevered and sized so that a total
loss is survivable, does not put the buyer at risk of ruin; a currency mismatch (a dollar-based buyer owning a real-based
business) is a loss risk, not a ruin risk, if unlevered. The target's own debt and exposures are Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning a fix on "what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**, found by "trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**.
- **What the business is (20-F Item 4, `0001439124-26-000013`).** The largest generator in Brazil, 43,872.3 MW, 17% of the
  country's installed capacity, 97.1% of its 2025 output hydroelectric; the largest transmission company, 70,238 km of Basic
  Network lines, 37% of the national grid; 8,973 MWavg sold in the free market in 2025. Net revenue 2025 R$ 41,282 million:
  generation R$ 23,840 million, transmission R$ 16,999 million, other R$ 443 million (Note 36). Since the privatization of
  2022-06-17 the Federal Government group holds 40.67% of the common (September 2026 IR table) with voting capped at 10%
  for any holder, three of ten board seats while it holds over 30% (the settlement ratified by the STF on 2025-12-11), and
  the golden share.
- **The key variables and how predictable each is.**
  1. *Transmission revenue (RAP).* Set by ANEEL for each concession, indexed to inflation, reviewed every five years; the
     renewed concessions (Law 12,783/2013) and the auctioned ones run 30 years. The cash received was R$ 14,833 million
     (2021), R$ 14,624 (2022), R$ 18,288 (2023), R$ 19,248 (2024), R$ 18,715 (2025). Predictable in level within a band the
     regulator sets; the 2025 remeasurement (-R$ 4,082 million) shows the band can move against the company.
  2. *Generation volume.* Assured capacity of the hydro plants, reviewed every five years, any single review limited to a 5%
     cut and the total to 10% of the original (FY2023 20-F risk factor); hydrology (GSF) moves the energy actually
     delivered. Predictable within a narrow range over ten years.
  3. *Generation price.* The quota energy moves to free-market prices in five annual steps (100% in quotas in 2022, 0% from
     2027; Item 4A), so by 2027 almost all of the hydro energy is sold at negotiated or spot prices. Not predictable: the
     filer itself lists "projections of future energy price curves which do not materialize" among its risks, and the
     speakers say "we are not two fellows who think we can predict the price of soybeans or corn or oil" **[M2016-025]**.
  4. *Legacy costs.* The compulsory-loan litigation (provision R$ 11,058 million), the Law 14,182/2021 obligations
     (R$ 43,767 million, scheduled to 2047), pensions. Knowable from the notes, with stated schedules.
- **Routing.** The framework sends a dependence on a commodity price away from Q1: it is "never by itself a STOP at Q1 or
  Q2", and Q1 asks whether the business can be understood from its figures, "off the figures" **[M2008-069]**. The volume
  and the regulated half can be foreseen; the price of energy enters at Q2 (the low-cost position) and at Q7 (the cycle
  base and the width). The change in the industry is real (curtailment, the 2025 Laws 15,235 and 15,269 opening the market)
  but it is change in prices and rules, not a technology that makes the plants obsolete: a reservoir hydro plant does the
  same job in 2036 that it does today, and the insiders do write the ten-year view down (ANEEL's tariff methodology, the
  company's own price curves), unlike the field in which they "would not want to put down on paper their predictions"
  **[M2000-105]**.
- **Abroad.** "where we think we understand the nuances of the corporate governance system and taxation" **[M2000-141]**.
  The governance (voting cap, golden share, three government seats, the 2023 constitutional challenge settled in 2025) and
  the tax (the 75% IRPJ reduction for the Nordeste and Norte subsidiaries; deferred tax assets of R$ 17.5 billion) are
  disclosed and readable. The speakers name this very country: "Brazil would not be off limits at all", with the condition
  "We would want it to be cheaper than if it were in the United States." **[M2006-021]**; that condition is carried to Q7.
- **"how far off we can be"** **[M2011-084]**: narrow on volume and on regulated revenue, wide on the free-market price;
  the width is Q7's to measure.
- **Contrary evidence written down** ("write it down in the first 30 minutes" **[M1997-127]**): "if you have doubts about something being into your circle of
  competence" **[M2002-092]**, it is outside. My doubt is about the price of energy and the regulator's discretion, not
  about what the business is or how its figures arise; the framework places exactly that doubt at Q2 and Q7, not here. A
  second analyst could close this TOO HARD (NATURE) on the price of energy; I do not, because the routing paragraph forbids
  closing on the commodity price at Q1.
- **VERDICT: IN.** The ten-year economics are a regulated, inflation-indexed transmission revenue plus a hydro fleet of
  known volume selling at a price that cannot be forecast but can be bounded; the business can be understood "off the
  figures" **[M2008-069]**, and the answer to "can I understand it?" **[M1995-051]** is yes.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. The moat is what "protects excellent returns on invested capital"
**[L2007-004]**.

**The parts table** (operating profit before the financial result, Note 36 of the FY2025 20-F and Note 34 of the FY2023
20-F; R$ million):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five years | Share of the two operating parts |
|---|---|---|---|---|---|---|---|
| Transmission | 14,438 | 3,923 | 7,239 | 13,606 | 3,154 | **42,360** | **65%** |
| Generation | 8,416 | 5,521 | 4,588 | 6,333 | -1,741 | 23,117 | 35% |
| Administration / other activities | -13,071 | -4,281 | -810 | -193 | 680 | -17,675 | (not a business part: holding costs, compulsory-loan provisions) |

Two checks on the split: transmission's figures carry the regulatory remeasurements (a gain of R$ 4,859 million in 2021,
R$ 365 million in 2022, R$ 6,130 million in 2024, a loss of R$ 4,082 million in 2025), and generation's 2025 figure carries
the loss on the agreed sale of Eletronuclear (Note 36's footnote; impairment R$ 7.2 billion, Item 5B). Taking both out,
transmission is about R$ 35.1 billion and generation about R$ 30.3 billion over the five years: transmission still carries
more than half (about 54%). **Transmission decides** under the business-of-parts convention; "lumping them together [...]
impedes analysis" **[L2008-005]**. Generation is read below as the part that does not decide.

**Transmission, the deciding part: the castle tests, each with its filing fact (20-F `0001439124-26-000013`, Item 4).**
- *The attacker with money.* "could I do it?" **[M2011-015]**. No: an existing line is held under an ANEEL concession and
  is not duplicated; a rival cannot build a parallel line into the same revenue. The attacker competes only where new lines
  are tendered, and there the lowest bid wins: AXIA won lots 8, 9 and 10 of Transmission Auction 01/2026 for an added RAP of
  R$ 50.8 million on R$ 668 million of investment (2Q26 release, `0001292814-26-004087`). The castle is the existing
  network, not the next line.
- *Pricing power and the agony before a rise.* None in the speakers' sense: "a prayer session before you raise your prices
  a penny" **[M2005-020]** is not even available, because ANEEL sets the RAP. What the contract gives instead is
  indexation: the 2025-2026 cycle added R$ 913 million for IPCA or IGP-M inflation (Item 4, Transmission Revenue). Through
  the inflation of 2021 to 2023 the RAP cash received rose from R$ 14,833 million to R$ 18,288 million (cash flow statements).
- *Would the customer choose it over the low bid?* The users of the grid pay a tariff and have no choice; the question
  only bites at the auction, where the bid is the low bid.
- *The low-cost position and the brand:* not applicable to a regulated wire.
- *Widening or narrowing* (knowing "how wide the moat is" **[M1999-108]**): narrowing at the regulator's hand. The approved
  RAP fell from R$ 17.6 billion (2024) to R$ 16.5 billion (2025), -5.9%: inflation +R$ 913 million and new reinforcements
  +R$ 283 million against a cut of R$ 1.4 billion when ANEEL "partially" accepted large consumers' requests to reconsider
  the RBSE financial component, and a further R$ 201 million of asset-base adjustments. The RBSE payment is also "subject
  to analysis by the TCU (proceeding 012.715/2017-4)", undecided (Item 3.D). For the renewed concessions the filer states
  that each periodic review takes in the non-depreciated assets, "resulting in a periodic decrease of RAP", which only new
  investment offsets (Item 4).
- *What could "destroy, or modify, or reduce the economic strengths"* **[M2000-014]**: a regulator that cuts what it
  granted (the 2025 events), the end of the concession terms (each 30 years; 56,971 km of the company's own lines are
  concessions renewed under Law 12,783/2013), and the "efficiency and tariff affordability" ANEEL weighs at each review
  (Item 4).
- **The field's returns, and why they do not close the file here.** A return set by a regulator is the stated exception to
  the ordinary-returns OUT, carried to Q3 as a second best: "no way we get rich on our utility investments"
  **[M2009-104]**; "decent returns on the incremental sums they invest" **[L2009-012]**. The speakers also record that the
  compact can break: "I did not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**,
  and that in utilities "the compact has been that you get a modest return" **[M2024-011]**.

**The competitor row** (CONVENTION of this run, as the brief directs: the 20-F names no rival; a text sweep of the FY2025
20-F for "competit" found none named. I chose the two Brazilian electricity companies that file 20-Fs with the SEC, CEMIG
(CIK 1157557) and COPEL (CIK 1041792); both are integrated, with distribution, so they are a field comparison, not a
like-for-like transmission comparison. Rivals not filing with the SEC and not read: ISA Energia Brasil (named in the 20-F
only as the counterparty of the IE Madeira and IE Garanhuns swap), Taesa, Engie Brasil Energia, CTG Brasil, Auren. Metric:
net income to owners over average owners' equity; 2017 to 2024 from the SEC XBRL facts as first filed for each year, 2025
from each FY2025 20-F; CEMIG's 2021 figure is tagged negative in XBRL and is taken as +R$ 3,753 million total net income from
its FY2023 20-F, `0000950170-24-050630`.)

| ROE % | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|---|---|---|---|
| AXIA (Eletrobras) | -4.1 | 27.1 | 16.9 | 8.8 | 7.5 | 3.9 | 4.1 | 8.9 | 5.5 | **8.7** |
| CEMIG (`0001554855-26-000648` for 2025) | 7.3 | 11.8 | 20.5 | 17.2 | 20.3 | 19.8 | 24.8 | 27.4 | 17.5 | **18.5** |
| COPEL (`0002070979-26-000155` for 2025) | 7.5 | 9.2 | 12.4 | 21.0 | 24.2 | 5.4 | 10.4 | 11.3 | 11.0 | **12.5** |
| Longest NTN-F yield, yearly average (Tesouro Nacional) | 10.25 | 10.59 | 7.85 | 7.34 | 9.69 | 12.31 | 11.79 | 11.85 | 14.14 | **10.65** |

Over the span AXIA earned on its book equity less than the government paid on its longest nominal bond in six of nine
years, and less on average, while the two state-influenced rivals earned more. AXIA's 2018 and 2019 figures carry RBSE
catch-up and gains; its 2022 to 2025 figures carry the R$ 75.0 billion of new-concession cost put on the balance sheet in
2022 (grant bonus R$ 26.6 billion, CDE obligation R$ 33.7 billion, river-basin obligation R$ 6.7 billion, credits R$ 8.0
billion; FY2023 20-F, note on the new concession agreements).

**Generation, the part that does not decide.** A commodity: the customer buys energy on price, as "most insureds don't care
from whom they buy" **[L2004-003]**. Realized price on contracted supply (Item 4, sales table): R$ 17,030 million on 69.4 TWh
in 2023 (about R$ 245/MWh), R$ 18,812 million on 90.9 TWh in 2024 (about R$ 207/MWh), R$ 18,311 million on 101.4 TWh in 2025
(about R$ 181/MWh), falling while inflation was positive, as the quota energy moved into the free market; the spot price
(PLD) averaged R$ 126/MWh in 2024 and R$ 202 in 2025 (Item 5). The way through a commodity is "to be the low-cost operator"
**[L2004-007]**, measured "more by cost of production than we would by whether copper was selling" **[M2006-004]**. The filer
calls hydro "our most cost-efficient energy source" (Item 4); a reservoir fleet of 43 GW cannot be rebuilt in Brazil today,
and its flexibility gains value as solar and wind add curtailment. Against that, the 2022 concessions put about R$ 75
billion of cost on the same plants for 30 years. No rival's unit cost was read from a filing (CEMIG and COPEL do not report
a comparable cost per MWh in the sections read), so the low-cost position is **not shown either way**. Generation is not
shown open on the evidence and does not decide; it is carried to Q7 inside the consolidated owner cash.

**Contrary evidence written down** ("write it down in the first 30 minutes" **[M1997-127]**): the deciding castle's returns are the regulator's to set and the
regulator cut them in 2025; the company's own returns over nine years sit below the risk-free rate in its currency; the
part that sells a commodity saw its realized price fall by about a quarter in two years.

- **VERDICT: IN**, on the deciding part. The transmission castle stands: the existing network cannot be crossed by an
  attacker with money ("could I do it?" **[M2011-015]**), and it protects a return the regulator sets, which the framework carries to Q3 as a
  second best rather than closing OUT ("no way we get rich on our utility investments" **[M2009-104]**; "decent returns on
  the incremental sums they invest" **[L2009-012]**). It is narrowing at the regulator's hand ("adverse developments in
  regulatory returns" **[L2023-011]**), and that is weighed at Q3 and in Q7's width, not here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"Has it earned high returns on capital?" **[M1995-051]**, on "the capital actually needed in the business" **[M2010-090]**.

- **Return on the capital needed, earnings after depreciation against capital employed.** Capital employed (all-equity):
  owners' equity plus borrowings, leases and the Law 14,182/2021 obligations, less cash and marketable securities. At
  2025-12-31: 118,502 + 74,296 + 489 + 43,767 - 16,418 - 11,857 = **R$ 208.8 billion**; at 2024-12-31 about R$ 204 billion
  (FY2025 20-F balance sheets). Operating profit before the financial result, 2021 to 2025: 9,783; 5,164; 11,668; 19,746;
  2,093; average **R$ 9.7 billion**, about **4.6% pre-tax** on that capital; adding the equity-method results (2,062 in 2023,
  2,503 in 2024, 1,854 in 2025), which come from about R$ 24 billion of the same capital, does not move it above 6%.
- **Cash earnings against capital spending.** Operating cash before interest (operating cash plus interest paid) was
  about R$ 13.7 billion in 2023, R$ 19.0 billion in 2024 and R$ 20.3 billion in 2025, against capex of R$ 7.4 billion,
  R$ 7.8 billion and R$ 7.4 billion: the business spends between a third and a little over a half of its pre-interest operating cash
  to keep and extend the assets, before a single real of interest or CDE instalment.
- **Reinvestment to stand still.** The filer states that each periodic review of the renewed transmission concessions
  takes in the non-depreciated assets, "resulting in a periodic decrease of RAP", offset only by new investment (Item 4);
  in 2025 the approved RAP fell 5.9% while the company spent R$ 4.9 billion on transmission construction. Generation spent
  R$ 1.3 billion of R$ 1.4 billion on maintenance (Item 5B). This is the pattern the speakers avoid, "a lot of compulsory
  reinvestment just in order to stand still" **[M1997-016]**, and the utility pattern the 2011 letter names: "To earn more,
  their owners must invest more." **[L2011-019]**. Depreciation (R$ 4.6 billion in 2025) understates the need: capex has
  run at 1.6 to 2.0 times depreciation since 2023, against the yardstick "amounts equal to our depreciation charge simply to
  stay in the same economic place" **[L2000-035]**.
- **What the added capital earns.** The 288 transmission reinforcement projects under way: added RAP of R$ 2.0 billion for
  R$ 15.5 billion of capex between 2026 and 2030, a gross revenue yield of about 12.9%, inflation-indexed, before O&M and
  tax; the 2026 auction lots: R$ 50.8 million of RAP for R$ 668 million, about 7.6% gross (2Q26 release). Against a long
  sovereign of 12.87% nominal (6.73% real), these are fair regulated returns at best, the second best the speakers accept
  only on "decent returns on the incremental sums they invest" **[L2009-012]**; "whether that’s good or bad depends on what
  we earn on that incremental" capital **[M2001-019]**.
- **The growth arithmetic.** Net revenue grew from R$ 34.6 billion (2021) to R$ 41.3 billion (2025), about 4.5% a year;
  the privatization's quota phase-out lifted the generation part's revenue (to 2027), and that uplift was bought with the
  R$ 75 billion of concession cost of 2022. Earnings rising after capital is put in prove nothing by themselves: "we’re not
  earning a higher rate of return on capital than we were when we started" **[M2023-081]**.
- **Time.** "if you have a business that’s earning 5 or 6 percent on equity and you hold it for a long time, you are not
  going to do well in investing" **[M1998-006]**: AXIA's return on book equity averaged 6.0% over 2021 to 2025 (Q2 table).
- **WEIGHS AGAINST.** A capital-heavy business that must keep investing to hold its regulated revenue, earning about 5% on
  the capital it needs in a currency whose government pays 12.87%; the second best is accepted only on "decent returns on the
  incremental sums they invest" **[L2009-012]**, and "cash-consuming businesses, by their nature, are unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**; the record here does not show it. (The "little or no debt" criterion is
  applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** ("balance sheets over an 8 or 10 year period before I
even look at the income account" **[M2025-032]**). R$ billion at 31 December; 2016 to 2024 from the SEC XBRL facts (latest
filed value for each date), 2025 from the FY2025 20-F balance sheet; 2024 checked against the FY2025 20-F (total assets
289.871, equity to owners 121.863: agree).

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 170.5 | 173.0 | 181.7 | 178.6 | 179.0 | 188.3 | 270.2 | 267.1 | 289.9 | 279.7 |
| Cash and equivalents | 0.3 | 0.6 | 0.6 | 0.3 | 0.2 | 0.2 | 10.7 | 13.0 | 26.6 | 16.4 |
| Marketable securities (where tagged / filed) | 2.3 | 7.2 | 6.0 | 5.9 | n/t | n/t | 0.4 | n/t | 9.4 | 11.9 |
| Trade receivables (current) | 4.4 | 4.7 | 4.1 | 5.3 | 6.0 | 5.1 | 4.8 | 5.2 | 5.9 | 5.6 |
| Transmission contract assets | n/t | 51.0 | 50.3 | 49.5 | 51.4 | 59.5 | 61.1 | 61.2 | 67.4 | 64.3 |
| Intangible assets (concession rights; no material goodwill) | 0.8 | 0.8 | 0.7 | 0.8 | 0.8 | 5.0 | 80.0 | 79.9 | 78.2 | 76.6 |
| Property, plant and equipment | 26.8 | 28.0 | 32.4 | 33.3 | 32.7 | 33.4 | 34.7 | 35.8 | 36.9 | 39.7 |
| Deferred tax assets (gross) | 3.7 | 3.6 | 4.0 | 7.4 | 9.7 | 8.9 | 11.0 | 6.7 | 5.7 | 17.5 |
| Borrowings (loans, financing, debentures) | 45.6 | 45.1 | 54.8 | 47.9 | 47.0 | 44.0 | 59.1 | 59.5 | 75.6 | 74.3 |
| Law 14,182/2021 obligations (CDE, river basins) | | | | | | | n/t | 39.5 | 42.0 | 43.8 |
| Litigation provisions | 20.7 | 24.6 | 24.1 | 25.2 | 25.8 | 33.4 | 33.3 | 26.5 | 23.4 | 19.9 |
| Equity to owners | 44.2 | 43.4 | 55.2 | 70.7 | 73.5 | 76.1 | 110.5 | 112.3 | 121.9 | 118.4 |
| Issued capital | 31.3 | 31.3 | 31.3 | 31.3 | 39.1 | 39.1 | 69.8 | 70.1 | 70.1 | 100.1 |
| Shares issued (million) | 1,352.6 | 1,352.6 | 1,352.6 | 1,352.6 | 1,568.9 | 1,568.9 | 2,301.2 | 2,307.1 | 2,307.1 | 2,915.4 |

(n/t: not tagged in XBRL and not read from the filed statement for that year.)

**What moved and why.** (1) *Equity against intangibles.* Equity to owners nearly trebled, from R$ 44 billion to R$ 118
billion, but R$ 38.5 billion of it is new capital (R$ 7.75 billion in 2020, the conversion of the Federal Government's
advances; R$ 30.6 billion in the 2022 privatization offering) and the R$ 30 billion step in 2025 is a reclassification of
reserves into the PNC bonus shares, not new money. In 2022 the intangibles jumped by R$ 75 billion: the new 30-year hydro
concessions, paid with the offering's cash (grant bonus R$ 26.6 billion) and with R$ 40.4 billion of new obligations to the
CDE and the river basins. So the privatization put roughly R$ 75 billion of purchased concession on the balance sheet and
about R$ 40 billion of debt-like obligation beside it; tangible equity (equity less intangibles) is about R$ 42 billion.
Purchased concession value is set aside in judging the business and counted in judging the capital allocation, "because we
paid for it" **[M2011-060]**. (2) *Cash.* From almost nothing before 2022 to R$ 10.7 to 26.6 billion after; the 2024 peak
came from R$ 30.0 billion of new borrowing in that year, and 2025's fall from R$ 12.2 billion of dividends paid. (3)
*Receivables* sit at about 9 to 16% of revenue across the decade (13.5% in 2025); nothing building. (4) *Debt:* borrowings stayed near R$ 45
to 55 billion until 2021, then rose to R$ 74 to 76 billion, with the Law 14,182 obligations on top: financial obligations of
about R$ 118 billion against R$ 46 billion in 2016. (5) *Retained earnings:* net income to owners over 2016 to 2025 summed to about R$
64 billion; equity grew R$ 74 billion, of which about R$ 38 billion was paid in, so about R$ 28 billion of the earnings went
out as dividends, buybacks and other movements. (6) *Deferred tax
assets* trebled in 2025, from R$ 5.7 billion to R$ 17.5 billion gross (Note 12: R$ 3,355 million on tax losses and
R$ 10,337 million on temporary differences recognized because management "reassessed its projected future taxable income",
citing among other things "the projected evolution of energy prices"); realization is expected "through 2047, without
assuming concession renewals" beyond transmission's expiry in 2042 and generation's in 2052. (7) *Litigation provisions*
peaked at R$ 33 billion in 2021 and 2022 and are being paid down, R$ 2.7 to 6.2 billion a year in cash.

**"what the figures are saying and what they don’t say and what they can’t say"** **[M2025-032]**. They say the business
throws off R$ 20 billion a year of operating cash before interest and spends R$ 7 to 8 billion of it on assets. They do not say
what the transmission business earns in a year: under IFRS its revenue is recognized as construction and as interest on a
contract asset, then remeasured when ANEEL changes the RAP (+R$ 6.1 billion in 2024, -R$ 4.1 billion in 2025); the speakers
name exactly this kind of account, "anything where you’ve got construction in progress or progress payment-type things"
**[M2013-086]**. The cash flow statement shows the RAP actually received (R$ 18.7 billion in 2025), and owner cash is built
from that, not from the accrual. They cannot say what 2025 earned: a pre-tax loss of R$ 6,980 million became a net profit of
R$ 6,560 million through a deferred-tax credit of R$ 13,873 million resting on management's price projections; and the
R$ 7.2 billion Eletronuclear loss sits inside "operating expenses".

**The real costs.** Depreciation is real and here it is short of the need (capex 1.6 to 2.0 times depreciation since 2023;
Q3): "almost always true costs" **[L2015-004]**; "depreciation is an economic cost every bit as real as wages, materials, or
taxes" **[R1996-023]**. The recurring "one-time": operating provisions were charged in every year read
(R$ 14.9 billion in 2021, R$ 6.9 billion in 2022, R$ 2.5 billion in 2023, a net R$ 0.6 billion in 2025), the R$ 7.2 billion
impairment of 2025, voluntary-dismissal plans in 2024 and 2025 (Item 6D); the judicial payments are recurring cash and are kept in owner cash.
Stock pay is small (Step 0). **EBITDA in the filer's own mouth:** the 2Q26 release (`0001292814-26-004087`) uses "EBITDA" 27
times, featuring "Regulatory EBITDA", "Adjusted Regulatory EBITDA" and "Adj Net Debt/Adjusted LTM EBITDA"; it does state
IFRS net income in its opening paragraph. "The one figure we regard as utter nonsense is the so-called EBITDA"
**[M1998-086]**; a management "highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**. No earnings
guidance was found (sweep: "guidance" in the 20-F and the 2Q26 release; the hits are about compliance training and tax).

**Is it confusion or suspicion?** The transmission accounting and the 2025 tax credit are hard, but each is explained in
its note and each can be stepped around by reading the cash flow statement, so the accounts do not "confuse" in the
speakers' sense, "when the accounting confuses you, I would just tend to forget about it" **[M1995-063]**. The tell the
speakers name, "deferred asset accounts start building up suspiciously high" **[M1995-064]**, is present in form (the
deferred tax asset trebled) and is disclosed with its reasons, audited, and non-cash; it is "the most optimistic
interpretation" **[M1994-079]** of the year in the sense that it rests on management's own price curve. I record it as a
weighing against, not as the suspicion that closes the file: it moves no cash and no figure used below. The unreconciled
share count (Step 0) is a gap in my reading, knowable from CVM filings not read; it does not touch the accounts.

- **VERDICT on the accounts: WEIGHS AGAINST.** Not a STOP: the cash statements are clear and owner cash is built from
  them. Against: income that depends on regulatory remeasurement and deferred-tax judgment, recurring "one-time" charges,
  and EBITDA featured in the releases, which is "a negative" but not "a total exclusionary factor" **[M1994-018]** and is
  carried to Q5. The recast owner cash (Step 0) feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet: "We read annual reports. We read about competitors."
**[M2007-081]**. The two yardsticks: "how well they run the business" **[M1994-008]**, read against "the hand they were dealt"
**[M1994-008]**, and how they treat the owners.

- **Who.** CEO Ivan de Souza Monteiro since 2023-08-14 (board member from August 2022, chairman until he became CEO;
  previously CEO and CFO of Petrobras, CEO of Credit Suisse Brasil; Item 6A). Chairman Vicente Falconi Campos, elected 2022,
  founder of the consultancy Falconi Consultores. Ten directors, three appointed by the Federal Government under the 2025
  settlement (Silas Rondeau, Nelson Hubner, Mauricio Tolmasquim, elected at the 2025 meeting).
- **The hand dealt and the record (ability).** The management took over a company privatized in June 2022 with 2021
  litigation provisions of R$ 33 billion, a quota-regime generation business, thermal plants, the Eletronuclear and Angra 3
  commitments and a constitutional challenge from the President (ADI 7,385, 2023). In three years: the thermal plants sold
  (R$ 4.7 billion with earn-out, 2024 agreement), Eletronuclear's investment agreement suspended and the stake's sale agreed
  (the R$ 7.2 billion loss taken in 2025), the ADI settled and ratified by the STF (2025-12-11), compulsory-loan provisions
  cut from R$ 13.7 billion to R$ 11.1 billion largely through judicial settlements (Note 27), voluntary-dismissal plans in
  2024 and 2025, Furnas merged in 2024, the share classes collapsed into common and PNC on the Novo Mercado (2026), the IE
  Madeira and IE Garanhuns swap closed with R$ 1.167 billion received (2Q26). Against it: the return on equity in those
  years was 3.9% to 8.9% (Q2), below the sovereign every year.
- **Integrity: the tests.** "see how they treat themselves versus how they treat the shareholders" **[M1994-009]**.
  1. *Pay* (Item 6B): total management pay R$ 77.0 million in 2025 (R$ 65.8 million for the executive officers),
     R$ 74.1 million in 2024, R$ 94.0 million in 2023; about 1.2% of 2025 net income. Options struck at not less than the
     R$ 42 offering price, indexed to IPCA plus a spread, 3-to-5-year vesting, 180-day lock-up after exercise; from 2026 a
     performance-share plan paying on total shareholder return. Weighed at Q6, Part B.
  2. *Related parties* (Item 6C): at 2025-12-31 "two contracts in place with companies owned by Mr. Vicente Falconi,
     Chairman", one for software licensing that covers, among other things, "variable compensation" (renewed through
     February 2027), one for consulting on "a strategic execution culture" (expired January 2026). **No amount is
     disclosed** in the 20-F (sweep: every "Falconi" in the document, Items 6A, 6C, 6E and 7B). The chairman's own firms
     selling to the company, including a tool for setting the pay of its people, is a fact about how the board treats
     itself; it is disclosed and policy-reviewed (Item 7B, TPR Policy).
  3. *The habits carried from Q4:* EBITDA variants featured in the releases, no earnings guidance found. "things that they
     do in public in relation to their investors and the promises they make" **[M2004-067]**: the releases state IFRS net
     income first and reconcile the regulatory figures (2Q26 Appendix 9).
  4. *Ownership:* the CEO holds 243,120 shares (about R$ 14 million), the chairman 7.7 million preferred through funds
     (about R$ 460 million), director José João Abdalla Filho 129 million shares through his funds (about R$ 7.7 billion),
     held through investment funds (Item 6E), which reads as bought, not granted: "huge and true ownership interests" **[L2002-033]**
     are present on the board.
  5. *The record of the company before this management:* the Angra 3 corruption investigations begun in 2015 (FY2023 20-F, risk factors), and an SEC Division of Enforcement inquiry from 2021 into the compulsory-loan disclosures, closed on 2025-04-01
     with notice that it "did not intend to recommend enforcement action" (FY2025 20-F, Item 8). Neither is the present
     management's conduct; both are written down.
  6. *Clear speech:* the 20-F's strategy and culture sections are written in consulting language ("Innovation Powerhouse",
     "high-performance culture", "Vision 2028"); "a standardized bunch of popular jargon that looks like it came out of the
     same consulting firm" **[M1998-038]** is a turnoff, not a finding of dishonesty.
- **Contrary evidence written down** ("write it down in the first 30 minutes" **[M1997-127]**): the chairman's firms' contracts with undisclosed amounts; the 2025
  deferred-tax recognition resting on management's own price curve (Q4); a government holder with three seats that is also
  the policy-maker, so that where "shareholders or somebody else has to suffer" **[M1998-121]** the choice may not fall on
  the consumer.
- **VERDICT on integrity: IN.** No fact found shows dishonesty in the present management: the related-party contracts are
  disclosed and governed by policy, the accounts reconcile, no guidance game is played, and the board's largest holders
  bought their shares. "If you’ve got doubts, forget it." **[M2013-088]**: the doubt I hold is about the board's
  independence and the government's conflicting interest, which is a weighing at Q6, Part B, not a doubt about honesty.
  **Ability WEIGHS FOR**, modestly: a hard hand played competently for three years, on a business whose returns remain
  low; "we still look to the underlying business, though" **[M1996-037]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test.** "whether retention, over time, delivers shareholders at least $1 of market value for each $1
  retained" **[R1995-009]**, and if not, after "three or four years [...] the presumption becomes very strong at that point
  that we should start paying out money" **[M1998-110]**. Since the privatization offering of June 2022 at R$ 42 a share:
  net income to owners of about R$ 23.3 billion (half of 2022, then 2023 to 2025), dividends paid of about R$ 15.1 billion
  and buybacks of R$ 2.1 billion (cash flow statements), so about R$ 6 billion retained, near R$ 2.6 a share. An original
  share is now one common share plus 0.263 PNC from the December 2025 bonus (606.8 million PNC on 2,308.6 million shares),
  worth about R$ 75 at today's prices against R$ 42 then, before the dividends received. **The market leg passes by a wide
  margin.** The intrinsic leg, which the speakers added after "When the stock market has declined sharply over a five-year
  stretch" **[R2009-002]** the market leg failed a good allocator, fails on
  Q7's computation below: the business's value at the sovereign rate does not cover its debt on the all-equity basis and
  is R$ 10.67 to 13.26 a share on the equity-only basis. Over the longer span 2016 to 2025 the company also took in R$ 38.5
  billion of new equity (Q4). *Carried as mixed.*
- **Paying out what cannot be employed.** The company paid R$ 12.2 billion of dividends in 2025 and its board approved up
  to R$ 7.7 billion "available for allocation" from the first-half 2026 results (2Q26 release); for a business earning about
  5% on its capital (Q3), "a company that expects to regularly earn more than it can profitably employ in its business,
  should be paying out dividends" **[M2004-089]**. *Weighs for.*
- **Buybacks and the PNC redemption.** Repurchases: R$ 1,967 million in 2023 at an average of R$ 36.19 per common and R$ 39.07
  per class B preferred (FY2023 20-F, Note on equity), R$ 115 million in 2024, R$ 37 million in 2025; the programme's stated
  purpose is "to increase the value to shareholders by the efficient application of the resources available in cash",
  and **no price above which purchases stop was found** (sweep of the FY2023 and FY2025 20-Fs for "average price",
  "repurchase", "buyback"; Item 16E of the FY2025 20-F reads "Not applicable"). The PNC shares, R$ 30 billion of capitalized
  reserves, are to be converted 1:1 or redeemed by 2031, any redemption "at a price per share equivalent to the closing
  market price of our common shares" (Item 3.D): a buyback rule priced at the market, never at value. "the question of
  whether a repurchase action is value-enhancing or value-destroying for continuing shareholders is entirely purchase-price
  dependent" **[L2016-002]**; "Continuing shareholders are hurt unless shares are purchased below intrinsic value."
  **[L2011-003]**. *The prices paid against the bottom of the Q7 range (written back at Q7, 2026-10-18):* the 2023 purchases
  at R$ 36.19 a common share (about R$ 28.7 per share of today's count after the 0.263 PNC bonus) sit far above the bottom
  of the range on either basis (-R$ 7.37 all-equity, R$ 11.25 equity-only) and above its top; a PNC redemption at today's
  market price would be the same. The programme with no stated price therefore weighs against, "entirely purchase-price
  dependent" **[L2016-002]**.
- **Issuance and deals.** "We will issue common stock only when we receive as much in business value as we give."
  **[R1995-010]**. Two issues in the decade: 2020 (R$ 7.75 billion, the Federal Government's advances converted) and the 2022
  privatization offering (R$ 30.6 billion primary at R$ 42, which paid the R$ 26.6 billion grant bonus for the new
  concessions); both were the selling government's design, not management's choice, and neither was a payment for a
  business in shares. No all-stock acquisition was found (deals 2021 to 2026 were cash: Eletronet, Tijoá/Juno, the IE
  swap), so the STOP on an all-stock deal in undervalued stock ("it's impossible for that buyer to make a sensible deal in an
  all-stock deal" **[L2009-019]**) does not arise. Not "hell-bent on issuing
  shares" **[L2014-015]**. The acquisitions of the window were small against disposals (purchases about R$ 5.0 billion,
  disposals about R$ 7.8 billion, 2021 to 2025), so the business is a net seller of parts, not a serial acquirer.
- **Part A: WEIGHS AGAINST**, narrowly: the payouts are right for a business that cannot earn its cost of money, but the
  repurchase rule and the PNC redemption are set at the market price, and the market price is far above any value the
  filings support (Q7).

**Part B: the pay, the board and the owners.**
- *Pay tied to what the person controls* ("tying performance to what is actually under the reasonable control of the person
  that’s being measured" **[M2003-019]**): the option plan has the step-up the speakers ask for, a strike not below the
  R$ 42 offering price, indexed to IPCA "subject to the addition of a specific spread", with a lock-up, close to "an
  appropriate strike price, 2) an escalation in price that reflects the retention of earnings, and 3) a ban on his quickly
  disposing of any shares" **[L2004-016]**; the new performance-share plan (2026) pays on total shareholder return, the
  market's "ride" **[M2000-062]**. Total management pay of R$ 77 million is modest against the company's size.
- *The board:* ten members; three appointed by a 40.67% holder that is also the policy-maker and the counterparty in
  Eletronuclear and Angra 3; the chairman's own companies under contract to the company, amounts undisclosed (Item 6C);
  large holdings bought by two directors (Q5), the "huge and true ownership interests" **[L2002-033]** the speakers prefer.
- *The owners as partners:* the 10% voting cap and the golden share keep any holder, including the government, from
  control; PNC holders are told the redemption may come "at a price" the board sets from the market, with tax costs
  (Item 3.D).
- **Part B: UNDECIDED**: an option plan of the fair form and owner-directors, against a TSR plan, a related-party
  chairman and a government bloc whose interests are not only the owners'.

## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**; value is "the discounted
value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, at "the risk-free interest rate"
**[L2000-021]**, here the BRL long nominal sovereign, 12.87% (Step 0). Arithmetic in
`Test Runs/_research 2026-10-18 AXIAY/q7.py`; R$ million unless per share.

**The construction, specific by specific.**
- *Owner cash* after every real cost, from the filed cash flow statements (Step 0 table), five-year window 2021 to 2025.
- *(a) The cycle base.* The 2022 figure carries the concession payment of the privatization, about R$ 31.9 billion of
  intangibles of which the grant bonus was R$ 26.6 billion, paid "in exchange for the right to explore electricity
  generation projects under the New Concession Agreements" for 30 years (FY2023 20-F, Item 5B): a year aberrational on the
  filer's own description: "If either year was aberrational, any calculation of growth will be distorted." **[L2005-003]**. The central base leaves it out: **R$ 8,388 million** all-equity, **R$ 4,738
  million** equity-only. *The literal window beside:* R$ 2,001 million all-equity and -R$ 1,649 million equity-only.
- *Aggregate growth shown.* Ex-grant all-equity owner cash rose from R$ 6,521 million (2021) to R$ 12,299 million (2025),
  17.2% a year; the literal series changes sign (2022 is -R$ 23,257 million), so by (b) the literal window is carried at no
  growth alone. Equity-only ex-grant fell from R$ 5,606 million to R$ 4,842 million, -3.6% a year: by **(b)** the decline is
  the bottom of the equity-only range and no growth its top.
- *(f) The cap.* 17.2% for ten years would take owner cash to about R$ 41.0 billion, 64% of revenue grown at its own rate,
  against the highest share of revenue owner cash reached in the filings read, 29.8% (2025): "you bump into absurdities" **[M1999-067]**.
  The growth carried is cut to the business's own revenue growth over the window, **4.49% a year** (R$ 34,627 million to
  R$ 41,282 million), never above the discount rate ("when the compound rate becomes higher than the discount rate, you get into infinite
  numbers" **[M1997-095]**). The shown rate and the cut are both written here.
- *(c) Acquisitions* (R$ 2,722, 74, 1,440, 177 and 568 million) are deducted and the total growth credited; disposals
  (R$ 7.8 billion over the window) are not added to owner cash, since they shrink the business and already sit in the lower
  net debt (CONVENTION of this run: a disposal's proceeds are counted once, in net debt, because counting them also as owner
  cash while valuing the remaining business at its growth would count them twice). After year ten purchases stop and the
  tail is on owner cash before purchases (average R$ 996 million added back). Not a serial acquirer (net seller). No merger
  in the window. *Deals closed after the window:* the IE Madeira / IE Garanhuns swap closed in 2Q26 with a net R$ 1.167
  billion received, already inside the 2026-06-30 net debt; no earnings credited. *Signed, not closed:* the Eletronuclear
  stake sale; assets held for sale were R$ 2,265 million at 2026-06-30; valued beside at book, about +R$ 0.8 a share,
  which changes nothing below.
- *(d) Working capital* is inside the operating cash flows used.
- *(e) Maintenance.* The filing allows the guess for generation (R$ 1.3 billion of R$ 1.4 billion in 2025 was maintenance,
  Item 5B), where growth spending is immaterial; it does not for transmission, whose construction spending both replaces the
  RAP that each review takes away and adds new RAP, with no split in the cash flow statement. The central case therefore
  charges all spending; the depreciation variant is shown beside.
- *Ten years, then zero nominal growth;* discount at 12.87%.
- *Basis* ("we evaluate acquisitions on an all-equity basis" **[L2017-004]**): central all-equity, owner cash before interest against market value plus net debt at the latest
  filed date, 2026-06-30 (2Q26 6-K): borrowings R$ 70,973 million + leases R$ 684 million - cash R$ 11,040 million -
  securities R$ 15,631 million = **R$ 44,986 million**, **plus the Law 14,182/2021 obligations of R$ 42,959 million**
  (CONVENTION of this run: these CDE and river-basin obligations are fixed, inflation-indexed instalments to 2047, accreting
  charges at 7.60% and 5.67% real (Note 25), booked by the filer as financing and paid as principal and interest; they are
  counted in net debt and their payments are left out of all-equity owner cash, so they are counted once; the case with
  them left out of net debt is shown beside and overstates value, because its owner cash also omits the payments). The
  litigation provisions (R$ 19.9 billion) are not added to net debt, since their payments stay inside owner cash. Subsequent
  events stated in the 2Q26 filing: R$ 3.5 billion of debentures in July (cash and debt both up, no change), and up to R$ 3.7
  billion "available for allocation" (a distribution to today's holders, value-neutral to them, not added). Equity-only:
  owner cash after interest and after every CDE payment, against the market value alone.
- *Whose tax:* the company's own cash tax (R$ 708 million paid in 2025). The low rate rests on tax losses and the 75% IRPJ
  reduction; Note 12 expects the tax-loss assets to be used "through 2047", not inside ten years, so the carryforward
  convention does not apply. The all-equity add-back of interest is pre-tax, which flatters the all-equity figure.

**Value range** (per share, on 2,775.95 million shares; per ADS at PTAX 5.0826, one share per ADS):

| Case | No growth | 4.49% for ten years | Expected return at the price |
|---|---|---|---|
| **CENTRAL, all-equity, 2022 grant left out, CDE in net debt** | **-R$ 7.37** (US$ -1.45) | **R$ 0.73** (US$ 0.14) | **3.6% to 5.1%** |
| Equity-only, 2022 grant left out (bottom -3.6%, top no growth) | R$ 11.25 (US$ 2.21) at -3.6% | R$ 14.09 (US$ 2.77) at 0% | 2.4% to 3.3% |
| Literal window, all-equity (grant inside; sign change, no growth only) | -R$ 26.1 | n/a | 0.8% |
| Beside: CDE left out of net debt (overstated) | R$ 7.3 | R$ 14.9 | 4.0% to 5.7% |
| Beside: depreciation in place of capex | -R$ 0.58 | R$ 9.73 | 4.5% to 6.4% |
| Beside: cash only to 2052, the generation concessions' end (transmission's 2042 would cut further) | -R$ 9.21 | -R$ 2.13 | 0.05% to 1.6% |
| Stress, not a convention case: 2025 alone as base, plus R$ 2.2 billion for the last quota energy, judicial payments kept | R$ 9.73 | R$ 23.40 | 6.0% to 8.2% |

(The literal, life-limited and CDE-out rows are from the first block of `q7.py`, without the after-year-ten purchase
add-back; the rest from its refined block.)

**Against the price of R$ 59.49** (AXIA3; AXIA7 R$ 59.99; ADS US$ 11.63).

**The floor, tested first.** "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**;
the convention's floor is about ten percent on owner cash after the company's tax. At the price, the expected return is
3.6% to 5.1% on the central case, 2.4% to 3.3% equity-only, and 8.2% on the most favourable stress I could construct; **no
case earns the floor.** Every case also falls below the government's own 12.87%, the yardstick "at a base" **[M2007-095]**.
And the speakers' condition for this very country, "We would want it to be cheaper than if it were in the United States."
**[M2006-021]**, points the other way from where the price sits. The width test is not reached: "the floor is tested
first", and the central range runs below zero, so a three-to-one ratio has no meaning here.

**Fair price (a reporting figure, never a verdict; Part VII):** each end valued with its own cash at ten percent, the two
averaged: **all-equity (central) R$ 5.75 a share, US$ 1.13 per ADS**; **equity-only R$ 16.42 a share, US$ 3.23 per ADS**;
after the company's own tax. No cheap price is reported.

- **VERDICT: OUT** at Q7, on the floor: the price of R$ 59.49 sits far above the top of every case of the range, and no
  case earns ten percent at it: "there’s just a point at which we drop out of the game" **[M2003-149]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Electricity generation and transmission are not among the businesses the framework names.)

---
## THE BOX
**OUT, at Q7 (the floor).** Value range, central all-equity case, **-R$ 7.37 to R$ 0.73 a share** (US$ -1.45 to 0.14 per
ADS), equity-only beside **R$ 11.25 to R$ 14.09** (US$ 2.21 to 2.77), against **R$ 59.49** (AXIA3, 2026-10-16; ADS
US$ 11.63); expected return at the price 3.6% to 5.1% (central), below both the ten-percent floor and the 12.87% BRL
sovereign. Fair price (reporting figure): R$ 5.75 all-equity (US$ 1.13 per ADS), R$ 16.42 equity-only (US$ 3.23). Q1 IN,
Q2 IN (transmission decides; regulated return), Q3 weighs against, Q4 weighs against, Q5 integrity IN and ability for, Q6
Part A against (narrowly), Part B undecided. Not a TOO HARD, so no research pass is opened.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2; each with its source, as "write it down in the first 30 minutes" **[M1997-127]** asks.)*
- **Bears on Q8 (the bond).** The Tesouro Nacional's longest nominal bond yields 12.87% (NTN-F 2037, 2026-10-15); every case
  in the Q7 table returns less at the price, the most favourable stress 8.2%. The longest inflation-linked bond yields 6.73%
  real (NTN-B 2060).
- **Bears on Q9 (debt and exposures).** Borrowings R$ 74.3 billion at 2025-12-31, maturing R$ 13.2 billion in 2026,
  R$ 7.6 billion in 2027, R$ 5.9 billion in 2028, R$ 7.6 billion in 2029, R$ 6.7 billion in 2030 and R$ 33.3 billion later
  (Note 24); R$ 71.0 billion at 2026-06-30. Law 14,182/2021 obligations R$ 43.8 billion, scheduled to 2047 (Note 25).
  Guarantees given for non-controlled investees R$ 21.5 billion (Note on guarantees, FY2025 20-F). Cross-default clauses:
  "A default with a single lender may trigger cross default clauses in other financing contracts" (Item 3.D). Litigation:
  R$ 19.9 billion provisioned, R$ 55.6 billion rated possible (civil R$ 16.5 billion, tax R$ 16.6 billion, land R$ 12.2
  billion, regulatory R$ 5.9 billion; Note 27.2); the State of Piauí's enforcement of R$ 3.59 billion suspended pending final
  judgment (Note 27.1.2). Dam-accident and Eletronuclear indirect-liability risks (Item 3.D). Interest paid R$ 5.8 billion in
  2025 against operating cash before interest of R$ 20.3 billion. The "little or no debt" criterion would not be met for a
  whole business.
- **Bears on Q10.** None beyond Q7 and Q8.
- **Bears on Q12.** The filer lists human-rights and community-relocation risks of large dams in the Amazon and elsewhere
  (Item 3.D); no named business of Q12 is involved.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits 359ef1aa (Step 0 to Q1), 6b4917a6 (Q2), 16d11e65 (Q3), 26f21f50 (Q4), fd38ba0a (Q5), 36540916 (Q6),
      c794300f (Q7 with the Q6 line written back), then this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present (the
      dispatcher's); folding into the register is the dispatching session's (operator rule ten). This run binds nothing
      until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched; what was seen by accident is declared
      under Contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-18 AXIAY/check_cites.py`
      (every id exists; every quoted fragment beside an id is in that row; no E-ids); every filing fact carries its
      accession or, for the post-15F company documents, the document and date.
- [x] The order was kept; Q7 was the first STOP that failed; nothing after it is a clearance, and Q8 to Q12 are NOT
      REACHED. Q1 to Q6 each passed or weighed before Q7 was computed, so Q7's figures are a valuation, not a
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy (operator rule 5);
      sovereign from the issuing authority (Tesouro Nacional, dated 2026-10-15); exchange rate from the Banco Central do
      Brasil (PTAX, 2026-10-16); the B3 and OTC quotes are an aggregator's and are flagged.
- [x] Contrary evidence written down as found (foundations, Q1, Q2, Q5); the facts for the questions not reached are
      under AFTER THE STOP. Q5 was reached and answered, so no "integrity facts recorded, not judged" flag is needed.
- [x] No point-in-time anchor: rows of any date may be cited (Part VII's anchor convention does not apply).
- [x] `tools/run.py` produced no arithmetic for this filer; nothing it prints was used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the final commit message).
- Open items I could not close: the share-count gap of about 115 million shares between the year-end issued count after
  conversion and the September 2026 table (Step 0); the amounts of the chairman's companies' contracts (not disclosed in
  the 20-F); rivals' unit generation costs (not read); the 3Q26 results (not yet published by the run date, as far as the
  documents read show).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The floor sits below the sovereign.** Q7's floor of "about ten percent" was stated by the speakers "in a world of 7
percent long-term bond rates" **[M1994-004]** and is applied here, in reais, against a government bond paying 12.87%. The
floor test then asks less of the stock than the bond does, and the reporting fair price (each end valued at ten percent)
is a price at which the buyer would earn less than the Tesouro pays, while the range itself is discounted at the higher
sovereign. The text foresees the floor moving with a lasting change in long rates ("he would change the numbers"
**[M2003-151]**) but gives no rule for a currency whose long rate is above it; I applied the ten percent literally, and Q8's
bond test would close a name at a lower price than Q7's floor. A currency rule for the floor (the higher of ten percent and
the sovereign plus a margin) would need a case. (2) **The 2022 concession payment fits neither (a) nor (c) cleanly.** It is a
one-time outlay the filer describes as such (so aberrational under (a)), but it bought a 30-year right and the quota
phase-out that drives the growth shown, and (c) forbids leaving a purchase out while crediting the total growth. I left it
out and credited the business's revenue growth, which favours the company, and the file still closes OUT; the text should
say how a renewal payment for a concession is treated. (3) **Debt-like regulatory obligations.** The net-debt definition
(borrowings and finance leases) does not reach the R$ 43 billion of Law 14,182/2021 obligations; I confessed a CONVENTION
of this run to count them in net debt and leave their payments out of owner cash. (4) **Finite concessions.** Q7 carries
zero growth for ever after year ten; the filer's own deferred-tax note says the concessions end in 2042 (transmission) and
2052 (generation) "without assuming concession renewals". The life-limited case is shown beside; the text is silent on
whether a concession's end caps the tail. (5) **The parts threshold measured on accounting profit.** Transmission decides
on IFRS operating profit inflated by regulatory remeasurements; I checked that it still decides with them taken out, but the
convention does not say which figure to use. (6) **The regulated-return exception at Q2** lets a castle that protects
returns below the risk-free rate pass Q2, leaving Q3 (a weighing) and Q7 to carry the whole verdict; that is what the text
says, and it worked here, but a run that reached Q7 at a lower price would have no STOP on the returns at all.
(7) `tools/run.py` cannot read an IFRS 20-F filer in reais (as the brief foresaw); every figure was hand-built from the
statements.
