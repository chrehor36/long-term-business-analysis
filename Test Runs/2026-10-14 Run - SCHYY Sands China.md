# Company Run — Sands China Ltd. (HKEX: 1928; US OTC ADR: SCHYY) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-15), after the run was committed: not held (`PORTFOLIO.md` carries no line for SCHYY, 1928 or Sands China).

**Dispatch.** Run by a dispatched analyst under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the two
departures the brief states: the lines of evidence were derived by the analyst from the company's own annual report, and
the primary-document rules for a name with no current SEC filings replace the EDGAR lines where they cannot apply.

**Contamination, declared before any verdict (the blind rule).** No blind-listed file was opened, listed or searched.
Three things were seen without being sought, in the context the session started with: (1) the recent commit subjects of
the repository, among them a fold of another Macao concessionaire's run (GXYYY, 2026-10-14) whose subject line states its
box (TOO HARD (NATURE) at Q1) and its reason (the concession's end in 2032 with the casinos reverted, and policy-set falls
in Macao gaming revenue). That is a verdict on a rival in the same field on the same question this run must answer, and it
is the most material contamination this run carries: it could anchor Q1. It is not used. Q1 below is decided only on Sands
China's own filings, the opposite reading is stated and tested, and the rows that argue against the box are written down
first. (2) A git status listing showing research-folder names of other tickers (AYI, ARCB), not opened. (3) The memory
index lines loaded with the session (a queue state and a count of names), which say nothing about this name. None is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Tools.** `python tools/run.py SCHYY` refused: "SCHYY: not an SEC filer." `python Screens/cover_shares.py SCHYY`
  refused: "NOT AN SEC REGISTRANT in the live ticker file." Every figure below was taken by hand from the filed documents
  (arithmetic lines only, each checked against the filed statement); the arithmetic is in
  `Test Runs/_research 2026-10-14 SCHYY/compute.py`.
- **Price:** HK$11.29 per ordinary share (1928.HK) and US$14.28 per ADS (SCHYY), both 2026-10-14, Yahoo chart through
  `tools/sources.price`: **aggregator quotes, flagged** (operator rule 5). The quote date falls after the interim dividend's
  record date of 2026-09-18, so the price is ex that dividend.
- **ADR ratio:** one ADS represents ten ordinary shares, the same in all three depositary registrations found on EDGAR for
  Sands China Ltd. /ADR (CIK 1491703): JPMorgan Chase Bank F-6EF filed 2019-12-09, accession 0001193805-19-001923 ("each
  American Depositary Share representing ten ordinary shares"); Deutsche Bank F-6 POS filed 2017-09-29, accession
  0001193805-17-002601; Bank of New York F-6EF filed 2011-06-21, accession 0001019155-11-000330. The programmes are
  unsponsored; which depositary's ADS trades as SCHYY was not established, and the ratio is the same in all three.
- **Shares:** 8,093,379,566 ordinary shares issued and fully paid, no treasury shares: 2025 Annual Report, note 19 (share
  capital, "At January 1, 2024, December 31, 2024 and December 31, 2025 8,093,379,566"); unchanged at 2026-06-30 (2026
  Interim Report: weighted shares 8,093,380 thousand, and "Neither the Company, nor any of its subsidiaries purchased, sold
  or redeemed any of the listed shares"). Las Vegas Sands holds 6,053,847,874 (74.80%) through Venetian Venture Development
  Intermediate II; the public holds 25.20%.
- **Market cap:** 8,093.38M × HK$11.29 = HK$91,375M = **US$11,654M** at HK$7.8406 to the US$ (the interim report's own
  illustration rate).
- **Earnings currency and sovereign.** The group reports in **US dollars** (both reports: "US$ in millions"); its revenues
  are earned in patacas and HK dollars, the pataca pegged to the HK dollar and the HK dollar to the US dollar (2025 Annual
  Report, risk factor "We are subject to limitations of the patacas and HK dollars exchange markets"). The sovereign of the
  reporting currency is used: **US Treasury daily par yield curve, 30-year, 5.56%, dated 2026-10-13** (`tools/sources.py`,
  issuing authority).
- **Filings read** (operator rule 4; HKEXnews documents are identified by their file reference in place of an accession):
  - 2025 Annual Report, published 2026-03-31, HKEXnews `/listedco/listconews/sehk/2026/0331/2026033101127.pdf`: the
    business overview, the concession section (2.2), the management discussion and analysis (2.3), the priority risk factors
    (2.4), the stakeholder section, the financial statements and notes 8, 19, and the five-year summary.
  - 2026 Interim Report, published 2026-08-24, `2026/0824/2026082400464.pdf`: the results summary, outlook, balance sheet,
    cash flows, changes in equity, substantial shareholders, the interim dividend.
  - 2024 Annual Report, published 2025-03-26, `2025/0326/2025032600391.pdf`: cash flows and equity for 2023.
  - 2022 Annual Report, published 2023-03-30, `2023/0330/2023033000789.pdf`: the concession history (subconcession
    extension, the 2022 tender, the deeds of reversion), the COVID closures, Macao gross gaming revenue for 2022.
  - 2020 Annual Report, published 2021-03-25, `2021/0325/2021032500539.pdf`: the 2016 to 2020 summary and the 2019 and
    2020 cash flows.
  - 2016 Annual Report, published 2017-03-30, `2017/0330/ltn20170330415.pdf`: the 2012 to 2016 summary and the 2014 to
    2016 decline in Macao gaming revenue.
  - The XBRL facts of Sands China's 20-Fs filed with the SEC (CIK 1755281; the last 20-F filed 2023-03-30, accession
    0001755281-23-000018) for the 2016 to 2022 cash-flow lines.
  - Not read: Las Vegas Sands' 10-K and 10-Qs (the brief's facts from them are used only as the brief states them); the
    circulars on connected transactions (see What I could not get).
