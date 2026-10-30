# Company Run: Rantizo, formerly SKK Holdings Limited (Nasdaq: RNTZ, formerly SKK), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 2c482f5c). Every judgment cites a v5
ledger id in bold; every filing fact carries its accession. Dispatched blind run; working folder
`Test Runs/_research 2026-10-17 SKK/` (notes, fetch and check scripts; raw filings in its gitignored cache).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, 2026-10-17, after the run was committed: **not held** (`PORTFOLIO.md` read for this one ticker, under SKK and RNTZ).

**Contamination, declared and not used.** Before any fetch the session context showed, without my opening anything: the
git status snapshot (commit subjects of another company's run, SNIRF, and the names of other runs' research folders, AYI
and ARCB, with uncommitted files), and a memory index line describing the state of an earlier queue (a count of
gate-clearers and the next name in that queue). None concerns this company; none was used. I opened no other run file,
holding review, `PORTFOLIO.md`, register, reading list or session-state file, and searched no `Test Runs/` text.

**This brief's departure from the canonical brief**, as the brief states it: the lines of evidence were left for me to
derive. The lines I chose, and why: (1) what was bought, its own history, revenue and losses (the asset purchase 6-Ks, the
proxy, the pro forma), because the acquired assets are almost all of what the price now pays for; (2) the legacy
business's tender model, customers and competition (20-F Items 3.D and 4), because it is the only part with a record;
(3) the share count, the issuance record and the insiders' side of the deal (424B5s, 6-Ks, S-8s, Forms 3 and 4), because
the deal was paid in shares; (4) the balance sheets FY2021 to FY2025 and the cash flows (F-1, both 20-Fs), for Q4 and the
computation.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Which business is judged.** The company as it stands on the price date: the Singapore subsurface-utility contractor
  (SKK Works and SKK M&E) plus the drone-based technology assets bought from Rantizo, Inc. on 2026-10-09 (6-K of
  2026-10-13, 0001493152-26-046697). What the filings say of the acquired assets' own record: the seller described itself
  at signing as "developing drone-based technology used in agricultural spraying, seeding, and monitoring" (press release,
  6-K of 2026-05-05, 0001493152-26-021165, ex99-1); the APA recites assets used "for agriculture, military defense,
  forestry emergency response and commercial applications" and excludes every seller contract, customer contracts
  included, not listed on Schedule 1.1(a) (APA, same accession, ex10-1, filed as page images; the schedule itself is not
  among the pages read). **No financial statements of the seller or of the acquired assets are filed** in any filing read
  (sweep: the 20-F, F-3, F-3/A, three 424B5s, every 2026 6-K and its exhibits, the S-8 of 2026-10-16). The pro forma
  statement of operations for FY2025 (6-K of 2026-09-25, 0001493152-26-044299, ex99-1) adds **no revenue and no cost of
  revenue** for the acquired assets; its only operating adjustments are transaction costs, stock pay and five-year
  depreciation of the drone equipment. The filer's preliminary purchase price allocation: property and equipment
  $380k, intangible asset $6,538k, goodwill $252,671k, total consideration $259,589k ($258,830k of shares at the
  then-assumed $4.39 VWAP plus $759k cash). So 97% of the price is goodwill, by the filer's own allocation.
- **Price:** $4.53 (close 2026-10-16, RNTZ; Yahoo chart, aggregator, flagged per operator rule 5, live quote only; that
  day's volume 8,200 shares). Closes the week before: $4.55 (10-06), $5.08 (10-07, 10-08), $5.45 (10-09), $6.08 (10-12,
  the last SKK-ticker day), $4.50 (10-13).
