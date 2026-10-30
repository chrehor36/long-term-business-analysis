# Company Run — ALPHABET INC. (GOOGL / GOOG) — 2026-09-06
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
- rate **5.24** % · date **2026-09-04** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck fresh this run via `tools/sources.py`. Not FRED.
- FX: none. Alphabet reports in USD and earns predominantly in USD. No ADR ratio.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2025 10-K, filed 2026-02-05, acc.
  0001652044-26-000018** (`goog-20251231.htm`, 2.6MB, downloaded and parsed in full);
  **Q2-2026 10-Q, filed 2026-07-23, acc. 0001652044-26-000071** (`goog-20260630.htm`).
  Eleven further 10-K vintages FY2015–FY2024 read for the Note 1 diff (register in
  `_research 2026-09-06 GOOGL/A1-useful-lives.md` and `C1-segments.md`).
- figure cross-checked against the filed statement: **seven of them, by string match in the
  filed HTML** — revenue $402,836M; operating income $129,039M; net income $132,170M; OCF
  $164,713M; purchases of property and equipment $(91,447)M; SBC $24,953M; depreciation of
  property and equipment $21,136M. All present verbatim in `goog-20251231.htm`.
  **SENTINEL:** "Alphabet Inc." appears 133 times in the FY2025 10-K, 35 times in the
  Q2-2026 10-Q — checked before any figure was transcribed (the AAPL run's stale-document
  hazard).

### STAGE 0(a) — THE SHARE COUNT, BY HAND, AND THE RENDERER WAS RIGHT

**THREE CLASSES, AND THE COVER REPORTS IN MILLIONS.** The audit's warning is confirmed
verbatim from the Q2-2026 10-Q cover:

> "As of July 15, 2026, there were **5,868 million** shares of Alphabet's Class A stock
> outstanding, **835 million** shares of Alphabet's Class B stock outstanding, and **5,527
> million** shares of Alphabet's Class C stock outstanding."

| class | ticker | votes | shares (2026-07-15 cover) | price 2026-09-04 | value |
|---|---|---|---|---|---|
| Class A | GOOGL | 1 | 5,868,000,000 | $338.46 | $1,986,083M |
| Class B | *unlisted* | 10 | 835,000,000 | $338.46 (converts 1:1 to A) | $282,614M |
| Class C | GOOG | **0** | 5,527,000,000 | $335.31 | $1,853,258M |
| **total common** | | | **12,230,000,000** | | **$4,121,956M** |

Cross-checked against the 2026-06-30 balance sheet, which states the same counts
independently: *"12,230 (Class A 5,868, Class B 835, Class C 5,527) shares issued and
outstanding."* At 2025-12-31 the count was **12,088** (5,822 / 837 / 5,429).
**THE COUNT ROSE BY 142 MILLION SHARES IN SIX MONTHS. Alphabet is issuing, not retiring.**

**Honest limit, recorded:** the cover and the balance sheet both round to the nearest
million, so the count is precise to ±0.5M per class — about ±$0.5bn of cap on a $4.1tn
company, immaterial, but it is a rounding and not a hand-count of an exact integer the way
AAPL's 14,594,180,000 was.

**A FOURTH INSTRUMENT, ISSUED 2026-06-05 AND NOT IN ANY SCREEN:** 19 million shares of
**6.25% Series A and Series B Mandatory Convertible Preferred Stock** (depositary shares
GOOGM / GOOGN), liquidation preference $1,000/share = **$19,000M**, net proceeds $19.0bn.
It converts automatically on or about **2029-05-15** into between 2.2520–2.8160 Class A
(Series A) and 2.2740–2.8420 Class C (Series B) per preferred share — i.e. **43–54 million
additional common shares are already contracted**. Cap used in this run:

> **$4,121,956M common + $19,000M preferred at liquidation preference = $4,140,956M,
> rounded $4,141,000M.** The common-only figure is carried alongside.

*Price source: Yahoo Finance close 2026-09-04 — **aggregator, flagged**, live quote only,
the same date and rung the parallel AAPL and MSFT runs used. Note GOOG trades at a **0.93%
discount** to GOOGL ($335.31 vs $338.46): the market prices the vote at under one percent,
which is the cleanest available evidence that the classes are economically equivalent.*

---

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Alphabet operates the box that
most of the world types its intentions into, gives the answer away free, and sells the
instant of intent to whoever bids most for it. A person who types "plumber near me" has
pre-qualified himself more completely than any advertisement could; Alphabet auctions that
moment. The marginal cost of serving one more query is a fraction of a cent of electricity
and amortised silicon; the marginal revenue on a commercial query is measured in dollars.
That gap — the highest-margin advertising asset ever assembled — is the whole business.

Everything else is a variation on it or a bet against it:
- **YouTube** rents the same attention in longer units and pays creators a revenue share.
- **Google Network** rents Alphabet's auction to other people's websites and pays them a
  share; it is the low-margin leg and it is **shrinking**.
- **Subscriptions, platforms and devices** sells storage, YouTube Premium, Play commissions
  and hardware — a mix of a toll and a manufacture.
- **Google Cloud** rents the datacentres Alphabet built for itself to other companies. It is
  a genuinely different business: capital-intensive, priced against two larger rivals,
  margin 23.7%.
- **Other Bets** is venture capital funded out of the search business's cash flow.

**The three-business structure is required, not optional [E5-37]** — *"different numbers are
of different importance … depending on the kind of business"*. On the FY2025 filed segment
note, one company contains three:

| FY2025 | revenue | operating income | margin |
|---|---|---|---|
| **Google Services** | $342,721M | $139,404M | **40.68%** |
| **Google Cloud** | $58,705M | $13,910M | 23.69% |
| **Other Bets** | $1,537M | **$(7,515)M** | (489%) |
| Alphabet-level activities | — | **$(16,760)M** | — |
| Hedging | $(127)M | — | — |
| **consolidated** | **$402,836M** | **$129,039M** | 32.03% |

**The scarce input this business controls.** Not the index, not the algorithm, not the
datacentres — competitors have all three. It is **the query stream**: the habit of tens of
billions of daily stated intentions arriving at one destination by default. And that habit
is, in material part, **purchased rather than owned** — Alphabet pays for default placement
on other people's devices and browsers. Traffic acquisition cost was **$59,926M in FY2025**.
That is the scarce input's rent, it is 14.9% of total revenue, and **who sets its price is
now a matter before a federal court** (Q2, criterion 3). A scarce input you rent from a
counterparty under a contract a judge is rewriting is a weaker thing to own than one you
possess, and the run says so here rather than at the end.

**Will the fundamentals look broadly the same in ten years?** The *mechanism* — intent
auctioned to advertisers — is thirty years old and I can state it without management's
language, which is [E3-31]'s test. The *delivery* is being rebuilt in public: generative
answers replace ten blue links, capex has gone from $22bn to a $161bn annual run-rate, and
the company is now funding that with debt, preferred and new equity. **[E3-31] asks for
"relatively simple and stable in character", and Alphabet is simple but is not currently
stable in character.** This does not fail Q1 — I can write the unit economics, name the
scarce input, and read the statements — but it is the reason certainty is spent here and
not saved for later **[E3-42]**, and it is why the (c) question at Q4 is the whole file.

**VERDICT: [x] IN** — the money-making mechanism is legible from the filings and statable
in one sentence. Recorded against it: the delivery mechanism is mid-rebuild, and the scarce
input is partly rented.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Judged as three businesses, not one [E5-37]** — *"different numbers are of different
importance … depending on the kind of business."*

- **Needed or desired [x]** — 13% more paid clicks year on year in Q2-2026, filed. Yes.
- **No close substitute [~]** — for *Search*, on the filed monetization series, still yes.
  For *Cloud*, no: it is the third-largest of three and Alphabet's own Competition section
  concedes "providers of enterprise cloud services" and "AI model developers".
- **NOT PRICE-REGULATED — [x] FAILS, ON ALPHABET'S OWN FILED WORDS.** See criterion 3 below.

### CRITERION 3 — THE BRIEF'S HYPOTHESIS (a), AND IT IS RIGHT

The brief asked whether the remedies materially set the terms on which Search is
distributed. **They do, a final judgment has been entered, and Alphabet says so itself.**
FY2025 10-K, acc. 0001652044-26-000018, Note 10, *Antitrust Matters*, verbatim:

> "In August 2024, the US District Court for the District of Columbia ruled against Google.
> **A final judgment was entered in December 2025, which, among other things, imposes
> restrictions on how Google distributes its services and requires Google to share certain
> search data with and offer syndication services to certain competitors.** In January 2026,
> we appealed the final judgment and moved to pause implementation of certain remedies. In
> February 2026, the DOJ and state Attorneys General also appealed."

This is the AAPL shape exactly — that run found Apple admitting "a court order preventing it
from imposing any commission or fee on certain purchases" — **but Alphabet is further along
and in more jurisdictions.** Orders altering distribution are in force in four:

| matter | rung | what is actually ordered | status |
|---|---|---|---|
| **US v. Google (Search)**, D.D.C. | 1 (10-K) + 2 (docket) | restrictions on distribution; **compelled search-data sharing and syndication to competitors** | **final judgment Dec 2025**; both sides appealed Jan/Feb 2026 |
| **EC Android** (Jul 2018) | 1 | €4.3bn → €4.1bn; **"directed the termination of the conduct at issue"**; Alphabet "implemented changes to certain of our Android distribution practices" | affirmed Sept 2022; ECJ appeal pending |
| **Japan JFTC** (Apr 2025) | 1 | **cease-and-desist requiring changes to Android agreements**; no monetary penalty | in force |
| **Australia ACCC** (Aug 2025) | 1 | settlement "requiring, among other things, changes to our Android agreements"; charge taken Q2-2025 | court-approved Dec 2025 |
| **Epic v. Google** | 1 | Oct 2024 remedies "ordering a variety of alterations to our business models and operations and contractual agreements for Android and Google Play" | **appeal DENIED Jul 2025**; appealing to SCOTUS |
| **US v. Google (Ad Tech)**, E.D. Va. | 1 | Apr 2025: "Google's publisher tools unfairly excluded rivals"; **"The DOJ's remedy proposal includes structural remedies that could have a material adverse effect on our business"** | remedies argued Nov 2025, **judgment awaited** |
| **EC Ad Tech** (Sep 2025) | 1 | €3.0bn fine + cease-and-desist on self-preferencing; **$3.5bn charge taken Q3-2025**; bank guarantees in lieu of cash Q4-2025 | appealed Nov 2025 |
| EC Shopping (2017) | 1 | €2.4bn; **$3.0bn cash paid 2024** | closed |
| EC AdSense (2019) | 1 | €1.5bn — **ANNULLED Sept 2024**, EC appealed | the one Alphabet won |

**Criterion 3 fails. The class is NARROW, not OUT** — [E2-59] is explicit that regulation
*caps* a franchise rather than creating or destroying the class, and the cap is priced at Q5
per [E2-63]. This is the AATC/QCOM "the licence has a term" shape at the largest scale the
queue has run.

