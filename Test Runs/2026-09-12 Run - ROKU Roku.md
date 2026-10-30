# Company Run — Roku, Inc. (ROKU) — 2026-09-12
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
- rate **5.35 %** · date **2026-09-11** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity** (`tools/sources.py:sovereign('USD')`, which reads
  the Treasury XML directly; FRED DGS30 is the fallback and was not used)
- FX: none. Roku earns in USD; "most of our Platform revenue" and "most of our Devices
  revenue" are generated in the United States (FY2025 10-K, Item 7). ADR ratio: n/a.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, filed **2026-02-13**, period 2025-12-31, accession **0001628280-26-008114**
  - **10-Q Q2 FY2026**, filed **2026-08-06**, period 2026-06-30, accession **0001628280-26-054335**
  - **8-K + EX-99.1 Shareholder Letter**, filed **2026-08-06**, accession **0001628280-26-054321**
  - **8-K Item 1.01, the merger agreement**, event 2026-06-14, filed 2026-06-15, accession **0001140361-26-025115**
  - **8-K Item 8.01, DOJ Second Request**, event 2026-09-08, filed 2026-09-09, accession **0001140361-26-035990**
  - **8-K EX-99.1, recast segments**, filed **2026-06-18**, accession **0001628280-26-044373**
  - 10-K FY2024 (0001428439-25-000013), FY2023 (0001428439-24-000011), FY2022
    (0001428439-23-000007), FY2021 (0001428439-22-000010), FY2020 (0001564590-21-009021),
    FY2019 (0001564590-20-007916), FY2018 (0001564590-19-005829), FY2017 (0001564590-18-004134)
- figure cross-checked against the filed statement: **FY2025 net cash provided by operating
  activities $483,718 thousand**, read off the Consolidated Statements of Cash Flows in the
  FY2025 10-K, agrees to the dollar with `us-gaap:NetCashProvidedByUsedInOperatingActivities`.
  Also cross-checked to the dollar: SBC **$354,169**, D&A **$68,904**, purchases of property
  and equipment **$5,280**, and the deferred-revenue line **$(4,987)**.

### THE SHARE COUNT, AND THE TWO CLASSES — read off the cover, then judged

`python Screens/cover_shares.py ROKU` off the cover of the 10-Q filed 2026-08-06
(accession 0001628280-26-054335), as-of the filing date:

| class | count |
|---|---|
| Class A Common Stock | 132,050,905 |
| Class B Common Stock | 16,368,064 |
| arithmetic sum | 148,418,969 |

**The tool refuses to sum them; the judgment is mine, and it is made from documents, not
arithmetic.** Two documents settle it in the same direction:

1. **The merger agreement treats the two classes identically.** 8-K of 2026-06-15: *"each
   share of Class A Common Stock … and Class B Common Stock … will be converted into the
   right to receive (i) 0.9693 … shares of Class A Common Stock … of Parent … and (ii)
   $96.00 in cash"* — one Merger Consideration, no class differential, and the vote is
   *"holders of a majority of the shares of Class A Common Stock and Class B Common Stock …
   voting together as a single class."*
2. **The voting arithmetic reconciles only if Class B carries ten votes and the founder holds
   essentially all of it.** 132,050,905 × 1 + 16,368,064 × 10 = 295,731,545 votes, of which
   the Class B is **55.3%**; the 8-K states the Wood-affiliated Voting and Support Agreement
   stockholders *"collectively held approximately 55% of Company's outstanding voting power."*
   The counts and the disclosure agree.

**DECISION: the two classes are economically equivalent and are summed. Shares =
148,418,969.** Class B is a **voting** instrument, not an economic one. Its economic
irrelevance and its governance relevance are separate findings and the second is carried to
Q3.

- **price $154.93, 2026-09-11** (aggregator — Yahoo chart `close`, flagged per operator rule 5)
- **market cap = 148,418,969 × $154.93 = $22,996M.** The queue's row said `cap_m 22995`.
  **The queue's cap is right** — the first time in this session's tier that it has been. It is
  right because it summed the classes, which is the answer this run reached independently from
  the charter and the merger agreement rather than by assumption.

### ⚠️ THE FACT THAT GOVERNS THIS ENTIRE FILE, AND IT IS NOT IN THE BRIEF OR THE QUEUE

**Roku signed a definitive agreement to be acquired by Fox Corporation on 2026-06-14**
(8-K accession 0001140361-26-025115). The consideration per Roku share, Class A and Class B
alike, is **0.9693 Fox Class A shares plus $96.00 in cash**. Roku stockholders are expected
to own **~27% of the combined company**. The board approved it unanimously; the founder and
his affiliates, holding ~55% of the voting power, have signed a Voting and Support Agreement.
The S-4 was declared effective **2026-09-01** and the definitive joint proxy mailed the same
day. **On 2026-09-08 the DOJ issued a Second Request** to both parties (8-K accession
0001140361-26-035990); Roku *"expects the Mergers to be consummated by the first half of
calendar year 2027."* Termination fees: **$866,084,000** payable by Roku, **$1,237,262,000**
payable by Fox on a regulatory failure. Outside date **2027-06-14**, extendable to
2027-12-14 and then 2028-03-14.

**What this does to the questions.** It does not excuse a single gate — the business gates
Q1-Q4 are about the business and are run in order on the filings, exactly as written. What it
does is **change what the quoted price is**. At the 2026-09-11 close of FOXA ($65.94) the
merger consideration is $96.00 + 0.9693 × $65.94 = **$159.90**, and ROKU trades at $154.93 —
a **3.1% discount**, i.e. the market is pricing a deal spread, not an owner-earnings yield.
A "price and pass/fail" line for this name that did not say so would be misleading, and the
queue's output contract is discharged with the fact attached.

## THE SCREEN ROW — EVERY NUMBER REPRODUCED FROM THE FILED STATEMENTS, AND WHAT EACH ONE MEANS

*Operator rule 8: a flag is a prompt to read, never a score. All seven reproduce; four of the
seven are arithmetically right and diagnostically misleading, and the reasons differ.*

**The series the screen reads is `NetCashProvidedByUsedInOperatingActivities` from the 10-Ks,
last nine years** — FY2017 through FY2025: 37,292 · 13,922 · 13,707 · 148,192 · 228,081 ·
11,795 · 255,856 · 218,045 · 483,718 (all $k, all cross-checked against the filed cash-flow
statements).

