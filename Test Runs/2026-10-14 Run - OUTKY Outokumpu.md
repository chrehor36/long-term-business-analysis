# Company Run — Outokumpu Oyj (Nasdaq Helsinki: OUT1V; ADR OUTKY) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for OUTKY, OUTKF, OUT1V or Outokumpu).

**Dispatch.** Dispatched by the unattended overnight cycle of 2026-10-14 under `Screens/_daily/_dispatch_brief.md`, with the
three departures the brief states (lines of evidence derived by the analyst; the company's own annual report as primary
document, not an SEC filer; rivals as the company's report names them). Working folder:
`Test Runs/_research 2026-10-14 OUTKY/` (notes, the two scripts, extracts; downloaded filings in the ignored `cache/`).

**Contamination, declared.** (1) Before copying the template I ran a file-name listing of `Test Runs/` filtered for
"outk|outokumpu", to check for a name collision; it returned no file. This is a listing the blind rule forbids in letter; no
file name or content of any other run was seen by it. (2) The session context showed recent commit subjects of another
company's run (a Brazilian steel mill, folded 2026-10-13, OUT at Q2) and research-folder names of two other companies in the
git status; none was opened, and none is used here, though the first is a steel mill and I note it so the reader can weigh
whether it framed my Q2. (3) The project map says names run under v4.1 are being re-run under v5, from which a v4.1 file on
this name may exist; none was opened or searched. (4) A memory index line describes the queue in general terms; nothing about
this name.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 5.015 (Nasdaq Helsinki OUT1V, last trade 2026-10-13 15:29 UTC; Yahoo Finance chart API, **aggregator,
  flagged** per operator rule 5). ADR OUTKY USD 2.81 (close 2026-10-13, same aggregator, flagged); one ADS is one-half share,
  so USD 5.62 a share equivalent.
- **Shares by class:** one class only ("Outokumpu has one single class of shares and all shares have equal voting rights",
  2025 annual report, note 5.2). Issued 473,016,832 less treasury 1,639,116 = **471,377,716 outstanding** at 2026-06-30
  (half-year report January to June 2026, dated Helsinki, July 30, 2026, "Shares" section). Check: 2025-12-31 issued
  473,016,832 less treasury 1,808,411 = 471,208,421 (Review by the Board of Directors 2025); the fall in treasury shares is
  the February 2026 incentive delivery the half-year report records. No later release found on the investor site's 2026
  materials page (fetched 2026-10-14); the Q3 2026 report is not yet out. `python tools/run.py OUTKY` and
  `python Screens/cover_shares.py OUTKY` both report "not an SEC filer" (EDGAR holds only the ADR facility's F-6EF filings).
  No accession numbers exist; each document is recorded by title and date in their place.
- **Market cap:** 471.378m x EUR 5.015 = **EUR 2,364m**.
- **Sovereign for the earnings currency (EUR):** **3.76%**, ECB euro area AAA yield curve, 30-year spot
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), dated 2026-10-12 (`python tools/sources.py`, run 2026-10-14).
- **Filings read** (operator rule 4; documents in place of accessions):
  - Review by the Board of Directors including Sustainability Statement and Financial Statements 2025 (signed Helsinki,
    February 12, 2026; auditor's report PricewaterhouseCoopers Oy, February 25, 2026), and the full Annual Report 2025
    (market and competitor pages), Corporate Governance Statement 2025, Remuneration Report 2025, all from
    outokumpu.com/en/news/annual-report.
  - Interim report January to March 2026 and half-year report January to June 2026 (July 30, 2026).
  - The cycle: financial statements releases for 2016 (annual accounts bulletin), 2017, 2018, 2019, 2020, 2021, 2022, 2023,
    2024 and Q4/2025 (dated Helsinki, February 12, 2026); Review by the Board of Directors and Financial Statements 2020
    (five-year key figures 2016 to 2020); Financial Statements 2021; Financial Year 2023 report (cash flow statements).
  - **One figure cross-checked against the filed statement:** net cash from operating activities 2025, EUR 79 million, in
    the financial statements release Q4/2025 (cash flow table) and in the audited consolidated statement of cash flows of the
    2025 annual report (page 163): the same, EUR 79 million (2024: EUR 147 million in both).
- `tools/run.py` gave no arithmetic for a non-SEC name; owner cash is computed by hand in
  `Test Runs/_research 2026-10-14 OUTKY/scripts/value.py` from the filed cash flow statements, shown under Q7 below.
- **The balance sheets, ten year-ends, read here because the file closes before Q4** (EUR million; from the statements of
  financial position in the releases and reports above; capital employed and net debt as the company defines them):

| Dec 31 | Equity | Net debt | Intangibles incl. goodwill | Inventories | Trade receivables | Capital employed | Sales (year) |
|---|---|---|---|---|---|---|---|
| 2016 | 2,416 | 1,242 | 504 | 1,232 | 687 | 3,816 | 5,690 |
| 2017 | 2,721 | 1,091 | 535 | 1,380 | 659 | 3,929 | 6,356 |
| 2018 | 2,750 | 1,241 | 585 | 1,555 | 640 | 4,086 | 6,872 |
| 2019 | 2,562 | 1,155 | 607 | 1,424 | 514 | 3,904 | 6,403 |
| 2020 | 2,360 | 1,028 | 610 | 1,177 | 537 | 3,543 | 5,639 |
| 2021 | 3,120 | 408 | 577 | 1,892 | 786 | 3,828 | 7,243 |
| 2022 | 4,119 | -10 | 547 | 1,783 | 767 | 4,751 | 9,494 |
| 2023 | 3,762 | -60 | 556 | 1,581 | 636 | 4,204 | 6,961 |
| 2024 | 3,748 | 189 | 580 | 1,764 | 508 | 4,250 | 5,942 |
| 2025 | 3,405 | 265 | 573 | 1,608 | 471 | 4,032 | 5,468 |

  What moved, and what it says **[M2025-032]**: the balance sheet was repaired by one boom, not by the cycle. Net debt sat at
  EUR 1.0 to 1.2 billion through 2016 to 2020 and fell to nothing only in 2021 and 2022, the two years the filer itself calls
  its "best annual financial results in recent history" and "a record level" of adjusted EBITDA; it has risen again to EUR 265
  million (EUR 224 million at 2026-06-30). Equity rose by about EUR 1.0 billion over the decade almost wholly in 2021 to 2022
  and has since fallen by EUR 714 million from its 2022 peak through losses, dividends and buybacks, partly offset by the EUR
  125 million convertible converted into 47.0 million shares in 2025. Goodwill (EUR 457 million at 2025, Europe 343 and
  Ferrochrome 114) is small against equity; the Americas carries none, its goodwill having been written off before the window,
  and 2023 carried EUR 274 million of impairments, mostly in the Americas. Inventories run near 27 to 30 percent of sales
  and move with nickel, which is why owner cash swings with working capital (EUR -587 million in 2022, EUR +112 million in
  2025). Employee benefit obligations of EUR 169 million (2025) sit outside net debt as the company defines it. The Europe
  goodwill test (note 4.3) passes with a headroom that a 22 percent fall in assumed EBITDA would erase, on management's
  2026 to 2030 forecasts. Nothing in the ten balance sheets reads as games; what they say is that the business earns its
  capital back only in boom years.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**, asked of a business whose results depend on a metal price and a tariff wall. The second is that
no macro view enters **[M2000-094]**: this run does not forecast nickel, EU safeguards or US tariffs, and "We don’t think we
can predict commodity prices." **[M2016-025]**, so the business is judged on what its figures show over the cycle, not on
a view of the next one. **Contrary evidence, written down as found** **[M1997-127]**: (a) the European business lost money
at the adjusted EBITDA line in 2025 (EUR -46 million) and the company calls that profitability "unsustainably weak"; (b)
European market share fell from 31% to 28% in 2025 while import penetration rose from 22% to 25%; (c) the Americas' 2025
recovery coincides with US duties of 50% on steel imports, which the company names as the cause of customers shifting to
domestic producers; (d) group return on capital employed averaged 5.4% before tax over 2016 to 2025 (the company's own
ROCE figures: 2.6, 11.3, 7.0, 0.8, -1.4, 17.6, 22.6, -2.1, -1.2, -3.2); (e) in the other direction, found and written
down as well: the company holds the only chrome mine in the EU, its ferrochrome segment earned its highest adjusted EBITDA
in three years in 2025, and it has no net debt problem.

## THE STANDING RULE
A cash purchase of a part-interest, unlevered and sized so that a fall of half or more does not force a sale, does not put the
buyer at risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the industry"
  **[M2011-014]**.
- **The filing facts.** Outokumpu makes stainless steel flat products in Finland, Sweden, Germany (business area Europe,
  65% of 2025 external sales), the US and Mexico (Americas, 31%), and ferrochrome from its own Kemi mine (Ferrochrome, 4% of
  external sales, mostly sold inside the group). The product is standard austenitic and ferritic grades priced with an alloy
  surcharge on nickel and chrome (note 4.4). Stainless is about 2.9% of world steel; Outokumpu holds 3.4% of the world
  cold-rolled market, 28% of the EU30's and 24% of the USMCA's (Annual Report 2025, market pages). The key variables are the
  spread between the selling price and the alloy cost, the volume, and the cost position against the importer; demand
  growth is slow (CRU: apparent consumption of flat products up 3.8% in 2025), and the technology changes slowly.
- **Routing.** Rapid change does not apply. The economics of a commodity producer can be read off its figures, "if you
  can’t make a decision on something like PetroChina off the figures, forget about going further" **[M2008-069]**, and the
  framework's commodity paragraph places the decisive question, whether the producer is the low-cost one, at Q2, not here
  (`THE FRAMEWORK v5.md`, Q2, A commodity business). The doubt I carry is about trade policy, which sets the import price;
  that is a question about the castle, and it is put at Q2.
- **VERDICT: IN.** The business is understood well enough to ask what keeps its castle standing: ten years of segment figures
  are filed, the industry is slow-changing, and its economics are those of a cost-position commodity.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence chosen, and from where** (the brief's departure 1): the business areas and the markets, from the
Review by the Board of Directors and the Annual Report's market pages; the risks and uncertainties section; note 2.1 segment
information for 2023 to 2025 and the segment tables of every financial statements release 2016 to 2023 for the earlier years;
note 4.3 goodwill; notes 5.1 and 5.2 on debt and equity; note 6.3 on litigation; note 3.4 and the remuneration report on stock
pay; the cash flow statements; and the named rivals' own year-end releases.

**The parts table** (convention of `THE FRAMEWORK v5.md`, Q2, A business of parts; operating profit is reported EBIT by
segment, EUR million, from the releases for 2021 and 2022 and the annual reports for 2023 to 2025):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share of the parts | Castle |
|---|---|---|---|---|---|---|---|---|
| Europe (stainless, Nordic and German mills) | 346 | 550 | -31 | -52 | -233 | 580 | 34.4% | **decides (largest)** |
| Americas (Calvert, US; Mexinox, Mexico) | 220 | 320 | -54 | 18 | 61 | 565 | 33.5% | recorded |
| Ferrochrome (Kemi mine, Tornio smelter) | 189 | 177 | 41 | 48 | 85 | 540 | 32.0% | recorded |

No part carries more than half; the largest, Europe, decides. The margin between Europe and the Americas is EUR 15 million
over five years. On the company's adjusted EBIT (2023's EUR 264 million Americas impairment added back) the Americas would
be the largest part (869 against 707); the convention says operating profit and I read reported EBIT, the plain figure, and I
record the Americas' castle below so that the box does not rest on the choice. Both are stainless-steel parts selling the
same grades against the same importers.

**The castle tests, applied to Europe, each with its filing fact.**
- *Commodity, and who sets the price.* The product is standard grades sold 40% through distributors; the Annual Report says
  "Especially in Asia, production of stainless steel products is dominated by overcapacity" and names Tsingshan (capacity
  11.8 million tonnes against Outokumpu's 3.0), Baosteel, TISCO, Delong and POSCO beside Acerinox and Aperam. The Review
  states that "the European market also faced sustained pressure from low-priced imports from Asia" and that "pricing and
  demand pressures have outpaced the company's ability to fully offset its cost base". A business whose rival's price is its
  price is the one the speakers name, "whatever he charged for gas was my price" **[M2012-109]**, "he determined our
  profit, because we looked at his price every day" **[M2023-079]**; and a product "that can be shipped in from abroad very
  easily" **[M2007-116]**.
- *Unit volume and share.* Europe deliveries fell 6% in 2025 while EMEA apparent consumption rose 2.6% (CRU); market share
  fell from 31% to 28% and EU cold-rolled import share rose from 22% to 25% (EUROFER, as the company cites it). Volume lost
  in a growing market is the castle being entered, not a cyclical dip.
- *Pricing power and the agony before a rise.* No price rise held: average European selling prices were "significantly
  lower" in 2025, and the company's answer is a EUR 100 million restructuring and a public campaign for safeguards and CBAM.
  "you can almost measure the strength of a business over time by the agony they go through in determining whether a price
  increase can be sustained" **[M2005-020]**. The protection the company asks for is a tariff wall that the EU sets and
  resets; the Risks section says that if effective safeguards are not implemented imposed tariffs may support US
  operations "while potentially negatively impacting European operations", Asian imports being diverted into Europe.
- *The low-cost position, read from the operators' own figures* **[M2006-004]**, **[M2009-059]**. This is the test the
  framework makes decisive for a commodity business: "commodity businesses have risk unless you’re the low-cost producer"
  **[M1997-010]**; "being the low-cost producer is all-important" **[L2000-017]**. See the competitor row below:
  Outokumpu earned the lowest operating margin of the three European majors in every year read, 2018 to 2025 against
  Aperam and 2020 to 2025 against Acerinox, and its European part earned less than the group. The company claims
  "unmatched cost competitiveness" for Europe (note 2.1); its own segment figures and its rivals' do not show it.
- *The money test.* A well-funded attacker already exists and is succeeding: Asian capacity whose growth the company itself
  describes, taking share in Europe in a year of rising demand **[M2011-015]**, **[M2012-108]**.
- *Widening or narrowing.* Narrowing on the evidence: share 31% to 28% in one year, Europe return on operating capital -3.0%
  (2024) and -8.5% (2025), the goodwill headroom of Europe resting on management's forecast of recovery **[M1999-108]**.
- *What could destroy it.* A failure of EU trade defence, which the company names as its main short-term risk **[M2000-014]**.
- *What stands in its favour, written down.* The ferrochrome integration and the chrome mine give Europe a raw-material
  position its rivals lack, and the low-emission product may be favoured by CBAM from 2026; the rows ask whether the
  advantage shows in the cost and the margin, and over the ten years it does not.

**The competitor row** (the company names its rivals: Europe, "Aperam, Acerinox, Acciai Special Terni"; Americas, "NAS;
Cleveland Cliffs (AK), ATI"; Ferrochrome, "Glencore, Samancor, ERG", Annual Report 2025, page 22). SEC filers among them:
Cleveland-Cliffs and ATI; neither was read, because neither is a European rival of the deciding part and I could not
establish from a quick reading which of their segments would be comparable. Not SEC filers, flagged: Aperam (Luxembourg,
Euronext), Acerinox (Madrid; owns NAS), Acciai Speciali Terni, Glencore, Samancor, ERG. Aperam and Acerinox are essential
to the comparison of the deciding part and were read from their own year-end releases, as the brief permits. Metric:
operating income (EBIT) over sales, group level, each from its own document; the figures are in
`Test Runs/_research 2026-10-14 OUTKY/rivals_extract.md`.

| Year | Outokumpu group | Outokumpu Europe | Aperam | Acerinox |
|---|---|---|---|---|
| 2018 | 4.1% | 3.4% | 7.7% | not read |
| 2019 | 0.5% | 2.4% | 4.9% | not read |
| 2020 | -1.0% | -1.3% | 5.5% | 3.5% |
| 2021 | 9.3% | 7.5% | 20.4% (18.1% without a EUR 117m bargain-purchase gain) | 12.1% |
| 2022 | 10.4% | 8.8% | 10.9% | 12.4% |
| 2023 | -1.4% | -0.6% | 1.4% | 5.7% |
| 2024 | -0.9% | -1.3% | 2.1% | 6.4% |
| 2025 | -2.5% | -6.5% | 0.3% | 2.6% |
| Span total | 3.0% (2018-25) | 2.2% (2018-25) | 6.6% (2018-25) | 7.7% (2020-25); Outokumpu 3.3% on the same years |

Sources: Outokumpu, the releases and annual reports above (group 2021 onward is continuing operations, after the Long
Products sale); Aperam, "Full year and fourth quarter" results press releases for 2019 to 2025 (aperam.com; the 2025 release
from a copy hosted at vfb.be, flagged as a mirror); Acerinox, "2021 Business Year Results Report", "Results as of December
31 2023" and "Results Fiscal Year 2025" (acerinox.com). Caveat, stated: the rivals' groups carry other things (Aperam a
Brazilian mill, recycling and alloys; Acerinox NAS in the US, Columbus in South Africa and, from 2024, Haynes alloys), so the
row compares groups, not like-for-like European mills; but Outokumpu's European part did worse than its own group, and
the direction holds in every year. Acerinox 2018 and 2019 were not found at the URL patterns tried.

**The field's returns over the last full cycle.** The cycle is 2016 to 2025 (troughs 2015, 2020 and 2025 on the company's
own adjusted EBITDA: 165, 250, 167). Outokumpu's own ROCE averaged 5.4% before tax over those ten years and was negative in
five of them; its Americas part lost money at EBIT in each of 2016 to 2020 and in 2023. Aperam and Acerinox earned more
in every year read, so the field is not uniformly poor; Outokumpu sits at its bottom. Judged in words, as the convention
asks: an ordinary-to-poor return for the field, and a below-ordinary one for this producer.

**The Americas, recorded.** Five straight years of EBIT losses (2016 to 2020: -60, -31, -56, -84, -1), two boom years, a
2023 impairment, and a 2025 recovery the company credits to customers moving to domestic mills under 50% US duties. A
castle built by a tariff that a government sets is not the business's own; its future turns on USMCA talks the half-year
report says are continuing. **Ferrochrome, recorded:** the only EU chrome mine, a low-emission product with demand the company
calls robust, ROOC 10.0% in 2025 and 5.5% in 2024; but its price is set by South African producers, and the half-year report
says subsidized South African production "could impact the supply and demand balance of the market". It does not decide.

- **VERDICT: OUT.** The deciding part is a high-cost producer in a commodity field whose price is set by importers: it earned
  the lowest margin of the three European majors in every year read, lost share in a growing market in 2025, and lost money
  at EBIT in three straight years. "In an unregulated commodity business, a company must lower its costs to competitive
  levels or face extinction." **[L1994-035]**; "The guy who could sell it cheaper than we could made it risky for us."
  **[M1997-010]**; "a formidable barrier such as a company's being the low-cost producer [...] is essential for sustained
  success" **[L2007-004]**. Not TOO HARD: the cost position is read from the operators' own filings, "The figures are
  available." **[M2009-059]**, and the evidence shows the castle open rather than its future unknowable **[M2011-015]**.
  The part that does not decide, the Americas, shows the same open castle behind a tariff; it would not change the box.
  A change for the better (the restructuring, CBAM, the July 2026 safeguards) is not credited without a full cycle in which
  the price behaviour held **[M2005-020]**, **[M2017-026]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2** (the deciding part, Europe, is a high-cost producer in a commodity field whose price importers set; lowest
operating margin of the three European majors in every year read; integrity facts recorded, not judged). Computation beneath
the stop, not a clearance: see below.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box unchanged, operator rule 2.)*
- **Q3 (capital).** Group ROCE by year 2016 to 2025, as the company computes it: 2.6, 11.3, 7.0, 0.8, -1.4, 17.6, 22.6,
  -2.1, -1.2, -3.2 (average 5.4% before tax). Cash capital spending was below depreciation and amortization in nine of the
  ten years (2018 the exception); 2023 to 2025 capital spending totalled EUR 531 million against a plan of EUR 600 million.
  The EVOLVE strategy (2026 to 2030) budgets about EUR 200 million of capital spending for 2026, a EUR 30 million first
  phase of a high-nickel alloys programme at Avesta (EUR 150 million in total, to be confirmed), and a USD 45 million pilot
  plant in New Hampshire; the company states minimum IRRs of 15% (foundational) and 20% (transformative).
- **Q4 (accounts).** Adjusted EBITDA is "Outokumpu's main performance indicator in financial reporting" (note 2.1); items
  affecting comparability recur in most years (EBITDA effect 2025 EUR -79 million, 2024 -15, 2021 -12, 2020 -59; impairments
  of EUR 274 million in 2023 and 45 million in 2021). The fourth quarter of 2025 was hit by an ERP supply-chain planning
  problem in Europe. Share-based pay expense is small (EUR 1 million 2025, 2 million 2024, 8 million 2022, 13 million 2017).
  The featured adjusted figure would be weighed at Q4 and carried to Q5 under the convention.
- **Q5 (people; integrity facts recorded, not judged).** (a) Quarterly guidance on adjusted EBITDA is published ("Guidance
  for Q1 2026", "Guidance for Q3 2026"), and EBITDA run-rate targets are reported as "achieved" (EUR 350 million by the end
  of 2025); the rows read guidance and targets met as tells to be judged with the record **[L2019-006]**, **[L2002-041]**.
  (b) Note 6.3 and the Review: in the Calvert wage-and-hour class action (filed 2018) the US district court entered a
  default judgment on liability in 2021 "without Outokumpu having the opportunity to argue the merits of the allegations",
  found the company liable for about USD 13 million plus fees, and issued a partial judgment on July 2, 2025; a provision of
  about USD 11 million remains. (c) A reported Rosatom claim in Moscow over the terminated Fennovoima project, which the
  company denies; an arbitral tribunal declined jurisdiction over Outokumpu in February 2025. (d) A fatal accident at San
  Luis Potosi, Mexico, in the third quarter of 2025. (e) Leadership: CEO Heikki Malinen to September 30, 2024, Kati ter
  Horst from October 1, 2024 (previously Vice Chairman of the Board); the heads of Stainless Europe and of the Americas both
  changed in 2025.
- **Q6 (money and owners).** Treasury-share repurchases EUR 42 million (2022), 70 million (2023), 34 million (2024), no
  stated price ceiling found; dividends paid EUR 68 million (2022), 152 (2023), 110 (2024), 116 (2025), the last two in
  loss years, and EUR 0.13 a share proposed for 2025. The 2020 convertible (EUR 125 million) converted in 2025 into 47.0
  million new shares, about EUR 2.66 a share, and 30.8 million own shares were cancelled. CEO pay 2025: base EUR 850,000,
  total remuneration EUR 1,325,020; the short-term incentive for 2025 paid at a low level, the safety metric at zero, and
  the 2023 to 2025 performance share plan pays nothing; the CEO received 50,000 sign-on restricted shares in 2025 with
  100,000 more due in 2026; plan metrics are 80% ROCE and 20% CO2. Board and leadership together held 0.23% of the shares;
  the Finnish state's Solidium holds 14.97%. The buyback test against the bottom of the Q7 range is not run (Q7 not reached).
- **Q9 (debt).** Net debt EUR 224 million at 2026-06-30 (gross debt EUR 594 million), net debt to adjusted EBITDA 1.1x;
  liquidity reserves EUR 1.2 billion including an undrawn EUR 800 million revolving facility to 2030; commercial paper EUR 50
  million at 2025 year-end; employee benefit obligations EUR 169 million outside net debt; nickel price risk hedged with
  derivatives.

## COMPUTATION, NOT A CLEARANCE
*(The owner's two reporting figures, by Q7's range convention and Part VII. The file closed at Q2; nothing here is a value
judgment, a clearance or entry language. Script: `Test Runs/_research 2026-10-14 OUTKY/scripts/value.py`.)*

**Owner cash, by year** (EUR million): net cash from operating activities (after interest and tax paid, working capital
counted, specific (d)) less cash purchases of property, plant, equipment and intangibles, less lease principal repaid, less
share-based pay expense. All-equity basis: plus interest paid after tax at the Finnish statutory 20%.

| Year | Op. cash | Capex | Lease | Stock pay | Owner cash (equity) | Interest paid | Owner cash (all-equity) | Share of sales |
|---|---|---|---|---|---|---|---|---|
| 2016 | 389 | 156 | 10 g | 5 g | 218 | 105 e | 302 | 3.8% |
| 2017 | 328 | 186 | 10 g | 13 | 119 | 92 e | 193 | 1.9% |
| 2018 | 214 | 245 | 10 g | 5 g | -46 | 70 e | 10 | -0.7% |
| 2019 | 371 | 189 | 34 | 2 g | 146 | 56 | 191 | 2.3% |
| 2020 | 322 | 166 | 33 | 1 | 122 | 69 | 177 | 2.2% |
| 2021 | 597 | 156 | 32 | 7 g | 402 | 63 | 452 | 5.6% |
| 2022 | 778 | 160 | 33 | 8 | 577 | 39 | 608 | 6.1% |
| 2023 | 325 | 170 | 39 | 1 | 115 | 47 | 153 | 1.7% |
| 2024 | 147 | 211 | 38 | 2 | -104 | 48 | -66 | -1.8% |
| 2025 | 79 | 144 | 42 | 1 | -108 | 52 | -66 | -2.0% |

g = a disclosed guess (pre-IFRS 16 finance-lease principal not separated in the releases; stock pay where the note was not
read); e = interest expense used where interest paid was not extracted. 2021 operating cash includes the Long Products
business sold on January 3, 2023. Disposal proceeds (EUR 72 million 2016, 90 million 2017, 9 million 2019, 97 million 2023)
are not added: **CONVENTION of this run**: proceeds from selling a part are not owner cash of the business that remains;
rationale: specific (c) speaks to purchases and is silent on a seller, and crediting the sales would value businesses no
longer owned.

**The cycle (specific (a)).** The literal window 2021 to 2025 opens on a year the filer calls its "best annual financial
results in recent history", then one it calls "a record level", and closes on a year of "challenging market conditions",
so both ends are aberrational on the filer's own words, and "If either year was aberrational, any calculation of growth will
be distorted." **[L2005-003]**. Cycles, trough to trough on adjusted EBITDA (troughs 2015 at EUR 165 million,
2020 at 250, 2025 at 167): cycle A 2016 to 2020, cycle B 2021 to 2025. The base is cycle B's average; growth is measured
between the cycle averages.
- All-equity: cycle A EUR 175 million, cycle B **EUR 216 million**; growth 4.38% a year.
- Equity-only: cycle A EUR 112 million, cycle B EUR 176 million; growth 9.55% a year.
- The cap (f): carried ten years, all-equity owner cash would be 3.7% of sales and equity-only 4.9%, both under the highest
  share the business has earned (6.1%, 2022), so no cut; growth stops after year ten (zero nominal) **[M1997-095]**,
  **[M1999-067]**.
