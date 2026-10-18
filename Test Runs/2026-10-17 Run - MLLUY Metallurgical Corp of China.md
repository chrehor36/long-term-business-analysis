# Company Run — Metallurgical Corporation of China Ltd. (HKEX: 1618 H / SSE: 601618 A / OTC ADR: MLLUY) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (2609e46c): not held; `PORTFOLIO.md` has no line for MLLUY, Metallurgical, MCC or 1618.*

**Dispatched run, two departures from the canonical brief stated by the brief itself:** (1) the name has no SEC financial
filings (CIK 0001485888 carries ADR registration forms only), so the primary documents are the company's own reports on
HKEXnews, recorded by document, date and HKEX file reference in place of an accession number; (2) the lines of evidence
were derived by the analyst from the annual report's business section, risk section and management discussion (listed
below), not supplied by the dispatcher.

**Contamination, declared:** the session opened with a git status and five recent commit subjects that I did not seek: the
subjects name another company (MAGH) and one of them reads "OUT at Q2"; the status lists research folders for two other
companies (AYI, ARCB). The memory index loaded with the session carries one-line summaries of the queue state ("57
gate-clearers, nothing buyable") that name no company. None of it concerns this company under any name, and none of it
was used. No `Test Runs/` file other than the template and this run's own files was opened, listed or searched;
`PORTFOLIO.md`, the register, the reading list and the resume-state files were not opened.

**Lines of evidence, chosen from the annual report (2025 Annual Report, Section IV, "Report of Board of Directors,
Management Discussion and Analysis"):** (1) the business and its segments (engineering contracting, featured business,
the discontinued real-estate and resources businesses); (2) the industry situation as the company states it
(construction output, housing starts, steel output); (3) the risk section, "(IV) Possible risks and response measures",
whose second risk is market competition: "The construction industry has entered a period of adjustment, shifting from a
supply model based on homogeneous scale to one centered on differentiated capabilities"; (4) the contract, receivable and
payable cycle (the key audit matters are revenue recognised over time and expected credit losses on receivables and
contract assets); (5) the December 2025 disposal of the real-estate and resources businesses to the controlling
shareholder and the impairments that preceded it; (6) the capital structure (perpetual bonds, minority interests) and
the distribution record; (7) the 2026 plan ("operating revenue of over RMB400 billion").

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** H share **HK$1.315** (close 2026-10-16; Yahoo Finance chart service, an aggregator, flagged per operator
  rule 5). A share RMB 2.58 (same date, same source). The ADR MLLUY shows a last quote of US$3.21 with zero volume on
  every day of the month fetched; it is stale and not used. **The ADR ratio is 20 H shares per ADR**, from the F-6EF of
  2019-11-22 (accession 0001193805-19-001645: "each American Depositary Share representing twenty ordinary shares"),
  the same ratio as the F-6 filings of 2010 (0001019155-10-000064), 2012 (0001193805-12-000657), 2013
  (0001193805-13-001183) and 2016 (0001193805-16-002333); the ADR programmes are unsponsored registrations by
  depositaries. **Price used: the H share**, which the ADR represents: 20 x HK$1.315 = HK$26.30 = **US$3.35 per ADR** at
  HK$7.8477 per US$ (aggregator, 2026-10-16). In renminbi, the earnings currency, the H share is RMB 1.121 at RMB 0.8526
  per HK$. The A share trades at RMB 2.58, about 2.3 times the H share for the same claim.
- **Shares by class:** 20,691,619,170 issued at 30 June 2026, of which A 17,852,619,170 and H 2,839,000,000, after the
  cancellation of 32,000,000 repurchased H shares on 2 June 2026 (2026 Interim Report, HKEX 2026-09-17, file
  2026091700586, Section VII share table and Section IV(II)). The same report states that by its date the company had
  repurchased 181,683,707 A shares and 33,815,000 H shares "(other than the cancelled shares)". **Shares outstanding used:
  20,476,120,463** (A 17,670,935,463; H 2,805,185,000). Checked against issued shares less shares held: the June balance
  sheet shows share capital RMB 20,691,619 thousand and treasury stock RMB 259,442 thousand against the 85,731,626 A
  shares then held. `python Screens/cover_shares.py MLLUY` returns "NOT AN SEC REGISTRANT in the live ticker file"; there
  is no 8-K or prospectus.
- **Market cap:** A shares at RMB 2.58 = RMB 45.59 bn; H shares at HK$1.315 = HK$3.69 bn = RMB 3.15 bn; **total RMB
  48.7 bn** (about US$7.3 bn at RMB 6.677 per US$, aggregator). Valued at the H price for every share: RMB 23.0 bn
  (US$3.4 bn). The run reports per-share figures in renminbi and per ADR, against the H price.
- **Sovereign for the earnings currency:** **2.06%**, the 30-year yield on the China Government Bond Yield Curve
  (财政部-中国国债收益率曲线) for 2026-10-16, published by the Ministry of Finance of the PRC (the page's sponsor line reads
  主办单位：中华人民共和国财政部), served on yield.chinabond.com.cn (China Central Depository & Clearing, the curve's
  compiler), fetched 2026-10-17 (`Test Runs/_research 2026-10-17 MLLUY/sovereign_2026-10-16.txt`). **CONVENTION of this
  run:** the protocol's table names no renminbi source; I take the Ministry of Finance's own published curve as the
  issuing authority and the 30-year tenor to match the protocol's USD choice. Rationale: the Ministry issues the bonds and
  publishes the curve; the 30-year is the longest point on it.
- **Filings read** (operator rule 4), all from HKEXnews, stock code 1618: the **2025 Annual Report** (HKEX 2026-04-17,
  file 2026041700852; audited by Deloitte Touche Tohmatsu Certified Public Accountants LLP, "standard unqualified"
  opinion dated 30 March 2026); the **2026 Interim Report** (HKEX 2026-09-17, file 2026091700586, unaudited); the annual
  reports for 2016 to 2024 (files ltn20170405825, ltn20180410611, ltn20190411572, 2020041501297, 2021041500339,
  2022042600744, 2023042000523, 2024041800666, 2025042200817); the **circular on the very substantial disposal and
  connected transaction** (HKEX 2025-12-12, file 2025121201700); the **announcement on the estimated 2025 annual results**
  (HKEX 2026-01-23, file 2026012301104) and the inside-information advance announcement (2026-01-16, file
  2026011601729); the 2025 third quarterly report (2025-10-30) and the A-share repurchase circular (2025-12-24) were
  downloaded and scanned only. **Standards:** the H-share report presents the statements prepared under the PRC
  Accounting Standards for Business Enterprises (ASBE) to all holders; the basis note says that "from fiscal year 2014,
  the Company no longer provides the financial statements prepared in accordance with the ASBEs and International
  Financial Reporting Standards ("IFRSs") separately to stockholders of A shares and H shares", so the A and H reports
  carry one set of statements, and the report says no IFRS difference applies. The English text is a translation; the
  auditor's report says the Chinese version prevails.
- **One figure cross-checked against the filed statement:** 2025 net cash flow from operating activities, RMB
  15,322,753 thousand, in the major-accounting-data table (Section III, VII(I), printed p.12) and in the consolidated
  cash flow statement (printed p.174): the same.
- `python tools/run.py MLLUY` prints "MLLUY: not an SEC filer. Use the evidence ladder [...] This is UNRESEARCHED, not
  UNKNOWABLE." and no arithmetic. The arithmetic was done from the filed statements in scripts in the research folder
  (`scripts/parse_statements.py`, `scripts/bs_table.py`, `scripts/field_returns.py`, `scripts/q7_computation.py`),
  every input typed or parsed from the filed statement pages. **Owner cash after every real cost by year** (RMB bn,
  operating cash flow less all spending on fixed and intangible assets less net cash paid for businesses; under ASBE
  interest paid sits in financing, so this is before interest paid): 2021 14.18, 2022 13.49, 2023 1.31, 2024 0.98,
  2025 9.05; **five-year average 7.80**. Capital spending 2021 to 2025: 3.55, 4.31, 4.60, 6.86, 6.28; depreciation and
  amortisation (segment notes): 3.55, 3.93, 4.07, 4.49, 4.79. Stock pay: the 2025 report marks the share-based-payment
  disclosure "Not applicable" (Section III, XI); no stock pay to resolve.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, bought for what the business produces, and the test
is whether one would be content "if the market closed for five years" **[M1997-109]**. Here the owner of an A or H share
owns a residual claim behind RMB 54.1 bn of perpetual bonds and RMB 28.2 bn of minority interests, in a group whose
controlling shareholder (China Minmetals, through CMGC) decided in December 2025 to take the real-estate and resources
businesses into its own hands; what the share is a claim on has to be read from the filings, not from the quotation. The
second bears too: the market quotes the same claim at RMB 2.58 in Shanghai and RMB 1.12 in Hong Kong on the same day, which
"just tells us prices" **[M2006-077]**. No macro forecast enters **[M2000-094]**: the 2025 report's own figures (national
construction output down 1.13%, new housing starts down 20.4%) are read only as evidence of the business's economics. The
speakers bought a Chinese state-controlled company and named the state's ownership as a factor "you stick in valuation"
**[M2004-082]**, and wanted "to get paid more for going into China" **[M2006-021]**. **Contrary evidence, written down
as found** **[M1997-127]**: (1) the 2025 accounts carry RMB 19.4 bn of asset impairments and RMB 8.2 bn of credit
impairments, and ordinary shareholders' share of 2025 profit was RMB 46 million after RMB 1,275 million to perpetual-bond
holders (EPS note); (2) receivables, contract assets and long-term receivables reached RMB 499 bn against revenue of RMB 455
bn at end-2025, from about half of revenue in 2019 to 2022; (3) accounts receivable aged over one year rose to RMB 121.7
bn gross of RMB 273.9 bn, the one-to-two-year bucket from RMB 39.5 bn to RMB 66.8 bn in a year; (4) the parent company's
own accounts show accumulated losses of RMB 2,785 million, so no dividend could be paid for 2025; (5) the field (two
rivals' own reports) earns pre-tax margins near 3% and MCC earns less.

## THE STANDING RULE
Owning a part-interest in this company, bought for cash without borrowing and sized so that its loss would not touch what
the buyer needs, puts the buyer at no risk of ruin; the rule binds the buyer's financing and sizing, "never going to
risk what we have and need for what we don't have and don't need" **[M2012-081]**, **[L2023-005]**, and borrowed money
"has no place in the investor's tool kit" **[L2014-005]**. Nothing in the target changes that; the target's own debt and
perpetual claims are weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** After December 2025 the company is an engineering contractor with a small
  "featured business" beside it. The 2025 segment note (2025 Annual Report, Note XVI.1, printed pp.365-366) reports
  operating income of RMB 407,982 million in engineering contracting, RMB 32,735 million in the featured business and
  RMB 20,619 million in the discontinued operations; the report describes engineering contracting as "metallurgical
  construction business, housing construction and municipal infrastructure engineering business", "mainly carried out by
  way of EPC contract and general financing and construction contracting contract, and is currently the major source of
  income and profits of the Company" (Section IV, printed p.37). The real-estate company and the resources companies
  (Non-ferrous Engineering, MCC Tongsin Resources, MCC Ramu, MCC Duddar, 67.02% of MCC-JJJ Mining) were sold to China
  Minmetals and its designated entity, approved by the extraordinary general meeting of 29 December 2025 (circular of
  2025-12-12; Section IV, printed p.20).
- **The key variables and how predictable they are** **[M1998-044]**: (1) the volume of work won: new contracts RMB
  1,112.9 bn in 2025, down 10.87%, and orders in hand of RMB 2,731.4 bn, of which RMB 1,125.7 bn "signed yet to be
  commenced" (Section IV, operational information, printed p.50); (2) the margin at which it is won: engineering
  contracting gross margin 12.54% (2015), 11.05% (2016), 11.15% (2017), 10.52% (2018), 10.14% (2019), 10.17% (2020),
  9.19% (2021), 8.96% (2022; 8.84% restated), 9.09% (2023), 9.24% (2024; 9.21% restated), 9.54% (2025), each from that
  year's report; (3) the conversion of profit into cash, which runs through receivables from project owners and payables
  to subcontractors (Step 0 and the balance sheets below). The first depends on state and industrial investment and is
  not forecast here **[M2000-094]**. The second and third are the economics, and ten filed years show their kind: a thin
  margin on a large volume, with the cash tied up in the receivable and payable cycle. That is "a reasonable fix on about
  what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**: the earning power
  is a thin contractor's margin and the position is one large contractor among several, which Q2 tests against the
  rivals' own reports.
- **Is the product or the economics the question?** The chemistry of a blast furnace need not be understood; "What is
  important is that I understand the economic dynamics of the industry. Is there — are there competitive moats? Is there
  ease of entry?" **[M2011-014]**. The dynamics are legible in the company's own words: "industry competition has evolved
  from "opportunity-driven competition" to "capability-driven competition," placing higher demands on construction
  companies" (risk section, printed p.61), and "We
  competed fiercely in the public bidding market" (Chairman's Statement, printed p.7).
- **Do the past statements tell me the future ones?** **[M2008-033]** For the contracting business, yes in kind: margin,
  receivable build and cash conversion repeat across 2016 to 2025. For the real-estate business they did not: the
  circular shows MCC Real Estate's net assets attributable to the parent falling from about RMB 6,041 million at 30 June
  2025 to net liabilities of about RMB 17,443 million at 31 July 2025 after the appraisal (circular, Letter from the
  Board, printed pp.21-22). That business is gone; the question of what the remaining receivable book is worth is a
  question of the accounts (Q4) and of exposure (Q9), recorded below, and does not make the contracting economics
  unforeseeable.
- **Abroad: governance and tax** **[M2000-141]**. The company is controlled by China Minmetals through CMGC, under SASAC;
  transactions with the controller are put to independent shareholders (the disposal was a "very substantial disposal and
  connected transaction"); the income tax is the PRC enterprise income tax, with 15% preferential rates for named
  high-technology subsidiaries (2026 Interim Report, Taxation note). The speakers' answer for a state-controlled Chinese
  company was a price, not a pass: the government's ownership is "obviously a factor that what — you stick in valuation"
  **[M2004-082]**, and "We wanted to get paid more for going into China, and we did, because we don't know the game as
  well there" **[M2006-021]**.
- **Routing.** Not a business of fast-moving technology; not a bank or a derivatives book. Under the framework's commodity paragraph
  (Q2) a commodity-like business is not stopped at Q1 for that alone; the test is the figures, "if you can't make a
  decision on something like PetroChina off the figures, forget about going further" **[M2008-069]**, and here the
  figures decide it.
- **Do I doubt it is inside?** **[M2002-092]** The doubt I carry is about the value of RMB 499 bn of receivables and contract
  assets, which is a question about the accounts and the exposures, not about what kind of business this is; it is
  carried to the AFTER THE STOP section if the file closes earlier.
- **VERDICT: IN.** The economics of a large Chinese engineering contractor can be foreseen in kind from ten years of its own
  filings: a thin and slowly narrowing margin on state-driven volume, with profit converted to cash through a long
  receivable cycle **[M2012-065]**, **[M2011-014]**, **[M2008-069]**; the state ownership is a matter for the price
  **[M2004-082]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (section B; total profit, RMB bn, from the segment note of the year's own report; the segment cuts
changed in 2023 and again in 2025, and each year is taken as its report filed it, 2024 as restated in the 2025 report):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Engineering contracting | 11.61 | 14.11 | 13.68 | 10.38 | 8.69 | 58.47 | about 102% | tested below | **yes** (more than half) |
| Featured business (equipment, materials, services; "equipment manufacture" before 2023) | 0.32 | -0.22 | 1.78 | 1.89 | 2.10 | 5.87 | about 10% | not tested | no |
| Property development / real estate (sold Dec 2025) | 0.01 | 0.44 | -2.47 | in discontinued | in discontinued | | | gone | no |
| Resources (sold Dec 2025, except what the featured line keeps) | 1.85 | 1.47 | 1.52 | in discontinued | in discontinued | | | gone | no |
| Discontinued operations (2024, 2025) | | | | -2.70 | -4.85 | | | gone | no |
| Company total profit | 14.01 | 15.39 | 13.76 | 9.25 | 5.01 | 57.43 | 100% | | |

Sources: 2021 Annual Report Note XV.1 (printed p.363); 2022 Annual Report Note XV.1 (printed p.369); 2023 Annual Report
Note XVI.1 (printed p.383); 2025 Annual Report Note XVI.1 (printed p.366). Engineering contracting carries more than all of
the five-year total profit, so it decides **[L2008-005]**; the file closes on its castle.

**The castle tests, each with its filing fact.**
1. **The attacker with money; is there ease of entry?** **[M2011-015]**, **[M2011-014]**. The company's own risk section:
   "The construction industry has entered a period of adjustment, shifting from a supply model based on homogeneous scale
   to one centered on differentiated capabilities" (printed p.61). "Homogeneous scale" is the company's description of
   the field it has been in. Its rivals include at least two state contractors each more than twice its size (below). No
   barrier that money could not cross is named in the filing; the advantages the report claims are its "technical and
   qualification advantages" (printed p.31) and "core advantages in industrial technology, full industrial chain and
   general engineering contracting fields" (printed p.20), which its rivals claim in kind. "there
   are some industries that are just never going to have barriers to entry" **[M2012-106]**.
2. **Pricing power; the agony before a rise** **[M2005-020]**. The engineering contracting gross margin fell from 12.54%
   (2015) to 8.96% (2022) and stood at 9.54% in 2025 (each year's report, Q1 above): over a decade in which revenue rose
   from RMB 219.6 bn to RMB 633.9 bn (2023), the price earned on the work fell. The report names no price it has been able
   to raise.
3. **Would the customer still choose it over the low bid?** **[M2017-009]**. The work is won by tender: "We competed
   fiercely in the public bidding market" (Chairman's Statement, printed p.7); the customers are project owners
   (governments, state enterprises, steelmakers) buying a standard service from many qualified bidders, which is the
   commodity mark the rows define, "most insureds don't care from whom they buy" **[L2004-003]**.
4. **The low-cost position** **[M1997-010]**, **[M2001-013]**, read from MCC's and two rivals' own reports (the competitor row
   below): MCC's pre-tax margin was below both rivals in every year from 2019 to 2025 and over the span (2.53% against
   3.48% and 3.19%). In a field where the price is set by the bid, MCC is not the low-cost producer; it is the
   higher-cost one. A commodity business is judged at Q2 "more by cost of production" **[M2006-004]**, and "The figures are
   available." **[M2009-059]**.
5. **The brand in the customer's mind; unit volume.** No brand by which a project owner asks for MCC instead of a rival is
   shown in the filing; volume is falling: new contracts down 10.87% in 2025, revenue down 17.51% (Section III,
   printed p.13), and the company plans "operating revenue of over RMB400 billion" for 2026 (printed p.60).
6. **Widening or narrowing** **[M1999-108]**. Narrowing on every filed measure: the gross margin above; the pre-tax margin
   from 3.48% (2016) to 1.10% (2025); and the receivable cycle, which lengthened from about half of revenue (2019 to 2022)
   to 110% of revenue at end-2025 (balance sheets, AFTER THE STOP, Q4). The newspapers "lost still another notch"
   **[L1995-023]**; this field has lost one in each of the last three years. The company's own record of the change:
   "resolutely abandon the extensive development model of scale expansion" (2026 plan, printed p.59).
7. **What could destroy, modify or reduce it** **[M2000-014]**, from the filing's figures and not as a forecast: national construction
   output fell 1.13% in 2025 and new housing starts fell 20.4% (Section IV, industry situation, printed p.28); crude steel
   output, the core metallurgical customer, fell 4.4%.
8. **Ask the competitors.** No competitor is named in the annual report (searched: "competitor", "competition", "China
   State Construction", "China Railway", "China Communications", "PowerChina", "market share" in the 2025, 2024, 2023,
   2020 and 2017 reports; no instance found of a named rival). Two rivals were chosen by me (a departure, stated): China
   Railway Group (HKEX 0390) and China Railway Construction (HKEX 1186), the two largest Hong Kong-listed state
   contractors with HKEX annual reports for the whole span. Neither files periodic reports with the SEC: CRCC's EDGAR
   record (CIK 0001436965) holds a 12g3-2(b) exemption, F-6 and SUPPL forms; China Railway Group's (CIK 0001447959) F-6
   forms only. China Communications Construction (HKEX 1800) was not read (gap, recorded).

**The competitor row and the field's returns over the last full cycle** (section C; `scripts/field_returns.py`; pre-tax
profit over revenue / pre-tax profit over year-end total equity, where total equity includes minority interests and
perpetual instruments for all three; RMB figures from each company's own report):

| year | MCC (1618) | CREC (0390) | CRCC (1186) |
|---|---|---|---|
| 2015 | 3.29% / 10.04% | 2.84% / 12.22% | 2.85% / 13.28% |
| 2016 | 3.48% / 9.20% | 2.97% / 12.60% | 3.01% / 12.76% |
| 2017 | 3.68% / 9.22% | 3.02% / 12.28% | 3.12% / 11.90% |
| 2018 | 3.29% / 9.28% | 3.37% / 11.24% | 3.44% / 12.11% |
| 2019 | 2.89% / 8.37% | 3.90% / 13.53% | 3.37% / 10.70% |
| 2020 | 2.98% / 8.49% | not read | not read |
| 2021 | 2.80% / 9.26% | 3.69% / 11.07% | 3.45% / 10.15% |
| 2022 | 2.60% / 9.51% | 3.87% / 10.57% | 3.45% / 9.80% |
| 2023 | 2.17% / 8.19% | 3.77% / 10.35% | 3.41% / 9.31% |
| 2024 | 1.68% / 5.08% | 3.50% / 7.96% | 3.04% / 7.68% |
| 2025 | 1.10% / 2.73% | 3.15% / 6.37% | 2.62% / 6.31% |
| span aggregate margin / mean return | 2.53% / 8.12% | 3.48% / 10.82% | 3.19% / 10.40% |

Sources: MCC, consolidated income statements and balance sheets of the 2016 to 2025 annual reports; CREC, Financial
Summary of the 2025 Annual Report (HKEX 2026-04-23, file 2026042300346, printed pp.4-5) and of the 2019 Annual Report
(HKEX 2020-04-16, file 2020041600391, printed pp.2-3); CRCC, Five Years' Financial Summary of the 2025 Annual Report (HKEX
2026-04-15, file 2026041501202) and of the 2019 Annual Report (HKEX 2020-04-22, file 2020042200769). MCC's own weighted
average return on net assets attributable to ordinary shareholders, as the company reports it: 9.46% (2015), 9.30%
(2016), 8.44% (2017), 8.25% (2018), 7.99% (2019), 8.93% (2020), 9.05% (2021), 10.47% (2022), 7.23% (2023), 4.87%
(2024), 0.05% (2025) (major-financial-indicators tables of the 2016, 2019, 2022 and 2025 reports).

**Judged in words, as the convention asks** **[M1999-108]**. Over eleven years that include the build-up to the 2023 peak
and two years of decline, the field's durable players earned three to four yuan of pre-tax profit per hundred of
revenue, and about a tenth before tax on an equity base swollen by minority and perpetual capital, falling to six
percent in 2025. That is a standing castle protecting ordinary returns at best: the rivals stand, but nothing in their
returns or MCC's shows the "excellent returns on invested capital" a moat is defined as protecting **[L2007-004]**; "you
can have only two competitors and they're still terrible businesses" **[M2013-052]**, and here there are many. The
return is not set by a regulator (the exception carried to Q3 does not apply). And within that field MCC is the
higher-cost operator, below both rivals on margin and on return in every year since 2019 **[M1997-010]**, **[L1994-035]**.
Not a change for the better awaiting a full cycle: every measure has moved the wrong way.

**Contrary evidence for the castle, written down** **[M1997-127]**: the company claims technical leadership in
metallurgical construction ("the core function of national team of metallurgical construction", 2024 report, printed p.16) and its metallurgy,
non-ferrous and mining contracts grew 12.3% in 2025 (printed p.20); the featured business earns a 15.6% gross margin.
Neither changes the deciding part's economics: metallurgical construction is a part of engineering contracting, whose
margin is the one tabled, and the featured business carried about a tenth of five-year profit.

- **VERDICT: OUT.** The deciding part, engineering contracting, sells a commodity service won by public tender
**[L2004-003]**, **[M2017-009]**, in a field whose durable players earn only ordinary returns over the last full cycle on
their own filings (CONVENTION of section C: judged in words), and MCC is the higher-cost producer in it, below both rivals
read in every year since 2019: "commodity businesses have risk unless you're the low-cost producer" **[M1997-010]**;
"a company must lower its costs to competitive levels or face extinction" **[L1994-035]**. A castle shown open on the
evidence closes OUT, not TOO HARD **[M2011-015]**, **[M2006-013]**. Price does not reopen it **[M2019-015]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0's place (the brief asks for them where the file closes before Q4);
they are set out under AFTER THE STOP, Q4.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question; the reporting figures are computed under the heading COMPUTATION NOT A CLEARANCE below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT, at Q2**: the deciding part (engineering contracting) is a commodity service won on the bid in a field of ordinary
returns, and MCC is the higher-cost producer in it on its own and two rivals' filings. Integrity facts recorded, not
judged (the related-party disposal of December 2025; see AFTER THE STOP, Q5 and Q6).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q2 closed the file. Facts already found that bear on later questions, each with its source, written down and not
weighed **[M1997-127]**; no verdict; the box unchanged, operator rule 2.)*

