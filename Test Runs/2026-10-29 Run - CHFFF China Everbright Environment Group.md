# Company Run: China Everbright Environment Group Limited (HKEX: 00257; OTC: CHFFF), 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (this filer has no
SEC accession numbers; HKEXnews documents are named by title, date and file number in place of an accession, as the brief
directs); a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-29, after the run was committed: not held (no CHFFF, 00257 or Everbright line in `PORTFOLIO.md`).*

**Dispatch and contamination.** Dispatched blind run (operator rule 10). The brief's stated departures: the repository
path (C:\Projects\BRK), the lines of evidence derived by the analyst, and HKEXnews in place of EDGAR. Seen by accident and
not used: the session's starting git context listed the last five commit subjects, which concern another company
(ticker CDTG, sewage treatment systems, closed OUT at Q2); the automatically loaded project map and memory index mention
gate-clearer counts and holdings in general terms, with no ticker of this company. No `Test Runs/` file other than the
template and this file was opened, listed or searched; `PORTFOLIO.md`, holding reviews, `Screens/RESUME STATE*`, the queue
and the reading list were not opened.

**Lines of evidence, chosen by the analyst from the Annual Report 2025** (HKEXnews 2026-04-23, file 2026042301737; the
business review in the Chairman's and CEO's statements and the Management Discussion and Analysis; the Principal Risks and
Uncertainties section, pages 55 to 59; the notes): (1) the shift from building concessions to operating them, and what it
did to the cash; (2) who pays: local governments for waste and waste-water fees, the State Grid and the national
renewable-energy subsidy for power, and how fast they pay (debtors and their ageing, the subsidy receivables sold to a
trust with liquidity support); (3) pricing: fees fixed in concession contracts and raised only with the grantor's approval,
competition for new projects; (4) the service-concession accounting (construction revenue at a cost-plus margin, finance
income accrued on the concession assets); (5) debt, perpetual capital instruments and the refinancing load; (6) issuance
(the 2018 rights issue, the proposed RMB share issue of 2025) and the absence of buybacks and stock pay; (7) connected
transactions with China Everbright Group; (8) management change (the CEO's resignation of 2026-07-17); (9) the new
concession of 2026-10-26. Litigation: no litigation against the group is disclosed (AR2025 and the Interim Report 2026
searched for "litigation", "legal proceeding", "lawsuit", "arbitration" and the contingent-liabilities paragraphs, whose
only item is the Company's guarantees for subsidiaries, HK$247.6m at 30 June 2026); the litigation the filings name runs
the other way: to collect from local governments in arrears the Company is "sending lawyer's letters and initiating
litigation" (Interim Report 2026, Management Discussion and Analysis, accounts receivable).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HK$4.735 for 00257 on the Hong Kong exchange (close 2026-10-28; Yahoo Finance chart API; **aggregator,
  flagged** per operator rule 5; the figure carries a half-tick that the exchange's HK$0.01 spread at this price would not
  print, so it is read as about HK$4.73 to 4.74). CHFFF on the US over-the-counter market: US$0.60 (last trade carried
  through 2026-10-28, same aggregator, flagged; thinly traded).
- **Shares by class:** one class, ordinary shares, 6,142,975,292 in issue, no treasury shares, no options, warrants or
  convertibles outstanding (Monthly Return of Equity Issuer on Movements in Securities for the month ended 30 September
  2026, submitted 2026-10-02, HKEXnews file 2026100202491). Checked against the Annual Report 2025, note 33 (issued and
  fully paid 6,142,975,292 ordinary shares at 31 December 2025 and 2024) and against basic earnings per share
  (HK$3,925,162k / HK63.90 cents = about 6,143m). `python Screens/cover_shares.py CHFFF`: "NOT AN SEC REGISTRANT".
- **Market cap:** HK$29,087m (6,142.975m x HK$4.735).
- **Sovereign for the earnings currency:** **renminbi, 2.05%**, the 30-year point of the China Government Bond yield
  curve of the Ministry of Finance of the PRC (财政部-中国国债收益率曲线, published for the Ministry on
  yield.chinabond.com.cn, key-tenor table for 2026-10-28; transcribed to `mof_cgb_curve_2026-10-28.txt` in the research
  folder, the HTML copy beside it being gitignored). **Why renminbi:** the group reports in Hong Kong dollars, but 96% of its 2025 revenue (HK$26,459m of
  HK$27,521m) arose in "Other parts of the PRC" (AR2025, note 4(ii), geographic information), its concession assets are
  in the PRC, and its fees, tariffs and most of its debt are in renminbi; Hong Kong is the place of domicile and earned
  HK$12m. The Hong Kong dollar is the reporting currency, not the earnings currency.
- **Filings read** (operator rule 4; HKEXnews, stock code 00257): Annual Reports 2016 to 2025 (files ltn20170330504,
  ltn20180328642, ltn20190408353, 2020041400632, 2021040900676, 2022040800333, 2023042600619, 2024042600614,
  2025042500497, 2026042301737); Interim Report 2026 (2026-09-16, file 2026091600258); announcements of 2025-11-14
  (proposed RMB shares, file 2025111401422), 2025-12-11 (renewal of continuing connected transactions, file
  2025121101108), 2026-07-17 (CEO resignation, file 2026071700983), 2026-10-26 (discloseable transaction, Dongguan
  concession, file 2026102600033), the 2023-02-24 profit warning (file 2023022400361) and the 2024-03-27 proposed change
  of auditor (file 2024032700363); the September 2026 Monthly Return. Rival: Dynagreen Environmental Protection Group
  (HKEX 01330) Annual Reports 2020, 2022 and 2025 (files 2021041501368, 2023041900939, 2026041300390).
- **One figure cross-checked against the filed statement:** profit attributable to equity holders of the Company for
  2025, HK$3,925,162k, in the Consolidated Statement of Profit or Loss (AR2025, page 161) equals the Five Year Summary
  (page 347) and the Interim Report 2026's comparative base. Borrowings at 31 December 2025, HK$88,548,513k (current
  HK$29,939,578k plus non-current HK$58,608,935k), read from the Consolidated Statement of Financial Position, pages 164
  to 165.
