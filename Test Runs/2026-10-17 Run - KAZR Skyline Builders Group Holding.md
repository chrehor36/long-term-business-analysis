# Company Run — Skyline Builders Group Holding Limited (Nasdaq: KAZR, formerly SKBL) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, 2026-10-17, after the run was committed: **not held** (`PORTFOLIO.md` read for this one ticker, under KAZR, SKBL and Skyline).

**Dispatched run.** Written by a dispatched analyst under the canonical brief with one stated departure (the lines of
evidence are derived by the analyst from the 20-F's Items 4, 3.D and 5; see Step 0). Research folder:
`Test Runs/_research 2026-10-17 KAZR/` (notes file `_notes.md`, fetch script `fetch.py`; raw filings in its gitignored `cache/`).

**Contamination, declared and not used.** (1) The session opened with the repository's last five commit subjects in
view; they concern another company's v5 run (ticker SKK, closed OUT at Q1, described as now a drone start-up bought for
shares) and its fold. (2) The session's working-tree status listed research-folder names of other runs (AYI, ARCB) and
daily digest files; none was opened. (3) The memory index loaded into the session carries one-line summaries of the queue
state (wave counts, a count of gate-clearers, "nothing buyable"); none names this company. Nothing from any of these was
used in this file. No other run file, holding review, `PORTFOLIO.md`, the register, the reading list or the session-state
file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.96 (close 2026-10-16; `tools/run.py` live quote, an aggregator, flagged per operator rule 5: live quote only).
- **Shares by class.** `python Screens/cover_shares.py KAZR` failed ("FETCH FAILED: HTTP Error 404"), as the brief warned
  for a 20-F filer; the counts below are taken by hand from the filed documents.
  - Cover of the FY2026 20-F/A (2026-08-21, accession `0001213900-26-092307`), as of 2026-03-31: **15,486,491 Class A
    Ordinary Shares and 1,995,000 Class B Ordinary Shares** (Class B carries 20 votes a share); and 47,332,468 preferred
    shares (47,326,026 Series A, 6,442 Series B). The balance sheet in the same filing shows the same counts; no treasury
    shares are reported.
  - Item 10 of the same filing, as of 2026-08-10: **15,947,094 Class A, 1,995,000 Class B, 47,326,026 Series A preferred,
    6,442 Series B preferred** issued and outstanding. Ordinary shares at that date: **17,942,094**.
  - The instruments that become Class A shares (note 14 and note 16 of the FY2026 statements, same accession):
    Series A preferred convertible one for one (47,326,026); Series B preferred, stated value $5,000 each, convertible at
    $2.40 (6,442 × 5,000 / 2.40 = 13,420,833 shares, conversion price resettable down to a $1.50 floor); senior unsecured
    convertible notes of $16,575,000 and $3,000,000 principal convertible at $2.40 (8,156,250 shares); pre-funded warrants at
    par, 35,963,636 at 2026-03-31 less 550,000 exercised after year end (note 20) = 35,413,636; investor warrants 17,370,908 at
    $1.50; placement-agent warrants 4,794,868 at $0.73 to $2.40 less 350,613 exercised after year end = 4,444,255; the
    executive chairman's award of 3,000,000 Class A (750,000 vested and "to be issued", 2,250,000 unvested), and a further
    3,000,000 Class A awarded to him at closing of the business combination (6-K 2026-04-30, accession `0001213900-26-049689`).
  - Counts used (a reporting arithmetic, labelled CONVENTION of this run: the brief asks for one market value and the
    preferred and pre-funded warrants are economically ordinary shares; rationale: a per-share figure on the 17.9M ordinary
    shares alone would ignore some 83M shares obtainable for nothing or almost nothing):
    ordinary 17,942,094; **nominal-exercise basis 101,431,756** (ordinary + Series A 47,326,026 + pre-funded 35,413,636 +
    750,000 vested award); **fully diluted about 150.1M** (adding Series B 13,420,833, notes 8,156,250, investor warrants
    17,370,908, agent warrants 4,444,255, unvested award 2,250,000 and the closing award 3,000,000).
