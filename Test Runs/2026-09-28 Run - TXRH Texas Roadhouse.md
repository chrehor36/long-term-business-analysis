# Company Run — Texas Roadhouse, Inc. (TXRH) — 2026-09-28
**WAVE 7, name 93 of 218 (the first name in `Screens/_daily/_wave7_order.txt` not in the done file; the done file held 92 lines, last OPXS, counted from the file). Claimed at dispatch 2026-09-28 by an unattended run agent under the headless cycle's lock (PID 16256); the template copied and committed before any fetch.**

**VERDICT: Q2 OUT.** Q1 IN. The file closes at Question 2, permanently, on the business: the best guest-traffic record in casual
dining (positive every year the filer disclosed it, 2014-2025) was bought with a check that rose less than the category's prices (FY2014-19
+10.4% against +17.0%; FY2022-25 +20.0% against +24.4%), the operating margin sat at 7.6-9.6% for seventeen years, and the filer bounds its
own pricing *"primarily due to competitive reasons"*: [E3-43]'s pricing demonstration runs the wrong way and [E3-03] criterion (2) fails in
the category's filed flows; [E2-58]'s wide-and-sustainable exception is not shown in a ten-filer row that Darden and Brinker lead on returns.
Q3 to Q6 are NOT scored; what was read beneath the close is recorded unscored.
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
Texas Roadhouse sells meals in the United States in dollars; its 61 international restaurants are franchised and pay royalties, and
*"Royalties and franchise fees"* were $30,841K of $5,878,075K of FY2025 revenue (0.5%, domestic and international together, 10-K MD&A).
Earnings currency **USD**; no FX step.
- rate **5.49%** · date **09/25/2026** (the last posted curve day when struck on Monday 2026-09-28 before that day's curve is published;
  09/26 and 09/27 are a weekend) · source **US Treasury daily par yield curve, 30-year, from the issuing authority**.
  `tools/_cache/sov_USD_treasury.csv` was deleted before `tools/sources.sovereign('USD')` ran, so the rate was fetched, not served
  from cache (`step0.py`, output `step0_out.txt`). FRED not used. Struck fresh; it happens to equal the OPXS figure because it is the
  same curve day, not because it was inherited.
- FX / ADR: not applicable.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes  [x] Item 1  [x] Item 1A  [x] Item 7A
- **Annual report: Form 10-K for the fiscal year ended 2025-12-30 (52 weeks), filed 2026-02-27, accession 0001104659-26-021292**
  (`txrh-20251230x10k.htm`).
- **Newest periodic: Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-07, accession 0001104659-26-092408**
  (`txrh-20260630x10q.htm`), with its earnings release (8-K filed 2026-08-06, accession 0001104659-26-091980, EX-99.1).
- **Registrant**: Texas Roadhouse, Inc., CIK 0001289460, Delaware (incorporated 2004), Louisville, Kentucky; large accelerated filer;
  Nasdaq Global Select. **Fiscal calendar**, from the 10-K: *"We operate on a fiscal year that ends on the last Tuesday in December.
  Fiscal year 2025 was 52 weeks in length, and the fourth quarter was 13 weeks in length. Fiscal year 2024 was 53 weeks in length, and
  the fourth quarter was 14 weeks in length."*
- **Figures cross-checked against the filed statement.** The consolidated statement of cash flows in the FY2025 10-K prints (table cells as extracted, pipes separating columns) *"Net cash
  provided by operating activities | 730,067 | 753,629 | 564,984"* (FY2025, FY2024, FY2023) against the companyfacts tag
  `NetCashProvidedByUsedInOperatingActivities` of 730.1M / 753.6M / 565.0M; the same statement's *"Depreciation and amortization |
  206,640 | 178,157 | 153,202"*, *"Share-based compensation expense | 47,765 | 47,055 | 34,230"* and *"Capital expenditures—property and
  equipment | ( 387,996 ) | ( 354,341 ) | ( 347,034 )"* each equal their tags (`series.py`, output `series_out.txt`). Every figure checked
  equals the printed one.
- **Prior filed workpaper used, and re-verified where it matters.** The DRI run of 2026-09-04 built a TXRH peer workpaper from nine
  TXRH 10-Ks FY2016-FY2025 with accessions (`Test Runs/_research 2026-09-04 DRI/peer_TXRH.md`): the traffic and check split by year,
  the menu-price actions, AUV, the dividend record. Its FY2025 and FY2024 lines were re-read here in the FY2025 10-K and agree (MD&A table, cells as extracted: guest
  traffic 2.8% and 4.4%, per person average check 2.1% and 4.1%, comparable restaurant sales 4.9% and 8.5%), and the price
  actions of Q2 and Q4 2024 and 2025 word for word (quoted at Q2).

**Price and shares.**
- Price **$159.75**, Nasdaq Global Select close **2026-09-25** (Friday), Yahoo chart endpoint via `tools/sources.price`,
  `regularMarketTime` 1790366400 (2026-09-25) checked; last eight closes $170.07 (09-16) to $159.75. **Aggregator, used for the live
  quote only, flagged.** No split events in the chart record.
- Shares **65,640,926**: the cover of the **10-Q for the quarter ended 2026-06-30, filed 2026-08-07, accession
  0001104659-26-092408**, reads *"The number of shares of common stock outstanding were 65,640,926 on July 29, 2026."*
  `python Screens/cover_shares.py TXRH` returned *"Common Stock, par value $0.001 per share 65,640,926"* from the same accession.
  **One class**: the 10-K and 10-Q carry no second class of common stock (a search of both for "Class A" and "Class B" returns nothing);
  nothing summed. The FY2025 year-end count was 65.94M (tagged `CommonStockSharesOutstanding`); 415,133 shares were repurchased in the
  26 weeks to 2026-06-30.
- **Market cap: $159.75 x 65,640,926 = $10,486M ($10.49bn).**

