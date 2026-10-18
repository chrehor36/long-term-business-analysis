# Company Run — Galaxy Entertainment Group Limited (HKEX: 0027; US OTC ADR: GXYYY) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template at the start of the run, before any fetch; first commit cd3af4fb.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for GXYYY, 0027 or Galaxy).

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md` with three stated departures: the lines of
evidence are derived by the analyst from the 2025 Annual Report; the company is not an SEC registrant, so its own annual
and interim reports are the primary documents (document and date recorded in place of an accession); the rivals for Q2 come
from the company's own reports, or, where those name none, are chosen by the analyst and confessed.

**Contamination declared.** Before any fetch the analyst saw, without opening them: the subjects of the five most recent
commits on the branch (all about another company's run and its fold, none about this company), and the memory index lines
loaded into the session (none names this company). Nothing of them is used. No other run file, holding review,
`PORTFOLIO.md`, queue or reading list was opened, listed or searched.

**Research folder:** `Test Runs/_research 2026-10-14 GXYYY/` (notes, scripts, statement extracts; the report PDFs and
full-text dumps sit in its ignored `cache/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HK$33.06 a share, close 2026-10-14 on the Hong Kong Stock Exchange (stock code 0027); the ADR GXYYY last
  closed at US$20.80 (2026-10-13, US OTC). Both from an aggregator (Yahoo Finance chart API), **flagged per operator rule 5**:
  live quotes only. At five shares per ADS the share price is HK$165.30 per ADS.
- **ADR ratio:** each American Depositary Share represents **five ordinary shares**, read from the depositary's registration
  on EDGAR: Form F-6EF filed 2022-04-05, accession `0001193805-22-000585` (CIK 1679056, "Galaxy Entertainment Group
  Limited/ADR"; the earlier F-6EF of 2016-07-07, accession `0001193805-16-003572`, is the only other filing listed).
- **Shares:** **4,379,240,712** ordinary shares, one class, read three ways: (1) 2026 Interim Report (posted 2026-09-16),
  note 18, "At 30 June 2026 4,379,240,712"; (2) the same figure in the 2025 Annual Report (posted 2026-04-09), note 27, at 31
  December 2025; (3) the HKEX Monthly Return of Equity Issuer for the month ended 30 September 2026 (company announcement of
  2026-10-07): balance at close of the month 4,379,240,712, no increase or decrease, no treasury shares. The share-award
  trustee holds 378,234 of these for unvested awards (interim note 18); they are counted as issued, as the filer counts
  them. Unvested share awards of 14,952,477 and share options outstanding (2,074,333 under one scheme on the monthly return)
  are dilution not yet in the count, about 0.4%, carried in Q6.
- **Market cap:** HK$33.06 x 4,379.24m = **HK$144,778m** (US$ at the ADR: 20.80 / 5 x 4,379.24m = US$18,219m).
- **`python tools/run.py GXYYY`:** "GXYYY: not an SEC filer ... UNRESEARCHED, not UNKNOWABLE." **`python Screens/cover_shares.py
  GXYYY`:** "NOT AN SEC REGISTRANT in the live ticker file." Both returned nothing; every figure below is taken by hand from
  the reports.
- **Earnings currency:** the Hong Kong dollar. The 2025 Annual Report's MD&A: "(All amounts are expressed in Hong Kong dollars
  unless otherwise stated)". The gaming business earns in Macau patacas (the concession's capital and investment terms are
  stated in MOP; the treasury policy places surplus cash in "Hong Kong dollar, Macau Patacas, U.S. dollar, Renminbi");
  the construction materials division earns partly in renminbi. No pataca or renminbi conversion is made; figures are
  as the filer states them in HK$.
- **Sovereign for the earnings currency:** **4.597%**, the closing reference yield of the 20-year HKSAR Institutional
  Government Bond (issue 20GB4503001, 3.99% coupon, maturing 2045-03-06) on **2026-10-13**, from the HKSAR Government Bond
  Programme's own file `HKD_DailyClosingReferencePricings_IBPandGSBP.xls` (hkgb.gov.hk, the Government's programme
  administered by the HKMA; the file states its prices are "powered by Bloomberg"); the same file's row for 2026-10-14
  also reads 4.597%. **CONVENTION of this run:** the issuer publishes no 30-year yield; the longest published tenor, 20
  years, is taken as the long government rate. Rationale: the brief's instruction for an issuer without a 30-year bond, and
  the 20-year is the longest rate the issuing authority itself quotes. (The HKMA's own API for the same series returned
  blank fields for recent dates and then refused further requests; the Government Bond Programme file was used instead.)
