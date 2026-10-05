# Company Run — Gencor Industries, Inc. (NYSE American: GENC) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The brief for this run forbids opening `PORTFOLIO.md` (blind
rule), so the analyst does not know whether the operator holds this name. The analyst holds no view formed before the reading.

**Exchange note:** the brief named NASDAQ. The filings say otherwise: the common stock "is traded on the NYSE American LLC
under the symbol "GENC."" (10-K FY2025, Item 5, accession 0001193125-25-312742). The run uses the filing.

**CONTAMINATION, declared:** the session's opening context showed recent commit subjects naming the boxes of other runs
(ENSG, OSIS, MBUU); none concerns this company and none was opened. No `Test Runs/` file about Gencor, no holding review,
no `Screens/` reading list, register or resume-state file was opened. The brief itself described the company in one
paragraph (asphalt plants, family control, securities portfolio); every such fact was re-read in the filings below. The
user's memory index, loaded with the session, names no company verdict for GENC.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $17.64 (close 2026-10-05; Yahoo chart endpoint through `tools/sources.py`; **aggregator, live quote only,
  flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: Common 12,338,845; Class B 2,318,857; arithmetic sum 14,657,702
  (10-Q for the quarter to 2026-06-30, filed 2026-08-10, cover as of 2026-08-07, accession `0001193125-26-341429`;
  `python Screens/cover_shares.py GENC`). **Charter note read before adding the classes:** "Common stock and Class B
  common stock shareholders have equal rights with respect to dividends, preferences, and rights, including rights in
  liquidation" (10-K FY2025, Note 11); Class B elects about 75% of the board and common about 25%. Economically equal,
  so the classes are added for value; they are not equal in control.
