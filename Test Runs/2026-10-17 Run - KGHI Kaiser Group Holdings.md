# Company Run: Kaiser Group Holdings, Inc. (OTC, no exchange listing: KGHI), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (eaddc90f): not held; `PORTFOLIO.md` has no line for KGHI or Kaiser.*

**Dispatched run.** Written by a dispatched analyst under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the
brief's three stated departures: (1) the lines of evidence were derived by the analyst from the filings; (2) the
competitors were to be taken from the rivals the company's own filing names; (3) the company stopped filing with the SEC
in 2008, so the primary document for the present is the company's own report to stockholders, recorded by document and
date in place of an accession number.

**Contamination, declared and not used.** (a) Before the file was written I ran a directory listing of `Test Runs/`
filtered for "KGHI" or "kaiser", to check the run file name was free; it returned nothing. Under the blind rule a filtered
listing counts as a search, so it is declared; nothing was seen. (b) The session context showed the repository's recent
commit subjects (other companies' runs and folds, none about this name) and the dispatching session's lock file name in a
directory listing. (c) The session context carried memory index lines about the queue's state in general (no line names
this company). (d) `python tools/run.py KGHI` printed a v4 verdict word ("UNRESEARCHED, not UNKNOWABLE"); by Part VII only
its arithmetic lines are read, and it printed none. None of this is used.

**Lines of evidence chosen, and why (departure 1).** From the last 10-K (fiscal 2006, filed 2007-03-30, accession
0001104659-07-024333), Item 1A and Item 7, and from the company's own statements to stockholders after deregistration:
(1) what the company owns and earns from, because the 10-K says it has "only a limited number of activities, assets and
liabilities" and the question is what replaced them; (2) the Kaiser-Hill Rocky Flats contract, its fee and its closeout,
because it was the only source of earnings; (3) the Nova Hut claims and the IFC arbitration, the only large contingent
asset or liability; (4) the captive insurer (Monument Select Insurance Company) and its run-off; (5) cash and its uses:
the 2006 dividend, the odd-lot tender, the buyback programme and the investments made from 2009; (6) management pay and
related-party dealings, from the 2007 proxy and the later statements' related-party note; (7) litigation; (8) whether any
current report exists at all, because the brief and the 8-K of 2008-02-28 both point to the company's website.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.0001 a share, "No trades", "Market closed", read 2026-10-17 from TradingView's KGHI page (an aggregator,
  flagged under operator rule 5; it gives no date of last trade). OTC Markets' own quote endpoints returned a
  maintenance page on 2026-10-17; its company record shows tier code "EM" on the SEC-filings list (read as the Expert
  Market tier; not confirmed on a quote page) and **zero** financial reports posted (`financial-report` endpoint,
  `totalRecords: 0`). The quote is therefore not a usable price for arithmetic; it is recorded, not relied on.
- **Shares:** no current cover page exists. The last figure from the company itself: **1,320,155 shares outstanding**
  at 2012-09-30 (1,791,577 issued less 471,422 in treasury), consolidated balance sheet, *Kaiser Group Holdings, Inc. and
  Subsidiaries, Consolidated Financial Statements, September 30, 2012 and 2011 (unaudited)*, posted on the company website
  www.kaisergroup.com/docs/KGHFinancialStatements9-30-2012.pdf (retrieved from the Internet Archive's capture of
  2013-02-28; the live site no longer exists). `python Screens/cover_shares.py KGHI` returned "NOT AN SEC REGISTRANT in
  the live ticker file". The last SEC figure: the odd-lot tender bought 6,313 shares, "0.35%" of the shares then
  outstanding (8-K/A, 2008-01-15, accession 0001104659-08-002854).
