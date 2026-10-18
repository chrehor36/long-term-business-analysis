# Company Run: ENN Energy Holdings Limited (SEHK: 2688; OTC ADS: XNGSY), 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (the company files no
annual report with the SEC, so the document and its HKEXnews path stand in place of an accession number, departure 3 of the
brief). A STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED. Dispatched blind run
under `Screens/_daily/_dispatch_brief.md` with the brief's three stated departures (lines of evidence derived by the analyst;
competitors as the annual report names them; the company's own annual report as the primary document).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (a3bc9d45): `PORTFOLIO.md` read for this one ticker; the operator does not hold XNGSY (no line names XNGSY, 2688 or ENN).*

**Contamination, declared and not used.** (1) The session context listed the last five commit subjects of the repository,
which carry another company's run (ENGGY, Enagas: its box, its expected returns and its fair price); read by accident, not
used; this run's method is the framework's Q7 text, not that run. (2) A directory listing of `Test Runs/` filtered for
"ENN" returned three other companies' file names (a 2026-07-15 run on LEN, a 2026-10-05 run and research folder on PENN);
names only, not opened. (3) The project map and the operator's memory index were loaded into the session context (queue
states, counts); not used. No run, research pass or holding review of ENN Energy under any name was opened or searched.

**Lines of evidence (departure 1), chosen from the annual report's own sections.** From the FY2025 annual report: the
Management Discussion and Analysis (segments: retail gas, integrated energy, wholesale of gas, construction and
installation, smart home), the Financial Review (debt, net gearing, currency, commodity hedging), the Corporate Governance
Report's "Key risk management" table (market, safety, operational, compliance risks), Note 6 (segment results, assets,
additions and depreciation), Note 11 (directors' pay), Note 41 (senior notes), Note 52 (related-party transactions), the
Directors' Report (share schemes, purchases of shares, connected transactions). Lines followed: segment margins over the
cycle; gas sourcing and pass-through of gas cost (the dollar margin series in the company's results presentations); pricing
through the 2021 to 2022 gas-cost inflation; concessions and their terms; acquisitions and goodwill (the 2018 purchase from
the controlling family); debt and leases; share purchases and their prices; share-based pay; dealings with the controlling
shareholder (ENN Natural Gas, ENN-NG) and companies controlled by Mr. Wang Yusuo; litigation and investigations (none
disclosed; see Q5).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HK$50.15 per ordinary share, close 2026-10-16 (Yahoo Finance chart API, an aggregator, flagged per operator
  rule 5; the last close before the run date, a Sunday). ADS XNGSY US$25.54, close 2026-10-16 (same aggregator, flagged).
  Cross-check: 4 x HK$50.15 / 7.8475 = US$25.56, within two cents of the ADS quote.
- **ADS ratio:** four ordinary shares per ADS (F-6EF of 2019-11-22, JPMorgan Chase Bank depositary, SEC CIK 0001454948, as
  the brief states; the CIK carries ADR F-6 filings only).
- **Shares by class:** one class, ordinary shares of HK$0.10. **1,131,839,264** in issue, no treasury shares, at
  2026-09-30 (Monthly Return of Equity Issuer for September 2026, submitted 2026-10-02, HKEXnews
  `/listedco/listconews/sehk/2026/1002/2026100202589.pdf`). Of these, 19,984,600 (about 1.77%) are held by the trustee of
  the Share Award Scheme (FY2025 annual report, Directors' Report); they are counted as outstanding here, because they are
  bought to be given to employees and the cash that bought them is charged as pay in owner cash (Q4). Options outstanding:
  224,000 under the 2012 Scheme (same monthly return). `python Screens/cover_shares.py XNGSY` returned "NOT AN SEC
  REGISTRANT in the live ticker file": nothing used from it.
- **Market cap:** 1,131.84m x HK$50.15 = HK$56,762m = RMB 48,621m at the CFETS central parity below.
- **Sovereign for the earnings currency (RMB):** **2.06%**, the 30-year point of the ChinaBond Government Bond Yield Curve
  (YTM), 2026-10-16, published by China Central Depository & Clearing (ChinaBond), the government's designated depository
  for the Ministry of Finance's bonds (yield.chinabond.com.cn, series "ChinaBond Government Bond Yield Curve(YTM)", curve id
  2c9081e50a2f9606010a3068cae70001; saved as `Test Runs/_research 2026-10-18 XNGSY/chinabond_2026-10-16.json`). Tenor
  chosen: 30 years, because the protocol's own table takes the 30-year point for USD and the speakers' rate is "the yield on
  long-term U.S. bonds" **[L2000-021]**; the 10-year point the same day is 1.648%, and the longer the tenor the higher
  (and so more conservative) the rate. `python tools/sources.py` covers USD, JPY and EUR only and was not used.
- **Exchange rates:** CFETS (China Foreign Exchange Trade System, the People's Bank of China's authorised publisher of the
  central parity) central parity 2026-10-16 09:15: HKD/CNY 0.85658, USD/CNY 6.7220; cross USD/HKD 7.8475 (saved as
  `Test Runs/_research 2026-10-18 XNGSY/cfets_ccpr_2026-10-16.json`). Price per share RMB 42.96.
- **Filings read** (operator rule 4; HKEXnews paths, all under `https://www1.hkexnews.hk`):
  - Annual Report 2025, published 2026-04-28 (`/listedco/listconews/sehk/2026/0428/2026042802499.pdf`): primary statements,
    notes 6, 11, 18, 27, 41, 52, MD&A, Financial Review, Corporate Governance Report, Directors' Report.
  - Annual Reports 2016 to 2024 (published 2017-04-06, 2018-04-16, 2019-04-15, 2020-03-30, 2021-04-06, 2022-04-06,
    2023-04-19, 2024-04-21, 2025-04-15): the primary statements of FY2016 to FY2023 taken from the reports for FY2017,
    FY2019, FY2021 and FY2023 (each carries the prior year), FY2024 from the FY2025 report; segment notes of FY2021, FY2023,
    FY2025; the FY2018 goodwill and acquisitions notes and its Directors' Report (connected transactions).
  - Interim Report 2026, published 2026-09-17 (`/listedco/listconews/sehk/2026/0917/2026091700629.pdf`): condensed
    statements at and for the six months to 2026-06-30.
  - HKEXnews announcements 2025-01-01 to 2026-10-18, every title listed and the following read: the Rule 3.5 joint
    announcement of 2025-03-26 (pre-conditional privatisation proposal, `/2025/0326/2025032600769.pdf`); the updates of
    2025-12-18, 2026-01-28 and 2026-05-15; the lapse of the proposal, 2026-06-12 (`/2026/0612/2026061201210.pdf`); the
    interim dividend notice, 2026-08-28; the early redemption of the US$550m 4.625% notes due 2027, 2026-10-09
    (`/2026/1009/2026100900312.pdf`); the ABS issuance, 2025-12-19; the change of directors, 2025-02-25.
  - Company results presentations (ennenergy.com investor relations): FY2017, FY2019, FY2021, FY2023, FY2025 and 1H2026,
    read for the dollar-margin series, the capital-spending split and the 2026 guidance.
- **The event the brief asked about (rename, merger, offer, scheme, privatisation).** On 2025-03-26 ENN-NG (the controlling
  shareholder, 34.28% through Xinneng (Hong Kong) Energy Investment Limited) announced a pre-conditional proposal to
  privatise ENN Energy by scheme of arrangement: for each share, 2.9427 new ENN-NG H shares and HK$24.50 in cash, a stated
  theoretical value of HK$80.00, 47.60% above the undisturbed close of HK$54.20. On 2026-06-12 the proposal **lapsed**: two
  pre-conditions (the Listing Committee's approval in principle for the ENN-NG H-share listing, and the CSRC and other
  approvals) "remained unfulfilled", and ENN-NG chose not to extend the long-stop date. The listing is not withdrawn. The
  same announcement states that ENN-NG "intends, through the Offeror, to increase its shareholding in ENN", at prices and
  times "determined with reference to market conditions", and Rule 31.1 bars a new offer for twelve months from
  2026-06-12. No rename or merger found in the 2025 and 2026 announcement titles.
- **One figure cross-checked against the filed statement:** net cash generated from operating activities FY2025, RMB
  10,433m, read in the consolidated statement of cash flows (AR2025 p.95) and in the Financial Review's text ("the
  Group's operating cash inflow was RMB10,433 million"); they agree.
- `python tools/run.py XNGSY` returned "XNGSY: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE": no arithmetic
  line produced; all arithmetic is by hand from the annual reports, in `Test Runs/_research 2026-10-18 XNGSY/scripts/`
  (`owner_cash.py`, `returns.py`, `q7.py`, outputs beside them).

## THE FOUNDATIONS (not a gate)
The foundations bearing on this name: a share is a business, judged by asking "Would I be happy buying this stock if the market
closed for five years?" **[M1997-109]**; the market's recent move (from about HK$67 at the end of 2025, with a
HK$80 offer outstanding, to HK$50.15 after the offer lapsed) "doesn’t tell us anything. It just tells us prices."
**[M2006-077]**, so the lapse is weighed only for what it says about the controlling shareholder (Q5, Q6), never as a
signal; margin of safety, a decision that needs pencil and paper is "too close to think about" **[M1996-084]**; no macro view of Chinese gas demand, property or rates enters except as a property of the business
**[M2000-094]**; and a business abroad is one where the speakers "wanted to get paid more for going into China"
**[M2006-021]**. Who is paid to tell you: the ESG ratings and awards that fill the report's opening pages are recorded and
given no weight **[M2020-037]**. **Contrary evidence, written down as found** **[M1997-127]**: (i) five years of capital
spending at 2.0 to 2.8 times depreciation (2021 to 2025) with owner cash before growth spending falling, not rising
(Q3, Q4); (ii) the dollar margin on retail gas fell from RMB0.73/m3 (2016) to RMB0.51/m3 (2021) and "Increased gas cost
has not been fully passed through during the year" (FY2021 results presentation) (Q2); (iii) construction and installation
gross profit fell from RMB4,446m (2021) to RMB1,662m (2025) (Q2); (iv) the controlling family sold the company a business
in 2018 for RMB2.6bn paid wholly in new shares, goodwill RMB1,998m of it (Q5, Q6); (v) the risk table names a "one city,
one enterprise" policy that "undermines the integrity of existing operating rights" (Q2); (vi) companies controlled by
Mr. Wang sold the group about RMB3.8bn of goods and services in 2025 (Q5); (vii) ROE fell from 21.7% (2021) to 12.3%
(2025), and every rival read fell with it (Q2).

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase for cash, unlevered, sized so that no fall in the quotation can force a
sale, keeps the rule, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**; no borrowed money for the purchase **[L2014-005]**. An OTC ADS of
a Cayman company whose operations are all in mainland China adds a currency and a jurisdiction exposure that must be sized,
not levered. Nothing in this name obliges the buyer to sudden demands for cash **[L2014-024]**. Passes as a rule of conduct.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** A city-gas distributor holding operating rights in 264 city-gas projects in
  China (AR2025 highlights), 32.76m connected residential households and 316,000 commercial and industrial (C/I) customers;
  retail gas volume 26,606m m3 in 2025 (+1.5%); revenue RMB111,905m; five reported segments (AR2025 Note 6). Substantially
  all revenue, profit and non-current assets are in mainland China (Note 6). Gas is bought from the "three major oil
  companies", long-term LNG contracts and the spot market, and resold at prices that for residential customers are set by
  local government (71.6% of residential volume had "completed gas price adjustment" by end-2025, MD&A).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) retail volume, now low single digits (2026
  guidance "Flat to slight growth", 1H2026 presentation); (2) the dollar margin between sale price and gas cost, set inside
  a regulated pass-through (Q2); (3) connection fees, tied to new housing (construction and installation revenue down 17.9%
  in 2025, "weighed down by the real estate downturn", MD&A); (4) the tenure of the operating rights (Q2); (5) the growth
  businesses, integrated energy (steam, heat, power for parks and factories) and smart home (appliances and services sold
  to the gas customers). Each is a fact about customers, regulators and gas cost, not a technology race **[M2017-019]**,
  **[M2023-030]**; the past statements do tell the shape of the future ones **[M2008-033]**: a large, slow, regulated
  distribution business whose growth parts are small beside it.
