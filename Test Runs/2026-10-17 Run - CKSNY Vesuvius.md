# Company Run — Vesuvius plc (LSE: VSVS; OTC ADR: CKSNY) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (2026-10-17): not held (`PORTFOLIO.md` does not name Vesuvius, VSVS or CKSNY).*

**Dispatch:** a blind analyst run under the overnight cycle's brief of 2026-10-17 15:16 (from `Screens/_daily/_dispatch_brief.md`; departures stated in the brief: lines of evidence derived by the analyst from the annual report, the primary document is the company's own annual report as no 10-K or 20-F exists, competitors taken from the company's own report).

**Contamination declared:** before the run file existed, a `ls "Test Runs" | grep 2026-10-1[5-7]` command used to check the date's naming showed the file names of ten other companies' run files dated 2026-10-15 and 2026-10-16 (FET, ACM, AER, AMMX, CTBG, ENYN, GATX, GBX, HMH, HRI). None was opened; none concerns Vesuvius; nothing from them is used. The git status and recent commit subjects in the session context name a run of another company (SUGP); not opened, not used. The tool `tools/run.py` printed only "not an SEC filer". No file about Vesuvius, VSVS, CKSNY or Cookson was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** 465.0 pence a share, London (LSE: VSVS) close 16 October 2026, the price of record. Source: Yahoo Finance chart
  series VSVS.L (an aggregator, flagged per operator rule 5); cross-check: a Form 8.5 (EPT/RI) filed on RNS (Investegate
  announcement 9828098) records dealings at 459.67p to 470.20p. The ADR: the F-6EF of 10 January 2013 (accession
  0001193805-13-000040) states each ADR represents "the right to receive one (1) ordinary share"; no ADR quote was taken.
  **The price is set by a pending possible offer** (see the takeover facts below): the close was 374.4p on 28 September 2026,
  the last day before the offer period, and 467.0p the next day (same aggregator series).
- **Shares:** 248,171,717 voting shares: 255,442,891 ordinary shares of 10p in issue less 7,271,174 in treasury, at close of
  business 28 September 2026 (Vesuvius RNS "Response to Media Speculation", 29 September 2026, Rule 2.9 paragraph). One class.
  `python Screens/cover_shares.py CKSNY` returns "NOT AN SEC REGISTRANT"; `python tools/run.py CKSNY` returns "not an SEC filer".
- **Market cap:** 248.171717m x 465.0p = **£1,154.0m**.
- **Sovereign for the earnings currency (pounds sterling):** **5.7225%**, Bank of England statistical database, series
  IUDLNPY (yield from British Government Securities, 20-year nominal par yield), 14 October 2026, the latest value published
  (`Test Runs/_research 2026-10-17 CKSNY/boe IUDLNPY IUDMNPY Sep-Oct 2026.csv`). The protocol's sovereign table has no GBP
  row; the Bank of England is the sterling issuing authority's central bank and 20 years is the longest par-yield series found
  in its database (no 30-year par series was found), so this is a departure, stated.
