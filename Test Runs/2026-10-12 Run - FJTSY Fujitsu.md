# Company Run — Fujitsu Limited (Tokyo Stock Exchange: 6702; US OTC unsponsored ADR: FJTSY) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its source document and date (this name
files nothing with the SEC, so there is no accession number; see Step 0); a STOP that returns OUT or TOO HARD closes
the run and later questions are marked NOT REACHED.

**Dispatched blind run.** Analyst dispatched by the session's dispatcher under the brief of 2026-10-12 (a departure from
the canonical brief, stated by the brief: no SEC filings; the lines of evidence derived by the analyst from the annual
report's equivalents of Item 1, Item 1A and Item 7).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker; not held.*

**Contamination, declared.** (1) At the start of the run a directory listing of `Test Runs/` filtered by ticker showed a
file name, `2026-07-15 Run - FJTSY (Fujitsu Ltd).md`. A listing filtered by ticker is a search, which the blind rule
forbids; the file was not opened, and nothing beyond its name and date was seen. Its existence says only that the name
was run once under an earlier edition. (2) The session's opening git context showed the last commit subjects, which
name another company's run (FUJIY, Fujifilm Holdings) and its box. Another company; not used. (3) The analyst's memory
index carries lines on the queue state (wave counts, a count of gate-clearers); none names this company. Not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥4,250 per Tokyo share, close 2026-10-09 (Friday; 2026-10-12 was a Tokyo market holiday; the quote of
  2026-10-13 morning, ¥4,172, is intraday and not used). ADR: $26.93, close 2026-10-12. Source: Yahoo Finance chart
  API via `tools/sources.py`, an aggregator, flagged and used for the live quote only (operator rule 5). USD/JPY 158.06
  (close 2026-10-08, same aggregator); ¥4,250 / 158.06 = $26.89, against the ADR's $26.93.
