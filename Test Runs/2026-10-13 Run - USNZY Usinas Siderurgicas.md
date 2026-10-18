# Company Run — Usinas Siderúrgicas de Minas Gerais S.A., Usiminas (B3: USIM5 / USIM3 / USIM6; OTC ADR: USNZY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run (operator rule 10). Foreign filer with no SEC annual filings: the primary documents are the
company's filings with the CVM (Brazil's securities regulator), recorded by document, date and CVM document number in
place of an accession number. Working folder: `Test Runs/_research 2026-10-13 USNZY/` (`notes.md`, the extraction
scripts, `data/` with the company's rows from the CVM open-data files, `q7_computation.py` and its output). Raw filings
sit in its `cache/` folder, gitignored. All amounts in R$ million unless marked; "R$ thousand" where the filing's own
figure is copied.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-13), after the run was committed: not held (`PORTFOLIO.md` carries no line for USNZY, USDMY, USIM3, USIM5, USIM6, Usiminas or Usinas Siderurgicas).

**CONTAMINATION, declared.** (1) Before the first fetch I ran a directory listing of `Test Runs/` filtered for "usnz",
"usim" and "usimin", to check the dated file name was free; it returned nothing. That is a listing the blind rule
forbids, made before I re-read the rule; nothing was seen and nothing is used. (2) The session's starting context
showed the subjects of the five most recent commits, which are a run of CSN (ticker SID) closing OUT at Q2 on iron-ore
cost against Vale, with its sovereign (NTN-F 2037, 12.57%) and its price figures. CSN is a Brazilian steel rival named
below. Nothing from that run is used: the CSN figures in this file are from CSN's own 20-F filings, steel segment (a
different segment from the one that run decided on); the sovereign was fetched independently from the Tesouro Nacional
file and happens to be the same day's figure. (3) The memory index loaded with the session names queue states and other
companies, nothing about this name. No `PORTFOLIO.md`, holding review, queue, resume-state or reading-list file was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **The ADR and its class.** EDGAR CIK 0000934823 holds only depositary filings. Two Form F-6 POS of 2017-11-09 amend
  two BNY Mellon facilities: accession 0001019155-17-000266 (common shares, Registration No. 333-147143) and
  0001019155-17-000265 (non-voting preferred shares, Registration No. 333-176425); each deposit agreement's receipt
  reads "Each American Depositary Share represents one deposited Share". The F-6 does not print the ticker. Over 429
  common trading days of the last two years, USNZY × USD/BRL divided by the B3 price has a median of 1.028 against the
  class A preferred (USIM5) and 1.052 against the common (USIM3) (aggregator data, Yahoo, flagged). **The run is priced
  in the class A preferred, USIM5, one ADR to one share**; the common trades about 2 to 4 percent lower. The two classes
  share earnings equally (2025 loss per share R$ (2.50) for ON and for PN, DFP 2025, statement of income).
- **Price:** R$ 7.15, USIM5, 2026-10-13 (Yahoo chart, aggregator, flagged: the day's volume field read zero at fetch, so
  this may be the last trade rather than the close; the close of 2026-10-09 was R$ 7.30; 2026-10-12 was a B3 holiday).
  USNZY US$ 1.40 on 2026-10-13 (thin: 200 ADRs). USIM3 R$ 7.02 on 2026-10-09.
- **Shares by class**, CVM capital composition (`dfp/itr_cia_aberta_composicao_capital`), ITR 2026-06-30 (CVM document
  159792, received 2026-07-30): issued 705,260,684 common (ON) and 547,818,424 preferred (PNA and PNB); treasury
  2,526,656 ON and 19,609,792 PN; **outstanding 702,734,028 ON + 528,208,632 PN = 1,230,942,660**. The same counts stand
  in every filing from DFP 2021 to the ITR of 2026-06-30 (no issue, no buyback; treasury PN fell from 20,019,445 at
  2020-12-31 to 19,609,792 at 2021-12-31). `python Screens/cover_shares.py USNZY` returns "NOT AN SEC REGISTRANT".
- **Market cap:** R$ 8,801m (1,230.94m shares at R$ 7.15; every class at the PNA price; at the ON price of R$ 7.02 the
  common would be about R$ 90m less).
- **Sovereign for the earnings currency (BRL):** **12.57%**, Tesouro Prefixado com Juros Semestrais (NTN-F) maturing
  2037-01-01, the longest nominal bond the Tesouro Nacional publishes, purchase rate of 2026-10-09 (Tesouro Nacional,
  Tesouro Transparente file `PrecoTaxaTesouroDireto.csv`, fetched 2026-10-13; 12.91% on 2026-10-08).
