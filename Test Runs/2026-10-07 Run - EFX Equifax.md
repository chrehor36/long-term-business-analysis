# Company Run — Equifax Inc. (NYSE: EFX) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (brief of 2026-10-07, slots filled by the dispatcher: lines
of evidence, competitors TRU, Experian (not an SEC filer), FICO, and any verification filer). Raw filings were saved
outside the repository (the session scratchpad), so none can enter a commit; the research folder holds only this run's
scripts and notes.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared:** (1) the session's git status, shown before any work, listed untracked research folders of
other companies by ticker (AYI, BDC, CHD, ARCB and others) and the last five commit subjects (CL, CMG, CSL, COKE re-runs of
batch 3); (2) the brief and `.gitignore` comments name ATR, MGM, AGCO, DELL and SNPS runs; (3) the project memory index
shown to the session says, in general terms, that holdings reviews are owed and gives a count of gate-clearers, with no
company named. None of it concerns Equifax and none of it is used. A count of the entries in `Test Runs/` was taken
(`ls | grep -c .`, a number only, no names shown) while checking the paths; no file there was listed by name, opened or
searched. I did not open any earlier Equifax run.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $142.40 (2026-10-07, printed by `tools/run.py`; **aggregator, live quote only, flagged** under operator rule 5).
- **Shares by class** from the latest filing's cover: common stock, $1.25 par, **117,484,896** shares (10-Q for the period
  ended 2026-06-30, filed 2026-07-21, accession `0000033185-26-000028`; `python Screens/cover_shares.py EFX`; one class).
  Check: the balance sheet of 2026-06-30 carries 117.6M outstanding and 189.3M issued (the rest is treasury), consistent
  with the cover. No 8-K after the 10-Q issues shares: the 8-K of 2026-07-29 (accession `0001193125-26-323760`) sells
  $1.0B of senior notes (5.000% due 2029 and 5.650% due 2033) to repay commercial paper, so it changes the form of the
  debt, not the share count.
- **Market cap:** 117.485M x $142.40 = **$16,730M**.
- **Sovereign for the earnings currency (USD; 77% of 2025 revenue was earned in the U.S.):** **5.64%**, the 30-year par
  yield, US Treasury daily par yield curve, 2026-10-06 (`python tools/sources.py`).
- **Filings read** (operator rule 4), all from EDGAR, CIK 33185: the 10-Ks for FY2016 to FY2025 (FY2025: filed
  2026-02-19, accession `0000033185-26-000010`; FY2024 `0000033185-25-000025`; FY2023 `0000033185-24-000017`; FY2022
  `0000033185-23-000012`; FY2021 `0000033185-22-000014`; FY2020 `0000033185-21-000025`; FY2019 `0000033185-20-000011`;
  FY2018 `0000033185-19-000007`; FY2017 `0000033185-18-000011`; FY2016 `0000033185-17-000008`); the 10-Q for Q2 2026
  (`0000033185-26-000028`); the proxy of 2026-03-27 (DEF 14A, `0001193125-26-127556`); the 8-Ks of 2026-04-24 (revolver
  raised to $2.0B, `0001193125-26-177620`), 2026-06-16 (bylaws, `0001193125-26-272759`), 2026-07-21 (Q2 results, exhibit
  99.1, `0000033185-26-000024`), 2026-07-29 (notes, above) and 2026-02-04 (FY2025 results, exhibit 99.1,
  `0000033185-26-000004`).
- **One figure cross-checked against the filed statement:** cash provided by operating activities for 2025, **$1,615.7M**
  in the FY2025 10-K's cash-flow table (MD&A, Liquidity, `0000033185-26-000010`), against $1,616M printed by `tools/run.py`
  from the tagged data: they agree. Cash at 2025-12-31, $180.8M filed, against $181M printed: they agree.
- `python tools/run.py EFX`, arithmetic lines only (Part VII): OCF less stock pay less capital spending, by year, 2023
  $444M, 2024 $731M, 2025 $1,056M; the same on the D&A basis $425M, $562M, $810M; stock pay $72M, $82M, $78M; capex
  (tag PaymentsToAcquireProductiveAssets) $601M, $512M, $481M; D&A $620M, $681M, $727M. The tool's three-year means,
  yields and "growth the price assumes" are not used. The ten-year balance-sheet table is read at Q4. The five-year
  series used at Q7 is built from the filed cash-flow statements (below), since the tool prints only three years.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own Equifax "if the market closed for five years"
**[M1997-109]**, which turns the run toward the Work Number, the bureaus and their cash, not toward the quotation. The
market serves, it does not instruct: the company itself bought 4.0 million shares in 2025 at about $231 each ($927.4M,
FY2025 10-K, MD&A, Operational and Financial Highlights) and the price is now $142.40; the fall "just tells us prices"
**[M2006-077]** and is read only against value at Q7. Who is paid to tell you: the company's releases lead with adjusted
EPS and an "AI data moat" (exhibit 99.1 of 2026-07-21), and "the money is in believing something different"
**[M2001-052]**; the filings' own figures are used instead. No macro forecast enters: the mortgage cycle is read from the
filer's own history across a full cycle, not forecast **[M2000-094]**. The analyst's habits: look for "what's wrong in
things" **[M2025-013]** and write contrary evidence down at once **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The filer's own competition paragraph calls Verification Services, the heart of Workforce Solutions, "highly
   competitive with low barriers to entry" in the FY2024 and FY2025 10-Ks; the phrase appears in none of the FY2016 to
   FY2023 10-Ks (text search of all ten). It entered the filing the year an antitrust class action was filed against the
   Workforce Solutions verification business (May 28, 2024, E.D. Pa.; FY2025 10-K, Item 3).
2. The CFPB has investigated data accuracy and dispute handling at Workforce Solutions since July 2023 (three CIDs: July
   2023, March 2024, August 2024; Q2 2026 10-Q, Note 6, still open).
3. The 2017 breach: legal settlements paid of $802.2M through 2023 (FY2023 10-K, Liquidity), plus $1,142.5M of
   incident costs net of insurance in 2017 to 2020 ($114.0M, $326.2M, $337.3M, $365.0M; FY2019 and FY2020 10-Ks,
   footnotes to the segment tables); consent-order commitments still binding (FY2025 10-K, Item 1A).
4. TransUnion's FY2025 10-K lists "uncertainty related to Fair Isaac Corporation’s (“FICO”) new Mortgage Direct License
   Program" among its forward-looking risks (accession `0001552033-26-000012`): the score supplier is moving on the
   bureaus' mortgage channel.
5. Capital spending rose from $173.5M (2016) to $624.5M (2022) for the cloud transformation; D&A rose from $268.7M to
   $726.9M (2025) as it is amortized.
6. Buybacks: $927.4M in 2025 at about $231 a share and $560.0M in the first half of 2026 at about $180 a share (Q2 2026
   10-Q, Note on equity), against $142.40 today.
7. A purchase of Círculo de Crédito (Mexico) for an enterprise value of $750M was signed in July 2026, expected to close
   in Q4 2026 (Q2 2026 10-Q, Liquidity): the acquisition habit continues.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of a marketable share with the buyer's own money, unlevered and sized so