- **Market cap:** $35.2M on the ordinary shares; **$198.8M on the nominal-exercise basis**; about $294M fully diluted.
- **Sovereign for the earnings currency (HKD):** **4.519%**, the HKSAR Government 20-year benchmark issue 20GB4503001
  (Infrastructure Bond Programme, maturity 2045-03-06), closing reference yield of 2026-10-16, from the Hong Kong
  Government Bond Programme's own file (hkgb.gov.hk, `HKD_DailyClosingReferencePricings_IBPandGSBP.xls`, saved in
  `cache/hkgb/`). The 20-year is the longest HKD government tenor published; the older programme's 20GB4205 closed at
  4.474% the same day (`DailyClosings.xls`). `tools/sources.py` covers USD, JPY and EUR only; the HKMA statistics API
  refused the request (blocked), so the programme's file was read directly. The statements are presented in US dollars;
  the operating subsidiaries earn in Hong Kong dollars.
- **Filings read** (operator rule 4): FY2026 Form 20-F (2026-08-17, `0001213900-26-090838`) and its Amendment No. 1
  (2026-08-21, `0001213900-26-092307`, filed "to correct certain clerical data entry errors" and to add the iXBRL; the
  amendment is the text read); NT 20-F (2026-07-31, `0001213900-26-083576`); FY2025 Form 20-F (2025-08-07,
  `0001213900-25-073107`); the IPO prospectus 424B4 (2025-01-24, `0001213900-25-006549`); the F-1 resale registration
  (2025-11-14, `0001213900-25-110919`, opened for share history only); the 425s of 2026-04-30 (`0001213900-26-049722`,
  `0001213900-26-050424`), 2026-08-03 (`0001213900-26-084658`), 2026-08-04 (`0001213900-26-085208`), 2026-08-11
  (`0001213900-26-087848`) and 2026-08-17 (`0001213900-26-090751`); and every 6-K from 2025-01-24 to 2026-08-17 (accessions
  listed in `_notes.md`). A foreign private issuer files no proxy; Item 6 and Item 7 of the 20-F/A stand in for it. No
  interim report after 2026-03-31 has been filed.
- **One figure cross-checked against the filed statement:** total assets at 2026-03-31, `tools/run.py` 121,760 (USD
  thousands, XBRL of `0001213900-26-092307`) against the filed balance sheet **$121,760,466**; and operating cash for FY2024,
  tool −6.5M against the filed cash-flow statement **$(6,507,832)** (424B4 and FY2026 20-F/A). Both agree.
