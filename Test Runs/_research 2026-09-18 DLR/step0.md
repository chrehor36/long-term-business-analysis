# Company Run — Digital Realty Trust, Inc. (DLR) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch
(no prior run file for DLR exists). WAVE 5, the last of the eight "capex unresolved [E5-20]" names.
Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-18 DLR/`; DLR filings
fetched earlier today for the EQIX competitor row are cited in place at
`Test Runs/_research 2026-09-18 EQIX/peers/` (not re-fetched).

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Asked aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE ROUTING NOTE, THE RATE, THE PRICE, THE PERIMETER, AND THE FILING

### The REIT routing note, checked on disk rather than followed
The wave 5 table says *"EQIX and DLR are REITs: the prepped reading list routes REITs to a sector
method first; a run states that and the verdict follows."* **`Framework/` was listed by this run on
2026-09-18** and holds: the two audit/synopsis files of 2026-08-26, the two archives, `CHANGELOG.md`,
`INVENTIONS - deleted and why.md`, `PLAIN ENGLISH - what this is and how it works.md`, `README.md`,
**one** sector method (`SECTOR METHOD - owner earnings for insurers and float-bearing holding
companies.md`), `THE FRAMEWORK v4.md`, `THE HOLDINGS FRAMEWORK.md` and the `v4/` folder. **There is no
REIT sector method.** The EQIX run found the same this morning and nothing has been added since. v4
says *"If a rule is not here, it is not in force"*, so **v4 is applied as written** and no REIT method
is invented (PRIME RULE 3). Digital Realty's own measures (FFO, Core FFO, AFFO, Adjusted EBITDA,
"recurring capital expenditures") are READ below as the company's claims, never adopted as the
run's definitions. The insurer method is not owed: Digital Realty is funded by notes, bank lines,
share issuance, joint-venture partners and asset sales, not by float.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority.**
  Struck by this run: the cached curve was deleted and `tools/sources.sovereign("USD")` re-fetched
  it at about 18:10 UTC on 2026-09-18, returning `(5.29, '09/17/2026', 'US Treasury daily par yield
  curve')` (`step0_out.txt`). 09/17 is the newest row published (the 09/18 curve appears after the
  close). FRED was not used.
- **The earnings currency is not only USD, recorded rather than smoothed.** Annualized rent by metro
  at 2025-12-31 (10-K MD&A, portfolio including unconsolidated entities at 100%): Northern Virginia
  21.4%, Chicago 7.1%, **Frankfurt 6.1%, London 4.5%, Singapore 4.5%**, Dallas 4.3%, **Paris 4.1%,
  Amsterdam 4.1%**, New York 4.0%, **Sao Paulo 3.8%, Johannesburg 3.5%**, Silicon Valley 3.5%,
  Portland 3.0%, **Tokyo 2.3%, Zurich 1.7%**, other 22.1%. The 10-K names the exposures: *"Our primary
  currency exposures are to the Euro, Japanese yen, British pound sterling, Singapore dollar, South
  African rand and Brazilian real."* Europe held 107 of 221 consolidated buildings at 2025-12-31.
  Precedent in this queue (CL, SPGI, EQIX) prices a USD reporter against the USD sovereign and names
  the currency at Q4; this run does the same. **The USD 30-year is the highest of the three
  sovereigns on file (EUR 3.83%, JPY 4.00%, last struck 2026-09-10/13), so it is the harder bar.**

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$184.26, the close of 2026-09-17**, the last COMPLETED close. Source: Yahoo Finance daily chart
  series via `sources._chart("DLR", rng="1mo")` (aggregator, permitted for live quotes only,
  **flagged**; `price_out.txt`). Bar: open 183.22, high 185.02, low 182.76, close 184.26.
- **`tools/sources.price()` was NOT used for the struck price.** At about 18:10 UTC on 2026-09-18,
  market open, it returned `(183.84, '2026-09-18', 'USD')`; the chart meta shows
  `regularMarketPrice 183.855` at `regularMarketTime 2026-09-18 18:10:47` UTC. An intraday price
  stamped with today's date while the docstring says "Latest close". **The TOST and EQIX defect
  reproduces on a third name.**
