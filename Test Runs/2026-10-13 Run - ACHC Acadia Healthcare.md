# Company Run — Acadia Healthcare Company, Inc. (NASDAQ: ACHC) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker, 2026-10-13).*

*Dispatched run under operator rule 10 and the canonical brief (`Screens/_daily/_dispatch_brief.md`), with the one stated
departure: the lines of evidence were derived by the analyst from the 10-K's Items 1, 1A and 7 (see Q1, "The lines of
evidence chosen"). Template copied before any fetch (commit 906885d2). Working folder `Test Runs/_research 2026-10-13 ACHC/`
(notes, scripts, the `tools/run.py` output; raw filings in its ignored `cache/`).*

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $30.20 (2026-10-13, the live quote printed by `tools/run.py`; **aggregator, flagged** under operator rule 5).
- **Shares by class** (one class, common stock, $0.01 par): **93,100,275** at July 27, 2026 from the cover of the 10-Q for
  the quarter ended June 30, 2026 (filed 2026-07-28, accession `0001193125-26-321076`; `python Screens/cover_shares.py ACHC`
  prints the same). **Check against issued less treasury:** the same 10-Q's balance sheet shows **90,868,250** shares issued
  and outstanding at June 30, 2026 and no treasury stock; the 10-K shows the same pattern (cover 92,212,000 at
  2026-02-25 against 90,452,843 issued and outstanding at 2025-12-31). The gap of about 2.2 million shares recurs on both
  covers and is not explained in the filings read; no 8-K or prospectus filed after the 10-Q issues shares (8-Ks of
  2026-07-28 and 2026-09-25 read). **CONVENTION of this run:** per-share figures use the larger cover count, the balance-sheet
  count shown beside where it matters; rationale: the cover is the filed count of shares outstanding and the larger count
  cannot overstate value per share.