- **Market cap:** at the aggregator's quote and the 2012 share count, about $132 (1,320,155 x $0.0001); TradingView
  prints the same $132. A figure built on a 14-year-old share count and a quote with no trades; recorded, not used.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2006 (2007-03-30, 0001104659-07-024333), Items 1A, 6, 7 and the statements;
  10-K FY2005 (2006-03-28, 0001104659-06-019740), for the 2004 balance-sheet figures in its selected data; 10-K/A FY2006
  (2007-04-30, 0001104659-07-033375); 10-Q for 2007-09-30 (2007-11-13, 0001104659-07-082552); DEF 14A (2007-09-26,
  0001104659-07-071331), pay and holders; SC 13E3 (2007-10-25, 0001047469-07-007976) and amendment (2007-11-30,
  0001047469-07-009627); 8-Ks of 2007-11-05 (0001104659-07-079810), 2007-11-30 (0001104659-07-086208), 2007-12-13
  (0001104659-07-088561), 2007-12-21 (0001104659-07-090575), 2008-01-04 (0001104659-08-000656), 2008-01-11
  (0001104659-08-002066), 2008-01-15 (0001104659-08-002854), 2008-02-28 (0001104659-08-013840); Form 15
  (2008-02-28, 0001104659-08-013837). **After deregistration** (departure 3; each is the company's own document, by
  name and date, retrieved from the Internet Archive's captures of www.kaisergroup.com because the site is gone):
  statements to stockholders for 2008-03-31, 2008-06-30, 2008-09-30, 2009-09-30, 2010-03-31, 2010-06-30, 2010-09-30,
  2011-03-31, 2011-06-30, 2011-09-30 and **2012-09-30, the latest the record holds**; the audited annual statements for
  2007, 2008, 2009 and 2010 were captured as scanned images with no text layer and were not read (their year-end
  balance sheets are read instead as the prior-year column of the next March or September statement); press releases
  2008 to 2011, including the Bally investment (2009-09-03) and the Alabama Aircraft acquisition (2011-09-12); the
  "NOVA HUT NOTICE" (after 2013-06-24).
- **Where I looked for a current report, and what is there.** (1) www.kaisergroup.com now resolves to
  `https://www.kaisergroup.com/en-GROUP`, the site of KAISER GmbH & Co. KG of Schalksmuehle, Germany, an unrelated
  electrical-installation maker. (2) The Internet Archive's captures of the company's financial-statements page list,
  in October 2015, statements through "December 31, 2014 and 2013", a "2015 Annual Stockholders Meeting" document and a
  "Kaiser Announcement"; **none of those documents, nor the 2011, 2012 or 2013 annual statements, was ever captured**
  (each request returned 404 from the archive); from 2016 the company's homepage captures read "Page cannot be
  displayed" and then a bare domain page. (3) OTC Markets: zero financial reports, no disclosure endpoint. (4) EDGAR:
  nothing after the Form 15. (5) A web search found aggregator profiles only, and two press items not from the company:
  a 2015 report that the Birmingham hangar complex "previously operated by Kaiser Aircraft Industries" was vacant, and a
  2018 report that Kaiser cut its workforce and space there in 2017 (both third-party, flagged, not relied on).
  **Plainly: no annual report or financial statement from the company dated after 2012-09-30 could be found.**
- **One figure cross-checked against the filed statement:** total shareholders' equity at 2006-12-31, $66,117 thousand,
  appears both in the FY2006 10-K balance sheet and in its Item 6 selected data (0001104659-07-024333); the 2011
  year-end column of the 2012-09-30 statement ($33,107 thousand) agrees with the treasury-stock and retained-earnings
  lines beneath it.
- `python tools/run.py KGHI`: returned "KGHI: not an SEC filer" and no arithmetic lines.

### The balance sheets, eight year-ends and the last interim, before any income account **[M2025-032]**
(USD thousands; from the 10-Ks for 2004 to 2006 and from the prior-year column of the company's own statements after;
2004 from the FY2006 10-K's selected data, which gives only the three lines shown.)

| Date | Total assets | Cash and equivalents | Investments (non-marketable, at cost) | Kaiser-Hill investment | Total liabilities | Equity | Shares outstanding |
|---|---|---|---|---|---|---|---|
| 2004-12-31 | 72,714 | n/s | n/s | n/s | 26,909 long-term (preferred) | 27,545 | n/s |
| 2005-12-31 | 122,024 | 14,633 | 0 | 87,310 | 42,913 (tax payable 32,315) | 79,111 | 1,787,640 |
| 2006-12-31 | 86,499 | 55,779 | 0 | 2,278 | 20,382 (dividend payable 10,745) | 66,117 | 1,790,890 |
| 2007-12-31 | 67,493 | 48,553 (+ CDs 3,433, securities 8,865) | 0 | 897 | 2,027 | 65,466 | 1,792,890 |
| 2008-12-31 | 63,566 | 53,876 (+ CDs 3,259) | 0 | 878 | 1,864 | 61,702 | 1,692,100 |
| 2009-12-31 | 53,614 | 30,526 (+ CDs 4,278, securities 5,034) | 11,700 | 886 | 1,251 | 52,363 | 1,412,431 |
| 2010-12-31 | 50,879 | 12,749 (+ CDs 4,330, securities 5,572) | 27,158 | 876 | 373 | 50,506 | 1,412,431 |
| 2011-12-31 | 36,268 | 2,273 | 28,919 | 785 | 3,161 | 33,107 | 1,320,155 |
| 2012-09-30 | 24,387 | 5,319 | 16,377 | 786 | 4,613 | 19,774 | 1,320,155 |

*n/s: not stated in the document read.*

What moved and why. The balance sheet is the record of one contract being collected and then spent. The Rocky Flats fee
arrived as the Kaiser-Hill investment (87.3 million at 2005), turned to cash and a tax liability in 2006, and paid a
$6.00 dividend (10.7 million payable at 2006). From 2007 nothing replaced it: there are no receivables or inventories of
size until the aircraft unit appears in 2011, and equity falls every year from 79.1 million (2005) to 19.8 million
(2012-09-30). Cash went into treasury stock (95,477 shares by 2008, 471,422 by 2012) and, from 2009, into
non-marketable investments carried at cost: a stake in Bally Total Fitness (11.7 million in 2009, 22.7 million paid in
all, written down 8.3 million in 2011 and 3.0 million in 2012), hedge-fund partnerships (Paulson Gold, Somerset,
Tennenbaum Opportunities Fund VI). By 2012 the non-marketable investments were two thirds of total assets, carried at
cost "net of impairment", so what most of the assets are worth is among "what they can’t say" **[M2025-032]**. What the
figures say plainly: the company has had no business that earns since the closeout of one government contract, and its
equity has been shrinking by losses and buybacks for seven years. What they cannot say: anything after 2012-09-30.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this if the market closed for five years **[M1997-109]**, or if they said "We’re just going to delist the stock" and open it again in twenty years
**[M1996-067]**? Here the market has in effect closed already: no
trades, no filings, no posted report for more than a decade. The question the foundation asks is then the whole
question: what does the business produce for its owner, and the record does not say. The analyst's habits: "destroy our
previous ideas" **[M2016-054]**, and look for "what’s wrong" and "what you’re missing" **[M2025-013]**. A quoted price of
a hundredth of a cent and a 2012 book value near $15 a share invite the reading "cheap"; that is a reading of the
quotation, not of a business, and the foundations rule it out of the analysis. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the company's last 10-K says "We do not have a significant business plan beyond Kaiser-Hill" and
"We currently have no active operations"; (2) every operating year read, 2004 to 2012, shows an operating loss; (3) the
company stopped publishing anything retrievable after 2012, its website died in 2016, and its domain now belongs to an
unrelated company; (4) the one operating business it bought (aircraft maintenance, 2011) lost money in every period read,
and third-party reports say its hangar was vacant by 2015.

## THE STANDING RULE
Owning this risks nothing beyond what is paid, if it is paid for in cash and not on margin **[L2014-005]**; the risk the
rule names is the buyer's, "what can really go wrong with this place" **[M2012-081]**, and at a quoted market value near
$132 no position of any size could be built. The rule is not engaged; the question is whether there is anything to buy.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**; "our definition of understanding is thinking that
we have a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]** ("asses"
is the transcript's spelling). The decision is made from the documents: "if you can’t make a decision on something like
PetroChina off the figures, forget about going further" **[M2008-069]**, and the PetroChina case was "right there in black
and white, in a report that anybody can get" **[M2005-015]**. Test 3: "do I understand enough about this business so that
the financial statements will tell me the information that’s useful to me in making a judgment about what the future
financial statements are going to look like" **[M2008-033]**.

**The key variable, and whether it can be known.** For a holding company the first variable is what it holds. The Q1
holding-company paragraph reads it by its parts, a part that "matters" being the one with more than half of five-year
operating profit or else the largest. The parts in the latest document the record holds (statements to stockholders,
2012-09-30, unaudited), with what each could tell a reader:

| Part (2012-09-30) | Carried at (USD thousands) | Earns | What a reader can know of it |
|---|---|---|---|
| 19.38% of Bally Total Fitness Holding Corp. (private; bought as secured loans in 2009, more shares in 2010 and 2011; 22.7 million paid) | 11,333 at cost after 11.3 million of impairments | no dividend recorded | nothing: no Bally statements are given; the stake is carried at "adjusted cost" |
| Cash and equivalents | 5,319 | interest | the amount, at one date 14 years ago |
| Tennenbaum Opportunities Fund VI (managed by an entity where a director is a senior managing partner) and Paulson Gold Fund LP | 2,583 and 2,461 at cost | distributions | no fund statements given |
| Kaiser Aircraft Industries (aircraft maintenance assets bought out of bankruptcy, September 2011, for 0.5 million) | working capital and 506 of equipment | gross loss of 1,480 on revenue of 3,043 in nine months of 2012 | a loss-making operation in its first year |
| 50% of Kaiser-Hill (Rocky Flats closeout, "not fee - bearing") | 786 | nothing; about 2.5 million withheld for closeout, half to the company if released | the fee is spent; the contract has ended |
| Claims: Nova Hut and the IFC (ICC arbitration); the Tippins award of 2.6 million (unrecorded) | nil | nothing | the IFC claim was lost on 2013-06-24 (the company's NOVA HUT NOTICE) |

No part had an operating profit in any year read, so no part "decides" by the five-year test; by size the largest part
is the Bally stake, a cost-carried minority interest in a private fitness chain whose figures the company never gave its
own stockholders. A part that cannot be understood and that matters keeps the whole outside the circle: "if you have
doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.

But the 2012 table is not the business on 2026-10-17. Fourteen years have passed. The company's own list of documents
in October 2015 shows annual statements through 2014 that no archive holds, a "2015 Annual Stockholders Meeting"
document, and a "Kaiser Announcement" whose content is unknown; the website then died and its domain passed to another
company; OTC Markets carries no report. Whether Kaiser Group Holdings today owns the Bally stake, the aircraft unit,
cash, or nothing, whether it has been dissolved, merged or reorganized, and what its share count is, cannot be read from
any document an outsider can get. The financial statements cannot tell me what "the future financial statements are
going to look like" **[M2008-033]**, because there are no financial statements of the present at all. "If something’s
important but unknowable, forget it." **[M2006-076]**. "And if we don’t have the faintest idea what the future stream is
going to look like, we don’t have the faintest idea what it’s worth, now" **[M1994-077]**.

**Routing.** Not a bank. Not a fast-changing industry. A holding company read by its parts: the one part that can be
read in the last document (cash) is small, and the largest part cannot be read; the present parts cannot be named at
all. Read on its own 2012 record the aircraft unit is close to the start-up the rows put aside, "Start-ups are not our
game." **[L2007-015]**, "We don’t do startups." **[M2008-088]**; the file is not decided on that ground, since the
question that closes it comes first.

**Which cause, WORK or NATURE.** The rows name two causes, "our own intellectual shortcomings" and "the nature of the
industry" **[L1993-023]**. The work the rows ask for has been done: "What do I not know that I need to know?"
**[M1999-129]** (what the company owns now, and what it has earned since 2012), and the reading, documents first and the
rest "the last 20 percent or 10 percent" **[M1998-144]**, across EDGAR, the company's own site and every capture of it,
OTC Markets, and a web search. The answer is that the documents do not exist on the public record. No further outside
work can produce them: "we’re not going to learn enough in the followings five months to make up for the fact that we
went in deficient in the first place" **[M2008-086]**. Part VII's refinement (c) records a question unanswerable from
primary documents "as such, with the search that failed", and decides the close on the remaining answers; the remaining
answers are the 2012 parts, which do not pass either (above). So the cause is recorded as **NATURE**.
**CONVENTION of this run** (no text in the framework names this case): an issuer that has published nothing an outsider
can retrieve for more than a decade is sent to TOO HARD (NATURE), not (WORK), because the cure lies with the issuer and
not with the analyst's work. Rationale: section I's WORK cause is a deciding question that is knowable with the work not
done; here the work has been done and the thing is not knowable from where any outside analyst stands. The re-look
condition, written in the box line: the company publishes audited financial statements for a fiscal year ending after
2012, or registers with the SEC again.

**VERDICT: TOO HARD (NATURE).** The file closes at Q1: what the company owns and earns today cannot be known from any
document an outsider can get (latest company report found: unaudited statements for 2012-09-30; website gone since
2016; no OTC disclosure; no SEC filing since 2008-02-28), and the largest part in the last report, a cost-carried
19.38% stake in a private fitness chain, could not be understood from it either **[M2008-069]**, **[M2006-076]**,
**[M2002-092]**, **[M2006-013]**. It is not a judgment of quality or price: "It doesn’t mean it isn’t a good buy. It
doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
**[M2000-038]**.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED. *(Departure 2, recorded for a later run: the FY2006 10-K names no competitor; a search of its text for
"compet" found none. No rival was read.)*

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion.
NOT REACHED as a verdict. The balance sheets were read in Step 0, as the brief and the template require when the file
closes first.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP. The buyback test needs the bottom of Q7's range, which cannot be built.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. **COMPUTATION, NOT A CLEARANCE**, for the operator's two reporting figures:
- **Value range: cannot be built.** Q7's range convention needs owner cash after every real cost for the last five
  years; no figure for any year after 2012 exists in any document found. Inventing one would add a number (the tools
  test). Value is "the discounted value of the cash that can be taken out of a business during its remaining life"
  **[R1996-018]**, and the business is unknown: "you may decide you can’t estimate it at all" **[M1996-025]**.
- **Fair price: cannot be computed**, for the same reason; there is no range and so no midpoint. The documents do not
  allow the figures, and none is reported.
- **For the record only (not a value, not a range):** in every documented year from 2004 the company's operations lost
  money (operating loss 6,364 thousand in 2004, 11,263 in 2005, 7,880 in 2006, 10,940 in the first nine months of 2012;
  FY2006 10-K, 0001104659-07-024333, and the 2012-09-30 statement); retained earnings, with no dividend declared after
  2006, fell 706 thousand in 2007, 1,023 in 2008, 1,396 in 2009, 2,236 in 2010, 14,224 in 2011 and 13,332 in the first
  nine months of 2012 (computed from the year-end columns in Step 0); cash used in operations was 6,524 thousand in the
  first nine months of 2012. The documented income came from the Kaiser-Hill fee and interest, not from operations.
  Equity at 2012-09-30 was 19,774 thousand, about $14.98 a share on 1,320,155 shares: a book figure 14 years old, not
  a value.

## Q8 to Q10, Q12
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE) at Q1**: what the company owns and earns today cannot be known from any document an outsider can
get (latest company report found: unaudited statements for 2012-09-30; no SEC filing since 2008; website gone since 2016,
domain now an unrelated German company; no OTC disclosure); the largest part in that last report, a cost-carried 19.38%
stake in a private fitness chain, could not be read either. No range, no fair price (none computable). Quote $0.0001,
no trades (aggregator, flagged). Re-look condition: audited financial statements for a fiscal year after 2012 published
by the company, or a new SEC registration. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2; **[M1997-127]**.)*

**Bearing on Q5 (integrity) and Q6 (the owners):**
1. **The going-dark sequence.** On 2007-10-25 the company offered to buy every holding of fewer than 100 shares at
   $29.80, "equal to the highest closing price for the Company’s common stock reported in the 90-day period prior to
   October 25, 2007" (8-K, 2008-01-04, 0001104659-08-000656); the stated purpose included that the offer "may result in
   the Company having fewer than 300 holders of record" so that it could "terminate its SEC Reporting Obligations" (SC
   13E3/A, 2007-11-30, 0001047469-07-009627). 6,313 shares were bought for $188,127.40 (8-K/A, 2008-01-15,
   0001104659-08-002854). Book equity per share at 2007-12-31 was about $36.51 (65,466 thousand over 1,792,890 shares).
   On 2008-02-28 the company filed Form 15 (approximately 200 holders of record), saying it intended "to voluntarily
   make financial and other information available periodically to its stockholders via its website" (8-K,
   0001104659-08-013840). By its own list of documents it did so through the 2014 statements; nothing after that has
   been found.