- **One figure cross-checked against the filed statement:** net cash from operating activities for 2020, US$(816)M in the
  2020 Annual Report's consolidated statement of cash flows (page 122) equals the XBRL value of the FY2020 20-F
  (CashFlowsFromUsedInOperatingActivities, −816); and 2025's US$2,105M in the 2025 statement (page 108) equals the
  management discussion's "Net cash generated from operating activities 2,105".
- **Arithmetic lines** (by hand; `tools/run.py` refused the name). Owner cash on the all-equity basis = net cash from
  operating activities (which under these statements is before interest paid and interest received, both outside it)
  less purchases of property, investment property and intangibles, plus disposal proceeds, less lease repayments, less the
  gaming-licence and franchise liability payments (the annual fee for the reverted gaming assets, classed in financing),
  less share-based compensation. US$M:

  | Year | Op. cash | Capex (all) | Owner cash | at 12% statutory tax | Revenue |
  |---|---|---|---|---|---|
  | 2016 | 2,346 | 1,151 | 1,177 | 1,021 | 6,543 |
  | 2017 | 2,626 | 477 | 2,145 | 1,938 | 7,586 |
  | 2018 | 3,049 | 532 | 2,494 | 2,242 | 8,665 |
  | 2019 | 2,812 | 754 | 2,032 | 1,765 | 8,808 |
  | 2020 | (816) | 1,038 | (1,879) | (1,879) | 1,687 |
  | 2021 | 88 | 640 | (571) | (571) | 2,874 |
  | 2022 | (473) | 241 | (749) | (749) | 1,605 |
  | 2023 | 2,293 | 231 | 2,022 | 1,875 | 6,534 |
  | 2024 | 2,072 | 871 | 1,147 | 994 | 7,080 |
  | 2025 | 2,105 | 553 | 1,485 | 1,349 | 7,443 |

  Five-year average 2021 to 2025: 667 (580 at the statutory rate). Depreciation and amortisation 2025: 792; 2024: 754.
  Share-based compensation is small (US$5M to 35M a year) and deducted. The statutory column charges the Macao complementary
  tax of 12% on operating profit, less tax actually paid, because the gaming exemption runs out inside ten years (Q7, Whose
  tax; see the COMPUTATION below).