| screen output | reproduced? | what it actually means |
|---|---|---|
| `cap_m 22995` | **yes — $22,996M** | Correct, and correct **because it summed the two share classes**, which is the judgment this run made independently from the charter and the merger agreement (Step 0). Eight runs have found the queue's cap wrong; this is not one of them. |
| `oe_bottom_m −151` | **yes — −$150,725k** | The **five-year 2021-2025** mean at the capex end. |
| `oe_top_m −81` | **yes — −$81,434k** | The **three-year 2023-2025** mean at the capex end. **These are two different WINDOWS, not two ends of a capex band** — the INTC defect of 2026-09-07 repeating. The real capex band inside the five-year window is $272k wide. |
| `yield_bottom −0.66%` · `vs_sovereign −6.01 pts` | **yes** | −150,725 ÷ 22,996,000 = −0.66%, against 5.35%. |
| `growth_required: n/a — negative bottom` | **yes** | Correct and honest. |
| `level_shift 4.23 "STEP UP"` | **yes — 4.228** | mean(2023-2025) $319,206k ÷ mean(2017-2022) $75,498k. **The step is real and it is in the wrong series.** Operating cash flow adds SBC back; the last three years' operating cash averages 4.23x the prior six **because gross profit grew while $1.1bn of the cost of earning it was paid in stock.** |
| `level_shift_oe n/a "EARLY HALF STRADDLES ZERO (from −$509.8M)"` | **yes** | The owner-earnings series' early half runs from **−$509,832k (FY2022)** upward across zero, so the function refuses the ratio. Correct refusal. |
| `flags_disagree: FIRES` | **yes** | `ls[0]` is 4.23 and `ls_oe[0]` is None. **This disagreement is the whole file in one boolean: operating cash stepped up 4.2x and owner earnings did not step at all, because the entire step sits inside the stock-compensation add-back.** The PLPC run of 2026-09-07 added this flag for exactly this case, and Roku is the sharpest instance of it in the queue. |
| `window_disagree: FIRES` | **yes** | The nine-year window begins at FY2017 and **excludes FY2016's negative operating cash of −$32,463k**; on the full filed series the ratio is refused. The LRCX diagnosis applies verbatim: *the nine-year window's "earlier half" already contains part of the current wave.* |
| `best_year_dep 0.261 "ONE YEAR CARRIES THE WINDOW"` | **yes — 0.2608** | Drop FY2025 and the nine-year operating-cash mean falls from **$156,734k to $115,861k, −26.1%.** One year of nine carries a quarter of the mean, and it is the most recent one. |
| `wc_note: FIRES — the CONTRACT-LIABILITY line moved by 351% of a year's operating cash` | **yes — 351.0%** | Decoded in full below. **It is the largest reading in the 361-name queue and it is a denominator artifact that names the smallest of the three working-capital movements in the statement.** |
| `newest_filing 2025-12-31` · `newest_periodic 2026-06-30` | **yes** | Both read. **And neither the row nor the brief carries the fact that the company signed a definitive agreement to be acquired on 2026-06-14** — recorded at Step 0. |

**The honest summary of the row: the queue's cap is right, its two owner-earnings numbers are
right and are two different windows, and every one of its four flags fires for a true reason
and points at the wrong thing.** The screen's `level_shift` sees a business improving 4.2x; the
business's owner earnings have not improved at all, because the improvement is the SBC add-back.
The screen's `wc_note` sees a 351% working-capital swing; the swing it names is $41.4M and the
one it cannot see is $313.2M.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Roku gives away, or sells below
cost, the software that runs a television set, and then rents the first screen the viewer
sees. Three revenue engines sit on top of that screen and all three are filed separately:
**advertising** ($2,327.8M in FY2025) sold against the home screen itself and against the
ad-supported content in Roku's own free channel; **subscriptions** ($1,817.1M) — a cut of
every streaming service a viewer signs up to through Roku's billing, plus Roku's own paid
services and the paid buttons on the remote control; and **devices** ($592.4M), the sticks and
Roku-branded TVs that carry the software into the house. The cost of the first two is content
and bought ad inventory; the cost of the third is a contract manufacturer's invoice. Nothing in
that chain requires a model to describe.

**The trade is stated, quantified and one-directional — and it answers the brief's question.**

| FY | Devices / Player revenue | Devices gross profit (loss) | Platform gross profit | **Platform as % of total gross profit** |
|---|---|---|---|---|
| 2015 | $270.0M | **+$48.6M** | $41.2M | 45.9% |
| 2016 | $293.9M | **+$44.1M** | $76.9M | 63.6% |
| 2017 | $287.4M | **+$29.3M** | $170.5M | 85.3% |
| 2018 | $325.6M | **+$35.8M** | $296.3M | 89.2% |
| 2019 | $388.1M | **+$17.1M** | $478.1M | 96.5% |
| 2020 | $510.6M | **+$43.7M** | $764.6M | 94.6% |
| 2021 | $499.7M | **−$37.8M** | $1,446.4M | 102.7% |
| 2022 | $415.1M | **−$90.6M** | $1,531.8M | 106.3% |
| 2023 | $490.5M | **−$43.9M** | $1,566.6M | 102.9% |
| 2024 | $590.1M | **−$80.3M** | $1,886.0M | 104.4% |
| **2025** | **$592.4M** | **−$82.0M** | **$2,156.4M** | **104.0%** |

*Sources: FY2025 10-K Item 7 (2025/2024); 8-K EX-99.1 of 2026-06-18 recast segment note
(2023); FY2022 10-K Item 7 (2022 and restated 2021); FY2021, FY2019 and FY2017 10-K Item 7.
FY2021 appears twice in the record because the FY2022 10-K reclassified Player into Devices
and moved ~$20M of revenue between segments; the restated figures are used.*

**So: the Platform half is 104.0% of consolidated gross profit and the Devices half is −4.0%.
Devices has produced a gross LOSS in every one of the last five years, cumulatively −$334.6M.**
**Is Devices a customer-acquisition cost recognised as revenue? Yes, and the filing says so in
its own words:** *"We expect to continue to manage the average selling prices of Roku streaming
devices in an effort to sell more devices, which we believe will increase our Streaming
Households. We expect that this trade off from Devices gross profit or loss to grow Streaming
Households should result in increased Platform revenue and Platform gross profit over time"*
(FY2025 10-K, Item 7, Overview). A negative-gross-margin product sold to acquire a user is a
marketing expense wearing a revenue line's clothes, and $592.4M of revenue and $674.4M of cost
both inflate the top and bottom of the income statement without adding a dollar of gross profit.
**The AMAT lesson holds: the segment split kills a claim the consolidated numbers supported.**
Consolidated FY2025 gross margin is 44%; the business that actually earns money runs at 52.0%
(Platform), and the 44% is the blend of a 52% franchise candidate with a −13.8%-margin
distribution expense.

**And one correction to the brief's framing.** The brief calls Devices "players and TVs,
historically sold at or below cost." The Q2 2026 shareholder letter shows the more important
half: *"our Devices revenue is generated from the sale of our players and Roku-made TVs and
does not include Roku TV models made and sold by our OEM licensing partners, **which account
for the largest portion of our overall unit volume**."* Most of the installed base arrives
through licensees at **no device cost to Roku at all**; the licence fee lands in Platform. The
Devices gross loss is therefore not the whole acquisition cost, and not even the main channel —
it is the cost of the minority of units Roku sells itself. The other side of that is in Sales
and marketing: *"we continue to anticipate distribution costs for Roku TV model sales, which
represent a significant component of Sales & Marketing (S&M) expense"* — so a second slice of
the customer-acquisition cost sits in opex, not in cost of revenue.