- `python tools/run.py CHFFF`: printed "CHFFF: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE" and no
  arithmetic. Every figure in this file is taken from the filed statements; the ten-year series is in
  `data_10y.csv` and the arithmetic in `calc_returns.py` (output `calc_returns_output.txt`) in the research folder.

**The balance sheets, ten of them, read before the income account** **[M2025-032]** (HK$bn, 31 December; Five Year
Summaries in AR2020 and AR2025, the statements of financial position in AR2017 to AR2025):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Contract assets, non-current (concession assets) | 25.5 | 36.8 | 43.5 | 58.9 | 79.6 | 102.0 | 97.0 | 94.9 | 93.3 | 93.6 |
| Intangible assets (operating rights) | 5.7 | 8.6 | 12.6 | 18.4 | 24.9 | 30.5 | 30.8 | 31.0 | 29.8 | 30.8 |
| Goodwill | 1.6 | 1.7 | 1.8 | 1.9 | 2.0 | 2.4 | 1.6 | 1.5 | 1.4 | 1.4 |
| Debtors (gross to 2023; net 2024 and 2025) | 1.4 | 2.3 | 2.5 | 3.7 | 6.5 | 13.8 | 16.3 | 21.4 | 21.1 | 24.2 |
| of which more than 13 months old | 0.1 | 0.1 | 0.2 | 0.4 | 1.0 | 2.4 | 5.6 | 9.0 | 9.9 | 11.6 |
| Borrowings | 21.6 | 31.5 | 38.5 | 53.2 | 75.0 | 99.1 | 94.7 | 94.6 | 91.7 | 88.5 |
| Cash, deposits and pledged deposits | 7.0 | 10.8 | 16.0 | 12.3 | 11.7 | 15.6 | 11.8 | 8.6 | 8.0 | 10.5 |
| Equity attributable to the Company | 17.4 | 22.6 | 33.9 | 36.3 | 45.1 | 51.8 | 47.4 | 48.1 | 48.2 | 52.2 |
| Non-controlling interests | 2.5 | 6.1 | 6.8 | 8.4 | 10.5 | 12.6 | 11.8 | 11.7 | 11.4 | 12.1 |
| Perpetual capital instruments | 0 | 0 | 0 | 0 | 0 | 0 | 3.5 | 5.7 | 6.8 | 7.9 |
| Share capital (rights issue of 2018) | 7.4 | 7.4 | 17.3 | 17.3 | 17.3 | 17.3 | 17.3 | 17.3 | 17.3 | 17.3 |