that its total loss cannot touch what the buyer has and needs, puts no one at risk of ruin: "We are never going to risk
what we have and need for what we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**. Nothing about Equifax changes that; its own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test** is whether I have "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, which means naming "the key variables in that particular business, and evaluating how
predictable they were first" **[M1998-044]**, and whether "the financial statements will tell me the information that’s
useful" about the future ones **[M2008-033]**.

**What the business is, from the FY2025 10-K (Item 1, `0000033185-26-000010`).** Three segments. *Workforce Solutions*
(2025 revenue $2,582.3M, operating income $1,141.5M): Verification Services sells employment and income verifications
from The Work Number, "about 209 million active and 813 million total" employment records fed by "payroll data received
from over 4 million organizations", who are generally not charged to contribute; Employer Services sells unemployment-claims,
I-9, tax-credit and ACA services. *U.S. Information Solutions* (revenue $2,078.5M, operating income $475.2M): the U.S.
credit bureau, the tri-merge mortgage report, fraud and identity, marketing data and consumer monitoring. *International*
(revenue $1,413.7M, operating income $182.5M): bureaus in Canada, the U.K., Spain, Australia, New Zealand, India and
twelve Latin American countries, plus debt-collection services.

**The key variables, and whether they can be foreseen.**
1. *Records and contributors at the Work Number.* A count the filer reports every year: total records 535M (2021), 600M
   (2022), 657M (2023), 734M (2024), 813M (2025); contributing organizations "over 7,100" (FY2016 10-K), "over one
   million" (FY2020), "over 4 million" (FY2025). The trend is long and visible.
2. *Price per verification and per credit report.* The filer says its mortgage growth in 2024 and 2025 came "primarily"
   from "product pricing" while mortgage inquiries fell (FY2025 10-K, MD&A, USIS). Price is visible in the filings;
   whether it holds is the castle question (Q2).
3. *U.S. mortgage originations.* Cyclical and not forecastable year by year; the filings show the whole cycle (mortgage
   was 20% of revenue in 2019 and 32% in 2020, FY2020 10-K, end-user note; inquiries fell more than 20% in 2022 and
   "significantly" again in 2023). A cycle that has been seen end to end can be carried as a range, not forecast.
4. *Regulation* (FCRA, CFPB supervision, GSE rules on the tri-merge report and on verification, state privacy law). Its
   direction is the least predictable variable; it bears on the castle and is weighed there.

**Is this inside the perimeter?** The economics are those of a data toll: lenders and employers supply the data, lenders,
employers and agencies pay per transaction to read it back, and the costs are largely fixed. "I never would understand the
chemistry of it, but [...] What is important is that I understand the economic dynamics of the industry. Is there [...]
are there competitive moats? Is there ease of entry?" **[M2011-014]**. Those dynamics can be read from ten years of
segment tables, and the bureaus' place in U.S. credit is the oldest fact in the file: Equifax's predecessor dates from 1899
(Item 1). This is not a business that lives on continued invention **[M1999-075]**: the cloud rebuild changed how the data
is held, not what is sold. The forecast is about customers who must verify income and check credit, not about a technology
whose winner is unknown **[M2017-019]**.

**Doubt, tested** **[M2002-092]**. Two things I cannot foresee: where regulators take verification pricing (CFPB, the
antitrust class action), and whether consumer-permissioned payroll connections replace the employer-contributed file.
Both are questions about the castle's permanence, which the framework gives to Q2 ("Rapid change is owned by Q2", Q1,
What understanding means). Would the industry's insiders write the ten-year economics down **[M2000-105]**? Equifax
does publish a multi-year framework (EFX2028, exhibit 99.1 of 2026-07-21), and its rivals describe the same three-bureau
field in their own filings (TransUnion FY2025 10-K, Competition), so the industry is not one whose future its insiders
call too hard. The doubt that remains is a doubt about durability, not about what the business is or how it earns.

**Routing.** Not a bank or lender (it holds no loans; Q9 test 10 does not arise). Not a holding company; it reports three
operating segments, and the parts are read at Q2 under the business-of-parts paragraph. Not fast-moving technology in the
sense of Q1's routing: the product (a verified record) has been the same since the Work Number's start; the channel has
changed.

**VERDICT: IN.** The earning power can be pictured five to ten years out from the filings' own variables, records,
price, the mortgage cycle seen whole, with the durability of the moat sent to Q2 **[M2012-065]**, **[M1998-044]**,
**[M2011-014]**. The doubts about regulation and substitutes are written down above and carried.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The moat is what "protects
excellent returns on invested capital" **[L2007-004]**; it is judged, not measured **[M1999-108]**.

### The parts table (the business-of-parts paragraph, section B)
The filer reports three parts with plainly different economics, and "lumping them together [...] impedes analysis"
**[L2008-005]**. Segment operating income as filed (segment notes of the FY2023 and FY2025 10-Ks, `0000033185-24-000017`,
`0000033185-26-000010`; FY2021 10-K `0000033185-22-000014` for 2021), before the unallocated general corporate expense:

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share | Decides? |
|---|---|---|---|---|---|---|---|---|
| Workforce Solutions | $1,000.7M | $1,006.0M | $969.3M | $1,053.3M | $1,141.5M | $5,170.8M | 63.1% | **yes, more than half** |
| U.S. Information Solutions | $551.8M | $402.1M | $365.0M | $404.4M | $475.2M | $2,198.5M | 26.8% | no |
| International | $141.9M | $147.0M | $167.8M | $181.2M | $182.5M | $820.4M | 10.0% | no |

Workforce Solutions decides. (The general corporate expense, $499M to $704M a year, is not allocated by the filer; the
share above is of the segments' own operating income.) The file closes on Workforce Solutions' castle; the other two are
read so that they can be carried correctly to Q7.

### Workforce Solutions, the deciding part: the castle tests, each with its filing fact
Segment revenue and operating margin, as filed (FY2018 10-K `0000033185-19-000007` for 2016 to 2018; FY2021 10-K for
2019 to 2021 as restated after the consumer segment was folded in; FY2023 and FY2025 10-Ks for 2022 to 2025):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue $M | 702.2 | 764.2 | 826.8 | 971.1 | 1,461.7 | 2,035.4 | 2,325.4 | 2,315.8 | 2,433.8 | 2,582.3 |
| Operating margin | 42.1% | 43.4% | 40.2% | 40.3% | 48.2% | 49.2% | 43.3% | 41.9% | 43.3% | 44.2% |

1. **The key factors, and how permanent** **[M1995-038]**. The Work Number holds employers' payroll records, which
   employers generally contribute free because the service "relieves them of the administrative burden and expense of
   responding to third-party employment verification requests" (FY2025 10-K, Item 1). The file grew from payroll data of
   "over 7,100 organizations" (FY2016 10-K) to "over 4 million organizations" and 209 million active records (FY2025).
   The factor is a two-sided network: verifiers come because the records are there, employers stay because the verifiers
   are served. Its weakness is named by the filer: "our data sources could withdraw, delay receipt of, or increase the
   cost of, the data they provide to us", and "We also compete with several of our third-party data suppliers" (FY2025
   10-K, Item 1A). The jump from thousands of contributors to millions implies contribution through payroll providers,
   who hold the same data; the filing does not name them or their share.
