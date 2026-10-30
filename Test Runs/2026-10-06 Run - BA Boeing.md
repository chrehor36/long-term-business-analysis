# Company Run: The Boeing Company (NYSE: BA), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before
any fetch. Research folder: `Test Runs/_research 2026-10-06 BA/` (`run_py_output.txt`, `cover_shares_output.txt`,
`sources_output.txt`, `series.py`, `owner_cash.py` and its output, `led.py`, `competitor_row_notes.md`; raw filings in
its gitignored `cache/`).

*(Style note: the em dash is avoided in written work, so operator rule 3's heading is written "COMPUTATION - NOT A
CLEARANCE".)*

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not
opened, so whether the operator holds Boeing is unknown to this analyst and played no part.

**CONTAMINATION DECLARED.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the run queue, the
prepped reading list, `tools/alerts.json`, any earlier run or research folder for BA. Opened for FORM only: the
2026-10-05 Adient run (`Test Runs/2026-10-05 Run - ADNT Adient.md`, its Step 0 and its closing sections); it says nothing
about Boeing. Seen without opening: the names of other 2026-10-05 runs in a directory listing, and five recent commit
subjects. Training memory: this analyst carries a prior about Boeing (the 737 MAX groundings, the 2024 strike and
equity raise, the Spirit purchase); every fact below is taken from the filings, and the prior was used only to know
which filings to open. One ledger row names Boeing (**[M2021-039]**, a remark about a supplier's earning power); it is
the speakers' only mention of the company found by a text search of `principle_ledger_v5.csv` for "Boeing".

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $192.72 (2026-10-05, live quote printed by `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: common stock, $5.00 par, **790,370,020** as of 2026-07-21 (10-Q for
  the quarter to 2026-06-30, filed 2026-07-28, accession `0001628280-26-050038`; `python Screens/cover_shares.py BA`).
  **Second class, read from the charter note in the 10-K:** 5,750,000 shares of 6.00% Series A Mandatory Convertible
  Preferred Stock, liquidation preference $5,750M, converting on or about 2027-10-15 "into between 5.8280 and 6.9940
  shares of common stock" each (FY2025 10-K, accession `0001628280-26-004357`, Item 1A and Note 20). At a price above
  $171.59 ($1,000 / 5.8280) the minimum rate applies: **33.511M** common as converted. Also $230M of Spirit 3.250%
  Exchangeable Notes due 2028 assumed in the Spirit purchase (immaterial, not added). **Diluted count 823.881M.**
- **Market cap:** common $192.72 x 790.370M = **$152,320M**; as converted (with the preferred) **$158,780M**.
- **Sovereign for the earnings currency:** **5.66%**, the US Treasury 30-year par yield, 2026-10-05 (issuing authority,
  `python tools/sources.py`, saved to `sources_output.txt`). Boeing reports and borrows in USD.
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-01-30, accession `0001628280-26-004357` (Item 1, Item 1A, Item 7, the statements, Notes
    on inventories, backlog, the preferred stock).
  - 10-Q for the quarter to 2026-06-30, filed 2026-07-28, accession `0001628280-26-050038` (cover).
  - Earnings release, 8-K filed 2026-07-28, accession `0001628280-26-049929`, EX-99.1 (second quarter 2026).
  - Proxy (DEF 14A) filed 2026-03-06, accession `0001193125-26-096787`: fetched; not read in substance, because the run
    closed before Q5.
  - 8-K filed 2026-08-28, accession `0001628280-26-059427` (a $3.0B 364-day revolver replacing the old one; the two
    five-year revolvers extended; a new covenant to keep liquidity of at least $5.0B; debt capped at 60% of total
    capital). 8-K filed 2026-08-21, accession `0001628280-26-058481` (a new controller from Ernst & Young, from 2027).
  - For the history: 10-K FY2022, accession `0000012927-23-000007` (cash flows 2020 to 2022, 777X timing);
    10-K FY2019, accession `0000012927-20-000014` (cash flows 2017 to 2019, 777X timing).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
  **$1,065M** on the filed Consolidated Statement of Cash Flows (10-K `0001628280-26-004357`, page 57) = the $1,065M
  `tools/run.py` transcribed from XBRL. Also capex $2,942M and share-based plans $426M (run.py: $427M; one million of
  rounding) match.
- `tools/run.py BA` arithmetic lines only (Part VII); output saved as `run_py_output.txt`. **What its owner-earnings
  line leaves out, found on reading the filing:** the cash-flow statement adds back, as a non-cash item, "Treasury
  shares issued for 401(k) contribution": $1,530M (2025), $1,601M (2024), $1,515M (2023), $1,215M (2022), $1,233M
  (2021), $195M (2020) (10-K FY2025 and FY2022). The employees' retirement match has been paid in Boeing stock since
  2020. It is compensation, and the speakers' earnings are counted "after [...] all forms of compensation"
  **[L2021-003]**; `tools/run.py` deducts only the share-based plans line, so its owner earnings overstate Boeing's by
  about $1.5B a year from 2021. Deducted below. (A tool defect, reported, not fixed.)

### Owner cash after every real cost (USD millions)
Operating cash, less share-based plans expense, less the 401(k) match paid in shares, less capital spending; the
depreciation basis beside it. Sources: the filed cash-flow statements named above; 2016 from the XBRL facts
(`series.py`). Arithmetic in `owner_cash.py`.

| FY | OCF | Stock pay | 401(k) in shares | Capex | D&A | **Owner cash (capex)** | Owner cash (D&A) |
|---|---|---|---|---|---|---|---|
| 2016 | 10,496 | 190 | 0 | 2,613 | 1,889 | **7,693** | 8,417 |
| 2017 | 13,346 | 202 | 0 | 1,739 | 2,047 | **11,405** | 11,097 |
| 2018 | 15,322 | 202 | 0 | 1,722 | 2,114 | **13,398** | 13,006 |
| 2019 | -2,446 | 212 | 0 | 1,834 | 2,271 | **-4,492** | -4,929 |
| 2020 | -18,410 | 250 | 195 | 1,303 | 2,246 | **-20,158** | -21,101 |
| 2021 | -3,416 | 833 | 1,233 | 980 | 2,144 | **-6,462** | -7,626 |
| 2022 | 3,512 | 725 | 1,215 | 1,222 | 1,979 | **350** | -407 |
| 2023 | 5,960 | 690 | 1,515 | 1,527 | 1,861 | **2,228** | 1,894 |
| 2024 | -12,080 | 407 | 1,601 | 2,230 | 1,836 | **-16,318** | -15,924 |
| 2025 | 1,065 | 426 | 1,530 | 2,942 | 1,953 | **-3,833** | -2,844 |
| **5-yr mean 2021-25** | | | | | | **-4,807** | -4,981 |
| 10-yr mean 2016-25 | | | | | | -1,619 | -1,842 |

First half 2026 (EX-99.1, `0001628280-26-049929`): operating cash $1,185M less capex $2,008M = -$823M, before stock pay
and the 401(k) shares. Over the ten years 2016 to 2025 the owner cash sums to about **-$16.2 billion**: the business
consumed owner cash in aggregate across a decade that includes its three best years.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own Boeing "if the market closed for five years"
**[M1997-109]**, which asks for a view of what the business will earn, not of the quote. The market serves and does not
instruct **[M2006-077]**: the price of $192.72 says the market expects a recovery; it carries no instruction. Margin of
safety **[M1996-084]**: whatever follows must not need a pencil. No macro enters **[M2000-094]**: the airline cycle and
the defence budget are not forecast here. Who is paid to tell you **[M2020-037]**, **[M2001-052]**: Boeing's own
release leads with "free cash flow (non-GAAP)" defined as operating cash less capital spending, a figure that leaves the
$1.5B a year of 401(k) stock and the stock pay inside "free" cash; and the industry's demand forecast (43,600 airplanes in
20 years, 10-K Item 7) is the seller's projection of what it sells. The analyst's habits: write contrary evidence down
at once **[M1997-127]**, look for "what you're missing" **[M2025-013]**, state the other side's case **[M2016-055]**, and
destroy the previous conclusion **[M2016-054]**; this analyst's prior was that Boeing is a broken company, so the
contrary evidence below is the case for it, stated as strongly as the filings allow.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Demand is not the problem. Total backlog $682,207M at 2025-12-31 and a record $715B at 2026-06-30, "over 6,200
   commercial airplanes" valued at $597B (10-K; EX-99.1). At 2025's 600 deliveries that is about ten years of output.
   Net orders in 2026's second quarter were 246.
2. The industry has two makers of 100-plus-seat jets ("one of the two major manufacturers", 10-K Item 7). The other one,
   Airbus, earned EUR 5,470M of adjusted commercial-aircraft EBIT on 793 deliveries in 2025 (flagged secondary source,
   `competitor_row_notes.md`). The duopoly's economics, run well, are visible.
3. Recovery is in the filings: deliveries 348 (2024) to 600 (2025) to 314 in the first half of 2026; the 737 rate
   moved to 42 a month with the FAA's agreement in October 2025 and began moving to 47 in the second quarter of 2026;
   certification flight testing of the 737-7 and 737-10 was completed by July 2026; operating cash was +$1,364M in the
   second quarter of 2026 (EX-99.1).
4. Global Services earned $3.3B to $3.6B a year from operations in 2023 and 2024 (18 to 19% margins in 2026) on a large
   installed fleet (10-K; EX-99.1). That part is a steady earner.
5. The balance sheet was repaired by owners, not lenders: $18,200M of common and $5,657M of mandatory convertible
   preferred issued in 2024 (10-K cash-flow statement), and $10.55B of cash from the Digital Aviation Solutions sale in
   2025. Equity turned positive ($5,454M) at 2025-12-31.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Only through the buyer's own conduct. Bought with no borrowed money and
sized so that a total loss could not touch what the buyer has and needs, a common-stock position cannot call on the
buyer for cash: "We are never going to risk what we have and need for what we don't have and don't need"
**[M2012-081]**; the borrowed money that "can prevent you from playing out your hand" is the one road to the zero
**[M2004-065]**, and no option, collateral or cash-out feature attaches to a share bought outright **[L2014-024]**.
Boeing's own debt ($45.9B at 2026-06-30, EX-99.1) is the target's exposure and belongs to Q9, not to this rule. **No
ruin to the buyer from the purchase as such.**

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The question is not whether airplanes can be understood. "Oh, we understand the product. We understand what it does for
people. We just don't know the economics of it 10 years from now." **[M2000-104]**. Understanding is "a reasonable fix
on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, "where we
think we know, in a reasonable way, what the economics will look like in five or 10 or 20 years" **[M2005-089]**.

**What is foreseeable.** The industry's shape: two makers of large jets (10-K Item 7), a backlog of about ten years of
output, products that live for decades (the 737 has 9,240 cumulative deliveries, 10-K deliveries table), a services
business on the installed fleet. The competitive position in ten years is very likely still one of two. So far the
industry is readable, and if the question were "will the duopoly exist" it would pass.

**The key variables of Boeing's own earning power, and whether they are predictable** **[M1998-044]**:
1. *Unit margins on the 737 and 787 at rate.* Commercial Airplanes lost money from operations in every year shown:
   -$1,635M (2023), -$7,969M (2024), -$7,079M (2025), -$885M in the first half of 2026 (10-K; EX-99.1). What a 737 or
   787 earns at a stable rate of 47 or more is therefore not in any recent statement; it rests on program-accounting
   estimates over 12,400 737s and 1,900 787s (10-K, accounting quantities), and those estimates carry **$11,777M** of
   737 and **$13,859M** of 787 deferred production costs, costs already spent above the average, to be recovered from
   units not yet built (10-K Note 9). The 737 figure rose by $2,098M in 2025.
2. *Certification timing.* Boeing says of the 737-7, 737-10 and 777X that "the FAA ultimately determines the timing of
   certification and entry into service" and "the ultimate timing will be determined by the regulators" (10-K Item 1A,
   Item 7). The production rate of the 737 "may only increase [...] with the concurrence of the FAA" (10-K Item 1).
3. *The cost of the programs in development, commercial and defence.* Reach-forward losses: 777X and 787 $6,493M (2020)
   and $3,460M (2021) (10-K FY2022 cash-flow statement); 777X and 767 $4,079M (2024) and $5,283M (2025), of which 777X
   $4,899M in 2025 (10-K FY2025); five fixed-price defence programs (KC-46A, T-7A, Commercial Crew, VC-25B, MQ-25)
   $5.0B more in 2024, and $280M more on VC-25B in the second quarter of 2026, with "ongoing risk that similar losses
   may have to be recognized in future periods" (10-K Item 1A and Note on estimates; EX-99.1).
4. *Labour and supply.* A 53-day strike in 2024 halted most commercial production; a 101-day strike in St. Louis in
   2025; engineers' contracts covering about 16,000 people expire in October 2026 and "could also have a material
   impact" (10-K Items 1 and 7).

**Test 3: do the past statements tell me the future ones?** **[M2008-033]**. No. Boeing's statements are themselves
estimates of the future (program accounting), and the insiders' own written forecast has moved by years and by tens of
billions. The 777X, launched in 2013, had "first delivery [...] targeted for 2021" (10-K FY2019, accession
`0000012927-20-000014`); then "previously expected in late 2023, and now expect it will occur in 2025" (10-K FY2022,
`0000012927-23-000007`); then "delayed first delivery of the 777-9 to 2027" (10-K FY2025), with a newly found "potential
durability issue on the engine" (same). Each slip came with a charge that the earlier statements did not contain.

**Test 5: would the insiders write it down?** **[M2000-105]**. The insiders did write it down, in the accounting
quantities and the certification dates, and the record of those written forecasts is the evidence against them; the
speakers ask for exactly that record ("I asked that the record of the people who made the projections, their past
projections also be presented" **[M1995-050]**). Boeing's own 10-K now hands the decisive date to the regulator.

**Test 8: how far off could I be?** **[M2011-084]**. Owner cash ran from +$13,398M (2018) to -$20,158M (2020) and
-$16,318M (2024); the ten-year sum is about -$16.2 billion (Step 0). A model of Boeing's earning power in 2036 would have
to choose between a business that throws off $10B or more (2016 to 2018) and one that consumes it, and nothing in the
filings says which. The speakers' one remark on the company puts its troubles among the probabilities a buyer of its
suppliers must carry: "when Boeing has troubles with the Max, well, that's a probability. [...] all kinds of things can
happen" **[M2021-039]**.

**Test 4: important and knowable?** **[M2006-076]**. The margin at rate, the next certification date and the next
reach-forward loss are the most important facts about Boeing's ten-year earning power. They are not knowable from
outside, and the filings show they were not knowable from inside either.

**Test 6 and the by-parts reading.** Seeing the industry is not seeing the company **[M2012-067]**: the duopoly can be
excellent (Airbus) while one of its two members loses money for seven years. Read by its parts (the CONVENTION of Q1 on
the holding company, applied here to segments): Global Services can be understood; Commercial Airplanes, the part that
decides the whole (revenues $41,494M of $89,463M in 2025 and the whole of the backlog's weight), cannot be foreseen; and
"if you have doubts about something being into your circle of competence, it isn't" **[M2002-092]**.

**Which cause, WORK or NATURE.** The rows distinguish the analyst who has not done the work from the industry whose
nature is the roadblock **[L1993-023]**, **[M1994-026]**. Here the work was done: ten years of statements, the insiders'
own dated forecasts, and the regulator's place in the timing were read. What stands in the way is not missing reading
but a forecast that the people with all the information wrote down and then revised for six years; more study would
not supply it ("we're not going to learn enough in the followings five months to make up for" it **[M2008-086]**). The
cause is the nature of this company's position in its industry today (certification and production quality governed
by a regulator, fixed-price development risk, program-accounting estimates over decades), not a gap in this analyst's
reading. **TOO HARD (NATURE).** Contrary view, stated: another analyst could call the cause WORK, on the ground that
the duopoly's economics are visible through Airbus and that a deeper pass on the 737 and 787 unit costs could close the
question; this run judges that pass could only read the same program-accounting estimates that have already failed.

- **VERDICT: TOO HARD (NATURE).** Boeing's ten-year earning power cannot be fixed: the key variables (unit margins at
  rate, certification dates, development-program costs) are "important but unknowable" **[M2006-076]**, the past
  statements do not tell the future ones **[M2008-033]**, and the doubt keeps it outside the circle **[M2002-092]**. It
  is not a judgment of quality: "It doesn't mean it isn't a good buy. [...] It just means that we don't know how to
  evaluate it." **[M2000-038]**; the box is "too hard" **[M2006-013]**. The file closes here.

## Q2: NOT REACHED (the file closed TOO HARD (NATURE) at Q1).
The competitor row was gathered before the close and is kept in `competitor_row_notes.md` (Airbus FY2025: 793
deliveries, commercial-aircraft adjusted EBIT EUR 5,470M; Boeing FY2025: 600 deliveries, Commercial Airplanes operating
loss $7,079M). The Airbus figures are a flagged secondary transcription: airbus.com could not be opened from this
session. No castle verdict is given.
## Q3: NOT REACHED.
## Q4: NOT REACHED as a verdict. The balance sheets are read below under COMPUTATION, as the template asks.
## Q5: NOT REACHED. (The proxy was fetched, `0001193125-26-096787`, and not read in substance.)
## Q6: NOT REACHED.
## Q7: NOT REACHED.
## Q8: NOT REACHED.
## Q9: NOT REACHED.
## Q10: NOT REACHED.
## Q12 (optional): NOT ASKED.

---
## COMPUTATION - NOT A CLEARANCE
*(Operator rule 3: arithmetic made after the file closed; it carries no entry language and clears nothing.)*

**The balance sheets, 2017 to 2025** (`run_py_output.txt`, first-filed XBRL; 2025 and 2024 checked to the filed
statement, 10-K `0001628280-26-004357`, page 56). Debt on the face of the balance sheet went from $11,117M (2017) to
$63,583M (2020) and $54,098M (2025); cash and short-term investments $29,400M at 2025-12-31, so net debt about $24.7B.
Shareholders' equity went from $355M (2017) to -$8,617M (2019) and -$18,316M (2020), stayed negative to 2024
(-$3,908M) and turned positive ($5,454M) at 2025-12-31 only after $23,857M of new common and preferred (2024) and the
$9,672M gain on the Digital Aviation Solutions sale (2025). Retained earnings fell from $55,941M (2018) to $15,362M
(2024). Inventories were $84,679M against revenues of $89,463M in 2025, inside which sit $25.6B of 737 and 787 deferred
production costs (Note 9); advances and progress billings from customers were $59,404M. Goodwill doubled to $17,275M
with the Spirit purchase, paid with about $4.7B of Boeing shares (10-K Item 7). What the figures say: the losses of
2019 to 2024 were funded first by debt and then by owners; what they cannot say is what the deferred production costs
will recover, which is the Q1 question itself **[M2025-032]**. A fact for Q6, had it been reached: $40,640M of buybacks
in 2014 to 2019 (XBRL, `series.py`), then $18,200M of common sold in 2024 (10-K cash-flow statement).

**The Q7 convention, run for the record.** The five-year mean of owner cash after every real cost (2021 to 2025) is
**-$4,807M** (capex basis; -$4,981M on depreciation). A discounted value on a negative base is negative at any growth,
so the convention gives no range: no "fair" price and no "cheap" price exist on the shown record. The ten-year mean is
also negative (-$1,619M). For scale only: at about ten percent (the floor CONVENTION of Q7) on the as-converted market
value of $158,780M, the buyer would need owner cash of about $15.9B a year with no growth, above the best year in the
table ($13,398M in 2018). These numbers decide nothing; Q1 closed the file before them.

---
## THE BOX
**TOO HARD (NATURE), at Q1.** Boeing's ten-year earning power cannot be fixed from the filings: the unit margins of the
737 and 787 at rate rest on $25.6B of deferred production costs to be recovered from units not yet built, certification
dates are set by the regulator, and the insiders' own written forecasts moved the 777X's first delivery from 2021 to
2027 with about $24B of reach-forward losses on commercial and defence programs booked in 2020, 2021, 2024 and 2025.
Q7 not reached; for the record the five-year owner cash mean is -$4,807M, so the convention yields no range against
$192.72. **Reversal condition:** Q1 would be asked again only on new facts, not a lower price **[M2000-038]**: the
737-7, 737-10 and 777X certified and delivering, and several years of positive owner cash after stock pay and the
401(k) shares at stable 737 and 787 rates with no new reach-forward loss, so that the past statements begin to tell the
future ones **[M2008-033]**. Q11 (has the business changed, or only its price) belongs to the holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 (`87a7dbe`) and
      again at the close (write-early).
- [x] Every v5 id resolves (`cite_check.py`: every M, L and R id present in `principle_ledger_v5.csv`, every quoted
      fragment beside an id found in that row, no E- id); every filing fact has its accession; no number without a
      filing or a CONVENTION label.
- [x] The order was kept; Q1's STOP closed the run; nothing after it is a clearance, and the arithmetic sits under the
      COMPUTATION heading.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash less stock pay, the 401(k) match paid
      in shares, and capex, with the depreciation basis beside it (operator rule 5). The sovereign from the US Treasury;
      the price an aggregator quote, flagged; the Airbus row a secondary transcription, flagged.
- [x] Contrary evidence written down as it was found **[M1997-127]** (five items, in the foundations, before the
      verdict).
- [x] No row dated after the anchor is cited (not a point-in-time test; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its yields and refusals were not used as verdicts.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **WORK or NATURE when the insiders did write the forecast down.** Test 5 asks whether the insiders "would not want
   to put down on paper their predictions" **[M2000-105]**. Boeing's insiders do put them down (accounting quantities,
   certification dates) and have missed them for six years. The framework does not say whether a written but
   repeatedly failed forecast counts as "would not write it down". This run read it as NATURE because the 10-K hands
   the deciding date to the regulator; another analyst could call it WORK. The section I text should say which.
2. **An industry understood, a member not.** Q1 says seeing the industry is not seeing the company **[M2012-067]**, but
   its routing sentence speaks of industries that change fast. Boeing's industry changes slowly; the unforeseeable
   variable is one company's execution under regulation. The framework could say whether that closes at Q1 or belongs
   to Q2 (a castle whose future cannot be judged) or Q5 (ability); the box would be the same, the reason recorded
   differently.
3. **Compensation paid in shares outside the stock-pay line.** Neither Q4 nor the Q7 convention names a 401(k) match
   paid in treasury shares, and `tools/run.py` deducts only the share-based plans tag, overstating Boeing's owner
   earnings by about $1.5B a year (2021 to 2025). Deducted here under **[L2021-003]**. **Tool defect reported:**
   `tools/run.py` should read the cash-flow statement's other non-cash compensation lines (here "Treasury shares
   issued for 401(k) contribution"); not fixed, per this run's instructions.
4. **A competitor that does not file with the SEC.** The template asks for the competitor row "from the competitors'
   own filings"; Airbus publishes only on its own site, which this environment blocks. The framework has no rule for a
   row that can be read only second-hand; it was kept and flagged.
5. **Deferred production costs.** Program accounting puts $25.6B of costs already spent on Boeing's balance sheet as an
   asset recovered by future deliveries. Q4's tells name "deferred asset accounts" building up **[M1995-064]**, but
   the framework does not say whether a balance the accounting standard requires is a tell or the ordinary working of
   the method; the run did not need to decide, since Q1 closed first.