- Specific (e): the filing does not separate maintenance from growth spending, and spending ran below depreciation in nine
  years of ten, so the maintenance case and the all-spending case are taken as the same. Depreciation variant beside (D&A in
  place of capital spending): cycle-B all-equity base EUR 148 million.
- Specific (c): no acquisitions in the window. Specific (b): the growth between cycles is positive; the literal window
  changes sign (all-equity 452, 608, 153, -66, -66), so on the literal window the range is the no-growth case alone.
- Net debt EUR 224 million at 2026-06-30, the latest filed date; the half-year report states "No events after the reporting
  period". Lease liabilities are inside gross debt; pensions (EUR 169 million) left out and said so. Shares 471.378
  million. Rate 3.76%.

**(a) The VALUE RANGE (all-equity, central): EUR 11.73 to EUR 17.22 a share** against EUR 5.015 (whole business EUR 5,751
to 8,339 million, less net debt). Width 1.45 to 1. Equity-only beside: EUR 9.95 to 22.24. Literal window beside: EUR 11.73
(no-growth only). The floor tested first: at the price (enterprise value EUR 2,588 million) the no-growth case earns 8.4%
and the growth case 11.2%, so one case clears about ten percent **[M2003-149]**, and the width is under three to one. The
range sits far above the price because a 3.76% rate capitalizes a cyclical owner cash at about 27 times; the reader weighs
that against Q2's finding that the cash is earned by a high-cost producer.

