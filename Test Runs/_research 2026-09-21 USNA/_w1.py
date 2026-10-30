import io
p="Test Runs/2026-09-21 Run - USNA USANA Health Sciences.md"
s=io.open(p,encoding="utf-8").read()

step0_new = """## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34%** - date **2026-09-18** - source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`python tools/sources.py`). FRED DGS30 not used; no fallback needed.
- FX: not applicable to the quote. **But note the earnings currency is only nominally USD** -
  91.1% of Core Nutritional net sales were made outside the United States in H1 2026 (10-Q,
  2026-07-04), and China alone was 41.3% of FY2025 consolidated net sales. USD is the reporting
  currency; the sovereign is read as the reporting currency of the filer, and this mismatch is
  recorded rather than adjusted for, because the corpus prices the currency the business earns in
  and offers no method for a basket. Recorded as a limit of this run.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document - date - accession no.:**
  - **Form 10-K, FY ended 2026-01-03 (a 53-week year), filed 2026-03-16, accession
    `0000896264-26-000021`**, primary document `usna-20260103.htm`.
  - **Form 10-Q, quarter ended 2026-07-04, filed 2026-08-13, accession `0000896264-26-000056`**,
    primary document `usna-20260704.htm`. *(This is the newest periodic filing - the `newest_periodic`
    field on the screen row, 2026-07-04, is correct.)*
  - **DEF 14A, filed 2026-04-07, accession `0000896264-26-000026`.**
  - **8-K of 2026-08-04, accession `0000896264-26-000050`** (Items 2.02, 7.01, 9.01) - the Q2 2026
    earnings release, pulled for **[E4-29]** and **[E4-22]**'s third flag, standing since the CGNX run.
- **Figures cross-checked against the filed statement** (Consolidated Statements of Cash Flows and
  of Comprehensive Income, 10-K accession `0000896264-26-000021`): FY2025 **net cash provided by
  operating activities $22,349 thousand**, **equity-based compensation expense $13,828**,
  **depreciation and amortization $32,562**, **purchases of property and equipment $13,823**. All
  four match the XBRL series used at Q4 below to the dollar. FY2025 **net sales $925,257** and
  **earnings from operations $37,432** cross-checked against the filed income statement.

---
## THE CAP FLAG - RESOLVED BEFORE ANY YIELD IS COMPUTED (operator rule 4)

The screen row's loudest field said: *"CAP BELOW FILED PUBLIC FLOAT - cap $263M against a filed
float of $328M (1.25x) as of 2025-06-27. A cap cannot be smaller than a subset of itself.
RE-STRIKE THE CAP BY HAND before using any yield on this row."*

**Neither input is wrong. The comparison is.** Read from the 10-K cover page, accession
`0000896264-26-000021`:

> "The aggregate market value of common stock held by non-affiliates of the registrant **as of
> June 27, 2025**, was approximately $ 328 million **based on a closing market price of $31.13
> per share**."

> "There were **18,456,935** shares of the registrant's common stock outstanding **as of March
> 13, 2026**."

And from the 10-Q cover page, accession `0000896264-26-000056`:

> "As of **August 11, 2026** , th ere were **18,476,534** outstanding shares of the registrant's
> common stock, $0.001 par value." *(the spacing artifact is the filer's; PRIME RULE 1 forbids
> smoothing it)*

The $328 million is a **dollar amount struck at a $31.13 price fifteen months before the cap was
measured.** The closing price on 2025-06-27 was **$31.13** - the price series agrees with the
cover page to the cent, which is the cross-check. The price on 2026-09-21 is **$14.40**, a
**53.7% fall**. The non-affiliate share count implied by the cover is 328/31.13 = **about 10.5
million shares**, against roughly 19 million outstanding, which is consistent with the 10-K's own
statement that *"Gull Global, Ltd., an entity that is solely owned and controlled by our founder,
Dr. Myron Wentz, owned approximately 40.0% of our outstanding common stock at January 3, 2026."*

**So the float is a proper subset of the cap at every single date; the screen compared two
different dates.** This is a **TOOLING DEFECT**, recorded in the fold: `cap_flag` sets a live
market cap against the cover-page non-affiliate market value, which by SEC rule is struck at the
last business day of the registrant's most recently completed second fiscal quarter and can be up
to eighteen months stale. In a stock that has halved it fires with a false claim of arithmetic
impossibility. **The flag was still worth obeying** - it sent a reader to the cover page, which is
exactly where operator rule 4 wanted them. It is a false positive with a true instruction.

**THE CAP, RE-STRUCK BY HAND:**

| | |
|---|---|
| shares outstanding | **18,476,534** |
| share basis | **10-Q cover page, as of 2026-08-11, accession `0000896264-26-000056`** |
| price | **$14.40** |
| price date | **2026-09-21** *(aggregator - live quote only, flagged, operator rule 5)* |
| **market cap** | **$266.1 million** |

No split has occurred between the measurement date and the anchor, so the split-invariance rule
is satisfied trivially; the cover count and the balance-sheet count (18,463 thousand shares issued
and outstanding at 2026-07-04) agree to within the quarter's equity-award issuance. The screen's
$263M differed only by the price used.

---
"""

