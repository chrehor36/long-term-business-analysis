# Company Run — NextEra Energy, Inc. (NYSE: NEE) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template before any fetch, commit 7904fae8. Dispatched blind run; working folder
`Test Runs/_research 2026-10-23 NEE/`, whose `worksheet.py`, `worksheet_out.txt`, `comps.py` and `comps_out.txt` hold
every sum below.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (8b41d773): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Contamination, declared.** (1) To confirm that no run file already stood at this run's path, I listed `Test Runs/`
through a case-insensitive filter on "nee"; it printed three file names of other companies whose names contain those
letters (an oilfield-services company, a payments company and an engineering company, all dated 2026-09 or 2026-10).
Names only; none opened; nothing used. No file about NEE, NextEra Energy or FPL Group was listed. (2) The session's
context showed recent commit subjects about another utility's v5 run (MGEE, a Q7 OUT on the floor). Not opened, not used;
it bears on nothing here except that I knew another utility had been run under the regulated-utility paragraph.
(3) The memory index line that the framework's own map loads names counts of gate-clearers; it names no company. Nothing
else from the blind-listed files was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $81.90 (close 2026-10-22; Yahoo chart via `tools/sources.py` `price()`; **aggregator, flagged** per operator
  rule 5, live quote only).
- **Shares by class** from the latest filing's cover: **2,097,306,049** NextEra Energy common shares outstanding at
  2026-09-30 (10-Q for Q3 2026, filed 2026-10-21, accession `0000753308-26-000081`; `python Screens/cover_shares.py NEE`).
  The tool also printed 1,000 shares: the cover says these are Florida Power & Light Company common shares "all of which
  were held, beneficially and of record, by NextEra Energy, Inc."; they are not NEE shares and are not added. The 10-Q
  balance sheet states "outstanding shares – 2,097"; NEE carries no treasury line, so issued less treasury is the same
  count. No 8-K after the 10-Q reports an issuance (submissions list fetched 2026-10-23: the only later-dated 8-K is the
  same-day earnings release, `0000753308-26-000077`). **Dilution in view, not in the count:** about 716 million shares to
  Dominion Energy holders if the merger closes (joint proxy, below); about 329 million shares reserved "for issuance
  pursuant to various financings and other arrangements" at 2026-07-24 (joint proxy), the corporate units (NEE.PRS,
  NEE.PRT, NEE.PRV) among them.
- **Market cap:** $171,769M (2,097.306M × $81.90).
- **Sovereign for the earnings currency:** USD **5.29%**, US Treasury daily par yield curve, 30-year, 10/22/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-13, `0000753308-26-000015` (NEE and FPL combined filing): Items 1, 1A, 7, 8 (the
    statements of both registrants, Notes 1, 4, 8, 15, 16).
  - 10-Ks for FY2024 `0000753308-25-000011`, FY2023 `0000753308-24-000008`, FY2022 `0000753308-23-000019`, FY2021
    `0000753308-22-000014`: the cash-flow statements of NEE and FPL for 2021-2022, the segment note, reserve
    amortization and the campaign-finance risk factor.
  - 10-Q for Q3 2026, filed 2026-10-21, `0000753308-26-000081`: balance sheets of NEE and FPL at 2026-09-30, nine-month
    cash flows, legal proceedings.
  - Proxy (DEF 14A), filed 2026-04-01, `0001104659-26-038551`: summary compensation, pay design, ownership, lead director.
  - Merger 8-K, filed 2026-05-18, `0001104659-26-063001` (Item 1.01); joint proxy statement/prospectus (424B3), filed
    2026-07-28, `0001104659-26-087576` (board's reasons, shares to be issued, deal terms); special-meeting 8-K, filed
    2026-09-03, `0000753308-26-000071` (votes); derivative-settlement 8-K, filed 2026-10-06, `0000753308-26-000074`, with
    its Exhibit 99.1 (the notice of settlement).
  - 8-Ks of 2022-01-25 `0000753308-22-000008` (chief executive succession) and 2023-01-25 `0000753308-23-000010` and
    `0000753308-23-000011` (FPL chief executive's retirement; the review of the campaign-finance allegations).
  - Comparators (Q2) and the merger target (Q7, beside): XBRL company facts of Duke Energy, Southern Company and Dominion
    Energy (filer-tagged 10-K data, transcription only); Dominion's 10-K for FY2025, `0001193125-26-063120`, read for
    one cross-check.
- **One figure cross-checked against the filed statement:** NEE's net cash from operating activities for 2025, $12,485M,
  in the XBRL company facts and on the filed consolidated statement of cash flows (10-K FY2025, page 67); total assets
  $212,721M and long-term debt $89,556M at 2025-12-31 likewise agree. Dominion's 2025 operating cash, $5,361M, agrees
  between its XBRL facts and its filed statement.
- `python tools/run.py NEE` printed one line: "NEE: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." No
  arithmetic from it is used. Every figure below is taken from the filed statements and summed in
  `worksheet.py` (Part VII, the tooling: same number sooner, no number added).

**The lines of evidence this name needs,** derived from the 10-K's Item 1, Item 1A and Item 7 (the brief's stated
departure from the canonical list):
1. FPL's rate regulation: the 2025 rate agreement (allowed ROE 10.95% in a 9.95% to 11.95% band, 59.6% equity ratio,
   the rate stabilization mechanism), the cost-recovery clauses, the FPSC's power to disallow (Item 1, FPL Regulation).
2. FPL's franchise and its competition: 226 franchise agreements, self-generation and rooftop solar (Item 1; Item 1A).
3. NEER's contracted fleet, merchant share and customer-supply trading (Item 1, NEER; Markets and Competition).
4. Clean-energy tax credits and their phase-out under the OBBBA (Item 1; Item 1A, tax laws).
5. The capital program and how it is paid for: capital spending by segment against operating cash, debt, equity units,
   tax-equity (differential membership) money and asset sales (Item 7; the cash-flow statements).
6. The accounts: the HLBV allocation of losses to noncontrolling interests, adjusted earnings, non-qualifying hedges,
   FPL's reserve amortization (Item 7; Notes 1 and 16).