**Q3 (capital).** Total assets RMB 377.5 bn (2016) to RMB 839.5 bn (2025) while revenue went from RMB 219.6 bn to a peak of
RMB 633.9 bn (2023) and back to RMB 455.4 bn. The growth was financed by perpetual bonds (RMB 9.9 bn to RMB 54.1 bn; RMB
29.8 bn issued in 2025 and RMB 18.4 bn in 2024, cash flow statements), by outside equity in subsidiaries (capital
contributions from minority shareholders of subsidiaries RMB 24.0 bn in 2020, RMB 9.7 bn in 2024, RMB 4.1 bn in 2025) and
by trade credit (accounts and notes payable RMB 129.6 bn to RMB 422.2 bn). Engineering contracting net profit over
segment net assets (segment assets less segment liabilities, segment notes): about 8.1% (2019), 11.0% (2021), 10.2%
(2023), 4.3% (2025). Capital spending exceeded depreciation and amortisation in 2024 (RMB 6.86 bn against 4.49 bn) and
2025 (6.28 against 4.79). Net cash paid for investments, largely equity stakes in project companies (long-term equity
investments RMB 30.3 bn in 2021 to RMB 40.7 bn in 2025), averaged RMB 3.6 bn a year over 2021 to 2025.

**Q4 (the accounts), the balance sheets first, ten of them** (consolidated balance sheets of each year's report, RMB bn;
`scripts/bs_table.py`; in 2016 and 2017 construction work in progress sat in inventories, before the contract-asset
standard, so the receivable column understates those two years):