- **Would the insiders write it down?** They do: the company publishes guidance for volume, new connections, capital
  spending, free cash flow and the dividend (1H2026 presentation), which is the opposite of the "That’s too hard" of
  **[M2000-105]** (the guidance habit itself weighs at Q4 and Q5).
- **Abroad.** The test is whether one understands "the nuances of the corporate governance system and taxation"
  **[M2000-141]**: a Cayman holding company, PRC operating subsidiaries taxed under the PRC enterprise income tax (25%
  statutory, effective 20.8% in 2025: tax RMB1,791m on profit before tax RMB8,614m), controlled 34.28% by a mainland-listed
  company (ENN-NG) itself controlled by Mr. Wang, with senior-note covenants that require "Mr. Wang and any affiliate of him
  to retain certain percentage of shareholding" (Note 52). The governance is legible from the filings; the rows ask for a
  higher price for it, not a pass **[M2006-021]**, and the decision can be made "off the figures" **[M2008-069]**.
- **Doubt.** The doubt rule, "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**, is applied to the deciding part (retail gas, Q2's parts table) and not met: what the gas franchise earns
  and why can be read; what is uncertain (the franchise tenure, the regulator's margin) is a question about the castle,
  owned by Q2, not a failure to understand the economics.
- **VERDICT: IN.** The ten-year economics of a regulated gas distributor can be pictured within a range **[M2012-065]**,
  **[M2000-037]**; the industry does not change fast; the uncertainties are knowable and are tested at Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (segment profit, which is gross profit after each segment's own depreciation and before central
administrative and selling costs; AR2021 Note 7, AR2023 and AR2025 Note 6; RMB m, 2021 to 2025; `scripts/rivals.py`):

| Part | 5-yr segment profit | Share | 2021 | 2025 | Castle | Decides |
|---|---|---|---|---|---|---|
| Retail gas sales | 31,010 | 43.8% | 6,164 | 6,127 | exclusive city-gas operating rights; regulated price | **yes (largest; no part above half)** |
| Construction and installation | 13,714 | 19.4% | 4,446 | 1,662 | the same rights (connections inside the franchise); tied to new housing | no |
| Value added / smart home | 12,403 | 17.5% | 1,723 | 3,114 | access to the franchise's 32.76m households | no |
| Integrated energy | 9,386 | 13.2% | 1,365 | 2,338 | none stated; the filing names "Intense competition in the integrated energy market" | no |
| Wholesale of gas | 4,334 | 6.1% | 358 | 51 | none; a trading margin | no |

No part carries more than half of five-year segment profit, so the largest, retail gas, decides (Q2's business-of-parts
CONVENTION, which rests on **[L2008-005]**). Construction and installation and smart home ride on the same franchise; the
parts without a castle (wholesale, integrated energy) are carried to Q7 as ordinary business at no growth, which the
owner-cash construction already does by valuing the whole on its cash.

**The castle tests, each with its filing fact (deciding part: retail gas).**
1. *What keeps it standing, and how permanent* **[M1995-038]**: piped gas inside an operating area is supplied only by the
   holder of that city's exclusive operating rights ("252 exclusive operating rights for city gas projects", AR2021 MD&A;
   264 city-gas projects at end-2025). It is "a natural franchise" in the speakers' list of moats **[M1995-037]**. Its
   permanence is the concession's term: Changsha's retail-gas concession "had expired" by the end of August 2023 and was
   renewed "for 10 years" (AR2023 Note 46), after which the group sold 6% and kept 49% as an associate.
2. *Would it stand without the lord*: yes; a gas network needs no superstar; the risk table's threats are policy, price and
   safety, not talent.
3. *The attacker with money* **[M2011-015]**: no second network can be laid inside a franchise. The attack comes at the
   large-customer edge: "direct supply to major customers, LNG point-of-supply, and competition within operating regions
   may have an impact on future market conditions" (AR2025, Corporate Governance Report, Key risk management, Market Risks).
