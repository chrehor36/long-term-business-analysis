# CASE 2026-10-12: floor-plan debt, merger or acquisition, and the serial acquirer, for the operator's approval
*A PRIME RULE 5 case, written 2026-10-12 at the operator's instruction after the ABG re-check of the same day raised three
points that recur across the operator's sheet (dealers, distributors, roll-ups). Nothing here changes a run of record.*

## Why this exists
The ABG re-run (`Test Runs/2026-10-12 Run - ABG Asbury Automotive.md`) closed OUT at Q7, and its analyst named three places
where the text left it to choose, two of which move the fair price by most of its value: whether $1,839.5M of floor-plan
notes count in net debt (the organic fair price is $102.33 without them and about zero with them); whether the large
dealer-group purchases are "mergers" or "acquisitions" (Q7's specific (c) treats the two differently); and why the central
figure still collapses for a company that grows by buying ($7.39 a share for ABG; ECL, EFX, AME and ESI before it).

---

## A. Floor-plan and other inventory-secured trade debt

### What the runs found
Dealers (ABG) and some distributors finance inventory with notes secured by that inventory and repaid as each unit is
sold, often from the manufacturer's own finance arm. Their interest is an operating cost: it sits inside cost of sales or
the operating cash flow the run starts from. Q7's section H counts "borrowings and finance leases less cash and
securities" in net debt and says nothing of this class. ABG left the notes out of net debt as its own convention.

### What the v5 rows say
On the basis: "we evaluate acquisitions on an all-equity basis" **[L2017-004]**. On the speakers' own dealerships: "We
don’t see the finance business, in dealers — we don’t bring anything to that party." **[M2015-011]**. On debt in general:
"We are not interested in incurring any significant debt at Berkshire for acquisitions or operating purposes."
**[L2005-020]**; "Businesses earning good returns on equity while employing little or no debt" **[R1997-001]**. No row
addresses inventory-secured trade finance.

### What the corpus decides, and what it leaves open
Decides that debt is weighed and that the central figure is all-equity. Leaves open whether trade finance whose cost is
already charged in owner cash is "debt" for that figure. Counting it in net debt while its interest is also inside owner
cash charges it twice; leaving it out while its interest is excluded from owner cash charges it never.

### The change proposed
Add to section H (Q7, "On what the floor is earned"):

> **Inventory-secured trade finance** *(CONVENTION, ours)*. Notes secured by inventory and repaid as that inventory is
> sold (floor plan and its equivalents) are treated as working capital, not as net debt, wherever their interest is
> already charged inside owner cash; the run states the amount, shows the fair price with it counted in net debt beside
> the central figure, and weighs it at Q9 with the other debt. Rationale: the cost is charged once, where the business
> pays it; the alternative figure keeps the reader from mistaking an operating liability for nothing.

### The operator is asked
Approve, or choose the alternative (count it in net debt and add its interest back to owner cash).

---

## B. Merger or acquisition

### What the runs found
Specific (c) says acquisitions are capital spending (deducted, with total growth credited) and that "A merger inside the
window is valued on the combined companies' own averages, with the deal's financing deducted." It does not say which is
which. ABG's three large dealer-group purchases (LHM, Koons, Herb Chambers) could be read either way, and the reading
moves the cash base materially.

### What the v5 rows say
"it's equally silly for the would-be purchaser to focus on current earnings when the prospective acquiree has either
different prospects, different amounts of non-operating assets, or a different capital structure." **[L1994-014]**. No row
draws the line between a merger and an acquisition for valuation.

### The change proposed
Add to specific (c):

> **Which deals are mergers** *(CONVENTION, ours)*. A deal is valued as a merger, on the combined companies' own averages,
> where the filer itself filed the target's audited financial statements (the SEC's significance test, which the filer
> applies, requires them for a large purchase, typically in an 8-K/A); every other purchase is an acquisition and is
> treated as capital spending. Rationale: the line is drawn by a fact in the filings, not by the analyst, and a merger can
> only be valued on the combined record where that record is filed.

