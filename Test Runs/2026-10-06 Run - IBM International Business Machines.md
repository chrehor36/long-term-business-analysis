# Company Run — International Business Machines Corporation (NYSE: IBM) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. The dispatch forbade
opening `PORTFOLIO.md`, any holding review, the session-state files, the register, the prepped reading list and
`tools/alerts.json`, and none was opened. Whether the operator holds or wants this name is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The session opened with the repository's recent commit subjects in view; they name
batches of other v5 runs (small-cap and S&P 600 screens), not IBM. (2) One other company's v5 run of 2026-10-05
(`Test Runs/2026-10-05 Run - EXTR Extreme Networks.md`) was read for form only. No earlier file about IBM, in `Test Runs/`,
`Framework/v4/` or `Framework/v5/tests/`, was opened. (3) **The corpus itself speaks of this company.** A search of
`principle_ledger_v5.csv` for "IBM" returns rows in which Buffett and Munger discuss their own purchase of IBM (2011) and
its outcome (2017). These are v5 rows, admissible by PRIME RULE 4 and the scope directive, and they are used below as
evidence, not avoided; they are also a prior of exactly the kind the dispatch warns of, and they are weighed against the
filings, not in place of them. (4) Training memory: I knew before reading that IBM spun off Kyndryl, bought Red Hat and
that Berkshire held and sold IBM. Every fact below is from the filings or the ledger, not from that memory.

