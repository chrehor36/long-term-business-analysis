# -*- coding: utf-8 -*-
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-12 Run - ROKU Roku.md"
t=open(p,encoding='utf-8').read()

rest = r"""## THE ONE NUMBER — SBC AGAINST OPERATING CASH, AND ROKU SETS THE RECORD **[E5-06, E3-70]**

*"To say 'stock-based compensation' is not an expense is even more cavalier"* **[E5-06]**, and
the brief's calibrated row exists so that a large figure can be read against something. **Every
year resolves; none is silently zero** (the defect fixed 2026-09-12 that was subtracting zero
SBC on 21 names does not touch Roku, and it is checked year by year below).

| FY | operating cash flow ($k) | SBC ($k) | **SBC ÷ OCF** |
|---|---|---|---|
| 2016 | (32,463) | 8,206 | n/m (OCF negative) |
| 2017 | 37,292 | 10,953 | 29.4% |
| 2018 | 13,922 | 37,674 | **270.6%** |
| 2019 | 13,707 | 85,175 | **621.4%** |
| 2020 | 148,192 | 134,076 | 90.5% |
| 2021 | 228,081 | 187,532 | 82.2% |
| 2022 | 11,795 | 359,931 | **3,051.6%** |
| 2023 | 255,856 | 370,130 | **144.7%** |
| 2024 | 218,045 | 384,662 | **176.4%** |
| 2025 | 483,718 | 354,169 | 73.2% |
| **TTM to 2026-06-30** | **719,037** | **328,038** | **45.6%** |

*Every figure from the filed Consolidated Statements of Cash Flows of the 10-K for that year;
TTM built as FY2025 less H1-2025 plus H1-2026 from the 10-Q of 2026-08-06 — OCF reconciles to
the dollar with the $719,037 the company itself reports in its own TTM table.*

**CUMULATIVE, WHICH IS THE COMPARABLE FIGURE IN THE BRIEF'S ROW:**
- **2016-2025: cumulative OCF $1,378,145k · cumulative SBC $1,932,508k · SBC/OCF = 140.2%**
- 2021-2025 (five years): $1,197,495k / $1,656,424k = **138.3%**
- 2023-2025 (three years): **115.8%**

**The calibrated row, with Roku placed in it:**

| name | cumulative SBC/OCF |
|---|---|
| **ROKU** | **140.2%** |
| CALX | 98.4% |
| ARM | 96.6% |
| PINS | 68.6% |
| CRWD (closed the file) | 68.0% |
| ELF | 40.9% |
| PLTR | 32.0% |
| QLYS | 24.9% |
| BE | 24.5% |
| CRM | 23.4% |
| SHOP | 22.1% |
| PAY | 11.5% |

**Roku is first in the queue and it is first by 42 points. Over ten filed years the business
generated $1.38 billion of operating cash and paid its employees $1.93 billion in stock — it
paid out 1.40 dollars of equity for every dollar of cash it produced.** That is not a ratio
that needs interpreting; on the framework's own arithmetic (OE = OCF − SBC − (c)) it means
owner earnings were negative for the decade before the (c) guess is even made.

**And [E3-70] says the reported charge is the FLOOR of the subtraction, not the measure** —
*"an amount equal to what the company could have realized by publicly selling options of like
quantity and structure."* Roku's awards are overwhelmingly time-vesting RSUs, for which the
grant-date fair value and the market value coincide, so the floor and the measure are close
here; no upward adjustment is made and none is available from the filing. **The downward
pressure is real and is stated for fairness: SBC peaked at $384,662k in FY2024 and has fallen
to a $328,038k TTM rate while operating cash more than trebled, and the company guided SBC
down to "approx. $325M for 2026" (Q1 2026 shareholder letter).** The trend is the right way.
The cumulative record is the one in the table.

---

## THE 351% CONTRACT-LIABILITY FLAG — DECODED TO THE DOLLAR, AND THE FLAG NAMES THE WRONG LINE

**What the line is.** The `wc_note` flag fires on `IncreaseDecreaseInContractWithCustomerLiability`.
At Roku that tag carries the **`Deferred revenue` line of the Consolidated Statements of Cash
Flows**. The reading reproduces exactly:

> **FY2022 `Deferred revenue` in the cash-flow statement = +$41,402 thousand.
> FY2022 `Net cash provided by operating activities` = $11,795 thousand.
> 41,402 ÷ 11,795 = 351.0%.** Both figures read off the filed FY2022 statement (10-K accession
> 0001428439-23-000007, Consolidated Statements of Cash Flows), and both agree with the FY2022
> XBRL to the dollar.

**What operating cash looks like without it: FY2022 operating cash flow was $11,795k. Strip the
deferred-revenue increment and it is −$29,607k — negative.** So the flag's underlying claim is
true: without customer money arriving early, Roku's FY2022 operating cash flow was negative.

**And it IS customer money, which is worth saying because the DELL and INOD precedents were
different animals.** The FY2022 movement was almost entirely the **Platform** half of deferred
revenue: current Platform deferred revenue went $17,144k → $59,276k, **+$42,132k**, while the
Devices half was flat ($56,276k → $55,643k). The filing's own explanation: *"Deferred revenue
increased by approximately $41.4 million during the year ended December 31, 2022 primarily due
to the **billings in excess of revenue recognized** and timing of fulfillment of performance
obligations related to revenue arrangements."* Advertisers and content partners paid ahead.

**But the flag is diagnostically wrong, and this is a tooling finding, not a company finding.**
Three reasons:

1. **The percentage is a denominator artifact.** $41.4M is an ordinary movement on a deferred
   revenue balance that has never exceeded **$149.8M, or 3.2% of revenue** (FY2025) — a smaller
   share of revenue than DELL's payables swing and only three times PINS's 1.1%. It read as
   351% because FY2022 operating cash had already collapsed from $228,081k to $11,795k.
   **`wc_note` divides a balance-sheet delta by a single year's operating cash; on any year
   whose operating cash is near zero, every routine delta reads as a giant percentage.** This
   is the same defect class as the `ZeroDivisionError` that made MU and INTC re-triage as
   UNPRICED and the two-different-windows artifact in INTC's band: **near-zero denominators.**
2. **It names the smallest of the FY2022 working-capital movements.** Read the same filed
   statement one line at a time. FY2022's actual working-capital event was
   **`Content assets and liabilities, net` = −$313,204k**, against −$193,440k the year before —
   **7.6 times the deferred-revenue line, in the opposite direction, and the screen does not
   test it at all.** The FY2022 collapse in operating cash was a $498.0M net loss plus a
   $313.2M content build; the $41.4M of advertiser prepayments was a small offset to it.
3. **The line the screen should watch at Roku is content, and the reason matters for (c).**
   Content is Roku's real capital expenditure and it runs through **operating** cash, not
   investing: `Amortization and write-off of content assets` of $223,230k added back in FY2025
   and `Content assets and liabilities, net` of −$184,457k taken out. Purchases of property and
   equipment are only **$5,280k** because the capital this business consumes is programming, and
   the cash-flow statement already nets it. Any owner-earnings construction that adds D&A back
   without noticing this would be double-counting; the construction below does not.

**Second-largest movement, also untested by the flag and also material:**
`Accounts payable` was **+$248,175k in FY2023 — 97.0% of that year's $255,856k of operating
cash** — and it was handed back over the following two years (−$110,678k in FY2024, −$122,503k
in FY2025). **If the screen had a single working-capital flag to fire on Roku, that was it.**

---

## OWNER EARNINGS — EVERY WINDOW PUBLISHED **[E4-38]**, BOTH (c) ENDS, AND THE SCREEN'S TWO NUMBERS ARE TWO DIFFERENT WINDOWS

**(c) IS A DISCLOSED JUDGMENT [E2-23, E3-44].** The corpus default is D&A **[E3-44, E2-41]**,
and the exception class is the capital-intensive filer whose depreciation understates renewal
**[E5-20]**. **Roku is neither case cleanly, and the judgment is written down here.** Its total
capex is $5,280k against D&A of $68,904k — depreciation currently runs **13 times** capital
spending, because the asset base being depreciated is offices Roku is exiting ($131.6M of
right-of-use assets and $72.3M of property and equipment impaired in the FY2023 restructuring)
plus acquired intangibles. So **D&A is the CONSERVATIVE end here and capex is the generous
end** — the reverse of the railroad case. Both ends are shown. **Separately-tagged capitalised
software: checked and there is none** — Roku tags no `CapitalizedComputerSoftwareNet` and no
software-development capitalisation line; its development cost is expensed in R&D ($729,477k in
FY2025). The HAS/CRWD defect does not apply. **Content, the one capitalised asset that matters,
is inside operating cash already** (above), so it is not added to (c) — the alternative would
double-count it.

| window | mean OCF ($k) | mean SBC ($k) | **OE, (c)=capex ($k)** | **OE, (c)=D&A ($k)** |
|---|---|---|---|---|
| 11 filed years, 2016-2025 | 137,814 | 193,251 | **(104,477)** | **(91,860)** |
| five years, 2021-2025 *(the corpus default window [E2-42])* | 239,499 | 331,285 | **(150,725)** | **(150,453)** |
| five years, 2020-2024 | 172,394 | 287,266 | **(189,232)** | **(167,000)** |
| early five, 2016-2020 | 36,130 | 55,217 | **(58,230)** | **(33,267)** |
| three years, 2023-2025 | 319,206 | 369,654 | **(81,434)** | **(117,802)** |
| two years, 2024-2025 | 350,882 | 369,416 | **(23,704)** | **(84,343)** |
| **FY2025 alone** | 483,718 | 354,169 | **+124,269** | **+60,645** |
| **TTM to 2026-06-30** | 719,037 | 328,038 | **+381,868** | **+322,135** |

**THE SCREEN'S ROW REPRODUCES, AND IT IS THE INTC DEFECT AGAIN.** `oe_bottom_m −151` is the
**five-year 2021-2025 mean at the capex end** (−$150,725k). `oe_top_m −81` is the **three-year
2023-2025 mean at the capex end** (−$81,434k). **They are two different windows, not two ends
of a capex band.** The advertised "spread $−151M to $−81M" therefore measures nothing about the
(c) guess; the real capex band inside a single window is $12.6k wide on the five-year
(−150,725 vs −150,453) and $36.4M wide on the three-year. And
`level_shift_oe "EARLY HALF STRADDLES ZERO (from −$509.8M)"` is FY2022 at the capex end
(−$509,832k) — a single year, correctly computed.

**REBUILT, IN DOLLARS AND A WORD: −$189M to +$382M — and the word is STRADDLES.**
A $571 million width on a $23.0 billion market capitalisation. Eight windows, two (c) ends,
sixteen constructions; **fourteen are negative and the two positive ones are the most recent
year and the trailing twelve months.**

**WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW [E4-41] — the judgment, written down.**
*"Using precise numbers is, in fact, foolish"* **[E4-25]**, and *"Do not pick a window and
justify it"*, so every window above stands. But the framework also requires a judgment about
which years are the same company, and mine is **FY2024, FY2025 and the TTM**, for four reasons
that are dated in the filings and not inferred: the cost base was reset by the restructuring
that ran from Q4-2022 to FY2024 ($356,094k of charges in FY2023, $30,999k in FY2024, $3,064k in
FY2025); total operating expenses fell from roughly $2,335M (FY2023) to $2,023.8M (FY2024) and
have grown 3% since; SBC peaked in FY2024 and is falling; and the company's own internal
reporting changed in Q1-2026, which is the filed evidence of what management now manages.
**On that basis the range is −$84M to +$382M, and it still straddles zero.**

**AND THE MEAN IS NORMALISED DOWN FOR LUCK [E4-41], because the TTM carries two named
favourable breaks and the company quantified one of them itself:**
1. **A tariff refund.** Q2 2026 letter, verbatim: *"Devices … gross margin of 20.1%, which
   benefited from an IEEPA refund for tariff payments paid in Q2 2025 through Q1 2026.
   **Excluding the IEEPA refund, Q2 Devices gross margin would have been (7.6%), net income
   would have been $127 million**, and Free Cash Flow would have been $242 million."* That is
   roughly **$37M** of cash that will not recur, and it is the difference between Devices
   showing its first positive gross profit in five years and showing another loss. Credit where
   it is due: the company disclosed it unprompted and quantified it — that is the [E2-26]
   half-owner standard met.
2. **A United States election year.** *"Q2 political advertising on the Roku platform exceeded
   the comparable quarter from the 2024 U.S. presidential election cycle … political ad spend on
   our platform is weighted toward the back half of the year."* A biennial cash inflow, only
   partly inside this TTM and therefore inflating the windows ahead of it more than this one.

**Normalised TTM owner earnings: $719,037k − $37,000k of tariff refund = $682,037k of operating
cash; less $328,038k of SBC; less (c) of $9,131k (capex) or $68,864k (D&A) = +$344,868k to
+$285,135k.** Call it **roughly +$285M to +$345M**, and say plainly that it is one year of a
ten-year record whose other nine years are negative.

---

## Q3 ITEMS — NO VERDICT IS WRITTEN; THE GATE IS CLOSED AT Q2 **[E2-01, E4-22, E4-29, E2-49, E4-30, E5-08, E4-52]**

*Recorded, not scored. The hard sequence (operator rule 2) forbids a Q3 verdict once Q2 returns
OUT, and a verdict written anyway would be the thing operator rule 9 warns about: a finding
produced because the work was done rather than because the gate was open.*

**[E2-49] metric-switching has already fired at Q2 and is the sharpest item in this file.** It
is recorded there because a discarded unit series is a *moat measurement* problem first and a
*manager* problem second.

**THE WEIGHT CASE, declared even though no verdict follows.** Daily execution — **ticked**: an
advertising platform whose inventory is re-sold every day and whose OEM licences are
renegotiated periodically is a have-to-be-smart-every-day business **[E3-38]**. Control — not
ticked. Leverage — not ticked; there is no debt. **One box ticked, so Q3 would have been a
BINARY GATE had it opened**, and that is worth recording precisely because it means no price
would have compensated **[E1-16, E3-29]**.

**[E2-01] THE PRIMARY TEST — a high earnings rate on equity capital employed, not EPS growth.**
This is the item that would have mattered most, and it is also **[E3-46]**, which the corpus
asks *about the business, before the manager*:

| FY | net income ($k) | **operating income ($k)** | stockholders' equity ($k) | return on equity |
|---|---|---|---|---|
| 2019 | (59,937) | (65,059) | 698,426 | negative |
| 2020 | (17,507) | (20,253) | 1,328,015 | negative |
| 2021 | 242,385 | **235,100** | 2,766,606 | 8.8% |
| 2022 | (498,005) | (530,888) | 2,646,556 | negative |
| 2023 | (709,561) | (792,377) | 2,326,333 | negative |
| 2024 | (129,386) | (218,167) | 2,492,737 | negative |
| **2025** | **88,361** | **(5,624)** | 2,657,945 | **3.3%** |

**Nine of the ten filed years show an operating loss. The single profitable operating year is
2021. And FY2025's positive net income is not the business: operating income was −$5,624k and
total other income, net was +$99,522k — interest on the cash pile.** On unleveraged net
tangible assets **[E2-43]** (equity $2,657,945k less goodwill $309,406k less intangibles
$50,207k = $2,298,332k) the FY2025 return is **3.8% on net income and −0.2% on operating
income.** *"The best businesses, by definition, are going to be businesses that earn very high
returns on capital employed over time"* **[E3-46]**. Over its filed life Roku has earned no
return on capital employed at all. **And the equity is contributed, not retained:** additional
paid-in capital $4,145,485k against an accumulated deficit of **−$1,488,594k** at 2025-12-31.
Of roughly $4.15 billion put in, $1.49 billion has been consumed.

**[E4-29] THE FIFTH FLAG — FIRES AT FULL STRENGTH, AND IT FIRES IN THE 10-K ITSELF, NOT ONLY IN
THE FURNISHED EXHIBITS.** The CGNX companion rule says to pull the 8-K EX-99.1 before scoring
this, because a run that reads only the annual report will score clean a company that built its
narrative on a non-GAAP metric. **Here the annual report is enough on its own:**

> *"The key performance metrics we use to evaluate our business, measure our performance,
> develop financial forecasts and make strategic decisions are Streaming Hours, Platform
> revenue, **Adjusted Earnings Before Interest, Taxes, Depreciation and Amortization ("Adjusted
> EBITDA")**, and Free Cash Flow."* — FY2025 10-K, Item 7
> *"We use Adjusted EBITDA as a primary metric to measure the performance of our business
> because it represents our ability to successfully manage profitability. **Our goal is to grow
> Adjusted EBITDA over time, driving continued growth in stockholder value.**"*

*"Trumpeting EBITDA … is a particularly pernicious practice. Doing so implies that depreciation
is not truly an expense, given that it is a 'non-cash' charge. **That's nonsense**"* **[E4-29]**.
And **Roku's version removes more than depreciation. The number in the filed reconciliation:**

| FY2025 ($k) | |
|---|---|
| Net income | 88,361 |
| less total other income, net | (99,522) |
| **add back stock-based compensation** | **354,169** |
| add back depreciation and amortization | 68,904 |
| add back restructuring charges | 3,064 |
| add back income tax expense | 5,537 |
| **Adjusted EBITDA** | **420,513** |

**Adjusted EBITDA of $420,513k sits against a GAAP operating loss of $(5,624)k — a gap of
$426,137k, of which $354,169k, or 83%, is stock-based compensation.** The metric the company
uses to make strategic decisions deletes the largest real cost in the business, which is the
precise thing [E5-06] refuses to allow. **And the same is true of the other headline.** "Free
Cash Flow" is defined as *"trailing 12-month cash flows from operating activities excluding
purchases of property and equipment and the effects of exchange rates on cash"* — with capex of
$5,280k, **Roku's Free Cash Flow is operating cash flow to within 1%**, and operating cash flow
adds SBC back. The Q2 2026 letter calls **Free Cash Flow per share** *"our north star metric."*
A north star that adds back $328M of annual equity issuance while the denominator counts the
shares it issues is measuring the same thing twice in opposite directions.

**[E4-22]'s other flags, each a prompt to read and each read:**
- **weak accounting** — not found. The statements are conventional, the segment recast was
  auditor dual-dated, the revenue-recognition note discloses the judgmental items (stand-alone
  selling prices, variable consideration, principal-versus-agent, non-cash consideration) and
  the $95.1M Frndly TV purchase price allocation is laid out. **Non-cash consideration in the
  transaction price is a live judgment and is disclosed as one** — Roku takes advertising
  inventory as consideration from content partners, which is a barter revenue stream valued by
  management. That is a prompt, and the prompt is answered by disclosure rather than by silence.
- **unintelligible footnotes** — not found. They are long but plain.
- **trumpeted earnings projections** — **fires**, with the unusual feature that the record is
  good. Roku guides quarterly and annually on revenue, gross profit, net income and Adjusted
  EBITDA. **[E3-48]** says to set the guidance against the outturn, so:

| outlook, given in | for | revenue | gross profit | net income | Adj. EBITDA |
|---|---|---|---|---|---|
| Q3 2025 letter | Q4 2025E | $1,350M | $575M | $40M | $145M |
| **actual Q4 2025** | | **$1,394.9M** | **$606.8M** | **$80.5M** | **$169.4M** |
| Q4 2025 letter | Q1 2026E | $1,200M | $530M | $50M | $130M |
| **actual Q1 2026** | | **$1,248.9M** | **$564.9M** | **$85.7M** | **$148.4M** |
| Q1 2026 letter | Q2 2026E | $1,295M | $580M | $90M | $170M |
| **actual Q2 2026** | | **$1,354.7M** | **$673.7M** | **$164.2M** | **$254.3M** |

**Beaten on every line in three consecutive quarters, by a widening margin** — net income 2.0x,
1.7x and 1.8x the guide. Under [E3-48] a beaten record earns weight, and it is given. But
**[E5-30]** is the countervailing reading and it is about the behaviour, not this year's
outturn: *"once you start it, it's all over … forecasting earnings, I can't imagine anything
more destructive."* A company that guides on Adjusted EBITDA quarterly, raises the annual
number mid-year, and publishes a 2028 target (*"$1 billion of Free Cash Flow by 2028, if not
sooner"*) has installed a ratchet. **And it has now switched itself off** — the Q2 2026 letter:
*"In light of the pending transaction, we will not host an earnings call and will not provide a
financial outlook."*
- **serial share issuance [E5-15]** — **does not fire on the flag's own terms.** The flag is
  about issuing stock to raise money as a promotion. Roku's share count went 99.157M (2017) to
  **147.850M (2025)**, +49.1%, but the recent rate is 1.7% then 1.3% a year and the cash-flow
  statement shows no capital raise since 2021 — only *"Proceeds from equity issued under
  incentive plans"*. The dilution is the SBC already counted above, not a promotion. Counting it
  twice would be the double-windage [E4-11] forbids.
- **filed-figure tells [E4-30]** — **checked and clean, with the reason.** Reported growth is
  not unnaturally smooth; it is violently unsmooth (operating income −$20M, +$235M, −$531M,
  −$792M, −$218M, −$6M). Cash taxes: $6,632k (2023), $19,406k (2024), **$13,690k (2025)** —
  against pretax losses in two of those years and $93,898k of pretax income in 2025, i.e. 14.6%.
  The low rate has an innocent, disclosed cause: *"We have a full valuation allowance against
  net deferred tax assets in the United States as of December 31, 2025."* **[E4-30]**'s tell is
  cash taxes *falling as a share of reported pretax income*; here they rose from nothing to
  14.6% as income appeared. No tell.
- **restructuring charges [E3-53, E5-33]** — **$356,094k (2023), $30,999k (2024), $3,064k
  (2025), and they are IN the owner-earnings mean above, not annualised away.** *"To tell owners
  year after year, 'Don't count this' … is misleading"* **[E5-33]**. Roku's own Adjusted EBITDA
  reconciliation removes them; this run's arithmetic does not, because they ran through operating
  cash and through the asset base ($131.6M of lease impairments, $72.3M of property impairments,
  $65.5M of content impairments, $83.2M of severance). They were borne by shareholders.

**[E5-08] THE BUYBACK — and the operator's likely prior is refuted in the company's favour.**
A $400M authorisation approved in Q3 2025, running to 2026-12-31; **1.5 million shares bought in
FY2025 for $149,982k, an average of $99.99 a share**; $250.0M remained at year end. **Nine
months later the board agreed to sell the whole company for consideration worth $159.90 a
share.** Condition (1), ample funds: satisfied — $2.2bn of liquidity and no debt. Condition (2),
a material discount to conservatively calculated intrinsic value: **satisfied in fact by the
board's own subsequent act**, at a 37% discount to the price it then accepted. Condition (3),
the third one from [E4-31] — *"Shareholders should have been supplied all the information they
need for estimating that value"*: **this is where it fails**, and the failure is the Q2 finding
again. The company deleted its installed-base count and its ARPU from the 10-K filed
2026-02-13 and was buying its own stock through the second half of 2025. **A buyback executed
at a real discount against a register that has just been deprived of the two metrics needed to
value the asset is [E4-31]'s named case.** And the stated *purpose* is not the [E5-08] purpose:
*"Combined with the net share settlement program we implemented in 2023, we see a clear path to
**fully offset dilution** in 2026 … align with our north star of maximizing Free Cash Flow per
share."* Buying stock to neutralise SBC is an expense being reimbursed, not capital being
returned. **The arithmetic of that, for FY2025: $149,982k of repurchases plus $164,850k of
"Taxes paid related to net share settlement of equity awards" = $314,832k, or 65.1% of the
year's $483,718k of operating cash, spent on managing the share count.** More went to employee
tax withholding than to shareholders.

**[E4-52] PAY, AND IT IS THE MOST UNUSUAL FINDING IN THE FILE.** From the DEF 14A filed
2026-04-24 (accession 0001140361-26-016715), verbatim: *"We do not pay our executive officers
cash bonuses or **grant equity awards tied to either individual or corporate performance
goals** because we expect our executives to perform at the highest level regardless of possible
bonus or other award payouts tied to discrete metrics. In determining each executive officer's
total compensation target, the Compensation Committee considers, among other factors, **what an
executive officer would be paid by another employer, what we would have to pay to replace the
executive officer**…"* The same policy runs to every employee (FY2025 10-K, Human Capital):
*"we generally do not pay cash bonuses … or have performance-based equity awards."*

**Read both ways, because both are true.** *In Roku's favour:* there is no bullseye to be
mis-set, so the ULTA finding (pay at ~182% of a target set 10.4% below the prior year's actual)
is structurally impossible here, and [E5-30]'s incentive to make the numbers is not installed
in the pay plan. *Against:* time-vesting RSUs priced off replacement cost pay identically
whether the business earns 8.8% on equity or loses $792M, and [E2-01] exists precisely to judge
*"managerial economic performance"* against a number. In June 2025 the Compensation Committee
raised the CEO's and the CFO's total compensation targets by **4% and 20%** respectively, *"in
alignment with our compensation philosophy"* and delivered through larger equity grants — in the
year the company reported a GAAP operating loss.

**[E2-30] THE INSTITUTIONAL IMPERATIVE — scored, not a fraud test.**
- resists change in current direction — **no**. The 2022-2024 restructuring was a real reversal,
  and opex was genuinely cut.
- projects or acquisitions materialise to soak up available funds — **partly**. Frndly TV was
  bought in May 2025 for $95,090k of cash plus $65,815k of non-cash contingent consideration;
  Howdy was launched; Nielsen's advanced video advertising business was bought in 2021. All
  adjacent to the base business, none a diversification.
- staff studies to justify the leader's craving — **not found in the filings.**
- peer behaviour mindlessly imitated — **yes, at the metric level.** Adjusted EBITDA, "Free Cash
  Flow per share" as a "north star", and a segment split into Advertising and Subscriptions are
  the standard vocabulary of the ad-tech peer group Roku itself lists (Magnite, PubMatic, Trade
  Desk, Pinterest, Snap).

**FOUNDER CONTROL — a Q3 item and a charter item, and it is now spent.** Anthony Wood, founder
and CEO, holds essentially all 16,368,064 Class B shares, ten votes each, **55.3% of the voting
power**; the 8-K of 2026-06-15 confirms the Wood-affiliated Voting and Support Agreement
stockholders held *"approximately 55% of Company's outstanding voting power."* Under a dual-class
structure the public Class A holders could not have stopped this transaction and did not need to
be persuaded by it — **the deal was decided by one holder and the vote is a formality.** The
economics are identical per share, so no Class A holder is disadvantaged in the consideration.
Recorded as a governance fact, with no verdict.

**THE GUARDRAIL, checked [E2-37, E2-38, E3-39].** Nothing in the above is used to promote the
name: the good guidance record, the buyback at a discount, the absence of pay gaming and the
falling SBC are all recorded, and **none of them can repair Q2 or substitute for Q4.** *"A
textile company that allocates capital brilliantly within its industry is a remarkable textile
company — but not a remarkable business"* **[E2-37]**. **And the key-person question is booked
where the corpus books it:** Roku's moat is not claimed to require a superstar, so no [E4-23]
moat defect is recorded — but the Q2 2026 letter's own framing of *"The Roku Experience … remains
a powerful competitive advantage"* rests on continuous product execution (a new Home Screen
described as *"our biggest update in more than a decade"*), which is [E4-04]'s continuously-rebuilt
question and is answered at Q2.

---

## Q4 ITEMS — RECORDED **[E5-11, E4-20, E2-54, E3-52, E2-27]**

*No verdict. The gate is closed at Q2.*

**STAYING POWER — all three scored [E5-11], at 2026-06-30 from the 10-Q.**
1. **A large and reliable stream of earnings — NO.** Gross profit is large ($2,074.4M FY2025,
   $1,238.6M in H1-2026) and has risen every year. **Earnings are neither large nor reliable:**
   nine operating losses in ten years, FY2025 operating income −$5,624k, and the only positive
   net income years are 2021 and 2025.
2. **Massive liquid assets — YES, and this is the strongest thing in the file.** Cash and
   equivalents **$2,001,815k** plus short-term investments **$555,387k** = **$2,557,202k**,
   against **zero interest-bearing debt**. Cash paid for interest in FY2025 was $1,055k. The
   liquidity is 11.1% of the market capitalisation and 1.8x the cumulative operating cash the
   business has ever produced.
3. **No significant near-term cash requirements — YES, and this is the one usually skipped.**
   Purchase commitments total **$561,117k, of which $389,489k falls in 2026** (content $124,320k,
   manufacturing $158,436k, other $106,733k). Operating lease liability $386,410k non-current plus
   $87,425k current. Uncertain tax positions $5,200k. **Total near-term calls are a fraction of
   the liquid assets and nothing is owed to a lender.** *"We will never be dependent on the
   kindness of strangers"* **[E5-39]** — on this test Roku passes cleanly.

**Leverage, named and quantified [E4-16, E3-29]: there is none.** Total liabilities $1,749,094k
at 2026-06-30 are accounts payable $167,197k, accrued liabilities $967,334k, deferred revenue
$149,104k, non-current operating lease liability $386,410k and other long-term $79,049k. **[E2-54]**'s
coverage test is vacuous because there is no interest to cover. **[E3-52]** says read the terms,
not the quantity, and the terms cut both ways: the deferred revenue is customer-prepaid,
covenant-free money of the good kind, but the **operating leases are dated, covenanted rent on
offices the company has already written down** — the opposite of float, and $131.6M of the
right-of-use assets behind them were impaired in 2023.

**Is the contract-liability balance customer money on the balance sheet? Partly, and it is
small.** Total deferred revenue $149,760k at 2025-12-31, of which **Platform $65,606k** (genuine
advance billings from advertisers and content partners) and **Devices $84,154k** (the portion of
a device's price allocated to *"unspecified upgrades and updates on a when-and-if available
basis"* — an accounting allocation of cash already collected at the point of sale, not a new
prepayment). **So 56% of the balance is not customer float at all; and the whole balance is 3.2%
of revenue and 5.9% of liquid assets.** It funds nothing.

**GREAT, GOOD OR GRUESOME [E4-20, E4-43] — gruesome, on the corpus's own definition, and the
definition has to be applied in the right currency.**
*"The worst sort of business is one that grows rapidly, requires significant capital to engender
the growth, and then earns little or no money."* Roku grew revenue from $398,649k (FY2016) to
$4,737,251k (FY2025), **11.9x**. The capital it required was not plant — capex over the ten
years totals $490,411k — it was **equity**: $4,145,485k of paid-in capital, of which
**$1,932,508k was stock paid to employees** and **$1,488,594k has been consumed** into the
accumulated deficit. And what it earns is an operating loss in nine years of ten.
**[E4-43]** insists the *good* class passes and warns against over-reading, so the test is
applied at its own bar: the good class earns *"$82 million pre-tax on $400 million of net
tangible assets"* — 20.5%. Roku earns **−0.2% of operating income on $2,298,332k of unleveraged
net tangible assets.** That is not the good class. **The one honest qualification, and it is
real: the TTM is the first period in which the arithmetic is not gruesome** — $719,037k of
operating cash, $328,038k of SBC, positive owner earnings on both (c) ends. One period.

**THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40] — and the filing names the
mechanism itself.**

**The mechanism: the operating system is displaced by the people who make and sell the
televisions, and Roku's installed base then decays with the TV replacement cycle while its
fixed cost base does not.** Roku does not own the shelf, the set, or the customer relationship.
Three filed facts make it concrete, all from the FY2025 10-K Risk Factors:

> *"Large companies such as **Amazon, Apple, and Google** offer TV streaming devices that compete
> with Roku streaming devices and those of our licensed Roku TV partners and the Roku TV OS.
> Google licenses its Android operating system software for integration into smart TVs,
> **including those of certain of our existing TV partners** … Amazon licenses its operating
> system software for integration into smart TVs and sells Amazon-branded smart TVs. We also
> face increased competition from **Walmart** … in light of its acquisition of **Vizio** … and the
> integration of Vizio's operating system into Walmart products **instead of other third-party
> proprietary operating systems.** These companies have greater financial resources than we do
> and **can subsidize the cost of their streaming devices or licensing arrangements**…"*

> *"**at times our existing licensed Roku TV partners have chosen to work exclusively with, or
> divert a significant portion of their business with us, to other operating system
> developers.**"*

> *"**Amazon, Best Buy, Target, and Walmart in total accounted for 81% of our Devices revenue**
> for each of the years ended December 31, 2025 and 2024 … **We have no minimum purchase
> commitments or long-term contracts with any of these retailers or distributors** … Our retailers
> and distributors also sell products that compete with our products … including house-branded
> televisions sold by such retailers that **utilize TV operating systems other than the Roku TV
> OS.**"*

**Two of the four retailers who are 81% of Devices revenue own competing television operating
systems, and Roku has no long-term contract with any of them.**

**QUANTIFIED FROM FILED FIGURES.** The installed base is ~90 million households and a television
is replaced roughly every seven years, so the base requires **~13 million household
replacements a year** simply to stand still — which is exactly the ~9.8 million net additions
plus churn that Roku has been running. Suppose OEM and retailer defection halves the gross
household inflow. Platform revenue is $4,144.9M at a ~52.0% gross margin, so Platform gross
profit is $2,156.4M and each 1% of base decline costs about **$21.6M of gross profit** at
constant ARPU. **A 7% annual decline in the base — half the replacement cycle going elsewhere —
removes ~$151M of gross profit a year, compounding.** Against total operating expenses of
$2,080.0M and consolidated gross profit of $2,074.4M, **Roku's operating line is already at zero
and has no cushion at all**: the first year of that scenario takes operating income from
−$5.6M to roughly −$157M, the third year to about −$440M, and the cost base is 88% personnel and
distribution, which cannot be cut at the speed an installed base decays.

**Likelihood: a real possibility.** Not "likely" — the base has grown for ten consecutive years,
the OS cost advantage on memory is real and widening on the company's own account, and Hisense
and TCL were added as partners in 2025. Not "a low-level possibility" either: the two largest
retailers of Roku devices are the two companies most motivated to displace it, Walmart has
bought a competing OS and is already integrating it *"instead of other third-party proprietary
operating systems"*, and the filing says partner defection **has already happened**. **And [E4-40]
governs the read: model exposure, not experience.** Ten years of household growth is exactly the
benign history the corpus calls *"not only useless, but actually dangerous"* as a guide, and the
metric that would show the exposure turning into experience — the household count — **is the one
that was deleted.**

---

## Q5 — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

**Q1-Q4 did not all return IN. Q2 returned OUT. Nothing below is an entry finding, a
recommendation, or a ranking position; it exists because the queue's output contract requires a
price either way, and it carries no entry language.**

**THE PRICE.** ROKU **$154.93** at **2026-09-11** (aggregator close, flagged per operator rule
5). Shares **148,418,969** (both classes, from the 10-Q cover of 2026-08-06, accession
0001628280-26-054335). **Market capitalisation $22,996M.**

**THE SOVEREIGN.** **5.35%**, 30-year US Treasury par yield, **2026-09-11**, from the Treasury's
own daily par yield curve. Roku earns in USD; no FX.

**THE YIELD, on every construction.**

| owner-earnings construction | OE | yield on $22,996M | vs 5.35% sovereign |
|---|---|---|---|
| five-year 2021-2025, (c)=capex *(the screen's `oe_bottom`)* | −$150.7M | **−0.66%** | **−6.01 pts** |
| eleven filed years, (c)=D&A | −$91.9M | −0.40% | −5.75 pts |
| three-year 2023-2025, (c)=capex *(the screen's `oe_top`)* | −$81.4M | −0.35% | −5.70 pts |
| two-year 2024-2025, (c)=D&A | −$84.3M | −0.37% | −5.72 pts |
| FY2025 alone, (c)=D&A | +$60.6M | 0.26% | −5.09 pts |
| FY2025 alone, (c)=capex | +$124.3M | 0.54% | −4.81 pts |
| **TTM normalised for the tariff refund [E4-41], (c)=D&A** | **+$285.1M** | **1.24%** | **−4.11 pts** |
| **TTM normalised, (c)=capex** | **+$344.9M** | **1.50%** | **−3.85 pts** |
| TTM unnormalised, (c)=capex — *the most favourable construction that exists* | +$381.9M | **1.66%** | **−3.69 pts** |

**The screen's `yield_bottom −0.66%` and `vs_sovereign −6.01 pts` reproduce exactly.** And the
line that matters: **the single most favourable owner-earnings construction available anywhere in
the company's filed history yields 1.66% against a 5.35% government bond — 3.69 points BELOW the
risk-free rate.** There is no window, no (c) end and no normalisation that puts Roku above the
bond.

**WHAT THE PRICE ALREADY ASSUMES.** At the [E4-28] floor of ~10%, the price of $22,996M against
the best TTM owner earnings of $381.9M requires **8.34% growth in perpetuity** (0.10 − g =
381.9/22,996). To justify the price against the bare 5.35% sovereign requires **3.69% in
perpetuity**. What the business has actually done: revenue compounded 31.6% a year over ten
years, Platform revenue 18% in FY2025 and 25% in Q2 2026 — **and owner earnings compounded from
negative to negative across nine of ten years.** The growth that has to be assumed is growth in
owner earnings, and the owner-earnings series has no positive trend to extrapolate from, only a
single positive year. **[E4-35]** is the bound the case must face: fewer than 10 of the 200 most
profitable companies of 2000 attained 15% annual EPS growth over the following twenty years.

**WHAT YOU ARE PAID: −3.69 to −6.01 points over the sovereign.**

**THE FLOOR VERDICT, FIRST [E4-28].** Honest pre-tax expectancy at this price: **1.66% at the
most generous, 1.24% normalised, negative on the corpus's own five-year default window.**
*"That's the figure we quit on"* — and 1.66% is not within sight of 10%. **The name is quit on,
not ranked, and the ranking lines are therefore not filled in.**

**VALUE, AS A ROUND-NUMBER RANGE [E4-01].** On the five-year default window there is no positive
value to state: owner earnings are negative and a zero-growth capitalisation of a negative number
is not a value. On the normalised TTM, **capitalised at the [E4-28] floor: ~$2.9bn to ~$3.4bn, or
roughly $19 to $23 a share. Capitalised at the 5.35% sovereign: ~$5.3bn to ~$6.4bn, or roughly
$36 to $43 a share.** Against a price of **$154.93**. **No margin of safety is applied and none
is needed** — this is the **screamer test [E4-01]** and its middle outcome does not even arise:
the price is above the whole range, which is the third outcome, and the answer is no. **Windage
count: one** — conservatism is spent only in taking the normalised rather than the reported TTM,
and nowhere else; no per-name premium is in the rate **[E3-42]**.

**AND NOW THE FACT THAT MAKES THE WHOLE COMPUTATION A DIFFERENT ANIMAL, WHICH IS WHY IT IS
STATED LAST RATHER THAN USED AS A CONCLUSION.** The $154.93 quote is not a market opinion about
Roku's owner earnings. **Roku agreed on 2026-06-14 to be acquired by Fox Corporation for 0.9693
Fox Class A shares plus $96.00 in cash per Roku share.** At FOXA's 2026-09-11 close of $65.94
that is **$159.90 of consideration**, so ROKU at $154.93 trades at a **3.1% discount to the deal
— a merger spread on a transaction with a DOJ Second Request outstanding since 2026-09-08 and an
expected close in the first half of calendar 2027.** Total consideration is **$23,732M**, which
is **62.1x** the best TTM owner earnings, **56.4x** FY2025 Adjusted EBITDA, and **10.0x** TTM
gross profit. Whoever buys ROKU at $154.93 today is underwriting antitrust clearance and Fox's
share price, not Roku's home screen. **The framework has nothing to say about that trade** — it
is an arbitrage, the corpus's own *parking place* category **[E2-74]** rather than a business
purchase, and this framework values businesses.

---

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position exists and none is opened; Q2 closed the file. So this section is written as
[E1-02] requires — yardsticks established in advance — and as reversal conditions in words, per
the QLYS ruling of 2026-09-07. No alert band is armed and no `PORTFOLIO.md` row is added,
because a name that failed at Q2 failed on the BUSINESS and a price alert on it would be a
category error.**

**WHAT WOULD REOPEN THIS FILE.** Q2 failed on [E3-03] criterion (2) and on the withdrawal of
the series that measures it. Four conditions, each a document:

1. **The installed-base series is restored as an audited number in a 10-K or 10-Q** — a
   Streaming Households count on the withdrawn definition, with a comparative — **and it shows
   the base still compounding.** This is the necessary condition; without it the moat's
   direction [E4-32] cannot be read at all and the gate cannot be re-run on evidence. A
   promotional *"more than 100 million"* in a furnished exhibit does not satisfy it.
2. **ARPU is restored and rises for three consecutive years while the base is flat or growing.**
   Four years of flat ARPU is the absence of [E2-44]'s first characteristic; three years of real
   increases against a growing base would be evidence of it.
3. **A filed OEM disclosure showing Roku's share of new smart-TV shipments rising**, and no
   further partner defection of the kind the FY2025 risk factors already concede has happened.
4. **Owner earnings positive on a five-year mean at both (c) ends** — not one year, not a TTM,
   and with SBC subtracted in full [E5-06]. At the current rate that is not achievable before
   FY2029 arithmetic.

**WHAT WOULD CONFIRM THE OUT VERDICT** (the thesis-breaking metric, pre-committed): Walmart
completing the substitution of Vizio's operating system for third-party operating systems in
Onn products; Amazon or Google licensing terms taking a named existing Roku TV partner; or
Platform gross margin falling below 50% on a mix shift to lower-margin subscriptions. Platform
gross margin was **52.0% (FY2025) and 53.0% (Q2 2026)**; the Subscriptions half is already down
360 basis points year on year to **41.4%**, and Subscriptions is the faster-growing half.

**WHY NO PRICE BAND IS ARMED.** *"we sell — really when we reevaluat[e] the economic
characteristics of the business … And those beliefs change quite gradually"* **[E4-17]**. The
belief here was never formed, so there is nothing to change. **The catalyst date is a
transaction date, not a business date:** the DOJ Second Request of 2026-09-08 must be complied
with before the HSR waiting period restarts; the outside date is **2027-06-14**, extendable to
2027-12-14 and then to 2028-03-14; the special meetings follow the joint proxy mailed
2026-09-01. **If the merger closes, ROKU ceases to exist as a security and this file is
permanently closed by the delisting rather than by the framework.** If it breaks, the framework's
verdict stands on the business and the file stays closed at Q2 — and the $1,237,262,000
regulatory termination fee payable by Fox would then be 5.4% of Roku's current market
capitalisation arriving as cash, which is a fact about a break price and not a moat.

- **VERDICT: [x] OUT** — the file is closed at Q2 on the business; Q6 records the reversal
  conditions in words and arms nothing.

---

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → stop.** Q3 and Q4
      items are recorded with **no verdict written**; Q5 is headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on
      filed segment revenue, cost and gross profit for eleven years. The Q2 moat class is **NONE**,
      not PROVISIONAL, and the reason is stated: the verdict is OUT on filed facts from Roku's own
      risk factors plus a like-for-like competitor whose data ends in 2024, and **a peer-data gap
      cannot rescue a franchise claim that the subject's own filing contradicts.**
- [x] Every UNRESEARCHED verdict names the artifact: **there are none.** The one document that
      would change the Q2 reading is named at Q6 condition 1 and **it does not exist** — Roku
      chose not to file it, which makes the moat's direction UNKNOWABLE from documents while the
      franchise question itself is answerable OUT on what is filed.
- [x] Every UNKNOWABLE states what cannot be known: **the direction of the Streaming Household
      count after 2024-12-31**, stated at Q2. It is recorded as a defect in the evidence, not as
      the file's verdict.
- [x] Step 0: the filing was read, with accession numbers for eleven 10-Ks, one 10-Q, four 8-Ks
      and one DEF 14A; **five figures cross-checked to the dollar** (FY2025 OCF $483,718k, SBC
      $354,169k, D&A $68,904k, capex $5,280k, deferred revenue $(4,987)k), and the FY2022 flag
      reproduced to the dollar from the filed statement.
- [x] Owner earnings on a multi-year mean; **eight windows published [E4-38]**; the capex band
      disclosed as a judgment with the direction of the exception reversed and the reason given.
- [x] Competitor row filled; the one unavailable class (Samsung, LG — foreign private issuers
      filing nothing with the SEC) is named with its limit.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen — the **screamer test** — not both; **windage count: one.**
- [x] Prices dated; the aggregator is used for live quotes only and flagged.
- [x] `python tools/check_framework.py` run and **PASS** before the commit.
- [x] Run committed to git, by file name, after each gate.

## REGISTER
- **Verdict: [x] OUT (about the business).**
- **One line: Roku fails [E3-03] criterion (2) — its own risk factors name Amazon, Apple, Google
  and Walmart/Vizio as licensors of substitute television operating systems with greater
  resources that "can subsidize" them, concede that existing Roku TV partners have already
  defected, and disclose that four retailers who are 81% of Devices revenue have no long-term
  contract and two of them own competing operating systems — while ARPU was flat for four years
  as Vizio's rose 71%, streaming-player units fell three years running, and the Streaming
  Household count and ARPU were both deleted from the 10-K in the year that mattered.**
- **PASS/FAIL: FAIL at Q2 (OUT).** Price **$154.93** (2026-09-11), cap **$22,996M** on
  **148,418,969** shares from the 10-Q cover (accession 0001628280-26-054335), sovereign
  **5.35%** (US Treasury, 2026-09-11). Owner earnings **−$189M to +$382M** across eight windows
  and both (c) ends — **it STRADDLES ZERO**; best-ever yield **1.66%** against the bond,
  **−3.69 points**. **Pending acquisition by Fox Corporation at 0.9693 FOXA + $96.00 cash
  ($159.90 at FOXA's 2026-09-11 close); the quote is a 3.1% merger spread, not a business
  price.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a as a verdict. Recorded as an evidence defect: the Streaming Household
  count and ARPU for FY2025 and FY2026 do not exist in any filed document.
"""

# splice: replace everything from Q3 heading to end of file
start = t.index("## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?")
t = t[:start] + rest
open(p,'w',encoding='utf-8').write(t)
print('ok', len(t))
