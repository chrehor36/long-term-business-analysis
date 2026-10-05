# RULING CASE — 2026-10-05 — should v5 replace v4.1? For the operator's approval.
## Presented under PRIME RULE 5. v4.1 governs every run and review until the operator rules. Nothing below is adopted by being written.

**What was asked.** On 2026-10-03 the operator said the annual meetings are the conglomeration of every lesson Buffett
and Munger learned, and asked for a framework built from them alone, as an intended replacement for v4.1, by a blind
read, to be adopted only on a written comparison. The case, the pre-registration, the read, the synthesis, the
reconciliation and the five tests are done and recorded; this document puts the decision.

## 1. What was built
- `principle_ledger_v5.csv`: 4,279 rows from the 32 meetings, the letters they discuss and the signed report sections,
  every row verifying against its source. Calibration: the blind read independently re-found 72 of the 78 meeting rows
  v4.1 already used.
- `Framework/v5/DRAFT - THE FRAMEWORK v5.md`: a preamble of foundations, a standing rule, Q1 to Q12 in the speakers'
  own order, a closing note; 1,384 ids; passes the acceptance test.
- `Framework/v5/DRAFT - THE HOLDINGS FRAMEWORK v5.md`: six hold questions; 183 ids; passes the acceptance test.

## 2. What the five pre-registered tests found
| test | result | where |
|---|---|---|
| acceptance test on the drafts | PASS, both | `tools/check_framework.py --also` |
| A', reproducibility | PASS on every STOP and both boxes (HRB, TJX; two analysts each); two weighings diverged on TJX | `Framework/v5/TESTS - A prime, B prime and the regression - results.md` |
| B', blind falsification | PASS, zero false passes on the five sealed cases; acceptance half untestable blind, as under v4.1 | same |
| regression | seven names, no name IN under either framework, every difference explained; one real change (ASML: v4.1 understood and sold on price, v5 TOO HARD at Q1) | same |
| reconciliation and calibration | 215 v4.1 rules: 130 reproduced, 52 partly, 28 absent, 5 contradicted; 87 new in v5. **Hypothesis FAILS narrowly on one rule** by the operator's ruling on E4-13 (accounting suspicion is a STOP in the meetings, only a prompt to read in v4.1). Holdings: 77 rules, 40 reproduced, 25 partly, 10 absent, 2 contradicted (PERMANENT); 34 new | `Framework/v5/RECONCILIATION - v5 against v4.1.md` and part 4 |

**Read plainly:** v5 can be applied, two analysts reproduce it at every stop, it refuses what it should refuse, and on
seven live names it reaches the same boxes as v4.1 or a more cautious one. The meetings reproduce or partly reproduce
182 of 215 v4.1 rules and add 87. They contradict one load-bearing rule, and the contradiction is a point in v5's
favour: on suspicion about the accounts, the meetings stop.

## 3. What the meetings do not carry, and what adopting v5 would cost
In the form of `Framework/INVENTIONS - deleted and why.md`: each item stated with its cost, so that if v5 is adopted the
loss is written down, not discovered later.
1. **A pre-committed "what would prove me wrong" metric and a sell rule written at purchase** (v4.1 Q6). ABSENT: no
   instance found in the v5 ledger. v4.1 rests them on one row, [E1-02], about measuring performance. **Cost:** the
   discipline that made every v4.1 run name its own falsifier before buying, the thing that reopened CRM and closed NKE.
   The meetings carry the analyst's habits (write down the contrary evidence, M1997-127; what do I not know, M1999-129)
   and after-purchase triggers (M2009-040), not the pre-commitment. **If adopted:** carry it as a CONVENTION in the
   foundations, confessed as ours with [E1-02] as its nearest corpus.
