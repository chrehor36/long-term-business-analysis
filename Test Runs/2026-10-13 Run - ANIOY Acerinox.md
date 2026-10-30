# Company Run — Acerinox, S.A. (BME Madrid/Barcelona: ACX; US unsponsored ADR: ANIOY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (this name has no
SEC accession for its accounts; see Step 0); a STOP that returns OUT or TOO HARD closes the run and later questions are
marked NOT REACHED. Copied from the template before any fetch (commit 6c983bd9).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-13), after the run was committed: not held (`PORTFOLIO.md` carries no line for ANIOY, ACX or Acerinox).

**CONTAMINATION, declared and not used.** (1) The session's opening context listed recent commit subjects, among them a
fold and a run of another company, APEMY, a stainless steel producer and a rival of this one, whose subject line gave that
run's Q2 box and its reasons (commodity producer, price set by imports, ordinary returns against a named rival) and a
computed range. I did not open that run file or its research folder. Its reasoning is close to the reasoning this run
reaches at Q2, so the reader should know I saw it before I read a page of Acerinox; the Q2 evidence below is drawn only
from Acerinox's and Outokumpu's own reports, and the strongest evidence against my reading is set out in full there.
(2) The memory index loaded into the session names counts of gate-clearers and a holding-review backlog; nothing in it
names this company. (3) The git status snapshot lists other research folder names (AYI, ARCB); not opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 16.77 a share, close 2026-10-13, ACX.MC on the Spanish continuous market (Yahoo chart via
  `tools/sources.py`; **aggregator, flagged**, operator rule 5). The ADR ANIOY closed $9.29 on 2026-10-12 (same
  aggregator). Cross-check from a primary document: the H1 2026 interim statements, Note 17, record 169,622 treasury shares
  bought on 2026-06-30 for EUR 2,702 thousand, EUR 15.93 a share.
- **ADR ratio, from EDGAR:** the F-6EF filed 2019-11-22 (accession 0001193805-19-001764, CIK 1438557, JPMorgan Chase Bank,
  N.A. as depositary) registers "American Depositary Share representing one-half of one ordinary share of Acerinox, S.A."
  Two ADSs are one share. This is the company's only kind of EDGAR filing; it files no accounts with the SEC.
- **Shares by class:** one class. 249,335,371 ordinary shares of EUR 0.25 (2025 Group Annual Accounts, Note 15.1 a,
  "249,335,371 ordinary shares of EUR 0.25 nominal value each"), unchanged at 2026-06-30 (H1 2026 interim statements,
  Note 17); treasury shares 176,622 at 2026-06-30. **Outstanding: 249,158,749.** Check against issued less treasury: done
  (the same note). `python Screens/cover_shares.py ANIOY`: "NOT AN SEC REGISTRANT in the live ticker file"; no 8-K or
  prospectus exists for this name. Largest holder: Corporación Financiera Alba, 19.29% (Note 15.1 a).
- **Market cap:** 16.77 x 249.159M = **EUR 4,178M.**
- **Sovereign for the earnings currency:** EUR, **3.76%**, ECB euro area AAA yield curve, 30-year spot
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), 2026-10-12, from the ECB data API (`tools/sources.py`), the issuing authority's
  series named in the protocol. **Currency treatment:** the group reports in euros; most of its profit is earned in US
  dollars by North American Stainless (NAS) and Haynes. The run values the euro-reported figures as filed at the euro
  sovereign, which is the earnings currency of the accounts; the translation swings this causes (EUR -288.8M in 2025 OCI)
  are noted, not modelled. A run that valued the US stream at the US Treasury rate would get a lower value, since the 30-year
  Treasury is above the euro AAA rate; that only strengthens the closes below.
- **Filings read** (operator rule 4; no accession numbers exist for these, so document and date stand in their place, as
  the brief allows). Every one is the company's own document, the in-house English translation of a Spanish original that
  prevails; I relied on the translations throughout.
  1. 2025 Acerinox Group Annual Accounts (consolidated financial statements at 2025-12-31, authorised by the board
     2026-02-25), acerinox.com.
  2. 2024 Acerinox Group Annual Accounts (at 2024-12-31), acerinox.com.
  3. 2023 Consolidated Annual Accounts and Integrated Annual Report (at 2023-12-31, with the integrated management report),
     acerinox.com.
  4. Management Report Business Year 2022 and Explanatory Notes to the Annual Financial Report (IFRS statements for 2022 and
     2021), acerinox.com.
  5. 2021 Business Year Results Report (company-format tables for 2021 and 2020), acerinox.com. **The 2020 figures in this
     run come only from this document**, in the company's own format, not from the audited 2020 statements, which I could not
     retrieve (flagged).
  6. Auditor's report and consolidated annual accounts FY2019 (with FY2018), PwC, signed 2020-02-27, CNMV file
     `AUDITA/2019/18351_en.pdf`.
  7. Consolidated annual accounts FY2017 (with FY2016), CNMV file `AUDITA/2017/17363_en.pdf`.
  8. Condensed consolidated interim financial statements for the six months to 2026-06-30, with the interim management
     report, PwC limited review, acerinox.com.
  Not read, and said so: the FY2025 Consolidated Management Report (the site's bot protection refused the fetch; the
  management-report material used is the 2023 integrated report, the 2022 management report and the H1 2026 interim
  management report); the CNMV inside-information and other-relevant-information notices (the CNMV portal query returned an
  error page). No proxy exists in the US sense; the board and pay are in the annual corporate governance and remuneration
  reports, which were not reached because the file closes at Q2.
