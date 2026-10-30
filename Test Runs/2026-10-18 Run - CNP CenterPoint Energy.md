# Company Run — CenterPoint Energy, Inc. (NYSE: CNP) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form: `Test Runs/_TEMPLATE - Company Run.md`,
copied to this dated file before any fetch. Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the one departure the
brief states: the lines of evidence were derived by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed in Step 0).
Working folder: `Test Runs/_research 2026-10-18 CNP/` (notes, the tool outputs, the arithmetic script, the citation check).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (bf17b27e):** not held; CenterPoint Energy (CNP) does not appear in `PORTFOLIO.md`.

**Contamination, declared and not used.** (1) Listing `Test Runs/` to check that no CNP file of today existed showed the file names of
other runs dated 2026-10-18 (twenty names, among them other gas and electric utilities); no file was opened. (2) The session's git
status and recent commit subjects named another company's run and its box (BEP, OUT at Q7). (3) The memory index loaded into the
session carries a line on the queue state (a count of gate-clearers and "nothing buyable"). (4) The adopted rule file
`Framework/v5/CASE 2026-10-18 - the regulated utility's fair price, decided from the corpus.md`, read for Q7's method, names sixteen
utilities run on 2026-10-17 and 2026-10-18 that closed OUT at Q7. None of this bears on CNP's filings and none of it is used below.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $40.55 (close 2026-10-16, the last close before this Sunday run; from `tools/run.py`, an aggregator, live quote only, flagged per operator rule 5).
- **Shares by class:** 658,720,288 common shares outstanding, excluding 166 treasury shares, on the cover of the 10-Q for the quarter to
  2026-06-30 (filed 2026-07-28, accession `0001130310-26-000041`; `python Screens/cover_shares.py CNP`). The two counts of 1,000 shares on
  the same cover are the common stock of the subsidiary co-registrants, all held inside the group, not CNP classes; there is one class.
  Cross-check: the 10-Q balance sheet shows 658,700,905 shares outstanding at 2026-06-30. The 8-Ks filed after the 10-Q (2026-07-31
  notes, 2026-09-09 credit facilities, 2026-09-14 data incident, 2026-10-01 Ohio closing) and the 424B5 of 2026-07-30 (junior
  subordinated notes) issue no common shares. **Pending:** forward sale agreements of May 2025 on 24,864,865 shares, to be settled on or
  before 2027-02-25 for about $910 million (10-Q, Note 15); shown beside the per-share figures, not in the central count.
- **Market cap:** 658.72M x $40.55 = **$26,711M** (with the forward shares: 683.59M shares, and the $910M they bring).
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-19, accession `0001130310-26-000008`): Item 1, Item 1A, Item 3,
  Item 7, the statements, Notes 4, 7, 11, 12, 14 and 16, and the Houston Electric statements; the 10-Ks for FY2023
  (`0001130310-24-000010`) and FY2021 (`0001130310-22-000023`) for the cash flows, segments and Houston Electric figures of 2019 to 2023;
  the 10-Q for 2026-06-30 (`0001130310-26-000041`); the proxy (DEF 14A, filed 2026-03-04, `0001104659-26-023457`); the 8-Ks of
  2026-02-12 (`0001104659-26-014406`), 2026-02-26 (`0001104659-26-020626`, convertible notes), 2026-07-28 with its press release
  (`0001104659-26-087279`), 2026-07-31 (`0001104659-26-089263`), 2026-09-09 (`0001104659-26-106356`), 2026-09-14
  (`0001104659-26-107560`) and 2026-10-01 (`0001104659-26-112565`); the 424B5s of 2026-05-15 (`0001104659-26-062746`, the $1 billion
  at-the-market and forward programme) and 2026-07-30 (`0001104659-26-088494`).
  **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025, $2,486M on the filed
  Statement of Consolidated Cash Flows (10-K FY2025), equal to the XBRL figure `tools/run.py` printed.
- **`python tools/run.py CNP`, arithmetic lines only** (saved as `run_py_output.txt` in the research folder): operating cash 2023 to 2025
  of $3,877M, $2,139M, $2,486M; capital spending $4,401M, $4,513M, $4,870M, plus the $357M Posey Solar asset purchase in 2025; D&A
  $1,401M, $1,439M, $1,530M; stock pay not found in XBRL (the cash flow statement carries no separate stock-pay line; the gap is
  declared at Q4, not filled). Owner cash after all capital spending is negative in each of the three years (mean -$1,761M; -$1,880M
  with the asset purchase). The tool's balance-sheet table is checked at Q4 against the filed statements; its debt table sums a non-debt
  line (d6, liabilities other than long-term debt) and is not used.