**The scarce input this business controls: the default home screen of a television set that is
already installed in a living room** — the position a viewer passes through before deciding
what to watch. The company's own claim for it, Q2 2026 letter: *"The Roku Home Screen is one of
the most valuable pieces of real estate in TV. In the U.S. alone, it is used by more than half
of broadband households, reaching them before they decide what to watch."* Whether that
position is defensible against the people who make the television sets is **Q2's question, not
Q1's**, and it is not answered here.

**Will the fundamentals look broadly the same in ten years?** The *mechanism* will: somebody
will sell the advertising and the subscription revenue-share attached to the first screen of a
connected television, and that revenue will be households × monetisation-per-household less
content and inventory cost. That is a legible, stable unit economics. **Two things are recorded
against the question rather than resolved by it.** First, the identity of the owner: after the
Fox merger the ten-year cash flows belong to Fox Corporation and Roku is 27% of it — that is a
Q5/Q6 fact, recorded, not used here. Second, the *stability of character* test in [E3-31]
(*"relatively simple and stable in character"*) is passed on the revenue mechanism and is
**stressed** by the content-cost side, where $223.2M of content was amortised in FY2025 against
$184.5M of net new content investment — a cost line that is a discretionary programming
decision, not a manufacturing input. That does not make the business unintelligible; it makes
(c) hard, which is Q4's problem and is handled there.

**Most names should end here [E5-13]. This one does not.** I can write the unit economics from
the filed statements without using a single word of management's vocabulary, name the scarce
input in one sentence, and state the arithmetic that turns it into cash.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### FIRST, THE BULL CASE, BUILT AS WELL AS ITS HOLDERS WOULD BUILD IT [E4-51]

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition"* **[E4-51]**. So the installed-base case first,
on filed facts and nothing else.

Roku is the **default operating system of the American living-room television**, and the
position is scarce because a television set has exactly one home screen. The company's claim,
Q2 2026 shareholder letter: *"The Roku Home Screen is one of the most valuable pieces of real
estate in TV. In the U.S. alone, it is used by **more than half of broadband households**,
reaching them before they decide what to watch."* Four filed facts support the case:

1. **The base is enormous and it grew every single year on the filed series.** Active Accounts
   / Streaming Households: 13.4M (2016) → 19.3 → 27.1 → 36.9 → 51.2 → 60.1 → 70.0 → 80.0 →
   **89.8M (2024)**. Ten consecutive years of growth, never a down year, +570% over eight.
2. **Engagement grew faster than the base.** Streaming Hours: 14.8bn (2017) → 24.0 → 40.3 →
   58.7 → 73.2 → 87.4 → 106.0 → 127.1 → **145.6bn (2025)**. Hours per household per year rose
   from 906 (2017) to 1,498 (2024) — from 2.5 to 4.1 hours a day. The base is not just large;
   it is deepening.
3. **The economics of the position are genuinely franchise-shaped where they are visible.**
   Advertising gross margin **62.4%** in Q2 2026, up 6.5 points year on year, on revenue
   growing 25%. Advertising gross profit grew **39%** on 25% revenue growth — operating
   leverage inside the ad business, not price competition.
4. **The OS has a real, filed cost advantage over the alternatives, which is the one claim in
   the bull case that is a moat claim rather than a scale claim.** Q2 2026 letter: *"the Roku TV
   OS requires significantly less dynamic memory (DRAM) and storage memory (Flash) than
   competing platforms, and this **widening cost advantage** is drawing more TV brands to
   Roku."* A cheaper OS wins the low-end TV shelf, and Roku's OEM partners now include **Hisense
   and TCL** — two of the largest low-cost TV makers in the world.

**That is the case, and criteria (1) and (3) of [E3-03] pass on it.** The service is plainly
desired — 145.6 billion hours a year is not a product people tolerate. And it is **not subject
to price regulation**: Roku sets its own ad prices and its own subscription revenue shares, and
the FY2025 10-K's Government Regulation section names privacy, content quotas and trade
restrictions — never rate regulation.

### THEN THE ATTACK — AND FIRST THE UNITS, BECAUSE THAT IS WHERE THE FRANCHISE IS MEASURED [E4-55]

*"Where units exist, monitor units"* **[E4-55]**: Precision Steel's pounds fell 69M → 46M while
price rises held dollar revenue level — *"a serious reverse, not likely to disappear in some
'bounce back' effect."* **Roku has published three physical/price series, and I ran the
decomposition the PINS run ran. It comes out differently, and worse.**

| FY | Streaming Households / Active Accounts, EOY (M) | filed **ARPU** | Streaming Hours (bn) | hours per household per year | Platform revenue ($M) |
|---|---|---|---|---|---|
| 2016 | 13.4 | — | — | — | 104.7 |
| 2017 | 19.3 | **$13.78** | 14.8 | 906 | 225.4 |
| 2018 | 27.1 | **$17.95** | 24.0 | 1,035 | 416.9 |
| 2019 | 36.9 | **$23.14** | 40.3 | 1,259 | 740.8 |
| 2020 | 51.2 | **$28.76** | 58.7 | 1,332 | 1,267.7 |
| 2021 | 60.1 | **$41.03** | 73.2 | 1,316 | 2,264.9 |
| 2022 | 70.0 | **$41.68** | 87.4 | 1,343 | 2,711.4 |
| 2023 | 80.0 | **$39.92** | 106.0 | 1,413 | 2,994.1 |
| 2024 | 89.8 | **$41.49** | 127.1 | 1,498 | 3,522.8 |
| **2025** | **NOT DISCLOSED — "more than 90 million"** | **NOT DISCLOSED** | 145.6 | **cannot be computed** | 4,144.9 |

*Households and ARPU: FY2017-FY2024 10-K Item 7 Key Performance Metrics, each year's own
filing. Hours: same. Platform revenue: Item 7 net revenue tables, restated figures where a
segment reclassification occurred. The FY2025 10-K (accession 0001628280-26-008114) contains
**no Streaming Households figure and no ARPU figure anywhere in the document**; the words
"more than 90 million Streaming Households globally" appear in Item 1, and ARPU survives only
twice — once in the defined-terms glossary as an orphaned definition, and once in a sentence
saying Streaming Hours "does not correlate to … ARPU." Both times without a value.*

**THE DECOMPOSITION, AND IT IS NOT THE PINS SHAPE — IT IS THE INVERSE, WHICH IS WORSE FOR THE
MOAT CLAIM.** The PINS run found ARPU rising 46% while the money segment's users fell: price
carrying a shrinking franchise. At Roku, **price did nothing for four years while units did all
the work.** ARPU was $41.03 at the end of 2021 and $41.49 at the end of 2024 — **+1.1% over
three years**, against US CPI over the same period. Platform revenue rose 55.5% across those
three years and **essentially all of it came from adding 29.7 million households, not from
monetising the ones already there.** A franchise is supposed to be able to *"raise prices
even when product demand is flat and capacity is not fully utilized"* **[E2-44]**; Roku could
not raise the revenue it earns per household at all while demand was growing 15% a year. Four
years of flat ARPU across a period of 50% base growth is the **absence** of [E2-44]'s first
characteristic, measured on the company's own metric, and the company's own explanation is that
the mix is diluting it: *"an increasing share of Streaming Households in international markets
where we are currently focused more on scale and engagement than monetization"* (FY2024 10-K).

