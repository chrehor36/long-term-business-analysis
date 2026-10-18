# Company Run: WANG & LEE GROUP, Inc. (OTC: WLGSF; formerly Nasdaq: WLGS), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run under
the canonical brief, with the two departures the brief names (lines of evidence derived from the 20-F's Items 3.D, 4 and 5;
rivals taken from the filer's own naming, or else confessed). Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (3fef48cc): `PORTFOLIO.md` read for this one ticker; the operator does not hold WLGSF (no line names WLGSF, WLGS or Wang & Lee).*

**Contamination, declared:** to check that no run file of this date existed I listed `Test Runs/`; the listing showed the file
names (not contents) of other runs dated 2026-10-17, among them several construction and engineering names. The session's
git context showed the subjects of recent commits about another company. Nothing of them was opened or used. Two of the
companies whose own SEC filings I later used as comparables at Q2 (SU Group, SUGP) appear by name in that listing; I chose the
comparables by a stated EDGAR search (Q2, CONVENTION of this run) and read only their filings, never any run file about them.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Status of the filer.** Nasdaq suspended the shares on 2025-08-26 (6-K of 2025-08-26, accession 0001641172-25-025474) and
  filed Form 25-NSE on 2025-11-21 (accession 0001354457-25-001166). EDGAR's submissions file for CIK 0001899658, read
  2026-10-17, lists that Form 25 as the last filing: **no filing by the company after August 2025, no 20-F for FY2025, no
  interim report for 2025.** The company's website (www.wangnlee.com.hk, read 2026-10-17) carries two news releases, both of
  April 2023, and links to EDGAR; no later annual or interim report. **The latest audited year is FY2024.** The latest interim
  statements are those of the six months to 2024-06-30 (6-K of 2024-12-30, accession 0001493152-24-052478), unaudited and,
  in the filing's words, "not been reviewed on behalf of the shareholders by the independent external auditors".
- **Price:** $0.0001 (close 2026-10-16, Yahoo chart feed through `tools/sources.py`; **aggregator, flagged** per operator rule
  5). It trades: 98,200 shares that day, and volume on most days since August 2026. The same feed shows the stock near $0.004
  to $0.013 (on its own post-combination basis) from September 2025 to July 2026 and at $0.0001 since 2026-07-28. Quote only;
  nothing in this run is taken from an aggregator's financial data.
- **Shares by class** (one class, ordinary, no par): 17,357,924 at 2024-12-31 (FY2024 20-F cover, accession
  0001641172-25-010670; matches the balance sheet and Note 11, issued and outstanding, no treasury shares). The 6-K of
  2025-08-21 (accession 0001641172-25-025052) states 174,679,566 shares before a 250-to-1 combination, "approximately
  698,719" after it, trading on the combined basis from 2025-09-02. **The count after that date is not on file.** The $8,000,000
  senior convertible notes of 2025-06-09 (6-K 0001641172-25-014262; conversion at 85% of the lowest daily VWAP of the prior ten
  days) and the Class B reset warrants of the March 2025 offering (424B5 0001641172-25-000251) could each have added shares
  after the last filing; whether they did is not on file. `python Screens/cover_shares.py WLGSF` returned "NOT AN SEC
  REGISTRANT in the live ticker file" (the delisted ticker has left the SEC ticker file).
- **Market cap:** not computable from the filings. On the last filed count (about 698,719) the quote gives about $70; the
  quote and the trading volume are hard to square with that count, which suggests (does not show) that the count is now far
  larger. Recorded as a gap, not estimated.
- **Sovereign for the earnings currency (HKD):** **not obtained from the issuing authority.** The earnings are in Hong Kong
  dollars (20-F, Item 3: "Our revenues and expenses will be denominated predominantly in Hong Kong dollars"). The issuer of
  HKD government debt is the HKSAR Government, its bond programme administered by the Hong Kong Monetary Authority; the
  longest institutional benchmark is the 20-year HKGB. Every request to the HKMA API endpoint for it
  (`api.hkma.gov.hk/.../gov-bond/instit-bond-price-yield-daily?segment=Benchmark`) on 2026-10-17 returned HTTP 405 from the
  HKMA's web firewall, by curl, by Python and by the fetch tool. **CONVENTION of this run:** the COMPUTATION below shows the
  US Treasury 30-year par yield, **5.43% (2026-10-16, US Treasury daily par yield curve, `python tools/sources.py`)**, as a
  stand-in, because the filing itself says the Hong Kong dollar "has been pegged since 1983" to the US dollar (20-F, Item 3);
  rationale: the stand-in decides nothing here, since owner cash is negative in every year and no discount rate makes the
  value positive. A fair-price alert built on it should be re-run on the HKGB yield when the HKMA endpoint answers.
- **Filings read** (operator rule 4): the 20-F for FY2024 (filed 2025-05-15, accession 0001641172-25-010670), Items 3.D, 4,
  5, 6, 7, 10 (Note 11, Equity), 16F, and the audited statements; the 20-F for FY2023 (2024-05-14, 0001493152-24-019005),
  Items 3.D, 4 and 5; the 20-F for FY2022 (2023-05-15, 0001493152-23-017465) and its 20-F/A (2023-12-08,
  0001493152-23-044141), balance sheets; the F-1/A of 2023-03-28 (0001493152-23-009252), FY2020 and FY2021 statements and its
  industry section; every 6-K from October 2024 to August 2025 (list in the research folder), the two 424B5s of 2025
  (0001641172-25-000251, 0001641172-25-014260), the NT 20-F of 2025-04-29, and the Form 25. No proxy statement exists for a
  foreign private issuer; the 2024 AGM notice (6-K of 2024-10-10, 0001493152-24-040687) and its results (6-K of 2024-10-29,
  0001493152-24-042796) were read in its place. **One figure cross-checked against the filed statement:** FY2024 contract
  revenue $3,951,649 in the audited statement of operations equals the SEC XBRL fact
  RevenueFromContractWithCustomerExcludingAssessedTax for 2024 (accession 0001641172-25-010670) and the MD&A table.
- **`python tools/run.py WLGSF`**: refused ("not an SEC filer", the ticker having left the SEC ticker file). Run again through
  a wrapper in the research folder that supplies the CIK (`scripts/run_cik.py`): "no overlapping OCF/D&A/capex annual facts.
  UNRESEARCHED." The tool produced no line. Every figure below is read from the filed statements by hand
  (`scripts/tables.py`, `scripts/compute.py`, output in `computation_output.txt`).
- **The filed series (US dollars, as filed; FY2020 and FY2021 from the F-1/A, FY2022 to FY2024 from the FY2024 20-F):**

| FY | Revenue | Gross profit (margin) | Operating result | Net result | Op. cash flow | Capex | Listing fee (in G&A) |
|---|---|---|---|---|---|---|---|
| 2020 | 4,074,258 | 735,165 (18.0%) | 142,626 | 278,018 | (74,380) | 2,926 | nil |
| 2021 | 4,135,059 | 859,760 (20.8%) | (360,859) | (354,743) | (482,801) | nil | 354,743 |
| 2022 | 4,169,931 | 785,704 (18.8%) | (641,452) | (596,881) | (352,764) | nil | 328,699 |
| 2023 | 6,825,879 | 2,440,600 (35.8%) | (771,090) | (648,854) | (3,814,384) | nil | 1,241,199 |
| 2024 | 3,951,649 | 412,171 (10.4%) | (2,548,875) | (2,543,959) | (1,569,940) | nil | 190,506 |

  Owner cash (operating cash flow less capital spending; no investing outflow other than the 2020 equipment purchase; no tax
  paid after 2020; stock pay: 2,264,077 shares awarded in December 2024, unvested at year end, no expense booked in 2024, Note
  11): **(77,306), (482,801), (352,764), (3,814,384), (1,569,940); five-year average (1,259,439).** Negative in every year.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own it "if the market closed for five years" **[M1997-109]**,
or delisted and reopened long after **[M1996-067]**. For this name the test is not hypothetical: the stock has been delisted, the
company has stopped reporting, and an owner today would hold a business whose accounts he cannot read after December 2024. The
market serves and does not instruct **[M2006-077]**: a price of $0.0001 says nothing about value, and the run does not read it
as a signal either way. The margin of safety is an attitude here **[M1996-084]**; it enters only at Q7. Who is paid to tell
you: the 2025 press releases (a "US$71 million contract" for "dual-purpose marble quarrying and solar crypto farm operations"
in Queensland, 6-K of 2025-03-17, accession 0001493152-25-010621) are the company speaking about itself while it sold stock and
convertible notes; they are read as claims, not facts. The analyst's habit: write the contrary evidence down at once
**[M1997-127]**. **Contrary evidence, written down as found [M1997-127]:** (1) three consecutive years of operating losses and
five of negative owner cash before any purchase question is asked; (2) the shares rose from 17,357,924 to 174,679,566 between
2024-12-31 and July 2025, then were combined 250 to 1, then the company stopped filing; (3) Nasdaq delisted the shares partly on
"public interest concerns primarily in relation to the Company’s June 9, 2025 issuance of convertible notes" (6-K of
2025-06-30, accession 0001641172-25-017061); (4) the FY2024 audited subsequent-events note is dated "May [ ], 2025", the blank
unfilled in the filed annual report. The evidence for the business, also written down: a 44-year operating history (founded
1981, Item 4.A), the four registrations it holds (Item 4.B), and a cash balance of $4.30M at 2024-12-31.

## THE STANDING RULE
Nothing about this name requires the buyer to borrow, give an option, or take an exposure that can call for cash
**[M2012-081]**; a buyer paying cash for a small stake does not put himself at risk of ruin. But the standing rule's second form,
"Never risk permanent loss of capital." **[L2023-005]**, bears on a holding whose issuer has stopped reporting and whose share
count is unknown: a buyer could not tell how much of the business a share represents. Recorded for the buyer's sizing; not a
gate on the business.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**Lines of evidence chosen (departure from the canonical brief, as the brief directs), derived from the FY2024 20-F:** from
Item 4, the service lines, the tendering process, customer and supplier concentration, the registrations, and the 2025
acquisition; from Item 3.D, the competition risk ("We may lose business to competitors that underbid us", FY2023 20-F), the
private-construction downturn, labour cost, and the listing and dilution risks; from Item 5, gross margin by service line, the
cost overrun of 2024, the strategic shift to "site project management" and "energized panel" work, and liquidity. Then the
2025 6-Ks for what happened after the last annual report.

- **What the business is, on the filings.** Through Wang & Lee Contracting Limited, a Hong Kong electrical and mechanical
  contractor: low-voltage electrical systems, ventilation and air-conditioning, fire services, plumbing and drainage, and
  fitting-out, sold project by project. "We usually receive invitations from customers to submit tenders for potential
  projects"; 138 submissions in 2024 at a success rate of about 36% (151 at 36% in 2023, 145 at 40% in 2022); "The vast
  majority of its projects are fixed unit price contracts"; as prime contractor "it utilizes subcontractors to perform
  approximately 69% of the total project"; five customers were 88%, 98% and 89% of revenue in 2024, 2023 and 2022, and "we do
  not have any long-term contracts with any one client" (FY2024 20-F, Item 4.B, accession 0001641172-25-010670). All of FY2024
  revenue came from E&M engineering services (Item 4.B).
- **The key variables and whether they are foreseeable** **[M1998-044]**: the volume of Hong Kong private fit-out and building
  work put out to tender, the share of tenders won, and the margin at which they are won against "a large amount of E&M
  service providers" (Item 3.D). These are the economics of a trade, not of a technology, and they can be read from the
  filings: the statements show what the business earns on its tenders over five years, and the industry section of the
  F-1/A describes the field as "relatively mature and fragmented" with 185 registered ventilation specialist contractors at
  2022-12-31 (F-1/A, accession 0001493152-23-009252). The question test 3 puts, whether the past statements tell me the future
  ones **[M2008-033]**, is answered yes for this trade: the five years on file show what a small Hong Kong E&M bidder earns.
  Understanding here is "a reasonable fix on about what the earning power and competitive position will look like in five or
  10 years" **[M2012-065]**, and a fix that the economics will be those of an undifferentiated tender contractor is a fix; it
  is a finding for Q2, not a reason the business cannot be understood **[M2011-014]**.
- **What cannot be foreseen, and why it does not decide here.** The 20-F says the company is moving into "site project
  management", footstep "energized panels", lithium battery development, waste treatment and, by its press release, a solar
  "crypto farm" and marble quarry in Australia (6-K of 2025-03-17, 0001493152-25-010621); it bought Solar (HK) Limited for
  HK$15,000,000 (closed 2025-03-31; 6-K of 2025-04-01, 0001641172-25-002065; paid in cash under the amendment of 2025-08-08,
  6-K 0001641172-25-022700). The new activities were "only 3% of total revenue" in FY2024 (Item 5) and Solar HK has no filed
  record. By Q1's paragraph on a business of parts (a part decides at more than half of five-year operating profit, or else
  the largest; CONVENTION of the framework, section B of the gaps case), the deciding part is the E&M contracting business,
  which is all the filed revenue; the ventures do not decide. Whether the company will still be a contractor in ten years is
  a real doubt **[M2002-092]**, and it is recorded: the company has stopped filing, so its present form cannot be read. But
  the question the file can answer, what the business on record is and what it earns, is answerable from documents "in black
  and white" **[M2005-015]**, and the run is decided "off the figures" **[M2008-069]**. The doubt is carried to Q2 and to the
  facts after the stop, not used to avoid the castle question the filings answer.
