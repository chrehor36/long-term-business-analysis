# -*- coding: utf-8 -*-
"""FOLD STEP 3: the narrative fold. Appended, never inserted into history."""
import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(BASE, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = io.open(P, encoding="utf-8").read()

ADD = u'''

---

## UPDATE 2026-09-21 - MGM: Q2 OUT. The company sold the moat and rented it back, and the filing says so in a table nobody quotes.

**Run file:** `Test Runs/2026-09-21 Run - MGM MGM Resorts International.md`. **Register entry 157.**
Wave 7, name 25 of 218. Price **$38.59** (2026-09-21, aggregator, flagged, intraday) x
**251,592,756 shares**, one class, from the **10-Q cover for the quarter ended 2026-06-30, filed
2026-07-29, accession `0000789570-26-000076`** = cap **$9,709M**. Sovereign **5.34% USD**, US
Treasury daily par yield curve, 30 Yr, **09/18/2026**, from the issuing authority; FRED was not
used. Primary filing: **10-K FY2025, accession `0000789570-26-000018`.**

### THE FINDING

**The Rule 13-01 guarantor summarized financial information is the number that decides this file,
and it is filed every year in the MD&A where nothing links to it.** MGM Resorts International
combined with its wholly owned **domestic** guarantor subsidiaries - a group that contains all
nine Las Vegas Strip resorts and excludes MGM China, LeoVegas, BetMGM, MGM Grand Detroit, MGM
National Harbor and MGM Springfield - reported:

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Net revenues | $10,783.2M | $10,825.1M | **$10,580.2M** |
| **Operating income** | **$1,324.6M** | **$733.7M** | **$78.5M** |

**A 94% fall in two years on 1.9% less revenue.** Assign every consolidated one-off to that group
and the series still reads about **$954M to $815M to $483M**, a 49% fall. Note 10 says the same
thing in one line: **domestic pre-tax income of $1,214.9M (2023), $256.9M (2024) and MINUS $237.1M
(2025)**, with the whole of FY2025 pre-tax income arising abroad - and roughly 44% of the Macau
part of it belonging to the minority holders of a separately listed Hong Kong company, who took
**$315.0M** of FY2025 net income against the **$205.9M** MGM's own shareholders received.

**The mechanism.** MGM sold the only input in its business that cannot be reproduced, the land,
and leased it back on 25-to-30-year triple net master leases with fixed 2% escalators (floored at
2%, capped at 3% after year ten or fifteen). The balance sheet carries **$25,068,747 thousand** of
operating lease liability and **$54,679,646 thousand** of undiscounted future minimum payments
against **$6,305,614 thousand** of property and equipment. Cash rent was **$1,867,130 thousand** in
FY2025 (Note 11) against a **$2,258,405 thousand** accounting rent expense (Note 17) - two numbers
the filing keeps apart and every summary conflates.

### THE PRIOR THAT WAS REFUTED, AND THE ONE THAT HELD

- **REFUTED (my own, inside the run).** I wrote the competitor row off reported operating income
  and it invited the reading that MGM's margin fell in four consecutive years. **It did not.** In
  2021 reported operating income contains a **$1,562.3M** gain on consolidating CityCenter; in 2022
  a **$2,277.7M** REIT gain and a **$1,037.0M** Mirage gain, against a one-off **$2.5bn** Macau
  concession amortisation; in 2023 a **$398.8M** Gold Strike gain; in 2025 a **$278.9M** goodwill
  impairment. Cleaned, the series is **6.7%, 4.8%, 9.4%, 9.1%, 8.0%** - a post-pandemic recovery
  and two declines since, not a slide. **A correction block sits inside Q2 of the run file above
  the verdict, because leaving a wrong reading standing is worse than a wrong first draft.** The
  verdict does not turn on it: on the corrected figures MGM is still last among the profitable
  peers in every year.
- **HELD.** The screen's `wc_note` - one payables line moved 32% of 2021 operating cash - is exact:
  **+$442,626 thousand against $1,373,423 thousand** on the filed FY2021 cash-flow statement. But it
  is **neither the DELL shape (a payables stretch) nor the INOD shape (a customer prepayment)**. It
  is the COVID reopening swing: the same line was **minus $1,382,980 thousand** in 2020, and Note 8
  shows casino front money going $133.1M to $206.2M and advance deposits $123.1M to $283.2M as the
  resorts reopened. Genuinely non-repeating, and it distorts 2020 and 2021 in opposite directions.
- **HELD, and it is a whole class.** The screen's `da_note` said D&A steps 4.3x at 2023-12-31.
  Read: it is a step **DOWN**, from $3,482.1M (FY2022) to $814.1M (FY2023), and the FY2022 10-K
  states the cause - *"an increase of $2.5 billion in amortization expense of the MGM Grand
  Paradise gaming concession as a result of the change in its useful life"*, with Note 7 confirming
  *"Amortization expense related to intangible assets was $2.7 billion, $197 million and $194
  million for 2022, 2021, and 2020."* **[E3-44]'s D&A default for (c) would therefore charge $2.5bn
  of licence runoff as required capital spending.** The run built a **third (c) end** - depreciation
  only, D&A less intangible amortisation - and says why. This is the class the resume state warned
  about, where the corpus's own default runs the wrong way and only a reader sees it.
- **HELD, to the dollar.** The `acq_note`: acquisitions net of cash acquired were $1,789.6M (2021,
  the other half of CityCenter), $1,889.1M (2022, The Cosmopolitan operations and LeoVegas),
  $122.1M (2023, Push Gaming) and $113.9M (2024) = **$3,914.7M**, 40.3% of today's cap. All cash,
  so the stock-consideration source limit does not bind. And the perimeter moved **both** ways: out
  went The Mirage (2022), Gold Strike Tunica (2023) and Northfield Park (closed Q2 2026). The
  FY2021 owner-earnings figure and the FY2025 one measure different companies.

### THE SPREAD, REBUILT - the `spread_caveat` was right and understated

Eleven windows, three (c) ends, eighteen filed years. **Mean owner earnings run from about $40M
(2020-2025, c=D&A) to $1,679M (2023-2025, c=depreciation only).** The screen's published band of
**$607M to $1,558M reproduces exactly** as the five-year and three-year means at the c=D&A end -
**and the true width is about 42 times wider at the bottom.** Five-year default: $607M to $1,259M.
Eighteen-year record: $175M to $543M. Against a $9,709M cap that is a yield of **0.4% to 17.3%**,
or 3.0% to 14.1% on the recent windows after the noncontrolling interests' claim. **[E4-25]: the
width IS the conclusion.** SBC resolves and is **COMPLETE for all 18 years**, checked before any
band was used.

### THE DEATH, AND THE SHAPE

**Shape #13 THE TENANT is the mechanism, with #1 CONTRACTED NOT TO STOP as its feature. No new
shape is proposed.** One honest amendment to the index's one-liner is stated in the run rather than
glossed: **MGM's rent is not reset at renewal, it is escalated by contract**, which protects it
from a market reset and removes any possibility that the rent falls when the business does. The
non-exclusivity is established from **VICI's own FY2025 10-K** rather than inferred: *"Caesars and
MGM, our two largest tenants representing 39% and 35%, respectively, of our annualized rent"*, with
MGM's leases parent-guaranteed and, per VICI, cross-defaulted across the entire portfolio.
Quantified: hold domestic revenue flat and the 2% escalator alone (about **$37.6M a year,
compounding**) consumes the guarantor group's ~$483M of adjusted operating income in roughly
thirteen years; one year of the 4.3% Las Vegas revenue decline that actually happened in FY2025, at
the 33.9% segment margin, costs about **$154M**. **A real possibility**, not likely and not
low-level, because the domestic leg has **already** crossed into a pre-tax loss. **[E4-40]:** the
comforting reading is that MGM survived 2020 - that is experience, and it is dangerous, because the
balance sheet that survived 2020 **owned** Bellagio, MGM Grand, Mandalay Bay and Aria and could
sell them, which is exactly what it did. That option has been spent.

### Q3, RECORDED BENEATH THE CLOSE

**[E4-29] fires at full strength, and this is the sharpest EBITDA finding the project has recorded
since CGNX.** MGM does not trumpet EBITDA; it trumpets **EBITDAR**, the same measure with the rent
removed as well. Segment Adjusted EBITDAR of **$5,134.0M** is 5.1x the **$1,001.8M** of operating
income, and the largest thing it deletes is a **cash** cost paid in cash and contractually owed for
29 more years. Because ASC 280 permits it, the release calls it *"our reportable segment GAAP
measure"* four times. **And the pay follows the measure [E4-27]: 75% of the CEO's annual bonus
turns on "Compensation Adjusted EBITDAR"**, whose target the proxy says was the board's budgeted
EBITDA *"as further increased by the Company's rental payments"*; 2025 outturn $4,304,248,000 and
approximately 100% of target paid, in the year the guarantor group's operating income fell 89% and
domestic operations lost money. The long-term incentive is 50% relative-TSR PSUs and 50% RSUs, so
**no part of the pay package is measured after rent or after depreciation.** [E4-52]: three flags
pointing one way are one system, not three prompts.

**[E2-49] fires with its mitigations named**: Absolute TSR PSUs removed and the Relative TSR index
moved from the S&P 500 to the S&P 1500 Hotels index in the single year 2025, with the stock down
from $44.88 (2021) to $36.49 (2025) - but announced ahead, with reasons and a consultant named, and
a negative-absolute-TSR funding cap retained. **[E4-30] recorded and it fires**: cash taxes 23.4%,
23.9%, then **minus 12.3%** of pre-tax income - and Note 10's explanation is worse news than the
flag, because it is the domestic loss and a $283.7M valuation-allowance release, not manipulation.
**[E3-54] fails**: market cap $15,575M (2020-12-31) to $9,426M (2025-12-31) plus **$9,406.8M**
returned = $18,833M, a $3,258M gain against **$4,822.2M** retained - **$0.68 per $1**.
**Three flags do NOT fire and are recorded as genuine positives**: no numeric guidance anywhere in
the earnings release, so [E3-48] and [E5-30] have nothing to bite on; no serial issuance (43% of
the shares retired); no dividend funded by issuance (the dividend is suspended and the 10-K says
so). **And [E2-26] passes**: the guarantor table, the domestic/foreign tax split and the cash-rent
line are all in the 10-K. **The filing tells you what you would want to know. The release does not,
and the pay plan is computed on the release's measure.**

### TOOLING AND PROCESS - four defects, one of them serious

1. **SERIOUS: `deal_note()` cannot see a bidder-disclosed go-private proposal, and MGM has one.**
   On **2026-06-01** People Incorporated (f/k/a IAC) filed a **Schedule 13D/A** on MGM attaching a
   letter from **Barry Diller**, who sits on MGM's board, proposing to buy every share it does not
   own for **$48.30 in cash**. Three months earlier MGM had signed a Voting Agreement with IAC and
   Mr Diller capping their voting power above **25.73%** (8-K of 2026-04-07). The screen's
   `deal_note` for MGM read *"2 8-K Item 1.01 filing(s) since 2026-02-11, none carrying a merger
   agreement (EX-2.1) - most likely a credit facility or offering; open them only if something else
   is odd."* **Both Item 1.01s were exactly what it guessed** (the voting agreement and an MGM China
   indenture). **The deal was in a form the function does not read: `DEAL_FORMS` in
   `tools/sources.py` is `("DEFM14A", "PREM14A", "S-4", "S-4/A", "SC 14D9", "SC TO-T", "425")` and
   contains no Schedule 13D or 13D/A.** This is the **fourth** live-deal miss after CTAS, ACLS and
   ROKU, and it is a **new class**: not a signed agreement the company announces, but a proposal the
   BIDDER discloses. The 13D/A appears in the subject's own submissions index, so the fix is
   mechanical - a third, soft list. **Recorded, not fixed** (operator rule: tooling changes are the
   operator's). Effect on this run: the $38.59 quote sits inside an unresolved control contest. The
   stock closed **$47.81 on 2026-06-30**, within 1% of the offer, and **$37.81 on 2026-09-18**.
   An EDGAR full-text search of MGM's filings for "People Incorporated" returns exactly three
   documents, the latest 2026-07-29, so the proposal stands unanswered.
   **A second, smaller defect inside the same string:** `deal_note`'s text ends *"open them only if
   something else is odd"* - **that is a tool telling a run which document will be boring**, which
   is the CGNX prohibition of 2026-09-07 embedded in the tooling rather than in a brief.
2. **`THE FRAMEWORK v4.md` misquotes two of its own ledger rows, and `check_framework.py` cannot
   see it because it checks ledger rows against sources, not the framework's requotations of them.**
   (a) At Q4 staying power the framework writes *"We will never be dependent on the kindness of
   strangers … cash is a lot like oxygen"* and cites **[E5-39]**. The phrase "cash is a lot like
   oxygen" is **not in that row's `quote_verbatim`**; it is in the row's `concept` and
   `evolution_notes`, and the source line those notes record reads **"available cash or credit is a
   lot like oxygen."** Dropping "or credit" matters, because the sentence the framework uses it to
   support is *"no bank lines counted"*. (b) At Q2 the framework writes that *"That day is gone"* is
   how the administered-pricing escape ends and cites **[E2-59]**; that phrase is likewise in the
   row's evolution notes, not in its quote_verbatim. **Recorded for the operator. Nothing in
   `Framework/` was edited** (the run's standing rule), and the MGM run file quotes neither phrase.
3. **The MASTER RUN QUEUE CSV truncates three note fields mid-word, in the file itself.** MGM's
   `acq_note` ends *"may be different compa"*, `level_note` ends *"the pre-window years run from
   $-"* and `level_note_oe` ends *"$-2,047.7M t"*. The brief's paste was blamed for the
   `spread_caveat` truncation, but that one is intact in the CSV; **these three are cut on disk**,
   so a reader quoting them verbatim quotes a fragment. Recorded, not fixed.
4. **MY OWN, and it is a gitignore gap.** `.gitignore` ignores stripped filing dumps by **name
   pattern** (`*10-K*.txt`, `*10-Q*.txt`, `*8-K*.txt` and ten more). This run named its stripped
   FY2025 10-K `tenk_2025.txt` and its XBRL dump `companyfacts.json`; **neither matches any pattern,
   and both entered history in the Q1 commit** (about 1.1MB and 3.8MB). The comment above those
   rules says the names are *"strongly patterned"*; mine were not. **History is not rewritten**
   (operator rule 6). Recorded so the next session names its dumps to match, or the operator widens
   the patterns.
5. **`tools/sources.py` and `Screens/cover_shares.py` produced no wrong number.** The sovereign came
   from the Treasury directly, the cover count and accession are the filing's own, and every figure
   used in the run was cross-checked against a filed statement.
6. **`CLAUDE.md` still says `principle_ledger.csv` is 267 rows; the file counts 311.** The same
   stale pointer the SGC, JAKK, CRC and USNA cycles recorded. All **98** ledger ids cited in the MGM
   run file were verified present in the file before the commit.
7. **A quotation checker was written for this run and it caught nine of my own errors.**
   `Test Runs/_research 2026-09-21 MGM/quotecheck.py` extracts every quoted span from a run file and
   asks whether it resolves to the ledger, to a downloaded filing, or to nothing. It found that I
   had put **`THE FRAMEWORK v4.md`'s own commentary inside quote marks and attributed it to the
   corpus** in four places (under [E4-55], [E2-59], [E2-60] and [E5-11]), that I had written "what
   the business requires" where [E2-23] says "that", and that I had bracket-altered a proxy
   sentence. **All nine are fixed in the file.** PRIME RULE 1: paraphrase is never recorded as
   quotation, and the only reliable way to know is to check every span against its source.
8. **Em dashes normalised to hyphens** outside quoted spans and blockquotes; the survivors are two
   corpus blockquote attributions and the `COMPUTATION — NOT A CLEARANCE` heading required by
   operator rule 3.

### NO BAND, NO PORTFOLIO ROW

**`tools/alerts.json` is untouched and no `PORTFOLIO.md` row is added** - the QLYS ruling of
2026-09-07. The file closed at Q2, on the business, and a price band on a business finding is a
category error. **The reversal condition is in words at Q6 of the run file**, and the headline item
is the one number that would say the domestic tenant business can carry its rent: **the guarantor
group's operating income recovering toward $1bn on flat revenue**, from the 10-K MD&A's "Guarantor
Financial Information", against $78.5M in FY2025. Completion of the People Incorporated transaction
at $48.30 would **not** reverse it: that is a liquidity event for a holder, not evidence about the
business.
'''

io.open(P, "w", encoding="utf-8").write(t.rstrip("\n") + ADD)
print("appended", len(ADD), "chars")