**AND THE UNIT SERIES THAT MATTERS MOST WAS DECLINING WHILE THE HOUSEHOLD COUNT ROSE.**
From the Devices MD&A of each 10-K, verbatim on the units:

| FY | the filed unit statement | the basis |
|---|---|---|
| 2021 | *"volume of streaming players sold **decreased by 4%**"* | streaming players |
| 2022 | *"volume of streaming players sold **decreased by 14%**"* | streaming players |
| 2023 | *"volume of streaming players sold **decreased by 8%**"* | streaming players |
| **2024** | *"volume of **all devices shipped** increased by 5%"*, ASP +18% | **basis changed** |
| 2025 | *"volume of all devices shipped **decreased by 3%**"*, ASP +6% | all devices |

**Three consecutive years of falling streaming-player units — roughly −24% cumulatively — with
average selling prices moving to hold dollar revenue roughly level. That is the Precision Steel
shape exactly [E4-55]. And in the fourth year the unit basis was widened from "streaming
players" to "all devices shipped", which folded in the newly launched Roku-made TVs and turned
the sign positive.** I do not have to allege intent, and [E2-30] says I should not —
*"institutional dynamics, not venality or stupidity"*. The reading stands on the record: the
honest physical series was falling, and it was replaced.

### THE YARDSTICKS WERE DISCARDED — [E2-49], AND IT IS THE STRONGEST SINGLE DISCLOSURE FINDING IN THE FILE

*"Yardsticks seldom are discarded while yielding favorable readings. But when results
deteriorate, most managers favor **disposition of the yardstick rather than disposition of the
manager**"* — demand *"pre-set, long-lived and small bullseyes"* **[E2-49]**. The operational
form is to compare the headline metric across successive filings. **Roku's headline metric set
changed in each of the last three annual reports.**

| filing | the Key Performance Metrics, verbatim from Item 7 |
|---|---|
| **10-K FY2023** (2024-02-16) | *"gross profit, Active Accounts, Streaming Hours, and ARPU"* |
| **10-K FY2024** (2025-02-14) | *"Streaming Households, Streaming Hours, ARPU, and Free Cash Flow"* |
| **10-K FY2025** (2026-02-13) | *"Streaming Hours, Platform revenue, **Adjusted Earnings Before Interest, Taxes, Depreciation and Amortization ("Adjusted EBITDA")**, and Free Cash Flow"* |

Four changes, and each one followed a deteriorating reading:

1. **Gross profit was dropped as a KPM in the FY2024 filing.** Consolidated gross margin had
   gone 50.9% (2021) → 46.1% (2022) → **43.7% (2023)**, and FY2023 gross profit grew 5.7%, the
   slowest year in the company's filed history. The yardstick was removed in the next annual
   report.
2. **"Active Accounts" was renamed "Streaming Households"** in the FY2024 filing, the same year
   the *player* unit basis changed.
3. **Streaming Households and ARPU were both deleted** in the FY2025 filing — the base count
   and the price. Net household additions had run 14.3M (2020), 8.9M, 9.9M, 10.0M, **9.8M
   (2024)**, i.e. a growth rate of 39% → 17% → 16% → 14% → **12%**, decelerating every single
   year; and ARPU had been flat for four.
4. **Adjusted EBITDA was promoted INTO the primary metric set** — which is the fifth flag
   **[E4-29]** and is dealt with at Q3.

**One thing must be said on the other side, because [E2-49] itself distinguishes the cases.**
The rule says a switch that *follows* deterioration fires, while *"one announced ahead with
reasons … is the candor case."* Roku announced this one at the time it took effect and gave a
reason: *"starting in the first quarter of 2025, we have updated our Key Performance Metrics to
better align with these priorities … we are now primarily focused on growing Platform revenue
and profitability."* That is a reason, it is a true one, and it is not concealment. **It is
still a disposition of the yardstick**, because what replaced two auditable unit-and-price
series was a revenue line and a non-GAAP profit measure, and because the reason given does not
require deleting the household count — a company primarily focused on Platform revenue has more
reason to publish the household base, not less, since Platform revenue is the product of the two
deleted numbers.

**What the replacement costs the analyst, stated precisely, because this is the point.** The
entire bull case above is an installed-base case. The FY2025 words *"more than 90 million"* are
consistent with **90.1 million** — household growth having stopped dead at +0.3% — and equally
with 99 million. Inverting the company's own published ARPU formula (*"Platform revenue for the
trailing four quarters divided by the average of the number of Streaming Households at the end
of the current period and the end of the corresponding period in the prior year"*), FY2025
Platform revenue of $4,144.9M implies ARPU of **$46.11 if households were 90M** and **$44.14 if
they were 98M**. So the withdrawal did not conceal a falling ARPU — ARPU rose 6-11% in FY2025.
**It concealed the one number that decides whether the moat is widening or has stopped
widening**, in the year that number stopped being flattering. *"Direction outranks existence"*
**[E4-32]** is *"the primary criterion of a great business"*, and **the direction of the scarce
asset is now unmeasurable from the filings.** The Q2 2026 letter offers *"more than 100 million
households worldwide choose Roku"* — a marketing sentence in a furnished exhibit, not a series,
not on the withdrawn definition, and not auditable.

**The brief's prior fires.** The [E2-49] prior has fired at SHOP, MRVL, PAY, ARM, CALX and BE
and failed at QLYS, CRM, CORT, PLTR and INOD. **At Roku it fires on all three series at once**,
which is the first time in this queue that a company's entire unit-and-price disclosure set has
gone in a single filing.

### THE SEGMENT STRUCTURE CHANGED TWICE AS WELL

Not a metric switch, but the same reading problem, and it is recorded because it is what made
the Q1 table hard to build. **FY2022:** the "Player" segment was renamed "Devices" and roughly
$20M of FY2021 revenue was reclassified between the two segments (FY2021 Platform revenue
restated from $2,284.9M to $2,264.9M; Player gross loss restated from −$52.4M to −$37.8M).
**Q1 2026:** the Platform segment was split into **Advertising** and **Subscriptions**, three
reportable segments replacing two, with the FY2025 10-K's Items 1, 7 and 8 re-issued on
2026-06-18 (accession 0001628280-26-044373) to recast them. The 2026 change is a **candor
event, not a flag**: it *adds* disclosure — Advertising and Subscriptions gross profit are now
filed separately, which is how the 62.4% advertising margin in the bull case above became
visible at all — and the auditor dual-dated its report for it (*"February 13, 2026, (June 18,
2026, as to the change in the composition of reportable segments…)"*). Read beside the metric
deletions it makes a plain point: **this company is perfectly capable of disclosing more when it
wants to.** The three deletions were choices, not oversights.

### THE COMPETITOR ROW — REQUIRED **[E3-28]**, AND THE ONE LIKE-FOR-LIKE FILER IS DEAD

*"I can't be an intelligent owner of a business unless I know what all the other businesses in
that industry are doing"* **[E3-28]**. A moat is a claim about *relative* position and cannot be
evidenced from one company's numbers. **Eleven competitors were taken** — Buffett says eight —
and the full working row with every accession number, quotation and derived-versus-filed label
is `Test Runs/_research 2026-09-12 ROKU/competitor_row.md`. Same metric, same window (calendar
2025 unless the row says otherwise), filing-sourced throughout.

