
---

## UPDATE 2026-09-21 — APOG (Apogee Enterprises): Q1 IN, Q2 OUT on the business. Wave 7, name 13; register entry 145.

`Test Runs/2026-09-21 Run - APOG Apogee Enterprises.md`. **Price $36.80 (close 2026-09-18,
aggregator, flagged) × 20,868,294 shares from the 10-Q cover of accession
`0000006845-26-000063` = a hand-struck cap of $768.0M**, against the screen's $787M. **Sovereign
5.34%, 09/18/2026, US Treasury daily par yield curve, 30-year, from the issuing authority.**

### The deal note was the thing that governed the arithmetic, and it was stale in both directions

The screen's `deal_note` sent the run to read EX-2.1 to the 8-K of 2026-05-28 and establish which
side Apogee was on. **It is the acquirer, and the note was nineteen days behind reality and one
deal short.** Item 1.01 of that 8-K: *"Apogee Enterprises, Inc. … entered into a Merger Agreement
… with Keller Companies, Inc. … the Company has agreed to acquire all of the outstanding equity
interests of KCI"* — $105M cash, up to $10M earn-out, on cash and the revolver. **Then the 8-K of
2026-07-01 (`0000006845-26-000068`) reports Item 2.01, COMPLETION**, and **the 8-K of 2026-09-03
(`0000006845-26-000087`) signs a SECOND deal** — SIA "GroGlass", Riga, Latvia, at *"approximately
€62.5 million on a cash-free, debt-free basis"*, still pending, expected to close in fiscal 2027
Q3.

**The lesson generalizes and should be carried into every future `deal_note` resolution: the flag
tells you a deal EXISTED on the screen date; it cannot tell you the deal CLOSED, and it cannot
tell you a second one was signed after.** The CSV's `newest_filing` column is what invites the
error — on this row it reads **2026-02-28, which is a REPORT date, not a filing date**, while the
newest actual filing on 2026-09-21 is 2026-09-15. **A run that trusted that column would have
been six months and two corporate transactions behind.**

**What it did to the arithmetic, stated in dollars rather than in warnings.** $177.5M of purchase
price spent or committed in four months = **23% of the hand-struck cap**, none of it in the
FY2026 balance sheet the owner-earnings series is built from; plus **$232.2M paid for UW
Solutions in FY2025**, on the filed cash-flow statement, inside the five-year window. **Counting
all three: $409.7M, 53% of the cap, in deals inside or immediately after the window**; across the
full seventeen filed years, **$626.9M**. The screen's own `acq_note` — *"the numerator and
denominator may be different compani[es]"* — is right and understates itself by a factor of two.
**This is the strongest case yet in the queue for [E4-38]'s publish-every-window remedy being
mandatory rather than stylistic.**

### The finding: the ONE metric a franchise must show, refused by the filer in four segments at once

[E2-44]'s first characteristic is the ability to raise prices *"even when product demand is flat
and capacity is not fully utilized."* The FY2026 MD&A answers it four times, in Apogee's own
words, in the year its demand fell:

| segment | % of net sales | the filer's own sentence | adj. EBITDA margin |
|---|---|---|---|
| Architectural Metals | 36% | *"lower volume, partially offset by **favorable price**"* | 13.5% → **10.7%** |
| Architectural Services | 31% | *"increased volume, partially offset by unfavorable project mix **and lower pricing**"* | 8.0% → **7.0%** |
| Architectural Glass | 19% | *"**lower volume and price** due to lower end-market demand"* | 22.2% → **16.1%** |
| Performance Surfaces | 14% | *"higher volume and price"* (plus $65.3M inorganic) | 25.3% → **21.0%** |
| **consolidated** | | | 12.6% → 14.2% → **11.9%** |