- **Filings read** (operator rule 4; dates in place of accessions, departure (2)): 2025 Annual Report (posted 2026-04-09;
  Chairman's Statement dated 26 February 2026) in full in its business, Chairman's Statement, MD&A, directors' report,
  remuneration, statements and notes 2, 6, 8, 12, 27, 33; 2026 Interim Report (posted 2026-09-16; approved 12 August 2026)
  statements and notes 18 and the substantial holders; Annual Reports 2015 to 2024 (posted 2016-03-23, 2017-03-24,
  2018-03-23, 2019-03-28, 2020-03-30, 2021-03-29, 2022-03-28, 2023-04-19, 2024-04-10, 2025-04-10), their primary
  statements, cash-flow reconciliation notes, tax notes and segment notes; the 2025 Interim Report (2025-09-10) was
  downloaded and not needed; announcements: Monthly Return for September 2026 (2026-10-07), Declaration of Interim
  Dividend (2026-08-12). All from https://www.galaxyentertainment.com/en/investor/financial-reports and its announcements
  page (PDFs under /uploads/investor/).
- **One figure cross-checked against the filed statement:** revenue for 2025, HK$49,242,325 thousand in the consolidated
  income statement (2025 AR p.78), agrees with the MD&A's "Net Revenue of $49.2 billion" and with the Five-Year Summary
  (p.72) "49,242,325". Net cash at 31 December 2025, HK$13,015,676 thousand in note 5's gearing table, agrees with cash and
  bank balances 14,309,798 less borrowings 1,294,122 on the balance sheet.
- **The lines of evidence chosen (departure (1)),** from the 2025 AR's business sections, Chairman's Statement, MD&A, the
  "principal risks and uncertainties" pointer in the directors' report, and the segment note: (1) the Macau gaming
  concession, its term, the reversion of the casinos and the investment commitment (note 2); (2) Macau's gross gaming
  revenue and visitation, and the central government's travel policy, which the Chairman names as the driver; (3) Galaxy's
  share of Macau GGR and its mass, premium-mass and VIP mix, and the "luck" adjustment; (4) the two segments, gaming and
  entertainment against construction materials (note 8); (5) capital spending: Phase 3, Phase 4 (targeted 2027) and the
  StarWorld renovation; (6) the Macau complementary-tax exemption and the dividend-tax agreement (note 12); (7) the
  treasury: listed debt securities, the Wynn Resorts stake (cost HK$7,142m, value HK$4,869m) and the Monaco (SBM)
  investment; (8) pay, share options and share awards, the board and the controlling family. The directors' report sends
  the reader for "principal risks and uncertainties" to the Chairman's Statement (pp.10 to 12) and the MD&A (pp.24 to 32);
  those pages name no risk by that word beyond monitoring "the global economic environment and geopolitical developments"
  and a market that "will remain highly competitive, especially in the premium mass segment". That thinness is itself
  recorded (Q5, Q6 facts).
- `tools/run.py` arithmetic lines: none (not an SEC filer). Owner cash is built by hand in the COMPUTATION below, from the
  cash-flow statements and their reconciliation notes, 2015 to 2025, and the 2026 interim.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be happy to own this "if the market closed for five years" **[M1997-109]**; the question
the market cannot answer for this name is what the business will be in the years the quote is shut, which is Q1's
question. The market serves and does not instruct **[M2006-077]**: the price is read only against the value at Q7. Margin of
safety **[M1996-084]**: carried to Q7. No macro forecast enters **[M2000-094]**: the speakers ignore "political and economic
forecasts" **[L1994-004]** and decide on "the average profitability of the business over time and how strong its competitive
mode is" **[M2015-016]**. This foundation is the strongest pull against the box below, and the run must say why it does not
govern: the concession and its terms are not a forecast about the economy at large but the legal term of this business's
right to operate, written in its own contract, and the closures of 2020 to 2022 and the rewritten law of 2022 were decisions
about this industry alone. Who is paid to tell you: the filer's own forward statements ("We remain highly confident about
the future of Macau") are a seller's projection, read as such.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The speakers once overrated regulatory risk to a licensed business and paid for it: "we tended to overestimate the
   difficulties from regulation. We refrained from buying television station stocks for a long, long time because it
   seemed like such a peculiar asset when anybody could just ask to have your license jerked away from you each year [...]
   but it turned out, the way the system evolved, that almost never happened." **[M2004-058]**. The one retender Macau has
   held (2022) renewed all six incumbents, Galaxy among them (2025 AR note 2).
2. "We will continue to ignore political and economic forecasts" **[L1994-004]**, and the speakers went into China asking
   "to get paid more", not passing **[M2006-021]**.
3. Galaxy's balance sheet is net cash (HK$13.0bn of cash net of borrowings, HK$36.3bn of "cash and liquid investments"
   on the filer's measure, 2025 AR MD&A), so no closure has threatened its survival: it came through three years of
   losses (2020 to 2022) paying no dividend in 2021 and borrowing nothing that mattered.
4. Visitation set a record in 2025 (40.1 million, MD&A), and the central government widened visa access for Zhuhai and
   Hengqin residents (Chairman's Statement): the policy variable has lately moved in the business's favour.

## THE STANDING RULE
A purchase of quoted shares, unleveraged and sized by the buyer, cannot ruin the buyer: "We are never going to risk what we
have and need for what we don’t have and don’t need." **[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**.
Nothing in this name obliges the buyer to borrow or to post collateral; the rule binds only how a purchase would be financed
and sized **[M2004-065]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**What the business is, from the filings.** Gaming and entertainment carried 90% of five-year adjusted EBITDA (the filer's
measure, used here only to size the parts: HK$36.3bn of HK$40.3bn, 2021 to 2025, segment notes; construction materials
HK$4.0bn). Galaxy Casino, S.A. operates three casino resorts under a Macau gaming concession; it pays 35% gaming tax plus
5% contributions on net gaming win (note 4.22), commissions and incentives (HK$9.5bn on HK$49.1bn of gross gaming revenue
in 2025), and keeps the rest less its costs. The mechanics are plain; the reports are readable from the figures
**[M2008-069]**, **[M2005-015]**. The holding company is read by its parts (Q1's holding-company paragraph, the parts
threshold): the gaming part decides; the construction-materials part does not.

**The key variables and how predictable they are** **[M1998-044]**:
1. **The right to operate after 2032.** "On 16 December 2022, the Macau Government and GCSA entered into a new gaming
   concession contract [...] for a term of 10 years, from 1 January 2023 to 31 December 2032." (2025 AR note 2.) On 30
   December 2022 Galaxy signed contracts by which "The casino areas of Galaxy Macau, StarWorld and Broadway held by
   subsidiaries of GEG, together with the revertible gaming assets held by GCSA are to be reverted to the Macau Government
   without compensation", handed back "for its continuing use in gaming operations during the 10-year term". The filer
   carries the assets on "the assumption of the subsequent successful retention and tendering of the gaming concession"
   and "believes that it will be successful in subsequent retention and tendering" (notes 2 and 6(b)); its auditor names
   "successful retention of the gaming concession in future years" as a key assumption of the HK$71.2bn impairment test
   (note 6(a); key audit matter). The end of the concession falls inside the ten-year horizon of the question, and the
   casinos already belong to the grantor. What the business is in 2036 turns on a tender the grantor has not designed yet.
2. **Macau's gaming revenue**, which the filer ties to the central government's travel policy (Chairman's Statement
   2025). Macau GGR, as the filer reports it from the DICJ, in HK$bn: 2016 216.7; 2018 294.0; 2019 283.9; 2020 58.7;
   2021 84.3; 2022 41.0; 2023 177.7; 2024 220.2; 2025 240.2, "85% of 2019 level" (AR MD&A each year). Galaxy's own GGR on
   a management basis: 2016 49.5; 2017 58.0; 2018 67.2; 2019 59.4; 2020 11.5; 2021 17.3; 2022 7.5; 2023 31.7; 2024 41.1;
   2025 49.1. Two collapses in ten years, each set by policy rather than by the customer: 2015, when "a Government led
   anti-corruption programme" weighed and "Total gaming revenue decreased by 34% year-on-year to HK$224 billion" (2015 AR
   MD&A; Galaxy's adjusted EBITDA fell from HK$13.2bn to HK$8.7bn, 2015 AR highlights), and three years of closures and
   travel restrictions, 2020 to 2022, in which Galaxy lost money at the pre-tax line in 2020 and 2022.
3. **The rules of the game**, rewritten by the 2022 law and contract: casinos reverted, MOP33.75bn of committed
   investment over the term, MOP32.85bn of it non-gaming (note 2), a MOP5.0bn capital floor (note 5), the satellite "City
   Club" casinos wound down (Waldo ceased operations on 31 October 2025, MD&A), and the VIP promoter trade shrunk (the
   2015 AR records "a reduction in the number of junkets operating within Macau" and a 45% fall in market VIP revenue;
   Galaxy's commission and allowances to gaming counterparties were HK$22.2bn in 2014, 2015 AR income-statement note).
4. **The tax.** The Macau complementary-tax exemption on gaming profits runs "for five years effective from the 2023 year
   of assessment till year 2027" (note 12(a)); the dividend-tax agreement ran to 31 December 2025 and an extension was
   applied for in February 2026 (note 12(a)). Both have been renewed before (2014 to 2018, 2019 to June 2022, June to
   December 2022, 2023 to 2027: tax notes 2016 to 2025), each by a decision of the Chief Executive.

**The tests.**
- *Where will it be in ten years?* **[M2000-037]**: "a reasonable probability of being able to asses where the business will
  be in 10 years". In ten years Galaxy either holds a re-tendered concession on terms not yet written, or holds hotels,
  a mall and arenas around casinos that belong to the Macau Government. The filer's belief is stated; no filing states
  the terms, the number of concessions, the tax or the investment that a 2032 to 2035 tender will set.
- *Important and knowable?* "If something’s important but unknowable, forget it." **[M2006-076]**. The concession
  outcome is the most important variable in the valuation and is not knowable from any document.
- *Would the insiders write it down?* **[M2000-105]**. The filer's own forward statement is confidence, not a forecast of
  economics ("We remain highly confident about the future of Macau", MD&A 2025); its principal-risks disclosure names
  no risk to the concession at all. The 2013 insiders did not foresee the 34% fall of 2015, and the 2019 insiders did not
  foresee three closed years. The question that decides the ten-year economics is a decision of two governments.
- *How the industry will develop and where the company will stand within it* **[M2012-065]**: the second half is
  readable (Galaxy's share of Macau GGR held near a fifth, 22.8% in 2016 and 20.4% in 2025 on the figures above, dipping
  to 17.8% in 2023); the first half is the grantor's.
- *Abroad: the governance and the tax* **[M2000-141]**: the corporate governance (a Hong Kong company, a controlling
  family trust holding 35.37%, interim report) can be read; the gaming regime's next terms cannot.
- *How far off could I be?* **[M2011-084]**: on the evidence of 2020 to 2022, by the whole of the earnings for years at a
  time, for reasons outside the business.
- *Do I doubt it is inside?* "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**.

**Against the box, weighed.** The television licences **[M2004-058]** were renewed under a system whose rules did not
change against the holder; Macau's one retender renewed the holders but changed the rules against them (reversion without
compensation, a committed MOP33.75bn, the satellite casinos and the promoter channel closed). The row is about one industry
and is weighed, never a verdict alone (Q2, A row about one company). China was entered at a higher price **[M2006-021]**
because the business was understood; here the business's own term ends inside the horizon, which no price discount
answers: a wide uncertainty is not "compensated" by "some extra large margin of safety" **[M2007-022]**. The macro
foundation **[L1994-004]**, **[M2015-016]** is answered above: the term of the licence is the business's own fact, not a
forecast of the economy.

**Routing.** The deciding question is not a matter of fast technology, so it is not the routing paragraph's case; it is
test 4 and test 5 of Q1: "where the business will be in 10 years" **[M2000-037]** turns on an important variable that is
unknowable **[M2006-076]** and that the insiders would not write down **[M2000-105]**. Study does not cure it: the
deciding fact is a future tender whose terms do not exist, "We couldn't solve this problem, moreover, even if we were to
spend years intensely studying those industries." **[L1993-023]**. The cause is therefore NATURE, not WORK: no filing not
yet read would answer it.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**, **[M2000-038]**: "It doesn’t mean it isn’t a good buy. It doesn’t mean
  it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." Filing facts: the
  concession ends 31 December 2032 and the casino areas have reverted to the Macau Government without compensation (2025
  AR note 2); Macau GGR fell from HK$283.9bn (2019) to HK$41.0bn (2022) on policy (AR MD&A 2019, 2022). The file closes
  here. Q2 to Q12 are NOT REACHED; the facts already found for them are under AFTER THE STOP, and the owner's two reporting
  figures are computed under COMPUTATION, NOT A CLEARANCE.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed TOO HARD (NATURE)). Facts under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0's spirit (template: read them in Step 0 if the file closes before Q4);