| year | revenue | receivables + contract assets + long-term receivables | % of revenue | accounts + notes payable | % of revenue | borrowings | cash | perpetual bonds | minority interests | ordinary book |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 219.6 | 96.8 | 44% | 129.6 | 59% | 95.8 | 44.9 | 9.9 | 12.6 | 60.7 |
| 2017 | 244.0 | 117.8 | 48% | 139.8 | 57% | 88.4 | 43.6 | 17.9 | 14.8 | 64.6 |
| 2018 | 289.5 | 175.7 | 61% | 141.0 | 49% | 94.8 | 44.5 | 15.9 | 18.7 | 68.0 |
| 2019 | 338.6 | 171.0 | 51% | 147.4 | 44% | 85.1 | 43.7 | 25.9 | 19.0 | 72.0 |
| 2020 | 400.1 | 184.8 | 46% | 164.2 | 41% | 67.9 | 53.1 | 20.5 | 42.5 | 77.4 |
| 2021 | 500.6 | 208.9 | 42% | 192.9 | 39% | 60.1 | 41.8 | 23.7 | 43.9 | 83.8 |
| 2022 | 592.7 | 241.1 | 41% | 224.4 | 38% | 62.3 | 45.5 | 28.5 | 40.8 | 92.6 |
| 2023 | 633.9 | 308.2 | 49% | 272.1 | 43% | 73.7 | 44.4 | 47.4 | 22.5 | 98.1 |
| 2024 | 552.0 | 437.6 | 79% | 365.2 | 66% | 93.4 | 52.6 | 50.6 | 29.3 | 102.4 |
| 2025 | 455.4 | 499.1 | 110% | 422.2 | 93% | 80.0 | 77.8 | 54.1 | 27.8 | 101.7 |