- **Filings read** (operator rule 4), all from the CVM (rad.cvm.gov.br; structured data from dados.cvm.gov.br):
  DFP (audited annual statements) FY2025, CVM document 154757, received 2026-02-13; DFP FY2023 version 2 (144312,
  2025-01-16), FY2021 (111713), FY2019 (90949), FY2017 (71440), for the segment notes 2016 to 2025; ITR 2026-06-30
  (159792, 2026-07-30), with its 2Q26 results release; the Formulário de Referência 2026, version 7 (159805,
  2026-07-30), sections 1.1 to 1.16, 2.1 to 2.11, 4.1 to 4.7, 8 and 11; the CVM open-data DFP and ITR files 2016 to 2026
  for the ten years of statements (`data/usim_*.csv`); the English 2025 Sustainability Report ("Usiminas_RA_2025_ing_vf2.pdf",
  usiminas.com, uploaded 2026-08). **One figure cross-checked against the filed statement:** consolidated net revenue
  FY2025 R$ 26,263,450 thousand in the CVM structured statement of income (DFP 154757, account 3.01) equals the total of
  the segment note (note 30, "26.263.450") in the filed DFP and the total in the Formulário section 1.3.
- `python tools/run.py USNZY`: "not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." No arithmetic printed; all
  arithmetic in this file is by hand from the CVM statements (`pivot.py`, `q7_computation.py`).
- **Owner cash after every real cost, by year** (equity basis, R$m; operating cash flow, which in these statements is
  after interest paid, income tax paid, pension cash and working capital, less purchases of fixed assets and
  intangibles, plus fixed assets sold, less lease principal and instalment tax payments, less dividends declared to the
  minority holders of the subsidiaries, from DMPL; `q7_computation.py`):

  | | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | Operating cash flow (DFC 6.01) | (310) | 877 | 510 | 1,972 | 3,759 | 5,297 | 997 | 4,568 | 989 | 2,179 |
  | Fixed assets + intangibles bought | (223) | (216) | (433) | (681) | (799) | (1,484) | (2,092) | (2,984) | (995) | (1,171) |
  | Depreciation, amortization, depletion | 1,216 | 1,172 | 1,030 | 992 | 1,000 | 983 | 903 | 1,062 | 1,226 | 1,275 |
  | Dividends to minority holders | (22) | (24) | (80) | (70) | (172) | (348) | (351) | (295) | (41) | (84) |
  | **Owner cash, equity basis** | **(551)** | **642** | **37** | **1,230** | **2,910** | **3,569** | **(1,414)** | **1,263** | **(99)** | **925** |
  | Owner cash before net interest (all-equity basis) | (57) | 1,032 | 347 | 1,422 | 3,105 | 3,793 | (1,391) | 1,219 | (85) | 1,080 |

  Five-year average 2021 to 2025: R$ 849m equity basis, R$ 923m all-equity. Ten-year 2016 to 2025: R$ 851m and R$ 1,046m.
  Spending on fixed assets and intangibles over the ten years, R$ 11,078m, against depreciation of R$ 10,859m. No stock
  pay line appears in the cash flow statement (Formulário 8.4 to 8.12 read; long-term variable pay is in cash, "remuneração
  variável de longo prazo"). The cash flow includes the movement in forfaiting (supplier finance owed to banks):
  (400), 118, 491, (352), 267, (163), 220, 642, (713), (294) in 2016 to 2025; the balance was R$ 570.1m at 2025-12-31
  (R$ 864.1m a year earlier; DFP 2025, note on forfaiting).

- **The balance sheets, ten years and the latest half** (CVM structured data, consolidated, R$m; the reading Q4 asks for,
  done here because the file closes before Q4):

  | 31 Dec | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 30 Jun 26 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Total assets | 26,255 | 25,984 | 26,524 | 26,337 | 29,952 | 39,482 | 40,000 | 40,162 | 39,872 | 35,685 | 35,107 |
  | Cash + short investments | 2,258 | 2,315 | 1,694 | 1,921 | 4,868 | 7,024 | 5,072 | 6,010 | 5,954 | 6,944 | 6,822 |
  | Receivables | 1,179 | 1,555 | 1,894 | 1,938 | 2,373 | 3,563 | 3,548 | 3,509 | 3,157 | 3,003 | 3,070 |
  | Inventories | 2,604 | 2,763 | 3,881 | 3,796 | 3,890 | 7,516 | 9,965 | 7,493 | 7,452 | 5,929 | 5,920 |
  | Fixed assets | 13,749 | 12,883 | 11,715 | 11,425 | 11,006 | 11,086 | 10,821 | 12,879 | 12,767 | 10,424 | 9,906 |
  | Intangibles (goodwill nil) | 694 | 677 | 696 | 727 | 1,598 | 1,651 | 1,976 | 1,964 | 1,973 | 2,014 | 1,939 |
  | Deferred tax assets | n/a | n/a | 2,765 | 3,038 | 2,914 | 2,982 | 2,410 | 3,100 | 3,258 | 1,974 | 2,197 |
  | Borrowings and debentures | 6,925 | 6,636 | 5,850 | 5,106 | 5,968 | 6,300 | 6,198 | 5,916 | 6,769 | 6,390 | 6,224 |
  | Provisions (non-current) | 2,094 | 1,878 | 1,873 | 2,584 | 2,501 | 2,293 | 2,128 | 2,089 | 1,448 | 1,364 | 1,315 |
  | Equity incl. minority | 15,192 | 15,184 | 15,697 | 15,566 | 16,838 | 24,359 | 25,888 | 26,549 | 26,684 | 23,701 | 23,645 |
  | of which minority interests | 1,656 | 1,409 | 1,431 | 1,522 | 1,971 | 2,609 | 2,733 | 2,694 | 2,802 | 2,888 | 2,894 |

  *What moved and why.* Equity rose by R$ 7.5bn in 2021 alone, the year of R$ 10.1bn of net income, and from its 2024 peak has given back
  R$ 3.0bn since (the 2025 loss of R$ 2.9bn: a R$ 2,214m impairment of steel assets and a R$ 1,284m deferred tax charge,
  which shows in the deferred tax asset falling from R$ 3,258m to R$ 1,974m). There is no goodwill; intangibles moved up
  R$ 0.9bn in 2020 (cause not read). Inventories went from 31% of sales in 2016 to 31% in 2022 (R$ 9,965m, at the coke
  plant failure of 2022, Formulário 1.4) and 23% in 2025; receivables have stayed between 11% and 15% of sales since
  2017. Debt has hardly moved in ten years (R$ 5.1bn to R$ 6.9bn) while cash tripled: from net debt of about R$ 4.7bn in
  2016 (after the 2016 creditor restructuring, "aproximadamente 92% do endividamento total", Formulário 1.1, and a
  R$ 1,050m capital increase received in 2016, DFC) to net cash of R$ 499m at 2026-06-30 on the company's own figure
  (2Q26 release in ITR 159792: cash and investments R$ 6,823m, gross debt R$ 6,324m). Fixed assets fell from R$ 13.7bn
  to R$ 9.9bn: spending below depreciation in 2016 to 2019 (R$ 216m to R$ 681m against about R$ 1bn), the blast-furnace
  reline spend of 2022 and 2023, then the 2025 impairment. What the figures do not say: the cost per tonne of the
  steel the plants make, which the filings read do not state; that is read at Q2 from margins.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what the Ipatinga and Cubatão plants and the Serra Azul mines
will earn, not where USNZY trades. The foundation that bears hardest is "no macro forecast enters": the case for this
name, as its own management states it, rests on Brazil's trade-defence measures against imported steel and on the
iron-ore price, both of which are forecasts the speakers decline to make, "macro conclusions are — just never enter into
the discussion" **[M2000-094]**, "We don’t think we can predict commodity prices." **[M2016-025]**. The currency is a
second foundation: owning a BRL business through a USD receipt is, in part, "a bet on how government now, and in the
future, will behave" **[M2011-025]**. Who is paid to tell you: the controlling group (Ternium/Tenaris, 71.02% of the
common shares after the NSC sale) consolidates Usiminas and is also its slab supplier (Q5 facts below). **Contrary
evidence, written down as found** **[M1997-127]**: (1) the business has improved: H1 2026 operating profit R$ 954m
against R$ 572m in H1 2025, the steel unit's adjusted EBITDA R$ 688m in 2Q26 up 26% on 1Q26 (ITR 159792 and its
release); (2) the balance sheet is now net cash; (3) the price is below what the controller paid NSC and Mitsubishi in
July 2025, "aproximadamente, US$ 2,06" a common share (Formulário 1.1), against US$ 1.40 for the ADR today; (4) the
company is "a maior fornecedora de aços planos para os principais segmentos consumidores do país" (Formulário 1.4).