2. **Would it stand without the lord?** Yes: the margin held above 40% under two chief executives and through the 2017
   breach; nothing in the filings ties it to one person.
3. **The money test** **[M2011-015]**. Against: from FY2024 the filer itself calls verification "highly competitive with
   low barriers to entry" (FY2024 and FY2025 10-Ks, Competition; absent from the FY2016 to FY2023 10-Ks), and names as
   rivals "employers who manage verifications in-house, lenders who obtain verifications directly from employers, and
   numerous online and offline firms", and third parties "seeking employee credentials to access information systems".
   For: the rivals it named in 2016 and 2020 (Verify Job System, Corporate Cost Control, Thomas & Company, First
   Advantage) did not stop revenue rising 3.7 times in nine years at margins never below 40%. The rows ask "why are there
   no new entrants into the field? [...] Normally, if you’ve got a profitable business, you know, a dozen people want to
   go into it." **[M2000-077]**: here entrants exist and are named, and the margins have not moved. The new wording
   arrived the year the antitrust suit was filed, and a defendant accused of monopoly has a reason to write it; that does
   not make it false.
4. **Pricing power, and the agony before a rise** **[M2005-020]**. Through the mortgage trough, when the filer reports
   inquiries falling more than 20% in 2022 and "significantly" again in 2023, segment revenue held ($2,325.4M, then
   $2,315.8M) and the margin stayed at 43.3% and 41.9%. Growth came from government, talent and consumer lending, and the
   Q2 2026 release reports Workforce Solutions mortgage revenue up 8% (exhibit 99.1, `0000033185-26-000024`). That is
   the behaviour of a price that holds. The rows add the warning that comes with it: "If you name some business that has
   incredible pricing power, you’re talking about a business that’s a monopoly or a near monopoly." **[M2010-092]**, and
   a near monopoly draws attackers of its own: the antitrust class action of May 28, 2024 on behalf of "all persons who
   purchased electronic verification of income and employment services from May 28, 2020 to present" (FY2025 10-K,
   Item 3), and the CFPB's three CIDs on Workforce Solutions' data accuracy (2023 to 2024, open at Q2 2026). Price
   pushed past the moat shows the moat smaller than thought **[M2001-087]**; no filing yet shows lost share.
5. **Unit volume.** The unit the filer reports, records, rose every year from 2021 to 2025 (535M, 600M, 657M, 734M, 813M
   total; 168M, 188M, 209M active from 2023): the visible measure of the network.
6. **Does it take adversity and still do well?** The 2017 breach is the largest test this file has: "if you see a
   business take a lot of adversity and still do well, that tells you something about the underlying strength of the
   business" **[M2000-032]**. The filer says its customer relationships "were damaged following the cybersecurity
   incident in 2017, resulting in a negative impact on our revenue for a period of time" (FY2025 10-K, Item 1A);
   Workforce Solutions revenue nevertheless rose 8% in 2018 (and $971.1M in 2019 on the restated basis). The customers
   did not leave, as with the card in the salad-oil scandal: "nobody quit using the card" **[M2018-073]**.
7. **Ask the competitors** **[M1999-130]**. TransUnion's FY2025 10-K names Equifax first among its U.S. competitors
   ("Equifax, Experian and LexisNexis", Competition, `0001552033-26-000012`) and claims no employment-verification line.
   The only SEC filer Equifax has named in verification, First Advantage, is a screening business earning operating
   margins of 9.0% (2021), 11.6% (2022), 10.7% (2023), a loss in 2024 and 8.4% (2025) on its own filings (XBRL
   OperatingIncomeLoss over revenue; FY2025 10-K `0001193125-26-076740`). Experian, the other large bureau and verifier,
   is not an SEC filer (listed in London) and its figures could not be read under the brief: **flagged**. The private
   verification firms the filer alludes to file nothing.
8. **Widening or narrowing** **[L2005-010]**. Widening on records and contributors; the margin is back from the 2023
   trough to 44.2% in 2025 and 44.9% in Q2 2026 (exhibit 99.1).
9. **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: (a) a court or regulator
   remedy on price or on access to the file (the antitrust suit, the CFPB); (b) payroll providers withdrawing their data
   or selling verifications themselves; (c) lenders and agencies accepting consumer-permissioned payroll connections in
   place of the employer file. Each would reduce more than destroy: the file would remain the largest, but its price
   could fall toward its cost. None of the three shows in any filing as having happened. Slow change "can lull you to
   sleep easier" **[M2014-038]**; it is the first thing a holding review would read.

### The competitor row (same metric, own filings, whole span)
Operating margin, GAAP operating income over revenue (each company's 10-Ks, XBRL OperatingIncomeLoss and revenue,
cross-read against the filed statements for the latest year: TransUnion FY2025 revenue $4,576.3M and operating income
$857.8M in its income statement, `0001552033-26-000012`; Fair Isaac FY2025 (September year) total revenues $1,990.9M and
operating income $924.9M, `0000814547-25-000030`):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Equifax, consolidated | 26.2% | 24.7% | 13.1% | -9.6% | 16.4% | 23.1% | 20.6% | 17.7% | 18.3% | 18.0% |
| Equifax, Workforce Solutions | 42.1% | 43.4% | 40.2% | 40.3% | 48.2% | 49.2% | 43.3% | 41.9% | 43.3% | 44.2% |
| Equifax, USIS | 43.4%* | 42.7%* | 35.4%* | 32.3% | 30.1% | 30.9% | 24.3% | 21.2% | 21.4% | 22.9% |
| Equifax, International | 13.9% | 18.2% | 11.2% | 10.9% | 7.9% | 12.9% | 12.9% | 13.7% | 13.4% | 12.9% |
| TransUnion | 17.6% | 24.0% | 22.1% | 22.0% | 19.8% | 22.0% | 16.9% | 3.4%** | 15.9% | 18.7% |
| Fair Isaac (Sept. years) | 19.3% | 19.5% | 17.5% | 21.9% | 22.9% | 38.3% | 39.4% | 42.5% | 42.7% | 46.5% |
| First Advantage | n/a | n/a | n/a | n/a | n/a | 9.0% | 11.6% | 10.7% | -7.2% | 8.4% |
| Experian | not an SEC filer: not read, flagged | | | | | | | | | |

\* USIS before 2019 excludes the consumer business then reported separately (Global Consumer Solutions), so 2016 to 2018
are not on the same basis as 2019 onward. \*\* TransUnion 2023 carries a $414.0M goodwill impairment. Equifax 2018 to
2020 carry the breach costs and the 2019 settlement accrual. First Advantage before 2021 is not on a comparable public
basis.