- **Shares by class, built from the filings** (the tools' counts are stale: `Screens/cover_shares.py SKK` and `RNTZ`
  both print 18,750,000 from the FY2025 20-F cover, a pre-consolidation, pre-issuance count):
  - 2,105,332 Class A + 1,085,264 Class B outstanding as of 2026-08-12 (424B5 of 2026-08-14, 0001493152-26-038282);
  - + 770,000 Class A, registered direct offering closed 2026-08-17 at $4.46, paid in Tether USDT (6-K of 2026-08-18,
    0001493152-26-039007);
  - + 51,966,591 consideration shares, + 2,409,300 Management Shares, + 2,000,000 AGP Shares at closing 2026-10-09; the
    1,085,264 Class B converted to Class A on transfer to the seller (6-K of 2026-10-13, 0001493152-26-046697);
  - **= 60,336,487 Class A shares, one class; no treasury shares found.** Check: the pro forma count of 67,930,983
    (0001493152-26-044299) reconciles to the same pre-deal 3,190,596 (2,448,679 + 41,917 ATM shares + 700,000 plan
    shares) with the deal shares at the then-assumed $4.39 plus 770,000 RDO shares and 2,277,904 PIPE shares.
  - **Not counted, pending:** the seller's $10M PIPE (shares at the $4.9807 closing VWAP, about 2,007,750) and the
    company's own $10M capital raise, both deferred to 2026-10-16 by the Waiver (ex99-2, 0001493152-26-046697); no 6-K
    reporting either was on EDGAR at the price date. The S-8 of 2026-10-16 (0001493152-26-047398) registers 6,000,000
    more shares under the "Rantizo 2026-2027 Equity Incentive Plan".
- **Market cap:** 60,336,487 x $4.53 = $273.3M (about $282M with the pending PIPE shares).
- **Sovereign for the earnings currency.** The filer's reporting currency is the U.S. dollar; its functional currency
  and "almost all" revenue and costs are Singapore dollars (20-F FY2025, 0001493152-26-016229, Foreign Currency Exchange
  Risk). As the brief directs, the SGD long rate: **2.41%, the SGS 30-year benchmark yield, 2026-10-16**, Monetary
  Authority of Singapore, SGS Prices and Yields, Benchmark Issues (average buying rates of SGS primary dealers), read
  from the MAS form by `mas.py` in the research folder. The protocol's table has no SGD row; MAS is the issuing
  authority's own statistics service. Shown beside: US Treasury 30-year par yield 5.43%, 2026-10-16 (`tools/run.py`),
  since the acquired assets are a U.S. business.
- **Filings read** (operator rule 4): 20-F FY2025 (filed 2026-04-10, 0001493152-26-016229); 20-F FY2024 (2025-05-15,
  0001641172-25-011043); F-1 (2024-01-29, 0001493152-24-004123) for FY2021 and FY2022; the 2026 6-Ks of 04-01
  (0001493152-26-014559), 04-20 (0001493152-26-018044), 05-05 (0001493152-26-021165), 06-05 (0001493152-26-027479,
  the EGM proxy at ex99-3), 06-24 (0001493152-26-029899), 08-18 (0001493152-26-039007), 08-19 (0001493152-26-039241),
  09-25 (0001493152-26-044299), 10-13 (0001493152-26-046697); F-3 (0001493152-26-021236) and F-3/A
  (0001493152-26-022637); 424B5s of 05-18 (0001493152-26-024103), 07-31 (0001493152-26-035691), 08-14
  (0001493152-26-038282); S-8 of 2026-10-16 (0001493152-26-047398); Forms 4 of Liao (0001493152-26-047232), Ng
  (0001493152-26-047081), Sze (0001493152-26-047072), McInerney (0000919574-26-006971) and her Form 3
  (0000919574-26-006969). No proxy statement in the 10-K sense: a foreign private issuer; the EGM proxy is the 6-K
  exhibit named. **One figure cross-checked against the filed statement:** FY2025 revenue $12,949k and operating cash
  flow $(512)k in the filed statements of the 20-F (F-3 and the cash-flow statement) match the XBRL that `tools/run.py`
  read (OCF -0.5M) and the historical column of the pro forma (revenue 12,949).
