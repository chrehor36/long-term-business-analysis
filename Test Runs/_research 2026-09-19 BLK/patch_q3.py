import io, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "2026-09-19 Run - BLK BlackRock.md")
s = io.open(P, encoding="utf-8").read()

OLD = """## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: ____

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC, so the test stays point-in-time honest: ____

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — comp not expensed, fanciful pension assumptions → *"seldom just one cockroach in the kitchen"*
- [ ] unintelligible footnotes
- [ ] trumpeted earnings projections / growth targets
- [ ] serial share issuance
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** *(the fifth flag; 12+ corpus statements)*
- [ ] filed-figure tells: unnaturally smooth reported growth; cash-tax % of pretax falling **[E4-30]**
- For every box ticked, what the filing actually says: ____

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.
- Years used, and the series: ____

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? *(a one-time item quantified separately at every line passes; the
same item buried in an adjusted figure does not)* ____

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction
- [ ] projects/acquisitions materialise to soak up available funds
- [ ] staff studies produced to justify the leader's craving
- [ ] peer behaviour mindlessly imitated

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? ____
- (2) repurchases at a **material discount** to conservatively calculated IV? ____
  *(unquantified because the corpus leaves it unquantified)*
- If (2) fails → **CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**:
  this rests on our own IV range, and management knows the business better than we do.
  **Binds position size, never the discount rate.**
**THE GUARDRAIL — check before writing the verdict.**
- [ ] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [ ] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — *"the moat will go when the surgeon goes"* — not here as a strength.
- [ ] If a great manager is the reason to act: is the franchise **already intact** and the
      damage **excisable**, or is the manager the plan? **[E2-35, E2-36]** ____

- **VERDICT: [ ] IN  [ ] OUT (integrity failure is permanent)  [ ] UNRESEARCHED → ____
  [ ] UNKNOWABLE → ____**
  *IN = no disqualifier found. NOT a finding that the managers are honest — "sincerity and
  empathy can easily be faked" **[E5-17]**. IN never promotes.*
"""