Working folder: `Test Runs/_research 2026-10-06 IBM/` (`run_py_output.txt`, `cover_shares.txt`, `sovereign.txt`,
`ibm_xbrl_annual.txt`, `computation.py` and `computation.txt`; raw filings under `cache/`, gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $221.58 (2026-10-05 quote through `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, 942,134,390 shares outstanding at
  2026-06-30 (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession `0000051143-26-000078`;
  `python Screens/cover_shares.py IBM`; the 10-Q cover reads "The registrant had 942,134,390 shares of common stock
  outstanding at June 30, 2026."). No other class is on the cover.
- **Market cap:** about $208,758M (942.13M x $221.58).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K for FY2025, filed 2026-02-24, accession `0000051143-26-000010`: the
  main document (Item 1 business and competition, Item 1A risk factors) and the integrated annual report filed with it
  (`ibm-20251231_d2.htm`: management discussion, segment details, the consolidated statements and notes). Form 10-K for
  FY2023 (`0000051143-24-000012`), its cash-flow statement only, for FY2021 and FY2022. Form 10-Q for the quarter ended
  2026-06-30 (`0000051143-26-000078`): cover, the Confluent acquisition note, the condensed statements. DEF 14A filed
  2026-03-10 (`0000051143-26-000025`), fetched; not read past the point the file closed (Q5 and Q6 not reached). 8-K of
  2026-07-14 (`0000051143-26-000070`), EX-99.1, the chief executive's letter on preliminary second-quarter results;
  8-K of 2026-07-22 (`0000051143-26-000077`), EX-99.1, the second-quarter release; 8-K of 2026-10-01
  (`0000051143-26-000086`), a director elected.
- **One figure cross-checked against the filed statement:** the FY2025 consolidated statement of cash flows
  (`0000051143-26-000010`, page 45) shows net cash provided by operating activities $13,193M, $13,445M and $13,931M for
  2025, 2024 and 2023, and stock-based compensation $1,715M, $1,311M and $1,133M; the tool's OCF and SBC columns equal
  them. One tool omission is recorded: the tool's capex column carries "Payments for property, plant and equipment" only;
  the filed statement also deducts "Investment in software" ($647M, $637M, $565M), which the tool prints separately as an
  "other capital payment" and leaves unchosen. Both are capital spending and both are deducted below.
- `python tools/run.py IBM`, arithmetic lines only (Part VII): OCF less stock pay less property capex FY2023 $11,553M,
  FY2024 $11,086M, FY2025 $10,387M; with investment in software also deducted, $10,913M, $10,260M, $9,460M. Its yield,
  "growth the price assumes" and "points over the sovereign" lines are v4 material and are not read as rules. Stock pay is
  resolved and complete in the filed cash-flow statement for every year used.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**, which
here means owning a company that in its latest five years produced $7.5B to $11.0B a year of owner cash (computation
block) on a $208.8B price. No macro forecast enters: "macro conclusions are — just never enter into the discussion." **[M2000-094]**. Who is paid to tell you bears on this
name: the filer's case for its future is made in its own words ("AI is changing the economics of enterprise
operations", annual report MD&A, `0000051143-26-000010`), and the speakers decided nothing on projections: "we’ve never
looked at a projection in connection with either a security we’ve bought or a business we’ve bought" **[M1995-050]**;
"don’t ask the barber whether you need a haircut" **[M2011-083]**. The analyst's habits: look for "what you’re
missing" **[M2025-013]**; state the other side's case better than its holder **[M2016-055]** (done at Q1); and the
worst anchor "is always your previous conclusion" **[M2016-054]**, which here includes the speakers' own 2011
conclusion about this company.

**Contrary evidence, written down as found** **[M1997-127]**: (a) gross margin rose from 49.8% in FY2015 ($40,684M on
$81,741M) to 58.2% in FY2025 ($39,297M on $67,535M) (XBRL, `0001047469-16-010329` and `0000051143-26-000010`);
(b) owner cash after stock pay and all capital spending was positive in every year FY2021 to FY2025, between 12.4% and
17.8% of revenue (computation block); (c) Software, $29,962M of FY2025 revenue, carries an 83.5% gross margin and a
33.1% segment profit margin (annual report, segment details); (d) the z17 mainframe, launched June 2025, lifted IBM Z
revenue 51.7% in FY2025, and in the July 2026 letter "z17 remains at nearly 130 percent program-to-program [...] with
clients representing 85% of installed MIPs maintaining or growing capacity" (8-K EX-99.1, `0000051143-26-000070`);
(e) the speakers' own row says "The chances of being way wrong in IBM are probably less, at least for us, than being way
wrong with Google or Apple." **[M2012-073]**; (f) Buffett named IBM with Coca-Cola and See's as businesses meeting the
"double-barreled test" of keeping purchasing power "while requiring a minimum of new capital investment" **[L2011-019]**.
Each is weighed at Q1.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase would be made without borrowed money and at a size that cannot
threaten the buyer, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**. Nothing in this name forces a breach; the file closes before
sizing arises.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position
will look like in five or 10 years. So I’ve got some notion of how the industry will develop and where the company will
stand within the industry." **[M2012-065]**; its failing form is "we understand the product [...] We just don’t know
the economics of it 10 years from now." **[M2000-104]**. The products are plain enough from the filing. FY2025 revenue
$67,535M (annual report, revenue by major products, `0000051143-26-000010`):
- **Software $29,962M**: Hybrid Cloud (Red Hat) $7,327M, Automation $7,733M, Data $6,299M, Transaction Processing
  $8,603M (the software stack that runs on the mainframe).
- **Consulting $21,055M**: Strategy and Technology $11,537M, Intelligent Operations $9,518M.
- **Infrastructure $15,718M**: Hybrid Infrastructure $10,618M (IBM Z, Power, storage), Infrastructure Support $5,100M.
- **Financing $737M.**

**The key variables** **[M1998-044]**, and how predictable each is in the filer's own words:
1. **The mainframe franchise and the software that rides on it** (Transaction Processing plus most of Hybrid
   Infrastructure, under a third of revenue). Its cycle is visible: IBM Z revenue up 51.7% in the z17 launch year, then a
   second-quarter 2026 shortfall "driven by a shortfall in our Z performance and the associated software stack,
   primarily in Transaction Processing", with "numerous large deals" failing to close (8-K EX-99.1,
   `0000051143-26-000070`). The installed base is the most foreseeable part of IBM.
2. **Red Hat and the hybrid-cloud software against the hyperscalers.** The filer names its principal software
   competitors as "Alphabet (Google), Amazon, BMC, Broadcom, Microsoft, Oracle, Salesforce, SAP and Splunk, a CISCO
   Company", and in infrastructure "cloud service providers are leveraging innovation in technology and service delivery
   to compete with traditional providers" (10-K Item 1, `0000051143-26-000010`).
3. **Consulting against Accenture, Capgemini and "India-based service providers"** (Item 1), in a business whose work
   the filer itself says AI is changing: "AI is changing the economics of enterprise operations" and clients "must
   become AI-first" (annual report MD&A).
4. **The bets that will make the 2036 company.** "IBM has moved into areas, including those that incorporate or utilize
   hybrid cloud, AI, quantum and other disruptive technologies [...] If IBM is unable to continue its cutting-edge
   innovation in a highly competitive and rapidly evolving environment [...] the company could fail in its ongoing
   efforts to maintain and increase its market share and its profit margins." (Item 1A.) In July 2026: "we disclosed
   plans to invest more than $10 billion in quantum over the next five years"; a "$5 billion commitment" (Lightwell)
   launched after "the introduction of Mythos"; "quantum computing is no longer decades away, it is upon us"
   (8-K EX-99.1, `0000051143-26-000070`).
5. **What the company buys.** Acquisitions, net of cash acquired, were $3,293M, $2,348M, $5,082M, $3,289M and $8,294M in
   FY2021 to FY2025 (filed cash-flow statements, `0000051143-24-000012` and `0000051143-26-000010`), $32,630M in FY2019
   (Red Hat; XBRL, `0001558370-20-001334`), and $10,480M in the first half of 2026, chiefly Confluent at "a total equity
   value of approximately $11.3 billion" (10-Q, `0000051143-26-000078`). The IBM of ten years hence will be in part
   whatever is bought between now and then.

The filer's verdict on its own predictability: "certain of the company’s growth areas involve new products, new
customers, new and evolving competitors, and new markets, all of which contribute to the difficulty of predicting the
company’s financial results"; "as we execute our hybrid cloud and AI strategy, we are regularly exposed to new
competitors" (10-K Items 1A and 1).

**The rows.** "a business that must deal with fast-moving technology is not going to lend itself to reliable
evaluations of its long-term economics" **[L1993-023]**; "if something comes in where there’s a technological component
that’s of significance [...] it won’t make it through the filter" **[M1998-008]**; "whenever we look at a business and
we see lots of change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**. Test 6, the winner not
the industry: "there’s industries we know that may have a wonderful future, but we don’t have the faintest idea who the
winners will be" **[M2012-067]**; seeing growth in AI and hybrid cloud "does not mean we can judge what its profit
margins and returns on capital will be as a host of competitors battle for supremacy" **[L2009-005]**. Test 7, is the
forecast about customers or about technology: the speakers drew this exact line with this company as the example,
"in terms of laying out what their prospective customers will do in the future, as opposed to, say, IBM’s customers,
it’s a different sort of analysis" **[M2017-019]**, putting IBM on the technology side of it. Munger, on a leader that
must carry its position into new fields, with this company's own history as the example: "just as IBM leveraged the
Hollerith machine into the computer. Predicting whether somebody’s going to be able to do that in advance is just —
it’s too tough for us." **[M1997-022]**. And leadership is not durability: "Witness the shocks some years back at
General Motors, IBM and Sears" **[L1996-031]**.

**The speakers' own ten-year test of this company.** No other evidence on the shelf bears so directly. Buffett had read
the reports for half a century before buying: "I have been reading the company's annual report for more than 50 years"
**[L2011-010]**. In 2013, owning a very large position, he graded his own understanding: "I would say that I do not
understand the moat around an IBM as well as I understand the mode around a Coca-Cola. [...] I could think of some
things that could go wrong with IBM." **[M2013-074]** (the transcript's "mode" kept as printed). In 2017 he graded the
outcome: "I was wrong on the first one" **[M2017-019]**, the first being IBM, and counted it among his mistakes in
marketable securities **[M2017-079]**. This is Q1's test 10 run by the authors of the test: "what would bother me is if
I think I understand a business and I don’t." **[M1997-024]**.

**The other side's case**, stated as strongly as I can **[M2016-055]**. IBM is not a garage start-up; it is an
incumbent incorporated in 1911 (10-K Item 1) whose customers run their transaction systems on its machines. The mainframe outlived every
forecast of its death, and z17 sold at about 130% of the record z16 program with 85% of installed MIPS holding or
growing. Gross margin has risen nine points in ten years as the mix moved to software, owner cash after stock pay has
run $7.5B to $11.0B a year, and the speakers' own reasoning in 2012 was not that IBM would do best but that one was less
likely to be "way wrong" there **[M2012-073]**, with a "model in our mind of how far off we can be" **[M2011-084]**. On
that reading the economics are foreseeable as a slow-growing annuity with a cyclical hardware layer, which would put
the name IN at Q1 and send it to Q2 and Q7.

I do not adopt it, for three reasons from the filings and rows. First, the foreseeable layer is the smaller one: the
mainframe stack is under a third of revenue, and the remainder (Red Hat against Microsoft, Amazon and Google;
consulting against Accenture and India-based providers while the filer says AI is changing the work; the AI and
quantum bets) is where the 2036 earning power is decided; the filer calls that environment "highly competitive and
rapidly evolving" (Item 1A). Second, the company is being re-made by purchase ($8.3B in FY2025, $10.5B in the first half
of 2026, a further $10B quantum programme announced), so the forecast is of businesses not yet owned. Third, and
decisively, the other side's case is the case the speakers themselves made in 2011 to 2013, after fifty years of
reading, and they called it wrong in 2017 **[M2017-019]**, **[M2017-079]**. If the people who wrote the test could not
hold a ten-year fix on IBM with a large position and full study, a doubt remains, and "if you have doubts about something
being into your circle of competence, it isn’t." **[M2002-092]**; "it’s better to be well within the circle than to be
trying to tiptoe along the line." **[M2002-093]**. The other reading is carried into "What in the framework was wrong or
unclear".

**Which cause** (section I, the two causes). The deciding question is: what will IBM's earning power and competitive
position be in 2036, across hybrid-cloud software, AI, IT services and the mainframe, and what will the businesses it
has yet to buy add to it? The test is whether the industry's insiders would write that forecast down **[M2000-105]**:
"they would not want to put down on paper their predictions about where 10 companies you would choose in the tech field
would be in 10 years, in terms of their economics. They would say, “That’s too hard.”" The insider here writes down a
quarter's expectation and misses it ("our performance in many areas showed strength", but "this quarter we faltered",
8-K EX-99.1 of 2026-07-14) and calls its own results "difficult to predict" (Item 1A). This is the industry's cause:
"the nature of the industry would be the roadblock" **[L1993-023]**; "Our problem -- which we can't solve by studying up
-- is that we have no insights into which participants in the tech field possess a truly durable competitive advantage."
**[L1999-018]**. It is also the one case on the shelf where the work was demonstrably done, by the speakers, over
decades, and did not cure it **[L2011-010]**, **[M2017-019]**; "we’re not going to learn enough in the followings five
months to make up for the fact that we went in deficient in the first place." **[M2008-086]**. The cause is NATURE, not
WORK.

- **VERDICT: TOO HARD (NATURE)** **[M1998-008]**, **[L1993-023]**, **[M2002-092]**, **[M2017-019]**. The ten-year
  economics of a technology incumbent re-making itself in hybrid cloud, AI and quantum, against named hyperscaler and
  services competitors, cannot be foreseen from the filings, and the speakers' own attempt on this company is on the
  record as a miss. The box is "in, out, and too hard" **[M2006-013]**, and it is not a judgment of quality: "It doesn’t
  mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t
  know how to evaluate it." **[M2000-038]**. A lower price does not reopen it (section I, TOO HARD (NATURE)). **The file
  closes here.**

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**NOT REACHED.**

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.**

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance-sheet reading is done in the computation block below.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.**

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The owner's reporting request is answered below under COMPUTATION — NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.**

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this block was produced after Q1 closed the file TOO HARD (NATURE). It carries no entry language and
reopens nothing (operator rule 3). It is written because the owner asks for the value range, the fair price and the
cheap price on every run, and because the template asks for the balance sheets when the file closes before Q4. Facts
that bear on questions not reached are recorded as found, not judged.*

### The balance sheets, nine year-ends, read before the income account
Read as **[M2025-032]** asks, "balance sheets over an 8 or 10 year period before I even look at the income account"
(tool table, first-filed XBRL vintages; FY2025 and FY2024 checked against the filed balance sheet and liquidity
discussion in `0000051143-26-000010`; the accessions of the earlier vintages are listed in `run_py_output.txt`). The
tool prints FY2017 to FY2025. USD millions.

| Year-end | Total assets | Equity | Goodwill | Intangibles | Equity less goodwill and intangibles | Retained earnings | Debt (tool sum) |
|---|---|---|---|---|---|---|---|
| 2017 | 125,356 | 17,594 | 36,788 | 3,742 | -22,936 | 153,126 | 39,837 (non-current only) |
| 2018 | 123,382 | 16,796 | 36,265 | 3,087 | -22,556 | 159,206 | 45,812 |
| 2019 | 152,186 | 20,841 | 58,222 | 15,235 | -52,616 | 162,954 | 62,899 |
| 2020 | 155,971 | 20,597 | 59,617 | 13,796 | -52,816 | 162,717 | 61,538 |
| 2021 | 132,001 | 18,901 | 55,643 | 12,511 | -49,253 | 154,209 | 51,704 |
| 2022 | 127,243 | 21,944 | 55,949 | 11,184 | -45,189 | 149,825 | 50,949 |
| 2023 | 135,241 | 22,533 | 60,178 | 11,036 | -48,681 | 151,276 | 56,547 |
| 2024 | 137,175 | 27,307 | 60,706 | 10,660 | -44,059 | 151,163 | 54,973 |
| 2025 | 151,880 | 32,648 | 67,717 | 11,391 | -46,460 | 155,648 | 61,260 |

What the figures say:
- **Goodwill and intangibles have exceeded equity at every year-end shown**, by $22.6B to $52.8B. The step in 2019 is
  Red Hat (acquisitions $32,630M that year, XBRL `0001558370-20-001334`): goodwill rose $21,957M, intangibles $12,148M
  and debt $17,087M in one year. Every dollar of reported equity, and more, is purchase price paid for other companies.
- **Retained earnings are flat for nine years** ($153.1B to $155.6B) while treasury stock stands at $170,605M (FY2025
  balance sheet): the company has paid out or spent on its own shares more than it has kept, and equity is positive only
  through paid-in capital.
- **Debt rose from $45.8B (2018) to $61.3B (2025)** and to $61,987M at 2026-06-30 (10-Q `0000051143-26-000078`), while
  cash, restricted cash and marketable securities fell to $8,178M at 2026-06-30 from $14,470M at year-end, after the
  Confluent purchase. Of the FY2025 total, $15,093M is Financing segment debt carried against $1,678M of Financing equity,
  about nine to one, "primarily comprised of intercompany loans" (annual report, Financing).
- **The 2021 drop in assets is the Kyndryl separation** of 2021-11-03 (FY2023 annual report, `0000051143-24-000012`).
- **Receivables did not follow revenue down or up**: $6.5B to $8.9B in every year while revenue went from $79.6B
  (2018) to $57.4B (2021) and back to $67.5B (2025). FY2025's operating cash absorbed $4,278M of receivables "including
  financing receivables", the z17 cycle being financed for clients (cash-flow statement and MD&A).
- **The pension book is the annuity company on the side** **[M2013-075]**: benefit obligations $47,103M against plan
  assets $44,820M at 2025-12-31, net underfunded $2,283M (annual report, retirement note and liquidity discussion). The
  row's words, said of this company in 2013: "the liabilities are a lot more certain than the assets over time."
- **What they cannot say:** what the $67.7B of goodwill will earn when the businesses it was paid for meet the AI
  transition named at Q1.

### Owner cash after every real cost
Net cash from operations less stock pay less all capital spending (property, plant and equipment plus investment in
software), the costs as Q4 states them: "a figure calculated after interest, taxes, depreciation, amortization and all
forms of compensation" **[L2021-003]**; stock pay "the most egregious example" of costs owners are told to ignore
**[L2015-003]**; and software amortization "very real expenses" **[L2012-003]**. Filed cash-flow statements: FY2023 to
FY2025 in `0000051143-26-000010`, FY2021 and FY2022 in `0000051143-24-000012`. USD millions.

| FY (Dec) | OCF | Stock pay | Property capex | Investment in software | Owner cash | Owner cash / revenue | Acquisitions, net of cash | Owner cash after acquisitions |
|---|---|---|---|---|---|---|---|---|
| 2021 | 12,796 | 982 | 2,062 | 706 | 9,046 | 15.8% | 3,293 | 5,753 |
| 2022 | 10,435 | 987 | 1,346 | 626 | 7,476 | 12.4% | 2,348 | 5,128 |
| 2023 | 13,931 | 1,133 | 1,245 | 565 | 10,988 | 17.8% | 5,082 | 5,906 |
| 2024 | 13,445 | 1,311 | 1,048 | 637 | 10,449 | 16.7% | 3,289 | 7,160 |
| 2025 | 13,193 | 1,715 | 1,091 | 647 | 9,740 | 14.4% | 8,294 | 1,446 |

Five-year average **$9,540M**, about $10.13 a share; after acquisitions, $5,079M. Notes on the inputs:
- **OCF is as filed**, so it is after interest paid ($2,042M in FY2025) and after the growth of client financing
  receivables. IBM's own "free cash flow" adds the change in financing receivables back ("management considers Financing
  receivables as a profit-generating investment, not as working capital", MD&A); that add-back is not taken here,
  because the receivables are funded by the debt above and the lending is a use of the owner's cash.
- **The FY2021 column includes Kyndryl's cash flows to 2021-11-03**: the FY2023 annual report presents its cash flows
  "on a consolidated basis, including cash flows of discontinued operations". The FY2021 base is therefore not the
  continuing company's, and the growth measured from it is confessed as distorted, direction not determined from the
  filings read.
- **Depreciation variant** (the tool's, three years): OCF less stock pay less depreciation and amortization, $8,402M,
  $7,467M, $6,457M for FY2023 to FY2025. It runs below the capital-spending line because D&A includes amortization of
  acquired intangibles (the FY2025 line is "Amortization of capitalized software and acquired intangible assets",
  $2,737M); the rows treat the purchase-accounting part as not a real expense and the software part as real
  **[L2012-003]**. Capital spending is deducted in full and is the base.
- **Acquisitions recur**, in every one of the five years and $10,480M in the first half of 2026 (10-Q). They are shown as
  a column and a sensitivity, not deducted in the base, because whether the purchases are the cost of keeping the castle
  or growth is a Q2 and Q3 judgment the file did not reach. A reader who holds them to be the cost of standing still
  should use the last column. This choice is mine and is carried into "What in the framework was wrong or unclear".

### (a) The value range, under the Q7 convention
- **Bottom: $178.90 a share.** Five-year average owner cash $9,540M at no growth, at 5.66%: $168,548M over 942.13M
  shares. Owner cash is after interest, so the value is of the equity and no debt is deducted a second time; cash is not
  added, its interest already being in OCF.
- **Top: $207.36 a share.** The growth shown on aggregate owner cash, FY2021 $9,046M to FY2025 $9,740M, 1.87% a year
  (the FY2021 caveat above), carried ten years, then zero nominal growth, at 5.66%: $195,361M.
- **Width: 1.16 to one**, inside the convention's three to one.
- **Against the price of $221.58:** the price is above the top of the range. The owner-cash yield at the price is
  4.57%, below the 5.66% Treasury, and the expected return on the shown-growth case is 5.31% a year, about half the floor
  CONVENTION of about ten percent **[M2003-149]**, **[L2002-020]**. Had the file reached Q7 it would have closed OUT there
  under the convention (a price above the top of the range closes OUT through the floor convention).
- **Sensitivity, acquisitions treated as a real cost:** $5,079M at no growth is $95.24 a share at the sovereign.

### (b) The fair price
**$114.95 a share**: the price at which the central case, the shown-growth case above, returns the floor CONVENTION of
about ten percent pre-tax (**[M2003-149]**, **[L2002-020]**): ten years at 1.87% then flat, discounted at 10%. Owner cash
is after IBM's own taxes, and the 10% is applied to it directly as the holder's pre-tax return. With acquisitions
deducted, the same arithmetic at no growth gives $53.91.

### (c) The cheap price
**$101.26 a share**. Rule (the one the EXTR run of 2026-10-05 stated, not a framework convention, confessed as mine
here too): the price at which the bottom of the range, five-year average owner cash at no growth, returns the 10%
floor ($9,540M / 0.10 = $95,398M over 942.13M shares). "it ought to just kind of scream at you" **[M1996-084]**; the
adjustment for doubt is "a big discount from that present value" **[M1997-126]**. On a name closed TOO HARD (NATURE) the
cheap price buys nothing: a lower price does not reopen the box (section I).

### The Q6 buyback note, recorded back as the convention asks
No open-market repurchase line after FY2019 ($1,361M that year; $11,995M to $15,375M a year in FY2010 to FY2014, XBRL);
since then only "Common stock repurchases for tax withholdings" ($1,018M in FY2025, cash-flow statement). The diluted
share count rose from 892.8M (FY2019) to 948.7M (FY2025) (XBRL, `0001558370-20-001334` and `0000051143-26-000010`).
There are no prices paid to read against the range. Not judged: Q6 not reached.

### Non-GAAP habits, recorded as found (Q4 not reached)
The second-quarter release (8-K EX-99.1, `0000051143-26-000077`) and the July letter feature "Operating (Non-GAAP)"
results, which remove "Acquisition-Related Adjustments" and "Retirement-Related Adjustments": second-quarter 2026
diluted EPS $2.27 GAAP against $2.93 operating, pre-tax margin 14.4% against 19.2% (8-K EX-99.1, `0000051143-26-000070`).
The rows bear both ways and are not weighed here: "a management that regularly attempts to wave away very real costs by
highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; against it, Buffett's own reading that
purchase-accounting charges such as the amortization of customer relationships "are clearly not real expenses" while
software amortization is real **[L2012-003]**. Stock pay is not among the two adjustment columns in the reconciliation
read. Restructuring charges of $435M, $692M and $653M in FY2023 to FY2025 (XBRL) recur.

### The competitor row, from the competitors' own filings (Q2 not reached; context)
| Company, fiscal year | Revenue $M | Revenue growth, last two years, a year | Operating margin | Stock pay / revenue | Owner cash (OCF - stock pay - capex) / revenue | Capital spending $M | Accession |
|---|---|---|---|---|---|---|---|
| IBM, FY Dec-2025 | 67,535 | 4.5% | 15.3% pre-tax (operating income not tagged) | 2.5% | 14.4% (software investment also deducted) | 1,738 | 0000051143-26-000010 |
| Accenture, FY Aug-2025 | 69,673 | 4.2% | 14.7% | 3.0% | 12.6% | 600 | 0001467373-25-000217 |
| Oracle, FY May-2026 | 67,357 | 12.8% | 30.6% | 7.1% | -42.3% (FY2024 14.8%) | 55,663 | 0001193125-26-277521 |
| Microsoft, FY Jun-2026 | 331,839 | 16.4% | 46.8% | 3.7% | 16.4% | 115,948 | 0001193125-26-323660 |

Source: each company's companyfacts XBRL, annual 10-K values (`peers_xbrl.txt`). What the row shows: IBM's
whole-company figures sit beside Accenture's (similar revenue, growth, margin and owner-cash margin), not beside the
software companies it names as competitors; and two of the software competitors it names spent $55.7B and $115.9B in a
single year on capital assets, thirty-two and sixty-seven times IBM's capital spending, building the infrastructure on
which the hybrid-cloud contest named at Q1 is fought. Recorded as found **[M1997-127]**; Q2 not reached.

### The strongest evidence against the business, written down as found **[M1997-127]**
1. **Revenue shrank for five years before it grew.** $81,741M (FY2015) to $73,620M (FY2020) before the Kyndryl
   separation; $57,350M (FY2021, continuing) to $67,535M (FY2025), with $22.3B spent on acquisitions in those five years
   (XBRL and the cash-flow statements above).
2. **Gross profit dollars have not grown in ten years**: $40,684M (FY2015) against $39,297M (FY2025) (XBRL).
3. **Equity is less than the goodwill and intangibles in every year read**, and debt has risen with each large purchase.
4. **The miss, in the chief executive's own words**: "this quarter we faltered. We did not adapt and move quickly
   enough" (8-K EX-99.1, `0000051143-26-000070`).
5. **The authors of the rows owned it and called it a mistake** **[M2017-019]**, **[M2017-079]**.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** **[M2000-105]**, **[L1993-023]**, **[M2002-092]**. The forecast that would decide it,
IBM's earning power and competitive position in 2036 across hybrid-cloud software, AI, IT services, quantum and the
businesses it has yet to buy, is one the industry's insiders would not write down, and the speakers' own ten-year
judgment of this company, made after fifty years of reading, is on the record as wrong **[M2017-019]**. No research pass
is opened (that is for WORK). For the record only, as COMPUTATION: value range $178.90 to $207.36 a share (1.16 to one)
against $221.58; fair price $114.95; cheap price $101.26; with acquisitions treated as a cost, $95.24 at the sovereign.

**Reversal condition (one line):** the box would change only if the deciding forecast became one an insider would write
down, for instance IBM reduced to the mainframe franchise and its software with that franchise's 2036 economics
foreseeable from the filings; a lower price alone does not reopen it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 closed and again at
      the end (write-early).
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and each quoted fragment beside an id
      checked to be in that row); every filing fact has its accession; no number without a row, a filing or a CONVENTION
      label.
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance, and the computation block is headed as the
      protocol requires.
- [x] Owner cash after every real cost (stock pay and all capital spending, software included), never a net-income
      proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q1's other-side case, the
      computation block).
- [x] No row dated after the anchor is cited in a point-in-time run (a live run; the rule does not bite).
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield, growth and "points over" lines were not used as
      rules.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The corpus contains its authors' own verdict on this company, and the framework does not say how to weigh it.**
The v5 rows include Buffett's 2012 case for IBM **[M2012-073]**, his 2013 grading of his own understanding
**[M2013-074]** and his 2017 "I was wrong on the first one" **[M2017-019]**. The scope directive admits them; the
anchor-date convention of Part VII bars later rows only in a point-in-time test. Nothing says whether a speaker's verdict
on the very company is evidence about the business (as I used it, at Q1, for the predictability of IBM's economics) or
a prior to be set aside. A second analyst could set those rows aside, read the mainframe annuity as foreseeable, and
reach Q2. The framework could say which. (2) **Q1's layer question again**: as in the EXTR run, part of the business
(the mainframe stack, under a third of revenue) is foreseeable and the rest is not. The holding-company rule reads a
company by its parts and keeps the whole outside the circle if a part that matters cannot be understood (Q1, A holding
company); I applied that reading to an operating company's segments by analogy, and the framework does not say it
extends that far. (3) **Recurring acquisitions under the Q7 convention.** The convention deducts "all capital spending"
and is silent on cash acquisitions made every year; for IBM they nearly halve five-year owner cash ($9,540M to
$5,079M). I showed them as a sensitivity and did not deduct them in the base. (4) **Financing receivables inside OCF.**
The convention takes OCF as filed; IBM's lending book makes OCF swing with the hardware cycle ($4,278M of receivables
absorbed in FY2025). The framework has no rule for a captive finance arm outside the sector method for insurers.
(5) **A separation inside the five-year window.** The FY2021 base includes Kyndryl; the convention's first-to-last growth
measure has no rule for it. (6) **Tool defects**: `tools/run.py` prints investment in software as an "other capital
payment" and leaves it unchosen, so its headline owner-earnings lines overstate IBM's owner cash by $565M to $647M a
year; its 2017 debt figure is a partial sum (the tool flags it with an asterisk).
