# Company Run — Brookfield Asset Management Ltd. (BAM) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Write-early protocol: this file was created before any fetch. Sections are appended as they
close. Research files: `Test Runs/_research 2026-09-13 BAM/`.*

**PRIORS, recorded before any filing was opened [E4-26]** — to be refuted, not confirmed:
1. The brief's prior: the perimeter is answerable from BAM's 10-K because BAM is the fee business
   and the funds are largely off its balance sheet, so the run reaches a real verdict rather than
   closing on measurement. A prior about measurability, not a verdict.
2. The queue's 2026-09-02 note: BAM and BN are a "different perimeter problem, closer to the
   DKS/HON class than to the insurer class", and were BLOCKED. A scheduling note, to be tested.
3. My own prior: BAM holds 100% of the asset manager only since a 2025 reorganisation, with BN
   keeping most of the carried interest on pre-2022 funds; the filed history under this CIK is
   therefore a slice before 2025 and the whole after. Unverified until the filings are read.
4. My own prior: the share count on the cover understates the economic count, or BN's holding is
   outside the float but inside the count. Unverified.


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
- rate **5.35%** · date **2026-09-11** (latest print; 09-12 and 09-13 are a weekend) · source
  **US Treasury daily par yield curve, 30-year** (issuing authority), struck fresh through
  `tools/sources.py:sovereign("USD")` on 2026-09-13. It agrees with the brief's figure; it was
  not inherited from it.
- **RE-STRUCK 2026-09-13, at the resume of this run** (the session that wrote Step 0 was killed
  at 01:44): `python tools/sources.py` returns **USD 5.35% at 09/11/2026, US Treasury daily par
  yield curve**. **Unchanged.** Recorded as a dated confirmation rather than an overwrite. (JPY
  4.00% at 2026-09-10, also from the issuing authority; the EUR leg failed on an SSL certificate
  verification error and is not needed — the earnings currency is USD.)
- **Earnings currency USD, established from the filing.** Reporting currency USD (10-K FY2025,
  "presented in U.S. dollars"). Item 7A: *"a majority of our private funds are denominated in USD.
  This means that a majority of the Fee Revenues that we earn are paid in USD, irrespective of the
  local currency of our underlying investment base. Additionally, the majority of our revenues are
  earned in the U.S."* FY2025 management and advisory fees by geography (MD&A): United States
  $2,551M, United Kingdom $943M, Canada $764M, Other $668M, plus $561M of incentive distributions
  from BIP/BEP/BBU. The 8-K of 2026-08-14 (`0001104659-26-097349`): 49% of AUM and ~50% of LTM
  capital raised are US-sourced. **The non-US legs are real (UK 17%, Canada 14% of management
  fees) and are disclosed, not blended; the reporting-currency sovereign is used, per the WTM open
  question (SECTOR METHOD, Finding 8).**
- FX: none needed — the NYSE line is USD. **Jurisdiction [E3-66]:** a British Columbia
  corporation, head office New York, co-listed TSX. Dividends to a US holder carry Canadian
  withholding tax at 25%, reduced to 15% under the Treaty (10-K Item 5). Stated, not priced.

**Price and share count — re-struck, not inherited:**
- Price **$47.26**, 2026-09-11 close (`sources.price("BAM")`, Yahoo chart API — **aggregator,
  flagged, live quote only**). No split after the measurement date (`split_factor_after` = 1.0).
- **Share classes, from the cover and the charter note.** Two classes: **Class A Limited Voting
  Shares** (NYSE/TSX: BAM) and **Class B Limited Voting Shares, 21,280, all held by BAM Partners
  Trust** (10-K Item 5: *"The BAM Partnership is the sole holder of the Class B Shares
  outstanding"*). Both participate in dividends (two-class EPS method; dividends *"Per Class A
  Share and Class B Share"* $1.75 in 2025). Class B is economically trivial (21,280 x $47.26 =
  $1.0M) and is counted.
- **Cover count confirmed: 1,597,230,353 Class A and 21,280 Class B at 2026-08-06**, 10-Q for the
  period ended 2026-06-30, filed 2026-08-10, accession `0001628280-26-054933` (balance sheet:
  1,638,280,619 issued, **1,597,215,738 outstanding**, 41,064,881 in treasury at 2026-06-30).
  **This cover post-dates the Oaktree close of 2026-07-31** and moved only +14,615 shares from the
  June balance sheet.
- **A COVER-DEFINITION BREAK, found by reading both covers.** The 10-K cover (filed 2026-03-02,
  `0001628280-26-013098`) reports **1,638,147,590 Class A at 2026-02-23 — the ISSUED count,
  including ~29.5M+ treasury shares** held by escrowed-stock-plan subsidiaries (balance sheet
  2025-12-31: 1,637,942,656 issued, 1,608,492,642 outstanding). The 10-Q cover reports the
  OUTSTANDING count. BN's 13D/A (`0001104659-26-040030`, 2026-04-06) also computes its percentage
  on the issued 1,638,131,687. **A screen reading the two covers in sequence sees a 40.9M-share
  (2.5%) fall and reads a buyback that is mostly a definition change** (actual net treasury
  acquisitions H1 2026: 11,614,867 shares, $592M, equity statement).
- **BN's holding is INSIDE the count.** **1,193,021,145 Class A shares** held by Brookfield
  Corporation through subsidiaries and by Brookfield Wealth Solutions (BNT) and its subsidiaries
  (13D/A Item 5(a); 10-K Item 12: *"Brookfield Corporation owns or controls approximately 73% of
  BAM, which includes approximately 4% held by subsidiaries of BWS"*). **74.7% of the outstanding
  count** (72.8% of issued). These are economic Class A shares, identical to the float.
  **65,000,000 of them are pledged** under a US$1.0bn RBC margin loan to BWS BAM Financing LP,
  maturing 2028-04-02 (13D/A Item 4).
- **Count used: 1,597,251,633 economic shares** (Class A outstanding 1,597,230,353 + Class B
  21,280). **Cap = $47.26 x 1,597,251,633 = $75,486M.** The public float is ~404M shares
  (~$19.1bn); **a cap computed on the float would understate the company by 75%** — the public-
  float guard's reason for existing. Diluted: weighted-average diluted shares Q2 2026 1,612.5M
  (escrowed stock and options, +14.9M), cap ~$76.2bn.

**The filing was read** — not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **10-K FY2025**, filed 2026-03-02, accession `0001628280-26-013098` (Items 1, 5, 7 incl. Key
  Measures, Fee-Bearing Capital, DE and the GAAP-to-non-GAAP reconciliation, Liquidity,
  Contractual Obligations; Item 7A; Item 8 statements; Notes 1-2 (organization, tracking shares,
  consolidation, revenue); the auditor's report incl. both critical audit matters; Items 11-13).
- **10-Q Q2 2026**, filed 2026-08-10, `0001628280-26-054933` (statements; equity statements;
  Note 17 subsequent events; FBC and DE tables; share repurchases).
- **10-K FY2024**, filed 2025-03-17, `0001937926-25-000007` — **the first 10-K under this CIK,
  not the 10-K of 2026-03-02 as the brief's pre-check said** (it followed an NT 10-K of
  2025-03-03) — and its **EX-99.1** (audited consolidated and combined statements of **Brookfield
  Asset Management ULC**, FY2022-FY2024) and **EX-99.2** (audited combined statements of the
  **Oaktree Asset Management Operating Group**, FY2022-FY2024). 10-K FY2025 **EX-99.1** fetched.
- **8-K 2025-02-05** (`0001104659-25-009249`, Items 1.01, 2.01, 3.02, 3.03, 5.01, 5.03, 5.07,
  7.01) and EX-99.1 — the 2025 Arrangement. **8-K 2026-08-03** (`0001104659-26-089471`, Item 2.01)
  and EX-99.1 — the Oaktree close. **8-K 2026-04-17** (`0001104659-26-044893`, Items 1.01/2.03).
  **8-K 2026-09-08** (`0001171843-26-005900`, Item 8.01) and EX-99.1. **8-K 2026-08-14**
  (`0001104659-26-097349`, Item 7.01). **8-K EX-99.1 Q2 2026 results release**
  (`0001171843-26-005272`). **Schedule 13D/A** 2026-04-06 (`0001104659-26-040030`).
- **Figure cross-checked against the filed statement:** FY2025 cash from operating activities
  **$2,101M** on the 10-K cash-flow statement = companyfacts
  `NetCashProvidedByUsedInOperatingActivities` 2,101,000,000 (accession `0001628280-26-013098`).
  FY2025 stock-based equity awards **$123M** (cash-flow add-back) = `ShareBasedCompensation`
  123,000,000. FY2025 distributions to common stockholders **$2,818M** = `PaymentsOfDividends`
  2,818,000,000. H1 2026 operating cash **$883M** on the 10-Q.

### THE TWO PROMPTS, OPENED
- **`deal_note` (one 8-K Item 1.01 since 2026-03-02, no EX-2.1) — OPENED: a notes offering.**
  8-K 2026-04-17: US$550M 4.832% senior notes due 2031 and US$450M 5.298% notes due 2036 (a
  re-opening of the $400M series), unsecured, lien covenant only, 101% change-of-control offer.
  **Not a merger.** The prompt was right that it is not a merger and **silent on the transaction
  that does change the perimeter** — the Oaktree close was filed under **Item 2.01** (8-K
  2026-08-03). The Oaktree **Transaction Agreement of 2026-04-14 is incorporated by reference as
  Exhibit 2.1 from Brookfield Oaktree Holdings, LLC's 8-K** (10-Q exhibit index), a different
  registrant — which is exactly why this CIK carries no EX-2.1.
- **8-K 2026-09-08 (`0001171843-26-005900`) — OPENED: a press release, Item 8.01.** The UK
  Nuclear Liabilities Fund selected Brookfield's Investment Solutions Group for a multi-asset
  mandate, **initial $1bn commitment**, proceeds *"expected to be reinvested … rather than
  routinely distributed"*. Immaterial to the perimeter (0.15% of $672bn Fee-Bearing Capital); it
  is Q2 evidence of a mandate won *"Following a competitive selection process"*.
- `name_change_note` returned nothing; confirmed — `formerNames` is empty in the submissions index.

### THE PERIMETER, FROM THE FILINGS — every reorganisation, dated
| date | event | what one BAM share owned | source |
|---|---|---|---|
| to 2022-12-09 | the asset management business sits **inside Brookfield Asset Management Inc. (now BN)**; carve-out statements only | no BAM shares exist | ULC EX-99.1 Note 1 (*"combined standalone basis … derived from the consolidated and combined financial statements and accounting records of BN"*) |
| 2022-07-04 | BAM Ltd and Brookfield Asset Management ULC incorporated (British Columbia) | — | 10-K FY2025 Note 1; ULC Note 1 |
| **2022-12-09** | **2022 Arrangement**: BN transfers its asset management business into the ULC and **25% of the ULC to BAM Ltd**, distributed to BN holders; Relationship Agreement (BN: 100% of mature-fund carry, 33.3% of new-fund carry); BUSHI/BMHL tracking shares issued to BN | **~25% (later ~27%) of the ULC**, equity-accounted | ULC EX-99.1 Note 1; 10-K FY2025 Items 1, 13 |
| 2023-2025 | BAM Ltd files a 20-F (FY2022, `0001937926-23-000004`), a 40-F (FY2023, `0001937926-24-000004`), then a 10-K (FY2024) as the ~27% holder | ~27% of the ULC | submissions index |
| **2025-02-04** | **2025 Arrangement**: BAM acquires BN's ~73% of the ULC for **1,194,021,145 new Class A shares**, one-for-one; BN ends at ~73% of BAM; board-election rules amended (A and B vote as one class while BN > 50%); BAM voluntarily moves to 10-K/10-Q/8-K | **100% of the asset manager** (subject to the carry split below) | 8-K `0001104659-25-009249`; 10-K FY2025 Note 1 |
| 2025-10-02 | Angel Oak, 51.3% economic interest, ~$149M cash | + | 10-K FY2025 Item 1 |
| **2026-07-31** | **Oaktree**: Brookfield acquires the remaining ~26% for ~$3.0bn of cash and BN/BAM shares, **~$2.2bn attributable to BAM**; **BAM obtains control** — equity method to that date, consolidated after it | + the Oaktree remainder; BAM's post-step economic share is not stated in the 10-Q | 10-Q Note 17; 8-K `0001104659-26-089471` |

**What the share buys today, from the filings: 100% of Brookfield Asset Management ULC (since
2025-02-04), which keeps 100% of base management fees, advisory fees and incentive distributions,
66.7% of carried interest on new and open-ended funds (BN takes 33.3%) and 0% of carried interest
on mature funds (BN takes 100%, through BUSHI tracking shares)**, plus equity-method stakes in
partner managers (Castlelake 51% of FRE, LCM 49.9%, Primary Wave 44% then +6% on 2026-07-01,
Angel Oak 51.3%, Pretium ~11%) **and, since 2026-07-31, control of Oaktree.** BN also holds BUSHI
preferred shares (class B senior preferred, $1.36375/yr cumulative; class B preferred, 6.7%
non-cumulative; class A preferred) — **$1,238M of preferred shares redeemable NCI at 2026-06-30
ranks ahead of the Class A holder.**

**THE FILED HISTORY OF THE 100% BUSINESS IS LONGER THAN THE CIK, AND SHORTER THAN FIVE YEARS.**
Because the ULC was the accounting acquirer in 2025, the 10-K FY2025 presents **the ULC as
Predecessor**: FY2023, FY2024 and FY2025 are the whole business on one perimeter. **FY2022 exists
(ULC EX-99.1) but is a separation year** — operating cash **−$374M** after a $7,396M due-to-
affiliates settlement and a $5,155M contribution from parent; the statements say they *"may not be
indicative of what they would have been had the Company been an independent standalone entity"*.
**Pre-2022 carve-out statements are in the F-1/424B3 of 2022-11-21 (`0001193125-22-289950`)**, on
costs allocated inside BN.

**COMPANYFACTS SPLICE — A FOURTH MECHANISM, stated so a tool can be fixed.** Under this CIK,
`NetCashProvidedByUsedInOperatingActivities` holds **both entities under the same period keys**:
BAM Ltd as a 27% holder (FY2023 **$508M**, FY2024 **$627M**; accessions `0001937926-24-000004`,
`0001937926-25-000007`) and the ULC-as-Predecessor restatement (FY2023 **$1,439M**, FY2024
**$1,612M**; `0001628280-26-013098`). **`sources.annual()` at its default `vintage="earliest"`
returns {2023: 508, 2024: 627, 2025: 2,101} — a 27% holding company spliced onto the 100%
business, a 3.4x step that is a perimeter change, not growth.** The same split holds for
`ShareBasedCompensation` (6 / 3 against 33 / 103) and `PaymentsOfDividends` (505 / 630 against
2,101 / 2,478). `tools/run.py BAM` (which uses `newest`) returned *"no overlapping OCF/D&A/capex
annual facts. UNRESEARCHED"* — D&A exists only in the newest filing and no capex tag resolves.
**No companyfacts row is used below; every figure is from the filed statements.** Same class as
NEGG's splice and RGTI's colliding de-SPAC keys; a different mechanism — **a predecessor
restatement filed by a registrant that had been the minority holder.**

**THE BLOCK OF 2026-09-02, TESTED.** The queue's note called BAM a *"different perimeter problem,
closer to the DKS/HON class"*. What the filings show: (1) the 2025 perimeter change is **fully
restated** — the Predecessor presentation gives three consistent years of the whole business;
(2) **consolidated funds are small and separately captioned** — BSI II at $505M of investments at
2025-12-31, $3,090M at 2026-06-30, each with its own revenue, expense, borrowing, cash-flow and NCI
lines, so they can be stripped; (3) **BN's carry share is separately captioned** (NCI in
consolidated entities; preferred shares redeemable NCI); (4) Oaktree was equity-accounted, with its
own audited statements filed as exhibits. **The perimeter is MEASURABLE from filings. The block was
a scheduling judgment, not a measurement finding.** Two things the block anticipated are real and
are carried forward: **a five-year window on one perimeter does not exist** (three clean years plus
H1 2026), and **the perimeter moved again on 2026-07-31** when BAM took control of Oaktree, whose
consolidation enters the statements from Q3 2026.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively
> simple and stable in character. If a business is complex or subject to constant change, we're
> not smart enough to predict future cash flows."* **[E3-31]**

