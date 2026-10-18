# Company Run — NOV Inc. (NYSE: NOV) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
NOV or National Oilwell).*

**Dispatch.** A dispatched blind purchase run, brief written by the unattended overnight cycle
(`Screens/_daily/_overnight_prompt.md`). The brief's one stated departure from the canonical brief: the lines of evidence
are derived by the analyst from the 10-K's Item 1, Item 1A and Item 7, and the competitors are the rivals the 10-K itself
names (up to three that file with the SEC). Both are stated below where they are used.

**Contamination, declared and not used.** (1) The session's opening git status showed the last commit subjects in the
repository, among them a fold of another company's run (FET, Forum Energy Technologies) whose subject line says that
company's operating margin 2015 to 2025 was "lowest against NOV, SLB and Tenaris". That is a fact about another company's
run, seen before any reading here; it was not opened and is not used. The competitor set below was chosen from NOV's own
10-K, not from that line (Tenaris is not among the rivals NOV's 10-K names). (2) The memory index loaded with the session
carries one-line notes on the queue state and on other names; none concerns NOV, and none was opened. No blind-listed file
was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $18.64 (close 2026-10-15; `tools/run.py` live quote, an **aggregator, flagged** per operator rule 5; used
  for the quote only).
- **Shares by class** from the latest filing's cover: **356,478,125** common, par $0.01, one class (10-Q for the period
  ended 2026-06-30, filed 2026-07-29, accession `0001193125-26-322979`; `python Screens/cover_shares.py NOV`). Cross-check:
  the same 10-Q's balance sheet shows 357,299,308 shares issued and outstanding at 2026-06-30 (repurchased shares are
  "constructively retired and returned to an unissued state", so there is no treasury line); the cover count is lower by
  the buyback continuing after quarter end (3.2 million shares bought in the second quarter, same 10-Q). No 8-K after the
  10-Q reports an issue or a split (EDGAR filing list read 2026-10-16: the last 8-K is the 2026-07-29 earnings release).
  `tools/run.py` used the older 2026-04-24 cover (358.9M); the 10-Q cover governs.
