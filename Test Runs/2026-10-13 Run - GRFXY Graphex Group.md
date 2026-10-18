# Company Run — GRAPHEX GROUP LIMITED (HKSE: 6128; former ADS GRFXY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker; not held.*

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's four stated departures:
(1) the lines of evidence derived by the analyst from the primary annual report; (2) competitors taken from the company's own
report; (3) no current SEC annual filing, so the primary document is the company's own annual report from HKEXnews, recorded
by document and date in place of an accession; (4) the sovereign for a currency the protocol's table does not cover.
Research folder: `Test Runs/_research 2026-10-13 GRFXY/` (notes, the arithmetic script and its output; the downloaded
reports sit in its ignored `cache/` subfolder and are not committed).

**Contamination, declared.** Before the blind rule was applied in full, a directory listing of `Test Runs/` filtered for
"grfx" or "graphex" was run to check that the dated file name was free; it returned no file. The session context showed
the map (`CLAUDE.md`), a memory index line on the state of a queue, the git status (research folders of other names) and
the subjects of the five latest commits (another company's run). None names this company; nothing of them is used. No
search under the company's former name (Earthasia International Holdings, read in the FY2019 report) was made.

**Lines of evidence (departure 1), chosen by the analyst from the FY2025 annual report:** the Chairman's Statement; the
Management Discussion and Analysis (business review, financial review, liquidity, capital commitments, share consolidation
and rights issue, events after the reporting period, prospects); the Corporate Governance Report's "Principal risks and
uncertainties" table; the notes on going concern (2.1), operating segments (4), impairments (14, 15), borrowings (30) and
related parties (40); the Five-Year Financial Summary. The earlier reports were read for the same lines over FY2016 to FY2025.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HK$0.051 a share (HKSE 6128, close 2026-10-13; Yahoo Finance chart feed, an aggregator, flagged per operator
  rule 5; last ten sessions HK$0.051 to HK$0.058, with zero volume on three of them). The ADSs (20 ordinary shares each) were
  delisted from NYSE American (Form 25-NSE, 2025-05-23, accession 0001143313-25-000028) and quoted on the OTC Expert Market;
  the company terminated the ADS programme (6-K of 2026-04-17, accession 0001493152-26-017177: notice to The Bank of New York
  Mellon on 10 April 2026, termination notice disseminated 16 April 2026, Termination Date 14 July 2026, after which the
  depositary "is expected to sell the ADSs that remain outstanding"). The aggregator returns no data for GRFXY today. The
  ordinary share in Hong Kong is the only security that trades.
- **Shares by class:** 941,313,336 ordinary shares in issue, no treasury shares; 323,657,534 non-convertible preference
  shares, unlisted (Monthly Return of Equity Issuer for the month ended 30 September 2026, HKEXnews 2026-10-02, file
  2026100200442). Check: 234,761,352 consolidated shares after the 5-to-1 consolidation of 26 March 2025, plus 704,226,370
  rights shares allotted 22 May 2025 (3 for 1 at HK$0.17), is 938,987,722; the annual report gives 941,313,336 at
  31 December 2025 and the monthly returns show no movement since. `python Screens/cover_shares.py GRFXY` returns "NOT AN SEC
  REGISTRANT in the live ticker file". The preference shares are carried in equity at HK$3,236k, are non-convertible and
  unlisted; they are left out of the per-share count and named here.
- **Market cap:** HK$48.0M (941.3M × HK$0.051), ordinary shares only.
- **Sovereign for the earnings currency:** the accounts are presented in HK$, but the earnings currency is the **renminbi**:
  Mainland China supplied HK$111.1M of HK$137.6M of FY2025 revenue (81%), the whole of the graphite segment, and the cash is
  "mainly held in HK$ and RMB" (FY2025 results, note 4 and liquidity section). The long sovereign is the **PRC Ministry of
  Finance treasury yield curve** (财政部-中国国债收益率曲线, published on the ChinaBond site under "主办单位：中华人民共和国财政部",
  yield.chinabond.com.cn, fetched 2026-10-13): **30-year 2.07% on 2026-10-12**; the longest maturity the authority publishes on
  that curve is 30 years (10-year 1.67%). The HKD sovereign (HKSAR Government Bond programme) was not used: the HK$ is the
  reporting currency, not the currency the business earns in. `python tools/sources.py` covers USD, JPY and EUR only.
- **Filings read** (operator rule 4; departure 3: HKEXnews documents by date in place of accessions): Annual Reports FY2019
  (HKEX 2020-05-11), FY2020 (2021-04-29), FY2021 (2022-04-28), FY2022 (2023-04-27), FY2023 (2024-04-29), FY2024 (2025-04-29),
  FY2025 (2026-04-30); Interim Report 2026 (2026-09-29); Rights Issue prospectus (2025-04-07); Placing announcement (2024-10-17);
  Monthly Return September 2026 (2026-10-02). On EDGAR (CIK 0001816723): the FY2022 20-F (2023-05-10, accession
  0001493152-23-016192; no later 20-F; NT 20-F 2024-05-01, accession 0001493152-24-017419); the FY2025 results announcement on
  6-K (2026-03-31, accession 0001493152-26-014336); the ADS-termination 6-K (above); the AGM-notice 6-K (2026-05-01, accession
  0001493152-26-020847); the change-of-domicile 6-K (2026-05-05, accession 0001493152-26-021235); the AGM poll 6-K (2026-07-01,
  accession 0001493152-26-031455). **One figure cross-checked against the filed statement:** FY2025 revenue HK$137,561k and
  loss attributable HK$364,644k, identical in the results announcement on 6-K (accession 0001493152-26-014336) and in the
  audited consolidated statement of profit or loss in the FY2025 Annual Report.
- `python tools/run.py GRFXY` returns "not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE"; no arithmetic lines. All
  arithmetic is by hand from the annual reports, in `Test Runs/_research 2026-10-13 GRFXY/owner_cash.py` (output beside it).
- **Owner cash after every real cost, by year (HK$'000; operating cash flow, less purchases of plant and intangibles and
  deposits for plant, less lease principal, less stock pay added back; before interest paid, which the filer shows under
  financing):** FY2021 −39,951; FY2022 +55,873; FY2023 −34,015; FY2024 −24,670; FY2025 −55,795 (of which −40,795 is the
  deposit for the new Anhui anode plant; −15,000 without it). Five-year average −19,712 (all spending), −11,553 (the plant
  deposit treated as growth spending). After interest paid: five-year average −32,436 and −24,277. Stock pay: HK$14,067k
  (FY2021), nil (FY2022), HK$16,433k (FY2023), HK$14,009k (FY2024, of which HK$5,447k to consultants), HK$12k (FY2025).
- **The balance sheets, ten years (read here because the file closes before Q4; HK$M; Five-Year Financial Summaries of the
  FY2020 and FY2025 reports and each year's statement of financial position):**

  | 31 Dec | Total assets | Total liabilities | Equity (owners) | Goodwill | Other intangibles | Trade receivables, net | Cash | Revenue | Loss to owners |
  |---|---|---|---|---|---|---|---|---|---|
  | 2016 | 234.4 | 63.2 | 171.2 | n/r | n/r | n/r | n/r | 183.8 | −9.4 |
  | 2017 | 309.1 | 167.3 | 122.2 | n/r | n/r | n/r | n/r | 128.7 | −57.3 |
  | 2018 | 314.2 | 213.8 | 91.6 | 5.4 | 36.0 | 50.2 | n/r | 197.3 | −36.0 |
  | 2019 | 1,151.5 | 930.4 | 220.7 | 105.1 | 665.7 | 108.1 | 53.9 | 313.9 | −57.1 |
  | 2020 | 1,104.2 | 935.7 | 171.5 | 101.9 | 639.3 | 69.8 | 37.7 | 388.9 | −91.7 |
  | 2021 | 1,096.9 | 905.9 | 197.3 | 101.9 | 608.6 | 123.5 | 30.2 | 391.0 | −53.5 |
  | 2022 | 894.7 | 524.8 | 380.6 | 101.9 | 512.1 | 103.0 | 31.5 | 341.2 | −69.7 |
  | 2023 | 847.3 | 477.7 | 369.7 | 101.9 | 461.0 | 148.0 | 27.2 | 291.9 | −113.2 |
  | 2024 | 809.3 | 529.0 | 280.4 | 101.9 | 408.4 | 182.1 | 15.4 | 187.9 | −111.4 |
  | 2025 | 541.9 | 500.6 | 31.5 | nil | 198.3 | 42.1 | 26.7 | 137.6 | −364.6 |

  (n/r: not read; the FY2016 and FY2017 reports were not fetched, and the five-year summary carries totals only.) What moved
  and why: the 2019 jump is the HK$692M purchase of the graphite business (Think High Global Limited, completed 7 August 2019:
  HK$210M cash, 48,000,000 shares at HK$4.02, and a HK$348.08M promissory note; FY2019 report), which put HK$101.9M of
  goodwill and HK$665.7M of intangibles on the books. Ten years, ten losses to owners. Equity was restored in 2022 by share
  issues: on 25 March 2022 the promissory-note holder took 323,657,534 non-convertible preference shares "at HK$236,270,000"
  in settlement of the note (FY2022 MD&A; carried at a fair value of HK$178,427,000, FY2025 note 34), and the NYSE American
  ADS offering raised HK$85.9M of ordinary shares; equity then fell to HK$31.5M in 2025 after HK$276.2M of goodwill and
  intangible impairments. FY2021's "other income and gains" of HK$72.5M included a HK$51.4M "gain on extension of
  promissory note" (FY2021 statement of profit or loss).
  Gross trade receivables rose from HK$143.8M (2019) to HK$276.6M (2024) while revenue fell from HK$391.0M (2021) to
  HK$187.9M (2024); the allowance against them reached HK$138.8M of HK$181.0M gross at 2025 (FY2025 note 20). Net current
  liabilities HK$182.7M at 31 December 2025 and HK$146.3M at 30 June 2026 (Interim Report 2026).

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. The
question is sharp here in a literal way: the US quotation has already closed (the ADS programme terminated 14 July 2026), and
the remaining Hong Kong quote trades a few hundred thousand shares on its busier days. The market serves and does not
instruct, "It just tells us prices." **[M2006-077]**: a price that has fallen from the rights issue at HK$0.17 (May 2025) to
HK$0.051 says nothing by itself about the business, either way. The analyst's habits bear hardest: look for "what’s wrong"
**[M2025-013]**, and research "to possibly reject your original hypothesis" **[M1998-144]**. No macro forecast enters; the
filer's own talk of "the global surge in demand for lithium-ion batteries" is the seller's projection of what it sells and
is weighed as such. **Contrary evidence, written down as found** **[M1997-127]**: (i) the FY2022 20-F said "We believe that we
have not been subject to unfavorable price competition"; the FY2025 report says graphite revenue fell 36% because of "drop in
sales order received from the customers caused by keen competition" and that "2025 was challenging in terms of pricing and
material sourcing"; (ii) every operating segment reported a segment loss in every year FY2020 to FY2025 save catering in
FY2021 and FY2022 (segment notes of each report); (iii) the capacity plans of FY2022 and FY2023 (30,000 t of spherical graphite
and 10,000 t of anode material in Heilongjiang; a 15,000 t plant in Michigan) were followed in FY2025 by a sale of the US
subsidiary and a new 15,000 t anode plant in Anhui, and in 2026 by entry into electric two- and three-wheelers; (iv) the FY2025
report places the new plant both in "Xuzhou, Anhui" with "equipment will be delivered soon" and at "our state-of-the-art
Xuancheng facility" with "the commencement of operations", in the same document.

## THE STANDING RULE
Owning a few thousand Hong Kong dollars of a quoted share bought with the buyer's own money puts nothing of the buyer's at
call: "Never risk permanent loss of capital." **[L2023-005]** binds how a purchase is financed and sized, and a purchase here
would be unlevered and small. The rule is not engaged by the buyer's conduct; the company's own position (net current
liabilities, a material going-concern uncertainty) is the target's, weighed at Q9 if reached.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The question: "can I understand it?" **[M1995-051]**, where understanding means "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" and "some notion of how the industry will develop and
where the company will stand within the industry" **[M2012-065]**.

**What the business is, from its filings.** Two reported parts (three from 2026):
- **Graphene products** (spherical graphite processed from Heilongjiang flake, sold in China as battery-anode feedstock and
  for refractory and other uses; a new anode-material plant of 15,000 t in Anhui under way). Revenue HK$215.5M (FY2020),
  HK$242.9M (FY2021), HK$214.6M (FY2022), HK$194.9M (FY2023), HK$118.0M (FY2024), HK$75.1M (FY2025); output about 12,000 t
  (FY2021), "slightly over 10,000" t (FY2022, FY2023), about 10,000 t (FY2024), about 7,800 t (FY2025). Segment result, each
  year FY2020 to FY2025: −5.3, −5.7, −7.2, −21.2, −49.4, −344.8 (HK$M, after amortisation and, in FY2025, the impairments).
  Interim 2026: revenue HK$48.4M (flat), segment result −19.1; the group's gross margin fell from 36% to 17%.
- **Landscape architecture and design** (Hong Kong, Macau and Mainland China; customers largely developers and municipal
  governments). Revenue HK$149.2M (FY2020) falling each year to HK$62.4M (FY2025); segment result FY2020 to FY2025 −14.9,
  −13.6, −3.9, −23.3, −10.0, −5.3; new contract sum HK$67.6M (2023), HK$67.8M (2024), HK$49.4M (2025), and HK$14.2M in the
  first half of 2026 against HK$29.7M a year before.
- **Electric vehicles** (from 3 February 2026: Tronche, two- and three-wheel short-range EVs sold "primarily in neighbouring
  countries of China"; and Xuzhou Hachi Motor Car Technologies, "our entry into the electric vehicle manufacturing market").
  Revenue HK$3.4M in the first half of 2026.

**The key variables** **[M1998-044]**, as the filer itself names them in its risk statements: (1) the demand for natural
spherical graphite in battery anodes, which depends on battery chemistry: "The development and adoption of new battery
technologies or alternatives to graphene products that significantly reduce the demand for our products could adversely
impact our prospects and future revenues" (FY2022 20-F, risk summary, accession 0001493152-23-016192), and "If the Group
fails to keep updated of important technological changes in the industry, the Group's business could be affected" (FY2025
Annual Report, Principal risks); (2) the price and volume a small processor can get against "competitors that are larger and
better funded" (20-F); (3) the property cycle and municipal budgets in China for the landscape part (FY2025 Principal risks:
"The slowdown of real estate development in China would affect the demand"); (4) what the company will be: in five years it
has added and dropped catering, planned and dropped a Michigan plant, planned a 30,000 t Heilongjiang expansion, started an
Anhui anode plant, and entered EV manufacturing.

**The tests, applied.**
1. *Where will it be in ten years?* **[M2000-037]**. The filer's own record answers how far its own picture held: the FY2022
   and FY2023 reports set out 30,000 t of high-purity spherical graphite and 10,000 t of anode material in Heilongjiang and a
   15,000 t plant in Michigan; by FY2025 output was 7,800 t, the US subsidiary was being sold "to concentrate its resources in
   the establishment of the Chinese market", the new capacity is a different product in a different province, and the 2026
   interim adds a third business. No picture of FY2035 can be drawn from that, by the filer or by me.
2. *Are the key variables predictable?* "If something is not very predictable, forget it." **[M1998-044]**. Variable (1) is
   battery technology, named by the filer as the risk; variable (2) turned within three years from "We believe that we have
   not been subject to unfavorable price competition" (FY2022 20-F, Competition) to a 36% fall in graphite revenue "caused by
   keen competition" and a year "challenging in terms of pricing and material sourcing" (FY2025 MD&A).
3. *Do the past statements tell the future ones?* **[M2008-033]**: no. Ten years of losses to owners (FY2016 to FY2025), a
   segment loss in every part in every year from FY2020 save catering in two years, and a business whose composition changed
   in 2019 (graphite bought), 2023 (catering gone), 2026 (US sold, EVs bought). The past statements describe a different
   company each time.
4. *Important and knowable?* "If something’s important but unknowable, forget it." **[M2006-076]**: the ten-year place of a
   small Chinese spherical-graphite and anode processor in the battery-materials field is important and is not in any document.
5. *Would the insiders write it down?* "They would say, “That’s too hard.”" **[M2000-105]**. The filer's own insiders wrote
   capacity plans in 2022 and 2023 and abandoned them by 2025; its impairment valuer in FY2025 put customer relationships at
   nil and discounted the patents at a pre-tax 25.05% (FY2025 MD&A). The people closest to the business could not hold a
   three-year picture.
6. *Can I name the winner, not just the industry?* **[M2012-067]**. The filer names no competitor, only "other active operation
   in the PRC producing comparable spherical graphite" (20-F, Competition) and "competitors that are larger and better funded".
   "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge what its profit
   margins and returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**: the filer's case for
   itself in every report is the growth of battery demand; its own graphite revenue fell by more than two thirds from FY2021 to
   FY2025.
7. *Customers or technology?* **[M2017-019]**, **[M2023-030]**: the forecast is about battery chemistry and Chinese anode
   capacity, not about what a consumer will keep asking for.
8. *How far off could I be?* **[M2011-084]**: the outcomes run from a working anode plant to the company not surviving its net
   current liabilities; the auditor (Crowe (HK) CPA Limited) reported "a material uncertainty which may cast significant doubt on
   the Group's ability to continue as a going concern" (FY2025 results on 6-K, accession 0001493152-26-014336, auditor's extract).
