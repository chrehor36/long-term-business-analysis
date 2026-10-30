## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (from about 05:00 local); the template was copied and committed before any fetch
(`e1a6ce1`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the third name in the
"cap rejected as a broken input: read the cover" row (HBB, LCID, SOUN, BIRD). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-19 SOUN/` (scripts copied from the LCID folder with the CIK and ticker changed). **No SOUN row exists in
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`** (grepped: zero matches). Every figure below is from SoundHound's own filings,
fetched by this run, with the accession, unless marked otherwise.

### The entity, in every year used
CIK 0001840856, `submissions.json` (fetched by this run, `subs.py`): *"SOUNDHOUND AI, INC."*, SIC 7372 *"Services-Prepackaged
Software"*, incorporated in Delaware, fiscal year end 1231, tickers SOUN and SOUNW on Nasdaq. **Former name:** *"Archimedes Tech Spac
Partners Co"* (2021-01-15 to 2022-05-02): the registrant is the SPAC shell into which the operating company ("Legacy SoundHound", founded
2005) merged on 2022-04-26 (FY2022 10-K, Note 1: *"On April 26, 2022 (the "Closing Date"), pursuant to a merger agreement dated as of
November 15, 2021 by and among Archimedes Tech SPAC Partners Co. ("ATSP"), ATSPC Merger Sub, Inc. and SoundHound, Inc. ("Legacy
SoundHound")..."*). The shell's own filings (10-Qs of 2021, the FY2021 10-K of 2022-03-09, and its two Item 4.02 8-Ks of 2021-12-28 and
2022-01-10 in the SPAC-warrant restatement wave) are the shell's, not the business's. **Every annual year used below is Legacy
SoundHound's**, taken from the combined company's 10-Ks (FY2021-22 from the FY2022 10-K, which presents Legacy SoundHound as the
accounting predecessor).

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"cap rejected as a broken input: read the cover."* The triage narrative (reading list line 1429-1434): the sanity guard,
*"a yield outside -100% to +50%, or a cap under $5M, is **a broken input and never a finding**. It immediately caught four more -
**BRK-B** ... plus LCID, SOUN and BIRD."* **A prompt to read, never a verdict.** Three hypotheses were tested (`_probe_screen.py`,
`triage_repro.py`, outputs beside them).

**(a) A per-class dimensioned cover plus a stale undimensioned fallback fact (the HBB two layers): CONFIRMED, both layers, and the
stale fact is the SPAC shell's.** The inline XBRL of the Q2 2026 10-Q (`0001840856-26-000022`, raw `10Q_2026Q2_raw.htm`, `dei_out.txt`)
tags `dei:EntityCommonStockSharesOutstanding` **twice, dimensioned on `us-gaap:StatementClassOfStockAxis`**: **411,574,436**
(`CommonClassAMember`, context c-4, instant 2026-08-06) and **32,535,408** (`CommonClassBMember`, context c-5). companyfacts publishes
only undimensioned facts, so the only `EntityCommonStockSharesOutstanding` it carries for this CIK is **17,461,000, the Archimedes SPAC
shell's count**, last filed in the shell's FY2021 10-K on 2022-03-09 (five facts, 2021-07-20 to 2022-03-09). The undimensioned
`us-gaap:CommonStockSharesOutstanding` is no better: its newest dates carry **0** (2022-06-30 and 2022-09-30) and 196,503,710 at the
merger date 2022-04-26. `Backtests/scripts/bt17_microcap.py` `shares_asof(..., 2026-09-01)` returns **(2022-03-09, 17,461,000)**,
because it has no staleness test; the `a8bc84f` `shares_outstanding()` returns **None** with its 550-day test and the same
(2022-03-09, 17,461,000) without it.

**(b) A split or share-class change: REFUTED as the cause.** No split in the filings list or the price series (`split_factor_after` 1.0);
the two classes have existed since the 2022 merger; the `a8bc84f` `share_count_shift()` returns None (no dei series to compare).

