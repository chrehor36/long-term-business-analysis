# Company Run — Community Health Systems, Inc. (NYSE: CYH) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure:
the lines of evidence were derived by the analyst from Items 1, 1A and 7 of the 10-K (listed in Step 0), not hand-written by
the dispatcher.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule; the dispatching session
fills it at the fold. *Filled at the fold, 2026-10-13, after the run was committed: not held (`PORTFOLIO.md` carries no line for CYH or Community Health Systems).*

**Contamination, declared.** A directory listing of `Test Runs/` made to confirm the dated file name showed the names of
other run files and research folders dated 2026-10-13 (among them a run on another hospital-and-behavioural-health operator,
ACHC). None was opened or searched, and nothing from them is used. The repository's recent commit subjects (shown in the
session's opening git status) name other companies' runs; not used. No file about CYH under any name was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $3.00 (quote of 2026-10-13 as printed by `python tools/run.py CYH`; an aggregator quote, live quote only,
  flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, **141,009,357** shares as of 2026-07-16 (Form
  10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession `0001193125-26-314196`; `python Screens/cover_shares.py CYH`
  prints the same). Checked against the balance sheet of the same 10-Q: 141,010,284 shares "issued and outstanding" at
  2026-06-30, so no treasury shares sit between issued and outstanding. No 8-K and no prospectus was filed after the 10-Q
  (the EDGAR submissions list read on 2026-10-13 shows the 8-K of 2026-07-22 and the 10-Q of 2026-07-23 as the latest filings).
- **Market cap:** 141.009M × $3.00 = **$423M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield on the US Treasury daily par yield curve,
  dated 2026-10-09 (the latest quoted; `python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for 2025, filed 2026-02-19, accession `0001193125-26-059509` (Items 1, 1A, 3, 5, 7, 7A; the income statement lines,
    cash-flow lines, Note 6 debt and the contingencies as quoted below).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession `0001193125-26-314196` (statements, Note 3
    divestitures, Note 6 debt, MD&A).
  - Proxy statement (DEF 14A) filed 2026-04-02, accession `0001193125-26-140269` (peer group, summary compensation, pay ratio).
  - 8-K of 2026-07-22, accession `0001193125-26-312454` (cover document only; the earnings release exhibit was not read).
  - Earlier 10-Ks for the cycle's income-statement and cash lines: FY2018 `0001193125-19-047042`, FY2021
    `0001564590-22-005570`, FY2023 `0000950170-24-018021`.
  - Competitors (HCA, Tenet, UHS): their own annual XBRL facts from SEC companyfacts (10-K values; transcription only, the
    filed statements themselves not opened; flagged).
- **One figure cross-checked against the filed statement:** net cash from operating activities for 2025, **$543M**, as
  printed by `tools/run.py` from XBRL, equals the 10-K's own table ("Net cash flows provided by operating activities | $ |
  543", Item 1 selected operating data, `0001193125-26-059509`). Capital spending of $335M for 2025 likewise matches the MD&A
  ("Capital expenditures for the year ended December 31, 2025 totaled $335 million").
- `python tools/run.py CYH`, **arithmetic lines only** (output kept at `Test Runs/_research 2026-10-13 CYH/run_py_output.txt`):
  OCF 210 / 480 / 543 for 2023 / 2024 / 2025; SBC 22 / 17 / 11; capex 467 / 360 / 335; D&A 505 / 486 / 426; distributions to
  minority partners 141 / 155 / 164 and finance-lease principal 3 / 2 / 2 printed as alternates outside capex. Its three-year
  "owner earnings" means (+7 on capex, −78 on D&A, −149 with the minority distributions) and its five-year means (−148 / −237)
  are noted as transcription; the owner cash this run uses is recast below (Q4 material, carried to the COMPUTATION).

### The lines of evidence, and where each came from (the brief's departure)
Derived from the 10-K for 2025 (`0001193125-26-059509`) before the questions were answered:
1. **Payers and pricing.** Item 1, "Sources of Revenue": Medicare 17.4%, Medicare Managed Care 18.0%, Medicaid 16.0%, managed
   care and other 47.8%, self-pay 0.8% of 2025 net operating revenues; Item 1A, the reimbursement risk factor; Item 7,
   "Overview of Legislative and Other Governmental Developments" and "Reimbursement, Legislative and Regulatory Changes".
2. **The 2025 Reconciliation Law, the end of enhanced ACA subsidies, Medicaid financing (provider taxes, state directed
   payments) and site-neutral and outpatient shifts.** Item 1, "Healthcare Public Policy", "Payment"; Item 1A; Item 7.
3. **Competition.** Item 1, "Competition" (non-urban sole providers, tax-exempt rivals, out-migration to urban hospitals,
   payer networks); Item 1A, "If we are unable to effectively compete".
4. **Divestitures and the shrinking base.** Item 7, "Acquisition, Divestiture and Closure Activity"; Item 1A, "If we are
   unable to complete divestitures"; the 10-Q's Note 3 and MD&A.
5. **Margins over the cycle.** Item 7, "Results of Operations" (three years), extended to 2016 from the earlier 10-Ks.
6. **Debt, maturities, rates and leases.** Item 1A, "Risks Related to Our Indebtedness"; Item 7, "Liquidity", "2025
   Financing Activity"; the 10-Q's Note 6.
7. **Buybacks, issuance and stock pay.** Item 5 (no open-market programme); the cover counts by year; the cash-flow SBC line.
8. **Litigation and investigations.** Item 3 (DOJ civil investigative demand, DOJ criminal investigation at Northwest, the QHC
   litigation trust suit); Item 1A, "Risks Related to Legal Proceedings".
9. **Labour and professional liability.** Item 1A, human capital; Item 7, critical accounting estimates (the $149M change in
   the professional liability estimate in 2024).

### The balance sheets, ten year-ends (read in Step 0 because the file closes before Q4) **[M2025-032]**
From `tools/run.py`'s ten-year table (first-filed XBRL, USD millions) with the 2026-06-30 balance sheet of the 10-Q added:

| year-end | assets | equity (CYH holders) | cash | patient receivables | goodwill | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 21,944 | 1,615 | 238 | 3,176 | 6,521 | 15,244 | −299 |
| 2017 | 17,450 | −767 | 563 | 2,384 | 4,723 | 13,913 | −2,761 |
| 2018 | 15,859 | −1,535 | 196 | 2,352 | 4,559 | 13,392 | −3,543 |
| 2019 | 15,609 | −2,218 | 216 | 2,258 | 4,328 | 13,385 | −4,218 |
| 2020 | 16,006 | −1,625 | 1,676 | 1,927 | 4,219 | 12,093 | −3,707 |
| 2021 | 15,217 | −1,372 | 507 | 2,062 | 4,219 | 12,109 | −3,477 |
| 2022 | 14,669 | −1,367 | 118 | 2,040 | 4,166 | 11,614 | −3,431 |
| 2023 | 14,455 | −1,392 | 38 | 2,231 | 3,958 | 11,466 | −3,564 |
| 2024 | 14,054 | −1,914 | 37 | 2,286 | 3,789 | 11,432 | −4,080 |
| 2025 | 13,204 | −1,394 | 260 | 2,077 | 3,316 | 10,380 | −3,571 |
| 2026-06-30 | 12,177 | −1,390 | 149 | 2,143 | 3,228 | 9,552 (total debt 9,578) | −3,559 |

What the figures say. The company has shrunk by sale: assets fell from $21.9B to $12.2B and revenue from $18.4B (2016) to
$12.5B (2025). Debt fell by about $5.7B, but the accumulated deficit deepened by about $3.3B over the same years, so the debt
was not paid from earnings: it was paid from the proceeds of hospitals sold (over $1.0B in 2025, about $1.2B in the first half
of 2026, per the 10-K and 10-Q MD&A) while the business it served got smaller. Stockholders' equity turned negative in 2017
(after $1.9B and $2.1B of impairments in 2016 and 2017, FY2018 10-K income statement) and has stayed negative for nine
year-ends. Goodwill, written down twice, is still $3.2B against a negative equity, so the tangible net worth is deeply
negative. Patient receivables run at about 17% of revenue in 2016 and 2025 alike: no build in receivables against sales
across the decade, which is the one line that reads clean. Cash is held thin (as low as $37M at 2024 year-end), the
business living on its $1.0B asset-based facility. What they cannot say: the earning power of the hospitals still owned,
since every year's statements include hospitals that were later sold.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own it "if the market closed for five years"
**[M1997-109]**. For CYH that question turns on the business's cash and its lenders, not on the quotation, and it is asked of
the questions below rather than answered here. The analyst's habits bear hardest: look for "what’s wrong in things"
**[M2025-013]** and ask "What do I not know that I need to know?" **[M1999-129]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) same-store net operating revenues rose 4.6% in 2025 and 5.5% in 2024, and same-store income from operations
rose 7.2% in 2025 (10-K MD&A and Item 1 table, `0001193125-26-059509`), so the hospitals kept are growing; (2) the speakers'
own rows on health care describe an industry that resists change because of "the political power that the industry will
have" **[M2025-056]** and "so many people have a vested interest" **[M2021-053]**, which argues for stable economics, against
the reading reached at Q1; (3) not-for-profit buyers paid $623M for 80% of one hospital and $450M for another in 2026 (10-K
MD&A), so the hospitals have value to others.

## THE STANDING RULE
Owning a share of CYH for cash, sized so that a total loss could not call on the buyer, puts the buyer at no risk of ruin;
bought with borrowed money it would, since "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and the
rule is "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. A share whose own
balance sheet carries $9.8B of debt principal against a $0.4B market value is one where a total loss of the stake is a live
outcome (Q9 material, recorded below), so the rule bears on sizing if the questions were ever passed. No breach in the
buyer's conduct as such.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years", with "some notion of how the industry will develop and where the company will stand within the industry"
**[M2012-065]**; "a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]**.

**What is understood.** The product and the mechanics are plain from the 10-K (`0001193125-26-059509`): 69 general acute care
hospitals at 2025 year-end in 36 markets across 14 states, most in "larger non-urban service areas in which we believe we are
the primary, if not the sole, provider"; revenue is volume times a price that is mostly set by others; labour is the largest
cost (salaries and benefits 43.3% of 2025 revenue, supplies 14.9%, other operating expenses 27.6%, Item 7). The product can be
understood without the economics being foreseeable, and the rows say which one counts: "What is important is that I
understand the economic dynamics of the industry" **[M2011-014]**.

**The key variables, and how predictable they are** **[M1998-044]**:
1. **The price, set mostly by government.** Medicare 17.4%, Medicare Managed Care 18.0% and Medicaid 16.0% of 2025 revenue,
   51.4% together (Item 1, Sources of Revenue). Of Medicare's rates the filer says: "These rates are indexed for inflation
   annually, although increases have historically been less than actual inflation." The other 47.8% is negotiated with
   payers whose "consolidation among private third-party payors tends to increase payor bargaining power" (Item 1,
   Competition).
2. **The policy now enacted and still being written.** The 2025 Reconciliation Law limits Medicaid eligibility (work
   requirements by 2026-12-31, six-monthly redeterminations), freezes and narrows provider taxes from fiscal years after
   2026-10-01 with tighter limits from federal fiscal 2028, and directs caps on state directed payments; the enhanced ACA
   marketplace subsidies expired at the end of 2025; CMS is phasing out the Inpatient Only List over three years from 2026;
   a 0.5% annual cut to the outpatient conversion factor began in 2026 "and was expected to continue for approximately 16
   years" (Item 1, Payment; Item 7). The filer's own forecast of the effect: "Although we are unable to fully assess the
   magnitude of the future impact of the 2025 Reconciliation Law, we expect the law to adversely impact our revenue and
   financial results" and "We cannot estimate the impact of Medicare and Medicaid reimbursement changes that have been enacted
   or otherwise determined or that are currently or may in the future be under consideration" (Item 7).
3. **Where the company will stand, and with which hospitals.** The footprint is not fixed: 69 hospitals at 2025 year-end,
   after four hospitals sold and three majority interests sold in 2025, two sold in 2024, and eight sold and one majority
   interest sold in 2023 (Item 7); nine more sold in the first half of 2026, hospitals with about $1.6B of 2025 revenue (10-Q
   MD&A, `0001193125-26-314196`); and "we may sell additional hospitals and/or non-hospital businesses" (both filings). Which
   hospitals remain in ten years depends on what must be sold to meet the debt (Q9 material), not on the business alone.
4. **The thinness of the margin the price acts on.** Owner cash before interest, recast in the COMPUTATION below, ran
   between −1.3% and 6.4% of revenue in 2021 to 2025 and averaged 3.6% in 2022 to 2025. A change of two or three points in
   the price of half the revenue is the whole of that margin.

**The tests.**
- *Is it important and knowable?* The price variable decides the earnings, and its enacted changes are, by the filer's own
  statement, not estimable: "If something’s important but unknowable, forget it." **[M2006-076]**; "If something is not
  very predictable, forget it." **[M1998-044]**.
- *Would the insiders write it down?* The company, with every contract and every state's rules in hand, writes that it
  "cannot estimate" the effect of changes already enacted. That is the insiders declining to "put down on paper their
  predictions" **[M2000-105]**.
- *Do the past statements tell me the future ones?* **[M2008-033]** No: every year in the window includes hospitals later
  sold; 2025's net income of $509M attributable to the company carried a $406M net gain on sales and a $163M tax benefit from
  the 2025 law (Item 7); operating cash in the first half of 2026 was −$209M against +$208M a year before (10-Q).
- *How far off could I be?* **[M2011-084]** Far: the five recast years span a negative figure to 6.4% of revenue, before any
  of the 2025 law's cuts arrive.
- *Do I doubt it is inside?* Yes, and "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**.

**Contrary evidence, written down as found** **[M1997-127]**: the speakers' health-care rows read the industry as one that
resists change, with "the political power that the industry will have" **[M2025-056]** and "so many people have a vested
interest" **[M2021-053]**, which cuts toward stable economics; the same-store business grew revenue 4.6% and income from
operations 7.2% in 2025; demand rises with age (the service areas' population aged 65 or older grew 16.8% from 2020 to 2025,
Item 1); and the largest rival's record (AFTER THE STOP, Q2) shows that hospital economics can be steady for a strong
operator. These are real. They speak to the industry's demand and to the strongest operator; they do not tell where this
company's price, its footprint and its thin margin will be in ten years, which is the question **[M2012-065]**.

**The routing, and the cause.** The routing paragraph of Q1 names fast-moving technology as the usual cause; here the cause is
a different one, a price set by legislatures and agencies whose enacted changes the filer itself cannot estimate. The tests
that close the file are Q1's own (tests 2, 3, 4, 5, 8 and 9). The cause is **NATURE**, not WORK: the deciding forecast is one
the company's own management, holding every filing an outsider could read and more, declines to make, and "We couldn't solve
this problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**. The box is "too
hard" **[M2006-013]**, and it is not a judgment of the business's quality or price: "It doesn’t mean it isn’t a good buy. It
doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
**[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** The ten-year earning power cannot be foreseen: half the price is set by government, the
enacted changes to it are declared not estimable by the filer (10-K Item 7, `0001193125-26-059509`), and the margin it acts on
averages a few points of revenue.

Q2 to Q10 and Q12: **NOT REACHED** (the file closed at Q1). Facts already found are written below, not weighed.

---
## THE BOX
**TOO HARD (NATURE) at Q1** (the ten-year economics cannot be foreseen: 51.4% of revenue at government-set prices whose
enacted changes the filer says it "cannot estimate", acting on an owner-cash margin before interest of about 3.6% of revenue;
the footprint itself is being sold down to meet the debt); integrity facts recorded, not judged. COMPUTATION beneath the stop:
no case earns the floor at $3.00; every case of the range, on the all-equity basis, values the business below its net debt.

---
## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).*

### Bearing on Q2 (the castle)
- **Competitors named by the filer.** The 10-K's Item 1 names no SEC-filing rival: "In most markets in which we are not the
  sole provider of general acute care health services, our primary competitor is a municipal or not-for-profit hospital",
  which are "exempt from sales, property and income taxes" (`0001193125-26-059509`). Those rivals do not file with the SEC
  (flagged); the buyers of its 2025-2026 hospitals (Vanderbilt University Medical Center, Huntsville Hospital Health System,
  Freeman Health System, Ascension, AdventHealth, Duke, Tenor Health Foundation) are of that kind. The proxy
  (`0001193125-26-140269`) names "the other three major hospital management companies": HCA, Tenet and Universal Health
  Services. Those three are the competitor row below.
- **The competitor row**, operating margin over ten years (USD revenue basis; CYH: income from operations with the
  "Impairment and (gain) loss on sale of businesses, net" line added back, from the filed income statements in the FY2018,
  FY2021, FY2023 and FY2025 10-Ks; rivals: pre-tax income plus interest expense over revenue from their own 10-K XBRL facts,
  HCA shown with its asset-sale gains of 2018, 2021 and 2022 taken out; transcription, filed statements not opened):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | ten-year average |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CYH | 5.7% | 1.6% | 6.2% | 6.0% | 10.0% | 11.5% | 7.3% | 7.0% | 6.7% | 8.7% | 7.1% |
| HCA (CIK 860730) | 15.7% | 13.9% | 14.3% | 13.8% | 13.6% | 16.6% | 15.0% | 14.8% | 15.0% | 16.0% | 14.9% |
| UHS (CIK 352915) | 13.1% | 12.3% | 11.0% | 10.8% | 11.8% | 10.9% | 7.4% | 8.0% | 10.6% | 12.3% | 10.8% |
| THC (CIK 70318) | 5.8% | 4.5% | 8.9% | 7.1% | 9.5% | 14.4% | 11.7% | 12.2% | 29.4% | 17.0% | 10.1% without 2024 |

  CYH's 2020 and 2021 include pandemic relief income ($148M recognized in 2021 and $173M in 2022, FY2023 10-K); Tenet's 2024
  carries large hospital-sale gains. Pre-tax operating return on total assets in 2025, same definitions: CYH 8.2%, HCA 19.9%,
  UHS 13.7%, Tenet 12.2% (crude: total assets include goodwill).
- **Competition facts from the 10-K.** Patients in CYH's service areas "may travel to these other hospitals" for "services
  we do not offer, payor networks that exclude our providers or physician referrals", and "may subsequently shift their
  preferences to those hospitals for services we do provide"; the tax exemptions "may provide the tax-supported or
  not-for-profit entities an advantage in funding general and capital expenditures"; some states are removing
  certificate-of-need laws, "which may reduce barriers to entry" (Item 1, Competition).
- **Volume.** Consolidated admissions fell 5.4% and adjusted admissions 6.3% in 2025 (divestitures); same-store admissions rose
  1.5% and adjusted admissions 0.6% (Item 7). Licensed beds 11,902 → 11,403 → 10,458 at 2023, 2024, 2025 year-ends (Item 1).
- **Parts.** One reportable segment, hospital operations (10-Q Note 12); no parts table applies.

### Bearing on Q3 (capital)
- Capital spending ran below depreciation in every year of the window: 469 / 415 / 467 / 360 / 335 against D&A 540 / 534 /
  505 / 486 / 426 for 2021 to 2025 ($M, cash-flow statements); 2026 is guided at "$350 million to $400 million" (10-K Item 7).
  The filing gives no split between maintenance and growth spending ("expansion and renovation", "additional access points",
  "routine expenditures", Item 7).

### Bearing on Q4 (the accounts)
- Recurring items called non-recurring: an "Impairment and (gain) loss on sale of businesses" line in every year 2016 to the
  first half of 2026 (−$406M gain in 2025, $301M charge in 2024, −$262M gain in the first half of 2026); a gain or loss on
  early extinguishment of debt in every year 2014 to 2026 (`tools/run.py` tags; 10-Q).
- An adjusted figure featured: "Adjusted EBITDA" ($1,526M for 2025) is set out in Item 1's selected operating data beside the
  GAAP figures, defined to add back, among other items, "net income attributable to noncontrolling interests" and "expense
  related to government and other legal matters" (10-K Item 1, note 8 to the table). (A habit weighed at Q4 and judged at
  Q5 under the gaps case, section A; recorded here, not weighed.)
- A change in the professional liability estimate of $149M pre-tax in 2024 (10-K Item 7, critical accounting estimates).
- Distributions to minority partners of $121M to $164M a year (cash-flow statements) are a cash cost to the common holder.
- 2021's operating cash of −$131M carries the repayment or recoupment of Medicare accelerated payments received in 2020
  (FY2021 and FY2023 10-Ks); the filer ties that year's figure to the repayment.

### Bearing on Q5 (the people): integrity facts, recorded, not judged
- "On January 11, 2024, we received a Civil Investigative Demand, or CID, from the Department of Justice for documents and
  information relating to a variety of subjects, including practices and procedures related to utilization review, inpatient
  admissions and inpatient dialysis at our hospitals" (10-K Item 3).
- "On October 31, 2024, the Department of Justice notified us that it is conducting a criminal investigation of Dr. Hyatt’s
  conduct" at the Northwest Arkansas behavioural health unit; "The Department of Justice has advised Northwest and several of
  its current and former officers and employees that they are also subjects of its investigation" (10-K Item 3). Northwest's
  four hospitals were sold to Freeman Health System on 2026-06-01 (10-Q).
- The QHC Litigation Trust suit (filed 2021-10-25) seeks recovery arising from the 2016 spin-off of Quorum Health, "including
  the $1.21 billion paid by QHC to the Company"; a motion to dismiss was granted in part and denied in part on 2023-03-16; the
  company's summary-judgment motion of 2025-08-25 is pending (10-K Item 3).
- "From time to time, we detect issues of non-compliance with federal healthcare laws pertaining to claims submission and
  reimbursement practices and/or financial relationships with physicians", addressed by repayment and voluntary disclosure
  protocols (10-K Item 3).
- Pay: the chief executive, Kevin J. Hammons, received total compensation of $4,772,869 for 2025 ($3,473,366 for 2024), with
  non-equity incentive pay of $1,746,642; the pay ratio is 60:1 (proxy, `0001193125-26-140269`).

### Bearing on Q6 (the money and the owners)
- No open-market repurchase programme ("We had no open market share repurchase programs", 10-K Item 5); the last repurchase
  of size in the facts read was $159M in 2015. No dividend; the debt agreements leave "approximately $300 million of capacity
  to pay permitted dividends and/or repurchase shares" (Item 5). With no buyback, Q6's buyback test has nothing to read.
- Shares on the 10-K covers: 112.8M (2016), 117.9M (2020), 129.6M (2021), 138.9M (2025), 141.0M (2026 10-Q): about 25% more
  shares in ten years while the business shrank. The 2021 step was not traced to its filing in this run.
- Divestiture proceeds go to "general corporate purposes (including potential debt repayments and/or debt repurchases)"
  (10-K and 10-Q); in May 2026 about $600M of proceeds repurchased $368M of the 4.750% 2031 notes and $231M of the 10.875% 2032
  notes by tender (10-Q Note 6).

### Bearing on Q7 (value): COMPUTATION, NOT A CLEARANCE
*Arithmetic beneath a closed file; no entry language; script and output at `Test Runs/_research 2026-10-13 CYH/compute.py`
and `compute_output.txt`.*
- **Owner cash after every real cost** ($M; cash-flow statements of the FY2021, FY2023 and FY2025 10-Ks): operating cash,
  plus the cash tax paid on divestiture gains (the 10-K states $169M in 2025 and $17M in 2024 "related to the gains on
  hospitals divested"), less stock pay, capital spending, purchases of businesses, distributions to minority partners and
  finance-lease principal. Levered: 2021 −749, 2022 −269, 2023 −461, 2024 −62, 2025 +199. **Before interest** (cash interest
  paid 778 / 835 / 801 / 741 / 804, added back after tax): 2021 −166, 2022 +357, 2023 +140, 2024 +494, 2025 +802, which is
  −1.3%, 2.9%, 1.1%, 3.9% and 6.4% of revenue. First half of 2026, levered: −509 (operating cash −209, capex 152,
  acquisitions 53, minority distributions 90, stock pay 5; 10-Q), with $437M of interest paid.
- **CONVENTIONS of this run, confessed:** (1) the interest added back for the all-equity basis is taken after a 25% tax rate
  (21% federal plus about 4% state; the company's 2025 effective rate of 6.6% rests on valuation-allowance releases, so the
  company's own rate does not separate the interest shield; rationale: Q7 asks for owner cash before interest after the
  company's tax, and the shield must be priced at some stated rate). (2) Divestiture proceeds are not owner cash, and the
  base is restated to the hospitals still owned: each case's owner-cash margin on revenue is applied to a base revenue of
  $10,885M (2025 revenue of $12,485M less the $1.6B of 2025 revenue of the hospitals sold in the first half of 2026, 10-Q
  MD&A; the 2025 revenue of hospitals sold during 2025 is not deducted, which overstates the base slightly); rationale:
  specific (c) nets businesses sold against businesses bought, written for a buyer of businesses; for a business selling a
  seventh of itself in a year to pay debt, counting the proceeds as owner cash would book the liquidation as earnings, and
  the net debt used below has already been cut by those proceeds.
- **Window.** 2021 is aberrational on the filer's own description (the repayment of Medicare accelerated payments), so by
  specific (a) the central base is 2022 to 2025; the literal 2021-2025 window is shown beside **[L2005-003]**. There is no
  full cycle to average.
- **Growth.** The shown growth of owner cash before interest, 2022 to 2025 end to end, is 30.9% a year; carried ten years on
  the central base it would require owner cash of 61% of base revenue against a highest earned share of 6.4%, an absurdity,
  so by specific (f) it is cut to the business's own sales growth over the same years, 0.74% a year **[M1999-067]**,
  **[M1997-095]**. The literal window changes sign, so its range is the no-growth case alone (specific (b)).
- **Maintenance.** The filing does not split maintenance from growth spending, so the central case charges all capital
  spending (specific (e) not available); because capital spending ran below depreciation every year, the depreciation case
  is shown beside and is the lower one.
- **Net debt** at 2026-06-30 (10-Q, `0001193125-26-314196`): total debt $9,578M as filed plus $192M of unamortized issuance
  costs, a principal of $9,770M (finance leases of $298M included), less cash of $149M: **$9,621M**. Operating leases left
  out (rent is inside operating cash). The captive insurer's securities are not deducted (they back the professional
  liability reserves). Minority interests are carried through their distributions, deducted above, not added to net debt.
  No signed, unclosed deal is stated in the 10-Q.
- **The range, all-equity basis, per share** (sovereign 5.60%; ten years at the growth stated, then zero nominal growth;
  141.009M shares) **[L2017-004]**:

| case | owner cash before interest | value of the business | per share, less net debt |
|---|---|---|---|
| central, capex, base restated, no growth (bottom) | $391M | $6,986M | **−$18.69** |
| central, capex, base restated, growth 0.74% (top) | $391M | $7,409M | **−$15.68** |
| beside: central, capex, base not restated, no growth / 0.74% | $448M | $8,003M / $8,485M | −$11.47 / −$8.06 |
| beside: central, depreciation instead of capex, restated, no growth | $309M | $5,526M | −$29.04 |
| beside: literal 2021-2025 window, capex, restated, no growth | $284M | $5,069M | −$32.28 |
| beside: 2025 alone, restated, no growth (not a case of the convention) | $699M | $12,492M | +$20.32 |

- **The floor, tested first** **[M2003-149]**: at $3.00 the enterprise is priced at $10,044M (market value $423M plus net debt).
  The central owner cash before interest yields 3.9% on it (4.5% unrestated); the best single year, 2025, restated, yields
  7.0%. A 10% return on the price would need about $1,004M a year, 9.2% of base revenue, above any year in the window. **No
  case earns the floor at the price**: under Q7 the file would close OUT whatever the width. The width test is not reached:
  both ends are below zero.
- **VALUE RANGE (reporting figure): −$18.69 to −$15.68 a share** against $3.00, all-equity basis: on every case the business
  is worth less than its net debt at the long government rate.
- **FAIR PRICE (reporting figure, Part VII): none above zero.** Each end valued at ten percent gives the business $3,912M and
  $4,114M, so −$40.49 and −$39.05 a share less net debt, averaging **−$39.77**; owner cash after the company's own tax (cash
  taxes paid, the tax on divestiture gains removed), all-equity basis. **Equity-only, beside:** owner cash after interest
  averages −$148M a year (central) and −$268M (literal), so there is no positive equity-only figure either. No cheap price is
  reported.

### Bearing on Q8 (the alternatives)
- The 30-year Treasury yields 5.60%; the central owner cash before interest yields 3.9% on the enterprise priced at $3.00.

### Bearing on Q9 (the target's debt)
- Debt principal at 2026-06-30 by series (10-Q Note 6): 6⅞% senior 2028 $42M; 6% senior secured 2029 $644M; 6⅞% junior-
  priority 2029 $1,244M; 5¼% senior secured 2030 $1,535M; 6⅛% junior-priority 2030 $1,227M; 4¾% senior secured 2031 $689M;
  10⅞% senior secured 2032 $1,549M; 10¾% senior secured 2033 $700M; 9¾% senior secured 2034 $1,790M; finance leases $298M.
  About $5.3B falls due in 2029 to 2031; the newest notes carry 9¾% to 10⅞%. The filer: "we have a substantial amount of
  indebtedness with certain series of our outstanding notes and other debt scheduled to mature in close proximity to each
  other" (Item 1A).
- 2025: cash interest $804M against income from operations before impairment and gains of about $1,082M; "debt as a
  percentage of total capitalization was 113%" (Item 7). The issuer "is a holding company with no direct operations",
  dependent on its subsidiaries' payments (Item 1A). The $1.0B asset-based facility had $751M available at 2026-06-30 (10-Q).
- Professional liability is "primarily self-insured" with excess cover purchased (Item 7); expense $295M in 2025, $372M in
  2024.
- For a whole business the acquisition criteria ask for "little or no debt" **[R1997-001]**; recorded, not applied (Q9 not
  reached).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `06766245`); written question by question; committed after Step 0,
      after Q1 and the box, after the facts and the computation, and after this audit (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      nothing until it is folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One directory listing of `Test Runs/` showed
      other runs' file names; declared under contamination above, not used.
- [x] Every v5 id was checked against `principle_ledger_v5.csv` by the script `Test Runs/_research 2026-10-13 CYH/check_ids.py`,
      which also checks that each quoted fragment beside an id is in that row; every filing fact carries its accession; the
      competitor figures are XBRL transcription and flagged as such.
- [x] The order was kept; Q1 failed and closed the file; nothing after it is a clearance; the arithmetic beneath it is headed
      COMPUTATION, NOT A CLEARANCE and carries no entry language.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy; the sovereign from the US
      Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down where found (foundations and Q1); the facts for later questions are under AFTER THE STOP,
      with "integrity facts recorded, not judged" in the box line.
- [x] Not a point-in-time run; no anchor issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 material was not read as rule.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message and the reply).

**Honest limits.** The competitor row rests on XBRL facts, not on the rivals' filed statements, and mixes CYH's income from
operations with the rivals' pre-tax income plus interest; the two differ by small items (equity earnings, other income). The
base restatement for the 2026 sales uses one revenue figure from the 10-Q and leaves the 2025 sales' partial-year revenue in;
the interest shield's tax rate is a stated guess. The 8-K earnings exhibits and the rivals' filed 10-Ks were not opened. None
of these could lift any case of the computation near the floor (the best single year, restated, yields 7.0% on the enterprise
at the price against a floor of about 10%), and none bears on the Q1 close, which rests on the filer's own sentence.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1's routing names one cause, not this one.** The routing paragraph sends a business to Q1 TOO HARD when "its industry
changes fast"; it says nothing of a business whose price is set by government and whose enacted price changes the filer says
it cannot estimate. I applied Q1's own tests 4 and 5 (important but unknowable; would the insiders write it down) and closed
at Q1, but a second analyst could take the economics as understood (the product is plain and the speakers' health-care rows
call the industry slow to change) and close the same name at Q2 or Q7 instead; the box would then be OUT, not TOO HARD
(NATURE), which changes whether a lower price ever reopens it. The framework would be clearer if it said whether a
government-set price whose enacted changes the filer declares not estimable is a Q1 matter, a Q2 matter, or a Q7 width matter.
(2) **Specific (c) is written for a buyer of businesses and misreads a seller.** It nets "businesses sold" against
businesses bought as capital spending; for CYH, which sold hospitals for over $1.0B in 2025 and $1.2B in the first half of
2026, that would count a liquidation as owner cash. I confessed a CONVENTION of this run (proceeds excluded, the base restated
to the hospitals still owned). (3) **The rivals for Q2 when the 10-K names none that file.** The brief says to take the rivals
the 10-K names; CYH's 10-K names only municipal and not-for-profit hospitals, none of which files with the SEC. I took the
three hospital companies the proxy names as its own peers and said so. (4) **The fair price when the range sits below zero.**
Part VII defines the fair price as the average of the two ends valued at ten percent; when both are below net debt the figure
is negative and means only that no positive price earns the floor; the text could say how such a figure is reported (here:
"none above zero", with the negative arithmetic shown).
