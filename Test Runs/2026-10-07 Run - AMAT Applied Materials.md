# Company Run — Applied Materials, Inc. (Nasdaq: AMAT) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`, as amended through 2026-10-07: sections A to H of the gaps case and the
Q2 paragraph on a row about one company in the text). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind
run under `Screens/_daily/_dispatch_brief.md` (operator rule 10); the dispatcher's lock was in `Screens/_daily/` when this
run started (read: "interactive v5 re-runs batch 1", 08:33). Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied from the template to this dated name before any fetch.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared and not used.** (1) The dispatching message says there are earlier run files about Applied
Materials; none was opened, listed or searched. The lock's text ("v5 re-runs") also implies the name was run before under
v4.1. (2) The session context showed, without my asking: a `git status` listing with research-folder names of other
companies (AYI, BDC, CHD, ARCB, and others truncated), recent commit subjects naming LMT, GD, BRK.B and TSCO, and a memory
index line saying "57 gate-clearers, nothing buyable" and that holding reviews are owed. None of it names Applied
Materials' box or position, and none of it was used. (3) The framework text itself names other runs (MITSY, PG, TJX, HRB,
Visa, a defence prime); read as framework text only. (4) After the closing commit, `git log` showed the subjects of other analysts' commits made the same
morning (ACNB: "Q1 closed IN"; ATR: a Q4 line); seen after this run's box was written, and not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $530.27 (close 2026-10-06; aggregator quote via `tools/run.py`, **flagged** per operator rule 5: a live quote
  only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **793,597,443** outstanding as of
  July 26, 2026 (10-Q for the quarter ended July 26, 2026, filed 2026-08-20, accession `0001628280-26-058235`;
  `python Screens/cover_shares.py AMAT` returns the same). Cross-check: the 10-Q's statement of stockholders' equity shows
  794 million shares outstanding and 1,244 million in treasury at July 26, 2026; the 10-K cover showed 792,943,366 at
  December 5, 2025 (accession `0001628280-25-056742`). No 8-K filed after the 10-Q changes the count (8-K of 2026-08-27,
  accession `0001628280-26-059257`, is a director election).
- **Market cap:** 793.6M x $530.27 = **$420.8B**.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 10/06/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (fiscal year ended October 26, 2025), filed 2025-12-12, accession
  `0001628280-25-056742`; 10-Q Q3 FY2026 (quarter ended July 26, 2026), filed 2026-08-20, `0001628280-26-058235`;
  proxy DEF 14A filed 2026-01-28, `0001193125-26-027307`; 8-Ks of 2025-10-23 (`0001628280-25-046107`, workforce
  reduction), 2026-02-11 (`0001628280-26-007444`, BIS settlement), 2025-09-26 (`0001628280-25-042933`, 364-day credit
  facility), 2026-08-13 (`0001628280-26-056699`, Q3 results), 2026-08-27 (`0001628280-26-059257`); and for the span, the
  10-Ks for FY2016 (`0000006951-16-000068`), FY2018 (`0000006951-18-000041`), FY2019 (`0000006951-19-000046`), FY2020
  (`0000006951-20-000048`), FY2021 (`0000006951-21-000043`), FY2022 (`0000006951-22-000043`), FY2023
  (`0000006951-23-000041`) and FY2024 (`0000006951-24-000044`). Text copies are in `Test Runs/_research 2026-10-07 AMAT/`.
  **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025, $7,958M in
  `tools/run.py` (XBRL), equals the 10-K's MD&A table "Cash provided by operating activities $ 7,958" (`0001628280-25-056742`).
- `python tools/run.py AMAT` arithmetic lines only (output saved as `run_py_output.txt` in the research folder; nothing it
  prints as a rule, id or verdict is used, Part VII): owner cash as (OCF − SBC − capex), USD millions: FY2023 7,104;
  FY2024 6,910; FY2025 5,030; the five-year figure on the same basis 5,534. Capex FY2023 1,106, FY2024 1,190, FY2025 2,260;
  D&A 515, 392, 435. Stock pay 490, 577, 668. Other capital payments: finance-lease principal 7 (FY2023) and 102 (FY2024).
  The full owner-cash series is built under COMPUTATION below, from the filed lines.

