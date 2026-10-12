# Company Run: BOUYGUES SA (Euronext Paris: EN; US OTC: BOUYF), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to bottom;
every judgment cites a v5 ledger id in bold; every filing fact carries its document (this name files no SEC documents, so the
AMF filing number, date and URL stand in place of an accession number, as the brief directs). Copied to this dated name before
any fetch (commit 8acaf5d6).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-12, after the run was committed: not held (`PORTFOLIO.md` does not name Bouygues, BOUYF or EN).*

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check this file's name showed two other
runs of today, `2026-10-12 Run - ADRZY Andritz.md` and `2026-10-12 Run - SUNB Sunbelt Rentals Holdings.md`, with their research
folders; neither was opened. (2) The session context carried the subjects of the last five commits (a SUNB/ASHTY fold and run,
closed TOO HARD (NATURE) at Q2); none concerns this company. (3) The memory index loaded with the session carries one-line
summaries of the queue (wave state, a count of gate-clearers, holding reviews owed, "Japanese names"); none names this company.
Nothing of the three was used.

**The documents (operator rule 4).** All from the AMF's BDIF database, `https://bdif.amf-france.org/back/api/v1/documents/<path>`
(bouygues.com refused every scripted and fetch request with HTTP 403, so the English edition was not obtained; the filed French
text is read, and every translation below is mine):
- **FY2025 Universal Registration Document** (Document d'enregistrement universel 2025, incl. the annual financial report),
  AMF filing **D.26-0111**, filed **2026-03-19**, ESEF package `2026/D.26-0111/3028C813...4F1A.zip`. The primary document.
- The registration documents for FY2024 **D.25-0147** (2025-03-26), FY2023 **D.24-0153** (2024-03-22), FY2022 **D.23-0133**
  (2023-04-21), FY2021 **D.22-0139** (2022-03-24), FY2020 **D.21-0139**, FY2019 **D.20-0157**, FY2018 **D.19-0176**, FY2017
  **D.18-0158**, FY2016 **D.17-0201**, FY2015 **D.16-0143**, FY2014 **D.15-0164**: twelve years of filed accounts.
- **The latest interim**: the half-year 2026 financial report itself was not obtained (bouygues.com, 403; it is not in BDIF). Used
  instead: the company's own release of **2026-07-30**, "Very strong Group performance in first-half 2026", with its condensed
  statements, and its release of the same day announcing the report's filing with the AMF, both via mfn.se / GlobeNewswire.
- The company's releases of **2026-06-06** (Bouygues Telecom signs, with Free-iliad and Orange, a memorandum of understanding with
  Altice France to acquire SFR), **2026-10-01** (shares and voting rights at 30 September 2026), **2026-09-14** (own-share
  purchases 7 to 11 September 2026), and **2026-02-26** (FY2025 results), all via mfn.se / GlobeNewswire.
- Text extracts and the arithmetic script are in `Test Runs/_research 2026-10-12 BOUYF/` (`notes.md`, `scripts/`); the raw filings
  are in its ignored `cache/`.

**One figure cross-checked against the filed statement:** the FY2025 cash-flow statement's closing net cash, **€6,432m**, equals the
balance sheet's cash and equivalents **€7,535m** less bank overdrafts **€1,103m** (URD 2025, 6.1.1 and 6.1.5). It agrees. A second:
the segment note's group net debt at 31 December 2025, **€(4,204)m** (note 17), equals the balance sheet's own net-debt line.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **€40.30**, close **2026-10-09** on Euronext Paris (EN.PA), from Yahoo Finance through `tools/sources.py`: an
  **aggregator, flagged** (operator rule 5). The euronext.com quote page and stooq refused scripted requests. Beside it, the US
  OTC line **BOUYF $43.90** (close 2026-10-09, same aggregator, thinly traded). The company's own purchases of its shares on
  7 to 11 September 2026 were at daily averages of **€43.95 to €45.07** (release of 2026-09-14). One-year range on the aggregator
  €38.07 to €53.00.
- **Shares:** **388,438,129** shares in issue at 30 September 2026 (release of 2026-10-01, Article 223-16 disclosure; the same
  release still prints share capital of €385,323,631, the year-end figure, so the capital line lags the count). Treasury shares:
  **1,035,555** at 31 December 2025 (URD 2025, note 5.3, outside the liquidity contract), the latest count filed; purchases
  continued in 2026. **Shares used: 387,402,574.** One class of share; double voting rights exist (499.6m theoretical votes).
  `Screens/cover_shares.py` and `tools/run.py` were not run: both read SEC filings, and this name has none (said, as the brief asks).
- **Market cap:** 387.4m x €40.30 = **€15,612m**. Net debt as the company defines it (borrowings less cash, lease obligations
  excluded) **€6,515m at 30 June 2026** (seasonally high; **€4,204m** at 31 December 2025); lease obligations **€3,294m** at 30 June
  2026, beside.
- **Sovereign for the earnings currency (EUR):** **3.778%**, the ECB euro-area AAA yield curve, 30-year spot, series
  `YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y`, dated **2026-10-08**, from the issuing authority through `python tools/sources.py`.
- **`tools/run.py` arithmetic:** not available for a non-SEC filer; the arithmetic was done from the filed statements in
  `scripts/q7_computation.py`, every input a filed figure.

