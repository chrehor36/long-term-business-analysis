# Company Run: Public Service Enterprise Group Incorporated (NYSE: PEG), 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form: `Test Runs/_TEMPLATE - Company Run.md`,
copied to this file before any fetch (commit 46edd067). Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the two departures the brief
states (the repository path; the lines of evidence and the competitors derived by the analyst from the 10-K, not given by the dispatcher).
Working folder: `Test Runs/_research 2026-10-26 PEG/` (notes, fetch and strip scripts, `calc.py` and `calc_out.txt` for Q7, `comp.py` and
`comp_out.txt` for the competitor row, `check_run.py` for the citation check; raw filings in its ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no PEG row).*

**CONTAMINATION, declared.** The session's opening context showed the five most recent commit subjects of the repository; they concern another
utility's v5 run (PPL), with that run's box, its Q5 reading and its fair price. I did not open that run file or its research folder, and nothing in
it is used here; I record that I saw the subject lines. The `git status` snapshot listed daily-digest files and one other research folder by name
(not opened). The `tools/run.py` output prints v4 material; only its arithmetic lines were read (Part VII). No other run file, holding review,
`PORTFOLIO.md`, queue, reading list or resume-state file was opened, listed or searched.

**Lines of evidence chosen from the 10-K (the brief's second departure).** From Item 1 (business and segments), Item 1A (risks) and Item 7 (MD&A) of
the FY2025 10-K I chose five: (1) the regulated return at PSE&G: the BPU distribution order of October 2024 (rate base $17.8 billion, ROE 9.6%,
equity 55%), the FERC formula rate (base ROE 9.90% plus a 50 basis point RTO adder), the CIP decoupling, and the risk that programmes are not approved
(Item 1, Item 1A, Item 7); (2) affordability politics in New Jersey: PJM capacity prices "approximately 10 times higher", the bill credits and shut-off
protections of 2025, a new administration from January 2026 (Item 7); (3) competition for new transmission after FERC Order 1000 removed the right of
first refusal (Item 1, Item 1A); (4) PSEG Power's merchant nuclear exposure: PJM prices set by gas, the PTC to 2032 and its unissued gross-receipts
guidance, the end of ZECs in May 2025, the planned licence extensions (Item 1, Item 7); (5) the capital programme and its financing: $24 to $28
billion for 2026 to 2030, funded "from a combination of internally generated funds and external debt financing" (Item 7, Capital Requirements).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $72.18 (2026-10-26, the live quote printed by `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares:** one class. 498,420,030 shares of common stock outstanding as of 2026-07-20, from the cover of the 10-Q for the quarter ended
  2026-06-30 (filed 2026-08-04, accession `0001193125-26-332943`; `python Screens/cover_shares.py PEG`). The second count the tool printed,
  132,450,344, is PSE&G's own common stock, all held by PEG (10-K cover: "all of which were held, beneficially and of record, by Public Service
  Enterprise Group Incorporated"); it is not added. Cross-check: 534 million issued less 36 million treasury at 2026-06-30 on the 10-Q balance
  sheet = 498 million. The 10-K cover gave 498,739,910 at 2026-02-20. The 8-Ks after the 10-Q (2026-08-04 earnings) record no share issue; the
  June 2026 $500 million 4.800% notes (8-K 2026-06-03, `0001193125-26-255562`) closed before the 10-Q balance sheet date and are inside it.
- **Market cap:** $72.18 x 498.42 million = **$35,976 million**.
- **Sovereign for the earnings currency (USD):** **5.33%**, US Treasury daily par yield curve, 30-year, 2026-10-23 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-26, `0001193125-26-077446`): Items 1, 1A, 7, the statements of PEG and PSE&G,
  Note 17 (stock pay), Note 22 (segments), the income-tax note; 10-K FY2023 (filed 2024-02-26, `0001628280-24-006885`) and 10-K FY2021 (filed
  2022-02-24, `0001628280-22-003860`) for the cash-flow statements of 2019 to 2023 and the segment note; 10-Q for 2026-06-30 (filed 2026-08-04,
  `0001193125-26-332943`); DEF 14A (filed 2026-03-12, `0001193125-26-104270`); earnings 8-Ks of 2026-02-26 (`0001193125-26-073678`, Ex. 99) and
  2026-08-04 (`0001193125-26-331660`, Ex. 99). **Cross-checked figure:** net cash from operating activities 2025, $3,298 million on the filed
  consolidated statement of cash flows equals the tagged figure `tools/run.py` read; PSE&G long-term debt $15,117 million at 2025-12-31 on the
  filed PSE&G balance sheet.
- **`tools/run.py PEG`, arithmetic lines only.** Its owner-earnings table stopped at 2024 and warned that its D&A element was intangible
  amortization only; both are true and both make its figures unusable, so the owner cash below is taken from the filed cash-flow statements.
  From those statements (USD millions):

| year | operating cash | additions to PP&E | D&A | nuclear fuel amortization | EE programme spending inside operating cash | stock pay | interest paid | cash collateral, net |
|---|---|---|---|---|---|---|---|---|
| 2021 | 1,736 | 2,719 | 1,216 | 187 | 117 | 28 | 547 | (709) |
| 2022 | 1,503 | 2,888 | 1,100 | 183 | 286 | 29 | 602 | (566) |
| 2023 | 3,806 | 3,325 | 1,135 | 189 | 466 | 18 | 683 | 1,207 |
| 2024 | 2,133 | 3,380 | 1,182 | 191 | 544 | 40 | 799 | (127) |
| 2025 | 3,298 | 3,272 | 1,257 | 202 | 552 | 43 | 932 | 35 |

  **Owner cash after every real cost** (operating cash less additions to PP&E less stock pay; EE programme spending and cost of removal are
  already deducted inside operating cash): 2021 (1,011); 2022 (1,414); 2023 463; 2024 (1,287); 2025 (17). **Five-year average (653).**
  Nuclear fuel purchases are inside additions to PP&E (Item 7: PSEG Power & Other spent "$236 million, excluding $336 million for nuclear fuel"
  in 2025). Stock pay is Note 17's "Compensation Cost included in O&M Expense". The collateral column is posting and return by PSEG Power's
  hedging (2021 and 2022 posted, 2023 returned); it nets to (160) over the window.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own PEG "if the market closed for five years" **[M1997-109]**; a regulated
wires company is the kind of asset for which that question is easy to ask. The margin of safety is an attitude here and arithmetic only at Q7
**[M1996-084]**. No macro view enters: interest rates, PJM capacity auctions and New Jersey politics are read only as they bear on this business's
cash. Who is paid to tell me: the company's own releases feature a non-GAAP figure and a guidance range, which I treat as the seller's projection
and do not use for value. **Contrary evidence, written down as found [M1997-127]:** (1) owner cash after all spending was negative in four of
five years and averaged (653) million: the owners have been paid dividends of about $1.1 to $1.3 billion a year while the business consumed cash,
the gap filled with debt; (2) long-term debt (with current maturities) rose from $16,180 million at 2020 year-end to $23,591 million at
2026-06-30 while equity rose from $15,984 million to $17,329 million; (3) the February 2026 release boasts "the 21st consecutive year that the
company has delivered non-GAAP Operating Earnings at or above management's earnings guidance" (Ex. 99, `0001193125-26-073678`); (4) the
FY2025 10-K reports PJM capacity prices "approximately 10 times higher" and political pressure on bills, with a new state administration;
(5) GAAP net income over 2021 to 2025 sums to $6,829 million while the non-GAAP figure is higher by roughly the 2021 fossil exit.

## THE STANDING RULE
Buying PEG for cash, unlevered and sized so that a fall of half would not force a sale, puts the buyer at no risk of ruin; the rule binds the
buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. Nothing in this purchase
requires borrowed money. Met.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**, reached by "trying to identify the key variables in that particular business, and evaluating how predictable they were first"
  **[M1998-044]**.
- **The parts.** PEG reports two segments (Note 22). Five-year operating income (USD millions): PSE&G 1,818, 1,892, 1,974, 2,286, 2,407 = 10,377;
  PSEG Power & Other (2,674), (511), 1,711, 67, 573 = (834) (2024 and 2025 by difference from the consolidated figures, since the 2025 note
  reports segment net income: PSE&G 1,547 and 1,745 against consolidated 1,772 and 2,111). PSE&G carries more than all of five-year operating
  profit; it **decides** (Q2, a business of parts; Q1's holding-company paragraph).
- **PSE&G's key variables:** the rate base (about $34 billion at 2024 year-end to about $36 billion at 2025 year-end, Item 7); the allowed returns
  (BPU distribution ROE 9.6% on 55% equity; FERC base ROE 9.90% plus a 50 basis point adder, Item 1); the regulators' willingness to approve
  programmes and recover costs on time (Item 1A); customer numbers (CIP decoupling makes "over 90%" of distribution margin vary only with customer
  count, Item 1). These are important and knowable **[M2006-076]**: the insiders do write them down (the 10-K states the 2026 to 2030 capital plan and
  the rate-base growth it expects; I use that only to show the forecast is one insiders would put on paper **[M2000-105]**, not as a value input).
  The economics in ten years: a franchised wires and pipes business in the densest part of New Jersey, earning a return a regulator sets on capital
  it must keep adding. No fast-moving technology carries the forecast **[M1998-008]**.
- **PSEG Power & Other** (not deciding): merchant nuclear output priced in PJM, where "natural gas prices often have a major influence" (Item 1),
  with the PTC as a floor to 2032. Its earnings cannot be forecast with precision; it does not decide, and it is carried to Q7 at no growth.
- **Doubt test.** I have no doubt that the deciding part is inside the circle **[M2002-092]**: "we have a reasonable probability of being able to
  asses where the business will be in 10 years" **[M2000-037]** holds for PSE&G, with the regulatory climate as the variable most likely to be wrong
  (carried to Q2).
- **VERDICT: IN.** The deciding part's ten-year economics can be foreseen from its filings; the key variable that could make the forecast wrong is
  regulatory, not technological.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now"
**[M1995-038]**.

**The parts table** (Q2, a business of parts; five-year operating income from Note 22 and the consolidated statements, USD millions):

| part | five-year operating income 2021 to 2025 | share | castle | decides |
|---|---|---|---|---|
| PSE&G (FERC transmission, BPU electric and gas distribution, regulated solar and EE) | 10,377 | more than all of the 9,543 total | franchised wires and pipes, return set by regulators | **yes** |
| PSEG Power & Other (merchant nuclear 3,758 MW, gas supply to PSE&G, PSEG LI fee contract, parent) | (834) | negative | price-taker in PJM, PTC floor to 2032 | no |

**The castle tests on PSE&G, each with its filing fact.**
- *The money test.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?" **[M2011-015]**. A rival with any sum
  cannot string a second set of distribution wires and gas mains to 2.4 million electric and 1.9 million gas customers across a 2,600 square mile
  franchised territory housing "about 74% of New Jersey’s population" (Item 1); the franchise is "a natural franchise because of surface capabilities"
  **[M1995-037]** in the plainest sense. Customers who choose another commodity supplier still pay PSE&G for delivery: "Our T&D business is not affected
  when customers choose alternate electric or gas suppliers" (Item 1).
- *Where the moat is breached.* New transmission: FERC Order 1000 "generally opened transmission development to competition from independent developers"
  (Item 1A), and the 10-K says the removal of the right of first refusal "could result in third-party construction of transmission lines in our area",
  with "minimal impact so far" (Item 1). Transmission is $835 to $975 million of a $4.2 to $4.4 billion annual PSE&G plan (Item 7); the distribution
  franchise is untouched by it.
- *Pricing power and the agony before a rise* **[M2005-020]**. PSE&G has none of its own: the price is the regulator's, set in rate cases and formula
  filings. The agony is political rather than commercial: in 2025 the BPU ordered bill credits, deferrals and extended shut-off protections after PJM
  capacity prices rose "approximately 10 times" (Item 7), and the 10-K names "regulatory and political uncertainty", "affordability" and a new
  administration (Item 7). That is the place where this castle could be reduced **[M2000-014]**.
- *Unit volume and share of mind.* Not the measure for a wires company: customers grew 0.9% a year (electric) and 0.7% (gas) from 2021 to 2025, and the
  CIP decoupling ties "over 90%" of distribution margin to customer count, not volume (Item 1).
- *The low-cost position.* Not applicable to the franchise; it applies to Power, below.
- *Would the customer choose it over the low bid?* There is no low bid for delivery inside the franchise; the substitute that could appear (customer-side
  solar and storage) has shown "minimal" effect on load so far, and the 10-K expects load to rise with data centres and electrification (Item 1).
- *Ask the competitors.* The 10-K names no rival as a competitor: its only named counterparties of this kind are "merchant generators, utility generators,
  energy marketers, retailers, private equity firms" in the wholesale markets (Item 1), and Constellation Energy Generation, named as co-owner and operator
  of Peach Bottom and co-owner of Salem (Item 2 and the jointly owned facilities note), not as a competitor. **CONVENTION of this run:** the competitor row
  uses Exelon and FirstEnergy, the two SEC filers whose subsidiaries (Atlantic City Electric; Jersey Central Power and Light) are the other large
  electric distribution companies under the same BPU and the same PJM, and Constellation Energy, the named nuclear co-owner, for the part that does not
  decide. Rationale: the 10-K names no rival, and these three share the deciding part's regulator and market or the non-deciding part's plants.
- *Widening or narrowing* **[M1999-108]**. Widening in size: rate base about $34 billion to about $36 billion in 2025 (Item 7), BPU approval of GSMP III
  ($1.05 billion plus $360 million) and CEF-EE II ($2.9 billion). Narrowing in climate: the capacity-price backlash, the new administration, and the
  possible loss of the 50 basis point FERC adder ("approximately $40 million" of annual net income, Item 7). The rows warn that "slow change can be much
  harder to perceive" **[M2014-038]**, and the speakers record their own utility error: "I did not anticipate or even consider the adverse developments
  in regulatory returns" **[L2023-011]**.

**The competitor row** (return on average equity, net income over the average of opening and closing equity, from each filer's tagged 10-K data;
`comp.py`, `comp_out.txt`):

| filer | 2021 | 2022 | 2023 | 2024 | 2025 | span | source |
|---|---|---|---|---|---|---|---|
| PSE&G (deciding part) | 10.4% | 10.3% | 9.3% | 8.7% | 9.1% | 9.5% | PSE&G statements in PEG 10-Ks `0001193125-26-077446`, `0001628280-24-006885`, `0001628280-22-003860` |
| PEG consolidated | (4.3%) | 7.3% | 17.6% | 11.2% | 12.8% | 9.0% | same |
| Exelon (EXC) | 5.1% | 7.3% | 9.2% | 9.3% | 9.9% | 8.0% | 10-K FY2025 `0001109357-26-000018`; 2021 includes the generation business spun off in February 2022 |
| FirstEnergy (FE) | 16.1% | 4.3% | 10.7% | 8.5% | 8.2% | 9.3% | 10-K FY2025 `0001031296-26-000046` |
| Constellation (CEG), for Power | n/a | (1.4%) | 14.8% | 31.1% | 16.8% | 15.7% (2022 to 2025) | 10-K FY2025 `0001868275-26-000032` |

**The field's returns over the cycle, judged in words.** The wires utilities in PSE&G's regulator and market earned about 8% to 9.5% on equity over
the five years, close to the allowed returns (9.6% BPU distribution; 9.90% plus 0.5% FERC), with leverage behind them. Those are the returns a
regulator sets, neither excellent nor failing. The framework's own exception governs: "A return set by a regulator is the exception, carried to Q3 as a
second best" (Q2, What it rules OUT), on the rows "there’s no way we get rich on our utility investments. But there’s no way we get poor, either"
**[M2009-104]** and "decent returns on the incremental sums they invest" **[L2009-012]**. The castle protects a fair return, and it stands.

**PSEG Power & Other (does not decide).** Its price is set by others: "the bid price of the last unit dispatched by PJM establishes the energy
market-clearing price" (Item 1), which is "whatever he charged for gas was my price" **[M2012-109]**. Nuclear's low variable cost makes it a low
marginal-cost producer, but its five-year operating income was negative (the 2021 fossil exit) and its returns swing with prices and subsidies
(ZEC to May 2025, PTC 2024 to 2032). I judge it not a castle; it does not decide, and it is carried to Q7 at no growth.

- **VERDICT: IN.** The deciding part's castle stands: a franchise no sum of money can duplicate, protecting a regulated, fair and not excellent return,
  which is carried to Q3 as a second best. Its threat is the regulatory and political climate in New Jersey, carried to Q9 as written.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the deciding part needs.** PSE&G 2025: net income $1,745 million plus interest $644 million after tax at the statutory
  combined rate of 30.1% (federal 21% plus New Jersey 11.5% net of the federal benefit; CONVENTION of this run, the statutory rate stated because the
  effective rate is moved by regulatory flow-through items) = about $2,195 million, on average capital (long-term debt with current maturities,
  commercial paper and equity) of about $35,010 million: **about 6.3% before leverage**. On equity, 9.1% in 2025 and 9.5% across the five years (Q2
  table). The return is "measured by the operating earnings after depreciation" **[M2014-086]**, and that is the measure used here.
- **What the added capital earned.** PSE&G's capital rose from about $24,138 million at 2020 year-end to about $36,133 million at 2025 year-end
  (+$11,995 million); operating income rose from $1,639 million (2020, 10-K FY2021 `0001628280-22-003860`) to $2,407 million (2025): **about 6.4%
  pre-tax on the added capital**. Net income rose $418 million on $6,687 million of added equity, about 6.3% (about 8% if the fall in non-operating
  pension credits, $205 million in 2020 against $70 million in 2025, is set aside). That is roughly the allowed return, which the rows call fair, not
  rich: "the answer is they’re good enough" **[M2018-056]**, "decent returns on the incremental sums they invest" **[L2009-012]**.
- **To stand still and to grow.** Depreciation at PSE&G averaged $997 million a year against additions of $2,737 million and EE spending of $393 million:
  about $2,134 million a year above depreciation. Owner cash after all spending was negative in every year at PSE&G and in four of five at PEG; dividends
  were paid from borrowing. The row on the utilities states the arithmetic: "To earn more, their owners must invest more." **[L2011-019]**. Part of the
  spending is compulsory replacement (cast iron and unprotected steel mains, aging substations, Item 1), which is the "compulsory reinvestment just in
  order to stand still" **[M1997-016]** in part, though here the regulator pays a return on it.
- **The grade.** The rows' three grades: the best business needs little capital, "The second-best business is a business that also gives you more and more
  money. It takes more money" **[M1998-081]**. PSE&G is the second-best kind at best, and its incremental return of about 6% before leverage sits below the
  floor Q7 applies.
- **WEIGHS AGAINST.** A capital-heavy second best whose added capital earns about the allowed return, around 6% on total capital and 8% to 9% on equity
  with leverage, while consuming all its cash and more; "cash-consuming businesses, by their nature, are unattractive unless the cash they consume gets to
  earn a reasonable return" **[M2012-057]**, and here the return is fair, not more. The "little or no debt" test is Q9's.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends** **[M2025-032]** (USD millions; `tools/run.py` transcription of the first-filed tagged values, spot-checked
against the filed statements: equity 2018 to 2023 against the statements of stockholders' equity in the FY2021 and FY2023 10-Ks, and 2025 against the
FY2025 10-K and the 10-Q comparative column):

| year-end | total assets | equity | cash | receivables | goodwill | long-term debt (non-current) | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 40,070 | 13,130 | 423 | 1,161 | 16 | 10,895 | 9,174 |
| 2017 | 42,716 | 13,847 | 313 | 1,348 | 16 | 12,068 | 9,878 |
| 2018 | 45,326 | 14,377 | 177 | 1,435 | 16 | 13,168 | 10,582 |
| 2019 | 47,730 | 15,089 | 147 | 1,313 | 0 | 13,743 | 11,406 |
| 2020 | 50,050 | 15,984 | 543 | 1,410 | 0 | 14,496 | 12,318 |
| 2021 | 48,999 | 14,438 | 818 | 1,859 | 0 | 15,219 | 10,639 |
| 2022 | 48,718 | 13,729 | 465 | 1,944 | 0 | 16,495 | 10,591 |
| 2023 | 50,741 | 15,477 | 54 | 1,482 | 0 | 17,784 | 12,017 |
| 2024 | 54,640 | 16,114 | 125 | 1,597 | 0 | 18,964 | 12,593 |
| 2025 | 57,576 | 16,982 | 132 | 1,888 | 0 | 21,670 | 13,446 |
| 2026-06-30 (10-Q) | 58,813 | 17,329 | 192 | 1,903 | 0 | 22,741 | 13,853 |

**What moved, and what the figures say, do not say and cannot say.**
- *Debt against equity.* Non-current long-term debt doubled (10,895 to 21,670) while equity rose 29% (13,130 to 16,982). Long-term debt with current
  maturities as a share of long-term capital went from about 46% (2016) to about 57% (2025) and 58% at 2026-06-30. The growth of the asset base was
  financed by lenders, not by retained earnings.
- *Equity against goodwill.* No goodwill; the equity is tangible. The fall in 2021 (15,984 to 14,438) is the fossil exit: "(Gains) Losses on Asset
  Dispositions and Impairments" of $2,637 million and a $298 million loss on extinguishment of debt (FY2023 10-K cash-flow statement).
- *Retained earnings* rose only $1,128 million net over 2021 to 2025 (GAAP net income $6,829 million less dividends $5,701 million), and $500 million of
  stock was bought in 2022 (treasury stock rose from 30 to 37 million shares).
- *Receivables against sales.* Receivables rose 63% (1,161 to 1,888) against revenue up 36% (8,966 to 12,168); the PSE&G allowance stood at $248 million
  at 2025 year-end, and the 2025 bill credits, deferred payment arrangements and extended shut-off protections (Item 7) are the filer's own explanation.
  It is a collection strain the politics of affordability put there, not an accounting tell.
- *What the figures cannot say.* PSE&G's non-current regulatory assets grew from $3,872 million (2020) to $6,431 million (2025): costs already spent
  and carried as assets on the expectation that regulators allow recovery. The balance sheet cannot say whether they will. Deferred taxes of $8,320
  million (2026-06-30) are not read as equity: "I don’t think I would look at that as a hidden form of equity" **[M2015-030]**.
- *Prepayments* rose from $75 million to $425 million in the first half of 2026; the first half of 2025 showed a like rise of $248 million on the
  cash-flow statement, so I read it as seasonal, not as an account "building up suspiciously high" **[M1995-064]**.

**The real costs.**
- Depreciation is charged and treated as a real cost **[R1996-023]**; nuclear fuel amortization likewise. No EBITDA in the 10-K, the releases or the proxy
  (no instance found by a text search of the four documents).
- Stock pay is small ($18 to $43 million a year, Note 17) and is deducted from owner cash.
- EE programme spending ($117 to $552 million a year) is recorded as a regulatory asset inside operating cash; it is capital spending in substance and is
  counted as such at Q7 (it is already deducted inside operating cash).
- The one-time items: the 2021 fossil impairment and debt-extinguishment loss, and a "$239 million after-tax pension charge" in 2023 (Item 7, note A).
  The company excludes such items from its featured figure; I do not: "we do not ask you to forget about those costs" **[M1999-023]**.
- **The featured adjusted figure and the guidance habit.** Every release leads with "non-GAAP Operating Earnings" and a guidance range (Ex. 99 of
  2026-08-04: "Maintains 2026 Non-GAAP Operating Earnings Guidance of $4.28 - $4.40 Per Share"; a five-year growth outlook of "6% to 8% through 2030");
  the February 2026 release counts "the 21st consecutive year" at or above guidance. The rows: "a management that regularly attempts to wave away very
  real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; "the scourge of earnings "guidance" and the desire of CEOs to
  "hit the number."" **[L2019-006]**; "we become downright incredulous if they consistently reach their declared targets" **[L2002-041]**. Recorded here as a
  WEIGHING against **[M1994-018]** and carried to Q5.
- **What the accounts themselves show** (the tells that live in the accounts): the excluded items are disclosed and reconciled line by line, and run both
  ways (2025 non-GAAP $2,029 million was **below** GAAP net income of $2,111 million; 2024 $1,839 million above $1,772 million; Ex. 99 of 2026-02-26);
  the recurring exclusions are the nuclear decommissioning trust's gains and losses and mark-to-market on hedges, which are not operating cash; no
  restatement (the 10-K cover's error-correction boxes are unchecked); management "has not identified any material weaknesses" (Item 9A). The accounts
  are not confusing and raise no suspicion of their own.
- **VERDICT on the accounts: WEIGHS AGAINST** (no STOP): the statements can be read and the owner cash recast from them (Step 0); the featured
  non-GAAP figure, the guidance and the streak weigh against and are carried to Q5. The recast owner cash feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
*(Corrected during the run, 2026-10-26, before Q6 was written. The version committed as 6f37af05 read "VERDICT on integrity: IN (narrowly)" and said
no enforcement action had been found. After that commit, a search of the FY2025 10-K for enforcement terms found the FERC matter below, which I had not
read. The earlier text stands in the commit as the record; the verdict below replaces it. Contrary evidence written down as found **[M1997-127]**.)*

The chief executive is Ralph LaRossa, chair, president and CEO; the board has a lead independent director, Susan Tomasky (DEF 14A,
`0001193125-26-104270`). For a marketable part-interest the speakers read rather than meet.
- **The proxy: how they treat themselves against the owners** **[M1994-009]**. CEO total pay $13,866,735 (2025), $12,367,961 (2024), $11,778,863 (2023)
  (Summary Compensation Table); annual incentive paid $2,563,400 in 2025 against a target of 135% of a $1,386,000 salary, about 137% of target. The proxy
  states that "our executive compensation programs link incentive payouts to measures of Non-GAAP Operating Earnings over multiple time frames": the
  figure the company features, defines and guides is the figure its executives are paid on. PSUs: 50% relative TSR, 25% operating EPS growth, 25% an ESG
  index. Say-on-pay 93.8%; no hedging or pledging; a clawback.
- **The habits carried from Q4.** The featured non-GAAP figure, annual guidance, a five-year growth outlook, a streak of 21 years at or above guidance,
  read with the pay link above: "Managers that always promise to "make the numbers" will at some point be tempted to make up the numbers." **[L2002-041]**;
  "I hate, with a passion, rewarding anything that can be easily faked" **[M1996-089]**; "The people who have their hands on the switch are the
  beneficiaries of the system" **[M1998-066]**.
- **The FERC enforcement matter (10-K FY2025, Note 12, "FERC Matters").** "FERC has completed a non-public investigation of the Roseland-Pleasant Valley
  (RPV) transmission project. In December 2024, FERC approved an agreement between PSE&G and FERC Enforcement Staff resolving its investigation. The
  agreement included a $6.6 million civil penalty and the implementation of certain compliance requirements". The FY2023 10-K (`0001628280-24-006885`)
  had said that in November 2021 "FERC staff presented PSE&G with its non-public preliminary findings, alleging that PSE&G violated a FERC regulation",
  which PSE&G disputed. Neither 10-K names the regulation or the conduct; the FY2025 10-K adds that the agreement reflected no challenge "to the
  end-of-life determination relative to the project and that no disgorgement had been sought", and that an intervenor filed a FERC complaint in January
  2026 seeking a hearing on recovery of the RPV costs. **Secondary sources, flagged (aggregator, not the order):** two law-firm summaries found by web
  search (Troutman Energy Report, LexBlog) describe the December 5, 2024 order in Docket IN21-5-000 as resolving PSE&G's alleged failure to provide
  full and accurate information to PJM when seeking approval to replace a transmission line in the regional expansion plan, with PSE&G stipulating to
  the facts and neither admitting nor denying the violations. I did not read the FERC order itself (the FERC page refused the fetch).
  Beside it: a BPU management and affiliate audit of PSE&G (begun 2021, report filed June 2023) whose recommendations the BPU has not yet determined.
- **The rest of the record, read for doubt.** No restatement; no material weakness; the non-GAAP reconciliation runs both ways (2025 below GAAP); the
  reports tell an owner much of what matters (Q4). The releases read as investor-relations product, which "tells you something about the individual"
  **[M2007-083]**.
- **Ability.** Operations: nuclear capacity factor 91.2% in 2025; storm restoration of about 380,000 customers "within 24 hours" (Ex. 99, 2026-08-04).
  Capital: the fossil exit cost an impairment of $2,637 million. On balance UNDECIDED; it does not bear on the verdict.
- **Judgment, on doubt alone.** The question is "do we really want to be in partnership with this person and count on them to behave in the future"
  **[M2015-005]**. Three facts point the same way: a federal regulator's enforcement staff found, and the company
  settled with a civil penalty and compliance monitoring, a violation that the secondary sources describe as giving the grid operator less than full and
  accurate information to win approval for a transmission project, which is the mechanism by which PSE&G adds to the rate base it earns on; the 10-K
  describes that matter without saying what the violation was, which is "dancing around something" **[M1995-111]**; and a 21-year streak of meeting
  self-set targets on a self-defined figure on which pay is set **[L2002-041]**. None is proof of dishonesty, and the penalty is small against the
  company. But the rule is applied on doubt, not on proof: "If you’ve got doubts, forget it." **[M2013-088]**; "we rule out 90 percent of the times. And
  we may be wrong about a fair number that we’re ruling out." **[M2007-092]**. I hold the doubt.
- **VERDICT on integrity: OUT (on doubt).** The file closes here. What would reopen it is knowable: the FERC order in Docket IN21-5-000 and its stipulated
  facts, and the BPU audit's findings; a later run that reads them answers this question first. Q6 onward are NOT REACHED; Q7 is computed below under
  the protocol's heading as a reporting figure only.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED (Q5 closed the file). Facts found are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? NOT REACHED as a verdict. Reported below as COMPUTATION, NOT A CLEARANCE (operator rule 3; Part VII, The owner's price).

### COMPUTATION, NOT A CLEARANCE
*Arithmetic in `calc.py`, output in `calc_out.txt`. USD millions unless per share. A reporting figure only; no entry language.*

- **Basis.** The deciding part (PSE&G) earns a return a regulator allows on its invested capital, "when you get an allowed return in the electric utility
  you’re almost certain of earning it" **[M2010-037]**, so Q7, The regulated utility, makes the **equity-only basis central** (the exception in
  **[L2017-012]**), with the all-equity basis beside. Tax: the company's own; the 2024 PTC is treated below.
- **The cash input (2021 to 2025, the literal window).** Owner cash after all spending averaged **(653)** a year (Step 0): no positive base. Specific (e):
  the filing allows the maintenance guess, with depreciation as the proxy "for required capital expenditures" **[M1998-127]**; "Every year we spend
  amounts equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**.
  - PSE&G after maintenance only (operating cash plus EE spending less D&A): 913, 1,379, 1,026, 1,244, 1,804; **average 1,273**. Its growth spending
    (additions plus EE spending less D&A): **average 2,134**.
  - PSEG Power & Other (consolidated less PSE&G): operating cash average 618 less additions 379 (which sit at its D&A plus nuclear fuel amortization,
    372, so all of it is treated as maintenance) = **239**, carried flat at no growth (Q2, the part that does not decide). Stock pay **(32)**, flat.
  - **No-growth stream, equity-only: 1,480 a year.** The collateral posted in 2021 and 2022 and returned in 2023 is inside the window and nets to (160);
    no cycle base is substituted (specific (a)); the literal window is the base.
- **The growth carried.** PSE&G's maintenance-case owner cash grew 18.6% a year between the end years (9.97% between the halves). Carried ten years it
  would need owner cash far above 18.9% of sales, the highest share in the window, so specific (f) cuts it to PSE&G's own sales growth, 7.63% a year
  (7,122 to 9,558), and that is capped at the discount rate: **5.33%** **[M1999-067]**.
- **The growth spending and the debt credit (specific (e), The regulated utility).** Growth spending 2,134 grows with the growth: **2,247 in year one,
  3,586 in year ten, none after.** Long-term debt with current maturities rose from 16,180 (2020) to 22,545 (2025): **1,273 a year**. The cap: the
  filing states an allowed debt share (45%, from the BPU's 55% equity) only for the $17.8 billion distribution rate base, under half of the about $36
  billion regulated rate base; so the cap is PEG's own long-term debt share of long-term capital at 2026-06-30, 23,591 / (23,591 + 17,329) =
  **57.65%**, which caps the credit at 1,230 against 1,273 raised. **Credit 1,230 a year**, growing with the growth spending (1,296 in year one, 2,067 in
  year ten) and stopping with it. The 45% cap is shown beside.
- **The range, equity-only, at 5.33%, per share on 498.42 million shares:**

| case | value | per share |
|---|---|---|
| no growth (1,480 a year for ever) | 27,775 | **$55.73** |
| growth (PSE&G at 5.33% ten years, net of growth spending and credit, then flat; Power and stock pay flat) | 31,470 | **$63.14** |

  **VALUE RANGE: $55.73 to $63.14 a share, against $72.18.** Width about 1.13 to one. With the 45% cap: $55.73 to $57.73.
- **The floor, tested first.** At the price, the no-growth stream yields 1,480 / 35,976 = 4.1%, below the sovereign and far below about ten percent;
  valued at ten percent, the two cases give $29.70 and $26.60, both below $72.18. **No case earns the floor at the price** **[M2003-149]**, and the price
  is above the top of the range: had Q7 been reached, it would close OUT by the floor.
- **FAIR PRICE (reporting figure, Part VII): $28.15 a share, equity-only, central** (the average of $29.70 and $26.60; with the 45% cap, $26.00).
  The growth case is worth less than the no-growth case at ten percent: the growth bought at the allowed return is worth less than its cost at the
  floor, "growth can destroy value" **[L2000-023]**.
- **All-equity, beside, never deciding:** owner cash plus after-tax interest (712.6 average interest paid at 30.1% statutory: 498), no debt credit, less
  net debt of 24,349 at 2026-06-30 (long-term debt 22,741, current maturities 850, commercial paper and loans 950, less cash 192; no finance lease line
  on the face; operating leases left out): range **$8.36 to $25.63**, fair price **($20.50)**, not positive.
- **Shown beside, not used:** the literal all-spending window, (653) a year, has no positive value; section E (the 2024 PTC benefit of $350 million,
  a credit that ends in 2032, removed from the base at the statutory rate, its future value set at nil because the filer expects 2026 realized prices
  "above the level at which we would receive PTCs"): $53.09 to $60.51; the window 2022 to 2025 (dropping 2021): $63.78 to $71.94, rejected because it
  keeps the 2023 return of collateral posted in 2021.

## Q8, Q9, Q10, Q12: NOT REACHED.

---
## THE BOX
**OUT at Q5 (integrity, on doubt): a FERC civil penalty of $6.6 million (December 2024) for a violation the 10-K does not describe and secondary sources
describe as incomplete information given to PJM on a transmission project, read with a 21-year streak of meeting self-set non-GAAP guidance on which pay
is set.** COMPUTATION, NOT A CLEARANCE beside it: equity-only value range $55.73 to $63.14 against $72.18, fair price $28.15 (all-equity fair price not
positive); no case earns the floor at the price, so Q7 would have closed OUT as well. Re-look condition: the FERC order in Docket IN21-5-000 and the BPU
audit's findings, read first by any later run.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; the box unchanged (operator rule 2) **[M1997-127]**.*
- **Q6 (money and owners).** Dividends paid $1,031 to $1,258 million a year (2021 to 2025), $5,701 million in all, against GAAP net income of $6,829
  million and owner cash after all spending of (653) a year: dividends funded by borrowing. Buyback: $500 million in 2022 for 7 million shares (about $71
  a share; stockholders' equity statement, FY2023 10-K), a fixed-sum programme with no stated price; that is above the bottom of the computed range
  ($55.73), the line Q6 would read. No acquisition in the window; the fossil fleet sold in February 2022 for $1,918 million of proceeds after a
  $2,637 million impairment. No shares issued for deals. Pay: chair and CEO combined, with a lead independent director; 50% of PSUs on relative TSR
  against a peer group; incentive payouts linked to non-GAAP Operating Earnings; CEO pay $13.9 million in 2025.
- **Q9 (debt and exposures).** Long-term debt with current maturities $23,591 million and commercial paper and loans $950 million at 2026-06-30, against
  equity $17,329 million. Interest coverage, pre-tax earnings over interest **[L2012-002]**: (2,374 + 1,005) / 1,005 = 3.4 times in 2025; (1,825 + 882) /
  882 = 3.1 times in 2024. Interest paid rose from $547 million (2021) to $932 million (2025). PSEG Power's hedging drew cash collateral of $790 million
  (2021) and $677 million (2022), alongside short-term loans of $2,500 million (2021) and $2,000 million (2022): demands for sudden sums of the kind the
  standing rule names **[L2014-024]**. A $500 million variable-rate PSEG Power loan due December 2026. Nuclear decommissioning trust $2,995 million
  against asset retirement obligations of $1,403 million (2026-06-30). Newark Bay Complex Superfund liability (Item 7). The regulatory climate:
  capacity-price backlash, bill credits, a new administration, possible loss of the FERC adder (about $40 million a year), the January 2026 complaint on
  RPV cost recovery.
- **Q10.** Nothing found beyond the above.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (46edd067); written question by question; committed after each (c6686bd2, 2e6849ea, f8c9e2d9, bd0cccf6,
      6f37af05, 1bc49585, and the closing commit). The Q5 verdict was changed after its first commit, on evidence found afterwards; the change is stated
      in Q5 and the first text stands in 6f37af05.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` opened, listed or searched; the commit subjects about another utility's run seen in the opening
      context are declared under CONTAMINATION and not used.
- [x] Every v5 id resolves (`check_run.py`: no E-ids, every M/L/R id in the CSV, every quoted fragment beside an id found in that row; the check treats
      straight and curly apostrophes and the replacement character as one). Every filing fact carries its document and accession. One fact rests on
      secondary sources (the FERC order's description), flagged as aggregator material.
- [x] The order kept; Q5 closed the file; Q7 shown only as COMPUTATION, NOT A CLEARANCE, with no entry language.
- [x] Owner cash from the filed cash-flow statements after every real cost, never a net-income proxy; the sovereign from the Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, the Q5 correction); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` used; its owner-earnings table was not used (stale window, D&A warning).
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) The utility debt credit's cap: the filing states an allowed equity share for the distribution rate base ($17.8 billion, set in the 2024 order) but
not for the FERC formula-rate transmission base, and the distribution base is just under half of the $36 billion regulated rate base at 2025 year-end
(it was just over half of the $34 billion a year earlier). The rule's switch at "less than half" therefore turns on which date's rate base is used, and
"the business's own long-term debt share" does not say whether the business is the holding company or the deciding subsidiary (PEG 57.65%, PSE&G about
45%). I used the latest date and the holding company and showed the 45% cap beside; the box does not turn on it. (2) Specific (f) cuts an absurd rate
to "sales growth", but a utility's sales include pass-through commodity costs (PSE&G's energy costs were $3,782 million of $9,558 million in 2025), so
sales growth measures fuel prices as much as the business; the cap at the discount rate bound here, so it did not matter. (3) Q5 names no box for its
STOP and no rule for an integrity fact whose primary document (here a FERC order) is knowable but not read: I closed OUT on doubt, as the rows apply the
rule, and wrote the re-look condition; a reader could argue for TOO HARD (WORK). (4) Q6's buyback line needs the bottom of Q7's range, which a file
closed at Q5 still computes; I recorded the comparison under AFTER THE STOP.