**The balance sheets, ten year-ends,** read as the row asks, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** (the run closes before Q4, so they
are read here, as the brief asks). USD millions, from `tools/run.py`'s first-filed XBRL table, read against the filed
balance sheets (10-K FY2025 and the 10-Q above):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | debt (face) | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2016-10-30 | 14,588 | 7,217 | 3,406 | 2,279 | 2,050 | 3,316 | 575 | 3,343 | 15,252 |
| 2017-10-29 | 19,419 | 9,349 | 5,010 | 2,338 | 2,930 | 3,368 | 412 | 5,304 | 18,258 |
| 2018-10-28 | 17,773 | 6,839 | 3,440 | 2,565 | 3,722 | 3,368 | 213 | 5,309 | 20,874 |
| 2019-10-27 | 19,024 | 8,214 | 3,129 | 2,533 | 3,474 | 3,399 | 156 | 5,313 | 24,386 |
| 2020-10-25 | 22,353 | 10,578 | 5,351 | 2,963 | 3,904 | 3,466 | 153 | 5,448 | 27,209 |
| 2021-10-31 | 25,825 | 12,247 | 4,995 | 4,953 | 4,309 | 3,479 | 104 | 5,452 | 32,246 |
| 2022-10-30 | 26,726 | 12,194 | 1,995 | 6,068 | 5,932 | 3,700 | 339 | 5,457 | 37,892 |
| 2023-10-29 | 30,729 | 16,349 | 6,132 | 5,165 | 5,725 | 3,732 | 294 | 5,561 | 43,726 |
| 2024-10-27 | 34,409 | 19,001 | 8,022 | 5,234 | 5,421 | 3,732 | 249 | 6,259 | 49,651 |
| 2025-10-26 | 36,299 | 20,415 | 7,241 | 5,185 | 5,915 | 3,707 | 226 | 6,555 | 55,227 |
| 2026-07-26 (10-Q) | 43,522 | 25,626 | 7,037 | 7,691 | 6,564 | 3,873 | 315 | 6,544 | 61,391 |

What the figures say. (a) **Equity against goodwill:** goodwill has sat between $3.3B and $3.9B for ten years while equity
nearly quadrupled; no large deal entered the balance sheet (the TEL merger terminated in 2015 and the Kokusai purchase
terminated in fiscal 2021 with a $154M fee paid to KKR, FY2021 10-K `0000006951-21-000043`). Equity is held down by the
buybacks: treasury stock reached $46.2B at July 2026 while retained earnings rose from $15.3B to $61.4B. (b) **Cash:**
cash, cash equivalents and investments were $12.9B at FY2025 and $14.5B at July 2026 (10-Q note), against $6.5B of senior
notes plus $1.3B of short-term debt classified current at July 2026; net cash $7,957M (cash and investments $14,501M less
debt $6,544M; the investments include publicly traded and private equity securities). *(Corrected before the Q2 commit:
this line first read "net cash about $6.7B", an arithmetic slip in the Step 0 commit.)* (c) **Receivables and inventory against sales:** receivables were 77 days of sales in FY2016 (2,279
against 10,825), 67 days in FY2025 (5,185 against 28,368), and the 10-Q reports 77 days at July 2026, "primarily driven by
higher down payment invoices for which revenue has not yet been" recognized (10-Q `0001628280-26-058235`); inventory was
19% of sales in FY2016 and 21% in FY2025, and $6.56B at July 2026. The receivables rise at July 2026 is the one
balance-sheet movement to watch; the filer gives its reason. (d) **Debt:** face debt rose from $3.3B to $6.5B over the
decade, all senior unsecured notes plus commercial paper, while cash and investments grew faster. (e) **Retained earnings**
grew every year. What the figures cannot say: the share of revenue that export rules will allow into China, and which
process steps the next device generations will need; neither is on a balance sheet.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**? For a maker
of equipment whose sales fell 15% in FY2019 and whose largest market by geography is set by export rules, the answer
depends entirely on whether its economics can be foreseen, which is Q1. "the market is there to serve you and not to instruct you"
**[M2006-077]**: the price has risen from the $161 to $172 averages paid for shares in FY2025 (10-K, Item 5; 10-Q) to $530.27, and that rise
carries no information about value. "macro conclusions are — just never enter into the discussion" **[M2000-094]**:
the AI capital cycle and the trade dispute enter this run only as properties of this business (its customers, its China
share), never as a forecast. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close
to think about" **[M1996-084]**. **Contrary evidence, written down as found**, "in the first 30 minutes" **[M1997-127]**: (1) the filer's own
segment margins rose across two cycles (Semiconductor Systems 23.3% in FY2014, 27.3% in the FY2019 dip, 35.5% in FY2025),
which is evidence for a castle and against the TOO HARD reading that the technology rows invite; (2) the field's
structure, the same five or six suppliers named in each other's filings for a decade (LRCX 10-K FY2026 names Applied
Materials as its primary competitor in deposition and etch), is evidence that the economics have been more foreseeable
than "fast-moving technology" suggests; (3) against the business: China was 37% of revenue in FY2024 and 28% in the first
nine months of FY2026, a share set by export rules, and the company paid $252.5M to BIS in February 2026 under a
settlement that carries a suspended denial order.

