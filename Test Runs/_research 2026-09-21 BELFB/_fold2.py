# -*- coding: utf-8 -*-
import io

P = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
s = io.open(P, encoding='utf-8').read()
if not s.endswith("\n"):
    s += "\n"

add = u"""
## UPDATE 2026-09-21 - BELFB (Bel Fuse Inc.): Q1 IN, Q2 OUT on the business. Wave 7, name 18; register entry 150.

**Run file:** `Test Runs/2026-09-21 Run - BELFB Bel Fuse.md`.
**Research:** `Test Runs/_research 2026-09-21 BELFB/` (two workpapers, the peer scripts, the FY2025
and FY2021 10-Ks, the Q2 2026 10-Q, three 8-Ks, the proxy, twelve companyfacts files).
**Step 0.** Sovereign **USD 30-year 5.34% at 09/18/2026**, struck fresh 2026-09-21 from the **US
Treasury daily par yield curve** (issuing authority; FRED not touched). Prices **BELFB $241.97** and
**BELFA $198.83**, both closes of 2026-09-18, Yahoo, flagged aggregator. Shares **2,115,263 Class A
and 12,324,187 Class B** hand-read from the cover of the 10-Q for the quarter ended 2026-06-30,
accession **`0001437749-26-025619`**, as of 2026-07-31, cross-checked against the filed balance
sheet in the same document. **Cap $3,402.7M.** Anchor filing **10-K FY2025,
`0001437749-26-005354`**; hand cross-check on FY2025 operating cash flow, **$80,612 thousand**.

## THE CAP: THIS IS THE FIRST DUAL-CLASS NAME IN WAVE 7 AND THE SCREEN HAD NO WAY TO SEE IT
The row's own `cap_flag` said a $541M cap could not sit under a $1,200M filed public float and
ordered a hand re-strike. It was right, and **the brief's prior about what was broken was wrong.**
BLMN's cap defect four hours earlier was a **stale price**; the brief carried that prior forward
and asked for it to be tested against the two-class structure. **It is refuted. The price was
fine.**

`dei:EntityCommonStockSharesOutstanding` resolves **undimensioned exactly once in Bel Fuse's entire
companyfacts file**:

    end 2011-08-01 | val 2,174,912 | fy 2011 | fp Q2 | form 10-Q/A | frame CY2011Q2I

One row, from 2011. Every filing since tags the element **dimensioned by class**, so an
undimensioned annual fetch falls back on a **fifteen-year-old Class A count**. The screen's figure
reproduces to the dollar: **$248.69 (BELFB close, 2026-08-28) x 2,174,912 = $540.85M**. The anchor
price was three weeks old and immaterial; the share count was **both the wrong class and fifteen
years stale**, and the error is **6.29x**.

What makes this worth writing down beyond the one name: **it is the same failure mode as the SBC
fix of RESUME STATE item 3F**. There, `AllocatedShareBasedCompensationExpense` was dimensioned by
expense line, an undimensioned fetch returned nothing, and `sbc.get(e, 0.0)` **substituted a
plausible zero**. Here a dimensioned tag returns a plausible **number**. In both cases the tool
produced something a reader would accept. `owner_earnings()` was made to refuse; **the share-count
path was not**, and it is the denominator of every price-side field in the queue.

## What the run found
1. **The gate closed on the registrant's own Item 1A, not on an outside judgment.** **[E3-03]**
   criterion 2 asks whether customers think the product has **no close substitute**. Bel answers
   twice in its own risk factors. *"Our business operates in a globally competitive industry,
   **with relatively low barriers to entry.** ... our major competitors, many of which are larger
   than Bel, have significant financial resources and technological capabilities."* And, under
   *There are several factors which can cause our margins to suffer*: *"**The average selling prices
   for certain of our products tend to decrease over their life cycles, and customers put pressure
   on suppliers to lower prices even when production costs are increasing.**"* **A customer who
   believes there is no close substitute does not extract falling prices from a supplier whose costs
   are rising.** Criterion 2 is observable in exactly one place, and that is the place.
2. **Seventeen years is what made the verdict OUT rather than UNKNOWABLE.** Operating margin
   FY2009-FY2025: `-9.5 / 5.0 / 2.5 / 0.6 / 4.3 / 2.8 / 5.0 / -15.3 / 3.5 / 4.9 / -0.3 / 4.0 / 5.8 /
   10.0 / 13.8 / 12.0 / 16.4`. **Thirteen of seventeen below 6%, two negative, nothing above 5.8%
   before 2022.** ROE on the same years averages **4.0%**. **[E2-53]** is the gate that fails:
   *"Once dominant, the newspaper itself, not the marketplace, determines just how good or how bad
   the paper will be. Good or bad, it will prosper."* For thirteen of seventeen years Bel did not
   prosper, so the position was never what set the economics.
3. **The competitor row removed the environment as the defence, which is the BA shape again.**
   Eleven peers, one construction, newest fiscal year and the five most recent. The line that
   decides it is not the level but the **minimum**: **Amphenol's worst operating margin in five
   years is 19.4% and TE Connectivity's is 14.4%, and both are above Bel's BEST of seventeen.**
   Same industry, same customers, same five years. **[E3-61]** says the row shows position and
   cannot show conduct, and that is what makes it usable here: it takes "the industry is just like
   that" off the table, because for two of the eleven it is not.
4. **[E2-58] is the governing equation and the filing prices it.** *"persistent over-capacity
   without administered prices (or costs) equals poor profitability"*, with long-term profitability
   set by *"the ratio of supply-tight to supply-ample years"*. The 10-K's own number for a
   supply-tight year is **raw-material expedite fee revenue of $14.9 million in FY2023 falling to
   $0.1 million in FY2024**: customers paying to jump a queue, and then not.
5. **The step-up is real, is disclosed, and is not a moat.** Gross margin rose every year for five
   (24.7 / 28.0 / 33.7 / 37.8 / 39.1), which is **[E4-32]**'s primary criterion of a great business
   and was this file's favourite hypothesis. Management attributes it, line by line, to **Enercon
   mix** (bought for $325.6M cash), **facility consolidations** in the PRC and Mexico, and
   **favourable exchange rates**. The **only** pricing action named anywhere in the document is one
   sentence: *"Gross margin for 2024 was favorably impacted by pricing actions on certain contract
   renewals."* **[E4-37]**'s agony metric reads off that directly. **[E3-51]** names the alternative
   explanation and Bel's own record supplies the control: the 2022-2025 run is three waves at once
   (the component shortage, defence spending, the datacenter build) and **2009-2021 is the
   shallows.**

## The bull case, built at full strength before it was tested
Bel's Class B stock is up **1,016% over ten years** on the company's own figure. FY2025 is the best
year in its filed history: 39.1% gross margin, 16.4% operating margin, **EBIT on unleveraged net
tangible assets of 39.2%, level with TE Connectivity and above Amphenol**. Backlog of **$452.2M**
against $675.5M of annual sales. The balance sheet is now **debt-free with $306.1M of cash**.
Capital allocation over the last two years looks genuinely good: it bought a defence business
before defence re-rated, sold equity at **$266.00** rather than buying it back at eleven times the
2020 price, and wrote off its failed eMobility investment in public with the causes named. **None
of that is a franchise**, and **[E2-37]** is the sentence that separates them: *"a textile company
that allocates capital brilliantly within its industry is a remarkable textile company, but not a
remarkable business."*

## Priors refuted, in both directions
- **REFUTED, against the screen: the cap defect was not a stale price.** It was the share count,
  wrong class and fifteen years old. See above.
- **REFUTED, in Bel's favour: the `wc_note`'s reading.** Its arithmetic is exactly right, read by
  hand off the FY2021 10-K (`0001437749-22-006139`): accounts payable **+$23,961** against operating
  cash of **$4,632** is **517.3%**. **Its direction is inverted.** The same statement's
  working-capital block nets to a **DRAIN of $36.1 million** (AR -12,982, unbilled -14,140,
  inventories -34,005, other current -2,240, other assets -1,182, AP +23,961, accrued +4,684, other
  liabilities +1,441, taxes -1,510). **The payable did not make the cash; it partly offset a block
  that consumed seven times the year's operating cash.** The flag exists to catch an OCF that one
  line inflated, and 2021 was deflated. **The flag's own docstring already states the limit that
  causes this (it reads annual facts), but the limit that bit here is different and is worth adding:
  it reads one line and not the block, so it cannot see sign.**
- **REFUTED, in Bel's favour: [E5-15] serial issuance.** Class B shares rose **16.9% in six
  months**, which looks exactly like the flag. It is one marketed follow-on, disclosed in advance:
  1,500,000 shares at **$266.00** plus a 225,000 over-allotment, net **$441.6M**, used to retire the
  revolver (8-K `0001213900-26-056732`). Priced **above** today's quote. **[E5-24]**'s first law,
  applied to the company's own paper, in the right direction.
- **CONFIRMED: `level_note` STEP UP, `level_note_oe` EARLY HALF STRADDLES ZERO, and
  `flags_disagree`** are all three right on the rebuilt seventeen-year series, and they disagree for
  a diagnosable reason (below). **[E4-41]** was then applied rather than cited: three favourable
  exogenous breaks are named and removable - the **$14.9M FY2023 expedite fees**, a **$10.1M FY2025
  foreign exchange revaluation gain**, and **gains on disposal of PP&E of $5,701 thousand (FY2025)
  and $6,440 thousand (FY2021)**. Removing them **widens** the gap between the three-year and
  seventeen-year means rather than closing it.
- **CONFIRMED: the `acq_note`'s substance survives its own arithmetic being void.** "62% of cap" is
  really **9.9% of cap** on the corrected denominator, but the point it was making stands: the
  numerator and the denominator are different companies. **FY2025 is the first year on the current
  perimeter and it is one year.**
- **CONFIRMED and acted on: the `spread_caveat`'s rebuild order.** Six windows were run instead of
  two. **The screen's published band reproduces**: four-construction min and max come out **40.2 and
  70.3** against the published **40 and 70**. Only the cap was wrong.
- **CONFIRMED again, for the eighth time in this queue: the standing 8-K EX-99.1 instruction.** The
  **10-K reads clean on [E4-29]** (EBITDA appears ten times, every one contractual). The furnished
  **8-K EX-99.1 of 2026-07-29 does not**: *"Adjusted EBITDA of $48.9 million (23.2% of sales)"* as a
  headline bullet against a filed income from operations of $38,419 thousand; non-GAAP net earnings
  **up 86%** in the same bullet as GAAP **down 5%**; and the release's own subtitle is *"Provides
  Q3-26 Sales and Gross Margin Guidance"*.

## The finding that is new to this project
**EBITDA here is not only the narrative metric. It is the contractual one.** The FY2025 10-K
discloses that the redemption value of the Enercon noncontrolling interest *"is calculated based on
a pre-determined multiple of trailing twelve-months EBITDA"*, and that the earnout owed to Enercon's
sellers turns on *"certain specified EBITDA targets"*. So the measure that deletes already-spent
depreciation is the measure that sets **what Bel will pay for the remaining 20% of a business it
already controls**, and the accreting liability is on the balance sheet at **$102,601 thousand** and
rising ($80,586 -> $93,161 -> $102,601 at the three recent balance dates). **[E5-41]**'s *"reverse
float"* is usually a comment about how a number is presented; here it is a comment about how a price
is set. **Prior Q3 reads have scored [E4-29] on the public narrative alone; this one should be
checked for whenever an acquisition carries an earnout or a put.**

## Tooling defects found - reported, not patched (three)
1. **The share-count denominator has a two-class hole and does not refuse.** Anything reading
   `dei:EntityCommonStockSharesOutstanding` undimensioned gets a 2011 Class A count for this filer.
   **The cheap fix already exists in the row**: `cap_flag` compares the cap to
   `dei:EntityPublicFloat` and it fired correctly here. **It should refuse and go unpriced, the way
   `SBC_UNRESOLVED` and `CAPEX_UNRESOLVED` already do, rather than annotate a number it has just
   shown to be impossible.** A row that carries a `yield_bottom` of 7.43% next to a note saying its
   own denominator is broken is a number a reader will use.
2. **`level_shift`'s zero-crossing guard still covers only the recent half.** RESUME STATE item 3A
   fixed the recent side after ARM. **BELFB's early half crosses zero** (FY2010, 2013, 2014 and 2018
   are negative at the D&A end), which is what produced `flags_disagree` on this row. Fifth
   iteration of the same one function's guard, and the pattern holds: the test reads one side and
   the defect lives on the other.
3. **No tool reads a multi-class cover.** BELFB is the **first dual-class name in Wave 7**. The
   count has to be read by hand from the cover, per class, and then priced per class from two
   separate quotes. **Worth writing into the queue's standing method before the next one arrives**,
   because the failure is silent: a cap built from one class is a number, not an error.

## No price band, and the reversal condition in words
**No alert armed and no `PORTFOLIO.md` row.** The name failed on the **business**, so the QLYS
ruling applies and **price is not a reopening condition at any level [E5-35]**. The reversal
condition, stated so it can be checked against future filings:
1. **A 10-K Item 1A that no longer says *"relatively low barriers to entry"* and no longer carries
   the *Declines in Selling Prices* bullet**, replaced by a statement of realised pricing power;
2. **an MD&A that attributes a margin gain to PRICE** rather than to facility consolidations, mix
   and exchange rates (**[E4-37]** read forward); and
3. **a competitor row in which Bel's operating margin clears Amphenol's five-year minimum of 19.4%
   through a supply-AMPLE year.**
Two consecutive 10-Ks meeting all three would be a new question, not a re-run of this one.

## The uncomfortable part, written down rather than hedged
This is a business whose stock is up **1,016% in ten years** and which earns **39.2% on unleveraged
net tangible assets**, and the file closes it OUT and permanently. **If the margin step-up is
structural rather than cyclical, this is an omission error, and [E3-47] prices omissions as the
expensive kind**: *"their invisibility does not reduce their cost."* The answer is not that the risk
is absent. It is that **[E4-26]** obliged the favourite hypothesis to be attacked hardest, and when
it was, the company's own Item 1A gave the disconfirming evidence in its own words, thirteen of
seventeen years gave the base rate, and two competitors in the same five years gave the control.
**[E4-18]** then governs what to do with a conclusion that would have needed fighting for:
*"there's no degree of difficulty factor ... I'd rather have the universe be a little smaller than
it really is, than being interpreted as larger than it is."*

**And one thing this run did NOT do, stated so it is not read as having been done:** no yield, no
value range, no ranking position and no floor computation for BELFB appears anywhere in the run
file. Q5 did not open. The hand-struck cap is recorded at Step 0 as a **correction to a defective
screen row**, not as a valuation input.

## Acceptance test
`python tools/check_framework.py` **PASS** before the commit. `tools/ledger_verbatim.py` not run:
the ledger was not touched. **Every ledger id written into the run file was resolved against
`principle_ledger.csv`; 83 distinct ids, PHANTOM 0.** One misattribution was caught by that check
and corrected before the commit: the clause *"unless the cash they consume gets to earn a reasonable
return"* was first written under **[E4-20]** and belongs to **[E5-40]**, which is the passage the
framework reads [E4-20]'s gruesome class through.
"""

io.open(P, 'w', encoding='utf-8').write(s + add)
print("narrative fold appended")
