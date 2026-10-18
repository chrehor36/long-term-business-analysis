# Company Run — Algonquin Power & Utilities Corp. (NYSE and TSX: AQN) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-18, after the run was committed: `PORTFOLIO.md` read for AQN only; not held.*

**CONTAMINATION (declared as found, not used):** (1) before the template was copied, a listing of `Test Runs/` filtered on
the date 2026-10-18 showed the file names of other runs of today (AES, HOKCY, MDU, NJR, NWN, OGS, SR, SWX, UGI, XNGSY) and
their research folders; no file was opened. (2) The session's opening context showed recent commit subjects of the AES run
of 2026-10-18 (its box and computation); not used. (3) The session's memory index lines name queue state in general terms
(wave 7, gate-clearer counts); nothing about this name.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.25 (close 2026-10-16, NYSE: AQN; Yahoo Finance chart feed through `tools/sources.py` `price()`;
  **aggregator, flagged**, permitted for the live quote only, operator rule 5).
- **Shares by class:** one class of common shares. Cover of the 40-F: **768,351,419** (40-F filed 2026-03-06, period
  2025-12-31, accession `0001174169-26-000015`; `python Screens/cover_shares.py AQN`, which read the 40-F). Checked
  against the filed statements: the Q2 2026 interim notes give 768,351,419 at the start of 2026, the same. Later filing:
  the Q2 2026 interim statements (6-K filed 2026-08-07, accession `0001174169-26-000031`, note 9(a)) give
  **769,747,684** at 2026-06-30 after 1,396,265 shares issued on share-based awards; no treasury shares are reported.
  **The count used is 769,747,684**, the latest filed. The preferred shares (Series A and Series D, carried at $184.3M)
  are not common and are treated as a claim ahead of the common at Q7.
- **Market cap:** 769,747,684 x $5.25 = **$4,041.2M** (on the cover count, $4,033.8M).
- **Sovereign for the earnings currency:** the company reports in US dollars and its revenue is about 82% American
  (AIF 3.1, Regulated Services Group revenue, United States 81.66%). **USD 30-year par yield 5.43% at 2026-10-16, US
  Treasury daily par yield curve** (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the **40-F for FY2025** filed 2026-03-06, accession `0001174169-26-000015`: the
  primary document `aqunf-20251231.htm` (audited statements, EY's opinion and ICFR attestation dated 2026-03-06),
  Exhibit 99.1 the Annual Information Form (business, competitive conditions, risk factors, dividends, legal
  proceedings), Exhibit 99.3 the MD&A. The **Q2 2026 6-K** filed 2026-08-07, accession `0001174169-26-000031` (interim
  statements `aqunf-20260630.htm`, MD&A Exhibit 99.2). The **6-K of 2026-08-28**, accession `0001174169-26-000038` (the
  Suralis sale release). The **management information circular**: the 6-K filed 2026-05-20, accession
  `0001140361-26-022268`, Exhibit 99.4 (`ef20074371_ex99-4.htm`), read on EDGAR, not SEDAR+. For the cycle and the
  ten-year balance sheets: the 40-Fs for FY2024 (`0001174169-25-000020`), FY2023 (`0001174169-24-000019`), FY2022
  (`0001174169-23-000016`), FY2021 (`0001174169-22-000021`) and FY2020 (`0001174169-21-000012`), their audited statements
  read for the auditor's opinions and the cash-flow statements, and the SEC XBRL company facts of the 40-Fs FY2010 to
  FY2025 for the long table.
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 **$593.6M** in
  the filed Consolidated Statements of Cash Flows (`aqunf-20251231.htm`) equals the XBRL fact
  NetCashProvidedByUsedInOperatingActivities for FY2025 (593.6); additions to property, plant and equipment and
  intangible assets $771.9M likewise equal PaymentsToAcquireProductiveAssets (771.9).
- `python tools/run.py AQN` **failed**: it printed "AQN: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (it
  reads 10-K and 20-F facts; this filer's are 40-F). As the brief directs, every figure below is taken from the filed
  statements and from the XBRL facts of the 40-Fs (forms 40-F only, latest-filed value per year), and the arithmetic is
  done in `Test Runs/_research 2026-10-18 AQN/facts.py` and the Q7 script there. Nothing printed by `run.py` is used.
- **Lines of evidence chosen (departure 1 of the brief), and why.** From the AIF (the Item 1 equivalent): the two
  business units and their weights (Regulated Services Group 98.39% of revenue and 95.62% of assets in FY2025, AIF 3);
  the cost-of-service ratemaking in every jurisdiction (AIF 3.1.1); the competitive conditions, "geographic monopolies"
  (AIF 3.1.3); Empire's weight, 32.07% of the group's revenue and 44.29% of its assets (AIF 3.1.1). From the risk factors
  (the Item 1A equivalent): regulatory risk and political pressure on affordability (AIF 4.2), wildfire and inverse
  condemnation (AIF 4.1, the Mountain View fire), the credit rating and leverage targets (AIF 2, 4.3, 4.4). From the MD&A
  (the Item 7 equivalent): the regulatory proceedings table (what was asked, what was granted, and why), the Corporate
  Group's cost, the 2026 to 2028 capital plan, the featured Adjusted Net Earnings and guidance, and liquidity. Chosen
  because for a regulated utility the earnings are rate base times the allowed return, less what the regulators do not
  grant, and those are what the filing itself says decide the results.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the owner would be content to hold this "if the market closed for five
years" **[M1997-109]**, and for a utility that is a test of the regulated cash, since there is nothing else to own. No
macro enters **[M2000-094]**: the long rate is used only as the yardstick at Q7, and no forecast of rates or inflation is
made. Who is paid to tell you: the company features "Adjusted Net Earnings" and a guidance range in its MD&A, and an
activist holder (Starboard Value) has had board seats under cooperation agreements since 2024 (AIF 2.1.2, 2.1.3); both
are read as interested voices, and the run works from the GAAP statements. **Contrary evidence, written down as found**
**[M1997-127]**: (1) shares outstanding rose from 95,422,778 (FY2010) to 768,351,419 (FY2025) while the accumulated
deficit reached $(2,961.3)M (XBRL facts of the 40-Fs; FY2025 balance sheet); (2) FY2024 net loss to common shareholders
of $(1,391.0)M, mostly a $1,357.3M loss on classifying the renewables business as held for sale (FY2025 cash-flow
statement, 2024 column); (3) regulators or their staffs moved to dismiss three of its rate cases (Granite State Electric
2023, EnergyNorth Gas 2024, Empire Electric Missouri 2025) and the Missouri Office of the Public Counsel recommended no
increase "citing ongoing billing issues" (MD&A FY2025, regulatory proceedings); (4) a fatal gas explosion at Lexington,
Missouri on 2025-04-09, with a Missouri Attorney General petition and an MPSC investigative docket (FY2025 note
20(a)(iii)); (5) the Apple Valley water system may yet be taken by condemnation (note 20(a)(ii)); (6) the Kansas filing
asks a base-rate increase of about 93.77% (MD&A FY2025, regulatory proceedings).

## THE STANDING RULE
The buyer's conduct, not the target's: bought for cash, with no borrowed money **[L2014-005]**, sized so that a total loss
of the position could not touch what the buyer has and needs **[M2012-081]**. Nothing in this name requires otherwise.
The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; "a reasonable probability of being able to asses where the business will be
  in 10 years" **[M2000-037]**. The first step is "trying to identify the key variables in that particular business, and
  evaluating how predictable they were" **[M1998-044]**.
- **The key variables, from the filing.** Every utility in the group operates under cost-of-service regulation, in which
  "the revenue requirement upon which rates are based is determined by applying an approved return on rate base, and
  adding depreciation, operating expenses and administrative and general expenses" (AIF 3.1.1(ii), electric; the water
  and gas sections say the same). So the earnings are three variables: the rate base (the capital put in; $3.2 billion of
  utility capital spending planned for 2026 to 2028, MD&A Financial Outlook), the return the regulators allow on it, and
  how much of the allowed return the company actually earns after regulatory lag, disallowances and its own costs. The
  first is in the company's plan; the second is in every order (allowed ROEs of 9.3% to 9.75% in the settlements and
  proposed decisions of 2025 and 2026, MD&A table); the third is read from the reported results. The speakers name this
  as the easy case: "the classic case used to be a water or electric utility where the cash could be deployed and the
  return was more or less guaranteed within a narrow range, and it was very easy to make calculations then as to the
  expectable returns in the future." **[M1998-058]**; "when you get an allowed return in the electric utility you’re
  almost certain of earning it, I mean, if you behave yourself." **[M2010-037]**.