- `python tools/run.py KAZR`, arithmetic lines only: it found operating cash for FY2023 and FY2024 only (2.1 and −6.5,
  USD millions), no stock pay tagged, a share basis 565 days stale and a weighted average, not a cover count; it refused a
  growth figure because "the lower owner-earnings mean is at or below zero". The later years are taken by hand below.
  **Owner cash after every real cost, by year (USD millions, from the filed cash-flow statements; operating cash less stock
  pay added back, less capital spending including deposits for plant, less finance-lease principal):**

  | FY to 31 March | operating cash | stock pay | capital spending | lease principal | owner cash |
  |---|---|---|---|---|---|
  | 2023 | 2.1 | 0 | 0.2 | 0.4 | **1.5** |
  | 2024 | −6.51 | 0 | 0.06 | 0.22 | **−6.79** |
  | 2025 | −3.01 | 0 | 1.78 (deposits for plant) | 0.14 | **−4.93** |
  | 2026 | −2.85 | 2.24 | 0.21 | 0.06 | **−5.35** |
  | mean of the four | | | | | **−3.89** |

  FY2022 is not in any filing read (the prospectus statements begin at FY2023); the window is four years, said so.
  Depreciation: 1.12 (2024), 0.80 (2025), 0.37 (2026). Stock pay is real only in FY2026 (the chairman's award, $2,235,000).

**The lines of evidence this name needs** (the brief's one departure: derived here from Items 4, 3.D and 5, and chosen
before the questions were written). (1) What a buyer of a share owns today and in ten years: Item 4's introduction and
the business-combination conditions (6-K and 425s of 2026-04-30). (2) The economics of the Hong Kong subcontracting
business: Item 4 (customers, licence, competition) and Item 5 (margins, credit losses, working capital). (3) The capital
history: note 14 and 16 (placements, warrants, preferred, notes), and Item 7 (control). (4) What the combination target is:
the 425s (tungsten deposits, studies, development cost). (5) The cash and its uses after year end: note 20 and the 6-Ks
(the loan to Cove Kaz, the Reemag sale, the Nevada claims). (6) Item 3.D's own statement of what follows if the legacy
business is sold and the combination fails.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the buyer would be content to own it "if the market closed for five years"
**[M1997-109]**, for the cash "the asset, itself, produces" and not "by selling it to somebody else" **[M1997-052]**. That
test bears hardest here, because what the share will be in five years is set by a pending transaction, not by an
operating record. No macro forecast enters **[M2000-094]**; the executive chairman's case in the 425 of 2026-08-17
(`0001213900-26-090751`) is one: "We believe we are early in a worldwide, commodity super cycle that will see precious
metals, base metals, strategic and critical metals' prices increase dramatically over the next decade". Who is paid to tell
you: the investor deck in the 425 of 2026-08-11 (`0001213900-26-087848`) is the seller's own projection of what it sells,
and "You do not want to ask an investment banker what he thinks the earnings are going to be in five years of something
he's trying to sell" **[M2011-083]**; it is not used as evidence of value. **Contrary evidence, written down as found**
**[M1997-127]**: the legacy business is real and has a filed record (revenue $44.6M to $50.1M a year, FY2023 to FY2026), the
company holds cash and a stake in the combination target, and the tungsten deposits carry a stated JORC resource (425 of
2026-04-30, `0001213900-26-049722`); none of these is a forecast the speakers would accept as a ten-year view of the
business the share will be.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if it is bought without borrowed money and sized so that its loss to
zero is tolerable: "Never risk permanent loss of capital" **[L2023-005]**; "never going to risk what we have and need for
what we don't have and don't need" **[M2012-081]**. Nothing in the target's structure can call on the buyer.

---
## THE BALANCE SHEETS, read in Step 0 because the file closes before Q4 **[M2025-032]**
Filed statements, US dollars millions (FY2023 and FY2024 from the 424B4 `0001213900-25-006549`; FY2025 and FY2026 from the
20-F/A `0001213900-26-092307`; FY2022 equity and cash from `tools/run.py`'s XBRL table only). Eight to ten years do not
exist: the holding company was formed on 2024-06-25 and the filings begin at FY2022.

| 31 March | total assets | liabilities | equity | cash (restricted) | receivables | contract assets | bank borrowings | convertible notes | other investment | revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | n/f | n/f | 1.78 | 0.69 | n/f | n/f | n/f | - | - | n/f |
| 2023 | 16.68 | 14.03 | 2.65 | 1.56 | 2.08 | 3.86 (current) | n/f | - | - | 44.56 |
| 2024 | 20.51 | 17.47 | 3.04 | 0.32 | 3.82 | 8.72 (current) | 10.93 | - | - | 48.82 |
| 2025 | 28.49 | 19.90 | 8.59 | 0.72 | 10.03 | 5.67 | 12.04 | - | - | 46.01 |
| 2026 | 121.76 | 42.14 | 79.62 | 4.63 (46.20) | 7.47 | 2.26 | 11.98 | 19.57 | 46.16 | 50.11 |

What moved and why. The operating business is flat: revenue $44.6M to $50.1M over four years at a gross margin of 6.3%
to 6.6% (Item 5). What it needs grew against flat sales: receivables went from $2.08M to $10.03M in two years while revenue
did not grow, and in FY2026 the company charged $8,196,074 for "expected non-collection of certain aged accounts
receivable balances" (Item 5); operating cash was negative in FY2024, FY2025 and FY2026; bank borrowings of about $11 to $12M
roll every year (some $42M drawn and $42M repaid in each of the last three years, financing section). Equity before FY2026
came from retained profits of about $1M a year and the IPO's $4.8M net. The FY2026 jump in assets is not the business: it is
$46.2M of escrowed placement money (restricted cash), $19.6M of convertible notes, and a $46.2M "other investment" of which
$43.2M is a stake in Kaz Resources LLC, the combination counterparty, bought for $20.0M and written up by $23,437,041 on
that counterparty's later financings (note 6). Retained earnings turned to a $4.7M deficit after a $16.6M "deemed
dividend" on the warrant exchange (note 14). "what the figures are saying and what they don't say and what they can't say"
**[M2025-032]**: they say the legacy contractor earns thin margins and consumes cash; they cannot say what the company will
be after the transaction, because the business it is merging into files no statements here.

## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** "our definition of understanding is thinking that we have a reasonable probability of being able
  to asses where the business will be in 10 years" **[M2000-037]**; "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The first fact is what the share will own.
  - The company says, in its own 425 of 2026-08-17 (`0001213900-26-090751`), that its new controlling investors "took
    control of the Company via a significant cash injection with a goal to divest of the legacy Asian construction business
    and acquire assets in the critical material supply chain".
  - The Transaction Agreement makes that a closing condition: SKBL "shall have disposed, in a manner reasonably
    satisfactory to Cove Kaz, of its Hong Kong legacy business and (ii) shall have no operations or business in Hong Kong or
    China or liabilities related thereto" (6-K 2026-04-30, `0001213900-26-049689`, condition (g)); every SKBL share is then
    cancelled for one share of PubCo (Kaz Resources Inc.).
  - What PubCo will own: 70% of Severniy Katpar LLP, "one of the largest known undeveloped tungsten resources globally";
    "The project is advancing through feasibility, permitting, and development toward commercial production"; a Definitive
    Feasibility Study engaged in August 2026; "Total development costs are estimated at approximately $1.1 billion", to be
    met in part by letters of interest from EXIM ($900M) and DFC ($700M) (425s `0001213900-26-049722`,
    `0001213900-26-084658`, `0001213900-26-090751`); and 75% of the Akbulak rare-earth project, where Cove Kaz is "financing
    exploration until reserves are formally listed". No production, no revenue and no filed statements of the target were
    found in any filing read.
  - What SKBL owns besides the legacy business: escrowed and free cash; a loan of $23,100,000 to Cove Kaz (2026-04-22),
    replaced by a convertible facility of up to $45,000,000 (note 20); about 20% of Kaz Resources LLC (note 6); and two
    Nevada exploration properties bought for $136,000, "at an early stage of exploration" (6-K `0001213900-26-090743`).
  - If the combination fails, Item 3.D says: "If the Business Combination is subsequently delayed or not completed, we may
    have limited or no operating business and may be required to seek another business combination, raise additional
    financing or take other actions to continue as a going concern."
- **Key variables and whether they are foreseeable.** In ten years the share is either (a) a minority interest in a
  tungsten mine that has not been built, whose economics depend on a feasibility study not yet done, a $1.1B financing not
  yet committed, Kazakh permits and a commodity price; or (b) a cash shell seeking a deal. The Hong Kong contractor, the only
  part with a filed record, is by the company's stated aim and the deal's condition not part of either. "Start-ups are not
  our game." **[L2007-015]**; "We don't do startups." **[M2008-088]**. The framework lists start-ups first among what Q1
  rules OUT. A tungsten price is never by itself a STOP (Q2's commodity paragraph, **[M2016-025]**), and it is not the
  ground here: the ground is that there are no figures to decide from, "if you can't make a decision on something like
  PetroChina off the figures, forget about going further" **[M2008-069]**, and that the business the share becomes has never
  operated.
- **Routing.** Not TOO HARD: the deciding fact is not a forecast the industry would refuse to write down **[M2000-105]**, nor
  a document not yet read; it is answered from the filings, and against the name. A holding company is understood by its
  parts; the part that decides what the share is worth in ten years is the undeveloped venture (and, until closing, the
  cash committed to it), and "if you have doubts about something being into your circle of competence, it isn't"
  **[M2002-092]**. The legacy contractor cannot rescue the file, since the share is not to own it.
- **VERDICT: OUT.** The buyer of a share today is buying a promised start-up: an undeveloped Kazakhstan tungsten venture
  (with Nevada exploration claims beside it) into which the company's cash is being lent, while its one operating business
  is to be sold as a condition of the deal **[L2007-015]**, **[M2008-088]**, **[M2000-037]**, **[M2006-013]**.

## Q2 to Q12 — NOT REACHED (operator rule 2). Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are not answered.

---
## THE BOX
**OUT at Q1** (start-up: the share is to become an undeveloped Kazakhstan tungsten venture, and the Hong Kong contracting
business, the only part with a filed record, is to be disposed of as a condition of closing). Integrity facts recorded, not
judged. COMPUTATION beneath the stop: value range nil to nil against $1.96; fair price nil.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2.)* **[M1997-127]**

**Bearing on Q2 (the castle).** The 20-F/A's "Market and Competition" paragraph names no competitor, and Item 3.D names
none; no rival filing was read and none was chosen, so no competitor row exists (said so; no CONVENTION invoked). Facts
of the legacy business: mostly a subcontractor in roads and drainage; Approved Public Works Contractor in "Group B
(Probation)", "only eligible to tender for public projects of aggregated value up to HK$400 million"; five largest customers
87.3%, 82.7% and 84.9% of revenue in FY2026, FY2025 and FY2024, with 10 to 12 customers a year; gross margin 6.6% (FY2026)
and 6.3% (FY2025); Item 3.D: "may not be able to compete favorably in our highly competitive industry" (all
`0001213900-26-092307`).

**Bearing on Q3 (capital).** Operating cash negative in FY2024, FY2025 and FY2026 on revenue that did not grow; receivables
rose from $2.08M (FY2023) to $10.03M (FY2025); bank borrowings of about $11M to $12M are drawn and repaid in full each year
(about $42M each way a year).

**Bearing on Q4 (the accounts).** FY2026 net income of $9,063,802 rests on a $23,437,041 unrealized write-up of the stake in
Kaz Resources LLC, the combination counterparty, measured on that counterparty's own later financing rounds (note 6, ASC 321
"observable price change"); without it and the $3,648,265 convertible-note fair-value loss, the year is a loss. FY2026 also
carries an $8,196,074 credit-loss charge on aged receivables, $2,235,000 of stock pay and a $16,593,954 deemed dividend on
the warrant exchange. Material weaknesses in internal control are disclosed (lack of US GAAP staff; no internal audit
function). The FY2026 20-F was filed late (NT 20-F, `0001213900-26-083576`) and amended four days later "to correct certain
clerical data entry errors". The critical-minerals activity is not a segment ("this strategy had not resulted in a new
reportable segment").

**Bearing on Q5 and Q6 (the people, the money, the owners): integrity facts recorded, not judged.**
- 2025-08-27: the same day the founder's company (Supreme Development, beneficially owned by the then chief executive
  Ngo Chiu Lam) sold its 1,995,000 Class B shares (20 votes each) to Quantum Leap Energy LLC, the company used $7,000,000 of
  the new placement's proceeds to retire that founder company's 18,500,000 Class A shares (note 14; 6-K `0001213900-25-080940`).
