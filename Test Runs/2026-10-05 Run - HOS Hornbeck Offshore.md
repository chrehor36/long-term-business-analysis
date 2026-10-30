# Company Run — Hornbeck Offshore Services, Inc. (NYSE: HOS) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`,
so the analyst does not know whether the operator holds this name. The incentive the protocol names (operator rule 9)
is declared in the other direction too: nothing here was written to clear or to fail a holding.

**CONTAMINATION, declared.** Read before the verdict: the session's git status listed untracked run files for CSW and
SHOE dated 2026-10-05 (names only, not opened), and the recent commit subjects named other runs' boxes (RYZ, GENC and
MBUU, each "OUT at Q2", and a PRIME RULE 5 case on "seven framework gaps found by the 2026-10-05 small-cap runs"). None
was opened. The commit subjects tell me that commodity-type names have recently closed OUT at Q2; I record it here
because it could anchor me toward the same box. No other `Test Runs/` file on Helix or Hornbeck exists by a filename
search; none was opened. `tools/run.py` printed v4 material (a "yield" and "points over the sovereign" verdict block);
only its arithmetic lines are used below (Part VII).

**WORKING FOLDER:** `Test Runs/_research 2026-10-05 HOS/` (filings as text, the XBRL facts files of the registrant,
old Hornbeck and four competitors, `span.py` and `valuation.py`, the `run.py` output).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING

### What the registrant is, from the filings
- **The registrant** is CIK 0000866829, Helix Energy Solutions Group, Inc. until 2026-08-31 (former names in the EDGAR
  submissions file: Cal Dive International to 2006, Helix to 2026-08-31). On **2026-09-01** Helix (converted from a
  Minnesota to a Delaware corporation) completed an all-stock combination with privately held **Legacy Hornbeck Offshore
  Services, Inc.** under a merger agreement dated **2026-04-22**, approved by Helix shareholders on 2026-08-31, and took
  the Hornbeck name; the stock trades as HOS from 2026-09-02 (8-K of 2026-09-01, accession `0001193125-26-378529`,
  Introductory Note, Items 2.01, 3.02, 5.02; Ex 99.3 press release).
- **The structure.** Each Legacy Hornbeck share became **10.27167** new shares; Legacy Hornbeck's **Jones Act Warrants**
  (issued in the 2020 reorganization to non-U.S. holders in lieu of stock, exercise price $0.00001) were assumed and each
  became exercisable for 10.27167 shares; its Creditor Warrants were settled in about 11.3M shares; Helix RSUs and PSUs
  were settled in cash. Consenting Hornbeck holders received **37,818,435** unregistered shares (8-K, Item 3.02). The
  deal is accounted for as a **reverse acquisition: Legacy Hornbeck is the accounting acquirer** and Helix the acquiree,
  at a preliminary purchase price of **$1,573.1M** (147,255K Helix shares at the $10.60 closing-date price plus awards),
  with **$195.4M of goodwill** recorded (8-K/A of 2026-09-08, accession `0001193125-26-384311`, Ex 99.1, Note 1).
  Hornbeck's CEO (Todd M. Hornbeck) became CEO; four of seven directors were designated by Legacy Hornbeck; Ares holds
  about 12% of the votes; on a fully diluted basis Helix holders own about **45%** and Hornbeck holders about **55%**
  (424B3 proxy statement/prospectus of 2026-07-31, accession `0001140361-26-030494`, and the 8-K/A).
- **The businesses now owned:** Legacy Hornbeck's 59 OSVs and 12 MPSVs (U.S.-flagged, Jones Act-qualified, Gulf of
  America, Latin America, U.S. military) and shore base; Helix's well intervention fleet (seven vessels, two of them,
  the Sea Helix 1 and Siem Helix 2, chartered from Sea1 Offshore for Petrobras), robotics (48 ROV/trencher assets, seven
  chartered vessels) and production facilities. Helix sold its shallow-water decommissioning arm, Helix Alliance, on
  2026-05-01 for $107.5M cash (10-Q for Q2 2026, accession `0000866829-26-000022`, Note 3).

### The numbers
- **Price:** $7.96 (live quote 2026-10-05 from `tools/run.py`; **aggregator, flagged**). Last full close: $7.59 on
  2026-10-02 (Yahoo chart API; **aggregator, flagged**). The filed closing-date price was $10.60 on 2026-09-01 (8-K/A,
  Note 1); the stock has fallen about 25% in the five weeks since it began to trade as HOS.