- **The rows against.** The same speakers, in 2023: "the regulatory climate in a few states has raised the specter of
  zero profitability or even bankruptcy [...] In such jurisdictions, it is difficult to project both earnings and asset
  values in what was once regarded as among the most stable industries in America." **[L2023-011]**. AQN has utilities in
  California (CalPeco Electric and the Mountain View fire; Park and Apple Valley water), the state that row names. They do
  not decide: the deciding system, Empire (Missouri, Kansas, Oklahoma, Arkansas), carries 32.07% of the group's revenue
  and 44.29% of its assets (AIF 3.1.1(iii)(3)), and the group answers to 17 regulators across 13 states, a province,
  Bermuda and Chile (MD&A FY2025, regulatory risk). Diversity of regulators is itself named a protection: "it is far
  safer to have earnings from ten diverse and uncorrelated utility operations [...] than it is to have far greater
  coverage provided by a single utility" **[L2005-019]**. The second clause of **[M2010-037]**, "if you behave yourself",
  is live here (the billing record), but it is a question about the people and the return actually earned, owned by Q2,
  Q3 and Q5, not about whether the economics can be foreseen.
- **Would the insiders write it down?** **[M2000-105]**: yes; the company itself writes a three-year capital plan and an
  earnings range for 2026 and 2027 (MD&A Financial Outlook), and the commissions write the allowed return. No technology
  named in the filing changes the wires and pipes within ten years; it names on-site generation and electrification of
  heating as competition (AIF 3.1.3), which is slow change, carried to Q2 test 11 **[M1998-008]**.
- **Do the past statements tell the future ones?** **[M2008-033]**: for the continuing business, yes, through the segment
  note (Regulated Services Group operating income, depreciation, capital spending and assets, note 19) and the earlier
  40-Fs; the renewables business that weighed on FY2017 to FY2024 is gone (sold 2025-01-08), and its cash is separated
  where the filings allow (Q4, Q7).
- **Routing.** No fast-changing industry closes the file here. The regulated return is "important and knowable"
  **[M2006-076]**; what remains in doubt is the regulators' future treatment and the company's conduct before them, which
  the rows treat as the castle and the people **[M2014-087]**, **[L2008-008]**.
- **VERDICT: IN.** A multi-jurisdiction cost-of-service utility whose earnings are rate base times an allowed return, read
  from its filings **[M1998-058]**, **[M2012-065]**; California's uncertainty **[L2023-011]** sits in a part that does not
  decide.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

**The parts table** (business of parts, the framework's CONVENTION of 2026-10-06). The segment note (FY2025 40-F, note
19) reports one operating segment, the Regulated Services Group, and discloses the Hydro Group beside it; the Corporate
Group is cost and debt, not a business. Operating income: FY2025 Regulated Services Group $508.6M, Hydro $19.2M; FY2024
$440.1M and $20.2M. Before FY2024 the hydro plants sat inside the Renewable Energy Group, now sold, so the five-year share
of the continuing parts is shown on the two years the filer reports them apart: Regulated Services about 96%. Inside the
group the filer aggregates by system type (MD&A FY2025, Regulated Services Group): electricity $934.9M of $1,754.6M net
utility sales (53%) and $5,566.5M of $9,578.6M of assets (58%); natural gas $387.4M and $2,018.1M; water and wastewater
$400.0M and $1,895.4M. Operating profit by system type is not reported (only its yearly change), so net utility sales
and assets are the nearest filed measure.

| Part | Share | Castle | Decides |
|---|---|---|---|
| Regulated Services Group | about 96% of FY2024 to FY2025 operating income | exclusive service territories under cost-of-service regulation | **yes** (more than half) |
| of which electric (Empire, BELCO, CalPeco, Granite State) | 53% of net utility sales, 58% of assets | same | the largest part inside the deciding part |
| Hydro Group | about 4% | small run-of-river plants, about 90% sold under long contracts (AIF 3.2) | no; carried to Q7 at no growth |

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent.* The filer: "Generally, the Regulated Services Group’s utility businesses have
   geographic monopolies in their service territories." (AIF 3.1.3). The New Brunswick gas franchise is exclusive to 2044
   and extendable by 25 years (AIF 3.1.1). The franchise is the moat; its permanence rests on a bargain: "We, in turn,
   look to our utilities' regulators (acting on behalf of our customers) to allow us an appropriate return [...] We
   shouldn't expect our regulators to live up to their end of the bargain unless we live up to ours." **[L2009-011]**.
2. *Would it stand without the lord?* The wires and pipes would; the return would not be protected from a poor operator:
   "There is no hiding your history when you stand before these regulators." **[L2008-008]**.
3. *The money test.* No attacker with money can build a second grid or water main in a franchised territory
   **[M2011-015]**. Two cracks named in the filing: a town may take the system by eminent domain (Apple Valley; the
   California Court of Appeal reversed the company's trial win on 2025-01-15 and the California Supreme Court is
   reviewing, note 20(a)(ii)), and on-site generation and other heating fuels compete (AIF 3.1.3).
4. *Pricing power and the agony before a rise.* By design there is none: "The whole idea behind the utility industry is
   not to allow extraordinary profits. But we think it’s a very good business." **[M2000-131]**. Every rise is a rate
   case, and the filing records the agony (MD&A FY2025, regulatory proceedings): Empire Missouri's true-up position of
   about $168M became $97M, phased over three years and released only once billing and customer-service metrics are met
   for three consecutive months; Granite State asked $15.5M and got $5.5M; EnergyNorth asked $27.5M and settled on the
   $8.7M temporary rates; Midstates asked $13.2M and got $9.1M; BELCO's 2026 allowance was cut by $3.6M; CalPeco's
   $64M base request stands at a proposed $48.6M at a 9.75% ROE against the 11% asked.
5. *Unit volume.* Customer connections 1,265,000 to 1,272,000 in FY2025; electric usage up 1.1%, "primarily due to
   favourable weather and customer growth at the Empire District Electric System" (MD&A FY2025). Flat, as a utility is.
6. *The low-cost position.* The Kansas filing asks about 93.77% more in base rates (MD&A FY2025). The rows warn of the
   incumbent "particularly if it is a high-cost operator" **[L2015-007]**. No filing read states AQN's rates against its
   neighbours'; recorded as not found.
8. *The low bid.* Inside the territory the customer cannot choose another wire, except New Hampshire's energy-supply
   choice (AIF 3.1.1).
