# Company Run: Upwork Inc. (NASDAQ: UPWK), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template before any fetch; working folder `Test Runs/_research 2026-10-06 UPWK/`.)*

**POSITION NOTE, declared before any verdict:** NOT CHECKED. The run is blind: the dispatch forbids opening
`PORTFOLIO.md`, any holding review, the resume-state files, the register and the reading list, and none was opened.
Whether the operator holds UPWK is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The session's opening context showed the five most recent commit subjects, all other
companies' v5 runs (LRN, INSW, NX, MTCH) and one tool change (`run.py`: vessel purchases); they name no fact about
Upwork. One of them (MTCH, "TOO HARD (NATURE) at Q1 ... low switching costs and free rivals") is a closing pattern on a
two-sided online business; I record it as a pull toward the same box and have tried to let the Upwork filings decide.
(2) The git status in the same context lists three untracked 2026-10-06 run files (CVSA, EMN, WWW) by name only; none
was opened. (3) The dispatch itself describes the business ("take rate on gross services volume; formed from the
Elance-oDesk merger") and asks what the filer says "about AI and lower-cost freelance work"; that framing names the
hypothesis against the business before any reading, and I record it as a steer. (4) My own general knowledge of
Upwork, Fiverr and the freelance market before this run (prices in 2021, the Elance-oDesk merger in 2013/2014) is
background only; no number below comes from it.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $8.36 (close 2026-10-05; `tools/run.py` live quote, **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: common stock, $0.0001 par, **124,903,365** shares (10-Q for the
  quarter ended 2026-06-30, filed 2026-08-10, accession `0001627475-26-000047`, cover as of 2026-07-31;
  `python Screens/cover_shares.py UPWK`). One class only. The balance sheet of the same 10-Q shows 124,797,586 issued and
  outstanding at 2026-06-30.
- **Market cap:** 124.903M × $8.36 = **$1,044M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (via `tools/run.py`, which calls `tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-13, accession `0001627475-26-000012` (business, risk factors, MD&A, statements, notes).
  - 10-Q for Q2 2026, filed 2026-08-10, accession `0001627475-26-000047`; 10-Q for Q1 2026, filed 2026-05-07,
    accession `0001627475-26-000034`.
  - Proxy (DEF 14A), filed 2026-04-23, accession `0001627475-26-000026`.
  - 8-Ks: `0001627475-26-000046` (Q2 results, 2026-08-10), `0001627475-26-000042` (CFO medical leave, 2026-07-14),
    `0001627475-26-000039` (secured revolver, 2026-06-23), `0001627475-26-000036` (annual meeting, 2026-06-04),
    `0001627475-26-000033` (Q1 results and the 2026 restructuring, 2026-05-07), `0001627475-26-000018` (GM Marketplace
    departure, 2026-03-12), `0001627475-26-000015` ($300M buyback authorization, 2026-02-18), `0001627475-26-000005`
    (FY2025 results and bylaw amendment, 2026-02-03), `0001627475-25-000063` (new chief accounting officer, 2025-12-08),
    `0001627475-25-000050` (new COO, 2025-08-12), `0001627475-25-000037` (chief accounting officer resignation,
    2025-07-21).
  - Earlier 10-Ks and the 2018 S-1 for the span: listed where used below.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
    **$248,259 thousand** in the filed consolidated statement of cash flows (10-K `0001627475-26-000012`), equal to
    `tools/run.py`'s 248.3 (XBRL). SBC 65,390 and the two capex lines (property and equipment 5,790; internal-use software
    and platform development 19,349; sum 25,139) also match.
- **Customer money is not the company's cash.** "Funds held in escrow, including funds in transit" ($180.8M at
  2025-12-31; $193.3M at 2026-06-30) is matched by an equal "Escrow funds payable" liability, and its change runs through
  **financing**, not operating, cash flow ("Change in escrow funds payable, net", FY2025 −6,731). So the operating cash
  flow above is clean of customer funds, and the escrow is excluded from the company's cash below.
- `python tools/run.py UPWK`, arithmetic lines only (USD millions; owner cash = OCF − SBC − capital spending, where
  capital spending = property and equipment + capitalized internal-use software):

| FY | OCF | SBC | capex (incl. capitalized software) | D&A | owner cash, capex basis | owner cash, D&A basis |
|---|---|---|---|---|---|---|
| 2021 | 10.8 (filed, not recast) | 53.6 | 6.1 | 10.3 | −48.9 | (not computed) |
| 2022 | 11.5 (6.6 filed + 4.9 recast) | 75.5 | 8.7 | 8.1 | −72.8 | (not computed) |
| 2023 | 52.7 | 74.2 | 13.4 (16.4 with a $3.0M intangible purchase) | 9.4 | −34.8 (−37.8) | −30.9 |
| 2024 | 153.6 | 68.4 | 14.4 | 14.8 | 70.7 | 70.4 |
| 2025 | 248.3 | 65.4 | 25.1 | 25.7 | 157.7 | 157.2 |

  `run.py`'s five-year window (FY2021 to FY2025) gives a mean owner cash of **$14.4M** (capex basis) and $15.5M (D&A
  basis); its three-year window gives $64.2M to $65.8M. "The spread between the windows is part of the range." The
  2021 and 2022 rows were read from the FY2023 10-K's cash-flow statement (`0001627475-24-000012`); 2022's OCF carries the
  $4.9M recast the FY2024 10-K discloses (see Q4 evidence below), 2021 is as first filed (the recast did not reach it). SBC is complete for every year (one tag,
  `ShareBasedCompensation`). `run.py`'s printed "yield", "growth the price assumes" and "points over the sovereign" are
  not used (Part VII: arithmetic lines only).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own Upwork "if the market closed for five years"
**[M1997-109]**, and that turns entirely on where its work-buying clients will be in five years, which is the Q1 question
below. The market serves and does not instruct: the price has fallen to $8.36 against $13.24 paid by the company itself for
its own shares in H1 2026 (10-Q `0001627475-26-000047`), and the fall "just tells us prices" **[M2006-077]**; it is not
evidence either way. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think
about" **[M1996-084]**. No macro enters: the filer blames part of the 2026 decline on "macroeconomic uncertainty"; that half
is set aside and only the business half (AI and client acquisition) is weighed. Who is paid to tell you: the filer's own
language ("the world’s human and AI-powered work marketplace") is a seller's description and is read as such.

**Contrary evidence, written down as found** **[M1997-127]**:
1. (against) Active clients have fallen from 851 thousand (2023) to 832 (2024), 785 (2025) and 763 (2026-06-30); the FY2025
   10-K says "driven by slower growth in acquisition of new clients as well as lower retention of existing clients" and the
   Q2 2026 10-Q says GSV and active clients "declined ... driven by the evolving impact of AI on certain categories of
   freelance work and on new client acquisition and retention" and "We expect these headwinds to continue".
2. (against) GSV has not grown since 2022: $4,104.9M (2022), $4,142.3M (2023), $4,008.1M (2024), $4,028.4M (2025), and
   −2% in H1 2026 ($1,952.5M against $1,990.4M).
3. (for) Marketplace take rate rose from 13.1% (2019) to 18.7% (2025) and 19.6% (Q2 2026), and owner cash went from
   −$72.8M (2022) to +$157.7M (2025). Read against item 1, the rise was bought by charging the same or a shrinking base more
   (client fee 3% in the FY2019 and FY2021 10-Ks, 5% now; talent fee tiered, then a flat 10% in 2023, then 0% to 15%
   "variable" from May 2025; Connects and ads sold to talent), and the filer itself warns that pricing changes cause
   "increased circumvention rates".
4. (against) The 2026 restructuring cut "approximately 24%" of the workforce (8-K `0001627475-26-000033`), the second large
   cost cut after 2024, while CEO total pay rose from $9.93M (2024) to $17.09M (2025) (proxy `0001627475-26-000026`).
5. (for, partly) GSV per active client rose 7% in 2025 and 5% to June 2026; the filer says "AI-related work" GSV "has
   increased as demand for AI talent has grown". Fiverr reports the same split (high-skilled up, simple work down).
6. (against) Fiverr, the nearest listed peer, reports annual active buyers falling from 4.3M (2022) to 3.1M (2025) "including
   as a result of AI technologies reducing demand for simple and low-skilled services" (20-F `0001178913-26-000858`).

## THE STANDING RULE
Owning UPWK would be bought with cash, never with borrowed money ("borrowed money has no place in the investor's tool
kit" **[L2014-005]**), and sized so that its loss to zero changes nothing ("never going to risk what we have and need for
what we don’t have and don’t need" **[M2012-081]**). No ruin to the buyer arises from the purchase as such; the
file closes before any sizing question.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" and "some notion of how the industry will develop and where the
company will stand within the industry" **[M2012-065]**; "a reasonable probability of being able to asses where the
business will be in 10 years" **[M2000-037]**. The product is not the question: "we understand the product. [...] We just
don’t know the economics of it 10 years from now" **[M2000-104]**.

**What the business is, from the filings.** A two-sided online market: clients post work, independent talent bids (paying
for "Connects", virtual tokens "required for talent to bid on projects"), the work is paid through Upwork's escrow, and
Upwork keeps a fee from each side plus ads, memberships, payments and currency fees. Marketplace revenue was $682.9M of
$787.8M total in FY2025; Enterprise (now "Lifted", including the 2025 acquisitions of Ascen and Bubty) $104.9M (10-K
`0001627475-26-000012`). The product is easy to understand. The company was formed by the combination of Elance and oDesk;
"We have incurred net losses in each fiscal year since the combination of Elance and oDesk" (prospectus 424B4,
2018-10-03, `0001193125-18-291879`); the first full year of positive GAAP net income was 2023.

**The key variables**, and "how predictable they were" **[M1998-044]**: (1) the volume of knowledge work that businesses will
buy from independent people over the internet ten years out; (2) the share of it that flows through Upwork rather than
direct hire, rival platforms, staffing firms or circumvention; (3) the fee Upwork can keep on it. The span shows each:

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 / mid-2026 |
|---|---|---|---|---|---|---|---|---|
| GSV ($M) | 2,087 | 2,524 | 3,547 | 4,105 | 4,142 | 4,008 | 4,028 | 1,952 (H1, −2% y/y; Q2 −4%) |
| Active clients (000) | 540 | 633 | 771 | 814 | 851 | 832 | 785 | 763 (−4% y/y) |
| Marketplace take rate | 13.1% | 13.6% | 13.2% | 13.8% | 15.4% | 18.0% | 18.7% | 19.6% (Q2) |
| Total revenue ($M) | 300.6 | 373.6 | 502.8 | 618.3 | 689.1 | 769.3 | 787.8 | 387.1 (H1, flat y/y) |
| Sales and marketing ($M) | 95.9 | 133.2 | 183.3 | 246.9 | 220.7 | 185.2 | 143.4 | 72.4 (H1) |

Sources: 10-K FY2019 `0001627475-20-000006`; 10-K FY2021 `0001627475-22-000009`; 10-K FY2023 `0001627475-24-000012`
(the 2022 and 2023 take rates as recast there to exclude Enterprise Solutions; the 2019 to 2021 rates are as first
reported, before that recast, so the step from 2021 to 2022 is partly a definition change); 10-K FY2025
`0001627475-26-000012`; 10-Q Q2 2026 `0001627475-26-000047`. Sales and marketing from the filed income statements via
XBRL, cross-checked to the FY2025 statement for 2023 to 2025.

**Variable 1 is the one that cannot be foreseen, and the filer says so in its own words.**
- "The market for online independent talent and the services they offer is relatively new, rapidly evolving, and unproven,
  and it is difficult to predict the size, growth rate, and expansion of this market. [...] The overall demand for
  independent talent will continue to be impacted by competition in the marketplace, technological developments
  (including AI)" (10-K FY2025, risk factors; repeated in the Q2 2026 10-Q).
- "The market for contingent work is characterized by rapid technological change, frequent product and service
  introductions and enhancements, changing customer demands, and evolving industry standards" (same filings).
- Clients may leave "if AI tools provide a suitable replacement for traditional talent tasks" (10-K FY2025), and in
  Q2 2026 this moved from a risk to a reported fact: "GSV and active clients declined during these periods driven by the
  evolving impact of AI on certain categories of freelance work and on new client acquisition and retention, as well as
  macroeconomic uncertainty. We expect these headwinds to continue to impact GSV, active clients, and revenue in the
  remainder of 2026" (10-Q `0001627475-26-000047`, MD&A).
- A new competitor class appears in the Q2 2026 10-Q that is not in the FY2025 10-K's list: "companies offering AI agents
  and tools that automate specific job functions, workflows, or knowledge work tasks".
- The channel that brings new clients is moving too: "AI-generated search alternatives and AI-related and other changes to
  search engine results pages have emerged recently, affecting new customer acquisition and resulting in changes to our
  customer acquisition strategy" (Q2 2026 10-Q).
- The nearest competitor writes the same: annual active buyers have been "declining, including as a result of AI
  technologies reducing demand for simple and low-skilled services on our marketplace, and future growth could be volatile
  and differ significantly from one year to another. [...] we cannot accurately predict or guarantee annual active buyer
  growth rates in the future" (Fiverr 20-F FY2025, `0001178913-26-000858`).

**The tests applied.**
- *Where will it be in ten years?* "You’re trying to print the next 10 years of Value Line in your head. And there’s some
  companies that you can do a reasonable job with, and there’s others that are just too tough." **[M1999-132]** I cannot
  print Upwork's GSV line for 2036: the same span shows +41% (2021) and −4% (Q2 2026), and the force now acting on it, AI
  substituting for some of the very work sold while creating demand for other work, has no history to read.
- *Do the past statements tell me the future ones?* **[M2008-033]**: no. The 2019 to 2022 statements describe a market
  growing on remote work and heavy marketing; the 2024 to 2026 statements describe a shrinking client base monetized
  harder. Neither tells me which regime holds in 2030.
- *Important and knowable?* The share of freelance knowledge work that AI agents replace, and how much new AI-related work
  offsets it, is the most important variable, and "If something’s important but unknowable, forget it." **[M2006-076]**
- *Would the insiders write it down?* The test is whether "They would say, “That’s too hard.”" **[M2000-105]**. Both
  insiders on the public record say it in effect: Upwork that the market's size and growth are "difficult to predict",
  Fiverr that it "cannot accurately predict" buyer growth. No instance found of either publishing a multi-year forecast of
  the volume of work bought (searched the FY2025 10-K, the Q2 2026 10-Q and the Fiverr FY2025 20-F for "long-term",
  "2030" and "target" near GSV, GMV and buyers).
- *Can I name the winner, not just the industry?* "there’s industries we know that may have a wonderful future, but we
  don’t have the faintest idea who the winners will be" **[M2012-067]**. If AI-related work grows, the filer's own list of
  rivals includes "well-established internet companies" and AI-agent sellers, and "businesses can easily and quickly
  launch online or mobile platforms and applications at nominal cost by using commercially available software" (10-K
  FY2025).
- *Customers or technology?* **[M2017-019]**, **[M2023-030]**: the forecast is about customer behaviour (will a small
  business hire a freelancer or prompt an agent?), but that behaviour is being set by a technology that moved enough
  between the 10-K (February 2026) and the Q2 10-Q (August 2026) to add a competitor class, so it is a technology forecast
  in another form.
- *How far off could I be?* **[M2011-084]**: very far. The computations below put the value between about $3.50 and $39
  a share depending only on which years are taken as normal and which way GSV moves.
- *Do I doubt it is inside?* "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**

**The routing.** "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations
of its long-term economics" **[L1993-023]**; "where we think the future technology could hurt the business as it presently
exists [...] it won’t make it through the filter." **[M1998-008]**; "whenever we look at a business and we see lots of
change coming, 9 times out of 10, we’re going to pass on that." **[M1999-063]** The framework fixes the route: a business
whose ten-year economics cannot be foreseen because its industry changes fast closes at Q1, TOO HARD, not OUT. This is not
a finding that the business is bad or dear: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a
fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**

**The case for the other side, stated as strongly as I can.** Upwork is the largest of the listed general freelance
markets by volume ($4.0B GSV against Fiverr's $1.07B marketplace GMV in 2025); GSV per active client keeps rising; the filer
reports AI-related work growing; owner cash rose to $157.7M in 2025 at a market value of $1.04B; and a market that matches
buyers to sellers of skilled work could gain from AI if the work that remains is harder and more valuable. All of that may
prove right. None of it lets me write down where GSV and the client count will be in 2036, which is what the question
asks; it is a forecast of which way a change will cut, and the speakers' answer to such a forecast is the filter, not a
discount.

**Which cause.** NATURE, not WORK. The deciding question (how much work businesses will buy from people through such a
market once AI agents do part of it) is not cured by reading more filings or talking to clients: "the nature of the
industry would be the roadblock" and "We couldn't solve this problem, moreover, even if we were to spend years intensely
studying those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up" **[L1999-018]**. The test
between the causes is test 5, and the insiders do not write the forecast down **[M2000-105]**. A lower price does not
reopen it **[M2000-038]**, and the circle is not widened to find a purchase: "if we have trouble finding things within our
circle, we will not enlarge the circle. You know, we’ll wait." **[M1995-018]** No research pass is opened (Part VII opens
one only for TOO HARD (WORK)).

**VERDICT: TOO HARD (NATURE).** The run closes here. Q2 to Q12 are NOT REACHED and nothing after this line is a
clearance.

## Q2: WHY IS THE CASTLE STILL STANDING? NOT REACHED.
(The competitor row is recorded below under COMPUTATION AND EVIDENCE, as evidence, not as a Q2 answer.)

## Q3: HOW MUCH CAPITAL MUST GO IN? NOT REACHED.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
(The eight-to-ten-year balance-sheet reading is recorded below at the owner's request, as evidence, not as a Q4 answer.)

## Q5: WHO RUNS IT? NOT REACHED.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.

## Q7: WHAT IS IT WORTH? NOT REACHED.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.

## Q9: COULD IT RUIN US? NOT REACHED.

## Q10: IS IT THE FAT PITCH? NOT REACHED.

## Q12 (optional): NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was produced after the file closed at Q1. It is reported at the owner's request (not a rule
change) and carries no entry language. No figure here reopens Q1 **[M2000-038]**.*

### A. The balance sheets, 2017 to mid-2026 (evidence for a Q4 that was not reached)
Read before the income account, as **[M2025-032]** asks ("balance sheets over an 8 or 10 year period before I even look
at the income account"). USD millions; `tools/run.py` table (first-filed XBRL) checked against the filed FY2025 and FY2023
statements and the Q2 2026 10-Q.

| year-end | total assets | equity | cash + securities | escrow (= payable) | goodwill | intangibles | debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 275 | −31 | n/r | n/r | 118 | 9 | 34 | −124 |
| 2018 | 392 | 244 | n/r | n/r | 118 | 6 | 24 | −143 |
| 2019 | 446 | 259 | n/r | n/r | 118 | 3 | 18 | −172 |
| 2020 | 529 | 299 | n/r | n/r | 118 | 1 | 11 | −195 |
| 2021 | 1,081 | 260 | n/r | n/r | 118 | 0 | 561 | −251 |
| 2022 | 1,080 | 249 | n/r | n/r | 118 | 0 | 564 | −341 |
| 2023 | 1,038 | 381 | n/r | n/r | 118 | 3 | 356 | −294 |
| 2024 | 1,212 | 575 | 622 | 196 | 121 | 13 | 358 | −78 |
| 2025 | 1,300 | 630 | 673 | 181 | 149 | 37 | 360 | 37 |
| 2026-06-30 | 1,274 | 611 | 614 | 193 | 149 | 31 | 361 | 94 |

(n/r = not read for this run; the 2024 to 2026 cash lines are from the filed statements.)

What moved and why:
- **Equity was negative before the 2018 IPO** and then stood near $250M to $300M for five years while the company lost
  money every year; stock pay credited to paid-in capital roughly offset the losses. Equity rose to $575M in 2024 mostly
  because of a **$140.3M non-cash tax benefit** from releasing a valuation allowance (10-K FY2025 MD&A), not from cash
  earned. The deferred tax asset it created ($111.5M at 2025, $109.9M at mid-2026) is a future saving of cash tax, not cash.
- **Goodwill of $118M** is the Elance-oDesk combination and sat unchanged from 2017 to 2023; the rise to $149M is the 2025
  purchases of Ascen and Bubty ($58.4M cash for acquisitions in 2025). No write-down in the span.
- **Debt**: $575M of 0.25% convertible notes issued in 2021 (FY2023 10-K cash flows); $171.3M of cash retired part of them
  in 2023 at a $38.9M gain; $361.0M fell due 2026-08-15, to be paid "using existing cash on hand and borrowings under our
  Revolving Credit Facility" (Q2 2026 10-Q). A $150M secured revolver was signed 2026-06-23 (8-K `0001627475-26-000039`),
  secured on "substantially all assets", with leverage and fixed-charge covenants. Whether it was drawn is not yet filed
  (the Q3 10-Q is not out).
- **Cash is not all the company's.** The escrow line (customer money held in trust) is matched by an equal liability and
  is excluded. Company cash and securities at 2026-06-30: $614.2M; less the notes at principal, **net cash about $253.2M**
  before any revolver draw.
- **Receivables** rose from $31M (2017) to $76M (2025) while revenue rose from $203M to $788M, so receivables fell as a
  share of revenue (about 15% to about 10%): nothing building up against sales. No inventory.
- **Retained earnings** went from −$341M (2022) to +$94M (mid-2026); about $140M of that is the 2024 tax release.
- **Share count**: 132.4M (end 2022) → 137.3M (2023) → 135.3M (2024) → 130.5M (2025) → 124.8M (mid-2026), with
  buybacks of $100.0M (2024), $136.0M (2025) and $109.7M (H1 2026, average $13.24 a share), against RSU settlements of
  3.7M to 4.6M shares a year.

**What the figures do not say**: how much of the 2024 to 2025 rise in owner cash came from cutting sales and marketing
($246.9M in 2022 to $143.4M in 2025) and headcount (two restructurings) rather than from the business, and whether the
lower marketing is why active clients fell. **One presentation change, disclosed**: in Q4 2024 the company moved the
change in client receivables funded through escrow from operating to financing cash flow, which raised reported operating
cash flow by $25.5M (2023) and $4.9M (2022) (10-K FY2024 `0001627475-25-000011`, Note 2). It is disclosed and plausibly
correct (the money is the talent's), so it is recorded as a fact, not as a tell; the owner-cash series above uses the
recast figures for 2022 and 2023.

### B. Owner cash after every real cost (operator rule 5; stock pay deducted)
USD millions; OCF − SBC − (property and equipment + capitalized software). From the filed cash-flow statements.

| | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 | TTM to 2026-06 |
|---|---|---|---|---|---|---|---|---|
| owner cash | −48.9 | −72.8 | −34.8 | 70.7 | 157.7 | 68.2 | 19.3 | 108.9 |

Notes on the real costs: stock pay ($65.4M in 2025) equalled 26% of OCF and is deducted in full **[L2015-003]**; the
company's "adjusted EBITDA" ($225.6M in 2025) excludes it and is not used. 2025 cash taxes ($13.5M paid) were well below
the book provision ($37.8M) because of the deferred tax asset; a full-tax variant deducts the $18.5M non-cash deferred tax.
2025 OCF also includes $23.9M of other income, mostly interest on about $670M of cash and securities, much of which went to
repay the notes in August 2026. **2025 adjusted** (full tax, interest removed after tax at 24.6%, the 2025 effective rate)
= 157.7 − 18.5 − 18.0 = **$121.2M**. H1 2026 owner cash fell because accrued liabilities fell $32.1M (bonus payments and
the restructuring) and capitalized software rose to $17.7M.

Five-year mean (2021 to 2025): **$14.4M**. Three-year mean: $64.5M. The five-year window holds two abnormal loss years
(2021 and 2022, when sales and marketing reached 36% and 40% of revenue against 18% in 2025), so the owner's whole-cycle
variant is shown beside it.

### C. Value range (the Q7 convention, applied only as computation)
Discount rate 5.66% (30-year Treasury, 2026-10-05); ten years at the stated growth, then zero nominal growth; plus net
cash of $253.2M; 124.903M shares. "Growth shown" cannot be measured on aggregate owner cash (it starts negative), so GSV
growth is used as the nearest shown rate: +9.8% a year 2020 to 2025, −0.6% a year 2022 to 2025; −4% is the Q2 2026
year-on-year GSV change. Script: `Test Runs/_research 2026-10-06 UPWK/value.py`.

| base (owner cash, $M) | −4% | 0% | −0.6% | +9.8% |
|---|---|---|---|---|
| five-year mean, 14.4 (the convention's base) | $3.51 | **$4.06** | $3.97 | **$6.45** |
| 2025 adjusted, 121.2 (whole-cycle variant) | $14.55 | **$19.18** | $18.35 | $39.29 |
| TTM to June 2026, 108.9 (raw, not tax-adjusted) | $13.27 | $17.43 | $16.68 | $35.49 |

- **Convention range: $4.06 (no growth) to $6.45 (shown growth) a share, against $8.36.** The price sits above the top.
  By the convention that is an OUT through the floor; but the file closed at Q1, so it is recorded only.
- **Whole-cycle variant (the five-year window holds abnormal years): $14.55 (GSV −4% a year) to $19.18 (flat).** On
  this base the price is below the bottom.
- Across the two bases the range runs from about $3.50 to about $39, more than three to one: the convention would
  itself close it TOO HARD ("the range must be so wide that no useful conclusion can be reached" **[L2000-025]**; a
  wide range is not cured "by having some extra large margin of safety" **[M2007-022]**). The arithmetic reaches the same
  place as Q1 by another road.

### D. Fair price and cheap price (owner's reporting, COMPUTATION)
- **Rule for the fair price:** the price at which the central case's expected pre-tax return equals about 10% (the floor
  CONVENTION), with no growth, so the expected return is the pre-tax owner-cash yield on the enterprise (equity less net
  cash). Owner cash is after cash tax; it is grossed up at the 2025 effective rate of 24.6% to put it on a pre-tax footing.
  The floor is applied to **equity less net cash** (the operating business), and the net cash is added back at face.
- **Central case:** the 2025 adjusted figure, $121.2M after tax = $160.8M pre-tax, held flat. Fair price =
  (160.8 / 0.10 + 253.2) / 124.903 = **$14.90**. On the convention's five-year base ($14.4M after tax, $19.1M pre-tax) the
  same rule gives **$3.56**; on the TTM base, $13.59. The central case is a choice (the latest year, adjusted), and the
  spread to $3.56 is the honest width.
- **Rule for the cheap price (CONVENTION of this run):** the price at which even the worst stated base (the five-year
  mean, which carries two loss years) clears the ~10% pre-tax floor with no growth, so that no choice of window is needed
  and no pencil decides it **[M1996-084]**: **$3.56**.
- **Against the price of $8.36:** above the cheap price; about 56% of the central fair price; above the whole convention
  range. The market price implies an operating business worth about $791M, roughly 6.5 times the 2025 adjusted owner cash,
  i.e. the market is pricing a decline. None of this is a clearance; the box is set at Q1.

### E. The competitor row (evidence for a Q2 that was not reached)

| measure | Upwork | Fiverr (FVRR) | Freelancer Ltd (ASX: FLN) |
|---|---|---|---|
| 2025 volume | GSV $4,028M | marketplace GMV $1,073.0M | not obtained |
| 2025 take rate | 18.7% (13.1% in 2019) | 27.7% (27.6% in 2024) | not obtained |
| buyers / clients | 851k (2023) → 785k (2025) → 763k (mid-2026) | 4.2M (2021), 4.3M (2022), 4.0M (2023), 3.6M (2024), 3.1M (2025) | not obtained |
| revenue | $300.6M (2019) → $787.8M (2025); H1 2026 flat | $107.1M (2019) → $430.9M (2025) | A$57.4M (2021) → A$53.2M (2025); **aggregator, flagged** (stockanalysis.com) |
| GAAP operating income | loss every year 2016 to 2023; $65.2M (2024), $129.3M (2025) | loss every year 2017 to 2025 (−$1.2M in 2025) | not obtained |
| 2025 owner cash (OCF − SBC − capex) | $157.7M | $51.9M (104.6 − 51.4 − 1.3) | not obtained |
| what the filer says about AI | demand down in "certain categories of freelance work"; AI-agent sellers now listed as competitors | "AI technologies reducing demand for simple and low-skilled services"; growth in AI-related complex work | not read |

Sources: Upwork filings as above; Fiverr 20-F FY2025 `0001178913-26-000858` and 20-F FY2022 `0001178913-23-001230`
(buyers 2021, 2022), revenue, OCF and SBC from Fiverr's filed XBRL. Fiverr's treatment of customer funds in its cash-flow
statement was not checked. Over the whole span both listed markets show the same shape: volume rising to 2021 to 2022,
then a falling count of buyers and a rising fee per buyer. Upwork has the larger volume and the better margins; neither
filing shows a castle the other cannot cross, and neither shows the volume of work rising since 2022. In-house hiring
platforms and AI-agent sellers file nothing comparable that this run read.

### F. Facts recorded for questions not reached (no verdict)
- **Management:** Hayden Brown, president and CEO (proxy `0001627475-26-000026`); CEO total pay $9.51M (2023), $9.93M
  (2024), $17.09M (2025), the 2025 rise mostly stock awards ($15.15M) in a year when active clients fell 6%; say-on-pay
  support "approximately 94%" in 2025. Officer turnover in fourteen months: chief accounting officer resigned (2025-07),
  new COO (2025-09), new chief accounting officer (2025-12), GM Marketplace departed (2026-03/04), CFO on medical leave with
  the CEO as interim principal financial officer (2026-07); two directors left the board at the 2026 meeting.
- **Buybacks:** authorizations of $100M (2025) and $300M (2026-02-18), "no expiration date", no stated price (8-K
  `0001627475-26-000015`). Prices paid: about $12.4 (2024), $14.6 (2025), $13.24 (H1 2026), all above the bottom of the
  convention range ($4.06) and above the cheap price ($3.56).
- **Restructuring:** 2024 workforce reductions; May 2026 plan, about 24% of the workforce, $16M to $23M of charges, $13.8M
  booked in Q2 2026, plus $12.4M of cash retention awards (10-Q `0001627475-26-000047`, Note 13).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The volume of work businesses will buy from people through an online market once
AI agents do part of that work is the deciding variable, the filer and its nearest competitor both say they cannot
predict it, and Upwork reported in August 2026 that AI was already cutting GSV and active clients. A lower price does not
reopen it. For reference only (COMPUTATION): price $8.36; convention range $4.06 to $6.45; whole-cycle variant $14.55 to
$19.18; central fair price $14.90; cheap price $3.56.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each: the dispatch
      forbids commits in this session; the file was written in four appends (Step 0, foundations, Q1, computation).*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row or a filing, except the Freelancer revenue (aggregator, flagged) and the CONVENTION figures
      labelled as such.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; everything after it is marked NOT REACHED or
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, stock pay deducted, never a net-income proxy (operator rule 5); the sovereign from
      the issuing authority (US Treasury); the price quote flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items under the foundations, and the
      strongest case for the business stated at Q1).
- [x] No row dated after the anchor is cited (this is a live run, not a point-in-time test; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its printed yield, implied growth and spread lines
      were not.
- [x] `python tools/check_framework.py` PASS before handing back (see the result recorded at the end of this file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The dispatch pointed to a Q1 routing for demand changed by AI and to network effects at Q2; the framework text has
   neither.** A search of `Framework/THE FRAMEWORK v5.md` for the words network, AI, artificial intelligence, marketplace
   and two-sided finds no instance. Q1's routing is written for fast-moving technology from the supplier's side (the
   business must keep up with technology); the case here is different in kind: a technology outside the business changing
   how much of the *product* customers will want (substitution of the work sold). A two-sided market's moat (each side
   stays because the other side is there) has no test of its own in Q2; a future run that reaches Q2 on a marketplace will
   have to argue it from share of mind, the low bid and asking the competitors.

   I applied the existing route because its words cover the case: **[L1993-023]** on fast-moving technology, and
   **[M1998-008]**, "where we think the future technology could hurt the business as it presently exists". The framework
   should still say whether substitution of demand is Q1 (foreseeability) or Q2 (test 11, what could destroy, modify or
   reduce the castle), since the same facts could be argued as a castle filling in (Q2 OUT) rather than a future that
   cannot be seen (Q1 TOO HARD), and the two boxes are acted on differently.
2. **The Q7 convention breaks when owner cash starts negative.** "Carried at the growth shown" has no meaning when the
   five-year series runs from −$72.8M to +$157.7M; I substituted GSV growth and said so. The convention should name the
   fallback (a volume measure, or no growth).
3. **The five-year window and the abnormal year.** The owner asks for a whole-cycle variant "if the five-year window holds
   an abnormal year", but neither the framework nor the dispatch says what makes a year abnormal or what the variant's
   base is. I treated the two heavy-marketing loss years as abnormal and used the latest year adjusted for full tax and
   for interest on cash about to leave; another analyst could choose the three-year mean ($64.5M) and get a value about
   half mine. The variant's base is a CONVENTION of this run.
4. **Interest on cash and tax shelters inside owner cash.** The convention does not say whether interest earned on the
   cash (later added as net cash) is removed from owner cash, or whether cash taxes depressed by a deferred tax asset are
   normalized. Leaving both in would have counted the cash twice and overstated the tax-free years; I removed both and
   say so.
5. **The cheap price** has no rule in the framework (it is the owner's reporting request); the rule above is mine.

---
*Acceptance test: `python tools/check_framework.py` run 2026-10-06 after the last edit: PASS (exit 0). Citation check (`Test Runs/_research 2026-10-06 UPWK/cite_check.py`): no E-ids; every M/L/R id resolves in `principle_ledger_v5.csv`; every quoted fragment set beside an id is found in that row.*
