# Company Run — Trump Media & Technology Group Corp. (DJT) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Fill top to bottom. **Stop at the first verdict that is not IN.**

Run unattended from scratch on 2026-09-18 (evening, EDT); the template was copied and committed before any fetch
(`e95031e`). No prior run file for DJT exists. WAVE 5, the fifth of the seven "perimeter or restatement above
threshold" names. Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-18 DJT/`; the brief is
`_BRIEF.md` there. Sections were written as they closed and committed after each gate. **The subject has political
prominence; this file keeps to the business, its filings and its management's conduct as filed, and quotes documents.**

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
## STEP 0: THE SKIP REASON, THE ENTITY IN EACH YEAR, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### Which entity each tagged year belongs to (the de-SPAC question, settled first)
The registrant (CIK 0001849635) was **Digital World Acquisition Corp. ("DWAC")**, a blank-check company incorporated
2020-12-11 (`submissions.json`: former name *"Digital World Acquisition Corp."* to 2024-03-22). The operating company,
Private TMTG, was incorporated 2021-02-08 and combined with DWAC on **2024-03-25**. The FY2025 10-K, Note 1: *"the
Initial Business Combination has been accounted for as a reverse recapitalization in accordance with U.S. GAAP because
TMTG is the operating company and has been determined to be the accounting acquirer ... while Digital World is a blank
check company"*, and *"the historical financial statements of Predecessor TMTG became the historical financial
statements of the combined company."* **So every filed statement from the FY2024 10-K onward is the operating company's
history; every annual filing before it (the 10-Ks of 2022-04-13, 2023-04-26 and 2024-04-01, and the 10-K/As of
2023-10-30, 2024-01-09 and 2024-04-03) is the shell's.**

**Companyfacts holds both under the same keys, and the screen read the shell for three years** (`companyfacts.json`,
read by this run):

| element | FY | value ($M) | accession | whose |
|---|---|---:|---|---|
| NetCashProvidedByUsedInOperatingActivities | 2021 | (1.11) | DWAC 10-K `0001193125-22-103731` | **shell** |
| same | 2022 | (1.38) | DWAC 10-K `0001193125-23-116102` | **shell** |
| same | 2022 | (24.20) | TMTG 10-K `0001140361-25-004822` | operating company |
| same | 2023 | (5.14) | DWAC 10-K `0001140361-24-017011` | **shell** |
| same | 2023 | (9.73) | TMTG 10-K `0001140361-25-004822`, `0001140361-26-007174` | operating company |
| NetIncomeLoss | 2022 | (15.6) shell / **+50.5** TMTG | both | collide |
| RevenueFromContractWithCustomer... | 2022-25 | 1.47, 4.13, 3.62, 3.68 | TMTG 10-Ks only | operating company (the shell had no revenue) |

The brief's operating-cash series (FY2021 -1.11, FY2022 -1.38, FY2023 -5.14) is **the shell's**; the operating
company's is **FY2021 (3.80), FY2022 (24.20), FY2023 (9.73)** (FY2021 from the DWAC S-4 prospectus, 424B4 of
2024-02-16, `0001193125-24-038590`, Private TMTG's statement for the period from inception, 2021-02-08, to 2021-12-31;
FY2022-23 from the FY2024 10-K). **The screen's three-year owner earnings (-$76.1M D&A end, -$74.5M capex end) mixed
the shell's FY2023 operating cash (-$5.14M) with the operating company's FY2024-25**; on the operating company's own
figures the FY2023-25 means are **-$77.7M and -$76.1M** (Q4). The difference is small here; the entity collision is
the finding, and it is the RGTI kind.