4. *Pricing power and the agony before a rise* **[M2005-020]**: residential prices are set by local government; the company
   "steadily promoted the price adjustment processes" (AR2025 MD&A). The dollar margin on retail gas (results
   presentations, ex VAT): RMB0.73/m3 in 2016, 0.63 in 2017, 0.59 in 2019, 0.60 in 2020, 0.51 in 2021; average selling
   price less average cost (VAT basis not stated) 0.53 in 2022 and 0.55 in 2023; no later figure found in the text of the
   2025 and 1H2026 presentations. In 2019 the company kept "a stable dollar margin of gas sales thanks to its effective
   pass-through mechanism during price hike period" (AR2019); in 2021 "Increased gas cost has not been fully passed through
   during the year" (FY2021 presentation). The pass-through exists, at a margin others set and with a lag, which is not the
   strong position that will "manage to pass through increases in raw material costs" **[M2005-017]** on its own terms.
5. *Unit volume*: retail volume 26,606m m3 in 2025 (+1.5%); 2026 guidance "Flat to slight growth". Residential households
   32.76m (2025) from 25.84m (2021); C/I installed daily capacity 229.4m m3 from 162.8m (AR2025 ten-year comparison, which
   includes joint ventures and associates). Customers keep coming; volume has stopped growing fast.
6. *Low-cost position*: not the moat here; the company buys at prices set by the national oil companies, LNG contracts and
   spot, and hedges the LNG book (Financial Review).
7. *Brand*: not the moat; the customer buys the pipe, not the name.
8. *The low bid* **[L2004-003]**: the household has no choice inside the franchise; the large industrial customer has one,
   and the company meets it with "flexible pricing strategies to unlock incremental volume from key accounts" (AR2025 MD&A)
   and a pricing mechanism "to meet the low-cost demands of large users" (risk table). At the large end the low bid is in
   play.
9. *Ask the competitors*: not done; no access. The rivals' own filings are read instead (below).
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: narrowing at the edges. Connection profit fell 63% in four
    years; the dollar margin fell about 30% from 2016 to 2021 and no later year read returns to the 2016 level; the risk
    table adds "Policy and Franchise Challenges: During the mid-term evaluation of city gas franchise operations, the
    government is promoting a "one city, one enterprise" policy, which undermines the integrity of existing operating
    rights", and "expiration of operating rights create revenue uncertainty". The deciding part's segment profit held flat
    (RMB6,164m in 2021, RMB6,127m in 2025) while its households grew by a quarter: the franchise stands, but each unit of it
    earns less.
11. *What could destroy, modify or reduce it* **[M2000-014]**: a regulator that sets the margin lower, or shortens or
    consolidates the concessions (the speakers' own utility mistake: "I did not anticipate or even consider the adverse
    developments in regulatory returns" **[L2023-011]**); electrification of household and commercial heat over twenty
    years. Neither is shown on the evidence to be happening to the deciding part beyond the narrowing above.

**The competitor row (departure 2).** The annual reports name no rival: a text search of the FY2016 to FY2025 reports for
"competitor", "China Gas", "Towngas", "China Resources Gas", "Kunlun" and "Beijing Enterprises" finds only unnamed
references ("another major competitor in Shantou", AR2016 and AR2017). No instance found of a named rival. **CONVENTION of
this run:** three listed rivals chosen, the three other large Hong Kong-listed city-gas distributors in mainland China, read
from their own annual reports' financial summaries; rationale: they hold the same kind of franchise under the same
regulators, so their returns are the field's. **None files with the SEC** (flagged). China Resources Gas Group (1193.HK;
2025 and 2020 annual reports, HKEXnews `/listedco/listconews/sehk/2026/0430/2026043001092.pdf` and
`/listedco/listconews/sehk/2021/0419/2021041900818.pdf`); China Gas Holdings (0384.HK; years to 31 March; 2025/26 and
2020/21 annual reports, `/listedco/listconews/sehk/2026/0727/2026072700334.pdf` and
`/listedco/listconews/sehk/2021/0715/2021071500432.pdf`); Towngas Smart Energy (1083.HK; 2025 and 2020 annual reports,
`/listedco/listconews/sehk/2026/0420/2026042000330.pdf` and `/listedco/listconews/sehk/2021/0415/2021041500369.pdf`).
Metric, the same for all four: profit attributable to owners over year-end equity attributable to owners.

| Year | ENN | CR Gas | China Gas (FY to March of next year) | Towngas SE |
|---|---|---|---|---|
| 2016 | 14.4% | 18.5% | 20.2% | 7.2% |
| 2017 | 16.5% | 16.6% | 21.4% | 8.6% |
| 2018 | 13.2% | 18.5% | 23.3% | 7.5% |
| 2019 | 21.9% | 18.8% | 23.2% | 7.0% |
| 2020 | 20.5% | 14.2% | 20.2% | 7.0% |
| 2021 | 21.7% | 15.5% | 12.1% | 5.5% |
| 2022 | 15.0% | 12.0% | 7.4% | 4.5% |
| 2023 | 16.0% | 12.8% | 5.9% | 6.9% |
| 2024 | 13.3% | 9.9% | 6.0% | 6.8% |
| 2025 | 12.3% | 8.0% | 4.8% | 6.2% |
| 2016-20 average | 17.3% | 17.3% | 21.7% | 7.5% |
| 2021-25 average | 15.7% | 11.7% | 7.2% | 6.0% |

**The field's returns over the cycle, judged in words** (Q2's CONVENTION gives the word no figure; the moat is judged, not
measured, "there’s no formula that gives you that precisely" **[M1999-108]**).
Over the whole span the field earned good returns on equity in the first five years and falling ones in the second, every
player falling together; ENN is the best of the four in 2021 to 2025 and fell least, and its returns were earned with net
debt of 20% to 54% of total equity (Q4). A common fall across four companies with different owners says the cause is the
field's terms (connection fees with housing, margins with the regulators), not one company's errors. The castle is durable
and its returns are bounded by regulators, which Q2 sends to Q3 as a second best (its convention cites **[M2009-104]** and
**[L2009-012]**). It is not a castle shown open (no rival crosses the franchise), and its future can be judged as a narrowing
utility-like franchise, so neither OUT nor TOO HARD applies.

- **VERDICT: IN**, on the deciding part (retail gas): a legal franchise that an attacker with money cannot cross
  **[M2011-015]**, with weak pricing power **[M2005-020]** and a moat narrowing at its edges **[M1999-108]**; the
  regulator-bounded return is carried to Q3 as a second best **[M2009-104]**. Carried forward as contrary evidence: the
  dollar-margin squeeze, the connection collapse, the franchise-policy risk, the field-wide fall in returns.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The capital test as the brief fixes it: earnings after depreciation set against capital employed, and cash earnings set
against capital spending, never one against the other. From `scripts/returns.py`, filed figures (after-tax operating
earnings = (profit before tax + finance costs) x (1 - effective tax rate); capital employed = total equity + borrowings -
cash and cash equivalents; RMB m):

| Year | After-tax operating earnings | Capital employed | Return | Capital spending / D&A |
|---|---|---|---|---|
| 2016 | 3,307 | 27,482 | 12.0% | 3.0x |
| 2018 | 4,252 | 37,880 | 11.2% | 4.7x |
| 2019 | 7,425 | 42,792 | 17.4% | 4.2x |
| 2021 | 9,450 | 53,356 | 17.7% | 2.8x |
| 2022 | 7,161 | 57,298 | 12.5% | 2.7x |
| 2023 | 8,339 | 60,496 | 13.8% | 2.5x |
| 2024 | 7,449 | 62,915 | 11.8% | 2.2x |
| 2025 | 7,293 | 65,152 | 11.2% | 2.0x |

- **What it earns on the capital it needs** **[M2010-090]**, **[M2011-060]**: 11% to 18% after tax on capital employed,
  11.2% in 2025; the deciding part earns segment profit of RMB6,127m on segment assets of RMB43,564m (14.1%, before tax and
  central costs; AR2025 Note 6). A respectable return on the base, read with the rows' warning that a regulated position and
  leverage help make it **[L1994-009]**.