- **One figure cross-checked against the filed statement:** net financial debt at 2021-12-31. The results report (document
  5) states EUR 578 million; the IFRS statement of financial position in document 4 gives bank borrowings 1,293,494 +
  483,271 and debentures 74,750 + 1,634, less cash 1,274,929 = EUR 578.2 million. Agrees. Second check: operating cash flow
  2022 of EUR 544 million in the management report equals "NET CASH FLOW PROVIDED BY OPERATING ACTIVITIES 544,083" in the
  IFRS cash-flow statement of the same document.
- `python tools/run.py ANIOY`: "ANIOY: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." Nothing printed; the
  arithmetic is done by hand in `Test Runs/_research 2026-10-13 ANIOY/figures.py` from the statements above.

**The ten years, as filed (EUR millions; operating income as filed; owner cash = operating cash flow after interest and
tax paid, less purchases of property, plant, equipment and intangibles, plus disposal proceeds; 2020 from document 5):**

| Year | Revenue | Operating income | D&A | Op. cash flow | Capex | Owner cash (equity) | Net interest paid | Acquisitions net | Net debt | Equity |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,968 | 157.4 | 169.8 | 268.8 | 163.0 | 111.5 | 34.7 | 0 | 620 | 2,169 |
| 2017 | 4,627 | 318.0 | 169.7 | 365.9 | 185.6 | 181.3 | 28.2 | 0 | 609 | 1,970 |
| 2018 | 5,011 | 312.1 | 166.2 | 326.4 | 146.1 | 181.7 | 15.5 | 10.5 | 552 | 2,119 |
| 2019 | 4,754 | 22.6 (after 165.5 impairment) | 175.3 | 358.7 | 145.7 | 228.2 | 14.6 | 0 | 495 | 1,929 |
| 2020 | 4,668 | 163 (company EBIT) | 179 | 421 | 99 (net) | 322.0 | 36 | 398 (VDM: 313 cash + 85 debt assumed) | 773 | 1,615 |
| 2021 | 6,706 | 809.7 | 179.1 | 387.8 | 102.1 | 298.4 | 40.3 | 0 | 578 | 2,215 |
| 2022 | 8,688 | 875.8 (after 203.9 impairment) | 192.9 | 544.1 | 136.7 | 409.4 | 25.2 | 0 | 441 | 2,548 |
| 2023 | 6,608 | 374.2 (after 156.2 impairment) | 171.1 | 481.5 | 174.9 | 307.6 | 3.5 | 0 | 341 | 2,463 |
| 2024 | 5,413 | 348.1 (incl. 146.1 gain on the Bahru sale) | 159.9 | 293.7 | 204.8 | 89.5 | 10.4 | 692.5 (Haynes 709.3 less 16.8 received) | 1,120 | 2,575 |
| 2025 | 5,781 | 153.2 | 195.5 | 455.5 | 309.8 | 145.9 | 47.0 | -68.3 (divestment receipts) | 1,189 | 2,098 |

**The balance sheets, read first** **[M2025-032]** (the file closes before Q4, so they are read here as the template asks):
- **Equity went nowhere in ten years:** EUR 2,169M at 2016 and 2,098M at 2025, through ten years in which the group
  reported profits in eight and paid dividends every year. Translation differences carry part of it (the dollar: EUR -288.8M
  in 2025 alone), and the rest is the losses written into the non-US plants (below).
- **Goodwill and intangibles grew from purchases:** EUR 72M at 2016, written down to 4M at 2019, then 98M after VDM (2021)
  and 283M after Haynes (2025). Tangible assets dominate; property, plant and equipment is about a third of total assets
  (2025 accounts, Note 9.1: "Property, plant and equipment represent 33% of the Group's total assets").
- **Inventory and receivables swing with the nickel price, not with volume:** inventories EUR 887M (2016), 1,777M (2021),
  2,156M (2022), 1,679M (2025); revenue rose 2.2 times from 2020 to 2022 on 2,196 to 2,619 thousand tonnes of melt-shop
  output (results report, document 5: "Melting shop production (thousands of tonnes) ... 2,619 2,196"). Working capital
  absorbed EUR 460M in 2021 alone (document 5: "despite an increase in working capital of EUR 460 million").
- **Debt doubled with the Haynes purchase:** net debt EUR 341M at 2023 to 1,120M at 2024 and 1,361M at 2026-06-30 (H1 2026,
  Note 8: "Net financial debt, 1.361 billion, has increased by 173 million with respect to December 31, 2025").
- **What the balance sheet does not show, the tax note does:** "The Group has unrecognized tax assets amounting to EUR
  226,806 thousand, equal to tax losses of EUR 895 million, which were not recognized for accounting purposes" (2025 accounts,
  Note 20; 2024: losses of EUR 687 million). Losses that large, unrecognised because they are not expected to be used, are the
  record of the plants outside the US.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own Acerinox "if the market closed for five years"