**Owner cash after every real cost, by year (€m, group share, before acquisitions and before working capital).** CAF after net
interest, lease interest and tax paid; less gross capital spending; plus disposal proceeds of fixed assets and the change in fixed-
asset payables; less lease principal repaid; less the IFRS 2 share-pay charge; times one minus the minority share of net profit.
All-equity adds back the cost of net debt at the 25.83% statutory rate. Sources: the consolidated cash-flow statements and equity
statements of URDs FY2021, FY2023 and FY2025.

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| CAF after interest, lease interest, tax paid | 3,165 | 3,324 | 3,855 | 4,307 | 4,180 |
| Gross capex | (2,446) | (2,625) | (2,572) | (2,714) | (2,488) |
| Disposals of fixed assets / fixed-asset payables | 472 / (90) | 404 / (105) | 455 / (92) | 230 / 216 | 571 / (13) |
| Lease principal repaid | (361) | (441) | (559) | (555) | (455) |
| Share pay (IFRS 2) | (10) | (15) | (22) | (9) | (19) |
| Minority share of net profit | 13.8% | 14.0% | 13.4% | 13.4% | 10.5% |
| **Owner cash, equity-only, group share** | **629** | **466** | **922** | **1,277** | **1,589** |
| **Owner cash, all-equity, group share** | **728** | **593** | **1,106** | **1,397** | **1,730** |
| Acquisitions net of disposals (group share) | 709 | (5,357) | (170) | (1,052) | (48) |
| Working capital (release +) | 204 | (606) | 1,148 | 776 | 954 |
| Sales | 37,589 | 44,322 | 56,017 | 56,752 | 56,877 |

Equans (bought from Engie for €6.27bn of cash net of cash acquired, consolidated from October 2022) sits inside the window.
2025's disposals include €322m from the Infracos asset sale at Bouygues Telecom (FY2025 release). Owner cash never exceeded
**3.0% of sales** in the window.

**The balance sheets first, ten of them, read in Step 0 because the file closes before Q4** **[M2025-032]** (consolidated balance
sheets of the URDs FY2017, FY2019, FY2021, FY2023, FY2025; €m):

| 31 Dec | Sales | Goodwill | Other intangibles | PP&E | Equity, group share | Total equity | Cash | Net debt | Trade receivables | Inventories |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 31,768 | 5,367 | 2,180 | 6,566 | 8,140 | 9,420 | 4,749 | (1,866) | 6,367 | 2,955 |
| 2017 | 32,904 | 5,385 | 2,132 | 6,858 | 8,851 | 10,210 | 4,820 | (1,914) | 6,732 | 3,037 |
| 2018 | 35,555 | 6,301 | 2,198 | 7,327 | 9,647 | 11,032 | 2,928 | (3,612) | 6,145 | 3,154 |
| 2019 | 37,929 | 6,541 | 2,177 | 7,502 | 10,405 | 11,800 | 3,574 | (2,222) | 6,288 | 3,239 |
| 2020 | 34,694 | 7,232 | 2,694 | 7,486 | 10,401 | 11,872 | 4,224 | (1,981) | 5,890 | 2,839 |
| 2021 | 37,589 | 7,446 | 2,774 | 8,048 | 11,144 | 12,789 | 6,501 | (941) | 6,641 | 2,810 |
| 2022 | 44,322 | 12,626 | 3,969 | 9,187 | 12,212 | 13,932 | 5,736 | (7,440) | 9,573 | 3,131 |
| 2023 | 56,017 | 12,658 | 3,717 | 9,365 | 12,408 | 14,112 | 5,548 | (6,251) | 9,700 | 2,924 |
| 2024 | 56,752 | 13,652 | 3,912 | 9,625 | 12,700 | 14,512 | 5,567 | (6,066) | 9,656 | 2,919 |
| 2025 | 56,877 | 13,715 | 3,646 | 9,632 | 13,036 | 14,851 | 7,535 | (4,204) | 9,196 | 2,704 |

(2018 is the restated column of the FY2019 document, after IFRS 16; 2016 and 2017 are before IFRS 16, so right-of-use assets,
€3,050m in 2025, are absent from the first two rows. The 2016 to 2019 associates line carried the Alstom stake, sold 2019 to 2021.)

What the balance sheets say, and what they cannot **[M2025-032]**: (1) **Goodwill and intangibles overtook the owners' equity.**
In 2016 goodwill plus intangibles (€7.5bn) were 93% of group equity; after the Equans purchase they are €17.4bn against €13.0bn,
133%: the tangible equity of the group, as stated, is negative, and the Equans goodwill alone is **€6,231m** (note 3.2.4.2).
(2) **The group became a net borrower in one stroke.** Net debt was €1.9bn in 2016 and €0.9bn in 2021, then €7.4bn after
Equans in 2022, and it has been worked down by retained cash and working-capital inflows to €4.2bn at December 2025, seasonally
back to €6.5bn at June 2026. (3) **Customers finance the business.** Contract liabilities (advances and billing ahead of work)
rose from €4.1bn (2020) to **€9.5bn** (2025), and trade payables (€10.1bn) exceed trade receivables (€9.2bn): working capital is
negative and its releases (€2.9bn over 2023 to 2025) are cash borrowed from customers and suppliers, which reverses if volumes
fall. (4) **Receivables and inventories track sales**: receivables 16 to 20% of sales throughout, inventories falling from 9% to
5% of sales; no build-up out of line. (5) **Retained earnings grew slowly**: group equity rose €4.9bn in nine years while about
€0.6 to €0.75bn a year was paid out in dividends. What the figures cannot say: the segment split of the Equans goodwill's
future earnings, and what the €8.5bn or so of new telecom debt for SFR would do (outside the window, not yet signed in final form).