- **The lines of evidence this name needs, derived from the 10-K** (the brief's departure): from **Item 1**, the parts and their
  regulators (Houston Electric under the PUCT, Indiana Electric under the IURC, the gas utilities under four states), the exclusive
  certificated territories, the customers (REPs for Houston Electric) and the divestitures (Louisiana and Mississippi 2025, Ohio 2026);
  from **Item 1A**, rate regulation and regulatory lag (the 2024 Houston Electric case), the TEEEF procurement and the $800 million that
  officials argued shareholders should bear, severe weather and Hurricane Beryl, the financing of the 10-year plan, the REP receivable
  concentration; from **Item 7**, the $65.5 billion capital plan (raised to $66.7 billion in the 2026-07-28 release), the rate case
  outcomes (allowed ROE and capital structure), the debt and equity raised and the securitizations, and the non-GAAP EPS guidance.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: would I be content to own this "if the market closed for five years"
**[M1997-109]**, on the cash the business itself produces. The second is who is paid to tell you: the company's ten-year capital plan
and its 7 to 9 percent non-GAAP EPS growth outlook through 2035 (proxy letter, DEF 14A 2026) are a seller's projection of what it
sells, and the speakers have "never looked at a projection" **[M1995-050]**; "you do not get impartial advice" where fees ride on one
answer **[M2020-037]**. No macro view of rates or of data-center demand enters **[M2000-094]**; the load forecast is the company's claim,
not a fact. **Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after capital spending was negative in each of
the last three years, the gap closed by $3.7B to $6.0B of new long-term debt a year, by divestitures and by forward equity; (2) Houston
Electric's return on its own equity fell from about 11.8% (2022) to about 7.9% (2025) while its parent put $3.1B of equity into it over
2021 to 2025 (Houston Electric statements, FY2025 and FY2023 10-Ks); (3) the 2024 Houston Electric rate case ended in a $47M revenue cut
and a 9.65% ROE against 10.4% asked; (4) after Hurricane Beryl, officials argued shareholders should pay about $800M of TEEEF costs, and
a complaint to end TEEEF recovery is still open (Item 1A); (5) pay is tied to non-GAAP Adjusted EPS, relative TSR and a P/E modifier
(proxy); (6) a theft of customer data was reported on 2026-09-14 (8-K).

## THE STANDING RULE
The buyer's conduct: a part-interest bought for cash in a listed share, no borrowed money, no option given, nothing that can call
**[M2012-081]**, **[L2014-024]**. Nothing in this purchase puts the buyer at risk of ruin, provided it is bought with money the buyer
has and does not need. The target's own debt is Q9's, not this rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from Item 1.** A utility holding company whose parts are regulated monopolies: Houston Electric (transmission and
  distribution only, 2.86M metered customers served through 67 REPs, rates set by the PUCT); Indiana Electric (SIGECO, vertically
  integrated, 154k customers, IURC); and the gas distribution utilities (4.03M customers in Indiana, Minnesota, Texas, and Ohio until
  2026-10-01). The Electric segment carried 58% of five-year operating income 2021 to 2025 (Q2's parts table).
- **The key variables and whether they are foreseeable**, "evaluating how predictable they were first" **[M1998-044]**: the rate base
  (what is spent and allowed), the allowed return and equity share (set in rate cases: Houston Electric 9.65% ROE on a 43.25% equity
  share from the 2025 order; Indiana Electric 9.8% on 55%; Ohio 9.79%; 10-K Item 7), regulatory lag and disallowances, storm
  restoration costs and their securitization, and load growth. "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]** is available for the first four: the earning power of a regulated wires
  and pipes business is an allowed return on a rate base, and what is needed is to "understand the economic dynamics of the industry"
  **[M2011-014]**, not the engineering. The fifth, load growth from data centers, is the company's forecast and is not needed to read
  the castle or the value.
- **Would the insiders write the forecast down?** **[M2000-105]**: they do, in rate filings with forward test years and in a ten-year
  capital plan, and the regulators publish the allowed returns. This is not the fast-moving field of **[L1993-023]**; the change it faces
  (distributed generation, electrified heating against the gas parts, heavier storms) is slow change, which "can lull you to sleep
  easier" **[M2014-038]**, and is weighed at Q2.
- **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence" it is not inside
  **[M2002-092]**: no doubt on the economics of a regulated monopoly. What is not knowable with precision is the
  regulators' future conduct, which is the castle question (Q2), not the understanding question.
- **VERDICT: IN.** The economics ten years out are those of an allowed return on a rate base, foreseeable within a range
  **[M2000-037]**, **[M2011-084]**; "the first question is, can I understand it?" **[M1995-051]** is passed.
## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (Q2, a business of parts; "lumping them together [...] impedes analysis" **[L2008-005]**). Operating income by
reportable segment, 2021 to 2025, from the segment tables of the FY2023 10-K (2021 to 2023) and the segment note of the FY2025 10-K
(2024 and 2025 computed from its lines: revenues less fuel and purchased power, O&M, D&A and other taxes):

| Part | Operating income 2021 / 2022 / 2023 / 2024 / 2025 ($M) | Five-year sum | Share | Castle | Decides |
|---|---|---|---|---|---|
| Electric (Houston Electric T&D under the PUCT; Indiana Electric, integrated, under the IURC) | 773 / 954 / 1,090 / 1,139 / 1,245 | 5,201 | 58% | exclusive certificated territory, regulated return | **yes, more than half** |
| Natural Gas (Indiana, Minnesota, Texas; Ohio to 2026-10-01; Louisiana and Mississippi to 2025-03-31; Arkansas and Oklahoma to 2022) | 618 / 631 / 681 / 867 / 897 | 3,694 | 42% | non-exclusive franchises, a pipe network nobody duplicates, regulated return | no |
| Corporate and Other | small | | | none | no |

Inside Electric, Houston Electric is the larger part (operating income $1,052M of the segment's $1,245M in 2025, from Houston
Electric's own income statement in the FY2025 10-K). The file closes on Electric, read through Houston Electric.

**The castle tests, each with its filing fact.**
- **What keeps it standing, and how permanent** **[M1995-038]**: the law. "There are no other electric transmission and distribution
  utilities in Houston Electric's service area. For another provider [...] it would be required to obtain a CCN from the PUCT" (10-K
  Item 1); in Indiana "service territory certificates are exclusive" (Item 1). The castle does not "depend on the genius of the lord"
  **[M1995-038]**: a wires utility is close to "The really great business" of **[M1996-037]** in this one respect, that it needs no genius to run, though the
  return on it does depend on how management behaves before its regulator (below).
- **The attacker with money** **[M2011-015]**, **[M1997-103]**: a rival with any sum could not build a second grid in Houston without a
  certificate the regulator does not give; "why are there no new entrants into the field?" **[M2000-077]** is answered by statute. The
  gas networks are franchises that "In most cases [...] are not exclusive" (Item 1), but no second network is built beside one already
  laid; the gas threat is substitution ("alternate energy sources such as electricity", Item 1), not a rival pipe.
- **Pricing power and the agony before a rise** **[M2005-020]**: the business has none of its own. Prices are set in rate cases, and the
  last Houston Electric case asked for about $60M more and a 10.4% ROE and ended in "an overall revenue requirement decrease of
  approximately $47 million" and a 9.65% ROE (Item 1A). The rate case is the prayer session, held in public before a regulator. The
  power "a monopoly or a near monopoly" would have **[M2010-092]** belongs here to the regulator, not to the owner.
- **Unit volume; the customer and the low bid** **[M2017-009]**: Houston Electric's metered customers grew about 2% a year (2,814,859 at
  2021 to 2,859,313 at 2025, FY2023 and FY2025 10-Ks); throughput rose from 103,000 GWh (2021) to 108,766 GWh (2023). Customers cannot take
  a low bid for delivery: the REPs compete on energy, not on wires.
- **Ask the competitors** **[M2017-091]**: not available from the record; the nearest public evidence is the filings of the other large
  utilities in the same state, read below.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: the evidence runs both ways. Narrowing: Houston Electric's return on its
  own equity fell from about 11.8% (2022) to 10.7% (2023), 8.2% (2024) and 7.9% (2025) (net income $510M, $593M, $546M, $578M on member's
  equity of $3,622M, $4,998M, $6,109M, $7,159M, $7,532M at the year-ends 2021 to 2025, Houston Electric statements); the 2024 case cut
  revenue; after Hurricane Beryl, government inquiries, a law of June 2025 (Senate Bill 231) limiting TEEEF leases to units of five MW or
  less, and a complaint to end recovery of the large and medium TEEEF units (Item 1A, Note 7). Holding: the regulator approved
  recovery of $1.1B of the $1.3B of Beryl restoration costs filed, with $78M deferred and a $22M reduction of carrying costs, and an
  irrevocable financing order for system restoration bonds sold in 2026 (Note 7); "Approximately 85% of our rate base has been subject
  to a rate case since the beginning of 2023" (Item 7).
- **What could destroy, modify or reduce it** **[M2000-014]**: a regulatory climate that stops honouring the return, "the specter of
  zero profitability or even bankruptcy" in a few states **[L2023-011]**; one catastrophic storm on a single coastal grid, since "A
  catastrophic event can render a single utility insolvent" **[L2005-019]** (CNP is two electric utilities and several gas utilities, not
  one, but Houston Electric carries the electric segment); wildfire liability (Item 1A); and, for the gas parts, slow substitution by
  electricity, "slow change can be much harder to perceive" **[M2014-038]**. Distributed generation "has not been a significant factor to
  date" (Item 1).