**Deal check (the screen's `deal_note`, blank; checked anyway).** The filer list since the 10-K of 2026-02-27 carries four 8-Ks: 2026-03-05
(Items 5.02, 7.01; accession 0001104659-26-024099; read: the appointment of Lisa Ingram, CEO of White Castle System, to the board), 2026-05-07
and 2026-08-06 (Items 2.02, 8.01, 9.01; quarterly results), and 2026-05-22 (Item 5.07; the annual meeting vote). No Item 1.01 or 2.01, no
S-4, DEFM14A, SC TO, SC 13E3 or 425. The only Item 1.01 in the two years before is the 2025-04-24 unsecured revolver (8-K accession
0001104659-25-039415, Items 1.01, 1.02, 2.03). **No deal; the quote is an owner-earnings price, not a spread.** The franchise acquisitions
($107.5M in FY2025, $71.8M in the 26 weeks to 2026-06-30) are the company buying its own franchisees' restaurants under
*"pre-determined formulas"*, recorded at Q4 as capital spent outside (c).

---
## THE SCREEN ROW: carried UNLABELLED, a set of claims and not a finding

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`: `cap_m 13062 · oe_bottom_m 258 · oe_top_m 461 · spread 0.786 · deal_note,
name_change_note, wc_note blank · yield_bottom 0.0197 · vs_sovereign −0.0338 · growth_required 0.0803 · level_shift 1.84 "STEP UP -
normalize down [E4-41]" · best_year_dep 0.073 "no single-year dependence (9-yr OCF series)" · level_shift_oe 1.86 "STEP UP - normalize
down [E4-41]" · best_year_dep_oe 0.105 · level_shift_full 2.66 · years_filed 17 · spread_caveat "4-construction width only (3y/5y x two
capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25]" · newest_filing 2025-12-30 · newest_periodic
2026-06-30`. Each field used is reproduced or refuted in this file; the list is gathered at the end. **First finding: `cap_m` 13,062 is
stale.** On today's count it implies about $199 a share; the close of 2026-09-25 gives $10,486M, 20% lower.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words.** Texas Roadhouse owns and runs 714 sit-down restaurants (648 Texas Roadhouse steakhouses, 56 Bubba's
33 sports bars, 10 Jaggers counter-service burger shops) and franchises 102 more, 61 of them abroad. A Texas Roadhouse is an 8,000
square-foot box with 270 to 325 seats, open for dinner on weekdays, that sold **$8.687M** in FY2025 (Bubba's 33 $6.283M). The company
buys beef (about half of food cost: *"Approximately half of our food and beverage costs relate to beef"*), cuts the steaks in each
restaurant, bakes the rolls there, and sells a moderately priced meal. Of each sales dollar in FY2025, food and drink took 35.0 cents, labour
33.3, rent 1.6 and other restaurant costs 14.6, leaving a **restaurant margin of 15.5%**; depreciation, pre-opening and head office take it
to an **operating margin of 8.1%** ($474.7M on $5,878.1M). The money is made by volume through a fixed box: the same kitchen, lease and
managers carry more covers. Growth is new boxes, about $8.3M each all in (*"In 2025 and 2024, our average capital investment for Texas
Roadhouse restaurants was approximately $8.3 million and $8.0 million"*), plus buying back franchisees' restaurants. Customers pay at
the table, so the company carries no receivables to speak of and holds $448.7M of customers' money in unredeemed gift cards; *"Our
operations have not required significant working capital [...] Sales are primarily for cash"*.

**The scarce input this business controls.** Not a patent, a licence or a site monopoly. What it holds is an **operating system**: a
managing partner in each restaurant who puts up a refundable deposit, signs a multi-year contract and is paid *"a percentage of
pre-tax income of the restaurant(s) they operate or supervise"*, with market partners over them and product and service coaches visiting;
and the habit of the guests that system has earned (guest traffic positive in every year the filer disclosed it, 2014-2025, below).
Whether that is a franchise in [E3-03]'s sense or the execution of *"a business"* **[E3-43]** is the Q2 question.

**Will the fundamentals look broadly the same in ten years?** Yes in mechanism: a steak dinner at a moderate price in a big box is the same
product it was in 1993, and the filer's own record shows the same unit economics across three decades. The input that moves is the price
of beef (commodity inflation 6.1% in FY2025, 7.0% in Q2 2026) and wages. The business is *"relatively simple and stable in character"*
**[E3-31]**.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no
> close substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's
> ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."* **[E3-03]**

### Altitude, first: who is the customer?

The diner. 714 of 816 restaurants are company-run and royalties and franchise fees are 0.5% of revenue, so this is an owner-operator, not
a franchisor: **the MCD precedent (2026-09-03, Q2 IN on the franchisee locked into a 20-year site) does not transfer**, for the reason the
DRI run gave when it declined it. Criterion (2) is asked at the table: does the guest who eats at a Texas Roadhouse think it has no
close substitute? The customer chooses again at every meal at no cost. That puts the file where the DRI run (2026-09-04, Q2 OUT) put
Darden: the route to IN is either a filed demonstration of [E3-43] (the ability *"to regularly price its product or service
aggressively and thereby to earn high rates of return on capital"*), or [E2-58]'s exception, *"a cost advantage that is both wide and
sustainable"*. Both are tested below. The Texas Roadhouse concept is the business (648 of 714 company restaurants; Bubba's 33 and
Jaggers are 66 together), so the company and the concept are scored as one (the ABT question, below).

### THE STRONGEST EVIDENCE AGAINST THE LEADING READING: written first (operator rule 9, [E4-26], [E3-41])

The leading reading after the filings and the precedents was OUT. The case against it, as strongly as the filings make it:
1. **The best physical series in the restaurant cohort [E4-55].** Guest traffic at company restaurants, as filed in each year's MD&A,
   was **positive in every year the filer disclosed it, FY2014 through FY2025** (eleven disclosed years; FY2020 was withheld, *"we do not
   believe that our per person average check and guest traffic counts provide a meaningful comparison to the prior year period"*):
   +3.2%, +5.4%, +2.1%, +3.6%, +3.9%, +1.8% (FY2014-FY2019), +27.6% (FY2021, reopening), +1.9%, +5.4%, +4.4%, +2.8% (FY2022-FY2025), and
   **+3.8% in the 26 weeks to 2026-06-30** (10-Q traffic table, cells as extracted: 3.0% Q2 2026, 4.0% Q2 2025, 3.8% YTD 2026, 2.6% YTD 2025). Traffic compounded **+21.7% FY2014-FY2019** and **+15.3% FY2022-FY2025**. The EAT run said it in its own row: *"the
   cohort's DURABLE physical series belongs to TXRH (11 of 12 years)"*; the DRI run: *"Only TXRH's record is better in the whole row."*
2. **The highest volume per box in casual dining.** Texas Roadhouse AUV **$8.687M** (FY2025) against Olive Garden $5.8M, LongHorn $5.6M,
   Chili's $5.0M and Outback $4.0M in the DRI run's row; record average weekly sales of $177,252 in Q2 2026. The filer adds seats and
   parking at *"our high volume restaurants"* to meet demand.
3. **High returns on capital, held for sixteen years [E3-46].** Operating income over net tangible operating assets (the DRI run's
   formula, applied uniformly below): **23.2% to 25.8% every year FY2010-FY2019**, 2.8% in FY2020, then **33.4%, 34.0%, 32.1%, 42.9%,
   34.0% (FY2021-FY2025)**. No debt at FY2025; customers fund $448.7M of the balance sheet through unredeemed gift cards.
4. **The attacker has come and the traffic held [E2-45].** Chili's (EAT) ran its traffic from −6.9% (FY2023) to +16.0% (FY2025) on a
   $10.99 value bundle; LongHorn, owned by the largest operator in the category with *"ample capital and skilled personnel"*, grew its
   guests about 21% on FY2019. Through both, Texas Roadhouse traffic stayed positive (+4.4% FY2024, +2.8% FY2025, +3.8% 2026 YTD).
5. **The founder died in 2021 and nothing moved [E4-23].** W. Kent Taylor is *"Our late founder"*; the CEO since March 2021 is a
   managing partner of 1997. Traffic, AUV and returns after 2021 are higher than before. The moat, whatever it is, did not go with the
   surgeon.
6. **Untapped pricing power is a live reading [E3-33].** A company that prices below the category, fills its boxes and has to add seats
   is the shape Munger describes: *"any manager could raise the return enormously just by raising prices, and yet they haven't done it."*

That is a real case, and it is weighed against what follows.

### (1) Needed or desired: PASSES

$5.8bn of restaurant sales, 816 restaurants, traffic rising for twelve years.

### (3) Not subject to price regulation: PASSES

Menu prices are set by the company *"individually in each local market"*. Minimum and tipped wage laws regulate a cost, not the price.
**The ABBV question (criterion (3) at the company or the product level) does not arise**: no product or company price is administered.

### (2) No close substitute, and [E3-43]'s demonstration: FAILS on the pricing half, in the filer's own words and the filed series

**The pricing half runs the wrong way: for twelve years the check rose LESS than the category's prices, and the traffic was bought with
it.** Set against the BLS consumer price index for food away from home (CPI-U, series CUUR0000SEFV, annual averages, fetched from
api.bls.gov 2026-09-28, `prices.py`, output `prices_out.txt`):

| FY | guest traffic | per person average check | food-away-from-home CPI, year on year | check less CPI |
|---|---|---|---|---|
| 2014 | +3.2% | +1.5% | +2.4% | −0.9 |
| 2015 | +5.4% | +1.8% | +2.9% | −1.1 |
| 2016 | +2.1% | +1.4% | +2.6% | −1.2 |
| 2017 | +3.6% | +0.9% | +2.3% | −1.4 |
| 2018 | +3.9% | +1.5% | +2.6% | −1.1 |
| 2019 | +1.8% | +2.9% | +3.1% | −0.2 |
| 2020 | withheld | withheld | +3.4% | |
| 2021 | +27.6% | +10.2% | +4.5% | +5.7 (reopening; to-go mix) |
| 2022 | +1.9% | +7.8% | +7.7% | +0.1 |
| 2023 | +5.4% | +4.7% | +7.1% | −2.4 |
| 2024 | +4.4% | +4.1% | +4.1% | 0.0 |
| 2025 | +2.8% | +2.1% | +3.7% | −1.6 |

**FY2014-FY2019: check +10.4% against the category +17.0%; traffic +21.7%. FY2022-FY2025: check +20.0% against +24.4%; traffic +15.3%;
the menu-price actions themselves compound to +18.5%** (Q2 2022 3.2%, Q4 2022 2.9%, Q2 2023 2.2%, Q4 2023 2.7%, Q2 2024 2.2%, Q4 2024 0.9%,
Q2 2025 1.4%, Q4 2025 1.7%, from the peer workpaper's filed table and, for 2024-2025, the FY2025 10-K: *"Per person average check for 2025
includes the benefit of menu price increases of approximately 1.4% and 1.7% implemented in Q2 2025 and Q4 2025, respectively. We
implemented menu price increases of approximately 2.2% and 0.9% in Q2 2024 and Q4 2024, respectively."*). *(Check includes mix and is not
pure price; the filer says so: "Menu price changes, the mix of menu items sold, and the mix of dine-in versus to-go sales can affect the
per person average check amount." The CPI is a national all-outlets index. Both limits are stated and neither reverses the direction.)*
**In real terms the Texas Roadhouse check has fallen, and the guests came for that.** It is **[E2-44]**'s first characteristic
(*"an ability to increase prices rather easily"*) run backwards, and the opposite of what carried the two restaurant names that passed Q2
in this project (below).

**The margin shows where the value went: to the guest.** Operating margin, every tagged year: **8.1% (FY2009), 9.0%, 8.6%, 8.7%, 8.4%,
8.2%, 8.0%, 8.6%, 8.4%, 7.6%, 7.7%, 1.0% (FY2020), 8.6%, 8.0%, 7.6%, 9.6%, 8.1% (FY2025)**, a band of two points for seventeen years
outside the pandemic year, through a period in which the category's prices rose 57% (CPI 243.1 in 2013 to 382.4 in 2025). The company
priced to hold the margin level, not to widen it, and when beef rose it let the margin fall: restaurant margin *"decreased to 15.5% in
2025 compared to 17.1% in 2024 [...] primarily due to commodity inflation of 6.1% and wage and other labor inflation of 3.7%"*, and again
in Q2 2026 to 16.4% on *"commodity inflation of 7.0%"*. **The filer names the limit itself, in Item 1A and Item 7A:** *"Extreme and/or
long term increases in commodity prices could adversely affect our future results, especially if we are unable, primarily due to
competitive reasons, to increase menu prices."* And among the factors that move its sales: *"our ability to implement menu price increases
without negatively impacting guest traffic or average check size"*. **That is [E4-37]'s agony metric in the filer's words**
(*"it's not a great business when you have to have a prayer session before you raise your prices a penny"*); the pricing policy is
*"we focus on remaining disciplined as we balance short-term pressures with long-term growth while always keeping our guest top of mind.
Prices are reviewed individually in each local market"*.

**What the returns are made of.** The 23-43% return on net tangible operating assets is real and it is made of **volume through a fixed
box**, not of price: the highest AUV in the row at the lowest real check growth, a building and a kitchen carrying more covers. That is
[E3-43]'s other sentence, word for word: *"In contrast, "a business" earns exceptional profits only if it is the low-cost operator or if
supply of its product or service is tight. [...] With superior management, a company may maintain its status as a low- cost operator for
a much longer time, but even then unceasingly faces the possibility of competitive attack. And a business, unlike a franchise, can be
killed by poor management."* **Texas Roadhouse is that business: the value operator kept at the front by superior management**, with a
managing partner paid a share of each restaurant's pre-tax income. The advantage is **[E4-36]**'s *"extreme performance over many
factors"* (cut-to-order steaks, scratch rolls, low table-to-server ratios, dinner-only weekdays, local marketing), which the corpus lists as
a cause of extreme success and which is not an ownable position.

**Criterion (2) in the customers' behaviour and the filer's words.** The filer: *"The restaurant industry is intensely competitive. We
compete with many well-established food service companies on the basis of taste, quality, and price of products offered [...] improving
product offerings of fast-casual and quick- service restaurants, together with negative economic conditions could cause consumers to
choose less expensive alternatives."* The category: the same three years moved guests out of Outback (−15.1% FY2022-FY2025) and Olive
Garden (−4.5% FY2023-FY2026) and into Texas Roadhouse (+15.3%), LongHorn (+6.5% FY2023-FY2026) and Chili's (+14.2% FY2022-FY2026), each
figure filed by its company (the DRI and EAT runs' workpapers). **That guests are won by value, at a real check that falls, is the evidence
that they are not held by the absence of a substitute** (the reading of the EAT run: *"Share moves this fast in both directions only where
substitutes are close [E3-03](2)"*, which is an inference from the filed series and labelled so here too). A guest who came for the
price will compare the price.

### [E2-58]'s exception, tested: the cost advantage is not WIDE in the row, and the owner does not keep it

The advantage, if it is one, is delivered to the customer as a lower real check, so the owner's return is the place to look for
"wide". It is not there:

### THE COMPETITOR ROW, required [E3-28]

Metric: **operating income over revenue, and operating income over net tangible operating assets (total assets less cash, short-term
investments, goodwill, intangibles and operating right-of-use assets, less current liabilities other than current debt and current
lease liabilities: the DRI run's NTOA), each summed over the filer's own last five fiscal years**, from each filer's SEC companyfacts
(`peers.py`, output `peers_out.txt`, summary `peers_summary.txt`). The subject's inputs reconcile to its 10-K (operating income 474,740;
revenue 5,878,075). Traffic from each filer's MD&A, via the DRI, EAT and CMG runs' workpapers.

| Company (SEC filer) | format | op. margin, last 5 FYs | OI / NTOA, last 5 FYs | op. margin, last 10 tagged FYs | physical series through the price wave |
|---|---|---|---|---|---|
| **Texas Roadhouse (TXRH, subject)** FY2021-25 | steakhouse, owner-operated | **8.4%** | **35.5%** | **7.8%** | traffic **+15.3%** FY2022-25; positive every disclosed year 2014-2025 |
| Darden (DRI) FY2022-26 | Olive Garden, LongHorn, fine dining | 11.7% | 39.7% | 10.0% | OG guests −4.5%, LongHorn +6.5% FY2023-26 |
| Brinker (EAT) FY2022-26 | Chili's, Maggiano's | 7.1% | 47.4% | 6.7% | Chili's +14.2% FY2022-26 (+16.0% in FY2025 alone) |
| Bloomin' Brands (BLMN) FY2021-25 | Outback, Carrabba's | 5.3% | 29.4% | 3.7% | Outback −15.1% FY2022-25 |
| Cheesecake Factory (CAKE) FY2023-25 (three years; FY2018-22 untagged) | Cheesecake Factory, North Italia | 4.4% | 21.0% | 5.0% | orders −21.5% FY2017-25 |
| Cracker Barrel (CBRL) FY2022-26 | family dining and retail | 2.1% | 8.7% | 5.5% | not rowed |
| BJ's Restaurants (BJRI) FY2021-25 | brewhouse casual dining | 0.8% | 2.1% | 1.5% | not rowed |
| Red Robin (RRGB) FY2021-25 | burgers, casual dining | −2.3% | negative | −3.1% | not rowed |
| First Watch (FWRG) FY2021-25 | daytime casual | 3.3% | 12.1% | 1.2% (FY2019-25) | not rowed |
| Kura Sushi USA (KRUS) FY2021-25 | conveyor sushi | −2.9% | negative | −3.7% | not rowed |
| *Chipotle (CMG) FY2021-25, the fast-casual precedent* | *counter service* | *15.0%* | *63.5%* | *11.7%* | *transactions +19.5% 2021-25 on menu price +34.3%* |

- **Peers named: ten** SEC-filing US restaurant operators (nine sit-down, plus CMG as the precedent that passed). **Not rowed, with the
  obstacle:** LongHorn and Olive Garden are segments of DRI (their guest counts are rowed from DRI's MD&A); Outback is inside BLMN;
  Applebee's and IHOP (Dine Brands) are franchisor P&Ls, not the same formula; private steakhouses (Logan's Roadhouse, Saltgrass, and the
  independents the filer names as competitors) file nothing. Denny's did not resolve in the SEC ticker map. **The EAT figure differs from
  the EAT run's own 82.1% because this row applies one formula and one set of tags to every filer; the ranking does not change.**
- **What the row shows.** Texas Roadhouse is in the top half and **not at the top on either measure**: Darden earns more on revenue in
  nine of its last ten fiscal years (the exception is its pandemic year to May 2020, 0.6% against Texas Roadhouse's 1.0% for calendar
  2020) and more on its operating assets over five; Brinker earns more on its operating assets; Chipotle earns
  nearly twice as much. Its margin is in the middle of the row and has not moved in seventeen years. **A cost advantage that is both
  "wide and sustainable" [E2-58] would show as an owner's return the row cannot match. The row matches it.** Whatever Texas Roadhouse's
  advantage is, the guest gets it, not the owner, which is why the traffic is the best in the row and the return is not.
- **The limit [E3-61]:** the row shows position, never conduct. The spread between Texas Roadhouse and Outback, two steakhouses in the same
  suburbs, is the spread between two managements, which is exactly [E3-43]'s *"a business [...] can be killed by poor management"*.

### Precedents, followed and distinguished in writing

- **DRI (2026-09-04, Q2 OUT): followed.** Its test (*"The only route to IN for an owner-operator in this category is [E2-58]'s named
  exception [...] plus [E2-53] dominance economics"*) is applied here unchanged, and it fails here for the same reason: the returns are not
  category-unique. The DRI run named this company as the refutation of Darden's scale claim (*"The scarce input DRI claims (scale) is
  demonstrably not required to match DRI's returns or to beat its traffic"*); the same row now shows Texas Roadhouse's own advantage
  is not wide against Darden's.
- **EAT (2026-09-05, Q2 OUT): followed.** Its reading of the category (guests moving both ways, on value, inside two years) is followed;
  Texas Roadhouse is the other side of the same flows, the operator that won the guests the losers lost.
- **BLMN (2026-09-21, Q2 OUT on criterion (2), on the company's own Item 1): followed** in kind. Outback is the direct steakhouse
  comparison and the losing half of the same substitution.
- **CMG (2026-09-05, Q2 IN NARROW): distinguished, on [E3-43]'s pricing half.** Chipotle took menu price **+34.3%** over 2021-2025 against
  a category that rose **+30.1%** (2020 to 2025 annual averages) and grew transactions **+19.5%**, and its operating margin went from
  **6.0% (2017) to 16.2% (2025)**: price above the category, volume up and the owner's margin widening, both halves of [E3-43]. Texas
  Roadhouse's check rose **less** than the category over each span it disclosed, and its margin did not move. Same physical strength; the
  opposite pricing record.
- **SBUX (2026-09-04, Q2 IN): distinguished, on the same half.** That run passed on *"real price +20% captured FY2019-25 and HELD through a
  two-year traffic decline"*. Texas Roadhouse captured negative real price and grew traffic; the SBUX test, applied here, does not pass.
- **MCD (2026-09-03, Q2 IN as a franchisor): not applicable** (altitude, above).

### The other Q2 tests, scored

- **[E3-33] / [E5-28], untapped pricing power: claimed by the strongest-evidence case, not established.** Claiming the class is claiming
  *"a monopoly or a near monopoly"* **[E5-28]**; the row shows LongHorn and Chili's growing guests in the same years at similar or lower
  checks, and the filer says its ability to raise prices is bounded *"primarily due to competitive reasons"*. No filing records a price
  rise above the category that held traffic. The class cannot be claimed on a record of pricing below it.
- **[E4-37], the agony metric:** reads agony, in the filer's words (above).
- **[E2-45], the attacker's test:** answered in part for the subject (traffic held through Chili's and LongHorn's gains) and in full for
  the category (Chili's took +16.0% of traffic in a single year with a price point). An attacker with capital and a value menu can move
  casual-dining guests inside two years; that Texas Roadhouse has not yet been the one to lose them is its management's record, not a
  structure that stops it.
- **[E2-53], dominance:** not shown. Texas Roadhouse is one of several chains and many independents in every market it names; the
  marketplace, not its position, set Outback's and Olive Garden's outcomes in the same years.
- **[E4-32], direction:** traffic and AUV widening; the owner's margin flat for seventeen years; restaurant margin narrowing in FY2025 and
  2026 on beef. The widening is in the guests' favour.
- **[E4-23], key-person dependence:** not the defect (point 5 above). The dependence is on a system of managing partners, and the filer
  lists *"Competition for these employees is intense"* among its risks.
- **[E4-04], verdict form:** not the perimeter close. There is no technology to judge and no rebuilt-from-zero basis; the filings decide the
  franchise question themselves. **OUT on the business, not UNKNOWABLE.**
- **[E4-47], inflation:** the record through 2021-2025 is of a business that did **not** retain its earning power in real dollars per
  guest; it held a nominal margin by growing volume.

### The three open operator questions, both readings written and not decided (PRIME RULE 5)

- **The ABT question ([E3-03] at the whole company or segment by segment).** *Segment by segment:* the Texas Roadhouse segment is the
  business (648 of 714 company restaurants, AUV $8.687M); Bubba's 33 (56 restaurants, AUV $6.283M, restaurant margin 15.2% in 2026 YTD)
  sells burgers, pizza and beer in the most substitute-dense corner of the category; Jaggers is ten counter-service restaurants. Each fails
  (2) on the same evidence or more of it. *Whole company:* the same. **Does not move this file.**
- **The ABBV question ([E3-03] criterion (3) at the company or the product level).** No price is regulated at either level. **Does not
  arise.**
- **The CAT question (whether [E2-58]'s wide-and-sustainable exception is for commodity products only).** *If only for commodities:* a
  Texas Roadhouse dinner is a branded, differentiated meal, the exception does not apply, and the file turns on [E3-03] (2) and [E3-43],
  which fail above: **OUT**. *If not only for commodities (the reading CAT's run applied, carried by Caterpillar's construction margin above
  Deere's in all fifteen years):* the exception is tested in the row and is not wide: Darden's margin is higher in nine of its last
  ten fiscal years and Brinker's and Darden's returns on operating assets are higher over five: **OUT**. **Does not move this file.**

### Class and verdict

- Needed or desired [x] · no close substitute [ ] (fails: the guests are won by a check that rises less than the category's prices, the
  filer bounds its pricing *"primarily due to competitive reasons"*, and the category's guests move between chains inside two years) ·
  not price-regulated [x]
- Must the moat be continuously rebuilt? The position is re-won at every meal by execution, the class **[E3-43]** calls *"a business"*,
  which *"unceasingly faces the possibility of competitive attack"*. Great manager required? Not one person; a system of operators, which is
  the same finding at the level of the business.
- Primary moat metric, filing-sourced, and its trend: guest traffic (positive every disclosed year 2014-2025) against the real check
  (below the category's prices over FY2014-19 and FY2022-25), with the operating margin flat at 7.6-9.6% for seventeen years.
- Class: **[ ] WIDE  [ ] NARROW  [x] NONE** (a superbly executed value operator; [E2-58]'s exception tested and not established) ·
  Direction: guests widening, the owner's margin flat.

**VERDICT: [x] OUT**

**Asked aloud, per [E4-19]: can I name the document that would resolve this?** Nothing further needs to be fetched. The traffic and check
split is filed for eleven of twelve years; the category's price index is public; the filer states its own pricing limit; the row is built
from ten filers. **OUT on the business, permanent, and not the [E4-04] perimeter close.** This is a finding that the business is not a
franchise in [E3-03]'s sense, not a finding that it is badly run: every number above says it is run very well, and that is the point of
[E3-43]'s last sentence. Q3 to Q6 are not scored; what was read is recorded beneath the close.

---
## Q3 to Q6: NOT SCORED. The file closed at Q2, OUT on the business.

⛔ Q3, Q4, Q5 and Q6 are not scored; no verdict below. What was read is recorded so a later reader does not have to
refetch it. Nothing here promotes or rescues the file **[E2-37, E2-38, E3-39]**.

---
## THE SCREEN ROW, ANSWERED

| Field | Screen | Finding |
|---|---|---|
| `deal_note` | blank | **CONFIRMED** (Step 0): four 8-Ks since the 10-K, a board appointment, two results releases and a vote; no merger, tender or going-private form |
| `cap_m` | 13,062 | **STALE**: implies about $199 a share on today's count; at the 2026-09-25 close, $159.75 x 65,640,926 = **$10,486M** |
| `oe_bottom_m` | 258 | **REPRODUCES** as the five-year window at the capex end, **$257.8M** (below) |
| `oe_top_m` | 461 | **REPRODUCES** as `tools/run.py`'s three-year window at the D&A end with acquired-intangible amortization left inside (c), $461M; on depreciation excluding that amortization the three-year top is $464.4M and the five-year $407.7M |
| `spread` | 0.786 | reproduces as 461 / 258 − 1, a width across two windows (a three-year top over a five-year bottom); the spread inside the five-year window is 58% |
| `yield_bottom`, `vs_sovereign` | 1.97%, −3.38% | struck on the stale cap and an older 5.35%; today the five-year bottom is **2.46%** against **5.49%** |
| `growth_required` | 8.03% | reproduces as ~10% less 1.97%; a derivative of the two fields above |
| `level_shift` 1.84, `level_shift_oe` 1.86, `level_shift_full` 2.66, "STEP UP - normalize down [E4-41]" | | **CONFIRMED as a step up, REFUTED as a windfall**: the rolling five-year mean rose from $54M (to FY2013) to $258M (to FY2025) at the capex end, and the filings attribute it to store weeks and AUV (units roughly doubled; AUV $4.8M in FY2016 to $8.7M in FY2025), which is growth, not luck. The one favourable break **[E4-41]** names is inside the window: FY2024 had a 53rd week (*"lapping the benefit of the additional week which added $114.7 million in revenue in 2024"*) |
| `best_year_dep` 0.073, "no single-year dependence (9-yr OCF series)" | | **CONFIRMED in effect, REFUTED on the series length**: no single year carries any window (the largest, FY2024, is 27% of the five-year capex-end sum), but the filed operating-cash series is **seventeen** years, FY2009-FY2025; FY2009-FY2014 sit under `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`, which the screen's series did not reach |
| `years_filed` | 17 | reproduces as FY2009-FY2025 |
| `spread_caveat` | "4-construction width only [...] rebuild it" | answered: every trailing window 1-17 years, every rolling five-year window and the TTM, both (c) ends, below |
| `newest_filing`, `newest_periodic` | 2025-12-30, 2026-06-30 | reproduce |

---
## COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Arithmetic beneath a closed file. It carries no entry language, no value range and no ranking.*

**Construction** (`oe.py`, output `oe_out.txt`): operating cash as filed (FY2015-FY2025 `NetCashProvidedByUsedInOperatingActivities`,
FY2009-FY2014 `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`, the latest filing's figure; FY2023-FY2025 checked against
the FY2025 10-K statement), less stock compensation in full **[E5-06]** (the cash-flow add-back *"Share-based compensation expense"*,
resolving in every year FY2009-FY2025, $7.5M to $47.8M, 6.1% to 12.8% of operating cash; the plans are service- and performance-based
restricted stock units and all run through that line), less (c) at two ends: **depreciation excluding the amortization of acquired
intangibles** (reacquired franchise rights, $6.5M in FY2025; untagged for FY2009-FY2010 and taken as zero there, flagged) and **total
capital expenditures**. No net-income proxy (operator rule 5). $M.

| FY | Operating cash | SBC | Depreciation | Capex | Franchise acquisitions (outside (c)) | OE, capex end | OE, depreciation end |
|---|---|---|---|---|---|---|---|
| 2009 | 115.1 | 7.5 | 41.8 | 45.5 | 0 | 62.1 | 65.8 |
| 2010 | 120.1 | 7.7 | 41.3 | 45.1 | 0 | 67.3 | 71.1 |
| 2011 | 136.4 | 10.5 | 41.6 | 79.7 | 0 | 46.2 | 84.3 |
| 2012 | 148.0 | 13.2 | 45.6 | 87.0 | 4.3 | 47.8 | 89.2 |
| 2013 | 173.8 | 14.7 | 50.0 | 111.5 | 0 | 47.6 | 109.1 |
| 2014 | 191.7 | 14.9 | 57.5 | 125.4 | 0 | 51.4 | 119.3 |
| 2015 | 227.9 | 22.8 | 68.3 | 173.5 | 0 | 31.6 | 136.8 |
| 2016 | 257.1 | 26.1 | 81.8 | 164.7 | 0 | 66.3 | 149.2 |
| 2017 | 286.4 | 26.9 | 92.6 | 161.6 | 16.5 | 97.9 | 166.9 |
| 2018 | 352.9 | 34.0 | 100.5 | 156.0 | 2.2 | 162.9 | 218.4 |
| 2019 | 374.3 | 35.5 | 114.8 | 214.3 | 1.5 | 124.5 | 224.0 |
| 2020 | 230.4 | 29.4 | 117.3 | 154.4 | 10.6 | 46.6 | 83.7 |
| 2021 | 468.8 | 38.1 | 126.0 | 200.7 | 0 | 230.0 | 304.7 |
| 2022 | 511.7 | 36.7 | 134.4 | 246.1 | 33.1 | 228.9 | 340.6 |
| 2023 | 565.0 | 34.2 | 150.2 | 347.0 | 39.2 | 183.7 | 380.6 |
| 2024 | 753.6 | 47.1 | 176.0 | 354.3 | 0 | 352.2 | 530.6 |
| 2025 | 730.1 | 47.8 | 200.2 | 388.0 | 107.5 | 294.3 | 482.1 |

**Every trailing window ending FY2025, against the cap of $10,486M:** one year **$294.3-482.1M (2.81-4.60%)**; two $323.3-506.4M
(3.08-4.83%); three $276.8-464.4M (2.64-4.43%); four $264.8-433.5M (2.53-4.13%); **five (the corpus default [E2-42]) $257.8-407.7M,
2.46-3.89%**; six $222.6-353.7M (2.12-3.37%); seven $208.6-335.2M (1.99-3.20%); eight $202.9-320.6M (1.93-3.06%); nine $191.2-303.5M
(1.82-2.89%); ten $178.7-288.1M (1.70-2.75%); eleven to sixteen from $165.4-274.3M (1.58-2.62%) down to $130.0-218.2M (1.24-2.08%);
**seventeen $126.0-209.2M (1.20-2.00%)**. **Rolling five-year windows** (capex end / depreciation end): to FY2013 $54.2M/$83.9M, FY2014
$52.1M/$94.6M, FY2015 $45.0M/$107.8M, FY2016 $49.0M/$120.7M, FY2017 $59.0M/$136.3M, FY2018 $82.0M/$158.1M, FY2019 $96.6M/$179.1M, FY2020
$99.6M/$168.4M, FY2021 $132.4M/$199.5M, FY2022 $158.6M/$234.3M, FY2023 $162.7M/$266.7M, FY2024 $208.3M/$328.0M, FY2025 $257.8M/$407.7M.
**TTM to 2026-06-30** (FY2025 less the 26 weeks to 2025-07-01 plus the 26 weeks to 2026-06-30, from the 10-Q's cash-flow statement):
operating cash $803.3M, SBC $51.4M, capex $396.9M, D&A $222.3M, depreciation about $215.8M (the half-year intangible amortization is not
tagged in the 10-Q; FY2025's $6.5M used, flagged): **$355.0-536.1M, 3.39-5.11%**.

- **Every window sits below the 5.49% bond at both ends, and no window reaches the ~10% the corpus quits on [E4-28].** Owner earnings
  were positive in every one of the seventeen years at both ends; the bottom never approaches zero.
- **(c) is a disclosed guess [E2-09] [E3-44], and here the filing says where it sits.** Capex ran 1.1x to 2.5x depreciation because the
  company is building restaurants. The FY2025 10-K splits it (table cells as extracted): *"New company restaurants | $ | 180,783"*,
  refurbishment or expansion $135,817K, relocation $43,626K, the Support Center $27,770K (its $22.8M purchase, one-time); FY2024 $198,367K,
  $122,905K, $25,633K, $7,436K. The spend on existing restaurants (refurbishment, expansion and relocation) was **$179.4M in FY2025 and
  $148.5M in FY2024, against depreciation of $200.2M and $176.0M**: [E3-44]'s default holds for this filer, and maintenance sits near the
  depreciation end, some of the "expansion" being seats added to full restaurants, which is growth.
- **Capital spent outside (c), recorded:** franchise restaurants bought back from franchisees, $179.8M over FY2021-2025 ($107.5M in FY2025,
  $71.8M more in the 26 weeks to 2026-06-30). With them counted as capital the owner spent, the five-year capex-end figure is $221.9M (2.12%).
- **Working capital is a source, not a use** ([E2-23]'s increment is not required here): customers prepay $448.7M of gift cards and the
  company runs negative working capital, as its MD&A says.

---
## BENEATH THE CLOSE: Q3 MATERIAL, RECORDED WITHOUT A VERDICT

- **Weight case, not declared as a verdict:** daily execution is the live determinant **[E3-38]** (a value operator kept at the front by
  its managers, [E3-43]'s *"a business, unlike a franchise, can be killed by poor management"*); no leverage; no control.
- **What pay vests on [E4-27]** (DEF 14A filed 2026-04-10, accession 0001104659-26-041771): the 2025 cash bonus, *"50% of the target incentive bonus was based on whether the Company achieves an annual EPS growth target of 10% (the “ EPS Performance Goal ”) and the remaining 50% was based on a profit sharing pool (the “ Profit Sharing Pool ”) comprised of 1.75% of the Company’s pre-tax profits"* (spacing inside the quoted labels as extracted); the 2025 performance units the same, with EPS growth targets of *"10%"*, *"21%"* and
  *"33%"* over one, two and three years against FY2024. **EPS growth is the metric [E2-01] defines itself against** (*"and not the
  achievement of consistent gains in earnings per share"*), and buybacks move it; recorded as a prompt, not scored. No return-on-capital
  measure in pay. Restaurant managing partners are paid a share of their restaurant's pre-tax income, which is a return on a fixed box.
- **[E4-29]:** "EBITDA" does not appear in the FY2025 10-K, the 10-Q or the Q2 2026 release; the release's non-GAAP measure is restaurant
  margin, reconciled to income from operations with the filer's own caveat that it *"is not indicative of overall company performance"*.
  The proxy uses an EBITDA multiple once, to price the purchase of franchise restaurants in which the CEO held 2% (below). Prompt, not
  fired.
- **Related party:** on 2025-12-31 the company bought five Southern California franchise restaurants, two of which the CEO owned 2% of;
  *"Mr. Morgan received $518,400 in total for his ownership interest"*, and the proxy states he *"was not involved in the overall
  negotiation"*. The franchise agreements carry *"pre-determined formulas"* for such purchases. Recorded.
- **Capital allocation, recorded:** buybacks of $150.0M in FY2025 for 869,007 shares (about $172.6 average), $70.8M for 415,133 shares
  in the 26 weeks to 2026-06-30 (about $170.5), against $913.3M for 22.8M shares at $40.01 average from 2008 to 2025; dividends $180.3M in
  FY2025, $0.75 a quarter declared for 2026; $50.0M drawn on the revolver at 2026-06-30 in the same half-year as $70.8M of buybacks and
  $98.7M of dividends. [E5-08]'s second condition would need an intrinsic value this file does not compute; not scored.
- **[E2-01]:** net income attributable $405.6M in FY2025 on average equity of about $1,410M, about 29%, with no funded debt at year end.

## BENEATH THE CLOSE: Q4 MATERIAL, RECORDED WITHOUT A VERDICT

- **Staying power [E5-11]:** no borrowings at FY2025 and $50.0M at 2026-06-30 against a $450.0M unsecured revolver to 2030-04-24; cash
  $134.7M at FY2025; operating-lease right-of-use assets $879.5M (556 of 714 company restaurants on leased land; *"158 of the 714 company
  restaurants have been developed on land which we own"*); gift-card deferred revenue $448.7M, a customer-funded, covenant-free liability.
- **Concentration:** beef is *"Approximately half of our food and beverage costs"*, bought *"primarily from four beef suppliers"* that
  *"represent a significant portion of the total beef marketplace"*; 101 company restaurants in Texas and 50 in Florida.
- **Great, good or gruesome [E4-20]:** not scored. Each new box costs about $8.3M and the return on operating assets has held 23-43%, the
  shape of [E4-43]'s good class; recorded, not a verdict.
- **Survival shape, as a signature WITHOUT a verdict (Q4 was never opened):** **#11 THE PASS-THROUGH** (the company survives and grows,
  and the gain of its execution is passed to the guest as a real check that falls, while beef, sold by four packers, sets the cost; the
  owner's margin has not moved in seventeen years). No new shape.

---
## TOOLING, REPORTED NOT PATCHED (operator rule 8; a tool may never add a number)

- **`tools/run.py TXRH`** (output `runpy_out.txt`) builds "D&A" from `DepreciationDepletionAndAmortization`, which **includes the
  amortization of reacquired franchise rights** ($6.5M in FY2025, $2.2M in FY2024, $3.0M in FY2023), so its depreciation end counts an
  acquisition's amortization as maintenance capital; its three-year top of $461M reads $464.4M on depreciation alone. **The fourth form of
  the acquired-amortization defect already on record.** It defaults to a **three-year** window and prints the corpus's five-year window as
  "THE OTHER WINDOW"; its *"3. POINTS OVER THE SOVEREIGN -0.22 .. +1.61"* rests on the unprinted growth assumption in `points_over()`, and
  its *"2. GROWTH THE PRICE ASSUMES 4.7% (at a 5.49% rate)"* is struck against the bond, not the ~10% floor [E4-28]; reported, not used.
- **The screen's operating-cash series stops at FY2015** for this filer (its own note says *"9-yr OCF series"*), though FY2009-FY2014 are
  tagged under `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations` (`tools/run.py` does read both tags). Any screen field
  built on the shorter series cannot see the pre-2015 level.
- The screen's `spread` divides a three-year top by a five-year bottom, so it is a cross-window width and not the capex band of either
  window; its own `spread_caveat` half-says this.

---
## Q6: THE REVERSAL CONDITION, IN WORDS (no band, no alert; FOLD step 4, the QLYS ruling)

The file failed on the business, so a price alert would be a category error. **The file reopens only on a filed change in what the
business is**: a multi-year record, in the MD&A's own traffic and check split, of the per person check rising faster than the category's
prices while guest traffic holds, with the operating margin rising out of the 7.6-9.6% band it has held since 2009, that is, [E3-43]'s
pricing half demonstrated; or a row in which the owner's return on operating assets stands clear of Darden's and Brinker's through a
cycle, which is [E2-58]'s "wide". None of these is a price.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT; Q3-Q6 not scored and labelled so.
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict. [x] No UNKNOWABLE verdict; the [E4-04] perimeter close was considered and refused in writing.
- [x] Step 0: the 10-K FY2025 (0001104659-26-021292) and the 10-Q to 2026-06-30 (0001104659-26-092408) read, with the Q2 2026 release
  (0001104659-26-091980), the 8-K of 2026-03-05 and the DEF 14A of 2026-04-10; operating cash, D&A, SBC and capex cross-checked against the
  filed statements.
- [x] Owner earnings on every trailing window 1-17 years, every rolling five-year window and the TTM at both (c) ends, beneath the close,
  headed COMPUTATION — NOT A CLEARANCE; **no net-income proxy**; SBC resolves in every year FY2009-FY2025; the depreciation end excludes
  acquired-intangible amortization.
- [x] Competitor row filled: ten SEC filers on one formula and each filer's own last five fiscal years, the subject reconciled to its
  10-K; the segments and private chains that cannot be rowed named with their obstacle.
- [x] Strongest evidence against the leading reading written first (operator rule 9).
- [x] Precedents read and applied or distinguished in writing: DRI, EAT, BLMN followed; CMG and SBUX distinguished; MCD not applicable.
  The ABT, ABBV and CAT questions written both ways and not decided.
- [x] Sovereign for USD from the US Treasury, dated 09/25/2026, struck fresh.
- [x] Value not stated (Q5 not opened). No bar chosen (Q5 not opened).
- [x] Price dated 2026-09-25, aggregator, flagged; shares from the latest periodic cover.
- [x] Every ledger id in this file checked present in `principle_ledger.csv` before writing; ledger rows quoted as stored.
- [x] Run committed to git at the claim, after Step 0/Q1, after Q2, and at the close.
- [x] **Own error, corrected here and not in history (operator rule 6):** the message of the close commit (`bc8c047a`) gives the
  trailing-window range as "$126.0-482.1M (1.20-4.83%..." with a stray ellipsis; the file's figures are right: across the seventeen
  trailing windows $126.0-506.4M (1.20-4.83%, the top being the two-year window), and $126.0-536.1M (1.20-5.11%) with the TTM. The commit
  is not amended.
- [x] Fold: register entry 235 (234 before, OPXS at 234, heading unique at line 502), done file 93 lines ending TXRH, next GWW.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **TXRH, 2026-09-28, FAIL AT Q2 (OUT on the business).** Price $159.75 (Nasdaq close 2026-09-25, aggregator, flagged) x
  65,640,926 shares (10-Q to 2026-06-30 cover, 0001104659-26-092408) = $10,486M, against 5.49% (US Treasury 30-year par, 09/25/2026). The
  best guest-traffic record in casual dining (positive in every year the filer disclosed it, 2014-2025) was bought with a per person check
  that rose less than the food-away-from-home CPI (FY2014-19 +10.4% against +17.0%; FY2022-25 +20.0% against +24.4%), the operating margin
  held at 7.6-9.6% for seventeen years, and the filer bounds its pricing *"primarily due to competitive reasons"*: [E3-43]'s pricing half
  runs the wrong way and [E3-03] criterion (2) fails in the category's filed flows; [E2-58]'s exception is not wide in a ten-filer row
  (five-year OI/NTOA 35.5% against Darden 39.7%, Brinker 47.4%). Beneath the close, owner earnings $126.0-536.1M (1.20-5.11%) across every
  window and the TTM, five-year $257.8-407.7M (2.46-3.89%). No band, no PORTFOLIO row.