(Borrowings: short-term, long-term, bonds and non-current liabilities due within one year; ordinary book: equity
attributable to shareholders less perpetual bonds.) What moved, read as the row asks, "what the figures are saying and
what they don’t say and what they can’t say" **[M2025-032]**: receivables and contract assets doubled against revenue in
two years, from 49% (2023) to 110% (2025), while payables rose from 43% to 93% of revenue; the company is being paid more
slowly by project owners and is paying its subcontractors and suppliers more slowly in turn. Accounts receivable aged over
one year rose to RMB 121.7 bn of RMB 273.9 bn gross, the one-to-two-year bucket from RMB 39.5 bn to RMB 66.8 bn in a year;
the allowance is RMB 30.5 bn (2025 Annual Report, Note VII.3, ageing table). Ordinary book grew from RMB 60.7 bn to RMB
101.7 bn in nine years and did not grow in 2024 or 2025. Retained profits RMB 16.2 bn to RMB 51.3 bn, falling in 2025;
goodwill negligible (RMB 47 million); intangible assets RMB 26.6 bn. Cash at end-2025 is a year-end high: operating cash
flow by quarter in 2025 was RMB -25.7 bn, +3.7 bn, +2.6 bn and +34.7 bn (Section III, IX), and cash and bank balances fell
to RMB 68.1 bn by 30 June 2026. Other facts for Q4: the auditor's key audit matters are "Engineering contracting business
– Revenue recognised over time" and "Expected credit losses on accounts receivable and contract assets"; losses from
derecognition of financial assets at amortised cost (sales of receivables) were RMB 1,061 million in 2025 and RMB 1,089
million in 2024 (income statement); the report gives the CSRC's mandatory "net profit attributable to Shareholders of the
listed Company after deducting non-recurring profits and losses" (RMB 450 million in 2025) beside the reported figure, a
required disclosure; the 2025 non-recurring items include "Impacts related to the asset disposal" of RMB -1,461 million and
the reversal of a 2007 housing-subsidy provision of RMB 461 million (Section III, X). No EBITDA figure was found featured.

