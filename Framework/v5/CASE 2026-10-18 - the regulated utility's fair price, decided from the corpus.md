# CASE 2026-10-18: the regulated utility's fair price, decided from the corpus
*Written and decided 2026-10-18 at the operator's instruction "check the corpus then make a rule", after the check-in on
the overnight runs. The structure of Q7 is unchanged (no question added, merged or deleted); this fixes which of Q7's two
existing bases is central for one kind of business, so it is recorded as a case and applied the same day, as the
cases of 2026-10-12 were.*

## Why this exists
Sixteen gas and electric utilities run 2026-10-17 and 2026-10-18 closed OUT at Q7 (ATO, CPK, MDU, NJR, OGS, SWX, SR, UGI,
AES, AQN, LNT, AEE, AEP, AVA, and HOKCY and NWN with other figures). On the all-equity basis of section H every one of them
has a fair price that is not positive: at ten percent, a business earning a regulated return on its whole capital is
worth less than its debt. So the fold armed no alert, and the operator's alert list cannot hold a utility at any price.
Fifty electric utilities come next in the order file.

## What the rows say
**The all-equity basis names this exception in the sentence that states it.** The ledger row **[L2017-004]** stops before
the parenthesis; the parenthesis is now its own row, added today through `tools/v5_ledger.py`: "to assign a large portion
of our debt to any individual business would generally be fallacious (leaving aside certain exceptions, such as debt
dedicated to Clayton's lending portfolio or to the fixed-asset commitments at our regulated utilities)." **[L2017-012]**.
The blind reader of 2026-10-03 had already written in L2017-004's notes that the quote stops before the exceptions.

**The debt belongs to the assets.** "A key characteristic of both companies is the huge investment they have in very
long-lived, regulated assets, with these funded by large amounts of long-term debt that is not guaranteed by Berkshire."
**[L2010-012]**; "The size of this debt [...] is entirely appropriate" **[L2003-016]**; "we expect additional borrowings to
be concentrated in our utilities and railroad businesses" **[R2009-001]**.

**The return is the allowed return on the added capital, measured after depreciation.** "when you get an allowed return in
the electric utility you’re almost certain of earning it" **[M2010-037]**; "the return is not measured by the cash minus
the increased capital investment we’re making. It’s measured by the operating earnings after depreciation." **[M2014-086]**;
"We expect only that these businesses have reasonable expectations of earning decent returns on the incremental sums they
invest." **[L2009-012]**; "it was very easy to make calculations then as to the expectable returns in the future"
**[M1998-058]**.

**And the return is modest, which is the price's business, not the basis's.** "there’s no way we get rich on our utility
investments. But there’s no way we get poor, either." **[M2009-104]**; "in utilities the trade has been the compact has
been that you get a modest return" **[M2024-011]**; "some utilities have sold at extraordinary prices. And we can’t pay them"
**[M2017-095]**.

**What stays at Q2 and Q9.** The regulatory climate can take the return away **[L2023-011]**, **[M2025-045]**; the debt is
judged by its cover in bad years and by the spread of jurisdictions **[L2010-012]**, **[L2005-019]**; inflation makes the
capital needs heavier **[L2011-019]**, **[M2015-049]**.

## What the corpus decides
1. For a regulated utility the all-equity basis is the wrong central figure, by the speakers' own exception
   **[L2017-012]**: the dedicated debt is assigned to the business. The central figure is the equity-only basis, owner cash
   after interest against the market value of the shares, with the all-equity figure beside.
2. On the equity-only basis, the fixed-asset spending the dedicated debt funded is not charged a second time to the equity.
   Owner cash to the equity is charged the capital spending less the long-term debt raised to fund it, up to the debt share
   of the capital structure the regulator allows (CONVENTION, ours: the cap keeps a run from crediting borrowing beyond what
   the regulated structure dedicates to the assets; where the filing states no allowed structure, the business's own debt
   share of capital at the latest filed date). The rows measure the return on added capital after depreciation
   **[M2014-086]** and describe the assets as debt-funded **[L2010-012]**.
3. The floor of about ten percent is unchanged and is earned on the equity **[M2003-149]**. A utility at a full price still
   closes OUT; what changes is that the fair price can be positive, so the alert can be armed.
4. Which business qualifies: one whose deciding part (Q2, a business of parts) earns a return a regulator allows on its
   invested capital. Merchant generation and unregulated renewables, priced by a market, stay on the all-equity basis.
5. Left open: the same parenthesis names debt dedicated to a lending portfolio. A bank's and a finance arm's reading of the
   basis (the gap the BAC run of 2026-10-13 named) is not decided here.

## Applied 2026-10-18
- `Framework/THE FRAMEWORK v5.md`: Q7, the paragraph "The regulated utility" after "Inventory-secured trade finance";
  Part VI, a convention line.
- `Test Runs/_TEMPLATE - Company Run.md`, `Screens/_daily/_dispatch_brief.md`, `Screens/_daily/_overnight_prompt.md`: one
  line each, and the fold arms the equity-only figure for a regulated utility.
- The runs of 2026-10-17 and 2026-10-18 bind as written; their boxes do not move (each is priced above every case).
  Where a run's equity-only fair price is already positive, its alert is armed at that figure, labelled as the
  equity-only figure computed with all capital spending charged (so the alert is lower than the rule's figure, never
  higher). Where it is not positive (OGS, SWX, SR, AQN), the name is re-queued after the electric utilities, to be run
  under the paragraph. AES is under a signed cash merger at $15.00 and is not re-queued. The register carries a dated note.
