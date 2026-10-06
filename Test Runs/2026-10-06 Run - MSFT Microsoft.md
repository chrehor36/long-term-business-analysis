# Company Run — Microsoft Corporation (NASDAQ: MSFT) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. The template was copied to this dated name before any fetch (commit
`f282bc7`). Working folder: `Test Runs/_research 2026-10-06 MSFT/` (`run_py_output.txt`, `cover_shares_output.txt`,
`sources_output.txt`, `compute.py` and its output `compute_out.txt`; the filings as text are there too, gitignored).

*Dash note: the dashes in the headings are the template's own; the label "COMPUTATION — NOT A CLEARANCE" is written as
operator rule 3 writes it.*

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not
opened, so whether the operator holds MSFT is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) When the template was copied, a directory listing of `Test Runs/` filtered on "msft"
showed two earlier file names for this ticker: `2026-07-15 Run - SPOT GOOGL MSFT SHW AMZN (5-pack).md` and
`2026-09-06 Run - MSFT Microsoft.md`. Names only; neither was opened, and their verdicts are unknown to this analyst.
The existence of a run dated 2026-09-06 suggests the name has been looked at before, nothing more. (2) The listing of
`Test Runs/` also showed the names of the 2026-10-05 v5 runs; three (YELP, EXTR, SONY) were opened for FORM only, as the
dispatch allows; none concerns Microsoft. (3) A search of `principle_ledger_v5.csv` for "Microsoft" returned rows in
which the speakers talk about Microsoft by name (**[M1996-059]**, **[M1998-050]**, **[M1999-072]**, **[M2002-048]**,
**[M2003-055]**, **[M2021-023]**). They are the corpus, not an earlier run, and are used below as evidence; they are
declared here because they carry the speakers' own view of this very company, which is the kind of row a reader should
know the analyst saw. (4) Training memory: the analyst came in with a prior of Microsoft as a high-return software
franchise; the filings below are what is relied on, and where they cut against that prior it is written down.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $525.18 (2026-10-05; Yahoo Finance quote via `tools/run.py`; **aggregator, live quote only, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: **7,425,545,491** common shares, one class, as of 2026-07-23
  (Form 10-K for the year ended 2026-06-30, filed 2026-07-29, accession `0001193125-26-323660`;
  `python Screens/cover_shares.py MSFT` returned the same; "single class / undimensioned"). The balance-sheet count at
  2026-06-30 is 7,427.0M.
- **Market cap:** $3,899,748M (about $3.90 trillion), $525.18 × 7,425.545M.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), all from EDGAR, CIK 789019:
  - **10-K FY2026** (year ended 2026-06-30), filed 2026-07-29, `0001193125-26-323660`: Item 1 (business, segments,
    competition), Item 1A (strategic and competitive risks, the cloud and AI investment risk, the evolution of the
    business), Item 7 (highlights, summary results, liquidity, cash flows, contractual obligations, share
    repurchases), the income and cash-flow statements, Note 13 (leases), the OpenAI paragraph of Note 1 and the
    other-income note, the remaining-performance-obligation note.
  - **10-K FY2025**, filed 2025-07-30, `0000950170-25-100235`: Note 13 only (leases not yet commenced at 2025-06-30;
    finance-lease assets obtained), for the trend.
  - **10-Q Q3 FY2026** (quarter ended 2026-03-31), filed 2026-04-29, `0001193125-26-191507`: MD&A highlights and the
    lease note. It is the latest 10-Q; the 10-K above is the latest periodic filing.
  - **DEF 14A**, filed 2025-10-21, `0001193125-25-245150` (the 2025 proxy; no 2026 proxy is on EDGAR at this date):
    read only for the chief executive's pay design paragraph; Q5 and Q6 are NOT REACHED.
  - **8-K** 2026-07-29, `0001193125-26-323632`, Exhibit 99.1 (FY2026 Q4 results) read in full before any view on
    non-GAAP habits: the non-GAAP measures exclude only the net gains and losses from the OpenAI investment, both ways.
  - **8-K** 2026-09-02, `0001193125-26-380280` (Item 7.01): from fiscal 2027 the company reports two segments, "Agents
    and Infra" and "Devices and Consumer". The Exhibit 99.1 deck is filed as page images and was not read.
  - **8-Ks** 2026-05-14 `0001193125-26-224155` (Carmine Di Sibio joins the board) and 2026-06-05
    `0001193125-26-258667` (Reid Hoffman will not stand for re-election).