- `python tools/run.py SKK` arithmetic lines only (RNTZ returned "not an SEC filer", the ticker map not yet updated):
  OCF $0.2M, $3.3M, $(0.5)M for FY2023 to FY2025; capex $3.0M, $7.8M, $5.1M; D&A $1.2M, $1.4M, $1.5M; stock pay found
  only in FY2025 ($2.4M; none in the cash-flow statements of FY2023 and FY2024, read); finance-lease principal $0.6M,
  $0.4M, $0.9M (the alternate it prints; used here, since equipment is acquired under finance leases: right-of-use
  assets obtained for finance leases $679k, $1,647k, $1,401k, FY2023 to FY2025, 20-F FY2025 supplemental cash flow).
  Its price line ($6.08, 2026-10-12) is the stale SKK quote and is not used. Owner cash is computed by hand below
  (AFTER THE STOP, Q4 facts) over FY2021 to FY2025.
- **Balance sheets:** the file closes before Q4; they were read in Step 0 and are set out under AFTER THE STOP (Q4).
  Five year-ends exist (FY2021 to FY2025); the company was formed in 2023 and no filed statement before FY2021 was found
  (the F-1 covers FY2021 and FY2022), so the eight-to-ten-year reading **[M2025-032]** is short by necessity.

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. A share is a business: "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**; what the price now pays for is a set of drone assets with no filed earnings, valued by a
banker for the seller's side of a share deal, so the question is what the assets will produce, not what the next
holder will pay. Who is paid to tell you: the valuation and fairness opinion came from Newbridge Securities, and A.G.P.,
the exclusive financial advisor, was paid 2,000,000 shares at closing and is also the company's at-the-market sales agent
(6-K of 2026-10-13; 424B5 of 2026-05-18); "you do not get impartial advice from Wall Street" when there is an
"enormous amount of fees possible from one action, and no fees applicable from another action" **[M2020-037]**, and
"don’t ask the barber whether you need a haircut" **[M2011-083]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the legacy business is real and audited, with ten-plus years of operation, public-utility customers
(PUB, Singtel) and six new fixed-price awards worth about S$34.1M announced 2026-08-19 (0001493152-26-039241), more than
two years of its FY2025 revenue; (2) the board formed a special committee of independent directors and took a valuation
range ($254.8M to $290.7M) and a fairness opinion (proxy, 0001493152-26-027479, ex99-3); (3) the APA conveys patents,
software, firmware, trade secrets and permits used in the drone business, so something identifiable was bought; (4) the
seller's holders accepted shares, not cash, and a six-month lock-up. Each is weighed where it bears.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought outright with the buyer's own money and sized as any
speculative small position: "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. The rule binds the buyer's conduct; nothing in
it is triggered by the target unless the purchase were financed or sized beyond a total loss being bearable. No
finding against the name here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "can I understand it? And unless it’s going to be in a business that I think I can understand, there’s no
sense looking at it." **[M1995-051]**; understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years"
**[M2000-037]**.

**Which part decides, and a convention of this run.** The company now has two parts. Q1's holding-company paragraph
reads a company by its parts, and "a part that cannot be [understood], and that matters, keeps the whole outside the
circle", "matters" being defined by Q2's threshold: more than half of five-year operating profit, or else the largest
part. Read literally, that threshold hands the decision to the legacy contractor, because the drone assets have no
filed operating profit at all (the five-year operating profit of the legacy part, FY2021 to FY2025, is $1,312k,
$1,552k, $325k, $512k and $(2,534)k as last filed, a positive sum; the drone part's is not on any filing). **CONVENTION of
this run:** where a part was bought after the five-year window and has no filed operating record, whether it "matters"
is read from the filer's own measure of its size, the purchase price and its allocation; rationale: a threshold on
five years of operating profit has no input for a part with no five years, and a missing figure is not a zero. By that
measure the drone assets matter beyond doubt: $259.6M of consideration (6-K of 2026-09-25) against a legacy business
whose shares had a market value of roughly $13M to $14M before the deal (3.19M shares at $3.98 to $4.46, proxy and RDO
filings) and book equity of $7.2M (20-F FY2025); the company took their name; the new President leads "all
drone-related business operations, developing new markets, driving acquisitions and partnerships" (6-K of 2026-09-25,
0001493152-26-044299). The reading under the literal threshold is given at the end of this section; it closes the file
too.

