# Company Run — newcleo plc (Nasdaq: NWCL) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run. The brief departs from the canonical brief in two stated ways: the analyst derives the lines of
evidence and the competitors from the filings, and the primary documents are registration statements and prospectuses,
because the issuer has filed no 10-K or 20-F. Working folder: `Test Runs/_research 2026-10-17 NWCL/` (extracts in
`notes.md`; raw filings under `cache/`, gitignored).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session (overnight 2026-10-17), after the run was committed: `PORTFOLIO.md` read for this ticker; the operator does not hold NWCL.*

**Contamination declared.** The session's opening context showed the last five commit subjects of the repository; they
name another company's v5 re-run and its box. Nothing about this company was in them, and nothing in them was used. No
blind-listed file was opened, listed or searched. `Test Runs/` was not listed; the only paths written there are this
file and its research folder.

**Lines of evidence chosen, and why.** The prospectus's own Business, Risk Factors and MD&A sections, read for: (1) what
the company sells today and to whom (the subsidiaries' engineering, pump and component revenue), because a reactor
developer's present revenue is the only owner cash it has; (2) the licensing path and timeline (ASNR, NRC, the Slovak
and UK regimes), because the reactor and the MOX plant earn nothing until licensed and built; (3) the cash burn and the
funding, because the auditor and MD&A both raise going concern; (4) the capital structure after the combination (PIPE,
warrants, Class B earnout shares, the prepaid forward, stock pay), because it sets the share count and part of the cash;
(5) related-party arrangements and (6) litigation, because Q5 would read them. Competitors are the ones the Competition
section names.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.88 (close 2026-10-16; `tools/sources.py` price(), an aggregator quote, **flagged** under operator rule
  5). Beside it, the filer's own print: "On October 15, 2026, the closing price of our Ordinary Shares on Nasdaq was $6.37
  per share" (424B3 resale prospectus, 2026-10-16, accession 0001140361-26-039925, cover).
- **Shares by class:** `python Screens/cover_shares.py NWCL` returned "no periodic filing found (CIK 2131813)": the
  issuer has filed no 10-K or 20-F cover. Count taken from the latest filed document, the 424B3 of 2026-10-16
  (0001140361-26-039925), The Offering: "281,534,950 Ordinary Shares and 10,354,197 Company Warrants" outstanding "as of
  the date of this prospectus"; the same 281,534,950 is the closing count in the press release of 2026-10-02 (6-K
  2026-10-05, 0001140361-26-038557, ex 99.1). Not outstanding: 17,677,233 Class B earnout shares (convert only if the
  VWAP reaches $15.00 and $18.00 within five years), about 8,855,000 NextChem Warrants (earn-out, settled by set-off),
  and options and RSUs under the equity plan. No treasury share count is filed yet; the prepaid forward of 2026-09-11
  covers up to 7,000,000 of the outstanding shares and the pro forma accounts for it as treasury shares (IAS 32), so the
  economic count may be up to 7,000,000 lower; the run uses the filed 281,534,950 and says so.
- **Market cap:** 281,534,950 × $5.88 = **$1,655.4M** (at the $6.37 print, $1,793.4M).
- **Sovereign for the earnings currency:** the statements are in **euros** (IFRS as issued by the IASB). **3.671%**, ECB
  euro area AAA yield curve, 30-year spot (series YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), 2026-10-15
  (`tools/sources.py` sovereign('EUR')), the protocol's issuing-authority source for EUR.
- **Filings read** (operator rule 4): no 10-K or 20-F exists. Read: the 424B3 resale prospectus of 2026-10-16
  (0001140361-26-039925): Business, Competition, Legal Proceedings, Risk Factors on the forward and on liquidity, MD&A
  liquidity, Certain Relationships, the audited consolidated statements for FY2025 and FY2024 (Grant Thornton, Dublin,
  report dated 2026-06-02) and the unaudited interim statements to 2026-06-30, Note 27. The 6-K of 2026-10-05
  (0001140361-26-038557: H1 2026 press release and interim statements); the 6-K of 2026-10-06 (0000950103-26-015281:
  general meeting result on the forward). The 6-Ks of 2026-09-30 (0000950103-26-014872) and 2026-10-14
  (0000950103-26-015583) were read at the cover only. The proxy statement/prospectus 424B3 of 2026-08-10
  (0001140361-26-031950) was searched only for audited years before FY2024; it has none. The F-4 and its amendments, the
  F-1 of 2026-10-06 (superseded in content by the 424B3 of 2026-10-16), the 425s and the S-8 were not read. No annual
  report exists on any date before the listing.
