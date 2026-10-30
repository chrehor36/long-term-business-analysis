# Company Run — Ambiq Micro, Inc. (NYSE: AMBQ) — 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: not held (`PORTFOLIO.md` does not name AMBQ, AMBI or Ambiq).*

**Dispatch.** A dispatched blind purchase run under `Screens/_daily/_dispatch_brief.md`, with three departures the brief
states: (1) the lines of evidence are derived by the analyst from the 10-K's Items 1, 1A and 7 (listed below with the item
each came from); (2) competitors are the rivals the 10-K names; (3) the operator's list carries the symbol AMBI, the
company's filings give AMBQ, which is used for files and tools. Template copied to this file before any fetch (commit
`20c09b01`).

**Contamination, declared.** Seen without opening anything blind-listed: the session context showed the repository's
recent commit subjects (a fold of another company, UNP) and the project map and memory index, which describe the queue
and the framework in general terms; none of it names this company or bears on it. Nothing of it is used. No file in
`Test Runs/` was listed or searched other than this run file, the template and this run's own research folder.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $58.56 (close 2026-10-09, the last session before the run date; Yahoo Finance chart feed through
  `tools/sources.py price()`; **aggregator, flagged per operator rule 5**, live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock, **24,184,536** shares outstanding as of
  2026-08-07 (Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-11, accession `0001193125-26-344145`;
  `python Screens/cover_shares.py AMBQ` returns the same). Checked: the balance sheet in the same 10-Q gives 24,146,260
  issued and outstanding at 2026-06-30, no treasury shares; the difference of 38,276 is option and award settlement in
  July. No 8-K or prospectus filed after the 10-Q issues shares (8-Ks after 2026-08-11: none; filings after it are Forms 4
  and 144 of insiders and a Schedule 13G/A, which do not change the count). Reserved but not outstanding at 2026-06-30:
  2,007,120 RSUs and 2,375,364 options and ESPP shares, 4,382,484 in all (10-Q, equity note), about 18% of the count.
  No preferred stock outstanding since the IPO conversion.