**[M1997-109]**, which turns the question to the plants and away from the quotation, which "just tells us prices" **[M2006-077]**.
No macro forecast enters: the nickel price, the dollar and the tariff decisions of Washington and Brussels drive these
accounts year by year, and "macro conclusions are — just never enter into the discussion" **[M2000-094]**, so none of them is
forecast here; they enter only as properties of the business (whose price is set by whom), at Q2. Margin of safety: "if you
have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. The analyst's habits: I
looked first for "what’s wrong in things" and "what you’re missing" **[M2025-013]**, and I write the contrary evidence down as
found **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) NAS has earned a profit in every year
read (EUR 63M in 2016 rising to 697M in 2022 and 307M in 2025) and produces, in the company's words, "nearly 50% of the
nation's stainless steel" (2023 integrated report); (2) over ten years Acerinox's operating income on capital employed beat the
return on capital employed of Outokumpu, the rival chosen in Q2, in every one of the ten years, on each company's own figures (Q2); (3) the European trade-defence measures
that took effect on 2026-07-01 and the US Section 232 tariff of 50% are, on the company's account, raising its plants'
volumes now (H1 2026 interim management report); (4) H1 2026 profit after minorities was EUR 77M against a loss of 18M in
H1 2025.

## THE STANDING RULE
The buyer's conduct, not the target's: a part-interest bought for cash, unlevered, at a size that cannot ruin the buyer, puts
nothing at risk that the buyer has and needs **[M2012-081]**; "borrowed money has no place in the investor's tool kit"
**[L2014-005]** governs how it would be paid for. Nothing in the target changes this line; its own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, and "the first question is, can I understand it?" **[M1995-051]**.
- **What the business is, from the filings.** Acerinox melts scrap, ferrochrome and nickel in electric-arc furnaces and
  rolls the steel into flat and long stainless products, at five stainless plants (Campo de Gibraltar, Ponferrada and
  Igualada in Spain; Ghent, Kentucky, through NAS; Middelburg, South Africa, through Columbus Stainless, 76% owned), and makes
  nickel alloys at ten High-Performance Alloys plants of VDM Metals (Germany, bought 2020-03-17) and Haynes International (US,
  bought 2024-11-21 for "USD 61 per share" in cash through NAS). Bahru Stainless in Malaysia was sold on 2024-12-03; the
  accounts give the reason as "Production overcapacity in this market and price pressure motivated the sale" (2025 accounts,
  Note 1). Two reported segments: Stainless steel and High-performance alloys (Note 7).