## THE STANDING RULE
Bought for cash, unlevered, in a size the buyer can hold through a fall, a part-interest in Usiminas cannot put the
buyer at risk of ruin: the rule forbids the buyer's borrowing, "It’s the one thing that forces you" **[M2004-065]**, and
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. Nothing in
the target can call on the holder. Not a bar.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (Formulário 1.2 to 1.4; DFP 2025 note 30). Two reporting segments. *Steel* (Siderurgia):
  the integrated Ipatinga works (blast furnaces, coke plants, plate, hot and cold rolling; galvanizing through the
  Unigal joint venture with Nippon Steel), the Cubatão works, which since 2015 only rolls slabs bought in ("A usina de
  Cubatão é abastecida por placas", Formulário 1.3; primary areas stopped in 2015 and the blast furnaces written off
  from September 2021, Formulário 1.1), the Soluções Usiminas service centres and Usiminas Mecânica. Sales 4.36 Mt in
  2025, 90.4% domestic; automotive 30.9%, distribution 33.5%, industry 35.6% of volume. *Mining and Logistics*
  (Mineração Usiminas, 70% owned, the rest a minority interest): Serra Azul iron ore, 9.64 Mt sold in 2025, 7.03 Mt of it
  exported.
- **The key variables** **[M1998-044]**: (1) the domestic flat-steel price, which the company says is held near "subsidized
  import prices" (2025 report, p. 155: "competitive practices that bring domestic prices closer to subsidized import
  prices undermines the sector's profitability"); imports took 25.6% of Brazilian flat-steel consumption in 2025, 4.21
  Mt, up 29.5% (Formulário 1.4); (2) the cost of Ipatinga's steel against the other mills and the import parity: coal and
  coke are imported, slabs are bought (from the controller's Ternium Brasil under a contract of R$ 4,344m,
  Formulário 11.2); (3) the iron-ore price and the sea freight for the mining part; (4) the real.