- **Filings read** (operator rule 4; Vesuvius files no 10-K or 20-F, so the documents are its own reports, by date in place of
  an accession): Annual Report and Financial Statements 2025 (signed 11 March 2026; report2025.vesuvius.com, full PDF);
  Annual Reports 2024, 2023, 2022 and 2021 (report2024 to report2021.vesuvius.com, full PDFs); the Group accounts for 2019 and
  2017 as filed at Companies House (company 08217766, filed 18 June 2020 and 3 July 2018; scanned images, read page by page for
  the income statements, cash flow statements and balance sheets of 2016 to 2019); Half Year Results for the six months to
  30 June 2026 (RNS, 30 July 2026); the Rule 2.4 announcements of 29 September 2026 by Vesuvius ("Response to Media
  Speculation") and by RHI Magnesita N.V. ("Statement re Possible Offer"), the RNS text read on Investegate below the site's AI
  summary, which is an aggregator's and is not used. No proxy statement exists; the Directors' Remuneration Report in the 2025
  annual report is its counterpart. Extracts of the three RNS texts are saved in the research folder.
- **One figure cross-checked:** net debt at 31 December 2025 of £452.4m in the filed 2025 statements (Note 35.15) equals the
  "31 December 2025: £452.4m" in the half-year RNS of 30 July 2026. Cash generated from operations 2025 of £173.4m in the
  Group Statement of Cash Flows (p.142) agrees with Note 11.
- **The lines of evidence chosen** (the counterparts of a 10-K's Items 1, 1A and 7): the strategic report (At a glance pp.4-7,
  Chairman p.8, Chief Executive's review pp.10-13, business model pp.14-15, principal risks pp.66-67, viability and going
  concern); the financial statements and notes (segment Note 4, cash generation Note 11, acquisitions Note 20, leases Note 26,
  contingent liabilities Note 32, APMs Note 35); the five-year divisional summaries of the 2025 and 2021 reports; the pricing
  passages of the 2021, 2022, 2024 and 2025 reviews; the remuneration report's buyback paragraph; the half-year RNS of 2026.
- **The takeover, as the documents state it.** Vesuvius: "since September 2025, it has received a series of unsolicited
  non-binding indicative proposals from RHI Magnesita N.V."; the first was a cash proposal at 448p on 29 September 2025; an
  all-cash 550p proposal of 17 March 2026 led the Board to grant "access to information to undertake confirmatory due
  diligence"; a 550p cash-and-share proposal of 23 June 2026 was "unanimously rejected" on 29 June; the latest, of 27 August
  2026, is "470 pence per ordinary share in cash; and 0.28 new RHI shares for every 10 Vesuvius shares", 551p on RHI's
  one-month VWAP; "The Board of Vesuvius is evaluating the Latest Proposal carefully". RHIM: headline value 549p on its
  28 September price, the cash "funded through new debt facilities", Cevian's irrevocable over 57,249,896 shares (about 23%),
  and the Rule 2.6(a) deadline of 5.00 pm on 27 October 2026. **No Rule 2.7 firm offer was found**: the Investegate VSVS
  announcement list read on 17 October 2026 (pages back to before 29 September) shows only Form 8 disclosures, holdings notices
  and PDMR notices after the two Rule 2.4 statements, and a web search found no firm offer, extension or withdrawal. How the
  framework treats the bid: it is a price, and a fact about one buyer's view; it is not a value (the foundations, below).
- `python tools/run.py` arithmetic lines: none (not an SEC filer). Owner cash is computed by hand from the filed cash flow
  statements in `Test Runs/_research 2026-10-17 CKSNY/owner_cash.py` (see the COMPUTATION after the stop).

**The balance sheets, ten of them, read here because the file closes before Q4** (£m, Group Balance Sheets as filed;
2016-2019 from the scanned Companies House accounts, 2018 as restated in the 2019 accounts; 2020-2025 from the 2021, 2023 and
2025 reports; 2024 from the 2025 report):

| 31 Dec | PPE | Intangibles (mostly goodwill) | Inventories | Trade and other receivables | Trade and other payables | Cash | Borrowings, current and non-current | Pension liabilities less surpluses | Equity to owners | NCI |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 323.6 | 781.9 | 207.7 | 394.1 | 239.7 | 144.4 | 464.7 | 29.4 | 1,056.4 | 42.1 |
| 2017 | 311.3 | 743.0 | 222.8 | 422.2 | 292.6 | 161.9 | 436.2 | 16.5 | 1,028.7 | 45.4 |
| 2018 | 303.7 | 724.0 | 244.3 | 440.4 | 311.8 | 236.9 | 484.9 | 15.3 | 1,090.7 | 50.0 |
| 2019 | 337.7 | 708.5 | 212.9 | 379.6 | 273.6 | 229.2 | 474.9 | 8.5 | 1,063.4 | 51.0 |
| 2020 | 337.5 | 696.1 | 187.3 | 369.9 | 288.7 | 209.7 | 378.1 | 2.1 | 1,079.4 | 51.4 |
| 2021 | 352.5 | 696.8 | 299.4 | 445.2 | 372.9 | 169.1 | 443.7 | 77.0 | 1,043.6 | 54.6 |
| 2022 | 417.6 | 737.5 | 316.0 | 476.9 | 378.4 | 184.2 | 441.9 | 56.1 | 1,260.2 | 59.4 |
| 2023 | 460.8 | 706.0 | 291.0 | 460.5 | 377.8 | 164.2 | 402.2 | 46.3 | 1,254.3 | 65.9 |
| 2024 | 482.6 | 690.9 | 295.4 | 438.9 | 363.4 | 186.4 | 520.2 | 37.4 | 1,168.4 | 75.2 |
| 2025 | 539.2 | 747.9 | 287.3 | 451.0 | 359.7 | 190.6 | 641.9 | 31.6 | 1,124.2 | 114.4 |

(Borrowings include IFRS 16 lease liabilities from 2019, £51.2m at 31 December 2025, Note 25. Pension column: employee
benefit liabilities less surpluses as printed.)

What moved and why, read before the income account **[M2025-032]**: equity to owners is where it was nine years earlier
(£1,056m in 2016, £1,124m in 2025) while the cash flow statements show dividends and buybacks paid in every year, so what was
retained has been paid out or absorbed, not compounded; intangibles, mostly goodwill from the 2008 Foseco purchase, are about
two thirds of equity in every year (goodwill £650.4m at 31 December 2025); PPE rose from £303.7m (2018) to £539.2m (2025)
while revenue was £1,798.0m in 2018 and £1,809.5m in 2025, so the added plant has not yet carried added sales; inventories
jumped £112m in 2021 (the filer: "investing in raw material inventory to mitigate some of the supply chain disruptions") and
have not gone back to the 2019-2020 level; borrowings rose from £402.2m (2023) to £641.9m (2025) as buybacks of £63.4m and
£34.8m and two acquisitions were paid while owner cash fell; non-controlling interests rose from £75.2m to £114.4m in 2025
because the Indian part of the MMS business was paid for with shares of the listed subsidiary Foseco India (Note 20: "issue
of 1,150,800 shares in Foseco India Limited (FIL) to the previous shareholders of Morganite Crucible (India) Limited (MCIL)
with a total value of £54.7m"). What the figures cannot say: the capital in Flow Control against Advanced Refractories, which
the filer does not report ("The Chief Operating Decision Maker does not review non-current assets and non-current liabilities
at a segmental level", Note 4.2).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-135]**: the question is what the refractory business will earn, not where the bid takes the
quote. The market serves, it does not instruct **[M2006-077]**: the 465p is a price set by a possible offer that carries "no
certainty" of being made; the bid "doesn’t tell us anything. It just tells us prices." **[M2006-077]**. Who is paid to tell
you **[M2020-037]**: the bidder's case rests on "significant synergies" and "meaningful earnings per share accretion" (RHIM,
29 September 2026), the projections of the party selling the deal, and the Board's rejections are an interested party's too.
**Contrary evidence, written down as found** **[M1997-127]**: (1) for the business: Flow Control and Foundry gained share in every
review read (2021, 2022, 2023, 2024, 2025) and in 2021 and 2023 did it while raising prices ("This ability to simultaneously
improve market share and prices in both Flow Control and Foundry", AR2023); the rival that knows the field best has made a
series of proposals over eleven months, the "which one would it be" answer **[M1999-130]** given in money; (2) against: owner cash averaged £47m a
year over 2021-2025 against trading profit averaging £182m; revenue was flat in pounds from 2018 to 2025; net pricing was
negative in 2025; the 12.5% return-on-sales target has not been met in any year 2017 to 2025; restructuring charges recur in
seven of the ten years 2016-2025; Advanced Refractories loses share when it prices and meets "imports from China" (half-year
RNS 2026); the bidder itself reports "available refractory capacity exceeding demand in all regions worldwide".

## THE STANDING RULE
Owning a part-interest bought for cash, with no borrowing and no size named, puts the buyer at no risk of ruin; "borrowed money
has no place in the investor's tool kit" **[L2014-005]**, and none is assumed **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test** **[M1995-051]**: "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" **[M2012-065]**. Vesuvius sells consumables: ceramic flow-control parts (isostatic tubes, stoppers and
  nozzles c.45% and slide-gate refractories and systems c.35% of Flow Control revenue of £750.9m), monolithic and shaped
  refractories (Advanced Refractories, £555.6m), sensors and probes (£36.1m), and foundry consumables under the Foseco brand
  (feeding and filtration, binders and coatings, crucibles; Foundry revenue £466.9m) (AR2025 pp.4-5). They are used up per
  tonne of steel cast or per casting poured; no customer exceeds 10% of revenue (Note 4.3).
- **The key variables** **[M1998-044]**: (1) steel production outside China and castings volume, which the filer reports from
  World Steel Association data in every review read; (2) share of the consumable spend, which the filer reports in words in
  every review ("gained market share"); (3) price net of raw-material and labour inflation, reported as "net pricing" in every
  review from 2021; (4) the cost base and the capital spending. All four are foreseeable in kind ten years out: steel and
  castings are made in the same continuous-casting and foundry processes the reports describe from 2017 to 2026, and the
  technology change named is slow (robotic handling of the same consumables; nine Flow Control robots shipped in 2025). The
  insiders write the forecast down (a 12.5% return-on-sales target and market outlooks in each report), so this is not an
  industry whose insiders "would say, “That’s too hard.”" **[M2000-105]**. The decision can be made "off the figures"
  **[M2008-069]**; what matters is "the economic dynamics of the industry" **[M2011-014]**, not the ceramics. A dependence on
  steel volumes and raw-material prices is not by itself a STOP here (Q2's commodity-business paragraph, **[M2016-025]**).
- **Routing:** not a fast-changing industry (no TOO HARD under **[M1998-008]**); not a bank; the two reported parts, Steel and
  Foundry, are each understood by the same tests.
- **VERDICT: IN.** The economics can be pictured ten years out from the filings; what they show is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question **[M1995-038]**: what keeps it standing, and does it protect "excellent returns on invested capital"
**[L2007-004]**?

- **The attacker with money** **[M2011-015]**, **[M2012-106]**. The field's largest player, RHI Magnesita (revenue €3,366m in
  2025), has bought into flow control rather than taken Vesuvius's place in it: its 2023 results describe an acquisition that
  "enables the Group to expand its flow control product range [...] in the Chinese domestic market", and since September
  2025 it has offered to buy Vesuvius outright. In Advanced Refractories the attacker is already inside: the half-year RNS of
  2026 reports "the challenging pricing environment in Europe for several Advanced Refractories products competing with
  imports from China", and the business is exiting Advanced Refractories in South Africa and manufacturing in South America.
  "one competitor is frequently enough to ruin a business" **[M2012-108]**.
- **Pricing power and the agony before a rise** **[M2005-020]**. The filer prices cost-plus, in both directions. 2021: price
  rises lagged cost, "a headwind of £14m in trading profit for the full year, although this headwind was fully eliminated by
  year-end as cost inflation was successfully passed through to customers" (AR2021), the pass-through that **[M2005-017]**
  credits to "businesses with strong competitive positions". 2024: "Headline pricing decreased slightly, reflecting a decline
  in raw materials costs" in Steel; in Foundry "Pricing net of cost inflation [...] was slightly negative as labour inflation
  was not fully compensated by price increases". 2025: "net pricing was -£11.5m"; in Steel "pricing net of cost inflation
  remained negative for the full year", positive again in H2 "reflecting, in particular, the technology leadership position
  of Flow Control". The price follows the input cost down as well as up; the margin is held, not widened.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. By part, the filer's own words split the answer.
  Flow Control and Foundry: "This ability to simultaneously improve market share and prices in both Flow Control and
  Foundry was again made possible by the technological differentiation of our products" (AR2023); share gains in every
  review read. Advanced Refractories: "lost market share in 2021 as priority was given very early in the year to pricing over
  volumes" (AR2021), "lost market share in 2023, particularly in Europe, as we gave priority to pricing" (AR2023), "market
  share losses at customers where we had historically given priority to pricing" (AR2024): when it prices, the customer takes
  the other bid, the mark of **[L2004-003]** and **[M2001-087]**. The principal risks name the same thing: "Cost pressures at
  customers leading to use of cheaper solutions" and "Commoditisation of product portfolio through lack of development"
  (AR2025 p.66).
- **Unit volume** **[M1999-054]**: revenue £1,798.0m in 2018 and £1,809.5m in 2025, with acquisitions in between; the volume
  is not growing in pounds across the cycle, and the filer ties it to steel production outside China, which it does not
  control.
- **The low-cost position** **[L2000-017]**, **[M1997-010]**: not claimed by the filer; its case is technology, not cost.
  For Advanced Refractories, the part that meets the low bid, no filing read states its cost against its rivals' **[M2006-004]**.
- **The brand in the customer's mind** **[M2023-073]**: Foseco is a brand in the Foundry trade; the Steel products are sold to
  steelmakers' engineers on performance, not by name to a consumer.
- **Ask the competitors** **[M1999-130]**: the rival's answer is in money: RHIM says the combination would create "a global
  leader in refractory and flow-control solutions" and has raised its proposal from 448p to 549p. The rows do not make this a
  pass; they say where the rival aims.
- **Widening or narrowing** **[M1999-108]**, **[M2000-075]**: the five-year divisional summaries (AR2021 and AR2025
  p.210) give return on sales by division: **Steel** 8.7% (2017), 10.4%, 10.0%, 7.3%, 8.7%, 11.5%, 10.5%, 11.4%, 8.9% (2025);
  **Foundry** 12.2% (2017), 12.3%, 11.9%, 6.1%, 8.6%, 9.9%, 10.0%, 7.4%, 6.7% (2025). Steel is where it was nine years ago;
  Foundry has narrowed by nearly half. The Group's own 12.5% return-on-sales target ("We continue to target a RoS of 12.5%",
  AR2025) was not reached in any year 2017 to 2025 (Group: 9.8%, 11.0%, 10.6%, 7.0%, 8.7%, 11.1%, 10.4%, 10.3%, 8.4%).
- **What could destroy, modify or reduce it** **[M2000-014]**: Chinese steel and refractory exports (the filer's and the
  rival's words); "available refractory capacity exceeding demand in all regions worldwide" (RHIM FY2025 results, 2 March
  2026); the customer's own margin squeeze.

**The competitor row.** The 2021 to 2025 annual reports name no competitor: a text sweep of all five for "competitor",
"RHI", "Magnesita", "Krosaki", "Shinagawa", "Imerys", "Calderys", "Saint-Gobain", "ASK Chemicals", "Huettenes"/"Hüttenes",
"Minerals Technologies" and "Refratechnik" found RHI Magnesita and Imerys only in directors' biographies and Morgan Advanced
Materials only as the seller of MMS. **CONVENTION of this run:** the rival read is RHI Magnesita N.V.; rationale: it is the
field's largest supplier by its own description ("the leading global supplier of high-grade refractory products"), it names
itself a flow-control rival in its 2023 results and in its offer, and it is the only one whose filings were reachable today.
**RHI Magnesita does not file with the SEC**; it was read from its own results announcements on the FCA National Storage
Mechanism (FY2022 results, RNS 4685982; FY2023, RNS 5084218; FY2025, 2 March 2026, NSM artefact 286c60fc). A second rival
(Krosaki Harima, Tokyo) was not read; flagged under what could not be got.

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Vesuvius return on sales (trading profit / revenue) | 8.7% | 11.1% | 10.4% | 10.3% | 8.4% |
| RHIM Adjusted EBITA margin | 11.0% | 11.6% | 11.4% | 11.7% | 11.1% |
| Vesuvius ROIC, the company's own, after tax, all invested capital | n/r | n/r | n/r | 8.4% | 6.3% |
| Vesuvius ROIC excluding Foseco goodwill and intangibles (company's own) | n/r | n/r | 15.8% | 14.4% | 10.5% |
| RHIM ROIC (NOPAT / invested capital, company's own) | 9.6% | 11.6% (12.3% on the 2023 definition) | 10.7% | 10.4% | 9.5% |

(n/r: not read on a comparable definition; the ROIC definition was changed in March 2025, Note 35.17.) Over the five years
the two companies earn the same thing within a point or two: about ten to twelve percent on sales and about ten percent after
tax on the capital invested, in a field whose largest player reports capacity above demand everywhere.

**The parts table** (the filer reports trading profit for two parts with different economics; Note 4 and the five-year
summaries; five years 2021 to 2025):

| Part | Trading profit 2021-2025, £m | Share | Castle | Decides |
|---|---|---|---|---|
| Steel (Flow Control, Advanced Refractories, Sensors & Probes) | 695.3 | 76.5% | Flow Control: technology-led, gains share while pricing. Advanced Refractories (41% of Steel revenue in 2025): loses share when it prices, meets Chinese imports. Steel's margin unchanged over nine years | **Yes** (more than half) |
| Foundry (Foseco) | 213.8 | 23.5% | brand and technology, share gains, but margin from 12.2% (2017) to 6.7% (2025) | No |

Inside Steel the filer reports revenue but not profit or capital for Flow Control and Advanced Refractories, so the deciding
part is Steel as reported **[L2008-005]**.

**The field's returns over the last full cycle, judged in words.** On its tangible operating capital (PPE plus inventories
and receivables less payables, year-end balances) Vesuvius's trading profit is a good pre-tax figure, 22.7% in aggregate over
2016-2025 (16.5% to 29.1% by year; `tangible_return.py`), before the restructuring charges that recur in seven of the ten
years. But the return does not come out as cash: owner cash after every real cost averaged about £70m a year over 2018-2025
and £47m over 2021-2025 (all-equity basis, before purchases) on tangible capital that grew from £677m to £918m, a cash return
of roughly five to nine percent on the capital the business needs; it "reports the 12 percent on capital but there’s never any
cash" **[M2003-122]**. On all the capital an owner has paid for, the company's own after-tax ROIC is 6.3% (2025) and 8.4%
(2024), and the rival's is 9.5% to 12.3% over five years. That is an ordinary return, and the field is one where "you can have
only two competitors and they’re still terrible businesses" **[M2013-052]** is the risk the rival itself describes (excess
capacity, Chinese exports). The castle is standing: Vesuvius has kept its share in Flow Control and Foundry for years, and the
rival would rather buy it than attack it. What it protects is a margin of about ten percent on sales and an ordinary return on
the owner's capital, held by cost-plus pricing that gives the input-cost changes back to the customer, with half the deciding
part showing the commodity marks. No full cycle shows a change for the better: Steel's margin was 8.7% in 2017 and 8.9% in
2025.

- **VERDICT: OUT.** The standing castle that protects only ordinary returns (Q2, What it rules OUT, the "ordinary" CONVENTION
  of 2026-10-06, judged in words): the deciding part, Steel, has earned about ten percent on sales across 2017-2025 with no
  widening, its cash return on the capital it needs is ordinary, and the field's largest rival earns the same ordinary return
  in a market it says has capacity above demand in every region **[L2007-004]**, **[M2013-052]**, **[M2003-122]**. Not TOO HARD:
  the tenuous-moat row sends a castle to TOO HARD because "We don’t know how to valuate that" **[M2000-019]**, and here what the
  castle protects is known from the filer's and the rival's own figures. A lower price does not reopen it **[M2019-015]**.

**Q3 to Q12: NOT REACHED** (operator rule 2). Q11 belongs to the holding review.

---
## THE BOX
**OUT at Q2** (the standing castle that protects only ordinary returns), integrity facts recorded, not judged. For the
operator, COMPUTATION, NOT A CLEARANCE (below): value range 131p to 403p a share (all-equity basis, at the sovereign) against
465p, a price held up by RHIM's possible offer at 549p to 551p, for which no Rule 2.7 firm offer had been announced by
17 October 2026.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).

