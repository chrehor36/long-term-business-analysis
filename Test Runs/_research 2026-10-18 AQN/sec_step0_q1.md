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

