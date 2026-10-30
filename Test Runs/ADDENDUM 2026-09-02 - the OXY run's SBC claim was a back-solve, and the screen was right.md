# ADDENDUM — 2026-09-02
## The OXY run's "the screen over-subtracts SBC" claim was MY back-solve, not a screen defect

**Operator rule 6: violations found later are corrected in an addendum, never by editing
history.** This corrects `Test Runs/2026-09-01 Run - OXY Occidental Petroleum.md` (committed
0c50287, folded in at 074c099) without touching it.

**Raised by the operator as a QUERY, correctly, before it entered the record as a confirmed
defect. The answer is (a): my own intermediate working. The screen was right and I was wrong.**

---

## WHAT THE RUN SAID

Two places in the committed run file assert a defect in the screen's stock-compensation input:

> *"(FIRST CORRECTION TO THE SCREEN: the SBC column is wrong. The FY2025 10-K's stock-based
> incentive note states the expense as **$234M, $213M and $203M** for 2025, 2024 and 2023 —
> not $629M, $423M and $443M. The screen is subtracting something else under that label…)"*

and, in the self-audit's corrections table:

> *"nine-year SBC of 443 / 423 / 629 (2023/24/25) → $203M / $213M / $234M per Note 14 of the
> FY2025 10-K"*

**Both are withdrawn.**

## WHERE $629 / $423 / $443 ACTUALLY CAME FROM

**They are residuals I computed myself.** The brief gave me the nine-year series as an output
(`1,247 · 2,514 · 812 · 1,218 · 7,277 · 11,970 · 5,595 · 3,998 · 3,476`) but not the
construction that produced it. I located the construction by back-solving from XBRL, assuming a
**two-term** deduction — cash capex plus SBC — and solving for the remainder:

```
X = OCF − cash capex − screen value
FY2025:  10,532 − 6,427 − 3,476 = 629
FY2024:  11,439 − 7,018 − 3,998 = 423
FY2023:  12,308 − 6,270 − 5,595 = 443
```

I then wrote `sbc = [..., 443, 423, 629]  # screen's implied subtraction` in
`Test Runs/_research 2026-09-01 OXY/calc.py`, **labelled the residual "SBC", and reported the
label as a finding.** The label was my inference. It was never read off anything.

## THE DECOMPOSITION, WHICH SETTLES IT

`Screens/floor_screen.py` line 432–433 builds owner earnings as
`OCF − SBC − capital_acquired`, and `capital_acquired()` is **cash capex PLUS finance-lease
additions** on `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`. **Three terms, not
two.** My residual is therefore SBC *plus* the lease term. From OXY's own XBRL
(`companyfacts`, CIK 0000797468):

| FY | my back-solved "SBC" | **filed SBC** (`AllocatedShareBasedCompensationExpense`) | **finance-lease additions** (`RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`) | sum |
|---|---|---|---|---|
| 2025 | 629 | **234** | **395** | **629** — exact |
| 2024 | 423 | 213 | 195 | 408 |
| 2023 | 443 | 203 | 226 | 429 |

**FY2025 reconciles to the dollar.** The $15M residuals in 2024 and 2023 are a capex-vintage
difference — the screen resolves capex from the latest accession, and those two years were
restated by the OxyChem discontinued-operations reclassification. They are not SBC.

**`ShareBasedCompensation` is ABSENT for this filer; `AllocatedShareBasedCompensationExpense`
resolves at 234 / 213 / 203, which is what Note 14 of the FY2025 10-K says.** The screen reads
the correct element and gets the correct number. There is no defect, and possibility (c) —
a different element the screen *should* be using — is refused.

## THE PART WORTH KEEPING

**The finance-lease term is exactly what the ADDENDUM of 2026-09-01 added to `capital_acquired`
after the COST and HD runs.** So the "over-subtraction" I reported as an error is a **correction
this project had already made and published**, and my back-solve mistook it for a mislabelled
input because I did not read the tool I was auditing.

**OXY is a substantial member of the class that addendum identified.** Finance-lease additions
of **$395M in 2025** against cash capex of $6,427M is **6.1%**, rising — $226M, $195M, $395M
across 2023–25, and $85M in 2022. It sits above the 5% line that addendum used to size the
affected population.

## WHAT THIS CHANGES IN THE OXY RUN, AND WHAT IT DOES NOT

**No verdict moves and no band is re-derived.**

- The run's own owner-earnings arithmetic **never used the disputed figures.** It was rebuilt
  from the filings at continuing-operations OCF less the **filed** SBC of $234M less the
  disclosed (c) judgment of $7,500M. The residuals appear only in the Stage 0 table that
  reproduces and locates the screen's construction.
- **(c) = $7,500M is unaffected**, and in fact the finding *strengthens the direction it was
  set in*: $395M a year of capital acquired outside the cash capex line is $395M the volume-flat
  anchor of $5,700M did not contain. The gap between the volume-flat anchor and the judgment
  narrows by about a sixth.
- The Q2 OUT and the Q4 OUT rest on the commodity doctrine, the reserve tables and the [E4-20]
  classification. **Nothing here touches them.**
- **The corrections table in the committed self-audit now has three valid rows, not four.** The
  capex/D&A correction (0.85× against the screen's 0.77×) and the dividend correction ($0.79 →
  $0.01, not $0.11) stand and were separately verified. **The SBC row is withdrawn.**

## THE LESSON, STATED AGAINST MYSELF

The run's own Q3 fired a flag on Occidental for a headline metric that deletes a real cash
item, and its register entry claims credit for refusing its own first-pass reading when the
competitor row refuted it. **In the same document I published a residual as if it were a read
figure.** The two are the same error in opposite directions: a number that was inferred,
presented as a number that was observed.

**The corpus already has the rule and this run had already quoted it: [E3-27] — *"There are no
answers in the financial statements. There are guidelines to enable you to figure out the
answer."*** And operator rule 8: *tools fetch and compute and are forbidden to conclude.* **A
back-solve against a tool is not a reading of the tool. The one-line fix is to open
`floor_screen.py` before asserting what it does** — the same discipline operator rule 4 imposes
on filings, applied to the project's own code.

*"you must not fool yourself, and you're the easiest person to fool"* **[E3-41]**.

## WHAT THE OPERATOR SHOULD RECORD

**QUERIED → RESOLVED as (a).** My own intermediate working, corrected here. **No defect in
`Screens/floor_screen.py`. No change to the reading list's treatment of the screen. No tool
fix required.** The three other corrections carried by the OXY run are unaffected.
