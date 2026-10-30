# Company Run — ASML Holding N.V. (Euronext Amsterdam: ASML; Nasdaq: ASML) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name; the position was sold on 2026-08-28 on
the v4.1 Q6 read (`PORTFOLIO.md`), and the name was kept on the watch list.*

*Dispatched purchase run of record, written by a blind analyst under the brief of 2026-10-26. The brief departs from the
canonical brief (`Screens/_daily/_dispatch_brief.md`) in one stated respect only: the repository moved on 2026-10-25 to
`C:\Projects\BRK`. Working folder: `Test Runs/_research 2026-10-26 ASML/` (notes, fetch and arithmetic scripts, tool
outputs; raw filings in its git-ignored `cache/`).*

**Contamination, declared and not used.** (1) `git status` at the start listed a modified file in another company's
research folder (`_research 2026-09-27 ARCB`) and untracked `Screens/_daily/` files. (2) `git log -5` showed commit subjects
naming other companies' v5 runs and alerts (AAPL, CRM, GOOGL, JPM, MSFT, NWE). (3) A directory listing of `Screens/` (run to
find `cover_shares.py`) showed the names of blind-listed files (`RESUME STATE ...`, `WATCHLIST RUN QUEUE.md`,
`2026-08-31 PREPPED READING LIST (operator lists).md`) and of `V5 PASSERS - the alert list.md` and
`GLOBAL QUALITY WATCHLIST v0.1.md`. (4) After the final commit, `git log -3` showed two other analysts' commit subjects (an
SNPS run and a PLTR fold, with their boxes and figures). None was opened, searched or read; nothing in any of them about ASML was seen; nothing
was used. No `Test Runs/` file other than the template and this run's own two paths was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **€1,424.80** a share, Euronext Amsterdam (ASML.AS), last quote 2026-10-26 through `tools/sources.py`
  (aggregator, flagged; live quote only). Beside it: Nasdaq **$1,571.80** (2026-10-23, aggregator, flagged). ECB euro
  reference rate 2026-10-23: **1.1193 USD per EUR** (ECB Data Portal, series EXR D.USD.EUR.SP00.A), at which the Amsterdam
  price is $1,594.78.
- **Shares by class:** one class of ordinary shares. Cover of the 20-F for FY2025 (filed 2026-02-25, accession
  `0001628280-26-011378`): **385,417,665** ordinary shares (`python Screens/cover_shares.py ASML` prints the same). Checked
  against issued less treasury: the 20-F's shareholder table states 385,417,665 "issued and outstanding as of December 31,
  2025, which excludes 2,730,009 ordinary shares which have been issued but are held in treasury" (same accession). Checked
  against later filings: the statutory interim report for H1 2026 (Exhibit to the 6-K of 2026-07-15, accession
  `0001628280-26-048235`) gives **384.1 million** issued and outstanding at 2026-06-28; the Q3 2026 statements (6-K of
  2026-10-14, accession `0001628280-26-065813`, Exhibit 99.3) give a Q3 weighted basic count of 383.1 million and €4,071.0
  million of shares bought in Q3, so the count at 2026-09-27 is lower still and is not filed. **Count used: 384.1 million**,
  the latest filed period-end count; the cover count is beside it. The cumulative preference shares are an anti-takeover
  option held by a foundation, none outstanding (20-F note on EPS), and are not added.