- **Shares by class.** `python Screens/cover_shares.py HOS` returned **147,382,447** from the 10-Q filed 2026-08-06
  (cover as of 2026-08-03, accession `0000866829-26-000022`). **That count is pre-merger and wrong for today.** The
  S-3ASR of 2026-09-15 (accession `0001193125-26-392128`) states **222,166,587 shares outstanding as of 2026-09-14**. On
  top of them sit the assumed **Jones Act Warrants, exercisable at $0.00001, for about 103.6M shares** (the pro forma EPS
  note counts "Conversion of Legacy Hornbeck Jones Act Warrants" at 103,637K shares, 8-K/A Ex 99.1 Note 5; the S-3ASR
  registers 99,511,689 of those warrant shares for the selling holders alone). A penny warrant is a share in all but the
  vote, so the share basis used here is **325.80M as converted** (222.17M + 103.64M), with about 1.9M more from options
  and unvested units (pro forma diluted 327,991K).
- **Market cap:** $1,768M on the 222.17M shares outstanding; **$2,593M as converted** at $7.96. (`tools/run.py` printed
  $1.17B on the pre-merger cover count; that line is set aside.)
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield on the US Treasury daily par yield
  curve, 2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the registrant's 10-K for FY2025 (filed 2026-02-26, `0000866829-26-000008`) and
  for FY2022 (`0000866829-23-000010`); the 10-Q for Q2 2026 (`0000866829-26-000022`); the 424B3 merger proxy statement/
  prospectus (`0001140361-26-030494`); the closing 8-K with **Legacy Hornbeck's audited FY2023 to FY2025 statements (Ex
  99.1, EY opinion dated 2026-03-24) and its Q2 2026 interim statements (Ex 99.2)** (`0001193125-26-378529`); the 8-K/A
  pro forma (`0001193125-26-384311`); the S-3ASR (`0001193125-26-392128`). Old Hornbeck (CIK 0001131227, now "Hercules
  Sub LLC"): the 10-Ks for FY2019 (`0001131227-20-000041`, filed 2020-07-10 during Chapter 11), FY2018
  (`0001131227-19-000015`) and FY2013 (`0001445305-14-000785`); the S-1 of 2023-12-07 (`0001193125-23-290782`) and the
  S-1/A of 2026-01-13 (`0001193125-26-011912`), the withdrawn IPO. The 2026 DEF 14A was not read (Q5 not reached).
- **One figure cross-checked against the filed statement:** Helix's FY2025 cash from operations **$136,749K** and
  capital expenditures **$16,342K** in the 10-K cash flow statement (`0000866829-26-000008`) match `tools/run.py`'s 137
  and 16. Legacy Hornbeck's FY2025 operating cash **$142,075K** is read from Ex 99.1 itself (no XBRL exists for it).
- **`tools/run.py HOS`, arithmetic lines only.** Its owner-earnings table is **Helix alone** (the pre-merger registrant:
  OCF 152 / 186 / 137, SBC 7 / 7 / 7, D&A 164 / 173 / 187, capex 20 / 23 / 16 for FY2023 to FY2025, $M). It does not
  describe the business now owned, which is half Hornbeck, so the combined owner cash is rebuilt below from both
  companies' filed cash flow statements.

### The balance sheets first, eight to ten years of them (Q4's instruction, read here because the file closes at Q2)
The rows ask for "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
Two sets exist, because the accounting acquirer is Hornbeck and the legal registrant is Helix.

| $M, year-end | Old Hornbeck 2010 | 2013 | 2015 | 2017 | 2019 | | New Hornbeck 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Total assets | 1,878 | 2,834 | 2,984 | 2,769 | 2,669 | | 1,026 | 1,153 |
| Long-term debt | 758 | 1,064 | 1,070 | 1,081 | n/a (reclassified in Chapter 11) | | 441 | 441 |
| Stockholders' equity | 842 | 1,295 | 1,446 | 1,438 | 1,172 | | 434 | 568 |
| Cash | 127 | 439 | 260 | 187 | 121 | | 81 | 54 |

*(Old Hornbeck: XBRL of its 10-Ks, first-filed values, `Test Runs/_research 2026-10-05 HOS/facts/facts_0001131227.json`;
2013 and 2015 to 2018 debt and equity agree with the selected-data tables of the FY2013 and FY2018 10-Ks. New Hornbeck:
audited balance sheets in Ex 99.1 of `0001193125-26-378529`: cash $80.8M (2024) and $54.2M (2025); debt $441.2M and $440.6M.)*

| $M, year-end (Helix, the registrant, from `tools/run.py`'s ten-year table) | 2016 | 2018 | 2020 | 2022 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| Total assets | 2,247 | 2,348 | 2,498 | 2,389 | 2,597 | 2,616 |
| Equity | 1,282 | 1,618 | 1,740 | 1,517 | 1,520 | 1,580 |
| Retained earnings | 323 | 383 | 465 | 323 | 368 | 399 |
| Cash | 357 | 279 | 291 | 187 | 368 | 445 |
| Receivables | 102 | 68 | 132 | 213 | 259 | 304 |
| Long-term debt | 558 | 393 | 259 | 226 | 306 | 298 |

**What the figures say.** (1) **Old Hornbeck's balance sheet is the record of a fleet built on borrowed money into a
collapse.** Debt went from $758M (2010) to about $1.1B (2013 to 2018) to pay for newbuild programs; capital spending was
$267.6M (2009), $258.3M (2012), **$542.7M (2013), $408.7M (2014), $293.3M (2015)** against depreciation and amortization
of roughly $55M to $93M a year (selected data, FY2013 and FY2018 10-Ks). Equity of $1,172M at the end of 2019 was then
cancelled: "All pre-petition equity interests in the Company will be canceled, released, and extinguished" (FY2019 10-K,
`0001131227-20-000041`, MD&A). (2) **New Hornbeck's balance sheet is a fresh-start balance sheet.** Its PP&E of $754M
(2025) is the 2020 fair value of the old fleet plus later purchases; depreciation fell from $65.7M for eight months of
2020 (predecessor) to $15.7M for all of 2021 "primarily due to a significant reduction in vessel carrying values
recognized as of September 4, 2020 resulting from the application of fresh-start" accounting (S-1 of 2023,
`0001193125-23-290782`, MD&A). The depreciation line therefore measures the write-down, not the cost of replacing the
fleet. (3) **Deferred charges are building:** Hornbeck's capitalized drydock costs rose from $72.1M to $97.2M in 2025
(Ex 99.1), with drydock spending of $63.9M against amortization of $43.8M; and $13.2M of the $44.7M of 2025 interest was
capitalized into vessel projects (Ex 99.1, Note 10). The rows say to look twice when "deferred asset accounts start
building up suspiciously high" **[M1995-064]**; here the build has an operating reason (more drydockings as stacked
vessels return), so it is a note, not a tell. (4) **Helix's ten years retained almost nothing:** retained earnings went
from $323M (2016) to $399M (2025), $76M in ten years on equity of $1.3B to $1.7B; the rise in equity in 2016 to 2017
came from issuing stock (cover counts 107.5M shares in February 2016, 147.7M in February 2017, the XBRL `dei` field of
its 10-Ks), not from earnings. (5) **Helix's receivables grew faster than its revenue** ($102M on $488M revenue in 2016,
$304M on $1,291M in 2025: 21% to 24% of a year's sales). (6) **What the figures cannot say:** Helix's fleet is old (the
Q4000 "has served customers in the spot market in the Gulf of America since 2002", the Seawell "has provided well
intervention and abandonment services since 1987" and was stacked for all of 2025, 10-K FY2025) and its capital
spending of $8M to $34M a year since 2020 ran at 6% to 23% of depreciation of $134M to $143M; whether that is a fleet being run down or a fleet that needs little is not on the
balance sheet. The rows say depreciation charges "are almost always true costs" **[L2015-004]**; in heavy-capital
businesses "your depreciation charges are inadequate and you’re kidding yourself as to your real economic profits"
**[M2015-049]**.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is that a share is a business: "Would I be happy buying this stock if the market closed
for five years?" **[M1997-109]**. For HOS the answer depends on where offshore spending goes, which the owner cannot
influence and the rows tell him not to forecast. The second is that the market "just tells us prices" **[M2006-077]**:
the 25% fall since the closing date says nothing about the business. The analyst's habits: hunt for "what you’re
missing" **[M2025-013]** and do scuttlebutt "to possibly reject your original hypothesis" **[M1998-144]**; and avoid "the
worst anchoring effect, which is always your previous conclusion" **[M2016-054]**, here the anchor of other names closed
OUT at Q2 in recent commits.

**Contrary evidence, written down as found** **[M1997-127]**, meaning evidence *for* the business, against the box I was
leaning toward:
- Hornbeck's dayrates beat the market: "our average dayrates were 41%, 20% and 42% higher than the global average term
  rates of comparably sized vessels owned by other operators in 2023, 2024, and the nine months ended September 30, 2025"
  (S-1/A, `0001193125-26-011912`, citing Fearnley Offshore Supply; the company's claim, from a third party's data).
- The Jones Act is a real legal shelter in U.S. coastwise trade, and U.S. military and offshore wind work also require
  Jones Act-qualified vessels (S-1/A, Business).
- Legacy Hornbeck earned operating income of $189.2M on $719.8M of revenue in 2025, a 26% margin, and $173.4M of net
  income (Ex 99.1); Tidewater's 2025 margin was 21% (283 on 1,353, XBRL).
- Helix carried $1.3B of contracted backlog at the end of 2025, $694M of it for 2026 (10-K FY2025).
- Pro forma the combined company held $684.5M of cash against $769.2M of debt at 2026-06-30 (8-K/A, balance sheet).
- My own lean could be wrong at Q1: the rows might send a business whose earnings ride a cycle no insider can forecast
  to TOO HARD at Q1 rather than to Q2. Recorded under "What in the framework was wrong or unclear".

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin, provided it is bought without borrowed money and sized so that a
second wipe-out of the equity (the 2020 one is on the record) is survivable: "We are never going to risk what we have and
need for what we don’t have and don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit"
**[L2014-005]**. The rule binds the buyer; the target's own debt is Q9's (not reached).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning
  power and competitive position will look like in five or 10 years" **[M2012-065]**. The product need not be understood
  in detail; "What is important is that I understand the economic dynamics of the industry." **[M2011-014]**.
- **The key variables.** (a) Offshore oil and gas spending by a few large customers (Shell 18% and Petrobras 10% of
  Helix's 2025 revenue, 10-K FY2025; two Hornbeck customers at 16% and 15%, Ex 99.1, Note 5), which follows the
  customers' view of oil prices (Helix 10-K FY2025, Item 7, "dependent on the prevailing view of future oil and natural
  gas prices"). (b) The supply of vessels: newbuilds, stacking and scrapping across the industry. (c) The Jones Act and
  its administrative interpretation. (d) For Helix, drilling-rig rates, which its own 10-K calls "a pricing indicator for
  our services". Variable (a) is not predictable, and the rows say "If something is not very predictable, forget it."
  **[M1998-044]**. Variables (b) to (d) are readable from the filings.
- **Do the past statements tell me "what the future financial statements are going to look like"** **[M2008-033]**? They tell me the *shape*: a capital-heavy service
  whose dayrates and utilization swing with customer spending and fleet supply, as Hornbeck's 2014 to 2019 figures show.
  They do not tell me the *level* of earnings in any year ten years out.
- **The routing.** Q1's TOO HARD is for a business whose ten-year economics cannot be foreseen "because its industry
  changes fast" (the framework's routing paragraph). Offshore vessels and well intervention change slowly; what makes the
  level unknowable is the cycle, not change. The competitive position, which is what the castle question needs, can be
  read from fifteen years of filings. The doubt rule, "if you have doubts about something being into your circle of
  competence, it isn’t." **[M2002-092]**, is applied to the castle judgment, and on that I have no doubt: the record
  answers it (Q2).
- **VERDICT: IN**, narrowly. The test "I understand the economic dynamics of the industry" **[M2011-014]** is met, and
  the castle can be judged from the record; Q1 must pass before Q2 can be asked, since without understanding "we can’t
  make a decision as to whether it has a sustainable edge" **[M1997-148]**. The unknowable variable (a) is carried to Q2
  as a finding about the castle, not settled here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. The answer from the filings is that, for the Hornbeck half, it
did not stand: the company that owns these vessels went through Chapter 11 in 2020 and its shareholders received
nothing; and that, for the Helix half, it never earned the return a castle protects.

**1. The attacker with money, and new entrants.** The attackers were domestic and came
with borrowed money. Hornbeck itself built the fifth newbuild program into the downturn (capex $542.7M in 2013,
$408.7M in 2014, $293.3M in 2015), and the S-1/A shows **21 or so of 59 OSVs still stacked in 2025** (average 59.4 OSVs,
37.7 active, nine months of 2025). Old Hornbeck's FY2019 10-K names the industry's own restructurings: "two of our
publicly traded domestic competitors emerged from chapter 11 proceedings in 2017 and such competitors merged in late-2018.
One of our privately held domestic competitors emerged from chapter 11 proceedings in 2018." The rows: "Normally, if
you’ve got a profitable business, you know, a dozen people want to go into it." **[M2000-077]**; here they did, and the
returns went to zero. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**: the answer was yes, shown by
events.

**2. Pricing power.** Hornbeck's new-generation OSV figures (FY2013 and FY2018 10-Ks,
S-1/A):

| | 2010 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2022 | 2023 | 2024 | 9M 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Average utilization | 71.6% | 83.2% | 83.7% | 79.6% | 54.4% | 25.2% | 23.1% | 26.3% | 28.3% | 37.7% | 44.3% | 41.3% | 47.9% |
| Average dayrate ($) | 21,561 | 23,445 | 26,605 | 27,416 | 26,278 | 25,233 | 20,250 | 19,150 | 18,679 | 32,305 | 39,297 | 41,956 | 44,366 |
| Effective dayrate ($) | 15,438 | 19,506 | 22,268 | 21,823 | 14,295 | 6,359 | 4,678 | 5,036 | n/a | 12,179 | 17,409 | 17,328 | 21,251 |

*(2019: utilization and dayrate from the FY2019 10-K MD&A; 2020 and 2021 not published, the company was private; from
2022 the series is "Average OSV" for the post-emergence fleet, S-1/A operating table, so the two halves are not strictly
the same fleet.)* The effective dayrate fell 79% from 2014 to 2017 and stayed there for five years. Hornbeck's own risk
factor: "Our customers award contracts based on price, industry reputation, service quality, vessel offerings and
capabilities, transit costs and other similar factors." (S-1/A). Helix's own: drilling rigs are "the asset class used for
offshore well intervention work, and rig rates are a pricing indicator for our services", and "larger competitors may
undercut us by reducing rates to levels we are unable to withstand" (10-K FY2025, Items 7 and 1A). A business whose
price is read off another industry's rate is the gas station of the rows: "whatever he charged for gas was my price."
**[M2012-109]**; "he determined our profit, because we looked at his price every day." **[M2023-079]**.

**3. Would the customer choose it over the low bid?** The customers are a few oil companies and
national oil companies who tender (Shell, Petrobras, Talos, Apache for Helix; two customers at 15% to 16% each for
Hornbeck). The premium Hornbeck claims (dayrates 20% to 42% above comparably sized vessels, Fearnley data via the
S-1/A) is a premium for larger, newer, higher-specification vessels, and it did not stop utilization falling to 23% in
2017. A premium that vanishes when the customer stops spending is not the See's question answered yes, where "it
wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**.

**4. The low-cost position, the one exception for a commodity field.** The rows: "being the low-cost producer is
all-important" **[L2000-017]**; "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**.
Hornbeck says plainly that it is *not* the low-cost operator absent the statute: "foreign vessels may have lower
construction costs and operate at significantly lower costs than companies operating in the U.S. coastwise trade"
(S-1/A, risk factors), and of the MPSVs, "prices for foreign-owned MPSVs in the GoM are often lower than prices we can
charge" (FY2019 10-K, Competition). A quarter of its 2025 revenue came from Brazil, Colombia and Mexico ($111.8M, $34.7M and
$33.0M of $719.8M, Ex 99.1, Note 5), where no Jones Act applies. The rows: "commodity businesses have risk unless you’re the
low-cost producer" **[M1997-010]**; "In an unregulated commodity business, a company must lower its costs to competitive
levels or face extinction." **[L1994-035]**; "the guy with the lower cost comes in and kills you" **[M2001-013]**.

