# Company Run — Lockheed Martin Corporation (NYSE: LMT) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Research folder: `Test Runs/_research 2026-10-06 LMT/` (the fetch and text scripts,
`run_py_output.txt`, `cover_shares_output.txt`, `sources_output.txt`, `arithmetic.py` and its output, the competitor
script `peers.py` and its output, the ledger-row printer `rows.py`; raw filings under `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened,
and no attempt was made to learn whether the operator holds or wants this name.

**CONTAMINATION, declared.** (1) No earlier run file or research folder for LMT exists in `Test Runs/` (a directory
listing showed only this run's two paths); none was looked for in `Framework/v4/` or `Framework/v5/tests/`. (2) One
other company's v5 run (ETN, 2026-10-05) was read for form only; it says nothing about this name. (3) Recent commit
subjects ("Export 2026-10-05: S&P 600 screen ranks ...") name no defense company. (4) Training memory: I came to this
name knowing it as the largest US defense prime, maker of the F-35, and with a recollection that the Air Force's
sixth-generation fighter award went to a competitor in 2025. That memory is a prior; every fact below is from the
filings, and where the filing does not say a thing (it does not name the NGAD winner) the run does not say it either.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $506.63 (2026-10-05, live quote via `tools/run.py`; aggregator, flagged per operator rule 5, used for the
  quote only).
- **Shares:** one class, common stock $1 par. `python Screens/cover_shares.py LMT`: 230,790,753 shares, from the cover
  of the 10-Q for the quarter ended 2026-06-28, filed 2026-07-23, accession `0001628280-26-049411` (cover as-of
  2026-07-20 per the dei fact). The charter has no second class; nothing to add.
- **Market cap:** $506.63 × 230.791M = **$116.93B**.
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-01-29, accession `0001628280-26-004195` (Item 1,
  Item 1A in full for the government-contract, competition, contract-mix and supplier factors, MD&A, the four
  statements, Note 1 on the program losses, the critical audit matter, Note 16); 10-Q for Q2 2026, filed 2026-07-23,
  `0001628280-26-049411` (statements, program-loss note, repurchases, Part II Item 2); proxy DEF 14A filed 2026-03-26,
  `0000936468-26-000004` (scanned for board leadership and the incentive metrics only, since Q5 was not reached); 8-K
  EX-99.1 earnings release of 2026-07-23, `0001628280-26-049277` (read before any judgment of non-GAAP habits); 8-K of
  2025-12-18, `0000936468-25-000057` (pension buy-out conversion, about $900M of obligations, about $480M settlement
  charge); 8-K of 2026-08-28, `0001193125-26-371750` (new $2.25B 364-day revolver; $3.0B five-year revolver extended
  to 2031; no borrowings). History: 10-K FY2022, `0000936468-23-000009` (cash flows and results 2020 to 2022); 10-K
  FY2019, `0000936468-20-000016` (cash flows and results 2017 to 2019).
- **One figure cross-checked against the filed statement:** operating cash flow 2025, $8,557M in the XBRL facts
  printed by `tools/run.py` and $8,557M on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 55).
  Agrees. Capital expenditures $1,649M also agree.
- **`tools/run.py LMT`, arithmetic lines only** (Part VII; its v4 wording and floor ignored). Its five-year window
  (OE capex mean $6,189M) agrees with the table below to the million. Capitalized software is inside "capital
  expenditures" by the filing's own definition ("inclusive of costs for the development or purchase of internal-use
  software that are capitalized", 10-K MD&A), so no software line is missing.

**Owner cash after every real cost** (operating cash flow, which already adds stock pay back, less stock pay, less all
capital spending; USD millions; from the filed cash-flow statements, `0001628280-26-004195` for 2023 to 2025 and
`0000936468-23-000009` for 2021 and 2022; `arithmetic.py`):

| year | OCF | stock pay | capex | owner cash | depreciation variant (OCF − stock pay − D&A) | sales | operating profit | op. margin | owner cash / sales |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 9,221 | 227 | 1,522 | **7,472** | 7,630 | 67,044 | 9,123 | 13.6% | 11.1% |
| 2022 | 7,802 | 238 | 1,670 | **5,894** | 6,160 | 65,984 | 8,348 | 12.7% | 8.9% |
| 2023 | 7,920 | 265 | 1,691 | **5,964** | 6,225 | 67,571 | 8,507 | 12.6% | 8.8% |
| 2024 | 6,972 | 277 | 1,685 | **5,010** | 5,136 | 71,043 | 7,013 | 9.9% | 7.1% |
| 2025 | 8,557 | 304 | 1,649 | **6,604** | 6,566 | 75,048 | 7,731 | 10.3% | 8.8% |
| five-year mean | | | | **6,189** | 6,343 | | | | |

Two things the table does not yet carry, written here so Q4 cannot lose them: (a) the operating cash flow of 2024 and
2025 adds back $1,965M and $1,615M of reach-forward losses that are not yet spent; at 2025 year-end $495M (Aeronautics
classified program) and $1.19B (MFC classified program) "remained accrued in other current liabilities" (10-K Note 1),
cash that will leave in later years; (b) operating cash flow is after the qualified pension contributions ($415M in
2025, $992M in 2024, 10-K cash-flow statement).

**COMPUTATION — NOT A CLEARANCE** (operator rule 3; made before Q1 to Q4 close, carries no entry language): the
five-year mean owner cash is $26.82 a share and 5.29% of the market value, against a sovereign of 5.66%; the shown
growth of aggregate owner cash, 2021 to 2025, is −3.0% a year.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. First, no macro forecast enters **[M2000-094]**: the 10-K and the July release lean
on "recent regional conflicts", "unprecedented demand", the FY2026 budget and a stated desire for "a significant increase
in defense spending in FY2027"; those are forecasts of the customer's politics and are kept out of every question below.
Second, the market serves and does not instruct **[M2006-077]**: the price says nothing about the business. Third, who is
paid to tell you **[M2020-037]**: the release headlines "Record backlog of $230 billion" and a raised outlook; the proxy
ties annual pay to sales, segment operating profit and free cash flow "aligned with the annual financial outlook we
disclosed publicly" (DEF 14A, `0000936468-26-000004`), so the outlook is a number the managers are paid to meet. The
analyst's habit applied is to look for "what’s wrong" and "what you’re missing" **[M2025-013]**. **Contrary evidence,
written down as found** **[M1997-127]**: (a) margins fell from 13.6% (2021) to 10.3% (2025) on rising sales; (b) reach-
forward losses of $1.965B in 2024 and $1.615B in 2025, the largest on two classified fixed-price programs that "cannot be
specifically described"; (c) a fixed-asset write-off "resulting from the U.S. Air Force’s Next Generation Air Dominance
(NGAD) competition and down-select decision" (10-K Note 16); (d) the 10-K names "increased competition from new entrants,
startups and non-traditional defense contractors" and a presidential order that "could limit certain contractors ...
from issuing excessive dividends or owner distributions, making share repurchases"; (e) no shares were repurchased in the
first half of 2026 (10-Q), after $3.0B in 2025; (f) for the other side: backlog rose from $176.0B (2024) to $193.6B (2025)
to $230B (2026-06), a $35B multi-year THAAD contract was signed, and first-half 2026 operating cash was $3.455B against
$1.610B a year earlier.

## THE STANDING RULE
Bought for cash, unlevered, at a size the buyer can hold through a fall of half, a share of Lockheed Martin puts the
buyer at no risk of ruin; the rule binds the buyer's financing and sizing, and borrowing to buy is ruled out
**[L2014-005]**, **[M2012-081]**. The target's own debt ($21.7B at 2025 year-end) belongs to Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, a "reasonable probability of being able to asses where the business will be in 10
years" **[M2000-037]**; the product may stay opaque if "the economic dynamics of the industry" are understood
**[M2011-014]**.

**The economic dynamics, from the filing.** One customer, the US Government, takes 72% of sales (63% the Department of
War) and international customers 28%, 77% of them through Foreign Military Sales contracted through the US Government
(10-K, `0001628280-26-004195`, MD&A). Prices are formed by regulation, not by a market: the government contract laws
"require certification and disclosure of all cost or pricing data", "impose specific and unique cost accounting
practices", and "define which costs can be charged" (Item 1). About 40% of 2025 sales were cost-reimbursable, billed as
costs are incurred; the rest fixed-price, often with performance-based or progress payments (MD&A, Liquidity). Profit
is a fee on cost, or the residue of a fixed price against an estimate the company itself makes under the
percentage-of-completion method. Programs run for decades: the C-130 and F-16 are still produced, and the F-35, 27% of
sales, rests on a stated US objective of 2,456 aircraft plus seven partner countries and twelve FMS customers (Item 1).
Backlog was $193.6B at 2025 year-end, about 37% to be recognized within twelve months and 60% within twenty-four
(MD&A), and $230B at 2026-06 (EX-99.1, `0001628280-26-049277`).

**The key variables and how predictable they are** **[M1998-044]**: (1) how much the customer buys, which is a
political appropriation, not a forecast this run makes **[M2000-094]**, but whose ten-year shape is visible in programs
of record and a backlog of about three years of sales; (2) the fee the customer allows, which the competitor row at Q2
shows sitting near 10% of sales for all four large primes; (3) execution on fixed-price development, where the company's
own estimates on its own classified programs moved by $950M within a year (Note 1); (4) which company wins the next
generation of programs. Variables 1 and 2 are foreseeable in kind for ten years; variable 3 is a cost the record shows
recurring and can be carried as one (Q4); variable 4 decides the castle after the present programs, and is asked at
Q2, where the rows put the ten-to-twenty-year question **[M1995-038]**.

**Do the past statements tell me the future ones?** **[M2008-033]** For the incumbent programs, largely yes: the same
four segments and the same named programs run through the FY2019, FY2022 and FY2025 10-Ks, and operating margin has
moved within 9.9% to 14.3% across 2019 to 2025 (the FY2019 10-K, `0000936468-20-000016`, gives $8,545M on $59,812M for
2019). The part that cannot be read is named by the filer itself: "A portion of our business is classified by the U.S.
Government and cannot be specifically described", and the auditor's critical audit matter cites "the classified nature
of the contracts" as what made the cost estimates "especially challenging". This is legal secrecy, not obfuscation, and
it is not the whole: the losses on the two classified programs are disclosed by amount ($1.8B and $1.46B cumulative).

**The technology test.** Rows send a business whose future technology could hurt it to the too-hard pile **[M1998-008]**,
**[L1993-023]**. The 10-K says "Technological advances in such areas as ... artificial intelligence, advanced materials,
autonomy and robotics, and new business models such as commercial access to space, are enabling new factors of
competition." This bears on who wins the next generation (variable 4), not on whether the programs already in hand
will be built and sustained in the next ten years; the customer still buys F-16s and C-130s decades after their first
contracts. I hold this as a doubt, written down **[M1997-127]**, and carry it to Q2.

**Routing.** Not a bank or a holding company. The doubt rule, "if you have doubts about something being into your
circle of competence, it isn’t" **[M2002-092]**, has been weighed: the doubt I have is about the castle's
twenty-year permanence, which is Q2's question by the framework's own order **[M1997-148]**, not about whether the
ten-year earning power of the programs in hand can be fixed in a range.

- **VERDICT: IN**, narrowly: the ten-year economics, a regulated fee on cost from a customer that funds much of the
  working capital, across programs that run for decades and a backlog of about three years' sales, can be fixed in a
  range **[M2012-065]**, **[M2011-014]**; the next-generation question is passed to Q2 **[M1995-038]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The castle tests,
each with its filing fact (10-K `0001628280-26-004195` unless named):

1. **What keeps it standing now, and how permanent.** The castle is incumbency on programs of record. Once a platform is
   chosen, the company designs, builds and sustains it for decades as prime ("We are the prime contractor on most of our
   contracts", Item 1A), with a security-cleared workforce of about 123,000, 72,000 of them engineers, scientists and IT
   staff (Item 1). F-35 production and sustainment, PAC-3 (seventeen nations), THAAD (a $35B multi-year contract,
   EX-99.1), Trident II D5 ("the only submarine-launched intercontinental ballistic missile currently in production in
   the U.S."), C-130 and F-16 are each such a position. That castle is real and has stood: the four segments and the
   named programs recur across the FY2019, FY2022 and FY2025 10-Ks. Its permanence is program by program, and each
   program ends; what keeps the company's castle standing twenty years out is the next generation of programs, which
   is awarded by competition. "While we generally expect to compete and be well positioned as the incumbent on
   existing programs, we may not be successful and, even if we are successful, the replacement programs may be funded
   at lower levels or result in lower margins" (Item 1A).
2. **Would it stand without the lord?** Yes; no superstar is needed to sustain an installed fleet **[L2007-006]**,
   **[M1996-037]**. This test passes.
3. **The money test.** Against the programs in hand, an attacker with money cannot displace the incumbent mid-life
   **[M2011-015]**, **[M1997-103]**. Against the next program it can, and has: the 10-K records a write-off of fixed
   assets "resulting from the U.S. Air Force’s Next Generation Air Dominance (NGAD) competition and down-select
   decision" (Note 16), a competition for the air-dominance role its F-22 ("air dominance") holds today (Item 1); the filing does not name
   the winner. The 10-K adds "increased competition from new entrants, startups and non-traditional defense contractors",
   and that "The U.S. Government may use or authorize others, including competitors, to use such intellectual property"
   developed under its contracts (Item 1). "one competitor is frequently enough to ruin a business" **[M2012-108]**.
4. **Pricing power, and the agony before a rise.** None in the speakers' sense **[M2005-020]**, **[M2005-019]**. The
   buyer sets the terms: certified cost and pricing data, cost rules "that may differ from" GAAP, the right "to
   unilaterally definitize contracts, which it has exercised in the past", audits that "often take years", payment
   terms the customer may move from performance-based to progress payments, and a presidential order that "could limit
   certain contractors ... from issuing excessive dividends or owner distributions, making share repurchases, and placing
   certain restrictions on executive compensation" (Items 1 and 1A, MD&A). On a program like the F-35 the company is a
   sole supplier, which the rows link to pricing power **[M2010-092]**, but it sells to a sole buyer who writes the
   price; the reading that this is a bilateral monopoly in which the buyer holds the pen is mine, from these facts.
5. **Unit volume and share of mind.** Volume is rising: sales $67.0B (2021) to $75.0B (2025); backlog $176.0B to $230B
   in eighteen months. For the castle, volume is evidence the incumbent positions hold **[M2000-030]**; it says nothing
   about the margin, which fell (test 10).
6. **The low-cost position.** No evidence of one. The competitor row below shows the four large primes at the same
   operating margin, about 10% to 11% of sales in 2025; the rows ask whether costs are below the rivals' **[M2001-013]**,
   and the filings show parity, which in a fee-on-cost business is what regulation produces.
7. **The brand.** The customer buys capability against a requirement under procurement law; "reputation and customer
   confidence derived from past performance" is one of the listed factors of competition (Item 1). No row-shaped
   brand test applies **[M2008-075]**.
8. **Would the customer still choose it over the low bid?** On new work, the record says the company has had to bid
   low to win: the MFC classified contract was "competitively bid" with fixed-price options that "if performed expect
   they would each be at a loss" ($1.46B recognized, Note 1); the Aeronautics classified program, fixed-price incentive
   with fixed-price options, has lost $1.8B cumulative. The 10-K's own words on the procurement: bids not tested for
   realism "can lead to bidders taking aggressive pricing positions, which could result in the winner realizing a loss
   upon contract award", and "Competitors may be willing to accept more risk or lower profitability". The rows' failing
   answer is the customer who buys on the low bid **[M2017-009]**, **[L2004-003]**; on the incumbent programs the
   customer cannot switch, on the next ones it runs the auction.
9. **Ask the competitors.** The filing answers part of it: "It is not unusual to compete for a contract award with a
   peer company and, simultaneously, perform as a supplier to or a customer of that same competitor" (Item 1); Javelin is
   made by a joint venture with RTX. No silver-bullet answer is on the public record **[M1999-130]**; recorded as not
   found.
10. **Widening or narrowing?** **[M1999-108]**, **[L2005-010]**. On volume, widening. On terms, narrowing: operating
    margin 13.6% (2021) to 10.3% (2025); owner cash 11.1% of sales to 8.8%; the filer says "our customers continue to
    implement procurement strategies such as these that shift risk to contractors" (Note 1). The two do not net to a
    verdict; the margin has come down to the level of the peers, not below it.
11. **What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]** Three things the filing
    names: the customer's procurement reform toward "commercial solutions" and OTAs that may require "a significant
    portion of the work" to be "performed by a non-traditional defense contractor"; technology ("artificial intelligence
    ... autonomy and robotics ... commercial access to space"); and the fixed-price development risk the customer now
    prefers. Each is a judgment about how a government buyer and a technology contest will behave over twenty years.

**The competitor row** (FY2025 unless stated; operating profit ÷ sales, and owner cash = OCF − stock pay − capex,
÷ sales; each company's own 10-K XBRL, `peers.py`):

| company | accession (FY2025 10-K) | op. margin 2025 | op. margin 2021 | owner cash / sales 2025 |
|---|---|---|---|---|
| Lockheed Martin | `0001628280-26-004195` | 10.3% | 13.6% | 8.8% |
| General Dynamics | `0000040533-26-000006` | 10.2% | 10.8% | 7.2% |
| Northrop Grumman | `0001133421-26-000003` | 10.8% | 15.8% | 7.6% |
| RTX | `0000101829-26-000006` | 10.5% | 7.7% | 8.4% |

The four converge on about 10% to 11% of sales; Lockheed's lead of 2021 is gone. In a business whose fee the buyer
sets, the convergence is what the castle protects: a regulated rate on cost, not a rate the company chooses. The
speakers' word for regulated returns is "fair", not outsized **[L2005-005]**, and they warn that the regulatory climate
can turn so that "it is difficult to project both earnings and asset values" **[L2023-011]**; reading the government
buyer as a regulator is my analogy, flagged as such.

**Contrary evidence, written down as found** **[M1997-127]**: record backlog and a $35B THAAD multi-year contract; first-
half 2026 operating cash more than doubled; the incumbent programs include the only US submarine-launched ballistic
missile in production and an air-defence missile chosen by seventeen nations; the speakers themselves note that some
moats are "as sustainable" as decades ago **[M2001-069]**. These show the present castle standing. They do not show what
stands in twenty years.

**The deciding row.** The speakers spoke to this business by name of kind. Of General Dynamics in 1994: "We think the
management of General Dynamics has done an absolutely sensational job. Obviously, also it isn’t the kind of business,
basically, that we have a 20-year view on, or something of the sort." **[M1994-063]**. The defence prime is the case
where the castle is evident today and its twenty-year future cannot be judged, because it is re-won program by program
in technology contests whose terms the buyer sets. Where the threat over five to fifteen years "is impossible for us to
figure ... we don’t even think about it then" **[M2000-014]**; a moat that cannot be valued is left alone **[M2000-019]**.
A castle shown open on the evidence would close OUT; the evidence does not show it open (the incumbent positions hold and
volume rises), so the box is TOO HARD **[M2006-013]**, not OUT.

**Which cause.** NATURE, not WORK. The deciding question, whether Lockheed Martin wins and profitably executes the
generation of programs that will replace the F-35, PAC-3 and Trident positions as the customer moves risk onto
contractors and admits non-traditional entrants, is one the industry's insiders do not write down **[M2000-105]**: the
filer's own estimate on its own Aeronautics classified program moved by $950M inside a year ("a greater impact on
schedule and costs than previously estimated", Note 1), it lost the NGAD down-select it bid, and it tells its owners it
"may not be successful" on replacement programs. "We couldn't solve this problem, moreover, even if we were to spend
years intensely studying those industries" **[L1993-023]**; the row of 1994 says the same of the kind of business
**[M1994-063]**. A lower price does not reopen it **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)** **[M1994-063]**, **[M2000-014]**, **[M2000-019]**, **[M2006-013]**. The file closes
  here; Q3 to Q12 are NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. *Facts gathered on the way, recorded for a later reader and answering nothing:* the ten balance sheets
printed by `tools/run.py` show equity of $1.5B (2016), −$0.7B (2017) and $6.7B (2025) against goodwill of $10.8B to
$11.3B, so tangible equity has been negative throughout; long-term debt on the face of the balance sheet rose from
$11.7B (2021) to $21.7B (2025); retained earnings fell from $21.6B (2021) to $14.0B (2025) while net earnings were
positive every year, because repurchases are charged to them (10-K statement of equity); the receivables line drops
from $8.6B (2017) to $2.4B (2018), a reclassification into contract assets on the revenue-standard change, not a
business change, which the tool's table does not flag. The July release headlines GAAP net earnings first and uses two
non-GAAP measures, segment operating profit and free cash flow (OCF less capex, stock pay not deducted); no adjusted
EPS and no EBITDA were found in it.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. (Recorded only: the chief executive is also chairman; the 2025 annual incentive weighted sales, segment
operating profit and free cash flow at targets "aligned with the annual financial outlook we disclosed publicly",
DEF 14A `0000936468-26-000004`.)

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (Recorded only: 2021 to 2025 repurchases $24.7B and dividends $15.2B, $39.9B in all, against $30.9B of
owner cash, the difference met by debt (filed cash-flow statements); the repurchase authority is "at prices per share
not exceeding the then-current market prices" and names no value-based price; no shares were bought in the first half
of 2026, 10-Q Part II Item 2.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was built; the Step 0 yield line is a computation, not a clearance.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. (Recorded only: $21.7B of fixed-rate notes, $1.168B due within a year; $5.25B of revolvers, undrawn, the
364-day one renewed on 2026-08-24 with no financial maintenance covenant, 8-K `0001193125-26-371750`; offset
obligations of $19.9B notional with penalties estimated at $2.2B, 10-K MD&A.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED; not asked.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q2**: the present castle (incumbency on programs of record) is standing, but what
keeps it standing ten to twenty years is the next generation of programs, re-won in technology contests on terms the
buyer sets, and the speakers' own word on the defence prime is that "it isn’t the kind of business, basically, that we
have a 20-year view on" **[M1994-063]**; Q7 not reached, so no range is set beside the price of $506.63. A lower price
does not reopen the box **[M2000-038]**. **What would change the cause, not the price:** the replacement programs for
the incumbent franchises awarded and run on terms whose margin can be read from the filings, with a span of fixed-price
development completed without reach-forward losses, so that the twenty-year question becomes one an insider would write
down **[M2000-105]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      Step 0 `09c153c`, Q1 `bec8dce`, Q2 `21beb8c`, close in the final commit.
- [x] Every v5 id resolves (each grepped through `rows.py` against `principle_ledger_v5.csv` before it was written);
      every filing fact has its accession; the only numbers without a filing are the price (aggregator, flagged) and
      the competitor row, which carries its own accessions.
- [x] The order was kept; Q1 IN, Q2 the first STOP that failed, closed TOO HARD; nothing after it is a clearance.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury curve; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, Q1, Q2).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the run date is
      today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 wording, ids and floor were ignored.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Which question owns the twenty-year horizon.** Q1 defines understanding as a fix "five or 10" years
out **[M2012-065]**, but also "five or 10 or 20" **[M2005-089]**, and the routing sends fast change to Q1 TOO HARD; Q2
asks "five, 10, 20 years" **[M1995-038]**. For a business whose ten-year economics are visible in programs already won
and whose twenty-year castle is a technology contest, the same doubt could close at Q1 or at Q2, and the same row
**[M1994-063]** would decide either. I placed it at Q2, because the doubt is about the castle's permanence and not about
the earning power of the programs in hand; another analyst could close it at Q1 with the same box. The framework should
say which question owns the ten-to-twenty-year span when the two diverge. (2) **The buyer who sets the price.** Q2's
pricing-power test presumes a market in which the seller names the price; it has no text for a sole buyer that
certifies costs, sets the fee, can definitize unilaterally and can, by executive order, restrict the seller's dividends
and buybacks. The nearest rows are the regulated-utility rows of Q3 and the regulatory-climate letter **[L2005-005]**,
**[L2023-011]**, used here only by analogy and flagged as such. (3) **Segments that cannot be described by law.** Q1 has
a convention for a holding company's unreadable part and a rule for banks, but none for classified segments whose losses
are disclosed by amount and whose contracts are not; I treated it as a doubt carried to Q2, not as a Q1 close. Also, for
Q4 and Q7 when reached on a contractor: owner cash taken from operating cash flow counts accrued reach-forward losses
only when spent ($1.69B still accrued at 2025 year-end here), and the Q7 convention does not say whether such an accrued,
unspent loss is deducted from the five-year average or from value once. **Tool notes:** `Screens/cover_shares.py` and
`tools/run.py` ran cleanly for LMT; `run.py`'s ten-year balance-sheet table does not flag the 2018 receivables
reclassification (a revenue-standard change), which a reader of the table could take for a business change. EDGAR
returned no 429s to this run's paced fetches.