9. *Ask the competitors.* There are none in the territory to ask; the regulators play the part, and their staffs moved
   to dismiss three of the company's rate cases (Granite State 2023, EnergyNorth 2024, Empire Missouri 2025) and the
   Missouri Office of the Public Counsel recommended no increase "citing ongoing billing issues" (MD&A FY2025).
10. *Widening or narrowing.* "Every day, in countless ways, the competitive position of each of our businesses grows
   either weaker or stronger. [...] But if we treat customers with indifference or tolerate bloat, our businesses will
   wither." **[L2005-010]**. The standing with the regulators narrowed from 2023 to 2025 on the filing's own record (the
   motions to dismiss, the performance-conditioned increase); the franchise itself did not.
11. *What could destroy, modify or reduce it.* **[M2000-014]**: wildfire liability under inverse condemnation in
   California (Mountain View fire, $178.4M accrued, the upper end "cannot estimate", note 20(a)(i)); the Lexington gas
   explosion (a death, the Missouri Attorney General's petition, an MPSC safety docket, $152.2M accrued, note
   20(a)(iii)); condemnation; political pressure on affordability (AIF 4.2); the regulatory climate the speakers
   themselves misjudged, "I did not anticipate or even consider the adverse developments in regulatory returns"
   **[L2023-011]**.

**The competitor row** *(CONVENTION of this run: the AIF names no rival, and says the utilities "have geographic
monopolies in their service territories" (AIF 3.1.3); so three SEC filers in the same regulated field were chosen, one
per system type, the electric one a neighbour of the deciding system. Rationale: a utility's rival for capital and for
the regulator's judgment is the comparable utility, not a seller in its territory.)* Metric: net income to common
shareholders over average common equity, from each filer's own 10-K or 40-F XBRL facts (script
`Test Runs/_research 2026-10-18 AQN/peers.py`):

| Filer | Field | Return on average common equity, by year | Mean | Latest accession read |
|---|---|---|---|---|
| AQN | multi-state electric, gas, water | 2016 7.5%, 2017 7.0%, 2018 6.7%, 2019 15.9%, 2020 18.0%, 2021 4.8%, 2022 -4.1%, 2023 0.4%, 2024 -29.7%, 2025 3.8% | 3.0% (2016 to 2025) | `0001174169-26-000015` |
| Evergy (EVRG) | Kansas and Missouri electric | 7.7%, 7.2%, 7.2%, 9.8%, 8.0%, 7.6%, 8.9%, 8.5% (2018 to 2025) | 8.1% | `0001711269-26-000017` |
| American Water Works (AWK) | multi-state water | 11.3%, 18.4%, 10.9%, 10.8%, 10.4%, 10.5% (2020 to 2025) | 12.1% | `0001410636-26-000034` |
| Atmos Energy (ATO) | multi-state gas incl. Kansas | 10.5% (FY2016) to 9.3% (FY2025), never below 8.7% | 9.9% (FY2016 to FY2025) | `0000731802-25-000056` |

AQN's 2019 and 2020 figures carry unrealized gains on its Atlantica shares of $276.5M and $559.7M (FY2020 cash-flow
statement, "Change in value of investments carried at fair value", accession `0001174169-21-000012`), later given back;
its 2016 to 2020 figures are net income before the preferred dividend (the XBRL common-only tag starts in FY2021), which
flatters them slightly. Over the decade AQN earned $613.6M in total for its shareholders while its common share capital
rose from $1,972.2M to $7,401.7M. Operating income over total assets, the same filings: AQN 2.3% to 3.6% (FY2021 to
FY2025), Evergy 3.7% to 4.8%, American Water 4.6% to 5.3%, Atmos 4.2% to 6.8%.

**The field's returns over the last full cycle, judged in words.** The field earns what regulators allow, high single
digits on equity over the decade for the three comparables. That is the case the framework sends on rather than closing:
"A return set by a regulator is the exception, carried to Q3 as a second best" (Q2, What it rules OUT), on the rows
"there’s no way we get rich on our utility investments. But there’s no way we get poor, either." **[M2009-104]** and
"We expect only that these businesses have reasonable expectations of earning decent returns on the incremental sums
they invest." **[L2009-012]**. AQN's own return over the cycle is far below the field's; that is a fact about the
company's earned return and its capital allocation, not about the franchise, and it is weighed at Q3 and Q6.

**Why IN, and not OUT or TOO HARD.** A castle is OUT when shown open on the evidence **[M2011-015]**: the franchise is not
open, no attacker can take the territory, and the filings show rate increases still granted in every jurisdiction listed,
smaller than asked. It is TOO HARD when its future cannot be judged **[M2000-019]**: the regulated return is set in public
orders, and the speakers' own bet is the one to be judged here, "the bet we are making is that regulatory authorities
will treat us fairly in the future [...] because we’ve done so much better than, really, the great majority of utilities
in delivering electricity at lower rates" **[M2014-087]**. AQN cannot show the second half of that sentence on the
filings read; the cost is a narrower and less certain earned return, which the rows price, not refuse: "you’d better hope
that the rate of return allowed is commensurate" **[M2005-052]**. The California exposure the 2023 letter names
**[L2023-011]** sits in parts that do not decide.

- **VERDICT: IN**, narrowly: the franchise castle stands **[M2011-015]**, **[M2000-131]**; the moat is narrowing at the
  regulators' table on the filing's own record **[L2005-010]**, **[L2008-008]**, which is carried, with the competitor
  row, to Q3, Q5 and Q6.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The question: "does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**; for a
utility the measure the speakers use is "the operating earnings after depreciation" set against the capital put in
**[M2014-086]**, and the condition for a capital-heavy business is "decent returns on the incremental sums they invest"
**[L2009-012]**.

**The regulated group, from its own segment notes** (US$ millions; 40-F segment notes FY2020 `0001174169-21-000012`,
FY2021 `0001174169-22-000021`, FY2023 `0001174169-24-000019`, FY2024 `0001174169-25-000020`, FY2025
`0001174169-26-000015`; the FY2023 column as restated in the FY2024 40-F):

| Year | Operating income | Depreciation | Capital spending | PP&E | Total assets | Op. income / PP&E |
|---|---|---|---|---|---|---|
| 2019 | 313.8 | 194.8 | 478.9 | 4,763.7 | 6,825.4 | 6.6% |
| 2020 | 322.1 | 219.1 | 690.8 | 5,757.5 | 8,528.4 | 5.6% |
| 2021 | 399.5 | 280.5 | 998.9 | 7,394.2 | 10,512.8 | 5.4% |
| 2022 | 459.3 | 317.3 | 908.7 | 8,554.9 | 12,109.6 | 5.4% |
| 2023 | 466.3 | 346.2 | 740.8 | 8,945.6 | 12,659.0 | 5.2% |
| 2024 | 440.1 | 386.8 | 757.2 | 9,284.4 | 12,927.9 | 4.7% |
| 2025 | 508.6 | 392.1 | 603.5 | 9,578.6 | 13,517.0 | 5.3% |

- **What the capital earns, before tax and before interest.** From 2019 to 2025 the group's operating income rose
  $194.8M while its property, plant and equipment rose $4,814.9M and its total assets $6,691.6M (acquisitions included,
  among them the New York water system in 2022): about **4.0% pre-tax on the added plant and 2.9% on the added assets**.
  After the company's own tax (the group's FY2025 tax was $96.2M on $370.8M of pre-tax earnings, 25.9%) that is about
  3% on the added plant, below the 5.43% long Treasury. The allowed returns in the orders are 9.3% to 9.75% on the equity
  part of rate base (MD&A FY2025), so the gap is the regulatory lag, the disallowances and the company's own costs. The
  speakers' rule of the poor business applies by its numbers: "if you have a business that’s earning 5 or 6 percent on
  equity and you hold it for a long time, you are not going to do well in investing. Even if you buy it cheap to start
  with." **[M1998-006]**; and of growth bought this way, "we’re not earning a higher rate of return on capital than we
  were when we started. We just put way more capital into the business" **[M2023-081]**.