- **The balance sheets, read first** **[M2025-032]** (read here because the file closes before Q4). US$M at 31 December
  (2012 to 2016 from the 2016 report, 2016 to 2020 from the 2020 report, 2021 to 2025 from the 2025 report, mid-2026 from
  the interim):

  | | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Jun 2026 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Total assets | 10,772 | 11,183 | 10,647 | 12,058 | 12,100 | 10,548 | 10,094 | 10,562 | 10,258 | 11,169 | 10,571 | 9,628 |
  | Equity | 5,839 | 5,007 | 4,538 | 4,409 | 4,446 | 1,929 | 888 | (700) | (4) | 1,031 | 1,401 | 1,287 |
  | Borrowings | 3,385 | 4,374 | 4,412 | 5,562 | 5,608 | 7,065 | 7,964 | 10,181 | 8,328 | 8,159 | 7,097 | 6,433 |
  | Cash | 1,283 | 1,284 | 1,239 | 2,676 | 2,471 | 861 | 678 | 790 | 1,361 | 1,970 | 1,505 | 851 |

  *(2026-10-15, on resuming: the borrowings for 2015, 2016 and 2023 read "n/r" (not read) until today; they are now filled
  from the 2016 Annual Report, note 25 (total borrowings 4,374 and 3,385, including finance leases on land), and the 2024
  Annual Report, note 22 (8,328 at 2023). Borrowings in every column are the carrying amounts as filed, lease liabilities
  included.)* What moved and why: the assets are a fixed plant of about US$10 to 12 billion
  and barely moved in eleven years; the equity was drawn down from US$5.8 billion to a deficit and back to US$1.3 billion,
  first by dividends larger than profit (about US$2.05 billion paid each year 2016 to 2019 against profit of US$1.2 to 2.0
  billion), then by losses of US$4.15 billion in 2020 to 2022, while borrowings rose from US$4.4 billion (2017) to US$10.2
  billion (2022), part of it a US$1.0 billion term loan from Las Vegas Sands (repaid March 2025). Receivables rose from
  US$188M to US$335M in 2025 with the credit provision ("increased in credit granted and increased aged casino
  receivables", 2025 Annual Report, MD&A). Current liabilities exceed current assets at both dates of the latest reports
  (net current liabilities US$345M at 2025, US$849M at June 2026). What the figures cannot say: what the gaming plant is
  worth after 2032, when by contract it reverts to the government (Q1).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]** *(corrected 2026-10-15 by the run's own citation check: this read `whether the buyer "would be happy buying
this stock if the market closed for five years"`, words not the row's own)*, which for this name means owning a Macao casino concessionaire through the end of its concession in
2032. The market serves and does not instruct **[M2006-077]**: the share price fell with each policy shock in the record
read and is no evidence either way. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too
close to think about" **[M1996-084]**. No macro forecast enters **[M2000-094]**; the question below is not a forecast of
China's economy but whether the business's own ten-year economics can be seen. **Contrary evidence, written down as
found** **[M1997-127]**: (1) in 2022 the Macao government re-awarded all six incumbents a new concession, so a renewal at
the next expiry has a precedent; (2) the speakers record that they "tended to overestimate the difficulties from
regulation" with television licences that "anybody could just ask to have your license jerked away", where "the way the
system evolved, that almost never happened" **[M2004-058]**; (3) "a license from the federal government became a royalty
stream on huge amounts of money" **[M2006-052]**; (4) "railroads, utilities, insurance companies, are all very much affected
by the political process. Fortunately, I think, in the railroad industry, you know, we’ve got economics on our side"
**[M2012-074]**; (5) Munger's "American investors are missing China [...] it just looks too hard, sitting in Omaha"
**[M2018-083]**. These are weighed at Q1.

## THE STANDING RULE
Owning a part-interest bought for cash, unlevered and sized so that its loss cannot touch what the buyer has and needs,
puts the buyer at no risk of ruin **[M2012-081]**, **[L2023-005]**; the target's own debt is a Q9 matter. Not reached as a
financing question in this run.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The lines of evidence, chosen by the analyst** (departure 1 of the brief), from the 2025 Annual Report: (i) the
concession: its term, the reversion of the gaming assets, renewal, redemption and the investment plan (section 2.2 and the
risk factor "Our Concession can be terminated or redeemed under certain circumstances without compensation to us"); (ii)
visitation from mainland China and the policies that govern it (MD&A overview; risk factor "The number of visitors to our
integrated resorts, particularly visitors from mainland China, may decline"); (iii) competition among the six
concessionaires and the cost of winning patrons (MD&A, adjusted property EBITDA; risk factor on competition); (iv) the tax
arrangements that end in 2027 (note 8; risk factor "Our tax arrangements with the Macao government may not be extended");
(v) the debt (risk factor on indebtedness); (vi) the relationship with Las Vegas Sands (business overview; corporate
expense). Lines (i) and (ii) decide Q1; the others are carried below.

**What the business is.** Sands China, through Venetian Macau Limited (VML), runs five integrated resorts in Macao (The
Venetian, The Londoner, The Parisian, The Plaza with the Four Seasons, and Sands Macao): 10,487 hotel rooms, about 2.1
million square feet of malls, 1.6 million square feet of meeting space, and 1,680 tables and 3,700 slot machines, the
maximum VML is allowed (2025 Annual Report, 2.1.2). Of 2025 net revenue of US$7,443M, casino was US$5,583M (75%), rooms
853, mall 521, food and beverage 270, other 216 (MD&A, Net Revenues). The casino is therefore the business, and it runs
under a government concession.

**The test, applied.**

1. **Where will it be in ten years?** **[M2000-037]** asks for "a reasonable probability of being able to asses where the
   business will be in 10 years"; **[M2012-065]** asks for "a reasonable fix on about what the earning power and competitive
   position will look like in five or 10 years". Ten years from this run is 2036. The concession does not reach it:
   "Our Concession expires on December 31, 2032. If our Concession is not extended or renewed, VML may be prohibited from
   conducting gaming operations in Macao, and we could cease generating revenues from our gaming operations when our
   Concession expires. In addition, upon the expiry of our Concession, the Gaming Assets [...] will be returned to the
   Macao government without compensation to us, along with any gaming-related equipment we acquire during our Concession.
   Furthermore, any new casinos, gaming areas and respective supporting areas that VML is authorized to operate during the
   Concession will revert to the Macao government without compensation to us." (2025 Annual Report, 2.2.1, page 15). The
   reversion is not a hypothesis: on 2022-12-30 VML and three other subsidiaries "entered into deeds of reversion, pursuant
   to which they confirmed and agreed to revert to the Macao government the Gaming Assets without compensation", and now
   pay an annual fee to use them (2022 Annual Report, 2.3; 2025 Annual Report, 2.2.1: US$14M in 2025, an estimated
   US$42M a year for the remaining seven years). The government may also redeem the concession on a year's notice from
   2029-01-01, with "fair compensation or indemnity" that "may not be adequate" (2025 Annual Report, risk factors).
2. **What are the key variables, and how predictable are they?** **[M1998-044]**: "trying to identify the key variables in
   that particular business, and evaluating how predictable they were first [...] If something is not very predictable,
   forget it." The filings name two that decide the cash. (a) **Whether, and on what terms, VML holds a gaming right after
   2032.** The terms are set by the Macao government in a tender. The last one changed them materially: the reversion of
   the gaming plant, a commitment to invest 35.84 billion patacas (about US$4.47 billion) by December 2032, 33.39 billion of
   it in non-gaming projects, with each year's projects subject to government approval and reallocation, and a rise in the
   required contributions to 5% of gross gaming revenue (2025 Annual Report, 2.2.1 and page 16; the 2016 report's figure was
   4%). The company's own words on the law: "Current Macao laws and regulations concerning gaming and gaming concessions
   are, for the most part, fairly recent and there is little precedent on the interpretation of these laws and
   regulations" (risk factors). (b) **Visitation from mainland China, which is set by policy.** "Slowdown in economic growth
   or changes of China’s current policies on travel and currency movements could disrupt the number of visitors"; "Policies
   and measures adopted from time to time by the Chinese government include restrictions imposed on exit visas" (risk
   factors). The record shows what such policy does: Macao gaming revenue fell for 26 consecutive months from May 2014 (2016
   Annual Report, Industry), and Sands China's revenue went from US$9,505M (2014) to US$6,820M (2015); travel restrictions
   from 2020 to 2022 took market visitation to "about 6 million visits in 2022, a decrease of approximately 86% compared to
   2019" and Sands China's revenue to US$1,605M, "approximately 18% of the year 2019" (2022 Annual Report). Owner cash went
   from US$2,494M (2018) to US$(1,879)M (2020). Neither variable is a figure the filings let an outsider fix.
3. **Do the past statements tell me the future ones?** Not across 2032. The statements show what the plant earns while the
   right to run casinos in it is held; they cannot show what it earns, or whether it earns from gaming at all, once the
   right lapses and the gaming plant is no longer the company's.
4. **Is it important and knowable?** "what you’re looking for is something — things that are important and knowable. If
   something’s important but unknowable, forget it." **[M2006-076]**. The terms of the 2032 tender are the most important
   fact about the business: they decide whether three quarters of revenue continues and what it costs to keep it. They are
   not knowable from any filing; they will be written by a government six years from now.
5. **Would the insiders write it down?** **[M2000-105]**: the insiders "would not want to put down on paper their
   predictions". The insider here does not: the company's own text says only that "If our Concession is not extended or
   renewed, VML may be prohibited from conducting gaming operations" and "There can be no assurance we will be able to
   obtain new licenses or renew any of our existing licenses". It writes no forecast of the renewal or its terms. That is the
   test of the cause: the deciding question is one the industry's insiders do not write down, so the cause is NATURE, and no
   research pass could answer it: "We couldn't solve this problem, moreover, even if we were to spend years intensely
   studying those industries. Sometimes our own intellectual shortcomings would stand in the way of understanding, and in
   other cases the nature of the industry would be the roadblock." **[L1993-023]**.
6. **Can I name the winner?** Inside the concession term the filing describes the company as seeking "to enhance our
   position as the leading developer and operator of integrated resorts and casinos in Macao" (2025 Annual Report, 2.1;
   the claim is the company's, not checked against rivals here); but whether any of the six holds the same position after 2032 is the question in test 4.
8. **How far off could I be?** **[M2011-084]**: "some model in our mind of how far off we can be. I mean there’s some things
   we can be way off on". Here the range runs from the gaming cash continuing on today's terms to the gaming plant handed
   back for nothing in 2032; the COMPUTATION below shows that difference to be most of the value.
11. **Abroad: do I understand the governance and the tax?** **[M2000-141]**: "where we think we understand the nuances of the
    corporate governance system and taxation and that sort of thing." The filings show both governed by the concession
    authority: the government approves any VML financing over 100 million patacas, any change of control, any
    recapitalisation, each year's investment projects, and may "require that we contribute additional capital" (2025 Annual
    Report, 2.2.1); the gaming tax exemption and the substitute dividend-tax agreement both end with tax year 2027, with
    "no certainty either of these tax arrangements will be extended" (risk factors; note 8). The speakers name exactly this:
    "there’s some disadvantages, always, to being in a culture that you don’t perfectly understand, or where tax laws can
    change, your ownership rules can change" **[M2005-016]**; and "We wouldn’t understand the tax laws as well, the nuances
    of governance, a whole bunch of things" **[M2006-021]**.

