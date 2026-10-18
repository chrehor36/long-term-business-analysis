# Company Run — Bimergen Energy Corporation (NYSE American: BESS) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (cf1229a9):** not held; Bimergen Energy (BESS) does not appear in `PORTFOLIO.md`.

**Dispatch:** a blind purchase run dispatched by an unattended overnight cycle under `Screens/_daily/_dispatch_brief.md`,
with the brief's stated departure (the analyst derives the lines of evidence from the 10-K). Working folder
`Test Runs/_research 2026-10-18 BESS/` (`_notes.md`, `rows.py`, `check_cites.py`, the `tools/run.py` output; raw filings in the
ignored `cache/`).

**Contamination, declared and not used.** (1) The session opened with the repository's last five commit subjects in view; two
name other companies' v5 re-runs and their boxes (BLDP, TOO HARD (NATURE) at Q1; AXIAY, OUT at Q7). Neither is this company;
the BLDP line is a closed box at Q1 for another pre-profit energy-technology name, and I declare that it was seen before this
file's Q1 was written, so a reader can weigh whether it primed the routing. (2) The session's git status listing showed
`Screens/WATCHLIST RUN QUEUE.md` as modified and the names of other research folders (AYI, ARCB). (3) The session's memory
index lines describe the queue's state in general terms (wave counts, "57 gate-clearers, nothing buyable"); none names this
company. No blind-listed file was opened, listed or searched; the only listing of `Test Runs/` was a filename filter for
`BESS|bimergen|bitech`, which returned nothing.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $2.21 (close 2026-10-16, the last trading day before this run; `tools/run.py`; an aggregator quote, flagged per
  operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: **7,097,573** common, single class (10-Q for the quarter to 2026-06-30, filed
  2026-08-14, accession `0001493152-26-038439`; `python Screens/cover_shares.py BESS`). Checked: the balance sheet of the same
  10-Q states 7,097,573 shares issued and outstanding, no treasury shares; the S-3/A filed 2026-10-02 (accession
  `0001493152-26-045536`) states 7,097,573 issued and outstanding as of 2026-09-23. Beside the count, from the 10-Q's notes:
  300,000 pre-funded warrants at $0.0001 (the filer counts them in its weighted shares), 3,600,000 public warrants at $5.00,
  underwriter warrants, 1,746,186 options, 57,027 performance restricted shares due to vest in the quarter to 2026-09-30.
  **CONVENTION of this run:** per-share figures use 7,397,573 (the cover count plus the 300,000 pre-funded warrants), because at a
  nominal exercise price they are shares in all but form and the filer's own per-share loss counts them; the cover-count figure is
  shown beside where it matters.
- **Market cap:** $15.7M on the cover count (7,097,573 x $2.21); $16.3M with the pre-funded warrants.
- **Sovereign for the earnings currency:** USD **5.43%**, the 30-year par yield, US Treasury daily par yield curve, 2026-10-16
  (`python tools/sources.py`; the issuing authority).
- **Filings read** (operator rule 4): the 10-K for 2025 (filed 2026-03-31, accession `0001493152-26-014356`: Item 1, Item 1A,
  Item 3, Item 7, Item 9A, the auditor's report, the statements and notes); the 10-Q for the quarter to 2026-06-30 (filed
  2026-08-14, `0001493152-26-038439`: statements, notes 6 to 11, MD&A); the 10-Q for the quarter to 2026-03-31 (filed 2026-05-15,
  `0001493152-26-023798`, fetched, used for the share history only); the 10-K for 2024 (filed 2025-05-30, `0001641172-25-013018`,
  cash flow statement) and for 2023 (filed 2024-04-01, `0001493152-24-012444`, cash flow statement); the final prospectus of the
  February 2026 offering (424B4, filed 2026-02-20, `0001493152-26-007618`: its risk factors and legal proceedings); the S-3/A
  (`0001493152-26-045536`, the share count); the 8-Ks of 2026-05-28 (`0001493152-26-025562`, the Cerberus-affiliated joint
  venture), 2026-07-02 (`0001493152-26-031911`, auditor change), 2026-02-25 (`0001493152-26-008049`, the offering), 2026-05-06
  (`0001493152-26-021523`, the co-chief executives' pay), 2025-10-21 (`0001493152-25-018830`, officer change), 2025-04-15
  (`0001641172-25-004736`), 2025-03-03 (`0001493152-25-008793`) and 2024-07-12 (`0001493152-24-027102`) (three earlier auditor
  changes); the information statement DEF 14C of 2024-10-21 (`0001493152-24-041780`, fetched). **No proxy statement (DEF 14A)
  was found in the filing list from 2024-01-01; the company has acted by written consent and information statement (DEF 14C of
  2024-07-23 and 2024-10-21).** The 10-K omits Item 1A: ‘Smaller reporting companies are not required to provide the information
  required by this item.’ The risk factors read are therefore the 424B4's.
- **One figure cross-checked against the filed statement:** cash at 2025-12-31, $401,203 on the 10-K's balance sheet
  (`0001493152-26-014356`), against 401 (USD thousands) in the `tools/run.py` table. They agree.
- `python tools/run.py BESS`, arithmetic lines only (output kept in the research folder): the tool's owner-earnings window stops at
  2018 because the later years carry no capital-spending tag it reads, so the owner-cash lines below are taken from the filed cash
  flow statements, not from the tool. Its balance-sheet table (2017 to 2025) and its debt line (2025-12-31: 826 thousand of
  short-term borrowings, the related-party loans) were checked against the filed statements.

**Owner cash after every real cost, by year (USD; from the filed cash flow statements; never a net-income proxy):**

| Year | Operating cash flow | Stock pay (options and awards, plus stock issued for services) | Cash spent on project rights (investing) | Owner cash | Source |
|---|---|---|---|---|---|
| 2021 | -162,653 | 111,200 | 25,000 | -298,853 | FY2022 10-K comparative, `0001493152-23-010282` (XBRL transcription, not read in the document; Bitech Mining, the accounting acquirer, from 2021-01-21) |
| 2022 | -789,344 | 0 (none stated) | 0 | -789,344 | FY2023 10-K, `0001493152-24-012444` |
| 2023 | -457,806 | 436,780 (378,559 + 58,221, as restated in the FY2024 10-K) | 0 | -894,586 | FY2024 10-K, `0001641172-25-013018` |
| 2024 | -349,833 | 1,325,391 (1,246,182 + 79,209) | 0 | -1,675,224 | FY2024 10-K, `0001641172-25-013018` |
| 2025 | +878,442 | 2,452,611 (2,285,000 + 167,611) | 1,678,320 | -3,252,489 | FY2025 10-K, `0001493152-26-014356` |
| **Five-year mean** | | | | **-1,382,099** | |
| H1 2026 (beside) | -2,452,475 | 3,877,150 (3,792,000 + 85,150) | 0 | -6,329,625 | 10-Q, `0001493152-26-038439` |

Notes on the lines. The 2025 operating cash flow is positive only because it takes in $3,814,000 of deferred revenue, chiefly a
$3.564M advance from GridSpan that is refundable if financing and milestone conditions are not met by 2027-03-31 (10-Q note 9),
less $1,885,680 of equipment deposits. The 2024 acquisition of Emergen was paid in shares (1,587,300 shares, booked at $22,222,200),
not cash, and brought no operations. There is no depreciation: the company owns no plant. Interest paid is immaterial (interest
expense $17,653 in the first half of 2026) and is not added back for the all-equity figure; said so. The H1 2026 operating cash
excludes $500,000 of joint-venture units received for services (non-cash income, deducted in the reconciliation).

**The balance sheets, 2017 to 2025 and 2026-06-30, read before the income account** **[M2025-032]** (run before Q4 because the
file may close earlier; USD thousands; `tools/run.py` table checked against the filed statements named):
- **2017 to 2020 (Spine Injury Solutions, the former registrant):** assets fall from 3,985 to 285, equity from 2,328 to -248; a
  shrinking medical-services company. **2021:** the reverse acquisition by Bitech Mining resets the history (the accounting acquirer's
  books replace the registrant's; retained deficit moves from -20,279 to -1,097 between the 2021 and 2022 columns because the
  predecessor's deficit drops out, not because anything was earned). **2022 and 2023:** a shell, assets 211 and 163, cash 198 and 152.
- **2024:** assets 23,251, of which 22,222 is one intangible: the development projects, which the 10-K says ‘were assigned to
  Emergen on April 23, 2024, with no cost basis’, and which were booked the next day at the market value of the 1,587,300 shares
  issued for them, at a closing price of $14.00 a share (post-split) on the OTC market (10-K Item 1, `0001493152-26-014356`).
  Equity 21,494 rests almost wholly on that number.
- **2025:** assets 27,200; intangible 23,901 (the 22,222 plus 1,678 paid for two Aggreko project companies); cash 401; vendor
  deposits 1,886; current liabilities 7,837, including deferred revenue 4,758 and related-party loans 826; working capital about
  -4,500; accumulated deficit -9,748. The business could not have paid its current liabilities without the February 2026 offering.
- **2026-06-30:** cash 9,377 after the $13.6M gross offering; receivable 2,847 from the joint venture; intangible 22,883 (1,018 amortized
  into cost of revenue against the Redbird project fees); no borrowings; deferred revenue 3,564; equity 33,082; accumulated deficit
  -11,871.
- **What the figures say:** a company whose only operating asset is a book entry set by its own thinly traded share price; cash has
  come only from selling shares and taking advances on projects; the deficit grows every year. **What they do not say:** what the
  projects are worth; the $126M of contingent development fees owed to a company controlled by the co-chief executive (10-Q note 6)
  are off the balance sheet by design, payable as projects are financed; the GridSpan refund obligation is disclosed and not accrued
  (10-Q note 9). **What they cannot say:** whether any project will be built, at what return.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. **A share is a business:** "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**; this company has funded itself from its first year by selling shares (2022 to 2025 sales of common stock;
the $13.6M offering of 2026-02-20; an S-3 shelf declared effective 2026-10-09, `9999999995-26-003205`), so a closed market would close
its funding, and the answer cannot be yes on the filings. **Who is paid to tell you:** the 10-K's market narrative (Item 1: ‘projected to grow
exponentially, making it a massive and lucrative market’) is the seller's, written in the year it registered shares for sale; "You do not
want to ask an investment banker what he thinks the earnings are going to be in five years of something he’s trying to sell"
**[M2011-083]**, and "you do not get impartial advice from Wall Street [...] when there’s (an) enormous amount of fees possible from one
action" **[M2020-037]**. **The market serves:** the price fell from the $4.00 offering price of February 2026 to $2.21, and "It just tells
us prices" **[M2006-077]**; the fall is no evidence either way. *(Quotation marks: double quotes carry the speakers' words beside their ids; single typographic quotes carry a filing's words.)* **Contrary evidence, written down as found** **[M1997-127]**: (1) an
affiliate of Cerberus Capital Management paid real cash for development work on three of the projects, $3.4M by 2026-06-30 and $3.0M on
2026-07-15, and took them into a joint venture with Bimergen keeping 7.5% (8-K `0001493152-26-025562`; 10-Q note 11), which is
evidence that informed buyers put some value on the pipeline; (2) the quarter to 2026-06-30 showed revenue of $7,903,159 and net income
of $1,628,379, the company's first profitable quarter (10-Q `0001493152-26-038439`); (3) RelyEZ, a battery supplier, funded $10.0M into
the GridSpan joint venture in 2025 (10-Q note 8).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought with cash and sized to a loss of the whole, since the rule binds the
buyer's financing and holding, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**; a
purchase on borrowed money would breach it, "It’s the one thing that forces you [...] or can prevent you from playing out your hand"
**[M2004-065]**. Nothing in the target requires the buyer to post money later.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence, derived from the filing** (the brief's stated departure). From the 10-K's **Item 1**: (a) the stage of the
business; (b) the contracts it holds; (c) how it means to earn (tolling, merchant power); (d) the related-party development-fee
agreement; (e) the industry as the filer describes it. From **Item 7**: (f) the development timeline; (g) liquidity and the dependence on
financing. **Item 1A** is omitted by the filer, so (h) the risk factors are read in the 424B4 of 2026-02-20. Because the 10-K is seven
months old and the business has changed since, (i) what the company actually earned in 2026 is read from the latest 10-Q's notes 6 to 11.

**The facts, line by line** (filing words in single quotes):
- (a) Item 1: ‘We are a development-stage company’; ‘As of December 31, 2025, we have not commenced commercial operations and have not
  generated revenue.’ The BESS business began on 2024-04-24 with the purchase of Emergen Energy LLC, ‘formed on April 4, 2024’, which
  ‘had no operating activity but held the Development Projects’. Before that the registrant was a shell that had been a medical-video
  business (Spine Injury Solutions, to 2022) and a bitcoin-mining venture (Bitech Mining, 2022 to 2024). `0001493152-26-014356`.
- (b) Item 1: ‘to date, we have not entered into any offtake agreements’; ‘Currently we have no binding contracts for our development
  projects.’ The company enters no binding contract on site control, equipment or construction ‘until project-specific financing is
  secured’.
- (c) Item 1: revenue would come from tolling agreements with traders (‘these contracts have not yet been finalized’) or, failing them,
  merchant power sales, where ‘electricity prices can vary significantly’ and the model ‘carries the risk of lower profits or losses when
  market prices drop’.
- (d) Item 1 and 10-Q note 6: Energy Independent Partners, ‘an entity owned or controlled by Mr. Johnson’ (the co-chief executive),
  is owed $0.035 a watt on each project financed, about $126M on the present portfolio, and on a sale ‘the greater of [...] unpaid
  [...] Development Fees [...] or (ii) 62.5% of the proceeds’, with 62.5% of remaining fees accelerating on a change of control or his
  removal.
- (e) Item 1: ‘The Battery Energy Storage Systems (BESS) industry is young’; ‘Despite its emergence as a distinct sector only in the
  2010s’; ‘Advances in battery techs and economies of scale will continue to drive down the costs of BESS’.
- (f) Item 7: ‘Our current project pipeline consists of multiple BESS initiatives, with an estimated development timeline spanning
  eight to nine years.’
- (g) Item 7 and the 10-Q's MD&A: construction is to be financed inside project joint ventures; the company's own operations have been
  funded ‘primarily from equity financing’; ‘There can be no assurance that additional financing will be available’. The 10-K's going-concern
  note says substantial doubt was raised during 2025 and alleviated by management's plans (the February 2026 offering).
- (h) 424B4 `0001493152-26-007618`: ‘we operate in a very competitive and rapidly changing environment’; a change in regulation ‘could
  reduce the competitiveness of battery energy storage’; higher rates or less tax equity ‘could make it difficult [...] to finance’.
- (i) 10-Q `0001493152-26-038439`, notes 7 and 11: the first revenue, $7.9M in the quarter to 2026-06-30, is development fees and
  expense reimbursements from contributing three projects to a Cerberus-affiliated joint venture (for 7.5% of it), plus a $943,500
  deposit on a 2024 solar-project sale recognised because the buyer made no progress in two years. That is a developer selling project
  rights, not the operator Item 1 describes.

**The tests.**
1. **Where will it be in ten years?** "You’re trying to print the next 10 years of Value Line in your head." **[M1999-132]**. There is no
   operating page to extend: no project built, none financed, none contracted, and the filer's own pipeline takes eight to nine years.
   Understanding is "a pretty good idea where it’s going to be in ten years" **[M1997-021]**; the filings give no such idea.
2. **The key variables, and how predictable are they?** "evaluating how predictable they were first, because that is the first step. If
   something is not very predictable, forget it." **[M1998-044]**. The variables are: whether each project wins interconnection, land,
   permits and financing; the price of an offtake contract or, without one, the spread between cheap and dear hours in ERCOT, PJM, MISO
   and the West; the cost of batteries, which the filer says keeps falling; and the share of every project's value that goes to the
   co-chief executive's company before owners. None can be read from a filing, because none has yet happened once.
3. **Do the past statements tell the future ones?** "do I understand enough about this business so that the financial statements will
   tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look like"
   **[M2008-033]**. The past statements are of three different businesses; the only BESS income so far comes from selling projects, which
   Item 1 does not describe as the business.
4. **Important and knowable?** "If something’s important but unknowable, forget it." **[M2006-076]**. Whether these projects are built, and
   at what return, is the whole of the value and is unknowable today.
5. **Would the insiders write it down?** The filer says its ‘pro forma models and financial practices meet customary industry standards
   to estimate, calculate and project these revenues’, so a forecast exists; it is the seller's, written while it sells shares, and the rows
   say not to take it: "You do not want to ask an investment banker what he thinks the earnings are going to be in five years of something
   he’s trying to sell." **[M2011-083]**.
6. **Can I name the winner, not just the industry?** "there’s industries we know that may have a wonderful future, but we don’t have the
   faintest idea who the winners will be" **[M2012-067]**; "Just because Charlie and I can clearly see dramatic growth ahead for an
   industry does not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for
   supremacy." **[L2009-005]**. The filer's case is industry growth; it names no rival and shows no cost or position against one.
9. **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.

**What it rules OUT, applied.** The framework's Q1 list of what it rules OUT opens with start-ups: "Start-ups are not our game."
**[L2007-015]**; "I say, “We don’t do startups.” They don’t exist. Well, if you blot out startups, there’s a whole layer of complexity that
goes out of your life." **[M2008-088]**. Bimergen is a start-up on its own filing: a ‘development-stage company’ that ‘ha[s] not commenced
commercial operations’, whose business was bought as a portfolio of rights from an entity formed twenty days earlier. The 1998 charter is
a corporate shell's date, not the business's; the business is two and a half years old and has no project in operation. The rows give the
start-up as a category refused outright, not as a business they cannot value, which is why the framework lists it under OUT while it sends
fast-moving technology to TOO HARD.

**The alternative reading, considered and not chosen.** The same facts would support TOO HARD (NATURE): "This kind of uncertainty
frequently occurs when new businesses and rapidly changing industries are under examination. In cases of this sort, any capital
commitment must be labeled speculative." **[L2000-026]**; "a business that must deal with fast-moving technology is not going to lend
itself to reliable evaluations of its long-term economics." **[L1993-023]**; the filer itself calls the field ‘young’ and ‘rapidly
changing’ and expects battery costs to keep falling. I choose OUT because the framework's text names the start-up specifically and places
it under OUT, and the more specific placement governs the general one; the routing question is reported under WHAT IN THE FRAMEWORK WAS
WRONG OR UNCLEAR. On either box the file closes here, and a lower price does not reopen it: "It doesn’t mean it isn’t a good buy. It
doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**.

**VERDICT: OUT** at Q1: a start-up with no operating project, no binding contract and no offtake (10-K Item 1,
`0001493152-26-014356`), which the rows refuse by category **[L2007-015]**, **[M2008-088]**; the ten-year economics cannot be foreseen
from its filings **[M1997-021]**, **[M1998-044]**. Q2 to Q12 NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (closed at Q1). The 10-K names no competitor: Item 1 has no competition section and Item 1A is omitted, so no rival
filings were read and no comparator was chosen (see AFTER THE STOP).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0; the accounts facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts were found and are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback line needs no write-back: the company has bought back no shares.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The range and the fair price are computed below under COMPUTATION, NOT A CLEARANCE, at the owner's request.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q1** (can I understand it): a start-up on its own 10-K, with no operating project, no binding contract and no offtake
**[L2007-015]**, **[M2008-088]**; the TOO HARD (NATURE) reading was considered and not chosen (Q1). **Integrity facts recorded, not
judged.** COMPUTATION, NOT A CLEARANCE: value range -$2.17 to -$1.33 a share (all-equity, no-growth cases, at 5.43%) against $2.21.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2. Each with its source **[M1997-127]**.)*

**Bearing on Q2 (the castle).** The 10-K names no rival and has no competition section (Item 1; Item 1A omitted,
`0001493152-26-014356`). The only comparison it makes is with the industry's growth. The 424B4 calls the environment ‘very competitive
and rapidly changing’ (`0001493152-26-007618`). The company builds nothing itself: ‘the Company and its subsidiaries do not have the
in-house personnel to construct these projects’ (10-K Item 1). The buyer of three of its projects (the Cerberus-affiliated joint venture)
agreed to pay about $5.7M of development fees and $3.2M of accountable expenses, of which $2.5M is contingent on one project reaching
notice to proceed (10-Q note 11, `0001493152-26-038439`).

**Bearing on Q3 (capital).** The pipeline's construction is to be financed at project level, by joint ventures, tax equity and project
debt, ‘non-recourse to the Company’ (10-Q MD&A); the GridSpan joint venture's project companies are to be owned 80% by RelyEZ and 20% by
Emergen until refinancing, with Emergen liable for up to $5.0M of capital calls (10-Q note 8). The company would own a minority of each
project financed that way.

**Bearing on Q4 (the accounts).**
- The $22,222,200 intangible was booked at the market value of 1,587,300 OTC-quoted shares ($14.00 post-split) for project rights that
  had been assigned to Emergen the day before ‘with no cost basis’ (10-K Item 1). It is called indefinite-lived and not amortized, yet
  $1,017,811 of it was relieved into cost of revenue in the quarter to 2026-06-30 against the Redbird fees (10-Q note 11 and cash flow).
- The 2023 figures were restated between filings: net loss $811,693 in the FY2023 10-K (`0001493152-24-012444`), $920,418 as the
  comparative in the FY2024 10-K (`0001641172-25-013018`); stock pay $328,055 became $436,780.
- Material weaknesses in internal control at 2025-12-31, among them inadequate segregation of duties and an ‘Insufficient number of
  personnel with an appropriate level of U.S. GAAP knowledge’ (10-K Item 9A).
- A critical audit matter on the RelyEZ, GridSpan and Aggreko arrangements, ‘especially challenging and subjective auditor judgment due to
  the number of interrelated agreements’ (10-K auditor's report).
- The 2025 operating cash flow of +$878,442 rests on a $3.564M GridSpan advance that is refundable if financing and milestone conditions
  are not met by 2027-03-31; management judges the loss remote and accrues nothing (10-Q note 9).
- The 7.5% joint-venture stake is carried at a ‘provisional amount’ of $500,000, booked as units received for services (10-Q note 11 and
  cash flow).
- The 2024 solar-project deposit of $943,500 was recognised as revenue in 2026 ‘because none of contractual milestone conditions had been
  met over the last two years’ (10-Q MD&A).
- Five engagements of auditors in two years: Fortune CPA dismissed 2024-07-08 for Farber Hass Hurley; FHH dismissed 2025-02-26 and Fortune
  re-engaged; Fortune dismissed 2025-04-11 for RJI CPAs, Fortune having ‘reviewed and responded with edits that were incorporated in the
  final 8-K but did not provide such letter’; RJI terminated 2026-06-30 for Weinberg & Company (8-Ks `0001493152-24-027102`,
  `0001493152-25-008793`, `0001641172-25-004736`, `0001493152-26-031911`). Each 8-K reports no disagreements.
- Late filings: NT 10-Q 2024-08-14, NT 10-Q/A 2025-03-26, NT 10-K 2025-03-31, NT 10-Q 2025-05-15 (EDGAR filing list). The FY2024 10-K was
  filed 2025-05-30.

**Bearing on Q5 (who runs it): integrity facts, recorded, not judged.**
- The co-chief executive and president, Cole Johnson, sold the project portfolio to the company through his holding company C&C Johnson
  Holdings for 1,587,300 shares, about 31.3% of the company (10-K Item 1). A condition that at least $50M of capital be committed before
  closing ‘was negotiated out of the acquisition definitive agreement’ (10-K Item 1).
- His company Energy Independent Partners is owed development fees of $0.035 a watt on every project financed, about $126M on the present
  portfolio; on a sale, the greater of unpaid fees or 62.5% of the proceeds; and 62.5% of the remaining fees on a change of control or on
  his removal (10-K Item 1; 10-Q note 6). On the Redbird transaction EIP earned $1.0M after offering to cut a $3.5M fee by $2.5M (10-Q
  note 6).
- In May 2024 Emergen sold 2.425 GW of solar projects for up to $19.4M to Bridgelink Development, whose sole member is C&C Johnson Holdings
  (10-K Item 1); EIP was paid $250,000 in 2024 and $339,688 in 2026 out of the $943,500 deposit and is due 62.5% of the proceeds; in 2026
  the company recognised the deposit as revenue because no milestone had been met in two years (10-Q note 7 and MD&A).
- The co-chief executives' base salaries were raised to $425,000 each from 2026-04-01 on five-year terms, with milestone bonuses (8-K
  `0001493152-26-021523`). Performance restricted shares vest on the uplisting to a national exchange, not on a business result; $2,165,000
  was recognised for them in the first half of 2026 (10-Q note 5).
- Item 3 of the 10-K says there are no material legal proceedings ‘except as provided below:’ and nothing follows. The company itself won a
  default judgment in 2025 against former licensors of the bitcoin-mining venture, on claims including fraud, and cancelled 1,287,694
  shares (424B4, legal proceedings).
- No proxy statement found from 2024-01-01; shareholder actions by written consent (DEF 14C of 2024-07-23 and 2024-10-21).
- Each of these is a filed fact; none is weighed here. Any later run that reaches Q5 must answer them **[M2013-088]**.

**Bearing on Q6 (the money and the owners).** Shares outstanding went from 3,930,906 (2025-12-31) to 7,097,573 (2026-06-30) through the
$4.00 offering of 3.1M shares, 0.3M pre-funded warrants and 3.6M warrants at $5.00 (8-K `0001493152-26-008049`); an S-3 shelf was declared
effective on 2026-10-09 (`9999999995-26-003205`). The Emergen purchase was paid wholly in shares. No buyback and no dividend.

**Bearing on Q9 (exposures).** No borrowings at 2026-06-30 (related-party loans of $825,700 repaid). Contingent: the $3.564M GridSpan
refund to 2027-03-31; up to $5.0M of GridSpan capital calls; a parent-company guarantee to GridSpan and RelyEZ; a capital contribution had
the third Cerberus project not been acquired (it was, on 2026-07-15) (10-Q notes 8, 9, 11).

## COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price, at the owner's request
*(The file closed at Q1. No figure here is a verdict or entry language, operator rule 3. Arithmetic in
`Test Runs/_research 2026-10-18 BESS/q7_computation.py`.)*
- **Cash input:** owner cash after every real cost, five-year mean 2021 to 2025, **-$1,382,099** a year (Step 0 table). Negative in every
  year.
- **Growth:** a compound rate between negative end years is meaningless; the first-half and second-half means (-$544,099 for 2021 and 2022,
  -$2,463,857 for 2024 and 2025) are both negative, so that measure is meaningless too; by specific (b) the range is the **no-growth case
  alone**, said so. No cap (f) is needed.
- **Growth spending (e):** the only investing outlays are project rights ($25,000 in 2021, $1,678,320 in 2025). They bought no growth the
  filings can credit, so by (e)'s inversion the maintenance-only no-growth case is the top and the all-spending case the bottom: top
  -$1,041,435 a year, bottom -$1,382,099.
- **Cycles (a):** the window's first three years are other businesses (a reverse acquisition, after which the filer calls its predecessor's
  results ‘not pertinent’); shown beside: the BESS-era base, 2024 and 2025.
