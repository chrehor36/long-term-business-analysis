# Company Run — Morgan Stanley (NYSE: MS) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Blind analyst run
of record. Research folder: `Test Runs/_research 2026-10-06 MS/` (the tool outputs, the arithmetic script and its output,
the fetch script; raw filings under its `cache/`, gitignored). Fill top to bottom; every judgment cites a v5 ledger id in
bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are
marked NOT REACHED. This file was copied from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open `PORTFOLIO.md`,
any holding review, any earlier MS run or research folder, the resume-state files, the queue, the prepped reading list or
`tools/alerts.json`. **Contamination, declared:** none from the repository that I noticed. My training-memory of the
company (a large broker-dealer turned bank holding company, with a wealth business grown by acquisition) is a prior, and
every fact below is taken from the filings instead. I read one other v5 run (CCB, 2026-10-05) for form only.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $190.19 (close 2026-10-05, Yahoo chart endpoint through `tools/sources.price`; **aggregator, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, $0.01 par, **1,570,566,292** (Form 10-Q for
  the period ended 2026-06-30, filed 2026-08-04, accession `0000895421-26-000212`; `python Screens/cover_shares.py MS`,
  output in the research folder). The preferred series are not common equity and are not added.
- **Market cap:** about $298,706M (1,570,566,292 × $190.19; `arithmetic.py`).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, dated 2026-10-05
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 0000895421:
  - Form 10-K for FY2025, filed 2026-02-19, accession `0000895421-26-000086` (Item 1A risk factors, the market-risk and
    VaR section, the funding and deposits section, the consolidated balance sheet, the fair-value hierarchy note, the
    derivative notionals note, the segment note).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession `0000895421-26-000212` (balance sheet,
    fair-value table, derivative notionals, segment assets).
  - DEF 14A, filed 2026-04-02, accession `0001140361-26-012975` (fetched; Q5 and Q6 not reached, so not judged).
  - Form 8-K, Items 2.02 and 9.01, filed 2026-07-15, accession `0000895421-26-000207`, EX-99.1, the second-quarter 2026
    earnings release. Its headline measures include ROTCE and tangible book value per share, which the release footnotes
    as non-GAAP; Q4 was not reached, so no judgment of the non-GAAP habit is made.
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $1,420,270 million on the
  consolidated balance sheet in the 10-K, against 1,420,270,000,000 in the XBRL `Assets` fact of the same accession
  (`0000895421-26-000086`); total assets at 2026-06-30, $1,675,057 million in the 10-Q balance sheet, against the XBRL fact
  of accession `0000895421-26-000212`. They agree.
- **`tools/run.py MS`:** it printed one line, "MS: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED.", and no
  arithmetic (output saved in the research folder). No owner-cash line was therefore produced by the tool. For a
  broker-dealer and bank an operating-cash-flow-less-capex figure would in any case carry trading-inventory and customer
  balance flows and would not be the cash an owner can take out. Q1 closes before Q4 and Q7 (below), so no substitute
  owner-cash figure is built and none is written (operator rule 5: no net-income proxy).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this firm's balance sheet and earning power will be in ten
years, not what a record quarter does to the quote. The market serves and does not instruct **[M2006-077]**: a price that
has carried the market value to about $299 billion says nothing about value. Who is paid to tell you **[M2020-037]**,
**[M2011-083]**: this is the one name in the queue whose own business is the fee-earning advice the foundations warn
about, and its release's language ("exceptional results", "record") is the seller's description of what it sells. The
analyst's habits: look for "what’s wrong" and "what you’re missing" **[M2025-013]**, and do not let the prior from
memory stand as a conclusion **[M2016-054]**.

**Contrary evidence, written down as found** **[M1997-127]**, in the order the filings gave it, both ways:
1. *For understanding:* the 10-K says deposits "are primarily sourced from our Wealth Management clients and are
   considered to have stable, low-cost funding characteristics relative to other sources of funding" (10-K,
   `0000895421-26-000086`). That is the readable deposit side the bank door asks for.
2. *For understanding:* Level 3 assets were $8,039M at 2025-12-31, about 1.5% of $532,009M of assets carried at fair
   value and about 7.2% of $111,632M of shareholders' equity (10-K fair-value table; `arithmetic.py`). Most of the marked
   book is Level 1 and Level 2.
3. *For understanding:* "There were six trading loss days in 2025, none of which exceeded 95% Total Management VaR" (10-K).
4. *Against:* gross derivative notionals on the asset side of $15,847 billion at 2025-12-31 and $19,441 billion at
   2026-06-30 (10-K note; 10-Q note), about 167 times shareholders' equity of $116,329M. The firm itself says notionals
   "generally overstate the Firm’s exposure"; the number is set down as the size of the book that has to be read, not as
   the exposure.
5. *Against:* total assets rose from $1,420,270M to $1,675,057M in six months, about 17.9%, and the Institutional
   Securities segment's share of total assets from 68.3% to 78.7% (10-K and 10-Q segment tables). Deposits were 31.8% of
   total liabilities at 2025-12-31 and 28.6% at 2026-06-30; the rest is borrowings ($392,556M), repurchase agreements,
   securities loaned, other secured financings, customer payables and trading liabilities (10-Q balance sheet).