## THE STANDING RULE
Owning this does not by itself put a buyer at risk of ruin: it is a marketable stock, and the rule binds the buyer's own
conduct, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**; bought
without borrowed money (leverage is "the one thing that ends — or can prevent you from playing out your hand"
**[M2004-065]**) and sized so that a 50% fall is borne, it passes. Nothing in the target's structure transfers a claim to
the buyer.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The parts, first.** Applied reports two segments, Semiconductor Systems and Applied Global Services; Display has not
been a reportable segment since FY2025 and sits in Corporate and Other (10-K FY2025, MD&A: "As of October 26, 2025,
management no longer considers Display a significant operating segment for separate reporting purposes", accession
`0001628280-25-056742`). Over FY2021 to FY2025 Semiconductor Systems earned $34,519M of segment operating profit and AGS
$8,302M (FY2021 and FY2022 from the FY2022 10-K `0000006951-22-000043`, FY2023 to FY2025 as recast in the FY2025 10-K):
**Semiconductor Systems is 80.6% of the five-year segment profit and decides**; by Q1's holding-company paragraph as
extended to operating segments (section B, 2026-10-06), it is the part that "matters", and Q1 is answered on it.

**The test as the text states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" and "some notion of how the industry will develop and where the company will
stand within the industry" **[M2012-065]**; the first step is "trying to identify the key variables in that particular
business, and evaluating how predictable they were" **[M1998-044]**.

**The key variables, from the filings, and how predictable each is.**
1. *Industry spending on fab equipment.* Cyclical: Semiconductor Systems revenue fell from $10,577M (FY2018) to $9,027M
   (FY2019) and its margin from 32.5% to 27.3% (FY2019 10-K `0000006951-19-000046`); total revenue rose from $9,072M
   (FY2014) to $28,368M (FY2025), and was $24,037M in the first nine months of FY2026, up 11%. The cycle itself is the
   ordinary kind and could be averaged.
2. *Applied's share of each technology inflection.* This is the variable the filer itself says cannot be held still:
   "products within the Semiconductor Systems segment are subject to significant changes in customer requirements,
   including transitions to smaller dimensions, increasingly complex chip architectures, new materials"; "While certain
   existing technologies may be adapted to new requirements, some applications create the need for an entirely different
   technological approach. The rapid pace of technological change can quickly diminish the value of current technologies
   and products and create opportunities for existing and new competitors"; "We must successfully anticipate technology
   inflections" (10-K FY2025, Item 1, Competition). Its "long-term growth strategy requires continued development of new
   materials engineering solutions" (Item 1, RD&E), and RD&E ran $3,570M, 12.6% of revenue, in FY2025 (14.2% in FY2016).
   The row fits the filer's description: "a lot of these businesses are quite dependent on the technology continuing to
   gallop" **[M1999-075]**.
3. *How much of the market export rules leave open.* China was 18% of revenue in FY2014, 17% in FY2015, 30% in FY2018,
   33% in FY2021, 27% in FY2023, 37% in FY2024, 30% in FY2025 and 28% in the first nine months of FY2026 (10-Ks FY2016,
   FY2019, FY2021, FY2023, FY2025; 10-Q `0001628280-26-058235`). The filer: "The U.S. government continues to issue new
   export licensing requirements"; it "could see increased competition from domestic equipment manufacturers in China
   resulting from local government incentives and funding as well as export controls" (10-K FY2025, MD&A and Item 1). The
   February 2026 BIS settlement "includes a denial order that is suspended and will be waived three years after the date
   of the order" if the audit terms are met (10-Q, Note 13). A variable that moved a fifth of revenue in each direction
   within a decade, on government decisions, is "important but unknowable" **[M2006-076]**.
4. *The two largest customers' plans.* Two customers were 19% and 15% of revenue in FY2025 and 20% and 14% in the first
   nine months of FY2026; Samsung's share ran 23% (FY2017), 13% (FY2018), below 10% (FY2019), 20% (FY2021), 12% (FY2024);
   TSMC's 15% (FY2017), 11% (FY2018), 14% (FY2019), 15% (FY2021), 19% (FY2023), 11% (FY2024) (customer notes of the
   10-Ks FY2018, FY2021, FY2024). Their capital plans are their own, by node and by year.

