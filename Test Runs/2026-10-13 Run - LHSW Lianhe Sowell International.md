# Company Run — Lianhe Sowell International Group Ltd (Nasdaq: LHSW, Class A ordinary shares) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the three departures the brief states: the lines of
evidence are derived by the analyst from the annual report, the competitors are those the filing names, and the primary
document is a Form 20-F. Research folder: `Test Runs/_research 2026-10-13 LHSW/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (LHSW; also searched for Lianhe and Sowell); not held.*

**Contamination, declared and not used.** (1) The session context at start listed the repository's last commits, which
name another company's v5 re-run and its box (the LZ run and its fold, 2026-10-13). (2) The same context listed
untracked file names inside other companies' research folders (AYI, ARCB). (3) The memory index loaded at start carries
one-line summaries of the queue state (a count of gate-clearers, a wave paused at a named ticker). None of these concerns
LHSW, none was opened, and none is used. No blind-listed file was opened, listed or searched; no search was run across
`Test Runs/`.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.47 (close 2026-10-12; Yahoo Finance chart series via `tools/run.py`, an aggregator, flagged per operator
  rule 5). The same series, split-adjusted for the 1-for-16 consolidation of 2026-06-22, shows $1.83 on 2026-06-30, $6.80
  on 2026-07-06, $4.50 on 2026-09-04 and $0.482 on 2026-09-11 (aggregator, flagged; `cache/yahoo_chart.json`, not
  committed). The September prospectus states a last sale of $2.88 on 2026-09-01 (424B4, 0001213900-26-096975).
- **Shares by class.** The 20-F cover (as of 2026-03-31, restated for the consolidation): 3,250,000 Class A and 62,500
  Class B (`python Screens/cover_shares.py LHSW`; 20-F FY2026, filed 2026-08-13, 0001213900-26-089090). Every count since
  then is later than the cover and comes from later filings:
  - April 2026: 2,000,000 pre-consolidation Class B (125,000 post) to Lianyue Holding Limited, the chief executive's
    wholly owned company, at $0.167 (20-F Note 23). Before the consolidation the company had 52,000,000 Class A and
    3,000,000 Class B; after it, about 3,250,000 Class A and 187,500 Class B (press release of 2026-06-17, 6-K
    0001213900-26-072296).
  - 2026-06-30: 2,400,000 post-consolidation Class B to Lianyue Holding at $0.165 a share, gross $396,000 (6-K
    0001213900-26-075052; Form 4 0001213900-26-075053; 13D/A 0001213900-26-075054).
  - 2026-09-03: 7,638,889 units at $1.44, each one Class A share and three warrants at $1.66 that expire six months
    after issue (6-K 0001213900-26-097772; 424B4 0001213900-26-096975). The prospectus states 3,267,277 Class A before the
    offering and **10,906,166 Class A and 2,587,500 Class B** after it.
  - **Count used: 13,493,666** (Class A plus Class B). The charter note: Class B carries 100 votes and converts one for one
    into Class A, and "The rights of the holders of Class A Ordinary Shares and Class B Ordinary Shares are identical,
    except with respect to conversion rights (noted above) and voting rights" (13D/A, 0001213900-26-075054), so the two
    are added for economic interest. Not counted: 22,916,667 offering warrants at $1.66 (out of the money at $0.47;
    cash-exercise or a net-share "cashless exercise", automatic at expiry only if in the money; warrant form, ex 4.1 of
    0001213900-26-097772) and 3,750 representative's warrants at $76.80 (20-F Note 18). No treasury shares are reported.
  - `tools/run.py` used a stale weighted average of 0.2M on the quote's basis; not used.
- **Market cap:** $6.34M at $0.47 on 13,493,666 shares.
- **Sovereign for the earnings currency.** The earnings currency is RMB: "all of our revenues, the vast majority of our
  expenses and most of our cash balances are denominated in RMB" and the functional currency is RMB (20-F Item 5.B and
  Note 3). `tools/run.py` labelled the earnings currency USD from the XBRL unit of the cash-flow series; that is the
  reporting currency, not the earnings currency, and its 5.60% US figure is not used. **PRC 30-year government bond
  yield 2.07%, 2026-10-12**, from the Ministry of Finance's own published China Treasury yield curve
  ("财政部-中国国债收益率曲线", compiled for the Ministry by ChinaBond). The Ministry of Finance is the issuer of PRC
  government bonds, so this is the issuing authority's figure (operator rule 5). Extract and endpoint:
  `_research 2026-10-13 LHSW/sovereign_and_fx.md`.
- **Conversion rate:** 6.7298 RMB per USD, the central parity of 2026-10-13 published by CFETS on the People's Bank of
  China's authorization (same extract). The statements are already translated into USD by the company at its own rates
  (period-end 6.8980 at 2026-03-31; FY2026 average 7.1019; 20-F Note 3).
- **Filings read** (operator rule 4): 20-F FY2026, filed 2026-08-13, 0001213900-26-089090 (Items 3.D, 4, 5, 6, 7, 15,
  16F, the audit report, the statements and Notes 1 to 23); 20-F FY2025, 0001213900-25-077169 (its figures read through
  the FY2026 comparatives); IPO prospectus 424B4 of 2025-04-04, 0001213900-25-028729 (balance sheets at 2024-03-31 and
  2023-03-31); first F-1 of 2024-05-10, 0001213900-24-041530 (balance sheets at 2023-03-31 and 2022-03-31); 424B4 of
  2026-09-03, 0001213900-26-096975; the 6-Ks, Forms 3 and 4 and Schedules 13D listed in `notes.md`. There is no proxy
  (a foreign private issuer); Item 6 of the 20-F stands in for it. **One figure cross-checked against the filed
  statement:** accounts receivable, net, at 2026-03-31: $14,978,869 on the filed balance sheet (F-3) against 14,979
  thousand in `tools/run.py`'s XBRL table; and operating cash flow FY2026, $(8,966,396) filed against -9.0 million. Both
  match.
- **`python tools/run.py LHSW`, arithmetic lines only** (`_research 2026-10-13 LHSW/run_py_output.txt`): owner cash
  (OCF less stock pay less capital spending) FY2024 -2.1M, FY2025 -1.5M, FY2026 -10.3M; mean -4.7M on either basis;
  depreciation and amortization about $0.04M a year; stock pay found only in FY2026 ($1.3M); no securities lines, no
  finance leases. Checked against the filed cash-flow statements: the as-filed columns match. The two earlier years are
  taken from the prospectuses (below).

### The balance sheets, read before the income account **[M2025-032]**
The file closes before Q4, so the balance sheets are read here, as the brief requires. **The filings give five year-ends,
2022-03-31 to 2026-03-31**; the company was private before its 2025 listing and no earlier statement is filed. Figures in
USD as filed (F-1 0001213900-24-041530 for 2022; 424B4 0001213900-25-028729 for 2023 and 2024; 20-F
0001213900-26-089090 for 2025 and 2026).

| year-end (Mar 31) | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Revenue for the year ended | 949,341 | 13,070,586 | 36,598,667 | 36,539,846 | 43,269,569 |
| Total assets | 2,657,008 | 9,239,193 | 19,129,887 | 30,729,130 | 40,991,535 |
| Cash | 150,317 | 752,007 | 206,187 | 108,745 | 1,885,367 |
| Accounts receivable, net | 674,159 | 7,591,115 | 13,272,976 | 19,144,103 | 14,978,869 |
| Allowance on receivables | n/r | n/r | 1,642,216 | 2,957,829 | 3,970,434 |
| Prepayments, current and non-current (incl. deposits, other receivables) | 259,401 | 351,965 | 3,389,227 | 9,357,175 | 18,573,492 |
| of which prepaid R&D consulting fees | n/r | n/r | n/r | 6,500,624 | 12,170,032 |
| Due from shareholders and related parties | 732,094 | 251,209 | 795,924 | 482,864 | 1,647,890 |
| Borrowings (bank, related-party and other loans) | 306,039 | 911,163 | 2,137,171 | 2,524,819 | 7,074,260 |
| Accounts payable | 198,295 | 3,198,965 | 4,795,154 | 11,782,429 | 10,224,153 |
| Total equity (2022 to 2024 total; 2025 and 2026 the company's share) | 1,321,153 | 3,248,112 | 7,848,920 | 11,595,608 | 13,870,849 |
| Retained earnings | n/r | 1,349,525 | 4,008,330 | 6,994,445 | 1,299,433 |

*(n/r = not read or not reported in the statement read; the 2022 and 2023 equity are total assets less total
liabilities as filed; the 2023 prepayments add current 231,143 and non-current 120,822; the 2024 figure adds current 1,200,827 and non-current
2,188,400.)*

What the figures say. **Sales rose about forty-fold in two years** before the listing, from $0.95M in FY2022 to $36.6M
in FY2024, and then went flat (FY2025) and up 18% (FY2026). **Receivables rose with them and stayed high**: net
receivables were 52% of the year's sales at March 2025 and 35% at March 2026, after an allowance that grew every year to
$3.97M, 21% of the gross $18.95M. **Cash never accumulated**: it was $0.15M to $0.75M at every year-end until the IPO
money arrived in FY2026, and then $1.89M. **Prepayments grew faster than anything else**: from $0.26M to $18.57M, of
which $12.17M is "Prepaid research and development consulting fee", against a research staff of "ten personnel" (Item
4.B) and a year's R&D expense of $7.81M; in the same year "Third party receivables" of $3.33M appear for the first time
(Note 6). **The equity grew from paid-in money and booked profits that never became cash**: retained earnings of $6.99M
at March 2025 fell to $1.30M after the FY2026 loss of $5.65M, while operating cash flow was negative in four of five
years. **Borrowing rose** to $7.07M, almost all one-year bank loans guaranteed by a shareholder (Note 11). **The chief
executive owes the company $1,369,876**, "unsecured, interest-free and repayable on demand" (Note 14), up from $400,406.
What they cannot say: whether the receivables and the prepayments will turn into cash. The company says that "As of and
through July 31, 2026, the Company has received approximately $ 8.6 million in settlement of accounts receivable"
(Note 4), with no statement of how much new receivable was booked in the same months.

### Owner cash after every real cost (operator rule 5; no net-income proxy)
Operating cash flow less stock pay less all capital spending (property, equipment and intangibles bought), USD, from
the filed cash-flow statements (FY2022 from the F-1; FY2023 from the IPO 424B4, which gives -1,469,694 where the F-1
gave -1,478,638; FY2024 to FY2026 from the 20-F).

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | five-year average |
|---|---|---|---|---|---|---|
| Operating cash flow | 239,201 | -1,469,694 | -2,075,626 | -1,474,574 | -8,966,396 | |
| Stock pay | 0 | 0 | 0 | 0 | 1,300,181 | |
| Capital spending | 57,618 | 5,257 | 72,126 | 39,928 | 91,953 | |
| **Owner cash** | **181,583** | **-1,474,951** | **-2,147,752** | **-1,514,502** | **-10,358,530** | **-3,062,830** |

Beside it: owner cash before interest paid (the all-equity input) averages -3,005,479; owner cash with the shareholder
and related-party advances that the company runs through operating cash flow taken out averages -2,865,699. Depreciation
($0.01M to $0.03M a year) is not a material cost here; the real costs are the working capital the sales consume and, in
FY2026, the prepaid consulting fees. RMB equivalent of the five-year average at 6.7298: about RMB -20.6M a year.
(`_research 2026-10-13 LHSW/compute.py` and `compute_output.txt`.)

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, and the test is "“Would I be happy buying this
stock if the market closed for five years?”" **[M1997-109]**. The quotation of this share moved from $1.83 to $6.80 in
four trading days in July 2026 and from $4.50 to $0.48 in five trading days in September (aggregator, flagged), and "it
doesn’t tell us anything. It just tells us prices." **[M2006-077]**; nothing in this run reads the quote as information
about the business. **Contrary evidence, written down as found** **[M1997-127]**: (1) revenue went from $0.95M (FY2022)
to $13.07M (FY2023) in the year before the first registration filing, and the top five customers and top five suppliers
were almost wholly different in each of FY2024, FY2025 and FY2026 (Item 5, Concentrations); (2) owner cash was negative
in four of five years while profits were booked in three; (3) prepaid R&D consulting fees of $12.17M against ten R&D
staff; (4) the chief executive owes the company $1.37M interest-free; (5) the June 2026 sale of 2,400,000 Class B shares
to the chief executive's company at $0.165 while the company's own filing says the Class A bid was at or above $1.00 for
the ten days from 2026-06-22 (6-K 0001213900-26-076354); (6) the prior auditor, WWC, P.C., was dismissed effective
2026-03-14, two weeks before the fiscal year end (Item 16F); (7) Note 2 of the 20-F is headed "GOING CONCERN". Evidence
for the business, also written down: the company says it has served Foxconn affiliates and built a defect-detection
system "used in Foxconn factories’ production line" (Item 4.B); it holds 18 invention patents (Item 4.B); and it has
borrowed from a dozen state and commercial banks (Note 11), which says some lenders extended it credit.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if it is bought, as every purchase must be, with the buyer's own
money and in a size whose total loss the buyer can bear: "We are never going to risk what we have and need for what we
don’t have and don’t need." **[M2012-081]**; and "borrowed money has no place in the investor's tool kit" **[L2014-005]**.
Nothing about this name bears on the buyer's conduct; no position is contemplated here (the file closes at Q1).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years. So I’ve got some notion of how the industry will develop and
where the company will stand within the industry." **[M2012-065]**; "our definition of understanding is thinking that
we have a reasonable probability of being able to asses where the business will be in 10 years." **[M2000-037]**.

**The lines of evidence chosen, and why** (the brief's first departure: derived from the 20-F, not supplied). From Item
4: what is sold, to whom, made by whom, and how the product set has moved, since Q1 asks whether the earning power can
be foreseen. From Item 5: the revenue lines and their margins over every year reported, customer and supplier
concentration, and the cash flow, since the key variables of Q1 must show in the figures. From Item 3.D: what the
company itself says about change, competition and entry. From Notes 4, 6, 11, 14, 18 and 23 and the 6-Ks, Forms 4 and
13D: receivables, prepayments, debt, related parties and the share issues, which are written under AFTER THE STOP
because Q1 decides first.

**What the business is, from the filing.** A Cayman holding company that owns, through BVI, Hong Kong and PRC holding
subsidiaries, Shenzhen Sowell (founded 2007) and its subsidiaries; not a VIE structure (Item 4.A). It sells four
"machine vision" product groups, "industrial machine vision, artificial intelligence (face recognition and AI behavior
analysis), intelligent weak current (building intelligence and intelligent transportation), and electronic customs
clearance", plus "Nine-Axis Linkage Spray Painting Robots", and in 2025 and 2026 added "a nano-molecular high-temperature
steam car washing machine and a fuel station service robot" (Item 4.B). It does not manufacture: "We do not manufacture
our machine vision products in-house. [...] outsource manufacturing to external manufacturers." Its R&D team "consists
of ten personnel", and it buys R&D from third parties (Item 4.B; R&D service fees rose 141% in FY2026, Item 5). It
reports a single segment and splits revenue into "Electronic products" and "Software" only (Item 5; Note 22).

**The key variables and whether they are foreseeable** **[M1998-044]**. The variables are what the company will be
selling, to whom, and at what margin. None has held still in the five years filed:

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Electronic products, share of revenue | 86% | 60% | 71% |
| Software, share of revenue | 14% | 40% | 29% |
| Gross margin, electronic products | 11% (computed) | 11% | 12% |
| Gross margin, software | 83% (computed) | 49% | 45% |
| Gross margin, total | 22% | 26% | 21% |
| Top five customers' share of revenue | 50.3% | 53.5% | 55.2% |
| Top five customers that were also top five the year before | n/a | 2 of 5 | 0 of 5 (A, B and E fell to 1.4% to 3.2%) |
| Top five suppliers that were also top five the year before | n/a | 1 of 5 | 0 of 5 |

*(Item 5, the revenue and cost tables and Concentrations, 20-F 0001213900-26-089090; FY2024 product margins computed
from the same tables: electronic 31,332,376 less 27,765,707; software 5,266,291 less 871,143.)* The company's own words
on the mix: in FY2025 it was "switching the sales focus to the products with higher gross margins and cutting down the
electronic products sales"; in FY2026 the mix swung back and "the gross margin of software decreased from approximately
49% to 45%" (Item 5). Before that, revenue was $0.95M in FY2022 and $13.07M in FY2023, "an increase of 1,277%" (F-1
0001213900-24-041530). The product line has moved from machine-vision inspection to robots for car paint shops, car
washes and fuel stations; the press releases of 2026 are about painting robots for Thailand and West and Southern Africa
and an agreement with an automaker's after-sales arm (6-Ks of 2026-06-08, 2026-06-24, 2026-09-22). So: "do I understand
enough about this business so that the financial statements will tell me the information that’s useful to me in making
a judgment about what the future financial statements are going to look like." **[M2008-033]**: they do not; no
filed year predicts the next year's customers, suppliers, mix or margin.

**How the industry will develop, and where the company will stand in it.** The company calls its field "a
transformative subset of artificial intelligence" and says "With the rapid iteration of technology and products, in
order to meet customers’ expectations and gain a competitive advantage in the industry, we attach great importance to
technology research and development" (Item 4.B). Its risk factors say "The machine vision industry in China is highly
fragmented and intensely competitive" and "New competitors can easily enter into the machine vision industry since there
are no significant barriers to entry." (Item 3.D). Its September 2026 prospectus counts "a total of 2,837 machine vision
companies" in Guangdong province alone at the end of 2022, and says "the mid to high end market is mostly controlled by
international brands" (424B4 0001213900-26-096975). This is the case the rows name: "a business that must deal with
fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics." **[L1993-023]**;
"if something comes in where there’s a technological component that’s of significance, or where we think the future
technology could hurt the business as it presently exists, [...] it won’t make it through the filter." **[M1998-008]**.

**The tests of the draft, applied.**
1. Where will it be in ten years? No reasonable probability can be attached to any picture of it **[M2000-037]**: the
   filed record covers five years, in which the company changed scale forty-fold, replaced most or all of its five
   largest customers in each of the two years compared, and added three robot and car-service products.
2. The key variables and how predictable they are: not predictable on the filings, as tabled above **[M1998-044]**.
3. Do the past statements tell me the future ones? No **[M2008-033]**.
4. Important and knowable? The ten-year position is important and, on this record, not knowable: "If something’s
   important but unknowable, forget it." **[M2006-076]**.
5. Would the insiders write it down? The company itself declines to: "Our historical growth rate and results may not be
   indicative of our future growth or performance" (Item 3.D). Of a field of thousands of machine-vision firms, an
   insider would not "put down on paper their predictions about where 10 companies you would choose in the tech field
   would be in 10 years, in terms of their economics. They would say, “That’s too hard.”" **[M2000-105]**.
6. Can I name the winner, not just the industry? No: "there’s industries we know that may have a wonderful future, but
   we don’t have the faintest idea who the winners will be" **[M2012-067]**; "Just because Charlie and I can clearly
   see dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on capital
   will be as a host of competitors battle for supremacy." **[L2009-005]**.
7. Customers or technology? Technology and the customers' changing projects both; the forecast turns on which products
   the company will be making, which it has changed every year.
8. How far off could I be? Without a model of the place there is no model of the error **[M2011-084]**.
9. Do I doubt it is inside? Yes, and "if you have doubts about something being into your circle of competence, it
   isn’t." **[M2002-092]**.
10. Do I only think I understand it? The products can be described; the economics cannot: "We understand what it does
   for people. We just don’t know the economics of it 10 years from now." **[M2000-104]**.
11. Abroad, governance and tax: a Cayman holding company over PRC subsidiaries, cash leaving the PRC only by dividend
   under SAFE rules (Item 3.D), voting control 97.69% in one person (6-K 0001213900-26-075052). Recorded; not needed to
   decide.

**Which cause.** The deciding question, where the economics of a small Chinese machine-vision and robotics integrator
will be in ten years, is a forecast the industry's own insiders would not write down **[M2000-105]**, and more reading
of this company's filings would not supply it: "We couldn't solve this problem, moreover, even if we were to spend years
intensely studying those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we
have no insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**.
That is the second cause of section I, NATURE, not WORK. Change is the reason, and the rows' response to it is to pass:
"whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on that."
**[M1999-063]**. The box is not a finding that the business is bad or that the price is wrong: "It doesn’t mean it isn’t
a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to
evaluate it." **[M2000-038]**. A lower price does not reopen it (section I).

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The filing facts: "rapid iteration of technology and products" and
"no significant barriers to entry" in the company's own words (20-F Items 4.B and 3.D, 0001213900-26-089090); top five
customers and suppliers replaced wholesale year to year (Item 5); three robot and car-service products added since 2022
(Item 4.B). The file closes here; Q2 to Q10 and Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion.
NOT REACHED. The balance sheets were read in Step 0, as the brief requires when the file closes before Q4.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts are recorded under AFTER THE STOP and are not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. No buyback exists to test against the bottom of a Q7 range (Item 16E answers "Not applicable.").

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

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
**TOO HARD (NATURE) at Q1, integrity facts recorded, not judged.** The ten-year economics of a small PRC machine-vision
and robotics integrator in a field the company itself calls one of "rapid iteration of technology and products" with
"no significant barriers to entry" are a forecast the industry's insiders would not write down **[M2000-105]**, and study
would not supply it **[L1993-023]**. A lower price does not reopen it. No research pass is opened (the cause is NATURE).
For the fold: the COMPUTATION below finds no positive price at which any case earns the floor, so the top of the computed
range is below zero and gives no alert price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source, written down and not weighed **[M1997-127]**.
The box is unchanged (operator rule 2).

### Bearing on Q2 (the castle)
- **The rivals the filings name.** The 20-F FY2026 names no competitor (text search of the filing for rival names and
  for "compete with"; Item 3.D speaks only of "various multinational corporations and domestic brands"). The September
  2026 prospectus names them by product group (424B4 0001213900-26-096975, Business, Competition): industrial machine
  vision, "JT Automation Equipment Co." and "Suzhou TZTEK Technology Co., Ltd."; face recognition, "SenseTime Group
  Inc.", "Hanwang Technology Co., Ltd" and "Wisesoft Co., Ltd."; weak current, "Beijing Qianfang Technology Co., Ltd."
  and "PCI Technology Group Co., Ltd."; AI behaviour analysis, "Huawei" and "Inspur Electronic Information Industry Co.,
  Ltd.". **None of the nine files with the SEC** (flagged; each is listed in Shanghai, Shenzhen or Hong Kong, or is
  private). So no competitor row can be filled from SEC filings, and the brief forbids supplying my own list as evidence.
  The same prospectus says that "the mid to high end market is mostly controlled by international brands" and that the
  company responds "with customized solutions at low cost".
- **Entry and price**, in the company's words: "New competitors can easily enter into the machine vision industry since
  there are no significant barriers to entry" (20-F Item 3.D); government bids are contested on "quality of products and
  pricing" (Item 4.B); customers return for a "competitive price offering" (Item 4.B); "We currently do not enter into
  any long-term framework agreements with our customers" (Item 4.B).
- **Margins over the span filed:** total gross margin 22% (FY2024), 26% (FY2025), 21% (FY2026); electronic products
  11% to 12% throughout; software 83% (FY2024, computed), 49%, 45% (Item 5). Operating margin 8%, 9%, then -16%.

### Bearing on Q3 (the capital the business needs)
- Booked operating income of $2.98M (FY2024) and $3.08M (FY2025) on equity of $7.85M and $11.60M, against owner cash of
  -$2.15M and -$1.51M in the same years: the profit ended each year as receivables and prepayments, not cash (Step 0
  tables). Net receivables were 35% to 71% of the year's sales at every year-end filed.
- The 20-F carries a plan for "$10 million cash required to complete the preliminary assembling and installation of
  production equipment and machineries of an in-house production and assembly line for our Nine-Axis Linkage Spray
  Painting Robot" (Item 5.B), while Item 4.B says the company does not manufacture in-house.

### Bearing on Q4 (the accounts)
- **Prepayments.** "Prepaid research and development consulting fee" $12,170,032 at 2026-03-31, up from $6,500,624;
  $10,443,032 of all prepayments is carried as non-current (Note 6). The R&D team is "ten personnel" (Item 4.B). FY2026
  R&D expense was $7,811,079, its rise "primarily attributable to a $4,017,098, or 141%, increase in third-party research
  and development service fees" (Item 5). "Third party receivables" of $3,331,487 appear for the first time (Note 6). The
  row that names this tell, for the question it belongs to: "if some prepaid expense, deferred asset accounts start
  building up suspiciously high [...] you want to look twice at companies like that." **[M1995-064]** (recorded, not
  applied).
- **Receivables.** Gross $18,949,303 less an allowance of $3,970,434 at 2026-03-31; the allowance rose from $1,642,216
  in two years (Note 4); expected credit loss charges of $1.12M, $1.31M and $1.39M in FY2024 to FY2026 (cash-flow
  statement).
- **The auditor.** WWC, P.C. was dismissed "effective as of March 14, 2026" and EliteCPA P.C. appointed, which "served
  as the Company’s auditor since 2026" (Item 16C, Item 16F, audit report). WWC's reports carried no adverse opinion or
  modification (Item 16F).
- **Going concern.** Note 2 is headed "GOING CONCERN"; on management's plan it concludes the cash will suffice for twelve
  months.
- **The same figure stated two ways.** FY2023 operating cash flow: $(1,478,638) in the F-1 of 2024-05-10 and $(1,469,694)
  in the IPO prospectus of 2025-04-04. The price of the June 2026 Class B sale: "the average closing price, as reported on
  Nasdaq.com, of the Class A ordinary shares" in the 6-K, the 13D/A and the September prospectus, but "75 % of the
  five ( 5 ) trading days" average "pre-consolidation closing price" in the 20-F (Note 23), which also dates the sale
  2026-07-01 where the 6-K and Form 4 say 2026-06-30. The FY2026 stock pay: "1,000,000 Class A Ordinary Shares to Lianyue
  Holding Limited" in Item 5, but "400,000 Class B Ordinary Shares be issued to Lianyue Holding Limited" in Note 18.
- **Prospectus text in the annual report.** The 20-F's liquidity paragraph speaks of costs "which we expect to be covered
  with 45% of our proceeds from this Offering" (Item 5.B), a sentence written for a prospectus.
- **Tax.** A deferred tax asset of $1,863,259, including $1,156,253 for operating-loss carryforwards, with no valuation
  allowance after a loss year (Note 17); income taxes paid were $12,901 (FY2026), nil (FY2025) and $13,230 (FY2024).

### Bearing on Q5 (who runs it): integrity facts, recorded and not judged
- **The June 2026 Class B sale.** On 2026-06-30, eight days after the 1-for-16 consolidation took effect, the company sold
  2,400,000 post-consolidation Class B shares to Lianyue Holding Limited, wholly owned by the chairman and chief executive
  Yue Zhu, at $0.165 a share, $396,000 in all, approved and ratified by the audit committee (6-K 0001213900-26-075052;
  Form 4 0001213900-26-075053; 13D/A 0001213900-26-075054). The company's own 6-K of 2026-07-08 says the Class A closing
  bid was "$1.00 per share or greater" on every day from 2026-06-22 to 2026-07-06 (0001213900-26-076354); the aggregator
  close on 2026-06-30 was $1.83 (flagged). At the company's own $1.00 the shares sold were worth at least $2.40M against
  $0.396M paid, a difference of about $2.0M; at $1.83, about $4.0M; the company's equity at 2026-03-31 was $13.87M. After
  it Mr Zhu held 939,688 Class A and 2,550,000 Class B, "approximately 97.69% of the aggregate voting power" (6-K), and,
  by my arithmetic on the prospectus counts, about 60% of the economic interest before the September offering (3,489,688
  of 5,854,777 shares) and about 26% after it.
- **Earlier issues to insiders.** November 2025: 400,000 Class B to Lianyue Holding and 600,000 Class B to Patton Holding
  (Dengyao Jia), "each at par value", charged as stock pay of $1,300,181 (Note 18; Item 5). April 2026: 2,000,000
  pre-consolidation Class B to Lianyue Holding at $0.167, after which Mr Zhu held 72.45% of the vote (Note 23).
- **Money owed by the chief executive.** "Mr. Yue Zhu" owed the company $1,369,876 at 2026-03-31 and $400,406 a year
  before, "unsecured, interest-free and repayable on demand" (Note 14); the operating cash flow shows "Advances to
  shareholders" of $930,035 in FY2026. The company's bank loans are "guaranteed by a shareholder" (Note 11).
- **Related-party business.** Shenzhen Botan Technology, wholly owned by the chief executive of a subsidiary, owed the
  company $870,315 at 2024-03-31 (after $566,002 of sales to it in FY2024) and $251,006 at 2026-03-31 (Item 7.B; Note 14).
- **The chief executive's pay** is a salary of "RMB20,000 (approximately $2,919)" a month; director's remuneration
  $33,794 in FY2026 (Item 6; Note 14). No options.
- **The September 2026 unit offering** was priced at $1.44 a unit, each unit one Class A share and three six-month
  warrants at $1.66, when the prospectus gave the last sale as $2.88 on 2026-09-01 (424B4 0001213900-26-096975; 6-K
  0001213900-26-097772). The aggregator close fell from $4.50 on 2026-09-04 to $0.482 on 2026-09-11 (flagged). The
  placement agent, R. F. Lafferty & Co., was also the IPO's underwriter (Note 18; 6-K).
- **Disclosure.** The 20-F's beneficial-ownership table lists only Mr Zhu among holders, though Lianhe Holding Group
  (Hainan Lianhe) received 15,000,000 pre-consolidation Class A shares, 30%, at the reorganisation (Item 7.A; Note 18);
  whether it still holds them is not stated in what I read.

### Bearing on Q6 (the money and the owners)
- Shares outstanding (post-consolidation basis): 3,125,000 at 2025-03-31; 3,312,500 at 2026-03-31; 5,854,777 after the
  June sale; 13,493,666 after the September offering; plus 22,916,667 warrants at $1.66 expiring about March 2027. Issue
  prices on the post-consolidation basis: $64.00 at the IPO of April 2025 ($4.00 before consolidation; Note 18); par in
  November 2025; about $2.67 in April 2026 ($0.167 before consolidation); $0.165 in June 2026; $1.44 in September 2026.
- No dividends ("Our board of directors has never declared a dividend", Item 8) and no buybacks (Item 16E, "Not applicable."). FY2026 G&A included "overseas marketing research and consultancy fees
  amounted to $2,259,167" (Item 5).
- Structure: a Cayman holding company over PRC subsidiaries owned outright, not a VIE; cash enters the PRC by capital
  contribution or shareholder loan and leaves by dividend under SAFE rules (Item 3.D). Class B carries 100 votes; one
  holder has 97.69% of the vote.

### Bearing on Q9 (could it ruin us)
- Borrowings $7,074,260 at 2026-03-31, of which $6,319,223 are one-year bank loans at 2.50% to 4.13%, almost all
  guaranteed by a shareholder; one WeBank loan at 13.77% (Note 11). Cash $1,885,367. Operating loss $6,824,783 in FY2026
  (Item 5). "there were no pending or threatened claims or litigation" (Note 19). No product-liability or
  business-interruption insurance (Item 4.B).

### Bearing on Q7: COMPUTATION, NOT A CLEARANCE
The owner's two reporting figures, built by Q7's range convention: arithmetic on a closed file, with no entry language.

- **Owner cash** (Step 0): five-year average **-$3,062,830** a year (about RMB -20.6M at 6.7298); before interest
  -$3,005,479; the literal three-year window, FY2024 to FY2026, -$4,673,595.
- **Specifics applied.** The growth input: the series changes sign (FY2022 positive, the rest negative), so the compound
  rate is meaningless; between the halves of the window (FY2022 and FY2023 average -$646,684; FY2025 and FY2026 average
  -$5,936,516) a rate on a negative base is also meaningless; so, by specific (b), **the range is the no-growth case
  alone, said so**. (a) Neither end year is a cycle peak or trough on the filer's own description; FY2022 is a pre-scale
  year and FY2026 carries IPO-year costs, so the FY2023 to FY2025 average (-$1,712,402) is shown beside. (c) No
  acquisitions (one minor subsidiary sold in FY2025). (d) Working capital is inside the operating cash flow used. (e)
  Depreciation and capital spending are each under $0.1M a year, so the maintenance-only case equals the all-spending
  case. (f) No cap is reached. Tax: owner cash is after the company's own tax as paid, which was close to nil; no
  carryforward shelter is priced, since nothing positive remains to shelter.
- **Net debt**, all-equity basis: borrowings $7,074,260 less cash $1,885,367 = $5,188,893 at 2026-03-31; operating leases
  ($1,074,417) left out. The latest filing carrying that balance sheet is the September prospectus, which states the April
  and June placements ($334,000 and $396,000) and the offering's net proceeds of $9,221,087 (the prospectus's estimate):
  **net cash $4,762,194**, on **13,493,666** shares. Beside it, the 20-F's own subsequent events only (the two
  placements): net debt $4,458,893 on 5,854,777 shares.
- **VALUE RANGE** (the no-growth case at the PRC 30-year rate of 2.07%): whole business -$147,962,821; **-$10.61 per
  Class A share** on the central basis (RMB -71.40 at 6.7298); on the literal three-year window -$16.38; on the FY2023 to
  FY2025 average -$5.78. Against a price of $0.47 (RMB 3.16).
- **FAIR PRICE** (each end case valued at ten percent and the two averaged; here there is one case): all-equity, the
  central figure, **-$1.92 per Class A share** (RMB -12.92); **equity-only -$2.27** (RMB -15.28; owner cash after
  interest against the share count, net debt not added). Beside them: on the 20-F's own subsequent events -$5.99; on the
  FY2023 to FY2025 average -$0.92; on the literal window -$3.11. **No positive price earns the floor on any case.**
- **The floor, tested first:** no case earns about ten percent at $0.47 or at any positive price; were the file open at
  Q7 it would close OUT on the floor before the width test: "there’s just a point at which we drop out of the game."
  **[M2003-149]**. The file is closed at Q1, and this changes nothing.
- The arithmetic: `_research 2026-10-13 LHSW/compute.py` and `compute_output.txt`.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 1885f516, before `tools/run.py` or any EDGAR request); written
      question by question. Committed after the template copy; Step 0, the foundations, the standing rule and Q1 went in
      one commit (08077842) because Q1 closed the file in the same sitting, so Step 0 was not committed on its own before
      Q1 as write-early asks; then AFTER THE STOP and the self-audit in a further commit.
- [x] Dispatched: the brief allowed the per-question pathspec commits and states the lock is held by the dispatching
      session; the fold is the dispatcher's (operator rule ten). The lock file was not opened by me.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the accidental sightings (commit
      subjects, research-folder names and memory lines in the session context) are declared at the top and not used.
- [x] Every v5 id resolves (`_research 2026-10-13 LHSW/check_ids.py`); every filing fact has its accession; numbers are
      from the filings or from `compute.py` on filed figures.
- [x] The order was kept; Q1 closed the run; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign for the earnings currency (RMB) from the issuing authority's own curve, dated; aggregator quotes
      flagged.
- [x] Contrary evidence was written down as found **[M1997-127]** (the foundations, and AFTER THE STOP); integrity facts
      flagged in the box line.
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used; its earnings-currency label (USD), its US sovereign and its
      stale weighted-average share count were not used.
- [x] `python tools/check_framework.py` PASS before the last commit (result in the last commit's message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The sovereign for an earnings currency outside the protocol's table.** The table names issuing authorities for USD,
JPY and EUR only. For RMB I used the Ministry of Finance's own published treasury curve (compiled by ChinaBond). And
`tools/run.py` takes the earnings currency from the XBRL unit, which for a 20-F filer that reports in USD with an RMB
functional currency names the wrong currency; the table and the tool could both cover the case. (2) **Which filing's
subsequent events set net debt.** Q7's basis rule takes net debt "at the latest filed balance-sheet date with the
subsequent events that filing itself states added". Here the 20-F states two small placements, and the later
prospectus, which reprints the same balance sheet, states an $11M offering. I took the prospectus as the latest filing
carrying the balance sheet and showed the 20-F-only figure beside; the text does not say which governs. (3) **A negative
base.** Specific (b) handles a declining series, not a base that is negative throughout. The no-growth perpetuity of a
cash loss at 2.07% gives -$148M for a business with $13.9M of book equity, a number with no economic meaning (a business
losing cash forever is closed or recapitalised), though the statement it supports, that no positive price earns the
floor, is sound. A line saying that a negative base is reported as "no positive price" rather than as a magnitude would
help. (4) **Eight to ten years of balance sheets** where only five exist: the template gives no instruction; I read every
one filed and said so. (5) **Q1 test 11 and a 97.69% vote.** The test asks about governance abroad but does not say
whether a dual-class structure that gives one person nearly all the vote is read at Q1 or left to Q5 and Q6; I recorded it
and left it to them, since Q1 closed on the economics alone.
