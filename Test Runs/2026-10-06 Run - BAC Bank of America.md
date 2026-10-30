# Company Run — Bank of America Corporation (NYSE: BAC) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Blind analyst run
of record. Research folder: `Test Runs/_research 2026-10-06 BAC/` (tool outputs, the XBRL transcription script and its
output, the id check; raw filings under its `cache/`, gitignored). The template was copied to this file before any fetch,
and the file is written and committed question by question.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open `PORTFOLIO.md`,
any earlier BAC run or research folder, any holding review, the session-state files, the queue register, the reading list
or `tools/alerts.json`.
**Contamination, declared:** (1) My training memory holds that Berkshire Hathaway has owned a large stake in Bank of
America since 2011. That is a prior of authority, and the v5 rows forbid outsourcing the decision: "we don’t believe in
outsourcing investment decisions" **[M2009-011]**; decisions are not made "based on what other people think"
**[M1994-014]**. I treat it as the bias to watch, not as evidence. (2) A grep of `principle_ledger_v5.csv` for the
company's name returned **[M2012-012]**, which names Bank of America for the soundness of its deposit funding. That row is
part of the governing evidence base, and the framework itself cites it in the bank door, so it is used, and written down
under contrary evidence. (3) The repository's recent commit subjects, shown to me at start-up, do not name BAC.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $54.00 (regular-market price, 2026-10-05, Yahoo Finance chart endpoint through `tools/sources.py`
  `price()`; **aggregator, flagged** per operator rule 5; used as a live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock, $0.01 par, **6,992,748,365** shares (Form
  10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession `0000070858-26-000394`;
  `python Screens/cover_shares.py BAC`, output in the research folder). Preferred stock is outstanding as well
  ($25,992M carrying value at 2025-12-31, 10-K balance sheet); it is a senior claim, not a common class, and is not added
  to the share count.
- **Market cap:** about $377,608M (6,992,748,365 × $54.00), common only.
- **Sovereign for the earnings currency (USD):** 5.66%, the US Treasury daily par yield curve, 30-year, dated
  2026-10-05 (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 0000070858:
  - Form 10-K for FY2025, filed 2026-02-25, accession `0000070858-26-000157` (Item 1A risk factors, MD&A segment
    results and deposit statistics, market-risk and VaR section, the consolidated balance sheet, Note 3 Derivatives, the
    fair-value hierarchy, Note 12 litigation).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession `0000070858-26-000394`.
  - DEF 14A, filed 2026-03-23, accession `0001193125-26-118929` (downloaded; read only if Q5 is reached).
  - Form 8-K, Items 2.02/7.01/9.01, filed 2026-07-14, accession `0000070858-26-000353`, EX-99.1 (the 2Q26 earnings
    release) read for its habits of presentation.
- **One figure cross-checked against the filed statement:** total deposits at 2025-12-31, **$2,018,729M** on the
  Consolidated Balance Sheet of the 10-K, against $2,018.729B in the XBRL `Deposits` fact of the same accession
  `0000070858-26-000157`. They agree.
- **`tools/run.py BAC`:** it returned "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." and printed nothing else
  (output saved). No arithmetic line came from it; the tool's cash-flow construction does not apply to a bank in any case.
  Price, shares and sovereign above come from `tools/sources.py` and `Screens/cover_shares.py`; the ten-year balance-sheet
  figures used below come from the SEC XBRL company facts, transcribed by `xbrl_tables.py` in the research folder.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this bank will be in ten years, not what the quote does. The
market serves and does not instruct **[M2006-077]**: a price of about 1.25 times book equity tells nothing about value
by itself. Who is paid to tell you **[M2020-037]**: the earnings release and the 10-K's segment tables are management's
presentation and are read as such. The analyst's habits: the worst anchor "is always your previous conclusion"
**[M2016-054]**, and here the anchor to resist is a borrowed one, the famous holder named under contamination above.

**Contrary evidence, written down as found** **[M1997-127]**, in the order the filings gave it:
1. The deposit side is plainly strong: deposits of $2,018,729M at 2025-12-31, 59% of total assets; 26% noninterest
   bearing; consumer banking paid 55 bps on its deposits in 4Q25; "approximately 70 percent of consumer and small business
   deposits [...] were held by clients who have had accounts with us for 10 or more years" (10-K, liquidity section). The
   v5 ledger names this very bank for it: "If you look at the Bank of America or Wells Fargo, they get an enormous amount
   of money from a natural customer base." **[M2012-012]**.
2. The trading book's recorded valuation is mostly observable: recurring Level 3 assets were 0.29% of total assets at
   2025-12-31 (10-K, fair-value note); there were no days in 2025 on which the backtested trading-revenue subset lost more
   than the one-day VaR; gross derivative assets of $292.2B net to $40.9B after master netting ($224.1B) and cash
   collateral ($27.2B).
3. Against reading the asset side as "very little risk": held-to-maturity debt securities carried at $522,685M had a fair
   value of $442,430M at 2025-12-31, an unrealized loss of $80,257M, about 26% of total shareholders' equity of
   $303,243M (10-K, Note 4 table and balance sheet).
4. Against reading the whole: the Global Markets segment held $1,032,858M of year-end assets (30% of the total) with
   $40,614M of deposits; the firm's derivatives carry a contract/notional amount of about $42.4 trillion (my sum of the
   Note 3 table); and the 10-K says of its own risk models "Our models may not be sufficiently predictive of future
   results" (Item 1A).