### The field's returns over the last full cycle (section C)
The mortgage cycle runs, on the filer's own description, from the 2019 base (mortgage 20% of revenue) to the 2020 and 2021
boom (32% in 2020) to the 2022 and 2023 fall in inquiries. Across it Workforce Solutions never earned below a 40% margin.
Its 2025 operating income of $1,141.5M was earned on segment assets of $4,067.6M, of which $2,574.1M is goodwill paid for
acquisitions (segment note and goodwill table, FY2025 10-K), so on the capital the business itself needs it earns far
more than an ordinary return; for the business, "forget about goodwill" **[M2011-060]** (it comes back at Q6, "because we
paid for it"). TransUnion and Fair Isaac earn high returns in the same field. This is a field whose durable players earn
excellent returns, not the "ordinary returns" the section-C exclusion is about.

### The two parts that do not decide
- **USIS: standing, narrowing.** One of three national bureaus, and mortgage lenders buy from all three (the tri-merge
  report, Item 1); revenue rose from $1,531.2M (2019, restated) to $2,078.5M (2025) and did not fall away after the
  breach. But its margin has roughly halved, 42.7% (2017, old basis) to 21.2% (2023) and 22.9% (2025); the filer names
  "higher royalty, revenue share and purchased data" costs and technology amortization (FY2025 10-K, MD&A), and says its
  mortgage growth came "primarily" from "product pricing" while volumes fell. Much of the price rise goes to the score
  supplier, whose own margin rose from 19.3% to 46.5% over the same years (table), and whose Mortgage Direct License
  Program TransUnion now lists as an uncertainty. "It is not what it was 20 years ago, relative to the competition"
  **[M1996-036]** fits the part. Not shown open on the evidence (no loss of customers or share in any filing), so it is
  carried with the company; its narrowing is weighed at Q3 and Q7.
- **International: ordinary.** Margins between 7.9% and 18.2% over ten years, 12.9% in 2025, on segment assets of
  $3,629.2M including $2,165.4M of goodwill (Asia Pacific $1,349.8M, Latin America $532.0M, Europe $189.6M, Canada
  $94.0M); the Asia Pacific goodwill test has the smallest cushion and the filer says that unit "is at risk of a possible
  future goodwill impairment" (FY2025 10-K, Critical Accounting Policies). Judged in words, as section C asks: an ordinary
  return. It does not decide; it is carried to Q7 at no growth.

### VERDICT: IN
The deciding part's castle stands on the evidence of a full mortgage cycle and of the 2017 breach: a two-sided network
of over 4 million contributors and 209 million active records, margins never below 40% in ten years, revenue held through
the trough and grown after the breach **[M1995-038]**, **[M2000-032]**, **[M2005-020]**. It is not shown open, and its
future can be judged in the sense the rows ask, by the network's size and the customers' dependence on it, with three
named threats (regulator or court, contributors, consumer-permissioned substitutes) recorded as what would "modify, or
reduce" it **[M2000-014]**. The strongest evidence against, the filer's own "low barriers to entry" and the pricing that
has drawn an antitrust suit **[M2010-092]**, is carried to Q7's certainty and to any later holding review. USIS is
carried with the company, narrowing; International is carried at no growth.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"The best business is one that gives you more and more money every year without putting up anything to get it, or very
little" **[M1998-081]**; the capital is "the capital actually needed in the business" **[M2010-090]**, and the added
capital is judged by "what it can earn on incremental invested assets" **[M2000-065]**.

**The capital the business needs.** Workforce Solutions spent $127.5M, $96.0M and $95.8M of capital in 2023 to 2025
against segment operating income of $969.3M, $1,053.3M and $1,141.5M (FY2025 10-K, segment note): the deciding part
throws off far more than it consumes. On the company's own net tangible capital (equity plus debt less cash, goodwill and
intangibles: $4,604M + $5,093M - $181M - $6,746M - $1,331M = about $1.4B at 2025-12-31, ten-year table at Q4) the 2025
operating income of $1,095.2M is a very high return. On the capital the business needs, it is a See's-type figure.

**What the added capital has earned.** The filed cash-flow statements (10-Ks FY2016 to FY2025, accessions at Step 0;
tagged figures cross-read for 2025), $M:

| Year | OCF | Stock pay | Capex | Owner cash (OCF - stock pay - capex) | D&A | of which acquired-intangible amortization | Acquisitions paid |
|---|---|---|---|---|---|---|---|
| 2016 | 823.0 | 37.1 | 173.5 | 612.4 | 268.7 | 176.5 | 1,791.6 |
| 2017 | 816.0 | 38.3 | 218.2 | 559.5 | 290.9 | 172.2 | 139.9 |
| 2018 | 672.2 | 42.5 | 321.9 | 307.8 | 315.9 | 152.8 | 138.3 |
| 2019 | 313.8 | 49.7 | 399.6 | -135.5 | 337.3 | 140.1 | 272.9 |
| 2020 | 946.2 | 54.7 | 421.3 | 470.2 | 399.3 | 141.8 | 61.4 |
| 2021 | 1,334.8 | 54.9 | 469.0 | 810.9 | 489.6 | 176.4 | 2,935.6 |
| 2022 | 757.1 | 62.6 | 624.5 | 70.0 | 568.6 | 236.7 | 433.8 |
| 2023 | 1,116.8 | 71.8 | 601.3 | 443.7 | 619.8 | 250.7 | 283.8 |
| 2024 | 1,324.5 | 81.6 | 511.5 | 731.4 | 680.6 | 261.1 | 0.0 |
| 2025 | 1,615.7 | 78.4 | 481.4 | 1,055.9 | 726.9 | 250.2 | 74.1 |

(2019 and 2022 carry breach settlement payments of $341.5M and about $345M: payments of $443.6M through 2021 and $788.6M
through 2022, FY2019, FY2021 and FY2022 10-Ks, Liquidity.)

Over 2017 to 2025 the company paid $4,339.8M for acquisitions and spent $4,048.7M of capital, of which about $1,402M
exceeded its depreciation and non-acquisition amortization: roughly $5.7B of added capital. Owner cash went from $612.4M
(2016) to $1,055.9M (2025), and operating income before acquired-intangible amortization from $1,001.6M to $1,345.4M. On
the added $5.7B that is an added $0.44B of owner cash, under 8% after tax, and $0.34B of pre-tax operating income, about
6%, even crediting the acquisitions with all of the organic growth. Part of the explanation is that 2016's cost base
was too low: it did not carry the security the breach showed was missing, and the incident's own costs of $1,142.5M
(2017 to 2020) and settlements of $802.2M are the price of that. Either way, "we’re not earning a higher rate of return on
capital than we were when we started. We just put way more capital into the business" **[M2023-081]** describes the
company's record better than the See's line does. Between the three accounts of **[L2007-010]**, the operating business
is the great one and the acquisition and rebuild spending has so far behaved like the gruesome one, which "requires you
to keep adding money at those disappointing returns".

