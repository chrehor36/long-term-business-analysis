# R V - run. Visa Inc. (NYSE: V), under the v5 drafts. Regression run, 2026-10-04.

Binds nothing. Run under `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`. Purchase questions under
`Framework/v5/DRAFT - THE FRAMEWORK v5.md`; Q11 under `Framework/v5/DRAFT - THE HOLDINGS FRAMEWORK v5.md` (the operator
holds this name). Every id below is a row of `principle_ledger_v5.csv`. Working files: `Framework/v5/tests/_work_R_V/`.

**Filings read (all SEC EDGAR, CIK 0001403161 unless stated):**

| Short name | Document | Filed | Accession |
|---|---|---|---|
| 10-K | Form 10-K, fiscal year ended 2025-09-30 | 2025-11-06 | 0001403161-25-000089 |
| 10-Q | Form 10-Q, quarter ended 2026-06-30 | 2026-07-29 | 0001403161-26-000104 |
| PROXY | DEF 14A for the 2026-01-27 annual meeting | 2025-12-08 | 0001308179-25-000635 |
| 8-K/S | Form 8-K, Item 8.01, escrow deposit and class B conversion-rate cut | 2026-09-23 | 0001403161-26-000121 |
| MA 10-K | Mastercard Inc. Form 10-K, year ended 2025-12-31 (CIK 0001141391) | 2026-02-11 | 0001141391-26-000013 |

---

## 0. Step 0

- **Price.** $360.66, close 2026-10-02. Source: aggregator, **flagged** (operator rule 5: live quotes only). `tools/run.py`
  printed the same figure from its aggregator.