**But the direction of the economic effect is NOT the one the brief assumed, and the run
says so against its own prior [E4-26].** The remedy that was *refused* matters more than the
ones granted: the judgment did **not** order divestiture of Chrome or Android, and it did
**not** ban the default-placement payments — it restricts and de-exclusivises them. Alphabet
therefore **keeps the distribution and keeps paying for it**. A ban would have *raised*
owner earnings by the whole TAC line. The realistic damage is share loss at the margin plus
compelled data sharing that lowers a rival's cost of entry — real, slow, and not quantifiable
from any filed document. **Alphabet discloses no accrual and says so: "Given the nature of
these matters, we cannot estimate a possible loss."**

**A candour point that runs the other way and is recorded here [E2-26]:** unlike Apple,
which disclosed no accrual for any named matter, Alphabet **accrues and quantifies** —
$5.1bn (Android, later reduced $217M), $1.7bn (AdSense), **$3.5bn (EC ad tech, Q3-2025)**,
charges for ACCC and for the Play state-AG settlement, and $3.0bn of cash actually paid on
Shopping. It also files the fact that it *lost* the AdSense fine on appeal. That is the
[E2-26] half-owner standard met on the litigation line.

### THE PRICE OF DISTRIBUTION IS THE SCARCE INPUT, AND IT IS RENTED

**TAC FY2025 = $59,926M**, 20.3% of advertising revenue, cross-checked: 59,926 ÷ 294,691
(Note 2 disaggregation: Search & other 224,532 + YouTube ads 40,367 + Network 29,792) =
20.34%, which reproduces Alphabet's own filed 20.3%. The series:

| FY | 2015 | 2017 | 2019 | 2021 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|
| TAC $M | 14,343 | 21,672 | 30,089 | 45,566 | 50,886 | 54,900 | **59,926** |
| aggregate rate | 21.3% | 22.7% | 22.3% | 21.8% | 21.4% | 20.7% | **20.3%** |