**The competitor row** (the 10-K names no rival company: it says there is no other T&D utility in Houston Electric's area and names
the gas threat only as "alternate energy sources" and unnamed "intrastate pipelines, other gas distributors and marketers"; no named
rival is therefore flagged as a non-filer). *CONVENTION of this run:* the field is read from the two nearest SEC filers in the same
state and business, Oncor Electric Delivery (the other large ERCOT wires utility) and Atmos Energy (the largest Texas gas distributor);
rationale: Q2 section C needs the field's returns from filings and the filer names no rival. Metric: net income over average equity,
from each filer's XBRL facts of its 10-Ks.

| Company (filing) | 2022 | 2023 | 2024 | 2025 | Note |
|---|---|---|---|---|---|
| Houston Electric (CNP 10-Ks FY2023 `0001130310-24-000010`, FY2025 `0001130310-26-000008`) | 11.8% | 10.7% | 8.2% | 7.9% | no goodwill in its equity |
| CNP consolidated, on common equity (same) | 11.3% | 9.2% | 10.0% | 9.6% | 2022 includes $303M of gains on sale; on equity less goodwill 21.7%, 16.6%, 16.7%, 14.7% |
| Oncor Electric Delivery (10-Ks `0001193311-23-000005` to `0001193311-26-000007`) | 6.9% | 6.2% | 6.5% | 6.3% | members' equity carries $4,740M of goodwill; less goodwill 10.9%, 9.5%, 9.5%, 8.7%; allowed equity share 42.5% |
| Atmos Energy (10-Ks `0000731802-22-000037` to `0000731802-25-000056`, fiscal years to September) | 8.9% | 8.7% | 9.1% | 9.3% | |

**The field's returns over the last full cycle, judged in words** (section C): the field earns regulated returns, about six to eleven
percent on book equity, the returns a regulator allows and no more. These are ordinary returns, and the framework's exception for a
return set by a regulator governs them (Q2, What it rules OUT: carried to Q3 as a second best). The rows behind the exception: "no way
we get rich on our utility investments" and no way to get poor either **[M2009-104]**; capital-heavy businesses are entered on
"reasonable expectations of earning decent returns on the incremental sums they invest" **[L2009-012]**. So the ordinary level does not close the file here; it goes to Q3.