- **VERDICT: IN** (the E&M contracting business, the deciding part on the filings), on **[M2012-065]**, **[M1998-044]**,
  **[M2008-033]**, **[M2011-014]**; the doubt about what the company has become since 2025 is written down **[M1997-127]** and
  bears on later questions. The reading that would have closed the file here instead, TOO HARD on the doubt rule
  **[M2002-092]** because the company stopped reporting, is named under "What in the framework was wrong or unclear".

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. The filings answer it from the attacker's side.

**The castle tests, each with its filing fact.**
- **The attacker with money** **[M2011-015]**. The field is "relatively mature and fragmented", 185 registered ventilation
  specialist contractors at 2022-12-31 alone (F-1/A, 0001493152-23-009252), and the 20-F says "We face significant competition
  in the E&M market due to a large amount of E&M service providers" (FY2024 20-F, Item 3.D). Entry needs registrations and
  registered workers, which the company holds (Item 4.B), but the company's own claim is that it is among "less than 1% of
  E&M engineering companies that hold all four licenses" (F-1/A), a breadth claim, not a barrier the filings show earning
  anything: the business that holds all four licences lost money in four of the five years. A competitor with money would not
  need to displace anything; it would bid. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
- **Pricing power and the agony before a rise** **[M2005-020]**. The company does not set prices; it answers tenders, at "fixed
  unit price contracts" (Item 4.B), and says "some market participants may adopt more aggressive pricing approaches, leading to
  downward market pricing pressure" (FY2023 20-F, Item 3.D, accession 0001493152-24-019005). Gross margin ran 18.0%, 20.8%,
  18.8%, 35.8%, 10.4% from 2020 to 2024: no level that holds, and the 2023 peak came from one fitting-out line at 69% (one year)
  while the 2024 trough came from "a single major project" whose "complex structure necessitated additional labor, resulting in
  cost overruns" (Item 5). A business that cannot hold its margin through one project has no pricing power to test.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. The customer runs a tender and the company wins
  about a third of them (36%, 36%, 40%; Item 4.B). Its own risk factor is headed "We may lose business to competitors that
  underbid us" (FY2023 20-F; F-1/A). Five customers gave 88% to 98% of revenue with no long-term contract with any (Item 4.B):
  the customer changes every few years and chooses each time on the bid. This is the commodity mark the rows name: "most
  insureds don't care from whom they buy" **[L2004-003]**.