- **One figure cross-checked against the filed statement:** cash and cash equivalents at 2026-06-30, **€66,540
  thousand**, the same in the press release (ex 99.1 of 0001140361-26-038557) and in the interim statement of financial
  position in the 424B3 (0001140361-26-039925); FY2025 cash, €105,270 thousand, the same in the audited balance sheet and
  the interim comparative column.
- `python tools/run.py NWCL`: "NWCL: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool found no tagged
  data for this new foreign issuer; every figure below is read from the filed statements.
- **Owner cash after every real cost, from the filed statements** (EUR thousands; operating cash flow less purchases of
  property, plant and equipment and of intangibles, less share-based payment, which the cash flow statement adds back):

  | | FY2024 | FY2025 | H1 2026 |
  |---|---|---|---|
  | Operating cash flow | (104,477) | (119,678) | (53,687) |
  | PP&E and intangible purchases | (49,463) | (45,863) | (26,970) |
  | Owner cash before stock pay | (153,940) | (165,541) | (80,657) |
  | Share-based payment | (8,316) | (14,895) | (21,010) |
  | **Owner cash after stock pay** | **(162,256)** | **(180,436)** | **(101,667)** |

  There is no five-year window: the company was founded in 2021, its first revenue came through acquisitions in 2023, and
  the audited statements cover two years. Every year filed is negative.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, and the test is "Would I be happy buying this