2. **The ten percent floor as a number** (v4.1 Q5). PARTLY: the meetings state it in 1994, 2002 and 2003, call it
   arbitrary, qualify it by rate conditions, replace it with "significantly higher than the bond" in 2007 and never
   restate it after 2011. v5 writes no number. **Cost:** every v4.1 gate-clearer was "quit on at the floor" by a number;
   under v5 the same names close OUT or TOO HARD at Q7 on a judgment two analysts may not share (TJX's Q7 in Test A'
   agreed; Visa's run said the growth input decides everything). **If adopted:** either carry "about ten percent" as a
   CONVENTION naming M1994-004, M2003-149 and M2007-095 as its history, or accept the judgment and the wider spread.
3. **The UNRESEARCHED verdict** (a document exists and has not been read). ABSENT: the rows have three boxes. v4.1
   already confesses it as a CONVENTION. **Cost:** none new; v5's Part I says the same.
4. **The weight gate's bank-leverage factor, "no price compensates", the return-on-equity test on the manager, the
   five-year window as a rule, Q4 as a gate** (the other load-bearing PARTLY rules). The meetings carry each one's
   substance and not its edge. **If adopted:** each named part becomes a CONVENTION or is dropped with this list as the
   record.
5. **A strict stop at every question.** v5 stops at Q1, Q2, Q4 (on confusion), Q5 (on integrity), Q7 and Q8, and weighs
   Q3, Q6, Q9 and Q10. **Cost:** a run can carry a bad capital-needs or use-of-money reading to Q7; **gain:** the
   meetings' own practice is weighing there, and the regression showed no name slipping through.

## 4. What v5 adds that v4.1 lacks (from the reconciliation's NEW IN V5, the ones that change verdicts)
The accounting-confusion STOP at Q4; Q8 as a separate opportunity-cost STOP with "more of what I already own" and the
company's own stock; the use of money (retention, buybacks, issuance, pay, boards, owners) as its own question with 709
rows behind it; the foundations (a share is a business, the market serves, no macro, who is paid to tell you,
temperament, the index for the non-professional); the standing rule of the buyer's own ruin-avoidance; sizing and the
fat pitch; the newspaper test; three boxes instead of four verdicts; the castle tests set out one by one with their
rows across thirty years.

## 5. What the tests found wrong in the drafts (owed before or at adoption)
From fifteen runs and the reconciliation, the gaps that showed in use: (a) Q1 and Q2 overlap on rapid change, so a name
can close at Q1 TOO HARD, Q1 OUT or Q2 TOO HARD; the routing must be fixed in one sentence; (b) Q7 has no rule for the
growth input or the horizon, so a wide range can close OUT or TOO HARD; (c) the holdings draft's Q5 needs the portfolio
and its Q6 does not say whether a purchase TOO HARD on a held name is a recognised mistake; (d) adds to a TOO HARD name;
(e) no named outcomes in the holdings draft, where four of six held names reached what v4 calls SELL REVIEW; (f) the
bank door against the bank exclusion for a very large bank; (g) a holding company understood by its parts or as a whole,
and equity-method income at Q3, Q4 and Q7; (h) for point-in-time tests, a rule barring rows dated after the anchor;
(i) `tools/run.py` prints v4 ids and the floor into every run; (j) two weighings (Q4's make-the-numbers habit, Q6's
buyback with no price limit) need a stated test.

## 6. Findings against v4.1 regardless
Corrected 2026-10-04 by addendum: Bar 1's paraphrase wearing a citation (now E5-63), two unlabelled conventions. Owed
as a PRIME RULE 5 case, filed today: the PERMANENT designation (withdrawn by its author in 2016, [E5-64]) and H2's
retention test (corrected by its author in 2009, [E5-65]). Three holdings-framework label defects in the same case.

## 7. The options
**A. Adopt v5 now, as drafted.** Both drafts become GOVERNING; v4.1 to `Framework/ARCHIVE - v4.x (superseded
2026-10-05)/`; the items in section 3 confessed as CONVENTIONS where the operator wants them kept; the gaps in section 5
fixed by addendum as they bite. Fastest; the gaps go live.

**B. Adopt v5 after one correction pass.** Fix section 5 (a) to (j) in the drafts first (one session), re-run the
acceptance test and one reproducibility pair, then adopt as in A. The pre-registered tests stay valid because none of
the fixes changes a STOP's substance; the fixes are routing, inputs and the holdings outcomes. **Recommended.** The
operator asked for a replacement; the tests say v5 is applicable, reproducible and refuses what it should; the
reconciliation says what it costs, and section 3 lets the operator keep the two things that cost most (the
pre-committed falsifier, the floor's number) as confessed conventions.

**C. Keep v4.1 and import.** v4.1 stays governing; the accounting-suspicion STOP, Q8's comparison, the use-of-money
question, the foundations and the PERMANENT withdrawal are added to v4.1 by written cases. Lowest risk to the live
process; the meetings' structure (the order the speakers themselves give, the weighings, the three boxes) is not taken
up, and the hypothesis the read was built to test is left at "failed narrowly".

**D. Refuse v5.** Everything stays as a test record. The reconciliation's findings against v4.1 are still corrected.

## 8. What adoption changes, if approved (A or B)
`Framework/THE FRAMEWORK v5.md` and `Framework/THE HOLDINGS FRAMEWORK v5.md` written from the drafts; GOVERNING in
`CLAUDE.md` and `Framework/README.md`; added to `DOCS` in `tools/check_framework.py`; `principle_ledger_v5.csv` published
and cited; the v4 templates copied to v5 templates with the run form from `Framework/v5/tests/PROTOCOL ...md`;
`Test Runs/README - which run files are in force.md` given a v5 cutoff date (runs before it bind under v4.1);
`PORTFOLIO.md`'s header; `Framework/OPERATOR-PROTOCOL.md`'s tool table; v4.1 and its holdings framework to an archive
folder, never applied again; the honest record (operator rule 7) unchanged: **the market-beating claim stays UNPROVEN
under v5 exactly as under v4.1**, and no result of the read bears on it.

# WHAT THE OPERATOR IS ASKED TO DECIDE
1. **A, B, C or D.**
2. If A or B: which of section 3's items are kept as CONVENTIONS (the pre-committed falsifier; the floor's number; the
   other PARTLY edges), and which are dropped with their cost recorded.
3. The PRIME RULE 5 case of the same date on PERMANENT and the retention test, which stands whatever is chosen here.