**5. The statute as the castle.** In U.S. coastwise trade the Jones Act keeps the low-cost foreign operator out. That
is a wall the owner did not build and does not hold: "For years, there have been attempts to repeal or amend such
provisions, and such attempts are expected to continue in the future" (S-1/A); and Customs rulings since 2009 have let
foreign MPSVs into coastwise work that Hornbeck's industry has spent years litigating (FY2019 10-K, Competition). Even
with the wall intact, the domestic fleet was overbuilt and the owners inside it went bankrupt (test 1). Fewness inside the
wall did not help: "you can have only two competitors and they’re still terrible businesses, they beat each other’s
brains out" **[M2013-052]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**6. Ask the competitors: the competitor row**, same metric from their own filings (operating income from the 10-K
income statements, XBRL first-filed values of each company's 10-Ks, saved in `Test Runs/_research 2026-10-05 HOS/facts/`;
computed by `span.py`). The whole span, not one year:

| Company (CIK) | Span | Revenue $M | Operating income $M | Margin | Op. income / avg. assets, per year | Cumulative net income $M | Years with an operating loss |
|---|---|---|---|---|---|---|---|
| Old Hornbeck (1131227) | 2009-2019 | 4,214 | 527 | 12.5% | 1.9% | +94, then equity cancelled 2020 | 4 of 11 |
| Helix (866829) | 2013-2025 | 11,461 | 364 | 3.2% | 1.1% | -84 | 5 of 13 |
| Tidewater (98222) | FY2010-FY2025 (the April-December 2017 stub omitted) | 15,064 | 543 | 3.6% | 1.1% | -190 | 7 of 16 |
| SEACOR Marine (1690334) | 2015-2025 | 2,522 | -585 | -23.2% | -5.9% | -568 | 9 of 11 |
| Oceaneering (73756) | 2010-2025 | 38,686 | 2,702 | 7.0% | 6.4% | +1,466 | 3 of 16 |
| TechnipFMC (1681459) | 2017-2025 | 94,014 | 927 | 1.0% | 0.6% | -5,742 | 3 of 9 |