- **What the added capital earns.** From 2021 to 2025 capital employed rose RMB11,796m and after-tax operating earnings fell
  RMB2,157m: the increment earned less than nothing. Over 2016 to 2025 the increment earned 10.6% (RMB3,985m on
  RMB37,670m). Cash against spending: capital spending (property, plant and equipment, intangibles, right-of-use, deposits)
  was RMB6,398m to RMB7,092m a year in 2021 to 2025 against depreciation and amortisation of RMB2,263m to RMB3,486m; about
  RMB19.8bn was spent above depreciation in those five years, and owner cash with depreciation put in place of capital
  spending fell from RMB7,494m (2021) to RMB7,316m (2025), RMB6,536m in 2024 (`scripts/owner_cash.py`).
- **How much to stand still** **[L2000-035]**, **[L1999-024]**: the filing states no maintenance figure and no split of
  capital spending into maintenance and growth; the FY2025 presentation splits it by business (gas projects RMB4,477m,
  integrated energy RMB2,336m, administrative RMB338m, newly acquired projects RMB280m). It does name spending that only
  keeps the business in place: "contract cost for the renovation and enhancement to the existing pipeline to improve the
  operational safety" (AR2025 Note 27); "pressure on safety investment continue to increase" (risk table); the Board's
  review of "security renovation" (Corporate Governance Report). Management guides capital spending of about RMB6.0bn for
  2026 against retail volume "Flat to slight growth" (1H2026 presentation): spending about 1.7 times 2025 depreciation for
  no stated growth in volume. That is the shape the rows warn of, "compulsory reinvestment just in order to stand still"
  **[M1997-016]**, the spending made "the same way if it’s unattractive" **[M1998-128]**.
- **The growth arithmetic and its caps**: revenue grew 4.7% a year 2021 to 2025 (RMB93,113m to RMB111,905m); owner cash
  after all spending grew 2.5% a year between the end years and fell 0.3% a year between the halves (Q7). Earnings rose with
  capital in 2016 to 2021 and not since; of a utility the speakers say "we just put way more capital into the business"
  **[M2023-081]**.
- **Second best.** A regulated network is the rows' accepted second best only on "decent returns on the incremental sums
  they invest" **[L2009-012]**; "cash-consuming businesses, by their nature, are unattractive unless the cash they consume
  gets to earn a reasonable return" **[M2012-057]**. The last five years fail that condition.
- **WEIGHS AGAINST.** A decent return on the base, a negative return on the last five years' increment, and spending at
  twice depreciation that the company itself expects to buy flat volume **[M1998-081]**, **[M2012-057]**. (The "little or no
  debt" criterion is applied at Q9 **[R1997-001]**.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** (consolidated statements of
financial position, FY2016 to FY2025, from the annual reports for FY2017, FY2019, FY2021, FY2023 and FY2025; RMB m;
`scripts/returns.py`):

| 31 Dec | Equity attrib. | Goodwill + intangibles | Cash | Trade and other receivables | Inventories | Borrowings | Net debt | Net debt / total equity | Receivables / revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 14,966 | 1,675 | 7,163 | 4,423 | 515 | 16,791 | 9,628 | 53.9% | 13.0% |
| 2017 | 16,952 | 1,873 | 7,972 | 6,068 | 744 | 18,067 | 10,095 | 49.9% | 12.6% |
| 2018 | 21,385 | 5,285 | 7,923 | 8,560 | 1,331 | 20,249 | 12,326 | 48.2% | 14.1% |
| 2019 | 25,868 | 6,554 | 7,373 | 7,492 | 1,169 | 19,145 | 11,772 | 37.9% | 10.7% |
| 2020 | 30,561 | 6,957 | 8,630 | 9,053 | 1,285 | 19,684 | 11,054 | 30.6% | 12.6% |
| 2021 | 35,777 | 6,831 | 8,684 | 10,568 | 1,508 | 19,890 | 11,206 | 26.6% | 11.3% |
| 2022 | 39,040 | 7,069 | 8,056 | 10,675 | 1,708 | 19,792 | 11,736 | 25.8% | 9.7% |
| 2023 | 42,660 | 6,845 | 9,689 | 11,091 | 1,682 | 21,923 | 12,234 | 25.3% | 9.7% |
| 2024 | 45,101 | 6,924 | 7,693 | 9,828 | 1,513 | 19,532 | 11,839 | 23.2% | 8.9% |
| 2025 | 47,825 | 6,806 | 8,064 | 9,040 | 1,590 | 19,141 | 11,077 | 20.5% | 8.1% |

