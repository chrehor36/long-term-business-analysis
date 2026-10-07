# Attackers on The Work Number + the mortgage-cost controversy

Evidence rungs: **[FILED]** = SEC filing · **[IR]** = company investor materials, not SEC-filed · **[R3]** = press release / media / vendor blog — lowest rung, self-interested sources, no figure here is verified.

## The incumbent's own filed description (baseline)

**[FILED]** EFX FY2025 10-K (filed 2026-02-19, accession 0000033185-26-000010), Item 1:
- "The Work Number® held about **209 million active and 813 million total (active and historic) employment records** at December 31, 2025." Payroll data "from over 4 million organizations"; employers contribute free; fees are per-transaction.
- EFX's own competition language (Item 1): "Competition in the Verification Services business is **highly competitive with low barriers to entry** and includes employers who manage verifications in-house, lenders who obtain verifications directly from employers, and numerous online and offline firms that provide verification services. **Third parties may also seek to obtain verifications directly from employees** by leveraging paper copies of information or by seeking employee credentials to access information systems." — the "employee credentials" sentence is EFX describing the consumer-permissioned attack vector (Argyle/Plaid model) without naming anyone.
- EFX 10-K names **no** verification competitor; zero mentions of Plaid, Argyle, Truework, or Experian Verify.

## Attacker 1 — Experian Verify **[IR]**

From Experian Annual Report 2026 (year ended 31 Mar 2026), see `row Experian.md`:
- "growing our active record count to **66 million**" (~32% of EFX's 209M active records).
- Product motion aimed at mortgage: "Experian Verify Preview to provide mortgage lenders with earlier visibility into borrower employment data"; TazWorks background-screening integration post-year-end.
- No verification revenue disclosed. The only attacker with a bureau's balance sheet and existing lender pipes.

## Attacker 2 — Argyle (private) **[R3 — all self-reported]**

- Consumer-permissioned payroll connectivity (borrower logs into own payroll account).
- CEO mid-2026 update (argyle.com blog): 1M+ verifications completed in Q2 2026 alone; volume +55% YTD; "consumers shared 110M+ paystubs through Argyle in Q2, and 350M+ over the last year"; ~15 new customers/month.
- **Xactus360 integration announced 2025-10-21** (xactus.com release) — the same Xactus that is FICO's Mortgage Direct License launch partner [FILED via FICO DEF 14A]. The attacker stack is coalescing around the same reseller.
- Argyle-commissioned survey claim: "43% of lenders said they've been shifting volume away from The Work Number, and 61% now use at least one alternative vendor." **Vendor's own survey — treat as marketing, not measurement.**

## Attacker 3 — Plaid (private) **[R3 — company docs]**

- Plaid Income / "Consumer Report by Plaid Check" — Plaid Check is Plaid's own consumer reporting agency subsidiary (plaid.com/docs). Payroll Income product claims support for "approximately 80% of the US workforce, including gig income workers" — coverage claim, not a records count; consumer-permissioned, so "coverage" means *could connect if the borrower cooperates*, not a standing database. Structurally different from The Work Number's employer-fed instant database.
- No disclosed verification revenue or mortgage GSE traction found.

## What TRU and FICO filings say about payroll/income verification

- **TRU: NOT FOUND.** FY2025 10-K claims no income/employment verification business; "verification" appears only as identity verification. TRU is not attacking The Work Number on the record.
- **FICO [FILED]:** DEF 14A (2026-01-27): the Mortgage Direct License Program's launch partner Xactus is described as "a fintech and market leader in **verification solutions** for the mortgage industry and the largest credit verification and tri-merge provider of FICO® Scores."

## The mortgage credit-report cost controversy

**FILED evidence:**
- FICO FY2025 10-K, Item 1A: "There has been **increased regulatory focus in the U.S. related to the transparency and fairness of certain fees charged to consumers in connection with the closing of a residential mortgage loan, including fees for credit reports and credit scores.** If new laws, regulations or other governmental action limit the fees that can be charged … our ability in the future to increase pricing for FICO Scores used in mortgage originations may be impacted…"
- FICO FY2025 10-K, Item 1A: "…the change announced by the FHFA Director in July 2025 **permitting mortgage originators to choose the credit score they submit** … or a potential future change **permitting mortgage originators to underwrite loans using credit scores from fewer than three national consumer reporting agencies.**" (The bi-merge threat, in FICO's own risk factor.)
- TRU FY2025 10-K: "**uncertainty related to Fair Isaac Corporation's ('FICO') new Mortgage Direct License Program**" listed among factors that could materially affect results; risk factor: data providers (with whom "we compete" "in some cases") could "increase the costs for their data … a desire to generate additional revenue."
- TRU 8-K investor exhibit (2026-03-10, furnished): guidance "**exclude[s] any impact from changes in FICO mortgage royalties**."
- **EFX FY2025 10-K (filed 2026-02-19): zero mentions of FHFA, VantageScore, score choice, or the FICO direct-license program.** Filed four months after the FICO announcement and seven months after the FHFA score-choice change, and silent on both. The tri-merge product is described (Online Information Solutions: "specialized credit reports that combine information from the three major consumer reporting agencies … commonly referred to as a tri-merge report") with no attached risk language.

**Press (rung-3, dated):**
- FICO press release 2025-10-01 (investors.fico.com): Mortgage Direct License Program — tri-merge resellers may "calculate and distribute FICO Scores directly … eliminating reliance on the three nationwide credit bureaus"; claims savings "up to 50% on per score FICO fees"; alternative "$10 per score" via existing bureau channel.
- FICO statement late 2024 (via press): 2025 mortgage royalty **$4.95 per score**, "fourth royalty increase … since 1989"; FICO defense: its royalty is ~15% of the typical $80-$100 tri-merge bundle. **Royalty figures appear in no filing** (confirmed by search of FICO 10-K/10-Qs).
- MBA letter to FHFA Director Pulte, dated Dec 12 (per CNBC 2026-02-22): credit reporting costs 2025 est. +20% vs 2024; 2026 projected +40-50%.
- FHFA Director Pulte (HousingWire, 2025): FICO "should make sure they're being as economical as possible"; communications with credit bureau CEOs "falling on deaf ears."
- CFPB: analyzing rise in mortgage closing costs including credit reporting costs, considering "possible rulemaking and guidance" (archived Chopra remarks to MBA; pre-2025 administration — weight accordingly).

## Read for the EFX run
The verification moat (209M employer-fed records, instant, no borrower friction) is attacked only obliquely: Experian has 1/3 the records, Argyle/Plaid have a different architecture (borrower-permissioned) that trades coverage certainty for cost. The nearer-term threat to bureau economics is not verification but the mortgage pipe: FICO going direct through Xactus and FHFA opening score choice both compress the tri-merge resale layer where the bureaus (EFX included) have been taking price. EFX's 10-K silence on FHFA/score-choice — where FICO devotes a full risk factor and TRU names the program — is itself a disclosure choice worth noting in Q3 (honesty) of the run.
