# Company Run: Consolidated Water Co. Ltd. (Nasdaq: CWCO), 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 96c45d95). Dispatched blind run;
working folder `Test Runs/_research 2026-10-28 CWCO/` (notes, fetch and arithmetic scripts; raw filings in the ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-28, after the run was committed (2e2c3c1b): not held (`PORTFOLIO.md` read for this ticker only).*

**Contamination, declared:** the brief's opening lines and the repository's start-of-session context showed the subjects of the
last five commits (all about another company's run, WTRG, closed OUT at Q7) and a git status listing untracked daily digest
files and one modified file in another run's research folder (ARCB). Nothing of them concerns CWCO and nothing of them was
opened or used. A memory index line names "57 gate-clearers" and wave counts with no company names; not used. No run file,
holding review, `PORTFOLIO.md` or blind-listed file was opened, listed or searched.

**Lines of evidence, chosen from the latest 10-K (FY2025, filed 2026-03-16, accession 0001104659-26-028587):**
from Item 1, the five segments (retail, bulk, services, manufacturing, the OC-BVI affiliate) and their revenue shares, the
retail licence and its history, the bulk contracts and their expiries, the named competitors; from Item 1A, the retail licence
renegotiation (OfReg "seek to restructure the terms of the license in a manner that could significantly reduce the operating
income"), the Bahamas receivables (71% delinquent), fixed-price contract risk, termination for convenience (Hawaii), customer
concentration (WSC 22% of revenue), tourism and rainfall, hurricanes, the pegged currencies, the 30% US withholding tax on
repatriated profit; from Item 7, segment margins over the cycle, the licence's royalty and frozen rates since January 2018,
pricing through the last inflation (bulk indexed, retail not raised), the Mexico project and its settlement, acquisitions
(PERC, REC) and their goodwill, debt (almost none), stock pay, dividends. Added from 8-Ks: the new licence's terms
(8-K filed 2026-06-24, accession 0001104659-26-077347, with the licence as Exhibit 10.1), the auditor change (8-K filed
2025-04-11, accession 0001558370-25-004720). Buybacks of common stock: none in the window (cash-flow statements).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $27.12 (2026-10-28, live quote via `tools/run.py`; **aggregator, flagged** under operator rule 5).
- **Shares by class:** Class A common 16,012,865 (cover of the 10-Q for the period ended 2026-06-30, filed 2026-08-10,
  accession 0001104659-26-093370; `python Screens/cover_shares.py CWCO`). Check: the balance sheet at 2026-06-30 shows
  16,000,190 issued and outstanding; the company holds no treasury stock (issued equals outstanding in every year of the
  `tools/run.py` table); the 10-Q's dei line shows 16,000,190 common and 47,734 redeemable preference shares (the preference
  shares are employee shares convertible one for one, $0.60 par; immaterial, left out of the count and said so). No 8-K or
  prospectus after the 10-Q issues shares (8-Ks of 2026-08-10, 2026-10-15 and 2026-10-21 are an earnings release and two
  Regulation FD items; not read beyond their item numbers, which carry no Item 3.02).
- **Market cap:** 16.013M x $27.12 = **$434.3M**.
- **Sovereign for the earnings currency:** the reporting and earnings currency is the US dollar (the Cayman and Bahamian
  dollars are pegged, 10-K Item 1A); **5.30%**, US Treasury daily par yield curve, 30-year, 2026-10-27 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (2026-03-16, 0001104659-26-028587): Items 1, 1A, 7, the statements and
  Note 14 (segments); 10-K FY2024 (2025-03-17, 0001558370-25-003137) segment note for 2022 to 2024; 10-K FY2023 (2024-03-27,
  0001558370-24-004095) MD&A; 10-K FY2022 (2023-03-30, 0001558370-23-005147), FY2020 (2021-03-31, 0001558370-21-003844) and
  FY2018 (2019-03-18, 0001144204-19-014413) statements and segment MD&A; 10-Q Q2 2026 (2026-08-10, 0001104659-26-093370);
  proxy DEF 14A (2026-04-22, 0001104659-26-046528); 8-Ks above; Q2 2026 earnings release (Exhibit 99.1, 8-K 2026-08-10,
  0001104659-26-093477). **Cross-check:** net cash from operating activities FY2025 $41,713,571 on the filed cash-flow
  statement equals the XBRL figure 41.71 printed by `tools/run.py`; cash at 2025-12-31 $123,788,390 on the filed balance
  sheet equals the tool's 123,788.
- `python tools/run.py CWCO`, arithmetic lines only (its v4 material ignored, Part VII): OCF 8.0 / 36.5 / 41.7 (FY2023 to
  FY2025), SBC 1.9 / 1.4 / 1.7, capex 5.0 / 6.7 / 8.5, D&A 6.6 / 6.7 / 6.9; no securities, intangible or software lines
  inside operating cash; no other stock-pay line. The run's own owner-cash series, recast from the filed statements for
  FY2017 to FY2025 (continuing operations, after SBC, all capital spending and dividends to minority partners, before
  interest income), is in `Test Runs/_research 2026-10-28 CWCO/value.py` and under Q4 and Q7.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, and here the cash comes from water sold under a licence and contracts, not from the next buyer. The market
serves and does not instruct **[M2006-077]**: the stock has roughly tripled since 2020 (proxy pay-versus-performance table,
$100 to $325.36), which is a fact about the quotation and not about the business. Margin of safety: "if you have to actually
do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**; this governs Q7. No macro forecast enters:
tourism, rainfall and Bahamian credit enter only as properties of the business. The analyst's habits: write contrary evidence
down at once **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the government spent eight
years seeking to "significantly reduce" the retail licence's income and the new licence cuts revenue and operating income by
about $1.9M a year on 2025 volumes (8-K 2026-06-24; 10-Q Q2 2026); (2) retail rates were not raised from January 2018 to
the licence date despite inflation (10-K Item 7, Impact of Inflation), and the new formula indexes only 55% of the base rate
(licence Condition 44); (3) the Cabinet may direct OfReg to modify the licence "with or without Cayman Water’s agreement"
(8-K); (4) 71% of the Bahamas receivable was delinquent at 2025-12-31 and no allowance is taken (10-K Item 1A); (5) the
FY2024 and FY2025 cash flows were swollen by the release of working capital built in FY2023 (filed cash-flow statements);
(6) an adverse ICFR opinion (IT general controls) at 2024-12-31 (8-K 2025-04-11), reported remediated at 2025-12-31.

## THE STANDING RULE
The buyer's conduct: a purchase of these shares for cash, unlevered, sized so that no fall in the quotation forces a sale,
risks nothing the buyer has and needs **[M2012-081]**; borrowed money to own it is ruled out **[L2014-005]**. Nothing about
the business itself bears on this rule; its debt and exposures are Q9's.

---
## Q1: CAN I UNDERSTAND IT? STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**; the key variables and how predictable they are **[M1998-044]**; whether the past
statements tell the future ones **[M2008-033]**.

**Routing: a business of parts.** The filer reports four operating segments plus corporate (Note 14). Five-year operating
profit before corporate costs, FY2021 to FY2025, USD millions (FY2022 to FY2025 from the segment tables of the FY2024 and
FY2025 10-Ks, which state corporate separately; FY2021 retail is the run's estimate, because until the FY2023 10-K "we record
all non-direct G&A expenses in our retail segment": FY2021 retail gross profit $11.04M less retail direct G&A taken at the
FY2022 figure, $2.61M, about $8.4M):

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year | share |
|---|---|---|---|---|---|---|---|
| retail (Cayman Water, licence) | ~8.4 (est.) | 10.76 | 13.27 | 14.28 | 15.30 | ~62.0 | ~41% |
| bulk (CW-Bahamas, OC-Cayman) | 7.68 | 8.39 | 8.74 | 8.75 | 9.40 | 42.96 | ~29% |
| services (PERC, REC, DesalCo, Kalaeloa) | 0.41 | 2.42 | 26.90 | 6.39 | 4.03 | 40.15 | ~27% |
| manufacturing (Aerex) | -4.04 (incl. $2.9M goodwill impairment) | -0.36 | 2.19 | 2.87 | 4.41 | 5.07 | ~3% |

No part carries more than half; the largest, **retail, decides** (Q2's business of parts, CONVENTION of 2026-10-06, which
also defines "matters" for Q1). The estimate for FY2021 retail does not move the answer: retail would need under about $5M of
the five years for bulk to be larger. The bulk and services parts do not decide; services' share is one Liberty Utilities
contract in FY2023 ($64M of construction revenue).

**Applied to the deciding part.** The retail business produces seawater-reverse-osmosis water at three company plants (5.0M
gallons a day) and sells it by its own 100-mile pipe network to 8,717 connections in Seven Mile Beach and West Bay, Grand
Cayman, under an exclusive licence (10-K Items 1 and 7). The key variables are three: volume (customer accounts, stay-over
tourism, rainfall), the rate (now written into a 25-year licence from 2026-08-01 with a stated annual adjustment formula and a
separate energy pass-through), and costs (electricity passed through; labour, chemicals, maintenance, the 7.5% royalty).
Volume history: 1.09 billion gallons in 2025, "the highest in our history"; volumes fell 13% in 2020 when the island closed to
tourists and recovered by 2023 (10-K FY2020 and FY2025, Item 7). The rate for ten years is now arithmetic on CPI and PPI
(licence Condition 44). The past statements tell the future ones for this part **[M2008-033]**: it is a water utility in a
fixed territory with no technology race; reverse osmosis has been used here since 1989.

What is harder: the government's conduct as licensor across the term, and the 10-year economics of the non-deciding
services part (lumpy fixed-price construction; the $204M Hawaii design-build-operate contract under permitting delay). The
first is a question of the castle and is carried to Q2; the second does not decide. The governance and tax of the Cayman
Islands and The Bahamas are stated plainly in the filing (no income tax; exchange control on Bahamian transfers; 30%
withholding on US profits sent to the parent), which meets the test of **[M2000-141]**; an understood business abroad asks a
lower price, not a pass **[M2006-021]**.

Would the insiders write the forecast down **[M2000-105]**? For the deciding part, yes: the licence itself is the regulator's
written ten-year forecast of the price, and the filer's own pro forma restates 2024 and 2025 under it (8-K 2026-06-24).

**VERDICT: IN.** The deciding part is a territorial water utility whose earning power over ten years rests on variables that
are knowable and written down **[M2012-065]**, **[M1998-044]**; the doubt rule **[M2002-092]** was put to it and the doubt
found was about the licensor's future conduct, which is Q2's question, not about whether the economics can be read. Filing
fact: retail volume and rate history, 10-K FY2025 Item 7; licence Condition 44, Exhibit 10.1 to 0001104659-26-077347.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. The file closes on the deciding part, retail (Q1's table).

**The castle tests, on the retail part.**
- *The attacker with money* **[M2011-015]**: no one may sell piped water in the licence area; the licence grants "the
  exclusive right to produce, distribute and sell potable water within the License Area during the license term" (8-K
  2026-06-24). The only other utility on Grand Cayman is the government's Water Authority (WAC), outside the area. A
  hundred million dollars cannot buy entry; only the licensor can. The moat is a legal grant, not a cost or a brand.
- *Pricing power and the agony before a rise* **[M2005-020]**: none of its own. The company "have not applied to increase the
  water rates for Cayman Water since January 2018 (despite the inflation that has occurred since that date)" (10-K Item 7).
  The new licence sets rates that would have lowered revenue and operating income by about $2.1M in 2024 and $1.9M in 2025
  (10-Q Q2 2026; about 6% of 2025 retail revenue of $33.6M), and adjusts the base rate each July by the factor
  0.45 + 0.20 x (1 + CPI change) + 0.35 x (1 + PPI change) (licence Condition 44): 45% of the base rate is never indexed, so
  at steady inflation the real price falls each year. Energy is passed through separately, subject to an efficiency test.
  This is a price the regulator sets, and the prayer session is held in the regulator's office.
- *Unit volume*: record 1.09 billion gallons in 2025 (+8.3%), customer accounts +6.6% in 2025 and +4.3% in 2024 (10-K Item 7);
  2025 was helped by rainfall 40% below the 30-year average, and Q2 2026 volume fell 2% in slightly wetter weather (release,
  0001104659-26-093477). Volume rests on Grand Cayman's population and stay-over tourism, both growing in the filing's figures.
- *The low-cost position*: inside the territory the question is moot; the licence's energy mechanism pays for efficiency.
- *Would the customer still choose it over the low bid* **[M2017-009]**: the customer has no choice in the area; the low bid
  is offered to the regulator, which is where the threat sits.
- *Would it stand without the lord* **[M1996-037]**: yes; the plants, the pipes and the licence carry it, not a person.
- *Widening or narrowing* **[M1999-108]**: on price, narrowing (eight frozen years, a cut, partial indexation); on volume and
  term, widening (accounts growing 4% to 7% a year; a 25-year term replaces eight years of operating on an expired licence).
  The licence also obliges the company to build New Works where "commercially feasible" (Condition 19) and to have its capital
  plan approved (Condition 42).
- *What could destroy, modify or reduce it* **[M2000-014]**: the licensor. The Cabinet may direct OfReg to modify the
  licence "for reasons of security, public interest or health of the general population of the Cayman Islands, with or
  without Cayman Water’s agreement"; it may be revoked for specified breaches; it does not renew automatically, and on
  revocation or non-renewal there is a "potential compulsory divestiture" of the works (8-K 2026-06-24). A hurricane or
  earthquake (three of eight storage tanks damaged in January 2020, Item 1A) is the physical threat; Condition 45 lets
  replacement assets enter the rate base. The speakers' own utility mistake: "the regulatory climate in a few states has
  raised the specter of zero profitability" **[L2023-011]**, and "whether you earn X or go broke is not an equation that
  works" **[M2024-011]**.

**What the evidence says about the threat.** For eight years the licensor and its predecessor sought to "restructure the
terms of the license in a manner that could significantly reduce the operating income and cash flows" (10-K Item 1A). The
outcome, now signed for 25 years, is a cut of about $1.9M of operating income on 2025 volumes (about 12% of the segment's
$15.3M before corporate costs) and a formula that indexes 55% of the base rate. The castle was attacked by the one party who
could attack it, with eight years to do it, and still stands with most of its income. The formula "will not be changed except
by agreement of the Company and the Office in writing" (Condition 44(1)); the Cabinet's public-interest power is the residual
risk and it cannot be measured from the filings. Carried to Q9.

**The returns the castle protects.** Retail operating capital at 2025-12-31 (segment assets less segment cash, Note 14):
$59.41M less $15.69M = $43.7M; retail operating income before corporate costs $15.30M, about 35% before tax (the Cayman
Islands levy no income tax, Item 1). With a share of corporate G&A by revenue (26% of $14.78M; a CONVENTION of this run,
rationale: the filer stopped charging corporate costs to retail in the FY2023 10-K and gives no allocation key) about $11.5M,
some 26% on tangible capital; less the licence cut, about 22%. These are excellent returns on the capital actually needed
**[M2010-090]**, earned on assets largely built before 2018. The castle "protects excellent returns on invested capital"
**[L2007-004]**; it is not the standing castle that protects only ordinary returns.

**The parts table.**

| part | share of 5-yr operating profit | castle | decides |
|---|---|---|---|
| retail | ~41% | exclusive licence to 2051, regulator-set price | yes (largest) |
| bulk | ~29% | long contracts with two government utilities (Bahamas to 2032 and 2033; Cayman Red Gate to 2034, North Sound and North Side extended only to 2027-03-31, 10-Q Q2 2026); won by tender against Veolia, IDE and others | no |
| services | ~27% | none shown: a fragmented field "against a large number of companies, many of which have greater resources" (Item 1); contracts terminable for convenience (Item 1A) | no |
| manufacturing | ~3% | none shown: "highly fragmented industry" (Item 1) | no |

Services and manufacturing, open, are carried to Q7 as ordinary businesses at no growth (business-of-parts CONVENTION); Q7
uses the whole company's owner cash, so their ordinary economics are already inside it.

**The competitor row.** The 10-K names Veolia, IDE Technologies, TSG, Seven Seas Water, Inframark and Jacobs Solutions
(Item 1, Competition). Veolia (files in France), IDE Technologies (private), TSG (no SEC filing found) and Inframark (private)
do not file with the SEC: flagged. Seven Seas Water filed through its parent AquaVenture Holdings until its sale in 2020; Jacobs
files. No rival competes in the deciding part's territory, so the row describes the non-deciding parts.

| company | metric | figures | source |
|---|---|---|---|
| AquaVenture Holdings (Seven Seas Water, Caribbean desalination for utilities; plus Quench) | operating income, $M, consolidated | 2015 -30, 2016 -12, 2017 -8, 2018 -6, 2019 +8 on revenue of $112M (2016) to $203M (2019); net loss each year 2016 to 2019 ($-20M to $-25M) | XBRL of the 10-Ks, last 0001558370-20-002101 |
| Jacobs Solutions (services rival in the US) | operating margin, fiscal years | FY2021 4.9%, FY2022 6.2%, FY2023 6.6%, FY2024 6.0%, FY2025 7.2% | 0000052988-21-000065, 0000052988-22-000111, 0000052988-23-000084, 0000052988-24-000065, 0001628280-25-053316 |
| CWCO bulk segment | operating margin before corporate | FY2021 28.6%, FY2022 25.4%, FY2023 25.3%, FY2024 26.0%, FY2025 28.1% | CWCO 10-Ks as listed in Step 0 |
| CWCO services segment | operating margin before corporate | FY2021 3.0%, FY2022 8.4%, FY2023 27.5%, FY2024 12.5%, FY2025 8.7% | CWCO 10-Ks as listed in Step 0 |

AquaVenture's span (2015 to 2019) does not cover CWCO's window, which the run says rather than smooths; it is the nearest
span on record. **The field's returns, judged in words:** the contract desalination field earned poor returns at its one
SEC-filing specialist (losses through 2018, a thin profit in 2019 on heavy debt); engineering-and-operations services earn
single-digit margins at the largest filer. CWCO's non-deciding parts sit at or above their field. The deciding part has no
field: its return is what the licensor leaves it, and the licensor has just left it most of what it had.

**VERDICT: IN.** The deciding part's castle is a 25-year exclusive licence, attacked for eight years by the only party able to
attack it and left standing with most of its income and a written price formula; it protects returns well above ordinary on
the capital it needs **[L2007-004]**, **[M2010-090]**; it needs no superstar **[M1996-037]**. Against it, weighed and carried:
no pricing power of its own **[M2005-020]**, a real price that falls under the formula, and a public-interest modification
power that the rows' own utility mistake shows can bite **[L2023-011]**, **[M2024-011]**. These make the castle's width a
regulator's decision; they do not show it filling in, since the one test of it on the record ended with the castle standing.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, measured on "the capital
actually needed in the business" **[M2010-090]**, on tangible assets **[M2011-060]**.

- **Return on the capital needed, the deciding part.** Retail: about 26% after a revenue share of corporate costs on $43.7M
  of segment operating assets (Q2), untaxed; about 22% after the licence cut. Built mostly before 2018; retail capital
  spending is modest (retail PP&E net $31.7M at 2024-12-31 and $32.4M at 2025-12-31, Note 14).
- **Return on the capital needed, the whole company.** Operating capital at 2025-12-31 = total assets $257.6M less cash
  $123.8M, goodwill $12.9M and intangibles $2.1M, less liabilities $30.9M (no debt to speak of) = **$87.9M**; operating income
  $18.36M less tax $2.16M = $16.2M, **about 18%**. At 2019-12-31 the same capital was about $116.7M ($192.3M less cash $42.9M,
  goodwill $13.3M, intangibles $5.0M and liabilities $14.3M) for operating income of $11.72M, about 10% before a near-zero tax.
  Operating income rose by $6.6M while operating capital fell by about $29M (filed balance sheets, FY2019 and FY2025 10-Ks).
- **Reinvestment to stand still and to grow.** Capital spending FY2019 to FY2025 averaged **$4.94M** against depreciation and
  amortization of **$6.84M** (cash-flow statements). "Every year we spend amounts equal to our depreciation charge simply to
  stay in the same economic place" **[L2000-035]**; here the company spent less than its depreciation for seven years, which
  either means the old plants are well past their book lives or that maintenance is being deferred. The filer plans about
  $11.1M of capital spending "for our existing operations" in 2026 (10-K Item 7, Liquidity), above depreciation, including the
  Bahamas Cat Island plants and the West Bay expansion. The filing does not split maintenance from growth; the run does not
  guess a split (Q7 says which case that leaves central).
- **The growth arithmetic.** Revenue rose from $68.8M (FY2019) to $132.1M (FY2025), mostly through services construction
  and the PERC and REC purchases; the growth that added capital at good returns is the retail volume growth on the existing
  network and the bulk contracts. Growth in services is lumpy and fixed-price: the FY2023 peak ($26.9M operating income) was
  one contract. "There’s a huge difference in the business that grows and requires a lot of capital to do so, and the business
  that grows, and doesn’t require capital" **[M1994-081]**; of the three grades in **[M1998-081]**, the retail part is close
  to the first, a business that "gives you more and more money every year without putting up anything to get it, or very
  little"; the services part is a contractor whose margin is the year's work. *(Corrected during the run, before Q7: this
  sentence first gave the quote's id as M1998-081; the quote is M1994-081's, found by the run's own citation check.)*
- **Purchases and their return.** Net business purchases FY2021 to FY2025: REC $3.42M (FY2023) and the PERC minority
  $2.44M cash plus 368,383 shares (FY2023), against owner cash of $75.6M over the same years: well under half, so not a serial
  acquirer under Q7(c). Aerex (bought 2016, minority bought out 2020 for $8.5M) had $2.9M of goodwill written off in 2021 and
  earned $4.4M before corporate costs in FY2025; PERC (51% in 2019, the rest by 2023) earned the FY2023 services peak.

**WEIGHS FOR.** The deciding part earns high returns on little capital and has grown its volume on the network it has
**[M1998-081]**, **[M2010-090]**; the whole company earns about 18% after tax on operating capital that has shrunk while its
income rose. Against: capital spending below depreciation for seven years **[L2000-035]**, now turning up, and a services part
whose returns are a contract's, not a castle's. The "little or no debt" criterion is applied at Q9.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** (`tools/run.py` table, first-filed
XBRL, USD thousands; the FY2019, FY2022, FY2024 and FY2025 balance sheets read on the filed statements):

| year-end | assets | liabilities | equity | cash | receivables | goodwill | intangibles | LT debt | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 163,605 | 9,499 | 145,605 | 39,254 | 16,501 | 9,784 | 5,195 | 490 | 51,589 |
| 2017 | 165,481 | 9,460 | 147,932 | 47,183 | 15,048 | 8,384 | 3,765 | - | 53,105 |
| 2018 | 172,516 | 8,760 | 154,971 | 31,337 | 24,228 | 8,004 | 1,892 | 0 | 59,298 |
| 2019 | 192,292 | 14,339 | 163,759 | 42,903 | 23,230 | 13,325 | 5,040 | 61 | 66,353 |
| 2020 | 179,556 | 10,543 | 160,909 | 43,794 | 21,484 | 13,325 | 4,148 | 126 | 64,911 |
| 2021 | 177,027 | 11,362 | 157,579 | 40,358 | 27,349 | 10,425 | 3,402 | 152 | 60,603 |
| 2022 | 193,007 | 25,243 | 159,667 | 50,712 | 27,046 | 10,425 | 2,819 | 216 | 61,248 |
| 2023 | 218,438 | 26,607 | 186,827 | 42,622 | 38,227 | 12,861 | 3,353 | 191 | 85,149 |
| 2024 | 243,313 | 28,004 | 209,961 | 99,350 | 39,581 | 12,861 | 2,697 | 70 | 106,876 |
| 2025 | 257,565 | 30,886 | 221,651 | 123,788 | 32,769 | 12,861 | 2,102 | 26 | 116,749 |

What moved and why. **Equity** rose $76M in ten years, $55M of it in FY2023 and FY2024: the Liberty Utilities construction
contract (FY2023 services operating income $26.9M) and the gain on the Mexico land sold under the settlement (FY2024,
$10.4M from discontinued operations; $33.3M of cash received). **Goodwill and intangibles** are small against equity ($15.0M
against $221.7M); goodwill came with Aerex (2016), PERC (2019) and REC (2023), and $2.9M of Aerex goodwill was written off in
2021. **Cash** went from $39M to $124M ($132.6M at 2026-06-30, 10-Q), now half of total assets: the balance sheet is mostly a
deposit account beside a utility. **Receivables** against sales: $16.5M on $57.9M of revenue (28%) in FY2016 and $32.8M on
$132.1M (25%) in FY2025, but $20.7M of the FY2025 figure is one debtor, the Bahamas government's Water and Sewerage
Corporation, 71% of it delinquent, with no allowance taken because "all previous delinquent accounts receivable [...] were
eventually paid in full" (10-K Item 1A); at 2024-12-31 it was $28.4M, 81% delinquent. **Debt**: none of consequence in any
year (the largest, $0.5M in 2016). **Retained earnings** rose from $51.6M to $116.7M after dividends every year.

What the figures do not say **[M2025-032]**: whether the Bahamas receivable is worth its book value (the filer's judgment,
supported by its payment history, against a government rated B1 by Moody's); what the Hawaii contract will earn (fixed-price
on about 80% of a $147M construction price indexed only to the notice to proceed, Item 7); and what the retail plants will
cost to keep up, since capital spending has run below depreciation for seven years (Q3).

**The income account and the real costs.**
- *Depreciation*: a true cost **[R1996-023]**; here it runs $6.2M to $7.4M a year and capital spending less (Q3). Owner cash
  is shown both ways at Q7.
- *Stock pay*: $0.98M to $1.93M a year FY2021 to FY2025 (cash-flow statements), deducted in full **[L2015-003]**; plus
  $0.07M of stock issued for services in FY2025.
- *Restructurings and the recurring "one-time"*: the Mexico project's costs ran through discontinued operations for a decade
  (operating cash outflows of $1.1M to $2.2M a year, FY2019 to FY2025) and ended with the land sale in 2024. The run treats the
  Mexico venture as an abandoned investment, its costs and its recovery both outside owner cash, and says so.
- *Working capital*: contract assets swung from a $18.6M build in FY2023 (Liberty) to a $17.1M release in FY2024; receivables
  released $6.5M and inventory $4.2M in FY2025. Changes in working capital were about -$31.5M (FY2023), +$11.1M (FY2024) and
  +$12.6M (FY2025) (the "Change in" lines of the filed statement, summed by the run). FY2024 and FY2025 owner cash is swollen
  by the FY2023 build coming back. Counted, as Q7(d) requires, over the whole window, where it nets.
- *Equity-method income*: OC-BVI is counted as the dividends received ($0.30M, $0.23M, $0.55M in FY2023 to FY2025), as the
  operating cash flow already does (Q4's equity-method CONVENTION).
- *Tax*: the Cayman and Bahamian operations pay none; the US subsidiaries do ($2.16M in FY2025). A 30% US withholding tax
  would fall on profits sent to the Cayman parent (Item 7, Liquidity); none has been paid that the filings show, so the cash
  that sits in the US subsidiaries ($46.4M services and $6.6M manufacturing at 2025-12-31, Note 14) is worth less to the parent
  than its face if it is ever moved. Not priced; carried.
- *EBITDA in the filer's mouth*: none found in the 10-K or the Q2 2026 release; the release reports GAAP figures and gives no
  numeric guidance. The incentive plan's net income target is "adjusted for certain components of net income that are not
  directly affected by management’s performance" (proxy), an internal figure, not one featured to owners.
- *Controls*: an adverse opinion on internal control at 2024-12-31 for IT general controls (8-K 2025-04-11, reported in the
  auditor's resignation letter after its attest business passed to CBIZ); management and CBIZ report control effective at
  2025-12-31 (10-K Item 9A).

What the accounts say of management's character: plain statements, segment detail beyond the requirement (cost of revenue by
line and segment, Note 14), and a risk section that states the licence threat and the delinquent receivable in numbers. "If
you find a management that doesn’t care about the accounting but does explain to you in clear terms what’s going on, I think
you should regard that as a plus" **[M1994-018]**.

**VERDICT on the accounts: IN; WEIGHS FOR.** Nothing confuses **[M1995-063]** and no tell of the kind that lives in the
accounts was found (no building prepaid or deferred accounts, no reserve movements tied to a deal, inventory falling with
sales) **[M1995-064]**. Weighing against: the Bahamas receivable carried at full value on a payment history rather than an
allowance, and capital spending below depreciation. The recast owner cash, FY2017 to FY2025 (continuing operations, after
stock pay, all capital spending and dividends to minority partners, before interest income; USD millions): 7.56, -9.73,
12.11, 15.54, 5.42, 12.64, 1.44, 27.75, 28.31. It feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The question: "do they love the business or do they love the money?" **[M2000-098]**, judged by two yardsticks, "how well
they run the business" against "the hand they were dealt", and "how well that they treat their owners" **[M1994-008]**. For a
marketable stock the speakers read rather than meet: "We read annual reports. We read about competitors." **[M2007-081]**.
Read here: the proxy (DEF 14A, 2026-04-22, 0001104659-26-046528), five 10-Ks (Step 0), the 8-Ks on the licence and the
auditor, the Q2 2026 release.

**The people.** Frederick W. McTaggart, 63, director since 1998, President since October 2000, Chief Executive since
January 2004, Chief Financial Officer 2001 to 2004; before that, from 1987 to 2000, Operations Engineer, Deputy Director and
then Managing Director of the Water Authority-Cayman, the government utility (proxy, Proposal 1). The Chief Financial Officer
(Sasnett) has served since 2006, the Chief Operating Officer (Jerrybandan) joined in 1998 as Operations Engineer on Grand
Cayman, the Chief Accounting Officer since 2007. A managing team of twenty-plus years, raised inside the island's water
system. One director (Ebanks) is the Cayman Islands government's nominee and sits on the compensation committee (proxy).

**Yardstick one, the record against the hand dealt** **[M1994-008]**:
- *The deciding part.* Retail volume at a record in 2025 on the same network; customer accounts up 4% to 7% a year (10-K
  Item 7). Eight years operating on an expired licence against a licensor seeking to "significantly reduce" its income
  ended in a 25-year exclusive licence that cuts about 12% of the segment's operating income (Q2). For a hand that held one
  card, the licensor's, the outcome is a good one; the speakers' "We’ve seldom been wrong about the people" **[M2000-100]**
  is a reminder that the economics, here set by the licensor, matter more than the play.
- *Capital, the record of deals and ventures.* Mexico (Rosarito): pursued from 2010, $21.1M of land bought from 2012, the
  contract won in 2016 and cancelled by the State in June 2020; arbitration filed 2022; settled May 2024 by the State's
  purchase of the land (MXN 596.1M, about $33.3M) and of documents (MXN 20M) (10-K FY2024, discontinued operations note).
  Fourteen years of capital and $1.1M to $2.2M a year of costs, returned at about nominal cost: not a loss, not a return.
  Aerex (2016): $2.9M of goodwill written off in 2021, the minority bought for $8.5M in 2020, now earning $4.4M before
  corporate costs (Q3). PERC (51% in 2019, the rest by January 2023): the services peak of 2023. Operating capital fell
  while operating income rose (Q3). The record is that of a careful operator with one long, unrewarded venture.
- *What ability shows in.* A long record, not a promise: "we don’t like banjo hitters who suddenly proclaim that they can
  become power hitters" **[M1996-038]**; the retail and bulk parts have been run by the same people for two decades with
  margins that held through the 2020 closure (Q1 and Q2 tables). Against: capital spending below depreciation for seven
  years (Q3), which could be good engineering or deferred upkeep, and the Hawaii plant, signed June 2023, still awaiting
  permits, with construction expected "to start later this year" in the Q2 2026 release after the delay disclosed in the
  FY2025 10-K and the 10-Q.

**Yardstick two, the owners** **[M1994-008]**, and the tells **[M2004-067]**, **[M2002-028]**, **[M2007-090]**:
- *Reports.* The 10-K tells an owner what an owner of the whole would want to know **[M1998-036]**: the licence threat in
  the government's own words, the delinquent Bahamas receivable as a percentage, the withholding tax on US profits, the
  permitting risk on Hawaii with its liquidated-damages exposure, segment cost detail beyond the requirement (Q4). No
  earnings guidance; no featured adjusted figure in the release; no EBITDA in management's mouth (Q4). The bad news was
  told: the adverse internal-control opinion on 2024 reached owners through an 8-K filed the week of the auditor's letter
  (8-K 2025-04-11). The release's last paragraph is boilerplate ("enhanced shareholder value", "strategic acquisitions and
  partnerships that can further accelerate growth"), the kind of jargon the speakers dislike, "a standardized bunch of
  popular jargon" **[M1998-038]**, but it is one paragraph of an otherwise factual release.
- *How they treat themselves* (proxy) **[M1994-009]**: Chief Executive total pay $1,222,966 in 2025 ($1,462,458 in 2024),
  of which salary $562,275; pay ratio 15 to 1; no options, no defined-benefit pension, no deferred compensation; car
  allowance $20,400. The Chief Executive owns 285,102 shares (1.78%), about $7.7M at $27.12, some six years of total pay;
  directors and officers together 929,390 shares (5.81%). Hedging and pledging by directors and officers are barred; a
  clawback applies to incentive awards.
- *Stock price.* No sign of a management fixed on its quotation **[M2004-067]**: no buyback programme, no guidance, no
  splits; the proxy's return chart is the SEC's required pay-versus-performance disclosure.
- *The habits carried from Q4.* No making or beating of a public number: there is no public number. The internal bonus
  target uses an adjusted net income ("adjusted for certain components of net income that are not directly affected by
  management’s performance", proxy), which came in at $20.79M against reported net income of $18.34M; it is a pay figure,
  not one featured to owners, and is weighed at Q6 Part B.

**Love of the business, and after the cheque.** No sale of control is in question; the test is read in tenure and stake.
A chief executive who came from running the island's government utility and has run this one for 22 years, with six years
of pay in its stock and pay modest for a $434M company, reads as one who loves the business more than the money
**[M2000-098]**. Nothing found suggests otherwise; nothing found proves it either, which the rows accept: "People are not
that easy to read." **[L2023-003]**.

**VERDICT on integrity: IN.** No tell of dishonesty was found in five years of reports, the proxy, the 8-Ks or the
release: nothing too good to be true **[M2002-028]**, no emphasis on the stock price **[M2004-067]**, the bad news stated
in numbers **[M1998-039]**. The doubt rule, "If you’ve got doubts, forget it." **[M2013-088]**, was put and found nothing to
act on. **Ability WEIGHS FOR, modestly**: a long record in the deciding part and a reasonable outcome with the licensor
**[M1996-038]**, **[M2012-089]**, set against a fourteen-year venture in Mexico that returned its cost and no more, a goodwill
write-off at Aerex, and the Hawaii delay. The business, not the manager, carries this company: "we still look to the
underlying business, though." **[M1996-037]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"the question becomes, “What do we do with the money, as it comes in?”" **[M2001-111]**.

**Part A, the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**, over FY2021 to FY2025. Retained earnings rose from $64.9M to
  $116.7M, **$51.8M** kept after $30.0M of dividends (filed balance sheets; dividends paid on the cash-flow statements:
  5.15, 5.15, 5.47, 6.28, 7.94). Market value at 2020-12-31: 15,169,687 shares (cover, 10-K FY2020) x $12.05 = $182.8M; at
  2025-12-31: 15,964,209 (cover, 10-K FY2025) x $35.29 = $563.4M (year-end closes from the aggregator's quote history,
  flagged). A rise of **$380.6M for $51.8M kept**; at today's $27.12 ($434.3M), still about $251M. The market leg passes by
  a wide margin. But read what the kept dollars did: cash rose from $43.8M to $123.8M over the same five years, more than
  the whole amount kept, and earned about 2% to 2.5% (interest income $2.67M in FY2025). The market's rise came from the
  business re-rated and from the FY2023 contract and the Mexico recovery, not from a retained dollar put to work. The
  forward question, "Can you keep using all of the capital you generate, effectively, for a very long time?"
  **[M2010-097]**: on the filings, no. The 2026 plan is $11.1M of capital spending (10-K Item 7) against $132.6M of cash
  (10-Q Q2 2026). Cash as a residual is the speakers' own default **[M1995-057]**, "cash is the default option"
  **[M2003-072]**; the dividend has risen from $0.34 a year (2018 to 2022) to $0.56 at the current quarterly rate, the
  direction **[M2004-089]** points. Against: the Chief Executive's words, "Supported by a strong balance sheet, we believe we
  are well positioned to move decisively [...] while also pursuing strategic acquisitions" (release, Q2 2026), read beside
  "we'll try to resist the temptation to do something marginal simply because we are long on cash" **[L1993-007]**.
- *Buybacks* **[L1999-023]**, **[L2011-003]**: none of common stock in the window (cash-flow statements; the only
  "buyback" lines are employee redeemable preference shares, $1,830 to $29,089 a year). There is no programme and no price
  paid to test. *Written back from Q7:* the bottom of the Q7 range is **$25.32 a share** (all-equity basis, central case);
  no common shares were bought at any price, so the test has nothing to read.
- *Issuance and deals* **[M1995-001]**, **[L2014-015]**. Shares on the cover rose from 14,715,899 (March 2015) to
  15,964,209 (March 2026), 8.5% in eleven years, from stock pay and one deal: not a company "hell-bent on issuing shares"
  **[L2014-015]**. The deal: the last 39% of PERC in January 2023 for $2.44M cash and 368,383 shares worth about $5.36M,
  about $14.55 a share (10-K FY2023, PERC note). Paid mostly in shares, so a merger in the speakers' usage **[L2009-019]**,
  at a price per share below the Q7 bottom; but it was not "an all-stock deal", so Q6's STOP does not reach it. Value given
  against value got: 39% of a unit that earned $26.9M before corporate costs in FY2023 and $4.0M in FY2025, for $7.8M.
  Value got exceeded value given; the shares were cheap currency, which **[L2009-019]** warns of, but the deal was small.

**Part B, the pay, the board, the owners.**
- *Pay tied to what the person controls* **[M2003-019]**: the annual bonus weighs adjusted net income, revenue (35% for
  the Chief Executive, excluding energy pass-through) and gross margin; the long-term grant weighs three-year operating cash
  flow, earnings per share and revenue (proxy). Revenue rewards size, not return; there is no charge for capital employed,
  which **[L1994-019]** and **[M2009-081]** ask of a business that uses capital. For 2025 the revenue leg missed (88.66% of
  target) and paid nothing, which shows the plan bites. *The bar*, the "chimpanzee" test **[M2004-097]**: the 2023 to 2025
  long-term targets were cumulative earnings per share of $0.87 and revenue of $206.4M, against FY2022 continuing earnings
  per share of about $0.53 for one year and revenue of $94.1M; results were $4.88 (562.9% of target) and $390.5M (189.2%).
  A three-year target below the prior year's run rate is a low bar; the plan's cap (158% of target shares) limited what it
  paid.
- *Design and the ratchet*: an outside consultant (FW Cook, 2023 and 2024) and a peer group of utilities set salaries "at
  comparable companies" (proxy), the practice **[L2005-015]** and **[M2004-016]** reject. Severance of 24 months for the
  Chief Executive; the Chief Financial Officer may elect to leave on a change in control with 36 months of salary.
- *The board*: an independent chair (Pergande, director since 1978, retiring in 2026 with a 43-year director; both join an
  advisory board), eight of nine nominees independent, a government-nominated director. Director pay about $70,000, over 40%
  in shares; director holdings range from none to 256,562 shares, some in retirement accounts, which suggests shares bought
  "with their savings" **[L2019-008]**, though the proxy does not say which were bought.
- *Owners as partners*: no guidance **[M2022-054]**, plain reports (Q5), dividends since 1985, a dividend reinvestment
  plan at market prices, no splits.

**WEIGHS: Part A UNDECIDED; Part B AGAINST, lightly.** Part A: the retention test passes on the market leg
**[R1995-009]**, but the kept dollars sit in cash and the business cannot use them at its own rate of return **[M2010-097]**;
issuance is small and the one share-paid deal returned more than it gave **[M1995-001]**; the stated wish to use the balance
sheet for acquisitions is the risk to watch **[L1993-007]**. Part B: modest pay, no options, real ownership, but
revenue-heavy targets set below the run rate and benchmarked by consultant **[M2004-097]**, **[L2005-015]**; "you get what
you reward for" **[M2016-083]**.

## Q7: WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
with credit only "for whatever net cash is left every year" **[M1998-080]**, at the long government rate **[L2000-021]**,
**[M1996-025]**, as a range **[L2000-024]**. Arithmetic: `Test Runs/_research 2026-10-28 CWCO/value3.py` (central and beside
cases) on the series of `value.py` and `value2.py`; every input from the filed statements named in Step 0 and Q4.

**The basis: is this a regulated utility under Q7, The regulated utility (2026-10-18)?** By its own text (Q7, The
regulated utility) the section applies "where the deciding part of a business [...] earns a return a regulator allows on its
invested capital". Its row is the electric utility: "when you get an allowed return in the electric utility you’re almost
certain of earning it" **[M2010-037]**,
and the exception it rests on is "debt dedicated [...] to the fixed-asset commitments at our regulated utilities"
**[L2017-012]**. The deciding part, retail, is regulated, but not on a return on invested capital. Its licence sets the base
rates in the licence itself and moves them each July by a fixed index formula, the Rate Cap Adjustment Mechanism (licence
Condition 44); the stated principle is "the opportunity to recover appropriate costs and earn a fair and reasonable profit
margin on its sales" (licence Schedule Six, paragraph 1); there is no allowed rate of return, no allowed debt share, and the
words "Rate Base" appear only for assets replaced after a disaster (Condition 45(3)). It is a price cap, not an allowed
return; and the company has raised no long-term debt to fund its plants (long-term debt $0.15M at 2021-12-31, $0.03M at
2025-12-31; Q4 table), so the section's debt credit would be nil in any case. **Decision: the section does not apply; the
all-equity basis is central** (Q7, On what the floor is earned), and the equity-only figure is shown beside. Had the section
applied, the equity-only basis with a nil credit would be central, and it is lower (below).

**Whose tax.** Owner cash is after the company's own tax: none in the Cayman Islands and The Bahamas, US income tax on the
US subsidiaries inside operating cash ($2.16M in FY2025). The 30% US withholding tax on profits sent to the Cayman parent
(10-K Item 7, Liquidity) has not been paid in the window and is not in owner cash; on the US subsidiaries' cash at
2025-12-31 ($46.4M services and $6.6M manufacturing, Note 14) it would be up to about $15.9M, $0.99 a share, if moved. Not
deducted; shown here as a figure beside, said so. No carryforward shelters the tax (section E does not arise).

**Net debt (all-equity basis).** Cash and cash equivalents $132.63M at 2026-06-30 (10-Q Q2 2026, latest filed balance sheet;
no subsequent event in it changes cash materially), less borrowings and finance leases $0.02M, less the book value of
non-controlling interests $5.36M (the minority partners' claim on the consolidated cash; a CONVENTION of this run, rationale:
owner cash deducts only the dividends paid to them, so their share of retained cash sits in the cash added back); operating
leases left out, said so. **Net cash $127.26M**; market value $434.27M; **enterprise value at the price $307.01M**.

**The cash input, year by year** (owner cash: operating cash from continuing operations, less stock pay, all capital
spending, dividends to minority partners and interest income; USD millions; Q4): FY2017 7.56, FY2018 -9.73, FY2019 12.11,
FY2020 15.54, FY2021 5.42, FY2022 12.64, FY2023 1.44, FY2024 27.75, FY2025 28.31. Highest share of sales 21.4% (FY2020 and
FY2025).

**The specifics, applied.**
- *(a) The base.* Both ends of the literal window FY2021 to FY2025 are aberrational on the filer's own description: FY2021
  sits in the tourism closure (retail volume fell 13% in 2020 and recovered by 2023, 10-K Item 7), and FY2025 is swollen by
  the release of working capital built in FY2023 for one contract (Liberty Utilities; contract assets built $18.6M in FY2023
  and released $17.1M in FY2024, Q4) **[L2005-003]**. The base is the last full cycle the series shows, **FY2019 to FY2025**:
  the year before the closure to the year after the contract's build and release, so that the closure trough and the
  contract's draw and return are all inside it. Average **$14.75M**. The literal window ($15.11M) is shown beside.
- *(b) Decline.* None; the series does not change sign inside the cycle.
- *(c) Acquisitions.* Cash paid for businesses, net of businesses sold, over the cycle: FY2019 PERC 51% $3.15M less the
  sale of CW-Belize $6.97M; FY2020 the Aerex minority $8.5M and 10% of PERC $0.9M; FY2023 REC $3.42M and the last 39% of
  PERC $2.44M in cash (the 368,383 shares paid are in the share count) (filed cash-flow statements, 10-Ks FY2020 and
  FY2025). Net $11.44M, **$1.63M a year**, against owner cash before purchases of $103.2M: under half, so not a serial
  acquirer; the default pair, purchases deducted and the total growth credited. The PERC deal was paid mostly in shares and
  is a merger by the speakers' usage; PERC was already consolidated, so the combined averages are the reported ones. In the
  growth case the purchases grow with the growth ($1.88M in year one, $6.51M in year ten) and stop after year ten. The
  no-growth case is valued on owner cash before purchases, reading "a business that buys no growth spends nothing to buy
  it" (specific (c)) as reaching the no-growth case too; the purchases-deducted no-growth case is shown beside.
- *(d) Working capital.* Counted inside owner cash in every year. The FY2023 draw tied to one contract is inside the cycle
  with its release; the three years' changes (-$31.5M, +$11.1M, +$12.6M) net to -$7.8M. Beside: the cycle with FY2023 to
  FY2025 working-capital changes set at zero.
- *(e) Growth spending.* The filing gives no split of maintenance from growth spending and no figure the run could use for
  the guess **[M2000-144]**, **[L1999-024]**: the 2026 plan of $11.1M is "for our existing operations" without a split, and
  capital spending has run below depreciation for seven years (Q3). The all-spending case is therefore central, with the
  depreciation variant beside. No growth spending is separated, so none is charged above maintenance; the purchases of (c)
  are the only spending that runs and stops with the growth.
- *The growth shown.* Measured on aggregate owner cash before purchases, between the halves of the cycle (FY2019 to FY2021
  average $11.03M; FY2023 to FY2025 average $19.17M): **14.8% a year**. On owner cash after purchases it is 17.1%; sales
  grew 11.5% a year end to end FY2019 to FY2025 and 21.0% between the same halves.
- *(f) The cap.* Inside the ten years the shown rate is the cap; after year ten no growth (zero nominal) **[M1997-095]**. The
  absurdity test: owner cash at 14.8% for ten years reaches $58.6M; sales carried at the business's own growth (11.5% end to
  end, from the cycle's average sales of $106.9M) reach $317M, at the highest share earned (21.4%) $67.9M. The shown rate does
  not require owner cash above the highest share of sales, so it is not cut **[M1999-067]**. On the literal window the
  shown rate (45.9% between its halves, from the FY2021 trough) does fail the test and is cut to the sales growth, never
  above the discount rate: 5.30%. Beside the central case, the growth case carried at the discount rate (5.30%) is shown, the
  reading of Q7's first CONVENTION paragraph ("no rate that runs past the discount rate").
- *The rate.* 5.30%, the US Treasury 30-year par yield, 2026-10-27 (Step 0).

**The floor, tested first** (CONVENTION, about ten percent after the company's tax **[M2003-149]**). At $27.12 the price
buys $307.01M of business. The no-growth case returns **4.80%** on it; the growth case (14.8% for ten years, purchases
deducted, then none) returns **12.04%**. One case clears the floor, so the floor does not close the file; the width decides
next.

**COMPUTATION of the range and the reporting figures.**

| case | owner cash base | growth | value range a share | width | return at $27.12: no-growth / growth | fair price |
|---|---|---|---|---|---|---|
| **central**: cycle FY2019-25, all spending, purchases deducted | $14.75M | 14.8% | **$25.32 to $62.85** | 2.48 : 1 | 4.80% / 12.04% | **$24.85** |
| beside: growth at the discount rate | $14.75M | 5.30% | $25.32 to $33.51 | 1.32 : 1 | 4.80% / 6.85% | $18.77 |
| beside: literal window FY2021-25 (rate cut by (f)) | $15.11M | 5.30% | $25.76 to $34.46 | 1.34 : 1 | 4.92% / 7.10% | $19.17 |
| beside: purchases deducted in the no-growth case too | $14.75M | 14.8% | $23.40 to $62.85 | 2.69 : 1 | 4.27% / 12.04% | $24.34 |
| beside: depreciation in place of capital spending | $12.84M | 14.8% | $23.08 to $55.54 | 2.41 : 1 | 4.18% / 10.80% | $22.58 |
| beside: less the new licence's cut, $1.9M a year (8-K 2026-06-24) | $12.85M | 14.8% | $23.08 to $55.55 | 2.41 : 1 | 4.18% / 10.80% | $22.59 |
| beside: FY2023-25 working-capital changes at zero | $15.86M | 14.8% | $26.64 to $67.12 | 2.52 : 1 | 5.17% / 12.74% | $26.17 |
| beside: nine years FY2017-25 | $11.23M | 14.8% | $21.18 to $49.72 | 2.35 : 1 | 3.66% / 9.82% | $20.81 |
| **equity-only** (beside; central had the utility section applied): owner cash after interest income $15.85M against market value, no cash added | $15.85M | 14.8% | $18.67 to $59.13 | | 3.65% / 9.83% | **$18.21** |

The fair price is each end case valued at ten percent and the two averaged, per share, all-equity less net debt (Part VII):
central ends $17.16 (no growth) and $32.54 (growth), average **$24.85**. If the US withholding were charged on the US
subsidiaries' cash, every per-share figure above falls by about $0.99.

**How sure** **[M1999-104]**, **[M2003-147]**: the no-growth end rests on a licence now fixed for 25 years and two bulk
contracts to 2032 to 2034, and is the firmer; the growth end rests on a rate measured from a base that holds the closure
trough and a one-contract peak, on a services part whose margins are the year's contracts (Q2 table: 3.0% to 27.5%), and on
the Hawaii plant not yet started. The growth the deciding part itself has shown is volume of 4% to 8% a year at a price the
licence now cuts and indexes at 55%; the 14.8% is not the castle's growth. The text's mechanical test does not cut it, and
the run does not cut it either; the doubt goes to the margin of safety asked **[M1997-080]**, not to the rate.

**Closes.** The floor is cleared by one case; the width is 2.48 to 1, under about three to one, so the range is usable and
the file is not TOO HARD. The price, **$27.12, sits inside the range**, 7% above its bottom of $25.32. That is not a price
"so obvious that you don’t have to carry it out to tenths of a percent" **[M2009-005]**; "if you have to actually do it on
— with pencil and paper, it’s too close to think about" **[M1996-084]**. On every beside case the price is also inside the range,
and above the fair price of every case ($18.21 to $26.17).

**VERDICT: OUT.** Valued, the range is narrow enough to read, and the price sits inside it, not "startlingly low in relation
to value" **[L2000-025]**; the case is close, and close cases are left **[M2009-005]**, **[M1996-084]**. The rows' three
boxes: this is "out" **[M2006-013]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
Not reached: Q7 closed the file. Facts found are under AFTER THE STOP.

## Q9: COULD IT RUIN US? WEIGHING.
Not reached. Facts under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH? WEIGHING.
Not reached. The draft would have the buyer do nothing: inaction is the default when the price is not a screamer.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not reached. Fact under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7 (the price sits inside the value range: $25.32 to $62.85 a share against $27.12 on 2026-10-28; not a screamer).**
Q1 IN, Q2 IN, Q3 weighs for, Q4 IN and weighs for, Q5 integrity IN and ability weighs for, Q6 Part A undecided and Part B
against lightly. Reporting figures (Part VII, not verdicts): value range $25.32 to $62.85; fair price $24.85 all-equity,
$18.21 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down **[M1997-127]**, not weighed; the box is unchanged.
- *Q8, the bond.* The 30-year Treasury yields 5.30% (2026-10-27). Owner cash before interest on the enterprise value at
  $27.12 is 4.80% with no growth; on the equity, owner cash after interest income is 3.65% of the market value.
- *Q9, debt and exposures.* Borrowings of $0.02M against cash of $132.6M (10-Q Q2 2026). Concentrations: the Bahamas Water
  and Sewerage Corporation, 22% of revenue and $20.7M of receivables at 2025-12-31, 71% delinquent, no allowance (10-K Item
  1A); the Hawaii contract, about $147M of fixed-price construction indexed to inflation only to the notice to proceed, with
  liquidated damages if permit delays are not excused (10-K FY2025 and 10-Q Q2 2026); hurricanes and earthquakes on small
  islands (three of eight storage tanks damaged in January 2020, Item 1A); the Cabinet's power to modify the licence in the
  public interest and the compulsory divestiture on revocation (8-K 2026-06-24); the North Sound and North Side bulk
  contracts extended only to 2027-03-31 (10-Q Q2 2026); the 30% withholding tax on US profits sent up (Item 7).
- *Q12.* Desalinated and piped drinking water, wastewater and water-treatment equipment; no business named by the rows.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 96c45d95); written question by question; committed after each,
      with this session's commits for Q5 and Q6 (f18938ac) and Q7 to the end (this commit) after the resume.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] Blind rule: no other run file, holding review, `PORTFOLIO.md`, resume-state, queue or reading-list file was opened,
      listed or searched; contamination as declared at the top (commit subjects and a git status listing, nothing about
      this company, not used). In this session the resume brief named the run file, its byte count and the last commit
      subject, all this run's own.
- [x] Every v5 id resolves (`check_cites.py`: no E-ids, every M/L/R id in `principle_ledger_v5.csv`); quoted fragments
      beside ids checked against the rows; the fragments the script flags are filing quotes with their source named in the
      same sentence. **One correction made during the run**: Q3 first gave the quote "There’s a huge difference in the
      business that grows [...]" the id M1998-081; it is M1994-081's; corrected in place before Q7 with a dated note, since
      the run was not yet complete (operator rule 6 reserves the addendum for violations found after a run closes).
- [x] The order was kept; Q7 closed the file; Q8 to Q12 not run; the figures after Q4 are computations, and the Q7 range is
      reported only because Q1 to Q6 did not close.
- [x] Owner cash from the filed cash-flow statements after stock pay, all capital spending, minority dividends and business
      purchases, never a net-income proxy; the sovereign from the US Treasury curve; the price and the year-end closes from
      the aggregator, flagged.
- [x] Contrary evidence written down as found (foundations list, Q2, Q3, Q4, Q5, Q6 and Q7's "how sure").
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit (see the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The growth cap is stated two ways.** Q7's first CONVENTION paragraph caps the carried growth at "no rate
that runs past the discount rate", while specific (f), adopted the next day, says "No rate above the discount rate is carried
after year ten [...]; inside the ten years the shown rate is the cap", with only the share-of-sales absurdity test cutting it.
Here the difference is the whole growth end ($62.85 against $33.51 at the top, $24.85 against $18.77 for the fair price). The
run read the later, more specific text as governing, made the shown rate central and put the discount-rate case beside; the
box is OUT either way. (2) **The share-of-sales test needs a sales projection the text does not define.** The run carried
sales at their own growth end to end over the cycle from the cycle's average sales; carried between the halves (21.0%), the
test is looser still. A test that compares one projected series with another projected at a faster rate rarely bites. (3)
**Specific (c) says purchases stop after year ten in the growth case and is silent on the no-growth case**; the run valued
the no-growth case before purchases and showed the deducted case beside ($25.32 against $23.40 at the bottom). (4) **The
regulated-utility section assumes an allowed return on invested capital.** A price-cap licence with an index formula and a
"fair and reasonable profit margin on its sales" is regulated but not on that basis; the run read the section as not
applying, which the absence of any long-term debt made immaterial here. Also minor: the cycle rule (a) assumes a series with
visible peaks and troughs; this one has a contract-driven peak and a closure trough that do not line up, and the run chose
FY2019 to FY2025 by the filer's descriptions, with the literal window beside.