**The ~$20bn Apple payment is NOT filing-sourced from either side of the contract, and this
run is the other half of the AAPL run's finding.** Recorded sweep of Alphabet's FY2025 10-K:
**"Apple" = 0 occurrences.** So does "Microsoft", "Amazon", "Meta", "OpenAI", "Anthropic",
"ChatGPT" and "TikTok" — **Alphabet names ZERO competitors by company name in any part of
its FY2025 10-K**, describing eleven *categories* instead ("general purpose search engines",
"AI model developers", "companies that design, manufacture, and market consumer hardware
products, including businesses that have developed proprietary platforms"). The AAPL run
found the identical absence from the other direction and found that Alphabet had named Apple
four times in FY2021. **Both counterparties to a ~$20bn annual contract have removed the
other's name from their filings.** The number exists only on the court-record rung.

### [E2-49] METRIC-SWITCHING — TWO WITHDRAWALS, BOTH DATED TO THE APPLE STANDARD

**(1) THE TAC SPLIT — and the brief's dating was wrong in BOTH prior versions.** An earlier
brief said FY2016; a mid-run correction said FY2018. Both are wrong: the split ran one
quarter further.

| | |
|---|---|
| **Last filed** | **Q3-2019 10-Q, `goog10-qq32019.htm`, filed 2019-10-29, acc. 0001652044-19-000032** |
| **First omitted** | **FY2019 10-K, `goog10-k2019.htm`, filed 2020-02-04, acc. 0001652044-20-000008** |
| **Elapsed** | **98 days**, with no intervening periodic report |
| Filed reason | **NONE.** "no longer" = 0 hits in the FY2019 10-K; no presentation-change note attaches to the TAC table |

**What the series was doing when it went.** The two legs moved in opposite directions and
the survivor is the one that flatters:

- **TAC to distribution partners as a % of Google properties revenue — the price of the
  Apple/Mozilla/carrier default deals — ROSE EVERY SINGLE YEAR IT WAS FILED:
  7.8% → 9.2% → 11.6% → 13.1% → 13.3%.** In dollars $4,101M → $12,572M, **3.07x in three
  years**, crossing 50% of total TAC for the first time in the final filed stub.
- Network Members' rate had peaked (71.9% in 2017) and was falling.
- **The aggregate rate — the only one that survived — was FALLING, purely on mix**, because
  high-TAC Network revenue was shrinking relative to low-TAC owned-and-operated revenue.

Alphabet's own final filed explanation names the cause verbatim: *"The increase in the Google
properties TAC rate was driven by **changes in partner agreements** and the ongoing shift to
mobile"* (FY2017 and FY2018 10-Ks). **"Changes in partner agreements" is Alphabet's filed
phrase for the default contracts repricing upward, and it stops appearing after the split
is withdrawn.** Since 2019-10-29 the price of the exact contracts at issue in *US v. Google*
has been unobservable on the filing rung — **six years and ten months**. The surviving
shadow is an adjective: Alphabet has said that rate "increased" twice (FY2019, FY2024) and
"substantially consistent" five times, and **has never once in seven years said it fell.**

**(2) THE AGGREGATE AND NETWORK PAID-CLICK SERIES**, withdrawn a year earlier:
last filed **FY2017 10-K, 2018-02-06, acc. 0001652044-18-000007**; first omitted **Q1-2018
10-Q, 2018-04-24, acc. 0001652044-18-000016**; **77 days**; no reason filed. What went:
**Network cost-per-click was negative in all four years it was ever filed** (−6/−3/−13/−9%)
and aggregate CPC was negative and deteriorating in all four (−5/−11/−11/−19%). Switching
the Network leg from *clicks* to *impressions* reset that streak to zero at the moment of the
switch. **Twice, the metric that went was the one printing the worse number.**

### [E4-55] THE PHYSICAL SERIES — AND HERE THE BRIEF'S PREDICTION INVERTS

*"Where units exist, monitor units"* — and **they exist, they are current, and they are
good.** Contrary to the AAPL precedent the brief expected to repeat, **paid clicks and
cost-per-click were NOT withdrawn.** They are in the FY2025 10-K and in both 2026 10-Qs:

| | FY2021 | FY2022 | FY2023 | FY2024 | **FY2025** | **Q1-26** | **Q2-26** |
|---|---|---|---|---|---|---|---|
| Search paid clicks Δ | 23% | 10% | 7% | 5% | **6%** | **13%** | **13%** |
| Search cost-per-click Δ | 15% | (1)% | 1% | 7% | **7%** | **5%** | **3%** |
| Network impressions Δ | 2% | 3% | (5)% | (11)% | **(7)%** | **(9)%** | **(12)%** |

**Units are ACCELERATING (5% → 6% → 13% → 13%) while price is RISING (+7%, +7%). That is
[E2-44](1) passed on a filed physical series — volume up and price up together — and it is
the single strongest fact in this file.** It is the exact inverse of Precision Steel and the
inverse of Apple's iPhone units. **On the evidence Alphabet actually files, the Search
franchise is not eroding; it is compounding, and the AI-answers thesis that was supposed to
kill it is not visible in the click series through 2026-06-30.**

And Alphabet keeps filing the *ugly* leg too: Network impressions −12% in the latest quarter,
published. That is [E2-26] met.

**The honest deduction on the other side:** the explanatory content was withdrawn even though
the numbers were kept. FY2019 named a cause ("continued growth in YouTube engagement ads
where cost-per-click remains lower"); FY2023, FY2024, FY2025, Q1-2026 and Q2-2026 are
**word-for-word identical boilerplate** reciting "a number of interrelated factors". And
from FY2021 the table carries **one column only** — no comparative — so the series exists but
must be rebuilt from five separate filings.

### THE MOAT METRIC, FILING-SOURCED, AND ITS TREND

| FY | 2018 | 2020 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|
| **Google Services op margin** | 33.05% | 32.38% | 32.62% | 35.17% | 39.77% | **40.68%** |
| Google Cloud op margin | (74.5)% | (42.9)% | (7.3)% | +5.19% | +14.14% | **+23.69%** |
| Consolidated | 20.12% | 22.59% | 26.46% | 27.42% | 32.11% | **32.03%** |

**And the Google Services number is flattered — the run computes the honest version.** The
Q1-2023 recast moved DeepMind and general AI R&D *out* of Google Services into
"Alphabet-level activities", whose loss went **$(1,299)M (2022) → $(16,760)M (2025)**.
Charging that back where the R&D is actually consumed: Google Services + Alphabet-level =
**32.1% (2022) → 35.8% (2025)**, not 32.6% → 40.7%. Still widening, by roughly half as much.
*(C1 also records that FY2018–FY2020 segment operating income was NEVER recast onto the
post-2023 basis, so no clean ten-year segment series exists.)*

### THE COMPETITOR ROW — required [E3-28]

Six peers taken, on two metrics, same window, all filing-sourced. The industry has roughly
six real participants at this scale and I took all of them; Samsung and the Chinese
hyperscalers are outside SEC reach and are stated, not stretched.

| Company | operating margin, latest FY | capex / revenue | capex / D&A | source |
|---|---|---|---|---|
| **ALPHABET** | **32.0%** *(Services 40.7%)* | **22.7%** *(TTM **29.7%**)* | **4.33x** *(TTM **5.25x**)* | FY2025 10-K 0001652044-26-000018 |
| **Meta** — the advertising peer | **41.4%** | 34.7% | 3.74x | FY2025 10-K |
| **Microsoft** | **46.8%** | 34.9% *(42% w/ leases)* | 3.38x | FY2026 10-K |
| **Amazon** | 11.2% | 18.4% | 3.15x | FY2025 10-K / MSFT run row |
| **Oracle** | 30.6% | **82.6%** | **7.30x** | FY2026 10-K |
| cloud margin | Google Cloud **23.7%** | AWS 35.4% · MSFT IC 41.3% | | segment notes |

**Three things the row says that one company's numbers cannot.**
1. **Alphabet is NOT the margin leader.** Meta earns 41.4% and Microsoft 46.8% against
   Alphabet's 32.0%. Alphabet's *Services* segment at 40.7% is roughly Meta's whole company,
   and Alphabet spends the difference on Cloud, Other Bets and frontier AI.
2. **Google Cloud is the WORST-positioned of the three clouds on the only comparable metric
   filed** — 23.7% against AWS 35.4% and Microsoft IC 41.3%. It is third of three, and
   [E3-03](2) plainly fails there.
3. **The capital escalation is universal, which is [E2-27] and [E2-30](4) together.** Every
   one of the five raised capex/revenue sharply in the same eighteen months. *"Viewed
   individually, each company's capital investment decision appeared cost-effective and
   rational; viewed collectively, the decisions neutralized each other and were irrational."*
   **And Alphabet is now the second-most capital-hungry of the four hyperscalers on
   capex/D&A** — 5.25x TTM, behind only Oracle. It has passed Microsoft.

**The row's limit, stated [E3-61]:** the row shows position, not conduct. Whether five
companies with the same capacity behave like "a demented Kellogg" is not readable from it.

### [E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT?

**Two answers, because there are two moats.**
- **Search's moat is DEFENDED, not replaced** — habit, index, brand, the query stream.
  [E5-23] prescribes continuous defence for every moat and [E3-49] calls maintenance "a
  permanent obsession"; TAC and R&D defend *the same* advantage. **Permitted.**
- **The delivery layer's basis MUST BE REPLACED.** The answer engine displacing ten blue
  links runs on accelerators carried at a **six-year** accounting life inside a two-to-three
  year silicon generation. Capital spent in 2026 buys capacity, not a durable position; the
  fleet must be bought again. **That is the excluded class**, and [E3-51]'s surfing image is
  the right one — the wave is real and long, but the advantage lives in the wave.

**Does success depend on a great manager? No** — [E4-23] passes. Search prospered under
Page, then Pichai, through a founder handover and a holding-company restructuring. [E2-53]'s
dominance class fits: position, not execution, sets the economics.

**[E3-33] / [E4-37] untapped pricing power — and the filed evidence says it is being USED,
not left on the table.** Cost-per-click has risen four straight years (+1%, +7%, +7%, and
+5%/+3% in 2026) *while* click volume accelerated to +13%. That is the yawn end of [E4-37]:
no agony, no prayer session, price and volume rising together. **[E5-28]'s scope test is
satisfied honestly — a court has adjudicated Alphabet a monopolist in general search, so the
near-monopoly claim is not mine, it is a finding of fact.**

- Peers named: **5** of the industry's ~6 real competitors *(Samsung, Baidu, Alibaba and
  ByteDance are outside SEC reach — stated, not stretched; the row is not held PROVISIONAL
  because all five US-listed participants at scale were obtained)*.
- Class: **[x] NARROW** · Direction: **MIXED, and the two halves are separable** —
  **WIDENING** at Search on the physical series (units +13%, price +7%) and on segment
  margin; **NARROWING** on criterion 3 (four jurisdictions with orders in force), on Cloud
  (third of three), and on capital intensity (capex/D&A 2.40x → 5.25x in five years).

**VERDICT: [x] IN (NARROW).** Criterion 3 fails and the class is capped, not destroyed
[E2-59]; the cap is priced at Q5 [E2-63]. Recorded as a moat defect at Q2, not as a Q3
finding: **the most profitable franchise in the world does not set the terms on which it is
distributed, and since 2019-10-29 it has not filed what that distribution costs.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**NONE TICKED → Q3 IS A QUALITATIVE OVERLAY.** Case declared:

- **Daily execution — argued at length and REFUSED, on the largest natural experiment
  available.** Alphabet has failed publicly and repeatedly at the things that were supposed
  to be adjacent to Search — Google+, Glass, Stadia, the Nest and Motorola write-downs, a
  decade of losing hardware, and **$48,750M of cumulative Other Bets operating losses since
  2013** — and Search's paid clicks were +13% in the last filed quarter regardless. That is
  [E5-18]'s *"capacity to stand it"* and [E2-53]'s dominance class demonstrated over twelve
  years: position, not execution, sets the economics.
- **Control — no.** Marketable security, exit available daily.
- **Leverage — no, and the direction is the finding rather than the level.** Long-term debt
  $46,547M at 2025-12-31 and **$98,165M at 2026-06-30** against **$640,480M** of equity.
  Small asset errors do not destroy this equity. But debt was **$4,685M in FY2019**, so the
  balance sheet is being rebuilt at speed, and that is a Q4 item, not a Q3 gate.

**Q3 therefore records findings and cannot stop this run on its own. It also cannot promote
it — the guardrail below is checked.**

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."*

**THE ADJUDICATED FACTS, AND THE RULING THE BRIEF ASKED FOR.** Alphabet is an adjudicated
monopolist. Dated to when each became public: EC Shopping **2017-06**; EC Android
**2018-07**; EC AdSense **2019-03** (*annulled 2024-09*); *US v. Google* Search liability
**2024-08**, **final judgment 2025-12**; *US v. Google* Ad Tech liability **2025-04**,
remedies argued 2025-11, judgment awaited; EC ad tech **2025-09**; Epic verdict **2023-12**,
remedies **2024-10**, appeal denied **2025-07**; JFTC **2025-04**; ACCC **2025-08**.

**Ruling: these are an INDUSTRY-REGIME DISPUTE ABOUT CONDUCT, NOT AN INTEGRITY FINDING —
and the reasoning is stated so it can be checked, because [E5-22] cuts both ways.** What has
been adjudicated is that certain *contracting practices* — exclusive defaults, tying,
self-preferencing between owned auction sides — unlawfully maintained monopolies. **No
filing in eleven vintages discloses a restatement, a fraud finding, an officer disciplined
for dishonesty, or a self-dealing finding.** [E5-16]'s "personal misconduct" is not what a
Sherman Act §2 judgment establishes. [E5-22] forbids reading penalty size as seriousness in
either direction, and its actual test is *"they didn't act when they learned"* — on that
test Alphabet paid $3.0bn on Shopping, **$5.2bn cash on Android in July 2026**, took a
**$3.5bn** charge on EC ad tech within one quarter of the decision, and implemented the
Android changes as directed. It acted.

**The honest limit, recorded rather than smoothed:** I have not obtained the D.D.C. opinion's
findings on document-retention and chat auto-deletion, which several accounts place in the
2024 liability opinion and which would sit closer to an integrity question than to a
conduct-regime one. **That is UNRESEARCHED, artifact named: the August 2024 memorandum
opinion in *US v. Google LLC*, No. 1:20-cv-03010 (D.D.C.), on the public docket.** It does
not change this verdict — a spoliation finding is a litigation-conduct matter, and the
framework's flags are *"accounting and disclosure, not litigation"* — but it is the one
stone left unturned and it is named here rather than left out.

**STEP 2 — THE FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each is a
prompt to READ, never a verdict.*

- [x] **weak accounting — FIRES, AND IT IS THE USEFUL-LIFE RECORD.** See Q4's (c) section.
      **FIVE distinct useful-life movements FY2015–FY2025, of which THREE ARE UNLABELLED and
      visible only by diffing Note 1 across vintages** — the identical shape the MSFT run
      found. The largest unlabelled one is **buildings "seven to 25 years" → "seven to 40
      years" in FY2024**, a 60% extension of the ceiling, with **no heading, no dollar
      effect, no rationale, and exactly one occurrence of "40 years" in the whole document.**
      And the disclosure **decayed to nothing**: "Change in Accounting Estimate" appeared in
      Item 7 in FY2020, FY2021, FY2022 and FY2023 and **has not appeared in an Alphabet 10-K
      since** — it vanished in the very vintage the buildings ceiling moved.
- [ ] unintelligible footnotes — **no.** The notes are unusually plain.
- [ ] trumpeted earnings projections — **no. "guidance" = 2 occurrences in the FY2025 10-K,
      both meaning OECD/tax regulatory guidance. Alphabet issues no earnings guidance in any
      filing.**
- [x] **serial share issuance [E5-15] — FIRES ON THE FORM, IN 2026, AND THE RUN STATES BOTH
      READINGS.** In four days of June 2026 Alphabet raised **$20.5bn** (public offering, 29M
      Class A at $355.1982 + 29M Class C at $351.8018), **$10.0bn** (private placement), and
      **$19.0bn** (6.25% mandatory convertible preferred) = **$49.5bn**, and on 2026-06-01
      opened a **$40bn at-the-market program**. Against it: [E5-15]'s tell is
      *promotion-minded* issuance, and this is capital-expenditure funding by a company that
      simultaneously **stopped repurchasing stock entirely**. See the [E5-24] finding below,
      which runs strongly the other way.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — DOES NOT FIRE. Recorded sweep of the
      FY2025 10-K: "EBITDA" 0 · "non-GAAP" 0 · "pro forma" 0 · "constant currency" 0 ·
      "free cash flow" 0 · "consecutive" 0.** "adjusted" 6 and "except for" 4, every one of
      the ten incidental accounting boilerplate ("Adjusted Cost" column headings, "except for
      per share information"). **ZERO management-defined non-GAAP performance measures.** On
      a par with MSFT (EBITDA 0 in eleven vintages) and AAPL. And [E2-57] does not fire:
      "consecutive" = 0 — **Alphabet does not boast of streaks.**
- [ ] **filed-figure tells [E4-30] — DO NOT FIRE, AND THE CASH-TAX TELL RUNS THE SAFE WAY.**
      Effective rate **13.9% (2023) → 16.4% (2024) → 16.8% (2025)** — *rising*, the opposite
      of the fraud shape. Reported growth is **not** smooth: net income fell in FY2017 and
      FY2022; operating income fell in FY2022.
- [x] **[E2-49] METRIC-SWITCHING — FIRES THREE TIMES, ALL DATED, AND IT IS THE STRONGEST
      FLAG IN THE FILE.** *"Yardsticks seldom are discarded while yielding favorable
      readings."*
      1. **Aggregate and Network paid-click/CPC series** — last filed FY2017 10-K
         (2018-02-06), first omitted Q1-2018 10-Q (2018-04-24), **77 days**, no reason.
         Network CPC had been negative in **all four** years ever filed; aggregate CPC
         negative and worsening in all four.
      2. **The TAC split** — last filed Q3-2019 10-Q (2019-10-29), first omitted FY2019 10-K
         (2020-02-04), **98 days**, no reason. The withdrawn distribution-partner rate had
         **risen every year it was ever filed, 7.8% → 13.3%**; the surviving aggregate rate
         falls on mix.
      3. **Every named competitor in Item 1** — last filed FY2021 10-K (2022-02-02, **26
         companies, 44 mentions, Apple named 4 times**), first omitted FY2022 10-K
         (2023-02-03), **366 days**, no reason. **Alphabet now names zero competitors.**
      **All three withdrawals removed the number that was deteriorating and kept the one that
      was not. None carries a filed explanation. "no longer" = 0 hits.**
- [x] **[E2-52] dividends funded by issuance — FIRES LITERALLY, ON H1-2026's FILED NUMBERS.**
      *"Beware of 'dividends' that can be paid out only if someone promises to replace the
      capital distributed."* H1-2026: OCF $84,859M − capex $80,598M = **$4,261M**, against
      **$5,231M** of common dividends and $86M of preferred dividends. **Alphabet did not
      cover its own dividend out of cash flow after capital expenditure in the first half of
      2026, and raised $49.5bn of equity and preferred in the same half.**

**STEP 3 — THE PRIMARY TEST [E2-01].** *"a high earnings rate on equity capital employed
(without undue leverage, accounting gimmickry, etc.) and not … consistent gains in EPS."*

Return on ending equity, FY2016–FY2025, filed:

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| 14.0% | 8.3% | 17.3% | 17.0% | 18.1% | 30.2% | 23.4% | 26.0% | 30.8% | **31.8%** |

**PASSES — and then the run refuses part of its own denominator and numerator, because
[E2-01] says "without accounting gimmickry" and two adjustments are required.**
1. **Non-operating gains are a rising share of the numerator.** FY2025 net income of
   $132,170M contains **$24,620M** of "Loss (gain) on debt and equity securities, net". On
   after-tax operating income the FY2025 return is **25.9%**, not 31.8%.
2. **H1-2026 makes the reported figure unusable.** Six-month net income **$174,771M** against
   operating income of **$80,466M** — *"Other income (expense), net"* was **$135,699M**, of
   which **$97,983M in Q2 alone**. **More than three-quarters of Alphabet's reported H1-2026
   net income is non-operating.** [E4-41] requires favourable exogenous breaks to be named
   and removed before the mean is trusted; this is the largest such break the queue has met.
   **Any ROE, EPS or P/E computed on Alphabet's 2026 reported earnings is meaningless.**
3. **[E2-43] tangible denominator:** goodwill is only $33,380M against $415,265M of equity
   (8.0%), so the goodwill wedge is immaterial here — unlike the AAPL/MSFT cases. Return on
   tangible equity FY2025 = 34.6%.

**Equity grew +65% from FY2021 to FY2025 ($251,635M → $415,265M) while net income grew +74%
— but the incremental return on the four years' retained capital is the [E2-56] test below,
and it does not hold up.**

**The half-owner test [E2-26]** — *does this reporting tell me what I would want to know if
the positions were reversed?* **SPLIT, AND BOTH HALVES ARE LARGE.**

**Passes, and generously:** it publishes Google Network impressions at **−12%** — the ugly
series — while its rival Microsoft files no unit series at all; it quantified both labelled
life changes with dollars, net income *and* EPS; it discloses **$15.6bn (2025-12-31), rising
to $17.4bn (2026-06-30)** of accrued legal fines as a named line; it files the segment
operating losses of **Other Bets ($7,515M)** and **Alphabet-level activities ($16,760M)**
rather than burying them; it discloses that it *lost* the AdSense fine on appeal; and the
FY2025 10-K added a footnote — absent in FY2024 — saying *"approximately 60% of technical
infrastructure assets were comprised of servers and network equipment"*, which is the single
most useful sentence in the document for an outside analyst and was volunteered.

**Fails, and in one specific place:** **the price of distribution.** Three separate
withdrawals have removed, without explanation, the ability of an owner to see what Alphabet
pays for the scarce input Q1 named. And **Alphabet does not disclose segment capital
expenditure after FY2019, segment assets in any vintage, or segment depreciation ever** —
its own 10-Ks say the CODM *"does not evaluate operating segments using asset information"*.
**The consequence is that return on capital by segment is not computable from any Alphabet
filing. That is UNKNOWABLE, not UNRESEARCHED — the document does not exist.**

### [E2-56] THE PRO-AM TEST — the brief's Other Bets question, answered

*"Their marvelous core businesses … camouflage repeated failures in capital allocation
elsewhere"* — judge retention **segment-by-segment, incrementally, never on the blended
return.**

**Cumulative Other Bets operating losses, FY2013–FY2025: $48,750M.** Add **Alphabet-level
activities, FY2021–FY2025: $40,871M** (where DeepMind and frontier-model R&D were moved in
2023). **Combined: $89,621M of cumulative disclosed operating losses**, running at
**$24,275M in FY2025 alone** — and Other Bets *revenue* **fell 6.7%** in FY2025, to $1,537M.

**BUT THE GRMN SHAPE DOES NOT REPEAT, AND THIS IS A CANDOUR PASS.** GRMN's auto-OEM segment
ran six loss years hidden inside a blended 18.5% ROE. **Alphabet publishes both loss lines,
by segment, every year.** The losses are camouflaged in the *consolidated margin* — 32.03%
conceals a 40.68% business subsidising a −489% one — but they are not camouflaged in the
*disclosure*. An owner who reads the segment note can see every dollar.

**The incremental return, and it does not survive the split:**

| | |
|---|---|
| consolidated operating income, FY2021 → FY2025 | $78,714M → $129,039M = **+$50,325M** |
| cumulative capex FY2022–25 | **$207,718M** |
| **consolidated incremental pre-tax return** | **24.2%** |
| — of which **Google Services** | **+$51,272M** — the whole of it |
| — **Google Cloud** | +$16,192M |
| — **Alphabet-level activities** | **−$13,675M** |
| — **Other Bets** | **−$3,464M** |

**The annuity added more than the entire consolidated gain; the two capital sinks together
subtracted $17,139M.** If the $207.7bn of capital is attributed to the legs that consumed it,
the incremental pre-tax return on the AI-datacentre capital is **7.8% (Cloud alone) or 1.2%
(Cloud net of Alphabet-level)** — against [E5-40]'s ~12% "quite satisfactory". **This is the
MSFT finding replicated at Alphabet: the segment that added the profit is not the segment
that consumed the money.**

**And the attribution cannot be closed, which is itself the finding.** Alphabet stopped
filing segment capex after FY2019 and has never filed segment assets or depreciation.
**UNKNOWABLE from filings.** Google Services also runs on the same infrastructure, so
"essentially no capital" overstates the case — but nothing in any Alphabet document permits
a better split, and MSFT's run *could* do this test because Microsoft files segment
cost-of-revenue. Alphabet does not.

**THE SHARPEST SINGLE FACT, FROM ALPHABET'S OWN MD&A.** Google Cloud went from a **$1,922M
operating loss (FY2022) to a $1,716M operating profit (FY2023)** — a $3.6bn swing — in the
same year a **$3.9bn** depreciation benefit from the server life extension was booked, and
Alphabet's own FY2023 MD&A names the life change as a driver of exactly that segment's turn:
*"Google Cloud operating income of $1.7 billion for 2023 compared to an operating loss of
$1.9 billion for 2022 … operating income benefited from a reduction in costs driven by the
change in the estimated useful lives of our servers and certain network equipment."*
**Alphabet does not disclose the segment split of the $3.9bn. Whether Google Cloud's maiden
operating profit is an artefact of the life extension cannot be closed from any filed
document.**

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] **resists any change in current direction — NO.** It changed hard and fast.
- [x] **projects/acquisitions materialise to soak up available funds — YES.** $48.75bn of
      cumulative Other Bets losses on $1.5bn of annual revenue, and a capex line that
      absorbed 103% of the increase in operating cash flow in H1-2026.
- [ ] staff studies produced to justify the leader's craving — **not observable from filings.**
- [x] **peer behaviour mindlessly imitated — YES, EMPHATICALLY, AND IT IS DATABLE.** Four
      hyperscalers extended server lives inside thirty months (MSFT eff. Jul 2022; **GOOGL
      eff. Jan 2023**; AMZN; ORCL), and all five of the companies in the Q2 competitor row
      raised capex/revenue sharply in the same eighteen months. **[E2-27] is the verdict:
      *"viewed individually … cost-effective and rational; viewed collectively, the decisions
      neutralized each other and were irrational."*** And the counter-example is on the
      record: **Amazon REVERSED, shortening a subset of servers 6→5 years effective January
      2025** for the filed reason *"the increased pace of technology development, particularly
      in the area of artificial intelligence and machine learning."* **Alphabet has not
      re-tested.**

**Capital allocation — the two buyback conditions [E5-08]:**

- **(1) ample funds for operations and liquidity? — NO, ON THE LATEST FILED HALF-YEAR.**
  OCF less capex was **$4,261M** in H1-2026 against $5,317M of dividends. Condition 1 is not
  met today, and the company's own behaviour concedes it: it stopped repurchasing.
- **(2) repurchases at a material discount to conservatively calculated IV? — FAILED IN
  FY2024 AND FY2025, PASSES BY CESSATION FROM 2026.** Average price paid rose monotonically
  **$37.22 (2015) → $60.12 (2019) → $123.52 (2021) → $164.17 (2024) → $190.45 (2025)**,
  $347,944M spent over eleven years at a blended **$107.40**. Against this run's Q5 value
  range, the FY2024–25 purchases at $164–190 were above value.
- **BUT [E5-24] IS OBEYED MORE EMPHATICALLY THAN BY ANY NAME IN THIS QUEUE, AND THE RUN SAYS
  SO AGAINST ITS OWN DIRECTION OF TRAVEL.** *"What is smart at one price is dumb at another."*
  Alphabet **bought least, at its highest-ever price, in the last year it bought at all
  (240M shares at $190 in FY2025, down from 528M at $116 in FY2023) — then STOPPED
  COMPLETELY.** Verbatim, Q2-2026 10-Q: *"In the three and six months ended June 30, 2026,
  there were no repurchases of the company's Class A or Class C shares."* **$69.5 billion of
  the $70.0 billion April-2025 authorization remains unused.** Four months later it **sold**
  new stock at $355.1982/$351.8018. **On the raw arithmetic that is buying low and selling
  high, and it is the [E2-51] refusal test passing in the right direction.** Whether it was
  intended as price discipline or forced by the capex bill, the filings do not resolve —
  and the run does not pretend to know.
- **THE BUYBACK ARITHMETIC AN OWNER SHOULD ACTUALLY CARE ABOUT.** $347,944M retired 3,240M
  shares, yet the count fell only 1,659M, 13,747M → 12,088M. **Just under half of every
  buyback dollar — roughly $170bn over eleven years — bought standing still against stock
  compensation.** Net per-share accretion: **12.07% over eleven years, ~1.16% a year.**
  From 2015 to 2018 Alphabet spent **$19.4bn** on buybacks and the share count went **UP
  every single year.** And the count has now risen **142 million shares (+1.17%) in six
  months**, before 42.8–54.0M of contracted mandatory-convertible dilution by May 2029 and
  the $40bn ATM.
- **SBC is the other half of that story.** $24,953M in FY2025 (6.2% of revenue, **15.1% of
  operating cash flow**); H1-2026 $14,708M, **+27.7% year on year**. Plus **$14,167M of cash
  paid to taxing authorities on net share settlement**, which sits in FINANCING and is
  therefore *outside* both the buyback line and operating cash flow. **[E3-70] recorded: the
  reported charge is the floor of the subtraction, not the measure.** And the new $40bn ATM
  states its purpose verbatim — *"primarily intended to be used to meet tax obligations
  associated with employee equity grants"* — i.e. **proposing to fund with new equity a cost
  funded from operating cash for a decade.** Nothing drawn yet.
- **CAPITAL ALLOCATION FLAG: LIVE, with the humility clause [E4-13]** — it rests on this
  run's own IV range and management knows the business better than I do. **Binds position
  size, never the discount rate.**

**[E2-60] RESTRICTED EARNINGS — FIRES.** *"restricted earnings are those whose payout costs
the business … its financial strength"*; *"where leverage rises to fund the payout, (c) was
understated."* Alphabet returned **$347,944M of buybacks + $17,412M of dividends** across the
window while taking long-term debt from **$4,685M (FY2019) to $98,165M (2026-06-30)** and
issuing **$49.5bn of equity and preferred in June 2026**. The capital returned in FY2023–25
is being replaced by capital raised in FY2025–26.

**[E4-52] LOLLAPALOOZA — RUN EXPLICITLY, AND RECORDED AS PARTIALLY FIRED.** Six disclosure
choices converge in one direction: three metric withdrawals, five life movements of which
three are unlabelled, the disappearance of the "Change in Accounting Estimate" heading in the
vintage the buildings ceiling moved 25→40 years, the absence of segment capital data, and
the absence of any named competitor. **But the candour record is large and runs the other
way** — published segment losses, published −12% impressions, quantified fines and a
disclosed appellate loss, a volunteered 60%-of-technical-infrastructure footnote, and no
non-GAAP measure anywhere. **[E2-30] and [E5-38] govern: institutional dynamics, not venality
— and a fired flag is not a venality finding.**

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: nothing in this Q3 promotes the name. The [E5-24] buyback discipline is
      recorded as a finding and is **not** used to repair Q2 or substitute for Q4
      **[E2-37, E2-38, E3-39]**.
- [x] This business does **not** require a great manager; recorded at Q2 as a franchise
      strength under [E4-23]/[E2-53], not here as a compliment to the people.
- [x] No great-manager case is being made, so [E2-35]/[E2-36] does not arise.

- **VERDICT: [x] IN — as an OVERLAY, meaning NO DISQUALIFIER FOUND.**
  *Not a finding that the managers are honest — "sincerity and empathy can easily be faked"
  **[E5-17]**, and [E5-32] adds that the filed statement is not bedrock. **IN never
  promotes.** Live flags carried forward: [E2-49] metric-switching ×3; weak accounting on the
  unlabelled life movements; [E2-52] dividends not covered in H1-2026; [E2-60] restricted
  earnings; [E5-08] condition 1 failing and condition 2 having failed in FY2024–25; [E2-30]
  two of four. Open work order, named: the **August 2024 D.D.C. memorandum opinion** and the
  **2026 DEF 14A** pay-versus-performance table — neither obtained, neither capable of
  changing an overlay verdict that rests on eleven read 10-K vintages.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**

**Owner earnings by year, OCF − SBC − (c), (c) = capex + finance-lease ROU additions:**

| | 2016 | 2018 | 2020 | **2021** | 2022 | 2023 | 2024 | **2025** | **TTM** |
|---|---|---|---|---|---|---|---|---|---|
| **OE strict** | 19,121 | 13,479 | 29,852 | **51,636** | 40,071 | 46,471 | 49,666 | **46,707** | **23,224** |
| OE at deprec. end | — | — | — | 66,003 | 58,658 | 67,340 | 87,203 | 118,624 | 132,291 |
| capex / deprec. | — | — | — | 2.40x | 2.34x | 2.70x | 3.43x | **4.33x** | **5.25x** |
| capex / revenue | 11.3% | 18.4% | 12.2% | 9.6% | 11.1% | 10.5% | 15.0% | **22.7%** | **29.7%** |

*(Full 13-year series in `_research 2026-09-06 GOOGL/E1-owner-earnings.md`. TTM = FY2025 −
H1-2025 + H1-2026 from the Q2-2026 10-Q, acc. 0001652044-26-000071.)*

- **Short-window mean** (3-yr FY2023–25): **47,615**
- **Long-window mean** (13-yr FY2013–25): **27,647**
- Corpus-default window (5-yr FY2021–25 **[E2-42]**): **46,910**
- also: 8-yr **37,258** · 10-yr **33,341** · **TTM 23,224**
- **Spread across MY OWN windows at the strict end alone: 23,224 → 47,615 = 105%.**
- **Combined range (window spread × capex band): $23,224M to $132,291M — a 5.7x width.**

### THE SCREEN REPRODUCES EXACTLY — AND THE FOURTH SPREAD DEFECT BITES ANYWAY

`2026-09-02 MASTER RUN QUEUE (corrected).csv`: `GOOGL,…,4097294,46910,91056,0.941,0.0114,…`

- **oe_bottom 46,910 = my 5-yr FY2021–25 strict mean, 46,910.2.** ✓ *Reproducing it required
  finding that `capital_acquired()` adds finance-lease ROU additions to cash capex — capex
  alone gives 47,522.2, which is not the screen number. The same trap the MSFT run recorded.*
- **oe_top 91,056 = my 3-yr FY2023–25 depreciation-end mean, 91,055.7.** ✓
- spread 0.941 = (91,056 − 46,910)/46,910. ✓ · yield 0.0114 = 46,910/4,097,294. ✓

**BOTH ROWS REPRODUCE TO THE MILLION — AND THE 94.1% IS STILL WRONG, WHICH IS EXACTLY WHAT
`spread_caveat` NOW WARNS.** The screen computes four constructions (3y/5y × two capex ends)
and **cannot see variation older than five years.** My six windows at **one** end already span
105%; every construction together spans **470%.** The screen understates the true width by
about five times, and it understates it in the flattering direction, because a narrow spread
reads as well-determined. **[E4-25] says the width IS the finding, so this is not a small
error — it is the AAPL finding replicated at a second name in the same week.**

**A wide spread is also a Q4 finding [E5-11] — name the distortion.** Two, and they run
opposite ways. **(1) The business changed character inside the window:** capex went from
$24,640M (FY2021) to a **$161bn annualised run-rate** (H1-2026 × 2), so the 5-year mean
averages a company that spent 9.6% of revenue on capital with one that spends 29.7%. **(2)
FY2021 was a COVID-advertising peak** at the front of that window. Averaging through 2026 is
what [E4-38] warns about — *"a calculated selection of either initial or terminal dates"* —
so **every window is published above rather than one chosen.**

### MAINTENANCE CAPEX — THE DISCLOSED JUDGMENT, AND THE BRIEF'S HYPOTHESIS (b) IS REFUTED

The brief allowed that Alphabet's capex might be better matched to depreciation than
Microsoft's, in which case the honest owner-earnings number would be much higher. **It is the
reverse, and the measurement is not close.**

| | **GOOGL TTM** | MSFT FY2026 | [E5-20] railroads |
|---|---|---|---|
| capex ÷ depreciation | **5.25x** | 3.38x | — |
| **depreciation as a share of total capex** | **19.1%** | 33% | **">higher than 60 percent"** |
| capex ÷ revenue | 29.7% | 34.9% | — |

**THE D&A END IS INVALID [E5-20], PROVEN THREE WAYS.**

**(i) The ratio.** Capex ran 9.6–12.2% of revenue and 2.3–2.7x depreciation through FY2023 —
[E3-44]'s default class. It is now 29.7% and **5.25x**. [E5-20] requires >60% of total capex
for the railroad exception; **Alphabet's depreciation charge is 19.1% of what it is actually
spending.** It is *further* outside the default class than Microsoft.

**(ii) The denominator has been lengthened by management judgment — FIVE times, three of them
unlabelled.** From `A1-useful-lives.md`, every vintage diffed:

| # | effective | asset | from | to | labelled? | $ effect filed? |
|---|---|---|---|---|---|---|
| 1 | FY2016 | information technology assets | "two to five years" | **"up to 7 years"** | **NO** | **NO** |
| 2 | FY2018 | IT assets — a **SHORTENING** | "up to 7 years" | "three to five years" | **NO** | **NO** |
| 3 | **Jan 2021** | servers 3→4 yr; certain network equipment 3→5 yr | 3 | 4 / 5 | YES | **YES — $2.6bn** |
| 4 | **Jan 2023** | servers 4→6 yr; certain network equipment 5→6 yr | 4 / 5 | 6 | YES | **YES — $3.9bn** |
| 5 | **FY2024** | **data center and office BUILDINGS** | "seven to 25 years" | **"seven to 40 years"** | **NO** | **NO** |

**MSFT's run found four where the brief named two; Alphabet's has FIVE.** Change 5 is the
largest and is invisible except by diff: a **60% extension of the building life ceiling**, in
a vintage that simultaneously **rebuilt the entire PP&E taxonomy** (land/buildings/IT assets/
CIP → technical infrastructure/office space/corporate and other/assets not yet in service),
so the reader is comparing across a relabelled taxonomy. Verification: **"40 years" returns
exactly one hit in the FY2024 10-K** — the policy sentence — and **"Change in Accounting
Estimate" returns zero.**

**The disclosure decayed to nothing, and it decayed in the same vintage:** the heading
appeared in Item 7 in FY2020, FY2021, FY2022 and FY2023 and **has not appeared in an Alphabet
10-K since.** [E2-49] fires. **And both times a benefit was guided, the outturn exceeded it —
$2.1bn guided / $2.6bn delivered; $3.4bn guided / $3.9bn delivered.**

**No rationale is filed for any of the five.** For 3 and 4 the filed reason is a bare
assertion of process — *"we completed an assessment of the useful lives"* — with no inputs, no
observed service life, no utilisation data. **Alphabet elevated useful lives to a Critical
Accounting Estimate for the first time in FY2024 — after both labelled changes were made.**

**(iii) BUILD (c) FORWARD FROM THE FILED GROSS BOOK AT MANAGEMENT'S OWN LIVES** — the MSFT
method, and the FY2025 10-K volunteered the sentence that makes it possible: *"approximately
60% of technical infrastructure assets were comprised of servers and network equipment."*

| bucket | gross, in service | management's own life | annual charge |
|---|---|---|---|
| servers and network equipment (60% of technical infrastructure) | $122,207M | **6 years** | **$20,368M** |
| data center land and buildings (40%) | $81,472M | 7–40 yr, at 20 | $4,074M |
| office space | $48,348M | 7–40 yr, at 20 | $2,417M |
| corporate and other | $14,463M | 2–25 yr, at 13 | $1,113M |
| **subtotal on the in-service book** | **$266,490M** | | **$27,972M** |
| **assets NOT YET in service** — capital already spent, not yet depreciating | **$78,592M** | | **+$9,431M** |
| **FORWARD (c) RUN-RATE ON CAPITAL ALREADY SPENT** | | | **~$37,400M** |

**Alphabet's FY2025 reported depreciation of $21,136M is 57% of the depreciation run-rate
implied by its OWN lives on the book it has ALREADY bought.** *(At the 40-year building
ceiling the build is $24,726M + $9,431M = $34,157M; reported is still only 62%. The land
component of technical infrastructure and office space is not separately disclosed and is not
depreciated, so this build is modestly overstated — an honest limit, and it does not close
the 57–62% gap.)*

**Where the MSFT case converged, Alphabet's does not, and the divergence is the finding.**
Microsoft's forward build ($50,660M) landed almost exactly on its 5-year mean capex
($55,394M) — two independent constructions agreeing on total capex. **Alphabet's forward
build (~$37,400M) sits BELOW its 5-year mean total capital spending ($47,084M) and far below
TTM total capital spending ($134,304M).** The gap is growth capital. So Alphabet's (c) is
genuinely bounded below by ~$37bn and above by ~$134bn, and the run must choose openly.

**THE JUDGMENT, AND WHY IT SITS AT TOTAL CAPITAL SPENDING [E2-23].** (c) is what the business
*"requires to fully maintain its long-term competitive position and its unit volume"* — not
merely to replace worn assets. Three filed facts decide it:
1. **Alphabet's own FY2025 10-K, verbatim:** *"The costs associated with operating our
   technical infrastructure — depreciation, energy, equipment, and network capacity — are
   expected to **significantly increase** as developing and serving AI offerings require more
   compute power than our historical consumer and enterprise offerings"*, and *"in 2026, we
   expect to **significantly increase**, relative to 2025, our investment in our technical
   infrastructure."*
2. **$707.0bn of long-term supply agreements to secure future production capacity, generally
   fulfilled through 2030** (Q2-2026 10-Q Note 10). **Alphabet has contractually removed its
   own option to spend less.** Committed spending is not discretionary growth capital.
3. Four rivals are building the same capacity simultaneously; the Q2 row shows all five
   raising capex/revenue together. In that setting, *not* spending is a competitive-position
   decision, which is precisely what (c) is defined to cover.

- **(c) judged at TOTAL CAPITAL SPENDING INCLUDING FINANCE LEASES**, 5-year mean **$47,084M**
  — the corpus-default window [E2-42].
- **Band carried: $23,224M to $132,291M.** Judged owner earnings **$45,000M**, and the run
  states plainly that this is **the generous end of the defensible range**: the live TTM
  reading is $23,224M, roughly half, and every window longer than five years is lower.
- **Stock compensation subtracted in full [E5-06]: $24,953M (FY2025), $28,147M TTM.**
  **[E3-70] recorded and NOT stacked** — a further **$14,167M** of cash was paid to taxing
  authorities on net share settlement in FY2025 and sits in *financing*, so it is outside both
  OCF and the buyback line. Taking it would cut FY2025 owner earnings to ~$32,540M. It is
  disclosed here and declined, so conservatism is spent once.

### THE FACT THE FILE TURNS ON

> **Owner earnings at the strict end peaked at $51,636M in FY2021 and are $23,224M on the
> latest twelve months — DOWN 55%, or −16.27%/yr — while revenue over the same span rose
> 73%, from $257,637M to $445,866M, and operating income rose +13.15%/yr.**

That is the MSFT shape (−44% in four years) **deeper and faster.** All of the apparent growth
lives in the gap between the two ends: on the construction this run calls INVALID, owner
earnings grew **+16.71%/yr** over the identical period.

**Is the range too wide to reach a conclusion [E4-25]? NO — and the reasoning is the MSFT
adjudication.** [E4-25] closes a file when the range **straddles the answer.** This one
straddles nothing: at a cap of $4,141,000M the yields run **0.56% / 0.67% / 0.81% / 0.90% /
1.09% judged / 1.13% / 1.15% / 2.20% / 2.47% / 3.19%** — and **every construction, on every
window, at both ends, is below the 5.24% sovereign.** The most generous number constructible
— the best twelve months in Alphabet's history, valued as though a twice-lengthened
depreciation charge covering 19% of current spending fully replaces the fleet — still pays
**2.05 points LESS than a government bond.** The width is real, it is a genuine Q4 finding,
and it changes no verdict.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [x] **good — attractive return, earned also on added capital**
- [ ] gruesome — grows, eats capital, earns little

**Evidence, and the two halves point different ways — which is what "good" means.**
- **The base is GREAT.** Google Services earns a **40.68%** operating margin on $342,721M of
  revenue, with paid clicks +13% and cost-per-click +7%. Goodwill is only 8.0% of equity, so
  the [E2-43] denominator is nearly all real: FY2025 operating income of $129,039M against
  roughly $280–300bn of net tangible operating assets is a **~43–46% pre-tax return.**
- **The marginal dollar is NOT.** [E2-56] above: the incremental pre-tax return on the
  FY2022–25 capital is **7.8% (Cloud alone) or 1.2% (net of Alphabet-level)** against
  [E5-40]'s ~12%. Consolidated it is 24.2%, and the whole of that gain came from the segment
  that consumed almost none of the money.
- **[E4-43] governs the verdict: the good class PASSES.** *"nothing shabby about earning $82
  million pre-tax on $400 million of net tangible assets."* Only gruesome fails Q4. **Good
  ranks below great at Q5, and that is all.**
- **Direction: travelling toward the gruesome description on the marginal dollar** — *"grows
  rapidly, requires significant capital to engender the growth, and then earns little"* is a
  fair description of Google Cloud plus Alphabet-level activities taken alone, and those are
  where the $707bn is committed. **Not yet true of Alphabet. Watch it at Q6.**

### Staying power — score all three **[E5-11]**

- **(1) large and reliable stream of earnings — PASS, emphatically.** Revenue $402,836M
  (+15%), operating income $129,039M, OCF $164,713M and $185,675M TTM. Twelve consecutive
  years of revenue growth.
- **(2) massive liquid assets — PASS, with the source named.** Cash and marketable securities
  **$242,474M** at 2026-06-30, up from $95,657M at FY2024. **But it is borrowed:** long-term
  debt rose $87.3bn over the same eighteen months, so net cash is ~$144bn, and the FY2020–24
  trend was *down* ($136.7bn → $95.7bn) as buybacks absorbed it. Also $131,461M of
  non-marketable securities, which are **not liquid** and are not counted here.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAIL. This is the third strength, the
  one [E5-11] says usually kills, and it is the largest such number the queue has recorded.**

> **Purchase commitments and other contractual obligations: $55.4bn (2024-12-31) → $149.1bn
> (2025-12-31) → $811.0 BILLION (2026-06-30), of which $200.7bn is short-term.**

  Q2-2026 10-Q Note 10, verbatim: *"expected future fixed or guaranteed commitments under
  these agreements were **$707.0 billion**, the significant majority of which related to
  **long-term supply agreements** … generally … fulfilled **through 2030**. The energy service
  agreements include terms ranging from two to 26 years, with obligations **through 2054**,
  and generally include **take-or-pay provisions** for minimum quantities of energy supply and
  **substantive termination fees**."*

  **Twelve-month fixed claims at 2026-06-30:** short-term purchase commitments **$200,700M** +
  current long-term debt $1,999M + drawn credit facilities $1,300M + short-term lease
  commencing Q3-2026 $5,800M + common dividends ~$10,700M + preferred dividends ~$1,188M +
  short-term accrued legal fines **$17,400M** = **~$239,100M.**
  Against liquidity of **$242,474M**: **1.01x on liquid assets alone.** Adding a full year of
  operating cash flow ($185,675M): **1.79x.**
  *(The short-term purchase commitments substantially ARE the next year's capex, so they are
  not additive to capex — the Apple self-liquidating shape. Stated so the coverage is not
  double-counted in either direction.)*

  **This clears more comfortably than Microsoft's did** — MSFT cleared $241.9bn by $17.8bn;
  Alphabet clears $239.1bn by $189bn. **The failure is not the twelve months. It is the four
  years:** ~$707bn of supply commitments fulfilled generally through 2030 is roughly **$175bn
  a year against ~$186bn a year of operating cash flow.** That leaves essentially nothing for
  dividends, buybacks, or anything else — which is precisely what H1-2026 already shows.

  **Off-balance-sheet total, my addition of separately filed narrative figures (items may
  overlap; an order-of-magnitude marker, not a number to compute with): ~$941bn** — purchase
  commitments $811.0bn + leases not yet commenced **$85.2bn** + the $5.8bn short-term lease +
  a **$9.9bn power purchase agreement (2027–2047)** expected to be a lease + $7.6bn of
  backstop guarantees + **$21.9bn of VIE funding commitments, including a $20.0bn
  equity-derivative commitment to an unnamed private company through 2030.**

**[E5-39] — "we will never be dependent on the kindness of strangers" — FAILS, AND IT FAILS
ON A NEWLY DRAWN FACILITY.** Q1-2026 10-Q, verbatim: *"As of March 31, 2026, we had $11.7
billion of credit facilities … of which **$1.2 billion was outstanding**"*, at **SOFR + 1.5%
to 2.25%**; $1.3bn at 2026-06-30. **This is the first draw in the eleven vintages read**, and
that spread is wide for an issuer of this quality. Alphabet has also raised **$87.3bn of debt
in six currencies** (including a **Sterling note maturing 2126** — a hundred-year bond),
**$30.5bn of new common**, **$19.0bn of 6.25% preferred**, and opened a **$40bn ATM**, all in
eighteen months. **A company that in FY2019 carried $4,685M of debt and $120bn of net cash is
now a regular, multi-currency, multi-instrument issuer.** That is a real change in kind.

**Leverage, named and quantified [E4-16, E3-29]** — *no ratio ceiling exists in this
framework and the corpus supplies none.* Face value of long-term debt **$12,000M (2024-12-31)
→ $101,085M (2026-06-30), 8.4x in eighteen months**, against **$640,480M** of equity. **The
terms are the good kind [E3-52]:** senior unsecured, ranking equally, **74% of the 2025 book
maturing after 2030**, no disclosed covenants, fair value ($94.9bn) *below* face. Commercial
paper program $25.0bn with **nothing outstanding**. Solvency is not the issue and the run
says so.

**[E2-54] COVERAGE — AND IT IS THE ONE TEST THAT HAS GENUINELY BROKEN.** *"whenever someone
creates a capital structure that does not allow all interest … to be comfortably met out of
current cash flow **net of ample capital expenditures** — zip up your wallet."* Interest on
$101bn of face debt at a ~4% blended coupon is ~$4.0bn, plus $1.19bn of preferred dividends
≈ **$5.2bn**. Against OCF less capex: **FY2025 $73,266M = 14x, comfortable. H1-2026
annualised ~$8,522M = 1.6x.** **The coverage went from fourteen times to under two in six
months.** It is not a solvency event — the capex is discretionary in timing if not in
contract, and liquidity is $242bn — but [E2-54]'s word is *"comfortably"*, and 1.6x after
capex is not that.

### Name the specific way THIS business dies **[E2-27, E3-24]**

**[E4-51] applies: each case is stated at the strength its holders would accept, then
answered. [E4-40] governs the selection — exposure, not experience.**

**1. THE [E2-27] CAPEX TREADMILL / OVERBUILD — and Alphabet's own competitor row is the
evidence.** *"Viewed individually, each company's capital investment decision appeared
cost-effective and rational; viewed collectively, the decisions neutralized each other and
were irrational … After each round of investment, all the players had more money in the game
and returns remained anemic."* Five companies are building the same capacity at once.
**Quantified: a 20% impairment of the $203,679M technical-infrastructure gross book is
$40.7bn — roughly one year of judged owner earnings.** And the tell is that **Alphabet has
never impaired a server in eleven years**: every accelerated-depreciation and impairment
charge it has ever filed relates to **office space** ($1.8bn exit + $269M accelerated in
FY2023; $796M in FY2024; nothing in FY2025).
**LIKELIHOOD: [x] a real possibility — and partially the base case, because it is what the
last four filed years of owner earnings already show.**

**2. THE DEPRECIATION-LIFE RECKONING, AND A PEER HAS ALREADY TAKEN IT.** Servers are on six
years; the useful life of the core revenue-producing asset **has doubled in three years**
inside a two-to-three-year silicon cycle. **Quantified: reverting the ~$122,207M server and
network book from 6 years to 4 adds $10,184M of annual depreciation** — operating income
$129,039M → ~$118,855M, **−7.9%.** **Amazon has already reversed**, shortening a subset of
servers 6→5 effective January 2025 for the filed reason *"the increased pace of technology
development, particularly in the area of artificial intelligence and machine learning."*
**Alphabet has not re-tested. AND THE MSFT RULING TRANSFERS EXACTLY: a life change cannot
move OCF − SBC − capex by one dollar.** It would savage reported earnings, reported ROE and
Google Cloud's segment profit, and leave owner earnings untouched.
**LIKELIHOOD: [x] a real possibility.**

**3. CRITERION 3 — THE REMEDIES, AND THE DIRECTION IS NOT WHAT THE BRIEF ASSUMED.** TAC is
$59,926M, **14.9% of revenue**. If the default payments were *banned*, owner earnings would
**RISE** by up to that amount; the judgment instead **restricts and de-exclusivises** them, so
Alphabet keeps the distribution, keeps paying, and faces share loss plus compelled data
sharing and syndication that lower a rival's cost of entry. **The economic magnitude is
UNQUANTIFIABLE from any filed document — Alphabet discloses no accrual and states "we cannot
estimate a possible loss" — and it is recorded as EXPOSURE per [E4-40], not scored.** The one
number that would let an owner price it, the distribution-partner TAC rate, **was withdrawn
on 2019-10-29.** The ad-tech remedy is the sharper structural risk: Alphabet's own words are
that the DOJ proposal *"includes structural remedies that could have a material adverse
effect on our business"*, and judgment is awaited.
**LIKELIHOOD: [x] a real possibility for a material share of Network and Search economics; a
low-level possibility for solvency.**

**4. THE ANSWER ENGINE DISPLACES THE AD UNIT.** The thesis that generative answers destroy
the ten-blue-links business. **Answered by Alphabet's own filed physical series, and the
answer is no, not yet: paid clicks +5% (FY2024) → +6% (FY2025) → +13% → +13% (2026 quarters),
with cost-per-click +7%, +7%, +5%, +3%.** Volume accelerating, price rising.
**LIKELIHOOD: [x] a low-level possibility on current filed evidence** — and this is the one
place the bears' case is *contradicted* rather than merely unquantified.

**5. THE NON-MARKETABLE SECURITIES MARK REVERSES.** Non-marketables went **$37,982M →
$131,461M in eighteen months, +$93.5bn, against only $5.7bn of purchases** — i.e.
overwhelmingly **mark-ups**, under the measurement alternative, on "observable price changes"
in third-party financing rounds. H1-2026 gains on equity securities were **$135,946M, of
which 99.4% UNREALIZED**, sourced in the filing to **SpaceX** (~$94.1bn carrying value from a
$900M cost in 2015, restricted from sale in part through Q3-2027) and an unnamed private
company (**$87.9bn remeasured in Q2 alone**, Level 2, option-pricing models).
**Quantified: a 30% write-down is ~$39.4bn.** **It cannot touch owner earnings — OCF strips
the gain out ($24,620M removed in FY2025) — but it would savage reported net income, reported
ROE and equity.** **[E4-41] applies in its purest form: this is a favourable exogenous break
and it is named and removed before any mean is trusted.**
**LIKELIHOOD: [x] a real possibility for reported earnings; irrelevant to owner earnings.**

**6. SOLVENCY — essentially unnameable, and I tried.** $242.5bn liquid, ~$144bn net cash,
senior unsecured long-dated debt with 74% maturing after 2030, no covenants disclosed, no
commercial paper outstanding, a $25bn CP program untouched, and $185.7bn of annual operating
cash flow. **[x] a low-level possibility.**

- **VERDICT: [x] IN** — **GOOD, not great, and travelling.** [E4-43] passes the good class;
  only gruesome fails Q4. Recorded against it: [E5-11] strength 3 **FAILS** on a $811bn
  commitment book and a $200.7bn twelve-month claim; [E5-39] fails on a first-ever drawn
  facility and a rebuilt, multi-currency capital structure; [E2-54] coverage after capex has
  fallen from 14x to 1.6x in six months.

### CORRECTIONS TO Q3, RECORDED HERE RATHER THAN BY EDITING HISTORY (operator rule 6)

Two findings arrived after Q3 was written and committed (`98fe84e`). Neither changes the Q3
verdict; both are recorded openly.

1. **[E4-30]'s CASH-TAX TELL FIRES, AND MY Q3 TEXT WAS WRONG.** Q3 states the effective rate
   rose 13.9% → 16.4% → 16.8% and calls the tell acquitted. **That is the BOOK rate. [E4-30]
   is about CASH taxes as a share of reported pretax income, and the cash rate FELL from
   22.8% to 13.6% in FY2025** — the exact shape the corpus names. **IT IS ACQUITTED ON THE
   FILED EXPLANATION, not on my arithmetic:** the fall is entirely US federal and the FY2025
   10-K attributes it to **bonus depreciation on eligible capital expenditures** under 2025 US
   tax legislation, with deferred taxes swinging $13.6bn the other way — **timing, and it
   reverses.** The same shape the MSFT run found and acquitted for the same reason. The flag
   fires; the finding is benign; my original sentence was not.
2. **AUDITOR INDEPENDENCE — a flag I did not have at Q3.** Ernst & Young, **auditor since
   1999 (27 years)**, with **non-audit fees at 52.5% of total fees in 2024 and 44.8% in
   2025**, including a $19.4M "All Other Fees" bucket defined only by exclusion. **Non-audit
   fees above half of total is high** and is a live prompt to read. It does not reach [E5-16]'s
   binary. Against it: **zero financial restatements in twenty-two years**; three 10-K/As
   ever, all administrative (two Part III, one to add a missing E&Y signature); both FY2025
   cover error-correction boxes **unchecked**.

**Also added to the Q3 record, in Alphabet's favour and against it:**
- **[E3-54] PASSES: Alphabet BEAT its 402(v) peer group in 5 of 5 disclosed years** ($360.95
  vs $138.27 in 2025) — the opposite of MSFT (3 of 5 trailing) and AAPL (trailed).
- **[E4-27] INCENTIVES — the sharpest structural point in the proxy: the SOLE financial
  measure in Alphabet's incentive plan is RELATIVE TSR.** There is no accounting metric to
  manipulate, which is clean — **and equally nothing that rewards return on incremental
  capital while capital expenditure doubles.** *"Never, ever, think about something else when
  you should be thinking about the power of incentives."*
- **[E3-53] THE RESTRUCTURING ROUND-TRIP.** ~$6bn of severance and office charges FY2023–24,
  and headcount went **190,234 → 182,502 → 183,323 → 190,820** — **586 MORE people than
  before the layoff.** And in the same January as the 2023 workforce reduction, the server
  life change cut depreciation by **$3.9bn**, nearly offsetting the $3.9bn of FY2023 charges.
- **Stage 0 economic equivalence VERIFIED from the charter, not assumed:** Class C receives
  *"the same form and amount of dividends and other distributions"* per share and converts
  1:1 into Class A immediately before any liquidating distribution; stock dividends are paid
  in like class. **Only voting differs, so valuing on the 12.23bn total is correct.**
  **Page and Brin hold 52.7% of total voting power** (27.4% + 25.3%); Class B cannot be
  reissued and converts nine months after a founder's death.
- **Accrued-but-unpaid capex reached $29.1bn at 2026-06-30, from $10.6bn** — so cash capex
  understates capex *incurred* by a further ~$18.5bn in H1-2026. **Declined, so conservatism
  is not stacked**; taking it would push TTM owner earnings from $23,224M toward ~$5bn.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*
**Honest pre-tax expectancy at this price: ~7% (range 5.5–9.1%).** Below roughly 10%, the
name is not ranked — **it is quit on**, whatever the sovereign is.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$45,000M judged** ÷ market cap **$4,141,000M** = **1.09%** · sovereign
  **5.24%**

**Every construction, so the reader can pick his own [E4-38]:**

| construction | OE $M | yield | vs bond |
|---|---|---|---|
| **TTM strict (c = capex + finance leases)** | **23,224** | **0.56%** | **−4.68 pts** |
| 13-yr strict | 27,647 | 0.67% | −4.57 |
| 10-yr strict | 33,341 | 0.81% | −4.43 |
| 8-yr strict | 37,258 | 0.90% | −4.34 |
| **JUDGED** | **45,000** | **1.09%** | **−4.15** |
| 5-yr strict *(= screen oe_bottom)* | 46,910 | 1.13% | −4.11 |
| 3-yr strict | 47,615 | 1.15% | −4.09 |
| 3-yr depreciation end *(= screen oe_top)* | 91,056 | 2.20% | −3.04 |
| FY2025 at the forward-built (c) of $37.4bn | 102,360 | 2.47% | −2.77 |
| **TTM at the depreciation end — the most generous number constructible** | **132,291** | **3.19%** | **−2.05** |

**TEN CONSTRUCTIONS. ALL TEN BELOW THE BOND.** The most generous — the best twelve months in
Alphabet's history, valued as though a twice-lengthened depreciation charge covering 19% of
current spending fully replaces a fleet Alphabet has contracted $707bn to keep buying — still
pays **2.05 points less than a government bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- **growth needed to match the bare bond: +4.15%/yr PERPETUAL.**
- **growth needed to clear the [E4-28] floor: +8.91%/yr PERPETUAL.**
- **what the business has actually done — and it cuts both ways, published both ways [E4-38]:**

| measure | period | rate |
|---|---|---|
| revenue | FY2021 → TTM | **+12.96%/yr** |
| operating income | FY2021 → FY2025 | **+13.15%/yr** |
| **owner earnings, strict end** | **FY2016 → FY2025 (9 yr)** | **+10.43%/yr** |
| **owner earnings, strict end** | **FY2021 → FY2025 (4 yr)** | **−2.48%/yr** |
| **owner earnings, strict end** | **FY2021 → TTM (4.5 yr)** | **−16.27%/yr** |
| owner earnings, depreciation end | FY2021 → TTM | +16.71%/yr |

**The whole file reduces to one comparison: on the construction this run judges honest,
owner earnings have compounded at MINUS 16.27% a year for four and a half years; on the
construction the framework calls INVALID, plus 16.71%.**

**[E4-35] BURDEN DISCHARGED IN WRITING.** *"fewer than 10 of the 200 most profitable
companies … will attain 15% annual growth … over the next 20 years."* **+8.91% forever** from
$45bn is **$106bn in ten years, $250bn in twenty, $588bn in thirty** — against TTM revenue of
$445,866M. In twenty years Alphabet's owner earnings would have to equal **56% of today's
entire revenue**; in thirty, **132%** of it. **And the zero-growth version of the floor at
this price requires $414,100M of owner earnings — 92.9% of TTM revenue.**

**3. WHAT YOU ARE PAID**
- **return at the current price = −4.15 points over the sovereign** on judged owner earnings;
  **−4.68 points** on the latest twelve months; **−2.05 points** on the most generous
  construction that can be built. **There is no construction on which an owner is paid.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24**% — **the bare rate, no per-name premium added.** Certainty about
  Alphabet is handled at Q1 (the understanding gate, where the run recorded that the delivery
  mechanism is mid-rebuild) and in the end discount. It is **not** in the rate.
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support. Per share, on **12,230,000,000 shares** across all three classes:

**(a) Zero growth, capitalised at the 5.24% sovereign:**

| construction | value/share |
|---|---|
| TTM strict | **~$36** |
| **judged $45,000M** | **~$70** |
| 5-yr strict | ~$73 |
| 3-yr depreciation end | ~$142 |
| TTM depreciation end *(the construction this run calls INVALID, priced anyway to show it does not rescue the case)* | **~$206** |

**(b) With growth, discounted at the [E4-28] floor**, on judged owner earnings of $45,000M:
6%/yr perpetual → **~$98** · 7% → **~$131** · 8% → **~$199**.
*(The sensitivity across two percentage points is 2x. That is [E4-25]'s point made on
Alphabet's own numbers, and it is why no point estimate is offered.)*

**(c) Zero growth at the floor:** ~$19 (TTM) to ~$108 (most generous), judged **~$37**.

- **conservative ~$36–70 · optimistic ~$200 · judged ~$110 · CURRENT PRICE $338.46 (GOOGL) /
  $335.31 (GOOG), 2026-09-04, aggregator, flagged.**
- **Price = 3.1x judged value, 4.8x the judged zero-growth value, and 1.64x the single most
  generous construction that can be built from the filings.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- **floor verdict first: honest pre-tax expectancy ~7% (5.5–9.1%) vs ~10% [E4-28] — BELOW.
  THE NAME IS QUIT ON, NOT RANKED, and the ranking lines below are therefore not filled in.**
  The expectancy is built as the judged owner-earnings yield of 1.09% plus the growth in
  owner earnings this run is willing to underwrite (4.5–8%/yr — below revenue growth, because
  capital intensity is structurally higher and $707bn of supply agreements lock it through
  2030). **Even the top of that range does not reach the floor.**
- points over sovereign, this name: **−4.15** *(recorded; it does not enter a ranking)*
- against the rest of the opportunity set: **not applicable — a name below the floor is not
  ranked [E4-28].** For the record it sits alongside AAPL (~7.4%) and MSFT (~6%), the other
  two trillion-dollar names run this week, all three quit on for the same reason.

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — not used.
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case? No
      margin is added on top. **OUTCOME THREE: the price is ABOVE THE WHOLE RANGE.** $338.46
      against a range whose most generous end is ~$206 and whose judged centre is ~$110. It
      does not *"kind of scream at you"* **[E3-25]**; it screams the other way.
- **Windage count: ONE**, and it is stated because it is not obvious which direction it runs.
  Conservatism is spent at **the (c) judgment** — total capital spending rather than the
  invalid D&A default. It is **not** stacked: this run explicitly **DECLINED** three further
  conservative adjustments it had the filed evidence to make — **[E3-70]**'s $14,167M of cash
  paid to taxing authorities on net share settlement; the **$18.5bn** H1-2026 increase in
  accrued-but-unpaid capex; and the choice of the TTM window over the corpus-default
  five-year window. **Taking any of the three would roughly halve owner earnings again.** In
  the other direction, the judged $45,000M sits at the *generous* end: it is nearly double the
  live TTM reading. The single windage is disclosed, and the run says which way it leans.

- **VERDICT: [x] UNRESEARCHED? No. [x] IN as a completed valuation, and the answer is a
  PRICE FAILURE — the name is QUIT ON at the [E4-28] floor · ranking position: NOT RANKED.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]** — written now, so it cannot be retro-fitted:

- **THESIS-CONFIRMING METRIC (both halves together, two consecutive years):** total capital
  spending **including finance-lease additions falls below 20% of revenue** WHILE owner
  earnings on that construction **rise above $80,000M.** Either half alone is not enough:
  capex falling because demand collapsed is not the signal, and owner earnings rising because
  a life was extended a third time is not either.
- **THESIS-BREAKING METRICS AND THEIR THRESHOLDS — the bull signals, pre-registered so they
  cannot be rationalised away:**
  1. **Paid clicks decelerating below +5% for two consecutive quarters, or cost-per-click
     turning negative.** This is the [E4-55] series and it is currently the strongest fact
     *against* this run's conclusion. If it holds above +10% while CPC stays positive, the
     Search franchise is compounding and the case is about price only.
  2. **Purchase commitments falling back below ~$300bn**, or the long-term supply agreements
     being renegotiated shorter — the $707bn through 2030 is what locks (c) at total capex.
  3. Alphabet **restoring the TAC split** or **reinstating named competitors** — either would
     reverse an [E2-49] finding and move Q2's direction.
- **BEARISH BREAKERS:** a **THIRD** server life extension beyond six years, or an
  Amazon-style **shortening**; any impairment of the technical-infrastructure book (there has
  never been one); leases not yet commenced above **$150bn**; the credit-facility draw rising
  above ~$5bn; the ATM actually being drawn; Google Cloud's margin falling back below 15%;
  the mandatory-convertible preferred being followed by a second issue.
- **NEXT CATALYST DATES:** the **FY2026 10-K (late January / early February 2027)** — the
  single most informative document that will exist, and the first to show a full year at the
  new capex run-rate; the **D.C. Circuit** on the *US v. Google* search remedies (both sides
  appealed Jan/Feb 2026); the **E.D. Va. ad-tech remedies judgment**, awaited; the **May 2029
  mandatory conversion**.

**The sell rule [E2-28]** — two triggers, three hold conditions. **No position is held, so
this is recorded as an entry standard rather than an exit plan:**
- SELL if the market judges it more valuable than the facts indicate → **this is the finding
  today: $338.46 against a judged ~$110.**
- SELL if funds are needed for something more undervalued or better understood → n/a.
- HOLD while: return on equity capital satisfactory → **yes on the base business**;
  management competent and honest → **no disqualifier found**; market does not overvalue →
  **it does.**
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** *Is this erosion an
aberrational cycle, or has the business slipped in a way that permanently reduces intrinsic
value?* **Neither, and the honest answer is that the two are separable at Alphabet in a way
they usually are not.** The *franchise* is not eroding — paid clicks +13% and cost-per-click
+7% are the opposite of erosion, and they are filed. What has changed is **the price of
staying in business**: capital intensity from 9.6% to 29.7% of revenue in five years, with
$707bn contracted through 2030. **That is a change in the economic characteristics of the
business [E4-17], not a cyclical dip — and it is exactly the thing the corpus says to
re-evaluate on.** Whether it reverses is genuinely open, and the pre-registered
thesis-confirming metric above is the test.

**Do not trim winners [E5-14]** — n/a, nothing held.
**Position size — a judgment, stated: ZERO.** The name does not clear the [E4-28] floor on
any construction, so there is nothing to size. **A capital-allocation flag is live**
([E5-08] condition 1 failing, condition 2 having failed in FY2024–25), which under [E4-13]
would bind size downward even if a price case existed.

- **VERDICT: [x] IN** — the exit and re-entry standards are pre-committed above and dated.

---
## THE STRONGEST FACT AGAINST THIS CONCLUSION [E4-51]

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."* Three, stated at full strength:

**1. THE PHYSICAL SERIES IS ACCELERATING, AND IT IS THE FRAMEWORK'S OWN PREFERRED EVIDENCE.**
[E4-55] says *"where units exist, monitor units"* and calls the physical series the honest
one. Alphabet's is filed, current, and improving: **paid clicks +5% → +6% → +13% → +13%,
with cost-per-click +7%, +7%, +5%, +3%.** Volume accelerating and price rising together is
[E2-44](1) passed on filed data, and it is the exact opposite of the Precision Steel shape
that condemned Apple's iPhone. **The AI-kills-Search thesis is not merely unproven — it is
contradicted by the only physical series either side has filed.**

**2. THE NINE-YEAR OWNER-EARNINGS RECORD EXCEEDS THE RATE THE FLOOR REQUIRES.** Owner
earnings at the strict end compounded at **+10.43%/yr from FY2016 to FY2025**, against the
**+8.91%/yr perpetual** the floor demands. **Alphabet is the fourth name in this queue —
after CTAS, GRMN and AAPL — whose filed long-run record exceeds its required rate.** And
[E4-38]'s endpoint sensitivity is published both ways: from FY2021 the same series is
**−2.48%/yr**, because FY2021 was a COVID-advertising peak at 9.6% capex intensity.

**3. BERKSHIRE HATHAWAY BOUGHT $10.0 BILLION OF THIS COMPANY ELEVEN WEEKS AGO.** Q2-2026
10-Q, Note 11, verbatim: *"the company completed a private placement of 14 million Class A
and 14 million Class C shares to **an affiliate of Berkshire Hathaway Inc.**"* at ~$355 and
~$352 a share, against this run's judged ~$110. **The operator whose corpus this framework is
built from is on the other side of this conclusion, at three times the price this run
computes, in size, in a negotiated deal, four months ago.** That is not an argument I can
answer with arithmetic, and the run does not pretend to. **[E4-13] applies with unusual
force — they know more about it than I do.**

**THE ANSWER TO ALL THREE IS THE SAME, AND IT IS ARITHMETIC RATHER THAN A COUNTER-NARRATIVE.**
Points 1 and 2 describe the *business*, and this run agrees with them — that is why Q1–Q4
all returned IN and why Q4 says GOOD rather than gruesome. **The failure is at Q5, on price,
and [E5-42] is the governing line: business quality is "the capital actually needed in the
business"; "whether it's a good investment for us depends on how much we pay for that in the
end."** At $4.14 trillion, clearing the floor with no growth requires **$414,100M of owner
earnings — 92.9% of Alphabet's entire revenue.** Every one of ten constructions pays less
than a government bond. Point 3 stands unanswered and is recorded as such.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q5 opened only after Q1–Q4 each
      returned IN, per operator rule 2.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The Q2 moat
      class is NARROW, which is a class, not a caveat; the competitor row is complete for all
      five SEC-reachable peers, so the row is not held PROVISIONAL.
- [x] Every UNRESEARCHED verdict names the artifact: the **August 2024 D.D.C. memorandum
      opinion** (public docket, *US v. Google LLC*, No. 1:20-cv-03010) and the FY2023-onward
      **intangible-amortization figure** (XBRL `AmortizationOfIntangibleAssets`, if tagged).
- [x] Every UNKNOWABLE states what cannot be known: **segment return on capital** — Alphabet
      files no segment capex after FY2019, no segment assets in any vintage, and no segment
      depreciation ever; and **the segment split of the $3.9bn FY2023 life-extension benefit**,
      which is what would settle whether Google Cloud's maiden profit is an artefact.
- [x] Step 0: filing read, accession recorded, **seven figures cross-checked by string match
      against the filed HTML**, sentinel-checked 133 times for "Alphabet Inc."
- [x] Owner earnings on a multi-year mean; **six windows published, not one chosen [E4-38]**;
      capex band disclosed as a judgment with the forward build shown.
- [x] Competitor row filled — five peers, two metrics, all filing-sourced.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04. Not FRED.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test); windage count stated as ONE, with the three
      declined adjustments named so conservatism is visibly not stacked.
