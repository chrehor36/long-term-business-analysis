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