- **One figure cross-checked against the filed statement:** net cash from operations FY2026 **$182,935M** on the filed
  consolidated cash flows statement (10-K FY2026) equals the tagged figure `tools/run.py` printed; additions to property
  and equipment $115,948M and stock-based compensation $12,405M also agree.
- **`tools/run.py MSFT --framework v5`, arithmetic lines only** (Part VII; nothing it prints as a rule was used; full
  output in `run_py_output.txt`), extended to eleven years from the filed cash-flow lines in `compute.py` (USD millions;
  owner cash = operating cash less all stock pay less all cash capital spending):

| FY | revenue | OCF | stock pay | capex | capex / revenue | owner cash | owner cash / revenue |
|---|---|---|---|---|---|---|---|
| 2016 | 91,154 | 33,325 | 2,668 | 8,343 | 9.2% | 22,314 | 24.5% |
| 2017 | 96,571 | 39,507 | 3,266 | 8,129 | 8.4% | 28,112 | 29.1% |
| 2018 | 110,360 | 43,884 | 3,940 | 11,632 | 10.5% | 28,312 | 25.7% |
| 2019 | 125,843 | 52,185 | 4,652 | 13,925 | 11.1% | 33,608 | 26.7% |
| 2020 | 143,015 | 60,675 | 5,289 | 15,441 | 10.8% | 39,945 | 27.9% |
| 2021 | 168,088 | 76,740 | 6,118 | 20,622 | 12.3% | 50,000 | 29.7% |
| 2022 | 198,270 | 89,035 | 7,502 | 23,886 | 12.0% | 57,647 | 29.1% |
| 2023 | 211,915 | 87,582 | 9,611 | 28,107 | 13.3% | 49,864 | 23.5% |
| 2024 | 245,122 | 118,548 | 10,734 | 44,477 | 18.1% | 63,337 | 25.8% |
| 2025 | 281,724 | 136,162 | 11,974 | 64,551 | 22.9% | 59,637 | 21.2% |
| 2026 | 331,839 | 182,935 | 12,405 | 115,948 | 34.9% | 54,582 | 16.4% |

  Five-year mean (FY2022 to FY2026), capex basis: **$57,013M**, a yield of 1.46% on the market cap against the 5.66%
  sovereign. The capex column does not hold all the capital put in. **Finance-lease assets obtained** (non-cash,
  datacenters and equipment; Note 13): $3,128M (FY2023), $11,633M (FY2024), $20,511M (FY2025), $24,608M (FY2026). With
  them, capital put in was $140,556M in FY2026, 42.4% of revenue, and owner cash after it **$29,974M** (0.77% of the
  market cap). FY2026 investing "Other, net" of $19,861M is described in MD&A as "cash used in other investing primarily
  to facilitate the purchase of components"; taken as capital too, FY2026 owner cash is about $10,113M. FY2026 operating
  cash includes a deferred-tax add-back of $14,189M (FY2025: minus $7,056M), and MD&A credits "a decrease in cash used
  to pay income taxes", so the FY2026 operating figure is lifted by tax timing.
