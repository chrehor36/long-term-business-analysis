# Company Run, THE SOUTHERN COMPANY (NYSE: SO), 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no SO row).*

**Run record.** Dispatched blind analyst; a RESUME of a run started 11:31 today and stopped by a usage limit (the template had
been copied with its title line only; nothing committed). Resumed the same day: the framework read again in full by this
session (notes in `Test Runs/_research 2026-10-26 SO/notes.md`), every fetch done fresh, the earlier cache file not used.

**Contamination declared.** Seen by accident and not used: the repository's git status and recent commit subjects shown at
session start (another company's v5 run and its fold, a research folder of another company); the memory index line that
reports a count of gate-clearers and holding reviews owed (it names no company). Nothing about this company, under any
name, was seen in any other run file, holding review, `PORTFOLIO.md`, the queue or the reading list; none was opened,
listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $92.69 (close 2026-10-26; Yahoo Finance chart endpoint via `tools/sources.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: **1,150,362,966** common shares of The Southern Company, par $0.01, outstanding at June 30, 2026
  (10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0000092122-26-000054`; `python Screens/cover_shares.py SO`).
  The other lines the script prints (30,537,500; 9,261,500; 1,121,000; 1,000; 100) are the common shares of the subsidiary
  registrants (Alabama Power, Georgia Power, Mississippi Power, Southern Power, Southern Company Gas), all owned by Southern
  Company; the script mislabels them as note series. They are not added. One class only.
  *Check against issued less treasury:* the 10-Q states 31.1 million shares issued in the first half of 2026, chiefly by
  forward-sale settlements; the year-end 2025 issued count tagged in XBRL (1,100.0M) is a rounded legacy tag and is not used.
  *After the 10-Q:* forward sale contracts sold and not settled total 11,483,995 shares at June 30, 2026, plus 1,340,454 sold
  after that date (10-Q, note on the equity distribution agreement), settleable to June 2028 at about $92 to $98 a share; they
  bring cash in at settlement and are not in the count. Equity units (2025 Series A Corporate Units, stock purchase contracts)
  and convertible senior notes (incl. $833.75M Series 2026A and $1,897.5M Series 2026B issued 2026-08-06, 8-K accession
  `0000092122-26-000063`) are potential shares, not counted; stated at Q6.
- **Market cap:** 1,150.363M x $92.69 = **$106,627M**.
- **Sovereign for the earnings currency (USD):** **5.33%**, US Treasury daily par yield curve, 30-year, 10/23/2026 (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-19, accession `0000092122-26-000006` (Items 1, 1A, 7, 8:
  the cash-flow statement, balance sheets, Notes 2, 8, 10, 15, 16); 10-K for FY2023, accession `0000092122-24-000009`
  (cash flows and segments for 2021 to 2023, the Vogtle charges); 10-K for FY2017, accession `0000092122-18-000012` (Kemper
  charges, the SEC investigation); 10-Q for Q2 2026, accession `0000092122-26-000054`; 10-Q for Q2 2020, accession
  `0000092122-20-000057` (the Kemper securities class action); proxy statement filed 2026-04-03, accession
  `0000092122-26-000028`; 8-Ks of 2026-08-03 (`0000092122-26-000058`), 2026-08-06 (`0000092122-26-000063`), 2026-10-22
  (`0000092122-26-000065`, by-law amendment) and 2022-03-18 (`0000092122-22-000010`, the Kemper derivative settlement).
  **One figure cross-checked against the filed statement:** net cash provided from operating activities 2025, $9,802M in the
  consolidated statement of cash flows of the FY2025 10-K (II-73), equal to the XBRL figure `tools/run.py` prints.
  Cross-check two: stock-based compensation. `tools/run.py` prints 73, 56, 48 (an APIC tag); the filed cash-flow statement
  shows "Stock based compensation expense" of 137, 132, 136 for 2023 to 2025 (and 144, 127 for 2021, 2022 in the FY2023
  10-K). **The filed figures are used.**
- `python tools/run.py SO` arithmetic lines only (saved in the research folder's cache): OCF 7,553 / 9,788 / 9,802 (2023 to
  2025), capex 9,095 / 8,955 / 12,737, D&A 4,986 / 5,266 / 6,030; owner cash on the capex basis negative in every year;
  finance-lease principal 18 / 11 / 21; ten year-end balance sheets 2016 to 2025 (read at Q4). The tool's yields, its
  "growth the price assumes" line and every rule or floor it prints are not used (Part VII, the tooling).

**Owner cash, recast from the filed cash-flow statements** (USD millions; `Test Runs/_research 2026-10-26 SO/oc.py`).
Owner cash = operating cash flow, less stock pay, less property additions, cost of removal net of salvage, payments under
long-term service agreements, net contributions to the nuclear decommissioning trusts, other investing outflows and
finance-lease principal (plus the change in construction payables, which the filer reports in investing), less the net cash
paid to minority (tax-equity and partnership) partners. Interest is already out of operating cash (this is the equity-only
basis); tax is the company's own cash tax.

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| Operating cash flow | 6,169 | 6,302 | 7,553 | 9,788 | 9,802 | |
| Capital spending, all of it, cash | 8,287 | 8,721 | 9,850 | 9,780 | 13,346 | 9,997 |
| D&A total (cash-flow statement) | 3,973 | 4,064 | 4,986 | 5,266 | 6,030 | 4,864 |
| **Owner cash, all spending, ex acquisitions** | -2,112 | -2,732 | -2,647 | -309 | -3,880 | **-2,336** |
| Owner cash, all spending, net acquisitions in | -1,195 | -2,457 | -2,483 | 60 | -4,800 | -2,175 |
| **Owner cash after maintenance only** (D&A as the guess) | 2,202 | 1,925 | 2,217 | 4,205 | 3,436 | **2,797** |

Sources: FY2025 10-K cash flows (2023 to 2025), FY2023 10-K cash flows (2021 to 2023); the 2023 column agrees in both.
Acquisitions net of dispositions: proceeds 917, 275, 164, 369 (2021 to 2024); 2025 a business acquisition of 635 and a
purchase of membership interests from minority partners of 286, less 1 of proceeds.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**; for a regulated utility the answer turns on the regulator, not the quotation. The bearing foundation here is
the margin of safety, "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**:
a utility's value is a narrow, computable thing, so a price close to it fails the foundation's attitude before any number is
run. No macro forecast enters: the data-centre load the filer projects is read as the filer's own statement about its
business, not as a forecast of mine. Who is paid to tell you: the company's own guidance and its "adjusted EPS" are the
seller's description of what it sells (Q4, Q5). The analyst's habits: the run hunts "what’s wrong" by writing contrary
evidence down as found. **Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after all capital
spending is negative in every year of the window; the dividend (about $3.0B a year) and growth are paid for with new debt
and new shares; (2) two flagship construction projects in a decade went badly over cost: Kemper (pre-tax charges of about
$3.8B in 2016 and 2017 alone, FY2017 10-K) and Vogtle 3 and 4 (pre-tax loss charges of $1.1B in 2018, $325M in 2020,
$1,252M in 2021 and $216M in 2022, FY2023 10-K); (3) a Kemper securities class action settled for $87.5M and a derivative
action settled with governance reforms; (4) the Georgia base-rate freeze through 2028 (ARP Extension) and the Nicor Gas
disallowances ($96M pre-tax 2023, $63M 2025) show regulators taking from the owners; (5) the CEO's pay is tied to adjusted
EPS against public guidance.

## THE STANDING RULE
The purchase would be made, if at all, with the buyer's own unborrowed money, at a size that cannot end the buyer: "We are
never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. Nothing in this name, a
marketable common stock, can call on the buyer for cash. **The rule is met by the buyer's conduct.** The target's own debt
is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. Southern Company is a holding
  company read by its parts (Q1, A holding company; the parts threshold of Q2). Parts by five-year segment net income
  2021 to 2025 (Note 16, FY2025 and FY2023 10-Ks): the traditional electric operating companies $17,663M, Southern Power
  $1,430M, Southern Company Gas $3,198M, of $22,291M for the reportable segments (79%, 6%, 14%); "All Other" (the parent's
  interest and costs) is a loss of $3,606M over the same years. The part that matters is the traditional electric operating
  companies, and within it Georgia Power (61% of the three companies' net plant at 2025: $50,871M of $83,296M).
- **The key variables and how predictable they are** **[M1998-044]**: (1) the rate base, set by the capital plan the
  commissions certify ($15.9B of construction planned for 2026 alone; 13 GW certified in Georgia, $19.5B of certified
  Georgia Power projects to 2030, Item 1); (2) the allowed return and equity ratio (Georgia Power: retail ROE set point
  10.50%, range 9.50% to 11.90%, equity ratio 56%, held through 2028 by the ARP Extension; Nicor Gas 9.60% on 50%; Virginia
  Natural Gas 9.85% on 49.35%; Item 7 and Note 2); (3) whether the companies earn the allowed return (Georgia Power's retail
  ROE "was within the allowed retail ROE range" in 2023, 2024 and 2025, Note 2); (4) whether the new large loads (about nine
  GW contracted with data centres and other large customers since 2023) arrive and pay their incremental costs; (5) the cost
  and schedule of large construction, where the record is poor (Kemper, Vogtle). The first three are written into
  regulatory orders and can be read; the fourth is a contracted load the filer describes; the fifth is the risk.
- **Do the past statements tell me the future ones?** **[M2008-033]**: largely yes. Revenue follows fuel cost (fuel is a pass-through:
  revenue $29,279M in 2022 against $25,253M in 2023, Note 16), and earnings follow rate base times allowed return; the
  statements show the mechanism year by year.
- **Would the insiders write it down?** **[M2000-105]**: they do. The companies file ten- to twenty-year resource plans
  (IRPs) with their commissions and the commissions certify them; the industry writes its forecast down as a matter of
  regulation. The change in the business (the large-load growth) is a change in quantity on a known mechanism, not in
  technology that makes the economics unknowable.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The doubt is
  the construction record and the regulatory climate, which are questions of Q2 and Q9, not of whether the economics can be
  foreseen. Southern Power (merchant-priced wholesale, 97% of investment under contract through 2030, Item 1) and the gas
  utilities are understood on the same terms and do not decide.
- **VERDICT: IN.** The deciding part's ten-year economics are rate base times an allowed return under orders the filings
  state; important and knowable **[M2006-076]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The castle questions** **[M1995-038]**: what keeps it standing is law, not preference. The Georgia Territorial Electric
  Service Act of 1973 assigns substantially all of Georgia's land to a supplier; Mississippi Power holds "Grandfather
  Certificates" and CPCNs; the gas utilities "do not compete with other distributors of natural gas in their exclusive
  franchise territories" (Item 1, Competition). The lord matters little: the franchise does not depend on genius.
- **The attacker with money** **[M2011-015]**: a rival with any sum could not build a second grid in Alabama or Georgia; it
  would need a franchise the statute does not give. The one opening the filing names is the large new customer: in Georgia
  a new customer of at least 900 kW outside 1973 municipal limits "may exercise a one-time choice" of supplier (Item 1), and
  self-generation and distributed generation compete "in varying degrees" (Item 1; risk factor "Increased competition from
  other companies that supply energy or generation and storage technologies").
- **Pricing power and the agony before a rise** **[M2005-020]**: the price is not the company's to set. It is set by the
  commission in a hearing; base rates in Georgia are frozen for 2026 to 2028 except storm costs (ARP Extension), Alabama
  rates are held stable through 2027 by a consent order of 2025-12-05 (Note 2), and earnings above Georgia Power's 11.90% ROE
  are shared 80% away from the owner (Note 2). Pricing power in the speakers' sense is absent; the protection is the allowed
  return instead.
- **Unit volume and the low-cost position**: volume rises with the territory's population (17 million, 116,000 square miles,
  Item 1) and the contracted large loads. The low-cost position is not shown or claimed; the filer's competitive language is
  "price, availability, technological advancements, service, and reliability" (Item 1).
- **Would the customer still choose it over the low bid?** For the retail customer there is no bid to take; for the large
  new customer in Georgia there is, once, which is where the castle can be attacked.
- **Widening or narrowing** **[M2000-018]**: the franchise has stood through two construction failures. After Kemper the
  Mississippi PSC kept the franchise and the owners took the loss; after Vogtle the Georgia PSC let Georgia Power recover
  $7.562B of construction and capital costs and denied the rest, which the owners took as about $2.9B of pre-tax charges
  2018 to 2022 (Note 2 of the FY2025 and FY2023 10-Ks). The castle stood; the owners' share of the cost overruns was
  real. The data-centre load is widening the volume; it is not yet a full cycle old.
- **What could destroy, modify or reduce it** **[M2000-014]**: the regulatory climate, in the speakers' own error: "the
  regulatory climate in a few states has raised the specter of zero profitability or even bankruptcy" **[L2023-011]**; a
  catastrophe in one territory (hurricanes on the Gulf coast; "A catastrophic event can render a single utility insolvent"
  **[L2005-019]**), mitigated here by three states and a gas business; stranded large-load investment if the data centres do
  not come.
- **The competitor row.** The 10-K names no rival company for the deciding part (Item 1, Competition, speaks of "competing
  suppliers of energy", self-generation and IPPs only; the named wholesale counterparties OPC, MEAG Power and Dalton are
  customers and co-owners, and MEAG Power and Dalton do not file with the SEC). **CONVENTION of this run:** the comparables
  are three SEC-filing, vertically integrated, rate-regulated utility holding companies of the Southeast and mid-Atlantic,
  Duke Energy (CIK 1326160), Entergy (CIK 65984) and Dominion Energy (CIK 715957); rationale: the same business under
  comparable state commissions, read in their own filings. Metric: net income to common over average common equity,
  2021 to 2025, from each filer's 10-K XBRL facts (frames as filed; a year shown NA is not framed in the facts):

  | | 2021 | 2022 | 2023 | 2024 | 2025 | span, as available |
  |---|---|---|---|---|---|---|
  | Southern (`0000092122-24-000009`, `-25-000018`, `-26-000006`) | 8.6% | 12.1% | 12.9% | 13.6% | 12.5% | 12.0% (2021-2025) |
  | Duke (`0001326160-24-000037`, `-25-000072`, `-26-000014`) | 7.8% | 5.0% | 5.6% | 8.9% | NA | 6.8% (2021-2024) |
  | Entergy (`0000065984-24-000012`, `-25-000012`, `-26-000174`) | 9.9% | 9.0% | 17.1% | 7.1% | NA | 10.8% (2021-2024) |
  | Dominion (`0001193125-26-063120`) | NA | NA | 7.3% | 6.5% | NA | 6.9% (2023-2024) |

  Southern's book equity carries $5.2B of goodwill from the gas acquisition; its 2021 figure carries the Vogtle charges.
- **The parts table** (five-year segment net income, Note 16; the filer reports segment net income, not operating profit,
  as its measure, and that measure is used, said so):

  | Part | Share of 2021-2025 segment net income | Castle | Decides |
  |---|---|---|---|
  | Traditional electric operating companies (Alabama, Georgia, Mississippi Power) | 79% | statutory franchise, allowed return | **yes** (more than half) |
  | Southern Company Gas (distribution, pipelines, marketing) | 14% | exclusive franchise for distribution, allowed return | no |
  | Southern Power (wholesale, market-based rates, long-term PPAs) | 6% | contracts, not a franchise; price set by the wholesale bid | no |

- **The field's returns over the last full cycle** (section C): the field's durable players earn returns on book equity in
  the high single digits to the low teens, set by commissions (allowed ROEs of 9.5% to 10.5% in the filer's own orders).
  Judged in words: ordinary, and set by a regulator. The framework's list of what Q2 rules OUT makes this the stated
  exception and carries it to Q3 as a second best (Q2, What it rules OUT, the standing castle that protects only ordinary
  returns). The rows under that exception: "there’s no way we get rich on our utility investments. But there’s no way we
  get poor, either" **[M2009-104]**; "We expect only that these businesses have reasonable expectations of earning decent
  returns on the incremental sums they invest" **[L2009-012]**; "when you get an allowed return in the electric utility
  you’re almost certain of earning it, I mean, if you behave yourself" **[M2010-037]**.
- **Southern Power**, the part that does not decide, is priced by the market and sells against "investor-owned utilities,
  IPPs, and others" (Item 1); it is carried to Q7 as an ordinary business at no growth (the parts paragraph). Its share is
  small and it is not valued separately (stated at Q7).
- **VERDICT: IN.** The deciding part's castle stands on statute and the commissions' orders, and has stood through two
  construction failures; its returns are a regulator's, carried to Q3 as a second best. The threats (the regulatory climate
  **[L2023-011]**, the one-time choice of the large new customer, catastrophe) are recorded for Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it earns on the capital it needs** **[M2010-090]**, measured on tangible assets **[M2011-060]**. *CONVENTION of this run:*
  return on tangible capital = net income to common plus interest paid after a 21% federal rate, over year-end common equity
  plus long-term debt (with current maturities and finance leases), short-term borrowings and minority interests, less
  goodwill and intangibles; rationale: the operating earnings after depreciation on all the capital in the plant, the
  measure the speakers give for a utility's added capital, "It’s measured by the operating earnings after depreciation"
  **[M2014-086]**. 2020: (3,119 + 1,330) / 75,656 = **5.9%**; 2025: (4,341 + 2,127) / 105,997 = **6.1%** (XBRL facts of the
  10-Ks cited in Step 0; interest paid 1,683 and 2,692). On common equity alone the return is 12.0% over 2021 to 2025 (Q2's
  table); the gap is leverage, and a high reported return is read for "a cyclical peak in earnings, a monopolistic position,
  or leverage" **[L1994-009]**: here it is the second and the third.
- **The added capital.** From 2020 to 2025 tangible capital rose by $30,341M and the after-tax operating earnings on it by
  $2,019M: **6.7% on the added capital**, about the allowed returns blended over a 56/44 capital structure. Common equity
  rose $8,044M (new shares and retained earnings) and net income to common by $1,222M (15.2% on the added equity, on borrowed
  money). Decent and regulated, not rich: "the industry offers owners the opportunity to deploy large sums at fair returns"
  **[L2005-005]**; "if they earn a decent return on capital, it can be a good business over time" **[M2007-112]**.
- **To stand still and to grow.** Capital spending in cash averaged $9,997M a year against D&A of $4,864M; the 2026
  programme is $15.9B. The cash never comes out: owner cash after all spending is negative in all five years, the profit
  "sitting in the yard" **[M2008-036]**, the business that "reports the 12 percent on capital but there’s never any cash"
  **[M2003-122]**. Part of the spending is compulsory (the obligation to serve, environmental compliance, CCR closure of $653M
  planned for 2026, Item 1), the trap of "you have to spend it the same way if it’s unattractive" **[M1998-128]**; and in
  inflation "To earn more, their owners must invest more" **[L2011-019]**; "your depreciation charges are inadequate and
  you’re kidding yourself as to your real economic profits" is said of the utility business by name **[M2015-049]**.
- **The growth arithmetic.** The growth is bought, dollar for dollar, with capital that earns about the allowed return; it
  adds value only as far as that return exceeds the owner's rate: "whether that’s good or bad depends on what we earn on that
  incremental $130 million over time" **[M2001-019]**. The speakers accept the case as second best: "as the second-best
  choice, still a good choice, the answer is yes. It’s not as good as the best choice" **[M2018-055]**, on condition of
  "decent returns on the incremental sums they invest" **[L2009-012]**.
- **WEIGHS: UNDECIDED.** The added capital earns a decent regulated return (for); every dollar of growth needs more than a
  dollar of outside money and the owner never sees cash (against): "cash-consuming businesses, by their nature, are
  unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**. Carried.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL; 2025 and 2024 checked
  against the filed consolidated balance sheet in the FY2025 10-K, and 2026-06-30 read from the 10-Q):

  | year-end | assets | common equity | goodwill + intangibles | debt (current LTD + short-term + LTD) | cash | retained earnings |
  |---|---|---|---|---|---|---|
  | 2016 | 109,697 | 24,758 | 7,221 | 47,457 | 1,975 | 10,356 |
  | 2018 | 116,914 | 24,723 | 5,928 | 46,849 | 1,396 | 8,706 |
  | 2020 | 122,935 | 27,972 | 5,767 | 49,189 | 1,065 | 11,311 |
  | 2022 | 134,891 | 30,408 | 5,567 | 57,550 | 1,917 | 11,538 |
  | 2024 | 145,180 | 33,208 | 5,493 | 64,824 | 1,070 | 13,750 |
  | 2025 | 155,720 | 36,016 | 5,461 | 72,591 | 1,639 | 14,856 |
  | 2026-06-30 (10-Q) | 162,027 | not read | not read | 75,582 | 2,984 | not read |

  (All ten year-ends are in the research cache, `cache/run_py.txt`; alternate years shown.) What moved, and why: debt rose
  $25.1B (53%) from 2016 to 2025 against common equity up $11.3B (45%), and the share count rose about 16% (weighted average
  951M in 2016, 1,103M in 2025; 1,150M at June 2026), so book value per share rose far less than book value. Retained
  earnings fell from $10.4B to $8.7B over 2016 to 2018 (the Kemper charges of 2017) and took until 2020 to pass the 2016
  figure; the growth in equity since is as much new shares as kept earnings (stock issued for $1,808M in 2022, $1,623M in
  2025, about $2.5B in the first half of 2026). Goodwill fell from $6,251M to $5,161M (dispositions and impairments) and is
  almost all the 2016 gas acquisition. Cash is kept thin throughout; the system runs on the debt and commercial-paper
  markets. Deferred regulatory assets are large ($7,427M, plus $5,129M related to asset retirement obligations, at 2025). What
  the figures say: a balance sheet growing on borrowed money and issued shares; what they "don’t say": whether the regulator
  will let the new assets earn **[M2025-032]**.
- **The real costs.** Depreciation is real **[R1996-023]**, and for a utility perhaps short of the true need **[M2015-049]**;
  stock pay is $136M a year in the filed cash flows (the tool's tag understated it). The recurring "one-time": Kemper charges
  2013 to 2017, Vogtle loss charges 2018 to 2022 (about $2.9B pre-tax), Nicor Gas disallowances 2023 and 2025, an Alabama
  Power impairment 2024, a $252M loss on debt extinguishment 2025, accelerated wind depreciation at Southern Power in 2025
  ($307M). Charges like these, in most years, are costs of the business: "we do not ask you to forget about those costs"
  **[M1999-023]**; to tell owners "Don't count this" year after year "is misleading" **[L2016-007]**. The owner cash of Step 0 is
  on cash and includes them as spent. Reported earnings also carry the equity part of AFUDC, a non-cash credit of $340M in
  2025 ($268M in 2023, $235M in 2024); construction accounting is where "there’s so many ways you can cheat in accounting"
  **[M2013-086]**; here it is prescribed by the regulator and disclosed, and owner cash, being on cash, does not contain it.
- **EBITDA in the filer's mouth:** none found in the 10-K text. **The adjusted figure and guidance:** the proxy reports that
  the company "Achieved the top of our adjusted EPS guidance range with payout at 176% of target for our short-term
  incentive plan", that it "delivered strong adjusted EPS results at or above the top end of our projected EPS guidance
  ranges", and sets the 2026 goal at "$4.55 reflecting the middle of the 2026 EPS guidance range" (DEF 14A,
  `0000092122-26-000028`). Guidance, an adjusted per-share figure featured, and targets consistently met: "a management that
  regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous"
  **[L2016-006]**; "the scourge of earnings "guidance"" **[L2019-006]**; "we become downright incredulous if they consistently
  reach their declared targets" **[L2002-041]**. Recorded as a WEIGHING against **[M1994-018]** and carried to Q5 (Q4, the
  make-the-numbers habit).
- **Confusion or suspicion in the accounts themselves?** None found. The regulatory accounting is heavy, but each regulatory
  asset, liability and rate mechanism is stated in Note 2 with its order; receivables and fuel stocks move with fuel prices
  and the recovery clauses, as the cash-flow lines show (the 2022 long-term fuel under-recovery of $2,166M, recovered over 2023
  to 2025). No prepaid or deferred account building without a stated order **[M1995-064]**.
- **VERDICT on the accounts: WEIGHS AGAINST** (not a STOP). The accounts can be read; the habits recorded go to Q5; the recast
  is owner cash on cash, after every capital outlay, stock pay and the minority partners' distributions (Step 0), and it
  feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Christopher C. Womack, Chairman, President and Chief Executive Officer (President since March 2023, CEO since May
  2023, Chairman since December 2023; Chairman and CEO of Georgia Power from June 2021 to March 2023, which covers the last
  two years of Vogtle 3 and 4; FY2025 10-K, executive officers). The board has a Lead Independent Director (DEF 14A).
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the hand is a regulated monopoly in
  growing states. The record against it: Kemper, an IGCC plant abandoned in 2017 after pre-tax charges of about $3.8B in 2016
  and 2017 alone (FY2017 10-K); Vogtle 3 and 4, placed in service on 2023-07-31 and 2024-04-29 (Note 2), with about $2.9B of pre-tax loss
  charges taken by the owners over 2018 to 2022 and $7.562B of construction and capital costs allowed into rates (Note 2).
  Against that, the companies earned inside their allowed ranges in 2023 to 2025 and their five-year return on equity (12.0%)
  is above that of the three comparables (Q2). *How they treat the owners:* read in the proxy, "see how they treat themselves
  versus how they treat the shareholders" **[M1994-009]**: the CEO's total pay for 2025 was $28,242,734 against $173,100 for
  the median employee; the short-term plan paid 176% of target on adjusted EPS at the top of guidance, the long-term plan 183%
  on relative TSR and 187% on consolidated ROE (DEF 14A, `0000092122-26-000028`).
- **The tells of dishonesty, and the integrity record.** (1) Kemper: in 2016 the SEC opened "a formal investigation of
  Southern Company and Mississippi Power concerning the estimated costs and expected in-service date of the Kemper County
  energy facility", and "On November 30, 2017, the SEC staff notified Southern Company that it had concluded its
  investigation with no recommended enforcement action" (FY2017 10-K, `0000092122-18-000012`). A securities class action on
  the same statements (class period April 2012 to October 2013) survived in part a motion to dismiss and was settled for
  "$87.5 million by defendants’ insurers"; the defendants "dispute and deny any and all such allegations"; the derivative
  actions settled for governance reforms and no payment (8-K exhibit, `0000092122-22-000010`). (2) The habits carried from Q4:
  guidance, adjusted EPS featured and paid on, targets met at or above the top of the range **[L2016-006]**, **[L2002-041]**.
  (3) No restatement and no material weakness found by a text search of the FY2025 10-K; the auditor, Deloitte & Touche, has
  "served as Southern Company's auditor since 2002" (FY2025 10-K).
- **The judgment on integrity.** The standard is doubt, not proof: "If you’ve got doubts, forget it" **[M2013-088]**; "we
  wouldn’t hire anybody, no matter how able, if we didn’t trust them" **[M2015-047]**. Read together: the one regulator
  charged with the question (the SEC) investigated the Kemper estimates and recommended nothing; the court narrowed the
  claims and the case was settled by insurers with liability denied; the cost overruns at both plants were disclosed as they
  came, in charges the owners bore, rather than buried. The guidance habit is a "negative" that the rows say they "can’t
  afford to use it as a total exclusionary factor" **[M1994-018]**, and the speakers judge the people on "things that they do
  in public in relation to their investors and the promises they make" **[M2004-067]**; what this management promises in
  public is an EPS range, and it has met it. That is the tell of **[L2002-041]** in its mild form (a regulated business whose
  earnings are largely set by orders can meet a range without fudging), and I find no instance in the filings read of a
  figure moved to meet it. My judgment: the record shows bad estimates of two plants and a promotional pay design, not
  dishonesty; the doubt is about competence and incentives, which is the ability weighing and Q6, not the integrity STOP.
  Written down as contrary evidence: a careful reader could hold the Kemper record (estimates repeatedly missed while the
  securities were sold) as doubt enough under **[M2013-088]**; I do not, on the SEC's closure and the disclosures, and say so.
- **Love of the business, and after the pay.** Not testable from outside for hired managers of a marketable stock **[M2016-066]**;
  the pay design rewards per-share earnings against a public guidance range and relative TSR, which is what the managers are
  paid to love.
- **VERDICT on integrity: IN** (the facts above recorded for any later run). **Ability: WEIGHS AGAINST**: two failed or
  badly overrun flagship plants in a decade, in a business whose one hard task is building plant on budget; "we’ve always
  been more concerned about how our record is achieved than the precise record itself" **[M2012-089]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 net income to common was $18,635M and
  common dividends paid $14,688M: about $3,947M kept (cash-flow statements and XBRL facts, Step 0). Over the same years the
  company also sold about $3,683M of new common stock and raised long-term debt by $23.3B. The market leg: the share price
  went from $61.43 (2020-12-31) to $87.20 (2025-12-31) (aggregator closes, flagged), a rise far larger than the roughly
  $3.6 a share kept, so the market leg is met. The intrinsic leg, which the rows require beside the market's **[R2009-002]**:
  the dollars kept, and the much larger sums borrowed and issued, went into rate base that earns about the allowed return
  (6.7% on added tangible capital, Q3), and owner cash after all spending stayed negative. Whether a dollar kept became more
  than a dollar of value depends on the regulated return exceeding the owner's rate; at the floor of about ten percent it
  does not. **Retention: UNDECIDED** (market leg met, intrinsic leg not shown).
- **Buybacks.** None in the window (no repurchases tagged after 2015, when $115M was paid; XBRL facts). Nothing to test
  against the bottom of the Q7 range; see the line written back from Q7 below.
- **Issuance and deals.** Issuance is a standing programme: an at-the-market plan for up to 50 million shares established June
  2026 after the 2024 plan, with forward sale contracts settling to June 2028 (10-Q, `0000092122-26-000054`); 31.1 million
  shares issued in the first half of 2026 for about $2.5B; equity units and convertible notes on top (Step 0). Value given
  against value got **[R1995-010]**, **[L2014-012]**: the shares were sold at about $88 to $98 (the forward prices in the 10-Q).
  Whether that gave less than it got turns on the Q7 range, written back below. The rows' warning is about the habit itself:
  "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**, which the framework carries as a
  candidate second STOP, unresolved; it is weighed here, not applied. **No deal paid in the company's own stock** in the
  window (the 2016 gas acquisition was paid in cash, before the window; the 2025 acquisition of $635M was cash), so the one
  STOP of Part A **[L2009-019]** does not arise.
- **Dividends.** About $3.0B a year, paid while owner cash after all spending is negative, so the dividend is in effect
  financed by the debt and share issuance above. The rows test a dividend by whether the dollar can be used at more than a
  dollar; here the company pays the dollar out and then raises more than a dollar back from the market.
- **Part B, the pay, the board, the owners.** Pay tied to what the person controls **[M2003-019]**: the short-term plan pays on
  adjusted EPS against the middle of public guidance; the long-term plan on relative TSR, a market ride of the kind
  **[M2000-062]** describes, and on consolidated ROE, which in a regulated business is set largely by the commissions' allowed
  return and the equity ratio. Payouts of 176%, 183% and 187% of target in a year when owner cash was negative. Goals should be
  "directly related to the daily activities of plan participants" **[L1996-018]**; these are related to the share price and to
  the regulator. The board: the CEO is also Chairman, with a Lead Independent Director. The by-law amendment of 2026-10-20 (8-K,
  `0000092122-26-000065`) requires a holder asking for a special meeting to own the requisite stake "on a net long basis and to
  hold such shares for at least one year": a modest step away from the owners' ability to act. Guidance itself, "forecasting
  earnings, I can’t imagine anything more destructive" **[M2022-054]**.
- **WEIGHS AGAINST.** Part A: retention UNDECIDED, continuous issuance weighed against under **[L2014-015]** (not applied as a
  STOP), no buyback, no all-stock deal. Part B: AGAINST, pay on adjusted EPS against guidance and on market and regulatory
  measures rather than on what the managers control.
- **Written back from Q7 (the buyback and issuance test, committed with Q7):** no shares were repurchased in the window, so no
  buyback price is tested. The shares issued in 2025 and 2026 at about $88 to $98 (forward prices, 10-Q) were sold above the top
  of the central range ($82.70) and about twice its bottom ($45.62): on this run's own range the owners received more in cash than
  they gave in value per share, which meets **[R1995-010]** on the arithmetic; the weighing against under **[L2014-015]** (the habit)
  stands.

## Q7 — WHAT IS IT WORTH? STOP.
- **Which basis.** The deciding part (Q2) is the traditional electric operating companies, which earn "an allowed return in
  the electric utility" **[M2010-037]** on invested capital: the regulated-utility paragraph of Q7 applies, and the
  equity-only basis is central, the exception being the row's own: "leaving aside certain exceptions, such as debt dedicated
  to Clayton's lending portfolio or to the fixed-asset commitments at our regulated utilities" **[L2017-012]**. The gas
  distribution utilities are regulated too. Southern Power (6% of five-year segment net income) sells at market-based rates
  and on the text belongs on the all-equity basis. *CONVENTION of this run:* the whole company is valued on the consolidated
  equity-only figures, Southern Power included; rationale: the filer reports operating cash and capital spending
  consolidated, not by part, and a 6% part cannot move the box; the all-equity figure is shown beside for the whole.
- **The cash input** (Step 0; `Test Runs/_research 2026-10-26 SO/oc.py`, `q7.py`): owner cash after interest and the company's
  own cash tax, after stock pay and the minority partners' net distributions. The window is 2021 to 2025, five years; no end
  year is aberrational on the filer's own description (the 2022 fuel under-recovery is a middle year and reverses inside the
  window), so the literal window is the base, specific (a) not engaged; working capital is inside operating cash (specific (d)).
  - **Maintenance guess** **[M2000-144]**, **[L1999-024]**: depreciation and amortization as the cash-flow statement totals it,
    average $4,864M a year, "the depreciation charge is not inappropriate in most companies to use as a proxy for required
    capital expenditures" **[M1998-127]**, "Every year we spend amounts equal to our depreciation charge simply to stay in the
    same economic place" **[L2000-035]**. Cross-check from the filing: the 2026 programme's maintaining categories (generation
    maintenance 1.4, distribution 2.0, general plant 1.8, nuclear fuel 0.3, environmental compliance 0.2: $5.7B) against 2025
    D&A of $6.0B; its growth categories (new generation 3.7, transmission 3.2, Southern Power 0.9, gas 2.2) are the rest of the
    $15.9B. The guess may be low for a utility under inflation **[M2015-049]**; it is the filing's best available.
  - **Owner cash after maintenance only: $2,797M a year** (2,202; 1,925; 2,217; 4,205; 3,436). After all spending: -$2,336M
    (ex acquisitions) and -$2,175M (net acquisitions in), the all-spending case shown beside, negative.
  - **Growth spending** (above maintenance, specific (e)): cash capital spending averaged $9,997M, so $5,133M a year, less net
    disposals of $161M a year (acquisitions net of businesses sold are capital spending, specific (c); here net sales):
    **$4,972M a year**. Not a serial acquirer (net purchases negative).
  - **The growth shown** (aggregate, specific of the PG re-test): owner cash after maintenance from $2,202M (2021) to $3,436M
    (2025), **11.77% a year**. The cap (specific (f)): carried ten years from the $2,797M base it reaches $8,507M, 15.57% of the
    year-ten sales at the window's own sales growth (6.34% a year, $23,113M to $29,553M), against the highest share of sales in
    the window, 15.73% (2024): **not cut**, but within a fifth of a point of the cut, said so. No rate above the discount rate is
    carried after year ten **[M1997-095]**.
  - **The utility debt credit** (Q7, The regulated utility, from 2026-10-23): long-term debt (current maturities, long-term
    debt and finance leases; no securitization bonds found in the FY2025 10-K) rose from $48,580M (2020) to $71,869M (2025):
    **$4,658M a year**. Credited against the growth spending only, capped at the deciding part's allowed debt share. The filing
    states an allowed equity ratio for Georgia Power only (56%, so **44% debt**, Note 2; Alabama Power's Rate RSE states a return
    range, not an allowed equity ratio; Mississippi Power's PEP neither); Georgia Power is 61% of the deciding part's net plant
    (rate base is not stated by company, *CONVENTION of this run:* net plant is the weight, rationale: the nearest filed measure
    of rate base), more than half, so the cap is 44%. Credit = 44% x $4,972M = **$2,188M a year**, below the debt raised.
    Beside it, the business's own long-term debt share of long-term capital (66.6% at 2025-12-31): credit $3,312M.
  - **Growth spending charged to the equity:** $4,972M - $2,188M = $2,784M at the window level; in the growth case it grows
    with the growth and stops after year ten: **$3,112M in year one, $8,469M in year ten, none after** (specific (e)).
- **The range** (equity-only, central; 1,150.363M shares; the sovereign 5.33%; zero nominal growth after year ten):

  | case | equity value | per share |
  |---|---|---|
  | no growth: $2,797M a year, maintenance only, for ever | $52,477M | **$45.62** |
  | shown growth: 11.77% for ten years, growth spending net of the debt credit charged, then flat | $95,137M | **$82.70** |
  | beside: growth case with the own-debt-share credit | $110,946M | $96.44 |
  | beside: growth case with no debt credit | $64,381M | $55.97 |
  | beside: book tax instead of cash tax (deferred tax charged, $386M a year) | | $39.33 to $66.61 |
  | beside: all spending charged (owner cash -$2,175M to -$2,336M) | negative | no value |

  **Value range: $45.62 to $82.70 a share against $92.69.** Width 1.81 to one.
- **The floor, tested first** (Q7, the floor is tested first): at $92.69 (market value $106,627M), the no-growth case returns
  2.62% a year and the shown-growth case about 4.94% (the rate at which its stream equals the price). **No case earns the floor
  of about ten percent at the price** **[M2003-149]**, **[M1994-004]**; even the own-debt-share case, whose top lies above the
  price, returns far below it. "there’s no way we get rich on our utility investments" **[M2009-104]**; the price is also above
  the top of the central range.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end valued at ten percent: no growth $24.32, shown
  growth $28.62; **fair price $26.47 a share** on the equity-only basis (central, the regulated utility), after the company's own
  tax. All-equity beside (owner cash before interest, interest paid added back after a 21% rate, $4,518M a year; net debt at
  2026-06-30 $72,598M = securities due within one year 4,694 + notes payable 2,132 + long-term debt 68,756 - cash 2,984, 10-Q;
  operating leases left out; the August 2026 convertible notes raised cash and debt alike and leave net debt unchanged): at
  ten percent -$23.84 and -$21.37, **all-equity fair price -$22.61, not positive**; at the sovereign the all-equity range is
  $10.57 to $64.66. No cheap price is reported.
- **Growth spending** (above maintenance) $3,112M in year one, $8,469M in year ten, none after (net of the debt credit; gross
  $5,557M and $15,122M). **Utility debt credit:** long-term debt increase $4,658M a year, against growth spending only, cap 44%
  (the deciding part's allowed share, Georgia Power's 56% equity ratio, the only allowed share the filing states, covering 61%
  of the deciding part's net plant).
- **Tax** (Q7, Whose tax): owner cash is after the company's own cash tax ($93M to $284M paid a year); the credit carryforwards
  are "immaterial" in the filer's words (Note 10), so no shelter is priced; the low cash tax is mostly deferred tax and
  production and investment credits, and in a regulated utility the deferred tax "helps our customer and it doesn’t help us,
  basically" **[M2015-030]**, which is why the book-tax case is shown beside.
- **VERDICT: OUT.** No case in the range earns the floor at the price, and the price sits above the top of the central range;
  "So, there’s just a point at which we drop out of the game" **[M2003-149]**. Not a close call needing a pencil either way **[M2009-005]**.


## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a judgment; the facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator for this run; no named business of Q12's list is involved).

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor of about ten percent at the price; equity-only range (the regulated
utility's basis) **$45.62 to $82.70 a share against $92.69** (2026-10-26, aggregator close). Q1 IN, Q2 IN, Q3 UNDECIDED,
Q4 WEIGHS AGAINST, Q5 integrity IN with ability WEIGHS AGAINST, Q6 WEIGHS AGAINST. Reporting figures (not verdicts): fair
price **$26.47** equity-only (central); all-equity **-$22.61**, not positive. Not a TOO HARD, so no research pass.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged; operator rule 2.)* **[M1997-127]**
- **Q8, the bond:** the 30-year Treasury yields 5.33% (2026-10-23); the stock's no-growth owner-cash yield at the price is
  2.62% and the growth case's implied return about 4.94% (Q7), both below the bond.
- **Q9, the debt and its cover:** long-term debt (with current maturities and finance leases) $71,869M at 2025-12-31; net
  debt $72,598M at 2026-06-30 (10-Q), with commercial paper and other notes payable of $2,132M and $4,694M of securities due
  within one year. Pre-tax income plus interest expense over interest expense: (4,999 + 3,238) / 3,238 = 2.5 times in 2025;
  (2,576 + 1,837) / 1,837 = 2.4 times in 2021 (Note 16, XBRL). The parent ("All Other") carried $1,416M of interest expense in
  2025 against no regulated asset of its own (Note 16). The test the rows give for a utility's debt is cover "even under very
  adverse business conditions" **[L2010-012]**; not judged here.
- **Q9, sudden demands for cash:** maximum potential collateral under contracts with credit-rating triggers, at 2025-12-31:
  $32M at BBB/Baa2, $445M at BBB-/Baa3, **$3,774M at BB+/Ba1 or below** (of which Georgia Power $2,503M, Southern Power
  $1,347M) (FY2025 10-K, MD&A, Financial Condition). Unused committed bank credit $8,909M across the system. New convertible
  notes of $833.75M due December 2027 and $1,897.5M due September 2029 (8-K `0000092122-26-000063`); equity units outstanding.
  Forward share sales settleable to June 2028.
- **Q9, one event:** three states and a gas business; hurricane exposure on the Gulf coast (storm damage recovery at Georgia
  Power, Note 2); nuclear plants (Farley, Hatch, Vogtle) and the risk factor that "Damages, decommissioning, or other costs
  could exceed the amount of decommissioning trusts or insurance coverage" (Item 1A); the regulatory climate (base rates in
  Georgia frozen through 2028 except storm costs; Nicor Gas disallowances), the speakers' own utility error **[L2023-011]**.
- **Q9, Southern Power:** 97% of its investment under contract through 2030 and 89% through 2035, average remaining contract
  about 12 years; 63% of contracted MW with AAA to A- counterparties (Item 1).
- **Q10:** nothing beyond the box.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (by the first session, 11:31); written question by question. **Departure:** the
      resumed session's first commit carried Step 0 through Q2 together, and Q3 with Q4 and Q5 with Q6 were committed in pairs;
      Q7 (with the Q6 line written back) and the close were committed on their own. Five commits in all, each with a pathspec of
      the two paths only.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (operator rule ten). The
      run binds nothing until folded into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (the check
      script `Test Runs/_research 2026-10-26 SO/check.py`: 0 problems); no E-ids; every filing fact carries its document and
      accession (the competitors' figures carry theirs; aggregator prices flagged).
- [x] The order was kept; Q7 closed the file; nothing after it is a clearance. The figures after the stop are facts only.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; stock pay from the
      filed statement (the tool's tag understated it); the sovereign from the US Treasury; the price flagged as an aggregator
      quote.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, and at Q5 the reading against my own integrity verdict);
      AFTER THE STOP filled. Integrity was judged at Q5 (IN), so the box carries no "integrity facts recorded, not judged" flag.
- [x] No point-in-time anchor: today's run; no row dated after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stock-pay column was replaced by the filed figure.
- [x] `python tools/check_framework.py` PASS before each commit.
- Honest limits: rate base is not stated by company, so net plant weighted the debt-credit cap (CONVENTION of this run);
  the rivals' 2025 returns (and Dominion's 2021 and 2022) are not framed in their XBRL facts and are shown NA rather than
  computed by hand; the proxy was read by search for pay, guidance and governance, not page by page; Southern Power was not
  valued separately (CONVENTION of this run, Q7).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The debt-credit cap for a deciding part of several regulated companies when only one states an allowed equity ratio.**
The text weights the allowed share "by rate base where that part is several regulated companies" and falls back to the
business's own share where an allowed share is stated "for less than half of the deciding part's rate base". Here the filing
states one allowed share (Georgia Power, 56% equity), covers more than half of the part, and states no rate base by company;
the text does not say whether the stated share is applied to the whole part or weighted with nothing for the rest. I applied
44% to the whole part, weighted by net plant as a confessed stand-in for rate base, and showed the own-share case beside
(top $96.44 instead of $82.70; the box does not change). (2) **A consolidated utility holding company with a merchant part.**
The regulated-utility paragraph puts merchant generation on the all-equity basis, but the filer reports operating cash and
capital spending only consolidated; the text does not say whether to split them by segment shares. I valued the whole on the
equity-only basis and confessed it. (3) **The maintenance guess for a utility.** The rows say depreciation can understate a
utility's real need ("your depreciation charges are inadequate" **[M2015-049]**) and Q7 asks for the filing's best guess; the
filing's own capital programme categories gave a cross-check ($5.7B of maintaining categories against $6.0B of D&A), but the
text does not say which categories count as maintaining. (4) **Q2's regulated-return exception** carries the field's ordinary
returns to Q3 "as a second best", while the template's Q2 line says "a durable castle that protects only ordinary returns closes
OUT"; the template omits the exception, and a reader of the template alone would close a utility at Q2. I followed the framework
text. (5) `Screens/cover_shares.py` labels the subsidiary registrants' common shares with the names of debt series from the cover
page; read from the cover itself they are the subsidiaries' shares. (6) `tools/run.py`'s stock-pay column used an APIC tag that
gave about half the filed expense.