stock if the market closed for five years?" **[M1997-109]**. A buyer of this share today owns a claim on a reactor and a
fuel plant that do not yet exist, funded by a balance sheet the auditor qualified for going concern; with the market
closed, the owner would hold a business that must raise more money to reach its first reactor, and could not. The second
is who is paid to tell you: the prospectus is a resale document written to let holders sell, much of it carries the
issuer's market sizing (the IEA forecasts, a "non-binding" 9.2 GW pipeline), and the rows say "don’t ask the barber
whether you need a haircut" **[M2011-083]** and that projections are not consulted **[M1995-050]**. No macro view
enters: the run takes no position on nuclear policy or power demand. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the auditor's report on FY2025 carries "Substantial doubt over going concern"; (2) revenue fell from
€46.7M (FY2024) to €32.8M (FY2025) before rising in H1 2026; (3) the MD&A says the LFR and MOX solutions "are not
expected to generate revenues for several years" and "we cannot accurately predict the amount, timing or duration of
funding required"; (4) about $74.6M of the trust went to the forward counterparty, not to the company; (5) the FY2025
income statement labels €9,744 thousand of SG&A "from related party" while Note 27 totals €313 thousand of related-party
transactions; (6) Elysia Capital S.r.l. is said to be beneficially owned by the chief executive in Certain
Relationships and by Carlo Zuccaro in Note 27 (all 424B3, 0001140361-26-039925).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if it is bought with his own money, unlevered and sized so that a total
loss is borne: "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. The run notes that the issuer's own cash
cannot carry it to its first reactor, so a position here is a claim that can go to zero; that is a fact about the
target for Q9, and the rule binds only how the buyer would finance and size it.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10 years"
**[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look like in five or
10 years" **[M2012-065]**; "the first question is, can I understand it?" **[M1995-051]**. Applied to the filings
(424B3 resale prospectus, 2026-10-16, accession 0001140361-26-039925, unless another document is named):

- **What the business is today.** By its own description "a development- and design-stage company that is preparing its
  flagship products for market" (MD&A). It reports one operating segment, "the research and development of LFRs". Its
  revenue (FY2024 €46.7M, FY2025 €32.8M, H1 2026 €19.4M) comes from subsidiaries bought from 2023 (S.R.S engineering,
  Fucina components, Rütschi pumps): "We commenced initial revenue-generating activities through our historical
  acquisitions in 2023 and are concurrently undertaking significant R&D efforts to develop our strategic LFR and MOX
  solutions, which are not expected to generate revenues for several years." The parts convention of Q2 does not apply:
  the filer reports one segment and no part's profit; every period shown is an operating loss (FY2025 €139.9M).
- **Test 1, where will it be in ten years.** The filed timeline: PRECURSOR, a non-nuclear 10 MWt testbed, "expected by the
  end of 2026"; "initial LFR deployment and related MOX fuel manufacturing activities will occur in the 2030s"; the first
  MOX plant "by 2031"; the ASNR opinion on the reactor's safety features is still awaited; in the United States only
  pre-application engagement and Regulatory Engagement Plans exist; Slovakia, Lithuania, Virginia and the rest are
  memoranda, letters of intent or feasibility studies, each "non-binding" or subject to conditions; the 9.2 GW pipeline
  "does not represent contracted backlog, committed revenue or binding customer obligations". Ten years out the company
  may have one first-of-a-kind reactor licensed and operating, or none. No fix on earning power is available.
- **Test 2, the key variables and how predictable they are** **[M1998-044]**: whether and when the reactor and the MOX
  plant are licensed in France and the United States; the cost and schedule of a first-of-a-kind lead-cooled reactor and
  plutonium fuel plant; access to plutonium feedstock (the DOE programme is "advanced negotiations", led by Oklo);
  whether any customer signs a binding order; and the funding, "$2.2 billion and $2.6 billion" for the contemplated U.S.
  fuel facility alone, with "no guarantee that we will obtain financing". None is predictable from the filings.
- **Test 3, do the past statements tell the future ones** **[M2000-104]**: no. The subsidiaries' engineering and pump
  revenue says nothing about the economics of licensing reactor IP and selling MOX fuel, which have never been earned.
- **Test 4, important and knowable** **[M2006-076]**: the deciding facts are important and not knowable today.
- **Test 5, would the insiders write it down** **[M2000-105]**: the company itself declines to: "At this stage, we cannot
  accurately predict the amount, timing or duration of funding required to successfully develop, construct and operate
  its LFRs or related facilities." (MD&A, Future Funding Requirements).
- **Test 6, can I name the winner, not just the industry** **[M2012-067]**, **[L2009-005]**: the filer cites the OECD
  NEA dashboard, on which its design ranks 11th of 63 SMR designs, and names rivals with "substantially greater financial,
  technical, commercial, manufacturing and regulatory resources". The industry may grow; who wins cannot be named.
- **Test 9, doubt** **[M2002-092]**: there is no doubt to resolve; the economics are outside the perimeter on the
  company's own words.

**The routing.** Two passages of Q1 reach this name, and both close the file.
1. **Start-ups are ruled OUT by kind.** "Start-ups are not our game." **[L2007-015]**; "I say, “We don’t do startups.”
   They don’t exist. Well, if you blot out startups, there’s a whole layer of complexity that goes out of your life."
   **[M2008-088]**. newcleo was founded in 2021, has never earned its business's first euro of reactor or fuel revenue,
   and expects its first reactor in the 2030s: it is a start-up on its own description, whatever its listing and its
   purchased subsidiaries. The 2000 letter names the case and its label: "This kind of uncertainty frequently occurs when
   new businesses and rapidly changing industries are under examination. In cases of this sort, any capital commitment
   must be labeled speculative." **[L2000-026]**.
2. **The ten-year economics cannot be foreseen**, which by itself would send the file to TOO HARD: "if we don’t have the
   faintest idea what the future stream is going to look like, we don’t have the faintest idea what it’s worth, now."
   **[M1994-077]**; "If something is not very predictable, forget it." **[M1998-044]**; "a business that must deal with
   fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**.
   The cause would be NATURE, not WORK: the insiders' own filing will not write the forecast down (test 5), and no
   reading of a further document could supply a reactor that has not been licensed or built **[M2008-086]**.

The box follows the first passage, because Q1's list of what it rules OUT names start-ups by kind and the row says they
"don’t exist" for the analyst before any reading **[M2008-088]**; the second passage is recorded as concurring, not as
the deciding ground (see What in the framework was wrong or unclear). The OUT is on the kind of business and the stage
it is at, not a finding that the technology fails: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t
selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. Price does
not reopen it.

**VERDICT: OUT** (a start-up, ruled out by kind at Q1 **[L2007-015]**, **[M2008-088]**; the ten-year economics are
also unforeseeable on the company's own statement **[M2000-037]**, **[M2000-105]**, **[L2000-026]**). The file closes
here. Q2 to Q10 and Q12: NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed the file OUT).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read and are recorded under AFTER THE STOP).
## Q5 — WHO RUNS IT? NOT REACHED (integrity facts recorded below, not judged).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (the computation below is headed as the protocol requires).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q1**: a start-up, ruled out by kind (**[L2007-015]**, **[M2008-088]**), its ten-year economics unforeseeable
on its own filing (the concurring ground, which alone would have closed TOO HARD (NATURE)). No Q7 range exists: no
period filed has positive owner cash. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**. The source is the 424B3
resale prospectus of 2026-10-16 (0001140361-26-039925) unless another document is named. EUR thousands unless stated.*

