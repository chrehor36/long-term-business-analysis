## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

*Working: `oe.py` / `oe_out.md` in the research folder. Every input is hand-read from the filed consolidated statements of cash flows: FY2017-FY2019
from the FY2019 10-K (`0001045810-19-000023`; FY2017 matched on the FY2017 10-K, `0001045810-17-000027`), FY2020 from the FY2022 10-K
(`0001045810-22-000036`), FY2021-FY2023 from the FY2023 10-K (`0001045810-23-000017`), FY2024-FY2026 from the FY2026 10-K (`0001045810-26-000021`), and
the two half-years from the Q2 FY2027 10-Q (`0001045810-26-000075`), with H1 FY2026 matched on the Q2 FY2026 10-Q. No line differed between vintages. The
FY2018 and FY2020 10-Ks were not needed: every year FY2017-FY2026 sits inside a 10-K on disk. Depreciation is property-and-equipment depreciation from each
10-K's note, not the cash-flow D&A line (Step 0 defect 3).*

### Owner earnings by year, $M **[E2-23]** (OCF less SBC less (c); CONVENTION at VI)
| year | OCF | SBC | OCF−SBC | capex (P&E and intangibles) + financed principal | P&E depreciation | capex ÷ depreciation | **OE, (c) = capex + principal** | OE, (c) = depreciation | acquisitions (Groq in FY2026) |
|---|---|---|---|---|---|---|---|---|---|
| FY2017 | 1,672 | 247 | 1,425 | 176 | 118 | 1.49x | 1,249 | 1,307 | 0 |
| FY2018 | 3,502 | 391 | 3,111 | 593 | 144 | 4.12x | 2,518 | 2,967 | 0 |
| FY2019 | 3,743 | 557 | 3,186 | 600 | 233 | 2.58x | 2,586 | 2,953 | 0 |
| FY2020 | 4,761 | 844 | 3,917 | 489 | 355 | 1.38x | 3,428 | 3,562 | 4 |
| FY2021 | 5,822 | 1,397 | 4,425 | 1,145 | 486 | 2.36x | 3,280 | 3,939 | 8,524 (Mellanox) |
| FY2022 | 9,108 | 2,004 | 7,104 | 1,059 | 611 | 1.73x | 6,045 | 6,493 | 263 |
| **FY2023** | 5,641 | 2,709 | 2,932 | 1,891 | 844 | 2.24x | **1,041** | 2,088 | 49 |
| FY2024 | 28,090 | 3,549 | 24,541 | 1,143 | 894 | 1.28x | 23,398 | 23,647 | 83 |
| FY2025 | 64,089 | 4,737 | 59,352 | 3,365 | 1,300 | 2.59x | 55,987 | 58,052 | 1,007 |
| FY2026 | 102,718 | 6,386 | 96,332 | 6,143 | 2,355 | 2.61x | 90,189 | 93,977 | 14,535 (13,000 Groq) |
| **TTM to 2026-07-26** | 134,360 | 7,241 | 127,119 | 7,474 | 2,972 | 2.51x | **119,645** | 124,147 | 17,100 (incl. 2,944 Groq in financing) |

*(The FY2025 depreciation figure is the note's rounded "$1.3 billion"; FY2026 is D&A of 2,843 less intangible amortization of 488; TTM = FY2026 − H1
FY2026 + H1 FY2027.)*

### Stock compensation: subtracted in full **[E5-06]**; RESOLVES, and the charge is the floor **[E3-70]**
- The cash-flow add-back *"Stock-based compensation expense"* resolves in every year FY2017-TTM from the filed statements. SBC ÷ OCF: **9.2% cumulative
  FY2022-FY2026**, 6.2% in FY2026, 5.4% TTM; far below the 50% level at which the resume state asks for a grant table read by hand.
- **Read anyway, because the market measure is the rule:** the estimated total grant-date fair value of awards granted was **$3,492M, $4,505M, $5,316M,
  $7,834M and $9,389M (FY2022-FY2026), 1.47-1.74x the charge** (10-K stock compensation notes). On grant-date value the five-year mean owner earnings fall
  from $35,332M to **$33,102M**. Shown as a band end, not stacked. Tax withholding on vesting ($7,948M in FY2026) is not added: it buys back part of what
  the charge already counts.