- **What must go back in.** Capital spending was 2.4 times depreciation over 2019 to 2025 ($5,178.8M against $2,136.8M).
  The plan is "$3.2 billion expected for 2026 through 2028 including approximately $0.8 billion in 2026" (MD&A Financial
  Outlook), against depreciation of about $400M a year. Consolidated cash from operations was $593.6M in FY2025 and
  dividends to common and preferred $211.8M; the plan cannot be paid from earnings, so it is paid by borrowing, issuing
  shares or selling parts (the Suralis sale, $126.5M expected, 6-K `0001174169-26-000038`). The rows on utilities say it
  plainly: "To earn more, their owners must invest more" **[L2011-019]**; "you have to keep putting more and more money
  into a public utility. And you’d better hope that the rate of return allowed is commensurate" **[M2005-052]**.
- **The second best, and its condition.** The rows admit the capital-heavy business as second best, "still a good choice"
  **[M2018-055]**, on the condition that "the cash they consume gets to earn a reasonable return" **[M2012-057]**; "if they
  earn a decent return on capital, it can be a good business over time" **[M2007-112]**. The comparables in Q2 earn 8% to
  12% on equity and 4% to 5% on assets before tax over the decade; AQN's regulated group earns 2.9% to 3.8% on total
  assets in FY2021 to FY2025 (operating income over assets, segment notes) and its shareholders 3.0% on equity over 2016
  to 2025 with two years of unrealized gains inside. The condition is not met on the record.
- **The growth arithmetic and its cap.** Growth here is rate base, bought at the cost of new capital at the allowed
  return less the lag; the per-share result over 2016 to 2025 is set out at Q6 (dividend per share cut from $0.713 in
  FY2022 to $0.26; shares outstanding up 2.8 times since FY2016). Growth that earns less than its cost "can destroy value"
  **[L2000-023]** and is carried so at Q7.
- **WEIGHS AGAINST**: a compulsory-reinvestment business **[M1997-016]** whose added capital has earned about 3% after
  tax over six years, below the bond and far below its field **[M1998-006]**, **[L2009-012]**, **[M2012-057]**. (The
  "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]**. US$ millions, from the 40-F XBRL
facts (latest-filed value for each year-end, so FY2023 and earlier carry the sold renewables business; FY2023 PP&E is
the restated continuing figure), checked for FY2024 and FY2025 against the filed balance sheet and for FY2020 and FY2021
against the filed equity section (`aqunf-20201231.htm`, `aqunf-20211231.htm`):

| Year-end | Total assets | PP&E | Goodwill | Equity to shareholders | Deficit (retained) | Common share capital | Long-term debt (incl. current) | Receivables | Revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 8,249.5 | 4,889.9 | 228.4 | 1,923.6 | (556.0) | 1,972.2 | 3,913.4 | 189.7 | 1,096.0 |
| 2017 | 8,395.6 | 6,304.9 | 954.3 | 2,717.5 | (524.3) | 3,021.7 | 3,079.6 | 244.6 | 1,521.9 |
| 2018 | 9,398.6 | 6,393.6 | 954.3 | 3,177.6 | (595.3) | 3,562.4 | 3,336.8 | 245.7 | 1,648.5 |
| 2019 | 10,920.8 | 7,241.0 | 1,031.7 | 3,875.1 | (367.1) | 4,017.0 | 3,931.9 | 259.1 | 1,626.4 |
| 2020 | 13,224.1 | 8,241.8 | 1,208.4 | 5,203.6 | 45.8 | 4,935.3 | 4,538.5 | 324.8 | 1,677.0 |
| 2021 | 16,797.5 | 11,042.4 | 1,201.2 | 5,859.0 | (288.4) | 6,032.8 | 6,211.4 | 403.4 | 2,274.1 |
| 2022 | 17,627.6 | 11,944.9 | 1,320.6 | 5,219.6 | (997.9) | 6,183.9 | 7,512.0 | 528.1 | 2,765.0 |
| 2023 | 18,374.0 | 9,126.8 | 1,324.1 | 5,039.6 | (1,279.7) | 6,230.0 | 7,500.2 | 524.2 | 2,403.9 |
| 2024 | 16,961.7 | 9,450.1 | 1,312.2 | 4,707.9 | (2,929.9) | 7,391.3 | 6,698.7 | 422.6 | 2,319.5 |
| 2025 | 14,136.2 | 9,749.9 | 1,320.1 | 4,641.1 | (2,961.3) | 7,401.7 | 6,532.9 | 494.8 | 2,433.6 |

**Reading them for "what the figures are saying and what they don’t say and what they can’t say"** **[M2025-032]**:
- *Equity against goodwill.* Equity grew by issuance, not retention: common share capital rose $5,429.5M (2016 to 2025)
  while the deficit deepened by $2,405.3M; shareholders' equity in 2025 ($4,641.1M, of which $184.3M preferred) is
  barely above 2020's after $2,466.4M more shares were sold. Goodwill, mostly from the Empire purchase of 2017, is
  $1,320.1M, 28% of shareholders' equity; on tangible common equity (about $3,067M) the business is thinner than its
  book says.
- *Cash and receivables against sales.* Cash is held near nothing ($32.7M at the end of 2025, $55.0M at 2026-06-30), the
  company living on its revolvers and commercial paper. Receivables ran 15% to 17% of revenue in 2016 to 2019 and 18%
  to 20% from 2020; at 20.3% in 2025 they are the highest of the decade, in the years of the billing-system complaints
  (Q2, Q5). Not a fraud tell on its own; consistent with the billing record.
- *Debt.* Long-term debt rose from $3.9bn to $7.5bn (2016 to 2022) and fell to $6.5bn only through the sale of the
  renewables business and the Atlantica stake ($1,374.8M of debt repaid on disposition in 2025, FY2025 cash-flow
  statement). Weighed at Q9.
- *Regulatory assets* (deferred costs awaiting recovery) rose from $243.5M non-current (2016) to $1,190.8M (2025); the
  FY2025 note 6 itemises them (securitized storm and plant-retirement costs $260.0M, deferred capitalized costs $244.1M,
  rate adjustment mechanisms $184.5M, wildfire mitigation $139.7M, fuel $116.1M and smaller items), and EY made their
  recoverability the critical audit matter. The rows tell the reader to look twice when "deferred asset accounts start
  building up suspiciously high" **[M1995-064]**; looked at twice, the build is itemised, mostly ordered by regulators,
  and audited as a CAM. Recorded as a weight against, not suspicion.
- *What they cannot say:* the regulated return actually earned on rate base (the filer reports no rate base figure in the
  documents read) and what the sold renewables business contributed to the consolidated cash flows, which "AQN has
  elected to present [...] combined with cash flows of continuing operations" (FY2025 note 1(c)). Q7 is therefore built
  from the segment notes, not the consolidated cash flow.

**The real costs.**
- *Depreciation* is a true cost **[R1996-023]**, and here it is short of what keeps the plant in place: the filer's own
  "Sustaining" spending, "Capital spend to support existing systems (e.g. asset replacements, safety & reliability
  projects)", was $610.5M in 2024 and $499.7M in 2025 against depreciation of $386.8M and $392.1M (MD&A FY2025, Summary
  of PP&E expenditures; segment note). The speakers name this case: "if you’re in a business such as the utility business
  or the railroad business, it just keeps eating up more and more money, and your depreciation charges are inadequate
  and you’re kidding yourself as to your real economic profits." **[M2015-049]**. The shortfall is subtracted at Q7
  **[L2015-004]**. A presentation change to record: the FY2024 MD&A showed "Rate Base Maintenance" of $387.1M for 2024,
  footnoted "Maintenance expenditures are calculated based on the depreciation expense for the period"; the FY2025 MD&A
  shows "Sustaining" of $610.5M for the same year. The new definition is the more conservative, and the run uses it.
