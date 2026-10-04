# Company Run - SoundHound AI, Inc. (SOUN) - 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The unit economics, in my own words, without management's language
SoundHound sells software that lets a machine understand and answer speech, in two ways. **(1) It licenses the engine to makers of
cars, televisions and devices**, who pay either a fee per unit shipped or used, or a fixed licence fee with a minimum guarantee
that SoundHound books as revenue on the day the licence is granted and collects over the contract (FY2025 10-K Note 2: *"Licensing
revenue on fixed considerations including fixed fee and minimum guarantee from royalty arrangements are recognized when the Company
grants the customer the right to use and benefit from the license at the start of the licensing period"*). The filer calls this
"product royalties". **(2) It runs hosted voice and chat agents for businesses**: phone and drive-through ordering for restaurants
(SYNQ3), and, since the Amelia (2024), Interactions (2025) and LivePerson (2026) purchases, customer-service agents for enterprises,
billed as subscriptions or per use. The filer calls this "service subscriptions"; it has been most of the revenue since FY2024. A
third stream, advertising in the old music-identification app, is under 0.3% of revenue. **Its costs are people and computing**:
cost of revenue is *"costs and depreciation related to hosting for cloud-based services, such as data centers, electricity charges,
content fees and certain personnel-related expenses including personnel costs under call centers"* plus amortisation of acquired
technology (FY2025 10-K Item 7), and below the gross line it spends on engineers, salespeople and administration. From the filed faces
(10-Ks FY2022-25, Q2 2026 10-Q), $M:

| line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 21.2 | 31.1 | 45.9 | 84.7 | 168.9 | 106.1 |
| of which product royalties (licences and per-unit) | 18.4 | 28.4 | 43.3 | 28.0 | 34.9 | 23.2 |
| of which service subscriptions (hosted agents) | 1.6 | 1.8 | 1.9 | 56.3 | 133.5 | 82.8 |
| of which licensing (Note 4; point in time unless customised) | 0 | 8.3 | 18.6 | 17.6 | 45.1 | 29.1 |
| Gross margin | 68.9% | 69.2% | 75.4% | 48.9% | 42.4% | 39.3% |
| R&D + S&M + G&A | 79.9 | 127.2 | 98.6 | 152.9 | 242.1 | 140.8 |
| **Operating loss before the earn-out mark** | **(65.3)** | **(105.7)** | **(68.6)** | **(118.7)** | **(186.4)** | **(109.1)** |
| earn-out fair-value change (non-cash; a gain is negative) | | | | 222.7 | (163.1) | (43.1) |
| Operating loss as reported | (65.3) | (105.7) | (68.6) | (341.4) | (23.3) | (66.0) |
| Contract assets and unbilled receivables, year end | | 8.7 | 28.3 | 39.5 | 68.1 | 82.9 |

*(FY2022 operating loss as revised in the FY2023 10-K, $105,672 thousand against the $105,407 first filed. FY2023 includes $4.6M of
restructuring. The earn-out line is the change in fair value of the SYNQ3, Amelia and Interactions contingent consideration, driven
mainly by SoundHound's own share price: *"The fluctuation is non-operating and non-cash in nature"*, FY2025 10-K Item 7.)*

Read as a business:
1. **It has never covered its costs.** The operating loss before the earn-out mark has been between $65M and $186M every year, about
   1.0 to 3.4 times revenue. The FY2025 net loss of $14.0M, which reads as near-breakeven, is a $163.1M non-cash gain on the fall in
   the value of shares it owes the sellers of Amelia; the H1 2025 net *income* of $55.2M is the same gain.
2. **The revenue doubled by purchase, and the same businesses owned throughout shrank.** The filer's own pro forma: $153.6M
   (FY2023), $143.5M (FY2024, without Interactions) and, with Interactions, $225.6M (FY2024) and $211.7M (FY2025) (FY2024 and FY2025
   10-K Note 3). Arithmetic on the filed contributions: FY2024 revenue less SYNQ3's $12.0M and Amelia's $42.0M leaves about **$30.7M for
   Legacy SoundHound against $45.9M the year before**; FY2025 revenue less Interactions' $23.1M leaves $145.8M for the FY2024 perimeter
   against its $143.5M pro forma, **about +1.6%**.
3. **A growing share of the revenue is booked before it is billed.** Licensing (booked at a point in time unless the solution is customised) was $45.1M of FY2025 revenue (27%) and
   $29.1M of H1 2026 (27%); contract assets and unbilled receivables rose from $8.7M (FY2022) to **$82.9M at 2026-06-30, about 41% of
   trailing-twelve-month revenue of $203.2M**, $48.1M of it non-current (to be billed beyond a year). Four customers hold 69% of the
   unbilled balance (Q2 10-Q Note 2: *"unbilled receivables from Customer A, B, C, and D accounted for 19 %, 19 %, 17 %, and 14 %"*).
   This is GAAP (ASC 606 requires it for a fixed-fee licence), and it is a Q3 read, not a finding of error; for Q1 it means reported
   revenue runs ahead of cash, which is why operating cash is worse than the operating line in FY2025 (Q4).
4. **Concentration moved from one customer to many smaller accounts** (the filings do not name Customer C). FY2023: *"Customer C and G accounted for 49 % and 13 % of
   revenue"*; FY2024 Customer C 14%; FY2025 none above 10% (10-K Note 2). Legacy royalties fell from $43.3M to $28.0M (-35%) in FY2024
   when that concentration unwound.

### The scarce input this business controls
**Its own speech engine and the contracts it has bought.** The 10-K's claim is technical: *"Our proprietary Speech-to-Meaning
technology tracks speech in real-time"*, *"over 359 patents granted and over 102 patents pending"*, and *"Due to the high barrier to
entry in Voice AI, the number of full solution platform providers is very limited"* (Item 1). Against that, the same Item 1 says its
chat product combines its domains *"with the most cutting-edge large language models like OpenAI's ChatGPT"*: the component that
changed the field in 2023 is rented, not owned. **The customer relationships are the one input that grew**, and they were bought:
Amelia, Interactions and LivePerson brought the enterprise customer base the 2026 releases describe (*"a customer base that includes 25
of the Fortune 100"*, EX-99.1 of 2026-09-04). Whether any of this is a position is Q2's question.

### Will the fundamentals look broadly the same in ten years?
**The company says not, in its own risk factor**: the market is *"characterized by intense competition, evolving industry and
regulatory standards, emerging business and distribution models, disruptive software technology developments, short product and
service life cycles, price sensitivity on the part of customers, and frequent new product introductions, including alternatives to
certain of SoundHound's products from other vendors which may be offered at significantly lower costs or free of charge"* (FY2025 10-K
Item 1A). The CEO's framing in the FY2025 release is *"As traditional software faces massive AI disruption"*; the product line has
moved from a music app (2009) to a developer platform (2016) to restaurant ordering (launched *"After we went public in 2022"*) to enterprise *"agentic AI"* (2025) to an
omnichannel customer-service suite (2026) in ten years.

### The case for UNKNOWABLE, recorded and not taken
[E3-31] asks for businesses *"relatively simple and stable in character. If a business is complex or subject to constant change,
we're not smart enough to predict future cash flows."* SoundHound is subject to constant change by its own description. **Not taken,
for the same reason as the RIVN, BZFD, PATH and LCID runs:** Q1 asks whether I can understand how the money is made, and the filings
make that plain: licences sold to device makers, hosted agents rented to businesses, costs of people and computing that have run at
one to three times revenue, and a revenue line built by acquisition. What cannot be predicted is the next product (agentic AI, voice
commerce, the LivePerson integration), which I keep **outside the circle [E3-31, E4-46]**; the business the filings show can be judged
at Q2 on evidence already in. Writing UNKNOWABLE here would avoid a finding the record supports, the error [E3-47] warns of in
reverse. **No degree-of-difficulty credit is claimed [E4-18].** And the circle's limit is stated at [E4-46]'s standard: a business
that took months to understand would be Q1 OUT; this one took one reading of four 10-Ks.

- **VERDICT: [x] IN** - the money-making is understandable from the filings; the future product economics are kept outside the
  circle and carried to Q2 as a franchise question, not guessed.

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The brief's instruction, followed first: argue for the franchise before ruling.** The strongest evidence FOR one, from SoundHound's
own documents:
- **Design-win stickiness, in the filer's words:** *"After a design win, a product or technology that did not receive the design win
  may not be able to displace the winner until the customer begins a new selection process because it is very unlikely that a
  customer will change complex technology until a product model is revamped"* (FY2025 10-K Item 1A). That is a switching cost, and in
  cars it lasts a model cycle.
- **Renewals and unit commitments** (EX-99.1 of 2026-02-26): *"Signed a new prominent OEM in Japan with a seven-digit unit
  commitment"*; *"One of the largest American automobile manufacturers signed a multi-year renewal"*; *"Renewed with Casey's General
  Stores ... with a multi-year agreement"*; an athletic-footwear supplier *"renewed its corporate contract for multiple years"*.
- **Per-unit royalty economics** in the licence stream (*"The product creator pays us a royalty based on volume, usage, or
  duration"*, Item 1), and a white-label position the filer says big technology cannot offer (*"there is no conflict of interest
  between us and our partners and customers as we do not compete with them"*).
- **A named rival confirms it wins business:** Cerence, the automotive voice incumbent, lists *"SoundHound in the U.S."* among
  *"Small, focused competitors"* that *"have had some success selling into our customer base"* (Cerence FY2025 10-K, filed 2025-11-20,
  `0001628280-25-053372`, Item 1).
- 359 patents granted, and legacy gross margins of 69-75% (FY2021-23) before acquired call-centre work diluted them.

Each of these is evidence that the product is **needed or desired** (criterion 1) and that SoundHound can win a contract. None is
evidence of criterion 2, and the same documents answer criterion 2 directly.

### The three conditions **[E3-03]**, on SoundHound's own filings
- **(1) Needed or desired: YES.** $203.2M of revenue in the twelve months to 2026-06-30; renewals above.
- **(2) Thought by its customers to have no close substitute: NO, in the filer's own words, in every 10-K read.** *"alternatives to
  certain of SoundHound's products from other vendors which may be offered at significantly lower costs or free of charge"*; *"Some of
  SoundHound's current or potential competitors are large technology companies that have significantly greater financial, technical
  and marketing resources"*, and they *"may be able to include or combine their competitive products or technologies with other of
  their products or technologies in a manner whereby the competitive functionality is available at lower cost or free of charge"*;
  *"current or prospective customers may decide to develop competing products"* (FY2025 10-K Item 1A). **The pricing is the buyers'
  vote**: *"SoundHound may be expected to quote fixed prices or be forced to accept prices with annual price reduction commitments for
  long-term sales arrangements"* (Item 1A, *"Pricing pressures from SoundHound's customers may adversely affect its results of
  operations"*). **And the switching cost cuts both ways in its own release:** *"An iconic Italian manufacturer of high-performance
  sports cars chose SoundHound to displace their incumbent native voice assistant"* (EX-99.1 of 2026-02-26): incumbents in this field
  are displaced, including by SoundHound. The auto incumbent's own 10-K carries a near-identical paragraph (*"alternatives for certain of
  our products that offer limited functionality at significantly lower costs or free of charge"*, and the same *"annual price
  reduction commitments"*), so this is the industry's condition, not one filer's modesty.
- **(3) Not subject to price regulation: YES.**

**Criterion 2 fails on the filer's own account; Q2 closes on it.** The tests below are recorded because they point the same way.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04, E4-23, E5-23]**
**Its basis is replaced, not defended [E4-04].** R&D was $98.3M in FY2025, **58% of revenue**, and the engine the company built for ten
years in "stealth" now sits beside a rented one (*"We combine this with the most cutting-edge large language models like OpenAI's
ChatGPT"*, Item 1). The filer calls the field one of *"short product and service life cycles"*. Since January 2024 it has bought five
businesses (SYNQ3, Amelia, Interactions, an unnamed MIPA target, LivePerson) to reach customers and channels its own product did not:
that is the class v4 scopes [E4-04] to exclude, *"the moat whose basis must be periodically replaced"*, bought rather than built. The [E5-23] defence test asks whether a lapse in spending
would merely narrow the structure or destroy it: in a market where a competitor's functionality can arrive *"free of charge"* inside a
larger offering, a lapse ends it. **Key person [E4-23]:** founder-run since 2005 (*"To this day, the Company is still run by its original
founding team"*), with the three founders holding all 32.5M Class B shares (ten votes each). Not the decisive defect; recorded.

### Primary moat metric, filing-sourced, and its trend
**Like-for-like revenue and contracted revenue, both falling.** (a) The filer's pro forma (Q1): the same businesses owned throughout
went $153.6M (FY2023) to $143.5M (FY2024), and $225.6M to $211.7M (FY2024 to FY2025, with Interactions); Legacy SoundHound's own
revenue fell from $45.9M to about $30.7M in FY2024. (b) **GAAP remaining performance obligations** (10-K and 10-Q MD&A): $20.7M
(FY2022), $12.7M (FY2023), $83.3M (FY2024, with Amelia), $69.2M (Q2 2025), $70.6M (Q3 2025), $79.5M (FY2025, with Interactions), $64.7M
(Q1 2026), **$60.0M (Q2 2026)**: falling for two quarters while reported revenue rose 45%, and **$37.3M due within a year against
$203.2M of trailing revenue, about two months of it.** Most revenue is not under committed contract at any date. (c) Gross margin 75.4%
(FY2023) to 42.4% (FY2025) and 39.3% (H1 2026), diluted by acquired, more labour-heavy services.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4)*
Peers from the documents, since **SoundHound's 10-K names no competitor** (a search of the FY2025 10-K for every name in Cerence's list
returned none; its Item 1 speaks of *"big tech"* companies and *"legacy
vendors"* without names; the brief's instruction to take peers from its competition section could not be followed as written):
**Cerence** names SoundHound and is the automotive voice incumbent; **LivePerson** (digital customer engagement, bought on 2026-09-04);
**Five9** and **NICE** from the selected-companies list of LivePerson's fairness opinion in the S-4 (*"Bandwidth Inc. • Five9, Inc. •
LINK Mobility Group Holding ASA • NICE Ltd. • RingCentral, Inc. • Sangoma Technologies Corporation • Sprinklr, Inc. • 8x8, Inc."*).
Same metric, same window (FY2021-25; Cerence's fiscal year ends 30 September), from each company's filed annual statements as
transcribed in companyfacts (`peers/peer_row.py`, `peers/peer_5y.py`, outputs beside them); one Cerence figure checked to its filed
face (operating cash FY2025 *"61,173"*, Cerence 10-K, against 61.2 in the row).

| Company | revenue FY2021 to FY2025, $M (CAGR) | gross margin FY2025 | operating margin FY2025 | five-year owner cash per revenue dollar (OCF less SBC, capex, capitalised software) | SBC / revenue, five years | source |
|---|---|---|---|---|---|---|
| **SoundHound** | 21.2 to 168.9 (+68%, **bought**; filer's pro forma -6.6% FY2024 and -6.1% FY2025) | **42.4%** | **-110.4%** before the earn-out gain (-13.8% as reported) | **-176.3%** | **50.3%** | 10-Ks FY2022-25 |
| Cerence (auto voice) | 387.2 to 251.8 (-10.2%) | 72.7% | -0.9% | -4.8% | 11.3% | 10-Ks FY2021-25 |
| LivePerson (digital CX) | 469.6 to 243.7 (-15.1%) | 71.5% | -32.3% | -26.3% | 11.7% | 10-Ks FY2021-25 |
| Five9 (contact centre) | 609.6 to 1,149.1 (+17.2%) | 55.1% | +2.5% | -10.1% | 17.9% | 10-Ks FY2021-25 |
| NICE (customer experience) | 1,921.2 to 2,945.4 (+11.3%) | 66.4% | +21.9% | **+14.7%** | 6.9% | 20-Fs FY2021-25 |

- **Peers taken: four filers**, of the field the documents name: Cerence adds Amazon, Apple, Google, Microsoft, Alibaba, Baidu and
  Tencent (voice assistants inside larger businesses, **unsegmented**: no voice line can be pulled) and iFlyTek (not an SEC registrant);
  the fairness list adds Bandwidth, RingCentral, Sprinklr, 8x8, LINK Mobility and Sangoma (not pulled: communications platforms more
  than voice AI, the two last not SEC filers). Verint's companyfacts stop at its fiscal year to January 2025; not used.
- **Position: SoundHound is last on every margin and cash column**, and its growth is the only column it leads, bought with stock and
  cash. The only filer in the row with a franchise-like record, NICE, earns +14.7 cents of owner cash per revenue dollar; SoundHound
  consumes $1.76. It is not narrowing the gap with the incumbent it displaces in cars: Cerence, shrinking, still converts revenue to
  near-breakeven owner cash; SoundHound's owner cash is worse than minus its revenue.
- **The row's limit [E3-61]:** it shows position, not conduct; the big-technology rivals cannot be put in it at all, which cuts against
  SoundHound, since they are the ones the filer says can give the function away.
- **Untapped pricing power [E3-33]:** none. No price increase appears in any 10-K, 10-Q or release read (FY2022 to Q2 2026); the filings
  describe the opposite, annual price reductions to carmakers.
- **Class: [x] NONE** · **Direction: narrowing** (like-for-like revenue down, RPO down, gross margin down).

### THE OTHER Q2 TESTS
- **Returns on capital [E3-46]:** pre-tax operating result before the earn-out mark over capital employed net of cash: negative capital
  employed in FY2021, FY2022 and FY2024 (losses had consumed the equity, so the ratio is not a number); about **-400% (FY2023) and -87%
  (FY2025)** ($186.4M lost on $215.3M of equity less cash); on tangible capital, negative in every year (FY2025 goodwill and intangibles
  $303.7M exceed equity less cash).
- **The two-characteristic test [E2-44]:** raising prices with flat demand, no evidence; growing dollar volume *"with only minor
  additional investment of capital"*: the reverse, revenue grew after $54.6M (FY2025) and $11.7M (FY2024) of cash acquisitions, $98.6M of
  stock consideration for Amelia, and 36,894,839 shares plus $5.8M of cash for LivePerson's creditors.
- **The attacker's test [E2-45]:** the competitor Buffett imagines *"assuming I had ample capital and skilled personnel"* is the filer's own description of its competition
  (*"significantly greater financial, technical and marketing resources"*), and the capability it would need, a large language model,
  is the one SoundHound itself rents.
- **Direction [E4-32] and units [E4-55]:** no unit series is filed (no devices, queries or locations by year), so the dollar series has
  to serve, and on the like-for-like dollars the business is shrinking; the one legacy line, royalties, fell 35% in FY2024.
- **Which cause of success [E4-36] and the surfing test [E3-51]:** the record's growth comes from wave-riding (the generative-AI wave of
  2023 onward that the filer calls *"an inflection point"*) and from purchases paid for with a share price the wave lifted (two-year
  high $24.23 on 2024-12-26); *"if he gets off the wave, he becomes mired in shallows"*. A surfing run is not a moat.
- **[E4-37]:** no price rise to agonise over; the inverse metric is not triggered because pricing runs one way, down.

### CLASS AND VERDICT
- Class: **NONE** · Direction: **narrowing**.
- **VERDICT: [x] OUT**, on the business, [E3-03] criterion 2: the filer says its products face alternatives *"offered at significantly
  lower costs or free of charge"* from rivals with *"significantly greater"* resources, accepts *"annual price reduction commitments"*,
  and wins some of its contracts by displacing incumbents, which is the switching cost failing; with [E4-04] (a basis replaced by
  rented models and five acquisitions), [E3-46] (returns negative), [E2-44], [E2-45], [E4-32] (like-for-like revenue and RPO falling),
  and last place on the competitor row. **The file closes here.** Q3 to Q6 are recorded, not governing.

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL? *(recorded, not governing: the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### STEP 1 - THE WEIGHT CASE: a GATE, on daily execution
- [x] **Daily execution** **[E3-38, E3-43]**: Q2 found a business, not a franchise, and [E3-43]'s original form is that *"a business,
  unlike a franchise, can be killed by poor management"*. Every quarter the company must win contracts against free and bundled
  alternatives, integrate a fifth acquisition, and raise or preserve cash.
- [ ] **Control** **[E1-16]**: a minority buyer of Class A. (The founders' Class B carries 325.4M of about 737M votes before the
  LivePerson shares, about 44%; recorded at Q3, not a weight determinant for the buyer.)
- [ ] **Leverage** **[E3-29]**: no funded debt at 2026-06-30; LivePerson's secured notes were extinguished for shares at the closing.
- **Case declared: GATE, on daily execution.** No price would compensate a failure here.

### Honesty - binary, permanent, filings-based **[E5-16]**, each matter dated to when it became public
- **Securities class action, *Liles v. SoundHound AI, Inc.*** (filed 2025-03-28; class period 2024-03-01 to 2025-03-11; the company,
  the CEO and the CFO of the time, Nitesh Sharan, who resigned effective 2026-04-03 *"for personal reasons"*, 8-K of 2026-03-18). Q2 2026 10-Q Note 7: *"On May 19, 2026, the court granted SoundHound's motion in part and denied it in
  part. The court dismissed the claims based on the Amelia accounting statements, as well as several statements about SoundHound's
  efforts to remediate material weaknesses in its internal controls. The court denied the motion, however, as to certain
  internal-control statements."* Mediation was scheduled for 2026-08-25; no outcome is filed. **Pending, not adjudicated.**
- **Derivative suits** (*Bishop v. Mohajer*, 2025-04-08; *Roy v. Mohajer*, 2025-04-16): stayed behind the class action.
- **No SEC enforcement or inquiry** found in the FY2024-25 10-Ks or the 2026 10-Qs (searched for "subpoena", "investigation", "Wells
  notice", "Division of Enforcement": no match).
- **Two CFO changes**: Sharan resigned 2026-03-18 (no disagreement stated); a co-founder served as interim CFO; LivePerson's CFO, John
  Collins, was appointed on the closing (8-K of 2026-09-04).
- **The auditor change of 2023** (Armanino resigned *"due to Armanino's internal determination to no longer provide financial statement
  audit services to any public companies"*, *"not the result of any disagreement"*, with Armanino's agreeing letter filed as Exhibit
  16.1): an exit from the audit business, not from the client.
- **Verdict on the binary: no disqualifier found.** A Q3 pass here is the absence of found disqualifiers, not a finding that the
  managers are honest [E5-17]; the one live allegation (internal-control statements) survives a motion to dismiss and is unresolved.

### STEP 2 - THE FLAGS **[E4-22, E5-15, E4-29]**, each a prompt to read
- [x] **Weak accounting [E4-22, first flag]**: material weaknesses in internal control in **every annual report from FY2023 to FY2025
  and in every 10-Q of 2026**, the current one reaching *"substantially all accounts and disclosures"*; they *"resulted in the revision of
  the consolidated financial statements as of and for the periods ended September 30, 2022, December 31, 2022, March 31, 2023, June 30,
  2023, and immaterial errors in various accounts during the interim and annual periods during 2023, 2024, 2025, Q1 2026 and Q2 2026"*
  (Q2 2026 10-Q Item 4). Three late-filing notices (NT 10-Q 2023-11-15, for *"immaterial accounting errors related to historical financing
  transactions"*; NT 10-K 2024-03-01; NT 10-K 2025-03-04, citing the SYNQ3 and Amelia acquisitions and the continuing weaknesses). The
  adverse ICFR conclusion runs three years; the Interactions subsidiary (14% of FY2025 revenue) was excluded from the FY2025 assessment.
  *"There is seldom just one cockroach in the kitchen."* Beside it, the revenue booked before it is billed (Q1: $82.9M of contract
  assets and unbilled receivables, 41% of trailing revenue) is the kind of estimate-driven balance [E2-50] tells a reader to weigh
  heavier when the controls over it are rated ineffective.
- [ ] Unintelligible footnotes: not fired; the earn-out, holdback and escrow notes are long but legible.
- [x] **Trumpeted projections [E4-22, third flag; E3-48]**: from August 2022 to August 2024 every release led with a *"cumulative
  bookings backlog"*, then a *"Cumulative subscriptions & bookings backlog customer metric"*: $283M (Q2 2022), $332M (FY2022), **$661M
  (FY2023)**, $723M (Q2 2024). The same dates' GAAP remaining performance obligations were **$20.7M (FY2022) and $12.7M (FY2023)**, 26 and
  52 times smaller. The release footnote says what the difference was: *"Subscriptions backlog refers to potential revenue achievable for
  the company with current customers where the company is the leading or exclusive provider, and assuming a 4-year ramp up during which
  time our technologies are being implemented and assuming a successful full roll out of our technologies"* (EX-99.1 of 2024-08-08). The
  metric vanished from the releases from Q3 2024 on without a stated reason. Now: *"Combined company expects a $500M revenue
  opportunity"* and *"2027 revenue range expected to be, at minimum, $350M-$400M"* (EX-99.1 of 2026-05-07), for a combination whose
  acquired half its own seller projected to shrink (LivePerson's projections in the S-4 imply CY2026 revenue of about $204M and CY2027 of
  about $184M, against $243.7M in FY2025, from the fairness opinion's multiples). **The guidance record [E3-48], set against outturn:**
  revenue guidance was met in every year (FY2022 $28-32M, outturn $31.1M; FY2023 $43-50M, $45.9M; FY2024 raised after Amelia to $82-85M,
  $84.7M; FY2025 $165-180M, $168.9M), the acquisitions carrying FY2024-25. **The profit promises were missed**: *"the Company expects to
  become adjusted EBITDA positive in the fourth quarter of 2023"* (EX-99.1 of 2023-03-07, repeated 2023-08-08 and 2023-11-09), outturn
  *"Adjusted EBITDA (non-GAAP) was ($3.7) million"*; and for 2025, *"revenue exceeding $100 million in revenue and achieve positive
  adjusted EBITDA"* (EX-99.1 of 2024-02-29), outturn *"Full year adjusted EBITDA was a loss of ($58.4) million"*.
- [x] **Discarded yardsticks [E2-49]**: the 2025 positive-adjusted-EBITDA target appears in the release of 2024-02-29 and in no later
  earnings release (EX-99.1 of every Item 2.02 8-K to 2026-08-05 searched for "positive", "break-even" and "profitab": no
  target; the outlook paragraphs speak of revenue only; call transcripts were not read), while adjusted EBITDA stayed negative. **Fires**:
  *"disposition of the yardstick rather than disposition of the manager"*. The backlog metric's withdrawal is recorded beside it but did
  not follow a deterioration in its own reading (it was still rising at $723M), so it is carried as the projections flag, not this one.
- [x] **Serial share issuance [E5-15]**: common shares 200.0M (FY2022), 254.4M (FY2023), 393.6M (FY2024), 422.6M (FY2025), 444.1M (the
  August 2026 cover) and about 485M after the LivePerson closing: **about 2.4 times in under four years**, through ELOC and three ATM
  programmes ($201.5M at $14.48 in 2025; a new $300M programme from May 2026), stock consideration for SYNQ3, Amelia and the Amelia
  earn-out, and 36.9M shares for LivePerson's creditors.
- [x] **EBITDA promotion [E4-29]**: adjusted EBITDA in every release since August 2022; non-GAAP gross margin 58.0% against GAAP 42.4%
  (FY2025); the annual bonus pays 25% on adjusted EBITDA (DEF 14A 2026).
- [ ] Filed-figure fraud tells [E4-30]: smoothness not present (the series is lumpy); cash taxes against pretax income not meaningful on
  losses. Not fired.
- **The flags converge [E4-52]**: weak controls, a backlog built partly of *"potential revenue achievable"*, missed and then dropped
  profit targets, adjusted-EBITDA promotion and serial issuance run toward one outcome, a quote sustained by promises while the share
  count more than doubled. Read as one system, not a sum. **None is a venality finding [E5-38]**; the binary above stands.

### STEP 3 - THE PRIMARY TEST [E2-01], balance sheet first
Return on equity capital employed: stockholders' equity was **negative** at FY2021 (-$343.2M) and FY2022 (-$36.6M) (redeemable
preferred and losses), then $28.2M, $182.7M and $463.8M (FY2023-25), built by issuance, not retention (accumulated deficit $957.1M at
FY2025, $1,024.9M at 2026-06-30). Earnings on it before the earn-out mark were negative every year (Q1 table). **The primary test
fails in every year; there is no year of positive earnings on capital to judge.** On [E2-43]'s unleveraged net tangible assets the
denominator is itself negative from FY2024 (goodwill and intangibles $303.7M against equity of $463.8M less cash of $248.5M).

**The half-owner test [E2-26]:** the FY2025 release headline is *"Record Annual Revenue of $169 Million, Up Nearly 100%"*; the 10-K's
own pro forma shows the owned businesses shrinking, and no release read says so. **Against that, a candor point [E2-69]:** every
release since the earn-out gains began states the mark and excludes it from the non-GAAP line (*"GAAP results include a gain from the
calculated fair value of contingent acquisition liabilities ... Non-GAAP measures exclude this non-operating/non-cash impact"*), and the
FY2025 net loss is not presented as a profit.

**The institutional imperative [E2-30]:**
- [ ] resists change: the reverse; the company changes direction often (Q1).
- [x] **acquisitions materialise to soak up available funds**: SYNQ3, an immaterial buy, Amelia, Interactions, the MIPA target, a $5M
  preferred stake and LivePerson in thirty-two months, while operating cash was negative in every period.
- [ ] staff studies: not observable from the filings.
- [x] **peer behaviour imitated**: the relabelling to *"agentic AI"* across the 2025-26 releases tracks the industry's vocabulary; a
  prompt, weakly held.

**Capital allocation.** No buybacks and no dividends, so [E5-08] does not arise. **Stock deals run the same law [E5-44]:** *"The
intrinsic value of the shares you give in an acquisition must not be greater than the intrinsic value of the business you receive."*
For LivePerson, SoundHound gave 36,894,839 shares (worth $261.2M on the agreement's terms) to the holders of **$373.7M face of secured
notes** (S-4 pro forma note (c)) plus about 5M shares and cash to LivePerson's stockholders, for a business with revenue down 53% since
FY2022, five-year owner cash of -26.3% of revenue, a *"non-renewal by a large LivePerson customer"* and first-quarter 2026 attrition
*"at levels higher than were forecasted"* disclosed in diligence (S-4, Background of the Mergers). What that business is worth, and
what SoundHound's shares are worth, are both unestablished here (Q5 finds no positive value range); the flag is that the price was
set by the creditors' claim, and the buyer's paper was the currency. **The ATM sales at $14.48 in 2025** were issuance at a high quote,
the direction [E5-24] favours for a seller of stock, stated in fairness.
**Insiders:** Rule 10b5-1 plans adopted by the CEO (up to 2,400,000 Class B plus RSU shares), the CSO (up to 2,400,000 Class B) and the
co-founder serving as interim CFO (750,000 Class B) (Q2 2026 10-Q Item 5): selling, not buying. **What pay vests on [E4-27]:** the 2022 executive PSUs vest 25%
on $100M of trailing GAAP revenue, 25% on trailing cash-flow break-even, and **50% on a 90-day average share price of $15 and $20**
(DEF 14A 2026) [E3-50, stock-price targeting]; the FY2025 bonus paid 100% on revenue (met with acquired revenue) and 0% on adjusted
EBITDA. Pay rewarded buying revenue and a higher quote.

**THE GUARDRAIL**
- [x] Nothing in this Q3 promotes the name; Q2 has already closed it [E2-37, E2-38, E3-39].
- [x] Key-person dependence recorded at Q2 [E4-23], not here.
- [x] A great manager is not the reason to act; the manager is the plan here (a sequence of acquisitions and a new platform), which is
  the [E2-36] Pygmalion case, not an excisable cancer.

- **VERDICT (recorded, not governing): [x] IN on the binary** (no integrity disqualifier found; the class action pending) **with
  converging flags [E4-52]**: weak accounting three years running, trumpeted backlog and projections, missed and dropped profit targets
  [E2-49], adjusted-EBITDA promotion, serial issuance, stock-price-linked pay, and a stock-paid acquisition priced by its creditors.
  *IN = no disqualifier found, not a finding that the managers are honest [E5-17]. IN never promotes.*

## Q4 - WILL IT SURVIVE? *(recorded, not governing: the file closed at Q2)*

### Owner earnings **[E2-23]** - from the filed cash-flow faces (`oe.py`, output `oe_out.txt`), $M
*CONVENTION (v4 section VI): operating cash flow less stock compensation, less the (c) guess.* Operating cash already nets the
working-capital increment, including the contract-asset build of the licensing model (-$22.4M in FY2025, -$16.9M in H1 2026), which
this business requires as it books licences before billing them. **The earn-out marks are non-cash and sit in the reconciliation, not
in operating cash** (FY2025 cash-flow face: *"Change in fair value of contingent acquisition liabilities | ( 163,127 ) | 222,670"*),
so they neither help nor hurt the figures below; the earn-outs settled in shares (8,126,674 Amelia shares in July 2026, 246,761 SYNQ3
shares in March 2026) are acquisition consideration, carried at Q3 [E5-15] and in the share count, not in owner earnings.

| year | OCF | SBC (add-back + capitalised) | (c) capex end: PP&E + capitalised software + finance-lease principal | (c) D&A end | **OE, capex end** | **OE, D&A end** |
|---|---:|---:|---:|---:|---:|---:|
| FY2021 | (66.2) | 6.3 | 3.2 | 5.5 | **(75.7)** | **(78.0)** |
| FY2022 | (94.0) | 28.8 | 2.6 | 4.0 | **(125.4)** | **(126.8)** |
| FY2023 | (68.3) | 27.9 | 0.6 | 2.3 | **(96.7)** | **(98.5)** |
| FY2024 | (108.9) | 33.1 | 0.8 | 16.1 | **(142.8)** | **(158.1)** |
| FY2025 | (98.2) | 83.1 | 5.1 | 34.1 | **(186.3)** | **(215.4)** |
| H1 2026 | (60.0) | 41.1 | 6.4 | 21.1 | (107.4) | (122.1) |
| TTM to 2026-06-30 | (114.5) | 82.9 | 11.1 | 39.7 | **(208.5)** | **(237.0)** |

- **Five-year mean (FY2021-25, the default [E2-42]):** **-$125.4M (capex end) to -$135.4M (D&A end).**
- **Four-year (FY2022-25):** -$137.8M to -$149.7M. **Three-year (FY2023-25):** -$142.0M to -$157.3M. **TTM:** -$208.5M to -$237.0M.
- **Ten-year:** not filed; Legacy SoundHound was private before the 2022 merger and its FY2019-20 statements sit in the 2022 S-4, not
  pulled (a limit, and it cannot change a sign that every filed year shares).
- **Spread and its meaning [E4-25, E5-11]:** every window and both ends are negative, and the figure worsens as the window shortens:
  the business consumes more each year, not less. **The range is not too wide to conclude; it is wholly below zero, so the verdict is
  not UNKNOWABLE.** The distorted years are the acquisition years (FY2024 SYNQ3 and Amelia, FY2025 Interactions), and they make the
  recent windows larger in size, not different in sign.
- **(c) as a disclosed judgment [E3-44, E2-41, E5-20]:** the capex end (PP&E, capitalised software and finance-lease principal, $0.6M
  to $11.1M a year) is the physical renewal a software company needs; the D&A end is **mostly amortisation of bought intangibles**
  ($33.0M of FY2025's $34.1M, 10-K Item 7), which measures the cost of the acquired technology and customer lists being used up. Given
  Q2's finding that the basis is replaced by purchase [E4-04], the D&A end is the more honest guess here, not the conservative
  extreme. Neither end changes the sign. **The screen's defect, measured:** companyfacts' FY2021 operating cash is the SPAC shell's
  -$0.864M (Step 0), which is why the `a8bc84f` five-year figures (-$110.2M capex end, -$121.8M D&A end) are smaller in magnitude than
  the -$125.4M and -$135.4M rebuilt here from the filed faces.
- **Stock compensation subtracted in full [E5-06]**, and it is the larger measure that matters [E3-70]: RSUs granted in FY2025 were
  13,628,889 at a weighted grant-date fair value of $12.34, **about $168.2M of grant value against an $83.1M charge** (FY2025 10-K,
  RSU activity table); FY2024 14,009,111 at $4.14, about $58.0M against $33.1M. At grant value the FY2025 owner earnings would be about **-$271M
  (capex end)**. Stock pay was **47.7% of FY2025 revenue** on the charge alone. The earn-out shares for acquisitions are not stock pay
  and are not added; the SYNQ3 restricted stock awarded to continuing employees (2,033,156 shares) is, and sits inside the charge.
- *If the capex band changed the verdict it would be UNKNOWABLE; it does not.*

### Great, good, or gruesome? **[E4-20]**
- [x] **gruesome**: *"grows rapidly, requires significant capital to engender the growth, and then earns little or no money"*. Reported
  revenue grew eight-fold in four years; the growth required about $915M of equity cash raised since the 2022 merger (financing faces:
  SPAC and PIPE $90.7M, preferred $24.9M, ELOC $71.6M, ATM programmes $12.4M, $407.3M, $201.5M and $48.5M, option and ESPP proceeds),
  plus $101.6M of stock and earn-out consideration for SYNQ3 and Amelia at acquisition-date fair value (FY2024 non-cash face:
  $33,606 thousand and $67,945 thousand) and 36.9M shares for LivePerson's creditors; and owner earnings are more
  negative now than when it was a quarter of the size. [E4-43]'s *good* class does not apply: there is no return on the added capital
  to call attractive.

### Staying power **[E5-11]** - scored on the worst case [E2-55]
- **(1) A large and reliable stream of earnings: NO.** Negative in every filed year and window.
- **(2) Massive liquid assets: NO, a runway.** Cash $202.8M at 2026-06-30 (Q2 10-Q), against cash consumed (operating cash plus
  (c) capex end) of $125.6M in the trailing twelve months, before LivePerson's own FY2025 operating cash of -$30.4M (its 10-K, via
  companyfacts) and before the July payments ($5.0M preferred stake, the MIPA balance) and the closing cash paid to LivePerson's
  noteholders ($5.8M) and Tel Aviv holders (up to $7.5M). LivePerson was to bring a closing cash target of $74M less its 2026
  convertible-note repurchase and transaction costs (S-4, Background); the amount delivered is not yet filed. **About one and a half
  years of runway at the filed burn, before any integration cost.**
- **(3) No significant near-term cash requirements: NOT MET, in the company's own liquidity plan**: *"We believe we will meet
  longer-term expected future cash requirements and obligations through a combination of cash flows from operating activities, available
  cash balances and expected cash proceeds from future use of our ATM program"* (Q2 2026 10-Q MD&A). **The plan names new shareholders as
  a source**: [E5-39]'s *"the kindness of strangers"*. Beside it: the Interactions earn-out of up to $25.0M in cash (2026-27), a $64.0M
  cloud commitment after 2026 (FY2025 10-K), and the LivePerson integration.
- **Leverage, named and quantified [E4-16, E3-29]:** no funded debt after the closing (the company says *"a strong, debt-free balance
  sheet"*, EX-99.1 of 2026-09-04, and the filings support it); **the leverage is operating, not financial.** [E2-54]'s coverage test has
  no interest to cover; its spirit, cash flow *"net of ample capital expenditures"*, is negative.

### The specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **The mechanism: shape #8, THE EQUITY IS THE REVENUE** (RGTI, 2026-09-13): customers pay a part of the costs and new shareholders pay
  the rest. Revenue of $203.2M in the twelve months to June 2026 against about $404M of operating costs before the earn-out mark (an
  operating loss of about $200.8M: FY2025's -$186.4M, less H1 2025's -$94.7M, plus H1 2026's -$109.1M); the gap has been
  filled every year by selling stock, and the company's liquidity plan says it will be again. **With #2, EARNS NOTHING FOR OWNERS AFTER
  PAYING ITS PEOPLE, as a feature** (stock pay 47.7% of FY2025 revenue on the charge; grant value about twice the charge).
  **And a proposed new shape, #21 THE ROLL-UP** *(proposed, pending the operator)*: the reported growth is bought with the acquirer's
  own shares from the owners and creditors of shrinking businesses (LivePerson revenue -53% FY2022-25; the filer's pro forma for its
  own perimeter -6.6% and -6.1% in FY2024 and FY2025), while the businesses owned throughout shrink; it lasts as long as the quote will
  buy the next one, and the earn-outs and creditor settlements are paid in the same currency. It is argued separately from #8 because
  #8 describes how the losses are funded and #21 how the revenue line is made; and from #10 THE CAMOUFLAGE because there is no strong
  leg whose cash is recycled, only a share price.
- **Quantified from filed figures:** at the TTM cash burn of about $126M plus LivePerson's about $30M, the $202.8M of June 2026 cash
  lasts roughly 15-19 months; replacing it through the $300M ATM at $5.93 would mean about 50M new shares, **about 10% more on the pro
  forma 485M**, and the Amelia 2026 earn-out adds up to 8,695,755 more. The owner dies by dilution before the company dies by
  insolvency, as long as the market will take the stock; if the quote falls far enough that it will not, the company has no other
  stated source.
- **Exposure, not experience [E4-40]:** the benign sign in the recent record (adjusted EBITDA losses narrowing, "debt-free") is experience;
  the exposure is a business whose own filing says its function can be given away free by larger rivals, with one and a half years of
  cash and a funding plan that depends on its share price.
- **Likelihood:** further dilution to fund losses: **likely** (the plan says so). Insolvency: **a low-level possibility** while the ATM
  and the cash last.
- **VERDICT (recorded, not governing): [x] OUT** - owner earnings negative in every window and at both ends of (c): **-$125.4M to
  -$135.4M (five-year), -$142.0M to -$157.3M (three-year), -$208.5M to -$237.0M (TTM)**; gruesome [E4-20]; none of [E5-11]'s three
  strengths; shape #8 with #2 as a feature, and #21 THE ROLL-UP proposed.

---
⛔ **Q5 did not open as a clearance: Q2 is OUT (and Q4, recorded, is OUT).** What follows is arithmetic for the record.

## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? *(COMPUTATION — NOT A CLEARANCE)*

### COMPUTATION — NOT A CLEARANCE
*Headed as operator rule 3 requires. No entry language; no band; no ranking.*

**THE FLOOR FIRST [E4-28].** The honest pre-tax expectancy at this price cannot be stated as a positive number: owner earnings are
negative in every window. The name is not ranked; under the floor it would be quit on even if Q1-Q4 had cleared.

**1. THE YIELD** (`oe_out.txt`), at US$5.93 (2026-09-18 close, aggregator flagged):

| cap basis | cap | five-year (capex end / D&A end) | three-year | TTM |
|---|---:|---|---|---|
| cover, 444,109,844 shares (10-Q `0001840856-26-000022`) | $2,633.6M | **-4.8% / -5.1%** | -5.4% / -6.0% | -7.9% / -9.0% |
| pro forma after the LivePerson closing, about 484.0M-486.8M shares | about $2,870-2,887M | **-4.3% to -4.4% / -4.7%** | -4.9% / -5.5% | -7.2% to -7.3% / -8.2% to -8.3% |

Against the sovereign **5.34%** (US Treasury 30-year, 09/18/2026) and the ~10% floor. **Neither cap basis includes LivePerson's
owner earnings**, which were negative (-$511.7M of five-year owner cash on $1,942.6M of revenue, the competitor row), so the pro forma
yield flatters the combination: the denominator carries the new shares, the numerator does not yet carry the business they bought.

**2. WHAT THE PRICE ALREADY ASSUMES.** The floor needs owner earnings of about **+$287M a year** on the pro forma cap (+$263M on the
cover cap), against **-$125M (five-year) to -$237M (TTM)**: a swing of roughly $410-525M a year. Year-1 growth needed from a negative
base is **not a number** (the MRVL rule, RESUME STATE item 3D). In words: the quote assumes that a business which has consumed cash in
every filed year turns, within a few years, into one earning more than its whole FY2025 revenue in owner earnings. The corpus's base
rate for sustained high growth among the best businesses is *"fewer than 10 of the 200 most profitable companies"* **[E4-35]**, and this
is not among the profitable.

**3. WHAT YOU ARE PAID.** About **-9.6 to -13.6 points under the sovereign** on the pro forma cap, five-year to TTM (-10.1 to -14.3 on the cover
cap); below the floor by more.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:** on the filed owner earnings the range lies **wholly below zero**; the price of $5.93
(about $2.9bn pro forma) is above the whole range. **What bounds the upside [E2-63]:** the filer's own 2027 target (*"at minimum,
$350M-$400M"* of revenue) carries no profit figure, and no filed document states an owner-earnings level.

**Bar used:** neither applies; there is nothing to apply a margin to and no conservative case above zero to screen. **Windage count:**
zero; the (c) band is displayed, not stacked.

- **VERDICT: not reached** (the file closed at Q2). Computation recorded: price above a value range that lies wholly below zero.

## Q6 - WHAT WOULD PROVE ME WRONG? *(recorded; reversal condition in words, no band)*

**No alert band is armed and no PORTFOLIO row is added.** A Q2 OUT is a finding about the business, and a price alert on it would be a
category error (the QLYS ruling, 2026-09-07).

**The reversal condition, pre-committed in words [E1-02]:** reopen Q2 only if **all** of the following appear in filed documents:
1. **Like-for-like revenue grows**: the filer's own pro forma (or organic disclosure) shows the businesses owned throughout growing in
   two consecutive annual reports, with LivePerson included.
2. **Pricing turns**: a filed price increase that holds, or the disappearance of the *"annual price reduction commitments"* and *"free of
   charge"* language from Item 1A, with gross margin before acquired amortisation rising for two years.
3. **Contracted revenue rises with reported revenue**: GAAP remaining performance obligations growing faster than revenue for four
   consecutive quarters, and contract assets plus unbilled receivables falling as a share of trailing revenue.
4. **Owner earnings turn positive**: operating cash less stock compensation (at the larger of charge and grant value [E3-70]) less
   capitalised software and capex, positive for a full year, with no ATM sales in that year.
5. **The control environment is clean**: an unqualified ICFR opinion with no material weakness for two consecutive years.
6. **The row moves**: SoundHound's five-year owner cash per revenue dollar at or above Cerence's and Five9's on the same basis.

**Thesis-breaking signals that would harden the OUT, if a later reader reopens:** an ATM draw or new equity raise to fund operations;
another stock-paid acquisition of a shrinking business; RPO below $60.0M; a restatement (Item 4.02) rather than revisions.

- **VERDICT (recorded): not reached.** Next dated evidence: the Q3 2026 10-Q (due about November 2026), the first to carry
  LivePerson, the post-closing share count, the delivered LivePerson cash and the Amelia 2026 earn-out assessment.

---
## SELF-AUDIT
- [x] Questions answered in order; the file stopped at Q2 (OUT) and Q3-Q6 are labelled recorded, not governing.
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1 IN rests on the filed faces; Q3's IN is the binary only).
- [x] No UNRESEARCHED verdict. The unfiled items (the exact LivePerson merger-share count, the cash LivePerson delivered) are named with
      the document that will carry them (the Q3 2026 10-Q) and neither can change the Q2 finding.
- [x] No UNKNOWABLE verdict; the case for it at Q1 is recorded and the reason it was not taken is stated; at Q4 every window is negative.
- [x] Step 0: the filing was read (10-K FY2025 `0001840856-26-000006`, 10-Q Q2 2026 `0001840856-26-000022`, and the others listed), and
      FY2025 operating cash and stock compensation were cross-checked against the filed face (identical to companyfacts); the FY2021
      operating cash was found NOT to match (companyfacts carries the SPAC shell's) and the filed face was used.
- [x] Owner earnings on multi-year means (five-year default, four, three, twelve months), both (c) ends shown, (c) disclosed as a
      judgment; the ten-year window is named as not filed.
- [x] Competitor row filled: four filers (Cerence, LivePerson, Five9, NICE), same metrics and window, from their filed annual statements
      as transcribed, one Cerence figure checked to its face; the unsegmented and non-SEC rivals named and the reason they are absent
      stated.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/18/2026, struck by this run.
- [x] Value stated as a range: none positive on any window; not a point estimate.
- [x] One bar only, and neither applied (nothing above zero to screen); windage count zero.
- [x] Price dated (2026-09-18 close), aggregator flagged, corroborated at the LivePerson closing terms (implied VWAP about $7.08 against
      Yahoo's late-August closes).
- [x] Share classes summed only after the charter was read (one-for-one conversion, ratable dividends and liquidation); the cover count
      and the post-closing pro forma both shown.
- [x] SBC resolved and complete: the add-back plus the SBC capitalised into software; the grant-value measure [E3-70] computed from the
      RSU table; earn-out shares identified as acquisition consideration, not pay.
- [x] Deal read (ROKU lesson): SoundHound the acquirer, the LivePerson deal closed 2026-09-04, no offer for SOUN; ATM programmes and
      the absence of convertibles recorded.
- [x] Every ledger id cited was checked against `principle_ledger.csv` (one row each).
- [x] Run committed to git (template `e1a6ce1`, Step 0 `74456b3`, Q1-Q2 `42d9d26`, Q3-Q6 with audit and register in the commit that
      carries this line; the fold in the fold commit).
- [x] No em dashes written by this run (the required heading and verbatim quotations keep theirs).

### CORRECTIONS MADE BEFORE CLOSE (my own errors, caught before commit of the section that carried them)
1. **A stale revision in my own table**: the Q1 draft summed FY2022 R&D, S&M and G&A to $127.0M using the first-filed G&A; the
   revised figure (FY2023 10-K, $30,443 thousand) gives $127.2M.
2. **An unsourced label**: the Q1 draft called Customer C (49% of FY2023 revenue) "one carmaker". No filing names it; removed.
3. **Two misquotations at Q2**: [E2-45] was quoted as *"with ample capital and skilled personnel"*, which is not a substring of the
   row (*"assuming I had ample capital and skilled personnel"*); and *"basis must be periodically replaced"* was put in [E4-04]'s mouth,
   when it is v4's scoping sentence. Both corrected to the exact text and the right source.
4. **Two counts at Q2**: "four acquisitions in twenty months" (it is five since January 2024, and 32 months to LivePerson), and
   "$36.9M of shares" for what is 36,894,839 shares.
5. **Two people at Q3**: the class action names the CFO of the time (Sharan, who resigned in 2026), not a "former CFO"; the insider with
   the 750,000-share plan is the co-founder serving as interim CFO, not merely "a director".
6. **Two figures at Q4**: "about $134M of stock consideration" for SYNQ3 and Amelia was not a figure I had computed; replaced by the
   filed $101.6M ($33,606 thousand plus $67,945 thousand, FY2024 non-cash face). "About $330M of costs" was wrong; the trailing
   operating loss before the earn-out mark is about $200.8M, so costs were about $404M.
7. **A scope claim at Q3**: "in no later release read" was widened into what was actually searched (every Item 2.02 EX-99.1 to
   2026-08-05, three search terms) and what was not (call transcripts).
8. **A tooling error of my own**: the first `peers/peer_row.py` took the first revenue tag with any data, which for LivePerson is
   `Revenues` ending in 2018, and printed nothing; corrected to merge tags year by year.
9. **A points-over-sovereign range at Q5** mixed the pro forma and cover caps (-9.6 to -14.3); split into -9.6 to -13.6 (pro forma)
   and -10.1 to -14.3 (cover).

### THE BRIEF'S DEFECTS (every brief in this queue has had at least one)
1. **"Name the peers from SOUN's own 10-K competition section"**: the 10-K has no such section and names no competitor (Item 1 speaks
   of unnamed *"big tech"* and *"legacy vendors"*; a search for every name in Cerence's list returned none). Peers were taken from
   Cerence's 10-K, which names SoundHound, and from the LivePerson fairness opinion.
2. **The brief did not mention the LivePerson acquisition**, the largest in the company's history, **closed on 2026-09-04, after the
   latest cover date**, with 36,894,839 shares issued to LivePerson's creditors and 3.0-5.8M to its stockholders. "SOUN has made
   acquisitions" and "check for any pending merger" pointed at the right place, but the cover-count instruction, followed literally,
   would have understated the count by about 8%. The deal-form alert (seven 425/S-4 filings) was about SoundHound as the acquirer,
   not a spread on its own quote.
3. **Hypothesis (a) was right and incomplete**: the SPAC shell left a second stale fact, **FY2021 operating cash of -$0.864M**, inside the
   owner-earnings series the triage used, not only a stale share count. The brief's instinct (check shell-era facts) found both.
4. **The prior the brief flagged as most likely wrong** (that a loss-making, acquisitive, heavily stock-paid AI company is an easy
   close) was **half right**: the close came at Q2, on the filer's own words about free alternatives and price reductions, not at Q4 on
   the losses; and it was not free, because the franchise case had real evidence (design-win stickiness in the filer's words, a named
   rival conceding SoundHound wins business, multi-year renewals, revenue guidance met every year) that had to be argued down on
   criterion 2 rather than waved away.
5. The ledger ids in the brief were all verified present; the brief's register count of 115 was checked by counting (fold).

### LIMITS OF THIS RUN
- **The post-closing share count is a range** (484.0-486.8M): the merger shares to LivePerson's stockholders are not filed; the Q3 2026
  10-Q will carry the count. **The cash LivePerson delivered at closing is not filed.**
- Earnings-call transcripts and investor decks were not read; a spoken profit target, or a spoken withdrawal, would be there.
- The ten-year window is not available from periodic filings; the 2022 S-4's FY2019-20 Legacy statements were not pulled.
- The competitor row uses companyfacts transcriptions of the peers' filed statements with one figure checked to a face; Verint's
  facts stop at FY2024 and it was not used; the big-technology rivals are unsegmented and iFlyTek is not an SEC registrant.
- No unit series (devices, queries, locations) is filed, so [E4-55] could only be run on dollars.
- The [E3-70] grant value uses the RSU table only (options and PSUs are small against 13.6M RSUs granted in FY2025).
- The *Liles* mediation of 2026-08-25 has no filed outcome.
- The watchlist pricing script that wrote the triage row is not on disk (the HBB finding); the triage inputs are reconstructed.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business), at Q2** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** SoundHound licenses voice AI to device makers and runs hosted voice and chat agents for businesses; its own 10-K says
  its products face alternatives *"offered at significantly lower costs or free of charge"* from larger rivals and accepts *"annual
  price reduction commitments"*; reported revenue doubled by acquisition while the filer's own pro forma for the businesses it owned
  fell; RPO fell to $60.0M; it is last on every margin and cash column of a five-filer row. The file closes at Q2 on [E3-03]
  criterion 2. Recorded, not governing: Q3 IN on the binary with converging flags (material weaknesses three years running, a
  "backlog" of *"potential revenue achievable"* 52 times GAAP RPO, missed and dropped adjusted-EBITDA targets, serial issuance to about
  2.4x, stock-price-linked pay); Q4 OUT, gruesome, owner earnings -$125.4M to -$135.4M (five-year) and -$208.5M to -$237.0M (TTM),
  shape #8 with #2 as a feature and #21 THE ROLL-UP proposed; price US$5.93 x 444,109,844 = US$2,633.6M on the cover (about
  US$2.87-2.89bn after the LivePerson closing), headed COMPUTATION — NOT A CLEARANCE, above a value range that lies wholly below zero.
  **FAIL at Q2.**