2. **Buybacks after going dark, below book.** Treasury shares and their cost, from the company's statements: 95,477
   shares for 2,578 thousand by 2008-12-31 (about $27.00 a share); 207,649 more for 5,862 thousand by 2009-09-30 (about
   $28.23); 73,020 more for 2,154 thousand by 2009-12-31 (about $29.50); 93,276 more for 2,784 thousand in 2011 (about
   $29.85). Book equity per share at those year-ends: about $36.46 (2008), $37.07 (2009), $35.76 (2010). The shares were
   bought from holders who no longer received SEC reports. Not judged here.
3. **Related-party dealings.** In 2007 Michael E. Tennenbaum held 552,899 shares, 30.9% (DEF 14A, 2007-09-26,
   0001104659-07-071331), and members of his family are named as significant holders. From 2010 the company committed
   $15.0 million to Tennenbaum Opportunities Fund VI, "an investment fund that is managed by an entity where one of the
   Company's directors serves as a senior managing partner"; effective 2012-04-01 "one of the Company's directors
   purchased in a private transaction from the Company $7.5 million of Company's $15.0 million commitment", the company
   recording a gain of $214,000, and "As an accommodation to the Company's Director, the investment fund assessed no fees
   for this transaction" (statements, 2012-09-30, notes 5 and 9). By 2015 the board was Michael E. Tennenbaum, Harold T.
   Bowling and Doris K. Sewell, with Ms. Sewell as chief executive (company website, officers page, capture of 2015-06-19).