**The opposite reading, stated and tested.** The case for IN: all six incumbents were re-awarded in 2022, so renewal is
the precedent; a government licence can be a royalty stream **[M2006-052]**; the speakers once overestimated regulatory
risk in television licences **[M2004-058]**; politics bears on railroads too, and economics usually win **[M2012-074]**;
and the speakers would go into China if paid more for it **[M2006-021]**, which asks a lower price rather than a pass. The
reading fails on the filings for three reasons. First, the television row's point is that revocation "almost never
happened"; here the loss of the gaming plant at expiry already happened once, by contract, in 2022, and the terms were
re-set at the same time, so the precedent is a renewal on new terms the company did not choose, not a renewal on the old
ones. Second, the royalty-stream row itself says the stream lost value when more "highways" were built **[M2006-052]**, and
the Macao government "could grant additional rights to conduct gaming in the future" (risk factors), so even that row
does not make the right durable. Third, the price-for-China row speaks of "a business we understood at an attractive
price" **[M2006-021]**: it lowers the price for a business already understood; it does not supply the understanding. And
the speakers' own later record on a regulated industry is the warning: "In such jurisdictions, it is difficult to project
both earnings and asset values in what was once regarded as among the most stable industries in America. [...] I did not
anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**.

**The doubt rule.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
There is doubt, and it is about the main variable, not a side one. "we think of business risk in terms of what can happen
— say five, 10, 15 years from now — that will destroy, or modify, or reduce the economic strengths [...] In some businesses
that’s very — it’s impossible — to figure — at least it’s impossible for us to figure — and then we just — we don’t even
think about it then." **[M2000-014]**.