- **Balance sheets, ten year-ends, read before the income account** **[M2025-032]** (`run_py_output.txt`, first-filed
  XBRL; the FY2026 sheet read against the filed 10-K): equity rose from $72,394M (2017) to $442,387M (2026); goodwill
  from $35,122M to $119,651M, the step in 2024 being Activision Blizzard (acquisitions $69,132M that year); long-term
  debt fell from $76,073M to $31,067M noncurrent ($40,294M with the current part); cash and equivalents $20,935M, with
  cash, equivalents and short-term investments $76.8B at 2026-06-30 against $94.6B a year earlier. What the balance
  sheet does not show is the large new item: **leases not yet commenced** of $92.7B at 2025-06-30, $196.6B at
  2026-03-31 and **$329.1B at 2026-06-30**, commencing fiscal 2027 to 2033; with **purchase commitments** of $194.1B
  ("primarily relate to datacenters") and construction commitments of $34.6B, total contractual obligations stand at
  **$743.8B** (MD&A, 10-K FY2026). Purchases of property and equipment unpaid in accounts payable rose from $6.9B to
  $26.7B in the year.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which here means owning the cash a $3.9 trillion business will throw off over a decade in which, by
its own filing, it is spending at a rate it has never spent before. The market serves and does not instruct
**[M2006-077]**: the quotation of $525.18 says nothing about whether the datacenter programme earns its keep. No macro
enters **[M2000-094]**: nothing here turns on rates or a cycle; it turns on one company's capital and one technology's
economics. Who is paid to tell you **[M2020-037]**: the whole investment industry has a view on AI and is paid for
having it; the analyst's view is built from the 10-K only. The analyst's habits: the worst anchor "is always your
previous conclusion" **[M2016-054]**, and the analyst's prior (a capital-light software franchise) is exactly the
conclusion the filings put under strain; look for "what’s wrong" and "what you’re missing" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) *against the prior of a capital-light business*:
capital spending went from 8.4% of revenue (FY2017) to 34.9% (FY2026) and to 42.4% with finance leases; revenue more
than tripled from FY2017 to FY2026 while owner cash after all capital put in (about $30.0B) is close to the FY2017
figure ($28.1B, capex basis; finance leases for FY2017 were not read); $329.1B of datacenter leases have been signed and not yet begun. The speakers themselves listed
Microsoft in 2021 among companies that "don’t require a lot of capital" **[M2021-023]**; the filings since then show
that this has changed, as the next row warns such businesses "don’t always stay that way" **[M2021-046]**. (b)
*against a TOO HARD close*: the company's commercial remaining performance obligation is $678B, up 84%, with about 30%
to be recognized in twelve months; Microsoft 365 Commercial cloud revenue rose 17% and has been sold by subscription
for a decade; FY2026 revenue rose 18% and operating income 21%; the speakers once said that if they had to bet on
anybody in software "I’d certainly bet on Microsoft, bet heavily if I had to bet" **[M1999-072]**. These are written
down here and weighed at Q1.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase would be made without borrowed money and at a size that cannot
threaten the buyer, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in owning a share of Microsoft
requires leverage, collateral or a short maturity on the buyer's side. Not breached, on the stated conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- The test as the draft states it, applied to the filings; the key variables and whether they are foreseeable.
- Routing: a business whose ten-year economics cannot be foreseen because its industry changes fast closes here, TOO
  HARD; a bank is inside the circle when both sides of its balance sheet can be read; a holding company is understood
  by its parts.
- **VERDICT: IN / OUT / TOO HARD**, with ids and the filing fact.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- The castle tests, each with its filing fact: the attacker with money; pricing power and the agony before a rise; unit
  volume and share of mind; the low-cost position; the brand in the customer's mind; would the customer still choose it
  over the low bid; ask the competitors; widening or narrowing; what could destroy it.
- **The competitor row**, same metric from the competitors' own filings (name, metric, accession).
- A castle shown open on the evidence closes OUT; a castle whose future cannot be judged closes TOO HARD.
- **VERDICT: IN / OUT / TOO HARD**, with ids.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- Return on the capital actually needed; reinvestment to stand still and to grow; the growth arithmetic and its caps.
- **WEIGHS FOR / AGAINST / UNDECIDED**, one sentence, with ids. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight to ten years of them, before the income account** **[M2025-032]** (`tools/run.py`
  prints the ten-year table; read the filed statements behind it). Say what moved and why: equity against goodwill and
  intangibles, cash, receivables and inventory against sales, debt, retained earnings; "what the figures are saying and
  what they don’t say and what they can’t say" **[M2025-032]**. *(line added 2026-10-05: the rule was in Q4 of the
  framework from adoption, and no run had been asked to do it.)*
