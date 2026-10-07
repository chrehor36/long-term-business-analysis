# TXN — acquisitions and divestitures, 2016–2026 (TASK 9)

Sweep of the FY2018–FY2025 10-Ks plus the recent 8-K list. **In the ten years FY2016–FY2025 Texas
Instruments completed exactly ONE acquisition of any kind: the Lehi, Utah fab, October 2021, $893 million
cash, accounted for as an ASSET ACQUISITION, not a business combination.** A second, much larger deal
(Silicon Labs, ~$7.5 billion) was signed 2026-02-04 and has not closed.

Corroborating evidence: goodwill is flat at **$4,330M / $4,362M** across the period and moves only by the
$32M impairment taken in 2025. No goodwill was created FY2016–FY2025.

TI states the position itself in the FY2020 10-K (line 143 of `prior10k/FY2020.txt`), verbatim:
> "Lastly, we allocate to acquisitions for inorganic growth, **which we last did in 2011 when we acquired
> National Semiconductor**."

---

## 1. THE LEHI FAB — October 2021, $893 million

### The purchase-price and accounting disclosure, verbatim and complete (FY2021 10-K, Note 11, L1465):

> "In October 2021, we completed our purchase of a 300-millimeter semiconductor factory in Lehi, Utah, for
> **cash consideration of $893 million**. The estimated fair value of assets acquired was determined based
> on market comparable information to purchase or build comparable assets and **allocated on a relative
> basis to purchase consideration**. Assets acquired included **$28 million of land, $305 million of
> buildings and improvements and $526 million of machinery and equipment**."

$28 + $305 + $526 = $859M. The $34M difference between the $859M of itemised assets and the $893M of cash
consideration is not explained in the note.

### THE ACCOUNTING — the answer to the question asked

**This was accounted for as an asset acquisition under ASC 805-50, not a business combination under
ASC 805-10.** Three markers in the filed text establish it:

1. The consideration was **"allocated on a relative basis to purchase consideration"** — relative fair
   value allocation is the asset-acquisition method. A business combination would allocate at full fair
   value with any residual to goodwill.
2. **No goodwill was recognised.** Goodwill was $4,362M at 2020-12-31 and $4,362M at 2021-12-31 —
   unchanged through the purchase year.
3. **No Note "Business combinations" exists** in the FY2021 10-K, and no pro-forma revenue/earnings
   disclosure was given, both of which ASC 805 would require for a business.

Consequently: **the entire $893 million landed in PP&E and is being depreciated**, not amortised as
intangibles and not tested as goodwill. It also means **the purchase is inside the capex line**, not a
separate investing caption. From the FY2021 10-K MD&A (L474), verbatim:

> "Investing activities for 2021 used $4.10 billion compared with $922 million in 2020. **Capital
> expenditures were $2.46 billion** compared with $649 million in 2020 and were primarily for semiconductor
> manufacturing equipment and facilities in both periods, **including the purchase of our 300-millimeter
> semiconductor factory in Lehi, Utah, during 2021.** As we continue to invest to strengthen our
> competitive advantage in manufacturing and technology as part of our long-term capacity planning, we
> expect our capital expenditures to be higher than historical levels."

**So $893M of the $2,462M FY2021 capex figure — 36% of it — was the Lehi purchase, not organic
construction.** That matters for any maintenance-capex estimate built off the FY2021 number.

### The seller is NEVER NAMED in any TXN SEC filing.

Word-boundary search for "Micron" across the FY2018, FY2019, FY2020, FY2021, FY2022, FY2023, FY2024 and
FY2025 10-K primary documents: **0 occurrences in every one.** No 8-K was filed for the transaction
(the 8-K list for 2021 contains only the routine Item 2.02 earnings releases of 2021-07-21 and
2021-10-26). Under a strict SEC-primary-documents rule, **the identity of the seller is not in the
record**. The user-supplied fact that the seller was Micron is consistent with the asset description but
is not verifiable from EDGAR filings by Texas Instruments — record it as such rather than as a filed fact.

### The carrying costs of Lehi, verbatim, year by year

**FY2021 10-K, Note 11 restructuring table (L1430):** Integration charges of **$104 million** in 2021,
footnoted:
> "(b) Includes costs related to our purchase of the Lehi, Utah, manufacturing facility, as well as
> ongoing costs until production begins in early 2023."

**FY2022 10-K (L429, L1457):**
> "Restructuring charges/other was **$257 million** compared with $54 million due to integration charges at
> our Lehi, Utah, manufacturing facility in both periods, which were partially offset by gains on sales of
> assets in 2021. The charges associated with our Lehi facility transitioned to cost of revenue **once
> production began in December 2022**."
> "(b) Includes costs related to our purchase of the Lehi, Utah, manufacturing facility, as well as
> preproduction costs before December 2022."

**FY2023 10-K (L429):**
> "Restructuring charges/other in the year-ago period was $257 million due to preproduction costs at our
> Lehi, Utah, manufacturing facility. **These costs transitioned primarily to cost of revenue after
> production began in December 2022.**"

**FY2025 10-K (L408) — five years after purchase, still not ramped:**
> "Our LFAB facility, which primarily supports our Embedded Processing business, was purchased as an
> operating fab and **is in the early stages of ramping**, so we expect factory loadings to increase over
> time. Until LFAB ramps, we expect Embedded to carry manufacturing costs that disproportionately affect
> Embedded Processing operating profit as compared to Analog."

