# -*- coding: utf-8 -*-
import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(BASE, "Test Runs", "2026-09-21 Run - MGM MGM Resorts International.md")
t = io.open(P, encoding="utf-8").read()

# ---- 1. correction inserted INSIDE Q2, before the class-and-direction block
corr = u'''### CORRECTION TO MY OWN ROW, MADE BEFORE THE VERDICT WAS FILED

**Found while building Q4, after row A above was written: MGM’s reported operating income in
2021, 2022, 2023 and 2025 each contains a large item that is not operating.** Row A is the same
metric for every filer and is left standing as computed, because changing one company’s
definition and not the others would be worse. But the 2021 and 2022 figures in particular must
not be read as trading margins, and the claim that the margin fell in four consecutive years —
which I would have written from row A alone — **is wrong.** **[E3-41]**: *"you must not fool
yourself, and you’re the easiest person to fool."*

From each year’s own filed reconciliation and Note 16:

| year | operating income as filed | what is in it that is not operating | operating margin as filed | **margin with those items removed** |
|---|---|---|---|---|
| 2021 | $2,278.7M | $1,562.3M gain on consolidation of CityCenter; $67.7M net property gain | 23.5% | **6.7%** |
| 2022 | $1,439.4M | $2,277.7M gain on REIT transactions; $1,037.0M property gain (The Mirage); less a **one-off $2.5bn** amortisation of the old Macau gaming concession on the change in its useful life | 11.0% | **4.8%** |
| 2023 | $1,891.5M | $398.8M gain on the sale of Gold Strike Tunica operations, net of $28.3M other property losses | 11.7% | **9.4%** |
| 2024 | $1,490.5M | $81.3M of property transaction losses | 8.6% | **9.1%** |
| 2025 | $1,001.8M | $278.9M goodwill impairment; $126.0M of property transaction losses | 5.7% | **8.0%** |

**The corrected series is 6.7%, 4.8%, 9.4%, 9.1%, 8.0% — a post-pandemic recovery to 2023 and
two declines since, inside a band of 4.8% to 9.4%.** It is not a four-year slide. **The Q2
verdict does not turn on the shape of that line and does not change**: on the corrected figures
MGM is still last among the profitable peers in every year of the window, against 15.7% to 21.6%
at LVS, BYD, CZR and WYNN in 2025, and the two most recent years still fall. **The peer rows were
NOT adjusted the same way**, so the 2021 and 2022 cross-section in row A is unreliable in both
directions; the 2023-2025 cross-section is the one that carries weight.

'''

anchor = u"### CLASS AND DIRECTION"
t = t.replace(anchor, corr + anchor, 1)

