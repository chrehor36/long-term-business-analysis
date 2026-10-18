# Company Run — Pony AI Inc. (NASDAQ: PONY; HKEX: 2026) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (85df9f76): `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatched blind run.** The brief granted per-question pathspec commits of this file and `Test Runs/_research 2026-10-16 PONY/`
only. The template was copied and committed (717d2fdc) before any fetch. Working notes, scripts and the arithmetic are in the
research folder (`compute.py`, `compute_output.txt`, `_notes.md`); raw filings are in its ignored `cache/`.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` filtered to today's date, made to check that
this run's file name was free, showed the names of about thirty other run files and research folders dated 2026-10-16 (rail,
leasing and oilfield-service names); none was opened, and none concerns this company. (2) The session's git snapshot showed
commit subjects for another company's run (RAIL) and untracked research-folder paths of two others (AYI, ARCB). (3) The memory
index loaded with the session carries one-line notes on the queue state (wave counts, a count of gate-clearers); none names
this company. No line about PONY, Pony AI or any former name was seen in any of these. No file on the blind list was opened,
listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $4.93 per ADS (Nasdaq close 2026-10-16; `tools/run.py` quote, cross-read against the Yahoo chart series for
  2026-10-07 to 2026-10-16; **aggregator, live quote only**, operator rule 5). One ADS represents one Class A ordinary share
  (Q2 2026 release, 6-K 0001104659-26-098113). Hong Kong line beside it: HK$45.38 a Class A share on 2026-10-09 (RSU grant
  announcement, 6-K 0001104659-26-115030).
- **Shares by class:** the FY2025 20-F cover count is 433,541,553 (`python Screens/cover_shares.py PONY`; 20-F filed
  2026-04-22, accession `0001104659-26-046406`), which the filed balance sheet splits as 352,452,783 Class A and 81,088,770
  Class B issued and outstanding at 2025-12-31. Later filings move it: the 2026 interim report (6-K `0001104659-26-109772`,
  2026-09-23) gives 353,324,845 Class A and 81,088,770 Class B in issue and "the Company did not have any treasury shares"
  at 2026-06-30; the HKEX monthly return for September (6-K `0001104659-26-114347`, filed 2026-10-07) closes September at
  **354,095,390 Class A and 81,088,770 Class B, no treasury shares, total 435,184,160**, the count used here. The charter
  note: Class B carries ten votes a share and Class A one (20-F Item 10 and Item 3.D); the classes rank alike for dividends
  (notes, 2(y)), so they are added for value. RSUs granted 2026-10-09 (1,638,591; 6-K `0001104659-26-115030`) are not yet
  shares and are not counted.
- **Market cap:** $4.93 x 435.184M = **$2,145.5M**.
- **Sovereign for the earnings currency:** the reporting currency is the US dollar, but "The functional currencies of its
  subsidiaries, the VIEs, and the VIEs’ subsidiaries in Chinese mainland are the Renminbi" (20-F note 2), and the Chinese
  mainland produced US$87.6M of the US$90.0M of 2025 revenue (20-F note 2(z)). The earnings currency is therefore the RMB.
  **30-year China government bond yield 2.06%, 2026-10-16**, from the Ministry of Finance of the PRC's published curve
  ("财政部-中国国债收益率曲线", served at yield.chinabond.com.cn, compiled by China Central Depository and Clearing; the
  series it returns is labelled "中债国债收益率曲线"; the 10-year point 1.648%). The protocol's table does not cover the RMB;
  the issuing authority's own page is used, and its compiler is named. **Beside it, not used for the box:** the US Treasury
  30-year par yield 5.43% (2026-10-15, `tools/run.py`, Treasury daily par curve), since the accounts and most of the cash
  pile (raised in US and Hong Kong dollars) are in dollars.
- **Filings read** (operator rule 4): the FY2025 20-F (filed 2026-04-22, accession `0001104659-26-046406`): Item 3.D risk
  factors (the operating, competition, capital and regulatory factors), Item 4.A and 4.B (history, the business, the three
  revenue lines, Competition), Item 5.A results and 5.B liquidity, Item 6 (directors), Item 10 (share classes), and the
  audited statements (balance sheet F-5, operations, cash flows, notes 2(l), 2(y), 2(z)). The Q2 2026 results release and the
  interim results announcement (6-K `0001104659-26-098113`, 2026-08-18, exhibits 99.1 and 99.2). The 2026 interim report
  (6-K `0001104659-26-109772`, 2026-09-23, exhibit 99.1, a PDF; read for the share count and treasury shares). The 6-Ks of
  2026-08-14 (`0001104659-26-096218`, Uber Europe), 2026-08-25 (`0001104659-26-100791`, annual-cap revision with Sinotrans),
  2026-10-02 (`0001104659-26-112948`, share issue on RSU vesting), 2026-10-07 (`0001104659-26-114347`, HKEX monthly return)
  and 2026-10-09 (`0001104659-26-115030`, RSU grant). FY2022 figures are from the FY2024 20-F (`0001410578-25-000895`) as
  tagged; that filing's statements were not opened, so FY2022 is transcription only. There is no proxy (a foreign private
  issuer; pay is in 20-F Item 6.B, not read, since the file closed at Q1). **Not read:** the F-1 and 424B4 of 2024 and the Hong
  Kong prospectus of 2025; the file closed at Q1 before any question they bear on.
- **One figure cross-checked against the filed statement:** FY2025 revenue US$90,001K and net cash used in operating
  activities US$(164,955)K as tagged equal the filed statement of operations and statement of cash flows in
  `0001104659-26-046406`. A discrepancy found and resolved: the risk factor's FY2025 "net loss of US$ 76.8 million" is the
  consolidated net loss after a US$128.0M gain on trading securities; the net loss attributable to Pony AI Inc. is
  US$(133,969)K, the difference being US$57.2M of net income allocated to non-controlling interests (filed statement of
  operations).
- **`python tools/run.py PONY`, arithmetic lines only:** three-year mean (OCF less SBC less capex) -$204.4M, D&A basis
  -$195.0M; four-year window -$199.6M; yield -9.56% on the capex basis; growth the price assumes REFUSED because the base is
  negative. The tool read the tagged SBC for 2023 as US$3.8M (allocated expense); the cash-flow statement adds back
  US$3.254M, which this run uses. The tool's v4 material is not read (Part VII). The run's own table is below.

**Owner cash after every real cost** (US$M; OCF as filed, less the stock pay added back in the cash-flow statement, less all
capital spending, less finance-lease principal and the 2025 dividend to a minority holder; `compute.py`):

| Year | OCF | stock pay | capex | lease + minority | **owner cash, equity-only** | cash interest in OCF | **owner cash before interest** |
|---|---|---|---|---|---|---|---|
| 2022 | -154.8 | 13.2 | 12.0 | 0.9 | **-180.8** | 9.0 | **-189.8** |
| 2023 | -115.4 | 3.3 | 5.1 | 1.1 | **-124.8** | 16.4 | **-141.2** |
| 2024 | -110.8 | 127.0 | 11.4 | 1.0 | **-250.2** | 14.7 | **-264.9** |
| 2025 | -165.0 | 30.8 | 43.9 | 7.4 | **-247.0** | 22.7 | **-269.7** |
| mean | | | | | **-200.7** | | **-216.4** |
| H1 2026 | -118.2 | 13.6 | 44.6 | n/a | **-176.5** (H1 2025: -110.3) | | |

Cash interest is approximated as investment income less the realized gains the cash-flow statement removes as non-cash
(2025: 43.0 less 20.3). The 2024 stock pay includes US$120.7M "incurred in connection with the vesting of share-based
compensation awards upon our initial public offering" (20-F Item 5, 98.8 in R&D and 21.9 in SG&A); without it the four-year
means are -170.5 and -186.2. On the depreciation basis the equity-only mean is -194.0. The trailing twelve months to
2026-06-30 are about -313. Every year, on every basis, is negative. "Stock-based compensation" is charged as a real cost
because it "is the most egregious example" of costs owners are told to ignore **[L2015-003]**.

**The balance sheets, read before the income account (template, Q4 line; read here because the file closes before Q4).**
Only four year-ends are filed with the SEC (2022 to 2025) plus the interim of 2026-06-30, not the eight to ten the line asks
for; the company was private before November 2024.

| US$M | 2022 | 2023 | 2024 | 2025 | 2026-06-30 |
|---|---|---|---|---|---|
| Cash and equivalents | 316.3 | 426.0 | 536.0 | 293.5 | 327.1 |
| Short-term investments | 261.6 | 163.6 | 209.0 | 872.2 | 787.0 |
| Long-term investments | 80.7 | 51.7 | 130.8 | 454.9 | 375.7 |
| Receivables | 25.9 | 31.6 | 28.6 | 23.6 | 43.3 |
| Property, equipment, software | n/r | n/r | 17.2 | 60.5 | 98.5 |
| Total assets | 771.5 | 747.1 | 1,050.8 | 1,812.8 | 1,738.6 |
| Total liabilities | 53.6 | 51.9 | 82.1 | 103.8 | 93.0 |
| Preferred (mezzanine) | 1,257.5 | 1,361.3 | 0 | 0 | 0 |
| Pony AI shareholders' equity | -551.5 | -677.3 | 951.1 | 1,652.3 | 1,575.5 |
| Accumulated deficit | -614.7 | -739.5 | -1,287.9 | -1,422.0 | n/r |
| Non-controlling interests | n/r | n/r | 17.6 | 56.7 | 70.1 |

(n/r: not read here.) What moved and why: there is no borrowing at any year-end (a US$3.9M short-term loan in 2022 only); the
equity is negative before 2024 only because the preferred shares sat outside it, and it turned positive on their conversion
at the Nasdaq IPO of November 2024 (US$408.4M net) and grew on the Hong Kong listing of November 2025 (US$829.4M net, filed
cash-flow statement). The accumulated deficit grew by US$807M in three years. The cash and securities are the whole of the
asset side: "Cash and cash equivalents, short-term investments, restricted cash and long-term debt instruments for wealth
management were US$1,390.5 million" at 2026-06-30 against US$1,435.5M at 2026-03-31 (Q2 release). Receivables are high
against sales (US$43.3M at mid-2026 against US$70.5M of half-year revenue). Fixed assets rose from US$17.2M to US$98.5M in
eighteen months as the company began to own robotaxis. A US$25.0M prepayment for long-term investments, carried at
2025-12-31, was written off in Q2 2026 as "unrecoverable" (Q2 release). What the figures cannot say: what a driverless
vehicle earns over its life at scale, which is the one number the business turns on.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, so the test is whether one would be content to own
this "if the market closed for five years" **[M1997-109]**, which here means owning a business that has spent cash every
year it has filed and holds about US$3.20 a share of cash and securities to keep spending. The analyst's habits bear next:
the filing's own story is a projection (fleet of "more than 3,500 vehicles by year end", "on track"), and the rows say "we’ve
never looked at a projection in connection with either a security we’ve bought or a business we’ve bought" **[M1995-050]**.
No macro forecast enters. **Contrary evidence, written down as found** **[M1997-127]**: (1) the business is not a bare
start-up: founded in 2016, US$90.0M of 2025 revenue from 213 corporate customers, fully driverless commercial permits in the
four tier-one cities, a fleet of 1,975 robotaxis at 2026-06-30, and robotaxi revenue up 691.2% year on year in Q2 2026
(20-F Item 4.B and 3.D; Q2 release). (2) The 20-F reports that the robotaxi business "reached city-wide unit economics
breakeven in Shenzhen in February 2026, following the same milestone achieved in Guangzhou in November 2025". (3) Gross margin
rose to 17.5% in Q2 2026 from 16.1%, and operating expenses grew 11.4% against revenue growth of 68.8%. (4) Uber contracted
for more than 2,000 robotaxis in Europe (6-K 2026-08-14). (5) The speakers once bought a company "on the developing edge of
new technology", because "BYD had won its spurs in life by the time we found it" **[M2010-095]**; the framework carries that row
OPEN against the avoidance of unforeseeable businesses (section VI, Q1). Each is weighed at Q1 below.

## THE STANDING RULE
A part-interest bought for cash, unlevered and sized within the buyer's means, does not by itself put the buyer at risk of
ruin; the rule binds how it would be financed and held, "never going to risk what we have and need for what we don’t have and
don’t need" **[M2012-081]**, and "Never risk permanent loss of capital." **[L2023-005]**. Nothing in the target's balance sheet
(no debt, no collateral calls found) engages the rule. Not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test, applied to the filings.** Understanding is "thinking that we have a reasonable probability of being able to asses
where the business will be in 10 years" **[M2000-037]**, a fix on "what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**. The product here is easy to understand (a car that drives itself, sold as a ride, a
freight haul or a licensed system); the question is the economics, and of those the rows say "We just don’t know the economics
of it 10 years from now." **[M2000-104]**.

**The key variables, and how predictable they are** **[M1998-044]**. The 20-F names them itself (Item 3.D): (1) the per-vehicle
unit economics, which turn on "costs of hardware, other fixed and variable costs associated with autonomous vehicle production
and operation, useful life of autonomous vehicles, vehicle utilization and product and service pricing", and "the appropriate
pricing is still being assessed by the market"; (2) the competitive structure, where "many established and new market
participants have entered or have announced plans to enter" with "significantly greater financial, manufacturing, marketing,
and other resources", and the company "do[es] not know how close these competitors are to commercializing"; (3) the rules,
"relatively new and evolving" in every jurisdiction, with a US connected-vehicle rule of January 2025 already in force;
(4) the technology itself, which the company has changed in kind within its own life (from modular rules to end-to-end models
and a "world model", PonyWorld 2.0 launched April 2026). None of the four is foreseeable ten years out from the filings.

**Do the past statements tell me the future ones?** The rows ask "do I understand enough about this business so that the
financial statements will tell me the information that’s useful to me in making a judgment about what the future financial
statements are going to look like" **[M2008-033]**. The filer answers no in its own words: "our historical revenues, cost mix,
margin profile and financial results in general are not indicative of future trends as we are still in a nascent stage of
commercializing our technologies", and "we cannot predict whether we will achieve profitability in the near term or at all"
(20-F Item 3.D). One third of 2025 revenue (32.9%) is freight paid by a related party, Sinotrans, through a subsidiary it owns
49% of; robotaxi services, the line the thesis rests on, were US$12.1M of a US$36.2M quarter in Q2 2026.

**Would the insiders write it down?** The test is whether they would "put down on paper their predictions about where 10
companies you would choose in the tech field would be in 10 years, in terms of their economics. They would say, “That’s too
hard.”" **[M2000-105]**. The company's own annual report is the insider's document, and it declines: it cannot say whether it
will ever be profitable, and it says the market's demand and adoption are "difficult to predict". The one public rival with a
ten-year operating start, Waymo, sits inside Alphabet's Other Bets, which lost US$7.5 billion in 2025 (Alphabet 10-K,
`0001652044-26-000018`); WeRide, the nearest filed peer, lost RMB1,846.8M at the operating line in 2025 on revenue of
RMB684.6M (20-F `0001104659-26-047323`). No operator in the field has filed a profitable full year, so there is no record from
which anyone could read the ten-year economics. **Can I name the winner?** "there’s industries we know that may have a wonderful
future, but we don’t have the faintest idea who the winners will be" **[M2012-067]**; "Just because Charlie and I can clearly
see dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on capital will be as
a host of competitors battle for supremacy." **[L2009-005]**.

**Is it important and knowable?** The unit economics at scale and the field's competitive end-state decide everything and are
not knowable now: "If something’s important but unknowable, forget it." **[M2006-076]**. **Abroad:** the operating companies are
PRC subsidiaries of a Cayman holding company, with ten-vote Class B shares; the rows ask for an understood governance and tax
system **[M2000-141]** and, for China, "We wanted to get paid more for going into China" **[M2006-021]**; that would bear on price,
which this file does not reach.

**The contrary evidence, weighed.** The unit-economics breakeven in two cities is the company's own measure, not a filed
statement, and the consolidated cash spent rose (H1 2026 owner cash -176.5 against -110.3 a year earlier) while it was being
reached; it shows progress, not a ten-year fix. The BYD row **[M2010-095]** is the speakers' one stated exception, and its
reason is a record already made, "BYD had won its spurs in life by the time we found it"; a company that has never filed a
profitable year has not yet made that record. The Uber contract and the fleet growth are volume, and volume in a field whose
returns are unknown is exactly what L2009-005 says does not settle the margins.

**Routing.** This is the case the framework fixes: "a business that must deal with fast-moving technology is not going to lend
itself to reliable evaluations of its long-term economics" **[L1993-023]**; "whenever we look at a business and we see lots of
change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**; where the technology could hurt the business,
"it won’t make it through the filter" **[M1998-008]**; and "If something is not very predictable, forget it." **[M1998-044]**. Doubt
alone would settle the perimeter, "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**, and here there is no doubt to resolve. The box is "too hard" **[M2006-013]**, not OUT on the business: "It
doesn’t mean it isn’t a good buy." **[M2000-038]**.

**The cause: NATURE, not WORK.** The deciding question (what a driverless fleet earns over a full life against well-funded
rivals and moving rules) is not one a filing not yet read could answer; the company's own insiders decline to write it down
(test 5, **[M2000-105]**), and no operator anywhere has the record. "Our problem -- which we can't solve by studying up -- is that
we have no insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**;
"We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**.
More reading would not cure it: "if we can’t make a decision in five minutes, we can’t make it in five months" **[M2008-086]**.

- **VERDICT: TOO HARD (NATURE).** Q1 closes the file. The filing fact: "we cannot predict whether we will achieve profitability
  in the near term or at all" (20-F `0001104659-26-046406`, Item 3.D), with owner cash negative in every filed year (mean
  -US$200.7M equity-only, 2022 to 2025).

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (Q1 closed the file). Competitor facts gathered are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the brief directs for a file that closes before Q4.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (No Q7 range bottom applies to a buyback test: no buyback was found in the filings read.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

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
**TOO HARD (NATURE), decided at Q1**: the ten-year economics of a driverless-fleet business cannot be foreseen, and the
company's own annual report declines to say whether it will ever be profitable. COMPUTATION, NOT A CLEARANCE, beside the price:
value range **-$20.94 a share** (the no-growth case alone, all-equity basis, at the 2.06% China 30-year rate; equity-only
-$22.39) against **$4.93**. Integrity facts recorded, not judged. No research pass: the cause is NATURE, and no case of the
computed range earns the floor at any positive price (Part VII). No re-look band can be set at the top of the range, which is
below zero.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).

**Bearing on Q2 (the castle and the field).** The 20-F names no rival: its Competition section speaks only of
"technology-focused companies building end-to-end technical capabilities for autonomous driving applications, and autonomous
players building internal autonomous development programs", and its risk factors of traditional taxi, ride-hailing and freight
carriers and automotive "market leaders" (Item 4.B, Item 3.D). **The rivals below are a CONVENTION of this run** (rationale: the
brief asks for a field comparison from rivals' own filings and the 20-F supplies no names): WeRide Inc., the nearest SEC filer
in the same business in China (20-F FY2025 `0001104659-26-047323`, IFRS, RMB; FY2022 to FY2024 from its XBRL in
`0001193125-25-062519`), and Alphabet's Other Bets, the segment that holds Waymo (10-K FY2025 `0001652044-26-000018`; Waymo is
not reported alone). Baidu's Apollo Go is not separately reported in Baidu's filings and was not read; flagged, not filed alone.

| | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Pony revenue, US$M | 68.4 | 71.9 | 75.0 | 90.0 |
| Pony gross margin | 46.9% | 23.5% | 15.2% | 15.7% |
| Pony loss from operations, US$M | -170.7 | -143.2 | -285.5 | -260.9 |
| WeRide revenue, RMB M | 527.5 | 401.8 | 361.1 | 684.6 |
| WeRide gross margin | 44.1% | 45.7% | 30.7% | 30.2% |
| WeRide operating loss, RMB M | -779.2 | -1,566.2 | -2,185.2 | -1,846.8 |
| Alphabet Other Bets revenue, US$M | n/r | 1,527 | 1,648 | 1,537 |
| Alphabet Other Bets operating loss, US$M | n/r | -4,095 | -4,444 | -7,515 |

Every filer in the field lost money at the operating line in every year read; no full-cycle return exists to compare. Pony's
customer concentration: top three customers 65.8%, 43.9% and 59.3% of revenue in 2023 to 2025; Sinotrans (a related party
holding 49% of the subsidiary Cyantron) 31.3%, 40.9% and 32.9% (20-F Item 3.D). The US Department of Commerce connected-vehicle
rule of 2025-01-14 is named as a risk (Item 3.D).

**Bearing on Q3 (capital).** Capital spending US$5.1M (2023), 11.4M (2024), 43.9M (2025), 44.6M in H1 2026, "primarily
attributable to investments supporting the continued mass production and deployment of the Gen-7 Robotaxi fleet, as well as
expenditures for data centers and servers" (Q2 release). Under the "joint deployment model", "Vehicle funding and ownership can
sit with different partners depending on the market" (6-K 2026-08-14). The 20-F: "The development and commercialization of our
autonomous driving technology and solutions are capital-intensive."

**Bearing on Q4 (the accounts).** The releases feature non-GAAP figures that exclude share-based compensation, changes in fair
value of trading securities and, from Q2 2026, "a one-off impairment loss on prepayment for long-term investments", described as
"a new adjustment introduced in the second quarter of 2026"; they also define "Free Cash Flows" as "the total of operating cash
outflows plus capital expenditures" (Q2 release and interim announcement, `0001104659-26-098113`). The FY2025 consolidated net
loss (US$76.8M) includes a US$128.0M gain on trading securities, of which US$57.2M went to non-controlling interests; Q2 2026
again had US$33.4M of such gains and US$14.5M of net income allocated to minority holders. A US$25.0M prepayment carried at
2025-12-31 was written off in Q2 2026. The "unit economics breakeven" claims are the company's own measure, not a filed figure.

**Bearing on Q5 (the people).** Founders Dr. Jun (James) Peng, chairman and CEO, and Dr. Tiancheng Lou, CTO, both formerly of
Baidu's autonomous-driving work and of Alphabet (20-F Item 6.A). Class B shares carry ten votes each (Item 10); 81,088,770 Class
B against 354,095,390 Class A at 2026-09-30. Related-party trade with Sinotrans: on 2026-08-25 the board raised the annual caps
on the Cyantron-Sinotrans transportation agreement because "the existing annual caps under the Transportation Services Framework
Agreement will not be sufficient", and entered two new connected agreements for vehicle export logistics (6-K
`0001104659-26-100791`). The October 2021 Fremont accident under a driverless permit led to a recall notice and the suspension of
the California driverless testing permit; NHTSA closed its review on 2025-01-16 (Item 3.D). The Q2 release says management is
"confident in our ability to exceed our full-year Robotaxi services revenues target" and states a year-end fleet target. These
bear on the habits Q4 carries to Q5; they are recorded, not judged.

**Bearing on Q6 (the money and the owners).** Equity raised: US$104.0M of Series D preferred (2023), US$408.4M net at the Nasdaq
IPO (2024), US$829.4M net at the Hong Kong listing (2025) (filed cash-flow statement). Shares 433,541,553 at 2025-12-31 to
435,184,160 at 2026-09-30 from RSU settlements and option exercises. A 2026 Share Scheme with a limit of 43,354,155 Class A shares
(10% of issued shares at adoption; interim report); 1,638,591 RSUs granted 2026-10-09 with no performance targets. The 20-F: "We
will need to raise additional capital to continue to fund our research and development and commercialization activities". No
buyback found. No dividend to ordinary holders; US$6.4M paid to a minority holder of a subsidiary in 2025.

**Bearing on Q9 (debt and exposures).** No borrowings at any filed year-end after 2022; operating lease liabilities US$19.0M at
2026-06-30. Cash, short-term investments, restricted cash and long-term debt instruments US$1,390.5M at 2026-06-30. Arithmetic
only, not a forecast: at the trailing-twelve-month owner cash of about -US$313M, that balance covers about four and a half years.

## COMPUTATION, NOT A CLEARANCE: THE OWNER'S TWO REPORTING FIGURES
*(Q1 closed the file; nothing here is a verdict or entry language, operator rule 3. Built by Q7's range convention in full, as
far as it applies to a negative stream; arithmetic in `Test Runs/_research 2026-10-16 PONY/compute.py` and its output file.)*

- **Base.** Owner cash after every real cost, averaged over the filed years. **CONVENTION of this run:** the five-year average
  uses the four years filed with the SEC (2022 to 2025); rationale: no earlier year is filed, and the company was private before
  2024. All-equity mean (before interest income) **-US$216.4M**; equity-only mean (after it) **-US$200.7M**. The company pays
  almost no tax (a loss-maker), so the company's own tax is nil and no shelter is priced.
- **(a) Cycle.** 2024 carries US$120.7M of stock pay recognized at the IPO for awards vesting on it, aberrational by the filer's own
  description (Item 5); shown beside: means -US$186.2M (all-equity) and -US$170.5M (equity-only). There is no business cycle in
  the window; the literal window is the base.
- **(b) Decline.** The series is negative in every year, so a compound rate between its end years (or its halves, -165.5 to
  -267.3 all-equity) reads a widening loss as growth; the rate is meaningless and **the range is the no-growth case alone**, as
  (b) directs. Beside it, as information only: the losses carried for ten years at the company's own sales growth (9.6% a year,
  2022 to 2025, the cap of (f)) give -$53.49 a share at the 2.06% rate.
- **(c) Acquisitions.** None; purchases of long-term investments (US$414.3M in 2025) are wealth-management debt instruments and
  minority stakes, counted with cash and securities, not as businesses bought. **(d) Working capital** is inside OCF.
  **(e) Maintenance.** The filing allows no maintenance guess (the capital spending is the new fleet and data centres); the
  depreciation-basis mean is shown beside, -US$194.0M equity-only. **(f) The cap** is not engaged: no positive growth is carried.
- **Net debt.** Borrowings nil, finance leases nil at 2025-12-31; cash and securities US$1,390.5M at 2026-06-30 (the latest filed
  balance, Q2 release `0001104659-26-098113`); net cash **US$1,390.5M, US$3.20 a share**. Operating leases (US$19.0M) left out;
  other long-term equity stakes (about US$104M) not counted; minority interests (US$70.1M of book equity) not deducted. Shares
  435.184M; market value US$2,145.5M; enterprise value US$755.0M.
- **The floor is tested first.** No case in the range earns the floor of about ten percent at any positive price: the stream is
  negative in every case, and "there’s just a point at which we drop out of the game" **[M2003-149]**. Had Q7 been reached it
  would close OUT on the floor before the width.

**(a) VALUE RANGE: -$20.94 a share** (all-equity, the no-growth case alone: -US$216.4M a year capitalized at the 2.06% China
30-year rate, -US$10,505M, plus net cash), against **$4.93**. Equity-only beside it: -$22.39. At the US Treasury 30-year 5.43%,
shown beside and not used: -$5.96 all-equity, -$8.49 equity-only.

**(b) FAIR PRICE: -$1.78 a share** on the all-equity basis (the no-growth case valued at ten percent, -US$2,164M, plus net cash;
the range has one end, so there is nothing to average), after the company's own tax (nil); **equity-only -$4.61**. The fair price
is below zero, so no price clears it. The figures say only that the cash stream as filed spends value; they carry no estimate of
what the business might become, which is the question Q1 found unanswerable.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (717d2fdc); written question by question; committed after Q1 (21135c8d) and at
      the close.
- [x] Dispatched: the brief allowed the per-question commits; the lock `Screens/_daily/_overnight.lock` was present (held by the
      dispatching session; not opened or touched). The fold into the register is the dispatcher's; until then this run binds
      nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is declared
      under Contamination at the top and was not used.
- [x] Every v5 id resolves (`check_run.py` in the research folder: every M/L/R id found in `principle_ledger_v5.csv`, every quoted
      fragment beside an id found in its row, no E-ids); every filing fact carries its accession. FY2022 figures are XBRL
      transcription from `0001410578-25-000895`, not read against that filing's statements (declared in Step 0).
- [x] The order was kept; Q1 closed the run; everything after it is NOT REACHED or headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending less lease principal), never a net-income
      proxy; the sovereign from the issuing authority's curve, dated (RMB, the earnings currency; USD beside); the price is an
      aggregator quote, flagged.
- [x] Contrary evidence was written down as found (Foundations) and weighed at Q1; facts for later questions are under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; one of its inputs (2023 stock pay) was replaced by the filed
      cash-flow figure and said so.
- [x] `python tools/check_framework.py` PASS before each commit.
- Not done, said plainly: the F-1, 424B4 and Hong Kong prospectus were not read; Baidu's filings were not read; the eight to ten
  balance sheets Q4 asks for do not exist on file (four year-ends and one interim were read).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q1's list of what it rules OUT names start-ups ("Start-ups are not our game." **[L2007-015]**) while its fixed routing sends
fast-moving technology to TOO HARD; a ten-year-old, never-profitable technology company fits both, and the text does not say
which governs. The routing sentence was followed (TOO HARD (NATURE)), because the reason this file cannot be judged is the
industry's unforeseeable economics, not the company's age; an analyst reading the start-up item would close OUT, and the
register would then show two boxes for the same facts. (2) Q7's specific (b) covers a declining series and a series that changes
sign, but not a series negative in every year; reading its compound rate as meaningless gave a range of one point, and Part
VII's fair price (each end case valued at ten percent, the two averaged) had only one end to average. The deterioration case is
shown beside for information. (3) The construction has no lower bound: capitalizing a perpetual loss at a 2.06% rate yields a
value of -US$10.5 billion for a company holding US$1.39 billion of cash, which no owner would bear, since the losses can be
stopped; the framework gives no instruction for a negative range, and Part VII's re-look alert "at the top of its computed range"
cannot be set below zero. (4) The protocol's sovereign table has no RMB line; the Ministry of Finance's curve is compiled and
served by China Central Depository and Clearing, and whether that counts as the issuing authority is not stated; the 2.06% RMB
rate against the 5.43% USD rate moves the computed value almost fourfold, though not the box. (5) The all-equity basis is written
for net debt; for a net-cash company whose interest income sits inside operating cash, the text does not say outright that the
interest is stripped and the cash added back. That reading was applied, with the equity-only figure beside it.