**Routing.** Not a fast-changing technology; the ten-year economics cannot be foreseen because the right to earn them is
granted by a government on terms it sets anew, and because the customers' ability to come is set by another government's
policy. Q1 owns the question whether the economics can be foreseen at all **[M2012-065]**; the file closes here.

- **VERDICT: TOO HARD (NATURE).** The deciding question, whether and on what terms VML will hold a gaming right after
  2032-12-31 (with its gaming plant reverting "without compensation" either way), is important and not knowable
  **[M2006-076]**; the insiders do not write it down **[M2000-105]**; study would not answer it **[L1993-023]**; and doubt
  means outside **[M2002-092]**. "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of
  its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. The box: "in, out, and too hard"
  **[M2006-013]**.

## Q2 TO Q12 — NOT REACHED (the file closed at Q1).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1**: whether, and on what terms, VML will hold a gaming right after its Concession
expires on 2032-12-31 (the gaming plant reverting to the Macao government "without compensation" either way) is a
forecast the industry's insiders do not write down **[M2000-105]**, and study would not answer it **[L1993-023]**. The
closed box: no research pass, and a lower price does not reopen it **[M2000-038]**. Q7 not reached; the COMPUTATION
below is not a clearance. **Integrity facts recorded, not judged** (the controlling shareholder's royalty and the featured
adjusted figure tied to pay, under Q4 and Q5 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source, written down as found **[M1997-127]**. None is
weighed; the box above is unchanged (operator rule 2).

**Q2, the castle, and the competitors.** The 2025 Annual Report names its rivals: "The other Concessionaires are SJM, Wynn
Resorts Macau, Galaxy, MGM Grand Paradise and Melco" (2.1.1, Competition in Macao), and adds casinos elsewhere in Asia,
online gaming and cruise ships. Three of the five report through parents that file with the SEC; **Galaxy and SJM do not
file with the SEC and were not read** (flagged). Each rival's Macao figures come from its own filings: Wynn Resorts 10-Ks
FY2019 (0001174922-20-000024), FY2022 (0001174922-23-000048), FY2025 (0001174922-26-000013), segment note, Macau
Operations; MGM Resorts 10-Ks FY2019 (0001564590-20-007393), FY2022 (0000789570-23-000008), FY2025
(0000789570-26-000018), segment note, MGM China; Melco Resorts & Entertainment 20-Fs FY2019 (0001193125-20-091982), FY2022
(0001193125-23-086859), FY2025 (0001193125-26-105023), the four Macao properties summed (Mocha, Altira, City of Dreams,
Studio City). Sands China from its own reports (the SCL 20-F FY2018, 0001755281-19-000042, for 2016 to 2018; the annual
reports for 2019 to 2025). The metric is each filer's own property-level earnings figure: adjusted property EBITDA for
Sands China and Melco, Adjusted Property EBITDAR for Wynn and MGM (defined differently, so the margins are indicative, not
identical). US$M, Macao only; arithmetic in `compute.py`.

| | Revenue 2017-19 | Revenue 2023-25 | Change | Margin 2017-19 | Margin 2023-25 | Property EBITDA 2020-22 (sum) | Margin, nine years |
|---|---|---|---|---|---|---|---|
| Sands China | 25,059 | 21,057 | −16.0% | 35.4% | 32.6% | (410) | 29.3% |
| Wynn Macau Operations | 14,033 | 10,501 | −25.2% | 30.2% | 30.6% | (362) | 25.6% |
| MGM China | 7,214 | 11,638 | +61.3% | 25.6% | 27.1% | (372) | 21.6% |
| Melco, Macao properties | 14,082 | 11,467 | −18.6% | 27.0% | 26.4% | (161) | 22.7% |

Over the whole span the four rank the same on margin in both phases, Sands China first; three of the four took in less in
2023 to 2025 than in 2017 to 2019, and all four lost money at the property level over 2020 to 2022 together. Sands China's
share of the four's Macao revenue: 41.2% (2017), 41.3% (2019), 41.1% (2023), 37.9% (2024), 37.1% (2025), while MGM China's
rose (MGM Cotai opened in 2018). The company's own 2025 account: "While revenues and our market share of gross gaming
revenues increased, we incurred higher sales and marketing costs to attract patrons to our properties and increased payroll
costs due to the competitive environment, resulting in an overall decrease in adjusted property EBITDA" (MD&A). The gaming
price is set by the state, not the firm: "we must pay a special gaming tax of 35% of gross gaming revenues", plus the
contributions and a minimum special gaming premium if gaming tax falls below 4.50 billion patacas a year (2.2.1). The
government "could grant additional rights to conduct gaming in the future" (risk factors).

**Q3, capital.** Capital spending (property, investment property, intangibles) averaged US$649M a year over 2016 to 2025,
against depreciation and amortisation averaging US$717M (2023: 809, from the 2024 Annual Report). The Concession binds
VML to invest 35.84 billion patacas (about US$4.47 billion) by December 2032, 33.39 billion of it non-gaming, project by
project with government approval (2025 Annual Report, 2.2.1); the filing does not split this into what keeps the
Concession and what grows the business. The plant is about US$10 to 12 billion of assets and barely moved in eleven years
(Step 0).

**Q4, the accounts.** The balance sheets are read in Step 0. The figure the company features is "adjusted property
EBITDA", which it says management uses "as a basis for determining certain incentive compensation" (2025 Annual Report,
MD&A and note on segments); it was US$2,312M in 2025 against owner cash (all spending, leases, the licence fee and stock pay
deducted) of US$1,485M and net cash from operations of US$2,105M. Net current liabilities US$345M (2025) and US$849M (June
2026). Credit and aged casino receivables rose in 2025 (Step 0). The cross-check of one figure is in Step 0.

