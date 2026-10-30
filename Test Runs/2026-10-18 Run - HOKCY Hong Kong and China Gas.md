# Company Run — The Hong Kong and China Gas Company Limited (SEHK: 0003; OTC ADS: HOKCY) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (this name files no
SEC annual report, so the document and its HKEXnews date stand in place of an accession); a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch
(commit 1cf8e222).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (9f25ca82): `PORTFOLIO.md` read for this one ticker; the operator does not hold HOKCY (no line names HOKCY, 0003, Towngas or Hong Kong and China Gas).*

**Contamination, declared as found and not used.** (1) A directory listing of `Test Runs/` made at the start to check the
dated file names showed the names of ten other run files dated 2026-10-15 and 2026-10-16 (FET, ACM, AER, AMMX, CTBG,
ENYN, GATX, GBX, HMH, HRI); none was opened. (2) The session context showed recent commit subjects for an XNGSY run
(ENN Energy Holdings), including its box, its value range in RMB and an RMB sovereign figure. ENN Energy is one of the
rivals this run reads at Q2; every ENN figure below is from ENN's own Annual Report 2025, and the RMB sovereign figure in
that subject line is not used anywhere in this run (I dropped an RMB sensitivity line for that reason). (3) The session's
memory index carried one-line summaries of the queue state; not used. No other run file, holding review, `PORTFOLIO.md`
or blind-listed file was opened, listed or searched.

**Research folder:** `Test Runs/_research 2026-10-18 HOKCY/` (notes, scripts; the filings themselves in its gitignored
`cache/`). The arithmetic is in `scripts/owner_cash.py`, every input typed from the filed statements named below.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** HK$7.215 a share, close 2026-10-16 (Friday; the last trading day before this run), SEHK 0003, from the
  Yahoo Finance chart feed. **Aggregator, flagged** (operator rule 5: live quote only). The ADS HOKCY closed US$0.86 the
  same day on the same feed, thinly traded; at the exchange rate below one share is US$0.919, so the ADS trades near one
  share's worth, consistent with the ratio.