4. **Pay.** FY2006, a year in which the 10-K says "We currently have no active operations": chief executive $579,783
   in total (salary $236,961, bonus $225,000), chief financial officer $452,926, and a departing officer $235,170 with
   severance; administrative expenses were $4.598 million against gross revenue of $222 thousand (DEF 14A and 10-K).
5. **Capital allocation after the contract ended.** $22.7 million paid for 19.38% of Bally Total Fitness (2009 to 2011),
   written down by $11.3 million by 2012-06-30; $10.0 million into a gold fund (7.5 million returned in 2012); $0.5
   million for a bankrupt aircraft maintainer's assets, which lost money in every period read. Equity fell from 79.1
   million (2005) to 19.8 million (2012-09-30).

**Bearing on Q4 and Q9:**
6. Kaiser-Hill: of the Rocky Flats fee, $510.8 million of $510.9 million has been received and "A substantial portion
   of the received fee remains subject to audit"; "Government audits at Kaiser-Hill are ongoing" (2012-09-30 statements,
   note 10); about $2.5 million withheld by Kaiser-Hill pending closeout.
7. Nova Hut: an ICC award of about $4.1 million against Kaiser Netherlands B.V. (which filed Chapter 11 on 2008-04-22);
   the company's claim against the IFC was rejected on 2013-06-24 (NOVA HUT NOTICE); the arbitration against Nova Hut
   itself was "still pending" in 2012.
