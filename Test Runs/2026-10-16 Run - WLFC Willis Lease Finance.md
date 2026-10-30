# Company Run: Willis Lease Finance Corporation (Nasdaq: WLFC), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 08af694c). Dispatched blind run under
`Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure (the lines of evidence derived by the analyst from
the 10-K's Items 1, 1A and 7, below). Research folder: `Test Runs/_research 2026-10-16 WLFC/` (raw filings in its ignored
`cache/`; the scripts `ownercash.py`, `value.py`, `compare.py` and `check_ids.py` are the arithmetic and the citation check).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only; not held.*

**CONTAMINATION, declared.** Seen by accident and not used: the session's start-up context showed the last five commit
subjects of the repository, all about another company's run (HRI, folded 2026-10-16), and the memory index lines (queue
state, counts of gate-clearers, nothing naming this company). No run file, holding review, `PORTFOLIO.md`, queue, reading
list or resume-state file was opened, listed or searched. `Test Runs/` was not listed or searched; the only `Test Runs/`
paths opened were the template and this run's own two paths. One command early in the session tested for an existing
file of this company by name pattern (`ls "Test Runs" | grep -i -E "wlfc|willis"`) before the copy; it returned nothing.
I declare it here because it is a search of `Test Runs/` file names, which the blind rule forbids; nothing was learned
from it beyond the empty result.

**Lines of evidence chosen, and why** (this brief's departure: derived from the FY2025 10-K, accession 0001018164-26-000036,
Items 1, 1A and 7). (1) **The spread**: Item 1 says the company buys engines "with a combination of equity capital and
funds borrowed", borrows "up to 85% of an engine's purchase price", and Item 1A says rivals "may have lower costs of
capital"; so the cost of funds against rivals is the low-cost test, read from WLFC's, AerCap's and FTAI's own filings.
(2) **The residual**: Item 1 says "the value of an engine begins to decline rapidly once the host aircraft is retired";
so gains on sale, write-downs and depreciation policy (15 years to a 55% residual) are read over the whole span.
(3) **The cycle**: Item 1A says "results of prior periods should not be relied upon"; so the reading runs 2015 to 2025,
through the 2020 to 2022 trough. (4) **Customer indifference**: Item 1 says operators "utilize several leasing companies
... to minimize reliance on a single leasing company", and Item 1A says buying engines generally involves "an auction
bidding process"; so the commodity question is asked at Q2. (5) **The debt and the control**: Item 1A says
"Substantially all of our assets are pledged" and the founder "effectively controls the Company"; so Q9 and Q5/Q6 facts
are recorded. (6) **The post-period deals**: the 8-Ks of 2026 (split, convertible notes, WNG II, Series B preferred, a
building purchase).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $37.61 a share (2026-10-16, the quote `tools/run.py` fetched; an aggregator live quote, flagged under operator
  rule 5, not a filed figure). Post-split basis.
- **The split, and the one basis used.** A three-for-one forward split became effective 4:05 p.m. ET 2026-07-17 (8-K of
  2026-07-17, accession 0001193125-26-307870, Item 5.03; checked: authorised common raised from 20,000,000 to 60,000,000);
  trading on the split basis began 2026-07-21 (10-Q for 2026-06-30, accession 0001018164-26-000068, note 1). **Every share
  count and per-share figure in this file is on the post-split basis.** Pre-split figures from the FY2025 10-K are divided
  by three and say so: the 30,000 shares bought from the Executive Chairman at $126.2782 are 90,000 at $42.09; the
  option for 300,000 shares at $126.55 is the 10-Q's option for 900,000 shares (the 10-Q states 900,000; the strike,
  divided by three, $42.18); the convertible notes' $268.80 conversion price is the 10-Q's $89.60.
- **Shares by class:** common, 21,144,111 outstanding at 2026-07-31 (cover of the 10-Q, accession 0001018164-26-000068;
  `python Screens/cover_shares.py WLFC`). Checked against issued less treasury: 22,808 thousand issued at 2026-06-30 on
  the balance sheet, and repurchased shares "are immediately retired" (10-Q note 10), so there is no treasury stock; the
  difference of 1,664 thousand is the unvested restricted stock, 1,663,635 shares at 2026-06-30 (10-Q note 11), and
  21,144 + 1,664 = 22,808. **The count used for per-share values is 22.808 million (issued, unvested restricted stock
  included), the 21.144 million cover count beside it.** No common was issued in the 8-Ks after the 10-Q: the May 2026
  "Concurrent Delta Offering" of 281,250 shares was borrowed stock, "no new shares of Common Stock were issued" (8-K of
  2026-05-18, accession 0001193125-26-228878). Potential shares: 900,000 options at about $42.18 (out of the money at the
  price) and $200.0 million of 2.50% convertible notes due 2031 at $89.60 (about 2.23 million shares, far out of the
  money). Preferred (all held by the Development Bank of Japan): Series A, $65.0 million liquidation value, 8.35%; Series B,
  1,750,000 shares at $20.00 (gross about $35 million), 8.09%, closed 2026-09-29, holder put on 2031-09-29 (8-Ks
  0001018164-26-000078 and 0001018164-26-000082; checked); both series then split three-for-one (5,250,000 Series B shares
  at one third of $20.00).
- **Market cap:** $857.8 million on 22.808 million shares ($795.2 million on the cover count).
- **Sovereign for the earnings currency (USD):** 5.43%, the 30-year par yield of the US Treasury daily par yield curve,
  2026-10-15 (`python tools/sources.py`, issuing authority). The leases are "denominated and payable in United States
  (“U.S.”) dollars" (10-K Item 1).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-03-10, accession 0001018164-26-000036 (Items 1, 1A, 5, 7, 7A,
  the statements and notes), and its 10-K/A of 2026-03-30, accession 0001018164-26-000041 (filed only to add the omitted
  Inline XBRL files, its explanatory note says); 10-Q for 2026-06-30, accession 0001018164-26-000068; 10-Q for 2026-03-31,
  accession 0001018164-26-000053 (fetched; not read, since the June 10-Q carries the six months); proxy DEF 14A filed 2026-04-24, accession
  0001193125-26-177136 (read for pay and the peer group, recorded under AFTER THE STOP); the 10-Ks for FY2024
  (0001018164-25-000027), FY2023 (0001018164-24-000013), FY2021 (0001018164-22-000007), FY2020 (0001018164-21-000013),
  FY2019 (0001018164-20-000008) and FY2016 (0001558370-17-001855), for the competition passage and the cycle; the 8-Ks
  0001193125-26-307870 (split), 0001018164-26-000058 (WNG II signed 2026-07-10, base price $379.3 million),
  0001018164-26-000072 (WNG II closed 2026-08-24), 0001018164-26-000078 and 0001018164-26-000082 (Series B),
  0001193125-26-228878 (convertible notes), 0001018164-26-000070 (building purchase), 0001018164-26-000063 (dividend),
  0001018164-26-000074 (presentation, item text only).
- **The brief's three 8-K facts, checked against the filings.** The split: as stated (above). WNG II: completed 2026-08-24,
  twelve commercial aircraft and thirteen spare engines, base price $379,300,000; but the filing adds what the brief does
  not: "At closing, the Adjusted Purchase Price was approximately $262,900,000", and "the Company intends to allocate ten
  (10) of the acquired aircraft engines and six (6) of the acquired aircraft to subsidiaries of joint ventures of, or
  investment vehicles managed by, the Company" (8-K 0001018164-26-000072, Item 2.01). Series B: as stated, 1,750,000 shares,
  8.09%, closed 2026-09-29.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, FY2025, $283,235
  thousand on the filed Consolidated Statement of Cash Flows (10-K 0001018164-26-000036) against $283.2 million in the
  XBRL series `tools/run.py` and my scripts read; also FY2023 $229,737 thousand and FY2022 $144,424 thousand (10-K
  0001018164-24-000013), FY2021 $90,658 thousand and FY2020 $93,444 thousand (10-K 0001018164-22-000007), all matching.
- **`python tools/run.py WLFC`, arithmetic lines only** (output in `run_py_output.txt`; nothing it prints as a rule, id or
  verdict is used, Part VII). It reads a three-year window ending 2024, which it flags as over eighteen months old; I
  rebuilt the series from 2015 to 2025 by hand (`ownercash.py`). Its "capex" column is property, equipment and furnishings
  only ($6.6 million to $15.6 million); it prints the purchases of equipment held for lease as an alternate it does not
  choose ($286.4 million, $163.6 million, $830.5 million), and it does not see the sale proceeds of leased equipment at
  all. For a lessor both belong in the owner-cash reading (the brief): **recast by hand**, below and at the COMPUTATION.
  Its D&A line (88.3, 90.9, 92.5) matches the filed statements. SBC (13.6, 14.8, 29.2) matches; FY2025 SBC is $44.6
  million (filed).

### The balance sheets first, ten years (read here because the file closes before Q4 **[M2025-032]**)
Ten year-ends from the filed balance sheets (USD millions; `tools/run.py` transcription, the FY2025 and FY2024 columns
checked against the filed statement in 0001018164-26-000036; 2026-06-30 from the 10-Q):

| year-end | assets | equity | debt | cash | restricted cash | retained earnings | debt / equity |
|---|---|---|---|---|---|---|---|
| 2016 | 1,338 | 196 | 900 | 10 | n/r | 195 | 4.6x |
| 2019 | 1,941 | 350 | 1,251 | 7 | n/r | 349 | 3.6x |
| 2021 | 2,463 | 376 | 1,790 | 14 | n/r | 355 | 4.8x |
| 2023 | 2,652 | 439 | 1,803 | 7 | n/r | 398 | 4.1x |
| 2024 | 3,297 | 549 | 2,265 | 9 | 123 | 491 | 4.1x |
| 2025 | 3,936 | 662 | 2,700 | 16 | 531 | 591 | 4.1x |
| 2026-06-30 | 3,653 | 709 | 2,321 | 11 | 161 | 637 | 3.3x |

(n/r: not read for that year.) What moved and why. **Equity tripled, all of it retained earnings**: paid-in capital is
$71.3 million at 2026-06-30, because the company retires what it buys and cancels restricted stock to pay employees'
withholding tax ($27.9 million in the first half of 2026 alone, statement of equity, 10-Q). **Debt moved with the fleet,
at four to nearly five times equity in every year read**, the lessor's model: "We usually borrow up to 85% of an engine's
purchase price. Substantially all of our assets secure our related indebtedness." (10-K Item 1). **No goodwill and
almost no intangibles** until 2026 ($8.3 million at 2026-06-30). **Receivables are small** against revenue ($35.7 million
at 2025 against $730.2 million of revenue). **Restricted cash swings** with the securitisations: $530.5 million at
2025-12-31, raised by the December WEST IX notes and used in 2026 to retire older notes (debt fell $379 million in six
months, with $12.4 million of loss on extinguishment, 10-Q). **A deferred tax liability of $264.8 million** has built
because the company pays almost no cash tax (income taxes paid $3.4 million in 2025 against a provision of $46.8
million, filed cash-flow supplement). What the figures do not say: what the engines would fetch. The balance sheet
carries them at cost less depreciation to a 55% residual; their market value appears only in the impairment test, which
the auditor names a critical audit matter ("Valuation of equipment held for operating lease", Grant Thornton, 10-K).
What they cannot say: whether the $2.0 billion of fixed-rate securitised debt can be refinanced on the same spread in a
year when credit is short **[L2010-020]**.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what a fleet of leased engines, owned on borrowed money, returns
to its owner over the years, not where the quotation goes. The market serves and does not instruct **[M2006-077]**: the
split and the price move since it carry no information about the fleet. Margin of safety **[M1996-084]**: if the case
needs pencil and paper it is too close. No macro forecast enters: the engine shortage of 2023 to 2026 is a condition of
the field, read in the figures, not forecast. Who is paid to tell you: the company features Adjusted EBITDA in its 10-K
and pays its managers on figures I have not yet read, so its own description of its prospects is read as the seller's.
The analyst's habits: hunt the evidence against hardest; what do I not know that I need to know **[M1999-129]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the 10-K's Item 1A, in every year read from FY2016,
says rivals "may have lower costs of capital", which goes to the low-cost test before any test was run; (2) the filer
says its results "should not be relied upon as an indication of our future performance" (Item 1A), which goes against
Q1's test 3; (3) cash taxes are close to nil while the provision is near 29%, so any cash figure that leaves out the
deferred tax flatters the owner; (4) the competition paragraph of Item 1A grew from five named rivals (FY2016, FY2019,
FY2021) to nine (FY2025); (5) stock pay rose from $3.7 million (2016) to $44.6 million (2025), faster than revenue;
(6) the latest 8-Ks add $262.9 million of fleet, $118.0 million of buildings and $35 million of 8.09% preferred after the
last balance sheet.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin, provided the buyer's own purchase is unlevered and sized so that a
total loss of it cannot end the buyer: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "the only
way smart people can get clobbered, really, is through leverage" **[M2004-065]**. The target's own leverage (four times
equity, every asset pledged) is not the buyer's conduct and is weighed at Q9, not here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years", with "some notion of how the industry will develop and where the company will
stand within the industry" **[M2012-065]**; the first step is "trying to identify the key variables in that particular
business, and evaluating how predictable they were first" **[M1998-044]**.

**The business, from the filing.** Two reportable segments; Leasing and Related Operations carried 94.9% of 2025
revenue and Spare Parts Sales the rest (10-K Item 1). At 2025-12-31, $2,801.7 million of equipment on operating lease plus
$139.9 million of notes receivable, $30.6 million of maintenance rights and $16.6 million of sales-type leases: 363 engines,
20 aircraft and one marine vessel, with 69 lessees in 37 countries, plus 116 engines managed for others (Item 1). The leases
are "triple-net": the lessee pays rent and all running costs and maintains the engine; the company keeps the residual
("Under operating leases, we retain the potential benefit and assume the risk of the residual value"). It funds the fleet
with warehouse lines and then fixed-rate asset-backed notes (WEST III, V, VI, VII, VIII, IX), $2.0 billion of fixed-rate
financing at 2025-12-31 (Item 1). The leasing part decides the file: segment income from operations $108,991 thousand against a
Spare Parts loss of $4,412 thousand in 2025, and $146,290 thousand against a loss of $1,666 thousand in 2024 (10-K segment
note); the parts paragraph of Q2 is applied there.

**The key variables, and whether they are foreseeable** **[M1998-044]**:
1. *Demand for spare engines*, set by the installed fleet and by shop-visit times (Item 1 lists both). Foreseeable in kind:
   the fleets that use these engines (CFM56, V2500, LEAP, GTF) are known and long-lived.
2. *Lease rates and utilisation*: average utilisation 85% in 2025 and 83% in 2024 (Item 7); readable over the cycle from
   rent and maintenance-reserve revenue.
3. *Residual values at sale*: gains on sale of leased equipment $54.0 million (2025) and $45.1 million (2024), write-downs
   $32.9 million and $11.2 million (Item 7); the value of an engine "begins to decline rapidly once the host aircraft is
   retired" (Item 1). The weakest variable: when the current-generation host fleets retire is the decade's question,
   and "how far off we can be" **[M2011-084]** is widest here.
4. *The cost of funds against fixed rents*: interest expense $132.1 million in 2025; $732.7 million of debt floating
   (Item 7A). Readable from the filings, year by year.
5. *Lessee credit*: one customer 13% of 2025 lease rent (Item 1A).

**Do the past statements tell me the future ones?** **[M2008-033]**. In kind, yes: the model (lease, collect reserves,
sell or part out at the end, refinance in the asset-backed market) is the same in every 10-K read from FY2016 to FY2025,
and the same five named rivals and the same "lower costs of capital" sentence stand in FY2016, FY2019 and FY2021. Against
it, written down **[M1997-127]**: the filer's own sentence that prior results "should not be relied upon as an indication
of our future performance" (Item 1A), which I read as a warning about year-to-year swings (sales timing, end-of-lease
reserve releases, all listed beside it), not about the ten-year economics.

**Would the insiders write the forecast down?** **[M2000-105]**. They do: the asset-backed notes are priced on the engines'
lease and residual cash flows with "an expected maturity of approximately six years and a final maturity of 25 years"
(WEST VIII and WEST IX, Item 7), and the impairment test forecasts each engine's cash flows to the end of its life, checked
by independent appraisers (critical audit matter, 10-K). The lenders and the auditor write down the long forecast; this
is not the tech field.

**A financial institution?** A lessor holds long-lived assets on borrowed money, so the door for a lender is the one that
applies: inside the circle when both sides can be read **[M2002-022]**, outside when the asset side cannot **[M2005-068]**,
**[M2002-094]**. Here both sides are on the face of the filings: the asset side engine by engine type with its depreciation
policy and its write-downs, the funding side by facility, rate and maturity, with $1,533.5 million of the $2,320.9 million
of debt non-recourse to the parent at 2026-06-30 (10-Q balance sheet note 2). No derivatives book beyond five interest-rate
swaps ($334.5 million notional, net fair value $0.1 million, Item 7). The economics are understood as a spread between
rents and funding, plus a residual; the products' engineering is not needed **[M2011-014]**.

**Doubt, said plainly.** The residual-value variable is the one I could be "way off on" **[M2011-084]**. I do not judge it
outside the circle, because its size is visible over the whole span read (gains, write-downs and the 55% residual policy
year by year) and Q2 and Q7 below are read on that record; a doubt about Q1 would close here **[M2002-092]**, and I record
that the doubt was weighed and found to be about the residual's size, not about whether the business can be pictured.

- **VERDICT: IN.** The economics are a spread-and-residual lessor's, foreseeable in kind for ten years from filings that
  show the same model, rivals and funding through a full cycle **[M2012-065]**, **[M1998-044]**, **[M2002-022]**. The
  residual is the variable carried forward as the widest.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. The moat is what "protects excellent returns on invested capital"
**[L2007-004]**.

**The parts table.** Leasing and Related Operations: segment income from operations $109.0 million (2025) and $146.3
million (2024); Spare Parts Sales: losses of $4.4 million and $1.7 million (10-K segment note); leasing is 94.9% of 2025
revenue. Leasing decides, by more than half of operating profit in each year read; spare parts does not decide and would
be carried at no growth.

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent?* **[M1995-038]**. The filer's own answer is "the quality of our portfolio
   of aircraft engines, supply reliability, and high level of customer service", engines placed "in high-demand
   locations", and "an engine pooling arrangement" (10-K Item 1, Competition). Each is a practice a rival with capital can
   copy; none is a reason the customer cannot go elsewhere.
2. *The money test: could a well-funded attacker take it?* **[M2011-015]**. The filing says money is the entry ticket:
   "Participants in this sector need access to capital, as well as specialized technical knowledge" (Item 1), and capital
   is entering: the named rivals grew from five in the FY2016, FY2019 and FY2021 10-Ks (GE Engine Leasing or GE Capital
   Aviation Services, Shannon Engine Support, Pratt & Whitney, Rolls-Royce Partners Finance, Engine Lease Finance) to nine
   in FY2025 (AerCap, Shannon, Pratt & Whitney, Rolls-Royce Partners Finance, ELFC, FTAI Aviation, MTU Aero Engines, SMBC
   Aero Engine Lease, StandardAero); and the company itself brought outside money into the field in December 2025, a
   Blackstone fund that "plans to deploy over $1 billion into target asset types" and a Liberty Mutual fund that "will
   invest up to $600 million" (Item 1). Where "a dozen people want to go into it" **[M2000-077]**, the castle is not keeping
   them out.
3. *Pricing power, and the agony before a rise* **[M2005-020]**. Rents are fixed for the lease term and set by the market
   at each re-lease: "If interest rates increase, it is unlikely we could increase lease rates in the short term" (Item 7,
   cash flows). Usage-fee rates rise by "systematic, contractual increase" (Item 7), a contract term, not a price the
   customer accepts against an alternative.
4. *Would the customer still choose it over the low bid?* **[M2017-009]**. "It is common for commercial aircraft
   operators and MROs to utilize several leasing companies to meet their aircraft engine needs and to minimize reliance on
   a single leasing company." (Item 1). The customer spreads its business on purpose; the commodity row's mark is exactly
   this indifference, "most insureds don't care from whom they buy" **[L2004-003]**.
5. *The input side.* "There is no organized market for the spare engines or the aircraft we purchase." and "The market for
   purchasing engine and aircraft portfolios is highly competitive, generally involving an auction bidding process."
   (Item 1A). The engines are bought at auction against the same rivals and leased against them.
6. *The low-cost position* **[M2018-043]**, **[L2004-007]**. In a lessor the costs are the cost of money and the cost of
   running the fleet. The filer answers the first itself, in every 10-K read from FY2016 to FY2025: "competing engine
   lessors may have lower costs of capital" (Item 1A). The competitor row below measures it.
7. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Narrowing, on the filing's own record: more named rivals (five
   to nine), general and administrative expense rising from 3.6% of average assets (2016) to 5.4% (2025), stock pay from
   $3.7 million to $44.6 million, and a spread over the cost of debt that did not widen (below).
8. *What could destroy it, five to fifteen years out* **[M2000-014]**. The host-aircraft transition the filing names: an
   engine's value "begins to decline rapidly once the host aircraft is retired" (Item 1); "The advent of superior engine
   and aircraft technology and higher production levels could cause our existing portfolio of aviation equipment to become
   outdated" (Item 1A heading). The company answers it by buying new engines (commitments of $857.4 million for 46 LEAP
   engines by 2030 and about $104.0 million for six PW1133 engines in 2026, Item 7), which is the rebuilding the rows warn
   of: "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**.

**The competitor row** (same metrics, each company's own filings: XBRL company facts transcribed from the 10-K or 20-F
filings, first-filed values; `compare.py`; means over 2016 to 2025, range in brackets):

| company (filing) | interest / average debt | (pre-tax income + interest) / average assets | pre-tax income / average equity | debt / equity | overhead / average assets |
|---|---|---|---|---|---|
| WLFC (10-K, CIK 1018164) | 4.7% (3.7 to 5.3) | 5.8% (3.0 to 8.7) | 15.9% (2.5 to 30.9) | 4.3x | G&A 4.2% (3.1 to 5.5) |
| AerCap Holdings N.V. (20-F, CIK 1378789) | 4.0% (3.1 to 4.5) | 5.1% (0.8 to 8.5) | 11.3% (-6.1 to 23.0) | 3.0x | SG&A 0.7% (0.6 to 0.8) |
| FTAI Aviation Ltd. (10-K, CIK 1590364) | 6.9% (5.9 to 8.1) | 5.2% (-1.3 to 20.3) | not meaningful (equity near nil 2022 to 2024) | n/m | not computed |

Year by year, WLFC's interest over average debt was above AerCap's in nine of the ten years and equal in one (2020, 4.3%
each): 2016 4.6% against 3.8%; 2019 5.2% against 4.4%; 2022 3.7% against 3.3%; 2025 5.3% against 4.5%. AerCap is the
right rival on the cost of money: it bought GE Capital Aviation Services, the rival WLFC's FY2019 and FY2021 10-Ks named
first, and it is named first in FY2025. Flags: AerCap's figures are the whole company, aircraft and engines together (its
engine business is not separable in the facts read); its 2020 and 2022 include the pandemic and the Russia write-off, and
2023 to 2025 the insurance recoveries. FTAI's figures before its 2022 spin-off include the infrastructure business it
then held; its pre-tax results were losses in seven of the ten years. **Named rivals that do not file with the SEC, or file
only inside a larger parent:** Shannon Engine Support (no SEC filing read), Pratt & Whitney (inside RTX), Rolls-Royce
Partners Finance (inside Rolls-Royce plc, UK), Engine Lease Finance Corporation (no SEC filing found), MTU Aero Engines
(Germany, no SEC filing), SMBC Aero Engine Lease (inside Sumitomo Mitsui Financial Group, whose 20-F does not separate
it), StandardAero (files a 10-K since its 2024 offering, but it is an engine repairer with no leasing book to compare on
these metrics; not used).

**The field's returns over the last full cycle, judged in words** (section C). Over 2016 to 2025, which runs from the
2019 peak through the 2020 to 2022 trough to the present peak, the field's leading lessors earned on their assets,
before tax and before interest, about a point more than they paid to borrow: WLFC 5.8% against 4.7%, AerCap 5.1% against
4.0%. In the trough WLFC earned less on its assets than its debt cost (2021: 3.2% against 3.9%; 2022: 3.0% against 3.7%)
and 2.5% before tax on its equity. Its pre-tax return on equity, 15.9% on average, is made by debt at more than four
times equity, the case the rows read before crediting a return: rule out "a cyclical peak in earnings, a monopolistic
position, or leverage" **[L1994-009]**; "we could make it almost any number you want if we just used enough leverage"
**[M2001-054]**; "dealing in what is basically a commodity" with "part of that is because the banks are geared up more"
**[M2007-013]**. The present years, 30.9% (2024) and 26.5% (2025) on equity, reach the height of 2019's 27.9% and no
higher, so I read them as the cycle's peak, not a change for the better to be credited **[M2017-026]**; the box below does
not rest on that reading, because the cost test fails in the trough and the peak alike. My judgment, in words as the
convention asks **[M1999-108]**: these are ordinary returns, a borrowed-money spread on a standard asset, which a durable
castle would not need leverage to show.

**The rows that decide.** The plainest is about this kind of business itself: "pure money-type leasing is not an
attractive business for us when we’ve got other people with a lower cost of funds. I mean, they’ve got the edge." and
"some people have done well in it by, in recent years, by using short-term money to finance longer-term assets which have
big residual risks" **[M2016-029]**. It is a row about leasing in general, weighed with the tests above and not deciding
alone. The commodity rule: "a company must lower its costs to competitive levels or face extinction" **[L1994-035]**;
"commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; the cost is measured against the
competitor, "if your costs are on parity or less" and "than your other major competitors, that is much more important to
you than the absolute level" **[M2001-013]**; and fewness of rivals does not cure it, "you can have only two competitors and
they’re still terrible businesses" **[M2013-052]**. Engine leasing as the filings describe it is a commodity-type field: a
standard asset, bought at auction, leased to customers who spread their business over several lessors, priced at the
market each time it is re-leased. WLFC is not its low-cost operator: it says rivals have lower costs of capital in every
10-K read, it paid more for its debt than AerCap in nine years of ten and the same in the tenth, and its overhead per
dollar of assets is several times AerCap's. Its unlevered return was a little higher than AerCap's (5.8% against 5.1%),
which is what a higher-cost lender in a riskier niche should earn, and the spread over its own debt was the same point.

Contrary evidence, written down **[M1997-127]**: (1) service is named as an escape from the commodity class, where "the
people care enormously about service" **[M2001-014]**, and WLFC sells availability and engine pooling plus maintenance,
storage and teardown services; but the customer's own conduct, using several lessors, shows the service does not tie it,
and the segment that is not leasing loses money. (2) The short-term leases, 40% of the book by net book value at
2025-12-31 (47% at 2024), carry "non-refundable, usage-based maintenance fees" (Item 1), a richer product than long
leases; the richer product shows in the unlevered return, and still only a point over the cost of debt over the cycle.
(3) The returns of 2024 and 2025 are high; read above as the peak. (4) G&A includes the service businesses, so the
overhead comparison with AerCap overstates the gap in pure leasing; the cost-of-funds comparison does not depend on it.

- **VERDICT: OUT.** A commodity-type field in which WLFC is not the low-cost operator, on its own admission and on the
  rival's filings over the whole span, and whose durable players earn ordinary returns over the full cycle, shown on
  their own filings: the high-cost producer in a commodity field **[L1994-035]**, **[M1997-010]**, **[M2001-013]**, and the
  standing castle that protects only ordinary returns **[L2007-004]**, **[M2013-052]**; the castle is shown open on the
  evidence, so OUT and not TOO HARD **[M2011-015]**, **[M2006-013]**.

## Q3 to Q10, Q12: NOT REACHED
The file is closed at Q2 (operator rule 2). Nothing below this line is a clearance. The facts already found for later
questions are under AFTER THE STOP, and the value arithmetic is headed COMPUTATION, NOT A CLEARANCE.

---
## THE BOX
**OUT at Q2** (after Q1 IN): engine leasing is a commodity-type field and Willis Lease is not its low-cost operator, on
its own 10-Ks and on AerCap's filings over 2016 to 2025, and the field's durable lessors earn ordinary returns over the
full cycle. COMPUTATION, not a clearance: value range -$58.57 to -$18.47 a share (all-equity, cycle base) against $37.61;
no case earns the floor at the price. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box is unchanged (operator rule 2) **[M1997-127]**.*

**Q3 (capital).** Assets rose from $1,338 million (2016) to $3,936 million (2025); owner cash before interest, after
maintenance and after the company's tax (below), averaged $86.3 million over 2015 to 2019 and $111.6 million over 2020 to
2025, while net fleet investment beyond maintenance averaged $247.9 million a year over 2020 to 2025: about 1.7% a year of
added owner cash on the added capital (`value.py`). Purchase commitments of $961.4 million at 2025-12-31, $348.5 million
due within a year (10-K Item 7).

**Q4 (the accounts).** (1) The 10-K's MD&A features "Adjusted EBITDA", $459.1 million for 2025, which adds back stock
compensation ($44.6 million) and write-downs of equipment ($32.9 million) along with depreciation and interest (10-K Item
7, "NON-GAAP FINANCIAL MEASURES"). (2) Engines are depreciated over 15 years to a 55% residual (Item 7, critical
policies); write-downs recur in every year read, 2015 to 2025, from $4.4 million (2023) to $32.9 million (2025); gains on
sale recur too, $3.1 million (2022) to $54.0 million (2025). (3) Cash taxes are a small fraction of the provision every
year; the deferred tax liability is $264.8 million at 2026-06-30. (4) Stock pay rose from $3.7 million (2016) to $44.6
million (2025), $5.3 million of it from accelerated vesting on the former General Counsel's resignation (Item 7). (5) The
10-K was refiled as a 10-K/A on 2026-03-30 to include Inline XBRL files "inadvertently omitted from the Original Filing"
(10-K/A explanatory note). (6) The auditor, Grant Thornton (since 2021), names the valuation of equipment held for
operating lease a critical audit matter. (7) In 2025, $13.8 million of non-recurring project expenses on a sustainable
aviation fuel project the company "decided to cease investment in", against $6.3 million of government grants received
for it (10-K Item 7 and note 1(y)).

**Q5 (the people), integrity facts recorded, not judged.** (1) The Executive Chairman and founder, Charles F. Willis, IV,
"beneficially owned or had the ability to direct the voting of" 3,075,576 pre-split shares, about 40% of issued shares,
and "effectively controls the Company" (10-K Item 1A). (2) 2025 total compensation in the proxy's Summary Compensation
Table: Executive Chairman $52,091,481 (stock awards $33,628,868, option awards $11,364,000, bonus $5,251,327); CEO Austin
C. Willis $19,209,005 (DEF 14A 0001193125-26-177136); net income attributable to common shareholders for 2025 was $108.1
million. The proxy says the 2025 stock column holds two programmes' grants (2024's, granted April 2025, and 2025's,
granted January 2025). (3) The 2025 cash bonus pool was funded at "approximately 255% of target" on "Pre-bonus, pre-tax
income of $189 million" (proxy), a measure with no charge for the capital employed, in a year whose pre-tax income
included the $43.0 million gain on selling BAML to the company's own 50% joint venture WMES (10-K Item 7). (4) A
non-qualified option for 900,000 post-split shares granted to the Executive Chairman in November 2025, six-year term
(10-Q note 11). (5) Related-party dealings: the BAML sale to WMES ($45.0 million, half of the proceeds, $22.5 million,
recontributed to the joint venture as a non-cash contribution, cash-flow supplement); engines sold to WMES ($52.7 million,
gain $3.7 million; and $55.6 million as equipment sales) and to CASC Willis ($13.6 million); about $0.1 million a year
paid to an entity in which the Executive Chairman has an interest, approved by the independent directors; 90,000
post-split shares bought from the Executive Chairman at a 2% discount to the day's volume-weighted price, approved by a
special committee of independent directors (10-K Items 5 and 7). (6) Holders' rights: a rights agreement with DBJ as the
Series A holder, action only at meetings, an 80% supermajority for certain changes of control (Item 1A). (7) The 8-K of
2026-07-10 (0001193125-26-300912) is signed by Scott B. Flaherty as "Executive Vice President and Chief Financial
Officer"; the 8-K of 2026-09-08 (0001018164-26-000074) signs him "Executive Vice President and Chief Executive Officer".
Read as a clerical slip; recorded only because the 2026 filings carry another correction of record (the Certificate of
Correction of 2026-09-24 nullifying a 2024 Series A filing, 8-K 0001018164-26-000082).

**Q6 (the money and the owners).** (1) Buybacks: a $60.0 million plan with no stated price; none bought under it in 2024,
2025 or the first half of 2026; $39.6 million unused (10-Q note 10). The one 2025 purchase, 90,000 post-split shares from
the Executive Chairman at about $42.09, sits above the bottom of the COMPUTATION range below (-$58.57), recorded for the
Q6 test, not weighed. (2) Issuance: 2,965,206 pre-split shares granted under the 2023 plan by 2025-12-31 (8,531,064
post-split by 2026-06-30); $200.0 million of convertible notes (May 2026); $35 million of Series B preferred (September
2026); restricted shares cancelled to pay withholding tax, $27.9 million in the first half of 2026. (3) A three-for-one
split in July 2026; the speakers' own view of splits is Berkshire's conduct, "we do not consider splitting the stock a
pro-shareholder move" **[M1997-019]**, a test of another company only by inversion. (4) WNG II: twelve aircraft and
thirteen engines for an adjusted price of about $262.9 million, ten of the engines and six of the aircraft intended for
joint ventures or managed vehicles. (5) Three commercial buildings in Coconut Creek for $118.0 million, agreement signed
2026-08-03, closing "subject to customary closing conditions" (8-K 0001018164-26-000070); not known to have closed. (6)
Common dividend $0.133 a share a quarter after the split (8-K 0001018164-26-000063).

**Q9 (debt and exposures).** (1) Debt $2,320.9 million at 2026-06-30 against equity of $710.3 million; "Substantially all
of our assets are pledged" (Item 1A); $1,533.5 million non-recourse to the parent (10-Q). (2) Maturities at 2025-12-31:
$109.7 million within a year, $475.1 million in one to three years (Item 7). (3) The revolving facility's covenants: interest
coverage at least 2.25 to 1.00 on an EBITDA basis, and total indebtedness to tangible net worth not above 4.25 to 1.00
(Item 7); at 2025-12-31 balance-sheet debt over equity was 4.08 times (my division, not the covenant's definition).
(4) $732.7 million floating at 2025-12-31 (Item 7A). (5) One customer 13% of 2025 lease rent; 69% of rent from non-US
lessees; "We may not be able to repossess an engine or aircraft when the lessee defaults" (Item 1A). (6) Preferred holders
may require redemption on, among other events, "incurring an operating or ordinary loss for two (2) consecutive fiscal
years" (Series B 8-K; the Series A carries the same trigger, 10-Q note 10); the Series B holder may put on 2031-09-29.

**Q12.** None of the named businesses applies.

### COMPUTATION, NOT A CLEARANCE: the value range and the fair price (reporting convention; neither is a verdict)
*Q7's range convention, in full, applied after the stop because the brief asks for the two figures. Arithmetic in
`ownercash.py` and `value.py`; inputs are the filed cash-flow lines, 2015 to 2025, transcribed from XBRL and
cross-checked for operating cash flow against the filed statements (Step 0).*

**Owner cash, recast by hand for a lessor** (USD millions). `tools/run.py` counts neither the purchases of leased
equipment as capital spending nor the sale proceeds of leased equipment; both are recast here.
- *Maintenance basis (central, specific (e)):* operating cash flow, less stock pay, less depreciation as the maintenance
  guess **[M1998-127]**, **[M2000-144]**, less write-downs of equipment (a recurring real loss of value **[R1996-023]**), plus
  the gain on sale of leased equipment (cash above book realised on the fleet; the brief), less the deferred part of the
  income tax provision, less principal received on sales-type leases (capital, not income), less debt issuance costs paid
  and preferred dividends paid (equity-only). The all-equity figure adds back interest paid and debt issuance costs after
  tax at the statutory rate (35% to 2017, 21% after), and the preferred dividends.
- *All-spending basis (beside):* operating cash flow, less stock pay and deferred tax, less property capital spending, less
  purchases of equipment held for lease and notes receivable issued, plus sale proceeds of equipment, note collections and
  the 2025 business-sale cash, less joint-venture contributions; the same interest add-back for all-equity.
- **CONVENTION of this run:** the tax charged is the full provision (current plus deferred), not the cash tax; rationale:
  the deferral lasts only while the fleet grows and reverses in the no-growth cases the range is built on, and the
  speakers decline to treat a deferred tax as "a hidden form of equity" **[M2015-030]**. The cash-tax variant is shown beside.
- **CONVENTION of this run:** 2017's deferred tax benefit of $26.4 million (the 2017 tax-law remeasurement) is replaced by
  the statutory 35% on that year's pre-tax income; rationale: a one-off non-cash credit, aberrational under specific (a).

| year | OCF (filed) | maintenance, equity-only | maintenance, all-equity | all-spending, equity-only | all-spending, all-equity |
|---|---|---|---|---|---|
| 2015 | 97.8 | 17.3 | 40.4 | -50.2 | -27.1 |
| 2016 | 91.6 | 2.4 | 29.4 | -43.0 | -16.0 |
| 2017 | 137.1 | 24.8 | 59.3 | -229.7 | -195.2 |
| 2018 | 188.7 | 79.6 | 135.7 | -220.3 | -164.2 |
| 2019 | 230.3 | 110.7 | 166.6 | 47.7 | 103.6 |
| 2020 | 93.4 | -46.0 | 5.0 | -449.5 | -398.5 |
| 2021 | 90.7 | -30.2 | 27.0 | -144.4 | -87.2 |
| 2022 | 144.4 | 17.8 | 71.3 | -109.7 | -56.2 |
| 2023 | 229.7 | 93.3 | 164.7 | 87.7 | 159.1 |
| 2024 | 284.4 | 112.4 | 204.6 | -564.6 | -472.4 |
| 2025 | 283.2 | 75.7 | 197.1 | -84.0 | 37.4 |
| mean 2021-25 (literal window) | | 53.8 | 132.9 | -163.0 | -83.9 |
| mean 2020-25 (cycle base) | | 37.2 | 111.6 | -210.8 | -136.3 |
| mean 2015-19 (prior span) | | 47.0 | 86.3 | -99.1 | -59.8 |

**The specifics, as applied.**
- *(a) Cycle base.* The literal window's first year, 2021, is a trough on the filer's own description ("COVID-19 has
  significantly impacted engine leasing", FY2021 10-K 0001018164-22-000007), and its last, 2025, sits at the height of the
  2019 peak (Q2). The base is the cycle from the year after the 2019 peak to the present peak, 2020 to 2025, mean $111.6
  million all-equity; the growth is measured between that mean and the prior span's, 2015 to 2019 (the earlier trough is
  before the series read; said so): $86.3 million to $111.6 million over 5.5 years between the midpoints, **4.8% a year**,
  aggregate, not per share. The literal window is shown beside ($132.9 million; its own end-to-end growth, $27.0 million to
  $197.1 million, is meaningless off a trough year **[L2005-003]**).
- *(b) Decline.* All-equity growth is positive. Equity-only owner cash fell from $47.0 million to $37.2 million between the
  spans, -4.2% a year, carried as that basis's bottom.
- *(c) Acquisitions.* No business was bought for cash inside the window; the 2025 sale of BAML ($21.9 million cash) is
  netted as a business sold. WNG II closed after the window and before the price date: no earnings of its own are filed,
  so it is credited at nothing and its $262.9 million adjusted price is added to net debt. The signed, unclosed $118.0
  million building purchase is left out of the central figure and shown beside. Not a serial acquirer (no net purchases
  of businesses).
- *(d) Working capital* is inside operating cash flow, counted.
- *(e) Growth spending.* Central case on maintenance only. The growth spending is charged against the growth it bought:
  $247.9 million a year of net fleet investment over 2020 to 2025 for about 1.7% a year of added owner cash on it, worth
  less than its cost, so **the inversion applies**: the maintenance no-growth case is the top of the range and the growth
  case, with its spending charged for ten years, the bottom: "growth can destroy value" **[L2000-023]**.
- *(f) The cap.* 4.8% is below the discount rate; carried ten years it gives $178.4 million, about 24% of 2025 revenue,
  below the highest share of sales earned (40.7% in 2019): no cut.
- Ten years, then zero nominal growth; discounted at 5.43% throughout.

**The basis.** All-equity (central): claims ahead of the common at the latest filed date with the stated subsequent events
added: debt $2,320.9 million less cash $10.7 million and restricted cash $161.5 million at 2026-06-30 = net debt
$2,148.7 million; plus WNG II $262.9 million; plus preferred at liquidation value $100.0 million (Series A $65.0 million and
Series B $35.0 million), less the Series B cash of $35.0 million: **$2,476.6 million**. Operating leases left out ($16.4
million of obligations, Item 7). Market value of the common $857.8 million, so the whole is priced at $3,334.4 million.
Equity-only (beside): owner cash after interest and preferred dividends against the market value, less the WNG II
financing (the Series B cash and claim offset).

**Value range, all-equity, cycle base (central): -$58.57 to -$18.47 a share** against $37.61 (22.808 million shares; on the
cover count of 21.144 million, -$63.18 to -$19.93). The top is the maintenance no-growth case, a whole-business value of
$2,055.2 million at 5.43% against $2,476.6 million of prior claims; the bottom is the growth case with its spending.
- Literal window beside (2021 to 2025 mean, $132.9 million): -$33.03 to -$1.28.
- Cash-tax variant beside (deferred tax not charged): top -$2.65.
- The signed building purchase beside: the top falls by about $5.17 a share if it closes on debt.
- Equity-only beside (never decides alone): cycle base $10.06 to $18.51; literal window top $31.91.

**The floor is tested first.** At the price, the all-equity no-growth case returns 3.35% a year on what is paid for the
whole (cycle base), 3.99% on the literal window and 3.93% on the cash-tax variant; the equity-only no-growth yields are
4.34% and 6.27%. Even the case the specifics forbid (growth credited, its spending not charged) returns 4.94% at the price.
**No case earns the floor of about ten percent at the price** **[M2003-149]**, so Q7, had it been reached, would close
OUT whatever the width; the price sits above the top of the range, which closes OUT by the same convention.

**Fair price (a reporting figure, never a verdict; Part VII): -$83.51 a share, all-equity basis** (each end case valued at
ten percent: top -$59.65, bottom -$107.37; averaged), after the company's own tax. **Equity-only beside: $2.81 a share**
(ends at ten percent: no growth and the -4.2% decline, averaged). The central figure is the all-equity one.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 08af694c); written question by question; committed after each
      (Q1 923b16f3, Q2 dd62a8fd, this close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      nothing until it is folded into the register by that session (operator rule ten).
- [x] Blind rule: no other run file, holding review, `PORTFOLIO.md`, queue, reading list or resume-state file was opened.
      One breach declared under CONTAMINATION: before the copy, one name-pattern test of `Test Runs/` file names for this
      company (empty result). Commit subjects about another company seen at start-up; not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`check_ids.py`, PASS); no E-ids; every filing fact carries its document and accession.
- [x] The order was kept: Q1 IN, Q2 OUT closed the file; everything after it is recorded, not weighed, and the value
      arithmetic is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash built from operating cash flow and the cash-flow lines, never a net-income proxy (operator rule 5);
      sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, Q1, Q2); integrity facts under AFTER THE STOP and flagged in the
      box line.
- [x] Not a point-in-time run; no anchor rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its capital-spending and sale-proceeds blind spots recast by hand.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A lessor's maintenance spending has no rule.** Specific (e) asks for the maintenance guess where the filing allows
it, and the rows allow depreciation as "a proxy for required capital expenditures" **[M1998-127]**; but for a lessor the fleet is both the plant and the
product, sold off and replaced every year, so whether gains on sale, write-downs and sales-type lease principal belong in
the maintenance figure is a choice the text does not make. I added gains, deducted write-downs and principal, and said so;
another analyst could defensibly leave gains out, which would lower every figure. (2) **Deferred tax.** "Whose tax" settles
whose tax and the carryforward case, not a company that pays almost no cash tax because its tax depreciation runs ahead;
the difference here is about $20 million a year, and I confessed a CONVENTION (the full provision) with the cash-tax figure
beside. (3) **The cycle base when the series begins after the prior trough.** Specific (a) wants peak to peak or trough to
trough; the XBRL series read starts in 2015, so the "prior cycle" is a five-year span, not a cycle, and the 4.8% growth
rests on it. (4) **Preferred stock on the equity-only basis.** The text names borrowings and leases for net debt but not
redeemable preferred; I put it at liquidation value in the all-equity claims and, on the equity-only basis, left it out
because its dividends are already deducted from owner cash; the text should say which. (5) **The all-equity basis in a
spread business.** For a lessor whose whole return is a spread over borrowing, valuing unlevered cash at the long rate
against all claims makes every case negative, while the equity-only figure is positive; the convention says the
equity-only figure "never decides alone", which I followed, but the size of the gap (-$83.51 against $2.81 on the fair
price) shows the basis, not the business, can dominate the reporting figures for any leveraged lessor or lender. (6) **The
brief's competitor list** says the 10-K's "Competition passage names" the nine rivals; in the FY2025 10-K the Competition
passage of Item 1 names none, and the nine are in Item 1A, under "Intense competition in our industry"; a small slip, but
the brief's facts are meant to be checked, and this one was.
