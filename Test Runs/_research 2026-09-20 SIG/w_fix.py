# -*- coding: utf-8 -*-
p = "Test Runs/2026-09-20 Run - SIG Signet Jewelers.md"
s = open(p, encoding="utf-8").read()

old_tbl = """| window | OE at c = D&A **[E3-44]** | OE at c = total capex | note |
|---|---|---|---|
| **18 years, FY2009–FY2026, as filed** | **$406.4M** | **$409.2M** | |
| **18 years, receivable-sale proceeds removed** | **$390.4M** | **$393.2M** | **the honest long figure** |
| 10 years, FY2017–FY2026, proceeds removed | $546.5M | $561.2M | |
| **5 years, FY2022–FY2026** (the corpus default **[E2-42]**) | **$581.6M** | **$598.7M** | unaffected by the adjustment; both distorted years are outside it |
| 4 years, FY2023–FY2026 (the pandemic year removed, **[E4-41]**) | **$465.0M** | **$477.8M** | |
| 3 years, FY2024–FY2026 | $422.9M | $431.5M | |
| **TTM to 2026-08-01** | **$520.3M** | **$505.8M** | 10-K less H1 FY2026 plus H1 FY2027 |

- **The spread is the range [E4-25], and it is wide: roughly $390M to $600M, a factor of 1.5.**
  **The screen's band was $423M to $599M.** Its **top is right** and its **bottom is 8% too
  high**: the eighteen-year figure the caveat asked for is **$390M**, and the screen could not
  reach it. **The rebuild was owed, it was performed, and it moved the bottom of the band down.**"""

new_tbl = """**CORRECTION, made before the fold commit and recorded rather than made silently (operator
rule 6).** The first version of the table below, committed at `a765ee6`, mislabelled its own
rows: it printed the proceeds-removed eighteen-year figure under "as filed", and the
proceeds-plus-run-off figure under "proceeds removed", and it carried the wide variant's
ten-year figures. **No verdict depended on it** - Q2 had already closed the file, and every
variant clears the [E4-28] floor - but a mislabelled table is the kind of thing that gets
quoted later. All three variants are now shown, so no label has to be trusted.

| window | OE at c = D&A **[E3-44]** | OE at c = total capex | note |
|---|---|---|---|
| **18 years, FY2009–FY2026, AS FILED** | $484.1M | $486.9M | counts the sale of the credit book as if it were earnings |
| **18 years, the two "Proceeds from sale of in-house finance receivables" lines removed** | **$406.4M** | **$409.2M** | |
| **18 years, those proceeds AND the receivable run-off removed** | **$390.4M** | **$393.2M** | **the most conservative long figure** |
| 10 years, FY2017–FY2026, proceeds removed | $575.3M | $590.0M | |
| 10 years, proceeds and run-off removed | $546.5M | $561.2M | |
| **5 years, FY2022–FY2026** (the corpus default **[E2-42]**) | **$581.6M** | **$598.7M** | unaffected by either adjustment; both distorted years sit outside it |
| 4 years, FY2023–FY2026 (the pandemic year removed, **[E4-41]**) | **$465.0M** | **$477.9M** | |
| 3 years, FY2024–FY2026 | $422.9M | $431.5M | |
| **TTM to 2026-08-01** | **$520.3M** | **$505.8M** | 10-K less H1 FY2026 plus H1 FY2027 |

- **The spread is the range [E4-25], and it is wide: roughly $390M to $600M, a factor of 1.5.**
- **THE SCREEN'S BAND REPRODUCES EXACTLY, WHICH IS WORTH SAYING BEFORE CRITICISING IT.** The
  screen gave **$423M to $599M** and its caveat said the band was *"4-construction width only
  (3y/5y x two capex ends)"*. This run's **3-year c=D&A figure is $422.9M** and its **5-year
  c=total-capex figure is $598.7M**. **The screen's arithmetic is right and the two methods
  agree to within a rounding step.**
- **What the rebuild adds is the part the construction cannot see, and it sits BELOW the
  screen's floor.** Over the full eighteen filed years the figure is **$406.4M to $409.2M**
  with the receivable-sale proceeds removed and **$390.4M to $393.2M** with the run-off removed
  too - **3% to 8% below the screen's bottom boundary of $423M.** The caveat asked for the
  rebuild, the rebuild was owed, and it moves the bottom of the band down rather than
  confirming it."""