**The drone part, against the tests.**
- **What it is, on the filings:** a business the seller itself described at signing as "developing drone-based
  technology" (0001493152-26-021165, ex99-1), with no revenue in the pro forma statement of operations, no filed
  financial statements, no customers named, no competitors named, and customer contracts excluded from the sale unless
  scheduled (APA, Section 1.1(b)(i)). The acquisition criteria ask for "Demonstrated consistent earning power (future
  projections are of no interest to us, nor are "turnaround" situations)" **[R1997-001]**; no earning power is
  demonstrated in any filing read.
- **Q1's own list rules out the start-up:** "Start-ups are not our game." **[L2007-015]**; "I say, “We don’t do
  startups.” They don’t exist." **[M2008-088]**. A pre-revenue asset bundle still being developed is a start-up on
  the filer's own words.
- **The ten-year question (tests 1, 2, 5, 6):** the key variables (drone unit economics, adoption by growers, FAA and
  state rules on spraying, the price of rival aircraft and services) are not given for even one year; management frames
  the horizon as "the next 24 months as a decisive window" (0001493152-26-021165, ex99-1), and no forecast of the
  economics ten years out is written anywhere in the filings; the test is whether insiders would write one, and of a
  technology field the row says they "would not want to put down on paper their predictions" **[M2000-105]**. "We just
  don’t know the economics of it 10 years from now." **[M2000-104]**. Even granting growth in farm drones, "Just because
  Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge what its profit margins
  and returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**; and no winner can be
  named from these filings **[M2012-067]**.
- **Technology:** "if something comes in where there’s a technological component that’s of significance [...] it won’t
  make it through the filter." **[M1998-008]**; "a business that must deal with fast-moving technology is not going to
  lend itself to reliable evaluations of its long-term economics." **[L1993-023]**.
- **Test 3, do the past statements tell me the future ones?** There are no past statements of this part **[M2008-033]**.
- **Test 9, doubt:** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.

**The legacy part, for completeness.** A subsurface-utility contractor (cable laying, pipelines, sewer rehabilitation,
horizontal directional drilling) for Singapore public-sector projects, won by tender or quotation project by project,
with the top five customers at 96.0% of FY2025 revenue and no long-term contract with any of them (20-F FY2025, Item 3.D: "we have not entered into long-term contracts with any of our top five (5) key customers"). Its
economics are plain enough to read from the filings; it is inside the circle as a business whose figures can be read.
It does not decide, and it does not rescue the part that does.

**WORK or NATURE, OUT or TOO HARD.** No filing not yet read could tell the drone part's economics: the seller is a private
company, its statements are not filed, and the filer's own pro forma shows none. So this is not TOO HARD (WORK). Q1's
list sends start-ups to OUT **[L2007-015]**, **[M2008-088]**, while it sends fast-moving technology to TOO HARD (NATURE)
**[L1993-023]**, **[M2000-038]**. The start-up item is the more specific of the two and fits the filed facts exactly (no
revenue, and a stage the seller itself calls developing), so the box is **OUT**; the technology route would give TOO HARD (NATURE), and both close the file
with no lower price reopening it **[M2000-038]**. Which of the two governs a technology start-up is recorded under
"What in the framework was wrong or unclear".