| peer | what it is to Roku | document | revenue, same-ish window | **OS installed base filed?** | **OS/CTV revenue filed separately?** | **OS/CTV gross profit filed?** |
|---|---|---|---|---|---|---|
| **ROKU** | subject | 10-K 0001628280-26-008114 | **$4,737M** | **NO — dropped; "more than 90 million"** | **YES — Platform $4,145M** | **YES — $2,156M** |
| **Vizio Holding Corp** | the only true comparable — **DEAD AS A FILER** | 10-Q 0001835591-24-000089 (9M to 2024-09-30); 10-K 0001835591-24-000011 (FY2023) | $1,235.9M (9M-2024) | **YES — 19.1M SmartCast accounts** | **YES — Platform+ $526.0M (9M)** | **YES — $302.7M (9M)** |
| **Amazon** | Fire TV | 10-K 0001018724-26-000004 | $716,924M (**151x**) | **NO** | **NO** — "Advertising services" $68,635M, all surfaces | **NO** |
| **Alphabet** | Google TV / Android TV, and YouTube | 10-K 0001652044-26-000018 | $402,836M (**85x**) | **NO** | **PARTLY** — YouTube ads $40,367M, no CTV split; Google TV inside "subscriptions, platforms and devices" $48,030M | **NO** |
| **Apple** | tvOS | 10-K 0000320193-25-000079 (FYE 2025-09-27) | $416,161M (**88x**) | **NO** | **NO** — the box sits in "Wearables, Home and Accessories" $35,686M | **NO** — only Products 36.8% / Services 75.4% |
| **Samsung Electronics** | Tizen | **NO SEC FILING EXISTS — EVER** | not obtainable | **NOT OBTAINABLE** | **NOT OBTAINABLE** | **NOT OBTAINABLE** |
| **LG Electronics** | webOS | **NO SEC FILING SINCE 2008-01-29** | not obtainable | **NOT OBTAINABLE** | **NOT OBTAINABLE** | **NOT OBTAINABLE** |
| **Netflix** | ad-supported streaming | 10-K 0001065280-26-000034 | $45,183M (**9.5x**) | **NO — has stopped filing membership counts entirely** | **NO ad-revenue figure at all** | **NO** — 29.5% operating margin filed |
| **The Trade Desk** | the CTV demand side | 10-K 0001671933-26-000014 | $2,896M (**0.61x**) | n/a — but **>95% client retention for over a decade**, filed | **NO CTV split**; gross spend **$13,395M** filed | **NO gross-profit line at all** |
| **Comcast** | distribution, **plus Xumo (consolidated)** | 10-K 0001628280-26-004994 | $123,707M (**26x**) | video customers **11,270k, −1,253k** | advertising **$3,712M, −9.2%**; Xumo unsized | **NO** |
| **Charter** | distribution, **plus Xumo (50%)** | 10-K 0001091667-26-000017 | $54,774M (**11.6x**) | video customers **12,605k, −287k** | advertising **$1,468M, −17.6%**; Xumo unsized | **NO** |
| **Walmart** | owner of Vizio / SmartCast | 10-K 0000104169-26-000055 (FYE 2026-01-31) | $713,163M (**151x**) | **NO** | **NO** — three Vizio mentions, none an operating metric | **NO** |

**Peers named: 11 of the industry's 11 real competitors in the two arenas Roku occupies** — six
TV operating systems (Fire TV, Google TV/Android TV, tvOS, Tizen, webOS, SmartCast) plus the
seventh the brief did not name and this row found, **Xumo**, plus the advertising counterparties
(Netflix, The Trade Desk) and the distribution leg (Comcast, Charter) and Vizio's acquirer.

**Limits, named as [E3-28] requires:**
1. **Samsung and LG are structurally invisible to this evidence base.** Checked, not assumed:
   the complete EDGAR company-name index was searched. Samsung Electronics Co Ltd (CIK
   0000879316) has **never filed a 10-K or 20-F** — its ~35 indexed filings are Schedules
   13D/13G and tender-offer papers it filed as a *holder* in other people's securities, and its
   last filing of any kind was **2015-01-20**. LG Electronics Inc (CIK 0000930445) last filed
   **2008-01-29**. Both trade on the KRX with unsponsored OTC ADRs and owe no Exchange Act
   periodic reports. **This is UNKNOWABLE-from-SEC, not UNRESEARCHED — I cannot name the
   document, because on this project's citation path it does not exist.**
2. **The only like-for-like filer died.** Vizio Holding Corp filed its last 10-Q on 2024-11-06,
   closed into Walmart on 2024-12-03, and deregistered on 2024-12-13 (Form 15-12G, accession
   0001193125-24-277647). Its data is fifteen months stale at Roku's FY2025 balance-sheet date,
   and its acquirer discloses nothing: **three Vizio mentions in Walmart's FY2026 10-K — a $1.9bn
   purchase price, the goodwill's segment, and an FTC consent decree running to 2037 — and zero
   occurrences of "SmartCast", "connected TV" or "operating system".**
3. **Amazon, Alphabet and Apple file no OS installed base, no OS revenue and no OS gross
   profit.** So no relative *margin* claim can be made against them. What IS filed is the
   asymmetry of resources, and it is quantified below.
4. **Gross margin is derived, not filed, for Amazon, Alphabet, Netflix and The Trade Desk.**
   Only Roku, Apple and Vizio publish a gross-profit subtotal.
5. **Window mismatches, not smoothed:** Apple −15 weeks, Walmart +1 month, Vizio −15 months.

---

### WHAT THE ROW ACTUALLY SAYS, AND IT IS FOUR THINGS

**ONE — THE ONE COMPETITOR THAT PUBLISHED THE SAME METRICS RAISED ITS PRICE 71% WHILE ROKU'S
STOOD STILL. This is the whole point of [E3-28] and no single-company analysis could reach it.**

| | SmartCast / Streaming Household **ARPU** | accounts / households |
|---|---|---|
| **Vizio** FY2021 | **$21.68** | 15.1M |
| **Vizio** FY2022 | **$28.30** | 17.4M |
| **Vizio** FY2023 | **$32.48** | 18.5M |
| **Vizio** Q3-2024 (last ever filed) | **$37.17** — *"up 18%"* | 19.1M — *"up 7%"* |
| **Roku** FY2021 | **$41.03** | 60.1M |
| **Roku** FY2024 | **$41.49** | 89.8M |
| **Roku** FY2025 | **withdrawn** | **withdrawn** |

**Vizio's monetisation per account rose 71.5% over the three years in which Roku's rose 1.1%,
from one-fifth the account base and one-fifth the platform revenue.** The definitions are not
identical and the differences are stated rather than smoothed: Vizio's unit is a **television
set**, Roku's is a **household**; Vizio's denominator excluded *"approximately 2.5 million
televisions connected to the internet through our legacy operating system"*; both divide by a
two-point average, so the formulas are the same shape. **The direction is not a definitional
artifact. Roku's flat ARPU is not an industry condition — the industry's smallest, weakest and
least-scaled participant was raising its take 18% a year while the scale leader could not raise
its take at all.** [E2-44]'s first characteristic is absent from Roku and present at Vizio.

