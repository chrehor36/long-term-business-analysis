# Company Run — California Water Service Group (NYSE: CWT) — 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under `Screens/_daily/_dispatch_brief.md`, with the departures the brief itself states (the repository path; the lines of
evidence derived from Items 1, 1A and 7 of the 10-K). Every judgment cites a v5 ledger id in bold; every filing fact carries
its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-28: the operator does not hold this name (`PORTFOLIO.md` has no CWT row).*

**CONTAMINATION, declared and not used.** (1) The session context listed recent commit subjects of another company's run
(American States Water, AWR: "OUT at Q7", with a range and a fair price in the subject line). AWR is one of the three rivals
chosen for Q2 below; it was read only from its own SEC filings (XBRL facts), its run and research files were not opened, listed
or searched, and the figures in those commit subjects were not used. (2) The git status in the session context showed the
name of another company's research folder (ARCB) and dated daily digests; none was opened. (3) The memory index loaded with
the session mentions counts of gate-clearers and owed holding reviews without naming this company; not used.

**Lines of evidence chosen, and why** (derived from the 10-K's Items 1, 1A and 7): (a) the regulatory record, since Item 1
says the Commissions "have plenary powers to set both rates and operating standards" and that their decisions "significantly
impact the Company’s revenues, earnings, and cash flows": the 2021 and 2024 California rate cases, the cost of capital, the
decoupling mechanisms; (b) the capital programme against the cash it throws off, since Item 7 says internally generated
funds "have not been at a level to meet the needs of our capital expenditure requirements" and expects that to continue;
(c) the liabilities the owner cannot see in the earnings: inverse condemnation (strict liability), the Rancho Palos Verdes
land-movement suits, PFAS capital, purchased-water cost; (d) the share issuance that funds the gap (the ATM programme);
(e) the accounting record (the 2022 material weakness and two corrections). Working notes and the computations are in
`Test Runs/_research 2026-10-28 CWT/`; the filings are in its cache (gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $47.82 (close 2026-10-27; `tools/sources.py` price, a Yahoo chart quote: **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: 61,839,101 common, one class (10-Q for the quarter ended 2026-06-30,
  filed 2026-07-30, accession 0001628280-26-050990; `python Screens/cover_shares.py CWT`). Checked: the 10-Q balance sheet
  shows 61,839 thousand outstanding at 2026-06-30 against 59,638 thousand at 2025-12-31, the rise being the at-the-market sale
  of $94.1 million of stock in the half year (10-Q MD&A). No 8-K or prospectus after the 10-Q reports a share issue; the 424B5
  of 2026-05-01 (0001104659-26-054204) only changes the sales agents of the $350 million ATM. The third-quarter 10-Q is not yet
  filed; any ATM sales in that quarter are not in this count (stated, not estimated).
- **Market cap:** $47.82 x 61.839M = **$2,957.1M**.
- **Sovereign for the earnings currency (USD):** 30-year par yield **5.30%**, US Treasury daily par yield curve, 2026-10-27
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for 2025, filed 2026-02-27, accession 0001628280-26-012444 (Items 1, 1A, 7, the
  statements, Note 1); 10-Q for 2026-06-30, filed 2026-07-30, 0001628280-26-050990 (balance sheet, rate-case section,
  liquidity); proxy DEF 14A filed 2026-04-08, 0001104659-26-040708 (Q5 and Q6); 8-K of 2026-10-15, 0001104659-26-116113 ($125M
  of senior unsecured notes and $150M of first mortgage bonds, to be issued by 2026-12-31, "to refinance existing indebtedness
  and for general corporate purposes"); 8-K of 2026-04-29, 0001104659-26-051525 (a dividend declaration of $0.335; the rate-case
  decision of 2026-04-30, D.26-04-045, is read from the 10-Q); the 424B5 above. The cash-flow statements of the 10-Ks for 2023
  (0001035201-24-000004), 2021 (0001035201-22-000002) and 2019 (0001035201-20-000002); the 10-K for 2022 (0001035201-23-000003)
  for its material weakness and restatement note.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025 is $302,561
  thousand in the filed cash-flow statement (10-K 2025) and $302.6M in the XBRL facts; long-term debt, net, at 2025-12-31 is
  $1,471,968 thousand in the 10-Q balance sheet and $1,472.0M in the XBRL facts.
- `python tools/run.py CWT` printed "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (the filer tags its capital
  spending `PaymentsToAcquireWaterAndWasteWaterSystems`). The arithmetic below is therefore built from the filed cash-flow
  statements, with the XBRL facts as transcription (`facts.py`, `owner_cash.py` in the research folder).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: a regulated water utility is about as near as a listed share comes to a business one
would hold with the market closed, so the only question is what the business will pay its owner. The market serves and does
not instruct **[M2006-077]**: the price is read against value at Q7 and nowhere else. No macro enters **[M2000-094]**:
interest rates enter only as the sovereign at Q7 and as the return the regulator allows, never as a forecast. Who is paid to
tell you **[M2020-037]**: a utility that funds its capital plan by selling stock through a panel of sales agents has an
interest in a high quotation; its investor material is not read as evidence. The analyst's habits: look for "what’s wrong"
**[M2025-013]** and read "to possibly reject your original hypothesis" **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after all capital spending was negative in every
year of the window (Q3, Q7), so every dividend dollar since 2021 was in effect borrowed or raised in stock; (2) the 2025 10-K
says internally generated funds after dividends have not met the capital plan and expects that to continue for five years;
(3) the return on average equity was 7.7% in 2025 against an allowed 10.27% (10-K Item 7); (4) a material weakness over
regulatory assets and liabilities in 2022, with an immaterial restatement, and a presentation correction in 2023 (Q4);
(5) strict-liability inverse condemnation in California, with live landslide suits (Item 1A); (6) the speakers' own costly
mistake on regulatory returns, naming California **[L2023-011]**.

## THE STANDING RULE
A part-interest bought with the buyer's own money, unlevered and sized so that its total loss could be borne, puts the buyer
at no risk of ruin **[M2012-081]**, **[L2023-005]**; the target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The business is
  simple: it pumps or buys water and pipes it to about 562,000 connections (10-K 2025, Item 1), 91.2% of revenue from Cal
  Water's California districts under the CPUC, with Washington, New Mexico, Hawaii and Texas small. No substitute for piped
  water is named anywhere in the 10-K.
- **The key variables, and how predictable** **[M1998-044]**: (1) rate base, which grows with the capital the CPUC authorizes
  (D.26-04-045 authorized about $1.45 billion for 2024 to 2027, 10-Q 2026-06-30); (2) the allowed return: 10.27% on equity,
  4.23% cost of debt, 53.4% equity in the capital structure, unchanged since 2023 through three extensions of the cost of
  capital filing to May 2027 (10-K Item 1); (3) the lag between spending and recovery, visible in the earned return; (4)
  liabilities outside the rate base: inverse condemnation, contamination, landslides (Item 1A); (5) the share count, since the
  capital plan is funded partly in stock (the two Coca-Cola variables were "unit case sales and shares outstanding"
  **[M1998-040]**). The first two are set by a regulator and are as foreseeable as business variables get; the third is
  readable from ten years of filings; the fourth is the far tail; the fifth is in management's hands.
- **Do the past statements tell me the future ones?** **[M2008-033]**: yes for revenue, rate base and spending, since each
  rate case sets them three years at a time and the filings disclose each step; the year's earnings swing with the timing of
  decisions (2023 net income $51.9M, 2024 $190.8M including about $64.0M belonging to 2023, 10-K 2025 Item 7), which a
  five-year view averages out.
- **How far off could I be?** **[M2011-084]**: narrow on rate base and revenue; wide only on the regulator's future temper and
  on a single liability event. The speakers' own error was there: "I did not anticipate or even consider the adverse
  developments in regulatory returns" **[L2023-011]**. That is a question of the castle's durability and of the return, owned
  by Q2 and Q9, not a question whether the economics can be pictured at all.
- **Routing.** Not a fast-changing industry; not a financial institution. A holding company read by its parts: Cal Water
  decides (the issuer's income from operations was $169.5M of a consolidated $170.4M in 2025, 10-K Item 7 guarantor table and
  income statement), and Cal Water is understood.
- **VERDICT: IN.** The ten-year economics of a California regulated water utility can be pictured from its filings: rate base
  grown by authorized spending, times an allowed return, less lag **[M2012-065]**, **[M2000-037]**. The doubt that remains is
  about the regulator and the tail; it is carried to Q2 and Q9 and is not a doubt whether the business is inside the circle
  **[M2002-092]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now" **[M1995-038]**.
- **The attacker with money** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s
  Candy, could I do it?" Against Cal Water the answer is no, but not because customers prefer it: "Under state laws, no
  privately owned public utility may compete within any service territory that we already serve without first obtaining a
  certificate of public convenience and necessity from the applicable Commission. Issuance of such a certificate would only be
  made upon finding that our service is deficient." (10-K 2025, Item 1, Competition and Condemnation). The one attacker the
  10-K names is a public agency, which may condemn the system by eminent domain against "just compensation"; the 10-K knows of
  no such action pending other than one annexed area on Orcas Island. The castle is the legal franchise and the pipe in the
  street, and it stands.
- **Pricing power and the agony before a rise** **[M2005-020]**: "you can almost measure the strength of a business over
  time by the agony they go through in determining whether a price increase can be sustained." For Cal Water every price
  is set by the CPUC: the 2024 rate case was filed in July 2024, requested $140.6M (17.1%) for 2026, was decided on
  2026-04-30 (D.26-04-045) at about $90.5M for 2026, four months late and with interim rates and a memorandum account to
  make up the lag (10-K Item 1; 10-Q 2026-06-30). The 2021 case was decided in March 2024, fourteen months late, with $64.0M of
  2023's income booked in 2024 (10-K Item 7). The power to price belongs to the regulator, not the business; what the
  business owns is the right to a return on what it invests, "within a range, anyway — a guaranteed return" **[M2009-104]**.
- **Unit volume, share of mind, brand, the low bid:** not tests that apply. Volume is regulated and decoupled: the decision
  continues the M-WRAM and adds a "new annual Sales Reconciliation Mechanism" (10-Q). The customer has no choice to make.
- **Ask the competitors / the rivals' filings.** The 10-K names no rival that files (its competition section names only
  public agencies). **CONVENTION of this run:** the three rivals chosen are American States Water (AWR, CIK 1056903; its
  Golden State Water serves California under the same CPUC), H2O America (formerly SJW Group, CIK 766829; San Jose Water,
  CPUC) and American Water Works (AWK, CIK 1410636; the largest listed US water utility, with a California subsidiary);
  rationale: the two listed California water utilities under the same regulator, and the national benchmark. Read from
  their XBRL company facts (10-K FY values), `peers.py`, `peers.txt`.
- **The competitor row** (net income over average shareholders' equity, each year, as each filer reports; the same metric
  from each filer's own facts):

| filer | 2016-2025 average | 2021-2025 average | range of years |
|---|---|---|---|
| CWT | 8.8% | 8.3% | 3.8% (2023) to 12.4% (2024) |
| AWR | 13.5% | 13.9% | 11.2% to 16.8% |
| H2O America (SJW) | 7.6% | 6.9% | 2.6% to 13.4% |
| AWK | 11.0% | 12.2% (2021 includes a sale gain; the other four years 10.4% to 10.9%) | 8.0% to 18.4% |

  CWT has earned well under its allowed 10.27% across the whole span, second lowest of the four; AWR, under the same CPUC,
  earned about five points more on equity (AWR includes a contracted military-base services business the CWT filings lack,
  so the gap is not all regulatory skill; stated, not adjusted).
- **The parts table.** One reportable segment (10-K Item 1). By subsidiary: Cal Water 91.2% of 2025 revenue and $169.5M of
  $170.4M operating income (Item 7 guarantor table). Cal Water decides; its castle is the CPUC franchise above.
- **The field's returns over the last full cycle**, judged in words: ordinary. CWT 8.8% on equity over ten years against a
  sovereign that now stands at 5.30%; the field 7.6% to 13.5%. A standing castle that protects only ordinary returns would
  close OUT, except where the return is set by a regulator, which the framework carries to Q3 as a second best: "there’s no
  way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**; "decent returns on
  the incremental sums they invest" **[L2009-012]**.
- **Widening or narrowing; what could destroy, modify or reduce it** **[M2000-014]**: the evidence against is the regulator.
  The speakers' own utility mistake names this state: "the regulatory climate in a few states has raised the specter of zero
  profitability or even bankruptcy (an actual outcome at California's largest utility" **[L2023-011]**. That row is about
  electric utilities and wildfire, and a row about one company is weighed, never a verdict on its industry (Q2, A row about
  one company). For water in California the filed record is mixed, not broken: the CPUC kept the 10.27% allowed return by
  three extensions, authorized $1.45 billion of investment, kept decoupling, and made the delays whole through interim-rate
  memorandum accounts (10-K Item 1; 10-Q); against that, two consecutive rate cases ran late, the 2024 award was about 64%
  of the first-year request, SERP costs were disallowed in the 2021 case (10-K Item 7), and inverse condemnation in
  California is strict liability whose recovery in rates "there is no assurance" of, citing the CPUC's 2017 refusal to an
  electric utility (Item 1A). The threat is "the threat of reregulation, which has a tempering effect on their pricing power"
  **[M2007-112]**, not a rival.
- **VERDICT: IN**, on the regulated exception. The castle (the exclusive franchise) is standing and is not shown open
  **[M2011-015]**; its return is set by a regulator and is ordinary, which the framework carries to Q3 as a second best
  **[M2009-104]**, **[L2009-012]**; the regulatory threat is weighed here and at Q9, and is not shown on the filed water
  record to have broken the castle **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**: net income plus after-tax interest over average equity plus
  long-term debt was 6.7%, 5.5%, 3.6%, 8.7% and 5.7% in 2021 to 2025 (`owner_cash.txt`; tax at the combined statutory 27.98%,
  21% federal plus 8.84% California net of the federal benefit, CONVENTION of this run, the filings' own statutory rates).
  On equity, 8.3% over the window (Q2). No goodwill of size ($37.1M of $5,671M assets, 10-K 2025).
- **Reinvestment to stand still and to grow.** Utility plant spending was $293M, $328M, $384M, $471M and $517M in 2021 to
  2025 against depreciation of $112M to $147M (filed cash-flow statements); the 2026 plan is $580M to $640M, and the 10-K
  expects spending "to increase during the next five years due to increasing needs to replace and maintain infrastructure".
  The 10-K's own words on the gap: internally generated funds, after dividends, "have not been at a level to meet the needs
  of our capital expenditure requirements. Management expects this trend to continue". Owner cash after all spending was
  negative every year of the window, $-58.5M to $-194.5M on the cash-tax basis (`owner_cash.txt`). This is the business
  "that reports the 12 percent on capital but there’s never any cash" **[M2003-122]**, with the difference that it reports
  about 8%. The spending is compulsory: water-quality rules (PFAS, an estimated $269.1M to comply; chromium-6), pipe
  replacement, power resilience (10-K Item 1); "we have tried to avoid places where there was a lot of compulsory
  reinvestment just in order to stand still" **[M1997-016]**. The maintenance guess is depreciation **[M1998-127]**; the
  10-K's statement that spending must rise to replace and maintain infrastructure is evidence that it may be short, as
  "your depreciation charges are inadequate" in "the utility business" **[M2015-049]**, so the guess is generous to the
  business.
- **The growth arithmetic.** Revenue grew 6.0% a year 2021 to 2025, but net income per diluted share went from $1.96 (2021)
  to $2.15 (2025), about 2.3% a year, while the share count rose from 51.6M to 59.6M (diluted weighted, XBRL) and equity from
  $1,172M to $1,692M. "we’re not earning a higher rate of return on capital than we were when we started. We just put way more
  capital into the business" **[M2023-081]**. The capital-heavy business is admitted "as the second-best choice"
  **[M2018-055]** only when "the cash they consume gets to earn a reasonable return" **[M2012-057]**; the regulated return is
  measured "by the operating earnings after depreciation" **[M2014-086]**, here about 6% on total capital and 8% on equity,
  close to the 5.30% sovereign. "To earn more, their owners must invest more" **[L2011-019]**.
- **WEIGHS AGAINST.** A second-best business at best **[M2018-055]**, whose added capital earns a thin return over the long
  government rate **[M2012-057]**, **[M2014-086]**, and which has never thrown off cash after its compulsory spending
  **[M2003-122]**, **[M1997-016]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten years** **[M2025-032]** (`bs_table.txt`, XBRL facts read against the filed balance sheets
  of the 10-Ks for 2019, 2021, 2023 and 2025 and the 10-Q): total assets $2,412M (2016) to $5,671M (2025); net utility plant
  $1,859M to $4,580M (the 2022 step of $626M is partly the cost-of-removal reclassification described below); goodwill $2.6M
  to $37.1M, small (Texas and Hawaii purchases of 2020 and 2021); cash $25M to $95M, never large, the business living on its
  revolvers; customer receivables $30M to $61M, roughly in step with revenue after the 2020 to 2021 arrears; noncurrent
  regulatory assets $256M to $433M, no trend; long-term debt $558M to $1,474M; short-term borrowings swinging $35M to $370M
  with the season and the bond calendar; noncurrent regulatory liabilities $39M to $930M (cost of removal $524M at 2025 and
  PFAS settlement proceeds held for customers, 10-K 2025 Note 4); deferred income taxes $195M (2017) to $451M;
  contributions in aid of construction $181M to $297M; total equity $660M to $1,692M, of which about $513M from stock sold
  2021 to 2025 (cash-flow statements). What the balance sheets say: a plant base growing about 10% a year, funded by debt,
  new stock, developers' money and deferred taxes, with retained earnings a minor source. What they cannot say: whether the
  regulator will allow a return on all of it.
- **The real costs.** Depreciation is real and is charged (Q3, Q7) **[L2015-004]**; stock pay $3.0M to $6.8M a year is
  charged in owner cash; no EBITDA in the 10-K, no adjusted earnings and no earnings guidance found (text search of the 10-K
  2025 and 10-Q for "EBITDA", "adjusted", "non-GAAP", "guidance": only accounting-standard uses). Deferred taxes: owner cash
  is shown with the deferral charged (central) and not charged (beside) at Q7, since for a utility "I don’t think I would
  look at that as a hidden form of equity" **[M2015-030]**.
- **The tells.** (1) A material weakness at 2022 year-end: the company "did not design and maintain effective internal
  controls over the completeness of its accounting for regulatory assets and liabilities"; a regulatory liability for 2019
  customer refunds had not been recorded; equity was restated down $11.1M as an immaterial error (10-K 2022, Item 9A and
  Note 16, 0001035201-23-000003). Remediated, per the later 10-Ks' risk factors ("which was remediated"). (2) The 2023 10-K
  moved the cost of removal from accumulated depreciation to a regulatory liability because it "should have been presented"
  that way (10-K 2023, Note 4, 0001035201-24-000004). Both errors were found by the company and disclosed; neither flattered
  cash. "When managements take the low road in aspects that are visible, it is likely they are following a similar path
  behind the scenes" **[L2002-039]**: the weakness was on the regulatory side, where a utility's earnings are made, so it is
  weighed, but it is a control gap, not a game with the numbers.
- **What the accounts say of management.** The 10-K explains the lumpy years in plain terms (the $64.0M of 2023 income in
  2024; the IRMA and MWRAM mechanics) "in clear terms what’s going on" **[M1994-018]**.
- **VERDICT on the accounts: IN; WEIGHS AGAINST, mildly.** Not confusing and not suspect **[M1995-063]**, **[M1995-065]**;
  the 2022 weakness and the two corrections weigh against **[L2002-039]**. The recast earnings (owner cash, Q7) carry the
  deferred-tax question both ways.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run it, against the hand dealt: the hand is the CPUC; against AWR,
  dealt the same regulator, CWT earned about five points less on equity over ten years (Q2); against H2O America it earned
  more. The CEO, Martin Kropelnicki, has run the company since 2013 (CFO 2006 to 2012) and became chairman in 2023 (10-K
  Item 1; proxy). How they treat the owners: Q6.
- **The proxy** **[M1994-009]**: CEO total pay $4.86M (2023), $4.80M (2024), $6.88M (2025, of which $2.25M is change in
  pension value); 2025 non-equity incentive $1.52M in a year when net income fell 33% (the 2024 figure carried 2023's
  income). Say-on-pay support fell to 67% in 2025 from 92% to 96% in 2021 to 2024; the response added relative TSR and a
  three-year "adjusted return on equity" to the long-term plan. The committee benchmarks pay to a "designated Proxy Peer
  group" with a consultant (proxy, DEF 14A 2026, 0001104659-26-040708). Directors and executives own about 1.0% together;
  the CEO 148,828 shares, about $7.1M at the price. Anti-hedging, anti-pledging and a clawback policy (proxy).
- **Tells of dishonesty** sought: no adjusted earnings in the filings, no guidance, no target-beating language found in the
  10-K or 10-Q; the proxy calls 2025 "a strong year" in which earnings per share fell from $3.25 to $2.15, which is
  salesmanship in a pay document, recorded as such. The 2022 material weakness (Q4) is a control failure the company found
  and fixed, not a concealment. No restatement of cash, no SEC action, no related-party matter found in the documents read.
- **Ability** shows in the record: the capital programme delivered (record $517.0M in 2025), two rate cases won late but
  whole, and an earned return persistently below allowed and below the same-state rival.
- **VERDICT on integrity: IN** (no doubt found on the record read **[M2013-088]**; trustworthiness first **[M2015-047]**);
  **ability WEIGHS AGAINST, mildly**: the hand dealt is the same as AWR's and the record is worse **[M1994-008]**. For a
  marketable stock the reading tests carry the weight **[M2007-081]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M2011-072]**: over 2021 to 2025 the company kept $268M of earnings
  (net income attributable $568M less dividends $300M) and sold $513M of new stock; market value went from about $2,720M
  (2020 year-end close $54.03 x 50.35M shares, aggregator closes flagged) to about $2,584M (2025 close $43.33 x 59.64M). About
  $781M put in against a fall of about $136M in market value: the market leg fails, and the price per share fell from $54.03
  to $43.33 while book value per share rose. Against intrinsic value: Q7's range ($22.60 to $27.66 a share, central) sits
  below book value per share (about $28.4 at 2025, $1,692M over 59.6M), so the retained and raised dollars are worth less
  than a dollar each at the long government rate on the central basis. The test fails on both legs **[M1998-110]**.
- **Dividends**: a stated "long-term targeted dividend payout ratio" of 60% and 59 consecutive annual increases (10-K Item 7),
  paid while owner cash after spending is negative and stock is sold to fund the plan. A payout set by ratio "strikes us as
  nuts" **[M2000-051]**; a dividend paid with money raised from the same owners imposes the tax cost **[L2012-014]** for no
  gain.
- **Buybacks**: none beyond about $1.4M to $1.8M a year of shares withheld for taxes on vesting (cash-flow statements). The
  buyback line, written back from Q7: there is no buyback programme to test against the bottom of the range ($22.60 central);
  had there been one at prices of $43 to $72 (the year-end closes 2021 to 2026), it would have been above the top of the
  range on every basis computed, which **[L1999-023]** forbids.
- **Issuance and deals**: shares outstanding 48.5M (Feb 2020 cover) to 61.8M (2026 cover), about 27%, through the ATM at
  roughly $43 to $59 a share (proceeds over shares added, cash-flow statements and covers). By the rule of issue, "only when
  we receive as much in business value as we give" **[R1995-010]**, stock sold above the Q7 range (as every ATM sale was) did
  not transfer value away from continuing holders on this run's valuation; the habit itself is the candidate second STOP,
  "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**, unresolved in the framework and
  weighed here as against: the issuance is the funding model, stated in the 10-K, not an event. No all-stock deal: the
  Nexus purchase ($218.0M) and the BVRT minority ($45.0M) are for cash, debt and stock raised, so the STOP of **[L2009-019]**
  does not apply.
- **Part B, pay, board, owners**: chairman and chief executive combined since 2023, with a lead independent director
  **[L2014-026]**; pay benchmarked to a peer group with a consultant, the ratchet **[M2012-095]**, **[L2005-015]**; the 2025
  bonus paid in a down year; short-term goals partly operational, and the committee itself says results are "substantially
  dependent upon CPUC regulation" and therefore ties pay to "factors that are within the officers’ control" (proxy), which is
  the rows' principle **[M2003-019]**.
- **WEIGHS AGAINST.** Part A: retention fails on both legs **[M1998-110]**, a ratio dividend funded by new stock
  **[M2000-051]**, serial issuance weighed against **[L2014-015]**; no undervalued all-stock deal **[L2009-019]**. Part B:
  mildly against (combined chair, peer ratchet) **[L2014-026]**, **[M2012-095]**, with pay tied in part to what the officers
  control **[M2003-019]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**; the rate is the long government bond **[M1996-025]**: 5.30%.

**Basis.** Cal Water, the deciding part, earns a return the CPUC allows on its invested capital, so the central figure is
the equity-only basis, with the long-term debt raised for the fixed assets credited against the growth spending it funded
(Q7, The regulated utility; the row's own exception, "the fixed-asset commitments at our regulated utilities"
**[L2017-012]**), and the all-equity figure beside.

**Owner cash** (equity-only: after interest and after the company's tax; filed cash-flow statements, $M; `owner_cash.py`):

| year | OCF | stock pay | D&A (maintenance guess) | deferred tax | capex | acquisitions | developer funds net | maintenance-only, deferred tax charged | maintenance-only, cash tax | growth spending | all spending, cash tax |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 231.7 | 6.8 | 111.6 | 25.2 | 293.2 | 5.5 | 17.5 | 85.8 | 111.0 | 169.5 | -58.5 |
| 2022 | 243.8 | 5.2 | 117.4 | 26.9 | 327.8 | 7.8 | 16.4 | 94.4 | 121.2 | 201.8 | -80.6 |
| 2023 | 217.8 | 3.0 | 123.1 | 35.6 | 383.7 | 3.0 | 11.8 | 53.4 | 89.0 | 251.8 | -162.8 |
| 2024 | 290.9 | 3.7 | 134.1 | 40.4 | 470.8 | 1.6 | 21.0 | 110.0 | 150.5 | 317.3 | -166.8 |
| 2025 | 302.6 | 5.0 | 146.5 | 38.2 | 517.0 | 0.0 | 28.0 | 109.7 | 147.9 | 342.4 | -194.5 |
| average | | | | | | | | **90.7** | 123.9 | 256.6 | -132.6 |

Definitions (CONVENTIONS of this run, each with its rationale): maintenance-only owner cash = operating cash flow less stock
pay, less depreciation and amortization as the maintenance guess **[M1998-127]**, **[M2000-144]**, less net purchases of
life insurance (the SERP funding, a cash cost); growth spending = utility plant spending plus acquisitions, less the
developers' advances and contributions net of refunds (developer-funded plant is paid for by developers, 10-K Item 1), less
the maintenance guess; working capital stays inside operating cash flow (specific (d)); PFAS settlement proceeds are left
out, being held for customers as contributions (10-K Note 4). **Deferred tax charged in the central case**: the deferral from
accelerated tax depreciation is passed to customers through the rate base, "that helps our customer and it doesn’t help us"
**[M2015-030]**, so the owner is not credited with it; the cash-tax figure is shown beside. Rationale: by analogy with the
framework's own rule for tax shelters (statutory rate, shelter valued separately), with the row saying this shelter's value
to the owner is small.

**The specifics.** (a) Window 2021 to 2025: the end years are not aberrational on the filer's description (2023 and 2024
are, the 2021 rate case moving $64.0M of 2023 income into 2024, and both sit inside the window, where they offset); the
literal window is the central one. (b) No decline: growth shown 6.34% a year on the central series (85.8 to 109.7), 7.44% on
the cash-tax series. (c) Acquisitions are inside growth spending; net purchases ($18M over the window) are far below half of
owner cash, so not a serial acquirer; the signed, unclosed deals are beside. (d) Working capital counted. (e) Central case
maintenance-only, with growth spending charged against the growth it buys, grown at the carried rate for ten years and
stopped: **growth spending $272.8M in year one, $474.3M in year ten, none after**. (f) The cap: carried ten years, 6.34%
growth on the central series would need owner cash of 9.3% of sales in year ten (sales at their own 6.04% growth, 2021 to
2025), under the highest share in the window (11.1%, 2022); no cut. **Utility debt credit**: long-term debt including
current maturities and finance leases rose from $791.4M (2020) to $1,476.2M (2025), **$137.0M a year**; credited against
growth spending only, capped at **46.6%** of it (Cal Water's authorized debt share, 10-K 2025 Item 1; Cal Water carries more
than half of the deciding part's rate base, so its stated share sets the cap) = $119.6M a year (year one $127.1M, year ten
$221.0M), growing and stopping with the growth spending.

**The range, central (equity-only, deferred tax charged, debt credit), at 5.30%:** no-growth case (maintenance-only owner
cash $90.7M for ever) **$27.66** a share; growth case (owner cash grown 6.34% for ten years, less growth spending net of the
debt credit, then flat) **$22.60** a share. The growth case is below the no-growth case: the growth bought is worth less than
its cost at the sovereign, "growth can destroy value if it requires cash inputs in the early years [...] that exceed the
discounted value of the cash that those assets will generate in later years" **[L2000-023]**; the maintenance-only no-growth
case is the top and the growth case the bottom (specific (e)). **Value range $22.60 to $27.66 a share against $47.82.**
Width 1.22 to one.
- Beside, cash tax (deferred tax not charged): $37.81 (no growth) to $43.88 (growth) at 5.30%.
- Beside, all spending deducted: owner cash negative on average ($-132.6M cash tax, $-165.9M deferred tax charged); no
  positive value at any rate.
- Beside, all-equity basis (owner cash before interest, after-tax interest $36.2M added back; net debt $1,634.1M at
  2026-06-30: long-term debt $1,471.9M, current maturities $0.6M, short-term borrowings $205.0M, less cash $43.4M; restricted
  cash $45.7M left out; operating leases left out; the October 2026 notes and bonds refinance existing debt and are not yet
  issued): $12.28 (no growth) to $-6.71 (growth at sales growth, no debt credit), deferred tax charged; $22.43 to $9.78 on
  cash tax.
- Beside, the signed unclosed deals (Nexus $218.0M; BVRT minority, $34.2M unpaid of $45.0M): no filed record of either
  target's earnings; with the financing added and nothing credited, about $-4.08 a share on every figure.

**Closes. The floor is tested first** **[M2003-149]**: at $47.82 no case earns ten percent. The central no-growth case yields
3.07% on the market value ($90.7M on $2,957.1M), the cash-tax variant 4.19%; every growth case is worth less at ten percent
than at the sovereign ($4.20 central, $13.97 cash tax). The price is also above the top of the range on every basis computed,
the most generous ($43.88: cash tax, the growth case, the debt credit) included, which closes OUT however wide the range.
"there’s just a point at which we drop out of the game" **[M2003-149]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** central **$9.43** a share (equity-only, the regulated
  utility basis, deferred tax charged: no-growth case at ten percent $14.66, growth case $4.20, averaged), after the company's
  own tax. Beside it, the all-equity figure is **not positive ($-17.68)**. On cash tax: $17.01 equity-only, $-10.91
  all-equity. No cheap price is reported.
  Growth spending (above maintenance) $272.8M in year one, $474.3M in year ten, none after (specific (e)). Utility debt
  credit: long-term debt increase $137.0M a year, against growth spending only, cap 46.6% (the deciding part's allowed share,
  Cal Water, stated in the 10-K).
- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case **[M2003-149]**; the price sits above the
  whole range **[L2013-012]**; and nothing here screams **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7.** Value range $22.60 to $27.66 a share (central: equity-only, regulated-utility basis, deferred tax charged,
debt credit) against $47.82; no case earns the floor at the price (best: 4.19% on the no-growth cash-tax case); fair price
$9.43 equity-only, all-equity not positive. Q1 IN, Q2 IN on the regulated exception, Q3 weighs against, Q4 IN and weighs
against mildly, Q5 IN on integrity, Q6 weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
**Q8 (the alternatives).** The sovereign the business must beat is 5.30% (Treasury, 2026-10-27); the best yield computed on
the business at the price is 4.19% (Q7). Source: Q7 above.

**Q9 (debt and exposures)** **[M1997-127]**:
- Debt at 2026-06-30: long-term $1,471.9M, current $0.6M, short-term borrowings $205.0M; cash $43.4M (10-Q). Capitalization
  53.5% equity, 46.5% long-term debt at 2025 (10-K Item 7). Covenants: debt to total capitalization not above 66.7% and
  interest coverage of three or more (credit agreements' definitions); at 2025 the ratio was 48.8% and coverage "greater than
  five to one" (10-K Item 7). On pre-tax earnings over interest, 2025: (net income $127.8M + income tax $19.1M + interest
  $70.4M) / $70.4M = about 3.1 times (XBRL facts; the 10-K's coverage is on its own definition).
- Maturities: none of the $1,474.2M of long-term debt matures in the next twelve months (10-K Item 7A); Cal Water's revolver
  borrowings must be repaid within 24 months by CPUC order; lines of $400M (Cal Water) and $200M (Group) (10-K Item 7). The
  8-K of 2026-10-15: $275M of new notes and bonds at 6.08% to 6.54%, to refinance.
- Sudden demands: no derivatives or hedges (10-K Item 7A); the revolvers are bank lines that must be renewed.
- Exposures: inverse condemnation in California, strict liability "even when damage occurs through no fault of the utility",
  with lawsuits from Rancho Palos Verdes land movement pending and others anticipated; wildfire and firefighting-water claims
  named; insurance may not suffice (10-K Item 1A). 91.2% of revenue in one state (Item 1A). PFAS compliance capital about
  $269.1M, partly offset by manufacturer settlements ($40.9M received in 2025). Purchased water 30.5% of operating costs, with
  wholesale prices rising 7.6% to 8.6% in several districts in 2026 (Item 1 table), passed through by offset filings.
- The "little or no debt" criterion **[R1997-001]** is stated for whole businesses; not applied to a part-interest (Q9 text).

**Q5 (integrity):** none beyond those already judged at Q5 (no integrity facts left unjudged).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; Q1 written and committed before the rest; Q2 to Q7
      were drafted together after the owner-cash computation they share was built, then committed one question at a time;
      the commits are in the log (a partial departure from write-early, stated).
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` opened, listed or searched; contamination declared at the top.
- [x] Every v5 id resolves (`check_ids.py` in the research folder); every filing fact has its accession; numbers carry a
      filing or a CONVENTION label.
- [x] The order was kept; Q7 closed the run; nothing after it is a clearance.
- [x] Owner cash built from the filed cash-flow statements after stock pay and depreciation, never a net-income proxy;
      the sovereign from the Treasury; the price and the year-end closes are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` produced no arithmetic for this filer; nothing it prints was used.
- [x] `python tools/check_framework.py` PASS before the final commit (see the commit log).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Deferred taxes in a utility's owner cash.** Q7 says owner cash is after "the company's own income tax" and prices a
carryforward shelter separately, but says nothing of the deferral from accelerated tax depreciation, which for a growing
utility is a permanent-looking 11% to 16% of operating cash flow here and which the regulator hands to customers by
deducting it from rate base. The choice moves the central range by about $10 to $21 a share (central $22.60 to $27.66
against $37.81 to $43.88). I charged it centrally on **[M2015-030]** and showed both; the box is the same either way, but a
utility near the line would be decided by an unwritten choice. (2) **Developer-funded plant.** The utility rule credits
long-term debt against growth spending but is silent on refundable developer advances (interest-free, refunded over 40
years) and non-refundable contributions; I netted them out of growth spending as funding the business did not provide, a
CONVENTION of this run. (3) **The cap on the debt credit** reads "capped at the allowed debt share of the deciding part"; I
read it as that share of the growth spending, which is the only reading under which a share can cap a flow; the text should
say so. (4) **The retention test when the company sells stock.** The rows test a dollar retained; this company retains
little and raises much. I counted retained and raised dollars together against the change in market value, which is the
owner's view of the same test, and said so. (5) `tools/run.py` cannot read a filer that tags capital spending as
`PaymentsToAcquireWaterAndWasteWaterSystems`, and every water utility may do so; the run was done by hand.