- Quantum Leap Energy LLC is a subsidiary of ASP Isotopes Inc., of which the executive chairman Paul E. Mann is executive
  director; Mr. Mann is reported as beneficial owner of 6,656,262 Class A held directly, 3,000,000 under his employment
  agreement, and 4,049,794 held by Quantum Leap (Item 7). The Class B shares passed on 2026-03-29 to Dablam LP, which holds
  71.4% of the votes (a "controlled company"); who stands behind Dablam LP was not found in the filings read.
- Issuance in fourteen months: an IPO of 1,725,000 shares at $4.00 (Jan 2025); placements of units at about $0.73 with two
  warrants each (Aug 2025, $17.775M gross) and at about $1.375 (Oct/Nov 2025, $23.885M gross), with 39.6M pre-funded
  warrants; the August warrants exchanged for 47,326,026 Series A preferred at a $16.6M deemed dividend (Jan 2026); Series B
  preferred at $5,000 a share ($32.19M gross, Feb/Mar 2026); $19.575M of convertible notes (Mar 2026); placement-agent
  warrants at each step. Issuance costs took $3.1M of the first $17.8M and $8.0M of the second $23.9M (note 14). The
  company elected home-country practice in place of Nasdaq Rule 5635's shareholder-approval requirements for issuances
  (6-K `0001213900-25-080360`). The row such facts would be read against at Q6 is **[L2014-015]**; not weighed here.