- Recent closes: 09-10 $185.37 · 09-11 $188.58 · 09-14 $179.14 · 09-15 $179.27 · 09-16 $181.07 ·
  09-17 $184.26. Last dividend in the series **$1.22** (ex-date 2026-09-15).
- **Primary-filing cross-checks of the aggregator (two, both corroborate):**
  1. Form 4, accession **`0001500081-26-000009`**, filed 2026-08-31: director Mark R. Patterson sold
     200 shares on **2026-08-27 at $193.96**. The Yahoo bar for 08-27 is low $191.48, high $196.83.
     **Inside the range.**
  2. 8-K of 2026-07-01, accession **`0001193125-26-292577`**: *"On July 1, 2026, Blackstone completed
     an underwritten public offering of 12,310,249 shares of common stock ... at a price per share to
     the public of $185.00."* A negotiated block price, not a trade print, but in the same range as the
     September closes.

### The share count: from the cover, with the accession
- **370,036,176 shares**, from the cover of the Q2 2026 Form 10-Q (period ended 2026-06-30, filed
  **2026-07-31**, accession **`0001104659-26-089296`**): *"Digital Realty Trust, Inc.: Class
  Outstanding at July 29, 2026 Common Stock, $.01 par value per share 370,036,176"*.
  `Screens/cover_shares.py DLR` returns the same figure from the same accession, *"(single class /
  undimensioned)"*.
- **ERIC trap checked**: the 2026-06-30 balance sheet reads *"370,010 and 343,557 issued and
  outstanding as of June 30, 2026 and December 31, 2025"* (thousands). Issued equals outstanding; there
  is no treasury stock. **SPGI trap checked**: no exclusion clause on the cover.
- **The non-voting class is inside the count.** 12,310,249 shares of non-voting common stock were
  issued to Blackstone on 2026-06-30 and converted to common on transfer on 2026-07-01 (8-K
  `0001193125-26-292577`), four weeks before the cover date.
- **The count grew 7.7% in seven months.** 343,557 thousand (2025-12-31) to 370,010 thousand
  (2026-06-30): about **13.5 million ATM shares** at an average $184.94 (net $2.5bn), **12.3 million**
  to Blackstone, the rest awards and unit exchanges (10-Q Note 10). A new **$7.5bn** ATM programme was
  opened on 2026-05-04 (8-K `0001193125-26-202581`), **$6.3bn** unused at 2026-06-30.

### The perimeter between the business and the common holder: stated, not blended
The owner-earnings figures below are built from the consolidated cash-flow statement, which is the
Operating Partnership's. Four claims sit between that cash and the common holder:
1. **Operating-Partnership common units held by third parties**: *"Limited Partners, 6,665 and 6,189
   units issued and outstanding as of June 30, 2026 and December 31, 2025"* (thousands; 1.8% of the
   OP), redeemable for cash or, at the Parent's option, one share each. **Treatment: they share the
   OP's cash one-for-one with a share, so the owner-earnings denominator is common shares PLUS these
   units (376.70 million).** The struck cap uses the cover count; the perimeter-consistent cap adds
   the units at the same price. Both are shown at Q5.
2. **Preferred stock**: series J, K and L, *"$ 755,000 liquidation preference ( $ 25.00 per share),
   30,200 shares issued and outstanding"* (thousands), dividends **$40.7M a year** (FY2023-25 income
   statements). A senior claim: deducted from owner earnings, never added to the cap.