**Unit economics in my own words, no management language.**

Pension funds, sovereign funds, insurers and (increasingly) wealthy individuals hand Brookfield
money to own infrastructure, power plants, buildings, companies and loans for them. Brookfield
charges a yearly fee on that money whether the investments do well or not, pays its ~5,800 people
out of the fee, and keeps the rest. That is nearly the whole of the cash. Four fee streams, all
filed (10-K FY2025 MD&A, Distributable Earnings table and Notes 1-2):

| $M | FY2023 | FY2024 | FY2025 | H1 2026 | source |
|---|---|---|---|---|---|
| **Base management fees** (100% basis incl. Oaktree) | 3,956 | 4,233 | 4,896 | 2,625 | DE table |
| Incentive distributions (BIP, BEP) | 378 | 424 | 466 | 258 | DE table |
| Performance fees (BBU, over a high-water mark) | — | — | 95 | 3 | DE table |
| Transaction and advisory fees | 47 | 49 | 30 | 34 | DE table |
| **Fee Revenues** | **4,381** | **4,706** | **5,487** | **2,920** | DE table |
| Direct costs (compensation, operating, G&A; Oaktree at 100%) | (2,014) | (2,136) | (2,410) | (1,296) | DE table |
| **Fee margin before tax** *(computed)* | **54.0%** | **54.6%** | **56.1%** | **55.6%** | |
| Fee-Bearing Capital, year-end ($bn) | 457.0 | 538.5 | 602.7 | 672.2 (06-30) | FBC tables |
| **Base fee rate on average FBC** *(computed)* | **90.4bp** | **85.0bp** | **85.8bp** | **82.4bp** (annualised) | |
| Realized carried interest allocations (GAAP, 100%) | 51 | 25 | **0** | 16 | statement of operations |

*(Fee rate arithmetic: FY2023 3,956 ÷ avg(417.9, 457.0); FY2024 4,233 ÷ avg(457.0, 538.5); FY2025
4,896 ÷ avg(538.5, 602.7); H1 2026 2 x 2,625 ÷ avg(602.7, 672.2). GAAP "base management and advisory
fees" are lower — $2,766M / $2,957M / $3,384M — because GAAP carries Oaktree by the equity method;
the reconciliation (MD&A, "Reconciliation of Revenues to Fee Revenues") adds $1,240M / $1,335M /
$1,569M of "Fee Revenues from equity method investments". **A fee rate computed as GAAP fees over
FBC mixes perimeters: the RMR run of 2026-08-30 printed BAM at 56bp that way ($3,384M ÷ $602.7bn);
on one perimeter it is ~81-86bp.** Recorded as a correction to that row, not an edit of it.)*

1. **The long-term private funds ($297.7bn FBC at 2026-06-30).** Closed-end, *"typically
   committed for 10 years with 2 one-year extension options"*; fees *"typically on committed
   capital or invested capital, depending on the nature of the fund and where the fund is in its
   life"*. When the fund sells assets the capital goes back to the client and the fee on it stops
   — FY2025 distributions took $26.8bn of FBC off the base — so **this stream has to be re-raised
   vintage by vintage** (BIF, BGTF, BCP, BSREP, Oaktree Opportunities). On top sits carried
   interest: 20% of profits over an 8% preferred return, paid late in a fund's life.
2. **Permanent capital and perpetual strategies ($293.5bn FBC).** Two different things share
   this label. **(a) BN's listed affiliates** (BIP, BEP, BBU) and BPG pay a base fee on their
   market capitalisation or NAV under Master Services Agreements that *"cannot be terminated
   without BN's consent"*, plus **incentive distributions** that grow when BIP and BEP raise their
   payouts ($561M in FY2025). **(b) Perpetual private funds, semi-liquid wealth vehicles, and
   BWS insurance capital** — BN's paired insurer: **$108bn of FBC paying $234M of fees in FY2025
   (~22bp)** (MD&A Credit note 2), and the source of $44.8bn of Q2 2026's $52.7bn of credit inflows.
3. **Liquid strategies ($81.0bn FBC)** — listed-securities funds and separate accounts on NAV,
   redeemable.
4. **Carried interest** — **BAM keeps 66.7% on new and open-ended funds and 0% on mature funds**
   (Relationship Agreement, 10-K Item 13). Realized carry reaching the common holder has been
   immaterial in every filed year: GAAP realized allocations $51M, $25M, $0 (FY2023-25), and the
   FY2024 realized amount *"net of carried interest compensation related to mature funds …
   attributable to BN"*. **Accrued, unrealized new-fund carry was $1,636M at 2025-12-31**, a
   Level-3 mark on fund valuations, before BN's third and before compensation.

**What the business consumes.** Not plant: capital expenditure appears only as "Other assets"
($17M / $8M / $9M, FY2023-25) and D&A is $14M / $14M / $40M. It consumes **money invested beside
clients and in other managers**: investments of $286M / $1,909M / $962M (FY2023-25; Castlelake,
Pretium, GEMS warehousing, Concora, Angel Oak, the Oaktree step-ups), BSI II consolidated, and
$2.2bn for the Oaktree remainder in July 2026. Those are acquisitions of fee streams and seed
capital, not maintenance — carried to Q4.

**The scarce input the business controls:** **locked, long-dated client commitments** — capital a
client cannot withdraw for a decade, or at all in the listed affiliates — **plus the track record
that lets the next vintage be raised, plus exclusive management of BN's own vehicles.** Three
qualifications, each from the filing, carried to Q2 rather than decided here: (i) *"BAM does not
have a legal right to the 'Brookfield' name or the 'Brookfield' logo"* — it holds a royalty-free
sublicence from BN, terminable on 30 days' notice if BN *"ceases to own at least 25% of the common
shares of our asset management business"* (Item 13, Trademark Sublicense Agreement); (ii) a
material part of the permanent capital is BN-controlled (*"a significant portion of our Fee-Bearing
Capital is represented by the capital of the perpetual affiliates, which are controlled by BN"*,
Item 1A); (iii) the locked commitment expires by design in the closed-end funds.

**Will the fundamentals look broadly the same in ten years?** The **mechanism** will: a fee on
committed capital, a carry on profits, a fee on BN's listed vehicles — the ULC's FY2022 combined
statements, carved out of BN, carry the same revenue lines (base management and advisory fees
$2,500M, incentive fees $335M, realized carry $241M; ULC EX-99.1). **The mix will not stay still**, and the filing
shows the direction: credit FBC $153.8bn (2022) → $325.9bn (2026-06-30), now **48% of FBC**,
much of it insurance capital at ~22bp; the blended base fee rate 90.4bp → 82.4bp in two and a half
years. **That is a Q2 question about the price of the product, not a Q1 question about what the
product is.**

**THE CASE FOR UNKNOWABLE, STATED AT FULL STRENGTH [E4-26, E4-51].** (1) The perimeter has changed
three times in four years (2022 spin, 2025 roll-up, 2026 Oaktree control) and will change the
statements again from Q3 2026 when Oaktree consolidates, bringing its own consolidated funds and
VIEs. (2) Fifty-nine strategies, five partner managers carried on the equity method, BUSHI and BMHL
tracking shares, three classes of BN-held preferred, compensation *"recovered from affiliates"*
($298M in FY2025) — the 10-K needs a 20-line reconciliation to get from net income to its own
headline measure. (3) A large share of the fee base is priced by a related party (BN sets BWS's
mandate terms; *"a fee may be paid as agreed … in other cases … no fee may apply"*, Item 13).
**Why it does not carry.** HHH closed UNKNOWABLE because the declared business was not the filed
one; RGTI because the model rested on a technical event that *"may never occur"*. **Here the
declared business and the filed business are the same business**, and every complexity above is
disclosed, captioned and reversible by a named subtraction: consolidated funds have their own
lines; BN's carry has its own NCI lines; the related-party fee is quantified ($234M on $108bn).
**[E4-46]'s five-minute test is passed** — the paragraph at the head of this section states the
engine — and no fetch is needed to understand it. Complexity of presentation is not complexity of
economics; it is carried to Q3 as a candor question **[E2-26, E4-22]**, where unintelligible
footnotes are a flag, not a Q1 closure.