**Running total of disclosed Lehi cost: $893M purchase + $104M (2021) + $257M (2022) integration and
preproduction charges = $1,254 million before any post-2022 underloading absorbed into cost of revenue.**
Post-2022 Lehi drag is not separately quantified — it is inside COR and inside the Embedded Processing
operating-profit collapse documented in `segment-series.md` ($1,008M in 2023 → $304M in 2025).

---

## 2. SILICON LABS — announced 2026-02-04, pending, ~$7.5 billion

### FY2025 10-K MD&A, verbatim and complete (L471):

> "As announced on February 4, 2026, we have entered into a definitive agreement to acquire Silicon Labs
> for **$231.00 per share in an all-cash transaction, representing a total enterprise value of
> approximately $7.5 billion**. Under the terms of the agreement, Silicon Labs stockholders will receive
> $231.00 in cash for each share of Silicon Labs common stock they hold at the time of closing, which is
> currently expected to close in the **first half of 2027**, subject to receipt of regulatory approvals and
> other customary closing conditions, including approval by Silicon Labs stockholders. **We expect to fund
> the transaction with a combination of cash on hand and debt financing to be arranged prior to closing.**"

### Q2 2026 10-Q, verbatim (L565–566 and L436/669):

> "During the second quarter and first six months of 2026, we incurred **$17 million and $34 million of
> acquisition charges**, respectively."
>
> "In June 2026, we entered into a **364-day delayed draw term loan credit facility for borrowings up to
> $5 billion** to support the Silicon Labs acquisition consideration and related transaction expenses. The
> availability of funding is conditioned on the consummation of the planned acquisition of Silicon Labs. As
> of June 30, 2026, there were no outstanding borrowings on the delayed draw term loan credit facility."

Related 8-Ks: **0001193125-26-036727** filed 2026-02-04 (Items 7.01, 9.01 — Reg FD announcement) and
**0001193125-26-040312** filed 2026-02-06 (Items 5.03, 9.01).

**Scale check (analyst note, not a quote):** $7.5 billion is roughly 1.5× TI's FY2025 free cash flow ×5,
8.4× the Lehi purchase, and 46% of TI's total stockholders' equity at 2025-12-31 ($16,273M). It will be
funded from a cash-and-ST-investment balance of $4.88 billion plus up to $5 billion of new term debt, on
top of $14.05 billion of existing debt. It lands in the first year after an elevated capex cycle that has
consumed **$19.70 billion over FY2021–FY2025** and will reach roughly $22 billion once 2026 is spent. Silicon Labs is a wireless/IoT microcontroller company — i.e. it goes into **Embedded Processing**,
the segment that is currently earning an 11.3% operating margin.

---

## 3. DIVESTITURES AND CLOSURES, 2016–2025

| date | event | filed disclosure |
|---|---|---|
| April 2019 | Sold the manufacturing facility in **Greenock, Scotland** | FY2019 10-K: "In April 2019, we sold our manufacturing facility in Greenock, Scotland." No price disclosed. |
| January 2020 | Announced closure of the two remaining 150mm factories, Sherman and Dallas TX | FY2019 10-K: "we announced a multiyear plan to close our two remaining factories with 150-millimeter production, **which are more than 50 years old** and located in Sherman and Dallas, Texas. Production will be transitioned from these sites to our more advanced and cost-effective 300-millimeter wafer fabrication facilities in North Texas. We expect this transition to be completed in the next three to five years. Charges for these closures cannot be reasonably estimated until a later phase of the transition." |
| 2021 | Partially reversed: "During 2021 we decided not to close a portion of our factory in Dallas." | FY2021 10-K |
| October 2021 | $50 million gain from sale of property | FY2021 10-K Note 11 |
| 2024 | $132 million gain on sale of a property; $195 million proceeds from asset sales | FY2025 10-K Note 11 and cash flow statement |
| 2025 | 150mm closures finally charged: **$85M restructuring + $32M goodwill impairment = $117M** | FY2025 10-K: "efforts to drive operational efficiencies to support our long-term strategy, including the planned closures of our two remaining factories with 150mm production, as well as a non-cash goodwill impairment related to our custom ASIC products." |

The 150mm closure announced in January 2020 as a "three to five year" transition was still being charged
for in 2025 — six years later. The $32M goodwill impairment in 2025 wrote the custom-ASIC goodwill in
*Other* to zero ($32M → $0).

---

## SUMMARY TABLE

| deal | date | size | accounting | goodwill created |
|---|---|---|---|---|
| National Semiconductor | 2011 (outside window) | $6.5bn (not from these filings) | business combination | yes — the $4,158M Analog goodwill |
| Greenock, Scotland fab | Apr 2019 | not disclosed | disposal | n/a |
| **Lehi, Utah 300mm fab** | **Oct 2021** | **$893M cash** | **asset acquisition, relative FV allocation, inside capex** | **none** |
| Silicon Labs | signed Feb 2026, close H1 2027 | **~$7.5bn EV, $231.00/sh cash** | business combination (pending) | to be determined |

**Ten-year record: one $893M asset purchase, funded from cash, with no goodwill and no premium paid for a
going concern — and then, immediately after the largest capex cycle in company history, a $7.5 billion
all-cash public-company acquisition at a scale TI has not attempted since 2011.**
