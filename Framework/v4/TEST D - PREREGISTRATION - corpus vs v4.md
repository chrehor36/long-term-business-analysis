# TEST D — PRE-REGISTRATION. The corpus read against v4.
**2026-08-28. Committed BEFORE any agent was launched.** Results append below the line.

## The question

`check_framework.py` proves the forward direction continuously: everything in v4 traces to
the corpus. **The reverse direction has never been tested:** does anything in the corpus
contradict v4, is any load-bearing doctrine absent, and does any v4 rule claim more than its
citation supports? Every targeted question asked of the shelf this month found missing
doctrine (the manager sweep, +19 rows; loss-of-focus [E3-40]; the range rule [E4-25]; Ground
Rule 7 [E1-17]) — three for three, so **omissions are expected. The live questions are
whether any omission is load-bearing, and whether any contradiction survives.**

## Design

Six partitions covering the whole shelf, read in full, **refutation-framed** per the Darwin
antidote **[E4-26]**: each agent's job is to break v4, not to confirm it. An agent returning
"no findings" is treated with suspicion, not relief. Each agent reads
`Framework/THE FRAMEWORK v4.md` and `Framework/v4/THE MANAGER STANDARD - Q3.md` first, may
consult `principle_ledger.csv` to avoid reporting already-rowed material, and returns
findings typed:

- **CONTRADICTION** — a passage that cuts against a v4 rule as written.
- **OMISSION** — doctrine absent from v4. *Load-bearing* (pre-registered definition):
  stated three or more times across the shelf, **or** framed by the authors as central
  ("the most important…", "the number one…", "the first rule…"), **and** capable of
  changing a run's verdict.
- **DRIFT** — v4 states a rule stronger, weaker, or narrower than its cited source supports.

Every finding: verbatim quote + file + line. **Nothing enters the ledger until I re-read the
cited lines myself** — agent transcription is never the transcription of record.

## Pre-registered standard

- **FAIL:** any CONFIRMED contradiction with no corpus-internal resolution. The corpus's own
  evolution does not count against v4 where the corpus graded itself (Hochschild Kohn is the
  worked example: 1966 [E1-16] vs 1989 [E2-38], resolved by the author); an **unresolved**
  tension becomes an open-question row, not a defect.
- **EXPECTED:** omissions. Each is triaged load-bearing or not by the definition above;
  load-bearing omissions become ledger rows and v4 edits, recorded in the results.
- **PASS is not "no findings."** A clean sweep from all six partitions would itself be
  suspect given the three-for-three precedent.

## Known hazards, stated in advance

1. **Content-filter kills.** Three prior agents on the letters partitions died to API
   filters on oversized outputs. Outputs are capped (~50 strongest findings per agent);
   a fourth kill means I read that partition directly, as before.
2. **The corpus index cannot substitute for reading** — 34% of verified passages are missed
   at top-10 from a paraphrase. Agents read the partitions; the index is not part of Test D.
3. **Agent misses are not proof of absence.** Test D lowers the probability of a
   load-bearing gap; it cannot take it to zero. The results will say so.

---
# RESULTS — appended after the agents return, each finding re-verified against source

## INTERIM LOG, 2026-08-28 — four of six partitions received. NO AMENDMENTS YET.

Received: letters 1965–1984 (34 findings) · letters 2000–2025 + OM/Special/Fortune (34) ·
meetings 2010–2025 (29) · Munger/Wesco/Partnership (32). Outstanding: letters 1985–1999,
meetings 1994–2009. Full agent outputs preserved in the session task files; every finding
below re-verified before any ledger row or v4 edit is cut.

### Citations personally re-verified against source so far (verbatim, in context)
1. `2002 Letter.txt:942-945` — "at least 10% pre-tax returns … we will sit on the sidelines" ✓
2. `2012 Letter.txt:466-467` — coverage defined as pre-tax earnings/interest, EBITDA/interest "deeply flawed" ✓
3. `2013 Letter.txt:1028-1034` — five-years-out earnings range; buy at reasonable price vs the bottom boundary ✓
4. `2015 Letter.txt:781-789` — railroad depreciation "falls far short" of maintenance outlays ✓
5. `1982 Letter.txt:27-45` — the primary-test yardstick scoped, then abandoned, with the arrow/bullseye warning ✓
6. `1980 Letter.txt:213-218` — "hurdle rate" used and defined (inflation + owner-level taxes) ✓
7. `1984 Letter.txt:1169-1174` — long bonds "required … to clear a special hurdle" ✓