- **Market cap:** 14,657,702 x $17.64 = **$258.6M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025 (year to 2025-09-30), filed 2025-12-09, accession `0001193125-25-312742`: Items 1, 1A, 1C, 2, 3, 5, 7,
    8 (both audit reports, statements, Notes 1 to 12), 9A, exhibit index.
  - 10-K FY2024, filed **2025-06-27, about six months late**, accession `0001193125-25-150836` (searched for restatement,
    revision and error-correction language: none; the cover's error-correction box is unticked).
  - 10-Qs: quarter to 2026-06-30, filed 2026-08-10 (`0001193125-26-341429`), read in full for statements, MD&A, Item 4;
    quarter to 2026-03-31, filed 2026-06-12 after an NT 10-Q (`0001193125-26-269656`).
  - Proxy: DEF 14A filed 2026-01-28, accession `0001193125-26-026856`, read in full.
  - 8-Ks and late-filing notices since 2024-11: `0001193125-24-252594` (auditor MSL to Forvis Mazars),
    `0001193125-24-280481` (NT 10-K: material weaknesses), `0001193125-25-004061` (NYSE delinquency notice),
    `0001193125-25-030825` (Forvis Mazars dismissed mid-audit; Exhibit 16.1 letter, which agrees with the company's
    statements), `0001193125-25-149714` (NYSE extension), `0001193125-25-166050` (compliance regained),
    `0001193125-25-329707` (founder E.J. Elliott retires; Marc Elliott chairman), `0001193125-26-026824` (auditor BPB
    to Carr, Riggs & Ingram), `0001193125-26-212435` (Item 5.01 change in control), `0001193125-26-219906` (NT 10-Q),
    `0001193125-26-232121` (CFO retires), `0001193125-26-251421` (NYSE delinquency notice again),
    `0001193125-26-257347` (interim CFO), `0001193125-26-274110` (compliance regained).
  - History: 10-K405 FY2000 filed 2001-10-25 (`0001021408-01-508738`; restatement, bankruptcy); 10-Ks FY2003
    (`0001193125-03-099730`), FY2004 (`0001193125-04-217456`), FY2008 (`0001193125-08-252779`), FY2012
    (`0001193125-12-502875`), FY2015 (`0001193125-15-398371`) to FY2023 (each by its own accession in the research
    folder); Schedule TO-I of 2003-11-13 (`0000950144-03-012760`) with its offering circular (exhibit (a)(1)) and
    Amendment 2 (`0000950144-03-013422`); Schedule 13D of 2003-12-02 (`0001047469-03-038886`); Schedule 13D/A of
    2008-05-09 (`0000950123-08-005435`).
  - **One figure cross-checked against the filed statement:** FY2025 net revenue $115,437,000 in the filed income
    statement (10-K FY2025, page 27) equals the XBRL value 115,437 (thousands); FY2025 total shareholders' equity
    $211,802,000 on the filed balance sheet equals the `tools/run.py` table. Both agree.
- `python tools/run.py GENC` arithmetic lines only (output saved in the research folder). Its defects, checked against
  the filing, and what was done:
  - **OCF includes the securities portfolio.** The company classes its marketable securities as trading and runs their
    purchases, sales and its own transfers of operating cash through operating cash flow ("Marketable securities
    (18,460,000)" in FY2025; "the transfer of $15,000,000 from the operating cash account to the investment portfolio",
    10-K FY2025 MD&A). Reported OCF of $3.07M (FY2025) is therefore not the business's cash. **The tool's "OE lo / OE
    hi" lines are not used.** Owner cash below is rebuilt from the filed income statements, cash-flow working-capital
    lines and capital spending.
  - Share basis: weighted average 14.7M; matches the cover sum (no splits since the 3-for-2 of 2016).
  - Stock pay: the tool prints 0; the filings agree for FY2022 to FY2025 ("There were no equity compensation plans and
    arrangements", Note 11; proxy: "There are no outstanding equity awards"). Option expense was $71K a year to FY2020.
  - Debt column: zero; the filing agrees ("The Company had no long-term or short-term debt").
  - D&A and capital spending match the filed cash-flow statements.

### The balance sheets first, ten year-ends (filed statements; $ thousands)

| FY end Sep | Cash + securities | Inventory, net | Contract assets | PP&E net | Total liabilities | Equity | Retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 104,157 | 11,634 | 4,921 | 5,239 | 8,507 | 120,205 | 107,881 |
| 2017 | 110,819 | 16,687 | 6,768 | 5,722 | 13,975 | 128,918 | 116,299 |
| 2018 | 112,070 | 18,214 | 11,900 | 7,889 | 10,844 | 142,179 | 128,863 |
| 2019 | 115,624 | 25,366 | 13,838 | 8,389 | 9,857 | 155,515 | 141,897 |
| 2020 | 125,082 | 27,090 | 6,405 | 8,341 | 9,874 | 161,220 | 147,428 |
| 2021 | 118,208 | 41,888 | 1,903 | 11,801 | 12,173 | 167,289 | 153,233 |
| 2022 | 98,881 | 55,815 | 2,118 | 13,491 | 12,396 | 166,917 | 152,861 |
| 2023 | 101,283 | 71,527 | 1,508 | 13,246 | 14,165 | 181,583 | 167,527 |
| 2024 | 115,409 | 63,762 | 9,339 | 11,472 | 11,980 | 196,141 | 182,085 |
| 2025 | 136,301 | 53,503 | 12,208 | 11,079 | 10,794 | 211,802 | 197,746 |
| 2026-06-30 (10-Q) | 164,169 | 46,985 | 6,397 | 11,220 | 14,215 | 224,769 | 210,713 |

Sources: 10-Ks FY2016 to FY2025 balance sheets (accessions in the research folder; first-filed vintage; FY2018 inventory
was later restated upward to 21,890 when the company moved from LIFO to FIFO in the fourth quarter of FY2019, 10-K FY2019
Note 1, `0001193125-19-310985`); 10-Q `0001193125-26-341429`.

**What the balance sheets say, read before the income account** **[M2025-032]**. No debt in any year, no goodwill, no
preferred, no stock issued except option exercises before FY2022. Equity rose $91.6M from FY2016 to FY2025 and not a
dollar was paid out. Of that, cash and securities rose only $32.1M; operating capital (inventory, contract assets,
receivables, prepaid and PP&E, less payables, deposits and accruals) rose from $16.3M to $72.8M, so about $57M of the
retained profit went into the yard, including the $13.8M Blaw-Knox paver purchase of October 2020. Inventory went from
16.6% of revenue (FY2016) to 68.1% (FY2023) and 46.3% (FY2025), while the slow-moving and obsolete reserve rose from
$9.8M (FY2023) to $13.3M (FY2024) and $15.6M (FY2025), 22.5% of gross inventory (10-K FY2025, Note 1 and Note 2; a
Critical Audit Matter in the auditor's report). That is the pattern the rows name: "inventories look out of line, you
know, with sales" **[M1995-064]**, and in this industry by name, "the construction equipment business" where "there’s
your profit sitting in the yard" **[M2008-036]**. What the figures cannot say: whether the reserved inventory has any
value, and how much of the remaining $47M is permanent. The securities ($137.9M at 2026-06-30) are Level 1 and Level 2
only (no Level 3): $86.5M government securities, $28.7M corporate bonds, $12.6M ETFs, $6.3M equities, $2.7M mutual
funds, $1.0M cash (10-Q MD&A), managed by "a professional investment management firm".

**History read for the record (written down as found** **[M1997-127]**):
- 1999 to 2001: accounting irregularities at the UK subsidiary Gencor ACP (opening net assets overstated by about $7M,
  FY1998 income overstated); "the disqualification of its then auditors of record, Deloitte & Touche, by the SEC"; trading
  suspended on the American Stock Exchange on 1999-02-22 and the stock delisted on 2000-06-01; a securities class action
  settled; Chapter 11 from 2000-09-13 (involuntary petition by lenders in April 2000), emerging 2001-12-31 with "100%
  payment of all secured and unsecured creditors and no dilution or diminution to the equity holders" (10-K405 FY2000,
  `0001021408-01-508738`; 10-K FY2003, `0001193125-03-099730`). In the company's favour: creditors were paid in full and
  equity was not diluted.
- 2001 to 2013: the cash pile came from synthetic fuel, not asphalt. Gencor built four synfuel plants for Carbontronics
  and took membership interests that "distributed significant cash to the Company from 2001 to 2010" (10-K FY2025,
  Item 1). Equity went from $15.3M (FY2004) to $99.0M (FY2008) while operating income in those five years summed to
  $17.5M (10-K FY2008 selected data, `0001193125-08-252779`).
- 2003: the controlled company offered to take itself private (see Q5 facts below).

---
## THE FOUNDATIONS (not a gate)
Three bear here. A share is a business: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. For a minority holder of a company that has paid no dividend and bought no stock in more than two
decades, the market quotation is the only door through which the retained cash ever reaches him, so the question cuts
harder than usual. No macro enters: the expiry of the federal highway law on 2026-09-30 (10-Q MD&A) is a forecast about
government, and "we just don’t get into the macro factors" **[M2000-094]**; it is not used for or against the name; the
dependence of demand on public road money is used only as a property of the business. The market serves: the quote "just
tells us prices" **[M2006-077]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the castle evidence
against is in Q2; (2) the evidence for: Gencor's operating margin beat Astec's over 2009 to 2025 taken whole (6.6% against
3.3%), backlog was $79.2M at 2026-06-30 against $26.2M a year earlier, parts and components are $27.0M (23%) of revenue,
no debt, and the FY2024 audit, though late, found no restatement; (3) the integrity and stewardship facts in the post-stop
section were found during the Step 0 reading, before Q2 was answered, and are recorded there, not weighed.
*(The line asked for a pre-committed falsifier until 2026-10-05; removed under the v5 scope directive.)*

## THE STANDING RULE
A cash purchase of a listed minority stake, unlevered and sized within the buyer's means, cannot ruin the buyer: "We are
never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. Nothing about the
target changes that. Clear.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- The test: "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**, and "I understand the economic dynamics of the
  industry" **[M2011-014]**.
- The parts (holding company read by its parts, Q1 CONVENTION):
  - **The machinery business.** Hot-mix asphalt plants (the H&B line "first manufactured in 1894"), combustion systems,
    thermal fluid heaters, Blaw-Knox pavers (bought from Volvo CE in October 2020), and parts. Three US plants, 318
    employees, one segment, 89.3% of FY2025 revenue in the US and 10.5% in Canada (10-K FY2025, Items 1 and 2, Note 1). The
    product changes slowly; no fast-moving technology is described. Key variables **[M1998-044]**: (1) road-building
    demand, which the filer ties to "the level of federal and state funding for domestic highway construction and
    repair, the replacement of existing plants, and a trend towards efficient, larger plants"; (2) price against a
    handful of larger rivals; (3) steel cost and how fast it passes through. All three are visible in 26 years of filed
    statements (FY2000 to FY2025), which show the pattern the future statements will show: a cyclical maker whose
    margin swings from loss to low teens **[M2008-033]**. The level of demand in a given year is not foreseeable; the kind
    of business it will be in ten years is.
  - **The securities.** Government and corporate bonds, ETFs, a few equities, Level 1 and 2, outside manager. Read.
- Routing: no fast-changing industry; not a bank; both parts that matter can be understood.
- Doubt test: "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The
  doubt here is about how good the business is, not about what it is; that belongs to Q2.
- **VERDICT: IN.** The economics of an asphalt-equipment maker tied to public road money, and of a bond portfolio, can be
  foreseen in kind ten years out **[M2012-065]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. A castle here must be something that "protects excellent returns on
invested capital" **[L2007-004]**.

- **The attacker with money; new entrants.** The field is crowded and entered: Astec lists more than twenty competitors in
  its Infrastructure Solutions segment, Gencor among them, calls the segment "highly competitive and fragmented", and
  bought a portable asphalt plant maker (CWMF) on 2026-01-01 (Astec 10-K FY2025, `0000792987-26-000011`, Item 1). The
  one well-funded rival that left, Volvo CE, left the North American paver line by selling it to Gencor (10-K FY2021,
  `0001193125-21-361338`): an exit by a big owner, not a barrier. No evidence that money could not take share from Gencor.
- **Pricing power and the agony before a rise.** The filer: "The markets for the Company’s products are highly
  competitive"; "The principal competitive factors include quality, price, delivery, availability, financing, and
  technological capabilities"; "Some of the Company’s competitors have greater financial and marketing resources";
  "if the current competitors enhance their products or lower their prices for competing products, the Company may lose
  sales or be required to lower the prices it charges"; "Market conditions could limit the Company’s ability to raise
  selling prices to offset increases in material and/or labor costs" (10-K FY2025, Items 1 and 1A). Its rivals' prices
  set its own, the case the rows describe as "whatever he charged for gas was my price." **[M2012-109]**. Gross margin
  swung from 19.9% (FY2022) to 29.5% (nine months FY2026). In the cost surge of FY2021 and FY2022 revenue rose 34% (FY2020
  $77.4M to FY2022 $103.5M) while operating margin fell from 7.2% to 0.8% and 4.0%; margins came back in FY2023. The rows
  allow a lag ("over time the businesses with strong competitive positions manage to pass through increases in raw
  material costs" **[M2005-017]**); the two-year lag is recorded as weak pass-through, not as failure.
- **Unit volume and share of mind; the brand.** No market share is disclosed (search of the 10-K FY2025 for "market
  share" finds it only in the risk factor that the company may "cause a loss in market share"). The brands are old (H&B
  1894, Blaw-Knox 1917) and the filer counts "brand recognition" among its factors; no filing shows a customer paying
  more for the name.
- **The low-cost position (the one exception in a commodity-type field).** The rows: "being the low-cost producer is
  all-important" **[L2000-017]**, because "the low-cost producer can put you out of business" **[M1997-010]**. The test
  is the last full downturn. Gencor, fiscal 2009 to 2015: operating margin -8.4%, -5.5%, -2.9%, +0.6%, +5.3%, -0.1%,
  -2.0%; five loss years of seven; aggregate -2.0% (10-K FY2012 selected data, `0001193125-12-502875`; 10-K FY2016
  income statements, `0001193125-16-783228`). The main rival's asphalt plant business in the same years: Astec "Asphalt
  Group" segment profit on external revenue 12.7% (2010), 11.3% (2011), 9.0% (2012) (Astec 10-K FY2012,
  `0000792987-13-000008`, segment note; measured before US federal tax and corporate overhead), and its "Infrastructure
  Group" 8.2% (2013), 7.6% (2014), 7.9% (2015) (Astec 10-K FY2015, `0000792987-16-000063`). Astec consolidated, after
  all overhead, earned 5.2% in aggregate over 2009 to 2015 and lost money in none of those years. When the market
  shrank, the larger rival earned and Gencor did not. On this evidence Gencor is not the low-cost producer.
- **Would the customer still choose it over the low bid?** Price is a named principal factor and customers pay
  "a significant up-front deposit" and "full payment ... prior to shipment" (Note 1): the filer reads as a seller of
  custom capital goods on bid, not of a product asked for by name. No customer above 10% of FY2025 revenue.
- **Ask the competitors.** Astec names Gencor as one of many, not as the one to fear (Astec 10-K FY2025 and FY2022,
  `0000792987-23-000015`, competitor lists).
- **Widening or narrowing.** Revenue rose from $39.2M (FY2015) to $115.4M (FY2025), partly bought (pavers); operating
  margin 12.1% to 12.8% in FY2023 to FY2025 against Astec's 3.6%, 1.8%, 4.7% in 2023 to 2025. Those are boom years for
  road money; the rows rule out crediting a high return before ruling out "a cyclical peak in earnings, a monopolistic
  position, or leverage" **[L1994-009]**, and the trough record above is the only test of the off years.
- **What could destroy it** **[M2000-014]**: a rival cutting price (the filer's own risk factor), the scale of rivals, and
  the funding cycle (not used: macro).

**The competitor row** (same metric, competitors' own filings):

| Company | Operating margin, aggregate | Span | Source |
|---|---|---|---|
| Gencor | -2.0% (5 loss years of 7) | FY2009 to FY2015 | 10-K selected data and income statements, `0001193125-12-502875`, `0001193125-16-783228` |
| Astec, consolidated | 5.2% (0 loss years of 7) | CY2009 to CY2015 | Astec XBRL facts; FY2015 revenue $983.2M checked against the filed segment table, `0000792987-16-000063` |
| Astec, Asphalt Group segment | 12.7%, 11.3%, 9.0% (segment basis, before federal tax and corporate overhead) | CY2010 to CY2012 | Astec 10-K FY2012, `0000792987-13-000008` |
| Gencor | 10.0% (0 loss years) | FY2016 to FY2025 | Gencor 10-Ks FY2016 to FY2025 |
| Astec, consolidated | 2.4% (1 loss year, 2018) | CY2016 to CY2025 | Astec 10-K FY2025, `0000792987-26-000011`, and XBRL facts |
| Gencor | 6.6% | FY2009 to FY2025 | as above |
| Astec, consolidated | 3.3% | CY2009 to CY2025 | as above |
| Ammann (Swiss, private), Fayat (French, private: ADM, Marini, Dynapac, Bomag), Wirtgen (inside Deere) | **not obtained**: no SEC segment filing gives their asphalt-plant margins | | flagged |

Gencor's return on its own operating capital, pre-tax, aggregated: about 15% to 16% (FY2010 to FY2025 operating income
$90.1M over the sum of year-end operating capital, 14.7%; FY2011 to FY2025 over average capital, 16.5%; operating capital
rebuilt from the filed balance sheets, `value.py` and `calc.py` in the research folder). On the capital added from FY2016 to FY2025 (+$56.5M including the paver line),
operating income rose $6.2M: about 11% pre-tax on the increment.

**Reading.** The span read whole shows a field in which the largest firm earns 2% to 5% and Gencor, a small one, has
earned more in booms and less in busts; "you can have only two competitors and they’re still terrible businesses"
**[M2013-052]**. Nothing found protects "excellent returns on invested capital" **[L2007-004]**: the filer says rivals'
prices set its own **[M2012-109]**; price is a principal factor in the customer's choice; in the last downturn the leader
earned and Gencor did not, so it does not hold the one title that saves a commodity-type maker **[L2000-017]**,
**[M1997-010]**; and its through-cycle return is ordinary. "most moats aren’t worth a damn" **[M1995-038]**; on the evidence
this business has none to describe. The castle question is answerable, so this is not TOO HARD: it is shown open. A low
price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle is shown open on the filings: competitors set price **[M2012-109]**, Gencor is not the
  low-cost producer in a commodity-type field **[L2000-017]**, **[M1997-010]** (trough FY2009 to FY2015: -2.0% aggregate,
  five loss years, against Astec's 9% to 13% asphalt-segment margins and 5.2% consolidated), and nothing protects excellent
  returns **[L2007-004]**. Box **[M2006-013]**: out. **The run closes here.**

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (closed at Q2). Facts found in the reading are recorded after the box, not weighed.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0 as the template requires; the accounting facts are recorded after
the box.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Facts recorded after the box.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts recorded after the box.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The owner's requested figures are computed after the box under COMPUTATION — NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** (For the record: no debt; a $150K letter of credit cash-collateralised; no pension; ordinary product
liability; the "little or no debt" criterion **[R1997-001]** would be met.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (No named business: road-building equipment.)

---
## THE BOX
**OUT, at Q2.** The castle is shown open: price set by rivals **[M2012-109]**, not the low-cost producer in a
commodity-type field **[L2000-017]**, **[M1997-010]**, ordinary through-cycle returns where a moat must protect excellent
ones **[L2007-004]**. Not TOO HARD: the question was knowable and the filings answered it. Q7 was not reached; the
owner's figures below are computation only: value range $9.76 to $26.44 a share, fair price about $11.80, cheap price
about $6.50, against $17.64.

---
## AFTER THE STOP: FACTS FOUND, NOT WEIGHED (recorded as contrary evidence, **[M1997-127]**; none is a verdict)

**For Q3 (capital).** Over FY2016 to FY2025 after-tax operating earnings (CONVENTION tax rates below) summed to $69.4M
while owner cash after every real cost (working capital and the paver purchase included) summed to $14.5M: the profit
went into inventory, contract assets and the paver line. The test the rows set is "depends on what we earn on that
incremental $130 million over time" **[M2001-019]** and "decent returns on the incremental sums they invest"
**[L2009-012]**: about 11% pre-tax on the increment here. A business that "reports the 12 percent on capital but there’s
never any cash" **[M2003-122]**.

**For Q4 (the numbers).** Tells found, by the template's list:
1. Inventories out of line with sales and a reserve climbing (Step 0) **[M1995-064]**.
2. Controls: the auditor's report on internal control is **adverse** for FY2024 and FY2025 (ITGC: user access, change
   management; journal-entry review, account reconciliations, segregation of duties; risk assessment and monitoring)
   (10-K FY2025, auditor's ICFR report; 8-K `0001193125-26-026824`), still not remediated at 2026-06-30 (10-Q Item 4).
3. Timeliness: FY2024 10-K filed six months late; two FY2025 10-Qs filed in July 2025; the 2026-03-31 10-Q late again,
   the NT 10-Q saying the company could not "determine if there will be a material change in its operating income or net
   income" (`0001193125-26-219906`); NYSE American delinquency notices twice.
4. Auditors: three changes in fifteen months (MSL to Forvis Mazars by merger, 2024-11; Forvis Mazars **dismissed** on
   2025-02-13 before finishing the audit; BPB to Carr, Riggs & Ingram by asset sale, 2026-01). The letters report no
   disagreements; Forvis Mazars' letter agrees with the company's statements.
5. The CFO (the chairman's brother-in-law, proxy footnote 2) retired effective 2026-06-10; the interim CFO is a consultant
   at $32,500 a month (8-Ks `0001193125-26-232121`, `0001193125-26-257347`).
6. In the company's favour: the financial-statement opinions are unqualified both years; no restatement; no adjusted
   earnings or EBITDA featured; no guidance; plain statements; a single segment; no debt; no stock pay.
   Under the two-tell CONVENTION these are control and timeliness failures, not the make-the-numbers habit; whether they
   meet the row's "when the accounting confuses you" **[M1995-063]** was not answered because the run closed at Q2. "There is seldom just one
   cockroach in the kitchen." **[L2002-039]** is the row a Q4 answer would have to meet; the 1999 restatement at ACP is
   the earlier cockroach.

**For Q5 (who runs it).**
1. **The 2003 going-private offer.** On 2003-11-13 the company, chaired by E.J. Elliott, offered to buy all public
   common for $2.00 cash plus $1.00 of 10% junior subordinated notes per share, a "going private transaction subject to
   Rule 13e-3", with the Elliott group as "Continuing Stockholders" who would not tender (Schedule TO-I and offering
   circular, `0000950144-03-012760`). The board noted book value of $1.48 a share and that it "did not take into account,
   the going concern value"; the fairness opinion valued the asphalt business and the Carbontronics synfuel stake
   separately. In fiscal 2003 the synfuel interests had paid the company $13,428K in cash (10-K FY2004 MD&A,
   `0001193125-04-217456`), about $1.55 per then-outstanding share in one year. Outside holders called the price "grossly
   inadequate" and bought to block it (13D, `0001047469-03-038886`); the offer was terminated on 2003-12-03
   (`0000950144-03-013422`). Equity then rose from $15.3M (FY2004) to $99.0M (FY2008). In current shares (3-for-2 split of
   2016) the offer was $2.00; book value per current share was about $7 five years later (FY2008 equity $99.0M) and is
$15.33 today. To the
   controller's credit: the offer carried a majority-of-the-minority condition and appraisal rights, and synfuel payments
   were then under IRS examination. The row it would be read against: "if shareholders or somebody else has to suffer, the
   choice is likely to be that somebody else will be chosen" **[M1998-121]**; and integrity is applied on doubt: "If
   you’ve got doubts, forget it." **[M2013-088]**.
2. **2007 to 2008.** Lloyd I. Miller III won a board seat from the common holders in a proxy contest (2008-03-06) and
   resigned two months later, saying he "was unable to influence the policies of the Company further as a member of the
   Board of Directors" (13D/A `0000950123-08-005435`).
3. **Control.** Class B elects 75% of the board; on 2026-05-01 the family partnership's control passed by gift to Marc
   Elliott, who may be deemed to hold 95.5% of Class B and 14.5% of common (8-K Item 5.01, `0001193125-26-212435`). He is
   President and, since 2026-01-01, Chairman, the case the rows flag: "how hard it is to replace a mediocre CEO if that
   person is also Chairman" **[L2014-026]**. The Nominating Committee is Marc Elliott alone.
4. **The proxy** ("see how they treat themselves versus how they treat the shareholders" **[M1994-009]**): FY2025
   salaries, fixed, no bonus, no equity: Marc Elliott $950,000; E.J. Elliott $600,000; Dennis Hunt $500,000; Eric Mellen
   (brother-in-law) $350,000; $2.43M in all, 17% of FY2025 operating income, tied to nothing. The compensation committee
   "did not meet during fiscal 2025". The three independent directors own no shares (fees $26,000 to $27,000), against
   the row on directors "purchasing shares with their savings" **[L2019-008]**. No related-party transactions in FY2025.
   The proxy's own total-shareholder-return line: $100 became $70.85 over FY2023 to FY2025.

**For Q6 (the money and the owners).**
1. No dividend and no buyback in the record read: "we have never purchased shares from our stockholders" (2003 offering
   circular) and none since; "does not expect to pay cash dividends for the foreseeable future" (10-K FY2025). Cash and
   securities of $164.2M (2026-06-30) are 63% of the market value and earn bond yields: interest and dividends net of
   fees $4.37M plus gains $1.80M in FY2025 on average holdings of about $126M. In the first nine months of FY2026 a
   further $25M of operating cash was moved into the portfolio (10-Q MD&A).
2. The retention test **[M1994-061]**: retained earnings rose $96.9M from FY2015 to FY2025 while market value rose from
   about $86.3M (Sept 2015, $6.03 split-adjusted, aggregator, x 14.31M shares) to about $214.4M (Sept 2025, $14.63 x
   14.66M): about $1.32 of market value per dollar kept over ten years; over FY2020 to FY2025, about $1.06. Passed in the
   market, thinly, and the surplus "should be paying out dividends" by the row that governs a company that "expects to
   regularly earn more than it can profitably employ in its business" **[M2004-089]**; the rewards are channelled "to the
   shareholders rather than to itself" only if the cash ever leaves **[L1993-020]**.
3. Investment Company Act: the filer says its non-government investment securities are below 40% of total assets and that
   it is not an investment company (10-K FY2025, Item 1A).

---
## COMPUTATION — NOT A CLEARANCE
*The file closed OUT at Q2. Nothing below is entry language or a clearance (operator rule 3). Reported at the owner's
request; it does not change the box.*

**Owner cash of the operating business** (Q4 and Q7 recast: "regular pretax earnings" **[M2012-034]**, after "all forms of
compensation" **[L2021-003]**, depreciation counted as a true cost **[L2015-004]**; $ thousands; working capital from the
filed cash-flow lines; CONVENTION of this run: tax at 36% to FY2017, 24.5% in FY2018, 22.2% from FY2019, the last being
the federal 21.0% plus state 1.2% in the FY2025 rate reconciliation; the portfolio's income excluded):

| FY | Operating income | After tax | + D&A - capex | Working capital (cash-flow lines) | Paver purchase | Owner cash |
|---|---|---|---|---|---|---|
| 2016 | 7,816 | 5,002 | +1,091 | -1,719 | | 4,374 |
| 2017 | 10,236 | 6,551 | -496 | -2,968 | | 3,087 |
| 2018 | 13,715 | 10,355 | -2,170 | -10,445 | | -2,260 |
| 2019 | 9,470 | 7,368 | -504 | -7,351 | | -487 |
| 2020 | 5,536 | 4,307 | +48 | +6,281 | | 10,636 |
| 2021 | 701 | 545 | -68 | +1,303 | -13,777 | -11,997 |
| 2022 | 4,167 | 3,242 | -1,693 | -14,169 | | -12,620 |
| 2023 | 13,425 | 10,445 | +88 | -12,525 | | -1,992 |
| 2024 | 13,687 | 10,648 | +1,762 | -3,325 | | 9,085 |
| 2025 | 14,018 | 10,906 | +393 | +5,341 | | 16,640 |

- Five-year average FY2021 to FY2025, every capital outlay deducted: **-$0.18M a year**; without the paver purchase
  $2.58M; ten-year average $1.45M. The depreciation variant shown beside it (after-tax operating earnings plus D&A less
  capex, no working-capital charge): $7.25M (five-year), growing 7.1% a year from FY2016 to FY2025 on that measure.
  Maintenance judgment: capex ($21.9M) and D&A ($20.4M) were close over the ten years, so maintenance is taken as D&A;
  the open question is working capital, not plant. Whether the inventory build is permanent cannot be read from the
  filings; FY2024, FY2025 and the first nine months of FY2026 released $7.8M, $10.3M and $6.5M of it (cash-flow
inventory lines).

**Value range, read by parts** (Q7 CONVENTION: five-year average owner cash, the shown growth, ten years then no growth,
at the sovereign 5.63% **[M1996-025]**; per share on 14,657,702):
- **Securities and cash** at 2026-06-30: $164,169K, less tax on the unrealized gain ($1,842K x 22.2% = $409K) and the
  unrecognized-tax-benefit liability ($2,582K) = $161,178K, **$11.00 a share**; less a working reserve of $15,000K
  (CONVENTION of this run: about the largest single-year working-capital draw in the ten years, FY2022's $14.2M, which
  the business funded from this pile) = $146,178K, **$9.97 a share**.
- **Operating business**, the convention's cash input (all capital): -$0.18M a year: no-growth value -$3.1M,
  **-$0.21 a share**; the shown-growth end cannot be computed on a negative base and is set equal to it (CONVENTION of
  this run). Depreciation variant beside it: no growth $128.8M (**$8.79**); shown growth 7.1% for ten years then flat,
  $226.3M (**$15.44**).
- **Whole company:** convention input, **$9.76 to $10.79**; depreciation variant, **$18.76 to $26.44**; the span of both,
  **$9.76 to $26.44 (2.7 to 1)**. Price $17.64 sits inside it. Had Q7 been reached it could not have closed IN: the
  operating part's own range runs from below zero to $226M, which "must be so wide that no useful conclusion can be
  reached" **[L2000-025]**, and the whole sits around the price, which "should scream at you" **[M2009-005]** and does not.

**Fair price** (the owner's request: the price at or below which the central case clears the floor of about ten percent
pre-tax, **[L2002-020]**, **[M2003-149]**, Q7 CONVENTION). Central case, CONVENTION of this run: (1) operating pre-tax
owner cash $6.94M, being the ten-year average operating income $9.28M, less capex over D&A $0.16M, less the working
capital that 3% revenue growth would need at FY2025's operating capital of 63 cents per revenue dollar ($2.19M), growing
3%; (2) the portfolio earns 4.5% pre-tax (FY2025's total return was 4.9% and the nine-month FY2026 rate about 3.5%) and,
as for twenty-plus years, is not paid out. Value at 10% pre-tax: $6.94M / (10% - 3%) = $99.1M for the business plus
$7.39M / 10% = $73.9M for the portfolio's income = $173.0M, **fair price about $11.80 a share**. The expected pre-tax
return at $17.64 on this case is about **6.6%** (about 5.2% after the 22.2% corporate rate); the after-tax equivalent of
the 10% floor at that rate is 7.8%. Sensitivity: if the portfolio could be had at face, as in a sale or a distribution,
the same arithmetic gives $17.76; the $5.96 gap is the price of the controller's retention policy.

**Cheap price** (rule, CONVENTION of this run: two-thirds of the bottom of the range, so that the operating business
comes free and the cash and securities net of tax and the working reserve cost two-thirds of their value; then no pencil
is needed **[M1996-084]**): two-thirds of $9.76 = **about $6.50 a share**. Even there the discount could persist, since
the minority has no way to make the cash leave.

**Against the price ($17.64):** above the fair price ($11.80), far above the cheap price ($6.50), inside the range.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied, then the first fetch was made). Written top to
      bottom. **Not committed after each question, nor at all: the brief for this run forbids commits**; the file and
      the research folder are left uncommitted for the operator.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; see the research folder note); every filing
      fact has its accession; numbers not from a filing or row are labelled CONVENTION.
- [x] The order was kept; Q2's OUT closed the run; Q3 to Q12 are NOT REACHED and the facts after the box are labelled
      as not weighed; the value figures are headed COMPUTATION — NOT A CLEARANCE and carry no entry language.
- [x] Owner cash rebuilt from operating income, D&A, capex and working-capital lines; never from net income; the
      tool's OCF-based lines were rejected because OCF here carries the securities portfolio. Sovereign from the US
      Treasury. Aggregator quotes flagged (current price; the 2015 and 2025 year-end prices used in the retention test).
- [x] Contrary evidence written down as found **[M1997-127]** (foundations paragraph; competitor row; the after-stop
      section).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of them (OCF, OE) were rejected for cause.
- [x] `python tools/check_framework.py` run after writing (result recorded in the reply to the operator).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q2 when no castle is claimed and the competitor comparison splits by era.** The framework sends "a castle shown open"
   to OUT and "a castle whose future cannot be judged" to TOO HARD, but gives no rule for a small maker in a poor field
   that beats its main rival over the whole span (6.6% against 3.3%) and loses to it in the downturn. I read the trough as
   the test of the low-cost title, because the rows place that title's value where the low-cost producer "can put you out
   of business" **[M1997-010]**, and read the absence of anything protecting excellent returns as "shown open". A second
   analyst could call the same facts TOO HARD (NATURE) on the funding cycle; I did not, because that cycle is macro.
2. **Q7's cash input when working capital is the main capital use.** The convention says the cash input "deducts all
   capital spending" but does not say whether working capital counts. Here it decides everything: the five-year average is
   -$0.18M with it and $7.25M without. I counted it (the rows name this industry's profit "sitting in the yard"
   **[M2008-036]**) and showed the other beside it. The shown-growth end is undefined on a negative base; I set it equal
   to the no-growth end and said so.
3. **A holding company read by parts, when the controller never distributes.** The by-parts convention values the
   securities, but nothing says whether cash that a controller has kept for twenty years is worth its face or the income
   it earns. The fair price moves from $17.76 to $11.80 on that choice alone. I used the income in the central case and
   showed the face value beside it; a rule is needed.
4. **Integrity facts found before the stop.** The 2003 going-private offer and the control and pay facts bear on Q5, a
   STOP, but the run closed at Q2 and the hard sequence leaves them unanswered. They are recorded as contrary evidence,
   not weighed. If the operator wants a STOP that is plainly met in the reading to be named even when an earlier STOP
   closes the file, the framework does not say so.
5. **The template's position note** tells the analyst to check `PORTFOLIO.md`; this run's blind brief forbids opening
   it. The note was left unanswered and the conflict is recorded.
6. **The working reserve against a cash pile** (how much of a company's cash belongs to its operations) has no rule; this
   run's $15M is a CONVENTION from the largest one-year working-capital draw.