**Q5 (the people).** The chairman who signed the 2025 report (Chen Jianguang) is not the legal representative who signed
the 2026 interim statements (Li Zhongze); the HKEX list shows a 2026 third extraordinary general meeting on 13 August 2026
for the "appointment of directors, appointment of chairman" (title only, not opened). No sweep was made for regulatory
penalties or litigation. The December 2025 disposal is a connected transaction with the controlling shareholder (Q6
below). **Integrity facts recorded, not judged.**

**Q6 (the money and the owners).** The disposal (circular of 2025-12-12): MCC Real Estate's entire equity and the debts it
owed MCC sold to Minmetals Land Holdings for RMB 31,236.6 million, after an appraisal under which "the appraised value of
the Company's equity interest in MCC Real Estate depreciated by approximately RMB25.7 billion compared to its book value";
the resources companies sold to China Minmetals for RMB 29,439.7 million (Non-ferrous Engineering 10,495.6; MCC Tongsin
Resources 12,240.7; MCC-JJJ Mining 67.02%, 5,035.8; MCC Duddar 1,656.7; MCC Ramu 10.9); RMB 60,676 million in cash in
total, half within twenty days of the board resolution and half on completion; the pro forma loss as if completed on 30
June 2025 was about RMB 2,519 million (circular, printed pp.2-3, 7-8, 21-22, 28). Dividends: RMB 0.072 a share for 2023
and RMB 0.056 a share for 2024 (RMB 1,160.52 million, 17.20% of 2024 profit attributable); none for 2025, because the
parent company's own statements show accumulated losses of RMB 2,785.15 million (2025 report, Important Notice V and
VI). Buybacks in 2026 to 30 June: 85,731,626 A shares at RMB 2.78 to 3.25 (RMB 259.4 million) and 32,000,000 H shares at
HK$1.49 to 1.94 (HK$55.5 million, cancelled); RMB 600 million in total by the report's date. The A-share plan (circular
of 2025-12-24, file 2025122402212, printed p.3) is for RMB 1 to 2 billion at a "maximum repurchase price of A Shares
[that] shall not exceed 150% of the average trading price of the A Shares for the 30 trading days prior to" the board
resolution, "being RMB4.90 per Share": a cap set from the market price, not from a stated value. **The buyback line Q6 needs from Q7** (computed below, not a clearance): the bottom of the
central range is RMB 1.84 a share; the H shares were bought at RMB 1.27 to 1.65 (below it) and the A shares at RMB 2.78 to
3.25 (above it), the same claim bought at about twice the price in Shanghai as in Hong Kong. Perpetual-bond holders
received RMB 1,275 million of 2025 profit and ordinary holders RMB 46 million (EPS note). Share capital stood at RMB
20,723,619 thousand from 2016 to 2025: no ordinary shares issued in the span.