**TWO — AND SCALE BOUGHT ROKU NO MARGIN ADVANTAGE EITHER, in the one business that is supposed
to be the franchise.**

| | platform gross margin |
|---|---|
| **Vizio** Platform+ FY2021 | **68.2%** |
| **Vizio** Platform+ FY2023 | **61.0%** |
| **Vizio** Platform+ 9M-2024 | **57.5%** |
| **Roku** Platform FY2023 | **52.3%** |
| **Roku** Platform FY2025 | **52.0%** |
| **Roku** Advertising only, FY2025 | **57.8%** |
| **Roku** Advertising only, Q2 2026 | **62.4%** |

Read fairly, because the mix differs: Vizio's Platform+ was **~80% advertising** (Q3-2024
advertising $161.0M of $197.0M) while Roku's Platform is **56% advertising / 44% subscriptions**,
and subscriptions carry a 41-45% margin. So the honest like-for-like is Roku's **advertising**
margin against Vizio's Platform+ margin: **57.8% (FY2025) against 57.5% (9M-2024) — they are
indistinguishable.** **Roku out-scales Vizio roughly 5:1 in platform revenue and earns the same
advertising gross margin.** Where a moat exists, scale shows up in price or in margin. Here it
shows up in neither.

**THREE — THE DEVICE GROSS LOSS IS AN INDUSTRY CONDITION, NOT A ROKU CHOICE, AND THAT IS WORSE
FOR THE MOAT, NOT BETTER.** Vizio's Device gross profit went **+$115.7M (FY2021) → +$16.0M
(FY2022) → −$8.6M (FY2023) → −$13.1M (9M-2024)** — the identical crossing Roku's made in the
identical years, and Vizio's platform was 106.1% of its total gross profit against Roku's 104.0%.
**Two independent filers, the same two-segment shape, the same sign flip, the same years.** That
is **[E2-27]** exactly: *"Viewed individually, each company's capital investment decision appeared
cost-effective and rational; viewed collectively, the decisions neutralized each other and were
irrational … After each round of investment, all the players had more money in the game and
returns remained anemic."* Every participant subsidises hardware to buy households, and Roku's
own filing says the larger ones *"can subsidize the cost of their streaming devices or licensing
arrangements to promote their other products and services."* A subsidy war against Amazon,
Google, Apple and Walmart is not a moat; it is the round of investment [E2-27] describes.

**FOUR — THE ASYMMETRY OF RESOURCES, FILED ON BOTH SIDES, AND THE 10-K CONCEDES IT IN THESE
WORDS: *"We compete with much larger companies which have resources and brand recognition that
pose significant competitive challenges."***

| | the figure | against Roku |
|---|---|---|
| Amazon's **advertising services** line alone | $68,635M | **14.5x Roku's entire revenue** |
| Amazon's **one-year growth** in that line | +$12,421M | **2.6x Roku's entire revenue** |
| Alphabet's **YouTube ads** | $40,367M | **9.7x Roku's Platform revenue** |
| Alphabet's **one-year growth** in YouTube ads | +$4,220M | **89% of Roku's entire revenue** |
| Apple's "Wearables, Home and Accessories" (where the Apple TV box lives) | $35,686M | **7.5x Roku's whole company** |
| Amazon operating cash flow | $139,514M | **288x** |
| Alphabet operating cash flow | $164,713M | **341x** |
| Apple operating cash flow | $111,482M | **231x** |

**And the *shape* of that asymmetry is the finding, not just its size.** Amazon's FY2025 10-K
uses the phrase **"Fire TV" once**, and the words **"connected TV" and "operating system" zero
times**. Alphabet's FY2025 10-K names **"Google TV" zero times and "Android TV" zero times**; its
single television reference describes Alphabet as a *tenant* — *"people access our products and
services through a growing variety of devices such as … **television-streaming devices** … Our
products and services may be less popular on some interfaces."* Apple names **"Apple TV" twice
and "tvOS" twice**, and **televisions are absent from its own statement of its market
opportunity**. None of the three names Roku. **Roku's entire business is a rounding error in the
annual reports of the three companies that make its substitutes — and every one of them ships
one anyway.** That is not an absence of competition; it is the definition of a business whose
whole market is somebody else's side project, and a side project funded at 300x cannot be
out-spent.

**FIVE — A THIRD PARTY'S OWN FILING DESCRIBES ROKU AS AN INTERCHANGEABLE SURFACE, AND THIS IS
THE CLEANEST [E3-03](2) EVIDENCE IN THE FILE.** Charter Communications is the only peer in the
row that names Roku, and here is how, verbatim from its FY2025 10-K:

> *"Customers are increasingly accessing their subscription video content through our highly
> rated Spectrum TV app via mobile devices and connected Internet Protocol ("IP") devices, such
> as **Xumo, Apple TV, Roku, Vizio, LG and Samsung TV**."*

**Six substitutes in one sentence, listed interchangeably, by a company that distributes through
all of them and part-owns one of them.** And Roku behaves the same way in reverse: its own 10-K
states that The Roku Channel *"is also available via the Roku mobile app, online at
TheRokuChannel.Roku.com, and on **Amazon Fire TVs, Samsung TVs, Google TV**, and other Android
TV OS devices."* **Roku distributes its own content and advertising business on its competitors'
operating systems, which is an admission by conduct that the operating system is not the moat for
the business that earns the money.**

**SIX — THE SEVENTH SUBSTITUTE THE BRIEF DID NOT NAME.** Comcast and Charter jointly own **Xumo**,
and it is a television operating system, not a channel. Comcast's FY2025 10-K, verbatim: *"**Xumo,
our consolidated streaming platform joint venture with Charter Communications. Xumo is focused on
developing and offering a streaming platform on a variety of devices, including Xumo TV smart
televisions, which have an operating system** that leverages our global technology platform, and
also operates the Xumo Play streaming service."* Plus hardware: *"We also offer **Xumo Stream
Box** devices to our domestic broadband customers."* Comcast consolidates Xumo but reports it
inside "Corporate and Other" with Sky Germany and the Philadelphia Flyers, so **it is unsized** —
a substitute backed by $33.6bn of annual operating cash whose scale cannot be read.

**SEVEN — AND THE STRONGEST FACT IN THE ROW RUNS ROKU'S WAY. It is stated here, not buried.**
Roku's Platform revenue of **$4,145M exceeds Comcast's entire advertising line ($3,712M, falling
9.2%) and is 2.8x Charter's ($1,468M, falling 17.6%)** — and Roku's grew 18% in FY2025 and 25% in
Q2 2026 while both of theirs fell. **Roku is winning the transfer of advertising dollars out of
linear television, on filed figures, on both sides.** That is real and it is the best argument
the bull case has.

