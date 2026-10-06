# Company Run — JPMorgan Chase & Co. (NYSE: JPM) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Blind analyst run
of record, at the operator's request. Research folder: `Test Runs/_research 2026-10-06 JPM/` (tool outputs, the
arithmetic script and its output, the filing notes; raw filings under its `cache/`, gitignored). This file was copied
from the template before any fetch and written question by question.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open
`PORTFOLIO.md`, any holding review, any earlier JPM run or research folder, the session-state files, the queue, the
prepped reading list or `tools/alerts.json`.
**Contamination, declared:** (1) reading the governing framework as instructed, I met its correction note under Q1 ("Test
B' case A, a very large bank, closed TOO HARD at Q1"); I do not know which bank that case was, and I did not open
`Framework/v5/tests/` to find out, but a large-bank Q1 TOO HARD is now a prior I carry. (2) My training memory holds that
Berkshire once owned and then sold JPM stock and that the speakers have spoken of large banks; that memory is a prior to
be replaced by the filings and is not cited. (3) The v5 ledger names "JP Morgan" in one row only (**[M2025-056]**, the
health-care venture), which bears on nothing here. Antidote, the row's: "if you have doubts about something being into
your circle of competence, it isn’t." **[M2002-092]**, applied to the evidence and not to the prior.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $332.38 (close 2026-10-05, Yahoo chart through `tools/sources.price`; **aggregator, flagged** per operator
  rule 5; saved as `price_JPM.txt`).
- **Shares by class** from the latest filing's cover: one class, common stock, **2,658,186,195** (Form 10-Q for the
  period ended 2026-06-30, filed 2026-08-06, accession `0001628280-26-054343`; `python Screens/cover_shares.py JPM`,
  saved as `cover_shares_JPM.txt`). The preferred stock is not common equity and is not added.
