# Company Run — Wells Fargo & Company (NYSE: WFC) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Blind analyst run
of record. Research folder: `Test Runs/_research 2026-10-06 WFC/` (tool outputs, the fetch and strip scripts, the
arithmetic script and its output; the raw filings and their text dumps sit under its `cache/`, gitignored). Written top
to bottom, question by question; the template was copied to this file before any fetch.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open `PORTFOLIO.md`,
any earlier WFC run or research folder, any holding review, the session-state files, the run queue, the prepped reading
list or `tools/alerts.json`.

**Contamination, declared.** (1) The governing document itself names this company: Q5 and Q6 list "Wells Fargo" among the
mistakes the speakers narrate (**[M2018-012]**, **[M2019-005]**, **[M2017-005]**), and a sweep of `principle_ledger_v5.csv`
for "Wells" returns rows that are the speakers' own past verdicts on it (**[M1995-097]**, **[M2008-090]**, **[M2009-036]**,
**[M2012-012]**, **[M2012-037]**, **[M2014-046]**). I read them because the brief sends me to the ledger; they are
judgments about the company as it stood in those years, and I carry them below as contrary evidence, not as verdicts.
(2) My training memory holds a prior: Berkshire's long holding of the stock and its later sale, the sales-practices
scandal of 2016, the Federal Reserve's asset cap of 2018 and its removal in 2025. That prior is replaced by the filings
where they speak, and nowhere relied on. The incentive operator rule 9 names runs both ways here: a famous Berkshire
holding invites clearance by association; the antidote is the row's, "if you have doubts about something being into your
circle of competence, it isn’t." **[M2002-092]**.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $81.44 (close 2026-10-05, Yahoo chart API read through `tools/sources.py` `price()`; **aggregator, flagged**
  per operator rule 5).
- **Shares by class** from the latest filing's cover: one class of common stock (par $1-2/3), **3,023,999,336** shares
  (Form 10-Q for the period ended 2026-06-30, filed 2026-07-28, accession `0000072971-26-000302`;
  `python Screens/cover_shares.py WFC`, which first printed "FETCH FAILED: HTTP Error 429" and succeeded on a retry with
  backoff). The preferred series listed on the cover (Series L convertible and the depositary shares) are not common
  equity and are not added; their liquidation preference was $16,116M at 2026-06-30 (10-Q balance sheet).
- **Market cap:** about **$246,275M** (3,023,999,336 × $81.44; `arithmetic.py` in the research folder).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated 10/05/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0000072971:
  - Form 10-K for FY2025, filed 2026-02-24, accession `0000072971-26-000133`; the financial review and statements are its
    Exhibit 13, filed inside the primary document (overview, Tables 1-2, balance sheet analysis, Tables 10-14, off-balance
    sheet arrangements, market risk and Table 29, liquidity and funding, model risk, risk factors, Note 13 Derivatives,
    Table 44 Level 3 summary, the consolidated statements, the critical audit matter).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-28, accession `0000072971-26-000302` (balance sheet,
    segment tables for Corporate and Investment Banking, Table 23 VaR, derivative tables, legal actions).
  - Form 8-K, Items 2.02/7.01/9.01, filed 2026-07-14, accession `0000072971-26-000288`, Exhibit 99.1 (the second-quarter
    2026 release; read for its headline figures and its Markets commentary).
  - DEF 14A filed 2026-03-18, accession `0000072971-26-000200`: fetched; not read past the cover, since Q5 and Q6 were
    not reached.
  - Form 8-K, Item 5.02, filed 2026-09-23, accession `0000072971-26-000308` (the Chief Operating Officer named Chief Risk
    Officer effective 2027-01-15).