8. Retiree medical plan: a VEBA funded with about $6.1 million in 2007, with a one-time top-up estimated at $1.0 million
   in 2012.
9. The captive insurer, Monument Select Insurance Company: "not at this time issuing new policies" (company website,
   2013 capture); its restricted cash was $109 thousand at 2011-12-31 and nil at 2012-09-30. Nothing in the record shows
   it deciding the run, so the sector method was not applied.
10. The investments were carried at cost "net of impairment"; the 2012 statements were unaudited; the audited annual
    statements for 2007 to 2010 were posted as scanned images.

**Bearing on Q2:** the FY2006 10-K names no competitor. Kaiser Aircraft provided "aircraft maintenance and modification
services to government and military customers" (2012-09-30 statements, note 1); third-party reports (2015, 2018;
flagged, not relied on) say its Birmingham hangar complex was vacant by 2015 and that Kaiser cut its workforce and space
there in 2017.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Step 0 and after Q1.
- [x] Dispatched: the brief allowed per-question pathspec commits; the dispatching session holds the lock (its lock file
      was seen in a listing of `Screens/_daily/`); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. One filtered listing of `Test Runs/` for the
      company's ticker and name was run before the file existed (to check the name was free); it returned nothing and
      is declared under contamination.
- [x] Every v5 id resolves and every quoted fragment beside an id is in its row (`check_ids.py` in the research folder);
      every SEC fact has its accession; every company fact after 2008 has its document and date, there being no accession.
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance; the Q7 lines are headed COMPUTATION, NOT
      A CLEARANCE and give no value.