**Bearing on Q2 (the competitors the prospectus names).** The Competition section names NuScale's Power Module, GE
Vernova Hitachi's BWRX-300, X-energy's Xe-100, TerraPower's Natrium and Oklo's Aurora. It says that "Many of our current
and potential competitors have substantially greater financial, technical, commercial, manufacturing and regulatory
resources than we do". The SEC filers among them, with figures from SEC companyfacts (XBRL transcription of the 10-Ks,
not read against the filed statements; USD millions):
- NuScale (CIK 0001822966; FY2025 10-K accession 0001822966-26-000018): revenue 2022 11.8, 2023 22.8, 2024 37.0, 2025
  31.5; operating loss 2022 230.0, 2023 275.6, 2024 138.7, 2025 689.6; operating cash outflow 2022 148.6, 2023 183.3,
  2024 108.7, 2025 459.6. The 2020 and 2021 tagged values look like the pre-merger shell's and are not used.
- Oklo (CIK 0001849056): no revenue tag in any year; operating loss 2022 1.8, 2023 4.3, 2024 52.8, 2025 139.3; operating
  cash outflow 2023 10.8, 2024 38.4, 2025 82.2.
- X-energy (CIK 0002088896, ticker XE) files with the SEC, but no annual tagged figures were found and its registration
  statement was not read.
- Named rivals with no separate figures: TerraPower has no ticker in the SEC ticker map. GE Vernova files, but the
  BWRX-300 is not a reported segment, so there is no comparable figure.
In no year shown does a named pure-play rival earn an operating profit. None of them, and not the filer, has returns over
a full cycle yet.

**Bearing on Q3 and Q4 (the balance sheets, every one filed).** Only FY2024 and FY2025 are audited, with H1 2026
unaudited. Equity at 2023-12-31 appears only as an opening balance. Eight to ten years of balance sheets do not exist,
since the company was founded in 2021. (n/r: not reported in the documents read.)

| | 2023-12-31 | 2024-12-31 | 2025-12-31 | 2026-06-30 |
|---|---|---|---|---|
| Cash and equivalents | n/r | 192,714 | 105,270 | 66,540 |
| Trade receivables, contract and other assets | n/r | 64,018 | 62,314 | 77,768 |
| of which contract assets | n/r | 14,835 | 20,938 | n/r |
| Other non-current receivables | n/r | 15,820 | 35,207 | 34,871 |
| Goodwill plus intangibles | n/r | 83,717 | 80,335 | 80,041 |
| Property, plant and equipment | n/r | 58,783 | 93,436 | 115,999 |
| Borrowings (current plus non-current) | n/r | 4,042 | 18,889 | 18,426 |
| Lease liabilities | n/r | 21,206 | 18,787 | 18,212 |
| Trade and other payables | n/r | 52,116 | 83,808 | 60,055 |
| Total equity | 326,454 | 361,243 | 296,928 | 320,223 |
| Accumulated deficit | (75,619) | (185,782) | (324,123) | +234,695 "retained earnings" |

What moved:
- Cash fell by about two thirds in eighteen months. Equity was held up by share issues (proceeds of €61,985 in FY2024,
  €31,637 in FY2025 and €45,121 in H1 2026) and by €38,577 of redeemable bond subscriptions in FY2025.
- Goodwill and intangibles from the 2023 acquisitions are about a quarter of equity.
- Contract assets rose from €14,835 to €20,938 in FY2025, while revenue fell from €46,743 to €32,769.
- Other non-current receivables doubled. They are mostly an R&D tax credit (€13,855), grants (€9,273) and "Purchases on
  behalf of ENEA" (€9,319), "expected to be recovered after 2025 from ENEA".
- The H1 2026 "retained earnings" of +€234,695 follow a share premium reduction of €730,510 transferred to retained
  earnings. The accumulated losses did not reverse.

