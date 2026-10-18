# Company Run — BioLargo, Inc. (OTCQX: BLGO) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (52884432): not held; `PORTFOLIO.md` has no line for BLGO, BioLargo or NuWay.*

**Dispatch:** a dispatched blind run under `Screens/_daily/_dispatch_brief.md` (operator rule 10). The brief departs from
the canonical brief in one place, which it states: it lists no lines of evidence, and this run derives them from the
latest 10-K (below, Step 0).

**Contamination, declared and not used.** (1) At the start of the session the harness showed the repository's git status
and its five most recent commit subjects; they name another company's run (SHIM) and research folders of other
companies (AYI, ARCB, by folder name only). Nothing in them concerns BioLargo. (2) The session's memory index, loaded by
the harness, carries queue counts and the names of other files; nothing in it concerns BioLargo. (3) Before any fetch I
ran one filename listing of `Test Runs/` filtered on "BLGO" or "biolargo" to make sure the dated run file did not already
exist; it returned no file, so no content was seen. That listing is itself a search of `Test Runs/` by the company's name,
which the blind rule forbids; it is declared here as a breach of form with nothing learned.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.07 (close 2026-10-16; aggregator quote via `tools/run.py`, cross-read against a second aggregator's weekly
  closes, which run from $0.15 in April 2026 to $0.07 on 2026-10-16; **aggregator, flagged per operator rule 5**).
- **Shares by class** from the latest filing's cover: 328,731,362 common, one class (10-Q for the quarter to 2026-06-30,
  filed 2026-08-14, accession `0001437749-26-028023`; `python Screens/cover_shares.py BLGO`). Cross-checks: the balance
  sheet of the same 10-Q shows 325,231,362 shares issued at 2026-06-30, and the 10-Q's subsequent-events note states
  3,500,000 shares sold to Clearthink after the quarter, which accounts for the difference (325.23M + 3.5M = 328.73M); the
  company holds no treasury shares on the face of the balance sheet. No 8-K after the 10-Q bears on the count (the only one,
  `0001437749-26-030124` of 2026-09-11 and its amendment `0001437749-26-030198`, furnish an investor slide deck under
  Item 7.01). The Clearthink line remains open (up to $10.0M of stock over 36 months, 8-K `0001437749-26-009813`), so the
  count is rising.
