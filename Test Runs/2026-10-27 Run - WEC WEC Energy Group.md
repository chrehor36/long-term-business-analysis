# Company Run — WEC Energy Group, Inc. (NYSE: WEC) — 2026-10-27
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-27: the operator does not hold this name (`PORTFOLIO.md` has no WEC row).*

**Dispatched run.** Analyst dispatched under `Screens/_daily/_dispatch_brief.md` with two departures the brief states
(the repository path is `C:\Projects\BRK` since 2026-10-25; the lines of evidence and the competitors are derived by the
analyst, not hand-written in the brief). Working folder: `Test Runs/_research 2026-10-27 WEC/` (notes, fetch and
arithmetic scripts, outputs; raw filings in its ignored `cache/`).

**Contamination, declared.** Seen by accident and not used: (1) a directory listing of `Test Runs/` made to check that this
file did not already exist showed the file name `2026-10-27 Run - VST Vistra.md` and its research folder; (2) the session's
opening git status and recent commit subjects name a VST v5 re-run "OUT at Q7, not armed" and an ARCB research file; (3) a
memory index line loaded with the session names the wave-7 queue and a count of gate-clearers. None is about WEC and none
was opened. No file about WEC under any name was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $111.12 (close 2026-10-26; Yahoo chart via `tools/sources.py`, an aggregator, flagged per operator rule 5;
  live quote only).
- **Shares by class:** one class of common stock. 325,849,383 shares outstanding "as of the latest practicable date
  (June 30, 2026)" on the cover of the 10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession
  `0000783325-26-000087`; the balance sheet of the same filing states the same 325,849,383 outstanding (no treasury shares:
  the issued count in the XBRL is the same figure). `python Screens/cover_shares.py WEC` parsed no cover count ("read the
  filing by hand"); read by hand as above. **After the 10-Q:** the October 2025 equity distribution agreement ($3.0 billion
  at-the-market with forward components) had issued no shares by 2026-06-30, but forward sales of 6,392,021 shares
  (58,533 + 3,726,090 + 2,607,398, at initial forward prices of $110.77, $114.85 and $111.41, maturing June to December 2027)
  were outstanding and unsettled (10-Q, Note on common equity). No 8-K filed after the 10-Q (2026-08-11, 2026-08-18,
  2026-09-04) reports a share issuance; an S-3ASR was filed 2026-10-16 (accession `0001104659-26-116528`, a shelf, not an
  issuance). Count used: **325.849M**; the count with the forwards physically settled, **332.241M**, is shown beside where it
  matters.