- **Q3 (capital in).** Net capital spending exceeded depreciation and amortisation in every year 2022-2025 (£86.1m, £87.2m,
  £96.1m, £79.8m against £55.5m, £57.8m, £62.2m, £65.8m; cash flow statements and Note 11); the 2025 review: "c. £100m growth
  capex programme concluded in 2025", 2026 capex first "expected to be in the range of £70m-75m", then "£75-80m" (half-year
  RNS). PPE rose by £236m from 2018 to 2025 with revenue flat. Pre-tax trading profit on tangible operating capital 16.5% to
  29.1% by year, 22.7% over ten years; owner cash on the same capital roughly five to nine percent.
- **Q4 (the numbers).** The figure featured is "Trading profit (adjusted operating profit)", before "separately reported items"
  that recur: restructuring charges of £28.5m (2016), £36.3m (2017), £15.3m (2018), £39.8m (2019), £6.1m (2020), cost-reduction
  programme expenses £14.6m (2024) and £18.9m (2025), £16.4m in H1 2026, plus a water-treatment provision at a disused mine
  (£9.7m, 2024) and acquisition costs (£7.0m, 2025). In H1 2026 the trading losses of businesses being exited (South Africa,
  South America, part of the US) were moved out of trading profit as separately reported (£-2.8m). Statutory operating profit
  H1 2026 £47.4m against trading profit £74.0m. Bonuses are paid partly on adjusted EPS, cash conversion and ROIC (Note 35).
  The rows on these: **[L2016-006]**, **[L2016-007]**, **[L1998-031]** (to be weighed at Q4 and carried to Q5 by a run that
  reaches them). Cash conversion (adjusted operating cash flow / trading profit) 69% in 2024 and 75% in 2025.