- The executive chairman's award: 3,000,000 Class A vesting quarterly from 2026-01-01, plus, at closing, accelerated vesting
  and a further 3,000,000 Class A (6-K `0001213900-26-049689`).
- The company's cash is being lent to the counterparty before closing: $23,100,000 on 2026-04-22, inside a facility of up to
  $45,000,000 (note 20); the escrow agreement was amended to add "convertible note offerings of up to US$20,175,000 and
  US$23,100,000" (restricted-cash note). The company also holds about 20% of Kaz Resources LLC, bought for $20.0M.
- Turnover: two independent directors resigned in September 2025 and one in April 2026; the founder resigned as director in
  July 2026; the chief financial officer resigned with effect from 2026-06-01 (6-Ks `0001213900-25-088975`,
  `0001213900-26-040172`, `0001213900-26-078143`, `0001213900-26-087516`), each "for personal reasons".
- Promotion in the deal documents: the chairman's "commodity super cycle" forecast (425 `0001213900-26-090751`); the
  target's deck describes its executive as having "grew company from $7M market cap to $1B valuation" (425
  `0001213900-26-087848`).

**Bearing on Q9 (the target's exposures).** The combination requires "no less than US$50,000,000 of net proceeds from the
PIPE Financing remaining available in the bank accounts of SKBL, reduced by any amounts that have or may be loaned by SKBL
to a Kaz Company" (condition (f)); Item 3.D says the facility to Cove Kaz "exposes us to credit and liquidity risks"; the
target's project needs about $1.1 billion of development spending.

## COMPUTATION, NOT A CLEARANCE (Q7 as Part VII's reporting figures; no entry language)
- **Owner cash** (Step 0 table): four filed years, FY2023 to FY2026: 1.5, −6.79, −4.93, −5.35; mean **−$3.89M a year**.
  Before interest (the all-equity basis; interest expense 0.73, 0.89 and 0.77 in FY2024 to FY2026, FY2023 not found): about
  −$3.3M a year. The company's own tax: no carryforward is priced, since the base is negative either way.
- **Growth.** The series changes sign; by specific (b) the halves are compared (FY2023 to FY2024 mean −2.65; FY2025 to
  FY2026 mean −5.14), a decline, and the compound rate is meaningless; the range is the no-growth case alone. Specific (a):
  FY2026 carries the pivot's costs (stock pay $2.24M, legal and professional fees up from $0.18M to $1.92M, marketing
  $0.83M) and FY2024 a $5.0M contract-asset build; on the filer's own description neither is a cyclical peak or trough, and
  with the pivot's costs removed FY2026's operating cash is still negative. Specific (d): the working-capital draws are
  counted. Specific (e): no maintenance guess is separable from capital spending this small. Specific (f): not reached.