9. *Do I doubt it is inside?* "if you have doubts about something being into your circle of competence, it isn’t."
   **[M2002-092]**. I do.

**The routing.** Technology "where we think the future technology could hurt the business as it presently exists [...] it
won’t make it through the filter." **[M1998-008]**; the filer's own risk statement says that of itself. By the routing fixed in
Q1 ("What understanding means"), a business whose ten-year economics cannot be foreseen because its industry changes fast closes
here in TOO HARD, not at Q2. **The commodity-business paragraph** (Q2, 2026-10-12) says a dependence on a commodity price is
never by itself a STOP at Q1, "We don’t think we can predict commodity prices." **[M2016-025]**, and that a business is judged
off its figures, "if you can’t make a decision on something like PetroChina off the figures, forget about going further"
**[M2008-069]**. Read off its figures, this business cannot be decided: the figures are ten years of losses in a business that
changed shape four times, and what decides its future is not the graphite price but battery chemistry and what the company
chooses to become. That is the routing sentence's case, not the commodity paragraph's; I say so because a second analyst could
read it otherwise (see the last section).

**By parts** (Q1, A holding company, with Q2's threshold): every part lost money in every year of the window, so no part carries
"more than half of five-year operating profit"; the largest part by revenue and by loss is graphite, which decides, and which
fails the tests above. The landscape part, read alone, is a design practice tied to China's property cycle and municipal budgets,
whose revenue has fallen five years running; it does not rescue the whole, and doubt keeps the whole outside **[M2002-092]**. The
EV part is a start-up, "Start-ups are not our game." **[L2007-015]**, "We don’t do startups." **[M2008-088]**, and too small
(4.5% of interim revenue) to decide.

**Which cause.** NATURE. The deciding question, where battery-anode economics and this processor's place in them will be in ten
years, is a forecast the industry's insiders would not write down **[M2000-105]**, and the filer's insiders wrote one and
abandoned it. "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
**[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have no insights into which participants in the
tech field possess a truly durable competitive advantage." **[L1999-018]**. No filing not yet read would answer it: the reports
FY2019 to FY2025, the interim and the 20-F were read.

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**. "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a
fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. Filing facts: FY2025 Annual Report
(HKEX 2026-04-30), MD&A and Principal risks; FY2022 20-F, accession 0001493152-23-016192, risk summary and Competition.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed the file).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0, as the brief asks).
## Q5 — WHO RUNS IT? NOT REACHED (integrity facts recorded below, not judged).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (a COMPUTATION, NOT A CLEARANCE, is below for the owner's reporting figures).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE) at Q1**: the ten-year economics of a sub-scale Chinese spherical-graphite and anode processor, whose own
three-year plans did not hold and which is changing what it is, cannot be foreseen; integrity facts recorded, not judged.
No research pass (the cause is NATURE; Part VII's pass is for WORK).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box is unchanged.)*

**Bearing on Q2 (the castle and the competitors; departure 2).** No rival is named in the FY2025 Annual Report or in the FY2022
20-F. The 20-F's Competition section reads in full for graphite: "We compete, primarily, with other active operation in the PRC
producing comparable spherical graphite for the battery and EV market. We believe that we have not been subject to unfavorable
price competition or challenged with superior technology or product quality by our competitors."; for landscape: "The barriers
to entry to the landscape architecture industry in the PRC and Hong Kong are low for small size contracts". The risk summary:
"We operate in competitive markets with competitors that are larger and better funded." So no named rival files with the SEC,
and none is named at all; no competitor comparison could be made from a rival's own filing, and none is shown. The filer's own
span: graphite revenue −69% FY2021 to FY2025 with a segment loss every year; FY2025 graphite revenue fell "due to drop in sales
order received from the customers caused by keen competition", and "certain customers faced liquidity issues and defaulted in
settlement for their trade debts" (FY2025 MD&A). The North American plans (a non-binding letter of intent with Northern Graphite
Corporation of 13 November 2022, 20-F; a Michigan plant) ended in the sale of Graphex Technologies LLC for US$3M cash and 29M
shares of an OTCQB buyer (approved 20 March 2026, not completed at the results date).