**Q9 (debt and exposures).** At 30 June 2026 the company's own net debt was RMB 20,812 million (borrowings RMB 80,008
million less cash and cash equivalents RMB 59,196 million; gearing note), against RMB 10,530 million at 31 December 2025;
perpetual bonds RMB 54,100 million, carried in equity; accounts and notes payable RMB 402.7 bn; guarantees (including to
subsidiaries) RMB 15.1 bn, 9% of net assets (2025 report, guarantees table). Overseas revenue RMB 31.5 bn (6.9%);
overseas non-current assets fell from RMB 12.1 bn to RMB 3.6 bn with the resources sale.

## COMPUTATION NOT A CLEARANCE: Q7 AS IT WOULD BE BUILT, AND THE TWO REPORTING FIGURES
*(The file closed at Q2. Nothing here is a clearance, a verdict or entry language (operator rule 3).
`scripts/q7_computation.py`, output in `q7_output.txt`.)*

- **Owner cash, central, all-equity basis** (before interest, after the company's own tax): operating cash flow (under
  ASBE interest paid is a financing flow) less all capital spending less net cash paid for businesses, 2021 to 2025: RMB
  14.18, 13.49, 1.31, 0.98, 9.05 bn; **five-year average RMB 7.80 bn**. Working capital is inside operating cash flow
  (specific d). The December 2025 sale of subsidiaries (net cash received RMB 28.5 bn) is left out of owner cash because
  the cash already sits in the net debt of 30 June 2026 (CONVENTION of this run; rationale: counting it in both would
  count it twice). Acquisitions were negligible (specific c). The filing gives no maintenance split (specific e); the
  depreciation variant is beside, average RMB 8.76 bn.