## THE FOUNDATIONS (not a gate)
The foundations bearing hardest here are the analyst's habits and the market that serves. A conglomerate of six businesses invites
the reader to find one good part and let it carry the rest, and a consolidation deal in telecoms invites the reader to price the
better market before it exists; the habit asked is to look "for what’s wrong in things because that’s part of investing – looking at
what you’re missing" **[M2025-013]**, and to treat the last 20 percent of the work as a chance "to possibly reject your original
hypothesis" **[M1998-144]**. The quotation "doesn’t tell us anything. It just tells us prices." **[M2006-077]**: the fall from €53
to €40 in the year is read here for nothing. **Contrary evidence, written down as found** **[M1997-127]**: (a) Bouygues Telecom's mobile ABPU fell €0.7 a month in
2025 and €0.6 more by Q2 2026 "in a market impacted by ongoing price pressure" (releases of 2026-02-26 and 2026-07-30); (b) the
deciding part's own goodwill test breaks even at a 6.0% discount rate (URD 2025, note 3.2.4); (c) S&P put the group's rating on
CreditWatch negative on 2026-07-03 after the SFR memorandum; (d) the Free Mobile damages claim against Bouygues Telecom was raised
to €805m to €1,440m on appeal (URD 2025, 4.2.4.1); (e) the shares in issue rose 2.5% in 21 months while the company was buying shares.

## THE STANDING RULE
The buyer's own conduct: a purchase of these shares for cash, unlevered and sized so that a fall of half would be borne, puts
the buyer at no risk of ruin; on borrowed money it would, since "the use of borrowed money can destroy the decent returns" and
"borrowed money has no place in the investor's tool kit" **[L2014-005]**; **[M2012-081]**. The target's own debt is Q9's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test, applied by parts.** Bouygues is a holding company of six reported businesses (note 17: Colas, Bouygues Construction,
Bouygues Immobilier, Equans, Bouygues Telecom, TF1). Q1's holding-company paragraph reads it by its parts, and a part "matters"
when it decides under Q2's parts convention: more than half of five-year operating profit, or else the largest part (CONVENTION,
the framework's, sections B of the gaps case). Five-year current operating profit 2021 to 2025, from note 17 of each URD (€m):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Sum | Share of parts |
|---|---|---|---|---|---|---|---|
| Bouygues Telecom | 572 | 694 | 798 | 795 | 674 | 3,533 | **30.4%** |
| Colas (roads, rail, materials) | 440 | 468 | 542 | 552 | 586 | 2,588 | 22.3% |
| Equans (energy and technical services; from Oct 2022) | - | 130 | 545 | 680 | 820 | 2,175 | 18.7% |
| Bouygues Construction | 342 | 413 | 281 | 326 | 376 | 1,738 | 15.0% |
| TF1 (television) | 343 | 322 | 287 | 297 | 252 | 1,501 | 12.9% |
| Bouygues Immobilier (property development) | 43 | 37 | 28 | (51) | 20 | 77 | 0.7% |

(2021 is "résultat opérationnel courant"; 2022 onward "résultat opérationnel courant des activités", before PPA amortisation; the
holding's own cost, €(300)m over five years, is not a part.) **No part carries more than half; the largest, Bouygues Telecom,
decides**, and it is the part Q1 must understand. (Equans was the largest in 2025 alone; the convention reads five years.)

**Bouygues Telecom's key variables** **[M1998-044]**: the number of network operators in France, the price per subscriber (mobile
and fixed ABPU), the subscriber count, and the capital the networks and spectrum consume. The business sells only in France (URD
2025, 4.1.3.1: "Bouygues Telecom propose exclusivement ses offres et services sur le marché français"), to consumers and firms, on
monthly plans. Each variable is in the filings year by year back to 2013, and the forecast is about "consumer behavior and threats
to a business" **[M2023-030]**, the customers' choices and the rivals' prices, not a technology bet: "laying out what their
prospective customers will do in the future" **[M2017-019]**. The industry's insiders do write a ten-year forecast down: the
2026-06-06 memorandum states synergies of about €1bn a year, 70% by 2032 and in full by 2034, and integration costs of €3.5bn to
€4bn, so the forecast the speakers' test 5 asks about is one the insiders put on paper **[M2000-105]**.

**Where it will be in ten years** **[M2000-037]**; **[M2012-065]**: a French mobile and fibre operator, either the third of four
networks (today) or, if the SFR transaction closes in the second half of 2027 as planned, the second of three, with about 3.8
million more mobile and 2.6 million more fixed consumer customers, SFR Business, and roughly €8.5bn of new debt (about 42% of a
€20.35bn enterprise value; release of 2026-06-06). Both branches are the same kind of business with stated terms, and "how the
industry will develop and where the company will stand within the industry" **[M2012-065]** can be pictured in each. What cannot
be pictured is whether the field's prices will hold, which is Q2's question, not Q1's: Q1 asks whether the economics can be
foreseen at all, Q2 what the foresight shows about the castle.