- **Unit volume and share of mind; the brand.** No filed measure of either. Revenue was $4.07M in 2020 and $3.95M in 2024 (a
  compound change of -0.8% a year over the window), with $6.83M in 2023 from a contract the 20-F calls "one of our largest
  construction projects" (FY2023 20-F, Item 5). Nothing in the filings says customers ask for the company by name.
- **The low-cost position.** The filings claim none: the 20-F's competitive strengths are breadth of service, history, the
  management team, quality systems and long relationships (Item 4.B), and its stated cost advantage is the preferred pricing of
  an authorised air-conditioning dealership held under "one-year non-exclusive dealership agreements" (Item 4.B). In a field
  where "the guy with the lower cost comes in and kills you" **[M2001-013]**, a contractor that subcontracts about 69% of its
  prime work and lost money on labour overruns has shown no low-cost position **[M1997-010]**.
- **Ask the competitors.** The 20-F names no competitor; no rival's view is on the public record I read.
- **Widening or narrowing** **[M1999-108]**. Narrowing on the filings: operating results moved from a profit of $142,626 in 2020
  to a loss of $2,548,875 in 2024; the 20-F says the 2024 "construction industry experienced a downturn", with "fewer available
  bids in the market", and that the company is "transitioning" to site project management and to sustainable-energy work
  "Recognizing the declining demand in traditional construction" (Item 5). The company itself describes its core field as
  declining and is moving out of it.
