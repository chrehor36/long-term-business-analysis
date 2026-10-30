# Company Run — Hitachi Construction Machinery Co., Ltd. (TSE Prime: 6305; ADS HTCMY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (this filer has no
SEC accession numbers); a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
**Copied from the template before any fetch** (commit 9d7a24f1).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (HTCMY; also searched for Hitachi, 6305 and LANDCROS); not held.*

**Dispatched run.** Departures from the canonical brief, stated by the brief itself: (1) the operator chose on 2026-10-10
to run foreign names, so the primary documents are the company's own Annual Securities Reports (English translations)
and Tokyo filings, not SEC filings; (2) the lines of evidence were derived by the analyst, not handed down (see Step 0).

**Contamination, declared.** (a) Before any fetch, a filtered listing of `Test Runs/` (for "htcmy", "6305", "hitachi")
returned one file name, `2026-07-15 Run - HTCMY (Hitachi Construction Machinery).md`. It was not opened and nothing of it
is used; I know only that a run of this name was dated 2026-07-15. (b) A misdirected download command listed the
repository root, which showed the file name `PORTFOLIO.md` (not opened, nothing seen of its contents). (c) The session's
loaded memory index says Japanese names were owed runs; it names no company. Nothing else of any blind-listed file was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥5,606 (Tokyo Stock Exchange close, 2026-10-13; Yahoo Finance chart API, an **aggregator, flagged**, used for
  the live quote only, operator rule 5). No ADS price is stated, so the F-6 ratio is not needed.
- **Shares:** issued 215,115,038 (62nd-term Annual Securities Report, filed with the Director, Kanto Local Finance Bureau,
  June 23, 2026, "Issued shares"; and the Q1 FY2026 Kessan Tanshin, July 30, 2026); treasury shares 2,354,657 at June 30,
  2026 (Kessan Tanshin, item (3)[2]); less 5,999,100 shares repurchased August 19 to October 8, 2026 (company notices of
  September 4, October 2 and October 9, 2026: 4,408,900 + 978,000 + 612,200; cumulative ¥33,999,921,700). **Shares
  outstanding: 206,761,281.** One class (common). `python Screens/cover_shares.py HTCMY` returned "NOT AN SEC REGISTRANT in
  the live ticker file"; the count is taken from the company's own documents, as the brief directs.
- **Market cap:** ¥1,159,104M (206,761,281 × ¥5,606).
- **Sovereign for the earnings currency (JPY):** **4.085%**, the 30-year JGB, Japan Ministry of Finance `jgbcme.csv`, row
  dated 2026/10/9 (the latest row in the file fetched 2026-10-13; issuing authority).
