# ADDENDUM — 2026-09-02 (third)
## The most-repeated defect in this project is now tooled, and the audit found twelve more

**COMPUTATION — NOT A CLEARANCE** (operator rule 3). Nothing here opens or closes a question
on any business. It decides which names need their market cap rebuilt by hand before a run
spends tokens on them.

---

## THE DEFECT, AND WHY IT KEPT HAPPENING

A market cap built on a share count that `companyfacts` could not supply has now been found
**five separate times, every one of them by a full run rather than by a screen**:

| | found | what the screen used |
|---|---|---|
| **LEVI** | 2026-08-31 | 37,602,843 — **pre-IPO, pre-split**, dated 2019-01-30. True count 384,850,562. **Wrong by 10.23x**; the "26.3% statute yield" was noise. |
| **NKE** | 2026-09-02 | a 2015 count, 11.1 years stale |
| **DKS** | 2026-09-02 | 93,768,978 from 2011-01-29, 15.6 years stale |
| **PINS** | 2026-09-02 | 127,371,000 from 2019-03-31 — **the pre-IPO balance sheet, three weeks before listing**. Cap 4.06x too small; the name sat in tier 1 on a 4.98% yield that is really 1.23%. |
| **BRK** | standing | an A/B artifact returning a **$473M cap and a 4,683% yield** |

**The mechanism is identical every time and it is not a filer error.** SEC `companyfacts`
**drops dimensioned facts.** The moment a filer tags its cover page by share class — which
every multi-class filer must — the undimensioned `dei:EntityCommonStockSharesOutstanding` row
stops advancing, and the fallback lands on whatever that filer last reported *without*
dimensions. For a company that went multi-class at its IPO, that is a pre-IPO number.

Five discoveries by five expensive runs is four too many. `Screens/cover_shares.py` reads the
rendered cover page (R1.htm), which carries every dimensioned value with its class label.

**It reproduced both hand-reads exactly** — DKS 65,931,904 + 23,570,633 and PINS 492,198,008
+ 74,115,019 — and reproduced the LEVI run's 384,850,562 without being told the answer.

### What the tool refuses to do, deliberately

**It does not sum the classes into a single number for a caller to divide by.** Whether two
classes are economically equivalent is a **judgment from the charter, not arithmetic**:
Berkshire's A converts to 1,500 B; **Ford's Class B does not trade at all**; a tracking stock
may not share in earnings. The tool prints the classes, prints the arithmetic sum **labelled
as not a share count**, and tells the reader to read the filing. Operator rule 8: it fetches
and computes and is forbidden to conclude.

**Berkshire is the case that proves the refusal matters.** A 488,450 + B 1,408,035,161:

| construction | count |
|---|---:|
| arithmetic sum — **wrong** | 1,408,523,611 |
| **B-equivalent, A × 1,500 + B — correct** | **2,140,710,161** |

**The arithmetic sum understates Berkshire by 1.52x.** A tool that had helpfully added them
would have replaced a 4,683% error with a 52% one and looked like it worked.

---

## TWO DEFECTS FOUND IN THE TOOL WHILE BUILDING IT, BOTH BY TESTING IT ON HARD CASES

**1. The label is not spelled the same by every renderer.** DKS and PINS emit *"Entity Common
Stock, Shares Outstanding"*; **NIKE emits it without the comma.** A `startswith()` on the
comma form returned **nothing at all** for a filer with two classes and 1.48bn shares — a
silent zero, on exactly the class of name the tool exists to catch. Now matched with an
optional comma.

**2. The renderer scales, and Alphabet proves it.** GOOGL's cover reported Class A as
**5,868** for a company with 5.868 **billion** Class A shares, because its header says
*"shares in Millions"*. Nike and Dick's carry no such header and report in units. **Assuming
units understates by 1,000,000x; assuming millions overstates by the same.** The scale is now
read off the page. This project's own screener README already records a units bug of exactly
this shape — a double 1e6 division that once produced "509 passes".

---

## THE AUDIT: 12 OF 69 QUEUE NAMES NEED THEIR CAP REBUILT

Run across the operator's tier 1, tier 2, tier 3 and Mini Berk lists.

### The live one that matters

