# AUDIT — WHAT ACTUALLY WORKS IN THIS FRAMEWORK, AND WHAT TO CUT
2026-08-26. Commissioned by the operator: "the framework has done very well so far, run
an audit and find what has worked so well about it. I want to be able to simplify it and
read the corpus to verify your findings."

Every finding below carries a file and line reference so it can be checked directly.

---
# PART 0 — THE PREMISE NEEDS CORRECTING FIRST

**The framework's market-beating claim is UNPROVEN, and it was this project's own audit
that withdrew it, on 2026-07-25.** Any simplification built on "it has done very well"
would be built on a result that no longer exists.

| Test | Clean? | Result |
|---|---|---|
| BT-9, BT-10, BT-14 (93.9% / 98.5% / 100% beat rates) | **NO — look-ahead bug** | **WITHDRAWN** |
| BT-11, 32 years, manual 10-K price extraction | **YES** | **UNDERPERFORMED SPY** |
| BT-15, 8 anchors 2013-2020, corrected screen | **YES** | beat SPY at **2 of 8** anchors; mean **-0.81 pts/yr**, median **-1.41** |
| BT-16, 944 one-year holdings, 13 anchors | **YES** | win rate **49.6%**; median pass trails SPY by **1.45 pts** |

The bug: market cap was `price x shares_at_anchor` using a price back-adjusted to today's
share basis. Companies that split are overwhelmingly companies whose stock rose, so the
screen was finding future winners *because* they were future winners. AAPL at 2013-06-30
computed to $11.7B against a real ~$372B. Re-tested on the corrected screen, only 5 of
BT-10's 18 survivors still clear Book One, and NVDA — the single largest contributor to
the headline result — misses the hurdle at **0.31%**.

**Every test that beat the market ran through the buggy screen. The only uncontaminated
full-gate test lost.**

**On the live portfolio.** HRB +25%, NCLTY +27%, TBTC +35%, V and MITSY up. That is five
positions over six weeks in a rising market. It is too short, too few, and has no control
group. The framework's own doctrine settles how to read it: this morning TJX fell 12.5%
and the finding was that this told us nothing about value. That has to hold in both
directions or it is not a rule.

**None of this says the framework is bad.** It says the evidence for the part everyone
cares about is not in yet. What follows is what the evidence *does* support.

---
# PART 1 — THE FOUR THINGS THAT DEMONSTRABLY WORK

These survive the bug because none of them depends on a price.

## 1. GATE 3 INTEGRITY IS THE STRONGEST RESULT IN THE PROJECT
Filings-based, point-in-time, and it repeats at independent dates.

**The Wells Fargo case is the cleanest validation the project has produced.** The
fake-accounts scandal broke 2016-09-08. WFC fails Gate 3 at the **2014** and **2016**
anchors anyway — not on hindsight, but on two genuinely prior, filed matters: the
**2011-07 Fed subprime-steering penalty** (falsified borrower income) and the **2012-07
DOJ fair-lending settlement**. **The framework would have avoided Wells Fargo years
before the famous scandal, using only information available at the time.**

Repeat catches at independent anchors: **Fifth Third at 3 dates, KLA at 2, Franklin
Resources at 2.**

**Corpus verification:** the binary-integrity rule traces to the Owner's Manual candor
principle (OM-12) and to Buffett's repeated statement that integrity is a gate rather
than a weighting. Note the honest cost, recorded rather than hidden: **KLAC returned
+1,961% in BT-9's window and Gate 3 eliminates it** for the 2006 options-backdating
fraud. A gate that only ever excluded losers would be suspicious.

## 2. THE FULL OWNER-EARNINGS FORMULA CATCHES WHAT NET INCOME HIDES
Three companies cleared a net-income-based yield screen and failed outright on the
complete formula, with negative owner earnings in the trough year:

| Ticker | Trough owner earnings | Reported NI |
|---|---|---|
| F (Ford) | **-$255M** | positive |
| CMG (Chipotle) | **-$89.5M** | positive |
| AN (AutoNation) | **-$1,249M** | positive |