- The real costs (depreciation, stock pay, restructurings, the recurring "one-time"); EBITDA in the filer's own
  mouth; what the accounts say of management's character. The make-the-numbers habit alone weighs against; with a
  second tell it is suspicion.
- **VERDICT on confusion: IN / OUT; WEIGHS FOR / AGAINST** otherwise, with ids. The recast earnings feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- The two yardsticks; the tells of dishonesty (the proxy, the letters, how they talk about mistakes); love of the
  business; what ability shows in. Integrity applied on doubt alone.
- **VERDICT on integrity: IN / OUT; ability WEIGHS FOR / AGAINST**, with ids.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- Part A: the retention test (a dollar kept worth more than a dollar, over time); buybacks (only below value; a buyback
  with no stated price weighs against unless the prices paid sit at or below the bottom of the Q7 range); issuance and
  deals (value given against value got; an all-stock deal at an undervalued price is the one STOP here).
- Part B: pay tied to what the person controls; the board; the owners as partners.
- **WEIGHS FOR / AGAINST / UNDECIDED**, one sentence per part, with ids.

## Q7 — WHAT IS IT WORTH? STOP.
- How much cash, how sure, how soon, at the long government rate, as a range (the CONVENTION construction: five-year
  average of owner cash after every real cost, carried at the growth shown and capped by Q3, ten years then no real
  growth, at the sovereign; the ends are the no-growth and shown-growth cases).
- The floor (CONVENTION): about ten percent pre-tax expected return, as the speakers stated and qualified it; below it
  the name is quit on, not ranked.
- **Value range:** $ ___ to $ ___ a share against $ ___. **Closes:** TOO HARD if the range is wider than about three
  to one; OUT if the price sits inside or just below a narrower range (not a screamer); IN only if the price is so far
  below that no pencil is needed.
- **VERDICT: IN / OUT / TOO HARD**, with ids.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
- The bond as the first filter, then the ranking against the best thing already held (for a private holder, more of
  what he owns; for a company, its own stock below value).
- **VERDICT: IN / OUT**, with ids.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- Debt in the business, demands for sudden large sums, counterparties, aggregation; "little or no debt" is the one STOP
  for a whole business bought.
- **WEIGHS FOR / AGAINST**, with ids.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- Inaction as the default; sizing when sure; the omission as the costliest error. No position is taken here; say what
  the draft would have the buyer do.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- The newspaper test; the businesses named. **STOP for named businesses; otherwise WEIGHS FOR / AGAINST.**

---
## THE BOX
One line: **IN / OUT / TOO HARD (WORK) / TOO HARD (NATURE)**, the question that decided it, and for a name that reached
Q7 the range beside the price. A TOO HARD names its cause (the framework's section I, the two causes): WORK when the
deciding question is knowable and the work is not done, which opens a research file (Part VII); NATURE when the
industry's insiders would not write the forecast down. Q11 (has the business changed, or only its price) belongs to the holding review, not to a purchase run.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
- [ ] Every v5 id resolves (grep it in `principle_ledger_v5.csv`); every filing fact has its accession; no number
      without a row or a filing.
- [ ] The order was kept; the first STOP that failed closed the run; nothing after it is a clearance.
- [ ] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quotes flagged.
- [ ] Contrary evidence was written down as it was found **[M1997-127]**.
- [ ] No row dated after the anchor is cited in a point-in-time run (Part VII).
- [ ] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [ ] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
One paragraph: the instruction found ambiguous, missing or unworkable in this run, and what was done. Every run so far
has had one; a run that reports none is suspect.