**But note what it is an argument for**, because [E4-36] asks which of the four causes of extreme
success the record comes from, and **[E3-51]** names this one: *"when a surfer gets up and catches
the wave and just stays there, he can go a long, long time. But if he gets off the wave, he
becomes mired in shallows."* Roku's own filing dates the wave: *"Since our IPO in 2017, the
streaming TV industry has evolved meaningfully, with **Americans now spending significantly more
TV time streaming than watching traditional TV**."* Winning share of a category that is doubling
is wave-riding, and **a surfing run is not a moat; the advantage lives in the wave, not the
surfer.** The test that separates them is whether the position can be priced — and the Vizio
comparison says it cannot.

**EIGHT — THE COMPARISON WITH THE ONE PEER ROKU IS BIGGER THAN, WHICH IS THE MOST UNCOMFORTABLE
ROW IN THE TABLE.**

| | Roku FY2025 | The Trade Desk FY2025 |
|---|---|---|
| Revenue | **$4,737M** | $2,896M |
| **Operating income** | **$(5.6)M** | **$589.3M — 20.4% margin** |
| **Operating cash flow** | **$484M** | **$993M** |
| Operating cash flow ÷ revenue | **10.2%** | **34.3%** |
| Filed switching-cost metric | **none** | **">95% retention for over a decade"** |
| Owns an operating system | yes | **no** |
| Owns hardware | yes | **no** |
| Negative-margin device line | **yes, −$82.0M** | **no** |

**The Trade Desk earns twice Roku's operating cash flow on 61% of Roku's revenue, with no
operating system, no hardware and no loss-making device segment — and it is the only company in
the row that files a switching-cost metric at all.** The asset Roku spends $82M a year of gross
loss and a large slice of sales and marketing to own produces less cash than the business of
buying access to it. And The Trade Desk describes Roku without naming it: *"Our platform delivers
valuable insights and results to clients without the conflict of interest and lack of objectivity
that come with **also selling owned advertising inventory**."*

**NINE — ROKU IS NOT ALONE IN DELETING ITS USER METRIC, AND THAT MAKES THE READ HARDER, NOT
MILDER.** Netflix's FY2025 10-K contains **no paid-membership count, no net-additions line and no
revenue-per-membership figure** — it reports revenue by region and an operating-margin target and
nothing below that. Vizio's metrics died with the company. **Three of the four CTV filers that
once published a user series have stopped.** That is a fact about the industry's disclosure, and
it is the reason the moat class below is what it is.

---

### THE REMAINING Q2 TESTS, ANSWERED

**[E3-03], criterion by criterion.**
- **(1) Needed or desired — YES.** 145.6 billion hours streamed in FY2025 across ~90 million
  households is not a product people tolerate.
- **(2) No close substitute — NO, AND THIS IS THE OUT.** Six operating systems substitute
  directly, plus Xumo. Roku's own risk factors name Amazon, Apple, Google and Walmart/Vizio,
  concede that *"These companies have greater financial resources than we do and can subsidize
  the cost of their streaming devices or licensing arrangements"*, and — decisively — concede
  that **substitution has already happened**: *"at times our existing licensed Roku TV partners
  have chosen to work exclusively with, or divert a significant portion of their business with
  us, to **other operating system developers**."* Charter's filing lists Roku as one of six
  interchangeable surfaces. Roku itself ships The Roku Channel onto Fire TV, Samsung TVs and
  Google TV. **A franchise's customers are *"thought by its customers to have no close
  substitute"*; Roku's customers demonstrably think there are five.**
- **(3) Not price-regulated — YES.**

**Two of three. [E3-03] is not a scorecard; criterion (2) is the criterion, and it fails.**

**[E4-04] — must the moat be continuously rebuilt?** The v4 scope test is whether *"a lapse in
spending destroys the structure, or merely narrows it — and does the spending defend the same
advantage, or buy its replacement?"* **Roku's scarce asset is the default position on a
television set, and a television set is replaced every seven years or so.** So the position must
be **re-won on roughly one-seventh of the installed base every year**, through OEM licences that
are *"renegotiated periodically"*, retailer shelf space held under **no long-term contract**, and
hardware sold at a cumulative gross loss of **$334.6M over five years**. That is the Rhodes Ridge
shape, not the Coca-Cola shape: the spending buys the *replacement* of the base, not the defence
of the same trademark. Coca-Cola's advertising defends a trademark that does not expire; Roku's
device subsidy buys households that physically wear out.

**[E3-33] and [E5-28] — untapped pricing power?** **No, and the evidence is the absence.** *"If
you name some business that has incredible pricing power, you're talking about a business that's
a monopoly or a near monopoly"* **[E5-28]** — the claim would require the competitor row to
support near-monopoly, and the row has six substitutes, two of them structurally unmeasurable and
three of them 85-151x larger. And **[E4-37]**'s inverse metric reads the other way: ARPU flat for
four years at the peak of Roku's position, with the company's own stated reason being mix
dilution it cannot price through, is *"the agony they go through in determining whether a price
increase can be sustained"* expressed as four years of not attempting one.

**[E2-45] — the attacker's test, the shelf's one forward-looking moat test.** *"how I would like,
assuming I had ample capital and skilled personnel, to compete with it."* **I would like it very
much, and the filing tells me how.** I would licence my operating system to TV makers for free or
for negative money, since I make my return elsewhere — which is what Amazon and Google already
do. I would buy the shelf, since two of the four retailers that sell 81% of Roku's devices are
already my company or my competitor's. I would subsidise the hardware from a business 150x the
size, which Roku's own risk factor says I can do. **There is no step in that attack that requires
skill Roku's competitors lack or capital they do not have — and three of them have already taken
every step.** Compare the answer a franchise gives: attacking Coca-Cola requires buying a century
of trademark, and no amount of capital buys it.

**[E2-53] — the dominance class?** *"Once dominant, the newspaper itself, not the marketplace,
determines just how good or how bad the paper will be. Good or bad, it will prosper."* **Refuted
on Roku's own numbers.** Households grew from 60.1M to 89.8M, +49.4%, and streaming hours from
73.2bn to 127.1bn, +73.6%, over 2021-2024 — and **operating income over the same three years was
−$531M, −$792M, −$218M.** Position did not set the economics; nothing prospered. This is the same
refutation the ULTA run found (stores +14.9%, members +6.2%, operating income −8.6%) and it is
sharper here.

**[E3-46] and [E2-01] — the second question about the business, and it is a number.** *"the best
businesses, by definition, are going to be businesses that earn very high returns on capital
employed over time."* **Roku has an operating loss in nine of its ten filed years.** FY2025
operating income was **−$5,624k**; the FY2025 net income of $88,361k is $99,522k of interest on
the cash pile. On unleveraged net tangible assets **[E2-43]** of $2,298,332k the FY2025 return is
**3.8% on net income and −0.2% on operating income.** Detail and the full series are in the Q3
items below, recorded there without a verdict; the *number* belongs here because the corpus asks
it about the business, before the manager.

**CLASS AND DIRECTION.**
- **Class: NONE.** Not PROVISIONAL. A PROVISIONAL class would be right if the verdict turned on
  peer data I could not get — and two peers' data genuinely cannot be got. **It does not turn on
  them.** It turns on Roku's own filed risk factors, on Roku's own withdrawn unit series, on
  Roku's own ten-year operating-loss record, and on one peer whose filed ARPU rose 71% while
  Roku's rose 1.1%. **A missing peer row cannot rescue a franchise claim that the subject's own
  filing contradicts in its own words.**