assert old_tbl in s, "table anchor"
s = s.replace(old_tbl, new_tbl)

old_y = """| window | owner earnings | yield on the $3,846.3M cap | points over the 5.34% sovereign |
|---|---|---|---|
| 18 years, proceeds removed | $390.4–393.2M | **10.1–10.2%** | +4.8 |
| 5 years (corpus default) | $581.6–598.7M | **15.1–15.6%** | +9.8 to +10.3 |
| 4 years, pandemic year removed | $465.0–477.8M | **12.1–12.4%** | +6.8 to +7.1 |
| 3 years | $422.9–431.5M | **11.0–11.2%** | +5.7 to +5.9 |
| TTM to 2026-08-01 | $505.8–520.3M | **13.2–13.5%** | +7.8 to +8.2 |"""

new_y = """| window | owner earnings | yield on the $3,846.3M cap | points over the 5.34% sovereign |
|---|---|---|---|
| 18 years, proceeds and run-off removed | $390.4-393.2M | **10.2%** | +4.8 |
| 18 years, proceeds removed | $406.4-409.2M | **10.6%** | +5.2 to +5.3 |
| 5 years (corpus default) | $581.6-598.7M | **15.1-15.6%** | +9.8 to +10.2 |
| 4 years, pandemic year removed | $465.0-477.9M | **12.1-12.4%** | +6.8 to +7.1 |
| 3 years | $422.9-431.5M | **11.0-11.2%** | +5.7 to +5.9 |
| TTM to 2026-08-01 | $505.8-520.3M | **13.2-13.5%** | +7.8 to +8.2 |"""

assert old_y in s, "yield anchor"
s = s.replace(old_y, new_y)

s = s.replace("""- [x] **One error of my own was caught and corrected in place, not silently**: the run first
      wrote "third CEO in three years" from memory, and the 8-K of 2024-10-01 says Gina Drosos
      retired "after twelve years." The correction is written into Q2 where the error was.""",
"""- [x] **TWO errors of my own were caught and corrected in place, not silently.** (1) The run
      first wrote "third CEO in three years" from memory; the 8-K of 2024-10-01 says Gina Drosos
      retired "after twelve years", and the correction is written into Q2 where the error was.
      (2) The first version of the [E4-25] rebuild table, committed at `a765ee6`, **mislabelled
      its own rows** - the proceeds-removed figure was printed as "as filed" and the wide
      variant as "proceeds removed". All three variants are now published side by side and the
      correction is recorded above the table. **No verdict moved**: Q2 had already closed the
      file and every variant clears the [E4-28] floor.""")

open(p, "w", encoding="utf-8").write(s)
print("run file corrected")

# ---- the register entry ----
q = "Screens/WATCHLIST RUN QUEUE.md"
t = open(q, encoding="utf-8").read()
old_r = """Rebuilt across all eighteen
  filed fiscal years, the owner-earnings mean is **$390.4M at c=D&A and $393.2M at c=total
  capex**, against the screen's bottom boundary of **$423M - 8% too high**; the screen's top of
  $599M is right and is the five-year figure ($581.6M to $598.7M). Other windows: 10-year
  $546.5-561.2M, 4-year with the pandemic year removed $465.0-477.8M, 3-year $422.9-431.5M, TTM
  to 2026-08-01 $505.8-520.3M."""
new_r = """**The screen's band reproduces exactly and
  should be said so first**: its $423M is this run's 3-year c=D&A figure of $422.9M and its
  $599M is the 5-year c=total-capex figure of $598.7M, which is precisely the *"3y/5y x two
  capex ends"* construction its own caveat describes. **What the eighteen-year rebuild adds
  sits BELOW that floor**: **$484.1M to $486.9M as filed, $406.4M to $409.2M with the two
  "Proceeds from sale of in-house finance receivables" lines removed, and $390.4M to $393.2M
  with the receivable run-off removed as well - 3% to 8% below the screen's bottom boundary of
  $423M.** Other windows: 10-year $575.3-590.0M (proceeds removed), 4-year with the pandemic
  year removed $465.0-477.9M, 3-year $422.9-431.5M, TTM to 2026-08-01 $505.8-520.3M."""