- **Market cap:** 328.73M × $0.07 = **$23.0M**.
- **Sovereign for the earnings currency (USD):** 5.43%, the 30-year par yield of the US Treasury daily par yield curve,
  dated 2026-10-16 (issuing authority; read by `tools/run.py` through `tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-03-04, accession `0001437749-26-006926` (Items 1, 1A in part, 3, 5, 7, 8: balance sheet,
    operations, cash flows, notes on going concern, noncontrolling interests, leases, Pooph).
  - 10-K/A for FY2025, filed 2026-04-30, accession `0001437749-26-014184` (Part III only: directors, pay, ownership; it
    states it was filed because no proxy would be filed within 120 days).
  - 10-Q for the quarter to 2026-06-30, filed 2026-08-14, accession `0001437749-26-028023`; 10-Q for the quarter to
    2026-03-31, accession `0001437749-26-017391` (downloaded, read only for the count).
  - 10-Ks for FY2024 (`0001437749-25-010172`), FY2023 (`0001437749-24-010394`), FY2022 (`0001437749-23-008876`) and
    FY2020 (`0001437749-21-007650`), for the segment results and cash flows 2019 to 2024.
  - 8-K of 2025-09-25 (`0001437749-25-029852`, Items 1.02 and 2.06: the Pooph termination and the expected impairment);
    8-K of 2026-03-25 (`0001437749-26-009813`, Items 1.01 and 3.02: the Clearthink purchase agreement); 8-K of 2026-09-11.
  - Proxy: the last definitive proxy is DEF 14A of 2025-04-25 (`0001437749-25-013006`), downloaded; the FY2025 Part III
    in the 10-K/A was read in its place as the later document.
- **One figure cross-checked against the filed statement:** net cash used in operating activities for FY2025, $(8,297)K,
  is the XBRL figure `tools/run.py` and the companyfacts series carry, and is the line printed on the filed consolidated
  statement of cash flows of `0001437749-26-006926` ("Net cash used in operating activities ( 8,297 )"). They agree.
- `python tools/run.py BLGO`, arithmetic lines only: the tool's owner-earnings window ended at 2017 because capital
  spending and depreciation were not tagged under the elements it reads for later years; its table was not used for owner
  cash. Owner cash below is built from the filed cash-flow statements (`q7_computation.py` in the research folder):

  | FY | OCF as filed | option expense | stock issued for services | equipment (and patent) purchases | **owner cash** |
  |---|---|---|---|---|---|
  | 2019 | (4,422) | 1,522 | 710 | 35 | **(6,689)** |
  | 2020 | (4,154) | 2,459 | 666 | 23 | **(7,302)** |
  | 2021 | (3,937) | 1,872 | 367 | 34 | **(6,210)** |
  | 2022 | (2,762) | 2,071 | 291 | 271 | **(5,395)** |
  | 2023 | (2,365) | 2,124 | 384 | 478 | **(5,351)** |
  | 2024 | (3,206) | 2,063 | 416 | 1,235 | **(6,920)** |
  | 2025 | (8,297) | 2,965 | 648 | 46 | **(11,956)** |

  USD thousands; sources the FY2020, FY2022, FY2023, FY2024 and FY2025 10-Ks named above. Five-year average (2021 to 2025)
  **$(7,166)K** after interest; before interest (interest paid added back: 99, 36, 58, 33, 344) **$(7,052)K**. Stock pay is
  resolved and complete: option expense plus common stock issued for services; no other stock-pay line found in the
  statements read. Depreciation was 145 (2025) and 155 (2024) against equipment purchases of 46 and 1,235. Operating cash
  flow was negative in every year from 2014 to 2025 in the companyfacts series, and in the first half of 2026, $(5,973)K
  (10-Q `0001437749-26-028023`).

- **The lines of evidence this run chose, and why** (the brief lists none; derived from the FY2025 10-K, Items 1, 1A
  and 7): (1) the segments and their results 2019 to 2026, because the company reports six operating units with different
  economics and only one has ever earned a profit; (2) the customer concentration and the Pooph relationship, because one
  private-label customer was 50% of revenue in 2022, 82% in 2023 and 77% in 2024 (the FY2023 and FY2024 10-Ks) and ended in
  2025; (3) the competitors the 10-K names; (4) going concern, cash burn and financing, because the 10-K and both 2026 10-Qs
  carry a going-concern paragraph; (5) share issuance and its prices, because the share count rose about fourfold in eleven
  years; (6) the minority interests and the subsidiaries' own financing (Clyra Medical, BLEST, BETI), because the
  subsidiaries raise outside money at their own level, guaranteed by the parent; (7) litigation (Pooph, both directions);
  (8) pay and ownership from the 10-K/A. Not chosen: acquisitions and goodwill (no acquisition found in the years read; no
  goodwill on any balance sheet read; intangible assets of $1.9M to $2.2M in 2018 to 2020 are nil from 2021), pricing (no price
  disclosure found beyond the cost-of-goods percentages).

- **The balance sheets, read first** (the file closes before Q4, so they are read here, as the template asks;
  **[M2025-032]**). Ten year-ends from `tools/run.py`'s first-filed XBRL vintages, the last two checked against the filed
  statements (USD thousands):

  | year-end | assets | liabilities | equity (parent) | cash | receivables | accumulated deficit |
  |---|---|---|---|---|---|---|
  | 2017 | 1,495 | 4,905 | (4,104) | 990 | 94 | (101,205) |
  | 2018 | 3,185 | 4,308 | (1,496) | 655 | 257 | (111,723) |
  | 2019 | 3,621 | 5,801 | (2,153) | 655 | 355 | (123,492) |
  | 2020 | 4,942 | 5,177 | 3,858 | 716 | 484 | (132,041) |
  | 2021 | 3,023 | 2,090 | 4,653 | 962 | 513 | (139,121) |
  | 2022 | 4,858 | 2,847 | 4,878 | 1,851 | 1,064 | (143,594) |
  | 2023 | 8,205 | 4,003 | 6,844 | 3,539 | 2,612 | (147,098) |
  | 2024 | 10,513 | 4,457 | 8,851 | 3,548 | 3,168 | (149,500) |
  | 2025 | 8,311 | 6,785 | 4,042 | 3,883 | 615 | (161,280) |
  | 2026-06-30 | 6,669 | 9,399 | (1,852) | 2,188 | 724 | (166,333) |

  What the figures say: the accumulated deficit grew by $65M over the nine and a half years, and equity was kept above zero
  only by paid-in capital, $165.3M at FY2025 (`0001437749-26-006926`); at 2026-06-30 the parent's equity is a deficit of
  $(1,852)K and total equity, after a noncontrolling interest of $(878)K, a deficit of $(2,730)K (`0001437749-26-028023`).
  Receivables rose with the Pooph sales (to $3,168K in 2024) and fell to $615K when Pooph stopped paying; $3,849K of
  receivable and note were written off in 2025 as a credit loss. There is no goodwill; the intangibles of 2018 to 2020 are
  gone. Debt is small at the parent ($252K at 2026-06-30) and growing in the subsidiary Clyra Medical, $4,854K carried at
  2026-06-30 against $1,814K at FY2025, at 15% interest, guaranteed by BioLargo; with finance leases of $311K, debt is
  $5,417K against cash of $2,188K. What they cannot say: what the patents and the subsidiaries' technologies are worth, since
  none is carried at a cost that tells it.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own it "if the market closed for five years"
**[M1997-109]**. For BioLargo the question is sharp, because the company has funded its operations by selling stock in
every year read, through Lincoln Park to February 2026 and Clearthink from April 2026; an owner of the business with the
market closed would be an owner of a business that could not, on its own filings, pay its way ("We do not believe gross
profits in the year ending December 31, 2026 will be sufficient to fund our current level of operations", 10-K
`0001437749-26-006926`). The analyst's habits bear most: look for "what’s wrong in things" and "what you’re missing"
**[M2025-013]**, and avoid "the worst anchoring effect, which is always your previous conclusion" **[M2016-054]**; the
company's own descriptions of its technologies ("best-in-class", "number-one performing") are the seller's projection and
are not evidence. **Contrary evidence, written down as found** **[M1997-127]**: (a) ONM Environmental did earn operating
income of $1,130K, $4,335K and $5,920K in 2022 to 2024, a 38% operating margin in 2023 and 2024, so the technology sold
something people paid for; (b) BLEST's third-party service revenue nearly doubled in 2025 to $1,998K and rose again in the
first half of 2026; (c) the patent suit against Pooph, if won, could return royalties and damages ($1,667,292 and
$2,154,110 claimed) and an injunction; (d) Clyra Medical received its first purchase order in February 2026 and booked
$154K of revenue in the first half. Each is weighed where it bears.

## THE STANDING RULE
The buyer's own conduct: the rule is "never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]** and "Never risk permanent loss of capital." **[L2023-005]**. A part-interest bought for cash, without
borrowed money and sized so that its loss to zero could be borne, does not put the buyer at risk of ruin; nothing in this
business can call on its shareholders for money (no partly paid shares, no guarantee by holders). The rule does not decide
the file. It is noted that a total loss of what is paid is a live outcome for this business on its own going-concern
paragraph, so the sizing half of the rule would bind hard if the file ever reached Q10.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the industry"
  **[M2011-014]**; the first step is "trying to identify the key variables in that particular business, and evaluating how
  predictable they were first" **[M1998-044]**.
- **The parts, and which part decides.** The 10-K reports six operating units with different economics (Item 1 and the
  segment note, `0001437749-26-006926`). Under Q1's holding-company paragraph and Q2's business-of-parts convention, a part
  "matters" and decides when it carries more than half of five-year operating profit, or else is the largest. Segment
  results 2021 to 2025, from the five 10-Ks' MD&A (USD thousands; ONM is operating income; the others are the filer's
  segment net income or loss, the only figure printed for every unit in every year):

  | part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum |
  |---|---|---|---|---|---|---|
  | ONM Environmental (odor control) | (511) | 1,130 | 4,335 | 5,920 | (2,317) | **8,557** |
  | BLEST (engineering, 70% owned) | (629) | (425) | (1,619) | (1,356) | (1,032) | (5,061) |
  | Clyra Medical (48% owned) | 593 | (1,412) | (2,097) | (3,490) | (6,564) | (12,970) |
  | BioLargo Canada / Water (research) | (566) | (604) | (713) | (504) | (528) | (2,915) |
  | BETI (battery, 95% owned) | n/a | n/a | (1,179) | (642) | (639) | (2,460) |
  | BEST (water equipment) | n/a | n/a | n/a | (273) | (276) | (549) |
  | corporate | (5,781) | (3,995) | (3,369) | (4,033) | (3,923) | (21,101) |

  The company's five-year operating result is a loss of $(35,592)K (companyfacts, OperatingIncomeLoss, the five 10-Ks), so
  "more than half of five-year operating profit" has no meaning here; ONM is the only part with a profit and the largest by
  profit, and the 2026 10-Q says so itself: "Other than ONM Environmental, none of our operating business units have operated
  at a profit" (`0001437749-26-028023`, segment note). **ONM decides.** The threshold's failure on a loss-making whole is
  recorded under What was wrong or unclear.
- **ONM's economics, read from the filings.** ONM sells a copper-based odor-control liquid (CupriDyne Clean) and the misting
  systems that deliver it, to landfills, transfer stations and municipalities, "a significant portion" of it under contracts
  with cities and counties in Southern California; and it sold the same chemistry, made by contract manufacturers, to
  private-label marketers at "an agreed-upon manufacturing margin" plus, from Pooph, "a six percent royalty" (10-K FY2025,
  Item 1). The key variables are two: the volume a private-label marketer buys, and the industrial book of landfill and
  municipal contracts. Both can be read from eight years of filings: the industrial book alone produced ONM revenue of
  about $1.5M in 2019 to 2021 (FY2020 and FY2022 10-Ks: $1,554K in 2020, $1,512K in 2021) and a loss each year; the
  private-label volume rose and fell with one customer. Odor control for landfills is not a field of fast technical change in
  anything the filings say; the product does not depend on a technology that "could hurt the business as it presently exists"
  **[M1998-008]**.
- **What is not understood, and why it does not decide here.** The non-deciding parts are a liquid-sodium battery with no
  revenue (BETI), a PFAS water system with one municipal installation (BEST and BLEST), and a wound-care start-up with its
  first $154K of sales (Clyra). These are start-ups and technologies whose ten-year economics no insider would write down;
  "Start-ups are not our game." **[L2007-015]**. Under the parts convention they do not decide; they are carried and noted,
  not judged here.
- **The doubt rule.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
  The doubt I hold about ONM is not whether its economics can be read but what they show; that is the castle question, and
  Q2 owns it. The answer at Q1 is therefore IN, narrowly, on the deciding part.
- **VERDICT: IN** (on ONM Environmental, the deciding part; the business as a whole would be TOO HARD if the start-ups
  decided, which by the convention they do not) **[M2012-065]**, **[M2011-014]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**. The deciding part is ONM Environmental (Q1). ONM has two castles to test: the
consumer private-label channel, which made all of its five-year profit, and the industrial odor book, which is what is left.

- **The parts table** (section B convention; five-year sums from Q1's table):

  | part | five-year result (USD K) | castle | decides |
  |---|---|---|---|
  | ONM Environmental | +8,557 operating income | open (below) | **yes**: the only part with a profit, the largest by profit |
  | BLEST | (5,061) | an engineering-services shop; no castle found in the filings | no |
  | Clyra Medical | (12,970) | a start-up; its future cannot be judged | no |
  | BioLargo Canada | (2,915) | a research unit funded by grants and the parent | no |
  | BETI | (2,460) | a pre-revenue battery against lithium-ion makers; cannot be judged | no |
  | BEST | (549) | pre-revenue water equipment | no |

- **The castle tests, each with its filing fact.**
  1. *What keeps it standing, and how permanent is it* **[M1995-038]**. ONM's profit years were made by one customer: Pooph
     was "almost 50%" of company revenue in 2022, 82% in 2023 and 77% in 2024 (FY2022 to FY2024 10-Ks), and ONM's
     operating income rose and fell with it ($1,130K, $4,335K, $5,920K, then $(2,317)K). The company wrote in two
     consecutive 10-Ks that it had "no way of determining whether ONM Environmental will have an operating income in the
     current year" (FY2023 `0001437749-24-010394`, FY2024 `0001437749-25-010172`). A profit that the business itself could
     not see a year ahead had no permanent reason under it.
  2. *The money test, and the attacker* **[M2011-015]**. The attacker was the customer. On 2025-09-19 Pooph wrote that "it
     has been working to independently develop a new formula for Pooph-branded products", that "it will no longer be ordering
     products from BioLargo", and that "it will not be accruing future royalty obligations" (8-K `0001437749-25-029852`, Item
     1.02). Pooph is a private marketer, not a large company; within about four years of the 2021 agreement it replaced the
     product it had been buying. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. "one competitor is
     frequently enough to ruin a business" **[M2012-108]**.
  3. *The brand in the customer's mind, and who owns it* **[M2023-073]**, **[M2019-041]**. The consumer asked for Pooph, a
     brand BioLargo never owned: "Because Pooph is owned and marketed by a third party, ONM Environmental has no control over
     the marketing and sales activity or levels of the Pooph brand" (10-K FY2025, MD&A). The speakers' test is whether the
     customer will "ask for you by name" **[M2023-073]**, and they name the brand as "our protection against the
     intermediaries making all the money" **[M2019-041]**; here the brand sat with the intermediary, and when the
     intermediary found another formula the value went with the brand, as the rows say it does "to the extent that people
     trust" the seller's name as much as the product's **[M2001-090]**. ONM's consumer products under its own name are not
     shown as material in any filing read.
  4. *Would the customer still choose it over the low bid* **[M2017-009]**. The one customer who mattered chose its own
     formula over a licence that cost it a manufacturing margin plus a six percent royalty. The industrial customers are
     municipalities and waste companies buying on contracts (Item 1); no filing read shows a price premium held or raised.
  5. *Gained fast, lost fast.* ONM's profit rose from a loss in 2021 to $5.9M in 2024 and back to a loss in 2025: "if
     something can gain competitive advantage very quickly, you have to worry about them losing it quickly, too"
     **[M2002-050]**.
  6. *Widening or narrowing, and what could destroy it* **[M1999-108]**. It narrowed to nothing in one year: ONM revenue
     fell 62% in 2025 to $5,905K and 81% in the first half of 2026 to $895K, with an operating loss of $(204)K
     (`0001437749-26-028023`). The patents are the remaining wall: 34 issued, "our patents have an average remaining duration
     of seven years" (10-K FY2025, Item 1), less than the ten-to-twenty-year span the question asks about, and their reach
     over Pooph's new formula is the subject of a suit filed 2025-11-11 and unresolved (10-Q, legal proceedings).
- **The industrial castle, standing alone.** Before Pooph and after it, ONM's industrial book lost money in every period
  read: 2019 segment loss $(337)K on revenue of about $1,459K; 2020 $(483)K on $1,554K (FY2020 10-K `0001437749-21-007650`);
  2021 operating loss $(511)K on about $1,512K (FY2022 10-K `0001437749-23-008876`; the 2019 and 2021 revenues are derived
  from the stated changes); first half of 2026 $(204)K on $895K. The 10-K names its industrial rivals as "national companies
  such as Weaver Consulting Group, Atmos Technologies, Chemstation and OMI Industries" and says each of its subsidiaries
  "competes against large, well established companies". A business that earns a loss in every period it stands without its
  one customer has no castle that "protects excellent returns on invested capital" **[L2007-004]**.
- **The competitor row.** The four odor-control rivals the 10-K names do not file with the SEC: an EDGAR company search on
  2026-10-17 for "Weaver Consulting", "Atmos Technologies", "Chemstation" and "OMI Industries" returned "No matching
  companies" for each. **Flagged: the rivals of the deciding part cannot be compared from their own filings.** The 10-K
  names filing rivals only for the non-deciding water part (Xylem, Pentair, AECOM; Veolia does not file 10-Ks) and the
  battery part (Tesla). Same metric, operating income over revenue, from their own 10-K XBRL facts, for context only:

  | company | 2021 | 2022 | 2023 | 2024 | 2025 | source (latest accession) |
  |---|---|---|---|---|---|---|
  | Xylem | 11.3% | 11.3% | 8.9% | 11.8% | 13.5% | `0001524472-26-000012` |
  | Pentair | 16.9% | 14.4% | 18.0% | 19.7% | 20.5% | `0000077360-26-000007` |
  | AECOM | 4.7% | 4.9% | 2.3% | 5.1% | 6.4% | `0000868857-25-000013` |
  | BioLargo, consolidated | (255)% | (92)% | (37)% | (24)% | (191)% | companyfacts, the five 10-Ks |
  | ONM Environmental | (34)% | 26% | 38% | 38% | (39)% | the five 10-Ks' MD&A |

  BioLargo consolidated is operating loss over revenue (2021 revenue $2,525K, derived from 2022's stated 133% increase to
  $5,884K). The water incumbents earn steady positive margins over the whole span; BioLargo's water part has no revenue of its
  own (BEST) beyond one AEC sale booked through BLEST in 2024.
- **The field's returns over the last full cycle** (section C convention). ONM's own record from 2019 to mid-2026 is the
  only filed record of its field available: losses in the four periods without the private-label customer, profits in the
  three with it. The named rivals' returns are not on the public record. Judged in words **[M1999-108]**: the standing part of
  the castle, the industrial book, has not earned even an ordinary return in any period read; the part that earned
  extraordinary returns did so on a customer's brand and left with the customer.
- **The strongest case against this reading, stated as its holder would.** The patent suit may succeed; an injunction could
  force Pooph back to a licence or out of the product, and the company says it is "actively seeking a new partner that can
  capitalize on the prior success" (10-K FY2025, MD&A). On that reading the castle is a patent, temporarily breached, whose
  future cannot be judged until the court rules, which would send the file to TOO HARD **[M2000-019]**, not OUT. I do not
  adopt it, for three reasons from the filings: the patents' average remaining life of seven years is shorter than the span
  the question asks about; even a won suit returns damages and leverage over one marketer, not the brand in the consumer's
  mind, which stays with Pooph **[M2023-073]**; and the industrial castle that would remain is shown open on its own losses,
  not merely unjudgeable. A castle being filled in on the evidence closes OUT (Q2, the routing with Q1), and here the evidence
  is the customer's own letter and the segment's own losses.
- **VERDICT: OUT.** The deciding part's castle is shown open on the evidence: the customer that made all of its five-year
  profit replaced its formula and left (8-K `0001437749-25-029852`), the brand belonged to the customer **[M2023-073]**,
  **[M2019-041]**, and without that customer the part lost money in every period read **[L2007-004]**; "If the answer had
  been yes, we wouldn’t have done it." **[M2011-015]**, **[M2012-108]**. The file closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Facts bearing on integrity are recorded, not judged, under AFTER THE STOP; the box line carries the flag.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. No buyback exists to test against the bottom of the Q7 range; the issuance record is under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The reporting figures the operator asks for are computed below.

### COMPUTATION, NOT A CLEARANCE
By Q7's range convention and its specifics, on owner cash after every real cost (Step 0 table; `q7_computation.py`):
- **Base.** Five-year average owner cash, 2021 to 2025: $(7,166)K after interest (equity-only basis); $(7,052)K before
  interest (all-equity basis). Every year of the window is negative, and so is operating cash flow alone in every year back
  to 2014. The company's own income tax is nil (no tax paid; "Income taxes $ —" in the FY2025 cash-flow supplement), so no
  tax conversion and no carryforward shelter arise: a shelter is worth nothing to a business with no taxable earnings.
- **(a) An aberrational end year.** 2025 carries the loss of the Pooph business and a doubled Clyra loss. Shown beside: the
  2021 to 2024 average, $(5,969)K, gives $(0.33) a share at the sovereign on the equity-only basis. The best single year of
  the window, 2023, was $(5,351)K, and in that year ONM earned $4,335K of operating income.
- **(b) Decline.** The series is negative throughout and worsens (2021 $(6,210)K to 2025 $(11,956)K, the outflow 93%
  larger; first half of the window $(5,803)K a year, second half $(9,438)K). A compound rate between two negative end years
  is meaningless and so is the halves' rate, so **the range is the no-growth case alone, said so**, as specific (b) requires.
- **(c) Acquisitions.** None in the years read. **(d) Working capital** is inside operating cash flow as filed (the 2025
  draw includes the receivable converted to the Pooph note and then written off).
- **(e) Growth spending.** The filing allows a guess: equipment purchases averaged $413K a year against depreciation of $94K;
  the maintenance-only case, charging depreciation in place of all equipment spending, is $(6,847)K a year, $(0.38) a share.
  The central case below charges all spending; the difference does not change the sign.
- **(f) The cap.** Not engaged; no positive growth is carried.
- **Beside it, the minority partners.** Consolidated owner cash carries all of the subsidiaries' outflows although outside
  investors own 52% of Clyra, 30% of BLEST and 5% of BETI (10-K FY2025, noncontrolling-interest policy). Removing the
  noncontrolling interests' average share of losses, $(1,394)K a year (companyfacts), as a rough guide only: $(5,772)K a
  year, $(0.32) a share. Still negative.
- **Net debt** (all-equity basis), from the 10-Q at 2026-06-30 (`0001437749-26-028023`): borrowings $5,106K (Clyra Medical
  $4,854K carried, net of discounts of $416K; parent $252K) plus finance leases $311K, less cash $2,188K = $3,229K; with the
  subsequent events that 10-Q states (Clyra notes $325K, adding equal cash; Clearthink proceeds $376K) **$2,853K**.
  Operating leases ($977K) are left out, as the convention says.
- **The floor is tested first** (2026-10-10 convention). At ten percent, no case earns the floor at any positive price,
  because every case is a stream of cash going out: "there’s just a point at which we drop out of the game" **[M2003-149]**.
  Were Q7 reached it would close OUT on the floor, whatever the width.
- **VALUE RANGE (COMPUTATION):** the no-growth case alone, at the 5.43% sovereign, ten years then zero nominal growth (a
  perpetuity of the base): all-equity, $(7,052)K / 0.0543 = $(129.9)M, less net debt $2.9M = $(132.7)M, **$(0.40) a share**;
  equity-only, $(7,166)K / 0.0543 = $(132.0)M, **$(0.40) a share**; against a price of **$0.07** (market value $23.0M).
  The range lies wholly below zero.
- **FAIR PRICE (COMPUTATION; a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the
  two averaged; with one case, that case. **All-equity (central): $(7,052)K / 0.10 = $(70.5)M, less net debt $2.9M =
  $(73.4)M, $(0.22) a share. Equity-only, beside it: $(7,166)K / 0.10 = $(71.7)M, $(0.22) a share.** Both after the
  company's own tax, which is nil. A negative fair price means no positive price earns the floor on the filed record.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED; not asked by the operator for this run.

---
## THE BOX
**OUT at Q2** (the deciding part, ONM Environmental, earned all of its five-year profit on one private-label customer's
brand; the customer replaced the formula and left in 2025, and without it the part lost money in every period read).
COMPUTATION, NOT A CLEARANCE: value range $(0.40) a share (no-growth case alone; all-equity and equity-only alike) against
$0.07; fair price $(0.22) all-equity, $(0.22) equity-only. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q3 (capital).** Equipment purchases were $1,235K in 2024 and $46K in 2025; paid-in capital, not retained earnings,
  funded every year (Step 0 tables).
- **Q4 (the accounts).** A going-concern paragraph appears in the FY2020 and FY2025 10-Ks and the 2026 10-Q ("The foregoing
  factors raise substantial doubt about our ability to continue as a going concern"). Stock pay ran $2.2M to $3.6M a year
  (option expense plus stock issued for services), between 44% and 106% of the operating cash used in 2021 to 2025. The
  FY2020 10-K told owners that "over half of our net loss is due to non-cash expenses, such as interest and stock/stock
  options issued to employees and vendors in lieu of cash" (`0001437749-21-007650`), and the FY2022 and FY2023 10-Ks repeat
  the framing ("approximately 50%", "approximately 68% of our net loss was attributable to non-cash expenses"); the rows call
  stock pay a real cost **[L2015-003]**, **[L2021-003]**. The auditor's report printed in the FY2025 10-K names the balance
  sheets "as of December 31, 2025 and 2024" in its first sentence and gives its opinion on the financial position "as of
  December 31, 2024 and 2023" in its second (`0001437749-26-006926`); recorded as found, not weighed.
- **Q5 (integrity facts, recorded, not judged).** (1) Serial issuance: weighted average shares rose from 80.0M (2014) to
  307.0M (2025), and the cover count is 328.7M (August 2026); stock was sold under an equity line in every year read
  (Lincoln Park to 2026-02-01, 17,368,716 shares for $3,216,147 in all; Clearthink from 2026-04-15). The rows list it among
  the tells: "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**. (2) The 10-K
  describes CupriDyne Clean as "the number-one performing industrial odor-control product in the market" and its technologies
  as "best-in-class", with no comparative data in the filing. (3) The chief executive, Dennis P. Calvert, has served since
  2002; salary $288,603 in 2024 and 2025 and no option award in the summary table for those years; the CFO is paid only in
  options; directors and officers as a group beneficially owned 66,531,600 shares at 2026-04-30, counting 22,841,864 under
  options and warrants (10-K/A `0001437749-26-014184`). (4) The company is plaintiff against Pooph (patent infringement,
  false advertising, breach, fraud) and defendant in Pooph's suit (breach, implied covenant), both open. A later run that
  reaches Q5 must answer these **[M2013-088]**.
- **Q6 (the money and the owners).** Issue prices: Lincoln Park in 2025, 11,745,123 shares for $2,122,000 (about $0.18);
  Clearthink, 3,250,000 shares for $391,000 (about $0.12) to 2026-06-30 and 3,500,000 for $376,000 (about $0.11) after it;
  the line lets the company direct purchases of up to the lesser of $500,000 or 300% of eight days' average traded value
  per notice (10-Q). The subsidiaries raise money at their own level: Clyra raised $5,745K in debt and equity in 2025 and
  issues 15% three-year notes with warrants at $7.50 a Clyra share, guaranteed by BioLargo; BETI sold $425K of its stock in
  2025 and $462K early in 2026. No buyback; no dividend on the common; a Clyra Series A preferred dividend of $347K in 2025
  (non-cash).
- **Q9 (debt and exposures).** Parent debt is small ($252K); Clyra Medical's carried debt rose from $1,814K (FY2025) to
  $4,854K (2026-06-30) at 15%, guaranteed by the parent; working capital was a deficit of $(1,266)K at 2026-06-30 with cash of
  $2,188K against six-month operating cash use of $5,973K. The company states that if it cannot raise more, "management may
  choose to curtail portions of our operations" (10-Q).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): the
      template copy and research folder were made before the first EDGAR call; commits after Q1, after Q2, and at the close.
- [x] Dispatched: the brief allowed the per-question commits; the lock is held by the dispatching session (not checked by
      me, by the brief); the run is folded by the dispatcher (operator rule ten). A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched: **not fully kept.** No such file
      was opened, but one filename listing of `Test Runs/` filtered on the ticker was run before any fetch (declared under
      Contamination; it returned nothing). The harness's git status and memory index were seen and are declared.
- [x] Every v5 id resolves (checked by `check_ids.py` in the research folder against `principle_ledger_v5.csv`); every
      filing fact has its accession; no number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; the Q7 figures
      are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations, and the strongest case at Q2); facts for later
      questions under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited: this is a run at today's date, not a point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used (price, count, sovereign, the balance-sheet table, the OCF and SBC
      series); its owner-earnings window, which stopped at 2017, was not used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The deciding-part threshold fails when the whole loses money.** Q2's business-of-parts convention says a part decides
when it carries "more than half of the company's five-year operating profit", or else the largest part decides. Here the
company's five-year operating result is a loss of $35.6M, one part earned $8.6M, five parts lost, and the corporate cost
centre lost more than any part earned. "More than half" of a negative total is met by any positive number, and "the largest
part" could be read by profit (ONM) or by the size of the result (Clyra, among the operating parts). I read it by profit, so
that the only part with economics to judge decides, and said so; a run reading it the other way would have judged Clyra, a
start-up, and closed at Q1 TOO HARD (NATURE). The convention needs a line for a loss-making whole. (2) **Q1 and the
start-up parts.** "Start-ups are not our game" **[L2007-015]** sits in Q1's list of what it rules OUT, but the parts
convention lets start-ups that do not decide pass Q1 unjudged even when together they lose more than the deciding part
earns; the text does not say whether parts that do not decide can keep the whole outside the circle by their weight in the
losses. (3) **Q2's field returns assume rivals who file.** None of the deciding part's named rivals files with the SEC; the
convention does not say what stands in their place, and this run used the part's own record with and without its customer.
(4) **Q7 has no instruction for a wholly negative base.** Specific (b) falls back to the no-growth case, which this run
used; the fair-price definition ("the price at which the midpoint of the range earns the floor") then yields a negative
number, which Part VII does not anticipate, and an alert set at a negative price would never fire. (5) **The template's Q7
line names "the six specifics"** where the framework now carries those six plus the four PG specifics and the later
amendments; the brief's summary was the more complete guide.