**Q5, who runs it (integrity facts, recorded, not judged).** (1) Las Vegas Sands controls 74.80% (Step 0) and is paid by
the company it controls: under the International Trademark License Agreement "each Licensee paid LVS an annual royalty at
the rate of 1.5% of its gross non-gaming and gaming revenue", US$118M in 2025 of total royalty fees of US$127M (2025
Annual Report, Continuing Connected Transactions; note on expenses), with a Shared Services Agreement renewed yearly beside
it. (2) The featured adjusted figure is a basis for incentive pay (Q4 above). (3) A claim by Asian American Entertainment
Corporation, filed 2012 in Macao against VML and three LVS entities over the joint bid for the 2001 concession tender, was
raised in 2019 to 96.45 billion patacas (about US$11.93 billion); the Macao court held the claim against VML "unfounded" in
2014 and AAEC appealed; the proceedings were still open in the 2025 Annual Report (Contingent liabilities). Not judged here;
any later run that reaches Q5 must answer them.

**Q6, the money and the owners.** Dividends of about US$2.05 billion a year were paid in 2016 to 2019 against profit of
US$1.2 to 2.0 billion, and equity fell from US$5.8 billion (2015) toward the deficit of 2022 (Step 0). A dividend of
HK$0.99 a share (US$1,025M) declared 2020-01-17 was paid in February 2020, as the closures began; on 2020-04-17 the Board
recommended no final, and none was paid until 2025 (2020 Annual Report, note 10; 2022 Annual Report). Dividends resumed with
HK$0.25 final for 2024 (paid June 2025) and HK$0.25 interim for 2025 (paid September 2025), US$517M in all (2025 Annual
Report, note 10), then HK$0.50 final for 2025 (paid June 2026, about US$517M) and HK$0.50 interim for 2026 (declared
2026-08-14, about US$516M, paid 2026-10-09) (2026 Interim Report, note 6). No shares bought back or issued (2026 Interim Report). The dividends from VML's gaming profits are subject to a
12% tax or a substitute annual payment under an agreement that ran to 2025 and whose extension to 2027 has been requested
(2025 Annual Report, risk factors).

**Q9, the target's debt.** Borrowings US$6,433M at June 2026 (senior notes US$4,550M due 2027 to 2031, bank loans US$1,756M,
lease liabilities US$164M), cash US$851M (2026 Interim Report, note 11 and balance sheet); interest paid US$381M in 2025.
Borrowings peaked at US$10,181M in 2022. The government may redeem the Concession from 2029-01-01 with compensation that
"may not be adequate", must approve VML financings above 100 million patacas, and may require more capital (Q1).

**Q12, how the money is made.** The business is a casino operator: casino revenue was 75% of 2025 net revenue (Q1). The
rows name the business: "It’s a dirty business, and I don’t think you’ll find a casino soon in Berkshire Hathaway."
**[M2007-018]**; and for a marketable stake the rows record owning what they would not run, "I do not have a problem
buying stock in companies" **[M2004-075]**. Recorded, not weighed (Q12 is optional and not reached).