**FLNC (Fluence Energy) — the screen count is 3.58x too small.** Screen 51,499,195; cover
**Class A 143,163,588 + Class B-1 41,432,781 = 184,596,369.** FLNC is in **tier 3** of the
operator's queue. Its yield as screened is **3.58x too high**, which is the LEVI mechanism
repeating on a name that has not yet been read. **Whether the B-1 shares are economically
equivalent to the A is a charter question the run must settle** — this note does not settle
it.

**BE (Bloom Energy) — 1.04x.** Small, and recorded rather than ignored.

### Ten names the screen could not count at all, now countable

**BRK-B · BRK-A · BAM · GHC · PINS · COKE · SHOP · PAY · ACMR · DKS.** Each returned no share
count, so each was correctly returned unpriced rather than mis-priced — the guard worked.
**The cover supplies the answer for all ten**, and **BRK-A/BRK-B is the specific blocker the
Mini Berk track has carried since 2026-09-01.**

**That blocker is now removed.** Berkshire's economic count is **2,140,710,161 B-equivalent
shares**, from the 10-Q cover of 2026-08-10 (accession 0001193125-26-341032, period
2026-06-30). The $473M cap and 4,683% yield are explained and disposed of.

### What the audit did NOT find, which is worth as much

**Fifty-seven of sixty-nine agree to within 2%**, including every single-class filer tested.
The defect is real, it is confined to multi-class filers and recent listings, and it is not
a general failure of the data. **Saying so is part of the practice** — an audit that only
reports its hits is not an audit.

---

## WHAT THIS CHANGES IN THE QUEUE

- **FLNC** is flagged for a hand-built cap before it is read.
- **BRK-B and BRK-A are unblocked** on the Stage 0 share-class test. The insurer sector
  method already covers the rest, and BRK-B is still deliberately run **last** — testing a
  method first on the case that generated it is the error **[E4-26]** exists to prevent.
- **PINS and DKS** are already re-priced by hand in the first addendum of today; this
  confirms both counts independently.
- **BAM stays out of scope** for the sector method regardless of its share count, for the
  reason already recorded: it is an asset manager with consolidated funds, a different
  perimeter problem.

---

## FLNC RESOLVED — it is an Up-C, and the screen priced it on the FOUNDERS' VOTING SHARES

The audit above flagged FLNC and said *"whether the B-1 shares are economically equivalent
to the A is a charter question the run must settle - this note does not settle it."* It is
settled here, because the answer turned out to be a Stage 0 fact rather than a judgment.

**Fluence Energy is an Up-C.** From the FY2025 10-K (filed 2025-11-25, period 2025-09-30,
`flnc-20250930.htm`):

> *"Fluence Energy, Inc. operates and controls all the business and affairs of Fluence
> Energy, LLC and its direct and indirect subsidiaries. As a result, Fluence Energy, Inc.
> consolidates Fluence Energy, LLC and records a **non-controlling interest** in its
> consolidated financial statements for the **economic interest in Fluence Energy, LLC held
> by the Founders.**"*

And the same filing's cover: *"As of November 20, 2025, the registrant had **131,369,447
shares of Class A** common stock outstanding and **51,499,195 shares of Class B-1** common
stock outstanding."*

**The screen used 51,499,195 — the Class B-1 count ALONE.** Not the total, not the Class A:
**the founders' voting stock, which carries essentially no economic interest in the Inc.**
It is the same companyfacts dimension-dropping mechanism as LEVI and PINS, except that here
it landed on the *smaller* of two classes rather than on a stale one, so the resulting cap
was 3.58x too small and the yield 3.58x too high.

**The consistent pairing, stated so the run does not have to re-derive it.** The consolidated
cash-flow statement is **100% of the LLC**, so the denominator must be the **fully-exchanged
economic count**: Class A + the paired exchangeable units represented by Class B-1 =
**184,596,369** off the 2026-06-30 10-Q cover (143,163,588 + 41,432,781). The alternative —
Class A alone against the Inc.'s share of cash flow — is equally consistent and gives the
same answer per share; **what is not permitted is either class alone against 100% of the
cash flow**, which is exactly what the screen did.

**FLNC is now runnable at Stage 0.** Nothing about its business has been decided, and the
Up-C structure raises a separate Q3 question the run still owes: a Tax Receivable Agreement
usually accompanies this structure, and it is a real claim on future cash.