- *Stock pay* $13.0M in FY2025 (cash-flow statement), small, and counted.
- *Restructuring:* "Restructuring costs include one-time costs related to the Company's ongoing simplification" (note
  17(a)), $27.0M in 2024, $38.7M in 2025, and more in the first half of 2026 ("higher non-recurring other losses related
  to restructuring costs", Q2 2026 MD&A). Three years of "one-time" is a recurring cost: "we do not ask you to forget
  about those costs" **[M1999-023]**; telling owners year after year to ignore them "is misleading" **[L2016-007]**.
  Counted at Q7.
- *Tax-equity accounting.* "Net effect of non-controlling interests" added $72.5M to FY2025 earnings attributable to
  shareholders (statement of operations): the tax-equity partners in the Missouri and Kansas wind farms are allocated book
  losses. It is not cash to the common holder and is left out of owner cash.
- *Taxes.* Cash taxes were a net receipt in 2024 and 2025 ("Cash received during the year for income taxes - net $73.4",
  FY2025 cash-flow statement); the provision was $65.0M on $211.0M pre-tax, and the regulated group's own rate 25.9%
  ($96.2M on $370.8M, note 19). The company guides a "low twenties" rate for 2026 and "mid-to-high twenties" for 2027
  (MD&A Financial Outlook). The group's 25.9% is used as the company's own tax at Q7.
- *EBITDA in the filer's mouth:* none; it features EBIT and "Adjusted Net Earnings" as non-GAAP measures (MD&A, Caution
  Concerning Non-GAAP Measures).

**The tells, and the habit carried to Q5.** The MD&A features Adjusted Net Earnings ($258.8M against GAAP $208.0M from
continuing operations, FY2025), gives an earnings-per-share range for 2026 and 2027, and reports that "Adjusted Net
Earnings per common share exceeded the top end of Company’s previously provided guidance range by $0.02", the beat
"driven by accelerated realization of operating expense savings, lower depreciation expense resulting from authorized
deferrals, and tax adjustments" (MD&A FY2025). An adjusted figure featured **[L2016-006]**, guidance **[L2019-006]** and a
target beaten partly by deferrals and tax **[L2002-041]** are weighed against here and carried to Q5, as the framework
directs. The statements themselves carry a clean opinion and an effective control attestation for every year read
(FY2020, FY2021, FY2023, FY2024, FY2025; EY, auditor since 2013), with no material weakness found in any of them.

**Confusion or suspicion?** The confusing items (the combined cash flows, the HLBV allocation, the restated years) are
each explained by the filer and knowable from the filings read; the deferred accounts are itemised and audited. No
confusion that closes the file **[M1995-063]**, and no suspicion raised by the accounts themselves **[M1995-065]**; the
outside doubt is the regulators', about the data in the rate filings, recorded at Q5. A management "preoccupied with
accounting considerations" is "a negative" but not "a total exclusionary factor" **[M1994-018]**.

- **VERDICT on the accounts: WEIGHS AGAINST** **[M1994-018]**: equity built by issuance while the deficit grew
  **[M2025-032]**; depreciation short of sustaining spending **[M2015-049]**; recurring "one-time" restructuring
  **[L2016-007]**; adjusted earnings and guidance featured **[L2016-006]**. The recast for Q7: segment operating income,
  less restructuring and other losses, after the company's own 25.9% tax, plus depreciation, less the filer's sustaining
  spending (all spending beside).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The two yardsticks: "how well they run the business [...] the hand they were dealt [...] how well that they treat their
owners" **[M1994-008]**. For a stock the reading tests carry the weight **[M2007-081]**.

**Who they are.** Almost the whole command is new: Roderick West, CEO from 2025-03-07 (25 years at Entergy, last as
Group President, Utility Operations; circular p. 52); Robert Stefani, CFO from 2026-01-05; Peter Norgeot, COO from
2026-01-05; a Chief Regulatory and External Affairs Officer and a Chief Customer Officer from 2025-06-30 (AIF 2.1.3,
2.1.4). The previous CEO stepped down in 2023 as the renewables sale began; an interim CEO served until 2025. Starboard
Value's Gavin Molinelli sits on the board under a cooperation agreement (AIF 2.1.3; circular).

**The integrity record, as the filings show it.**
- No penalty, sanction or securities settlement in FY2025 (AIF 9.2); no restatement found; clean audit opinions and
  effective internal control attested for FY2020, FY2021, FY2023, FY2024 and FY2025 (EY), with no material weakness
  found in any of them.
- Bad news is told, and told plainly: the MD&A's regulatory table states the motions to dismiss, the Public Counsel's
  "no increase, citing ongoing billing issues", the performance conditions on the Missouri increase, the opposing
  testimony on the wildfire recovery, and the Lexington death and the Attorney General's petition (MD&A FY2025; note
  20). The rows ask for exactly this: "tell us the bad news immediately" **[M1998-039]**; a management "telling us about
  the things that we would want to know about if we owned a hundred percent of the company" **[M1998-036]**.
- What is not told: the documents read define "rate base" as a measure (MD&A, non-GAAP caution) but give no rate base
  figure and no earned return on equity, though the circular credits management with "a ~130 basis point increase to
  earned return on equity" (circular p. 52) without stating its level. For a utility those are the figures that matter
  **[M2007-082]**; their absence from the filed documents read is recorded as a gap in candour, weighed against, not as
  a misleading statement (the allowed returns are stated in every case).
- The regulators' doubt (2023 to 2025): New Hampshire's Department of Energy moved to dismiss two rate cases and the
  NHPUC ordered an independent audit of the accounting information in a rate filing after the company's own
  third-party review; Missouri's staff and Public Counsel moved to dismiss the Empire case (MD&A FY2025). The filings
  tie these to the new customer and accounting systems (the integrated customer platform completed in 2024, AIF 2.1.2;
  "deficiencies in the design or implementation of these systems", MD&A risk). The record shows errors of systems and
  execution, settled in each case, and the Missouri commission implemented the $97M increase on 2026-07-15 "following
  improvements to customer performance metrics" (Q2 2026 earnings release, 6-K `0001174169-26-000031`, Exhibit 99.5). No
  instance found, in the filings read, of a regulator or court finding dishonesty.

**The habits carried from Q4, read with that record.** The featured Adjusted Net Earnings, the guidance range and the
FY2025 beat "driven by [...] lower depreciation expense resulting from authorized deferrals, and tax adjustments" (MD&A)
are weighed against **[L2016-006]**, **[L2002-041]**; the bonus that rides on them is read at Q6 Part B. The deferrals
were authorized by regulators and the sources of the beat were disclosed in the same paragraph. Read with the candid
regulatory disclosures, they show a management that sells to the market in the market's terms, the "things that they do
in public in relation to their investors and the promises they make" **[M2004-067]**; they do not show a figure made up.
The rows apply integrity on doubt alone: "If you’ve got doubts, forget it." **[M2013-088]**. The doubt this file carries is
about competence and about incentives (Q6), not about whether these people tell the truth; on the filings read, no
instance found of a statement shown false.