- **The key variables** **[M1998-044]**: tonnes shipped, the base price over the alloy surcharge, and the cost per tonne
  against the competing mill and the competing import. Each is stated in the filings: melt-shop tonnes in the results reports;
  the price behaviour in the management reports ("aggressive pricing and production policies by major Chinese and Indonesian
  competitors", 2023 integrated report); the plant-by-plant earnings in the accounts' table of each company's contribution to
  consolidated profit (Note 15.5 of the 2025 accounts and its predecessors).
- **Routing.** "We don’t think we can predict commodity prices." **[M2016-025]** and the framework's commodity-business
  paragraph hold that a dependence on a commodity price is never by itself a STOP at Q1; Q1 asks whether the business can be
  understood from its figures, "So if you can’t make a decision on something like PetroChina off the figures, forget about
  going further" **[M2008-069]**. The figures here are plain: a mill business whose earnings by plant are disclosed, whose costs
  are scrap, alloys, energy and labour, and whose price is set in a market the management describes year by year. The
  technology is old and slow-moving (the Campo de Gibraltar plant "was the first integral stainless-steel factory in the world",
  2025 accounts, Note 9.1), so the fast-change routing to TOO HARD does not apply. The parts that matter (the stainless
  segment, below, carries more than half of five-year operating profit) can each be understood by the tests; the alloys part
  can be too, as "the economic dynamics of the industry" **[M2011-014]** of an aerospace and energy alloy supplier are on the
  page. I have no doubt that the understanding question, as distinct from the castle question, is inside the circle, so the
  doubt rule **[M2002-092]** does not bite here.
- **VERDICT: IN.** The economics can be read from the figures; whether they are any good is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, and why these** (the brief's second departure: no dispatcher's list; chosen from the annual
report's own description of the business, its risk note and its management report). (1) **The parts and which decides**,
from the segment note (Note 7), because the convention closes the file on the deciding part. (2) **Who sets the price**,
from the management reports' market sections, because the accounts themselves name imports and trade defence as what moves
the price. (3) **The cost position plant by plant**, from the table of each company's contribution to consolidated profit
(Note 15.5 of the 2025 accounts and its predecessors) and from the impairment note (Note 9.1), because the commodity
paragraph asks whether the business is the low-cost producer "read from its own and its operators' filings". (4) **The
field's returns over the full cycle**, against a rival's own reports, because a standing castle that protects only ordinary
returns closes OUT. (5) **What could destroy it**, from the risk and trade-policy passages, because the earnings visibly
depend on tariff regimes. Lines (2) to (5) are what the reports themselves spend their pages on. A line I did not choose,
and say so: the high-performance-alloys order book and aerospace qualification, which bear only on the part that does not
decide.

**The question** is "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**(1) The parts table** (operating profit = segment "gross profit from operations" less depreciation and impairment, Note 7
of the 2025 accounts, the 2023 integrated report and the 2022 management report; EUR millions):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five years | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Stainless steel | 807.0 | 816.9 | 276.1 | 331.8 | 147.0 | 2,378.8 | 85.5% of the two segments (92.9% of group operating income) | below | **yes, more than half** |
| High-performance alloys | 31.1 | 93.1 | 142.0 | 81.1 | 57.6 | 404.9 | 14.5% | not judged for the box | no |
| Unallocated (holding) | -28.4 | -34.2 | -44.0 | -64.7 | -51.4 | -222.7 | | | |

The five-year total, 2,561.0, equals the sum of operating income as filed (809.7 + 875.8 + 374.2 + 348.1 + 153.2). The
stainless segment decides. It is itself four plants with different economics, and the accounts show each one's contribution
to consolidated profit after tax (EUR millions; blank where the table was not read for that year):

| Company in the stainless segment | 2016 | 2017 | 2018 | 2019 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| North American Stainless Inc. (Kentucky) | 63.4 | 165.0 | 199.7 | 268.4 | 697.5 | 579.4 | 345.7 | 306.9 |
| Acerinox Europa (Campo de Gibraltar) | 20.4 | 55.0 | 27.2 | -57.7 | -46.8 | -189.9 | -251.2 | -239.4 |
| Bahru Stainless (Malaysia; sold 2024-12-03) | -39.8 | -40.5 | -51.2 | -164.8 | -218.0 | -205.2 | -23.2 | |
| Columbus Stainless (South Africa, 76%) | 18.4 | 22.8 | 7.7 | -69.2 | | | -32.8 | -45.2 |

Sources: the "contribution profit or loss" columns of the reserves-and-results-by-company tables in CNMV 2017/17363_en (2017,
2016), CNMV 2019/18351_en (2019, 2018), the 2023 integrated report (2023, 2022) and the 2024 and 2025 Group Annual Accounts.
**In 2025 NAS contributed EUR 306.9M to a group that lost EUR 40.1M.** The castle the stainless segment has is one plant.

**(2) Who sets the price.** The accounts say it in their own words. In the US: "The U.S. steel industry continues to operate
under a well-established trade defense model based on Section 232 of the Trade Expansion Act, which imposes a 50% tariff on
steel and aluminum imports. This measure has reduced the market share of foreign imports of flat steel in the U.S. from 24%
to 22%, contributing to stable domestic market conditions despite weak demand." (H1 2026 interim statements, Note 5). In
Europe: "Imports reached levels close to 25% market share, although the Group expects these levels to fall to 15% once the
new trade defense measures come into force." (2025 accounts, Note 9.1). In Asia, the reason for leaving: "Production
overcapacity in this market and price pressure motivated the sale" (2025 accounts, Note 1, of Bahru), and "The Asian market
continued to suffer from aggressive pricing and production policies by major Chinese and Indonesian competitors" (2023
integrated report). The price in each of the group's markets is the import price plus whatever duty the government levies.
That is the business whose price a competitor sets: "whatever he charged for gas was my price." **[M2012-109]**; "he
determined our profit, because we looked at his price every day." **[M2023-079]**. The pricing-power test fails in its
plainest form: the price rises and falls with the nickel and chrome surcharge and with the tariff, and no instance was found
of a price raised against the market (the 2023 integrated report, the 2022 management report and the H1 2026 interim report,
read for price language); "it’s not a great business when you have to have a prayer session before you raise your prices a
penny" **[M2005-020]**, and here the prayer is said in Brussels and Washington.

**(3) The cost position.** Stainless coil is a commodity: the buyer takes the grade and the gauge from whoever is cheapest
after duty, the steel version of "most insureds don't care from whom they buy" **[L2004-003]**. The one way through a
commodity field the rows name is to be the low-cost operator **[L2004-007]**: "being the low-cost producer is all-important"
**[L2000-017]**, judged against the competitor **[M2001-013]**, "more by cost of production than we would by whether copper was
selling for $2.00 a pound or a dollar a pound" **[M2006-004]**. On the company's own figures:
- **Three of the four stainless plants are not the low-cost producer in their markets.** Bahru lost money in every year read
  and was sold for "overcapacity in this market and price pressure". Acerinox Europa lost EUR 46.8M, 189.9M, 251.2M and 239.4M
  in 2022 to 2025, and the accounts say "In light of the market conditions and financial results of recent years, the Group
  put forward the idea that a new organizational and production model would need to be implemented at the Acerinox Europa
  factory", which the strike of 2024 "prevented us from carrying out ... to ensure the plant's viability" (2025 accounts,
  Note 9.1). The same note: "These include Columbus Stainless in South Africa and Acerinox Europa, Roldan and Inoxfil in
  Spain", of the plants showing signs of impairment. Unrecognised tax losses of EUR 895M (Note 20) are what years of this
  leave behind. That is the high-cost producer in a commodity field: "commodity businesses have risk unless you’re the
  low-cost producer, because the low-cost producer can put you out of business." **[M1997-010]**; "In an unregulated
  commodity business, a company must lower its costs to competitive levels or face extinction." **[L1994-035]**. The rows'
  warning about protection fits Europe: the airline "had protected routes" and lived with high costs "because Southwest
  hadn’t gotten there yet with their 8 cent costs. But they get there." **[M2007-117]**.