**The tests.**
- *Where will it be in ten years*, "where the business will be in 10 years" **[M2000-037]**: the industry will very likely be larger; where Applied will stand
  within it depends on variable 2, which the filer says can "quickly diminish the value of current technologies".
- *Do the past statements tell me the future ones*, "the financial statements will tell me the information that’s useful to me" **[M2008-033]**: they show the cycle and a rising margin; they do not
  show which process steps the next device architectures will need, or what share of them Applied will win.
- *Would the insiders write it down*, or "would not want to put down on paper their predictions" **[M2000-105]**: no instance found of a forecast of Applied's economics past the
  next year in the filings read (a search of the FY2025 10-K and the Q3 FY2026 10-Q for "2030" to "2039", "ten years",
  "10 years", "long-term model" and "long-term target" returned debt maturities and accounting dates only; the 8-K
  investor-meeting exhibits were not searched). The company's own outlook runs one quarter ahead in figures, revenue of
  $10,250M plus or minus $500M for Q4 FY2026, and one year in words, "we expect another strong growth year for Applied
  Materials in 2027" (press release, 8-K `0001628280-26-056699`, Ex. 99.1). The rivals' filings describe the field the
  same way: Lam, "The semiconductor capital equipment industry is characterized by rapid change and is highly
  competitive throughout the world" (10-K FY2026, `0000707549-26-000037`); KLA, "characterized by rapid technological
  development and product innovation" (10-K FY2026, `0000319201-26-000027`).
- *Can I name the winner, not just the industry*, or "we don’t have the faintest idea who the winners will be" **[M2012-067]**: the growth of the industry is visible, but "Just
  because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge what its profit
  margins and returns on capital will be as a host of competitors battle for supremacy" **[L2009-005]**. Lam's filing
  names Applied as its "primary competitor in the dielectric and metals deposition market" and, with Hitachi and Tokyo
  Electron, in etch; the filer names China's domestic makers as rising competitors. Who wins each new step is settled at
  each node.
- *Is the forecast about customers or about technology*, "it’s a different sort of analysis" **[M2017-019]**: about technology. The customer is a chipmaker
  choosing a tool at each node on "technical capability and differentiation, productivity, cost-effectiveness" (10-K
  FY2025, Item 1), not a matter of "what we think we can project out in terms of consumer behavior" **[M2023-030]**.
- *Do I doubt it is inside*: "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. I do.

**Contrary evidence, carried and not explained away**, as "evidence that flew in the face of his previous convictions" **[M1997-127]** is to be. Semiconductor Systems' margin was 23.3% in FY2014,
27.3% in the FY2019 dip and 35.5% in FY2025; AGS's stayed between 25.4% and 30.1% in all twelve years; the same rivals
have faced each other for the whole span. A reader could call this TOO HARD (WORK): a research pass could read the share
of each process step over two decades. I do not, for the reason the rows give: the deciding question is a forecast of
technology inflections and export policy ten years out, which the filer itself says can "quickly diminish the value of
current technologies", and which its insiders forecast one quarter and one year ahead. That is the nature of the
industry, not a document unread: "a business that must deal with fast-moving technology is not going to lend itself to
reliable evaluations of its long-term economics" **[L1993-023]**; "Our problem -- which we can't solve by studying up --
is that we have no insights into which participants in the tech field possess a truly durable competitive advantage"
**[L1999-018]**. The margin record is Q2 evidence, and Q2 is reached only by a business Q1 has passed.

**Routing.** "if something comes in where there’s a technological component that’s of significance, or where we think
the future technology could hurt the business as it presently exists" **[M1998-008]**, the same row says, "it won’t make
it through the filter" **[M1998-008]**. The framework sends fast-moving technology to TOO HARD, never OUT, since the
reason is ignorance and not a finding against the business: "It doesn’t mean it isn’t a good buy. It doesn’t mean it
isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. The test
between the two causes is test 5, whether insiders "would not want to put down on paper their predictions" **[M2000-105]**, answered above: the insiders do not write the ten-year forecast down.
A lower price would not reopen it.

- **VERDICT: TOO HARD (NATURE)**, the third of "in, out, and too hard" **[M2006-013]**, because "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]** and such a business "won’t make it through the filter" **[M1998-008]**: the ten-year economics of the
  deciding part turn on technology inflections and export rules that the filer says can quickly diminish its current
  products' value, and no insider writes the forecast down past a year. Q2 to Q10 and Q12 are NOT REACHED.

