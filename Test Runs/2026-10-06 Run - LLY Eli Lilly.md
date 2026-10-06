# Company Run — Eli Lilly and Company (NYSE: LLY) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not opened, so
whether the operator holds this name is not stated here.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, `tools/alerts.json`, any earlier run file or research folder on
this ticker. Seen without opening: a listing of the 2026-10-05 run file names in `Test Runs/` (none names this company) and
the box lines of about twenty of them, read for form only. The analyst's training memory of Lilly (incretin drugs, a large
share price rise) is a prior, to be replaced by the filings and not confirmed by them.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Identity.** Eli Lilly and Company, CIK 59478, Indianapolis, incorporated in Indiana in 1901; "We discover, develop,
  manufacture, and market products in a single business segment—human pharmaceutical products." (10-K FY2025, Item 1,
  accession 0000059478-26-000013).
- **Price:** $1,143.12 (2026-10-05, printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common, **941,357,065** outstanding at 2026-08-03 (10-Q
  for the quarter to 2026-06-30, filed 2026-08-05, accession `0000059478-26-000081`, cover: "Common | 941,357,065").
  `python Screens/cover_shares.py LLY` returned the same count from the same accession.
- **Market cap:** 941.357M x $1,143.12 = **$1,076,084M** (about $1.08 trillion).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, accession 0000059478-26-000013): Item 1 (products,
  competition, intellectual property table, pricing and regulation), Item 1A, Item 7 overview and revenue tables, the
  cash-flow statement; 10-Q Q2 2026 (filed 2026-08-05, accession 0000059478-26-000081): cover, revenue tables, MD&A
  overview; 8-K of 2026-08-05 with EX-99.1, the Q2 2026 results release (accession 0000059478-26-000077); proxy DEF 14A
  (filed 2026-03-20, accession 0000059478-26-000029), fetched and not read past its opening, because the run closed
  before Q5. Extracts and arithmetic: `Test Runs/_research 2026-10-06 LLY/NOTES - filing extracts and arithmetic.md`.