- **Net debt, latest filed date (2026-03-31):** bank borrowings $11.98M + overdraft $0.20M + convertible notes $19.575M
  principal − cash $4.63M − restricted cash $46.20M = **net cash $19.07M** (finance leases nil; operating leases left out).
  Subsequent events stated by the filing: the $23.1M loan to Cove Kaz (cash into a receivable), the Reemag interest sold
  for $3.0M (carried $2.98M), the Nevada claims for $0.136M.
- **The range.** No-growth case at 4.519%: −3.3 / 0.04519 = −$73M for the business, plus net cash $19.07M = −$54M; the
  equity-only figure −3.89 / 0.04519 = −$86M. Every case is negative, so **value range nil to nil** against $1.96
  (CONVENTION of this run: a negative case is reported as nil, not as a negative price; rationale: the reporting figure is a
  price, and Q7 gives no rule for a negative value). The floor tested first: no case earns about ten percent at any
  positive price, "there's just a point at which we drop out of the game" **[M2003-149]**, so the computation would close
  OUT whatever the width.
- **Fair price (Part VII):** each end valued at ten percent: −3.3 / 0.10 + 19.07 = −$14M (all-equity basis); −3.89 / 0.10 =
  −$39M (equity-only). **Fair price nil** on both bases, against $1.96.