- [x] Prices dated 2026-09-04; **aggregator flagged**, live quote only.
- [x] Run committed to git after every question (`3ab1213`, `61500d8`, `98fe84e`, `9b49c58`).
- [x] Corrections to committed sections made **by addendum inside the file**, never by editing
      history (operator rule 6) — see the two Q3 corrections recorded in Q4.

## REGISTER
- Verdict: **[x] IN on the business (all four gates), FAIL at Q5 on price.** Not OUT — the
  business is sound; not UNRESEARCHED — the evidence was obtained; not UNKNOWABLE — the range
  is wide but it straddles nothing.
- **One line: the most profitable advertising franchise ever built, still compounding on the
  only physical series it files, whose owner earnings have nonetheless fallen 55% in four and
  a half years because it has contracted $707 billion of capacity through 2030 — priced at
  4.14 trillion dollars, where every one of ten constructions pays less than a Treasury bond.**
- **THE PRICE: $338.46 (GOOGL) / $335.31 (GOOG), 2026-09-04.**
- **PASS/FAIL: FAIL. Q1 IN · Q2 IN (NARROW) · Q3 IN (OVERLAY) · Q4 IN (GOOD) · Q5 FAIL, on
  price, at the [E4-28] floor · Q6 IN (standards pre-committed).**
- **Pre-committed re-look: judged value ~$110/share at a 5.24% sovereign, recomputed at the
  rate of the day. RE-OPEN BELOW ~$130 — a ~62% decline — but the file is far likelier to
  re-open on earnings than on price:** the thesis-confirming metric is total capital spending
  below 20% of revenue with owner earnings above $80bn, two years running.