On controls, the company and its auditor report "significant deficiencies in our internal control over financial
reporting, information technology, and revenue disclosure cut-off and contract existence controls" (Risk Factors). The
records for 2024 "were not maintained in a sufficiently complete and timely manner at the time of audit requests".

Stock pay was €8,316 in FY2024, €14,895 in FY2025 and €21,010 in H1 2026 (against €4,975 in H1 2025). The filer puts the
rise down to share-based payment and "transaction incentives payable on completion". D&A added back was €13,121
(FY2024) and €16,931 (FY2025). The H1 2026 release does not feature EBITDA; it features "Tangible Capital Expenditures"
and the net loss.

**Bearing on Q5 (integrity facts, recorded, not judged).**
- The Italian head office in Turin is leased from Isola S.r.l., which the chief executive, Stefano Buono, controls with
  his spouse through BuonoLopera S.r.l. Lease costs were €0.5M in FY2025 and €0.4M in FY2024. In 2024 there was also a
  rental with Planet Idea S.r.l. (€0.2M), owned by Planet Smart City, of which Mr Buono is chairman.
- **The same prospectus names two different owners for one counterparty.** Certain Relationships: "Elysia Capital S.r.l.
  is a company beneficially owned by Stefano Buono, our Chief Executive Officer, through BuonoLopera S.r.l., together
  with his spouse." Note 27 of the audited statements: "Elysia Capital Srl is a company beneficially owned by Carlo
  Zuccaro." (Mr Zuccaro was a director until January 2025.) The amount is small: €24 a year of income.
- **The income statement and its related-party note do not agree.** The FY2025 income statement labels "Selling,
  General and Administrative expenses (2025: €9,744; 2024: €7,327 from related party)". Note 27 totals related-party
  transactions at (€313) in 2025 and (€485) in 2024, and ends "Except for the information disclosed above, we have not
  undertaken any significant transactions with members of the Board, the executive management or the major
  shareholders". The sections read do not explain the difference. It may be key-management pay; that was not verified.
- The control deficiencies above, on revenue cut-off and contract existence.
- The auditor's going-concern paragraph on FY2025: "the Company has suffered recurring net losses and cash outflows from
  operating activities and has an accumulated net deficit". The interim statements say the material uncertainty "no
  longer exists" on the strength of the business combination.
- The insiders' cost: the Sponsor's 4,404,951 shares were acquired "at purchase prices as low as approximately $0.0001
  per share", and "certain of our shareholders were issued Ordinary Shares at purchase prices as low as approximately
  €0.01 per share" (cover). The resale registration covers 71.1% of the outstanding shares.
- The H1 2026 release states gross proceeds of "approximately $247 million" ($31M from the trust plus the $216M PIPE).
  The MD&A states $322.1M, with $106.1M from the trust, of which $74.6M was "applied to the prepayment under the Forward
  Purchase Agreement". The two figures reconcile, but the release does not mention the forward.
- Litigation: "We currently do not have any claims, lawsuits or proceedings against us that, individually or in the
  aggregate, would be considered material" (Legal Proceedings).

**Bearing on Q6 (the money and the owners).**
- Funds raised since founding: "over $1 billion" (release of 2026-10-02).
- Shares were issued in every period read: an October capital raise, a pre-PIPE financing, and a July 2026 raise of
  3,994,146 shares at €4.10. As far as the sections read show, that price is in the pre-consolidation share count; the
  share-consolidation ratio was not read.
- After closing: 281,534,950 shares; 10,354,197 warrants at $11.50; about 8,855,000 NextChem warrants; options and RSUs.
- The earnout: 17,677,233 Class B shares that convert at $15.00 and $18.00 VWAP within five years, plus "Earnout Bonus
  Options and Earnout Bonus RSUs" of 10% of the existing awards.
- The prepaid forward with Tech Opportunities LLC (2026-09-11) covers up to 7,000,000 shares. The prepayment was about
  $74.6M from the trust, and maturity is up to 24 months. If not physically settled, it settles in cash at "the lesser
  of (a) 95% of the daily VWAP of the Shares on the applicable exchange and (b) the Reset Price". The company states
  "there can be no assurance that the settlement amounts we receive under the Forward Purchase Agreement will offset the
  Prepayment Amount in full". The general meeting of 2026-10-06 approved the off-market purchase (6-K
  0000950103-26-015281).