### MORE THAN ONE WINDOW, AND EVERY (c) QUESTION SHOWN BOTH WAYS **[E4-25, E4-38]**
| window | OE, (c) = capex + principal | OE, (c) = depreciation | capex end, less acquisitions | capex end, SBC at grant-date value |
|---|---|---|---|---|
| **5-yr FY2022-FY2026 (the default [E2-42])** | **35,332** | 36,851 | 32,145 | 33,102 |
| 3-yr FY2024-FY2026 | 56,525 | 58,559 | 51,316 | 53,902 |
| 10-yr FY2017-FY2026 (crosses Mellanox) | 18,972 | 19,898 | 16,526 | not computable (grant values not extracted before FY2022) |
| 5-yr FY2017-FY2021 (crosses Mellanox) | 2,612 | 2,946 | 907 | not computable |
| FY2023-FY2025 + TTM (five periods; the TTM overlaps H2 FY2026, stated) | 58,052 | 60,382 | 51,497 | not computed |
| **TTM to 2026-07-26** | **119,645** | 124,147 | 102,545 | 116,240 (FY2026's 1.47x applied to TTM SBC, CONVENTION) |

- **The spread is the wave, and it is enormous:** the TTM is **3.4x** the five-year mean and **6.3x** the ten-year mean; FY2023 alone was $1,041M. By
  **[E3-55]**, volatility around a certain endgame is not a defect; **here the endgame is what Q2 found uncertain**, so the spread is uncertainty about the
  level, not noise around it.
- **[E4-41], normalise the mean down for luck:** the TTM sits at the top of a filed boom (Data Center revenue +117% year on year in Q2 FY2027), with the outlook
  assuming no Data Center compute revenue from China. The favourable exogenous break is the AI buildout itself, and it cannot
  be stripped out by a figure; it is named, and it is why the five-year mean rather than the TTM is the default.
- **Perimeter:** the five-year default does not cross Mellanox (FY2021); the ten-year and FY2017-FY2021 windows do. **Groq sits inside FY2026 and the TTM**,
  and the 10-K says *"No customer contracts, existing products, or equity interests were purchased"*, so it is a purchased technology and workforce, not a
  revenue perimeter. Hugging Face is pending and crosses no window.

### Maintenance capex: a DISCLOSED JUDGMENT with a corpus DEFAULT **[E3-44, E2-41, E5-20, E4-47]**
**THE [E5-20] QUESTION, ASKED ON THE FILING, SEPARATELY FROM THE LABEL. Answer: NOT the exception class on the plant, and the plant is not where (c) lives.**
- **What NVIDIA's own filing says about useful lives:** *"In February 2023, we assessed the useful lives of our property, plant, and equipment. Based on
  advances in technology and usage rate, we increased the estimated useful life of a majority of the server, storage, and network equipment from three
  years to a range of four to five years, and assembly and test equipment from five years to seven years"* (10-K FY2024). **The filer lengthened lives; at
  AMZN the filer shortened them "due to the increased pace of technology development".** From the FY2025 10-K the equipment range reads *"two to seven
  years"* (FY2026: gross *"Equipment, compute hardware, and software | 12,619"* at *"2 - 7"* years). **No instance found**, in the FY2024-FY2026 10-Ks or the
  Q2 FY2027 10-Q, of NVIDIA saying depreciation understates what it must spend to renew its plant.
- **Where the product cadence does its damage: inventory, not plant.** Provisions for inventory and excess purchase obligations **$116M (FY2021), $354M
  (FY2022), $2.17bn (FY2023), $2.2bn (FY2024), $3.7bn (FY2025), $7.2bn (FY2026), $2.1bn (H1 FY2027)**, less releases of $137M, $540M, $689M, $1.5bn and
  $280M (FY2023-H1 FY2027). *"We have experienced and may in the future experience reduced demand for current generation architectures when customers
  anticipate transitions"* (10-K FY2023).
- **Do the provisions belong in (c)? They belong in owner earnings, and they are already there; adding them to (c) would count them twice.** A provision
  reduces net income and reduces the inventory balance (or raises the accrued obligation) by the same amount, so operating cash flow is unchanged in the
  quarter it is booked; **the cash was spent when the inventory was bought, or leaves when the obligation is settled**, and both sit inside OCF. Over any
  multi-year window, the OCF-based owner earnings above already carry the cash cost of every transition in the window. What they do **not** carry is the
  transition not yet taken: the next write-down is inside the **$279bn** of supply commitments, which is exposure, and it is quantified in the named death,
  not guessed into (c).
- **Plant, the corpus default [E3-44]:** capex (with financed principal) ran **1.28-2.61x depreciation** FY2022-TTM while revenue grew 11x. The two plant
  ends differ by **$1.5bn on the five-year mean and $4.5bn on the TTM (about 4% of each)**. **The plant band does not move any conclusion here; the D&A end is not
  INVALID on NVIDIA's filing, and the capex end is used as the stated (c) because it is the more conservative and the difference is immaterial.**

**THE WORKING-CAPITAL INCREMENT [E2-23]: included, through OCF, and it is large.**
- **The flag (a single line above 30% of a period's OCF) fires twice:** FY2023 inventories **−$2,554M (45.3% of OCF)**, the down-year build that preceded the
  provisions; H1 FY2027 accounts receivable **−$24,590M (33.0%)**. Near misses: FY2023 prepaid and other −26.9% (supply prepayments), FY2017 and FY2019
  inventories −22.4% and −20.7%.
- **TTM working capital consumed $40,745M, 30.3% of OCF** (receivables −$35,246M, inventories −$16,648M, prepaid and other −$6,849M, against payables and
  accruals +$15,163M and other +$2,835M), while customer advances rose (deferred revenue note: *"Included $ 15.6 billion and $ 7.5 billion of customer advances for the first half of fiscal years
  2027 and 2026"*).
- **Growth or maintenance?** *For adding it back:* most of the build is the growth [E2-23] does not ask (c) to carry; without it TTM owner earnings would be
  ~$160bn. *Against:* the receivable build is partly the price of volume: *"longer payment terms ranging from 90 days up to one year"* for large customers,
  and *"Financing arrangements with certain investment-grade customers, including extended payment terms under large, multi-quarter agreements, will continue
  to affect the timing of our operating cash flows"* (10-Q MD&A). **Terms extended to keep customers buying are a cost of maintaining unit volume. No
  "ex-working-capital" figure is used; the ~$160bn is displayed only as the most generous number constructible.**

**THE PRIOR I WAS TOLD I AM MOST LIKELY WRONG ABOUT: are the capacity buy-backs, stakes and guarantees purely balance-sheet items outside (c)?** *Built both
ways before ruling.*
- **(a) AI cloud agreements, $36bn.** *The mechanism:* *"AI clouds procure our data center infrastructure products and we commit to cloud service agreements,
  which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates. Our commitments, which are
  typically six years in duration, totaled $36 billion as of July 26, 2026, and decrease as capacity is used by third-party customers or by us for our
  research and development efforts"* (10-Q MD&A; schedule **$6bn FY2028, $8bn FY2029, $7bn FY2030, $6bn FY2031, $9bn after**, nothing in the rest of FY2027).
  *For (c):* the partner buys NVIDIA's systems (revenue now, inside the TTM) **because** NVIDIA stands behind the capacity for six years (cost later, outside
  every window); that is a cost of the unit volume, booked after the volume. *Against:* it is a backstop, not a certain cost; it falls away as third parties
  use the capacity, NVIDIA uses it for R&D, and *"we will participate in revenue share"*. **Ruled: partly (c).** The cost is contingent, so the band is
  **$0 (never called) to ~$6bn a year (fully called, $36bn over six years)**. The revenue booked on these sales is not disclosed (Q3 half-owner gap).
- **(b) Cloud service agreements, $29bn** (*"cloud infrastructure to support our research and development of our open models"*): rented R&D compute, a
  cost of competitive position, **already expensed inside OCF as it is used**. Not added.
- **(c) Equity stakes in customers.** *For (c):* the 10-K says *"These investments include AI model makers that purchase our products directly or through
  CSPs"*, and the 10-Q says the buyers *"currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity"*.
  Where the stake finances the purchase, the cash is a demand-maintenance cost that the cash-flow statement files under investing. *Against:* the stakes
  are assets with market values (*"Gains from equity securities, net | ( 23,707 )"* H1 FY2027) and some are sold (*"Proceeds from sales of equity securities |
  7,241"*); Intel's $5bn is not customer finance; Step 0 ruled the **gains** out of owner earnings, which stands. **Ruled: shown both ways, not chosen.**
  Equity purchases: five-year mean ~$4.0bn (FY2022-FY2026 investing lines, gross: *"Investments and other, net"* 24 and 77, then non-marketable equity
  862, 1,486 and 17,502); **TTM at least $51.4bn** (FY2026 non-marketable
  purchases net 17,418, less H1 FY2026's 1,175, plus H1 FY2027's 35,163; FY2026 public-equity purchases sit inside "Purchases of marketable securities" and
  are not separable on the face).
- **(d) Guarantees ($108.5bn cap) and third-party leases ($20bn).** No cash in any window; the SB Energy guarantees are *"triggered upon certain tenant
  defaults"* and not yet effective. **Ruled: outside (c); exposure, carried to the named death.** Treating a contingent guarantee as an annual cost would
  guess a default rate no document supplies.
- **(e) Groq (~$17bn) and Hugging Face ($11.9bn).** *For (c):* Q2 found the moat is rebuilt by buying the replacement, and Groq is a licence to a rival
  inference architecture, which is [E2-23]'s *"to fully maintain its long-term competitive position"* in its plainest form. *Against:* one-off purchases;
  Mellanox added a business. **Shown both ways** (the "less acquisitions" column).
- **So the prior was half right.** The guarantees are exposure, not (c). **The AI cloud buy-backs are a contingent maintenance cost booked after the
  revenue, and the stakes in buyers are, in part, demand finance filed as investment**; a TTM owner-earnings figure that counts the sale and not the
  financing overstates what owners keep.

**The combined range, stated in dollars (windows × (c)):**
- **Five-year default:** $35.3bn (capex end) → **~$26bn** with the five-year means of net equity purchases (~$4.0bn), acquisitions (~$3.2bn) and SBC at
  grant value (~$2.2bn) all taken as (c); $36.9bn at the depreciation end.
- **TTM:** $119.6bn (capex end) → **~$62bn** with TTM net equity purchases ($51.4bn) and a fully called AI cloud backstop ($6bn) as (c); $102.5bn less
  acquisitions alone; $124.1bn at the depreciation end; ~$160bn before the working-capital build (most generous, not a judgment).
- **The judged central figure is the capex end ($35.3bn five-year, $119.6bn TTM), with the stake and backstop question displayed as the downward band.**
  *Is that range too wide to reach a conclusion [E4-25]?* **For survival, no: every construction is positive, in every window, in every year including
  FY2023.** For value it is a factor of about five from the conservative five-year end to the generous TTM end, and that width is carried to Q5, where it
  does not matter because the price sits above all of it.
- **Look-through [E3-04]: none added** (no undistributed investee earnings are evidenced, and the equity-method income is *"not significant"*).

### Great, good, or gruesome? **[E4-20, E4-43]**
- **[x] great, on the filed record of capital required** · [ ] good · [ ] gruesome
- **Evidence:** after-tax operating income ÷ average operating capital **127% (FY2017) to 212% (FY2025), 181% TTM, 20% in FY2023** (Q3 table); net plant
  $14.3bn carries TTM operating income of $197.6bn; in the six months to 2026-07-26 operating capital rose ~$31bn while after-tax operating income for the half was ~$98bn. That
  is [E4-20]'s great account, *"an extraordinarily high interest rate"*.
- **But [E4-20]'s great account is one whose rate *"will rise as the years pass"*, and two things move the account on the filed record.** (1) The rate is a
  wave: 20% in FY2023, and Q2 found its basis re-won each cadence. (2) **The capital is now going outside operating capital**: $99bn of stakes, $25bn more
  committed, $36bn of buy-backs and $108.5bn of guarantees, none earning a filed cash return. On the operating capital alone the account is great; **counted
  with the capital committed to keep the customers buying, it is travelling toward good**, and at Q2's close no class above good is claimable for the whole.

### Staying power: score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: LARGE, NOT RELIABLE.** Owner earnings $119.6bn TTM; but two filed pauses in seven years: FY2020 revenue
  −6.8% and operating income −25%; FY2023 revenue flat and operating income −58%, owner earnings $1.0bn. **Half.**
- **(2) Massive liquid assets: YES.** Cash $22,443M and marketable debt securities $34,143M (**$56,586M**) at 2026-07-26; marketable equity $42,783M, of which
  *"$36.9bn under short-term lock-up restrictions"* (Step 0 table), not counted; the $25.0bn commercial paper program is undrawn and **not counted** [E5-39].
  **One.**
- **(3) No significant near-term cash requirements: NO.** 10-Q Note 10: **commitments of $120bn due in the remainder of FY2027** (supply and capacity $92bn,
  equity investments $18bn, capital expenditures $7bn, cloud $3bn) and **$100bn in FY2028**; Hugging Face ~$11.9bn on close (expected first half of
  2027; the 8-K does not state the form of payment); accrued Groq consideration $986M; the dividend at $0.25 a quarter (~$24bn a year); repurchase authorization of ~$99.0bn. In a normal year these
  are paid from revenue (TTM OCF $134.4bn). **In a FY2023-type year they are not, and the supply commitments are the part the 10-Q says may be adjustable
  only *"in certain instances"*.** **Zero.**
- **Score: 1.5 of 3.**
- **Leverage, named and quantified [E4-16, E3-29]:** senior notes **$33.5bn** face (from $8.5bn at 2026-01-25; $25.0bn issued June 2026 in seven tranches,
  2028-2056, coupons 4.25%-5.625%), $1.0bn due in FY2027 and $4.75bn in 2028 (Note 9); operating lease liabilities $4,985M long-term plus $25bn of leases not
  commenced for own use and $20bn for third parties; guarantees capped at $108.5bn; equity $228,984M, of which 43.2% is stakes.
- **Coverage [E2-54]:** interest expense TTM **$464M** (FY2026 259 − H1 FY2026 124 + H1 FY2027 329), rising to roughly $1.4-1.5bn a year on the new notes'
  coupons (my arithmetic); against OCF net of capital expenditure of **$127bn** TTM, **met about 90 times over**. [E2-54] is comfortably passed.
- **[E2-60] the third dimension of maintenance (financial strength):** H1 FY2027 distributions and investments exceeded cash generated by ~$18bn and the half
  raised $24.9bn of notes (Q3). Not yet a restricted-earnings finding; recorded as the direction to watch.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: THE ROUND TRIP [#18], from the vendor's side, on top of CONTRACTED NOT TO STOP [#1].** *NVIDIA finances and guarantees the laboratories and
AI clouds whose purchases are its demand, extends them terms of up to a year, stands behind their capacity, and commits $279bn forward to supply them. A
demand pause at an architecture transition, the FY2023 mechanism, arriving while those positions are open would turn one lost year of margin into a capital
loss across inventory, stakes, receivables, buy-backs and guarantees at once, because they are the same few counterparties.* The company does not die;
**the owners' return on several years of the wave does.**

**Exposure, from the filing, not experience [E4-40]:**
- **Supply:** inventory $31,575M and supply and capacity commitments **$279bn**, raised from $119bn in one quarter, *"for long-term demand across current and
  future product architectures"*.
- **The counterparties:** three direct customers were 16%, 15% and 13% of H1 FY2027 revenue; receivables $63,059M; *"one AI research and deployment company
  contributed a meaningful amount of our revenue by purchasing cloud services from our customers"*; stakes of $99bn and $25bn committed; AI cloud buy-backs
  $36bn; SB Energy guarantees capped at $105bn for *"an affiliate of OpenAI Group PBC"*, payable on tenant default, phases from FY2029, each over a 20-year
  lease; land, power and shell guarantees $3.5bn.
- **The regime:** H20 ($4.5bn) and H200 ($0.4bn) charges followed export rules; China's preliminary finding on the Mellanox conditions is open (Q3). A rule
  change is the other filed trigger for a sudden write-down, and it has fired twice in eighteen months.
- **The address (#12, carried, not the death):** *"geopolitical tensions and conflicts, including but not limited to China, Hong Kong, Israel, Korea and Taiwan
  where the manufacture of our product components and final assembly of our products are concentrated"* (10-K FY2026). TSMC is the named foundry; the TSM
  run's shape applies to the supplier and reaches NVIDIA through it.

**Quantified, from filed figures (my arithmetic; the scalings are CONVENTION, confessed):**
- **The FY2023 ratio, scaled.** FY2023 provisions of $2.17bn were **18.7%** of the opening exposure (inventory $2,605M plus inventory purchase and supply
  obligations of $9.00bn at 2022-01-30, FY2022 10-K). The same ratio on 2026-07-26's exposure ($31.6bn plus $279bn) is **~$58bn**. In FY2023 operating
  margin went from 37.3% to 15.7%; the same fall on TTM revenue of $303.0bn takes operating income from $197.6bn to **~$48bn**.
- **The stakes:** $99bn carrying value; a pause that closes the laboratories' funding would mark them down. Half is **~$50bn** (illustrative; non-cash; the
  10-Q itemises no investee, so no filed basis exists for a better figure).
- **The backstop:** up to **$36bn** over six years if the AI clouds' third-party customers disappear; up to **$105bn** over twenty-year leases if OpenAI's
  affiliate defaults after the phases commence, less whatever NVIDIA recovers by hosting its own infrastructure on the site (*"the site will exclusively
  host NVIDIA AI infrastructure"*).
- **Against what survives it:** equity **$229.0bn**; liquid assets $56.6bn; notes $33.5bn with nothing large due before 2028; FY2023 itself, when the
  company stayed profitable, kept paying its dividend and repurchased $10.04bn. **A pause plus a half write-down of the stakes plus the full AI cloud backstop
  (~$58bn + ~$50bn + $36bn = ~$144bn) consumes most of a year's operating income and about 63% of equity, and the company survives it.** Only the pause and
  a laboratory default together, with the guarantees called over years, reach the $105bn cap on top, and no document on disk lets that joint case be sized
  honestly.
- **Likelihood:** the erosion (demand partly financed by the seller, commitments outrunning a quarter's revenue by 2.9x) is **not a possibility but the
  filed present**. **A FY2023-type pause at today's scale is a real possibility**: two filed pauses in seven years, a one-year cadence that invites buyers to
  wait (*"reduced demand for current generation architectures when customers anticipate transitions"*), and an export regime that has twice turned product
  into write-downs. **A laboratory default that calls the guarantees cannot be placed**: no document states OpenAI's finances, and [E4-40] forbids reading
  the last three years of its fundraising as the guide.

**Against the index (18 shapes, six proposed, as read at 2026-09-13 after the AMZN fold):**
- **#18 THE ROUND TRIP (AMZN, proposed)** is the nearest, and NVIDIA is a **later instance from the vendor's side**: Amazon funds the laboratories and sells
  them cloud capacity it builds with borrowed money; NVIDIA funds and guarantees the same laboratories and the AI clouds, and sells them the chips. **The
  difference is where the loss lands:** at Amazon on plant with five-year lives; at NVIDIA on inventory, forward supply, receivables, stakes and guarantees,
  with almost no plant.
- **#1 CONTRACTED NOT TO STOP (ORCL)** is carried beside it: $279bn of supply and $36bn of buy-backs are commitments the business may not recover.
- **#11 THE PASS-THROUGH (TM)** does not fit the record: gross margin has held at ~75% through the transitions; nothing on file shows gains passed to buyers
  outside the FY2023 channel programs and the H200 tariff it could not pass on.
- **#12 THE ADDRESS (TSM)** applies through the supplier and is carried as exposure.
- **No new shape is proposed.** The FY2023 mechanism (the surfer off the wave [E3-51]) is Q2's finding; the death is what the financing does to it.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *The company survives every mechanism quantified from the filing ([E5-11] 1.5 of 3; [E2-54] met ~90x; owner earnings positive in every window and year).
  Great on operating capital, travelling toward good once the capital committed to customers is counted. The owner-earnings level spans about five times
  (~$26bn on the conservative five-year end to $124bn at the TTM depreciation end), which is a Q5 width. The named death is the round trip from the
  vendor's side on top of $279bn of supply: a real possibility of a capital loss of the order of $144bn in a FY2023-type pause, survivable; a joint pause and
  laboratory default is not sizable from any document. Not a finding against the business, and not what closed this file.*

---