**Reinvestment to stand still, and the transformation.** Capex rose from 5.5% of revenue (2016) to 12.2% (2022) and is
back to 7.9% (2025); D&A other than acquired-intangible amortization rose from $92.2M to $476.7M and now equals capex
($481.4M), and the filer expects capex "for the next twelve months to be down from current levels" (FY2025 10-K, Other
Planned Uses of Capital). The filing gives no maintenance figure **[M2000-144]**, **[L1999-024]**; the amortization of
the rebuilt software is a real cost (Q4), so the run takes capital spending as roughly the cost of standing still now.
"Every year we spend amounts equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**.

**WEIGHS AGAINST, on the added capital.** The deciding business needs little capital and earns very high returns on what
it needs **[M1998-081]**, **[M2010-090]**; but the company has put about $5.7B in since 2016 for about $0.44B more owner
cash a year **[M2000-065]**, **[M2023-081]**, and the acquisition habit continues (Círculo de Crédito, $750M enterprise
value, signed July 2026). The weighing is carried to Q6 (the money) and Q7 (the growth credited).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]**. `tools/run.py` table (first-filed
tagged values, $M), read against the filed balance sheets of the FY2025 10-K and the segment and debt notes:

| Year-end | Assets | Equity | Cash | Receivables | Goodwill | Intangibles | Total debt | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 6,664 | 2,663 | 129 | 433 | 3,974 | 1,324 | 2,672 | 4,153 |
| 2017 | 7,233 | 3,174 | 336 | 445 | 4,184 | 1,247 | 2,704 | 4,601 |
| 2018 | 7,153 | 3,108 | 224 | 469 | 4,130 | 1,099 | 2,636 | 4,718 |
| 2019 | 7,909 | 2,579 | 401 | 532 | 4,308 | 1,045 | 3,383 | 4,132 |
| 2020 | 9,612 | 3,168 | 1,685 | 631 | 4,496 | 998 | 4,378 | 4,185 |
| 2021 | 11,041 | 3,584 | 225 | 728 | 6,258 | 1,898 | 5,295 | 4,752 |
| 2022 | 11,548 | 3,956 | 285 | 858 | 6,384 | 1,818 | 5,787 | 5,256 |
| 2023 | 12,280 | 4,534 | 217 | 908 | 6,830 | 1,859 | 5,711 | 5,609 |
| 2024 | 11,759 | 4,797 | 170 | 958 | 6,548 | 1,521 | 5,010 | 6,019 |
| 2025 | 11,864 | 4,604 | 181 | 1,013 | 6,746 | 1,331 | 5,093 | 6,445 |

What the figures say: (1) goodwill and acquired intangibles, $5.3B in 2016, are $8.1B in 2025, more than the whole of
equity ($4.6B): tangible equity has been negative throughout, and the company's growth in assets is bought growth (2021
alone added $1.8B of goodwill, the $2.9B of 2021 purchases). (2) Debt doubled, $2.7B to $5.1B ($5.5B at 2026-06-30, Q2
10-Q), with cash kept near $0.2B except the 2020 build ahead of the settlement and the 2021 deals. (3) Retained earnings
fell in 2019 by the breach loss (net loss $384.1M) and have risen every year since. (4) Receivables rose faster than
revenue: 13.8% of revenue in 2016, 15.2% in 2019, 16.8% in 2022, 16.7% in 2025; prepaid expenses ($144.2M) and other
current assets ($74.5M) are small and not building (FY2025 balance sheet). The receivables drift is noted, not
suspicious on its own: the government vertical grew in the same years. (5) Capitalized internal-use software stands at
$3,098.2M gross (FY2025 balance sheet), the cloud rebuild held as an asset and amortized. What they cannot say: whether
the $6.7B of goodwill was worth what was paid; the Asia Pacific test already has the thinnest cushion (Q2).

**The real costs.**
- *Depreciation and software amortization.* Real: "With software, for example, amortization charges are very real
  expenses" **[L2012-003]**. The owner-cash figure (OCF less stock pay less all capex) charges the rebuild in full as
  it is spent, and capex now equals non-acquisition D&A (Q3), so the two bases meet.
- *Acquired-intangible amortization* ($250.2M in 2025): the purchase-accounting kind the same row calls "clearly not
  real expenses" **[L2012-003]**; owner cash does not charge it, and the acquisitions themselves are charged at Q7 (c).
- *Stock pay* ($78.4M in 2025) is deducted **[L2015-003]**.
- *The breach.* $1,142.5M of incident costs net of insurance (2017 to 2020) and $802.2M of settlements paid through
  2023. The company reports them as items outside "adjusted" earnings; the rows call the exclusion of rare large losses
  "deceptive nonsense" **[L2002-002]**, so the run counts the settlement payments in the years they were paid (2019,
  2022) and does not remove them.
- *Restructuring, "realignment of resources and other costs".* $46.1M (2018), $48.0M (2024), $49.9M (2025), and again
  among the Q2 2026 adjustments: recurring, and counted. "to tell owners year after year, "Don't count this," when
  management is simply making business adjustments that are necessary, is misleading" **[L2016-007]**.

**EBITDA and the adjusted figure, in the filer's own mouth.** Every release leads with adjusted EPS and gives guidance in
adjusted EPS and adjusted EBITDA (2026 midpoint "Adjusted EBITDA is $2.12 billion", exhibit 99.1 of 2026-02-04,
`0000033185-26-000004`). For 2025, adjusted EPS was $7.65 against GAAP $5.32: the bridge adds back acquired amortization
$250.2M, realignment $49.9M, "acquisition-related costs other than acquisition amortization" $35.0M, a legal settlement
$30.0M, antitrust litigation costs $5.4M and the breach accrual $1.0M. In 2024 the same bridge added back $68.4M of
"acquisition-related costs" described as "integration costs resulting from recent acquisition activity" in a year in
which the 10-K says "we did not complete any acquisitions", and $15.0M for the CFPB penalty. The release reconciles
every item to GAAP, and the 10-K itself reports GAAP. "a management that regularly attempts to wave away very real costs
by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; EBITDA is "the one figure we regard as
utter nonsense" **[M1998-086]**; and the company gives quarterly guidance **[L2019-006]**. By the 2026-10-06 rule these
are recorded here as a weighing against **[M1994-018]** and carried to Q5.

**Confusion or suspicion?** No. The statements are clear, the segment notes reconcile to the consolidated figures, the
breach accruals and payments are disclosed year by year, and none of the tells that live in the accounts appears:
prepaid and deferred accounts are not building, there are no inventories, and no reserve is seen to move with a
financing **[M1995-064]**. Nothing confuses **[M1995-063]**.

**VERDICT on the accounts: IN (no STOP); WEIGHS AGAINST.** The figures show what the business earns once owner cash is
taken after stock pay, all capex, restructuring and the settlement payments; the featured adjusted EPS and EBITDA, with
recurring items waved away, weigh against and go to Q5 **[L2016-006]**, **[L2016-007]**, **[M1994-018]**. Recast
earnings for Q7: owner cash as in the Q3 table.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
"you judge management by two yardsticks. One is how well they run the business [...] And then the second thing you want
to figure out is how well that they treat their owners" **[M1994-008]**; for a marketable stock the reading is "reports
rather than any intimate personal knowledge", the proxy above all **[M1994-009]**.