**Under the literal threshold (the legacy part decides).** Q1 would pass on the legacy contractor and Q2 would close the
file OUT: the business tenders against "932 contractors registered with the BCA under the CW02 (civil engineering)
workhead", competes on price with "keen competition and significant downward pricing pressure", has no price-adjustment
mechanism in most contracts (20-F FY2025, Item 3.D), and its customers buy on the low bid: "most insureds don't care from
whom they buy" **[L2004-003]** is the commodity mark, and the See's question, "would people still want [...] in
preference [...]? And it wouldn’t be a question of people buying candy for the low bid." **[M2017-009]**, is answered no
by a tender. Those facts are recorded under AFTER THE STOP (Q2). Either reading closes the file OUT; the box does not
depend on the convention above.

- **VERDICT: OUT.** The business that the price now pays for, the drone-based technology assets, is a start-up with no
  filed revenue, statements or customers (6-K of 2026-05-05, 0001493152-26-021165; pro forma, 0001493152-26-044299);
  "Start-ups are not our game." **[L2007-015]**. The file closes here; Q2 to Q12 are NOT REACHED.

## Q2 to Q10, Q12: NOT REACHED
Q1 closed the file OUT (operator rule 2). Nothing below is a clearance. Facts already found are under AFTER THE STOP; the
figures are under COMPUTATION, NOT A CLEARANCE.

---
## THE BOX
**OUT at Q1:** the business the price pays for is a drone-technology start-up with no filed revenue, statements or
customers, bought for $259.6M of consideration, 97% of it goodwill on the filer's own allocation; under the literal
parts threshold the legacy contractor decides and closes OUT at Q2 (a tender business whose customers buy on the low
bid). **Integrity facts recorded, not judged** (Q5, below). COMPUTATION beside the price: value range nil to nil a share
(about one cent with later-filed cash) against $4.53; fair price nil.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Q2 (the legacy part's castle).**
- Tender and quotation work, project by project: 51.0%, 30.9% and 45.3% of awarded contracts by open tender in FY2025,
  FY2024, FY2023, the rest by quotation on request (20-F FY2025, 0001493152-26-016229, Contracts and Pricing Model).
- Field: 932 contractors registered under CW02 (180 at Grade C1), 523 under CR07; "approximately 200 market participants"
  in subsurface utility works, "less than 30" in HDD works, the company "one of the five (5) key players for HDD works in
  Singapore" (Frost & Sullivan, cited in Item 4); "competition from many large international players from China, India,
  Australia and Europe" (Item 4, Competition).
- Pricing: "keen competition and significant downward pricing pressure"; "Most of our contracts with customers do not
  have any price adjustment mechanisms" (Item 3.D).
- Concentration: top five customers 96.0%, 90.2%, 87.0% of revenue, FY2025 to FY2023; top customer 29.9%, 42.9%,
  26.9% (Item 3.D).
- **Competitors:** the 20-F names none; it gives only registry counts and an unnamed group of five HDD key players. The
  drone filings (F-3, 424B5s, proxy, pro forma, 6-Ks) name none either. No competitor's filings were read (the file
  closed at Q1); any rival chosen would have been a CONVENTION of the run, and none was chosen.
- The returns over the span, from the filer's own figures: operating margin 11.0% (FY2021), 16.1% (FY2022), 3.4%
  (FY2023), 4.6% (FY2024), (19.6)% (FY2025, after $2.4M of share pay); operating profit over revenue as filed in the F-1
  (0001493152-24-004123) and the FY2025 20-F.
- The drone part: no instance found, in the filings read, of a named customer, a unit volume, a price, a market share or
  a rival.

**Q3 (capital).** Property and equipment rose from $6.2M (FY2021) to $19.8M (FY2025) while revenue went from $11.9M to
$12.9M (2.1% a year) and operating profit from $1.3M to a loss; capex $1.5M, $1.2M, $3.0M, $7.8M, $5.1M, FY2021 to
FY2025, against depreciation of $1.1M to $1.5M (F-1; 20-F FY2025).

**Q4 (the accounts), balance sheets first** (US$000; F-1 for FY2021 and FY2022, 20-F FY2024 for FY2023, 20-F FY2025 for
FY2024 as revised and FY2025):