- **Market cap:** 325.849M x $111.12 = **$36,208M**.
- **Sovereign for the earnings currency (USD):** **5.31%**, US Treasury daily par yield curve, 30-year, 10/26/2026
  (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-20, accession `0000783325-26-000018`: Item 1 (business, segments, regulation, the allowed
    returns table), Item 1A (risk factors), Item 3, Item 7 (MD&A: corporate strategy, capital plan, results by segment,
    liquidity, Illinois proceedings), Item 8 (the statements; notes on acquisitions, income taxes, segments, regulatory
    environment).
  - 10-K for FY2022, filed 2023-02-23, accession `0000107815-23-000100` (cash flows 2020 to 2022, segments 2020 to 2022,
    tax reconciliation 2020 to 2022, the February 2021 gas-cost event, the purpose of share purchases).
  - 10-K for FY2019, filed 2020-02-27, accession `0000107815-20-000089` (opened for the 2017 to 2019 cash-flow statement;
    used for context only).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession `0000783325-26-000087` (cover, balance sheet, equity
    and forward sales, debt).
  - Proxy (DEF 14A) filed 2026-03-26, accession `0000783325-26-000035` (pay, board, pay ratio).
  - 8-Ks: 2026-02-03 (`0000783325-26-000006`, the Illinois Attorney General settlement), 2026-02-05 (`0000783325-26-000011`,
    FY2025 earnings release, exhibit 99.1), 2026-04-01 (`0000783325-26-000040`, the 2027-2028 Wisconsin rate requests and
    the Oak Creek 7 and 8 extension), 2026-07-29 (`0000783325-26-000080`, Q2 2026 release), 2026-08-11
    (`0000783325-26-000092`, controller succession), 2026-08-18 (`0000783325-26-000095`, the Point Beach PPA), 2026-09-04
    (`0000783325-26-000099`, investor slides, not read beyond the item).
  - Competitors' XBRL company facts (see Q2): Alliant Energy (CIK 0000352541), Xcel Energy (CIK 0000072903), CMS Energy
    (CIK 0000811156).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025, $3,379.4M on
  the filed consolidated statement of cash flows (10-K `0000783325-26-000018`, Item 8, E), equals the XBRL figure
  `tools/run.py` prints (3,379). Also long-term debt at 2025-12-31, $18,498.1M filed, equals the XBRL 18,498.
- **`python tools/run.py WEC`, arithmetic lines only** (Part VII; its v4 material ignored): three-year owner earnings mean
  on the capex basis **-53** ($M; OCF less stock pay less capital spending), on the depreciation basis **1,805**; the
  five-year window **-237** and **1,452**. Its capex tag (`PaymentsToAcquireOtherPropertyPlantAndEquipment`) carries the
  "Capital expenditures" line only and leaves out the acquisitions of renewable facilities, the capital contributions to
  ATC and the other investing lines that are on the same filed statement; the figures used below are therefore taken from
  the filed cash-flow statements, not from the tool. Depreciation was found and agrees with the filed statement
  (1,478.5 in 2025). Stock pay resolved: `AllocatedShareBasedCompensationExpense` 15.7, 34.8, 9.7, 39.3, 48.2 for 2021 to
  2025 ($M); performance units are settled in cash (proxy), so subtracting the whole expense may count part of it twice;
  it is subtracted all the same, the conservative way, and it is small.
- **The lines of evidence, chosen and where from.** From Item 1: the six segments and what each owns; the regulated retail
  rates table (authorized return on equity and equity component per utility); the ATC interest; We Power's lease terms;
  the data-centre load (Microsoft, Vantage) and the very-large-customer tariffs. From Item 1A: regulation and rate
  recovery, the capital programme and its funding, the holding company's dependence on subsidiary dividends, credit
  ratings and collateral, competition and retail choice, tax credits. From Item 7: the capital plan ($37.5 billion 2026 to
  2030), the three-year capital table by segment and by kind, results by segment, the earnings-sharing mechanisms, the
  Illinois riders and the Attorney General settlement, the ICC's pause of Peoples Gas pipe replacement, liquidity and
  the working-capital deficit, financing (debt issued, the ATM and forwards), the 2026 effective tax rate guide. From
  the statements and notes: ten years of balance sheets (with `tools/run.py`'s table), cash flows 2020 to 2025, the
  acquisitions note, the income-tax reconciliation (PTCs), the segment note.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own WEC "if the market closed for five years"
**[M1997-109]**, which for a regulated utility turns on the regulatory compact, not on the quotation. The margin of safety
bears most: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. No
macro view enters: interest rates, data-centre demand forecasts and gas prices are not forecast here **[M2000-094]**; the
data-centre load enters only as what the filings say is contracted or proposed. Who is paid to tell you: the company's
own 7 to 8 percent long-term EPS growth projection and the annual EPS guidance are a manager's projection of what he
sells and are not used as inputs. **Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after all
capital spending was negative in every year 2021 to 2025 (average -$734M a year), the dividend and the growth being paid
with new debt and, from 2024, new shares; (2) the capital plan of $37.5 billion for 2026 to 2030 is larger than the
whole market value; (3) the Illinois segment has carried a regulator's pause on pipe spending (November 2023), capital
disallowances (2023, 2024) and a $205M settlement charge (2025); (4) holding-company leverage raises the consolidated
return on equity above the regulators' allowed figure; (5) the bonus for 2025 was paid at the 200 percent maximum on an
adjusted EPS that excluded the Illinois charge; (6) consolidated debt rose faster than equity over ten years.

## THE STANDING RULE
The run assumes an unlevered buyer paying cash for a small part-interest that he is never forced to sell; on that
assumption owning WEC does not put the buyer at risk of ruin: "We are never going to risk what we have and need for what
we don’t have and don’t need." **[M2012-081]**; no margin, no collateral, nothing that "can result in sudden demands for
large sums" **[L2014-024]**. The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]** (the row's spelling). The product (electricity and gas delivered under tariffs) is plain; what has
  to be foreseen is "the economic dynamics of the industry" **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the return the regulators allow and the
  equity share they allow: 9.80 percent on a 53.0 percent equity component for WE, WPS and WG (PSCW), 9.86 percent on 50
  percent for UMERC and MGU (MPSC), 9.38 percent on 50.79 and 52.58 percent for PGL and NSG (ICC), 9.65 percent on 53
  percent for MERC (MPUC) (10-K `0000783325-26-000018`, Item 1, E, the 2025 retail rates table); We Power's leases at a
  12.7 percent return on equity and a 55 or 53 percent equity ratio under the Leased Generation Law (Item 1, D); ATC's
  base return of 9.98 percent set by FERC (Item 7). (2) The rate base: how much capital the commissions approve, which
  the filing states as a plan ($33.4 billion of utility capital spending plus $4.1 billion for ATC, 2026 to 2030). (3) The
  regulatory climate in each state, which the filing shows differing: Wisconsin rate orders that raised margins by $402.4M
  in 2025 and an earnings-sharing refund because the Wisconsin utilities earned above their allowed return, against
  Illinois, where the ICC paused Peoples Gas's main replacement in November 2023 and disallowed capital. (4) The new load:
  Microsoft and Vantage data centres, "up to 2.6 GWs of load growth in the Milwaukee-to-Chicago corridor through 2030" and
  1.3 GW at Port Washington, with very-large-customer tariffs proposed at returns of 10.48 to 10.98 percent on a 57 percent
  equity ratio (Item 1 and Item 7, Corporate Strategy). The first three are the cost-of-service model, which has been
  stable in Wisconsin for the whole span read; the fourth is a forecast of others' building, which the tariffs are built
  to pass to those customers.
- **Is it important and knowable?** **[M2006-076]** The deciding thing for ten years is what the regulators let the owners
  earn on the capital they put in. That is knowable in kind from the filings (orders, allowed returns, sharing mechanisms,
  disallowances), though not as a forecast of any one order. The insiders do write this forecast down: the company
  publishes a five-year capital plan by segment and kind, and the commissions publish allowed returns **[M2000-105]**.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The
  doubt I have is about the price the regulators will allow for the capital, not about how the business makes its money;
  that doubt belongs to Q2 (is the compact durable) and Q7 (what is the cash worth).
- **Routing.** No fast-changing technology closes the file: the generating mix is changing (coal out by 2032, gas, solar,
  batteries in) but the economics stay cost of service plus an allowed return on whatever is built. A holding company of
  parts: the deciding part (Q2) is the Wisconsin segment, which is understood by the same tests.
- **VERDICT: IN.** A regulated return on approved capital in four states, with the variables named in the filing and a
  published plan **[M2012-065]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (business of parts, section B convention). The filer reports six segments and measures them by net
income attributed to common shareholders, the measure its chief operating decision maker uses (10-K `0000783325-26-000018`,
Note 22: "Net income attributed to common shareholders best measures our segment profitability"); it reports no segment
operating income. **CONVENTION of this run:** the parts are sized on the filer's segment net income, since that is the only
segment profit the filing states; rationale: the threshold needs a profit figure per part and the filer gives one.
Five years 2021 to 2025 ($M; 2023 to 2025 from `0000783325-26-000018`, 2021 and 2022 from `0000107815-23-000100`):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year total | Share of the positive parts | Castle |
|---|---|---|---|---|---|---|---|---|
| Wisconsin (WE, WPS, WG, UMERC: electric, gas, steam) | 706.5 | 758.4 | 851.3 | 863.1 | 1,054.8 | 4,234.1 | 54.2% | statutory service territory; PSCW-allowed return |
| Illinois (PGL, NSG gas distribution) | 223.0 | 226.9 | 140.0 | 252.1 | 122.1 | 964.1 | 12.3% | Chicago charter, "first in the field"; ICC hostile |
| Other states (MERC, MGU gas) | 35.8 | 39.7 | 48.1 | 54.5 | 60.8 | 238.9 | 3.1% | franchises; Minnesota not exclusive |
| Electric transmission (about 60% of ATC, equity method) | 106.3 | 129.5 | 119.1 | 141.0 | 147.6 | 643.5 | 8.2% | FERC-regulated wires |
| Non-utility energy infrastructure (We Power leases to WE; Bluewater storage; WECI contracted renewables) | 279.2 | 324.4 | 336.0 | 380.8 | 411.1 | 1,731.5 | 22.2% | leases fixed by statute; WECI on offtake contracts and PTCs |
| Corporate and other (holding-company interest, mostly) | (50.5) | (70.8) | (162.8) | (164.3) | (238.9) | (687.3) | | |
| Consolidated | 1,300.3 | 1,408.1 | 1,331.7 | 1,527.2 | 1,557.5 | 7,124.8 | | |

**Wisconsin decides**: 54.2 percent of the positive parts, 59.4 percent of the consolidated five-year total. The file
closes on the Wisconsin castle; the others are carried.

**The castle tests, each with its filing fact.**
- *What keeps it standing* **[M1995-038]**: law. "Our electric utilities are authorized to provide retail electric service
  in designated territories in the state of Wisconsin, as established by indeterminate permits and boundary agreements
  with other utilities" (Item 1, B); the PSCW "continues to maintain the position that the question of whether to
  implement electric retail competition in Wisconsin should ultimately be decided by the Wisconsin legislature. No such
  legislation has been introduced" (Item 7, Competitive Markets). This is the "natural franchise" kind of moat the rows
  name **[M1995-037]**. It does not depend on "the genius of the lord" **[M1995-038]**.
- *The attacker with money* **[M2011-015]**: a rival could not build a second set of wires and pipes into Milwaukee; for
  Illinois the filing itself says "it would be impractical to construct competing duplicate distribution facilities due
  to the high cost of installation" (Item 7). The real attackers are three: self-generation and alternative supply
  (Item 1, Competition), a legislature that opens retail choice (Item 1A), and the regulator who lowers the return.
- *Pricing power* **[M2005-020]**: the business has none of its own; prices are set by the commission. What it has instead
  is the expectation of earning the allowed return: "when you get an allowed return in the electric utility you’re almost
  certain of earning it" **[M2010-037]**. Filing fact: the Wisconsin utilities earned above their allowed 9.80 percent in
  2025 and booked an earnings-sharing expense of $28.6M (Item 7, Wisconsin segment operation and maintenance table);
  Wisconsin rate orders effective 2025-01-01 raised margins by $402.4M.
- *Unit volume*: electric customers 1,669.3 thousand (2023) to 1,696.6 thousand (2025); weather-normal retail electric
  deliveries up 1.1 percent in 2025; the filer forecasts 2026 retail volumes "relatively flat" excluding the very large
  data-centre customers (Item 1).
- *The low-cost position* **[M2004-091]**: not the castle here; the customer cannot choose another wire. The low-cost
  question bites only in MISO dispatch of generation (Item 1: "The cost of our individual generation offered into the MISO
  Energy Markets compared to our competitors affects how often our generating units are dispatched"), which is a cost
  race among generators for dispatch, not a customer's choice of wire.
- *Widening or narrowing* **[M1999-108]**: Wisconsin widening in the span read (rate orders granted, sharing paid, new
  generation approved for data centres); Illinois narrowing on the evidence (November 2023 ICC order pausing PGL's
  pipe-replacement spending; capital disallowed in 2023 and 2024; a 2018 UEA refund upheld by the Illinois courts in
  March 2025; the $205M settlement of February 2026; a "Future of Gas" proceeding open to the end of 2026 that could cut
  gas investment in Illinois). Illinois is 12 percent of the parts and does not decide.
- *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: a regulatory climate that turns,
  the row on the utility mistake: "the regulatory climate in a few states has raised the specter of zero profitability or
  even bankruptcy" **[L2023-011]**; electrification mandates against gas distribution (Item 1, Competition); retail choice
  by statute (Item 1A); stranded data-centre generation if the large customers do not come, which the proposed tariffs are
  written to put on those customers (Item 1A, the VLC and Bespoke Resources tariffs, pending before the PSCW). Slow change
  can "lull you to sleep easier" **[M2014-038]**: the Illinois gas business is the slow-change case.

**The competitor row.** The 10-K names no rival company: competition is described only as "other utilities", "alternative
electric suppliers" and "marketers" (Item 1, Competition). **CONVENTION of this run:** three comparable SEC filers chosen
by me: Alliant Energy (the other large PSCW-regulated holding company, through Wisconsin Power and Light), Xcel Energy
(a neighbouring Upper Midwest utility with a Wisconsin subsidiary) and CMS Energy (a Michigan combination utility); no
named rival exists to be flagged as a non-filer. Rationale: the castle is a legal franchise and the field's returns are set
by commissions, so the comparison that tests the castle is the same metric for other regulated holding companies in the
same region. Metric: net income to common over average common equity, each year 2016 to 2025, from each company's own
10-K XBRL facts (WEC 2018 and 2019 common equity from the filed FY2019 balance sheet, `0000107815-20-000089`: $9,788.9M
and $10,113.4M; script and output in the research folder, `peers.py`, `peers_roe.txt`, `peers_out.txt`):

| Company (CIK) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Ten-year mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WEC (0000783325) | 10.6 | 13.0 | 11.0 | 11.4 | 11.5 | 12.0 | 12.4 | 11.3 | 12.3 | 11.6 | 11.7 |
| Alliant (0000352541) | 9.5 | 11.1 | 11.7 | 11.4 | 11.3 | 11.3 | 11.2 | 10.8 | 10.0 | 11.3 | 11.0 |
| Xcel (0000072903) | 10.4 | 10.2 | 10.7 | 10.8 | 10.6 | 10.6 | 10.8 | 10.3 | 10.4 | 9.4 | 10.4 |
| CMS (0000811156) | 13.5 | 10.6 | 14.3 | 13.9 | 14.4 | 22.2 | 12.1 | 12.0 | 12.6 | 12.2 | 13.8 |

(CMS 2021 includes the gain on the sale of its bank; WEC 2017 includes that year's deferred-tax remeasurement.) WEC's
consolidated return runs about two points above its Wisconsin allowed 9.80 percent, and the filings point to the reasons:
We Power's 12.7 percent lease return, WECI's tax credits, ATC, the Wisconsin earnings above the allowed figure, and
holding-company debt (corporate segment interest expense $359.0M in 2025, against the utilities' 53 percent allowed equity
component). Every company in the field earned roughly 10 to 14 percent on book equity in every year of the span, and every
one spent more on capital than its operating cash brought in, in most years (`peers_out.txt`).

**The field's returns over the last full cycle, judged in words.** Ordinary to decent and remarkably steady, set by
commissions, for all four. The castle protects a return, not a high return: "there’s no way we get rich on our utility
investments. But there’s no way we get poor, either." **[M2009-104]**. The framework sends a standing castle that protects
only ordinary returns to OUT, with its stated exception: a return set by a regulator is carried to Q3 as a second best
(Q2, What it rules OUT, citing **[M2009-104]** and **[L2009-012]**). WEC's return is set by regulators; it is carried to Q3.

**Is the castle open, or its future unjudgeable?** Open: no, on the Wisconsin evidence (statutory territory, no retail
choice bill, rate orders granted, sharing paid). Unjudgeable: the OPEN tension the framework carries, that the regulatory
compact can break **[L2023-011]**, **[M2024-011]**, is real and is shown in miniature in Illinois; but the deciding part's
record across the span read is the opposite, and the rows' own reading is that the allowed return is "almost certain"
**[M2010-037]** for a utility that behaves. I judge the Wisconsin castle standing for the regulated return; Illinois is
weighed against at Q3 and Q7, not decisive.

- **VERDICT: IN**, for a regulated castle that protects a modest allowed return, carried to Q3 as a second best
  **[M2009-104]**, **[L2009-012]**, **[M2010-037]**; Illinois and the compact's fragility weighed against **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **The grade.** This is the business the rows grade second: "It takes more money, but the rate at which you invest —
  reinvest — the money to get that growth is a very satisfactory rate" is the second-best case **[M1998-081]**, accepted
  "as the second-best choice, still a good choice" **[M2018-055]**, on the condition of "decent returns on the incremental
  sums they invest" **[L2009-012]**. The utility's own form of it: "To earn more, their owners must invest more."
  **[L2011-019]**.
- **Return on the capital actually needed** (operating earnings after depreciation against capital employed, the measure the
  row gives for a utility: "It’s measured by the operating earnings after depreciation." **[M2014-086]**). Operating income
  plus equity earnings of ATC ($M, filed income statements, `0000783325-26-000018` and `0000107815-23-000100`; 2020 from
  the XBRL of `0000107815-21-000079`): 2020 1,881.9 (1,706.1 + 175.8); 2025 2,460.7 (2,244.9 + 215.8). Capital employed
  (all debt including short-term and finance leases, plus total equity): end-2020 about $24,953M (long-term debt with current
  maturities and finance leases 12,513.9, short-term 1,776.9, equity 10,662.5); end-2025 $36,367M (18,498.1 + 1,519.4 +
  372.0 + 1,924.7 debt; 14,052.8 equity). Pre-tax return on all capital: 7.5 percent in 2020, 6.8 percent in 2025, goodwill
  of $3,052.8M included. **The added capital**: $11,414M more capital produced $578.8M more pre-tax operating earnings, about
  **5.1 percent pre-tax** on the increment, before the company's tax and below the 30-year Treasury today. On common
  equity the same years show 11 to 12 percent (Q2's table), because about 62 percent of the capital is debt at the
  consolidated level (Q4). A high return on equity is read for "leverage" before it is credited **[L1994-009]**; return on
  equity "could make it almost any number you want if we just used enough leverage" is Munger's warning about financial
  practice **[M2001-054]**. Some of the added capital is construction work not yet in rates (AFUDC, a $21.0M tax item in
  2025), so the increment's return is understated somewhat; it is not understated by half.
- **Reinvestment to stand still, and to grow** **[L2000-035]**, **[L1999-024]**. Depreciation and amortization 2021 to 2025:
  1,074.3, 1,122.6, 1,264.2, 1,354.5, 1,478.5. All capital spending (net cash used in investing, rabbi-trust securities lines
  removed: capital expenditures, the acquisitions of wind and solar farms, contributions to ATC): 2,330.5, 2,657.8, 3,558.2,
  3,802.5, 4,874.7. Spending above depreciation averaged $2,186M a year, 1.7 times depreciation. The forward plan is larger:
  $5,018.1M, $6,949.5M and $6,965.6M of capital in 2026, 2027 and 2028 (Item 7, Significant Capital Projects), against
  depreciation near $1.5 billion. The maintenance guess **[M2000-144]** is depreciation: a regulated rate base stands still
  when spending equals depreciation, so depreciation is here what "we spend [...] simply to stay in the same economic place"
  means; the filing's own reliability programme ($11.8 billion of gas and electric distribution 2026 to 2030, about $2.4
  billion a year) suggests the true stand-still figure may be higher than depreciation, as the rows found for a railroad
  **[L2023-009]**. That is weighed against.
- **The growth arithmetic.** Segment net income grew from $1,199.9M (2020) to $1,557.5M (2025), 5.4 percent a year, while
  capital employed grew 7.8 percent a year: "we’re not earning a higher rate of return on capital than we were when we
  started. We just put way more capital into the business" **[M2023-081]**. Whether growth is good "depends on what we earn
  on that incremental $130 million over time" **[M2001-019]**: here about 5 percent pre-tax on all capital, 12 percent on the
  equity slice after the debt. The spending is close to compulsory: coal retirements under EPA rules, the ICC's order to
  retire cast iron pipe by 2035 "could subject us to civil penalties", and the data-centre load the company has undertaken to
  serve; the rows avoid "places where there was a lot of compulsory reinvestment just in order to stand still"
  **[M1997-016]**.
- **WEIGHS AGAINST**, narrowly. The capital-heavy business is admitted as a second best **[M2018-055]**, **[L2009-012]**, and
  the regulated return on the equity slice is decent and dependable **[M2009-104]**; but the added capital earns about 5
  percent pre-tax before leverage **[M2014-086]**, the spending is largely compulsory **[M1997-016]** and is about to double,
  and the owners must keep investing to earn more **[L2011-019]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (`tools/run.py`'s XBRL table, read
against the filed balance sheets of FY2025 `0000783325-26-000018` and FY2019 `0000107815-20-000089`; $M):

| Year-end | Total assets | Equity (2019 on incl. NCI) | Goodwill | Receivables | Long-term debt (non-current) | Short-term debt | Retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 30,123 | 8,960 | 3,046 | 1,242 | 9,158 | 860 | 4,614 |
| 2017 | 31,590 | 9,492 | 3,054 | 1,351 | 8,747 | 1,445 | 5,177 |
| 2018 | 33,476 | 9,789 (common, filed) | 3,053 | 1,281 | 9,976 | 1,440 (CP) | 5,538 |
| 2019 | 34,952 | 10,255 | 3,053 | 1,176 | 11,171 | 831 | 5,928 |
| 2020 | 37,028 | 10,662 | 3,053 | 1,203 | 11,673 | 1,777 | 6,330 |
| 2021 | 38,988 | 11,113 | 3,053 | 1,506 | 13,472 | 1,897 | 6,775 |
| 2022 | 41,872 | 11,617 | 3,053 | 1,818 | 14,656 | 1,647 | 7,265 |
| 2023 | 43,940 | 12,072 | 3,053 | 1,503 | 15,367 | 2,021 | 7,613 |
| 2024 | 47,363 | 12,802 | 3,053 | 1,669 | 17,178 | 1,117 | 8,084 |
| 2025 | 51,518 | 14,053 | 3,053 | 2,063 | 18,498 | 1,925 | 8,494 |

What moved and why. Assets rose 71 percent in nine years, nearly all of it plant (net plant $38,278.1M at 2025-12-31).
Equity rose 57 percent, of which retained earnings supplied $3.9 billion and new shares about $0.9 billion (2024 and 2025,
the first issuances since the period read began; 2020 to 2022 the company bought shares in the market to supply its plans).
Debt rose faster than equity: all debt (long-term with current maturities and finance leases, plus short-term) about $10.2
billion at 2016 to **$22.3 billion** at 2025, so debt went from about 53 to about 62 percent of debt plus common equity.
Goodwill is flat at $3,052.8M, all from the 2015 Integrys deal: no acquisition by shares since, and no impairment of it.
Cash is never more than $85M: the business runs on commercial paper and the capital markets, and current liabilities exceeded
current assets by $2,308.7M at 2025-12-31 (Item 7). Receivables against revenue: 16.6 percent (2016, $1,242M on $7,472M) to
21.0 percent (2025, $2,063M on $9,800M); the filer ties the 2025 rise to higher collections due under the new Wisconsin rates
and to gas costs; not a tell on its own. Regulatory assets $3,156.3M and regulatory liabilities $4,121.3M at 2025; deferred
income taxes $5,891.7M, which the rows do not count as equity in a utility: "I don’t think I would look at that as a
hidden form of equity" **[M2015-030]**. What the figures cannot say: whether the $3.0 billion of Illinois QIP capital still
in reconciliation (Item 7) will all stay in rate base (the February 2026 settlement removes $130M of it) **[M2025-032]**.

**The real costs.**
- *Depreciation* is a real cost **[R1996-023]**, **[L2015-004]**, and here a fair proxy for stand-still spending in a regulated
  rate base **[M1998-127]**, with the caution of Q3 that the stand-still figure may be higher.
- *Stock pay* is expensed (proxy and Note 11); performance units are cash-settled; subtracted in owner cash.
- *The recurring "one-time" charge.* Illinois charges in three straight years: impairments of $178.9M (2023), $12.1M plus a
  $25.3M disallowance charge (2024), and $205.0M (2025, the settlement: $130.0M impairment and $75.0M of revenue reversed)
  (cash-flow statement and Item 7). The FY2025 earnings release headlines GAAP first ("net income based on generally
  accepted accounting principles (GAAP) of $1.6 billion, or $4.81 per share") and then features "adjusted earnings for 2025
  rose to $5.27 per share – an increase of 8.0 percent over 2024 adjusted earnings of $4.88", excluding the Illinois
  charges of both years (8-K `0000783325-26-000011`). Telling owners year after year "Don't count this" for adjustments a
  business keeps making "is misleading" **[L2016-007]**; "a management that regularly attempts to wave away very real costs
  by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**. Two years running is a habit beginning.
- *Guidance and targets.* Annual EPS guidance ($5.51 to $5.61 for 2026, reaffirmed 2026-07-29, 8-K `0000783325-26-000080`)
  and a long-term projection: "long-term EPS growth over the next five years is projected to be 7 to 8 percent on a compound
  annual basis" (8-K `0000783325-26-000011`); 2025 adjusted EPS of $5.27 landed on the top of the $5.17 to $5.27 guidance
  range (proxy). "the scourge of earnings "guidance"" **[L2019-006]**; "we become downright incredulous if they consistently
  reach their declared targets" **[L2002-041]**. Recorded as a weighing against and carried to Q5.
- *Tax.* The effective rate was 7.1 percent in 2025 and is guided to 5.5 to 6.5 percent for 2026, because of production tax
  credits ($261.3M in 2025, up from $81.3M in 2021, tax-rate reconciliations) that the company sells for cash under the
  IRA's transfer rules; cash taxes were net receipts of $264.2M (2024) and $281.3M (2025). The credits run ten years per
  project and new wind and solar credits end under the OBBBA deadlines (Item 7). Priced at Q7 under "Whose tax".
- *EBITDA.* Not featured in the releases read. Coverage the rows' way, pre-tax earnings over interest **[L2012-002]**:
  (1,409.7 + 322.9 + 515.1) / 515.1 = 4.4 times in 2022; (1,673.5 + 895.1) / 895.1 = **2.9 times** in 2025. Falling.
- *What the accounts say of management's character.* The statements are clear and the charges are described in plain words
  where they arise **[M1994-018]**; nothing builds up in prepaid or deferred accounts out of line with the business
  **[M1995-064]**; the earnings figure the owners are steered toward leaves out a cost that has recurred.
- **VERDICT on the accounts: IN** (no confusion: the accounts can be followed line by line **[M1995-063]**; no suspicion
  from the statements themselves **[M1995-065]**); **WEIGHS AGAINST** for the adjusted figure featured over recurring Illinois
  charges **[L2016-006]**, **[L2016-007]** and for guidance met at the top of its range **[L2019-006]**, **[L2002-041]**,
  carried to Q5 (section A convention). The recast owner cash goes to Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. *How they run it, against the hand dealt:* the hand is a regulated monopoly in
  Wisconsin and a gas utility in Chicago with an old cast-iron system and a hostile commission. In Wisconsin the record is
  good: rate orders granted, returns above the allowed 9.80 percent (sharing paid), coal retirements on schedule, large
  customers signed; the same Wisconsin net income figure grew from $706.5M to $1,054.8M in five years. In Illinois the
  record is poor on the evidence: a pause ordered by the ICC in November 2023, capital disallowed in 2023 and 2024, a UEA
  refund the company appealed and lost through the Illinois Supreme Court (March 2025), and a $205M settlement in 2026 that
  takes $130M out of rate base for good. The peers' returns (Q2) show WEC's consolidated return at or above the field's
  middle for ten years. *How they treat the owners:* read in the proxy below and at Q6, Part B **[M1994-009]**.
- **The integrity record, with the habits carried from Q4.** Searched in the 10-K (Item 3, Notes 24 and 26, risk factors) for
  investigations, subpoenas, penalties and class actions: none reported against the company or its officers; the Illinois
  matters are rate reconciliations of cost recovery (prudence of capital and of bad-debt recovery), settled with the
  Attorney General as a party to the regulatory proceedings, not findings of dishonesty (8-K `0000783325-26-000006`). The
  releases headline the GAAP figure first and state the adjustments in plain words with the amounts (8-K
  `0000783325-26-000011`). Against: the adjusted figure is featured two years running over recurring Illinois charges, and
  guidance is given and met at the top of its range (Q4); the rows read such things as "things that they do in public in
  relation to their investors and the promises they make" **[M2004-067]**, and predictions "corrode CEO behavior"
  **[L2000-039]**. Read together: the habits are those of a company that sells a steady growth rate to investors; the
  record contains no misleading statement, no restatement, no reserve that moves, and the charges that spoil the steady
  rate were taken, disclosed and quantified in the year they arose. I find doubt about owner orientation (carried to Q6,
  Part B), not about honesty. "If you’ve got doubts, forget it." **[M2013-088]** is applied to the honesty question and is
  not met on this record.
- **Love of the business.** Not separately visible from outside for a hired management of a utility holding company; the
  chief executive (Scott Lauber, in the job since 2022, previously chief financial officer) and the board's long-tenured
  former chief executive as chairman until May 2026 (proxy) suggest continuity, not a seller's motives. No inference drawn.
- **Ability.** WEIGHS FOR in Wisconsin (the deciding part) and AGAINST in Illinois.
- **VERDICT on integrity: IN** **[M2013-088]** (applied on doubt; doubt found about pay and investor habits, not about
  honesty); **ability WEIGHS FOR** on the deciding part **[M1994-008]**, with the Illinois record weighed against.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[M1994-061]**, **[R1995-009]**, with the market leg checked against value **[R2009-002]**. 2021 to 2025:
  net income to common $7,124.8M, dividends $4,960.9M, retained **$2,163.9M**; new shares sold for cash $925.3M (2024 and
  2025). Market value: $92.03 x about 315.4M shares = about $29.0 billion at 2020-12-31 (year-end closes from the aggregator,
  `prices_yearend.txt`; the share count is the weighted basic count of 2023, there being no issuance from 2020 to 2023) and
  $105.46 x 325.46M = $34.3 billion at 2025-12-31: about $5.3 billion of market value for about $3.1 billion retained and
  raised. On the value leg, owner cash after maintenance per share (Q7's central series) rose from $2.73 (2021, a depressed
  year) to $4.89 (2025). The test is met over the five years, on both legs, though with less to spare per share than in
  aggregate (price to book fell from about 2.7 to 2.5).
- *Buybacks.* None as a capital-allocation programme. Shares were bought in the market in 2020 to 2025 ($99.2M, $33.1M,
  $69.2M, $16.6M, $3.2M, $1.3M) "to satisfy requirements of our stock-based compensation plans" (10-K
  `0000107815-23-000100`, Item 7) at prices in the $80s to $100s, above the bottom of the Q7 range ($67.70, written back
  from Q7): buying "to cover options [...] isn’t the best reason to buy in shares" **[M2014-008]**. Weighs against, small.
- *Issuance.* $3.0 billion at-the-market programme with forward sales (October 2025), succeeding a $1.5 billion programme of
  August 2024; 3.5M shares sold in the first half of 2025 alone and 6.4M shares sold forward at about $111 to $115 (10-Q).
  Value given against value got **[R1995-010]**: the shares are being sold above the whole Q7 range (top $78.29 at the
  sovereign), which by the rows' own truism does not harm continuing holders, since the harm is to "issue shares beneath
  that figure" **[M1996-013]**. But a programme that sells shares continuously to fund a capital plan larger than the
  company is the pattern the rows distrust: "we have never invested in companies that are hell-bent on issuing shares"
  **[L2014-015]**. Serial issuance is a candidate second STOP the framework leaves unresolved (Q6, Part A); here it is
  weighed: the issuance is modest against the market value (about 2 percent a year) and is the regulated utility's way of
  holding the allowed equity share, not a promoter's, but it is ongoing and growing.
- *Dividends.* $1,147.8M in 2025, about 74 percent of net income, raised 6.7 percent for 2026, the 23rd consecutive rise
  (8-K `0000783325-26-000011`), while the company sells new shares and borrows to fund capital. The policy is clear and
  consistent **[L2012-015]**; whether it is rational for a company that cannot fund its own investment is the question: the
  owners are paid a dividend in part with money then raised from them and their neighbours. The rows' rule is that a
  company "that expects to regularly earn more than it can profitably employ in its business, should be paying out
  dividends" **[M2004-089]**; WEC is the opposite case.
- *Deals.* No merger since Integrys (2015); acquisitions are of wind and solar farms for cash (Q7). No all-stock deal: the
  narrower STOP does not arise **[L2009-019]**.
- **Part A WEIGHS AGAINST**, mildly: the retention test is met **[R1995-009]**, but the capital is raised as fast as it is
  paid out, the dividend is part-funded by new shares **[M2004-089]**, issuance is continuous **[L2014-015]**, and the small
  purchases were for plan shares above value **[M2014-008]**.

**Part B: the pay, the board, the owners** (proxy `0000783325-26-000035`).
- *Annual bonus (STPP).* 75 percent on EPS, 25 percent on an "Adjusted Cash From Operations"; for 2025 the EPS bands ran from
  $5.15 (25 percent payout) to $5.25 (200 percent), the cash band from $2,675M (target) to $2,800M (maximum). GAAP EPS was
  $4.81, below the lowest band; the committee measured EPS on the adjusted $5.27 because the Illinois settlement charge "is
  not indicative of WEC Energy Group’s operating performance", and paid **200 percent** of target on the financial goals.
  The adjusted cash figure was $3,400.0M against a $2,675M target, so the cash goal was set about $725M below the outcome.
  Pay that excludes a loss the company's own regulated business incurred, and a cash bar set far below what the business
  delivered, fail "a partner in both directions, not just on the upside" **[L1994-020]** and the chimpanzee test of where the
  bar sits **[M2004-097]**. Paying on the EPS growth the company guides to ties pay to the number promised to investors,
  which is the habit carried from Q4 **[L2019-006]**.
- *Long-term pay.* Performance units, cash-settled, vesting on total stockholder return against a peer group, with up to 25
  percent added for the company's P/E ratio against peers; restricted stock and options as well. Pay on relative stock
  price is an option on the market's mood, the "option on $300 million worth of S&P futures" objection **[M2000-062]**, and
  not tied to what the person controls **[M2003-019]**.
- *Size and form.* Chief executive total compensation $12,188,492 in 2025, 92 times the median employee; a retention credit
  of $347,288 and tax gross-ups on perquisites (proxy, Summary Compensation Table and notes). The size is not decisive:
  the rows put "the real sin" in having a mediocre manager **[M1997-045]**; the design is the finding here.
- *The board.* All nominees but the chief executive independent; the former chief executive was non-executive chairman to
  May 2026, when the board "intends to appoint Director Lauber as Chairman of the Board" (proxy). The rows warn of the
  chief executive who also chairs **[L2014-026]**.
- *Owners as partners.* Hedging and pledging prohibited; ownership guidelines; clawback policy (proxy). Releases and the
  10-K are candid about the Illinois losses in the year they arose **[M1998-036]**.
- **Part B WEIGHS AGAINST**: bonus paid at maximum on a figure that excludes the year's regulatory loss **[L1994-020]**, an
  easy cash bar **[M2004-097]**, long-term pay on relative stock price **[M2000-062]**, and the chief executive about to
  chair **[L2014-026]**.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**, as a range (the Q7 range
convention and its specifics; the floor of about ten percent **[M2003-149]**, **[M1994-004]**, **[L2002-020]**). Arithmetic
in `Test Runs/_research 2026-10-27 WEC/q7.py`, output in `q7_out.txt`; every input from the filed statements named in
Step 0.

**The basis: a regulated utility, equity-only central.** The deciding part (Wisconsin) earns a return its regulator allows
on its invested capital **[M2010-037]**, so Q7's central figure is owner cash after interest and after the company's tax,
against the market value of the shares; the all-equity figure is beside it **[L2017-012]**. The long-term debt raised to
fund the fixed assets is credited against the growth spending only, capped at the deciding part's allowed debt share
(Q7, The regulated utility, 2026-10-18 and 2026-10-23).

**Owner cash after every real cost** **[L2021-003]**, **[L2015-004]**: operating cash (already after interest paid and cash
taxes) less stock pay less the maintenance guess, depreciation (Q3) **[M2000-144]**, **[L2000-035]** ($M):

| | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year average |
|---|---|---|---|---|---|---|
| Operating cash (filed) | 2,032.7 | 2,060.7 | 3,018.4 | 3,211.8 | 3,379.4 | |
| Less stock pay | 15.7 | 34.8 | 9.7 | 39.3 | 48.2 | |
| Less depreciation and amortization (maintenance guess) | 1,074.3 | 1,122.6 | 1,264.2 | 1,354.5 | 1,478.5 | |
| Owner cash after maintenance, literal | 942.7 | 903.3 | 1,744.5 | 1,818.0 | 1,852.7 | **1,452.2** |
| Less PTCs (tax at statutory, "Whose tax") | 81.3 | 107.6 | 168.2 | 200.1 | 261.3 | 163.7 |
| **Owner cash after maintenance, central** | 861.4 | 795.7 | 1,576.3 | 1,617.9 | 1,591.4 | **1,288.5** |
| All capital spending (investing, securities lines removed) | 2,330.5 | 2,657.8 | 3,558.2 | 3,802.5 | 4,874.7 | 3,444.7 |
| Owner cash after all spending (the depreciation variant's twin) | (313.5) | (631.9) | (549.5) | (630.0) | (1,543.5) | **(733.7)** |

- *Whose tax.* The company pays tax well below the statutory rate (7.1 percent effective in 2025 against 21 percent federal
  plus about 6 percent state) because of production tax credits that run ten years per project and, under the OBBBA, end
  for new wind and solar; by the convention, owner cash is computed with the credits taken out and their present value
  added at the long rate. **CONVENTION of this run:** the shelter is the five-year average credit ($163.7M) carried ten
  years, $1,244.8M at 5.31 percent and $1,005.9M at 10 percent; rationale: the filings do not give the credit schedule by
  project, and ten years is the life of a credit. Only the PTCs are removed: the other reconciling items (excess deferred
  tax amortization, AFUDC equity) are returned to customers or are regulatory gross-ups, and deferred taxes on depreciation
  are left in operating cash as the timing difference of a growing regulated rate base, said so **[M2015-030]**.
- *Cycles, specific (a).* 2021 is aberrational on the filer's own description: "Due to the cold temperatures, wind, snow and
  ice throughout the central part of the country during February 2021, the cost of gas purchased for our natural gas
  utility customers was temporarily driven higher" and the company sought recovery of "an additional $322 million" (10-K
  `0000107815-23-000100`, Item 7); the under-recovery was collected in 2022. A regulated utility has no business cycle to
  average over; **CONVENTION of this run:** the base without 2021 (2022 to 2025, $1,395.3M) is shown beside the literal
  window; rationale: specific (a) names the aberrational end year but its remedy, a full cycle, does not exist here.
- *Growth shown, and the cap, specific (f).* On the central series 2021 to 2025, 16.6 percent a year (literal series 18.4
  percent), inflated by the depressed 2021. Carried ten years it would make owner cash 40.5 percent of sales (sales carried
  at their own growth), against a highest share in the filings read of 18.8 percent (central series, 2024) or 21.1 percent
  (literal, 2024); it traces to an absurdity **[M1999-067]**, so the growth carried is the business's own sales growth over
  the same window: revenues $8,316.0M (2021) to $9,800.1M (2025), **4.19 percent a year**, below the discount rate. Both
  rates are written down here as the convention asks.
- *Acquisitions, specific (c).* The cash paid for wind and solar farms (Jayhawk, Thunderhead, Sapphire Sky, Samson I, Maple
  Flats, Delilah I and Hardin III by WECI; West Riverside, Red Barn and Whitewater by the utilities) is in all capital
  spending above and so in the growth spending; total growth is credited (the default pair). Purchases over the window
  were $2,916.7M (WECI $2,501.6M, the utilities $415.1M), 45 percent of the $6,442.7M of central owner cash before purchases:
  below half, so not a serial acquirer by the convention's test (it exceeded half in 2023 and 2024 taken alone). No deal signed and unclosed at the price date is material (the Whitetail wind share and the Point
  Beach PPA are a purchase and a contract, the PPA pending PSCW approval from 2030).
- *Working capital, specific (d):* inside operating cash as filed; the 2021 to 2022 gas-cost draw is the aberration above.
- *Growth spending and the debt credit, specific (e) and the utility rule.* Maintenance-only is central. Growth spending
  (all spending less depreciation) averaged **$2,185.9M**. Long-term debt (non-current, current maturities and finance
  leases) rose from $12,513.9M at 2020-12-31 (11,672.8 + 785.8 + 55.3, XBRL of the FY2020 and FY2021 10-Ks, current
  maturities including the current finance lease) to $20,312.8M at 2025-12-31 (18,498.1 + 1,519.4 + 372.0, less the WEPCo
  Environmental Trust securitization bonds of $76.7M repaid from a dedicated customer charge, left out with the charge):
  **$1,559.8M a year**. The credit is taken against the growth spending of the regulated businesses only, the WECI
  purchases of contracted renewables (average $500.3M) staying on the all-equity basis as the rule requires of unregulated
  renewables: $1,685.6M x the cap. **Cap: 47 percent**, the debt share left by the 53.0 percent common equity component the
  PSCW allows WE, WPS and WG (Item 1, E); UMERC's 50 percent (MPSC) sits in the same segment and is small, and the filing
  gives no rate base by company to weight it, so the Wisconsin figure is used, said so. Credit **$792.2M a year** (the cap
  binds; the debt actually raised was larger). Growth spending charged to the equity in the growth case: **$1,452.1M in year
  one, $2,101.1M in year ten** (grown at 4.19 percent with the growth), none after year ten.

**The range at the sovereign 5.31 percent, central (equity-only)**, $M and per share on 325.849M shares:
- No-growth case: 1,288.5 / 0.0531 + 1,244.8 shelter = 25,512, **$78.29**.
- Growth case: owner cash growing 4.19 percent for ten years less the net growth spending, then flat with no growth spending
  = 22,060, **$67.70**.
- The growth bought is worth less than its cost at this rate (the inversion of specific (e), "growth can destroy value"
  **[L2000-023]**), so the growth case is the bottom and the no-growth case the top: **$67.70 to $78.29**, a width of 1.16
  to 1. Beside: the literal window (credits left in, no shelter) $77.12 to $83.93; the base without 2021, $76.34 to $84.46;
  the debt credit taken on all growth spending including WECI, $74.51 to $78.29; the all-equity basis (owner cash before
  after-tax interest of $475.4M a year at 27 percent, growth spending with no credit, less net debt of $22,929.7M at
  2026-06-30: long-term debt 19,216.3, current maturities 1,413.5, finance leases 415.8, short-term debt 1,934.1, less cash
  50.0, 10-Q; operating leases left out; no later borrowing found in the 8-Ks), $12.86 to $35.40. Owner cash after all
  spending is negative in every year; on that series alone there is no positive value without new money.

**The floor, tested first.** At $111.12 the market value is $36,208M. The central owner cash is a 3.56 percent return on it
(the literal window 4.01 percent; the best three years, 2023 to 2025 literal, 4.99 percent). No case in the range earns the
floor of about ten percent at the price; none earns even the 5.31 percent sovereign. The price is also above the top of the
range, which closes OUT by the floor convention. "there’s just a point at which we drop out of the game" **[M2003-149]**.
The width test is not needed. Nothing here needs a pencil to see **[M2009-005]**.

**Value range:** $67.70 to $78.29 a share (equity-only, central) against $111.12.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged, after
the company's own tax: no-growth $13,891M ($42.63), growth $7,706M ($23.65); **fair price $33.14 a share on the equity-only
basis, the central figure for a regulated utility.** The all-equity figure beside it is **not positive** (-$29.34: at ten
percent the owner cash before interest is worth less than the net debt). Beside, for the reader: the literal window gives
$35.91; the base without 2021 gives $36.96; with the forwards physically settled (6.392M more shares, $725.6M more cash at
the 2026-06-30 settlement values) the central figure is $34.69. Growth spending charged: $1,452.1M in year one, $2,101.1M
in year ten, none after (specific (e)). Utility debt credit: long-term debt increase $1,559.8M a year, against growth spending
only, cap 47 percent (the deciding part's allowed debt share, PSCW), credit $792.2M a year. No cheap price is reported.

*(Written back to Q6: the bottom of the range, $67.70, is the line the buyback test reads; the plan-share purchases were made
above it.)*

- **VERDICT: OUT**, at the floor: no case earns about ten percent at the price **[M2003-149]**, and the price sits above the
  whole range **[L2013-012]**. The rows expect only "decent returns on the incremental sums" of a utility **[L2009-012]**,
  and "no way we get rich on our utility investments" **[M2009-104]**; at $111 the buyer is paid less than the bond.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** (the floor): value range $67.70 to $78.29 a share (equity-only, central, at the 5.31 percent
sovereign) against $111.12; fair price $33.14 (equity-only, central), all-equity not positive. Q1 IN, Q2 IN (regulated
castle, Wisconsin decides), Q3 weighs against narrowly, Q4 IN on the accounts and weighs against, Q5 integrity IN and
ability weighs for, Q6 weighs against in both parts.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Bears on Q8 (the alternatives).** The 30-year Treasury yields 5.31 percent (2026-10-26); the central owner cash return at
  the price is 3.56 percent, the literal 4.01 percent.
- **Bears on Q9 (debt and exposures).** All debt $22.3 billion at 2025-12-31 and $22.98 billion gross at 2026-06-30 (10-Q),
  about 62 percent of debt plus common equity at year-end 2025, up from about 53 percent in 2016; pre-tax coverage 4.4 times
  (2022) falling to 2.9 times (2025); current liabilities above current assets by $2,308.7M; commercial paper $1,924.7M at
  year-end, backed by bank facilities (Item 7); holding-company debt serviced from subsidiary dividends, with the utilities
  (other than UMERC and MGU) barred from lending to the parent (10-Q); junior subordinated notes of 2024 and 2025 that rating
  agencies count partly as equity, so the company presents an adjusted capitalization (10-Q, non-GAAP note); a credit
  downgrade "could [...] require the posting of collateral" (Item 1A). Diversity of the earning sources: eight regulated
  utilities in four states plus ATC and WECI (Item 1); the Wisconsin share is above half. Exposure named in the filing:
  very large data-centre customers (Microsoft, Vantage) for whom the company plans generation under tariffs pending at the
  PSCW. The Point Beach PPA (8-K `0000783325-26-000095`) is a 20-year purchase commitment from 2030 and 2033, pending approval.
- **Bears on Q10.** None beyond the above.
- **Bears on Q12.** Coal still about 30 percent of the electric supply (Item 1, 2025), with a stated plan to end coal by
  2032; the extension of Oak Creek 7 and 8 into 2027 (8-K `0000783325-26-000040`). Not weighed.
- **Integrity facts:** none found beyond those answered at Q5 (the run reached Q5 and answered them).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `49135a48`); written question by question; committed after Step 0
      and Q1, Q2, Q3 with Q4, Q5 with Q6, and Q7 with the close. One departure: the Q6 buyback line cites the bottom of the Q7
      range ($67.70) in the Q5 and Q6 commit, because the Q7 arithmetic (`q7.py`, `q7_out.txt`) was already in the research
      folder; Q7's close was committed after it.
- [x] Dispatched run: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is
      the dispatcher's (operator rule 10). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the accidental sightings are
      declared under Contamination at the top and were not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_ids.py` in the research folder (every id exists;
      every quoted fragment beside an id is in that row; no E-ids). Every filing fact carries its accession or names the
      filing whose accession is in Step 0.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price and the year-end closes from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations line, and at each question) **[M1997-127]**; the facts found for
      later questions are under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its capex line was replaced by the filed statement's
      investing lines (it omits the acquisitions and the ATC contributions).
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the research folder,
      `check_framework_out.txt`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **Whose tax, for a utility.** The convention prices "carryforwards or credits that run out inside ten years"
at the statutory rate with the shelter added back, but a regulated utility's tax line also carries items that pass to
customers (excess deferred tax amortization, regulated-renewable credits flowing through rates) and deferred taxes that
are a permanent feature of a growing rate base; the text does not say which of these the statutory computation reaches. I
removed only the production tax credits and added a ten-year shelter at their five-year average, confessed as a
CONVENTION of this run; it moves the central range by about $5 a share and the fair price by about $3, not the box.
(2) **Specific (a) without a cycle.** The filer itself calls the first window year (February 2021 gas costs) extraordinary,
but a regulated utility has no business cycle to average over; I showed the base without 2021 beside, confessed. (3)
**Specific (f) for a utility.** Cutting the shown growth to revenue growth uses a figure that, for a utility, moves with gas
and fuel prices passed through to customers (revenue fell in 2023 and 2024 on lower gas prices while rate base grew); the
cap is mechanically met but measures fuel prices as much as the business. It does not change the box: at the price no
growth rate the window could support reaches the floor. (4) **The utility debt credit and unregulated growth spending.**
The rule says unregulated renewables stay on the all-equity basis and the credit is against growth spending, but not
whether the unregulated part's growth spending is to be taken out of the base the cap applies to; I took WECI's purchases
out and showed the other reading beside ($35.85 against $33.14). (5) **The growth case's year one.** The text says the
growth spending "grows at the growth rate carried", not whether year one is the window average or the average grown one
year; I grew both owner cash and growth spending from year one (`q7.py`), which is the same treatment on both sides.
