# Company Run — OSI Systems, Inc. (NASDAQ: OSIS) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The brief's blind rule forbids opening `PORTFOLIO.md`, so
whether the operator holds OSIS is unknown to this analyst. The run is written as a purchase run of record.

**CONTAMINATION, declared.** (1) The directory listing of `Test Runs/` and the git commit subjects showed the names and,
for some, the boxes of other 2026-10-05 runs and research passes (MBUU, BN, HRB, SONY, TBTC, holding reviews); none is
about OSIS and none was opened. (2) The analyst came to the name knowing in outline of the December 2017 short-seller
report, the 2012 to 2013 TSA show-cause matter and the Mexico contracts; every such fact used below was re-found in a
filing and carries its accession. (3) `tools/run.py` printed v4 material; only its arithmetic lines were read.

Working folder: `Test Runs/_research 2026-10-05 OSIS/` (filings as text, `valuation.py` and its output, the ledger rows
cited, the Smiths Group results PDFs, the peer filings in `peers/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $197.93 (2026-10-05, live quote printed by `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common, 15,941,968 shares (10-K for FY ended 2026-06-30,
  filed 2026-08-21, accession `0001104659-26-099752`; `python Screens/cover_shares.py OSIS`). No second class; preferred
  authorized, none issued.
- **Market cap:** $197.93 × 15.942M = **$3,155M**. Convertible notes: $350M 2.25% due 2029 (conversion price about
  $191.98, so at today's price about 0.06M net shares would issue on net-share settlement) and $575M 0.50% due 2031
  (conversion price about $353.82, out of the money). Same 10-K, Note 8.
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2026 (2026-08-21, `0001104659-26-099752`): business, risk factors, MD&A,
  statements, Notes 1, 5, 8, 11, 12, 14. 10-K FY2025 (`0001410578-25-001887`), FY2024 (`0001410578-24-001571`), FY2023
  (`0001104659-23-096477`), FY2022 (`0001104659-22-092999`), FY2021 (`0001104659-21-108619`), FY2020
  (`0001104659-20-097650`), FY2019 (`0001047469-19-004853`), FY2018 (`0001047469-18-005819`), FY2017
  (`0001047469-17-005596`), FY2016 (`0001047469-16-015059`): segment notes, legal proceedings notes, concentration notes.
  10-Qs: March 2026 (`0001104659-26-055014`), December 2025 (`0001104659-26-008109`), September 2025
  (`0001104659-25-104478`), and the FY2022 three (`0001104659-21-131824`, `0001104659-22-009019`,
  `0001104659-22-053645`) for the class-action settlement. Proxy: DEF 14A filed 2025-10-22 (`0001104659-25-101517`),
  downloaded, **not read** (Q5 and Q6 not reached). 8-Ks of 2025-11-17/20 (the 2031 notes) and 2026-08-20 (results)
  downloaded. No 10-Q after the FY2026 10-K exists yet (Q1 FY2027 ends 2026-09-30).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2026 **$275,904
  thousand** in the filed consolidated statement of cash flows (F-9, `0001104659-26-099752`) equals the XBRL value and the
  `tools/run.py` line (276). Also: accounts receivable, net $764,626 thousand at 2026-06-30, balance sheet F-6, equals
  `run.py`'s 765.
- **`tools/run.py OSIS` arithmetic lines, checked against the filing:** share count 15.9M matches the cover. OCF lines
  match the statements; no securities purchases sit in OCF (investing shows only certificate-of-deposit maturities).
  `run.py` does **not** deduct "payments for intangible and other assets" ($16.4M to $18.0M a year, FY2023 to FY2026),
  which this run treats as capital spending. `run.py`'s debt column shows non-current debt only; the FY2024 bank line
  of $384M and FY2025's $178M are missing from it. Stock pay is complete in the statements (FY2026 $26.4M).

### Owner cash after every real cost, by year (USD M; OCF − stock pay − capex − payments for intangible and other assets)
| FY | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| OCF | 62.8 | 133.1 | 119.1 | 129.2 | 139.1 | 63.8 | 94.8 | −87.5 | 97.6 | 275.9 |
| Stock pay | 26.1 | 23.8 | 25.3 | 23.8 | 26.8 | 28.1 | 29.1 | 28.7 | 32.0 | 26.4 |
| Capex | 17.1 | 43.2 | 27.4 | 21.1 | 16.9 | 14.9 | 15.8 | 22.1 | 23.8 | 30.6 |
| Intangible and other assets | 5.1 | 2.5 | 2.8 | 13.4 | 13.8 | 15.6 | 16.4 | 17.3 | 17.7 | 18.0 |
| **Owner cash** | 14.5 | 63.6 | 63.6 | 70.9 | 81.6 | 5.2 | 33.5 | **−155.6** | 24.1 | 200.9 |
| Net income | 21.1 | −29.1 | 64.8 | 75.3 | 74.0 | 115.3 | 91.8 | 128.2 | 149.6 | 154.7 |
| D&A | 68.2 | 69.8 | 56.2 | 49.8 | 43.9 | 38.7 | 38.5 | 42.2 | 43.6 | 42.6 |

Five-year average owner cash (FY2022 to FY2026): **$21.6M**; ten-year average **$40.2M**. Depreciation variant (net income
+ D&A − capex − intangible and other assets, working capital left out): five-year average **$130.6M**. The two differ
because receivables absorbed $293.6M in FY2024 and $164.7M in FY2025 (cash-flow statement, `0001104659-26-099752`).
Sources: the filed cash-flow statements of the 10-Ks listed above; XBRL used for transcription only. Taxes paid on
net-share settlement of equity awards ($36.4M in FY2026) sit in financing and are not deducted again: stock pay is
already deducted at its expense.

### The balance sheets, ten years, read before the income account **[M2025-032]**
| June 30, USD M | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue (for scale) | 961 | 1,089 | 1,182 | 1,166 | 1,147 | 1,183 | 1,278 | 1,539 | 1,713 | 1,786 |
| Receivables, net | 207 | 211 | 238 | 270 | 291 | 308 | 381 | 648 | 838 | 765 |
| of which unbilled | n/a | n/a | 19 | 43 | 41 | 43 | 87 | **339** | 243 | 191 |
| Receivables / revenue | 21% | 19% | 20% | 23% | 25% | 26% | 30% | 42% | **49%** | 43% |
| Inventory | 249 | 314 | 274 | 241 | 294 | 334 | 338 | 398 | 407 | 416 |
| Cash | 170 | 85 | 96 | 76 | 81 | 64 | 77 | 95 | 106 | 360 |
| Goodwill + intangibles | 361 | 434 | 440 | 439 | 448 | 475 | 490 | 491 | 571 | 599 |
| Bank lines + all term debt | 347 | 364 | 347 | 327 | 277 | 353 | 360 | 522 | 650 | 1,001 |
| Equity | 569 | 489 | 552 | 572 | 640 | 638 | 726 | 863 | 951 | 833 |
| Retained earnings | 364 | 335 | 400 | 475 | 549 | 664 | 736 | 861 | 942 | 852 |

(Unbilled from the contract-asset notes of each 10-K; debt from the balance sheets and Note 8; FY2017 to FY2020 debt
includes the 1.25% notes due 2022.)

**What the figures are saying.** (1) **Receivables are the story.** For six years they ran at 19% to 26% of revenue. In
FY2024 they jumped to 42% and in FY2025 to 49%, while unbilled revenue (revenue recognised before the contract gave the
right to invoice) went from $43M to $339M in two years. In the same two years Mexico revenue went from $23M to $423M
(geographic note, FY2026 10-K), two Security customers were 16% and 11% of revenue and 39% and 10% of receivables
(FY2024 10-K, Note 1), and operating cash was −$87.5M. This is the pattern the rows tell the reader to look twice at:
"inventories look out of line, you know, with sales" **[M1995-064]**, here receivables. (2) **The cash then came.**
FY2026 operating cash was $275.9M with receivables down $98.7M; the single largest customer fell from 42% of receivables
(about $352M) to 25% (about $191M); unbilled fell to $191M. The filer attributes the cash to "collections on large
Security projects". So the balance sheet shows revenue booked ahead of cash on one government's contracts, and then
mostly collected; it does not show revenue that never turned to cash. About $191M still sits with one customer.
(3) **Equity was bought back with borrowed money.** FY2025 and FY2026 buybacks were $80.4M and $271.9M (FY2026 at
$267.03 and $218.82 average prices); debt went from $360M (FY2023) to $1,001M (FY2026) through two convertible issues;
equity fell $118M in FY2026 while net income was $154.7M. Net debt at 2026-06-30: $641M. (4) **Goodwill and
intangibles** rose from $361M to $599M through small acquisitions; tangible equity at 2026-06-30 is $234M. (5) **What
they cannot say**: whether the Mexico margins "above the division average" (FY2026 MD&A) will recur, and how the
Department of Justice subpoenas on the company's "business dealings in Mexico since 2020" (FY2023 to FY2025 10-Ks)
ended: the matter is absent from the September 2025 10-Q onward with no stated outcome (no instance found of a closure
statement in the 10-Qs of September 2025, December 2025, March 2026 or the FY2026 10-K).

## THE FOUNDATIONS (not a gate)
A share is a business: would the analyst be content owning OSIS "if the market closed for five years?" **[M1997-109]**
That depends on the business (Q1, Q2), not on the quotation. The market serves and does not instruct **[M2006-077]**:
the stock's fall from the $267 the company paid in its second fiscal quarter to $198 says nothing by itself. Margin of
safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**; the
COMPUTATION below needed a pencil and still finds the price above every central figure. **Contrary evidence, written
down as found** **[M1997-127]**: (a) Security segment margin rose from 6.4% (FY2017) to 16.7% to 17.6% (FY2024 to FY2026),
a widening, against the OUT below; (b) service revenue rose from $331M to $441M (FY2024 to FY2026), installed-base
income of the kind a castle produces; (c) Smiths Detection's own goodwill model assumes margins rise with aftermarket
mix; (d) the FY2026 cash collection answers much of the receivables worry; (e) OSIS's Security margin has run above
Smiths Detection's in every year compared. Each is weighed at Q2.

## THE STANDING RULE
Owning OSIS for cash, unlevered, sized as a single position, does not put the buyer at risk of ruin: "We are never going
to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**; "Never risk permanent loss of
capital" **[L2023-005]** is a rule on the buyer's conduct and is kept by not borrowing to buy. The target's own debt is
Q9's question (not reached).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The test: "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**. OSIS is three businesses (10-K FY2026, Note
14): Security 70% of revenue (screening equipment, cargo and border systems, turnkey screening services, radio-frequency
systems), Optoelectronics and Manufacturing 21% (components and contract electronics manufacturing), Healthcare 9%
(Spacelabs patient monitors and cardiology). Read by its parts.

- **Key variables and how predictable** **[M1998-044]**. Security: (i) government demand for screening, set by mandates
  (TSA, EU, air-cargo rules) that have only tightened for twenty-five years; (ii) the installed base and its service,
  which rose to $441M of services revenue in FY2026; (iii) the win rate in large foreign tenders, which is not predictable:
  Mexico revenue was $121M (FY2015), $8M (FY2022), $423M (FY2024), $99M (FY2026); (iv) price in those tenders. Opto:
  contract manufacturing volume and price, an ordinary business. Healthcare: hospital capital budgets against much larger
  rivals; its revenue fell from $256M (FY2015) to $163M (FY2026).
- **Would the insiders write it down?** **[M2000-105]**. For the shape of the Security business in ten years (a handful
  of certified vendors selling to governments, an installed base serviced for its life, a technology that moves inside
  regulators' approval cycles), yes: the Smiths Group directors wrote down a five-year margin path for Smiths Detection
  in their 2023 goodwill test (EBIT margin from 11.2% to an average of 14.5%, Smiths Group annual results FY2023, flagged
  non-SEC). For which large tenders OSIS wins, no; that is a range-width matter for Q7, not a matter of not understanding
  the economics.
- **Is the forecast about customers or technology?** **[M2017-019]**. About customers (governments that must screen)
  more than technology. The filer's boilerplate says its markets are "characterized by evolving customer needs and rapid
  technological change" (10-K FY2026, Item 1, Competition). The analyst reads the change (dual-energy X-ray to computed
  tomography, algorithms) as change inside a certification regime that the incumbents themselves carry out; it does not
  "hurt the business as it presently exists" in the way the technology filter means **[M1998-008]**. This is a judgment,
  and written as one.
- **The parts.** Opto is understood as a contract manufacturer; Healthcare is understood as a small, shrinking monitor
  maker. Each part that matters can be understood **[M2011-014]**: "What is important is that I understand the economic
  dynamics of the industry."
- **How far off could I be?** **[M2011-084]**: far, on any one year's earnings, because one country's contracts were 27%
  of revenue in FY2024 (Mexico $423M of $1,539M, geographic note; two Security customers 16% and 11% of revenue). That is carried to Q7.
- **Doubt test** **[M2002-092]**: the analyst's doubt is about the castle (Q2), not about what the business is or how
  its economics work.

**VERDICT: IN.** The economics of each part can be foreseen in outline ten years out; the unforeseeable element is
contract timing and size, which is a question of the castle and of the range, not of understanding.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**; the moat is what "protects excellent returns on
invested capital" **[L2007-004]**; a great business "is going to earn a high return on capital employed for a very long
period of time" **[M2007-023]**.

**Why it is still standing (the case for).** The Security business stands because there are few vendors that hold the
regulators' approvals (TSA, UK, EU; 10-K FY2026 Item 1) and decades of government relationships, and because every
machine sold is serviced for its life (services $331M FY2024 → $441M FY2026; Smiths Detection reports 51% of its sales
from aftermarket, FY2025 results, non-SEC). OSIS also claims a cost edge from vertical integration and manufacturing in
Malaysia, India and Indonesia (10-K FY2026, Growth Strategy). Its Security margins have run above Smiths Detection's in
every year compared. The castle stands as an oligopoly. The question is whether the oligopoly protects excellent returns.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**. Two cases. Leidos, a large defense and civil contractor, bought into the field
   (Security Enterprise Solutions) and recorded "a non-cash goodwill impairment charge of $596 million for the SES
   reporting unit as of fiscal 2023", citing discontinued products, delayed airport projects and "higher than anticipated
   servicing costs" (Leidos 10-K FY2025, `0001336920-26-000030`, goodwill note). Nuctech, part of the PRC-controlled
   Tsinghua Tongfang group, is the subject of the European Commission's first ex officio in-depth Foreign Subsidies
   Regulation investigation, opened on concerns that "grants, preferential tax measures, and preferential financing"
   distorted the EU market for threat-detection systems (Commission press release IP/25/3019, December 2025; non-SEC,
   flagged; read through a search summary, not the release itself). A state-financed attacker is already inside the
   market bidding for the same tenders. "We have found in a long life that one competitor is frequently enough to ruin a
   business." **[M2012-108]**
2. **Pricing power and the agony before a rise** **[M2005-020]**. The filer, on its own market: "Competition results in
   price reductions and reduced margins and could result in loss of market share" (10-K FY2026, Item 1, Competition). No
   instance found in the FY2026 10-K or the FY2026 MD&A of a price increase named as a driver of Security revenue; the
   FY2026 gross margin fell (34.3% to 33.2%) and the filer gives lower margins "in aviation and checkpoint inspection
   systems" as a cause.
3. **Would the customer still choose it over the low bid?** **[M2017-009]**. The customers are governments buying by
   tender: "A significant portion of our business is generally awarded through a competitive bidding process", with
   awards that "may be split among competitors" and protests after award (10-K FY2026, Item 1A). Among certified bidders
   the price decides much; the rows' failing answer is the buyer who does not "care from whom they buy" **[L2004-003]**.
   Regulated certification narrows the bidders; it does not stop them bidding against each other.
4. **The low-cost position** **[M2018-043]**. OSIS's margins sit above Smiths' (below), consistent with a cost edge
   over Smiths. No figure was found for Nuctech's costs (non-SEC, no filings reached); a subsidised rival's price is the
   price OSIS bids against, the case in which "whatever he charged for gas was my price" **[M2012-109]**.
5. **Ask the competitors** **[M2022-021]**. Smiths Group, owner of the market leader, chose to sell Smiths Detection to
   CVC at an enterprise value of £2.0bn, 16.3 times headline operating profit (Smiths Group announcement, 3 December
   2025, non-SEC, flagged). Leidos wrote down most of the goodwill it paid to enter. Of the two other public Western vendors,
   one owner sold its detection business and the other wrote down most of the goodwill it paid to enter.
6. **Widening or narrowing** **[M1999-108]**, **[M2000-075]**. Security: widening on the margin line (below), which is
   contrary evidence, written down. Healthcare: narrowing, revenue −36% since FY2015 and margin from 9.6% to 4.2%.
7. **What could destroy or reduce it** **[M2000-014]**: the subsidised bidder; a large customer's change of policy
   (Mexico revenue fell $177M, FY2025 to FY2026, and the filer says it carried margins "above the division average");
   the termination-for-convenience clauses in US and foreign government contracts (Item 1).

**The competitor row** (same metric, each company's own report; margins are segment operating profit before
unallocated corporate cost unless stated):

| Company, segment | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Return on capital | Source |
|---|---|---|---|---|---|---|---|
| OSIS Security | 14.9% | 15.1% | 17.6% | 17.3% | 16.7% | segment income / segment assets FY2026: 13.2% pre-tax | 10-Ks, Note 14 (accessions above) |
| Smiths Detection (Jul FY) | 11.1% | 11.2% | 11.9% | 12.7% | n/a | ROCE 7.1%, 7.7%, 9.1%, 11.4% | Smiths Group annual results FY2023, FY2025 (non-SEC, flagged) |
| Leidos SES | not disclosed | $596M goodwill impairment | | | | not disclosed | Leidos 10-K, `0001336920-26-000030` |
| Nuctech | no figures reached | | | | | | non-SEC, flagged |
| OSIS Healthcare | 12.0% | 6.0% | 4.0% | 2.8% | 4.2% | | 10-Ks, Note 14 |
| GE HealthCare, Patient Care Solutions | | | | 11.1% (CY2024) | 6.8% (CY2025) | | GEHC 10-K CY2025, `0001932393-26-000007` |
| OSIS Opto and Manufacturing | 12.3% | 12.0% | 12.1% | 12.7% | 12.8% | | 10-Ks, Note 14 |

**OSIS Security margin over the whole span the filings give** (segment income / segment revenue; FY2015 to FY2023
segment income includes restructuring charges, FY2024 on excludes them, so the series is not perfectly comparable):
FY2015 14.1%, FY2016 9.2%, FY2017 6.4%, FY2018 12.2%, FY2019 13.0%, FY2020 12.1%, FY2021 13.5%, FY2022 14.9%, FY2023
15.1%, FY2024 17.6%, FY2025 17.3%, FY2026 16.7%. Average FY2015 to FY2023, before the Mexico contracts: **12.3%**. The
Smiths Detection comparison covers FY2022 to FY2025 only; the earlier divisional figures were not reached (the FY2021
results page gives group figures only). This is a confessed gap: the margin comparison does not cover the whole span.

**Reading.** The castle stands as a certified oligopoly, but the evidence is that it does not protect excellent returns:
the industry's largest player earns a return on capital of 7% to 11%; a large, well-funded entrant wrote off $596M; a
state-financed entrant bids in the same tenders; the filer itself says competition cuts its prices; and OSIS's own best
years came from one country's contracts it now says are mostly delivered. OSIS earns more than Smiths, by a few points of
margin, which is consistent with a cost edge among ordinary-return vendors, not with a moat. In the rows' words, "most
moats aren’t worth a damn" **[M1995-038]**, and in a field where "you can have only two competitors and they’re still
terrible businesses" **[M2013-052]** the number of vendors is not the castle. Healthcare is a small player losing ground
in a field whose leader earned 6.8% in CY2025; Opto is contract manufacturing. A castle shown open on the evidence
closes OUT **[M2011-015]**.

**Against this reading, written down** **[M1997-127]**: the Security margin widened over ten years, and service revenue
is growing; if aftermarket mix keeps lifting margins, the field may be better than its recent returns. The analyst weighed
this and finds that margin widening at OSIS coincided with the Mexico contracts (FY2024 to FY2025) and that Smiths, with
51% aftermarket, still earned 11.4% on capital at its best. The alternative close, TOO HARD (NATURE) on a tenuous moat
**[M2000-019]**, is recorded in the last section; it was not chosen because the evidence here is a finding about the
field's returns, not an inability to judge them.

**VERDICT: OUT.** The castle protects ordinary returns, and the attacker with money is already inside **[L2007-004]**,
**[M2012-108]**. Price does not reopen it **[M2019-015]**. The file closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED. (Facts recorded for the record, not a clearance: capex $15M to $31M a year against D&A of $39M to $44M,
FY2022 to FY2026; working capital, not plant, is where this business's capital goes: receivables plus inventory less
payables rose from about $580M (FY2023) to $1,012M (FY2026).)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets were read in Step 0. Recorded for the record, not a clearance: two tells in
the rows' sense were found and should be weighed first if the name is ever re-run: receivables and unbilled revenue out
of line with sales for two years **[M1995-064]**, and a disclosure of a Department of Justice subpoena on Mexico dealings
that stopped being made without a stated outcome. Whether the second is a tell (the rows' "dancing" reports) or simply
the matter's quiet end could not be determined from the filings. Neither is a finding of wrongdoing.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. The record, gathered for the next analyst, **not a verdict** (every fact from the filings):
- **2012 to 2013, TSA and DHS.** Security subsidiaries received a TSA "show cause" letter (November 2012) and a DHS
  Notice for Proposed Debarment (May 2013); resolved by an Administrative Agreement allowing continued US government
  business (10-K FY2016, `0001047469-16-015059`, risk factors).
- **2016 to 2018, GSA.** The acquired AS&E was investigated by the GSA Inspector General over discount practices under
  its GSA schedule; resolved in FY2018 with a $5.0M release of the accrual (10-K FY2017, FY2018).
- **FY2018 Healthcare.** $19.4M accrued "for estimated claims and settlements in our Healthcare division" (10-K FY2018,
  restructuring note); the claims are not described there.
- **December 2017, the short seller.** A report on the company's compliance with the FCPA (the Albania turnkey program
  and Mexico were the businesses then named in the filings' risk sections). The SEC and DOJ opened FCPA investigations;
  "We were notified of closure of the inquiries by the DOJ in May 2019 and by the SEC in June 2019, and no action was
  taken by either agency" (10-K FY2019, `0001047469-19-004853`, Note 10).
- **Trading investigation.** SEC and DOJ subpoenas on trading by "executives, directors, and employees"; "in fiscal
  year 2018, we took action with respect to a senior level employee" (10-K FY2019 to FY2021). Last disclosed in the FY2021
  10-K; absent from the September 2021 10-Q onward with no stated outcome.
- **Securities class action** (Arkansas Teacher Retirement System v. OSI Systems): settled for $12.5M, paid in the
  quarter to March 2022, fully reimbursed by insurance; derivative suits dismissed, dismissal affirmed by the Ninth
  Circuit (10-Qs `0001104659-21-131824`, `0001104659-22-053645`).
- **2023 to 2025, Mexico.** DOJ subpoenas (February 2023, February 2024) arising from a case against a former employee
  of a subsidiary, requesting records of "the Company’s business dealings in Mexico since 2020" (10-Ks FY2023 to FY2025);
  absent from the September 2025 10-Q onward with no stated outcome.
- **Related party.** The Executive Chairman and the President and CEO own 10.5% and 4.5% of the Indian joint venture
  ECIL-Rapiscan, in which the company owns 36% and to which subsidiaries sell (10-K FY2026, Note 12).
- **The former CEO's pension.** A December 2025 plan amendment for the former CEO added $4.4M of prior-service
  amortization in FY2026 (MD&A, interest and other expense).
The rows that would govern this record: "If you’ve got doubts, forget it." **[M2013-088]**; and "everybody mouths the
integrity, even when it’s lacking" **[M2010-069]**. The proxy was not read.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Recorded, not a clearance: $271.9M of stock bought in FY2026 at average prices of $267.03 and $218.82,
funded in effect by the $575M 2031 convertible; a further 1,000,000 shares authorised on 2026-08-20; no price limit
stated in any filing read. The test is whether a programme names "a price above which repurchases will be eschewed"
**[L2016-002]** and buys "below its intrinsic value, conservatively-calculated" **[L1999-023]**; every price paid sits
above every central figure in the COMPUTATION below.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. **COMPUTATION — NOT A CLEARANCE**, reported at the owner's request. It carries no entry language
(operator rule 3). Method: the Q7 CONVENTION of v5 (five-year average owner cash after every real cost, growth shown on
aggregate owner cash, ten years then zero nominal growth, at the sovereign 5.63%) **[L2000-021]**, **[L2000-024]**;
script and output in `Test Runs/_research 2026-10-05 OSIS/valuation.py` and `valuation_out.txt`.

- **Cash basis (the convention's input):** five-year average owner cash $21.6M. Shown growth on it cannot be measured:
  the base year (FY2022, $5.2M) and the path through −$155.6M give "a breathtaking, but meaningless, growth rate"
  **[L2005-003]**. Using the depreciation variant's growth (4.75% a year, FY2022 to FY2026) for the top end:
  **$24 to $35 a share.**
- **Depreciation variant beside it** (working capital left out): five-year average $130.6M, growth 4.75% → **$146 to
  $212 a share.**
- **VALUE RANGE: $24 to $212 a share against $197.93.** Top over bottom about 9 to 1; under the convention a range wider
  than about three to one would close TOO HARD **[L2000-025]**, **[M2007-022]**. Even the depreciation variant alone
  ($146 to $212) has the price inside the range, which under the convention closes OUT: not a screamer **[M2009-005]**.
- **FAIR PRICE (owner's request; CONVENTION of this run for the central case):** central case = the depreciation variant
  less a working-capital charge of 35% of the sales added at 4.75% growth (35% is the receivables-plus-inventory-less-
  payables intensity of FY2019 to FY2022, before the Mexico contracts): $100.9M after tax, $125.7M pre-tax at the FY2026
  effective tax rate of 19.7%. Carried at 4.75% for ten years, then flat, discounted at **10% pre-tax** (the v5 floor
  CONVENTION **[M2003-149]**): **$1,740M, about $109 a share.** After-tax equivalent: about 8.0% at the 19.7% rate. At
  $197.93 the expected pre-tax return on the central case is **about 5.8%**, below the floor and roughly the long bond.
- **CHEAP PRICE (rule of this run, CONVENTION):** the price at which the central case's pre-tax owner cash alone, with no
  growth, yields 10%: **$1,257M, about $79 a share.** Rationale: below it the floor is met even if the business never
  grows and the Mexico years never return, so no growth assumption has to be penciled.
- The price ($197.93) sits above the fair price by about 80% and above the cheap price by about 2.5 times.

## Q8 — BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED. (For the record: at a 5.8% pre-tax central expectation against a 5.63% 30-year Treasury, the bond would win
on certainty.)

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED. Recorded: debt $1,001M against FY2026 operating income of $219M; no maturity of size before August 2029
($350M) except $2.5M due within twelve months; $629M undrawn on the revolver; performance bonds $102M and letters of credit
$95.8M outstanding. Not "little or no debt" **[R1997-001]**; the test is the ability to pay **[M1995-104]**.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Nothing in the named businesses; screening equipment, components and patient monitors.)

---
## THE BOX
**OUT, at Q2.** The castle stands as a certified oligopoly but protects ordinary returns: the field's leader earns a
7% to 11% return on capital, a well-funded entrant wrote off $596M, a state-financed bidder competes in the same tenders,
and OSIS's best years came from one government's contracts. Q7 not reached; for the owner, as COMPUTATION only: value
range $24 to $212, fair price about $109, cheap price about $79, against $197.93.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not
      done.** The file was written after the reading was finished, and nothing was committed, on the brief's instruction
      not to commit. The write-early protocol was therefore not followed; declared.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every quoted fragment beside an id is
      in that row (checked by script); every filing fact carries its accession or names its non-SEC source. Non-SEC
      figures (Smiths, Nuctech) are flagged.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is marked NOT REACHED or
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost from filed cash-flow statements, never a net-income proxy; the depreciation
      variant is shown beside it and labelled. Sovereign from the US Treasury, dated. The price is an aggregator quote,
      flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations paragraph and Q2).
- [x] No row dated after the anchor: not a point-in-time run; every row predates 2026-10-05.
- [x] Only the arithmetic lines of `tools/run.py` were used; three of its defects were found and corrected (missing
      bank lines in the debt column, intangible and other asset payments not deducted, the three-year window).
- [x] `python tools/check_framework.py` run before handing over (result in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 has no rule for a castle that stands but protects only ordinary returns.** The text routes "a castle shown open
on the evidence" to OUT and "a castle whose future cannot be judged" and the tenuous moat **[M2000-019]** to TOO HARD.
OSIS fits neither cleanly: the oligopoly is real and durable, but the evidence is that it earns ordinary returns. This
run read the moat by its definition, what "protects excellent returns" **[L2007-004]**, and closed OUT on the field's
returns. A second analyst could close TOO HARD (NATURE) on the tenuous-moat row with the same facts. A sentence saying
which governs, when the castle is shown durable but low-return, would settle it. (2) **The Q7 convention breaks on a
working-capital business.** Its input, five-year average owner cash, is $21.6M here because one country's contracts took
$458M of receivables over two years; its "growth shown on aggregate owner cash" has no meaning when a year is negative.
The convention says to show the depreciation variant beside it, but not which governs the range, so the range spans 9 to
1 and closes TOO HARD mechanically, though on either variant alone the price fails. The fair and cheap prices needed a
central case the framework does not define; this run confessed its own (working capital at the pre-Mexico intensity).
(3) **The template's Q4 balance-sheet line asks for eight to ten years "before the income account"**, but the hard
sequence puts Q4 after Q2; for a run that closes at Q2 the template says to read them in Step 0, which was done, and
what they found (two tells) could not be weighed because Q4 was not reached. A business whose decisive defect is in the
accounts can pass Q1 and fail Q2 before the accounts are judged; that order is the speakers', and the run kept it.
(4) **The competitor-row instruction asks for "same metric from the competitors' own filings"**, but two of the four
security competitors (Smiths, Nuctech) are non-SEC and one (Leidos) does not disclose the segment; the comparison could
cover only four years for Smiths and none for Nuctech. The framework gives no rule for a STOP decided partly on a
partial competitor row; this run declares the gap.