What moved and why, in the filer's figures: from 2016 to 2021 the concession assets quadrupled (HK$25.5bn to HK$102.0bn)
and the operating rights quintupled, paid for with borrowings (HK$21.6bn to HK$99.1bn) and a HK$10bn rights issue in
2018 (1,660,263,592 shares at HK$6.00; AR2018, Share Capital, and the Use of Proceeds section). From 2021 the build
stopped growing: concession assets flat at about HK$93bn to 97bn, borrowings down HK$10.6bn, and, from 2022, HK$7.9bn of
perpetual capital instruments issued (equity in the accounts, a fixed claim ahead of the ordinary shares in substance).
Over the whole decade debtors rose seventeenfold while revenue roughly doubled and then fell back; the part more than 13
months old rose from HK$0.1bn to HK$11.6bn and stood at HK$13.7bn at 30 June 2026 (Interim Report 2026, debtors ageing).
Goodwill is small. What the figures cannot say: whether the HK$93.6bn of concession assets and the HK$24.2bn of debtors
will be collected in full and on time; the filer itself names the payers' ability to pay as its first principal risk
(below).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which turns on the concessions' cash, not the quotation. The margin-of-safety foundation bears hardest:
"if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**, and a
business priced at about half its book value invites exactly the pencil the row warns against. No macro enters
**[M2000-094]**: the fiscal state of Chinese local governments is not forecast here; it enters only as the filer's own
statement about its own payers. Who is paid to tell you **[M2020-037]**: the report's own figures for the business
segments are "Adjusted EBITDA" (AR2025, note 4), and the filer has a fresh plan to sell shares in Shenzhen, which gives
it a reason to present well. **Contrary evidence, written down as found** **[M1997-127]**: (a) the operating cash turned
from strongly negative (2016 to 2021) to strongly positive (2024, 2025, first half of 2026), which is the case for the
business; (b) the price is about 0.56 times the book equity attributable to the Company and about 7.4 times 2025
attributable profit; (c) against it, debtors more than 13 months old grew every year of the decade and grew again in the
first half of 2026; (d) part of the 2025 operating cash came from selling subsidy receivables to a trust while keeping
liquidity support (AR2025, note 45); (e) the concessions are finite and are handed to the grantor for nothing at expiry
(AR2025, note 48(b); the Dongguan announcement of 2026-10-26).

## THE STANDING RULE
A part-interest bought for cash in the market, unlevered, puts the buyer at no risk of ruin by its financing; the rule is
the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**,
and "Never risk permanent loss of capital." **[L2023-005]**. Nothing in this business changes that, provided it is not
bought on borrowed money **[L2014-005]**. Passes for the buyer as described.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; the product need not be understood if "I understand the economic dynamics
  of the industry" **[M2011-014]**. **The parts** (Q1's holding-company paragraph, extended to segments): AR2025 note 4
  reports four segments by "Adjusted EBITDA"; 2025 environmental energy HK$7,110m, environmental water HK$1,917m,
  greentech HK$1,639m, others a loss of HK$26m, total HK$10,640m. Less each segment's depreciation and amortisation
  (energy HK$1,035m, water HK$236m, greentech HK$876m), energy earned about HK$6.1bn of HK$8.5bn of segment profit after
  depreciation, about 71%, and its share was larger in the construction years (energy construction revenue was
  HK$21.8bn of HK$49.9bn in 2021, AR2021 note 5). **Environmental energy decides** (more than half of five-year
  operating profit); water (through the 72.87%-owned Everbright Water) and greentech do not.
- **The deciding part's economics.** Waste-to-energy plants and related solid-waste plants in the PRC, built and run
  under service-concession agreements of 20 to 41 years; "The Grantors guarantee that the Group will receive minimum
  annual payments"; at expiry the plants "will be transferred to the local government authorities" (AR2025, note 48(b)).
  Revenue in operation is a waste-treatment fee paid by the local government and the sale of power to the grid at an
  on-grid tariff, part of which is a national renewable-energy subsidy settled "upon the successful completion of
  government administrative procedures" (AR2025, note 23(b)). Key variables **[M1998-044]**: tonnes received (set by
  the city's waste), the fee per tonne (fixed in the concession, raised only on approval: "2 WTE projects received
  regulatory approval to increase waste treatment fee", AR2025, Management Discussion and Analysis), power per tonne
  (467 kWh, AR2025), the tariff and subsidy, the cost of debt, and, above all, whether the payers pay. These are
  knowable from the filings and the concession terms; none turns on technology that changes fast. Do the past statements
  tell me the future ones **[M2008-033]**? The cash-flow statements do, once the construction years are separated from
  the operating years; the income account alone does not (Q4, below, and AFTER THE STOP).
- **Abroad.** The rows ask whether "we understand the nuances of the corporate governance system and taxation"
  **[M2000-141]**, and for China they ask a lower price, not a pass: "We wanted to get paid more for going into China,
  and we did, because we don’t know the game as well there." **[M2006-021]**. The governance is legible from the
  filings: Central Huijin Investment holds 43.08% through China Everbright Group (AR2025, substantial shareholders); the
  group's tax is PRC enterprise income tax at the project level, stated in the notes. The payers are arms of the state.