- **Direction [E4-32]: UNMEASURABLE, and that is itself the answer.** *"Direction outranks
  existence"* is *"the primary criterion of a great business"*, and the two series that measure
  the direction of Roku's scarce asset were deleted from the 10-K in the year it mattered. What
  can still be measured points down: streaming-player units −4%, −14%, −8% before the basis
  changed; ARPU +1.1% over three years; household growth decelerating 39% → 17% → 16% → 14% →
  12% before the series ended; platform gross margin 52.3% → 52.0%; and consolidated gross margin
  50.9% → 43.8%.

**THE STRONGEST SINGLE FACT AGAINST THIS VERDICT, stated as its holders would state it
[E4-51].** **Roku's advertising gross margin expanded approximately 650 basis points year on year
to 62.4% in Q2 2026, while advertising revenue grew 25% and grew faster than both the US OTT and
the US digital advertising markets, and advertising gross profit grew 39% on that 25% of revenue
growth.** A business with no moat, facing five larger and several vertically integrated rivals,
should be surrendering price. Roku gained 650 basis points of margin while taking share. Add to it
that the OS cost advantage is a real, filed, *technical* advantage — *"the Roku TV OS requires
significantly less dynamic memory (DRAM) and storage memory (Flash) than competing platforms, and
this widening cost advantage is drawing more TV brands to Roku"* — and that Roku added **Hisense
and TCL** as OEM partners in 2025, in the same year the risk factor concedes other partners
defected. **If I am wrong about Roku, that is where the error is, and the document that would
settle it is the household series at Q6 condition 1.**

**Why the verdict stands anyway.** [E3-03](2) asks about substitutes, not about this year's
margin. The 650 basis points were earned inside a category that Roku's own filing says is still
taking share from linear television, which is the surfing run **[E3-51]**, and the test that
separates a moat from a wave is whether the position can be *priced* when the wave flattens.
**Roku's own ARPU was flat for four years at the peak of its position while a fifth-the-size
competitor raised its take 71% — that is the test, it was run, and Roku failed it.**

- **VERDICT: [x] OUT** — permanent, on criterion (2) of **[E3-03]**, evidenced from Roku's own
  risk factors, one third party's filing, and the one competitor that published the same metrics.

## THE ONE NUMBER — SBC AGAINST OPERATING CASH, AND ROKU SETS THE RECORD **[E5-06, E3-70]**

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
- [x] Step 0: the filing was read, with accession numbers for nine 10-Ks, one 10-Q, four 8-Ks
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

---
## RUN LOG
- **2026-09-12.** Framework and template read; run file created from the template before any
  filing was fetched (write-early protocol); committed after each gate, by file name.
- **Documents fetched and read:** nine Roku 10-Ks (FY2017 through FY2025, which between them
  carry filed figures back to FY2015), the Q2 FY2026 10-Q, four 8-Ks (the merger agreement, the segment recast, the
  Q2 earnings furnishing, the DOJ Second Request), four EX-99.1 shareholder letters (Q3 2025
  through Q2 2026), and the 2026 DEF 14A. Eleven peer primary documents for the competitor row.
  Artifacts and extraction scripts in `Test Runs/_research 2026-09-12 ROKU/`.
- **Priors in the brief that were REFUTED:**
  1. *"an advertising platform whose early years straddle zero"* (the PINS analogue) — **the
     straddle is not in the early years. Fourteen of sixteen constructions are negative,
     including the five-year default window, and the only positive ones are FY2025 and the TTM.**
  2. *"ARPU is not a price … the PINS run found ARPU rising 46% while the money segment's users
     fell. Run the same decomposition"* — **run, and it comes out inverted: users rose 49% while
     ARPU rose 1.1%.** The Precision Steel shape is present, but in the *streaming-player unit*
     series, not in ARPU.
  3. *"Devices … historically sold at or below cost"* — true, but the brief's framing misses that
     **OEM-licensed Roku TV models "account for the largest portion of our overall unit volume"**
     and cost Roku no device margin at all; the Devices gross loss is the minority channel.
  4. *"net cash and little debt is my expectation — check it"* — **confirmed and then some:
     $2,557M liquid, zero interest-bearing debt, $1,055k of interest paid in FY2025.**
  5. *"check whether the contract-liability balance is customer money on the balance sheet"* —
     **only 44% of it is. The larger half is an accounting allocation of cash already collected
     at the point of a device sale.**
- **Priors that were CONFIRMED:** the [E2-49] withdrawal prior (on all three series at once, a
  first for this queue); the Q2-OUT prior on [E3-03] criterion (2); the [E4-29] prior on Adjusted
  EBITDA; the Q1 segment-split prior (the split does kill a claim the consolidated numbers
  supported, as at AMAT and SHOP).
- **DEFECTS FOUND — in the brief:**
  1. **The brief does not contain the single most important fact about this security: Roku signed
     a definitive merger agreement with Fox Corporation on 2026-06-14.** Neither does the queue
     row, which reads `newest_periodic 2026-06-30` — a periodic filing whose own EX-99.1 says
     *"In light of the pending transaction, we will not host an earnings call and will not
     provide a financial outlook."* The screen reads the XBRL of the 10-Q and cannot see Item
     1.01 of an 8-K, which is a structural blind spot worth a guard: **a `merger_flag()` that
     tests for an 8-K Item 1.01 or a DEFM14A since the last 10-K would have caught it, and the
     same blind spot will recur on every name in the queue that gets taken over.**
  2. The brief calls the 351% line *"the CONTRACT-LIABILITY line"* and asks what it is at Roku.
     Answered — but the brief's two precedents (DELL's payables swing, INOD's $116M customer
     prepayment) primed the wrong shape. **At Roku the flag is a small-denominator artifact and
     the real working-capital events are untested lines.**
- **DEFECTS FOUND — in the tooling:**
  1. **`wc_note` divides one balance-sheet delta by a single year's operating cash.** On any year
     whose operating cash is near zero every routine delta reads as a giant percentage, and the
     flag then reports the smallest movement in the statement. Roku FY2022: the flag names
     `Deferred revenue` at +$41.4M and cannot see `Content assets and liabilities, net` at
     −$313.2M in the same column. **Same defect family as the `ZeroDivisionError` that made MU
     and INTC re-triage as UNPRICED: near-zero denominators.** The fix is not a threshold — it is
     to report the delta as a share of **revenue** or of the **largest working-capital line**
     alongside the operating-cash ratio, and to flag the largest movement rather than one chosen
     tag.
  2. **`oe_bottom` and `oe_top` are again two different windows on the same name** (five-year and
     three-year, both at the capex end), advertised as a spread. Found on INTC 2026-09-07,
     unfixed, and it recurs here.
  3. **No working-capital flag reads the content-asset line**, which is the largest
     working-capital line in Roku's cash-flow statement in every one of the last four years and
     is this business's real capital expenditure.