- **NAS is the strongest evidence against this reading, and it is real.** It is profitable in every year read, it "produces
  nearly 50% of the nation's stainless steel" and is "one of the most efficient and advanced factories in the world" (2023
  integrated report); its contribution, EUR 307M to 697M a year since 2022, exceeds the whole group's profit in most of those
  years; and Outokumpu's American business, its nearest US rival among those read, earned a return on operating capital of
  13.0% in 2025 and 4.2% in 2024 (Outokumpu Annual Report 2025, business area Americas). Inside the US, NAS is the low-cost
  domestic operator. But the domestic price it earns is the import price plus the Section 232 duty: NAS contributed EUR
  63.4M in 2016, before the tariff of 2018, and 199.7M to 697.5M after it. Whether that wall stands for ten or twenty years is a
  forecast about US trade law, which the foundation "macro conclusions are — just never enter into the discussion"
  **[M2000-094]** forbids me to make, and which the company itself states only as an expectation ("Section 232 remains in
  effect, and a reduction in these tariffs is not anticipated", H1 2026, Note 8).

**(4) The field's returns over the last full cycle**, from the filer's and a rival's own reports. **The competitor row.** The
annual report names no competitor (no instance found in the 2025 accounts, the 2023 integrated report, the 2022 management
report or the H1 2026 interim report, by a search for "competitor", "Outokumpu", "Aperam", "POSCO", "Tsingshan",
"Cleveland", "ATI" and "Carpenter"; it names only "major Chinese and Indonesian competitors" and, in a share-price chart,
unnamed "European competitors"). The rivals are therefore chosen as a **CONVENTION of this run** (rationale: the report names
none, and the brief asks for rivals read from their own filings). For the deciding stainless part, **Outokumpu Oyj**, the
largest European stainless producer, with a US mill at Calvert, Alabama; it **does not file with the SEC**, and its own annual
reports were read (Annual Report 2020, five-year key figures 2016-2020; Annual Report 2025, five-year key figures 2021-2025
and the business-area tables). Among SEC filers, **Cleveland-Cliffs** owns US stainless mills but reports them inside its steel
segment, so no stainless figure can be taken from its filings (flagged, not used). Not used, and why: **Aperam**, a European
stainless producer that does not file with the SEC, is the subject of the other run named under contamination, and I chose
not to read its reports so as not to bring that run's frame into this one; **the Chinese and Indonesian producers** the report
names as a class do not file with the SEC and were not read. For the alloys part, which does not decide, the SEC filers **ATI
Inc.** (CIK 1018963) and **Carpenter Technology** (CIK 17843) were read from their XBRL company facts only (tagged data,
screening, operator rule 4; not a filing read): operating income over revenue ATI 2021-2025 4.2%, 7.5%, 11.2%, 14.0%, 14.0%;
Carpenter fiscal 2022-2026 -1.4%, 5.2%, 11.7%, 18.1%, 22.5%; Acerinox's alloys segment 3.8%, 7.3%, 9.8%, 6.0%, 3.4% on the parts
table. The alloys part trails both.

| Year | Acerinox: operating income / (equity + net debt at year end) | Outokumpu: ROCE as its own reports define it |
|---|---|---|
| 2016 | 5.6% | 2.6% |
| 2017 | 12.3% | 11.3% |
| 2018 | 11.7% | 7.0% |
| 2019 | 0.9% | 0.8% |
| 2020 | 6.8% | -1.4% |
| 2021 | 29.0% | 17.6% (restated) |
| 2022 | 29.3% | 22.6% |
| 2023 | 13.3% | -2.1% |
| 2024 | 9.4% | -1.2% |
| 2025 | 4.7% | -3.2% |
| **Ten-year average** | **12.3%, before tax** | **5.4%** |

The two measures are not identical (Outokumpu's capital employed is its own defined figure; Acerinox's is mine, equity plus
borrowings less cash at year end); the comparison is of the same kind of number over the same ten years. Acerinox beats its
European rival in every year, by about seven points on average, and the margin is the NAS plant. In absolute terms: before
tax, a ten-year average of 12.3%, which the two boom years carry (2021 was "an all-time record", results report); the other
eight years average 8.1%. The cash tax the group paid over the ten years was EUR 1,334.5M on pre-tax profit of EUR 3,275.3M,
40.7%, high because the losses in Spain and Malaysia are not deductible against the US profit; after that tax the ten-year
return on capital is about 7%. In words, as the convention asks ("ordinary" carries no figure; judged, not measured
**[M1999-108]**): a commodity field in which the best durable player earns, over a full cycle and after its own tax, a return
that is ordinary, with two exceptional years and three of its four stainless plants losing money, while the rival loses money
in five of the ten years. "you can have only two competitors and they’re still terrible businesses, they beat each other’s
brains out." **[M2013-052]**.

**(5) The other tests, briefly.** The money test: capacity in this field is built by whoever has the capital, and the
company's own reports say it was built ("the constant threat of overcapacity in Asia", 2023 integrated report); "If the answer
had been yes, we wouldn’t have done it." **[M2011-015]**, and "one competitor is frequently enough to ruin a business."
**[M2012-108]**. Shipped in from abroad: stainless coil is "a product that can be shipped in from abroad very easily"
**[M2007-116]**, which is why each of the group's markets needs a tariff. Widening or narrowing **[M1999-108]**: on the plant
table, narrowing outside the US over the decade (Europa from +55.0M in 2017 to -239.4M in 2025; Bahru sold; Columbus from
+22.8M to -45.2M), holding in the US. What could destroy it five to fifteen years out **[M2000-014]**: the removal or erosion of
Section 232 for NAS; for Europe, whether the quota regime of 2026-07-01 and the carbon border charge hold. Raw-material
pass-through: the alloy surcharge passes nickel and chrome through, which is the commodity mechanism, not pricing power
**[M2005-017]**.

**The verdict, and why OUT rather than TOO HARD.** The deciding part, stainless steel, is a commodity business which, across
its four plants, is not the low-cost producer: three lose money against imports, one of them was sold for "overcapacity in
this market and price pressure", and the segment's price in every market is the import price plus a duty. The field's returns
over the full cycle are known from the filer's and the rival's own reports and are ordinary. The framework's list sends both
to OUT ("The high-cost producer in a commodity field"; "The standing castle that protects only ordinary returns ... is OUT,
not TOO HARD"), since the tenuous-moat row sends a castle to TOO HARD only because "We don’t know how to valuate that"
**[M2000-019]**, which does not hold when the returns are known. The one plant with a castle, NAS, has one whose wall is a
statute; it is recorded above as the strongest evidence against, and the parts convention's silence on splitting a reported
segment by plant is noted at the end. Had the segment been split, NAS alone would face the question whether a tariff lasts
twenty years, which no insider would write down **[M2000-105]**; that is a TOO HARD (NATURE) question for the one plant, and it
would not make the deciding part IN.
- **VERDICT: OUT.** Deciding part: Stainless steel, 85.5% of five-year segment operating profit: a commodity producer that is
  not the low-cost operator across its plants, whose price is set by imports and tariffs, earning ordinary returns over the
  full cycle on its own and Outokumpu's reported figures **[M1997-010]**, **[M2012-109]**, **[M2013-052]**, **[L2007-004]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (facts under AFTER THE STOP).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT. NOT REACHED (facts under AFTER THE STOP).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (facts under AFTER THE STOP).
## Q7 — WHAT IS IT WORTH. NOT REACHED as a clearance; the reporting figures are below, headed COMPUTATION, NOT A CLEARANCE.
## Q8, Q9, Q10, Q12 — NOT REACHED.

---
## THE BOX
**OUT at Q2.** Deciding part Stainless steel (85.5% of 2021-2025 segment operating profit): a commodity producer that is not
the low-cost operator across its plants (Acerinox Europa, Columbus and the sold Bahru lose money against imports; NAS earns
the group's profit behind the US Section 232 tariff), its price set by imports and duties, earning ordinary returns over the
full cycle (ten-year operating income on capital employed 12.3% before tax, about 7% after its 40.7% cash tax; Outokumpu
5.4% on its own figures). **Integrity facts recorded, not judged** (earnings guidance and an adjusted EBITDA featured, below).
COMPUTATION, NOT A CLEARANCE: organic-pair range EUR 25.31 to 26.61 a share at the 3.76% euro rate against EUR 16.77, no case
earning the ten percent floor at the price (5.2% to 5.4% all-equity); fair price EUR 6.24 all-equity, EUR 10.70 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box is unchanged, operator rule 2.)* **[M1997-127]**
- **Q3 (capital).** Capex against depreciation, 2016-2025: EUR 1,668M of purchases of property, plant and intangibles against
  EUR 1,758M of depreciation and amortisation (figures.py). 2025 capex of EUR 309.8M includes the NAS expansion ("an investment
  (its thirteenth since 1990) totaling US$244 million. This will increase its production capacity by 20%", 2023 integrated
  report). Purchases: VDM Metals 2020 (EUR 313M cash plus EUR 85M debt assumed, results report 2021), Haynes International
  2024 (net cash EUR 709.3M; "USD 799 million through a cash payment by the US subsidiary North American Stainless", 2025
  accounts, Note 6); goodwill on Haynes EUR 113.7M (H1 2026). Alloys segment operating margin 3.4% to 9.8% in 2021-2025 (parts
  table), below ATI and Carpenter on their XBRL figures.
- **Q4 (the accounts).** Impairments recur: EUR 165.5M (2019), 203.9M (2022), 156.2M (2023), each charged in operating
  income and charged to the stainless segment (the 2022 and 2023 segment tables put them there; the 2019 charge was
  "Impairment of goodwill and tangible assets", the goodwill line falling from EUR 69.1M to 1.2M that year). 2025: income tax EUR 143.2M on pre-tax profit of EUR 89.8M, largely from the
  derecognition of Spanish tax credits ("tax credits recognized have decreased due mainly to the derecognition of tax credits
  recorded in Spain", Note 20). The 2024 operating income includes a EUR 146.1M "Gain (loss) on sale of shares" on Bahru. The
  management reports headline EBITDA and an "Adjusted EBITDA: EBITDA net of extraordinary events during the year" (H1 2026
  glossary; "adjusted EBITDA of 119 million" against EBITDA of 95 million for Q1 2026). In 2020 the company bridge and the 2021
  results report present cash flow from EBITDA. The auditor is PwC from 2017 (KPMG signed 2016); the opinions were not read for
  qualifications.
- **Q5 (integrity facts, recorded, not judged).** (a) Earnings guidance, quarter by quarter: "we expect the group's
  third-quarter EBITDA to be slightly higher than that of the second quarter" (H1 2026 interim management report, Outlook);
  the same form in the 2021 results report ("we expect EBITDA in the first quarter of 2022 to improve"). (b) An adjusted EBITDA
  featured beside EBITDA in the headline (above). (c) The accounts state plainly the losses at Acerinox Europa and the failed
  plan there, and name the impaired plants; no instance found of a figure dressed or a loss hidden in what was read. A later
  run that reaches Q5 must answer (a) and (b) against **[M2013-088]**.
- **Q6 (the money and the owners).** Dividend EUR 0.62 a share for 2023 and for 2024 (EUR 154.6M paid in 2025, Note 15.2), and
  an interim of EUR 0.31 for 2025 declared on 2025-12-17, in the loss year; policy: "while net debt does not exceed 1.2x recurring EBITDA for the cycle permit, the Board of
  Directors may resolve to provide Acerinox shareholders with extraordinary shareholder remuneration through share buyback plans
  or the payment of extraordinary dividends" (Note 15.2). Buybacks: EUR 206.0M of treasury shares bought in 2022 and EUR 9.4M in
  2021 (2022 management report, statement of changes in equity), cancelled through capital reductions (subscribed capital EUR
  67.6M in 2021 to 62.3M in 2023); EUR 48.7M bought in 2019 with a share-premium distribution of 54.1M. The prices paid were
  not read against a Q7 range (Q6's buyback test was not reached). The Haynes purchase was paid in cash, borrowed (net debt EUR
  341M at 2023 to 1,120M at 2024), so Q6's STOP on an all-stock deal does not arise. NAS paid its parent dividends of EUR 848M
  in 2025 (Note 15.5). Largest holder Corporación Financiera Alba, 19.29%.
- **Q9 (debt and exposures).** Net financial debt EUR 1,361M at 2026-06-30 against 2025 EBITDA (operating income plus
  depreciation, as filed) of EUR 348.6M. Columbus "led to a breach of the financial covenant associated with its `Borrowing
  Base Facility'", a waiver under negotiation, EUR 138M drawn, the parent granting "a credit facility of up to 100 million"
  (H1 2026 interim statements, Note 14, bank borrowings). Two loans of EUR 140M signed in 2026 carry covenants on net debt to equity. Long-term provisions EUR 229.8M (composition not read). Currency: the 2025 dollar fall cut equity by EUR 288.8M through translation.

## COMPUTATION, NOT A CLEARANCE
*(The file closed OUT at Q2. These are the two reporting figures the owner asked for, built by Q7's range convention in full;
nothing here is a verdict or entry language, operator rule 3. Arithmetic: `Test Runs/_research 2026-10-13 ANIOY/q7_computation.py`.)*
- **Owner cash.** Operating cash flow after interest and tax paid (which carries the change in working capital, specific d),
  less all purchases of property, plant and intangibles, plus disposal proceeds; acquisitions separately. All-equity basis:
  the same with net interest paid added back (gross; its tax shield is not removed, which flatters the all-equity figure
  slightly). Company's own tax as paid, no conversion (Whose tax); no carryforward shelter is priced, since the losses that
  shelter are unrecognised and sit in Spain and South Africa, not where the profit is.
- **(a) The base.** The literal window 2021-2025 opens on the company's "all-time record" year, an aberrational first year by
  the filer's own description **[L2005-003]**, so the base is the last full cycle, trough to trough, 2020 to 2025 (2020 the
  pandemic year, 2025 a loss year): average owner cash **EUR 289.2M all-equity, 262.1M equity-only**. The previous cycle,
  2016-2019 (trough 2016 to trough 2019): EUR 198.9M / 175.7M. The 2020 figure is the company-format one (flagged, Step 0).
- **(c) Acquisitions, and the serial-acquirer rule.** Net purchases over the cycle window, EUR 1,022.2M (VDM 398, Haynes 709.3,
  less divestment receipts 85.1), exceed half of owner cash before purchases (EUR 786.4M), so **the central figure is the organic
  pair**: purchases left out, organic growth credited. The filer reports no organic growth figure; **CONVENTION of this run**:
  organic growth is taken as the stainless business's own sales growth, 2016 (when the group was all stainless) to 2025 (the
  stainless segment), EUR 3,968.1M to 4,143.8M, **0.48% a year** (rationale: the only organic series the filings give over the
  span, and specific f's own fallback is the business's sales growth). On the literal window the purchases (EUR 624.2M) fall
  just under half of owner cash (EUR 625.4M); the run follows the cycle window that specific (a) requires and says so.
- **The default pair, beside:** purchases deducted (EUR 170.4M a year over the cycle), total growth credited: base EUR 118.8M,
  a decline of 9.55% a year between the cycle averages, carried as the bottom (b), the no-growth case the top.
- **(e) Maintenance:** the filing states no maintenance figure; capex over the cycle (EUR 171.2M a year) was below
  depreciation (EUR 179.6M), so the depreciation variant is shown beside and the central case charges all spending. **(f) The
  cap:** 0.48% does not approach any share-of-sales or discount-rate limit. Ten years then zero nominal growth, discounted at
  the euro sovereign 3.76% **[L2000-021]**; net debt at the latest filed date, EUR 1,361M plus leases taken at the right-of-use
  balance of EUR 23.5M (not separated in the condensed statements), **EUR 1,384.5M**; 249.159M shares.

| Case | Value per share at 3.76% | Expected return at EUR 16.77 |
|---|---|---|
| **Central, organic pair, all-equity: no growth / 0.48% growth** | **EUR 25.31 / 26.61** | **5.20% / 5.40%** |
| Equity-only beside (owner cash after interest, against the market value) | EUR 27.98 / 29.15 | 6.3% / 6.51% |
| Default pair beside (purchases deducted; -9.55% / no growth) | EUR 0.08 / 7.13 | below 2.2% |
| Literal window 2021-2025 beside (organic, all-equity) | EUR 23.84 / 25.08 | 4.95% / 5.15% |
| Depreciation variant beside | EUR 24.13 / 25.37 | |

- **The floor is tested first:** no case earns about ten percent at the price; the best, the equity-only growth case, earns
  6.51%. Had Q7 been reached it would close OUT on the floor, "there’s just a point at which we drop out of the game"
  **[M2003-149]**, whatever the width; the organic range itself is narrow (top over bottom 1.05). The range at the long rate
  lies above the price because the euro rate is low; the floor, not the rate, is what the price fails.
- **(a) VALUE RANGE (reporting figure):** **EUR 25.31 to 26.61 a share** (organic pair, all-equity, at 3.76%), against
  **EUR 16.77** (ACX, 2026-10-13, aggregator, flagged). Per ADS (one-half share, F-6EF 2019): EUR 12.66 to 13.30.
- **(b) FAIR PRICE (reporting figure):** each end case valued at ten percent, the two averaged, less net debt: **EUR 6.24 a
  share on the all-equity basis (central)**; **EUR 10.70 a share equity-only (beside)**. Per ADS EUR 3.12 / 5.35. On the default
  pair the fair price is negative (EUR -1.89), shown so. After the company's own tax, as paid.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 6c983bd9); written question by question; committed after Step 0 to
      Q1 (6cda002f) and after Q2 (3ba62ac4), and again at the close.
- [x] Dispatched analyst: the brief allowed per-question pathspec commits of my two paths only; the lock is the dispatcher's
      (a lock file was present in `Screens/_daily/` when I looked, not touched). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared under
      contamination: commit subjects naming the APEMY run and its Q2 reasons; the memory index; research folder names in the
      git status snapshot. Aperam's own reports were deliberately not read.
- [x] Every v5 id resolves (check script in the research folder); every filing fact carries its document and date (no
      accession exists for these accounts; the EDGAR F-6 carries its accession); the ATI and Carpenter figures are XBRL
      company facts, flagged.
- [x] The order was kept; Q2 closed the run; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy; the sovereign from the ECB;
      the price from an aggregator, flagged, and cross-checked against the company's own treasury purchase.
- [x] Contrary evidence written down as found (foundations; NAS in Q2); facts for later questions under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run.
- [x] `tools/run.py` printed nothing usable for a non-SEC name; nothing from it was used.
- [ ] Gaps, honestly: the FY2020 and FY2021 audited statutory accounts and the FY2025 Consolidated Management Report were not
      retrieved (2021 came from the IFRS statements in the 2022 management report; 2020 only from the company-format results
      report); the CNMV inside-information notices were not read; the plant contributions for 2020 and 2021 and for Columbus in
      2022 and 2023 were not read; leases were taken at the right-of-use balance.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the commit).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts convention stops at reported segments.** Acerinox reports one stainless segment that is four plants, one of