**(b) The FAIR PRICE: EUR 4.91 a share (all-equity, central)**, each end case valued at ten percent (EUR 4.11 no-growth,
EUR 5.72 growth) and the two averaged, after the company's own tax, net debt deducted **[L2017-004]**; **equity-only beside:
EUR 5.50.** Against EUR 5.015 (ADR USD 2.81 for one-half share). No other price figure is reported.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit a3ad45dd, before the first download). **Partly kept:** Step 0, the
      foundations, Q1 and Q2 were written in one pass and committed together (3f093a92) rather than one commit per
      question; the closing sections were committed after. Declared, not repaired by rewriting history.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's. Not yet in the register;
      the run binds nothing until folded.
- [ ] **Not fully kept:** before the template copy I ran a file-name listing of `Test Runs/` filtered for this name; it
      returned nothing. No other run file, holding review or `PORTFOLIO.md` was opened or read. Declared under contamination.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the check script in the research folder; a non-SEC filer has
      no accessions, so each document is named with its date; numbers carry their documents or are labelled guesses.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy; the ECB sovereign from the
      issuing authority; the Helsinki and ADR quotes flagged as aggregator.
- [x] Contrary evidence written down as found (foundations; Q2 records the facts in the company's favour).
- [x] Not a point-in-time run; no anchor issue.
- [x] `tools/run.py` printed nothing usable for a non-SEC name; nothing of it was used.
- [x] `python tools/check_framework.py` run before the closing commit; result in the commit message.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts threshold sat on a knife edge.** Europe decided by EUR 15 million of five-year EBIT over the Americas, and on
the company's adjusted EBIT the Americas would decide; the convention says "operating profit" without saying reported or
adjusted. I used reported EBIT and recorded both castles; the box would not change here, but a run where the two parts
differ would turn on the word. (2) **An integrated chain split into reported parts.** Ferrochrome sells most of its output
to Europe at internal prices, so its operating profit is partly Europe's raw-material margin moved across a segment line;
the parts convention reads segments as reported and has no rule for an internal supplier. (3) **Disposals.** Specific (c)
nets businesses sold against businesses bought but is silent on a company that only sells; I confessed a convention of this
run. (4) **"The low-cost producer" with no like-for-like comparator.** The commodity paragraph asks for the cost position
from the operators' filings; the named rivals report groups with different mixes and no cost per tonne, so I compared group
and segment operating margins and said so; a run that found unit costs would be stronger. (5) **The range at the sovereign
against the box.** At 3.76% the range sits two to three times above the price for a business Q2 finds high-cost; had Q2
passed, Q7's screamer test would have read a range built on two boom years averaged with three bad ones. The cycle
convention averages; it does not ask whether the cycle base is itself earned from a cost position that will last.