**The shell was itself restated.** DWAC's 10-K/A of 2023-10-30 (`0001193125-23-265441`) is a comprehensive report that
*"contains restatements of"* its FY2021 and FY2022 audited statements and three 2022 quarters, which is why
companyfacts carries three vintages of the shell's FY2021 operating cash (-1.11, -0.92, -1.14). That restatement is of
the blank-check company's statements, not of the business.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list: *"revenue step
or cross-accession restatement above threshold."* **A prompt to read, never a verdict.** Reproduced by the brief-writer
against `Screens/floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py`) over companyfacts cut to facts filed by
2026-09-01 (`triage_repro.py`, `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | 1.281 | no (inside 0.75-1.50) | chiefly the 2025 PIPE (55,857,181 shares, May 2025), with the Cronos exchange (2,797,985 shares) and vesting, net of buybacks; no split (`split_factor_after` 1.0) |
| **2. `scale_shift`** | **2.809** | **YES: THE GUARD THAT RETURNED DJT UNPRICED** | **A REAL STEP AT THE OPERATING COMPANY, NOT A PERIMETER.** FY2022 $1.47M to FY2023 $4.13M, consecutive years (the TSLA check was run: 2022-12-31 and 2023-12-31), both years Private TMTG's (the shell had no revenue element). The FY2024 10-K MD&A: *"Revenues increased by $2,660.6, or 181%, to $4,131.1 for the year ended December 31, 2023 compared to revenue of $1,470.5 for the year ended December 31, 2022. The increase was primarily the result of enhanced early-stage testing of a nascent advertising initiative on our Truth Social platform."* Truth Social launched in the first quarter of 2022 and advertising was sold through Rumble from August 2022 (Rumble Agreement of 2022-08-19, S-4 prospectus), so FY2023 was the first full year of advertising. The step is measured off a base of $1.47M. |
| 3. `filed_years` | 5 | no | FY2021-25 under the revenue-and-cash keys, but FY2021 operating cash is the shell's (above) |
| 4. `owner_earnings` | 3y D&A -$76.1M, 3y capex -$74.5M | no (priced, negative) | the triage stopped at guard 2; the figures mix entities (above) |
| (`restatement_shift`, not a guard in that pipeline) | (1.0, FY2023) | n/a | a null, as at SMCI, SNOW, TSLA and RIVN |

**So the label was, for DJT: a real organic revenue step off a near-zero base (the first full year of advertising),
not a perimeter event and not a restatement of the business.** Two things the label's words name DID happen and no
guard read either: **a perimeter** (the reverse recapitalization of 2024-03-25, which put a shell's and an operating
company's years under the same keys), and **a restatement** (the shell's own, 2023-10-30). Checked on the documents:
the FY2025 10-K cover leaves the error-correction box unticked; the one 10-K/A for FY2025 (2026-04-30) is a Part III
amendment (*"The Original 10-K Filing omitted certain information required by Part III"*); no 10-Q/A exists in the
702-filing index (`filings_list.txt`).

**SBC tags FY2022-23 as zero: the face agrees.** The FY2024 10-K cash-flow statement reads *"Stock based compensation |
107,387.1 | - | -"* (FY2024, 2023, 2022): Private TMTG had no equity plan before the combination; the 2024 Equity
Incentive Plan began after it. Not the SBC-of-zero tag defect. `working_capital_flag` (payables, 182% of FY2025 operating
cash) is taken up at Q4 and shown both ways.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned the cached **09/17/2026 5.29%** row (`step0_out.txt`), the stale-cache
  defect recorded four times now; the issuing-authority figure is used. FRED was not used. Not inherited from RIVN.
- **Earnings currency: USD.** A Florida corporation in Sarasota; revenue is US advertising, subscriptions and ETF fees;
  the treasury assets are priced in dollars. No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$8.85, the close of 2026-09-18** (Friday). Source: Yahoo Finance daily chart via `sources._chart("DJT", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`). Bar: open 8.73, high 8.88,
  low 8.65, close 8.85, volume 4.50M; `regularMarketTime` 1789761602 = 16:00 EDT, so the figure is the closing print.
  `tools/sources.price()` returned the same 8.85 stamped 2026-09-18.
- Recent closes: 09-11 $8.66 · 09-14 $8.85 · 09-15 $8.58 · 09-16 $8.55 · 09-17 $8.68 · 09-18 $8.85. One-month range of
  closes $8.35-$9.77.
- **Primary-filing cross-check:** Form 4 `0001437749-26-028743` (Kevin McGurn, Interim CEO) reports a tax-withholding
  disposition of 7,958 shares on **2026-08-21 at a weighted $8.8864** (*"prices ranging from $8.685 to $9.10"*), inside
  Yahoo's 08-21 bar (low $8.65, high $9.195); Form 4 `0001437749-26-027758` reports 16,509 shares on 2026-08-13 at a
  weighted $8.3252. **Corroborated.**
- **Split factor after the count's date (2026-08-07): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **277,941,274 shares**, from the cover of the **Q2 2026 Form 10-Q** (quarter ended 2026-06-30, filed **2026-08-10**,
  accession **`0001437749-26-026777`**): *"As of August 7, 2026, there were 277,941,274 shares of common stock, par value
  $0.0001 per share, of the registrant issued and outstanding."* `Screens/cover_shares.py DJT` returns the same figure
  and accession. One class. Treasury stock (4,279,691 shares, bought back in 2024-25) is outside it.
- **Instruments outside the cover count, at $8.85, stated either way** (10-Q Notes 10-13):
  1. **Convertible senior secured notes, 28,324,940 shares if converted** (*"28.8 shares per $1,000 of Notes"*, a
     conversion price of about **$34.72**). **Far out of the money; excluded**, and carried as debt at Q4, where the
     holders' **cash put on 2026-11-30** is the governing fact.
  2. **Warrants 11,011,237** at $11.50, out of the money; excluded.
  3. **RSUs 3,893,553** unvested: the future SBC charge, which Q4 subtracts; not added.
  4. **6,000,000 shares to Yorkville Securities** as the M&A advisory fee, payable only if the TAE merger closes (10-Q
     Note 9); contingent; excluded, and recorded at Q3.
  5. **The TAE merger itself** (below): at closing, TAE's holders would own *"approximately 50% of the combined
     company"* on a fully diluted basis, so the count roughly doubles if it closes. **Not issued; excluded from the
     count, and it is the reason Q1 is decided as it is.**
- **The earnout is already in the count**: 40,000,000 earnout shares were issued in 2024 (FY2025 10-K statement of
  equity, *"Issuance of earnout shares 40,000,000"*), 36,000,000 of them to President Trump (10-K Item 1).

### THE DEAL CHECK: A LIVE MERGER, AND DJT IS THE LEGAL ACQUIRER
`sources.deal_note("0001849635")`: *"LIVE DEAL FORM: 15 filing(s) since the annual report of 2026-02-27, first 425 on
2026-03-27"*; the filing index holds **113 Form 425s**. Read on the documents:
1. **TAE Technologies (live).** 8-K of 2025-12-18, Item 1.01 (`0001140361-25-046056`): *"Merger Sub will merge with and
   into TAE (the "Merger"), with TAE surviving the Merger as a wholly owned subsidiary of TMTG"*; *"TMTG expects that
   its pre-Merger shareholders will own approximately 50% of the combined company and pre-Merger shareholders of TAE will
   own approximately 50% of the combined company, in each case on a fully diluted equity basis."* Conditions include
   TMTG shareholder approval of the share issuance and a charter amendment, HSR, and an effective Form S-4; outside date
   **2026-12-18**; termination fee **$90M** either way. The Donald J. Trump Revocable Trust (*"approximately 42% of the
   total outstanding TMTG Shares"*) signed a support agreement to vote for it. **Status:** the Q2 2026 10-Q (filed
   2026-08-10) still calls it *"the pending merger with TAE"*; **no S-4 has been filed** (EDGAR full-text search for
   "TAE Technologies" in S-4, S-4/A, DEFM14A and proxy forms from 2025-12-01 to 2026-09-18 returns zero; the filing
   index holds no S-4 after 2024), and the Interim CEO, in a transcript the company furnished on 2026-08-28 (8-K
   `0001437749-26-029174`, EX-99.1): *"TAE Technologies, is finishing their audits, and we're getting towards an S-4 to
   file to complete a merger of equals."* DJT lent TAE **$200M** on a convertible note (balance sheet; 10-Q MD&A).
   *DJT is the buyer of a business, not the target of one, so the quote is not a spread; but the price now buys a claim
   on a combined company half of which is a business no DJT filing describes (Q1).*
2. **Crypto.com / Yorkville Acquisition Corp. (terminated).** A business combination to form *"Trump Media Group CRO
   Strategy, Inc."* (8-K of 2025-08-26) was ended by *"a Mutual Termination and Release Agreement ... due to market
   conditions"* on **2026-08-07** (8-K Item 1.02, `0001437749-26-026597`).
3. **The spin-off of the legacy business (abandoned).** On 2026-02-27 the board authorised a study of placing
   *"businesses including Truth Social into a new publicly-traded company ("SpinCo")"* to merge with Texas Ventures
   Acquisition III Corp., described as *"a related-entity"* (FY2025 10-K Note 18); on 2026-06-10 *"the parties
   announced that they had decided to discontinue pursuing a spin-off. Following the close of the TAE merger, the board
   of directors of the combined company will evaluate potential strategic alternatives for the combined company's legacy
   business units"* (Q2 2026 10-Q MD&A).
4. No SC TO, SC 13E-3 or going-private filing. The Trust files Schedule 13D/A (latest `0001140361-25-046424`,
   2025-12-22).

### The perimeter between the business and the common holder: stated, not blended
At **2026-06-30** (Q2 2026 10-Q balance sheet; MD&A *"approximately $1,863.1 million of cash, cash equivalents,
restricted cash, short-term investments, equity securities, convertible note receivable, interest receivable, digital
assets, and digital assets pledged as well as approximately $970.3 million of debt"*), $M:

| item | 2026-06-30 | what it is |
|---|---:|---|
| cash and equivalents | 215.5 | of which $3.0M in the consolidated VIE |
| restricted cash | 30.7 | collateral for the notes |
| short-term investments | 209.2 | overnight repurchase agreements |
| equity securities | 480.5 | ETFs, *"invested in bitcoin related securities"* per Note 17; $233.0M pledged to the notes |
| digital assets | 597.7 | 9,477 bitcoin (cost $1,006.0M, fair value $557.1M) and 756M Cronos (cost $113.9M, value $40.6M) |
| digital assets pledged | 122.1 | 2,077 bitcoin pledged to an options counterparty that *"can rehypothecate at their sole discretion"* |
| convertible note receivable (TAE) | 200.0 | fair value $193.4M (Level 3) |
| **financial assets** | **1,863.1** | |
| debt, minimum payments | (989.0) | $983.5M of 0% convertible senior secured notes, **putable for cash on 2026-11-30**; a $5.4M term loan |
| **net financial assets** | **about 874** | **about $3.14 a share**, marked at June 30 |
| goodwill and intangibles | 138.0 | from the 2024 WorldConnect acquisition |

- **Subsequent event (10-Q Note 17):** in July 2026 the company sold $159.6M of bitcoin-related equity securities and
  bought bitcoin; *"As of July 31, 2026, we held approximately 14,139 bitcoins, including bitcoin pledged, with an
  aggregate fair market value of $890,524.5"*. The treasury is now mostly bitcoin itself.
- **Operating business cash:** Media $7.7M, Truth.Fi $3.3M; Corporate and other (the treasury) $924.8M of the
  cash-and-securities total (Note 16).
- **So the price of $2,460M (below) is about $874M of net financial assets marked at June 30 plus about $1,586M for
  everything else**: a social-media and streaming business with $3.7M of annual revenue, a fund-sponsorship business
  with $0.1M of half-year fees, and the pending TAE combination. Bitcoin has moved since June 30; the filed marks are
  used and none is re-struck.

### The market cap
- **$8.85 x 277,941,274 = US$2,460M ($2.46bn).** Split factor after 2026-08-07 = 1.0.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, fiscal year ended 2025-12-31, filed **2026-02-27**, accession **`0001140361-26-007174`**
  (`10K_FY2025.txt`); auditor **Semple, Marchal & Cooper, LLP** (PCAOB ID 178), which also audited internal control;
  **FY2025 Form 10-K/A** (Part III), filed 2026-04-30, `0001140361-26-018230`.
- **Q2 2026 Form 10-Q**, quarter ended 2026-06-30, filed **2026-08-10**, `0001437749-26-026777`; Q1 2026 10-Q
  `0001140361-26-020229`.
- Also read: FY2024 10-K (`0001140361-25-004822`, which carries FY2022-24 re-audited by Semple, Marchal & Cooper: *"for
  each of the three years in the period ended December 31, 2024"*); the DWAC FY2023 10-K (`0001140361-24-017011`, the
  shell); the DWAC comprehensive 10-K/A (`0001193125-23-265441`); the S-4 prospectus 424B4 (`0001193125-24-038590`) for
  Private TMTG's FY2021; the 8-Ks and exhibits named in this file.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash flows): *"Net cash
  provided by/(used in) operating activities | 14,758.1 | (60,982.7 ) | (9,733.5 )"*, *"Stock based compensation |
  59,191.1 | 107,387.1 | -"*, *"Purchases of property and equipment | (573.5 ) | (5,033.8 ) | (2.2 )"*, *"Depreciation
  and amortization | 7,421.3 | 2,933.9 | 60.4"* and *"Accounts payable and accrued liabilities | 26,800.6 | 5,535.9 |
  1,332.0"* match companyfacts to the hundred dollars for the operating company's years. **SBC is complete on the
  face**: the FY2025 statement of operations footnote allocates it $21,957.0 (R&D) + $37,234.1 (G&A) = $59,191.1K, the
  same figure as the cash-flow add-back and the equity statement; no capitalised SBC is disclosed.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### What the filings show, in my own words, without management's language
**Three things sit inside this company, and the price pays for a fourth that no filing describes.**

1. **A social network and a streaming service that sell advertising and subscriptions, at a scale of about $3.7M a
   year, against a cost several times that.** From the filed faces (FY2024 and FY2025 10-Ks, Q2 2026 10-Q; segment note),
   $M:

   | line | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
   |---|---:|---:|---:|---:|---:|
   | Revenue | 1.47 | 4.13 | 3.62 | 3.68 | 2.54 |
   | of which advertising | 1.47 | 4.13 | 3.62 | 3.43 | 2.05 |
   | of which subscriptions (Truth+ "Patriot Package") | | | | 0.26 | 0.37 |
   | of which Truth.Fi fund fees | | | | 0 | 0.12 |
   | Media segment EBITDA (company's measure, before SBC) | | (7.0) | (22.3) | (22.0) | (13.1) |
   | Truth.Fi segment EBITDA | | | | (2.8) | (1.5) |
   | Loss from operations (GAAP, incl. treasury marks from 2025) | | (16.0) | (186.0) | (573.0) | (457.0) |

   The advertising is sold through one outside platform: *"One advertising platform accounted for 49.9 % and 91.0 % of our
   total revenue for the six months ended June 30, 2026 and 2025, respectively"* (10-Q Note 2), under a minimum-guarantee
   publisher agreement with Rumble of 2023-10-30 whose *"prices for the Ad Units are set by an auction operated and
   managed by Rumble"* (FY2025 10-K). Part of H1 2026's increase is **barter**: *"provisioning of advertising services
   related to a barter agreement"*, with *"$1,035.0 of expense incurred related to a barter arrangement where we have
   received advertising services, but not provided full reciprocating advertising services"* (10-Q MD&A).
   **The two numbers a reader of an advertising business needs, users and revenue per user, are not reported and the
   company says they may never be**: *"TMTG does not currently, and may never, collect, monitor and/or report certain key
   operating metrics used by companies in similar industries"*, including *"average revenue per user, ad impressions and
   pricing, or active user accounts, including monthly and daily active users"* (FY2025 10-K, risk factors). Revenue
   has been flat at $3.6-4.1M for three years.
2. **A bitcoin treasury financed by a 2025 share placement and secured convertible notes.** $1,395M of new shares and
   $1,000M of 0% notes (May 2025) bought bitcoin, bitcoin-related ETFs and, by exchange of shares and $50M, Cronos; the
   company writes and buys options on its bitcoin, pledges bitcoin to a counterparty that may rehypothecate it, and has
   *"deployed a portion of our bitcoin holdings to third-party counterparties through lending, placement, and other
   yield-generation arrangements"* (10-Q, Item 1A). Its result is the price of bitcoin: a loss of $403.2M on digital
   assets plus $183.0M of investment losses in FY2025, and $360.6M plus $180.0M in H1 2026. This is **an asset, not a
   business** in the sense Q1 asks about; it earns what the market pays for bitcoin, and no filing can say what that will
   be.
3. **A fund-sponsorship business** (Truth.Fi) run through a consolidated VIE with a related party (Yorkville America),
   which earned $116.5K of management fees in H1 2026.
4. **What the price also pays for, and the filings do not show: a fusion-energy company.** The signed merger makes TAE
   Technologies a wholly owned subsidiary and gives its holders about half of the combined company. **No DJT filing
   contains TAE's financial statements** (the S-4 is not filed; the CEO says TAE *"is finishing their audits"*). What the
   DJT filings say about TAE's business is in the forward-looking-statement lists: *"risks related to TMTG's or TAE's
   ability to demonstrate and execute on commercial viability of its technology"*, *"delays in the development and
   manufacturing of fusion power plants and related technology"*, *"potential generation capacities of specific reactor
   designs"*, *"demand for nuclear energy"* (8-K of 2026-08-28). The CEO puts the combination at *"a $6 billion valuation
   merger"* (same transcript; a spoken figure, not a filed one).

### The scarce input this business controls
**For the media business, one person's posts, held under a licence the licensor can loosen.** The License, Likeness,
Exclusivity and Restrictive Covenant Agreement (royalty-free, *"$100 upon the execution"*) obliges President Trump to post
non-political content first on Truth Social for six hours, but *"President Trump may make any post that he deems, in his
sole discretion, to related to government, politics, or similar topics ("Political Related Posts") on any social media
site at any time"*, *"Most or all of Donald J. Trump's posts as President of the United States may be deemed by him to
be Political Related Posts"*, and he *"may terminate the Exclusivity Obligation upon thirty days prior written notice
provided at any time on or after February 2, 2025"* (FY2025 10-K Item 1). The company's own risk factor: *"the death or
incapacity of President Donald J. Trump, or discontinuation or limitation of his use of TMTG's products, would
negatively impact TMTG's business."* The newest product sells that input directly: Truth API, launched 2026-08-01, *"a
business-to-business data feed subscription that provides licensed, low latency access to publicly-available posts from
certain top Truth Social accounts"* (10-Q Note 17). Whether any of this is a position is Q2's question; Q1 records that
the input is a person, not an asset the company owns.

**For the treasury, none**: bitcoin is bought at the market price by anyone.

### Will the fundamentals look broadly the same in ten years?
**The company's own filings say no, in three separate ways inside nine months.**
1. **The declared forward entity is a combination with a fusion developer**, half-owned by TAE's holders, with the
   legacy business under review: *"Following the close of the TAE merger, the board of directors of the combined company
   will evaluate potential strategic alternatives for the combined company's legacy business units"* (Q2 2026 10-Q).
2. **The strategy has changed repeatedly inside the filed window** [E3-31: *"If a business is complex or subject to
   constant change, we're not smart enough to predict future cash flows"*]: a bitcoin treasury (May 2025); a Cronos
   treasury SPAC (August 2025, terminated August 2026); prediction markets on Truth Social (October 2025), which *"rather
   than develop a direct prediction market integration"* became *"a marketing agreement"* (August 2026); a digital token
   for shareholders (December 2025, *"currently assessing feasibility"*); a fusion merger (December 2025); a spin-off of
   the social network (February 2026, abandoned June 2026); a new CEO (April 2026); a data feed (August 2026). The 10-K
   describes the direction itself: TMTG may evolve *"into a holding company with numerous, largely autonomous
   subsidiaries in a variety of industries."*
3. **The social network's economics depend on the licence above**, whose exclusivity the licensor may end on thirty
   days' notice.

### The honest limit, and the verdict
**What I can state from the filings:** the media business sells about $3.7M a year of advertising and subscriptions
through an outside ad platform and loses about $22-25M a year before stock pay (the company's segment EBITDA, FY2024-25) and $84-130M after it; the treasury earns or
loses the price of bitcoin; the balance sheet holds about $874M of net financial assets against a $2.46bn price.

**What I cannot state from any filing:** what the common share will own and how it will make money. If the merger
closes (conditions open, S-4 unfiled, outside date 2026-12-18), half the company is a fusion-power developer whose own
risk language is *"ability to demonstrate and execute on commercial viability of its technology"*; understanding when a
fusion plant sells power at a profit is outside this analyst's circle and months of study would not put it inside
**[E4-46]**: *"if we can't make a decision in five minutes, we can't make it in five months."* If it does not close, the
company is a bitcoin holding with a small, loss-making media business attached, on a strategy that has added seven initiatives in fifteen months and dropped two of them. **Either way the fundamentals will not look broadly the same in ten years, and which of the two
companies the price buys is not yet decided.**

**THE ARGUMENT FOR OUT, AT FULL STRENGTH.** [E4-46] turns a competence gap into Q1 OUT so that UNRESEARCHED cannot be
abused: fusion power is outside the circle, and *"no fetch repairs it."* [E3-31] names constant change as the class the
corpus cannot predict, and this filer has changed direction repeatedly inside eighteen months. The media business on its
own is legible and small. **Why not OUT:** OUT is *"the evidence is here and the business fails."* The filings do not
yet say which business the share will be: the combination may close or fail by 2026-12-18, and after it the board says
it will decide what to do with the legacy units. That is the HHH shape recorded on 2026-09-02 (*"the forward entity is,
by its own declared program, not the filed entity"*) and the RGTI shape (the business the company declares it will be
*"has not yet happened"*). [E3-47] names the cost of closing a file wrongly as OUT; UNKNOWABLE closes it without a
finding about a business that does not yet exist in the filings. *Under either verdict the file closes here and nothing
below can reopen it.*

**THE SEPARATING TEST, ASKED ALOUD: can I name the document that would resolve what the share will own and how it will
make money?**
- **Not a document that exists and I have not fetched.** Every rung that could carry it was read: the FY2025 10-K and
  10-K/A, both 2026 10-Qs, the merger 8-K and its Item 1.01 summary, the termination 8-K, the 2026 earnings releases and
  the furnished interview. EDGAR full-text search finds no S-4, proxy or DEFM14A for the TAE merger.
- **The S-4, when filed, will carry TAE's audited statements and resolve part of it** (what TAE spends, what it owns,
  what the combined count will be). **It cannot resolve the rest**: no fusion plant has sold power, so no statement can
  show how TAE makes money; whether the merger closes is decided by votes and conditions after the filing; and what the
  combined board does with Truth Social is a decision not yet taken.
- **So: NO. UNKNOWABLE, closed without prejudice [E4-19].** The S-4 is named as the first record to read if the file is
  reopened (Q6), not as a work order that would settle Q1.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE → the company the common share buys is, by its own signed
  merger agreement, about to become half a fusion-power developer whose statements are not filed and whose product has
  not been sold, with the legacy media business under review after closing; if the merger fails, it is a bitcoin
  treasury attached to a $3.7M-revenue media business on a strategy that has added seven initiatives in fifteen months and dropped two of them. No
  document can say which company the price buys, or how that company makes money, until the combination is decided and
  a record of the combined business exists [E3-31, E4-46].**
- *The hard sequence closes the file here. **Q2, Q3 and Q4 below are RECORDED, NOT GOVERNING** (the HHH, RGTI and RIVN
  precedent), written on the filed business (Truth Social, Truth+, Truth.Fi and the treasury) because the brief asks for
  them and because they set the reopening conditions at Q6. Nothing recorded below can reopen Q1.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> **RECORDED, NOT GOVERNING.** The file closed at Q1 (UNKNOWABLE). This section tests the filed business (Truth
> Social, Truth+, Truth.Fi) because the brief asks for it and because it sets the Q6 reopening conditions. The treasury
> is not a business and is not tested for a moat; TAE is outside the circle and cannot be.

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
Truth Social owns something no rival can copy: it is the first place a sitting President's posts appear, under a
perpetual licence, so every trader, newsroom and political follower who needs those posts first must come to it; the
new data feed proves someone will pay for that access (*"more than ten customer agreements signed to date"*, Q2 2026
release); the brand is licensed royalty-free; and a platform that was deplatformed-proof by design has a loyal audience
the large networks cannot win back.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: SHOWN ONLY WEAKLY.** Revenue of $3.6-4.1M a year for three years (FY2023-25); no user,
  impression or revenue-per-user figure is reported (*"TMTG does not currently, and may never, collect, monitor and/or
  report"* them, FY2025 10-K). One advertising platform supplied 91.0% of H1 2025 revenue.
- **(3) Not subject to price regulation: YES** for advertising and subscriptions. (The Truth API faces congressional
  inquiry, in the Interim CEO's furnished interview of 2026-08-24: *"That service is being investigated by members of
  Congress"*, the interviewer's words; no filing states a regulatory action.)
- **(2) No close substitute: NOT SHOWN, AND CONTRADICTED IN THE COMPANY'S OWN 10-K AND LICENCE.**
  - *"The industries in which TMTG operates or plans to operate—social media, streaming video, and financial
    products—are all highly competitive"* (FY2025 10-K Item 1); *"other social media platforms, including those that
    previously engaged in widespread censorship, could embrace free speech and target the same audience as Truth Social.
    For example, as a private company under new ownership, X may demonstrate a sustained commitment to free speech
    principles that will heighten competition"* (risk factors).
  - **The one input a rival cannot copy is not owned and is not exclusive.** The licence lets the licensor post anything
    he deems political *"on any social media site at any time"*, lets him end the six-hour exclusivity on thirty days'
    notice, and *"The license is in any event revocable by President Donald J. Trump"* (10-K/A Item 13). The Interim CEO,
    in the furnished transcript: *"his information goes out all over the internet. It starts on Truth Social; it goes to
    Twitter, it goes to Reddit ... We give a 50-millisecond advantage in that post."* A fifty-millisecond head start on
    content that is republished everywhere is a substitute problem stated by the company itself.
  - **The customers treat it as having substitutes**: FY2024 revenue fell 12% (*"attributable to a change in a revenue
    share agreement with one of our advertising partners"*), and FY2025 advertising fell again while total revenue held
    only because a subscription product was added.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
Same metric, same window: revenue and GAAP operating margin, FY2025, from each filer's own 10-K as tagged in
companyfacts (`peers.py`, `peers_out.txt`; transcription with accession, **not** hand-checked against each face, which
is acceptable only because this section does not govern).

| company | FY2025 revenue | FY2025 operating margin | FY2023-25 | source (10-K accession) |
|---|---:|---:|---|---|
| **DJT (Trump Media)** | **$3.7M** | **-15,561% GAAP; -4,612% excluding the $403.2M digital-asset loss; -676% on the company's own segment EBITDA** | revenue $4.1M, $3.6M, $3.7M | `0001140361-26-007174` |
| Meta Platforms | $200,966M | +41.4% | 34.7%, 42.2%, 41.4% | `0001628280-26-003942` |
| Reddit | $2,202.5M | +20.1% | -17.4%, -43.1%, +20.1% | `0001713445-26-000022` |
| Pinterest | $4,221.8M | +7.6% | -4.1%, +4.9%, +7.6% | `0001506293-26-000021` |
| Snap | $5,931.4M | -9.0% | -30.4%, -14.7%, -9.0% | `0001564408-26-000013` |
| Rumble (DJT's own ad partner) | $100.6M | -125.9% | -167.4%, -137.0%, -125.9% | `0001213900-26-024099` |
| X Corp. | private | not available | | no SEC filing |

- Peers named: **six of the category's real competitors**, five with filings; X, the rival the 10-K itself names, is
  private and unavailable. By the framework's rule that makes the moat class **PROVISIONAL**; on a governing Q2 that
  would be a work order, but nothing in X's numbers could put DJT's own figures in a franchise's range.
- **What the row shows**: DJT is smaller than its own advertising reseller by a factor of 27 and loses more per dollar
  of revenue than any filer in the category. Scale and returns go the other way from a franchise [E3-43, E3-46].
- **The row's limit [E3-61]:** it shows position, not conduct.

### THE OTHER Q2 TESTS
- **Return on capital [E3-46]:** the operating business has no positive return in any filed year; Media segment EBITDA
  (before stock pay) was (7.0), (22.3), (22.0) and (13.1) $M in FY2023, FY2024, FY2025 and H1 2026.
- **The two-characteristic test [E2-44]:** no price rise is on file; ad prices *"are set by an auction operated and
  managed by Rumble"*; growth has needed new products (Truth+, Truth.Fi, Truth API), not price. **Fails.**
- **The attacker's test [E2-45]:** a well-funded rival would need only what DJT's own CEO says every large platform
  already runs (*"All of the big platforms run APIs into high-frequency trading platforms"*) plus the same public posts.
- **[E4-37]:** no price rise to agonise over; not applicable.
- **Rapid change [E4-04, E5-23]:** the product set has been rebuilt every year (streaming 2024, ETFs 2025, prediction
  markets announced and pivoted 2025-26, data feed 2026); the business buys its next product rather than defending one
  advantage.
- **Key-person dependence [E4-23], recorded here as the moat defect it is:** *"TMTG's success depends in part on the
  popularity of its brand and the reputation and popularity of President Donald J. Trump ... the death or incapacity of
  President Donald J. Trump, or discontinuation or limitation of his use of TMTG's products, would negatively impact
  TMTG's business"* (FY2025 10-K). *"The partnership's moat will go when the surgeon goes."*
- **Untapped pricing power [E3-33, E5-28]:** would require near-monopoly; the row shows the opposite. None.

### CLASS AND VERDICT
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL (by rule, for want of X's figures) · Direction: flat revenue,
  advertising declining, new products added.**
- **VERDICT (RECORDED, NOT GOVERNING): would be OUT** on [E3-03] criterion (2): the company's 10-K names the
  substitutes; the one scarce input is a person's posts under a licence he may revoke and whose political content he may
  post anywhere; no return on capital in any year and a row in which DJT is the smallest and least profitable filer
  [E3-46, E3-43]; [E2-44] fails; [E4-23] recorded.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q1. Written because the brief asked for Q3 with the earnings releases
> and the Part III amendment, and because its findings belong in the reopening conditions. Nothing here can promote the
> name or repair Q1 or Q2 **[E2-37, E2-38, E3-39]**. Political matters that no filing states are left out.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution [E3-38, E3-43]:** there is no franchise to stand a mistake (Q2), and the balance sheet is a
  leveraged position in a volatile asset managed with written and bought options, pledged collateral and lending
  arrangements (10-Q Item 1A: counterparties *"can liquidate such bitcoin without prior notice if margin requirements are
  not met"*). *"a business, unlike a franchise, can be killed by poor management."*
- [ ] **Control [E1-16]:** a minority purchase of a listed share (the Trust holds about 41%, Item 12 of the 10-K/A).
- [x] **Leverage [E3-29]:** $983.5M of secured notes against about $1.86bn of mostly volatile assets, with a
  loan-to-collateral covenant that counts bitcoin at 52.6% of market value (Note 10).

**Case declared: a BINARY GATE**, on daily execution and leverage. No price compensates.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
1. **2023-07-20: SEC settled order against the shell (DWAC), $18M penalty.** The FY2024 10-K lists as an exhibit the
   *"Order Instituting Cease-and Desist Proceedings pursuant to Section 8A of the Securities Act of 1933 and Section 21C of the Securities Exchange Act of 1934, Making Findings, and Imposing a Cease-and-Desist Order, dated July 20, 2023"*, and the company's own complaint describes Mr. Orlando's *"breach of fiduciary duty, which exposed Digital World
   to regulatory liability and resulted in an $18 million penalty"* (FY2025 10-K Note 16). The conduct was the shell's
   under its former chief executive, before the combination; the combined company sued him. [E5-22]: size is not the
   read; the read is who acted. Recorded against the shell's former management, not against TMTG's.
2. **2024-02 to 2026-07: litigation with the shell's former sponsor and chief executive (ARC, Mr. Orlando)**, which the company brought, with *"allegations against ARC and Mr. Orlando related to pre-targeting and other misconduct as set forth in the SEC Complaint against Mr. Orlando"*; *"all claims ... had been mutually resolved pursuant to a confidential settlement
   agreement"* (announced 2026-07-19, 10-Q Note 15). The company had paid or agreed to pay *"approximately $ 22 million to Mr. Orlando's attorneys"* under advancement obligations (10-K). No finding against TMTG's officers.
3. **2024-05-03: the auditor of FY2022-23 was dismissed** (*"Effective May 3, 2024, TMTG dismissed BF Borgers CPA PC"*,
   FY2024 10-K), with no reported disagreement; the successor, Semple, Marchal & Cooper, re-audited *"each of the three
   years in the period ended December 31, 2024."* The re-audit is the remedy the corpus would ask for; recorded.
4. **2026-07-07, open: a demand letter** from an investor in DWAC's sponsor *"alleging an entitlement to the issuance of
   TMTG stock"* (10-Q Note 15). No adjudication.
5. **No restatement of the operating company's statements, no SEC action against TMTG or its current officers, and
   effective internal control** at 2025-12-31 per the auditor, are on file.

**Read on the binary:** no adjudicated integrity finding against the company's current officers is on file. *A Q3 pass is
the absence of found disqualifiers, not a finding that the managers are honest* **[E5-17]**.

### THE INCENTIVE READ **[E4-27]**
- **What executive pay vests on (10-K/A, Summary Compensation Table):** time. The 2024 and 2025 RSU grants vest in
  instalments *"subject to continued service"*; no performance condition is disclosed. The former CEO's 2024
  compensation was **$46.9M**, of which $44.1M in RSUs and a $600K *"transaction bonus paid in 2024 to each executive in
  connection with the consummation of the business combination"*; he left on 2026-04-21 with salary continuation to
  2026-09-30 and 96,721 RSUs accelerated (8-K `0001140361-26-016743`).
- **The adviser is paid only if the merger closes:** *"a fee equal to 6,000,000 shares of our common stock in the event
  that (a) a transaction is consummated"* (10-Q Note 9), about $53M at $8.85, to Yorkville Securities. The same group was
  placement agent for the 2025 PIPE and notes (**$71.9M** fee), bought **$208.7M** of the PIPE, runs the consolidated
  fund VIE, and was counterparty to the terminated Crypto.com SPAC (Yorkville Acquisition Corp.); the abandoned SpinCo
  partner, Texas Ventures III, is *"a formerly related-entity"* whose officers include *"Certain affiliates of Yorkville
  America"* and former TMTG executives (FY2025 10-K Notes 10 and 18). [E4-27]: *"Never, ever, think about something else
  when you should be thinking about the power of incentives"*: the party advising on the deal is paid in shares only if
  it closes.
- **The Interim CEO holds other chief-executive posts**: *"Chief Executive Officer and a director of Blue Water
  Acquisition Corp. III ... Chief Executive Officer ... of SONO Group N.V. ... Chief Executive Officer ... of New America
  Acquisition I Corp."* (8-K of 2026-04-24). An [E3-40] focus prompt, and he says the TAE merger *"is one of the reasons
  why I got this role."*

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **weak accounting / unintelligible footnotes [E4-22]:** not in the arithmetic, which reconciles; but the company
  **refuses the operating metrics** of its own industry and says reporting them *"might not align with the best
  interests of TMTG or its stockholders"* (FY2025 10-K). That is a disclosure choice, read at candor below.
- [ ] **trumpeted projections [E4-22, E3-48]:** no numeric revenue or earnings guidance in the 2026 releases; the
  forward claims are qualitative (*"completing its prospective merger with TAE Technologies ... in the fourth quarter of
  2026"*). Not fired.
- [x] **serial share issuance [E5-15]:** 87.5M shares (restated FY2023) to 220.8M (FY2024) to 281.0M issued (FY2025):
  the combination, 40M earnout shares, $450M of SEPA sales, $1,395M PIPE, warrant exercises, Cronos consideration; and a
  merger that would roughly double the count. Most of the issuance was at prices well above today's ($24.98 in the PIPE),
  and the proceeds went into the treasury (below).
- [x] **EBITDA promotion [E4-29]:** the CODM measure is *"Segment EBITDA"*, and the Q2 2026 release reports *"a $223.5
  million Adjusted EBITDA* loss"* beside a headline of *"Over $1.9 Billion in Financial Assets"*, a non-GAAP gross figure
  that does not net the $970.3M of debt putable on 2026-11-30. *"Doing so implies that depreciation is not truly an
  expense ... That's nonsense."* (Depreciation is small here; the flag fires on the practice.)
- [ ] **filed-figure tells [E4-30]:** no taxes paid; not applicable.
- **Flags that converge [E4-52]:** issuance at high prices, proceeds into a volatile treasury, a gross "financial
  assets" headline, and a deal adviser paid only on closing point one way: the balance sheet and the next transaction
  are the product.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Return on equity: FY2023 equity negative; **-43.9%** (FY2024), **-43.3%** (FY2025), **-63.0%** for H1 2026 alone (net
loss over period-end equity). Excluding the treasury marks, the operating business still loses $135-190M a year after
stock pay (Q4). **Fails in its own terms in every filed year.**

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**Fails on two items.** (1) The number an owner of an advertising business would most want, users and revenue per user,
is withheld by policy. (2) The Q2 2026 release leads with gross *"financial assets"* of $1.9bn and an Adjusted EBITDA
figure, while the $983.5M noteholder put five months away appears in the 10-Q liquidity section (*"potentially refinance
our convertible notes if noteholders elect to exercise their right to cash repayment in November 2026"*), not in the
headline. The 10-Q itself is plain about the put, the collateral and the counterparty risks, which is to its credit.

### RATIONALITY IS CAPITAL ALLOCATION
- **The treasury [E2-30 (2), E5-24, E3-40]:** $2.4bn raised in May 2025 (PIPE and notes) went into bitcoin, bitcoin
  ETFs and Cronos; realized and unrealized losses on those holdings were **$1,126.8M** over FY2025 and H1 2026 ($403.2M +
  $183.0M + $360.6M + $180.0M); bitcoin cost $1,006.0M and was marked at $557.1M on 2026-06-30. *"corporate projects or
  acquisitions will materialize to soak up available funds."* The base business (Q1) received a small fraction of it.
- **Buybacks [E5-08, E4-31]:** 3,855,208 shares at an average **$11.76** in 2025 ($45.3M), when net financial assets
  were about **$5.36 a share** (2025-12-31 balance sheet) and the operating business lost money. Condition (2), a
  material discount to intrinsic value conservatively calculated, is not shown: the price paid was about 2.2 times the
  per-share net financial assets. **CAPITAL-ALLOCATION FLAG**, with the humility clause **[E4-13]**: management knows the
  business better than I do, and it binds position size, never the rate.
- **Stock deals [E5-44]:** the TAE merger gives about half the combined company for a business whose statements are not
  yet public; *"The intrinsic value of the shares you give in an acquisition must not be greater than the intrinsic value
  of the business you receive."* Not measurable from any filing (Q1).

### THE GUARDRAIL
- [x] Nothing in this Q3 is used to promote the name. [x] Key-person dependence is recorded at Q2 **[E4-23]**. [x] The
  manager is not the plan; the plan is a merger, which is the [E2-36] turnaround case, not the excisable-cancer one.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary as the filings stand** (no adjudicated disqualifier against
  current officers; the $18M SEC order was the shell's, under its former chief executive) [ ] OUT [ ] UNRESEARCHED [ ]
  UNKNOWABLE. **Flags converge [E4-52]:** [E5-15] issuance, [E4-29] Adjusted EBITDA and a gross "financial assets"
  headline, [E2-26] candor failures on user metrics and the put, a capital-allocation flag on the 2025 buyback [E5-08],
  [E2-30] and [E3-40] on the treasury and the CEO's other posts, and an [E4-27] incentive in the adviser's
  closing-contingent fee. *IN = no disqualifier found, never a promotion.*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q1. Written because the owner-earnings number and the near-term cash
> requirement are what any reopening would need.

### Owner earnings — the one number **[E2-23]**
**Which earnings owner earnings measures here, and why:** owner earnings are those of **the business** (*"the
average annual amount of capitalized expenditures ... that the business requires to fully maintain its long-term
competitive position and its unit volume"*); the corpus's worked practice separates **operating earnings** from gains on
holdings (look-through earnings are built from *"the operating earnings"* and investees' *"retained operating
earnings"*, **[E3-04]**), and a favourable break is stripped before the mean is trusted **[E4-41]**. So the governing
figure is the operating business's; the treasury's gains and losses, the interest on cash raised by selling shares, and
the option premiums are the price of an asset and are shown separately. Both are shown.

From the filed cash-flow faces (FY2024 and FY2025 10-Ks; the 424B4 for FY2021; Q2 2025 and Q2 2026 10-Qs), `oe_out.txt`
and `oe2_out.txt`, $M. SBC is complete on the face (Step 0) and subtracted in full **[E5-06]**.

| year | OCF (face) | SBC | capex | D&A | **OE, capex end** | **OE, D&A end** | payables line in OCF | put premiums in OCF | interest income (P&L) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| FY2021 (Private TMTG, from 2021-02-08) | (3.80) | 0 | 0.07 | 0.01 | **(3.87)** | **(3.80)** | 0.81 | | |
| FY2022 | (24.20) | 0 | 0.08 | 0.06 | **(24.29)** | **(24.26)** | (0.54) | | |
| FY2023 | (9.73) | 0 | 0.00 | 0.06 | **(9.74)** | **(9.79)** | 1.33 | | |
| FY2024 | (60.98) | 107.39 | 5.03 | 2.93 | **(173.40)** | **(171.30)** | 5.54 | | 14.72 |
| FY2025 | 14.76 | 59.19 | 0.57 | 7.42 | **(45.01)** | **(51.85)** | **26.80** | **43.98** | 46.56 |
| TTM Jun-26 | 8.52 | 43.51 | 0.03 | 7.54 | **(35.02)** | **(42.53)** | 46.09 | 43.98 | 36.13 |

- **Windows, all of them [E2-42, E4-25, E4-38]:** five-year FY2021-25 **$(51.3)M capex end to $(52.2)M D&A end**; four-year
  FY2022-25 $(63.1)M to $(64.3)M; three-year FY2023-25 $(76.1)M to $(77.7)M; TTM $(35.0)M to $(42.5)M. **No window longer
  than five years exists**: the operating company was incorporated on 2021-02-08 and Truth Social launched in the first
  quarter of 2022, so FY2021 is a part-year of pre-launch spending. **In words: every window and both ends are negative;
  the business has consumed between about $4M and $173M a year of owners' money, about $51-78M a year on average.**
- **The FY2025 positive operating cash, shown both ways (the `working_capital_flag`).** The $14.76M contains **$26.80M**
  from *"Accounts payable and accrued liabilities"* (182% of the figure) and **$43.98M** of *"Premiums received from
  assigned put options"* written on bitcoin, plus interest on the cash pile ($46.56M of interest income in the P&L).
  **Without the payables line: $(12.0)M. Without the payables, the option premiums and the interest: $(102.6)M.** The
  payables build continued in H1 2026 (+$26.07M), largely *"Other accrued expenses"* ($6.9M to $19.5M), in the half-year when legal fees were $49.7M and the release says legacy legal matters are *"substantially resolved"*; an accrual built by unpaid bills reverses when they are paid.
- **The operating business alone** (OCF less the treasury's put premiums and interest income; a CONVENTION, since the
  P&L interest line includes small accruals): FY2024 **$(75.7)M** of operating cash, **$(188.1)M** of owner earnings at
  the capex end; FY2025 **$(75.8)M** and **$(135.6)M**. **This is the governing owner-earnings figure: about $(136)M to
  $(188)M a year for the last two years.** Part of it is legal cost the company calls legacy (*"$49,678.7"* of legal fees
  in H1 2026, *"related to recently concluded legal matters"*); [E2-57] and [E5-33] keep it in the mean: *"you must count
  the runs scored against you in all nine innings."*
- **Maintenance capex, a DISCLOSED JUDGMENT [E2-23, E3-44, E2-41]:** plant is negligible (property and equipment
  $2.1M; capex $0.6M in FY2025); D&A is mostly amortisation of the WorldConnect intangibles (*"Source code and technology
  $24,500.0"*, *"Exclusivity rights 3,100.0"*) bought in 2024. **(c) for this business is not plant**: its real
  maintenance spending is people and servers, which sit in operating cash, and stock pay. The two ends differ by less
  than $7M a year, so the band does not change any conclusion. Not the [E5-20] class.
- **Stock compensation [E5-06, E3-70]:** subtracted at the charge ($107.4M, $59.2M). Grant-date values: RSUs granted
  2025 at $23.29 (3,023,481) and H1 2026 at $9.11 (3,431,830); the [E3-70] market measure for time-vested RSUs is about
  the grant value, and the charge is used.
- **Look-through [E3-04 convention]:** no equity-method investees; the TAE note earns interest (Level 3); nothing to add.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great [ ] good [x] **worse than the definition's words, not better**: *"earns little or no money"* without the
  growth. Revenue is flat at $3.6-4.1M; the business consumes $135-190M a year of owners' money after stock pay, and the
  savings account is refilled by share sales (SEPA 2024, PIPE 2025). *"unless the cash they consume gets to earn a
  reasonable return"* **[E4-43]**: it has not in any filed year.

### Staying power — score all three **[E5-11]**
- (1) **Earnings: none** from the business in any year.
- (2) **Liquid assets: about $1.66bn** at 2026-06-30 (cash $215.5M, repo $209.2M, ETFs $480.5M, bitcoin $597.7M plus
  $122.1M pledged, restricted cash $30.7M), **most of it bitcoin or bitcoin-linked**, with $514.2M pledged to the notes ($30.7M cash, $233.0M ETFs, $250.5M bitcoin) and
  $122.1M to an options counterparty that may rehypothecate it.
- (3) **Near-term cash requirement: $983.5M on 2026-11-30**, the holders' put at 100% of principal. The conversion price
  is about $34.72 against $8.85, so a rational holder puts. That is **40% of the market cap and 53% of the financial
  assets, due in 73 days.** The company's own words: it may *"potentially refinance our convertible notes if noteholders
  elect to exercise their right to cash repayment in November 2026."* **This is the strength that fails.**
- **Leverage [E4-16, E2-54, E3-52, E5-39]:** 0% notes accrete $23.0M a half-year of non-cash interest; **[E2-54]'s
  coverage test fails** because there is no operating cash flow to cover anything; the notes carry covenants and a hard
  date, the opposite of [E3-52]'s covenant-free liabilities; the answer to the put is either selling the treasury at
  the day's bitcoin price or *"the kindness of strangers"* **[E5-39]**.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism: shape #6, THE BORROWED BALANCE SHEET, with #8's feature (THE EQUITY IS THE REVENUE)**
  (`Screens/SURVIVAL SHAPES - index.md`). The treasury was bought with borrowed money that falls due on a fixed date
  against a volatile asset, and the operating losses have been paid by selling shares every year. The owner is hurt by
  three things at once: a forced sale of bitcoin at whatever price holds on 2026-11-30, a continuing operating burn, and
  an all-stock merger that halves the claim.
- **Quantified from filed figures:** at the June 30 marks, paying the put from the $1.66bn of liquid assets leaves about
  **$670M**; on bitcoin alone (14,139 coins at $890.5M on 2026-07-31, Note 17), a fall of half before the put date takes
  about **$445M** off that, leaving about **$225M** against an operating burn of about $75-100M a year before stock pay. A
  refinancing instead would add new debt or new shares against the same asset.
- **Likelihood: [x] a real possibility** that the put forces a sale of much of the treasury at an adverse price or a
  dilutive refinancing (it is dated, sized and filed); **likely** that the operating business needs further owners'
  money (every filed year); **a low-level possibility** of insolvency before the put date, since liquid assets exceed it
  at the filed marks. This is exposure, not experience **[E4-40]**: the treasury has fallen by about $1.1bn in eighteen
  months, and nothing in the filings bounds its next move.
- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN [x] OUT** on owner earnings negative at every window and both ends
  [E2-23, E4-43] and on [E5-11]'s first and third strengths (no earnings; a $983.5M requirement in 73 days against
  assets that are mostly bitcoin) [ ] UNRESEARCHED [ ] UNKNOWABLE.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q1 is UNKNOWABLE (and Q2 and Q4, recorded, are OUT). Nothing below is
a clearance.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
Cap **$2,460M** ($8.85 x 277,941,274); sovereign **5.34%** (US Treasury 30 Yr, 09/18/2026).

| owner earnings case | $M | yield on the cap | vs 5.34% |
|---|---:|---:|---:|
| operating business, FY2025, capex end (governing construction) | (135.6) | (5.5)% | -10.8 |
| 5y FY2021-25, capex end, all cash flows | (51.3) | (2.1)% | -7.4 |
| 3y FY2023-25, D&A end, all cash flows | (77.7) | (3.2)% | -8.5 |
| TTM to 2026-06-30, capex end, all cash flows (the most generous) | (35.0) | (1.4)% | -6.8 |

- **The floor first [E4-28]:** a 10% pre-tax expectancy at this cap needs about **$246M a year of positive owner
  earnings** from a business that has never produced one. No growth rate converts a negative base into a yield; the
  growth-required figure is refused.
- **What the price already assumes:** net financial assets were about **$874M ($3.14 a share)** at the June 30 marks;
  the price pays about **$1.59bn more** for a media business with negative owner earnings and for half of a combined
  company with TAE, which Q1 placed outside the circle. **[E4-35] and [E4-44]** bind: no filed period supports any
  positive figure for the business.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
On owner earnings from any filed window, **no positive value can be computed for the business**. The balance sheet
supplies **roughly $3 a share** of net financial assets at the June 30 marks, moving with bitcoin, and shrinking by the
operating burn. **Bar 2, the screamer test [E4-01]**: the price ($8.85) is above the whole range; the answer would be
*no*. **Windage count: none spent.**

- **VERDICT: none. Q5 did not open (Q1 UNKNOWABLE).** Had every gate been IN, the computation shows a negative yield
  against a 5.34% bond and a 10% floor, and a price about 2.8 times the net financial assets.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed (a Q1 close is a finding about the evidence, and a
> price alert on it would be a category error, the QLYS ruling). These are the conditions on which the file would be
> reopened, written before any reopening **[E1-02]**.

**What would reopen Q1 (the governing gate):**
1. **The combination decided.** Either the TAE merger closes, and the combined company then files **at least two to
   three years of audited statements** in which TAE's revenue, cost and capital employed can be read as a business
   (the first record to read is the **S-4, when filed**, for TAE's audited history and the final share count); or the
   merger terminates, and the company states in a filing what business it will be.
2. **A stable strategy on the record**: two consecutive annual reports without a new line of business announced or an
   old one dropped [E3-31].
3. **The operating metrics reported**: users, engagement and revenue per user, so that the media business's unit
   economics can be written at all.

**What would reopen Q2, if Q1 cleared:** the media business earning a positive return on capital for three years on its
own revenue, with the licence's exclusivity intact and no filed dependence on one person's use [E3-03, E3-46, E4-23].

**What would close it harder:** the put met by selling most of the treasury near a low; a dilutive refinancing; the
licence's exclusivity ended by notice; the adviser's closing fee paid on a merger priced at quote rather than value
[E5-44].

**The sell rule [E2-28]** does not apply (nothing held). **Position size:** none.
**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q1 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q1 (UNKNOWABLE); Q2-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The only IN is Q3's binary, recorded and
  not governing, written as the absence of found disqualifiers. The Q2 moat class is PROVISIONAL by rule (X is private)
  and Q2 does not govern.
- [x] The UNKNOWABLE verdict states what specifically cannot be known (which company the share buys, and how it makes
  money) and why no document now existing resolves it; the S-4 is named as the first record to read on reopening.
- [x] Step 0: the de-SPAC entity question settled on the filings (reverse recapitalization, accounting acquirer), the
  colliding keys tabulated with accessions, the skip reason reproduced and explained, the filing read with accession
  numbers, and OCF, SBC, capex, D&A and the payables line cross-checked to the FY2025 10-K face.
- [x] Owner earnings on the five-year default window and on four-year, three-year and TTM windows, both (c) ends; no
  window longer than five years exists and that is said; the operating business separated from the treasury with the
  ledger ids that govern the choice [E2-23, E3-04, E4-41]; the payables line shown both ways.
- [x] Competitor row filled from five peers' filings with accessions (companyfacts transcription, labelled); X named and
  unavailable.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the
  cached 09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a range (no positive value for the business; about $3 a share of net financial assets) under a
  COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count none spent.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by two Form 4s.
- [x] Share count from the Q2 2026 10-Q cover with its accession; notes, warrants, RSUs, the adviser's contingent
  shares and the merger issuance considered and stated either way.
- [x] Deal check run on EDGAR: a live merger (TAE; DJT the legal acquirer; no S-4 filed), a terminated SPAC combination
  (Crypto.com), an abandoned spin-off; no tender or going-private filing.
- [x] Run committed after Step 0 and Q1, and after Q2-Q6 with the audit, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written; the absence of any
  bitcoin or gold row was checked by a sweep of the ledger for "bitcoin|crypto|gold" (no instance found), so this file
  cites no corpus passage about bitcoin and treats the treasury by the owner-earnings rules alone.
- [x] No em dashes in anything this session wrote (the template's headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded filings, the 2.4 MB 424B4 dump and the 0.9 MB `companyfacts.json` were
  left out of every commit.
- [x] Political prominence: the file quotes filings and the company's own furnished transcript; the interviewer's
  statements are marked as the interviewer's; no commentary without a filing behind it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q1, corrected before commit:** a draft said the media business loses *"$80M+"* a year after stock pay; the filed
   figures are about $84M (FY2025) and $130M (FY2024) on segment EBITDA less SBC, and the text says $84-130M.
2. **Q1, corrected before commit:** a draft said the strategy had *"changed seven times in fifteen months"*; the list
   supports seven initiatives announced and two dropped, and the text says that.
3. **Step 0, corrected before commit:** a draft attributed the whole `share_count_shift` of 1.281 to the PIPE and the
   Cronos exchange; vesting and buybacks also moved the count, and the text says "chiefly".

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The operating-cash series in section 2 is the shell's for three years.** FY2021 -1.11, FY2022 -1.38 and FY2023
   -5.14 are DWAC's; the operating company's are (3.80), (24.20) and (9.73). The brief warned that this might be so and
   asked for it to be established, which is right; but its own FY2023 figure (-5.14) is the one the screen used, and the
   screen's three-year owner earnings therefore mixed entities.
2. **"No 5y window returned"** is a screen fact, not a filing fact: the 424B4 of 2024-02-16 carries Private TMTG's
   FY2021 statement, so a five-year FY2021-25 window can be built by hand (FY2021 being a part-year before launch).
3. **The unverified beliefs, settled:** combination with DWAC closed in late March 2024: **held** (2024-03-25; TMTG the
   accounting acquirer, reverse recapitalization). Products Truth Social, Truth+, Truth.Fi with ETFs and SMAs: **held**
   (plus Truth API from 2026-08-01, and Truth Predict pivoted to a marketing agreement). About $2bn-plus raised in 2025
   for bitcoin: **held** ($1,395.3M PIPE plus $1,000M of 0% convertible senior secured notes, May 2025; 684.4M Cronos
   for 2.8M shares and $50M). A crypto-token arrangement: **held and more**: the Cronos purchase, a Crypto.com SPAC
   combination terminated on 2026-08-07, and a shareholder token initiative still being assessed. **TAE merger, all
   stock, announced December 2025: held** (2025-12-18; DJT the legal acquirer, about 50/50, $90M fees, outside date
   2026-12-18), **but no S-4 has been filed**, which the brief's list of documents to settle it assumed exists. Donald
   J. Trump's stake in a revocable trust, and earnout shares: **held** (114,750,000 shares in the Trust, of which
   36,000,000 earnout shares; Donald J. Trump, Jr. sole trustee with sole voting power, 10-K/A). DWAC's 2023 SEC
   settlement: **held** (order of 2023-07-20, $18M penalty); the related insider-trading cases were not settled on a
   filing by this run and are not relied on. Revenue almost entirely advertising and small: **held through FY2024;
   FY2025 added subscriptions ($0.26M) and H1 2026 added fund fees and barter.**
4. **The brief did not know about the noteholders' put on 2026-11-30**, which is the most consequential dated fact in
   the file (Q4).

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`ocf()` and the owner-earnings construction read the earliest vintage per year, which for a reverse
  recapitalization is the shell.** Companyfacts carries the shell's and the operating company's FY2022-23 values under
  the same element; the earliest filed is the shell's. The RGTI run found the same collision. A screen could flag any
  year where two accessions of the same element differ by more than a factor of two.
- **`tools/sources.sovereign()` served the cached 09/17 row** at 19:44 EDT while the Treasury had published 09/18 (5.34%):
  the SNOW, TSLA and RIVN note, reproduced a fourth time.
- **`deal_note()` correctly flagged the live merger** from the 425 filings; it cannot tell a buyer from a target, so the
  "quote is a spread" warning had to be read against the 8-K.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A de-SPAC's tagged history can belong to two companies, and a de-SPAC can buy a third.** Read the basis-of-presentation
note before any tagged year is used, and read the deal filings before the price is used: here the shell's cash sat under
the operating company's keys, and the share now points at a fusion developer whose statements no filing yet contains.

---
## REGISTER
- Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [x] **UNKNOWABLE (about my
  evidence)**, at Q1.
- **One line:** DJT CLOSES AT Q1 (UNKNOWABLE, [E3-31, E4-46]): the company the share buys is, by its own signed merger
  agreement of 2025-12-18, to become half a fusion-power developer (TAE Technologies) whose statements no filing
  contains (no S-4 filed; outside date 2026-12-18), with the legacy media business under review after closing; if the
  merger fails, it is a bitcoin treasury attached to a $3.7M-revenue social network, on a strategy that added seven
  initiatives in fifteen months and dropped two. Q2 recorded as OUT (the 10-K names the substitutes; the scarce input
  is one person's posts under a licence *"revocable by President Donald J. Trump"*; the smallest and least profitable
  filer in a six-name row; [E4-23]); Q3 recorded IN on the binary with converging flags ([E5-15], [E4-29], [E2-26], a
  2025 buyback at about 2.2x net financial assets per share, a closing-contingent adviser fee); Q4 recorded OUT (owner
  earnings negative at every window and end, five-year $(51.3)M to $(52.2)M on all cash flows and about $(136)M to
  $(188)M a year for the operating business alone; a $983.5M noteholder put on 2026-11-30 against mostly-bitcoin
  assets; shape #6 with #8's feature); price $8.85 x 277,941,274 = $2.46bn against about $874M of net financial assets
  at June 30 marks, headed COMPUTATION — NOT A CLEARANCE: yield negative against 5.34%; Q6 arms nothing.
- **If UNKNOWABLE:** what cannot be known is **which company the common share will own after the TAE combination is
  decided, and how that company makes money**: TAE's business has no filed period and its product has not been sold;
  the merger's closing and the fate of the legacy business are decisions not yet taken. The first record to read on
  reopening is the S-4, when filed; it cannot by itself settle the question.