- **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities, $16,813M in the
  XBRL series printed by `tools/run.py`, matches the consolidated statement of cash flows ("Net Cash Provided by
  Operating Activities | 16,813 | 8,818 | 4,240") and the MD&A ("increased to $16.8 billion in 2025, compared with $8.8
  billion in 2024"), accession 0000059478-26-000013.
- `python tools/run.py LLY`, arithmetic lines only (saved as `Test Runs/_research 2026-10-06 LLY/run_py_output.txt`;
  the first attempt failed on an SEC HTTP 429 and the retry ran; its statement-lines block still records one earlier
  10-K not read on a 429). **COMPUTATION — NOT A CLEARANCE** (operator rule 3), USD millions:

  | FY | OCF | SBC | D&A | capex | OCF-SBC-capex | OCF-SBC-D&A |
  |---|---|---|---|---|---|---|
  | 2023 | 4,240 | 629 | 1,527 | 3,448 | 163 | 2,084 |
  | 2024 | 8,818 | 646 | 1,767 | 5,058 | 3,114 | 6,405 |
  | 2025 | 16,813 | 626 | 1,997 | 7,841 | 8,346 | 14,190 |

  Cash paid for acquired in-process research (not in capex): 3,944, 3,346 and 3,008; with it deducted the capex column
  reads -3,781, -232 and 5,338. Five-year means printed by the tool: 4,539 (capex basis) and 6,769 (D&A basis). Owner
  cash on the price: 0.36% to 0.70% on the three-year means. These lines are recorded and not used: the run closed at Q1.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own Lilly if the market closed for years
**[M1997-109]**, which turns on what the business will produce, not on the price's recent rise, which "is never a reason
to buy" in itself (the foundations' reading of **[L2013-007]**). The analyst's habits bear hardest here: write contrary
evidence down at once **[M1997-127]**, ask "What do I not know that I need to know?" **[M1999-129]**, and distrust the
anchor of a prior conclusion **[M2016-054]**. Who is paid to tell you: the company's one-year guidance and its "Key
Products" framing are a seller's account **[M2011-083]**; the run reads the filed statements instead. **Contrary evidence,
written down as found** **[M1997-127]**: (1) the speakers themselves put the pharmaceutical industry inside their circle:
"it was within our circle of competence to identify the industry as likely to enjoy very high profits over time"
**[M1998-073]**; Munger, "the future of the pharmaceutical industry was easier to predict than the future of the
high-technology sector" **[M2001-002]**; they call the missed group purchase a mistake **[M1999-043]**. (2) Lilly's own
record in the filing is strong: revenue $34,124M (2023), $45,043M (2024), $65,179M (2025), operating cash $4,240M to
$16,813M, and the 10-K's compound patent on tirzepatide runs to 2036 in the U.S. (accession 0000059478-26-000013). Both
are weighed at Q1 below; the first is the strongest case against the close the run reaches.

## THE STANDING RULE
Owning a marketable stake bought for cash, without borrowed money and without any instrument that can call for cash,
puts the buyer at no risk of ruin from this purchase **[M2012-081]**, **[L2014-005]**, **[L2014-024]**; the run takes no
position and sets no size (Q10 not reached).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years", with "some notion of how the industry will develop and where the company will stand within the
industry" **[M2012-065]**; "we understand the product [...] We just don’t know the economics of it 10 years from now" is
the failing form **[M2000-104]**. Understanding the drug is not the question; foreseeing Lilly's economics in 2036 is.

**What the filings say the business is.** One segment, human pharmaceuticals (10-K FY2025, Item 1, accession
0000059478-26-000013). The filer states its own condition of success in the words of the row that names the risk: "Our
long-term success depends on our ability to continually discover or acquire, develop, and commercialize innovative
medicines." (Item 1). Munger's test, "Take pharmaceuticals, if they had never invented any more pharmaceuticals, it would
be a terrible business." **[M1999-075]**. And the filer on what invention does to its own products: "When new products,
uses, or delivery systems with therapeutic, convenience, or cost advantages are introduced, including by developing new
modalities, our existing products become subject to decreased sales volumes, progressive price reductions, or both."
(Item 1, Competition).

**The key variables, and whether they are foreseeable** **[M1998-044]**:
1. *One molecule family.* Tirzepatide (Mounjaro, Zepbound) was $5,339M of $34,124M revenue in 2023 (15.6%), $16,466M of
   $45,043M in 2024 (36.6%), $36,507M of $65,179M in 2025 (56.0%; the filer: "56 percent") (10-K disaggregation table,
   accession 0000059478-26-000013), and "65 percent of our total revenue for the six months ended June 30, 2026" (10-Q,
   accession 0000059478-26-000081). Its U.S. compound patent is estimated to expire in **2036**, its U.S. data
   protection in 2027 (10-K, Our Intellectual Property Portfolio). The ten-year horizon of the test ends in the year the
   largest product loses its compound patent in its largest market.
2. *The successor.* The prior incretin, Trulicity, fell in the U.S. from $5,433M (2023) to $3,694M (2024) to $2,914M
   (2025), before its own 2027 U.S. expiry, as the company's next molecule displaced it (10-K). The business renews its
   position by replacing its own leading product. What replaces tirzepatide is in the pipeline and in purchases:
   orforglipron (Foundayo), launched in the U.S. for obesity in Q2 2026 and licensed from Chugai at royalties "from mid
   single digits to low teens" (10-Q); retatrutide, with a BLA planned for "the first quarter of 2027"; and four
   acquisitions completed in Q2 2026 with three more after the quarter, $2.8B of acquired IPR&D charged in the quarter
   (EX-99.1, accession 0000059478-26-000077). Which of these succeed, and against which rivals, is the question the
   speakers say they cannot answer: "when we invest in something like pharma, we don’t know the answer on the pipeline.
   It will be a different pipeline anyway five years from now." **[M2008-113]**; "You shouldn’t be trying to guess
   whether, you know, one drug company has a better drug pipeline than another." **[M2007-069]**; "we bring nothing to
   the table when it comes to evaluating patents [...] So we simply don't get into judgments in those fields."
   **[L1999-019]**.
3. *The price.* Set by governments and intermediaries, not by the maker alone. Q2 2026: U.S. realized price down 3%
   ("Excluding these adjustments, U.S. price would have declined by approximately 9%"), outside the U.S. down 36%,
   "driven primarily by the addition of Mounjaro to the National Reimbursement Drug List (NRDL) in China" (EX-99.1). The
   10-K: "The outcome of our preliminary agreements with the U.S. government and broader U.S. policy efforts to align
   domestic pharmaceutical pricing with international benchmarks [...] is uncertain"; "in July 2025, CVS Caremark [...]
   stopped covering Zepbound as a preferred obesity management medicine on some insurance plans"; of the IRA, "The full
   impact [...] remains uncertain". The speakers on this industry's future: "much of it is in the political realm. And my
   judgment about the — what politicians will do is probably not better than yours." **[M2005-098]**, under the heading
   "Future of pharmaceuticals is “too hard”", where Munger adds "We just throw some decisions into the “too hard” pile"
   **[M2005-099]**.

**The tests, applied.**
- *Where will it be in ten years?* **[M2000-037]**: not foreseeable from the filings; see the three variables.
- *Do the past statements tell me the future ones?* **[M2008-033]**: no. The 2023 statements (tirzepatide 15.6% of
  revenue, owner cash after capex $163M) did not tell the 2025 ones (56.0%, $8,346M); the business changed shape in two
  years, and "usually if something can gain competitive advantage very quickly, you have to worry about them losing it
  quickly, too" **[M2002-050]**.
- *Would the insiders write it down?* **[M2000-105]**: the filer writes down one year. The release gives 2026 revenue
  guidance of $85.0B to $87.0B and nothing further (a text search of the release and the 10-Q for 2030, 2031, 2035,
  "long-term outlook" and "long-range" found no instance). The 10-K: "it can be very difficult to predict revenue growth
  rates of, or variability in demand for, new or future products and indications" (Item 1A); "we cannot predict the
  extent to which our business may be affected by current or potential future legislative, regulatory, or private
  actor developments" (Item 1); and of the long run, the durability of the franchise "will depend on our ability to
  maintain or strengthen our competitive position as the therapeutic landscape evolves and to deliver further
  innovations" (10-Q MD&A).
- *Can I name the winner, not just the industry?* **[M2012-067]**: this is where the rows speak of this industry by
  name. "it’s easy for me to figure out that Coca-Cola’s the soft drink company to be in [...] than it is for me to
  figure out which one in the pharmaceutical." **[M1997-119]**; "It would not have been within our circle of competence
  to try and pick a single company." **[M1998-073]**; "We would not have great insights on specific companies. [...]
  It’s hard to evaluate the individual companies." **[M2002-060]**.
- *How far off could I be?* **[M2011-084]**: very far. Two-thirds of revenue rests on one molecule family whose price
  and share in 2036 depend on undiscovered rivals, on a compound patent ending that year and on government price setting.
- *Do I doubt it is inside?* Then it is not **[M2002-092]**.

**Contrary evidence, weighed** **[M1997-127]**. The strongest case against the close: the speakers put the industry inside
their circle ("it was within our circle of competence to identify the industry as likely to enjoy very high profits over
time" **[M1998-073]**; the pharmaceutical future "easier to predict than the future of the high-technology sector"
**[M2001-002]**; "we did blow it" in not buying the group **[M1999-043]**), and Lilly's record and protection on the
filing are strong. The same rows answer it: each one that admits the industry excludes the single company in the same
breath **[M1998-073]**, **[M2002-060]**, and the instrument they name for an understood industry with unpickable winners
is a group of the leaders bought at reasonable prices **[M1999-044]**, **[M2008-113]**. A run on one name is not that
instrument; and Lilly today, at 65% of revenue from one molecule family, is further from a proxy for the industry than
the companies of 1993 to 2008 the rows discussed. The basket stays a tension the framework carries as the reader's
(**[M2002-060]** against **[M2002-092]**, section VI, Q1); this run does not resolve it and does not act on it.

**Routing and cause.** The reason is ignorance, not a finding against the business, so the box is TOO HARD, not OUT
**[M2000-038]**, **[M2006-013]**: "Industries whose winners cannot be named go to the same box" (the framework's Q1,
**[M2012-067]**, **[L2009-005]**). The cause is **NATURE**, not WORK: the deciding question (which molecules, from which
companies, at what government-set prices, hold the incretin market in 2036, the year tirzepatide's U.S. compound patent
ends) is a forecast the industry's insiders do not write down **[M2000-105]**: the filer gives one year and calls the
rest very difficult to predict, and the speakers say of this industry that the pipeline cannot be known and will be a
different one in five years **[M2008-113]**. "We couldn't solve this problem, moreover, even if we were to spend years
intensely studying those industries." **[L1993-023]**. More reading of Lilly's filings would not supply the 2036
pipeline or the 2036 price; the research pass of Part VII is not opened, and a lower price does not reopen the file
**[M2000-038]**. Outside the circle the stop is not the error of omission the rows count **[M2001-006]**.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**, **[M1999-075]**, **[M2008-113]**, **[M2000-105]**. The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed TOO HARD (NATURE)). No competitor row was drawn.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets printed by `tools/run.py` are saved in the research folder and were not read as Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED (operator rule 2). The proxy was fetched (accession 0000059478-26-000029) and not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was computed. The owner-cash lines in Step 0 are COMPUTATION — NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** **[M2006-013]**. Lilly's ten-year economics rest on one molecule family (56% of 2025
revenue, 65% of the first half of 2026) whose U.S. compound patent ends in 2036, on a successor pipeline the speakers say
cannot be known in this industry **[M2008-113]**, **[L1999-019]**, and on prices set by governments and intermediaries
**[M2005-098]**; the filer itself says its long-term success depends on continual discovery **[M1999-075]**, writes down
one year and calls the rest very difficult to predict **[M2000-105]**. The rows admit the industry and exclude the single
company **[M1998-073]**, **[M1997-119]**, **[M2002-060]**. Q7 not reached; no range. Price $1,143.12, market cap
$1,076,084M, against owner cash after capex of $163M to $8,346M a year (2023 to 2025), shown in Step 0 as computation
only. No research pass is opened (NATURE), and a lower price does not reopen the file **[M2000-038]**. The one route the
rows give into this industry, a group of the leading companies bought at a reasonable price **[M1999-044]**,
**[M2008-113]**, is a different purchase from this one and would need its own run; this run does not make it. Q11 belongs
to the holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit c468e36, before the first EDGAR request); written question by
      question; committed after Step 0 and after Q1 (write-early).
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before it was written: one row each); every filing
      fact has its accession; no number without a row or a filing.