**Ability, read against the hand dealt** **[M1994-008]**. The hand: franchised utilities in fair-to-middling
jurisdictions, the same hand Evergy, American Water and Atmos played to 8% to 12% returns on equity over the decade
(Q2). The record of the people who ran it to 2023: a 3.0% average return on equity over 2016 to 2025, a deficit grown
by $2.4bn, three rate cases met with motions to dismiss, a billing system that cost a rate increase its timing, and a
fatal gas explosion under investigation. The present team has eighteen months and one rate cycle: the Missouri metrics
met, the Kansas and Arizona cases settled, costs cut. The rows ask for a record read over years: "we
don’t like banjo hitters who suddenly proclaim that they can become power hitters." **[M1996-038]**; "we’ve actually seen
they batted .350" **[M2005-039]**. The new team has no record yet at this company to read either way; the company's record
is poor.

**Love of the business and alignment.** The CEO, paid $7,402,219 for 2025 (summary compensation table, circular p.
79), held 19,417 common shares worth $163,209 at the guideline date, 1.9% of his ownership guideline, with until
2030-03-07 to comply; the interim CFO held none (circular p. 73). The rows prefer people who "have gotten rich with their
shareholders and not off their shareholders" **[M2003-055]**; at eighteen months the test cannot yet be passed or failed
by the CEO, and is recorded.

- **VERDICT on integrity: IN.** No instance found of dishonesty in the filings read; bad news told plainly
  **[M1998-039]**; the habits carried from Q4 weigh against but leave no doubt about truthfulness **[M2013-088]**.
- **Ability: WEIGHS AGAINST**: the company's record against its field **[M1994-008]**, and a new team whose record is a
  promise **[M1996-038]**, **[M2005-039]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"the biggest judgment you have to make is how well capital will be deployed in the future" **[M2001-111]**.

### Part A: the money
**The retention test, over the decade** **[R1995-009]**, **[M1998-110]**. Nothing was retained in the ordinary sense:
common dividends paid over FY2016 to FY2025 were $2,356.8M (XBRL PaymentsOfDividendsCommonStock, 40-Fs), against net
earnings to shareholders of $613.6M over the same years (Q2), of which $836.2M in 2019 and 2020 was unrealized gain on the
Atlantica shares. The capital that went in came from the owners instead: shares sold for $4,666.0M in new issues
(FY2014 to FY2024) and $1,114.7M on the 2017 conversion of the subscription receipts that funded Empire (XBRL
StockIssuedDuringPeriodValueNewIssues and ...ConversionOfConvertibleSecurities), the dividend funded in part by the
issues. The per-share result: book value per common share **$6.35** at FY2016 ((1,923.6 - 184.3) / 274,087,018) and
**$5.80** at FY2025 ((4,641.1 - 184.3) / 768,351,419); the dividend per share cut from $0.713 (FY2022) to $0.26 (FY2025,
AIF 5.1); the 76.9 million shares delivered on the equity units in June 2024 were sold at about $14.95 each ($1.15bn for
3.3439 shares per $50 contract, AIF 2.1.2), against $5.25 today. Common share capital paid in stands at $7,401.7M; the
market values the common at $4,041.2M. Every test the rows give fails: "if after three or four years, you’ve found that
the dollars we’ve retained hasn’t created more of that in value, then the presumption becomes very strong" **[M1998-110]**;
the yardstick is "at least $1 of market value for each $1 retained" **[R1995-009]**.

**The forward question** **[M2010-097]**: the $3.2bn plan for 2026 to 2028 goes into rate base that, on the record of Q3,
has earned about 3% after tax on the added plant; the company's own guidance is the improvement of that return, which is
a promise, not a record.

**Buybacks.** None in the window: the cash-flow statements FY2020 to FY2025 read show no repurchase of common shares,
and the XBRL facts carry none. The buyback test has nothing to read. **Written back from Q7:** the bottom of the central range is **$(8.85) a
share** (the organic pair; every case computed is below zero), so no repurchase price could have sat at or below it.

**Issuance and deals.** Shares outstanding rose from 95,422,778 (FY2010) to 768,351,419 (FY2025), eight times, through
a decade of issues; the rows: "we have never invested in companies that are hell-bent on issuing shares. That behavior is
one of the surest indicators of a promotion-minded management, weak accounting, a stock that is overpriced and [...]
outright dishonesty." **[L2014-015]**. The framework carries serial issuance as a candidate second STOP, unresolved
(Q6, section VI); this run weighs it heavily against and does not close on it. The 2026 circular asks owners to double
the shares reserved for the unit plan, from 14,000,000 to 29,000,000 (circular p. 17). The deals: Empire (2017) was
bought for cash, $1,519.9M (XBRL PaymentsToAcquireBusinessesNetOfCashAcquired), funded by the subscription receipts, so it
is an acquisition under the framework's definition, not a merger; **no all-stock deal in the window, so the one STOP of
Part A is not engaged** **[L2009-019]**. The renewables business, built over a decade, was sold in 2025 for about
$2.1bn net after a $1,357.3M loss on its classification as held for sale (FY2024); the Atlantica stake was sold for about
$1.1bn (AIF 2.1.2); the Kentucky Power purchase was abandoned in 2023 (AIF 2.1.1). Value given against value got
**[M1995-001]**: on the filed record the decade's deals and their unwinding returned less than was put in.
Post-mortems are "rare in American boardrooms. They should instead be standard practice." **[L2014-013]**; the filings
read contain none.

**Dividends.** Cut from $0.713 (FY2022) to $0.434, $0.347 and $0.26; the AIF says "There are no restrictions on the
dividend policy of AQN" and that payment depends on the risk factors (AIF 5.1). Paying a dividend the business did not
earn, with shares sold to do it, is the opposite of "clear, consistent and rational" **[L2012-015]**.

**Part A: WEIGHS AGAINST**, heavily: a decade in which owners' capital went in at prices up to about $15 a share and is valued
at $5.25, with no repurchase and serial issuance **[R1995-009]**, **[M1998-110]**, **[L2014-015]**. The all-stock-deal STOP is
not engaged **[L2009-019]**.

### Part B: the pay, the board and the owners
- **The bonus rides on the featured number.** The 2025 short-term plan weighted Adjusted Net EPS at 40% and it paid at
  the stretch maximum (80% against a 40% weight); funds from operations was below target; the corporate scorecard paid
  145% of target, after the board took 15.1 points off for safety in the year of the Lexington death (circular pp. 52,
  62 to 63). The 2025 long-term units vest half on cumulative Adjusted Net EPS and half on relative return (circular p.
  67). Pay tied to a figure management shapes, partly through regulator-authorized deferrals and tax (Q4), is nearer what the
  rows warn against, "rewarding anything that can be easily faked" **[M1996-089]**, than a cash return; "you get what
  you reward for" **[M2016-083]**.
- **Upside without the downside.** The 2023 performance units vested at 107.4% of grant value although the company's
  shareholder return over the period was below the 25th percentile of its index group; the sustainability target was
  rewritten to two years after the renewables sale (circular p. 67). "alignment means being a partner in both
  directions, not just on the upside" **[L1994-020]**.
- **The proxy test** **[M1994-009]**: the CEO was paid $7,402,219 for 2025 and held $163,209 of shares at the guideline
  date (Q5); the owners' dividend per share was cut by nearly two-thirds since 2022. Say-on-pay passed with 82.87%
  (circular p. 18).
