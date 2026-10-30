# v5 READING REGISTER — one entry per unit of the blind read, appended by the cycle that read it
**Opened 2026-10-03.** Append-only. The order of units is `Screens/_daily/_v5_order.txt`; the rows are in
`principle_ledger_v5.csv`; the per-unit notes are in `Framework/v5/notes/`; the one-line log is
`Screens/_daily/V5 READ LOG.md`. The design that binds every entry is
`Framework/v5/PREREGISTRATION - v5 blind read and comparison.md`. Count rows from the ledger
(`python tools/v5_ledger.py count`), never from this file.

**What an entry is:** `### <key> - <date>`, then three to six lines: rows written by kind; the one passage the
reader would show the operator first; anything surprising, including any place the auto-loaded map or
protocol steered a reading. No rule is drafted here. Judgment belongs to the synthesis, with the operator present.

**Two facts fixed before the first entry.** The signed report sections (Owner-Related Business Principles,
Acquisition Criteria, Intrinsic Value, The Managing of Berkshire) are printed in the FY1995 to FY2017 reports
and not by those headings afterwards, so R-rows can come only from the 1996 to 2018 AM units. The 1994 and
1995 AM units read the FY1993 and FY1994 letters, which are the only form of those reports on disk.

---

### 1994 AM - 2026-10-03
Rows: 91 (L 32 from the FY1993 letter, M 59 from the morning session). Letter: rule 18, test 8, definition 6. Meeting: rule 34, test 19, definition 3, tension 2, mistake-and-lesson 1.
First to show the operator: L1993-020, the letter's definition of real risk as the loss of purchasing power over the holding period, with its five factors (the business, the managers' ability, their treatment of owners, the price, tax and inflation); the meeting restates it as risk tied to the time horizon (M1994-044).
Surprising: how much of the session is about the incentives of the other party (sellers' projections, managers rewarded for size, LBO funds with upside only, single-line insurers with nowhere else to put capital), and that insurance pricing and stock buying are described as one discipline (M1994-056, M1994-058). Two tensions rowed: own-stock volatility against the welcome of volatility (M1994-013 vs L1993-018), and Lynch's diversification as a "useful religion" against concentration (M1994-055 vs L1993-026).
Steering: the auto-loaded map's bond-comparison wording was noticed on M1994-004; details in the note. The brief arrived truncated; the full prompt file was read, see the note's last section.

### 1994 PM - 2026-10-03
Rows: 26, all M (rule 16, test 6, definition 2, tension 1, mistake-and-lesson 1). No letter or report rows (PM unit).
First to show the operator: M1994-081, growth judged by the capital it consumes: a business with no growth that throws off cash can beat a fast grower, and analysts underweight the difference.
Surprising: the plainness of the value definition (M1994-077: no foreseeable stream, no known value) and the strength of the capital-allocation answer (M1994-082 to 084: the CEO's own job, never delegated, operating capital left local). One tension rowed: M1994-076, an easier-to-understand future "doesn’t mean it’s a better buy", against the session's own preference for certainty (M1994-078).
Brief: the section 7 pathspec commit fails on a new untracked note until it is added; see the note's last section.

### 1995 AM - 2026-10-03
Rows: 90 (L 38 from the FY1994 letter, M 52 from the morning session; no report in this unit's order line). Letter: rule 19, test 12, definition 6, mistake-and-lesson 1. Meeting: rule 29, test 17, definition 6. No tension rows; four tensions are recorded in the note instead (projections against discounted cash, dry-spell waiting against not deferring on fear, not selling businesses against per-share value, past record against predictable future).
First to show the operator: M1995-037 and M1995-038 together, the moat and castle answer: a wide, long-lasting moat, an honest lord, every moat under attack and most worthless, and the questions of why the castle still stands and how much depends on the lord; Munger's translation follows as M1995-039 (scale advantages, low agency cost).
Surprising: how directly the meeting rejects written valuation models while keeping discounted cash as the definition (M1995-032, M1995-049, M1995-050), and the clean statement of mistake timing in the letter (L1994-034: mistakes occur at the time of decision).
Steering: the map's Q1 and Q2 wording was noticed on M1995-051; details in the note. Brief: the letter cites the report's acquisition-criteria appendix, which this unit's order line does not include; see the note's last section.

### 1995 PM - 2026-10-03
Rows: 67, all M (rule 31, test 25, definition 6, tension 3, mistake-and-lesson 2); Buffett 56, Munger 11. No letter or report rows (PM unit).
First to show the operator: M1995-105 and M1995-106 together, the measuring stick. Every new purchase is weighed against buying more of the best thing already owned ("Why would I rather have this than more Coca-Cola?"), and Munger says this screens out 99 percent and that institutions throw the tool away when they allocate 3 percent to a category.
Surprising: Munger's Title Insurance and Trust case (M1995-061). A hand-kept monopoly treated the computer as a cost reducer, and the computer let twenty rivals copy its plant until the industry's earnings went below zero. Also surprising: how many rows are about reading reported numbers skeptically (M1995-063 to 065, M1995-086 to 088).
Three tensions rowed (M1995-062, M1995-100, M1995-110). M1995-110's notes cite the wrong earlier id (103 for 109). The quote verifies, so nothing fails, but the helper has no amend command. The erratum is in the note.

### 1996 AM - 2026-10-03
Rows: 84 (L 34 from the FY1995 letter, R 15 from the 1995 report's signed sections, M 35 from the morning session). Letter: rule 13, test 11, definition 4, mistake-and-lesson 6. Report: rule 12, test 2, definition 1. Meeting: rule 18, test 11, definition 6; Buffett 33, Munger 2. No tension rows; four tensions recorded in the note.
First to show the operator: M1996-024 and M1996-025 together, the discount-rate answer: the long-term government rate, no risk premium in the rate, most companies cannot be estimated at all, stay above a threshold of understanding and get excited only at a significant discount; risk-adjusted rates on speculative businesses are "mathematical gibberish".
Surprising: how much of the letter is mistake-and-lesson about selling or under-owning wonderful businesses (GEICO 1952, Disney 1967, Cap Cities, the Gillette preferred), and that the morning's Class B discussion yields clean rules on issuance and buybacks (M1996-002, M1996-013) and on wanting a fair rather than a high price (M1996-020).
First unit with R rows. Brief: single-line source spans were written as `(lines N)` on fifteen rows instead of the earlier `N-N`; the report file renders printed dashes as spaces; see the note's last section.

### 1996 PM - 2026-10-04
Rows: 67, all M (rule 28, test 25, definition 8, mistake-and-lesson 4, tension 2); Buffett 59, Munger 8. No letter or report rows (PM unit).
First to show the operator: M1996-058 and M1996-059 together. "We feel change is likely to work against us": Buffett looks for businesses where change will not matter much, names Gillette's credibility in shaving as an asset "that can't be built" and "very hard to destroy", and declines to bet on Microsoft even under the best manager because he cannot see where that world will be in 10 or 20 years.
Surprising: the Mayo Clinic against the local brain surgeon (M1996-065), which comes back in the Disney answer as "the mouse doesn't have an agent" (M1996-079); and Munger saying he has never seen Buffett do a discounted cash flow (M1996-083, rowed as tension against the morning's M1996-011 and M1996-024).
Brief: some lessons are two-speaker exchanges and the row takes one speaker; first speaker used, labels kept in the quote. See the note's last section.

### 1997 AM - 2026-10-04
Rows: 118 (L 44 from the FY1996 letter, R 25 from the 1996 report's reprinted Owner's Manual, M 49 from the morning session). Letter: rule 26, test 11, definition 6, mistake-and-lesson 1. Report: rule 13, test 7, definition 5. Meeting: rule 20, test 19, definition 6, mistake-and-lesson 4; Buffett 40, Munger 9. No tension rows; four tensions recorded in the note. Two rows refused as word-for-word repeats of L1995-021 and L1994-008 and dropped.
First to show the operator: M1997-021 with L1996-035. "My idea of understanding a business is that you've got a pretty good idea where it's going to be in ten years", set beside the letter's circle of competence whose size "is not very important; knowing its boundaries, however, is vital", and M1997-024: what would bother him is thinking he understands a business when he does not.
Surprising: risk is defined three ways in one answer and never as volatility (M1997-009, M1997-013, M1997-014), with overpaying called a risk of time rather than of principal (M1997-011); and Buffett narrating that being "incredibly price conscious" was "in some cases, a huge mistake" (M1997-003) in the same answer that warns one can pay too much for The Inevitables.
Brief: the helper's report pointers omit the Owner's Manual section PURCHASE-ACCOUNTING ADJUSTMENTS, which I read and rowed as part of the signed span; the report file ends in binary garbage after the last signed section. See the note's last section.

### 1997 PM - 2026-10-04
Rows: 107, all M (rule 49, test 33, definition 15, mistake-and-lesson 8, tension 2); Buffett 84, Munger 23. No letter or report rows (PM unit).
First to show the operator: M1997-148 with M1997-089. "The first filter ... whether it's a business we're going to understand ... if it passes through that, it's whether a company can have a sustainable edge", set beside Munger's bond-first opportunity-cost filter: half of all stocks fall to the government bond, and the survivors are ranked against each other.
Surprising: Buffett says outright that risk is handled by "a big discount from that present value calculated using the risk-free interest rate", and adds of the discounting "which Charlie says I never do anyway and he's correct" (M1997-126), settling M1996-083. Also Munger's account of nearly losing See's over $100,000 (M1997-104).
Brief: there is no way to correct a cross-reference typo in a row already appended (M1997-085); recorded in the note's last section.

### 1998 AM - 2026-10-04
Rows: 103 (L 40 from the FY1997 letter, R 1 from the 1997 report, M 62 from the morning session). Letter: test 20, rule 14, definition 3, mistake-and-lesson 3. Report: test 1. Meeting: rule 33, test 20, definition 4, mistake-and-lesson 4, tension 1; Buffett 49, Munger 13.
First to show the operator: M1998-044. "trying to identify the key variables in that particular business, and evaluating how predictable they were first, because that is the first step. If something is not very predictable, forget it", set beside M1998-042 ("policies at GEICO are unit cases at Coca-Cola") and Munger's M1998-045 that appraising any company at all is "attempting the impossible".
Surprising: the Confession (L1997-029), where Buffett says his stock-financed deals left owners worse off not because sellers misled him but because what he gave away was better than what he got; and the 1997 report's reprinted Owner's Manual is unreadable binary in this file, so no R rows came from it.
Brief: the helper found no signed sections in the 1997 report (its markers are `===== Title =====`); I located Acquisition Criteria and Owner's Manual by hand. Two cross-reference slips in appended rows are recorded in the note, since rows cannot be amended. See the note's last section.

### 1998 PM - 2026-10-04
Rows: 116, all M (rule 56, test 34, definition 18, mistake-and-lesson 6, tension 2); Buffett 94, Munger 22. No letter or report rows (PM unit).
First to show the operator: M1998-150 with M1998-151. Risk as "a go/no-go valve": what cannot be foreseen is "risky for us" and is given up, and they do not discount it "at 9 percent instead of 7 percent"; past the threshold of being quite certain, "the same discount factor tends to apply to everything".
Surprising: M1998-111, Buffett's admission that Berkshire had no present use for a retained dollar that would beat a dollar of value; M1998-084, the Frozen Corporation from Graham's class; and the due-diligence answer (M1998-175 to 177), where no bad deal in 30-some years would have been saved by it.
Brief: a speaker label the transcript appears to misattribute (line 1735, M1998-169) has no place in the speaker field; flagged in evolution_notes. See the note's last section.

### 1999 AM - 2026-10-04
Rows: 99 (L 36 from the FY1998 letter, R 3 from the 1998 report, M 60 from the morning session). Letter: test 16, rule 14, definition 5, mistake-and-lesson 1. Report: rule 3. Meeting: rule 30, test 26, definition 2, tension 1, mistake-and-lesson 1; Buffett 51, Munger 9.
First to show the operator: M1999-011 with M1999-052. Discount "at the long-term government rate" to compare 50 companies, "But we wouldn't pay that number after we discounted it back. We would look for appropriate discounts from that figure", and abroad "the same kind of a discount model in our mind of how much cash is this business going to generate over years and how much is going to have to be put into it".
Surprising: the letter's options method stated as a working rule, with the admission that the adjustment has changed actual buy and sell decisions (L1998-025, L1998-027); and Buffett's own confession that his 1998 trading lowered the year's result (L1998-019).
Brief: the FY1998 letter has no title line for pre-section rows, and a new note cannot be committed by pathspec until it is added. See the note's last section.

### 1999 PM - 2026-10-04
Rows: 80 (M only; Buffett 65, Munger 15). Kinds: rule 38, test 26, definition 12, mistake-and-lesson 4, tension 0.
First to show the operator: M1999-104 with M1999-105. "The moat and the management are part of the valuation process, in that they enter into our thinking as to the degree of certainty that we attribute to the stream of income", followed by the Wrigley questions on unit growth, pricing flexibility, market share and whether management will be "very bright with the cash that they develop, or being very stupid with it".
Surprising: the research method given as journalism with two named questions for competitors (M1999-130, M1999-131); the McDonald's sale costed at "a billion dollars-plus" (M1999-123); Munger's "at least it’s not an easy investment decision for us. And that’s what we’re looking for" (M1999-121).
Brief: no threshold for a tension the speaker reconciles at once; a same-batch cross-reference cannot carry an id (M1999-073 should read M1999-064). See the note's last section.

### 2000 AM - 2026-10-04
Rows: 111 (L 33 from the FY1999 letter, R 0 from the 1999 report, M 78 from the morning session). Letter: test 15, rule 13, definition 4, mistake-and-lesson 1. Meeting: test 37, rule 28, definition 9, mistake-and-lesson 3, tension 1; Buffett 68, Munger 10.
First to show the operator: M2000-002 with M2000-035. Aesop's bird in the hand "is an investment equation" missing only when the birds come out and the interest rate; in practice "a stream of cash that will be thrown off over, say, a 20-year period, that makes sense discounted at a proper interest rate, compared to what you’re paying today."
Surprising: the moat called "the primary criterion of a great business" (M2000-018) with three working tests of it (M2000-031, M2000-032, M2000-077); the idiot-nephew and genius pair on newspapers (M2000-071); the report's signed sections are a reprint, so no R rows, by repetition not absence.
Brief: the report carries a signed section (Purchase-Accounting Adjustments) the helper does not list; a reprinted report has no stated rule. See the note's last section.

### 2000 PM - 2026-10-04
Rows: 82 (M only; Buffett 69, Munger 13). Kinds: rule 37, test 21, definition 21, mistake-and-lesson 3, tension 0.
First to show the operator: M2000-104 with M2000-105. "We understand the product. We understand what it does for people. We just don’t know the economics of it 10 years from now", and the test that the industry's own leaders "would not want to put down on paper their predictions about where 10 companies you would choose in the tech field would be in 10 years, in terms of their economics."
Surprising: the maintenance spending figure given as "my best guess ... It could be 70. It could be 30" with owners "entitled" to it (M2000-144); options costed at about a third of the stock's value (M2000-080); the cigar-butt Berkshire purchase turned on an eighth of a point (M2000-116).
Brief: a same-batch lesson row cannot cite its mistake row's id; a narrated miss with no stated lesson has no kind. See the note's last section.

### 2001 AM - 2026-10-04
Rows: 93 (L 41 from the FY2000 letter, R 0 from the 2000 report, M 52 from the morning session). Letter: test 18, rule 14, definition 6, mistake-and-lesson 3. Meeting: test 26, rule 17, definition 7, mistake-and-lesson 2, tension 0; Buffett 37, Munger 15.
First to show the operator: L2000-021 with L2000-025. Aesop as three questions, the third being "the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)", answered to give "the maximum value of the bush"; then "Usually, the range must be so wide that no useful conclusion can be reached", and only occasionally do "very conservative estimates" show a price "startlingly low in relation to value."
Surprising: errors of omission counted only inside the circle of competence, with the eyedropper purchase as the worst kind (M2001-006, M2001-007); Munger's Belridge Oil omission priced at $200 million (M2001-005); EBITDA and "the tooth fairy" as a reading test (L2000-036). The report's signed sections are again a reprint, so no R rows, by repetition not absence.
Brief: the FY2000 letter file's first printed line is a table note, not a title; the matcher ignores case, so a capitalised first letter passed (M2001-031). See the note's last section.

### 2001 PM - 2026-10-04
Rows: 64 (M only; Buffett 49, Munger 15). Kinds: test 30, rule 28, definition 4, mistake-and-lesson 1, tension 1.
First to show the operator: M2001-080 with M2001-083. Risk "relates to ... the risk of permanent capital loss. And then the other risk is just an inadequate return on the kind of capital we put in. It does not relate to volatility at all"; and See's risk is determined "by looking at the business, and the competitive environment in which it operates."
Surprising: the three capital questions in order with the cost of a deal as "the second best deal" (M2001-082, M2001-084); the moat disagreement left open between the two speakers (M2001-069, M2001-070); the cigar butt defined and set aside for "a cheap, wonderful business" (M2001-113, M2001-114).
Brief: no test for where a general rule inside a political answer ends; an evolution-note misquote is not checked (erratum on M2001-109). See the note's last section.

### 2002 AM - 2026-10-04
Rows: 88 (L 29 from the FY2001 letter, R 0 from the 2001 report, M 59 from the morning session). Letter: rule 14, test 8, mistake-and-lesson 5, definition 2. Meeting: test 29, rule 21, mistake-and-lesson 6, definition 3, tension 0; Buffett 49, Munger 10.
First to show the operator: L2001-010 with L2001-012. "all of us in the industry made a fundamental underwriting mistake by focusing on experience, rather than exposure", and the confession that Buffett saw it beforehand: "I did, but I didn't convert thought into action. I violated the Noah rule: Predicting rain doesn't count; building arks does."
Surprising: the three underwriting principles stated as rules for the first time (L2001-007 to 009); "loss development" defined as an estimation error, with insurance accounting as "a self-graded exam" (L2001-021, L2001-022); the franchise test that everyone knows Gillette's margins and still "they can't knock off Gillette" (M2002-051); the report's signed sections are again a reprint, so no R rows, by repetition not absence.
Brief: a signed chairman's memo printed outside the four sections has no place under section 4; a reworded lead-in is not a word-for-word repeat. See the note's last section.
Correction to the entry above: the file prints "I did � but I didn't convert thought into action" (letter line 478, a dash lost in extraction); the entry's "I did, but" smoothed it. The row L2001-012 carries the printed text.

### 2002 PM - 2026-10-04
Rows: 73 (M only; Buffett 52, Munger 21). Kinds: test 31, rule 30, mistake-and-lesson 7, definition 5, tension 0.
First to show the operator: M2002-078. "a business or any economic asset is going to be worth what it produces in the way of cash over its lifetime", with investment as getting the money back "from what the asset itself will produce" and speculation as "what somebody else will pay you for it later on".
Surprising: the options afternoon, from "All options have value" to the two-farms test (M2002-109, M2002-111) and Munger's "an insane way to value the option" for long terms (M2002-112); the circle-of-competence test "if you have doubts ... it isn’t" (M2002-092); Buffett refusing a measure that "looks good on what they call a backtest" (M2002-120); See's failure to travel east (M2002-128).
Brief: no rule for a meeting passage that restates an earlier meeting row; the political test leaves the population asymmetry unrowed; no form for flagging a garble inside a quote. See the note's last section.

### 2003 AM - 2026-10-04
Rows: 104 (L 41 from the FY2002 letter, R 0 from the 2002 report, M 63 from the morning session). Letter: test 19, rule 18, mistake-and-lesson 3, definition 1. Meeting: test 28, rule 27, mistake-and-lesson 5, definition 3, tension 0; Buffett 53, Munger 10.
First to show the operator: M2003-034 with L2002-016. "when things go bad, all kinds of things correlate that no one ever dreamed correlated ... You were getting a concentration that would — you didn’t realize. And there’s nothing more deadly than unrecognized concentrations of risk", the meeting form of the letter's "a crisis often causes problems to correlate in a manner undreamed of in more tranquil times."
Surprising: the derivatives section as a set of tests (no exit, estimate-based earnings, asymmetric marking errors, downgrade collateral spirals; L2002-011 to 018); the four questions for auditors (L2002-037); a stated 10% pre-tax hurdle (L2002-020); "a wonderful business at a fair price, than a fair business at a wonderful price" rowed for the first time in this read (M2003-040); Buffett's own $8 billion Walmart mistake from stopping when the price rose (M2003-047). The report's signed sections are again a reprint, so no R rows, by repetition not absence.
Brief: same-line rows cannot be linked "by line span"; no rule for a meeting passage that restates the same year's letter; an elision over a printed page number. See the note's last section. The commit 8fc1e878 that carries headings 32-39 and the finished note went out under the previous batch's message ("headings 24-31"); history is not rewritten, so it is recorded here.

### 2003 PM - 2026-10-04
Rows: 92 (M only; Buffett 73, Munger 19). Kinds: rule 46, test 32, definition 9, mistake-and-lesson 5, tension 0.
First to show the operator: M2003-073. "if you compute intrinsic value as reflecting the discounted value of future cash flows, that should have, built into it, a calculation that allows for the fact that certain businesses are going to earn less in the future than now", read with the Dexter error that follows it, "a case of projecting into the future, conditions which were not going to exist in the future" (M2003-077).
Surprising: Munger's good-but-not-fabulous business whose profit "sits in the yard" (M2003-122); EBITDA looked at only "when you tell me you’ll make all the capital expenditures" (M2003-108); the open bankruptcy bid as an underpriced put (M2003-142); a 10 percent floor called "arbitrary" by Buffett and a guessed future opportunity cost by Munger (M2003-149, M2003-151); two personal-conduct rules rowed for the operator to judge (M2003-124, M2003-125).
Brief: no word on stated ways of acting outside investing; replies printed under the next question's heading. See the note's last section.

### 2004 AM - 2026-10-04
Rows: 90 (L 23 from the FY2003 letter, R 1 from the 2003 report, M 66 from the morning session). Letter: rule 9, test 9, mistake-and-lesson 3, definition 2. Report: test 1. Meeting: rule 34, test 26, mistake-and-lesson 6, definition 0, tension 0; Buffett 49, Munger 17.
First to show the operator: M2004-055. "I think you take all of the variables and calculate them reasonably conservatively. But you don’t try and put too much windage in at every level. And then when you get all through, you apply the margin of safety", read with M2004-056, skip companies that need extreme assumptions: "You only have to look at the ones that you feel capable of evaluating and you skip all rest."
Surprising: the first new R row since 1998, because the Owner's Manual's third principle dropped its 15% passage (R1996-004) for "we will be disappointed if our rate does not exceed that of the average large American corporation" (R2003-001); the Gen Re Securities confession that its troubles would "commandeer the capital and credit of Berkshire at just the time" it was most valuable (L2003-018); the Walmart mistake now at $10 billion with anchoring named (M2004-038, M2004-039); leverage as what stops a sound hand being played out (M2004-065).
Brief: no route for an unreconciled tension whose passage is already rowed as another kind; word-for-word repetition of a report reprint cannot be checked inside the whitelist. See the note's last section.

### 2004 PM - 2026-10-04
Rows: 62 (M only; Buffett 49, Munger 13). Kinds: rule 32, test 25, mistake-and-lesson 3, definition 2, tension 0.
First to show the operator: M2004-077 with M2004-078. "if the silent message had gone out to our employees that unless you write a lot of business, you’re going to lose your job, they would have written a lot of business", so underwriters are told writing no business never costs a job, and Berkshire "would rather suffer of having too much overhead" than teach a habit of writing bad business.
Surprising: the compensation answer's bar set at what "a chimpanzee could run the place" would earn, and "a lousy manager will always suggest" a low one (M2004-097); downgrade-triggered collateral called "just like a margin account" (M2004-107); IPOs treated as negotiated sales timed by informed sellers (M2004-100); four personal-conduct rules rowed for the operator to judge (M2004-123 to M2004-126).
Brief: no route for Berkshire's own administrative practices stated as rules; a general rule inside a political heading that instructs no investor. See the note's last section.

### 2005 AM - 2026-10-04
Rows: 64 (L 16 from the FY2004 letter, R 0 from the 2004 report, M 48 from the morning session). Letter: rule 6, test 6, mistake-and-lesson 4. Meeting: test 25, rule 22, definition 1, mistake-and-lesson 0, tension 0; Buffett 39, Munger 9.
First to show the operator: M2005-020. "you can almost measure the strength of a business over time by the agony they go through in determining whether a price increase can be sustained", read with the See's question that precedes it, "if we raised the price 10 cents a pound, would sales fall off a cliff?" (M2005-019).
Surprising: the letter's commodity test, "we wait in vain for \"I'd like a National Indemnity policy, please.\"" (L2004-003), and its two opposite routes for a commodity business (L2004-004, L2004-007); "I talked when I should have walked" (L2004-011); the zinc write-off as the arithmetic of simple propositions (L2004-002); Munger's "blood brother of evil" for headquarters' smooth-earnings expectations (M2005-037). The report's signed sections are again a reprint (the acquisition floor rose to $75 million), so no R rows, by repetition not absence.
Brief: no rule for a letter passage that restates only an earlier meeting or report row; an elision crossing the row speaker's own interjection. See the note's last section.

### 2005 PM - 2026-10-04
Rows: 66 (M only; Buffett 52, Munger 14). Kinds: rule 30, test 29, mistake-and-lesson 4, definition 3, tension 0.
First to show the operator: M2005-057. GM's and Ford's retiree commitments were signed partly because "they bore no accounting consequences at the time. It’s a terrible mistake for managers not to think in terms of reality rather than the accounting numbers", read with M2005-056, the same legacy cost seen as paying "several thousand dollars a ton more for steel than their competitors did".
Surprising: financial companies where even the current condition may be unknowable, not only the future (M2005-068); "It’s better to pay attention to something that is being scorned than something that’s being championed" (M2005-079), the first such line in the read; Munger's Elihu Root test of a director, "perfectly willing to leave the office at any time" (M2005-092); a superb legal business refused whole on moral grounds after a thousand-mile trip (M2005-097).
Brief: no route for a named third party's maxim quoted by a speaker (Peter Lynch, M2005-080); no instruction for a transcript gap (the heading 18 tape change). See the note's last section.

### 2006 AM - 2026-10-04
Rows: 68 (L 22, M 46, R 0; Buffett 63, Munger 5). Kinds: test 33, rule 24, mistake-and-lesson 7, definition 4, tension 0.
First to show the operator: L2005-014. The Fred Futile arithmetic: a fixed-price option holder's "self-interest is clear: He should skip dividends entirely and instead use all of the company's earnings to repurchase stock", and "fixed-price options give them capital that is free", a worked test of pay against owners' interests.
Surprising: "widening the moat" defined as daily, invisible acts, with the moat placed above short-term targets (L2005-010, L2005-011); "the time to act is now" after years of dithering over Gen Re Securities (L2005-009); suspicion of a growth rate's base year (L2005-003); "a long string of impressive numbers multiplied by a single zero always equals zero" (L2005-021); "the worst thing you could have would be a 100year history book" for hurricane pricing (M2006-030); a larger margin for buying Berkshire's own shares because "we might be less objective" (M2006-039). The report's signed sections are again a reprint, so no R rows, by repetition not absence.
Brief: no rule on whether a tension's conflicting statement must itself be a lesson (the $955 million currency conviction against M2006-038); a signed article listed on the contents page but absent from the extraction; a changed example inside a reprinted principle. See the note's last section.

### 2006 PM - 2026-10-04
Rows: 54 (M only; Buffett 43, Munger 11). Kinds: test 25, rule 23, mistake-and-lesson 3, definition 3, tension 0.
First to show the operator: M2006-061. "we thought they were the greatest of businesses, the ultimate bulletproof franchise. But it became apparent we were wrong [...] we’ve got to believe our eyes", read with Munger's "I once thought General Motors was a bulletproof franchise" (M2006-062) and Buffett's account of why owners resisted seeing it (M2006-064).
Surprising: "A strategic buyer is some guy that pays too much" (M2006-092) with funds marking businesses up to one another for the 20 percent slice (M2006-094); huge short interests "very often have been later revealed to be frauds or semi-frauds" (M2006-098); gambling as created risk against insurance as transferred risk (M2006-095); portfolio insurance as a "doomsday machine" built from individually intelligent procedures (M2006-055).
Brief: the two-speaker and elision conventions give different answers for a line-by-line exchange in which each speaker states a lesson; a misprinted speaker label in an unrowed passage has no row to carry the SPEAKER FLAG. See the note's last section.

### 2007 AM - 2026-10-04
Rows: 82 (L 19, M 62, R 1; Buffett 70, Munger 12). Kinds: test 49, rule 24, definition 7, mistake-and-lesson 2, tension 0.
First to show the operator: L2006-012. The test for the man who will run the money is not brains or a recent record but someone "genetically programmed to recognize and avoid serious risks, including those never before encountered", because "A single, big mistake could wipe out a long string of successes"; the meeting repeats it three times (M2007-015, M2007-050: "anything times zero is zero").
Surprising: the newspaper franchise taken apart in the letter, from "Survival of the Fattest" to insiders "blind or indifferent to what was going on under their noses" (L2006-007, L2006-008); the Walter Schloss hat test for skill against chance (L2006-018); the unrecognized "crowded trade" (M2007-035); a margin of safety never used to cover a business one cannot predict (M2007-022); a new principle 15 in the Owner's Manual reprint, "Otherwise, why do our investors need us?" (R2006-001).
Brief: no rule for earlier R rows that fail against a later reprint whose principles read unchanged; no rule for new text inside an otherwise repeated reprint. See the note's last section.

### 2007 PM - 2026-10-04
Rows: 77 (M only; Buffett 60, Munger 17). Kinds: rule 34, test 31, mistake-and-lesson 7, definition 5, tension 0.
First to show the operator: M2007-123. "Most stock deals, they think about what they’re getting and they don’t think about what they’re giving [...] if not extra value is being created, are you getting more than you’re giving?", with Dexter as the worked case, "2 percent of the present Berkshire Hathaway company" (M2007-124), and the accounts that never show it (M2007-125).
Surprising: "Volatility is not a measure of risk" with the farm bought at $600 an acre whose beta "shot way up" (M2007-075, M2007-076); the industry's most important figure missing from an oil company's glossy report as a "dishonest message" (M2007-082); a CEO's letter written by investor relations (M2007-083); "Areas don’t make opportunities; brains make opportunities" (M2007-065); Gutenberg proposing newsprint today (M2007-133).
Brief: section 5 admits only Buffett and Munger while section 6 offers `OTHER:<name>` (Joe Brandon at heading 17 not rowed); a check told as a joke (M2007-073). See the note's last section.

### 2008 AM - 2026-10-04
Rows: 81 (L 21, M 60, R 0; Buffett 69, Munger 12). Kinds: rule 42, test 29, mistake-and-lesson 7, definition 3, tension 0.
First to show the operator: L2007-010. "think of three types of "savings accounts." The great one pays an extraordinarily high interest rate that will rise as the years pass. The good one pays an attractive rate of interest that will be earned also on deposits that are added. Finally, the gruesome account both pays an inadequate interest rate and requires you to keep adding money", the summary of the letter's great, good and gruesome businesses (L2007-004 to L2007-009).
Surprising: a business that needs a superstar "cannot be deemed great", the brain surgeon against the Mayo Clinic (L2007-006); "A moat that must be continuously rebuilt will eventually be no moat at all" (L2007-005); two errors of omission confessed beside the taxonomy (L2007-011, L2007-012); a pension assumption and a double-digit return translated into the index levels they imply (L2007-017, L2007-019); Munger, "Diversification is for the know-nothing investor" with Buffett's LTCM case that leverage, not concentration, is the danger (M2008-049, M2008-051). The report's signed sections are again a reprint, so no R rows, by repetition not absence.
Brief: the new-text-in-a-reprint convention cannot always be applied, since the previous report is off the whitelist (the "existing units" clause in the Acquisition Criteria). See the note's last section.

### 2008 PM - 2026-10-04
Rows: 55 (M 55; Buffett 45, Munger 10). Kinds: rule 30, test 17, mistake-and-lesson 5, definition 3, tension 0.
First to show the operator: M2008-084. "it just doesn’t make any sense to us to be exposed to ruin and disgrace and embarrassment and — for something that’s not that meaningful. If we can earn a decent return on capital, you know, what’s an extra percentage point? [...] It cannot be farmed out." The afternoon's risk theme in one passage (with M2008-061, M2008-081, M2008-082).
Surprising: "if we can’t make a decision in five minutes, we can’t make it in five months" (M2008-086); conventional due diligence never caught one of his big mistakes (M2008-072); Munger's "good until reached for" assets (M2008-064) and CDS bettors with an incentive to cause the default (M2008-103); "a brand is a promise" with the penny-cheaper substitute test (M2008-075, M2008-076); pharma bought as a group, banks never (M2008-113, M2008-089).
Brief: section 5 says "states", but heading 15 gives a principle only by a refusal at a price (M2008-095); and nothing says whether one row may elide text another row quotes (M2008-099, M2008-100). See the note's last section.

### 2009 AM - 2026-10-04
Rows: 89 (L 27, M 62, R 0; Buffett 76, Munger 13). Kinds: test 46, rule 32, mistake-and-lesson 8, definition 3, tension 0.
First to show the operator: L2008-016. "The type of fallacy involved in projecting loss experience from a universe of non-insured bonds onto a deceptively-similar universe in which many bonds are insured pops up in other areas of finance. "Back-tested" models of many kinds are susceptible to this sort of error." With the mortgage-model failure and "Beware of geeks bearing formulas" (L2008-017, L2008-018), and at the meeting "if you need to use a computer or a calculator to make the calculation, you shouldn't buy it" (M2009-005).
Surprising: the Irish banks, "Nobody lied to me, nobody gave me any bad information. I just plain wasn't paying attention" (M2009-057); Munger's "copy what you please" beside Buffett's "we don't believe in outsourcing investment decisions" (M2009-043, M2009-011); "Science advances one funeral at a time" applied to finance (M2009-022); the trustee who would sell the Buffalo News (M2009-046); the report is again a reprint, so no R rows, by repetition not absence.
Brief: the letter restatement rule cannot be applied against letters the whitelist excludes (L2008-005); nothing requires reading an earlier row before citing it, and four errata followed. See the note's last section.

### 2009 PM - 2026-10-04
Rows: 44 (M 44; Buffett 34, Munger 10). Kinds: rule 22, test 19, definition 2, mistake-and-lesson 1, tension 0.
First to show the operator: M2009-088. The worst case for the insurance business is inflation so bad that customers, facing a bill that is frequent, "very visible" and "something they can’t give up", demand that the state take the business over.
Surprising: both partners admit they have been slow "every time" with a declining manager, "If we really love the guy, we’re really slow" (M2009-097); "there’s always a fee that accompanies it" (M2009-075); Munger doubts Buffett's own remedy for egregious pay, big investors being glass houses (M2009-093, M2009-095); "a lot of moats have been filling up with sand lately" (M2009-106).
Brief: nothing checks case and punctuation before a row is appended, and one slip passed (M2009-071); the exchange convention does not say how a label stands next to an elision (M2009-075). See the note's last section.

### 2010 AM - 2026-10-04
Rows: 67 (L 23, M 42, R 2; Buffett 54, Munger 13). Kinds: rule 41, test 18, mistake-and-lesson 6, definition 2, tension 0.
First to show the operator: R2009-002. Buffett rewrites a 1983 owner-related principle after a shareholder's question at the 2009 meeting: "I should have written the "five-year rolling basis" sentence differently", and the retention test becomes book value against the S&P plus a stock always above book; the reprint drops the earlier "we will pay them out" sentence (R1996-012 DRIFT).
Surprising: the stock-for-stock argument, "If we wouldn't dream of selling Berkshire in its entirety at the current market price, why in the world should we "sell" a significant part" (L2009-019), with the contingent-fee second adviser (L2009-022); "close to the line probably tells them it’s over the line" (M2010-034); Munger's "we celebrate wealth only when it’s been fairly won and wisely used" (M2010-036); an advantage others "know" and still do not copy (M2010-039).
Brief: a DRIFT cannot tell a deleted sentence from a reworded one without the earlier report, and I broke the whitelist (nine lines of the FY2008 report) to see; recorded in the note's last section.

### 2010 PM - 2026-10-04
Rows: 61 (M 61; Buffett 44, Munger 17). Kinds: rule 31, test 22, mistake-and-lesson 5, definition 2, tension 1.
First to show the operator: M2010-070. Buffett on the 498 of the S&P 500 that chose not to expense options, run by people "I would trust to be a trustee of my will", who said "I can’t do it if the other guy isn’t doing it"; with Munger's cure, a system in which "the people who are making the decisions bear the consequences" (M2010-072), and no budgets sent to the top because watched targets invite fudging (M2010-071).
Surprising: Munger's BYD tension, "we have always bragged about avoiding that ... And yet here we are", reconciled by "BYD had won its spurs" (M2010-095); a good business defined by the capital it needs, a good investment by the price (M2010-090); "your ability to price evaporates" when the advertiser no longer needs you (M2010-053); Kraft's pizza sale judged on $2.5 billion kept, not $3.7 billion paid (M2010-066).
Brief: nothing says whether a test may be folded into a tension row (M2010-095), or how a quote that opens mid-sentence is capitalised (M2010-066, a slip recorded). See the note's last section.

### 2011 AM - 2026-10-04
Rows: 64 (L 21, M 43, R 0; Buffett 53, Munger 11). Kinds: rule 29, test 24, mistake-and-lesson 5, definition 5, tension 1.
First to show the operator: L2010-002. The letter names a third, subjective element of intrinsic value, "the efficacy with which retained earnings will be deployed": "if the CEO's talents or motives are suspect, today's value must be discounted", because the outside investor "stands by helplessly as management reinvests his share".
Surprising: the See's ease-of-entry test stated whole, "if I had a hundred million dollars and I wanted to go in and take on See's Candy, could I do it?" (M2011-015); "to finish first, you must first finish" with leverage "addictive" and credit "like oxygen" (L2010-019, L2010-020); the 80/20 pay for investment managers against the old own-unit rule, rowed as a tension (L2010-016); Munger's "you don't want to make important decisions in anger" on Sokol (M2011-008). The report adds nothing new: all R-text repeats.
Brief: the FY2010 letter file carries the biennial managers' memo after the letter's signature; the brief does not say whether that is letter text. Read, not rowed; see the note's last section.

### 2011 PM - 2026-10-04
Rows: 59 (M 59; Buffett 38, Munger 21). Kinds: rule 35, test 19, mistake-and-lesson 4, definition 1.
First to show the operator: M2011-094. Buffett on Berkshire's first 15 years in reinsurance: "it looks way easier than it is", like accepting bets on boxcars, "you can win a lot of bets by giving the wrong odds, but if you keep do it long enough, you lose a lot of money", so "not fool yourself by whether you make money in a given year or two years or even three or four years."
Surprising: goodwill split cleanly, tangible returns for the business and full price for the allocator (M2011-060); the error of measuring every deal against the best one ever made (M2011-074); the option strike set at what the whole business would bring, rising yearly less dividends (M2011-067); Munger's "speed is overestimated" against Buffett's "huge advantage to be able to read fast" (M2011-075, M2011-076).
Brief: "one row under the speaker who speaks first" files the auction rule under Munger, whose quip came first, though Buffett stated it (M2011-071). See the note's last section.

### 2012 AM - 2026-10-04
Rows: 73 (L 20, M 53, R 0; Buffett 64, Munger 9). Kinds: rule 34, test 26, mistake-and-lesson 7, definition 6.
First to show the operator: L2011-013. The letter defines risk as "the reasoned probability ... of that investment causing its owner a loss of purchasing-power over his contemplated holding period", not beta: "Assets can fluctuate greatly in price and not be risky", and "a non-fluctuating asset can be laden with risk."
Surprising: the "double-barreled test" for a productive asset, keeping purchasing power in inflation while needing little new capital, which the regulated utilities fail (L2011-019); "The first law of capital allocation" (L2011-003); seven confessions in one unit, among them Energy Future's bonds, stock issued for BNSF and missing the internet's effect on GEICO (L2011-002, M2012-021, M2012-045); Munger's Gottesman story as a risk control rule (M2012-004). The report adds nothing new: all R-text repeats.
Brief: the helper points to a fifth report section, "INTRINSIC VALUE - TODAY AND TOMORROW", which is FY2010 letter text reprinted; the brief does not say how to treat it. Read, not rowed; see the note's last section.

### 2012 PM - 2026-10-04
Rows: 63 (M 63; Buffett 44, Munger 19). Kinds: rule 31, test 23, mistake-and-lesson 7, definition 2.
First to show the operator: M2012-093. Buffett on motivating managers who no longer need money: "I can’t put passion into somebody about their jobs, but I can certainly create a structure that will take that passion away from them. And Berkshire is a negative art in that way."
Surprising: the declining-business confession, three failed starts that built billions and "We’re not looking for an opportunity to do it again" (M2012-062 to M2012-064); Buffett's definition of "understand" as a five-to-ten-year fix on earning power and competitive position, not knowing what a business does (M2012-065); the Troy brewer in the vat of hot beer as the case against sigmas (M2012-084); Buffett saying he does not dwell on his own mistakes and fixed his philosophy at 19, beside Munger's "learning and learning and learning" (M2012-101, M2012-103).
Brief: the "speaker who states the lesson" rule does not settle an exchange where one speaker states the lesson narrowly and the other generally (M2012-078, M2012-098). See the note's last section.

### 2013 AM - 2026-10-04
Rows: 55 (L 15, M 40, R 0; Buffett 40, Munger 15). Kinds: rule 25, test 22, definition 3, mistake-and-lesson 3, tension 2.
First to show the operator: L2012-012. The FY2012 letter on why managers misfire in reinvesting: "they start with the answer they want and then work backwards to find a supporting rationale. Of course, the process is subconscious; that's what makes it so dangerous", with Buffett's own textile years as the case: "wishing makes dreams come true only in Disney movies; it's poison in business."
Surprising: the letter's dividend arithmetic, owners' own share sales beating a dividend when the company earns well and sells above book (L2012-013, L2012-014); declining newspapers bought at a very low multiple against the 2012 meeting's "stay away from declining businesses" (L2012-010, a tension the 2013 meeting settles as an exception); Buffett calling Singleton's issue-high, buy-back-low cycle a way of taking advantage of shareholders, against the Teledyne lesson drawn in 2011 (M2013-027). The report adds nothing new, and its reprint of R2009-001 drops the sentence on brief parent borrowing for a large purchase.
Brief: a reprint that drops a principle is to be recorded in the nearest R-row's notes, but this unit writes no R-row; recorded in the note only. See the note's last section.

### 2013 PM - 2026-10-04
Rows: 54 (M 54; Buffett 43, Munger 11). Kinds: rule 33, test 17, definition 2, mistake-and-lesson 2.
First to show the operator: M2013-076. On life insurers and callable mortgages: "We do not like giving options in this world ... you always want to accept an option; you never want to give an option."
Surprising: the purchase test stated without ratios, a five-to-ten-year view, confidence in it, and a big gap between price and value (M2013-045), beside the definition of a wonderful business for which one should "stretch a little" (M2013-059), which this session does not reconcile; Munger's "You really couldn’t create another railroad ... and you can create another airline ... That’s what we don’t like about it." (M2013-054); the IBM pension as "a big annuity company on the side" (M2013-075); Munger's "Good until reached for." (M2013-090).
Brief: no rule says how to carry speaker labels when an exchange row opens inside the first speaker's paragraph (M2013-058, M2013-069, M2013-094). See the note's last section.

### 2014 AM - 2026-10-04
Rows: 50 (L 14, M 36, R 0; Buffett 43, Munger 7). Kinds: rule 27, test 13, mistake-and-lesson 6, definition 4.
First to show the operator: L2013-012. The FY2013 letter's purchase test for stocks and whole businesses alike: "We first have to decide whether we can sensibly estimate an earnings range for five years out, or more. If the answer is yes, we will buy the stock (or business) if it sells at a reasonable price in relation to the bottom boundary of our estimate."
Surprising: "Some Thoughts About Investing" built on a farm and a building that never carry a price quotation, ending in a will that puts his wife's trust 90% in an index fund (L2013-005 to L2013-014, M2014-016); "Next time I'll call Charlie" as the EFH lesson (L2013-004); net option dilution worked by hand at the meeting (M2014-004); Munger's "pretty damn stupid when we bought See’s" and "ignorance removal" (M2014-026). The report adds nothing new; six old R-row drops got errata under the 2013 convention, and the pension memo and NFM pages are absent from the extraction.
Brief: the drop-erratum convention does not say whether it reaches long-standing drops that recur every year. See the note's last section.

### 2014 PM - 2026-10-04
Rows: 63 (M 63; Buffett 46, Munger 17). Kinds: rule 30, test 20, mistake-and-lesson 7, definition 6.
First to show the operator: M2014-086. Asked why a utility with negative cash after capital spending deserves capital, Buffett: "the return is not measured by the cash minus the increased capital investment we’re making. It’s measured by the operating earnings after depreciation", and Munger adds that the same numbers from a declining department store "we would just hate" (M2014-088).
Surprising: the forces toward dumb deals named one by one, animal spirits, strategy staff, bankers calling daily, against "We’re just eager to do a deal that makes sense" (M2014-076, M2014-077); the coal-CEO question, which competitor would you own for ten years and which would you short (M2014-057); "the last thing Berkshire should do is own a helmet company" (M2014-083); Munger on removing unnecessary costs as "a service to civilization" the same day he said great businesses need not squeeze the last nickel (M2014-093 against M2014-006).
Brief: the political test does not say whether an incentive principle carried inside a prosecution answer is rowed; dropped and listed. See the note's last section.

### 2015 AM - 2026-10-04
Rows: 53 (L 5, M 48, R 0; Buffett 40, Munger 13). Kinds: rule 30, test 14, mistake-and-lesson 7, definition 2.
First to show the operator: M2015-034. National Indemnity's claims man hid claims in a drawer, with no money at stake, only to escape Jack Ringwalt's teasing; Buffett's lesson: "you really have to be very careful in the messages you send as a CEO", and managers told never to disappoint Wall Street "start fudging figures to protect your predictions" (with M2015-033, hidden ego incentives, and Munger's Singleton story, M2015-032).
Surprising: the FY2014 letter proper yields only five rows (Tesco's dawdling, near-term needs in Treasuries, no borrowed money for investors); "I would rather be, you know, a hundred times too cautious than 1 percent too incautious" with the missed opportunities admitted (M2015-027); "almost any time we’ve issued shares, it’s been a mistake" (M2015-026); "competitive mode" printed for moat (M2015-016). The report adds nothing new; its six old R-row drops already carry errata, so none was added.
Brief: the two Golden Anniversary letters (letter file lines 1207-2178, about a third of the file) sit after the letter's signature; read whole, not rowed under the post-signature convention, every candidate passage listed by span for the operator to decide. See the note's last section.

### 2015 AM (supplement: the 2014 pair) - 2026-10-04
Rows: 41 (L 41; Buffett 25, Munger 16). Kinds: rule 20, test 14, mistake-and-lesson 6, definition 1. The FY2014 letter file's anniversary texts (lines 1207-2178), rowed on the parent session's ruling; the first Munger L-rows.
First to show the operator: L2014-012. "The intrinsic value of the shares you give in an acquisition must not be greater than the intrinsic value of the business you receive", with Berkshire's future CEO and board promised to calculate it, "You can't get rich trading a hundred-dollar bill for eight tens".
Surprising: how many of Buffett's own mistakes the text carries (Stanton's eighth of a point, NICO into Berkshire rather than BPL, See's nearly lost to caution, Dexter generalised: L2014-007, L2014-008, L2014-010, L2014-011); the three strengths of staying power and "madness to risk losing what you need in pursuing what you simply desire" (L2014-023, L2014-025); Munger's fifteen elements as a written constitution and his errors of omission put at $50 billion (L2014-031 to L2014-039, L2014-045). Munger's four factors of success, good luck among them, read and not rowed.
Brief: the letter restatement rule does not say whether it binds Munger's restatements of Buffett's letters; rowed with ids named. See the note's supplement section.

### 2015 PM - 2026-10-04
Rows: 51 (M 51; Buffett 34, Munger 17). Kinds: rule 30, test 17, mistake-and-lesson 3, tension 1.
First to show the operator: M2015-079. On buying more auto dealers in a good car year: "we would rather buy at a 10 or 12 times multiple of a bad year than buy at an eight times multiple of a good year. And that’s not necessarily the way that sellers think".
Surprising: Munger's "it’s dishonorable to stay stupider than you have to be" (M2015-093); the repurchase test as a partner's buyout at 120 or 80 percent of worth (M2015-074); "money is so cheap that it causes people to do almost anything on the asset side" with extra debt declined though "Logically, we probably should" (M2015-077); Dow Jones losing financial information for want of imagination, against Munger's "it’s hard to invent new — entirely new — modalities" (M2015-098, M2015-099, the only tension row).
Brief: the political clarification does not say what to do with a principle stated only of the political actor (tax writers, the euro, kleptocrat rulers); three such passages were left out and named. See the note's last section.

### 2016 AM - 2026-10-04
Rows: 52 (L 13, M 39, R 0; Buffett 43, Munger 9). Kinds: rule 19, test 26, mistake-and-lesson 6, definition 1.
First to show the operator: L2015-008. The FY2015 letter on the 10-K's risk factors: the important risks are usually well known, and what must be judged is "(1) the probability of the threatening event actually occurring; (2) the range of costs if it does occur; and (3) the timing of the possible loss."
Surprising: Buffett telling readers to subtract something for BNSF's inadequate depreciation (L2015-004) in the same letter that tells them to add back amortization; Noah's Law, "If an ark may be essential for survival, begin building it today" (L2015-010); Munger's "we buy a business an idiot can manage" turned into plan B, superior managers for businesses that need them (M2016-004, M2016-005); the hedge-fund bet read as the arithmetic of no-energy against hyperactive investors (M2016-035). The report adds nothing new; its six old R-row drops already carry errata.
Brief: one shared commit-message file let commit 6aee2130 go out under the previous message; recorded, not amended. See the note's last section.

### 2016 PM - 2026-10-04
Rows: 68 (M 68; Buffett 46, Munger 22). Kinds: rule 39, test 25, mistake-and-lesson 3, definition 1.
First to show the operator: M2016-066. On handshake diligence: "assessing whether he’s going to behave differently in the future in running that business than he has in the past when he owned it, that’s incredibly important, but there’s no checklist in the world that’s going to answer that", with the mistakes "always about making an improper assessment of the economic conditions in the future of the industry" (M2016-065).
Surprising: the GEICO pay grid, growth in policies in force and profit on seasoned business, because rewarding profits alone "It’d be the dumbest thing you could do" (M2016-084, M2016-085); Munger's "the worst anchoring effect, which is always your previous conclusion" (M2016-054); "if you’re not confused, you haven’t thought about it correctly" (M2016-079); cheap money making Buffett "pay a little more" against the 10 percent floor of M2003-149 (Tensions seen).
Brief: the political test does not say whether a principle about political conduct itself (M2016-107, no corporate public stands) is rowed; rowed. See the note's last section.

### 2017 AM - 2026-10-04
Rows: 80 (L 14, M 65, R 1; Buffett 64, Munger 16). Kinds: test 42, rule 28, mistake-and-lesson 6, definition 3, tension 1.
First to show the operator: M2017-056. A management's money mind shows in how it reasons about buying in its own stock: "it’s not a very complicated equation if you sort of think straight about that sort of a subject. But some people think that way and some don’t".
Surprising: the letter's buyback test, would a board buy out a partner in a private company without regard to price (L2016-002), and the two exceptions to cheap buybacks (L2016-003); "investing success to breed failure" (L2016-012); Salomon judging its scandal by "the dimensions of the fine" (M2017-005); Munger's "small statistical advantages, where in the old days it was like shooting fish in a barrel" (M2017-024, the unit's one tension row); the report's single new sentence, principle 11 covering controlled businesses only (R2016-001).
Brief: a report addition that repeats the same year's letter was rowed twice (L2016-010, R2016-001), and the .msg numbering does not say batch or commit. See the note's last section.

### 2017 PM - 2026-10-04
Rows: 38 (M 38; Buffett 28, Munger 10). Kinds: rule 18, test 15, mistake-and-lesson 4, definition 1, tension 0.
First to show the operator: M2017-091. Buffett's scuttlebutt question, put to the heads of ten companies in one industry: “If you had to go away for 10 years on a desert island and you had to put all of your family’s money into one of your competitors, which one would it be and why?”, then which one they would sell short.
Surprising: a business just lousy enough to recognise is safer to own than a slightly better one, "If it had been a little bit better, we would’ve hung on" (M2017-075); Munger's "Just because you’re right doesn’t mean you should always do it" (M2017-067); the Redding surgeons who "thought that what they were doing was good for people" (M2017-093); managers' personal-preference political giving from corporate funds called "a breach of trust" (M2017-103). Greg Abel speaks once (heading 36), not rowed.
Brief: whether "an earlier meeting row" reaches a restatement within the same session is not said; morning restatements rowed, a same-afternoon one named in notes. See the note's last section.

### 2018 AM - 2026-10-04
Rows: 58 (L 11, M 47, R 0; Buffett 51, Munger 7). Kinds: rule 30, test 26, mistake-and-lesson 1, definition 1, tension 0.
First to show the operator: M2018-041. Buffett, asked whether health care's barriers justify higher multiples for its incumbents: "though the system may have a moat against intruders, it doesn’t mean that everybody operating within the system has individual moats".
Surprising: the FY2017 letter's "The less the prudence with which others conduct their affairs, the greater the prudence with which we must conduct our own" (L2017-006) and its warning that a debt-financed deal at a high price still lifts per-share earnings (L2017-004); "a terrible mistake ... to measure their investment "risk" by their portfolio's ratio of bonds to stocks" (L2017-010); Buffett not pushing Goldman and GE "to the limit" in 2008 "because there really wasn’t anybody else around" (M2018-016); Munger, "decisions get made better if you eliminate the bureaucracy" (M2018-038). The FY2017 report adds no new signed text: the last report with signed sections by heading gives 32 MATCH and the same 17 DRIFT ids as FY2016.
Brief: the same-session restatement convention cannot reach a row already committed under write-early except by erratum, which is reserved for wrong notes. See the note's last section.

### 2018 PM - 2026-10-04
Rows: 44 (M 44; Buffett 28, Munger 16). Kinds: rule 22, test 17, mistake-and-lesson 4, definition 1, tension 0.
First to show the operator: M2018-055. Asked by an eight-year-old why Berkshire bought BNSF rather than capital-light businesses, Buffett: capital-intensive businesses are "the second-best choice, still a good choice", taken only because "we can’t get more money deployed in capital-light businesses at prices that make sense to us", and "we have not foregone any opportunity" in the first for them.
Surprising: Munger naming love of newspapers as the likely cause of the miscalculation (M2018-057) and owning the 401(k) lapse that delegation produced (M2018-066); "if I think something will be a miracle, I tend not to bet on it" beside "I underestimated him" (M2018-085, M2018-087); a stock avoided because of the inference that inside information passed (M2018-048); "whenever you hear a theory described as elegant, watch out" (M2018-081). Greg Abel speaks twice in the formal meeting, not rowed.
Brief: the parent's same-session clarification leaves "adds something new" undefined and sits against the 2002 PM rule that meeting restatements are rowed to count recurrence. See the note's last section.

### 2019 AM - 2026-10-04
Rows: 48 (L 4, M 44, R 0; Buffett 41, Munger 7). Kinds: rule 22, test 17, mistake-and-lesson 6, definition 3, tension 0.
First to show the operator: M2019-024. Munger, with Buffett supplying the evidence, on missing Google: “We could see in our own operations how well that Google advertising was working. And we just sat there sucking our thumbs”, while Amazon is excused as the work of “kind of a miracle worker”.
Surprising: the FY2018 letter retiring book value as the yardstick (L2018-001) and Buffett admitting he preached doom over deficits for years (L2018-004); a stand-alone insurer able to pay any claim is “not a very good business” and its reinsurance may fail in the worst case (M2019-025); Berkshire paying every claim of two failed small insurers as the root of trust in its word (M2019-027, M2019-033); private-equity IRRs leaving out the idle committed money (M2019-021); “you can pay way too much for a growing brand, probably be easier to be sucked into that” (M2019-043). The FY2018 report reprints no signed section at all. Ajit Jain answers heading 30, not rowed.
Brief: nothing says what to do when a report omits the whole Owner's Manual; the helper reports 49 DRIFT and the drop-erratum convention would fire on every R-row. No erratum written. See the note's last section.

### 2019 PM - 2026-10-04
Rows: 43 (M 43; Buffett 35, Munger 8). Kinds: rule 23, test 15, mistake-and-lesson 4, definition 1, tension 0.
First to show the operator: M2019-076. Buffett: "we don’t have any formula that evaluates risk", and a staff "would try and figure out what I wanted the answer to be", so with a 15 percent hurdle rate the projects "all come out at 15.1 or 15.2"; paired with M2019-077, the first question is "are you reasonably sure that you know what you’re doing?"
Surprising: Buffett saying he "would rather own an index fund than carry Treasury bills" and that a successor may do it (M2019-060); Munger's "two or three stocks" against the finance schools (M2019-080); a seller asking to be paid for earnings created by unexpensed options, called "lying about our accounting" (M2019-078).
Brief: the 2018 same-session restatement rule leaves "adds a new test" to the reader's judgment; two rows (M2019-083, M2019-084) rest on that judgment. See the note's last section.

### 2020 AM - 2026-10-04
Rows: 28 (L 10, M 18, R 0; Buffett 28). Kinds: rule 13, test 10, mistake-and-lesson 4, definition 1, tension 0. The FY2019 report prints no signed section; Munger absent and Abel silent in Part 1.
First to show the operator: M2020-017 with M2020-018. Buffett on the airline sale: "it turned out I was wrong about that business because of something that was not in any way the fault of four excellent CEOs"; a 20 to 40 percent price fall does not make an owner poor, "We felt we were poor, in terms of what had actually happened to those airline businesses, just as if we owned a hundred percent of them."
Surprising: the FY2019 letter on director pay, "It's the cocker spaniel that gets taken home" and the fee-dependent director classed as "independent" (L2019-007); the will's "safe" Treasury course as protection for the fiduciary rather than the beneficiary (L2019-004); cash held against the chance that "the Fed will not have a chairman that acts like that" (M2020-016).
Brief: the dispatch's ABEL speaker value conflicts with the standing brief's 2025-only rule for Abel and Jain; see the note's last section.

### 2020 PM - 2026-10-04
Rows: 32 (M 32; Buffett 32). Kinds: rule 15, test 11, definition 4, mistake-and-lesson 2, tension 0. Munger absent; Greg Abel answers throughout and is not rowed (2025-only rule); his maintenance-capex answer at heading 20 and his "no cushion" buyback remark at heading 28 are listed in the note.
First to show the operator: M2020-047. Buffett on not buying back Berkshire after a 30 percent fall: "There could be a price, relative to value at the time, not relative to what it was worth a year ago", because "Berkshire is worth less today because I took that position than if I hadn’t"; the repurchase is weighed against "the option value of money".
Surprising: Treasury bills called "a terrible investment over time" yet held because "the rest of the world may have stopped" (M2020-039); "If you own oil, you should only own oil, if you expect these prices to go up significantly" (M2020-035); the bank question asked for clues to a true banker and got none (listed under Rows).
Brief: no rule for Buffett adopting an Abel point inside his own answer (M2020-045); see the note's last section.

### 2021 AM - 2026-10-04
Rows: 37 (L 8, M 29, R 0; Buffett 35, Munger 2). Kinds: rule 16, test 15, mistake-and-lesson 4, definition 2, tension 0. The FY2020 report prints no signed section; its appendix reprints the FY2019 letter's insurance section (read, not rowed). Abel and Jain speak and are not rowed.
First to show the operator: L2020-001. Buffett on the $11 billion PCC write-down: "I was simply too optimistic about PCC's normalized profit potential", right that it "would, over time, earn good returns on the net tangible assets", but "wrong in judging the average amount of future earnings and, consequently, wrong in my calculation of the proper price to pay for the business."
Surprising: Buffett has "never recommended Berkshire to anybody ... no matter what it was selling for" (M2021-009); stocks bought "where ... we don’t have any insights", better than Treasury bills but uncomfortable at size (M2021-029); the chewing-tobacco business declined though "probably the best business we’ve ever seen" (M2021-013), beside "if you expect perfection ... in companies, you’re not going to find it" (M2021-012).
Brief: section 5's tension-row rule and the 2004-2005 no-duplicate convention leave no case for a tension row between two statements rowed in the same batch; see the note's last section.

### 2021 PM - 2026-10-04
Rows: 36 (M 36; Buffett 29, Munger 7). Kinds: rule 18, test 13, mistake-and-lesson 3, definition 2, tension 0. Abel and Jain answer at ten headings and are not rowed; the formal meeting and two shareholder proposals yield nothing rowable.
First to show the operator: M2021-051. Buffett on "the myths that people have about their own organization": repeated to analysts every couple of months they become "the catechism", a successor "can’t" say his predecessor was wrong, "and then he starts repeating it. And it leads to enormous errors." Munger adds that the speaker comes to believe it (M2021-052).
Surprising: "the number one risk factor ... is that this business gets the wrong management", never listed in a prospectus (M2021-042); the corporate tax as the government's "Class AA stock", passed to customers only in a utility (M2021-035); Buffett agreeing with Munger that turnover is "still too much" (M2021-062).
Brief: three passages state a mechanism that fits none of the five kinds and were rowed under the nearest one; see the note's last section.

### 2022 AM - 2026-10-04
Rows: 56 (L 11, M 45, R 0; Buffett 47, Munger 9). Kinds: rule 26, test 19, definition 5, mistake-and-lesson 5, tension 1. The FY2021 report prints no signed section; its appendix reprints the FY2019 insurance section a second year, and the Greg Abel Letter (A-3) is signed by Abel (both read, not rowed). Abel and Jain speak and are not rowed.
First to show the operator: M2022-039. Buffett on the textile mill: the manager "was 100% honest with me in every way ... And if he’d been a jerk, it would have been a lot easier. I would have probably thought differently about it. But we just stumbled along for a while", and he bought a second mill years later; beside Munger's "an absolutely hopeless hand" (M2022-038).
Surprising: State Farm, a mutual from which "nobody’s really gotten rich", as the winner that "refutes" the incentive teaching (M2022-023, the unit's one tension row); "It is also far easier to exit from a mistake when it has been made in the marketable arena" (L2021-001); a long-term owner base limiting profitable buybacks, and preferred anyway (L2021-007).
Brief: the letter restatement rule (rowed only if it adds a new test or rule) and the 2021 mechanism convention point different ways for L2021-006; see the note's last section.

### 2022 PM - 2026-10-04
Rows: 39 (M 39; Buffett 30, Munger 9). Kinds: rule 19, test 18, definition 2, mistake-and-lesson 0, tension 0. Abel and Jain do not speak. Two speaker-label faults: no label for Buffett at heading 5 (rowed BUFFETT, flagged) and a Munger label over Buffett's words at heading 9 (kept MUNGER, flagged).
First to show the operator: M2022-055. Buffett: "I’ve got 360,000 people out there, and they know whether I’m lying or not ... if you have a culture of lying, the processes really don’t — they just disappear ... if you set the wrong example at the top, you’ve got a real problem."
Surprising: decent neighbours who would return a lost wallet, "But they’d play games with any number that came to them" (M2022-070); a buyback's absolute test, "if it isn’t intelligent on an absolute basis, you also don’t do it" (M2022-083); Munger's claim letter, raising the stakes tenfold on both sides to get a $12,000 claim paid (M2022-075).
Brief: the speaker convention covers a misprinted label but not a missing one; see the note's last section.

### 2023 AM - 2026-10-04
Rows: 67 (L 21, M 46, R 0; Buffett 57, Munger 10). Kinds: rule 32, test 28, definition 2, mistake-and-lesson 5, tension 0. The FY2022 report prints no signed section; its appendix reprints the FY2019 insurance section a third year (read, not rowed). Thirteen of the letter rows are Munger's thoughts printed by Buffett, rowed under Buffett. Abel and Jain speak and are not rowed.
First to show the operator: M2023-045. Buffett: "it’s hard to judge successor management in a really good business. Because if they don’t show up at the office, it’ll keep working for a long time ... Some would be better off not managed hardly at all. Others really need help, but they got a lousy business."
Surprising: "We are understanding about business mistakes; our tolerance for personal misconduct is zero." (L2022-001); Buffett grading most of his capital-allocation decisions "no better than so-so" (L2022-003); Munger on the commitment effect, "the act of deciding that an investment is already good, they get to thinking it’s better than it is" (M2023-037).
Brief: a question title printed without its `### 12.` marker (line 287) is not covered by the heading convention; see the note's last section.

### 2023 PM - 2026-10-04
Rows: 60 (M 60; Buffett 49, Munger 11). Kinds: rule 33, test 22, definition 1, mistake-and-lesson 4, tension 0. Abel and Jain do not speak. One speaker-label fault: Buffett's Rockford story opens under a doubled Munger label (lines 1229-1233), flagged in M2023-056.
First to show the operator: M2023-103. Buffett: "if you’re a bank ... you’ve got to pay attention to whether they’ve gotten out of whack in terms of the value of what they own and what can be demanded of them tomorrow morning ... And if we had all of our money that could be demanded from us tomorrow morning, we’d have to behave a lot differently than Berkshire does."
Surprising: the First Republic test, "you could look at their 10-K ... You don’t give options like that ... it was in plain sight" (M2023-049); Buffett calling his own staged purchase of Pilot, with the last 20% at the seller's option, "always an unintelligent way of structuring something" (M2023-060); Munger on his year at US Steel, "to be that ignorant as I was at that age, it was a sin" (M2023-106).
Brief: the political test does not say how to count a parallel line said only of the political actor when the other speaker gave the general form; see the note's last section.

### 2024 AM - 2026-10-04
Rows: 50 (L 13, M 37, R 0; Buffett 50). Kinds: rule 25, test 18, definition 0, mistake-and-lesson 6, tension 1. The first meeting without Munger. The FY2023 report prints no signed section; its page 18 reprints the FY2019 insurance section a fourth year (read, not rowed). Abel and Jain speak at twelve headings and are not rowed. `### 19.` is missing; its title (line 1129) was treated as a heading boundary under the parent's instruction.
First to show the operator: M2024-025. Buffett: "we haven’t had a history of being very tough on people that coasted ... And Greg will do something about it. And Charlie and I wouldn’t have. Not because we didn’t know it should be done, but because we were doing so well ourselves."
Surprising: "our low costs have masked the fact that ... we could do without progressing as much as we should’ve in the matching of rate to risk" (M2024-014); the letter favouring "the rare enterprise that can deploy additional capital at high returns", against L2009-012 (L2023-002, the unit's tension row); "I did not anticipate or even consider the adverse developments in regulatory returns" (L2023-011).
Brief: the citation rules do not say how to cite a range of ids, and the heading-boundary instruction is not yet in the prompt file; see the note's last section.

### 2024 PM - 2026-10-04
Rows: 35 (M 35; Buffett 35). Kinds: rule 23, test 8, definition 2, mistake-and-lesson 2, tension 0. Nine rules are personal conduct, most in the last third (luck, wills, heroes, kindness). Greg Abel speaks at seven headings and is not rowed; Ajit Jain does not speak. Most apostrophes are missing from the printed text and are kept so.
First to show the operator: M2024-040. Buffett: "The responsibility has been with me, and I farmed out some of it. And I used to think differently about how that would be handled. But I think the responsibility should be that of the CEO ... we do not want to try and have, you know, 200 people around that are managing a billion each. It just doesnt work."
Surprising: on BNSF, "its worked out very well, but its because we were putting out capital in 2008 and 09. And if we put money in anything, wed have made a lot of money" (M2024-057); "We never worried about missing something we didnt understand" (M2024-049); the Pilot question asking for lessons got none (heading 11).
Brief: the same-session restatement convention asks the first row to name a restatement that write-early has not yet read, and the message-file numbering does not cover a commit carrying two batches; see the note's last section.

### 2025 AM - 2026-10-04
Rows: 41 (L 10, M 31, R 0; Buffett 37, Abel 2, Jain 2). Kinds: rule 28, test 11, definition 1, mistake-and-lesson 1, tension 0. The FY2024 letter is Buffett's last as CEO; the FY2024 report prints no signed section. Six rows are personal conduct. The first meeting in which Abel's and Jain's answers are rowed.
First to show the operator: L2024-003. Buffett: "That taboo, implying managerial perfection, always made me nervous [...] if you start fooling your shareholders, you will soon believe your own baloney and be fooling yourself as well."
Surprising: a decade without income tax at "a venerable pillar of American industry" as "a blinking yellow light" (L2024-005); "This approach encourages caution but does not ensure foresight" (L2024-008); "You never reach a final answer in this business – you reach a point of action that you take" (M2025-028); the yen funding called "not a policy of ours" (line 275) against L2023-007.
Brief: it does not say whether the 2021 rule listing Abel's and Jain's lines under Rows survives into 2025, when they are rowable; see the note's last section.

### 2025 PM - 2026-10-04
Rows: 26 (M 26; Buffett 20, Abel 6, Jain 0). Kinds: rule 17, test 7, definition 1, mistake-and-lesson 1, tension 0. The last unit of the read. Six rows are personal conduct. Jain does not speak this afternoon; the session ends with Buffett announcing Abel as CEO from year-end.
First to show the operator: M2025-040. Abel: "You earn a very set return for taking on a very defined risk associated with that asset, and this has gone well beyond that. We don’t earn the type of returns nor can you earn a large enough return to take on these risks."
Surprising: "If you’re in something where you’re going to lose, the big thing to do is quit" (M2025-041); "It’s easier to do stupid things with other people’s money than it is with your own" (M2025-042); balance sheets read over eight or ten years before the income account (M2025-032); "it’s easier for an organization to see its quality move downward than it is upward" (M2025-055).
Brief: the 2014 PM rule gives no test for a general form addressed to a political actor against a remark made only of one; see the note's last section.