- **Routing.** Not a business whose industry changes fast; not a bank (Q1's bank door and the insurer sector method do
  not bear on it; the subsidiary's finance-lease receivables are HK$11m). The industry's insiders would write down a
  ten-year forecast for an operating concession portfolio; whether its castle protects anything is Q2's question.
- **VERDICT: IN**, on the deciding part (environmental energy): its ten-year economics are a portfolio of fixed-term
  concessions whose variables are stated in the filings **[M2012-065]**, **[M2011-014]**, with China's lower-price
  condition carried forward **[M2006-021]**. Doubt about the perimeter was weighed **[M2002-092]**: the doubt this file
  meets is about what the castle protects and whether the payers pay, which the rows place at Q2 and Q9, not about
  whether the business can be understood.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
*(Written by a second analyst on 2026-10-29, resuming the run after the first session ended at a usage limit. The
first analyst's draft Q7 script in the research folder carried the words "the file closed at Q2" in its header; that
was a draft conclusion in this run's own folder, not a blind-listed file. It is declared here, and the judgment below
was made from the filings and the framework's text, with the evidence against the business hunted first.)*

**The parts table** (Q2, a business of parts; segments separated because "lumping them together, as is done in standard
financial statements, impedes analysis" **[L2008-005]**). Segment profit after depreciation and amortisation (the
filer's "Adjusted EBITDA" less each segment's own D&A, AR2022 to AR2025 note 4, each year from the latest report that
prints it; `calc_q2.py`, output `calc_q2_output.txt`):

| Part | Share of five-year (2021-2025) segment profit after D&A | Castle | Decides |
|---|---|---|---|
| Environmental energy (waste-to-energy concessions) | 70.4% (64% to 75% in each year) | below | **yes, more than half** |
| Environmental water (72.87% of Everbright Water) | the rest of the 29.6% with greentech and others | not judged | no |
| Greentech (biomass, hazardous waste, solar, wind) | (impairments of PP&E and intangibles in 2024 and 2025) | not judged | no |

**The deciding part, test by test, each with its filing fact.**
1. **The castle questions** **[M1995-038]**: "why is that castle still standing?" Each operating plant stands on a
   service-concession contract of 20 to 41 years in which "The Grantors guarantee that the Group will receive minimum
   annual payments" (AR2025, note 48(b)). The key factor is the contract, and "how permanent are they?" has a written
   answer: the plant "will be transferred to the local government authorities" at expiry (same note), for nothing.
   The castle is a lease with an end date, not a franchise that renews itself.
2. **The money test** **[M2011-015]**, "if I had a hundred million dollars": an attacker with money cannot take an
   operating plant's waste stream from it during the concession; that half of the castle stands. The new concession
   is another matter: the filer's own principal risks say "the incremental market for traditional businesses has
   shrunk sharply, and market competition has become increasingly fierce" (AR2025, Principal Risks and Uncertainties,
   III, Market competition risk, page 58), and the 2023 profit warning gives the year's fall in profit as "mainly
   resulting from a significant drop in the number of new projects in the industry" and speaks of "the backdrop of
   intense competition" (announcement of 2023-02-24, HKEXnews 2023022400361). Where new capacity is won by tender
   against rivals, the industry is one of those "that are just never going to have barriers to entry" **[M2012-106]**
   for the next contract, whatever protects the last one.
3. **Pricing power** **[M2005-020]**, "a prayer session before you raise your prices a penny": the waste fee is fixed
   in each concession and moves only with the grantor's approval; in 2025 "2 WTE projects received regulatory approval
   to increase waste treatment fee", against 161 waste-to-energy projects in operation at 31 December 2025 (AR2025,
   Management Discussion and Analysis, environmental energy). The power tariff and the renewable subsidy are set by national
   policy, and the filer lists "Changes in industry and macro policies in respect of special funds, national
   (provincial) subsidies, electricity prices" as its fourth principal risk (AR2025, page 59). No pricing power.
4. **Unit volume** **[M2005-020]**: waste processed rose 3% in 2025 to 53,704,000 tonnes (AR2025, MD&A); but the
   Chairman's statement writes of "a widening waste supply gap across the industry" (AR2025, page 11), and the
   operational-stability risk names "insufficient waste volume" (AR2025, Principal Risks). The industry has more
   furnace than waste. **Contrary evidence, written down as found** **[M1997-127]**: this group's own plants are full;
   the 53,704,000 tonnes processed exceed the 51,209,500 tonnes a year of designed capacity of the 161 plants in
   operation (AR2025, MD&A). Its volume is not the weak point; its price and its payers are.
5. **Would the customer choose it over the low bid** **[M2017-009]**: the customer is a city government buying a
   service by tender, which is "people buying candy for the low bid"; the passage on a commodity service fits it:
   "Consequently, price competition in insurance is usually fierce." **[L2004-003]**. The filer's own word is "fierce".
6. **The low-cost position**: no filing read states the group's cost per tonne against a rival's; the filings give
   power per tonne (467 kWh, up 1%) and plant power use (15.5%), not a comparison. No instance found in the filings
   read of a stated cost lead.