### The operator is asked
Approve, or set another line (for example a share of the acquirer's owner cash).

---

## C. The serial acquirer

### What the runs found
Under specific (c), as amended on 2026-10-10 (purchases stop after year ten), the central figure for a company whose
purchases consume most of its owner cash still comes out near zero or negative: ABG $7.39 a share, ECL $(4.09) to $30.89,
EFX nil, AME $(5.56) to $31.35, ESI $4.56 to $5.78. Every such run then set the alert on the organic pair, labelled so.
The figure is not wrong in arithmetic: it is what the business is worth to an owner if it keeps buying at the returns it
has earned. But it values the programme of purchases, not the business, and the programme is a choice management makes
each year.

### What the v5 rows say
"they don’t get credit for gross cash flow, they get credit for whatever net cash is left every year." **[M1998-080]**;
"growth can destroy value if it requires cash inputs in the early years of a project or enterprise that exceed the
discounted value of the cash that those assets can generate in later years" **[L2000-023]**; "the history of acquisitions
is that it’s not an enormous way to wealth." **[M2014-074]**; "what is smart at one price is dumb at another." **[L2011-003]**.
The rows judge purchases as uses of the money, which is Q6's question.

### What the corpus decides, and what it leaves open
Decides that purchases are judged by what they return against their price, a capital-allocation judgment. Leaves open
whether Q7 or Q6 carries it. Today Q7 carries it in the arithmetic, which makes the central figure a forecast of
management's future buying, and Q6 weighs it again.

### The change proposed
Add to specific (c):

> **The serial acquirer** *(CONVENTION, ours)*. Where net purchases over the window exceed half of owner cash before
> purchases, the central figure is the organic pair (purchases left out, organic growth as the filer reports it), and the
> default pair is shown beside it; Q3 states what the purchases have returned on their price, and Q6 weighs the programme
> as a use of the money **[L2011-003]**, **[M2014-074]**. Rationale: the business is valued as it stands, and the buying,
> which management can stop or continue, is judged where the framework judges uses of the money; the default pair beside
> it shows what continued buying at the record's returns would be worth.

### The operator is asked
Approve or refuse; and if approved, whether the alerts of ECL, EFX, AME, ESI (no alert, closed at Q5) and ABG, all already
set on the organic pair, stand unchanged (they would).

---

## What this case does not do
It changes no governing document, run or alert; the overnight cycle continues under today's text while the operator
decides. No ledger row is added; every row cited is in `principle_ledger_v5.csv`, and the case says where no row speaks.

## Summary of the decisions asked
| | the gap | proposed | the operator decides |
|---|---|---|---|
| A | floor-plan and inventory-secured trade debt | working capital where its interest is inside owner cash; the counted figure beside | approve, or count it as debt |
| B | merger or acquisition | a merger where the filer filed the target's audited statements | approve, or another line |
| C | the serial acquirer | the organic pair central above a half-of-owner-cash threshold; the buying judged at Q3 and Q6 | approve or refuse |

---
# DECIDED 2026-10-12, from the corpus, at the operator's instruction
The operator asked that the three points be decided from the corpus. A search of the whole shelf (letters, meetings, Wesco letters) found: **B decided by the corpus, differently from the proposal.** The speakers use "merger" for a deal paid in the buyer's own shares (**[L2009-019]**, **[L1998-001]**; Gen Re was a merger, Van Tuyl a purchase for cash), so a merger is a stock deal, valued on the combined averages with the shares added, and a cash deal is an acquisition; the proposed line (the filer's filing of audited target statements) was set aside for the speakers' own usage. **C supported by the corpus and adopted as proposed**: buying is judged by its price each time (**[L2011-003]**, **[M2014-074]**; of dealerships, "we may buy a lot of them, we may buy very few, just depending on price developments", 2015 meeting), which is Q6's question. **A: the shelf is silent on floor plan**; adopted as proposed, as a CONVENTION, on the arithmetic of charging the cost once and on the speakers' keeping a finance arm apart from operations (**[L2008-005]**). Applied the same day to Q7 (specific (c) and section H) and section VI of `Framework/THE FRAMEWORK v5.md`.