- **Filings read** (operator rule 4; documents and dates in place of accession numbers):
  - Annual Securities Reports (Yukashoken Hokokusho), English translations from the IR library: **62nd term** (FY April 2025
    to March 2026, filed June 23, 2026, Kanto Local Finance Bureau) read for Description of Business, Business Risks,
    Management Analysis, Important Contracts, shares, the statements and the notes; **53rd to 61st terms** read for the
    statements of financial position, income and cash flows, the segment notes and the notes named below.
  - Q1 FY2026 Consolidated Financial Results (Kessan Tanshin), July 30, 2026 (balance sheet at June 30, 2026, forecast).
  - Company notices (TSE timely disclosure, English): February 19, 2026 (ITOCHU, HCJI); August 19, 2026 (three: Hitachi,
    Ltd.'s sale of 21,462,310 shares; the repurchase resolution; the change in major shareholder); September 4, October 2,
    October 9, 2026 (repurchase status and completion); May 25, 2026 (name change).
  - No proxy in the U.S. sense; the 62nd report's Corporate Governance section is its equivalent and was not reached.
- **One figure cross-checked against the filed statement:** total assets ¥1,857,321M at March 31, 2026 in the 62nd report's
  consolidated statement of financial position equals the March 31, 2026 column of the Kessan Tanshin balance sheet; and
  net cash from operating activities ¥164,223M appears identically in the 62nd report's five-year table and its cash-flow
  statement. **A discrepancy found and resolved:** the 59th report's cash-flow table prints ¥(53,479)M on the capital
  expenditure line for FY ended March 2023; the same report's management analysis says "an outlay of ¥52,839 million for
  capital expenditures", and the 60th report's restated table says ¥(52,839)M. ¥52,839M is used; ¥53,479M is the ACME
  guarantee payment, misplaced in the translation's table.
- `python tools/run.py HTCMY` returned "not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." No arithmetic line was
  produced; every figure below is from the company's filed documents, computed in the research folder
  (`owner_cash.py`, `returns.py`, `valuation.py`, each with its output file).

**The lines of evidence, chosen and why.** The Annual Securities Report's equivalents of a 10-K's Items 1, 1A and 7 are
"Description of Business" (two segments: Construction Machinery, 90% of revenue; Specialized Parts and Service, Bradken
and H-E Parts), "Business Risks" (thirteen items; the first five are market conditions with "a decline in selling prices
caused by intensified competition", exchange rates, interest rates and pensions, procurement and tariffs, and credit on
installment sales and finance leases) and "Management Analysis" (results, cash flows, the medium-term plan against its
targets). From them I chose five lines: (1) the cycle: global hydraulic-excavator demand ("250,000 units in FY2022 to
234,000 units in FY2025") and the company's revenue and margin through a full cycle; (2) the competitive position: price
competition, the rebuilt Americas business after the Deere joint venture ended, and the field leader's returns; (3) cash
conversion: owner cash against reported earnings, since the five-year table shows operating cash ranging from ¥(26,135)M to
¥164,223M against steady profits; (4) capital and control: the HCJI/ITOCHU and Hitachi, Ltd. holdings, the 2026 repurchase,
the ¥500 billion growth-investment plan; (5) the exposures: the ACME guarantee, sales finance, the engine-certification
compensation, tariffs. The whole last cycle is covered by the 53rd to 62nd terms (FY April 2016 to March 2026).

**Ten years of balance sheets, read before the income account** **[M2025-032]** (Q4's line; the file closes before Q4, so
they are read here). Millions of yen, March 31 (June 30 for 2026Q1); receivables are current plus non-current trade
receivables; debt is bonds and borrowings; leases (IFRS 16 from FY2019) shown separately.

| Mar 31 | Cash | Receivables | Inventories | PP&E | Goodwill + intangibles | Debt | Leases | Equity (parent) | NCI | Total assets |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 79,110 | 206,053 | 248,564 | 276,293 | 18,305 | 217,895 | n/a | 395,963 | 60,853 | 926,628 |
| 2017 | 65,455 | 215,739 | 235,522 | 297,843 | 76,728 | 248,701 | n/a | 399,619 | 50,811 | 1,012,208 |
| 2018 | 81,929 | 260,991 | 255,623 | 299,987 | 72,764 | 230,665 | n/a | 448,502 | 56,528 | 1,089,796 |
| 2019 | 67,347 | 280,521 | 324,844 | 311,245 | 76,656 | 304,808 | n/a | 486,407 | 56,254 | 1,185,256 |
| 2020 | 62,165 | 247,415 | 301,222 | 315,465 | 68,421 | 338,943 | 60,791 | 473,537 | 51,574 | 1,167,567 |
| 2021 | 80,330 | 247,807 | 297,766 | 345,847 | 76,007 | 329,488 | 59,431 | 513,602 | 54,954 | 1,219,882 |
| 2022 | 94,257 | 304,195 | 368,267 | 384,164 | 81,079 | 353,107 | 61,431 | 611,608 | 56,323 | 1,409,560 |
| 2023 | 111,992 | 340,349 | 450,782 | 417,077 | 80,125 | 507,467 | 71,798 | 659,992 | 41,048 | 1,627,003 |
| 2024 | 143,530 | 352,375 | 552,319 | 465,609 | 101,901 | 575,582 | 74,242 | 763,380 | 51,033 | 1,835,672 |
| 2025 | 147,136 | 317,906 | 531,183 | 486,031 | 105,243 | 537,858 | 72,565 | 809,337 | 48,615 | 1,791,006 |
| 2026 | 141,456 | 342,570 | 541,224 | 492,584 | 112,859 | 497,566 | 70,969 | 900,166 | 55,504 | 1,857,321 |
| 2026 Jun 30 | 130,831 | 299,267 | 582,504 | 500,030 | 115,685 | 498,549 | 73,684 | 920,647 | 58,748 | 1,880,790 |

(Sources: statements of financial position of the 53rd to 62nd reports, the later restated figure used where two differ
(2017 inventories and intangibles after Bradken's purchase-price allocation; 2021 intangibles, equity and total assets as
restated in the 58th report; 2024 PP&E and goodwill after ACME's); June
2026 from the Kessan Tanshin.)

What the figures say. **Inventories have outgrown sales:** 33% of revenue at March 2016 (248,564 on 758,331), 31% at March
2019, 37% at March 2021, 39% at March 2024 (552,319 on 1,405,928), 38.5% at March 2026 (541,224 on 1,405,493), and higher again at June 2026 (582,504);
the filer explains the rise by its own distribution in the Americas after the Deere joint venture and dealer inventory,
and twice reduced inventories (FY2024, FY2025) to raise operating cash. Inventories "out of line, you know, with sales and,
particularly, the trend of them" is the tell **[M1995-064]**; here the trend has a stated business cause, and I record it
as a fact, not a suspicion. **Debt more than doubled** (217,895 to 497,566) while equity rose 504,203 (retained earnings
222,721 to 614,725, plus ¥130,998M of accumulated other comprehensive income at March 2026, mostly translation gains from
a weaker yen). **Goodwill and intangibles rose six-fold** (18,305 to 112,859): Bradken and H-E Parts (2016 to 2017), ACME
(2024), Brake Supply (December 2024). **Receivables** rose 66% against revenue up 85%. **Other financial assets
(non-current)** jumped to 73,391 at March 2023: the ¥51,330M indemnity claim against ACME after the company paid ¥53,479M
as guarantor of an affiliate's bank loans (59th report, notes 18 and 27), resolved in March 2024 by taking ACME over (60th
report, business combinations: assets 52,973, liabilities 63,201, goodwill 10,400). What the balance sheets do not say:
how much of the debt finances customer receivables (installment and lease) rather than the factories; the reports give
lease receivables (43,244 and 38,137 at March 2023 and 2024) but no captive-finance balance sheet.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, so the question is the excavator business, not the 2026 share-price moves around Hitachi, Ltd.'s exit. The
market serves: "It just tells us prices." **[M2006-077]**. No macro enters: the yen, U.S. tariffs and the Middle East fill
the filer's own explanations, and "macro conclusions are — just never enter into the discussion" **[M2000-094]**; they are
read only as properties of the business (how much of its growth is translation). Who is paid to tell you: the filer's own
"LANDCROS 2028" plan ("one of the top three in the industry by 2030") is a projection, and "we’ve never looked at a
projection in connection with either a security we’ve bought or a business we’ve bought" **[M1995-050]**. Margin of
safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.

**Contrary evidence, written down as found** **[M1997-127]**, looking for "what’s wrong in things" **[M2025-013]**:
(1) owner cash after every real cost averaged about ¥20bn a year (all-equity, after acquisitions) over FY2021 to FY2025
against net income to the parent averaging about ¥79bn; the earnings went into inventories, receivables and the rental
fleet; (2) inventories rose from about a third of revenue to 39%; (3) a ¥53,479M guarantee payment for an affiliate in
FY2022, ending in the takeover of a U.S. rental company; (4) the field's leader (Caterpillar) earned operating margins
averaging 13.7% over 2016 to 2025 against this company's 8.8%; (5) the Hitachi name is being given up (LANDCROS
Corporation from April 2027) and Hitachi, Ltd. sold its last 21,462,310 shares in August 2026, the company spending
¥34.0bn of its cash to absorb the sale; (6) the new plan seeks "approximately ¥500 billion in funding for growth
investments by generating stable operating cash flow and strategically utilizing financial leverage", with "inorganic
growth"; (7) the medium-term targets were missed (ROE 8.6% against "over 13%"). For the business, in fairness: record
revenue, a parts and service business the filer calls steady, net debt to equity brought to 0.40, operating cash of
¥143,932M and ¥164,223M in the last two years.

## THE STANDING RULE
A cash purchase of a listed share, unlevered and sized within means, puts the buyer at no risk of ruin; "borrowed money has
no place in the investor's tool kit" **[L2014-005]**, and the rule is "We are never going to risk what we have and need for
what we don’t have and don’t need." **[M2012-081]**. No question here; the target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "the first question is, can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the
  earning power and competitive position will look like in five or 10 years" **[M2012-065]**.
- **What it is.** A manufacturer of hydraulic excavators (mini to ultra-large), wheel loaders and mining dump trucks, with
  their parts and service, sold through about 300 dealers, about 90% of revenue (Construction Machinery segment, ¥1,268,519M
  of ¥1,405,493M in FY2025); plus Bradken (wear parts and mill liners for mines) and H-E Parts (mining service), the other
  10% (62nd report, Description of Business and segment note). No single customer exceeds 10% of sales.
- **The key variables and how predictable they are** **[M1998-044]**: (1) global excavator demand, which is cyclical and not
  forecastable year to year (250,000 units in FY2022, 234,000 in FY2025, per the filer) but whose economics over a cycle are
  on the record: ten years of filed results show revenue between ¥753,947M and ¥1,405,928M and operating margins between
  3.1% and 11.6%; (2) the company's position against Caterpillar, Komatsu and the Chinese makers, which is Q2's question;
  (3) price against cost (steel, tariffs), which the filer reports each year; (4) the share of parts and service in revenue,
  which the filer calls steady; (5) the yen, a translation effect visible in the accounts. These are "important and knowable"
  **[M2006-076]**.
- **Do the past statements tell me the future ones?** **[M2008-033]** Yes, in the sense that matters: the ten years of
  statements show a pattern (cyclical revenue, a mid-single to low-double-digit margin, earnings absorbed by working
  capital and the rental fleet) that the structure of the business explains and that is likely to recur. The one break in
  comparability, the Americas after the Deere joint venture ended (agreed August 2021), is now four years old and visible
  in the figures.
- **Technology and change.** The product is not fast-moving technology; electrification and autonomous haulage are
  coming in mining (the filer's battery dump truck aims at commercial sale in FY2027), but on the filer's own account they
  are extensions of the existing machines, not a replacement of the business. It is not a business where "the future
  technology could hurt the business as it presently exists" in the sense of **[M1998-008]**; the industry insiders would
  write down where excavator demand and margins stand in ten years in broad terms, unlike the tech field of **[M2000-105]**.
- **Understanding the economics, not the hydraulics.** "I never would understand the chemistry of it, but I — but that’s
  not necessarily vital. What is important is that I understand the economic dynamics of the industry." **[M2011-014]**.
  The economic dynamics here (a capital goods cycle, dealer channels, an installed base that buys parts) are readable from
  the filings.
- **Abroad.** A Japanese company under IFRS with a nominating-committee board; I understand "the nuances of the corporate
  governance system and taxation" well enough to read its filed reports **[M2000-141]** (statutory tax rate 30.6%, effective
  rate about 33%).
- **Routing.** Not a bank, not a holding company. The parts: Construction Machinery carries 91.3% of five-year segment
  profit (FY2021 to FY2025: ¥629,841M of ¥689,819M), so it "matters" under the business-of-parts paragraph and is read here;
  it is understood by the tests above. Specialized Parts and Service does not decide.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. My
  doubts about this name are about the castle and the cash, which are Q2 and Q3 questions, not about whether its economics
  can be foreseen from its figures.
- **VERDICT: IN.** The economics of a cyclical heavy-machinery maker are readable from ten years of filed statements and
  the key variables are knowable **[M2012-065]**, **[M2006-076]**, **[M2008-033]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The standard: "A
truly great business must have an enduring "moat" that protects excellent returns on invested capital." **[L2007-004]**.

**The parts table** (segment profit is operating income; 58th to 62nd reports, segment notes):

| Part | FY2021 to FY2025 segment profit | Share | Castle | Decides |
|---|---|---|---|---|
| Construction Machinery (excavators, wheel loaders, mining machines, their parts and service) | ¥629,841M | 91.3% | read below | **yes** (more than half) |
| Specialized Parts and Service (Bradken, H-E Parts) | ¥59,978M | 8.7% | the filer reports "reduced investment by some major customers and intensifying competition" (FY2025) and "intensifying competitive conditions" (Q1 FY2026); segment profit ¥10,858M on ¥145,226M revenue in FY2025 | no |

**The castle tests, on Construction Machinery, each with its filing fact.**
- **What keeps it standing.** On the filer's account: "Japan-originated manufacturing capability", a "sales and service
  capability" of "approximately 300 dealers and around 9,000 mechanics worldwide", the machines in operation that buy parts,
  and the mining machines (62nd report, Management Policy). These are real, and the parts business on an installed base is
  the strongest of them. How permanent: the Americas channel had to be rebuilt from 2022 after the Deere joint venture ended
  (the filer still supplies Deere excavators under an OEM contract running "Five years from March 1, 2022, extendable upon
  request of the counterparty", 62nd report, Important Contracts, and reports "a decline in sales in the Americas OEM
  business" in FY2025); and the name customers know is being given up for LANDCROS in April 2027 (notice of May 25, 2026),
  with Hitachi, Ltd. gone as a shareholder since August 19, 2026.
- **The money test.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?
  [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The filer answers for its own field: its first
  business risk is "a decline in selling prices caused by intensified competition", and its plan says "Amid an increasingly
  challenging competitive environment, expanding our business scale is essential to achieve autonomous and sustainable
  growth". A management that says it must grow larger to sustain itself is describing a castle the attackers are reaching.
  "We have found in a long life that one competitor is frequently enough to ruin a business." **[M2012-108]**.
- **Pricing power.** The filer raised prices in FY2023, FY2024 and FY2025 ("an increase in sales prices contributed to higher
  profits" in FY2025), yet the operating margin fell from 11.6% (FY2023) to 9.3% (FY2025) because "the impact of U.S.
  tariffs, rising costs associated with growth investments, and a deterioration in regional and product mix acted as
  downward factors". The price rises did not carry the costs; "you can almost measure the strength of a business over time
  by the agony they go through in determining whether a price increase can be sustained" **[M2005-020]**.
- **The low-cost position.** Where customers set a maker's price against its rivals', "being the low-cost producer is
  all-important" **[L2000-017]**, and "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. The
  cost position is read from the producers' own filings, "we would measure it, probably, more by cost of production"
  **[M2006-004]**: operating margin, the same metric from each filer, shows the company below the field's leader in eight of
  ten years (table below). It is not the low-cost operator.
- **The customer and the low bid.** Contractors, rental fleets and miners buy capital equipment against competing bids; the
  filer's own risk text names the selling price as what competition attacks. Nothing in the filings shows customers paying
  up for the name, which is about to change. The test, "would people still want to be both eating and giving away that
  candy in preference to other candies?" **[M2017-009]**, is not answered in the company's favour by any filing fact I found.
- **Widening or narrowing.** "how wide the moat is and whether it’s likely to widen further or shrink on you" **[M1999-108]**.
  After-tax return on capital at the last two peaks: 10.3% (FY2017) and 9.6% (FY2023); operating margin at the same peaks:
  10.0% and 11.6%. Neither widening nor clearly narrowing; level, at an ordinary height.
- **What could reduce it, five to fifteen years out** **[M2000-014]**: the end or non-renewal of the Deere supply contract
  after February 2027; the brand change; the Chinese makers (not named in the filings; see the competitor row).
- **Ask the competitors.** Not possible from filings; not done.

**The competitor row.** The company's reports name no rival: a search of the 53rd to 62nd reports for Caterpillar, Komatsu,
Sany, XCMG, Volvo, Kobelco, Liebherr and "competitor" found none by name. The comparison is therefore taken from the field's
leader in excavators and mining machines that files with the SEC (Caterpillar), the company's former joint-venture partner
and present OEM customer, named in its own Important Contracts, that files with the SEC (Deere), and one more SEC filer in
construction equipment (CNH Industrial); the last two are dominated by agricultural machinery and are shown for
completeness only. **Komatsu, Volvo Construction Equipment, Sany, XCMG, Kobelco and Liebherr do not file with the SEC
(flagged; not read).** Rival figures are from SEC XBRL company facts (tagged data, a transcription; latest 10-Ks: CAT
0000018230-26-000008, DE 0001104659-25-122321, CNH 0001567094-26-000006). Calendar years for CAT and CNH, October or
November years for DE, April-to-March years for the company (labelled by the year they start).

| Year | HCM operating margin | CAT operating margin | DE pre-tax margin | CNH pre-tax margin |
|---|---|---|---|---|
| 2016 | 3.1% | 3.0% | 8.3% | -0.1% |
| 2017 | 10.0% | 9.8% | 10.6% | 2.4% |
| 2018 | 9.9% | 15.2% | 10.9% | 4.9% |
| 2019 | 7.8% | 15.4% | 10.4% | 4.2% |
| 2020 | 3.5% | 10.9% | 10.9% | -1.2% |
| 2021 | 10.4% | 13.5% | 17.3% | 9.9% |
| 2022 | 10.7% | 13.3% | 17.4% | 11.4% |
| 2023 | 11.6% | 19.3% | 21.3% | 10.9% |
| 2024 | 11.3% | 20.2% | 17.8% | 7.3% |
| 2025 | 9.3% | 16.5% | 13.7% | 3.4% |
| **Ten-year average** | **8.8%** | **13.7%** | **13.9%** | **5.3%** |

**The field's returns over the last full cycle.** The company's revenue ran trough (FY2016, ¥753,947M) to peak (FY2018,
¥1,033,703M) to trough (FY2020, ¥813,331M) to a higher plateau (FY2023 to FY2025, about ¥1.4 trillion, much of it a weaker
yen). Over those ten years its after-tax operating return on capital employed (equity plus borrowings less cash) averaged
**7.5%**, 8.2% on tangible capital, never above 10.3% in any year and as low as 2.4% (`returns.py`); return on equity was
8.6% in FY2025 against the plan's "over 13%". Caterpillar's operating margin averaged 13.7% over the same decade, more than
half as much again. The leader's returns show the field is not ordinary; this castle's returns are. The rows' second
question, "Has it earned high returns on capital?" **[M1995-051]**, is answered no over a full cycle.

**Judged in words, as the rows ask** **[M1999-108]**: a standing castle, with a real installed base, a dealer network and a
mining franchise, that has protected only ordinary returns through a full cycle, in a field whose leader earns far more and
whose low-cost producer it is not, while its own management describes price competition and the need for scale. The
returns are known from the filings, so the tenuous-moat reason for TOO HARD, "We don’t know how to valuate that"
**[M2000-019]**, does not apply: the castle is not unknown, it is shown to protect ordinary returns. Under the list of what Q2
rules OUT (the standing castle that protects only ordinary returns; the high-cost producer in a commodity field), and since
the deciding part decides the file under the business-of-parts paragraph, the box is OUT. A row about one named business in
this very industry exists, "There was never any cash. Just more used construction equipment. We tend to hate businesses
like that." **[M2008-036]**; under Q2's convention on rows about one company it is not used as a verdict here, and the box is
decided on the tests and the filings above.

- **VERDICT: OUT.** The deciding part's castle protects ordinary returns over a full cycle (after-tax return on capital 7.5%
  average, FY2016 to FY2025), it is not the low-cost operator (operating margin below the leader's in eight of ten years),
  and the filer itself reports price competition **[L2007-004]**, **[M1997-010]**, **[M2011-015]**, **[M2006-013]**.
  Questions Q3 to Q12 are NOT REACHED; what was already found is written under AFTER THE STOP, and the Q7 figures the
  owner asked for are a COMPUTATION, NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten years of balance sheets were read in Step 0; other facts are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts, including the buyback against the bottom of the computed range, are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed below under **COMPUTATION, NOT A CLEARANCE**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Nothing in the filings places the business among the named ones.)

---
## COMPUTATION, NOT A CLEARANCE: the value range and the fair price (the owner's reporting figures)
*Computed beneath a closing STOP at Q2. These figures decide nothing, carry no entry language, and are not a verdict
(operator rule 3). Scripts and outputs: `owner_cash.py`, `valuation.py`, `owner_cash_out.txt`, `valuation_out.txt` in the
research folder.*

**Owner cash after every real cost** (operating cash, less capital expenditure net of disposal proceeds, intangible assets,
lease principal paid, and distributions to non-controlling interests; acquisitions shown separately; the all-equity
figure adds back net interest paid after the 30.6% statutory rate). Millions of yen; FY starting April.

| FY | Operating cash | Net capex + intangibles | Lease principal | To NCI | Owner cash, equity | Owner cash, all-equity | Acquisitions, net | All-equity after acquisitions | Revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 87,961 | 15,305 | 5,556 | 7,862 | 59,238 | 59,905 | 59,877 | 28 | 753,947 |
| 2017 | 84,528 | 16,748 | 4,700 | 2,103 | 60,977 | 62,740 | 20,947 | 41,793 | 959,153 |
| 2018 | (25,693) | 29,516 | 6,388 | 4,933 | (66,530) | (64,565) | 997 | (65,562) | 1,033,703 |
| 2019 | 22,682 | 36,404 | 12,770 | 5,544 | (32,036) | (28,679) | (1,635) | (27,044) | 931,347 |
| 2020 | 91,339 | 32,815 | 11,534 | 4,255 | 42,735 | 44,977 | (569) | 45,546 | 813,331 |
| 2021 | 39,317 | 25,617 | 12,699 | 8,857 | (7,856) | (5,802) | (18,920) | 13,118 | 1,024,961 |
| 2022 | 27,344 * | 47,201 | 11,745 | 9,316 | (40,918) | (36,713) | 68,311 * | (105,024) | 1,264,927 |
| 2023 | 73,035 | 54,887 | 12,890 | 6,747 | (1,489) | 6,436 | (15,289) | 21,725 | 1,405,928 |
| 2024 | 143,932 | 42,762 | 15,040 | 9,213 | 76,917 | 85,757 | 13,719 | 72,038 | 1,371,285 |
| 2025 | 164,223 | 47,865 | 13,479 | 10,574 | 92,305 | 99,543 | (861) | 100,404 | 1,405,493 |

\* FY2022: the ¥53,479M paid as guarantor of ACME's loans is moved from operating cash to acquisitions, since it ended in
the purchase of ACME (60th report, business combinations); it is deducted either way in the default pair. Operating cash
includes the rental fleet ("other property, plant and equipment [...] principally operating assets for leasing", 62nd
report note 10), bought at ¥82,249M (FY2024) and ¥64,417M (FY2025) outside the capital-expenditure line.

**The inputs.** Long government rate 4.085% (MOF, 2026/10/9). Shares 206,761,281. Net debt on the all-equity basis: bonds
and borrowings ¥498,549M less cash ¥130,831M at June 30, 2026 (the latest filed balance sheet) = ¥367,718M, **plus
¥33,999.9M** paid for the 5,999,100 shares repurchased after that date (CONVENTION of this run: the share count already
reflects the repurchase, so the cash that bought it is added; rationale: both sides of the per-share figure at one date).
Lease liabilities (¥73,684M) are left out because lease principal is charged in owner cash, and said so. Net debt used:
**¥401,718M**. Enterprise value at the price: ¥1,560,822M.

**The range, built by Q7's convention in full.**
- *Base:* the last five years, FY2021 to FY2025. (a) Neither end year is aberrational on the filer's own description; the
  one aberration inside the window (the ACME guarantee) is moved to acquisitions. The ten-year average (two cycles) is shown
  beside.
- *All spending deducted, the literal window, acquisitions deducted* (specifics (c) default pair, (d) working capital
  counted): owner cash, all-equity, after acquisitions averaged **¥20,452M**. (b) The series changes sign (13,118;
  (105,024); 21,725; 72,038; 100,404); the halves of the window (first two years averaging ¥(45,953)M, last two ¥86,221M)
  also change sign, so the growth is meaningless and this leg is the no-growth case alone, said so. Aggregate, not per share
  (PG specific 1).
- *Not a serial acquirer:* net purchases over the window ¥46,960M against half of owner cash before purchases (¥149,221M,
  half ¥74,611M). No signed, unclosed acquisition was found; the planned sale of ECCO Equipment Company, LLC (a divestiture,
  62nd report note 20) is not valued. The organic pair is shown beside.
- *(e) The maintenance case:* the filer states no maintenance figure; the rows' proxy is taken, "the depreciation charge is
  not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**, as a disclosed
  guess **[M2000-144]**: net income to the parent, the equity-method share replaced by the dividends received (Q4's
  convention), with net interest after tax added back for the all-equity basis: FY2021 to FY2025 73,135; 81,065; 99,105;
  88,701; 79,432; average **¥84,288M**. This is the maintenance-only case the specific orders, shown beside the owner-cash
  figure, not a net-income proxy for owner cash (operator rule 5): the owner cash is the bottom of the range.
- *The growth bought was worth less than its cost.* Growth spending (the gap between the maintenance case and owner cash
  before acquisitions) totalled about ¥272,217M over the five years, and the maintenance-case earnings rose by ¥6,297M a year
  (73,135 to 79,432), about 2.3% on the spending, below the 4.085% long rate. So, by (e), the maintenance-only no-growth case
  is the **top** and the all-spending case the **bottom**; "growth can destroy value if it requires cash inputs in the early
  years [...] that exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**.
  (f) No growth is carried on either end, so the cap does not bind; zero growth after year ten (PG specific 3) is moot.

| Case | Owner cash a year | Value at 4.085% | Less net debt | Per share | Return at the price |
|---|---|---|---|---|---|
| Bottom: all spending, no growth | ¥20,452M | ¥500,666M | ¥98,948M | **¥479** | 1.31% |
| Top: maintenance only, no growth | ¥84,288M | ¥2,063,347M | ¥1,661,629M | **¥8,036** | 5.40% |
| Beside: ten-year average, all spending after acquisitions | ¥9,702M | | | ¥(794) | |
| Beside: organic pair, literal window, before acquisitions | ¥29,844M | | | ¥1,591 | |

**VALUE RANGE (a): ¥479 to ¥8,036 a share (all-equity basis), against ¥5,606.** The floor is tested first: at the price no
case earns about ten percent (the top case returns 5.40% on the enterprise value), so had Q7 been reached it would close
**OUT whatever the width** ("there’s just a point at which we drop out of the game" **[M2003-149]**). The width is 4.1 to
one on business value (above the three-to-one convention), which does not matter once the floor fails.

**FAIR PRICE (b), a reporting convention and never a verdict (Part VII):** each end valued at ten percent and the two
averaged, after the company's own tax. **All-equity (the central figure): ¥590 a share** (bottom end ¥(954), top end
¥2,134). **Equity-only, beside: ¥2,240 a share** (owner cash after interest, ¥14,400M bottom and ¥78,235M top, against the
market value alone; it never decides alone). For the record, with the filed net debt only (repurchase cash not added):
¥754. Against the price of ¥5,606. No other price figure is reported.

---
## THE BOX
**OUT at Q2** (the deciding part's castle protects only ordinary returns over a full cycle: after-tax return on capital
7.5% average FY2016 to FY2025; not the low-cost operator; the filer reports price competition). Integrity facts recorded,
not judged. COMPUTATION beneath the stop: value range ¥479 to ¥8,036 a share against ¥5,606 (no case earns the floor at
the price); fair price ¥590 all-equity, ¥2,240 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; not weighed; no verdict; the box unchanged (operator rule 2).*

**Q3 (capital).** Owner cash after every real cost averaged ¥20,452M a year (all-equity, after acquisitions) over FY2021 to
FY2025 and ¥9,702M over ten years, against net income to the parent averaging ¥78,783M over the five; the difference went
into inventories (¥297,766M at March 2021 to ¥541,224M at March 2026), receivables and the rental fleet. After-tax return on
capital employed 2.4% to 10.3%, average 7.5% (`returns.py`). The growth spending of FY2021 to FY2025 earned about 2.3% on
its cost (computation above). Row about one named business in this industry, recorded for the later question it bears on,
not weighed: "There was never any cash. Just more used construction equipment." **[M2008-036]**.

**Q4 (the accounts).** Balance sheets: Step 0. The filer features "adjusted operating income" ("calculated by subtracting
the sum of cost of sales and selling, general and administrative expenses from revenue") as its performance indicator; it
excludes other income and expenses, which in FY2025 netted to ¥(2,807)M (adjusted ¥132,951M, operating income ¥130,144M) and
in FY2024 to ¥+9,741M (adjusted ¥144,989M, operating ¥154,730M), so it did not flatter in both years. The 60th report's plan
set "an EBITDA margin of 18% or more as an indicator of our ability to generate cash"; EBITDA in the filer's own mouth.
Compensation income from a supplier for the engine-certification violation, ¥16,826M (FY2024) and ¥9,786M (FY2025), against
related losses of ¥4,514M and ¥4,960M; insurance income ¥6,613M (FY2025) for a fire of July 4, 2024. Equity-method share
¥3,576M against dividends received ¥2,577M (FY2025). Restricted shares to executive officers (33,801 shares in FY2025). The
59th report's capital-expenditure table figure differs from its own text (Step 0).

**Q5 (the people): integrity facts, recorded, not judged.** (1) The company publishes earnings forecasts and revises them
(Q1 FY2026: revenue ¥1,470,000M, net income ¥84,000M, raised from ¥1,430,000M and ¥80,000M). (2) The adjusted-operating-
income figure featured as the performance indicator (Q4 above). (3) It states its misses plainly: FY2025 results against
the plan's targets, ROE 8.6% against "over 13%", the income ratio 9.5% against "over 13%". (4) The ACME episode: the
company guaranteed the bank loans of an equity-method affiliate (guarantee obligations ¥64,003M at March 2022), paid
¥53,479M when it defaulted, was "in dispute with ACME and its related parties", and settled in March 2024 by taking ACME
over and paying ¥2,019M "related to the resolution of a dispute". (5) Representative executive officer changed (notice of
February 27, 2026); not read further.

**Q6 (the money and the owners).** Dividends ¥175 a share for FY2025 (payout 50.9% against a 30% to 40% policy), ¥190
planned for FY2026. **The 2026 repurchase:** resolved August 18, 2026 for up to 6,420,000 shares or ¥34.0bn, completed
October 8 at 5,999,100 shares for ¥33,999,921,700, an average of about ¥5,667 a share; the stated reason was "to mitigate
the short-term impact of the aforementioned sale on the supply of and demand for the Company's shares" (Hitachi, Ltd.'s
sale of 21,462,310 shares); the resolution names a share count and an amount, not a price above which it stops. **The
buyback test's line, written back from the computation:** the prices paid (about ¥5,667) sit far above the bottom of the
computed range (¥479 a share), so under Q6's convention for a buyback with no stated price it would weigh against, had Q6
been reached. The new plan's "approximately ¥500 billion in funding for growth investments", with "strategically utilizing
financial leverage" and "inorganic growth" toward "one of the top three in the industry by 2030". Purchases of minority
stakes ¥19,022M (FY2022), ¥3,623M (FY2024); Brake Supply bought December 2024 (¥15,946M for businesses that year). Control:
ITOCHU holds about 33.4% directly and through HCJI Holdings (notice of February 19, 2026); HCJI may propose a director and
agreed to a five-year standstill from January 2022 (62nd report, Important Contracts).

**Q9 (debt and exposures).** Bonds and borrowings ¥498,549M at June 30, 2026, of which ¥323,331M current; net debt to
equity 0.40 on the filer's measure (FY2025). Interest expense ¥15,883M against income before taxes ¥124,226M (FY2025).
Guarantee obligations for borrowings ¥56,564M at March 2026, up from ¥42,791M a year earlier (62nd report note 29).
Sales-finance credit risk on installment sales and finance leases (Business Risks, item 5); lease receivables ¥38,137M at
March 2024. Retirement benefit liability ¥22,099M. A commitment line and credit line are maintained (liquidity note).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9d7a24f1); written question by question; committed after each
      (Step 0 to Q1: a371894e; Q2: f7fecb59; this close: the next commit).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the fold is
      the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. **Declared under contamination** (header): a filtered
      listing of `Test Runs/` showed the name of a 2026-07-15 HTCMY run (not opened); a listing of the repository root
      showed the name `PORTFOLIO.md` (not opened). That root listing came from a backgrounded download command that lost its
      directory: it wrote two files of mine (`jgbcme.csv`, `results_index.html`) into the repository root, which I deleted
      at once (they were mine, untracked, never committed); three PDFs already in the root (`ar22.pdf`, `ar23.pdf`,
      `ar24.pdf`, not mine) were left untouched.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (check script
      `check_ids.py` in the research folder); no E-ids. Filing facts carry their document and date (no accession numbers
      exist for this filer; the rivals' 10-K accessions are given).
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: the range's bottom is owner cash from operating cash;
      the top is the maintenance-only case that specific (e) orders, built from earnings with depreciation as the disclosed
      maintenance guess **[M1998-127]**, **[M2000-144]**, labelled as such and never used as owner cash. Sovereign from the
      issuing authority (MOF). The price quote is an aggregator's, flagged.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` produced no lines for this filer (not an SEC registrant); nothing it prints was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (2026-10-13); `check_ids.py`: 52 id citations,
      39 distinct, all in the ledger, 33 quoted fragments checked, 0 problems, no E-ids.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The ordinary-returns item of Q2 speaks of a field**, "a field whose durable players earn ordinary returns over a full
cycle". Here the field's leader earns well above the ordinary (Caterpillar's operating margin 13.7% against this
company's 8.8% over the same decade), and it is the deciding part's own castle that protects ordinary returns. I applied
the item to the part's own returns, together with the high-cost-producer item and the moat's definition **[L2007-004]**;
the text does not say whether one player's ordinary returns, in a field the leader shows is not ordinary, closes OUT under
that item or should be argued through the low-cost test alone. (2) **The all-equity net debt** is taken "at the latest filed
balance-sheet date with the subsequent events that filing itself states added"; a repurchase completed after the latest
filing and reported in later company notices is not covered, though the share count must reflect it. I added the cash
paid (a CONVENTION of this run) and showed the figure without it. (3) **IFRS 16** leaves no operating-lease category for a
lessee; the text's "operating leases left out" was read as all lease liabilities left out because lease principal is
charged in owner cash. (4) **Non-controlling interests** are not addressed in Q7; I deducted distributions to them from
owner cash and used net income to the parent in the maintenance case. (5) **Specific (e)'s "where the filing allows the
maintenance guess"**: the filing gives no maintenance figure; whether the depreciation proxy row counts as the filing
allowing the guess is unclear; I used it, disclosed, and the inversion made the maintenance case the top. (6) **Captive
sales finance**: the floor-plan convention covers notes secured by inventory, not borrowings that fund customers'
installment and lease receivables; I counted all borrowings as net debt. (7) **The fair price averages a negative end**:
the bottom end valued at ten percent is below the net debt (¥(954) a share); the definition averages it in as written.
(8) **A foreign filer under the template**: the template asks for accessions and a proxy; document names and dates were
used, and the governance section of the securities report was not reached. (9) A practical note: the dispatched brief
names a "plain browser User-Agent" for the IR site; it worked, and the MOF file needed none.