- **What could destroy it** **[M2000-014]**. The company's own funding: the shares that paid for the business's losses were
  delisted, and the filings end in August 2025.

**The competitor row, from the rivals' own filings.** The 20-F names no rival. **CONVENTION of this run:** the comparables are
the Hong Kong special-trade contractors filing 20-Fs that an EDGAR full-text search for "electrical and mechanical" "Hong Kong"
contractor (forms 20-F, 2023-01-01 to 2026-10-17) returned under SIC 1700 with a Hong Kong business address, Masonglory Ltd and
Ming Shing Group Holdings Ltd, plus the only other filer the search "registered electrical contractor" returned, SU Group
Holdings Ltd; rationale: the brief forbids hand-picked rivals and the filer names none, so a stated search fixes the set before
any figure is read. None is an E&M installer of the same mix: Masonglory and Ming Shing are wet-trades subcontractors (plastering,
tiling), SU Group installs security systems and provides guarding; all three win Hong Kong work by tender (Masonglory's and Ming Shing's 20-Fs: "tender by
customers"; SU Group's 20-F lists "tendering" among its forward-looking risks). Named rivals that do not file: none named. Figures from each filer's SEC XBRL facts, by accession.

| Company (fiscal year end) | Accessions | Gross margin by year | Operating margin by year | Operating result over the span / revenue over the span |
|---|---|---|---|---|
| Wang & Lee (Dec), FY2020 to FY2024 | 0001493152-23-009252; 0001493152-23-017465; 0001493152-24-019005; 0001641172-25-010670 | 18.0, 20.8, 18.8, 35.8, 10.4% | 3.5, -8.7, -15.4, -11.3, -64.5% (before listing fees: 3.5, -0.1, -7.5, 6.9, -59.7%) | -18.0% (-8.9% before listing fees) |
| Masonglory (Mar), FY2023 to FY2026 | 0001213900-25-069393; 0001213900-26-083085 | 4.7, 8.2, 9.3, 4.4% | 2.9, 7.4, 6.4, -33.2% | -6.0% |
| Ming Shing (Mar), FY2022 to FY2026 | 0001493152-24-033838; 0001641172-25-024398; 0001493152-26-038558 | 18.3, 16.0, 18.5, -3.9, -18.4% | 14.7, 12.1, 11.8, -15.8, -37.4% | -2.5% |
| SU Group (Sep), FY2021 to FY2025 (HKD) | 0001213900-24-008504; 0001213900-25-007523; 0001753926-26-000125 | 30.6, 28.7, 29.3, 26.1, 16.0% | 6.9, 5.0, 6.6, 6.0, -10.4% | 2.1% |

**The parts table.** The filer reports one business (E&M engineering services, "not disclosed as a separate segment" for the
new activities, Item 5); its service lines (low-voltage electrical, ventilation and air-conditioning, fitting-out, other E&M)
report revenue and gross profit only. No part reports operating profit, and every line is won by the same tender; the business
is read whole. Gross profit by line moves from year to year without a stable leader (fitting-out was 143% of 2024 gross profit
because low-voltage electrical was negative, Item 5).

**The field's returns over the last full cycle, judged in words.** The span read covers a cycle of Hong Kong building work: the
filer's and the rivals' years from 2020-21 through the 2024-25 downturn the 20-F describes. In the good years the field earned
thin margins on revenue (low single figures for the wet-trades and security contractors, low teens at best for Ming Shing), and
in the downturn every one of the four fell into operating losses, three of them in their latest year. Over the whole span
two of the three rivals lost money in aggregate and the third earned about 2% of revenue; Wang & Lee lost 18% of revenue (9%
before its listing fees). These are not durable players protecting ordinary returns; they are bidders in a field where the
rows' description holds: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**, and "there
are some industries that are just never going to have barriers to entry" **[M2012-106]**. "Ordinary" is judged in words, as
the convention requires **[M1999-108]**: the field's returns over the span are below ordinary, and the filer's are the worst of
the four.

**What the castle is.** None that the filings show. The company bids for work "the low bid" decides **[M2017-009]**, holds no cost
advantage **[M1997-010]**, has a price set by whoever bids lowest **[M2012-109]**, and has lost money in four of five years in
a field whose members all lost money in the latest year. A castle "earning high returns" is what attracts assault
**[L2007-004]**; here there are no high returns to protect and nothing protecting the ordinary ones. This is not a castle whose
future cannot be judged (TOO HARD, **[M2000-019]**); it is a castle shown open on the evidence of the filer's and the rivals'
own filings, the case **[M2011-015]** sends to OUT. A low price does not reopen it: "What you can’t do is turn any investment
into a good deal by paying little" **[M2019-015]**, and "If you really think a business is declining, most of the time you
should avoid it." **[M2012-062]** (the 20-F's own words for its field: "declining demand in traditional construction").

- **VERDICT: OUT.** The castle is open on the evidence: tendered fixed-price work won on the bid **[M2017-009]**, **[L2004-003]**,
  no low-cost position **[M1997-010]**, **[M2001-013]**, a field without barriers **[M2012-106]** whose members earned below
  ordinary returns over the span read **[M2013-052]**, and a filer whose own margins narrowed to a 64.5% operating loss in 2024
  **[M1999-108]**. Closed under the three boxes **[M2006-013]**; nothing after this is a clearance.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The template asks for the balance sheets in Step 0 when the file closes before Q4; they are read under AFTER THE
STOP, Q4, as facts, not weighed.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts were found and are recorded, not judged, under AFTER THE STOP; the box line carries the flag.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed below under the heading COMPUTATION, NOT A
CLEARANCE (operator rule 3; Part VII, The owner's price).

### COMPUTATION, NOT A CLEARANCE
*No entry language. The file is closed OUT at Q2; nothing here reopens it.*
- **Cash input.** Owner cash after every real cost, operating cash flow less capital spending, as filed, FY2020 to FY2024:
  (77,306), (482,801), (352,764), (3,814,384), (1,569,940); five-year average **(1,259,439)** (`scripts/compute.py`). No income
  tax was paid after 2020 (losses), so the company's own tax is nil in every case; the carryforward question of Q7's "Whose
  tax" does not arise while the cash is negative. Before interest (the all-equity basis): average **(1,202,426)** (interest
  paid added back: 49,229; 13,312; 35,377; 59,976; 127,173).
- **Growth.** The series is negative in all five years, so a compound rate between end years is meaningless and so is the
  first-half against second-half rate; by specific (b) the range is **the no-growth case alone, said so**.
- **The six specifics, run.** (a) Cycles: 2023 (IPO year, one large contract, a $3.07M receivables build) and 2024 (the cost
  overrun and the downturn the filer describes) are aberrational on the filer's own description; no full cycle on file has
  positive owner cash, so no cycle base changes the sign. Shown beside: the variant before working capital (net result plus
  depreciation) averages (761,308); the same with the listing fees added back averages (338,279); both negative. The literal
  window is the central figure. (b) Decline: carried; the range is the no-growth case alone. (c) Acquisitions: none paid for
  inside the window. Solar (HK) Limited closed after the window (2025-03-31): it has no filed record, so it is credited at
  nothing, and its price, HK$15,000,000 ($1,935,484 at the filing's rate), stated in the FY2024 20-F's Note 18 as a subsequent
  event, is added to net debt (the 6-K of 2025-08-08 later replaced the note with cash; either way the money leaves the
  company). (d) Working capital: counted (it is inside operating cash flow). (e) Maintenance: capital spending was nil in four
  of the five years; no maintenance guess changes the sign. (f) The cap: not engaged.
- **Net debt at 2024-12-31** (FY2024 balance sheet, accession 0001641172-25-010670): bank loans $1,890,316 + $447,086, finance
  leases $11,125 + $24,489, less cash $4,304,514 = net cash $1,931,498; the director's advances shown as "Other payables,
  related parties" $1,366,738, which the cash-flow statement carries in financing, are counted as borrowings (net cash
  $564,760); the Solar HK consideration added: **net debt $1,370,724.** Operating leases left out, as the convention says
  ($89,770). The $8M convertible notes of June 2025 (net proceeds about $3.57M) are a later 6-K's event, not stated in the 20-F,
  and are left out of the central figure by the convention; beside it, they would raise net debt by up to their principal.
- **Floor test first.** No case in the range earns the floor at any positive price: every case is a negative value. By the floor
  convention the computation would close OUT whatever the width.
- **VALUE RANGE (reporting figure):** the no-growth case alone. At the stand-in rate 5.43% (CONVENTION of this run, Step 0):
  whole-business value $(22,144,118) on the all-equity basis, less net debt $1,370,724 = **$(23,514,842)**; per share
  **$(1.35)** on the last audited count (17,357,924) or **$(33.65)** on the post-combination count of the 6-K of 2025-08-21
  (about 698,719); the true count today is unknown. Equity-only beside it: $(23,194,088), $(1.34) or $(33.20) a share.
  **Against a price of $0.0001, the price sits above the top of the range.**
- **FAIR PRICE (reporting figure, Part VII):** each end case valued at ten percent and averaged (one case here): all-equity
  $(12,024,256) less net debt $1,370,724 = $(13,394,980), **$(0.77) a share** on 17,357,924 shares or $(19.17) on about 698,719;
  equity-only beside it $(12,594,390), $(0.73) or $(18.03). **No positive fair price exists**: the central case does not earn
  the floor at any price above zero. Tax treatment: the company's own tax, nil on these losses.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2**: a Hong Kong E&M tender contractor with no castle shown on the evidence (work won on the bid at fixed unit prices,
no low-cost position, a field of filing rivals earning below ordinary returns over the span, the filer worst of four);
**integrity facts recorded, not judged.** COMPUTATION only: value range $(23.5)M for the whole equity (the no-growth case alone;
$(1.35) a share on the last audited count, $(33.65) on the post-combination count), no positive fair price, against $0.0001.
Q11 belongs to the holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).*