This is mechanical, bug-independent, and it is exactly the gap the formula exists to
catch. **It also caught a live position four hours ago**: TBTC's July run used OE = NI
and recorded a Statute cushion of 7.62% that a correct calculation puts at roughly 4.3%.

**Corpus verification:** 1986 letter [E2-23], `Shareholder Letters/1986 Letter.txt:1650`.
The same letter names the failure mode directly: "All of this points up **the absurdity
of the 'cash flow' numbers** that are often set forth in Wall Street reports. These
numbers routinely include (a) plus (b) — **but do not subtract (c)**."

## 3. THE 10:1 LEVERAGE CEILING IS THE BEST MECHANICAL RULE IN THE SYSTEM
One line of arithmetic, no judgment, no exceptions. **Citigroup at mid-2007 computes to
19:1 and fails automatically** — the exact case the rule exists for. It also removed
LNC (17.5:1), STT (11.2:1) and PFG (20.8:1) from the 2018 candidate set.

**Corpus verification:** 1990 letter, on banking: "When assets are twenty times equity —
a common ratio in this industry — mistakes that involve only a small portion of assets
can destroy a major portion of equity."

## 4. THE SELF-AUDIT DISCIPLINE IS THE REAL PRODUCT
This is the finding I did not expect and it is the most valuable one.

- The original claims audit found **9 misattributed quotes, 9 claims found nowhere in the
  corpus, and 5 inventions** passed off as Buffett's or Munger's words, including a
  famous "30-year Treasury... that's my yardstick" line that does not exist verbatim.
- The project then **found and published its own look-ahead bug**, withdrawing four of
  its own best results rather than quietly re-running until the numbers looked good.
- **Today alone it found six more defects**: a stacked-conservatism error (Ruling 7), a
  margin-of-safety rule derived from half a quote (5-A), a trough anchor that would have
  rejected Wells Fargo in 1990 (9), an owner-earnings formula missing its working-capital
  term (10), a single-year misapplication of that same fix, and a Gate 2 that has never
  read a competitor (11).

**No other part of this framework has a track record like that.** The gates are unproven.
The auditing is proven, repeatedly, against itself.

---
# PART 2 — WHAT DOES NOT CARRY ITS WEIGHT

## GATE 8 IS ALREADY DEAD. Of **121 run files, the asymmetry ratio was actually computed
in 10.** Gate 8 is mentioned in 34 and filled in 10. Ruling 6 then moved its one genuinely
useful output — the implied-growth reverse DCF — into the Gate 6 price ladder, where it
is now computed on *every* run instead of one in twelve. **Gate 8 has no remaining job.**

## BOOK ONE DOES NOT SELECT. It is a **coin flip**: 49.6% over 944 holdings, median
trailing by 1.45 points. BT-15 adds that the corrected screen selects **deep-value
cyclicals** (KSS, M, GPS, FOSL, HOG, PBI, IBM, XOM, refiners, regional banks), not
compounders. **Keep it as a cheap candidate generator. Stop treating a Book One pass as
a finding.**

## BOOK TWO CANNOT AUTHORIZE, BY ITS OWN RULING. Ruling 4-B already says the model "may
reject; it may not, by itself, authorize," on Munger's "Warren talks about these
discounted cash flows. **I've never seen him do one.**" A test that cannot say yes and is
run on every name is doing less work than its cost.

## THE CONVENTIONS HAD STACKED. Ruling 7 found conservatism applied at **six** compounding
places. That is not rigour; it is a thumb on the scale that nobody could see.

---
# PART 3 — THE PROPOSED SIMPLIFICATION: EIGHT GATES TO SIX

**The corpus supports a shorter framework, and says so directly.**

> "We've got three boxes at the company: **in, out, and too hard**." — Buffett, 2006
> annual meeting, `Annual Meetings/2006 Annual Meeting.txt:215`

> "**We try to look for easy problems** because those are the ones we find we have the
> answers for. And you can do that in investments. **We don't really try tough things.**"
> — 2007 annual meeting, `Annual Meetings/2007 Annual Meeting.txt:297`

