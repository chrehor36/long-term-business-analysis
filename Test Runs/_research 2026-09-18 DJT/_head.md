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