- **Q5 (integrity facts, recorded, not judged).** (1) "In March 2025, the Board re-defined ROIC for the purpose of
  remuneration targets, to exclude the impact of goodwill and intangibles that arose on the acquisition of Foseco in 2008"
  (Note 35.17): on the old basis ROIC was 6.3% in 2025 and 8.4% in 2024; on the new basis 10.5% and 14.4%. (2) The adjusted
  figure is featured in the highlights, the KPIs and the bonus targets, with recurring restructuring outside it (Q4 above).
  (3) The buyback's stated purpose (below). (4) The Board rejected 448p to 550p proposals and is "evaluating" 549p to 551p;
  the largest holder (about 23%) has already undertaken to accept. No investigation, litigation or contingent liability of
  note found: Note 32 refers only to guarantees by the Company on behalf of the Group.
- **Q6 (the money and the owners).** Buybacks: £63.4m (2024) and £34.8m (2025); the second £50m programme bought 12,220,715
  shares, 8,550,527 of them in 2025 ("The average price paid for the shares purchased in 2025 was £4.03 per share"); its stated reason: "it would send a
  positive public signal that the Company was performing well" (Directors' Remuneration Report section, AR2025), the motive
  **[L1999-028]** names; no price limit stated. Against the COMPUTATION range below, 403p sits at the top of the range
  (403p), not at or below its bottom (131p); the line Q6 owes to Q7 would read: the prices paid sit above the bottom of the
  range. Dividends to owners £61.1m (2024) and £57.9m (2025) against owner cash on the equity basis of £25.8m and £5.4m in
  those years, so dividends and buybacks were paid partly with borrowings (borrowings £402.2m to £641.9m, 2023-2025). Deals:
  PiroMET (61.65%, Turkey) for £21.9m cash, February 2025; MMS from Morgan Advanced Materials for £75.2m, of which £20.5m cash
  and £54.7m in new shares of the listed subsidiary Foseco India, November 2025, goodwill £34.7m on provisional values.