**Who.** Mark W. Begor, chief executive since April 2018, before that 35 years at General Electric and two at Warburg
Pincus (FY2025 10-K, executive officers); John W. Gamble, Jr., CFO and COO. An independent chairman, Mark L. Feidler, a
director since 2007 (proxy of 2026-03-27). The 2017 breach happened under the previous chief executive; the board formed a
special committee to review it (FY2017 10-K, Item 1). The present team inherited the breach, the consent orders and the
rebuild.

**The record against the hand dealt.** Dealt in 2018: a breached company under four regulators' orders, a legacy data
centre estate, and a mortgage cycle about to boom and bust. Done since: the settlements paid ($802.2M through 2023), the
cloud migration brought to its "final stages" (FY2025 10-K, Item 1A), capex now falling back to D&A, Workforce Solutions
grown from $826.8M to $2,582.3M of revenue at margins above 40%. Against: USIS margins halved while TransUnion's held
roughly level over the same years (Q2 table); some $5.7B of added capital has earned under 8% (Q3); and compliance has
kept failing in ways regulators fined: a 2022 coding error that "impacted how some credit scores were calculated during a
three-week period", a CFPB consent order of January 2025 with a $15M civil penalty covering it and USIS dispute handling,
a $30.0M settlement in 2025 of four class actions over inquiry disputes, and an open CFPB investigation of Workforce
Solutions' accuracy (FY2024 and FY2025 10-Ks, Item 3; Q2 2026 10-Q, Note 6). When the coding problem surfaced, the filings
show it disclosed and settled, not hidden; "the main problem was they didn’t act when they learned about it"
**[M2017-005]** is not what the record shows.

**The tells, read from the reports.** (1) The habits carried from Q4: guidance every quarter in adjusted EPS and adjusted
EBITDA; adjusted EPS of $7.65 featured against GAAP $5.32; recurring realignment charges and settlements added back. (2)
The same adjusted figures pay the managers (below): Corporate Adjusted EPS decides the chief executive's whole annual
bonus, and Adjusted EBITDA decides 30% of his long-term award. (3) The language of the reports is promotional: "Equifax
AI Data Moat", "the New Equifax", "on offense" (proxy, letter section; exhibit 99.1 of 2026-07-21). A report that sounds
like "the product of some investor relations department" tells something **[M2007-083]**. (4) Against the tells: the
10-K is candid about the breach and its damage ("our reputation with consumers and other stakeholders and our customer
relationships were damaged", Item 1A), names its own competition as having "low barriers to entry", and reconciles every
adjusted figure to GAAP, which is what owners would want to be told **[M1998-036]**. The stock price is not the centre of
the pay: relative TSR is 30% of the long-term award, and stock price emphasis of the kind that "make us nervous"
**[M2004-067]** does not appear beyond that.

**Integrity on doubt** **[M2013-088]**. The question is whether the record leaves a doubt about honesty, not about
competence. The compliance failures are failures of control, disclosed and paid for; nothing in the filings shows a
figure misstated, a reserve moved or a fact concealed. The adjusted-earnings habit and the pay tied to it are the kind of
thing that "makes us nervous" because "bad behavior is contagious" **[L2016-006]**, and they are recorded as such; they
are the conduct the gaps case of 2026-10-06 sends here to be read with the rest, and with the rest they do not amount to
doubt about the people's honesty. This is a judgment, written down with the evidence that could reverse it: an adverse
finding in the CFPB's Workforce Solutions accuracy investigation, or any restatement, would be the fact that does.

**Love of the business, and after the pay.** Mr. Begor owns 90,660 shares, 200,448 deferred share units and 409,244
exercisable options (proxy, ownership table as of March 9, 2026), above the six-times-salary rule; the holdings came from
grants, not purchases. His reported pay was $13.0M (2023), $14.8M (2024) and $23.4M (2025), the last after the committee
raised his long-term target from $10.1M to $17.1M, which in the committee's words "aligned his annual target compensation more
competitively with market practices", in a year in which operating income rose 5% (proxy, CD&A). Weighed at Q6, Part B.

**VERDICT on integrity: IN** (no doubt on honesty from the filings; the adjusted-earnings habit, the pay on the adjusted
figures and the compliance record are recorded against) **[M2013-088]**, **[M2004-067]**, **[L2016-006]**. **Ability
WEIGHS UNDECIDED:** the rebuild and the Workforce Solutions growth for it; the USIS margin, the returns on added capital
and the repeated compliance failures against; "if the CEO's talents or motives are suspect, today's value must be
discounted" **[L2010-002]**, and the discount is taken in Q7's certainty, not as a stop.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
**The retention test** **[R1995-009]**, **[M1998-110]**, over the five years 2021 to 2025. Net income attributable to
Equifax $3,250.1M (744.2, 696.2, 545.3, 604.1, 660.3); dividends paid $998.9M; so $2,251.2M retained, and in the same
years net debt rose from $2,693M (2020: debt $4,378M less cash $1,685M) to $4,912M (2025), another $2,219M put in.
Market value, at aggregator closes (flagged): end-2020 121.8M shares x $192.84 = $23,488M; end-2025 about 120.7M shares
(117.6M at 2026-06-30 plus the 3.1M bought in the first half) x $216.98 = $26,190M; with the $997.4M of buybacks added
back, a gain of about $3.7B against $2.25B retained: passed at end-2025, narrowly, and only before counting the $2.2B of
added debt. At today's price (117.485M x $142.40 = $16,730M, plus all buybacks since 2021 of $1,557M) the same five-plus
years show a loss of about $5.2B in market value against more than $2.25B retained: failed. The market leg alone misleads
when prices fall **[R2009-002]**, so the intrinsic leg is read at Q7; what the market leg shows is that the retained and
borrowed money of these years, mostly spent on the $3.7B of acquisitions of 2021 to 2025 (Q3 table), has not yet shown
up as value an owner can see. Weighs against **[M1998-110]**.

**Buybacks.** None from 2018 to 2024 apart from $69.9M in 2021; then $927.4M in 2025 (4,006,173 shares, about $231
each), $560.0M in the first half of 2026 (3,107,628 shares, about $180), under a $3B authorization of April 2025 that
names no price (FY2025 10-K, MD&A; Q2 2026 10-Q, equity note). Bought with "cash plus sensible borrowing capacity"
**[L1999-023]**: commercial paper rose $474.7M in 2025 and total debt rose to $5,485.3M by June 2026, so part of the
buyback was borrowed. A programme that names no price weighs against, "entirely purchase-price dependent"
**[L2016-002]**, unless the prices paid sit at or below the bottom of the Q7 range; that test is run at Q7 and recorded
below.

**Issuance and deals.** No stock-paid acquisition in the ten years: every deal was for cash (cash-flow statements), so
the one STOP of Part A, the all-stock deal by an undervalued acquirer **[L2009-019]**, does not arise. Shares
outstanding drifted up from 121.2M (2019) to 124.0M (2024) through stock pay, before the buybacks. The deals themselves
are the question: $6.1B paid in ten years (largest: $2.9B in 2021, adding $1.8B of goodwill; Boa Vista in Brazil in
2023) for the returns Q3 found, and the next ($750M, Mexico) already signed. The 10-K offers no post-mortem of the deals
against what was expected of them **[L2014-013]**; its acquisition strategy is "accretive and strategic acquisitions
that drive incremental annual revenue growth" (Item 1), a revenue test, not a value test.

**Dividends.** $1.56 a share a year through 2024, $0.50 a quarter from Q2 2025: steady, a small part of earnings.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**. The chief executive's annual bonus rests "exclusively" on
  Corporate Operating Revenue and Corporate Adjusted EPS; his long-term award is 30% relative TSR shares, 30% Adjusted
  EBITDA shares, 20% options priced at 110% and 120% of the grant-date price, 20% time-vested RSUs (proxy, CD&A). The
  measures are revenue and adjusted profit, with acquired amortization and recurring charges added back, and none
  charges for the capital used: an acquisition that adds revenue and adjusted EBITDA pays the managers whatever it earns
  on its price. "you get what you reward for" **[M2016-083]**. The premium-priced options are the one feature that asks
  for a gain before paying.
- **Treatment of themselves against the owners** **[M1994-009]**. Reported pay of the chief executive rose from $14.8M
  to $23.4M in 2025, with operating income up 5% and the stock down 15% over the year (from $254.85 to $216.98,
  aggregator closes).
- **The board.** An independent chairman separate from the chief executive; that is the structure the rows prefer to a
  combined post **[L2014-026]**. Directors' holdings were not traced to purchases (the ownership table shows holdings,
  not their source); not credited.