7. Legal and integrity matters: the campaign-finance allegations, the securities class action, the derivative actions,
   the Avangrid antitrust suit (Item 1A; Note 15; the 10-Q's legal proceedings).
8. Weather and storms, and the recovery of storm costs (Item 1A; Note 1).
9. Liquidity, credit ratings, collateral and guarantees (Item 1A; Item 7, Liquidity; Note 1, Guarantee Arrangements).
10. Nuclear operations and licences (Item 1; Item 1A).
11. The XPLR affiliate and its impairments (Item 7; Notes 4 and 8).
12. The Dominion Energy merger (the 8-K, the joint proxy, the vote).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own NEE "if the market closed for five years" **[M1997-109]**, which
turns the question to FPL's franchise and NEER's contracts, not to the quotation. The market serves and does not instruct
**[M2006-077]**: the share price rose and fell with rates and with the tax-credit news, and none of that is an input here.
No macro forecast enters **[M2000-094]**: the joint proxy's demand forecast (U.S. electricity demand "expected to grow
approximately 60% by 2045", data-center load "of more than 130 gigawatts") is a macro forecast and is given no weight.
Who is paid to tell you **[M2020-037]**: the merger's fairness opinions (Lazard, BofA Securities) are paid opinions, and
the board's case for the merger is stated in "adjusted earnings per share" growth of "over 9% through 2032"; both are
read as advocacy. Margin of safety **[M1996-084]**: if it needs a pencil it is too close.
**Contrary evidence, written down as found** **[M1997-127]**:
- Owner cash after all capital spending was negative in every year 2021 to 2025, by $5.8B to $11.0B a year after asset
  sales; dividends ($3.0B to $4.7B a year) were paid out of borrowed and newly issued money.
- Total debt tripled from $30.7B (2016) to $95.6B (2025) and reached $113.9B at 2026-09-30.
- More than half of NEER's five-year net income attributable to NEE (56%) is the HLBV allocation of book losses to
  tax-equity investors, not cash.
- FPL's reported earnings are steered to a target ROE by a reserve the company amortizes or reverses.
- A securities class action over statements about political activities, revived on appeal, is being settled for
  $150M; derivative actions naming the current chief executive allege "an alleged political influence scheme tied to
  improper use of “dark money” funding".
- $2.7B of the XPLR (former NextEra Energy Partners) stake was written off in three years (2023-2025).
- The merger issues about 716M shares, a quarter of the combined company.

## THE STANDING RULE
Owning a part-interest in NEE bought with the buyer's own money, unlevered and sized so that a total loss cannot touch
what the buyer has and needs, puts the buyer at no risk of ruin; the rule governs the buyer's financing and sizing, not
the target's debt (that is Q9) **[M2012-081]**, **[L2014-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**Which part must be understood.** Q1's holding-company paragraph (extended 2026-10-06 to operating segments) asks that
each part that "matters" be understood, and "matters" means the part that decides under Q2's business-of-parts
paragraph: more than half of five-year operating profit, or else the largest part. NEE reports two segments (Note 16;
the chief operating decision maker's measure is net income attributable to NEE). Five-year sums, 2021-2025 (10-Ks FY2023
and FY2025, Note 16): **FPL $21,014M, NEER $9,716M, Corporate and Other −$1,919M; total $28,811M, which equals NEE's
reported five-year net income attributable**. FPL is 72.9% of the total and 68.4% of the two segments. **FPL decides.**
(On NEER's figure before the HLBV allocation to noncontrolling interests, −$147M, −$616M, $2,530M, $1,051M and
$1,472M, FPL's share is larger still.)

**FPL, the deciding part.** FPL is "a rate-regulated electric utility" serving "more than 6 million customer accounts"
in Florida (10-K FY2025, Item 1). Its rates are set by the FPSC "at a level that is intended to allow the utility the
opportunity to collect ... its cost of providing service, including a reasonable rate of return on invested capital".
The 2025 rate agreement runs "through at least December 2029", with an authorized ROE of 10.95% in a 9.95% to 11.95%
band, a 59.6% equity ratio, base increases of $945M (2026) and $705M (2027), and solar and battery adjustments; fuel
and several other costs pass through clauses (Item 1, FPL Regulation). Customer accounts grew 1.7% in 2025 (Item 7).
The key variables **[M1998-044]** are four: rate base (the capital FPL is allowed to put to work), the allowed return
and the regulatory climate that sets it, customer growth in Florida, and storm costs and their recovery. Each is stated
in the filings, and the regulator's settlement fixes the first two for four years ahead. That is "a reasonable fix on
about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, which is the
rows' definition of understanding **[M2000-037]**; the past statements do tell me what the future ones will look like
**[M2008-033]**: FPL's net income rose in step with its equity (book return 10.2% to 11.7% a year, Q3). The variables
are important and knowable **[M2006-076]**. I understand the economic dynamics without the engineering **[M2011-014]**.

**What I do not foresee, written down.** (a) The regulatory compact itself: the rows record that it can break
**[L2023-011]**; FPL's 2025 agreement is under a motion for reconsideration by the Office of Public Counsel and others
(Item 1). (b) Self-generation: "Changing technology (particularly the increasing efficiency of solar power generation)
... could alter the favorable relative cost position that FPL currently enjoys" (Item 1). Both are Q2's tests of the
castle, not a bar to understanding where FPL's economics stand.

**NEER, the part that does not decide.** NEER is understood in its contracted core ("approximately 95% of NEER's net
generating capacity was committed under long-term contracts", remaining term about 14 years), and not understood in
its growth: its new-build economics turn on federal tax credits being phased out ("Wind and solar generation
facilities are eligible ... if such facilities begin construction before July 5, 2026 or are placed in service by
December 31, 2027"), on new IRS guidance on "begin construction", on the foreign-entity rules, and on a customer-supply
and trading book. If NEER mattered under the convention, the doubt rule would keep the whole outside the circle
**[M2002-092]**; under the convention it does not decide, and the doubt is carried to Q2 and Q7, where NEER is valued
with no growth credited at the top of the range.

**Routing.** No fast-changing technology closes the deciding part here; FPL's threat from rooftop solar and storage is a
slow change, owned by Q2. Not a bank. A business of parts read by its deciding part.

**VERDICT: IN** on FPL, the deciding part, **[M2012-065]**, **[M2000-037]**, **[M2008-033]**; NEER's growth economics
recorded as outside my foresight **[M2002-092]**, not deciding.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The parts are read separately,
since "lumping them together, as is done in standard financial statements, impedes analysis" **[L2008-005]**.

**The parts table** (Note 16, net income attributable to NEE, 2021-2025, $M; operating income is not reported by
segment, and the chief operating decision maker's measure is this one):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| FPL (rate-regulated utility) | 3,206 | 3,701 | 4,552 | 4,543 | 5,012 | 21,014 | 72.9% | regulated franchise, standing; return set by the regulator | **yes** |
| NEER (contracted generation, storage, transmission, customer supply) | 599 | 285 | 3,558 | 2,299 | 2,975 | 9,716 | 33.7% | price competition in a commodity-driven field; ordinary cash returns on new capital | no |
| Corporate and Other | −232 | 161 | −800 | 104 | −1,152 | −1,919 | −6.7% | (financing and eliminations) | no |

**FPL's castle, test by test.**
- *The key factor and how permanent* **[M1995-038]**: the franchise. "During the term of a franchise agreement, which is
  typically 30 years, the municipality or county agrees not to form its own utility"; FPL held 226 such agreements
  "with varying expiration dates through 2055", covering "the vast majority of FPL's retail customer base", and serves
  the rest "pursuant to the general obligation to serve as a public utility" (10-K FY2025, Item 1). The FPSC also has
  jurisdiction over "service areas" and "planning, siting and construction of facilities" (Item 1).
- *The attacker with money* **[M2011-015]**: a rival with any sum could not string a second grid over FPL's service
  area without franchises, rights-of-way ("FPL relies upon Florida law for access to public rights-of-way") and the
  FPSC's leave. The money test passes. The FPSC's request-for-proposal rule lets independent producers bid to supply new
  steam or solar capacity of 75 MW or more (Item 1); that opens supply to bidders, not the customer relationship.
- *Pricing power and the agony before a rise* **[M2005-020]**: FPL has none of its own. Its prices are what the FPSC
  allows; the 2025 increases ($945M and $705M of annual base revenue) came by negotiated settlement and are under a
  motion for reconsideration by the Office of Public Counsel and consumer groups (Item 1). The return is the
  regulator's, not the market's.
- *The low-cost position*: FPL says "FPL's cost of service is lower than the cost of self-generation for a significant
  majority of customers" and that "maintaining low rates requires a strategy focused on developing and maintaining a
  low-cost position" (Item 1). The filings read give no bill comparison with other utilities; I record the claim, not a
  finding.
- *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: (1) self-generation:
  "Changing technology (particularly the increasing efficiency of solar power generation), tax incentives, economic
  conditions, regulatory changes and other factors could alter the favorable relative cost position that FPL currently
  enjoys" (Item 1), and laws that "would permit third-party sales of electricity" could have a material adverse effect
  (Item 1A); a slow change, which "can lull you to sleep easier" **[M2014-038]**; (2) the regulatory climate, which the
  rows record breaking in other states, "the specter of zero profitability or even bankruptcy" **[L2023-011]**; FPL's
  standing with its regulators and legislators is itself under the cloud recorded at Q5; (3) hurricanes, whose
  restoration costs FPL recovers by surcharge after the fact, "subject to prudence review by the FPSC", and for which
  "NEE does not have property insurance coverage for a substantial portion of either its transmission and distribution
  property or natural gas pipeline assets" (10-Q, risk factors).
- *Widening or narrowing* **[M1999-108]**: customer accounts +1.7% in 2025, average usage per retail customer −1.2%
  (Item 7); a settlement that raised the allowed ROE from 10.80% to 10.95% and kept the 59.6% equity ratio. On the
  evidence of this window the franchise is standing; I see no sign of it filling in.

**The competitor row.** The 10-K names no rival company as a competitor (a search of its text for the large U.S.
utilities and independent power producers found only Avangrid, as plaintiff in an antitrust suit, and Gulf Power, as
FPL's merged predecessor). **CONVENTION of this run:** the comparators are three large U.S. investor-owned regulated
electric utility holding companies that file with the SEC and operate in the Southeast beside FPL: Duke Energy (whose
Duke Energy Florida serves much of the rest of peninsular Florida), Southern Company, and Dominion Energy (also NEE's
merger target); rationale: a regulated franchise is compared with other regulated franchises earning a regulator's
return, and these three are the nearest on size and region. Metric: net income to common over average book equity,
2021-2025, from each filer's XBRL 10-K facts (transcription; equity as tagged may include preferred; `comps.py`):

| | 2021 | 2022 | 2023 | 2024 | 2025 | five-year, book | five-year, tangible |
|---|---|---|---|---|---|---|---|
| FPL (FPL's own statements in NEE's 10-Ks) | 10.2% | 10.2% | 11.7% | 11.1% | 11.1% | **10.9%** | about 11.8% (goodwill $2,965M) |
| Duke Energy (CIK 1326160) | 7.8% | 5.0% | 5.6% | 8.9% | 9.6% | 7.4% | 12.1% |
| Southern Company (CIK 92122) | 8.6% | 12.1% | 12.9% | 13.6% | 12.5% | 12.0% | 14.5% |
| Dominion Energy (CIK 715957) | 7.4% | 0.6% | 7.3% | 6.5% | 10.6% | 6.5% | 7.8% |

**The field's returns over the last full cycle, judged in words.** The field earns what its regulators allow, from
the middling to the decent, on very large equity bases; FPL sits in the upper half of it, steadily, with less
variation than any of the three. This is a standing castle that protects ordinary-to-decent returns, and Q2's list
names the exception for exactly this case (Q2, What it rules OUT: a return set by a regulator is carried to Q3
as a second best). The rows' own description of the field fits:
"there’s no way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**; "It
will never be a sensational business. It’s a very capital-intensive business." **[M2007-112]**.

**NEER, the part that does not decide.** NEE's own words: "Wholesale power generation is a capital-intensive,
commodity-driven business with numerous industry participants. NEER primarily competes on the basis of price, but
believes that its track record of completing projects on schedule, creditworthiness, operating scale and ability to
offer and manage reliable customized risk solutions to wholesale customers are competitive advantages" (Item 1, Markets
and Competition). In a field the filer itself calls commodity-driven, the castle the rows admit is the low-cost
producer, "when a company is selling a product with commodity-like economic characteristics, being the low-cost
producer is all-important" **[L2000-017]**; NEER claims scale, not a measured cost lead, and the filings read state no
cost per MWh against rivals. Its cash return on the growth capital of the window is low: operating cash before
after-tax interest rose by $2,973M from 2021 to 2025 while D&A rose $1,144M, about $1.8B a year more on about $44.7B
of net growth spending (spending less maintenance, less asset sales), about 4.1% (`worksheet_out.txt`). The castle is
judged open in the sense that matters here, a price-competitive field earning ordinary returns on new capital, where
even few competitors can "beat each other’s brains out" **[M2013-052]**; as a part that does not decide it is carried
to Q7 as an ordinary business at no growth (Q2, a business of parts). It does not close the file.

**VERDICT: IN**, on FPL, the deciding part: a regulated franchise standing, whose return is the regulator's and is
carried to Q3 as a second best **[M1995-038]**, **[M2011-015]**, **[M2009-104]**; threats recorded for Q7 and Q9
(self-generation **[M2014-038]**, the regulatory climate **[L2023-011]**, storms). NEER carried at no growth.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**FPL, the deciding part.** Return on the capital it needs: 10.9% on average book equity over 2021-2025 (10.2%, 10.2%,
11.7%, 11.1%, 11.1%), about 11.8% with its $2,965M of goodwill taken out; the regulator's earned-ROE figures are 11.70%
(2025) and 11.40% (2024) (Item 7). The capital it must put in: capital spending and nuclear fuel of $43,304M over five
years against D&A of $15,355M (plus $1,691M of reserve amortization credited inside D&A), about 2.5 times; it retained
nearly everything (net cash sent to NEE, dividends less capital contributions, $3,160M on $21,014M earned) and still
raised $11,363M of net long-term debt. This is the regulated utility the rows describe: "To earn more, their owners must
invest more" **[L2011-019]**, and the earnings rise because the capital rises, not the rate: "we’re not earning a higher
rate of return on capital than we were when we started. We just put way more capital into the business" **[M2023-081]**.
The rows accept it as a second best on one condition, "decent returns on the incremental sums they invest"
**[L2009-012]**, and name it "the second-best choice, still a good choice" **[M2018-055]**. FPL's incremental equity
earned about the same rate as its old equity (the book return held at 10% to 12% while equity rose from $29.2B to
$47.0B), so the condition is met at the regulator's rate, no better. Read with care **[L1994-009]**: part of the return
is leverage the regulator allows (40.4% debt in the capital structure), and part is the reserve amortization that steers
the reported figure to the target (Q4).

**NEER and the consolidated company.** NEER's spending is not optional in the business it has chosen: in 2021-2025
NEER's investments were $64.9B, against asset sales of $10.0B, and its cash return on the net growth spending was about
4.1% (Q2). For the whole company, owner cash after all capital spending was negative in every year, from −$5.8B to
−$11.0B after asset sales (`worksheet_out.txt`): "The second business is one that reports the 12 percent on capital but
there’s never any cash" **[M2003-122]**. The rows' third grade is "the one that grows a lot, and where you’re forced
[...] to grow to stay in the game at all, and where you’re reinvesting the capital at a very low rate of return"
**[M1998-081]**; NEER's new capital earning about 4% cash comes near it, and the cash return is below the long
government rate of 5.29%.

**WEIGHS FOR on FPL as a second best** at the regulator's decent rate **[L2009-012]**, **[M2018-055]**; **AGAINST on
NEER and the whole**, where the growth capital earns low cash returns and the company never ends a year with cash
**[M2003-122]**, **[M1998-081]**. Carried. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]**. NEE consolidated, $M, at each
31 December (XBRL 10-K facts, transcription; 2025 checked against the filed balance sheet, `0000753308-26-000015`;
2026-09-30 from the 10-Q, `0000753308-26-000081`). Total debt is long-term debt, its current portion, commercial paper
and other short-term debt.

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-09-30 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 90,474 | 97,963 | 103,702 | 117,691 | 127,684 | 140,912 | 158,935 | 177,489 | 190,144 | 212,721 | 245,052 |
| Net PP&E | 66,912 | 72,289 | 70,334 | 82,010 | 91,803 | 99,348 | 111,059 | 125,776 | 138,852 | 156,197 | n.r. |
| Common equity | 24,341 | 28,236 | 34,144 | 37,005 | 36,513 | 37,202 | 39,229 | 47,468 | 50,101 | 54,608 | 61,498 |
| of which retained earnings | 15,458 | 19,020 | 23,837 | 25,199 | 25,363 | 25,911 | 26,707 | 30,235 | 32,946 | 35,102 | n.r. |
| Noncontrolling interests | 990 | 1,295 | 3,269 | 4,355 | 8,416 | 8,222 | 9,097 | 10,300 | 10,359 | 11,871 | n.r. |
| Total debt | 30,690 | 35,025 | 37,712 | 42,583 | 48,091 | 54,827 | 64,966 | 73,211 | 82,333 | 95,619 | 113,932 |
| Cash | 1,292 | 1,714 | 638 | 600 | 1,105 | 639 | 1,601 | 2,690 | 1,487 | 2,812 | 5,579 |
| Goodwill | 779 | 764 | 891 | 4,204 | 4,254 | 4,844 | 4,854 | 5,091 | 4,866 | 4,849 | n.r. |
| Equity-method investments | 1,767 | 2,321 | 6,748 | 7,453 | 5,728 | 6,159 | 6,582 | 6,156 | 6,118 | 5,528 | n.r. |
| Customer receivables | 1,784 | 2,220 | 2,302 | 2,282 | 2,263 | 3,378 | 4,349 | 3,609 | 3,336 | 4,018 | n.r. |
| Debt / common equity | 1.26 | 1.24 | 1.10 | 1.15 | 1.32 | 1.47 | 1.66 | 1.54 | 1.64 | 1.75 | 1.85 |

(n.r.: not read for that date. 2019 short-term borrowings appear under two tags at $400M each; counted once.)

What the figures say. Assets rose 2.35 times in nine years and debt 3.1 times; common equity rose 2.24 times, and of its
$30.3B rise only $19.6B is retained earnings, the rest new shares (equity units, at-the-market and block issuance:
$1,460M in 2022, $4,514M in 2023, $2,038M in 2025, $969M in nine months of 2026). Noncontrolling interests went from
$1.0B to $11.9B: the tax-equity partners who fund NEER's projects in exchange for their tax credits. Goodwill jumped
in 2019 with the Gulf Power purchase and has been flat since. Receivables moved with revenue and stand lower against
it in 2025 (14.7%) than in 2021 (19.8%); nothing is building up in the current accounts. Cash is a working balance,
never a reserve. What the figures do not say: how much of the rising debt the regulator will let FPL earn on (about a
third of the debt is FPL's: $30.5B of $113.9B at 2026-09-30) and how much sits on NEER's contracted fleet and at the
holding company, where no regulator stands behind it. What management would like them to say: the earnings (below).

**The real costs.**
- *Depreciation* is a true cost **[L2015-004]**, and the reported figure at FPL is not the plain one: FPL credits a
  "reserve amortization" inside D&A, $429M (2021), $114M (2022), $227M (2023), $328M (2024), $593M (2025), and the
  10-K for 2022 states its purpose in so many words: "In general, the net impact of these income statement line items
  must be adjusted, in part, by reserve amortization to earn the targeted regulatory ROE. In certain periods, reserve
  amortization is reversed so as not to exceed the targeted regulatory ROE." The new agreement continues it as a "rate
  stabilization mechanism" of up to about $1.5B after tax through 2029 (10-K FY2025, Item 1). FPL's reported earnings
  are therefore a target reached by a lever, within a band the regulator set. I add the reserve amortization back to
  D&A in the maintenance guess (Q7), which makes the guess larger, not smaller.
- *Stock pay*: $119M to $185M a year (2021-2025), added back inside operating cash; deducted from owner cash in Q7
  **[L2021-003]**.
- *Interest* is paid in cash and sits inside operating cash; on the equity-only basis it is a cost, as it should be.
- *Storms*: "Recoverable storm-related costs" took $2.5B out of operating cash over five years; counted, since storms
  in Florida recur.
- *Taxes*: NEE received cash for taxes, net, in 2021, 2022, 2024 and 2025 ($1,275M received in 2025; $1,893M in nine
  months of 2026), from clean-energy tax credits. Its effective tax rate was negative in 2025 (benefit of $802M on
  pre-tax income of $4,530M). The credits are real cash for the projects that earn them; the law now phases them out
  for wind and solar (Q1). Treated at Q7 under "Whose tax".

**What the accounts say about the earnings figure.** Net income attributable to NEE ($6,835M in 2025) exceeds net
income ($5,332M) by the $1,503M of book losses allocated to tax-equity partners under the HLBV method; over five years
that allocation is $5,426M, 56% of NEER's attributable income. Net income also swings with unrealized marks on hedges
not designated as hedges (a $3,594M gain in nine months of 2026, inside net income of $8,677M). And NEER books gains on
disposing of businesses and assets ($260M to $405M a year inside operating income), including sales to its own
affiliate XPLR (2023: 688 MW for $566M plus working capital), whose units NEE then wrote down by $1.2B (2023), $0.8B
(2024) and $0.7B (2025). The headline figure is "sometimes it’s the all-deceptive figure" **[M2011-003]**; the cash
statements of NEE and of FPL separately are clear, and the run is built on them.

**Tells.** No prepaid or deferred accounts building, no receivables or inventories out of line, no reserve released
into earnings in the manner the rows describe for insurers' and merger reserves **[M2013-085]**: the reserve FPL moves is
authorized by its regulator, is bounded by the ROE band, and its amount is disclosed each year. The accounts confuse in
places (the HLBV allocation, the hedge marks) but are readable from the filings already read, and I could recast them;
they do not raise suspicion by the tells that live in the accounts **[M1995-063]**, **[M2003-029]**.

**The make-the-numbers habit, weighed here and carried to Q5.** NEE uses "adjusted earnings", "a non-GAAP financial
measure, internally for financial planning, analysis of performance, reporting of results to the Board of Directors and
as an input in determining performance-based compensation", and "when communicating its financial results and earnings
outlook to analysts and investors" (10-K FY2025, Item 7). The board's case for the merger is "a compound annual growth
rate in adjusted earnings per share of over 9% through 2032" and a dividend growth policy "of 6% through 2028" (joint
proxy). Executive pay turns on "adjusted EPS growth, adjusted ROE" (proxy). The rows: "a management that regularly
attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**;
the "scourge of earnings "guidance" and the desire of CEOs to "hit the number."" **[L2019-006]**. FPL's own figure is
steered to a target by a reserve, by design. Preoccupation of this kind is "a negative", not "a total exclusionary
factor" **[M1994-018]**.

**VERDICT on the accounts: no STOP** (neither confusion that the filings read cannot cure nor suspicion raised by the
accounts' own tells) **[M1995-063]**, **[M1994-018]**; **WEIGHS AGAINST**: an earnings figure built in large part from
tax-equity allocations, hedge marks and a target-steered reserve, featured and paid on in adjusted form **[M2011-003]**,
**[L2016-006]**. The habit (adjusted earnings featured, guidance, targets) is carried to Q5 **[M2004-067]**. The recast
owner cash feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The question in the row that asks it whole is whether one wants "to be in partnership with this person" **[M2015-005]**; integrity is
the one trait the rows make absolute: "we wouldn’t hire anybody, no matter how able, if we didn’t trust them"
**[M2015-047]**, and it is applied on doubt, not on proof: "If you’ve got doubts, forget it." **[M2013-088]**.

**The people.** John W. Ketchum, president and chief executive since March 2022 and chairman since July 2022; before
that chief executive of NEER (2019-2022) and chief financial officer of NEE (2016-2019) (8-K `0000753308-22-000008`;
proxy). The FPL chief executive of the window, Eric Silagy, retired in 2023; the chief executive before Ketchum, James
Robo, became executive chairman in March 2022 for a transitional period; Ketchum has chaired the board since July 2022
(8-Ks of 2022 and 2023; proxy).

**The integrity record, from the filings, in date order.**
1. Media articles first published in 2021 "allege, among other things, Florida state and federal campaign finance law
   violations by FPL"; a complaint was filed with the Federal Election Commission in October 2022 (10-K FY2023, Item 1A;
   8-K 2023-01-25, `0000753308-23-000011`).
2. On 2023-01-25 the company's chief executive told investors that the review was "substantially complete" and that
   "based on information in our possession, we believe that FPL would not be found liable for any of the Florida
   campaign finance law violations as alleged in the media articles"; the FEC complaint was "filed by a special interest
   group and primarily relies on media articles", and "The total amount of contributions referenced in the complaint is
   less than $1.3 million" (8-K `0000753308-23-000011`). The same day the FPL chief executive's retirement was filed, with
   his 2022 annual incentive paid in full and a pro rata part of his performance shares, restricted shares and options
   left to vest "in accordance with their terms" (8-K `0000753308-23-000010`). The wording of the statement is "would not
   be found liable", not that the conduct did not occur.
3. A shareholder securities class action against "NEE, FPL, and certain current and former executives", over "alleged
   false or misleading statements regarding NEE's alleged campaign finance and other political activities", class period
   2021-12-02 to 2023-01-30, was dismissed in September 2024; "in November 2025, a panel of the U.S. Court of Appeals for
   the 11th Circuit reversed the dismissal and remanded"; in June 2026 the parties agreed that "NEE would pay an aggregate
   of $ 150 million", covered by insurance; the court denied preliminary approval in August 2026 "requesting additional
   information" and a renewed motion was filed in October 2026 (10-Q Q3 2026, legal proceedings).
4. Shareholder derivative actions naming current and former officers and directors, the present chief executive among
   them (Davis v. Ketchum; Worrell v. Ketchum; Lewis v. Ketchum), "allege that certain of the Company’s directors and
   officers breached their fiduciary duties in connection with an alleged political influence scheme tied to improper use
   of “dark money” funding, among other related misconduct, to manipulate public policy favorable to the Company". They
   are being settled for about $16M paid by insurers to NEE and nine governance reforms, among them "the appointment of
   one new independent director with political and/or legislative experience", "enhanced Board obligations related to
   oversight of political contributions", and "enhanced duties of the Chief Compliance Officer with respect to overseeing
   the Company’s compliance with campaign finance laws"; a hearing is set for 2026-12-14. "Each of the Individual
   Defendants denied and continues to deny that he or she has committed or attempted to commit any violations of law"
   (8-K `0000753308-26-000074`, Exhibit 99.1).
5. The FEC complaint is not mentioned in the 10-Ks for FY2024 and FY2025 (no instance found by a search of those two
   filings and the Q3 2026 10-Q for "FEC" and "Federal Election Commission"); its outcome is not stated in the filings
   read.

**The case for, stated as its holder would state it** (the analyst's habit, **[M1997-127]**): no court, regulator or
election authority has found a violation in the filings read; the defendants deny everything; settlements of
securities and derivative suits are commonly made to end cost, and insurers pay these; the sums named in the FEC
complaint were under $1.3M against a company earning billions; the executives who ran FPL then have gone; the board has
added a lead director and is adopting reforms; the 2023 review found FPL would not be liable under Florida law.

**The case against, which decides.** The allegation goes to the heart of this business: FPL's return is whatever its
regulators and legislators allow (Q2), and the allegation is that the company used concealed political money "to
manipulate public policy favorable to the Company". A federal appeals court found the securities claims fit to go
forward; the company then agreed to pay $150M rather than try them; the derivative settlement's reforms are aimed at
exactly the conduct alleged (political contributions, campaign-finance compliance, the disclosure committee, the
hotline). The present chief executive was the chief executive during most of the class period and is a named defendant
in three of the derivative actions; the investor statement of 2023-01-25 framed the matter as a special-interest
complaint built on press reports, and it falls inside the class period of the action now being settled. The rows'
front-page test is met in the literal sense: a course of action that, "if put on the front page, you know, would make
you very unhappy, you can get in a lot of trouble. It may take a while." **[M2016-033]**. "People are not that easy to
read. Sincerity and empathy can easily be faked." **[L2023-003]**; "everybody mouths the integrity, even when it’s
lacking" **[M2010-069]**; a long reputation is not proof **[M1995-066]**. The habits carried from Q4 (adjusted earnings
featured and paid on, earnings guidance, a reported figure steered to a target) are "things that they do in public in
relation to their investors and the promises they make" **[M2004-067]** and read in the same direction, though alone
they would only weigh.

I cannot resolve this from the filings, and the rows say I need not: "we rule out 90 percent of the times. And we may be
wrong about a fair number that we’re ruling out. The important thing is whether the ones we’re ruling in we’re right
about." **[M2007-092]**; "you can’t make a good deal with a bad person. [...] we don’t try and protect ourselves by
contracts" **[M1995-084]**, and governance reforms written into a settlement are such a contract. I have doubts about
whether the people who run NEE, the present chief executive among them, would act, after they hold my money, as the
company's political conduct under them is alleged and has not been answered on the merits. The rule is "If you’ve got
doubts, forget it." **[M2013-088]**.

**Ability, weighed for the record (not reached as a decision).** The first yardstick, the record against the hand dealt
**[M1994-008]**: FPL's book return (10.9%) sits in the upper half of its Southeastern peers and steadier than any of
them (Q2); NEER's new capital has earned about 4% in cash (Q2), $2.7B of the XPLR stake was written off in three years,
and the consolidated company has never ended a year of the window with cash after spending (Q3). The second, the
treatment of owners **[M1994-009]**: the chief executive's 2025 pay was $24.2M (pay ratio 147 to 1), with annual and
long-term incentives tied to "adjusted EPS growth, adjusted ROE" and relative shareholder return (proxy); he owns 412,689
shares directly (about $34M at the price), with options on 1,065,839 more; the chairman and chief executive are one
person, with a lead director.

**VERDICT on integrity: OUT**, on doubt **[M2013-088]**, **[M2016-033]**, **[L2023-003]**, **[M2007-092]**. The file closes
here. Ability: not decided; the record above weighs mixed (FPL for, NEER and the capital record against)
**[M1994-008]**, **[M1994-009]**. Q6 to Q12 are NOT REACHED; what follows them is facts and COMPUTATION, NOT A
CLEARANCE.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED** (Q5 closed the file). Facts found are under AFTER THE STOP, Q6, not weighed.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED** as a clearance (Q5 closed the file). The value range and the fair price the brief's reporting
convention asks for are computed under AFTER THE STOP, Q7, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q5 closed the file).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED** (Q5 closed the file). Facts found are under AFTER THE STOP, Q9, not weighed.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED** (Q5 closed the file).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (Q5 closed the file). Facts found are under AFTER THE STOP, Q12, not weighed.

---
## THE BOX
**OUT, at Q5, on integrity (doubt)** **[M2013-088]**: campaign-finance and "dark money" allegations about how FPL sought
political outcomes, a securities class action over the company's statements about them revived on appeal and being
settled for $150M, and derivative actions naming the present chief executive being settled with political-oversight
reforms; the defendants deny all of it and no violation has been found in the filings read. Q1 IN and Q2 IN on FPL,
the deciding part; Q3 weighs for on FPL as a second best and against on NEER and the whole; Q4 no STOP, weighs against.
COMPUTATION, NOT A CLEARANCE: value range $25.45 to $37.77 a share (equity-only, the regulated-utility basis as read)
against $81.90; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q5 closed the file. What follows is written down, not weighed; no verdict; the box is unchanged (operator rule 2).
Each fact with its source **[M1997-127]**.)*

### Q6 (the money and the owners), facts
- No buybacks in the window (cash-flow statements 2021-2025; none in nine months of 2026). Dividends paid rose from
  $3,024M (2021) to $4,680M (2025), $2.27 a share in 2025, while owner cash after all capital spending was negative in
  every year (Q3); the board's stated policy is dividend growth "of 6% through 2028" (joint proxy).
- Common stock and equity units issued: $14M (2021), $1,460M (2022), $4,514M (2023), $48M (2024), $2,038M (2025),
  $969M (nine months of 2026); about 329M shares reserved for financings at 2026-07-24 (joint proxy). The serial-issuer
  row **[L2014-015]** is the framework's candidate second STOP; not judged.
- The Dominion merger is paid almost wholly in shares: 0.8138 NEE shares per Dominion share plus a pro rata share of
  $360M (8-K `0001104659-26-063001`); about 716M NEE shares, so that NEE's holders keep about 74.5% (joint proxy);
  approved by NEE's holders on 2026-09-03 with 99.47% of votes cast (8-K `0000753308-26-000071`). Termination fees: NEE
  pays $6.52B or, on certain regulatory failures, $4.83B; Dominion pays $2.24B. Customer bill credits of about $2.25B
  over two years after closing; charitable giving up about $10M a year for five years (joint proxy). The Q6 STOP on an
  all-stock deal by an acquirer whose stock is below its value (Q6, Part A; the row is **[L2009-019]**) turns on whether NEE's stock is below its value: on the
  COMPUTATION under Q7 below the price is above the top of every range computed, so the stock given is not shown to be
  undervalued. On the no-growth, maintenance-only basis the deal buys Dominion's owner cash at about 23 times (value
  given about $59.0B against Dominion's five-year average maintenance-only owner cash of about $2.56B), against NEE's own
  41 times; the combined figure per share is higher than NEE's alone (below). Not weighed.
- XPLR (formerly NextEra Energy Partners), the affiliate to which NEER sold projects: impairments of the stake of $1.2B
  (2023), $0.8B (2024) and $0.7B (2025) (10-K FY2025, Note 4); in 2025 XPLR suspended its common distribution
  "for an indefinite period" (same note).
- Pay (proxy): chief executive's 2025 total $24.2M; annual incentive scorecard at 189% on "adjusted EPS growth,
  adjusted ROE, and operational goals"; performance shares initially at 198%, cut to 158% for relative TSR. Chairman
  and chief executive one person, with an independent lead director. The derivative settlement adds an independent
  director "with political and/or legislative experience".

### Q7 (what it is worth): COMPUTATION, NOT A CLEARANCE
*All figures from `worksheet.py`, run 2026-10-23; $M unless per share; 2,097.306M shares; price $81.90; long government
rate 5.29%.*

**The basis, and how I read the regulated-utility paragraph for a company of two parts.** The paragraph applies
"Where the deciding part of a business (Q2, a business of parts) earns a return a regulator allows": FPL decides (Q1,
Q2) and earns an allowed return, so **the central figure is the equity-only basis for the whole company**: owner cash
after interest and after the company's tax, against the market value of the shares. The debt credit is applied as the
paragraph states it, to "the long-term debt raised over the window to fund the fixed assets ... up to the debt share
of the capital structure the regulator allows": FPL's net long-term debt raised ($11,363M over five years) against
FPL's capital spending, capped at 40.4% (the 2025 agreement's 59.6% equity ratio). NEER's debt gets no credit, since
"Merchant generation and unregulated renewables, priced by a market, stay on the all-equity basis", and no regulator
allows NEER a debt share. Beside the central figure: the all-equity basis for the whole company, and a sum-of-parts
reading (FPL equity-only plus NEER and Corporate on the all-equity basis, less their net debt by difference), shown
because the paragraph does not say how a company of two parts is read.

**Owner cash.** Operating cash (after interest and the company's own tax), less stock pay ($119M to $185M), less
distributions to tax-equity partners ($179M, $75M, $740M, $516M for 2022-2025; 2021 not stated separately and taken as
nil), less the maintenance guess. **The maintenance guess** **[M2000-144]**, **[L1999-024]**: D&A, with FPL's reserve
amortization added back, plus nuclear fuel purchases ($4,628M to $7,726M a year), on the rows' allowance that
depreciation "is not inappropriate in most companies to use as a proxy for required capital expenditures"
**[M1998-127]**; the rows also say utilities' depreciation can be "inadequate" **[M2015-049]**, so the guess may be low
and the owner cash high.

| equity-only, $M | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| owner cash after maintenance only | 2,806 | 3,101 | 4,796 | 6,193 | 4,058 | **4,191** |
| the same, fuel-clause timing removed (for the growth rate only) | 3,405 | 4,566 | 3,692 | 5,177 | 4,147 | 4,197 |
| owner cash after all spending (FPL debt credit, asset sales and tax-equity proceeds credited) | −1,819 | −3,119 | −4,676 | −5,947 | −6,467 | −4,406 |

**The specifics, one by one.** (a) Cycles: no peak or trough; but FPL's fuel-cost recovery clause took $599M and
$1,465M out of operating cash in 2021 and 2022 and returned $1,104M and $1,016M in 2023 and 2024 (five-year net −$33M),
timing the filer ties to fuel costs; it leaves the average unchanged and makes the literal end-year growth meaningless,
so the growth is measured on the series with the clause timing removed (5.1%) and the literal window (9.7%) is shown
beside, per (a) and (d). (b) Decline: none on the maintenance-only series; the all-spending series is negative in every
year, so no range is built on it. (c) Acquisitions: none of size in the window; asset and business sales ($9,982M by
NEER, $924M of Florida City Gas) are credited against spending in the growth case. The signed, unclosed Dominion merger
is valued beside, not in the central figure. (d) Working capital: counted inside operating cash. (e) Growth spending:
the central case is owner cash after maintenance only, and the growth case charges the window's average growth spending
for the ten years of growth: FPL's spending above maintenance less the debt credit ($2,698M) plus NEER and Corporate's
spending above maintenance less asset sales and tax-equity proceeds ($5,899M), $8,597M a year. (f) The cap: year-ten
owner cash at 5.1% is $6,860M, 7.7% of sales grown at the window's own 12.6% sales growth, below the highest share in
the window (25.0%): no cut. After year ten, zero growth and no growth spending.

**The range at 5.29%:** no-growth case **$37.77** a share; growth case **$25.45** a share. The growth bought is worth
less than its cost at the long government rate, so by (e) the no-growth case is the top and the growth case the bottom:
**$25.45 to $37.77, against $81.90**. Width 1.5 to 1. Literal-window growth (9.7%), shown beside: $50.69.
**The floor, tested first:** the expected return at $81.90 is 2.44% on the no-growth case and 2.66% on the growth case;
even with no growth spending charged at all (which (e) forbids, shown only as the outer bound) it is 3.74%. No case
earns about ten percent at the price: on the floor convention the computation would close OUT, and the price is above
the top of every range computed.
**Beside, all-equity basis:** $2.34 (no growth) and −$9.87 (growth) a share at 5.29%, after net debt of $108,353M at
2026-09-30 (debt $113,932M less cash $5,579M; finance leases inside long-term debt; operating leases left out).
**Beside, sum-of-parts reading:** $9.82 (no growth) to $68.42 (growth) a share at 5.29%.
**Beside, the signed Dominion merger as if closed** (merger paid in shares; combined averages, 716M shares added, the
$360M cash and the $2.25B of bill credits after tax at 21% deducted; Dominion's operating cash and D&A from its XBRL
facts, 2025 checked against its 10-K): no-growth, maintenance-only, $44.62 a share at 5.29% (NEE alone $37.77).
Dominion's growth leg is not computed: its window contains the sale of its gas distribution businesses and a
restatement its 10-K reports, neither read.

**Whose tax, not applied in full.** NEE's owner cash includes tax credits received in cash (net tax receipts of
$1,275M in 2025). The convention computes owner cash at the statutory rate and adds the shelter's present value where
credits "run out inside ten years". Each project's credits run ten years and the fleet's are renewed by new building
until the phase-out, so the convention fits awkwardly; I did not apply it. As an order of size only: tax at 21% on
2025's $4,530M of pre-tax income would be about $950M paid instead of $1,275M received. Applied, it would lower owner
cash and every figure above; the figures here are high on this point.

**The two reporting figures (reporting convention, not a verdict, no entry language):**
- **Value range: $25.45 to $37.77 a share** (equity-only, central, regulated-utility basis as read above), against
  $81.90.
- **Fair price: $11.53 a share** on the equity-only basis (central): the no-growth end valued at ten percent is $19.98
  and the growth end $3.07, averaged. **All-equity basis, beside: −$33.00** (ends −$23.09 and −$42.91; not positive).
  Sum-of-parts reading, beside: −$6.13. Merger as if closed, no-growth end only at ten percent: $23.25.

### Q9 (the target's debt and exposures), facts
- Total debt $113,932M at 2026-09-30 against common equity $61,498M (1.85 to 1); $95,619M at 2025-12-31; $30,690M at
  2016-12-31. FPL's share: $30,520M (10-Q).
- Coverage, pre-tax earnings plus interest expense over interest expense **[L2012-002]**: 2.0 times (2025: $9,102M over
  $4,572M), 3.7 times (2024), 3.2 times (2023); cash interest paid $3,501M in 2025, against $1,323M in 2021.
- Liquidity: net available liquidity about $18.7B at 2025-12-31 and $19.3B at 2026-09-30 (10-K; 10-Q).
- Sudden demands for cash **[L2014-024]**: a downgrade of FPL and NEECH to BBB/Baa2 would require about $650M of
  collateral; guarantees of about $7.1B (PPAs, acquisitions, interconnection, nuclear and other obligations), about $3.0B
  in place of collateral on project financings, and about $1.6B of net mark-to-market exposure on trading guarantees
  (10-K FY2025, Guarantee Arrangements). The merger's termination fees payable by NEE ($6.52B; $4.83B on certain regulatory failures).
- No property insurance for a substantial portion of FPL's transmission and distribution property; storm costs
  recovered by surcharge subject to prudence review (10-Q).
- The "little or no debt" criterion **[R1997-001]** is stated for whole businesses; not judged.

### Q12 (how the money is made), facts
- The allegations recorded at Q5 concern how FPL sought political outcomes; the newspaper test **[M2008-011]** is the
  instrument the framework names. Media articles were written (10-K FY2023, Item 1A). Not judged.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 7904fae8); written question by question; committed after each
      (Q1 8b9ed537, Q2 1055802a, Q3 c61d4036, Q4 02a0a6ff, Q5 d69c8c28, after the stop a38053ad, then the close).