- **Market cap:** $1,416M (24,184,536 × $58.56).
- **Sovereign for the earnings currency:** USD, **5.60%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-09 (`python tools/sources.py`, Treasury rung, not the FRED fallback).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-03-05, accession `0001193125-26-094004` (Items 1, 1A, 3, 7, 8).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-08-11, accession `0001193125-26-344145` (statements, equity note,
    MD&A, legal proceedings).
  - IPO prospectus (424B4) filed 2025-07-31, accession `0001193125-25-169401` (FY2023 and FY2024 statements).
  - Follow-on prospectuses (424B4) filed 2026-01-26, accession `0001193125-26-021460`, and 2026-06-25, accession
    `0001193125-26-281376` (offering terms).
  - Draft registration statement DRS/A of 2022-11-17, accession `0000950123-22-012507` (FY2020 and FY2021 statements,
    from the IPO attempt of 2022), and DRS/A of 2025-02-13, accession `0000950123-25-001897` (FY2023 cash flow and the
    equity roll from 2022-12-31). **FY2022 statements were never filed publicly:** the 2025 registration carries FY2023 and
    FY2024 only (an emerging growth company's two years) and the 2022 draft stops at FY2021. FY2022 is known only by the
    balance at 2022-12-31 in the equity roll.
  - Proxy (DEF 14A) filed 2026-04-22, accession `0001193125-26-170349` (summary compensation table).
  - 8-K of 2026-08-11 with exhibit 99.1 (Q2 2026 results and Q3 outlook), accession `0001193125-26-343443`; 8-K of
    2026-07-30 with exhibit 99.1 (CEO letter), accession `0001193125-26-325025`.
- **One figure cross-checked against the filed statement:** cash and cash equivalents at 2025-12-31, $140,275K, is the
  same in the 10-K balance sheet, the 10-K cash flow statement's ending balance, and the 10-Q's comparative column;
  total assets $184,680K likewise. Q2 2026 net sales of $33,901K in the press release match the 10-Q.
- `python tools/run.py AMBQ` printed one line: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The company
  has a single 10-K in XBRL. Every figure below is transcribed by hand from the filed statements named above; the
  arithmetic is in `Test Runs/_research 2026-10-11 AMBQ/scripts/owner_cash.py`.
- **Owner cash after every real cost**, by year, $ thousands: operating cash, less stock pay (added back in operating cash
  and a real cost), less capital spending, less purchases of intangible assets (the 10-K's MD&A: "technology investments
  in intangible assets to procure intellectual property licenses", a recurring cost of designing chips):

  | Year | Operating cash | Stock pay | Capex | IP licences | **Owner cash** | Source |
  |---|---|---|---|---|---|---|
  | FY2020 | (34,639) | 702 | 2,630 | 1,962 | **(39,933)** | DRS/A `0000950123-22-012507` |
  | FY2021 | (52,881) | 1,290 | 4,623 | 0 | **(58,794)** | DRS/A `0000950123-22-012507` |
  | FY2022 | not filed | | | | **not filed**; accumulated deficit rose $67.5M (158,097 to 225,592) | DRS/A `0000950123-25-001897` |
  | FY2023 | (26,958) | 2,623 | 459 | 2,562 | **(32,602)** | DRS/A `0000950123-25-001897` |
  | FY2024 | (21,428) | 5,174 | 658 | 3,073 | **(30,333)** | 10-K `0001193125-26-094004` |
  | FY2025 | (19,690) | 6,835 | 1,344 | 6,099 | **(33,968)** | 10-K `0001193125-26-094004` |
  | H1 2026 | (20,678) | 6,919 | 781 | 5,120 | **(33,498)**, six months | 10-Q `0001193125-26-344145` |

  Owner cash is negative in every year the filings show. Average of the four filed years in the literal FY2021 to FY2025
  window: **$(38.9)M** a year (equity-only basis); **$(40.2)M** on the all-equity basis (interest and other income on
  the cash removed: 43, 1,020, 980 and 3,122). D&A: $2.6M (2021), $7.7M (2023), $6.2M (2024), $7.2M (2025); it runs above
  capex because it includes amortization of the purchased IP licences, which are deducted above as spent.

**The balance sheets, read here because the file closes before Q4** (the template's instruction; the rule is
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**). The filings carry
six year-ends and one half-year, not eight to ten: the company was private until 2025 and FY2022's balance sheet was
never filed (only its equity line). $ millions:

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Jun 2026 |
|---|---|---|---|---|---|---|---|
| Cash | 65.1 | 25.9 | 25.8 | 27.3 | 61.0 | 140.3 | 366.8 |
| Receivables | 11.0 | 20.7 | n/f | 12.3 | 10.4 | 7.3 | 17.5 |
| Inventories | 7.4 | 33.7 | n/f | 21.5 | 15.0 | 16.9 | 29.4 |
| Prepaid foundry capacity | 10.5 | 16.5 | n/f | none | none | none | none |
| Intangibles (IP licences) | 1.6 | 0.7 | n/f | 5.6 | 11.7 | 11.6 | 10.2 |
| Total assets | 99.7 | 105.1 | n/f | 72.4 | 104.3 | 184.7 | 435.6 |
| Borrowings | none | none | n/f | none | none | none | none |
| Redeemable preferred | 219.7 | 237.5 | 288.3 | 320.2 | 378.2 | converted | none |
| Accumulated deficit | (132.8) | (158.1) | (225.6) | (277.9) | (320.3) | (356.7) | (374.0) |
| Net sales in the year | 51.0 | 91.0 | n/f | 65.5 | 76.1 | 72.5 | 59.0 (H1) |

Sources: DRS/A `0000950123-22-012507` (2020, 2021); DRS/A `0000950123-25-001897` (2022 equity roll); 424B4
`0001193125-25-169401` (2023, 2024); 10-K `0001193125-26-094004` (2024, 2025); 10-Q `0001193125-26-344145` (Jun 2026).
n/f = not filed. **What the figures say:** the business has been funded by its owners every year, never by its
customers: the preferred balance rose from $219.7M to $378.2M between 2020 and 2024, then the IPO and two follow-ons
raised $102.7M and $243.3M net (10-K cash flow; 10-Q equity statement), while the deficit grew by $241.2M from 2020 to
mid-2026. In 2021, the chip-shortage year, inventory rose to 37% of the year's sales and $16.5M was prepaid to the
foundry for capacity; net sales then fell to $65.5M in 2023 and inventory was worked down to $15.0M by 2024. The
receivables and inventory build of H1 2026 ($10.2M and $12.4M, 10-Q cash flow) comes with the 89.7% rise in Q2 sales.
There are no borrowings and no goodwill on any filed balance sheet; the IP licences are partly bought on credit
($9.8M of intangible purchases sat in payables and other liabilities at 2025-12-31, 10-K supplemental cash flow).
**What they cannot say:** anything about 2022, the year the deficit grew most ($67.5M), or how the business behaves
through a full downturn after its 2025 change of customers.

**Lines of evidence this name needs, derived from the 10-K** (departure (1) of the brief):
| Line | Item it came from |
|---|---|
| Rate of technical change in the field; the company's own ten-year outlook for its technology | Item 1 (Competition), Item 1A (industry cyclicality, "no guarantee that our approach to low power will remain competitive") |
| Customer and distributor concentration, and how fast the customer list turns | Item 1 (Our End Customers), Item 7 (net sales by region) |
| Foundry and supplier dependence | Item 1 (Manufacturing), Item 1A (TSMC the only wafer producer) |
| Pricing: declining average selling prices | Item 1A |
| Margins over every year filed; losses; accumulated deficit | Item 7, Item 8, the two registration statements |
| Funding: preferred rounds, IPO, two follow-ons, share issuance and its prices | Item 7 (liquidity), Item 8 (equity), the prospectuses |
| Stock pay and the non-GAAP figure featured | Item 7 (non-GAAP measures), the Q2 press release |
| Debt, leases, litigation | Item 8 (balance sheet, leases), Item 3 |

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the owner would be content to hold this "if the market closed for five years"
**[M1997-109]**, and the answer depends on whether its cash can be foreseen at all; the company has never produced owner
cash in any year it has filed. "the market is there to serve you and not to instruct you" **[M2006-077]**: the price has moved from the
$24.00 IPO (2025-07-31) to the $78.00 follow-on (2026-06-25) to $58.56 within fifteen months, and none of those prices
says anything about value. Margin of safety: if the decision needs pencil and paper, "it’s too close to think about"
**[M1996-084]**. The analyst's habits: "write it down in the first 30 minutes" **[M1997-127]** and look for "what you’re
missing" **[M2025-013]**. **Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**): (1) the 10-K's own words, "The
semiconductor market is intensely competitive. We anticipate that the market for our products will continually evolve
and be subject to rapid technological change" (Item 1, Competition); (2) the top five end customers were 91% of 2025
net sales and 92% of 2024's, and the largest customer of 2024 (Customer D, 41%) is not among the customers above 10% in
2025 (Item 1); (3) sales to Mainland China fell from 50% to 9% of net sales in one year, $38.0M to $6.2M (Items 1 and
7); (4) every filed year from FY2020 to H1 2026 is a loss with negative owner cash, accumulated deficit $374.0M at
2026-06-30; (5) the flagship next family, Atomiq, "is currently in development" (Item 1). For the business: net sales in
Q2 2026 rose 89.7% on the year to $33.9M, and gross margin has risen from 29.7% (FY2023) to 45.0% (Q2 2026); no debt;
$366.8M of cash at 2026-06-30.

## THE STANDING RULE
The buyer's own conduct is not the target's: a purchase of this name, unlevered and sized so that its loss to zero is
bearable, puts the buyer at no risk of ruin; borrowed money to own it would, "borrowed money has no place in the
investor's tool kit" **[L2014-005]**, and "We are never going to risk what we have and need for what we don’t have and
don’t need" **[M2012-081]**. No finding against the purchase on this rule; the questions follow.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" and "some notion of how the industry will develop and where
the company will stand within the industry" **[M2012-065]**; "a reasonable probability of being able to asses where the
business will be in 10 years" **[M2000-037]**. Understanding the product is not enough: "We just don’t know the economics
of it 10 years from now" **[M2000-104]**.

**The product is understood; the economics are not foreseeable.** What Ambiq sells is plain from Item 1: fabless
systems-on-chip, made by TSMC, that run sub- and near-threshold to cut power two to five times, sold mostly through
distributors into wearables and other battery devices, with software kits on top. The ten-year questions are another
matter. Applied to the filings, the tests of Q1:

1. **Where will it be in ten years?** "You’re trying to print the next 10 years of Value Line in your head."
   **[M1999-132]**. The company's revenue base has not held its shape for two years
   running: net sales $51.0M (2020), $91.0M (2021), not filed (2022), $65.5M (2023), $76.1M (2024), $72.5M (2025),
   $59.0M in H1 2026. Its strategy names three new fields it has not yet entered at scale: Atomiq, which "is currently in
   development"; SPOT applied to "new chip classes such as application processors (APs), dedicated AI processors"; and a
   licensing business, "such as building next-generation AI data center chips" (10-K, Item 1, Our Strategy). Where the
   business will be in ten years depends on which of these works, and none has a filed record.
2. **The key variables, and how predictable they are.** The variables the 10-K itself names: design wins
   in "lengthy selection processes" won "without any assurance" (Item 1A); a customer list in which the top five took 91%
   of 2025 net sales and the largest 2024 customer, 41% of that year, fell below 10% the next year (Item 1); average
   selling prices that are "generally characterized by" decline (Item 1A); wafer supply from "TSMC, which is the only
   producer of semiconductor wafers that are used in our products" (Item 1A); and the pace of a rival approach to low
   power. Each moves on the decisions of a handful of device makers and of rivals with "substantially greater financial,
   technological, manufacturing, marketing, and sales resources" (Item 1A). "If something is not very predictable,
   forget it." **[M1998-044]**
3. **Do the past statements tell me the future ones?** The speakers ask whether "the financial statements will tell me
   the information that’s useful to me in making a judgment about what the future financial statements are going to look
   like" **[M2008-033]**. No. Six filed years are losses, and the mix of
   the latest year was remade in one year: Mainland China fell from 50% to 9% of net sales, $38.0M to $6.2M, "as we made
   a deliberate decision to diversify away from low margin, Mainland China customers" (Item 1, Item 7). The 2021 figures
   came from a shortage year with prepaid foundry capacity; the 2025 figures from a new customer set; H1 2026 from a ramp
   of new products. No two of the windows describe the same business.
4. **Important and knowable?** "If something’s important but unknowable, forget it." **[M2006-076]**. The decisive item, whether SPOT stays ahead of the "other, diversified
   technological approaches" to low power, is important and is not knowable from outside. The 10-K says: "There is no
   guarantee that our approach to low power will remain competitive [...] There is the possibility that novel, unique
   approaches to low power emerge that surpass the capabilities of our technology" (Item 1A).
5. **Would the insiders write it down?** The insiders' own document declines to: "We anticipate that
   the market for our products will continually evolve and be subject to rapid technological change" (Item 1,
   Competition), and the industry "is characterized by constant and rapid technological change, rapid product
   obsolescence, price erosion, evolving standards, short product life cycles" (Item 1A). The speakers' test is that such
   insiders "would not want to put down on paper their predictions about where 10 companies you would choose in the tech
   field would be in 10 years" **[M2000-105]**.
6. **Can I name the winner, not just the industry?** "we don’t have the faintest idea who the winners will be"
   **[M2012-067]**. Edge AI may well grow; the 10-K and the Q2 letter
   say so. Growth seen for an industry "does not mean we can judge what its profit margins and returns on capital will be
   as a host of competitors battle for supremacy" **[L2009-005]**. The named rivals include Infineon, Microchip, NXP,
   Silicon Laboratories, STMicroelectronics, Texas Instruments, Nordic Semiconductor, Renesas, Synaptics and Qualcomm
   (Item 1A); which of them, or Ambiq, holds the low-power edge in ten years cannot be named from the filings.
7. **Customers or technology?** The later rows project "consumer behavior and threats to a business" **[M2023-030]**.
   The forecast is about technology and the design
   choices of a few device makers, not about consumer habit; the brand the end user knows is the device's, not Ambiq's.
8. **How far off could I be?** "some model in our mind of how far off we can be" **[M2011-084]**. Very far: the outcomes run from a chip family designed out at two
   customers to a licensing platform in data centres.
9. **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**

**Routing.** "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations
of its long-term economics" **[L1993-023]**; where a technological component "of significance" could hurt the business,
"it won’t make it through the filter" **[M1998-008]**; "We view change as more of a threat into the investment process
than an opportunity" **[M1999-063]**. By the routing fixed in Q1, a business whose ten-year economics cannot be foreseen
because its industry changes fast closes here, TOO HARD.

**The cause: NATURE, not WORK.** Section I separates the two causes by test 5 of Q1, the insiders who "would not want to put down on paper their
predictions" **[M2000-105]**. Here the filer, the best-informed insider, writes that its approach may be
surpassed and that its market will "continually evolve". More reading does not cure it: "We couldn't solve this problem,
moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**; "Our problem -- which we
can't solve by studying up -- is that we have no insights into which participants in the tech field possess a truly
durable competitive advantage." **[L1999-018]**. A research pass could not end otherwise: the deciding question is not
knowable, so by Part VII step (1) it would close TOO HARD (NATURE) at once. The box is not a judgment of quality: "It
doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we
don’t know how to evaluate it." **[M2000-038]**. A lower price does not reopen it (section I).

**Against the verdict, stated as strongly as the filings allow.** Ambiq has shipped five generations of one product
family, over 290 million units; its process is mature (TSMC nodes from 180 to 12 nanometres) rather than leading-edge;
its customers face a cost to qualify a new supplier that the 10-K says keeps them with existing suppliers "for a lengthy
period of time" (Item 1A); net sales have grown for five consecutive quarters and gross margin rose from 40.1% in Q2 2025 to 45.0% in Q2 2026
(8-K exhibit 99.1, `0001193125-26-343443`). A reader could call it a narrow, slow niche
that large rivals will not bother to contest. That reading fails on the filer's own record: the customer set turned
over in one year, the next product family is unbuilt, the rivals the 10-K names have, in its words, "substantially greater" resources, and the company has never covered its costs in a filed year. The doubt stands: "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**.

- **VERDICT: TOO HARD (NATURE)**, at Q1, the third of "in, out, and too hard" **[M2006-013]**: the ten-year economics of
  an ultra-low-power chip designer in an industry its own 10-K calls subject to "rapid technological change" cannot be
  foreseen; understanding is "being able to asses where the business will be in 10 years" **[M2000-037]**, and "a
  business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its
  long-term economics" **[L1993-023]**, so "it won’t make it through the filter" **[M1998-008]**; the filer's own Item 1A declines the forecast, as the speakers say insiders do: they "would not want to
  put down on paper their predictions" **[M2000-105]**. Q2 to Q12 NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed the file).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (the reporting figures are computed below under COMPUTATION, NOT A CLEARANCE).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year economics of a fabless ultra-low-power chip designer in a field its
own 10-K says will "continually evolve and be subject to rapid technological change" cannot be foreseen: "a business
that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its long-term
economics" **[L1993-023]**; the people closest to such a field "would not want to put down on paper their predictions"
**[M2000-105]**. Closed box: no research pass, and a lower
price does not reopen it (section I). **Integrity facts recorded, not judged** (quarterly guidance and a featured
non-GAAP net loss that leaves out stock pay and depreciation; see AFTER THE STOP, Q4 and Q5).
COMPUTATION, NOT A CLEARANCE, for the operator's reporting figures: owner cash negative in every filed year; value range
(one case, no growth) **$(14.53)** a share all-equity, $(28.74) equity-only, against **$58.56**; fair price **$(1.46)**
all-equity, $(16.09) equity-only. Neither is positive.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2). Each with its source*, written down as Darwin's rule asks, "write it down in the first 30 minutes" **[M1997-127]**.