- **Q9 (debt and exposures).** Net debt £452.4m at 31 December 2025 (2.1x adjusted EBITDA; 2.0x pro forma), £429.6m at
  30 June 2026; covenants net debt/EBITDA below 3.25x and interest cover of at least 4x, the viability test showing a breach only
  on "an unforeseen reduction in revenue of greater than 17%"; liquidity £386.1m; pension liabilities less surpluses £31.6m
  (the UK plan bought in with Pension Insurance Corporation in November 2021). "little or no debt" **[R1997-001]** is a
  whole-business criterion, not applied here.
- **Q12.** No named business of the rows. Nothing found.

## COMPUTATION, NOT A CLEARANCE (the operator's two reporting figures; Q7's construction applied after the stop)
Scripts: `Test Runs/_research 2026-10-17 CKSNY/owner_cash.py` and `value.py`. Figures in £m unless stated.

**Owner cash after every real cost**, by year, from the filed cash flow statements: cash generated from operations, less
interest paid plus interest received, less tax paid, less purchases of PPE and intangibles plus disposal proceeds, less lease
principal, less the share-based payment charge (Note 28; equity-settled and not added back on its own line in Note 11), plus
dividends from joint ventures, less the non-controlling interests' share of profit after tax (**CONVENTION of this run**:
the minority holders own that share of the cash, chiefly in the listed Indian subsidiaries, and their dividends paid, £1.7m to
£3.2m, understate it). The all-equity figure adds back net interest less 25% tax (the UK statutory rate). 2016-2018 are
pre-IFRS 16 (lease cost inside operating cash); the 2019 lease principal (£12.0m) and the 2016-2019 share pay (£3.0m a year)
are guesses, disclosed as such, because those lines were not read.