**Q3 (capital).** Capital spending nil in 2021 to 2024 and $2,926 in 2020; plant and equipment $50,835 at 2024-12-31. The capital
the business needs is working capital: receivables, contract assets and retention receivables together were $2.07M, $1.84M,
$2.33M, $5.99M and $3.94M at the year ends 2020 to 2024, against revenue of $4.07M, $4.14M, $4.17M, $6.83M and $3.95M (about
51%, 45%, 56%, 88% and 100% of the year's revenue). Operating cash flow was negative in every year. The IPO raised $8.0M gross
in April 2023 (Note 11).

**Q4 (accounts; the balance sheets, every year on file, FY2020 to FY2024).** Equity $(765,744), $(1,116,434), $(1,713,445),
$6,008,925, $3,494,999: negative until the IPO, then cut by 42% in one year by the 2024 loss. Accumulated deficit from
$(1,270,198) to $(5,414,635). Cash $8,219, $537,738, $609,616, $5,210,193, $4,304,514. Bank borrowings (with the 2020 line of
credit) $358,243, $1,011,398, $1,108,288, $1,701,580, $2,337,402; related-party payables (the director's advances) $1,172,259,
$1,526,557, $1,853,263, $1,347,019, $1,366,738. No goodwill or intangibles. What moved and why: receivables grew with the 2023
contract and did not come back as cash; $1,523,063 of trade receivables was classed non-current at 2024-12-31 (a customer paying
over more than a year), and the expected-credit-loss charge rose from $6,019 (2020) to $636,182 (2024). Listing fees inside G&A
were $354,743, $328,699, $1,241,199 and $190,506 from 2021 to 2024. The FY2024 20-F's reconciliation is headed "Adjusted EBIDA
(Non-GAAP)" and presents "Adjusted EBITDA and Adjusted EBITDA Margin" as "key performance indicators" (Item 5), negative in all
three years. The audited subsequent-events note reads "to the date of May [ ], 2025", the date left blank in the filed report.
Material weaknesses are disclosed, "related to a lack of accounting staff and resources with appropriate knowledge of U.S. GAAP
and SEC reporting and compliance requirements" (Item 16F). The auditor changed from WWC, P.C. to AOGB CPA Limited, engaged on
2023-12-15 (Item 16F). The 2,264,077 shares awarded in December 2024 carried no expense in 2024 (Note 11: "There is no vesting
on the year ended December 31, 2024.").

**Q5 (people; integrity facts, recorded, not judged).** (1) The chairman and chief executive, Mr. Pui Lung Ho, owned through Wang &
Lee Brothers, Inc. 8,000,000 shares, 25.19% (Item 7, FY2024 20-F), and received 150,477 of the 2,264,077 shares awarded on
2024-12-18 (Item 6). (2) On 2023-03-20, a month before the IPO at $5.00, 1,400,000 shares were placed privately "at $ 0.25 per
share to the selling shareholders" (Note 11). (3) The share count went from 17,357,924 (2024-12-31) to 174,679,566 (July 2025,
6-K 0001641172-25-025052) through a registered direct offering with reset warrants (424B5 of 2025-03-24, 0001641172-25-000251)
and $8,000,000 of senior convertible notes sold "for net proceeds of approximately US$3,570,000", convertible at 85% of the
lowest daily VWAP (6-K of 2025-06-09, 0001641172-25-014262). (4) Nasdaq's staff moved to delist "based on public interest
concerns primarily in relation to the Company’s June 9, 2025 issuance of convertible notes" (6-K of 2025-06-30,
0001641172-25-017061); the Panel denied continued listing for violation of the "Public Interest Concern", "Listing of Additional
Shares", "Bid Price", and "Low Priced Stocks" rules (6-K of 2025-08-26, 0001641172-25-025474), after a plan that included "the
cancellation of the convertible notes previously issued". (5) A press release announced a "US$71 Million Contract" for "Dual-Purpose
Marble Quarrying and Solar Crypto Farm Operations in Queensland" (6-K of 2025-03-17, 0001493152-25-010621) while the core business
lost money; the FY2024 20-F's "Market and Competition" section describes waste management and cryptocurrency mining rather than
the E&M market (Item 4.B). (6) The company stopped filing after the Form 25 of 2025-11-21, with no 20-F for FY2025. Any later run
that reaches Q5 must answer these **[M2013-088]**.

**Q6 (money and owners).** The 2025 issuance (above) is the behaviour the rows describe in "we have never invested in companies that
are hell-bent on issuing shares" **[L2014-015]** (recorded, not weighed). The Solar HK purchase was first to be paid with a note
convertible at 80% of the market price (6-K of 2025-04-01), amended to cash on 2025-08-08; the consideration, HK$15,000,000, was
about 45% of the year-end cash of $4.30M. No dividend or buyback.

**Q9 (debt).** Bank loans of $2.34M against negative operating cash flow in every year; the $8M convertible notes were due nine
months after June 2025 unless extended; whether they were converted, repaid or remain is not on file.

**Q12.** The 2025 announcements include solar-powered cryptocurrency mining; the newspaper test is not run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit f1c1a8c1); written question by question; committed after each (Step 0 and
      foundations 21e604e6; Q1 09b764e4; Q2 655c9eb3; the remaining sections in the closing commit).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (the lock file was
      present in `Screens/_daily/` when I listed it); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One directory listing of `Test Runs/` showed the
      file names of other runs dated today; declared under contamination above and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`scripts/check_ids.py`, output `check_ids_output.txt`); every filing fact has its accession; the peer figures carry theirs.