- **Acquisitions (c):** Emergen (2024) was paid in shares, a merger in the speakers' usage; it had no operations, so the combined averages
  are the filer's own and its shares are in the count. The Cerberus contribution closed after the window and before the price date; its
  filed record shows no earnings of the joint venture, so the 7.5% stake is credited at nothing; the $2.5M Redbird fee contingent on notice
  to proceed is not counted; the July 2026 receipts are operating cash, not financing, and are left out of net debt.
- **Working capital (d):** counted (it is inside operating cash flow; 2025's GridSpan advance is a draw the filer ties to one arrangement,
  and removing it would lower the 2025 figure by $3.564M, which would only widen the negative).
- **Net debt:** cash $9,377,141, borrowings and finance leases nil at 2026-06-30 (10-Q); net cash $9.38M; the operating lease is left out,
  said so. No subsequent financing event is stated in the 10-Q.
- **Floor first:** no case of the range is positive, so no case earns the floor of about ten percent at any positive price; this alone would
  close Q7 OUT whatever the width. The three-to-one width test has no meaning on a negative range.

| Figure | All-equity basis (central) | Equity-only (beside) |
|---|---|---|
| **VALUE RANGE** at the 5.43% sovereign, no-growth cases, per share on 7,397,573 | **-$2.17 (all spending) to -$1.33 (maintenance only)** | -$3.44 to -$2.59 |
| same, on the cover count of 7,097,573 | -$2.26 to -$1.38 | |
| **FAIR PRICE** (each end valued at ten percent, the two averaged, Part VII) | **-$0.37** a share | -$1.64 a share |
| Beside: BESS-era base 2024 and 2025, range | -$4.87 to -$2.78 | -$6.13 to -$4.04 |
| Beside: BESS-era base, fair price | -$1.50 | -$2.76 |
| Price | $2.21 (2026-10-16, aggregator) | |