(Borrowings = bank and other loans, senior notes, corporate, unsecured and medium-term bonds, convertible bonds; leases
excluded. The company's own net-debt figures for 2023 to 2025, RMB12,234m, 11,839m and 11,077m, agree with these.)

**What moved and why, and what the figures do not say** **[M2025-032]**:
- Equity attributable more than tripled, almost all from retained profit; borrowings stayed between RMB16.8bn and 21.9bn
  for ten years, so gearing fell from 54% to 20.5% of equity without any debt being repaid in aggregate.
- Goodwill and intangibles jumped in 2018 from RMB1.9bn to RMB5.3bn: goodwill of RMB1,998m "Integrated energy business
  located in the PRC" (AR2018 Note 19) arose on the purchase from Essential Investment Holding Limited, "a company
  controlled by Wang Family", of a "technology solutions of multiple forms of energy" business for RMB2,606,595,755,
  "fully settled by the allotment and issue ... of 39,926,534 consideration shares" (AR2018 Directors' Report, connected
  transactions; approved at the EGM of 2018-08-08 with a whitewash waiver). About 77% of the price was goodwill (Q5, Q6).
  Goodwill and intangibles are 14.2% of owners' equity in 2025.
- Receivables rose with revenue to 2023, then fell; at 8.1% of revenue they are the lowest of the decade, and turnover days
  are 13 for receivables, 21 for payables, 6 for inventory (Financial Review). The expected-credit-loss charge is rising:
  RMB515m in 2025, RMB326m in 2024, RMB280m in 2023, RMB123m in 2021 (cash-flow adjustments).
- Contract liabilities (gas fees and connection fees received in advance) are the free funding behind the RMB12,939m net
  current liabilities ("receipts in advance of gas fee, and construction and installation contracts. These funds are stable
  and will normally not be returned", Financial Review); they fell from RMB15,915m (2019) to RMB14,962m (2025) as
  connections fell. A shrinking float of this kind is a use of cash in the years it shrinks.
- What the balance sheet cannot say: the value of the 264 operating rights (only the purchased ones are carried); the terms
  left on each concession (no table of expiries found in AR2025 by a text search for "expir"); the share of the FVTPL book (RMB3,908m)
  that is the 1.13% unlisted interest in Sinopec Marketing, a Level 3 valuation (Note 24).

**The real costs** (Q4's costs that are real):
- *Depreciation* is a real cost **[R1996-023]**, and here less than the spending: capital spending was 2.0 to 2.8 times
  depreciation in each of the last five years (Q3); "merely spending their depreciation expense will not keep them in the
  same place" is the speakers' warning for heavy networks **[M2016-092]**, and the filing's own guidance and safety
  spending point the same way (Q3).
- *Stock pay*: options are small (224,000 outstanding); the real cost is the trust that buys shares for the Share Award
  Scheme: 4,047,500 shares for about HK$250m in 2023 and 13,252,000 for about HK$731m in 2024 (AR2023 and AR2024 Directors'
  Reports; RMB229m and RMB665m in the cash-flow statements). Counted as pay in owner cash, since earnings are "a figure
  calculated after interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**, and stock
  pay is a real expense **[L2015-003]**.
- *Leases* (RMB96m to RMB187m a year) and the cash paid to minority holders of subsidiaries (dividends net of their capital
  contributions, RMB492m to RMB816m a year in 2020 to 2025) are charged in owner cash.
- *Recurring "one-time" items*: impairments every year (goodwill RMB601m in 2016 and property RMB478m in 2017 on the North
  American refuelling business sold in 2018; RMB244m in 2025); fair-value swings on commodity derivatives, which the
  company strips out of its headline figure.

**EBITDA and the adjusted figure, in the filer's own mouth.** The annual report leads with "core profit" (profit
attributable "stripping out other gains and losses ... and relevant deferred tax", RMB6,741m against reported RMB5,904m in
2025; Highlights, Chairman's Statement, Financial Review); the 1H2026 presentation leads with "EBITDA increased by 7.8% yoy
to RMB6.22 bn" (EBITDA: no instance found in the text of AR2025 or the 2026 Interim Report); the company publishes annual
guidance for volume, connections, capital spending, free cash flow and the dividend (1H2026 presentation, "2026 Guidance").
The adjusted figure featured **[L2016-006]**, guidance **[L2019-006]**, and the EBITDA headline weigh against here and are
carried to Q5, as "things that they do in public in relation to their investors and the promises they make" **[M2004-067]**.
Against them: the core-profit reconciliation is printed beside the GAAP figure, the GAAP statements are complete, and the
company publishes a ten-year free-cash-flow series after capital spending.

**Owner cash after every real cost** (operator rule 5; never a net-income proxy). Definitions, CONVENTIONS of this run,
each with its rationale: *all-equity owner cash* = net cash from operating activities (after tax paid; the filer puts
interest paid in financing and interest received in investing, so this figure is before both) - capital spending on
property, plant and equipment, intangibles, right-of-use assets and deposits for them + disposal proceeds of those assets +
dividends received from joint ventures, associates and financial investments (Q4's equity-method convention) + net cash
from commodity derivatives (part of the gas cost; the company's own core profit keeps the realised settlements) - lease
repayments - cash to minority holders of subsidiaries net of their contributions - purchases of shares for the award trust
- 25% of interest paid (the PRC statutory rate, removing the tax saving that debt gives, so that the all-equity figure is
the cash an unlevered owner would keep). Rationale: the owner of all the shares gets this cash before lenders, after every
cost of running and replacing the business. *Equity-only* = the same before the tax adjustment, less interest paid, plus
interest received. *Acquisitions* = net cash for subsidiaries, additional interests, joint ventures, associates and equity
investments, less disposals of the same. Excluded and said so: wealth-management products and restricted deposits
(cash-like), and advances to and repayments from third parties, joint ventures, associates and related companies (lending
balances that reverse; their net over 2021 to 2025 is small beside owner cash). RMB m, `scripts/owner_cash.py`:

| Year | Operating cash | Capital spending | D&A | Acquisitions, net | All-equity, before acquisitions | **All-equity, after acquisitions** | Equity-only, after acquisitions | Depreciation variant, after acquisitions |
|---|---|---|---|---|---|---|---|---|
| 2016 | 5,366 | 3,289 | 1,100 | 1,151 | 3,175 | 2,024 | 1,647 | 4,213 |
| 2017 | 6,093 | 4,719 | 1,156 | 431 | 1,384 | 952 | 753 | 4,516 |
| 2018 | 8,294 | 6,252 | 1,329 | 2,193 | 2,585 | 392 | -7 | 5,315 |
| 2019 | 11,690 | 7,526 | 1,784 | 1,399 | 4,670 | 3,272 | 2,867 | 9,014 |
| 2020 | 9,696 | 5,669 | 2,081 | 921 | 4,105 | 3,184 | 2,821 | 6,772 |
| 2021 | 10,466 | 6,398 | 2,263 | 649 | 4,008 | **3,358** | 3,044 | 7,494 |
| 2022 | 10,102 | 6,913 | 2,603 | 352 | 3,664 | **3,312** | 2,893 | 7,622 |
| 2023 | 9,612 | 6,987 | 2,840 | 537 | 3,012 | **2,475** | 1,996 | 6,622 |
| 2024 | 10,294 | 6,734 | 3,106 | 71 | 2,979 | **2,908** | 2,525 | 6,536 |
| 2025 | 10,433 | 7,092 | 3,486 | -226 | 3,484 | **3,710** | 3,364 | 7,316 |
| 2021-25 avg | | | | | 3,429 | **3,153** | 2,764 | 7,118 |

The 2018 acquisition figure excludes the RMB2.6bn paid in shares (no cash); 2025's net disposal includes RMB429m from
selling a financial asset. Cross-check against the company's own series ("10-Year Free Cash Flow Trend", 1H2026
presentation, after net finance costs and before minority dividends, leases and award purchases): RMB2,936m (2021), 2,365m,
2,132m, 3,734m, 3,871m (2025), the same order of magnitude as the equity-only column. Owner cash after every cost averages RMB3,153m on
the all-equity basis against reported profit attributable of RMB5,904m to RMB7,755m in the same years: the cash the owner
receives falls "considerably short" of reported earnings, as the speakers say of a network that must spend more than its
depreciation **[L2023-009]**.

- **Confusion or suspicion?** Neither found. The tells in the accounts were looked for **[M1995-064]**: prepaid and deferred
  accounts (other non-current assets RMB901m, mainly deposits and capitalised pipeline-safety renovation costs, Note 27,
  small), inventories in line with sales, reserves not moving with any share sale, no restatement found beyond the 2022
  comparatives restated in AR2023 on the application of amended accounting standards ("Comparative figures have been
  restated", AR2023 Note 2). The accounts can be read; they do not confuse
  **[M1995-063]**.
- **VERDICT on the accounts: no STOP; WEIGHS AGAINST.** The headline is an adjusted figure, EBITDA is featured in the
  presentation, guidance is given **[L2016-006]**, **[L2019-006]**, **[M1994-018]** (carried to Q5), and owner cash runs at
  about half of reported profit because spending runs at twice depreciation **[L2023-009]**. The recast owner cash feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The people: Mr. Wang Yusuo, founder (the group dates from 1993), chairman and controlling shareholder through ENN-NG;
Mr. Zhang Yuying, chief executive; Mr. Wang Dongzhi, chief financial officer; six executive directors, one non-executive
director (Mr. Wang Zizheng) and four independent non-executive directors (AR2025 Corporate Information). For a marketable
stake the speakers read rather than meet **[M2007-081]**; the two yardsticks are how they run it and how they treat the
owners **[M1994-008]**.

**First yardstick: the record against the hand dealt** **[M1994-008]**. The hand was a field whose returns fell for every
player (Q2's table). ENN's return on equity fell from 21.7% to 12.3% from 2021 to 2025, the least of the four companies
read, and stayed the highest of them; receivables fell to 8.1% of revenue; selling and administrative costs were held to
4.6% of revenue (Financial Review); the company reports no fatality in 2024 or 2025 (AR2025 Key Performance Highlights).
That is a business run well inside a worsening field.

**Second yardstick: how they treat the owners, read from the reports and the proxy** **[M1994-009]**.
- *The controlling family's dealings with the company.* (a) In 2018 the company bought from "a company controlled by Wang
  Family" an energy-technology business for RMB2,607m, paid entirely in 39,926,534 new shares, with goodwill of RMB1,998m,
  approved by independent shareholders with a whitewash waiver (AR2018 Directors' Report, Note 19). (b) In 2025 companies
  controlled by Mr. Wang supplied the group under continuing connected transactions within annual caps: equipment RMB306m
  (cap RMB400m), construction services RMB863m (cap 1,200m), information-technology services RMB281m (cap 530m), natural
  gas RMB1,652m (cap 1,750m), use of the Zhoushan LNG terminal RMB585m (cap 800m), "risk prevention services" RMB118m (cap
  220m), about RMB3.8bn in all (AR2025 Directors' Report; Note 52), against owner cash of RMB3.7bn that year. The
  independent non-executive directors confirm the terms as "normal commercial terms" and "fair and reasonable", and the
  auditor "has issued its unqualified confirmation letter" on them (Directors' Report). (c) A back-to-back agency
  agreement under which "a significant shareholder" bought RMB4,498m of gas for the company "at market price without
  charging any agency fees or commission" (Note 52). (d) The 2025 privatisation offer by ENN-NG, in ENN-NG H shares plus
  cash, kept the company in an offer period for fifteen months, during which the companies "have complied with, certain
  restrictions ... which have constrained certain aspects of their operations and management arrangements", and after its
  lapse ENN-NG "intends ... to increase its shareholding in ENN" in the market (announcement of 2026-06-12). A controller
  that may buy more in the market is not paid by a higher quotation; the rows ask whether, "if shareholders or somebody
  else has to suffer, the choice is likely to be that somebody else will be chosen" **[M1998-121]**, and say this reading is
  "hard to judge" in foreign countries (same row).
- *The pay*: modest. Total directors' emoluments RMB24.4m in 2025; the chief executive RMB4.93m (salary RMB2.4m, bonus
  RMB2.28m); the chairman RMB2.9m salary and no bonus (Note 11). Pay is read fully at Q6, Part B.
- *How they talk.* The Chairman's Statement is written in strategy jargon ("customer demand-driven, partner self-driven
  value creation", "Load-Source-Grid-Storage-Carbon", "de-involution"): "a standardized bunch of popular jargon that looks
  like it came out of the same consulting firm" is "a big turnoff" **[M1998-038]**, and it tells something when a letter is
  "the product of some investor relations department" **[M2007-083]**. No mistake is discussed: the word "mistake" appears
  once in AR2025, in a clause on misconduct "during the performance of his duties", and nowhere in the Chairman's Statement or the MD&A; the speakers'
  test is whether "mistake" or "wrong" are "forbidden words" **[L2024-003]**.
- *The habits carried from Q4*: the core-profit headline **[L2016-006]**, the EBITDA headline in the presentation, published
  guidance **[L2019-006]**. Read with the record: the reconciliation to GAAP is printed each time, the full statements are
  complete, and no instance found in the reports read of targets declared and then always met (the guidance found is a
  range for volume and a floor for the dividend). These are a weighing against, not doubt about honesty **[M1994-018]**.
- *The record searched for dishonesty*: a text search of AR2022 to AR2025 and the 2026 Interim Report for "litigation",
  "investigation", "penalty", "punish", "explosion", "antitrust" and "bundl" finds no proceeding, penalty or investigation
  against the group; the risk table names "pricing practices and bundled sales" in smart home as a risk it manages, and
  states that "fraud and compliance self-inspections were completed for more than 200 companies". No instance found of a
  restatement for error, a qualified audit opinion (Deloitte), or a regulator's sanction. No dancing around the key
  figure: the dollar margin, the connection decline and the debt are each reported plainly **[M1995-111]**.

**Love of the business.** The founder has run the business since 1993 and controls it through his own listed company; the
chairman takes a salary and no bonus. The love-or-money question **[M2000-098]** is answered by thirty years of building
one business, with the caveat that the controller's love may be for the group (ENN-NG, ENN Group), of which the listed
company is a part.

- **VERDICT on integrity: IN.** The record shows a controlling family that deals heavily with the company, on disclosed,
  capped, independently confirmed terms, and once sold it a business for shares; it shows no dishonesty, no misleading
  report and no sanction. Applying the rule on doubt **[M2013-088]**: the doubt here is about the terms of trade between a
  controller and the minority, which is a question about value given and received, weighed at Q6, not a doubt that these
  people would cheat; recorded and carried. **Ability WEIGHS FOR** on running the business (the best returns of the field
  in a falling field, costs and working capital held, safety) **[M1994-008]**; the capital half of the first yardstick is
  Q6's and weighs against there.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 profit attributable summed RMB32,329m and
  dividends paid RMB14,535m: RMB17,794m retained. Market leg (aggregator prices, flagged): HK$120.20 x 1,128.37m shares at
  end-2020 = HK$135.6bn; HK$67.35 x about 1,131.8m at end-2025 = HK$76.2bn (HK$56.8bn at today's price): the market value
  fell while RMB17.8bn was kept. Intrinsic leg, which the rows add because the market leg alone misleads **[R2009-002]**:
  owner cash after every cost and after acquisitions (all-equity) averaged RMB1,965m a year in 2016 to 2020 and RMB3,153m in
  2021 to 2025, an increase of about RMB1.19bn a year bought with about RMB32.2bn retained over 2016 to 2025 (profit
  attributable RMB52,048m less dividends RMB19,862m): about 3.7% on the money kept. A dollar kept has not become more than
  a dollar **[M1994-061]**; the presumption "becomes very strong at that point that we should start paying out money"
  **[M1998-110]**.
- **What they do with the money now.** Dividends of RMB3,059m in 2025 (HK$3.00 a share, payout 45.5% of core profit per the
  FY2025 presentation) against owner cash of RMB3,710m all-equity and RMB3,364m equity-only: they now pay out most of the
  cash the business throws off, and the rest of reported profit is the excess of accounting profit over cash, spent on
  capital at twice depreciation (Q3). The 2026 guidance promises a dividend of "No less than HK$3.00 per share". Paying out
  is right where the dollar cannot be employed at more than a dollar **[M2004-089]**; promising a floor regardless of the
  year's cash is a policy the rows would want "clear, consistent and rational" **[L2012-015]**, and this one is clear.
- **Buybacks.** No shares were bought for cancellation in 2019 to 2025 (small purchases of RMB29m in 2016 and RMB78m in
  2018). The trustee of the Share Award Scheme bought 4,047,500 shares in 2023 for about HK$250.2m (about HK$61.83 each) and
  13,252,000 in 2024 for about HK$731m (about HK$55.16 each), held for employees, not cancelled (AR2023, AR2024 Directors'
  Reports); a 2024 Board approval allowed "up to HK$300 million to buy-back Shares from the open market" (AR2025 Directors'
  Report), and none was bought in 2025. No stated price above which the purchases stop was found **[L2016-002]**.
  *Written back at Q7 (committed with Q7):* the prices paid, about HK$61.83 and HK$55.16, sit **below the bottom of Q7's
  range** at the sovereign (RMB133.70 = HK$156.09 a share, central all-equity case), so by the convention the purchases are
  read by what they did and do not weigh against for want of a stated price **[L1999-023]**; they sit far **above** the
  reporting fair price (HK$23.76), which is the figure at which the range's midpoint earns the floor. The low sovereign
  makes the range's bottom generous; the comparison is recorded, not leaned on. They were pay, not a return of capital.
- **Issuance and deals** **[L2014-012]**. The share count rose from about 1,082m (2016, weighted average, AR2016) to 1,131.84m (2026), about +4.5% in ten
  years, most of it the 2018 consideration shares; not serial issuance **[L2014-015]**. The 2018 purchase from the Wang
  family was paid wholly in stock: 39,926,534 shares for RMB2,606,595,755 (HK$3,194,122,681), HK$80.00 a share. **The one
  STOP (an all-stock deal in undervalued stock) is tested and not met** **[L2009-019]**: the rows' condition is a buyer whose
  shares sell "below their intrinsic value"; on no figure read was the stock cheap in 2018 (owner cash after all spending
  and acquisitions was RMB952m in 2017 and RMB392m in 2018 against a market value of roughly HK$74bn to HK$84bn in 2018 at
  aggregator prices), so the issue was not of undervalued stock. What it was: value given to the controlling family in shares for a business whose price was 77%
  goodwill, approved with a whitewash waiver that let the controller raise its stake without a general offer. Whether
  the company received as much as it gave **[L2014-012]** cannot be shown from the filings (the business was folded into
  integrated energy, whose segment profit rose from RMB903m in 2020 to RMB2,338m in 2025 with RMB1.4bn a year of capital
  spending). Weighs against.
- **The 2025 offer** was the controller's, not the company's use of money; it is read under Part B.
- **Part A WEIGHS AGAINST**: the retention test fails on both legs **[R1995-009]**, the capital spending earns little on its
  increment (Q3), and the one large deal of the decade was a related-party share issue **[L2014-012]**; mitigated by a
  payout that now passes most owner cash to the owners **[M2004-089]**.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**. Executive pay is salary plus a year-end bonus set "with
  reference to an individual employee's position, performance and ability" and "the profitability of the Company, ESG
  performance indicators", with "salaries paid by comparable companies" as a benchmark (AR2025 Corporate Governance Report).
  No charge for capital employed **[L1994-019]**, in a business whose problem is the return on added capital (Q3); peer
  benchmarking is the rows' ratchet **[L2005-015]**. The sums are small (directors RMB24.4m in total, Note 11). The Board
  extended, "at its discretion", the expiry of 60,000 options held by a former director to 27 March 2029 (Directors'
  Report): a small one-way favour **[L1994-020]**. The 2019 options at HK$76.36 held by directors were cancelled in 2025.
- **The board.** Chairman and controlling shareholder in one person; six executive directors, one non-executive, four
  independent non-executives at RMB600,000 a year each (Note 11). The independent directors and the auditor review the
  connected transactions each year (Q5). The board's capacity to check the controller is the open question; the rows say
  boards struggle most "if that person is also Chairman" **[L2014-026]**.
- **The owners as partners.** Guidance is given **[L2019-006]**; information is published to all holders at once through
  HKEXnews; the controller has dealt with the company in shares (2018), in services (RMB3.8bn in 2025) and by an offer in
  its own paper (2025), and now intends to buy more in the market. The 1993 factor is "The certainty with which management
  can be counted on to channel the rewards from the business to the shareholders rather than to itself" **[L1993-020]**:
  the dividends do reach the minority, and the services flow does reach the controller; neither is shown to be unfair.
- **Part B WEIGHS AGAINST**: pay without a capital charge and benchmarked on peers **[L1994-019]**, **[L2005-015]**, a
  chairman who is the controller **[L2014-026]**, guidance **[L2019-006]**; the sums are modest.

## Q7: WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**; value is "the discounted
value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, held as a range
**[L2000-024]**. Arithmetic in `scripts/q7.py`, output in `q7_output.txt`.

**Inputs.**
- *Cash input*: owner cash after every real cost (Q4), **all-equity basis, acquisitions deducted, total growth credited**
  (the default pair of specific (c)), averaged over the five-year window 2021 to 2025: **RMB3,153m**. Equity-only beside:
  RMB2,764m.
- *Price on the all-equity basis*: market value RMB48,621m + net debt RMB12,667m = **RMB61,288m**. Net debt at the latest
  filed balance sheet, 2026-06-30 (2026 Interim Report): bank and other loans RMB9,461m + RMB2,435m, senior notes RMB3,740m +
  RMB3,308m, less cash and cash equivalents RMB8,554m (the company's own figure, RMB10,390m), plus the dividend payable of
  RMB2,277m on the same balance sheet, which the filing states and which left the company after the balance-sheet date
  (the price is ex that dividend). Leases left out (their payments are charged in owner cash), restricted deposits left
  out, financial investments (RMB3,761m FVTPL, RMB151m FVTOCI) left out with only their dividends counted. Subsequent
  events stated in that filing: "no material events" (Interim Report). The early redemption of the US$550m 4.625% notes on
  2026-11-30 (announcement of 2026-10-09) exchanges cash for debt and leaves net debt about unchanged.
- *Rate*: 2.06%, ChinaBond 30-year government yield, 2026-10-16. *Floor*: about ten percent (CONVENTION, Q7), on owner cash
  after the company's own tax, no conversion **[M1994-004]**, **[L2002-020]**, **[M2003-149]**.
- *Whose tax*: the company's own. Its effective rate is 20.8% (2025) against the 25% statutory rate because of "Tax
  concession and exemption granted to certain PRC subsidiaries" of RMB316m (AR2025 Note 12), preferential rates granted
  for three-year periods and renewed; not a carryforward or credit running out inside ten years, so carried as continuing.
  At the statutory rate owner cash would be about RMB316m a year lower, which only lowers every return below.

**The specifics, each applied.**
- *Aggregate, not per share*: growth measured on aggregate owner cash.
- *(a) Cycle base*: neither end year of the window is aberrational on the filer's own description or in the series
  (RMB3,358m, 3,312m, 2,475m, 2,908m, 3,710m); no full gas-cost cycle can be marked in the owner-cash series. The literal
  window is used, with 2025 alone shown beside. 2025 includes RMB429m from selling a financial asset (Q4).
- *Growth shown*: 2.52% a year between the end years (RMB3,358m to RMB3,710m); between the halves (2021-23 average against
  2023-25) -0.28% a year. The series does not change sign, so the end-year rate is the one used **[L2005-003]**.
- *(b) Decline*: none on the central series; the series before purchases declines 3.44% a year and is shown beside.
- *(c) Acquisitions*: deducted, total growth credited. The filer reports no organic growth rate, so the organic pair is
  not shown; the before-purchases series is shown beside, labelled as total, not organic, growth. Net purchases 2021 to
  2025 were RMB1,383m against owner cash before purchases of RMB17,147m (8%): not a serial acquirer. No signed, unclosed
  deal and no merger in the window found. After year ten, when growth stops, purchases stop with them: the terminal cash is
  taken before purchases (multiplier 1.0877 on the central case).
- *(d) Working capital*: counted, inside operating cash flow each year; no single-year draw tied to one event.
- *(e) Growth spending*: **the filing states no maintenance figure and no split of capital spending into maintenance and
  growth** (Q3), so the guess the rows ask the manager to give **[M2000-144]** is not given, and the central case deducts
  all capital spending; the depreciation variant is shown beside, as the PG specific asks. Why the variant is not made
  central: depreciation is a fair proxy "in most companies" **[M1998-127]**, but not where the business must spend more
  than its depreciation to stay in place **[M2016-092]**, **[L2023-009]**; here capital spending ran at 2.0 to 2.8 times
  depreciation for five years while owner cash with depreciation in place of capex fell, the filing names safety
  renovation of existing pipe as a cost it capitalises (Note 27), and management guides RMB6.0bn of spending for flat to
  slightly growing volume (Q3). On that evidence the spending above depreciation has not bought growth and is at least
  partly required to stand still; to treat it as optional growth would credit the business with cash it has never
  delivered.
- *(f) The cap*: the shown rate, 2.52%, is above the 2.06% discount rate; the rule forbids carrying a rate above the
  discount rate after year ten, and none is carried (zero nominal growth after year ten) **[M1997-095]**. Inside the ten
  years the shown rate gives owner cash of about RMB4.0bn in year ten, 3.6% of 2025 revenue, below the highest owner-cash
  share of revenue in the filings read (4.7% in 2019), so the absurdity cut does not bind **[M1999-067]**.

**The floor, tested first** (Q7's CONVENTION of 2026-10-10, **[M2003-149]**). Expected return at today's price (the rate
at which each case's cash stream equals the price):

| Case | Base (RMB m) | Growth yrs 1-10 | Expected return at the price | Earns the floor? |
|---|---|---|---|---|
| **Central, all-equity, no growth** | 3,153 | 0% | **5.41%** | no |
| **Central, all-equity, shown growth** | 3,153 | 2.52% | **6.55%** | no |
| Equity-only, no growth (beside) | 2,764 | 0% | 6.00% | no |
| Equity-only, shown growth (beside) | 2,764 | 2.53% | 7.23% | no |
| Before purchases, all-equity, no growth / decline (beside) | 3,429 | 0% / -3.44% | 5.60% / 4.20% | no |
| Literal window, 2025 alone, no growth (beside) | 3,710 | 0% | 6.34% | no |
| Depreciation variant, no growth / shown (beside, not central, see (e)) | 7,118 | 0% / -0.60% | 11.76% / 11.32% | yes |

No case of the range earns the floor at the price: the central pair returns 5.4% to 6.6%, the equity-only pair 6.0% to
7.2%. Only the depreciation variant would, and it is not a case of the range for the reasons in (e).

**Value range (the reporting convention, at the sovereign):** RMB133.70 to RMB171.27 a share on the central all-equity
basis (whole-business value RMB163,999m to RMB206,512m less net debt RMB12,667m, over 1,131.84m shares) = HK$156.09 to
HK$199.95 a share = US$79.56 to US$101.92 an ADS, against the price of RMB42.96 = HK$50.15 = US$25.54 an ADS. Width 1.28 to
one, narrow. Equity-only beside: RMB128.24 to RMB161.62. The range sits three to four times above the price only because
the RMB sovereign is 2.06%: at that rate any stream yielding five percent is worth twenty times more than the price asks,
which is why the floor, not the width, decides.

- **Closes: OUT, on the floor.** "There’s just a point at which we drop out of the game." **[M2003-149]**; the expected return
  at the price is below the minimum on every case the analyst can defend, so the width and the screamer tests are not
  reached **[L2000-025]**, **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged,
  after the company's own tax. **All-equity (central): RMB20.35 a share** (RMB32,594m and RMB38,810m, averaged, less net
  debt RMB12,667m) **= HK$23.76 = US$12.11 an ADS**. **Equity-only (beside): RMB27.80 = HK$32.45 = US$16.54 an ADS.**
  Exchange rates: CFETS central parity 2026-10-16, HKD/CNY 0.85658, USD/CNY 6.7220 (USD/HKD 7.8475). No cheap price is
  reported.
- **COMPUTATION, NOT A CLEARANCE, beside: what the depreciation variant would do.** Were the filing to state a maintenance
  figure near depreciation, (e) would make that case central and, the growth bought being worth less than its cost, invert
  the range: top the depreciation variant at no growth (11.76% at the price, RMB303.77 a share at the sovereign), bottom
  the all-spending case at shown growth (RMB171.27). The floor would then be met on the top case, the width would be 1.8
  to one, and the fair price would be RMB37.87 = HK$44.21 = US$22.53 an ADS (RMB38,810m and RMB72,246m, averaged, less net
  debt), below today's price; the file would turn on the screamer test. Recorded so that a filing that states the
  maintenance figure can re-open the question; it does not decide this run.
- **VERDICT: OUT** **[M2003-149]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing **[M1996-006]**.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7 (the floor):** expected return at the price 5.41% (no growth) to 6.55% (shown growth) on the central
all-equity case, 6.00% to 7.23% equity-only, every case below the floor of about ten percent **[M2003-149]**. Value range at
the 2.06% RMB sovereign RMB133.70 to RMB171.27 a share (HK$156.09 to HK$199.95; US$79.56 to US$101.92 an ADS) beside the
price of HK$50.15 (RMB42.96; ADS US$25.54); reporting fair price RMB20.35 = HK$23.76 = US$12.11 an ADS (all-equity),
RMB27.80 = HK$32.45 = US$16.54 an ADS (equity-only). Q1 IN, Q2 IN (regulator-bounded franchise), Q3 against, Q4 no STOP and
against, Q5 integrity IN and ability for, Q6 against on both parts. The deciding judgment is Q7 (e): no maintenance figure
is stated, so all capital spending is charged; the depreciation variant, not central, would clear the floor (COMPUTATION
in Q7).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8, the alternatives.** The RMB 30-year government yield is 2.06% (ChinaBond, 2026-10-16); the central case's expected
  return at the price is 5.4% to 6.6%. No holding of the buyer was looked at (the blind rule).
- **Q9, debt and exposures.** Borrowings RMB18,944m at 2026-06-30 (bank and other loans RMB11,896m, senior notes
  RMB7,048m); the company's net debt RMB10,390m, net gearing 19.1% (1H2026 presentation). In 2025, pre-tax earnings plus
  finance costs covered finance costs 15.5 times (RMB9,207m against RMB593m), the coverage the rows ask for **[L2012-002]**.
  Foreign-currency borrowings US$1,039m, about 38% of the total, with US$400m hedged (hedge ratio 38.5%, Financial Review);
  the US$550m 4.625% notes due 2027 are to be redeemed on 2026-11-30 (announcement 2026-10-09). Short-term debt RMB8,785m
  at end-2025; net current liabilities RMB12,939m (end-2025) and RMB17,575m (2026-06-30), funded by customer prepayments and
  "unutilised banking facilities" (RMB16.0bn, FY2025 presentation); credit ratings BBB+ (S&P), Baa1 (Moody's), BBB+
  (Fitch), all stable. The senior notes require "Mr. Wang and any affiliate of him to retain certain percentage of
  shareholding over the Company, failing which the Company would be required to repay or repurchase all outstanding debts
  at predetermined prices" (Note 52). Guarantees for joint ventures and an associate: RMB584m utilised (Note 52). Named
  exposures: "Pipeline network leaks, explosions, and construction accidents may result in casualties and cause serious
  social impact" (risk table); two long-term international LNG contracts priced on oil or gas indices, partly hedged
  (Financial Review). The "little or no debt" criterion is stated for whole businesses **[R1997-001]**.
- **Q10.** Nothing found beyond the above.
- **Q12, how the money is made.** City-gas distribution, integrated energy and household appliances and services; none of
  the businesses the rows name. The filing names "risks associated with pricing practices and bundled sales" in smart
  home, sold to customers who depend on the company for gas (risk table); weighed nowhere, recorded here.
- **Q5 was reached and answered**; its integrity record (the 2018 share-paid purchase from the controlling family, the
  RMB3.8bn of 2025 continuing connected transactions, the lapsed 2025 offer and ENN-NG's stated intention to buy more in
  the market) is in Q5 and Q6, judged there.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 77109fa0, before the first download). **Not fully kept:** the
      reading and the arithmetic for Q2 to Q7 were done before the Q1 section was written; the sections were then written
      and committed one question at a time (Step 0 to Q1, Q2 and Q3, Q4, Q5, Q6, Q7, the close). A draft of the Q6
      buyback write-back line sat in `drafts/` and was committed with the Q6 commit, one commit before Q7; the run file's
      Q6 carried a placeholder until the Q7 commit.
- [x] Dispatched: the brief allowed per-question pathspec commits of the two paths; the lock is the dispatching session's
      (not checked from here); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched for this company; the accidental
      sightings (commit subjects of another company's run, two other companies' file names, the map and memory index) are
      declared under Contamination at the top and not used.
- [x] Every v5 id resolves (`scripts/check_run.py`: no E-ids, every M/L/R id in `principle_ledger_v5.csv`, every quoted
      fragment beside an id found in that row); every filing fact carries its document and date in place of an accession
      number (departure 3); no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance; the fair price
      and range are reporting figures.
- [x] Owner cash after every real cost (stock pay as the award-trust purchases, leases, minorities, capital spending in
      full), never a net-income proxy (operator rule 5). Sovereign: the ChinaBond curve, published by the Ministry of
      Finance's designated depository, flagged as the publisher for the issuing authority rather than the Ministry itself;
      FX from CFETS, the central bank's authorised publisher. Aggregator quotes (prices, ADS, the historical prices in Q6)
      flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations list, each question's own); after the STOP, the
      facts for Q8, Q9 and Q12 are under AFTER THE STOP; Q5 was answered, so no unjudged integrity flag is needed.
- [x] Not a point-in-time run; no anchor date applies.
- [x] `tools/run.py` produced no arithmetic lines for this name (not an SEC filer); nothing from it was used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded below the framework section).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **"Where the filing allows the maintenance guess" (Q7 (e)) is undefined, and here it decides the box.** If depreciation
alone allows the guess, the depreciation variant becomes central, the range inverts, the top case earns 11.8% at the
price, and the file turns on the screamer test with a fair price of about HK$44; if a stated figure or a maintenance and
growth split is needed, the file closes OUT on the floor. I read "allows" as the filing stating a maintenance figure or
split, because the row behind it is the manager's own guess **[M2000-144]**, and because this filing's evidence (capital
spending at twice depreciation for flat guided volume) argues against using depreciation; the operator may want the text
to say which. (2) **A very low sovereign empties the width and screamer tests.** At 2.06% the range at the sovereign sits
three to four times above the price for any business yielding five percent, so "IN only if the price is so far below that
no pencil is needed" would be met by nearly every name that passed the floor; only the floor and the fair price (at ten
percent) carry information. The text does not say how the screamer test reads when the sovereign is far below the floor.
(3) **The protocol's sovereign table has no RMB line.** I took the ChinaBond 30-year government point (the Ministry of
Finance's depository publishes the official curve; the Ministry publishes none of its own that I found), matching the
30-year tenor used for USD; the table could name it. (4) **"Expected return at the price" is not defined in the text.** I
used the rate at which each case's ten-year stream and flat terminal value equal the price, and applied the after-year-ten
stop of purchases (specific (c)) to the no-growth case as well as the growth case, since the text says "when growth stops"
without excepting the no-growth case; both readings are mine. (5) **Shares bought by an award trust** are neither a buyback
nor an issue in Q6's terms; I charged them as pay in owner cash (Q4) and kept the shares in the count. (6) **Minority
interests on the all-equity basis** are not addressed: I deducted the net cash paid to minority holders of subsidiaries
from owner cash rather than adding their equity to the price. (7) **A dividend payable on the latest balance sheet** is not
named among the "subsequent events" of the all-equity basis; I added it to net debt because the price is ex that dividend.

**Checks run before the final commit (2026-10-18):** `python tools/check_framework.py`: PASS (ledger 4280/4280 verbatim;
Test Runs phantom in 0 files; pointers 0 missing; v5 scope 0 outside). `scripts/check_run.py`: PASS (138 id citations, 100
distinct, none missing, no E-ids; 32 quoted fragments beside ids found in their rows; five filing quotes standing before
later ids reviewed by hand and confirmed as filing text attributed to their documents).