6. *Against:* the 10-K's own risk factor: "Our risk management strategies, models and processes may not be fully effective
   in mitigating our risk exposures in all market environments or against all types of risk, which could result in
   unexpected losses", and "these methods may not predict future risk exposures, which could be significantly greater
   than the historical measures indicate", and the techniques "cannot anticipate every economic and financial outcome or
   the timing of such outcomes" (10-K, Item 1A).
7. *Against:* Institutional Securities pre-tax income was $4,476M in 2023, $8,749M in 2024 and $11,237M in 2025, from
   37.9% to 51.2% of the firm's pre-tax income; it rose 2.5 times in two years (10-K segment note).

## THE STANDING RULE
Owning a part-interest in MS bought for cash puts the buyer at no risk of ruin by the buyer's own conduct: no borrowed
money and no instrument that can call is assumed **[L2014-005]**, **[L2014-024]**; the rule binds how the purchase is
financed and sized **[M2012-081]**, and nothing in a cash purchase of a listed share gives anyone the switch. Passed as a
condition of the buyer; it says nothing about the business.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**; "we will never buy anything we don’t think we
understand" **[M2000-037]**. For a financial institution the framework fixes the routing: "A bank is inside the circle
when both sides of its balance sheet can be read from its filings, the little-risk asset side and the cheap deposit side
**[M2002-022]**, and outside it when the asset side cannot **[M2005-068]**. [...] A bank that has both a readable deposit
base and a wholesale or derivatives book that its own filing calls unpredictable closes TOO HARD: the readable half does
not make the unreadable half readable **[M2002-094]**." (framework, Q1, The door against the exclusion, settled.)

**What the filings show, half by half.**
- **The deposit side is readable and, by the firm's own account, cheap.** Deposits of $446,068M at 2026-06-30, "primarily
  sourced from our Wealth Management clients" and "considered to have stable, low-cost funding characteristics" (10-K,
  `0000895421-26-000086`; 10-Q, `0000895421-26-000212`). This is the "natural customer base" of **[M2012-012]**.
- **But deposits fund well under a third of the liabilities.** 31.8% at 2025-12-31 and 28.6% at 2026-06-30; borrowings of
  $392,556M (of which $147,514M at fair value), repurchase agreements of $102,202M, other secured financings, securities
  loaned, customer payables of $279,070M and trading liabilities of $255,589M carry the rest (10-Q balance sheet). The
  funding the rows call fast, "on a wholesale basis, and that money can run pretty fast" **[M2012-012]**, is the larger
  part. This is the finance-company question in Buffett's own words: "whether I can continually fund it" **[M2002-094]**.
- **The asset side is a dealer's book.** Trading assets at fair value of $428,276M at 2025-12-31, of which $213,269M
  pledged; securities borrowed and resale agreements of $272,151M; gross derivative notionals of $15,847 billion (asset
  side) at 2025-12-31 and $19,441 billion at 2026-06-30 (10-K and 10-Q derivative notes). The balance sheet grew 17.9% in
  six months, and the Institutional Securities segment went from 68.3% to 78.7% of total assets (segment tables). That is
  the condition the exclusion row names: "with financial institutions, it’s much tougher. Then you add — throw in
  derivatives on top of it [...] no one probably knows [...] the exact condition of some of the biggest, you know, banks
  in the world." **[M2005-068]**; "the only thing we understand is that we don't understand how much risk the institution
  is running." **[L2002-018]**.
- **The filing itself calls the book unpredictable.** Item 1A: the firm's risk methods "may not predict future risk
  exposures, which could be significantly greater than the historical measures indicate"; the techniques "cannot
  anticipate every economic and financial outcome or the timing of such outcomes"; and the VaR model's inputs "may not be
  accurate predictors of future market conditions" (10-K, Item 1A and the market-risk section). The framework's rule asks
  for exactly this fact: a book "that its own filing calls unpredictable".
- **The earnings of the part that matters swing.** Institutional Securities pre-tax income of $4,476M (2023), $8,749M
  (2024), $11,237M (2025): from 37.9% to 51.2% of the firm's pre-tax income in two years (10-K segment note). Test 3, "do I
  understand enough about this business so that the financial statements will tell me [...] what the future financial
  statements are going to look like" **[M2008-033]**, is answered no for this half: three years of segment results that
  differ by 2.5 times say what a run of markets paid, not what the next ten years will.
- **The gearing.** Assets of 14.4 times shareholders' equity at 2026-06-30 (12.7 at year-end), against a reported ROTCE of
  26.6% for the quarter (EX-99.1, `0000895421-26-000207`). The rows read such a return "dealing in what is basically a
  commodity — money" for how much "is because the banks are geared up more" **[M2007-013]**. That cannot be split out
  from the outside when the gearing sits in a dealer book whose risk the filer says its own models may understate.