| year-end | total assets | equity | cash | receivables + contract assets | PP&E | bank debt | finance leases | due to related parties | retained earnings | revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 13,095 | 5,372 | 2,142 | 4,434 | 6,180 | 5,523 | 640 | 676 | 3,502 | 11,917 |
| 2022 | 12,352 | 1,812 | 1,427 | 4,617 | 5,922 | 3,862 | 649 | 4,893 | 8 | 9,621 |
| 2023 | 15,306 | 2,053 | 350 | 6,386 | 7,231 | 5,050 | 1,575 | 4,795 | 206 | 9,663 |
| 2024 | 26,022 | 7,282 | 2,931 | 6,855 | 14,625 | 6,010 | 1,811 | 5,991 | 588 | 11,108 |
| 2025 | 31,643 | 7,240 | 732 | 9,155 | 19,845 | 8,927 | 2,397 | 6,995 | (2,332) | 12,949 |

What moved: equity fell by two-thirds in FY2022 when SKK Works declared a $4.9M (S$6.8M) dividend to Ms. Liao and
Mr. Ng on 2022-12-30, which was not paid and sits in "due to related parties", "unsecured, interest-free and repayable
on demand" (F-1, Dividends and Dividend Policy); the IPO's $5.1M in FY2024 (1,750,000 shares at $4.00) restored equity
while that payable stayed; receivables and contract assets reached 71% of FY2025 revenue; bank debt rose to $8.9M;
retained earnings turned negative in FY2025. What they do not say: there were no goodwill or intangibles of note until
the drone deal, which adds $259.2M of them to a $31.6M balance sheet (pro forma). Other accounting facts: a material
weakness, "insufficient accounting personnel" (Item 3.D); a new auditor (WWC, P.C., "since 2025"); an FY2024 revision
for a "mis-computation of the gain from disposal of property and equipment" ($62k, Note 19); FY2024 and FY2023 revenue
shown as $11,108k and $9,663k in the FY2025 20-F against $11,301k and $9,759k as first filed (0001641172-25-011043), a
difference the revision note does not explain (no reconciliation found in the FY2025 20-F); the pro forma calls the deal
an acquisition under ASC 805 and, in Note 3, "accounted for as recapitalization of SKK", and dates its effect both to
2025-01-01 and to 2025-12-31; the 20-F's liquidity text says the company is "required to prepay the majority of our
inventory purchases" while inventory is $45k (Item 5, Cash Requirements). Stock pay first appears in FY2025 ($2,399k).

**Q5 (integrity facts, recorded, not judged).**
- The controlling holder, Ms. Liao (Executive Director, spouse of the CEO), held 782,372 Class B shares carrying 71.20% of
  the vote and stated she would vote them for the deal (proxy, 0001493152-26-027479, ex99-3). She, Mr. Ng (COO) and the
  other Class B holders sold all 1,085,264 Class B shares to the seller for $8,000,000, $7.37 a share (Forms 4,
  0001493152-26-047232 and 0001493152-26-047081), against the $4.9807 VWAP at which Class A shares were issued to the
  seller.
- The Waiver of 2026-10-09 defers that $8M, which the seller "has agreed to pay following the Company’s receipt of the
  Capital Raise proceeds, rather than at Closing" (6-K of 2026-10-13, 0001493152-26-046697); the Form 4 footnotes say
  "Rantizo, Inc. paid $8,000,000".
- Management Shares worth $12M at grant were issued at closing; the CEO received 1,284,960 shares (Form 4,
  0001493152-26-047072) and the new President, who signed the APA for the seller, 1,059,519 (Form 4,
  0000919574-26-006971). The proxy names both the CEO and Ms. Liao as recipients.
