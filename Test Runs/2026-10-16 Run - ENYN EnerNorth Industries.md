# Company Run — EnerNorth Industries Inc. (formerly AMEX: ENY, Frankfurt: EPW1; OTC symbol ENYNF; ENYN) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the three departures the brief states (lines of
evidence derived from the 20-F by the analyst; competitors from the 20-F; the "filer with no current filings" paragraph
governs the primary document and the sovereign). SEC CIK 0001049021, Commission File Number 0-29586; an Ontario company,
Toronto, June fiscal year, 20-F filer; renamed from Energy Power Systems Ltd in 2003.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for ENYN or EnerNorth).

**Contamination, declared and not used.** Before any work, this session's context carried: the commit subjects of the
working repository's latest commits (a fold and run of another dark filer, CTBG, closed TOO HARD (NATURE) at Q1, and an
overnight log line for NOA); the file names in `git status` of other research folders (`_research 2026-09-26 AYI`,
`_research 2026-09-27 ARCB`) and of the daily digests; the one-line index of the operator's memory files (queue state,
counts of gate-clearers, holdings reviews owed, none naming this company); and a comment in `.gitignore` naming Ford.
None of it names EnerNorth. The CTBG subject line is the one that bears on method (a dark filer closed at Q1); it is
declared here so that the reader can judge whether it steered this run. The box below was reached on this company's own
record and the rows cited, and the run states the alternative reading (OUT) in its last section. No `Test Runs/` file,
holding review, `PORTFOLIO.md`, register or reading list was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** no usable public quote. The last exchange listing was AMEX: ENY, struck by a Form 25-NSE filed by the American
  Stock Exchange on 2007-04-10 (acc `0001143313-07-000057`). Aggregators, flagged under operator rule 5: stoxray.com
  (fetched 2026-10-16) shows OTC symbol ENYNF, "Last price 0.00 USD" and "Market cap 0 USD" with an undated "Jan 07"
  stamp; a search snippet of Simply Wall St (page itself refused the fetch, HTTP 403) gave a market cap of US$4,000 on
  about 4.29 million shares and called the listing no longer active; the Weiss Ratings page now says the ticker is not
  found; Yahoo's chart API returns "No data found, symbol may be delisted"; OTC Markets was down for maintenance at fetch.
  **No price is used in this run**; where a comparison needs one, the aggregator figure of about US$0.00 is named as such.
- **Shares by class:** one class, common shares, no par value. 4,272,009 at 2006-06-30 (20-F cover, acc
  `0001049021-06-000046`); "approximately 4.293 million shares issued and outstanding" at 2007-03-20 (6-K, press release
  on the assignment in bankruptcy, acc `0001049021-07-000016`). `python Screens/cover_shares.py ENYN` refused: "NOT AN
  SEC REGISTRANT in the live ticker file"; the count is taken by hand from the filings. Issued less treasury: the 20-F
  reports no treasury shares (Item 7.A gives 4,272,009 "issued and outstanding"). The run uses 4,293,000.
- **Market cap:** not computable from a primary quote; on the aggregator's US$0.00, nil.
- **Sovereign for the earnings currency (CDN$):** **4.19%**, the Government of Canada long-term benchmark bond yield,
  Bank of Canada series `BD.CDN.LONG.DQ.YLD`, observation of 2026-10-14 (the latest published at fetch on 2026-10-16;
  saved as `cache/boc_long.json`). The protocol's sovereign table has no CAD row; the Bank of Canada is the issuing
  authority's central bank and publisher of the series, the nearest to the Treasury and MoF rows the table names.