- [x] Dispatched: the brief allowed per-question pathspec commits of this file and the research folder only; the lock in
      `Screens/_daily/` is the dispatching session's and was not touched. The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the one filtered
      listing of `Test Runs/` declared at the top (three other companies' file names seen, none opened). Contamination
      declared there.
- [x] Every v5 id resolves and every fragment quoted beside an id is in that row (`check_ids.py` in the research
      folder, output in `check_ids_out.txt`); every filing fact carries its accession or names its filing; no number
      without a filing or a CONVENTION.
- [x] The order was kept; Q5 closed the run; nothing after it is a clearance, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE. **Declared:** the owner-cash arithmetic in `worksheet.py` (needed for Q3 and Q4) was
      run, and its rough Q7 lines were printed, before Q5 was written. When I judged integrity I already knew the price
      stood far above every case I could build. The Q5 verdict rests on the litigation and the filings named there, but
      a reader should know the order in which I saw things: a run that already "knows" the answer is OUT on price has
      an incentive to close early on a softer ground, and the reverse.
- [x] Owner cash after every real cost (stock pay, interest, tax-equity distributions and a maintenance guess
      deducted), never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price from an
      aggregator, flagged.
- [x] Contrary evidence written down as it was found (foundations); the facts for later questions are under AFTER THE
      STOP. The Q5 facts were judged at Q5, so the box line carries no "recorded, not judged" flag.
- [x] Not a point-in-time run; no row was barred by an anchor.
- [x] `tools/run.py` printed no arithmetic for NEE ("UNRESEARCHED"); nothing of it was used. All sums are in
      `worksheet.py` from the filed statements.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the close).