- [x] The order was kept; Q1, the first STOP, closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): the Step 0 lines are OCF less stock
      pay less capex, with the D&A variant and the acquired-IPR&D cash beside them, and none is used; the sovereign from
      the issuing authority (US Treasury); the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: in the foundations and weighed in Q1 (the
      speakers' own admission of the industry to their circle, and Lilly's strong record).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the run is dated
      today and every row cited is dated 2025 or earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); nothing it prints as a rule, an id or a floor.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Two things in the framework and one in the tools. (1) **Which box for a business that lives on continued invention.** Q1's
"What it rules OUT" list carries "Businesses that live on continued invention" **[M1999-075]** as an OUT, while the same
section sends industries whose winners cannot be named to TOO HARD **[M2012-067]**, and every pharmaceutical row in the
ledger gives ignorance of the single company as the reason, never a finding against it (**[M1998-073]**, **[M2002-060]**,
**[M2008-113]**). Section I defines OUT as a question answered against the name, which **[M1999-075]** alone does not do.
The run chose TOO HARD on **[M2000-038]**'s reasoning and records the choice; the framework should say which governs, or
move **[M1999-075]** to the TOO HARD paragraph as the 2026-10-05 pass did for the unnamed-winner item. (2) **The basket has
no run surface.** For this industry the rows' own instrument is a group of the leaders at reasonable prices
(**[M1999-044]**, **[M2008-113]**), and the framework carries the basket only as a reader's tension (**[M2002-060]** against
**[M2002-092]**). The template has no form for a group purchase, so a single-name run in such an industry can only close
TOO HARD and say so; whether the operator wants a basket form is a PRIME RULE 5 question, not answered here. **Tool
defects:** `tools/run.py` died on its first attempt with an uncaught SEC HTTP 429 at the ticker map (`tools/sources.py`,
`ticker_map`, no retry or backoff); on the retry it ran, but its statement-lines block still printed "NOT read:
0000059478-24-000065 (HTTPError: HTTP Error 429)", so the 2023 statement lines came from one filing fewer than intended.
Parallel sessions sharing one SEC rate limit will meet this again; a retry with backoff in `_get` would get the same
numbers sooner and add none. Not fixed here (brief: report, do not edit tools).