- **Filings read** (operator rule 4), all from SEC EDGAR:
  - 20-F for the year to 2006-06-30, filed 2006-10-06, acc `0001049021-06-000046` (Items 3.A, 3.D, 4, 5.B, 7, 8.A.7 read).
  - 20-F for FY2002, filed 2002-12-20, acc `0001049021-02-000052` (Item 3.A, FY1998 to FY2002); 20-Fs for FY2001
    (`0001130319-01-500356`), FY2003 (`0001049021-03-000035`), FY2004 (`0001049021-04-000054`), FY2005
    (`0001137171-05-001601`) downloaded; their selected data are carried in the two tables above, not re-read line by line.
  - 6-K interim statements to 2006-12-31, filed 2007-02-14, acc `0001049021-07-000009` (balance sheet, operations, cash
    flows; "Notice to Reader": "An accounting firm has not reviewed or audited these interim consolidated financial
    statements"); MD&A of the same date `0001049021-07-000010` (downloaded).
  - 6-K material change report 2007-01-18, acc `0001049021-07-000002` (Supreme Court of Canada denies leave; Oakwell
    judgment of "approximately CDN $6.8 million in addition to the $1.5 million posted as security").
  - 6-K press release 2007-02-14, acc `0001049021-07-000011` (the buyer 1211115 Alberta Ltd. says EnerNorth "is not in a
    position to close").
  - 6-K material change report 2007-03-09, acc `0001049021-07-000013` (Notice of Intention to make a proposal under the
    BIA filed 2007-02-09; Zwaig Associates Inc. appointed trustee and Interim Receiver; 45-day extension).
  - 6-Ks 2007-03-21, accs `0001049021-07-000015`, `-000016`, `-000017` (director resigns 2007-03-19; Assignment in
    Bankruptcy filed 2007-03-20, Zwaig Associates Inc. trustee in bankruptcy).
  - 8-K 2006-12-15, acc `0001049021-06-000071` (AMEX deficiency notice of 2006-12-12; exhibit index read).
  - Form 25-NSE 2007-04-10, acc `0001143313-07-000057`.
- **Later primary documents searched, none found:** EDGAR has no filing after 2007-04-10 (submissions JSON, fetched
  2026-10-16). The company's site www.enernorth.com now redirects to a parked "/lander" page. Web searches for the trustee's
  reports (Zwaig Associates, "EnerNorth" bankruptcy estate), for an Ontario Securities Commission cease-trade order, and for
  a sale of the Alberta subsidiary returned nothing on this company. SEDAR+ and the federal insolvency-name search were not
  reachable by this session's tools (both need an interactive session); that is a gap, recorded under what I could not get.
- **One figure cross-checked against the filed statement:** total assets at 2006-06-30, CDN$15,198,471, in the 20-F's
  Item 3.A table (acc `0001049021-06-000046`) and in the comparative "June 30, 2006 (audited)" column of the interim balance
  sheet (acc `0001049021-07-000009`): the same figure.
- `python tools/run.py ENYN`: refused, "ENYN: not an SEC filer [...] This is UNRESEARCHED, not UNKNOWABLE." Every figure
  in this run is taken by hand from the filed statements and computed in `Test Runs/_research 2026-10-16 ENYN/computation.py`
  (output beside it). Owner cash by year is given under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

**Lines of evidence, derived from the 20-F (as the brief asks), and why.** Item 4 says the company's "primary activities
are investment in, exploration and development and production of oil and gas", that it began oil and gas in fiscal 2001,
and that it also held Indian power-project interests and the Oakwell litigation. Item 3.D opens with the "Need for
additional capital", an "unfunded liability in the amount of approximately CDN $6,186,971 in relation to a Judgment", and
"A history of losses and limited operating history". Item 5 carries a going-concern note. The lines chosen: (1) whether any
business still exists behind the shares, and what record of it there is after 2006 (the deciding line, since the last
filings are of a bankruptcy); (2) the Oakwell judgment against the assets; (3) the oil and gas economics: net revenue
against operating, administrative and capital costs, and finding cost; (4) the ten-year balance sheets; (5) related-party
dealings in the last year. Line (1) decided the file.

## THE FOUNDATIONS (not a gate)
Two foundations bear. A share is a business: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**; for this name the market did close, in April 2007, and nineteen years later there is no account of the
business at all, so the test cannot even be put. And the market serves, it does not instruct: an aggregator quote of
US$0.00 "just tells us prices" **[M2006-077]** and is no evidence of value either way. **Contrary evidence, written down as
found** **[M1997-127]**: the speakers do say that "a complicated bankruptcy can offer opportunities for profit"
**[M2006-089]**, and Buffett bought bonds where "if they went into bankruptcy that the assets were considerably greater in
relationship to the liabilities than indicated by the market" **[M2001-078]**. Written against the hypothesis that the
shares are worthless: at 2006-12-31 the unaudited balance sheet showed total assets of CDN$14,730,077 against total
liabilities of CDN$11,977,273, a book equity of CDN$2,752,804 (acc `0001049021-07-000009`), so on book the estate was not
plainly insolvent three months before the assignment. Against that: the same 20-F's US GAAP column shows equity at
2006-06-30 of only CDN$867,362 after ceiling-test write-downs (Item 3.A), the half-year to 2006-12-31 lost CDN$1,818,643,
the oil and gas carrying values were never realised by the sale the company sought, and the speakers' own row says it is
creditors who bear losses in bankruptcies **[L2005-016]**, ahead of owners.

## THE STANDING RULE
Owning this puts the buyer at no risk of ruin if bought for cash in a size the buyer could lose entirely: the rule is
"Never risk permanent loss of capital" **[L2023-005]** and "never going to risk what we have and need for what we don’t have
and don’t need" **[M2012-081]**; with no quote, no market and no filing, any money put in should be counted as at risk of
total loss. No borrowing, no position. Nothing here closes the file.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it, applied to the filings.** "the first question is, can I understand it? And unless it’s
going to be in a business that I think I can understand, there’s no sense looking at it." **[M1995-051]**; understanding is
"a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]**.

**What the filings say the business was.** A junior oil and gas producer in Western Canada and Ontario, begun in fiscal
2001 (20-F Item 4.A, acc `0001049021-06-000046`), whose net oil and gas revenue after royalties was CDN$980,268 in FY2006
against administrative expenses of CDN$2,198,024 (Item 3.A); losses from continuing operations every year FY1998 to FY2006
(FY2002 20-F Item 3.A, acc `0001049021-02-000052`; FY2006 20-F Item 3.A); plus minority Indian power-project interests and
a Singapore judgment of US$5,657,000 plus costs (Item 8.A.7). A dependence on the oil price is not by itself a STOP here
**[M2016-025]** (framework Q2, "A commodity business"), so that is not what decides.

**What the filings say the business became.** On 2007-01-18 the Supreme Court of Canada denied leave to appeal, and the
company said "all or substantially all of the assets of the Company may be sold or pledged" (acc `0001049021-07-000002`).
On 2007-02-14 the buyer of its pending acquisition said EnerNorth "is not in a position to close" (acc
`0001049021-07-000011`). On 2007-02-09 it filed a Notice of Intention under the BIA and the court appointed an Interim
Receiver (acc `0001049021-07-000013`). On 2007-03-20 it "filed an Assignment in Bankruptcy under the Bankruptcy and
Insolvency Act (Canada), appointing Zwaig Associates Inc. as trustee in bankruptcy" (acc `0001049021-07-000017`). The
exchange delisted the shares on 2007-04-10 (acc `0001143313-07-000057`). Nothing has been filed, published or posted by
the company since, on any record this session could reach (Step 0).

**The tests.**
- *Do the past statements tell me the future ones?* "do I understand enough about this business so that the financial
  statements will tell me the information that’s useful to me in making a judgment about what the future financial
  statements are going to look like" **[M2008-033]**. No: the last statements (unaudited, not reviewed, to 2006-12-31)
  describe a business that was surrendered to a trustee eleven weeks later. Whatever the trustee sold, kept or distributed,
  and whether any asset or business remains under these shares, is in no document found. "if you can’t make a decision on
  something like PetroChina off the figures, forget about going further" **[M2008-069]**: here there are no figures for
  nineteen years.
- *Is it important and knowable?* **[M2006-076]**. Important: it is the whole question. Knowable from the public record
  this session could reach: no. The trustee's reports may exist in the federal insolvency records, but they would report a
  liquidation's receipts and distributions to creditors, not the ten-year economics of a business; no document suggests
  any business continued.
- *Would the insiders write it down?* **[M2000-105]**. The company's own last annual report said its risks "may affect the
  Company in a manner and to a degree which cannot be foreseen at this time" (20-F Item 3.D), and then its insiders stopped
  writing anything down at all: no annual report, interim statement or press release after March 2007.
- *Do I doubt it is inside?* "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**. I doubt there is a business here to understand.

**Which cause, WORK or NATURE.** The rows give two causes, the analyst's shortcomings and "the nature of the industry"
**[L1993-023]**. This is not a forecast the work could make: the deciding fact, what if anything sits under these shares
after the assignment, has been on no public record for nineteen years, and "we’re not going to learn enough in the
followings five months to make up for the fact that we went in deficient in the first place." **[M2008-086]**.
**CONVENTION of this run:** a company that assigned itself into bankruptcy and has published no account of any business
since is treated as TOO HARD (NATURE) at Q1, its insiders having in fact declined to put any forecast on paper
**[M2000-105]**; rationale: the label WORK would open a research pass whose only primary source (the trustee's estate file)
reports a liquidation, not a business, and a research pass "never widens the circle to find something to buy" (framework
section I). A lower price does not reopen it **[M2000-038]**. The alternative reading, OUT, is stated in the last section.

**The re-look condition (CONVENTION of this run, the same rationale):** a new audited statement of this company, or a
filed document showing a business carried on under these shares after 2007-03-20.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**: no account of the business since the unaudited statements to
  2006-12-31; an Assignment in Bankruptcy filed 2007-03-20 (acc `0001049021-07-000017`); delisted 2007-04-10 (acc
  `0001143313-07-000057`). "if we don’t have the faintest idea what the future stream is going to look like, we don’t have
  the faintest idea what it’s worth, now." **[M1994-077]**.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (Q1 closed the file).

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten years of balance sheets are read under AFTER THE STOP, as the brief asks when the file closes before Q4.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's two reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE) at Q1**: an Assignment in Bankruptcy filed 2007-03-20 (acc `0001049021-07-000017`), delisted
2007-04-10 (acc `0001143313-07-000057`), and no account of any business since the unaudited, unreviewed statements to
2006-12-31 (acc `0001049021-07-000009`). The NATURE label and the re-look condition (a new audited statement, or a filed
document showing a business carried on under these shares after 2007-03-20) are CONVENTIONS of this run, confessed at Q1.
Integrity facts recorded, not judged. COMPUTATION on the filed record: value about $-16.16 a share all-equity (no-growth
case alone; $-14.64 equity-only), fair about $-7.66 all-equity ($-6.14 equity-only), CDN$; no usable public quote
(aggregator about US$0.00, flagged).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged, operator rule 2.)*

**Competitors (for Q2).** The 20-F names no rival. Item 3.D: the company "competes directly and indirectly with major and
independent oil and gas companies" and "the industry is not dominated by any single competitor or a small number of
competitors"; Item 4.B: "Many of the Company’s competitors have greater financial and technical resources" (acc
`0001049021-06-000046`). The only other company named in the oil and gas business is GeoCan Energy Inc., a co-holder of
working interests of which a director, Mr. Cassina, is also a director (Item 7.B): a partner, not a rival. Since the 20-F
names none and Q2 was not reached, no rivals were chosen and no competitor row was built. Finding cost per Mcf or barrel,
which the speakers call "the most important figure in an oil and gas company over a period of years" **[M2007-082]**, was
not located in the parts of the 20-F read.

**The balance sheets, ten year-ends (for Q4).** CDN$000, Canadian GAAP as filed: FY1998 to FY2001 from the FY2002 20-F
Item 3.A (acc `0001049021-02-000052`); FY2002 to FY2006 from the FY2006 20-F Item 3.A (acc `0001049021-06-000046`); the
last column from the interim balance sheet (acc `0001049021-07-000009`, unaudited, not reviewed).

| June 30 | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | Dec 31 2006 |
|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 29,002 | 30,051 | 23,511 | 19,050 | 25,415 | 28,835 | 23,263 | 15,709 | 15,198 | 14,730 |
| Working capital | (3,104) | (4,542) | (1,925) | 4,205 | 7,314 | 777 | 815 | (101) | (6,916) | (7,713) |
| Due to shareholders, long-term | 4,584 | 4,026 | 1,842 | 350 | nil | nil | nil | nil | nil | nil |
| Long-term debt | 3,243 | 2,333 | 738 | 646 | 502 | 528 | 542 | nil | 153 | 143 |
| Shareholders' equity | 5,665 | 13,402 | 12,107 | 11,357 | 18,059 | 11,254 | 7,090 | 7,076 | 4,542 | 2,753 |

What moved and why, from the filings: equity rose only when shares were sold (financing inflows of CDN$9,387,044 in FY2002)
and fell in every other year, because the company lost money in every year shown: net loss FY1998 (4,334), FY1999 (7,981),
FY2000 (2,688), FY2001 (3,635), FY2002 (1,131), FY2003 (8,047), FY2004 (2,218), FY2005 (163), FY2006 (3,009), and
(1,819) in the half-year to 2006-12-31 (CDN$000). At 2006-12-31, capital stock of CDN$43,797,995 stood against a deficit of
CDN$41,239,391: the owners had put in about CDN$43.8 million and the accounts showed about CDN$41.2 million of it lost. The
share capital was consolidated one-for-four in 1999, one-for-four in 2001 and one-for-three in 2003 (Item 4.A), forty-eight
old shares to one. The working-capital deficiency of 2006 is the Oakwell judgment carried in current liabilities
(CDN$7,686,971 at 2006-06-30; CDN$7,825,946 at 2006-12-31, against CDN$1,500,000 of restricted cash posted as security).
Reading "what the figures are saying and what they don’t say" **[M2025-032]**: the FY2002 total assets read 25,314 in the
FY2002 20-F and 25,415 in the FY2006 20-F, unexplained in the parts read; and the FY2006 20-F's US GAAP column shows
depletion of CDN$5,566,679 against CDN$729,856 under Canadian GAAP, and equity of CDN$867,362 against CDN$4,542,157 (Item
3.A), the gap being the carrying value of the oil and gas properties. The interim statements carry a going-concern note
(acc `0001049021-07-000009`, note 1: if the going-concern assumption "is not appropriate for these consolidated financial
statements then adjustments may be necessary to the carrying value of assets and liabilities").

**Owner cash and the reporting figures (for Q3, Q4, Q7). COMPUTATION, NOT A CLEARANCE.** By the brief's reporting
convention, not a verdict and not entry language. Script and output: `Test Runs/_research 2026-10-16 ENYN/computation.py`
and `Test Runs/_research 2026-10-16 ENYN/computation_output.txt`. Owner cash = cash from operating activities less
purchases of oil and gas properties (and, in FY2002, CDN$163,000 of capital assets), from Item 3.A of the two 20-Fs;
FY2002 to FY2004 include the discontinued M&M Engineering division's cash, which the selected data do not separate in the
cash-flow lines; no net-income proxy is used.

| FY to June 30 (CDN$) | 2002 | 2003 | 2004 | 2005 | 2006 |
|---|---|---|---|---|---|
| Operating cash flow | (2,020,541) | 621,878 | (3,052,995) | 4,625,926 | (789,226) |
| Oil and gas property spending | 2,759,206 | 354,625 | 1,740,154 | 1,001,743 | 6,535,176 |
| Owner cash after all capital spending | (4,942,747) | 267,253 | (4,793,149) | 3,624,183 | (7,324,402) |

- Five-year average: CDN$(2,633,772) after interest (equity-only); CDN$(2,628,984) before interest (all-equity; interest
  averaged CDN$4,788). The continuing oil and gas business alone, before depletion, capital spending and tax (net revenue
  less operating, administrative and interest costs), lost between CDN$1,444,899 and CDN$1,877,675 in every year, average
  CDN$(1,645,814): no case that charges nothing for capital turns positive.
- **Range, by Q7's convention in full.** The series changes sign (FY2003 and FY2005 positive), so the growth is measured
  between halves (FY2002-03 average CDN$(2,337,747); FY2005-06 average CDN$(1,850,110)); a growth rate of a negative series
  is meaningless, so by specific (b) the range is the no-growth case alone, said so. (a) cycle base: no year is called
  aberrational by the filer; the literal window is the base. (c) acquisitions: the FY2006 spending includes the Sawn Lake
  and Great Northern share purchases (cash CDN$2,126,608 and CDN$1,750,210, Item 4.A), deducted with the total, and no
  growth credited. (d) working capital: inside operating cash as filed. (e) the filing states no maintenance figure, so no
  maintenance case. (f) the cap: not reached, no growth carried. The floor tested first: no case earns the floor at any
  price, since every case is negative.
- **Net debt** at 2006-12-31: borrowings CDN$1,109,964 (short-term debt 225,834, promissory note 654,105, convertible
  debenture 15,152 + 143,151, due to shareholder 71,722) less cash and securities CDN$822,647 = CDN$287,317; plus the stated
  subsequent event, the Oakwell judgment made final by the Supreme Court's denial of leave on 2007-01-18 (acc
  `0001049021-07-000002`), CDN$7,825,946 less the CDN$1,500,000 posted = CDN$6,325,946; total CDN$6,613,263. The judgment
  is not a borrowing under Q7's definition; it is counted because a filing states it as a subsequent event that fixed a
  money claim ahead of the owners, and the figure without it is shown beside.
- **(a) VALUE RANGE** (the no-growth case alone, at 4.19%): about **CDN$-16.16 a share all-equity** (CDN$-14.68 without
  the judgment); **CDN$-14.64 equity-only**. Price: no usable quote (aggregator about US$0.00, flagged).
- **(b) FAIR PRICE** (each end case at ten percent, averaged; one end here): about **CDN$-7.66 a share all-equity**;
  **CDN$-6.14 equity-only**. Tax: the company paid little or no current tax in the window; owner cash is after whatever it
  paid, no conversion. Both figures are negative: on the filed record no price earns the floor.
- What the computation cannot see: the outcome of the bankruptcy. The figures value a going concern on its last five filed
  years; the shares' claim since 2007-03-20 is a residual after the trustee pays creditors, on no record found.

**Integrity facts (for Q5), recorded, not judged.**
- In September 2006 the company agreed to buy 1211115 Alberta Ltd., of which two of its own directors, James C. Cassina and
  Sandra J. Hall, owned 11.24% and 6.49% (20-F Item 7.B). 1211115 advanced CDN$650,000, which on failure of the deal became
  "a demand promissory note, the repayment of which is secured by the unencumbered assets of the Company"; the note stood at
  CDN$654,105 at 2006-12-31 (acc `0001049021-07-000009`), and 1211115 declared on 2007-02-14 that EnerNorth was "not in a
  position to close" (acc `0001049021-07-000011`). The board formed an independent committee and obtained a fairness
  opinion (Item 7.B).
- The chairman was awarded CDN$95,000 for FY2006 services; CDN$29,450 was paid to a firm controlled by the daughter of a
  director, Ramesh K. Naroola; the director and his daughter each own 1.5% of the Indian subsidiary EIPCL (Item 7.B).
- In August 2006 the company sold its KGPL shares to its own Barbados subsidiary CanPower for a demand note of
  CDN$5,760,595 (Item 7.B), an intra-group transfer.
- In the Oakwell litigation the company's defence in Ontario was that "Singapore does not adhere to the Rule of Law"; the
  Ontario courts recognised the judgment and the Supreme Court of Canada refused leave with costs (Item 8.A.7; acc
  `0001049021-07-000002`).
- Several 2007 6-Ks carry a signature date a year early ("Date: March 21, 2006" on the report dated March 21, 2007, acc
  `0001049021-07-000017`; likewise `0001049021-07-000013`, `0001049021-07-000011`, `0001049021-07-000002`): a clerical
  slip, recorded as found.
- Any later run that reaches Q5 must answer these **[M2013-088]**.

**For Q8.** On the computation, the government bond at 4.19% beats every case; "there’s just a point at which we drop out
of the game." **[M2003-149]**. Recorded, not weighed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      template copy and the notes file were made before the first EDGAR request; Q1 was committed (12c596b2) before this
      section was written.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatcher's (operator rule
      ten). Folding into the register is the dispatcher's; this run binds nothing until then.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (commit
      subjects, `git status` file names, the memory index) is declared under contamination at the top and not used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-16 ENYN/check_ids.py`); every filing fact has its
      accession; every number has a filing or is labelled COMPUTATION or CONVENTION.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance.
- [x] Owner cash from filed operating cash less capital spending, never a net-income proxy (operator rule 5); the sovereign
      from the Bank of Canada, named and dated, with the protocol's missing CAD row stated; aggregator quotes flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations paragraph); facts for later questions are
      under AFTER THE STOP, and the integrity flag is in the box line.
- [x] No point-in-time anchor: the run is dated today, so no row is barred by date.
- [x] `tools/run.py` refused this name; no line of it was used.
- [x] `python tools/check_framework.py` PASS before the commit.

**Honest gaps.** The trustee's estate file, SEDAR+ and the federal insolvency records were not reached; the FY2001, FY2003,
FY2004 and FY2005 20-Fs were downloaded but only their selected-data figures (as carried in the later 20-Fs) were used; the
interim MD&A to 2006-12-31 was downloaded and not read; finding cost was not located; no reserve report was read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The framework has no box for a company whose business no longer exists on the record. Section I says TOO HARD covers "a
business whose economics cannot be foreseen" and OUT "a question answered against it"; a company that assigned itself into
bankruptcy and has filed nothing for nineteen years fits both. OUT is arguable: the filings themselves show the business
surrendered to a trustee, so Q1 is answered against the name on the evidence. I chose TOO HARD (NATURE), as a CONVENTION of
this run, because no document shows how the bankruptcy ended (a residual to owners, though the computation and the rows on
creditors make it unlikely, is not disproved by any filing found), and OUT should rest on a fact found rather than on an
absence of facts. WORK was rejected because the only primary source left, the trustee's file, would describe a liquidation,
not a business, and a research pass could not produce the ten-year forecast Q1 asks for. A written rule for dark and bankrupt
filers (which box, which label, what re-look condition) would stop two analysts closing the same name OUT and TOO HARD.
Second: the protocol's sovereign table has no CAD row; the Bank of Canada long benchmark was used. Third: the reporting
convention asks for a fair price even where every case is negative; the negative figure is reported as computed, but the
definition does not say whether a negative figure should be reported, floored at nil, or replaced by "none", and a price
alert set on it would be meaningless.