- **Growth shown:** -10.6% a year between the end years of the window (14.18 to 9.05; the series does not change sign).
  Beside, the decade: owner cash averaged RMB 15.20 bn in 2016 to 2020 and RMB 7.85 bn in 2021 to 2025, -12.4% a year
  between the half-averages. The decline is carried as the bottom of the range and the no-growth case is the top
  (specific b). No end year is described by the filer as aberrational in cash (specific a); the ten-year base is shown
  beside. The cap (specific f) does not bind a decline.
- **Bridge from the whole business to the ordinary shares** (CONVENTION of this run): net debt RMB 20.8 bn (the company's
  own, 30 June 2026), plus the perpetual bonds of RMB 54.1 bn, counted as a claim ahead of the ordinary shares because
  their coupons are paid before ordinary profit (RMB 1.28 to 1.86 bn a year), plus minority interests at book, RMB 28.2 bn,
  because minorities took RMB 1.2 bn of 2025's RMB 2.5 bn net profit; claims RMB 103.1 bn. Rationale: the all-equity basis
  values the business before any claim, "we evaluate acquisitions on an all-equity basis" **[L2017-004]**, and these
  claims are paid before the ordinary holder. Subsequent events: the repurchased shares are out of the count (Step 0).
- **Sovereign:** 2.06% (Step 0). Ten years at the case's growth, then zero nominal growth.
- **VALUE RANGE (central): RMB 1.84 to RMB 13.46 a share** (decline case to no-growth case), **US$5.50 to US$40.23 an
  ADR** (20 H shares), against the H price of RMB 1.121 (HK$1.315; US$3.35 an ADR) and the A price of RMB 2.58. Width 7.3
  to 1. The width comes from the 2.06% rate: the no-growth whole business is worth RMB 378.7 bn at that rate and RMB 78.0
  bn at ten percent.
