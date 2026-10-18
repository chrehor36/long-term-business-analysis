# Company Run: MSC Industrial Direct Co., Inc. (NYSE: MSM), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch
(commit 89a34a4e).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (MSM; also searched for MSC Industrial); not held.*

**Dispatched run.** Dispatched to a blind analyst under the canonical brief with the departure the brief states (the lines of
evidence derived by the analyst from Item 1, Item 1A and Item 7, below). Per-question pathspec commits of this file and
`Test Runs/_research 2026-10-13 MSM/` only.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check this file's name showed the
names of seven other run files and research folders dated 2026-10-13 (other companies; none about MSM); no file was opened.
(2) The session's starting context showed the subjects of the last five commits, which concern another company's run and
fold. (3) The session's memory index carries one-line summaries of project state (queue counts, a count of gate-clearers);
none names MSM. Nothing of these is used below.

**Lines of evidence chosen, and why (the brief's departure).** From Item 1 (one reportable segment; a distributor of
metalworking and MRO supplies, about 2.5 million SKUs, about 15% of sales under its own brands, 67% of sales to
manufacturing), Item 1A (cyclical customer demand; gross margin pressure from mix and cost; a "highly competitive industry,
which is evolving and consolidating" with "price transparency" from web-based rivals; debt covenants; a controlling family
with board nomination rights) and Item 7 (operating margin 8.0% in FY2025 against 10.2% in FY2024; a "web price
realignment initiative"; a receivables sale facility; restructuring every year), the lines are: **(i)** the margin and
cost record over full cycles against the rivals' own filings (the castle: Q2's tests 4, 6 and 10); **(ii)** unit volume
against price in the sales bridges (Q2 test 5); **(iii)** the receivables purchase agreement and what it does to operating
cash (Q4, Q7, Q9); **(iv)** the 2023 reclassification of the family's Class B shares and the buybacks that followed (Q5,
Q6); **(v)** the eight to ten balance sheets (Q4).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $128.67 (close 2026-10-12; `tools/run.py` live quote; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: Class A Common Stock 55,846,298 (10-Q for the quarter ended
  2026-05-30, filed 2026-07-01, accession `0001003078-26-000080`, cover as of 2026-06-17; `python Screens/cover_shares.py MSM`).
  One class only: the Class B shares were reclassified into Class A in the first quarter of FY2024 at 1.225 Class A per
  Class B (10-K FY2025, Item 1, accession `0001003078-25-000123`). Check: the 10-Q balance sheet shows 57,166,810 shares
  issued less 1,320,624 in treasury = 55,846,186 at 2026-05-30, within 112 shares of the cover. No 8-K or prospectus after
  the 10-Q changes the count (the 8-Ks of 2026-07-01 to 2026-09-08 are results, director and officer items).
- **Market cap:** $7,186M (55.846M x $128.67).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (year ended 2025-08-30), filed 2025-10-23, accession
  `0001003078-25-000123` (Items 1, 1A, 7, the cash-flow statement, the receivables, debt, reclassification and segment notes);
  10-K FY2024 `0001003078-24-000107`, 10-K FY2023 `0001003078-23-000102`, 10-K FY2021 `0001003078-21-000199`, 10-K FY2017
  `0001003078-17-000307` (MD&A margin explanations, cash-flow statements); 10-Q for the quarter ended 2026-05-30, accession
  `0001003078-26-000080` (balance sheet, cash flows, MD&A, the RPA note); proxy DEF 14A filed 2025-12-11, accession
  `0001003078-25-000174` (peer group, pay); 8-Ks `0001003078-25-000181` (RPA amendment), `0001003078-26-000006` (new CEO
  effective 2026-01-01), `0001003078-26-000050`, `0001003078-26-000064`, `0001003078-26-000078`, `0001003078-26-000091`,
  `0001003078-26-000094` (new CFO effective 2026-09-14). The FY2026 10-K is not yet filed (EDGAR index read 2026-10-13: the
  latest 10-K is the FY2025 one).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $333,717
  thousand in the filed Consolidated Statement of Cash Flows (10-K `0001003078-25-000123`), equal to the $333.7M that
  `tools/run.py` transcribed from the tagged data; FY2023's $699,582 thousand likewise.
- `python tools/run.py MSM`, **arithmetic lines only**: owner cash (OCF less stock pay less capital spending) FY2023 588.5,
  FY2024 292.4, FY2025 228.3 ($M); five-year window mean 285.6 on the capex basis. Capital spending 92.5 / 99.4 / 92.8;
  D&A 75.1 / 80.9 / 90.6; stock pay 18.6 / 18.8 / 12.6; finance-lease principal 1.0 / 0.3 / 0.2 (tagged) against the filed
  "Payments on finance lease and financing obligations" of 2.2 / 3.6 / 1.5, the filed line used below. **The FY2023 figure
  is not owner cash**: its operating cash includes a one-time $300M sale of receivables (see Q4 below and line (iii)). The
  tool's rule lines, ids and floor are not read (Part VII, The tooling).

**The balance sheets, read in Step 0 because the file closes before Q4** **[M2025-032]** (ten fiscal year-ends from the
first-filed XBRL, `tools/run.py`, accessions as it lists them; checked against the FY2025 and FY2023 filed statements;
$M):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | debt on the face | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2016-09-03 | 2,065 | 1,098 | 53 | 392 | 444 | 624 | 105 | 607 | 1,040 |
| 2017-09-02 | 2,099 | 1,225 | 16 | 472 | 465 | 634 | 110 | (partly untagged) | 1,169 |
| 2018-09-01 | 2,289 | 1,387 | 46 | 524 | 518 | 675 | 123 | (partly untagged) | 1,326 |
| 2019-08-31 | 2,311 | 1,479 | 32 | 541 | 559 | 677 | 117 | 442 | 947 |
| 2020-08-29 | 2,382 | 1,315 | 125 | 492 | 543 | 678 | 105 | 619 | 750 |
| 2021-08-28 | 2,462 | 1,151 | 41 | 560 | 624 | 693 | 102 | 786 | 532 |
| 2022-09-03 | 2,729 | 1,350 | 44 | 688 | 716 | 710 | 114 | 795 | 681 |
| 2023-09-02 | 2,544 | 1,479 | 50 | 435 | 727 | 718 | 111 | 454 | 755 |
| 2024-08-31 | 2,462 | 1,392 | 30 | 412 | 644 | 724 | 101 | 509 | 457 |
| 2025-08-30 | 2,462 | 1,388 | 56 | 423 | 644 | 724 | 85 | 486 | 433 |
| 2026-05-30 (10-Q) | 2,496 | 1,419 | 74 | 413 | 684 | 724 | 74 | 507 | 451 |

What moved and why. **Equity is flat for a decade** ($1,098M to $1,419M) while net income summed to about $2.7 billion
(FY2016 to FY2025, tagged): the earnings went out as regular and special dividends and buybacks, and retained earnings
*fell* from $1,040M to $433M (dividends and buybacks above earnings; one special dividend is read in the filings
opened, $195.4M paid in FY2021, `0001003078-23-000102`; the falls in FY2019 and FY2020 were not traced to their lines).
**Goodwill and intangibles are 33% of assets** ($809M of $2,462M) and rose by $80M over the decade from bolt-on purchases.
**Receivables fell from $688M to $435M in FY2023 while sales rose to their peak**: that is the $300M sale of receivables
under the RPA (10-K FY2025 receivables note), not faster collection; at 2026-05-30 the facility is $350M, so about $350M of
the company's receivables financing does not appear as debt on the face. Read with it, debt on the face ($486M) plus
the RPA ($350M) is about $836M against equity of $1,388M. **Inventory** rose with sales to FY2023 and was drawn down by
$85M in FY2024 (cash-flow statement). What the figures do not say: whether the receivables sold are recourse in substance
(the note says collateral of $359M was pledged and covenants match the credit facility's) **[M2025-032]**.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the distributor will earn, not where the quote goes **[M1997-109]**; the price
is read only against where the facts lead **[M2006-077]**. No macro enters: the filer's own correlation with the industrial
production index is a description of the business's cyclicality, not a forecast used here. The analyst's habit applied:
look for "what you’re missing" **[M2025-013]** and write contrary evidence down at once. **Contrary evidence, written down
as found** **[M1997-127]**: (1) FY2023 operating cash of $699.6M is inflated by a $300M receivables sale (found in Step 0
before any judgment); (2) operating margin halved from 17.5% (FY2012) to 8.0% (FY2025) while sales rose 60% (found in the
first pull of the tagged series); (3) the quarter to 2026-05-30 shows the margin recovering to 10.2%, but on price
($70.1M) not volume ($4.5M) (10-Q MD&A); (4) the family's Class B shares were exchanged at a 22.5% premium in shares, then
bought back with borrowed money (10-K FY2024).

## THE STANDING RULE
Nothing in this file asks the buyer to borrow, to give anyone a call on his cash, or to size beyond what he can lose; a
part-interest in a listed distributor bought for cash puts the buyer at no risk of ruin **[M2012-081]**, **[L2023-005]**.
The target's own debt and receivables financing are Q9's (not reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**. MSC buys from more than 3,000 suppliers (none over 5% of purchases) and
  resells about 2.5 million SKUs, 85% of them third-party brands, to machine shops, national accounts and the public sector,
  shipping the same day from five fulfilment centres (10-K FY2025, Item 1, `0001003078-25-000123`). One reportable
  segment (10-K FY2025, segment note). The economics are those of a distributor: gross margin set by what customers will
  pay over the suppliers' price, operating cost per dollar of sales, and working capital.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (a) volume, tied by the filer's own statistical
  analysis to industrial production (67% of sales to manufacturing), cyclical but not unknowable; (b) the gross margin, which
  the filer says moves with customer mix and with "price transparency" from web rivals (Item 1A); (c) operating expense per
  dollar of sales. These are about customers and rivals, not about a technology the analyst cannot follow **[M2017-019]**,
  **[M2023-030]**. The petroleum-additives row fits: the product range need not be understood, "the economic dynamics of
  the industry" must be **[M2011-014]**, and they can be read from the filings of the filer and its rivals
  **[M2008-033]**.
- **Would the insiders write the forecast down?** **[M2000-105]**: a distributor's ten-year volume, gross margin and cost
  ratio are the figures this industry's managements plan on and pay bonuses against (the proxy's bonus metrics are
  organic ADS growth and adjusted operating profit, DEF 14A `0001003078-25-000174`). The forecast is hard, not unwritable.
- **A caution written down** **[M1997-127]**: distribution is close kin to retail, of which the rows say "it’s easy to sort
  of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**; and doubt means outside
  **[M2002-092]**. The doubt here is about the castle's direction, which is Q2's question, not about whether the economics
  can be pictured at all **[M1997-148]**.
- **VERDICT: IN.** The economics of an industrial distributor can be pictured ten years out from its own and its rivals'
  filings **[M1995-051]**, **[M2000-037]**, **[M2012-065]**; whether its position will hold is put to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital"
**[L2007-004]**. The filer's own claim for its castle is service: technical metalworking specialists, vending and in-plant
programmes, same-day shipping, a broad range (10-K FY2025, Item 1). The rows allow service as an escape from the commodity
class **[M2001-014]**. The tests below ask whether the record bears the claim out.

**The competitor row** (same metric, each company's own 10-K XBRL; the 10-K names no rival, so the three SEC filers in MRO
supply are taken from the filer's own proxy peer group, DEF 14A `0001003078-25-000174`; named classes of rival not filing:
web-based e-commerce sellers, warehouse stores, manufacturers' own sales forces; peers on calendar years, MSM on years
ending late August; table in `Test Runs/_research 2026-10-13 MSM/peers_table.txt`):

| | MSM | W.W. Grainger | Fastenal | Global Industrial |
|---|---|---|---|---|
| sales, first year to FY2025 | $2,356M (2012) to $3,770M, +60%, with about $817M paid for businesses FY2013 to FY2025, $549M of it for Barnes Distribution North America in FY2013 | $8,950M to $17,942M, +100% | $3,134M to $8,200M, +162% | $792M (2017) to $1,379M, +74% |
| gross margin, 2012 / 2025 | 45.8% / 40.8% | 43.8% / 39.1% | 51.5% / 45.0% | 44.4% (2017) / 35.5% |
| operating margin, 2012 / 2025 | 17.5% / 8.0% | 12.6% / 13.9% | 21.5% / 20.2% | 9.0% (2017) / 7.1% |
| operating cost per $ of sales (gross less operating margin), 2012 / 2025 | 28.3% / 32.8% | 31.2% / 25.2% | 30.0% / 24.8% | 35.4% (2017) / 28.4% |
| operating margin at MSM's cycle peaks (FY2012, FY2018, FY2023) and the same calendar years | 17.5%, 13.1%, 12.1% | 12.6%, 10.3%, 15.6% | 21.5%, 20.1%, 20.8% | n/a, 6.9%, 7.6% |
| accessions (2025 row) | `0001003078-25-000123` | `0000277135-26-000011` | `0000815556-26-000009` | `0001628280-26-012945` |

**The tests, each with its filing fact.**
1. **Is the moat widening or narrowing?** "whether it’s likely to widen further or shrink on you" **[M1999-108]**; "Every
   day, in countless ways, the competitive position of each of our businesses grows either weaker or stronger."
   **[L2005-010]**. Over thirteen years and three cycle peaks MSM's operating margin fell 17.5%, 13.1%, 12.1%, and its
   trough years fell too (FY2021 9.3%, FY2025 8.0%) (tagged series, accessions in the table). In the same years Fastenal
   held about 20% and Grainger rose from 12.6% to 13.9% (15.6% at its 2023 peak). The fall is MSM's, not the field's. It is
   the "lost a notch" pattern, repeated, with the rivals not losing it **[L1995-023]** (cited for the test's form, not as a
   verdict on an industry).
2. **The low-cost position.** In a business whose products are mostly the same third-party brands its rivals sell (85% of
   MSC's sales, Item 1), cost against the competitor decides: "if your costs are on parity or less [...] than your other major competitors, that
   is much more important to you than the absolute level" **[M2001-013]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. In 2012 MSM spent
   28.3 cents of each sales dollar to operate, the lowest of the three; by 2025 it spent 32.8 cents (32.5% operating
   expenses plus 0.3% restructuring, 10-K FY2025 MD&A) against Grainger's 25.2 and Fastenal's 24.8. It has moved from the
   low-cost to the high-cost operator among its two largest MRO rivals. The filer's own words name the threat: rivals "with
   new lower-cost business models are able to operate with lower prices and gross profit on products" (Item 1). "sooner or
   later, the nature of a capitalist society is that the guy with the lower cost comes in and kills you." **[M2001-013]**;
   "you do not want to have something whose competitive position is going to erode over time." **[M2007-117]**.
3. **Pricing power, and the agony before a price rise** **[M2005-020]**. The gross margin fell five points in thirteen years,
   and the filer explains the steps by price and mix: FY2016 and FY2017 "changes in pricing and customer and product mix"
   (10-K FY2017 `0001003078-17-000307`); FY2023 large public-sector sales "below our typical public sector customer margins"
   and national account and public sector growth "at lower gross margins" (10-K FY2023 `0001003078-23-000102`); FY2024
   "discounting during the launch of our web price realignment initiative" (10-K FY2024 `0001003078-24-000107`); and the
   strategy itself: "we strategically adjust our customer pricing to maintain competitiveness" (10-K FY2025, Item 1). A web
   price cut to stay level with transparent online prices is the business whose price a competitor sets **[M2012-109]**.
   For the business: the quarter to 2026-05-30 passed tariff costs through, $70.1M of price and a gross margin of 41.1%
   against 41.0% (10-Q `0001003078-26-000080`), and "businesses with strong competitive positions manage to pass through
   increases in raw material costs" **[M2005-017]**; but every rival in the row passes the same tariffs through, so it does
   not separate MSM from them.
4. **Unit volume** **[M1999-054]**. Volume in the filer's own sales bridges: FY2023 +$136.0M, FY2024 −$239.1M, FY2025
   −$88.1M, and +$4.5M in the latest quarter on $971M (10-Ks FY2023 to FY2025, 10-Q Q3 FY2026). Over FY2023 to FY2025 volume
   fell about $191M net while Grainger's sales rose in calendar 2024 and 2025 and Fastenal's rose 8.7% in 2025 (their 10-Ks,
   the table). Over the whole span MSM grew sales 60% with about $817M of purchased businesses; Fastenal grew 162% and
   Grainger 100%.
5. **Would the customer still choose it over the low bid?** **[M2017-009]**. The 10-K says purchasing decisions "are based
   primarily on one or more of the following criteria: price, product selection, product availability, technical support
   relationship, level of service and convenience" and that online rivals compete "with price transparency" (Item 1). The
   customer types growing fastest (national accounts, public sector) are the ones the filer says buy at lower margins; core
   customers fell $145.7M in FY2024 and $45.5M in FY2025 (10-Ks). The service is real (29,611 vending machines and 411
   in-plant sites at FY2025, 10-K MD&A), but the record shows customers taking a lower price as the service grew: the failing
   answer, a product "that has a whole bunch of competitors" **[M2023-074]**.
6. **The money test** **[M2011-015]**. A competitor with money has already done it: Grainger and Fastenal, each larger,
   each now with the lower cost per sales dollar, and web sellers the filer describes but does not name. The filer says
   "new entrants in the MRO supply industry could increase competition" (Item 1). No barrier is named in the filing beyond
   service and range, which the rivals also offer.
7. **What could destroy or reduce it in five to fifteen years** **[M2000-014]**: the price transparency the filer names, and
   consolidation that "could cause the industry to become more competitive (i) as greater economies of scale are achieved by
   competitors" (Item 1). Both are already in the record above, not forecasts.
8. **Change for the better?** The latest quarter's 10.2% operating margin (10-Q) and a new chief executive from 2026-01-01
   (8-K `0001003078-26-000006`) are not credited: a change for the better is credited only on the evidence of a full cycle
   **[M2005-020]**, **[L1995-022]** (the framework's Q2 convention), and one quarter on price is not one.

**The field's returns over the last full cycle**, judged in words (Q2's CONVENTION, no figure): the field's durable
leaders earn excellent returns, Fastenal about 20% of sales as operating profit on little debt and Grainger rising, so this
is not a field of ordinary returns where the question would close on the field; it closes on MSM's own position in it.

**Where it stands.** The castle question is asked from the attacker's side **[M1995-038]**, and here the attack is not
hypothetical: across three cycles the filer went from the low-cost operator to the high-cost one against its two largest
rivals, its margin halved while theirs held or rose, its volume fell while theirs grew, and it cut web prices to stay
level. A castle being filled in on the evidence closes OUT **[M2011-015]**. It is not TOO HARD: the future is not unknown
here, the last three cycles show the direction, read from the filings, "The figures are available." **[M2009-059]**. Price
does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **The parts table:** not needed; one reportable segment (10-K FY2025, segment note).
- **VERDICT: OUT.** The castle is shown on the evidence to be narrowing: margin halved over three cycles while the two
  largest rivals held theirs, the low-cost position lost, prices set against transparent web rivals **[M1999-108]**,
  **[M2001-013]**, **[M1997-010]**, **[M2012-109]**, **[M2011-015]**.

## Q3 to Q12: NOT REACHED
Q2's STOP closed the file OUT (operator rule 2). Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are not answered. Figures below
are facts found, not weighed, and computation, not clearance.

---
## THE BOX
**OUT, at Q2** (the castle shown narrowing on the evidence over three cycles against the two largest rivals' own filings);
integrity facts recorded, not judged (the 2023 reclassification, below under Q5 and Q6). COMPUTATION, NOT A CLEARANCE:
value range $74.08 to $84.75 a share (all-equity basis) against $128.67; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).

**Bearing on Q3 (capital).** Operating income was $412M in FY2012 and $302M in FY2025 while about $817M was paid for
businesses (tagged series; cash-flow statements). Capital spending doubled from about $50M a year (FY2017 to FY2021) to
$92M to $99M (FY2023 to FY2025), "mainly related to vending programs and other infrastructure and technology investments"
(10-K FY2025 MD&A); depreciation and amortization rose from $68.8M (FY2021) to $90.6M (FY2025).

**Bearing on Q4 (the accounts).** (a) The receivables purchase agreement: $300M of receivables sold in the second quarter
of FY2023 and derecognised, raised to $350M in December 2025 (8-K `0001003078-25-000181`; 10-Q note); collateral pledged
$359.5M at FY2025; covenants "substantially the same" as the credit facility's; fees of $12.2M, $18.4M and $15.8M (FY2023
to FY2025) sit in other expense, below operating income (10-K FY2025 receivables note). The sale put $300M into FY2023's
operating cash ($699.6M filed) and $50M into FY2026's; the 10-Q says the RPA "is a key component" of the company's
liquidity and its proceeds "were utilized to pay down existing debt". (b) Restructuring and other costs every year:
$7.9M (FY2023), $14.5M (FY2024), $11.0M (FY2025), $7.3M (nine months of FY2026), with a $30.1M PPE inventory write-down and
$16.3M of lease and asset impairments in FY2021 (10-Ks). (c) The proxy's bonus metrics are "adjusted operating profit" and
organic ADS growth, and the three-year share award runs on "average adjusted return on invested capital" (DEF 14A
`0001003078-25-000174`). No adjusted figure is featured in the 10-K's MD&A read. (d) Expenditures for cloud computing
arrangements ($20.3M in FY2024) are charged inside operating cash, not in capital spending (cash-flow statement).

**Bearing on Q5 and Q6 (integrity facts, recorded, not judged).** (a) In the first quarter of FY2024 each of the 8,654,010
Class B shares (ten votes each, held by the Jacobson and Gershwind family) was exchanged for 1.225 Class A shares (10-K
FY2024, Item 1 and the equity note, `0001003078-24-000107`; 10-K FY2023 balance sheet for the count): about 1.95 million
more shares for the family than one-for-one, where the charter's own conversion had been one-for-one on transfer. (b) The
company then bought back $187.7M of stock in FY2024, which "included shares purchased to offset the share dilution
resulting from the Reclassification", and its borrowings rose "primarily to fund" that buying (10-K FY2024 MD&A). (c) The
Reclassification Agreement gives the family the right to designate two board nominees while it holds 10% or more (10-K
FY2025, Item 1A). (d) The chief executive in FY2025 was a family member, Erik Gershwind; his FY2025 non-equity incentive
was $1,425,750 in a year operating income fell 22.8%, the bonus measured against "our fiscal year 2025 operating plan"
(DEF 14A). A new chief executive took office on 2026-01-01 (8-K `0001003078-26-000006`); the chief financial officer left
in August 2025 and the interim served to 2026-09-14 (8-K `0001003078-26-000094`); the general counsel resigned in April 2026
(8-K `0001003078-26-000064`). The test these bear on is how the managers "treat themselves versus how they treat the
shareholders" **[M1994-009]**; any later run that reaches Q5 must answer them.

**Bearing on Q6 (buybacks).** The repurchase plan of June 2021 is for up to 5,000,000 shares, "no expiration date", "at
any time and in any increments it deems appropriate"; no price is named (10-K FY2025, Item 5 and equity note), the case
**[L2016-002]** describes. Repurchases: $95.8M (FY2023), $187.7M (FY2024), $39.3M (FY2025), $13.9M (nine months FY2026).
Regular dividends $189.7M in FY2025 against net income of $199.3M.

**Bearing on Q9 (debt).** Debt on the face $506.8M and cash $74.1M at 2026-05-30 (10-Q), so net debt $432.7M, plus the RPA
of $350M; $100M of long-term debt maturing in FY2026 (10-K FY2025 obligations table); revolving facility unused
$543.7M at 2025-10-02 (10-K FY2025 MD&A).

**COMPUTATION, NOT A CLEARANCE** (the reporting figures the owner asked for; Q7 was not reached and nothing here is a
verdict or entry language; script and output in `Test Runs/_research 2026-10-13 MSM/value.py` and `value_output.txt`).

*Inputs.* Five-year window FY2021 to FY2025, filed cash-flow statements (10-K FY2025 for FY2023 to FY2025, 10-K FY2023 for
FY2021 and FY2022). The window runs trough to trough (operating margin 9.3% in FY2021, the PPE write-down year, and 8.0% in
FY2025, "soft demand"), so it is itself one full cycle and the literal window serves as the cycle base (specific (a)).
Owner cash, all spending = operating cash less the $300M RPA sale in FY2023, less stock pay, capital spending, cash paid for
businesses and finance-lease payments: FY2021 $128.4M, FY2022 $105.2M, FY2023 $266.1M, FY2024 $264.8M, FY2025 $226.0M;
average **$198.1M** (working capital counted, specific (d)). Maintenance case (specific (e); the filing gives no split, so the
guess is depreciation, $57.2M to $72.1M a year, against capital spending of $53.7M to $99.4M, "almost always true costs"
**[L2015-004]**; no purchases, since a business that buys no growth spends nothing to buy it): average **$240.6M**. Company's
own tax (cash taxes inside operating cash; no carryforwards found). All-equity basis adds back interest paid after the
filer's 25% effective rate: $15.3M a year. Net debt $432.7M at 2026-05-30 (borrowings and finance leases $506.8M less cash
$74.1M; operating leases left out). Shares 55.846M. Sovereign 5.60%.

**CONVENTION of this run (the RPA).** The framework's inventory-secured trade finance convention (Q7) is extended to
receivables sold under a revolving purchase agreement whose fees are charged inside owner cash: the $350M is treated as
working capital, not net debt, and the one-time $300M inflow of FY2023 is removed from that year as an aberrational year
tied to one event (specifics (a) and (d)); the figures with the RPA counted in net debt and its fees added back as interest
are shown beside. Rationale: the cost is charged once, where the business pays it, and the sale itself is financing, not
earnings, so leaving it in would credit a borrowing as owner cash.

*Growth.* Owner cash end to end grew 15.2% a year, a figure made by working-capital swings (the first half averaged $116.8M,
the second $245.4M); carried ten years it would put owner cash at 14.8% of sales, above the highest share the filings read
show (10.4% in FY2016 and FY2020), so the cap (specific (f)) cuts it to the business's own sales growth over the window,
**3.83%** (FY2021 $3,243M to FY2025 $3,770M, acquisitions deducted so total growth credited, specific (c)). Purchases over the
window were $124.8M against owner cash before purchases of about $1,115M, so not a serial acquirer. Ten years, then zero
nominal growth.

| case (all-equity, per share, less net debt) | value at 5.60% | expected return at $128.67 |
|---|---|---|
| no growth, maintenance only (bottom) | **$74.08** | 3.4% |
| 3.83% growth, all spending (top) | **$84.75** | 3.9% |
| beside: no growth, all spending | $60.49 | |
| beside: 3.83% growth, maintenance only (the most generous case built) | $103.17 | 4.6% |
| beside: equity-only pair | $76.94 to $85.87 | 3.4% to 3.8% |
| beside: RPA counted as debt, fees added back | $70.03 to $81.49 | |
| beside: the literal window with the RPA inflow left in | $79.67 to $110.75 | 3.6% to 4.9% |

**(a) VALUE RANGE: $74.08 to $84.75 a share** (all-equity basis, central) against **$128.67**; equity-only $76.94 to $85.87.
The floor is tested first: no case in the range, nor any case beside it, earns about ten percent at the price (the highest,
4.6%), so the computation would close OUT whatever the width: "there’s just a point at which we drop out of the game"
**[M2003-149]**; the width is 1.14 to one. The price sits above the top of every case.

**(b) FAIR PRICE: $39.99 a share** on the all-equity basis (each end valued at ten percent, the two averaged, less net debt),
after the company's own tax; **$44.59** on the equity-only basis beside it; $35.16 with the RPA counted in net debt.
(Part VII; no cheap price is reported.)

*What the latest quarter does to it.* Trailing twelve months to 2026-05-30, operating cash was $305.7M including the $50M
RPA increase (10-K FY2025 less the nine months of FY2025 plus the nine months of FY2026, 10-Q), so $255.7M without it,
below FY2025's $333.7M; it would not raise the range.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 89a34a4e); written question by question; committed after Step 0 to
      Q1 (99ee49c6) and after Q2 (92c8c4f8), and after this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the fold is
      the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. A listing of `Test Runs/` to check this
      file's name showed other runs' file names (none about MSM), and the starting context showed recent commit subjects
      and memory lines; declared under contamination, not used.
- [x] Every v5 id resolves (`check_ids.py` in the research folder: no E-ids, every id in `principle_ledger_v5.csv`, every
      quoted fragment beside an id found in that row); every filing fact has its accession; the peer figures carry theirs.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the computation is headed so.
- [x] Owner cash after every real cost (stock pay, all capital spending, purchases, finance leases, working capital),
      never a net-income proxy; the RPA's one-time inflow removed and confessed; the sovereign from the Treasury; the price
      flagged as an aggregator quote.
- [x] Contrary evidence written down as found (the foundations paragraph, four items); facts for later questions under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no row was rejected for date.
- [x] Only the arithmetic lines of `tools/run.py` were used; its FY2023 owner-cash figure was not used as owner cash.
- [x] `python tools/check_framework.py` PASS before the closing commit (run 2026-10-13: PASS, no phantom id in any run file); `check_ids.py` 43 ids, 0 bad.
- Gaps owned: the falls in retained earnings in FY2019 and FY2020 were not traced to their lines; the peer companies'
  margins are from their tagged data, cross-checked to no filed statement of theirs; Amazon Business and other web rivals
  are not in the competitor row because the 10-K does not name them and their MRO results are not separately filed.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Rivals when the 10-K names none.** The brief says to take the rivals the 10-K names; this 10-K names
classes of rival and no company. The proxy's compensation peer group was used, cut to the three SEC filers in MRO supply,
and said so; neither the framework nor the template says where to go when the filer names nobody, and a peer group chosen
for pay is not the filer's statement of who it competes with. (2) **Receivables sold.** The framework's net-debt definition
("borrowings and finance leases less cash and securities, as the filing states them") leaves out a $350M receivables
facility that the filing treats as a sale but whose covenants are the credit facility's, and nothing in Q4 or Q7 says what to
do with the one-time operating-cash inflow when such a facility starts. The inventory-secured trade finance convention was
extended by analogy and confessed as this run's CONVENTION, with the debt-counted figures beside; a ruling would make runs
of other factoring companies comparable. (3) **"Shown open" against "lost a notch."** Q2 closes OUT on a castle "filled in on
the evidence" and TOO HARD on one whose future cannot be judged, but the rows also carry a business that "retains its
excellent economics, but has lost still another notch" **[L1995-023]**, which a reader could take as narrowing short of
open. This run read a halving of margin over three cycles, with the two largest rivals holding theirs and the cost position
reversed against them, as shown filling in; the framework gives no test that separates a castle losing notches from one
being filled in, and another analyst could weigh the same record as TOO HARD (NATURE) on the question of whether the new
management's service and pricing actions will hold the line. The computation makes the choice moot at this price, which is
recorded only so that the box is not read as depending on it.