- **The board.** The chair is not the CEO (circular, letter of the chair). A partner of Starboard Value, an activist
  owner, sits on the board under a cooperation agreement and the board was capped at nine without Starboard's consent
  (AIF 2.1.2, 2.1.3); a large owner in the room is what the rows call "The only cure" where boards fail **[M2006-011]**.
  Directors carry an ownership guideline of four times the retainer (circular p. 19).

**Part B: WEIGHS AGAINST**: pay keyed to the adjusted figure and paid above target while owners lost **[L1994-020]**,
**[M2016-083]**; the activist owner on the board weighs for.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a
business during its remaining life" **[R1996-018]**, net of "are you going to have to put more cash into after you buy
it?" **[M2014-068]**. The rate: the long Treasury, 5.43% (Step 0) **[M1996-025]**. The arithmetic is in
`Test Runs/_research 2026-10-18 AQN/q7.py`, its output in `q7_output.txt` beside it; every input is typed there with its
filing.

**The base, and why it is built from the segment notes.** The consolidated cash-flow statements combine the sold
renewables business with the continuing one through FY2024 (FY2025 note 1(c)), so the five-year window FY2021 to FY2025
is built from the continuing parts the segment notes report (Regulated Services, Hydro, Corporate). *CONVENTION of this
run:* (1) the Hydro Group, reported apart only from FY2023, is carried for FY2021 and FY2022 at its FY2023 to FY2025
average ($18.3M of EBIT a year), since it then sat inside the sold group; rationale: it is 4% of the business and has no
other filed figure for those years. (2) Working capital is the consolidated figure (XBRL IncreaseDecreaseInOperatingCapital),
which includes the sold business through FY2024; rationale: no segment figure is filed, and leaving it out would flatter
the base. Each year:

| Year | EBIT (continuing, Atlantica income out, FX loss back) | after the company's 25.9% tax | Depreciation | Sustaining spending | All spending incl. acquisitions | Increase in working capital |
|---|---|---|---|---|---|---|
| 2021 | 403.4 | 298.7 | 288.2 | 406.7 (est.) | 1,013.1 | 522.0 (Storm Uri year) |
| 2022 | 464.7 | 344.2 | 325.0 | 459.2 (est.) | 1,524.6 (incl. $609.3M New York water) | 221.6 |
| 2023 | 388.9 | 288.0 | 354.1 | 500.5 (est.) | 748.7 | (86.3) |
| 2024 | 442.7 | 327.8 | 395.7 | 617.1 | 763.8 | 139.5 |
| 2025 | 497.2 | 368.2 | 400.3 | 505.0 | 608.8 | 45.7 |

Restructuring, the Kentucky termination ($46.5M, 2023) and the disallowed securitization costs ($63.5M, 2023) stay in as
real costs (Q4). The tax is the company's own: the regulated group's FY2025 provision, 25.9% (note 19), no conversion
(Q7, Whose tax); cash taxes were refunds in 2024 and 2025 and are not used as the rate. The tax-equity allocation to
non-controlling interests is left out (Q4).

**The specifics, applied.**
- *(e) Maintenance, central.* The filer's own "Sustaining" spending is filed for 2024 and 2025 only. *CONVENTION of this
  run:* for 2021 to 2023 sustaining is estimated at depreciation times the 2024 to 2025 ratio of sustaining to the
  regulated group's depreciation, 1.426; rationale: the filer's earlier "maintenance" figure was depreciation by
  definition (Q4), which the filer itself replaced with the larger sustaining figure. The depreciation variant and the
  all-spending case are shown beside. The growth spending (all spending less sustaining, $434.1M a year on average) is
  charged against the growth it buys, ten years, stopping with growth.
- *(d) Working capital.* 2021's draw of $522.0M is the year of the February 2021 winter storm, whose "qualified
  extraordinary costs" the filer later securitized (AIF 2.1.2); by (d) it is carried at the other four years' intensity
  ($80.1M) in the central case, the literal window beside.
- *(b) The series changes sign* (central owner cash: 2021 $100.1M, 2022 $(11.7)M, 2023 $227.9M, 2024 $(33.1)M, 2025
  $217.8M), so growth is measured between the halves: $44.2M to $92.4M, 27.8% a year.
- *(f) The cap.* 27.8% carried ten years would need owner cash far above any share of sales the business has earned; cut
  to the business's own sales growth, 4.63% a year (regulated group revenue plus other revenue, FY2021 $1,997.6M to
  FY2025 $2,394.4M, segment notes), below the discount rate **[M1999-067]**, **[M1997-095]**.
- *(c) Acquisitions, and the serial acquirer.* The New York water purchase (2022, $609.3M, MD&A FY2023) is the window's
  one purchase. Net purchases ($609.3M) exceed half of the central owner cash before purchases ($501.0M over five years,
  half $250.5M), so by the serial-acquirer specific the **central figure is the organic pair**: the purchase left out of
  the growth spending (which falls to $312.2M a year) and only organic growth credited. The filer reports no organic
  growth; *CONVENTION of this run:* the total sales growth, 4.63%, is used as its upper bound, which flatters the organic
  case. The default pair (purchase deducted, total growth credited) is shown beside. Q3 has stated what the added
  capital returned, and Q6 weighs the buying.
- *(a) Cycle base.* The window holds the storm year, handled by (d), and the year of the sale (2024), whose consolidated
  working capital is shown as filed.
- *A deal signed but not closed:* the Suralis sale (6-K `0001174169-26-000038`, expected $126.5M) is left out of the
  central figure; valued beside as if closed, it would cut the claims ahead of the common by at most the proceeds and
  Suralis's share of non-controlling interests, about $0.27 a share before taking away Suralis's own cash, and changes
  nothing below.

**The claims ahead of the common** (Q2 2026 balance sheet, 2026-06-30): long-term debt $520.6M current and $6,115.1M
non-current, less cash $55.0M: **net debt $6,580.7M** (operating leases left out; the securitization bonds left in);
preferred shares $184.3M; non-controlling interests $356.3M; **$7,121.3M** in all. Enterprise value at $5.25:
**$11,162.5M**. No later subsequent event in the filings read changes the debt.