## Q2 to Q10, Q12: NOT REACHED (Q1 closed the file TOO HARD (NATURE)).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1**: the ten-year economics of Semiconductor Systems, 80.6% of five-year segment profit,
turn on technology inflections and export rules that the filer says can quickly diminish the value of its current
products, and no insider writes the forecast down past a year. Q7 was not reached; the COMPUTATION below puts the
central range at $148 to $280 a share against $530.27. **Integrity facts recorded, not judged** (the BIS settlement and
its suspended denial order; see AFTER THE STOP, Q5). No research pass is opened: the cause is NATURE, and a lower price
does not reopen it: "It just means that we don’t know how to evaluate it." **[M2000-038]**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on a later question, each with its source, written "in the first 30 minutes" **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).

**Q2 (the castle).**
- *The parts table* (segment operating profit FY2021 to FY2025; FY2021 and FY2022 from the FY2022 10-K, FY2023 to FY2025
  recast in the FY2025 10-K): Semiconductor Systems $34,519M, 80.6%, decides; AGS $8,302M, 19.4%; Display folded into
  Corporate and Other from FY2025 (its margin had fallen to 5.8% in FY2024, 10-K FY2024 `0000006951-24-000044`).
- *Segment margins over two cycles* (10-Ks FY2016, FY2019, FY2022, FY2023, FY2025): Semiconductor Systems 23.3% (FY2014),
  23.0%, 26.3%, 33.3%, 32.5% (FY2018), 27.3% (FY2019 dip), 32.7%, 38.8% (FY2021), 37.1%, 36.0% (34.9% recast), 35.1%,
  35.5% (FY2025), 34.0% for nine months of FY2026 (37.7% in Q3). AGS 25.4% (FY2014) to 30.1% (FY2021), 28.1% (FY2025),
  29.2% for nine months of FY2026. Display 23.8% (FY2014) to 5.8% (FY2024). Note: the FY2014 to FY2016 segment figures
  sit beside a Corporate and Other line that carried stock pay, and later years were recast; the series is as filed.
- *The competitor row, same metric, from their own filings* (fiscal years as each files them): operating margin, first
  three years against last five:

  | company | filing | operating margin, early | operating margin, last five | owner-cash margin (OCF − SBC − capex), last five |
  |---|---|---|---|---|
  | Applied Materials | 10-K FY2025 `0001628280-25-056742` | 25.4% (FY2017-19) | 29.4% (FY2021-25) | 21.1% |
  | Lam Research | 10-K FY2026 `0000707549-26-000037` | 26.4% (FY2017-19) | 31.7% (FY2022-26) | 22.2% |
  | KLA | 10-K FY2026 `0000319201-26-000027` | 23.2% pre-tax (FY2014-16); operating income not tagged after FY2014 | 37.5% pre-tax (FY2022-26) | 28.6% |
  | ASML | **20-F** FY2025 `0001628280-26-011378` (US GAAP, EUR; a foreign filer's annual report, flagged) | 25.8% (2017-19) | 33.2% (2021-25) | 31.1% (customer prepayments swing its operating cash: 53% in 2021, 11% in 2023) |
  | Tokyo Electron | **not an SEC filer, flagged**; no row | | | |

  Applied's margins are the lowest of the four in the last five years on both measures (KLA's on pre-tax income, not
  the same line). All four operating (KLA pre-tax) margins rose from the first span to the last; owner-cash margins rose
  for Applied (18.7% to 21.1%), KLA and ASML, and fell slightly for Lam (23.0% to 22.2%). China's share of revenue in the rivals' own filings: Lam 42% (FY2024), 34% (FY2025), 34%
  (FY2026); KLA 43%, 33%, 30%; ASML 36.1% (2024), 29.1% (2025).
- *The field's returns over the last full cycle* are high for all four on both measures; nothing here is judged.
- *Pricing:* the filer credits "increases in average selling prices" in the FY2025 10-K and the Q3 FY2026 10-Q
  segment discussions.
- *Who they fight:* Lam names Applied as its "primary competitor in the dielectric and metals deposition market" and,
  with Hitachi and Tokyo Electron, in etch (Lam 10-K FY2026).

**Q3 (capital).** Capex rose from $241M (FY2014) and $668M (FY2021) to $2,260M (FY2025), $1,696M of it in Corporate and
Other, "primarily for investments in real property and improvements, demonstration and testing equipment, manufacturing
and network equipment" (10-K FY2025, MD&A); $1,988M in the first nine months of FY2026. Depreciation and amortization
was $435M in FY2025. RD&E 15.7% of revenue (FY2014), 10.7% (FY2022), 12.6% (FY2025). Equity was $20.4B at FY2025 on
operating income of $8.3B; equity is shrunk by $46.2B of treasury stock, so return on equity flatters (the row's
warning on equity kept low by buybacks applies at Q3 when reached).