q1_new="""## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

USANA makes vitamin pills, protein powder and face cream, and sells them to the people who sell
them. There is one customer type that matters: a person who signs up, buys a monthly box of
supplements largely for their own use, and is paid a commission if they recruit others who do the
same. The filing calls them Brand Partners and Preferred Customers and adds them together as
*"active Customers"*; it counts as active anyone who bought at any time in the most recent three
months. Revenue is therefore **customers times average spend**, and the company says so itself:
*"we increase our sales by increasing the number of our active Customers, the amount they spend
on average, or both."*

The cost structure is the tell. Of FY2025's $925.3M of net sales (filed income statement): gross
profit 78.3%, then **Brand Partner incentives of $336.2M - 43.3% of core nutritional net sales** -
paid back out to the customers themselves for selling and recruiting. Roughly forty-three cents of
every core dollar returns to the distributor network as commission, and after SG&A of $337.4M what
was left was **$37.4M of operating earnings on $925.3M of sales, or 4.0%**. This is not a
product-margin business. It is a **recruitment-margin business**: the gross margin is high because
the distributor, not the company, carries the selling cost, and the distributor is then paid out of
that same gross margin. The economics live or die on the size of the network, and the network is
counted in the filing, in people.

Since December 2024 there is a **second business**: Hiya, a children's vitamin subscription sold
direct to consumers online, bought for **$206.1 million in cash** for a 78.85% controlling interest
(Note B, 10-K). That is a different animal - no distributors, no commissions, paid advertising to
acquire a subscriber, lower gross margin (the 10-K attributes the 280 basis point consolidated
gross-margin fall to Hiya's mix). Plus Rise (protein bars, retail) and Oola, both acquired 2022.
Two reportable segments and an "other".

**The scarce input this business controls.** There is none that the company controls. It does not
control the distributor: *"Our Brand Partners may terminate their services at any time and, like
most direct selling companies, we experience a high turnover among new active Customers from year
to year."* It does not control its largest market - China is **41.3% of net sales and 49.9% of core
active Customers**, conducted through BabyCare, under a regulatory regime Item 1A devotes pages to.
It does not control manufacture of nearly half its output - **third-party suppliers and
manufacturers accounted for approximately 44% of product sales in 2025.** The formulations, the
trademarks and the Salt Lake City plant are owned; none of them is scarce. **What the company
actually owns is a list of people who can leave on any day, and the right to pay them forty-three
cents of every dollar they bring in.**

**Will the fundamentals look broadly the same in ten years?** The mechanism will. Someone will sell
supplements to someone else on commission in 2036. Whether *this* network exists at the size that
supports this cost base is a different question, and it belongs at Q2 and Q4, not here. The business
is **relatively simple** in [E3-31]'s sense: two segments, one revenue identity, one cash-flow
statement, no financial leverage to speak of, no derivatives book, no float. There is no part of it
I cannot follow from the filing.

**The Hiya complication is real and does not close Q1.** A direct-to-consumer subscription vitamin
business is also simple. It is a second business bolted onto the first, and the 10-K reports it as a
separate segment with its own net sales, its own subscriber count (181,700 active Monthly Subscribers
at 2026-01-03) and its own goodwill. Two simple businesses reported separately is still
understandable; what the bolting-on does to the **earnings series** is a Q4 perimeter finding,
recorded there, and it is not used to duck the verdict here.

**VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

*Reason for IN, and its limit: the unit economics are legible from one page of the income statement
and one table of customer counts, and both are filed. [E4-46] governs the alternative - a business
that would take months of study is Q1 OUT and no fetch repairs it; this one took one filing.
Nothing in this verdict is a judgment about whether the business is good.*

"""

a=s.index("## STEP 0"); b=s.index("## Q1 -") if "## Q1 -" in s else s.index("## Q1 —")
s = s[:a] + step0_new + s[b:]
c=s.index("## Q1 -") if "## Q1 -" in s else s.index("## Q1 —")
d=s.index("## Q2 — IS IT A FRANCHISE?")
s = s[:c] + q1_new + s[d:]
io.open(p,"w",encoding="utf-8").write(s)
print("OK", len(s))