**Judgment.** The castle stands: no attacker can cross it, because the law has filled the moat with a certificate **[M2011-015]**. What
is narrowing is not the castle but the rent the lord is allowed to collect inside it, and that is shown in Houston Electric's falling
return and the political weather after Beryl. On the evidence the regulator still honours the bargain (the Beryl recovery, the 2025
orders through 2029), so the future can be judged within a range; the castle is not shown open **[M2000-019]**, and the regulatory climate
is carried to Q3, Q7 and Q9 as the rows direct **[L2023-011]**.
- **VERDICT: IN**, on the deciding part (Electric), with the regulated return carried to Q3 as a second best **[M2009-104]**,
  **[L2009-012]** and the regulatory climate recorded as the strongest evidence against **[L2023-011]**, **[M2025-045]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it has earned on the capital it needs** **[M2010-090]**, **[M2000-065]**: on common equity 9.2%, 10.0% and 9.6% in 2023 to 2025
  (11.3% in 2022 with $303M of gains on sale, 19.0% in 2021 with the $681M Enable merger gain); on common equity less goodwill 16.6%,
  16.7% and 14.7% (`q7.py`, from the balance sheets and income statements of the FY2021, FY2023 and FY2025 10-Ks). The goodwill ($3,550M at
  2025, mostly from the $6.0B Vectren purchase of 2019) is left out when judging the business and kept when judging the capital
  allocation, "because we paid for it" in the framework's reading of **[M2011-060]**. Read with care: the tangible figure is flattered by
  leverage, the trap of **[M2001-054]**, since debt was about two thirds of debt plus equity at 2025 (Q4); and the deciding part's own
  return fell to 7.9% in 2025 (Q2).
- **What the added capital earns, "measured by the operating earnings after depreciation"** **[M2014-086]**: operating income rose from
  $1,039M (2020) to $2,110M (2025), +$1,071M, while net plant rose from $22,362M (2020) to $35,859M (2025, the $34,056M on the balance
  sheet plus $1,803M of Ohio plant held for sale), +$13,497M, after the sale of the Arkansas, Oklahoma, Louisiana and Mississippi gas
  businesses. About 7.9% pre-tax on the added plant, before interest on the debt that funds more than half of it: a regulated return,
  "decent" in the sense of **[L2009-012]**, not the See's equation.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**: the filing does not split maintenance from growth spending.
  The speakers' proxy is depreciation **[M1998-127]**, $1,395M a year over 2021 to 2025, against capital spending of $4,478M a year
  (including the finance-lease principal and the Posey Solar purchase). For a utility under inflation the depreciation charge
  understates what keeps it in place, "your depreciation charges are inadequate" **[M2015-049]**, so the guess flatters the business.
- **Is the reinvestment compulsory?** The ten-year plan of $65.5B (Item 7; $66.7B in the 2026-07-28 release) is spent to keep a growing
  and storm-exposed grid in service as much as to grow it; resiliency spending is ordered and approved by regulators (the $2.68B System
  Resiliency Plan, Item 1A). That is the spending the rows fear when it earns too little, "spend money like crazy" whether attractive or
  not **[M1998-128]**, and accept when it earns a reasonable return, "cash-consuming businesses, by their nature, are unattractive unless
  the cash they consume gets to earn a reasonable return" **[M2012-057]**.
- **The cash test** **[M2003-122]**, **[M2008-036]**: over 2021 to 2025 operating cash was $10,334M against capital spending of $22,388M;
  the gap and $2,406M of common dividends were met by $9,175M of net new long-term debt and commercial paper, $5,438M from selling
  businesses and the Energy Transfer units received for Enable, and $494M of new common stock (cash flow statements). It is the business
  that "reports the 12 percent on capital" while the cash never reaches the owner **[M2003-122]**; every dollar paid out was borrowed or raised.
- **WEIGHS AGAINST.** A capital-heavy regulated business is a second best **[M2018-055]**, **[M1998-081]**; here the added capital earns
  about the regulated return, the deciding part now earns below its allowed return, and the owner's cash never arrives without new debt
  or new shares **[M2012-057]**, **[L2011-019]**. The "little or no debt" criterion goes to Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (year-ends 2016 to 2025, the filed statements behind `tools/run.py`'s table,
  accessions in `run_py_output.txt`): total assets $21.8B to $46.5B; shareholders' equity $3.5B to $11.2B, raised mostly by issuing stock
  (common in 2018, 2020 and 2024, mandatory convertible preferred converted in 2021) rather than by retention: retained earnings went from
  -$668M (2016) to $2,043M (2025), with a fall to -$845M in 2020 when the Enable investment was written down. Goodwill went from $862M to
  $5,164M with the Vectren purchase (2019) and back to $3,550M through impairment and through the sale of businesses that carried it
  ($217M to Louisiana and Mississippi, $393M to Ohio, Note 4). Long-term debt (non-current) went from $7.5B to $20.6B; with current
  portions, short-term borrowings and securitization bonds, debt was $23.0B at 2025 and $24.6B at 2026-06-30 (10-Q), against equity of
  $11.7B. Receivables moved with revenue ($740M on $7.5B of revenue in 2016, $806M on $9.4B in 2025); cash is kept near zero ($38M). The
  regulatory assets ($3.0B non-current at 2025, $3.6B at 2026-06-30) are the storm and gas costs awaiting recovery, the item to "look
  twice" at when deferred accounts build **[M1995-064]**: they did build (Uri in 2021, Beryl in 2024 and 2025) and each build has a
  regulator's order behind it (Note 7). What the figures say: the equity grew by issue, the debt grew faster, and the owner's cash came
  from selling parts. What they cannot say: whether the regulators will keep honouring the deferred costs.
- **The real costs.** Depreciation is a real cost **[L2015-004]**, and here likely an understated one **[M2015-049]**. Stock pay of
  $48M, $51M, $65M, $34M and $48M (2021 to 2025, LTIP expense, Note 8) is a real cost **[L2021-003]**, not found in XBRL and deducted in
  `q7.py`. The finance-lease payments for TEEEF ($179M in 2021, $485M in 2022, financing section) are capital spending and are charged.
  Preferred dividends ($107M, $49M, $50M to 2023) are charged to the common owner. The items presented as one-time recur: gains, losses and costs of
  mergers and divestitures are excluded from the company's non-GAAP EPS in 2020, 2021, 2022, 2023, 2024 and 2025 (the reconciliation in
  the FY2025 earnings release, 8-K `0001130310-26-000010`), because the company sells a business nearly every year; telling owners year
  after year "Don't count this" is what **[L2016-007]** calls misleading when the adjustments are the business's ordinary conduct.