Tax: the company has paid no income tax (losses); owner cash is taken as filed, with no carryforward shelter priced, since a shelter is
worth nothing to a stream with no taxable income in it. The negative values say the owner cash shown consumes capital in every case; they
are what the arithmetic gives, not a forecast of where the shares will trade, and the net cash would be spent long before such a stream
could run forever.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `ef9736a1`); written question by question; committed after Step 0, after Q1, and
      after this closing section (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked by me, by the
      brief); the run binds nothing until folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the one listing of `Test Runs/` was a filename
      filter for this company's names, which returned nothing. What was seen by accident is declared under Contamination at the top.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (`check_cites.py`: 0
      problems); every filing fact has its accession; the filing quotations were matched against the downloaded text.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; the figures after it are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost from the filed cash flow statements (stock pay deducted, project-rights spending deducted), never a
      net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote. One exception confessed: the 2021 line
      is an XBRL transcription of the FY2022 10-K comparative, not read in the document.
- [x] Contrary evidence written down as found (Foundations); facts for later questions are under AFTER THE STOP, with the integrity flag in
      the box line.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text was not read as rule.
- [x] `python tools/check_framework.py` PASS before the final commit (recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Q1's routing for a start-up is unclear. The framework lists start-ups under Q1's list of what it rules OUT, on two rows (L2007-015 and M2008-088, cited in Q1 above), yet
section I describes Q1's failing box only as TOO HARD (a business whose economics cannot be foreseen), and the corrections of 2026-10-04,
2026-10-05 and 2026-10-10 moved fast-moving technology, unnameable winners and businesses that live on invention out of the OUT lists and
into TOO HARD because the rows give ignorance as their reason. A pre-revenue developer in a young, changing field meets both descriptions,
so two analysts could close it OUT or TOO HARD (NATURE) on the same facts. I chose OUT because the start-up item is the more specific
placement and its rows refuse the category outright rather than confess an inability to value; the text should say which governs. Two
smaller gaps: (1) Q7's specific (e) and the no-growth-alone rule of (b) meet awkwardly when every year's owner cash is negative: (e) forbids
charging all spending while capping growth, but (b) forces zero growth, so I applied (e)'s inversion clause by analogy, the maintenance-only
case as the top and the all-spending case as the bottom; (2) the template asks for "the proxy", and a company that acts only by written
consent and information statement has none; the run says so rather than counting a DEF 14C as a proxy.
