# Company Run: Innoviva, Inc. (NASDAQ: INVA), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form: `Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold; every filing fact carries its accession; the first STOP that failed closed the run and later questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 INVA/` (filings as text, `fetch.py`, `series.py`, `ledger.py`, `compute.py`, the `tools/run.py` output). *(The template's headings carry em dashes; this file writes them with colons or hyphens under the standing no-em-dash rule, and writes the protocol's heading as "COMPUTATION - NOT A CLEARANCE", as the September runs did.)*

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`, so the analyst does not know whether the operator holds INVA. The verdict below was reached without that knowledge.

**CONTAMINATION, declared:** none about this company. Seen before the run began: the session's git status and five recent commit subjects (CALY, PRKS, TDS, CENT, OGN runs, all OUT), and a directory listing of `Test Runs/` that showed other companies' 2026-10-05 file names (no INVA file); none was opened. The memory index line "57 gate-clearers, nothing buyable" was in context; it names no company. No INVA run, review, queue line or reading-list line was opened.

**A premise of the brief corrected by the filings:** the brief says INVA receives royalties on Trelegy. It no longer does. "On July 20, 2022, we completed the sale of our 15% ownership interest in TRC to Royalty Pharma Investments 2019 ICAV (“Royalty Pharma”) for $282.0 million [...] and a potential $50.0 million sales-based milestone" (10-K FY2022, accession 0000950170-23-005168); "we are no longer entitled to receive 15% of royalty payments made by GSK stemming from sales of TRELEGY® ELLIPTA®. We retained our royalty rights with respect to RELVAR®/BREO® ELLIPTA® and ANORO® ELLIPTA®." (same filing). The royalty portfolio today is Breo/Relvar and Anoro only.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $20.63 (close 2026-10-05, from `tools/run.py`; aggregator, live quote only, flagged under operator rule 5).
- **Shares, one class:** 72,245,485 common shares as of 2026-07-31, cover of the 10-Q for the period ended 2026-06-30, filed 2026-08-05, accession `0001193125-26-335235` (`python Screens/cover_shares.py INVA`). No other class; balance-sheet count 72.637M at 2026-06-30 before July repurchases of 453,798 shares (10-Q, same accession).
- **Market cap:** about $1,490M (72.245M × $20.63).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05 (via `tools/run.py`, which calls `tools/sources.py`).
- **Filings read (operator rule 4):**
  - 10-K FY2025, filed 2026-02-25, accession `0001193125-26-071776` (Items 1, 1A, 5, 7, notes on revenue, investments, debt, segments, equity statement, cash-flow statement).
  - 10-Q Q2 2026, filed 2026-08-05, accession `0001193125-26-335235` (MD&A, balance sheet, fair-value tables, debt, buybacks).
  - DEF 14A filed 2026-03-24, accession `0001140361-26-010912` (board, ownership, pay).
  - 8-K 2026-05-18, accession `0001193125-26-228958` (two directors resign to run Syndeio; new director); 8-K 2026-08-05, accession `0001193125-26-335192` (results, Item 2.02).
  - Earlier 10-Ks for the span: FY2022 `0000950170-23-005168`; FY2019 `0001104659-20-022807`; FY2016 `0001047469-17-001057`. XBRL company facts for the ten-year series (`facts.json`, `series.py`).
  - Competitors: GSK plc 20-F FY2025, filed 2026-03-06, accession `0001131399-26-000004`; AstraZeneca PLC 20-F FY2025, filed 2026-02-24, accession `0001104659-26-019130`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 is $196,930 thousand in the filed cash-flow statement (10-K FY2025) and 196.9 in `tools/run.py`; cash and cash equivalents $550,941 thousand filed against 551 in the tool's balance-sheet table. Both agree.
- **`tools/run.py INVA`, arithmetic lines only** (its v4 material is not read, Part VII):

| FY | OCF | SBC | D&A | capex | other capital payments (intangibles, IPR&D) | OE capex basis | OE D&A basis |
|---|---|---|---|---|---|---|---|
| 2023 | 141.1 | 5.8 | 21.8 | 0.4 | 0.0 | 134.8 | 113.4 |
| 2024 | 188.7 | 6.4 | 25.9 | 0.3 | 4.0 | 182.0 (alt 178.0) | 156.4 |
| 2025 | 196.9 | 9.5 | 26.3 | 1.1 | 9.4 | 186.3 (alt 177.0) | 161.2 |

  Three-year mean 167.7 (capex) / 143.7 (D&A); alternates with the other capital payments 163.3; five-year window 211.9 (capex). The D&A here is almost entirely amortization of acquired drug intangibles and of the 2014 GSK milestone, not plant.

**Owner cash recast by the analyst, ten years** ($M; OCF less stock pay, capex and other capital payments, less distributions to the noncontrolling holder of TRC, which were cash the consolidated OCF counted but INVA's owners never received; sources: XBRL facts tagged `NetCashProvidedByUsedInOperatingActivities`, `ShareBasedCompensation`, `PaymentsToAcquirePropertyPlantAndEquipment`, `PaymentsToMinorityShareholders`, and the FY2022 cash-flow statement):

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| OCF | 61.0 | 141.7 | 223.5 | 257.5 | 313.1 | 363.8 | 201.7 | 141.1 | 188.7 | 196.9 |
| less NCI distributions | 0 | 0 | 6.0 | 10.6 | 30.5 | 59.5 | 69.8 | 0 | 0 | 0 |
| owner cash | 52.4 | 131.9 | 214.3 | 244.8 | 280.9 | 302.3 | 124.5 | 134.9 | 178.0 | 176.9 |

Five-year mean 2021 to 2025: 183.3. **What this cash is:** almost all of it is the GSK royalty (gross royalties $250.3M in FY2025 against income from operations of $163.7M, 10-K FY2025) plus interest on cash ($21.1M in FY2025). The 2022 figure is low partly because $53.9M of tax paid on the TRC sale gain ran through OCF while the $248.2M proceeds ran through investing. Nothing in this table deducts the capital put into drug businesses and venture stakes, which the brief and the framework treat as capital: 2020 to 2022 alone, $300M placed in the Sarissa-managed ISP Fund (FY2025 10-K, Item 1), purchases of equity and long-term investments of $88.0M, $66.3M and $58.7M, La Jolla for $159.1M net of cash, and the Entasis minority for $43.9M (FY2022 cash-flow statement, `0000950170-23-005168`).

**Balance sheets, ten years, read before the income account** (`tools/run.py` first-filed XBRL, $M): "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.

| year-end | assets | equity | cash | goodwill | intangibles | LT debt | retained |
|---|---|---|---|---|---|---|---|
| 2016 | 379 | -353 | 118 | - | - | 708 | -1,633 |
| 2018 | 548 | 154 | 62 | - | - | 383 | -1,104 |
| 2020 | 1,000 | 540 | 246 | - | - | 386 | -722 |
| 2021 | 926 | 415 | 202 | 0 | 0 | 395 | -456 |
| 2022 | 1,231 | 566 | 291 | 27 | 253 | 444 | -205 |
| 2023 | 1,244 | 675 | 194 | 18 | 230 | 446 | -25 |
| 2024 | 1,301 | 691 | 305 | 18 | 208 | 256 | -2 |
| 2025 | 1,635 | 1,173 | 551 | 18 | 182 | 258 | 269 |

What moved and why. (1) Equity went from minus $353M to $1,173M as the royalty paid down the Theravance-era debt ($708M to $258M) and refilled a $1.6B accumulated deficit; this is the royalty's work, not the new businesses'. (2) Equity fell in 2021 ($540M to $415M) after $394.1M bought back GSK's entire stake (FY2022 10-K: "we completed the share repurchase agreement with GSK to buy back all of its shares"). (3) Goodwill and $253M of intangibles appear in 2022 with Entasis and La Jolla and have amortized to $182M; goodwill was written from $27M to $18M. (4) The 2025 jump of $482M in equity is $192.5M of convertible notes converted into 11,149 thousand shares and $271.2M of net income, of which $161.6M was unrealized fair-value gain on investments, mostly Armata (10-K FY2025, equity statement and MD&A); the 10-Q shows $161.0M of that reversed in Q2 2026. (5) The asset side is now cash $570.4M, investments $660.9M (equity-method $219.5M plus equity and long-term $441.3M) and drug intangibles and goodwill $186.9M, against $1,702.7M total (10-Q, 2026-06-30). **What the figures cannot say:** $316.0M of the investments are Level 3, priced by Monte Carlo and discounted-cash models (10-Q fair-value table), including a $15.0M 2021 Syndeio note carried at $70.3M and $133.1M of term loans plus a $105.0M convertible note lent to Armata, a 68.8%-owned clinical-stage phage company (10-K FY2025, Note on equity-method investments). The balance sheet also does not show that the asset producing nearly all the cash, the royalty, carries only $49.2M of capitalized fees, amortizing to zero in about 3.6 years.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: the owner gets the cash the parts produce, and here the parts are a royalty that ends, a hospital drug business, and a book of venture stakes; the royalty's coupons are close to printed, "Businesses have coupons that are going to develop in the future, too. The only problem is they aren’t printed on the instrument." **[M1997-050]**, which is why it is the one part that can be pictured. The second is who is paid to tell you: the company calls itself "well-positioned to deliver significant long-term shareholder value" (10-K FY2025, Item 1), and its strategy was set by an activist whose fund it paid. The row: "good salespeople believe their own baloney" **[M2020-009]**. **Contrary evidence, written down as found** "in the first 30 minutes" **[M1997-127]**: (a) the brief's Trelegy premise is false (above); (b) the royalty is not flat but sliding, Breo plus Anoro gross royalties $279.0M in 2021 to $250.3M in 2025 (10-Ks FY2022 and FY2025); (c) GSK received a paragraph IV notice for a generic Breo in August 2025, trial set for 2 November 2026 (GSK 20-F FY2025); (d) Breo is selected for Medicare price negotiation effective 1 January 2027 and Anoro for 2028 (INVA 10-K FY2025, Item 1A); (e) the capitalized-fee amortization, which the company sets to the royalty term, runs out about early 2030; (f) the non-royalty operations (IST plus corporate) lost money before amortization in H1 2026 even with $12.9M of license income (10-Q); (g) in its favour, written down the same way: product sales grew from $60.6M (2023) to $172.1M (2025) and $93.1M in H1 2026, cash is $570.4M, and the company has $261.0M of 2.125% debt due 2028 and no other borrowings (10-K, 10-Q).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought without borrowed money and sized so that a total loss is survivable: "never going to risk what we have and need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. No financing or size is set here; the run closes before Q10.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "the first question is, can I understand it?" **[M1995-051]**; understanding is "a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]**, "what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**. Key variables first: "If something is not very predictable, forget it." **[M1998-044]**. A holding company is read by its parts: the framework's CONVENTION at Q1 keeps the whole outside the circle when a part that matters cannot be understood. The row it rests on: "if you have doubts about something being into your circle of competence" **[M2002-092]**. The row that read five trading houses "as a group" **[M2023-031]** stays OPEN against it and is answered below.

**The parts, from the filings.**

1. **The GSK royalty (Breo/Relvar and Anoro): understood, and ending inside the horizon.** Terms: 15% on the first $3.0B of annual global Breo/Relvar net sales and 5% above; Anoro tiered 6.5% to 10% (10-K FY2025, Item 1). Term: the company amortizes the 2014 milestone "as the later of the expiration or termination of the last patent right covering the compound in such product in such country and 15 years from first commercial sale of such product in such country" (10-K FY2025, Note 1), and the remaining $49.2M at $13.8M a year (10-Q) puts the company's own estimate of the end at about early 2030; US Breo launched October 2013 (10-K, Item 1A), so 15 years runs to October 2028. GSK's patent table: Relvar/Breo US new-molecular-entity patent "expired", other US patents 2027 to 2031, EU 2028; Anoro US 2027, EU 2029 (GSK 20-F FY2025, `0001131399-26-000004`). Threats on dated filings: generic Breo paragraph IV from Transpire Bio, trial 2 November 2026 (GSK 20-F); Medicare negotiated price on Breo from 1 January 2027 and on Anoro from 2028 (INVA 10-K FY2025, Item 1A). The ten-year key variables (GSK's sales of two products, a contractual rate, a contractual end) are knowable, and they show a stream that is near zero by 2031. Ten-year history of the gross royalty ($M, INVA 10-Ks FY2016, FY2019, FY2022, FY2025):

| | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Breo/Relvar | 16.6 | 59.2 | 128.6 | 198.7 | 220.2 | 189.4 | 221.5 | 234.1 | 215.0 | 208.0 | 207.9 | 204.0 |
| Anoro | 1.8 | 7.7 | 17.9 | 29.0 | 41.3 | 42.6 | 46.0 | 44.9 | 38.4 | 44.6 | 47.6 | 46.3 |

   (H1 2026 gross royalties: $58.6M and $59.8M, 10-Q.) **Inside the circle, as a liquidating asset.** "we bring nothing to the table when it comes to evaluating patents" **[L1999-019]** bites only on the generic case's timing, and the contractual end bounds it.

2. **Innoviva Specialty Therapeutics (IST): a hospital anti-infective and critical-care drug business whose present products all lose exclusivity inside the ten years.** Products and the filed dates: Xerava US patents expire 7 August 2029 (crystalline-form patents 2037); Giapreza generic licensed under the February 2025 settlement "commencing in the early 2030s", patents 2029 to 2040; Xacduro patents 2 April 2033 and 17 November 2035; Zevtera ten years of exclusivity from April 2024; Nuzolvence ten years from December 2025, patents to May 2035 (10-K FY2025, Item 1). Competition the company names: Giapreza against generic norepinephrine and vasopressin; Nuzolvence against generic ceftriaxone and GSK's Blujepa, approved the day before it (10-K FY2025, Item 1). Hospital drugs "generally are not reimbursed by third-party payors" and adoption "generally occurs more slowly" (same). Earnings: INVA reports one segment (10-K FY2025, Note 16), so IST's profit is not disclosed; on the filed lines, income from operations less net royalty revenue was minus $72.8M in FY2025 and minus $22.5M in H1 2026, or minus $9.3M before $13.2M of intangible amortization and after $12.9M of license income (10-Q). Ten years out (2036) IST's economics are the economics of drugs it has not yet bought or invented. The rows put that business in Q1's list of what it rules OUT: "Take pharmaceuticals, if they had never invented any more pharmaceuticals, it would be a terrible business." **[M1999-075]**; and the analyst brings nothing to "evaluating patents" **[L1999-019]**.

3. **The strategic investments: venture stakes stated at $669.5M, about 45% of the market value.** At 2026-06-30: Armata $457.7M (common $162.5M, warrants $57.0M, five term loans $133.1M, convertible note $105.0M), other strategic equity and convertible debt $177.3M (Syndeio note $70.3M, Lyndra, InCarda, Beacon Biosignals, ImaginAb), ISP Fund $34.5M (10-Q fair-value table and MD&A). Armata is a clinical-stage bacteriophage developer, 68.8% owned, two of whose seven directors sit on INVA's board (10-K FY2025, investments note). Inside INVA, Nortiva Bio was launched in Q2 2026 to develop the Lynx long-acting oral platform (10-Q). These are start-ups and development programmes: "Start-ups are not our game." **[L2007-015]**; "blot out startups" **[M2008-088]**; and the 2007 meeting row on not trying to guess "whether, you know, one drug company has a better drug pipeline than another" **[M2007-069]**.

**The by-parts test.** Part 1 is understood; parts 2 and 3 are not, and they matter: the investments are about 45% of the market value, IST is where management says the company is going ("a meaningful transformation of our company over the years from a pure-play royalty business to a diversified biopharmaceutical company", 10-K FY2025, Item 1), and once the royalty ends near 2030 parts 2 and 3, and whatever the royalty cash has been turned into, are the whole company. So the test, "where the business will be in 10 years" **[M2000-037]**, has no answer that runs through the understood part. **[M2023-031]** does not rescue it: the trading houses were bought as "understandable companies" earning "14%" with long records "we could understand as a group"; the group here is a liquidating royalty plus an unproven drug portfolio plus clinical-stage stakes, which is not a group of the same kind.

**Hunting the other side** **[M2025-013]**. The strongest rows for the pharmaceutical case: Munger, "the future of the pharmaceutical industry was easier to predict than the future of the high-technology sector", and Buffett, "the pharmaceutical industry has a far, far better record of returns on large amounts of equity over time" **[M2001-002]**; and "if we could buy a group of leading pharmaceutical companies at a below-market multiple" **[M1999-043]**. Both speak of the industry as a group, its leaders, bought as a basket. Neither speaks of a single small hospital-antibiotic portfolio with seven-year-old products, nor of clinical-stage stakes, and neither row says the economics of one company's drugs ten years out can be seen. They do not move the verdict; they are recorded.

**Routing, and which box.** The rows on which the file turns are those Q1's own list places under what it rules OUT: the drug business that is "a terrible business" unless new drugs keep coming, "if they had never invented any more pharmaceuticals" **[M1999-075]**, and the start-up, "Start-ups are not our game." **[L2007-015]**, **[M2008-088]**. The framework's section I says a Q1 failure ("a business whose economics cannot be foreseen") is TOO HARD, while Q1's list sends these two cases to OUT and moved only fast-changing technology to TOO HARD; the list is the more specific text and is the framework's only routing for pharmaceuticals, so this run follows it (the conflict is reported below). The NATURE reading would close the file the same way and forever: the industry's insiders "would not want to put down on paper their predictions" **[M2000-105]** of a portfolio of this kind ten years out, and more study would not mend it, "we went in deficient in the first place" **[M2008-086]**. It is not TOO HARD (WORK): the deciding question, IST's and the stakes' economics after 2030, is not knowable from any document, so no research pass is opened: "important but unknowable, forget it" **[M2006-076]**.

- **VERDICT: OUT** at Q1. The understood part, the GSK royalty, ends inside the horizon (about early 2030 on the company's own amortization; US October 2028 on the 15-year rule); what remains and matters, a drug business whose products all lose exclusivity 2028 to 2035 and venture stakes stated at $669.5M, depends on drugs not yet found and on start-ups, the two cases Q1's list rules out (rows **[M1999-075]**, **[L2007-015]**, **[M2008-088]**, with **[L1999-019]** on patents), read by parts under **[M2002-092]**. The box: "in, out, and too hard" **[M2006-013]**.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
**NOT REACHED** (the file closed at Q1). The competitor facts gathered for it are recorded under "Evidence gathered past the STOP" below and are not judged.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
**NOT REACHED.**

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion, otherwise WEIGHING.
**NOT REACHED as a verdict.** The ten balance sheets were read in Step 0 above, as the template asks when the file closes before Q4. No confusion verdict is entered.

## Q5: WHO RUNS IT. STOP on integrity.
**NOT REACHED.** Facts recorded below, not judged.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts recorded below, not judged; the buyback test against the bottom of the Q7 range is not run because Q7 was not reached.

## Q7: WHAT IS IT WORTH? STOP.
**NOT REACHED as a verdict.** The owner's requested arithmetic is below under COMPUTATION - NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9: COULD IT RUIN US? WEIGHING.
**NOT REACHED.**

## Q10: IS IT THE FAT PITCH? WEIGHING.
**NOT REACHED.**

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.**

---
## COMPUTATION - NOT A CLEARANCE
*Made at the owner's request after the closing STOP (operator rule 3). It carries no entry language and clears nothing. Script: `Test Runs/_research 2026-10-05 INVA/compute.py`. Valuation date: the 2026-06-30 balance sheet (10-Q `0001193125-26-335235`), less the $10.0M of July buybacks; shares 72.245M; price $20.63 on 2026-10-05. The method is the Q7 idea, value as discounted cash at the long government rate **[L2000-021]**, the same for "an oil royalty, a farm, an apartment house" **[M2003-135]**, read by parts as the owner asked.*

**CONVENTION of this run (confessed): a royalty with a contractual end is valued as a declining annuity to that end, not by the Q7 range convention.** Rationale: the framework's range convention (five-year average of owner cash, carried at the growth shown, ten years, then no real growth for ever) would capitalize a stream the filings say ends about 2030 as a perpetuity; it does not fit a wasting asset. The two ends here mirror the convention's two ends: the **high** end is the shown trend (Breo plus Anoro gross royalties fell from $279.0M in 2021 to $250.3M in 2025, about 2.7% a year) run to the company's own amortization end (2029 full year, nothing after); the **low** end puts each filed threat on its earliest filed date (generic Breo after the November 2026 trial and the Medicare price from January 2027, the Anoro Medicare price in 2028, US Breo term ending October 2028 under the 15-year rule, an ex-US tail in 2029). The **central** case sits between. Royalty flows by year, gross, $M: low H2-2026 118, 2027 155, 2028 100, 2029 40; central 119, 200, 165, 120, 2030 20; high 120, 240, 233, 227.

**The parts ($M), discounted at the sovereign, 5.66%:**

| part | low | central | high | source / treatment |
|---|---|---|---|---|
| GSK royalty, present value (pre-tax) | 386.6 | 572.5 | 746.6 | the cases above |
| IST and corporate | -127.3 | 0 | 215.1 | low: the non-royalty operations' cash loss, about $40M a year, borne until the royalty ends; central: nil; high: carrying value of IST's net assets (intangibles 169.0 + goodwill 17.9 + inventory 39.0 + receivables 50.8 - HCR royalty obligation 61.6) |
| cash, less July buybacks | 560.4 | 560.4 | 560.4 | 10-Q |
| royalty receivable (Q2 royalties) | 59.8 | 59.8 | 59.8 | 10-Q |
| strategic investments at stated values | 669.5 | 669.5 | 669.5 | 10-Q, as the owner asked |
| less 2028 convertible notes (face) | -261.0 | -261.0 | -261.0 | 10-Q; conversion price $26.22, so carried as debt below that price |
| less HCR Giapreza royalty obligation | -61.6 | -61.6 | (in IST) | 10-Q |
| less long-term income tax payable, deferred tax liability, leases | -107.8 | -107.8 | -107.8 | 59.9 + 36.7 + 11.2, 10-Q |
| **total** | **1,118.5** | **1,431.8** | **1,882.6** | |
| **per share** | **$15.48** | **$19.82** | **$26.06** | 72.245M shares |

(a) **VALUE RANGE: about $15.50 to $26.10 a share against $20.63.** Top over bottom about 1.7, inside the three-to-one width, so by the Q7 convention this would be a narrow range with the price inside it: "too close to think about" **[M1996-084]**, the case that "should scream at you" and does not **[M2009-005]**. Sensitivities: royalty taxed at 21% gives $14.36 to $23.89; the $316.0M of Level 3 investments at zero gives $11.11 to $21.69. Over half of every case (cash, receivable and investments less liabilities, $11.89 a share) is the balance sheet, not the business, and the investments are the part Q1 could not read.

(b) **FAIR PRICE: about $19.35 a share, pre-tax.** The central case discounted at the ~10% pre-tax floor (the framework's CONVENTION at Q7, **[M1994-004]**, **[M2003-149]**): royalty present value $538.5M, IST nil, the balance-sheet items at stated values, total $1,397.8M. Tax treatment: royalty cash pre-tax, as the floor is stated pre-tax **[L2002-020]**; INVA pays cash tax (FY2025 paid $19.1M; its $497.7M of federal NOLs are all acquired with Entasis and La Jolla and limited by annual caps, 10-K FY2025), and with the royalty taxed at 21% the same case is $17.78. The fair price is generous in one way stated plainly: it treats the cash and the investments as if worth face to the buyer, while the company has said it will redeploy them, "deploying capital in areas of significant unmet medical need" (10-K FY2025, Item 1). At $20.63 the price is above it.

(c) **CHEAP PRICE: about $11.00 a share.** Rule (CONVENTION of this run, confessed): the price below which no pencil is needed is the **low** case discounted at the 10% floor with every Level 3 investment at zero, so that the buyer is covered even if the generic and the Medicare price arrive on their earliest dates, the specialty business burns cash to 2029, and the unpriced stakes are worth nothing; that is $10.98. Rationale: the margin is taken as "a big discount from that present value" **[M1997-126]**, and the cheap price is the point where even the bad case pays. At $20.63 the price is nearly twice it.

**Where the price sits.** Inside the range and above the fair price. Had the file reached Q7 it would have closed OUT by the convention (price inside a narrow range). With the Level 3 investments at zero the range runs $11.11 to $26.06, about 2.3 to one, still short of the width at which "the range must be so wide that no useful conclusion can be reached" **[L2000-025]**; the width is set mostly by marks Q1 could not read, not by the royalty.

---
## EVIDENCE GATHERED PAST THE STOP (recorded, not judged)
*Collected because the owner's reply asks for it. None of it is a clearance or a weighing; the run closed at Q1.*

**Competitor row (for Q2, not reached).** Same metric, product net sales, from the makers' own filings:

| product | maker | 2023 | 2024 | 2025 | source |
|---|---|---|---|---|---|
| Relvar/Breo (implied from INVA's 15% royalty) | GSK | $1,387M | $1,386M | $1,360M | INVA 10-Ks; GSK 20-F says Relvar/Breo "£1bn", -5% AER |
| Anoro | GSK | | | £542m, -5% AER | GSK 20-F FY2025 |
| Trelegy (GSK's own triple; INVA's share sold 2022) | GSK | | £2,702m | £2,986m, +11% AER | GSK 20-F FY2025 |
| Breztri (triple) | AstraZeneca | $677M | | $1,199M | AZN 20-F FY2025 |
| Symbicort US (authorised generic) | AstraZeneca | $726M | $1,187M | $1,193M | AZN 20-F FY2025 |

Over the whole span the implied Breo/Relvar sales were $1,325M in 2017, peaked at $1,561M in 2021 and are $1,360M in 2025, while the triples grow: AstraZeneca reports China "being affected by ICS/LABA class erosion in COPD in favour of FDC triple therapy" (AZN 20-F FY2025), and GSK reports "Other respiratory products continue to reduce across all regions as a result of continued generic erosion and competitive pressures" (GSK 20-F FY2025). INVA's own risk factor: "sales of generic Advair®, GSK’s approved medicine for both COPD and asthma, continue to have a negative impact on sales of RELVAR®/BREO® ELLIPTA®" (10-K FY2025). Royalty Pharma, the brief's model, is the company that bought INVA's Trelegy interest in 2022; its filings were not read.

**People and the money (for Q5 and Q6, not reached).**
- The activist contest: 2017 "net proxy contest and associated litigation costs" of $8.1M; February 2018 settlement with Sarissa including a $2.7M payment to Sarissa; $5.7M of severance to departing senior management in 2018 (10-K FY2019, `0001104659-20-022807`). The chief executive since May 2020 came from Sarissa's investment team (10-K FY2025, Item 1).
- December 2020: $300M placed in ISP Fund LP, managed by Sarissa for "a customary one percent management fee" and "a customary 10% annual performance allocation" (10-K FY2025, MD&A); the fund's investments were valued at $255.7M at 2024 year-end after a 36-month lock-up (10-K FY2025 fair-value table, 2024 column); unwinding since, $121.0M distributed in 2025. Sarissa's representatives left the board in May 2025.
- May 2026: two directors, one Sarissa's former general counsel, resigned "to focus on the growth of Syndeio BioSciences Inc.", a company in which INVA holds notes carried at $70.3M against $15.0M lent in 2021 (8-K `0001193125-26-228958`; 10-Q).
- Share count: 101.4M (2020), 69.6M (2021, after buying GSK's stake for $394.1M), 62.7M (2024), 74.6M (2025, after 11,149 thousand shares issued on conversion of the 2025 notes, about $17.26 a share, and 591 thousand on warrants at $18.11), then 2,374,313 shares bought back in H1 2026 at an average $21.83 and 453,798 in July (10-Ks, 10-Q). The programme names no price: "The authorization permitted management to repurchase shares of the Company’s common stock from time to time at management’s discretion" (10-Q). The rows on this: "almost never refer to a price above which repurchases will be eschewed" **[L2016-002]** and issuance low with buying high, "they sell low and then they buy high" **[M1998-027]**, would be weighed at Q6 against the bottom of the Q7 range ($15.48 above); they are not weighed here.
- Pay: chief executive total $5,400,197 in 2025 against $868,648 in 2023; contingent 2026 plan awards of 439,146 to him; directors and officers own 2.01%, the chief executive's 734,885 being 714,063 options (DEF 14A `0001140361-26-010912`).
- Capital allocation 2020 to 2025: Trelegy interest sold for $282.0M (2022); Entasis and La Jolla bought (2022); dividends none since 2015; convertible notes $261.0M due March 2028 at 2.125%.

---
## THE BOX
**OUT, at Q1.** The part that can be understood, the GSK royalty on Breo/Relvar and Anoro (gross $250.3M in 2025, sliding about 2.7% a year), ends inside the ten-year horizon on the company's own amortization (about early 2030); the parts that matter after it, a hospital drug business whose products all lose exclusivity between 2028 and 2035 and venture stakes stated at $669.5M (about 45% of the market value), depend on drugs not yet found and on start-ups, the two cases Q1's list rules out (rows **[M1999-075]**, **[L2007-015]**), read by parts under **[M2002-092]**. Not reached: Q2 to Q12. For the owner's request only, COMPUTATION - NOT A CLEARANCE: value range $15.48 to $26.06 a share, fair price $19.35 (central case at the 10% pre-tax floor), cheap price $10.98, against $20.63. Q11 belongs to a holding review, not to this purchase run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written in one pass after the reading, not question by question with a commit after each: the operator's instruction for this run forbids commits, so the write-early commits were not made. *(Partial: copied first, but not committed per question.)*
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; no v4 or E ids); every filing fact has its accession; every number has a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance; the arithmetic after it is headed COMPUTATION - NOT A CLEARANCE and carries no entry language.
- [x] Owner cash after every real cost, never a net-income proxy (OCF less stock pay, capex, other capital payments and the minority's distributions); the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found **[M1997-127]**, including the evidence for the pharmaceutical case **[M2001-002]**, **[M1999-043]**.
- [x] No row dated after the anchor is cited (the anchor is today; this is not a point-in-time run).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 ids and floor were not read as rules.
- [x] `python tools/check_framework.py` PASS on 2026-10-05 (both ledgers verbatim, run files phantom in 0 files, V5 SCOPE OK). No commit made, at the operator's instruction for this run. A script check also found no E or v4 ids, every M/L/R id present in `principle_ledger_v5.csv`, and every quoted fragment beside an id inside that row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Two routings for the same Q1 failure.** Section I says a Q1 failure ("a business whose economics cannot be foreseen") is TOO HARD; Q1's own list of what it rules OUT keeps two such cases as OUT, the pharmaceutical business that depends on new drugs (row M1999-075) and the start-up (row L2007-015), having moved only fast-changing technology to TOO HARD. For a pharmaceutical or a start-up holding the two texts give different boxes; this run followed the more specific list and recorded that the NATURE reading closes the file too. A sentence saying which governs is needed. (2) **The holding-company convention names no box.** "keeps the whole outside the circle" does not say OUT or TOO HARD, nor what "matters" means; this run used size (about 45% of market value) and the fact that the unreadable parts become the whole company once the readable part ends. (3) **The Q7 range convention cannot value a wasting contractual stream.** Five-year average, shown growth, ten years, then no real growth for ever, would capitalize a royalty that ends about 2030 as a perpetuity; a royalty, a patent-bound drug, a mine or a lease needs a stated rule for a contractual or legal end. This run confessed a declining-annuity CONVENTION. (4) **The floor is stated as a return on the price, but most of this company's value is cash and marked investments**; "the central case clears the ~10% floor" means little when 60% of the value is balance-sheet items valued at face, and the framework says nothing on how cash and marked investments enter the floor test. (5) **Owner cash for a liquidating royalty.** The template's owner-cash line and `tools/run.py` treat the royalty's cash as recurring; the framework has no line asking whether the cash source itself ends. (6) **The brief's premise was wrong** (Trelegy sold in 2022); the template has no place to record a corrected premise, so it was written at the top. (7) Operator rule 3 prints the computation heading with an em dash between "COMPUTATION" and "NOT A CLEARANCE", which the standing style rule forbids; written with a hyphen here, as the September runs did.