the reading is under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Facts under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year economics turn on the Macau gaming concession, which ends on 31
December 2032 with the casino areas already reverted to the Macau Government without compensation, and on travel and
gaming policy that twice in ten years cut Macau's gaming revenue by a third or more; neither is a forecast the industry's
insiders would write down **[M2000-105]**, **[M2006-076]**. Integrity facts recorded, not judged (the featured adjusted
EBITDA that excludes stock pay; Q4 and Q5 below). COMPUTATION, NOT A CLEARANCE: value range HK$41.75 to 54.08 a share at
the 4.597% HKSAR 20-year rate against HK$33.06; no case earns the ten percent floor at the price; fair price HK$26.86 a
share (HK$134.31 per ADS) all-equity, HK$20.89 (HK$104.43 per ADS) equity-only. A lower price does not reopen a NATURE box
**[M2000-038]**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box is unchanged (operator rule 2). Each with its source **[M1997-127]**.)*

**Q2, the castle.**
- *The barrier is a licence.* Six concessions; the 2022 contracts run 2023 to 2032 for every holder read (2025 AR note 2;
  the rivals' filings, `competitors_extract.md`). No newcomer can buy its way in while the licences stand (the money test
  **[M2011-015]**); how permanent the castle is **[M1995-038]** is the grantor's to decide. Before 2023 the Sands
  operation held a subconcession granted through Galaxy's concession (LVS 10-K FY2016, as extracted).