- **Can the ten-year economics be foreseen?** Steel and iron ore are commodities, and a dependence on a commodity price
  "is never by itself a STOP at Q1 or Q2" under the framework's commodity paragraph; the test is whether the business can
  be read off its figures, "if you can’t make a decision on something like PetroChina off the figures, forget about going
  further" **[M2008-069]**. It can: two plants, one mine, a domestic market, segment accounts for ten years, and the
  economic dynamics are plain, "What is important is that I understand the economic dynamics of the industry"
  **[M2011-014]**. Where the business will be in ten years in the sense of **[M2012-065]**, "a reasonable fix on about
  what the earning power and competitive position will look like in five or 10 years", turns on its cost position against
  the other mills and the importers, which is a Q2 question and is answerable from filings **[M2009-059]**.
- **Abroad.** Brazil's governance and tax are a known extra layer: the company is controlled by a foreign steel group
  that is also a counterparty, the preferred shares carry no vote, and the tax rules are Brazilian **[M2000-141]**. The
  rows ask a lower price for it, not a pass: "Brazil would not be off limits at all [...] We would want it to be cheaper
  than if it were in the United States." **[M2006-021]**.
- **Parts.** Read by part **[L2008-005]**; both parts are commodity businesses of the same kind and both are understood.
  Which part decides is Q2's table.
- **VERDICT: IN.** The economics are readable from the filed figures **[M2008-069]**, **[M2011-014]**; the deciding
  variable, cost position, is knowable from the filer's and the rivals' filings **[M2009-059]**; no doubt about the
  perimeter beyond the foreign-governance layer, which the rows price rather than exclude **[M2006-021]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question as asked:** "why is that castle still standing? And what’s going to keep it standing or cause it not to
be standing five, 10, 20 years from now." **[M1995-038]**. For a commodity business the framework's paragraph puts the
test on cost: "we would measure it, probably, more by cost of production than we would by whether copper was selling for
$2.00 a pound or a dollar a pound" **[M2006-004]**, read from the producer's own and its rivals' filings, "The figures
are available." **[M2009-059]**.

**The parts table** (segment note of each DFP: 2025 note 30, 2023 v2 note 29 with 2022 restated, 2021 note for 2020 and
2021; operating result of each segment before inter-segment eliminations, R$m; the equity-method line taken out, because
most of the steel segment's is its share of the mining subsidiary that the eliminations remove; the as-reported figure
beside):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year | Share | As reported, five-year | Share |
|---|---|---|---|---|---|---|---|---|---|
| Mining and logistics | 3,335 | 1,140 | 540 | 106 | 320 | 5,441 | 40.5% | 6,140 | 33.3% |
| Steel (with steel transformation, merged into it from 2023) | 8,439 | 1,374 | 86 | 76 | (1,990) | 7,986 | **59.5%** | 12,290 | 66.7% |

**Steel decides** (more than half of the five-year operating profit on either reading; the framework's business-of-parts
paragraph, **[L2008-005]**). Written down at once **[M1997-127]**: the steel share rests on one year. 2021 alone gave
steel R$ 8,439m; over 2022 to 2025 steel earned R$ (453)m and mining R$ 2,106m, and mining was the larger part in four of
the five years. The 2025 steel figure carries the R$ 2,214m impairment, which the DFP places in the steel segment
("a perda por impairment reconhecida no segmento de siderurgia", DFP 2025, note on impairment); before it steel earned
R$ 225m in 2025. Mining does not decide; it is carried to Q7 as an ordinary business at no growth.