- **Owners as partners.** Quarterly guidance **[L2019-006]** and adjusted figures featured (Q4); the 10-K is otherwise
  full and plain.

**WEIGHS AGAINST, both parts.** Part A: the retained and borrowed money has gone mainly into acquisitions at low returns
(Q3), the market leg of the retention test fails at today's price, and the buyback names no price and was partly
borrowed **[L2016-002]**, **[L2011-003]**. Part B: pay on revenue and adjusted earnings with no charge for capital, and a
large rise in 2025 **[M2003-019]**, **[M2016-083]**; the independent chairman is for.

**The buyback-price test, recorded back from Q7 (run when Q7 was reached, as Q7's specifics require).** The prices paid,
about $231 (2025) and about $180 (first half of 2026), sit far above the bottom of the Q7 range on every basis computed:
nil on the default pair, $70.62 on the organic pair, $93.93 on the equity-only organic case. The exception for a
priceless programme does not apply; the buyback weighs against, as written above **[L2016-002]**, **[L1999-023]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be?" with
the long government rate as the third question **[L2000-021]**, and "are you going to have to put more cash into after
you buy it?" **[M2014-068]**. Arithmetic in `Test Runs/_research 2026-10-07 EFX/q7_range.py`; every input is a filed
figure named in Q3 and here.

**Inputs.** Owner cash (OCF less stock pay less all capital spending; Q3 table) 2021 to 2025: $810.9M, $70.0M, $443.7M,
$731.4M, $1,055.9M, average $622.4M (equity-only basis). All-equity basis: interest paid ($139.7M, $161.7M, $231.5M,
$214.9M, $209.7M, cash-flow supplementary data) added back after each year's own effective tax rate (21.1%, 24.7%, 23.2%,
25.1%, 25.8%, tax over pre-tax income as filed): $921.1M, $191.8M, $621.6M, $892.4M, $1,211.6M, average **$767.7M**.
Acquisitions net of divestitures paid in the window: $2,935.6M, $433.8M, $276.9M, $0, $72.9M, average $743.8M. Net debt
at 2026-06-30: total debt $5,485.3M less cash $170.1M = **$5,315.2M** (Q2 2026 10-Q, balance sheet and debt note);
operating leases ($148.9M of payments, FY2025 10-K) left out, as the convention says; the subsequent events the 10-Q
states are the Círculo de Crédito agreement ($825M purchase price, $750M enterprise value, expected to close in Q4 2026),
which is a commitment, not yet debt, and is not added. Rate 5.64%. Shares 117.485M.

**The specifics, applied.**
- *(a) Cycles.* The window opens in 2021, the top of the mortgage boom on the filer's own description (inquiries
  expected to fall more than 20% in 2022, then "significantly lower" in 2023), and 2022 is aberrational on the filer's
  description (the $345M breach settlement payment). The last full cycle, trough to trough on the filer's account, is
  2019 to 2023; its all-equity average is $453.2M, shown beside. The literal window is the central figure because the
  cycle base would put two breach payments and the transformation's peak capex in the base; both are shown.
- *Growth shown.* All-equity owner cash grew 7.09% a year between the end years (921.1 to 1,211.6); the
  halves method gives 29% because 2022 carries the breach payment, which makes it meaningless, so it is not used.
- *(c) Acquisitions.* Default pair: deducted, with total growth credited. Organic pair beside: left out, with the
  filer's organic growth credited; the filer reports organic local-currency revenue growth only by period in releases
  (about 10% guided for 2026); for 2025 its reported and local-currency growth were both 7% with an immaterial
  acquisition, so 7.0% is used, inside the shown cap.