- Gaps, honestly: the maintenance guess is depreciation-based and may be low for a utility **[M2015-049]**; the "Whose
  tax" convention was not applied (figures high on that point); 2021's distributions to tax-equity partners are not
  stated separately and were taken as nil; Dominion's growth leg was not computed; the comparators' returns are from
  XBRL tags (equity may include preferred) and were not cross-checked against their filed statements except Dominion's
  2025 operating cash; the FEC complaint's outcome, the 11th Circuit's opinion and the content of the media articles were
  not read (they are not SEC filings).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The regulated-utility paragraph does not say how to read a company of two parts.** It keys the equity-only basis
   on "the deciding part" but then says "Merchant generation and unregulated renewables ... stay on the all-equity
   basis". For NEE (FPL deciding, NEER a large unregulated part) three readings give very different figures: the whole
   company equity-only with the regulator's debt credit for FPL only (central here, fair $11.53), a sum of parts with
   NEER on the all-equity basis (fair −$6.13), and the whole company all-equity (fair −$33.00). I took the literal
   reading as central and showed the others beside; the operator should say which governs.
2. **The debt credit has no rule for the no-growth case.** A utility that only maintains its rate base raises no net
   new debt, so I credited FPL's net long-term debt raised only against growth spending, capped at 40.4% of FPL's
   spending; the paragraph's words could also be read to credit the window's debt in every case.