**The competitor row.** Usiminas's own documents name no rival: the Formulário says only that competition "se dá tanto
com relação às demais usinas, como também em relação às importações" (1.4), and a sweep of the Formulário and the DFP 2025
for "concorr", "ArcelorMittal", "Gerdau" and "CSN" finds the names only in a port-terminal lawsuit. I took the other
Brazilian flat-steel mills ("demais usinas") that file with the SEC on Form 20-F: **CSN** (Companhia Siderúrgica Nacional,
steel segment), **ArcelorMittal** (Brazil segment, which also holds long steel and Acindar in Argentina; reported in US$),
and **Gerdau** (Brazil operation, mostly long steel, with Ouro Branco's flat products). Not filing with the SEC: ArcelorMittal
Brasil itself, and the importers, who are the price-setters (Formulário 1.4: 4.21 Mt, 25.6% of consumption in 2025, 69%
of it from China). Metric: segment operating result over segment net revenue, every year 2016 to 2025.

| Year | **Usiminas steel** (1) | CSN steel (2) | Gerdau Brazil (3) | ArcelorMittal Brazil (4) |
|---|---|---|---|---|
| 2016 | **(5.4)%** | 10.5% | 4.8% | 9.9% |
| 2017 | **7.3%** | 11.2% | 7.7% | 9.0% |
| 2018 | **7.2%** | 13.0% | 13.3% | 15.6% |
| 2019 | **2.3%** | 1.1% | 9.4% | 10.4% |
| 2020 | **2.5%** | 6.7% | 17.0% | 12.3% |
| 2021 | **30.3%** | 28.1% | 33.4% | 29.5% |
| 2022 | **4.8%** | 13.6% | 15.5% | 20.2% |
| 2023 | **0.4%** | (2.5)% | 8.1% | 11.1% |
| 2024 | **0.3%** | (3.2)% | 9.3% | 11.3% |
| 2025 | **(8.8)%**; 1.0% before the impairment | (1.9)% | 2.9% | 5.4% |
| Ten years, summed | **5.4%** (0.9% without 2021) | 8.4% | 13.4% | 14.3% |

(1) Steel, steel transformation and capital goods segments, operating result less their equity-method income, over
consolidated net revenue less the mining segment's revenue (this denominator removes the steel segments' sales to each
other, which the 2016 to 2021 notes do not eliminate; it slightly flatters Usiminas). Leaving out the equity line also
leaves out Unigal, the galvanizing joint venture; its effect is under one point a year (the whole group's equity income
ran R$ 143m to R$ 301m). (2) CSN Form 20-F: FY2025, accession 0001292814-26-002714 (2023 to 2025, "Operating result before
Financial Income and Taxes"); FY2022, 0001292814-23-001912 (2020 to 2022); FY2019, 0001292814-20-001135 (2017 to 2019) and
FY2018, 0001292814-19-001150 (2016): for 2016 to 2019 the segment note gives adjusted EBITDA, so the figure is adjusted
EBITDA less the segment's depreciation. (3) Gerdau Form 20-F: FY2025, 0001104659-26-027678 (2023 to 2025: gross profit less
SG&A and other operating items); FY2022, 0001104659-23-040166 (2020 to 2022); FY2019, 0001104659-20-041231 (2017 to 2019);
FY2016, 0001104659-17-016620 (2016); the Brazil operation's scope changed in 2023 when special steels were folded in.
(4) ArcelorMittal Form 20-F, Brazil segment, sales and operating income in US$: FY2025, 0001243429-26-000020 (2024, 2025);
FY2023, 0001243429-24-000005 (2023); FY2022, 0001243429-23-000005 (2020 to 2022); FY2019, 0001243429-20-000004 (2017 to
2019); FY2016, 0001243429-17-000002 (2016).

Usiminas's steel margin is the lowest of the four in six of the ten years (2016, 2017, 2018, 2020, 2022, 2025), below
Gerdau's Brazil operation in all ten and below ArcelorMittal Brazil in nine (all but 2021), and over the decade it earned
5.4 cents of operating profit per real of sales against 13 to 14 cents at the two larger rivals. It sits above CSN's steel
segment in 2019, 2021, 2023 and 2024, so the bottom of the field is shared with CSN. Contrary evidence, written down
**[M1997-127]**: in the first half of 2026 the steel segment's operating result before equity income was R$ 794m on
R$ 10,625m of revenue, 7.5% (ITR 159792, segment note 26), after the blast-furnace coal-injection project and the new
anti-dumping measures.

**The field's returns over the last full cycle.** Usiminas's steel side held R$ 32.6bn to R$ 38.5bn of assets in 2021
to 2025 (segment notes) and earned R$ 7,986m of operating profit before tax over those five years, about 4.4% a year
before tax on its assets, all of it from 2021; over 2016 to 2025 the steel side earned R$ 9,806m, under R$ 1bn a year,
on assets of R$ 26.0bn in 2017 (DFP 2017 segment note) and more in every later year. CSN's steel segment lost money at the operating line in each of 2023, 2024 and
2025. Against a long government rate of 12.57%, those are not even ordinary returns for the two flat-steel integrated
mills; only ArcelorMittal Brazil, the low-cost slab producer of the field, earned a double-digit margin through the cycle.

**The castle tests, with the filing fact.**
- *Low-cost position* **[M1997-010]**: "commodity businesses have risk unless you’re the low-cost producer". The margins
  above say Usiminas is not the low-cost producer of its field. Its own plant history says the same: Cubatão's primary
  steelmaking was stopped in 2015 and its blast furnaces written off in 2021 (Formulário 1.1); Cubatão now rolls
  bought-in slabs, and the company buys slabs under a 2023 contract of R$ 4,344m with the controller's Ternium Brasil
  (Formulário 11.2).