- **The floor, tested first:** the expected return at the price on the better (no-growth) case is 6.2% with every share
  at the H price (owner cash RMB 7.80 bn against RMB 126.1 bn of market value plus claims) and 5.1% at the A and H market
  prices (RMB 151.8 bn); the decline case is lower. **No case earns the floor of about ten percent at the price**, "there’s
  just a point at which we drop out of the game" **[M2003-149]**: Q7, had it been reached, would close OUT before the width
  is tested. Without the perpetual and minority claims (net debt only), the no-growth return at the H price would be
  17.8%; the bridge convention decides this figure, and it is stated so the operator can see it.
- **FAIR PRICE (central, all-equity; Part VII: each end case valued at ten percent, the two averaged): none positive.**
  The no-growth case at ten percent is RMB 78.0 bn and the decline case RMB 39.3 bn, both below the RMB 103.1 bn of claims
  ahead of the ordinary shares: RMB -1.23 and RMB -3.11 a share, average **RMB -2.17 a share** (HK$-2.55; US$-6.49 an
  ADR). **Equity-only figure beside** (owner cash after interest expense, perpetual coupons and dividends paid to minority
  holders, a CONVENTION of this run in its extension to the last two: 2021 to 2025 RMB 9.02, 8.21, -4.35, -4.73, 2.33 bn,
  average 2.10 bn; the series changes sign, so the no-growth case alone, specific b): **RMB 1.02 a share = HK$1.20 an H
  share = US$3.06 an ADR**, against HK$1.315; it never decides alone. Tax: owner cash is after the company's own income
  tax (cash paid, inside operating cash flow); no expiring carryforward shelter was identified.
- **Variants beside, none central:** deducting net cash into project-company stakes as well (average RMB 4.18 bn) lowers
  every figure; the ten-year base (RMB 11.53 bn, no growth) gives RMB 0.59 a share at ten percent on the central bridge.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 4c48ab5e, before the first download); written question by
      question; committed after Step 0 (819f545d), Q1 (3a7cb6bf), Q2 and the box (3b9564ec), and this section.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's. The run
      binds nothing until it is folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident
      (commit subjects and folder names of other companies, memory lines) is declared under contamination and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row
      (`scripts/check_run.py`); every filing fact carries its document, date and HKEX file reference (HKEX filings have no
      accession numbers; the F-6 accessions are given).
- [x] The order was kept; Q2 closed the file; everything after it is under AFTER THE STOP or COMPUTATION NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy; the sovereign from the
      Ministry of Finance's own curve (a CONVENTION of this run for the currency); the quotes are an aggregator's, flagged.
- [x] Contrary evidence written down as found (foundations; Q2's contrary paragraph); facts for later questions under
      AFTER THE STOP, with "integrity facts recorded, not judged" in the box line.
- [x] No point-in-time anchor: not applicable.
- [x] `tools/run.py` printed no arithmetic for this name; nothing it prints was used.
- [x] `python tools/check_framework.py` run before the final commit.
- Honest gaps: China Communications Construction not read; CREC and CRCC 2020 not read; no sweep for penalties or
  litigation; the 2026 interim operating cash flow not used (full years only); the English translation read, not the
  Chinese original; the rivals chosen by me because the report names none.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. **(1) The all-equity bridge says nothing of perpetual bonds or minority interests.** Q7's basis defines net
debt as borrowings and finance leases less cash and securities "as the filing states them". This filer classes RMB 54.1
bn of perpetual bonds in equity and carries RMB 28.2 bn of minority interests; left out, the no-growth return at the H
price is 17.8% and the fair price is positive; counted as claims, the return is 6.2% and no positive fair price exists.
The run counted both as claims, as a CONVENTION of this run; the framework should say which, since for Chinese state
contractors these two lines are larger than the net debt. **(2) Which share price?** The same claim trades at RMB 2.58
(A) and RMB 1.12 (H); the template asks for one price and one market cap. The run reported per-share figures against the H
price (the ADR's underlying) and showed the market value both ways; the framework has no rule for classes of one claim
quoted at different prices. **(3) The cash from a segment sale.** Specific (c) counts businesses sold as negative
spending; read literally, the RMB 28.5 bn received in December 2025 for the real-estate and resources companies would
raise five-year owner cash by RMB 5.7 bn a year while the same cash also lowers net debt. The run left it out of owner
cash; the text should say that a sale whose cash is already in net debt is not also owner cash. A smaller point: the
protocol's sovereign table has no renminbi row, so the source was chosen by this run.