**(c) Which bound tripped, reproduced.** On facts filed by 2026-09-01 the `a8bc84f` `owner_earnings()` returns **{5y_da: -$121.8M,
5y_capex: -$110.2M, 3y_da: -$156.5M, 3y_capex: -$139.7M}**. Over the stale shell count at the 2026-08-31 close ($7.16 x 17,461,000 =
**$125.0M**) the yields are **-97.4%, -88.1%, -125.2% and -111.7%**: the two three-year yields fall below the guard's -100% bound; at
the 2026-09-01 close ($6.85, cap $119.6M) three of the four do. Over the correct cover count (A+B 444,109,844 x $7.16 = $3,179.8M) the
same owner earnings give **-3.5% to -4.9%, inside the guard.** The cap was never under $5M. **So for SOUN the label was RIGHT in both
words: the cap was broken (the denominator was the SPAC shell's 2022 count, a twenty-fifth of the real one), and the guard caught it,
through its lower YIELD bound rather than the cap floor.** It is the HBB mechanism (per-class cover invisible to companyfacts, a stale
pre-business fact behind it) arriving by the LCID bound. **The instructive contrast with LCID:** there the correct count tripped the
yield bound on a real finding; here a stale count tripped the same bound on a broken input. A range guard on the quotient caught both,
and could tell them apart in neither.

**A second stale shell fact, in the owner-earnings series itself, which the brief did not name.** companyfacts' FY2021 operating cash
flow for this CIK is **-$0.864M: the SPAC shell's**, not Legacy SoundHound's **-$66.2M** (FY2022 10-K cash-flow face: *"Net cash used
in operating activities | ( 94,019 ) | ( 66,177 )"*). The screen's five-year window (FY2021-25) therefore averages four years of the
business with one year of a blank-cheque company, and its `working_capital_flag` fires on the shell's 2021 (*"OCF was $0.9M"*). The
five-year owner earnings the triage used are **understated in magnitude by about $13M a year** (see Q4, where the series is rebuilt
from the faces). SBC, D&A and capex for FY2021 in companyfacts are Legacy SoundHound's (6.3M, 5.5M, 0.6M), so the series mixes two
entities within one year. **The code that wrote the triage row is not on disk** (the HBB finding), so which count and which windows it
used are reconstructed, not read.

**The other guards** (`_probe_screen_output.txt`, current screen): `da_discontinuity_flag` fires at FY2024 (*"steps 6.9x UP ... $2M to
$16M"*: the Amelia and SYNQ3 intangibles, an acquisition, below); `lease_capex_flag` fires (25% of cash capex under a legacy element);
`scale_shift` 1.99; `acquisition_flag` $66.3M; `stale_filer` 262 days with two later 10-Qs; `restatement_shift` 1.0. `sbc_annual`
resolves for every year FY2021-25, so the SBC-of-zero defect does not arise at the charge level (its completeness is tested at Q4).
**Not a verdict**: Q4 rebuilds owner earnings from the filed faces.

**Restatement and control history (carried to Q3, dated).** No Item 4.02 by the combined company. But: prior-period **revisions** of
the statements for 2022-Q3, FY2022, 2023-Q1 and 2023-Q2 (FY2025 10-K Item 9A); **material weaknesses in internal control every year
from FY2023 to Q2 2026**, the current one reaching *"substantially all accounts and disclosures"*; late-filing notices (NT 10-Q
2023-11-15, NT 10-K 2024-03-01, NT 10-K 2025-03-04); and an auditor change in 2023 (Armanino resigned 2023-07-31, *"due to Armanino's
internal determination to no longer provide financial statement audit services to any public companies"* and *"not the result of any
disagreement"*, 8-K `0001840856-23-000035`; PwC appointed 2023-09-13, 8-K `0001840856-23-000050`). Auditor now PricewaterhouseCoopers
LLP; its ICFR opinion on FY2025 is adverse by the company's own account (*"management concluded that the Company did not maintain
effective internal control over financial reporting as of December 31, 2025"*).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run at
  05:04 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.34, '09/18/2026', 'US Treasury daily par yield curve')** in the same minute
  (`step0_out.txt`). FRED not used. Struck by this run, not inherited.
- **Earnings currency: USD.** Statements in US dollars (functional currency of the company and its subsidiaries is the US dollar, FY2025
  10-K Note 2); FY2025 revenue 69% Americas, 16% Asia, 15% EMEA. No ADR or FX conversion of the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$5.93, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("SOUN", rng="1mo", max_age_h=0)`
  (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 5.93, `regularMarketTime` 1789761601
  = 16:00:01 EDT, exchange NGM; the day's bar $5.83-$6.08 on 19.9M shares. `tools/sources.price()` returned the same 5.93 stamped
  2026-09-18.
- **The path** (`price2y_out.txt`): $9.97 at 2025-12-31; $8.36 on 2026-02-24; $8.32 on 2026-04-20 (the day before the LivePerson
  announcement) and $7.85 the next; $6.55 on 07-02 (the amended merger agreement); $6.43 on 08-05 (the Q2 release) and $7.08 on 08-06;
  **$7.16 on 08-31**; $6.74 on 09-04 (the closing); $5.93 on 09-18. Two-year high $24.23 (2024-12-26), low $4.56 (2024-10-01).
- **Primary-filing corroboration:** the merger terms fix a SoundHound price implied by the filer's own numbers: *"the Per Share Merger
  Consideration ... will be an amount equal to 0.4673 shares of Class A Common Stock"* and *"the Per Share Cash Merger Consideration
  ... will be an amount in cash equal to $3.31"* (8-K of 2026-09-02, `0001213900-26-096796`), so the closing VWAP the agreement used was
  about **$7.08** ($3.31 / 0.4673); and the noteholders' $261.2 million of consideration (Q2 2026 10-Q Note 3) settled in 36,894,839
  shares plus $5.8M of cash implies about $6.92-$7.08 a share. Yahoo's closes in the last days of August and early September are
  $6.74-$7.16. **The aggregator's series is corroborated at the closing**; the 2026-09-18 close rests on the aggregator alone.
- **Split factor after the count's date: 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and what happened after it
- **Cover of the Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-10, accession `0001840856-26-000022`**, the latest periodic
  filing: *"As of August 6, 2026, there were 411,574,436 shares of the Company's Class A Common Stock, $0.0001 par value per share,
  issued and outstanding, and 32,535,408 shares of the Company's Class B Common Stock, $0.0001 par value per share, issued and
  outstanding."* `python Screens/cover_shares.py SOUN` read the same two numbers and printed *"MULTIPLE CLASSES ... READ THE FILING."*
- **The charter was read before the classes were added** (the S-3ASR base prospectus as supplemented, 424B7 `0001213900-26-097476`,
  Description of Capital Stock): Class A one vote, Class B ten votes; *"Each share of Class B Common Stock shall convert into one fully
  paid and nonassessable share of Class A Common Stock"* (Q2 10-Q Note 11); both classes *"are entitled to receive dividends"* and on
  liquidation the assets *"are distributable ratably among the holders of our Class A Common Stock and Class B Common Stock"*. **The
  classes differ in votes only and convert one for one, so they are summed: 444,109,844.** (The votes matter at Q3: the founders' Class
  B carries 325.4M votes against 411.6M of Class A.)
- **Cross-check against the filed balance sheet (rule 4):** at 2026-06-30 *"403,287,100 and 390,070,691 shares issued and outstanding"*
  (Class A) and *"32,535,408 shares issued and outstanding"* (Class B). The +8,287,336 Class A between 06-30 and 08-06 is mostly the
  **8,126,674 shares issued in July 2026 to settle the 2025 portion of the Amelia earnout** (Note 17). The 424B7 of 2026-09-04 gives
  **411,576,753 Class A at 2026-08-31**: no ATM sales in August.
- **THE COVER IS STALE BY A CLOSED STOCK DEAL.** On **2026-09-04**, after the cover date, SoundHound closed its acquisition of
  **LivePerson, Inc.** (8-K `0001213900-26-097712`) and issued: **36,894,839 Class A shares** to LivePerson's secured noteholders
  (*"25,142,335 shares of Company Common Stock and an aggregate amount of cash equal to $2,499,450"* for the First Lien notes and
  *"11,752,504 shares of Company Common Stock and an aggregate amount of cash equal to $3,348,550"* for the Second Lien notes); plus
  **0.4673 shares for each LivePerson share** not held through the Tel Aviv clearing house. **That second number is not filed**: the
  S-4 prospectus (424B3 `0001213900-26-076737`) estimated *"approximately 3.0 million to 5.1 million shares of SoundHound Common Stock"*,
  and 12,332,427 LivePerson shares at the record date x 0.4673 = **5.76M is the ceiling** if no share was held through Tel Aviv. The
  S-4MEF of 2026-09-04 registered 726,888 more LivePerson shares for exchange; the S-8 of the same day registered 220,285 shares for
  assumed LivePerson RSUs (not outstanding).
- **Pro forma count after the closing: 411,576,753 + 32,535,408 + 36,894,839 + 3.0M to 5.76M = about 484.0M to 486.8M.** The first
  periodic filing to carry it will be the Q3 2026 10-Q.
- **Beside the count, not in it:** the remaining Amelia earnout of up to **8,695,755 shares** (16,822,429 less the 8,126,674 issued) on
  the 2026 revenue target, *"assessed ... probable of being met"*; 3,654,115 warrants at $11.50; 3,883,413 options; 15,971,969 RSUs
  (both at 2025-12-31); a **$300.0M at-the-market programme** entered 2026-05-11, unused at 06-30 (the second, $250M, programme sold
  13,913,014 shares at $14.48 in 2025 and $48.5M more in H1 2026).

### THE PAIR
**Cover basis: US$5.93 x 444,109,844 x 1.0 = US$2,633.6M. Pro forma for the 2026-09-04 closing: US$5.93 x about 484.0M-486.8M = about
US$2,870M-2,887M.** The pro forma is the economic cap (the shares exist; only their count is unfiled) and is used at Q5, with the cover
figure beside it. Beside the cap at 2026-06-30: cash and equivalents **$202.8M**, no funded debt (*"No interest expense was incurred
during the year ended December 31, 2025"*; Q2 2026 interest expense $0.1M), contingent acquisition liabilities **$83.6M** (the Amelia
2026 share tranche and the Interactions cash earnout), and after 09-04 whatever cash LivePerson brought and the $5.8M paid to its
noteholders and up to $7.5M to its Tel Aviv holders.

### The deal check
`sources.deal_filings("0001840856")` returned **seven deal-form filings since the FY2025 10-K** (425s of 2026-04-21, 07-02, 07-24 and
09-02; S-4 and two S-4/As) and printed *"LIVE DEAL FORM ... IF A DEAL IS LIVE THE QUOTE IS A SPREAD"*. **Read, per the ROKU lesson:
SoundHound was the ACQUIRER, paying in its own stock, and the deal CLOSED on 2026-09-04.** The SOUN quote is therefore not a spread on
anyone's offer; it is the price of a company that has just changed its perimeter. **No live offer for SOUN** (no SC TO, SC 13E-3 or
DEFM14A naming it as target).

### The perimeter: every acquisition in the windows used, from the filings
| date | business | consideration (filed) | what it changes |
|---|---|---|---|
| 2024-01-03 | **SYNQ3** (restaurant voice ordering) | $15.8M: $3.9M cash, 5,755,910 shares, holdbacks, earnout up to 1,434,936 shares | FY2024 onward; contributed $12.0M revenue in FY2024 |
| 2024-06-14 | an unnamed immaterial acquisition | $1.0M, a $1.2M bargain-purchase gain, *"pre-filing bankruptcy status of the selling entity"* | immaterial |
| 2024-08-06 | **Amelia Holdings** (enterprise conversational AI) | $98.6M: 3,809,520 shares + 2,149,530 in escrow + earnout up to **16,822,429 shares**; $121.5M of Amelia debt assumed and repaid in December 2024 | five months of FY2024 ($42.0M revenue), all of FY2025 on |
| 2025-09-03 | **Interactions** (AI customer service) | $76.1M: $19.4M cash, **$41.5M of its debt paid**, earnout up to $25.0M cash | four months of FY2025 ($23.1M revenue, 14% of FY2025) |
| 2026-05-12 | an unnamed private company (asset acquisition, "MIPA") | up to $30.2M cash, $26.1M paid by 06-30 | H1 2026 investing |
| 2026-07-29 | $5.0M of preferred shares of an unnamed private company | cash | an investment, not consolidated |
| 2026-09-04 | **LivePerson** (enterprise digital messaging) | about $42.8M to its shareholders (0.4673 SOUN shares or $3.31 cash each) and **$261.2M to its secured noteholders** (36,894,839 shares plus $5.8M cash) | after every period used here; the first filing to carry it is the Q3 2026 10-Q |

**How the perimeter changes the comparability of the years:** FY2021-23 are Legacy SoundHound alone; FY2024 adds SYNQ3 for the year
and Amelia for five months; FY2025 adds Amelia for the year and Interactions for four months; H1 2026 adds Interactions for the half.
**The filer's own pro forma** (FY2025 10-K Note 3, *"as if the SYNQ3 and Amelia acquisitions were completed on January 1, 2023, and the
Interactions acquisition was completed on January 1, 2024"*) gives combined revenue of **$153.6M (FY2023), $225.6M (FY2024) and
$211.7M (FY2025)**, and the FY2024 10-K's pro forma without Interactions gives **$143.5M for FY2024 against $153.6M for FY2023**. Read at
Q1 and Q2: **the reported revenue doubled while the same set of businesses, owned throughout, shrank.**

### The filing was read (rule 4)
- [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
- **Documents:** FY2025 10-K filed 2026-03-02 (`0001840856-26-000006`); Q2 2026 10-Q filed 2026-08-10 (`0001840856-26-000022`); Q1 2026
  10-Q (`0001840856-26-000015`); 10-Ks FY2024 (`0001628280-25-011821`), FY2023 (`0001840856-24-000013`), FY2022
  (`0001840856-23-000019`); 10-Qs Q2 and Q3 2025; DEF 14A 2026 (`0001213900-26-041978`); the LivePerson S-4 prospectus (424B3
  `0001213900-26-076737`), S-4MEF, S-8 and the 424B7 resale supplement; the 8-Ks and exhibits named in this file. Raw text in the
  research folder (`*.txt`, `.flat.txt`).
- **Figure cross-checked against the filed statement:** FY2025 net cash used in operating activities, *"Net cash used in operating
  activities | ( 98,222 ) | ( 108,878 ) | ( 68,265 )"* (FY2025 10-K cash-flow face) against companyfacts' -98,222,000 for FY2025:
  **identical**; FY2025 stock-based compensation *"80,620"* against the tag's 80,620,000: identical. **And the one that does not match:
  FY2021**, where companyfacts carries the shell's -$0.864M against Legacy SoundHound's filed -$66,177 thousand (above).
