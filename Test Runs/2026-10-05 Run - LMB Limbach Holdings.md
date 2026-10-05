# Company Run — Limbach Holdings, Inc. (NASDAQ: LMB) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The run was dispatched blind: `PORTFOLIO.md`, every holding
review, the session-state file, the queue register and the prepped reading list were not opened, and no attempt was made
to learn whether the operator holds or wants this name.

**CONTAMINATION, declared:** (1) the session opened with the repository's recent commit subjects in view; five of them
record v5 purchase runs of other specialty contractors dated today (FIX, IESC, MYRG, PRIM, MTZ), each closing OUT at Q2.
I did not open those files, nor the EME, FIX or IESC run files listed in `Test Runs/`; every competitor figure below was
fetched fresh from the competitors' own filings. The commit subjects nonetheless told me how five near-peers closed before
I read a page of this company, which is an anchor toward OUT at Q2; I name it so the reader can discount for it. (2) The
memory index loaded with the session carries a one-line portfolio summary ("nothing buyable"); it names no holding and no
view on this company. (3) `tools/run.py` prints v4 material; only its arithmetic lines were read.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $49.53 (2026-10-05, `tools/run.py`, aggregator, live quote only, flagged per operator rule 5); a second
  aggregator quote the same morning read $49.75 intraday (Yahoo chart API, flagged). The month-end closes from the same
  aggregator: $77.00 (June 2026), $71.70 (July), $41.22 (August, after the second-quarter release of 2026-08-04),
  $48.93 (September).
- **Shares by class** from the latest filing's cover: common stock, par $0.0001, **11,924,993** shares (10-Q for the
  period ended 2026-06-30, filed 2026-08-04, accession `0001628280-26-052622`; `python Screens/cover_shares.py LMB`).
  One class. Redeemable preferred appears in the XBRL contexts of the FY2025 10-K as a historical member only.
- **Market cap:** $49.53 × 11.925M = **$590.6M**.
- **Sovereign for the earnings currency:** USD **5.63%**, the 30-year par yield on the US Treasury daily par yield curve,
  dated 2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-03-02, accession `0001628280-26-013285` (Item 1, Item 1A, Item 7, the balance sheet, the
    cash-flow statement, the segment and debt notes).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession `0001628280-26-052622`.
  - DEF 14A filed 2026-04-23, accession `0001628280-26-026892`.
  - 8-Ks: 2025-07-01 (`0001628280-25-033623`, Pioneer Power closing, revolver to $100M); 2025-12-15
    (`0001628280-25-056884`, $50M buyback authorisation); 2026-01-05 (`0001628280-26-000237`, director fees raised);
    2026-05-18 (`0001628280-26-035982`, new COO); 2026-07-24 (`0001628280-26-049590`, revolver to $125M); 2026-08-04
    (`0001628280-26-052611`, Q2 results release ex. 99.1 and the CYMCOR acquisition release ex. 99.2); 2026-09-01
    (`0001628280-26-059713`, 1901 Inc. closing); 2026-09-09 (`0001628280-26-061042`, PNC credit agreement, Wintrust
    facility repaid).
  - History: the 10-Ks for FY2016 (`0001144204-17-020753`), FY2017 (`0001144204-18-018709`), FY2018
    (`0001144204-19-019702`), FY2019 (`0001628280-20-007572`, filed 2020-05-12), FY2020 (`0001628280-21-005652`), FY2021
    (`0001628280-22-006391`), FY2022 (`0001628280-23-007012`), FY2023 (`0001628280-24-010995`), FY2024
    (`0001628280-25-011745`), read for segment tables, write-downs, material weaknesses, acquisitions and the 2021 offering.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
    **$45,700 thousand** in the FY2025 10-K's cash-flow table (Item 7, Liquidity), equal to the XBRL value (45.7) and to
    `tools/run.py`'s "46".
