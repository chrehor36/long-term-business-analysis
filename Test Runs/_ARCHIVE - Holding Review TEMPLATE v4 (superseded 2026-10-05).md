# HOLDING REVIEW - [TICKER] ([Company])
**Date:** YYYY-MM-DD · **Governing document:** `Framework/THE HOLDINGS FRAMEWORK.md`
**Occasioned by:** annual report / proxy statement / tripwire / price alert / replacement cleared / first review under the holdings framework

Copy to `Test Runs/YYYY-MM-DD Holding Review - TICKER Company.md` and fill top to bottom.
**All five hold questions are answered.** None closes the file early.

---
## BEFORE ANY QUESTION

**1. Position.** Shares ____ · cost ____ · account: **taxable / tax-sheltered** · current price ____ (date, source, aggregator flagged)

**2. Designation.** [ ] SECURITY (default) · [ ] PERMANENT, designated in writing on ____ in ____ **[E2-39, E1-02]**

**3. The purchase thesis.** Run file that bought it: ____ · what it said at Q2: ____ · at Q4: ____ · exit metric set before entry **[E1-02]**: ____
[ ] No thesis on file (position predates the framework): recorded, and H1 is judged against the current purchase run.

**4. The filing was read** (operator rule 4). Documents, dates, accession numbers: ____ · one figure cross-checked against the filed statement: ____

**5. Tripwires set at the last review, and whether any fired:** ____

---
## H1 - IS THE BUSINESS'S ECONOMIC POSITION INTACT? [E4-17]

- Current purchase-framework Q2 verdict and its run file: ____
- Competitor row, pricing power **[E2-44]**, durability **[E4-04]**: ____
- Physical volume against price **[E4-55]**: ____
- Aberrational cycle or permanent slip **[E3-30]**: ____
- Key-person dependence **[E4-23]**: ____
- **Was the business judged a franchise at purchase?** [ ] yes, and the view has / has not changed · [ ] no, held for its returns (H2 carries the weight)
- **Has the view crystallized [E2-40]?** ____

**VERDICT: IN / OUT / UNRESEARCHED (document: ____, due ____) / UNKNOWABLE**

---
## H2 - IS THE PROSPECTIVE RETURN ON EQUITY CAPITAL SATISFACTORY? [E2-28]

- Return on capital employed, and why this measure rather than raw return on equity **[E2-01]**: ____
- Owner earnings on the purchase framework's default window, both (c) ends: ____
- Retention test, rolling five years, where earnings are retained **[E3-54]**: ____
- Forward view: is any decline under way, and is it aberrational **[E3-30]**: ____

**VERDICT: IN / OUT / UNRESEARCHED (document: ____, due ____) / UNKNOWABLE**

---
## H3 - IS MANAGEMENT COMPETENT AND HONEST? [E2-28]

- Honesty: the purchase framework's Q3 flags on the latest proxy and annual report: ____
- Capital allocation, and loss of focus **[E3-40]**: ____
- Share issuance **[E5-15]**: ____
- If capital is being misallocated and will continue: exit, do not engage **[E4-24]**: ____

**VERDICT: IN / OUT (honesty / capital allocation) / UNRESEARCHED (document: ____, due ____) / UNKNOWABLE**

---
## H4 - DOES THE MARKET NOT OVERVALUE THE BUSINESS? [E2-28]

[ ] PERMANENT: H4 skipped **[E2-39]**.

- Sovereign for the earnings currency, issuing authority, dated **[E4-21]**: ____
- Growth the record supports, against the base rate **[E4-35]** and the bound **[E4-44]**: ____
- **Value range** (a range, never a point **[E4-25]**): ____ to ____ per share
- Price against the range: [ ] above the whole range · [ ] inside · [ ] below
- *The ~10% floor [E4-28] is a buying rule and is not applied here.*

**VERDICT: IN (inside or below) / OUT (above the whole range) / UNRESEARCHED / UNKNOWABLE**

---
## H5 - IS HOLDING STILL THE BEST USE OF THIS MONEY? [E2-28]

- Named replacement that has cleared the purchase framework, with its run file: ____ · [ ] none
- Switching bar for this account: tax **[E2-46, E3-64]** ____ · friction **[E3-67]** ____ · material gap **[E4-45]** ____
- Tax never vetoes a sale H1 to H4 require **[E3-64]**.

**VERDICT: IN (no replacement clears) / OUT (replacement ____ clears the bar)**

---
## OUTCOME

| H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|
| | | | | |

**OUTCOME: HOLD / SELL REVIEW / SELL** · **ADDS: BARRED / OPEN** (open only if a current purchase-framework run clears all six questions at the add price)

- If SELL REVIEW: the question, the document that settles it, and its due date. It concludes HOLD or SELL when read and is not renewed without new evidence **[E2-40]**.
- If SELL: the whole position, and the reason in one sentence.

**Reasons NOT used** (confirm none drove the outcome): [ ] the price rose **[E2-28]** · [ ] held a long time **[E2-28]** · [ ] position grew large **[E5-14]** · [ ] a wish to act **[E3-15, E3-35]** · [ ] the purchase framework would not buy it today

---
## TRIPWIRES FOR THE NEXT REVIEW, set now, before the act [E1-02]

- H1: ____
- H2: ____
- H3: ____
- H4: price band ____ (COMPUTATION — NOT A CLEARANCE)
- Next scheduled document: ____ due ____

---
## SELF-AUDIT
- [ ] All five questions answered; each non-IN verdict names its document or states why none exists
- [ ] H1 asked separately from H2; a purchase-framework Q2 of OUT treated as evidence, not as the H1 verdict
- [ ] The floor was not applied at H4; the range was built against the sovereign
- [ ] Any add routed to the purchase framework
- [ ] Every judgment cited by ledger id (the division of labor in `Framework/OPERATOR-PROTOCOL.md`)
- [ ] `python tools/check_framework.py` PASS
