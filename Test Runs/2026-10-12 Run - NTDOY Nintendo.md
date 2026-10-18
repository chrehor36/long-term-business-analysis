# Company Run — Nintendo Co., Ltd. (TSE: 7974; US ADS: NTDOY) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Dispatched blind run, resumed after a
usage-limit stop (nothing had been fetched or written before this session but the copied template and the notes file).
Working folder: `Test Runs/_research 2026-10-12 NTDOY/` (scripts in `scripts/`, filings under the ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker; not held.*

**Contamination, declared and not used.** (1) The previous session's notes record that a directory listing of
`Test Runs/` showed a file named "2026-07-14 Test Run - SONY, TBTC, NTDOY.md": not opened, not used. (2) The session's
start-up context showed commit subjects about another company's run (JAPAY) and untracked research-folder names of other
runs (AYI, ARCB) in a git status listing, and memory-index lines about queue state that name no position in this company;
none was opened or used. Nothing else from the blind list was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥8,146 a share, close 2026-10-09, Tokyo Stock Exchange (2026-10-12 was a Tokyo holiday); NTDOY $12.99, close
  2026-10-12. **Aggregator: Yahoo Finance chart API, live quotes only, flagged** (operator rule 5). Cross-check:
  ¥8,146 / 4 / 158.06 (JPY per USD, same aggregator, 2026-10-08) = $12.88, against $12.99 for the ADS.
- **ADS ratio:** one ADS represents one-fourth of one common share. Source: the depositary's Form F-6EF, Citibank N.A.
  for Nintendo Co., Ltd., filed 2022-09-27, accession `0001193805-22-001309` ("each American Depositary Share
  representing the right to receive one-fourth (1/4) of one share of common stock of Nintendo Co., Ltd.").
- **Shares, one class (common):** 1,287,260,000 issued less 134,431,295 treasury = **1,152,828,705 outstanding** at
  2026-03-31 (Annual Report 2026, IV.1(1)(ii) and IV.2(4)). 11,430,000 treasury shares were cancelled effective
  2026-03-31. The Q1 FY2027 release (2026-08-06) gives 134,431,384 treasury at 2026-06-30 and an average of 1,152,828,655
  outstanding for the quarter, the same count to within 100 shares. No share subscription rights or dilutive shares
  ("Diluted profit per share is not noted because the Company has not issued any dilutive shares").
  `python Screens/cover_shares.py NTDOY` returns "NOT AN SEC REGISTRANT"; `python tools/run.py NTDOY` returns "not an SEC
  filer"; the count above is by hand from the report.
- **Market cap:** 1,152,828,705 × ¥8,146 = **¥9,390.9 billion** (about $59.4 billion at 158.06).
- **Sovereign for the earnings currency (yen):** **4.085%**, the 30-year JGB, 2026-10-09, Japan Ministry of Finance,
  `jgbcme.csv` (the issuing authority; fetched 2026-10-12).
- **Filings read** (operator rule 4; Nintendo is not an SEC registrant, so the document and its date stand in place of an
  accession):
  - **Annual Report 2026** for the fiscal year ended 2026-03-31 (the English translation of the Annual Securities Report,
    issued 2026-06-25), `https://www.nintendo.co.jp/ir/pdf/2026/annual2603e.pdf`: description of business, management
    policy, risk factors, management's analysis, shares, dividend policy, the consolidated statements and notes.
  - **Annual Reports 2012 to 2025**, same site (`annualYY03e.pdf`), read for the key financial data, the consolidated
    balance sheets and the cash-flow statements of FY2011 to FY2025, and the management-policy and Wii U passages of the
    2014, 2017 and later reports.
  - **Latest quarterly release:** Consolidated Financial Highlights for the three months ended 2026-06-30, dated
    2026-08-06 (`https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf`).
  - No proxy in the US sense; the report's corporate-governance section is the equivalent and was not read past the
    dividend policy, since the file closed at Q1.
- **One figure cross-checked against the filed statement:** the share count. 1,152,828,705 outstanding against the filed
  net assets per share: (net assets ¥2,955,180m less non-controlling interests ¥1,155m) / ¥2,562.41 = 1,152.83 million
  shares. Agrees. Also: operating profit ¥360,117m in the consolidated statement of income equals the key-data table
  and the MD&A's "¥360.1 billion".
- **Arithmetic** (`scripts/q7.py`, by hand from the cash-flow statements of the reports listed; `tools/run.py` does not
  serve a non-SEC name). Owner cash, millions of yen = operating profit after the statutory tax rate of each year's tax
  note + depreciation − purchase of property, plant, equipment and intangibles ± the change in trade receivables,
  inventories and trade payables as each cash-flow statement states it. Operating profit is before interest income, FX
  and the equity-method share, so this is owner cash before interest (the all-equity basis). Stock pay is restricted
  stock, small, and already expensed in SG&A; there is no goodwill of size and no acquisition spending in the window.

| FY (Mar) | Net sales | Op. profit | after tax | Depr. | Capex | ΔWC | **Owner cash** | % sales |
|---|---|---|---|---|---|---|---|---|
| 2013 | 635,422 | (36,410) | (22,611) | 12,637 | 9,488 | (61,179) | **(80,641)** | (12.7%) |
| 2014 | 571,726 | (46,425) | (28,830) | 9,918 | 19,540 | (1,037) | **(39,489)** | (6.9%) |
| 2015 | 549,780 | 24,770 | 15,977 | 9,011 | 4,582 | 67,564 | **87,970** | 16.0% |
| 2016 | 504,459 | 32,881 | 22,030 | 9,139 | 4,670 | 28,389 | **54,888** | 10.9% |
| 2017 | 489,095 | 29,362 | 20,319 | 8,366 | 10,458 | (14,333) | **3,894** | 0.8% |
| 2018 | 1,055,682 | 177,557 | 122,869 | 9,064 | 9,609 | (46,501) | **75,823** | 7.2% |
| 2019 | 1,200,560 | 249,701 | 173,542 | 9,564 | 10,736 | (51,281) | **121,089** | 10.1% |
| 2020 | 1,308,519 | 352,370 | 244,897 | 9,557 | 9,843 | 8,690 | **253,301** | 19.4% |
| 2021 | 1,758,910 | 640,634 | 445,241 | 10,798 | 7,011 | 28,719 | **477,747** | 27.2% |
| 2022 | 1,695,344 | 592,760 | 411,968 | 10,527 | 7,587 | (51,304) | **363,604** | 21.4% |
| 2023 | 1,601,677 | 504,375 | 350,541 | 11,040 | 22,190 | (5,254) | **334,137** | 20.9% |
| 2024 | 1,671,865 | 528,941 | 367,614 | 17,856 | 16,123 | 86,533 | **455,880** | 27.3% |
| 2025 | 1,164,922 | 282,553 | 196,374 | 15,361 | 19,008 | (248,397) | **(55,670)** | (4.8%) |
| 2026 | 2,313,051 | 360,117 | 250,281 | 15,854 | 27,169 | (22,677) | **216,289** | 9.4% |

  Statutory rates from the reports' tax notes: 37.9% (FY2013 to FY2014), 35.5% (FY2015), 33.0% (FY2016), 30.8% (FY2017
  to FY2018), 30.5% thereafter. Five-year average FY2022 to FY2026: ¥262.8 billion; capex against depreciation runs 1.0
  to 1.7 times, so the maintenance-only case moves the averages by about ¥1 billion (FY2018 to FY2025: ¥253.2 billion all
  spending, ¥254.3 billion maintenance). Earlier operating profit, Annual Report 2012 five-year summary: FY2008 487,220;
  FY2009 555,263; FY2010 356,567; FY2011 171,076; FY2012 (37,320).
- **Equity-method income** (The Pokémon Company and smaller associates; share of profit ¥82.8 billion in FY2026, ¥35.1
  billion in FY2025) is counted as the dividends received (Q4, Equity-method income). The roll-forward of the filed
  "Investments in unconsolidated subsidiaries and associates" (¥192,921m to ¥278,251m in FY2026, against a share of profit
  of ¥82,792m and a share of OCI of ¥2,615m; the same pattern every year from FY2018) shows dividends of about nil to ¥1
  billion a year, so it adds nothing to owner cash. Its carrying value, ¥278.3 billion, is noted beside and not added.

### Q4's balance sheets, read here because the file closes before Q4 (ten year-ends, millions of yen)
**[M2025-032]**: "balance sheets over an 8 or 10 year period before I even look at the income account". From the
consolidated balance sheets of the Annual Reports 2018, 2020, 2022, 2024 and 2026 (each states two year-ends).

| Mar | Cash & deposits | Securities (current) | Investment securities | Receivables | Inventories | Total assets | Trade payables | Total liabilities | Retained earnings | Treasury | Net assets |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 662,763 | 283,307 | 157,963 | 106,054 | 39,129 | 1,468,978 | 104,181 | 218,005 | 1,489,518 | (250,601) | 1,250,972 |
| 2018 | 744,555 | 243,431 | 198,538 | 69,829 | 141,795 | 1,633,748 | 138,015 | 310,173 | 1,564,240 | (250,679) | 1,323,574 |
| 2019 | 844,550 | 238,410 | 167,134 | 78,169 | 135,470 | 1,690,304 | 59,689 | 275,505 | 1,556,881 | (156,755) | 1,414,798 |
| 2020 | 890,402 | 326,382 | 237,710 | 133,051 | 88,994 | 1,934,087 | 98,074 | 393,186 | 1,707,119 | (156,798) | 1,540,900 |
| 2021 | 1,185,151 | 557,238 | 214,832 | 140,570 | 86,817 | 2,446,918 | 114,677 | 572,304 | 1,993,325 | (156,851) | 1,874,614 |
| 2022 | 1,206,506 | 504,385 | 312,663 | 141,087 | 204,183 | 2,662,384 | 150,910 | 593,074 | 2,198,706 | (220,343) | 2,069,310 |
| 2023 | 1,263,666 | 615,699 | 276,253 | 119,932 | 258,628 | 2,854,284 | 149,217 | 587,818 | 2,392,704 | (271,049) | 2,266,466 |
| 2024 | 1,484,350 | 768,355 | 290,620 | 93,608 | 155,987 | 3,151,394 | 58,084 | 546,396 | 2,646,967 | (271,033) | 2,604,998 |
| 2025 | 1,586,275 | 471,915 | 369,373 | 65,180 | 486,428 | 3,398,515 | 201,091 | 673,068 | 2,732,509 | (271,015) | 2,725,446 |
| 2026 | 1,791,802 | 425,054 | 420,875 | 147,485 | 539,804 | 3,805,312 | 236,082 | 850,132 | 2,979,910 | (341,854) | 2,955,180 |

What the figures say. (1) **No borrowings in any year**; the only interest-bearing liabilities at 2026-03-31 are lease
obligations of ¥7,512m (supplemental schedule of borrowings). Liabilities are trade payables, taxes, contract liabilities
(¥174,944m of deferred revenue at 2026-03-31) and provisions. (2) **Cash and securities dominate**: cash and deposits plus
current securities plus non-associate investment securities were ¥1.08 trillion in 2017 and ¥2.36 trillion in 2026,
62% of total assets in 2026; net of the lease obligations, **¥2,351,968m of net cash, ¥2,040 a share**, a quarter of the
price. Of investment securities, ¥278,251m is the equity-method associates and about ¥108,701m listed equity holdings
(fair-value table) in partners such as DeNA and Konami. (3) **Goodwill and intangibles are trivial** (intangibles
¥44,647m in 2026); equity is retained earnings, not purchased assets. (4) **Inventories move with the platform cycle,
not with sales**: ¥39bn at the Wii U's last year-end (2017), ¥142bn in the Switch's first year, ¥87bn at the Switch peak
(2021), then ¥486bn at 2025, before Switch 2, when sales were ¥1,165bn (42% of sales), and ¥540bn at 2026. Raw materials
and supplies were ¥178,874m at 2025 and ¥220,924m at 2026 (inventory note). The 2025 build is the launch stocking the
filer describes ("During the launch periods of new products [...] there may be temporary increases in [...]
inventories"), and it is the largest single swing in the ten years. Receivables are small for the sales (6% to 10%).
(5) **Retained earnings rose from ¥1.49tn to ¥2.98tn** while dividends and buybacks were paid each year (dividends paid
¥1.52tn over FY2017 to FY2026 by the cash-flow statements read; treasury purchases ¥31bn FY2019, ¥95bn FY2022, ¥51bn
FY2023, ¥100bn FY2026). What they do not say: anything about the next platform. A balance sheet this liquid tells the reader that the
company can survive a failed console (it did, FY2012 to FY2017), not whether the next one will earn.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own it "if the market closed for five years"
**[M1997-109]**, for "what the asset, itself, produces" **[M1997-052]**. That bears hard here, because what this asset
produces swings from losses to ¥478 billion of owner cash inside nine years. No macro view, no adviser's projection and
no price movement enters this file. **Contrary evidence, written down as found** **[M1997-127]**: (a) the characters
are forty years old and still sell (Mario Kart World 14.70 million units in its first ten months; Switch software 136.91
million units in FY2026, a platform in its tenth year); (b) the company survived the Wii U years on its own cash with no
borrowing; (c) the company does publish a one-year forecast (FY2027: net sales ¥2,050bn, operating profit ¥370bn,
release of 2026-08-06), so its insiders write down one year; (d) digital sales ¥407.6bn in FY2026, up 25.0%, a steadier
stream than boxed hardware; (e) the speakers treat a consumer product with technology inside as a consumer business
when the customer can be forecast **[M2017-019]**. Each is weighed at Q1 below.

## THE STANDING RULE
The buyer pays cash for a marketable part-interest; no borrowed money, no margin, no option written, so the purchase
itself creates no "sudden demands for large sums" on the buyer. The rule binds the buyer's financing and sizing: "We are
never going to risk what we have and need for what we don't have and don't need." **[M2012-081]**; "borrowed money has
no place in the investor's tool kit" **[L2014-005]**. Nothing about this name puts the buyer at risk of ruin if bought
for cash at a modest size; the target has no debt (Step 0).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence, chosen by me from the report** (the brief's stated departure: no hand-written list). From the
Annual Report 2026's equivalents of Item 1 (I.3 Description of business; II.1 Management policy, management environment,
issues to address), Item 1A (II.3 Risk factors) and Item 7 (II.4 Analysis of financial position, operating results and
cash flow by management, with its part (4), "Factors which have a significant impact on operating results"), and the same
sections of the 2012 to 2025 reports for the cycle: (1) what the business is and where its money comes from; (2) the key
variables and how predictable they were over the last two platform cycles; (3) what the insiders themselves will and will
not write down; (4) whether the forecast is about customers or about technology.

**(1) What it is.** One segment: "dedicated video game platforms" (hardware and software for its own consoles), 96.8% of
FY2026 sales (¥2,239.5bn of ¥2,313.1bn); IP-related income (films, mobile, licensing) ¥73.5bn; 76.9% of sales outside
Japan. Manufacturing is outsourced ("Nintendo commissions outside companies to produce key components and assemble
finished products"). The product, the customer and the distribution are plain. The question is not the product: "we
understand the product. [...] We just don't know the economics of it 10 years from now." **[M2000-104]**

**(2) The key variables, and how predictable they were** **[M1998-044]**: "trying to identify the key variables in that
particular business, and evaluating how predictable they were first". The variables the filer itself names are three:
whether each new platform is adopted ("the presence or lack of hit products and their sales volumes may have a
significant impact on its operating results", II.4(4)); the hardware-software mix ("hardware and software have very
different profit margins", ibid.); and the yen (over 70% of sales abroad, ibid.). The first decides the others, and the
filings show how it moved:

| Platform era | Fiscal years | Operating profit, ¥bn (filed) |
|---|---|---|
| Wii / DS | FY2008 to FY2011 | 487, 555, 357, 171 |
| 3DS / Wii U | FY2012 to FY2017 | (37), (36), (46), 25, 33, 29 |
| Switch | FY2018 to FY2025 | 178, 250, 352, 641, 593, 504, 529, 283 |
| Switch 2 | FY2026, FY2027 forecast | 360, 370 (forecast) |

A reader holding the FY2009 statements, the best year of the Wii, would have forecast nothing like FY2012 to FY2014:
three operating losses on the same characters, the same management tradition and a debt-free balance sheet. The 2014
report gives the cause in the filer's words: the Wii U "business as a whole showed slow growth. The global sales of the
"Wii U" hardware and software reached only 2.72 million and 18.86 million units" (Annual Report 2014, operating results),
and the Wii U hardware "still has a negative impact on Nintendo's profits". A reader holding the FY2017 statements
(operating profit ¥29bn) would equally not have forecast ¥641bn four years later. So test 3 fails on the record: the past
statements did not tell the reader what the future ones would look like **[M2008-033]**; "sometimes the past doesn't
give you any insights into the future" **[M2007-025]**. Test 8, how far off could I be **[M2011-084]**: owner cash in the
fourteen years read ran from minus ¥80.6bn to plus ¥477.7bn (Step 0 table), and the swing was set by one variable, the
adoption of one machine.

**(3) What the insiders write down** (test 5, **[M2000-105]**: "they would not want to put down on paper their
predictions about where 10 companies you would choose in the tech field would be in 10 years, in terms of their
economics"). The filer answers the question for itself, in every report from 2017 to 2026. Annual Report 2026, II.1(2):
"Because Nintendo deals with entertainment products and content that naturally hold many uncertainties in terms of
business operations, we have not set any specific management index targets." Annual Report 2017, II.1(2): "Because we
deal with entertainment products, which by nature hold many uncertainties in terms of their research and development,
and operate in a market which involves intense competition, flexible business decisions are made without being
constrained by any specific management index." The company writes down one year (the FY2027 forecast) and refuses to
write down anything longer. Its risk factors say why: "there is no guarantee that all new products and services will be
accepted by consumers due to ever shifting preferences"; "As development of hardware is time-consuming, with technology
continuously advancing, Nintendo may not be able to readily acquire technologies required for entertainment"; "The
emergence of new competitors resulting from technological innovation could have a significant impact"; "if Nintendo is
unable to adapt to rapid structural changes or other changes, its financial position, operating results and cash flows
could be adversely affected" (II.3(2)). And II.1(3): "The market environment surrounding the Company group continues to
undergo rapid change, driven by the diversification of the entertainment consumers seek, advances in technology and the
resulting intensification of competition."

**(4) Customers or technology** (test 7, **[M2017-019]**, **[M2023-030]**). The strongest case for IN is here, and it is
written down first **[M1997-127]**: the speakers read Apple as "much more of a consumer products business" whose
"prospective customers" can be laid out **[M2017-019]**, and they read Disney by "what place in the mind of billions of
children around the world, and their parents" its characters hold ten years out **[M1996-063]**. Mario, Zelda and Pokémon
hold such a place; the forecast that the characters will still be loved in 2036 is one I would write down. But the
characters are not the cash. The cash comes through a platform each generation of which must be designed, priced and
adopted afresh, at a time set by technology the filer says it may not "readily acquire"; the same characters carried the
Wii U to three years of losses. What must be forecast for FY2027 to FY2036 is the adoption of Switch 2 through its life
and of a successor not yet designed, in a field the filer itself calls one of "rapid change". That is the forecast the
speakers decline: "where we think the future technology could hurt the business as it presently exists [...] it won't
make it through the filter" **[M1998-008]**; "whenever we look at a business and we see lots of change coming, 9 times
out of 10, we're going to pass on that" **[M1999-063]**; "a business that must deal with fast-moving technology is not
going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**. The rows name this kind of
business: "a lot of these businesses are quite dependent on the technology continuing to gallop and do more and more for
people" **[M1999-075]**, and the framework sends such businesses to TOO HARD, "those are the businesses of rapid change"
**[M2001-069]**.

**Weighing the contrary evidence written at the foundations.** (a) Durable characters: real, and they make the business
survivable, not forecastable; the record above is the test. (b) Survival on its own cash: true, and it is a fact for Q9,
not an answer to Q1. (c) The one-year forecast: one year is not ten; the same reports refuse every longer target. (d)
Digital sales: they ride on the installed base of the platform, so they inherit its forecast. (e) The Apple row: the row
itself says "That doesn't mean it's correct. And we'll find out over time." **[M2017-019]**, and a row about one named
company is weighed, never a verdict alone (Q2, A row about one company). Then the doubt rule decides the edge: "if you
have doubts about something being into your circle of competence, it isn't." **[M2002-092]**.

**The routing and the cause.** A business whose ten-year economics cannot be foreseen because its industry changes fast
closes at Q1 in TOO HARD (Q1, The routing, fixed; **[M1998-008]**). The cause is **NATURE**, not WORK: the deciding
question (what Switch 2 and its successor will earn over FY2027 to FY2036) is a forecast the company's own management
declines in writing, every year since 2017 **[M2000-105]**; no filing not yet read could answer it, and more study would
not: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
**[L1993-023]**. Important and unknowable: "If something's important but unknowable, forget it." **[M2006-076]**. It is
no judgment of quality: "It doesn't mean it isn't a good buy. It doesn't mean it isn't selling for a fraction of its
worth. It just means that we don't know how to evaluate it." **[M2000-038]**; and a lower price does not reopen it
(section I, TOO HARD (NATURE)).

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**. Filing facts: operating profit ¥555bn (FY2009), ¥(46)bn (FY2014),
  ¥641bn (FY2021), ¥283bn (FY2025) (Annual Reports 2012, 2016, 2021, 2026, key financial data); "we have not set any
  specific management index targets" (Annual Report 2026, II.1(2)); "the presence or lack of hit products and their sales
  volumes may have a significant impact on its operating results" (II.4(4)).

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). The annual report names no rival (a text search of the 2026 report for Sony, Microsoft,
PlayStation, Xbox, Tencent, Apple, Google and "competitor" finds only the generic "emergence of new competitors" in
II.3), so no competitor row was built; the comparison was not run because the file closed before Q2.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance. The reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8, Q9, Q10, Q12
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** (the ten-year economics turn on the adoption of each new platform, a forecast the
company's own management declines to write down; **[M2000-105]**, **[L1993-023]**, **[M2006-013]**); integrity facts
recorded, not judged. Not reached: Q7, so no range is a clearance; the COMPUTATION below puts the price of ¥8,146 inside a
computed range of ¥7,418 to ¥9,614 a share. No research pass is opened (the cause is NATURE; section I).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; each with its source **[M1997-127]**.)*

**Bearing on Q2 (the castle).** The report names no competitor. Digital sales ¥407.6bn in FY2026, up 25.0%; IP-related
income ¥73.5bn, down 9.7% (II.4(2)(i)). Switch hardware 3.80 million units in its tenth year; Switch 2 19.86 million in its
first ten months (ibid.). The Q1 FY2027 release (2026-08-06) records "the refund of IEEPA tariffs in the US, which were
recorded as cost of sales in prior periods": a tariff cost carried in FY2026 cost of sales and refunded after the year.

**Bearing on Q3 (capital).** Capital spending ¥7.0bn to ¥27.2bn a year over FY2017 to FY2026 against depreciation of
¥8.4bn to ¥17.9bn (Step 0 table); the capital the business ties up is mainly inventory, which swings with the platform
(¥39bn at 2017, ¥540bn at 2026), and the cash pile, which is not needed to operate.

**Bearing on Q4 (the accounts).** FY2026 reported profit attributable ¥424.1bn includes items that are not owner cash
from operations: the equity-method share ¥82.8bn (dividends from associates about nil by the roll-forward), interest
income ¥46.1bn, foreign-exchange gains ¥44.3bn, a gain on sale of investment securities ¥32.7bn, and a loss on litigation
¥6.4bn (consolidated statement of income); operating profit was ¥360.1bn. Inventory valuation losses in cost of sales
¥14.1bn in each of FY2025 and FY2026 (note *1). No adjusted or EBITDA figure was seen in the sections read. The company
publishes a one-year earnings forecast (FY2027: operating profit ¥370bn; "Revisions to previously announced financial
forecast: Not applicable", release of 2026-08-06). By the Q4 convention the guidance habit is recorded as a weighing
against and carried to Q5 **[L2019-006]**; it is carried here unweighed.

**Bearing on Q5 (integrity, recorded, not judged).** (1) The earnings forecast above, the habit Q5 reads with the rest of
the record **[M2004-067]**. (2) The management-policy text declines any "specific management index targets", which a later
reader at Q5 may read as candour about uncertainty. (3) Loss on litigation ¥6,414m in FY2026, its subject not read. The
proxy-equivalent (IV.4 Corporate governance, directors' pay with restricted stock) was not read.

**Bearing on Q6 (the money and the owners).** Dividend policy revised in FY2026 to the higher of 40% of consolidated
operating profit or a 60% consolidated payout (IV.3); dividends paid ¥1.52tn over FY2017 to FY2026. Buyback: 11,430,000
shares bought on the Tokyo Stock Exchange on 2026-03-03 to 2026-03-04 for ¥99,921,060,000, an average of ¥8,742 a share,
under a board resolution of 2026-02-27 capped at 14,000,000 shares and ¥100bn, and cancelled 2026-03-31 (IV.2(2), notes
to the statement of changes in equity). The resolution states a share and money cap, not a price limit. ¥8,742 is above
the bottom of the computed range below (¥7,418); Q6's test of it is not run. 134.4 million treasury shares (10.44% of
issued) are still held. "It is the Company's basic policy to internally provide the capital necessary to fund future
growth [...] and to maintain a strong and liquid financial position in preparation for changes in the business
environment and intensified competition" (IV.3).

**Bearing on Q9 (debt and exposures).** No borrowings; lease obligations ¥7,512m; current ratio 396% (II.4(5)); net cash
¥2,352bn. Dependence on outside manufacturers for key components and assembly, and over 70% of sales in foreign
currencies (II.3).

### COMPUTATION, NOT A CLEARANCE: the two reporting figures (Q7's construction, Part VII)
*(The file closed at Q1. Everything in this subsection is arithmetic for the operator's report, carries no entry
language, and is not a Q7 verdict.)*

- **Cash input.** Owner cash before interest, after the company's tax at the statutory rate (Q7, Whose tax; the company's
  effective rate on operating profit is not separable from untaxed equity-method income, so the statutory rate of each
  year's tax note is used: a CONVENTION of this run, rationale: it taxes the operating profit the business itself earns at
  the rate the filer states, without crediting the equity-method profit that carries no tax). Table in Step 0.
- **Specific (a), the cycle.** The literal window FY2022 to FY2026 ends in the launch year of Switch 2 (sales up 98.6%)
  and contains the trough before it (FY2025, owner cash minus ¥55.7bn on the launch inventory build); the filer describes
  both as launch effects (II.4(5)). Base = the last full platform cycle, FY2018 to FY2025 (the Switch's first full year to
  the year before its successor; peak-to-peak and trough-to-trough are not cleanly defined for a platform business, so the
  cycle is drawn at the platform boundaries, a CONVENTION of this run, rationale: the filer's own description of what
  moves the series is the platform): **average owner cash ¥253.2bn**; maintenance-only case ¥254.3bn (specific (e); the
  difference is immaterial). Literal window beside: ¥262.8bn.
- **Growth.** Between the successive cycle averages, Wii U cycle FY2013 to FY2017 (¥5.3bn) and Switch cycle (¥253.2bn):
  81.2% a year, meaningless on a near-zero base **[L2005-003]**; carried ten years it would require owner cash of about
  ¥96 trillion, far above the highest share of sales the business has earned (27.3%, FY2024), so by specific (f) it is cut
  to the business's own sales growth between the same cycles (15.9% a year: average sales ¥550.1bn to ¥1,432.2bn) and
  capped at the discount rate: **4.085%** **[M1997-095]**, **[M1999-067]**. (The halves of the Switch cycle, FY2018 to
  FY2021 against FY2022 to FY2025, give 4.29%, also capped at 4.085%.) Ten years, then zero nominal growth.
- **Specific (b)** not engaged (no negative growth at cycle level). **(c)** no acquisitions of size in the window. **(d)**
  working capital counted in every year; FY2025's ¥333.8bn inventory build, tied by the filer to launch periods
  generically and not to one named event, stays in the central case; the case at the FY2018 to FY2024 working-capital
  intensity (FY2025 owner cash ¥188.4bn) is shown beside. **(e)** maintenance case as above. **(f)** applied as above.
- **Net cash** (all-equity basis, latest filed balance sheet 2026-03-31; no subsequent event stated that changes it):
  cash and deposits ¥1,791,802m + securities ¥425,054m + investment securities other than associates ¥142,624m − lease
  obligations ¥7,512m = **¥2,351,968m, ¥2,040 a share**. The associates (¥278,251m) are left out, counted only by their
  dividends (Q4, Equity-method income).

| Case (all-equity, ¥ a share) | No growth | 4.085% for ten years | Width |
|---|---|---|---|
| **Central: cycle base FY2018-25, at the sovereign 4.085%** | **7,418** | **9,614** | 1.30 to 1 |
| Beside: literal window FY2022-26 | 7,622 | 9,902 | |
| Beside: FY2025 at prior working-capital intensity | 8,065 | 10,527 | |

- **VALUE RANGE (central): ¥7,418 to ¥9,614 a share, against ¥8,146** (NTDOY: $11.73 to $15.21 an ADS at 158.06 yen and
  four ADS a share, against $12.99). The floor is tested first: the expected return at ¥8,146 is **3.6%** on the
  no-growth case and **5.0%** on the growth case (4.0% and 5.6% on the third line), below about ten percent on every case
  **[M2003-149]**. Had the file reached Q7, it would have closed OUT on the floor before any width test.
- **FAIR PRICE** (each end case valued at ten percent, the two averaged; after the company's own tax; Part VII):
  **¥4,591 a share on the all-equity basis (the central figure)**; **¥2,827 a share on the equity-only basis** beside it
  (owner cash plus the FY2022 to FY2026 average interest and dividend income after tax, ¥27.4bn, with no net cash
  added). In ADS terms $7.26 and $4.47. Beside, on the third line's working-capital case: ¥4,898. No cheap price is
  reported.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the previous session); written question by question; committed after
      Step 0 and after Q1, and after this close (write-early).
- [x] Dispatched: the brief allowed per-question pathspec commits of my two paths only; the lock is the dispatching
      session's; the run binds nothing until folded into the register by that session (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched in this session; the file name
      seen in the previous session and the start-up context items are declared under contamination and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `scripts/check_ids.py`, every quoted fragment beside an id
      found in its row; no E-id. Filing facts carry their document and section (no accession exists for a non-SEC
      filer; the ADS ratio carries the F-6EF accession).
- [x] The order was kept; Q1 failed and closed the file; Q2 to Q12 are NOT REACHED; the arithmetic after the stop is
      headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: built from operating profit, tax, depreciation, capital
      spending and working capital (operator rule 5); the sovereign from the Ministry of Finance; quotes flagged as an
      aggregator's.
- [x] Contrary evidence written down at the foundations before Q1 was decided, and weighed there; facts for later
      questions under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; rows of any year may be cited.
- [x] `tools/run.py` was used for nothing (it refuses a non-SEC name); the arithmetic is by hand in `scripts/q7.py`.
- [x] `python tools/check_framework.py` PASS before the final commit (recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Specific (a) assumes a cycle defined by peaks or troughs of owner cash**, but in a platform business the
natural cycle is the platform's life, and the troughs fall in the year before a launch because inventory is built for
it; the framework does not say whether the cycle is drawn at the platform boundary or at the owner-cash trough, and the
two give different bases (FY2018 to FY2025 here, against FY2017 to FY2025 trough to trough). I drew it at the platform
boundary and confessed it as a CONVENTION of this run. (2) **The growth between successive cycles is meaningless when
the earlier cycle averaged nearly zero** (¥5.3bn); specific (b)'s fallback to the halves of the window is written for a
series that changes sign, not for a near-zero base, so I applied (f)'s cut instead and showed the halves beside; the two
happened to land on the same capped rate, but the text does not say which governs. (3) **Q7, Whose tax, says "after the
company's own income tax"** but gives no instruction for a company whose reported tax is struck on a pre-tax profit
that includes large untaxed equity-method income and interest on cash; owner cash before interest needs a tax on
operating profit alone, which the filer does not state. I used the statutory rate from the tax note and confessed it.
A smaller point: the template's self-audit asks that "every filing fact has its accession", which a non-SEC filer cannot
meet; the document, date and section were recorded instead, as the brief directed.