5. The rows themselves pull the other way on the gamier half: "the gamier it gets and the more it looks like investment
   banking, the less I like it" **[M2023-055]**; "you don’t know what has happened to the stickiness of deposits at all.
   [...] we’re very cautious in a situation like that about ownership of banks." **[M2023-054]**.
6. Conduct: the 10-K records a consent order on BSA/anti-money-laundering and sanctions compliance programmes and orders
   or settlements on sweep-account rates, card sales practices, representment fees and pandemic benefit processing
   (Item 1A, accession `0000070858-26-000157`).

## THE STANDING RULE
Owning a common share bought with cash puts the buyer at risk of losing what is paid and nothing more; no borrowing, no
collateral, no option given is involved **[M2012-081]**, **[L2023-005]**. The rule is engaged only if the buyer financed
or sized the purchase so that its total loss mattered; borrowing is the road the rows name to the zero **[M2004-065]**.
Not engaged by a cash purchase.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it for a bank.** "A bank is inside the circle when both sides of its balance sheet can
be read from its filings, the little-risk asset side and the cheap deposit side **[M2002-022]**, and outside it when the
asset side cannot **[M2005-068]**." And, settled at the correction pass: "A bank that has both a readable deposit base and
a wholesale or derivatives book that its own filing calls unpredictable closes TOO HARD: the readable half does not make
the unreadable half readable **[M2002-094]**." Size alone decides nothing either way **[M2005-068]**, **[M2012-012]**.
Bank of America reports four segments and an "All Other"; the balance sheet is read by the halves the filing itself
draws.

**The balance sheet, 2025-12-31 and 2026-06-30** (10-K accession `0000070858-26-000157`; 10-Q accession
`0000070858-26-000394`; $M):

| | 2025-12-31 | 2026-06-30 |
|---|---|---|
| Total assets | 3,411,738 | 3,499,191 |
| Total deposits | 2,018,729 (59% of assets) | 2,025,124 |
| Loans and leases, net of allowance | 1,172,497 | |
| Debt securities, of which held to maturity at amortized cost | 925,635, of which 522,685 | HTM 505,828 |
| Unrealized loss on held-to-maturity securities | (80,257) | (82,095) |
| Trading account assets | 366,954 | |
| Fed funds sold, securities borrowed or purchased under resale agreements | 316,578 | |
| Fed funds purchased, securities loaned or sold under repurchase agreements (liability) | 344,716 | |
| Long-term debt | 317,816 | |
| Total shareholders' equity (of which preferred) | 303,243 (25,992) | 301,094 |
| Global Markets segment: year-end assets / deposits | 1,032,858 / 40,614 | 1,106,999 / 38,146 |