- **VERDICT: [x] IN.** The business sells the management of other people's long-dated capital for
  a fee of roughly 0.8-0.9% a year and keeps about 56 cents of each fee dollar before tax; the
  filing shows every stream, the share of carry the Class A holder keeps, and the related-party
  portion, on one restated perimeter for FY2023-H1 2026. Nothing about how it makes money is
  hidden. Whether clients can take that money elsewhere at the same fee is Q2.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."*
> **[E3-03]**, 1991 letter

- **Needed or desired [x] YES.** Institutions must own duration-matched, inflation-linked real
  assets and private credit, and mostly cannot originate them in house. Fee-Bearing Capital rose
  $364.1bn (2021) → $417.9bn (2022) → $457.0bn (2023) → $538.5bn (2024) → $602.7bn (2025) →
  **$672.2bn (2026-06-30)** on gross inflows of $87.3bn in H1 2026 alone (10-K FY2025 and 10-Q
  Q2 2026 Fee-Bearing Capital roll-forwards). Demand is filed, not asserted.
- **No close substitute [ ] NO — and this is where the question is decided.** BAM's own Item 1
  says it in its own words: *"BAM competes with many other firms in every aspect of our business,
  including fundraising, investment opportunities and hiring and retaining professionals"*, and
  *"There are other funds focused on renewable power and transition, infrastructure, private
  equity, real estate, and credit strategies that compete for investor capital. Fund managers
  have also increasingly adopted investment strategies outside of their traditional focus"*
  (10-K FY2025, Item 1, Competition). The risk factors name the consequence for price:
  *"as competition and disintermediation in the asset management industry increase, there may be
  pressure to reduce or modify our asset management fees, including base management fees and/or
  carried interest, or modify other terms governing our current asset management fee structure,
  in order to attract and retain investors"*, and the substitute of last resort is the client
  itself: *"investors may prefer to insource and make direct investments; therefore, becoming
  competitors and ceasing to be clients"* (Item 1A). Nine SEC-filing managers sell the same
  product on the same metric below; the competitor row is the evidence, not this paragraph.
- **Not price-regulated [x] YES** — criterion (3) passes. Fees are contractual, negotiated fund
  by fund. No administered price floors this business and none caps it **[E2-59]**; the SEC
  attention every peer names in its risk factors is a disclosure regime, not a price regime.

**Criterion (2) fails, so the conjunction fails.** Two of three is not a franchise.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

> *"A moat that must be **continuously rebuilt** will eventually be no moat at all. Additionally,
> this criterion eliminates the business whose success depends on having a great manager."*
> **[E4-04]**, 2007 letter

**The framework's own scope test: does a lapse in spending destroy the structure or merely narrow
it, and does the spending defend the same advantage or buy its replacement?** BAM has three legs
and they answer differently, so the answer is given by leg and then weighted (10-Q Q2 2026,
Fee-Bearing Capital by strategy type).

| leg | FBC at 2026-06-30 | share | does the basis get replaced? |
|---|---|---|---|
| **Long-term private funds** | **$297,683M** | **44.3%** | **YES.** Closed-end, *"typically committed for 10 years with 2 one-year extension options"*; when the fund realises, the capital returns to the client and the fee on it stops. Distributions removed **$18.0bn** of FBC in FY2024 and **$12.8bn in H1 2026 alone** (roll-forwards). The fee base is a **depleting asset** and the next vintage **buys its replacement** — the Rhodes Ridge case the framework names, not the Coca-Cola case. |
| **Permanent capital and perpetual strategies** | **$293,484M** | **43.7%** | **NO.** Listed-affiliate Master Services Agreements on BIP/BEP/BBU that *"cannot be terminated without BN's consent"*, perpetual private funds, semi-liquid wealth vehicles, and BWS insurance capital. This leg is genuinely durable. |
| **Liquid strategies** | **$80,992M** | **12.1%** | **Redeemable at NAV.** Firm-wide outflows of $13.3bn in H1 2026. |

**So 56.4% of the fee base is periodically replaced or redeemable, and 43.7% is not.** The
durable leg is real, and the run states its limit rather than counting it as a franchise:
**the non-terminable part of it is non-terminable because the counterparty is the 74.7% owner.**
The MSAs on the listed affiliates cannot be terminated without BN's consent and BN controls both
sides; BN *"is not committed to an exclusive relationship with us, and we may compete with BN
(except for capital represented by the perpetual affiliates, which is exclusive) or compete with
other asset managers for BN's capital"* (Item 1A); and on the insurance mandate BN sets the fee
in its sole discretion. **That is [E2-59]'s shape — the protection belongs to the regime, not to
the product**, and the corpus's own version of how such a regime ends is *"That day is gone."*
A lock granted by your controlling shareholder is not a customer judgment that no close
substitute exists.

**Does success depend on a great manager? NO — and the [E4-23] check is written here at Q2, as
the framework requires, rather than as a compliment at Q3.** No fund key-person clause is quoted
in the 10-K; the Chair has been at Brookfield 36 years and a new CEO took office 2026-02-03 with
no disclosed capital consequence. **Key-person dependence is NOT recorded as a moat defect on
this evidence.** What IS recorded is the adjacent finding, in the filing's own words: *"our
ability to raise capital for existing and future funds depends on our funds' relative and
absolute performance"* and *"Strong investment performance enhances our ability to compete for
investors"* (Item 1). The fee base is re-won on results, continuously, across 59 strategies —
the **[E3-38]** have-to-be-smart-every-day shape, carried to Q3's weight case.

**Which of the four causes of extreme success is this [E4-36]?** Not an extreme max/min of one or
two variables, and not a nonlinear combination. It is closest to **wave-riding** — the twenty-year
institutional reallocation into private markets, which lifted every name in the row below by
10-35% a year of fee-earning capital at the same time. **[E3-51]**: *"when a surfer gets up and
catches the wave and just stays there, he can go a long, long time. But if he gets off the wave,
he becomes mired in shallows."* **A surfing run is not a moat; the advantage lives in the wave,
not the surfer.** The row shows nine surfers on one wave.

### Primary moat metric, filing-sourced, and its trend

**The metric: the base management fee rate in basis points on fee-earning capital** — the price of
the product. It is the right one because it is what the corpus's moat tests are actually about
([E2-44] raising prices, [E3-33] untapped pricing power, [E4-37] the agony of a price increase),
because every competitor files it or its inputs, and because it is what falls first when close
substitutes exist.

**BAM's trend, from the filed Distributable Earnings table and the Fee-Bearing Capital
roll-forwards (10-K FY2025 `0001628280-26-013098`; 10-K FY2024 `0001937926-25-000007`; 10-Q Q2
2026 `0001628280-26-054933`):**

| | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Base management fees, 100% basis incl. Oaktree ($M) | 3,956 | 4,233 | 4,896 | 2,625 (half-year) |
| Fee-Bearing Capital, period end ($M) | 456,998 | 538,541 | 602,714 | 672,159 |
| **Rate on average FBC (bp)** | **90.4** | **85.0** | **85.8** | **82.4** (annualised) |

*(Arithmetic: 3,956 ÷ avg(417,863, 456,998); 4,233 ÷ avg(456,998, 538,541); 4,896 ÷ avg(538,541,
602,714); 2 × 2,625 ÷ avg(602,714, 672,159). FY2022 FBC of $417,863M is read from the 10-K
FY2024.)*

**DIRECTION: DOWN, 8 basis points in two and a half years — and direction outranks existence
[E4-32].** The second reading says the same thing without a rate: H1 2026 Fee Revenues
**$2,920M, +13%** against FBC **+19%** year over year ($672,159M at 2026-06-30 against $562,735M
at 2025-06-30). **Revenue is growing six points slower than the capital it is charged on.** This
is **[E4-55]** inverted — there, pricing flattered dollars and the physical series was the honest
one; here volume flatters dollars while the price per unit falls, and the rate is the honest
series.

**THE DISCONFIRMING READ, built at full strength before the verdict is written [E4-26].** The
fall is **mix, not third-party price erosion**, and the filing supplies the separation.
Fee-Bearing Capital from BWS — BN's own insurer — was **$108 billion generating $234 million of
Fee Revenues in FY2025 ($92 billion and $167 million in FY2024)** (10-K MD&A, Credit, note 2):
**23.4bp on average capital.** Excluding it, the FY2025 rate is **(4,896 − 234) ÷ avg(446,541,
494,714) = 99.1bp** against a blended 85.8bp. **The third-party book prices near 99bp and is not
visibly eroding.** What that does and does not prove:
- It **defeats** any claim that BAM's outside customers are forcing its price down. They are not,
  yet.
- It **does not rescue criterion (2)**: 99.1bp still sits fourth of ten in the row below, and
  several peers' blended rates are depressed by exactly the same mechanism (KKR's by Global
  Atlantic, APO's by Athene), so a like-for-like ex-insurance row would lift them too.
- It **sharpens the mix finding rather than softening it.** In H1 2026, **$48.6bn of the firm's
  $87.3bn of gross inflows — 55.7% — came from BWS**, *"inclusive of the Just Group Plc.
  mandate"*, of which $44.8bn of Q2's $52.7bn (10-Q, Credit). **Seventy per cent of the
  half-year's entire $69.4bn increase in Fee-Bearing Capital was supplied by the controlling
  shareholder's insurance balance sheet, at roughly a quarter of the third-party price.** The
  growth on which the $1-trillion plan rests is, in the most recent filed period, majority
  related-party capital.

**THE COMPETITOR ROW — required [E3-28].** *"I can't be an intelligent owner of a business unless
I know what all the other businesses in that industry are doing."*

**One specification for every line: FY2025 management fees ÷ the average of the fee-earning
capital balances at 2024-12-31 and 2025-12-31, each read from that company's own FY2025 10-K.**
Every figure below was checked back to the peer's own 10-K text rather than taken from the
transcription. Supporting data, quotes and arithmetic: `Test Runs/_research 2026-09-13
BAM/peers/peer_row.md` and `peers/calc.py`.