- **ADR ratio:** 1 ADR = 1 ordinary share. Citibank, N.A. (depositary) Corporate Action Announcement of February 15,
  2024, "Ratio Change, Stock Distribution", Fujitsu Limited, FJTSY, CUSIP 359590304: ratio (ORD:DR) current 1:5, new
  1:1; "Unsponsored ADR Program"; custodians Citibank N.A. Tokyo Branch and The Mizuho Corporate Bank (notice PDF,
  depositaryreceipts.citi.com, caId=2520). The ratio change matched the company's 10-for-1 split of April 1, 2024. The
  quote check above agrees (the ADR trades at one share's yen price converted).
- **Shares** (one class, ordinary): issued 1,739,778,265; treasury 5,000,980; outstanding **1,734,777,285** at June 30,
  2026 (Consolidated Financial Results for the First Quarter Ended June 30, 2026, July 30, 2026, "Number of issued
  shares", Fujitsu IR site). Cross-check against the annual figures: issued 1,739,778 thousand and treasury 5,000
  thousand at March 31, 2026 (Integrated Report 2026, Financial Section, Note 18; 331,330 thousand treasury shares
  were cancelled in the year). After the quarter: the board resolved on April 28, 2026 to buy up to 100 million shares
  or ¥150 billion from May 1, 2026 to March 31, 2027 (Note 40, Events after the reporting period); the June 30 treasury
  count (5,000,980 against 5,000,060 at March 31) shows no purchases under it by June 30. Purchases from July to the price
  date are not in any document read; the count used is June 30's. `python Screens/cover_shares.py FJTSY`: "NOT AN SEC
  REGISTRANT in the live ticker file"; the count is taken by hand from the company's documents.
- **Market cap:** 1,734,777,285 × ¥4,250 = **¥7,372.8 billion** (about $46.6 billion at 158.06).
- **Sovereign for the earnings currency (JPY):** **4.085%**, the 30-year JGB on 2026-10-09, Japan Ministry of Finance,
  `jgbcme.csv` (saved in the research folder as `jgbcme_2026-10-12.csv`). (`tools/sources.py` returned 4.136% dated
  2026-10-08 from its cache; the issuing authority's file read directly carries 10-09, the later date, used here.)
- **Filings read** (operator rule 4; this name files no 20-F or 40-F, so each document is recorded by title and date in
  place of an accession number):
  - **Integrated Report 2026, Financial Section** ("Financial Section 2026, For the year ended March 31, 2026"; the
    company's own English annual financial report, audited, with the five-year summary, Management's Analysis, the
    statements, notes and the auditor's report; its value-creation pages are dated "as of June 2026"). Fujitsu IR site,
    `ir/documents/secreport/126/Financialsection2026-all.pdf`.
  - Integrated Report Financial Sections 2024 (year ended March 31, 2024), 2022 (year ended March 31, 2022) and 2020
    (year ended March 31, 2020), same site, for the ten-year balance sheets. The 2025 section (year ended March 31,
    2025) returned HTTP 404 from both hosts; the 2026 section carries that year as its comparative.
  - FY2025 Financial Results (April 28, 2026), its Financial Summary presentation, the Medium-Term Plan summary
    deck, and the **Summary Translation of the Question & Answer Session** of April 28, 2026 (CEO Takahito Tokita, CFO
    Takeshi Isobe).
  - Consolidated Financial Results for the First Quarter Ended June 30, 2026 (July 30, 2026) and its summary deck.
  - Not obtained: the English Integrated Report 2025 and 2024 main volumes (the risk and governance chapters; HTTP 429
    then 404 on both hosts); the Japanese annual securities report (yūhō, with the "business risks" section) on EDINET
    (the API needs a key; not attempted further); the notice of the general meeting (the proxy equivalent). The Item 1A
    equivalent is therefore taken from the forward-looking-statement risk list in the results releases, the contingency
    note (Note 39) and the April 28 Q&A, and this is a gap, stated.
- **The lines of evidence, chosen by the analyst** (the brief's departure): from the Financial Section's Management's
  Analysis (Item 7 equivalent) and the segment note (Item 1 equivalent): (i) the parts and which decides: Service
  Solutions against Hardware Solutions and Ubiquitous Solutions, and within Service Solutions the Regions (Japan)
  subsegment; (ii) the portfolio churn: every carve-out, sale and discontinued operation of the window; (iii) what the
  company itself says of the ten-year economics of its deciding part (the man-hour model, generative AI, modernization's
  peak); (iv) the cash: operating cash, capital spending, leases, the sale proceeds; (v) the UK Post Office Horizon
  inquiry (Note 39) for Q5 and Q9. From the risk list (Item 1A equivalent): price competition, unprofitable projects,
  R&D and acquisition risk.
- **Rename, merger, spin-off, split and disposals in the window, from the company's documents:**
  - **Share split** 10-for-1 effective April 1, 2024 (five-year summary, note 3); per-share figures restated. Earlier, a
    1-for-10 consolidation effective October 1, 2018 (the price history's split events and the Citi notice of September
    25, 2018; the 2020 section's per-share figures reflect it).
  - **Discontinued operation:** the Device Solutions segment (SHINKO ELECTRIC INDUSTRIES and FDK) classified as
    discontinued from the year ended March 2025; revenue and profit from continuing operations for the years ended March
    2024 to 2026 exclude it (five-year summary, note 4). **FDK**: Fujitsu's shares tendered to SILITECH TECHNOLOGY, tender
    closed March 13, 2025, transfer March 21, 2025. **SHINKO**: tender by JICC-04 closed March 18, 2025; Fujitsu's 50.02%
    transferred June 11, 2025 through SHINKO's buyback; gain ¥141.5 billion in discontinued operations. **Fujitsu Optical
    Components**: shares transferred to Furukawa Electric April 1, 2025.
  - **Equity-method sale:** **Fujitsu General** (44.02%), tender by Paloma Rheem Holdings closed May 28, 2025; transfer
    completed August 22, 2025 through Fujitsu General's buyback; gain ¥40.0 billion in equity-method income.
  - **Internal carve-outs (spin-offs into subsidiaries, still consolidated):** the server and storage business into **Fsas
    Technologies Inc.** (in the year ended March 2025) and the Network Products business into **1FINITY Inc.** (July 2025).
  - **Acquisition:** **BrainPad Inc.** (data and AI services), 86.30% by cash tender on December 22, 2025, consideration
    ¥48,829 million (Q1 results, business-combination note); made wholly owned in the year (Management's Analysis, cash
    flows). An investment in **Rapidus Corporation** (semiconductor maker) in the same year.
  - **Restructuring under way:** Fujitsu Frontech, exits and sales (CFO, Q&A, April 28, 2026); structural reforms in
    European and domestic hardware (¥42.2 billion of one-off losses in the year to March 2026).
  - **Segments re-cut:** "Having merged a number of business segments, the Group now has the following three reportable
    segments": Service Solutions, Hardware Solutions, Ubiquitous Solutions; and from the year to March 2027 the Service
    Solutions sub-segments change again (Q&A, Questioner A).
  - No rename and no merger (a deal paid in shares) was found in the documents read.
- **One figure cross-checked against the filed statement:** revenue for the year ended March 31, 2026, ¥3,502,971
  million, is the same in the five-year summary, the consolidated statement of profit or loss, and the segment note's
  total; operating cash ¥338,130 million and closing cash ¥450,366 million agree between the five-year summary and the
  cash-flow statement.
- `python tools/run.py FJTSY`: "FJTSY: not an SEC filer. Use the evidence ladder [...] This is UNRESEARCHED, not
  UNKNOWABLE." No arithmetic lines were printed; every figure in this run is taken by hand from the company's
  documents, arithmetic shown.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Fujitsu's business will produce, not what the quotation will do. Abroad:
the rows ask whether the buyer understands "the nuances of the corporate governance system and taxation" **[M2000-141]**
and want to be paid more where the game is less well known, "We would want it to be cheaper than if it were in the
United States." **[M2006-021]**; the reading here is of a Japanese company in English translation, with the yūhō's
risk chapter not read. The analyst's habits govern: look for "what’s wrong in things" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the Service Solutions margin more than doubled in five
years (6.0% to 15.4%) and orders in Japan were strong "across all industries" (CFO, April 28, 2026); a business that
improves this fast may be better than its history. (2) Against: the company's own CEO, asked what Service Solutions will
be worth as AI advances, said "it is difficult to picture what sort of technologies will exist 10 years from now", and
that the "death of existing applications" is something "we do believe it is possible [...] could actually occur" (Q&A,
April 28, 2026). (3) Against: the UK Post Office Horizon inquiry is an open contingency whose effect "it is difficult to
predict" (Note 39). (4) For: net cash of ¥317.2 billion at March 31, 2026 (Management's Analysis).

## THE STANDING RULE
Owning a part-interest in Fujitsu, bought for cash and held unlevered, puts no buyer at risk of ruin; the rule binds
the buyer's conduct: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Fujitsu's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The parts, and which decides** (Q1's holding-company paragraph, extended to operating segments; a part "matters" when
it decides under Q2's business-of-parts CONVENTION: more than half of five-year operating profit, or else the largest).
Service Solutions' adjusted operating profit for the five years ended March 2022 to 2026 was ¥117.2, 162.9, 237.2,
289.9 and 361.4 billion, a total of ¥1,168.6 billion, against consolidated adjusted operating profit of ¥199.8, 243.4,
265.3, 307.2 and 390.5 billion, a total of ¥1,406.2 billion (Management's Analysis, sections 1(1) and 1(2); continuing
operations, Device Solutions excluded): **83%** of the consolidated figure, which is after corporate costs. For the two
years the segment table gives all three parts, Service Solutions is ¥651.3 billion of ¥849.7 billion of segment profit
(Hardware ¥61.3 and 67.0, Ubiquitous ¥31.3 and 38.8): **77%**. *(These are the company's adjusted figures, which leave out
restructuring; the adjustment was ¥42.1 and 42.2 billion in the last two years, not by segment.)* **Service Solutions
decides.** Inside it, Regions (Japan) earned ¥260.3 and ¥293.9 billion in the last two years, 90% and 81% of the
segment's ¥289.9 and ¥361.4 billion (Global Solutions ¥5.6 and 33.3, Regions (International) ¥23.9 and 34.1); the deciding business is
**Japanese IT services**: system integration, outsourcing and maintenance for Japanese government, finance, manufacturing
and distribution customers, and now "Uvance" offerings and "modernization" of legacy systems.

**The test as the rows state it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**; "We just don’t know the economics of it 10 years from now.
[...] It’s the predictability of the economics of the situation 10 years out." **[M2000-104]**. The key variables, and
whether they are predictable **[M1998-044]**:
1. **Japanese demand for IT services and Fujitsu's share of it.** Readable from the filings, and for now strong: domestic
   order backlog ¥1,127.0 billion, up 7%; orders up 8% excluding large deals. Over ten years this variable is tied to the
   next one.
2. **The price and the effort of building and running systems, i.e. how the work is paid for.** This is the variable that
   moved the margin, and the company's own documents say it is being changed by technology now: "The Company is moving away
   from the traditional man-hour based business revenue structure of system integration, where compensation is determined
   by the number of engineers and the duration of work" (Management's Analysis, 1(3)); "we are also expanding the
   application of generative AI across delivery processes" (same); the CFO: about 75% of projects used AI "at least in a
   small way", but only "around 3 or 4%" of a project's processes, with "cases in which we achieved 100-fold productivity
   gains" on its AI development platform (Q&A, April 28, 2026). Whether that productivity stays with Fujitsu as margin or
   passes to the customer as a lower price, or lets the customer do the work itself, is the ten-year economics of the
   business, and it is not readable from any filing.
3. **The life of the legacy base.** The modernization business, 11% of segment revenue, "will peak in 2028 or 2029"
   (CEO, Q&A), and after it "modernization will focus on replacing legacy applications with AI agents".

**Test 5, would the insiders write it down** **[M2000-105]**. The company's own chief executive, asked on April 28, 2026
for Service Solutions' "irreplaceable intrinsic value proposition" as AI advances, with the questioner granting that "it
would not be possible to predict what technology will be like 10 years from now", answered: "the advancements in AI and
the speed at which they have spread throughout society [...] have been faster and more vigorous than with any other
technology to date"; "Although I am not of the belief that it would be appropriate to simply refer to this as the death of
existing applications, we do believe it is possible that such a thing could actually occur"; "Although it is difficult to
picture what sort of technologies will exist 10 years from now"; and, on customers, "I get the sense that customers are
bringing more work inhouse". Asked about AI agents replacing business applications: "it is an undeniable fact that the
applications that can take the place of SaaS, as well as the architecture and technologies that will form them, are
undergoing a rapid transformation"; "applications that up until now could only be developed by certain specific
developers [...] can now be made by users themselves. It is also true that this is rapidly spreading." The insider was
asked to write the ten-year forecast down and declined; the medium-term plan he offers in its place is a three-year
target, not a forecast of the industry's economics. This is the case of **[M2000-105]**: "They would say, “That’s too
hard.”"

**The company is itself changing fast.** In the window it sold or carved out its device, optical-component and
air-conditioner interests, spun its server, storage and network businesses into subsidiaries, re-cut its segments twice,
and describes itself as "a technology company" pursuing AI, quantum computing and a next-generation processor (Management's
Analysis, 1(7); Q&A). "We view change as more of a threat into the investment process than an opportunity. [...] whenever
we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on that." **[M1999-063]**;
"if something comes in where there’s a technological component that’s of significance, or where we think the future
technology could hurt the business as it presently exists, we look at, you know, we look at that as something to worry
about. We will — it won’t make it through the filter." **[M1998-008]** *(the dash is the transcript's, kept as printed)*.

**Against this, written down** **[M1997-127]**: the forecast is partly about customers, not technology (test 7,
**[M2017-019]**), and Japanese government and bank customers change vendors slowly; the CEO also reports that customers who
bring work in-house "ask for Fujitsu's help", so "the volume of requests to Fujitsu is also increasing". This bears on
Fujitsu's competitive position, which is the more foreseeable half; it does not fix the earning power, which turns on who
keeps the productivity of a technology the CEO calls the fastest-spreading to date. Seeing strong demand for the industry
is not judging its margins: "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean
we can judge what its profit margins and returns on capital will be" **[L2009-005]**. And the doubt rule decides the edge:
"if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.

**Which cause.** NATURE, not WORK. The deciding question is how generative AI changes the price and effort of Japanese
system integration over ten years; no filing not yet read would answer it, and the industry's own insider says he cannot
picture it. "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of
its long-term economics." **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have no
insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**. The
routing is Q1's own: a business whose ten-year economics cannot be foreseen because its industry changes fast closes at
Q1, TOO HARD **[M1998-008]**. It is not a finding against the business: "It doesn’t mean it isn’t a good buy. It doesn’t
mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**, on the deciding part, Service Solutions (83% of five-year consolidated
  adjusted operating profit): its ten-year economics turn on how generative AI changes the man-hour system-integration
  model, which the company's own chief executive said on April 28, 2026 he cannot picture. Q2 to Q12 NOT REACHED; what
  follows is COMPUTATION, NOT A CLEARANCE, and facts recorded, not weighed.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). The parts table and the competitor row are recorded under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The template asks that the eight to ten years of balance sheets be read in Step 0 when the file closes
before Q4; they are read under AFTER THE STOP, Q4, below, as facts, not weighed.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts were found and are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts recorded below.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. **COMPUTATION, NOT A CLEARANCE** (operator rule 3), made because the owner asks for the two
reporting figures; it carries no entry language and changes no box. Workings: `owner_cash.py`, `value.py` and their
outputs in the research folder.

**Owner cash, years ended March 2022 to 2026, ¥ billion** (filed cash-flow statements: Financial Sections 2022, 2024 and
2026; never a net-income proxy, operator rule 5):

| | 2022 | 2023 | 2024 | 2025 | 2026 | avg |
|---|---|---|---|---|---|---|
| Operating cash flow (as filed, includes Device Solutions to its sale) | 248.3 | 220.3 | 309.2 | 303.9 | 338.1 | |
| less purchases of PP&E and intangibles, net of PP&E sale proceeds | (143.3) | (152.5) | (191.1) | (150.9) | (78.1) | |
| less lease payments (all leases; leases kept out of net debt) | (62.3) | (58.6) | (52.6) | (46.3) | (46.6) | |
| less payments for acquisitions of subsidiaries (GK Software 2024, BrainPad 2026) | 0 | (9.8) | (43.3) | (0.9) | (45.8) | |
| less Device Solutions' owner cash (estimate, see below) | (45.6) | (19.7) | 34.9 | (1.0) | 0 | |
| less stock pay (Note 33; earlier years not read) | | | | (4.3) | (6.3) | |
| **Owner cash, continuing, equity basis** | **(2.9)** | **(20.3)** | **57.2** | **100.4** | **161.4** | **59.2** |
| less interest and dividends received, plus interest paid | (5.5) | (5.8) | (12.6) | (8.3) | (12.9) | |
| **Owner cash, continuing, all-equity basis** | **(8.3)** | **(26.0)** | **44.6** | **92.1** | **148.5** | **50.2** |

- **Device Solutions removed** (discontinued; SHINKO and FDK sold): for 2022 to 2024 estimated from the segment notes as
  adjusted operating profit × 0.7 + depreciation − capital expenditure (2022: 78.3, 34.8, 44.0; 2023: 77.4, 39.0, 73.5;
  2024: 18.3, 31.8, 79.6); 2025 from Note 30, discontinued operating cash 53.8 less investing 52.8; 2026 taken as zero
  (operating cash 9.1, capital spending for the ten weeks to the sale not disclosed). The 0.7 is a CONVENTION of this run
  (an assumed 30% tax on the segment's profit; rationale: the segment notes give no segment tax and the estimate needs
  one; between 20% and 40% it moves the five-year average by under ¥3 billion either way).
- **Sale proceeds of businesses left out**: SHINKO and Fujitsu General (¥298.7 billion in 2026) and earlier sales.
  CONVENTION of this run, confessed: Q7 specific (c) nets businesses sold against businesses bought; the filer calls
  these sales "asset recycling" and excludes them from its own core cash flow, and the sold businesses' cash flows have
  been removed from the series, so crediting the proceeds as well would count a one-time sale as recurring cash. The
  literal series, proceeds credited and Device Solutions kept in, is shown beside: 59.1, 87.5, (7.3), 148.2, 466.4;
  average 150.8.
- **The company's own "core free cash flow"** (184.4 to 289.9 over FY3/2021 to FY3/2026) is higher than owner cash
  chiefly because it does not deduct lease payments (financing) or acquisitions; it is an adjusted figure, given for
  comparison only.
- **Specific checks.** (a) No end year is called aberrational by the filer (2023's working-capital draw is reversed in
  2024 "to reduce inventories and to collect accounts receivable", Financial Section 2024, cash flows); not applied.
  (b) The series changes sign: no end-to-end rate; the halves (2022-2023 average −17.2, 2025-2026 average 120.3,
  all-equity) are meaningless because the first half is negative; **so the range is the no-growth case alone, said
  so.** (c) Acquisitions deducted (default pair); purchases over the window (¥99.8 billion) are 28% of owner cash
  before purchases (¥350.7 billion, all-equity), under half: not a serial acquirer; the organic pair is in the workings
  (average 70.1). No merger (a deal paid in shares) and no signed unclosed deal found. (d) Working capital counted (it
  is inside operating cash). (e) The filing gives no split of capital spending into maintenance and growth that would
  allow the guess; the central case is all spending. (f) No growth is carried, so the cap does not bind.
- **Net debt** (all-equity basis), latest filed balance sheet, June 30, 2026 (Q1 results): borrowings about ¥3.1 billion
  (borrowings and lease obligations ¥133.7 billion less lease liabilities, taken at their March 31 figure of ¥130.6
  billion because the quarter does not split them), less cash ¥597.9 billion and other investments (securities)
  ¥165.1 billion: **net cash ¥760.0 billion**. Leases are left out of net debt because their payments are deducted in
  owner cash; equity-method investments (¥86.0 billion) are left out, and dividends are out of all-equity owner cash. At
  March 31, 2026 (audited year end, before the seasonal collection of receivables) net cash was ¥605.5 billion; per
  share that is ¥89 lower on every figure below. No subsequent event stated in the filings changes net debt.
- **Rate:** 4.085%, MOF 30-year JGB, 2026-10-09.

**VALUE RANGE (by Q7's range convention, specific (b) applied: the no-growth case alone):** five-year average
all-equity owner cash ¥50.2 billion, ten years at no growth then zero nominal growth, at 4.085%: ¥1,228.9 billion, plus
net cash ¥760.0 billion = ¥1,988.9 billion, over 1,734,777,285 shares = **¥1,146 per share, against ¥4,250**
(ADR $26.93, ratio 1:1). Beside it, not the range: the five-year average carried at Service Solutions' sales growth of
5.4% a year (FY3/2021 to FY3/2026), ¥1,551; the last three years' average (¥95.1 billion) at no growth, ¥1,780; the
last year alone (¥148.5 billion) at no growth, ¥2,534, and at 5.4%, ¥3,732; the company's own core free cash flow of
¥289.9 billion at no growth, ¥4,529. Every case but the last, which is an adjusted figure, is below the price.

**The floor, tested first.** At ¥4,250 the business is priced at ¥6,612.8 billion net of cash. Five-year average owner
cash yields 0.76% on that, the last year 2.25%; to reach about ten percent the last year's owner cash would have to grow
about 7.6% a year forever, against consolidated continuing revenue that was flat over FY3/2024 to FY3/2026. No case
earns the floor at the price: "there’s just a point at which we drop out of the game." **[M2003-149]**. Had Q1 passed,
Q7 would close OUT on the floor; it is recorded only as computation.

**FAIR PRICE (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and averaged; here
both ends are the one no-growth case: ¥50.2 billion at 10% = ¥502.0 billion, plus net cash ¥760.0 billion = **¥727 per
share, all-equity basis, central** (ADR about $4.60 at 158.06). **Equity-only, beside:** owner cash after interest,
¥59.2 billion at 10%, no net cash added: **¥341 per share**. Tax: owner cash is after the company's own income tax as
paid (operating cash is after taxes paid), no conversion; no carryforward that runs out inside ten years was identified
in the documents read. No cheap price is reported.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED. Facts recorded below.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE) at Q1**, on the deciding part (Service Solutions, 83% of five-year adjusted operating profit): its
ten-year economics turn on how generative AI changes the man-hour model of Japanese system integration, which the
company's own chief executive said on April 28, 2026 he cannot picture ten years out. The closed box; a lower price does
not reopen it. COMPUTATION, NOT A CLEARANCE: value ¥1,146 per share (no-growth case alone) against ¥4,250; fair price
¥727 all-equity, ¥341 equity-only; no case earns the floor at the price. **Integrity facts recorded, not judged** (the
UK Post Office Horizon inquiry, Note 39).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box unchanged, operator rule 2.)*

**Q2, the parts table** (adjusted operating profit, ¥ billion; years ended March 2025 and 2026 from the Financial
Section 2026 segment table; five-year share from Management's Analysis):

| Part | 2025 | 2026 | margin 2026 | share | decides |
|---|---|---|---|---|---|
| Service Solutions (Regions Japan 260.3 / 293.9) | 289.9 | 361.4 | 15.4% | 83% of five-year consolidated adjusted OP | yes |
| Hardware Solutions (servers, storage, network; Fsas, 1FINITY) | 61.3 | 67.0 | 6.6% | | no |
| Ubiquitous Solutions (PCs) | 31.3 | 38.8 | 16.9% | | no |
| Corporate / eliminations | (75.3) | (76.7) | | | |

Service Solutions margin: 6.0% (FY3/2021), 6.1%, 8.2%, 11.1%, 12.9%, 15.4% (FY3/2026); the improvement is recent and
has not been through a downturn in Japanese IT spending. Gross margin 33.1% (FY3/2023) to 38.7% (FY3/2026), which the
company attributes to standardized and automated delivery, generative AI, "value-based pricing" and portfolio change.
The CFO: the offshoring and standardization gains "are starting to level off". Domestic backlog ¥1,127.0 billion, up 7%.

**Q2, the competitor row.** The documents read name no rival. An analyst at the April 28, 2026 briefing named NEC
(BluStellar), which does not file with the SEC; NTT DATA and Hitachi, the other Japanese system integrators, do not
either, and no figure of theirs was read. The analyst chose three SEC filers in IT services and legacy outsourcing (XBRL
transcription, flagged): **Accenture** operating margin 13.7% to 15.2% in every year read, CY2016 to CY2025 (10-K
0001467373-25-000217 and earlier); **IBM** pre-tax margin 1.9% to 15.4%, erratic, revenue $79.9 billion to $67.5
billion after the 2021 Kyndryl spin-off (0000051143-26-000010); **DXC Technology**, the legacy-outsourcing case,
operating margin 6.2% to 15.8%, revenue $21.7 billion (CY2017) to $12.6 billion (CY2025) (0001688568-26-000022).
**Fujitsu**, statutory operating margin, FY3/2017 to FY3/2026: 2.8%, 4.5%, 3.3%, 5.5%, 7.4%, 6.1%, 9.0%, 4.3%
(continuing), 7.5%, 9.9%. Over the whole span Fujitsu's consolidated margin was below Accenture's in every year and
mostly below DXC's; only its Service Solutions segment has lately reached Accenture's range. Detail: `competitors.txt`.

**Q3.** Owners' equity ¥1,590.7 billion (March 2022) to ¥2,024.9 billion (March 2026); FY3/2026 adjusted operating
profit ¥390.5 billion. Capital spending fell below depreciation in FY3/2026 (net ¥78.1 billion against depreciation,
amortization and impairment of ¥141.2 billion, which includes discontinued operations and right-of-use depreciation).

**Q4, the balance sheets, March 2019 to March 2026** (¥ billion; Financial Sections 2020, 2022, 2024, 2026):

| March | cash | trade receivables | inventories | goodwill + intangibles | interest-bearing debt incl. leases | treasury stock | retained earnings | owners' equity | total assets |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 416.7 | 906.1 | 226.0 | 155.3 | 316.2 (pre-IFRS 16) | (29.6) | 576.9 | 1,132.1 | 3,104.8 |
| 2020 | 451.9 | 879.5 | 238.1 | 143.9 | 405.6 (IFRS 16 leases added) | (59.6) | 735.9 | 1,241.0 | 3,187.4 |
| 2021 | 481.8 | 859.9 | 237.0 | 161.7 | 316.3 | (79.5) | 909.1 | 1,450.1 | 3,190.2 |
| 2022 | 484.0 | 878.5 | 309.8 | 181.3 | 285.3 | (128.9) | 1,088.4 | 1,590.7 | 3,331.8 |
| 2023 | 355.9 | 927.8 | 337.0 | 201.4 | 211.2 | (277.7) | 1,226.6 | 1,586.8 | 3,265.6 |
| 2024 | 342.1 | 928.7 | 298.8 | 293.6 | 245.7 | (380.9) | 1,487.4 | 1,752.4 | 3,514.8 |
| 2025 | 236.1 | 894.9 | 205.9 | 307.5 | 247.1 | (559.7) | 1,701.0 | 1,741.0 | 3,497.8 |
| 2026 | 450.4 | 898.0 | 204.1 | 369.5 | 133.1 | (10.8) | 1,533.3 | 2,024.9 | 3,399.7 |

What moved and why: owners' equity rose from ¥1,132 billion to ¥2,025 billion while revenue fell from ¥3,952 billion
to ¥3,503 billion, the fall being disposals (Device Solutions in this window); retained earnings rose by about ¥1,674
billion before the ¥717.5 billion of treasury stock cancelled in FY3/2026 was charged against them; borrowings fell to
almost nothing beside the leases; goodwill and intangibles more than doubled (GK Software, BrainPad, software); trade
receivables stayed near ¥0.9 trillion, about 23% of revenue in 2019 and 26% in 2026; inventories rose to ¥337 billion
in 2023 and came back to ¥204 billion. Cash at March 2025 is low because SHINKO's cash sat in assets held for sale.
What the figures do not say: the segment economics before FY3/2023, because the segments were re-cut twice.

**Q4, the real costs and the featured figures.** "One-time" adjustments recur: operating profit against adjusted
operating profit was ¥149.3 against ¥265.3 billion (FY3/2024), ¥265.1 against ¥307.2 billion (FY3/2025), ¥348.3
against ¥390.5 billion (FY3/2026), the adjustments being business restructuring, business-model transformation and M&A
costs. The company features adjusted operating profit, adjusted EPS and core free cash flow, and reports results
against its Medium-Term Management Plan ("both exceeding levels forecast in the Medium-Term Management Plan"; the CFO
calls the FY3/2027 margin target "reasonable"). Stock pay ¥4.3 and ¥6.3 billion (Note 33).

**Q5, integrity facts, recorded, not judged.** Note 39, Contingencies: "Fujitsu Services Ltd., the Company's
consolidated subsidiary, is responding to the UK statutory public inquiry regarding an accounting system for the UK
Post Office. Based on the findings of the inquiry, we will take appropriate measures with the UK government, but it is
difficult to predict the impact of this matter on the consolidated financial statements at this time." The inquiry's
own reports were not read (not a company filing); what it found about the conduct of Fujitsu's staff, and what Fujitsu
has said and paid, is the first thing a later run reaching Q5 must read and answer **[M2013-088]**. The governance
report, the notice of meeting and director pay were not read.

**Q6.** Buybacks: ¥453.1 billion over the three-year plan; ¥170.0 billion in FY3/2026 for 43,311 thousand shares, an
average of ¥3,926 per share, against the computed range of ¥1,146; the April 28, 2026 programme names a number of
shares and an amount (up to 100 million shares, ¥150 billion) and no price; 331,330 thousand treasury shares cancelled.
Dividends raised every year since fiscal 2016 (Management's Analysis). The CFO: "if we were to make an acquisition of
around 1,000 billion yen, then it is possible that we may lower the amount of share buybacks"; "our first consideration
will be dividends, and our second will be growth investments". Acquisitions in the window paid in cash (GK Software,
BrainPad); no all-stock deal found. Book value per share ¥809 (March 2022, split-adjusted) to ¥1,167 (March 2026).

**Q9.** Net cash (see Q7). Bond ratings A3 (Moody's) and AA− (R&I) "as of the submission date of this report". UK
defined-benefit plan (closed to new members in 2000; a special contribution of ¥114,360 million in March 2013);
retirement benefit assets ¥206.6 billion against liabilities ¥92.2 billion at March 2026. The Horizon contingency is
unquantified (Note 39). The results releases' risk list names "Potential emergence of unprofitable projects" and
"Intensifying price competition".

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each closing step
      (Step 0 to Q1 at the stop; then the computation, the facts after it and the audit). The file closed at Q1.
- [x] Dispatched: the brief allowed the per-question commits and states the lock is held by the dispatching session;
      the fold is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Not met in full:** a
      directory listing of `Test Runs/` filtered by ticker was run at the start and showed the name of an earlier run
      file of this company; declared under contamination above; not opened, not used.
- [x] Every v5 id resolves (checked by `check_ids.py` in the research folder); every filing fact has its document and
      date (this name has no accession numbers; the SEC competitor figures carry theirs); no number without a filing or
      a CONVENTION label.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the Ministry of Finance file; the
      price and FX quotes flagged as aggregator.
- [x] Contrary evidence written down as found (the foundations; Q1's "Against this"); facts for later questions under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (not a point-in-time run).
- [x] `tools/run.py` printed no arithmetic for this name; nothing it prints as a rule was used.
- [x] `python tools/check_framework.py` PASS before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Discontinued operations inside the five-year window.** Q7's specifics cover acquisitions, mergers and sale
proceeds, but not how to take a sold segment's own cash flows out of a consolidated cash-flow statement that is not
restated (IFRS restates the income statement for discontinued operations, not the cash-flow statement, and the filer
gives the discontinued cash flows for two years only). This run estimated the segment's owner cash from the segment
notes, with a tax rate confessed as its own CONVENTION; a rule is needed, because the estimate moved 2022 owner cash
from +42.8 to −2.9. (2) **Netting businesses sold against businesses bought** (specific (c)) credits the sale of a whole
segment as owner cash when the segment's earnings have also left the series; here the literal reading triples the
five-year average (150.8 against 50.2 to 59.2). This run left the proceeds out and showed the literal series beside;
the text should say which. (3) **Leases under IFRS 16.** The all-equity convention puts finance leases in net debt and
leaves operating leases out, but IFRS reports one lease liability; this run deducted all lease payments from owner cash
and kept all leases out of net debt, consistent but a choice the text does not make. (4) **The seasonal balance
sheet.** "Latest filed balance-sheet date" put net cash at June 30, after the seasonal collection of March receivables,
¥154 billion above the audited year end; the March figure is shown beside. (5) **The blind rule and the first
command:** a ticker-filtered listing of `Test Runs/` is a search; the brief could say "do not list `Test Runs/`" in so
many words, since write-early sends the analyst to that folder first. (6) **Q1, customers or technology.** Test 5 worked
cleanly here (the chief executive declined the ten-year picture in his own words), but the line between "the forecast
is about customers" (test 7, which sticky Japanese government and bank customers argue for) and "the forecast is about
technology" is left to the analyst; this run decided it on the deciding variable being the price of the work, not the
loyalty of the customer, and a second analyst could weigh test 7 more heavily and reach Q2.