> "**the math is not complicated. But you do have to understand something about the
> business.**" — 1994 annual meeting [E3-27], `Annual Meetings/1994 Annual Meeting.txt:1233`

> "it ought to just kind of **scream at you**" — 1996 annual meeting [E3-25],
> `Annual Meetings/1996 Annual Meeting.txt:1283`

> the 20-punch card — Munger, USC 1994, `Munger Talks (PCA)/Talk 02 ...:309`

Buffett's own filter has three boxes. Ours has eight gates, two books, eleven rulings and
a sensitivity grid. **The complexity is ours, not his, and it is not where the evidence
of value is.**

## THE PROPOSED STRUCTURE

**THE BUSINESS — four questions, each a hard stop**
1. **Can I explain how it makes money, in my own words?** (was Gate 1)
2. **Is it a franchise — and does it beat its competitors on one filing-sourced metric?**
   (was Gate 2, plus Ruling 11's competitor row, which is the single biggest *addition*
   this audit supports)
3. **Are they honest?** Binary, permanent, filings-based. (was Gate 3 — competence and
   alignment demote to *notes*, since only the integrity half has evidence behind it)
4. **Does it survive a 50% owner-earnings decline for two years?** Full OE formula;
   assets/equity > 10:1 is an automatic fail for financials. (was Gate 4)

**THE PRICE — one question**
5. **The price ladder**: CHEAP / FAIR / CURRENT, plus IRR as points of equity premium,
   implied year-1 growth, and years to reach the sovereign. Two verdicts, business and
   price, never merged. (was Gates 6, 7 and 8 — **Gate 8 is deleted; Gate 7's sizing line
   becomes one row of the ladder**)

**THE COMMITMENT — one question**
6. **What would prove me wrong, what is the number, and how big is the position?**
   (was Gate 5 plus Gate 7)

**Net: 8 gates to 6. One gate deleted outright (8). One merged (7). One narrowed (3).
One strengthened (2).**

## WHAT I AM NOT PROPOSING TO CUT, AND WHY
- **Gate 5's pre-committed exit metric.** No backtest evidence either way, but it costs
  one sentence and it is the only thing standing between a thesis and a rationalisation.
  Corpus basis [E1-02].
- **The two-book structure.** Book One is nearly free to run and enforces the hurdle-rate
  discipline; Book Two vetoes. Neither should authorize alone.
- **The verbatim-sourcing rule.** It is the thing that actually works.

---
# PART 4 — HOW TO VERIFY THIS YOURSELF, IN ORDER

Five passages, about twenty minutes, and they carry most of the argument:

| # | Read | Where | Tests |
|---|---|---|---|
| 1 | Owner earnings, the full (c) clause | `Shareholder Letters/1986 Letter.txt:1650` | whether Finding 2 and Rulings 10/11 are right |
| 2 | "no answers in the financial statements" | `Annual Meetings/1994 Annual Meeting.txt:1233` | whether XBRL can ever produce a verdict |
| 3 | What he reads annual reports FOR | `Annual Meetings/1996 Annual Meeting.txt:681` | the competitor row, Ruling 11's biggest ask |
| 4 | "in, out, and too hard" | `Annual Meetings/2006 Annual Meeting.txt:215` | whether eight gates is his method or ours |
| 5 | Wells Fargo, valuation vs the stress case | `Shareholder Letters/1990 Letter.txt:326-332` | Ruling 9, and Finding 1's loss-avoidance logic |

**If passage 4 does not persuade you, do not cut anything.** The whole simplification
rests on the claim that the corpus favours few hard questions over many procedural ones,
and that is the sentence where he says it plainly.

---
# THE ONE-LINE ANSWER TO THE QUESTION ASKED

**What has worked is not the machinery. It is the exclusions and the auditing.** The
gates that earn their place are the ones that throw things out on filed facts — dishonest
managers, negative owner earnings, 19:1 leverage — and the habit of checking the framework
against the corpus and against itself. The valuation apparatus on top has, so far, no
evidence supporting it and one clean test against it.

**The simplification is therefore not a trim for elegance. It is cutting the parts that
have never demonstrated they do anything.**