- **The adjusted figure featured, and the guidance habit** (recorded here as a WEIGHING, carried to Q5): the FY2025 release leads with
  "Non-GAAP earnings per diluted share" of $1.76 against $1.60 GAAP, the gap made of ZENS marks (which net to about nothing), $60M of
  merger and divestiture impacts and, new in 2025, $46M after tax of "Impacts associated with TEEEF Units removed from Rate Base" (8-K
  `0001130310-26-000010`), the cost of the generators the company leased, could not use as planned and no longer charges to customers.
  Every release reiterates guidance; the proxy letter says the company "both increased and delivered on our 2025 non-GAAP EPS guidance"
  and gives a 7 to 9% non-GAAP EPS growth outlook through 2035. The rows: "a management that regularly attempts to wave away very real
  costs by highlighting" an adjusted figure makes them nervous **[L2016-006]**; predicting growth rates is "both deceptive and dangerous"
  **[L2000-037]**; "the scourge of earnings" guidance **[L2019-006]**; those who "consistently reach their declared targets"
  **[L2002-041]**. The GAAP figures are reconciled line by line in the same release, and EBITDA is not featured.
- **Suspicion or confusion in the statements themselves?** No: the accounts are long but readable, every deferred cost is tied to an
  order, the ZENS are explained, and no reserve or deferred account moves without its stated cause **[M1995-063]**, **[M2003-029]**. A
  management "preoccupied with accounting considerations" is "a negative" but not "a total exclusionary factor" **[M1994-018]**.
- **VERDICT on the accounts: IN (no confusion, no suspicion); WEIGHS AGAINST** for the recurring exclusions, the TEEEF exclusion, the
  adjusted figure featured and the guidance habit, carried to Q5 **[L2016-006]**, **[L2002-041]**. The recast earnings for Q7: owner cash
  after stock pay, preferred dividends, finance-lease principal and depreciation as the maintenance guess, $449M a year to the common
  owner over 2021 to 2025 (`q7.py`).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run it, against the hand dealt: the hand is a monopoly grid in a fast-growing
  city; under the present chief executive (Jason Wells, Chief Executive Officer and President, a director since January 2024, Chair since October 2025, Item 7) Houston Electric's return on
  its equity fell from 10.7% (2023) to 7.9% (2025), the 2024 rate case cut revenue, and the Beryl response brought inquiries, a
  derivative suit (filed 2025-01-22, stayed) and the TEEEF controversy, whose leases predate him. How they treat the owners: through
  the proxy and the reports, read below and at Q6.
- **The reports** **[M1998-036]**, **[M2007-082]**: the 10-K is candid about what hurts, stating the $800M that officials argued
  shareholders should bear for TEEEF, the open complaint, the disallowance positions in the Beryl case and the 2024 rate cut in its own
  risk factors; the 2026 proxy discloses a $19,134 omission from the 2024 compensation table and corrects it. The proxy letter, by
  contrast, celebrates guidance met and raised and does not name Beryl, TEEEF or any mistake; "That taboo, implying managerial perfection,
  always made me nervous" **[L2024-003]**.
- **The habits carried from Q4, read with the integrity record**: the adjusted figure that removes the TEEEF cost is also the figure on
  which the short-term bonus and 35% of the long-term award are paid (proxy: "a specified cumulative non-GAAP Adjusted EPS goal"; 2023
  to 2025 PSUs vested at 172% of target), and the remaining TSR award carries a P/E modifier paying at least 75% "regardless of the level
  of TSR performance achieved" if the stock's P/E is top-quartile. A company that pays its officers for the market's multiple is close
  to the stock price "posted in the lobby" that makes the speakers nervous **[M2004-067]**.
- **Is that doubt on integrity?** **[M2013-088]**. Judged on the record: no instance found in the filings read of a misstatement, a
  restatement, a regulator's finding of dishonesty, or a figure that the company does not reconcile; the exclusions are named and sized in
  the release; the Beryl costs passed a contested prudence review with $78M deferred and $22M of carrying costs given up (Note 7). The tells are those of a
  management "preoccupied with accounting considerations" and paid on its own adjusted number **[M1994-018]**, **[L2016-006]**, not of
  a rascal **[L2023-003]**. I do not find doubt about honesty; I find a habit the rows warn "can turn fudging into fraud" in time
  **[L2000-039]**, which weighs heavily and is recorded. A reader who takes the TEEEF exclusion inside the pay figure as doubt would close
  the file here OUT; the box at the end of this run would not change (Q7 closes it OUT on the floor).
- **Love of the business** **[M2000-098]**: not observable for a hired management of a listed utility beyond the record; no instance found
  of insider buying with own savings in the filings read (directors' and officers' holdings in the proxy are grants and awards).
