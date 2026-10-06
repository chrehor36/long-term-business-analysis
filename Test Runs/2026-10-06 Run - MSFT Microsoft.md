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
**The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will
be in 10 years" **[M2000-037]**; it is not knowing the product: "We understand what it does for people. We just don’t
know the economics of it 10 years from now." **[M2000-104]**. The first step is "trying to identify the key variables
in that particular business, and evaluating how predictable they were first [...] If something is not very
predictable, forget it." **[M1998-044]**

**What the business is, from the 10-K FY2026 (`0001193125-26-323660`).** Three segments in FY2026: Productivity and
Business Processes, revenue $139,996M and operating income $83,879M (Microsoft 365 Commercial and Consumer, LinkedIn,
Dynamics); Intelligent Cloud, revenue $137,791M and operating income $56,972M (Azure and other cloud services, server
products), with Azure "and other cloud services" up 41% and above $100 billion of revenue for the first time (8-K
Exhibit 99.1, `0001193125-26-323632`); More Personal Computing, revenue $54,052M (Windows OEM and devices, XBOX, search
advertising). From fiscal 2027 the company reorganizes its reporting into two segments, "(1) Agents and Infra and (2)
Devices and Consumer" (8-K Item 7.01, `0001193125-26-380280`). Item 1 describes itself first as "a technology company
committed to making digital technology and artificial intelligence (“AI”) available broadly", and states: **"Our future
growth depends on our ability to transcend current product category definitions, business models, and sales
motions."**

**The key variables, and whether each is foreseeable.**
1. **What the AI and datacenter capital will earn over ten years.** This is now the largest single variable in the
   business. Capital spending rose from $28,107M (FY2023) to $115,948M (FY2026), with $24,608M more taken on as finance
   leases; leases signed and not yet commenced rose from $92.7B (2025-06-30) to $196.6B (2026-03-31) to $329.1B
   (2026-06-30); datacenter purchase commitments are $194.1B (Step 0). The company says of this programme, in Item 1A:
   the investments "are being made at significant scale and on an accelerated timeline, require substantial and
   increasing capital expenditures and continued access to capital, and are **in advance of fully developed revenue
   streams**. The associated revenue may not be realized in the expected timeframes or at expected levels"; **"Demand
   for cloud-based and AI products and services is evolving and difficult to forecast.** Overestimation of demand or
   misalignment of capacity investments may result in underutilization of infrastructure and may lead to impairment of
   assets"; "**The cost structure for AI products and services is subject to significant uncertainty**, including with
   respect to model training and inference costs, the availability and pricing of components, and energy costs [...]
   or if pricing for AI products and services declines as a result of competition, **commoditization**, or other market
   forces, our margins [...] could be adversely affected"; and "**Investments in new technology are speculative.**"
   Not foreseeable, and the filer says so.
2. **Whether the seat franchise survives the move to agents.** Microsoft 365 Commercial cloud revenue grew 17% and
   seats 6% (MD&A); this is the part of the business with the longest record of subscription revenue. But the company
   itself names the variable that decides it, "the accelerating importance of agentic computing" (Item 1A), renames its
   main segment after "Agents", lists among Office's competitors "AI-first application companies" (Item 1), and says
   that "Barriers to entry in many of our businesses are low and many of the areas in which we compete evolve rapidly
   with changing and disruptive technologies" (Item 1A). Whether work done by agents is sold per seat, per use or not by
   Microsoft at all is a forecast about the technology, not about the customer's habits.
3. **The OpenAI relationship.** An equity-method investee of about 25% on an as-converted basis, a related party, a
   source of $24.1B of FY2026 revenue "from commercial arrangements with OpenAI, inclusive of revenue-sharing payments",
   and a competitor: "Our AI offerings compete with AI products from hyperscalers, open-source offerings, and frontier
   model providers, some of which are also current or potential partners" (Note 1 and Item 1A). The economics of that
   arrangement ten years out are not in the filings and could not be.

**The tests of Q1, each against the filing.**
- *Where will it be in ten years* **[M1999-132]**: on the evidence above, at a level of capital intensity the company has
  never run at (capital put in 42.4% of FY2026 revenue, finance leases included, against cash capex of 8.4% to 13.3% of revenue in FY2016 to FY2023), earning a return on
  that capital that no filing yet shows.
- *Do the past statements tell me the future ones* **[M2008-033]**: no. The FY2016 to FY2023 statements describe a
  software business whose owner cash ran at 23% to 30% of revenue; the FY2026 statement, after finance leases, shows
  9.0%, and the commitments signed since make the FY2027 to FY2033 statements a different business again. The record
  does not describe the business now being built.
- *Important and knowable* **[M2006-076]**: the return on the datacenter programme is the most important figure in the
  valuation and is, in the filer's own words, "difficult to forecast".
- *Would the insiders write it down* **[M2000-105]**: the insiders here are the issuer, and in a document signed under
  liability they decline to: "The associated revenue may not be realized in the expected timeframes or at expected
  levels." That is test 5 answered by the company itself.