- **Market cap:** $18.64 x 356.478M = **$6,645M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-12, accession `0001193125-26-048350` (Items 1, 1A,
  7, Note 12 litigation, Note 16 segments); 10-Q for the quarter ended 2026-06-30, filed 2026-07-29, accession
  `0001193125-26-322979` (balance sheet, debt, repurchases, royalty litigation); proxy DEF 14A filed 2026-04-09,
  accession `0001193125-26-148884` (read only so far as the closing STOP required; see AFTER THE STOP); 8-Ks of
  2025-11-20 (`0001193125-25-288885`, CEO succession), 2026-02-20 (`0001193125-26-060618`, a director's resignation),
  2026-03-18 (`0001193125-26-113299`, a director appointed), 2026-04-15 (`0001193125-26-156143`, first-quarter
  operational update), 2026-05-22 (`0001193125-26-236271`, dividends) and 2026-07-29 (`0001193125-26-322315`, second
  quarter results). Ten years of balance sheets and eighteen years of income and cash-flow lines from the first-filed XBRL
  of each 10-K (accessions listed in `Test Runs/_research 2026-10-16 NOV/run_py_output.txt` and in the research scripts).
  **One figure cross-checked against the filed statement:** cash and cash equivalents $1,552M and total debt $1,718M at
  2025-12-31, as stated in the 10-K's MD&A liquidity paragraph (`0001193125-26-048350`), equal the XBRL balance-sheet
  values `tools/run.py` printed; operating cash flow $1,251M (XBRL) equals the MD&A's "$1.25 billion".
- `python tools/run.py NOV` arithmetic lines only (the full print is `Test Runs/_research 2026-10-16 NOV/run_py_output.txt`;
  nothing it prints as a rule, an id or a verdict is used, Part VII). Operating cash less stock pay less capital spending:
  2023 **-$206M**, 2024 **$883M**, 2025 **$809M**; the five-year window 2021 to 2025 averages **$208M** on the capital
  spending basis and $171M on the depreciation basis. Stock pay resolved: $66M, $70M, $67M (2023 to 2025; one tag, no
  other stock-pay lines found). Finance-lease principal (not in capital spending): $23M, $28M, $28M. Depreciation and
  amortization $303M, $343M, $355M against capital spending $283M, $351M, $375M.
- **The balance sheets, 2016 to 2025, read here because the file closes before Q4** (the brief's instruction; `tools/run.py`
  ten-year table from the first-filed XBRL of each 10-K, accessions in `run_py_output.txt`; the 2025 column checked
  against the 10-K's MD&A). What moved, and why:
  - *Equity against goodwill and intangibles.* Equity fell from $13,940M (2016) to $6,268M (2025). Goodwill plus
    intangibles fell from $9,597M to $2,037M over the same years. The fall in equity is almost wholly the write-off of
    purchased goodwill and intangibles (goodwill impairments of $1,485M in 2015, $972M in 2016, $3,509M in 2019, $1,295M
    in 2020 and $40M in 2025; a long-lived and intangible impairment of $2,209M in 2019; XBRL). Retained earnings went
    from $7,285M to negative in 2020 and stand at -$673M. What the figures say: most of the capital paid for acquisitions
    in 2008 to 2014 ($10.7 billion of acquisition cash in those seven years, XBRL) was written off within six years.
  - *Receivables and inventory against sales.* Receivables $2,083M on sales of $7,251M in 2016 (29%), $1,701M on $8,744M
    in 2025 (19%); inventory $3,325M (46% of sales) to $1,799M (21%). Working capital is far leaner than in the bust; the
    10-K reports inventory reserves of $261M, 12.7% of gross inventory, at 2025-12-31 (Item 7).
  - *Cash and debt.* Cash $1,408M to $1,552M; long-term debt $2,708M to $1,688M (two senior note issues, 3.95% and 3.60%,
    plus $129M other debt at 2025-12-31; Item 7). Long-term lease liabilities $521M (Item 7), not in the debt line.
  - *What they do not say.* The $140M of royalty receivables in "Other assets" depend on an appeal NOV lost at trial
    (10-Q, `0001193125-26-322979`); the $888M of the $1,552M of cash held abroad could bear tax on repatriation (Item 7).
    Nothing in the ten balance sheets suggests a game played with the accounts: the movements are explained by the
    write-offs, the bust and the recovery, each disclosed.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what NOV's businesses will earn over a decade, not where the quote
goes after a 2026 in which management speaks of a "synchronized global recovery" (8-K of 2026-07-29). The market serves
and does not instruct **[M2006-077]**: the price of $18.64 against a 2014 peak operating profit of $3.6 billion tells
nothing by itself. No macro enters **[M2000-094]**: the oil price, OPEC+ and the Middle East war that cut the first
quarter of 2026 (8-K of 2026-04-15) are not forecast here; what counts is "the average profitability of the business over
time and how strong its competitive mode is" **[M2015-016]**. Who is paid to tell you: the competitive-strength section of
Item 1 and the earnings releases are the company's own advocacy, and are read against its own figures. **Contrary evidence,
written down as found** **[M1997-127]**: (1) the 10-K's own competition risk factor: "Certain of these competitors may have
greater financial, technical, manufacturing and marketing resources than us, and may be in a better competitive
position"; (2) Item 1: "competitive products with different designs have been successfully developed and marketed by
others"; (3) the leaching-patent royalties: every drill-bit licensee stopped paying, and the district court ruled in
2025 that NOV cannot collect after each stopped (10-K Note 12; 10-Q); (4) operating profit of $3.6 billion in 2014
became seven years of losses, 2015 to 2021, with $7.3 billion of goodwill written off (XBRL, 10-Ks 2015 to 2020);
(5) 2025: segment margin in Energy Products and Services fell from 11.5% to 7.0% on "tariffs and other inflationary
pressures" while the segment gained share (10-K MD&A).

## THE STANDING RULE
Owning NOV puts the buyer at risk of ruin only through the buyer's own financing and sizing: an unlevered position sized so
that the 2015 to 2021 kind of fall cannot touch "what we have and need" **[M2012-081]**; borrowed money has no place in it
**[L2014-005]**. The target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (10-K Item 1, `0001193125-26-048350`). An independent maker and servicer of equipment for
  drilling, completion and production, in 57 countries, 66% of 2025 revenue outside the United States. Two segments:
  **Energy Equipment** (rigs and rig components, offshore drilling packages, pressure pumping and coiled tubing units,
  marine cranes and jacking systems, FPSO process systems and turret moorings, flexible subsea pipe; capital equipment
  from a backlog of $4.34 billion at 2025-12-31, plus aftermarket spares and service on a large installed base) and
  **Energy Products and Services** (drill bits, downhole motors and tools, drill pipe, completion tools, artificial lift,
  tubular inspection and coating, solids control, digital services; shorter-cycle, transactional). The product chemistry
  and engineering need not be understood; "What is important is that I understand the economic dynamics of the industry"
  **[M2011-014]**.
- **The key variables and how predictable they are** **[M1998-044]**. (1) The level of customer spending on wells and on
  offshore capital equipment, which the 10-K says depends "primarily upon the general level of activity in the oil and gas
  industry worldwide", "heavily influenced by ... oil and gas prices" (Item 1). Not predictable, and not to be forecast
  here: "We don’t think we can predict commodity prices." **[M2016-025]**. (2) NOV's share and its margin against the
  rivals over the cycle, readable from its own and the rivals' filings. (3) The installed base and its aftermarket,
  which the 10-K names as a source of repeat revenue (Item 1, "Large installed base of equipment").
- **Routing.** The dependence here is on a commodity price at one remove, through customers' budgets. The framework's
  commodity paragraph (Q2) sends that dependence away from Q1: in the framework's own words it is never by itself a STOP
  at Q1 or Q2. The business is bought or refused "off the figures" **[M2008-069]**; Q2 asks the cost and competitive
  position from the filings, and the price level enters at Q7 as the cycle base. Fast technological change does not close
  it here: the core products (drill pipe, bits, motors, rig machinery, flexible pipe) are long-lived lines; the digital and
  robotics offers are additions to them, not a field whose winners cannot be named **[M2012-067]**. Not a bank, not a
  holding company; two operating segments, read at Q2 as parts.
- **Where it will be in ten years** **[M2000-037]**, **[M2012-065]**. What can be said from the figures: the same
  equipment and consumables, sold into the same cyclical field, with revenue between roughly $5.5 billion (2021) and
  $9 billion (2023 to 2025) in the current shape, and the competitive position a matter for Q2. What cannot be said is the
  level of the field's spending in any given year; the framework places that at Q7, not here. The doubt that remains is
  written down **[M2002-092]**: the 10-K's own risk factor on laws, regulation and "societal perceptions of our industry"
  that may reduce demand for oil and gas over the energy transition (Item 1A). It is a threat to the castle's future, which
  Q2 test 11 asks **[M2000-014]**, not a failure to understand what the business is or how it earns.
- **VERDICT: IN.** The economics can be read off eighteen years of filings **[M2008-069]**; the unforecastable part is
  the commodity-driven activity level, which the framework routes to Q2 and Q7, not a reason to close here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, derived from the 10-K as the brief requires** (`0001193125-26-048350`): from Item 1, the claimed
advantages (scale in procurement and manufacturing, distribution, fleet standardization, the large installed base and its
OEM aftermarket, proprietary technology, a "capital-light" model) and the Markets and Competition paragraph; from Item 1A,
the competition risk factor, the fixed-price contract risk factor and the equipment-contract (backlog) risk factor; from
Item 7, the segment results and margins for 2025 against 2024, the backlog and book-to-bill, the inventory-obsolescence
paragraph, and the drill-bit royalty litigation it points to (Note 12). The castle question is put to these and to
eighteen years of the filer's own figures **[M1995-038]**.

**The competitor set.** Item 1 names no rival ("publicly traded oilfield service and equipment companies and smaller
independent equipment manufacturers"); Item 1A names none either. The only rivals the 10-K names are the drill-bit
makers in Note 12's royalty litigation: Schlumberger, Halliburton, Baker Hughes, Ulterra, Varel and Taurex. The three that
file with the SEC are used: **SLB** (CIK 87347), **Halliburton** (CIK 45012), **Baker Hughes** (CIK 808362 to 2016,
then CIK 1701605). **Flagged, not filers:** Ulterra and Taurex (no EDGAR registrant found by company search, 2026-10-16);
Varel (one inactive EDGAR entity, last filing dated 2007-11-14, no periodic reports). The three filers are far larger
service companies, rivals of NOV in drill bits and some downhole and completion lines, and customers of its Energy
Equipment segment; the 10-K itself names that double role in its strategy ("Capitalize on and drive end-market
fragmentation", Item 1). The comparison is therefore of the field the 10-K names, not of like-for-like equipment makers,
and is read that way.

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent.* The 10-K's own answer is scale, standardization and the installed base:
   "Most service companies prefer, and many of their customers demand, OEM aftermarket support" (Item 1). That is a real
   reason a customer returns. It did not hold the returns through the cycle (the field table below), and in 2025 the
   Energy Equipment segment reported "lower demand for aftermarket spare parts and services" (Item 7).
2. *Would it stand without the lord.* Not tested further; the deciding facts are elsewhere.
3. *The money test* **[M2011-015]**. The 10-K: "Certain of these competitors may have greater financial, technical,
   manufacturing and marketing resources than us, and may be in a better competitive position" (Item 1A), and local-content
   policies are expected to "prompt more local startup enterprises" (Item 1). Attackers with money exist and are named by
   the filer as possibly better placed.
4. *Pricing power and the agony before a rise* **[M2005-020]**. Strong positions "manage to pass through increases in raw
   material costs" over time **[M2005-017]**. In 2025 Energy Products and Services gained share and its operating margin
   still fell from 11.5% to 7.0%, "due to a less favorable sales mix, tariffs and other inflationary pressures" (Item 7);
   the Item 1A fixed-price risk factor says NOV sometimes takes multi-year contracts "without sufficiently protective
   price escalation clauses", some "required by our customers, including national oil companies", which "often possess
   substantial leverage". Against that, Item 1: surcharges have "generally" mitigated raw-material costs. Weighs against.
5. *Unit volume and share of mind.* Revenue was $21.4 billion in 2014 and $5.5 billion in 2021, $8.7 billion in 2025
   (XBRL; the 2014 figure includes the distribution business spun off that year). The volume is the customers' capital
   budget, not a place in anyone's mind.
6. *The low-cost position* **[M1997-010]**. Measured "more by cost of production" **[M2006-004]**, read from the filings: the
   proxy for cost against rivals is the margin over the same years from the same kind of figure: NOV's pre-tax,
   pre-interest margin was the lowest of the four in 2015 to 2025 and below SLB's and Halliburton's in 2008 to 2025
   (field table). "It’s like comparing a copper producer whose costs are $2.50 a pound with a copper producer whose costs
   are $1 a pound." **[M2009-059]**. Weighs against.
7. *The brand.* Brands are named (TDS top drive, NOVOS, Tuboscope, Bondstrand); the 10-K itself rates its intellectual
   property no higher than "quality and timely delivery", service and skills, and concedes "competitive products with
   different designs have been successfully developed and marketed by others" (Item 1).
8. *The low bid.* Fixed-price engineered packages for national oil companies on the customers' terms (Item 1A) are the
   low-bid end of the business. Not decided alone.
9. *Ask the competitors* **[M1999-130]**. Not on the public record; not asked.
10. *Widening or narrowing* **[M1999-108]**. Narrowing on the filer's own evidence: (a) the leaching-patent royalties:
    "all of the drill bit manufacturer licensees unilaterally stopped making royalty payments", and on 2025-09-29 and
    2025-10-07 the district court ruled "that NOV cannot collect royalties under the License Agreements after the date each
    licensee stopped making royalty payments" (10-K Note 12; 10-Q `0001193125-26-322979`, royalty receivables $140M net of
    $78M reserves, under appeal); (b) the 10-K's inventory paragraph speaks of "the obsolescence of certain older products
    in a dramatically-shifted and more highly-competitive recovering market" (Item 7, critical accounting estimates);
    (c) margins: 14% to 17% in 2012 to 2014, 4% to 10% in 2022 to 2025 on the recovery (field table).
11. *What could destroy, modify or reduce it* **[M2000-014]**. Item 1A names the energy transition's laws, regulation and
    "societal perceptions of our industry" as a risk to demand; the 2015 to 2021 record shows what a long fall in
    customer spending did to a business with these fixed costs. The rows' gypsum case: "there has been too much gypsum
    capacity" **[M2017-043]**; the rig-building years of 2008 to 2014 filled the field with rigs and the newbuild demand
    did not return in the decade after (Energy Equipment revenue now rests on offshore production and aftermarket, Item 7).

**The parts table** (10-K Note 16, `0001193125-26-048350`; the segment table in the two-segment form covers 2023 to 2025
only; no earlier segment figures in this form were found in the filings read, so the share is of three years, not five,
and is said so).

| part | operating profit 2023 / 2024 / 2025 ($M) | share of the three years | castle | decides |
|---|---|---|---|---|
| Energy Equipment | 371 / 608 (includes a $130M gain on the Pole Products sale) / 493 | 53.9% (51.6% without the gain) | installed base and aftermarket; capital equipment from backlog; margin 7.9%, 12.4% (9.8% without the gain), 10.0% | **yes**, more than half on either reading |
| Energy Products and Services | 507 / 475 / 277 | 46.1% | consumables, rentals and services; drill-bit IP eroding (Note 12); margin 12.4%, 11.5%, 7.0% | no, but near half, and read |

Both parts are near half, so both castles were read; the box is the same on either, because the field-return evidence
below is of the whole company and the two parts' margins in 2023 to 2025 are alike. "lumping them together, as is done in
standard financial statements, impedes analysis" **[L2008-005]**; the two segments here have similar margins and the same
customers, so the lumping costs little in this case.

**The field's returns over the last full cycle** (from the filer's and the rivals' own filings; first-filed XBRL values of
each 10-K; figures in `Test Runs/_research 2026-10-16 NOV/q2_field_table.txt` and `q2_tangible.txt`). The cycle, on the
filer's own figures: operating profit peaked at $3,613M in 2014, fell to losses in every year 2015 to 2021 but 2018, and
recovered to $876M in 2024, the highest since 2014; 2025 fell to $494M and the first quarter of 2026 to an operating
profit of $47M on the filer's preliminary figure (8-K of 2026-04-15). The last full cycle is read as 2014 to 2024, peak to
peak.

| measure (pre-tax income plus interest expense, as filed) | NOV | SLB | Halliburton | Baker Hughes |
|---|---|---|---|---|
| margin on revenue, 2008 to 2014 | 17.8% | 18.9% | 14.6% | 11.4% |
| margin on revenue, 2015 to 2025 | **-10.9%** | 2.5% | 0.6% | -1.6% |
| margin on revenue, 2008 to 2025 | 5.2% | 9.5% | 6.6% | 2.9% |
| on book capital (equity plus debt), 2015 to 2025 | **-8.0%** | 2.0% | 0.6% | -1.5% |
| on book capital, 2008 to 2025 | 4.2% | 8.4% | 7.8% | 2.8% |
| margin on revenue, 2022 / 2023 / 2024 / 2025 | 4.4 / 8.2 / 10.4 / 5.3% | 16.9 / 17.5 / 17.0 / 13.6% | 10.4 / 14.6 / 14.1 / 8.0% | 0.2 / 10.4 / 11.7 / 10.4% |

These are all-in figures: each company's own impairments are inside its own numbers, so the comparison is like for like
in method. Transcription cautions: Halliburton's 2008 and 2009 interest tags carry a negative sign and its 2010 to 2017
interest is untagged in the series used (margins there are pre-tax only, slightly understated); NOV's 2008 to 2011 and
Halliburton's 2008 figures are operating income as filed, where the pre-tax line was not tagged; Baker Hughes' 2015 and
2016 pre-tax lines in the old CIK's XBRL disagree with its operating income lines; none changes the order of the 2015 to
2025 row.

**The most favourable reading for NOV, tested.** Goodwill is left out when judging the business, "look at return on
tangible assets", and put back when judging the capital allocation, "because we paid for it" **[M2011-060]**. On tangible
capital (equity plus debt less cash, goodwill and intangibles) and with **every** goodwill, intangible and long-lived
impairment added back, NOV earned pre-tax: **6.8%** a year over the peak-to-peak span 2014 to 2024 (0.4% for 2015 to 2024,
without the first peak year); **15.3%** over the recovery 2022 to 2025; and in the 2012 to 2014 boom 41% to 50%
(`q2_tangible.txt`). On the capital actually paid for the business, goodwill included, the 2008 to 2025 figure is 4.2%
pre-tax and 2015 to 2025 is negative (table). The castle "protects excellent returns on invested capital" **[L2007-004]**;
over the last full cycle this one protected ordinary returns at best, on the most favourable measure, and below-ordinary
returns on the capital paid in. The boom returns of 2008 to 2014 are not the norm the cycle shows: they rested on a
customers' building spree that ended, and a change for the better since 2021 is not credited before a full cycle shows it
(the framework's Q2, Change, section C convention); the recovery margins of 2022 to 2025 (4% to 10%) are well below the
boom's and below SLB's and Halliburton's in the same years.

**The judgment, in words** (the framework's convention on ordinary returns carries no figure; the figures above are the filings', the word is
mine). The field the 10-K names, NOV and the three filers among its named rivals, earned ordinary to poor returns over the
last full cycle on the capital put into it, and NOV the poorest margins of the four from 2015 to 2025. "you can have only
two competitors and they’re still terrible businesses" **[M2013-052]**: a field of large, durable players can still earn
ordinary returns. NOV's castle stands (it survived the bust with an investment-grade balance sheet and a $4 billion
backlog), but what it protects is not an excellent return: it is the standing castle that protects only ordinary returns,
which the framework sends to OUT, not TOO HARD, because the returns are known from the filings and not a matter of
"We don’t know how to valuate that" **[M2000-019]**. The low-cost test (test 6) and the narrowing evidence (test 10) point
the same way; nothing in the filings read points the other way except the boom years and the installed base, both weighed
above. Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**.

- **VERDICT: OUT.** The standing castle that protects only ordinary returns over the last full cycle (2014 to 2024),
  on the filer's and its named rivals' own filings **[L2007-004]**, **[M2013-052]**, **[M2011-060]**; not the low-cost
  producer against the rivals it names **[M1997-010]**, **[M2009-059]**; the moat narrowing on the filer's own evidence
  **[M1999-108]**. Q3 to Q12 are NOT REACHED; what follows them is facts and computation only.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2). Facts under AFTER THE STOP.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. The balance sheets were read in Step 0 and the facts are under AFTER THE STOP.
## Q5 — WHO RUNS IT. NOT REACHED. Facts under AFTER THE STOP.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED. Facts under AFTER THE STOP.
## Q7 — WHAT IS IT WORTH. NOT REACHED. The owner's two reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED. Facts under AFTER THE STOP.
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## THE BOX
**OUT at Q2**: the standing castle that protects only ordinary returns; over the last full cycle (2014 to 2024) NOV earned
6.8% a year pre-tax on tangible capital even with every impairment added back, below-ordinary returns on the capital paid
in, and the poorest margins of the four companies its 10-K names in 2015 to 2025; the drill-bit royalties are lost at trial;
not the low-cost producer against those rivals. Integrity facts recorded, not judged (adjusted EBITDA featured in
releases and as the annual-bonus measure; quarterly guidance, missed and pre-announced in April 2026). COMPUTATION beneath
the stop: value $5.19 to $11.06 a share all-equity against $18.64; fair price $3.92 all-equity, $4.24 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down **[M1997-127]**, not weighed; no verdict; the box is unchanged (operator rule 2).*

**Bearing on Q3 (capital).**
- Capital spending was below depreciation across the cycle: $2,681M of capital spending against $3,194M of depreciation
  in 2015 to 2024; 2025 capital spending $375M against depreciation $300M and depreciation plus amortization $355M (XBRL).
  The 10-K calls the model "capital-light" and says its facilities "require relatively low investment and maintenance
  expenses versus the sales they enable" (Item 1). The filing states no maintenance figure.
- Tangible capital about $4.4 billion at 2025-12-31 against revenue of $8.7 billion; pre-tax earnings before interest on
  it, impairments added back, 21.7% in 2024 and 12.1% in 2025 (`q2_tangible.txt`).
- What purchases returned: $10.7 billion of acquisition cash in 2008 to 2014; $7.3 billion of goodwill and about
  $2.2 billion of intangibles written off in 2015 to 2020 (XBRL); the acquisitions earned far less than their price on
  the filer's own impairment testing.

**Bearing on Q4 (the accounts).**
- The filer features "Adjusted Operating Profit" and "Adjusted EBITDA" (operating profit before depreciation,
  amortization, gains on asset sales and "pre-tax Other Items") in the 10-K's MD&A and every earnings release read. The
  "Other Items" recur every year read: $59M in Energy Products and Services, $79M in Energy Equipment and $45M at corporate
  in 2025; a net credit in 2024 (the $130M Pole Products gain); $17M in the second quarter of 2026 (10-K Item 7; 8-K of
  2026-07-29). The second-quarter 2026 adjusted figures include "a benefit of approximately $40 million related to tariff
  refunds".
- Effective tax rate 59.7% in 2025 on valuation allowances for foreign tax credit carryforwards (allowance up from $266M
  to $352M); a $373M tax benefit in 2023 from releasing valuation allowances (10-K Item 7; XBRL). Cash taxes paid $106M in
  2025 (XBRL).
- Equity income from the largest unconsolidated affiliate (an oil country tubular goods business) fell from $119M (2023)
  to -$16M (2025) (Note 16; Item 7).
- No restatement box is checked on the 10-K cover; the word sweep (material weakness, restatement, investigation,
  subpoena, FCPA) of the 10-K and the 10-Q found only risk-factor language and the auditor's standard wording.

**Bearing on Q5 (the people): integrity facts recorded, not judged.**
- The company gives quarterly guidance ("Adjusted EBITDA expected to be between $240 million and $270 million" for the
  third quarter of 2026, 8-K of 2026-07-29) and pre-announced a first-quarter 2026 miss against "prior guidance",
  attributing it to the Middle East war (8-K of 2026-04-15). Reported, not weighed.
- The adjusted figure is featured in place of GAAP in releases and is the annual bonus measure (proxy, below).
- Succession: Clay Williams retired; Jose Bayardo (with NOV since 2015 as CFO, then President and COO) became Chairman,
  President and CEO on 2026-01-01; William Thomas is Lead Independent Director (8-K of 2025-11-20). One director resigned
  on 2026-02-19 "not the result of any dispute or disagreement" (8-K of 2026-02-20); one was appointed on 2026-03-17
  (8-K of 2026-03-18).
- The Russian business: an agreement to sell it was signed in the third quarter of 2022 and "remains subject to various
  government approvals"; the Russian subsidiaries were deconsolidated in 2025 (10-K Items 1A and 7).

**Bearing on Q6 (the money and the owners).**
- Repurchases: $779M in 2014 and $2,221M in 2015 (XBRL), the second in the year the bust began and before the $7.3
  billion of goodwill write-offs; none in 2016 to 2023; $229M (14.2M shares, about $16.13 a share) in 2024, $315M
  (22.8M shares, about $13.82) in 2025, $130M (6.7M shares, about $19.40) in the first half of 2026 (10-K Item 7; 10-Q).
  The programme is "up to $1 billion ... over a period of 36 months" and names no price; the stated policy is to return
  "at least 50% of Excess Free Cash Flow" through dividends, buybacks and a supplemental dividend (10-K Item 7; 10-Q).
  Against the computation below, every average price paid in 2024 to 2026 sits above the top of the computed range
  ($11.06); this is a computation beneath a stop, recorded, not a Q6 finding.
- Dividends: $0.09 a quarter plus a $0.09 supplemental (8-K of 2026-05-22); $190M paid in 2025 (XBRL).
- Pay (proxy, `0001193125-26-148884`): the annual incentive is "primarily designed to incentivize near term-generation
  of Adjusted EBITDA", with a working-capital modifier and safety measures; it paid below target for 2025. Long-term
  awards are stock options, restricted stock and performance shares, the performance shares 85% on total shareholder
  return relative to the PHLX Oil Service Sector Index and 15% on an internal returns measure (NVA); the 2023 award paid
  86.02% of target; "all previously granted stock options were underwater other than those granted during 2021 and
  2025". The compensation consultant is Meridian Compensation Partners.

**Bearing on Q9 (debt and exposures).**
- Total debt $1,706M and cash $1,164M at 2026-06-30; the $1.5 billion revolver is undrawn to 2030-09-12, with a 60%
  debt-to-capitalization covenant against 23.9% actual (10-Q). Letters of credit of $909M outstanding (bid, advance
  payment and performance bonds). Multi-year fixed-price contracts with liquidated-damages exposure (Item 1A). Insurance
  "subject to coverage limits" for environmental and product liability (Item 1A). Investment-grade rating stated in
  Item 1.

**Bearing on Q12.** Equipment for oil and gas, geothermal, offshore wind and industrial markets; none of the businesses
the framework names.

## COMPUTATION, NOT A CLEARANCE
*Q7 is NOT REACHED. Everything in this section is arithmetic beneath the Q2 STOP, for the owner's two reporting figures
(Part VII, The owner's price); it carries no entry language and no verdict (operator rule 3). Script and full output:
`Test Runs/_research 2026-10-16 NOV/q7_computation.py` and `q7_computation.txt`.*

**Owner cash** after every real cost: operating cash flow less stock pay ($66M to $130M a year; a cost, "all forms of compensation" **[L2021-003]**), less all capital spending, less finance-lease principal, less acquisition cash net of businesses sold
(the default pair), each year from the first-filed XBRL. Not a net-income proxy (operator rule 5). The all-equity basis
adds back net interest paid (interest paid less interest income) after a 21% tax shield; **CONVENTION of this run**:
the shield at the US federal statutory rate, because the company's effective rate swings from a benefit (2023) to 59.7%
(2025) and the framework names no rate for the add-back. "they get credit for whatever net cash is left every year"
**[M1998-080]**; "are you going to have to put more cash into after you buy it?" **[M2014-068]**.

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| owner cash, all-equity, acquisitions deducted ($M) | 754 | 407 | 481 | -70 | 190 | 610 | -13 | -489 | -206 | 771 | 808 |

**The six specifics, applied.**
- *(a) Cycles.* The literal window 2021 to 2025 runs from the trough (2021 revenue $5.5 billion, the lowest of the
  eighteen years read; 2022 and 2023 negative owner cash as working capital was rebuilt) to the recovery, so its first
  years are aberrational **[L2005-003]**; the base is the last full cycle on the owner-cash series, peak 2014 to peak
  2024, averaged over 2015 to 2024: **$243.6M** all-equity ($189.8M equity-only). The literal window is shown beside:
  $174.2M. *Departure, confessed:* the filer's own description of 2021 and 2022 (the FY2021 and FY2022 10-Ks) was not
  read; the cycle is read off the filed figures.
- *(b) Decline.* Growth between the averages of successive cycles: on the default pair the prior cycle (2008 to 2014)
  averages only $26.6M after its $10.7 billion of purchases, so the default rate (+29.8% a year) is an artefact of the
  purchases; on the organic pair owner cash fell from $1,561M to $356M (-16.0% a year); sales fell from $16.8 billion to
  $7.9 billion a year on average (-8.0% a year; the prior cycle's sales include the distribution business spun off in
  2014, which overstates the fall). A decline is carried as the bottom; the no-growth case is the top.
- *(c) Acquisitions.* Deducted net of divestitures, total growth credited (default pair, central); organic pair beside.
  Net purchases were 37% of owner cash before purchases in 2015 to 2024, under the serial-acquirer half (the 2008 to 2014
  cycle was 99%). No merger in the window. No signed, unclosed acquisition; the Russian sale signed in 2022 and still
  awaiting approvals is a small divestiture of a business already deconsolidated, not valued. Rigsmart and Cranesmart,
  bought in the second quarter of 2026 (8-K of 2026-07-29), are credited at nothing (no price or earnings found).
- *(d) Working capital.* Counted, inside operating cash flow, as the filer reports it; no single year's draw is tied by
  the filer to one contract.
- *(e) Growth spending.* The filing states no maintenance figure; capital spending ran below depreciation over the cycle,
  so the all-spending case is central and the depreciation basis is shown beside ($192.3M).
- *(f) The cap.* The default-pair rate carried ten years would need owner cash of 40% of sales against a highest filed
  share of 14.0% (2009); cut to the business's own sales growth between the cycles, -8.0% a year, which is below the
  discount rate **[M1997-095]**, **[M1999-067]**.
- Rate 5.43% (US Treasury 30-year, 2026-10-15); ten years, then zero nominal growth; net debt $542M at 2026-06-30
  (debt $1,706M less cash $1,164M; operating lease liabilities, $521M at 2025-12-31, left out, said so; the 10-Q states
  no subsequent events changing it); 356.478M shares.

**The floor, tested first.** Expected return at the price (no-growth cash against an enterprise value of $7,187M): cycle
base **3.4%**; cycle base before acquisitions 4.9%; literal window 2.4%. No case of the range earns about ten percent
(the floor CONVENTION, **[M2003-149]**), so Q7, had it been reached, would close OUT whatever the width. Shown for the
evidence for, and not a case of the range: the 2024 and 2025 average ($789M) would yield 11.0% at the price; it is the
recovery's two best years, not a cycle **[L2005-003]**.

**(a) THE VALUE RANGE (COMPUTATION):** **$5.19 to $11.06 a share**, all-equity central (whole-business $2,391M to $4,486M
less net debt), against **$18.64**; width 1.9 to 1. The price is above the top. Equity-only beside: $5.23 to $9.81.
Beside, not central: organic pair $3.89 to $16.86; literal window, no growth, $7.48; depreciation basis, no growth, $8.41.

**(b) THE FAIR PRICE (COMPUTATION; a reporting figure, never a verdict):** **$3.92 a share** on the all-equity basis
(each end valued at ten percent: $2,436M at no growth, $1,445M on the decline; averaged, less net debt $542M, over 356.478M
shares), after the company's own tax; **$4.24** on the equity-only basis beside it. No other price figure is reported.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `ffffedb4`); written question by question; committed after Step 0
      to Q1, after Q2, and after the close (write-early).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present and held
      by the dispatcher, not touched. Folding into the register is the dispatcher's (operator rule ten); a run not in the
      register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. The commit subject seen at
      session start (another company's run naming NOV as a comparator) is declared under contamination and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the script in the research folder
      (`check_citations.py`); every filing fact has its accession; every number has a filing or is labelled
      COMPUTATION or CONVENTION.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the figures beneath are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal, acquisitions), never a
      net-income proxy; the sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its share count was replaced by the later 10-Q cover.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the closing commit message).
- Honest gaps: the FY2021 and FY2022 10-Ks were not read (the cycle base rests on filed figures, not the filer's words
  about those years); the five-year parts split could not be made (the two-segment form is filed for three years only);
  the rival figures are XBRL transcriptions with the tag cautions stated under Q2; the competitors' own 10-K text was not
  read, only their filed figures; the proxy was read only for pay design.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Which capital ordinary returns are judged on.** Q2's convention sends a field whose durable players earn ordinary
returns over a full cycle to OUT, and Q3 says the business is judged on tangible assets with goodwill left out
**[M2011-060]**, while the capital allocation is judged with it. For a company whose bust years are dominated by writing
off purchased goodwill, the two measures give very different pictures (2008 to 2025: about 4% pre-tax on book capital,
far higher on tangible capital ex-impairments because of the boom). I judged on both and on the peak-to-peak span,
and the box was the same; a sentence saying which capital, and whether impairments are added back, would stop two
analysts splitting. (2) **The full cycle for a long-cycle business.** "The last full cycle" is not defined where the
cycle runs a decade and the boom before it was a once-in-a-generation build-out; whether 2008 to 2014 or 2015 to 2024 is
"the" cycle decides the box. I used peak to peak on the filer's own operating-profit series and said so. (3) **The
cycle-base specific (a) asks for "the filer's own description" of an aberrational year**, which requires the 10-K of
that year; for a window starting five years back, that means reading two or three older 10-Ks that the rest of the run
does not need. I read the figures instead and confessed it. (4) **The brief's competitor rule** ("the rivals the 10-K
itself names") gave only the drill-bit licensees in a litigation note, three of them service giants that are also NOV's
customers; the rule worked but yields a field of a different shape from NOV's equipment business, which I stated rather
than corrected. (5) **The all-equity add-back needs a tax rate** for the interest shield that the framework does not
name; confessed as a CONVENTION of this run at the 21% statutory rate.