- **VERDICT on integrity: IN** (no evidence of dishonesty; the habits recorded against) **[M2013-088]**, **[M1994-018]**; **ability WEIGHS
  AGAINST** (falling returns in the deciding part, the TEEEF capital, the Beryl response) **[M1994-008]**, **[M1999-104]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**: over 2021 to 2025 net income to common was $5,337M, common dividends
  $2,406M, so about $2.9B was kept, and $0.5B of new common was sold besides, plus the forward equity; book value per common share went
  from about $10.9 (2020) to $17.1 (2025) and the market value from about $12B to $26.7B. On the market leg the test is met by a wide
  margin **[M2011-072]**; on the intrinsic leg, which the market leg cannot replace **[R2009-002]**, Q7 below finds the value of the
  common far under the price, so the market's premium is not evidence that the kept dollars became more than a dollar of owner cash.
  The forward question, "Can you keep using all of the capital you generate" **[M2010-097]**, is answered by the plan: yes, and more than
  it generates, at the regulated return.
- **Part A, buybacks**: none. "none of CenterPoint Energy's equity securities [...] were purchased" (10-K Item 5); no programme. The
  buyback test does not arise; the issuance line against the Q7 range is written back below.
- **Part A, issuance and deals** **[R1995-010]**, **[L2014-015]**: the share count rose from about 431M (2016) to 658.7M (2026), about 53%
  in ten years, through common offerings (2018, 2020, 2024 at $25.36 a share), the conversion of mandatory convertible preferred (2021),
  forward sales in 2025 at $36.26 to $37.49 still to settle, a $1 billion at-the-market and forward programme opened 2026-05-15 to run to
  2029, and convertible notes ($1.0B due 2028, $650M due 2029, Item 7 and 8-K `0001104659-26-020626`). This is planned, continuing issuance
  to fund a capital plan larger than the cash the business makes; the rows' warning is against companies "hell-bent on issuing shares"
  **[L2014-015]**, which the framework carries as a candidate STOP not yet resolved (section VI); it weighs heavily here. The Vectren
  purchase (2019, "Acquisitions, net of cash acquired" of $5,991M in the FY2021 10-K cash flow statement) was paid for in part with that new stock and preferred; since then its
  Ohio gas utility (sold 2026 for $2.62B) and its Energy Systems Group (sold 2023) have been sold and goodwill written down. No
  post-mortem against the original projections is published **[L2014-013]**. No all-stock deal in undervalued stock: the STOP of
  **[L2009-019]** does not apply.
- **Part A, dividends**: the company pays out about 55% of earnings ($0.88 a share paid in 2025) while selling new shares and borrowing to
  fund its spending, a round trip through the market for the owner's own money; the policy is consistent **[L2012-015]**, but a dividend
  is right when the business "expects to regularly earn more than it can profitably employ" **[M2004-089]**, which is the opposite of
  this business.
- **Part B, pay, the board, the owners**: CEO total pay $12.1M in 2025 and $9.3M in 2024 (Summary Compensation Table); the short-term
  plan on non-GAAP Adjusted EPS, safety, operations and customer measures; the long-term plan 35% relative TSR with the P/E modifier, 35%
  cumulative non-GAAP Adjusted EPS, 30% restricted units; a compensation consultant and an 18-company peer group set the levels. Pay is
  not tied "to what is actually under the reasonable control of the person" **[M2003-019]** where it rides on the market's P/E;
  consultants and peer data are the ratchet the rows name **[M2004-016]**, **[L2005-015]**, **[M2012-095]**. The chief executive became
  Chair in October 2025, with a lead independent director; "how hard it is to replace a mediocre CEO if that person is also Chairman"
  **[L2014-026]**. Owners are told the guidance and the adjusted figure first (Q4), the opposite of "We never make a forecast on earnings"
  **[M2016-002]**.
- **WEIGHS AGAINST**, Part A: continuing issuance and borrowing to pay a dividend and fund spending the business cannot fund, with a
  serial-issuance tell **[L2014-015]**, **[R1995-010]**; Part B: pay on an adjusted figure and on the stock's multiple, CEO and Chair
  combined **[M2003-019]**, **[L2014-026]**.
- *Buyback and issuance line, written back from Q7 (committed with Q7):* no shares were bought back, so the buyback test has nothing
  to read. The issues were priced above the range: $25.36 a share in August 2024 and $36.26 to $37.49 on the 2025 forwards, against a
  range top of $20.51 (Q7). Selling stock above what it is worth gives the continuing owner more business value than it takes, the test
  of **[R1995-010]**, so the prices paid weigh for the issues themselves; the habit of issuing remains the tell of **[L2014-015]**.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**, as a range. Arithmetic in `q7.py`,
output in `q7_output.txt` (research folder); every input is a filed figure named in the script.