3. **Tax-equity money is not addressed.** NEER's projects are part-funded by "differential membership" investors who
   take the tax credits; their cash goes in as financing and their returns largely never pass through NEE's operating
   cash. I credited their proceeds against NEER's spending and deducted their distributions (a CONVENTION of this run,
   rationale: charging the whole project cost while its tax credits stay outside owner cash would charge the same asset
   twice). A rule is needed; the effect on this run is large on the all-spending series.
4. **"Whose tax" does not fit a fleet whose credits are renewed by building.** Each project's credits run ten years,
   but the fleet's are renewed until the phase-out; the convention's "run out inside ten years" test cannot be applied
   cleanly. Not applied; the direction of the error is stated.
5. **Q2's business-of-parts threshold says "operating profit".** NEE reports no operating profit by segment, only net
   income attributable (the CODM's measure), which includes the HLBV allocation that is 56% of NEER's five-year figure.
   I used the reported measure; on any measure FPL decides, but a closer case would turn on the choice.
6. **Q5's doubt rule meets unresolved litigation without guidance.** The rows close on doubt, and the framework says how
   habits carried from Q4 are read, but not whether allegations that survive a motion to dismiss and are settled
   without admission, with reforms aimed at the conduct alleged, are doubt. I judged them doubt and said why; another
   analyst could weigh them instead and reach Q7, where the computation closes the file anyway.
7. **Q7 (e) gives no method for "the growth spending charged against the growth it buys".** I held the window's average
   growth spending for the ten years of growth and stopped it at year ten; holding it at the last year's level (about
   double) would lower the growth case further.
8. **The maintenance guess for a utility whose D&A includes a regulatory reserve.** FPL's reported D&A is net of a
   reserve amortization used to hit a target ROE; I added it back. The framework's maintenance guess **[M2000-144]** says
   nothing of regulatory amortizations inside D&A.
