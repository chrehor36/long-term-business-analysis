# Company Run — Meta Platforms, Inc. (META) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

Run unattended from scratch on 2026-09-18 (night, EDT); the template was copied and committed before any fetch
(`f80e17c`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the first
name in the "no share count from dei: read the cover" row. Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 META/`; the brief is `_BRIEF.md` there. Prior runs that put Meta in a competitor row
(GOOGL, MSFT, AMZN, PINS, the 2026-07-15 five-pack) were read for where to look; **no figure below is taken from them**.
Every figure is from Meta's own filings, fetched by this run, with the accession.

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
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### The entity, in every year used
CIK 0001326801, `submissions.json` (fetched by this run): *"Meta Platforms, Inc."*, SIC *"Services-Computer Programming, Data
Processing, Etc."*, `fiscalYearEnd` 1231 (correct: every 10-K reports a December 31 year end), one former name (*"Facebook Inc"*,
2005-05-06 to 2021-10-27). SEC `company_tickers.json`: *"{'cik_str': 1326801, 'ticker': 'META', 'title': 'Meta Platforms,
Inc.'}"*. One Delaware corporation throughout (*"We were incorporated in Delaware in July 2004"*, FY2025 10-K Note 1); the 2021
rename changed no reporting key; no shell, no reverse recapitalization (the DJT check does not apply).

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The brief-writer's probe
(`_probe_screen.py`, `_probe_screen_output.txt`, re-read by this run) shows companyfacts carries **one** dei element for Meta,
`EntityPublicFloat`, and no `EntityCommonStockSharesOutstanding` at all; `share_count_shift` therefore returned **None**, which is
"not measured", not "stable" (the RIVN reading). **The hypothesis (two share classes on the cover) was tested on the inline XBRL
of the latest 10-Q** (`dei.py`; the raw document `meta-20260630.htm`, accession `0001628280-26-050705`), and it holds exactly:
the cover tags the element twice, once per class, and **each fact carries a dimension**:

- *"name="dei:EntityCommonStockSharesOutstanding" ... 2,205,128,509"* in context c-2, whose segment is
  *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-07-24;
- the same element in context c-3, segment *"us-gaap:CommonClassBMember"*, **342,377,716**.

companyfacts publishes only undimensioned facts, so a count tagged per class never reaches it. **So the label was, for META, a
tagging convention for a two-class cover: the count exists on every cover, split by class, and the screen could not see it.**
The other a8bc84f guards (probe output): `scale_shift` 1.372 (the largest one-year revenue step in the window, FY2020 to FY2021,
$86.0bn to $117.9bn, consecutive years; did not fire); `restatement_shift` (1.0, FY2017), a null and not a guard (the SNOW
note); no acquisition, working-capital, D&A, capex-funding or lease-capex flag fired. **No restatement exists:** no 10-K/A,
10-Q/A or NT filing in either submissions index read (2017-05 to 2026-09); the FY2025 10-K cover leaves the error-correction box
unticked (*"reflect the correction of an error to previously issued financial statements. ☐"*). **One presentation change was
found and is carried:** FY2023 capex is *"Purchases of property and equipment | ( 27,266 )"* beside *"Proceeds relating to
property and equipment | 221"* on the FY2023 10-K face and **27,045** (net) on the FY2025 10-K face; the FY2025 face is used for
FY2023-25 and the earlier faces for FY2017-22 (the proceeds line is $0.1-0.2bn a year).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this
  run at 22:03 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** a second later (`step0_out.txt`): the stale-cache defect,
  reproduced a seventh time. The issuing-authority figure is used. FRED not used. Struck by this run, not inherited from AEHR (it
  agrees because it is the same day's print).
- **Earnings currency: USD.** The company reports in dollars; **62.8% of FY2025 revenue was billed to customers outside the
  United States** (US revenue *"$ 74.78 billion"* of $200,966M, FY2025 10-K Note 2), so the dollar result carries currency
  translation (FY2022: *"a $5.96 billion negative impact from the appreciation of the U.S. dollar"*, FY2022 10-K MD&A). No ADR
  or FX conversion of the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$665.75, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("META", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 665.75,
  `regularMarketTime` 1789761602 = 20:00:02 UTC = **16:00:02 EDT**, the closing print. The day's bar had not finalised (open
  686.82, high 690.15, low 660.80, close None: the BX and AEHR `close None` note again). `tools/sources.price()` returned the
  same 665.75 stamped 2026-09-18.
- **The month, recorded rather than choosing a day:** 08-19 $546.03 · 08-28 $578.02 · 09-02 $592.85 · 09-09 $653.69 · 09-15
  $670.24 · 09-17 $682.31 · 09-18 $665.75. **+22% in a month.**
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Christopher K. Cox sold 20,000 shares on 2026-09-15 at a
  weighted **$675.2278** (`0000950103-26-014140`), inside Yahoo's 09-15 range ($656.20-$678.87); Javier Olivan sold on
  2026-09-14 at **$657.73** (`0000950103-26-014061`), inside $649.22-$668.60; Cox on 2026-09-09 at $650.21 and $651.15
  (`0000950103-26-013860`), inside $638.56-$657.86. **The aggregator's series is corroborated on three dates (inside the day's
  range, not to the cent: these are sales, not withholding at the close); no Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-24): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the A/B treatment from the charter
- **Class A 2,205,128,509 + Class B 342,377,716 = 2,547,506,225 shares**, from the cover of the **Form 10-Q for the quarter
  ended 2026-06-30, filed 2026-07-30, accession `0001628280-26-050705`**, the latest periodic filing: *"Class A Common Stock |
  $0.000006 par value | 2,205,128,509 | shares outstanding as of July 24, 2026 | Class B Common Stock | $0.000006 par value |
  342,377,716 | shares outstanding as of July 24, 2026"*. `Screens/cover_shares.py META` returns the same two figures and
  prints their sum as *"arithmetic sum, NOT a share count"*: **the addition is a judgment, made here from the charter.**
- **Why A and B are added, one for one.** The Amended and Restated Certificate of Incorporation (Exhibit 3.1 to the 10-Q filed
  2024-08-01, accession `0001326801-24-000069`, incorporated by reference in the FY2025 10-K exhibit list): *"3.1. Equal Status .
  Except as otherwise provided in this Restated Certificate of Incorporation or required by applicable law, shares of Class A
  Common Stock and Class B Common Stock shall have the same rights and powers, rank equally (including as to dividends and
  distributions, and upon any liquidation, dissolution or winding up of the corporation), share ratably and be identical in all
  respects and as to all matters."* Dividends *"shall be treated equally, identically and ratably, on a per share basis"* (3.3);
  liquidation *"entitled to receive ratably all assets"* (3.5); mergers *"made ratably on a per share basis among the holders of
  the Class A Common Stock and Class B Common Stock as a single class"* (3.6); each with a proviso allowing disparate treatment
  only with the disadvantaged class's separate approval. Conversion (Exhibit 4.6, Description of Capital Stock, 10-K filed
  2024-02-02, `0001326801-24-000012`): *"a share of Class B common stock may be converted at any time into one share of Class A
  common stock"*, and *"each share of Class B common stock will convert automatically into one share of Class A common stock upon
  any transfer"*, with limited exceptions. The one difference is votes: *"The holders of our Class B common stock are entitled to
  ten votes per share, and holders of our Class A common stock are entitled to one vote per share."* **The two classes are
  economically identical, so the cash-flow claim is the sum. The votes are not identical, and they belong at Q3 (control), not in
  the count.** The company counts them together too: basic EPS on 2,521M weighted shares FY2025, and *"Diluted EPS ... assumes
  the conversion of our Class B common stock to Class A common stock"* (10-Q Note 3).
- **Sold after the cover date: nothing found.** No equity offering: the S-3ASR of 2026-04-30 (`0001193125-26-194008`) carried a
  $25bn notes offering (8-K `0001193125-26-204128`, 2026-05-04: six tranches, 4.550% 2031 to 6.450% 2066); post-cover Form 4s
  are sales of existing shares. Buybacks were **zero** in H1 2026 (*"Repurchases of Class A common stock | — | ( 22,921 )"*, six
  months 2026/2025, 10-Q face).
- **Dilution not in the count:** **146,464 thousand unvested RSUs** at 2026-06-30 (5.7% of the cover count), and options on
  **20 million** Class A shares granted in H1 2026 at a weighted exercise price of **$2,788** (10-Q Note 10). Shown beside the
  cap, not in it (the cover is the rule).

### The market cap
**$665.75 x 2,547,506,225 = US$1,696.0bn** (Class A $1,468.1bn; Class B at the Class A price, $227.9bn, which the charter's
equal-status clause licenses). **With the unvested RSUs: $1,793.5bn.** The options are 4.2 times out of the money and are not
added. Split factor 1.0. Public float on the FY2025 10-K cover: *"approximately $ 1.6 trillion"* at 2025-06-30.

### THE DEAL CHECK: none live
`sources.deal_filings("0001326801")` returned `([], [], '2026-01-29')` and `deal_note` returned empty (`step0_out.txt`). Read on
both submissions indexes (2017-05 to 2026-09): **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D filed on this registrant.**
The one S-4 (2022-11-15, `0000950103-22-019633`, effective 2022-11-23) followed the August 2022 notes offering (8-Ks of
2022-08-04 and 2022-08-09) and is not a business combination (no 425 or merger 8-K accompanies it). The 8-Ks filed since
2024-08 carry Items 2.02, 5.02, 5.03, 5.07 and 8.01 (the notes offerings of 2024-08, 2025-11 and 2026-05, and the 2025-12-12
notice of a derivative-suit settlement, read at Q3); **no Item 1.01 or 2.01.** **The quote is not a spread and buys this
company.**

### The perimeter: what (c) and the cap must see
- **Scale AI, a minority stake, 2025:** *"our minority investments in Scale AI for $ 13.80 billion, which was closed during 2025"*
  (FY2025 10-K Note 5), carried under the measurement alternative (*"We do not have significant influence over these investees'
  operations"*). Cash on the face: *"Purchases of non-marketable equity investments | ( 18,330 )"* FY2025 (Scale AI and others).
  Not consolidated; it contributes nothing to owner earnings and no look-through [E3-04] is possible (no investee earnings are
  filed). **Q4 carries the cash.**
- **The Louisiana data-centre Venture, October 2025, OFF the balance sheet:** *"At Venture formation, we contributed $ 4.30
  billion of held-for-sale assets, net of liabilities, and we received a one-time distribution of $ 2.55 billion. We hold a 20 %
  membership interest in the Venture, which is accounted for under the equity method ... The parties have committed to fund their
  respective pro rata share of approximately $ 27 billion in total estimated development costs."* Meta leases it back from 2029:
  *"The aggregate initial lease commitment is approximately $ 12.31 billion, with each property having an initial four-year lease
  term and options to renew for a total lease period of up to 20 years. In addition, we have provided residual value guarantees
  (RVG) with an aggregate threshold of approximately $ 28 billion"*; *"we are not the primary beneficiary and do not consolidate
  the variable interest entity (VIE). Our maximum exposure to loss related to the Venture was $ 45.95 billion as of December 31,
  2025"* (FY2025 10-K Note 5). (The filing calls it only "the Venture"; the name Hyperion appears in no filing read.) **A data
  centre built for Meta, managed by Meta, leased by Meta and guaranteed by Meta, 80% of whose construction cost does not pass
  through Meta's capex line.** Q4 carries it.
- **Leases not yet commenced and purchase commitments:** *"we have additional operating and finance leases, that have not yet
  commenced, with total lease obligations of approximately $ 103.77 billion, mostly for data centers, colocations, and network
  infrastructure"* (FY2025 10-K Note 7), and *"$ 131.05 billion of non-cancelable contractual commitments ... mostly related to
  third-party cloud capacity arrangements"* (Note 11). Both are read against the 2026-06-30 10-Q at Q4.
- **Acquisitions of businesses** are small on the face ($0.3-1.3bn a year FY2019-24, $4,231M in FY2025) and are shown in their
  own column at Q4.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, filed **2026-01-29**, accession **`0001628280-26-003942`** (`10K_FY2025.txt`), and the **Q2 2026 Form
  10-Q**, filed **2026-07-30**, accession **`0001628280-26-050705`** (`10Q_2026Q2.txt`).
- Also read: the FY2019, FY2021, FY2022, FY2023 and FY2024 10-Ks (`0001326801-20-000013`, `-22-000018`, `-23-000013`,
  `-24-000012`, `-25-000017`) for the FY2017-24 statements, segment notes and the ad-price series; the Q3 2025 and Q1 2026 10-Qs
  (`0001628280-25-047240`, `0001628280-26-028526`); the DEF 14A of 2026-04-16 (`0001628280-26-025532`); the charter and the
  Description of Capital Stock (above); the 8-K EX-99.1 earnings releases for Q4 2021, Q4 2022, Q4 2023 and every quarter Q4
  2024 to Q2 2026; the 8-Ks of 2025-11-03, 2025-12-12 and 2026-05-04; five Form 4s filed 2026-09-08 to 2026-09-17.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statement of cash flows, $M, FY2025/24/23):
  *"Net cash provided by operating activities | 115,800 | 91,328 | 71,113"*, *"Share-based compensation | 20,427 | 16,690 |
  14,027"*, *"Depreciation and amortization | 18,616 | 15,498 | 11,178"*, *"Purchases of property and equipment | ( 69,691 ) |
  ( 37,256 ) | ( 27,045 )"* and *"Principal payments on finance leases | ( 2,524 ) | ( 1,969 ) | ( 1,058 )"* match
  companyfacts (the brief's tagged series) to the million, except FY2023 capex (tagged 27,266, the FY2023 10-K's gross figure,
  above) and FY2024 D&A (tagged 15,501, an earlier vintage, against 15,498 on the FY2025 face). Revenue *"$ 200,966 | $ 164,501 |
  $ 134,902"* matches.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
About 3.6 billion people a day open one or more of four free apps (Facebook, Instagram, Messenger, WhatsApp). Meta fills
a share of what they scroll through with advertisements and sells each slot in an auction to whichever advertiser's bid,
multiplied by the chance this particular person responds, is highest. Revenue is therefore **ads shown x price per ad**, and
the company files both halves as year-on-year changes. The price an advertiser will pay depends on how well Meta predicts who
will respond, which depends on what Meta knows about each user and on the prediction machinery (servers and models). The
costs are the people who build the apps and models, the data centres that run them, and payments to content creators and
partners. It is the same mechanism in every 10-K read, FY2019-25.

| $M (segment notes; FY2019-20 from the FY2021 10-K recast) | FY2019 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Family of Apps revenue | | | | 133,006 | 162,355 | 198,759 | 116,278 |
| of which advertising | | | | 131,948 | 160,633 | 196,175 | |
| Family of Apps operating income | 28,489 | 56,946 | 42,661 | 62,871 | 87,109 | 102,469 | 50,294 |
| FoA operating margin | | | | 47.3% | 53.7% | 51.6% | 43.3% |
| Reality Labs revenue | | | | 1,896 | 2,146 | 2,207 | 833 |
| **Reality Labs operating loss** | **(4,503)** | **(10,193)** | **(13,717)** | **(16,120)** | **(17,729)** | **(19,193)** | **(8,647)** |
| Consolidated operating income | 23,986 | 46,753 | 28,944 | 46,751 | 69,380 | 83,276 | 41,647 |
| ad impressions, y/y | +33% | +10% | +18% | +28% | +11% | +12% | +16% |
| average price per ad, y/y | -5% | +24% | -16% | -9% | +10% | +9% | +12% |
| Family daily active people (December; June for 2026) | 2.26bn | 2.82bn | 2.96bn | 3.19bn | 3.35bn | 3.58bn | 3.60bn |

(FY2020: RL loss (6,623), FoA 39,294; price per ad *"a decrease of approximately 10% in 2020"* (FY2021 10-K). FY2025 advertising
is 97.6% of revenue.) **Reality Labs has lost $96.7bn from FY2019 to H1 2026**, on revenue of about $2bn a year.

**The scarce input the business controls:** the daily habit of 3.6 billion people inside four apps, and the behavioural record
that habit produces, which is what lets Meta price an impression. **What it does not control**, on its own filing: the phones
the apps run on (*"Apple has released changes to iOS that limit our ability, and the ability of others in the digital
advertising industry, to target and measure ads effectively"*, FY2025 10-K Item 1A; in 2022 *"limitations on our ad targeting
and measurement tools arising from changes to iOS and the regulatory environment"* came with *"Our average price per ad
decreased by 16%"*, FY2022 10-K MD&A), and the users' alternatives (*"competitive products and services, such as TikTok, that
have reduced some users' engagement with our products and services"*, FY2025 10-K Item 1A).

**Will the fundamentals look broadly the same in ten years?** The mechanism (attention sold by auction) has been the same since
the mobile shift. **The company's own description of its industry is the opposite of [E3-31]'s "stable in character":** *"Our
business is characterized by innovation, rapid change, and disruptive technologies"* (FY2025 10-K Item 1, *Competition*). The
format has been replaced twice in the filed decade (feed to Stories to Reels), two of the four apps were bought
(Instagram 2012, WhatsApp 2014), the 2021 strategy was *"to focus on helping to bring the metaverse to life"*, and the 2026
10-Qs describe *"significant investments in AI initiatives, including generative AI and superintelligence"*, with capital
expenditure guided at *"$130-145 billion"* for 2026 (Q2 2026 EX-99.1) against $69.7bn in 2025 and $15.1bn in 2019.

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) The company says its business is characterized by *"rapid change, and disruptive technologies"*, which is [E3-31]'s
exclusion in the filer's own words. (2) The price ($1.70 trillion, Step 0) is being asked while the company commits capital on
a scale no filed revenue explains: at 2026-06-30, *"$ 349.31 billion of non-cancelable contractual commitments"* and leases not
yet commenced of *"approximately $ 278.99 billion"*, plus *"approximately $ 68 billion"* signed in July 2026 (Q2 2026 10-Q Note
9), against 2025 revenue of $201bn. What that capital is for is described only in purpose words (*"superintelligence"*,
*"entirely new enterprise opportunities"*, Q2 2026 release), and no filing gives it a revenue line or a return. (3) Reality
Labs has absorbed $96.7bn with revenue still near $2bn a year.

**Why it does not carry, and what is excluded.** HHH, RGTI and DJT closed at Q1 because the declared business was not the
filed one. **Here the filed business is the declared one: 97.6% of FY2025 revenue is advertising sold on four apps, and I can
state its unit economics from the filed series (impressions and price per ad) every year FY2019 to H1 2026.** What is outside
the circle is named: **superintelligence, AI products for enterprises, and Reality Labs as a future business** have no revenue
line that decides anything, and [E4-46] says study will not repair that (*"if we can't make a decision in five minutes, we
can't make it in five months"*). They are recorded as outside the circle and **cannot be counted at any later gate**,
including Q5. **Their cost is not outside the circle**: it is being paid now, out of the advertising cash, and it is carried at
Q2 (does the spending defend the advantage or buy its replacement? [E4-04]) and at Q4 (how much of it (c) must see).
Whether a business that describes itself as characterized by rapid change has a position that survives the change is the Q2
question, and it is carried there.

- **VERDICT: [x] IN** on the business the filings show (advertising sold by auction against the daily attention of 3.6 billion
  people on four owned apps, 97.6% of FY2025 revenue). **Not IN** for superintelligence, enterprise AI and Reality Labs as
  businesses: outside the circle [E3-31, E4-46], never counted later; their cost is carried at Q2 and Q4.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no close
> substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
Meta owns the largest audience any advertiser can buy: 3.6 billion people a day. The filed physical series pass [E2-44]'s
first half in the three latest periods: **ad impressions +11%, +12% and +16% (FY2024, FY2025, H1 2026) while the average price
per ad rose +10%, +9% and +12%**, volume and price up together, which is the Alphabet paid-click result the GOOGL run treated
as the strongest fact in its file. The Family of Apps earned **$102.5bn of operating income at a 51.6% margin** in FY2025.
Consolidated operating income was **41.7% of average equity** in FY2025 (83,276 on the average of 182,637 and 217,243), 41.3%
in FY2024 and 33.5% in FY2023 [E3-46]. The largest US antitrust attack on the position (the FTC's suit to unwind Instagram and
WhatsApp) was lost by the FTC at trial. If any advertising business is a franchise, this one is the candidate.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** Advertisers pay more per ad while buying more ads (above); DAP 3.60bn.
- **(3) Not subject to price regulation: YES FOR PRICE, WITH A CAP ON TERMS.** No regulator sets the price of an ad. But the
  European Commission sets the terms of the product in the European Union, which is **23.2% of FY2025 revenue** (Europe
  $46,569M of $200,966M, Note 2): *"In April 2025, the European Commission issued a final decision that our "subscription for no
  ads" model does not comply with such requirements and imposed a fine of EUR € 200 million. Based on feedback from the European
  Commission in connection with the DMA, we launched less personalized ads (LPA) in November 2024 and made significant
  modifications to LPA since the European Commission issued its final decision ... further modifications to our model may be
  imposed during the appeal process, which could result in a materially worse user experience for European users and a
  significant impact to our European business and revenue"*; and, in June 2026, *"the European Commission imposed an interim
  measure requiring WhatsApp to offer access to the API for free for such general purpose AI providers"* (Q2 2026 10-Q Note 9).
  A price set at zero by a regulator on one product line, and the terms of the core product set by a regulator in a quarter of
  the revenue. **[E2-59]: regulation caps a franchise; it does not create or destroy the class.** Recorded as a cap, as the
  GOOGL run recorded its criterion 3; not the ground of this verdict.
- **(2) No close substitute: NO, and three independent records say so.**
  1. **The company's own filings, FY2025:** *"competitive products and services, such as TikTok, that have reduced some users'
     engagement with our products and services"*; *"We believe that some users, particularly younger users, are aware of and
     actively engaging with other products and services similar to, or as a substitute for, our products and services, and we
     believe that some users have reduced their use of and engagement with our products and services in favor of these other
     products and services"*; on the advertiser side, *"Many of our marketers spend only a relatively small portion of their
     overall advertising budget with us"* and *"loss of advertising market share to our competitors, including if prices to
     purchase our ads increase or if competitors offer lower priced, more integrated, or otherwise more effective products"*
     (FY2025 10-K Item 1A). **The filer names the substitute and names the price response.**
  2. **A federal court, on a full trial record, at Meta's own urging.** *FTC v. Meta Platforms, Inc.*, No. 20-3590 (JEB)
     (D.D.C.), Memorandum Opinion of 2025-11-18, fetched by this run from the court's own server
     (`ecf.dcd.uscourts.gov/cgi-bin/show_public_doc?2020cv3590-693`, `FTC_opinion.pdf`, 89 pages; the text extraction renders
     apostrophes and quotation marks as a replacement character and splits one word, *"main feat ures"*; restored below and flagged as extraction artifacts): Meta's
     position was that its market *"at a minimum includes TikTok and YouTube, fierce competitors for users' time and attention"*;
     the court: *"The Court ultimately finds that YouTube and TikTok belong in the product market, and they prevent Meta from holding a
     monopoly. Even if YouTube is out, including TikTok alone defeats the FTC's case"*; and *"Meta holds no monopoly in the
     relevant market."* On the product: *"Facebook, Instagram, TikTok, and YouTube have thus evolved to have nearly identical main
     features."* The 10-Q records only *"On November 18, 2025, the court granted judgment in our favor. On January 20, 2026, the
     FTC filed a notice of appeal"* (Note 9). **The one adjudicated finding on this question, argued for by Meta itself, is that
     its users have close substitutes.** This is the mirror of the GOOGL file, whose Q2 IN rested on a court having found Alphabet
     a monopolist in search [E5-28]; here the court found the opposite, and the company asked it to.
  3. **The price series, read across the whole filed window rather than its best three years [E4-38, E4-55].** Average price per
     ad, FY2019-25: -5%, -10%, +24%, -16%, -9%, +10%, +9%. **Compounded, the FY2025 average price per ad is 0.97 times FY2018's,
     and 0.92 times FY2021's**, while impressions grew 1.88 times from FY2021 to FY2025 (+18%, +28%, +11%, +12%). Meta sells more
     ads each year at, over seven years, about the same price; the three rising years follow two falling ones, and the company
     attributes the rise to *"ongoing improvements to our ad performance from our ad targeting and measurement tools"* (FY2025
     10-K MD&A), not to a price set against flat demand. The fall is attributed to substitutes and platforms it does not control
     (iOS, above; *"products, such as Reels, that monetize at lower rates"*, the format built against TikTok). **The GOOGL run's
     cost-per-click rose in four straight years; Meta's price per ad is where it was in 2018.** A mix measure, yes (geography and
     format), and the filer is the one who reports it this way.

**Criterion (2) fails, so the conjunction fails.**

### [E4-04]: MUST THE MOAT BE CONTINUOUSLY REBUILT? (the test v4 sets: does a lapse in spending destroy the structure or narrow it, and does the spending defend the same advantage or buy its replacement?)
**The filer's answer is the class [E4-04] excludes, in nearly its words.** [E4-04]: *"Our criterion of "enduring" causes us to
rule out companies in industries prone to rapid and continuous change."* Meta, FY2025 10-K: *"Our business is characterized by
innovation, rapid change, and disruptive technologies."* The court, 2025-11-18: *"In the online world of social media, the
current runs fast, too. The landscape that existed only five years ago when the Federal Trade Commission brought this antitrust
suit has changed markedly"*, and *"With apps surging and receding, chasing one craze and moving on from others, and adding new
features with each passing year"*; *"The Court's two Opinions on motions to dismiss did not even mention the word "TikTok."
Today, that app holds center stage as Meta's fiercest rival."*

**The record of the basis being replaced, on the filings:** the attention moved from the Facebook feed to Instagram (bought,
2012) and WhatsApp (bought, 2014), then to Stories, then to short video, where Meta had to build Reels in answer to TikTok
(FY2021 10-K: *"in response to competitive pressures, we have introduced new features such as Reels, which is growing in usage
but is not currently monetized at the same rate as our feed or Stories products"*), at a lower price per ad. **Each change
of format was met by buying or copying the replacement.** Now the spending is on a scale that is itself the evidence: capital
expenditure **$15.1bn (FY2019) to $69.7bn (FY2025) to a guided $130-145bn (FY2026)**, $349.31bn of purchase commitments and
$347bn of signed leases not yet commenced (Step 0, Q4). Some of it defends the same advantage (the Q2 2026 10-Q: AI to
*"recommend relevant content across our products, enhance our advertising tools"*); some of it buys a different one (*"develop
new products"*, *"superintelligence"*, *"entirely new enterprise opportunities"*), and **no filing splits the two**. What the
filing does say is what happens if it fails: *"If our investments are not successful longer-term, our business and financial
performance could be harmed"* (Q2 2026 10-Q Item 1A). A franchise whose owner describes a lapse in a $130-145bn annual build as
a threat to the business is the moat that must be continuously rebuilt; the advantage lives in the prediction machinery, and
the machinery is being re-bought at rising cost. **The four causes [E4-36]:** the FY2012-21 record is extreme performance on a
few variables (reach, targeting data) plus **wave-riding [E3-51]** (the mobile-feed wave); the FY2022 break (iOS, TikTok,
price -16%, operating income -38%) is what *"if he gets off the wave, he becomes mired in shallows"* looks like for one year,
and the recovery was bought with Reels and with AI ranking.

**The TSMC tension against [E4-04] (the 2023 meeting) is an open operator question**; v4 is applied as written. **It does not
decide this verdict**, because criterion (2) fails independently on the filer's own words and the court's finding.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
**Whom Meta names:** TikTok once (above), Apple and Google as platform owners (*"each of Apple and Google have integrated
competitive products with iOS and Android, respectively"*); YouTube, Snap, Amazon and Pinterest zero times (count in
`10K_FY2025.flat.txt`). **Who names Meta:** Snap, Pinterest and Reddit each name *"Meta (including Facebook, Instagram, Threads,
and WhatsApp)"* in their FY2025 competition sections; Alphabet and Amazon name no competitor by company name (zero hits for
Meta, Facebook, Instagram or TikTok in either FY2025 10-K). **TikTok (ByteDance), the substitute the court and Meta name
first, files nothing with the SEC**, and neither do X or OpenAI.

The row: every SEC filer selling advertising against user attention at scale, FY2021-25 (Reddit FY2022-25, its first filed
year), from companyfacts re-fetched by this run (`peers/getpeers.py`, `peers/calc.py`, `peers/calc_out.txt`), with one
operating-cash figure per peer found on the filer's own FY2025 10-K face (`peers/fetchpeer10k.py`): Alphabet *"Net cash provided
by operating activities | $ | 125,299 | $ | 164,713"* (`0001652044-26-000018`); Snap *"656,170 | $ | 413,480 | $ | 246,521"*
(`0001564408-26-000013`); Pinterest *"Net cash provided by operating activities was $1,284.3 million"*
(`0001506293-26-000021`); Reddit *"690,875 | $ | 222,068 | $ | (75,114)"* (`0001713445-26-000022`). Owner cash here is OCF less
SBC less capex less finance-lease principal, **before any (c) judgment** (the same construction for every row).

| company | 5y revenue ($bn) | revenue growth, a year | FY2025 growth | operating margin, 5y (FY2025) | capex / revenue, first year → FY2025 | SBC / OCF, 5y | 5y OCF − SBC − capex − FL principal, % of revenue |
|---|---:|---:|---:|---:|---:|---:|---:|
| **META (subject)** | **734.9** | **14.3%** | **22.2%** | **37.4% (41.4%)** | **15.8% → 34.7%** | **18.7%** | **16.8% ($123.2bn)** |
| GOOGL (consolidated) | 1,600.7 | 11.8% | 15.1% | 29.9% (32.0%) | 9.6% → 22.7% | 18.3% | 14.6% |
| GOOGL Google Services segment | | | 12.4% | FY2025 40.7% (139,404 / 342,721) | | | |
| AMZN advertising services (revenue only; no profit filed) | | | 22.1% (56,214 → 68,635) | not filed | | | |
| SNAP | 24.6 | 9.6% | 10.6% | -19.6% (-9.0%) | 1.7% → 3.7% | 326.8% | -19.9% |
| PINS | 16.3 | 13.1% | 15.8% | 3.7% (7.6%) | 0.4% → 0.8% | 78.5% | 4.7% |
| RDDT (FY2022-25) | 5.0 | 48.9% | 69.4% | -8.7% (20.1%) | 0.9% → 0.3% | 167.7% | -10.7% |

**WHERE THE SUBJECT SITS:** **the margin leader and the owner-cash leader of the row, by a distance**; growing faster than
Alphabet and at Amazon's advertising rate; the only small peer growing faster is Reddit, off a base 1% of Meta's. **And the
most capital-hungry of the row by the end of it: capex/revenue went 15.8% to 34.7%, and to about 56-62% on the 2026 guide against H1 2026 revenue annualised ($234bn)**,
past Alphabet (22.7%). **The row shows a position far stronger than any filed rival's. It cannot show the rival the court and
Meta itself name first, TikTok, which files nothing.** Peers: five filers of the industry's roughly eight participants at scale
(Meta, Alphabet/YouTube, Amazon, ByteDance/TikTok, Snap, Pinterest, Reddit, X); three are unlisted in the US and cannot be put
in the row. **Not PROVISIONAL, and the reason is directional** (the BX and AEHR argument): the verdict below stands on the
subject's own words, a court's finding on a trial record and the subject's own price series [E3-43]; the unpulled rival is the
one the court found to be the close substitute, so pulling it can only confirm the finding. **The row's limit [E3-61]:** it
shows position, not conduct.

### THE OTHER Q2 TESTS
- **The two-characteristic test [E2-44]: half (1) passes in FY2024 to H1 2026 and fails across the window; half (2) fails.**
  (1) Price up with volume up in the last three periods, but not under flat demand (impressions +11-16%), and the seven-year
  price is flat (above). (2) *"only minor additional investment of capital"*: capital expenditure was 21.4% of revenue in FY2019,
  34.7% in FY2025, and 2026 is guided at $130-145bn (including finance-lease principal) against H1 2026 revenue of $117.1bn;
  property and equipment net went **$96.6bn (2023) to $225.7bn (2026-06-30)**. The growth is not capital-light and the filer says
  it will not become so: *"we have significantly increased our infrastructure investments in connection with our AI initiatives,
  and expect our investments to continue to increase"* (Q2 2026 10-Q Item 1A).
- **Return on capital [E3-46]:** high on the record (operating income 33.5-41.7% of average equity, FY2023-25). **The marginal
  return is falling on the filing:** net plant rose $129.1bn from 2023 to 2026-06-30 while twelve-month operating income rose
  $40.2bn (FY2023 $46.8bn to $86.9bn for the year to 2026-06-30), and Q2 2026 operating income **fell 8% on revenue up 28%**
  (*"Operating margin | 31 | % | 43 | %"*, Q2 2026 EX-99.1).
- **The attacker's test [E2-45]:** answered by the filed history. ByteDance attacked with TikTok from outside the US system
  and took enough engagement that Meta's own 10-K names it and a federal court found it in the market; the platform owners
  attacked from underneath (iOS, FY2022). The attacker was not hypothetical.
- **[E4-37] and untapped pricing power [E3-33, E5-28]:** the auction sets the price; there is no list price to raise and no
  price increase on file. The near-monopoly [E5-28] requires is the claim the court rejected at Meta's request. None.
- **The dominance class [E2-53]:** no. *"Good or bad, it will prosper"* does not describe FY2022 (operating income -38%,
  price per ad -16%), when a platform change and a rival format did the damage.
- **Direction [E4-32], and the physical series [E4-55]:** users still grow (DAP +3%, June 2026) and impressions grow; price per
  ad is up for three periods and flat over seven years; the moat's cost is rising much faster than its revenue (Q2 2026 costs
  +55%, revenue +28%). **Mixed on units, narrowing on the capital it takes to hold them.**
- **Key-person dependence [E4-23], recorded here as the moat check it is:** Class B carries ten votes, and *"Holders of our
  Class B common stock, including our founder, Chairman, and CEO, together hold a majority of the combined voting power"*
  (FY2025 10-K Item 1A); every strategic turn in the filed decade (the acquisitions, the metaverse, superintelligence) was the
  founder's, and no owner can overrule the next one. **Recorded as a defect of the business**, not as a Q3 finding.

### CLASS AND VERDICT
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL**, on [E3-03]'s definition. **Not a finding that Meta is a poor
  business**: it is the most profitable advertising business in the row, with the largest audience in the world. It is a
  finding that the audience has close substitutes by the company's own account and a court's, that the price per ad has not
  risen over seven years, and that the position is held by rebuilding its basis at a capital cost that has quadrupled in six
  years and is guided to double again.
- **Direction: narrowing on capital, mixed on units.**
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on three independent records: the
  company's own Item 1A (users *"actively engaging with other products and services similar to, or as a substitute for, our
  products"*, TikTok named; marketers spending *"only a relatively small portion of their overall advertising budget with us"*);
  the federal court's finding of 2025-11-18, argued for by Meta, that *"YouTube and TikTok belong in the product market, and they
  prevent Meta from holding a monopoly"*; and a price per ad that compounds to 0.97 times FY2018's across seven filed years
  **[E4-55, E4-38]**. [E4-04] points the same way in the filer's own words (*"characterized by innovation, rapid change, and
  disruptive technologies"*), with the basis replaced by purchase and copy and now by a $130-145bn-a-year build no filing splits
  between defence and replacement **[E3-51, E4-36]**; [E2-44](2) fails; the marginal return on capital is falling **[E3-46]**;
  the EU caps the terms in a quarter of revenue **[E2-59]**; key-person control recorded **[E4-23]**.
  *Not UNRESEARCHED: the documents that decide it (the 10-K, the 10-Qs and the court's opinion) are read; TikTok's own accounts
  do not exist in any filing and could only add to the substitute. Not UNKNOWABLE: the evidence is in and it decides.*
- **A conclusion that required fighting for it is worth less [E4-18].** This one did not need the price series or the capital
  test; the company's risk factor and the court's holding are each sufficient for criterion (2). **The omission cost of a wrong
  close [E3-47]** is acknowledged: this is the largest name in wave 5 and the most profitable in its row; the Q6 reopening
  conditions are written to catch the error.

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** (the BAM, DJT, RIVN, BX and AEHR precedent),
written because the brief asks for the owner-earnings rebuild, the Q3 read and the perimeter treatment, and because they set
the reopening conditions at Q6. **Q5 carries the heading `COMPUTATION — NOT A CLEARANCE` and no entry language appears anywhere
below.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT, on the business). Written because the brief asked for the
> earnings releases and the proxy to be read, and because the findings belong in the reopening conditions. Nothing here can
> promote the name or repair Q2 **[E2-37, E2-38, E3-39]**.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution [E3-38, E3-43]:** Q2 found a business, not a franchise, whose basis is rebuilt format by format and is
  now being re-bought at $130-145bn a year. *"a business, unlike a franchise, can be killed by poor management."*
- [ ] **Control [E1-16]:** a minority purchase of a listed share, which can be sold. **But the owner of that share cannot
  influence anything:** *"Holders of our Class B common stock, including our founder, Chairman, and CEO, together hold a
  majority of the combined voting power of our outstanding capital stock, and therefore are able to control the outcome of all
  matters submitted to our stockholders for approval so long as the shares of Class B common stock represent at least 9.1% of
  all outstanding shares"* (FY2025 10-K Item 1A; Class B is 13.4% of the cover count). Recorded beside the weight case, not in
  it: the determinant is the inability to exit, and a Class A holder can exit.
- [ ] **Leverage [E3-29]:** long-term debt $83.7bn against equity of $261.2bn and $90.3bn of cash and marketable securities
  (2026-06-30). Not a leverage case today; the off-balance-sheet obligations are scored at Q4.

**Case declared: a BINARY GATE** on daily execution. No price compensates.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
1. **The FTC consent order, its violation, and the proceeding to modify it again.** 2019 (FY2019 10-K, `0001326801-20-000013`):
   *"our settlement with the FTC requires us to pay a penalty of $5.0 billion and to significantly enhance our practices and
   processes for privacy compliance and oversight"*, a settlement of *"the FTC's allegations that the Company violated the 2012
   Consent Order"* (derivative Stipulation, 8-K EX-99.1 of 2025-12-12, `0001628280-25-056768`). 2023-05-03 (public in every 10-Q
   since): *"the FTC filed a public administrative proceeding ... seeking substantial changes to the modified consent order ...
   include, among others, a prohibition on our use of minors' data for any commercial purposes, changes to the composition of
   our board of directors, and significant limitations on our ability to modify and launch new products"*, stayed since
   2025-07-30 while Meta's jurisdictional challenges are heard (Q2 2026 10-Q Note 9). Not adjudicated.
2. **The derivative action over the same events**, settled for *"one-hundred-and-ninety million United States dollars
   ($190,000,000) to be paid or caused to be paid by Defendants to Meta"*, funded by the directors' insurers; *"Defendants deny
   any and all allegations of fault, liability, wrongdoing, or damages whatsoever"* (Stipulation, 2025-12-12). Settlement
   hearing set for 2026-04-07; the outcome is not in the Q2 2026 10-Q read.
3. **Youth matters, 2026 (Q2 2026 10-Q Note 9):** *"On March 24, 2026, a jury returned a verdict against us and ordered that we
   pay a civil penalty of $ 375 million"* (New Mexico Attorney General); the abatement claim (*"$ 953 million in abatement costs
   and a broad set of injunctive terms"*) awaits decision; a personal-injury bellwether verdict of *"$ 6 million in compensatory
   and punitive damages"* shared 70/30 with YouTube, appealed; further state trials in 2026-27; the EC's preliminary view under
   the DSA that *"users under 13 years of age are present on Facebook and Instagram and that both platforms present potentially
   addictive design features"*. And *"$2.40 billion of charges related to legal proceedings"* in Q2 2026 (EX-99.1), with the
   CFO's own sentence: *"we continue to see scrutiny on youth-related issues in several markets and have a number of
   youth-related trials scheduled for this year in the U.S., which may ultimately result in a material loss."*
4. **Regulatory fines, all appealed or paid:** *"EUR € 1.2 billion"* (IDPC, GDPR transfers, 2023); *"EUR € 798 million"* (EC,
   Marketplace, 2024); *"EUR € 200 million"* (EC, DMA, 2025); *"EUR € 542 million"* of damages to Spanish media (2025); the Flo
   Health liability verdict (2025-08-01), damages undetermined.
- **[E5-22] is the rule that governs how these are read: penalty size is not seriousness, and the failure that counts is *"they
  didn't act when they learned."*** The filed sequence is a 2012 order, a finding of its violation in 2019, an agency proceeding
  in 2023 alleging the need for a further order, and a 2026 jury verdict of unlawful conduct toward minors. None names an
  officer; every settlement denies wrongdoing; the largest verdict is under appeal or undecided. **Can I name the document that
  would resolve it?** Yes: the New Mexico verdict form and findings (First Judicial District Court, 2026-03-24), and the FTC's
  2023 Order to Show Cause with its preliminary findings. Neither was fetched.
- **Recorded (not governing): UNRESEARCHED on the binary**, with the work order above. Not OUT on the filings read (no finding
  against a person; conduct matters of a corporation are read, not counted). Not IN, because the [E5-22] pattern is present on
  the filed record and the two documents that would test it are nameable.

### THE INCENTIVE READ **[E4-27]**
- **What pay vests on (DEF 14A, 2026-04-16, `0001628280-26-025532`):** the CEO takes *"a base salary of $1 per year in addition
  to his overall security program, and he does not participate in the annual bonus plan or receive additional equity awards"*;
  his interest is his shares. The other officers' cash bonus: *"The company priorities did not have specific target levels
  associated with them for purposes of determining performance under the Bonus Plan, and our compensation, nominating &
  governance committee had full judgment"*; the four priorities were *"Build awesome things. | Make our business successful. |
  Make progress on societal issues related to our business. | Go out and tell our story."*; payout 115% of a target raised in
  2025 from 75% to 200% of salary. Equity is time-vested RSUs. **Nothing vests on cash, margin, or return on the capital being
  spent.** A new President and Vice Chairman (2026-01-12) received RSUs with *"an initial equity value of $60,000,000"* vesting
  over four years (8-K `0001628280-26-002429`).
- **The option grant of 2026, recipients not named in any filing read:** *"we issued nonstatutory stock options to purchase an
  aggregate of 20 million shares of our Class A common stock under the 2025 Plan to certain of our executives and employees.
  These options have a weighted-average exercise price of $ 2,788 per share"*, vesting on *"service and market conditions"* (Q2
  2026 10-Q Note 10); the proxy says *"there were no outstanding options"* at 2025-12-31 and the Q1 2026 10-Q mentions none, so
  they were granted in Q2 2026. **Pay tied to a share price 4.2 times today's**, which is the [E3-50] prompt (the highest stock
  price possible as the job) in its sharpest form; who holds them would be on Form 4s not read here.
- **What insiders did:** five Form 4s of September 2026 are sales by Cox, Olivan and Anderson (Step 0); no purchase found in
  them. Not a survey of the year.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **Weak accounting, one prompt:** server lives lengthened twice, *"effective the second and the fourth quarters of 2022"*
  (*"a reduction in depreciation expense of $860 million"*, FY2022 10-K) and to *"5.5 years, effective January 1, 2025"* (*"a
  reduction in depreciation expense of $ 2.92 billion and an increase in net income of $ 2.59 billion, or $ 1.00 per diluted
  share"*, FY2025 10-K Note 1), while the same filings describe *"an increase in the expected cost of infrastructure hardware"*
  and *"higher component pricing"* (EX-99.1 Q1 2025 and Q1 2026). **Quantified in the filing each time**, which is the candor
  standard met; ticked because the direction (lower depreciation on faster-turning AI hardware) is the one that flatters, and it
  bears on (c) at Q4.
- [ ] **Unintelligible footnotes:** no. The Venture note states the structure, the funding share, the lease, the guarantee and
  *"maximum exposure to loss"* of $45.95bn in plain words.
- [x] **Projections [E4-22], scored against outturn as [E3-48] requires.** Meta guides next-quarter revenue and full-year
  expense and capital spending, not earnings. Revenue guidance, five quarters: Q2 2025 *"$42.5-45.5 billion"* (outturn $47.52bn),
  Q3 2025 *"$47.5-50.5 billion"* ($51.24bn), Q4 2025 *"$56-59 billion"* ($59.89bn), Q1 2026 *"$53.5-56.5 billion"* ($56.31bn),
  Q2 2026 *"$58-61 billion"* ($60.80bn): **met or beaten every time.** Capital spending is the other way, a ratchet: 2025 guided
  *"$60-65 billion"* (January 2025), raised to *"$64-72 billion"*, *"$66-72 billion"*, *"$70-72 billion"*, outturn $72.22bn;
  2026 guided *"$115-135 billion"* (January 2026), raised to *"$125-145 billion"* and *"$130-145 billion"*. Earlier: 2022
  *"$29-34 billion"*, outturn $32.04bn; 2023 cut from *"$34-37 billion"* to *"$30-33 billion"*, outturn $28.10bn; 2024 *"$30-37
  billion"*, outturn $39.23bn. **The revenue guidance is conservative; the spending guidance has been raised in every quarter
  since January 2025.** Ticked for the spending record, which is [E5-30]'s ratchet applied to capital rather than to earnings.
- [ ] **Serial share issuance [E5-15]:** no. Basic weighted shares fell from 2,574M (FY2023) to 2,521M (FY2025) through repurchases (FY2021-25:
  136M, 161M, 92M, 65M and 40M shares retired). **But the direction turned in 2026:** no repurchase in H1 2026, Class A up from 2,187,177,748
  (January) to 2,205,128,509 (July), and RSU grants of 78.9M shares in six months. Recorded as a prompt for the next filing.
- [ ] **EBITDA or adjusted-earnings promotion [E4-29]:** no. The releases' non-GAAP measures are *"revenue excluding foreign
  exchange effect, advertising revenue excluding foreign exchange effect, and free cash flow"* (every release read, Q4 2021 to Q2
  2026); earnings are reported GAAP. The Q4 2022 release quantified its restructuring charges (*"Excluding these charges, our
  operating margin would have been 13 percentage points higher"*), which is disclosure of the item, not a replacement headline;
  recorded under [E2-57] and [E3-53] below.
- [ ] **Filed-figure tells [E4-30]:** cash taxes as a share of pretax income fell: 18.0% (FY2021), 22.2%, 13.9%, 14.9%, **8.8%
  (FY2025)** and about 4.9% in H1 2026 ($1,999M on about $40.6bn). **Explained by law in advance**: *"We expect a significant
  reduction in our U.S. federal cash tax payments for the remainder of 2025 and future years due to the implementation of the One
  Big Beautiful Bill Act"* (Q3 2025 EX-99.1). Not a tell.
- [x] **Metric-switching [E2-49]:** *"Beginning with our Quarterly Report on Form 10-Q to be filed for the first quarter of 2024,
  we will no longer report DAUs, MAUs, ARPU, and MAP"* (FY2023 10-K), the Facebook-app series, replaced by family-level DAP and
  impression and price changes. Announced a quarter ahead, with the replacement named: the candor form of a switch. **Ticked as
  a prompt only**: the withdrawn series is the one that isolated the oldest app, and no filing read gives a reason beyond the
  announcement.
- **[E2-57] and [E3-53]:** restructuring in FY2022-23 (*"Impairment charges for facilities consolidation, net | 2,432 | 2,218"*,
  *"Data center assets abandonment | ( 224 ) | 1,341"*), severance of $1.18bn in Q2 2026. Real costs, and **they stay in the
  owner-earnings mean** (they are inside OCF already) **[E5-33]**.
- **Flags that converge [E4-52]:** three ticks (the depreciation lives, the spending ratchet, the metric switch) point one way,
  toward a build whose cost is recognised later than it is spent. Recorded as a prompt, a reading of the accounting and never of
  the person **[E5-38]**.
- **The auditor's-eye test [E4-34]:** the auditor's critical audit matters include *"Consolidation accounting for a variable
  interest entity"* (the Venture), which is the right place to look; the fourth question (period-shifting) bears on the useful-
  life changes above, and is not answered beyond them.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income on average equity: FY2021 31.1%, FY2022 18.5%, FY2023 28.0%, FY2024 37.1%, FY2025 30.2% (38.2% before the
*"$ 15.93 billion discrete charge recognized in the third quarter of 2025 upon enactment of the One Big Beautiful Bill Act"*,
Q2 2026 10-Q Note 11, a non-cash valuation allowance, partly reversed by *"a discrete income tax benefit of $ 8.03 billion
recognized in the first quarter of 2026"*). Without undue leverage. **High on every year of the record.** [E2-56] asks it by
segment: Family of Apps carries the whole of it, and Reality Labs has consumed $96.7bn since FY2019 (Q1), the Pro-Am
camouflage in its plainest filed form.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
Credits: the segment note shows the Reality Labs loss every year; the Venture's maximum exposure is quantified; each useful-life
change is quantified in dollars and per share; legal charges are quantified at the line; the Q2 2026 release puts the
youth-trial risk in the CFO's own words. Deductions: the Facebook-app user series withdrawn (above); **no filing splits the
$130-145bn between defending the advertising business and building superintelligence**, which is the one fact a half-owner most
needs; the option grant of 2026 is disclosed in aggregate only.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08]:** $44.8bn in FY2021 at an average of about $329 a share (136M shares), then $27.9bn in FY2022 at about $173
  (161M), $20.0bn at about $218 (FY2023), $29.8bn at about $458 (FY2024) and **$26.3bn at about $657 (FY2025)** (equity
  statements, FY2022 and FY2025 10-Ks). Condition (1), ample funds: yes then; in 2026 the company stopped and borrowed $25bn
  (Step 0). **Condition (2), a material discount to value conservatively calculated: on this file's own Q5 computation the FY2025
  purchases at about $657 bought owner earnings at a 1.5-3.0% yield. CAPITAL ALLOCATION FLAG**, stated with the humility clause:
  *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole lot more about them than I do"*
  **[E4-13]**; it binds position size, never the discount rate.
- **Dividends [E2-52, E2-60]:** $5.3bn in FY2025 and $2.7bn in H1 2026, when operating cash after stock pay, capital spending and
  finance-lease principal was **-$0.5bn** for the half and $24.9bn of notes were sold. Paid by borrowing, not by issuing shares,
  so [E2-52]'s letter does not fire; [E2-60]'s third dimension does: where leverage rises to fund a payout, (c) was understated.
- **The institutional imperative [E2-30]:** (2) *projects soak up available funds*: the spending guidance raised in every
  quarter since January 2025 (above) [x]; (3) *the leader's craving supported by studies*: the metaverse ($96.7bn of Reality Labs
  losses) and superintelligence were the founder's turns, and no owner vote can refuse them [x, as a prompt]; (4) *peer
  behaviour imitated*: every filer in the row raised capital intensity in the same two years (Q2 row) [x]. (1) not scored.
  *"Institutional dynamics, not venality or stupidity."*
- **Loss of focus [E3-40]:** the corpus's named worry about outstanding businesses. The base business is still growing (revenue
  +28% in Q2 2026), and the attention of the capital has moved to two new fields; recorded as a Q6 monitoring item.
- **VERDICT (RECORDED, NOT GOVERNING): UNRESEARCHED on the binary** (work order: the New Mexico verdict record and the FTC's 2023
  Order to Show Cause), with three converging accounting prompts, a capital-allocation flag on the FY2025 buybacks, and pay that
  vests on nothing the capital earns.

### THE GUARDRAIL
- [x] Nothing in this Q3 promotes the name; Q2 is closed on the business **[E2-37, E2-38, E3-39]**.
- [x] Key-person control recorded at Q2 as a defect **[E4-23]**.
- [x] No great-manager exception is claimed.

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The brief asked for the owner-earnings rebuild over every window the filed statements support,
> both (c) ends, the finance leases and the off-balance-sheet build; it is done here and it governs nothing.

### Owner earnings — the one number **[E2-23]**
**Windows: every one the faces read support**, FY2017-25 and the twelve months to 2026-06-30 (`oe.py`, `oe_out.txt`, $M, every
input from the filed faces: FY2019 10-K for FY2017-18, FY2021 10-K for FY2019-20, FY2023 10-K for FY2021-22, FY2025 10-K for
FY2023-25, Q2 2026 10-Q for H1; capex net of the small proceeds line throughout, to match the FY2025 face). **Five years
FY2021-25 is the default [E2-42].** Owner earnings = OCF − SBC − (c); the capex end subtracts capital expenditure **and
finance-lease principal** (the cash cost of finance-leased plant, which the capex line does not see).

| FY | OCF | SBC | D&A | capex | finance-lease principal | acquisitions | **OE, D&A end** | **OE, capex end** | capex end less acquisitions | (capex + FL) / D&A | SBC / OCF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2017 | 24,216 | 3,723 | 3,025 | 6,733 | 0 | 122 | 17,468 | 13,760 | 13,638 | 2.23 | 15.4% |
| 2018 | 29,274 | 4,152 | 4,315 | 13,915 | 0 | 137 | 20,807 | 11,207 | 11,070 | 3.22 | 14.2% |
| 2019 | 36,314 | 4,836 | 5,741 | 15,102 | 552 | 508 | 25,737 | 15,824 | 15,316 | 2.73 | 13.3% |
| 2020 | 38,747 | 6,536 | 6,862 | 15,115 | 604 | 388 | 25,349 | 16,492 | 16,104 | 2.29 | 16.9% |
| 2021 | 57,683 | 9,164 | 7,967 | 18,567 | 677 | 851 | 40,552 | 29,275 | 28,424 | 2.42 | 15.9% |
| 2022 | 50,475 | 11,992 | 8,686 | 31,186 | 850 | 1,312 | 29,797 | 6,447 | 5,135 | 3.69 | 23.8% |
| 2023 | 71,113 | 14,027 | 11,178 | 27,045 | 1,058 | 629 | 45,908 | 28,983 | 28,354 | 2.51 | 19.7% |
| 2024 | 91,328 | 16,690 | 15,498 | 37,256 | 1,969 | 270 | 59,140 | 35,413 | 35,143 | 2.53 | 18.3% |
| 2025 | 115,800 | 20,427 | 18,616 | 69,691 | 2,524 | 4,231 | 76,757 | 23,158 | 18,927 | 3.88 | 17.6% |
| **12m to 2026-06-30** | 130,301 | 25,136 | 22,729 | 89,325 | 3,104 | 4,643 | 82,436 | **12,736** | 8,093 | **4.07** | 19.3% |
| **5y FY2021-25** | | | | | | | **50,431** | **24,655** | 23,197 | | |
| 3y FY2023-25 | | | | | | | 60,602 | 29,185 | 27,475 | | |
| 9y FY2017-25 | | | | | | | 37,946 | 20,062 | 19,123 | | |
| before the build FY2017-21 | | | | | | | 25,983 | 17,312 | 16,910 | | |

- **The screen is reproduced at the D&A end** ($50,430.8M at `a8bc84f` against $50,431M; the $1M is FY2024 D&A, 15,501 tagged
  against 15,498 on the FY2025 face). **At the capex end the screen gives $25,624.6M against this file's $24,655M**: the screen
  subtracts finance-lease right-of-use *additions* ($160-613M a year, a non-cash figure) and gross capex, where this file
  subtracts finance-lease *principal paid* ($677-2,524M) and net capex. The cash construction is the stricter one.
- **H1 2026 alone, capex end: -$520M** (64,088 − 13,690 − 49,113 − 1,805). The company's own Q2 2026 free cash flow, before stock
  pay, was *"$784 million"* (EX-99.1).
- **What the working-capital increment is made of [E2-23]:** small and not the story. FY2025's six working-capital lines sum to
  -$885M (receivables -$1,815M, accrued liabilities +$1,077M); H1 2026's to -$7,258M (other liabilities -$4,528M, prepaid -$3,230M,
  other assets -$2,535M, receivables -$2,273M, accrued +$5,662M), a half-year swing inside the build. The one-time tax items are
  non-cash and sit in *"Deferred income taxes | 18,738"* (FY2025), so OCF is not distorted by them. The growth in plant payables is
  the larger unseen item: *"Property and equipment in accounts payable and accrued expenses and other current liabilities"*
  $9,331M at 2025-12-31 and **$19,502M at 2026-06-30** (10-Q face), capital already bought and not yet paid for, which will reach
  the capex line in later periods.
- **Maintenance capex, a DISCLOSED JUDGMENT, and the [E5-20] exception class APPLIES.** (i) Capital-intensive by the filing: net
  plant $225.7bn at 2026-06-30 against twelve-month revenue of $228.2bn; capex plus finance-lease principal 4.07 times D&A. (ii)
  The filer's own evidence that depreciation understates renewal: server lives lengthened twice (2022, 2025) while hardware cost
  rises (*"an increase in the expected cost of infrastructure hardware"*, *"higher component pricing"*), which is [E4-47]'s
  current-dollar condition. (iii) Plant already bought is not yet in D&A: construction in progress $50,521M at 2025-12-31, and
  $19.5bn of plant payables. **So the D&A end is INVALID, not merely optimistic** (v4, Q4), and (c) is judged upward from D&A
  toward total capex. **Where in the band:** no filing splits maintenance from growth. The company's own statement for 2025 was
  *"The majority of our capital expenditures in 2025 will continue to be directed to our core business"* (Q4 2024 and Q1 2025
  EX-99.1), and the 2026 guide names *"our Meta Superintelligence Labs efforts and core business"* without proportions. **The run
  sets (c) at total capex plus finance-lease principal (the capex end) as the central case**, on the filer's own word that most
  of the spending serves the core business it is defending (Q2: the spending is what holds the position), and shows the D&A end
  only as the display of the guess.
- **The off-balance-sheet build (c) must also see, and the capex end does not:** $278.99bn of leases not yet commenced at
  2026-06-30 plus about $68bn signed in July 2026 (**about $347bn**, terms up to 30 years); the Louisiana Venture (Meta's 20% of
  about $27bn of development, $12.31bn of initial lease commitments from 2029, a $28bn residual value guarantee, maximum exposure
  $45.95bn); and $349.31bn of non-cancelable purchase commitments, *"mostly"* cloud capacity and infrastructure, $53.52bn due in
  the rest of 2026 and $81.65bn in 2027. When the leases commence, their cost passes through OCF; **at an 18-20-year term
  (the July 2026 leases' stated term), $347bn is roughly $17-19bn a year of lease cost that no year in the table above bears.**
- **The perimeter items:** acquisitions of businesses are shown as their own column (FY2025 $4,231M). The **Scale AI** stake
  (*"$ 13.80 billion"*) and other *"Purchases of non-marketable equity investments | ( 18,330 )"* (FY2025) are investments, not
  (c); they add no owner earnings and no look-through is possible [E3-04]. The Venture's formation (*"Payments for held-for-sale
  assets | ( 2,432 )"*, *"Proceeds from Venture distribution | 2,554"*) nets to about zero in FY2025.
- **SBC, resolved and complete on the face in every year used:** *"Share-based compensation"* 3,723 to 20,427 ($M) on each face,
  matching the note total (FY2025 *"Total | $ | 20,427"*); no capitalised SBC disclosed; H1 2026 face 13,690 against the RSU note
  13,626 (the $64M difference is the new options). SBC/OCF 13-24%, the high teens as the brief said. **[E3-70], the market
  measure, read by hand from the RSU tables:** grants net of forfeitures at grant-date value were **$22.7bn gross (FY2023),
  $24.7bn (FY2024), $46.1bn gross and $40.4bn net (FY2025: 69,666K granted at $661.57, 14,840K forfeited at $379.82), and $38.6bn
  net in H1 2026 alone** (78,904K at $598.76 less 16,194K at $533.48), against charges of $14.0bn, $16.7bn, $20.4bn and $13.7bn.
  *"unrecognized share-based compensation expense for RSU awards was $ 79.79 billion"* at 2026-06-30. **At the grant-value
  measure, FY2025 capex-end owner earnings fall from $23.2bn to about $3.1bn, and H1 2026 to about -$25.4bn.** The charge is the
  floor of the subtraction, as [E3-70] requires, and it is far below the measure now.
- **[E4-41], normalize down for luck:** FY2025-26 cash taxes are lowered by legislation (Q3); the FY2021 year carried the
  pandemic advertising rebound (*"a recovery from declines in advertising demand in the first two quarters of 2020"*). Nothing is
  normalized up.
- **Short-window mean (3y FY2023-25): $29.2bn at the capex end ($60.6bn at the invalid D&A end). Long-window mean (5y FY2021-25,
  the default): $24.7bn ($50.4bn). Twelve months to 2026-06-30: $12.7bn. At the [E3-70] measure, FY2025 about $3bn and H1 2026
  negative. Combined range, capex end, before the off-balance-sheet leases: about $0-29bn a year, and falling through the
  window's end.** **Is the range too wide to conclude? The width is the question:** the top of it is a business that earned $29bn
  for owners in 2023-25, the bottom a business spending everything it earns on a build whose return no filing states.

### Great, good, or gruesome? **[E4-20, E4-43]**
- **Before the build (FY2017-21): great or good** (owner earnings $11-29bn a year rising, capex 2.2-3.2 times D&A on a growing
  fleet). **Now: undecidable on the filings.** *"grows rapidly, requires significant capital to engender the growth, and then
  earns little or no money"* describes the twelve months to June 2026 at the capex end ($12.7bn, 0.75% of the cap) and H1 2026
  (-$0.5bn); **[E4-43]'s good class** (*"unless the cash they consume gets to earn a reasonable return"*) is exactly what no
  filing yet shows for the AI build. **The capex band changes the class, so by the template's own rule the recorded verdict is
  UNKNOWABLE.**

### Staying power — score all three **[E5-11]**
- **(1) Large and reliable stream:** **yes** for operating cash ($130.3bn in twelve months); **no longer** for owner cash (above).
- **(2) Massive liquid assets:** **yes**, $90.26bn of cash, cash equivalents and marketable securities (2026-06-30), plus $13.1bn of
  restricted cash in other assets; against $83.66bn of long-term debt.
- **(3) No significant near-term cash requirements: FAILS.** $53.52bn of purchase commitments due in the rest of 2026 and $81.65bn
  in 2027; capital spending guided at $130-145bn for 2026; $19.5bn of plant payables; interest obligations of *"$4.40 billion"* in
  the next twelve months; $347bn of leases commencing from 2026 to 2036; the Venture guarantee. **[E5-11]: *"Ignoring that last
  necessity is what usually leads companies to experience unexpected problems."***
- **Leverage and coverage [E4-16, E2-54]:** debt $84.0bn of notes *"which mature from 2027 through 2066"*, up from $18.4bn at
  2023-12-31 (*"Long-term debt | 18,385"*, FY2023 10-K). **[E2-54]'s test (interest met out of cash flow net of ample capex):** H1 2026 OCF less capex and finance-lease
  principal was $13.2bn against $1.1bn of interest paid; **Q2 2026 alone, $0.78bn (the company's free cash flow) against
  twelve-month interest obligations of $4.40bn, about 0.7 times on an annualised quarter.** [E5-39] (*"We will never be dependent
  on the kindness of strangers"*): the 2026 build is being financed in the bond market.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism, stated as its holders would accept it:** Meta does not die; **its owners' return does.** The advertising
  business keeps producing $100bn-plus of segment operating income, and the founder, whom no vote can overrule, recycles it into
  races that must be re-won: the metaverse ($96.7bn of losses since FY2019) and now superintelligence and AI capacity, with
  every large rival raising its own capacity in the same years (*"viewed collectively, the decisions neutralized each other and
  were irrational"* **[E2-27]**). **This is shape #10, THE CAMOUFLAGE (SONY)**: cash from the strong leg recycled into legs that
  must re-win a race each cycle; **with #1, CONTRACTED NOT TO STOP (ORCL), as its feature** ($349bn of commitments and $347bn of
  signed leases oblige the spending whether or not it earns), **and #2, EARNS NOTHING FOR OWNERS AFTER PAYING ITS PEOPLE, at the
  [E3-70] measure** (grants of $38.6bn net in six months). No new shape is proposed.
- **The exposure, quantified from filed figures [E4-40]:** if the build earns nothing beyond today's advertising, the costs
  still arrive: net plant of $225.7bn on the company's own *"5.5 years"* server life (a blended plant life is longer; this is the
  upper case) is up to about $41bn a year of depreciation against FY2025's $18.6bn, and the signed leases add roughly $17-19bn a
  year as they commence: **about $40bn of annual cost against FY2025 operating income of $83.3bn**, before the purchase
  commitments. Owner earnings at the capex end would stay near zero for as long as the build continues, as they did in H1 2026.
- **Likelihood:** owner earnings near zero while the build runs, **likely** (it is the filed present, H1 2026, and the guidance);
  the build failing to earn a return that restores them, **a real possibility** (no document states the return); insolvency, **a
  low-level possibility** ($90bn of liquidity, notes laddered to 2066).
- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN [ ] OUT [ ] UNRESEARCHED [x] UNKNOWABLE.** *Can I name the document that would
  resolve it? No.* The (c) judgment turns on how much of $130-145bn a year is needed to hold the advertising position and what
  the rest earns, and no filing separates them or states a return; the capex band changes the great/good/gruesome class
  **[E4-25, E4-20]**; strength 3 fails **[E5-11]**.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT. The block below is arithmetic only.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
Cap **$1,696.0bn** ($665.75 x 2,547,506,225, Class A and Class B one for one); sovereign **5.34%** (US Treasury 30 Yr,
09/18/2026). Owner earnings are after tax; the comparison is shown as the runs have shown it.

| owner earnings case | $bn a year | yield on the cap | vs 5.34% |
|---|---:|---:|---:|
| 5y FY2021-25, capex end (central) | 24.7 | 1.45% | -3.89 |
| 5y FY2021-25, capex end less acquisitions | 23.2 | 1.37% | -3.97 |
| 3y FY2023-25, capex end | 29.2 | 1.72% | -3.62 |
| twelve months to 2026-06-30, capex end | 12.7 | 0.75% | -4.59 |
| FY2025, capex end with SBC at grant value [E3-70] | about 3.1 | about 0.2% | about -5.2 |
| 5y FY2021-25, D&A end (INVALID for this class; display only) | 50.4 | 2.97% | -2.37 |
| twelve months, D&A end (INVALID; display only) | 82.4 | 4.86% | -0.48 |

- **Every case, including the invalid one, sits below the bond.** With the unvested RSUs in the count ($1,793.5bn), each yield
  falls by about a twentieth of itself.
- **What the price already assumes:** a 10% pre-tax return **[E4-28]** on $1,696bn needs about **$170bn a year** of owner
  earnings: **6.9 times** the five-year capex end, 3.4 times the invalid D&A end, 13 times the last twelve months. In growth terms,
  the gap from a 1.45% yield to the floor is about 8.6 points a year in perpetuity. **[E4-35]:** fewer than one in twenty of the
  most profitable companies sustain 15% a year for twenty years; **[E4-44]:** value cannot outgrow earnings, and here the
  owner earnings are falling while revenue grows 22-28%, because the capital is growing faster. The Q1 exclusion binds: none of
  the superintelligence or enterprise-AI revenue may be counted here.
- **The value, as a round-number range [E4-01]**, at the ~10% floor with no growth: capex end five-year, about **$250bn ($97 a
  share)**; three-year, about $290bn ($115); the invalid D&A end, about $500bn ($200). **Price $665.75 is about 3.3 to 7 times
  that range.** Bar 2, the screamer test **[E4-01]**: the price is above the whole range; the answer would be *no*. **Windage
  count: zero** (the capex end is the (c) judgment, not a margin; the D&A end is shown; nothing else was lowered).
- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a yield of 0.75-1.72% at the capex
  end against a 5.34% bond and a ~10% floor, with the price 3.3 to 7 times a no-growth floor value.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed (a Q2 OUT is a finding about the business, and a price
> alert on it would be a category error, the QLYS ruling). These are the conditions on which the file would be reopened,
> written before any reopening **[E1-02]**.

**What would reverse Q2 (the governing gate), in words:**
1. **Pricing shows up across a cycle:** average price per ad rising for five consecutive years, including at least one year in
   which impressions grow less than 5%, so that price rises against flat demand [E2-44](1), [E4-55].
2. **The substitute finding is reversed on the record:** the D.C. Circuit reverses the 2025-11-18 judgment on the ground that
   TikTok and YouTube are not in Meta's market, **and** Meta's own 10-K drops the sentence that users engage with *"other products
   and services similar to, or as a substitute for, our products"* [E3-03](2).
3. **The capital returns to minor:** capital expenditure plus finance-lease principal below 25% of revenue for three consecutive
   years with revenue growing, or a filed disclosure that splits the build into core-business maintenance and new-business
   investment and shows a return on the second [E2-44](2), [E4-04].
4. **Owner cash:** operating cash less stock pay (at grant value, [E3-70]) less capex and finance-lease principal positive and
   rising over a rolling five-year window, without net borrowing in it.

**What would close it harder:** DAP falling year on year; the price per ad falling while impressions rise, as in FY2022-23; the
2026 capital guide raised again or a 2027 guide above it; an FTC order modifying the consent order; the New Mexico abatement or
the multistate youth trials going against Meta at scale; further RSU grants at the H1 2026 pace.

**Next catalyst dates:** the Q3 2026 10-Q and release (late October 2026); the FTC's appeal in the D.C. Circuit; the New Mexico
abatement decision; the multidistrict state attorneys general trial scheduled to begin 2026-08-12.

**The sell rule [E2-28]** does not apply (nothing held). **Position size:** none.
**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT, on the business); Q3-Q6 recorded beneath explicit RECORDED,
  NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed segment notes and the
  impression and price series FY2019 to H1 2026; superintelligence, enterprise AI and Reality Labs as businesses are excluded
  by name.
- [x] The one UNRESEARCHED verdict (Q3, recorded) names its artifacts and where they live: the New Mexico verdict record (First
  Judicial District Court, 2026-03-24) and the FTC's 2023 Order to Show Cause.
- [x] The one UNKNOWABLE verdict (Q4, recorded) states what cannot be known: the split of $130-145bn a year between holding the
  advertising position and building new businesses, and the return on the second; no filing states either.
- [x] Step 0: the skip reason tested on the inline XBRL of the latest 10-Q (the count is tagged per class with a dimension, which
  companyfacts omits); the entity checked; the filing read with accession numbers; OCF, SBC, D&A, capex, finance-lease principal
  and revenue cross-checked to the FY2025 10-K face, with the two vintage differences named.
- [x] Owner earnings on the five-year default and on three-year, nine-year, pre-build and twelve-month windows; both (c) ends
  with the D&A end declared INVALID under [E5-20] and shown as display; finance-lease principal subtracted; acquisitions in their
  own column; the off-balance-sheet leases, the Venture and the commitments quantified beside the table; SBC at the [E3-70]
  grant-value measure read by hand from the RSU tables.
- [x] Competitor row filled from five SEC filers (Alphabet with its Services segment, Amazon's advertising line, Snap, Pinterest,
  Reddit), companyfacts re-fetched and one operating-cash figure per peer found on its own FY2025 10-K face; the unlisted
  rivals (TikTok/ByteDance, X, OpenAI) named; the class not PROVISIONAL, with the directional reason.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the cached
  09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a round-number range under COMPUTATION — NOT A CLEARANCE ($250-500bn at the floor with no growth, the top
  on the invalid D&A end).
- [x] One bar (the screamer test); windage count zero, stated.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, the series corroborated by three Form 4 sale prices inside the
  day's range.
- [x] Share count from the latest 10-Q cover with its accession; the A/B addition justified from the charter's equal-status,
  dividend, liquidation, merger and conversion clauses; dilution (RSUs and the 2026 options) shown beside the cap.
- [x] Deal check run on EDGAR: none live.
- [x] Run committed after the template, after Step 0, after Q1-Q2, and after Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`, a sweep of every id in the file: none missing).
- [x] No em dashes in anything this session wrote (the template's headings and the required `COMPUTATION — NOT A CLEARANCE`
  heading carry them; one heading of mine that carried one was changed to a colon before the Q3-Q6 commit).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded 10-Ks, 10-Qs, 8-Ks, proxy, charter, court opinion, peers' 10-Ks and companyfacts
  were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Step 0, corrected before its commit:** a first draft said the 8-Ks *"of the last two years"* carried Item 7.01 (the last
   7.01 was 2023-03-14); rewritten as *"filed since 2024-08"*. A first attempt to write Step 0 through a bash heredoc failed on an
   apostrophe (the brief's warning); rewritten through a file.
2. **Q1-Q2, corrected before commit:** impressions were first compounded *"2.07 times over FY2021-25"* using the FY2021
   growth rate (which is FY2020 to FY2021); corrected to 1.88 times from FY2021 to FY2025. The twelve-month operating-income
   increase was first written $40.1bn (it is $40.2bn). *"formats replaced three times (feed, Stories, Reels)"* is two
   replacements; corrected. The court quotation was first introduced as the court *"ultimately finds"*; the opinion's sentence
   begins *"The Court ultimately finds"* and is now quoted whole.
3. **Q1-Q2's first commit attempt failed** because `git add` refused an ignored research file (`legal_10Q_2026Q2.txt`) and the
   chained commit did not run; the commit was re-run without it (`5f8d195`). Nothing was lost.
4. **Q3-Q6, corrected before commit:** a sentence citing a *"2,854M-class"* historical share count had no source on disk and was
   replaced by the filed weighted basic counts (2,574M FY2023, 2,521M FY2025); the multistate youth trial was described as
   *"begun"* on 2026-08-12 when the 10-Q says it was *"scheduled to begin"*; the no-growth value per share was $95 (it is $97).
5. **A judgment disclosed, not an error:** the FTC opinion was read from the court's own server, a rung the v4 evidence ladder
   does not list (it lists SEC, company and exchange rungs); the GOOGL run used the court-record rung the same way. It is cited
   for what the court found and what Meta argued, not for any number.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"Latest 10-K: FY2025, filed 2026-01-29 (per the dei public-float fact)" (section 1):** held (`0001628280-26-003942`). The
   brief did not give the 10-K accession; supplied here.
2. **The skip-reason hypothesis (section 1):** held exactly, and more precisely than stated: the cover *does* carry
   `dei:EntityCommonStockSharesOutstanding`, twice, each fact dimensioned by `us-gaap:StatementClassOfStockAxis`; companyfacts
   drops dimensioned facts. "No share count from dei" means "no *undimensioned* share count".
3. **"Capex 15.1, 15.1, 18.6, 31.4, 27.3, 37.3, 69.7" (section 2):** FY2021-23 are the gross figures from the earlier faces; the
   FY2025 face nets a small *"Proceeds relating to property and equipment"* line (FY2023 27,045 against 27,266). Immaterial;
   named in Step 0.
4. **"FinanceLeasePrincipalPayments $2.5bn FY2025 ... finance-lease capex is capex the capex tag does not see" (section 2):**
   held; the screen's capex end subtracts finance-lease right-of-use *additions* ($613M in FY2025), not principal ($2,524M), which
   is why its $25.6bn differs from this file's $24.7bn.
5. **The memory-sourced beliefs (section 3), settled:** Class B ten votes, one-for-one conversion, founder control: **held**
   (charter and 10-K). Two segments with Reality Labs losing $15-20bn a year: **held** ($16.1bn, $17.7bn, $19.2bn FY2023-25;
   $10.2bn and $13.7bn in FY2021-22). The Q3 2025 tax charge: **held** ($15.93bn, OBBBA, partly reversed by an $8.03bn CAMT
   benefit in Q1 2026). Scale AI: **held** ($13.80bn minority stake, measurement alternative). The Louisiana joint venture:
   **held, and off the balance sheet** (20% equity-method interest, unconsolidated VIE, $45.95bn maximum exposure); the name
   "Hyperion" appears in no filing read. 2026 capex far above 2025: **held** ($130-145bn guided against $72.2bn including
   finance-lease principal). The FTC monopolisation case: **decided for Meta** (2025-11-18), FTC appeal filed 2026-01-20; and
   the ground of the decision, that TikTok and YouTube are in Meta's market, decided Q2. EU DMA decisions and fines: **held**
   (EUR 200M, 2025; plus a June 2026 interim measure on WhatsApp). Competitors in the 10-K: **the 10-K names TikTok (once, as a
   cause of reduced engagement), Apple and Google (as platform owners), and no other rival**; Alphabet and Amazon name no
   competitor at all, and Snap, Pinterest and Reddit name Meta.
6. **The brief did not know** about the $349.31bn of commitments and $347bn of signed leases at mid-2026, the RSU grants of
   $47.2bn gross in H1 2026 ($79.79bn unrecognized), the 20 million options at $2,788, the $2.4bn Q2 2026 legal charges, the New
   Mexico $375M verdict, or the $190M derivative settlement; each is in the file.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.sovereign()` served the cached 09/17 row** at 22:03 EDT while the Treasury had published 09/18: the seventh
  reproduction.
- **`sources._chart()` returned `close None` for the day's bar** after the close, as at BX and AEHR.
- **`share_count_shift` and every dei reader miss per-class covers.** A reader of the inline XBRL cover (the raw 10-Q, not
  companyfacts) would find the dimensioned facts; `Screens/cover_shares.py` already does this and correctly refuses to add them.
  The remaining names in this row (DASH, PATH, PUBM, BZFD) should be checked for the same dimensioned-cover pattern first.
- **The screen's capex end subtracts finance-lease ROU additions, not principal paid**, which understates the cash cost of
  finance-leased plant wherever principal exceeds additions (Meta FY2025: $2,524M against $613M).

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Read the company's own litigating position.** Meta's 10-K says users have substitutes; in court, on a full trial record, Meta
argued its market *"at a minimum includes TikTok and YouTube"*, and won. A company that has proved in court that it has close
substitutes has answered [E3-03]'s second criterion for us.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)**, at Q2. [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** META CLOSES AT Q2 (OUT, ON THE BUSINESS, [E3-03] criterion 2, with [E4-04], [E4-55], [E4-38], [E2-44], [E3-46],
  [E3-51], [E2-59], [E4-23]): the FY2025 10-K says users are *"actively engaging with other products and services similar to, or
  as a substitute for, our products"*, names TikTok, and says marketers spend *"only a relatively small portion of their overall
  advertising budget with us"*; the D.D.C. held on 2025-11-18, on Meta's own argument, that *"YouTube and TikTok belong in the
  product market, and they prevent Meta from holding a monopoly"*; the average price per ad compounds to 0.97 times FY2018's over
  seven filed years while impressions grow; the company describes its business as *"characterized by innovation, rapid change,
  and disruptive technologies"* and holds its position by rebuilding the basis, now at $130-145bn a year of capital spending
  (capex/revenue 15.8% FY2021 to 34.7% FY2025) with $349bn of commitments and $347bn of signed leases, no filing splitting defence
  from replacement; the EU caps the terms in 23% of revenue; founder control recorded. On a five-filer row it is the margin and
  owner-cash leader. Q1 IN (advertising by auction on four apps, 97.6% of revenue; superintelligence, enterprise AI and Reality
  Labs outside the circle). Q3 recorded UNRESEARCHED on the binary (the [E5-22] pattern: the 2012 FTC order, its $5.0bn
  violation settlement in 2019, the 2023 modification proceeding, the 2026 New Mexico $375M jury verdict; work order: that
  verdict record and the FTC Order to Show Cause), with prompts on server-life extensions, a capital-spending guidance ratchet and
  the withdrawn Facebook-app series, a capital-allocation flag on FY2025 buybacks at about $657, pay vesting on nothing the capital
  earns, and 20 million options at $2,788. Q4 recorded UNKNOWABLE: owner earnings five-year FY2021-25 **$24.7bn at the capex end
  (central; the D&A end $50.4bn is INVALID under [E5-20])**, $12.7bn for the twelve months to June 2026, about $3bn in FY2025 with
  SBC at grant value [E3-70]; strength 3 fails; shape #10 THE CAMOUFLAGE with #1 and #2 as features. Price $665.75 x 2,547,506,225
  = $1,696.0bn, headed COMPUTATION — NOT A CLEARANCE: yield 0.75-1.72% at the capex end against 5.34% and a ~10% floor, which would
  need about $170bn a year; Q6 records the reversal condition in words and arms nothing.
- **The skip reason, as it turned out:** a tagging convention, not a missing count. The 10-Q cover carries both class counts
  under `dei:EntityCommonStockSharesOutstanding`, each dimensioned by class of stock, and companyfacts publishes only
  undimensioned facts. The charter makes the classes economically identical, so the count is their sum.
