# Company Run: Coil Tubing Technology, Inc. (OTC, Expert Market: CTBG): 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Dispatched blind run (overnight cycle
2026-10-16) under the brief filled for CTBG, which departs from the canonical brief in three places it names (lines of
evidence derived from the 10-K; competitors from the 10-K's own list; a paragraph on primary documents after 2015).
Research folder: `Test Runs/_research 2026-10-16 CTBG/` (raw filings in its gitignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for CTBG).

**Contamination declared.** Before any work the session context showed the subjects of the five most recent commits
(another company's run and fold, NOA) and the one-line index of the operator's memory files (queue counts, no
company named in it bears on CTBG). Nothing in them names CTBG or Coil Tubing Technology; none of it was used.
No other run file, holding review, `PORTFOLIO.md`, register or reading list was opened, listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Filer.** Coil Tubing Technology, Inc., Nevada, Spring (now Porter), Texas, SEC CIK 0001084463, SIC 3533 (oil and gas
  field machinery). Former names on EDGAR: IPMC Holdings Corp (2003), Access Health Alternatives Inc (1999 to 2003).
  The separate CIK 0001399247, Coil Tubing Technology Holdings, Inc., is the filer's wholly owned operating subsidiary
  (FY2014 10-K, Item 1, Corporate Organization: "one wholly-owned subsidiary, Coil Tubing Technology Holdings, Inc."); it
  registered by SB-2/S-1 in 2007 to 2009, filed one 10-K (FY2008, 2009-04-23, 0001432093-09-000148) and suspended its
  reporting by Form 15-15D on 2011-03-21 (0001432093-11-000122). No rename, merger, split or spin-off after 2013 found
  in the filer's 8-Ks.
- **Filing status.** The last periodic filing is the 10-Q for the quarter to 2015-09-30, filed 2015-11-16
  (0001019687-15-004085). 8-K of 2016-01-08 (0001019687-16-004754): Jason and Jerry Swinford "resigned from all
  positions" effective 2015-12-31, leaving "Richard R. Royall, Chief Financial Officer," as "the sole officer"; a
  consultant engaged at $9,000 a month plus 5% of gross profit on sales he originates. 8-K of 2016-03-16
  (0001019687-16-005486): "Due to a lack of financial resources, we will be unable to continue to file the required
  annual and quarterly filings", beginning with the FY2015 10-K. No filing of any kind under the CIK since
  (EDGAR submissions index, read 2026-10-16). No Form 15 deregistering and no Section 12(j) revocation appear in the index.
- **Primary documents after 2015 (operator rule 5).** Searched 2026-10-16: (1) EDGAR, both CIKs: nothing after
  2016-03-16. (2) The company's own website, www.coiltubingtechnology.com: live, pages modified as late as 2026-06-20
  (Contact) and 2025-11-11 (Products), address now 23722 Loop 494, Porter, Texas, a Canadian service centre through
  "Brico Oil Tools"; product pages, case studies and a careers page; **no investor page, no annual report, no
  financial statement, no share count** (WordPress page list and home page read). (3) OTC Markets' issuer
  disclosure service: the site returned "This site is temporarily unavailable ... scheduled maintenance" on every try
  between about 06:49 and 06:52 EDT (four requests); not read. (4) A web search for an annual report, disclosure statement or the
  litigation: found only the EDGAR filings, and an aggregator page (Seeking Alpha, **aggregator, flagged**) showing the
  symbol on the **Expert Market** with a quoted range "$0.0002-0.04" as of 2026-01-09. **No primary document of the
  business after 2015-11-16 was found.**
- **Price:** **no live public quote found.** The Expert Market does not publish quotations to the public; the only
  figure seen is the aggregator's range above, flagged and not used.
- **Shares:** 15,632,425 common shares outstanding at 2015-11-14 (cover of the 10-Q to 2015-09-30,
  0001019687-15-004085), equal to the balance sheet's 15,632,425 issued and outstanding at 2015-09-30 (no treasury
  stock line; 19,402 shares were bought and retired in a 2015 settlement, per the 10-Q's Note 7 and its financing
  section). `python Screens/cover_shares.py CTBG` returns "NOT AN SEC REGISTRANT in the live ticker file"; the count is
  read by hand. No later 8-K or prospectus. The count today is unknown.
- **Market cap:** cannot be computed (no price; share count ten years old).
- **Sovereign (USD):** 5.43%, the 30-year par yield of 2026-10-15, US Treasury daily par yield curve
  (`python tools/sources.py`, 2026-10-16).
- **Filings read** (operator rule 4): FY2014 10-K, filed 2015-03-30 (0001019687-15-001138), Items 1, 1A, 7, 8 and the
  notes; 10-Q to 2015-09-30, filed 2015-11-16 (0001019687-15-004085); the two 2016 8-Ks above; FY2013 10-K
  (0001019687-14-001087) and FY2012 10-K (0001019687-13-000936), statements; the Form 10 of 2012-01-23
  (0001432093-12-000046) for the 2009 to 2011 balance sheets; the 424B3 of 2013-01-30 (0001214782-13-000062), the final
  prospectus of S-1 333-184443, kept for history. **No proxy statement exists** in the index (the filer held no
  solicited meeting under the CIK in 2013 to 2016). **Cross-check:** total revenue for 2014 of $6,866 thousand in the
  filed statement of operations equals the "$6,866,000" of Item 1, Major Customers, and of Item 7.
- **`python tools/run.py CTBG`:** "CTBG: not an SEC filer" (the ticker is no longer in the SEC's map); every figure
  below is taken by hand from the filed statements, in thousands of dollars.

**Owner cash by year, by hand** (operating cash flow, less stock pay, less all spending on rental tools, buildings and
equipment, plus proceeds from lost or sold tools and assets; no income tax was paid in any year):

| | FY2011 | FY2012 | FY2013 | FY2014 | 9M 2015 |
|---|---|---|---|---|---|
| Revenue | 5,541 | 7,765 | 6,143 | 6,866 | 2,495 |
| Net income (loss) | 729 | 752 | (866) | (316) | (2,698) |
| Operating cash flow | 1,015 | 817 | 694 | 1,196 | 47 |
| Stock pay (added back in OCF, deducted here) | (32) | (216) | (460) | (205) | (89) |
| Rental tools bought | (3,663) | (1,108) | (419) | (665) | (118) |
| Buildings, machinery, equipment | (496) | (216) | (1,242) | (415) | (1,186) |
| Proceeds, lost tools and asset sales | 179 | 210 | 187 | 336 | 85 |
| **Owner cash** | **(2,997)** | **(513)** | **(1,240)** | **247** | **(1,261)** |
| Interest paid | 13 | 17 | 24 | 62 | n/a |

Sources: FY2012 10-K statements (FY2011, FY2012), FY2014 10-K statements (FY2013, FY2014), 10-Q to 2015-09-30 (nine
months). FY2015 as a year was never filed.

**The balance sheets, read before the income account** **[M2025-032]** (thousands; 2009 and 2010 from the Form 10):

| Dec 31 (Sep 30 for 2015) | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 Q3 |
|---|---|---|---|---|---|---|---|
| Cash | 0.2 | 330 | 226 | 1,153 | 902 | 1,280 | 676 |
| Receivables, net | 173 | 280 | 1,581 | 1,827 | 1,875 | 2,102 | 633 |
| Rental tools, net | 379 | 463 | 3,567 | 3,687 | 3,034 | 2,325 | 1,553 |
| Property and equipment, net | 110 | 115 | 501 | 534 | 1,500 | 1,575 | 2,537 |
| Intangibles (patents bought from the chairman) | n/r | 1,193 | 1,113 | 1,033 | 953 | 4,602 | 4,355 |
| Total assets | n/r | n/r | 7,042 | 8,291 | 8,376 | 12,078 | 9,811 |
| Related-party notes (to Jerry Swinford) | n/r | n/r | 557 | 402 | 247 | 3,841 | 3,750 |
| Other notes payable | n/r | n/r | 277 | 205 | 890 | 972 | 1,642 |
| Equity | n/r | n/r | 4,784 | 7,204 | 6,798 | 6,687 | 4,066 |
| Accumulated deficit | n/r | n/r | (2,946) | (2,194) | (3,060) | (3,376) | n/r |

n/r: not read (the 2009 and 2010 statements were read for current assets and the long-lived lines only). 2015 Q3 equity
is total assets 9,811 less total liabilities 5,745 (Item 2 of the 10-Q).

What moved and why. Equity was raised, not earned: $3.2 million of stock sold in 2011 and $1.45 million in 2012
(financing sections), against an accumulated deficit that was never closed. The rental fleet was bought in 2011 with that
money and then run down (rental tools net from 3,687 to 1,553) while buildings were bought (property from 534 to 2,537,
two Spring buildings in 2013 and 2015, financed by bank and seller notes). The largest single asset from 2014 is the
$3,750 thousand of patents bought from the company's own chairman with a note to him, which nearly tripled
intangibles and created the largest liability. Receivables fell from 2,102 to 633 in nine months of 2015 as revenue fell
79% in the third quarter, with $519 thousand written off as bad debt. "what the figures are saying and what they don't
say": they say what the business was in 2015; they say nothing of what it has been for the ten years since.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own it "if the market closed for five years"
**[M1997-109]**, or if the stock were delisted and reopened long after **[M1996-067]**. Here the question is inverted
by the facts: the reporting, not the market, closed in 2016, and an owner of these shares has had no figures from the
business for ten years. The analyst's habits bind most: "What do I not know that I need to know?" **[M1999-129]**, and
contrary evidence written down at once **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) revenue fell 79% in the third quarter of 2015 and gross profit turned negative, with "an increase in competitive
pricing to our customers" (10-Q, Item 2); (2) the company paid its own chairman a $3.75 million note for patents that its
earlier filings said it already owned (10-Q, Note 4); (3) the officers sued the company and other shareholders
intervened alleging fraud (10-Q, Note 7); (4) the company stopped filing for lack of money (8-K, 2016-03-16). The one
fact the other way: the website shows the tool business still operating in 2025 and 2026, at a new address.

## THE STANDING RULE
Owning a share of this company puts no buyer at risk of ruin if it is bought outright with spare money, since the loss is
capped at what is paid; the rule binds the buyer's financing and sizing, not the target **[L2023-005]**,
**[M2006-079]**. No purchase can be sized here in any case (no quote). Not engaged.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The lines of evidence, chosen from the FY2014 10-K** (the brief's departure (1)). From Item 1: the business is the
rental and sale of patented downhole tools, 95% outsourced manufacture, a small number of repeat customers, the
patents "make up the core of our business". From Item 1A: the company needs outside money ("The revenues we have
generated since our incorporation have not been sufficient to support our operations"); customers are also competitors;
dependence on oil and gas prices; control by an 81.7% holder; a board of two, father and son. From Item 7: the 2015
purchase of patents from the chairman, and liquidity. So the lines chosen are four: (a) **whether any current account
of the business exists** for an owner to read; (b) who owns the patents that are the core of the business; (c) the
economics through a full oil-price cycle (2014 to 2016 was the downturn the filings describe); (d) the funding. Line
(a) is read first because the other three can only be read from it.

**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**; the first question is "do I understand enough about this business so that the
financial statements will tell me the information that" is useful in judging "what the future financial statements are
going to look like" **[M2008-033]**; and the quick decision is made from the documents: "if you can" not decide "off the
figures, forget about going further" **[M2008-069]**.

**Applied.** There are no figures to decide from. The last statement of the business is a quarter that ended on
2015-09-30, in which revenue was $450 thousand against $2,160 thousand a year before and gross profit was negative (10-Q,
Item 2). Since then the company has published no statement of revenue, cash, debt, share count, management or the
outcome of the patent suit: its own 8-K says it cannot afford to (0001019687-16-005486). Of the four lines: (a) no
current account exists (Step 0, primary documents); (b) who owns the patents was in litigation in Harris County in
November 2015, with the interveners claiming the company "owns all or most of the patents free and clear" and the
former officers claiming payment under the $3.75 million note (10-Q, Note 7), and no outcome has been published; (c) the
filed record covers the boom years 2011 to 2014 and three quarters of the bust, and stops there; (d) the last statement
shows $676 thousand of cash against $5,392 thousand of notes, of which $3,804 thousand fell due in 2018 (10-Q, Note 4
maturity table), and no later statement says whether they were paid, restructured or defaulted. The business that exists
today (the website shows one, at a different address, selling the same tool names) cannot be connected to the shares
by any document: its owners, its debts and its earnings are not on the public record.

Is the deciding question knowable? It is important (it is the whole business) and, to an outside owner, not knowable
from any primary document: "important but unknowable, forget it." **[M2006-076]**. With no figures,
"what the future stream will look like" cannot be pictured, and so neither can the value **[M1994-077]**. The doubt rule
settles any remainder: "if you have doubts about something being into your circle of competence" **[M2002-092]**.

**Which cause** (section I, the two causes). The cause is not the industry's nature in the sense of **[L1993-023]**: a
tool-rental business in the oilfield is a business whose economics could be read from a full set of accounts (a
commodity dependence is never by itself a STOP at Q1, Q2's commodity paragraph, **[M2008-069]**). Nor is it work the
analyst has left undone: every place a primary document could be was searched (Step 0), the company's own filing says it
will not produce one, and the research pass of Part VII could only read documents that do not exist; a second pass on
the same question is barred, and "we're not going to learn enough" more by waiting **[M2008-086]**. Part VII's step (1)
gives the routing: "if the deciding question is not knowable, the file closes TOO HARD (NATURE) at once". The insiders
of this company have in fact declined to write the figures down, which is the form of test 5 **[M2000-105]**: they "would
not want to put down on paper their predictions", and here not even the past. **CONVENTION of this run:** a company that
has ceased to publish accounts is closed TOO HARD (NATURE), not (WORK), with a re-look condition in place of a research
pass; rationale: the label WORK promises that reading will cure the box, and here no reading exists to be done; the
condition that would reopen the question is a document, not a downturn and not a price. Re-look condition: the company
files a 10-K with audited statements, or posts audited annual statements through OTC Markets' disclosure service.
One source was not reached (OTC Markets, under maintenance this morning); the aggregator's Expert Market listing is
consistent with no current public disclosure there, and the next run of the name reads that service first.

A lower price does not reopen it: "It just means that we don't know how to evaluate it." **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE).** The business's present and ten-year economics cannot be known from any document
  available to an owner: the last statement is of 2015-09-30, the company announced it would stop filing for "a lack of
  financial resources" (8-K, 2016-03-16, 0001019687-16-005486), and none has been published since **[M2008-069]**,
  **[M2006-076]**, **[M1994-077]**, **[M2006-013]**.

## Q2: NOT REACHED
## Q3: NOT REACHED
## Q4: NOT REACHED (the balance sheets were read in Step 0, as the template asks when the file closes before Q4)
## Q5: NOT REACHED
## Q6: NOT REACHED
## Q7: NOT REACHED (COMPUTATION below)
## Q8: NOT REACHED
## Q9: NOT REACHED
## Q10: NOT REACHED
## Q12: NOT REACHED

---
## COMPUTATION, NOT A CLEARANCE (the operator's two reporting figures; a reporting convention, not a rule)
Computed after the STOP at Q1, on figures ten years old, and on no price. Nothing here is a verdict or entry language
(operator rule 3), and none of it describes the business today.
- **Window.** Q7's five-year window cannot be built: FY2015 was never filed. The filed window is FY2011 to FY2014, four
  years, used here as a CONVENTION of this run (rationale: it is all the filed record holds). Owner cash after every
  real cost (Step 0 table): (2,997), (513), (1,240), 247; average **(1,126) thousand a year** equity-only (interest is
  inside operating cash), **(1,097) thousand** before interest (all-equity basis, interest paid added back). No income
  tax was paid in any year (carryforwards from the accumulated deficit); the company's own tax is taken as paid, nil.
- **Specific (a), cycles.** FY2011 carries the rental fleet's build ($3,663 thousand of tools); the filer does not call
  the year aberrational, so it stays in the base; the three years FY2012 to FY2014 are shown beside: average (502)
  thousand, still negative.
- **Specific (b), decline.** The series changes sign, and the compound rate between the end years is meaningless; both
  halves (FY2011 to FY2012, FY2013 to FY2014) are negative, so the rate between them is meaningless too. The range is
  the **no-growth case alone**, said so.
- **Net debt** at the latest filed date, 2015-09-30: notes payable of $5,392 thousand (Note 4 maturity table, including
  the $3,750 thousand note to Jerry Swinford) less cash of $676 thousand, **$4,716 thousand**; operating leases left
  out. No subsequent event is stated in that filing other than the litigation.
- **(a) VALUE RANGE**, no-growth case alone, at the 30-year Treasury of 5.43%: **about $-1.59 a share** on the
  all-equity basis ((1,097) / 0.0543, less net debt, over 15,632,425 shares); equity-only beside it **about $-1.33 a
  share**. The range is below zero.
- **(b) FAIR PRICE** (each end case valued at ten percent, the two averaged; here one case): **about $-1.00 a share**
  all-equity (the central figure); **about $-0.72 a share** equity-only beside it. Not positive. Against the price:
  **no public quote exists** (Expert Market; the aggregator's "$0.0002-0.04" is flagged and not used).
- Had the file reached Q7, the floor would have closed it OUT before any width test (Q7, the floor is tested first),
  since no case earns the floor at any positive price. Q6's buyback line is not needed: the company made no buybacks
  other than the $11 thousand settlement retirement of 2015.

---
## THE BOX
**TOO HARD (NATURE) at Q1**: the business's present and ten-year economics cannot be known from any document available
to an owner; the last statement is the quarter to 2015-09-30 and the company stopped filing in 2016 for "a lack of
financial resources". Re-look condition (CONVENTION of this run, Q1): audited annual statements filed with the SEC or
posted through OTC Markets' disclosure service. COMPUTATION on the filed record only: value range about $-1.59 a share
all-equity (no-growth case alone), fair about $-1.00 all-equity ($-0.72 equity-only), against no public quote.
**Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Q2 (the castle).**
- Competitors named by the FY2014 10-K itself (Item 1, Coiled Tubing Industry): National Oilwell Varco (files with the
  SEC), Baker-Hughes (filed as Baker Hughes Incorporated until its 2017 combination; the successor files), Weatherford
  (files), **Thru Tubing Solutions (does not file; private)**, **Smith International (no longer files; acquired by
  Schlumberger in 2010)**. Their filings were not read: the file closed at Q1, and the comparison is a Q2 task.
- Item 1A: "a significant portion of our revenues came from customers who are also our competitors"; "The oil and gas
  industry is highly competitive and fragmented"; larger rivals "may be able to devote greater resources".
- 10-Q to 2015-09-30, Item 2: gross profit fell to (17%) of revenue in the third quarter "mainly due to a decrease in
  rentals and product sales and an increase in competitive pricing to our customers".
- Customer concentration: two customers 17% and 18% of 2013 sales; the Supreme Oilfield Services distribution agreement
  carried 33% of 2013 and 19% of 2014 revenue (FY2014 10-K, Item 1).
- Revenue: 5,541 (2011), 7,765 (2012), 6,143 (2013), 6,866 (2014), 2,495 for nine months of 2015 against 5,073.

**Q3 and Q4 (capital and the accounts).**
- Owner cash negative in three of four filed years (Step 0 table); the business was funded by stock sales of $3.2
  million (2011) and $1.45 million (2012) and by notes; Item 1A: "The revenues we have generated since our
  incorporation have not been sufficient to support our operations".
- The 2015 10-Q says the earlier agreements and disclosures of the company's ownership of Mr. Swinford's later patents
  "were made in error", and the 2015 purchase, effective December 2014, was booked as a $3,750 thousand intangible
  against a note to him; no impairment had been taken at 2015-09-30 ("To date, no such impairment has occurred") while
  third-quarter revenue fell 79%.
- Bonuses to the two officers were based on "yearly EBITDA" in years other than 2013 and 2014 (FY2014 10-K, Item 1A):
  EBITDA in the filer's own pay plan.
- Bad debt of $519 thousand written off in nine months of 2015.

**Q5 (the people): integrity facts, recorded, not judged.**
- The board in 2014 and 2015 was Jerry Swinford and his son Jason Swinford only, "None of Whom Are Independent", with
  "the power, in their sole discretion, to approve discretionary bonuses to themselves" ($84,795 each for 2014; Item 1A).
- The 2015 IP Purchase Agreement: the company, whose two directors were the seller and his son, issued the chairman a
  $3,750,000 note for patents that its 2010 agreements and its own earlier reports had treated as the company's; the
  filing says those agreements "were entered into error" (10-Q, Note 4; FY2014 10-K, Item 7). The note is secured on the
  assets acquired and falls due at once on a change of control.
- The majority holder (Herbert C. Pohlmann, 81.7% of the common, Item 1A) had promised Mr. Swinford $3.75 million in his
  will at the time of the 2010 purchase and removed the provision in late 2014; the company's $3.75 million note to
  Mr. Swinford followed, effective December 2014 (10-Q, Note 4).
- On 2015-08-14 the two officers and sole directors sued the company for non-payment under that note; on 2015-11-10
  shareholders including the majority holder intervened alleging "fraud and a breach of fiduciary duty" by the two
  officers (10-Q, Note 7, Cause No. 2015-58884, 164th District Court, Harris County). Outcome not on the public record
  searched.
- Both officers resigned effective 2015-12-31; the company then stopped filing (the two 2016 8-Ks).
- A voting agreement let Mr. Swinford direct the majority holder's vote for 40% of the board until 2015-12-31 (Item 1A).

**Q6 (the money and the owners).** No dividends; no buybacks apart from the 2015 settlement retirement ($11 thousand);
the company has given owners no financial information since 2015.

**Q9 (debt).** At 2015-09-30, $5,392 thousand of notes against $676 thousand of cash; $3,804 thousand fell due in 2018
(Note 4); building loans secured by the Spring properties, one personally guaranteed by Jason Swinford. Whether any of
it was paid is not on the public record searched.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 and at the close
      (write-early). The file closed at Q1, so two commits carry it.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's. The run
      binds nothing until it is folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident
      (commit subjects about NOA, the memory index) is declared at the top under contamination and was not used.
- [x] Every v5 id resolves (checked by the script `check_ids.py` in the research folder); every filing fact carries its
      accession or names the document it came from; the website and the aggregator are named as such.
- [x] The order was kept; Q1 closed the run; everything after it is headed NOT REACHED, COMPUTATION or AFTER THE STOP.
- [x] Owner cash after every real cost, by hand from the filed cash-flow statements, stock pay deducted, never a
      net-income proxy (operator rule 5); the sovereign from the US Treasury, dated 2026-10-15; the only market figure
      seen is an aggregator's and is flagged and unused.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP,
      with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` and `Screens/cover_shares.py` both failed on the ticker map; no line of either was used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The framework has no stated box for a company that has stopped publishing accounts. Section I says a verdict for "a
document not yet read" has no instance in the rows and would be a CONVENTION; this is the other case, a document that
does not exist and that the company has said it will not produce. The two causes of TOO HARD fit it badly: WORK promises
that reading will cure the box, and here there is nothing to read; NATURE is defined by an industry whose insiders would
not write the forecast down, while here the industry is readable and it is this company that has stopped writing even
its past. I closed TOO HARD (NATURE) through Part VII's step (1) ("if the deciding question is not knowable, the file
closes TOO HARD (NATURE) at once") and confessed the label as a CONVENTION of this run, with a re-look condition (a
filed or posted audited statement) in place of a research pass, by analogy with Q2's dated re-look condition for a
change for the better. A rule naming this case (a dark filer: TOO HARD (NATURE), re-looked on a new audited statement)
would make the next such run mechanical. Two smaller gaps: Q7's range convention assumes a five-year window exists,
and here only four filed years do (I used four and said so); and the template's Step 0 asks for a price and a market cap
without saying what a run reports when no public quote exists (the Expert Market publishes none); I reported "no public
quote" and computed the fair price on the filed record with no price to set it against. Last, one source the brief names
(OTC Markets' disclosure service) was down for maintenance through the run; the box rests on EDGAR, the company's own
website and the aggregator's Expert Market listing, and the next run of the name should read that service first.