7. **Ask the competitors**: the annual reports 2016 to 2025 name no rival (text search of all ten and the Interim
   Report 2026 for the names of the listed waste-to-energy operators, for "competitor" and "peer"; the only hits are
   "peers and partners" in the competition risk and an acquired company's name in 2021). The rival used below was
   chosen by the analyst as the other HKEX-listed waste-to-energy concession operator whose annual reports were on
   HKEXnews; the analyst read no rival's opinion of this company.
8. **Widening or narrowing** **[M1999-108]**, "how wide the moat is": narrowing on the evidence of returns (below)
   and of the payers (next).
9. **What could destroy, modify or reduce it** **[M2000-014]**, "destroy, or modify, or reduce the economic
   strengths": the payer. The filer's first principal risk: "the ability of governments at all levels to pay has been
   impaired, increasing the likelihood of deferring settlement of national subsidies, waste and waste water treatment
   fees" (AR2025, Principal Risks, I, page 55). Debtors more than 13 months old rose from HK$0.1bn (2016) to HK$11.6bn
   (2025) and HK$13.7bn at 30 June 2026, half of debtors of HK$27.5bn, which are "due within 30 to 90 days from the date
   of billing" (Interim Report 2026, note 10, HKEXnews 2026091600258); "The vast majority of the Company's accounts
   receivable comprises arrears from governments at all levels, of which national subsidy arrears account for
   approximately 45%", and the Company is "sending lawyer's letters and initiating litigation" (Interim Report 2026,
   MD&A). Subsidy receivables are sold to a trust with liquidity support kept (AR2025, note 45). A castle whose lord
   does not pay the garrison is being reduced, whatever the contract says.

**The competitor row, the field's returns over the whole span** (same metric from each filer's own filings; ten years
each, `calc_q2_output.txt`). Attributable profit over total equity including non-controlling interests (and, for this
company, the perpetual capital instruments):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| China Everbright Environment (HK$; AR2016 to AR2025) | 14.0% | 12.3% | 10.6% | 11.6% | 10.8% | 10.6% | 7.4% | 6.8% | 5.1% | 5.4% |
| Dynagreen Environmental Protection (HKEX 01330, RMB; Five-Year Operations Highlights, AR2020 HKEXnews 2021041501368 and AR2025 HKEXnews 2026041300390) | 10.3% | 10.5% | 11.9% | 11.9% | 8.7% | 10.1% | 9.5% | 7.6% | 6.9% | 7.1% |

And for the deciding part itself, segment profit after D&A over segment assets, before interest and tax: 8.4% (2021),
7.5%, 7.6%, 5.6%, 5.7% (2025) (AR2022 to AR2025 note 4). Group operating profit over equity plus net debt, before tax:
13.6% (2016) falling every year to 5.3% (2024 and 2025) (`calc_returns_output.txt`). The returns of 2016 to 2021 carried
the build: construction revenue booked at a margin under the concession accounting (energy construction revenue
HK$21.8bn of HK$49.9bn in 2021, AR2021 note 5), which ended when "the number of new projects in the industry" fell
(profit warning, 2023-02-24). The full span holds one complete turn of the field, the build and the operation that
followed; in the operating years both durable players earn about 5% to 7% on their equity, and the deciding part earns
under 6% before interest and tax on its assets, while borrowing at a group finance cost of HK$2.4bn on HK$88.5bn of
debt (AR2025). Judged in words, as the convention asks **[M1999-108]**: ordinary. Not the "excellent returns on
invested capital" a moat protects **[L2007-004]**, nor a business that will "earn a high return on capital employed
for a very long period of time" **[M2007-023]**; a field of a few large players in which, as the rows say, "you can
have only two competitors" and still have a poor business **[M2013-052]**.

**Is it the regulated-return exception?** This is the strongest case for the business and was weighed hardest. The
exception is for "a return set by a regulator", carried to Q3 as a second best **[M2009-104]**, **[L2009-012]**, where
the owner gets "more or less" "a guaranteed return" **[M2009-104]** and, in Q7's words, "an allowed return"
**[M2010-037]** on the capital invested. A minimum-payment concession looks like it. The analyst's judgment is that it is
not: (a) no regulator allows this business a return on its invested capital; the fee is the price the group bid to win
the concession, and the tariff is a national power price that pays the same per kWh to every plant whatever it cost;
(b) the guarantee is not being kept on time by the guarantors, on the filer's own account of them (test 9), and the
national subsidy that is part of the tariff is paid only "upon the successful completion of government administrative
procedures" (AR2025, note 23(b)); this is the case the rows name as the compact breaking, "I did not anticipate or even
consider the adverse developments in regulatory returns" **[L2023-011]**; (c) the rows' utility is one where "you just
pump in more money" with a known return **[M2009-104]**, and this one's added money has earned less each year since
2016. Even read as a regulated return, the Q2 text would carry it to Q3 only as a second best on "decent returns on
the incremental sums they invest" **[L2009-012]**, which the decade's figures do not show. The doubt is recorded below,
under what in the framework was unclear.