- **Share count by class**, from the 10-Q cover (as of 2026-07-21; `python Screens/cover_shares.py V`): class A
  1,704,112,694; class B-1 2,180,148; class B-2 486,669; class B-3 60,589,871; class C 17,059,152. The arithmetic sum
  (1,784,428,534) is **not** a share count. The charter note in the 10-Q (Note 11, Stockholders' Equity, "As-converted
  class A common stock") gives each class's conversion rate into class A: B-1 1.5445, B-2 1.5014, B-3 1.4953, C 4.0000;
  the series A, B and C preferred convert to about 7m, 1m and 2m class A (as of 2026-06-30). Dividends and diluted EPS
  are computed on that as-converted basis (10-Q Note 11 and Note 13), so the economic count is the as-converted one:
  A 1,704.1m + B-1 3.37m + B-2 0.73m + B-3 90.60m + C 68.24m + preferred about 10m = about 1,877m. The 8-K/S then cut the
  as-converted B-3 count from 90,599,965 to 89,510,039 and B-1/B-2 by about 14 thousand, a reduction of about 1.1m after a
  $405m escrow deposit. **Working count: about 1,876m as-converted class A shares.** (The B-1/B-2/B-3 figures above
  reproduce the 8-K/S's own "from" figures exactly, which cross-checks the conversion arithmetic.)
- **Market cap.** 1,876m x $360.66 = **about $677bn** (`python tools/run.py V --shares 1876`: 676.60B).
- **Sovereign, earnings currency USD.** US Treasury daily par yield curve, 30-year, **5.63% on 10/02/2026** (issuing
  authority; `tools/run.py` fetched the same).
- **Cross-check of a tagged figure against the filed statement (operator rule 4).** `tools/run.py` reads operating cash
  flow FY2025 as 23,059 and purchases of property, equipment and technology as 1,482 ($m); the 10-K's consolidated
  statement of cash flows shows "Net cash provided by (used in) operating activities | 23,059" and "Purchases of
  property, equipment and technology | ( 1,482 )". They agree.
- **Tool output set aside.** `tools/run.py` also printed v4 ids ([E4-28], [E4-21], [E3-28], [E3-42]), a "~10% floor"
  and an owner-earnings yield. Those are v4 constructs; they are ignored here and nothing below rests on them.

## 1. The foundations

Three bear on this name. **A share is a business** **[M1997-109]**: Visa is a toll on card payments, and the question is
whether I would hold it with the market shut. **Margin of safety** **[M1996-084]**, **[M1997-126]**: the price sits at
about 30 times trailing earnings, against a long government rate of 5.63%, so whatever comes out at Q7 will turn on
whether the case will "scream at you" or needs a pencil. **Who is paid to tell you** **[M2020-037]**: Visa's MD&A leads with
non-GAAP results that leave out a litigation provision every year, and the proxy pays on an adjusted EPS, so management
is paid more for one reading of the numbers than another. **The analyst's habits** **[M2016-054]**: the operator already
holds this name, and "the worst anchoring effect [...] is always your previous conclusion". No macro forecast enters
**[M2000-094]**. The 5.63% rate is used as the yardstick, not as a forecast.

## 2. The standing rule

This run takes no position and changes no financing. The rule is the buyer's: never risk what one has and needs
**[M2012-081]**, **[L2023-005]**, and no borrowed money behind a stock **[L2014-005]**, **[M2020-022]**. The session may not
open `PORTFOLIO.md`, so it cannot see how the operator's holding is financed or sized. It records the condition: the rule
is met if the holding is unlevered and the operator could watch it "go down 50 percent — or more — and be comfortable
with it" **[M2020-022]**.

## 3. Q1 to Q8 in order

### Q1. Can I understand it? STOP.

**Test as stated.** "a reasonable fix on about what the earning power and competitive position will look like in five or
10 years" **[M2012-065]**; the key variables and how predictable they are **[M1998-044]**; whether the past statements tell
me the future ones **[M2008-033]**; whether the forecast is about customers or about technology **[M2017-019]**,
**[M2023-030]**; whether I can name the winner, not only the industry **[M2012-067]**; whether it is a financial
institution whose condition cannot be read **[M2001-066]**.

**Applied.** The 10-K (Item 1, "Our Core Business") states the economics in two lines: Visa earns service revenue on
payments volume and data-processing revenue on processed transactions, and "Visa is not a financial institution. We do
not issue cards, extend credit or set rates and fees for account holders [...] nor do we earn revenue from or bear credit
risk". The key variables are four and are all disclosed (10-K, MD&A): nominal payments volume ($13,894bn, +7% for the
twelve months to June 2025), processed transactions (257,545m, +10%), the pricing of the fee schedule ("select pricing
modifications" named in three revenue lines), and client incentives ($15,751m, +14%). Their record is regular: net revenue
$32,653m, $35,926m, $40,000m for FY2023 to FY2025, and $33,764m for the nine months to June 2026, +15% (10-Q). The
forecast is of consumer and merchant behaviour (the shift of spend from cash to cards and tokens) more than of a
technology; the technology risks (account-to-account rails, stablecoins, agentic commerce, all named by Visa itself in
Item 1) go to Q2, which owns change. The winner is named, not just the industry: two global networks, of which Visa is
the larger. The one feature that looks like a financial institution, the settlement guarantee (10-Q Note 9: maximum daily
settlement exposure $168.6bn, average $99.5bn, collateral $9.5bn), is disclosed in figures and is read at Q9.

**Verdict: IN.** The economics ten years out can be pictured from the filings, inside the perimeter **[M2012-065]**,
**[M1998-044]**, **[M2008-033]**. Doubt noted and carried, not hidden: "if you have doubts about something being into your
circle of competence, it isn’t" **[M2002-092]**. The doubt here is about the threats to the castle, not about how the
money is made, so it is carried to Q2.

### Q2. Why is the castle still standing? STOP.

**Test as stated.** The castle questions **[M1995-038]**; the money test **[M2011-015]**, **[M1997-103]**; pricing power
**[M2005-020]**, **[M2000-031]**; would the customer still choose it over the low bid; ask the competitors **[M1999-130]**;
widening or narrowing **[M1999-108]**, **[L2005-010]**; what could destroy it five to fifteen years out **[M2000-014]**.

**Applied.**
1. *What keeps it standing.* Acceptance at "more than 175 million merchant locations" and "nearly 5 billion payment
   credentials" issued by "nearly 14,500 financial institutions" (10-K, Item 1). Each side joins because the other is
   there. That is a reason the customer comes, and a reason it lasts, of the kind **[M1995-038]** asks for.
2. *The money test.* A new entrant needs both sides at once. The filing's own competitor set is Mastercard, American
   Express and domestic and account-to-account networks; none has replicated global two-sided acceptance. "if you gave
   me a hundred billion dollars [...] I wouldn’t have the faintest idea of how to do it" **[M1997-103]** reads true here
   on the filed numbers; the answer to **[M2011-015]** is no.
3. *Pricing power.* Service, data-processing and other revenue each rose in FY2025 partly on "select pricing
   modifications" while payments volume still grew 7% and transactions 10% (10-K, MD&A). "Anytime you can charge more
   for a product and maintain or increase market share [...] you have something very special" **[M2000-031]**.
4. *The low bid.* Merchants have litigated interchange against Visa since 2005 (MDL 1720, 10-K Note 20) and kept
   accepting; the 10-Q reports settlements with merchants "representing approximately 95 %" of the opt-out volume.
   "if you have a business where your customers are mad at you and you’re growing, you know, that has met a certain test,
   in my mind, of utility" **[M2000-032]**; also **[M2013-043]**.
5. *Ask the competitor, same metric, from its own filing* **[M1999-130]**, **[M2022-021]**. GAAP operating margin
   (operating income / net revenue): Visa FY2025 23,994 / 40,000 = **60.0%**; Mastercard 2025 18,897 / 32,791 = **57.6%**
   (MA 10-K, Consolidated Statements of Operations). Before each company's own litigation line (Visa "Litigation
   provision" 2,562; MA "Provision for litigation" 504): Visa **66.4%**, Mastercard **59.2%**. Capital spent per dollar of
   net revenue: Visa 1,482 / 40,000 = **3.7%**; Mastercard (489 property and equipment + 726 capitalized software) / 32,791
   = **3.7%**. Volume growth: Visa total payments volume +7% nominal (twelve months to June 2025); Mastercard GDV +9%
   USD (2025); cross-border, Visa +13% nominal, Mastercard +15% local. So Visa earns more on each dollar of revenue for
   the same capital, while Mastercard grew volume a little faster.
6. *Widening or narrowing* **[M1999-108]**. Two signs of a notch: Mastercard's faster volume growth (item 5), and client
   incentives rising as a share of gross revenue, 27.4% (FY2023), 27.7% (FY2024), 28.3% (FY2025) (10-K revenue table:
   incentives / (net revenue + incentives)), which is the price paid to issuers to keep their cards on the network. Signs
   of widening: value-added services revenue $7.2bn, $8.8bn, $10.9bn (10-K), and nine-month FY2026 net revenue +15%
   (10-Q). Read together: holding, with a slow rise in the cost of keeping issuers.
7. *What could destroy or reduce it* **[M2000-014]**. Named in the filings: the US Department of Justice suit of
   2024-09-24 alleging monopolization of debit network services, seeking to enjoin the agreements (motion to dismiss
   denied 2025-06-23; 10-K Note 20); debit class actions copying it (amended 2026-02-27; 10-Q Note 16); UK Competition
   Appeal Tribunal findings that certain interchange rates restrict competition (June 2025) and were not passed on
   (2026-02-18), with new European merchant claims filed April to June 2026 (10-Q Note 16); and a challenge to the
   forward-looking release in the class settlement (Potayto-Potahto, 2026-04-21). The rows warn that a regulated moat can
   break **[L2023-011]** and that the card business was called "very competitive" thirty years ago **[M1996-036]**. Against
   that, twenty years of this litigation sit beside revenue growing about 10% a year and a margin above the rival's.

**The case for TOO HARD, stated so it can be weighed.** "when we see a moat that’s tenuous in any way [...] we leave it
alone" **[M2000-019]**; slow change "can lull you to sleep" **[M2014-038]**. If the debit suit or a routing mandate
reprices the network, the forecast moves. I judge the threats as major, not life-threatening: they bear on the fee
schedule and on debit routing, not on the two-sided acceptance that is the castle, and the record of the last twenty
years is of a toll that survived caps and suits. That is a judgment, and the next analyst may place it in the "too hard"
box **[M2006-013]**.

**Verdict: IN.** The castle stands on two-sided acceptance a funded attacker cannot buy **[M1997-103]**, **[M2011-015]**,
with price rises carried by volume **[M2000-031]** and customers who sue and stay **[M2000-032]**; the moat is holding, not
plainly widening (incentive share and Mastercard's growth), and the threats are graded major **[M2000-014]**.

### Q3. How much capital must go in, and what does the added capital earn? WEIGHING.

**Applied.** Operating income FY2025 $23,994m (after a $2,562m litigation provision) against "Property, equipment and
technology, net" of $4,236m (10-K balance sheet). Tangible equity is negative: total equity $37,909m against goodwill
$19,879m and intangible assets $27,646m (10-K), because the large intangibles came from the Visa Europe purchase and
later deals. Capital spending was $1,059m, $1,257m, $1,482m (FY2023 to FY2025) while net revenue rose by $7.3bn over the
two years; acquisitions were $915m (FY2024) and $887m (FY2025) (10-K cash flow statement). The business "gives you more and
more money every year without putting up anything to get it, or very little" **[M1998-081]**, measured as return on
tangible assets **[M2011-060]**. Reported return on equity is not used: equity is shrunk by buybacks and could be made
"whatever you want" **[M1998-017]**; the rows ask that a high return be checked for leverage **[L1994-009]**, and here the
return on operating tangible assets is high without the debt.

**Verdict: WEIGHS FOR.** Little capital in, rising earnings out **[M1998-081]**, **[L2009-012]**, **[M2011-060]**.

### Q4. Do the numbers show what it earns? STOP on confusion, otherwise WEIGHING.

**Applied.** The class structure and the two retrospective responsibility plans are complicated but fully disclosed:
covered US litigation is paid from an escrow that Visa funds, and the cost is recovered by cutting the class B
conversion rates, which "have the same effect on earnings per share as repurchasing the Company’s class A common stock"
(8-K/S). Share-based compensation ($897m FY2025) is expensed and is **not** removed from non-GAAP results (10-K
reconciliation), which meets **[L2015-003]** and **[L2021-003]**. Two tells are present. First, non-GAAP results remove the
"Litigation provision" in every year shown (pre-tax $906m FY2023, $434m FY2024, $2,533m FY2025; 10-K reconciliation) and
it recurs in FY2026 ($1,290m for nine months, 10-Q). A cost that recurs every year is a cost **[M1999-023]**,
**[L2016-007]**, and "a management that regularly attempts to wave away very real costs by highlighting "adjusted
per-share earnings" makes us nervous" **[L2016-006]**. Second, the FY2025 non-GAAP figures also remove severance
($213m) and lease-consolidation charges. Depreciation: capital spending ($1,482m) exceeded depreciation and amortization
($1,220m, of which $218m is amortization of acquired intangibles), so the shortfall is subtracted, not added back
**[L2015-004]**, **[M1998-127]**; acquired-technology amortization is not added back either, since "With software [...]
amortization charges are very real expenses" **[L2012-003]**.

**The earnings figure carried to Q7** (all from the 10-K and 10-Q): GAAP net income, trailing four quarters to 2026-06-30,
= 17,502 (nine months FY2026) + (20,058 - 14,968) (fourth quarter FY2025) = **$22.6bn**, with litigation counted as a
cost. Less the trailing excess of capital spending over depreciation and amortization (1,567 - 1,342 = about $0.2bn):
about **$22.4bn**. The cash version, operating cash flow less share pay less capital spending, trailing: 22,580 - 919 -
1,567 = **$20.1bn**, lower because litigation accrued earlier was paid out of escrow in FY2026 (10-Q: "Accrued litigation |
( 1,758 )"). Range carried: **$20bn to $22.5bn**, or about $10.70 to $12.00 per as-converted share.

**Verdict.** STOP on confusion: **IN** (not triggered; the accounts are dense but they explain themselves **[M1994-018]**,
**[M1995-063]**). WEIGHING: **WEIGHS AGAINST, lightly**: the featured adjusted earnings leave out a litigation cost that
recurs every year **[L2016-006]**, **[L2016-007]**.

### Q5. Who runs it? STOP on integrity, WEIGHING on ability.

**Applied.** Chief executive Ryan McInerney since February 2023, president from May 2013 to January 2023 (PROXY,
director biography); an independent board chair, John F. Lundgren, since January 2024 (PROXY). The record against the
hand dealt **[M1994-008]**: net revenue +10% and +11% in the two full years of his tenure and +15% in the nine months to
June 2026, with a GAAP operating margin above Mastercard's (Q2, item 5). Owners' treatment from the proxy **[M1994-009]**:
see Q6, Part B. The integrity question: the DOJ complaint alleges monopolization and is unproven; the shareholder
securities class action built on it was dismissed "without leave to amend on June 29, 2026" (10-Q Note 16). An antitrust
allegation about a dominant network's contracts is not evidence of personal dishonesty; it is carried to Q12, the
newspaper test. Reading the reports **[M1998-038]**, **[M2007-083]**: the 10-K opens with "Our purpose is to uplift
everyone, everywhere by being the best way to pay and be paid" and the proxy runs to 119 pages; that is the house style
**[M1998-038]** calls a turnoff, a small weight, not a doubt about honesty.

**Verdict.** Integrity: **IN**. No doubt of the kind **[M2013-088]** or **[M2015-047]** names was found in the filings read.
Ability: **WEIGHS FOR**: a long inside record and results ahead of the hand dealt **[M1994-008]**; and the business would
stand a lesser manager **[M1996-037]**.

### Q6. What will they do with the money and with the owners? WEIGHING.

**Part A, the money.** Visa keeps almost nothing: FY2025 repurchases $18,316m and dividends $4,634m against net income
$20,058m, partly funded by $3,924m of new senior notes (10-K cash flow statement); accumulated income fell from $17,289m
to $15,106m to $12,753m (10-K, 10-Q balance sheets). For a business that cannot use its earnings, paying them out is
right **[M2008-104]**, **[M2004-089]**. Buybacks: 54m shares for $18.2bn in FY2025 and 50m at an average $328.29 in the
nine months to June 2026 (10-Q Note 11); the programme is set in dollars ("$30.0 billion" April 2025, "$20.0 billion"
April 2026, "no expiration date") and the 10-K says repurchases "will be executed at prices we deem appropriate". It names
no price above which it stops, the thing **[L2016-002]** calls puzzling, and gives owners no value estimate, the caveat
in **[L1999-023]**. Whether the buying is below value depends on Q7: at about $328 it sat near the bottom of the range
found there, so it was probably not harmful; but it was not shown to be bought at a discount **[L2011-003]**,
**[M2015-074]**. Deals: Featurespace for $946m in cash (10-K); no all-stock deal, so the one STOP in Part A
**[L2009-019]** does not arise.

**Part B, pay, board, owners.** CEO total compensation FY2025 $31,560,660 (PROXY, Summary Compensation Table),
about 0.16% of net income. Equity is 25% options, 25% restricted stock units, 50% performance shares; the performance
shares pay on an annual "EPS – PS adjusted" goal (FY2025 result $11.37 against GAAP diluted EPS $10.20) times a relative
TSR modifier against the S&P 500; the 2023 grant paid at 162.7% of target (PROXY). For: the EPS goal is corrected if
buybacks run "significantly above or below" budget (PROXY, "Impact of Stock Repurchases on EPS"), which blunts the
equity-shrinking route **[M1998-017]**; an independent chair separate from the chief executive **[L2014-026]**; clawback,
anti-hedging and anti-pledging rules (PROXY). Against: options at a fixed strike with no step-up for retained earnings
**[L1994-021]**, and the proxy does not name the dividend conflict **[L2005-014]**, **[M2003-018]**; a peer group and an
independent consultant set the size **[L2005-015]**, **[M2004-016]**; the TSR modifier pays partly for the market's ride;
the EPS paid on is the adjusted figure of Q4; the proxy is 119 pages **[M2009-087]**. Directors' fees: the chair
$642,391, others about $430,000 to $450,000 (PROXY); directors' holdings are small (the largest non-executive holding
32,376 shares) and the proxy does not say whether they were bought or granted **[L2019-008]**, **[L2002-033]**. The rows
rank all of this below the manager himself **[M2007-006]**.

**Verdict: WEIGHS AGAINST, lightly.** Payout is right for the business **[M2008-104]**; buybacks without a stated price
or value **[L2016-002]**, **[L1999-023]** and conventional peer-set pay on an adjusted EPS **[L2005-015]** weigh against;
none reaches a STOP.

### Q7. What is it worth: how much cash, how sure, how soon, at the long government rate, as a range; and is the price so far below it that it needs no pencil? STOP.

**How much cash.** Owner cash, from Q4: $20bn to $22.5bn a year now, nearly all of it paid out (Q6), so "how soon" is
now, year by year **[L2000-021]**, **[M2009-004]**, **[R1996-018]**. **How sure.** The moat and the people enter here
**[M1999-104]**: a castle judged IN with major threats unresolved (Q2), and a management weighed for ability. **The rate.**
5.63%, the long Treasury, with no risk premium added **[M1996-025]**, **[M1998-151]**; certainty is taken in the margin, not
the rate **[M1997-126]**.

**The arithmetic (CONVENTION, labelled as the draft requires).** The draft gives no growth path; I use a two-stage
projection, ten years at a stated growth then a lower rate for ever, *CONVENTION: the simplest form that keeps growth
below the discount rate after year ten, as **[M1997-095]** and **[M1999-067]** require*. Inputs: starting cash $20bn and
$23bn; ten-year growth 4% to 10% (payments volume grew 7% nominal and net revenue 10% to 15%; growth above that is not
assumed to last **[M2002-052]**, **[M1999-024]**); later growth 0% to 3%. Results per as-converted share
(`_work_R_V/value.py`):

| Starting cash | 10-yr growth | then 0% | then 2% | then 3% |
|---|---|---|---|---|
| $20bn | 6% | $305 | $419 | $541 |
| $20bn | 8% | $357 | $495 | $642 |
| $23bn | 6% | $351 | $482 | $622 |
| $23bn | 8% | $411 | $569 | $738 |

The 4% and 10% rows run from $260 to $1,240 a share. Read the other way, the price of $360.66 implies about 4% to 6% a
year for ten years and 0% to 2% thereafter.

**The range, in round numbers:** about **$300 to $900 a share**, most of the weight between **$400 and $600**
(about $550bn to $1.7 trillion for the company), beside a price of **$361**. The range is wide **[L2000-024]**,
**[L1999-027]**, and its width is a finding: nearly all of it is the long-run growth assumption, because at a 5.63% rate the
years after the tenth carry most of the value.

**Is the price so far below it that it needs no pencil?** No. The price is below the middle of the range and above its
bottom. Taking conservative inputs once and the margin once at the end **[M2004-055]** ($20bn, 6%, then 2%), the value is
about $420 and the price is about 14% under it; the speakers' own band of error is "maybe of 10 percent" **[M2019-003]**.
The rows buy "at a reasonable price in relation to the bottom boundary of our estimate" **[L2013-012]**, and the bottom
boundary here ($300) is below the price. The stress test of **[M2007-096]** ("if interest rates go up another hundred basis
points or 200 basis points, we’re still happy") fails: at 7.63% the same conservative inputs give about $265 to $355. The
expectancy, roughly the owner-cash yield of 3.0% to 3.3% plus per-share growth of 6% to 8% (CONVENTION, the plain sum),
is 9% to 11%, above the bond **[M2007-095]**, but "significantly higher" is "fuzzy" **[M2007-096]** and the draft writes
no floor; it does not decide the box. What decides it is that the case had to be carried out with a table, which is the
case **[M2009-005]** and **[M1995-115]** send away: "So if you really need a calculator [...] forget about the whole
exercise. Just go onto something that shouts at you."

**Verdict: OUT** (the third way the draft names: valued, price below the middle of the value, but the case is close)
**[M2009-005]**, **[M1996-084]**, **[L2013-012]**. In the three boxes **[M2006-013]** this is "out", on price and on this day,
not on the business **[M2019-015]**, **[M2003-040]**.

### Q8. Is it better than the alternatives? STOP. NOT REACHED.

Closed at Q7.

## 4. Q9 and Q10. NOT REACHED.

Closed at Q7. For the record only, under the protocol's heading:

**COMPUTATION — NOT A CLEARANCE.** Debt at 2026-06-30: long-term $20,862m, current $2,996m, commercial paper issued
$1,496m in FY2026 (10-Q balance sheet and cash flow statement); cash and cash equivalents $12,359m. FY2025 pre-tax
income $24,194m against interest expense $589m, about 42 times (pre-tax earnings over interest **[L2012-002]**). The
sudden-demand exposure the rows ask about **[L2014-024]** is the settlement guarantee: maximum daily exposure $168.6bn,
average $99.5bn, against $9.5bn of collateral (10-Q Note 9) and $9.2bn of liquidity held for settlement (10-K MD&A). No
weighing is recorded.

## 5. Q11 and Q12

### Q11. Having bought: has the business changed, or only its price? (holdings draft, six questions)

The default is to keep, and the burden is on the reason to sell: "when in doubt, keep holding" **[M2009-040]**. The holder
cannot be forced to sell only if the position is unlevered (section 2, condition recorded, not verified).

**H-Q1. What has moved: the business, or only its price?** (STOP against selling on the price alone; WEIGHING on a silly
price.) The business moved forward: nine-month FY2026 net revenue +15% and diluted EPS +20% (10-Q). The price, $361, is
up from the company's own nine-month buying average of $328.29 (10-Q Note 11). About 30 times trailing GAAP earnings is
not shown to be "a silly price" **[M2007-089]**; the rows give no multiple and this draft writes none. A price too high to
add at is not a price to sell at **[M1998-160]**, **[L1999-021]**. **Answer: price alone moved upward; no sale on it (the
STOP holds); not a silly price. This is the zone where "we would neither be a buyer nor a seller" **[M2005-071]**.**

**H-Q2. Has the castle changed?** (WEIGHING, action at the life-threatening grade.) Earnings rose, allowing for the
industry **[L2007-016]**; the moat test **[M2000-075]** reads as holding: margin ahead of Mastercard, volume growth a little
behind, incentive share rising slowly (Q2 above). New since the 10-K: the injunctive-relief class settlement won
preliminary approval (2026-06-09); about 95% of opt-out volume settled; new UK and European interchange claims
(April to June 2026); the debit suit continues. Graded **major, not life-threatening** **[M2016-081]**; a slow loss of
advantage is not a reason to change the portfolio **[M2016-080]**. **Answer: castle unchanged in kind; threats major;
WEIGHS toward holding.**

**H-Q3. Has the management changed, or changed after being paid?** (WEIGHING on ability; on trust the rows press prompt
action.) Same chief executive since February 2023 and same chair; the CEO holds 274,569 shares outright plus 548,517
obtainable within 60 days (PROXY, beneficial ownership), and the securities class action was dismissed without leave to
amend (10-Q). No lost trust found **[M2016-066]**, **[L2014-003]**; the business would carry a lesser successor
**[M2023-045]**. **Answer: no change; WEIGHS toward holding.**

**H-Q4. Is the money kept still becoming more than a dollar?** (WEIGHING; one STOP on further money into a business that
chews it up.) Almost nothing is kept (Q6); the retention test **[M1998-110]**, **[R1995-009]** has little to bite on, and the
earnings progress per as-converted share (+20% in nine months) outruns the small sums kept **[M2011-072]**. Buybacks at an
average $328 sit near the bottom of the Q7 range, so they were probably not bought above value, though the company never
says what it thinks the value is **[L2011-003]**, **[M2015-074]**. The STOP **[L2023-010]** does not arise: the business
yields cash, it does not consume it. **Answer: WEIGHS toward holding, with the unstated buyback price noted against.**

**H-Q5. Is there a plainly better use for this money?** (WEIGHING.) The draft's test is the least attractive thing held
**[M2007-104]** and a replacement "immensely better" **[M1998-013]**. This session may not open `PORTFOLIO.md`, so it cannot
name the operator's least attractive holding or the alternatives. The one alternative it can see, the 30-year Treasury at
5.63%, is surer but its expected return is below the 9% to 11% rough expectancy of Q7, so it is not plainly better
**[M2007-098]**. **Answer: none shown; WEIGHS toward holding (incomplete: the portfolio comparison is owed by a session
allowed to open the portfolio).**

**H-Q6. Was it a mistake to buy, now recognised?** (WEIGHING on the finding.) No new fact in the filings read contradicts
a purchase case built on a toll on growing card payments: the results since are better, not worse. The litigation and
regulatory facts were known in kind before **[M2012-031]**, **[M2016-065]**. Contrary evidence written down at once
**[M1997-127]**: the rising incentive share and Mastercard's faster volume growth (Q2, items 5 and 6). **Answer: no mistake
found; keep.**

**The add.** An add is a purchase on price (Q7) and on the comparison (Q8) (holdings draft, section IV); Q7 is OUT today,
so the draft would have the holder not add at $361 **[M1999-055]**, **[M1999-077]**. **Holdings result (no named outcome
exists in the draft; section VI, item 2): keep; do not add at this price.**

### Q12. Would we be proud of how the money is made? (optional; STOP for named businesses, otherwise WEIGHING.)

Visa is none of the named businesses (casinos, tobacco, loading schemes) **[M2007-018]**, **[M2005-097]**, **[M2013-015]**.
The newspaper test **[M2008-011]**: an unfriendly reporter has the DOJ complaint and twenty years of merchant suits about
swipe fees to write from. The allegations are about the pricing and contracts of a dominant network, not about selling
"things that are bad for people" **[M2021-059]**; the company also earns from consumer credit cards whose revolving
balances the speakers warn against **[M2001-063]**, but it is not the lender. **Verdict: UNDECIDED**, a filter on how
the money is made; the antitrust record is the item a reporter would lead with.

## 6. The box

**OUT, decided at Q7** (valued; the price is not so far below the bottom of the range that it needs no pencil).
Value about **$300 to $900 a share, most of the weight $400 to $600, against a price of $361** (2026-10-02, aggregator),
at the 5.63% long Treasury. Q1 IN, Q2 IN, Q3 weighs for, Q4 IN on confusion and weighs lightly against, Q5 IN on
integrity and weighs for on ability, Q6 weighs lightly against. Holdings draft: keep; no add at this price.

## 7. Self-audit

- [x] **Every id resolves.** All bracketed ids in this file were checked against `principle_ledger_v5.csv` by script
  by script after writing: 128 distinct ids, zero missing. Quotations of rows were also matched against the row text,
  and straight apostrophes corrected to the ledger's curly ones where they differed.
- [x] **Every filing fact has an accession** (table at the top; each fact names its document).
- [x] **No number without a row or a filing.** Filing numbers carry their document; the projection inputs and the
  two-stage form and the expectancy sum are labelled CONVENTION; the 30-times multiple is price over the Q4 earnings
  per share.
- [x] **Whitelist kept.** Opened: the protocol, both v5 drafts, `principle_ledger_v5.csv`, `tools/run.py` and
  `tools/sources.py` (run, and `sources.py` grepped for its SEC user agent), `Screens/cover_shares.py` (run only), SEC
  EDGAR. Not opened: v4 documents, `principle_ledger.csv`, `Test Runs/`, other `Screens/` files, `PORTFOLIO.md`, other
  test files. The project map and `Framework/OPERATOR-PROTOCOL.md` were loaded by the session itself; the protocol file
  is on the whitelist.
- [x] **Order kept; first failing STOP stopped the run.** Q1 to Q7 in order; Q7 OUT closed the purchase run; Q8 to Q10
  NOT REACHED; Q11 answered because the name is held; Q12 answered as the optional newspaper test.
- [x] No em dashes in my own prose; the dashes inside quotations are the ledger's.

## 8. What in the draft was wrong or unclear

Q7 asks for a range "at the long government rate" and forbids any number not carried by a row, but gives no instruction
on the one input that decides the answer: the growth path and the horizon of "how soon". At a 5.63% rate a large, slowly
growing toll is worth almost anything from $260 to $1,240 a share depending on what is assumed after year ten, so the
draft's three STOP routes overlap: the range is arguably "so wide that no useful conclusion can be reached"
**[L2000-025]** (which would be the first route, cannot be valued, TOO HARD) and also valued-but-close (the third route,
OUT), and the draft does not say which governs when a range is wide only because of the terminal assumption. I used a
labelled CONVENTION two-stage projection, took the conservative case once as **[M2004-055]** directs, and closed on the
third route, citing **[M2009-005]** and **[L2013-012]**. Two smaller gaps: the floor is described as "the speakers' minimum
expectancy" with no way to compute an expectancy, so it could not be applied; and Q4's "STOP on confusion, otherwise
WEIGHING" needs two verdicts in the protocol's words, which I recorded side by side. In the holdings draft, H-Q5 asks
for "the least attractive thing I hold", which a test session barred from `PORTFOLIO.md` cannot answer; I answered it
against the bond only and marked it incomplete.