# ---- 2. Q3
q3 = u'''## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
### RECORDED, NOT GOVERNING — the file closed at Q2. No verdict box below is ticked.
*Q3 is written out in full because the framework’s guardrail runs both ways: Q3 can stop a run and
can never start one, so a Q3 finding cannot rescue a Q2 OUT, and a clean Q3 cannot either. It is
recorded because the register and any future reader are owed what the filings actually say.*

**STEP 1 — THE WEIGHT CASE, DECLARED [E3-38, E1-16, E3-29].**
- [x] **Daily execution.** Yield management, marketing spend, credit extension to players, and
  hold are decided every day across 30 properties. **[E3-43]**’s original form governs: *"a
  business, unlike a franchise, can be killed by poor management"* — and Q2 found no franchise
  at the registrant level.
- [ ] Control. This is a public-market read, not a purchase of the whole thing.
- [x] **Leverage, and it is the lease.** At 2025-12-31 total liabilities were $38,097.5M against
  **$2,429.9M** of equity attributable to MGM’s own shareholders — 15.7 to 1 — of which
  $25,068.7M is the operating lease liability and $6,230.1M is debt. **[E3-52]** says read the
  terms, not just the quantity, and the terms run the wrong way from Berkshire’s float: these are
  covenanted (*"requires the Company to comply with certain financial covenants, which, if not
  met, would require the Company to maintain either cash security or one or more letters of
  credit in favor of the landlord in amounts ranging from six months to two years of rent"*,
  Note 11), dated, escalating, parent-guaranteed, and — per VICI’s own 10-K — cross-defaulted
  across the whole portfolio.

**Two of three ticked → Q3 would be a BINARY GATE here, and no price would compensate
[E1-16, E3-29, E5-35].**

**HONESTY — the binary [E5-16], each matter dated to when it became public.** No finding of
personal misconduct by management is present in the filings read. The one conduct-adjacent matter
is the **September 2023 cybersecurity incident** (10-K Note 12): consumer class actions in the
U.S. and Canada, settled for **$45 million** covering the 2023 and a 2019 incident, *"paid by
insurance carriers into a settlement fund in February 2025"*, judgment entered June 2025;
**investigations by state regulators continue** and the Company *"cannot predict the timing or
outcome."* **[E5-22] governs the reading: penalty size is not seriousness in either direction** —
the Wells Fargo error was reading a $185M fine as small, and the failure that counts is *"they
didn’t act when they learned."* The filings disclose the incident, the settlement, the insurer
funding and the open regulatory matters; nothing in them shows a failure to act on knowledge.
**No disqualifier found. That is the absence of found disqualifiers, not a finding that the
managers are honest [E5-17].**

**STEP 2 — THE FLAGS. Each is a prompt to read, never a verdict [E5-36, E5-38].**

- [x] **EBITDA / adjusted-earnings promotion — [E4-29], AND IT FIRES AT FULL STRENGTH. This is the
  sharpest thing in the file after the guarantor table.** *"Trumpeting EBITDA … is a particularly
  pernicious practice. Doing so implies that depreciation is not truly an expense, given that it
  is a ‘non-cash’ charge. That’s nonsense."* MGM does not merely trumpet EBITDA. **It trumpets
  EBITDAR — the same measure with the RENT taken out as well.** From Note 17 and repeated verbatim
  in the Q2 2026 earnings release: *"Segment Adjusted EBITDAR is a measure defined as earnings
  before interest and other non-operating income (expense), income taxes, depreciation and
  amortization, preopening and start-up expenses, property transactions, net, **triple net lease
  rent expense**, income (loss) from unconsolidated affiliates, goodwill impairment, and also
  excludes corporate expense and stock compensation expense."*
  **Quantified for FY2025: Segment Adjusted EBITDAR of $5,134.0M is struck before $1,017.8M of
  depreciation and amortization, $2,258.4M of triple net lease rent, $519.9M of corporate expense
  and $90.5M of stock compensation. Operating income was $1,001.8M.** The headline profit measure
  is 5.1 times the operating income, and the largest single thing it deletes is a **cash** cost
  that was paid in cash ($1,867.1M in FY2025, Note 11) and is contractually owed for 29 more
  years. **[E5-41]**’s inversion is doubly true here: depreciation is *"reverse float … you spend
  the money first and record the expense later"*, and rent is neither float nor reverse float —
  it is simply a bill, and EBITDAR deletes it.
  **The disclosure is technically correct and that is part of the finding**: because ASC 280 lets
  a registrant call its chief-operating-decision-maker measure the "reportable segment GAAP
  measure", MGM writes *"Segment Adjusted EBITDAR is our reportable segment GAAP measure"* — four
  times in the release. A reader who does not know Topic 280 reads the letters G-A-A-P next to a
  number struck before rent.

- [x] **Metric-switching — [E2-49], and it fires with its mitigations named.** *"Yardsticks seldom
  are discarded while yielding favorable readings. But when results deteriorate, most managers
  favor disposition of the yardstick rather than disposition of the manager."* From the DEF 14A
  filed 2026-03-27 (accession 0001193125-26-129074), **two yardsticks changed in the single year
  2025**: the Committee *"determined to remove Absolute TSR PSUs as a component of the long-term
  incentive program"*, and *"determined to modify the peer group for the Relative TSR PSUs … from
  the S&P 500 to the S&P 1500 Hotels, Restaurants and Leisure Index."* Removing absolute TSR
  removes the test that requires the share price to rise at all; moving from the S&P 500 to a
  sector index compares MGM with a set that moves with it. The stock closed 2021 at $44.88 and
  2025 at $36.49, so the changes did not follow favourable readings. **The mitigations are real
  and are stated rather than buried:** the change was announced in advance with the Committee’s
  reasons and its consultant named (F.W. Cook), and a guard survives — *"Funding capped at 100% of
  target if absolute TSR is negative, unless relative TSR is above the 75th percentile."* On
  [E2-49]’s own operational form (a switch announced ahead with reasons is the candor case), this
  sits between the two poles. It is recorded as fired, with the counter-evidence attached.

- [x] **What the pay actually vests on — [E4-27], read from the proxy.** *"Never, ever, think about
  something else when you should be thinking about the power of incentives."* From the DEF 14A:
  **75% of the annual bonus for the CEO, the CFO and the Chief Legal Officer turns on
  "Compensation Adjusted EBITDAR"** (50% for the digital president). That measure is EBITDAR —
  before rent — grossed up further by adding MGM China’s, BetMGM’s and Boa Lion’s *target*
  EBITDAR or EBITDA multiplied by MGM’s ownership percentage, and reduced by thirteen enumerated
  classes of exclusion including goodwill impairment, deal costs, and consequences of changes in
  tax law or accounting principles. The proxy states the target was *"consistent with the EBITDA
  approved by the Board in the budgeting process for 2025, **as further increased by the
  Company’s rental payments**."* **The rent is added back to the bonus target by name.** The 2025
  outturn was $4,304,248,000 and *"each NEO receiv[ed] approximately 100% of their target award
  for this component"* — in a year when consolidated operating income fell 33%, the guarantor
  group’s operating income fell 89%, and domestic operations lost $237.1M before tax. **The long
  term incentive is 50% relative-TSR PSUs and 50% time-vested RSUs, so no part of the pay package
  is measured after rent or after depreciation.**

- [x] **The cash-tax tell — [E4-30]. RECORDED WHETHER OR NOT IT FIRES, as the brief requires. It
  fires on the ratio, and the filing explains it, and the explanation is worse news than the
  flag.** Cash taxes paid as a share of reported pre-tax income: **23.4% (2023), 23.9% (2024),
  then MINUS 12.3% in 2025** (a net $34.6M refunded against $280.8M of pre-tax income). [E4-30]
  reads a falling cash-tax share as a fraud tell. Here Note 10 gives the mechanism outright and it
  is not fraud: **domestic operations produced a pre-tax LOSS of $(237,067) thousand in FY2025**,
  against $256,890 thousand in 2024 and $1,214,888 thousand in 2023, and the benefit is driven by
  a **$283.7M release of the federal deferred valuation allowance**. The tell led to the number
  that matters most in this file, which is what a prompt-to-read is for.

- [ ] **Weak accounting — DOES NOT FIRE, and the disclosure is better than most.** Stock
  compensation is expensed and disclosed ($90.5M in FY2025). The lease note gives cash rent,
  accounting rent, the maturity ladder, the escalators and the discount rate. Note 12 quantifies
  the Macau concession premiums, the investment commitment, the bank guarantees, the Bellagio
  shortfall guarantee and the Osaka funding. The Rule 13-01 guarantor table is given in full. **A
  reader who wants to know where the earnings are can find out from this filing**, which is the
  [E2-26] half-owner test and it passes.

- [ ] **Unintelligible footnotes — DOES NOT FIRE.**

- [ ] **Trumpeted earnings projections — DOES NOT FIRE [E4-22, E3-48, E5-30].** No numeric
  guidance appears in the Q2 2026 earnings release; the forward-looking language is qualitative.
  There is therefore no guidance record to set against outturn under **[E3-48]**, and the
  irreversible-ratchet warning of **[E5-30]** has not been triggered. **Recorded as a genuine
  positive.**

- [ ] **Serial share issuance — DOES NOT FIRE [E5-15]. The opposite happened**, and it is read
  under capital allocation below.

- [ ] **Dividends funded by issuance — DOES NOT FIRE [E2-52].** The dividend is suspended and the
  10-K says so in its own risk list: *"the fact that we suspended our payment of ongoing regular
  dividends to our stockholders, and may not elect to resume paying dividends in the foreseeable
  future or at all."*

- [x] **The except-for flag — [E2-57], in numeric form.** *"‘except for’ should be excised from
  the lexicon … you must count the runs scored against you in all nine innings."* The Q2 2026
  release reports GAAP diluted EPS of $1.11 against $0.18, a six-fold increase — and **Adjusted
  EPS of $0.59 against $0.79, a 25% DECREASE.** The gap is a $(1.13) per share property
  transactions gain (the sale of the MGM Northfield Park operations) partly offset by a $0.37
  goodwill impairment. Both directions are adjusted away, which is even-handed; but four separate
  non-GAAP measures now carry the narrative — Consolidated Adjusted EBITDA, Segment Adjusted
  EBITDAR, Same-Store Segment Adjusted EBITDAR and Adjusted EPS — and the reconciliations,
  though complete, are the ninth-inning problem [E2-57] names.

- [x] **The restructuring/impairment habit — [E3-53, E5-33].** Goodwill impairments of **$278.9M
  in FY2025** and **$111.0M in the second quarter of 2026** are excluded from Consolidated
  Adjusted EBITDA, from Segment Adjusted EBITDAR and from Compensation Adjusted EBITDAR. [E5-33]:
  *"to tell owners year after year, ‘Don’t count this’ … is misleading."* These are non-cash and so
  do not touch the owner-earnings construction at Q4; what they are is the delayed recognition of
  prices paid for businesses — the Regional Operations goodwill written down $256.1M in 2025 —
  and they belong in the reader’s judgment of the acquisitions, not out of it.

**FLAGS THAT CONVERGE ARE A DIFFERENT EVENT [E4-52].** The lollapalooza test asks whether several
flags point one way as a reinforcing system. Here three do, and they point the same way:
**the reported segment measure removes rent; the CEO’s bonus target removes rent and is then
increased BY the rent; and the equity awards are measured on share price alone.** Nothing in the
pay structure or the reported profit measure is computed after the $2,258.4M that the landlords
take. That is one system, not three prompts. **It is not a venality finding [E5-38]** — [E2-30]
governs: *"Institutional dynamics, not venality or stupidity, set businesses on these courses"* —
and the whole of the gaming industry reports EBITDAR. That it is an industry convention is the
[E2-30] point (4), peer behaviour mindlessly imitated, not a defence.

**STEP 3 — THE PRIMARY TEST [E2-01].** *"the achievement of a high earnings rate on equity capital
employed (without undue leverage, accounting gimmickry, etc.) and not the achievement of
consistent gains in earnings per share."* **The test cannot be run on book equity here and the
reason is [E2-47]’s own carve-out** — unusual debt-equity ratios and mis-stated asset values.
Equity attributable to MGM has been driven to $2,429.9M by $9,406.8M of buybacks over five years,
so a return on it is an artefact of the retirement, not a measure of the business. **[E2-43]’s
denominator is the one to use for an acquisitive, leveraged filer: unleveraged net tangible
assets, with the goodwill wedge reported separately.** At 2025-12-31 that is property and
equipment net $6,305.6M plus operating lease right-of-use assets $23,002.7M, against goodwill of
$4,902.0M and other intangibles of $1,356.7M reported separately. Clean operating income of
$1,406.7M on $29,308.3M of tangible operating assets is **4.8%**; the pre-rent version, the one
row B of the competitor table uses, is **11.2%**. Against LVS at 24.2% and BYD at 25.8% on the
identical construction.

**And the EPS series [E2-01] is defined against says the opposite of the business series, which is
exactly the situation the rule was written for.** Diluted EPS: $3.19 (2023), $2.40 (2024), $0.76
(2025) — falling. But per-share book, per-share revenue and per-share everything else were held up
by retiring 43% of the shares. The clean way to see it: **net income attributable to MGM fell from
$1,142.2M to $205.9M over two years while the share count fell 21%.** [E2-01] asks for the rate on
capital, and the rate on capital fell.

**THE HALF-OWNER TEST [E2-26] — PASSES, and it is the strongest thing on this page.** *"tell you
the business facts that we would want to know if our positions were reversed."* Three disclosures
carry it: the **Rule 13-01 guarantor summarized financial information**, which lets a reader see
that the note-guaranteeing domestic group earned $78.5M of operating income on $10,580.2M of
revenue; the **domestic/foreign split of pre-tax income** in Note 10, which shows the domestic
loss; and **Note 11’s separation of cash rent from accounting rent**. None of those three is in the
press release, and all three are in the 10-K. **The filing tells you what you would want to know.
The release does not, and the pay plan is computed on the release’s measure.**

**THE INSTITUTIONAL IMPERATIVE — SCORE ALL FOUR [E2-30].**
- [ ] **Resists any change in current direction** — no. The opposite: the company has re-made
  itself, selling the real estate of essentially every domestic property in six years.
- [x] **Projects or acquisitions materialise to soak up available funds** — yes, and it is
  measurable. $3,914.7M of acquisitions net of cash acquired in 2021-2024 (CityCenter’s remaining
  half, The Cosmopolitan operations, LeoVegas, Push Gaming), plus a **remaining JPY356.9 billion,
  about $2.3 billion, to fund MGM Osaka through 2028** for a resort opening in 2030, newly part
  financed by a JPY54.2 billion senior **secured** yen term loan taken in October and November
  2025 — in the year the domestic business lost money before tax.
- [ ] Staff studies produced to justify the leader’s craving — not visible from filings.
- [x] **Peer behaviour mindlessly imitated** — the asset-light sale-leaseback model and the EBITDAR
  reporting convention are industry-wide (Caesars with VICI, PENN with GLPI). [E2-30]’s fourth
  behaviour is the one that describes this best, and its last clause governs the reading: these are
  institutional dynamics, **not venality or stupidity**.

**CAPITAL ALLOCATION — THE BUYBACK CONDITIONS [E5-08, E4-31, E5-24, E5-31].**
- **(1) Ample funds for operational and liquidity needs? — QUESTIONABLE, and it is stated as a
  question.** In the five years 2021-2025 MGM spent **$9,406.8M** retiring stock while owing
  $1.8bn of cash rent a year, carrying $6.3bn of debt, committing $2.3bn more to Osaka, and
  guaranteeing $3.01bn of its Bellagio landlord’s debt maturing in 2029. **[E5-25]** shows what
  real compliance looks like — Berkshire published both conditions as numbers in advance, with a
  liquidity floor, because *"financial strength that is unquestionable takes precedence over all
  else."* MGM publishes no liquidity floor.
- **(2) Repurchases at a material discount to conservatively calculated intrinsic value? — NOT
  DEMONSTRATED, and the market has now supplied an unusually direct test.** $7,653.3M was spent in
  2022-2025 retiring 195.5M shares, an average of roughly **$39.15** a share. The stock closed at
  **$36.49** on 2025-12-31 and trades at **$38.59** today. Four years and $7.7 billion later, the
  price is where the buying was done. That is not proof the purchases were above value — price is
  not value — but it is the absence of any evidence that they were below it, which is what
  condition (2) requires the buyer to have had. **Stated with the humility clause [E4-13]:** this
  rests on our range, not theirs, *"it is natural for CEOs to be optimistic about their own
  businesses. They also know a whole lot more about them than I do."*
- **(3) The third condition, from the earliest full statement [E4-31] — MET.** *"Shareholders
  should have been supplied all the information they need for estimating that value."* The
  guarantor table, the lease note and the domestic/foreign tax split are all filed.
- **THE SCORED TEST [E3-54] — AND IT FAILS.** At least $1 of market value per $1 retained, five
  years rolling. Market capitalisation 2020-12-31: 494.3M shares × $31.51 = **$15,575M**.
  2025-12-31: 258.3M × $36.49 = **$9,426M**. Cash returned to shareholders over 2021-2025:
  **$9,406.8M** of repurchases (the dividend is suspended and was immaterial before that). So
  ending value plus cash returned is $18,833M against $15,575M five years earlier, a gain of
  $3,258M, against **$4,822.2M** of net income attributable to MGM retained over the same five
  years. **$0.68 of market value per $1 retained.** Prices are from an aggregator and flagged as
  such; the test is [E3-54]’s own, and it is carried with the published 2009 self-correction
  Buffett attached to it.

**THE CONTROL CONTEST — a Q3 fact, filed, and the screen’s deal check did not see it.** On
**2026-06-01**, People Incorporated (f/k/a IAC) filed a Schedule 13D/A on MGM attaching a letter
from **Barry Diller**, who sits on MGM’s own board, proposing *"to acquire all of the outstanding
shares of common stock of MGM not already owned by IAC, for 100% cash consideration of **$48.30
per share**."* The letter says the price *"represents a premium of 24.1% to the volume-weighted
average price … for the 30 trading days ending on May 29, 2026 … and a 10.6% premium to the most
recent closing price"* (MGM closed at $43.67 on 2026-05-29; $43.67 × 1.106 = $48.30, which ties).
On **2026-04-03**, three months earlier, MGM had signed a Voting Agreement with IAC and Mr Diller
(8-K filed 2026-04-07, accession 0000789570-26-000029) under which IAC and Mr Diller vote any
securities above **25.73%** of total voting power in proportion to the other shareholders, in
exchange for the right to designate two directors.
**Read at Q3 under [E2-68]:** the conduct that matters is conduct across an information asymmetry,
and the discloser here is the bidder, not the company. MGM has filed no board response, no 14D-9
and no merger agreement; the only company acknowledgement is one clause in the forward-looking
paragraph of the Q2 2026 release and one bullet in the 10-Q risk list. An EDGAR full-text search
of MGM’s filings for "People Incorporated" returns **exactly three documents, the latest dated
2026-07-29**, so the proposal stands unresolved as of this run. **What it does to the run: it makes
the $38.59 quote a number inside an unresolved control contest rather than a clean
owner-earnings price.** The stock closed at **$47.81 on 2026-06-30** — within 1% of the offer —
and at **$37.81 on 2026-09-18**. Whatever moved it, the quote today is 20.1% below a live cash
proposal from the holder of a quarter of the votes, and that is not a fact a valuation can ignore.
*This is the ROKU finding in a new form and it is written up as a tooling defect in the fold.*

**THE GUARDRAIL — checked before anything above is used.**
- [x] Confirmed: nothing in this Q3 is being used to promote the name. It could not be — the file
  closed at Q2 — and **[E2-37, E2-38, E3-39]** would forbid it anyway. *"a good managerial record
  … is far more a function of what business boat you get into than it is of how effectively you
  row."*
- [x] The business does not require a superstar; no key-person moat defect was recorded at Q2.
- [x] Is the franchise intact with a localised excisable cancer **[E2-35, E2-36]**? **No.** The
  thing Q2 found is not a local lesion a skilled surgeon removes. It is the rent, and the rent is
  a signed 25-to-30-year contract with escalators, parent guarantees and cross-defaults. That is
  the Pygmalion case, not the GEICO case.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

'''