- The issuance record: 1,750,000 IPO shares (2024-10-07); 3,125,000 shares under the 2024 Equity Incentive Plan
  (2025-03-24); 5,625,000 shares to "Professional Service Providers" (2026-03-18, a 30% addition; 20-F, subsequent
  events); a 10-for-1 consolidation (2026-04-06), followed by a Nasdaq delisting determination of 2026-04-14 that the
  consolidated bid price cured (6-K, 0001493152-26-018044); an ATM ($201,983 sold, 424B5 0001493152-26-035691); 700,000
  plan shares (S-8 of 2026-08-04); 770,000 RDO shares paid in Tether (0001493152-26-039007); 56,375,891 shares at
  closing; a further 6,000,000 registered on 2026-10-16. The row this record would be read against at Q5 and Q6:
  "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**.
- The seller had filed no Form 3 or Schedule 13D as the holder of about 88% of the shares (53,051,855 of 60,336,487) by
  the price date (EDGAR submissions list, read 2026-10-17).
- The 2022 dividend to the controlling holders (Q4, above) was still unpaid at FY2025, interest-free.

**Q6 (the deal and the owners).**
- Value given: 51,966,591 shares ($258.83M at $4.9807), $759,047 cash, $12M of Management Shares, 2,000,000 AGP Shares
  (about $10M at the VWAP), estimated transaction costs of $7.7M (pro forma Note 5). Value got, on the filer's own
  preliminary allocation: $6.9M of identifiable assets and $252.7M of goodwill. The deal was paid in shares, a merger in
  the speakers' usage ("by issuing our stock in a merger" **[L2009-019]**); the shares outstanding before the deal are about
  6.6% of the total (3,960,596 of 60,336,487), and 1,085,264 of them went to the seller.
- The independent valuation range was $254.8M to $290.7M; the consideration "was based upon the valuation in accordance
  with the Valuation Report" (proxy).
- Board after closing: five members, three independent; the seller may nominate one more independent director later.

**Q9 (debt).** Bank borrowings $8.9M and finance leases $2.4M against $0.8M of cash at FY2025; performance bonds of 5.0%
of contract sums on main-contractor work (Item 4); the RDO proceeds were held in USDT, and the company "may convert all
or a portion thereof into U.S. dollars" (0001493152-26-039007).