| Year | Trading profit | Owner cash, equity basis | Owner cash, all-equity basis | Acquisitions, cash | All-equity after acquisitions |
|---|---|---|---|---|---|
| 2016 | 133.3 | 46.9 | 56.0 | 7.7 | 48.3 |
| 2017 | 165.5 | 80.6 | 89.7 | 0.0 | 89.7 |
| 2018 | 197.2 | 94.7 | 103.3 | 1.0 | 102.3 |
| 2019 | 181.4 | 103.1 | 112.2 | 25.9 | 86.3 |
| 2020 | 101.4 | 96.0 | 106.3 | 1.4 | 104.9 |
| 2021 | 142.4 | -19.6 | -13.9 | 43.7 | -57.6 |
| 2022 | 227.2 | 99.2 | 106.2 | 3.5 | 102.7 |
| 2023 | 200.4 | 86.7 | 88.7 | 0.0 | 88.7 |
| 2024 | 188.0 | 25.8 | 37.0 | 0.0 | 37.0 |
| 2025 | 151.1 | 5.4 | 18.9 | 38.9 | -20.0 |

Averages: window 2021-2025, all-equity 47.4 before acquisitions, 30.2 after; cycle 2018-2025, 69.8 before, 55.5 after.
2025 cross-check against the filer's own "Free cash flow" of £36.0m: owner cash on the equity basis is £5.4m after the lease
principal (£16.7m), share pay (£3.0m) and the minority share (£12.6m less the £1.7m paid, already inside the filer's figure).

**The range, by Q7's convention in full.**
- (a) **Cycle base.** The first window year, 2021, is aberrational on the filer's own description (the £113.5m inventory build,
  "investing in raw material inventory to mitigate some of the supply chain disruptions"), and the last, 2025, is a trough
  ("2025 was a challenging year", "extended weakness in our end-markets"). The base is the average over 2018-2025, peak (2018)
  to trough (2020) to peak (2022) to trough (2025) (**CONVENTION of this run** for the choice of years: the rows give no rule for
  a cycle that ends in a trough). The literal window is shown beside.
