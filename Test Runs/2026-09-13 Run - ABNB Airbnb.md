# Company Run — Airbnb, Inc. (ABNB) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run history: WAVE 5 of `Screens/WATCHLIST RUN QUEUE.md` (skip reason from the 2026-09-01 triage:
"capex unresolved [E5-20]: build (c) by hand from the filing"). Created under the write-early
protocol; research in `Test Runs/_research 2026-09-13 ABNB/`. The brief was read as a set of
hypotheses and the skip reason as UNLABELLED: nothing in it says which gate will be short.*

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, THE COVER, AND THE FILING

### The sovereign, for the currency the business EARNS in **[E4-15, E3-32]**
- rate **5.35 %** · date **09/11/2026** · source **US Treasury daily par yield curve, 30-year
  (issuing authority), struck this session via `python tools/sources.py`** — not inherited from
  the brief, which quoted the same figure; not the FRED fallback.
- FX: none for the quote. Reporting currency USD (FY2025 10-K Note 2: *"The Company's reporting
  currency is the U.S. dollar"*). **But the earnings are not a US-dollar stream in substance**:
  revenue by listing location 2025 was North America $5,196M (42%), EMEA $4,729M (39%), Latin
  America $1,160M (10%), Asia Pacific $1,156M (9%) of $12,241M; the US alone $4,814M (39%). The
  sovereign stays the USD 30-year because that is the currency the reported owner earnings are
  denominated in; the currency exposure is a Q4 item (the 2025 FX hedge reclassification took
  $64M out of revenue; FX translation added $655M to cash in 2025 and took $237M in 2024).

### The cover count, by hand **(operator rule 4; the tool refuses the judgment and is right to)**

`python Screens/cover_shares.py ABNB`:

    10-Q filed 2026-08-06, period 2026-06-30, accession 0001559720-26-000027
    Common Class A        419,529,556
    Common Class B        170,056,126
    Common Class C                  0
    Common Class H          9,200,000
    --- arithmetic sum, NOT a share count ---   598,785,682
    MULTIPLE CLASSES. ... READ THE FILING.

The 10-Q cover itself, verbatim: *"As of July 15, 2026, 419,529,556 shares of the registrant's
Class A common stock were outstanding, 170,056,126 shares of the registrant's Class B common stock
were outstanding, no shares of the registrant's Class C common stock were outstanding, and
9,200,000 shares of the registrant's Class H common stock were outstanding."*

**The charter description, from the filing (FY2025 10-K `0001559720-26-000004`, Note 11 and
Note 15), verbatim:**
- *"Class A common stock is entitled to one vote per share and Class B common stock is entitled to
  20 votes per share. One share of Class B common stock is convertible into one share of Class A
  common stock voluntarily at any time by the holder, and will convert automatically into one
  share of Class A common stock upon the earlier of (a) the date and time, or the occurrence of an
  event, specified by vote or written consent of the holders of at least 80 % of the outstanding
  shares of Class B common stock ... and (b) the 20 -year anniversary of the closing of the IPO."*
- *"The rights, including the liquidation and dividend rights, of the holders of Class A and Class
  B common stock are identical, except with respect to voting and conversion. ... the resulting net
  income per share attributable to common stockholders will, therefore, be the same for both Class
  A and Class B common stock on an individual or combined basis."*
- *"Each share of Class C common stock is entitled to no votes and will not be convertible into any
  other shares of the Company's capital stock. Each share of Class H common stock is entitled to no
  votes and will convert into one share of Class A common stock on a share-for-share basis upon the
  sale of such share of Class H common stock to any person or entity that is not the Company's
  subsidiary."*
- Item 5: *"Class H common stock: All outstanding shares were held by our wholly-owned Host
  Endowment Fund subsidiary."*
- The balance sheet (10-Q, June 30, 2026): *"Class H - authorized 26 shares; 9 shares issued and
  zero shares outstanding"*; Class A *"420"*, Class B *"170"* issued and outstanding (millions).

**DECISION.**
1. **Class A and Class B are economically identical and are summed**: identical dividend and
   liquidation rights on the filing's own words, 1:1 conversion, one EPS figure. The difference is
   twenty votes, not money — a Q3 finding, not a count adjustment.
2. **Class H (9,200,000) is EXCLUDED.** It is held by a wholly-owned subsidiary, carries no votes,
   is shown on the balance sheet as *"issued and zero shares outstanding"* and is outside the EPS
   denominator. It is the economic equivalent of treasury stock until sold to a non-subsidiary, at
   which point it converts to Class A. The cover calls it "outstanding"; the balance sheet does not;
   **the balance sheet governs the economics.** Recorded as a latent dilution of 9.2M shares (1.6%),
   not counted.
3. **Class C: zero.** No preferred issued.
4. **Count: 419,529,556 + 170,056,126 = 589,585,682 economic shares** (as of 2026-07-15), agreeing
   with the balance sheet's 590M at 2026-06-30. `run.py`'s 623.0M was the **FY2025 diluted
   weighted average** — a denominator 5.7% above the cover count, which the tool itself warned.
5. **Not counted, and stated:** at 2025-12-31, 5M options (WAEP $108.28) and 32M RSUs outstanding,
   plus *"RSUs to be settled in 9.6 million shares of Class A common stock"* subject to unmet market
   conditions (Note 15). The 0% 2026 convertible notes were repaid in cash on 2026-03-15
   (10-Q: *"Principal repayment of long-term debt | ... | ( 2,000 )"*), so no conversion shares.

### The price and cap
- **US$170.19**, Nasdaq close **2026-09-11**, via `tools/sources.py:price()` (Yahoo chart
  endpoint — **aggregator, flagged, live quote only**). `split_factor_after('ABNB','2026-07-15')` =
  1.0 (the only split on record is the pre-IPO 2-for-1 of 2020-10-26).
- **Cap: 170.19 × 589,585,682 = US$100,341.6M.**

### The filing was read — not tagged data **[E3-27]**
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary documents read** (all from EDGAR, saved as text in the research folder):
  - **FY2025 10-K, filed 2026-02-12, accession `0001559720-26-000004`** — Items 1, 1A (regulation),
    5, 7 in full, 8 in full (all 16 notes and Schedule II).
  - **10-Q Q2 2026, filed 2026-08-06, accession `0001559720-26-000027`** — cover, statements, notes,
    MD&A.
  - **FY2024 10-K `0001559720-25-000010`; FY2023 `0001559720-24-000006`; FY2022
    `0001559720-23-000003`; FY2021 `0001559720-22-000006`; FY2020 `0001559720-21-000010`** — cash-flow
    statements, MD&A key metrics, FCF reconciliations, SBC notes.
  - **424B4 prospectus, 2020-12-11, `0001193125-20-315318`** — the 2017-2019 history and the 2020
    collapse.
  - **DEF 14A, filed 2026-04-24, `0001193125-26-175062`** — ownership, voting power, pay.
  - **8-K 2026-03-16 (`0001193125-26-108514`, Items 1.01/2.03/8.01)** — opened because `deal_note`
    flagged one Item 1.01 with no EX-2.1. **It is a debt offering, not a deal**: *"$2.5 billion
    aggregate principal amount of senior notes, consisting of $850.0 million ... 4.400% Senior Notes
    due 2029 ..., $850.0 million ... 4.650% Senior Notes due 2031 ..., and $800.0 million ... 5.250%
    Senior Notes due 2036"*, closed March 16, 2026; exhibits are the underwriting agreement (1.1),
    indentures (4.1, 4.2) and legal opinion (5.1). Nothing pending: no 425, DEFM14A, S-4 or tender
    form in the submissions index since the 10-K. **The quote is an owner-earnings price, not a
    spread.** `name_change_note` returned nothing; the one "former name" in the submissions JSON is
    *"Airbnb, Inc."* itself (2012-10-24 to 2026-09-03) — SEC bookkeeping, as the brief said.
  - **8-K EX-99.1 shareholder letters**: Q2 2026 (`0001193125-26-337928`), Q4 2025
    (`0001193125-26-048670`), Q4 2024 (`0001193125-25-026054`), Q4 2023 (`0001193125-24-033706`) —
    read for [E4-29] and [E4-22] before Q3 is scored (the CGNX companion rule). **Most of each letter
    is rendered as JPG images**; only the text layer and tables were machine-readable. Flagged as a
    source limit at Q3.
- **Figure cross-checked against the filed statement:** **net cash provided by operating activities
  FY2025 = $4,646M** — filed statement (10-K p. 53, *"Net cash provided by operating activities |
  3,884 | 4,518 | 4,646"*) equals the companyfacts `NetCashProvidedByUsedInOperatingActivities`
  value (4,646.0) and the MD&A table. **Second check, and it found a restatement:** FY2020 OCF is
  **-$629.7M in the FY2020 10-K** (*"Net cash provided by (used in) operating activities | 595,557 |
  222,727 | (629,732)"*, in thousands) and **-$740M in the FY2022 10-K**; financing moved the other
  way (*"Taxes paid related to net share settlement of equity awards"* -$1,650.5M → -$1,527M;
  funds payable -$1,012.1M → -$1,024M). About $110M was reclassified from financing into operating
  cash. **This run uses the newest vintage (-$740M)**, which is also what companyfacts carries.

### THE TAG GAP THE TRIAGE SKIPPED ON — tested, and it is REAL, and it is a PRESENTATION change
The triage's `run.py` row priced only 2020-2022 because `PaymentsToAcquirePropertyPlantAndEquipment`
ends at FY2022 in companyfacts. **The filing shows why:**
- FY2020, FY2021, FY2022 10-Ks carry *"Purchases of property and equipment"* as its own investing
  line: **$37M, $25M, $25M** (2019: $125.5M).
- **From the FY2023 10-K on, the line is gone from the face of the cash-flow statement** and folded
  into *"Other investing activities, net"* (the FY2023 10-K restates 2022's "other" from -$2M to
  -$27M). **The capex figure survives only in the MD&A's non-GAAP FCF reconciliation**:
  *"Purchases of property and equipment | (25) | (47)"* (2022, 2023; FY2023 10-K) and *"(34) |
  (33)"* (2024, 2025; FY2025 10-K).
- **And it is negligible**: $33M on $12,241M of revenue in 2025 is **0.27%**. Capitalised
  internal-use software sits inside it (Note 8: *"Capitalized software development costs are
  classified as property and equipment"*; amortisation $13M / $34M / $61M in 2023-25; net carrying
  value $69M → $33M). Property and equipment, net, is **$107M** on $22.2bn of assets.
- **So the [E5-20] label was wrong for this name.** The corpus's exception class is the business
  whose own filing says depreciation understates renewal. Airbnb's D&A ($91M in 2025) runs **above**
  its capex ($33M) — the D&A end is the **conservative** end here, the opposite of a railroad. The
  real renewal costs of this business are expensed (data hosting: a *"commercial agreement with a data
  hosting services provider to spend or incur an aggregate of at least $1.7 billion for vendor
  services through 2031"*; product development $2,354M) or run through operating working capital
  (*"web hosting prepayments"* inside prepaids and other assets). (c) is built by hand at Q4.

**Nothing blocked on the evidence ladder**: SEC XBRL and EDGAR primary documents were both reached.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words
A traveller pays Airbnb the whole price of a stay up front (or in instalments). Airbnb keeps a fee
and pays the rest to the owner of the home the business day after check-in. **It owns no rooms,
bears no inventory, and sets no prices** (FY2025 10-K Note 2: *"It does not fulfill rental promises,
bear inventory risk, or set prices. Therefore, revenue is presented on a net basis"*). Revenue is the
fee, recognised at check-in.

**Every figure below is from the 10-Ks (MD&A key metrics) and the 424B4; take rate = revenue ÷ GBV,
my arithmetic (`_research .../q1calc.py`).** GBV is *"inclusive of host earnings, service fees,
cleaning fees, and taxes"*.

| year | revenue $M | GBV $M | **take rate** | nights & experiences/seats booked (M) | GBV per night $ | revenue per night $ |
|---|---|---|---|---|---|---|
| 2016 | 1,656 | 13,925 | 11.89% | 125.7 | 110.8 | 13.17 |
| 2017 | 2,562 | 20,975 | 12.21% | 185.8 | 112.9 | 13.79 |
| 2018 | 3,652 | 29,441 | 12.40% | 250.3 | 117.6 | 14.59 |
| 2019 | 4,805 | 37,963 | 12.66% | 326.9 | 116.1 | 14.70 |
| **2020** | **3,378** | **23,897** | 14.14% *(timing: revenue at check-in, GBV at booking net of cancellations)* | **193.2** | 123.7 | 17.48 |
| 2021 | 5,992 | 46,877 | 12.78% | 300.6 | 155.9 | 19.93 |
| 2022 | 8,399 | 63,212 | 13.29% | 394 | 160.4 | 21.32 |
| 2023 | 9,917 | 73,252 | 13.54% | 448 | 163.5 | 22.14 |
| 2024 | 11,102 | 81,784 | 13.57% | 492 | 166.2 | 22.57 |
| 2025 | 12,241 | 91,273 | 13.41% | 533 | 171.2 | 22.97 |
| Q2 2026 | 3,608 | 27,247 | 13.24% (letter: *"implied take rate ... of 13.2% was in-line with Q2 2025"*) | 148.3 | 183.7 | — |

Sources: FY2020 10-K (2016-2020 metrics; 2018-2020 revenue), 424B4 `0001193125-20-315318` (2015-2017
revenue: *"Revenue | $ 919,041 | $ 1,655,576 | $ 2,561,721"*, thousands), FY2022-FY2025 10-Ks, Q2 2026
EX-99.1. The metric was renamed *"Nights and Experiences Booked"* → *"Nights and Seats Booked"* when
services launched in 2025; the 10-K says *"Substantially all of the bookings on our platform to date
have come from nights."*

**Revenue by region 2025** (listing location, 10-K Note 3): North America $5,196M (42%), EMEA $4,729M
(39%), Latin America $1,160M (10%), Asia Pacific $1,156M (9%). **Nights by region 2025**: North America
158M (+3%), EMEA 215M (+7%), Latin America 90M (+18%), Asia Pacific 70M (+15%). North America nights
were 75.5M in 2020, 114.0M in 2021, 133M in 2022, 146M in 2023, 154M in 2024, 158M in 2025 — **the
largest-revenue region's physical growth has slowed to 3% while its revenue grew 4%** (a units reading
[E4-55], carried to Q2). *"no single city represented more than 2% of our revenue"* (2025).

**The fee.** Historically *"a split-fee structure, charging service fees as a percentage of the booking
amount to both hosts and guests. In October 2025, the Company began transitioning to a single-fee
structure, charging only the host a service fee"* (Note 2). The Q4 2025 letter (`0001193125-26-048670`)
gives the numbers the 10-K does not: hosts on the split model *"paid a 3% fee and guests paid a separate
service fee"*, migrating *"to a 15.5% single service fee"*; the Q2 2026 letter: *"In July, we announced
plans to migrate most of the remaining hosts to a single 15.5% service fee, with migration expected to be
completed this year. Hosts are able to adjust their prices to maintain the same net earnings."* **The
guest-fee percentage under the split model is not stated in any document read** (searched the 10-Ks, the
424B4 and the letters for "guest fee" and "service fee ... %"); Q1 does not need it, because the
realised blend is the take rate above.

**Where the money goes (2025, 10-K Note 16 significant segment expenses; % of revenue my arithmetic):**
merchant fees and chargebacks $1,666M (13.6%) · **stock-based compensation $1,592M (13.0%)** · salaries
and benefits $2,009M (16.4%) · marketing $1,704M (13.9%) · professional and third-party services $1,218M
(10.0%) · non-income taxes $305M (2.5%) · other $1,203M (9.8%) → **income from operations $2,544M
(20.8%)**.

**The second way it makes money is the money it holds.** Interest income was **$721M / $818M / $705M**
in 2023-25 — **34.3% / 24.6% / 22.5% of pre-tax income** — *"interest earned on our cash, cash
equivalents, marketable securities, and amounts held on behalf of customers"*. It holds its own $11.0bn of
cash and short-term investments (2025), **$6,959M of guests' money owed to hosts** (2025 year-end;
**$12,224M at 2026-06-30**, the seasonal peak) and **$1,743M of its own fees collected before check-in**
(unearned fees; $2,831M at 2026-06-30). The customer-funds separation is done at Q4.

### The 2020 collapse and recovery, from the filings
FY2020 10-K MD&A, verbatim: *"In 2020, we had 193.2 million Nights and Experiences Booked, a 41% decrease
from 326.9 million ... The decline in 2020 was most severe in the second quarter, with Nights and
Experiences Booked declining 67% from the prior year period, and our business improved from those levels
in the third and fourth quarters with declines of 28% and 39%"*; *"our GBV was $23.9 billion, a 37%
decrease from $38.0 billion in 2019"*. Revenue fell 29.7% to $3,378M. **Recovery: GBV and revenue passed
2019 in 2021 ($46.9bn, $5,992M); nights passed 2019 only in 2022 (394M against 326.9M).** The recovery
ran on price and mix: GBV per night $116 (2019) → $156 (2021), *"a significant geographic mix shift
towards bookings in North America, entire homes, and non-urban destinations, all of which tend to have
higher average daily rates"* (FY2021 10-K). 2020 also carried the IPO (December 2020, $68.00 a share), a
term loan with warrants, and **$2.8bn of stock compensation for pre-IPO RSUs whose liquidity condition
was met at the IPO** — so 2020's reported figures describe the pandemic and the listing at once.

### The scarce input this business controls
**A two-sided list of private homes that are not hotel rooms, and the guests who come to it without
being paid for.** The supply is not owned (hosts have *"no obligation to make them available to guests
for specified dates"*, FY2022 10-K) and is *"often cross-listed"* (FY2025 10-K) — so the scarce thing is
not the homes but **the concentration of guest demand arriving directly**: *"approximately 91% of all
traffic to Airbnb coming through direct or unpaid channels during the nine months ended September 30,
2020"* (424B4). **That figure is not repeated in any later filing read**; the FY2025 10-K says only that
*"the strength of Airbnb's brand and our communication strategy has allowed us to maintain lower reliance
on paid marketing channels."* Whether the scarce input is still scarce is the Q2 question, not a Q1 one.

### Will the fundamentals look broadly the same in ten years?
**The mechanism, yes; the product perimeter is being deliberately widened.** A fee on stays booked
through a trusted marketplace was the business in 2016 and is the business in 2025 (take rate 11.9% →
13.4%; *"Substantially all of our revenue comes from stays"*). Management is adding services (*"grocery
delivery, car rentals, airport pickups, and luggage storage"*), relaunched experiences and **hotels**
(*"hotel nights booked grew approximately three times as fast as our homes business"*, still *"a
single-digit percentage of nights booked"*, Q2 2026 letter), and is rebuilding the fee from split to
single. None of these changes how the money is made; all of them are carried as Q2/Q3 facts.

### What is understood as a mechanism but not yet sized **[E3-31]**
- **Taxes on the platform are a running cost of the model, not a one-off**: Italy €576M + €139M + €179M
  settled for 2017-2023 ($621M + $150M + $186M); host withholding-tax reserves $199M with $150-160M more
  reasonably possible; lodging-tax reserves $114M; a Spanish fine proposal of €65M; and the IRS Notice of
  Deficiency on the 2013 intellectual property sale claiming **$1.3bn plus penalties and interest**, which
  the 10-K says *"exceeds the current reserve recorded in its consolidated financial statements by more
  than $1.0 billion."* The mechanism is plain (the platform is being made tax collector and taxpayer in
  *"approximately 33,000 jurisdictions"*); the size is carried to Q4.
- Nothing in the revenue model requires months of study **[E4-46]**.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *A marketplace fee of about 13% of bookings, plus interest on held cash, with a decade of filed units
  and a filed collapse and recovery. Nothing in this IN carries "unverified" or "provisional": every
  figure above is from a named filing.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by
> its customers to have no close substitute and; (3) is not subject to price regulation. The existence of all
> three conditions will be demonstrated by a company's ability to regularly price its product or service
> aggressively and thereby to earn high rates of return on capital."* — **[E3-03]**, 1991

**Airbnb has two sets of customers and the test is run on both** (its own filing: *"hosts and guests
(collectively referred to as 'customers')"*).

### Criterion (1) — needed or desired: **[x] YES.**
533M nights and seats booked in 2025, $91.3bn of GBV, *"over 5 million hosts"* and *"over 9 million active
listings"* (Q4 2025 letter). Recovered past 2019 GBV within one year of the pandemic.

### Criterion (2) — thought by its customers to have no close substitute: **[ ] NO, on the filed record, on both sides.**

**Hosts: they list elsewhere, and the filings of three companies say so.**
- Airbnb, FY2025 10-K: *"Hosts have numerous options for listing their spaces, experiences, and services, both
  online and offline, and often cross-list their offerings."* · *"Numerous companies offer homes for booking,
  often cross-listed on multiple platforms, which can make our pricing appear less competitive for a number of
  reasons, including differences in fee structure and policies. Some property managers and hosts encourage
  direct bookings, bypassing our platform"*. The 424B4 (2020) said it before the IPO: *"It is also common for
  hosts to cross-list their offerings"*; *"Some of our hosts have chosen to cross-list their properties, which
  reduces the availability of such properties on our platform."*
- Expedia, FY2022 10-K (`0001324424-23-000007`): *"vacation rental property managers such as Vacasa, who operate
  their own booking sites in addition to listing on Airbnb, Vrbo, and Booking.com"*; repeated in the FY2023,
  FY2024 and FY2025 10-Ks (`0001324424-26-000008`: *"alternative accommodation property managers, who operate
  their own booking sites in addition to listing on Airbnb, Vrbo, and Booking.com"*).
- **The only counter-claim is a belief, never measured:** *"believe the majority of new listings are exclusive to
  Airbnb"* (Q3 2023 letter). No filing read gives a share of listings that are exclusive.

**Guests: the substitutes are named, sized, and growing faster than Airbnb in the documents.**
- Airbnb, FY2025 10-K: *"As guests compare offerings across multiple sites, our marketing efficiency may decline"*;
  competitors *"include online travel agencies ... such as Booking Holdings (including the brand Booking.com),
  Expedia Group (including the brands Expedia and VRBO), Trip.com Group"*, search engines, and hotel chains.
- **Booking.com's homes business, from Booking's own 10-Ks** (`0001075531-20-000011` to `0001075531-26-000009`):
  *"Homes, apartments and other unique places to stay"* **~2,120,000 (2019) → ~3.9 million (2025)**; the
  alternative-accommodation share of Booking.com room nights **about 29% (2019, per the FY2021 10-K) → ~36%
  (2025)**; FY2025: *"companies like Airbnb and Vrbo (owned by Expedia) compete directly with our accommodations
  businesses."* Booking Holdings booked **1,235M room nights in 2025** (all brands); ~36% of Booking.com's alone is
  a homes business of the same order as Airbnb's 533M nights (Booking.com's own room-night count is not separately
  disclosed, so the figure is bounded, not computed). **Over 2019-2025 Booking.com's homes listings grew ~84%
  and their share of its nights rose seven points; Airbnb's nights grew 63%.**
- Vrbo: *"approximately 2.4 million online bookable alternative accommodations"* (Expedia FY2025 10-K).
- **Hotels as the substitute run the other way.** 2020: Airbnb nights -41% and GBV -37%; Marriott worldwide RevPAR
  -60.2%, IHG -52.5%, Hilton -56.7% (IHG run file, from the filers' 10-Ks/20-F); Airbnb *"shift towards ...
  entire homes, and non-urban destinations"*. Airbnb is a substitute **for** hotels; the filings do not show hotels
  as a close substitute for a whole home.

### Criterion (3) — not subject to price regulation: **[x] YES on price, with the regime caveat [E2-59].**
No authority sets Airbnb's fee. **But the product's supply is administered**: permits, night caps and bans
(New York City's *"de facto ban"*), the EU Short-Term Rental Regulation from May 2026. Regulation here does what
[E2-59] says it does to a franchise — it **caps** it — and the cap is recorded at Q4 (THE PERMIT).

### The pricing test [E3-03]'s own sentence names — and **[E2-44](1)**, **[E4-37]**
*"ability to regularly price its product or service aggressively"*; *"an ability to increase prices rather easily
... without fear of significant loss of either market share or unit volume"*; *"you can almost measure the strength
of a business over time by the agony they go through in determining whether a price increase can be sustained."*
- **Take rate: 11.89% (2016) → 13.54% (2023) → 13.57% (2024) → 13.41% (2025) → 13.2% (Q2 2026).** A decade's rise
  of 1.5 points, then **flat for three years** — and **below Booking's 14.46% (13.82% ex-advertising)** on a net-fee
  basis.
- **The 2025-26 fee restructuring is not a price rise; it is a price defence.** From a split fee (host 3% plus a
  guest fee) to a single 15.5% host fee, *"which is helping our hosts price more competitively and creating greater
  guest transparency"*; *"Hosts are able to adjust their prices to maintain the same net earnings"*; guidance: *"We
  expect our implied take rate to remain relatively in-line year-over-year"* (Q2 2026 letter). **The motive is stated
  in the 10-K's own competition risk factor: cross-listed homes make *"our pricing appear less competitive for a
  number of reasons, including differences in fee structure."*** The fee is being re-cut so the displayed price
  survives comparison on another site. That is [E4-37]'s agony, on the record.
- **2023: the same pressure from the guest side.** *"since launching Total Price Display in early 2023, we've seen
  nearly 300,000 listings remove or lower their cleaning fees"*; *"the average nightly price of a one-bedroom listing
  on Airbnb in December was $114, down 2%"* while *"hotel prices rose 7%"* (Q4 2023 letter) — offered as a
  competitive point, it is also a record of price restraint.
- **[E4-55] units:** nights +8% (2025), +10% (Q2 2026) — growing; North America, 42% of revenue, +3% in 2025.
- **[E3-33] untapped pricing power?** The filings show the opposite of untapped: fees restructured to be *neutral*
  under competitive display, and **[E5-28]** — incredible pricing power means *"a monopoly or a near monopoly"*; the
  row below shows two filers of comparable or larger scale selling the same category.

### THE COMPETITOR ROW — required **[E3-28]** *(CONVENTION, confessed at VI)*
Source: `Test Runs/_research 2026-09-13 ABNB/peers/PEER_ROW.md` (every figure with document and accession; XBRL
cross-checks matched). ABNB from its own 10-Ks. Arithmetic ratios.

| | **ABNB** | **Booking (BKNG)** | **Expedia (EXPE, incl. Vrbo)** | **Trip.com (TCOM, RMB)** | Marriott (hotel substitute) |
|---|---|---|---|---|---|
| Take rate (rev ÷ gross bookings) 2019 / 2023 / 2025 | 12.66 / 13.54 / **13.41%** | 15.62 / 14.18 / **14.46%** (ex-adv. 13.82%) | 11.19 / 12.34 / **12.32%** (ex-adv. 11.24%) | not computable (no GMV amount) | n/a (fees on hotel revenue) |
| Units 2019 → 2020 → 2025 | 326.9M → 193.2M → **533M** nights | 845M → 355M → **1,235M** room nights | 389.0M → 173.4M stayed; **415.4M** booked (2025, releases, basis change) | not disclosed | RevPAR $117.30 → $46.28 → $128.80 |
| **2020 vs 2019**: bookings / units / revenue | **-37% / -41% / -30%** | -63% / -58% / -55% | -66% / -55% / -57% | GMV -51/-72/-51/-45% by quarter; rev -49% | RevPAR -60.2%; gross fees -56% |
| First year back above 2019 (bookings / units) | **2021 / 2022** | 2022 / 2022 | 2024 / n/d | 2023 (GMV, core OTA) | — |
| Operating margin 2019 / 2025 | -10.4% / **20.8%** | 35.5% / **32.8%** | 7.5% / 12.7% | 14.1% / 25.3% | — |
| **Marketing ÷ revenue 2019 / 2025** (brand + performance only, where split) | 23.7% / **13.0%** (brand & performance marketing; S&M incl. field ops & policy 33.7% / 21.1%) | 33.0% / **30.4%** (performance + brand) | 50.8% / 55.6% (S&M total; direct 41.8% / 49.9%) | 26.1% / 23.9% (S&M) | — |
| **SBC ÷ OCF, 2021-2025 cumulative** | **31.7%** | 7.3% | 12.2% | 14.7% | — |
| (OCF − SBC − capex) ÷ revenue 2025 | **24.7%** | 31.5% | 18.4% | 18.1% | — |
| Capex ÷ revenue 2025 | 0.27% | 1.2% | 5.2% | 1.3% | — |
| Customer float inside OCF? | **fee float only** (host funds in financing) | yes, merchant float | yes, merchant float | yes, advances | — |

- **Peers named: 3 OTAs of the industry's real competitors, plus the hotel substitute (Marriott; IHG, Hilton from
  the IHG run file).** Named in Airbnb's 10-K but not rowed: Google and AI search, property managers' direct sites,
  experiences platforms (Viator, GetYourGuide, Klook), Tujia and Xiaozhu (private or unsegmented). **Vrbo is
  unsegmented since 2019** (2019: $11,933M gross bookings, $1,340M revenue, 11.2% revenue margin) — its later
  position cannot be rowed from any filing.
- **Limits of the row, stated [E3-61]:** peers' OCF includes merchant float Airbnb's does not, which flatters their
  cash margins relative to column A; Booking and Expedia revenue carries advertising (removed in the ex-adv. rates)
  and Expedia's B2B commissions sit in selling and marketing; Trip.com gives no GMV amount or units. **The row
  shows position; it cannot show conduct.**
- **Untapped pricing power [E3-33]:** no — see the fee record above.
- **The attacker's test [E2-45]** is not hypothetical here: Booking.com, with the larger system, has run it since
  2019 and nearly doubled its homes listings.
- **[E4-04] — continuous rebuild? [E4-32] direction?** The basis — two-sided network and brand — is defended, not
  replaced (*"we substantially completed a rebuild of our technology stack"*, 2025); that alone would not exclude it
  **[E5-23]**. **Direction is not widening on the filed evidence**: take rate flat 2023-25; sales and marketing
  17.8% (2023) → 19.3% → 21.1% of revenue, with *"Field operations and policy"* +43% in 2025; Booking.com's homes
  share of its own nights rising every year.
- **[E4-23] key person:** *"critical to retain and incentivize in light of his sustained and unparalleled leadership
  since the inception of Airbnb"* (DEF 14A on Mr. Chesky); the product rebuild is founder-led. Recorded as a moat
  caution, not decisive.

### What the franchise case rests on — stated at full strength, because it is the strongest fact against this verdict
**Airbnb buys far less of its demand than any rival.** Brand and performance marketing was **13.0% of revenue in
2025 against Booking's 30.4%**, and in 2020-21 the company **cut that spend from $1,140M (2019) to $479M (2020) and
$723M (2021) while GBV rose from $38.0bn (2019) to $46.9bn (2021)** — demand arrived without being paid for, the
424B4's *"approximately 91% of all traffic ... through direct or unpaid channels"* made visible in the income
statement. It also fell least in 2020 and recovered first. **That is a real, measured advantage, and it is why the
return on operating capital is extreme.** But [E3-03] asks what the customer thinks about substitutes and whether
the company can price aggressively; the filings of Airbnb, Booking and Expedia answer both: hosts list on several
platforms, guests compare across sites, the fee is being restructured so as not to lose that comparison, and the
largest rival's homes business has grown faster since 2019. **An efficient, strong position in a contested
category is not a franchise under [E3-03]; it is the "business" of [E3-43] that must be won every day.** The
omission cost of closing wrongly **[E3-47]** is acknowledged: this is the kind of name where it is highest, and
the reopening conditions at Q6 are written to catch the error.

- **Class: [ ] WIDE [x] NARROW [ ] NONE [ ] PROVISIONAL** · **Direction: flat to narrowing** (take rate flat, marketing
  and policy spend rising, the largest rival's homes share rising).
- **Can I name the document that would resolve it?** A filing that measures host exclusivity or guest multi-homing
  does not exist in any filer's disclosures read; the filed record that does exist already answers criterion (2).
  So the verdict is not UNRESEARCHED, and it is not UNKNOWABLE: **the evidence is in, and on it the business is not a
  franchise.**
- **VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *OUT on [E3-03] criterion (2), tested by [E3-03]'s own pricing sentence, [E2-44](1) and [E4-37]: close substitutes
  on both sides of the market are named, sized and quoted in the filings of Airbnb, Booking and Expedia, and the fee
  record is one of price defence (the 2025-26 single-fee restructuring, take-rate-neutral by design) rather than
  aggressive pricing. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].


**STEP 1 — DECLARE THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day **[E3-38]**. Q2 found a strong position in a contested
  category, not a franchise; the 1991 original then governs: *"a business, unlike a franchise, can be killed by poor
  management"* **[E3-43]**. Airbnb competes every day on fee structure, displayed price, product and marketing against
  Booking.com's homes business, Vrbo and hosts' direct sites.
- [ ] **Control** — whole business, no exit **[E1-16]**: not ticked (a listed minority position can be sold).
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**: not ticked ($2.5bn notes, ~$9.6bn net cash).
- **Case declared: Q3 is a BINARY GATE, on daily execution.** *(Recorded, not governing.)*

**The control fact, which is not the [E1-16] determinant but bears on everything below.** The founders
hold the company: *"Directors Brian Chesky (CEO), Nathan Blecharczyk, and Joseph Gebbia, the founders of
the Company, beneficially own approximately 30.5%, 29.7%, and 19.0%, of the company's aggregate voting
power, respectively"* (DEF 14A 2026, in the dual-class sunset proponent's statement, printed by the
company) — **79.2% of the votes** — bound by a *"Founder Voting Agreement ... to vote their shares for
the election of each founder to our board of directors, and to vote against their removal"*. Class B
carries 20 votes; it converts on most transfers, on a founder's death or disability (nine months after), and
otherwise only at *"the 20 -year anniversary of the closing of the IPO"* (December 2040) or on an 80% Class B
vote. **The 2026 dual-class sunset proposal failed 250,653,536 for to
3,558,926,151 against** (8-K 2026-06-11, Item 5.07, `0001559720-26-000018`). An outside owner cannot
change the board, the pay plan or the capital allocation; the exit is the only remedy, which is why the
corpus's exit doctrine **[E4-24]** is the operative one at Q6.

**Honesty — binary, permanent, filings-based [E5-16].** *Each matter dated to when it became public.*
- **IRS transfer-pricing dispute** (NOPA December 2020; Notice of Deficiency May 2024; Tax Court petition
  July 2024): a valuation dispute over the 2013 sale of international IP to a subsidiary, **disclosed with the
  amount and the reserve shortfall** (*"exceeds the current reserve ... by more than $1.0 billion"*). A tax
  position, contested in court, fully disclosed: **not a conduct finding.**
- **Italy** (2017 law; settlements December 2023, December 2024, January 2025): *"without admitting any
  liability"*, $957M in total, and Airbnb **began withholding** on Italian host payments in 2024. A disputed
  legal obligation, settled and complied with: **not a conduct finding.**
- **Spain** (July 2025 proposal €110M, reduced September 2025 to €65M; disputed): listing-rule compliance.
  **Open; not a conduct finding on the record.**
- **No finding of personal misconduct by a named officer or director in any document read** (10-Ks 2020-2025,
  10-Q, DEF 14A 2026, letters). Written as the absence of found disqualifiers, not as a finding that the
  managers are honest **[E5-17]**.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a verdict.*
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, and at full strength in the letters.** The
  guided annual metric is **Adjusted EBITDA Margin**, three years running: *"we expect to maintain an Adjusted
  EBITDA Margin of at least 35%"* (FY2024, Q4 2023 letter); *"at least 34.5%"* (FY2025, Q4 2024 letter);
  *"at least 35.5%"* (FY2026, raised, Q2 2026 letter). Adjusted EBITDA excludes **stock-based compensation
  ($1,592M, 13.0% of revenue)** and *"settlements and reserves for lodging, withholding, transactional and
  other non-income taxes"* — the two recurring costs of this model the run has named. 2025: **Adjusted EBITDA
  $4,297M (35%) against income from operations $2,544M (21%)**. The 10-K presents it with the GAAP line
  first and lists its limits (*"Adjusted EBITDA excludes stock-based compensation expense, which has been, and
  will continue to be for the foreseeable future, a significant recurring expense in our business"*) — **the
  candour is in the footnote; the promotion is in the headline.** Both are recorded.
- [x] **Trumpeted projections [E4-22, third] — FIRES as a prompt; the record is checked [E3-48]:**
  | guided | guidance (letter) | outturn (10-K / letter) |
  |---|---|---|
  | FY2024 Adj. EBITDA margin | *"at least 35%"* | 36% ($4,041M / $11,102M) — **met** |
  | FY2025 Adj. EBITDA margin | *"at least 34.5%"* incl. $200-250M new-business investment | 35% ($4,297M / $12,241M) — **met** |
  | Q1 2024 revenue | $2.03-2.07bn | $2,142M — **beat** |
  | Q1 2025 revenue | $2.23-2.27bn | $2,272M — **top of range** |
  | Q1 2026 revenue | $2.59-2.63bn | $2,678M — **beat** |
  | FY2026 revenue growth | *"at least low double digits"* (Feb) → *"at least mid teens"* (Aug) | H1 +17.1% — on track |
  **Guidance has been met or beaten on every item checked.** The corpus's concern is the ratchet **[E5-30]**,
  not the miss: a quarterly guidance culture is on the record, and it is recorded as a live behaviour, not a
  failure.
- [x] **Serial share issuance [E5-15] — FIRES as a prompt; read, and it is issuance to employees, bought
  back.** ~59M shares re-issued to employees (net of withholding) from January 2022 to July 2026 against ~103M
  repurchased; the 2020 plan carries *"an annual increase ... equal to the lesser of (a) 5 % of the shares of
  all series of the Company's common stock outstanding"* through 2030. Not issuance to raise capital or to buy
  businesses; the net count fell 6.9% from December 2021. The cost is at Q4.
- [ ] weak accounting — **not fired on the statements**; one presentation defect recorded: **the capex line
  was removed from the face of the cash-flow statement from FY2023** while *"FCF: Net cash provided by operating
  activities less purchases of property and equipment"* remained the promoted liquidity measure, so the
  subtrahend of the company's own FCF exists only in the MD&A. Immaterial in amount ($33M); a
  presentation-over-substance note, not a cockroach.
- [ ] unintelligible footnotes — not fired. The customer-funds, unearned-fee and Pay Less Upfront mechanics
  are explained in plain words (Note 2).
- [ ] **filed-figure tells [E4-30]** — cash taxes paid / pre-tax income **6.3% / 10.5% / 7.4%** (2023-25):
  low, and not falling steadily; explained in the filing by NOL carryforwards (*"no remaining net operating
  loss carryforwards for federal income tax purposes"* by 2025), R&D credits, stock-compensation deductions
  (-16.7 points of rate in 2023) and 2025's immediate R&D expensing. Reported growth is not unnaturally smooth
  (2020; 2023's valuation-allowance year). **Read; not fired.**
- [x] **Metric-switching [E2-49] — a soft fire, recorded for checking, not concluded.** Two disclosures that
  were once prominent are **no longer made**: the *"approximately 91% of all traffic ... through direct or
  unpaid channels"* (424B4, 2020; no later filing read repeats a figure), and the **active-listing count**
  (*"over 7 million"* Q3 2023, *"exceeded 7.7 million"* Q4 2023, *"over 8 million"* Q4 2024, *"over 9 million"*
  Q4 2025; **absent from the Q2 2026 letter**, which says only *"Our supply strategy is deliberate and
  precise"*). The Q3 2023 letter's claim that management *"believe the majority of new listings are exclusive to
  Airbnb"* has no measured successor. **No deterioration is shown to have preceded either omission**, so under
  [E2-49]'s own test (a switch that *follows* deterioration fires) this is a prompt, not a finding. The
  "Nights and Experiences Booked" → "Nights and Seats Booked" rename was announced with its reason (services
  launched in 2025): the candour case.
- [x] **Stock-price targeting [E3-50] — FIRES as a prompt on the pay design; no stratagem found.** The CEO's
  entire pay since November 2020 is *"a performance-based RSU award intended to cover ten years of compensation
  ... earned, if at all, based on our 60 trading day trailing average closing stock price exceeding progressively
  higher stock price hurdles, ranging from $125 to $485"*, with a *"$1 base salary"* and no bonus; *"The Company
  does not utilize any other financial performance measures ... in any significant way in its executive
  compensation programs"*. Two of ten tranches ($125, $165) have vested; none in 2025. **What pay vests on
  [E4-27]: the quoted price, and nothing else.** The corpus's objection **[E3-50]** is to the premise
  *"that their job at all times is to encourage the highest stock price possible"* and its next step,
  *"unadmirable accounting stratagems"*. **The premise is written into the pay plan; the stratagem is not
  found in the statements.** The board records Mr. Chesky's *"intention to donate the net proceeds from the
  award"* — a fact about motive the filing offers and this run cannot verify.

**Where the flags converge [E4-52].** Four prompts point one way: **a headline margin that excludes the
13%-of-revenue stock compensation, a pay plan that vests only on the share price, a repurchase programme
described as managing dilution rather than as buying below value, and $4bn+ a year of cash spent to keep a
per-share count falling.** Each is disclosed; none is a stratagem. **Together they form one reinforcing
system that tilts every reported per-share and margin figure toward the quote** — which is exactly the
confluence the lollapalooza row describes. It is read as a system, and it bears on the buyback test below
and on position size, **not** on honesty.

**STEP 3 — THE PRIMARY TEST [E2-01]** — earnings on equity, balance sheet first.
- Equity (year-end): $4,776M (2021), $5,560M (2022), $8,165M (2023), $8,412M (2024), $8,199M (2025), $7,799M
  (2026-06-30). **Book equity is mostly not operating capital**: $11.0bn of own cash and short-term investments
  and $2.1bn of deferred tax assets against $14.0bn of liabilities that include $7.0bn owed to hosts.
- Net income / year-end equity: 2022 34.0%; 2023 58.7% as reported, **23.2% without the $2,897M
  valuation-allowance release**; 2024 31.5%; 2025 30.6%.
- **Unleveraged net tangible operating assets [E2-43] are negative** (the operating balance sheet is funded by
  customers), so the return on the capital the operators actually use is not a finite number. The operating
  test therefore runs on the business, not the ratio: income from operations $2,544M on $107M of property and
  equipment. **Primary test: passed on the business's economics**; the owner's share is thinned by the Q4 SBC
  arithmetic.

**The half-owner test [E2-26].** The 10-K tells the owner the IRS shortfall with its size, the Italian
settlements by year, the customer-funds mechanics, the SBC by line, and puts GAAP before non-GAAP. The
letters lead with Adjusted EBITDA and FCF, **both before stock compensation**, and dropped the listing count.
**Mixed: the annual report passes; the quarterly narrative is built on the before-SBC figures.**

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists any change in current direction — **not ticked**: exited mainland China domestic listings
  (*"In July 2022, all mainland China listings were taken down"*), cut a quarter of staff in 2020, rebuilt
  the fee structure in 2025-26.
- [x] projects materialise to soak up funds — **prompt**: services (*"grocery delivery, car rentals, airport
  pickups, and luggage storage"*), relaunched experiences (*"supply by nearly 80% year-over-year"*), hotels,
  *"$200 million to $250 million towards launching and scaling new businesses"* (2025). Sized small against
  $4.6bn of OCF; watched for [E3-40] loss of focus.
- [ ] staff studies to justify a craving — no evidence either way in a filing.
- [x] peer behaviour imitated — **prompt**: adding hotels (*"We added thousands of boutique and independent
  hotels to Airbnb"*, with a *"price match guarantee and up to 15% Airbnb credit"*), the product the OTAs sell.

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-24].**
- (1) ample funds for operations and liquidity? **Yes** — $12.1bn own liquidity, $2.5bn notes, net cash.
- (2) repurchases at a **material discount** to conservatively calculated IV? **No, on this run's own
  range.** 2022-H1 2026 repurchases averaged ~$107-$140 a share (2025: $3,789M for 29.7M = ~$128), when owner
  earnings were ~$2.5-3.1bn on ~600M shares — **$4-5 a share, a 3-4% owner-earnings yield at the purchase
  prices**, far below the 10% floor (the sovereign at each purchase date was not struck and is not claimed). **And the company does not claim the
  discount**: the stated purpose is *"to help manage the impact of share dilution"*; the stated order is
  *"investments in organic growth, strategic acquisitions or partnerships, and return of capital to
  shareholders, in that order"*. **(3) [E4-31]:** no intrinsic-value estimate or policy is supplied to owners.
- **CAPITAL ALLOCATION FLAG — fired**, with the humility clause **[E4-13]**: *"it is natural for CEOs to be
  optimistic about their own businesses. They also know a whole lot more about them than I do"* — and
  *"many CEOs never stop believing their stock is cheap"* **[E5-08]**. This rests on this run's own IV range,
  which management may reasonably dispute on growth. **It binds position size, never the discount rate.**
- **The refusal test [E2-51]** does not apply: repurchases are not refused; they are made on a dilution
  rationale instead of a value one.

**Pay and what it vests on [E4-27].** CEO: share-price hurdles only (above). Other NEOs: *"70% of the intended
award value in time-based restricted stock units ... and 30% ... in stock options"*; cash bonus on company
priorities (*"Business Performance: Deliver topline growth and maintain bottom-line margin"*, global-markets
nights, defects and engagement), paid at 100% for 2025. **No element of executive pay vests on owner earnings,
per-share value after dilution, or return on capital.** Say-on-pay passed 3,785,488,625 to 23,678,837 — a vote
the founders' Class B shares decide.

**THE GUARDRAIL — checked before the verdict.**
- [x] Nothing in this Q3 is used to **promote** the name **[E2-37, E2-38, E3-39]**.
- [x] **Key-person dependence recorded at Q2 as a moat question [E4-23]**, not here as a strength: the company
  describes Mr. Chesky as *"critical to retain and incentivize in light of his sustained and unparalleled
  leadership since the inception of Airbnb"* and the risk factors say *"Our founders ... may terminate their
  employment with us at any time"*.
- [x] Is a great manager the reason to act? **No; the manager is not the plan in this run.**

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *No integrity disqualifier found (the absence of found disqualifiers, not a finding of honesty [E5-17]). Live and
  carried: the capital-allocation flag [E5-08] with its humility clause, the converging stock-price system [E4-52],
  [E4-29] in the letters, and founder control of 79.2% of the votes. IN never promotes.*
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].


### First: what is in operating cash, and what is not — the customer-funds separation
**Read from the cash-flow statement and Note 2 before any owner-earnings figure is stated.** Airbnb's
balances are of three kinds, and the filing classifies them differently:

| balance | what it is (filing's words) | 2024 → 2025 → 2026-06-30, $M | where its change sits |
|---|---|---|---|
| **Funds receivable and amounts held on behalf of customers** / **funds payable and amounts payable to customers** | *"cash received or in-transit from guests ... which the Company remits for payment to the hosts following check-in"*; *"a liability for the same amount is recorded"* | 5,931 → 6,959 → **12,224** (asset = liability, to the dollar) | **FINANCING**: *"Change in funds payable and amounts payable to customers"* +936 / +320 / +401 (2023-25), +5,426 (H1 2026); the cash sits in *"Cash and cash equivalents included in funds receivable and amounts held on behalf of customers"* (5,871 → 6,891 → 12,161) inside the cash-flow statement's restricted-cash total |
| **Unearned fees** | *"Host and guest fees are recorded as cash with a corresponding amount in unearned fees"*; *"subject to refund in the event of a cancellation"* | 1,616 → 1,743 → 2,831 | **OPERATING**: +242 / +200 / +122 (2023-25); +1,085 (H1 2026) |
| **Interest earned on customer funds** | *"Funds held on behalf of our hosts and guests ... do not impact Free Cash Flow, except interest earned on these funds"* (Q2 2026 letter) | not separately disclosed | **OPERATING**, inside interest income ($721M / $818M / $705M) |

**So the trap the brief named is smaller here than at PAY, and it is in a different place.** The hosts'
money (the $7-12bn) **never enters operating cash**: its swing is financing, and the 2020 refund wave
(*"Change in funds payable ... (1,024)"*) ran through financing too. **What does enter operating cash is
(a) Airbnb's own fees collected before the stay, which reverse when bookings shrink (2020: -$267M), and
(b) the interest on the hosts' money.** Owner earnings are therefore shown three ways:
- **A — as filed:** OCF − SBC − (c).
- **B — the fee float removed:** A − the change in unearned fees. *(The corpus's working-capital rule
  [E2-23] runs the other way here: this business does not require working capital to grow, it releases
  it. B shows the earnings without the release.)*
- **C — B less the interest attributable to customer funds.** **CONVENTION, confessed:** interest income
  × average customer funds ÷ (average customer funds + average own cash and short-term investments),
  year-end averages for 2019-2023 and five quarter-end points for 2024-2025 (Q2 2026 letter's quarterly
  summary). Removed **pre-tax**, because cash taxes paid ran 6.3% / 10.5% / 7.4% of pre-tax income in
  2023-25; the conservative direction. The attribution share ran 29-42%: **~$294M of 2025's $705M.**
  A pass-through of smaller size is left in A: lodging taxes collected and owed ($312M → $387M) sit in
  accrued liabilities; their +$75M swing in 2025 is not stripped (0.3% of cap; stated, not used).

### Owner earnings — the one number **[E2-23]**
**Inputs, all from the filed cash-flow statements (newest vintage) and the MD&A FCF reconciliations; $M.**
`_research .../q4calc.py`, output in `q4calc_out.txt`.

| year | OCF | SBC (add-back) | capex (MD&A) | D&A | Δ unearned fees | cust.-funds interest (C, est.) | **A capex end** | **A D&A end** | B capex / D&A | C capex / D&A | SBC/OCF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 (pre-IPO) | 223 | 98 | 126 | 114 | 176 | n/a | 0 | 11 | -177 / -165 | n/a | 43.8% |
| **2020** | **-740** | **3,003** | 37 | 126 | -267 | 10 | **-3,780** | **-3,869** | -3,513 / -3,602 | -3,523 / -3,612 | n/m |
| 2021 | 2,313 | 899 | 25 | 138 | 496 | 4 | 1,389 | 1,276 | 893 / 780 | 889 / 776 | 38.9% |
| 2022 | 3,430 | 930 | 25 | 81 | 280 | 60 | 2,475 | 2,419 | 2,195 / 2,139 | 2,135 / 2,079 | 27.1% |
| 2023 | 3,884 | 1,120 | 47 | 44 | 242 | 253 | 2,717 | 2,720 | 2,475 / 2,478 | 2,222 / 2,225 | 28.8% |
| 2024 | 4,518 | 1,407 | 34 | 65 | 200 | 334 | 3,077 | 3,046 | 2,877 / 2,846 | 2,543 / 2,512 | 31.1% |
| 2025 | 4,646 | 1,592 | 33 | 91 | 122 | 294 | 3,021 | 2,963 | 2,899 / 2,841 | 2,605 / 2,547 | 34.3% |
| TTM 2026-06 | 4,860 | 1,707 | 33 | 84 | -29 | — | 3,120 | 3,069 | 3,149 / 3,098 | — | 35.1% |

*2020 is not dropped [E4-25]*: it is the pandemic trough **and** the IPO year — *"$2.8 billion of
stock-based compensation expense associated with the vesting of RSUs in connection with our IPO"*, years
of pre-IPO service recognised at once, plus the 2020 OCF restatement (-$629.7M filed, -$740M in the
FY2022 10-K). It is shown in every window that includes it.

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE **[E4-25, E4-38]**
| window | A (capex end … D&A end) | yield on US$100,341.6M | B (fee float removed) | C (and cust.-funds interest) |
|---|---|---|---|---|
| **5y 2021-2025, ex-2020 (the corpus default [E2-42])** | **2,536 … 2,485** | **2.53% … 2.48%** | 2,268 … 2,217 (2.26-2.21%) | 2,079 … 2,028 (2.07-2.02%) |
| **5y 2020-2024, incl. 2020** | **1,176 … 1,118** | **1.17% … 1.11%** | 985 … 928 | 853 … 796 (0.85-0.79%) |
| 6y 2020-2025, full listed history | 1,483 … 1,426 | 1.48% … 1.42% | 1,304 … 1,247 | 1,145 … 1,088 |
| 3y 2023-2025 | 2,938 … 2,910 | 2.93% … 2.90% | 2,750 … 2,722 | 2,457 … 2,428 |
| 7y 2019-2025, incl. pre-IPO 2019 | 1,271 … 1,224 | 1.27% … 1.22% | 1,093 … 1,045 | n/a |
| TTM to 2026-06-30 | 3,120 … 3,069 | 3.11% … 3.06% | 3,149 … 3,098 | — |

- **Spread, conservative end:** the ex-2020 five-year window (D&A end, 2,485) against the incl.-2020
  five-year window (1,118) is **-55%**; against the float-stripped incl.-2020 window (796), **-68%**.
- **Combined range: $0.8bn (5y incl. 2020, C, D&A) to $3.1bn (TTM, A, capex).** Is it too wide to reach a
  conclusion? **Not for the question Q4 asks** — every window with 2020 removed lies at $2.0-3.1bn and every
  window with it lies at $0.8-1.5bn, and **all of them sit below the 5.35% sovereign at this price**. The
  width is a **level** uncertainty, not a sign uncertainty, and the distortion is named: one pandemic year
  combined with an IPO-year stock-compensation catch-up.
- **The distorted year, as a Q4 finding [E5-11]:** the stream is **not reliable through a travel stoppage**.
  2020: GBV -37%, OCF -$740M, a quarter of employees cut (*"approximately 1,800 employees in May 2020"*),
  and survival financed by strangers at a price (below).
- **Favourable exogenous breaks, removed before the mean is trusted [E4-41]:** interest income rose from
  $12.7M (2021) to $818M (2024) on rates, not on the business. C strips the customer-funds share; the
  interest on Airbnb's own $11bn (~$411M of 2025's $705M) is left in, and would fall with rates.

### Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT **[E3-44, E2-41, E5-20]**
- **Which case is this?** The **default case, not the exception class.** The tag gap was a presentation
  change (Step 0). Capex is $25-47M a year since 2020 (0.27-1.1% of revenue); property and equipment, net,
  $107M. **Nothing in the filing says depreciation understates renewal**; the opposite holds: D&A ($44-138M)
  has exceeded capex in five of six listed years, because D&A carries acquired-intangible amortisation
  (HotelTonight, 2019; *"Amortization expense related to intangible assets was immaterial"* by 2023-25) and
  1.5-3-year software lives.
- **Band used: capex end to D&A end, which differ by $3-113M a year — under 5% of the owner-earnings
  figure in every window (5.2% in the incl.-2020 five-year window, under 2.1% in every window without 2020).** **The (c) guess does not move any verdict.** Where it sits: nearer the D&A end,
  **because the maintenance of this competitive position is expensed, not capitalised** — product development
  $2,354M and marketing $1,704M in 2025, and a $1.7bn data-hosting commitment through 2031 — so both ends
  of (c) are small only because OCF has already paid the real renewal bill. That is the reason to trust the
  small (c), and it is also the reason owner earnings are not larger.
- **Capitalised stock compensation:** the equity statement's SBC ($1,146M / $1,424M / $1,600M, 2023-25)
  exceeds the cash-flow add-back ($1,120M / $1,407M / $1,592M) by $8-26M, capitalised into software. It is
  inside the D&A end (as amortisation) and outside the capex end; one more reason the D&A end is used as
  the conservative figure.
- *If the capex band changes the verdict → UNKNOWABLE.* **It does not.**

### Stock compensation — subtracted in full **[E5-06]**, and it RESOLVES and is COMPLETE
**Cross-checked to the dollar, 2025:** cash-flow add-back **$1,592M** = MD&A table (*"Operations and support
| $ | 90 ... Product development | 886 | ... | 1,017 ... Sales and marketing ... 212 ... General and administrative
... 273 ... Stock-based compensation expense | $ | 1,407 | ... | $ | 1,592"*: 90 + 1,017 + 212 + 273 = 1,592) =
Note 16 segment expense 1,592 = companyfacts `ShareBasedCompensation` 1,592.0. H1 2026: 63 + 561 + 122 +
151 = **897** = cash-flow add-back 897. Every year 2019-2025 resolves from the filed statement; no year is
missing, dimensioned, or zero (the item-3F defect cannot bite here).

**SBC / OCF, over the full filed history since the IPO:**
| span | SBC $M | OCF $M | **SBC/OCF** |
|---|---|---|---|
| **2020-2025 cumulative (listed history, incl. the IPO catch-up)** | 8,951 | 18,051 | **49.6%** |
| 2020 – H1 2026 | 9,848 | 21,029 | 46.8% |
| **2021-2025 cumulative (ex-2020)** | 5,948 | 18,791 | **31.7%** |
| 2021 – H1 2026 | 6,845 | 21,769 | 31.4% |
| by year 2021 / 22 / 23 / 24 / 25 / TTM | | | 38.9% / 27.1% / 28.8% / 31.1% / 34.3% / 35.1% |

**In the calibrated row: ACVA 330.5% · ROKU 140.2% · CALX 98.4% · ARM 96.6% · CRWD 68.0% · ABNB 49.6%
(cumulative since the IPO year) / 31.7% (ex-2020).** ABNB sits **below CRWD** — the name whose 68.0% closed
its file — on either reading. **But the direction is up for four straight years (27.1% → 35.1%), and SBC
is 13.0% of revenue.** SBC is subtracted in full; it is not the centre of this file the way it was at
CRWD, and saying so is the finding, not a softening.

**The market-value measure [E3-70] — the charge is the floor.** RSUs granted at grant-date fair value
(10-K Note 12; share counts rounded to millions in the filing, so ±$70M): 2024 13M × $153.36 ≈ $1,994M;
2025 16M × $136.11 ≈ $2,178M; less cancellations (2M × $143.07; 3M × $140.20) ≈ **$1.71bn (2024) and
$1.76bn (2025)**, plus ~1M options a year at $93.29 / $69.08 — against charges of $1,407M and $1,592M.
**On this measure owner earnings are ~$0.2-0.3bn a year lower than column A** (2025: ~$2.7bn). Stated as the
[E3-70] sensitivity; the charge-based figures above are the floor of the subtraction, as the framework says.

**The employee tax withholding on net share settlement — how it was treated.** A financing outflow:
*"Taxes paid related to tax on equity awards"* $1,527M (2020, the IPO settlement) / $177M / $607M / $1,224M
(2023, incl. *"$567 million of employee withholding tax"* on a May 2023 cashless option exercise) / $630M /
$561M / $305M (H1 2026). **Treatment: NOT subtracted from owner earnings a second time.** It is the cash
settlement of part of the same awards whose full grant value SBC already subtracts — economically the
company buying back, at market, the shares it would otherwise have issued. **It is counted with the
buybacks**, below, where it belongs: in the cost of holding the share count.

### Buybacks against dilution — the net share count
| | Dec 2020 | Dec 2021 | Dec 2022 | Dec 2023 | Dec 2024 | Dec 2025 | Jul 15 2026 (cover) |
|---|---|---|---|---|---|---|---|
| Class A + B outstanding (M) | 599.2 | 633.5 | 631 | 638 | 623 | 602 | **589.6** |
| gross repurchased (M) | — | — | 14 | 18 | 25 | 30 | 16 (H1) |
| repurchases $M | — | — | 1,500 | 2,252 | 3,430 | 3,789 | 2,139 (H1) |
| withholding $M | 1,527 | 177 | 607 | 1,224 | 630 | 561 | 305 (H1) |

- **Net change Dec 2022 → Jul 2026: -41.4M shares (-6.6%)** for **$16.4bn** of repurchases plus withholding —
  **~$397 of cash per net share retired**, against average repurchase prices of ~$107 (2022) to ~$140 (2024). Of ~103M shares
  bought from January 2022 (count 633.5M at Dec 2021), **~59M (net of withholding) were re-issued to employees**. The letter's own words:
  *"We repurchased $1.1 billion of Class A common stock during Q2 2026 to help manage the impact of share
  dilution"*; *"our fully diluted share count has decreased approximately 10%, driven by our share
  repurchases and cash used for employee tax obligations totaling over $16 billion"*.
- **Net change Dec 2020 → Jul 2026: -9.6M (-1.6%)**; Dec 2021 → Jul 2026: -43.9M (-6.9%).
- **The cash view, to the dollar:** OCF − capex − repurchases − withholding = **$1,298M / $361M / $424M /
  $263M** (2022-25). **Holding the count down ~3% a year absorbed 61% / 89% / 90% / 94% of operating cash.**
  That is capital allocation, not maintenance, and it is scored at Q3 — but it is the plainest measure of what
  employee ownership costs the other owners: **most of what the company earns is being spent buying back what
  it pays its people.**

### Taxes — a non-cash release, stated and set aside
2023 net income $4,792M includes a **$2,897M valuation-allowance release** (Schedule II, *"Credited to
Expenses | ( 2,897 )"*; cash-flow *"Deferred income taxes | ( 2,875 )"*). 2025 carries a **$213M valuation
allowance** against CAMT credits. **Neither touches cash; owner earnings come from cash; moved on.** Cash
taxes paid: $132M / $350M / $232M (2023-25).

### Great, good, or gruesome? **[E4-20]**
- [x] **great** — high return, rising, little capital needed
- [ ] good  [ ] gruesome
- Evidence: revenue 2.5× since 2019 ($4,805M → $12,241M) while capex **fell** ($126M → $33M) and property and
  equipment, net, is $107M. **The business runs on negative operating capital** — customer funds, unearned
  fees and payables exceed its operating assets — so the return on operating capital is not a meaningful
  number; income from operations $2,544M is earned on a balance sheet whose tangible operating base is
  approximately nil. **Qualification, stated:** the "little capital" is true of capex and false of people —
  ~$4.3bn a year of repurchases and withholding is what the equity-funded payroll consumes. The class is
  great on capital; the owner's share of it is thinned at the rate shown above.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — PARTLY.** Large ($2.5-3.1bn ex-2020). **Not reliable
  through a travel stoppage**: 2020 OCF -$740M; in April 2020 the company took *"a $1.0 billion First Lien
  Credit and Guaranty Agreement"* at *"7.5% plus the London Interbank Offered Rate ... subject to a floor of
  1%"* and a second-lien loan with warrants, repaid in 2021 with *"Prepayment penalty on long-term debt |
  (213)"* and *"Loss from extinguishment of debt | 377"*. **That is the kindness of strangers [E5-39], priced.**
- **(2) massive liquid assets — YES.** Own cash, equivalents and short-term investments **$12.1bn**
  (2026-06-30; *"$12.1 billion of cash and cash equivalents, short-term investments, and restricted cash"*),
  undrawn $1.0bn revolver (*not counted* [E5-39]). The $12.2bn of customer funds is **not** counted: it is
  owed, and *"In certain jurisdictions, we are required to either safeguard customer funds in
  bankruptcy-remote bank accounts, or hold such funds in eligible liquid assets"*.
- **(3) no significant near-term cash requirements — YES, with one named exception.** Debt: **$2.5bn senior
  notes, first maturity $850M in March 2029**; interest ~$119M a year (my arithmetic on the 8-K coupons:
  850 × 4.400% + 850 × 4.650% + 800 × 5.250%). Leases $86M due 2026. Data hosting $219M due within a year.
  **The exception: the IRS Notice of Deficiency — *"$1.3 billion in tax, plus penalties and interest"*, which
  *"exceeds the current reserve ... by more than $1.0 billion"*,** in Tax Court since July 2024. Against $12.1bn
  of own liquidity it is survivable in full; it is named, not netted.
- **Score: 2.5 of 3.** Leverage, named and quantified [E4-16]: $2.5bn of covenant-light unsecured notes
  (*"limit the ability ... to ... create liens ... sale and leaseback ... consolidate"*; no financial covenant
  in the notes) against $12.1bn of own liquidity — **net cash ~$9.6bn**. **Coverage [E2-54]:** ~$119M of
  interest against ~$2.5-3.1bn of owner earnings net of capex — **~21-26×**. The revolver carries *"a leverage
  ratio and fixed charge coverage ratio"*; undrawn.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**
**The mechanism — THE PERMIT** *(a proposed seventeenth shape; checked against the index below).* **The
product is the right of private owners to rent their homes by the night, and that right is granted, capped
or withdrawn city by city by governments that the hotels lobby, while the same governments deputise the
platform to enforce the rules and collect — and increasingly pay — the tax.** The business does not die of a
competitor; it is **regulated out of its densest, highest-rate markets one ordinance at a time**, and each
jurisdiction also sends a bill.
- **Exposure, from the filing, not experience [E4-40]:** *"the City of New York has effectively banned
  short-term rentals, and this has led to similar restrictions being considered throughout the State of New
  York"*; *"the EU Short-Term Rental Regulation ... will enter into force in May 2026 and will require
  additional compliance efforts ... potentially discouraging and prohibiting current and potential hosts from
  listing properties"*; *"Host listings may also be limited by night caps, density restrictions, onerous
  permitting requirements, primary residence or host presence requirements, permit caps, minimum night stays,
  and/or discretionary permitting or lottery systems"*; *"Hotels and groups affiliated with hotels have engaged
  and will likely continue to engage in various lobbying and political efforts for stricter regulations"*;
  *"We have resolved some disputes by agreeing to remove listings or share data with authorities."*
- **What it has cost, from the filings:** **New York City: *"Prior to September, New York City represented
  approximately 1% of Airbnb global revenue"*** (Q3 2023 letter, `0001193125-23-268164`); *"Approximately 80%
  of our top 200 markets by revenue already have some form of regulation."* Italy: €576M + €139M + €179M =
  **$957M** settled for 2017-2023, with withholding now applied to Italian host payments. Spain: a proposed
  **€65M** fine for listing-rule non-compliance. Host withholding-tax reserves $199M (+$150-160M reasonably
  possible); lodging-tax reserves $114M (+$25-35M). G&A carried *"a $74 million increase from non-income taxes
  and related fees and penalties"* in 2025. **The 10-K quantifies no listing count or revenue lost to
  regulation beyond New York**; the absence is stated as "no instance found in the 10-Ks, 10-Qs and letters
  read".
- **Quantified, from filed figures (my arithmetic, 2025 base):** revenue $12,241M; merchant fees 13.6% of
  revenue are the only cost that falls one-for-one with bookings, so roughly **86% of lost revenue falls to
  operating income** in the short run. **A New York repeated across EMEA** — say one-fifth of EMEA's $4,729M
  (≈$946M, 7.7% of revenue) — takes ~$810M from operating income (2,544 → ~1,730) and owner earnings from
  ~$3.0bn toward ~$2.2bn: **survived.** **Owner earnings reach zero only when ~28-30% of revenue (~$3.5bn) is
  regulated away** — the equivalent of losing most of Europe, or North America's big cities and resort
  counties together. Even then, $12.1bn of own liquidity against $2.5bn of notes funds years of adjustment.
- **The second mechanism, carried beside it:** disintermediation of demand — *"If consumers become less reliant
  on search engines for travel searches and instead use AI apps and other channels, we may not be able to
  optimize for searches on these emerging channels"*; *"Some property managers and hosts encourage direct
  bookings, bypassing our platform"*. Not quantifiable from any filing read.
- **Likelihood:** [ ] likely · **[x] a real possibility** (continued erosion: market-by-market restriction that
  flattens nights growth in the core and raises the tax bill) · the death itself — ~30% of revenue regulated
  away — **a low-level possibility** on the filed record (New York was 1%; growth continued through it:
  nights +14% in 2023).
- **Against the index (16 shapes, four of them proposed, as read at 2026-09-13 after the IHG fold):** not #11 THE PASS-THROUGH (no capex race; gains are not competed away by
  customers but withdrawn by permit); not #13 THE TENANT (supply is millions of owners, none renting to
  every rival on a reset rent — though they do cross-list, see Q2); not #14 THE PATRON (no government funds the
  business; it permits it, and bills it); not #12 THE ADDRESS (one disputed jurisdiction); not #16 THE FLAG (owners re-flag to a rival brand at contract end — the
  nearest in kind, since Airbnb hosts also cross-list, but there is no contract end, no key money and no rival bid; the
  supply here is lost to the permit-giver, not to a rival). **Nearest is THE
  PATRON; the difference is that the patron pays and sets terms, while the permit-giver pays nothing, can
  withdraw the product itself, and makes the platform its tax collector.** Proposed as the seventeenth shape,
  pending the operator, like #13-#16.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *Owner earnings exist and are positive in every window without 2020 ($2.0-3.1bn) and in every window with it
  ($0.8-1.5bn); SBC resolves and is complete; (c) moves nothing; great on capital; [E5-11] 2.5 of 3; the named death
  (THE PERMIT) is a real possibility as erosion and a low-level possibility as death. Survival is not what closed this
  file.*

---

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** **Q2 is OUT; Q5 does not open.** What follows is headed as operator rule 3 requires, and carries no entry language.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Operator rule 3 and the queue's instruction that every run ends with a price. The file closed at Q2 (OUT). Nothing
below is an entry signal, a ranking or a verdict.*


**The price and what the buyer is paying for, in words.** At **US$170.19 × 589,585,682 = US$100,341.6M**,
the buyer pays **~32-33 times the owner earnings of the best twelve months ever filed** (TTM $3.07-3.12bn),
**~40 times the five-year ex-2020 mean** ($2.49-2.54bn), and **~85-90 times the five-year mean that keeps 2020**
($1.12-1.18bn). Put plainly: the price already pays for **a decade in which a fee on private-home stays
compounds at double digits after stock compensation, keeps its take rate while moving to a 15.5% host-only
fee, holds its densest cities against permit regimes, and carries its interest income through lower rates**
— and it asks nothing of the buyer's 10% floor in return for the 2020 lesson.

**THE FLOOR, before the ranking [E4-28, E3-13].** Honest pre-tax expectancy at this price, on the arithmetic
below: **owner-earnings yield 1.1-3.1% plus whatever growth the buyer believes**; reaching ~10% needs
**6.7-8.8% a year forever**. Below roughly 10% the name is quit on, not ranked.

**1. THE YIELD** (`_research .../q5calc.py`, output `q5calc_out.txt`)
| base | owner earnings $M | ÷ cap | yield | vs sovereign 5.35% |
|---|---|---|---|---|
| 5y 2020-2024 incl. 2020, D&A end (conservative) | 1,118 | 100,341.6 | **1.11%** | -4.24 pts |
| 6y 2020-2025, D&A end | 1,426 | | 1.42% | -3.93 |
| 5y 2021-2025 ex-2020, float-stripped (C), D&A | 2,028 | | 2.02% | -3.33 |
| **5y 2021-2025 ex-2020, D&A end (the default window)** | **2,485** | | **2.48%** | **-2.87** |
| 3y 2023-2025, capex end | 2,938 | | 2.93% | -2.42 |
| TTM to 2026-06-30, capex end (generous) | 3,120 | | **3.11%** | -2.24 |

**2. WHAT THE PRICE ALREADY ASSUMES**
- Perpetual growth needed to earn the **10% floor**: **8.8%** (conservative base) · **7.3%** (default window) ·
  **6.7%** (TTM). To earn merely the **bond**: 4.2% · 2.8% · 2.2%.
- DCF engine (casts no vote [E3-34]): **13.5-16.6% a year for ten years, then 3% forever**, from the TTM and
  default-window bases, to justify the cap at 10%.
- What the business has actually done: revenue +16.9% a year 2019-2025 (4,805 → 12,241, a recovery-inflated
  base) and **+10% in 2025**; nights +8% in 2025; owner earnings (A, D&A end) 2,419 → 2,963 from 2022 to 2025,
  **+7.0% a year**, with SBC/OCF rising. **[E4-35]**: sustained 15% growth is a fewer-than-one-in-twenty event
  among the most profitable companies; the engine's 13.5-16.6% for a decade carries that burden, in writing,
  and does not meet it on the filed record. **[E4-44]**: value cannot outgrow earnings; the ceiling is the
  home-stays market that regulation permits **[E2-63]**.

**3. WHAT YOU ARE PAID**
- **-2.2 to -4.2 points against the sovereign** on today's owner earnings. Nothing is paid for the certainty
  question; the 2020 answer is not priced.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** Sovereign used **5.35%**, bare. The end
margin is the only place certainty is priced **[E4-11, E4-48]**; it is not needed below, because the price
sits above the whole range.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — at the 10% floor, Gordon OE × (1+g)/(0.10−g), per share:
| owner earnings | g = 0% | 3% | 5% | 6% | 7% |
|---|---|---|---|---|---|
| $2.03bn (C) | $34 | $51 | $72 | $91 | $123 |
| $2.49bn (default) | $42 | $62 | $89 | $112 | $150 |
| $3.12bn (TTM) | $53 | $78 | $111 | $140 | $189 |

**Conservative ~$35-60 · optimistic ~$110-140 (6% forever on the best filed year) · current price $170.19.**
Even the most generous cell on this page that does not assume 7% forever ($140) is below the quote.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **~3% plus growth, needing ~7-9% perpetual growth for 10%**
  vs ~10% **[E4-28]** — **below → quit on; the ranking lines are not filled in.**

**WHICH BAR? — Screamer test [E4-01]:** does the price clear the conservative case (~$35-60)? **No. Price above
the whole range as stated → no.** The price enters a range only when 7% a year forever is granted on the best
twelve months ever filed ($189 in the table) — the assumption [E4-35] puts the burden of proof on, and the
filed record (owner earnings +7.0% a year 2022-25 with SBC/OCF rising) does not discharge it. No margin added; windage count **one** (the conservative end of the owner-earnings
range; the float-stripped column C is displayed, not stacked into the value).

- **VERDICT: none — Q5 did not open (Q2 OUT).** The computation shows the price above the whole value range at the
  10% floor; had every gate been IN, this would have failed on price.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].


**Pre-committed [E1-02] — reopening conditions, in words, because nothing is owned and nothing is armed:**
- **Why nothing is armed:** the file failed at Q2 on the business; a price alert would be a category error (the QLYS
  ruling, 2026-09-07). The reversal conditions are written in words.
- **What would reopen Q2 (the error this run most fears [E3-47]):**
  1. **A measured exclusivity or multi-homing figure** in a filing — share of nights from listings not on Booking.com
     or Vrbo — showing a large and rising exclusive base. The Q3 2023 letter's belief is not that figure.
  2. **A take-rate rise that holds units**: the implied take rate above ~14% for a full year after the single-fee
     migration completes (guided *"this year"*), with nights growth not slowing below the market's — the [E2-44](1)
     behaviour this run did not find.
  3. **Booking.com's alternative-accommodation share of its room nights falling** (36% in 2025) while Airbnb's nights
     grow — the substitute retreating.
  4. **Brand and performance marketing held near 13% of revenue** while *"Field operations and policy"* stops growing
     faster than revenue — the direct-demand advantage re-proven without buying it.
- **What would confirm the close:** take rate below 13% after the fee migration; sales and marketing above ~22% of
  revenue; North America nights flat or falling [E4-55]; a second New York (a top-ten market losing most short stays).
- **Next catalyst dates:** Q3 2026 results (early November 2026; guidance: take rate *"relatively in-line"*); the
  single-fee migration's completion (*"expected to be completed this year"*); the EU Short-Term Rental Regulation in
  force from May 2026 (first full year in the FY2026 10-K, due ~February 2027); IRS Tax Court.
- **Sell rule [E2-28] / monitoring [E4-17, E3-30]:** not applicable — nothing owned. Position size: **none**.
- **VERDICT (RECORDED, NOT GOVERNING): not applicable — the file closed at Q2; reopening conditions recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6 recorded beneath
  explicit RECORDED, NOT GOVERNING banners; Q5 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on named filings; the
  recorded Q3 and Q4 INs carry no such word. The one estimate in the file (column C's customer-funds interest) is
  labelled CONVENTION and does not sit under an IN it could promote.
- [x] Every UNRESEARCHED verdict names the artifact — none issued. The Q2 non-IN verdict was put to the separating test
  aloud (no filing measures host exclusivity; the filed record already answers criterion 2) → OUT, not UNRESEARCHED.
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued.
- [x] Step 0: filing read with accession numbers (10-K `0001559720-26-000004`, 10-Q `0001559720-26-000027`, DEF 14A
  `0001193125-26-175062`, FY2020-FY2024 10-Ks, 424B4, 8-Ks); figures cross-checked (OCF FY2025 $4,646M filed =
  companyfacts; FY2020 OCF restatement found; SBC FY2025 $1,592M to the dollar across four places).
- [x] Owner earnings on multi-year means; six windows with and without 2020 and pre-IPO 2019; both (c) ends; the
  customer-funds separation done from the cash-flow statement before any figure; (c) disclosed as a judgment [E3-44].
- [x] Competitor row filled from filings (BKNG, EXPE, TCOM, MAR; IHG/HLT from the IHG run file, read only), limits
  stated [E3-61]; Vrbo unsegmented since 2019 stated.
- [x] Sovereign for the earnings currency, from the issuing authority, dated (USD 30-year 5.35%, US Treasury,
  09/11/2026, struck this session).
- [x] Value stated as a round-number range (~$35-60 conservative, ~$110-140 optimistic at 6% forever), under the
  COMPUTATION heading.
- [x] One bar (screamer), windage count one.
- [x] Prices dated; aggregator used for the quote only and flagged (US$170.19, 2026-09-11 close, Yahoo via
  `tools/sources.py:price()`).
- [x] Every ledger id cited was checked against `principle_ledger.csv` before citing (all present; the [E4-27]
  incentives row used for what pay vests on, [E4-52] only for the convergence).
- [x] Run committed to git with a pathspec at each stage (Step 0 `21f66bd`, Q1 `b782730`, Q2 `ab67084`, Q3-Q6 and
  audit in the next commit).

**Errors of mine in this run, recorded rather than smoothed:**
1. **A bash heredoc containing apostrophes killed the first Q1 append** (the brief warned of it); nothing was written
   and nothing was lost. All later sections were written to files and appended by `append.py`.
2. **I passed `fts_count()` a phrase wrapped in its own quote marks** (`'"Local Law 18"'`) and got **98** hits for
   Airbnb; the correct call returns **2**. The helper adds quotes itself and does not refuse embedded ones — recorded as
   a tooling defect below. No conclusion was drawn from the inflated count.
3. Draft figures corrected before they reached the run file: repurchase price range ($107-$134 → $107-$140), the
   revenue level at which owner earnings reach zero ($3.7bn → ~$3.5bn), the (c) band width (under 2% → under 5%, the
   incl.-2020 window being 5.2%), the 2019-25 revenue CAGR (19.5% → 16.9%), and the price multiples (33-40× → 32-33×
   TTM). A claim that repurchases were "below the bond at the time" was deleted: the historical sovereign was not struck.

**Tooling and brief defects found:**
- **`tools/sources.py:fts_count()` accepts a phrase that already contains quote marks and silently inflates the count**
  (98 against 2 for "Local Law 18", CIK 0001559720). It guards the CIK and not the phrase. Same defect class as the CALX
  harness: a malformed input returns a plausible number. Not fixed here (this run edits no tool).
- **`tools/run.py` priced ABNB on 2020-2022 only**, because `PaymentsToAcquirePropertyPlantAndEquipment` ends at FY2022:
  the filer moved capex into *"Other investing activities, net"* on the face of the statement and kept it only in the MD&A
  FCF reconciliation. **The triage's [E5-20] label ("the corpus calls [the D&A end] INVALID for this class") was wrong for
  this name** — D&A exceeds capex; the default case applies. The skip reason's generic wording attaches the railroad
  exception to every tag gap.
- **`run.py`'s share basis for ABNB was the diluted weighted average (623.0M)**, 5.7% above the economic cover count; the
  tool warned, correctly. `cover_shares.py`'s sum (598,785,682) includes **Class H, which the balance sheet shows as
  "issued and zero shares outstanding"** (held by a wholly-owned subsidiary) — a 1.6% overcount if summed. The cover calls
  those shares "outstanding"; only the balance sheet does not.
- **The brief's "possibly others" on share classes resolved to Class C (zero) and Class H (subsidiary-held, excluded).**
- **The brief's "funds payable and guest deposits are the owner-earnings trap" was true in kind and smaller in size
  than at PAY**: the host funds run through financing, not operating cash; the trap in OCF is the unearned-fee float and
  the interest on held funds.
- **The brief suggested stock compensation was "likely the centre of the file"**; measured, ABNB's SBC/OCF (49.6% since
  the IPO year, 31.7% ex-2020) sits below CRWD's 68.0% in the calibrated row. The file closed on the franchise question.
- Research dumps were renamed to the gitignored patterns (`10k_`, `10q_`, `8K_`); `s1_424b4.txt` (1.5MB) and the
  companyfacts/submissions JSON match no ignore pattern and were left uncommitted by pathspec.

---
## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT on [E3-03] criterion 2): close substitutes on both sides of the market — hosts and
  property managers list on Airbnb, Vrbo and Booking.com, Booking.com's homes listings nearly doubled to ~3.9 million —
  and the fee record is price defence (take rate 13.4-13.6% flat 2023-25 and below Booking's; a take-rate-neutral
  15.5% single host fee introduced so cross-listed prices compare). Q1 IN. Price US$170.19 × 589,585,682 = US$100.3bn;
  COMPUTATION — NOT A CLEARANCE: owner-earnings yield 1.1-3.1% against USD 5.35%, 6.7-8.8% perpetual growth needed for
  the 10% floor, value roughly $35-60 (conservative) to $110-140 (6% forever) a share; price above the whole range.**
- If UNRESEARCHED — not applicable. If UNKNOWABLE — not applicable.