- **Market cap:** about $883.5B (2,658,186,195 × $332.38; `arithmetic.py`).
- **Sovereign for the earnings currency (USD):** 5.66%, the US Treasury daily par yield curve, 30-year, dated
  2026-10-05 (`python tools/sources.py`, issuing authority; saved as `sources_sovereign.txt`).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0000019617:
  - Form 10-K for FY2025, filed 2026-02-13, accession `0001628280-26-008131`: Item 1A risk factors (market, credit,
    liquidity, model risk, legal), the Market Risk Management section (VaR), the deposits table, the fair-value
    hierarchy table, Note 5 derivative notional table, the consolidated balance sheet.
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001628280-26-054343`: the balance sheet,
    trading assets, derivative receivables, average deposits.
  - DEF 14A, filed 2026-04-06, accession `0000019617-26-000096`: fetched; not read past the cover, since Q5 is not
    reached (see Q1).
  - Form 8-K, Item 2.02, filed 2026-07-14, accession `0001628280-26-048078`, EX-99.1 (second-quarter 2026 earnings
    release): read for its headline and its non-GAAP item. The release leads with "NET INCOME OF $21.2 BILLION ($7.70
    PER SHARE), NET INCOME EXCLUDING SIGNIFICANT ITEMS OF $16.9 BILLION ($6.14 PER SHARE)"; the excluded items are a
    $4.6 billion net gain on Visa shares and $1.0 billion of equity-investment gains, so the adjusted figure is lower
    than the reported one. Recorded for Q4, which is not reached.
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $4,424,900 million on the
  consolidated balance sheet of the 10-K, against 4,424,900,000,000 in the XBRL `us-gaap:Assets` fact for the same
  accession. They agree. The 10-K's loans-to-deposits ratio of 58% was also recomputed from its own loans
  ($1,493,429M) and year-end deposits ($2,559,320M): 58.4%.
- **`tools/run.py JPM`:** printed one line, "JPM: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." and nothing
  else, not even the price or the balance-sheet table (saved as `run_py_JPM.txt`). A bank files no capex or D&A facts in
  the shape the tool expects. **Tool defect, reported, not fixed:** for a bank the tool returns no arithmetic lines at
  all, so the price came from `tools/sources.price` and the balance-sheet figures from the filings by hand. No owner-cash
  figure is built: Q1 closes before Q4 and Q7, and a bank's operating cash flow (trading and loan flows) is not owner
  cash in any case.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this balance sheet will be doing in ten years, not where
the quote goes. The market serves and does not instruct **[M2006-077]**: an $883.5B market value says nothing about
whether the condition of the firm can be read. Who is paid to tell you **[M2020-037]**: the earnings release's own
headline ratios (ROE 24%, ROTCE 29%) are the filer's framing and are read as such. The analyst's habits: "What do I not
know that I need to know?" **[M1999-129]**; look for "what’s wrong" and "what you’re missing" **[M2025-013]**; the
worst anchor "is always your previous conclusion" **[M2016-054]**, and here the anchor to resist is the large-bank
TOO HARD declared above.

**Contrary evidence, written down as found** **[M1997-127]**, in the order the filings gave it:
1. The deposit side reads well. Average deposits of $2,506.6B in 2025 at an average rate of 1.80%, against a 30-year
   Treasury of 5.66% today; $604.2B of them noninterest-bearing (24.1%); loans only 58% of deposits (10-K, deposits
   table and liquidity section). That is the "very cheap money on the deposit side" of **[M2002-022]**, and the deposits
   come from "a natural customer base" rather than wholesale **[M2012-012]**.
2. Level 3 is small: $26.5B of $1,831.9B of fair-value assets, about 1% of total assets (10-K, fair-value table); level
   3 derivative receivables $8.9B, about 2.5% of equity (`arithmetic.py`).
3. After legally enforceable netting of $548.6B, net derivative receivables are $57.8B, about 15.9% of equity, and the
   10-K says the notional amounts "significantly exceed, in the Firm’s view, the possible losses that could arise from
   such transactions" (Note 5).
4. The speakers record that they misjudged banking the other way: "banking was a way better business than we figured
   out in advance" **[M2003-114]**; and a bank's low cost of funds is named as an edge Berkshire lacks **[M2016-029]**.
5. The Q2 2026 release's non-GAAP figure removes gains rather than costs (see Step 0), the conservative direction.

## THE STANDING RULE
Not engaged by this run: no purchase is proposed, financed or sized, and none can be, since the file closes at Q1. Any
purchase would be bought with owned money and never on borrowed or callable funds **[M2012-081]**, **[L2014-024]**,
**[M2004-065]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**; the first step is to identify "the key variables" and to evaluate "how
predictable they were" **[M1998-044]**; and "do I understand enough about this business so that the financial statements
will tell me the information that’s useful to me in making a judgment about what the future financial statements are
going to look like" **[M2008-033]**. For a bank the framework's own text fixes the routing (Q1, "The door against the
exclusion, settled"; these are the framework's sentences, not a speaker's): a bank "is inside the circle when both sides
of its balance sheet can be read from its filings [...] and outside it when the asset side cannot", and "A bank that has
both a readable deposit base and a wholesale or derivatives book that its own filing calls unpredictable closes TOO HARD:
the readable half does not make the unreadable half readable". The rows it rests on: "very little risk on the asset side
and very cheap money on the deposit side. And even Charlie and I can understand that." **[M2002-022]**; "throw in
derivatives on top of it" **[M2005-068]**; and of a finance company, "even though I could understand every individual
transaction they did, I don’t regard the whole enterprise, or the operation of it, necessarily as being within my circle
of competence." **[M2002-094]**.

**The key variables of this business**, from the 10-K's own structure (Consumer & Community Banking, Commercial &
Investment Bank, Asset & Wealth Management, Corporate): (a) the cost and stickiness of the deposits; (b) credit losses on
$1,493.4B of loans through a cycle; (c) the capital the regulators require, which can "change the math of banking"
**[M2016-027]**; (d) the losses the market-making and derivatives book can take in a severe shift. Three of the four can
be read from the filings. The fourth is the one the file turns on.

**The deposit side: readable.** Average deposits $2,506.6B in 2025 at 1.80%, $604.2B of them noninterest-bearing, loans
58% of deposits (10-K, accession `0001628280-26-008131`); Q2 2026 average deposits $2,685.6B at 1.60% (10-Q, accession
`0001628280-26-054343`). This is the "very cheap money on the deposit side" **[M2002-022]** from "a natural customer
base" and not "on a wholesale basis" **[M2012-012]**. Banking "if you just keep out of trouble on the asset side, is a
very good business because you get your money so cheap" **[M2011-022]**. This half passes.

**The asset side: not readable, on the filing's own words.**
- **Scale.** Trading assets $802.9B of $4,424.9B total assets at 2025-12-31 (18.1%), rising to $1,062.1B of $5,015.1B at
  2026-06-30 (21.2%). Free-standing derivative notional **$50,642B** at 2025-12-31, about 140 times stockholders' equity
  of $362.4B. Gross derivative receivables of $606.4B, about 1.67 times equity, are carried at $57.8B only after
  $548.6B of netting (Note 5 and the fair-value table, 10-K; `arithmetic.py`). At Q2 2026 the gross figure is about
  $690.6B, netted to $67.8B. Markets revenue was $35.8B of $185.6B managed revenue in 2025 (19.3%). This is not a
  side-line; it is a fifth of the balance sheet and a fifth of the revenue, and its size against equity rests on the
  netting holding in a crisis.
- **What the filer says of it.** "As VaR is based on historical data, it is an imperfect measure of market risk exposure
  and potential future losses. [...] VaR measures are inherently limited in their ability to measure certain risks and to
  predict losses, particularly those associated with market illiquidity and sudden or severe shifts in market
  conditions." (10-K, Market Risk Management.) Its "market-making businesses could suffer losses due to unanticipated
  market events and conditions, including [...] events or conditions that cause previously uncorrelated market factors to
  become correlated [...] other market risks that may not have been adequately considered when developing, structuring
  or pricing a financial instrument"; market conditions "could make it extremely difficult to value certain financial
  instruments"; "hedging and other risk management strategies may not always be effective, and it could incur
  significant losses, if extreme market events were to occur"; and its models "may not be effective in all cases" because
  of "inherent limitations associated with forecasting uncertain economic and financial outcomes" (10-K, Item 1A). The
  firm that holds the book declines, in its own filing, to say what the book can lose in the conditions that matter.
- **What the rows say of exactly this.** "When Charlie and I finish reading the long footnotes detailing the derivatives
  activities of major banks, the only thing we understand is that we don't understand how much risk the institution is
  running." **[L2002-018]**; "with financial institutions, it’s much tougher. Then you add — throw in derivatives on top
  of it [...] no one probably knows [...] or even within a reasonable range — the exact condition of some of the biggest,
  you know, banks in the world." **[M2005-068]**; "You spot troubles in financial institutions late. It’s just the nature
  of the beast." **[M2001-066]**. Size is not the reason: the framework's own text says "Size alone decides nothing",
  reading the row as naming "some of the biggest [...] banks in the world" for a condition that cannot be known, not for
  their size **[M2005-068]**; the reason is the derivatives "on top of it", which this bank carries at $50.6 trillion of
  notional.
- **Gearing.** Total assets are 12.2 times equity at 2025-12-31 and 13.4 times at 2026-06-30 (`arithmetic.py`); the
  release's ROE of 24% is read for how much of it is gearing **[M2007-013]**, a question the readable half can answer
  and the unreadable half cannot.

**Tests, as the section lists them.** 1, where will it be in ten years: the deposit and lending franchise can be pictured;
the condition of the book cannot **[M1999-132]**. 2, the key variables and their predictability: (d) is named by the filer
as not predictable from its own models **[M1998-044]**. 3, do the past statements tell me the future ones: for (d) the
filer says its own history-based measure does not **[M2008-033]**. 4, important and knowable: important, and not
knowable from outside **[M2006-076]**. 5, would the insiders write it down: they have not; the VaR passage is the
insiders declining to **[M2000-105]**. 8, how far off could I be: on the book, by an amount I cannot bound
**[M2011-084]**. 9, do I doubt it is inside: yes, so it is not **[M2002-092]**. 12, for a derivatives book: whether both
sides of a zero-sum trade "put on the books a profit that day" **[M2004-026]** cannot be tested from the outside; the
funding test of the same item, "natural customer base" against "wholesale", is passed **[M2012-012]**.

**Contrary evidence weighed, not dismissed** **[M1997-127]**: the small level 3 share, the netting, and the filer's
statement that notional amounts "significantly exceed [...] the possible losses" are real and are written in the
foundations. They are the filer's own estimate of the same book, made with the models it says are "inherently limited";
they do not make the book readable to an outsider. Of the speakers' own bank holdings, the row that admits them asks to
"know something about the culture of the management and the institution to make a firm buy decision on a bank, and
that’s hard to do for 99 percent of the banks" **[M2008-090]**; I have no such knowledge and the filings do not supply
it. The public Federal Reserve stress-test results were not read; they model a prescribed scenario and do not give the
condition of the book "within a reasonable range" **[M2005-068]**, so in my judgment they would not answer the deciding
question. That judgment is mine and is stated so that another analyst can contest it.

**VERDICT: TOO HARD.** The deposit half is readable; the derivatives and market-making half, $50.6 trillion of notional
and a fifth of the balance sheet, is one the filer's own 10-K says its models cannot predict in a severe shift, which is
the case the framework closes at Q1 (its sentence: the readable half does not make the unreadable half readable) on the
rows **[M2002-094]**,
**[M2005-068]**, **[L2002-018]**; the box is "too hard" **[M2006-013]**. It is no judgment that anything is wrong with
the bank: "It’s no judgment that there’s anything bad." **[M2007-052]**; "It doesn’t mean it isn’t a good buy. [...] It
just means that we don’t know how to evaluate it." **[M2000-038]**.

**Cause: NATURE.** The deciding question, what the book can lose in "sudden or severe shifts in market conditions", is a
forecast the insiders would not write down (test 5, **[M2000-105]**), and the filing is the proof that they have not.
The rows say study does not cure it: "We couldn't solve this problem, moreover, even if we were to spend years intensely
studying those industries." **[L1993-023]**; of Gen Re's book, "we still wouldn’t have known what was going on"
**[M2013-089]**; "we’re not going to learn enough in the followings five months to make up for the fact that we went in
deficient in the first place." **[M2008-086]**; and "It’s just the nature of the beast." **[M2001-066]**. No research
pass is opened (Part VII). A lower price does not reopen the box **[M2000-038]**. The circle is not widened to find
something to buy **[M1995-018]**.

**Reversal condition, one line:** the file reopens only if the derivatives and market-making book ceased to be material
to the firm's condition (separated, or shrunk so that the firm's condition rests on loans and deposits the filings let
an outsider read), never on a price.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED.
The STOP at Q1 closed the file. No castle test, competitor row or verdict is given.

## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
The earnings release's non-GAAP headline is recorded in Step 0 as a fact only; no Q4 judgment is made from it.

## Q5 — WHO RUNS IT? NOT REACHED.
The proxy was fetched and not read.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.

## Q7 — WHAT IS IT WORTH? NOT REACHED.
No value range, "fair" price or "cheap" price is computed, and no valuation arithmetic was done (operator rule 3).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.

## Q9 — COULD IT RUIN US? NOT REACHED.
Its test 10 points back to Q1 for a financial institution, which is where this file closed.

## Q10 — IS IT THE FAT PITCH? NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED (not asked).

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the deposit side can be read; the derivatives and market-making book ($50,642B
of notional, trading assets 21.2% of total assets at 2026-06-30) cannot, and the filer's own 10-K says its loss
measures are "inherently limited in their ability [...] to predict losses" in "sudden or severe shifts in market
conditions" (10-K, accession `0001628280-26-008131`); rows **[M2005-068]**, **[L2002-018]**, **[M2002-094]**. Q7 not reached; no value range. Price $332.38 (aggregator,
flagged), market cap about $883.5B, sovereign 5.66%. Q11 belongs to the holding review, not to this run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Step 0 and after Q1
      (write-early).
- [x] Every v5 id resolves: 39 distinct ids checked against `principle_ledger_v5.csv` by
      `_research 2026-10-06 JPM/check_ids_and_quotes.py`, none missing, and every quoted fragment set directly before
      an id found in that row; the others were checked by hand. Two sentences of the framework's own text (the bank-door
      routing and "Size alone decides nothing") were first written as if they were row quotations; corrected before the Q1
      commit, and now marked as the framework's sentences. Every filing fact carries its accession.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] No owner-cash figure was built (Q4 and Q7 not reached), so no net-income proxy was used; the sovereign is from the
      issuing authority (US Treasury, 2026-10-05); the price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations, five items) and weighed at Q1.
- [x] No row dated after the anchor is cited: the run is dated today and is not a point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used: it printed none for a bank (defect reported below).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. **(1) "calls unpredictable" is literal or substantive?** The Q1 bank-door sentence closes a bank whose
derivatives book "its own filing calls unpredictable". JPM's 10-K uses the word "unpredictable" of its legal exposure
and of geopolitics, not of its trading book; of the trading book it says its VaR is "inherently limited in [its]
ability [...] to predict losses" and that its models face "inherent limitations associated with forecasting". I read
the rule by substance, the filer declining to predict the book's losses, and said so; a literal reader could find the
rule not triggered and send the file on to Q2. Nearly every large bank's 10-K carries the same model-risk boilerplate, so
the substantive reading closes almost every bank with a market-making book, and the framework does not say whether that
is intended or what share of the balance sheet or revenue makes the book "material" (I used a fifth of each). **(2) WORK
or NATURE for a bank.** The two-cause rule sends a forecast "the industry's own insiders would not write down" to
NATURE. The bank's insiders do publish a forecast of a kind (VaR, and the regulator's stress-test results), but disclaim
it for the severe case; the framework does not say whether a disclaimed forecast counts as one written down. I read it
as not written down, citing **[M2001-066]** ("the nature of the beast"), and recorded that the Federal Reserve
stress-test results were not read. **(3) Tooling.** `tools/run.py JPM` prints only "no overlapping OCF/D&A/capex annual
facts. UNRESEARCHED." for a bank and stops before printing the price, the shares or the ten-year balance-sheet table
that the template's Q4 line says it prints; the template's Step 0 therefore has no tool path for a bank's arithmetic
lines, and they were taken from `tools/sources.price` and the filings by hand. Reported, not fixed.
