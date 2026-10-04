# TOOL TEST — the Q3 integrity check. **VERDICT: NOT ADMITTED TO v4.**
**2026-08-26.** Built, tested on ten companies, and rejected. Recorded because a test
that cannot fail is not a test, and because the failure is instructive.

## Why it was attempted
The 2026-08-26 audit found that Q3 integrity is **the strongest-evidenced component in the
project** — Wells Fargo fails at the 2014 and 2016 anchors on the 2011 Fed subprime-steering
penalty and the 2012 DOJ fair-lending settlement, years before the September 2016 scandal;
Fifth Third caught at three independent anchors, KLA at two, Franklin Resources at two.

And yet it has **no tooling**, while the valuation layer — whose market-beating claim is
**unproven** — has a full pipeline and a screener. Verifying Citigroup 2007 earlier today
meant hand-pulling a 5MB 10-K and reading Item 3. That is exactly the friction a tool
should remove, and removing it sits inside Ruling 14 because it fetches rather than judges.

## The test set
Six names with known, documented matters, and four controls. **A tool that flags everything
is useless**, so the controls matter as much as the positives.

| expected heavy | expected light |
|---|---|
| WFC, C, KLAC, FITB, BEN, MO | ROST, ORLY, FAST, TJX* |

\* TJX is the edge case: its 2022 CPSC penalty is real but was ruled a **product-safety**
failure, not the financial dishonesty toward owners that Q3 tests.

---

# FAILURE 1 — the structured layer is blind before ~2010

XBRL litigation tags, `--since 2000-01-01`:

| | tagged matters | earliest | what is missing |
|---|---|---|---|
| **WFC** | **1** | 2010-11-05 | **the 2011 Fed penalty and 2012 DOJ settlement — the two matters that make WFC the validation case — do not appear** |
| **KLAC** | **0** | — | **the 2006 options-backdating fraud is invisible** |
| **C** | 8 | **2024-05-03** | the entire Enron / WorldCom / Adelphia / Parmalat era is invisible |
| MO | 101 | 2012 | correctly heavy |
| FITB | 20 | 2010 | correctly flagged |
| BEN | 15 | 2011 | correctly flagged |
| ROST | 0 | — | control behaves |
| FAST | 1 | 2011 | control behaves |
| ORLY | 12 | 2015 | control behaves (small amounts) |
| TJX | 2 | 2026 | the 2022 CPSC matter does not appear |

**Litigation tagging begins around 2010 and is inconsistent even after that.** A tool
reporting *"WFC: 1 matter · KLAC: 0"* gives **false comfort on the two dirtiest names in the
set**. That alone is disqualifying: the failure mode is silent and points the wrong way.

# FAILURE 2 — keyword detection is drowned in boilerplate

Walking all 18 Wells Fargo annual reports and scanning Item 3 for regulatory language:

```
2009-02-27   regulator penalty x2      2018-03-01   regulator penalty x2
2010-02-26   regulator penalty x2      2019-02-27   regulator penalty x2
2011-02-25   regulator penalty x2      ...
2012-02-28   regulator penalty x2      2025-02-25   consent order x2  regulator penalty x2
2013-02-27   regulator penalty x2      2026-02-24   regulator penalty x2
```

**Identical every year for seventeen years.** The detector cannot distinguish 2011, when
the Fed penalty landed, from 2009, when nothing did. Signal-to-noise is zero. The one year
that differs is 2025, which is not the year that matters.

# FAILURE 3 — the extraction does not isolate Item 3

Diffing consecutive years to surface what is *new* — the right idea — returned this for
2010 and 2011:

> "Our subsidiary national banks are subject to regulation and examination primarily by the
> Office of the Comptroller of the Currency…"
> "As a participant in the Supervisory Capital Assessment Program (SCAP) the Parent must
> consult with the Federal Reserve staff before increasing the level of dividends."

That is the **Regulation and Supervision** section, not Legal Proceedings. Taking a
fixed window from the first plausible "Legal Proceedings" match sweeps in adjacent
discussion. Worse, **large filers routinely make Item 3 a cross-reference** — *"see Note 14"*
— so the actual content lives in the notes and the window catches nothing of substance.

---

# VERDICT

**NOT ADMITTED.** Q3 remains a manual read of the filed record, which is what it has always
been and what worked on Citigroup earlier today.

**Nothing in the framework changes.** The check itself is intact and, on the audit's
evidence, is the strongest thing in the project. What failed is an attempt to accelerate it.

The tool stays in `tools/integrity.py` marked **CANDIDATE — NOT ADMITTED**, because its
history-walking machinery (`annual_filings`) is correct and reusable, and because the next
attempt should start from this record rather than rediscover it.

---

# WHAT WOULD ACTUALLY WORK

The operator's proposal during the test is the right design, and the failures above sharpen
it: **the tool should extract and date; the judgment should be made by whoever runs it, and
justified against the corpus.**

1. **Resolve the cross-reference.** Item 3 usually points at a note. Follow the pointer and
   extract *that*, rather than taking a window. This is the engineering work the failed
   attempt skipped.
2. **Diff consecutive years and emit the new text, not a count.** The point-in-time event is
   a matter appearing for the first time. Emit the sentences; do not score them.
3. **Add the sources XBRL cannot reach** — SEC litigation releases and accounting
   enforcement actions by CIK — which is where KLAC 2006 and the Citigroup era actually
   live.
4. **The AI reading the output makes the binary call and cites the ledger for it.** A matter
   is disqualifying because of what the corpus says integrity is **[E2-26, E2-31]**, not
   because a regex fired. TJX is the worked example of why: a real penalty that is
   nonetheless not a Q3 failure, and no keyword can tell you that.

**Estimated honest cost:** the cross-reference resolution is the hard part and it is
per-filer idiosyncratic. This is a real project, not an afternoon.

---

# WHAT THIS TEST WAS WORTH

It cost one build and produced three specific, documented failure modes and a design that
starts from evidence rather than optimism. **It also nearly shipped a tool that would have
reported Wells Fargo and KLA as clean** — the exact two names the framework is proudest of
catching.

That is the case for testing before admitting, made concrete.