- `python tools/run.py LMB`, arithmetic lines only (saved in `Test Runs/_research 2026-10-05 LMB/run_py.txt`): OCF
  57 / 37 / 46 (FY2023 to FY2025), SBC 5 / 6 / 7, D&A 8 / 12 / 18, capex 2 / 8 / 4. **Defects found and corrected
  below:** its capex omits the vehicle fleet bought through finance leases (right-of-use assets obtained for new finance
  lease liabilities: $5.2M, $7.6M and $13.5M in FY2023 to FY2025, FY2025 10-K cash-flow supplement), so its owner-earnings
  lines overstate owner cash; its five-year window starts at FY2021, whose OCF was negative (−$24.2M).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this contractor "if the market closed for five
years" **[M1997-109]**. The quotation has just halved, from $77 at the end of June to $41 at the end of August; that
movement "doesn’t tell us anything. It just tells us prices." **[M2006-077]**, and it is neither a reason to buy nor a
reason to think the business worse; the filings are. Who is paid to tell me: the company's own releases feature Adjusted
EBITDA and a "free cash flow" defined to exclude working capital and rental-equipment purchases; I read the GAAP lines
and the cash-flow statement instead. The analyst's habits: the research was aimed "to possibly reject your original
hypothesis" **[M1998-144]**, and the hypothesis the company offers (owner-direct service relationships as a protected
franchise) was the one hunted hardest.

**Contrary evidence, written down as found** **[M1997-127]** ("write it down in the first 30 minutes"):
1. FY2025 10-K, Item 1, Competition: "The MEPC systems services industry is highly competitive and fragmented", and the
   first factor named is "price and cost efficiency".
2. FY2025 10-K, Item 1, GCR plan-and-spec bidding: "The Company believes price is the predominant selection criteria in
   this process."
3. FY2025 10-K, Item 1A: renewals are "often competitive" and could be "repriced at lower margins".
4. EME FY2025 10-K: "there are relatively few barriers to entry into the building services industry", and EME's building
   services segment lost "certain facilities maintenance contracts that were not renewed upon rebid".
5. FIX FY2025 10-K: "low barriers to entry in most of our markets"; "price is often the principal factor".
6. LMB's ODR segment, the "higher margin" segment, earned after its own SG&A 6.6% of revenue in FY2021 and 7.6% in FY2022
   (the last years segment SG&A was reported), the same band as EME's building services segment (4.8% to 6.0%,
   FY2018 to FY2025).
7. Q2 2026 release (8-K `0001628280-26-052611`): the chief executive attributes the miss to "project timing and price
   sensitivity in certain markets"; organic revenue fell $17.5M in the half; organic ODR revenue fell $8.6M; gross margin
   fell from 27.8% to 21.9%, partly from "competition for skilled labor and materials associated with construction
   activity in data center markets".
8. The company enters new territory by buying local contractors outright: Pioneer Power $66.6M (July 2025), CYMCOR $30M
   (August 2026), 1901 Inc. $63.0M (September 2026). A regional position can be bought for a sum in tens of millions.
9. History: two material weaknesses at FY2016 and FY2017, one at FY2018 in "monthly project reviews" that failed to
   identify "project claim and pending change order" situations; net losses in FY2018 and FY2019; a $4.4M goodwill
   impairment of the Construction unit in FY2019; negative operating cash flow in 2019 attributed to "project write-downs
   experienced in the Southern California region".
10. In favour, also written down: "The service businesses are generally the better businesses." **[M2009-047]**; no
    customer above 10% of revenue in FY2023 to FY2025; ODR (and predecessor Service) gross margin 25.5% to 31.2% from FY2020 to FY2024; organic ODR
    growth of $58.8M (17%) in FY2025.

## THE STANDING RULE
A purchase would be made for cash, without borrowed money, and sized so that its loss would not touch what the buyer has and needs: "never going to risk what we have and need for
what we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Owning this
name does not put the buyer at risk of ruin. Nothing here bears on the target's own debt, which is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The question:** "can I understand it?" **[M1995-051]**, meaning "what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the 10-K (`0001628280-26-013285`):** a 125-year-old union and open-shop mechanical,
  electrical and plumbing contractor, about 1,500 people in 21 offices in the East and Midwest. Two segments: ODR (owner
  direct: service and maintenance under "evergreen" contracts, time-and-materials repair, retrofits, rental equipment and
  owner-direct projects, $485.7M, 75.1% of FY2025 revenue) and GCR (subcontract work for general contractors, $161.1M).
  Work is "fixed-price, modified fixed-price, and time and materials contracts over periods of typically less than two
  years"; revenue on construction-type contracts is recognised by the cost-to-cost method.
