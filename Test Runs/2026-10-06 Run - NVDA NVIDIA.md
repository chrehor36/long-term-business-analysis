# Company Run — NVIDIA Corporation (NASDAQ: NVDA) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. The dispatch forbade
opening `PORTFOLIO.md`, any holding review, the session-state files, the register, the prepped reading list,
`tools/alerts.json` and any earlier run or research folder for this ticker; none was opened. Whether the operator holds
or wants this name is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The repository map (`CLAUDE.md`) and the protocol loaded at session start; neither names
this ticker. (2) One other company's v5 run, `Test Runs/2026-10-05 Run - EXTR Extreme Networks.md`, was read for form
only, as the dispatch allows; it closed at Q1 TOO HARD (NATURE), and I was aware of that box before writing this one, a
possible anchor on a technology name's routing, declared here so it can be discounted. (3) The file listing of
`Test Runs/` was seen to find that form file; it shows no file for this ticker dated 2026-10-05, and earlier files were
not looked for. (4) `tools/run.py` prints v4 material (a yield, "growth the price assumes", "points over the
sovereign"); those lines were not read as rules (Part VII). (5) Prior general knowledge: I knew before reading that
NVIDIA designs graphics and AI accelerator chips sold mostly into data centers and that its revenue had grown very fast;
every fact below is from the filings, not from that memory.

Working folder: `Test Runs/_research 2026-10-06 NVDA/` (`run_py_output.txt`, `cover_shares.txt`,
`sources_sovereign.txt`, `xbrl_revenue_margins.txt`, `computation.txt`; raw filings and text dumps under `cache/`,
gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $238.90 (close 2026-10-05; `tools/run.py` live quote; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, $0.001 par. "The number of shares of
  common stock, $0.001 par value, outstanding as of August 21, 2026, was 24.1 billion." (Form 10-Q for the quarter ended
  2026-07-26, filed 2026-08-26, accession `0001045810-26-000075`, cover; the filer rounds to a tenth of a billion). The
  equity statement of the same 10-Q gives 24,147M at 2026-07-26; preferred stock nil. **Tool defect:**
  `python Screens/cover_shares.py NVDA` returned "1,045,810,000,000,000", which is the registrant's CIK (1045810) read as
  the count and scaled by a billion; its output is saved and not used. The cover sentence above was read in the filing
  itself.
- **Market cap:** about $5,757,000M ($5.76 trillion; 24.1B x $238.90; on the equity-statement count, $5,769B).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K for the year ended 2026-01-25 (filed 2026-02-25, accession
  `0001045810-26-000021`): Item 1 (business, competition, export controls), Item 1A (risk factors), Item 7 (customer
  concentration, revenue by market), Item 8 (income statement, balance sheet, cash-flow statement, the Groq note). Form
  10-Q for the quarter ended 2026-07-26 (filed 2026-08-26, `0001045810-26-000075`): cover, statements, Note 10
  (commitments and guarantees), Item 2 (gross margin, export controls), Item 1A (debt, guarantees). 8-K of 2026-08-17
  (`0001045810-26-000069`, Items 1.01 and 2.03: the SB Energy residual value guarantees for OpenAI's leases). 8-K of
  2026-09-03 (`0001045810-26-000078`, Item 8.01: the agreement to acquire Hugging Face). DEF 14A of 2026-05-12 (`0001045810-26-000036`):
  read only for the incentive horizon and the FY2026 goals used at Q1. Fetched and not read, because the run closed
  before the question it serves: the 8-K of 2026-08-26 with the Q2 FY2027 release and CFO commentary (`0001045810-26-000073`, Q4's non-GAAP reading).
- **One figure cross-checked against the filed statement:** the FY2026 consolidated statement of cash flows
  (`0001045810-26-000021`) gives net cash from operations $102,718M, stock-based compensation $6,386M and purchases of
  property, equipment and intangibles $6,042M; `tools/run.py` gives 102,718 / 6,386 / 6,042. **Tool defect:** its D&A
  column (FY2026 2,888, FY2025 1,893) is not the filed cash-flow line (2,843 and 1,864); the capex basis is used.
- `python tools/run.py NVDA` arithmetic lines only (Part VII): owner cash after stock pay and all capital spending
  FY2024 $23,472M, FY2025 $56,116M, FY2026 $90,290M; five-year mean (FY2022 to FY2026) $35,421M; three-year mean
  $56,626M. Stock pay is resolved and complete in the cash-flow statement (FY2024 $3,549M, FY2025 $4,737M, FY2026
  $6,386M). **Not resolved, because Q4 was not reached:** whether the FY2026 cash paid for the Groq licence and hires
  ($13,000M at closing, plus $4B payable within a year, of which $2,944M was paid in the first half of FY2027) and
  acquisitions ($1,535M) are costs of staying in the race, which would take FY2026 owner cash to $75,755M
  (`computation.txt`). The v4 floor, yield and "points over the sovereign" lines are not read.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**, which
here means owning, at about $5.76 trillion, a company whose operating margin was 15.7% in FY2023 and 62.4% in FY2025
(XBRL, first-filed, `xbrl_revenue_margins.txt`), so the question is what the business will earn, not what the next
buyer will pay. Who is paid to tell you bears on this name with unusual force: "you do not get an information flow that
is balanced in any way [...] because the money is in believing something different" **[M2001-052]**; "don’t ask the
barber whether you need a haircut" **[M2011-083]**. No macro view enters **[M2000-094]**, which applies here to the
temptation to answer Q1 with a forecast of "AI spending"; that forecast is the industry's, not the business's. The
analyst's habit: look for "what you’re missing" **[M2025-013]**, state the other side's case better than its holder
**[M2016-055]** (done under Q1), and "destroy our previous ideas" **[M2016-054]**. **Contrary evidence, written down as
found** **[M1997-127]**: (a) gross margin has stayed between 56% and 75% for eleven years (FY2016 56.1%, FY2023 56.9%,
FY2025 75.0%, XBRL) and was 75.0% in the first half of FY2027 (10-Q Item 2), a stable figure in an industry the filer
calls one of "rapid technological change"; (b) the filer has spent on research since 1993 and dates its software
platform, CUDA, to 2006 ("We have invested over $76.7 billion in research and development since our inception", 10-K
Item 1), which is a two-decade position, not a recent one; (c) owner cash after stock pay and capital spending was
$90,290M in FY2026 on $6,042M of capital spending, so the business needs little capital per dollar earned; (d) after a
$4.5B charge in the first quarter of FY2026 when H20 sales to China required a licence (10-Q Item 2), FY2026 revenue
still rose 65% over FY2025 ($215,938M against $130,497M, 10-K income statement). Each is weighed at
Q1 below. Found against the case, and written down at once: (e) the filer has begun to finance its customers: guarantees
"capped at a total of $ 105 billion, to provide credit support [...] on behalf of a customer, an affiliate of OpenAI"
(10-Q Note 10), equity purchases of $42,404M in six months (10-Q cash-flow statement), and "Financing arrangements with
certain investment-grade customers, including extended payment terms" (10-Q Item 2); (f) supply commitments rose
"from $ 119 billion last quarter to $ 279 billion as of July 26, 2026" (10-Q Note 10).

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase would be made without borrowed money and at a size that cannot
threaten the buyer, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**. Nothing in this name forces a breach on the buyer's side; the
target's own guarantees and commitments (contrary evidence (e) and (f)) belong to Q9, which this run does not reach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position
will look like in five or 10 years" **[M2012-065]**; the failing form is "We understand the product. [...] We just don’t
know the economics of it 10 years from now." **[M2000-104]**. The product is plain enough: accelerated-computing chips
and the systems, networking and software sold with them, 89.7% of FY2026 revenue from Data Center ($193,737M of
$215,938M, 10-K revenue by market, `0001045810-26-000021`). The question is whether the earning power of NVIDIA inside
that industry can be seen ten years out.

**The key variables** **[M1998-044]**, and how predictable each is, in the filer's own words:
- **Its share of AI computing against rivals that include its own largest customers.** The 10-K's list of "current
  competitors" names AMD, Huawei and Intel, and "large cloud services companies with internal teams designing hardware
  and software that incorporate accelerated or AI computing functionality as part of their internal solutions or
  platforms, such as Alibaba Group, Alphabet Inc., Amazon, Inc., or Amazon, Baidu, Inc., Huawei, and Microsoft
  Corporation" (Item 1, Competition). The same filing reports that "sales to one direct customer represented 22% of
  total revenue and sales to another direct customer represented 14%" and that "our customers can generally cancel,
  change, or delay product purchase commitments with little notice to us and without penalty" (Item 1A). The buyers
  are building the substitute.
- **The pace of the technology.** "The market for our products is intensely competitive and is characterized by rapid
  technological change and evolving industry standards" (Item 1); "Our accelerated computing platforms experience rapid
  changes in technology, customer requirements, competitive products, and industry standards" (Item 1A); "bringing new
  advanced architectures on a one-year product cadence" (Item 7). In FY2026 the company paid $13,000M at closing, and
  owes $4B more, for "a non‑exclusive license agreement with Groq, Inc., or Groq, for its language processing unit
  technology" and hired its employees (Note on Groq), a rival architecture bought in rather than out-built; the filer
  adds that "The economic outcomes of this arrangement depend on our ability to translate the licensed technology into
  commercially viable products" (Item 1A).
- **Whether the customers can keep paying.** "Future demand may be affected by the ability of customers and partners,
  including those developing open models, to generate revenue and sustain investment in computing infrastructure"
  (10-Q Item 1A, `0001045810-26-000075`). The filer now supports that demand with its own balance sheet: guarantees
  "capped at a total of $ 105 billion" for OpenAI's leases (10-Q Note 10; 8-K `0001045810-26-000069`), $42,404M of
  equity securities bought in six months, and "extended payment terms under large, multi-quarter agreements" (10-Q
  Item 2). The economics of NVIDIA ten years out depend on the economics of its customers' AI businesses ten years out.
- **Government.** "Under the current rules and geopolitical landscape, we are unable to create and deliver a
  competitive product for China’s data center market that receives approval from both the USG and the Chinese
  government" (10-K Item 1); the H20 rules cost a $4.5B charge in one quarter
  and H200 licences a further $0.4B (10-Q Item 2). Each new rule is set outside the business.

**What the record shows of the forecast.** Revenue was $26,974M in FY2023 and $215,938M in FY2026, eight times in three
years; operating margin went from 15.7% (FY2023) to 62.4% (FY2025) (XBRL, first-filed, `xbrl_revenue_margins.txt`).
"How far off we can be" **[M2011-084]** is answered by the company's own board: its FY2026 stretch revenue goal was
$190.0 billion (cut to $160.0 billion for the export controls), and the year closed at $215.9 billion, 13.7% above the
stretch figure set at the year's start (DEF 14A 2026, `0001045810-26-000036`, pay discussion). The insiders missed a
one-year forecast by that much, upward.

**The rows.** "if something comes in where there’s a technological component that’s of significance [...] it won’t make
it through the filter" **[M1998-008]**; "a business that must deal with fast-moving technology is not going to lend
itself to reliable evaluations of its long-term economics" **[L1993-023]**; "whenever we look at a business and we see
lots of change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**. Seeing the industry grow is not
seeing the company's returns: "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not
mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy."
**[L2009-005]**; "we know there’ll be change, and we don’t know who the winners will be" **[M2014-097]**. The nearest
case in the rows is the one Buffett named of the best-run technology company of his day: "We think Microsoft is a
sensational company run by the best of managers. But we don’t have any idea what that world is going to look like in 10
or 20 years." **[M1996-059]**. And a lead won fast is a warning: "usually if something can gain competitive advantage
very quickly, you have to worry about them losing it quickly, too. I mean, when an industry is in flux, there are a lot
of people that think they’re the survivors" **[M2002-050]**. Test 3, do the past statements tell me the future ones
**[M2008-033]**: the FY2023 statements did not tell anyone the FY2025 ones. Test 9: "if you have doubts about something
being into your circle of competence, it isn’t." **[M2002-092]**.

**The other side's case**, stated as well as I can **[M2016-055]**. NVIDIA is not a young company riding one product: it
invented the GPU in 1999, opened it to general computing with CUDA in 2006, and has spent "over $76.7 billion in research
and development since our inception" (10-K Item 1). Gross margin has held between 56% and 75% for eleven years, through a
crypto bust, a gaming glut and an export ban, which is the mark of a position, not a fad; the buyers who are building
their own chips are still its largest customers; the business needs little capital ($6,042M of capital spending against
$102,718M of operating cash in FY2026). On this reading the ten-year economics are foreseeable in kind (a toll on
computing) even if not in amount, and the speakers themselves regretted missing technology they could see from the
inside: "I feel like a horse’s ass for not identifying Google better" **[M2019-024]**. I do not adopt it, for three
reasons from the filings. First, the stable figure is gross margin over a decade in which the product, the customer and
the market all changed under it: in the three years the 10-K reports, Data Center went from $47,525M (78% of revenue,
FY2024) to $193,737M (89.7%, FY2026) and the largest direct customer from 13% to 22% of revenue, so the stability is
of a ratio across a changing business, not proof of a position that will hold. Second, the Google regret rests on an
insight Berkshire had as GEICO's buyer of clicks **[M2019-024]**; no comparable insight into the economics of AI
computing is available to this analyst, and outside the circle "that is not an error, as far as we’re concerned"
**[M2001-006]**. Third, the filer itself now pays to buy in a rival architecture (Groq), guarantees a customer's rent
($105B cap) and lends its own balance sheet to demand; a business whose ten-year position were secure would not need to
do any of these, and none of them can be read ten years forward. The other reading is carried into "What in the
framework was wrong or unclear".

**Which cause** (section I, the two causes). The deciding question is: what will NVIDIA earn on its capital in 2036,
against AMD, Huawei and the chips its own largest customers are designing, after a decade of one-year architecture
turns, export rules and its customers' own success or failure in AI? The test is whether the insiders would write that
down **[M2000-105]**: "they would not want to put down on paper their predictions about where 10 companies you would
choose in the tech field would be in 10 years, in terms of their economics. They would say, “That’s too hard.”" The
insiders here set their operating goals one year at a time ("SY PSUs that can be earned based on annual Non-GAAP
Operating Income performance", DEF 14A) and missed the one-year figure by 13.7%. This is the industry's cause, "the
nature of the industry would be the roadblock" **[L1993-023]**; "Our problem -- which we can't solve by studying up --
is that we have no insights into which participants in the tech field possess a truly durable competitive advantage."
**[L1999-018]**; "we’re not going to learn enough in the followings five months to make up for the fact that we went in
deficient in the first place." **[M2008-086]**. The cause is NATURE, not WORK: more reading of NVIDIA's filings would
tell what NVIDIA has earned, not where the technology and its customers will put it.

- **VERDICT: TOO HARD (NATURE).** "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a
  fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**; the box is "too hard"
  **[M2006-013]**, and a lower price does not reopen it **[M2000-038]**. The file closes here; every question after it is
  NOT REACHED, and no number below Step 0 is a clearance.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed TOO HARD (NATURE)). The routing is fixed: "a business whose ten-year economics cannot be foreseen
because its industry changes fast has already closed at Q1 TOO HARD" **[M1998-008]**. No competitor row was built; the
competitors named in the 10-K (AMD, Huawei, Intel, and the cloud companies' own chip teams) are recorded at Q1 as a
fact of the filing, not as a castle test.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. Left for a reader who reopens the name on a different reading of Q1, from the filings already fetched:
the ten balance sheets in `run_py_output.txt`; the Groq payment and acquisitions against owner cash (Step 0); equity
gains in "Other income, net" ($24,140M in the first half of FY2027 against $3,039M a year earlier, 10-Q income
statement); the Q2 FY2027 release (`0001045810-26-000073`) for the non-GAAP habit, unread.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was computed, and none is to be inferred from the Step 0 arithmetic.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Recorded for whoever reaches it: senior notes of $33.5B at 2026-07-26 against $8.5B at the FY2026 year-end
(10-Q Item 1A; 10-K Item 7A), the residual value guarantees capped at $105B (8-K `0001045810-26-000069`), and supply
and capacity commitments of $279B (10-Q Note 10).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing; outside the circle there is "no penalty in investing if
you don’t swing" **[M2018-087]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT ASKED (the run closed at Q1).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** **[M2000-105]**, **[L1993-023]**, **[L1999-018]**. The forecast that would decide
it, NVIDIA's return on capital in 2036 against AMD, Huawei and the chips its own largest customers design, after a decade
of one-year architecture turns, export rules and its customers' own fortunes in AI, is one the insiders would not write
down: the company sets its operating goals one year at a time and its FY2026 revenue ran 13.7% past the board's stretch
figure. Q7 was not reached; no value range is given beside the price of $238.90. "too hard" **[M2006-013]** is not a
judgment of quality **[M2000-038]**, and a lower price does not reopen the box. Q11 belongs to the holding review, not
to this purchase run.

**What would reverse it** (a reading, not a trigger): evidence from the filings that NVIDIA's ten-year economics had
become foreseeable, such as its architecture cadence and customer base settling into a slow-changing toll whose share
the in-house chips of its customers visibly fail to take over several years, so that the insiders' own planning ran on
multi-year operating targets they then met. On the rows, that would be a different industry, not a cheaper price.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      The template copy was made before any fetch; the first commit came after Step 0, the foundations and the standing
      rule were written, the second after Q1, the third at the close.
- [x] Every v5 id resolves (grep it in `principle_ledger_v5.csv`): every id in this file was checked against the ledger's
      id column before the commit; every filing fact has its accession; no number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): Step 0 gives operating cash less
      stock pay less all capital spending, from the filed statement, and names the Groq and acquisition cash it did not
      resolve; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations, items (a) to (f); the other
      side's case at Q1).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is
      today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **The Q1 routing has no test for a long-held position inside a fast-changing industry.** The
framework sends "a business whose ten-year economics cannot be foreseen because its industry changes fast" to Q1 TOO
HARD **[M1998-008]**, but the other side's case here is not that the industry is slow; it is that one company has kept
its place for two decades through every change, which is a castle claim that only Q2 is built to test. The rows that
would separate a maintained lead from a rebuilt one are carried OPEN in Part VI (**[L2005-010]** and **[L2004-007]**
against **[L2007-005]**), and nothing tells the analyst whether "the company has survived the change" can be weighed at
Q1 at all. I closed at Q1 because the variables that decide the ten-year earnings (the customers' own chips, their
ability to pay, the export rules) are outside the company, not because the company has no position; a reader who holds
that the position can be judged would send the name to Q2, where it would need the moat that is "continuously rebuilt"
**[L2007-005]** to be read. Both routes end in the same box on these filings, but the framework should say which owns
the question. (2) **Step 0 asks for owner cash "after every real cost" before Q4 decides what a real cost is.** A
$13,000M payment for a rival's technology and its staff, booked as goodwill and an intangible, is exactly the item Q4
would have to rule on; a run that closes at Q1 leaves the line unresolved, and the template does not say whether
Step 0 must settle it or only name it. I named it and left it (`computation.txt`). (3) **The insider test asks whether
insiders "would not write it down" **[M2000-105]** but not where to look for what they did write.** I used the proxy's
incentive horizon and the board's own one-year goals as the insiders' written forecast; that is a reading of mine, not a
rule, and another analyst might use management's public remarks instead. **Tool defects, reported and not fixed:**
`Screens/cover_shares.py NVDA` returned the CIK (1045810) as the share count, scaled by a billion
("1,045,810,000,000,000"), apparently from a cover whose count is stated in words ("24.1 billion") rather than a
number; `tools/run.py`'s D&A column (FY2026 2,888; FY2025 1,893) does not match the filed cash-flow line (2,843; 1,864).