- **One figure cross-checked against the filed statement:** total deposits at 2025-12-31, **$1,426,207M** on the
  consolidated balance sheet of the 10-K, against 1,426,207,000,000 in the XBRL concept `us-gaap:Deposits` for accession
  `0000072971-26-000133`. They agree. (The 10-Q's 2026-06-30 figure, $1,501,405M, also agrees with its XBRL fact.)
- **`tools/run.py WFC`:** it printed one line, "WFC: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.", and exited
  with status 1 (saved as `run_py_output.txt`). It produced no arithmetic lines at all, so none was used; the price,
  shares and balance-sheet figures above come from the cover tool, the price function and the filed statements. Its
  "owner earnings" construction (operating cash less capex) would in any case be meaningless for a bank, whose operating
  cash flow carries trading and loan-sale flows. Q1 closes before Q4 and Q7, so no substitute cash figure is built.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this bank will be in ten years, not where the quotation goes.
The market serves and does not instruct **[M2006-077]**: a $246B market value says nothing about whether the condition of
a $2.28T balance sheet can be read. Who is paid to tell you **[M2020-037]**: the 10-K's own non-GAAP line, "net interest
income excluding Markets", is offered so that readers can assess the lending and deposit business "without the volatility
that may be associated with Markets activities"; that is management's framing and is read as such. The analyst's habits:
the worst anchor "is always your previous conclusion" **[M2016-054]**, and the previous conclusion on offer here is not
mine but the speakers' own, from the years they owned the stock; look in every business for "what’s wrong" and "what
you’re missing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**, in the order it was met:
1. The ledger's rows on this company run in its favour for the years they cover: its real-estate lending "was way better
   than average" in the early 1990s **[M1995-097]**; its deposits come "from a natural customer base" **[M2012-012]**;
   "we felt 100 percent comfortable buying Wells Fargo" **[M2014-046]**; and the speaker of **[M2008-090]** said of the
   banks he held that he understood "quite well the DNA of the institution". These are the strongest evidence that a bank
   of this name has been inside the circle. They describe a balance sheet that the filings below show has since changed.
2. The deposit side is cheap and large: $1,501,405M of deposits at 2026-06-30, $370,116M of them noninterest-bearing
   (24.7%); average deposit cost 1.44% in the fourth quarter of 2025 (10-K, Deposits); loans 68.7% of deposits.
3. The trading book, by the filer's own measures, is small against equity: average one-day 99% Trading General VaR of
   $31M in the second quarter of 2026 (10-Q, Table 23); Level 3 assets $7.0B, 0.3% of total assets at 2025-12-31 (10-K,
   Table 44); net derivative exposure after netting and collateral $19,604M at 2026-06-30, about 10.8% of total equity
   (10-Q, Note on derivatives). And the speakers warn against the notional figure I would otherwise lead with: "There is
   no perfect measurement of the size of a derivative position. [...] they tend to exaggerate things in a huge — in a
   very dramatic way, in terms of trillions of this or that." **[M2004-127]**.
4. Against these, as found: the total assets rose $218,786M in 2025 (10-K, Table 1), and the filing names the place:
   repurchase-agreement liabilities rose from $95,235M to $232,687M "driven by increased client-driven activity in our
   Markets business" (10-K, Liquidity Risk and Funding); resale assets rose $88,599M and trading assets $59,340M. By
   2026-06-30 the Corporate and Investment Banking segment held $862,472M of assets (37.8% of the total), of which
   $444,717M were trading-related assets, up 52% in a year (10-Q, segment table).
5. Derivative notionals of $18,728,686M at 2025-12-31 and $19,449,472M at 2026-06-30 (Table 13.1 of each filing), about
   107 times total equity; the filing itself says the notional "is not, when viewed in isolation, a meaningful measure of
   the risk profile of the instruments" (10-K, Note 13), which is the same warning as **[M2004-127]**.
6. The 10-K's risk factor on models: "there is no assurance that these models will appropriately or sufficiently capture
   all relevant risks or accurately predict future events or exposures", said of the models that "measure, monitor and
   predict risks, such as market, interest rate, liquidity and credit risks".
7. Regulatory standing at the 10-K date: "we are subject to a consent order and other regulatory actions, including a
   February 2018 consent order with the FRB regarding the Board’s governance and oversight of the Company, and the
   Company’s compliance and operational risk management program", and "a September 2024 formal agreement with the OCC
   regarding anti-money laundering" (10-K, Risk Factors). A text search of the 10-Q for "consent order" found no update.
8. Estimated uninsured deposits of $600B at 2025-12-31, 42.1% of deposits (10-K, Deposits).

## THE STANDING RULE
Nothing in this purchase need put the buyer at risk of ruin, provided it is paid for in cash and never with borrowed money
**[L2014-005]**, **[M2004-065]**, and sized so that the loss of the whole stake could not end the buyer, since "anything
times zero is zero" applies to a bank share as to any other **[M2007-050]**; "it’s our job to figure out what can really
go wrong" **[M2012-081]**. The question is moot here because the file
closes at Q1; it is recorded so that a reopened file starts from it.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it for a bank.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**. A bank is inside the circle when both sides of
its balance sheet can be read from its filings, "very little risk on the asset side and very cheap money on the deposit
side" **[M2002-022]**, and outside it when the asset side cannot; and "A bank that has both a readable deposit base and a
wholesale or derivatives book that its own filing calls unpredictable closes TOO HARD: the readable half does not make the
unreadable half readable" (the settled rule in Q1, resting on **[M2002-094]**). Size alone decides nothing **[M2005-068]**,
**[M2012-012]**. So the run reads the two sides in turn, and the asset side in its two halves.

**The deposit side: readable, and cheap.** Deposits $1,501,405M at 2026-06-30, $370,116M noninterest-bearing (24.7%);
average deposit cost 1.44% in the fourth quarter of 2025; "Deposits have historically provided a sizable source of
relatively low-cost funds" (10-K, Funding Sources). That is the "natural customer base" of **[M2012-012]**, and the
cheapness the bank rows prize: "Banking, if you just keep out of trouble on the asset side, is a very good business
because you get your money so cheap" **[M2011-022]**. One qualification, readable from the filing: $600B of deposits
(42.1%) were estimated uninsured at 2025-12-31.

**The asset side, first half: the loan and securities book, readable.** Loans $1,031,115M at 2026-06-30, set out by class
and maturity (10-K, Tables 11 and 12); net charge-offs in 2025 of 19 basis points of average commercial loans and 79 of
average consumer loans; nonperforming assets 0.86% of loans; the allowance 1.45% of loans (10-K, Credit Quality). The
debt securities, $448,899M at 2026-06-30 (10-Q balance sheet), were 99% rated AA- or above at 2025-12-31 and
"predominantly" Treasury, agency and agency MBS (10-K, Balance Sheet Analysis), with an unrealized loss on the held-to-maturity book of $32,226M at 2025-12-31 that
the filing states outright. A reader can see what this half holds, what it has lost, and where the danger is "always on
the asset side" **[M2011-022]**. Had the bank been only this, the door of **[M2002-022]** would be open to argument.

**The asset side, second half: the Markets book, not readable from outside.** The facts, from the filings:
- The Corporate and Investment Banking segment held $862,472M of assets at 2026-06-30, 37.8% of the total; of these,
  $444,717M were trading-related assets (trading assets, derivative assets and resale agreements), up 52% in a year, and
  Markets loans were $111,624M, up 36% (10-Q, segment table).
- The growth is the filer's own account of where 2025's $218,786M of new assets went: repurchase liabilities rose
  $137,452M "driven by increased client-driven activity in our Markets business"; resale assets rose $88,599M and trading
  assets $59,340M (10-K, balance sheet and Liquidity Risk and Funding). "Net interest margin decreased in 2025 [...] driven
  by growth in our Markets business."
- Derivative notionals $19,449,472M at 2026-06-30 (10-Q, Table 13.1), about 107 times total equity of $182,323M.
- Wholesale funding: repurchase agreements, short-term borrowings and trading liabilities were $333,603M at 2026-06-30,
  15.9% of liabilities. Of such money the rows say "on a wholesale basis, and that money can run pretty fast" **[M2012-012]**.
- What the filer itself says of the book: it offers a measure of net interest income excluding Markets so that the rest
  can be judged "without the volatility that may be associated with Markets activities" (10-K, Earnings Performance); its
  VaR is a one-day, 99%, twelve-month-look-back historical simulation, and "Given the inherent limitations of the VaR
  models, the Company uses other measures"; its stress scenarios rest on "management’s assumptions"; and of the models
  that "measure, monitor and predict risks, such as market, interest rate, liquidity and credit risks", "there is no
  assurance that these models will appropriately or sufficiently capture all relevant risks or accurately predict future
  events or exposures" (10-K, Market Risk and Risk Factors).

**Weighing the contrary evidence written down above.** The filer's measures of this book are small: VaR $31M, Level 3
0.3% of assets, net derivative exposure about 10.8% of equity; and the notional is the figure the rows tell me not to lead
with **[M2004-127]**. I accept all of that and it does not settle the question, for two reasons the rows give. First, every
one of those small numbers is the bank's own model output on positions I cannot see; the key variable of this half of the
business is how $445B of trading-related assets and $19T of notional behave when "everything correlates" **[M2005-025]**,
and neither the filing nor I can say "how far off we can be" **[M2011-084]**. Second, the rows name exactly this case and
put it outside: "with financial institutions, it’s much tougher. Then you add — throw in derivatives on top of it, and,
you know, it’s — no one probably knows, you know, perfectly, what some of the — or even within a reasonable range — the
exact condition of some of the biggest, you know, banks in the world." **[M2005-068]**; "even though I could understand
every individual transaction they did, I don’t regard the whole enterprise, or the operation of it, necessarily as being
within my circle of competence." **[M2002-094]**; "the only thing we understand is that we don't understand how much risk
the institution is running." **[L2002-018]**; "You spot troubles in financial institutions late. It’s just the nature of
the beast." **[M2001-066]**.

**The speakers' own past verdicts on this name, weighed.** **[M2014-046]** and **[M2008-090]** say the speakers were
comfortable with this bank and understood its "DNA". They were said of the bank of 2008 to 2014. The filings read today
show a different balance sheet, one whose fastest-growing third is a markets book, and a regulatory record the same
filing states: a February 2018 Federal Reserve consent order "regarding the Board’s governance and oversight of the
Company, and the Company’s compliance and operational risk management program", still named at the 10-K date, and a
September 2024 OCC formal agreement on anti-money-laundering practices. **[M2008-090]** itself sets the bar for a firm
buy decision on a bank at knowing "the culture of the management and the institution", "hard to do for 99 percent of the
banks"; from the documents I can read that the governance order is now in its ninth year, and no more. The worst anchor
"is always your previous conclusion" **[M2016-054]**, and borrowing the speakers' conclusion about an earlier bank would
be that anchor at one remove.

**Test 9 and test 10.** "if you have doubts about something being into your circle of competence, it isn’t."
**[M2002-092]**: I have that doubt about the half of the asset side that grew fastest. "what would bother me is if I think
I understand a business and I don’t." **[M1997-024]**: the readable deposit and loan franchise is exactly what would
make me think I understand this one. The literal trigger of the settled rule, a book "that its own filing calls
unpredictable", is met in substance and not in that word: the 10-K uses "inherently unpredictable" of its mortgage
servicing rights and of legal actions, and of the Markets book says "volatility" and "no assurance [...] accurately
predict" (see the section on the framework, below).

**The cause.** The deciding question is the condition of the Markets and derivatives book within a reasonable range,
under stress, over ten years. It is important, and it is not knowable from outside **[M2006-076]**: the filer's own
document declines to write the forecast down (the models carry "no assurance"), and the row says "no one probably knows"
**[M2005-068]**, which is test 5's mark of the industry's cause, insiders who "would not want to put down on paper" the
forecast **[M2000-105]**. More reading would give me the regulator's stress models or a rating, not a reading of the book,
and "we don’t believe in outsourcing investment decisions" **[M2009-011]**. The cause is the nature of the institution,
not work undone: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those
industries." **[L1993-023]**. A lower price does not reopen it: "It doesn’t mean it isn’t a good buy. It doesn’t mean it
isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**.

**What would reopen the file** (a change in the business, never in the price): filings showing the Markets book shrunk
back to a part of the balance sheet whose loss under stress could be read from the statements themselves, so that the
bank is again deposits funding loans and high-grade securities, the two sides of **[M2002-022]**.

- **VERDICT: TOO HARD (NATURE).** The deposit side and the loan book can be read; the markets and derivatives book (in a
  segment holding 37.8% of total assets, with $444,717M of trading-related assets and $19.4T of notional) cannot be read
  from outside, and its own filer gives
  "no assurance" its models predict it **[M2005-068]**, **[M2002-094]**, **[L2002-018]**, **[M2002-092]**; the box is "too
  hard" **[M2006-013]**. The file closes here; Q2 to Q12 are NOT REACHED.

## Q2 to Q12 — NOT REACHED
Q1 closed the file TOO HARD (NATURE). Under the hard sequence nothing after it is answered, and no valuation was
computed: no value range, no "fair" or "cheap" price, no buyback or pay reading, no ranking against the bond. The DEF 14A
was fetched and not read. Q11 belongs to a holding review, not to a purchase run.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** Wells Fargo's deposit side and loan and securities book can be read from its
filings; its Markets and derivatives book (CIB segment 37.8% of total assets, $444,717M of trading-related assets up 52%
in a year, $19.4T of derivative notional, $333,603M of wholesale and trading liabilities) cannot be read from outside,
and the filer's own risk factor gives "no assurance" that its models predict it **[M2005-068]**, **[M2002-094]**,
**[M2002-092]**. Price $81.44 (aggregator, 2026-10-05); market cap about $246,275M; no range computed. Reopened only by a
change in the business (the Markets book shrunk back to a part whose stressed loss can be read from the statements),
never by a lower price **[M2000-038]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      step 0 with the foundations and standing rule (`cc46092`), Q1 (`e3f9f16`), the close (this commit).
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv`, and every quoted fragment matched against its row
      before writing); every filing fact carries its document and accession; no number without a filing or a row.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance.
- [x] Owner cash: not computed, because Q1 closed before Q4 and Q7; no net-income proxy appears anywhere. The sovereign is
      from the US Treasury (5.66%, 10/05/2026); the price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, eight items, including the speakers' own past
      verdicts in this company's favour and the filer's small risk measures.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): this is a live run dated 2026-10-06, so
      the anchor rule does not bind; no row is dated after 2025.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): it printed none, and nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The settled bank rule turns on the filer's vocabulary.** Q1 closes TOO HARD a bank whose derivatives or wholesale
book "its own filing calls unpredictable". Wells Fargo's 10-K uses "inherently unpredictable" only of its mortgage
servicing rights and its legal actions; of the Markets book it says "volatility" and gives a generic risk factor that its
models carry "no assurance" of predicting exposures, a sentence nearly every large bank prints. Read literally the rule is
either never met or always met by boilerplate, so it cannot discriminate; I decided on the substance of **[M2005-068]**
and **[M2002-094]** and declared the literal gap. A rule that named what must be readable (the stressed loss of the
trading and counterparty book from the filer's own statements) would decide the next bank the same way for two analysts.
(2) **No proportion test.** The door of **[M2002-022]** is drawn for "oddball" banks with little risk on the asset side;
the framework gives no way to say when a markets book is large enough to shut it (here 19.5% of total assets are CIB
trading-related assets). (3) **WORK against NATURE for a regulated bank is unclear.** Test 5 asks whether the insiders
would write the forecast down; for a large bank the regulator publishes stressed trading and counterparty losses each
year. Whether that is the insiders writing it down (WORK, to be read) or an outsourced judgment the rows refuse
(**[M2009-011]**, NATURE) is not said; I took the second. (4) **The ledger carries the speakers' own verdicts on the name
being run** (**[M2014-046]**, **[M2008-090]**, **[M2012-012]**). Part VII's anchor convention bars later rows only in a
point-in-time test; nothing tells a live run how to treat earlier rows that judge the very company. I carried them as
contrary evidence about the company of their years, not as verdicts. **Tool defects:** `tools/run.py WFC` exits with status
1 and the single line "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." for a bank, printing no price, share or
balance-sheet lines, so a bank run gets no arithmetic from it at all; `Screens/cover_shares.py` reported "FETCH FAILED:
HTTP Error 429" and still exited 0, so a caller that checks the exit status would not see the failure (it succeeded on a
retry with backoff).