**Q4 (the accounts).** (a) Depreciation fell from $471M (FY2023) to $346M (FY2024) "as a result of changes in certain
assets’ useful lives effective as of the beginning of fiscal 2024" (10-K FY2024, MD&A). (b) Restructuring: $181M in
FY2025 (8-K `0001628280-25-046107`), $12M in nine months of FY2026; earlier charges in FY2015 (solar). (c) FY2025 tax:
a $659M remeasurement of deferred tax assets on new Singapore incentives and a $407M valuation allowance on CAMT credits
(10-K FY2025); Singapore "conditional reduced tax rates" begin to expire in fiscal 2030. (d) A goodwill impairment of
$41M in Q4 FY2025. (e) The earnings releases feature non-GAAP figures (record "non-GAAP EPS $3.50" against GAAP $3.17 in
Q3 FY2026; the non-GAAP measure excludes the $253M legal settlement, restructuring and strategic-investment gains and
losses, and keeps stock pay as a cost), give one-quarter guidance (revenue $10,250M plus or minus $500M for Q4 FY2026)
and state that non-GAAP measures are used "as performance measures in its executive compensation program" (Ex. 99.1 to
8-K `0001628280-26-056699`). Under section A these are weighed at Q4 and carried to Q5; they are recorded here only.
(f) Receivables at 77 days of sales at July 2026, against 67 at FY2025, which the filer ties to down-payment invoices.

**Q5 (the people): integrity facts, recorded, not judged.** (a) "Since 2022, we have received multiple subpoenas from
government authorities requesting information relating to certain China customer shipments and export controls
compliance, including from the U.S. Department of Justice, the U.S. Commerce Department Bureau of Industry and Security,
and the U.S. Securities and Exchange Commission. We also have received subpoenas from the U.S. Department of Justice
requesting information related to certain federal award applications and information submitted to the federal
government." (10-K FY2025, Note 14.) (b) On February 11, 2026 the DOJ and the SEC closed their inquiries with no
enforcement action, and the company settled with BIS for $252.5M, agreeing to internal audits of its export-controls
compliance (8-K `0001628280-26-007444`); the settlement "includes a denial order that is suspended and will be waived
three years after the date of the order, provided that we have timely completed the audit requirements" (10-Q
`0001628280-26-058235`, Note 13). (c) The status of the DOJ subpoenas on federal award applications: no mention found in
the Q3 FY2026 10-Q (search for "federal award"). (d) The CEO, Gary Dickerson, has run the company since 2013 (President
since 2012); total pay $29.6M in FY2025, $27.8M in FY2024, $26.9M in FY2023, CEO pay ratio about 330 to 1 (proxy
`0001193125-26-027307`). Incentive measures named in the proxy: relative TSR, non-GAAP gross margin, non-GAAP operating
margin and wafer fabrication equipment market share; non-GAAP EPS and non-GAAP gross margin are bonus targets. A clawback
policy and stock-ownership guidelines are stated.

**Q6 (the money and the owners).** Buybacks: $1,325M (FY2015), $1,892M, $1,172M, $5,283M (FY2018), $2,403M, $649M,
$3,750M, $6,103M (FY2022), $2,189M, $3,823M, $4,895M (FY2025), $1,177M in nine months of FY2026 (cash-flow statements).
Average prices paid: $172.46 in Q4 FY2025 and $160.95 for the first nine months of FY2025; $343.16 for the first nine
months of FY2026 and $455.43 in Q3 FY2026 (10-K Item 5; 10-Q Note on stockholders' equity). The programme names no price
above which it stops: "$10.0 billion in repurchases" authorized in March 2025 on top of March 2023's $10.0B, $12.8B
remaining at July 2026. Diluted shares fell from 1,231M (FY2014) to 808M (FY2025). Dividends $1,384M in FY2025; the
quarterly dividend rose from $0.46 to $0.53 in March 2026. Under the buyback convention, prices paid are read against the
bottom of the Q7 range: by the COMPUTATION below that bottom is $148 a share (central basis); the FY2025 purchases at
about $161 to $172 sit above it, and the FY2026 purchases at $343 and $455 sit above the top of the central range. Not
weighed here. Acquisitions small: cash paid $262M in nine months of FY2026, $441M in FY2022; the Kokusai purchase
terminated with a $154M fee (FY2021).

**Q9 (ruin).** Senior unsecured notes $6.5B, commercial paper programme up to $4.0B, a $2.0B five-year and a $2.0B 364-day
revolver (the latter maturing September 2026), none drawn at FY2025; short-term debt $1,299M at July 2026; cash and
investments $14,501M (10-Q). Purchase obligations $10.6B, $7.3B due within twelve months (10-K FY2025). The suspended BIS
denial order would, if reinstated, "prohibit us from exporting certain of our products outside of the United States"
(10-Q, Risk Factors). Two customers 34% of nine-month revenue.

**Q12.** Nothing found that bears on it.

---
## COMPUTATION, NOT A CLEARANCE
*The file closed at Q1. Everything in this section is arithmetic reported at the owner's request (the brief's reporting
convention); it is not Q7, carries no entry language, and decides nothing (operator rule 3). Script and output:
`value.py`, `value_output.txt` in the research folder.*