- *Who sets the price* **[M2012-109]**: "whatever he charged for gas was my price." The company's words: "competitive
  practices that bring domestic prices closer to subsidized import prices undermines the sector's profitability" and its
  revenue per tonne fell 4% in 2025 while Brazilian flat-steel consumption rose (2025 report, p. 155-156). The importer
  sets the price; the product "can be shipped in from abroad very easily" **[M2007-116]**.
- *Pricing power* **[M2005-020]**: the strength of a business is measured "by the agony they go through in determining
  whether a price increase can be sustained". The filings show the agony: the price rises the 2Q26 outlook expects come
  after the government's trade-defence measures, and the company asks for more of them ("É fundamental continuar com os
  processos de defesa comercial", ITR 159792, management's comments).
- *The money test* **[M2011-015]**: the attacker with money is already inside the walls; imports in 2025 were "more than
  three times higher than that recorded in 2020" (2025 report, p. 156).
- *Widening or narrowing* **[M1999-108]**: narrowing on the record: imports more than tripled from 2020 to a quarter of
  consumption in 2025, a plant's primary areas closed, a R$ 2.2bn impairment in 2025.
- *Evidence for a castle*: the automotive and industrial customers buy specified grades with service attached
  (Formulário 1.4; Volkswagen's supplier award, 2025 report); the company names its advantage as "close ties with
  Brazilian customers and engagement with the domestic market" (2025 report, chairman's message). Neither shows in the
  margins against the other mills over ten years.
- *A change for the better* (the 2026 trade-defence measures, the coal-injection project): the framework credits it only
  after a full cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**; the railroads "were a terrible
  business for decades and decades and decades and then they got good." **[M2017-026]**, but that is shown, not assumed.
  The protection is also a government's decision, a macro fact **[M2000-094]**, not a property of the business.

**Price does not reopen it:** "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**.

- **VERDICT: OUT.** The deciding part, steel, is a high-cost producer in a commodity field, and "In an unregulated
  commodity business, a company must lower its costs to competitive levels or face extinction." **[L1994-035]**; its
  price is set by imports **[M2012-109]**, **[M2007-116]**; and on its own and its rivals' filings the field's integrated
  flat-steel mills earned less than ordinary returns over the full cycle, where a moat is what "protects excellent returns
  on invested capital" **[L2007-004]** and "you can have only two competitors and they’re still terrible businesses"
  **[M2013-052]**. The castle is shown open on the evidence, so the box is OUT, not TOO HARD.


## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed OUT at Q2; operator rule 2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets were read at Step 0, as the template asks when the file closes before Q4; the facts
found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part, steel (59.5% of five-year segment operating profit), is not the low-cost producer of a
commodity field whose price imports set, and the field's integrated flat-steel mills earned less than ordinary returns
over the cycle on their own and their rivals' filings. **Integrity facts recorded, not judged.** Beneath the stop,
COMPUTATION, NOT A CLEARANCE: value range R$ 5.51 to R$ 7.17 a share on the all-equity basis (equity-only R$ 5.46 to
R$ 5.50) against R$ 7.15; fair price R$ 7.78 all-equity, R$ 6.89 equity-only. No research pass: the box is OUT, not TOO
HARD (WORK).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box is unchanged (operator rule 2) **[M1997-127]**.*

**Bearing on Q3 (capital).** The steel side held R$ 32.6bn of assets at 2025-12-31 and R$ 38.5bn at 2021-12-31 (segment
notes). Over 2016 to 2025 fixed assets and intangibles bought, R$ 11,078m, against depreciation R$ 10,859m: spending ran
well below depreciation in 2016 to 2019 (R$ 216m to R$ 681m a year against about R$ 1bn), then the blast furnace 3 reline
years of 2022 and 2023 (R$ 2,092m and R$ 2,984m). Rebuild projects announced and running: coke-plant 2 battery 4
reconstruction, about R$ 1.7bn, to 2029; battery 3 hot repair, about R$ 978m, to 2028; coal-injection plant, about R$ 597m;
a new gas holder, about R$ 233m, to 2027 (2025 report, p. 156). Steel sales were 4.36 Mt in 2025, "the second-highest
volume in the last ten years" (2025 report, p. 156): the spending keeps the plant in place rather than growing it.

**Bearing on Q4 (the accounts).** The 2025 net loss of R$ 2,910m carries a R$ 2,214m impairment of steel assets and a
R$ 1,284m deferred tax charge (DFC 2025, lines 6.01.01.12 and 6.01.01.08). EBITDA in the filer's own mouth: "EBITDA
ajustado" of R$ 1,993m for 2025 is the headline figure of the 2025 report ("Adjusted EBITDA: 2.0 R$ billion", p. 154)
beside an EBITDA under CVM Resolution 156 of R$ (89)m; the adjustment removes the impairment and the equity income and adds
70% of Unigal's EBITDA (Formulário 2.5). The quarterly release gives an outlook for the next quarter ("Para o próximo
trimestre, a expectativa é de estabilidade nos resultados operacionais da Siderurgia [...] e de queda na Mineração", ITR
159792, management's comments). Operating cash flow includes forfaiting (bank-financed supplier payables), whose balance
was R$ 570.1m at 2025-12-31 and R$ 864.1m a year before; the movement is inside operating cash every year. No confusion
was met in the statements read; whether these habits weigh against is Q4's and Q5's question, not answered here.

**Bearing on Q5 (integrity facts recorded, not judged).** (1) The controlling group is also a counterparty, on the
Formulário 11.2 list of related-party contracts: slabs bought from Ternium Brasil under a 2023 contract of R$ 4,344m;
assembly services from Techint Engenharia e Construção, R$ 354m (2024); raw materials through Exiros, R$ 357m (from 2020);
steel sold to Tenaris's SIAT, R$ 593m, and to Confab, R$ 304m (2025); royalties to Nippon Steel, R$ 419m (since 2009);
raw materials from Mitsubishi RTM Japan, R$ 501m (2024). (2) Control changed hands in January 2026: NSC and Mitsubishi
sold their 21.71% of the common shares to Ternium at about US$ 2.06 a share, leaving the T/T group with 71.02% of the
common (Formulário 1.1 and 1.13); the preferred shares carry no vote. (3) The adjusted figure featured and the quarterly
outlook given (Q4 above). (4) Pay: the six statutory officers received R$ 29.3m in 2025, of which bonus R$ 12.5m; the
board R$ 4.7m; the shareholders approved a ceiling of R$ 41.5m for 2026 to 2027 (Formulário 8, CVM open data). Any later
run that reaches Q5 must answer these first **[M2013-088]**.

**Bearing on Q6 (the money and the owners).** No buyback: the treasury counts are unchanged from 2021-12-31 to 2026-06-30
(CVM capital composition). Dividends and interest on capital paid (consolidated, including to the subsidiaries' minority
holders): R$ 0m, 26, 125, 255, 68, 1,849, 1,233, 727, 384, 43 in 2016 to 2025 (DFC 6.03.06); the by-laws' minimum is 25% of
adjusted net income (Formulário 2.7). A capital increase of R$ 1,050m was received in 2016 (DFC 6.03.10). Equity
attributable to the parent's shareholders went from R$ 13,536m at 2016-12-31 to R$ 20,751m at 2026-06-30, against a market
value today of about R$ 8.8bn. No acquisition in ten years (DFC 6.02.02 nil in every year).

**Bearing on Q9 (debt and exposures).** Net cash of R$ 499m at 2026-06-30 on the company's figure (cash and investments
R$ 6,823m, gross debt R$ 6,324m); a US$ 500m bond due 2032 issued in January 2025, the 2026 bonds largely bought back,
"no significant amortization payments due until 2028" (2025 report, p. 156). Provisions for tax, labour and civil claims
R$ 1,103m (BPP 2.02.04.01, 2025). Unprovided claims rated possible loss are itemized in the DFP 2025 contingencies note,
chiefly São Paulo and Minas Gerais ICMS tax claims from R$ 3m to R$ 790m each (not summed here). Forfaiting R$ 570.1m at
2025-12-31 sits outside reported debt. The pension fund Previdência Usiminas is a party to the shareholders' agreement
(Formulário 1.13).