- **Beside it.** The signed, unclosed combination, valued as if closed on the target's own filed record: the target files
  no statements and has no earnings, so it is credited at nothing (Q7, specific (c)). The stake in Kaz Resources LLC
  (carried $43.18M) pays no dividends and is credited at nothing under Q4's equity-method paragraph. For scale only, not a
  value: the 2026-03-31 net cash of $19.07M is $0.19 a share on the nominal-exercise basis of 101.4M shares and $1.06 on
  the 17.9M ordinary shares; the deal commits it to the venture.
- **Research pass:** none; the box is OUT, not TOO HARD (WORK), and no case earns the floor at the price in any event.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit caf5b9d1); committed after Step 0 (dfe767a9), after Q1 (d673f879)
      and after this close. **Departure, declared:** the filings were read through before Step 0 was written, so the
      sections were written as each closed but the reading was not interleaved with them.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatcher's; the run binds only
      once folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (commit
      subjects about SKK, research-folder names in the status listing, the memory index) is declared under contamination and
      not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` (`Test Runs/_research 2026-10-17 KAZR/check_ids.py`); every
      filing fact has its accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q1 closed the file; everything after it is facts not weighed or COMPUTATION.
- [x] Owner cash from the filed cash-flow statements, stock pay deducted, never a net-income proxy; the HKD sovereign from
      the issuing government's bond programme, dated; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations line); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; the anchor rule does not arise.
- [x] Only the arithmetic lines of `tools/run.py` used; `Screens/cover_shares.py` failed (404) and the counts were taken by hand.
- [x] `python tools/check_framework.py` run before the final commit (result in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) Q1 rules start-ups OUT but does not say what to do with a company whose present business is real and
whose signed, unclosed transaction would turn the share into a start-up while requiring the real business to be sold. Q7's
specific (c) keeps a signed, unclosed deal beside the central figure, which, read alone, suggests Q1 should judge the
legacy contractor and leave the deal aside. I judged what the share is contracted to own, on the company's stated aim and
the closing condition, because the ten-year question **[M2000-037]** cannot be answered for a business the owner has agreed
to sell. One sentence in Q1 saying which governs (the business today, or the business a signed deal makes) would stop two
analysts reaching Q2 on the contractor and OUT on the venture from the same filings. (2) Q7 gives no rule for a negative
range or a negative fair price; this run reported nil and confessed it as its own CONVENTION. (3) The protocol's sovereign
table has no HKD line and Hong Kong issues no 30-year; I used the HKSAR Government's 20-year benchmark from its bond
programme's file, the longest HKD tenor published, and named it; the table could say which tenor stands in.