**1. The deposit side: readable, and cheap.** Consumer Banking held $956,265M of deposits at year-end 2025 and paid 55
bps on them in 4Q25; 26% of all deposits bear no interest; about 70% of consumer and small-business deposits belong to
clients of ten years or more (10-K, liquidity section). Across all deposits the bank paid $34,513M of interest on
average deposits of $1,984,182M in 2025, about 1.74%, while the cash it placed at the Federal Reserve and other banks
earned 4.03% (10-K, average-balance table). That is "very cheap money on the deposit side" **[M2002-022]**, from "a
natural customer base" **[M2012-012]**; the ledger names this bank for it **[M2012-012]**. This half passes the door. One
caution the rows carry: after 2023 "you don’t know what has happened to the stickiness of deposits at all"
**[M2023-054]**; uninsured deposits were $723.0B (U.S.) and $134.9B (non-U.S.) at year-end 2025 (10-K, liquidity section, "Uninsured Deposits").
I record it and do not let it decide.

**2. The consumer and commercial lending book: readable.** Loans of $1,185,700M against an allowance of $13,203M; the
Consumer Banking segment's provision was $4,649M on average loans of $319,312M in 2025. A reader can say what the card,
mortgage, auto and commercial books are and roughly what they lose. The rows' danger, "It’s always on the asset side"
**[M2011-022]**, is visible here in a different place: the bank put deposits into long fixed-rate securities, and the
held-to-maturity book stood at an unrealized loss of $80,257M at year-end 2025 and $82,095M at 2026-06-30, about 27% of
shareholders' equity. That loss is disclosed and readable; it is a choice the filings let me see, not a fog. It bears on
"very little risk on the asset side" **[M2002-022]** and would be weighed at Q9 if Q1 passed.

**3. The Global Markets half: the filing itself says it cannot be read in advance.** This is the deciding finding.
- **Its size.** Global Markets held $1,032,858M of assets at year-end 2025 (30% of the corporation) and $1,106,999M at
  2026-06-30 (32%), with only $40,614M and $38,146M of deposits: it is funded on the wholesale side, through repurchase
  agreements ($344,716M), short-term borrowings ($48,088M), trading liabilities ($105,996M) and long-term debt. Its
  trading-related assets were $670,949M at year-end and $733,711M at June 30, 2026. It earned $6,111M of the
  corporation's $30,509M net income in 2025 (20%).
- **The derivatives "on top of it" [M2005-068].** Note 3 lists derivative contracts with a contract/notional amount that
  sums to about $42.4 trillion at 2025-12-31 (interest rate $29.6T, foreign exchange $8.7T, equity $2.6T, commodity $0.4T,
  credit $1.1T; my sum of the filed table), about 140 times shareholders' equity. Gross derivative assets of $292.2B and
  liabilities of $297.6B become $40.9B and $42.1B only after $224.1B of master netting and cash collateral. Netting is a
  legal claim on counterparties under enforceable agreements; whether it holds in a crisis is a fact about the
  counterparties and the courts, not about the filing.
- **What the bank says of its own measures.** Item 1A: "Our models may not be sufficiently predictive of future results,
  including from limited historical patterns, extreme or unanticipated market movements or clients’ behavior and
  liquidity, especially during severe market downturns or stress events"; "In times of market stress or other unforeseen
  circumstances, previously uncorrelated indicators may become correlated. Such changes to the relationship between market
  parameters may limit the effectiveness of our hedging strategies and cause us to incur significant losses"; and "we are
  inherently limited by our ability to identify and measure all risks, including emerging and unknown risks". The VaR
  section: "Within any VaR model, there are significant and numerous assumptions that will differ from company to
  company", and "VaR may not be indicative of realized revenue volatility". These are boilerplate in every large bank's
  10-K; that does not make them untrue, and the settled rule asks exactly whether the filing calls its book unpredictable.
  It does, of the book that is 30% of the assets.
- **What the outside reader can see** is a one-day 99% VaR of the trading positions averaging $72M in 2025 (Table 42), an
  absence of backtesting breaches in 2025, and Level 3 assets of 0.29% of total assets. These say the book was valued from
  observable prices and was calm last year. They do not say what it loses when correlations change, which is the bank's
  own warning. "with financial institutions, it’s much tougher. Then you add — throw in derivatives on top of it, and,
  you know, it’s — no one probably knows, you know, perfectly, what some of the — or even within a reasonable range — the
  exact condition of some of the biggest, you know, banks in the world." **[M2005-068]**; "the only thing we understand is
  that we don't understand how much risk the institution is running." **[L2002-018]**; "You spot troubles in financial
  institutions late." **[M2001-066]**.