3. **Teraco minority (redeemable noncontrolling interest, $1,567M at 2026-06-30)** and
   **noncontrolling interests in consolidated joint ventures** ($421M at 2025-12-31; *"Depreciation
   related to non-controlling interests | (86,159)"* in FY2025). Their share of consolidated cash is
   not the common holder's; handled at Q4.
4. **Share overhang not in the cover count, shown separately [E2-26]**: **2,337,036 shares** issued to
   buy Columbia Capital (8-K `0001193125-26-357083` of 2026-08-19 registers their resale, *"shares of
   common stock that were issued as consideration"*), plus up to **1,457,506** more on earn-out
   milestones; **3,425,031 shares** due in H2 2026 to settle the Teraco put (10-Q Note 10); **517,475
   OP units** issued for the Astra Enterprise Park land (April 2026, inside the 6,665k above); any ATM
   sales after 2026-06-30 (unknown until the Q3 10-Q). Together about **7.2 million shares (+1.9%)**
   known and pending.

### The market cap
- $184.26 × 370,036,176 = **US$68,182.9M**. Split factor after 2026-07-29 = **1.0**
  (`sources.split_factor_after`); `close` used, never `adjclose`.
- Perimeter-consistent (common plus third-party OP units): $184.26 × 376,701,176 = **US$69,410.9M**.
- With the known pending shares (Columbia 2.34M, Teraco 3.43M): about **US$70.5bn** before the
  earn-out and any post-June ATM sales. Displayed, not blended.

### LIVE-DEAL CHECK: re-queried by this run, not inherited
- `sources.deal_filings("0001297996")` returned `([], [], '2026-02-13')`: no merger, tender or
  exchange form and no flagged 8-K.
- **Every 8-K since 2024-01-01 with Items 1.01, 2.01, 3.02, 3.03, 7.01 or 8.01 was listed and the
  2025-2026 ones were read** (`fetch8k.py`): note issues and credit agreements (2024-09-13, 2024-09-30,
  2024-11-12, 2025-01-14, 2025-06-25, 2025-11-21), ATM agreements (2024-12-23, 2026-02-17,
  2026-05-04), and the **2026 perimeter events**: the Astra land purchase and Columbia Capital and
  Teraco-put agreements (8-K `0001193125-26-276844`, 2026-06-22), the **Blackstone joint-venture
  buy-in** (8-K `0001193125-26-288761`, 2026-06-29, completed 2026-06-30 per `0001193125-26-292577`),
  and the Columbia Capital resale registration (2026-08-19). **All of these are Digital Realty buying;
  none is an offer for Digital Realty's shares. The quote is an owner-earnings price, not a spread.**
  They are perimeter changes and are carried into Q4.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, period ended 2025-12-31, filed **2026-02-13**, accession
  **`0001104659-26-015365`** (`dlr-20251231x10k.htm`; text at `../_research 2026-09-18 EQIX/peers/DLR_10K_FY2025.txt`).
- **Q2 2026 Form 10-Q**, filed **2026-07-31**, accession **`0001104659-26-089296`**; Q1 2026 10-Q
  (`0001104659-26-054255`).
- Also read: 10-Ks FY2014-FY2024 (FY2014 `0001297996-15-000010`, FY2015 `0001297996-16-000124`, FY2016
  `0001297996-17-000020`, FY2017 `0001297996-18-000026`, FY2018 `0001297996-19-000032`, FY2019
  `0001558370-20-001906`, FY2020 `0001558370-21-002191`, FY2021 `0001558370-22-002195`, FY2022
  `0001558370-23-002087`, FY2023 `0001558370-24-001575`, FY2024 `0001558370-25-001424`); 8-K EX-99.1
  releases and EX-99.2 supplements for Q4 2021-Q4 2025 and Q2 2026 (on disk in the EQIX peers
  folder); the **DEF 14A of 2026-04-17** (`0001308179-26-000296`); the Interxion closing 8-K of
  2020-03-13 (`0001193125-20-072868`) and the DuPont Fabros closing 8-K of 2017-09-14
  (`0001193125-17-285083`); the 8-Ks listed above.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash flows):
  *"Net cash provided by operating activities | 2,412,136"*, *"Depreciation and amortization |
  1,894,636"* and *"Improvements to investments in real estate | ( 3,181,179 )"* all match companyfacts
  exactly (`NetCashProvidedByUsedInOperatingActivities`, `DepreciationAndAmortization`,
  `PaymentsToDevelopRealEstateAssets`, accession `0001104659-26-015365`). **The fourth line is the
  finding of Q4**: *"Amortization of share-based compensation | 93,766 | 75,606 | 80,532"* is on the
  face and **in no element companyfacts carries** (searched by value across every namespace in the
  file), and the capex line sits under `PaymentsToDevelopRealEstateAssets`, **which no `CAPX_TAGS`
  element reaches.**