assert old_r in t, "register rebuild anchor"
t = t.replace(old_r, new_r)
t = t.replace("""puts trailing owner earnings at **US$390M to US$599M on a US$3,846.3M cap, a 10.1% to 15.6%
  yield, ABOVE the ~10% [E4-28] floor on every one of the five windows built.**""",
"""puts trailing owner earnings at **US$390M to US$599M on a US$3,846.3M cap, a 10.2% to 15.6%
  yield, ABOVE the ~10% [E4-28] floor on every one of the six windows built.**""")
open(q, "w", encoding="utf-8").write(t)
print("register corrected")

# ---- the narrative fold ----
r = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
u = open(r, encoding="utf-8").read()
old_n = """| window | c = D&A | c = total capex |
|---|---|---|
| **18 years, receivable proceeds removed** | **$390.4M** | **$393.2M** |
| 10 years | $546.5M | $561.2M |
| **5 years (the corpus default [E2-42])** | **$581.6M** | **$598.7M** |
| 4 years, pandemic year removed [E4-41] | $465.0M | $477.8M |
| 3 years | $422.9M | $431.5M |
| TTM to 2026-08-01 | $520.3M | $505.8M |

**The screen's band was $423M to $599M. Its top is right; its bottom is 8% too high.** The
eighteen-year figure the caveat asked for is **$390M**, and the screen's five-year construction
could not reach it."""
new_n = """| window | c = D&A | c = total capex |
|---|---|---|
| 18 years, AS FILED | $484.1M | $486.9M |
| **18 years, the receivable-sale proceeds removed** | **$406.4M** | **$409.2M** |
| **18 years, proceeds and receivable run-off removed** | **$390.4M** | **$393.2M** |
| 10 years, proceeds removed | $575.3M | $590.0M |
| **5 years (the corpus default [E2-42])** | **$581.6M** | **$598.7M** |
| 4 years, pandemic year removed [E4-41] | $465.0M | $477.9M |
| 3 years | $422.9M | $431.5M |
| TTM to 2026-08-01 | $520.3M | $505.8M |

**The screen's arithmetic is right and should be said so first.** Its band was **$423M to
$599M**; this run's **3-year c=D&A figure is $422.9M** and its **5-year c=total-capex figure is
$598.7M**, which is exactly the *"3y/5y x two capex ends"* construction the caveat describes.
**What the rebuild adds sits below that floor**: over eighteen years the figure is **$406.4M to
$409.2M** with the receivable-sale proceeds removed and **$390.4M to $393.2M** with the run-off
removed too, **3% to 8% below the screen's bottom boundary**. The caveat asked for the rebuild;
the rebuild moves the bottom of the band down rather than confirming it."""
assert old_n in u, "narrative rebuild anchor"
u = u.replace(old_n, new_n)
u = u.replace("""earnings at **$390M-$599M on a $3,846.3M cap - a 10.1% to 15.6% yield, ABOVE the ~10% [E4-28]
floor on every one of the five windows built**, and **4.8 to 10.3 points over the 5.34%
sovereign.**""",
"""earnings at **$390M-$599M on a $3,846.3M cap - a 10.2% to 15.6% yield, ABOVE the ~10% [E4-28]
floor on every one of the six windows built**, and **4.8 to 10.2 points over the 5.34%
sovereign.**""")
u = u.rstrip("\n") + """

## A second error of mine, caught before the fold commit and recorded, not hidden

The first version of the [E4-25] rebuild table, committed in the run file at `a765ee6`,
**mislabelled its own rows**: it printed the proceeds-removed eighteen-year figure under "as
filed" and the proceeds-plus-run-off figure under "proceeds removed", and carried the wide
variant's ten-year numbers. All three variants are now published side by side in the run file,
in the register entry and above, and the correction is written above the table rather than
applied silently (operator rule 6). **No verdict moved**: Q2 had already closed the file, and
every variant clears the [E4-28] floor. The lesson is the cheap one - **a derived table with
more than one adjustment in it should print every variant, because a label is the part a reader
cannot check.**
"""
open(r, "w", encoding="utf-8").write(u)
print("narrative corrected")