## COMPUTATION NOT A CLEARANCE: Q7 AS IT WOULD BE BUILT (reporting figures at the owner's request)
*The file closed at Q1. Nothing here is a verdict or entry language (operator rule 3). The two figures are the reporting
convention of Part VII, The owner's price; the construction is Q7's range convention, its specifics and the floor.*

- **Inputs.** Price HK$11.29 a share and US$14.28 an ADS (2026-10-14, aggregator, flagged). Market cap US$11,654M.
  **Net debt US$5,971M**: borrowings at face excluding lease liabilities US$6,306M (2026 Interim Report, note 11: senior
  notes 4,550 plus bank loans 1,756) less cash US$851M, plus the interim dividend of about US$516M that the interim report
  states was declared after the balance-sheet date (note 6). **CONVENTION of this run:** the IFRS 16 lease liabilities
  (US$164M) are left out of net debt because their principal repayments are already deducted inside owner cash, so the
  cost is charged once (the floor convention leaves operating leases out; under IFRS 16 they sit inside borrowings); the
  restricted bank deposit of US$125M is not counted as cash. Value of the business at the price: US$17,625M. Rate: the
  US Treasury 30-year, 5.56% (2026-10-13). HK$ at 7.8406 to the US$ (the interim report's rate); per ADS = ten shares.
- **Tax (Q7, Whose tax).** The gaming-profit exemption from the 12% complementary tax runs "through December 31, 2027"
  with "no certainty" of extension (2025 Annual Report, note 8 and risk factors). Owner cash is computed at the statutory
  12% on operating profit less tax paid, and the shelter's present value for 2026 and 2027 (12% of 2025 operating profit
  of US$1,231M less US$12M paid, two years at 5.56%) is added: US$250M. **CONVENTION of this run:** the text's convention
  names carryforwards and credits; a time-limited statutory exemption is treated the same way, because it is cash for its
  life and not after. Tax as paid is shown beside.
- **(a) The base.** The literal window 2021 to 2025 opens on 2021, a year of closures and travel restrictions by the
  filer's own description (2022 Annual Report), and its first three years are aberrational. The base is the average over
  the full cycle read, 2016 to 2025 (the 2016 low after the 2014 to 2016 fall in Macao gaming revenue, the 2018 peak, the
  2020 to 2022 closures, the recovery): **US$798M** a year at the statutory tax (US$930M as paid). The literal window is
  shown beside: US$580M.
- **(b) The growth.** Successive cycles cannot be compared, because only one cycle of owner cash was read; the series
  changes sign, so Q7 (b) measures the growth between the halves of the window: 2016 to 2020 averaged US$1,017M, 2021 to
  2025 US$580M, **−10.64% a year**. A decline is carried as the bottom of the range and the no-growth case is the top.
  Beside it: the two operating phases either side of the closures (2016 to 2019 against 2023 to 2025), −3.24% a year; the
  revenue over the same phases, −1.80%.
- **(c) Acquisitions:** none in the span. **(d) Working capital:** inside net cash from operations, counted. **(e)
  Maintenance:** the filing does not separate maintenance from the Concession's mandated investment (Q3 above), so the
  all-spending case is central; the depreciation variant is beside (base US$727M). **(f) The cap:** no growth above zero is
  carried, so the cap does not bind (the highest owner-cash share of sales in the span, 28.7%, is not approached).
- **The floor, tested first.** At the price, the central top (no growth) returns 4.60% a year and the bottom 1.67% on the
  all-equity basis. **No case of the range earns the floor of about ten percent**: "there’s just a point at which we drop
  out of the game" **[M2003-149]**. Had Q7 been reached, it would have closed OUT on the floor, whatever the width.
- **(a) VALUE RANGE, central, all-equity basis: HK$0.55 to HK$8.37 a share** (HK$5.48 to HK$83.71 an ADS; US$0.70 to
  US$10.68 an ADS), against **HK$11.29** (US$14.28 an ADS). The price is above the top of the range. Width: 2.28 to one on
  the value of the business, 15.3 to one per share after net debt.
- **(b) FAIR PRICE, all-equity basis (central): HK$0.27 a share** (HK$2.75 an ADS; US$0.35 an ADS): each end case valued
  at ten percent, the two averaged, less net debt, after the company's own tax at the statutory rate with the shelter added.
  **Equity-only beside it: HK$3.52 a share** (HK$35.22 an ADS; US$4.49 an ADS): owner cash after net interest paid, base
  US$544M, halves growth −23.84%, range HK$1.92 to HK$9.72. The all-equity figure is the central one; the equity-only figure
  never decides alone.
- **Beside, not central** (per share, all-equity): with the phase growth of −3.24%, range HK$5.23 to HK$8.37, fair HK$1.44;
  tax as paid on the cycle base, HK$6.71 to HK$10.67; the literal window, HK$2.28 to HK$4.56; the base 2023 to 2025
  (US$1,406M), HK$13.43 to HK$18.96, its top returning 8.09% at the price; trough to trough 2016 to 2024, top HK$7.30;
  peak to peak 2018 to 2023, top HK$2.25; the depreciation variant, top HK$7.12.