- **The rows' own view of this half.** "If you follow sound banking methods, which means not doing some things that other
  people do, a bank can be a perfectly decent investment." **[M2023-053]**; and "the gamier it gets and the more it looks
  like investment banking, the less I like it" **[M2023-055]**. Global Markets is the investment-banking half.

**4. Can the ten-year economics be foreseen?** Understanding means "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**. For the deposit franchise I think the answer is
nearly yes. For the whole, the ten-year earning power turns on two things the filings cannot fix: the loss the
Global Markets and derivatives book takes in the next severe dislocation, and the capital the regulators will require,
since "You can change the math of banking, and the attractiveness of banking, totally, by capital requirements."
**[M2016-027]**. Test 3 asks whether the past statements tell me the future ones **[M2008-033]**; for the trading half the
bank says its own history-based models may not. And the culture that would let me trust the trading half without seeing
it is the thing the row says is "hard to do for 99 percent of the banks" **[M2008-090]**; the consent order on
anti-money-laundering and sanctions programmes and the orders on sweep rates, card sales practices and representment fees
(10-K, Item 1A) do not make it easier.

**The door, applied.** Deposit side: readable and cheap, on the evidence and by name in the ledger **[M2012-012]**.
Consumer and commercial loans: readable. The Global Markets half, 30% to 32% of the assets, funded wholesale and carrying
about $42.4 trillion of derivative notional: its own filing says its models "may not be sufficiently predictive". The
settled reading governs: the readable half does not make the unreadable half readable (the framework's sentence, resting
on "even though I could understand every individual transaction they did, I don’t regard the whole enterprise, or the
operation of it, necessarily as being within my circle of competence." **[M2002-094]**), and the file
closes in the "too hard" box **[M2006-013]**. Even on a kinder reading of the boilerplate, doubt alone closes it: "if you
have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. This is no judgment that
the bank is bad or that the price is wrong: "It’s no judgment that there’s anything bad." **[M2007-052]**; "It doesn’t
mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know
how to evaluate it." **[M2000-038]**.

**Which cause: NATURE, not WORK.** The test between them is whether the insiders would write the forecast down (test 5,
**[M2000-105]**). The deciding question is the stress loss of a trillion-dollar trading and derivatives book under
correlations not yet seen. The insiders, in the one document where they must speak carefully, decline to vouch for their
own forecast of it ("may not be sufficiently predictive"; "inherently limited by our ability to identify and measure all
risks, including emerging and unknown risks"). The rows call this the industry's nature, not the reader's shortfall:
"in other cases the nature of the industry would be the roadblock." **[L1993-023]**; "It’s just the nature of the beast."
**[M2001-066]**. A research pass would list: the counterparty concentration behind the $224.1B of netting; the stress-test
loss the regulators project for the trading book; the composition of the $1.1 trillion Global Markets balance sheet by
liquidity. The first is not disclosed by name; the second is a regulator's model, which the rows would not outsource to
**[M2009-011]**; the third would describe the book and still not say what it loses when "previously uncorrelated
indicators may become correlated". Under the pass's own rule a question unanswerable from primary documents is set aside,
and a pass that ends unsure ends TOO HARD (NATURE) **[M2002-092]**. No lower price reopens the box **[M2000-038]**.

**VERDICT: TOO HARD (NATURE)** at Q1. The deposit side is readable and cheap (consumer deposits at 55 bps, 26% of all
deposits noninterest bearing; 10-K accession `0000070858-26-000157`), but the Global Markets half, $1,106,999M of assets
at 2026-06-30 (10-Q accession `0000070858-26-000394`) funded wholesale and carrying about $42.4 trillion of derivative
notional, is a book whose own filing says its models "may not be sufficiently predictive of future results".

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED.
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## EVIDENCE GATHERED BEYOND THE CLOSING STOP: NOT A CLEARANCE
*The brief asks for a competitor row, and the bank door needs a yardstick for "cheap money" and a view of the balance
sheet over time. Both were gathered while Q1 was open. They are recorded here as evidence, not as answers to Q2 or Q4,
which were not reached; nothing below carries entry language.*

**The competitor row** (FY2025, from each bank's own 10-K XBRL facts; `peer_row.py` in the research folder; ratios mine:
ROA on the average of year-end assets 2024 and 2025, cost of deposits as interest on deposits over the average of
year-end deposits, efficiency as noninterest expense over net interest income plus noninterest income):

| Company | 10-K accession | ROA | Cost of deposits | Efficiency | Equity / assets | Deposits / assets | Net income ($B) |
|---|---|---|---|---|---|---|---|
| Bank of America (BAC) | `0000070858-26-000157` | 0.91% | 1.73% | 61.7% | 8.9% | 59.2% | 30.5 |
| JPMorgan Chase (JPM) | `0001628280-26-008131` | 1.35% | 1.82% | 52.4% | 8.2% | 57.8% | 57.0 |
| Wells Fargo (WFC) | `0000072971-26-000133` | 1.05% | 1.46% | 65.5% | 8.4% | 66.4% | 21.3 |
| Citigroup (C) | `0000831001-26-000011` | 0.57% | 2.60% | 64.7% | 8.0% | 52.8% | 14.3 |

What the row shows for the door: BAC's money is about as cheap as the cheapest of the four large peers' (Wells Fargo's
is cheaper, Citigroup's much dearer), and its return on assets sits between Wells Fargo's and Citigroup's, below
JPMorgan's. All four run at eight to nine dollars of equity per hundred of assets, and all four carry large trading and
derivatives books; the row does not distinguish BAC from its peers on the Q1 ground, it places the whole group in the
same "biggest, you know, banks in the world" **[M2005-068]**. Equity / assets uses total shareholders' equity, preferred
included.

**The balance sheets, 2016 to 2025** **[M2025-032]** (SEC XBRL facts of BAC's 10-Ks, latest-filed value for each year;
`xbrl_tables.py`; $B; the 2020 loans line is not tagged under the tags the script reads and is left blank):

| Year-end | Assets | Deposits | Net loans | Trading assets | Goodwill | Equity (incl. preferred) | Long-term debt | Retained earnings | Net income | Interest on deposits |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 2,188.1 | 1,260.9 | 895.4 | 180.2 | 69.0 | 266.2 | 216.8 | 101.2 | 17.8 | 1.0 |
| 2017 | 2,281.2 | 1,309.5 | 926.4 | 209.4 | 69.0 | 267.1 | 227.4 | 113.8 | 18.2 | 1.9 |
| 2018 | 2,354.5 | 1,381.5 | 937.3 | 214.3 | 69.0 | 265.3 | 229.4 | 136.3 | 28.1 | 4.5 |
| 2019 | 2,434.1 | 1,434.8 | 974.0 | 229.8 | 69.0 | 264.8 | 240.9 | 156.3 | 27.4 | 7.2 |
| 2020 | 2,819.6 | 1,795.5 | | 198.9 | 69.0 | 272.9 | 262.9 | 164.1 | 17.9 | 1.9 |
| 2021 | 3,169.5 | 2,064.4 | 966.7 | 247.1 | 69.0 | 270.1 | 280.1 | 188.1 | 32.0 | 0.5 |
| 2022 | 3,051.4 | 1,930.3 | 1,033.1 | 296.1 | 69.0 | 273.2 | 276.0 | 207.0 | 27.5 | 4.7 |
| 2023 | 3,180.2 | 1,923.8 | 1,040.4 | 277.4 | 69.0 | 290.2 | 302.2 | 224.7 | 26.3 | 26.2 |
| 2024 | 3,261.3 | 1,965.5 | 1,082.6 | 314.5 | 69.0 | 294.0 | 283.3 | 240.8 | 27.0 | 38.4 |
| 2025 | 3,411.7 | 2,018.7 | 1,172.5 | 367.0 | 69.0 | 303.2 | 317.8 | 261.7 | 30.5 | 34.5 |

What the figures say: deposits rose 60% in nine years and stayed near 59% of assets; goodwill did not move from
$69.0B, so the decade had no material acquisition; retained earnings rose by $160.5B while total equity rose by only
$37.0B, because the difference went out in dividends and repurchases (common shares issued and outstanding fell from
7,610,862,311 to 7,212,464,345 in 2025 alone, 10-K balance sheet); equity fell from 12.2% to 8.9% of assets; trading
account assets doubled, from $180.2B to $367.0B, faster than any other line. What they do not say: the HTM loss of
$80.3B is not in the equity line (held-to-maturity securities are carried at cost), and the derivative notional is not on
the balance sheet at all. **What they cannot say:** what the trading and derivatives book loses in the next dislocation.
That is the Q1 finding.

**The earnings release** (EX-99.1, accession `0000070858-26-000353`), read for habits only: segment highlights and
league-table claims ("#1 in U.S. Consumer Deposits"); the 10-K itself labels its excluding-DVA figures "a non-GAAP
financial measure". Not weighed: Q4 was not reached.

**COMPUTATION — NOT A CLEARANCE.** At $54.00 the common market capitalisation of about $377,608M is about 1.25 times total
shareholders' equity of $301,094M at 2026-06-30 (preferred included), and about 12.4 times 2025 net income of $30,509M
before preferred dividends. Recorded as arithmetic only; Q7 was not reached and no value is stated.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. Both sides of the commercial bank can be read: the deposits are cheap and from
a natural customer base (consumer deposits at 55 bps in 4Q25; 26% noninterest bearing), and the ledger names this bank for
it **[M2012-012]**. The Global Markets half cannot: $1,106,999M of assets at 2026-06-30, 32% of the corporation, funded
wholesale, with about $42.4 trillion of derivative notional, and a 10-K that says of its own risk models "Our models may
not be sufficiently predictive of future results". Under the bank door as settled, the readable half does not make the
unreadable half readable **[M2002-094]**, **[M2005-068]**. The cause is NATURE: the insiders decline to vouch for the
forecast that decides it **[M2000-105]**, **[L1993-023]**; no research pass is opened and no lower price reopens the box
**[M2000-038]**. Q7 not reached; no range is stated.

**Reversal condition, in one line:** the box would reopen only if the trading and derivatives book ceased to be a material
part of the bank (for example, a separation of Global Markets that left a deposit-funded lender whose asset side could be
read whole from its filing), since that, and not price or more reading, is what the door turns on.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (commits `d875806`
      for step 0 to the standing rule, `2b18f31` for Q1, and the closing commit for the rest).
- [x] Every v5 id resolves (`check_ids.py` in the research folder: all cited ids present in `principle_ledger_v5.csv`, no
      v4 ids, every quoted fragment set before an id found in that row's text); every filing fact has its accession; no
      number without a filing or a stated computation.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance, and the evidence beyond the stop is headed
      as such.
- [x] Owner cash after every real cost, never a net-income proxy: not computed, because Q4 and Q7 were not reached; the
      only earnings figures written are filed net income, labelled as such, in the NOT A CLEARANCE section. The sovereign
      is from the Treasury, dated; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items under the foundations, the first two
      of them for the name).
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): it printed none for this name.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **"Its own filing calls unpredictable" has no threshold for boilerplate.** The settled bank-door sentence
closes a bank whose wholesale or derivatives book "its own filing calls unpredictable". Every large U.S. bank's Item 1A
carries model-risk language ("may not be sufficiently predictive"), so read literally the sentence closes every money-centre
bank by its risk factors alone, and read loosely it closes none. I applied it with the size of the book (30% to 32% of
assets, about $42.4 trillion of notional, funded wholesale) beside the words, and with the doubt row **[M2002-092]** as the
floor; the framework should say whether the words, the size, or both decide. (2) **The door has no rule for a
readable but loss-carrying asset choice.** The held-to-maturity book's $80.3B to $82.1B unrealized loss (about 27% of
equity) is fully disclosed, so it is "readable", but it is not "very little risk on the asset side" **[M2002-022]**. The
door treats readability and low risk as one test; here they part, and I recorded the loss without letting it decide.
(3) **The research pass for NATURE versus WORK leans on insiders writing a forecast down** **[M2000-105]**, but banks are
required to file risk factors that disclaim their own models; whether a mandated disclaimer is the insiders "not
writing it down" is my reading, not a rule. (4) **`tools/run.py` returns UNRESEARCHED for a bank** ("no overlapping
OCF/D&A/capex annual facts") and gives no price, shares or sovereign line, so a bank run gets nothing from it; and there is
still no stated owner-cash method for a bank at Q4 and Q7 (the sector method covers insurers and float companies only).
Had the run reached Q4, I would have had to invent one and confess it.
