# ADDENDUM — 2026-09-02
## DKS and PINS re-priced from filed covers; and a third perimeter class both guards miss

**COMPUTATION — NOT A CLEARANCE** (operator rule 3). Nothing below opens or closes a
question on either business. This corrects two screen entries and records one new tool
defect, per operator rule 6: violations found later are corrected in an addendum.

---

## WHY THEY NEEDED RE-PRICING

The NKE run of 2026-09-02 found that `shares_outstanding()`'s 550-day staleness guard was
being **defeated by its own caller**: the master-queue script wrote
`F.shares_outstanding(f) or M.shares_asof(f, TODAY)`, and the `or` handed control to an
**unguarded** path exactly when the guard fired. Nineteen of 379 priced names used a share
count older than 550 days. **DKS and PINS were both in the live tier-1 queue.** The
fallback is removed; this addendum reprices the two that mattered.

Counts below are **read by hand off the cover page of the most recent 10-Q**, not taken
from XBRL — operator rule 4.

| | cover date | accession | classes | total shares |
|---|---|---|---|---|
| **DKS** | 2026-05-29 | 0001089063-26-000027 (10-Q, period 2026-05-02) | Common 65,931,904 + Class B 23,570,633 | **89,502,537** |
| **PINS** | 2026-07-28 | 0001506293-26-000104 (10-Q, period 2026-06-30) | Class A 492,198,008 + Class B 74,115,019 | **566,313,027** |

Both companies have **no `dei:EntityCommonStockSharesOutstanding` in companyfacts at all**
— the LEVI mechanism, now confirmed a third and fourth time. Once a filer tags the cover
by share class, `companyfacts` drops the dimensioned facts, and the fallback chain lands on
`us-gaap:CommonStockSharesOutstanding`, whose last observation is whatever the filer last
reported **undimensioned**:

- **DKS: 93,768,978 at 2011-01-29** — fifteen years and seven months old.
- **PINS: 127,371,000 at 2019-03-31** — the **pre-IPO** balance sheet. Pinterest listed
  three weeks later.

---

## PINS — THE SCREEN'S CAP WAS 4.06x TOO SMALL

| | screen | corrected |
|---|---:|---:|
| shares | 127,371,000 | **566,313,027** |
| market cap | $2,954M | **$11,995M** (at $21.18, 2026-09-02) |
| owner earnings, bottom boundary [E5-34] | $147M | $147M *(unchanged)* |
| **yield** | **4.98%** | **1.23%** |
| vs sovereign (5.18%) | −0.20% | **−3.95%** |
| **perpetual growth needed for the [E4-28] floor** | **5.02%** | **8.77%** |

**PINS leaves tier 1.** It was queued as a name needing ≤6% growth; it needs 8.77%.

**And the generous construction does not rescue it.** Owner earnings by year, $M
(OCF − SBC − (c)):

| year | OCF | SBC | D&A | capex | OE (D&A end) |
|---|---:|---:|---:|---:|---:|
| 2021 | 753 | 415 | 28 | 0 | 310 |
| 2022 | 469 | 497 | 46 | 29 | −74 |
| 2023 | 613 | 648 | 22 | 8 | −56 |
| 2024 | 965 | 766 | 21 | 25 | 178 |
| 2025 | 1,284 | 880 | 25 | 32 | **379** |

**Take the single best year in the company's history and the yield is 3.16%, still two
points below the government bond.** Two years in the five-year window are negative.
`level_shift` reads **5.26x, "STEP UP — normalize down [E4-41]"**, and
`best_year_dependence` reads **24%**, its own warning that a tight spread here is
arithmetic rather than knowledge.

**The number that governs this business is $880M of stock compensation against $1,284M of
operating cash flow — 68.5%.** SBC is simply an expense **[E5-06]**; the corpus is
stricter here than any threshold this project ever invented. Nothing about Pinterest's
business is decided by this note; the price question is answered before the reading starts.

---

## DKS — THE SHARE COUNT WAS NEARLY RIGHT, AND A LARGER ERROR WAS HIDING BEHIND IT

| | screen | corrected |
|---|---:|---:|
| shares | 93,768,978 (2011) | **89,502,537** |
| market cap | $12,467M | **$12,255M** (at $136.92) |
| yield, bottom boundary | 4.27% | **4.34%** |
| growth needed for the floor | 5.73% | **5.66%** |

**The fifteen-year-old count was 4.5% too high and the error ran the conservative way.**
Dick's retired only 4.5% of its shares in fifteen years. Recorded plainly: on this name
the defect did not matter, and saying so is part of the practice.