NEW = r"""## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. The file closed at Q2 on the
business. Nothing below can reopen it, and nothing below is used to promote the name
**[E2-37, E2-38, E3-39]**.*

**STEP 1 — THE WEIGHT CASE.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**Case declared, and why: Q3 would be a BINARY GATE.** The 1977 root **[E2-70]** is the
governing one: where *"their only products are promises"*, an undifferentiated product
**magnifies** the manager. That is a literal description of this business as Q2 found it —
BlackRock's product is a promise (to track, to manage risk, to act as fiduciary, to keep
Aladdin running) delivered every day across $15.3 trillion of other people's money, and Q2
established that the product itself is undifferentiated from Vanguard's. A single conduct or
operational failure — in securities lending, in proxy voting, in a fund's tracking, in the
Aladdin platform on which clients run their own operations — is not recoverable by price.
**Leverage is NOT ticked:** borrowings $12,768M against $55,888M of equity is 0.23x, there is
no maturity before March 2027, and the $68,020M of separate-account assets is matched dollar
for dollar by an identical liability. **Control is NOT ticked:** this is a public-market
position with a daily exit.

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."*
- **No personal-misconduct matter is found in the filings.** The Note 16 contingencies
  disclosure is the standard receives-subpoenas-from-time-to-time language plus one named case.
- **The one named matter, dated as the filing dates it:** *"BlackRock is currently defending a
  lawsuit filed by thirteen state Attorneys General in Federal Court in the Eastern District of
  Texas against BlackRock, State Street, and Vanguard, alleging antitrust violations on the
  theory that the three companies conspired to artificially suppress coal supply. Four states
  are also pursuing alleged violations of state consumer protection laws regarding statements on
  BlackRock fund websites. **In 2025, the court largely denied defendants' motion to dismiss.**"*
  (10-K FY2025, `0001193125-26-071966`, Note 16.) **Read under [E5-22]** — penalty size is not
  seriousness in either direction, and the failure that counts is not acting when you learn. This
  is a live, surviving antitrust claim against the three largest index managers jointly, and the
  survival of a motion to dismiss is a fact, not a finding. **It is not a conduct disqualifier on
  the filed record, and it is recorded as a matter to watch, not as a verdict.**
- **[E5-16] is satisfied in the only form the corpus permits [E5-17]: no disqualifier was found.
  That is not a finding that these managers are honest.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E3-50, E2-57, E3-53, E2-52].**
*Accounting and disclosure, not litigation. Each is a prompt to READ, never a verdict
**[E5-36]**, and a fired flag is not a venality finding **[E5-38]**.*

- [ ] **weak accounting — NOT FOUND, and in several places the accounting is better than it
  needed to be.** Stock compensation is expensed in full. Consolidated investment products are
  consolidated line by line and then *separated for the reader* in a published reconciliation.
  Contingent consideration is marked to fair value through income, and the 2025 mark was a
  **$720M charge taken to the income statement**, not buried. Deferred tax liabilities of
  $4,618M are disclosed against the acquired intangibles. No pension assumption issue.
- [ ] **unintelligible footnotes — NO. The opposite.** The filer publishes (a) a consolidated
  balance sheet with the CIP and separate-account columns removed to an "As Adjusted" column,
  (b) a GAAP-to-excluding-CIPs cash-flow reconciliation for two full years, (c) the full
  non-GAAP reconciliation line by line, and (d) in the proxy, the BPIP payout matrix in advance.
  This run's Q4 owner-earnings separation of the consolidated funds is **performed using the
  filer's own arithmetic**, which is the strongest available evidence on [E2-26].
- [x] **trumpeted earnings projections / growth targets — FIRES.** In the 10-K strategy section:
  *"BlackRock's investments in infrastructure, private credit, and alternatives-to-wealth
  underpin its **ambition to raise $400 billion in private markets by 2030**."* In the Q2 2026
  earnings release (8-K EX-99.1, 2026-07-15, `0001193125-26-304013`), the CEO: *"**8% organic
  base fee growth – well in excess of our target**"*, *"a nearly 46% adjusted operating margin,
  double-digit EPS growth, and increasing capital return"*, *"I've never been more optimistic
  about the growth"*. **[E5-30] is the reason this matters more than it looks:** *"once you
  start it, it's all over. You can't quit … And forecasting earnings, I can't imagine anything
  more destructive."* A target the CEO measures himself against in public every ninety days is a
  ratchet, not a fact about 2026. **[E4-35]** sets the base rate the $400bn-by-2030 ambition has
  to face: fewer than 10 of the 200 most profitable companies were wagered to compound EPS at
  15% for twenty years, and *"lofty targets corrode CEO behavior"* is the flag itself.
- [x] **serial share issuance — FIRES on the facts, and the reading changes what it means.**
  **6.9M shares for GIP, 8.5M Subco Units for HPS, and 4.0-5.2M + 2.8-4.4M more contingent — up
  to 25.0M shares and units, 15.4% of the 162.5M outstanding.** But **[E5-15]** describes a
  *dribble-out* pattern — *"one of the surest indicators of a promotion-minded management, weak
  accounting, a stock that is overpriced and — all too often — outright dishonesty"* — and this
  is not that: it is acquisition consideration, disclosed at every line, alongside $1.6bn of
  annual repurchase. **The flag's proper destination is [E5-44], not [E5-15]:** *"The intrinsic
  value of the shares you give in an acquisition **must not be greater than the intrinsic value
  of the business you receive**."* Measured at IV, not at quote. On the closing paper alone,
  $22.0bn of shares and units bought books producing **$2,350M of base fees and $695M of
  performance fees in 2025 — 7.2x combined fee revenue**, before the contingent $8,429M. The GIP
  shares were struck at **~$855 after a two-year registration discount off a $950 quote**, which
  is a real, disclosed, shareholder-favouring haircut. **Judgment recorded: not obviously wrong,
  not obviously right, and not resolvable from the filings. It is not scored as a disqualifier.**
- [x] **adjusted-earnings promotion [E4-29] — FIRES AT FULL STRENGTH on the adjusted-earnings
  limb, and reads CLEAN on the EBITDA limb.** *The CGNX standing rule of 2026-09-07 was
  followed: the 8-K EX-99.1 earnings release and the proxy were both pulled before scoring this
  flag.* **The word "EBITDA" appears zero times in the FY2025 10-K, zero times in the Q2 2026
  earnings release, and zero times in the 2026 proxy.** That deserves saying plainly: BlackRock
  does not do the thing the corpus calls *"a particularly pernicious practice"*. What it does
  instead:
  - **The earnings release headline is the adjusted number:** *"BlackRock Reports Second Quarter
    2026 Diluted EPS of $12.19, **or $13.91 as adjusted**"*. The phrase "as adjusted" appears
    **35 times** in that release.
  - **FY2025 GAAP diluted EPS $35.31; "as adjusted" $48.09 — a gap of $12.78, 36.2%.** In 2024
    the same gap was $1.60, 3.8%. **The gap grew nine-fold in one year.**
  - **GAAP operating margin fell 37.1% → 29.1%. "Operating margin, as adjusted" went 44.5% →
    44.1%.** The add-backs that did it: amortisation and impairment of intangibles **$775M**,
    **acquisition-related compensation costs $738M**, acquisition transaction costs $122M, the
    contingent-consideration mark **$720M**, the Charitable Contribution $109M, the restructuring
    charge $39M, deferred-comp market moves $52M — **$2,555M in 2025 against $536M in 2024.**
  - **The denominator is reduced too**, which raises the margin independently of the numerator:
    revenue for the margin measure is $21,756M rather than $24,216M, after removing $1,355M of
    distribution fees and $1,105M of investment advisory fees.
  - **[E3-53] and [E5-33] govern two of the add-backs directly.** Restructuring charges and
    retention compensation are *real costs*, and *"to tell owners year after year, 'Don't count
    this' … is misleading."* $738M of pay to retain people the company bought is the most
    ordinary cost imaginable. **[E2-57]** is the same point from the other side: the adjusted
    apparatus is *"except for"* institutionalised at eight lines, and *"you must count the runs
    scored against you in all nine innings."*
  - **Why it matters here and not only as a disclosure point:** the 10-K states that the Company
    uses operating margin, as adjusted, *"to determine the long-term and annual compensation of
    the Company's senior-level employees."* **The pay metric is the metric that excludes the cost
    of the acquisitions.** That is **[E4-27]**: *"Never, ever, think about something else when
    you should be thinking about the power of incentives."*
- [ ] **filed-figure tells [E4-30] — DO NOT FIRE.** *Cash taxes as a share of pretax income:*
  **33.3% (2021), 17.0%, 19.5%, 20.5%, 30.2% (2025)** — cash taxes paid $2,298M on $7,619M of
  pretax income in 2025, against a 22.0% book rate. **Rising, not falling**, and cash tax above
  book tax in the latest year. *Smoothness:* GAAP operating income **7,450 → 6,385 → 6,275 →
  7,574 → 7,045** is visibly lumpy; nothing is unnaturally smooth. **The smooth series is the
  adjusted one**, which is the point already made above, not a separate tell.
- [x] **metric-switching [E2-49] — FIRES as a prompt; the reading is genuinely mixed, and the
  positive half is real.**
  - *Three definitional changes inside the window, each disclosed with a reason and with prior
    periods recast:* non-GAAP definitions updated in Q1 2023 to exclude deferred-cash-comp market
    moves; the AUM and base-fee product-line presentation reclassified in Q1 2025 (*"Such line
    items have been reclassified for 2023 and 2024 to conform to this new presentation"*, with
    the reclassified 2024 figures pointed to an 8-K exhibit); and, **in Q3 2025, at the moment of
    the HPS closing**, adjusted EPS redefined to *"assume all outstanding Subco Units issued as
    part of the consideration for the HPS Transaction have been exchanged … on a one-for-one
    basis"*. Announcing a change ahead with reasons is the candour case [E2-49] explicitly
    allows, and all three qualify on that test.
  - **But the yardstick was not discarded — it was kept because it is insulated.** The BPIP
    target for adjusted operating margin was **raised from 41.5% (2023-2025 cycle) to 44.0%
    (2026-2028 cycle)** while GAAP operating margin **fell from 37.1% to 29.1%**. The pay
    bullseye moved up 2.5 points while the filed number moved down 8.
  - **The positive half, and it is strong.** BlackRock publishes the entire BPIP payout matrix in
    advance and then reports the prior cycle's outturn against its own pre-set target:
    *"BlackRock achieved above-target level results in the 2023-2025 performance cycle, with
    three-year average annual Organic Revenue Growth of **$716 million** (above Target Level of
    **$640 million**) and Operating Margin, as adjusted, of **43.4%** (above Target Level of
    **41.5%**). Accordingly, participants received … **116.6%** of the base number of units."*
    **That is [E2-49]'s demand for "pre-set, long-lived and small bullseyes" honoured almost to
    the letter, and it is the [E3-48] artifact done well** — guidance set, published in advance,
    and outturn reported against it. It is recorded as a credit.
- [ ] **dividends funded by issuance [E2-52] — DOES NOT FIRE.** Dividends and Subco distributions
  $3,347M against ex-CIP operating cash of $7,463M; no equity was raised for cash.
- [x] **stock-price targeting [E3-50] — FIRES, and this is the sharpest single finding in the
  file.** The 2026 proxy (`0001308179-26-000262`, filed 2026-04-10) prints the **"2025 NEO
  Pre-Set Performance Scorecard"**. Under *Financial Performance · Priority 1: Drive profitable
  growth*, the scored measures are, in the proxy's own order:
  > *"◦ **Next 12-Month P/E Multiple (including relative premium)** ◦ **Total Shareholder
  > Return** ◦ Diluted EPS, as adjusted ◦ Operating Income, as adjusted"*

  **[E3-50]** describes managers whose premise is *"that their job at all times is to encourage
  **the highest stock price possible** (a premise with which we adamantly disagree)"*, and names
  the next step: *"unadmirable accounting stratagems."* **Writing the forward price/earnings
  multiple — and the relative premium to peers — into the CEO's pre-set scorecard is that premise
  formalised into a pay formula.** It is not the share price as an outcome; it is the
  *multiple the market applies* as a scored objective. The positive doctrine the corpus states
  instead is a price *"in a narrow range centered at intrinsic business value"*, with
  overvaluation as unwelcome as undervaluation. Nothing in this proxy expresses that preference.
- [x] **restructuring charge [E3-53] — FIRES, small.** $39M (2025), nil (2024), $61M (2023),
  $91M (2022). Each disclosed and each added back in the adjusted metric. **This run's owner
  earnings are computed from cash flow, so the charges stay in the mean, as [E5-33] requires.**

**CONVERGING FLAGS ARE A DIFFERENT EVENT [E4-52].** Four of the fired flags point one way:
(a) an adjusted-earnings apparatus that grew its gap to GAAP EPS to $12.78; (b) a pay scorecard
that scores the forward P/E multiple and total shareholder return; (c) buybacks announced as a
**dollar quantity in advance** rather than as a price condition (below); (d) a $400bn-by-2030
target and a quarterly organic-base-fee-growth target the CEO measures himself against in
public. **Read together, as [E4-52] instructs — *"extreme consequences from confluences … it
dominates life"* — they describe a management system optimised for the share price and scored on
a metric that excludes the cost of the acquisitions the system is making.** Two corpus
constraints bind the reading and are applied: **[E5-38]** — a fired flag is not a venality
finding, and people one would trust with one's wallet *"would play games with any number that
came to them"*; and **[E2-30]**'s last clause — *"Institutional dynamics, not venality or
stupidity, set businesses on these courses."* Every one of these practices is the industry
standard. That is the point of [E2-30], not an excuse for it.

**STEP 3 — THE PRIMARY TEST [E2-01].** *"The primary test of managerial economic performance is
the achievement of a high earnings rate on equity capital employed (without undue leverage,
accounting gimmickry, etc.) **and not the achievement of consistent gains in earnings per
share**."* Balance sheet before income statement.

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Total BlackRock, Inc. stockholders' equity, year end ($M) | 37,693 | 37,744 | 39,347 | 47,495 | **55,888** |
| Net income attributable to BlackRock, Inc. ($M) | 5,901 | 5,178 | 5,502 | 6,369 | **5,553** |
| **Return on average equity, GAAP** | **16.2%** | **13.7%** | **14.3%** | **14.7%** | **10.7%** |
| Return on average equity, "as adjusted" net income | — | — | — | 15.2% | 15.0% |
| Goodwill + intangibles, net ($M) | — | 33,643 | 33,782 | 46,692 | **63,251** |
| **Net tangible equity ($M) [E2-43]** | — | **+4,101** | **+5,565** | **+803** | **−7,363** |
| Diluted EPS, GAAP | 38.22 | 33.97 | 36.51 | 42.01 | **35.31** |
| Diluted EPS, as adjusted | — | — | — | 43.61 | **48.09** |

**The series is the test's own opposition, running in both directions at once.** GAAP return on
the equity shareholders actually funded **fell from 14.7% to 10.7%**, and GAAP EPS fell from
$42.01 to $35.31 — while **adjusted EPS rose 10% to $48.09**, the metric used to set senior pay
held at 44.1%, and the CEO was rated **"Far Exceeds Expectations"** with a total incentive award
of **$43.5 million, up 24%**, on total annual compensation of **$45.0 million**. [E2-01] was
written to prefer the first number and distrust the second, and here they disagree by the widest
margin in the window.

**[E2-43] must be applied and it changes the denominator question.** *"Unleveraged net tangible
assets"* is *"the best guide to the economic attractiveness of the operation"*, with the goodwill
wedge reported separately, never hidden in book equity. **BlackRock's net tangible equity is
negative $7,363M**, so a return-on-tangible-equity figure cannot be computed at all. The honest
statement of the two facts: **the operating business earns an extremely high return on the
tangible capital it employs** (it employs almost none — $1,256M of property and equipment), **and
the purchase price of the acquired managers has been added to the equity the shareholder funded**,
which is why the reported rate fell. **[E2-73]** is the third denominator and it says the same
thing from the operator's side: *"what we pay for a business does not affect the amount of
capital its manager has to work with."*

**The half-owner test [E2-26] — PASSES, and it is the strongest thing in this Q3.** *"the
business facts that we would want to know if our positions were reversed."* This filer hands the
reader the separations the reader would otherwise have to construct: the CIP cash-flow
reconciliation, the balance sheet with the CIP and separate-account columns stripped, the
line-by-line non-GAAP bridge, the reclassified prior-year product lines with a pointer to where
they were published, and the pay matrix in advance with its outturn. **The one-time items are
quantified separately at every line, which is exactly the passing case the framework names.**
What the reporting does *not* do is prefer the GAAP number in its own headlines.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] **resists any change in current direction — NO, the opposite.** It changed direction hard,
  and fast, into private markets and data.
- [x] **projects/acquisitions materialise to soak up available funds — YES.** $28.3bn of
  acquisitions in twenty-one months after a decade in which the largest deal was eFront at
  roughly $1.3bn. The funds available were the share price and a $3bn/$2.5bn pair of note issues
  raised *in advance of* the GIP and Preqin closings, which the 10-K states explicitly.
- [x] **staff studies produced to justify the leader's craving — PARTLY, and disclosed.** Both
  contingent-consideration fair values were *"determined by using the income approach **with the
  assistance of a third-party valuation specialist**"*, on Level 3 inputs including *"estimates
  of the timing and amounts of fundraising and fee related earnings forecasts, cost of equity,
  and future stock price performance."* **[E3-58]** warns that solving capital allocation *"by
  either having a staff that does it, or by hiring consultants"* is *"a terrible mistake"*. The
  valuations were outsourced; whether the decisions were cannot be read from the filing.
- [x] **peer behaviour mindlessly imitated — YES, and it is the clearest of the four.** Every
  large traditional manager bought private-markets capability in the same window: Franklin bought
  Lexington, Alcentra and Putnam; T. Rowe bought Oak Hill Advisors; the pattern is visible in the
  peer 10-Ks pulled for the Q2 row. BlackRock is the largest instance of a universal industry
  move. *"Institutional dynamics, not venality or stupidity, set businesses on these courses."*

**Capital allocation — the buyback conditions [E5-08], with [E4-31]'s third:**
- **(1) ample funds for operations and liquidity? YES.** $11,007M of own cash (CIP cash removed),
  $7,463M of ex-CIP operating cash in 2025, no debt maturity before March 2027, and a $5.9bn
  undrawn facility that **[E5-39]** says not to count.
- **(2) repurchases at a material discount to conservatively calculated IV? FAILS on this run's
  own numbers.** 2025: *"the Company repurchased an aggregate of 1.6 million shares and share
  equivalents for approximately $1.6 billion"* — roughly $1,000 a share, and the Item 5 table for
  October-December 2025 shows **103,520 shares and 370,558 Subco Units at an average price of
  $1,073.40**. Q5 below computes an honest owner-earnings yield of **2.7% to 3.0%** at
  $1,069.78 against a **5.34%** sovereign. On those figures the shares are not at a material
  discount to a conservatively calculated value; they are above any conservative value this run
  can defend.
- **And the form of the commitment is itself the [E5-24] problem.** The Q2 2026 release announces
  *"Increasing planned quarterly share repurchases to **$550 million**"* and *"our conviction in
  the growth ahead for BlackRock led us to increase our **planned level of 2026 share repurchases
  to $2 billion**."* **[E5-24]**: *"what is smart at one price is dumb at another."* A
  pre-announced dollar quantity is a commitment to buy at whatever price arrives, which is the
  opposite of a price condition. Contrast **[E5-25]**, where compliance was made real by
  publishing **both conditions as numbers in advance** — the 110%-of-book ceiling and the $20bn
  liquidity floor. BlackRock publishes the quantity and not the price test. **[E2-51]** cuts the
  other way and is recorded for balance: a manager who *refuses* repurchases when they are
  clearly in owners' interests *"reveals more than he knows of his motivations"* — BlackRock is
  not that manager.
- **(3) [E4-31]'s third condition — shareholders supplied all the information needed to estimate
  value? YES.** The disclosure is good enough that this run could build the whole file from it.
- → **CAPITAL ALLOCATION FLAG, LIVE**, stated with the humility clause **[E4-13]**: this rests on
  *our* IV range, *"it is natural for CEOs to be optimistic about their own businesses. They also
  know a whole lot more about them than I do,"* and **[E5-08]**'s own note that *"many CEOs never
  stop believing their stock is cheap"* — infractions here are innocent. **The flag binds
  position size, never the discount rate. No position is being taken: the file closed at Q2.**

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** A strong manager cannot
  repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**. The Q2 verdict was written before
  this section and is untouched by it.
- [x] **This business does not require a great manager**, and that was recorded at Q2 as the
  absence of a key-person defect **[E4-23]**, not here as a strength.
- [x] **No great-manager case is being made.** There is no excisable cancer and no Pygmalion
  **[E2-35, E2-36]**: the franchise question failed on price, which no manager can excise.
- **And [E5-32]'s cap is carried:** audited does not mean true. Salomon's books carried an
  invented daily number signed for twelve years. Every filing-based test above sits under
  **[E5-17]**'s ceiling — *"People are not that easy to read. Sincerity and empathy can easily be
  faked."*

- **VERDICT: [x] IN — no disqualifier found. RECORDED, NOT GOVERNING** (the file closed at Q2),
  **with a LIVE CAPITAL ALLOCATION FLAG and four converging disclosure flags [E4-52].**
  *IN = the absence of found disqualifiers, **not** a finding that the managers are honest
  **[E5-17]**. IN never promotes. The sharpest adverse finding is [E3-50]: the forward P/E
  multiple, including its relative premium, is a scored measure in the CEO's pre-set pay
  scorecard. The sharpest favourable finding is [E2-49] and [E3-48] honoured: the pay bullseyes
  are published in advance and the prior cycle's outturn is reported against them.*
"""

assert OLD in s, "Q3 anchor not found"
s = s.replace(OLD, NEW, 1)
io.open(P, "w", encoding="utf-8").write(s)
print("Q3 written, chars:", len(NEW))
