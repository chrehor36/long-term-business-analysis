# Company Run — Aperam S.A. (Euronext Amsterdam: APAM; New York Registry Shares, OTC: APEMY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (this name files no
SEC accession; see Step 0); a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-13, after the run was committed: not held (`PORTFOLIO.md` carries no line for APEMY, APAM or Aperam).*

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's stated departures: the
name files nothing with the SEC (the operator's choice of 2026-10-10 to run foreign names), and the lines of evidence were
derived by the analyst from the annual report rather than listed by the dispatcher.

**Contamination declared (seen by accident, not used).** The session's opening context showed recent commit subjects about
another company's run (an industrial supplier closed OUT at Q2 on 2026-10-13), untracked research-folder names of other
runs in the git status, and memory-index lines describing the queue in general terms (a count of v4.1 gate-clearers,
"nothing buyable", a paused wave). None names this company, its former names or its ticker. Nothing of them was opened
or used. No file under `Test Runs/` other than this file and its research folder was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING

- **Tools.** `python tools/run.py APEMY` returned "APEMY: not an SEC filer. Use the evidence ladder [...] This is
  UNRESEARCHED, not UNKNOWABLE." `python Screens/cover_shares.py APEMY` returned "NOT AN SEC REGISTRANT". All arithmetic
  below is by hand from the company's own reports, shown in `_research 2026-10-13 APEMY/scripts/q7_computation.py` and its
  output file.
- **Price:** EUR 38.50, APAM on Euronext Amsterdam, last trade 2026-10-13 15:35 UTC (previous close 2026-10-12 EUR 38.30).
  **Aggregator, flagged** (Yahoo chart feed via `tools/sources.py`, live quote only, operator rule 5); Euronext's own quote
  endpoint returned an encrypted payload and could not be read. APEMY on OTC Pink: USD 42.93, last printed 2026-10-12
  (aggregator, flagged; thin and stale). Record: `_research 2026-10-13 APEMY/price_2026-10-13.txt`.
- **Shares:** 73,184,570 issued less 716,887 treasury = **72,467,683 outstanding**, at 2026-09-30, from the company's
  Share Capital & Voting Rights page (aperam.com, read 2026-10-13). Checked against the Annual Report 2025 statement of
  financial position: 73,184,570 issued, 842,907 treasury, 72,341,663 outstanding at 2025-12-31; the difference (126,020)
  is treasury shares delivered to employee plans in 2026, and no share cancellation or buyback is disclosed after
  2024-05-29 (the last cancellation, 4,852,118 shares of the 2022 programmes). One class of ordinary shares, no par value.
  The significant shareholder (a trust for the Mittal family, through Value Holdings II S.a r.l.) holds 29,513,459 shares,
  40.33% of issued, 40.73% of voting rights.
- **ADR ratio:** **1:1.** The listed US instrument is not a depositary receipt but the ordinary share itself, registered
  on the New York Register kept by Citibank, N.A.: "ordinary shares registered on the New York Register are referred to as
  `New York Registry Shares'" (Annual Report 2025, share capital section). The company's ADR page gives Citibank as the
  contact and no ratio. Check by price: USD 42.93 / 1.1181 (ECB, 2026-10-12) = EUR 38.40 against APAM's EUR 38.30 close
  that day.
- **Market cap:** 72.467683 million × EUR 38.50 = **EUR 2,790 million**.
- **Net financial debt, latest filed date:** **EUR 993 million at 2026-06-30** (short-term debt 224 + long-term debt 1,103
  less cash 334; lease obligations are inside the debt lines), Q2 2026 results release, 2026-07-30. No subsequent event
  that changes it is stated; the release expects it "to remain flat at Q3 2026". Enterprise value at the price:
  2,790 + 993 = **EUR 3,783 million**.
- **Sovereign for the earnings currency (EUR):** **3.76%**, ECB euro area AAA yield curve, 30-year spot
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), dated 2026-10-12, via `python tools/sources.py` (record:
  `sovereign_2026-10-13.txt`). EUR/USD for the ADR figures: ECB reference rate 1.1188, 2026-10-13 (`fx_ecb_2026-10-13.txt`).
- **Filings read** (operator rule 4; no accession numbers exist, so document and date stand in their place):
  - Annual Report 2025 (fiscal 2025 and 2024), published 2026-03-26 per the company's press release of that date
    (`PR_Annual_Report_2025_EN.pdf`, fetched from aperam.com). The PDF itself (`Aperam_AnnualReport_2025.pdf`) was taken as
    a byte copy of the aperam.com file from the Wayback Machine snapshot of 2026-10-09 (sha256 466834e9...ba835), because
    aperam.com refused connections from 19:35 local time onward after a partial first download.
  - Annual Reports 2024, 2023, 2021, 2019 and 2017, same route (aperam.com file names `AnnualReport_2024_compressed.pdf`,
    `Annual_Report_2023.pdf`, `Annual_Report_2021.pdf`, `Annual Report 2019.pdf`, `Annual_Report_2017__0.pdf`; Wayback
    snapshots 2025-05-01, 2024-05-28, 2023-05-14, 2026-04-21, 2023-05-14). Together they give fiscal 2016 to 2025. Fiscal
    2016 and 2017 are reported in **US dollars** (the reporting currency changed to the euro in 2018); the 2018 annual
    report, which would restate 2017 in euros, was not archived and could not be fetched.
  - Q2 2026 results release, 2026-07-30 (EQS regulatory dissemination, read via Investegate; the aperam.com PDF could not
    be fetched). **The Half-Year Report 2026 (`Aperam_HYR_2026.pdf`) was not obtained**: aperam.com refused connections and
    no archive copy exists. Its condensed statements are taken from the release, which is unaudited.
  - The company's investor pages (results, spin-off, ADR, share capital, share buyback), read 2026-10-13 before the site
    closed.
  - Universal Stainless & Alloy Products (CIK 931584): the 8-K of 2025-01-23 (accession 0001193125-25-011290, exhibit 99.1),
    the DEFM14A of 2024-11-27 (accession 0001193125-24-267249), and its XBRL company facts for 2014 to 2023 (screening only).
  - The named rival Outokumpu, from its own Annual Report 2025 (financial statements part, Group key figures) and its own
    financial statements releases for 2019 and 2020 (outokumpu.com). Not an SEC filer.
- **The spin-off, dated from the annual report:** Aperam was incorporated on 9 September 2010 to hold ArcelorMittal's
  stainless and specialty steels businesses; ArcelorMittal's shareholders approved the spin-off at an extraordinary general
  meeting on 25 January 2011 (Annual Report 2025, shareholder information); the investor page gives the exchange ratio of
  20 to 1 and first trading on 31 January 2011.
- **One figure cross-checked against the filed statement:** 2025 sales of EUR 6,080 million in the Annual Report 2025
  consolidated statement of operations equal the "sales of EUR 6,080 million" in the company's press release of
  2026-03-26. A second check found a restatement: 2024 capital expenditure is EUR 152 million in the Annual Report 2024 and
  EUR 139 million in the 2024 column of the Annual Report 2025 (bearer plants of 12 million moved to biological assets, note
  2); the restated figure is used, with the biological-asset line deducted beside it, so the total is unchanged in substance.
- **Owner cash after every real cost, by year (EUR million; computed by hand; net cash from operations less capital
  expenditure, less biological assets bought, less lease principal repaid; working capital and cash taxes inside it):**

  | Year | Operating cash | CapEx | Bio. assets | Lease principal | Owner cash, equity-only | Net interest paid | Owner cash, all-equity | Businesses bought (cash) | D&A and impairment |
  |---|---|---|---|---|---|---|---|---|---|
  | 2018 | 295 | (192) | in CapEx | (1) | 102 | 5 | 107 | -- | 143 |
  | 2019 | 400 | (151) | in CapEx | (8) | 241 | 5 | 246 | -- | 150 |
  | 2020 | 303 | (109) | in CapEx | (9) | 185 | 7 | 192 | -- | 144 |
  | 2021 | 550 | (152) | in CapEx | (9) | 389 | 4 | 393 | (31) ELG | 144 |
  | 2022 | 642 | (285) | (11) | (14) | 332 | (3) | 329 | -- | 186 |
  | 2023 | 471 | (250) | (51) | (15) | 155 | 5 | 160 | -- | 204 |
  | 2024 | 280 | (139) | (26) | (19) | 96 | 26 | 122 | -- | 229 |
  | 2025 | 422 | (137) | (37) | (25) | 223 | 40 | 263 | (415) Universal | 259 |

  Five-year average 2021 to 2025: equity-only 239, all-equity 253, before acquisitions; after acquisitions, all-equity 164.
  Stock pay is inside these figures as a charge in net income and an add-back in operating cash (share-based payments of
  EUR 4 to 5 million a year, statement of changes in equity); it is a real cost of about that size per year and is not
  material to the totals. No `tools/run.py` lines were used, because none were produced.

## THE FOUNDATIONS (not a gate)
A share is a business: the question here is what a stainless and specialty steel producer will earn over a decade, not
where the quotation goes, and the macro forecast (nickel, Chinese capacity, European trade policy) is not made:
"macro conclusions are — just never enter into the discussion." **[M2000-094]**; what counts is "the average
profitability of the business over time and how strong its competitive mode is" **[M2015-016]**. The margin of safety is
the attitude Q7 would test: "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**. The analyst's habits govern the reading: the research is aimed "to possibly reject your original
hypothesis" **[M1998-144]**, and the list asked first is "What do I not know that I need to know?" **[M1999-129]**.
**Contrary evidence, written down as found** **[M1997-127]**:
1. (Step 0) Operating income was EUR 16 million on EUR 6,080 million of sales in 2025 and EUR 129 million in 2024; net income
   in 2023 to 2025 (446 in total) exceeds pre-tax income (120 in total) because of EUR 326 million of income tax benefits,
   mostly the recognition of deferred tax assets on tax losses (EUR 190 million in 2024 and 130 million in 2025, "primarily
   in Luxembourg", note 8).
2. (Step 0) Capital expenditure has run below depreciation since 2024 (139 against 229; 137 against 259).
3. (Q2) The company's own description of its market: base price "negotiated with customers and depends on market supply and
   demand"; "global structural overcapacity has stabilised at a high level"; "Persistently low NPI (Nickel-Pig-Iron) prices
   also supported low production costs for stainless steel and prevented stainless steel prices from recovering"; "Import
   pressure increased in Europe during 2025 despite weak demand" (Annual Report 2025, market and pricing sections).
4. (Q2) Brazil, the segment's stronger leg, is described by the company as a "Well-protected market with a long history of
   fighting unfair trade practices"; the protection is trade law, not a cost advantage.
5. (Q2, Q6) Universal Stainless was bought at an enterprise value of about USD 535.7 million, "10.6x to the latest 12 months
   adjusted EBITDA" (DEFM14A); its own filings show operating cash of about USD 57 million against capital spending of about
   USD 111 million over 2014 to 2023 (XBRL, 2015 operating cash missing), and Alloys & Specialties operating income fell from
   EUR 70 million in 2024 to EUR 38 million in 2025, the first year with Universal inside it.
6. (Q4, Q5) Brazilian tax assessments against Aperam South America, the largest R$1.2 billion (EUR 202 million) on
   corporate income tax for 2021 and 2022 (note 28).

## THE STANDING RULE
A part-interest bought for cash, unlevered, puts the buyer at no risk of ruin from this name; the rule binds the buyer's
financing and sizing, "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The foundation's test of
temperament applies with force to a cyclical producer whose quotation has ranged from EUR 29.50 to 53.85 in a year: the
buyer must be "prepared, when you buy a stock, to have it go down 50 percent — or more — and be comfortable with it"
**[M2020-022]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The lines of evidence chosen** (the brief's departure: derived by the analyst from the Annual Report 2025's business
description and segments, principal risks and management report, the equivalents of Items 1, 1A and 7): (i) the four
segments and their margins over 2016 to 2025; (ii) the stainless pricing mechanism (base price plus alloy surcharge) and
what it did through the 2021 to 2022 inflation; (iii) the market and competition section (overcapacity, imports, named
rivals); (iv) trade measures (EU safeguard, anti-dumping, CBAM; Brazilian duties); (v) the acquisitions and their goodwill
(ELG 2021, Universal 2025); (vi) debt, leases and covenants (note 18); (vii) buybacks and the prices paid; (viii) stock pay
(note 23); (ix) litigation and tax claims (note 28); (x) the tax line and deferred tax assets (note 8).

- **What the business is.** Four segments: Stainless & Electrical Steel (flat stainless and electrical steel from mills in
  Belgium, France and Timoteo, Brazil, 2.5 million tonnes of capacity), Services & Solutions (distribution and processing),
  Alloys & Specialties (nickel alloys and specialty steels: Imphy, VDM, and since 2025-01-23 Universal Stainless), and
  Recycling & Renewables (ELG scrap trading and processing, and BioEnergia's eucalyptus charcoal in Brazil). Group
  shipments were 1.92 million tonnes in 2016 and 2.29 million in 2025, the rise from the acquisitions.
- **The key variables and whether they are foreseeable.** The economics turn on the base price of commodity stainless
  against the cost of making it, in Europe and Brazil, against Chinese and Indonesian supply. The speakers do not forecast
  the commodity price: "We don’t think we can predict commodity prices." **[M2016-025]**; "I really didn’t think we could
  guess the price of oil" **[M2011-044]**. The framework's commodity-business paragraph makes that dependence no STOP at Q1:
  the business is judged off its figures, "So if you can’t make a decision on something like PetroChina off the figures,
  forget about going further" **[M2008-069]**, and its cost position is the question for Q2, "we would measure it, probably,
  more by cost of production than we would by whether copper was selling for $2.00 a pound or a dollar a pound"
  **[M2006-004]**.
- **Can the figures tell me the future figures?** Yes, in the sense the definition asks, "a reasonable fix on about what the
  earning power and competitive position will look like in five or 10 years" **[M2012-065]**: ten years of segment
  results, shipments, average selling prices, and the company's own account of the field are on file, and they tell a
  consistent story of a cyclical, price-taking producer. The technology is old and slow-moving; nothing here is the
  fast-change case that Q1 routes to TOO HARD.
- **Parts.** Under the business-of-parts convention the deciding part is Stainless & Electrical Steel (70.7% of five-year
  operating profit; table at Q2), and it is understood by the tests above. Alloys & Specialties is the least familiar part
  (aerospace and energy alloys) but does not decide.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The doubt
  here is not about what the business is or how it earns; it is about whether its castle stands, which is Q2's question
  **[M1997-148]**.

**VERDICT: IN.** The economics can be read off the figures **[M2008-069]**, **[M2012-065]**; the commodity dependence goes to
Q2's cost test, not to a STOP here **[M2006-004]**, **[M2016-025]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**

**The parts table** (operating income by segment, EUR million, from the segment notes of the Annual Reports 2021, 2023,
2024 and 2025; five-year window 2021 to 2025):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year total | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Stainless & Electrical Steel | 774 | 689 | (25) | 75 | 19 | 1,532 | 70.7% | open (below) | **yes**, more than half |
| Services & Solutions | 196 | 79 | 10 | 24 | 9 | 318 | 14.7% | distribution of the same commodity; not judged | no |
| Alloys & Specialties | 50 | 44 | 40 | 70 | 38 | 242 | 11.2% | not judged | no |
| Recycling & Renewables | -- | 27 | 84 | (2) | (38) | 71 | 3.3% | not judged | no |
| Others / eliminations | 22 | 51 | (20) | (38) | (12) | 3 | 0.1% | -- | -- |
| **Group** | 1,042 | 890 | 89 | 129 | 16 | 2,166 | 100% | | |

2021 group operating income includes a preliminary bargain purchase gain of EUR 119 million on ELG (statement of
operations, 2021); ELG was consolidated from 2021-12-31, so Recycling & Renewables shows no 2021 result. Without the gain
the deciding share is about the same (1,532 of 2,047, 74.8%). Q2 reads each part's castle separately, since "lumping them
together [...] impedes analysis" **[L2008-005]**, and the file closes on the deciding part.

**The deciding part's margin over the whole span** (Stainless & Electrical Steel operating income over its sales including
intersegment sales; 2016 and 2017 in US dollars):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Segment sales | 3,510 | 4,198 | 3,840 | 3,352 | 2,897 | 4,369 | 5,510 | 4,229 | 4,007 | 3,823 |
| Operating income | 265 | 366 | 296 | 152 | 159 | 774 | 689 | (25) | 75 | 19 |
| Margin | 7.5% | 8.7% | 7.7% | 4.5% | 5.5% | 17.7% | 12.5% | (0.6)% | 1.9% | 0.5% |

**The castle tests, each with its filing fact.**
1. **The castle questions.** What keeps it standing is, on the company's own account, trade protection and integration,
   not a reason the customer chooses it at a higher price. The market is "a global one", stainless "is suitable for
   transport over long distances, as logistics costs represent a small proportion of overall costs", and "prices for
   commoditised stainless steel products evolve similarly across regions" (Annual Report 2025, stainless steel pricing).
2. **The money test.** Money has already attacked: "global structural overcapacity has stabilised at a high level, driven by
   additional capacity in China and Southeast Asia", with slab overcapacity in China of 10 million tonnes and close to 20
   million globally (Annual Report 2025, production and capacity), against Aperam's 2.5 million tonnes of flat capacity. The
   See's test is answered the other way: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
3. **Pricing power and the agony before a rise.** The base price is "negotiated with customers and depends on market supply
   and demand"; the alloy surcharge passes nickel, chromium and molybdenum through (Annual Report 2025). Through the last
   inflation the segment's margin rose to 17.7% (2021) and 12.5% (2022) and then fell to (0.6)%, 1.9% and 0.5% (2023 to
   2025) as prices fell with imports; in 2025 "prices and producer margins eroded further" and "Weak demand, falling
   surcharges and heightened import competition converged". The surcharge is a pass-through of a cost every rival also
   passes through, not the power the rows name: "over time the businesses with strong competitive positions manage to pass
   through increases in raw material costs" **[M2005-017]**; and the price behaviour over the cycle is the evidence, "you
   learn a lot about the durability of the economics of a business by observing the behavior of — the price behavior."
   **[M2005-020]**.
4. **Unit volume.** Group shipments 1.92 million tonnes (2016), 1.94 (2017), 1.97 (2018), 1.79 (2019), 1.68 (2020), 1.82
   (2021), 2.31 (2022, with ELG), 2.20 (2023), 2.29 (2024 and 2025, with Universal from 2025). The deciding segment shipped
   1,668 thousand tonnes in 2025 including intersegment. No organic volume growth across the decade.
5. **The low-cost position.** This is the commodity paragraph's test, and the rows put it plainly: "commodity businesses have
   risk unless you’re the low-cost producer, because the low-cost producer can put you out of business." **[M1997-010]**;
   "when a company is selling a product with commodity-like economic characteristics, being the low-cost producer is
   all-important." **[L2000-017]**. The company does not claim the low-cost position in its field. It writes that
   "Persistently low NPI (Nickel-Pig-Iron) prices also supported low production costs for stainless steel and prevented
   stainless steel prices from recovering", that "Import pressure increased in Europe during 2025 despite weak demand, due to
   competitive import prices", and that in South America "we face competition primarily from Asian imports" (Annual Report
   2025). It lists among its principal risks that "A lack of competitiveness in workforce costs might have a material adverse
   effect on Aperam's cost position." Its advantages are named elsewhere: charcoal from its own forests in Brazil ("low-cost
   biomass"), the lowest scope 1 and 2 emissions, and a flexible mill at Timoteo. None of them is shown, in any figure read,
   to put its cost below the Asian producers who set the price. The cost is measured against the rival, "if your costs are
   on parity or less [...] than your other major competitors, that is much more important to you than the absolute level"
   **[M2001-013]**, and "The figures are available." **[M2009-059]**: on the figures available, the deciding part is not the
   low-cost producer.
6. **The brand, and the low bid.** Commodity flat stainless is sold on grade and price; the company itself writes that the
   products are "not completely interchangeable" only because of shape, chemistry and specification. No fact read shows a
   customer paying more for Aperam's coil than an import of the same grade.
7. **Ask the competitors.** Not done; no scuttlebutt was possible in a blind dispatched run.
8. **Widening or narrowing.** Narrowing on the company's own words: Chinese producers "now ranking among the 10 largest
   global flat stainless steel producers", Indonesia's "steady increase in stainless steel capacity", "it is unlikely that
   noticeable overcapacity reductions will take place in the near future" (Annual Report 2025).
9. **What could destroy, modify or reduce it.** The castle's remaining wall is trade policy: the EU steel safeguard (amended
   2025, and "set to expire" in June 2026, with a replacement measure proposed), anti-dumping and anti-circumvention duties
   on cold-rolled stainless, CBAM, and Brazilian import duties (Annual Report 2025, trade measures). A change in any of them
   is the "destroy, or modify, or reduce" of **[M2000-014]**, and none of it is under the company's control. The rows do not
   want "a product that can be shipped in from abroad very easily. Because, sooner or later, that will probably be trouble"
   **[M2007-116]**.

**The competitor row.** The report names its rivals: "Aperam's main competitors in Europe are Outokumpu, Acerinox and Arvedi
Acciai Speciali Terni S.P.A.", and globally Tsingshan, TISCO-BaoWu and Beihai Chengde (Annual Report 2025, competition).
**None of the named rivals files with the SEC** (Outokumpu reports on Nasdaq Helsinki, Acerinox in Madrid, Arvedi is
private, the Chinese producers are not US registrants). **CONVENTION of this run:** where the named rivals file nothing with
the SEC, the comparison is read from the largest named European rival's own primary reports (Outokumpu), over the same
span; rationale: the brief's rule exists to compare the field over the span from the rivals' own filings, and the rivals'
own regulated reports serve that purpose where the SEC route does not exist. Acerinox's reports were not read (a gap).

| Return on capital, % | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Ten-year mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Aperam, operating income / (equity + net debt), pre-tax | 12.0 | 15.0 | 14.1 | 8.3 | 8.8 | 30.5 | 23.1 | 2.3 | 3.3 | 0.4 | 11.8 |
| Outokumpu, ROCE as reported | 2.6* | 11.3* | 7.0 | 0.8 | (1.4) | 17.6 | 22.6 | (2.1) | (1.2) | (3.2) | 5.4 |
| Outokumpu, EBIT margin, % | | | | | | 9.3 | 10.5 | (1.4) | (0.9) | (2.5) | |

Aperam's figure is computed by hand from the year-end statements (2016 and 2017 in US dollars; 2021 includes the EUR 119
million bargain gain, 27.0% without it); its capital is book equity plus borrowings less cash, which carries goodwill of
about EUR 0.4 to 0.5 billion. Outokumpu's ROCE for 2021 to 2025 is from its Annual Report 2025 Group key figures (ROCE
redefined in 2022, 2021 restated), 2018 to 2020 from its own financial statements releases for 2019 and 2020; the two
starred years (2016, 2017) are from an aggregator copy of its earlier financial tables and are **flagged**.

**The field's returns over the last full cycle, judged in words** (the convention gives no figure). Over a cycle that ran
from the trough of 2019 and 2020 through the 2021 and 2022 peak to the trough of 2023 to 2025, the two largest European
producers earned high returns for two years and little or nothing in the other years. Aperam did better than Outokumpu on
average and had no loss year at group level, but its deciding part earned 0.6% of segment sales on average in 2023 to 2025
and its group return on capital was 2% in the last three years. The ten-year mean of about 12% pre-tax on book capital
rests on the two peak years; without 2021 and 2022 it is about 8%. That is an ordinary return for a capital-heavy
producer, earned when the cycle allows and not protected by anything the business controls. "A truly great business must
have an enduring "moat" that protects excellent returns on invested capital." **[L2007-004]**; "you can have only two
competitors and they’re still terrible businesses, they beat each other’s brains out." **[M2013-052]**.

**Who sets the price.** The base price follows imports from producers with lower costs. This is the gas station of the rows:
"whatever he charged for gas was my price. (Laughs) I didn’t have much choice. You don’t like to be in a business like
that." **[M2012-109]**; "he determined our profit, because we looked at his price every day." **[M2023-079]**. And the
high-cost producer's end is named: "In an unregulated commodity business, a company must lower its costs to competitive
levels or face extinction." **[L1994-035]**; this field is not unregulated, which is exactly the point of test 9: its
returns depend on duties the company cannot set.

**OUT or TOO HARD.** The castle's future is not unknowable here; the filings show it. The deciding part is a commodity
producer that is not the low-cost operator in its field, whose price is set by imports, and whose returns over the full
cycle, on its own and its largest named rival's reports, are ordinary. Each of those is on the list of what Q2 rules OUT:
the high-cost producer in a commodity field **[M1997-010]**, **[L1994-035]**; the business whose price a competitor sets
**[M2012-109]**, **[M2023-079]**; the standing castle that protects only ordinary returns **[L2007-004]**, **[M2013-052]**.
It is not the tenuous moat that cannot be valued, "We don’t know how to valuate that" **[M2000-019]**: the moat is judged,
as the rows say it must be, "You have to understand the businesses." **[M1999-108]**. Nor does the price reopen it: "What
you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "marginal businesses purchased at
cheap prices may be attractive as short-term investments, they are the wrong foundation on which to build a large and
enduring enterprise." **[L2014-009]**.

**VERDICT: OUT.** The deciding part, Stainless & Electrical Steel (70.7% of 2021 to 2025 operating income), is a commodity
business that is not the low-cost producer **[M1997-010]**, **[L2000-017]**, takes its price from imports **[M2012-109]**,
and earned ordinary returns over the last full cycle on the filer's and the rival's own reports **[L2007-004]**,
**[M2013-052]**. The file closes here. Q3 to Q12 are NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The template asks for the balance sheets in Step 0 when the file closes before Q4; they were read
and are set out under AFTER THE STOP, without a verdict.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, including the buyback prices set against the bottom of the computed range.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The owner's two reporting figures are computed below under **COMPUTATION, NOT A CLEARANCE**.

### COMPUTATION, NOT A CLEARANCE
*(Q2 closed the file OUT. Every figure in this sub-section is arithmetic beneath a closed stop. It carries no entry language
and decides nothing; operator rule 3.)*

- **Cash input.** Owner cash after every real cost from the Step 0 table, all-equity basis (before interest paid, after the
  company's cash tax) as the central figure, equity-only beside. Taxes are taken as paid in cash (EUR 9 to 118 million a
  year, 2021 to 2025); the deferred tax assets on losses (EUR 429 million recognised, of EUR 2,567 million gross losses) are
  mostly in Luxembourg, and no expiry inside ten years was found in what was read, so the carryforward convention of section
  E was not applied and the shelter is left inside the cash figures (stated, not priced).
- **(a) Cycles.** The window's first year, 2021, is a cyclical peak on the filer's own account (the record year, with the
  bargain gain), and its last, 2025, a trough (operating income of EUR 16 million; the report calls the year "a challenging environment for regional mills"). The base is
  therefore the average over the last full cycle, **trough to trough 2020 to 2025**: all-equity owner cash before purchases
  **EUR 243 million** a year; after the purchases in that cycle (ELG 31, Universal 415), **EUR 169 million**. Growth is
  measured between the cycle average and the end of the previous cycle in euros, 2018 and 2019 (average 176.5), whose start
  in 2016 and 2017 is reported in dollars only: **7.38% a year** over 4.5 years. *(CONVENTION of this run: the previous
  cycle is represented by its two euro years; rationale: the 2018 report that restates 2017 in euros could not be fetched,
  and mixing dollar years into a euro series would add a number the filings do not state.)*
- **(b) Decline.** The literal window shows decline (first half 2021 to 2022 average 361, second half 2024 to 2025 average
  192, or minus 18.9% a year); it is shown beside, as the rule asks, and is not the governing base because both of the
  window's end years are aberrational.
- **(c) Acquisitions.** Net purchases over the window (446) are 35.2% of owner cash before purchases (1,267), under half, so
  the default pair governs: purchases deducted inside the ten years, total growth credited, and after year ten the business
  valued at no growth on owner cash before purchases. Universal closed inside the window and is in the figures. The 2026
  purchase of Magnetec (EUR 1 million) is immaterial.
- **(d) Working capital.** Inside operating cash every year (the 2021 build of inventory, EUR 748 million, and the 2025
  release, 237, are both counted).
- **(e) Maintenance.** No split of maintenance and growth spending was found in the reports read; the all-spending case is
  central. The depreciation variant beside it (operating cash less depreciation and impairment, less leases, plus net
  interest) averages EUR 248 million over 2020 to 2025, against 243 on the capital-spending basis.
- **(f) The cap.** The shown cycle growth carried ten years would require owner cash of EUR 496 million in year ten, 8.2% of
  2025 sales, above the highest share of sales earned in the years read (7.7%, 2021). The growth carried is therefore cut to
  the business's own sales growth over the same span, **6.70% a year** (sales, 2018 to 2019 average 4,459 against 2020 to
  2025 average 5,968, which itself carries nickel prices and two acquisitions). Both the shown rate and the cut are written
  here.
- **The floor, tested first.** At the price the enterprise value is EUR 3,783 million. Each end case discounted at ten
  percent is worth EUR 1,975 million (no growth) and EUR 3,225 million (growth): **no case in the range earns the floor of
  about ten percent at the price**, so Q7, had it been reached, would close OUT whatever the width **[M2003-149]**.
- **The width.** Top over bottom at the sovereign: 131.50 / 67.12 = 1.96, inside three to one.

**(a) VALUE RANGE (reporting figure, Q7's range convention, all-equity basis less net debt of EUR 993 million, 72.468 million
shares, discounted at 3.76%):**
- no-growth case (bottom): **EUR 67.12 a share** (ADR equivalent USD 75.09);
- growth case at 6.70% for ten years, then zero nominal growth (top): **EUR 131.50 a share** (USD 147.12).
- Equity-only beside: EUR 75.99 to 136.69 (USD 85.02 to 152.93).
- Literal window beside: no-growth EUR 69.19; with the literal decline of 18.9% a year as the bottom, EUR 1.62.

**(b) FAIR PRICE (reporting figure, Part VII: each end case valued at ten percent, the two averaged; after the company's own
tax; the floor's "pre-tax" read as before the holder's tax):**
- **all-equity (central): EUR 22.18 a share** (ADR equivalent USD 24.81), from end cases of EUR 13.55 and 30.81;
- **equity-only (beside): EUR 33.53 a share** (USD 37.51), from end cases of EUR 25.44 and 41.63.

Against the price of EUR 38.50 (APEMY USD 42.93): the price is above the central fair price and above both all-equity end
cases valued at ten percent; it sits below the bottom of the range at the sovereign rate. No other price figure is reported.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Debt facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2** (the deciding part, Stainless & Electrical Steel, 70.7% of 2021 to 2025 operating income, is a commodity
producer that is not the low-cost operator, takes its price from imports and earned ordinary returns over the full cycle);
integrity facts recorded, not judged. COMPUTATION beneath the stop, not a clearance: range EUR 67.12 to 131.50 a share at the
sovereign against EUR 38.50; no case earns the floor at the price; fair price EUR 22.18 all-equity (USD 24.81), EUR 33.53
equity-only (USD 37.51).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2.)* **[M1997-127]**

**Bearing on Q3 (capital):**
- Group operating income over equity plus net debt, pre-tax: 12.0% (2016), 15.0%, 14.1%, 8.3%, 8.8%, 30.5%, 23.1%, 2.3%,
  3.3%, 0.4% (2025) (computed from the year-end statements; table at Q2).
- Capital expenditure against depreciation and impairment: 2021 152 / 144; 2022 285 / 186; 2023 250 / 204; 2024 139 / 229;
  2025 137 / 259 (EUR million).
- Universal Stainless: bought for USD 45.00 a share in cash, completed 2025-01-23 (8-K, 0001193125-25-011290); enterprise
  value about USD 535.7 million, 10.6 times last-twelve-months adjusted EBITDA to 2024-06-30 (DEFM14A,
  0001193125-24-267249); cash paid net of cash acquired EUR 415 million (Annual Report 2025 cash flow). Its own record
  (XBRL facts, screening only): sales USD 156 to 286 million and operating income between USD (30) and 16 million a year,
  2014 to 2023; operating cash about USD 57 million against capital spending about USD 111 million over the decade.
  Goodwill and intangibles rose from EUR 427 million to 505 million in 2025.
- ELG (completed 2021-12-27, Annual Report 2025): cash EUR 31 million net, with a preliminary bargain purchase gain of EUR
  119 million in 2021 operating income; the Recycling & Renewables segment it anchors lost EUR 2 million in 2024 and 38
  million in 2025.

**Bearing on Q4 (the numbers): the balance sheets, ten years, read before the income account** (EUR million; 2016 and
2017 in USD million):

| Dec 31 | 2016$ | 2017$ | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Jun 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total equity | 2,485 | 3,050 | 2,519 | 2,418 | 2,204 | 2,953 | 3,392 | 3,450 | 3,366 | 3,210 | 3,287 |
| Goodwill and intangibles | 565 | 610 | 490 | 479 | 429 | 439 | 451 | 452 | 427 | 505 | 514 |
| Cash | 325 | 367 | 199 | 375 | 358 | 524 | 457 | 443 | 216 | 325 | 334 |
| Trade receivables | 238 | 324 | 274 | 228 | 229 | 556 | 454 | 429 | 384 | 435 | n/a |
| Inventories | 1,226 | 1,475 | 1,410 | 1,227 | 1,101 | 2,332 | 2,592 | 2,281 | 2,159 | 2,028 | n/a |
| Sales (year) | 4,265 | 5,051 | 4,677 | 4,240 | 3,624 | 5,102 | 8,156 | 6,592 | 6,255 | 6,080 | 3,264 (H1) |
| Borrowings incl. leases | 479 | 292 | 247 | 450 | 425 | 990 | 925 | 934 | 760 | 1,303 | 1,327 |
| Retained earnings | 1,282 | 1,549 | 1,402 | 1,389 | 1,424 | 2,253 | 2,742 | 2,821 | 2,914 | 2,783 | n/a |
| Deferred tax assets | 285 | 237 | 160 | 128 | 94 | 135 | 101 | 213 | 351 | 408 | 402 |

What moved and why, as the figures say it **[M2025-032]**: inventory roughly doubled with ELG at the end of 2021 and sits
at about a third of sales (2,028 against 6,080 in 2025); borrowings rose to EUR 1.3 billion with Universal; equity in euros
is about where it was in 2018 plus the 2021 to 2022 profits, less dividends of about EUR 140 to 151 million a year, buybacks
and translation losses on the Brazilian real (other comprehensive loss of EUR 815 million at 2025); deferred tax assets rose
from 94 (2020) to 408 (2025) while pre-tax income fell, and the 2023 to 2025 income tax benefits (87, 154, 85) carried net
income above pre-tax income in each year.
- EBITDA and "Adjusted EBITDA" are the headline figures of the results releases (Q2 2026: "Adjusted EBITDA of EUR 130
  million"); the GAAP operating income (102) is in the table beside. The releases give forward statements of the kind the
  rows name, "Q3 2026 adjusted EBITDA is expected to be lower compared to Q2 2026" and "Net financial debt expected to
  remain flat at Q3 2026". Recorded for Q4 and Q5; the rows on them are **[M1998-086]**, **[L2016-006]**, **[L2019-006]**;
  not weighed.
- Restatements found: 2024 capital expenditure 152 in the 2024 report and 139 in the 2025 report (bearer plants moved); 2022
  comparatives reclassified in the 2023 report (note 2). Neither changes a total in substance.

**Bearing on Q5 (the people): integrity facts recorded, not judged:**
- A controlling shareholder: the Mittal family trust holds 40.33% of issued shares (40.73% of votes) at 2026-09-30.
- In the 2022 buybacks the family sold into the programme pro rata to keep its voting share: of 3,499,999 shares bought in
  August and September 2022 for EUR 94 million, 1,433,599 (EUR 38.57 million) were bought off-market from the Mittal family
  (company share-buyback page).
- The headline figure in results releases is Adjusted EBITDA, with guidance on the next quarter's adjusted EBITDA and net
  debt (Q2 2026 release); the self-help programme's "gains" are reported each quarter (EUR 100 million in 2025).
- Brazilian tax assessments against Aperam South America (note 28): corporate income tax and social contribution for 2021
  and 2022, R$1.2 billion (EUR 202 million), first-level court decision in the company's favour on the interest-on-equity
  part, appealed by the government; COFINS R$191.3 million; ICMS assessments of R$167.7 million and R$121.6 million (2021 to
  2024) and smaller ones. A Central Bank fine of R$70.5 million (EUR 11.9 million) over exchange operations of 2004, lost at
  the second judicial instance in 2025 and appealed to the superior courts. Provisions for tax claims about EUR 8 million
  and for other litigation about EUR 29 million.
- The 2024 and 2025 tax benefits came "primarily in Luxembourg, resulting from the measurement of uncertain tax position
  following the issuance of the tax assessments of certain prior years by the tax authorities" (note 8).

**Bearing on Q6 (the money and the owners):**
- Dividends: a base dividend of EUR 2.00 a share, maintained for 2026 (Annual Report 2025); cash paid USD 97 million in 2016, rising to about EUR 145 million a year
  from 2022, paid through the 2023 to 2025 trough when operating income was 89, 129 and 16.
- Buybacks (cash, from the cash flow statements; average prices derived from the change in treasury shares and the
  programme reports, approximate): 2017 USD 98 million; 2018 EUR 70 million (about EUR 40 a share); 2019 EUR 93 million
  (about EUR 25); 2021 EUR 105 million (about EUR 53); 2022 EUR 194 million, of which the August to September programme
  paid about EUR 26.90 a share (EUR 94 million for 3,499,999 shares). The programmes name a maximum per share tied to recent
  market prices ("shall not exceed 110% of the average of the final listing prices of the 30 trading days"), not a price
  related to value. **Q6's line from Q7 (COMPUTATION, NOT A CLEARANCE):** the bottom of the computed range at the sovereign
  is EUR 67.12 a share, and every average price paid listed above sits below it; at the fair price of EUR 22.18
  (all-equity), all of them sit above it. Recorded, not weighed.
- Stock pay: share-based payments recognised EUR 4 to 5 million a year (2024, 2025).
- No acquisition paid in shares was found; Universal and ELG were paid in cash, so Q6's STOP on an all-stock deal in
  undervalued stock does not arise on the facts read **[L2009-019]**.

**Bearing on Q9 (debt):**
- Net financial debt EUR 993 million at 2026-06-30 (EUR 978 million at 2025-12-31), about 3.6 times 2025 EBITDA of EUR 275
  million and 0.30 times equity. Covenants: maximum consolidated total debt of 90% of consolidated tangible net worth, in the
  revolving facilities and the Flemish-guaranteed loan, complied with. Undrawn: EUR 500 million revolving facility to
  February 2029, EUR 200 million to September 2027, EUR 150 million guaranteed loan; commercial paper programme of EUR 250
  million (51 drawn at 2025-12-31). The EUR 500 million bridge for Universal was repaid in October 2025.
- Employee benefit obligations EUR 135 million (2025); environmental reserves EUR 26 million.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch (done, and committed before the first fetch); written question by question;
      committed after each. **Not kept in full:** Step 0, Q1, Q2 and the computation were written in one pass after the
      evidence was gathered and committed together, because the fetch problems (aperam.com refusing connections from mid-run,
      recovery through archive copies) took most of the session. The research notes were committed with the template copy;
      the run file's sections were not committed one by one. Recorded as a write-early violation.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is declared
      under contamination at the top and was not used.
- [x] Every v5 id cited resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (check
      script `_research 2026-10-13 APEMY/scripts/check_citations.py`, output `citation_check.txt`); every filing fact carries
      its document and date in place of an accession (none exists for this issuer), and the SEC facts carry accessions.
- [x] The order was kept; Q2, the first STOP that failed, closed the run; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE and carry no entry language.
- [x] Owner cash after every real cost from operating cash less all capital spending, biological assets and lease principal,
      never a net-income proxy (operator rule 5); the sovereign from the ECB, dated; aggregator quotes flagged (the price,
      the APEMY quote, two Outokumpu years).
- [x] Contrary evidence written down as found (Foundations, six items); facts for later questions under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] No point-in-time anchor; no row-date rule applies.
- [x] `tools/run.py` produced no arithmetic for this issuer; nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before the final commit (recorded in the reply).
- *Honest limits:* the Half-Year Report 2026 was not obtained (the Q2 release's condensed figures were used); the 2018 annual
  report was not obtained, so 2016 and 2017 stand in dollars; the annual-report PDFs are archive byte copies of the
  company's own files, not fetched from aperam.com directly; Acerinox was not read; no scuttlebutt.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. First, the brief's competitor rule (rivals "that file with the SEC") has no answer when the report names its
rivals and none of them files with the SEC; the framework's commodity paragraph asks for "its own and its operators'
filings" without saying which filings count, so I read the largest named rival's own regulated reports and confessed it as
a CONVENTION of the run. Second, Q7's cycle specific (a) assumes the previous cycle is in the earnings currency; here the
previous cycle's first years are reported in US dollars, and the rule does not say whether to convert, drop or substitute,
so I used the two euro years and confessed it. Third, the cap in (f) compares year-ten owner cash with "the highest share of
sales the business has earned in the filings read", but for a producer whose sales swing with the nickel price that share
moves with the commodity, not with the business; the cut it forced (7.38% to 6.70%) is small here, but the test is measuring
the alloy surcharge as much as the business. A smaller note: Q2's list rules OUT "the high-cost producer in a commodity
field", but the run must infer high cost from the company's own words and its rivals' returns, since no filing read states a
cost per tonne against a rival's; the framework's commodity paragraph sends that case to TOO HARD (WORK) only "where the
cost position cannot be read because the operators' reports were not read", which leaves open whether a cost position read
from words and returns, rather than from costs, is "read". I judged it read, because the price-setter test and the
ordinary-returns test close the file on their own evidence.