**Two segments carrying half of net sales conceded price outright; the one that raised price still
lost 2.8 points to aluminium; and the one that raised both price AND volume lost 4.3 points
because the business it bought earns less than the business it had.** [E4-37]'s agony metric is
in the risk factors verbatim: *"We may be unable to pass through additional tariff costs to our
customers through price increases"*, and recovery *"may lag the cost increases."* Item 1 supplies
the [E3-03] refusal directly: *"The North American non-residential construction market is
**highly fragmented**. Competitive factors include **price** …"*, and *"we compete with regional
glass fabricators and international competitors **who can provide certain products with
attributes similar to ours**."*

### The refuted prior, and it is mine as much as the screen's: the 2022-2023 numbers were the WAVE

**Apogee earned 18.7% and 20.9% on capital employed in calendar 2022 and 2023 — better than
Gibraltar, near Armstrong.** That is the fact that made this file worth forty minutes, and it is
the fact the competitor row destroys. Ten calendar years, seven listed peers, EBIT ÷ capital
employed, each from its own 10-K facts, with Apogee's late-February fiscal year aligned and the
alignment stated:

| | **APOG** | TGLS | AWI | BLDR | ROCK | GFF | JELD |
|---|---|---|---|---|---|---|---|
| **cal 2022** | **18.7** | **43.2** | 18.5 | **43.1** | 13.1 | −7.9 | 2.2 |
| **cal 2023** | **20.9** | **35.7** | 21.9 | **25.2** | 11.7 | 9.6 | 6.2 |
| **cal 2025** | **9.9** | **25.4** | **26.0** | 8.1 | 11.9 | 11.9 | −27.3 |
| **10-yr mean** | **12.2** | **22.8** | 19.5 | 19.7 | 11.5 | 7.1 | 2.6 |
| **10-yr mean op margin** | **6.7** | **20.6** | 25.8 | 8.1 | 9.8 | 5.9 | 1.9 |