**Basis.** The deciding part (Electric, Q2) earns a return its regulators allow on its invested capital ("when you get an allowed
return in the electric utility you" are almost certain of earning it, in the row's own words **[M2010-037]**), so by Q7's paragraph
on the regulated utility the central figure is the **equity-only basis**, the dedicated debt assigned to the business by the
exception in the row itself, "leaving aside certain exceptions, such as debt dedicated to Clayton's lending portfolio or to the
fixed-asset commitments at our regulated utilities" **[L2017-012]**; the all-equity figure is shown beside. The allowed debt share
is Houston Electric's, 56.75% long-term debt and 43.25% equity in the PUCT order of 2025-03-13 (Item 7), the deciding part's.

**Inputs, 2021 to 2025** (cash flow statements of the FY2023 and FY2025 10-Ks; the 2026 half-year in the 10-Q is not a full year and is
not used): operating cash $22M, $1,810M, $3,877M, $2,139M, $2,486M; capital spending $3,164M, $4,419M, $4,401M, $4,513M, $4,870M, plus
TEEEF finance-lease principal ($179M, $485M) and the Posey Solar asset purchase ($357M, 2025); depreciation and amortization $1,316M to
$1,530M; stock pay $48M to $65M a year (Note 8); preferred dividends $107M, $49M, $50M. The window spans Winter Storm Uri (operating cash
of $22M in 2021, the gas costs deferred, recovered in 2023) and Hurricane Beryl (restoration costs paid in 2024 and 2025, recovered by
$1.19B of bonds sold 2026-02-26, Note 7). Net long-term debt and commercial paper raised over the window: $9,175M; the cap, 56.75% of
capital spending of $22,388M, is $12,705M, so the whole $9,175M is credited (securitization bonds included, since they repay restoration
costs charged inside operating cash in the same window; CONVENTION of this run, rationale: the cap is not reached, so the inclusion moves
the figure by nothing the cap would have stopped).

**The cases** (owner cash to the common owner a year, after every real cost and the company's own tax, less the Ohio business's share,
$98M of pre-tax income at 21% = $77M, since it was sold on 2026-10-01 for $1.42B in cash and a $1.2B note, which are added back to the
value as cash; Note 4 and 8-K `0001104659-26-112565`):

| Case | Owner cash ($M a year) | Return at the price, no growth | Value at 5.43% a share | Value at 10% a share |
|---|---|---|---|---|
| **Maintenance only, depreciation as the guess, literal window (central)** | 371 | 1.54% | **$14.36** | $9.62 |
| Maintenance only, the window before the Beryl draw (specific (d), beside) | 591 | 2.45% | **$20.51** | $12.96 |
| All spending, with the debt credit (specific (e)'s all-spending case, beside) | -744 | negative | -$16.81 | -$7.31 |
| All spending, the debt credit and $5,438M of divestiture proceeds counted (specific (c), beside) | 344 | 1.43% | $13.59 | $9.20 |
| Maintenance only with the debt also credited against the maintenance spending (a mechanical reading, beside) | 1,163 | 4.83% | $36.49 | $21.63 |
| The same, before the Beryl draw (beside) | 1,383 | 5.74% | $42.64 | $24.97 |

*How the specifics were applied.* **(e)** The filing does not split maintenance from growth spending; the guess is the rows' proxy,
depreciation **[M1998-127]**, stated as a guess **[M2000-144]**, and for a utility under inflation it is a generous one **[M2015-049]**.
The growth spending is then charged against the growth it buys, and in the no-growth case it stops. *CONVENTION of this run:* in the
maintenance-only no-growth case no debt is credited, because a rate base that does not grow raises no new debt under a fixed
regulated capital structure; rationale: crediting borrowing forever against spending that adds no assets would lever the business
without limit. The mechanical reading that credits it anyway is shown beside. **(b)** The maintenance-only series changes sign
(-$1,628M, -$63M, $2,361M, $666M, $908M), and its halves (-$846M against $787M) give no meaningful rate, so the range is the no-growth
case alone, said so; the two figures reported as its ends are that case on the literal window and on the window before the Beryl draw
**(d)**: a draw tied by the filer to one event, shown beside. **(c)** The company was a net seller of businesses over the window; the
proceeds are shown beside, and they stop with growth. **(f)** No growth is carried, so the cap does not bind. **(a)** The window holds
both Uri's cost and most of its recovery; no first or last year was replaced. Working capital is inside operating cash **(d)**.

*An illustrative growth case, outside the range convention, for the floor test only:* the before-Beryl maintenance cash grown at the
operating income's 11.5% a year (2021 to 2025) for ten years, growth spending net of the debt credit ($1,248M a year) charged, then
flat: $31.11 a share at 5.43%, $12.36 at ten percent, an expected return of 4.49% at the price. At the revenue's 2.9% it is worth less
than the no-growth case: the growth bought at these returns is worth less than its cost to the equity at ten percent, "growth can
destroy value" **[L2000-023]**.

**The floor, tested first.** At $40.55 the expected return on the central case is 1.54% a year, and no case in the table, nor the
illustrative growth case, reaches ten percent: the highest is 5.74%, on a reading that credits debt the business does not need to raise.
To earn ten percent at the price with no growth the common owner would need about $2,487M a year of owner cash, against $371M on the
central case. The rows quit there: "just a point at which we drop out of the game" **[M2003-149]**, and every case is below it. The width test is
not reached; the price also sits above the top of the range ($20.51), which closes OUT by the same convention.

**Value range (equity-only, central): $14.36 to $20.51 a share against $40.55.** The literal window beside is the bottom figure itself.
On the all-equity basis (beside; owner cash before interest after a 21% shield, against market value plus net debt of $22,020M: debt
of $25,093M at 2026-06-30 including the ZENS derivative, less cash and the ZENS equity securities, less the $2.62B of Ohio proceeds)
the no-growth value less net debt is -$6.78 to -$0.63 a share.

**Fair price (a reporting figure, never a verdict; Part VII):** **$11.29 a share on the equity-only basis (central for the regulated
utility)**, each end valued at ten percent ($9.62 and $12.96) and the two averaged, after the company's own tax; $12.21 with the
24.86M forward shares and their $910M counted. **All-equity figure beside: -$17.29 a share** (not positive). No cheap price is reported.

- **VERDICT: OUT** (the floor, tested first: no case earns about ten percent at the price **[M2003-149]**; the price is above the
  range, the case is no screamer **[M2009-005]**). A utility at a full price closes OUT, "no way we get rich on our utility
  investments" **[M2009-104]**, and "some utilities have sold at extraordinary prices" **[M2017-095]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Fact for later, not weighed: the central case's 1.54% sits below the 5.43% thirty-year Treasury.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Gas and electricity delivery; no business the rows name.)

---
## THE BOX
**OUT at Q7 (the floor): no case earns about ten percent at $40.55; value range $14.36 to $20.51 a share on the equity-only basis
(central for the regulated utility), fair price $11.29 (all-equity -$17.29).** Q1 IN, Q2 IN on Electric, Q3 against, Q4 accounts IN
with the adjusted figure against, Q5 integrity IN with the habits recorded and ability against, Q6 against. Integrity facts recorded
at Q5 and judged there (the TEEEF exclusion inside the pay figure, the P/E modifier, guidance); a later run should read them first.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.
- **Q8.** The central case's return at the price, 1.54%, is below the 5.43% thirty-year Treasury of 2026-10-16 (Treasury par curve).
- **Q9, debt.** Debt of $24.6B at 2026-06-30 against equity of $11.7B (10-Q); debt excluding securitization bonds about 66% of debt
  plus equity, against a credit-facility covenant of 67.5% of consolidated capitalization, as the facility defines it (8-K
  `0001104659-26-106356`, which also lets the ratio rise to 70% after a natural disaster); $1.6B of long-term debt due within a year
  at 2026-06-30; convertible notes of $1.0B (2028) and $650M (2029), junior subordinated notes with optional interest deferral, new
  $700M junior notes of 2026-07-30. Coverage, pre-tax earnings plus interest over interest, the rows' definition **[L2012-002]**: about
  2.5x in 2023, 2.4x in 2024, 2.4x in 2025 (income statements). The criterion "little or no debt" of **[R1997-001]** is not met by any
  reading, and the rows apply it to whole businesses.
- **Q9, sudden demands and one event.** A single coastal grid carries the electric segment: "A catastrophic event can render a single
  utility insolvent" **[L2005-019]**; storm costs have been recovered so far by securitization after the fact (Uri, the May 2024 storms,
  Beryl, Note 7), each depending on a regulator's financing order; the open TEEEF complaint, the Beryl personal-injury suits (dispositive
  motions denied 2026-01-28, Note 14), and the customer-data incident of September 2026 (8-K `0001104659-26-107560`).