- *Can I name the winner, not just the industry* **[M2012-067]**: the 10-K names its AI competitors as "hyperscalers,
  open-source offerings, and frontier model providers", some of them partners; the speakers said of the cloud in 2017
  that "there are a lot of people that would aim that silver bullet at Jeff" **[M2017-022]**, i.e. the cloud has more
  than one strong contender. Seeing that AI will be large is not seeing who earns what on it **[L2009-005]**.
- *Customers or technology* **[M2017-019]**: the deciding variables (inference cost curves, component pricing,
  "commoditization", agents against seats) are technology variables, the IBM-type analysis, not the Apple-type one.
- *How far off could I be* **[M2011-084]**: FY2026 owner cash alone is $54,582M, $29,974M or about $10,113M depending
  on whether finance leases and component prepayments are counted (Step 0); ten years out the spread is wider than
  that, and its direction is the open question.
- *Do I doubt it is inside* **[M2002-092]**: yes. "if you have doubts about something being into your circle of
  competence, it isn’t."

**The speakers on this company, read as rows, not as authority.** "We think Microsoft is a sensational company run by
the best of managers. But we don’t have any idea what that world is going to look like in 10 or 20 years."
**[M1996-059]**; "I don’t know where Microsoft or Intel — I don’t know what that world will look like in 10 years"
**[M1998-050]**; and the leader that must "leverage its current leadership into new activities [...] Predicting whether
somebody’s going to be able to do that in advance is just — it’s too tough for us." **[M1997-022]**. The 10-K's
sentence about transcending "current product category definitions, business models, and sales motions" is that
leverage stated as the company's plan. These rows were said of an earlier Microsoft; they are cited because the test
they apply is Q1's, and the filings show the same kind of change again, not because the speakers' verdict binds.