### Convergence clusters (found independently by 2+ agents; the priority list for triage)
- **"No hurdle floor" is overstated.** 2002 letter 10% pre-tax (verified), adopted verbatim by
  Munger's 2004 Wesco letter; "hurdle" used in 1980/1984 (verified); 12% named "quite
  satisfactory" for utility retention (2012 meeting). Against: [E4-21] 2007. **Unresolved
  corpus-internal tension at minimum; v4's flat denial cannot stand as written.**
- **"The corpus does not supply one" (leverage/coverage) is false as written.** The 2012
  coverage definition (verified); BPL's self-imposed 25% borrowing ceiling; the 1982–84
  published screen criterion "little or no debt."
- **D&A is not a valid floor for maintenance capex in capital-intensive businesses.** 2015
  letter (verified) + 2019 letter + 2016 meeting (">60% of capex"). The band convention needs
  a carve-out.
- **EBITDA/adjusted-earnings is a missing fifth flag** — the most-repeated disclosure tell in
  the shelf (12+ statements, three partitions), and v4's own [E4-22] ellipsis dropped it.
- **The Q3 primary test needs its source's own scoping**: 1977 carve-outs, 1982 abandonment
  (verified), 1983 goodwill appendix's "unleveraged net tangible assets" denominator,
  restated 2003/2010/2014/2019. Two denominators, two eras, currently unnamed in v4.
- **The Q3 guardrail is stated harder than the shelf**: the source hedge "with few
  exceptions" (1980) is dropped in [E2-17]'s quote; the 1981 "managerial superstars"
  category and Talk 02's "load up… not that hard to identify" (same talk as [E3-39]) name a
  second exception class.