- [x] No net-income proxy: owner cash was not computed because no document allows it; past losses are stated as what
      they are. The sovereign is from the Treasury. The only quote is an aggregator's, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` returned no arithmetic lines; its v4 verdict word was ignored.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **The issuer that has gone silent.** Section I gives TOO HARD two causes, WORK (knowable, the work not
done) and NATURE (a forecast the industry's insiders would not write down). Neither fits a company whose present is a
plain fact known to its insiders and published nowhere for a decade: the work is done and fails, yet the cause is not
the industry. Part VII's refinement (c) points the way but is written for a research pass, not a Q1 close. I sent it to
NATURE as a CONVENTION of this run, with a re-look condition (published audited statements); the operator may want a
named rule, a third cause or a line in section I. (2) **A document listed but not retrievable.** The absence recorded in
section I (a verdict for a document not yet read) assumes the document can be read. Here the company listed 2013 and
2014 annual statements that no outsider can now retrieve; the framework does not say whether that differs from a
document never published. (3) **The reporting figures.** The brief and Part VII ask for a value range and a fair price
where the documents allow; the template's Q7 line has no place for "not computable", and the operator's alert needs a
figure. I wrote "cannot be built" and gave no number; the fold will need a rule for an alert on a name with no tradeable
price and no figures.
