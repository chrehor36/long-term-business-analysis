# Company Run: Arcadis N.V. (Euronext Amsterdam: ARCAD; US OTC ADR: ARCAY), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the template `Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit `4cbb1228`). Every
judgment cites a v5 ledger id in bold; every filing fact carries its document and page (Arcadis files no annual report
with the SEC, so a document name, date and PDF page stand in place of an accession number, as the brief directs). A STOP
that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (99593cb6): `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatch.** Dispatched blind run of record under the brief of 2026-10-17 (a departure from the canonical brief for a
name with no SEC filings, stated in the brief). The lock `Screens/_daily/_overnight.lock` was present when this run
started (seen in a directory listing at the start; not opened); the dispatching session holds it.

**Contamination, declared and not used.** (1) The git status shown at session start lists other companies' research
folders by name (an ARCB folder of 2026-09-27 and an AYI folder of 2026-09-26) and the recent commit subjects name a KBR
run of 2026-10-17 closed OUT at Q2 on its own castle; none was opened, and nothing of them is used here. (2) An auto-memory
index line loaded at session start says, in general terms, that some number of names cleared the gates under the old
edition and "nothing buyable"; it names no company and is not used. (3) No file about Arcadis under any name or ticker
was opened, listed or searched: the only `Test Runs/` listing made was a filename filter for "arcad|ARCAY", which
returned nothing.

**Documents read (operator rule 4; primary documents from the issuer's investor site, URLs in the research notes):**
- Arcadis Annual Integrated Report 2025 (PDF, financial statements authorized 18 February 2026), the full statements,
  notes 4 to 7, 14, 21, 25, 28, 29, 31, 32, the business sections, the risk-management chapter (pages 152 to 155; the
  principal-risks table on PDF pages 157 to 162 is an image in both the PDF and the official iXBRL package and could not
  be read as text), the remuneration report and the appendices. Cited below as "AR2025 p.N" (PDF page).
- Arcadis Interim Financial Statements 2026 (six months to 30 June 2026, authorized 30 July 2026) and the H1 2026
  press release of 30 July 2026. Cited as "H1 2026 IFS".
- Annual reports for 2016, 2017, 2018, 2019, 2020, 2021, 2023 and 2024 (statements and the passages cited). The 2022
  report was not at the address pattern tried; its figures are taken from the comparative column of the 2023 report.
- Competitor filings from SEC EDGAR company facts (XBRL, transcription only, cross-checked as stated in Q2): AECOM 10-K
  FY2025 (accession 0000868857-25-000013), Jacobs Solutions 10-K FY2025 (accession 0001628280-25-053316), Stantec 40-F
  FY2025 (accession 0001131383-26-000007).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 41.20, close 2026-10-16, Euronext Amsterdam (ARCAD.AS), from Yahoo Finance via `tools/sources.py`
  (**aggregator, flagged**, operator rule 5; live quote only). The US OTC line ARCAY closed at USD 44.81 the same day
  (same aggregator); the depositary's documents were not read, so the ADR ratio is not confirmed and the ADR is **not**
  priced. Every per-share figure in this file is in **EUR per ordinary share**.
- **Shares** (no SEC cover page exists; `python Screens/cover_shares.py ARCAY` returned "ARCAY NOT AN SEC REGISTRANT in
  the live ticker file"). From the company's own share notes: issued 90,442,691 ordinary shares; treasury 4,313,923;
  **outstanding 86,128,168 at 31 December 2025** (AR2025 p.238, note 25); then 1,070,633 repurchased and 148,066 reissued,
  **outstanding 85,205,601 at 30 June 2026**, treasury 5,236,490 (H1 2026 IFS, note 17). The AGM of 20 May 2026 approved
  cancelling 4,575,796 treasury shares; not yet effective at 30 June (same note). One class only carries economics: 600
  priority shares held by the Priority Foundation carry control rights and a dividend of 5% of their EUR 0.02 par
  (AR2025 p.239 to p.240); no preference shares are issued. **Count used: 85,205,601.**
- **Market cap:** 85,205,601 x EUR 41.20 = **EUR 3,510.5M**.
- **Sovereign for the earnings currency:** the reporting and functional currency of Arcadis N.V. is the euro (AR2017 p.84,
  basis of preparation; the 2025 statements are in EUR millions). **EUR 30-year: 3.67%**, ECB euro area AAA yield curve
  (YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y), observation 2026-10-15, issuing authority, via `python tools/sources.py`. Stated
  plainly: about two thirds of net revenue arises outside the euro area (United States 1,394, Canada 263, UK and Ireland
  831 of 3,760 million, AR2025 p.206); the same tool gives the US Treasury 30-year at 5.43% (2026-10-16). The euro rate is
  used because the owner cash is earned, reported and paid out in euros; the mismatch is carried to the framework section.
- **Filings read:** listed above. No proxy exists in the US sense; the remuneration report (AR2025 p.181 to p.191) and the
  governance chapter stand in for it.
- **One figure cross-checked against the filed statement:** net cash from operating activities 2025, EUR 386M, in the
  consolidated cash flow statement (AR2025 p.200) and in the company's free-cash-flow reconciliation (AR2025 p.301:
  386 - 25 capital expenditure + 1 proceeds - 74 lease payments = 288). Net revenue 2025, 3,760, agrees between the
  income statement (p.196) and the segment note total (p.207).
- `python tools/run.py ARCAY` returned: "ARCAY: not an SEC filer. Use the evidence ladder [...] This is UNRESEARCHED, not
  UNKNOWABLE." No arithmetic line was produced; **all arithmetic below is done by hand from the filed statements**, in
  `Test Runs/_research 2026-10-17 ARCAY/scripts/owner_cash.py`, output in `owner_cash_output.txt`.

**Owner cash after every real cost, by year (EUR M)** = net cash from operating activities (already after interest paid
and received and corporate tax paid, and after the change in working capital) less investments in (in)tangible assets,
plus proceeds of asset sales, less payments of lease liabilities (shown in financing from 2019 under IFRS 16; before 2019
rent sat inside operating cash), less share-based compensation (added back in operating cash; stock pay is a real cost),
less net other non-current investments. 2025 is reduced by EUR 19M, the filer's own "non-organic 19 million cash
amelioration derived from factoring facility settled end of 2025" (AR2025 p.186; receivables of EUR 34M were sold
non-recourse at year end, p.235). The all-equity column adds back net interest paid at the company's own five-year tax
rate of 27.5% (income taxes / profit before tax, 2021 to 2025, filed income statements). Purchases are cash paid for
businesses and for associates and joint ventures, net of disposals.

| Year | Owner cash, equity basis | Owner cash, all-equity basis | Purchases (net) | % of net revenue (all-equity) |
|---|---|---|---|---|
| 2016 | 70.7 | 88.2 | 12.0 | 3.6% |
| 2017 | 88.5 | 105.8 | 14.4 | 4.3% |
| 2018 | 145.7 | 161.5 | 39.9 | 6.6% |
| 2019 | 83.4 | 101.5 | 24.8 | 3.9% |
| 2020 | 317.3 | 331.8 | 57.0 | 13.3% (the filer: "exceptional working capital improvement", AR2021 p.114) |
| 2021 | 225.8 | 234.5 | 4.6 | 9.1% |
| 2022 | 168.7 | 179.1 | 798.9 (IBI Group, cash) | 5.9% |
| 2023 | 182.8 | 201.3 | -3.9 | 5.4% |
| 2024 | 219.0 | 250.9 | 1.0 | 6.5% |
| 2025 | 260.0 | 291.9 | 84.0 (KUA Group, WSP Germany rail) | 7.8% |
| **avg 2021-2025** | **211.3** | **231.6** | **176.9** | |

Capital spending 2021 to 2025 was 25 to 45 a year against depreciation and software amortization of 100 to 114 (of which
most is right-of-use depreciation, whose cash is the lease payment already deducted). Stock pay was 6 to 12 a year.

**The balance sheets, ten of them, read before the income account (Q4's instruction, read here because the file closes
before Q4).** EUR M, 31 December; filed statements AR2016 p.151, AR2017 p.82, AR2019 p.179, AR2021 p.207 (2020 restated
under IAS 8 for cloud-computing configuration costs, AR2021 p.214 to p.215), AR2023 p.172, AR2025 p.198; H1 2026 IFS.

| | 2016 | 2017 | 2018 | 2019 | 2020r | 2021 | 2022 | 2023 | 2024 | 2025 | 30 Jun 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Goodwill and intangibles | 1,170 | 1,074 | 1,054 | 1,080 | 829 | 866 | 1,581 | 1,505 | 1,506 | 1,473 | 1,476 |
| Total equity | 1,002 | 981 | 944 | 965 | 866 | 1,022 | 993 | 1,061 | 1,230 | 1,033 | 1,052 |
| Cash | 260 | 268 | 241 | 297 | 449 | 351 | 273 | 290 | 376 | 323 | 273 |
| Trade receivables + contract assets - contract liabilities | 853 | 781 | 874 | 988 | 639 | 641 | 871 | 807 | 864 | 727 | 936 |
| same, % of gross revenue | 25.6% | 24.3% | 26.8% | 28.4% | 19.3% | 19.0% | 21.6% | 16.1% | 17.3% | 14.9% | (half year) |
| Loans and borrowings + overdrafts | 757 | 691 | 588 | 611 | 501 | 264 | 973 | 881 | 854 | 879 | 1,086 |
| Net debt, leases excluded | 497 | 423 | 347 | 314 | 52 | -87 | 701 | 591 | 478 | 556 | 813 |
| Lease liabilities | - | - | - | 291 | 278 | 255 | 315 | 281 | 262 | 252 | 238 |

What moved and why. (1) **Goodwill and intangibles exceed equity in eight of the ten year ends**: tangible equity is
negative, and the equity is mostly the price paid for past acquisitions (Hyder and CallisonRTKL before the span, IBI Group
in 2022 for 799.6M cash, AR2023 p.174). (2) **Equity barely moved in ten years** (1,002 to 1,033) while the company
reported cumulative net income of about 1,050 over 2016 to 2025; the difference went out in dividends and buybacks and was
lost to translation (the translation reserve stood at -254 at the end of 2025, AR2025 p.199) and to write-offs (goodwill
impairments of 15 in 2016, 40 in 2018 for the Middle East and Latin America, AR2018 p.86, and 119 in 2020 for the Middle
East and CallisonRTKL, AR2020 p.111; the ALEN associate in Brazil, an expected credit loss of 53 in 2018 and a further
provision of 85 in 2019, AR2018 p.86 and AR2019 p.9, with cash of 64.7 paid to it in 2020, AR2021 p.210). (3) **Working
capital fell from about a quarter of gross revenue to about a seventh**, the main source of the better cash since 2020;
part of the 2025 figure is the factoring sale noted above, and the half-year balance sheet shows the seasonal rebuild
(936 at 30 June 2026). (4) **Net debt** fell to a net cash position in 2021 and was rebuilt by the IBI purchase; it stood
at 813 at 30 June 2026 after the 2025 to 2026 buyback of about 178M and the dividend. What the figures do not say: the
balance sheet carries the people only as payroll, so nothing on it shows what the business would be without its staff;
"what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is that a share is a business: the question is whether one "Would [...] be happy buying
this stock if the market closed for five years" **[M1997-109]**, which for a firm of 34,000 consultants means owning their
billable hours and their bids for a decade, not the 40% fall of the shares in 2025 that the company itself reports against
its peer group (AR2025 p.44). The habit applied throughout is "looking for what’s wrong in things because that’s part of
investing – looking at what you’re missing" **[M2025-013]**. **Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**):
(i) the filer's own words in 2019, "much needed differentiators for us in an increasingly commoditized market" (AR2019
p.19); (ii) goodwill above equity in most years; (iii) a run of write-offs in 2016 to 2020 in parts later shrunk or exited
(Middle East operations "are being wound down", H1 2026 press release footnote 7; Intelligence "is no longer managed or
reported as a separate Global Business Area" from 2026, H1 2026 IFS note 4); (iv) a chief executive change on 1 March 2026
(AR2025 p.8); (v) for the business: 95% of 2025 revenue came from clients also served in 2024, and no client exceeds 10%
of revenue (AR2025 p.12 and p.207).

## THE STANDING RULE
A part-interest bought for cash, unlevered, in a liquid listed share puts the buyer at no risk of ruin from the purchase
itself; the rule binds how it would be financed and sized, "never going to risk what we have and need for what we don’t
have and don’t need" **[M2012-081]**, "Never risk permanent loss of capital" **[L2023-005]**. No borrowing is assumed.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from its own report.** Fees for the time of its own staff (net revenue, 3,760M in 2025, is
  gross revenue less subcontractors and third parties, AR2025 p.298) in design, engineering, project management,
  environmental and advisory services for natural and built assets, to public, regulated and private clients; 9,000+
  clients a year, the largest projects under 5% of net revenue, 95% of revenue from clients served the year before
  (AR2025 p.12); about 270 "Key Clients" give 65% of net revenue (p.15). Revenue is recognized over time on labour cost
  incurred against labour cost estimated (p.211); the auditor singles out contracts "that include a fixed price element"
  (AR2024 p.324). Four Global Business Areas in 2025: Resilience (water, environmental restoration, energy transition,
  climate adaptation), Places (buildings, industrial and data-center facilities, property), Mobility (rail, highways,
  transit), Intelligence (software); three from 2026.
- **The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular business, and
  evaluating how predictable they were first" **[M1998-044]**): billable headcount and its utilization; the
  hourly rate set against wage inflation; the public and regulated capital programmes that fund the work (US water and
  remediation, UK water's five-year AMP cycles, German grid expansion, transit); fixed-price exposure; receivables; and the
  price of the acquisitions through which the firm has grown. Each is visible in the filings year by year, and the
  statements of the last ten years do say what the next ones will look like in kind ("the financial statements will tell me the information that’s useful to
  me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**): a fee business whose
  revenue tracks headcount and whose margin moves within a band (operating EBITA 7.3% to 11.5% of net revenue from 2018 to
  2025, AR2023 p.165 and AR2025 p.297).
- **Would the insiders write the forecast down?** They do: the company publishes three-year targets (for 2027 to 2029,
  "Mid-single digit" organic growth and an operating EBITDA margin "Mid- to high-teens by 2029", H1 2026 press release),
  which is the opposite of the "That’s too hard" of **[M2000-105]**; whether to believe them is a later question.
- **Change.** The industry is a century old (Arcadis's roots go to 1888, AR2025 p.12); the change on the horizon is the
  automation of design work, which the company names as an opportunity (its stake in Nomic, "AI engineering workflow tool
  increasing design speed and quality for our clients under lump-sum contracts", H1 2026 press release). That change bears
  on who keeps the fee for a design hour, which is the castle question; it does not make the ten-year economics of a
  consulting engineer unforeseeable in kind. Routed to Q2 test 11, as the framework routes it.
- **Contrary evidence, written down.** Munger in 1997 on firms of this kind: "we are not in the business of designing oil
  refineries with armies of engineers [...] By and large, we’ve avoided the field. Again, it’s hard for us to understand."
  **[M1997-114]**. Weighed, not decisive: the row states the speakers' own field of choice; the test the framework applies
  is the foresight test, "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" **[M2012-065]**, and the doubt test, "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]**. What I can foresee is the earning power in kind (a fee business at the field's
  margins, growing with infrastructure spending and acquisitions); what I cannot foresee is whether Arcadis holds any
  advantage over the next bidder, and that is Q2's question, not a doubt about understanding what the business is.
- **Routing.** Not a bank or financial institution; not a holding company. Its operating segments are read by parts at
  Q2.
- **VERDICT: IN.** The economics are understandable and foreseeable in kind for ten years, "a reasonable probability of being
  able to asses where the business will be in 10 years" (the transcript's spelling) **[M2000-037]**, the "first question" of
  **[M1995-051]**:
  the key variables are few and visible in the filings, and the insiders write forecasts down. The open question is the
  castle.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question as the row puts it: "why is that castle still standing? And what’s going to keep it standing or cause it not
to be standing five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**; and
the moat is what "protects excellent returns on invested capital" while "competitors will repeatedly assault any business
"castle" that is earning high returns" **[L2007-004]**.

**Lines of evidence chosen (a departure from the canonical brief, stated as the brief directs).** The equivalents of a
10-K's Item 1 are AR2025 p.10 to p.15 (About Arcadis, how it works, strategic focus areas) and the four Global Business
Area chapters (p.20 to p.40); of Item 1A, the Enterprise Risk Management chapter p.152 to p.155 (the principal-risks
table itself, p.157 to p.162, is an image and was not readable, said so) and the auditor's key audit matters (AR2024
p.324); of Item 7, the financial performance review (AR2025 p.42 to p.43), the segment note (p.205 to p.207), the
five-year summary and the alternative performance measures (p.297 to p.301), with the same sections of the earlier
reports for the span.

**The parts table** (section B of the gaps case). Segments with different economics are reported: Resilience, Places,
Mobility, Intelligence (2022 to 2025; in 2021 the segments were geographic, Americas, Europe and Middle East, Asia
Pacific and CallisonRTKL, AR2021 p.217, so the share is taken over the four years of the current structure, said so).
Segment operating EBITA, EUR M (AR2023 p.182 for 2022 and 2023; AR2025 p.207 for 2024 and 2025):

| Part | 2022 | 2023 | 2024 | 2025 | Sum | Share (operating EBITA) | Share (segment operating income) | Margin on net revenue 2022 to 2025 |
|---|---|---|---|---|---|---|---|---|
| Resilience | 133.8 | 158.8 | 194 | 205 | 691.6 | 43.9% | 50.6% | 10.8%, 11.8%, 13.4%, 14.4% |
| Places | 92.9 | 136.6 | 151 | 106 | 486.5 | 30.9% | 23.7% | 9.1%, 9.1%, 10.2%, 7.9% |
| Mobility | 72.3 | 90.5 | 100 | 108 | 370.8 | 23.5% | 25.0% | 9.7%, 11.1%, 11.6%, 11.9% |
| Intelligence | 1.9 | 10.9 | 9 | 4 | 25.8 | 1.6% | 0.7% | 9.2%, 11.6%, 9.7%, 4.3% |

**Resilience decides**: it is the largest part on the company's own segment measure (43.9%), and more than half on
segment operating income after amortization and non-operating costs (50.6%). It is water (US utilities, UK water's AMP 8
cycle), environmental restoration (remediation), energy transition (German and Dutch grid programmes) and climate
adaptation (AR2025 p.22 to p.24). Places and Mobility, which do not decide, are read for the same tests and carried
below.

**The castle tests, each with its filing fact.**
1. *"What are the key factors? And how permanent are they?"* **[M1995-038]**. What brings a client to Arcadis rather than another firm, in the
   company's own account: relationships with repeat clients (95% of revenue from clients served the year before; 270 Key
   Clients giving 65% of net revenue), technical rankings (ENR "#1 for semiconductors, pharma, and hazardous waste"; "Top 5
   in [...] drinking water treatment [...] remediation", AR2025 p.12), and positions on multi-year programmes. None of
   these is a thing a rival cannot also hold: the same ENR tables rank the rivals beside it, and the company's own
   strategy is to win share of wallet from those same clients against them ("growing our share of wallet within Key
   Clients", p.15). The factor that is permanent is the client's need, not Arcadis's place in meeting it. The company's
   own description of its market, in 2019: "much needed differentiators for us in an increasingly commoditized market"
   (AR2019 p.19).
2. *Would it stand without the lord?* The asset is the staff, who are paid as wages and can leave (voluntary turnover
   10.7%, H1 2026 press release). The 2026 strategy is a reorganisation around client sectors, a new incentive programme
   and the redeployment of "over 200 leaders into customer-facing roles" (H1 2026 press release): a business whose results
   are being re-earned by management action, which is the "have to stay smart" case of **[M1995-040]**.
3. *The money test* **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
   could I do it? [...] If the answer had been yes, we wouldn’t have done it." Here the attackers with money are named in
   the report's own peer group and they act: Stantec paid C$702M (2021), C$555M (2024) and C$454M (2025) for businesses
   (40-F XBRL, accession 0001131383-26-000007); AECOM paid USD 213M in FY2025 (10-K, 0000868857-25-000013); WSP sold
   Arcadis its German rail-engineering business in April 2025 (AR2025 p.209); and Arcadis itself entered Canada at scale by
   paying 799.6M cash for IBI Group in 2022 (AR2023 p.174). Share in this field is bought with money and hiring, so the
   answer to the See's question is yes.
4. *Pricing power: "the agony they go through in determining whether a price increase can be sustained"* **[M2005-020]**. Through the last inflation Arcadis passed its costs on:
   average remuneration per employee rose 8% in 2022 and 13% in 2023 (AR2023 p.165) while the operating EBITA margin rose
   from 9.6% (2021) to 10.4% (2023) and 11.5% (2024). But the rivals' margins rose in the same years (competitor row
   below), so the pass-through was the field's: the test that "the businesses with strong competitive positions manage to
   pass through [...] increases in labor costs" **[M2005-017]** was met by every firm at once, which shows a market priced
   at cost plus a margin, not a castle at Arcadis. Where demand weakened the margin did not hold: Places fell from 10.2% to
   7.9% in 2025 and 7.4% in H1 2026, "impacted by weak Property & Investment billability" (H1 2026 press release).
5. *Unit volume and share of mind.* Net revenue organic growth 3.0%, 3.1%, -1.5%, 4.2%, 8.9%, 9.0%, 4.5%, -0.5% from 2018
   to 2025 (AR2023 p.165; AR2025 p.191): volume moves with the clients' capital programmes. No share-of-mind evidence: the
   client asks for a qualified firm, not for Arcadis by name.
6. *The low-cost position: "to be the low-cost operator"* **[L2004-007]**. The company cites its Global Excellence Centers in the Philippines, India and
   Romania for efficiency (AR2025 p.12) and their "higher utilization" for the 2026 margin (H1 2026 press release); no
   filing read shows Arcadis's cost per hour below its rivals', and its group margins sit inside the rivals' band, not
   below their costs. Not shown.
7. *The brand.* The firm works under one name, Arcadis (AR2025 p.12); no filing evidence that the name, rather than the
   team and the price, wins the work.
8. *The low bid: "it wouldn’t be a question of people buying candy for the low bid"* **[M2017-009]**. Public and regulated clients procure by tender
   and framework; the company describes its own response as "a disciplined and selective order intake approach focusing on
   higher margin projects" (AR2025 p.22) and "making deliberate bidding choices" (p.15), which is choosing which contests
   to enter, and the auditor's key matter is the fixed-price element in contracts (AR2024 p.324). On no evidence read does
   the customer pay up for Arcadis over an equally qualified bidder.
9. *Ask the competitors "which one would it be and why?"* **[M1999-130]**. Not done (no access); the public record that stands in for it is the competitor
   row below.
10. *"whether it’s likely to widen further or shrink on you"* **[M1999-108]**. Mixed, by part: Resilience's margin widened each year 2022 to 2025 (10.8% to
   14.4%), which the company credits to "increased selectivity and shift towards high growth sectors" (AR2025 p.22);
   Places narrowed; Intelligence, the software part, is dissolved into the other areas from 2026 (H1 2026 IFS note 4); the
   Middle East is being wound down; CallisonRTKL and the Middle East carried goodwill impairments of 119M in 2020 (AR2020
   p.111).
11. *What could "destroy, or modify, or reduce the economic strengths"* **[M2000-014]**. Two things on the filings: the public budgets that fund the
   work (the UK Spending Review and the delay of AMP 8 investment are named for 2025, AR2025 p.22), and the automation of
   design hours, where in a fee-for-hours business "the improvement you get one day, your competitor gets the next day.
   And it very much tends to work to the benefit of consumers but not to increase overall profitability." **[M2004-053]**.

**The competitor row** (rivals the report names; up to three that file with the SEC). The report names its peer group:
AECOM, AFRY, Alten, AtkinsRéalis, Fugro, Jacobs, NV5, Spie, Stantec, Sweco, Tetra Tech, Worley and WSP (AR2025 p.44 and
p.183). Read: **AECOM** (10-K), **Jacobs Solutions** (10-K) and **Stantec** (40-F), the three largest design and
consultancy firms among the SEC filers named. Flagged as named and not filing with the SEC, not read: WSP Global,
AtkinsRéalis, Sweco, AFRY, Fugro, Worley, Spie, Alten. Named SEC filers not read (the brief's limit of three): Tetra Tech,
NV5. Same metrics, from each filer's own figures (XBRL company facts, latest filed value for each year; Jacobs is on
continuing operations as last filed; Stantec's line is profit before tax, as its IFRS tags carry no operating-income
line). Script and output: `scripts/peers.py`, `competitor_row.txt`.

| Metric, mean over 2016 to 2025 | Arcadis | AECOM | Jacobs | Stantec |
|---|---|---|---|---|
| Operating income / revenue | 5.0% (range 2.4% to 7.8%) | 4.0% (FY2017-25; 2.3% to 6.4%) | 4.8% (3.1% to 7.2%) | n/a |
| Profit before tax / revenue | 3.8% (0.1% to 6.8%) | | | 5.8% (4.2% to 7.7%) |
| Net income / year-end equity | 9.9% (-2.8% to 20.1%) | 6.4% (-7.1% to 22.5%) | 9.2% (2.8% to 17.7%) | 9.6% (2.5% to 14.8%) |
| Goodwill / equity, 2025 | 1.42 | 1.48 | 1.31 | 0.99 |
| Direction 2021 to 2025 | margin up | margin up | margin up | margin up |

Arcadis's figures are from its filed statements; the three rivals' are XBRL transcription and were not checked against
their HTML filings (said so).

**The field's returns over the last full cycle, judged in words** (section C). The four firms' margins sit in one narrow
band and moved together, low in 2018 to 2020 and higher in 2021 to 2025; no firm's margin stands apart over the decade.
On the equity owners have put up, which in this field is mostly purchased goodwill, the field's ten-year return is
ordinary, near ten percent, with years of loss at Arcadis (2018) and AECOM (2019, 2020). The row against this reading is
the rows' own instruction to judge a business on tangible capital: "Goodwill should not be used in evaluating the
fundamental attractiveness of a business. There you should look at return on tangible assets" **[M2011-060]**, and on that
measure Arcadis earns a high return (operating EBITA of 418M in 2025 against net working capital of 397M, AR2025 p.300,
and under 100M of fixed assets), as service businesses do: "They require less capital" **[M2009-047]**. That is carried
to Q3 as a weighing FOR. It does not answer Q2, because the same high return on tangible capital is earned by every rival
in the row and by any team of engineers that sets up or is bought: it comes from the absence of capital in the work, and
it is open to anyone who hires the people. The castle question is what keeps the next equally qualified bidder from the
next contract, and on the filings nothing does.

**A change for the better** (section C). Arcadis's return on equity rose from about 3% in 2016 to 2020 to 13% to 20% in
2021 to 2025. The change is field-wide (every firm in the row improved in the same years), so it is not evidence of an
Arcadis castle; in the one year of falling volume since (2025: net revenue -3.1%, organic -0.5%, AR2025 p.42), the
weaker part's margin fell by a fifth (Places 10.2% to 7.9%) and the group held its margin by rightsizing and
restructuring (non-operating costs of 40M in H1 2026, H1 2026 press release). The rule that a change for the better waits
a full cycle does not help the castle here: even credited, it would raise the field, not separate Arcadis from it.

**Why it is a STOP, applied.** The deciding part's castle is shown open on the evidence of the filings: share is bought
with money by named rivals and by Arcadis itself (test 3 fails, **[M2011-015]**); the field's improvements are shared, the
"competitive nature to capitalism where the improvement you get one day, your competitor gets the next day"
**[M2004-053]** visible in the competitor row; this is a field where "anything you do, your competitors can copy"
**[M1996-017]** and one of the industries "that are just never going to have barriers to entry" **[M2012-106]**, in the
filer's own word "increasingly commoditized". Those are OUT on the framework's list (Q2, What it rules OUT, first item).
It is not a castle whose future cannot be judged (TOO HARD): the future of the field is judged, and it is a contest
without a moat. A lower price would not cure it: "What you can’t do is turn any investment into a good deal by paying
little" **[M2019-015]**.

Evidence for the castle, weighed and not enough: the repeat-client figure (95%), the rising Resilience margin, the high
"return on tangible assets" **[M2011-060]** ("They require less capital" **[M2009-047]**), and the ENR leadership in hazardous waste and remediation.
Each is shared with or contestable by the rivals in the row; none is a barrier.

- **VERDICT: OUT.** The deciding part (Resilience, 44% of four-year segment operating EBITA, 51% of segment operating
  income) and the field around it earn their returns in open competition with named, well-funded rivals who buy and hire
  their way into the same clients; no castle test shows a barrier. The See's question is answered yes, and "If the answer
  had been yes, we wouldn’t have done it." **[M2011-015]**; the field's gains are shared, "your competitor gets the next
  day" **[M2004-053]**. Places and Mobility, which do not decide, show the same marks and are carried as ordinary businesses.

---
## Q3 to Q12: NOT REACHED
The file closed OUT at Q2 (operator rule 2). Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are not answered; nothing below is a
clearance. The facts already found for them are under AFTER THE STOP, written down and not weighed.

## COMPUTATION, NOT A CLEARANCE: Q7's range and the two reporting figures
*Made at the owner's request (the brief's reporting convention). No entry language; operator rule 3. Script
`scripts/q7_computation.py`, output `q7_computation_output.txt`.*

**Inputs.** Owner cash as in Step 0: five-year average 2021 to 2025, **231.6M on the all-equity basis** (before interest,
after the company's tax) and **211.3M on the equity basis**. Discount rate: the EUR 30-year, **3.67%**. Net debt at the
latest filed balance-sheet date, 30 June 2026: borrowings 1,086 + overdrafts 0 - cash 273 = **813M**; lease liabilities
(238M) are left out because their payments are already deducted inside owner cash, said so; the 225M Schuldschein
repayment of 20 July 2026, the one stated subsequent event with a figure, was paid from cash and leaves net debt unchanged
(H1 2026 IFS note 24). Shares 85,205,601. Market value 3,510.5M; market value plus net debt **4,323.5M**.

**The specifics, as Q7's text applies them.**
- (a) *Cycle base.* The window 2021 to 2025 is used as filed: the filer calls 2020's cash "outstanding due to exceptional
  working capital improvement" (AR2021 p.114), but 2020 is outside the window; neither end year of the window is described
  by the filer as aberrational. The last year is reduced by the filer's own 19M non-organic factoring figure (Step 0). The
  literal window is therefore the base; nothing is shown beside it because nothing differs.
- (b) *Decline.* The growth shown is positive; not applied.
- (c) *Acquisitions.* Net purchases over the window were 884.6M against owner cash before purchases of 1,157.8M (half is
  578.9M), so **the serial-acquirer convention applies**: the central figure is the organic pair, purchases left out and
  growth taken as the filer's reported organic growth of net revenue, 8.9%, 9.0%, 4.5% and -0.5% in 2022 to 2025, a
  compound **5.40%** a year (AR2025 p.191). The default pair (purchases deducted at their window average of 176.9M a year
  for ten years, total growth of all-equity owner cash 2021 to 2025 of 5.62% credited, purchases stopping after year ten)
  is shown beside. Every deal in the window was paid in cash (IBI Group 2022; KUA Group and WSP Infrastructure Engineering
  2025, consideration 106M including a 10M earn-out, AR2025 p.210): no merger by the framework's definition. The SATEL
  purchase was signed after 30 June 2026 and had not closed at 30 July 2026, with no price disclosed (H1 2026 IFS note 24):
  a signed, unclosed deal with no filed record to value it on, so nothing is shown beside for it, said so.
- (d) *Working capital.* Counted: operating cash is after the change in working capital each year.
- (e) *Growth spending.* The filing does not allow the maintenance guess to be separated: capital spending is small (25M to
  45M) and the growth outlay of this business is hiring and training, inside personnel costs. The all-spending case is
  therefore the central case, said so.
- (f) *The cap.* The growth carried is a revenue growth rate applied to owner cash, so owner cash stays at its base share of
  net revenue (6.2% of 2025 net revenue) and never reaches the highest share earned in the years read (13.3%, 2020); no cut.
  Zero nominal growth after year ten.

**The floor, tested first.** Expected return at the price on each case: central no-growth **5.36%**, central growth
**7.96%**; default pair 4.02% and 6.38%; equity-only 6.02% and 8.84%. **No case earns the floor of about ten percent at
EUR 41.20** ("we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**). Had the file
reached Q7, it would have closed **OUT** on the floor, whatever the width.

**(a) VALUE RANGE (central, all-equity basis, at 3.67%, less net debt):** **EUR 64.52 to EUR 107.66 per share** against
**EUR 41.20**. Width 1.67 to one. The default pair beside: EUR 47.39 to EUR 92.73.

**(b) FAIR PRICE** (each end valued at ten percent, the two averaged, after the company's own tax): **EUR 23.74 per share on
the all-equity basis (the central figure)**; **EUR 30.37 per share on the equity-only basis** (owner cash after interest
against the market value, beside it, never deciding alone). The default pair's fair price would be EUR 11.28.

The two figures pull against each other and the reader should see why: the range is built at the euro 30-year rate of
3.67%, so it sits far above the price, while the fair price applies the floor of ten percent, so it sits far below it.
Owner cash is 5.36% of what the business costs at the price (all-equity) and grows, on the filer's own organic record, at
about five percent; that does not reach ten.

---
## THE BOX
**OUT, at Q2** (the castle of the deciding part, Resilience, shown open on the filings: share is bought with money by
named rivals and by Arcadis itself, and the field's margins move in one band; the filer's own words, "an increasingly
commoditized market"). COMPUTATION beneath the stop: value range EUR 64.52 to EUR 107.66 against EUR 41.20, no case earning
the floor at the price (best 7.96% all-equity); fair price EUR 23.74 (all-equity), EUR 30.37 (equity-only). Integrity facts
recorded, not judged (the adjusted-figure and guidance habits, the move to an EBITDA margin target; under AFTER THE STOP,
Q4 and Q5).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2); "write it down in the first 30 minutes"
**[M1997-127]**.*

**Q3 (capital).** Operating EBITA 418M in 2025 against net working capital of 397M (AR2025 p.300); property, plant and
equipment 76M; capital spending 25M to 45M a year. Growth has come largely through purchases: 884.6M net over 2021 to 2025,
almost all IBI Group (799.6M cash, 2022, AR2023 p.174); goodwill and intangibles 1,473M at the end of 2025. What the IBI
price has returned was not computed (the IBI business is not reported separately).

**Q4 (the numbers).** (i) Adjusted figures featured: "Operating EBITA" excludes restructuring, integration, M&A and other
non-operating costs, which were 29M in 2024, **77M in 2025** (restructuring 53M, including in "other non-operating costs"
"€6 million related to wages tax on excessive remuneration") and 40M in H1 2026 (AR2025 p.299 as read in the iXBRL text;
H1 2026 press release); "Net income from operations" adds back the amortization of acquired intangibles (AR2025 p.197).
Restructuring recurs in every year read. (ii) **EBITDA in the filer's own mouth**: "Operating EBITDA will replace Operating
EBITA as the margin KPI from 1st January 2027", with the 2027 to 2029 target set as "Operating EBITDA margin: Mid- to
high-teens by 2029" (H1 2026 press release). The rows on that figure: "The one figure we regard as utter nonsense is the
so-called EBITDA" **[M1998-086]**. (iii) Guidance: the company guides each year ("Reaffirming 2026 full year operating EBITA
margin guidance of 11.7%-12.0%", H1 2026 press release); "the scourge of earnings "guidance"" **[L2019-006]**. (iv)
Year-end factoring: receivables of 34M sold non-recourse at the end of 2025 (AR2025 p.235); the remuneration committee
itself stripped the 19M "non-organic" cash out of the free-cash-flow bonus measure (AR2025 p.186). (v) Restatement of 2020
under IAS 8 after the IFRIC decision on cloud configuration costs: 54M of previously capitalized costs written off against
equity at 1 January 2020 (AR2021 p.214 to p.215). (vi) Two figures for one year: free cash flow 2023 is 220M in the 2023
report and the 2025 remuneration table (AR2025 p.191) but 190M in the 2025 five-year summary (AR2025 p.297); not resolved.
(vii) Auditor's key matter: contracts with a fixed-price element and the estimate of cost to complete (AR2024 p.324).

**Q5 (who runs it).** Chief executive Alan Brookes stepped down; Heather Polinsky, previously Global President for
Resilience and Mobility, became chief executive from 1 March 2026 (AR2025 p.8). Reported chief-executive pay EUR 4,538k in
2022 (+227% on 2021) and EUR 4,245k in 2023 (AR2023 p.165). 28 Speak Up reports in 2025, none involving substantiated
corruption or bribery (AR2025 p.150). On the 2019 ALEN loss the board wrote: "We have given the ALEN associate ample time
to create a return on the investments in clean energy assets" and "we are no longer willing to negatively impact our
financial performance" (AR2019 p.9). The habits recorded at Q4 (i) to (iii) are evidence on the people to be read at Q5 by
any later run, where "If you’ve got doubts, forget it." **[M2013-088]**.

**Q6 (the money and the owners).** Buybacks: 2,316,830 shares at EUR 27.58 to 40.24 in 2021, 810,000 at EUR 61.34 to 66.16
in 2024, 3,505,163 at EUR 35.11 to 50.86 in 2025 (average EUR 38.70), and 1,070,633 in H1 2026 for 41M (about EUR 38)
(AR2025 p.240; H1 2026 IFS note 17 and cash flow). The 2025 to 2026 programme was announced as "a maximum total value of
175 million" with no price above which it stops (AR2025 p.205). The line Q6 would need from Q7: the bottom of the
computed range is EUR 64.52, built at the 3.67% sovereign; the 2021, 2025 and 2026 prices paid sit below it and the 2024
prices straddle it; at those prices the owner cash still yields under the ten-percent floor (above). Dividend policy: 30% to
40% of net income from operations (AR2025 p.301). Control devices: priority shares held by a foundation whose consent is
needed for share issuance, charter changes and large investments, and a call option for a protective-preference foundation
over up to as many shares as are outstanding (AR2025 p.239); the employee Lovinklaan Foundation held 16,979,844 shares at
the end of 2025, about a fifth of the outstanding shares (same page). No all-stock deal in the span.

**Q9 (could it ruin us).** Net debt (leases excluded) 813M at 30 June 2026, 556M at 31 December 2025; the company's covenant
measure, net debt to EBITDA, 1.5 at the end of 2025 (AR2025 p.297). Senior unsecured notes 800M at 4.0% to 4.9%, including a
300M five-year bond issued May 2026 at 4.00%; RCF 600M undrawn at 30 June 2026; Schuldschein 278M, of which 225M repaid 20
July 2026 (H1 2026 IFS notes 20 and 24). Guarantees 254M; litigation provisions 43M; "claimants allegedly claim amounts
for project contract breaches that are significant to the Consolidated financial statements" (AR2025 p.262).

**Q12.** None of the named businesses applies.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `4cbb1228`); written question by question; committed after Step 0
      to Q1 and after Q2, and with the computation and audit.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present at start
      and is the dispatcher's; the fold is the dispatcher's (operator rule ten). This run binds nothing until folded.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the accidental sightings are
      declared under Contamination and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (check script `scripts/check_ids.py`, output `check_ids_output.txt`);
      no E-id; every filing fact has its document and page; numbers carry a filing or are labelled.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (leases, stock pay, capital spending, working capital), never a net-income proxy;
      the sovereign from the issuing authority (ECB), dated; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (Foundations, Q1, and the evidence for the castle in Q2); facts for later
      questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; rows of any date may be cited.
- [x] `tools/run.py` and `cover_shares.py` produced no lines for this name; all arithmetic is by hand from the filings.
- [x] `python tools/check_framework.py` PASS before the final commit (see the commit message).
- Honest limits: the principal-risks table could not be read (image); the 2022 annual report was not found and its year is
  taken from the 2023 report's comparatives; the rivals' figures are XBRL transcription not checked against their filed
  documents; Tetra Tech and NV5 were not read; no scuttlebutt.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2's "ordinary returns" names no capital base.** The section C convention closes OUT a field whose durable players earn
ordinary returns, but "Goodwill should not be used in evaluating the fundamental attractiveness of a business"
**[M2011-060]**, which tells the analyst to judge a business's attractiveness on tangible assets and to leave
goodwill out. In consulting engineering the two bases give opposite answers (very high on tangible capital, about ten
percent on equity that is mostly goodwill). This run did not rest the OUT on the ordinary-returns item; it rested it on the
money test and the copying items, and recorded the tangible return as a weighing FOR at Q3. The text should say which base
"ordinary" is judged on, or say that a high tangible return earned by every entrant is not a castle. (2) **The sovereign
for a euro reporter that earns two thirds of its net revenue in dollars, sterling and Canadian dollars.** The protocol says
"the earnings currency" and the table offers one rate per currency; the run used the euro (3.67%) as the reporting and
paying currency, but the US 30-year was 5.43% the same day and the value range moves a great deal with that choice. A
blended or largest-currency rule is not written. (3) **Net debt at the latest filed date when that date is a half-year with
a seasonal working-capital build** (813M at 30 June against 556M at 31 December; the difference is EUR 3.02 a share on every
all-equity figure). Followed as written; the text could say whether a seasonal half-year is the right date. (4) **The range
at the sovereign and the floor at ten percent pull apart**: here the range (EUR 64.52 to EUR 107.66) sits far above the
price while no case earns the floor, and Q6's buyback test reads prices paid against the bottom of that range, so a
buyback "below the bottom of the range" can still be a purchase at less than the floor. (5) **The serial-acquirer
convention fires on one large deal** (IBI was 90% of the window's purchases); the organic pair then credits the base that
IBI's cash bought without charging its price. Applied as written, with the default pair beside. (6) **The parts table's
"five-year operating profit"** met a segment structure that changed twice (geographic segments in 2021, four GBAs in 2022 to
2025, three from 2026); the share was taken over four years, and the choice between the company's segment profit measure
(operating EBITA) and segment operating income decides whether Resilience passes half; it decides either way here, but the
text names no measure. (7) No rule covers a principal-risks section published only as an image; recorded as unreadable.