### COMPUTATION, NOT A CLEARANCE: the value range and the fair price
*Reporting figures at the owner's request (Part VII, The owner's price). Not a verdict and carrying no entry language
(operator rule 3). Script and output: `Test Runs/_research 2026-10-13 USNZY/q7_computation.py`, `q7_output.txt`.*

- **The cash input** is owner cash after every real cost as tabled at Step 0, after the company's own cash taxes (no
  conversion; Q7, Whose tax), after dividends declared to the minority holders of the subsidiaries (Mineração Usiminas is
  70% owned). All-equity basis: owner cash before net interest, interest paid less income on financial investments added
  back net of a 34% tax shield. **CONVENTION of this run:** the 34% shield is Brazil's statutory income-tax and social
  contribution rate; rationale: the framework names the all-equity basis but no shield rate, and the company's own cash
  tax rate is distorted by carryforwards.
- **(a) Cycle.** The window's first year, 2021, is the cyclical peak of the decade on the filer's own figures (operating
  profit R$ 11,490m, four times any other year; owner cash R$ 3,569m). The base is the ten-year average 2016 to 2025, which
  runs from the trough of the 2016 restructuring through 2021's peak to 2025: **R$ 851m equity basis, R$ 1,046m
  all-equity**. Literal window 2021 to 2025 beside: R$ 849m and R$ 923m. Trough to trough 2016 to 2024: R$ 843m equity basis.