- (b) **Decline.** Growth between the halves of the cycle (after acquisitions): 2018-2021 average 59.0, 2022-2025 average 52.1,
  -3.1% a year; carried as the bottom. The literal window changes sign (2021 negative), so its halves are used beside: 2021-22
  average 22.5, 2024-25 average 8.5.
- (c) **Acquisitions.** Purchases averaged 14.3 a year over 2018-2025, under half of owner cash before purchases (69.8), so not
  the serial acquirer; default pair, purchases deducted with the total growth credited. After year ten purchases stop. MMS
  (closed 12 November 2025) is in the window for seven weeks only; its full-year earnings are not filed separately and are
  credited at nothing; its £20.5m cash is in 2025's purchases; its £54.7m paid in subsidiary shares is in the minority's
  higher share. No deal signed and unclosed.
- (d) **Working capital** is inside cash generated from operations in every year, including the 2021 build.
- (e) **Maintenance case.** The filer gives "c. £100m growth capex programme concluded in 2025" and calls 2026's lower capex a
  return "to a normalised level". **CONVENTION of this run:** the £100m spread evenly over 2022-2025 (£25m a year; the filer
  gives the total, not the years), added back for the maintenance-only case: 12.5 a year on the eight-year cycle base, 69.8 +
  12.5 = 82.3. The growth that spending bought is not visible (revenue flat), so by (e) the maintenance-only no-growth case is
  the top of the range and the declining case the bottom.
- (f) **The cap**: no growth is carried above zero, so no cap binds.
- **Net debt** for the all-equity basis: £429.6m at 30 June 2026 (half-year RNS), plus the 2025 final dividend of 16.5p paid
  6 July 2026 (£40.9m) and the 2026 interim of 7.1p paid 8 October 2026 (£17.6m), both stated in the filer's announcements,
  less IFRS 16 lease liabilities of £51.2m (31 December 2025, Note 25; lease payments are already charged in owner cash):
  **£437.0m**. Pension deficit (£31.6m) left out and said so.