**The holding-company reading** (CONVENTION, framework Q1 and VI: a holding company is understood by its parts; a part
that cannot be, and that matters, keeps the whole outside). Wealth Management (FY2025 pre-tax $9,293M; 10-K segment note)
and Investment Management ($1,478M) are fee and spread businesses that might be read; that question is not reached. The
part that cannot be read, Institutional Securities, earned 51.2% of FY2025 pre-tax and holds 78.7% of the assets. It
matters, so the whole stays outside: "if you have doubts about something being into your circle of competence, it isn’t."
**[M2002-092]**. Understanding each line of business is not understanding the enterprise: "even though I could
understand every individual transaction they did, I don’t regard the whole enterprise, or the operation of it,
necessarily as being within my circle of competence." **[M2002-094]**.

**Contrary evidence weighed, not dismissed.** The Level 3 share is small (about 1.5% of fair-value assets) and VaR had no
95% exceedance in 2025 (Step 0, items 2 and 3). Both are the firm's own measurements of the book by the methods the same
filing says "may not predict future risk exposures". They describe a year in which "There were six trading loss days";
they do not read the book in the year the rows are about, and Buffett's own derivatives book "cost us about $400 million to
find out, but — and that was in a benign market. But nobody can." **[M2013-089]**.

**Which cause** (section I, the two causes; CONVENTION, the labels). Test 5 asks whether the insiders would write the
forecast down **[M2000-105]**. Here they have already answered in the filing: the firm's own risk-factor text declines to
say its methods can foresee its exposures. The rows say study does not cure this case: "Charlie and I could’ve spent 24
hours a day, and had the help of 10 or 20 math Ph.Ds. and we still wouldn’t have known what was going on" **[M2013-089]**;
"in other cases the nature of the industry would be the roadblock" **[L1993-023]**. The deciding question (the condition
of a $1.7 trillion dealer balance sheet ten years out) is "important but unknowable" **[M2006-076]**, so this is NATURE,
not WORK: no research pass is opened, and a lower price does not reopen it **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE).** A readable, cheap deposit base from wealth clients **[M2002-022]**, **[M2012-012]**
  does not make readable a dealer and derivatives book that carries most of the assets and half the pre-tax income and
  that the firm's own 10-K says its models "may not predict" **[M2005-068]**, **[M2002-094]**, **[L2002-018]**. The file
  closes here **[M2006-013]**. "It doesn’t mean it isn’t a good buy. [...] It just means that we don’t know how to
  evaluate it." **[M2000-038]**.
- **Reversal condition (one line):** price does not reopen it; only a change in the business would, namely the dealer and
  derivatives book shrinking until it no longer matters to the earnings, leaving a firm whose both sides can be read
  from its filings **[M2002-022]**.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (Q1 closed TOO HARD). No competitor row was built.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. (The balance-sheet facts above were read for Q1, not as a Q4 clearance.)

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. The proxy was fetched and not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range, no fair or cheap price is computed.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED. (Q9 test 10 points back to Q1 for a financial institution; the case was decided there.)

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: a bank holding company whose readable wealth-client deposit half funds under a
third of its liabilities, and whose dealer and derivatives half (78.7% of assets at 2026-06-30, 51.2% of FY2025 pre-tax
income, $19.4 trillion gross notional) its own 10-K says its risk models "may not predict" **[M2005-068]**,
**[M2002-094]**, **[M2006-013]**. Q7 not reached; no range. Price $190.19 (aggregator, 2026-10-05) against no value
judgment. A lower price does not reopen it **[M2000-038]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Step 0 to the standing rule committed as `107cfab`; Q1 and the close committed after it.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before writing); every filing fact has its
      accession; no number without a filing (the ratios are in `arithmetic.py` from filed figures).
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy: no owner-cash figure was built (Q1 closed; `tools/run.py`
      produced none); the sovereign from the issuing authority (US Treasury); the aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Step 0, seven items, both directions).
- [x] No row dated after the anchor is cited in a point-in-time run (this is a live run dated today; not applicable).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): it printed none.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The bank rule closes TOO HARD a bank whose wholesale or derivatives book "its own filing calls
unpredictable", but every large dealer's 10-K carries boilerplate risk-factor language of this kind ("may not predict
future risk exposures"), so the test as worded is met by the filing genre rather than by a finding about this book; the
run leaned on it together with the size facts (assets mostly the dealer segment, notionals at about 167 times equity,
deposits under a third of liabilities) rather than on the boilerplate alone, and the framework does not say whether the
risk-factor text by itself suffices. (2) The framework gives no test for how much of a holding company "matters" under the
by-parts CONVENTION; I used the segment's share of pre-tax income and of assets, which is my choice, not a row's. (3) The
choice between TOO HARD (WORK) and (NATURE) for a large bank is not fixed: test 5 (would the insiders write it down) was
read off the filer's own risk factors, which is an inference from a legal document, not an insider declining to forecast.
**Tool defect:** `python tools/run.py MS` exits 1 with "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." and prints
no price, shares or balance-sheet table at all, so for a bank holding company the tool supplies none of its arithmetic
lines; the price was taken from `tools/sources.price` directly. Also, `tools/sources.sec_facts` raised an HTTP error (EDGAR
rate limiting during parallel runs) with no retry; the XBRL cross-check was fetched with backoff by the research folder's
`fetch.py` instead.