- *The rivals.* **CONVENTION of this run:** the reports name no rival company (a search of the 2016 to 2025 reports for
  the rivals' names found only Wynn Resorts, as an investment), so three concessionaires' SEC-filing parents were chosen:
  Las Vegas Sands (Macao segment), Wynn Resorts (Macau Operations), Melco Resorts & Entertainment (Macau properties). MGM
  China (inside MGM Resorts' 10-K) was not read; SJM Holdings does not file with the SEC. Rationale: the brief's
  instruction where the reports name no rival; these three file Macau-only segment figures. Adjusted property EBITDA over
  net revenue, the filers' own measure (each excludes stock pay and corporate cost), US$m, from the LVS 10-Ks (accessions
  0001300514-17-000005, 0001300514-20-000011, 0001300514-23-000021, 0001300514-26-000013), the Wynn 10-Ks
  (0001174922-17-000027, 0001174922-20-000024, 0001174922-23-000048, 0001174922-26-000013) and the Melco 20-Fs
  (0001193125-20-091982, 0001193125-23-086859, 0001193125-26-105023); 2016 on the pre-ASC 606 basis; extraction in
  `competitors_extract.md`:

  | Year | LVS Macao rev / EBITDA / % | Wynn Macau rev / EBITDA / % | Melco Macau rev / EBITDA / % | Galaxy gaming segment adj. EBITDA, HK$m |
  |---|---|---|---|---|
  | 2016 | 6,732 / 2,244 / 33.3 | 2,847 / 785 / 27.6 | not read | group 10,300 (2016 AR highlights) |
  | 2017 | 7,609 / 2,607 / 34.3 | 4,367 / 1,288 / 29.5 | 4,597 / 1,188 / 25.8 | 13,554 |
  | 2018 | 8,689 / 3,079 / 35.4 | 5,052 / 1,577 / 31.2 | 4,497 / 1,209 / 26.9 | 16,111 |
  | 2019 | 8,834 / 3,189 / 36.1 | 4,614 / 1,378 / 29.9 | 4,988 / 1,413 / 28.3 | 15,497 |
  | 2020 | 1,707 / (431) | 980 / (237) | 1,426 / (136) | (1,993) |
  | 2021 | 2,897 / 338 / 11.7 | 1,509 / 96 / 6.4 | 1,660 / 145 / 8.7 | 2,694 |
  | 2022 | 1,627 / (324) | 722 / (221) | 845 / (170) | (1,001) |
  | 2023 | 6,559 / 2,224 / 33.9 | 3,100 / 954 / 30.8 | 3,117 / 809 / 26.0 | 9,417 |
  | 2024 | 7,107 / 2,327 / 32.7 | 3,682 / 1,176 / 31.9 | 3,920 / 988 / 25.2 | 11,462 |
  | 2025 | 7,470 / 2,310 / 30.9 | 3,718 / 1,085 / 29.2 | 4,429 / 1,234 / 27.9 | 13,758 (of which about 1,482 luck) |

  Galaxy's segment figures are from the segment notes of the 2017 to 2025 annual reports. Galaxy Macau's own adjusted
  EBITDA margin was 31% (2024) and 33% (2025) (2025 AR MD&A). From 2019 to 2025 the three rivals' Macau EBITDA fell 28%,
  21% and 13%; Galaxy's gaming segment fell 11% as reported and about 21% after the luck the MD&A states. The whole field
  lost money in 2020 and 2022: the closures were the market's, not one castle's. Pre-tax EBITDA on long-lived Macau
  assets in 2025: LVS 2,310 on 7,944 (29%), Wynn 1,085 on 3,041 (36%), Melco 1,234 on 5,224 (24%); Galaxy's gaming segment
  13,758 on PPE plus right-of-use assets of HK$54,846m for the whole group (25%). In words: good returns in the years the
  market is open, losses in the closed years, for every operator alike.
- *Share of the market* (Galaxy GGR over Macau GGR, figures in Q1): 22.8% (2016), 22.5% (2017), 22.9% (2018), 20.9%
  (2019), 19.6% (2020), 20.5% (2021), 18.3% (2022), 17.8% (2023), 18.7% (2024), 20.4% (2025). Narrowed 2018 to 2023,
  partly recovered since, with VIP win up 79% in 2025 and a lucky hold.
- *Widening or narrowing* **[M2000-075]**: the 2022 contract took the casinos' ownership, added the investment commitment
  and wound down the City Clubs; Waldo closed on 31 October 2025. The MD&A says the market "will remain highly
  competitive, especially in the premium mass segment".
- *Parts:* gaming and entertainment 90% of five-year adjusted EBITDA; construction materials 10% (2021 to 2025, segment
  notes). For construction materials the 2025 MD&A expects oversupply in Mainland China to "persist" and Hong Kong demand
  to "continue to drop".

**Q3, the capital.** Capital spending 2015 to 2025, HK$m (PPE, land and intangibles): 6,594; 2,128; 2,022; 3,033; 4,172;
5,797; 6,931; 5,077; 6,018; 4,868; 3,482 (cash-flow statements). Depreciation and amortisation: 3,086; 3,573; 3,349;
3,316; 3,457; 2,817; 2,264; 2,088; 2,836; 3,561; 3,794. In 2016 to 2018 spending ran below depreciation; from 2020 to 2024
it ran far above it (Phase 3, Capella, Phase 4 targeted for 2027, the StarWorld renovation); capital commitments
contracted but not provided for were HK$11.2bn at the end of 2025 (note 35). PPE plus right-of-use assets went from
HK$37.7bn (2019) to HK$54.8bn (2025) while gaming-segment adjusted EBITDA went from HK$15.5bn to HK$13.8bn; whether the
growth spending earns its cost is unproven on the record to date, "whether that’s good or bad depends on what we earn on
that incremental $130 million over time" **[M2001-019]**. The MOP33.75bn investment commitment (MOP32.85bn non-gaming) is
spending the concession requires (note 2).

**Q4, the accounts (the balance sheets first, 2015 to 2025)**, "balance sheets over an 8 or 10 year period" **[M2025-032]**.
Equity attributable to owners, HK$bn: 41.1 (2015), 46.3, 55.5, 62.3, 73.6 (2019), 67.4, 68.4, 63.9 (2022), 70.8, 75.9,
83.1 (2025): the closures cost about HK$9.7bn of equity from 2019 to 2022, recovered by 2024. Intangibles stayed small
(HK$0.15bn to HK$2.5bn; the 2023 rise is the concession premium, booked as an intangible with its payable). Cash, deposits
and securities: about HK$46bn at the end of 2019 (14.6 cash, 25.2 at amortised cost, 6.3 at fair value), about HK$25bn at
the end of 2022 (14.0, 6.7, 4.2), about HK$37bn at the end of 2025 (14.3, 17.1, 6.0). Borrowings peaked at HK$9.9bn (2017,
mostly short-term) and were HK$1.3bn at the end of 2025. Creditors and accruals swung from HK$20.0bn (2019) to HK$8.3bn
(2021), the working-capital unwind behind the negative cash from operations in 2021 and 2022. Depreciation is charged in
full; the tax line is small because gaming profit is exempt from Macau complementary tax to 2027 (note 12). **Weighs
against, carried to Q5:** the featured figure is "Adjusted EBITDA", whose basis "excludes the [...] share option expenses
and share award expenses" (2025 AR note 8; the 2016 and 2021 notes say the same), and which leads the Chairman's Statement
**[L2016-006]**, **[L2015-003]**. Beside it, the MD&A reports a "Normalized" figure that removes luck in both directions
(2024: HK$(157)m; 2025: HK$1,482m), and net profit is stated in the same paragraph. No confusion was met and no tell of the
kind that lives in the accounts (reserves that move, prepaid accounts building).

**Q5, the people.** A controlling family: the trust of the late Dr. Lui Che Woo (died 7 November 2024, 2025 AR note
10(a)(v)) and related holders, 35.37% (2026 interim, substantial holders). The Chairman, Francis Lui Yiu Tung, aged 70,
joined in 1979; Paddy Tang Lui Wai Yu and, from 9 May 2025, Eileen Lui Wai Ling are executive directors. His 2025 pay was
HK$82.2m, of which HK$48.5m is the charge for share options and awards; executive directors together HK$106.7m (note
10(a)). In 2024 he and Dr. Lui waived 50% of their bonuses (note 10(a)(vii)). The principal-risks disclosure is a pointer
to the Chairman's Statement and MD&A, which name no risk to the concession. Integrity facts recorded, not judged: the
featured adjusted figure that leaves out stock pay (Q4 above). No other tell was met in the pages read.

**Q6, the money and the owners.**
- *Retention:* 2021 to 2025 profit attributable HK$24,153m less dividends HK$10,925m = HK$13,228m retained (Five-Year
  Summary, 2025 AR). Share price HK$58.80 at the end of 2020 and HK$33.06 now (aggregator, flagged); net assets per share
  HK$15.70 (2021) and HK$18.99 (2025). The test is market value per dollar retained over a five-year span **[R1995-009]**,
  **[M1998-110]**.
- *Buybacks:* none were made; the share count has risen through option exercises and award issues (to 4,379,240,712).
  Buyback line from Q7: not applicable.
- *Surplus cash:* 5.2 million Wynn Resorts shares at a cost of HK$7,142m, worth HK$4,869m at the end of 2025 (MD&A); a
  euro-funded stake in SBM Monaco (August 2015, MD&A treasury policy); HK$17.1bn of listed debt securities. The filer
  will "actively pursue international development opportunities" (MD&A 2025).
- *Dividends:* HK$1.20 paid in 2025, HK$1.50 declared for 2025, HK$0.90 interim for 2026 (announcement 2026-08-12).
- *Pay:* options are struck at the closing price on the grant date or the five-day average (share option scheme, 2025 AR
  report of the directors), with no step-up for retained earnings **[M1997-043]**; the speakers ask that "the base price
  should be what the business is worth" **[M2011-067]**. Options outstanding carry exercise prices from HK$34.08 to
  HK$62.19 (note 28).
- No all-stock deal was found in 2015 to 2025; the narrower Q6 STOP is not engaged.

**Q9, debt and exposures.** Net cash (HK$33.5bn on the measure below). Guarantees for subsidiaries' bank facilities
HK$4.0bn (HK$0.87bn drawn); a MOP1bn bank guarantee in favour of the Macau Government for the concession (note 39); the
concession payable of about HK$2.1bn; the MOP33.75bn investment commitment through 2032. One jurisdiction, one regulator,
one licence: every operating dollar of the gaming part depends on the same grantor. Pillar Two applies from 2025; the
filer assesses no top-up tax (note 12(b)).

**Q12, how the money is made.** Casinos are a business the rows name: "It’s a dirty business, and I don’t think you’ll
find a casino soon in Berkshire Hathaway." **[M2007-018]**. The framework makes this a STOP when the whole is bought and run
and a WEIGHING for a marketable stake **[M2005-096]**, **[M2004-075]**. A run that reached Q12 would weigh it against;
the operator chooses whether Q12 is asked.

## COMPUTATION, NOT A CLEARANCE
*(Q1 closed the file; nothing below is a clearance, and no entry language attaches to any figure (operator rule 3).
Scripts: `Test Runs/_research 2026-10-14 GXYYY/scripts/q7.py` and `scripts/owner_cash.py`.)*

**Owner cash, HK$m, after every real cost, before interest, after the company's own tax:** cash generated from operations
(which already excludes interest income and listed dividends and includes working-capital changes); less income tax paid;
less stock pay, which the reconciliation adds back; less capital spending (PPE, leasehold land, intangibles) net of
disposal proceeds, or depreciation in the maintenance case; less lease payments and, from 2023, the concession payments;
plus dividends received from joint ventures and associates (the equity-method convention).

| Year | All spending, tax as paid | Maintenance (D&A) case, tax as paid | Exemption value (12%) | Maintenance case, statutory tax | Net acquisitions |
|---|---|---|---|---|---|
| 2015 | (237) | 3,270 | 1,066 | 2,204 | 650 |
| 2016 | 10,309 | 8,865 | 1,167 | 7,697 | 0 |
| 2017 | 16,323 | 14,997 | 1,572 | 13,424 | 0 |
| 2018 | 10,919 | 10,636 | 1,843 | 8,792 | 0 |
| 2019 | 15,375 | 16,090 | 1,809 | 14,281 | 0 |
| 2020 | (13,274) | (10,294) | 0 | (10,294) | 0 |
| 2021 | (10,214) | (5,547) | 333 | (5,880) | 0 |
| 2022 | (7,874) | (4,885) | 0 | (4,885) | 0 |
| 2023 | 5,144 | 8,327 | 1,065 | 7,262 | 850 |
| 2024 | 6,125 | 7,433 | 1,331 | 6,102 | (27) |
| 2025 | 10,212 | 9,900 | 1,583 | 8,317 | (1) |

First half of 2026, as paid, all spending: about HK$4.4bn (interim cash-flow statement), against about HK$4.1bn in the
first half of 2025.

**Choices, each under Q7's text.**
- *Whose tax:* gaming profit is exempt from the 12% Macau complementary tax "till year 2027" (note 12(a)), a shelter that
  runs out inside ten years; the central case is at the statutory rate (the exemption's tax value as the filer's own tax
  reconciliation states it, "Profit exempted from Macau Complementary Tax"), with the present value of the 2026 and 2027
  exemption at the 2025 level, HK$2,960m at 4.597%, added. The exemption has been renewed at each expiry since at least
  2014 (tax notes); the convention does not credit renewal. The as-paid case is shown beside.
- *(e) Maintenance case central:* the filer states no maintenance figure; depreciation is the guess, "not inappropriate in
  most companies to use as a proxy for required capital expenditures" **[M1998-127]**; in 2016 to 2018 actual spending ran
  below it. All-spending case beside.
- *(a) Cycle base:* the literal window 2021 to 2025 opens with two closure years the filer describes as such
  **[L2005-003]**; its average is HK$2,019m (maintenance, statutory) or HK$(348)m (all spending, statutory), shown and not
  used. The last full cycle of owner cash runs from the 2015 trough through the 2019 peak to the 2020 trough; the base is
  the 2015 to 2019 average. Growth is measured from that average (midpoint 2017) to the average of the three years since
  reopening, 2023 to 2025 (midpoint 2024), seven years apart: an incomplete second cycle, the only one there is.
- *(c) Acquisitions:* net purchases of HK$650m (2015) and HK$850m (2023, a joint-venture stake net of a disposal) are
  deducted (default pair); small against owner cash, so not a serial acquirer; they stop after year ten.
- *(b) Decline:* the growth shown is negative and is carried as the bottom; no growth is the top.
- *(d) Working capital:* inside cash generated from operations. *(f) Cap:* not engaged (negative growth).
- *Net cash at 30 June 2026 (On what the floor is earned):* cash and bank deposits 15,704 + listed debt securities at
  amortised cost 18,080 + financial assets at fair value, chiefly the Wynn shares, 5,467 - borrowings 1,831 - the interim
  dividend of HK$0.90 a share paid after that date (HK$3,941m, declared in the interim report) = **HK$33,478m**; less
  non-controlling interests at book, HK$465m. Lease liabilities (HK$639m) and the concession payable (about HK$2.1bn) are
  left out because their payments are charged inside owner cash; said so.

**The range (all-equity, per share, at 4.597%):**

| Case | Base, HK$m | Growth carried | Range a share | Fair price a share (each end at 10%, averaged) |
|---|---|---|---|---|
| **Central: maintenance, statutory tax, acquisitions deducted** | **9,150** | **-3.85% a year** | **HK$41.75 to 54.08** | **HK$26.86 (HK$134.31 per ADS)** |
| All spending, statutory tax | 8,916 | -6.52% | HK$34.57 to 52.92 | HK$25.14 |
| Maintenance, tax as paid | 10,642 | -3.52% | HK$47.51 to 60.81 | HK$29.41 |
| All spending, tax as paid | 10,408 | -5.73% | HK$40.26 to 59.65 | HK$27.68 |

Equity-only figure beside the central (owner cash after interest paid, with the interest and listed dividends actually
received, base HK$9,671m, valued at the floor with no balance-sheet addition): **HK$20.89 a share (HK$104.43 per ADS)**.

**The floor, tested first.** At HK$33.06 the all-equity value paid for the business is HK$111,765m (market value
HK$144,778m less net cash plus minorities). The best case of the central range, no growth on HK$9,150m (HK$9,280m once
purchases stop), returns about 8.2% on it; every other central case returns less; the most generous variant (maintenance,
tax as paid) returns 9.5%. **No case earns the floor of about ten percent at the price** **[M2003-149]**: had Q1 passed,
Q7 would close OUT at HK$33.06 whatever the width (the width is 1.30 to 1, inside three to one). The range at the long
rate lies above the price only because the 20-year HKSAR rate (4.597%) is far below the floor.

**What the convention assumes and this business does not have.** Q7's construction carries the cash for ten years and then
forever. The concession ends in 2032. On the central base and decline with the cash stopping at the end of 2032 and nothing
after (no renewal, nothing for the hotels without casinos), the figure is about HK$18.81 a share including net cash: shown
beside to measure what the renewal assumption carries, not a reporting figure.

**Reporting figures (Part VII, The owner's price; a reporting convention, not a rule; labelled COMPUTATION):**
(a) VALUE RANGE: **HK$41.75 to HK$54.08 a share; HK$208.75 to HK$270.40 per ADS**, against HK$33.06 (HK$165.30 per ADS).
(b) FAIR PRICE: **HK$26.86 a share, HK$134.31 per ADS** (all-equity, central); equity-only **HK$20.89 a share, HK$104.43
per ADS** beside. Tax: the company's own, at the statutory Macau complementary-tax rate on gaming profit, the remaining
exemption's present value added.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit cd3af4fb); Q1 committed when it closed (f066d400); the
      after-the-stop facts and the computation committed with the close. Declared: the 2015 to 2025 statements were
      extracted in one reading pass before Q1 was written; the Q1 verdict was written and committed before any Q7
      arithmetic was run.
- [ ] Dispatched: the brief allowed the per-question commits; the lock and the fold are the dispatcher's (operator rule
      ten); not checkable by the analyst.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Contamination declared at the
      top. A subagent extracted the rivals' segment figures from the cached SEC filings only, under the same blind rule.
- [x] Every v5 id checked against `principle_ledger_v5.csv` and every quoted fragment against its row
      (`scripts/check_citations.py`); filing facts carry document and date (departure (2)) or accession (SEC filings);
      numbers carry a filing or a CONVENTION.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the arithmetic is headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (stock pay, depreciation or all spending, leases, concession payments), never a
      net-income proxy; the sovereign from the issuing authority's programme file (20-year, confessed); aggregator quotes
      flagged.
- [x] Contrary evidence written down as found (Foundations, four items, weighed at Q1); later-question facts under AFTER
      THE STOP; the integrity flag in the box line.
- [x] Not a point-in-time run.
- [x] `tools/run.py` returned nothing (not an SEC filer); none of its lines used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **A licence that ends inside the horizon has no stated home.** Q1's routing names fast technology for TOO HARD; Q2's
   change section speaks of competitors and technology. Neither says where a government grant that expires in year seven,
   with the operating assets already reverted, is judged. This run placed it at Q1 (tests 4 and 5) because the deciding
   fact is the industry's next tender, not Galaxy's place in it; a reader could place it at Q2 ("a castle whose future
   cannot be judged"). Both end TOO HARD (NATURE); the text should say which.
2. **The macro foundation and the licence rows pull the other way, and the text gives no line.** "We will continue to
   ignore political and economic forecasts" **[L1994-004]** and the television licences **[M2004-058]** argue against
   closing a file on a political decision; nothing separates a macro forecast (ignored) from a policy that is the term of
   the business's own licence (decisive). The run drew the line and said so.
3. **Q7's perpetuity assumes no end date.** For a concession, "ten years then no real growth" credits a renewal the filings
   cannot show; no specific covers a finite licence. The concession-only figure was shown beside.
4. **"Whose tax" names carryforwards and credits, not exemptions renewed by decree.** The Macau exemption has been renewed
   at each expiry, yet each grant runs five years. The run treated it as a shelter that runs out inside ten years; another
   analyst could credit the renewal record. The difference is about 15% of owner cash.
5. **The cycle rule assumes a cycle.** The 2020 to 2022 closures were an event, and the recovery since is not yet a cycle;
   specific (a) gives no rule for growth when the second cycle is incomplete. The run used the three years since reopening
   and said so.
6. **The protocol's sovereign table has no rule for an issuer with no 30-year bond.** The brief supplied one (longest
   tenor, confessed).