**The whole industry printed its best numbers in the same two years.** That is [E3-51]'s surfing
run and [E4-36]'s fourth cause, *"Catching and riding some sort of big wave"* — not a moat.
**Calendar 2025 settles it: APOG back to 9.9%, BLDR to 8.1%, JELD to −27.3%, while TGLS holds
25.4% and AWI 26.0%.** The tide went out and two names were still dressed. **The screen's own
`window_disagree` flag predicted this in so many words** (*"the 9yr base may already contain the
wave [E4-41]"*) **and it was right — which is now the second wave-7 name where that flag was the
most valuable thing on the row.**

**And a related prior of the reading list's is worth correcting in passing:** Tecnoglass earning
three times Apogee's operating margin **on the same product, in the same market, over the same
decade** is the clean disproof of the reflex that "architectural glass is a commodity, so nobody
earns in it." Somebody does. It is not Apogee.

### [E4-55] with the concealment running through acquisitions rather than pricing

Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level. **Apogee's
version is the same disease with a different vector: consolidated net sales FY2019 $1,402.6M →
FY2026 $1,404.7M, with $232.2M of cash paid in between for a business the 10-K says "delivered
upon the first-year financial targets of $100 million in revenue."** Seven fiscal years, a
quarter of a billion dollars, and the top line is **$2.1M higher** — so the pre-existing business
is roughly **7% smaller in nominal dollars** and very much smaller in units, through a period of
heavy construction-cost inflation. The three architectural segments make it explicit:
**$1,317.6M → $1,238.9M → $1,206.8M, −8.4% in two years.** Backlog $720.3M → $693.8M. **Standing
note for future runs: where a filer publishes no unit series, "revenue net of what was bought" is
the honest [E4-55] proxy, and it is computable from the acquisition line of the cash-flow
statement plus the acquired revenue the 10-K discloses.**

### The disconfirming case that nearly worked, and why it did not — [E4-26], [E2-43]

**Performance Surfaces earns a 21.0% adjusted EBITDA margin on proprietary brands (Tru Vue,
ChromaLuxe, ResinDEK, Unisub), it is growing, and both 2026 acquisitions were bought for it.**
That is the real argument for a franchise inside this company and the run took it seriously.
Three answers, and **the third is the one worth carrying forward as a method**: on the capital
actually employed, **Performance Surfaces is the WORST of the four segments** — FY2026 segment
EBIT of $26.5M (adjusted EBITDA $41.6M less segment D&A $15.2M) against identifiable assets of
**$337.1M = 7.9%**, against Architectural Glass 16.0%, Services 15.2% and Metals 12.1%. **The
segment that looks most like a franchise on MARGIN is the one whose returns were bought rather
than earned**, because the $232.2M paid for UW Solutions sits in its asset base. **[E2-43] is the
rule that catches this and it should be run on every segment table in this queue where the filer
publishes identifiable assets: a margin comparison across segments of an acquisitive filer is
meaningless until the denominator is looked at.** The same test also disposes of the third
argument — *"one of only a few architectural glass installation service companies in the U.S. to
have a national presence"* is filed and true, **and that segment earns the lowest margin of the
four**, which is [E2-53] running backwards.

### Tooling defects

1. **NEW, AND IT AFFECTS EVERY LOW-CAPEX ROW IN THE QUEUE: `best_year_dep` measures single-year
   dependence on the WRONG SERIES, and `flags_disagree` does not fire when it and
   `best_year_dep_oe` disagree.** On this row `best_year_dep` reads **0.079** and prints the
   verdict string *"no single-year dependence (9-yr OCF series)"* while `best_year_dep_oe` reads
   **0.121** — **a 53% disagreement with `flags_disagree` empty.** Rebuilt by hand, dropping
   FY2024 moves the FY2018-FY2026 owner-earnings mean from **$69.5M to $59.1M (−15.0%)** and the
   FY2022-FY2026 mean from **$76.6M to $57.5M (−24.9%)**. **A quarter of the five-year
   owner-earnings mean is one year, and the screen says there is no single-year dependence.** The
   mechanism is arithmetic and general: **subtracting a roughly constant (c) and SBC from a
   variable OCF series AMPLIFIES the outlier's share of the mean rather than damping it**, so the
   OCF-based flag will under-report single-year dependence on every filer whose capex is small
   and stable relative to its operating cash flow. **Not patched — recorded**, because it changes
   the semantics of a published column and that is the operator's call.
2. **`newest_filing` is a REPORT date, not a filing date, and it invites exactly the error the
   `deal_note` warns about.** On this row it reads 2026-02-28 while the newest filing was
   2026-09-15 — a six-month, two-transaction gap. **Every run should check EDGAR directly; this
   run did, and that is the only reason the closed Kalwall deal and the pending GroGlass deal are
   in the file at all.**
3. **`cap_flag`'s "One of the two is wrong" is wrong for the FIFTH consecutive run.** CALM, EMBC,
   BRBR, FC and now APOG: **the two dates differ.** Here the float is struck 2025-08-29 at $43.98
   and the cap at $36.80 twelve and a half months later, with 269,500 shares retired for $9.7M in
   one quarter in between; −16.3% of price plus the count reproduces the 1.16x to rounding. **The
   proposed rewording is now seconded twice and should be adopted: "or the two dates differ."**

### A prior REFUTED, which is the happier kind of finding

**FC's tooling defect (i-a) — "the screen priced off the stale ANNUAL cover when a newer 10-Q
cover existed" — does NOT reproduce here, and FC's warning that it would recur "on every filer
retiring ~5% of its shares a year" is too strong.** Tested: the screen's $787M implies **$37.71**
on the 10-Q count of 20,868,294 and **$37.09** on the annual count of 21,220,737; the closes on
the screen's own dates were **$37.59 (2026-09-01)** and **$38.06 (2026-09-02)**, which bracket
$37.71 and not $37.09. **The screen used the newer 10-Q count on this row.** The whole $787M →
$768M gap is nineteen days of price, and it points the safe way — the screen made APOG look
**dearer** than it is. **So (i-a) is a per-row question, not a systematic bias, and the standing
instruction should be to TEST it each time rather than to assume it.**

### And the uncomfortable part, recorded as MGPI and FC recorded theirs: THE PRICE WAS NEVER THE PROBLEM

**COMPUTATION — NOT A CLEARANCE** (operator rule 3; no entry language, and Q5 was never opened).
Owner earnings rebuilt by hand over **seventeen fiscal years** from the filed consolidated
statements of cash flows — OCF less SBC less (c), with (c) shown at both the [E3-44] D&A default
and the total-capex end — against the hand-struck **$768.0M** cap and the **5.34%** sovereign:

| window | OE, (c) = D&A | OE, (c) = capex | yield |
|---|---|---|---|
| FY2022-FY2026, the [E2-42] default | $76.6M | $87.7M | **9.97% – 11.42%** |
| FY2018-FY2026 | $69.5M | $76.9M | **9.05% – 10.02%** |
| FY2010-FY2026, everything filed | $51.9M | $55.4M | **6.76% – 7.21%** |

**The five-year window clears the [E4-28] ~10% floor; the seventeen-year window is nowhere near
it.** That is `window_disagree` being right in dollars — and the seventeen-year series carries
the reason it should not be trusted at the short end: **owner earnings were NEGATIVE in FY2011
(−$41.4M to −$22.3M) and near zero in FY2012 and FY2013**, which the five-year width structurally
cannot see. **THIS IS THE THIRD CONSECUTIVE WAVE-7 NAME WHOSE PRICE WAS NOT THE PROBLEM** —
MGPI, FC, APOG — and the fact that three in a row have closed on the business while looking cheap
is itself worth watching: **it is what the gate order is FOR, and it is also exactly the pressure
operator rule 9 says the analyst will feel.** No bar chosen, no margin applied, **windage count
0**.

### What was NOT done, and why

- **No `tools/alerts.json` band and no `PORTFOLIO.md` row.** The QLYS ruling: a name that failed
  on the BUSINESS does not get a price alert. **The reversal condition is in words:** *reopen
  this file only if the Performance Surfaces Segment — post-Kalwall, post-GroGlass — reaches a
  majority of consolidated net sales AND holds an adjusted-EBITDA margin above 20% for three
  consecutive fiscal years while the architectural segments shrink; that is, only if Apogee stops
  being a bid-priced construction business and becomes a branded-coatings business.* Management
  is moving in exactly that direction, and the arithmetic says how far: **$177.5M has bought
  roughly $130M of revenue against $1.2bn of architectural sales, so the reversal is three or
  four more deals away and no price move triggers it.** Carried against **[E3-47]** —
  wrongly-closed files inside the circle are the expensive error class, and this one is inside
  the circle.
- **No survival shape counted in `Screens/SURVIVAL SHAPES - index.md`.** The file closed at Q2
  and Q4 was never reached as a gate, so on the PAGP, MGPI and FC precedents this is **the
  signature without the verdict** and is deliberately not counted.
- **Nothing in `Framework/`, `CLAUDE.md` or `principle_ledger.csv` was edited by this run.**
- **No tool was changed.** The three defects above are recorded, not patched.

### Acceptance test and the pointer

`python tools/check_framework.py` **PASS before the commit** — 0 phantom citations, 0 unlabelled
numbers, every ledger row verbatim against its cited source. **Every ledger id cited in the run
file was then checked directly against `principle_ledger.csv`: 62 distinct ids, 0 phantom**; the
register entry's 14, likewise 0. **Eight verbatim renderings were spot-checked back to the
ledger's own text before the commit** — [E4-37]'s *"agony they go through"* and *"prayer
session"*, [E3-51]'s *"mired in shallows"*, [E2-58]'s *"persistent over-capacity"* and *"ratio of
supply-tight"*, [E2-53]'s *"Good or bad, it will prosper"*, [E3-62]'s *"stay home"*, [E4-55]'s
*"not likely to disappear"* — and one was **corrected in place**: [E4-36]'s fourth cause is
*"Catching and riding some sort of big wave"*, which the run had paraphrased as "wave-riding"
from the framework's summary; **PRIME RULE 1, the ledger's own words now stand in the file.**
**`CLAUDE.md` still says the ledger is 267 rows; the file is 311 data rows. TENTH consecutive
wave-7 fold to record that stale pointer, which remains the operator's call and not a run's.**