- *(e) Growth spending.* The filing allows no maintenance figure (Q3); all capex is charged; capex now equals
  non-acquisition D&A, so the D&A variant gives nearly the same 2025 figure ($810M on the D&A basis against $1,056M on
  capex, `tools/run.py`; the D&A basis is lower because D&A still carries the rebuild's amortization).
- International (10.0% of segment profit) carried at no growth (Q2). *(f)* No rate above 5.64% after year ten.

**The range** (per share, against $142.40):

| Case | Base | Growth | Range | Width | Fair price |
|---|---|---|---|---|---|
| **All-equity, default pair (acquisitions deducted, total growth)** | $23.8M | 7.09% | **nil** (-$41.64 to -$39.20) | n/a | **nil** (-$42.63) |
| All-equity, organic pair (acquisitions left out, 7.0%) | $767.7M | 7.0% | $70.62 to $147.98 | 2.10x | $38.51 |
| All-equity, organic pair, breach payments added back | $840.3M | 7.0% | $81.57 to $166.25 | 2.04x | $46.43 |
| All-equity, cycle base 2019-2023, organic | $453.2M | 7.0% | $23.15 to $68.82 | 2.97x | $4.20 |
| Equity-only, organic pair | $622.4M | 6.82% | $93.93 to $154.60 | 1.65x | $67.41 |
| Equity-only, default pair | -$121.5M | n/a | nil | n/a | nil |

What the default pair says: over 2021 to 2025 the company spent on businesses almost exactly what its operations threw
off before interest ($743.8M a year against $767.7M), so the whole of the owner cash of those years was put back in,
and on the rule that is the cash the owner did not get **[M2014-068]**, **[L2000-023]**. The organic pair asks the
kinder question, what the business is worth if it stopped buying and kept growing 7% on its own, and even then the
price sits inside the range, near its top.

**At the price.** The enterprise value at $142.40 is $22,045M. On the organic base of $767.7M the price yields 3.5%
with no growth; to earn 10% the base would have to grow about 16% a year for ten years; to be worth the price at 5.64%
it needs about 6.6% a year. The expected return at the price is below the floor of about ten percent on every case
computed: "there’s just a point at which we drop out of the game" **[M2003-149]**. Nothing here screams **[M2009-005]**;
the margin a run asks should grow as certainty falls **[M1997-080]**, and the certainty here is lowered by the Q2
threats, the Q3 returns on added capital and the Q6 habits.

**Value range (reporting figure, Part VII):** central, all-equity, default pair: **nil**; organic pair beside
**$70.62 to $147.98** a share; literal window 2021 to 2025, cycle base (2019 to 2023) beside at $23.15 to $68.82.
**Fair price (reporting figure, never a verdict; Part VII):** the price at which the midpoint of the range earns the
floor, after the company's own tax, read as the stream whose value at 5.64% equals the midpoint, discounted at 10%:
central all-equity **nil** on the default pair; **$38.51** all-equity and **$67.41** equity-only on the organic pair.
No cheap price is reported.

**VERDICT: OUT.** On the default pair the value per share is nil and the price is above it; on the organic pair the
range is narrower than three to one and the price sits inside it, near the top; on both the expected return at the price
is below the floor **[M2003-149]**, **[L2013-012]**, **[M2009-005]**. "a price that does not clear the floor" is the
section-I OUT; the file closes here.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q7** (the floor): central value nil on the default pair; organic range $70.62 to $147.98 against $142.40; fair
price nil central, $38.51 all-equity and $67.41 equity-only on the organic pair. Q1 IN, Q2 IN (Workforce Solutions
decides), Q3 weighs against, Q4 no stop and weighs against, Q5 integrity IN and ability undecided, Q6 weighs against.
No integrity facts left unjudged (Q5 was reached and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2.)* **[M1997-127]**
- **Q8:** the sovereign is 5.64% (Treasury, 2026-10-06); the owner-cash yield on the enterprise value at the price is
  3.5% (organic base). Recorded only.
- **Q9, debt and exposures:** total debt $5,485.3M at 2026-06-30, of which $1,410.3M short-term including commercial
  paper (Q2 2026 10-Q); $1.0B of notes due 2029 and 2033 sold in July 2026 to repay commercial paper (8-K
  `0001193125-26-323760`); revolver raised to $2.0B, $1.9B of it to August 2029 (8-K `0001193125-26-177620`); senior
  notes outstanding mature from 2026 to 2037 (FY2025 10-K, MD&A); covenant maximum leverage 3.75x EBITDA, in compliance;
  2025 operating income $1,095.2M against interest expense $212.3M, about 5.2 times; no rating triggers that accelerate
  debt; pension and post-retirement gross obligations $445.4M; outsourcing commitments about $1.1B; the Círculo de
  Crédito purchase ($825M) expected in Q4 2026; consent-order commitments from the 2017 breach, whose breach "could
  potentially result in fines, penalties and new business practice commitments" (FY2025 10-K, Item 1A); Canadian breach
  class actions pending; the antitrust class action and the CFPB Workforce Solutions investigation open. Cash held abroad
  $167.4M.
- **Q10:** nothing beyond Q7.
- **Q12:** the business sells data about consumers, collected without their consent under the FCRA; none of the
  businesses Q12 names (casinos, tobacco, loading schemes, gambling) applies. Recorded only.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Commits: Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, then Q7 with the close in one commit (declared: Q7's OUT closes the file, so the close is Q7's own consequence). A timed session limit stopped the work after the Q2
      commit; the run resumed from the file on disk without refetching.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock was present in `Screens/_daily/`, held
      by the dispatching session (not touched). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top.
- [x] Every v5 id resolves (check script `check_ids.py` in the research folder: ids present, fragments in their rows, no
      E-ids); every filing fact carries its document and accession at first use; numbers carry a filing or the script.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after stock pay and all capital spending from the filed cash-flow statements, never net income; the
      sovereign from the Treasury; the price and the historical closes used at Q6 are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (Foundations); facts for the unreached questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year means, yields and implied growth were not.
- [x] `python tools/check_framework.py` run before the closing commit: PASS (2026-10-07); `check_ids.py`: PASS.
- Departures, declared: (1) segment margins for 2016 to 2018 are on the old segment basis (noted in the table); (2) the
  2022 and 2019 breach payments are taken from cumulative totals in successive 10-Ks, so the yearly split is derived;
  (3) end-2025 share count for the retention test is derived (117.6M at June 30 plus the 3.1M bought), not filed; (4)
  the organic growth figure of 7.0% is the filer's 2025 reported and local-currency revenue growth, not an owner-cash
  organic rate, which the filer does not report.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 (c) breaks on a serial acquirer.** With acquisitions deducted and total growth credited, a window that holds a
$2.9B purchase gives a base near zero (here $23.8M on an all-equity average of $767.7M) and a negative value per share,
and specific (b)'s fallback for a series that "changes sign" does not say whether it applies to the base after the
deduction; I reported nil and showed the organic pair beside. The default rule penalises the window's largest deal year
in full while crediting only four years of its growth; a rule for averaging acquisition spend over a longer span, or for
crediting the acquired earnings on their own filed record, is missing. (2) **The fair price's "midpoint earns the
floor" is undefined as arithmetic**: the midpoint is a value, not a cash stream. I took the stream whose value at the
sovereign equals the midpoint and discounted it at 10%; another analyst could take the midpoint growth rate and get a
different figure. (3) **Q7 (a) and a breach year.** The cycle rule speaks of peaks and troughs of "owner cash as Q4
recasts it"; here the troughs are made by litigation payments, not by the cycle, and Q4 says catastrophe losses must be
counted. Whether a settlement year is "aberrational" (and so excluded from the base) or a real cost (and so kept) is
answered differently by Q7 (a) and by Q4's catastrophe-loss line; I kept them in the central figure and showed them
added back beside. (4) **EBITDA talk.** Q4's "What it rules OUT" lists "EBITDA as earnings and managements that talk
it" with the 2002 count of "about zero", while the gaps-case paragraph of 2026-10-06 sends a featured adjusted figure to
Q5 as a weighing. The filer gives guidance in adjusted EBITDA; I followed the newer paragraph, but the older list still
reads as a stop. (5) **Business of parts and unallocated corporate cost.** The share that decides is of segment operating
income; the general corporate expense ($704M in 2025, including technology, security and litigation) is not allocated,
and the paragraph does not say whether "five-year operating profit" means before or after it. Here it does not change
the deciding part. (6) **The brief.** Its line "If no STOP among Q1 to Q6 closes the file (Q3 and Q6 are weighings,
recorded and carried), do Q7 to Q10" omits that Q3, Q6 and Q9 each carry one narrower STOP (the framework's reading
rule; Q6's all-stock deal STOP is a real stop inside a weighing), and that Q12 follows Q10; and it lists Part VII among
the readings, whose own text still says "The run template for v5 does not yet exist", which is stale since adoption.