**VERDICT: OUT.** The deciding part (environmental energy, 70% of five-year segment profit) stands behind contracts that
keep an attacker out of each plant for its term, and that is a real wall; but the castle protects ordinary returns,
shown over the field's whole span in the filer's and the rival's own filings, which is the standing castle the Q2 list
sends to OUT **[L2007-004]**, **[M2013-052]**; the next concession is won by tender in a field the filer calls fiercely
competitive **[L2004-003]**, **[M2012-106]**; and the payer of the guarantee is reducing it **[M2000-014]**. The returns
are known, so this is not the tenuous moat that cannot be valued ("therefore we leave it alone" **[M2000-019]** sends
that to TOO HARD); it is the castle shown on the evidence, which closes OUT. China's lower-price condition from Q1
**[M2006-021]** is not reached, since price does not reopen a Q2 OUT.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict (closed at Q2). The ten balance sheets were read in Step 0, before the income account, as the
template asks **[M2025-032]**; the facts are under AFTER THE STOP.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (The buyback line needs the bottom of Q7's range; there are no buybacks, and Q7 is COMPUTATION only.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance. The figures the operator asks for are below, under AFTER THE STOP, headed COMPUTATION, NOT
A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part's castle (waste-to-energy concessions in the PRC) stands for each contract's term but
protects only ordinary returns, about 5% to 7% on equity for this company and its listed rival in the operating years
and under 6% before interest and tax on the deciding segment's assets, with the next contract won by tender and the
payers in arrears. COMPUTATION, NOT A CLEARANCE: the value range by Q7's convention is the no-growth case alone and is
negative, and no case examined earns the floor at HK$4.735 on the central basis.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).** Group operating profit over equity plus net debt, before tax: 13.6% (2016), 12.8%, 13.0%,
11.5%, 9.6%, 8.9%, 7.3%, 6.9%, 5.3%, 5.3% (2025); attributable profit over attributable equity 16.0% (2016) to 7.5%
(2025) (`calc_returns_output.txt`, from `data_10y.csv`). Owner cash on the all-equity basis was negative every year from
2016 to 2023 and positive in 2024 (HK$4.4bn) and 2025 (HK$10.3bn). The row on low returns held long reads: "you are not
going to do well in investing. Even if you buy it cheap to start with." **[M1998-006]** (recorded, not weighed).

**Bearing on Q4 (the accounts).** The segment measure is "Adjusted EBITDA", defined as "earnings before interest,
taxes, depreciation and amortisation" (AR2025, note 4); the rows call EBITDA "utter nonsense" **[M1998-086]** (a fact
for Q4's weighing, not a finding). The concession accounting books construction revenue at a margin and accrues
finance income on the concession assets before cash is received, the kind of accounting the rows name as "particularly,
probably, prone" to games (Q4, construction in progress); the concession assets were HK$93.6bn at 31 December 2025
(AR2025, note 23). Subsidy receivables of RMB1,440m were sold to a trust in 2025 for HK$1,564,593k, derecognised, with
liquidity support kept and a maximum exposure equal to their carrying amount (AR2025, note 45). Impairments in 2025:
goodwill HK$67m, PP&E HK$363m, intangibles HK$163m, an associate HK$214m (AR2025, note 4). Ernst & Young retired as
auditor at the 2024 AGM under the state-owned-enterprise rotation rule, with a written confirmation of no circumstances
to bring to shareholders' attention (announcement 2024-03-27, HKEXnews 2024032700363). Goodwill of HK$590m in Poland was
written off in 2022 (profit warning, 2023-02-24).

**Bearing on Q5 (the people)** (no integrity fact found that bears on honesty; the box line carries no flag). The CEO,
Mr. Luan Zusheng, resigned on 2026-07-17 "due to aged-related reason"; the Chairman, Mr. Wang Silian, is Acting CEO
(announcement 2026-07-17, HKEXnews 2026071700983). Central Huijin Investment holds 43.08% through China Everbright Group
(AR2025). The Company renewed continuing connected transactions with its parent's group on 2025-12-11 (HKEXnews
2025121101108; not read beyond its title for this run).

**Bearing on Q6 (the money and the owners).** A rights issue in 2018: 1,660,263,592 shares at HK$6.00, about HK$10bn
(AR2018); the price on 2026-10-28 was HK$4.735. A proposed issue of up to 800,000,000 RMB shares on the Shenzhen
exchange, no more than 11.52% of the enlarged capital, approved as a preliminary proposal on 2025-11-14 (HKEXnews
2025111401422); at about 0.56 times book this would be issuance below book value. No buybacks and no share options
outstanding (Monthly Return, September 2026). Interim dividend HK16.0 cents for the first half of 2026, paid on or about
2026-10-20 (Interim Report 2026). Perpetual capital instruments of HK$7.8bn issued from 2022.