*(Helix's 2013 to 2025 span starts after it sold its oil and gas production arm in 2013. TechnipFMC's span carries the
2018 to 2020 impairments and the 2021 separation of Technip Energies; it is the weakest comparator and is shown because
the brief named it. Oceaneering's NI sum is from its table rows; the others are from `span.py`.)* No company in the row,
over a whole cycle, earned on its assets what the long Treasury pays today. Oceaneering, the robotics comparator and the
best of them, lost operating money in 2018 to 2020 and its equity fell from $2,043M (2013) to $505M (2021). This is an
industry in which "the improvement you get one day, your competitor gets the next day" **[M2004-053]**.

**7. Widening or narrowing; what could destroy it.** The rows ask what could "destroy, or modify, or reduce the economic
strengths" **[M2000-014]**. What destroyed it last time was not a technology but
the customers' spending and the industry's own newbuilds, and both can recur without warning: Hornbeck's FY2019 10-K says
"The principal question facing the offshore oilfield industry is the remaining duration of the current downturn in
offshore activities", and the same filing records that the company "expected generally improved market conditions to
take hold during 2020" before the collapse.
The combination itself is an admission that neither half stood alone well: Hornbeck tried to list in 2023 and 2024 and
postponed (S-1, S-1/A; "Postponed offering costs" of $9.1M in 2024 and $3.7M in 2023, Ex 99.1) and withdrew the
registration on 2026-09-01 (RW, `0001193125-26-377906`).

**The reading.** The castle is shown open on the evidence, not merely unclear: a commodity-like service priced off the
competitor's rate (test 2), sold to customers who tender (test 3), by an owner who is not the low-cost operator (test 4),
inside a statutory wall that did not prevent an overbuilt domestic fleet and a wiped-out equity (tests 1 and 5), in an
industry whose whole-cycle returns sit below the risk-free rate (test 6). "A moat that must be continuously rebuilt will
eventually be no moat at all." **[L2007-005]**; "Business history is filled with "Roman Candles," companies whose moats
proved illusory and were soon crossed." **[L2007-004]**. A low price does not change the box: "What you can’t do is turn
any investment into a good deal by paying little" **[M2019-015]**; "Time is the enemy of the poor business"
**[M1998-006]**.

- **VERDICT: OUT.** The castle is shown open on the evidence, the case the framework sends to OUT rather than to TOO
  HARD (Q2, Why it is a STOP; the rows' boxes are "in, out, and too hard" **[M2006-013]**). The file closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING. **NOT REACHED.**
*(Fact recorded for the record only, no weighing made: old Hornbeck spent about $2.08B of capital in 2009 to 2019
against cumulative operating cash of about $1.02B; the equity that financed the gap was cancelled.)*

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. **NOT REACHED.**
*(The balance sheets were read in Step 0, as the template asks when the file closes before Q4.)*

## Q5 — WHO RUNS IT. **NOT REACHED.**
*(Facts noted, not judged: the CEO of the combined company, Todd M. Hornbeck, founded old Hornbeck in 1997, was its CEO
from 2002 and its chairman from 2005, and led it into the 2020 Chapter 11 in which its shareholders received nothing
(FY2019 10-K, `0001131227-20-000041`; 424B3, Management Following the Mergers). The merger agreement required an
employment agreement and equity awards for him (424B3, Background of the Mergers); Helix's departing CFO and General
Counsel received $300,000 special bonuses each and its CEO an $800,000-a-year consulting agreement (8-K of 2026-09-01,
Item 5.02).)*

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. **NOT REACHED.**
*(Facts noted, not judged: Helix bought Alliance for $112.6M in 2022 plus an earnout of $58.3M paid in 2024, and sold it
for $107.5M in 2026 (10-K FY2022; 10-K FY2025; 10-Q Q2 2026). Helix grew its share count 37% in 2016. The combination was
paid wholly in stock; whether Helix's stock was then above or below its value was not judged, since Q6 was not
reached.)*

## Q7 — WHAT IS IT WORTH? **NOT REACHED.** The figures below are reported at the owner's request.

### COMPUTATION — NOT A CLEARANCE
*No entry language. The file closed OUT at Q2; these numbers answer the owner's three reporting questions and clear
nothing.*

**Owner cash after every real cost**, the combined business rebuilt from both companies' filed cash flow statements
(OCF, less stock pay added back in OCF, less capital spending; $M; `valuation.py`):

| Year | Helix: OCF / SBC / capex | Helix owner cash | Hornbeck: OCF / SBC / net investing | Hornbeck owner cash | **Combined** |
|---|---|---|---|---|---|
| 2021 | 140.1 / 7.7 / 8.3 | 124.1 | 49.6 / 3.4 / 4.1 | 42.1 | **166.2** |
| 2022 | 51.1 / 7.5 / 33.5 | 10.2 | 113.0 / 5.3 / 109.2 | -1.5 | **8.6** |
| 2023 | 152.5 / 6.5 / 19.6 | 126.4 | 146.1 / 19.1 / 168.3 | -41.3 | **85.0** |
| 2024 | 186.0 / 7.3 / 23.3 | 155.5 | 16.5 / 9.4 / 120.0 | -112.9 | **42.5** |
| 2025 | 136.7 / 6.6 / 16.3 | 113.8 | 142.1 / 7.7 / 114.7 | 19.7 | **133.5** |
| **Five-year average** | | 106.0 | | -18.8 | **87.2** |

Sources: Helix 10-K FY2022 (2021, 2022) and FY2025 (2023 to 2025) cash flow statements; Hornbeck S-1 of 2023 (2021,
2022: OCF and net investing as stated in MD&A; SBC from the income statement) and Ex 99.1 (2023 to 2025). Notes:
Hornbeck's 2024 OCF carries $74.4M of paid-in-kind interest accrued in earlier years and paid in cash on refinancing;
Helix's 2024 OCF carries the $58.3M Alliance earnout; the 2022 Alliance purchase price ($112.6M) is left out because the
business was sold in 2026 and its proceeds sit in today's cash. Hornbeck capital spending includes growth (vessel
purchases from the "ECO Acquisitions", MPSV newbuilds); the convention deducts it all.

**The depreciation variant beside it** (the convention's instruction): OCF less SBC less depreciation as the maintenance
proxy (Helix's depreciation excluding certification amortization, $134.5M to $138.4M in 2023 to 2025, and its D&A as
filed for 2021 and 2022; Hornbeck's depreciation excluding drydock amortization, $15.7M to $41.6M): combined average
**$43.8M**. **The maintenance judgment:** the truth sits nearer the depreciation variant or below it. Helix's capital
spending has run at 6% to 23% of its depreciation since 2020 on a fleet that includes a 1987 vessel, and
Hornbeck's depreciation is a fresh-start number that measures the 2020 write-down, not replacement; "merely spending their
depreciation expense will not keep them in the same place" **[M2016-092]** is the railroad case, and these fleets are
the same kind of case in that the charge understates the cost of staying in place.

**Growth shown:** combined owner cash fell from $166.2M (2021) to $133.5M (2025), **-5.3% a year** on the aggregate.
Both end years are ordinary (neither is the 2022 trough), as the rows require: "it will pay you to be suspicious as to
why the beginning and terminal years have been selected" **[L2005-003]**.

**Value range (the Q7 CONVENTION: five-year average, carried at the growth shown for ten years and then at zero nominal
growth, discounted at the 5.63% sovereign; the two ends are the no-growth and shown-growth cases).** Two choices of this
run, confessed: (i) CONVENTION, ours: the owner cash is after interest, so the debt is treated as rolled over and is not
deducted again, while the pro forma cash of **$684.5M** (8-K/A) is added in full; this is generous, since part of the
cash is working cash and $53.8M of debt is current. (ii) CONVENTION, ours: the shares are counted as converted,
325.80M, because the Jones Act Warrants carry a $0.00001 strike.

| Case | Value of the owner cash $M | Plus cash $M | Per share |
|---|---|---|---|
| No growth (the top of the range) | 1,548.5 | 684.5 | **$6.85** |
| Shown growth, -5.3% for ten years then flat (the bottom) | 1,018.6 | 684.5 | **$5.23** |
| *Depreciation variant, no growth (beside)* | 777.9 | 684.5 | *$4.49* |
| *Depreciation variant, shown growth (beside)* | 511.7 | 684.5 | *$3.67* |

- **(a) VALUE RANGE: $5.23 to $6.85 a share against $7.96** (1.3 to 1, well inside the three-to-one width). The price
  sits **above the top** of the range. At $7.96 the as-converted market value less the cash credited is $1,908.9M, and
  the five-year average owner cash of $87.2M is a **4.6%** return on it (2.3% on the depreciation variant), below the
  5.63% bond, before any margin. Under the convention a price above the top closes OUT through the floor: "there’s just
  a point at which we drop out of the game" **[M2003-149]**.
- **(b) FAIR PRICE: about $4.78 a share.** Rule: the price at which the central case (the five-year average owner cash
  of $87.2M at no growth, with the $684.5M of cash credited) returns the floor of about ten percent pre-tax, the floor
  being the framework's Q7 CONVENTION, which takes the speakers' own figure: "we don’t want to buy equities where our real
  expectancy is below 10 percent" **[M2003-149]**. Arithmetic: $87.2M / 10% = $871.8M, plus $684.5M, over 325.80M
  shares. The ten percent is applied to owner cash at the company level (after the companies' own taxes, which were small
  in this span because of losses carried forward); to a taxable corporate holder at the **21%** federal rate the
  after-tax equivalent is about **7.9%**. The fair price sits below the bottom of the range, because the range is
  discounted at 5.63% and the floor asks ten.
- **(c) CHEAP PRICE: about $2.62 a share.** Rule (CONVENTION, ours): one half of the range's bottom ($5.23), so that the
  price is "a big discount from that present value" **[M1997-126]** wide enough that it would survive the owner cash
  being only the depreciation variant ($3.67 at its own bottom) and needs no pencil, "It should scream at you."
  **[M2009-005]**. At $2.62 the pro forma cash alone ($2.10 a share gross, before the debt) would cover four-fifths of
  the price. A cheap price does not reopen a Q2 OUT: "What you can’t do is turn any investment into a good deal by
  paying little" **[M2019-015]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. **NOT REACHED.**
## Q9 — COULD IT RUIN US. **NOT REACHED.**
*(Fact noted, not weighed: pro forma debt $769.2M plus $328.7M of finance and operating lease liabilities, the leases
mostly Helix's chartered Brazil vessels; Hornbeck's second-lien term loans of $448.3M due 2033 amortize $31.6M in 2026
rising to $49.8M in 2030 and carry about $3.4M of cash interest a month (Ex 99.1, Note 10; 8-K/A balance sheet).)*
## Q10 — IS IT THE FAT PITCH. **NOT REACHED.**
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? **NOT REACHED.**

---
## THE BOX
**OUT at Q2.** The castle is shown open on the evidence: a commodity-like vessel and intervention service whose price is
set by fleet supply and by drilling-rig rates, sold by tender to a few oil companies, owned by an operator that says
foreign vessels run at significantly lower cost, behind a statutory wall that did not stop an overbuilt domestic fleet
or the 2020 cancellation of Hornbeck's equity; whole-cycle operating returns on assets of 1% to 2% for both halves and
for Tidewater. Reported at the owner's request, all COMPUTATION: value range **$5.23 to $6.85**, fair price **about
$4.78**, cheap price **about $2.62**, against **$7.96** (aggregator, 2026-10-05). Not TOO HARD: the deciding question is
answered by the record, so no research pass is opened. Q11 belongs to a holding review.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      **Partly.** The template was copied to this dated name before the first fetch (`tools/run.py` and EDGAR came
      after), but the file was written in one pass after the reading, not question by question, and **nothing was
      committed**: the brief for this run forbids commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession
      or names its filing; no number without a row or a filing, except the two CONVENTIONs of this run, labelled.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; Q7's figures
      are headed COMPUTATION — NOT A CLEARANCE and carry no entry language.
- [x] Owner cash after every real cost, from the filed cash flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the issuing authority; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the Foundations list).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): this run is dated today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its share count and market cap were found wrong
      for the merged company and replaced from the S-3ASR and the pro forma note.
- [x] `python tools/check_framework.py` PASS before the commit (run; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a cyclical commodity.** The routing sends to Q1 TOO HARD only a business whose economics cannot be
foreseen "because its industry changes fast". It is silent on a slow-changing industry whose earnings *level* rides a
customer cycle no insider can forecast (Hornbeck's own 10-K could not see 2020). I passed Q1 on the competitive position,
which the record shows, and closed at Q2 OUT; another analyst could close the same file at Q1 TOO HARD (NATURE). Both
close it, but the box differs and the framework should say which. (2) **A merged company has no five-year owner cash.**
The Q7 convention assumes one company with a five-year history; HOS is five weeks old, a reverse acquisition whose
accounting acquirer was private. I summed the two predecessors' filed cash flows year by year; nothing in the text says
whether to do that, to use the accounting acquirer alone, or to use the pro forma statements (which cover only eighteen
months). (3) **The range convention is silent on cash and debt.** Whether owner cash is taken before or after interest,
and whether cash on hand is added, moves the range by about $2 a share here; I confessed my choice. (4) **Penny warrants
and the share count.** The template's share line reads "from the latest filing's cover"; here the cover (pre-merger, and
even the post-merger S-3ASR count) leaves out 103.6M shares behind $0.00001 warrants, 32% of the economic share count.
`cover_shares.py` and `run.py` both undercounted; a rule that counts instruments with a nominal strike as shares would
prevent it. (5) **Negative shown growth.** The convention says growth is carried "never above" what was shown, but not
whether a negative shown rate becomes the range's bottom; I used it. (6) **Fresh-start depreciation.** The depreciation
variant is meant as the conservative case, but after a bankruptcy write-down it is not conservative; the text gives no
instruction for a fresh-start balance sheet.