**The doubt, written down** **[M2002-092]**: the transaction is not certain ("At this stage, there is no certainty that this
transaction will go ahead", release of 2026-06-06), and definitive documents, expected in the second half of 2026, had not been
announced by 2026-10-12 (the company's release list to that date carries none). The doubt is about which of two understood
structures arrives, not about the economics of either; it is carried to Q2. **TF1**, whose linear television audience falls
year by year ("les Français regardent en moyenne 2h44 la télévision par jour, soit moins 7% par rapport à 2024", URD 2025,
4.1.4.1), is the part closest to the fast-change routing, but it carries 12.9% of five-year operating profit and does not decide;
it is carried as a non-deciding part.

**VERDICT: IN** (by its deciding part): Bouygues Telecom's ten-year economics turn on knowable variables, filed back to 2013,
and on a market structure whose two possible forms are stated in the company's own documents **[M2012-065]**; **[M1998-044]**;
**[M2023-030]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence chosen** (the brief's second departure: derived from the registration document, not from a hand list):
from the business description and management report (URD 2025, chapter 1 and the segment note 17), the segments' operating
profit and cash over the window and Bouygues Telecom's back to 2013; from the risk factors (4.1.3, telecoms; 4.1.4, media), the
competitive pressure on prices; from the litigation section (4.2.4), the disputes between the operators; from the goodwill note
(3.2.4), the deciding part's impairment test; from the company's releases of 2026, the SFR memorandum and the first-half trends.

**The rivals the documents name, and what was obtained.** The URD names Free Mobile and Orange as Bouygues Telecom's adversaries
in litigation (4.2.4) and, with Altice France (SFR), as the parties to the SFR transaction (note 1.2.1 and the 2026-06-06
release). Three primary documents were obtained: **Orange**, URD FY2025, AMF **D.26-0217** (filed 2026-04-02), France segment
(section 3.1.3.1, segment assets note 1.6); **Iliad** (Free), URD FY2020, AMF **D.21-0312**, and its URD FY2012, AMF **D.13-0318**
(Iliad left the stock market in 2021 and files no URD since; its H1 2025 financial report was read from a copy hosted by a trade
site, gsmonline/siteor, flagged as a secondary host of the company's own report); **Altice France** (SFR), FY2025 MD&A and
financial statements of Altice France Lux 3 SA, from alticefrance.com. Not obtained: Iliad's FY2025 annual report (its site
serves documents only through a script), and Orange's France segment for the 2012 to 2022 years (Orange's FY2013 to FY2022 URDs
are listed on BDIF, D.14-0439 onward, but were not read in this run).

**The parts table** (section B convention; five-year current operating profit as in Q1):

| Part | Share of 2021-25 operating profit | Castle, in one line from the filings | Decides |
|---|---|---|---|
| Bouygues Telecom | 30.4% | Third of four French networks; prices set by the field; returns ordinary through the cycle (below) | **Yes (largest)** |
| Colas | 22.3% | Public road and rail works won by tender (36% of group sales are public contracts, note 12.4); margins 2.8% to 3.7% | No |
| Equans | 18.7% | Technical services contracting; margin from activities 4.4% (2025) to 5.2% (H1 2026) | No |
| Bouygues Construction | 15.0% | Building and civil works by tender; margin 3.5% (2025) | No |
| TF1 | 12.9% | Leading free-to-air broadcaster in a linear market in structural decline (4.1.4.1) | No |
| Bouygues Immobilier | 0.7% | Housing developer; a loss in 2024 | No |

The non-deciding parts are carried, not judged; the file closes on Bouygues Telecom.

**The castle tests, on Bouygues Telecom.**
- **The attacker with money** **[M2011-015]**: it came, and it worked. Free Mobile launched in 2012 as a fourth network. Bouygues
  Telecom's current operating profit went from €125m in 2013 to **€(65)m in 2014** and **€(11)m in 2015** (URD FY2014 management
  report: "Le résultat opérationnel courant ressort à (65) millions d'euros, en baisse de 190 millions d'euros"; URD FY2016), and
  its 2014 objective was only that EBITDA cover capital spending, met with **€10m** to spare (URD FY2014). The answer to "could I
  do it?" was yes, and "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**; "one competitor is frequently enough
  to ruin a business." **[M2012-108]**.
- **Pricing power and the agony before a rise** **[M2005-020]**: the company's own risk factor names the opposite: "Une pression
  concurrentielle très intense sur les tarifs Mobile et Fixe pourrait affecter négativement les résultats attendus par Bouygues
  Telecom, dans un marché nécessitant des investissements importants" (URD 2025, 4.1.3.1). Mobile ABPU fell €0.7 a month in 2025
  (to €18.4 excluding La Poste Telecom) and €0.6 more by Q2 2026 (to €16.7), "negatively impacted by continued low prices for new
  customers, particularly for digital plans" (release of 2026-07-30). Fixed ABPU rose a little (€33.2, up €0.2). No business "that
  has incredible pricing power" here, which would be "a monopoly or a near monopoly" **[M2010-092]**.
- **The low-cost position** **[L2000-017]**; **[M1997-010]**: Bouygues Telecom is not the low-cost operator; its rival Free is,
  on the filed figures. EBITDA after leases less capital spending, as a share of sales: **Bouygues Telecom 6.9%** in 2025 (€2,042m
  less €1.48bn gross capex, on €8,098m; FY2025 release); **Iliad France 20.8%** in H1 2025 (€682m on €3,273m; H1 2025 report);
  **Orange France 19.2%** in 2025 (€6,429m less €3,077m eCapex, on €17,473m; Orange URD 2025, 3.1.3.1); **SFR 16.1%** in 2025
  (€3,071m less €1,560m, on €9,382m; Altice France MD&A FY2025). Operating margin: Bouygues Telecom **9.7%** in 2020 (€623m on
  €6,438m) against Iliad France **18.5%** (€924m on €5,004m; Iliad URD FY2020). "It’s like comparing a copper producer whose costs
  are $2.50 a pound with a copper producer whose costs are $1 a pound." **[M2009-059]**; "the low-cost producer can put you out of
  business" **[M1997-010]**.
- **Would the customer still choose it over the low bid** **[L2004-003]**: the filings describe a market won by price for new
  customers ("low prices for new customers on digital offers", FY2025 release), a mobile number that moves between four networks,
  and a subscriber base grown largely by acquisition (Euro-Information Telecom, consolidated 2022; La Poste Telecom, 2024).
- **Unit volume and share of mind**: volumes do grow (mobile plans 18.8m, fixed 5.5m at June 2026), but the volume is bought
  with price and capital, and Bouygues Telecom's sales billed to customers were "almost stable" in H1 2026 on rising customer
  counts (release of 2026-07-30).
- **Ask the competitors** **[M1999-130]**: the rivals' own conduct answers it. Free sued Bouygues Telecom over its handset offers
  and won €308m in first instance (2023, paid; appeal claim raised to €805m to €1,440m); Bouygues Telecom sues Free over its
  advertising and Orange over access to copper and fibre (URD 2025, 4.2.4). The field fights for each customer in court as well as
  on price.
- **Widening or narrowing** **[M1999-108]**: the operating profit recovered from the 2014 trough to €798m in 2023 and has fallen
  since (€795m, €674m, and €274m in H1 2026, down €32m), the company saying the decline comes from depreciation "in line with the high
  level of investments made over recent years". Capital spending peaked; the price per mobile customer still falls.
- **What could destroy or reduce it** **[M2000-014]**: a renewed price war at the low end, which the 2026 releases describe as
  under way; and, in the other direction, the SFR transaction, which is a forecast, not a fact on the record.

**The field's returns over the last full cycle, judged in words.** The cycle here is the one the fourth licence opened: from the
2012 entry, through the trough of 2014 and 2015, to 2025. On the filer's own evidence Bouygues Telecom's returns over that span
were ordinary at best: negative operating profit in 2014 and 2015, and in 2025 a current operating profit of €674m on operating
assets of about **€14.8bn** (PP&E €5,932m, intangibles €2,124m, right-of-use €1,493m, goodwill €4,328m, joint ventures €923m; note
17 and 3.2.4.2), about 4.6% before tax. The company's own goodwill test says the same thing in its own words: at a discount rate
of **6.0%** the recoverable value of Bouygues Telecom equals its book value (note 3.2.4, "la valeur recouvrable serait égale à la
valeur comptable des actifs testés en retenant ... Taux d'actualisation 6,0"), and a 20% cut in normative cash with a one-point
rise in the rate would put it €1.1bn to €1.7bn below book. The rivals: SFR's revenue fell 9.5% in 2025 to €9,382m and its owner
reached agreement with its creditors on 26 February 2025 and "On October 1, 2025, Altice France completed its financial
restructuring, fully implementing the accelerated safeguard plans" (Altice France Lux 3 MD&A FY2025, Significant Events); Orange France's revenue fell 2.1% in 2025, its 2024 operating income of €3,289m stood
on €39.0bn of non-current segment assets (about 8.4% before tax); Iliad France, the attacker, earns the most. A field whose players
have, over thirteen years, ranged from a creditor restructuring to high single digits before tax on their capital, with the deciding
company at the bottom of the cost table, is one whose castle "protects" nothing like "excellent returns on invested capital"
**[L2007-004]**: "you can have only two competitors and they’re still terrible businesses, they beat each other’s brains out."
**[M2013-052]**; **[M2018-088]**.

**The SFR transaction, and whether it is a change for the better to be credited.** It is not credited, on two grounds. First,
it has not happened: a memorandum signed 2026-06-06, definitive documents expected in the second half of 2026 and not announced by
the date of this run, completion "could occur in the second half of 2027, following clearance from the competent authorities,
particularly the competition authorities" (release of 2026-07-30); no year of three-player prices is on any filed record. Second,
even after it, a change for the better is credited only on a full cycle in which the price behaviour held **[M2005-020]**;
**[L1995-022]**; **[M2017-026]**, and the rows warn that three or two players can still "beat each other’s brains out"
**[M2018-088]**. The castle is judged on the field as it stands and as it has performed, which is the evidence; the consolidation is
written down here and not weighed.

**VERDICT: OUT.** The deciding part's castle is shown open on the evidence: an attacker with money entered and was able **[M2011-015]**;
**[M2012-108]**; Bouygues Telecom is the high-cost operator in a field that sells on price **[M1997-010]**; **[M2009-059]**; and the
field's durable players have earned ordinary returns over the full cycle since 2012, on their own filings, which closes OUT and not
TOO HARD (Q2, What it rules OUT, the standing castle that protects only ordinary returns; **[L2007-004]**; **[M2013-052]**).

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's reporting figures (Part VII, The owner's price) are computed below under COMPUTATION,
NOT A CLEARANCE (operator rule 3).

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2** (the castle of the deciding part, Bouygues Telecom, shown open on the evidence: the attacker with money came and
was able, Bouygues Telecom is the high-cost operator, and the field earned ordinary returns over the full cycle since 2012; the
SFR consolidation, signed as a memorandum on 2026-06-06 and not closed, is not credited). **Integrity facts recorded, not judged.**
COMPUTATION beneath the stop, at €40.30: value range €76.73 to €79.58 a share all-equity at the sovereign; fair price €17.09
all-equity (equity-only €29.98); no case earns the floor at the price.

## COMPUTATION, NOT A CLEARANCE: the owner's two reporting figures
*(Part VII, The owner's price, and How the fair price is computed; the file is closed, so nothing here is a verdict, a clearance or
entry language. Script: `Test Runs/_research 2026-10-12 BOUYF/scripts/q7_computation.py`; every input is a filed figure.)*

**The cash input.** Owner cash after every real cost, group share, as tabled in Step 0. **The tax** is the company's own, as paid
(the cash-flow statement's "impôts décaissés"), no conversion (Q7, Whose tax); the floor's "pre-tax" is read as before the holder's
tax. **The all-equity basis** (central) adds back the cost of net debt at the 25.83% statutory rate and sets the value against
the company's net debt (borrowings less cash; lease obligations left out of net debt, their payments charged as an operating
cost, and said so); **the equity-only figure** beside uses owner cash after interest with no net debt deducted.

**The window and its specifics, in full.**
- **Literal window 2021 to 2025, shown beside:** all-equity owner cash less acquisitions averages **€(73)m** a year; the series
  changes sign (the €6.27bn Equans purchase in 2022), so the compound rate is meaningless and specific (b) leaves the no-growth case
  alone, which is negative: **€(21.79)** a share after net debt. The literal window gives no positive value.
- **(a) Cycle, aberrational years, and the merger rule.** Equans is a merger inside the window, and the framework values such a
  merger "on the combined companies' own averages, with the deal's financing deducted". Equans's own pre-acquisition figures are
  not in Bouygues's filings (it was a division of Engie), so the combined average can be formed only from the full combined
  years: **2023 to 2025** is the base (CONVENTION of this run: the three full post-merger years stand for the combined companies'
  averages, because the target's pre-merger figures are not filed by the buyer; the Equans financing is already in net debt).
  Base all-equity owner cash **€1,411m**; equity-only **€1,263m**. 2025 includes €322m of Infracos disposal proceeds at Bouygues
  Telecom (about €96m of the three-year average, about €2.50 of the fair price); kept, as filed, and said here.
- **Aggregate growth, all spending deducted.** The shown growth of all-equity owner cash 2023 to 2025 is **25.1% a year**,
  measured on the aggregate, not per share. Acquisitions after the merger (La Poste Telecom 2024, Equans and Colas bolt-ons) are
  deducted as capital spending: **€(423)m** a year, group share, 2023 to 2025 (specific (c), the default pair; the filer reports
  no organic owner-cash growth to set beside it).
- **(f) The cap.** Carried ten years, 25.1% would make owner cash 21.5% of sales against a highest filed share of **3.0%**; the
  growth carried is cut to the business's own sales growth over the same years, **0.76% a year** (sales €56,017m to €56,877m).
- **Zero growth after year ten**, computed as zero nominal growth; purchases stop with growth after year ten (specific (c),
  2026-10-10): from year eleven the business is valued on owner cash before purchases.
- **(e) Growth spending, and the inversion.** The growth bought (0.76% a year for €423m a year of purchases) is worth less than
  its cost, so the no-growth case is the **top** of the range and the growth case the bottom: "growth can destroy value"
  **[L2000-023]**; the inversion is the finding, as the convention says, not an error.
- **(d) Working capital.** Excluded from the central figure: the window's movements are releases of negative working capital
  (customer advances), €2.9bn over 2023 to 2025, which reverse when volumes fall. The variant with the releases counted is shown
  beside (CONVENTION of this run, rationale: specific (d) speaks of increases as spending and says nothing of releases of a
  negative balance; counting a three-year release as perpetual cash would raise the base by about 60%).
- **Minorities.** Owner cash is taken at the group's share (one minus the minority share of net profit, 10.5% to 14.0%), since
  TF1 is 47% owned and Bouygues Telecom 90.5% (CONVENTION of this run: the all-equity convention is silent on minority interests).
- **A price above the top closes OUT** through the floor; the floor is tested first (2026-10-10).
- **The deal signed but not closed** (SFR) is left out of the central figure and set beside it, below.

**The rate.** The ECB euro-area 30-year yield, **3.778%** (2026-10-08). **Net debt** at the latest filed date, **30 June 2026,
€6,515m** (release of 2026-07-30; the €350m paid at the SFR signing and the Vannoy purchase of 30 June 2026 are inside it; the CV
Services purchase announced 22 July 2026 has no price stated and is not added). It is the seasonal peak: at 31 December 2025 it
was €4,204m, shown beside. **Shares: 387,402,574.**

| (€ a Paris share) | Net debt 30 Jun 2026 (central) | Net debt 31 Dec 2025 (beside) |
|---|---|---|
| **(a) VALUE RANGE, all-equity, at 3.778%** | **€76.73 (growth case) to €79.58 (no-growth case)** | €82.70 to €85.55 |
| Value range, equity-only | €82.75 to €86.28 | n/a |
| Literal window 2021-25 (beside) | €(21.79), no-growth alone | n/a |
| **(b) FAIR PRICE, all-equity** (each end at 10%, averaged) | **€17.09** (ends €19.60 / €14.58) | €23.05 |
| Fair price, equity-only | **€29.98** | n/a |
| Fair price with working-capital releases counted (variant) | €39.34 | n/a |

**Against the price of €40.30:** the price is above the fair price on every basis computed, including the variant that counts
three years of working-capital releases as permanent. The floor test (2026-10-10): at €40.30 the enterprise value is €22,127m; the
no-growth case yields **6.38%** on it and the growth case **4.46%** with 0.76% growth, so **no case earns the floor of about ten
percent at the price** **[M2003-149]**; had Q7 been reached it would have closed OUT on the floor, before the width test (the range
is narrow, about 1.04 to one). The range at the sovereign rate lies far above the price; it is the floor, not the range, that the
price fails. Width and screamer tests not reached.

**The SFR deal, beside the central figure** (signed memorandum, not closed): Bouygues Telecom's share is about 42% of a €20.35bn
enterprise value, about **€8.5bn**, to be financed by a bank loan then bonds; its share of the scope is about €4.1bn of sales and
about €1.0bn of 2025 EBITDA after leases (release of 2026-06-06, on Altice's accounts). On the scope's own filed record, SFR's 2025
capital spending was 16.6% of its sales (Altice France MD&A FY2025); at that rate the scope's capital spending is about €0.68bn,
leaving about **€0.3bn** a year before tax, integration costs (€3.5bn to €4bn, mostly in the first five years) and synergies
(about €1bn a year by 2034, not credited). At ten percent, €8.5bn of added net debt needs about €0.85bn a year; on the filed record
the deal would lower the fair price by roughly €5.5bn, about €14 a share, before any synergy. Arithmetic only; the box is decided
on the central figure.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged **[M1997-127]**.)*

**Bearing on Q3 (capital).** Bouygues Telecom's gross capital spending was €1.48bn in 2025 against €2,042m of EBITDA after leases;
the company says its capex "peak" of the last five years is ending (about €1.3bn guided for 2026). Group owner cash never exceeded
3.0% of sales in 2021 to 2025. Equans was bought for €6.27bn of cash in 2022; its goodwill is €6,231m. Margins of the contracting
parts in 2025 (current operating profit from activities on sales): Colas 3.7%, Bouygues Construction 3.5%, Equans 4.4%.

**Bearing on Q4 (the accounts).** Lease principal of €455m to €559m a year is a real cost below the company's featured "EBITDA
après Loyer". The company features adjusted figures: "current operating profit from activities" (before PPA amortisation), "free
cash flow" before working capital, and in H1 2026 "net profit attributable to the Group excluding exceptional income tax
surcharge" as a key-figure line. It gives yearly guidance by segment (2026: Bouygues Telecom FCF "around €600 million"; group COPA
"maintained at a record high level"). "Other operating income and expenses", presented as non-current, recur every year: €(224)m net
in 2025, €(196)m in 2024, €(60)m in H1 2026 (litigation, incentive plans, restructuring). The effective tax rate was 34.1% in 2025.
Nothing found in the statements themselves that confuses or raises suspicion; not judged.

**Bearing on Q5 (integrity facts, recorded, not judged).** (1) The Paris commercial court ordered Bouygues Telecom on 9 February
2023 to pay Free Mobile €308m, on Free's claim that its old handset-and-plan offers were consumer-credit operations and deceptive
practices; paid (€310m with interest) in May 2023; Bouygues Telecom appealed; Free raised its claim to €805m to €1,440m in October
2025; the appeal hearing was scheduled for April 2026, and no outcome was found in the documents read (URD 2025, 4.2.4.1).
(2) Île-de-France schools (METP): after a 2007 competition-authority decision on anti-competitive practices in the award of lycée
renovation contracts in the 1990s, the Paris administrative court of appeal on 5 December 2025 ordered the defendants, Bouygues
group companies among them, to pay damages in eight first cases, now final; other cases to be heard in 2026; total loss alleged
€293.3m (4.2.2.1). (3) Colas Rail: a 2017 internal audit and external inquiry found suspicious payments to local consultants in a
foreign subsidiary, on contracts dating to 2011; Colas Rail filed a criminal complaint in France; the URD says the matter saw
developments in October 2025 that put new risks on Colas (4.2.1.3). (4) A €100m tax reassessment notified to a Bouygues
Construction subsidiary in December 2025, contested (4.2.2.2). (5) €190m of 2025 charges for disputes at Bouygues Telecom (note
13.2). (6) A Canal+ trademark suit against TF1 (€46m claimed). Any later run that reaches Q5 must answer these **[M2013-088]**.
Governance, pay and the board (URD chapter 2) were not read.

**Bearing on Q6 (the money and the owners).** Shares in issue rose from 378,957,797 (end 2024) to 385,323,631 (end 2025) and
388,438,129 (30 September 2026): stock options exercised in 2025 created 7,754,692 shares for €258.14m (about €33.29 a share), while
the company bought and cancelled 1,388,858 shares (bought in 2024, cancelled 4 November 2025, €48.4m, about €34.85) and bought
400,000 in 2025 for €16.5m (about €41.25) and more in September 2026 at €43.95 to €45.07. The buyback programme's maximum price was
not read. Dividends €2.00 a share (paid 2025) and €2.10 (2026). Against the computation above: the purchases of 2025 and 2026 were
made above the computed fair price and below the computed value range at the sovereign rate; neither is a Q7 finding. The SFR
purchase is to be paid in cash and debt, not stock.

**Bearing on Q9 (debt and exposures).** Net debt €6.5bn at June 2026 (€4.2bn at December 2025), lease obligations €3.3bn;
liquidity €15.8bn (€4.2bn cash and €11.5bn of undrawn medium and long-term lines); bonds averaging 5.8 years, next redemption
October 2026. S&P placed the long-term rating on CreditWatch negative on 3 July 2026 after the SFR memorandum; Moody's kept a
stable outlook (16 June 2026). The SFR share (about €8.5bn) is to be financed by "a fully secured bank loan from partner banks, to be
refinanced via a bond issue in due course". Contingent claims include the Free Mobile appeal (above) and a £236m arbitration claim
over a Belfast biomass plant built by a former Bouygues Energies & Services subsidiary, now in Equans (4.2.3.1).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 8acaf5d6); written question by question; committed after Q1 (bb8d265f)
      and Q2 (a508243e), then at the close.