**The contrary evidence, weighed** **[M1997-127]**. (a) The commercial remaining performance obligation is $678B, up 84%,
about 30% to be recognized within twelve months (Note on revenue): there is contracted demand. But a weighted average
duration of 2.3 years covers a fraction of a ten-year horizon and of leases running to 20 years, and an unknown share of
it is owed by OpenAI, the related party named above; contracted revenue is not the return on the capital that serves
it. (b) The Microsoft 365 Commercial franchise, taken alone, may well be foreseeable: an installed base sold by
subscription for a decade. Read by its parts, a part that cannot be understood and that matters keeps the whole outside
**[M2002-092]** (the by-parts reading is the framework's CONVENTION at Q1), and the datacenter programme is the part
that will decide the next ten years' owner cash. (c) "If I had to bet on anybody, I’d certainly bet on Microsoft, bet
heavily if I had to bet. But I don’t have to bet." **[M1999-072]**: the row is for the company's quality and against
the need to forecast it; it is the clearest statement in the ledger of a TOO HARD that is not a judgment against the
business. (d) Revenue grew 18% and operating income 21% in FY2026: the year was good; Q1 asks about the tenth year.

- **VERDICT: TOO HARD (NATURE)** **[M1998-008]**, **[L1993-023]**, **[L1999-018]**, **[M2000-105]**. The ten-year
  economics of Microsoft now turn on what a datacenter and AI programme of a size the company has never run will earn,
  and on whether agents keep or break the seat-based franchise; the company's own 10-K calls the demand "difficult to
  forecast", the cost structure "subject to significant uncertainty", and its new-technology investments "speculative".
  "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its
  long-term economics" **[L1993-023]**, and the routing sends that case here, to TOO HARD, not OUT **[M1998-008]**.
  **The cause is NATURE, not WORK**: the deciding forecast is one the industry's insiders would not write down
  **[M2000-105]**, and here the insider is the issuer, in its own risk factors; "Our problem -- which we can't solve by
  studying up -- is that we have no insights into which participants in the tech field possess a truly durable
  competitive advantage." **[L1999-018]**. A research pass would read the same filings and meet the same sentence;
  "we’re not going to learn enough in the followings five months to make up for the fact that we went in deficient in
  the first place" **[M2008-086]**. This is not a judgment of quality: "It doesn’t mean it isn’t a good buy. It doesn’t
  mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
  **[M2000-038]**; and a miss here is not counted an error, since "if somebody knows how to make money [...] in a
  software company or anything, and we miss that, that is not an error, as far as we’re concerned." **[M2001-006]**. A
  lower price does not reopen it **[M2000-038]**. The box is "in, out, and too hard" **[M2006-013]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**NOT REACHED.** No competitor row was built (it belongs to Q2). The Q2 material met while reading Q1 (the low barriers
to entry the 10-K concedes, the hyperscaler and frontier-model competitors, the RPO) is recorded under Q1 as contrary
evidence and context, not as a verdict.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** The capital figures in Step 0 are transcription, not a Q3 weighing.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The ten balance sheets were read in Step 0 because the template asks for them before the income
account; nothing there is a Q4 verdict.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.**

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** No value range, fair price or cheap price is computed: the dispatch asks for them only if Q7 is reached,
and operator rule 3 allows no entry language from a computation made before the earlier STOPs close. The only valuation
arithmetic in this file is the owner-cash yield of Step 0 (1.46% on the five-year mean, capex basis, against a 5.66%
sovereign), which is transcription and carries no verdict.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** (For a reader: the $743.8B of contractual obligations in Step 0, most of them datacenter leases and
purchase commitments, are the facts Q9 would weigh first.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** **[M2000-105]**, **[L1993-023]**, **[L1999-018]**. The forecast that would decide it
is what a datacenter and AI programme of a size Microsoft has never run (capital put in $140.6B in FY2026 with finance
leases, 42.4% of revenue; $329.1B of leases signed and not yet commenced; $194.1B of datacenter purchase commitments)
will earn over ten years, and whether agents keep or break the seat-based franchise; the issuer's own 10-K calls that
demand "difficult to forecast" and the cost structure "subject to significant uncertainty". No research file is opened:
the cause is the nature of the industry, not undone work, and a lower price does not reopen the box **[M2000-038]**.
Q7 was not reached; no value range, fair price or cheap price is given. Price for the record: $525.18 (aggregator,
2026-10-05), market cap $3.90 trillion, owner-cash yield 1.46% on the five-year mean (capex basis) against a 5.66%
Treasury. Q11 belongs to the holding review, not to a purchase run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `f282bc7`). Written question by question and committed after
      each: Step 0 to the standing rule in one commit, Q1 in its own (`c076f71`), the close in this one. **Declared:** the
      first Step 0 commit also swept in four plain-text filing dumps whose names (`k.txt`, `q.txt`, `p.txt`, `k25.txt`)
      escaped the `.gitignore` patterns; it was undone with a soft reset before anything else was written, the dumps were
      renamed to ignored names, and Step 0 was committed again (`9ef47d7`). No other history was rewritten.
- [x] Every v5 id resolves: each bold id was checked against `principle_ledger_v5.csv` by script before the commit, and
      the quoted fragments of each row were matched against the row's `quote_verbatim`. Every filing fact carries its
      accession; the 10-K quotations were matched against the filing text by script.
- [x] The order was kept; Q1 closed the file TOO HARD (NATURE); Q2 to Q10 and Q12 are NOT REACHED and nothing after Q1 is
      a clearance. The owner-cash yield in Step 0 is transcription, with no entry language (operator rule 3).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less all stock pay
      less all capital spending, with the finance-lease and component variants shown beside it. The sovereign is from the
      US Treasury, dated 2026-10-05; the price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: in the foundations (against the analyst's
      capital-light prior, and against a TOO HARD close) and weighed again at Q1.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is
      today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **What counts as "all capital spending" when capital arrives as leases and prepayments.** Q7's CONVENTION says the
cash input "deducts all capital spending" and Q4 lists the real costs, but neither says whether finance-lease assets
obtained (non-cash at signing, $24,608M in FY2026), component prepayments carried in investing "Other, net" ($19,861M),
or capex unpaid at year-end ($26.7B in accounts payable) are capital spending. For Microsoft the choice moves FY2026
owner cash from $54,582M to about $10,113M. This run computed the first two variants, gave the third as a figure only, and decided nothing on them, since Q1
closed first; a run that reaches Q7 on a business in a build-out needs a rule. (2) **Test 5 of Q1 when the insider is
the issuer.** Test 5, *would the insiders write it down* **[M2000-105]**, was answered here from the company's own risk factors.
Risk factors are written to disclaim, and almost every 10-K says its markets are competitive and uncertain; read
loosely, the test would close every filer TOO HARD. This run used only the sentences tied to the deciding variable
(demand for the capacity being built "difficult to forecast", the revenue "in advance of fully developed revenue
streams", the cost structure "subject to significant uncertainty") and backed them with the capital figures that make
them decisive. The framework gives no line between boilerplate and a substantive refusal to forecast; it should. (3)
**The by-parts reading at Q1** is written for "a holding company" (CONVENTION). It was applied here to the segments of
an operating company, on the doubt row **[M2002-092]**, because one part (Microsoft 365 Commercial) may be foreseeable
alone and another (the datacenter programme) is not. The framework does not say whether the convention reaches an
operating company's segments. (4) **Tool notes, not fixed (the dispatch forbids it):** `tools/run.py` prints a
three-year window and a "capex alt" that adds finance-lease *principal payments* from the financing section, not the
finance-lease assets obtained; in a build-out the payments lag the assets badly ($3,101M paid against $24,608M obtained
in FY2026), so the tool's alternate understates the capital put in. The run extended the series to eleven years in
`compute.py` from the filed lines. And the research-folder `.gitignore` patterns match only named dump files
(`tenk*.txt`, `*10-K*.txt` and the like); a dump with a generic name is committed silently.