**Bearing on Q9 (debt and exposures).** Borrowings HK$90.5bn at 30 June 2026, of which HK$31.0bn due within a year
(Interim Report 2026, condensed statement of financial position), against cash and deposits of HK$9.9bn; the rows'
"short-term debt maturities of size" **[L2014-024]** and "maturities must actually be met by payment" **[L2010-020]**
are the tests that would be applied. Finance costs HK$2.4bn against operating profit HK$8.0bn in 2025 (AR2025,
statement of profit or loss). Guarantees given by the Company for subsidiaries HK$247.6m at 30 June 2026 (Interim
Report 2026, contingent liabilities).

**Bearing on Q7: COMPUTATION, NOT A CLEARANCE** (the file closed OUT at Q2; `calc_q7.py`, output `calc_q7_output.txt`;
the first analyst's draft of the script was checked input by input against the filings and rewritten; HK$ throughout,
the reporting currency; the sovereign is the renminbi 30-year at 2.05%, the earnings currency's rate).
- **Owner cash**, all-equity basis: net cash from operating activities (after the company's own tax paid; interest
  paid is in financing; the concession construction spending runs through operating cash as the change in contract
  assets) less PP&E additions, operating-right (intangible) additions and acquisitions net of cash acquired; equity
  basis less interest paid, lease interest and perpetual distributions. By year, all-equity, HK$m: 2021 -12,007;
  2022 -1,852; 2023 -1,351; 2024 4,416; 2025 10,277. Five-year average **-103**; equity basis **-3,284**. Never a
  net-income proxy (operator rule 5).
- **Claims**: borrowings HK$90,514m less cash and deposits HK$9,918m at 30 June 2026, plus the interim dividend of
  HK$983m paid since (a subsequent event the interim report states), net debt **HK$81,579m**; perpetual capital
  instruments HK$7,825m and non-controlling interests at book HK$13,317m counted as claims ahead of the shares
  (CONVENTION of this run: the perpetuals rank ahead of the ordinary shares and the owner cash is consolidated, so
  the minorities' part of it must come off; book value of the minorities is used because only one of them is listed
  and the rows give no method; rationale: the alternative, leaving them out, credits the ordinary shares with cash
  they do not own). Lease liabilities are small (interest HK$2.1m in the half-year) and left out, said so. Enterprise
  value at the price HK$131,807m; owner cash needed to earn about ten percent on it: HK$13,181m a year.
- **The range by Q7's convention.** The series changes sign, and so do the halves of the window (2021-22 average
  -6,930, 2024-25 average +7,347), so the growth is meaningless and the range is the no-growth case alone, said so
  (specific (b)). (a) Is an end year aberrational? 2021 was the peak of the build, which the filer's own profit
  warning ties to "a significant drop in the number of new projects in the industry" in 2022; the build-out is a turn
  that ended, not a cycle that repeats, so no cycle base can be formed; the literal window is central and the cases
  below are shown beside. (c) Acquisitions are deducted (small: HK$1.9bn in 2021, HK$0.4bn in 2022, about nil since).
  (d) Working capital, including the rise in debtors, is inside operating cash. (e) The maintenance guess: each
  concession is handed back for nothing at expiry, so the recovery of the concession assets is a real cost; the
  guess shown is 2025 earnings before interest less the company's tax and less the tax shield on the interest at the
  25% PRC statutory rate (CONVENTION of this run: the tax an unlevered owner would pay; rationale: the all-equity
  basis is before interest, so the interest's tax saving is not the business's). (f) No growth carried, so no cap
  arises.

| Case | Owner cash a year (all-equity, HK$m) | Return at the price on enterprise value | Value at the sovereign, no growth, a share | Valued at ten percent, a share (all-equity) | Equity-only at ten percent, a share |
|---|---|---|---|---|---|
| A. Literal window 2021-25, all spending (**central**) | -103 | -0.1% | HK$-17.54 | HK$-16.89 | HK$-4.64 |
| B. 2025 less the HK$1,565m receivables sale (beside) | 8,713 | 6.6% | HK$52.46 | HK$-2.54 | HK$8.64 |
| C. 2024-25 average, the operating years (beside) | 7,347 | 5.6% | HK$41.62 | HK$-4.76 | HK$6.29 |
| D. Maintenance guess, 2025 (beside) | 6,500 | 4.9% | HK$34.89 | HK$-6.14 | HK$6.35 |

  (Equity-only figures: equity-basis owner cash times the ordinary shareholders' share of 2025 profit after the
  perpetual holders, 86.8%, over ten percent, a share. With the perpetuals and minorities left out of the claims the
  all-equity returns are 7.9%, 6.6% and 5.9% for B, C and D, still under the floor.)