- **The key variables** **[M1998-044]** ("trying to identify the key variables in that particular business"): the price
  obtained at bid and at renewal; the cost and availability of union craft labour; execution on fixed-price work (the
  estimate at completion); and the volume of maintenance and retrofit spending on existing institutional buildings.
- **Are they foreseeable?** The demand variable is: buildings in healthcare, higher education, industry and data centres
  will need their mechanical systems serviced and replaced in ten years, and the trade has done this work for a century.
  The industry is not one of fast-moving technology; controls and automation change, the pipe and the craft do not. The
  insiders would write down where this trade will be in ten years (test 5, "would not want to put down on paper their
  predictions" **[M2000-105]**, does not describe it). The price and labour variables are foreseeable in kind: the
  filings of the company and of three competitors describe the same fragmented, bid-priced, labour-bound trade in every
  year read (FY2016 to FY2025). That is a forecast of the competitive position, which is the half of understanding
  **[M2012-065]** that Q2 then reads.
- **Do the past statements tell me the future ones?** **[M2008-033]** In outline yes: ten years of segment tables,
  backlog and cash flows are on file. The caution is the accounting form (cost-to-cost estimates, claims and change
  orders), carried to Q4: "construction in progress or progress payment-type things" **[M2013-086]**.
- **Doubt:** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. My
  doubt is not about what the business is or how it makes money; it is about whether it has any protection, and that is
  a question the filings answer at Q2 rather than one that is unknowable ("If something’s important but unknowable,
  forget it." **[M2006-076]** does not apply: it is knowable from the record).
- **VERDICT: IN.** The ten-year economics of a regional mechanical service contractor can be sketched from the filings;
  the sketch is what Q2 judges.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, asked from the attacker's side, since "competitors
will repeatedly assault" **[L2007-004]** any castle earning high returns. The castle the company claims is its owner
relationships: being "an indispensable partner" and a "single-source provider" whose maintenance contracts "lead, drive
and support" owner-direct projects (10-K Item 1).

**Test 3, the money test.** "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The company answers
it for me: it enters a new region by buying a local contractor. Pioneer Power (Minnesota, $66.6M, 10-Q note 3), 1901
Inc. (Wisconsin, $63.0M initial for a business the release puts at "approximately $140 million in revenue and $11
million in adjusted EBITDA", 8-K `0001628280-26-059713` ex. 99.1), CYMCOR ($30M, ex. 99.2 of `0001628280-26-052611`).
A buyer with $100 million can assemble a regional MEP service position of LMB's kind. The competitors say the same of the
trade in their own filings: EME, of the building services segment that is the nearest match to ODR, "there are relatively
few barriers to entry into the building services industry" (EME FY2025 10-K, accession `0000105634-26-000025`, Item 1,
Competition); FIX, "the high degree of competition and low barriers to entry in most of our markets" (FIX FY2025 10-K,
`0001104659-26-017530`); IESC, "competitors in certain parts of this market have faced few barriers to entry" (IESC FY2025
10-K, `0001048268-25-000174`). This is the industry of which the rows say "there are some industries that are just never
going to have barriers to entry" **[M2012-106]**.

**Test 8, would the customer still choose it over the low bid?** **[M2017-009]**. The company's own words: GCR
plan-and-spec work is won where "price is the predominant selection criteria"; renewal of service agreements is "often
competitive" and work may be "repriced at lower margins" (10-K Item 1A); and in August 2026 the chief executive named
"price sensitivity in certain markets" as a cause of the quarter's miss (8-K `0001628280-26-052611`, ex. 99.1). EME,
the largest service peer, lost facilities maintenance contracts "that were not renewed upon rebid" (EME FY2025 10-K,
MD&A). The rows' failing answer is the customer who does not care from whom he buys, "most insureds don't care from whom
they buy" **[L2004-003]**. No instance found, in the FY2025 10-K, the Q2 2026 10-Q, the 2026 proxy or the Q2 2026
release, of a customer retention or contract renewal rate (searched for "retention rate", "renewal rate", "customer
retention", "recurring revenue"), nor of the split of ODR revenue between maintenance contracts and projects. The one fact
that would show customers refusing the low bid is not disclosed.

**Test 4, pricing power.** "a prayer session before you raise your prices a penny" **[M2005-020]**. The 10-K says that in
ODR the company "can often adjust pricing to reflect cost increases" on short cycles, and also that it "may be unable to
recover all cost increases in a timely manner". The 2026 record runs the other way: gross margin 21.9% in the first half
against 27.8% a year earlier (10-Q), with the release naming price sensitivity and labour competition.

**Test 6, the low-cost position, and the labour input.** The scarce input is union craft labour, and the company does not
set its price: the Q2 2026 margin fell on "competition for skilled labor and materials associated with construction
activity in data center markets". The rows: "if your costs are on parity or less — labor costs — than your other major
competitors, that is much more important to you than the absolute level" **[M2001-013]**; "the answer is the less labor
intensive business" **[M1997-111]**. About 46% of employees are in collective bargaining units and the company pays into
about 70 multiemployer pension plans, some underfunded (10-K Item 1A). No evidence of a cost advantage over rivals was
found; the overhead runs the other way (below).

**The competitor row, same metric from each company's own filings** (operating income ÷ revenue; XBRL companyfacts
checked against each latest 10-K; LMB from its 10-Ks):

| Year | LMB | FIX (`0001104659-26-017530`) | EME (`0000105634-26-000025`) | IESC (`0001048268-25-000174`, FY to Sept) |
|---|---|---|---|---|
| 2017 | 1.2% | 5.6% | 4.3% | 2.5% |
| 2018 | 0.2% | 6.9% | 5.0% | 3.0% |
| 2019 | 1.5% | 6.3% | 5.0% | 3.9% |
| 2020 | 3.0% | 6.7% | 2.9% | 4.2% |
| 2021 | 2.9% | 6.1% | 5.4% | 5.6% |
| 2022 | 2.4% | 6.1% | 5.1% | 2.6% |
| 2023 | 5.7% | 8.0% | 7.0% | 6.7% |
| 2024 | 7.4% | 10.7% | 9.2% | 10.4% |
| 2025 | 7.6% | 14.4% | 10.1% | 11.4% |

LMB is lowest of the four in every year but 2020 (EME 2.9%). Its gross margin is the highest of the four in 2025 (26.2%
against FIX 24.1%, EME 19.3%, IESC 25.5%) because its SG&A is the heaviest (16.9% of revenue in FY2025, 18.7% in FY2024):
the service model carries a selling and account-management overhead that consumes the gross margin.

**The service segments compared.** EME reports its service and maintenance business as a segment: United States building
services, operating margin 5.0% (2018), 5.4% (2019), 5.3% (2020), 4.8% (2021), 5.3% (2022), 5.9% (2023), 5.7% (2024),
6.0% (2025), against 12.1% and 12.8% in its two construction segments in 2025 (EME 10-Ks for FY2019, FY2021, FY2023 and
FY2025; the 2025 line from `0000105634-26-000025`). LMB reported segment SG&A through FY2022: ODR gross margin 28.9% less
ODR SG&A 22.3% = **6.6%** in FY2021; 25.5% less 17.9% = **7.6%** in FY2022; its predecessor Service segment 24.7% less
18.3% = **6.4%** in FY2019 and 28.5% less 19.5% = **9.0%** in FY2020 (FY2020, FY2021 and FY2022 10-Ks). FIX reports no
service segment (36.8% of its 2025 revenue came from work in existing buildings). So at the operating line LMB's
owner-direct service work has earned what the largest service peer's service segment earns, and that peer earns twice as
much on construction. "The service businesses are generally the better businesses." **[M2009-047]** is the strongest row
for the company, and its reason is capital, not price: "They require less capital". It does not say service work is
protected from competitors, and the evidence above says this service work is not.

**Test 10, widening or narrowing?** "how wide the moat is and whether it’s likely to widen further or shrink on you"
**[M1999-108]**. FY2018 to FY2024 LMB's operating margin rose from 0.2% to 7.4%, by leaving large GCR work and by mix.
In the same years FIX rose from 6.1% (2022) to 14.4% (2025), EME from 5.1% to 10.1%, IESC from 2.6% to 11.4%: the rise was
shared by the whole trade in a construction boom, and LMB stayed at the bottom of it. Then the first half of 2026 (10-Q
`0001628280-26-052622`): total gross margin 21.9% against 27.8%; ODR gross margin 23.5% against 29.0%; GCR 17.5% against
24.7%; organic revenue −$17.5M; organic ODR revenue −$8.6M; net income $9.1M against $18.0M; Adjusted EBITDA guidance cut
from $90M to $94M to $78M to $84M (8-K ex. 99.1). The year's growth is bought: Pioneer Power contributed $37.5M of ODR
revenue in the half. "Every day [...] the competitive position of each of our businesses grows either weaker or stronger"
**[L2005-010]**; the filed record of 2026 reads weaker.

**Test 11, what could destroy, modify or reduce it.** "destroy, or modify, or reduce the economic strengths" **[M2000-014]**:
a construction boom elsewhere (data centres) that bids away the craft labour; a downturn in which institutional owners
rebid maintenance on price; a fixed-price project gone wrong, as in Southern California 2017 to 2019. None of these needs
a new technology; each is the ordinary weather of an open trade, and "one competitor is frequently enough to ruin a
business" **[M2012-108]**.

**The case for the castle, stated as well as I can.** The company's owner relationships are real: hundreds of building
owners, no customer above 10%, healthcare program management that the release says "pulled through approximately $60
million of project bookings" on $3M of fees, and ODR gross margins between 25.5% and 31.2% for five years. Service quality can lift
a business out of the commodity class: "the people care enormously about service" **[M2001-014]**. Against it, the filings
supply no measure of the relationships' durability (no retention rate, no renewal history, no maintenance-contract share),
and the measures they do supply (operating margin against peers, the service segment against EME's, entry by purchase,
price-led bidding in the company's and the peers' own words, the 2026 reversal) all point to an open castle. "anything you
do, your competitors can copy" **[M1996-017]**.

**Routing.** A castle whose future cannot be judged closes TOO HARD **[M2000-019]**; a castle shown open on the evidence
closes OUT **[M2011-015]**, **[M2012-106]**. The future here can be judged, from the company's and its competitors' own
words and numbers, and the judgment is that the trade has few barriers and this firm earns no premium within it. The
missing retention figure is not the deciding fact: even granting sticky relationships, the economics the relationships
produce (ODR operating margin 6.6% to 7.6% when last disclosed, consolidated margin lowest of four peers for nine years)
are an unprotected contractor's.

- **VERDICT: OUT.** The castle is shown open on the evidence: few barriers to entry in the company's and three
  competitors' own filings, price as the deciding factor in its own words, positions bought for tens of millions, the
  lowest operating margin of four peers from 2017 to 2025, and a service segment that earns at the operating line what
  EME's service segment earns. "it’s where I misgauged the competitive position of the business" **[M2012-031]** is the
  error the rows say is made here, and the stop is meant to prevent it.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING: NOT REACHED (run closed OUT at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS: NOT REACHED as a verdict; the balance-sheet reading the owner asked for is
recorded under the computation section below, headed as not a clearance.
## Q5 — WHO RUNS IT: NOT REACHED (proxy facts recorded below as record only).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS: NOT REACHED.
## Q7 — WHAT IS IT WORTH: NOT REACHED; the arithmetic below is a COMPUTATION, NOT A CLEARANCE.
## Q8 — BETTER THAN THE ALTERNATIVES: NOT REACHED.
## Q9 — COULD IT RUIN US: NOT REACHED (debt facts recorded below as record only).
## Q10 — THE FAT PITCH: NOT REACHED.
## Q12 (optional): NOT ASKED. The newspaper test would not be troubled by a mechanical contractor; the business is not one
of the named ones.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was computed after the file closed OUT at Q2 (operator rule 3). It carries no entry language
and clears nothing. It is written because the owner asked for the value range, the fair-price band and the cheap price on
every run.*

### The balance sheets first, FY2017 to FY2025 (Q4's reading rule, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**)
From the filed 10-Ks (accessions in Step 0; the table in `run_py.txt` checked against the FY2025 balance sheet):

| Year-end | Equity | Goodwill + intangibles | Tangible equity | Cash | Receivables | Debt (incl. leases) |
|---|---|---|---|---|---|---|
| 2017 | 48.2 | 24.7 | 23.4 | 0.6 | 129.3 | 20.6 LT |
| 2019 | 46.9 | 18.4 | 28.4 | 8.3 | 105.1 | 38.9 LT |
| 2021 | 87.8 | 28.3 | 59.6 | 14.5 | 89.3 | 29.8 LT |
| 2023 | 120.9 | 41.4 | 79.5 | 59.8 | 97.8 | (leases) |
| 2024 | 153.5 | 74.3 | 79.3 | 44.9 | 119.7 | 27.2 total |
| 2025 | 195.7 | 119.8 | 75.9 | 11.3 | 133.2 | 35.9 total |
| 2026-06 | 203.1 | 118.4 | 84.7 | 17.5 | n/r | 41.1 total |

($ millions.) What the figures say: (1) equity grew from $48M to $196M, but from 2023 the growth went into goodwill and
intangibles; tangible equity has been flat at about $76M to $85M since 2023 while $137M was spent on acquisitions
(2021 to 2025) and $93M more in August and September 2026. (2) Cash fell from $59.8M (2023) to $11.3M (2025); the
September 2026 refinancing repaid "approximately $118.1 million of principal indebtedness" under the Wintrust facility (8-K `0001628280-26-061042`),
so the company that ended 2025 with net debt near zero now carries roughly $120M to $140M of net debt (inferred: the
revolver repaid plus about $23.6M of lease and financing debt, less cash not yet reported; a figure to be read in the
Q3 2026 10-Q). (3) Contract liabilities (billings in excess of costs) fell from $44.5M to $20.9M in 2025: the customer
float that flattered 2023's $57.4M operating cash flow has been running off. (4) Receivables were 26.6% of revenue in
2017 and 20.6% in 2025, collections better than in the troubled years. (5) Retained earnings were negative until 2021
(−$9.7M at 2019); the company was built on the 2016 SPAC merger with 1347 Capital Corp. and an $11.28-a-share net
offering in February 2021 (FY2021 10-K). What they cannot say: the split of ODR between maintenance contracts and
projects, and the retention of owner relationships. The construction-accounting caution stands: "construction in
progress or progress payment-type things — there’s so many ways you can cheat in accounting" **[M2013-086]**; the 2018
material weakness was exactly in claims and pending change orders.

### Owner cash after every real cost (recast; never a net-income proxy, operator rule 5)
Operating cash flow, less purchases of property and equipment, less vehicles acquired under finance leases (capital
spending in another form), less stock pay (a real cost, "all forms of compensation" **[L2021-003]**). $ millions, from the
10-K cash-flow statements:

| FY | OCF | Capex | Finance-lease vehicles | Stock pay | **Owner cash** | Acquisitions | After acquisitions | Net income |
|---|---|---|---|---|---|---|---|---|
| 2021 | −24.2 | 0.8 | 1.3 | 2.6 | **−28.9** | 19.0 | −47.9 | 6.7 |
| 2022 | 35.4 | 1.0 | 2.6 | 2.7 | **29.1** | 0 | 29.1 | 6.8 |
| 2023 | 57.4 | 2.3 | 5.2 | 4.9 | **45.0** | 15.3 | 29.8 | 20.8 |
| 2024 | 36.8 | 7.5 | 7.6 | 5.8 | **15.9** | 36.6 | −20.7 | 30.9 |
| 2025 | 45.7 | 3.8 | 13.5 | 7.0 | **21.4** | 65.7 | −44.3 | 39.1 |
| Avg | | | | | **16.5** | | −10.8 | 20.8 |

Capital spending in all forms ($17.3M in FY2025) ran above depreciation (D&A $18.1M less $8.4M amortisation = about
$9.7M), as the rows say it usually does: depreciation is "almost always true costs" **[L2015-004]**. The growth shown is
on aggregate owner cash: from a negative base in 2021 it cannot be measured, and from 2022 to 2025 it fell ($29.1M to
$21.4M); net income rose fivefold from $6.7M, but "a base year in which earnings were poor can produce a breathtaking, but
meaningless, growth rate" **[L2005-003]**, and much of the rise was bought with $137M of acquisitions. After acquisitions,
the owner took out nothing: −$10.8M a year on average. "are you going to have to put more cash into after you buy it?"
**[M2014-068]**.

### The value range (CONVENTION construction, Part VI)
Discounted at 5.63% throughout; ten years then no growth; equity = value less net debt of $23.5M at 2026-06-30, with the
August and September 2026 acquisitions ($93M) counted at cost against the borrowing that paid for them (a CONVENTION of
this run, confessed: no earnings from them are in the five-year history, and crediting management's EBITDA for them would
be a projection).

| Case | Base | Growth | Value of business | Per share |
|---|---|---|---|---|
| Owner cash, no growth (the cash end) | 16.5 | 0% | $293M | **$22.6** |
| Owner cash, growth capped at the discount rate | 16.5 | 5.63% ×10 | $458M | $36.4 |
| Depreciation variant (net income), no growth | 20.8 | 0% | $370M | $29.1 |
| Depreciation variant, growth capped at the discount rate | 20.8 | 5.63% ×10 | $579M | **$46.6** |

The shown growth of owner cash is not positive, so on the convention's own reading both ends sit at about $22.6. The
depreciation variant is shown beside it, as the convention asks, and its growth is capped at the discount rate rather than
at the shown rate, because the shown rate (net income +55% a year) runs "when the compound rate becomes higher than the
discount rate" **[M1997-095]** and was bought. **Value range, generously drawn: $22.6 to $46.6 a share** (width 2.1 to 1,
inside the three-to-one line). **Price $49.53 sits above the top of the range.** Had the file reached Q7, it would close OUT
through the floor convention: at the price the expected return is below the minimum, "a point at which we drop out of the
game" **[M2003-149]**.

### Fair-price band, cheap price (at the owner's request; COMPUTATION)
- **The floor:** about ten percent pre-tax (CONVENTION, Part VI). Pre-tax owner cash = owner cash $16.5M + average cash
  taxes $5.9M = $22.4M; average pre-tax income FY2021 to FY2025 = $27.2M.
- Price at which the expected pre-tax return is ten percent: owner cash, no growth, **$16.8**; owner cash with growth at
  the cap, $25.6; pre-tax income, no growth, $20.8; pre-tax income with growth at the cap, **$31.6**.
- **FAIR-PRICE BAND: about $22.6 to $31.6**, and only on the generous reading (pre-tax income growing at the cap); on the
  owner-cash reading the band is empty, since the ten-percent price ($16.8) sits below the bottom of the range.
- **CHEAP PRICE: about $11** (half the bottom of the range; CONVENTION of this run, from "buy it at a big discount from
  that present value" **[M1997-126]** and "I would know they were fat" **[M2008-068]**; the framework gives no figure).
- **Against the price of $49.53:** the price is above the top of the range, more than twice the top of the owner-cash
  fair band, and about four times the cheap price. At the price, the pre-tax yield on owner cash is about 3.1% of
  enterprise value (about $720M with the September debt), against a 5.63% Treasury.

### Record only (questions not reached)
- **Q5 record (proxy `0001628280-26-026892`):** chief executive Michael McCann, 2025 total pay $2.76M; short-term bonus on
  Adjusted EBITDA (target $84.3M, actual $81.8M, paid 92.66% of target); long-term awards from 2025 on relative TSR
  against the Russell 2000, earlier on Adjusted EBITDA margin; executives hold 12 to 23 times their guideline. The
  company pays on the figure the rows call "utter nonsense" and talks it in every release; "where people are talking about
  EBITDA, is going to be about zero" **[M2002-026]**. Its "free cash flow" excludes working capital and rental equipment,
  a way to "wave away very real costs" **[L2016-006]**. Recorded, not judged.
- **Q6 record:** $50M buyback authorised December 2025 with no stated price; no shares bought through 2026-06-30 (10-Q);
  three acquisitions for about $160M in fourteen months, paid in cash and debt, no stock issued; tax payments on net-settled
  equity awards $10.7M in 2025. Shares outstanding rose from 7.5M (2017, diluted) to 12.1M (2025).
- **Q9 record:** the PNC facility (September 2026): up to $300M, five-year maturity, maximum net leverage 3.0 times
  EBITDA (3.5 after qualifying acquisitions), fixed-charge cover 1.15, secured by substantially all assets; about $7.0M of
  letters of credit; about 70 multiemployer pension plans, some underfunded, no withdrawal liability recorded.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the evidence: the company and three competitors describe a fragmented trade
with few barriers to entry and price-led awards; LMB buys regional positions for tens of millions; its operating margin is
the lowest of four peers in eight of nine years 2017 to 2025; its owner-direct segment earns at the operating line what
EME's building-services segment earns (6.6% to 7.6% against 4.8% to 6.0%); and 2026 shows the margin falling on price
sensitivity and labour competition. For the record, computed after the close: value $22.6 to $46.6 a share against
$49.53; fair-price band about $22.6 to $31.6 on the generous reading only; cheap price about $11.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not written question by question or committed after each:** the file
      was filled in one pass after the reading, and the dispatch forbade commits. Declared.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script: every id present, every quoted fragment beside
      an id found in that row); no v4 (E-) id is used; every filing fact carries its accession.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; Q3 to Q10 are marked NOT REACHED; the arithmetic after the close is
      headed COMPUTATION — NOT A CLEARANCE and carries no entry language.
- [x] Owner cash after every real cost (OCF less capex, finance-leased vehicles and stock pay), never a net-income proxy;
      net income shown only as the convention's depreciation variant beside it. Sovereign from the US Treasury, dated.
      Aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, in the foundations list, before the Q2 verdict.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; two defects in them found and corrected (finance-lease
      vehicles missing from capex; the five-year window's negative first year).
- [x] `python tools/check_framework.py` PASS before closing (result recorded in the reply; no commit made, per dispatch).
- [ ] Contamination: commit subjects naming five near-peer verdicts were seen before the run (declared at the top). Not
      curable after the fact; the competitor data were refetched and the peers' run files left unopened.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Capital spending in other forms.** The Q7 convention says the cash input "deducts all capital spending", but does
not say whether assets bought through finance leases or whole businesses bought for cash count. Here the difference
decides the picture: excluding leased vehicles overstates owner cash by $13.5M in FY2025, and excluding acquisitions turns
an average of −$10.8M into +$16.5M while the growth that the net-income variant shows was largely bought. I deducted
finance-leased vehicles (they are the fleet) and showed acquisitions beside the figure, not in it; the convention should
say which. (2) **Shown growth from a negative or falling base.** The convention measures shown growth on aggregate owner
cash over five years, but gives no rule when the first year is negative or the series falls while net income rises
fivefold; I read it as "no positive growth shown" and capped the depreciation variant at the discount rate, which makes
the range's top end a choice of mine. (3) **EBITDA talk at Q4.** The text puts the EBITDA count row inside "Why confusion
is a STOP" and lists "managements that talk it" among what Q4 rules OUT, yet calls the make-the-numbers habit a weighing
and states no rule for a company that pays its officers on Adjusted EBITDA; had the run reached Q4 I could not have said
from the text whether that alone closes the file. (4) **The cheap price and the fair-price band** are reporting requests,
not framework terms; the framework has the screamer **[M2009-005]** but no number for it, so the "half the range bottom"
used here is this run's own convention and another analyst may draw it elsewhere. (5) **Acquired businesses after the
history window** (CYMCOR, 1901) are not addressed by the range convention; counting them at cost is mine.