- **Market cap:** 384.1M × €1,424.80 = **€547.3B** (on the cover count, €549.1B; `tools/run.py` prints €549.14B on the cover count).
- **Sovereign for the earnings currency:** the earnings currency is the euro (the filer reports in euros; the XBRL unit of
  the cash-flow series is EUR). **3.62%**, ECB euro area AAA yield curve, 30-year spot (series
  YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), dated 2026-10-23, through `python tools/sources.py` (the issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 0000937966:
  - 20-F FY2025, filed 2026-02-25, `0001628280-26-011378` (the integrated annual report filed as the 20-F): risk factors,
    customers, regions, export controls, sales by technology and end-use, cash-flow statement, balance sheet, equity
    investments (Mistral AI), equity method investment and related parties (Carl Zeiss SMT), buybacks, commitments and
    contingencies, the 2030 opportunity.
  - 20-F FY2022, filed 2023-02-15, `0000937966-23-000014`; 20-F FY2019, filed 2020-02-12, `0000937966-20-000011`;
    20-F FY2016, filed 2017-02-08, `0000937966-17-000007`: customer concentration, bookings and backlog, the long-term
    revenue "opportunity" each gave, buyback prices, the down payments.
  - 6-K of 2026-01-28 (Q4 and FY2025 results, `0001628280-26-003701`), 6-K of 2026-07-15 (Q2 2026 results and the H1 2026
    statutory interim report, `0001628280-26-048235`), 6-K of 2026-10-14 (Q3 2026 results, press release Exhibit 99.1 and
    summary US GAAP statements Exhibit 99.3, `0001628280-26-065813`).
  - No proxy: a foreign private issuer files none. The AGM 6-Ks (2026-03-11, `0001628280-26-016671`; 2026-04-23,
    `0001628280-26-026703`) and the remuneration report were not read, since the file closed at Q1 (Q5 and Q6 Part B not reached).
  - XBRL company facts were used for transcription of the ten-year series only and checked against the filed statements below.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, **€12,658.5
  million** on the filed consolidated statement of cash flows (20-F FY2025, `0001628280-26-011378`), against 12,658 in
  `tools/run.py`. Agreed. Two tool lines do **not** agree with the filing and the filing governs: depreciation and
  amortization FY2025 is €1,025.9 million on the filed cash-flow statement against 1,040 in `run.py`; other intangible assets
  at 2025-12-31 are €540.1 million on the filed balance sheet against 486 in `run.py`'s balance-sheet table.
- `python tools/run.py ASML --quote ASML.AS --framework v5` arithmetic lines only (output kept in the research folder):
  owner cash (operating cash less stock pay less PP&E spending) by year, EUR millions: 2021 9,828; 2022 7,136; 2023 3,153;
  2024 8,926; 2025 10,883; five-year mean **7,985**; with intangible purchases also deducted (the tool's alternate),
  9,783 / 7,099 / 3,112 / 8,910 / 10,825, mean **7,946**; on the depreciation basis, mean 8,830 (8,833 on the filed D&A line).
  Stock pay is the filed share-based compensation line (2021 118; 2022 69; 2023 134.8; 2024 172.6; 2025 202.3), the only
  stock-pay line the tool found; no securities inside operating cash, no finance-lease principal of size (€5 million in 2021),
  no other stock-pay line. Capex (PP&E) 2021 901; 2022 1,282; 2023 2,155.6; 2024 2,067.2; 2025 1,573.6. D&A (filed) 471;
  584; 739.8; 918.6; 1,025.9. Nothing the tool prints as a rule, an id or a verdict is used (Part VII, the tooling).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety as an attitude: a decision that needs pencil and paper is
"too close to think about" **[M1996-084]**; a business whose ten-year economics turn on the next generation of a machine and
on governments' export rules is the case where the analyst is most tempted to let a celebrated monopoly stand in for an
understood one, and the habits that answer it are to be "somewhat critical of everything" **[M2025-013]** and to state the
other side's case before disagreeing **[M2016-055]** (done at Q1 below). Second, who is paid to tell you: the most specific
long-range forecast on the record is the company's own 2030 "opportunity", which is a seller's projection and is read as
such, with the projector's past projections asked for and set beside it (Q1, test 5). No macro view enters: the AI cycle and
the memory cycle are not forecast here; they enter only as the width of the range at Q7. **Contrary evidence, written down
as found** **[M1997-127]**: (1) customers prepay: contract liabilities rose from €5.6 billion at the end of 2020 to €19.4
billion at the end of 2025 and the non-current part alone jumped to €9.3 billion at 2026-09-27, which is strong evidence
that the customers cannot do without the product (for the business); (2) sales rose in every year from 2016 to 2025,
straight through the 2019 and 2023 memory downturns (for the business); (3) the company's own five- and seven-year revenue
ranges have been outrun by its results, above the top, twice, and its own one-year guidance for 2026 moved from €34-39
billion in January to €44-45 billion in October (against foreseeability, though not against the business); (4) four
customers took 61.2% of 2025 sales and China took 29.1% (against); (5) the operating margin over 2016 to 2025 averaged about
30%, below KLA's about 36%, for the field's only EUV maker (against the size of the castle's toll, see AFTER THE STOP, Q2).

## THE STANDING RULE
Owning a marketable part-interest in ASML, bought without borrowed money and sized so that a 50% fall would not force a sale,
puts the buyer at no risk of ruin: "always be sure you can play the next day" **[M2025-015]**. Nothing in the target's own
balance sheet (net cash of about €10.0 billion at 2026-09-27) bears on the buyer's survival. The rule is not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business, from the filing.** ASML makes the lithography scanners that print chip patterns, and is the only maker of
EUV scanners. FY2025 total net sales €32,667.3 million, of which net system sales €24,474.3 million and installed base
management (service and field options) €8,193 million (20-F FY2025, `0001628280-26-011378`; IBM figure from the 6-K of
2026-01-28, `0001628280-26-003701`). Systems by technology, 2025 (units, € millions): EXE (High NA EUV) 4, 1,156.9; NXE (low
NA EUV) 44, 10,445.8; ArF immersion 131, 10,311.4; ArF dry 16, 427.0; KrF 78, 1,001.3; I-line 54, 307.3; metrology and
inspection 208, 824.6 (2023: NXE 53 units for €9,124.0 million; ArFi 125 for €9,017.4 million). By end-use 2025: logic
€16,054.1 million, memory €8,420.2 million (same 20-F).

**The key variables, and how predictable each is** **[M1998-044]**, read from the filings:
1. *What chipmakers spend on lithography, year by year.* Net bookings, € billions (20-F FY2019 five-year table
   `0000937966-20-000011`; 20-F FY2022 `0000937966-23-000014`; 6-K 2026-01-28): 2015 4.6; 2016 5.4; 2017 9.4; 2018 8.2;
   2019 11.7; 2022 30.7; 2024 18.9; 2025 28.0. Backlog €38.8 billion at the end of 2025. The swings are wide, but the
   framework carries a cycle at Q7, not here; this variable alone would not close Q1.
2. *Lithography intensity: how many critical exposures, and on whose machine, the customers' future processes use.* The
   filer's own risk factor: "if customers choose not to adopt our innovations or shift toward architectures that rely less
   on lithography, our competitive position may weaken", and "if alternative solutions gain traction, our competitive edge
   and financial returns may suffer" (20-F FY2025, risk factors, `0001628280-26-011378`). This is a forecast about
   technology choices, not about customer habits **[M2017-019]**.
3. *Whether the next generation is adopted, and at what price.* The filer calls High NA EUV "essential to advancing
   Moore’s Law" and says its success "depends on continued technical progress by both us and our suppliers"; at the end of
   2025 customers had run "more than 400,000 wafers on High NA EUV systems" and ASML was still "qualifying this system for
   high-volume manufacturing" (20-F FY2025, CEO Q&A and risk factors). Four EXE systems were recognized in 2025.
4. *What governments allow.* China was 29.1% of 2025 sales and 36.1% of 2024 sales (€9,519.7 million and €10,195.1
   million; 2023 €7,251.8 million, 26.3%); Taiwan 25.5% and South Korea 25.0% of 2025 sales. EUV and specific DUV immersion
   systems need Dutch export licenses; a US "Affiliates Rule" of 2025-10-01 is suspended until 2026-11-10, and China's
   rare-earth export restrictions are suspended to the same date (20-F FY2025, "Global geopolitics – export controls" and
   risk factors). The filer: "we do not control the licensing process or approval criteria." These are political decisions
   not yet made; no filing can state them.
5. *Who the customers are.* Four customers each above 10% took €20.0 billion, 61.2% of 2025 sales; the largest took
   23.9% (2024: 16.6%); in 2019 the largest took 39.7% and in 2021 37.0% (20-F FY2025; 20-F FY2019; 20-F FY2022).
6. *The sole supplier.* Carl Zeiss SMT is "our single supplier, and we are their single customer, of optical columns"
   (20-F FY2025, related parties); ASML owns 24.9% of its holding company and lends to it for its capital spending.

**The tests.**
- *Where will it be in ten years* **[M2000-037]**, **[M2012-065]**? Which company wins in lithography can be named today
  (test 6): no other company makes an EUV scanner, and Canon and Nikon compete in DUV only (20-F FY2025, "We compete
  primarily with Canon and Nikon in respect of DUV systems"). What cannot be named is the earning power in 2035: it turns on
  variables 2, 3 and 4, each a forecast of technology or of policy.
- *Would the insiders write it down* **[M2000-105]**? The company does write down a long-range figure, and its own record
  is the evidence. In the 20-F for FY2016 it targeted "an annual revenue opportunity ... of around EUR 11 billion in 2020"
  (`0000937966-17-000007`); 2020 sales were €13,978 million. In November 2018 it modelled 2025 revenue "between €15
  billion in a low-market scenario and €24 billion in a high-market scenario" (20-F FY2019, `0000937966-20-000011`); 2025
  sales were €32,667 million, 36% above the top of the range. Its current figure is a 2030 range of "approximately €44
  billion and €60 billion" (20-F FY2025), five years out, not ten; and on 2026-01-28 it guided 2026 sales to "€34 billion
  and €39 billion" (6-K `0001628280-26-003701`), then on 2026-10-14 to "€44 billion and €45 billion" (6-K
  `0001628280-26-065813`), a move of more than a fifth inside one year. The insiders write down five-year ranges that the
  business has outrun beyond their top, and no ten-year figure. The misses so far have run in the owner's favour; the test
  is not their direction but whether anyone, insiders included, has a fix on the economics ten years out.
- *Is the forecast about customers or about technology* **[M2017-019]**, **[M2023-030]**? About technology and
  governments: the next node's patterning choices, the adoption of High NA, the filer's "architectures that rely less on
  lithography" (20-F FY2025, risk factors), and export licences. The row's own ground, "we know what we think we can project
  out in terms of consumer behavior and threats to a business" **[M2023-030]**, has no purchase here: ASML's customers are
  four or five chipmakers whose own roadmaps change node by node.
- *How far off could I be* **[M2011-084]**? Very far: the company's own seven-year range missed by more than a third, and
  a single variable (China, 29% to 36% of sales in the last two years) can be moved by a licensing decision in a year.
- *Do the past statements tell me the future ones* **[M2008-033]**? Sales rose every year from €6,875 million (2016) to
  €32,667 million (2025), a near fivefold rise no 2016 statement foretold, on a product (EUV) of which the 2016 report said
  "To date, we have only sold a limited number of EUV systems" (20-F FY2016, `0000937966-17-000007`). The statements describe a business transformed by one technology
  inside the span; they do not show what the next one will do.
- *Abroad: governance and tax* **[M2000-141]**: a Dutch N.V. with a two-tier board, a structure regime and a preference-share
  foundation (20-F FY2025, corporate governance); readable, and not what decides this file.

**The other side's case, stated as well as I can** **[M2016-055]**. ASML is no start-up and no fad: it has been the
lithography leader for two decades; EUV took decades and the joint work of a single optics supplier to build, which is the
kind of advantage "in times measured shorter than decades" could not be built **[M2002-048]**; it is the only maker, so the
winner can be named; customers prepay billions years ahead, the backlog was €38.8 billion at the end of 2025, and in October
2026 some customers were "expressing an interest in placing orders with us for 2029 and even 2030" (6-K
`0001628280-26-065813`); its sales did not fall in the 2019 or 2023 downturns; and a quarter of its revenue (€8,193 million
of €32,667 million in 2025) comes from servicing and upgrading an installed base that customers keep running for decades. On this case the economics are those of a monopoly
toll on a growing industry, and the only uncertainty is the cycle, which Q7 can carry.

**Why the case does not carry the file.** The rows define understanding as a fix on "earning power and competitive
position" in five or ten years **[M2012-065]**, and they draw the distinction this case blurs: "We understand what it does
for people." but not "the economics of it 10 years from now" **[M2000-104]**. The winner
of today's lithography can be named; its economics in 2035 depend on whether a product not yet in high-volume manufacturing
(High NA) and its successor are adopted at prices that hold the margin, on whether chipmakers' architectures keep or reduce
lithography's share of their spending, and on export rules for the market that took 29% to 36% of sales. Each is a
forecast of technology or of policy, and the rows send that forecast to the box: "a business that must deal with
fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**; a
"technological component" that is "of significance" does not "make it through the filter" **[M1998-008]**; and "If something
is not very predictable, forget it." **[M1998-044]**. The company's own forecasting record (test 5) shows that those closest
to the business carry ranges a third wide five years out and miss beyond them. And the rows settle the doubt: "if you have
doubts about something being into your circle of competence" the answer is that it is not **[M2002-092]**. By the fixed routing, a business whose ten-year economics cannot be foreseen because its industry changes fast
closes here, at Q1, in TOO HARD, never OUT on the business **[M2006-013]**, **[M2000-038]**.

**The cause: NATURE, not WORK.** The deciding question, ASML's earning power in 2035 as set by lithography intensity, the
adoption and pricing of the next two EUV generations, and the export rules for China, is a forecast the industry's own
insiders would not write down **[M2000-105]**: the best-informed insider on the record, the company, writes a five-year
range and has been outrun beyond it twice, and the rules for China depend on governments that have suspended, not settled,
them. No filing not yet read would answer it; the reading done for this run (four 20-Fs across the cycle and three 6-Ks of
2026) is the reading the rows ask for, and "We couldn't solve this problem, moreover, even if we were to spend years
intensely studying those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have
no insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]** A
lower price does not reopen the box **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**, **[L1993-023]**, **[M2000-104]**, **[M2000-105]**, **[M2002-092]**; filing
  fact: the filer's own risk factor on "architectures that rely less on lithography" and "alternative solutions", its five-year
  revenue ranges outrun beyond their top (2025: €32.7 billion against a 2018 range of €15-24 billion), and China at 29.1% of
  2025 sales under export licences "we do not control" (20-F FY2025, `0001628280-26-011378`).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (the file closed at Q1). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets were read in Step 0's place (as the brief asks when the file closes before Q4)
and are written below under COMPUTATION, NOT A CLEARANCE.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The arithmetic is written below under COMPUTATION, NOT A CLEARANCE.

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
**TOO HARD (NATURE)**, decided at **Q1**: ASML's earning power ten years out turns on lithography intensity, the adoption
and pricing of the next EUV generations, and export rules for China (29.1% of 2025 sales), forecasts its own insiders do not
write down for ten years and have missed beyond their own five-year ranges; a lower price does not reopen it. Integrity facts
recorded, not judged (the guidance habit and the beaten guidance, under AFTER THE STOP, Q5).
COMPUTATION, NOT A CLEARANCE: range €661 to €808 a share (all-equity, maintenance case) against €1,424.80; fair price €272
(equity-only €246).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(The file closed at Q1. These are facts already found that bear on later questions, each with its source, written down and
not weighed **[M1997-127]**; no verdict; the box is unchanged, operator rule 2.)*

**Q2, the castle.**
- Competition, in the filer's words: "We compete primarily with Canon and Nikon in respect of DUV systems", and "We also face
  competition from new competitors with substantial financial resources, as well as from those driven by the ambition of
  self-sufficiency in the geopolitical context" (20-F FY2025, risk factors, `0001628280-26-011378`). No other EUV maker is
  named in any filing read. Canon, Nikon and Carl Zeiss are not SEC filers; their own reports were not read.
- Price per tool, from the filed sales by technology (20-F FY2025): NXE (low NA EUV) €172 million a unit in 2023 (€9,124.0m /
  53) and €237 million in 2025 (€10,445.8m / 44); EXE (High NA) €289 million a unit in 2025 (€1,156.9m / 4); ArF immersion
  €72 million (2023) and €79 million (2025). The price per low NA EUV tool rose about 38% in two years while units fell.
- The low end shrank: KrF units 184 (2023, €2,202.5m) to 78 (2025, €1,001.3m); ArF dry 32 to 16 (same table). The filer does
  not say in the passages read whether this is China's buying slowing or share lost.
- Customers prepay: contract liabilities (down payments and consideration for systems not yet recognized) were €1.8 billion at
  the end of 2016, €5.6 billion at the end of 2020 and €19.4 billion at the end of 2025 (XBRL `ContractWithCustomerLiability`,
  checked to the FY2025 balance sheet: current €16,006.3m plus non-current €3,366.3m); non-current contract liabilities were
  €9,300.6 million at 2026-09-27 (6-K `0001628280-26-065813`, Exhibit 99.3). Most contracts "require our customers to pay a
  down payment on systems to be shipped" (20-F FY2022, `0000937966-23-000014`).
- Installed base management (service and field options) €8,193 million in 2025, 25% of sales; €3,289 million in Q3 2026,
  "above guidance" (6-K `0001628280-26-065813`).
- Gross margin 52.8% in 2025, 57.5% in Q3 2026; operating margin 34.6% in 2025, 44.4% in Q3 2026 (same filings).
- The parts table: one reportable segment; the chief operating decision maker uses consolidated net income and sales (20-F
  FY2025, segment note). Systems and installed base are not reported as segments with their own profit.
- The field's returns over the last full cycle, from the filers' own statements (see the competitor row under COMPUTATION):
  operating margin, average of fiscal 2016 to 2025, ASML 29.9%, Applied Materials 26.9%, Lam Research 27.5%, KLA about
  35.7%; none of the four had an operating margin below 18% in any year. The field earns excellent returns, not ordinary ones.
- The one fact that runs against the size of the castle's toll: the only EUV maker's average operating margin over the span
  sits below KLA's and only two to three points above Applied Materials' and Lam's, with R&D at 14.4% of 2025 sales
  (€4,699 million).

**Q3, capital.**
- Operating income after tax against tangible capital (equity plus debt less cash, short-term investments, goodwill and
  intangibles), from XBRL checked to the FY2025 balance sheet: 2016 to 2020 between 37% and 63% a year; 2023 to 2025 between
  132% and 166%; 2021 and 2022 meaningless (tangible capital near zero, €1.6 billion and €0.3 billion, because customer down
  payments and buybacks exceeded the operating assets). The business runs largely on its customers' money.
- Capital spending (PP&E plus intangibles) €941m (2021), €1,320m (2022), €2,196m (2023), €2,083m (2024), €1,631m (2025),
  against depreciation and amortization €471m, €584m, €739.8m, €918.6m, €1,025.9m (filed cash-flow statements). Spending
  above depreciation averaged €886 million a year in the window. PP&E net rose from €1,601m (2017) to €7,894m (2025).
- Loans to the sole optics supplier: under the 2021 framework agreement and the 2021 and 2024 loan agreements ASML finances
  Carl Zeiss SMT's capital spending above thresholds through ten-year loans whose interest rate is "subject to a floor of
  0.01 % and a cap of 1 %" (the 2024 loan carries an effective 3.1% after its discount); loans receivable €1,920.0 million at
  2025-12-31 (current €266.1m, non-current €1,653.9m) and €2,085.5 million at 2026-09-27; ASML also makes non-interest-bearing
  advance payments to secure optical column deliveries (20-F FY2025, related parties; 6-K `0001628280-26-065813`).
- Outside the core: €1,302.2 million for 11.1% of Mistral AI (September 2025, lead investor in its Series C), a further
  €405.7 million of equity investments in Q3 2026, equity investments carried at €2,239.4 million at 2026-09-27, and a €509.7
  million "gain on equity investments" in Q3 2026 income before tax (20-F FY2025, note 9; 6-K `0001628280-26-065813`).
- Acquisitions in the span: HMI (2016, €2,641 million cash, with Cymer the source of today's goodwill), Berliner Glas (2020,
  €223 million), €33.6 million in 2023 (20-F cash-flow statements; XBRL). Net purchases are far below half of owner cash; not a
  serial acquirer.

**Q4, the accounts.**
- US GAAP is the primary standard for the quarterly releases and the 20-F; IFRS statutory statements are also published. No
  adjusted earnings figure is featured in the releases read, and no EBITDA was found in them.
- Stock pay €202.3 million in 2025 (0.6% of sales), expensed (cash-flow statement).
- Inventory reserves charged every year: €485.3m (2023), €554.7m (2024), €469.4m (2025), a recurring cost inside earnings;
  inventories €11,429.3m at the end of 2025, 35% of sales (filed balance sheet and cash-flow statement).
- The equity-method investee (24.9% of Carl Zeiss SMT Holding, a variable interest entity not consolidated) paid dividends of
  €218.0m (2023), €225.4m (2024) and €320.5m (2025), inside operating cash (20-F FY2025, cash-flow note 2). A "variable pricing
  model for purchases of products and services determined by the annual financial performance of both ASML and Carl Zeiss SMT
  GmbH in the lithography business" shares the lithography profit between them (20-F FY2025, related parties); its terms are
  not disclosed.
- Restructuring announced 2026-01-28: ASML "to strengthen focus on engineering and innovation by streamlining the Technology
  and IT organizations" (6-K `0001628280-26-003701`); its cost was not found in the filings read.
- Effective tax rate 17.7% in 2025 (pre-tax €11,406m, tax €2,013m) against the Dutch statutory rate; the gap was not read in
  the tax note line by line and is not a carryforward found in the passages read.
- The balance sheets over ten years are read under COMPUTATION below.

**Q5, the people (integrity facts recorded, not judged).**
- Guidance: quarterly sales and gross-margin guidance and annual sales guidance in every results release read (6-Ks of
  2026-01-28, 2026-07-15, 2026-10-14), and published long-range figures (2020 "opportunity" of around €11 billion, 2025 range
  €15-24 billion, 2030 range €44-60 billion; 20-F FY2016, FY2019, FY2025). The rows weigh earnings guidance and the habit of
  reaching declared targets against at Q4 and judge them at Q5 (**[L2019-006]**, **[L2002-041]**).
- Beaten guidance, in the company's words: Q3 2026 sales "towards the high end of our guidance"; installed base sales "came in
  above guidance"; gross margin "above guidance at 57.5%" (6-K `0001628280-26-065813`). The 2026 annual guidance was raised
  from €34-39 billion (January) to €44-45 billion (October).
- Chief executive Christophe Fouquet signs the 6-Ks of 2026; chief financial officer Roger Dassen (6-K of 2026-10-14). The
  remuneration report and AGM materials were not read.
- No material contingencies "probable or reasonably possible" (20-F FY2025, note 17); no investigation of the company was
  found in the passages read.

**Q6, the money and the owners.**
- Buybacks are announced as amounts with no stated price: "up to €12 billion" for 2022-2025 (€7.6 billion executed), and a
  new program "of an amount up to €12 billion" for 2026-2028 announced 2026-01-28, which "may be suspended, modified or
  discontinued at any time" (6-K `0001628280-26-003701`). The row the template points to is **[L2016-002]**; not weighed here.
- Prices paid (20-F filings): 2021 14,358,838 shares for €8,560.3m, about €596 a share; 2022 8,538,787 shares at an average
  €543.37; 2024 574,925 shares for €500.0m, about €870; 2025 8,323,320 shares for €5,950.0m, about €715; 2023 €1,000.0m (share
  count not read); 2026 to 2026-09-27 €6,148.4m (6-K `0001628280-26-065813`; prices not in the SEC filings read). Against the
  bottom of the computed range below (€661 a share, central basis; COMPUTATION, NOT A CLEARANCE): the 2021 and 2022 prices sit
  below it; the 2024 and 2025 prices sit above it; the 2026 prices were not found.
- Dividends paid €2,348.3m (2023), €2,452.9m (2024), €2,550.3m (2025); €7.50 a share declared for 2025, up 17% (filed
  cash-flow statements; 6-K `0001628280-26-003701`).
- No all-stock deal in the span (the deals above were paid in cash).

**Q9, debt and exposures.**
- Debt: Eurobonds; €4,390.9 million at 2025-12-31 (long-term €2,709.0m plus current €1,681.9m), about €2,697.6 million at
  2026-09-27 after repayments of €692.9m and €1,000.4m; cash and short-term investments €12,735.1m at 2026-09-27 (6-K
  `0001628280-26-065813`). Net cash about €10.0 billion.
- Purchase obligations €12.7 billion at 2025-12-31, €9.6 billion due within a year, with terms that let ASML "delay or cancel
  delivery of ordered goods and services" (20-F FY2025, note 17).
- Concentrations: four customers 61.2% of 2025 sales; China 29.1%, Taiwan 25.5%, South Korea 25.0%; a single supplier of
  optical columns; the three largest customers held 35.4% of receivables at 2025-12-31 (20-F FY2025).

**Q12.** None of the businesses the rows name. Not weighed.

---
## COMPUTATION, NOT A CLEARANCE
*(Arithmetic done after the closing STOP at Q1. It carries no entry language and changes no box, operator rule 3. Scripts and
outputs: `value.py` / `value_output.txt`, `series.py` / `series_output.txt`, `peers.py` / `peers_output.txt`,
`run_py_output.txt` in the research folder.)*

### The balance sheets, ten year-ends, read before the income account (**[M2025-032]**)
EUR millions, year-end, from XBRL checked to the FY2025, FY2022, FY2019 and FY2016 20-F balance sheets:

| year | equity | cash (+ ST inv.) | receivables | inventories (% sales) | PP&E | goodwill + intangibles | debt | contract liabilities |
|---|---|---|---|---|---|---|---|---|
| 2016 | 9,972 | 2,907 | 700 | 2,781 (40%) | 1,687 | 6,197 | n/r | 1,834 |
| 2017 | 10,691 | 2,259 | 1,740 | 2,956 (33%) | 1,601 | 5,707 | 3,008 | 2,152 |
| 2018 | 11,641 | 3,121 | 1,498 | 3,440 (31%) | 1,590 | 5,645 | 3,008 | 2,953 |
| 2019 | 12,592 | 3,532 | 1,787 | 3,809 (32%) | 1,999 | 5,645 | 3,108 | 4,286 |
| 2020 | 13,865 | 6,049 | 1,310 | 4,569 (33%) | 2,470 | 5,678 | 4,678 | 5,594 |
| 2021 | 10,141 | 6,952 | 3,028 | 5,179 (28%) | 2,983 | 5,508 | 4,584 | 11,161 |
| 2022 | 8,811 | 7,268 | 5,324 | 7,200 (34%) | 3,944 | 5,398 | 4,260 | 17,751 |
| 2023 | 13,452 | 7,005 | 4,334 | 8,851 (32%) | 5,493 | 5,331 | 4,632 | 16,266 |
| 2024 | 18,477 | 12,741 | 4,478 | 10,892 (39%) | 6,847 | 5,210 | 4,688 | 18,196 |
| 2025 | 19,612 | 13,322 | 3,023 | 11,429 (35%) | 7,894 | 5,129 | 4,391 | 19,373 |
| 2026-09-27 | 22,064 | 12,735 | 9,253 | 11,907 | 8,077 | 5,171 | about 2,698 | non-current 9,301 |

(Cash for 2016 to 2023 is cash and equivalents only; short-term investments were small and not added. "n/r": not read. The
2025 intangibles are the filed €540.1m, not the tool's 486.) **What the figures say.** Equity doubled over the span although
€13.2 billion went into buybacks in 2021 and 2022 alone, which is why equity fell in those two years and retained earnings dipped
in 2021. Goodwill and intangibles (Cymer and HMI) are flat at about €5 billion and a shrinking share of equity (62% in 2016,
26% in 2025). Cash grew with sales and the company carried net cash at every year-end read. Receivables swing with the timing of
shipments and down payments (from 9% to 25% of sales) and reached €9.3 billion at 2026-09-27 after Q3's record shipments.
Inventories hold at about a third of sales and carry an obsolescence charge every year. PP&E has risen nearly fivefold since
2018. The largest liability is the customers' money: contract liabilities grew from €1.8 billion to €19.4 billion, exceeded
equity at the ends of 2021, 2022 and 2023, and nearly matched it at the ends of 2024 and 2025. **What they do not say:** the economics inside Carl Zeiss SMT, which is not consolidated
and whose profit is shared with ASML under an undisclosed pricing model; whether the down payments are refundable if orders
are cancelled under export rules; and what the installed base will earn when the next generation arrives. **What they cannot
say:** the export rules and the customers' process choices of the 2030s, the variables that closed the file.

### Owner cash, after every real cost (operator rule 5; never a net-income proxy)
EUR millions, from the filed cash-flow statements (operating cash, which includes working capital and the Zeiss dividends,
less stock pay, less capital spending):

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| all spending (PP&E + intangibles) | 9,787 | 7,098 | 3,112 | 8,911 | 10,825 | **7,947** |
| maintenance case (D&A as the maintenance guess) | 10,257 | 7,834 | 4,569 | 10,075 | 11,430 | **8,833** |

- Growth shown, aggregate owner cash 2021 to 2025: 2.55% a year (all spending); 2.74% a year (maintenance case). Sales grew
  15.1% a year over the same years; owner cash did not, because 2021's operating cash was swollen by down payments (contract
  liabilities doubled in 2021) and 2023's was depleted when they reversed.
- Specific (a): not applied. The filer describes no year of the window as aberrational; the trough year (2023) sits inside
  the window, not at an end. The literal window is the window used.
- Specific (b): no decline; not applied.
- Specific (c): no acquisition in the window beyond €33.6 million (2023), immaterial; not a serial acquirer.
- Specific (d): working capital is inside operating cash and so counted, including €2,756 million a year of build-up in
  customer down payments (contract liabilities €5,594m at the end of 2020 to €19,373m at the end of 2025). Beside: with that
  build-up removed the maintenance base is €6,077 million and the no-growth value €463 a share.
- Specific (e): the filing allows the guess, by the rows' default that depreciation is "not inappropriate in most companies to
  use as a proxy for required capital expenditures" (**[M1998-127]**) and the filer's own account of its spending as capacity
  for EUV and High NA (20-F FY2025); the maintenance case is central and the all-spending case beside. Growth spending (above
  D&A) €886 million in year one and €1,131 million in year ten of the growth case, none after year ten.
- Specific (f): not triggered; 2.74% for ten years asks for nothing near the highest share of sales the business has earned.
- **CONVENTION of this run:** loans to Carl Zeiss SMT (build-up about €384 million a year, from nil at the end of 2020 to
  €1,920 million at the end of 2025) are left out of owner cash; rationale: they are repayable loans secured by a parent
  guarantee, recovered over ten years, not spending consumed. With them deducted the central bottom is about €634 a share.
- **CONVENTION of this run:** the Mistral AI stake (€1,302.2m in 2025, €405.7m more in Q3 2026) is neither capital spending
  nor net cash; rationale: it is an outside investment, neither a cost of the lithography business nor cash. It is carried at
  €2,239.4m at 2026-09-27 (with the other equity investments), about €5.8 a share, and left out of the range.
- **CONVENTION of this run:** owner cash "before interest" for the all-equity basis is taken as filed; rationale: interest
  paid (€137.8m, €160.0m, €114m in 2023 to 2025) and interest received (€190.8m, €169.5m, €201.3m) nearly cancel, and removing
  the interest earned on the cash added back separately would lower the base by a few tens of millions a year.

### The value range (Q7's range convention, in full)
Sovereign 3.62% (ECB 30-year AAA, 2026-10-23). Ten years at the growth shown, then zero nominal growth; the ends are the
no-growth and shown-growth cases. All-equity basis central: whole-business value plus net cash of €10,037.5 million at
2026-09-27 (cash and short-term investments €12,735.1m less debt of about €2,697.6m; finance leases inside the debt, operating
leases left out), over 384.1 million shares. Equity-only beside (owner cash as filed against the market value, net cash not added).

| case | no growth | shown growth | per share, all-equity | per share, equity-only | width |
|---|---|---|---|---|---|
| **central: maintenance case** | €244.0B | €300.3B | **€661 to €808** | €635 to €782 | 1.23 |
| beside: all-spending case | €219.5B | €273.0B | €598 to €737 | €572 to €711 | 1.24 |
| beside: down-payment build-up removed | €167.9B | not computed | €463 (no growth) | | |
| beside: Zeiss loans deducted | | | about €634 (no growth) | | |

**The floor, tested first.** At €1,424.80 the market value is €547.3 billion and the enterprise value €537.2 billion. The
expected return at the price is 1.64% on the no-growth case and 2.07% on the shown-growth case (maintenance basis; 1.48% and
1.87% on all spending). No case of the range earns the floor of about ten percent (**[M2003-149]**), so Q7, had it been
reached, would close OUT on the floor whatever the width. Beside, as sensitivities and not the convention's range: the
maintenance base carried at 10%, at the 2021-2025 sales growth of 15.1%, or at the 2020-2025 sales growth of 18.5% for ten
years and then flat gives expected returns at the price of 3.7%, 5.3% and 6.6%.

### The two reporting figures (the owner's request; a reporting convention, not a rule; neither is a verdict)
- **(a) VALUE RANGE:** **€661 to €808 a share** (central: all-equity, maintenance case, the company's own tax, no conversion);
  equity-only €635 to €782 beside; all-spending case €598 to €737 beside; the literal window is the window used. Nasdaq
  equivalents at the ECB rate of 2026-10-23 (1.1193 USD per EUR): $740 to $904.
- **(b) FAIR PRICE:** **€272 a share** (all-equity, central; each end case valued at ten percent and the two averaged, net cash
  added), **$304** at 1.1193; equity-only **€246** ($275) beside. On the all-spending case, €253 ($283), equity-only €227 ($254).
- **Against the price:** €1,424.80 in Amsterdam (2026-10-26); $1,571.80 on Nasdaq (2026-10-23), against $1,594.78 for the
  Amsterdam price at the ECB rate. The price is 1.8 times the top of the range and 5.2 times the fair price.
- Growth spending charged: €886 million in year one, €1,131 million in year ten, none after (specific (e)). No utility debt
  credit (not a regulated utility).

### The competitor row, from the competitors' own filings (whole span, never one year)
Fiscal years ending in the calendar year shown (ASML December; Applied Materials October; Lam Research and KLA June).
Transcribed from XBRL company facts and checked against each filer's latest 10-K statement of operations:

| filer (10-K checked) | sales FY2016 to FY2025 | op. margin, avg FY2016-25 (min, max) | owner cash / sales, avg | latest op. margin |
|---|---|---|---|---|
| ASML (20-F `0001628280-26-011378`) | €6.9B to €32.7B (18.9% a year) | 29.9% (23.6%, 36.3%) | 26.7% | 34.6% (FY2025) |
| Applied Materials (`0001628280-25-056742`: FY Oct 2025 sales $28,368m, income from operations $8,289m) | $10.8B to $28.4B (11.3%) | 26.9% (19.9%, 30.2%) | 20.0% | 29.2% (FY2025) |
| Lam Research (`0000707549-26-000037`: FY Jun 2025 sales $18,436m, operating income $5,901m; FY Jun 2026 $23,233m and $8,200m) | $5.9B to $18.4B (13.5%) | 27.5% (18.3%, 32.0%) | 21.7% | 35.3% (FY2026) |
| KLA (`0000319201-26-000027`: FY Jun 2026 sales $13,579m) | $3.0B to $12.2B (16.9%) | about 35.7% (25.4%, 40.7%) | 27.0% | about 41.7% (FY2026) |

KLA tags no operating income after FY2014; its margin in the averages is pre-tax income plus interest expense, which carries
other income and overstates the operating margin by about 1.7 points in FY2026 (its statement gives about $5,661m, 41.7%,
against the proxy's 43.4%). Owner cash here is operating cash less stock pay less PP&E spending, before acquisitions. Canon,
Nikon and Carl Zeiss are not SEC filers and are not in the row.

---
## RESEARCH PASS
Not written. The box is TOO HARD (NATURE), not (WORK); the brief asks for steps 1 and 2 only for a TOO HARD (WORK). Had it
been WORK, Part VII would still close the pass unrun, since no case of the computed range earns the floor at the price.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `15c13122`, before the first EDGAR call); written question by
      question; committed after Q1 and after the closing sections (write-early).
- [x] Dispatched: the brief allowed per-question commits by pathspec of the two paths only; the lock is the dispatching
      session's. The run binds nothing until folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at
      the top under contamination: other companies' names in commit subjects and in `git status`, and blind-listed file names
      in a `Screens/` directory listing. Not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `check_cites.py` in the research folder, which also checks
      every quoted fragment in the sentence of an id against that row, and finds no E-id); every filing fact carries its
      accession or names its filing.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; every figure after it is headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from the
      ECB (issuing authority); the Amsterdam and Nasdaq quotes flagged as aggregator quotes.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line (guidance and beaten guidance).
- [x] No row dated after the anchor: a current run, not a point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used; two of its lines disagreed with the filing and the filing was used.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest limits: Q1 is a judgment, and another analyst could read the same filings as IN on the other side's case written at
  Q1; the deciding facts are listed so the difference can be argued on them. The Amsterdam quote is dated 2026-10-26 and the
  Nasdaq quote 2026-10-23. The share count used (384.1 million at 2026-06-28) is above the unfiled count at 2026-09-27 by
  perhaps three million shares (Q3 buybacks), under 1% on the per-share figures. Not read: the remuneration report, the AGM
  materials, the tax-rate reconciliation line by line, the 2023 buyback share count, the 2026 buyback prices, and the reports
  of Canon, Nikon and Zeiss.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1, test 5, when the company itself writes the forecast down.** The test asks whether the insiders would put a ten-year
forecast on paper; ASML publishes five-year revenue ranges every two or three years. The text does not say whether a company's
own published scenario counts as the insiders writing it down, or is a seller's projection under the foundations (who is paid
to tell you; projections not consulted). I read it as neither passing nor failing the test by itself, and used the company's
own record of being outrun beyond its ranges as the evidence of how far off a ten-year view could be (test 8). A line saying
how a published company target is read at Q1 would settle it. (2) **Specific (a) and down payments.** The cycle base applies
only where the filer itself calls a window year aberrational. ASML's operating cash swings by billions with customer down
payments (2021 up, 2023 down); the filer describes the swings but never calls a year aberrational, so the literal window
stands and about €2.8 billion a year of customer financing sits inside the base while sales growth (15% a year) and owner-cash
growth (2.6%) diverge. Specific (d) counts working capital but does not say what to do when the working capital is a liability
that grows with orders; I showed the base without it beside. (3) **Supplier loans and minority stakes.** The text says what to
do with acquisitions, but not with repayable loans to a sole supplier that finance the supplier's capital spending, nor with a
minority stake in an unrelated company; both were confessed as CONVENTIONS of this run. (4) **"Before interest" on the
all-equity basis.** The text adds net cash back but does not say whether the interest earned on that cash comes out of owner
cash; for a net-cash company the two count the same money twice. Immaterial here, and confessed. (5) **The share count.** The
template asks for the cover count; a 20-F cover is ten months stale by October, and the latest filed period-end count (an
interim report filed as a 6-K exhibit) was used with the cover count beside; the text could say which governs. (6) **The Q1
routing and a technology monopoly.** The routing sends a fast-changing industry to TOO HARD at Q1 and the castle to Q2; it does
not say how to treat a business whose castle is the technology itself, where the strength of the castle (sole EUV maker) and
the unforeseeability of the economics (next generation, export rules) are the same fact. This run closed at Q1 on the
economics; a reader who weighs the castle first would reach Q2, and on the computation would close at Q7 on the floor.