which earns more than the whole group and three of which lose money. The convention says a part "decides" at more than half
of five-year operating profit and reaches "operating segments as well as holding companies", but not whether a segment may be
split into the plants whose figures the accounts also give. I kept the reported segment as the part and recorded that a split
would put NAS alone before a TOO HARD (NATURE) question (the life of a tariff), not an IN; an operator ruling on whether
disclosed subsidiaries inside a segment can be parts would settle it. (2) **A castle that is a statute.** Q2 has no paragraph
for a moat made by trade law (Section 232, the EU quota regime): it is not the regulated return of Q3's second best, nor a
moat the business owns. I read it under the commodity paragraph, as the price set by imports plus a duty. (3) **"Ordinary"
returns with no figure** left me to judge 12.3% before tax and about 7% after tax as ordinary in words; another analyst could
call 12.3% decent. The verdict does not rest on that alone (the high-cost plants carry it), but the convention gives no help
when the filer clearly beats its rival and still earns little in absolute terms. (4) **The serial-acquirer test flips on the
window.** On the literal 2021-2025 window the purchases are 49.9% of owner cash; on the cycle window specific (a) requires they
are 65%. The text does not say which window the test reads; I used the cycle window. (5) **The all-equity add-back of
interest** is not specified gross or net of its tax shield; I added it back gross and said so. (6) **Owner cash where the cycle
base needs a year whose audited statements could not be retrieved** (2020): the convention has no rule; I used the company's
own reported operating cash flow and investment payments, which agree with the IFRS figures in every year where both were
read (2021, 2022), and flagged it.