- **Q9, counterparties.** Houston Electric's receivables are concentrated in a small number of REPs (Item 1A); gas supply 52% from three
  suppliers (Item 1).
- **Q12.** Nothing in the filings read bears on a named business of the rows.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Committed after Q1, Q2 and Q7 separately; **Q3 to Q6
      were written in one pass and committed together** (`534c4aa1`), a lapse from one commit per question, declared here.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (not touched here); the run binds
      only once folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. `Test Runs/` was listed once, before the first fetch,
      to check that no CNP file of today existed; the names seen and the other accidental sightings are declared under
      contamination at the head of this file and were not used. The adopted rule file of 2026-10-18 was read for Q7's method and its
      list of other utilities' boxes is declared.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_cites.py`: 101 ids, 0 problems); no E-id;
      every filing fact carries its document and accession; the run's own conventions are labelled CONVENTION of this run.
- [x] The order was kept: Q1 and Q2 IN, Q3 and Q6 weighings recorded and carried, Q4 and Q5 IN on their STOP grounds; Q7, a STOP,
      closed the file OUT; Q8 to Q12 NOT REACHED and nothing after Q7 is a clearance.
- [x] Owner cash after every real cost (stock pay, preferred dividends, finance-lease principal, depreciation as the maintenance guess,
      all spending in the cases beside), never a net-income proxy; the sovereign from the US Treasury par curve; the price from an
      aggregator, flagged.
- [x] Contrary evidence written down as found (the foundations' list, Q2's narrowing evidence, Q4 and Q5's habits); facts for Q8, Q9
      and Q12 under AFTER THE STOP; the integrity facts named in the box line.
- [x] Not a point-in-time run; no anchor-date bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its debt table was set aside (it sums a non-debt line).
- [x] `python tools/check_framework.py` PASS before each commit that touched this file after Q2 (Q1 and Q2 were committed before the
      first run of the test; it passed on the file as it then stood when next run).
- **Not obtained:** the maintenance share of capital spending (the filing does not split it); stock pay before 2021; Houston Electric's
  2020 equity (its 2021 return is not computed); the competitors' named rivals (the 10-K names none); the operating results of the
  Ohio business beyond its pre-tax income; any insider purchase with own money (none found in the filings read).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The regulated-utility paragraph of Q7, adopted today, says the long-term debt raised over the window is "credited against the capital
spending it funded", but it does not say how that credit meets specific (e)'s maintenance-only central case. Applied mechanically, the
debt is credited against depreciation-sized maintenance spending too, and the no-growth case then capitalises borrowing forever against
a rate base that does not grow; the owner cash on that reading rises from $371M to $1,163M a year. I read the credit as belonging to the
growth spending only (a CONVENTION of this run, stated at Q7) and showed the mechanical reading beside; the box does not depend on the
choice (5.74% at the price on the most generous figure). Three smaller gaps: (1) the paragraph names "the regulator's allowed debt share"
in the singular, and CNP has five regulators with shares from 45% to 56.75%; I used the deciding part's (Houston Electric's) and the cap
did not bind. (2) It does not say whether securitization bonds, which repay storm costs inside operating cash rather than fund fixed
assets, count as debt raised; I counted them, and said so. (3) Specific (b) sends a sign-changing series to the no-growth case alone,
which leaves the range a single case; the fair price's "each end case valued at ten percent" then has one end, and I used the literal
window and the window before the Beryl draw (specific (d)) as the two ends. Separately, the brief asks for rivals "the 10-K itself
names", and a franchise monopoly's 10-K names none; Q2 section C still needs the field's returns, so I took the two nearest same-state
SEC filers as a CONVENTION of this run. Finally, Q4 and Q5's division of the make-the-numbers habit leaves open whether an adjusted
figure that removes the cost of management's own decision (TEEEF) and is then used to pay management is still a "habit" weighed at Q4 or
already "doubt" at Q5; I judged it a habit, and wrote that the box would be the same either way.