**Bearing on Q3 (capital).** The graphite business was bought for HK$692M in 2019; its goodwill (HK$101.9M) is written off and
the group's other intangibles (trademarks, customer relationships, patents) are carried at HK$198.3M after FY2025 impairments
of HK$174.3M, all in the graphite segment (FY2025 segment note). The segment has not reported a profit after
amortisation in any year since. New plant: capital commitments of HK$51.4M at 31 December 2025 and an equipment contract of
RMB42.25M for the Anhui project (FY2025 MD&A, capital commitments).

**Bearing on Q4 (the accounts).** Gross trade receivables HK$276.6M at 31 December 2024 against FY2024 revenue of HK$187.9M,
with HK$69.3M of the net balance aged one to two years (FY2025 results, note 10); written down to HK$42.1M net in FY2025. The
filer features an "Adjusted segment EBITDA" (HK$14.6M in FY2025) in its financial highlights beside a loss before tax of
HK$387.6M. FY2021 income included a HK$51.4M "gain on extension of promissory note". The preference shares are described as
issued "at HK$236,270,000" (FY2022 MD&A) and carried at a fair value of HK$178,427,000 (FY2025 note 34); the accounting policy
calls them "redeemable only at the Company's option" while note 34 calls them "non-redeemable and non-convertible" (FY2025
Annual Report). The same report places the new plant in "Xuzhou, Anhui" (MD&A) and in "Xuancheng, Anhui" (Chairman's Statement),
says "the equipment will be delivered soon" and refers to "the commencement of operations at our state-of-the-art Xuancheng
facility". The FY2025 report calls Allied Apex Limited "a non-wholly owned subsidiary"; the Interim Report 2026 calls it "a wholly
owned subsidiary" and says a purchase of 40% of Tronche made it "a 58% indirect non wholly-owned subsidiary". The AGM poll of
29 June 2026 refers to "the notice of the AGM dated 30 April 2025" (6-K accession 0001493152-26-031455). The results announcement
was "agreed" by the auditor but not assured; the auditor's opinion is unmodified with a material uncertainty on going concern.

**Bearing on Q5 (integrity facts, recorded, not judged).**
- SEC reporting: the last 20-F is for FY2022; an NT 20-F was filed on 2024-05-01 (accession 0001493152-24-017419) and no 20-F for
  FY2023 or FY2024 followed; NYSE American suspended trading on 15 May 2025 and the ADSs were delisted on 23 May 2025 (ADS
  termination announcement, 6-K accession 0001493152-26-017177). The exchange's stated reason was not read.
- Board: after a death and a resignation the company did not meet the Hong Kong Listing Rules on the number of independent
  directors, the audit committee's size, or board gender diversity, and at 31 March 2026 "still does not meet the requirements of
  the Listing Rule 3.10(1), 3.10A, 3.21 and 13.92(2)" (FY2025 results, Corporate Governance Code).
- Directors as lenders: loans from the chairman (HK$9.156M at 6%) and the chief executive (HK$3.244M at 6% and RMB8.75M at
  3.75%), extended to 31 December 2027; HK$12.962M owed interest-free to executive director Mr. Qiu Bin (FY2025 note 40).
- An executive director, Mr. Zhao Aiyong, has run EV makers in Xuzhou since 2007 and is a director of Tronche, whose 40% was
  bought for HK$1.5M from "an independent third party" (FY2025 directors' biographies; Interim Report 2026). The seller's identity
  was not read.
- The graphite business is pledged: Think High Global Limited was "charged in favour of Lexinter International Inc." for the
  US$15M convertible notes and warrants of 2021 (FY2025 results, pledge of assets).
- The 2019 vendor guaranteed profits of HK$35M a year for 2020 and 2021 (FY2019 Annual Report); whether they were met was not
  read.
- Share issues, at prices per present share (the 2025 consolidation was 5 to 1; no other consolidation found in the reports
  FY2019 to FY2024): 48,000,000 consideration shares at HK$4.02 in 2019 (HK$20.10 a present share); the NYSE American ADS
  offering of August 2022 at US$2.50 an ADS, "equivalent to approximately HK$0.9798 per underlying ordinary shares" (20-F; about
  HK$4.90 a present share); a placing at HK$0.066 in October 2024 (about HK$0.33); the rights issue at HK$0.17 in May 2025,
  three for one, 704,226,370 shares, HK$119.7M gross; plus the 2022 preference shares to the note holder. Today's price is
  HK$0.051. The rows name serial issuance as a tell (Q5's list; Q6, Issuance and deals); it is recorded, not weighed.
- Stock pay of HK$14.1M (FY2021), HK$16.4M (FY2023) and HK$14.0M (FY2024) in years of losses, part of it to consultants.

**Bearing on Q6 (the money).** Loans out while borrowing from directors: a revolving HK$21M facility at 12% to EA Trading (a
joint venture) and RMB31.9M lent in FY2025 to another joint venture at 4% (FY2025 note 40). No dividend; no buyback.

**Bearing on Q9 (the target's debt).** At 31 December 2025: interest-bearing borrowings HK$174.4M (all current), promissory note
HK$29.0M (extended to 5 August 2027), convertible notes HK$3.8M, lease liabilities HK$16.4M; cash and bank balances HK$27.3M;
equity HK$41.3M; the filer's gearing ratio 541.5%; net current liabilities HK$182.7M; going concern resting on a new HK$80M loan
facility, unsigned talks with investors, debt extensions and the US disposal (FY2025 results, note 2). At 30 June 2026: borrowings
HK$166.1M, promissory note HK$28.0M, convertible notes HK$3.0M, leases HK$14.6M, cash HK$20.0M, equity HK$24.8M, net current
liabilities HK$146.3M (Interim Report 2026).

## COMPUTATION, NOT A CLEARANCE
*(The owner's two reporting figures, built as Q7 would build them. They are not a verdict and carry no entry language; the file
closed at Q1.)*

- **Owner cash** (all-equity basis, before interest, after the company's own tax; HK$'000): FY2021 −39,951; FY2022 +55,873;
  FY2023 −34,015; FY2024 −24,670; FY2025 −15,000 with the HK$40,795k Anhui plant deposit treated as growth spending (specific (e),
  the filing allows that split), −55,795 with it. Five-year average **−11,553 (central, maintenance)**; −19,712 (all spending, the
  literal window). Equity-only (after interest paid): −24,277 and −32,436. Script and output:
  `Test Runs/_research 2026-10-13 GRFXY/owner_cash.py`.
- **Specifics applied.** (a) FY2022's positive year is a working-capital release inside a run of losses; no full cycle can be
  defined in a ten-year run of losses, so the literal window is used and shown. (b) The series changes sign; the halves (FY2021-22
  average +7,961; FY2024-25 average −19,835) also change sign, so the growth is meaningless and **the range is the no-growth case
  alone**. (c) No acquisition in the window paid in cash beyond the HK$1.5M Tronche purchase after it (credited at nothing, no
  earnings filed). (d) Working capital is inside operating cash. (e) as above. (f) No growth carried, so no cap. Tax: the company
  paid little tax in loss years; no carryforward shelter is priced, since there are no profits for it to shelter.
- **Net debt** at 30 June 2026 (the latest filed balance sheet): HK$177.1M excluding IFRS 16 lease liabilities (HK$191.7M with them).
- **VALUE RANGE** (the no-growth case alone, zero nominal growth, discounted at the PRC 30-year 2.07%): business value −HK$558M
  (central) to −HK$952M (all spending); **per share, less net debt, −HK$0.78 (central) to −HK$1.20**, against a price of HK$0.051.
  Equity-only beside it: −HK$1.25 a share. No case is positive.
- **FAIR PRICE** (Part VII: each end case valued at ten percent and averaged; with one case, that case): **−HK$0.31 a share on the
  all-equity basis** (central; −HK$0.33 with leases in net debt); **−HK$0.26 a share equity-only**, beside it. Tax treatment: the
  company's own, no conversion. There is no positive fair price.
- **The floor, tested first:** no case in the range earns the floor at any positive price, "there’s just a point at which we drop
  out of the game." **[M2003-149]**; had Q7 been reached, it would have closed OUT on the floor before the width was read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Step 0, after Q1, and at the close
      (write-early). The first write of this file replaced the template text with Step 0 rather than filling the template in
      place; the template's headings are carried below Q1.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatcher's (operator rule ten); the run binds
      only once folded into the register.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One filtered listing of `Test Runs/` for the
      ticker and name was run before writing (it returned nothing); declared under contamination at the top. Nothing else.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (check script in the research folder); every filing fact has its document
      and date or its accession; no number without a filing or a row.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the figures after it are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (stock pay and lease principal deducted), never a net-income proxy; the sovereign from the
      issuing authority (PRC Ministry of Finance curve), named and dated; the price quote flagged as an aggregator's.
- [x] Contrary evidence written as found (foundations, items i to iv); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` returned no arithmetic for this name; none of its output was used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. **(1) Q1's routing sentence against the commodity-business paragraph of 2026-10-12.** The routing sends a business
whose ten-year economics cannot be foreseen "because its industry changes fast" to Q1 TOO HARD; the commodity paragraph says a
commodity dependence is never by itself a STOP at Q1 and sends the cost question to Q2. A battery-material processor sits on both:
its product is a commodity (spherical graphite) and its demand is a technology bet (anode chemistry). I applied the routing
sentence because the filer's own risk statements name technology change and the company's identity keeps changing; another
analyst could take the commodity paragraph, reach Q2, and close OUT on the high-cost producer or TOO HARD (WORK) for want of
rivals' cost data. The text does not say which governs when both describe the same business. **(2) The parts threshold when every
part loses money.** Q2's business-of-parts paragraph defines the deciding part by "more than half of the company's five-year
operating profit"; with every part at a loss every year, the share is undefined, and "where no part does, the largest part
decides" leaves "largest" unmeasured (by revenue, by assets or by loss). Here all three measures pick graphite, so nothing turned
on it. **(3) The reporting figures when owner cash is negative throughout.** Part VII's fair price and Q7's range presume a
positive cash stream; a perpetuity of losses at 2.07% yields a large negative value whose size says only that the rate is low.
I reported the negative figures as computed and said there is no positive fair price, rather than invent a floor at zero; a
stated convention for this case would make the runs comparable. A smaller point: departure (4) asks for the longest maturity from
the authority; the PRC MoF curve stops at 30 years, while the protocol's own table for other currencies names the 30-year point,
so they agree here by luck rather than by rule.