- **Q6 gradualism is missing its counter-trigger**: 1979 ("even more serious mistake in not
  selling"), the 2020 airline exit, BPL 1966 "constant evaluation … absolutely essential."
- **Fraud tells from Talk 08** (smooth reported growth; falling cash-tax rate vs pretax) —
  computable from the series v4 already requires; the strongest actionable omission.
- **Structural**: no ledger row cites any meeting after 2009; the manager standard quotes
  2017/2025 meeting lines without ids.
- **Unresolved corpus-internal conflicts to row as open questions, not defects**: trim vs
  no-trim (2020 vs 2024); long bond vs T-bill as the yardstick (2000 letter vs 2021 meeting);
  no-macro vs the 1969 wind-up and 2003 FX position.

**Standard reminder:** none of the above is a confirmed defect until re-verified; several
"contradictions" may downgrade to DRIFT on context. Amendments happen once, after all six
partitions are triaged.

## INTERIM LOG 2, same day — fifth partition received (letters 1985–1999, 30 findings)

New verified citations (read in place, in context):

8. `1987 Letter.txt:856-869` ✓ — the permanent-holdings passage sits **directly after
   [E2-28]** and exempts three named marketable stocks from sell trigger 1 ("we would not
   sell even though they became far overpriced"). **And it carries a qualifier the agent's
   quote cut short**: *"To that, I will add one qualifier: These stocks are held by our
   insurance companies and we would, if absolutely necessary, sell portions…"* — so the
   permanent class itself has a solvency carve-out. Q6's scope warning is partly falsified;
   the correct structure is: E2-28's three conditions + an optional PERMANENT designation
   exempting trigger 1 (not trigger "solvency") — which, noted for the record, is exactly
   how `PORTFOLIO.md` already treats the anchor holdings.

9. `1991 Letter.txt:274-289` ✓ — **the single most valuable verification of the sweep,
   because it RESOLVES three open tensions at once rather than adding one:**
   - *"The existence of all three conditions will be demonstrated by a company's ability to
     regularly price its product or service aggressively and thereby to earn high rates of
     return on capital"* — the corpus's own **single-company moat test**. The mandatory
     competitor row is v4's convention on top of it, and must be relabelled as such.
   - *"franchises can tolerate mis-management… **And a business, unlike a franchise, can be
     killed by poor management.**"* — the franchise/business boundary IS the Q3 weight rule
     in its original form: franchise → Q3 overlay; "a business" → Q3 gate. The
     daily-execution determinant added 2026-08-27 is this 1991 doctrine rediscovered; it
     should be re-sourced to this passage, and [E5-18] read as its 2009 restatement.
   - *"a company may maintain its status as the low-cost operator for a much longer time"*
     with superior management — the low-cost moat class the 1982-letter finding flagged as
     missing from Q2, stated here inside the franchise taxonomy itself.

Partition 5's sharpest unverified items queued for triage: the 1992/1994 DCF passages ("the
only logical way"), the 1993 after-tax purchasing-power risk floor, look-through earnings
(eleven consecutive letters), cost-of-float for insurers, the LIFO working-capital carve-out
inside [E2-23] itself, and the 1985 guardrail parenthetical dropped from [E2-37]'s quote.

Outstanding: meetings 1994–2009 (final partition). Then: one combined triage, one amendment
pass, one commit.

---

# VERDICT, 2026-08-28 — all six partitions received: **FAIL, as pre-registered.**

**The pre-registered FAIL condition is met: confirmed contradictions exist with no
corpus-internal resolution.** ~190 findings across six partitions; the citations that decide
the verdict were re-read by me, in context, before this section was written. This is the
test working — a framework built in weeks against a 60-year corpus, tested adversarially for
the first time, should fail somewhere, and now it is known where.

## The decisive, personally-verified finding: v4's Q5 rate machinery is wrong

Three citations, all verified verbatim today:

1. **`2007 Annual Meeting.txt:773-777`** — the source of **[E4-21]**, v4's authority for "no
   hurdle floor." The passage immediately above v4's quoted fragment states the floor: *"if
   government bond rates were 2 percent, we're not going to buy a business to earn 3 or
   3 1/2 percent expectancy… We'd rather sit around and wait."* And v4's ellipsis in the
   Munger quote removed: *"The concept of a hurdle rate makes nothing but sense… **not that
   we don't have one, in a sense** — is it doesn't work as well as a system of comparing
   things."* **v4's citation for abolishing the floor is the passage that states it.**
2. **`2003 Annual Meeting.txt:1223-1229`** — *"the 10 percent we mention… **that's the
   figure we quit on**… whether short rates are 6 percent or whether short rates are 1
   percent… **we still want a threshold return of 10 percent.**"* Munger grounds it: a guess
   at **future opportunity cost**, revisable if rates settled permanently lower — not a
   spread over today's sovereign. Same 10% as the 1994 meeting (**[E3-13]**'s source), the
   2002 letter (verified), and Munger's 2004 Wesco letter (adopted verbatim).
3. **`1996 Annual Meeting.txt:623-625`** — adding risk premia to the discount rate is
   *"mathematical gibberish… use the government bond rate"* and buy at *"a significant
   discount."* Confirmed independently by 1997:1167, 1998:1547-1549, 1999:1065.

**The corpus's actual structure, now legible across four sources and three decades:**
- **Discount at the government bond rate. No per-name risk premia — that is the named error.**
- **Certainty is handled by the understanding gate (go/no-go) and by the discount to value
  demanded at the end — not by the rate.**
- **A floor exists** — ~10% pre-tax expectancy, the stated "quit point," grounded in guessed
  future opportunity cost, held even when the sovereign is far below it.
- **Above the floor, rank** — [E4-21]'s comparison system operates *on top of* the floor,
  not instead of it.

v4 inverted the certainty mechanism (built a +3% "certainty spread" from [E3-13]'s 10−7
arithmetic and directed *wider* spreads for less certainty) and denied the floor outright.
**Both are confirmed against the shelf.**

## Other confirmed defects (verified citations noted; the rest triaged from convergent 2+
agent findings, to be re-verified during the amendment pass)

1. **v4's negative claims are its systematic failure mode.** "There is no leverage ratio…
   the corpus does not supply one" (falsified: 2012 coverage definition ✓, BPL 25% ceiling,
   1982-84 "little or no debt" screen, 1989 zip-up-your-wallet coverage test); "the corpus
   leaves it unquantified"; "not one discounted cash flow in it" (falsified: 1991 worked DCF,
   1992/1994 "only logical way," 1999 meeting endorsement, OM definition); "the corpus
   supplies one number [sizing]" (falsified: 40% + "five to ten" + "three… is more than you
   need" + Munger's 90%). `check_framework.py` cannot catch a false claim of absence, because
   such claims cite nothing. **Amendment rule: v4 may assert corpus absence only with a
   Test-D-style sweep behind it, and each such claim gets flagged as an ABSENCE CLAIM.**