## COMPUTATION, NOT A CLEARANCE
*(Q7's range convention applied in full after the stop, for the owner's two reporting figures; no entry language; the
script is `compute.py` in the research folder.)*
- **Owner cash after every real cost**, US$000: operating cash less stock pay, all capital spending net of disposal
  proceeds, and finance-lease principal (equipment is bought on finance leases): FY2021 2,473; FY2022 146; FY2023
  (2,725); FY2024 (4,661); FY2025 (8,290); **five-year average (2,611)**. Depreciation variant (operating cash less stock
  pay less D&A, the maintenance proxy **[M1998-127]**): 3,053; 557; (1,108); 1,855; (4,496); average (28). On the
  all-equity basis (interest paid added back after Singapore's 17% statutory rate): all spending (2,383); depreciation
  variant **+201**. Never a net-income proxy (operator rule 5).
- **The specifics.** (a) Cycle: no year is called aberrational by the filer; FY2025's loss includes $2.4M of share pay,
  a real cost **[L2015-003]**, kept in; the literal window FY2021 to FY2025 is the window used. (b) Decline: the series
  changes sign and the halves' comparison is meaningless, so **the range is the no-growth case alone**, said so. (c) The
  drone deal is a merger (paid in shares): valued on the combined averages with the shares added to the count; the
  acquired assets have no filed earnings, so they are **credited at nothing**; no signed unclosed deal; the pending PIPE
  and capital raise are left out of the count and of net debt (not reported done). (d) Working capital is inside
  operating cash. (e) The filing gives no maintenance split; the all-spending case is central, the depreciation variant
  beside as the top; the growth bought (PP&E tripled for 2.1% a year of revenue growth) is worth less than its cost, so
  the maintenance-only no-growth case is the top and the all-spending case the bottom. (f) No growth is carried, so the
  cap does not bind.
- **Net debt, 2025-12-31** (20-F FY2025): bank borrowings $8,927k + finance leases $2,397k less cash and restricted cash
  $813k = **$10,511k**; operating leases ($580k) left out; the $6,995k due to related parties shown beside, not added.
  The 20-F's own subsequent events add no cash (share issues for services).
- **The floor, tested first:** enterprise value at the price $283.8M (60,336,487 x $4.53 plus net debt); the best case,
  $201k a year, is 0.07% of it. **No case earns about ten percent at the price** **[M2003-149]**; the file would close
  OUT at Q7 too, whatever the width.
- **VALUE RANGE (COMPUTATION): nil to nil a share, against $4.53.** Bottom: negative owner cash, nil. Top: $201k a year,
  no growth, at the SGS 2.41% is $8.3M for the whole business, less net debt $10.5M, nil (at the US Treasury 5.43%:
  $3.7M, nil). Beside, with the later-filed cash events added (ATM $0.2M, RDO $3.4M, less $0.76M paid at closing):
  $0.7M, about $0.01 a share, before the $7.7M of estimated transaction costs, which turn it negative again.
- **FAIR PRICE (COMPUTATION, reporting figure, all-equity basis, company's own tax): $0.00 a share.** Each end valued
  at ten percent: top $2.0M less net debt $10.5M, negative; bottom negative; the average nil. **Equity-only figure
  beside: $0.00** (owner cash after interest averages $(28)k on the best case). The tax is the company's own
  (Singapore); no carryforward is priced.
- **Width:** not tested; the floor closes it first.
- A re-look alert at the top of the computed range would sit at about nil (about $0.01 with the later cash events).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 2c482f5c); written question by question; committed after Q1
      (bd0b0b2c) and at the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run
      binds nothing until folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination and was not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_run.py` in the research folder (ids exist,
      quoted fragments in their rows, no E-ids); every filing fact carries its accession.
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance; the figures are headed COMPUTATION.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal), never a net-income
      proxy; the sovereign from the issuing authority (MAS for SGD; the US Treasury beside); the price quote flagged
      as an aggregator's.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No point-in-time anchor; the rule on later rows does not apply.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stale price and share count were not.
- [x] `python tools/check_framework.py` run before the final commit (result in the commit message).
- Honest limits: the APA's schedules (the list of acquired assets and contracts) are not among the filed pages read;
  the Newbridge valuation report is not filed; the pending PIPE and capital raise were unreported at the price date, so
  the share count may be about 2M to 4M low; no competitor's filings were read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts threshold has no input for a part bought after the window.** Q2's business-of-parts paragraph, which
also defines "matters" for Q1, measures a part by its share of five-year operating profit. A part acquired the week
before with no filed operating record scores nothing, so the literal rule hands the decision to a $13M legacy
contractor while 97% of a $273M price pays for the new part. I confessed a CONVENTION of this run (size from the filer's
purchase price and allocation) and showed that the literal reading also closes OUT; the text should say how an
unmeasured part is sized. (2) **Start-up OUT against technology TOO HARD.** Q1 lists start-ups under what it "rules
OUT" and sends fast-moving technology to TOO HARD (NATURE); section I names Q1's closures only as TOO HARD. A technology
start-up fits both; I took the more specific start-up item. The text should say which governs, since the boxes differ
in what follows (an alert at the top of the range against a closed box). (3) **The merger specific for a target with
no filed record.** Q7(c) values a share-paid deal "on the combined companies' own averages"; where the target files no
statements the combined average is the buyer's alone, which I applied, crediting the assets at nothing as the
closed-after-the-window sentence directs; the two sentences could be joined. (4) **The sovereign for a USD-reporting,
SGD-earning filer that has just bought a U.S. business.** The protocol's table has no SGD row and does not say whose
currency governs once the earnings are mixed; the brief chose SGD, and I showed the US rate beside. It decided nothing
here, since the range is nil at either rate.