- **ADS ratio:** each American Depositary Share represents **one ordinary share**, per the depositary's Form F-6EF filed
  2007-07-13 (accession 0001144204-07-036452, "each American Depositary Share representing one ordinary share of The Hong
  Kong and China Gas Company Limited"). The SEC record for CIK 0000810039 holds only that F-6EF and paper 12g3-2(b)
  submissions to 2010. No later F-6 amendment was found in the EDGAR submissions list.
- **Shares:** 18,659,870,098 ordinary shares issued and fully paid at 30th June 2026 and at 31st December 2025 (Interim
  Report 2026, note 14, Share Capital; the weighted average for the half year is the same figure, note 9). No treasury
  shares are reported by the Company. `python Screens/cover_shares.py HOKCY` returned "NOT AN SEC REGISTRANT"; the count is
  from the interim report, cross-read against Annual Report 2025 (same count) and the bonus-share history (last bonus issue
  2021: 888,565,242 shares, one for every twenty; Annual Report 2021, share capital note; none since).
- **Market cap:** 18,659.87M × HK$7.215 = **HK$134,631M** (US$17,155M at the rate below).
- **Exchange rate:** HK$1 = US$0.12742 (Yahoo feed, 2026-10-16/18, **aggregator, flagged**). The HKMA's own daily
  release of 2026-10-16 confirms the Linked Exchange Rate band of 7.75 to 7.85 HKD per USD (HKMA API, daily figures of
  interbank liquidity, "cu_strongside 7.75, cu_weakside 7.85"); the aggregator rate, 7.848, sits inside it.
- **Earnings currency, and why:** **the Hong Kong dollar.** The Company reports and pays its dividend in HK dollars. On the
  filer's own operating-profit line (segment adjusted EBITDA less depreciation and amortisation, before the share of
  associates and joint ventures), the Hong Kong utility segment earned HK$22,911M of the group's roughly HK$43,000M over
  2021 to 2025, more than half (Q2's parts table). The mainland part, which earns in renminbi, is larger only when the
  equity-accounted shares are added in, and the framework counts equity-method income as the dividends received (Q4,
  Equity-method income). I judge the HKD the earnings currency and say so as the run's own reading; the box does not turn
  on it (Q7 shows the floor test is independent of the sovereign).
- **Sovereign for the earnings currency:** **4.246%**, the annualised yield at the average accepted price (97.27) of the
  re-opening tender of the **20-year HKD HKSAR Institutional Government Bonds**, 22 July 2026, published by the Hong Kong
  Monetary Authority (press release 2026-07-22, "Results of 20-year HKD HKSAR Institutional Government Bonds tender through
  re-opening"). This is the longest HKD government tenor and the latest print of it the issuing authority has published
  that I could reach. **What I could not get:** the HKMA's daily indicative-yield API for institutional government bonds
  refused every request from this machine (HTTP 405, a firewall block), so no October print of the 20-year was read. The
  nearest October print from the same authority is the 10-year HKD bond (maturing 24 July 2035) at an indicative 3.986% on
  14 October 2026 (HKMA press release 2026-10-14). `python tools/sources.py` covers USD, JPY and EUR only and was not used.
- **Filings read** (operator rule 4; HKEXnews dates in place of accessions): Annual Report 2025 (HKEXnews 2026-04-28,
  file 2026042801254; also towngas.com), Annual Report 2024 (2025-04-23, file 2025042300667), Annual Report 2023
  (2024-04-23, file 2024042300494), Annual Report 2022 (2023-04-24, file 2023042400563), Annual Report 2021 (2022-04-20,
  file 2022042000719), Annual Report 2020 (2021-04-21, file 2021042100496), Annual Report 2019 (2020-04-21, file
  2020042100391), Annual Report 2017 (2018-04-23, file ltn20180423372), and the Interim Report 2026 (towngas.com,
  e_2026-interim-report.pdf, six months to 30th June 2026). The older reports on towngas.com returned 404 and were taken
  from HKEXnews. There is no proxy statement in the US sense; the annual report's directors' report, corporate governance
  report and note 12 (directors' emoluments) were read in its place.
- **One figure cross-checked against the filed statement:** the borrowings at 31st December 2025, HK$16,828.7M current and
  HK$42,871.9M non-current on the Consolidated Statement of Financial Position (AR2025 p.117-118), total HK$59,700.6M,
  equal to the closing borrowings in the reconciliation of liabilities from financing activities, note 40(b) (HK$59,700.6M).
  The ten-year table's 2025 net assets (HK$71,389.3M) also equal the statement of financial position.
- `python tools/run.py HOKCY`: "HOKCY: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." Nothing usable; every
  number below is from the annual reports.

**Owner cash after every real cost, by year (HK$M)**, as defined at Q4 and built in `scripts/owner_cash.py`: cash from
operations (after tax paid; interest paid sits in financing in these statements) plus dividends received from associates,
joint ventures and securities, less purchases of property, plant and equipment, right-of-use payments and intangibles net
of disposal receipts, less lease principal and lease interest, less dividends paid to non-controlling shareholders:

| | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr avg |
|---|---|---|---|---|---|---|
| Owner cash before interest, purchases of businesses left out ("organic") | 3,162 | 2,259 | 3,340 | 4,128 | 6,447 | 3,867 |
| Net purchases of businesses, associates, JVs, less sales of them and of minority stakes | 5,238 | (20) | (3,704) | (1,136) | (1,147) | (154) |
| Owner cash before interest, purchases deducted ("default") | (2,076) | 2,279 | 7,044 | 5,264 | 7,594 | 4,021 |
| Capital spending, net | 8,270 | 8,227 | 8,288 | 6,344 | 5,106 | 7,247 |
| Depreciation and amortisation | 3,289 | 3,525 | 3,549 | 3,568 | 3,803 | 3,547 |
| Interest paid, incl. perpetual securities | 1,755 | 1,741 | 2,088 | 2,293 | 1,955 | 1,966 |

Stock pay: share-based payments are expensed in the accounts (HK$63.9M in 2025, AR2025 note 40(a)) and the incentive
payments to directors are settled in options and shares of a subsidiary (note 12(a)(v)); immaterial against the figures
above and inside cash from operations as the cash part of pay.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety as an attitude: a utility whose dividend has been held at
HK$0.35 while earnings per share sat between HK$0.27 and HK$0.33 looks like a bond to many holders, and "the market is
there to serve you and not to instruct you" **[M2006-077]**, so the price's own record says nothing about value. A share
is a business **[M1997-109]**: the question is what the gas pipes in Hong Kong and on the mainland will pay out. No macro
view enters **[M2000-094]**; the Hong Kong dollar's peg and the renminbi are taken as they are, and a currency holding is
"a bet on how government now, and in the future, will behave" **[M2011-025]**, which this run does not make.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the Company's own chairman's statement features
"after-tax operating profit" and "core operating profit" (HK$7.5bn and HK$6.0bn for 2025) above the HK$5,688M
attributable profit (AR2025, chairman's statement); (2) shareholders' funds were HK$60,438.8M in 2017 and HK$59,351.1M in
2025 while borrowings rose from HK$36,918.8M to HK$59,700.6M (ten-year table; balance sheets); (3) dividends paid
(HK$6,531.0M a year since 2022) exceeded attributable profit in every year 2021 to 2025; (4) Hong Kong town gas volume
fell from 29,550 million MJ (2018) to 27,181 million MJ (2025) while customers rose; (5) the fixed-price Australian gas
contract that the Company credits with HK$20 billion of savings to customers was signed in 2003 for 25 years, with supply
from 2006 (AR2022, chairman's statement), so it ends inside the ten-year horizon; (6) the chairman's private funds hold
shares in EcoCeres, Inc., in which the Group holds an interest (Interim Report 2026, disclosure of interests, notes 9 and 10).

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money and no borrowing puts the buyer at no risk of ruin from this
name; "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and the rule binds the buyer's conduct
**[M2012-081]**, not the target's. The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the filing.** Note 5 of AR2025 reports three product segments, the first split by
  geography: (a) gas, water and waste treatment, renewable energy, extended and related businesses, Hong Kong (revenue
  HK$11,508.9M, adjusted EBITDA HK$5,795.3M in 2025) and Chinese mainland (HK$41,489.9M, HK$6,163.4M, plus shares of
  associates HK$1,263.5M and joint ventures HK$593.1M); (b) Green Fuels (HK$396.2M revenue; loss after depreciation and
  equity shares); (c) property (an associate's share of the International Finance Centre complex, HK$336.0M in 2025).
  The Hong Kong business is the town gas monopoly network serving 2,056 thousand customers; the mainland business is
  city-gas concessions, held largely through Towngas Smart Energy (about 70.11% owned after the scrip allotment of 14th
  July 2026, Interim Report 2026, disclosure of interests note 6) and equity-accounted city-gas companies, with 44,265
  thousand customers and 36,348 million m3 sold in 2025 (ten-year table).
- **The key variables and whether they are foreseeable** **[M1998-044]**: for Hong Kong, gas volume, customer count and
  the standard tariff, set by the Company and adjusted at intervals (4.4% from 1st August 2022, AR2022; again from August
  2024, AR2025 Financial Review), with fuel cost passed through by a fuel cost adjustment (HK$1,062.0M in 2025, note 5);
  for the mainland, volume, the dollar margin under the government's cost pass-through mechanism ("Price adjustments for
  industrial and commercial customers are now largely complete, while 90% of residential users have either implemented or
  confirmed their adjustment plans", AR2025 chairman's statement), and new-household connections, which the filer ties to
  the property market (gas connection income HK$2,897.4M in 2024, HK$2,202.8M in 2025, note 5). These are slow-moving
  utility variables, not technology. The past statements tell me a good deal about the future ones **[M2008-033]**.
- **Routing.** No fast-changing technology closes it here **[M1998-008]**. It is a holding company read by its parts
  (Q1's holding-company paragraph; the parts that matter are the two gas businesses, Q2's table). Green Fuels and
  renewables are small and do not decide.
- **Abroad.** The two parts sit under Hong Kong and PRC governance and tax; the speakers do business "where we think we
  understand the nuances of the corporate governance system and taxation" **[M2000-141]**, and for China "We wanted to get
  paid more for going into China, and we did, because we don’t know the game as well there." **[M2006-021]**. The answer
  the rows give to an understood business abroad is a lower price, not a pass; this is carried to Q7 as a reason for the
  margin, not used here.
- **Doubt.** The mainland pricing regime is a policy variable, and "if you have doubts about something being into your
  circle of competence, it isn’t." **[M2002-092]**. My reading: the direction of the regime is written in the filing
  (cost pass-through being completed; connection fees falling with property), and the economics of a city-gas pipe
  concession in ten years are foreseeable in kind, with the dollar margin the uncertain figure. That is a question of how
  sure the cash is, which Q7 carries, not of whether the business can be understood.
- **VERDICT: IN.** A gas distribution utility in two jurisdictions whose earning power is foreseeable in kind for ten years
  **[M2000-037]**, **[M2012-065]**; the holding is read by its two gas parts.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (five-year operating profit, HK$M, 2021 to 2025, latest-restated figures; operating profit = segment
adjusted EBITDA less depreciation and amortisation; the share of associates and joint ventures shown separately, because
Q4's equity-method convention counts it as dividends received):

| Part | Operating profit 2021-25 | Share of 5-yr total | With equity-method shares added | Share | Castle |
|---|---|---|---|---|---|
| Hong Kong gas, water and related | 22,911 | about 53% | 22,911 | about 43% | standing; narrowing slowly |
| Chinese mainland gas, water, renewables | 19,540 | about 45% | 27,852 | about 52% | standing on exclusive concessions; returns regulated and falling |
| Green Fuels / New Energy | 822 | about 2% | 731 | about 1% | does not decide |
| Property | 183 | under 1% | 2,614 | about 5% | does not decide |
| Other segments | (501) | | (519) | | does not decide |

Sources: note 5 of AR2025 (2025, 2024 restated), AR2024 (2023 restated), AR2023 (2022), AR2022 (2021). On the filer's
operating-profit line **Hong Kong carries more than half and decides**; with the equity-accounted shares added in, the
mainland carries just over half. Because the two readings name different deciding parts, I read both castles and the file
closes on them together (a CONVENTION of this run, below).

**Hong Kong town gas.**
- *The attacker with money.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
  it?" **[M2011-015]**. A second town gas network under Hong Kong's streets is not a plausible build; the substitute is
  not a rival pipe but electricity (CLP and HK Electric) and LPG. The rows warn that "one competitor is frequently enough to
  ruin a business." **[M2012-108]**; here the competitor is a different energy, sold by regulated utilities.
- *Pricing power and the agony.* "you can almost measure the strength of a business over time by the agony they go
  through in determining whether a price increase can be sustained" **[M2005-020]**. The filing shows the agony plainly:
  the 2022 rise was "For the first time in three years ... after delaying the increase by one year owing to the epidemic",
  4.4%, with a 50% concession kept for about 50,000 needy customers (AR2022). Through the inflation of 2021 to 2023, the
  fuel cost was passed through by the fuel cost adjustment, and the business's margin held: Hong Kong adjusted EBITDA
  HK$4,886.0M (2021), HK$5,186.1M (2022), HK$5,852.6M (2023, restated), HK$5,526.3M (2024, restated on the 2025 basis),
  HK$5,795.3M (2025). "over time the businesses with strong competitive positions manage to pass through increases in raw
  material costs" **[M2005-017]**: this one did.
- *Unit volume and share of mind.* Volume fell: 29,550 million MJ (2018), 28,712 (2019), 27,947 (2020), 27,677 (2021),
  27,398 (2022), 27,125 (2023), 27,159 (2024), 27,181 (2025); customers rose from 1,909 thousand to 2,056 thousand (ten-year
  table). Volume per customer is falling; the total has been flat since 2022.
- *Low cost and the customer's choice.* The Company's 2003 contract for Australian gas at a price "equivalent to US$25 per
  barrel of crude oil", supplied from 2006, is credited with saving customers "over HK$20 billion in fuel costs" (AR2022,
  chairman's statement). The saving goes to the customer through the fuel cost adjustment, which keeps town gas
  competitive with electricity; a 25-year contract signed in 2003 ends by about 2028 to 2031 on the filer's own dates.
- *Widening or narrowing.* "how wide the moat is and whether it’s likely to widen further or shrink on you" **[M1999-108]**.
  Narrowing, slowly: falling volume per customer, Hong Kong's carbon target named in the Company's own reports ("Hong
  Kong’s Climate Action Plan 2050", AR2022), and the end of the fixed-price gas contract. "slow change can be much harder
  to perceive" **[M2014-038]**. Against it: the network is the only one, the tariff has been raised without volume falling
  off a cliff, and segment returns are high (below).
- *What could destroy it, five to fifteen years out* **[M2000-014]**: electrification of cooking and water heating under a
  decarbonisation policy. The Company's answer in its reports is hydrogen in the town gas mix and landfill biogas
  (AR2025, risk factors). This is a twenty-year threat more than a ten-year one, on the filer's evidence.

**Chinese mainland city gas.**
- The castle is a set of local exclusive concessions: inside a concession there is no second pipe. The attacker competes
  for new concessions and new industrial customers, not for the installed household. The return is set by price
  regulation and the cost pass-through mechanism the chairman describes (AR2025). Q2's list sends a return set by a
  regulator to Q3 as a second best rather than to OUT, on the rows' own utility verdict: "there’s no way we get rich on
  our utility investments. But there’s no way we get poor, either." **[M2009-104]**; **[L2009-012]**.
- Narrowing: connection income fell from HK$2,897.4M (2024) to HK$2,202.8M (2025) with "the ongoing downturn in the
  mainland property market" (AR2025 Financial Review); an impairment of HK$178.3M in 2024 was "primarily due to
  under-performance with decline in future cash flows of city-gas projects in the Chinese mainland" (AR2025 note 7). The
  regulated-utility mistake the rows narrate applies in kind: "I did not anticipate or even consider the adverse
  developments in regulatory returns" **[L2023-011]**.

**The competitor row** (CONVENTION of this run, below: the annual report names no rival; I chose them). None files an
annual report with the SEC; all publish their own on HKEXnews.

| Rival (document) | Metric, 2021 → 2022 → 2023 → 2024 → 2025 |
|---|---|
| ENN Energy Holdings (Annual Report 2025, HKEXnews 2026-04-28; ten-year results, RMB) | Profit for the year / net assets: 21.3% → 14.6% → 16.0% → 13.5% → 12.6%; residential + C/I piped gas volume 24.6 → 25.7 → 24.9 → 26.0 → 26.4 bcm |
| China Resources Gas Group (2025 Annual Report, HKEXnews 2026-04-30; five-year summary, HK$) | Profit for the year / total equity: 15.6% → 12.0% → 11.1% → 9.0% → 7.5% |
| HK Electric Investments (Annual Report 2025, HKEXnews 2026-04-20; five-year summary and Scheme of Control statement) | Permitted return fixed at "8% of average net fixed assets" under a Scheme of Control to 2033; operating profit HK$4,845M → 4,509 → 4,976 → 5,488 → 5,048 on property, plant and equipment of HK$76.7bn to 80.1bn (about 6% pre-tax) |
| HKCG consolidated (ten-year table) | Profit for the year / total equity: 7.6% → 8.4% → 10.1% → 9.9% → 9.4% |
| HKCG Hong Kong segment (note 5) | Operating profit / segment assets, 2025: HK$4,934.5M / HK$22,778.2M, about 22% pre-tax |
| HKCG mainland segment (note 5) | Operating profit with equity shares / segment assets, 2025: HK$5,439.3M / HK$103,919.6M, about 5% pre-tax |

Named rivals that do not file with the SEC: all of them; CLP Holdings and Kunlun Energy were not read (a choice to keep
the row to three, said so).

**The field's returns over the last full cycle, judged in words.** On the mainland the field's returns fell for four years
running at both large rivals, and HKCG's mainland part earns about five percent pre-tax on its segment assets: ordinary
returns, under a regulator, and narrowing. In Hong Kong the town gas network earns a high return on the capital in it,
far above the regulated electricity utility next door, with pricing power shown through the last inflation. A moat
"protects excellent returns on invested capital" **[L2007-004]**: the Hong Kong part has excellent returns protected; the
mainland part has a standing castle with ordinary, regulated returns, which Q2 sends to Q3 as a second best rather than
OUT **[M2009-104]**.

**CONVENTION of this run (two parts, two deciders).** Where the filer's operating-profit line makes one part the decider
and the same line with equity-method shares added makes another, both are read and the file closes on the two together:
OUT only if both are open, TOO HARD if either deciding castle's future cannot be judged. Rationale: the parts paragraph
names "operating profit" without saying whether equity-accounted shares are in it, and choosing the reading that suits a
box would be choosing the box.

- **VERDICT: IN.** The Hong Kong castle stands on a single network with pricing power shown through the last inflation,
  narrowing slowly **[M2005-020]**, **[M1999-108]**; the mainland castle stands on exclusive concessions at a regulated,
  falling return, carried to Q3 as a second best **[M2009-104]**. Neither is shown open on the evidence **[M2011-015]**,
  and neither future is beyond judging at ten years; the narrowing on both is carried to Q7's certainty, since the moat
  enters "the degree of certainty that we attribute to the stream of income" **[M1999-104]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**. Hong Kong: operating profit HK$4,934.5M on segment assets of
  HK$22,778.2M in 2025, about 22% pre-tax, with segment assets of HK$18.5bn to HK$22.8bn across 2021 to 2025 (note 5 of
  each report): a high return on a modest base. Mainland: operating profit with equity shares HK$5,439.3M on segment assets
  of HK$103,919.6M in 2025, about 5% pre-tax, and about the same in each year read. The whole: profit for the year of
  HK$6.2bn to HK$7.2bn on total equity of HK$68bn to HK$82bn (ten-year table), 7.6% to 10.1%.
- **Reinvestment to stand still and to grow.** Capital spending, net, was HK$36,235M over 2021 to 2025 against depreciation
  and amortisation of HK$17,734M (owner-cash table): about twice depreciation for five years. "Every year we spend amounts
  equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**; the rest was meant to grow.
- **What the added capital earned.** Over the eight years 2017 to 2025, property, plant, equipment and right-of-use assets
  rose from HK$58,056.7M to HK$73,998.8M and associates from HK$23,393.4M to HK$39,556.1M; borrowings rose from HK$36,918.8M
  to HK$59,700.6M; and profit attributable to shareholders went from HK$8,225.3M (2017) to HK$5,688.2M (2025), with revenue
  growth of 0.35% a year in HK dollars over 2021 to 2025 (ten-year table). Mainland operating profit on the filer's line
  fell from HK$4,724.0M (2021) to HK$3,582.7M (2025). This is the third grade of the 1998 passage: "reinvesting the capital at
  a very low rate of return" **[M1998-081]**, or at best the utility of 2023, "we’re not earning a higher rate of return on
  capital than we were when we started. We just put way more capital into the business" **[M2023-081]**. The diversification
  spending (new energy, a chemical production project, renewables) produced impairments and a restructuring in 2023
  (Q4) rather than earnings.
- **The second best.** The mainland is a regulated, capital-heavy business of the kind the rows accept when "these
  businesses have reasonable expectations of earning decent returns on the incremental sums they invest" **[L2009-012]**;
  "cash-consuming businesses, by their nature, are unattractive unless the cash they consume gets to earn a reasonable
  return" **[M2012-057]**. The incremental sums here have not earned a decent return on the record read.
- **Growth arithmetic and its caps, for Q7.** Volume grew on the mainland (31,080 to 36,348 million m3, 2021 to 2025) and
  customers grew in both places, but revenue in HK dollars was flat and organic owner cash grew mainly because capital
  spending fell (HK$8,270M in 2021 to HK$5,106M in 2025), not because the business earned more. Q7's cap applies.
- **WEIGHS AGAINST.** A small, high-return Hong Kong network carries a large mainland and diversification book that has
  absorbed about twice depreciation for five years at a low return, and earnings per share are lower than eight years ago
  **[M1998-081]**, **[M2023-081]**, **[M2012-057]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, 2016 to 2025** **[M2025-032]** (ten-year table of AR2025, cross-read with the
  balance sheets of AR2017, AR2019, AR2021, AR2023 and AR2025):

| HK$M | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| PPE and right-of-use | 51,226 | 58,057 | 60,193 | 63,808 | 70,936 | 75,160 | 74,632 | 73,417 | 72,648 | 73,999 |
| Associates | 20,485 | 23,393 | 26,314 | 27,476 | 28,670 | 36,150 | 34,178 | 36,064 | 36,075 | 39,556 |
| Intangible assets | 5,572 | 5,884 | 5,682 | 5,291 | 5,463 | 5,607 | 5,340 | 4,463 | 4,388 | 4,464 |
| Borrowings | 33,248 | 36,919 | 35,672 | 37,936 | 42,139 | 55,111 | 59,304 | 55,425 | 57,422 | 59,701 |
| Cash and deposits up to 3 months | 8,076 | 10,759 | 8,501 | 7,849 | 7,455 | 10,557 | 13,241 | 8,972 | 6,272 | 6,548 |
| Perpetual capital securities | 2,354 | 2,354 | – | 2,384 | 2,384 | 2,384 | 2,384 | – | – | – |
| Shareholders' funds | 53,932 | 60,439 | 62,401 | 64,209 | 66,759 | 67,426 | 61,228 | 59,853 | 57,390 | 59,351 |
| Non-controlling interests | 6,612 | 7,453 | 7,793 | 8,803 | 10,011 | 12,028 | 11,527 | 11,166 | 10,943 | 12,038 |

  *(2018 perpetual securities: the ten-year table prints a dash; I did not resolve whether they were redeemed and
  re-issued; immaterial to the box.)* What moved and why: borrowings less cash went from about HK$25bn (2016) to about
  HK$53bn (2025) while shareholders' funds rose to 2021 and then fell back to about their 2017 level; the fall after 2021
  is dividends above earnings plus exchange losses on the renminbi book. Goodwill and intangibles are small against equity
  and falling. Trade receivables moved with revenue (HK$10,662.8M on revenue of HK$60,953.4M in 2022; HK$9,881.3M on
  HK$54,326.3M in 2025), inventories with gas prices; nothing building out of line **[M1995-064]**. What the figures cannot
  say: what the renminbi concessions will be worth in Hong Kong dollars ten years out.
- **The real costs.** Depreciation is real **[L2015-004]**, and capital spending ran at about twice it. Impairments recur: a
  "Provision for assets" of HK$1,531.7M (2021), HK$240.0M (2022), HK$3,237.7M (2023), HK$178.3M (2024), nil (2025) (cash
  flow reconciliations); and in 2023 "Realised losses on an equity investment and related derivatives" of HK$1,729.4M and
  a remeasurement loss of HK$678.8M, set against a HK$4,677.2M gain on deconsolidating EcoCeres, all labelled "Business
  restructuring" (AR2023 note 7). Telling owners year after year to ignore such adjustments "is misleading"
  **[L2016-007]**; this run does not ignore them: the cash the ventures consumed is inside capital spending and business
  purchases in owner cash. Stock pay is expensed and small. The pension scheme shows a small surplus (retirement benefit
  assets HK$187.3M, AR2025).
- **EBITDA in the filer's own mouth, and the featured figures.** The segment measure is "adjusted EBITDA" (note 5), the
  chief operating decision-maker's measure. The chairmen's statement leads with "after-tax operating profit and core
  operating profit were HK$7.5 billion and HK$6.0 billion" before the HK$5.7bn attributable (AR2025). The rows: "a
  management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us
  nervous" **[L2016-006]**. A featured adjusted figure weighs against here and is carried to Q5. No earnings guidance and no
  habit of declared financial targets was found (a search of AR2025 for "guidance" and "target" found operating and ESG
  targets only).
- **Equity-method income.** Counted as dividends received (Q4's rule): HK$8,556M received from associates and joint
  ventures over 2021 to 2025 against a booked share of HK$10,634M; the dividends are in owner cash, the booked share is not.
- **What the accounts say of management's character.** They are full, consistent and reconciled; the 2023 restructuring is
  set out line by line. The accounts "can offer you a lot of insight into the character of management" **[M1995-064]**, and
  what they show here is a management that diversified and wrote part of it off, in plain view.
- **VERDICT on the accounts: WEIGHS AGAINST.** No confusion and no suspicion raised by the statements themselves, so no STOP
  **[M1994-018]**. Against: the featured adjusted figures **[L2016-006]** and the recurring "one-time" impairments
  **[L2016-007]**. The recast owner cash is the table in Step 0 and feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Two brothers, Dr. Lee Ka-kit and Dr. Lee Ka-shing, are chairmen and non-executive directors; Lee Ka-kit is also
  Chairman and Managing Director of Henderson Land Development, which with Henderson Development is interested in
  7,748,692,715 shares, 41.53% (AR2025, substantial shareholders), and chairs Towngas Smart Energy. The Managing Director
  is Peter Wong Wai-yee.
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the Hong Kong network is run well
  (margin held through the inflation; Q2); the mainland book and the diversification have earned little on a great deal
  of capital (Q3), and ENN and China Resources Gas, dealt the same mainland hand, earned more on equity in every year of
  the window (Q2's row), though both fell too. *How well they treat the owners:* modest pay for the controlling family
  (Lee Ka-kit HK$1.6M, Lee Ka-shing HK$1.3M, fees and benefits only) and HK$30.7M for the Managing Director in 2025, HK$37.4M
  in 2024 (AR2025 note 12(a)). "see how they treat themselves versus how they treat the shareholders" **[M1994-009]**: not
  greedy in pay.
- **The tells, as found.** (1) The featured "core operating profit", carried from Q4 **[L2016-006]**. (2) The chairman's
  private funds hold shares and Series B preferred shares of EcoCeres, Inc., in which the Group holds an interest after
  selling down from 65.5% to 44.2% in 2023 "to an independent investor" for US$319M (Interim Report 2026, disclosure of
  interests notes 9 and 10; AR2023 key audit matter), and the Group's food-waste business supplies used cooking oil to
  EcoCeres (AR2025 chairmen's statement). The co-investment is disclosed, and the directors' report states no significant
  transaction in which a director had a material interest (AR2025 note 12(b)). (3) Related-party banking: "one bank with a
  common director with the Company" had HK$682.6M of loans and interest payable to it at the end of 2025 (note 39(c)); the
  common director is, on the board biographies, Sir David Li Kwok-po, Executive Chairman of The Bank of East Asia and an
  Independent Non-executive Director of the Company since 1984, who chairs its Board Audit and Risk Committee and its
  Remuneration Committee (AR2025, board of directors). (4) How they talk about mistakes: the 2023 write-offs are a
  restructuring "to streamline and rationalise" with no mistake named. "That taboo, implying managerial perfection, always
  made me nervous" **[L2024-003]**.
- **Integrity, judged.** "If you’ve got doubts, forget it." **[M2013-088]**. I do not find doubt about honesty in the record
  read: the accounts are candid, related dealings are disclosed and small against the Group, the family's own pay is
  modest, and the reports read disclose no regulator's finding against the Company, no restatement and no material
  litigation (search of AR2025 for "litigation", "investigation" and "contingent"). Tells (2) and (3) are conflicts of
  structure, not shown misconduct; they are recorded for Q6 Part B and for any later run.
- **Ability.** Real in Hong Kong; poor in the capital record elsewhere (Q3). "if the CEO's talents or motives are suspect,
  today's value must be discounted" **[L2010-002]**.
- **VERDICT on integrity: IN; ability WEIGHS AGAINST** **[M1994-008]**, **[M2013-088]**, **[L2010-002]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test.** "any time we thought that we weren’t going to get more than a dollar of value per dollar
  retained, that, obviously, would be the course to follow" **[M1994-061]**; the test is assessed "over time"
  **[R1995-009]**. Over 2021 to 2025 the Company paid HK$32,451M of dividends against HK$27,735M of attributable profit: at
  the shareholder level it retained nothing and paid out more than it earned, while borrowings rose by about HK$4.6bn from
  the end of 2021. At the group level money was kept and reinvested (capital spending about twice depreciation, Q3), partly
  with minority partners' money and debt. What became of it: shareholders' funds fell from HK$67,426M (2021) to HK$59,351M
  (2025), and the share price from about HK$12.1 (September 2021) to HK$7.215 (Yahoo feed, bonus-adjusted; aggregator,
  flagged). The group-level retention fails on market value and on book value **[R1995-009]**, **[M1998-110]**. The
  dividend above earnings while debt rises is not what "dividend policy should always be clear, consistent and rational"
  **[L2012-015]** describes; the stated policy is "to allow its shareholders to participate in the Company’s profits whilst
  retaining adequate reserves for future growth" (AR2025, Dividend Policy).
- **Buybacks.** None by the Company in the years read: "neither the Company nor any of its subsidiaries had purchased, sold
  or redeemed any of the Company’s listed securities" apart from a subsidiary's share-award trustee buying Towngas Smart
  Energy shares for about HK$40.2M (AR2025). *Buyback line against the bottom of the Q7 range (written back at Q7):* no
  repurchase by the Company in the years read, so no price paid to set against the bottom of the range (HK$2.26 a share
  all-equity, HK$2.59 equity-only); the test has nothing to read, and the no-stated-price rule **[L2016-002]** does not
  arise.
- **Issuance and deals.** Bonus shares, one for ten and one for twenty, in 2017 to 2021 (AR2017 to AR2021), with the dividend
  per share held or raised, so the cash dividend grew with the count; no shares issued for value. No all-stock acquisition
  by the Company was found, so the STOP does not apply **[L2009-019]**. Subsidiaries sold minority stakes: Affinity Equity
  Partners invested HK$2.8bn in Towngas Smart Energy shares and convertible bonds in 2021 (AR2021); a subsidiary issued
  preferred shares for HK$3,393.9M in 2022 (AR2022 cash flow statement); EcoCeres was sold down in 2023. Whether those were
  sold at or above value is not knowable from the reports read.
- **Part A: WEIGHS AGAINST.** The retention test fails over the five-year span **[M1994-061]**, **[R1995-009]**, and the
  dividend above earnings is paid while the debt rises.
- **Part B, the pay, the board, the owners.** Executive bonuses and incentives are set "by the Board from time to time with
  reference to directors’ duties and responsibilities and the Group’s performance and profitability" (note 12(a)(v)): not
  tied to capital employed or to what each person controls **[M2003-019]**. The independent directors include two aged 86
  and 87 (AR2025 biographies); the one appointed in 1984 chairs both the audit and the remuneration committees and his bank
  lends to the Group (Q5). The doubt is tenure and the bank tie, not fees: the rows' test of independence is substance, not
  the label **[M2009-086]**. The owners are told the facts in full (Q4), the featured adjusted figure excepted.
- **Part B: WEIGHS AGAINST**, lightly: pay is not tied to capital **[M2003-019]**, and the independence of the director who
  chairs the two checking committees is doubtful in substance **[M2009-086]**.

## Q7 — WHAT IS IT WORTH? STOP.
**The question:** "How certain are you that there are indeed birds in the bush? When will they emerge and how many will
there be? What is the risk-free interest rate" **[L2000-021]**, with "use the government bond rate" **[M1996-025]**.

**Inputs (HK$M, five-year averages 2021 to 2025, Step 0 table; `scripts/owner_cash.py`).**
- All spending, business purchases deducted (the default pair of specific (c)): **4,021**.
- Organic (purchases left out): 3,867. Net purchases over the window were a net sale of about HK$768M, so the business is
  not a serial acquirer and the default pair stands **[M1998-080]**, **[M2014-068]**.
- Maintenance-only, depreciation as the maintenance guess, purchases left out: **7,567**. The filing states no maintenance
  figure; depreciation is the rows' proxy, "the depreciation charge is not inappropriate in most companies to use as a proxy
  for required capital expenditures" **[M1998-127]**, and it is the guess specific (e) asks for where the filing allows one
  **[M2000-144]**, **[L1999-024]**. The guess is generous: town gas pipes and mainland networks are old assets whose
  replacement costs more than their historical depreciation (the rows' warning **[L2023-009]**).
- Working capital is inside cash from operations (its increase is charged, specific (d)); no single year is tied by the
  filer to one contract or event.
- Non-controlling interests: dividends paid to minority partners are deducted from owner cash (the cash the Company's own
  owners never receive); the alternative, deducting the book value of non-controlling interests (HK$12,542.3M at 30th June
  2026) as a claim and not the dividends, is shown beside.
- Tax: owner cash is after the tax actually paid, the company's own tax (Q7, Whose tax); no carryforward shelter is
  material. The interest deduction lowers that tax by an estimated HK$324M to HK$492M a year (average interest of HK$1,966M
  at 16.5% to 25%), so the all-equity figure is slightly generous; not adjusted.

**The specifics, in order.**
- (a) Cycles: a utility, not cyclical; no first or last window year is aberrational on the filer's own description. 2021
  carries a mainland associate purchase of about HK$6.3bn and 2023 the exit from Shanghai Gas and the EcoCeres sale (AR2023
  note 7); both are inside net purchases under (c). The literal window is the window used.
- (b) Decline: the default series changes sign (−2,076 in 2021 to 7,594 in 2025); its halves (101 for 2021-22, 6,429 for
  2024-25) give a meaningless rate, so that series is valued at no growth alone, said so. The maintenance series
  (8,144; 6,960; 8,079; 6,904; 7,750) shows a decline of 1.23% a year, carried beside as negative.
- (e) Growth spending: capital spending about twice depreciation bought revenue growth of 0.35% a year and a falling
  maintenance series: "growth can destroy value" **[L2000-023]**. The growth bought is worth less than its cost, so the
  maintenance-only no-growth case is the **top** and the all-spending case the **bottom**.
- (f) The cap: the organic series' end-year rate, 19.5% a year, carried ten years would need owner cash of HK$23.9bn, 43.9%
  of 2025 revenue, against a highest share earned of 14.0%; it is cut to the business's own sales growth, 0.35% a year
  **[M1999-067]**, **[M1997-095]**. The shown rate and the cut are both written here.
- After year ten, zero nominal growth; discounted at the 4.246% HKD sovereign throughout **[L2000-021]**.
- Net debt at 30th June 2026, the latest filed date: borrowings HK$62,526.3M less cash and deposits HK$8,525.2M less current
  securities at fair value through profit or loss HK$1,444.2M = **HK$52,556.9M** (Interim Report 2026, statement of
  financial position). Lease liabilities are left out (lease payments are charged in owner cash), and so are the
  non-current investment securities (their dividends are in owner cash). No subsequent event in that report changes it.
  Enterprise value at the price: HK$134,631M + HK$52,557M = HK$187,188M.

**The floor, tested first.** About ten percent pre-tax, applied to owner cash after the company's own tax (CONVENTION, the
floor; **[M2003-149]**, **[L2002-020]**, **[M1994-004]**). Expected return at the price, all-equity basis: maintenance-only
no growth **4.04%**; maintenance-only at its own decline 3.64%; all spending at no growth 2.15%; all spending at sales growth
2.22%. Equity-only (owner cash after interest against market value): 1.53% to 4.16%. **No case earns the floor.** For the
top case to earn ten percent at this price its owner cash would have to grow about 13% a year for ten years, to about
HK$25.7bn, nearly half of 2025 revenue: the absurdity the cap forbids **[M1999-067]**. The floor test does not depend on the
sovereign or on the earnings-currency judgment.

**COMPUTATION, NOT A CLEARANCE (the range, reported by the reporting convention).**
- **Value range, all-equity (central):** whole-business value HK$94,698M to HK$178,225M; less net debt; **HK$2.26 to HK$6.73
  a share** against HK$7.215. Width 2.98 to one. Beside: all spending at sales growth HK$2.41; maintenance at its own
  decline HK$5.80; non-controlling interests at book instead of their dividends, HK$2.56 to HK$6.86.
- **Equity-only, beside:** HK$2.59 to HK$7.07 a share.
- **Fair price** (each end valued at ten percent, the two averaged, Part VII): all-equity **HK$0.29 a share**, equity-only
  **HK$2.05 a share**; per ADS (one share) **US$0.037** all-equity and **US$0.261** equity-only, at HK$1 = US$0.12742
  (2026-10-16/18, aggregator, flagged). The all-equity bottom end is negative at ten percent (owner cash of HK$4,021M is
  worth HK$40.2bn at ten percent, less than the net debt); the all-equity figure is therefore the average of a negative and
  a positive end. With non-controlling interests at book instead, the all-equity fair price is about HK$(0.02).

**Closes.** "there’s just a point at which we drop out of the game" **[M2003-149]**: no case in the range earns the floor
at the price, so the file closes OUT whatever the width (the floor tested first, Q7). The price also sits above the top of
the all-equity range, which closes OUT by the same route. Not a screamer by any reading: "It should scream at you."
**[M2009-005]**.

- **VERDICT: OUT**, on the floor **[M2003-149]**, **[L2002-020]**; the price is above every case of the range **[L2000-025]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED (Q7 closed the file).
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT, at Q7 (the floor).** Q1 IN, Q2 IN; Q3, Q4 and Q6 weigh against; Q5 integrity IN, ability against. COMPUTATION, NOT A
CLEARANCE: value range HK$2.26 to HK$6.73 a share all-equity at the 4.246% HKD sovereign against HK$7.215 (equity-only
HK$2.59 to HK$7.07); best expected return at the price 4.04% all-equity, 4.16% equity-only. Fair price HK$0.29 all-equity,
HK$2.05 equity-only; US$0.037 and US$0.261 per ADS. Integrity facts recorded and judged at Q5 (the chairman's funds in
EcoCeres; the long-serving independent director whose bank lends to the Group).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; **[M1997-127]**.)*
- **Q8.** The HKD 20-year sovereign at 4.246% (HKMA, 2026-07-22) exceeds every all-equity expected return computed at the
  price (2.15% to 4.04%).
- **Q9.** Borrowings HK$62,526.3M at 30th June 2026, of which HK$16,669.8M current (Interim Report 2026); net debt about
  HK$52.6bn against five-year average owner cash before interest of HK$4.0bn (all spending) to HK$7.6bn (maintenance);
  interest paid about HK$2.0bn a year; profit before tax HK$8,605.8M against interest expense HK$1,971.9M in 2025 (AR2025
  income statement). Related-party bank loans HK$682.6M (note 39(c)). The "little or no debt" criterion is for whole
  businesses; not applied.
- **Q10.** Nothing found.
- **Q12.** Town gas and city-gas distribution; nothing in the named-business list. Not asked.
- **For any later run:** the fixed-price Australian gas contract (2003, 25 years, supply from 2006; AR2022) ends inside the
  ten-year horizon; Hong Kong town gas volume has fallen from 29,550 to 27,181 million MJ since 2018.

## WHAT I COULD NOT GET
- An October 2026 print of the 20-year HKD government bond yield: the HKMA's daily institutional-bond API returned HTTP 405
  (firewall) to every request; the 22 July 2026 tender result and the 14 October 2026 10-year indicative (3.986%) were used
  and beside. At 3.986% the all-equity range is HK$2.59 to HK$7.36 a share; the floor test is unaffected; the box is unchanged.
- Annual reports before 2019 on towngas.com (404); taken from HKEXnews instead. The 2018 perpetual-securities dash in the
  ten-year table was not resolved. CLP Holdings and Kunlun Energy were not read.
- An exchange rate from the HKMA itself: the HKMA daily release gives the convertibility band, not a closing rate; the
  aggregator rate inside the band was used, flagged.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 1cf8e222); written question by question; committed after Q2, after
      Q3 to Q6, and after Q7 with the buyback line written back into Q6 (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (operator rule
      ten); this run binds nothing until folded into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared
      under contamination at the top: ten run-file names in a directory listing, XNGSY commit subjects (ENN Energy), the
      memory index. Nothing of them used; the RMB sovereign in a commit subject was deliberately not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (`scripts/check_run.py`: every M/L/R id found, every quoted
      fragment set directly beside an id found in that row, no E-ids). Every filing fact names its report, note or page and
      the HKEXnews date stands in for an accession; the ADS ratio has its EDGAR accession.
- [x] The order was kept: Q1 to Q6 answered, Q7 the first STOP that failed; Q8, Q9, Q10 and Q12 NOT REACHED; the range and
      fair price headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the issuing authority (HKMA), dated, with its staleness stated; the price and exchange rate from an
      aggregator, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations paragraph, and at each question).
- [x] Not a point-in-time run; no anchor rule arises.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned nothing for a non-SEC filer; nothing they print was used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit message).
- Honest gaps in the audit: the maintenance guess (depreciation) is the run's choice and is generous to the business; the
  non-controlling-interest treatment is the run's choice (two methods shown); the 2018 perpetual-securities entry was not
  resolved; mainland segment returns are on segment assets that include equity-accounted investments.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **"Operating profit" in Q2's parts paragraph does not say whether equity-accounted shares are in it.** Here the choice
   names the decider: Hong Kong carries 53% of five-year operating profit on the filer's line, the mainland 52% once the
   shares of associates and joint ventures are added. Q4's equity-method rule points one way, the segment note the other. I
   read both castles and confessed a CONVENTION of the run (both decide together). A one-line definition would settle it.
2. **Specifics (e) and (f) pull against each other.** (e) says "Never charge all spending and also cap the growth that
   spending bought"; (f) cuts any absurd rate to sales growth. The all-spending series here shows 19.5% a year only because
   capital spending fell, and (f) must cut it. I resolved it through (e)'s own inversion (growth bought worth less than its
   cost: maintenance no-growth is the top, all spending the bottom) and valued the all-spending series at no growth by (b),
   whose halves were meaningless. (b) says such a series is "the no-growth case alone", while (e) asks for a growth case as
   the bottom; the text does not say which governs.
3. **Minority interests have no rule on the all-equity basis.** Section H defines net debt but not what to do with a
   listed subsidiary's minority (about 30% of Towngas Smart Energy) or with preferred shares issued by a subsidiary. I
   deducted dividends paid to minority partners from owner cash (central) and showed book non-controlling interests as a
   claim beside; the two give fair prices of HK$0.29 and about HK$(0.02).
4. **The fair price can be negative on the all-equity basis.** When the bottom end valued at ten percent is worth less than
   net debt, Part VII's average of the two ends mixes a negative and a positive end. I reported it as computed; the text
   does not say whether an end is floored at zero (an equity holder's loss is limited, the computation's is not).
5. **The sovereign table covers USD, JPY and EUR only, and the HKD's longest government tenor is 20 years, not 30.** The
   issuing authority's daily yields were blocked; the latest tender result (July) was used with an October 10-year print
   beside. The protocol does not say how stale a sovereign may be, or what to do for a group whose parts earn in two
   currencies; I judged the earnings currency by the filer's operating-profit line and showed that the box does not turn on
   it.