# ---- 3. Q4
q4 = u'''## Q4 — WILL IT SURVIVE?
### RECORDED, NOT GOVERNING — the file closed at Q2. No verdict box below is ticked.

### THE PERIMETER — settled from the filings, in the framework’s own words

**The brief asked whether the consolidation perimeter is measurable, and it is. It is MEASURABLE,
and the instrument is the Rule 13-01 guarantor summarized financial information the registrant is
already required to file.** This is the BN-class answer, not the HHH/RGTI-class one, and it is not
"blocked".

What is consolidated that is not wholly MGM’s: **approximately 56% of MGM China**, separately
listed in Hong Kong, and **LeoVegas**. What is not consolidated at all: **BetMGM (50%)**, **MGM
Osaka (50% interest, an approximately 43.5% equity share after minority funding)** and the
**Bellagio REIT Venture (5%)** — all three VIEs or joint-control ventures per Note 2, entering the
income statement only through *"Income (loss) from unconsolidated affiliates"*.

**Three filed measures of how much of the consolidated numbers are not MGM’s:**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Net income attributable to **noncontrolling interests** | $172.7M | $318.1M | **$315.0M** |
| Net income attributable to **MGM Resorts International** | $1,142.2M | $746.6M | **$205.9M** |
| Cash actually **distributed to noncontrolling interest owners** | $177.1M | $188.6M | **$169.2M** |

**In FY2025 the minority shareholders of a Hong Kong listed subsidiary had a larger claim on the
year’s profit than MGM’s own shareholders did — $315.0M against $205.9M.** The consolidated
operating cash flow of $2,529.4M is therefore not an MGM shareholder number, and two disclosed
adjustments bracket the leak: **$169.2M** (the cash that actually left, a floor, because
undistributed Macau cash sits behind another listed company’s board) and **$315.0M** (the economic
claim on the year’s earnings).

**And the guarantor table says where the earnings are, which is the finding of this run.** From
the 10-K MD&A, for the registrant combined with its wholly owned material domestic guarantor
subsidiaries — a group that **excludes MGM China, LeoVegas, BetMGM, MGM Grand Detroit, MGM
National Harbor and MGM Springfield**, and **includes all nine Las Vegas Strip resorts**:

| | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Net revenues | $10,783.2M | $10,825.1M | **$10,580.2M** | $5,430.2M |
| **Operating income** | **$1,324.6M** | **$733.7M** | **$78.5M** | $665.1M |
| Net income attributable to MGM Resorts International | — | — | $246.4M | $364.9M |

**The domestic group that guarantees the notes earned $78.5 million of operating income on $10.6
billion of revenue in FY2025 — a 0.74% margin — having earned $1,324.6 million two years
earlier on 1.9% more revenue.** The FY2025 and H1 2026 figures carry one-off items I cannot
allocate to the group precisely, so the bound is stated both ways: **even if every consolidated
special is assigned to the guarantor group** (the $278.9M goodwill impairment and $126.0M of
property transaction losses in 2025; the $370.5M net gain in 2023; the $81.3M loss in 2024), the
series reads approximately **$954M → $815M → $483M**, a 49% fall in two years on revenue that
fell. H1 2026’s $665.1M contains a gain of about $272.5M on the Northfield Park sale and a
$111.0M impairment; net of both it annualises near the FY2025 adjusted level, not the FY2023 one.

**Note 10 says the same thing in one line, and it is the plainest sentence in the filing.**
Income before income taxes, by origin:

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Domestic operations** | $1,214.9M | $256.9M | **$(237.1)M** |
| Foreign operations | $257.9M | $860.2M | **$517.8M** |

**In FY2025 the entire pre-tax income of MGM Resorts International came from abroad, and roughly
44% of the Macau part of it belongs to somebody else.** The domestic business — the Las Vegas
Strip and the regional casinos, which is what a buyer of this share thinks they are buying — lost
$237.1M before tax.

**The stock-consideration limit does not bind here (resume state section 5, first bullet), and it
is checked rather than assumed.** Every acquisition in the window was paid in cash: $1,789.6M
(2021, the remaining half of CityCenter), $1,889.1M (2022, The Cosmopolitan operations and
LeoVegas), $122.1M (2023, Push Gaming), $113.9M (2024) — **$3,914.7M, which reproduces the
screen’s $3,915M acquisition note to the dollar and confirms it is the 2021-2024 investing-cash
line, 40.3% of today’s $9,709M market capitalisation.** The screen’s warning that *"the numerator
and the denominator may be different companies"* is correct and is worse than it looks, because
the perimeter moved in **both** directions: in came CityCenter (2021), The Cosmopolitan and
LeoVegas (2022) and Push Gaming (2023); out went **The Mirage** operations (December 2022,
$1,054.3M proceeds, $90M of annual rent removed from the VICI lease), **Gold Strike Tunica**
(February 2023, $460.4M, $40M of rent removed) and **MGM Northfield Park** (agreed October 2025 at
$546M, closed in the second quarter of 2026, $53M of rent removed). **The FY2021 owner-earnings
figure and the FY2025 one are not measurements of the same company.**

### SBC RESOLVES AND IS COMPLETE — checked before any band was used

**The BE failure mode (a silent zero) and the Boeing failure mode (SBC under a tag no SBC element
contains) were both tested for.** The undimensioned `ShareBasedCompensation` cash-flow add-back
resolves for **every one of the 18 filed years, 2008 through 2025**, with no gaps:
$36.3M, $36.6M, $35.0M, $39.7M, $39.6M, $32.3M, $37.3M, $42.9M, $55.5M, $62.5M, $70.2M, $88.8M,
$107.0M, $65.2M, $71.3M, $73.6M, $80.2M, $90.5M. Cross-checked against the filed FY2025 cash-flow
statement: *"Stock-based compensation | 90,471"*. **SBC is COMPLETE. No year is silently
subtracting zero.** SBC is 3.6% of FY2025 operating cash flow, well under the 50% threshold at
which the resume state says to read the grant table by hand, so **[E3-70]**’s market-value
measure is noted as the stricter standard and the reported charge is used as its floor.

### THE SPREAD, REBUILT OVER EVERY WINDOW AND EVERY (c) END **[E4-25, E4-38]**

*The screen’s `spread_caveat` said the published band was a four-construction width that "CANNOT
see variation older than the 5-year window; rebuild it [E4-25]". Rebuilt below over eleven windows
and three (c) ends, 2008 to 2025.*

**Why there are THREE (c) ends here and not two — this is the `da_note` resolved.** The screen
flagged *"D&A steps 4.3x at 2023-12-31 — READ Note 1 and the cash-flow statement"*. Read: the step
is a step **DOWN**, from $3,482.1M in FY2022 to $814.1M in FY2023, and the FY2022 10-K states the
cause in its own MD&A — *"Depreciation and amortization expense increased $2.3 billion compared to
the prior year period, due primarily to an increase of **$2.5 billion in amortization expense of
the MGM Grand Paradise gaming concession as a result of the change in its useful life**"* — with
Note 7 of that filing confirming *"Amortization expense related to intangible assets was $2.7
billion, $197 million and $194 million for 2022, 2021, and 2020, respectively."* **That is the
write-off of a purchased Macau sub-concession on the day a new concession replaced it. It is not
depreciation of anything MGM must renew.** Using **[E3-44]**’s D&A default for (c) in 2022 would
charge $2.5bn of licence runoff as required capital spending. **This is the class of filer the
resume state warns about, where the corpus’s own default runs the wrong way, and only a reader
sees it.** So a third end is built: **(c) = depreciation only**, D&A less intangible amortisation.

**OWNER EARNINGS BY YEAR, $M** — operating cash flow, less SBC, less (c). Eighteen filed years.

| year | OCF | SBC | (c)=D&A | (c)=depr only | (c)=capex | **OE(D&A)** | **OE(depr)** | **OE(capex)** |
|---|---|---|---|---|---|---|---|---|
| 2008 | 753.0 | 36.3 | 778.2 | — | 781.8 | **-61.5** | — | **-65.0** |
| 2009 | 587.9 | 36.6 | 689.3 | — | 136.8 | **-137.9** | — | **414.5** |
| 2010 | 504.0 | 35.0 | 633.4 | 632.4 | 207.5 | **-164.4** | **-163.4** | **261.5** |
| 2011 | 675.1 | 39.7 | 817.1 | 636.1 | 301.2 | **-181.7** | **-0.7** | **334.2** |
| 2012 | 909.4 | 39.6 | 927.7 | 606.7 | 422.8 | **-57.9** | **263.1** | **447.0** |
| 2013 | 1310.4 | 32.3 | 849.2 | 606.2 | 562.1 | **428.9** | **671.9** | **716.0** |
| 2014 | 1130.7 | 37.3 | 815.8 | 583.8 | 872.0 | **277.6** | **509.6** | **221.4** |
| 2015 | 1005.1 | 42.9 | 819.9 | 620.9 | 1466.8 | **142.3** | **341.3** | **-504.6** |
| 2016 | 1534.0 | 55.5 | 849.5 | 669.5 | 2262.5 | **629.0** | **809.0** | **-784.0** |
| 2017 | 2206.4 | 62.5 | 993.5 | 820.5 | 1864.1 | **1150.4** | **1323.4** | **279.8** |
| 2018 | 1722.5 | 70.2 | 1178.0 | 1002.0 | 1486.8 | **474.3** | **650.3** | **165.5** |
| 2019 | 1810.4 | 88.8 | 1304.6 | 1112.6 | 739.0 | **416.9** | **608.9** | **982.6** |
| 2020 | -1493.0 | 107.0 | 1210.6 | 1016.6 | 270.6 | **-2810.6** | **-2616.6** | **-1870.6** |
| 2021 | 1373.4 | 65.2 | 1150.6 | 953.6 | 490.7 | **157.6** | **354.6** | **817.5** |
| 2022 | 1756.5 | 71.3 | 3482.1 | 782.1 | 765.1 | **-1796.9** | **903.1** | **920.1** |
| 2023 | 2690.8 | 73.6 | 814.1 | 711.1 | 931.8 | **1803.0** | **1906.0** | **1685.4** |
| 2024 | 2362.5 | 80.2 | 831.1 | 712.1 | 1150.6 | **1451.2** | **1570.2** | **1131.7** |
| 2025 | 2529.4 | 90.5 | 1017.8 | 878.8 | 1068.9 | **1421.1** | **1560.1** | **1370.0** |

**EVERY WINDOW, MEAN OWNER EARNINGS, $M.** *[E4-38]: publish every window, because
"growth-rate presentations can be significantly distorted by a calculated selection of either
initial or terminal dates."*

| window | n | mean OE, (c)=D&A | mean OE, (c)=depr only | mean OE, (c)=capex |
|---|---|---|---|---|
| 2023-2025 | 3 | **1,558.4** | 1,678.8 | 1,395.7 |
| 2022-2025 | 4 | 719.6 | 1,484.9 | 1,276.8 |
| **2021-2025 (the five-year default [E2-42])** | **5** | **607.2** | **1,258.8** | **1,184.9** |
| 2020-2025 | 6 | **37.6** | 612.9 | 675.7 |
| 2019-2025 | 7 | 91.8 | 612.3 | 719.5 |
| 2018-2025 | 8 | 139.6 | 617.1 | 650.3 |
| 2017-2025 | 9 | 251.9 | 695.6 | 609.1 |
| 2016-2025 | 10 | 289.6 | 706.9 | 469.8 |
| 2014-2025 | 12 | 276.3 | 660.0 | 367.9 |
| 2011-2025 | 15 | 233.7 | 590.3 | 394.1 |
| **2008-2025 (the whole filed record)** | **18** | **174.5** | 543.2 | 362.4 |
| 2015-2019 (five years, pre-COVID) | 5 | 562.6 | 746.6 | **27.9** |

- **Short-window mean** (2023-2025, (c)=depr only): **$1,678.8M**
- **Long-window mean** (2008-2025, (c)=D&A): **$37.6M is the floor across all windows (2020-2025);
  $174.5M over the full eighteen years**
- **Combined range, window spread × capex band: about $40M to about $1,680M.** The screen’s
  published band was $607M to $1,558M; **those reproduce exactly as the 2021-2025 and 2023-2025
  means at the (c)=D&A end, and the rebuild shows the true width is roughly 42 times wider at the
  bottom than the published one.** The `spread_caveat` was right and understated.
- **Is that range too wide to reach a conclusion? YES, and under [E4-25] that IS the conclusion:**
  *"Usually, the range must be so wide that no useful conclusion can be reached."* A band whose
  bottom is $40M and whose top is $1,680M against a $9,709M market capitalisation spans a yield of
  0.4% to 17.3%. Nothing can be ranked on that.
- **The wide spread is a Q4 finding in its own right [E5-11], and the distorted years are named,
  not hidden.** **FY2020** is the pandemic: operating cash flow of **minus $1,493.0M**, with
  accounts payable and accrued liabilities alone taking **minus $1,383.0M** out as the properties
  closed. **FY2021** is the rebound of that same line, **plus $442.6M**, which is 32.2% of the
  year’s $1,373.4M of operating cash — **this is exactly the screen’s `wc_note`, and it
  reproduces to the dollar from the filed FY2021 cash-flow statement.** Read against Note 8, the
  cause is visible: casino front money went from $133.1M to $206.2M and advance deposits and
  ticket sales from $123.1M to $283.2M as the resorts reopened. **It is neither the DELL shape
  (a payables stretch) nor the INOD shape (a customer prepayment); it is a COVID reopening swing,
  and it is genuinely non-repeating.** The two years are a matched pair: FY2020 understates by
  roughly $1.4bn and FY2021 overstates by roughly $0.4bn.
- **THE DISCLOSED WINDOW JUDGMENT, made in the open as the brief requires.** I do not pick one.
  **All eleven windows are published above**, which is [E4-38]’s own remedy. If a reader wants one
  sentence: the three years since the lease set was completed and the Macau concession reset
  (2023-2025) give $1,396M to $1,679M; the five-year default window [E2-42] gives $607M to
  $1,259M; and the full eighteen-year record gives $175M to $543M. **The spread between them is
  not noise to be resolved — it is the answer.** And the normalisation runs DOWN, not up
  **[E4-41]**: FY2025 operating cash flow was helped by a tax refund (cash taxes were **minus
  $34.6M**), and Q2 2026 Las Vegas casino revenue was helped by a table hold of 29.6% against
  22.9%, a number the registrant itself says is *"not fully controllable by us."*
- **And every figure above is BEFORE the minority leak.** Deduct the FY2025 noncontrolling
  interests’ claim of $315.0M and the 2023-2025 mean falls from $1,678.8M to about $1,364M; deduct
  only the cash that actually left, $169.2M, and it falls to about $1,510M.

### MAINTENANCE CAPEX — THE (c) JUDGMENT, DISCLOSED **[E2-23, E3-44, E2-41, E5-20]**

*"(c) must be a guess — and one sometimes very difficult to make."* **[E2-09, E2-23]**. Here is the
guess and its grounds.

- **The D&A-as-filed end is INVALID for this filer in at least one year and unreliable in the
  rest**, for the reason set out above: FY2022’s $3,482.1M contains $2.7bn of intangible
  amortisation, of which about $2.5bn is a single Macau concession write-off. A (c) that swings
  4.3x on a licence replacement is not measuring *"what the business requires to fully maintain
  its long-term competitive position and its unit volume."*
- **(c) is judged UPWARD, toward total capex, and there are three filed reasons.** First,
  **[E5-20]**’s exception class asks whether the business’s own filing says depreciation
  understates renewal, and MGM’s does so contractually: each triple net lease obligates the
  Company *"to spend a specified percentage of net revenues at the properties on capital
  expenditures"* (Note 11). **Capex here is not discretionary; it is a lease covenant.** Second,
  the record: capex exceeded depreciation-only in each of the last three years — $931.8M against
  $711.1M (2023), $1,150.6M against $712.1M (2024), $1,068.9M against $878.8M (2025). Third, the
  guidance-free but specific forward statement in the MD&A: *"We have planned capital
  expenditures in 2026 of approximately $950 million to $1.05 billion on a consolidated basis."*
  On flat revenue, that is a renewal rate, not a growth rate.
- **Band used: (c) between $878.8M (depreciation only, FY2025) and $1,068.9M (total capex,
  FY2025), and the honest point inside it sits nearer the capex end.** Rooms and casino floors
  are a renewal business; the MD&A attributes FY2025 capex to *"room remodels, casino floor
  remodels and equipment, and information technology"*, every item of which is maintenance in
  substance.
- **Stock compensation subtracted in full [E5-06]:** yes, every year, $90.5M in FY2025. Not
  added back, not netted, not thresholded.
- **The working-capital increment [E2-23] constraint 3:** included, because the construction
  starts from operating cash flow, which nets the change from one audited line. The 2020 and 2021
  swings above are that line doing its work.
- **[E2-60]’s third dimension — financial strength — and it bites.** Restricted earnings are
  those whose payout costs the business *"its ability to maintain … its financial strength"*, and
  *"where leverage rises to fund the payout, (c) was understated."* MGM returned $9,406.8M to
  shareholders over 2021-2025 while cash fell from $4,703.1M to $2,063.0M and while signing a new
  secured yen term loan. **Part of the payout was funded by asset sales and by the balance sheet,
  not by earnings, which is [E2-60]’s own definition of the problem.**

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] great · [ ] good · **[x] GRUESOME, at the registrant level**

*"The worst sort of business is one that grows rapidly, requires significant capital to engender
the growth, and then earns little or no money … Investors have poured money into a bottomless
pit, attracted by growth when they should have been repelled by it."* The filed arithmetic:
**revenue grew 81% from $9,680.1M (2021) to $17,537.7M (2025)**; the growth consumed **$3,914.7M
of acquisitions plus $5,406.1M of capital expenditure** over the same five years, roughly $9.3bn;
and at the end of it **net income attributable to MGM’s own shareholders was $205.9M, domestic
operations lost $237.1M before tax, and the guarantor group’s operating income was $78.5M.**
**[E4-43] is applied honestly and does not rescue it:** the *good* class passes when capital-hungry
growth still earns a satisfactory return — *"nothing shabby about earning $82 million pre-tax on
$400 million of net tangible assets"*, which is 20.5%. MGM’s clean operating income of $1,406.7M
on $29,308.3M of tangible operating assets is **4.8%**, and the domestic half of it is negative.
**[E5-40]**’s benchmark for a satisfactory return on retention is about 12%. This is not that.

### STAYING POWER — SCORE ALL THREE **[E5-11]**, at 2026-06-30 where possible

- **(1) A large and reliable stream of earnings — PARTIAL, and the reliable part is not MGM’s.**
  $17.5bn of revenue is large. But FY2025 pre-tax income was $280.8M, all of it foreign;
  the domestic leg lost money; the segment that grew, MGM China, is 56% owned; and MGM Digital has
  lost money every year and is losing more — Segment Adjusted EBITDAR of $(32.4)M, $(77.2)M and
  $(90.3)M in 2023, 2024 and 2025, with a further $(31)M in the second quarter of 2026 alone.
- **(2) Massive liquid assets — NO, on the scale of the obligations.** Cash and equivalents of
  **$2,547.4M at 2026-06-30** ($2,063.0M at 2025-12-31, *"of which MGM China held $565 million"*),
  against $1,878.8M of operating lease payments due in the next twelve months alone. The
  $2.3 billion revolver was undrawn at 2025-12-31, which is real — but **[E5-39]** is explicit that
  bank lines are not counted: *"We will never be dependent on the kindness of strangers … cash is
  a lot like oxygen."*
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAILS, and it fails by the widest margin of
  the three. This is the one [E5-11] says is "the killer and is the one most often skipped."**
  Named and quantified from the filings, for the twelve months from 2025-12-31:
  - **$1,878.8M of operating lease payments** (Note 11 maturity table), rising every year, to
    $2,010.2M by 2030 and **$54,679.6M in total undiscounted**;
  - **$89.2M of finance lease payments**;
  - **$1,150M of debt maturing in 2026** ($750M MGM China 5.875% notes, $400M parent 4.625% notes);
  - **approximately $350M of consolidated cash interest** in 2026 (MD&A), $210M of it excluding
    MGM China;
  - **$950M to $1,050M of planned capital expenditure** in 2026 (MD&A), part of it obliged by the
    lease covenants;
  - **approximately $269M a year of Macau concession premiums** through 2030 plus **$540M**
    thereafter to the December 2032 expiry, and **$19M a year** for the reverted gaming assets
    (Note 12);
  - **a remaining $2.3 billion of MGM Osaka funding**, to be paid *"on a quarterly basis through
    2028"* for a resort that opens in 2030 and earns nothing before then;
  - **MOP19.7 billion (about $2.5 billion) of committed gaming and non-gaming investment** over
    the ten-year Macau concession, of which MOP18 billion is designated for non-gaming projects.
  Against a consolidated operating cash flow of **$2,529.4M**, of which the domestic guarantor
  group generated the part that pays the $1.8bn of rent, and **that group’s operating income was
  $78.5M.**
- **Leverage, named and quantified — there is no ratio ceiling in this framework and none is
  imposed.** $6,230.1M of debt, net, plus $25,068.7M of operating lease liabilities and $255.0M of
  finance lease liabilities, against $2,429.9M of equity attributable to MGM at 2025-12-31.
  **[E2-54]’s coverage test is the one the corpus supplies**, and it is the right one here because
  it is built to defeat exactly the measure MGM reports: *"whenever someone creates a capital
  structure that does not allow all interest, both payable and accrued, to be comfortably met out
  of current cash flow **net of ample capital expenditures** — zip up your wallet."* Run it on the
  FY2025 filed figures: operating cash flow $2,529.4M, less capex $1,068.9M, leaves $1,460.5M
  against $389.1M of interest paid — **3.75 times, and comfortable**. Run it with the rent
  restored to where [E2-54] would put a fixed, cross-defaulted, parent-guaranteed 29-year
  obligation — that is, treat the $1,867.1M of cash rent as the financing charge it economically
  is — and the numerator becomes $1,460.5M + $1,867.1M = $3,327.6M against $2,256.2M of rent plus
  interest: **1.47 times.** **The framework does not supply a threshold and none is invented. The
  two numbers are reported and the reader is told which convention produced each.**
- **[E3-66] jurisdiction:** the registrant is a Delaware corporation and the US system is the one
  **[E3-66]** calls *"especially favorable to shareholder interests"*. But **44% of the only
  profitable leg sits inside a Hong Kong listed subsidiary operating under a Macau government
  concession**, where MGM’s shareholders stand behind MGM China’s own minority holders, MGM
  China’s own creditors, and a concession the government may decline to extend. That queue is
  stated because [E3-66] says a non-US exposure must state where its shareholders stand in it.

### THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**SHAPE #13, THE TENANT, is the mechanism — with SHAPE #1, CONTRACTED NOT TO STOP, as its
feature.** The index is the authority on the numbering and #13 was KEPT on 2026-09-20 on rows
[E3-79, E3-03]; its one-line mechanism is *"the only product is rented non-exclusively from a few
owners who rent it to every rival and reset the rent at each renewal."* **It fits, with one
honest amendment stated rather than glossed: MGM’s rent is not reset at renewal, it is escalated
by contract at 2% a year, floored at 2% and capped at 3% after year ten or fifteen depending on
the lease.** That difference cuts both ways — it protects MGM from a market reset, and it removes
any possibility that the rent falls when the business does. **No new shape is proposed.** The
non-exclusivity is established from the landlord’s own filing rather than inferred: VICI’s FY2025
10-K says Caesars and MGM are *"our two largest tenants representing 39% and 35%, respectively, of
our annualized rent"*, and the Bellagio landlord is a venture in which MGM holds 5%.

**THE MECHANISM, IN ONE SENTENCE.** MGM sold the only asset in its business that could not be
reproduced, kept the operations, and signed contracts obliging it to pay a rising real price for
the use of what it used to own — so any decline in the revenue the buildings produce lands
entirely on the shareholders’ residual, which is already thin, while the landlord’s claim rises 2%
a year whatever happens.

**QUANTIFIED FROM FILED FIGURES, in the corpus’s own form [E3-24] — "Consider some mathematics".**
- The domestic guarantor group earned **$78.5M** of operating income on $10,580.2M of revenue in
  FY2025, after **$2,258.4M** of triple net lease rent expense. Adjusted for the $278.9M
  impairment and $126.0M of property losses, call it **$483M**.
- Contractual rent rises **2.0%** a year, floored at 2% and capped at 3%. Two per cent of the
  FY2026 payment of $1,878.8M is **$37.6M a year, compounding**.
- Las Vegas Strip Resorts revenue fell **4.3%** in FY2025 ($8,816.1M to $8,441.5M) and Segment
  Adjusted EBITDAR fell **8.0%**. Regional Operations revenue fell **4%** in the second quarter of
  2026 as reported (up 3% same-store).
- **So: hold the domestic guarantor group’s revenue flat and let the rent escalate at 2%, and the
  $483M of adjusted operating income is consumed in roughly thirteen years by the escalator
  alone.** Now suppose instead a single recessionary year in which domestic revenue falls the
  **4.3%** it actually fell in Las Vegas in 2025, at the FY2025 domestic contribution margin
  implied by the segment tables (Las Vegas Strip Resorts Segment Adjusted EBITDAR margin 33.9%):
  **$10,580.2M × 4.3% × 33.9% = $154M of lost profit in one year**, against $483M of adjusted
  operating income and a rent bill that rises $37.6M in the same year. **Three such years in a row,
  with the escalator running, take the domestic group to roughly minus $150M of operating income
  while it still owes $2.0 billion of cash rent.** The holes are then filled from Macau dividends
  — of which **44 cents in the dollar go to other shareholders** and all of which require the
  approval of a separately listed company’s board — or from asset sales, of which three have
  already been made (The Mirage, Gold Strike Tunica, Northfield Park) and each one **reduced the
  revenue base as well as the rent**.
- **The covenant is the accelerator.** Note 11: failing the leases’ financial covenants *"would
  require the Company to maintain either cash security or one or more letters of credit in favor
  of the landlord in amounts ranging from **six months to two years of rent**"* — that is
  **$0.9bn to $3.8bn** of cash or letters of credit demanded precisely when the cash is scarcest.
  And per VICI’s own filing the master lease is **cross-defaulted across the entire portfolio**,
  so no single weak property can be handed back.

**THE LIKELIHOOD, in the corpus’s vocabulary:** **[x] a real possibility.** Not *likely*, because
the Macau leg is currently growing, BetMGM has turned profitable ($59.6M of MGM’s share of
operating income in FY2025 against $(110.1)M in FY2024), the revolver is undrawn and the 2026
maturities are modest against $2.5bn of cash. Not *a low-level possibility*, because **the
domestic leg has already crossed into a pre-tax loss and the guarantor group’s operating income
has already fallen 94% in two years while revenue was flat** — the mechanism is not a forecast,
it is in the filed record for FY2025.

**[E4-40] — EXPOSURE, NOT EXPERIENCE.** *"all of us in the industry made a fundamental
underwriting mistake by focusing on experience, rather than exposure."* The benign reading here
would be that MGM survived a total shutdown in 2020 and is still here. That is experience, and it
is dangerous as a guide, because **the balance sheet that survived 2020 owned Bellagio, MGM Grand,
Mandalay Bay, Aria and The Mirage outright, and could sell them — which is exactly what it did.
The exposure today is a company that has already spent that option.** The 2020 rescue is not
available a second time.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

'''

a = t.index(u"## Q3 — ARE THEY HONEST")
b = t.index(u"---\n⛔ **Q5 does not open")
t = t[:a] + q3 + q4 + t[b:]
io.open(P, "w", encoding="utf-8").write(t)
print("ok", len(t))