- Acquisitions: Fucina, S.R.S and Rütschi from 2023 on, and Bonifait Pesage signed (equity value €1.8M, 45% paid in
  shares). The filer says "We may selectively pursue acquisitions".

**Bearing on Q7.** COMPUTATION, NOT A CLEARANCE.
- Owner cash after every real cost was (€162,256) in FY2024, (€180,436) in FY2025 and (€101,667) in H1 2026 (Step 0). No
  period filed has positive owner cash.
- The business that is to earn it (reactor IP licences and MOX fuel) has no revenue and is "not expected to generate
  revenues for several years".
- Q7's convention builds the range from five years of owner cash. Here there is no window and no positive base for
  either end case.

**No value range and no fair price are reported.** Neither can be built without inventing the cash stream: "if we don’t
have the faintest idea what the future stream is going to look like, we don’t have the faintest idea what it’s worth,
now." **[M1994-077]**; "If, however, we lack the ability to estimate future earnings" [...] "we simply move on to other
prospects." **[L2013-012]** (the row's replacement characters are left out of the quotation).

Against the price: the market values the equity at $1,655.4M. Preliminary unaudited cash at 2026-09-30 was about €233M
(release of 2026-10-02). At the June 30 convenience rate of $1.14 to the euro, that is about $266M, so about $1.39bn of
the price is paid for a cash stream that has not begun.

**Bearing on Q9 (the target's debt and exposures).**
- At 2026-06-30, borrowings were €18,426 and lease liabilities €18,212.
- The forward prepayment is at risk.
- The company has "commitments that require us to make substantial capital contributions or other investments,
  including before such arrangements generate revenues or positive cash flows".
- The contemplated U.S. fuel facility would cost "between $2.2 billion and $2.6 billion" over five to six years.
- Cash outflow before financing was about €165M in FY2025, against about €233M of cash at 2026-09-30.
- The MD&A's own words: "These conditions indicate the existence of a material uncertainty that may cast significant
  doubt on our ability to continue as a going concern."

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 4e43dc10); written question by question; committed after each
      (Step 0 at 7bbeb7cf, Q1 at 24b268de, this section in the closing commit).
- [ ] If dispatched to an analyst: the brief allowed the per-question commits (it did). Whether the lock was held and
      whether the run is folded are the dispatching session's to tick (operator rule ten). A run not in the register
      binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. The commit subjects seen in the
      opening context are declared under contamination and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (checked
      by `Test Runs/_research 2026-10-17 NWCL/check_ids.py`). Every filing fact has its accession, and no number stands
      without a filing or a row. The competitor figures are XBRL transcriptions, flagged as such.
- [x] The order was kept. Q1 failed and closed the run; nothing after it is a clearance; the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash flow less all capital
      spending and less stock pay, from the filed cash flow statements. The sovereign is from the issuing authority
      (ECB); the price is an aggregator quote, flagged, with the filer's own print beside it.
- [x] Contrary evidence was written down as it was found (the six items under THE FOUNDATIONS). The facts for later
      questions are under AFTER THE STOP, and the integrity flag is in the box line.
- [x] No row dated after the anchor is cited (the run is dated today and has no point-in-time anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used; it returned none.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**Two Q1 routings fit, and they name different boxes.** Q1's list of what it rules OUT names start-ups
(**[L2007-015]**, **[M2008-088]**). Its routing paragraph sends a business whose ten-year economics cannot be foreseen to
TOO HARD, and **[L2000-026]** joins the two cases ("new businesses and rapidly changing industries"). The text does not
say which governs when both apply. This run chose OUT on the start-up item, because Q1's list names the kind and the
item was left in place when the case of 2026-10-10 moved the continued-invention item to TOO HARD. TOO HARD (NATURE) is
recorded as the concurring ground. The choice changes what follows: an OUT is re-looked like any OUT, while a NATURE box
is closed and a lower price never reopens it. A rule is needed.

**The text does not define a start-up.** This run read it as a company whose own business has not yet earned its first
revenue, so purchased subsidiaries with revenue of their own did not make newcleo something else. Another analyst could
read the €32.8M of subsidiary revenue the other way.

**Two smaller gaps.** First, the template's Step 0 assumes a 10-K or 20-F cover and a five-year window; a new foreign
issuer has neither. The share count came from the prospectus, and the five-year line was answered with two audited
years and a half. Second, only the brief says what to report "where the business has no owner cash history"; Part VII
assumes a range can always be computed beneath a stop.
