# Company Run: Localiza Rent a Car S.A. (B3: RENT3; transitional preferred RENT4; OTC Level I ADR: LZRFY), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; this company does not file with the SEC, so every filing fact carries
the document and its date (and the CVM sequence number where the CVM index gives one) in place of an accession; a STOP that
returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch
(commit b1337c35).

**Dispatched blind run.** Analyst dispatched by the session's brief of 2026-10-16. Research folder:
`Test Runs/_research 2026-10-16 LZRFY/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only (LZRFY, RENT3, Localiza); not held.*

**Contamination, declared and not used.** (1) Before the first fetch I listed the `Test Runs/` file names through a filter for
"LZRFY|RENT|Localiza" to make sure no earlier run of this company existed; the filter returned no Localiza file and two other
companies' run file names (an AMH run of 2026-07-15 and a SUNB run of 2026-10-12, matched on the word "Rent"). Neither was
opened. (2) The session context showed the working tree's status (research folder names of other runs) and the last five
commit subjects, which concern another company's run (TRN). (3) The project's memory index, loaded into every session, carries
one-line summaries of the queue state (counts of runs and gate-clearers). (4) `.gitignore` comments name other runs (SNPS,
DELL, MGM) as the origin of its rules. None of this bears on Localiza and none of it was used.

**Corporate events since 2017, identified from the latest statements and the Reference Form (the brief asked for them):**
- 2017: acquisition of Hertz's car rental operations in Brazil (the dispatcher's description; not re-read here).
- 2019: primary public offering, BRL 1.8 billion (Reference Form 2026 v5, item 1.1).
- 2020: Localiza Fleet acquired MOBI7 (telematics), 2020-03-12; merger-of-shares agreement with Companhia de Locação das
  Américas ("Locamerica", then B3: LCAM3) signed September 2020, approved by shareholders 2020-11-12, approved by CADE with
  remedies 2021-12-15 (Reference Form item 1.1).
- 2022: **merger of shares with Locamerica effective 2022-07-01**, paid in Localiza shares (Reference Form item 1.1; share
  capital rose from BRL 4.0 billion to BRL 12.15 billion in the company's balance sheet, spreadsheet "AssetLiability"); as the
  CADE remedy, a carve-out of about 49,000 cars and 202 agencies was sold to a Brookfield-managed fund (now Unidas Locadora
  S.A.) for BRL 3,878.9 million, completed 2022-10-01; launch of the corporate brand **Localiza&Co** (the legal name is
  unchanged).
- 2023: primary follow-on offering, BRL 4.5 billion, June 2023; merger of Locamerica Rent a Car into Locamerica, 2023-12-31.
- 2025: **merger of Locamerica into the Company, 2025-08-01**, after which the goodwill began to be amortized for tax;
  a write-off of BRL 936.8 million of Locamerica's tax-loss carryforward assets followed (DFP FY2025, management report 8.1).
  **Bonus issue of 41,638,625 transitional preferred shares (RENT4)**, approved at the EGM of 2025-12-29 by capitalizing
  BRL 2,065.3 million of retained earnings: voting, equal in dividends, convertible 1:1 into common shares by 2028-12-31 or
  redeemable by the Board at the prior day's closing price of the common shares (DFP FY2025 note 22(a)(i); Reference Form
  item 12). Agreement to sell the 64.6% stake in Voll (corporate travel platform), completed January 2026 for BRL 382.0
  million.
- No share split found in the documents read (DFP FY2025 note 22, ITR 2Q26 note 21, Reference Form item 1.1). One ADR
  represents one share (DFP FY2025 note 22(a)(iii)).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** RENT3 **BRL 49.69** (2026-10-16 close as served intraday by the Yahoo Finance chart API; an aggregator, flagged
  under operator rule 5, live quote only). RENT4 BRL 48.20 the same day (same source). LZRFY USD 9.80 (same source; not used).
- **Shares** (no cover page exists; the count is from the statements, as the brief directs): ITR 2Q26, "Company Information /
  Capital" and note 21, as of 2026-06-30: issued 1,082,620,720 common + 41,638,625 preferred = 1,124,259,345; treasury
  18,584,089 common + 1,060,334 preferred = 19,644,423; **outstanding 1,064,036,631 common + 40,578,291 preferred =
  1,104,614,922**. The preferred shares rank equally with the common in distributions and convert 1:1, so they are counted
  with the common (CONVENTION of this run: the per-share figures divide by all outstanding shares of both classes; rationale:
  the preferred are a transitional class with identical economic rights). Checked against the later notices to the market:
  the 2026 list on the IR site (filemanager categories "fatos-relevantes", "comunicados-mercado", "aviso-acionistas") shows
  after 2026-06-30 only shareholding notices from holders, interest-on-equity notices and debenture notices; no buyback,
  redemption or issuance that changes the count.
- **Market cap:** 1,064.04 m × BRL 49.69 + 40.58 m × BRL 48.20 = **BRL 54,828 million**.
- **Sovereign for the earnings currency (BRL):** the protocol's table covers USD, JPY and EUR only; the issuing authority for
  BRL is the **Brazilian National Treasury (Tesouro Nacional)**, file `PrecoTaxaTesouroDireto.csv` from Tesouro Transparente
  (downloaded 2026-10-16, latest base date **2026-10-15**). The longest-dated **nominal** bond published is **Tesouro
  Prefixado com Juros Semestrais (NTN-F) maturing 2037-01-01: 12.87% (Taxa Compra, the rate at which the Treasury sells to an
  investor) / 12.99% (Taxa Venda)**. Used: **12.87%, nominal**. The longest-dated bonds published at all are inflation-linked
  (Tesouro IPCA+ com Juros Semestrais 2060-08-15, 6.73% real; Tesouro Renda+ 2084, 6.71% real); they are not used because Q7
  discounts nominal cash and carries zero nominal growth after year ten (Q7, the four specifics), which needs a nominal rate.
  Year-end yields of the longest NTN-F in the same file, used at Q2: 2015 16.57%, 2016 11.51%, 2017 10.37%, 2018 9.32%,
  2019 6.93%, 2020 7.01%, 2021 10.82%, 2022 12.81%, 2023 10.44%, 2024 15.28%, 2025 13.89%.
- **Filings read** (operator rule 4; primary filings, the English free translations from the company's IR site, ri.localiza.com,
  served by its filemanager API):
  - **DFP FY2025** (annual audited financial statements with the Management Report and the audit committee report), filed with
    the CVM on **2026-02-26** (CVM DFP index: Localiza Rent a Car S.A., CD_CVM 019739, sequence 154953), English version
    published 2026-02-26.
  - **ITR 2Q26** (interim statements to 2026-06-30), published **2026-08-06**.
  - **Reference Form 2026, version 5** (Formulário de Referência), published **2026-09-11**: items 1 (business, competition),
    4 (risk factors, proceedings), 8 (pay), 11 (related parties), 12 (capital).
  - Earnings releases 4Q25 (2026-02-26) and 2Q26 (2026-08-06), for the free-cash-flow text, net debt and ROIC definitions.
  - Ten years of statements: **CVM open data, DFP consolidated statements FY2015 to FY2025** (dados.cvm.gov.br,
    `dfp_cia_aberta_YYYY.zip`, the regulator's transcription of each filed DFP), extracted to
    `cvm_lzr_*.csv` in the research folder; and the company's own historical spreadsheet (`Localiza-Spreadsheet-2Q26.xlsx`,
    IR site), used only where it matched the filed figures.
- **One figure cross-checked against the filed statement:** FY2025 EBIT (profit before financial result and taxes)
  **BRL 7,811.6 million** in the DFP's Management Report table 8.1 = CVM DFP line 3.05 BRL 7,811.7 million (rounding) =
  segment note 24(a)(ii) total 7,811,656 thousand. Also FY2025 net operating cash BRL 2,146.5 million in the company spreadsheet
  = CVM DFP line 6.01 (BRL 2,146 million).
- **Tools:** `python tools/run.py LZRFY` printed "LZRFY: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE"; `python
  Screens/cover_shares.py LZRFY` printed "NOT AN SEC REGISTRANT". Both return nothing for this company; all arithmetic below is
  by hand from the statements, shown, with scripts in the research folder (`extract_cvm.py`, `pivot.py`, `extract_peers.py`,
  `owner_cash.py`, `valuation.py`).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the fleet will earn, "Not by selling it to somebody else" **[M1997-052]**. The
market serves and does not instruct **[M2006-077]**: the quotation of about BRL 55 billion is read only against the value the
filings support. No macro forecast enters **[M2000-094]**; Brazil's interest rate enters only as the yardstick (the Treasury's
own long bond) and as the business's own cost of funds, a property of the business and not a forecast. Margin of safety: a
foreign business the analyst knows less well asks a lower price, "We would want it to be cheaper than if it were in the United
States." **[M2006-021]**, which names Brazil. Who is paid to tell you: the company's own release features an adjusted net income
and an adjusted ROIC that leave out two real costs (Q4 below), and its managers are paid on a ROIC that leaves out the
merger goodwill; both are read as the rows read a seller's projection **[M2011-083]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Localiza is plainly the scale leader and, on the filer's own evidence, the low-cost buyer and the best reseller of cars in
   Brazil: 44.5% of car rental and 32.7% of fleet rental by fleet (ABLA, Reference Form item 1.2), a fleet 2.4 times the
   second player's, 286,347 cars bought in 2025 against about 110,000 for its "main direct competitor", about 10.8% of all new
   cars and light commercial vehicles sold in Brazil, 263 own resale stores. This is the GEICO pattern in the rows.
2. Returns are recovering: the 2Q26 release reports an annualized 1H26 ROIC spread of 6.1 p.p. over the after-tax cost of
   debt, and 1H26 EBIT of BRL 5,057 million (BRL 4,775 million without the Voll gain) annualizes to about BRL 9.5 billion,
   well above any year of the window.
3. Against the business: depreciation per car swung from BRL 941 a year (Car Rental, 2021) to BRL 10,109 (2024), and the
   residual value of the fleet was revised down three times in three years by events outside the company (Provisional Measure
   1,175/2023 discounts on new cars, the Rio Grande do Sul floods, the IPI decree 12,549/2025): Reference Form item 1.1; DFP
   FY2025 management report 6.3 and 7. The company's own risk factor says "The car rental and fleet rental businesses have few
   barriers to entry" with 37,047 active rental companies (Reference Form item 4.1(iii)).
4. Against the business: return on equity was 7.1%, 6.9% and 7.3% in FY2023 to FY2025 (net income over year-end equity, CVM
   DFP), below the Treasury's own long bond in each of those years.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of RENT3 would be made with the buyer's own money, unlevered, in a position
that a fall of half would not force to sell **[M2020-022]**; nothing in owning a listed share gives anyone a call on the buyer
**[M2006-079]**. A currency holding is "a bet on how government now, and in the future, will behave" **[M2011-025]**: a BRL
asset bought with dollars carries that bet, which the buyer must size so that it cannot ruin him. No ruin path found for the
buyer.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business, from the DFP FY2025 Management Report (section 4) and the Reference Form (item 1.2).** Two operating segments
(note 24): **Car Rental** (daily, replacement, monthly and ride-hailing rentals; franchising; 691 agencies, 592 in Brazil;
cars usually sold after about 12 months) and **Fleet Rental** (24 to 60 month contracts for companies, car subscription
"Localiza Meoo", heavy vehicles); **Seminovos** sells the decommissioned cars of both segments through 263 own stores and
wholesale, and its results are reported inside each segment. FY2025 net revenue BRL 41,781.6 million, of which rentals BRL
19,598.1 million and car sales BRL 22,183.5 million; EBIT BRL 7,811.6 million; 655,716 cars in Brazil at year end.

**The key variables** **[M1998-044]**: (1) rental price per day and utilization; (2) the depreciation of each car, which is the
purchase price less the resale price, and so depends on new-car prices set by the automakers and by Brazilian tax policy; (3)
the cost of funds, floating over the CDI, since the fleet is financed with BRL 43.6 billion of debt; (4) the cost of
maintaining, licensing and selling the cars. The company states its own model in these terms: it prices "based on demand,
seasonality, customer profile, rental period, pick-up/return location, and vehicle-related costs, including purchase price
and depreciation" (Management Report 4.2), and it manages to a spread of ROIC over the after-tax cost of debt (release 4Q25,
section 13).

**The test as the draft states it** **[M2012-065]**: a reasonable fix on "what the earning power and competitive position
will look like in five or 10 years". The ten-year picture is foreseeable in outline: people and companies in Brazil will rent
cars, the fleet will turn over every one to three years, and the largest buyer and reseller will still be the largest, since
the scale facts above are a decade and more in the making (agency network from 1973, Seminovos from 1991, market leader by
agencies from 1981: Management Report section 3). The economics are those of a spread business: the return on the fleet is
what rates leave after depreciation and running costs, set against a funding cost that floats with the CDI. The past
statements do tell the future ones in that sense **[M2008-033]**: ten years of filed statements show the spread, its collapse
when residual values fell (FY2023 to FY2024) and its repair by repricing (FY2025), which is the cycle a forecast must allow
for. The product is plain and the customer's behaviour is what is forecast, not a technology **[M2017-019]**.

**What could put it outside the perimeter, and the answer.** (a) Residual values move with government tax decisions on new
cars; the company's own residual-value revisions in 2023, 2024 and 2025 show the variable is volatile, but it is a known
variable whose direction the company can price over a cycle (rates rose from BRL 68.5 a day in 2020 to BRL 150.8 in 2025 in
Car Rental, company spreadsheet "Car Rental"); its effect belongs to the castle and the value, not to understanding. (b)
Ride-hailing, car subscription and, further out, self-driving cars change who rents; the change is slow in Brazil and is
already inside the business (Zarp rents to ride-hailing drivers; Meoo is a subscription product). No industry insider would
refuse to write down where car rental in Brazil will be in ten years in the way the tech insiders of the 2000 row would
**[M2000-105]**. (c) Abroad: the governance (Novo Mercado listing, no controlling shareholder, a transitional voting
preferred class) and the tax (interest on equity deductible, ICMS on car sales, accelerated tax depreciation of the fleet)
are read in the filings; the rows ask a higher reward for Brazil rather than a pass **[M2000-141]**, **[M2006-021]**, which
is carried to Q7.

**Doubt test** **[M2002-092]**: the doubt found is about the level of returns, not about whether the economics can be
foreseen; that doubt is the castle question and goes to Q2.

**VERDICT: IN.** The economics of a large car renter and reseller in Brazil can be foreseen in outline ten years out
**[M2012-065]**, **[M2000-037]**; the key variables are named and visible in the filings **[M1998-044]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (section B). The filer reports two segments with different economics (note 24); Seminovos is reported
inside each. Five-year operating profit FY2021 to FY2025 (segment EBIT including each segment's car sales, company spreadsheet
"Car Rental" and "Fleet Rental", which sum with Mexico and write-up amortization to the filed consolidated EBIT; FY2024 and
FY2025 agree with note 24(a)(ii)):

| Part | EBIT FY2021-FY2025, BRL m | share | castle | decides |
|---|---|---|---|---|
| Car Rental (Brazil, with franchising and its Seminovos) | 2,404.7 + 3,037.2 + 2,800.0 + 2,827.9 + 3,960.6 = 15,030.4 | 54.3% | standing, ordinary returns (below) | **yes, more than half** |
| Fleet Rental (with its Seminovos, Meoo, heavy vehicles) | 819.4 + 1,492.2 + 3,157.5 + 3,135.6 + 4,036.8 = 12,641.5 | 45.7% | same field, same competitors (Reference Form 1.4) | no |
| Mexico | losses (FY2024 EBIT -158.4; FY2025 -185.8, note 24) | n/a | start-up | no |

Segment return on the segment's own net invested assets (note 24(a)(i) and (ii), pre-tax EBIT over year-end net invested
assets): Car Rental FY2024 2,827.8 / 24,075.9 = 11.7%, FY2025 3,960.6 / 29,222.7 = 13.6%; Fleet Rental FY2024 3,135.7 /
32,180.7 = 9.7%, FY2025 4,036.8 / 26,906.4 = 15.0%. (The two segments' asset columns appear to change places between the two
years in the filed table; the sums are unaffected.)

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**: the reasons a customer rents from Localiza are the network (691 agencies,
   "larger than the combined total of the other two main competitors", Reference Form 1.4), the brand (7th most valuable in
   Brazil, Brand Finance; Reclame Aqui 8.7 against 8.0 for the main competitor) and price. The reasons it earns are the cost of
   its cars (scale purchasing), the resale price it gets (own retail channel) and its funding cost (the highest ratings in the
   sector, Management Report 4.1). These are scale advantages, durable and decades old.
2. *Would it stand without the lord* **[L2007-006]**: yes; the advantages are scale and process, not a person. The CEO
   succession of 2021 (Management Report section 3) passed without a break in share.
3. *The money test* **[M2011-015]**, **[M2012-106]**: could a well-funded attacker take it? Not the whole of it, quickly: a
   rival would need a decade of purchases and stores. But the company's own risk factor answers the narrower question: "The car
   rental and fleet rental businesses have few barriers to entry. In a highly fragmented market, competitors may invest to
   enter this business at any time" (Reference Form 4.1(iii)); 37,047 active rental companies (ABLA, 2025); the number of
   rental companies grew 40.2% between 2023 and 2025, and "automakers, vehicle dealerships, and digital platforms have entered
   the car rental and fleet rental segments" (Reference Form 1.4(ii)). In the words of the row, an industry "just never going
   to have barriers to entry" **[M2012-106]**, where the leader stays ahead by running.
4. *Pricing power and the agony before a rise* **[M2005-020]**: the Car Rental daily rate fell from BRL 84.6 (2015) to BRL 68.5
   (2020) while the average price of a car bought rose from BRL 35.5 thousand to BRL 50.5 thousand (company spreadsheet
   "Operating data"); it rose to BRL 150.8 by 2025 only after depreciation per car rose from BRL 941 (2021) to BRL 10,109 a year
   (2024), and the company describes the rises as adjusting rates "to restore return levels" (Reference Form 1.4), with rental
   days slightly down in 2025 (Management Report 7). The company's own long series says the price of a rental day fell from 35%
   of the minimum wage in 2003 to about 10% (Reference Form 1.4). Prices follow costs, and the gains of scale have gone to the
   customer, the commodity mark in the rows: "the improvement you get one day, your competitor gets the next day. And it very
   much tends to work to the benefit of consumers but not to increase overall profitability." **[M2004-053]**.
5. *Unit volume and share of mind* **[M1999-054]**: share has risen (44.5% of car rental by fleet), partly by merger; rental
   days in Car Rental rose from 15.6 million (2015) to 75.8 million (2025). Volume holds.
6. *The low-cost position* **[L2004-007]**, **[L2000-017]**: this is Localiza's case, and the filer documents it: 286,347
   cars bought in 2025 against about 110,000 by the "main direct competitor"; purchase scale that "contributes to a lower
   investment per vehicle for renewal and expansion, as well as reduced depreciation"; own retail resale that reduces
   "intermediary costs, resulting in lower depreciation expenses" (Reference Form 1.2). The rows call this "Another way to
   prosper in a commodity-type business" **[L2004-007]**. Whether it has prospered is the returns test below.
7. *The brand* **[M2023-073]**: recognized, but no filing evidence was found that renters pay more for the name; price is set
   with "pricing position relative to competitors" among its factors (Reference Form 1.2).
8. *Would the customer choose it over the low bid* **[M2017-009]**: in fleet rental the customer is a company buying on
   contract terms; in car rental the replacement segment is bought by insurers, and ride-hailing drivers rent on price. Mostly
   the low bid, with service at the margin.
9. *Ask the competitors* **[M1999-130]**: not available on the public record; the rivals' filings were read for their numbers
   only.
10. *Widening or narrowing* **[M1999-108]**: share widened (merger, scale). Returns narrowed: see the field's returns.
11. *What could destroy, modify or reduce it* **[M2000-014]**: government decisions on new-car taxes and discounts that cut
   resale values (three revisions in 2023 to 2025); cheaper imported electric cars; ride-hailing and subscription changing who
   owns cars. None closes the castle; each moves the spread.

**The competitor row.** The DFP and the Reference Form name **no competitor**: they speak of "our main direct competitor" and
"the other two main competitors" without names (Reference Form 1.2 and 1.4). **CONVENTION of this run: the rivals are chosen
by the analyst**: the three car and fleet renters that file audited statements with the CVM in the same business,
**Movida Participações S.A.** (CD_CVM 023825; the largest independent rival, consistent with the filer's "about 110,000"
purchases), **Companhia de Locação das Américas** ("Locamerica", CD_CVM 022691, owner of the Unidas brand until the 2022
merger; it filed DFPs to FY2024) and **Unidas Locadora S.A.** (CD_CVM 027162, the Brookfield-owned carve-out, DFPs from FY2023).
Rationale: the filer names none, and these are the filers whose fleets the filer's own share figures count. Not filing or not
comparable, flagged: the "large global brands" the Reference Form mentions without names (no Brazilian filing found for them),
the "automakers, vehicle dealerships, and digital platforms", and the truck renter Vamos (CD_CVM 024716, a different asset).
Same metric for all, from each company's own consolidated DFP as transcribed by the CVM: **pre-tax EBIT over average capital
employed (equity plus loans, financing and debentures, less cash and short-term investments)**, every year filed in the span
(scripts `extract_peers.py` and `q2_returns.py`; outputs `peer_returns.csv`, `q2_returns.txt`):

| Company | Years | Pre-tax EBIT / average capital, by year (%) | Mean | After 34% | Long NTN-F, mean of the same year-ends |
|---|---|---|---|---|---|
| Localiza (filer) | FY2016-FY2025 | 19.6, 18.0, 17.0, 14.7, 14.7, 23.3, 14.3, 11.3, 10.1, 13.2 | 15.6% | 10.3% | 10.8% |
| Localiza, goodwill and intangibles left out of capital | FY2016-FY2025 | 20.0, 18.3, 17.2, 14.8, 14.8, 23.6, 16.6, 13.7, 11.9, 15.6 | 16.7% | 11.0% | 10.8% |
| Movida Participações | FY2016-FY2025 | 11.9, 12.6, 13.9, 12.5, 6.4, 21.7, 20.2, 8.9, 15.6, 16.5 | 14.0% | 9.3% | 10.8% |
| Cia de Locação das Américas | FY2018-FY2024 | 18.3, 14.4, 11.0, 19.1, 15.2, 13.5, 6.1 | 13.9% | 9.2% | 10.4% |
| Unidas Locadora | FY2024-FY2025 | 8.9, 10.0 | 9.4% | 6.2% | 14.6% |

The 34% is Brazil's combined statutory income tax and social contribution, from which the DFP's tax note reconciles; it
overstates what Localiza pays in cash (interest on equity is deductible and accelerated tax depreciation defers tax), so the
after-tax column understates the measure somewhat; it is the same for every company in the row. On the company's own
definition (NOPAT at the effective tax rate, goodwill left out of invested capital) ROIC was 14.6% "adjusted" for FY2025, and
the company states its "historical levels" as a spread "between 5 and 8 percentage points above the cost of debt" after tax
(release 4Q25, section 13), the cost of debt itself floating over the CDI. Return on equity, which carries the leverage:
20.7%, 18.6%, 19.4%, 21.3%, 15.3%, 17.3%, 26.8% in FY2015 to FY2021, with net debt about equal to equity, then 9.0%, 7.1%,
6.9%, 7.3% in FY2022 to FY2025 after the merger (CVM DFP, net income over year-end equity).

**The field's returns over the last full cycle, judged in words** (section C). The span FY2015 to FY2025 holds a full cycle in
the filer's own description: the recession of 2015-2016, the pandemic of 2020, the used-car price boom of 2021-2022 (Car Rental
depreciation BRL 941 a car in 2021) and the residual-value collapse of 2023-2024 (BRL 10,109 a car in 2024). Over it, the
durable players in this field, the leader included, earned on all the capital they employ a pre-tax return of about 14% to 16%,
which after Brazil's tax comes to about what the Treasury paid on its own long nominal bond in the same years. The leader's
edge over its rivals is real but small over the span (15.6% against 14.0% and 13.9% pre-tax) and, after the merger, absent
(FY2023 to FY2025: Localiza 11.3%, 10.1%, 13.2%; Movida 8.9%, 15.6%, 16.5%). The high returns on equity before the merger
were made with debt about equal to equity, a source the rows say to rule out before crediting a high return: "a cyclical peak
in earnings, a monopolistic position, or leverage" **[L1994-009]**; "we could make it almost any number you want if we just
used enough leverage" **[M2001-054]**. The moat in the rows is what "protects excellent returns on invested capital"
**[L2007-004]**; in this field the castle stands and the leader is the low-cost operator, but what it protects is a return
about equal to the risk-free rate in its own currency. The rows' own case: "you can have only two competitors and they’re still
terrible businesses" **[M2013-052]**. "Ordinary" carries no figure (the section C CONVENTION): the judgment in words is that
the returns over the whole span are ordinary, no better than the government's own bond, for the leader and for the field.

**A change for the better?** The 1H26 annualized return is higher (contrary evidence 2 above), and the rows record that "the
railroads were a terrible business for decades and decades and decades and then they got good" **[M2017-026]**. The framework
credits a change for the better only on a full cycle in which the price behaviour held **[M2005-020]**: one half-year of
repricing after two years of write-downs is not that cycle. It is not credited here; if it were the deciding question the box
would carry a re-look condition, but it is not: even the 1H26 run rate is tested against the price under Q7's computation
below.

**Routing.** The castle is not filling in on the evidence (share is rising), and its future can be judged (scale advantages
decades old, returns read from ten years of filings), so neither the open-castle OUT nor TOO HARD applies. What applies is the
item in Q2's list of what it rules OUT, "The standing castle that protects only ordinary returns", which is "OUT, not TOO
HARD", because the tenuous-moat row's reason, "We don’t know how to valuate that" **[M2000-019]**, does not hold when the
returns are known. The regulated-return exception does not apply: no regulator sets these returns. The deciding part (Car
Rental) and the other part (Fleet Rental) sit in the same field with the same rivals and the same level of return, so the parts
rule gives the same answer.

**VERDICT: OUT.** A standing castle that protects only ordinary returns over a full cycle, on the evidence of the filer's and
three rivals' own filings **[L2007-004]**, **[M2013-052]**, **[M2004-053]**, **[L1994-009]**. Localiza is the low-cost operator
**[L2004-007]**, but the filings do not show it prospering beyond the field or beyond the Treasury's own long rate. The file
closes here. Q3 to Q12 are NOT REACHED; what was found for them is written below under AFTER THE STOP, and Q7 is computed
under the heading COMPUTATION, NOT A CLEARANCE for the two reporting figures the brief asks for.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The ten years of balance sheets were read in Step 0 and Q2 as the template asks, and are written
down under AFTER THE STOP.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts found are under AFTER THE STOP, flagged in the box line.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found, including the buyback line against the bottom of the computed range, are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The range and the fair price are computed under AFTER THE STOP, headed COMPUTATION, NOT A
CLEARANCE, for the reporting figures the brief asks for.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing: "if there’s nothing smart to do, cash is the default option"
**[M2003-072]**.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. No named business is involved (car rental and used-car retail).

---
## THE BOX
**OUT at Q2** (Q1 IN): a standing castle that protects only ordinary returns over a full cycle. Localiza is the scale leader
and the low-cost buyer and reseller of cars in Brazil, but over FY2016 to FY2025 it earned a pre-tax 15.6% on the capital it
employs (16.7% with goodwill left out), about the Treasury's own long nominal bond after tax, and its three filing rivals the
same or less (Movida 14.0%, Locamerica 13.9%, Unidas Locadora 9.4%); return on equity was made with leverage before the 2022
merger and was about 7% after it. **Integrity facts recorded, not judged** (the featured adjusted net income and adjusted ROIC
that leave out the residual-value write-down of FY2025; the executives' pay metric that leaves out the merger goodwill; a
restricted-share plan for senior managers that the filer says is "not considered part of the Company's compensation strategy").
COMPUTATION, NOT A CLEARANCE: value range **BRL -9.92 to BRL 0.16** a share against **BRL 49.69**; no case earns the floor at
the price. Fair price BRL 5.81 a share all-equity (BRL 11.90 equity-only). Not a TOO HARD; no research pass is opened.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2; each with its source **[M1997-127]**.)*

### Bearing on Q3 (capital)
- Capital employed (equity plus net debt, CVM DFP) rose from BRL 3.6 billion (FY2015) to BRL 58.5 billion (FY2025); BRL 8.4
  billion of the latter is goodwill from the 2022 merger. New equity: BRL 1.8 billion (2019 offering), the merger shares (2022;
  share capital from BRL 4.0 to 12.15 billion), BRL 4.5 billion (2023 offering) (Reference Form 1.1; company spreadsheet
  "AssetLiability").
- Every car bought is cash spent; cars bought in FY2025 cost BRL 26,951.4 million against BRL 22,183.2 million received for
  cars sold (DFP cash flow). The average price of a car bought rose from BRL 35.5 thousand (2015) to BRL 91.1 thousand (2025)
  (company spreadsheet "Operating data"): a fleet of the same size needs more money every year as car prices rise, the
  inflation test of the rows: the best business "retains its earning power in real dollars without commensurate investment"
  **[M2005-049]**.
- What the added capital earned: owner cash on the combined basis rose from BRL 3,371 million (FY2021) to BRL 5,482 million
  (FY2025) while tangible capital employed rose by about BRL 27.6 billion (from about BRL 22.0 billion combined, after the
  carve-out proceeds, to BRL 49.7 billion): about 7.6% after tax on the added capital (`valuation.py`), below the long NTN-F
  in each of those years.
- The company's own ROIC (effective tax, goodwill left out): 14.6% adjusted FY2025; 4Q25 annualized 15.5%; 1H26 spread 6.1
  p.p. over the after-tax cost of debt (releases 4Q25 and 2Q26).

### Bearing on Q4 (the accounts), with the balance sheets first **[M2025-032]**
Ten balance sheets, FY2015 to FY2025, consolidated, CVM DFP (BRL millions; `bpa_pivot.txt`, `bpp_pivot.txt`):

| | 2015 | 2017 | 2019 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Total assets | 6,123 | 11,186 | 19,393 | 25,312 | 65,657 | 80,947 | 87,244 | 85,567 |
| Cars and other PP&E | 3,925 | 7,484 | 14,570 | 17,294 | 43,020 | 52,116 | 53,842 | 53,732 |
| Intangibles incl. goodwill | 89 | 83 | 140 | 143 | 8,734 | 8,851 | 8,878 | 8,874 |
| Cash and financial assets (current) | 1,385 | 2,614 | 2,831 | 5,009 | 5,560 | 10,322 | 11,426 | 10,592 |
| Trade receivables | 486 | 585 | 1,275 | 1,310 | 2,480 | 3,682 | 4,034 | 3,995 |
| Suppliers (mostly automakers) | 691 | 1,332 | 2,565 | 2,059 | 6,178 | 8,881 | 10,026 | 9,343 |
| Loans, financing, debentures | 3,019 | 6,477 | 9,379 | 12,433 | 33,272 | 40,608 | 44,767 | 43,595 |
| Deferred tax liabilities | 142 | 220 | 353 | 1,148 | 2,019 | 1,701 | 1,948 | 2,493 |
| Equity | 1,942 | 2,601 | 5,448 | 7,617 | 20,571 | 25,398 | 26,343 | 25,539 |

What moved and why: the fleet and the debt grew together, about fourteenfold; equity grew by new shares more than by kept
earnings (profit reserves stayed between BRL 0.9 and 4.9 billion while interest on equity was paid out every year, and the
2025 bonus issue moved BRL 2.1 billion of reserves into capital); goodwill appeared with the 2022 merger and has not been
impaired (note 13); receivables stayed about one fifth of rental revenue (486 of 1,883 in 2015; 3,995 of 19,598 in 2025);
payables to automakers are a large, interest-bearing source of fleet finance (BRL 2.2 billion settled early in 4Q25 at 115% of
the CDI, Management Report 8.2). What the figures cannot say: the fleet's book value rests on management's estimate of each
car's resale value, revised down in 2Q23, 2Q24 and 3Q25 (DFP FY2025 note 12; Reference Form 1.1), so equity and every past
year's EBIT moved with those estimates. Deferred taxes: a BRL 8.1 billion liability for accelerated tax depreciation of cars,
against a BRL 6.1 billion asset for tax-loss carryforwards that the same accelerated depreciation created (note 21), net
liability BRL 2.0 billion; cash taxes paid were BRL 83 to 488 million a year in FY2022 to FY2025 against EBIT of BRL 4.5 to
7.8 billion.
- **Real costs.** Car depreciation is the business's largest cost and is charged (FY2025 BRL 5,413 million for cars, BRL 573
  million other, BRL 5,941.8 million in all, DFP note 24(iii)). Stock pay is expensed under IFRS 2 inside EBIT (the total
  expense was not located in the notes read; the Statutory Board's share-based pay was BRL 82.6 million in FY2025, Reference
  Form 8.2).
- **EBITDA in the filer's own mouth**: the CEO's message reports "EBITDA was BRL 13.8 billion" and segment EBITDA margins of
  67.0% and 72.6% (Management Report section 2); for a car renter EBITDA leaves out the cost of the cars. The rows: "The one
  figure we regard as utter nonsense is the so-called EBITDA" **[M1998-086]**.
- **An adjusted figure featured, weighing against and carried to Q5** (section A of the gaps case): the CEO's message
  features "Adjusted net income totaled BRL 3.4 billion" against filed net income of BRL 1,870.4 million; the adjustment adds
  back the FY2025 residual-value revision (BRL 929.2 million pre-tax, BRL 613.3 million after tax, "non-recurring") and the
  BRL 936.8 million write-off of Locamerica's tax-loss carryforward asset (company spreadsheet "Consolidated 2025 adjusted";
  Management Report 8.1). Residual-value revisions were also taken in 2Q23 and 2Q24, so the "non-recurring" cost recurred
  three years running. The rows: "a management that regularly attempts to wave away very real costs by highlighting "adjusted
  per-share earnings" makes us nervous" **[L2016-006]**; telling owners year after year to ignore necessary business
  adjustments "is misleading" **[L2016-007]**.
- **No guidance**: "The Company did not disclose any projections for year 2026" (ITR 2Q26, Comments on the Performance of
  Business Projections).
- Nothing found that confused the reading of the accounts; the audit opinion on the FY2025 statements carries a key audit
  matter on the recoverability of goodwill (DFP auditor's report).

### Bearing on Q5 (the people), integrity facts recorded, not judged
- The adjusted net income and adjusted ROIC above (Q4).
- Executive pay metric: the corporate goal is the "ROIC spread, measured by Nopat (EBIT x (1 - Effective income tax rate)
  divided by Invested Capital (Net Debt + Equity - Goodwill)" (Reference Form 8.1). The goodwill left out is the price paid in
  shares for Locamerica, which the rows say to include when judging the capital allocation, "because we paid for it"
  **[M2011-060]**.
- The "Reference Managing Shareholder" plan grants senior managers "a significant number of restricted shares over the long
  term, subject to their continued service"; the filer says "The plan is not considered part of the Company's compensation
  strategy due to its corporate nature", and the compensation chart "does not include the costs associated with the Reference
  Managing Shareholder Program" (Reference Form 8.1 and 8.4). Amended 2026-04-30 to deliver the shares at once under lock-up.
- Pay, FY2025 (Reference Form 8.2): Statutory Board (7 members) BRL 111.0 million, of which share-based BRL 82.6 million, bonus
  and profit sharing BRL 9.2 million (profit sharing BRL 5.9 million); Board of Directors (7.33 members on average) BRL 22.7
  million, almost all fixed. Variable pay was described as reflecting "performance levels below expectations" in 2025.
- Proceedings: tax disputes (PIS/COFINS credits, BRL 201.6 million and others; ICMS on car sales, BRL 770.0 million possible
  loss), labor conduct-adjustment terms with the Public Ministry of Labor being complied with; "no confidential cases that the
  Company considered relevant" (Reference Form 4.4 to 4.7). No investigation of the company or its officers for fraud or
  corruption found in the documents read.
- Clear speech in places: the management report states plainly that net income rose only 3.1% "after recognition of a
  write-off of BRL 936.8 million" and explains the IPI effect in figures (Management Report 8 and 8.1).

### Bearing on Q6 (the money and the owners)
- **Buybacks.** In 2024 the company repurchased common shares under its 16th program (maximum 87,000,000 shares, no price
  stated), at an average cost of about BRL 40 to 42.5 a share (DFP FY2025 note 22(b)(iii)); a 17th program runs 2026-01-20 to
  2027-07-21 for up to 72,000,000 shares, again with no price stated; its stated aim is "to maximize the generation of value for
  shareholders or settle the share purchase programs within the scope of the Company's long-term incentive plans". **The Q6
  buyback line, written back from the COMPUTATION below:** the prices paid (about BRL 40 to 42.5) sit far above the bottom of
  the computed range (BRL -9.92) and above its top (BRL 0.16); under the convention of Q6 a programme with no stated price
  whose prices are not at or below the bottom of the range weighs against **[L2016-002]**, **[L1999-023]**. Buying to settle
  incentive plans is the use the rows name and refuse **[M2014-008]**.
- **The transitional preferred shares** may be redeemed by the Board "at the closing market price of the Company's common
  shares on the trading day immediately preceding the date on which the redemption is approved", without a shareholders'
  vote (Reference Form 12; bylaws), a cash return at the market price with no stated test of value.
- **Issuance and deals.** Shares issued in 2019 (BRL 1.8 billion), 2022 (the merger, paid in shares) and 2023 (BRL 4.5
  billion), plus the share plans. The merger was a deal paid in Localiza's own shares, a "merger" in the speakers' usage
  **[L2009-019]**; the Q6 STOP on an all-stock deal applies only where the acquirer's stock sat below its intrinsic value; the
  COMPUTATION below puts today's price far above the computed range, and no computation was made for 2020 to 2022, so the
  STOP is neither found nor excluded for the deal's own date. Whether this record is "hell-bent on issuing shares"
  **[L2014-015]** (Q6's candidate second STOP) was not judged.
- **Dividends.** Interest on equity of BRL 2,101.7 million declared for FY2025, 104.2% of net income after the legal reserve
  (Management Report 8.3); minimum dividend 25% by the bylaws. Retention test not run.
- The Voll stake, bought in May 2022, was sold for BRL 382 million, which the company calls "a return of approximately 5x on
  the original investment" (Management Report section 2).

### Bearing on Q9 (debt and exposures)
- Net debt (company definition: debt plus or minus swaps, less cash and short-term investments) **BRL 32,352 million at
  2026-06-30** (release 2Q26, section 12), BRL 31,052 million at 2025-12-31. Gross loans, financing and debentures BRL 44,636
  million at 2026-06-30 (ITR 2Q26 balance sheet). Lease liabilities BRL 1,296 million (branches and stores; left out of net
  debt and said so). Subsequent event: a July 2026 exchange of BRL 7.06 billion of debentures into new CDI + 1.25% notes due
  2033 (ITR 2Q26 note 30), a refinancing that leaves net debt unchanged.
- Coverage on the rows' measure, pre-tax earnings over interest, not EBITDA **[L2012-002]**: FY2025 (3,197.8 + 4,613.8) /
  4,613.8 = 1.69 times; FY2024 (1,866.5 + 3,938.6) / 3,938.6 = 1.47 times.
- The debt floats over the CDI (debentures at CDI + 0.91% to 2.40%), partly swapped to fixed (BRL 22 billion at 11.9%); cash of
  BRL 11.8 billion at 2025-12-31 covered 2026 and 2027 maturities (release 4Q25). Ratings from Moody's, S&P and Fitch
  (Management Report 4.1). It is not a business "employing little or no debt" **[R1997-001]**.

### Bearing on Q7: COMPUTATION, NOT A CLEARANCE
Built by Q7's range convention, with the six specifics, for the two reporting figures only (scripts `owner_cash.py`,
`valuation.py`; output `valuation_out.txt`). BRL millions unless stated.

**Owner cash, all-equity, after the company's own tax, maintenance only (spec (e), central).** For a car renter the
maintenance spending is the fleet's consumption, which the filed car depreciation measures (purchase price less estimated
resale, revised when resale prices fall); the maintenance guess is therefore the depreciation charge **[M2000-144]**,
**[L2000-035]**, and the purchases of cars beyond it (fleet growth and the rise in car prices) are growth spending, charged to
the growth case. Owner cash = EBIT (after car and other depreciation) less tax at 34% on (EBIT less the interest on equity
paid, which is deductible), plus other depreciation, less other capital spending, lease principal and lease interest.
**Merger in the window (spec (c)):** FY2021 and FY2022 are the company's own pro forma combined figures (Localiza with
Locamerica from 2021-01-01, company spreadsheet "Consolidated results proforma"); FY2023 to FY2025 are as filed.

| FY | EBIT | tax 34% × (EBIT − IOC paid) | other D&A − other capex − lease principal − lease interest | owner cash |
|---|---|---|---|---|
| 2021 (combined) | 5,142 | 1,652 | -119 | 3,371 |
| 2022 (combined) | 6,273 | 1,886 | -312 | 4,075 |
| 2023 | 5,899 | 1,620 | -262 | 4,017 |
| 2024 | 5,805 | 1,534 | -287 | 3,984 |
| 2025 | 7,812 | 2,059 | -271 | 5,482 |
| **average** | | | | **4,186** |

- **Cycle base (spec (a)):** the window FY2021 to FY2025 runs from the used-car price peak (2021-2022) through the
  residual-value trough (2023-2024) to the IPI revision the filer calls non-recurring (2025); it holds one peak and one trough,
  so the five-year average is the cycle base; the literal window is the same five years.
- **Growth (specs (a), (b)):** measured between the halves of the window (2021-2022 average 3,723 to 2024-2025 average 4,733,
  three years apart): **8.3% a year**; the literal end-to-end rate 2021 to 2025 is 12.9%, shown beside.
- **Growth spending (spec (e)) and the inversion.** The growth bought has cost about BRL 13.1 of added tangible capital for each
  BRL 1 of added yearly owner cash (BRL 27.6 billion for BRL 2.1 billion, FY2021 to FY2025), an after-tax return of about
  7.6% on the added capital, below the 12.87% discount rate. Growth bought below the discount rate is worth less than its cost,
  so the no-growth case is the top of the range and the growth case the bottom: "growth can destroy value" **[L2000-023]**.
- **Cap (spec (f)):** the 8.3% growth of owner cash is below the combined sales growth over the window, so no cut is needed.
- **Working capital (spec (d))** is inside the cash-flow variant below; the payables to automakers swing with purchases.
- **Tax** (CONVENTION of this run): statutory 34% less the interest-on-equity deduction the company actually takes. The
  company's cash taxes are far lower (BRL 297 million a year on average, FY2021 to FY2025) because tax depreciation of cars runs
  ahead of book depreciation; that deferral is carried as a BRL 8.1 billion liability, net BRL 2.0 billion after the loss
  carryforwards it created. No shelter is added (rationale: the carryforwards and the goodwill amortization are the
  counterpart of a deferred liability that reverses when the fleet stops growing, which is the case the range assumes after
  year ten; the Whose-tax convention's shelter rule names carryforwards that run out, not these).
- **Net debt** BRL 32,352 million (2026-06-30, company definition, stated subsequent events add nothing); **shares**
  1,104.61 million; **market value of the shares** BRL 54,828 million; enterprise value BRL 87,180 million.

**The range, at the long NTN-F rate of 12.87%:**

| Case | Whole business | Less net debt | Per share |
|---|---|---|---|
| Growth case: 8.3% for ten years with its growth spending charged, then zero nominal growth (**bottom**) | 21,392 | -10,960 | **BRL -9.92** |
| No-growth case: maintenance owner cash 4,186 forever (**top**) | 32,525 | 173 | **BRL 0.16** |
| Shown beside: literal 12.9% growth, spending charged | 11,806 | -20,546 | BRL -18.60 |
| Shown beside, a bound only: 8.3% growth with no growth spending charged (forbidden as a case) | 55,098 | 22,746 | BRL 20.59 |

- **Floor tested first.** At the price, the best case (no growth) yields 4,186 / 87,180 = **4.8%** on the whole business,
  below the floor of about 10% (CONVENTION, Q7) and below the Treasury's 12.87%. **No case in the range earns the floor at the
  price: Q7 would close OUT whatever the width** (the floor-first convention, **[M2003-149]**). The width test is not reached.
- **Equity-only, beside:** owner cash after after-tax interest (net financial expense FY2023 to FY2025 averaged BRL 4,192
  million; × 0.66 = 2,767): 4,186 − 2,767 = **1,419**, a 2.6% yield on the market value of the shares.
- **Contrary evidence, tested (a sensitivity, not a case):** 1H26 EBIT without the Voll gain, annualized, is BRL 9,550
  million. Taxed as above it gives about BRL 6.9 billion, 7.9% of the enterprise value; taxed only at the FY2025 cash tax paid
  (BRL 477 million) it gives about 10.4%. Only by taking the best half-year of the record and the deferred tax as permanent
  does the price meet the floor, and then not the Treasury's rate.

**The two reporting figures (the owner's price, Part VII), BRL per RENT3 share:**
- **VALUE RANGE: BRL -9.92 to BRL 0.16** a share (growth case to no-growth case at 12.87%), all-equity basis less net debt,
  against the price of **BRL 49.69**.
- **FAIR PRICE: BRL 5.81** a share, all-equity basis (central): each end case valued at ten percent instead of the long
  government rate, no-growth BRL 41,860 million and growth BRL 35,683 million, averaged BRL 38,771 million, less net debt BRL
  32,352 million, over 1,104.61 million shares. **Equity-only figure beside: BRL 11.90** (owner cash after interest, 1,419,
  valued at ten percent in both cases and averaged). Tax treatment: the company's own tax as stated above, no conversion. The
  fair price sits above the top of the value range because the floor of ten percent is below the Brazilian Treasury's own long
  rate (see the last section). Neither figure is a verdict or entry language (operator rule 3).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit b1337c35); written question by question; committed after Step 0 and
      Q1 (b9d45570), after Q2 (ec4d75a4), and at the close.
- [x] Dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatching session's; the fold
      into the register is the dispatcher's (operator rule ten). Not checked by the analyst, by the blind rule.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One filtered listing of `Test Runs/` file
      names was made before the first fetch (to confirm no Localiza run existed); the two other companies' file names it showed
      are declared under contamination and were not opened or used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `check_ids.py` in the research folder, PASS); no E-ids. Every filing fact names its document and date (no accession
      numbers exist for a CVM filer; the DFP's CVM sequence number is given).
- [x] The order was kept; Q2 closed the run; everything after it is NOT REACHED or written under AFTER THE STOP, and the Q7
      figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from EBIT after car depreciation, never a net-income proxy (operator rule 5); the
      sovereign from the issuing authority (Tesouro Nacional), dated; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (four items under the foundations; the 1H26 sensitivity under Q7).
- [x] Not a point-in-time run; no anchor rule applies.
- [x] `tools/run.py` and `Screens/cover_shares.py` were run and returned nothing for a non-SEC filer; no line of theirs was
      used.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Honest limits: the Q2 rivals are the analyst's choice (CONVENTION above); the 34% tax in the Q2 row is statutory and the
  same for all; FY2021-FY2022 owner cash rests on the company's pro forma, not on an audited combined statement; the Hertz
  Brasil acquisition of 2017 was not re-read; the stock-pay expense total was not located.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The floor is below this currency's risk-free rate.** Q7's CONVENTION floor of "about ten percent pre-tax" was the
   speakers' figure "in a world of 7 percent long-term bond rates" **[M1994-004]**; the Brazilian Treasury's long nominal bond
   pays 12.87%. Part VII's fair price (each end valued at ten percent) therefore discounts at a rate below the government
   bond, and here the fair price (BRL 5.81) lands above the top of the value range (BRL 0.16), which no reader would expect.
   The rows already say the floor moves with lasting changes in long rates **[M2003-151]** and must be "significantly higher"
   than the bond **[M2007-095]**, but the text gives no rule for a currency whose bond exceeds the floor. What I did: computed
   the figures exactly as Part VII defines them and said so; the floor test closes OUT on either rate.
2. **"Ordinary returns" has no stated yardstick.** Q2's item says to judge the field's returns in words, with no figure, but
   not against what: the rivals, the cost of debt, or the sovereign. I set them against both the rivals and the Treasury's own
   long bond in the same years, and said which.
3. **Owner cash for a fleet business.** Under IFRS the purchase and sale of rental cars run through operating cash flow
   (IAS 16.68A), so "capital spending" in the template and in Q7's specifics does not find the car purchases where it looks
   for them, and the net figure mixes maintenance, growth and car-price inflation. I took depreciation as the maintenance guess
   and charged the rest as growth spending; the text could say how to read a business whose main capital asset is a
   trading inventory.
4. **Deferred tax from accelerated depreciation.** The Whose-tax convention prices a shelter that "runs out inside ten
   years"; it does not say what to do when the low cash tax is a deferral carried as a liability that reverses only if the
   fleet stops growing. I taxed at the statutory rate less the interest-on-equity deduction and showed the cash-tax sensitivity.
5. **The competitor row when the filer names none.** The brief anticipated it; the template does not. I confessed the choice.
6. **Two share classes and the brief's per-share figure.** The transitional preferred shares carry identical economics; I
   divided by both classes and said so.