**COMPUTATION.** Five-year average owner cash, all-equity basis (before interest, after the company's tax):

| Case | Average owner cash | No-growth value (whole business) | Growth case, net of growth spending | Per share, after claims |
|---|---|---|---|---|
| **Central: organic pair, sustaining maintenance, (d) working capital** | **$100.2M** | $1,845.6M | $310.9M | **$(8.85) to $(6.85)** |
| Default pair beside (purchase deducted, total growth) | $100.2M | $1,845.6M | $(610.7)M | $(10.04) to $(6.85) |
| Sustaining maintenance, literal working capital | $11.8M | $218.1M | (no growth; series changes sign twice) | $(8.97) |
| Depreciation as maintenance, (d) working capital | $245.3M | $4,516.8M | $2,160.0M | $(6.45) to $(3.38) |
| All spending (growth capped at zero, (b)) | $(333.9)M | negative | negative | $(17.24) |

In both pairs the growth case is below the no-growth case: the growth spending is worth less than its cost, so the
no-growth case is the top of the range and the growth case the bottom, as specific (e) records the inversion, "growth
can destroy value" **[L2000-023]**.

**The floor is tested first** (2026-10-10). The most generous case the run can defend, depreciation as the maintenance
charge, growth spending ignored altogether, gives an expected return at $5.25 of **3.28%** a year (the rate at which that
cash stream equals the enterprise value); the central case gives 1.38%. A single-year check beside: FY2025's operating
profit after tax alone, $368.2M, is 3.3% of the enterprise value. No case earns about ten percent at the price
**[M2003-149]**; the width test is not reached.

- **Value range (central, the organic pair): $(8.85) to $(6.85) a share against $5.25.** Default pair beside: $(10.04)
  to $(6.85); literal window beside: $(8.97).
- **Fair price (a reporting figure, never a verdict; Part VII):** each end valued at ten percent and averaged, after the
  company's own tax: **$(8.95) a share on the all-equity basis** (central, the organic pair); **equity-only $(3.70) a
  share** (owner cash after after-tax interest, $(113.5)M a year, with the preferred and the non-controlling interests
  deducted). Default pair beside: $(9.44) all-equity, $(4.18) equity-only. Both are
  below zero: at no positive price does the midpoint of the range earn the floor. No cheap price is reported.
- **Closes: OUT.** No case earns the floor at the price **[M2003-149]**; the price sits above the top of the range, which
  closes OUT however wide the range (Q7, the four specifics). "So, there’s just a point at which we drop out of the
  game." **[M2003-149]**.
- **VERDICT: OUT** **[M2003-149]**, **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT (operator rule 2). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (Not asked by the operator for this run; no named business of Q12's list is involved.)

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor at $5.25; the central range is **$(8.85) to $(6.85) a share** (the
organic pair; default pair $(10.04) to $(6.85); every case computed below zero) against $5.25 (close 2026-10-16, aggregator
flagged). Q1 IN; Q2 IN narrowly (the franchise stands; standing with regulators narrowed); Q3, Q4 and Q6 weigh against;
Q5 integrity IN, ability weighs against. Fair price (reporting figure, Part VII): $(8.95) all-equity, $(3.70)
equity-only; not positive. Re-look condition, as for any OUT: an alert at the top of the computed range, which is below
zero, so no price alert can be armed on this computation.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q8 (the bond).** The long Treasury yields 5.43% (Step 0). The most generous case at Q7 gives an expected return of
  3.28% at the price; FY2025's after-tax operating profit alone is 3.3% of the enterprise value (`q7_output.txt`).
- **Q9 (debt and exposures).** Net debt $6,580.7M at 2026-06-30 against shareholders' equity of $4,620.9M (Q2 2026 6-K).
  FY2025 operating profit before tax, Atlantica income out, $497.2M against interest expense of $282.5M: about 1.8
  times (Q7 table; FY2025 statement of operations). Principal due within twelve months of 2025-12-31: $1,577.9M,
  including the $1.15bn 5.365% notes due 2026-06-15 (AIF 2.1.2; XBRL maturity facts of the FY2025 40-F); in Q2 2026 the
  company raised $1,174.1M of long-term debt and repaid $1,164.1M (Q2 2026 cash-flow statement), so that maturity was
  refinanced. Ratings: issuer BBB at S&P, DBRS and Fitch; subordinated notes BB+ (AIF 3.10). The revolving facility at
  the parent was cut from $1.0bn to $750M in November 2025 (AIF 2.1.3). Cash is held near zero ($55.0M); the company
  depends on revolvers and a $1.0bn commercial paper program at Liberty Utilities (AIF 2.1.3). Exposures without an upper
  estimate: the Mountain View fire ($178.4M accrued; "cannot estimate the upper end", note 20(a)(i)); the Lexington gas
  explosion ($152.2M accrued against $149.0M insurance; "cannot currently estimate the upper end", note 20(a)(iii)); the
  Apple Valley condemnation (note 20(a)(ii)). The Q2 2026 release records a $17.2M write-off on the California proposed
  decision on wildfire cost recovery (6-K `0001174169-26-000031`, Exhibit 99.5). Seventeen regulators in diverse
  jurisdictions (MD&A risk) bear on L2005-019's point about diversity.
- **Q12.** Nothing found bearing on the named businesses.
- **Integrity facts (Q5 was answered IN; recorded here for any later run):** the regulators' motions to dismiss three
  rate cases and the NHPUC's order of an independent audit of the accounting information in a rate filing (MD&A FY2025);
  the 2023 performance units vesting at 107.4% of grant value with bottom-quartile shareholder return and a target
  rewritten after the sale (circular p. 67); the absence of any rate base or earned-ROE level in the filed documents read
  while the circular credits an increase in earned ROE (circular p. 52).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `d66c5c34`, before any EDGAR request); written question by
      question; committed after each (Step 0 to Q1 `dc148275`, Q2 `05b18056`, Q3 `7bdc5687`, Q4 `33da6e03`, Q5
      `68edfaad`, Q6 with Q7 `05f32a69`, as the brief directs for the buyback line).
- [x] Dispatched run: the brief allowed per-question pathspec commits; the lock and the fold are the dispatching
      session's (operator rule ten). This run is not in the register until the dispatcher folds it.
- [ ] **No other run file was opened, listed or searched: not clean.** Before the template was copied, one listing of
      `Test Runs/` filtered on today's date showed other runs' file names (AES, HOKCY, MDU, NJR, NWN, OGS, SR, SWX, UGI,
      XNGSY); no file was opened; declared at the top under CONTAMINATION and not used. The session's opening context
      also showed the AES run's commit subjects; declared, not used. No `PORTFOLIO.md`, holding review, resume-state
      file, queue file or reading list was opened. (Spire, whose run of today appeared in that listing, was not used as a
      comparable; Atmos was chosen instead.)
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-18 AQN/check_ids.py`, below); every filing fact
      carries its document or accession; numbers carry a filing or are labelled CONVENTION.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): built from segment operating
      results, the company's own tax, depreciation, the filer's sustaining spending, all spending beside, and working
      capital; the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations, six items; Q2 tests 9 to 11); facts for
      later questions are under AFTER THE STOP.
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] `tools/run.py` printed only a failure line; nothing of it was used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A divestiture inside the window.** Q7's specifics cover purchases (c) but not the sale of half the business: the
consolidated cash flows of FY2021 to FY2024 include the sold renewables business, and the framework says nothing on
whether the five-year base should be the whole company as it was or the continuing parts as they are. This run built the
base from the segment notes of the continuing parts and confessed two conventions to do it (hydro years, consolidated
working capital); a sentence in (c), "net of businesses sold", reads as if sale proceeds were negative capital spending,
which would credit $3bn of proceeds as owner cash and is absurd here. (2) **The maintenance guess when the filer
changes its definition.** The filer's "maintenance" was depreciation by definition until FY2024 and became a larger
"sustaining" figure in FY2025; (e) says "where the filing allows the guess" without saying what to do for the window's
earlier years. This run scaled depreciation by the two filed years' ratio, confessed. (3) **The regulated-return
exception at Q2 has no test of its own.** Q2 sends "a return set by a regulator" to Q3 as a second best, but does not say
how to judge a utility whose regulatory standing is narrowing (motions to dismiss, performance-conditioned increases)
while its franchise stands; this run closed Q2 IN narrowly and weighed the narrowing at Q3, Q5 and Q6, and a reader could
argue for TOO HARD. (4) **Preferred shares and minority interests in the all-equity basis.** The framework's all-equity
figure subtracts net debt only; here $184.3M of preferred and $356.3M of non-controlling interests also stand ahead of
the common, and the run deducted them, confessed in the Q7 claims line. (5) **Serial issuance** is still an unresolved
candidate STOP (Q6, section VI); this company is the case the row describes, and the run could only weigh it.

**CONVENTIONS of this run, collected:** the competitor choice (Q2); the hydro years and the consolidated working capital
in the Q7 base; the sustaining estimate for 2021 to 2023; total sales growth as the upper bound of organic growth;
preferred shares and non-controlling interests deducted as claims ahead of the common.