- **The floor is tested first.** No case earns about ten percent on the all-equity basis at HK$4.735: the best is 6.6%
  (B), and even 2025 unadjusted (HK$10,277m) gives 7.8%. The floor convention closes such a file OUT whatever the width
  ("a point at which we drop out of the game" **[M2003-149]**). The equity-only figures clear ten percent in B, C and D
  (13% to 18% on the market value), and that gap is the flattery of a debt-financed business that the all-equity basis
  exists to refuse **[L2017-004]**; the equity-only figure "never decides alone" (Q7, On what the floor is earned).
  No research pass is owed: the box is OUT, not TOO HARD (WORK), and no case earns the floor (Part VII).
- **Reporting figures (a reporting convention, not a verdict, not entry language):** **(a) VALUE RANGE:** the no-growth
  case alone, HK$-17.54 a share (all-equity, at the 2.05% sovereign, net of claims), against a price of HK$4.735; the
  literal window is the central case and the cases beside it run to HK$52.46 at the sovereign (B), a spread that is
  itself a finding about how much the answer depends on which years are believed. **(b) FAIR PRICE:** **HK$-16.89 a
  share** on the all-equity basis (central; owner cash after the company's own tax, no conversion; the single
  no-growth case valued at ten percent, so the two ends are the same case and the average is that case), with the
  equity-only figure **HK$-4.64 a share** beside. Both negative: at no positive price does the central case earn the
  floor. Currency: Hong Kong dollars, the reporting and listing currency of 00257 (the US over-the-counter line CHFFF
  last traded at US$0.60).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (first analyst, commit 65d3eeb0); written question by question;
      committed after each (Step 0 to Q1 by the first analyst; this analyst committed the first analyst's uncommitted
      sovereign edit first (165b4757), then Q2 and everything after it in one commit (de386227): Q2 was the
      closing STOP, so no later question was answered, but the after-the-stop facts and the computation were not
      committed separately).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's. The fold is
      the dispatcher's (operator rule ten); this run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident: the commit
      subjects of the session's starting context (the CDTG run and its fold, the CHFFF commits of the first analyst)
      and the project map and memory index loaded automatically (no line about this company). Declared in the header
      and here; not used.
- [x] Every v5 id resolves (checked by `check_run.py` in the research folder); every filing fact carries its document,
      date and HKEXnews file number in place of an accession; no number without a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the file; every figure after it is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from the cash-flow statements, never a net-income proxy; the sovereign from the issuing authority
      (Ministry of Finance of the PRC curve, published on yield.chinabond.com.cn; checked: the brief's choice is the
      Ministry's own curve, and the renminbi is the earnings currency); the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations (a) to (e); the regulated-return case weighed in Q2); the
      facts for later questions are under AFTER THE STOP; no integrity fact found, so no flag.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` and `Screens/cover_shares.py` printed that the name is not an SEC filer; nothing of theirs used.
- [x] `python tools/check_framework.py` PASS before the commit.
- Gaps the analyst confesses: the low-cost position (Q2 test 6) could not be read, since no filing read compares cost
  per tonne; only one rival was compared (Dynagreen), chosen by the analyst because the report names none; the rival's
  2016 to 2025 figures come from its five-year highlights (profit and balance sheet totals), not its full statements; the
  segment assets used for the deciding part's return include segment cash and receivables, so the return on the plant
  alone is somewhat higher than 5.7%, though the receivables are part of the capital the business needs.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Two things. **First, the regulated-return exception has no edge for a concession.** Q2's list sends a standing castle
that protects ordinary returns to OUT but excepts "a return set by a regulator", and Q7's utility paragraph turns on "a
return a regulator allows on its invested capital". A government service concession with guaranteed minimum payments,
a bid fee and a state-set power tariff sits between the two: a regulator sets part of the price, but no regulator
allows a return on capital, and the price was won by tender. This run judged it outside the exception, for the three
reasons written in Q2, but a second analyst could read the guarantee as the exception and carry the file to Q3; the
text would be clearer if it said whether the exception requires a return on invested capital allowed by a regulator, or
only a price set by one, and what follows when the guarantor is in arrears. **Second, specific (a) has no rule for a
one-off build-out.** The window's first year is the peak of a construction boom the filer itself says ended, which is
aberrational on the filer's own description, but the cycle base that (a) prescribes needs a repeating cycle, and a
concession group's build is a turn that does not repeat; the run kept the literal window central and showed the
operating years and a maintenance guess beside it. Here the floor closed every case, so the choice did not decide; in a
cheaper name it would.