- **Market cap:** $2,811.6M at the cover count ($2,744.2M at the balance-sheet count).
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-09 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-27, accession `0001193125-26-078266` (Items 1, 1A, 3, 7,
  8 and Notes 5 and 11 read); 10-Q for Q2 2026, filed 2026-07-28, `0001193125-26-321076` (balance sheet, debt note,
  contingencies note, MD&A cash flows); proxy DEF 14A filed 2026-03-25, `0001140361-26-011130` (pay sections); 8-Ks of
  2025-10-07 (`0001193125-25-233507`), 2025-11-10 (`0001193125-25-274380`), 2026-01-20 (`0001437749-26-001486`),
  2026-01-23 (`0001193125-26-020169`), 2026-03-12 (`0001193125-26-104272`), 2026-04-23 (`0001193125-26-173769`), 2026-05-06
  (`0001193125-26-209324`), 2026-05-18 (`0001193125-26-229138`), 2026-07-28 with Exhibit 99.1 (`0001437749-26-024693`),
  2026-09-25 (`0001437749-26-031225`); for the cycle, the 10-Ks for FY2021 (`0001564590-22-007930`), FY2023
  (`0000950170-24-022057`) and FY2024 (`0000950170-25-029095`). Rival: Universal Health Services 10-Ks for FY2025
  (`0001193125-26-071676`), FY2024 (`0000950170-25-027785`) and FY2022 (`0000950170-23-004656`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for FY2025,
  $131,898 thousand on the filed consolidated statement of cash flows (10-K `0001193125-26-078266`), against $131.9M in the
  `tools/run.py` transcription; capital expenditures $571,807 thousand against $571.8M. Both agree.
- `python tools/run.py ACHC` arithmetic lines only (output kept in `Test Runs/_research 2026-10-13 ACHC/run_py_output.txt`;
  its window is three years, so the five-year figures below are this run's own sums from the filed statements):

| FY | Op. cash (cont.) | Stock pay | Capex | of which maintenance (filer's split) | Acquisitions | Minority distributions | Interest paid |
|---|---|---|---|---|---|---|---|
| 2021 | 374.2 | 37.5 | 244.8 | 41.8 | 139.0 | 1.6 | 93.7 |
| 2022 | 380.6 | 29.6 | 296.1 | 60.5 | 9.5 | 5.1 | 65.7 |
| 2023 | 462.3 | 32.3 | 424.1 | 99.6 | 0.3 | 5.1 | 80.7 |
| 2024 | 129.7 | 37.1 | 690.4 | 104.0 | 53.5 | 3.0 | 113.4 |
| 2025 | 131.9 | 31.7 | 571.8 | 104.4 | 8.2 | 3.9 | 124.7 |

  (USD millions. The maintenance split is the filer's own words: "routine or maintenance capital expenditures of $104.4
  million and expansion capital expenditures of $467.4 million" for 2025, 10-K FY2025 Item 7; 2024 and 2023 from the FY2024
  and FY2025 10-Ks; 2022 and 2021 from the FY2023 and FY2021 10-Ks. Proceeds from property sales: 3.5, 7.1, 29.4, 10.4,
  23.8.) Owner cash after stock pay, maintenance capex and minority distributions, after interest: 293.3, 285.4, 325.3,
  -14.4, -8.1; five-year average **$176.3M**. After all capital spending and acquisitions (net of property sales): -45.2,
  47.4, 29.9, -643.9, -459.9; average **-$214.3M**. Operating cash in 2024 carries the $400.0M Desert Hills payment and in
  2025 the $147.5M securities settlement (10-K FY2025, Item 7, Liquidity). D&A 106.7, 117.8, 132.3, 149.6, 189.2.

**Balance sheets, 2016 to 2025, read first**, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** (the `tools/run.py` ten-year table, read
against the filed statements of the 10-Ks listed; first-filed vintages). What moved, and why:
- **Size and the U.K. business.** Total assets ran $6.0bn to $6.9bn from 2016 to 2020 with a U.K. arm; the U.K. business
  was sold in January 2021 (proceeds of $1,511.0M, 10-K FY2021, Item 7, investing activities), and assets fell to $4.8bn at
  2021 while long-term debt fell from $2,969M to $1,479M. The 2018 and 2020 net losses (-$175.8M and -$672.1M) are mostly
  the U.K. (discontinued losses of -$233.0M and -$812.4M); retained earnings went from $429M (2017) to -$310M (2020).
- **Equity against goodwill.** Equity rose from $2,518M (2021) to $3,074M (2024) and fell to **$1,949M** at 2025; goodwill
  fell from $2,265M to **$1,296M** on a **$996.2M goodwill impairment** in 2025, which the filer ties to "higher professional
  and general liability (“PLGL”) expenses associated primarily with patient-related litigation", lower revenue projections
  "to reflect changes in Medicaid reimbursement, primarily related to New York State exclusion of Medicaid referrals to our
  facilities in Pennsylvania", and "a sustained decline in our stock price" (10-K FY2025, critical accounting estimates).
  Retained earnings went to **-$766M**. Tangible equity at 2025 is about $556M.
- **Property against debt.** Property and equipment rose from $1,771M (2021) to **$3,111M** (2025) on expansion capex of
  about $1.82bn over the five years; long-term debt rose from $1,479M (2021) to **$2,472M** (2025), face $2,429.6M at
  June 30, 2026 (10-Q debt note). The building programme was paid for with borrowing, not with owner cash, which was
  negative after all spending in four of five years.
- **Receivables against sales.** Receivables rose 20.6% in 2025 ($365M to $441M) against revenue up 5.0%; days sales
  outstanding went from 43 to 49, which the filer explains as "new facilities that continue to ramp up during the start up
  period, as well as identifiable payor delays" (10-K FY2025, Item 7). Other current assets rose from $136M to $240M (the
  filer shows a $31.5M insurance receivable for the securities settlement inside it). Inventory is immaterial (about $6M).
- **Liabilities that grew without debt.** Other liabilities rose from $122M to $202M and other accrued liabilities from $88M
  to $137M in 2025, alongside the professional liability reserve increases; redeemable minority interests in joint ventures
  rose from $65M (2021) to $192M (2025).
- What the figures cannot say: the balance sheet carries no estimate for the DOJ Criminal Division and SEC investigations,
  the pending 2020-2025 securities class action or the sixth Desert Hills suit, each of which the filer says it "cannot
  reasonably estimate" (10-K FY2025, Note 11).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which for a business whose price moves on verdicts, subpoenas and state budgets puts the weight on what the
business will earn, not on the quote. "the market is there to serve you and not to instruct you" **[M2006-077]**: the fall in the share price
(a reason the filer itself gives for the goodwill charge) is a price, not a finding. Margin of safety: if it needs pencil
and paper "it’s too close to think about" **[M1996-084]**. Macro conclusions "just never enter into the discussion" **[M2000-094]**; the Medicaid law of
2025 is not macro here, it is the price the business is paid for most of what it sells, and it is read as a property of the
business. "you do not get impartial advice from Wall Street" **[M2020-037]**: the filer's "Adjusted EBITDA" and guidance are read as the filer's own
framing. The analyst's habit: look for "what’s wrong in things" **[M2025-013]**, and hunt the evidence against hardest.
**Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**): (1) the rival Universal Health Services has earned behavioral
segment operating margins of 17.1% to 19.7% in every year 2021 to 2025 (UHS 10-Ks above), which says the field's economics
can be stable and foreseeable for a well-run operator; (2) the filer reports demand growing (same-facility patient days
+2.1% in 2025, +3.2% in 2024) and joint ventures with large health systems (Henry Ford Health, Geisinger, Ascension Seton,
Fairview, ECU Health in 2025; Orlando Health and Methodist Jennie Edmundson in Q2 2026); (3) certificate-of-need laws in
many states regulate new capacity (10-K Item 1); (4) maintenance capital is low, "approximately 3% of our revenue" (10-K
Item 1); (5) operating cash rose to $223.6M in the first half of 2026 and the filer raised its 2026 operating cash
guidance to $350M to $400M (8-K 2026-07-28, Exhibit 99.1; a projection, recorded as a fact and not used in any figure).
Each is weighed at Q1 below.

## THE STANDING RULE
The buyer's own conduct: a purchase in cash, unlevered, sized so that a total loss could not touch what the buyer needs,
meets "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]** and the
refusal of practices that bring "sudden demands for large sums" **[L2014-024]**. Nothing in the target changes the buyer's
rule; the target's own debt is a matter for Q9. No breach on the buyer's side.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The lines of evidence chosen, and why** (the brief's departure: derived by the analyst from the 10-K, not handed down).
From Item 1: what is sold (inpatient and outpatient behavioral care: acute psychiatric 55% of 2025 revenue, specialty 17%,
comprehensive treatment centers 17%, residential 11%), who pays ("57.7% of our revenue from Medicaid, 24.6% from
commercial payors, 14.3% from Medicare"), how it grows (beds, joint ventures, de novo, acquisitions), and who competes
(UHS by name). From Item 1A: the risks the filer itself puts first, "Legal Proceedings and Regulatory Risks", led by
governmental investigations and patient-care litigation, then government payment. From Item 7 and Note 11: what those
risks have already cost (legal settlements expense $394.2M in 2023 and $151.0M in 2025; "Government investigations" costs
of $135.3M in 2025 and $30.6M in 2024; the $996.2M goodwill impairment), and what is still open. These were chosen because
they are the variables that decide the business's earnings ten years out; demand, which the filer stresses, was read as
well and written down above as contrary evidence.

**The test applied:** "trying to identify the key variables in that particular business, and evaluating how predictable they were first" **[M1998-044]**. Understanding is "a reasonable fix
on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, "where the
business will be in 10 years" **[M2000-037]**. The product is plain: a bed-day of psychiatric or addiction care. The
economics turn on four variables, and the filings say how knowable each is.

1. **The price, set by governments.** About 72% of revenue comes from Medicare and Medicaid (10-K, Item 1A), and Medicaid
   pays from 46 states, the District of Columbia and Puerto Rico. The One Big Beautiful Bill Act of July 2025 restricts
   federal matching funds, bars new or increased provider taxes for state fiscal years after October 1, 2026, caps state
   directed payments at Medicare rates for new programs, and reduces grandfathered programs from January 1, 2028 (10-K,
   Item 1, "One Big Beautiful Bill Act"). The filer: "We are unable to predict whether or how future legislation,
   rulemaking, or judicial action will impact implementation of the OBBBA" and, of payment generally, "We are unable to
   predict the effect of recent and future policy changes on our operations" (Item 1A). Lumps of revenue arrive from state
   supplemental programs on the states' timing ($48.7M of prior-period Tennessee revenue in Q2 2025; $22.3M of Florida in Q2
   2026; the proxy says incentive Adjusted EBITDA for 2025 was adjusted by $75.9M for amounts recognized from Tennessee
   Medicaid; 8-K 2026-07-28 Ex. 99.1 and DEF 14A). The size of the supplemental programs inside revenue is not stated in
   the 10-K read: no instance found by a search of the 10-K text for "supplemental". One state (New York) excluded Medicaid
   referrals to the Pennsylvania facilities, which the filer named as a cause of the 2025 write-down.
2. **The cost of patient-care liability.** A jury awarded $80.0M compensatory and $405.0M punitive damages in one Desert
   Hills case in 2023, an award the filer says "far exceeded any precedent for comparable cases"; $400.0M was paid in
   January 2024 and a sixth suit is pending with no estimate (10-K, Note 11). A second jury awarded $35.0M and $70.0M
   against a treatment-centre subsidiary in May 2026, which the filer says "far exceeds any reasonable expectation based on
   precedent" (8-K 2026-05-18; 10-Q Q2 2026, contingencies note). The professional liability reserve was raised by $52.7M
   in 2025 and by $28.6M in Q2 2026 (10-K Item 7; 8-K 2026-07-28 Ex. 99.1). The rival shows the same in the field: a
   Virginia jury awarded three plaintiffs $60M compensatory, $180M trebled and $120M punitive damages against a UHS
   behavioral subsidiary in September 2024, the punitive part later reduced under Virginia law (UHS 10-K FY2025,
   `0001193125-26-071676`, Item 1A).
3. **Whether the core revenue was lawfully earned.** Since September 2024 the DOJ Criminal Division has held grand jury
   subpoenas "related to the Company’s acute care service line and related admissions, length of stay and billing
   practices", the SEC has subpoenaed "similar information as well as information relating to the CTC service line", members
   of Congress have asked about "admissions, length of stay, billing practices, and opioid treatment programs", and the
   company "cannot reasonably estimate the amount or range of the ultimate liability, if any" (10-K Note 11; the same in the
   10-Q of July 2026). The acute line is 55% of revenue. The filer's own Item 1A names what such investigations can bring:
   "the imposition of a corporate integrity agreement, loss of enrollment status, and exclusion from participation in
   governmental health programs", which pay about 72% of revenue. A securities class action covering 2020 to 2025 survived a
   motion to dismiss on July 24, 2026 (10-Q Q2 2026).
4. **Labour.** Salaries, wages and benefits are 55% of revenue (2025), with "rising labor costs and turnover" and contract
   labour named in Item 1. This is the ordinary variable of any service business and the least uncertain of the four.

**The tests, each against those facts.**
- **Is it important and knowable?** "If something’s important but unknowable, forget it." **[M2006-076]**. Variables 1 and
  3 are important beyond argument (one is the price of most of what is sold; the other decides whether payers that fund
  72% of revenue keep paying on the same terms), and the filer itself says neither can be predicted or estimated.
- **Would the insiders write it down?** The test is whether the people inside would put the ten-year economics "down on
  paper" or say "That’s too hard." **[M2000-105]**. The insiders here declined in writing, three times in one 10-K: unable
  to predict the payment law, unable to predict policy changes, unable to estimate the investigation. Within six months of
  the law they cut their own revenue projections and wrote off $996.2M of goodwill.
- **Do the past statements tell me the future ones?** Whether "the financial statements will tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**. They do not: of the last three years, 2023 carried a
  $394.2M legal charge, 2025 a $151.0M settlement, $163.6M of "transaction, legal and other costs" and a $1,007.9M
  impairment, and 2024 the $400.0M payment in cash; the pre-tax line went -$25.4M, $341.9M, -$1,065.9M (10-K FY2025).
  Owner cash after maintenance only (after interest) fell from $293M (2021) to -$8M (2025). The statements record events
  whose recurrence is the open question.
- **How far off could I be?** "some model in our mind of how far off we can be" **[M2011-084]**. On the price, the liability and the investigation, way off: anything from
  today's business continuing to a corporate integrity agreement or a narrowed government book.
- **Can I name the winner, not just the industry?** Demand may grow, but "there’s industries we know that may have a
  wonderful future, but we don’t have the faintest idea who the winners will be" **[M2012-067]**, and "dramatic growth
  ahead for an industry does not mean we can judge what its profit margins and returns on capital will be"
  **[L2009-005]**. The contrary evidence written above is that UHS's behavioral margins held at 17% to 20% through 2021 to
  2025; but UHS is a different company carrying the same field risks (its own nine-figure verdict), and its record does
  not answer variable 3, which is particular to this company.
- **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**. I do. **Do I only think I understand it?** "what would bother me is if I think I understand a business and I don’t" **[M1997-024]**: the product is understood; the earnings are
  not foreseeable.

**The speakers' own rows on the industry, weighed and not extended.** The rows on Berkshire's health-care venture speak of
"the political power that the industry will have" **[M2025-056]** and of "changing something that so many people have a
vested interest in doing" **[M2021-053]**. They are about Berkshire's own failed attempt on the buyers' side, and by the Q2
convention on a row about one company or venture they are weighed, not extended into a verdict on providers. Read as
contrary evidence, they say the industry's place in the economy is durable; they do not say what governments will pay a
given provider, which is variable 1, or how variable 3 ends.

**Which cause.** The deciding variables are a payment policy the filer says it is "unable to predict", liability awards the
filer twice calls beyond precedent, and an investigation the filer "cannot reasonably estimate". None is answered by a
filing not yet read; no reading of the public record resolves a criminal investigation in progress or a legislature's
future rates. This is the second cause the rows name, "the nature of the industry would be the roadblock"
**[L1993-023]**, with the insiders' own refusal to write the forecast down **[M2000-105]**, and not the first ("I haven’t
done the work" **[M1994-026]**). Study does not cure it: "we’re not going to learn enough in the followings five months to
make up for the fact that we went in deficient in the first place" **[M2008-086]** ("followings" is the transcript's). The
verdict is not a judgment of quality or of price: "It doesn’t mean it isn’t a good buy. [...] It just means that we don’t
know how to evaluate it." **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)**, the third of "in, out, and too hard" **[M2006-013]**. The ten-year earning power turns on government payment that the filer
  says it cannot predict and on the outcome of a DOJ Criminal Division investigation into the admissions, length of stay
  and billing of the acute service line (55% of revenue) that the filer says it cannot estimate (10-K FY2025 Item 1A and
  Note 11, `0001193125-26-078266`; 10-Q Q2 2026, `0001193125-26-321076`). The file closes here; a lower price does not
  reopen it.

## Q2 TO Q10, Q12: NOT REACHED
Closed at Q1 (operator rule 2). Facts already found that bear on them are written under AFTER THE STOP, not weighed.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year earning power turns on government payment the filer says it is
unable to predict and on a DOJ Criminal Division investigation of the acute line's admissions, length of stay and billing
that the filer says it cannot estimate: "If something’s important but unknowable, forget it." **[M2006-076]**; the insiders would say "That’s too hard." **[M2000-105]**; "the nature of the industry would be the roadblock" **[L1993-023]**. **Integrity facts recorded, not
judged.** COMPUTATION, NOT A CLEARANCE: value range **-$18.22 to $23.92 a share** (all-equity basis, maintenance case
central) against **$30.20**; no case earns the floor at the price. No re-look condition: a lower price does not reopen a
TOO HARD (NATURE); of such a name, "It doesn’t mean it isn’t selling for a fraction of its worth." **[M2000-038]**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found ("write it down in the first 30 minutes" **[M1997-127]**), under the question each bears on; no verdict; the box unchanged (operator rule 2).*

**Q2 (the castle).**
- **The competitor row.** The 10-K names one rival: "Universal Health Services, Inc. (NYSE: UHS)"; the rest are unnamed
  classes ("other acute inpatient psychiatric hospitals, other residential behavioral healthcare providers, other outpatient
  opioid treatment providers and general healthcare facilities that provide mental health services", and private equity as
  a rival buyer), so no further named rival could be read; flagged. Same metric, operating income before interest as a
  share of revenue, 2021 to 2025:

| Year | UHS behavioral segment, income from operations / net revenues | ACHC, before legal settlements, impairments, "transaction, legal and other costs" and provider relief income | ACHC, after every charge except interest and debt extinguishment |
|---|---|---|---|
| 2021 | 18.7% | 17.1% | 16.3% |
| 2022 | 17.1% | 17.1% | 17.0% |
| 2023 | 17.5% | 17.3% | 1.9% |
| 2024 | 19.7% | 16.6% | 14.5% |
| 2025 | 19.7% | 11.7% | -27.9% (2.5% without the goodwill impairment) |

  UHS figures from its 10-Ks FY2022 (`0000950170-23-004656`), FY2024 (`0000950170-25-027785`) and FY2025
  (`0001193125-26-071676`), "All Behavioral Health Care Services" tables; whether UHS's segment line carries all corporate
  overhead was not checked, so the comparison may flatter UHS. ACHC from its 10-Ks FY2023 and FY2025. Over the whole span
  UHS's behavioral margin rose about one point; ACHC's fell five points before the legal items and was far lower after them.
- **Price.** Same-facility revenue per patient day +2.8% (2025) and +4.3% (2024), patient days +2.1% and +3.2% (10-K
  Item 7); revenue per patient day fell 0.8% in Q2 2026 on the timing of supplemental payments (8-K 2026-07-28 Ex. 99.1).
  The price of about 72% of revenue is set by Medicare and Medicaid, not by the seller, and payers apply "utilization
  review" to "reduce admissions and lengths of stay" (10-K Item 1A).
- **Entry.** Certificate-of-need laws regulate capacity in many states, and "significant CON reforms have been proposed"
  (10-K Items 1 and 1A). Patients come through referral sources that "may instead refer patients to hospitals that are able
  to provide a full suite of medical services or to other behavioral healthcare centers" (Item 1).

**Q3 (capital).** Expansion capex of $1,817M and acquisitions of $210.5M over 2021 to 2025 (filer's split above) took
revenue from $2,314.4M to $3,312.8M, while operating income before the legal items went from $396.7M (2021) to $388.1M
(2025) (10-K FY2023 and FY2025 statements of operations). Pre-tax operating income before the legal items averaged $472.3M
over 2023 to 2025 against average net property of $2,743.7M (about 17%); after the average legal settlement and
"transaction, legal and other costs" of those years ($272.5M a year) it was $199.8M (about 7%). The filer says it judges
construction "by determining whether the projected cash flow return on investment exceeds our cost of capital" (Item 1A).

**Q4 (the accounts).** The balance sheets are read in Step 0. "Transaction, legal and other costs" appear every year
($62.0M, $46.8M, $163.6M in 2023 to 2025), of which "Government investigations" were $135.3M in 2025; depreciation rose
from $106.7M to $189.2M as the new facilities came in, "almost always true costs" **[L2015-004]**. The 10-K's MD&A does not feature an
adjusted figure (no instance found by a search of the 10-K text for "Adjusted EBITDA"), but each earnings release
leads with "Adjusted EBITDA" and gives and revises guidance (8-K 2026-07-28 Ex. 99.1: 2026 Adjusted EBITDA guidance
$590M to $615M, revised from $580M to $615M), and guidance excludes "non-recurring legal settlements expense" in a run of
years where such expense recurred. Under the Q4 convention these habits are recorded as weighing against ("a management that regularly attempts to wave away very real costs" **[L2016-006]**;
"an offense that has been encouraged by the scourge of earnings" guidance **[L2019-006]**) and carried to Q5, which was not reached. Receivables rose 20.6% against revenue up 5.0% in 2025 (Step 0).

**Q5 (integrity): facts recorded, not judged** (the box line carries the flag; a later run that reaches Q5 answers them
under "If you’ve got doubts, forget it." **[M2013-088]**).
- The 2019 securities class action (class period April 2014 to November 2018) settled for $179.0M with no admission;
  approved and dismissed with prejudice on April 29, 2026 (10-K Note 11; 10-Q Q2 2026).
- The 2017 OIG/DOJ investigation of nine facilities "focused on claims not eligible for payment because of alleged
  violations of certain regulatory requirements relating to, among other things, medical necessity, admission eligibility,
  discharge decisions, length of stay and patient care issues" was settled in September 2024 for $19.9M plus interest,
  with no admission (10-K Note 11).
- The DOJ Criminal Division grand jury subpoenas (September 2024, withdrawn and re-issued December 2024) on the acute line's
  admissions, length of stay and billing; SEC subpoenas including the CTC line; congressional requests; an internal
  investigation with "no findings or conclusions" yet (10-K Note 11; 10-Q Q2 2026).
- A second securities class action (purchasers February 2020 to February 2025) survived the motion to dismiss on July 24,
  2026 (10-Q Q2 2026). Derivative actions against former and current officers and directors received preliminary approval
  of a settlement on September 1, 2026 (8-K 2026-09-25, `0001437749-26-031225`); the stipulation (Exhibit 99.1) was not
  opened, so its terms are not recorded.
- Jury verdicts: Desert Hills, $80.0M and $405.0M (2023), settled with two related cases for $400.0M; Fashion Valley,
  $35.0M and $70.0M (May 2026) for a retaliatory termination claim, under challenge (10-K Note 11; 8-K 2026-05-18).
- Turnover at the top: the chief executive departed on January 20, 2026 with severance of 1.5 times salary and target
  bonus plus a $1,785,000 retention payment (8-Ks 2026-01-20 and 2026-01-23); the former chief executive (2018 to 2022),
  age 70, returned. The CFO seat passed from an interim (2025) to an outside hire on October 27, 2025, who resigned
  effective April 30, 2026, to an interim (the CFO of 2012 to 2023) (8-Ks 2025-10-07 and 2026-04-23). A director retired
  in March 2026 "not the result of any disagreement" (8-K 2026-03-12). Item 1A carries a risk factor on activist investors.

**Q6 (money and owners).** Buybacks: 1,706,625 shares for $50.4M in 2025 (about $29.5 a share) under a $300M programme
that names no price (10-K Item 7; none in the first half of 2026, 10-Q), where the rows note that announcements "almost never
refer to a price above which repurchases will be eschewed" **[L2016-002]**; the computed bottom below is negative, so the
prices paid sit above it (COMPUTATION). Pay: the 2025 annual incentive was "based 33.3% on each Company-wide measure of
Adjusted EBITDA and revenue and 33.4% on achieving certain" quality measures, and performance units vest on cumulative
Adjusted EBITDA and clinical metrics (DEF 14A); no capital charge was found in the pay sections read (searched for
"capital" in the pay discussion), against the rows' test of pay tied "to what is actually under the reasonable control of
the person that’s being measured" **[M2003-019]**. The new chief executive's 750,000-share first option tranche vests at
share prices of $25, $35 and $45 (8-K 2026-01-20). Say on pay, May 2026: 60,889,503 for, 19,942,924 against (8-K
2026-05-06). No dividend.

**Q7. COMPUTATION, NOT A CLEARANCE.** *(Built by Q7's range convention as if Q7 were reached; it clears nothing and carries
no entry language, operator rule 3. Script: `Test Runs/_research 2026-10-13 ACHC/scripts/compute.py`.)*
- **Basis.** All-equity central (owner cash before interest, interest paid added back after the 21% statutory rate,
  against market value plus net debt; "we evaluate acquisitions on an all-equity basis" **[L2017-004]**); equity-only beside. Net debt at June 30, 2026: face debt $2,429.6M
  (Term Loan A $625.6M, revolver $329.0M, notes $450.0M, $475.0M and $550.0M; 10-Q debt note) plus finance leases $11.8M,
  less cash $171.3M = **$2,270.1M**; operating leases ($143.1M at 2025) left out; redeemable minority interests of $191.6M
  are a further claim not deducted. Enterprise value at the price: $5,081.7M.
- **Window and cycle base, specific (a).** 2021 to 2025, the five years of the U.S.-only business after the January 2021
  U.K. sale. Not a cyclical business; the filer calls legal settlements "non-recurring", but they fall in three of the
  five years (charged 2023 and 2025, paid 2024 and 2025) with more open, so no year is treated as aberrational and the
  literal window is the base. Beside it: the same with the two settlement payments added back after tax.
- **Specific (e), maintenance central.** The filer gives the maintenance split each year, so the central case is owner
  cash after maintenance capex only. All-equity series: $367.3M, $337.3M, $389.1M, $75.2M, $90.4M; average **$251.9M**
  (equity-only $176.3M). All-spending series beside: $28.8M, $99.3M, $93.7M, -$554.3M, -$361.4M; average -$138.8M.
- **Growth shown, specific (b).** Owner cash fell: end years $367.3M to $90.4M, -29.6% a year (between halves, -38.3%).
  Revenue grew 9.4% a year, but the growth bought by $1.8bn of expansion spending did not appear in owner cash, so the
  maintenance no-growth case is the top and the shown decline the bottom (the inversion of specific (e)). The equity-only
  and all-spending series change sign, so each is the no-growth case alone, said so.
- **Specific (c).** Net purchases $210.5M over the window, under half of the maintenance-case owner cash before purchases
  ($881.5M, equity-only); against the all-spending owner cash before purchases, which is negative, the serial-acquirer
  test would be met trivially. Either way the central case already leaves purchases out (maintenance only), so the organic
  pair and the central case coincide; purchases are inside the all-spending case beside. No signed, unclosed deal found. **(d)** Working capital is inside
  operating cash. **(f)** No growth is credited, so the cap does not bind.
- **Tax.** The company's own cash tax is inside operating cash. State operating loss carryforwards of $671.0M, part
  expiring from 2028 (10-K tax note): at a state rate of about 5% (an assumption of this run, not a filed figure) the
  shelter is about $34M undiscounted, about $0.36 a share, not added; it does not change any line below.
- **Value range (central, all-equity, 93.10M shares):** **-$18.22 to $23.92 a share** against **$30.20** (top: $251.9M,
  no growth, at 5.60%: $4,497M less net debt; bottom: the same declining at 29.6% a year for ten years, then flat). At the
  balance-sheet count the top is $24.51. Beside: all-spending no-growth -$51.00; equity-only no-growth $33.82 (top and
  bottom alike); settlement payments added back, all-equity $40.52 (equity-only $50.41).
- **The floor first, then the width.** At $30.20 the central top case returns 4.96% on the enterprise value; the
  settlement-free case 6.66%; the equity-only cases 6.27% and 9.35%. No case earns the floor of about ten percent ("we don’t want to buy
  equities where our real expectancy is below 10 percent" **[M2003-149]**), so Q7 would close OUT whatever the width (the bottom is negative, so the width is beyond three to one,
  where "no useful conclusion can be reached" **[L2000-025]**). Nothing here does what the rows ask, "It should scream at you." **[M2009-005]**.
- **Fair price (Part VII; a reporting figure, never a verdict):** each end case valued at ten percent and averaged. Central,
  all-equity: top $2.67, bottom -$19.31, **fair price -$8.32 a share, not positive**. Equity-only beside: the no-growth case
  alone at ten percent, **$18.94**. Settlement payments added back (beside only): all-equity top $11.96, equity-only
  $28.23. Every figure is below the price.

**Q9 (debt and exposures).** Net leverage 4.1 times Adjusted EBITDA at June 30, 2026 under the credit agreement, whose
covenants require no more than 5.0 times and interest coverage of at least 3.0 times (8-K 2026-07-28 Ex. 99.1; 10-K
Item 1). Maturities: $450M of 5.5% notes in 2028, $475M of 5.0% notes in 2029, the term loan and revolver in February 2030,
$550M of 7.375% notes in 2033 (10-Q debt note). Pre-tax earnings over interest: 3.9 times in 2024; 0.6 times in 2025
without the goodwill impairment. A "large self-insured retention" and a captive insurer covering up to $10.0M a claim
(10-K Items 1A and 7). The parent is "a holding company with no operations" (Item 1A).

**Q12 (how the money is made).** None of the businesses the rows name (casinos, tobacco, distributor loading). The filer
states that "patient incidents, including deaths, sexual abuse, assaults and elopements, have occurred in the past and
could continue to occur" (10-K Item 1A); with the investigations above, these bear on the newspaper test, not weighed.

**Research pass:** none. The box is TOO HARD (NATURE), which takes no pass; and no case of the computed range earns the
floor at the price, so by Part VII no pass would be run in any case.

## REPORTING FIGURES (the owner's request; a reporting convention, not a rule; COMPUTATION, the file closed at Q1)
- **(a) VALUE RANGE:** -$18.22 to $23.92 a share (all-equity basis, central) against $30.20; equity-only $33.82
  (no-growth alone).
- **(b) FAIR PRICE:** -$8.32 a share on the all-equity basis (central; not positive); $18.94 on the equity-only basis
  (beside). Company's own tax, no conversion.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (906885d2); written section by section; committed after each closed part
      (Step 0 5a184a2e; Q1 1c793809; the rest in the closing commit).
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (not checked here, by
      the brief); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under CONTAMINATION below and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (check script in the research folder); every filing fact carries
      its document and accession; the numbers come from filings or are labelled as this run's assumption.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from
      the Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations; Q1); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year window and its yield lines were not.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the commit).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 and Q5 overlap on a pending investigation.** The deciding unknown here, a criminal investigation into whether the
core line's admissions and billing were lawful, is both an unforecastable economic variable (Q1, tests 4 and 5) and an
integrity question (Q5). The hard sequence sends it to Q1 and leaves the integrity record unjudged; the text gives no
routing for an investigation of the revenue itself. I closed at Q1 on the filer's own written refusals to estimate and
flagged the integrity facts. (2) **Q1 has no rule for a price set by government.** The bank door and the commodity
paragraph exist; a provider paid mostly by Medicaid at legislated rates has no paragraph, so I read it by tests 2, 4 and 5.
(3) **Specific (a) and "non-recurring".** The convention takes an aberrational year "on the filer's own description", but
this filer calls legal settlements non-recurring while they recur in three of five years; I kept them in, against the
filer's word, on the ground of "wave away very real costs" **[L2016-006]**, and showed the alternative beside. The text should say which wins. (4) **A
negative fair price.** Part VII defines the fair price as the average of the two end cases at ten percent; with the shown
decline as the bottom the central figure is negative, and the text says what to do only for the acquisition case (the
organic pair). I reported the negative figure and the equity-only figure beside. (5) **The equity-only figure can exceed
the central one in an odd way:** because the equity-only series changes sign, specific (b) makes it the no-growth case
alone, which yields a higher equity-only fair price ($18.94) than the all-equity one (-$8.32); the two bases are then not
computed on the same growth rule. (6) **Share count:** the cover count exceeds the balance-sheet issued and outstanding
count by about 2.2 million shares on two consecutive filings, with no explanation found; the brief's check (issued less
treasury) does not say which to use; I used the larger. (7) **The serial-acquirer test's denominator** ("owner cash before purchases") is not said to be the maintenance or the
all-spending figure; for a heavy builder the second is negative and makes any purchase "serial". I used the maintenance
figure and said so.

## CONTAMINATION
Seen by accident, not used: the session context's project map and a memory index line on the queue's state (wave and
gate-clearer counts, not this name); the starting git status, which lists other runs' research folder names (AYI, ARCB)
and recent commit subjects naming other tickers (BAC, MTW); and one count of the entries in `Test Runs/` (`ls | grep -c`,
1,195 entries, no names displayed), made before the blind rule was applied to my own commands; it should not have been run.
Nothing seen concerns ACHC or any former name of it.