**Owner cash after every real cost, after the company's own tax** (OCF − stock pay − capital spending − cash paid for
acquisitions − finance-lease principal; USD millions; cash-flow statements via XBRL, OCF FY2025 checked against the 10-K):

| FY | OCF | stock pay | capex | D&A | acquisitions | owner cash, all spending | owner cash, maintenance only (D&A as the guess) |
|---|---|---|---|---|---|---|---|
| 2019 | 3,247 | 263 | 441 | 363 | 28 | 2,515 | 2,593 |
| 2020 | 3,804 | 307 | 422 | 376 | 107 | 2,968 | 3,014 |
| 2021 | 5,442 | 346 | 668 | 394 | 12 | 4,416 | 4,690 |
| 2022 | 5,399 | 413 | 787 | 444 | 441 | 3,758 | 4,101 |
| 2023 | 8,700 | 490 | 1,106 | 515 | 25 | 7,072 | 7,663 |
| 2024 | 8,677 | 577 | 1,190 | 392 | 0 | 6,808 | 7,606 |
| 2025 | 7,958 | 668 | 2,260 | 435 | 29 | 5,001 | 6,826 |

Five-year averages (FY2021-25): **$5,411M** all spending; **$6,177M** maintenance only. Depreciation is taken as the
maintenance guess, the charge being "not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**: the filing describes the FY2025 capex step-up as real property, demonstration and test
equipment, which reads as building for growth, and the FY2024 useful-life change lowers depreciation, so the guess may be
low. All-equity basis: add back after-tax interest expense and remove after-tax interest income on the cash (both at 21%,
a CONVENTION of this run: the cash tax rate swings, and the statutory rate is the filer's own reconciliation start);
the five-year averages barely move ($6,176M maintenance only), because interest income ($26M to $486M) and interest
expense ($228M to $269M) roughly offset. Cash taxes paid were 15.7% of pre-tax income over FY2021-25; at the 21% statutory
rate owner cash would be about $422M a year lower (Singapore's reduced rates begin to expire in fiscal 2030; section E's
rule names carryforwards and credits, not reduced-rate incentives, so it is shown and not applied).

**Construction** (the Q7 CONVENTION and its specifics, applied as arithmetic): base the five-year average; growth shown
on aggregate owner cash between the window's end years, carried ten years, then zero nominal growth; discounted at the
sovereign 5.64%; the ends are the no-growth and shown-growth cases; maintenance-only central, all-spending beside it;
acquisitions deducted with total growth credited. Net debt at July 26, 2026: debt $6,544M less cash and investments
$14,501M = **net cash $7,957M**, added to the whole-business range; operating leases ($565M obligation at FY2025) left
out. Shares 793.6M.

| case | basis | base | growth shown | range per share | top/bottom | fair price |
|---|---|---|---|---|---|---|
| **literal window FY2021-25, maintenance only** | **all-equity (central)** | 6,176 | 8.5% | **$148 to $280** | 1.95x | **$119** |
| literal window FY2021-25, maintenance only | equity-only (beside) | 6,177 | 9.8% | $138 to $301 | 2.18x | $116 |
| literal window FY2021-25, all spending | all-equity | 5,410 | 1.7% | $131 to $148 | 1.14x | $82 |
| literal window FY2021-25, all spending | equity-only | 5,411 | 3.2% | $121 to $155 | 1.28x | $76 |
| whole cycle, maintenance only | all-equity | 5,212 | 17.4% | $126 to $467 | 3.93x | $155 |
| whole cycle, all spending | all-equity | 4,647 | 14.6% | $114 to $338 | 3.15x | $121 |

- **The whole-cycle variant** (the window holds the FY2021-22 boom; the brief asks for it): the owner-cash series has had
  no second trough since FY2019, so no full cycle has closed. CONVENTION of this run: base = the FY2019-25 average (from
  the last trough to the latest year); growth measured between the FY2014-18 average and the FY2019-25 average, 17.4%
  (maintenance only) and 14.6% (all spending). Rationale: specific (a) asks for successive cycle averages, and this is the
  nearest the series allows. Its width exceeds three to one, which by itself would close Q7 TOO HARD had Q7 been reached.
- **Fair price** (Part VII reporting figure): the price at which the midpoint of the range earns about 10% after the
  company's own tax. Reading used (a CONVENTION of this run, since the text does not say how a midpoint value becomes a
  cash stream): the growth rate whose value at 5.64% equals the range's midpoint (4.9% on the central basis) is carried
  as the stream, and that stream is discounted at 10%; on the all-equity basis the whole-business figure plus net cash,
  per share. **Central: $119 (all-equity); equity-only beside: $116.**