| Company | FY2025 mgmt fees (line as filed) | fee-earning capital YE2024 → YE2025 (measure as filed) | **fee rate, bp** | FEAUM CAGR 23-25 | FRE margin FY2025 | perpetual / long-dated share, as stated | 10-K accession |
|---|---|---|---|---|---|---|---|
| **BAM (subject)** | **$4,896M** "Base management fees", 100% basis incl. Oaktree *(GAAP "Base management and advisory fees" $3,384M)* | **$538,541M → $602,714M** "Total Fee-Bearing Capital" | **85.8** *(GAAP line 59.3; **ex-BWS 99.1**)* | **14.8%** | **54.6%** (FRE $2,995M ÷ Fee Revenues $5,487M; 56.1% before the "not attributable to BAM" step) | **87%** *"long-dated or perpetual"*; permanent + perpetual 39.9% of FBC | `0001628280-26-013098` |
| OWL | $2,521.9M "Management fees, net" | $159,794M → $187,735M FPAUM | **145.1** | 35.2% | 56.4% | **85%** of mgmt fees from Permanent Capital vehicles | `0001823945-26-000009` |
| TPG | $1,826.4M "Management fees" | $141,286M → $170,102M FAUM | **117.3** | 11.5% | 45.2% | not disclosed | `0001880661-26-000011` |
| ARES | $3,680.5M "Management fees" | $292,553M → $384,949M FPAUM | **108.6** | 21.1% | 41.7% | **93%** of mgmt fees from *"perpetual capital or long-dated funds"* | `0001628280-26-011413` |
| BX | $8,075.6M "Management and Advisory Fees, Net" *(segment base fees $7,548.9M)* | $830,709M → $921,674M FEAUM | **92.2** *(86.2 on base fees; firm's own "Annualized Base Management Fee Rate" **0.86%**)* | 9.9% | 58.3% | Perpetual Capital $523.6bn = 41.1% of AUM | `0001193125-26-082531` |
| CG | $2,396.6M "Fund management fees" *(segment $2,243.1M)* | $304,358M → $336,778M fee-earning AUM | **74.8** *(70.0 on segment)* | 4.7% | 46.8% | Perpetual 32.9% of FEAUM (9.1% ex-Fortitude) | `0001527166-26-000009` |
| KKR | $2,496.8M GAAP "Management Fees" *(segment $4,100.8M)* | $511,963M → $604,144M FPAUM | **44.7** *(**73.5** on segment)* | 16.4% | 69.1% | **92%** of AUM duration ≥8 years incl. perpetual | `0001404912-26-000007` |
| APO | $2,378M GAAP "Management fees" *(segment $3,391M)* | $568,666M → $709,139M Fee-Generating AUM | **37.2** *(**53.1** on segment)* | 19.9% | 56.6% | *"over 70% of total fee-generating AUM"* perpetual | `0001858681-26-000013` |
| TROW | $6,602.3M "Investment advisory fees" | $1,606.6bn → $1,775.6bn ending AUM *(no FEAUM measure)* | **39.0** *(firm's own EFR 39.4, down from 41.9 in 2023)* | 10.9% | 29.9% GAAP operating margin *(no FRE)* | n/a | `0001628280-26-008002` |
| BLK | $19,179M "Total investment advisory, administration fees and securities lending revenue" | $11,551.3bn → $14,041.5bn total AUM *(no FEAUM measure)* | **15.0** | 18.4% | 44.1% *"operating margin, as adjusted"* *(no FRE)* | n/a | `0001193125-26-071966` |

**Comparability flags, carried rather than smoothed:** BLK and TROW publish no fee-earning-AUM
measure, so their denominators are total AUM and their rates are not like-for-like — they are in
the row because they are the substitute at the traditional end, and their direction (TROW 41.9 →
39.4bp on its own disclosure) is the comparable fact. KKR's and APO's GAAP fee lines are net of
consolidation eliminations, so both bases are shown. FRE definitions differ by firm (BX and KKR
include fee-related performance and transaction fees; ARES is after OMG costs; OWL's own margin
is before NCI). **None of these flags moves the subject out of the middle of the pack on any
column.**

**WHERE THE SUBJECT SITS: fifth of ten on price (fourth ex-BWS), sixth of ten on growth, fifth of
eight on FRE margin, and inside the pack on duration (87% against ARES 93%, KKR 92%, OWL 85%).
Not an outlier on any of the four.** That is what a close substitute existing looks like in filed
data, and establishing it is the row's whole job.

- **Peers named: NINE**, of an industry whose SEC-filing managers of scale number nine. Buffett
  says eight **[E3-28]**; the row takes nine, each from its own FY2025 10-K, on one specification.
- **Peers NOT taken, named with the document that would resolve them:** EQT AB (Stockholm),
  Partners Group (Zug), Antin (Paris) and Tikehau (Paris) are listed managers of scale that do not
  file with the SEC; their annual reports would resolve them. Stonepeak, I Squared, Bain Capital
  and Global Infrastructure Partners (now inside BLK) are private or absorbed. **This does not
  make the class PROVISIONAL, and the reason is directional: every missing name is an additional
  substitute.** A longer row can only strengthen a finding that close substitutes exist; it cannot
  manufacture their absence. **Were this Q2 heading for IN, those four annual reports would have
  to be pulled first and the class held PROVISIONAL — which is UNRESEARCHED — until they were.**
  It is not, so they are named and left. *(Recorded so that a later run wanting to reverse this
  verdict knows exactly which four documents it must fetch.)*
- **The row's limit, stated [E3-61]:** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't … I think you'd have to know the people
  involved."* The row shows position; it cannot show conduct. What it can show is that **all nine
  independently describe the same discounting behaviour in their own risk factors** — BX's
  *"willingness of certain of our competitors to charge lower fees"*; KKR's *"reduced management
  fees, fee holidays"*; APO's *"there is a risk that management fees and performance fees in the
  alternative investment management industry will decline, without regard to the historical
  performance of a manager"*; ARES's *"a general trend toward lower fees in the investment
  management industry"*; TROW's *"persistent downward fee pressure"*. Nine filers is as close as a
  row can come to evidencing conduct, and it points one way.

### The remaining Q2 tests, each answered

- **[E2-44], the two-characteristic test.** *(a) Can it raise prices when demand is flat and
  capacity is not fully utilised?* **NO** — the filed rate fell 90.4 → 82.4bp through a period of
  record fundraising, which is the easier conditions, not the flat ones. *(b) Can it grow dollar
  volume with only minor additional capital?* **PARTLY** — cumulative "Other assets" capex of $34M
  across FY2023-25 against $146bn of added FBC; but growth was also **bought**, at investments of
  $286M / $1,909M / $962M (FY2023-25) and ~$2.2bn attributable to BAM for the Oaktree remainder in
  July 2026. Half the test passes.
- **[E3-46], the second question about the business, and it is a number.** Net income to common
  $1,839M / $2,168M / $2,485M on average common equity of ~$9.3bn / ~$8.9bn / ~$8.4bn =
  **19.7% / 24.3% / 29.5%**. High — and **not evidence of a moat here**, because it is the
  industry's structural result: a fee manager employs almost no capital by construction, so every
  name in the row prints a high return on it. A class characteristic shared by ten filers is not a
  relative advantage. Recorded, not counted.
- **[E2-53], the dominance class.** **NO.** *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be."* BAM's $602.7bn of FBC sits
  against BX's $921.7bn, APO's $709.1bn of fee-generating AUM, KKR's $604.1bn and BLK's $14.0tn of
  AUM. Nobody here sets the price alone.
- **[E2-45], the attacker's test — the sharpest single fact against a moat.** *"how I would like,
  assuming I had ample capital and skilled personnel, to compete with it."* **The industry has
  already answered it in filings.** Blue Owl took fee-paying AUM from $102.7bn to $187.7bn in two
  years — **35.2% a year, at 145.1bp**, having reached the public market only in 2021. Ares did
  21.1% at 108.6bp; Apollo 19.9%. All three grew faster than BAM's 14.8% at an equal or higher
  price. **Capital and people are demonstrably sufficient to take share in this industry inside
  two years.**
- **[E4-37], the inverse metric.** *"you can almost measure the strength of a business over time
  by the agony they go through in determining whether a price increase can be sustained."* The
  10-K's pricing language is entirely defensive — *"pressure to reduce or modify our asset
  management fees"*, *"investors in our private funds may demand lower fees for new or existing
  funds"*. **No price increase is contemplated anywhere in the filing.** Not yawn-pricing, not
  even agony-pricing: the direction of the conversation is down.

### Untapped pricing power **[E3-33]** — could a manager raise the return simply by raising prices, and has not?

**NO, and the claim is refused rather than left open.** **[E5-28]** scopes the class: *"If you name
some business that has incredible pricing power, you're talking about a business that's a monopoly
or a near monopoly"* — claiming it here would be claiming near-monopoly, and the row is nine filed
competitors, four of them charging more on the same metric. The filed direction is down rather
than held back: 90.4 → 82.4bp, with the largest single block of new capital (BWS, 55.7% of H1 2026
gross inflows) priced at ~23bp. **The one place the question is genuinely live is that
related-party block** — a third party might well pay more than 23bp for the same mandate. But it
is BN that would have to raise that price on itself; the 10-K gives BN the discretion, and *"a fee
may be paid as agreed … in other cases … no fee may apply"* (Item 13). **Untapped pricing power
that your controlling shareholder must volunteer to pay is not the ultimate no-brainer; it is a
related-party term.**

### Class and direction

- Class: [ ] WIDE  [x] **NARROW — on the perpetual leg only, and conferred rather than won**
  [ ] NONE  [ ] PROVISIONAL
  *(Not PROVISIONAL: nine peers, one specification, one window, each from its own 10-K, with the
  four unpulled foreign filers named above and shown to be directionally incapable of reversing
  the finding.)*
- **Direction: NARROWING.** The primary metric fell 90.4 → 85.0 → 85.8 → 82.4bp; fee revenue is
  growing six points slower than the capital it is charged on; the fastest-growing block of
  capital is the cheapest and comes from the controlling shareholder; and 56.4% of the fee base is
  replaced or redeemable by design. **[E4-32]**: the moat *widened every year* is *"the primary
  criterion of a great business."* This one is not widening.

### THE CASE FOR IN, BUILT AT FULL STRENGTH AND REJECTED **[E4-26, E4-51]**

*[E4-51] requires a bear case its holders would accept as fairly stated at Q4. The same discipline
is owed to the bull case at the gate that closes the file.*

**The strongest case for a franchise.** 87% of the fee base is long-dated or perpetual and a
closed-end client **literally cannot leave** for a decade — switching cost in its most literal
form, stronger than a brand. The listed-affiliate MSAs are perpetual and non-terminable. The
third-party fee rate is **99.1bp and is not falling**. The scarce input is real: very few firms on
earth can write a $10bn equity cheque into a regulated infrastructure platform and then operate it
with 250,000 operating employees, and **[E2-45]**'s attacker would need a decade and a filed track
record, not merely money. Returns on the capital the business actually uses are ~27% on tangible
common equity. Oaktree, Castlelake, Angel Oak and Primary Wave bought capabilities an entrant
would have to build from nothing.

**Why it does not carry, one line each:**
1. **Criterion (2) is a customer judgment, and nine filers sell the substitute.** The lock is on
   money already committed, never on the next dollar — and the next dollar is competed for daily,
   by the company's own account.
2. **The basis of the largest leg is periodically replaced** — $12.8bn of FBC left through
   distributions in H1 2026 — which is precisely the class **[E4-04]** excludes.
3. **The durable leg's durability is granted by the 74.7% holder**, who is also the largest
   client, the carry partner, the licensor of the name (terminable on 30 days' notice if BN falls
   below 25% of the asset manager) and the party setting the price on $108bn. **[E2-59]**: that
   protection belongs to the regime.
4. **Direction outranks existence [E4-32]**, and every direction available in the filings — rate,
   revenue against capital, mix — points the same way.
5. **The record is a surfing run [E3-51, E4-36]**, and nine surfers are on the wave, three of them
   moving faster.

**A conclusion that required fighting for it is worth less, not more [E4-18].** This one required
no fighting: the subject's own Item 1 concedes the competition, and the row puts it mid-pack on
all four filed measures.

- **VERDICT: [x] OUT — ON THE BUSINESS. Permanent.** It is a very good business and it is not a
  franchise. Criterion (2) of **[E3-03]** fails on the filings of nine competitors selling the same
  product at the same or higher prices, three of them growing faster; 56.4% of the fee base is
  replaced or redeemable by design **[E4-04]**; the durable remainder is locked by the controlling
  shareholder rather than by the customer **[E2-59]**; there is no untapped pricing power
  **[E3-33, E5-28]**; and the one metric that prices the moat has fallen in every measured period
  **[E4-32]**.
  *Not UNRESEARCHED: the competitor row is complete on one metric, one window, from primary
  filings, and the four unpulled foreign managers are named and shown to be directionally unable
  to reverse it. Not UNKNOWABLE: the evidence is in and it decides.*

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** — written because
the operator's instruction of 2026-09-01 requires a price and a refutation record on every name,
and because a run that stops writing at the closing gate destroys the evidence a future reader
would need to reopen it. **Q5 carries the heading `COMPUTATION — NOT A CLEARANCE` (operator rule
3) and no entry language appears anywhere below.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT GOVERNING**
*The file closed at Q2 (OUT, on the business). This section is written and kept because the
operator requires a refutation record on every name, and because a Q3 read discarded at the
closing gate is a read that has to be bought again. **It decides nothing here.** Full standard:
`Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE.**
- [x] **Daily execution [E3-38]** — the fee base is re-won vintage by vintage on investment
  results decided continuously across 59 strategies: *"our ability to raise capital for existing
  and future funds depends on our funds' relative and absolute performance"* (10-K Item 1A).
  **And because Q2 above returned OUT — no franchise — [E3-43]'s original form is the one that
  applies:** *"franchises can tolerate mis-management … a business, unlike a franchise, can be
  killed by poor management."* *(Written after Q2 closed, not before it: the draft of this
  section carried this sentence in the form "once Q2 has found no franchise", which presupposed a
  verdict that had not been reached. Corrected on the resume of 2026-09-13 and recorded here
  rather than silently repaired, per operator rule 6.)*
- [ ] **Control [E1-16]** — not ticked in the corpus's sense; a public holder can sell. **But the
  holder is a permanent minority**: BN holds 74.7% of the economic count, its CEO chairs BAM's
  board, Class A and B vote as one class while BN exceeds 50% (8-K 2025-02-05, Item 3.03), and BN
  controls the boards of the BUSHI and BMHL subsidiaries that can redeem its own tracking shares.
  Recorded as the condition under which every related-party term below was set.
- [ ] **Leverage [E3-29]** — not 20:1: corporate borrowings $3,466M against $7,513M of common
  equity (2026-06-30). **Recorded, not ticked:** $8.0bn of bridge-financing and equity commitments
  and $433M of fund guarantees sit off the balance sheet (10-Q Note 15), carried to Q4.
- **Case declared: Q3 would be a BINARY GATE** on daily execution and on [E3-43]. **No price
  compensates** where that case holds **[E1-16, E3-29, E5-35]** — which is a statement about how
  this question would have been weighed, not a live finding, because Q2 already closed the file.

**Honesty — binary, filings-based [E5-16], each matter dated to when it became public.**
- **No integrity disqualifier found.** Litigation: *"there was no material outstanding
  litigation"* (10-K Note 21, 2026-03-02; 10-Q Note 15, 2026-08-10). No Item 4.02 filing, no
  restatement box ticked on the 10-K cover, and no NT filing except the **NT 10-K of 2025-03-03**
  (`0001104659-25-019527`) for FY2024 — the year the registrant moved from 40-F to 10-K; the 10-K
  followed 14 days later.
- **The ICFR scope of FY2025, read.** Management's report and Deloitte's attestation both
  **excluded Brookfield Asset Management ULC — *"99% of total revenues"* and *"96% of net
  income"*** — from the FY2025 internal-control assessment, under SEC guidance for an entity
  *"acquired on February 4, 2025"*, while the same 10-K presents that entity as the **accounting
  acquirer and Predecessor**. Permitted, disclosed in plain words, and a one-year exclusion. **A
  prompt to read, not a finding [E5-36]:** the audited financial statements carry an unqualified
  opinion; the first year of internal-control assurance over the business that is 99% of revenue
  is FY2026.
- **A Q3 pass is the absence of found disqualifiers, not a finding that the managers are honest
  [E5-17].**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E3-48, E2-49, E2-52, E3-50].** *Each a prompt to
read, never a verdict.*
- [x] **Trumpeted projections [E4-22] — FIRES, in two published five-year plans.** Q3 2023
  shareholder letter (6-K filed 2023-11-09, `0001937926-23-000020`): *"This year, we put forth the
  goal of surpassing $1 trillion in fee-bearing capital by 2028. This 18% compounded annual growth
  … will propel our fee-related earnings to approximately $5 billion by 2028"* and *"in 2029 BAM
  is expected to realize approximately $2 billion of gross carried interest, which should grow to
  approximately $7 billion of annual gross carried interest realized by 2033."* Q3 2024 letter
  (6-K filed 2024-11-12, `0001937926-24-000029`): *"Our plan is to grow fee-bearing capital to
  more than $1 trillion over the next five years, doubling the size of our business. This
  generates 15%+ annual growth in earnings and dividends … with expected fee-related earnings
  growing to $5.0 billion"* and *"BAM can expect to realize approximately $2 billion of gross
  carry by 2029, this base has the potential to grow to $7 billion by 2034."* The Q2 2026 release
  (8-K `0001171843-26-005272`) reports performance *"above our long-term targets"*. **[E4-35]'s
  base rate applies to the *"15%+ annual growth in earnings"* leg:** fewer than 10 of the 200 most
  profitable companies of 2000 were expected to attain 15% annual EPS growth over twenty years.
- [x] **Guidance against outturn [E3-48] — READ, and the record is mixed, not clean.**
  - **The 2023 fundraising target, missed and re-described.** Q3 2023 letter: *"we increased our
    fundraising target to close to $150 billion for the year."* Outturn, Q4 2023 release (6-K
    `0001171843-24-000644`): *"We raised $93 billion of capital which, combined with the
    approximately $50 billion anticipated upon the closing of the American Equity Investment Life
    (AEL) insurance account, brings the total to $143 billion."* **$93bn raised against ~$150bn
    targeted; the gap was closed in the headline by a mandate from BN's own insurance affiliate
    that had not yet closed** (it closed 2024-05-02, 10-K definitions).
  - **The five-year bullseye moved one year in twelve months [E2-49]:** $1 trillion of FBC and
    ~$5bn of FRE *"by 2028"* (2023 plan) became the same two numbers *"over the next five years"*,
    i.e. 2029 (2024 plan); $7bn of annual carry *"by 2033"* became *"by 2034"*. The yardstick was
    kept and the date was moved, in the year after the fundraising target was missed. **Fires as a
    prompt.** *(The standing tally of this metric-withdrawal prior across the project — six fires,
    five failures before this run — is carried at the fold.)*
  - **On the 2024 plan to date the numbers are on or ahead of the line:** FBC $538.5bn
    (2024-12-31) → $672.2bn (2026-06-30), **15.9% annualised against the 13.2% a year that $1
    trillion by end-2029 needs**; FRE $2,456M (FY2024) → **$3,201M LTM** against the 15.3% a year
    that $5.0bn needs. **Two qualifications from the filing, both of which Q2 has now scored:**
    $48.6bn of H1 2026's $87.3bn of gross inflows came from BWS, *"inclusive of the Just Group
    Plc. mandate"* — BN's own insurer, at ~23bp; and **realized carry toward the $2bn-by-2029 leg
    is $0 in FY2025 and $16M in H1 2026.**
- [x] **EBITDA-style promotion [E4-29, E5-06] — FIRES, in the release and the 10-K alike.** The Q2
  2026 release headlines *"Fee-Related Earnings of $808 Million … Distributable Earnings of $707
  Million"*; GAAP net income is the fifth line of the table. FRE removes the tax provision (*"we
  do not believe this item reflects the present value of the actual tax obligations"*), D&A, and
  $298M of *"compensation costs recovered from affiliates"*; DE then **adds back equity-based
  compensation ($44M in FY2025)** against a Note 12 SBC charge of **$247M** (equity-settled $159M
  plus cash-settled $88M). **The dividend is set on this measure** (*"at least approximately 90%
  of its Distributable Earnings"*), and **DE exceeded operating cash on BAM's own perimeter by
  $805M, $500M and $127M in FY2023-25 and $545M in the TTM** (Q4 table). *(The corpus's mechanism,
  [E5-41]: depreciation is "reverse float" — the expense already paid — and it is exactly what
  these measures delete. Here D&A is small; the substantive deletions are tax, SBC and the
  affiliate recharge.)*
- [x] **Dividends that need the capital replaced [E2-52] — FIRES as a prompt, with debt in the
  role the corpus gives to issuance.** Dividends paid $2,101M / $2,478M / $2,818M (FY2023-25) and
  $3,020M TTM, against owner earnings of $1,285-1,326M / $1,659-1,822M / $2,065-2,227M /
  $1,686-2,020M — **127% to 179% of owner earnings in every period.** Funded first out of cash
  ($3,545M at end-2022 → $404M at end-2024), then by **$2.5bn of senior notes in 2025 and $1.0bn
  in April 2026**, plus $655M of related-party deposits in H1 2026 (including $555M of Oaktree
  cash transferred from BN). *"Beware of 'dividends' that can be paid out only if someone promises
  to replace the capital distributed."*
- [ ] **Serial share issuance [E5-15] — does not fire.** The 1,194,021,145 shares issued in 2025
  were an exchange for BN's 73% of the same business (no economic dilution); since then the
  outstanding count has fallen (1,614.2M at end-2024 → 1,597.2M) on buybacks, and the
  escrowed-stock plan is designed non-dilutive (equity-statement share subscriptions 785,664
  shares in FY2025). **Do not read the 10-K-to-10-Q cover fall as buybacks** — it is the
  issued-versus-outstanding definition break recorded at Step 0.
- [ ] **Cash-tax tell [E4-30] — does not fire.** Income taxes paid $171M / $449M / $426M against
  pretax income $2,554M / $2,546M / $2,925M (6.7%, 17.6%, 14.6%) — rising over the window, not
  falling. *(Cash-flow supplemental disclosure, 10-K FY2025.)*
- [x] **Stock-price language [E3-50] — a weak prompt.** The 2024 letter framed the roll-up as
  *"allowing the market cap to accurately reflect the total market value of our asset management
  business, something closer to approximately $85 billion today"* and index inclusion as driving
  *"increased ownership among passive institutional investors"*; the pay disclosure says value
  *"is almost entirely based on share price over the long term."* The structural reason (one
  listed entity instead of a 27% holding) is real and disclosed. **Recorded, not scored.**
- [ ] **Except-for [E2-57] / restructuring charge [E3-53]** — a $35M *"non-recurring
  restructuring"* add-back in FY2023's FRE reconciliation; none since. Not fired.
- **Unintelligible footnotes [E4-22]:** the tracking shares, three preferred series, the affiliate
  recoveries and the carry split take real effort to follow, and **each is explained in words with
  a number beside it** (Notes 1-2, 12, 20; Item 13). **Not fired; the effort is recorded.**
- **Convergence [E4-52]:** four of the eleven prompts above fire, and they point one way — a
  non-GAAP headline that runs ahead of cash, a payout set on it, two five-year plans, a moved
  bullseye. *"extreme consequences from confluences"* — read as one reinforcing system rather than
  as a sum of prompts.

**STEP 3 — THE PRIMARY TEST [E2-01], balance sheet before income statement.** Common equity
(Predecessor-restated) $9,508M (2022) → $9,126M → $8,752M → $8,118M (2025) → $7,513M (2026-06-30)
— **falling because distributions exceed earnings**, not because earnings are weak. Net income
attributable to common stockholders $1,839M / $2,168M / $2,485M = **19.7% / 24.3% / 29.5% on
average common equity**; conservative owner earnings on tangible common equity (2025: $8,118M less
goodwill $236M less intangibles $234M) **~27%**. Two cautions: common equity includes the $4.8bn
carrying value of Oaktree and $1.6bn of accrued carry marks, and GAAP income includes unrealized
carry ($209M in FY2025). **Without undue leverage at the corporate level, the earnings rate on the
capital the fee business actually uses is high** — which Q2 has already scored as the industry
class result under **[E3-46]**, not as a moat.

**The half-owner test [E2-26]:** the 10-K and 10-Q tell a holder the carry split, the
BN-affiliated capital ($108bn of BWS FBC, $234M of fees), the ICFR exclusion, the bridge
commitments and the related-party deposits, in plain words. **It passes on disclosure.** It is
weaker on emphasis: the fact that **dividends have exceeded operating cash in every restated
year** appears nowhere in the MD&A in those words — the reader must assemble it from the
cash-flow statement.

**Authorship [E2-72]:** the shareholder letters are signed by the CEO and President. Recorded.

**The institutional imperative — score all four [E2-30].** *Not a fraud test:* *"Institutional
dynamics, not venality or stupidity."*
- [ ] resists any change in current direction — **no:** two restructurings in three years, a
  head-office move, and a voluntary change of filer status.
- [x] **projects/acquisitions materialise to soak up available funds** — Castlelake 51% (2024),
  Pretium ~11%, SVB Capital via Pinegrove, GEMS warehousing, Concora, Angel Oak 51.3% (~$149M),
  Primary Wave step-ups, and the Oaktree remainder (~$2.2bn attributable to BAM, 2026); investing
  outflows of $1,909M (FY2024) and $962M (FY2025) **while distributions already exceeded operating
  cash.** A prompt; each deal buys a fee stream.
- [ ] staff studies produced to justify the leader's craving — nothing in the filings tests it.
- [x] **peer behaviour mindlessly imitated** — insurance capital (BWS/AEL/Just Group),
  private-wealth semi-liquid vehicles, partner-manager stakes and AI-infrastructure funds are the
  industry's shared strategy set of 2023-26, visible in all nine competitor filings in the Q2 row.
  **A prompt, not a charge.**

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-24]:**
- **(1) ample funds for operations and liquidity? Not on the filing's own figures.** $412M of
  treasury purchases in FY2025 (cash-flow statement; 6,548,561 shares at an average $54.15 under
  the 2025 normal-course issuer bid, Item 5) and **$576M in H1 2026** (12,466,459 shares under the
  2026 bid by 2026-06-30) were made while dividends alone exceeded operating cash, while corporate
  borrowings rose from nil to $3,466M, and against $8.0bn of bridge and equity commitments with
  $3.1bn of corporate liquidity.
- **(2) repurchases at a material discount to conservatively calculated intrinsic value? No, on
  this run's range**: at $47-54 a share the buybacks were made at an owner-earnings yield of
  ~2.0-2.7% (see the Q5 computation).
- **→ CAPITAL ALLOCATION FLAG**, stated with the humility clause **[E4-13]**: the range is ours,
  and management knows the fee pipeline and the carry book far better than we do; *"many CEOs
  never stop believing their stock is cheap"* **[E5-08]**. **It binds position size, never the
  discount rate** — and there is no position here to bind.

**Pay — what vests on what.** Summary Compensation Table (10-K Item 11): NEO total $22.5M in 2025
(**0.75% of FRE**); Bruce Flatt $375,000 of salary plus $3,221,160 of escrowed shares at BAM (also
paid by BN). **Vesting is time-based only: *"we do not add performance conditions to our vesting
terms"***; awards vest 20% a year over five years with hold periods; *"Value creation for our
senior management team is almost entirely based on share price over the long term."* Cash bonuses
are *"discretionary … not formulaic."* **No DE, FRE or FBC formula drives pay**, so the trumpeted
targets are not wired into compensation — the incentive runs through the share price and the
~15.1M-share beneficial holding of the Chair. **[E4-27]** cuts both ways here and is recorded
rather than resolved: time-vesting removes the incentive to make a number, and leaves the
incentive to support a price.

**Related parties, read as terms [E4-52, E2-68].** BN sets the fee on its own capital *"in its
sole discretion"* (Item 1A); BN takes 100% of mature-fund carry and 33.3% of new-fund carry
*"regardless of participation"*; BAM's $1.1bn cash equivalent at 2025-12-31 was **a deposit with
BN**; BN provides BAM a $300M revolver; BN may terminate the Brookfield-name licence if it falls
below 25% of the asset manager; BWS has pledged 65M BAM shares for a $1.0bn margin loan.
**All disclosed.** The asymmetry is structural: **the controlling holder is simultaneously the
largest client, the carry partner, the landlord of the name and the bank.** **Recorded as the Q2
and Q4 context, not as an integrity finding** — [E2-68] tests conduct across an information
asymmetry, and the conduct visible here is disclosure of the asymmetry rather than concealment
of it.

**THE GUARDRAIL — checked before the verdict is written.**
- [x] Confirmed: nothing in this Q3 is being used to **promote** the name. The fee margin and the
  equity returns belong to the industry class **[E2-37, E2-38, E3-39]**, and Q2 has already scored
  them there. **IN never promotes, and this Q3 is not governing in any case.**
- [x] Key-person dependence is recorded **at Q2**, where **[E4-23]** puts it, and the finding there
  was that no moat defect of that kind is evidenced.
- [x] Is a great manager the reason to act? **No.** No action is contemplated.

- **VERDICT: [x] IN — no disqualifier found. RECORDED, NOT GOVERNING** (the file closed at Q2).
  Carried with a **live capital-allocation flag** — buybacks and dividends above owner earnings,
  debt-funded — and **converging presentation flags [E4-52]**: a DE headline that adds back SBC
  and sets the dividend, two five-year plans, a bullseye moved after a missed year, and a
  fundraising target closed in the headline by related-party capital. *IN is the absence of found
  disqualifiers, not a finding that the managers are honest — "sincerity and empathy can easily
  be faked" **[E5-17]**. IN never promotes.*

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT GOVERNING**
*The file closed at Q2 (OUT, on the business). Owner earnings are built and the survival question
answered because a closed file that discarded its arithmetic would have to buy it again. **It
decides nothing here.***

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**Built from the filed cash-flow statements only** (10-K FY2025 `0001628280-26-013098` for
FY2023-25 on the Predecessor-restated perimeter; 10-Q Q2 2026 `0001628280-26-054933` for H1 2025
and H1 2026; Note 12 for SBC). Script and output: `Test Runs/_research 2026-09-13 BAM/oe.py`,
`oe_out.txt`. **Not a net-income proxy, and not Distributable Earnings** — DE is reconciled below
and is not used.

| $M | FY2023 | FY2024 | FY2025 | TTM 2026-06 |
|---|---|---|---|---|
| Operating cash, as filed | 1,439 | 1,612 | 2,101 | 2,341 |
| + consolidated-fund investment flows sitting inside operating activities, stripped (BSI II etc.) | 0 | +251 | +467 | −49 |
| **= operating cash on BAM's perimeter (A1)** | **1,439** | **1,863** | **2,568** | **2,292** |
| − distributions to NCI and redeemable NCI (BN's carry and the BUSHI preferreds) | (42) | (52) | (216) | (281) |
| − SBC, Note 12 total (equity-settled plus cash-settled) | (98) | (138) | (247) | (273) |
| − (c) at D&A | (14) | (14) | (40) | (52) |
| **CONSERVATIVE owner earnings** | **1,285** | **1,659** | **2,065** | **1,686** |
| *generous: SBC at the cash-flow add-back (33 / 103 / 123 / 140), (c) at "Other assets" capex (17 / 8 / 9 / 22), plus look-through undistributed equity-method earnings [E3-04] (−21 / +122 / +7 / +171)* | 1,326 | 1,822 | 2,227 | 2,020 |
| *display only: OCF as filed − SBC(CF) − D&A, no perimeter adjustment* | 1,392 | 1,495 | 1,938 | 2,149 |
| Distributable Earnings (management, non-GAAP) | 2,244 | 2,363 | 2,695 | 2,837 |
| **DE minus A1** | **805** | **500** | **127** | **545** |
| Dividends paid to common | 2,101 | 2,478 | 2,818 | 3,020 |
| Treasury share purchases | 0 | 0 | 412 | 872 |

*(TTM = FY2025 − H1 2025 + H1 2026 on every line. H1 2025: OCF 643, consolidated-fund −465, SBC
note 101 / CF 62, D&A 14, capex 3, NCI 11, look-through +36, buybacks 116. H1 2026: OCF 883,
consolidated-fund −85 +136, SBC note 127 / CF 79, D&A 26, capex 16, NCI 76, look-through +200,
buybacks 576.)*

**Why the perimeter adjustments, and which way each cuts.** (1) "Changes in investments of
consolidated funds" is the fund's own investing, financed by the fund's own borrowings and outside
capital (the financing lines "Borrowings of consolidated funds" and "Capital raised from
redeemable non-controlling interest in consolidated funds"); leaving it in would charge BAM with
other investors' capital. Stripping it **raises** owner earnings, and BAM's own seed share is
charged instead at the great/good test below. (2) BN's carry and preferred dividends leave through
financing and are not the Class A owner's, so they come out — this **lowers** owner earnings.
(3) Look-through **[E3-04]** enters the generous end only.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** **No five-year window on one
perimeter exists**, against **[E2-42]**'s five-year default: FY2022 is the separation year
(operating cash −$374M after a $7,396M affiliate settlement and a $5,155M contribution from
parent, ULC EX-99.1) and FY2021 and earlier are carve-outs inside BN. The run says so rather than
splicing two perimeters, which is exactly the error the companyfacts splice at Step 0 would have
produced.
- **Short-window mean** (FY2024-25): conservative **$1,862M** · generous **$2,024M**
- **Long-window mean** (FY2023-25, the longest on one perimeter): conservative **$1,670M** ·
  generous **$1,792M**
- **TTM to 2026-06-30:** conservative **$1,686M** · generous **$2,020M**
- **Combined range: $1,670M to $2,024M** (window spread × capex/SBC band) — **21% wide.** **Not
  too wide to reach a conclusion [E4-25].**
- **Distorted years, named [E5-11]:** FY2024 carries a −$426M accounts-payable swing (cash-settled
  awards and bonuses paid) and FY2023 a −$559M rise in amounts due from affiliates; FY2025 carries
  the 2025 Arrangement (non-cash) and $2.5bn of notes (financing, not operating).
- **Favourable exogenous breaks [E4-41] — named, and not removed, with the reason:** FY2025 fee
  growth includes $95M of BBU performance fees earned over a unit-price high-water mark, and
  higher BEP/BIP/BBU prices added $44M of base fees. Both are market-driven and recur only with
  the prices. They total $139M, under 7% of the conservative mean; **carried inside the range
  rather than stripped, and the fact that the range's bottom does not depend on them is stated.**
- **Maintenance capex — a DISCLOSED JUDGMENT with the corpus default applied.** **The D&A default
  [E3-44, E2-41] holds; this is not the capital-intensive class [E5-20].** The plant is offices
  and software: "Other assets" capex $17M / $8M / $9M against D&A $14M / $14M / $40M (FY2025 D&A
  includes amortisation of the $234M of intangibles recognised in the 2025 Arrangement, which is
  not renewal spending). **The band, $9M to $52M a year, moves owner earnings by under 2% and
  changes no verdict.** What the business genuinely consumes — seed and GP capital, partner-manager
  stakes ($1,909M in FY2024, $962M in FY2025, ~$2.2bn for the Oaktree remainder in 2026) — **buys
  new fee streams rather than maintaining the existing one, so it is judged growth, not (c)**, and
  is priced at the great/good test. **[E2-23]'s fifth constraint via [E2-60] is live and is scored
  below: where leverage rises to fund the payout, (c) was understated.**
- **Stock compensation subtracted in full [E5-06] — RESOLVES AND IS COMPLETE on the charge
  measure.** Note 12 lists every plan: Management Share Option Plan ($44M), Escrowed Stock Plan
  ($60M), Restricted Stock Plan ($55M), Deferred Share Units ($88M, cash-settled), RSUs (nil) for
  FY2025. **The cash-flow add-back of $123M is below the Note 12 equity-settled charge of $159M**,
  so the conservative end takes the Note total ($247M) — the max-rule, applied in the direction
  that lowers owner earnings. **Carried-interest compensation sits outside the SBC tags** ($146M
  of expense and $155M realized in FY2025) and is a cash cost already inside operating cash when
  paid; the mature-fund portion is recovered from BN ($268M of recharges in FY2025, Note 20).
  **SBC/OCF(A1) on the Note measure: 6.8% / 7.4% / 9.6% / 11.9% TTM; cumulative FY2023-25 8.2%** —
  rising every period, and far below the ~50% level at which a grant-date read **[E3-70]** becomes
  necessary.
- **DE reconciled to cash.** DE exceeded A1 by **$805M / $500M / $127M / $545M**. The bridge, from
  the MD&A reconciliation and the cash-flow detail: DE counts **Oaktree's FRE at BAM's share**
  ($494M of *"Fee-related earnings of equity method investments at our share"* in FY2025) where
  cash counts only Oaktree's distributions; DE adds back **"compensation costs recovered from
  affiliates"** ($298M) before BN has paid them (receivables from affiliates for share- and
  cash-based compensation $732M → $1,611M → $1,240M); DE adds back **equity-based compensation**;
  and DE never sees the **working-capital build** in fees earned but uncollected. **DE is an
  accrual measure that runs ahead of cash, and the dividend is paid on DE.**

### Great, good, or gruesome? **[E4-20]**
- [x] **great — at the fee engine.** Fee Revenues $4,381M → $5,487M (FY2023-25, +25%) and
  Fee-Bearing Capital +$146bn on $34M of cumulative capex; owner-earnings return on tangible
  common equity ~27% (FY2025). *"The great one pays an extraordinarily high interest rate."*
- [ ] good  ·  [ ] gruesome
- **But the owner's account is not the fee engine's, and the run says so rather than taking the
  compliment.** Growth has also been **bought** — the partner-manager stakes and the Oaktree
  remainder — at prices the filings do not let a reader convert into a return (the Oaktree
  purchase accounting is *"not available"*, 10-Q Note 17) — and **the payout has exceeded owner
  earnings in every period.** Recorded as great-class economics with an **unmeasured acquisition
  return**, not as gruesome. **[E4-43]** is the check that stops this being over-read in either
  direction: only gruesome fails Q4.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — YES.** Positive owner earnings in every filed year
  on one perimeter; **87% of FBC long-dated or perpetual**; closed-end fees charged on committed
  capital for 10-12 years, so the near-term revenue line does not depend on fundraising. Qualified:
  $108bn (17.9%) of FBC is BN's insurer at ~23bp, and fees on BEP/BIP/BBU market capitalisation
  move with their unit prices (Item 7A names this as the primary market risk).
- **(2) massive liquid assets — NO.** Corporate liquidity **$3.0bn at 2025-12-31** (*"$1.6 billion
  in cash and short term financial assets … as well as $1.4 billion in undrawn credit facilities"*)
  and **$3.1bn at 2026-06-30** (*"$1.8 billion … as well as $1.4 billion in undrawn credit
  facilities"*), of which **$1.1bn of the 2025 cash was a deposit with BN** (10-K cash note).
  Against a **dividend run-rate of ~$3.2bn a year** ($0.5025 × 4 × 1,597M shares) and a **$1.0bn
  commercial-paper programme established 2026-03-03** with no borrowings outstanding. **[E5-39]'s
  test counts neither bank lines nor commercial paper** — *"We will never be dependent on the
  kindness of strangers"* — and on that test the liquid assets are $1.6-1.8bn against a $3.2bn
  annual payout.
- **(3) no significant near-term cash requirements — NO.** **Bridge-financing and other equity
  commitments: $3.3bn (2024-12-31) → $6.6bn (2025-12-31) → $8.0bn (2026-06-30)** —
  *"signed investment commitments for bridging portfolio company acquisitions and limited partner
  commitments with third parties and funds and or entities managed by BAM. The Company earns fees
  in connection with bridge financing and **bears the risk associated with syndicating the
  commitment**"* (10-Q Note 15) — plus **$433M of fund guarantees** (from $179M). **2.6× corporate
  liquidity.** The filing gives the total and **no maturity schedule**; that absence bounds how
  precisely the exposure can be sized, not whether it exists.
- **Score: 1 of 3.**
- **Leverage, named and quantified [E4-16, E3-29, E2-54, E3-52]:** senior notes **$3,466M** (from
  nil at end-2024): $600M 4.653% 2030, $550M 4.832% 2031, $750M 5.795% 2035, $850M 5.298% 2036,
  $750M 6.077% 2055 — **no maturity before 2030**; unsecured, a lien covenant, a 101%
  change-of-control offer (8-K 2026-04-17); and a bank-facility covenant that *"may limit our
  overall indebtedness to a percentage of distributable earnings"* (Item 1A). **The coverage test
  [E2-54]** — all interest met out of current cash flow net of ample capex: interest paid $87M
  (FY2025) and $90M of expense in H1 2026 against conservative owner earnings of $1,686-2,065M,
  **~9× to ~24×**, with capex already deducted. Also ranking ahead of the Class A holder: **$1,238M
  of preferred shares redeemable NCI** held by BN, $1,244M due to affiliates (including the $555M
  Oaktree deposit), and $589M of non-recourse consolidated-fund borrowings. Net corporate debt
  ~$2.0bn, ~1.2× conservative TTM owner earnings. **The quantity is modest. The direction is not:
  nil to $3.5bn in eighteen months, while distributions exceeded owner earnings.** **[E3-52]**
  cuts the other way and is recorded: none of this is customer-prepaid, covenant-free, long-dated
  float; it is ordinary covenanted corporate debt, merely long-dated.
- **Restricted earnings [E2-60] — FIRES.** *"a company that consistently distributes restricted
  earnings is destined for oblivion"*, the restricted portion being the one whose payout costs
  *"its financial strength."* FY2025: dividends plus buybacks $3,230M against conservative owner
  earnings $2,065M, with corporate borrowings +$2,478M. H1 2026: $2,187M paid against $883M of
  operating cash, with notes +$995M and related-party deposits +$655M. **By the framework's own
  fifth constraint, the owner-earnings figures above overstate what could be distributed without
  borrowing; the excess above them is the restricted part.**
- **Jurisdiction [E3-66]:** a British Columbia corporation controlled 74.7% by another Canadian
  corporation; US holders bear Canadian withholding on dividends (15% under the Treaty). **Where
  do the public shareholders stand in the queue?** Behind $1,238M of BN-held redeemable preferred,
  behind BN's 100% of mature-fund carry and 33.3% of new-fund carry, and alongside BN on the Class
  A line — with BN holding 74.7% of it. **Stated, not priced.**

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
**The bear case its holders would accept as fairly stated:** *BAM is a fee manager on locked
capital that has been turning itself into a lender to its own deal flow while paying out more than
it earns.*
- **The mechanism — THE WAREHOUSE.** In a real-asset and credit downturn of the kind already
  visible in its own filings — accrued carry on mature funds fell from **$1,394M (2023) to $931M
  (2024) to $197M (2025)**, a −$734M fair-value change in 2025 alone *"reflecting lower relative
  valuations across various mature real estate flagship funds"* — four things arrive together:
  (i) the **$8.0bn of bridge and equity commitments** stop syndicating and land on BAM's balance
  sheet; (ii) the commercial paper and the revolver that would fund them are the markets that shut
  first; (iii) fees on the **$374bn of permanent, perpetual and liquid FBC** billed on market
  capitalisation or NAV fall with prices, and new vintages slip; (iv) the dividend, set at *"at
  least approximately 90%"* of an accrual measure that already runs ahead of cash, must be cut or
  borrowed for. **Exposure, not experience [E4-40]:** the commitment total grew **2.4× in eighteen
  months, in a benign market**, which is exactly the *"benign loss history late in a good cycle"*
  the corpus calls *"not only useless, but actually dangerous"* as a guide.
- **Quantified from filed figures [E3-24].** If **half** of the $8.0bn failed to syndicate and
  were held at a 20% mark-down, BAM would need ~$4.0bn of funding against **$3.1bn** of corporate
  liquidity and would book ~$0.8bn of losses — **about 40-50% of a year's conservative owner
  earnings, and a funding gap of ~$0.9bn** before any dividend. **Fees on the $298bn of closed-end
  FBC would keep arriving** (committed capital, 10-12 year terms), which is why this mechanism
  kills the payout path and the growth plan rather than the business. A **25% fall in BEP/BIP/BBU
  prices** would take a share of the $466M of incentive distributions (plus the $95M of BBU
  performance fees, earned over a unit-price high-water mark) and the market-cap base fees
  with it (the magnitude is not separable from the 10-K's tables; **named, not computed**).
- **The second mechanism, slower: the controlling holder.** BN is the largest client (BWS $108bn
  of FBC; the listed affiliates' capital, *"exclusive"*), the carry partner, the licensor of the
  name (terminable if BN falls below 25%), the depository of BAM's cash and a lender; BWS has
  pledged 65M BAM shares against a $1.0bn margin loan. **A stress at BN transmits to BAM through
  every one of those channels at once**, and Q2 has already found that the durable half of the
  moat is granted by the same party.
- **Likelihood, in the corpus's vocabulary:** insolvency of BAM — **a low-level possibility** (no
  maturity before 2030, 9-24× coverage, contractually locked fees). **The dividend path breaking —
  a real possibility** (it has exceeded owner earnings in every filed period).
- **Survival shape: a NINTH, THE WAREHOUSE** — the asset-light manager that lends its own balance
  sheet to its funds' deals, so that its commitments grow faster than its liquidity and the
  syndication risk lands in the same downturn that shuts its short-term funding — **carrying the
  FIFTH shape's feature (distribution above owner earnings, [E2-60]) in a debt-funded rather than
  divestiture-funded form.** Not ORCL's (the commitments are bridges, not a multi-year build it
  contracted not to stop), not ARM's (SBC is 8.2% of operating cash), not BE's (three restated
  years exist, and the carve-outs exist behind them), not ACVA's (the deposits are related-party,
  not customers').

- **VERDICT: [x] IN — RECORDED, NOT GOVERNING.** The business survives its named death; the payout
  does not. Owner earnings $1,670M-$2,024M across every window and both (c) ends, 21% wide; SBC
  resolves and is complete; coverage ~9-24×; no maturity before 2030; the fee base is contractually
  locked for a decade on $298bn of committed capital.
  **Staying power scores 1 of 3 and the IN is written anyway, for a stated reason rather than a
  caveat:** the near-term cash requirement that fails strength (3) is, in the main, **the dividend
  and the buyback — both discretionary.** Cutting the payout releases ~$3.2bn a year immediately
  and the fee revenue keeps arriving on committed capital, which is why **[E2-54]**'s coverage test
  passes at 9-24× and why the mechanism above breaks the distribution rather than the company.
  **The restricted-earnings flag [E2-60] fires and the ninth survival shape is named — neither is
  a finding that BAM dies; both are findings about the dividend and the growth plan.**
  *The one document that would sharpen, but not reverse, this section is a maturity or syndication
  schedule for the $8.0bn of commitments. No filing carries one; the 10-K and 10-Q give the total
  alone. It is recorded at Q6 as a reopening condition rather than as a caveat on this verdict,
  because the verdict rests on the coverage test and the contractual fee term, not on the schedule.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass. **Q2 returned OUT, so what follows is headed as a computation, per
operator rule 3.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? — **COMPUTATION — NOT A CLEARANCE**

*The hard sequence closed the file at **Q2 (OUT, on the business)**. Operator rule 3: valuation
arithmetic produced where Q1-Q4 have not all cleared is headed as a computation and carries no
entry language. It is reported because the operator's instruction of 2026-09-01 requires a price
on every name. Script and output: `Test Runs/_research 2026-09-13 BAM/q5.py`, `q5_out.txt`. The
engine casts no vote **[E3-34]**.*

**Inputs, all established above:** price **$47.26** (2026-09-11 close; Yahoo chart API —
**aggregator, flagged, live quote only**) × **1,597,251,633 economic shares** = cap **$75,486M**;
owner earnings **$1,670M (conservative, FY2023-25) to $2,024M (generous, FY2024-25)**, TTM
$1,686M-$2,020M; sovereign **5.35% USD** (US Treasury daily par yield curve, 30-year, 2026-09-11,
re-struck at the resume of this run).

**THE FLOOR, before anything else [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: the yield is **2.2%-2.7%**, so reaching ~10% needs
**~7.3-7.8 points a year of perpetual growth** in owner earnings — or, run through a
ten-year-then-4% engine at 10%, **14.1% a year (from $2,024M) to 16.7% a year (from $1,670M) for
ten years**. **Below the floor on every construction.** **[E4-35]**'s base rate stands against the
15% leg: *"fewer than 10 of the 200 most profitable companies"* of 2000 were expected to attain
15% annual EPS growth over twenty years. **Below roughly 10%, the name is not ranked — it is quit
on, whatever the sovereign is.**

**One book. Owner earnings against the bond.**

**1. THE YIELD**
- owner earnings **$1,670M-$2,024M** ÷ market cap **$75,486M** = **2.21% to 2.68%** · sovereign
  **5.35%**
- *management's Distributable Earnings ($2,837M TTM) would read 3.76%* — **not used**: DE runs
  $127M-$805M a year ahead of operating cash on BAM's own perimeter (Q4), adds back SBC, and is
  the measure the payout is set on.

**2. WHAT THE PRICE ALREADY ASSUMES**
- perpetual growth implied at the **sovereign**: **2.6% (generous) to 3.1% (conservative)** a year,
  forever
- at the **~10% floor**: **~14-17% a year for ten years**, then 4%
- what the business has actually done: Fee-Bearing Capital +13.0% a year (2022-25); Fee Revenues
  +11.9% a year (FY2023-25); conservative owner earnings $1,285M → $2,065M (FY2023-25, +26.8% a
  year) and back to $1,686M on the TTM — **a three-year series on one perimeter, containing a
  bought acquisition stream and a BN-affiliate mandate at ~23bp**
- the company's own plan: *"15%+ annual growth in earnings and dividends"* to FRE of $5.0 billion
  and FBC above $1 trillion by 2029 (Q3)

**3. WHAT YOU ARE PAID**
- return at the current price = **2.7 to 3.1 points BELOW the sovereign** on the yield, before any
  growth.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** Sovereign used **5.35%, the
bare rate; no per-name premium added.** Certainty was handled at the understanding gate (Q1, IN)
and would have been handled once more in the end discount. It is not stacked **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — priced at the ~10% floor, which is the corpus's
quit line rather than a discount rate chosen for this name:
- **zero growth:** **~$10-13 a share** (at the sovereign instead, ~$20-24)
- **conservative engine** ($1,670M, 8% for ten years, 3% after): **~$20-25 a share**
- **central engine** ($1,860M, 12% for ten years, 4% after): **~$35-40 a share**
- **plan-shaped engine** ($2,024M, 15% for ten years, 4-5% after): **~$50-60 a share**
- **current price $47.26** — **above the conservative and the central cases; inside the range only
  if the company's own 15%-a-year plan is delivered for a decade.**
- **The ceiling, stated [E2-63, E4-44]:** the growth that carries the plan-shaped case requires
  continuous fundraising and continued acquisitions, and *"the value of an asset … cannot over the
  long term grow faster than its earnings do"*. The upside is bounded by the fee rate — falling on
  the blend, and with the fastest-growing block of capital priced at ~23bp by the controlling
  shareholder — and by BN's share of the carry.

**WHAT THE BUYER IS PAYING FOR, IN WORDS.** At $47.26 a share, **about $10-13 a share buys today's
fee engine at the 10% quit line with no growth; the other ~$35 a share is payment for a decade of
~14-17% annual growth** — the five-year plan delivered and then repeated — out of a business that
already pays its owners more each year than it earns in cash and has borrowed $3.5bn in eighteen
months to do it.

**WHICH BAR?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — not used; no end margin is meaningful below the floor.
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      **No: $47.26 against a conservative case of ~$20-25. Above the whole conservative range → no.**
- **Windage count: ONE.** Conservatism is spent in the owner-earnings construction (Note 12 SBC in
  full, BN's distributions out, no look-through at the conservative end). The floor is not windage;
  it is the corpus's quit line **[E4-28]**. The engine growth rates are displays, not a second
  margin.

- **VERDICT: would be BELOW THE FLOOR — a FAIL ON PRICE, had the gates been reached. Not ranked
  [E4-28].**
  *(COMPUTATION — NOT A CLEARANCE. No entry language; the file closed at **Q2**. Note for the
  register: the price verdict and the business verdict agree here, so the Q2 finding is not
  load-bearing for the investment outcome — at this quote the name fails on price on any reading
  of the moat.)*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*No position is held and none is entered; the file closed at **Q2**. Q6 records, in words and
dated, what would reopen it and what would refute this run's findings **[E1-02]** — *"I believe in
establishing yardsticks prior to the act."* **No alert is armed and no PORTFOLIO row is added**
(FOLD step 4; the QLYS ruling — a price band on a name that failed on the BUSINESS is a category
error).*

**What would prove this run wrong — pre-committed, each tied to a named future filing:**

1. **On Q2 (the franchise verdict: close substitutes exist and the price of the product is
   falling).** The verdict rests on four legs, and it is withdrawn if the filings break any two of
   them together:
   - **the price leg** — three consecutive fiscal years in which BAM's **third-party (ex-BWS) base
     management fee rate rises** on the specification used in the competitor row (FY fees ÷ average
     fee-earning capital) **while at least five of the nine peers' rates fall** on the same
     specification. That would be BAM pricing *above* its industry rather than with it, which is
     what criterion (2) of **[E3-03]** actually asks about;
   - **the pricing-power leg [E4-37]** — a **filed fee increase on an existing fund or mandate**,
     taken without a compensating concession elsewhere in the terms. One such disclosure would be
     direct evidence of the class **[E3-33]** describes, and this run found none;
   - **the mix leg** — permanent and perpetual FBC rising above ~60% of the total **on third-party
     capital**, with BN-affiliated capital (BWS and the listed affiliates) disclosed separately and
     *not* supplying the majority of new inflows, as it did in H1 2026 (55.7% of gross inflows);
   - **the row leg** — the four listed managers not pulled here (**EQT AB, Partners Group, Antin,
     Tikehau**, each via its own annual report) showing BAM materially above all of them on fee
     rate and duration. *(This leg alone cannot reverse the verdict — every added name is an added
     substitute — but it is the named work order for anyone attempting the reversal.)*
2. **On the owner-earnings / DE gap:** two consecutive fiscal years in which operating cash on
   BAM's perimeter (filed OCF less consolidated-fund investment flows, as defined at Q4) **equals
   or exceeds Distributable Earnings**, with receivables from affiliates for compensation not
   rising. That would withdraw the finding that DE runs ahead of cash.
3. **On the payout [E2-60, E2-52]:** a fiscal year in which **dividends plus buybacks are covered
   by conservative owner earnings** with corporate borrowings flat or falling. That withdraws the
   restricted-earnings flag.
4. **On the ninth survival shape (THE WAREHOUSE):** bridge-financing and equity commitments (10-Q
   commitments note) falling back below corporate liquidity, **or** a filed maturity or
   syndication schedule showing them matched to uncalled fund capital. That withdraws strength
   (3)'s failure and is the single document Q4 named as missing.
5. **On the plan [E3-48, E2-49]:** FBC above $1 trillion and FRE at or above $5.0bn in the FY2029
   10-K, **with BWS/BN-affiliated FBC disclosed separately and third-party FBC growing at the
   plan's rate**, and gross realized carry approaching the stated ~$2bn in 2029. Delivered on
   third-party capital, that would count for the managers at Q3 and against this run's scepticism.
6. **On the Oaktree step:** the Q3 2026 10-Q's purchase accounting and first consolidated quarter
   — if consolidating Oaktree brings in funds or VIEs whose cash flows cannot be separated, the
   **perimeter finding at Step 0 reverses** and a future run must say so.

**Next catalyst dates:** Q3 2026 10-Q (~2026-11-10; the first quarter with Oaktree consolidated
and its purchase accounting); FY2026 10-K (~2027-03; the first ICFR opinion covering the ULC,
which was 99% of revenue and excluded from the FY2025 assessment); the normal-course issuer bid
expires 2027-01-12.

**The sell rule [E2-28]** — not applicable; there is no holding, so neither trigger and none of
the three hold conditions is live.

**The monitoring question, for any future holder [E4-17, E3-30]:** is the fall in the blended fee
rate *"just part of an aberrational cycle"* — a mix effect from cheap insurance capital, with the
third-party book intact at ~99bp — *"or [has] the business … slipped in a way that permanently
reduces intrinsic business values"*? **This run's answer is that it is mix today and that the mix
itself is the finding**, because the mix is supplied by the controlling shareholder. The series to
watch is the **ex-BWS rate**, published annually from the Credit note's BWS disclosure, against
the blended rate. **[E4-17]**: *"those beliefs change quite gradually"* — this one would need
three years to move, and **[E2-40]**'s counter-trigger would then govern the speed of acting on it.

**Do not trim winners [E5-14]** — not applicable. **Position size: none.** *(A capital-allocation
flag is live at Q3; any future sizing would be reduced by it, and that binds size, never the rate
**[E4-13]**.)*

- **VERDICT: [x] IN** — refutation and reopening conditions written, dated and tied to named
  filings, before any act rather than after one **[E1-02]**.

---
## SELF-AUDIT
*Ticked by the session that finished the run, 2026-09-13. An unticked box is a finding, and the
two qualified ticks below say what they are qualified by.*

- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → file closed.** Q3, Q4,
      Q5 and Q6 are written beneath an explicit RECORDED, NOT GOVERNING banner, and Q5 carries the
      literal heading `COMPUTATION — NOT A CLEARANCE` (operator rule 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Checked
      deliberately, because the killed session's Q4 draft ended *"if this Q4 were governing,
      strength (3) would need the commitment maturity schedule … before an IN could be written
      without a caveat"* — which is a thin-evidence IN and therefore UNRESEARCHED by the
      framework's own rule. **The caveat was removed and replaced by a reason**: the verdict rests
      on the coverage test **[E2-54]** at 9-24× and on the contractual fee term, not on the
      schedule, and the near-term cash requirement that fails strength (3) is discretionary.
      The missing schedule is recorded at Q6 as a reopening condition.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **None was issued.** The
      one place the question was live is Q2's moat class: four listed non-SEC managers (EQT AB,
      Partners Group, Antin, Tikehau) were not pulled, and the run states why the class is still
      not PROVISIONAL — every missing name is an additional *substitute*, so a longer row can only
      strengthen an OUT. **Had Q2 been heading for IN, those four annual reports would have had to
      be fetched first and the class held PROVISIONAL, which is UNRESEARCHED.** Named at Q6 as the
      work order for any attempted reversal.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **None was issued.** The
      case for Q1 UNKNOWABLE was built at full strength at Q1 and rejected on the stated ground
      that the declared business and the filed business are the same business.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked. **FY2025
      operating cash $2,101M on the filed cash-flow statement against companyfacts
      `NetCashProvidedByUsedInOperatingActivities` 2,101,000,000, accession
      `0001628280-26-013098`**, plus three further cross-checks. **No companyfacts row is used in
      any computation** — the splice found at Step 0 makes them unusable under this CIK.
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Three windows carried (FY2023-25, FY2024-25, TTM) and both (c) ends; range $1,670M-$2,024M,
      21% wide.** **The five-year default [E2-42] cannot be met and the run says so rather than
      splicing two perimeters** — that is a disclosed limit of the subject's filed history, not a
      choice of window.
- [x] Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED. **Nine peers, one
      specification, one window, each figure checked back to that peer's own FY2025 10-K text.**
- [x] Sovereign is for the earnings currency, from the issuing authority, dated. **USD 5.35%,
      2026-09-11, US Treasury daily par yield curve; re-struck at the resume rather than inherited
      from Step 0, and unchanged.**
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen, not both; windage count stated. **Screamer test [E4-01]; windage count ONE.**
- [x] Prices dated; aggregator used for live quotes only and flagged. **$47.26, 2026-09-11 close,
      Yahoo chart API, flagged; share count from the 10-Q cover, not the aggregator.**
- [x] Run committed to git. **Committed after Q2 and again at the fold, both with a pathspec.**

**One further check, not on the template, recorded because this was a resumed run.** The four
section drafts left on disk by the killed session carried five unresolved placeholders and at
least one line phrased as though Q2's verdict were already known (*"once Q2 has found no
franchise"*). **Q2 was decided from the filings and the peer row before any draft was read back
into the file**, and every presupposing line was rewritten with the correction recorded in place
rather than silently repaired (operator rule 6, and the CGNX prohibition). The verdict the drafts
presupposed and the verdict reached happen to agree; that they agree is not what makes the
rewriting unnecessary — the rewriting was done anyway.

## REGISTER
- Verdict: [ ] IN  **[x] OUT (about the business)**  [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT — a very good business and not a franchise: nine SEC-filing
  competitors sell the same product and BAM is mid-pack on price (85.8bp, 99.1bp ex-BWS), on
  growth and on margin, while its own fee rate falls 90.4 → 82.4bp and 56.4% of its fee base is
  replaced or redeemable by design; the durable remainder is locked by the 74.7% controlling
  shareholder rather than by the customer. Q3, Q4, Q5 and Q6 recorded, not governing.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable; no UNRESEARCHED verdict was issued. *(The
  nearest thing is the four non-SEC managers named at Q2 and Q6; they are a reversal work order,
  not a gap in this verdict.)*
- **If UNKNOWABLE:** not applicable.
- **Price verdict, for the register only:** below the ~10% floor on every construction — yield
  2.2-2.7% against a 5.35% sovereign, value ~$20-25 a share conservative against a $47.26 quote.
  **The business verdict and the price verdict agree, so nothing here turns on the Q2 call alone.**