- [x] The order was kept; Q2's STOP closed the file; nothing after it is a clearance; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash is operating cash flow less capital spending, never a net-income proxy (the net-result variant is shown beside,
      labelled). **Not met: the sovereign from the issuing authority.** The HKMA endpoint refused every request (HTTP 405); a USD
      stand-in is used and confessed as a CONVENTION of this run; it cannot change the sign of any figure. The quote is an
      aggregator's, flagged.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No point-in-time anchor; no row dated after an anchor is at issue.
- [x] `tools/run.py` printed no line (refused, then "UNRESEARCHED" through the CIK wrapper); no rule, id or verdict from it was used.
- [x] `python tools/check_framework.py`: PASS (run 2026-10-17, before the closing commit); the run's own check (`scripts/check_ids.py`): no E-ids, 33 distinct ids all in the ledger, every quoted fragment beside an id in its row, 0 problems.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**A filer that has stopped filing.** Q1's test 3 asks whether the past statements tell me the future ones **[M2008-033]**, and the
doubt row says "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. Neither the
framework nor the template says what to do when the company has stopped reporting: the last audited year is 22 months old, the
company has announced a move out of its field, and its share count is unknown. One reading closes the file at Q1 TOO HARD on the
doubt; which cause, WORK or NATURE, is then unclear, since no filing exists to read (not WORK in the framework's sense of "a filing
not yet read") and the industry's insiders could write the forecast down (not NATURE). I read Q1 on the business the filings show,
by the parts paragraph, and let Q2 decide on the evidence; a different analyst could close at Q1. A rule is wanted, for example
that a filer with no audited year in the last eighteen months is read on its last audited years at Q1 and Q2, with the gap
flagged in the box line. **No HKD sovereign in the protocol's table**, and the HKMA's public API refused an automated request;
the protocol could name the HKMA series and a fallback (the brief anticipated the first half). **Comparables when the filer names
none**: the brief asks the run to confess its own choice; a standing rule (a stated EDGAR search, as here) would make runs
comparable. **Per-share figures with an unknown share count**: Part VII's fair price is per share, and Q7's net-debt rule takes
subsequent events only from the last filing; for a delisted issuer whose later 6-Ks show heavy issuance, neither yields a usable
per-share figure, and the run shows two counts. **Q7 with negative owner cash in every year**: specific (b) gives the no-growth
case alone, which is then a negative value; the text does not say that a negative range means "no fair price", which is what this
run reports.