- **(b) Decline.** The series changes sign (2016, 2022, 2024), so growth is measured between the halves of the cycle:
  equity basis R$ 853m (2016 to 2020) to R$ 849m (2021 to 2025), (0.11)% a year; all-equity R$ 1,170m to R$ 923m,
  (4.63)% a year. A decline is carried as the bottom of the range, the no-growth case as the top.
- **(c) Acquisitions:** none in the window. **(d) Working capital:** counted (inside operating cash; the forfaiting
  movement left in, its balance shown beside net debt). **(e) Maintenance:** spending over the decade equals depreciation
  and the named projects are rebuilds; the filing allows the guess that all spending is maintenance, so the central case is
  the all-spending case, and no growth spending is separated. **(f) The cap:** not reached (no positive growth).
- **The rate and the horizon:** NTN-F 2037, 12.57%; ten years, then zero nominal growth (the PG specifics).
- **Net debt** at 2026-06-30, as the company states it: **net cash R$ 499m**, added on the all-equity basis. Forfaiting of
  about R$ 177m at 2026-06-30 (R$ 570.1m at year-end less the H1 2026 outflow of R$ 393m) shown beside, not in.
- **Value range: R$ 5.51 to R$ 7.17 a share (all-equity, central), against R$ 7.15.** Equity-only beside: R$ 5.46 to R$ 5.50.
  With forfaiting counted as debt, the top is R$ 7.02.
- **The floor, tested first:** at R$ 7.15 the no-growth all-equity case yields 12.60% on the enterprise value, which earns
  the floor of about ten percent; the declining case does not (valued at ten percent it is worth R$ 6.66). Width 1.3 to
  one, so not TOO HARD by width; the price sits inside the narrow range, just below its top: by Q7's text this would close
  **OUT** (not a screamer) **[M2009-005]**, had the file reached it.
- **Fair price** (each end case valued at ten percent, the two averaged; Part VII): **R$ 7.78 a share all-equity
  (central)**, **R$ 6.89 equity-only** (beside); R$ 7.64 all-equity with forfaiting counted as debt. The all-equity fair
  price sits above the top of the value range because the floor (about ten percent) is below the BRL long government
  rate (12.57%); see the last section.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9d9558f8); written question by question; committed after Q1 and
      after Q2, and after this closing section.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock and the fold are the dispatching session's
      (operator rule ten). A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched: **not fully kept.** No file was
      opened, but one filtered listing of `Test Runs/` for this company's names was run before the first fetch and returned
      nothing; and the starting context showed the CSN run's commit subjects. Both declared under CONTAMINATION; nothing used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in its row (check script
      `check_cites.py` in the research folder). Filing facts carry CVM document numbers or SEC accessions.
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance; the computation is headed as such.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (Tesouro Nacional); aggregator quotes (Yahoo) flagged.
- [x] Contrary evidence written down as found (the foundations; the 2021 dependence of the parts table; H1 2026 steel
      margin of 7.5%; the 2026 trade measures); later-question facts are under AFTER THE STOP, with the integrity flag in
      the box line.
- [x] No row dated after the anchor is cited (not a point-in-time run).
- [x] `tools/run.py` printed no arithmetic for this name; none of its output was used.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The floor below the long rate.** The floor convention takes its figure of about ten percent from rows spoken against US long
rates of about 7% (**[M1994-004]**), and Part VII computes the fair price at ten percent. In BRL the issuing authority's
long rate is 12.57%, so the "fair price" (R$ 7.78) lies above the top of the value range discounted at the sovereign
(R$ 7.17): a price could be "below fair" while above every case of the range. The rows say the floor moves with a lasting
change in rates (**[M2003-151]**); the text gives no rule for a currency whose long rate is above the floor. I reported both
figures as the text defines them and did not substitute the sovereign for the ten percent. (2) **The parts threshold and
the peak year.** Steel decides at 59.5% only because of 2021; on 2022 to 2025 mining earned more in four years of five. Q7
has a cycle rule for an aberrational window year; Q2's business-of-parts threshold has none, and a single peak year chose
the deciding part. I applied the literal five-year rule and wrote the dependence down. (3) **Equity-method income inside
segment results.** The steel segment's operating result includes its share of the mining subsidiary, removed only in the
eliminations; the threshold text does not say whether the parts are measured before or after that line. I measured
without it and showed the as-reported shares beside; steel decides either way. (4) **Rivals not named.** The brief asks for
the rivals the company's own documents name; Usiminas names none ("demais usinas"), so the choice of CSN, Gerdau and
ArcelorMittal is mine, and two of the three report segments of a different shape (ArcelorMittal's Brazil segment includes
Argentina and is in US$; Gerdau's Brazil operation is mostly long steel). (5) **The ADR's class.** The F-6 filings name two
facilities and no ticker; the class was inferred from price parity, which an unattended run cannot always do. (6) **Zero
nominal growth after year ten** against a nominal 12.57% rate in a currency with inflation of several percent a year
undervalues every BRL business against a USD one; the PG specific was written for USD.