- [x] Dispatched run: the brief allowed per-question pathspec commits of the run file and research folder only; the lock and the
      fold belong to the dispatching session (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened or searched. One listing of `Test Runs/`
      filtered to today's date showed two other runs' names; declared under contamination above, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every fragment quoted beside an id is in that row (check script
      `scripts/check_run.py`). Filing facts carry the AMF filing number or the release date and source in place of an accession
      number, the brief's stated departure for a non-SEC filer.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the figures after it are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (capital spending, leases, share pay, tax paid), never a net-income proxy; the sovereign
      from the ECB, dated; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP, with "integrity
      facts recorded, not judged" in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` was not used (no SEC filings); the arithmetic is in `scripts/q7_computation.py`.
- [x] `python tools/check_framework.py` PASS before the commit of the close.
- Owed and not done: Iliad's FY2025 annual report (not obtainable by script) and Orange France's segment from 2012 to 2022 were
  not read; the competitor comparison over the span rests on Bouygues Telecom's own series 2013 to 2025, Iliad France 2012, 2020
  and H1 2025, Orange France 2024 and 2025, and SFR 2024 and 2025. The H1 2026 report itself was not obtained; its figures come
  from the company's release. The outcome of the Free Mobile appeal (hearing April 2026) was not found.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts convention let a 30% part decide the whole box.** Bouygues has no part above half of five-year operating profit;
the largest, Bouygues Telecom at 30.4%, decides, and the file closes on it although 70% of the profit comes from four contracting
and media parts that were not judged. Equans was the largest part in 2025 alone and would decide on a shorter window. The rule
works as written; whether a part with less than a third of the profit should carry the box, or whether a company with no dominant
part should be read on its two largest parts, the framework does not say. (2) **The merger rule cannot be applied when the target's
own figures are not filed by the buyer.** "On the combined companies' own averages" presumes the target's pre-deal figures are in
reach; Equans was a division of Engie. I used the three full combined years as the base and confessed it. (3) **Net debt at the
latest filed balance-sheet date is seasonal here**: €6.5bn at June against €4.2bn at December moves the fair price by about €6 a
share; the convention gives no rule for a seasonal business. (4) **Minority interests** are not mentioned in the all-equity
convention; with TF1 47% owned, a whole-group cash figure would overstate the owners' share. (5) **Specific (d) speaks of increases
in working capital only**; for a business financed by customer advances, the releases are the larger question. (6) **Q2 has no rule
for a structural change signed but not closed**: Q7 says how to set a signed deal beside the figure, but the castle question credits
a change for the better only "on the evidence of a full cycle", which reads naturally of a change already in the filings; I treated
the pending consolidation as not yet a change and wrote it down unweighed. (7) **The template assumes SEC documents** (accession
numbers, `cover_shares.py`, `run.py`); for an AMF filer the BDIF filing number serves, and the template could say so. (8) The
template's headings carry dashes the brief asks not to use in prose; I changed them to colons in this file.