- **The one sensitivity that reaches the floor, not a case of the range.** The four years before the closures (2016 to
  2019) carried flat for ever return 10.02% at the price at the statutory tax (value HK$24.80 a share) and 11.29% with the
  exemption kept for ever (HK$28.64). It is not a case of the range under (a): it takes the peak phase as the base and
  drops the trough, and the years since reopening do not show it (Sands China's Macao revenue 2023 to 2025 was 16.0% below
  2017 to 2019). Written down because it is the evidence most favourable to the name.
- **The Concession case, beside.** The range convention carries cash for ever after year ten; the Concession ends after
  year seven, with the gaming plant reverting. Seven years of the cycle-base cash and nothing after is worth US$4,778M,
  less than net debt: HK$(1.16) a share (HK$2.18 on the 2023 to 2025 base). The gap between this case and the range is the
  question Q1 found unknowable.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 8761bad5, before the first download). **Partly kept on
      write-early:** the first session wrote Step 0, the foundations, the standing rule and Q1 and committed them together
      (0436fc8c) before it was killed, not one commit per section; the resuming session (2026-10-15) committed after each
      section it closed (3c9821ad, 2b0657ba, and the final commit).
- [ ] Dispatched: the brief allowed per-section pathspec commits, and they were made. Whether the dispatching session holds
      the lock was not checked by the analyst; the fold is the dispatcher's (operator rule ten). A run not in the register
      binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen without being sought and
      declared, not used: (1) at both sessions' start, the recent commit subjects, which carry another Macao
      concessionaire's run (GXYYY) with its box, its reason, its rate, its range and its fair price, and name the rivals it
      read; the resuming session saw them again in its own `git log` output. This run's box was written by the first
      session; its sovereign (US Treasury, chosen on the reporting currency) and its rivals (taken from the report's own
      list) were kept on their own reasons and not changed after seeing them. (2) A git status listing naming other
      tickers' research folders (AYI, ARCB), not opened. (3) The memory index lines loaded with the session, which do not
      name this company.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; no E-ids (`check_cites.py` in the research folder). Filing facts
      carry the HKEXnews document reference and date in place of an accession (no SEC filings for the current years), the
      SEC accession for every rival's filing and for the SCL 20-Fs. **One defect found and corrected:** the M1997-109
      quote in the foundations was not the row's own words (dated note in place).
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance, and the Q7 figures are headed COMPUTATION
      NOT A CLEARANCE.
- [x] Owner cash after every real cost (all capital spending, lease repayments, the gaming-licence and franchise payments,
      stock pay), never a net-income proxy; the sovereign from the US Treasury par curve, dated; the price flagged as an
      aggregator quote.
- [x] Contrary evidence written down as found (the foundations and Q1's opposite reading; the most favourable sensitivity
      written beside the computation); the facts for later questions are under AFTER THE STOP, and the integrity flag is in
      the box line.
- [x] No row dated after an anchor: not a point-in-time run.
- [x] `tools/run.py` refused the name; none of its output was used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A right to earn that ends inside ten years.** Q7's range carries owner cash for ten years and then for ever at no
growth; it has no instruction for a business whose licence to earn ends by contract in year seven, with its plant handed
back. The range was built as the convention says and the Concession case was shown beside it; the gap between the two is
most of the value, which is why Q1 owns the question. (2) **Q7 (a) against (b).** Where only one cycle of owner cash was
read, (a)'s "between the averages of successive cycles" cannot be measured, and the series changes sign, so (b)'s halves
apply; but the halves of 2016 to 2025 place one closure year in the first half and two in the second, so the rate (−10.64%)
measures where the closures fall as much as any growth. The literal text was followed and the phase comparison (−3.24%)
shown beside; the fair price moves from HK$0.27 to HK$1.44 between them. (3) **The width test's basis.** The three-to-one
width is not said to be measured on the business or per share after net debt; here it is 2.28 to one on the business and
15.3 to one per share. The floor test decided first, so it did not matter here. (4) **Whose tax.** The tax convention
names carryforwards and credits; a time-limited statutory exemption (gaming profits exempt to 2027, renewed before) is not
named; it was treated the same way and confessed as a CONVENTION of this run. (5) **Net debt under IFRS 16.** The
all-equity convention leaves operating leases out of net debt, but under IFRS 16 every lease sits inside borrowings; the
lease liabilities were left out because their principal is already inside owner cash (CONVENTION of this run). (6) **The
earnings currency.** Operator rule 5 asks for the sovereign of the earnings currency; this company reports in US dollars
and earns in patacas and HK dollars pegged to it. The first session took the reporting currency (US Treasury); the
protocol's table does not settle which is meant. The rate moves the range, not the floor test or the fair price, both of
which are computed at ten percent. (7) **The accession rule for a name with no SEC filings.** The template asks for an
accession on every filing fact; HKEXnews file references were used in its place, as the brief allows.