**Q2 (the castle).**
- Rivals named by the 10-K (Item 1 and Item 1A): Infineon, Microchip, NXP, Silicon Laboratories, STMicroelectronics,
  Texas Instruments, Nordic Semiconductor, Renesas, Synaptics, Qualcomm, and "emerging companies". **Not SEC filers,
  flagged:** Infineon, Nordic Semiconductor, Renesas. STMicroelectronics files a 20-F and was not among the three read.
- **The competitor row**, same metrics, from the three rivals' 10-K XBRL facts (SEC companyfacts, transcription and
  screening only, not checked against each filed statement; `scripts/peers.py`), whole span:

  | Company | Span | Gross margin | Operating margin | Latest 10-K accession |
  |---|---|---|---|---|
  | Silicon Laboratories (SLAB) | CY2016-CY2025 | 53.4% to 62.7% | (28.3)% to 11.6% | `0001038074-26-000005` |
  | Microchip (MCHP), fiscal years ending March, SEC frames | CY2016-CY2025 | 51.6% to 67.5% | 6.7% to 36.9% | `0000827054-26-000016` |
  | NXP (NXPI) | CY2017-CY2025 | 49.2% to 56.9% | 4.9% to 28.8% | `0001413447-26-000008` |
  | **Ambiq (AMBQ)** | FY2020-H1 2026, FY2022 not filed | **29.7% to 44.4%** | **(78.3)% to (27.6)%** | `0001193125-26-094004` |

  Ambiq, by year: gross 42.3% (2020), 33.8% (2021), 29.7% (2023), 31.9% (2024), 44.3% (2025), 44.4% (H1 2026);
  operating (39.7)%, (27.6)%, (78.3)%, (53.4)%, (54.5)%, (34.6)%. Over every year filed, Ambiq's gross margin sits below
  the lowest year of each of the three rivals, and its operating margin below the worst year of Microchip and NXP in every year, and below Silicon Labs' worst year
  in all but FY2021 ((27.6)% against Silicon Labs' (28.3)% in CY2024).
- Pricing: "The market for our products is generally characterized by declining average sale prices (ASP)" and "We
  typically conduct pricing negotiations for our existing products with our largest end customers" (10-K, Item 1A).
- Customers: top five end customers 91% (2025) and 92% (2024) of net sales; Customer E 36%, F 29%, G 20% in 2025;
  Customer D 41%, F 24%, E 21% in 2024; distributors B 21% and C 20% of 2025 net sales (10-K, Item 1). Purchase orders,
  not long-term agreements (Item 1).
- Patents: 57 issued U.S. patents, 11 issued foreign, expiring 2033 to 2042 (10-K, Item 1).

**Q3 (capital).** Fabless: capex $0.5M to $4.6M a year; IP licence purchases $0M to $6.1M; R&D $38.5M (53% of 2025
sales) expensed (10-K, Item 1). The capital that keeps the business going has come from equity every year (Step 0
balance sheets). No return on capital can be computed: operating income negative in every filed year.

**Q4 (the accounts).**
- The Q2 2026 press release (8-K `0001193125-26-343443`) features non-GAAP gross profit, operating expense and net loss;
  the 10-K defines non-GAAP net loss as excluding "income taxes, depreciation and amortization, stock-based compensation,
  gain on nonmonetary transaction, severance costs, transaction costs including IPO bonuses, and warrant valuation"
  (Item 7). Q2 2026 non-GAAP net loss $(1.8)M against GAAP $(7.1)M.
- Quarterly guidance: Q3 2026 net sales $36.0M to $37.0M, non-GAAP gross margin 46.5% to 47.5%, non-GAAP net loss per
  share $(0.20) to $(0.12) (same 8-K).
- A vendor's "nonreciprocal transfer of assets" of about $1.6M a year in 2024 and 2025, booked as a gain in cost of
  sales (10-K, Item 8 note). It lifts reported gross profit by that amount each year.
- Stock pay rising: $0.7M (2020), $1.3M (2021), $2.6M (2023), $5.2M (2024), $6.8M (2025), $6.9M in H1 2026 alone.
- Auditor's report, internal-control findings and revenue-recognition notes were not read for this run.

**Q5 (the people).** CEO Fumihide Esaka, total pay $6.27M in 2025 against $2.74M in 2024 (proxy `0001193125-26-170349`);
the founder, Scott Hanson, is named in Item 1A as a key person. Insider Forms 144 filed August to October 2026 and Forms 4
(submission index; not opened). The guidance and the featured non-GAAP figure above are the habits a later run reaching
Q5 reads with the integrity record, where "If you’ve got doubts, forget it." **[M2013-088]** No material legal proceedings (10-K Item 3; 10-Q Part II Item 1).

**Q6 (money and owners).** IPO of 4,600,000 shares at $24.00 including the over-allotment, $102.7M net (10-K cash flow;
424B4 `0001193125-25-169401`); follow-ons of 2,636,651 primary shares at $31.00 (plus 42,949 sold by holders) and
2,300,000 at $78.00 (2,000,000 plus the over-allotment, by difference from the equity statement), 4,936,651 primary
shares in all for $243.3M net (424B4s
`0001193125-26-021460`, `0001193125-26-281376`; 10-Q equity statement). Common shares outstanding 18,316,928 at
2025-12-31 and 24,184,536 at 2026-08-07, up 32% in seven months. No buybacks, no dividends. A secondary listing on the
Singapore Exchange announced in the Q2 release.

**Q9 (ruin).** No borrowings; cash $366.8M at 2026-06-30; operating lease liabilities $4.6M; TSMC the only wafer
source; some design-service agreements and purchase commitments "are non-cancelable" (10-K, Item 1A).

## COMPUTATION, NOT A CLEARANCE: the two reporting figures
*Q1 closed the file. These figures are computed only because the operator asks for them (Part VII, The owner's price);
they carry no entry language and no verdict (operator rule 3).*

- **Input:** owner cash after every real cost (Step 0 table). **Literal window FY2021 to FY2025**, four filed years
  (FY2022 never filed): average $(38.9)M equity-only, $(40.2)M all-equity (interest and other income removed).
- **Growth.** The series is negative throughout, so a compound rate between end years is meaningless; the halves of the
  window are both negative and equally meaningless; by Q7 specific (b) "the range is the no-growth case alone, said so".
  **Said so: the range is one case.**
- **Cycle base, specific (a).** FY2021 was the shortage year (prepaid foundry capacity, inventory at 37% of sales). The
  filer's own description of that year as aberrational was not read (the 2022 draft's MD&A was not opened), so the
  literal window is central. Beside it, the window without FY2021 (FY2023 to FY2025): $(32.3)M equity-only, $(34.0)M
  all-equity a year. No base drawn from any filed year, nor H1 2026 ($(33.5)M in six months), turns owner cash positive.
- **Rate and basis.** Discount at the 30-year Treasury, 5.60% (2026-10-09). All-equity basis: owner cash before interest,
  plus net cash of $366.8M at 2026-06-30 (no borrowings, no finance leases; operating leases left out); shares
  24,184,536. Tax: the company pays almost none ($40K in 2025); no carryforward is priced, since there is no positive
  income to shelter.
- **(a) VALUE RANGE** (one case, no growth, ten years then none, at 5.60%): **$(14.53) a share on the all-equity basis
  (central)**; $(28.74) equity-only. On the FY2023 to FY2025 base beside it: $(9.95) all-equity, $(23.85) equity-only.
  Price **$58.56**.
- **(b) FAIR PRICE** (the end case valued at ten percent; with one case, the average is that case): **$(1.46) a share
  all-equity (central)**; $(16.09) equity-only. On the FY2023 to FY2025 base: $1.10 all-equity, $(13.36) equity-only.
- **Owner cash is negative over the whole window. The convention yields no positive value on the literal window.** No
  substitute input (a forecast, a margin assumption, sales growth) is used. The one positive figure, $1.10 on the
  shorter base at ten percent, comes only from the arithmetic of a negative stream: a higher rate shrinks the value of
  the losses and leaves the cash, so the fair price rises above the value range. It is a quirk of the definition, not a
  price (see the last section).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (`20c09b01`); written question by question; committed after each
      (Step 0 `b365549b`, Q1 `ac21d1a9`, the box, facts after the stop, the computation and this audit in the closing commit).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is
      the dispatcher's. Until folded, the run binds nothing.
- [x] No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened, listed or searched; what was
      seen in the session context is declared under Contamination at the top.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row
      (`scripts/check_run.py`, run before the commit); no E-ids. Every filing fact carries its accession.
- [x] The order was kept: Q1 closed the file; nothing after it is a clearance; Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (stock pay and IP licences deducted), never a net-income proxy; the sovereign
      from the Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP; the
      integrity flag in the box line.
- [x] No point-in-time anchor applies (a live run); no row is cited for a date after the run.
- [x] `tools/run.py` produced no arithmetic for this name; every figure was transcribed by hand from the filings named.
- [x] `python tools/check_framework.py` PASS before the commit (result recorded in the commit message).
- Not done, said plainly: FY2022's statements do not exist on the public record; the auditor's report and the notes on
  revenue recognition were not read; the Forms 4 and 144 were not opened; the rivals' figures are XBRL transcriptions,
  not checked against their filed statements.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The fair price breaks down when owner cash is negative.** Part VII values each end case at ten percent instead of
the long rate. With a negative stream and net cash, a higher rate makes the losses smaller in present value, so the
"fair price" rises above the value range (here $1.10 against a range of $(9.95) on the shorter base). The definition
assumes positive owner cash; for a loss-maker it reports a figure with no meaning as a price. What was done: both
figures reported as the convention yields them, the quirk named, and no substitute invented. A rule is needed, for
example "where owner cash is negative over the window, no fair price is reported". (2) **A filed window with a hole.**
Q7's five-year window and the cycle-base specific assume five filed years; FY2022 was never filed by this company, so
the window has four years. The run averaged the four and said so; the convention does not say whether to average four,
reach back to FY2020, or shorten the window. (3) **The template asks for "balance sheets over an 8 or 10 year period"** **[M2025-032]**; a company that listed in 2025 files six. The run read what exists and said what is missing; the
template could say what a short record means for the box (nothing here, since Q1 closed first). (4) `tools/run.py`
returned UNRESEARCHED for a recent filer with a single 10-K in XBRL; for such names it adds no friction relief and every
figure must be transcribed by hand.