| Case | Owner cash base | Growth | Value at 5.7225% (EV) | Per share | Value at 10% (EV) | Per share |
|---|---|---|---|---|---|---|
| **Top**: maintenance-only, no growth, cycle base before purchases | 82.3 | 0% | 1,438.2 | **403p** | 823.0 | 156p |
| All spending, no growth, cycle base before purchases (beside) | 69.8 | 0% | 1,219.7 | 315p | 698.0 | 105p |
| **Bottom**: cycle base after purchases, declining | 55.5 | -3.1% for ten years, then flat | 763.2 | **131p** | 452.6 | 6p |
| Literal window 2021-2025 after purchases, no growth (beside) | 30.2 | 0% | 527.7 | 37p | 302.0 | -54p |
| Literal window, declining at its halves rate (beside) | 30.2 | -27.7% | 75.6 | -146p | 61.6 | -151p |

- **(a) VALUE RANGE: 131p to 403p a share** (all-equity basis, at the sovereign), against **465p**. The literal window beside:
  37p and below.
- **The floor, tested first:** at 465p the market value plus net debt is £1,591.0m; the top case's owner cash of 82.3 is a
  5.2% return on it at no growth, and every other case is lower. No case earns the floor of about ten percent **[M2003-149]**:
  were the file open, Q7 would close OUT on the floor, before the width (3.07 to one per share, 1.88 to one on enterprise
  value). The owner cash the price would need at no growth to earn ten percent on £1,591.0m is £159.1m a year, more than
  twice the best year in the ten (£112.2m, 2019).
- **(b) FAIR PRICE: 81p a share** on the all-equity basis (each end case valued at ten percent, 156p and 6p, averaged).
  **Equity-only figure beside: 226p** (owner cash after interest: top 61.4 + 12.5 at no growth, bottom 61.4 less 14.3 of
  purchases declining at 3.1%, each at ten percent, averaged; no net debt deducted). The central figure is the all-equity
  one; the two differ because net debt of £437.0m costs about £43.7m a year at ten percent against about £12m of interest
  after tax actually paid. Tax: owner cash is after the company's own tax as paid; no carryforward was examined. No other
  price figure is reported.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 144c1ac9); written question by question; committed after each
      (c081df46 Step 0 to Q1, 82ba8390 Q2, then this close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      only once folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched for this company. Contamination
      declared at the top: one directory listing of `Test Runs/` filtered to 2026-10-15 to 2026-10-17 showed ten other
      companies' run-file names (not opened, not used), and the session context showed another company's commit subjects.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the check script in the research folder; every filing fact
      carries its document and date (no accession numbers exist for UK filings; the ADR's F-6EF accession is given).
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the figures after it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy; the sovereign from the Bank of
      England (no GBP row in the protocol's table, said so); the price from an aggregator, flagged, and cross-checked against a
      Form 8.5 dealing range.
- [x] Contrary evidence written down as found (THE FOUNDATIONS); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` printed only "not an SEC filer"; nothing of it used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).
- Honest gaps: the 2016-2019 lease and share-pay lines are guesses; the 2020-2021 lease principal is taken from Note 26's
  cash payments less lease interest; Krosaki Harima not read; RHIM read for 2021-2025 only, not over 2017-2020; the Steel
  part's capital is not reported, so its return on capital is inferred from the Group's.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q2's "standing castle that protects only ordinary returns" does not say on what the return is read: on reported profit
against tangible capital Vesuvius earns a good pre-tax 22.7% over ten years, while its owner cash on the same capital is five
to nine percent and its own ROIC on all invested capital 6.3% to 8.4%; the rows put the moat's object as "excellent returns on
invested capital" **[L2007-004]** and Q3 measures on "the capital actually needed", so a run can close OUT or pass on the same
facts depending on which return it reads. This run read both and decided on the cash return and the rival's comparable figure,
and says so; a sentence in Q2 naming the measure would settle it. (2) The parts paragraph decides on reported parts, but the
filer reports profit only for Steel as a whole, while its own words show two different castles inside Steel (Flow Control
gaining share while pricing, Advanced Refractories losing share whenever it prices); the convention has no rule for a reported
part that mixes a castle and a commodity, so the run decided on Steel as reported. (3) The protocol's sovereign table has no
GBP row and the Bank of England's longest par-yield series found is 20 years; the run used it and said so. (4) Q7(a) gives no
rule for a cycle whose last year is a trough; the base years 2018-2025 are this run's choice. (5) Q7(c) classes a deal by the
larger part of what was paid in the buyer's own shares; MMS was paid mostly in new shares of a listed subsidiary, not of the
buyer, which the text does not cover; treated here as an acquisition with the minority's share counted. (6) A price lifted by
a pending possible offer is not addressed anywhere in the framework; the run treated it as the price of record and the bid as
a fact about one buyer's view (the foundations), not as value.