### What does matter: the perimeter changed inside the window

From the fiscal 2025 10-K (accession 0001089063-26-000007, filed 2026-03-27):

> *"On September 8, 2025, we completed the acquisition of Foot Locker, a leading footwear
> and apparel retailer, for total purchase consideration of $2.5 billion, pursuant to the
> Merger Agreement dated May 15, 2025. … Foot Locker delivered sales of $8 billion in
> fiscal 2024"*

> *"The Foot Locker Business contributed net sales of $3.1 billion and a net loss of
> $60.0 million during fiscal 2025. These results reflect the operations from the
> September 8, 2025 acquisition date through the end of fiscal 2025, **which does not
> include the peak back-to-school selling season in August.** Pro forma comparable sales
> for the Foot Locker Business … **decreased 3.3%** … includes a decrease in Foot Locker's
> International comparable sales of **8.1%**"*

And the pro forma table, which is the whole finding:

| (in thousands) | Fiscal 2025 | Fiscal 2024 |
|---|---:|---:|
| Net sales | $21,786,502 | $21,431,183 |
| **Net income** | **$755,469** | **$1,142,955** |
| Diluted EPS | $8.30 | $12.34 |

**Combined revenue is flat (+1.7%) and combined net income fell 33.9%** — after the pro
forma *adds back* Foot Locker's $110M goodwill impairment and *excludes* fiscal 2025
acquisition costs.

**So the screen divided eight years of standalone Dick's, plus a five-month loss-making
stub of an acquired business that excluded its own peak season, by the market cap of the
fully combined company.** That is the Honeywell error running the other way, and the
direction of the resulting bias **is not determinable from the screen** — it depends on
whether Foot Locker adds or subtracts owner earnings, which requires the filing.
**DKS's screen yield is unreliable in both directions and the run must build (c) and owner
earnings on a pro forma basis.**

A second thing the window is carrying, worth flagging to whoever runs it: **capex against
depreciation is 1.49x, 2.01x and 2.33x in the last three fiscal years** ($587M, $803M,
$1,137M against $394M, $400M, $489M). That settles the [E3-44] direction question before
the run starts — **capex is emphatically the conservative end here**, and it is why the
bottom boundary is $532M against $925M at the D&A end.

---

## THE TOOL DEFECT: A CASH-FUNDED ACQUISITION IS INVISIBLE TO BOTH PERIMETER GUARDS

Two guards exist and **neither one could ever have caught this**:

- **`share_count_shift()`** reads the share count, because Honeywell's spin-off and reverse
  split moved it 635.7M → 316.9M. **Dick's paid cash and debt. Its count went 93.8M →
  89.5M, a 0.95x ratio, comfortably inside the 0.75–1.50 band.** A guard that watches the
  equity cannot see a deal that did not use equity.
- **`scale_shift()`** reads the largest year-over-year revenue ratio. **DKS reads 1.28x**,
  against a 2.0x line — and revenue rose 28.1% on an acquisition that added a business
  60% of Dick's own size, only because the stub was five months long.

**This is a third perimeter class, not a threshold that needs tuning.** The existing two
watch *consequences* that a particular deal shape happens to produce. The event itself is
tagged, and it should be read directly.

`acquisition_flag()` is added to `floor_screen.py`. It sums
`PaymentsToAcquireBusinessesNetOfCashAcquired` (and its siblings) across the owner-earnings
window and **raises a prompt to read whenever the total is material against market cap**.
Per operator rule 8 it **flags and does not adjust** — the first finance-lease fix tried to
compute an answer and was wrong on SHOE, and the correct fix computes less.

**The limit, stated rather than hidden:** DKS's own acquisition line reads **−$257M** in
fiscal 2026, because Foot Locker's cash on hand exceeded the net cash paid. **The $2.5
billion of consideration is nowhere in the cash-flow statement.** So the new flag would
have fired on the sign anomaly, not the size, and on many filers it will not fire at all.
**A screen cannot establish a perimeter. Only the filing can** — operator rule 4, again,
and the third time in four days that a tool fix has ended in that sentence.

---

## EFFECT ON THE QUEUE

- **PINS** moves from tier 1 to tier 2 (8.77% growth required). It is not judged and it is
  not dropped; the operator's instruction is that every business on the lists is run, and
  the floor screen decides **order**, never inclusion.
- **DKS** stays in tier 1 at 4.34%, with a standing instruction attached: **build owner
  earnings pro forma, or state why not.**
- Neither name has had a question opened. Both still owe a price and a pass/fail line.