- **Against the price** of $530.27: the price is above the top of every range above, including the whole-cycle maintenance
  case's top ($467), and is about 4.5 times the central fair price. At the price, the central all-equity base needs about
  16.9% a year of growth for ten years to be worth the price at 5.64%, and 27.2% at 10%. The owner-cash yield at the
  price is 1.47% (maintenance only) and 1.29% (all spending), against the 5.64% sovereign.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits "Step 0, foundations and standing rule", "Q1 closed TOO HARD (NATURE)", then this close.
- [x] Dispatched: the brief allowed per-question commits; the lock was held by the dispatching session (read at start);
      the fold into the register is the dispatcher's, and until then this run binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `check_ids.py` in the research folder, PASS); every filing fact carries its accession.
- [x] The order was kept; Q1, the first STOP, closed the run; nothing after it is a clearance; the figures after it are
      headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the US Treasury; the price quote
      flagged as an aggregator's.
- [x] Contrary evidence written down as found (foundations; Q1); the facts for later questions are under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its rule, id and verdict lines were ignored.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 carries a business both ways.** Its "What it rules OUT" list still names businesses "quite dependent on the technology continuing to gallop"
**[M1999-075]** as OUT, while the routing paragraph and "Sent to TOO HARD, not OUT" send fast-moving technology
to TOO HARD. Applied is both: its growth "requires continued development" and its industry is one of "rapid technological
change". I followed the routing paragraph (the later correction, 2026-10-05) and the rows' own reason, "we don’t know how to
evaluate it" **[M2000-038]**; the list should say which governs when both describe the business. (2) **WORK or NATURE is close here,
and test 5 does the deciding alone.** The castle evidence (two cycles of rising margins, a stable set of rivals) is the
kind of fact a research pass reads, and the framework forbids weighing it before Q1 passes; a second analyst could fairly
call the box TOO HARD (WORK). The text gives no rule for a business whose past economics were steady inside an industry
its own filer calls fast-changing. (3) **Section E's tax rule** names carryforwards and credits that run out inside ten
years; Applied's low tax comes from Singapore reduced-rate incentives that begin to expire in fiscal 2030, which the rule
does not reach; I showed the statutory-rate effect and did not apply it. (4) **The all-equity basis** says "owner cash
before interest"; with net debt defined net of cash and securities, interest income on that cash must also come out of
owner cash or the cash is counted twice; the text does not say so, and I removed it. (5) **The fair price** is defined as
the price at which "the midpoint of the range earns the floor", but the range is a range of values, not of cash streams;
I chose the stream whose value at the sovereign equals the midpoint, and say so. (6) **Specific (a) on cycles** presumes a
closed cycle; Applied's owner cash has had no second trough since FY2019, so I built the nearest variant and confessed it.

**Errors in the brief.** (a) Its lines of evidence name "the three segments (Semiconductor Systems, Applied Global
Services, Display)": Display has not been a reportable segment since FY2025 and is in Corporate and Other (10-K FY2025;
the 10-Q calls the line "Other"), and the 200mm equipment business moved from AGS to Semiconductor Systems from Q1
FY2026. (b) The canonical brief's "Read first" sends the reader to "Part VI (the Q7 range convention and the floor)": the
range convention and the floor are written in Q7 (section IV); Part VI only lists them among the confessed conventions.
(c) The canonical brief calls the floor "about ten percent pre-tax" in the same sentence that applies it after the
company's own tax; the framework resolves this (Q7, Whose tax: "pre-tax" means before the holder's tax), but the brief's
wording, read alone, invites the wrong tax treatment.