2. **The [E2-28]/permanent-holdings structure at Q6** (`1987:856-869` ✓): the three-condition
   hold rule, plus an optional PERMANENT designation exempting sell-trigger 1, with its own
   solvency qualifier. Q6's scope warning rewritten accordingly; the 1979 "more serious
   mistake in not selling," the 2020 airline exit, and BPL's continuous re-ranking add the
   missing crystallized-view counter-trigger.
3. **The 1991 franchise/business boundary** (`1991:274-289` ✓) re-sources the Q3 weight rule
   (franchise → overlay; "a business… can be killed by poor management" → gate), supplies the
   corpus's own single-company moat test (aggressive pricing + high returns on capital —
   the competitor row is a v4 CONVENTION on top, and must be relabelled), and adds the
   low-cost-operator moat class.
4. **The guardrail is over-hardened**: the 1980 hedge "with few exceptions" (✓) and the 1985
   parenthetical are cut from v4's quotes; the 1981 "managerial superstars" category, SAFECO
   1978, Wells Fargo 1990-95 ("if we hadn't gone a little further than just looking at
   numbers"), and the 2000 castle-and-knight passage give management a constitutive role v4
   currently forbids a run from recording. The binary (integrity veto) survives untouched —
   no partition found a contradiction of it.
5. **Owner earnings, (c) and the window**: the corpus supplies a *default* for (c)
   (depreciation as proxy — 1997/1998/2003 meetings, 1986 appendix "quite close," 1989 "95%
   of American businesses") **and** the named exception class (capital-intensive: railroads
   ">60% of capex," 2015-16 ✓); the LIFO/flat-volume working-capital carve-out sits inside
   [E2-23] itself; look-through earnings (eleven consecutive letters) corrects OCF-based OE
   for investee-heavy names; and the five-year rolling window with the aggregate-industry
   benchmark ("red lights should start flashing," 1983-84 ×3) replaces part of the window
   CONVENTION with corpus text.
6. **Missing flags with corpus warrant** (the Q3 checklist is not closed at four): EBITDA /
   adjusted earnings (12+ statements, fraud base-rate named); restructuring-charge serialism;
   metric-switching after bad years (1982 arrow/bullseye ✓); dividend funded by issuance;
   management targeting the stock price; self-graded-exam businesses; Talk 08's smooth-growth
   and falling-cash-tax-rate tells; guidance-vs-outturn scoring (1995 "nine cases out of
   ten" + the named remedy).
7. **Open-question rows (unresolved corpus-internal tensions, not v4 defects)**: trim vs
   never-trim (2020 vs 1997-98 ✓-adjacent and 2024); long bond vs T-bill yardstick; no-macro
   vs the 1969 wind-up, 1997 zeros, 2003 FX; the 1993 probability-weighted diversified mode
   vs stop-at-first-non-IN; E5-16's binary vs Munger 1995:1345.

## What checked out clean

[E4-16], [E4-17], [E4-18], [E4-19], [E3-23], [E3-27], [E3-32], [E3-34] verified in full
context with no drift; Q1's ten-year horizon confirmed at 2006:215 against the 2013 letter's
five-year phrasing (both live; state as "five to ten"); Q6's silence on tax as a hold reason
supported at 1998:859; **the integrity binary and the four-verdict structure survived all six
partitions without a contradiction.**

## Disposition

**v4 as written is not corpus-faithful in the places named above. The amendment pass — v4.1 —
executes from this section, one pass, with every new row line-verified, and
`check_framework.py` green throughout.** The six-question skeleton, the verdict system, the
hard sequence, the owner-earnings definition, the integrity veto, and the honest-record
discipline all survived. What failed was, overwhelmingly, v4's *negative* claims about its
own corpus and a set of quotes cut too short — the exact failure mode the pre-registration
predicted ("no findings is suspect") and the reason Test D existed.