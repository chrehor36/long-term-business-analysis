# Company Run — AMETEK, Inc. (NYSE: AME) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

A dispatched blind run under `Screens/_daily/_dispatch_brief.md` (operator rule ten). Analyst: a dispatched Claude session.
Working folder `Test Runs/_research 2026-10-10 AME/` (scripts committed; raw filings and XBRL in its `cache/`, gitignored).
No em dashes in my own prose; the template's own headings keep theirs.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared before any verdict (the blind rule).** Seen by accident and not used: (1) the session's opening
git status lists file names of other runs and research folders (a KLAC run file dated 2026-10-07; research folders for AYI and
ARCB) and the recent commit subjects, which name an ITW run (Q1 closed IN), a JKHY run, a KEYS run ("template copied before
any fetch") and a fold of re-run batch 5 that names boxes for ESI, HAS, GFF and GRMN; KEYS is one of my listed competitors,
and I used only Keysight's own SEC filings, never its run file or that subject line; (2) the lock file
`Screens/_daily/_overnight.lock`, read once to see whether a lock was held, reads "interactive AME and v5 re-runs batch 6";
(3) the auto-memory index loaded into the session says, of the queue, "57 gate-clearers, nothing buyable" and that five holding
reviews are owed. None names AME's box, holding or any view of AMETEK. Nothing else of the blind-listed files was opened,
listed or searched; `Test Runs/` was never listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $248.58 (close 2026-10-09, as printed by `python tools/run.py AME`; **aggregator, live quote only, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock $0.01 par, **229,261,244** shares (10-Q for
  the quarter ended 2026-06-30, filed 2026-08-04, accession `0001037868-26-000175`; cover date 2026-07-28;
  `python Screens/cover_shares.py AME`). Checked against issued less treasury at 2025-12-31 in the 10-K balance sheet
  (`0001037868-26-000016`): 270,471,745 issued less 41,434,441 treasury = 229,037,304; the small rise to the cover count is
  option exercises and grants (the 10-Q equity statement shows shares issued under employee plans). The two 8-Ks filed after
  the 10-Q (`0001037868-26-000183`, commercial paper programme raised to $3.5 billion; `0001037868-26-000191`, Indicor
  Instrumentation closed for cash) issue no shares. No other class; preferred authorised, none issued.
- **Market cap:** 229.261244M x $248.58 = **$56,990M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield on the US Treasury daily par yield curve,
  2026-10-09 (issuing authority; as printed by `tools/run.py`'s sovereign line, which reads `tools/sources.py`).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-17, `0001037868-26-000016`): Items 1, 1A, 3, 5, 7,
  7A, the statements and the notes on acquisitions, goodwill, debt, taxes, stock pay and segments; the 10-Q for Q2 2026
  (filed 2026-08-04, `0001037868-26-000175`); the proxy for the 2026 meeting (DEF 14A filed 2026-03-11,
  `0001037868-26-000062`; fetched at Step 0, read for Q5 and Q6); the 8-Ks of 2026-05-26 (First Aviation, `0001037868-26-000163`), 2026-06-12 (new revolver and
  $4.0 billion term loans, `0001037868-26-000166`), 2026-08-04 (Q2 release, `0001037868-26-000173`), 2026-08-11 and 2026-08-26
  (above); and the 10-Ks for FY2006 to FY2024 for the cycle, the segments and the acquisition record (accessions in
  `Test Runs/_research 2026-10-10 AME/annual_report_accessions.txt`). **One figure cross-checked against the filed statement:** cash
  provided by operating activities FY2025, $1,801,763 thousand on the filed Consolidated Statement of Cash Flows
  (`0001037868-26-000016`), against $1,801.8M in the XBRL series `tools/run.py` read: agrees.
- `python tools/run.py AME`, arithmetic lines only (its v4 material ignored, Part VII): OCF 2023/2024/2025 $1,735/1,829/1,802M;
  stock pay $46/48/48M (complete: the tool found no other stock-pay line); capex $136/127/130M; D&A $338/383/423M, of which
  amortization of acquired intangibles $215/248/277M (XBRL `AmortizationOfIntangibleAssets`) and depreciation $123/135/146M.
  The tool found no securities, software, intangible or rental spending inside or beside the cash-flow lines. The recast is
  at Q4 and the five-year owner cash at Q7; the tool's "owner earnings" on D&A charges amortization of acquired intangibles as
  if it were capital spending, which I do not use (Q4 says why).
- **The deal closed after the window, stated here because it changes the balance sheet before any question:** Indicor
  Instrumentation, "an all-cash transaction valued at $5.0 billion", closed 2026-08-26 (8-K `0001037868-26-000191`, Ex. 99.1),
  with "annual sales of approximately $1.1 billion" (10-Q `0001037868-26-000175`, Note on the Indicor agreement), financed by a
  $4.0 billion term loan in three tranches maturing three, four and five years after funding and up to $1.0 billion of revolver
  (8-K `0001037868-26-000166`). Net debt at the last filed balance sheet, 2026-06-30: total debt $2,036.2M less cash $495.4M =
  **$1,540.8M** (10-Q, Non-GAAP net debt table); with the Indicor financing the filing itself states added (Q7, On what the floor
  is earned): **$6,540.8M**. Operating leases ($288.2M at 2025-12-31) left out, as the convention says.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, so the questions below are about AMETEK's instrument and component businesses and the acquisition machine
that adds to them, never about the quotation. The market serves and does not instruct: "It just tells us prices." **[M2006-077]**;
the $248.58 quote is used only at Q7 and Q8. Margin of safety: if the decision needs pencil and paper "it’s too close to think
about" **[M1996-084]**. No macro forecast enters **[M2000-094]**: the filer's own cyclical end markets (aerospace, oil and gas,
process, power) are read as properties of the business at Q2 and Q7, not as a forecast. Who is paid to tell you: the filer's
own "AMETEK Growth Model" language and its EBITDA and "adjusted earnings" are management's selling words, read at Q4 and Q5.
The analyst's habits: I look for "what’s wrong in things" **[M2025-013]** and write contrary evidence down at once.

**Contrary evidence, written down as found** **[M1997-127]**:
1. (Step 0) A $5.0 billion all-cash purchase closed six weeks before the price date, about 9% of the market value, financed
   almost wholly with new bank debt of three-to-five-year maturities; net debt rises from $1.5 billion to about $6.5 billion.
2. (Step 0, 10-K Item 7) EIG, the larger group, shrank organically in 2025: "a 1% organic sales decrease"; the group's 5.6%
   sales rise came from acquisitions (6%) and currency (1%).
3. (Step 0, 10-K Item 1A) goodwill and other intangibles "totaled $11,299.2 million or 70% of our total assets" at 2025-12-31.
4. (Step 0) The filer features EBITDA in the 10-K highlights ("EBITDA ... was a record $2,296.9 million") and in each 10-Q, and
   its press releases speak of "adjusted earnings" (Indicor release, `0001037868-26-000191`).
5. (Step 0, 10-K Item 1) The filer claims "strong market share in a number of targeted niche markets" and names no share
   figure for any niche.

## THE STANDING RULE
The buyer would own a part-interest in a listed company bought with its own money and no borrowing; nothing in the purchase
gives anyone a claim on the buyer: "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and the rule is
"Never risk permanent loss of capital." **[L2023-005]**. The target's own debt, now raised by the Indicor financing, is the
target's, weighed at Q9, not the buyer's ruin. Sizing is Q10's. **No breach by the buyer's conduct.**

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic
dynamics of the industry" **[M2011-014]**. The tests applied:

- **What the business is** (10-K FY2025, `0001037868-26-000016`, Item 1): two groups. EIG designs and makes "advanced
  analytical, test and measurement instruments for the process, aerospace, medical, research, power and industrial
  markets" (process and analytical 70% of EIG sales; aerospace and power 30%). EMG makes "highly engineered medical
  components and devices, automation solutions, thermal management systems, specialty metals and electrical
  interconnects" and runs aviation MRO (automation and engineered solutions 70%; aerospace 30%). About 22,500 employees;
  48.2% of sales outside the US.
- **Which part decides** (Q1's holding-company paragraph, extended to segments by the parts convention): EIG earned
  **71.6%** of five-year (2021 to 2025) segment operating income (EIG $6,234.4M, EMG $2,473.0M; segment table in
  `Test Runs/_research 2026-10-10 AME/segments_table.txt`, transcribed from each year's 10-K MD&A). EIG decides; EMG is
  read but does not decide.
- **Test 2, the key variables and how predictable they are** **[M1998-044]**: for EIG, (a) the volume of niche instruments
  bought by industrial, process, aerospace, pharmaceutical and semiconductor customers through their capital cycles,
  (b) the price those instruments hold against rivals, (c) the margin. (a) is cyclical and the 10-K says so ("A number of
  the industries in which we operate are cyclical in nature"); (b) and (c) have a twenty-year record: EIG's margin was
  20.0% to 21.9% in 2005 to 2008, 20.3% in the 2009 trough, 24.5% to 27.1% through 2010 to 2022, and 28.4% to 30.7% in
  2023 to 2025. The past statements describe the later ones well (test 3, **[M2008-033]**): two full recessions (2009,
  2020) and one industrial downturn (2015 to 2016) moved the volume and barely moved the margin.
- **Test 5, would the insiders write it down** **[M2000-105]**: the filer writes down its own ten-year intent, "high single
  digit annual percentage growth in sales and double digit annual percentage growth in earnings per share over the
  business cycle" (10-K Item 1). That is a plan that relies on acquisitions, not a forecast of the existing businesses;
  the existing businesses' economics (margin, cash conversion, capital needs) are the part an insider would write down,
  and the record above is what the forecast would be built on. Not an industry the insiders would call "too hard".
- **Test 7, customers or technology** **[M2017-019]**: the products carry technology (spectrometers, electron microscopy
  microanalysis, 3D metrology, aircraft sensors) and the filer says "Approximately 27% of sales in 2025 were from products
  introduced in the past three years" (10-K Item 7). The rows' warning is "a technological component that’s of
  significance" **[M1998-008]**. Against it: the change is incremental replacement inside long-standing niches (power quality meters, process
  analyzers, turbine sensors, specialty metals), not a platform war; R&D expense is 3.2% of sales ($236.1M on $7,401.1M in
  2025). The forecast is about the customers' continued need to measure and qualify, which is old and slow-moving.
  Contrary evidence carried to Q2: some EIG niches sit on faster technology (semiconductor metrology, FARO's 3D scanning
  bought in 2025).
- **The acquisition programme.** The ten-year economics of what AMETEK will buy cannot be foreseen from here; the parts
  convention reads "a company whose stated policy is to keep buying and selling parts [...] on the parts it owns, with
  the policy weighed at Q6 as a use of the money" (Q2, A business of parts). Q1 is therefore asked of the parts owned.
- **Test 9, doubt** **[M2002-092]**: my doubt is not whether EIG's economics can be foreseen (the record says they can, at
  the group level) but whether forty-odd separate niches can each be judged; I judge the group by its record, as Q1's
  holding-company paragraph allows when the deciding part is understood as a whole. Stated so a reader can disagree.

**VERDICT: IN.** EIG's ten-year earning power and position can be foreseen in the sense the rows ask, "where the business
will be in 10 years" **[M2000-037]**: a high-margin, low-capital collection of measurement niches whose volume follows
its customers' capital cycles and whose margin has held through two recessions (10-K series FY2005 to FY2025, segment
table). The acquisition programme goes to Q6; the technology exposure goes to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question:** "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

**The parts table** (business of parts, CONVENTION of 2026-10-06; filer's segment figures, 10-Ks FY2021 to FY2025):

| Part | Five-year segment OI 2021-2025 | Share | Margin range 2005-2025 | Castle | Decides |
|---|---|---|---|---|---|
| EIG | $6,234.4M | 71.6% | 20.0% (2006) to 30.7% (2024) | standing, judged below | **yes** (more than half) |
| EMG | $2,473.0M | 28.4% | 15.5% (2008) to 26.2% (2022) | standing on its margin record; not decisive | no |

**The castle tests, applied to EIG with the filing fact for each:**
1. *The key factors and how permanent* **[M1995-038]**: the filer's own account is "strong market share in a number of
   targeted niche markets through its ability to produce and deliver high-quality, differentiated products at competitive
   prices" and, in aerospace, a "70-year-plus reputation as an established aerospace supplier" with products "designed to
   customer specifications and manufactured to stringent operational and reliability requirements" (10-K Item 1). **No
   share figure is given for any niche** (contrary evidence 5); the castle has to be read from the results, which the rows
   allow: the moat is judged, "You have to understand the businesses." **[M1999-108]**.
2. *Would it stand without the lord*: the castle is a collection of small specialist businesses run by "the business level"
   (marketing "organized and carried out at the business level", Item 1); no single superstar. Passes.
3. *The attacker with money*: the rows name exactly this shape of moat: "very small markets that aren’t really too
   attractive to anybody with any sense to enter" **[M2011-017]** and businesses "of a size and have specialized skills
   that other organizations just can’t get into it" **[M1997-071]**. EIG's 2025 sales of $4.9 billion are spread over many
   niches; the filer says it ranks "as a leader in certain analytical measurement and control instruments, and power and
   industrial markets" (Item 1). Evidence that money has not broken in: the margin rose over twenty years while larger
   instrument companies (Danaher, Fortive, Keysight, Teledyne) competed in adjacent fields (competitor row below).
4. *Pricing power through the last inflation*: the FY2022 10-K (`0001037868-23-000012`): "Beginning in 2021, we
   experienced heightened levels of inflation in material and transportation costs" and "We have taken steps to mitigate
   the impacts of material and transportation cost inflation by implementing pricing actions". The result: EIG's margin
   25.5% (2021), 25.8% (2022), 28.4% (2023), 30.7% (2024); consolidated cost of sales 64.3% of sales in 2024 and 64.0% in
   2025 (FY2025 10-K). The rows' test is whether the business can "pass through increases in raw material costs"
   **[M2005-017]**; it did, and widened the margin afterward. The filer does not quantify price separately from volume
   (a gap, recorded).
5. *Unit volume*: the filer reports organic growth, not units. Compound organic growth 2005 to 2025 was **+2.35% a year**
   and 2015 to 2025 **+2.24% a year** (segment table; the filer's own organic percentages, 2009 to 2013 and 2015 to 2016
   weighted from its group figures), against total segment sales growth of 8.55% and 6.42% a year. Organic growth that
   includes price and runs near general inflation says the volume of the existing businesses has been roughly flat for
   a decade. **This is the strongest evidence against the castle widening**: the rows want "a lot more unit cases sold"
   **[M1999-054]**; AMETEK's growth has been bought.
6. *The low-cost position*: not claimed by the filer beyond "best-cost manufacturing" facilities in China, Czechia,
   Malaysia, Mexico and Serbia (Item 1). Not the castle; neutral.
7. *The brand*: the business units' names (Spectro, Cameca, Zygo, Brookfield, Creaform, Taylor Hobson) are known to
   their specialist buyers; not a consumer brand. Neutral.
8. *The low bid* **[M2017-009]**: the rows' own industrial case is Precision Castparts, "where people don’t simply just
   take the low bid in order to get this gadget" **[M2016-006]**. EIG's aerospace sensors and the process instruments that
   are qualified into customers' plants and regulatory procedures are of that kind; the filer's own word is that
   competition is "based on technology, performance, quality, service and price" (Item 1), price last. Customer
   concentration is low: "Approximately 4% of EIG’s 2025 net sales were made to its five largest customers. No single
   customer comprises more than 2% of net sales." (Item 1). No customer can set the price.
9. *Ask the competitors*: the filer names no competitor (Item 1, Competition); no competitor's filing names AMETEK as the
   rival it fears, in the filings read. Not available; recorded.
10. *Widening or narrowing* **[M1999-108]**: the margin widened (EIG 21.9% at the 2008 peak, 26.0% at the 2019 peak, 29.4%
   in 2025); volume did not (test 5). The filer attributes part of the 2024 to 2025 margin to "Operational Excellence"
   and part of 2025 EIG margin to adjustments ("Excluding the dilutive impact of recent acquisitions and acquisition-related
   integration costs, EIG's operating margins increased 20 basis points"; on GAAP the EIG margin fell from 30.7% to 29.4%).
11. *What could destroy, modify or reduce it* **[M2000-014]**: a faster technology turn in the niches that sit on
   semiconductors and 3D metrology; a long industrial and aerospace downturn (volume, not margin, on the record); China
   and tariff exposure (48.2% of sales abroad; "Increasing trade tensions between the United States and certain
   countries, including China", Item 1A). None of these, on the record of 2009 and 2020, has broken the margin.

**The cycle record** (segment table, from the 10-Ks): 2008 to 2009, EIG sales -18.3%, operating income -24.1%, margin 21.9%
to 20.3%; 2019 to 2020, EIG sales -10.0%, operating income -10.9%, margin 26.0% to 25.8%; 2015 to 2016 (oil and gas), EIG
operating income -9.6%, margin 26.5% to 24.5%. EMG: 2009 margin 15.5% to 17.5% (the 2008 figure carries $19.4M of
restructuring), 2020 21.1% to 21.0%.

**The competitor row** (GAAP operating margin, from each filer's own 10-K XBRL; the full table with return on total capital
and accessions is `Test Runs/_research 2026-10-10 AME/comp_table.txt`):

| Filer (CIK) | 2008 | 2009 | 2015 | 2019 | 2020 | 2023 | 2025 | notes |
|---|---|---|---|---|---|---|---|---|
| AME (1037868) | 17.1% | 17.4% | 22.8% | 22.8% | 22.6% | 25.9% | 25.8% | |
| ROP (882835) | 21.1% | 19.3% | 28.7% | 28.1% | 26.9% | 28.2% | 28.3% | became mainly software after 2016 |
| MTD (1037646) | 14.8% | 14.5% | 20.5% | 23.9% | 25.5% | 27.7% | 27.8% | tags no operating income: pre-tax earnings plus interest expense |
| DHR (313616) | 14.7% | 13.7% | 15.0% | 18.3% | 19.0% | 21.8% | 19.1% | Fortive (2016) and Veralto (2023) spun off; now life sciences and diagnostics |
| TDY (1094285) | 11.5% | 10.4% | 12.3% | 15.5% | 15.6% | 18.4% | 18.8% | FLIR bought 2021 |
| FTV (1659166) | n/a | n/a | 20.5% | 9.7% | 11.6% | 14.7% | 17.3% | first own filing 2016 (FY2014 and FY2015 carve-out figures); restated for the Vontier (2020) and 2025 separations |
| KEYS (1601046) | n/a | n/a | 15.1% | 16.5% | 18.1% | 24.9% | 16.3% | first own filing FY2014 (October year); FY2018 tagged as an operating loss, as filed |

Pre-tax return on total capital (operating income over equity plus debt less cash, goodwill included) over the span: AME
15.5% (2009), 18.9% (2015), 14.4% (2020), 15.3% (2025); ROP 12.0%, 13.2%, 5.6%, 7.9%; DHR 11.2%, 6.0%, 7.7%, 7.1%; TDY 19.2%,
14.0%, 14.8%, 9.4%; MTD 30.1%, 45.8%, 51.7%, 54.2%; FTV 24.5% (2015), 5.4%, 8.6%; KEYS 22.5% (2015), 23.0%, 13.4%.

**The field's returns over the last full cycle** (section C, judged in words): on the capital the businesses need,
AMETEK's returns are far above ordinary: 2025 operating income before acquired-intangible amortization was $2,187.6M
($1,910.3M plus $277.3M) against tangible capital of about $1.2 billion (equity $10,628.8M plus net debt $1,825.3M less
goodwill $7,170.8M and other intangibles $4,128.4M; 10-K FY2025). On the total capital including the goodwill it paid,
the pre-tax return is 14% to 20% across 2008 to 2025, at the top of the field except Mettler-Toledo, the one rival that
has bought little; Roper and Danaher, the other serial buyers, earn 6% to 13% on the same measure. This is not a castle
that protects only ordinary returns. The goodwill question (what the purchases earn) is Q3's and Q6's.

**What I could not get:** a market-share figure for any AMETEK niche (none in the filings read); a price-versus-volume split
of organic growth; any competitor's statement about AMETEK. Fortive and Keysight have no filings of their own before
2016 and 2014, so their columns do not cover 2008 to 2009; Danaher's consolidated figures stopped being an instruments
comparator after its 2016 and 2023 separations.

**VERDICT: IN.** The deciding part, EIG, shows the castle the rows describe for small specialist niches **[M2011-017]**,
**[M1997-071]**: margins that held through 2009 and 2020 and widened through the 2021 to 2023 inflation by "implementing
pricing actions" (FY2022 10-K), with no customer above 2% of sales, and returns on the capital the business needs that
are far above ordinary. It is judged, not measured **[M1999-108]**. Carried forward as the weight against: organic growth
of about 2.3% a year for twenty years means the castle has kept its margin but not grown its volume, so the growth the
company shows is bought (Q3, Q6, Q7). EMG does not decide; its castle stands on its own margin record and is not open on
the evidence.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**The capital the business needs** (goodwill set aside, as the rows say for judging the business: "Goodwill should not be
used in evaluating the fundamental attractiveness of a business. There you should look at return on tangible assets"
**[M2011-060]**). 10-K FY2025 (`0001037868-26-000016`) balance sheet: receivables $1,119.3M, inventories $1,106.4M, other
current assets $336.2M, PP&E $855.2M, right-of-use assets $273.1M, less accounts payable $618.0M, customer advances $396.2M
and accrued liabilities $537.0M: operating tangible capital about **$2,139M**. Against it, 2025 operating income before
acquired-intangible amortization was $2,187.6M (operating income $1,910.3M plus amortization $277.3M): a pre-tax return on
the operating tangible capital of about **100%**. The filer's own pay metric agrees in kind: its "Return on Tangible
Capital" averaged 100% in 2023 to 2025 (proxy `0001037868-26-000062`, PRSU outcome). This is the first grade of the rows:
"more and more money every year without putting up anything to get it, or very little" **[M1998-081]**.

**To stand still**: capital spending $130.2M (1.8% of sales) against depreciation of $145.5M in 2025; $127.1M against
$135.3M in 2024; $136.2M against $122.5M in 2023 (10-K cash-flow statement and EBITDA reconciliation). Capital spending runs
at about the depreciation charge, so the rows' proxy holds: "every year we spend amounts equal to our depreciation charge
simply to stay in the same economic place" **[L2000-035]**. The filer gives no maintenance split ("Capital expenditures in
2026 are expected to be approximately 2% of net sales, with a continued emphasis on spending to improve productivity",
Item 7); I take all capital spending as maintenance, the conservative guess **[M2000-144]**. Working capital: the
cash-flow lines show net working capital investment of $48.6M a year on average over 2021 to 2025 (a $266.5M draw in 2022
that the filer ties to "higher investments in inventory to support sales and backlog growth, and to mitigate inventory
supply chain constraints", FY2022 10-K, partly reversed in 2023 and 2024). Receivables held at 15.1% to 15.4% of sales
from 2016 to 2025.

**To grow**: organic growth has been about 2.3% a year for twenty years (Q2, test 5), so almost all of the growth the
company shows comes from acquisitions. Cash paid for businesses, net of businesses sold, 2016 to 2025: **$8,672M**
($8,933M paid less $261M of divestiture proceeds; 10-K cash-flow statements). Operating income before acquired-intangible
amortization rose from $988.5M (2015: $907.7M plus $80.8M) to $2,187.6M (2025), an increase of $1,199.1M. Charged entirely
to the acquisitions, that is a pre-tax return of **13.8%** on the money paid; if the 2015 base had grown only at the
filer's organic rate (2.24% a year, to about $1,232M), the acquisitions' share of the increase is about $955M, a pre-tax
return of about **11%**, about 9% after the company's 17.7% to 19.1% tax rates. The rows' test is "what we earn on that
incremental $130 million over time" **[M2001-019]**: on the incremental billions, AMETEK earns a decent return, not a high
one; the high return is on the small tangible base, and "Most of the great businesses generate lots of money. They do not
generate lots of opportunities to earn high returns on incremental capital" **[M2003-120]** describes the company exactly.
The growth arithmetic: more earnings have come from more capital put in, as in the rows' utility case, "we’re not earning a
higher rate of return on capital than we were when we started. We just put way more capital into the business"
**[M2023-081]**: AMETEK's pre-tax return on total capital including goodwill fell from 18.7% (2008) and 19.6% (2014) to
15.3% (2025) (comp table).

**WEIGHS FOR**, with the growth half carried: the business needs very little capital to stand still and earns returns on
the capital it needs that put it in the first grade **[M1998-081]**, **[M2011-060]**; the growth is bought with acquisitions
earning roughly 11% to 14% pre-tax on the price paid, "decent returns on the incremental sums they invest" **[L2009-012]** at
best, which is the second grade and is weighed again at Q6 (capital allocation, where "you have to include goodwill,
because we paid for it" **[M2011-060]**) and priced at Q7.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL; read against the filed
balance sheets of FY2016 `0001193125-17-053600`, FY2020 `0001037868-21-000007` and FY2025 `0001037868-26-000016`;
USD millions):

| year-end | equity | goodwill | intangibles | GW+int / equity | cash | receivables / sales | inventory / sales | debt (current + LT) | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,257 | 2,819 | 1,734 | 140% | 717 | 15.4% | 12.8% | 2,342 | 4,404 |
| 2018 | 4,242 | 3,612 | 2,404 | 142% | 354 | 15.1% | 12.9% | 2,633 | 5,654 |
| 2020 | 5,949 | 4,225 | 2,624 | 115% | 1,213 | 13.1% | 12.3% | 2,414 | 7,095 |
| 2022 | 7,477 | 5,373 | 3,342 | 117% | 345 | 14.9% | 17.0% | 2,385 | 8,857 |
| 2023 | 8,730 | 6,448 | 4,165 | 122% | 410 | 15.4% | 17.2% | 3,313 | 9,940 |
| 2025 | 10,629 | 7,171 | 4,128 | 106% | 458 | 15.1% | 14.9% | 2,283 | 12,252 |

What the figures say: equity tripled, and goodwill and intangibles rose with it to **$11,299M, 70% of total assets**
(Item 1A); **tangible equity has been negative in every year shown** (2025: equity $10,629M less $11,299M). Retained
earnings rose every year, $4.4 billion to $12.3 billion. Receivables held steady against sales; inventories rose from
12.8% to 17.2% of sales in the supply-chain years and came back to 14.9%. Debt stayed between $2.1 and $3.3 billion for a
decade while about $8.9 billion was spent on businesses: the deals were paid mostly from cash generated, with short-term
borrowing between (commercial paper $740.0M at 2025-12-31, Item 7). What they do not say: whether the $11.3 billion of
purchased goodwill and intangibles is worth what was paid; the impairment record is a $13.9M trade-name charge in 2016 and
"immaterial" trade-name charges in 2022 and 2023, no goodwill impairment in the 10-Ks read (FY2006 to FY2025). What they
cannot say: the earnings of Indicor Instrumentation, which joins after the last balance sheet with $5.0 billion of new debt.

**The real costs.** Depreciation: real, and covered by capital spending at about its level (Q3) **[L2015-004]**. Stock
pay: $47.8M in 2025, expensed in GAAP and deducted in owner cash below. Restructuring and the recurring "one-time": the
filer took restructuring or realignment charges in 2008 ($40.0M), 2015 ($36.6M), 2016 and 2020 ($43.7M), and acquisition
integration costs in 2014 (Zygo, $18.9M), 2024 (Paragon, $29.2M) and 2025 (FARO, $37.3M); all are inside GAAP operating
income and operating cash, and all are counted here, since the rows do not ask owners to forget them **[L2016-007]**.
Amortization of acquired intangibles ($277.3M in 2025) is a purchase-accounting charge on customer relationships,
technology and trade names; the rows say such charges on customer relationships "are clearly not real expenses"
**[L2012-003]**, while the money that bought them is real: owner cash below is taken before that amortization, and the
acquisition spending is deducted at Q7 by specific (c). Pensions: contributions $8.5M in 2025, small. Taxes: effective
rates 17.2% to 19.1% in 2021 to 2025; cash taxes paid $404.2M in 2025 against a $318.2M provision; tax-effected
carryforwards $159.0M of losses (mostly indefinite) and $30.5M of credits (expiring 2026 to 2045), immaterial against owner
cash, so the statutory-rate convention of Q7 (section E) is not applied and the company's own tax is used.

**Owner cash after every real cost** (operating cash less stock pay less all capital spending; 10-K cash-flow statements
FY2021 to FY2025; `Test Runs/_research 2026-10-10 AME/valuation_out.txt`): 2021 $1,003.7M; 2022 $963.0M; 2023 $1,552.8M;
2024 $1,653.9M; 2025 $1,623.7M; five-year average **$1,359.4M** (equity basis, after interest). Before net interest after the
company's tax (all-equity basis): average **$1,427.2M**. Net cash paid for businesses averaged $1,132.4M a year over the same
five years. No net-income proxy is used anywhere (operator rule 5).

**EBITDA in the filer's own mouth, the featured adjusted figure, and guidance** (section A of the gaps case: weighed here,
judged at Q5). The 10-K's list of "Highlights in 2025" includes "EBITDA (earnings before interest, income taxes,
depreciation, and amortization) was a record $2,296.9 million in 2025", and every 10-Q carries an EBITDA reconciliation;
the filer says it presents EBITDA "because the Company is aware that it is used by rating agencies, securities analysts,
investors and other parties" and that it "should not be considered, however, as an alternative to operating income". The
rows on EBITDA talk are severe: "the number of times we’re going to buy into a company [...] where people are talking about
EBITDA, is going to be about zero" **[M2002-026]**. The press releases lead with "Adjusted earnings" per share that "adds
back non-cash, after-tax, acquisition-related intangible amortization" and excludes "one-time acquisition-related costs"
(8-Ks `0001037868-26-000006`, `0001037868-26-000173`); full-year 2025 adjusted EPS $7.43 against GAAP $6.40. The
amortization add-back is one the rows themselves make **[M1997-015]**, **[L2012-003]**; the exclusion of integration costs
that recur with every deal is the "Don’t count this" the rows call "misleading" **[L2016-007]**. Guidance: given yearly and
quarterly, and raised: 2025 adjusted EPS guided $7.02 to $7.18 (February 2025, `0001037868-25-000004`), raised to $7.32 to
$7.37 (October 2025, `0001037868-25-000075`), delivered $7.43 (February 2026); 2026 guided $7.87 to $8.07, raised to $8.20
to $8.30 (August 2026, "Raises Full Year Guidance"). The rows: "we become downright incredulous if they consistently reach
their declared targets" **[L2002-041]** and "the scourge of earnings "guidance"" **[L2019-006]**.

**The tells that live in the accounts** (the Q4 STOP): no prepaid or deferred accounts building out of line (other current
assets 3.5% to 4.5% of sales), inventories back toward their pre-2021 ratio, no reserve released into earnings in the
filings read, no restatement of results (the 2017 and 2016 income statements were reclassified for the pension-cost
standard only), no material weakness, an unqualified opinion from Ernst & Young, the auditor "since 1930". The accounts
are clear and the 10-K explains in plain words what moved, including what went against the company ("a 1% organic sales
decrease" in EIG): "If you find a management that doesn’t care about the accounting but does explain to you in clear terms
what’s going on, I think you should regard that as a plus" **[M1994-018]**.

**VERDICT on the accounts: IN (no confusion, no suspicion from the statements themselves) **[M1995-063]**,
**[M1995-064]**; WEIGHS AGAINST on the habits**: EBITDA in the highlights, adjusted earnings featured, and guidance
beaten and raised, carried to Q5 as evidence on the people **[L2016-006]**, **[L2002-041]**. The recast owner cash above
feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The people.** David A. Zapico, Chairman and Chief Executive since 2016 (CEO) and with the company more than 35 years
(proxy `0001037868-26-000062`: "over 35 years of experience in our industry and with our company"); the 10-K says senior
management has "an average of approximately 24 years of AMETEK service" (Item 1). Group presidents John W. Hardin (EIG) and
David F. Hermance; CFO Dalip M. Puri since April 2024. Marketable stock, so the reading tests carry the weight
**[M1994-009]**.

**Yardstick one, the record against the hand dealt** **[M1994-008]**: EIG's margin went from 24.5% (2016) to 29.4% (2025),
EMG's from 18.8% to 23.3%, through 2020 and the 2021 to 2023 inflation, while Danaher, Teledyne and Fortive ran lower
margins over the same years and Keysight's swung (Q2 competitor row). Fifteen acquisitions from 2021 to 2025 "with
annualized sales totaling approximately $1.8 billion" (Item 1) were absorbed without a goodwill impairment. The hand dealt
included weak organic growth (Q2), which management has not changed. Ability **weighs FOR**.

**Yardstick two, how they treat the owners**: the proxy shows the CEO holding stock worth **46.5 times his salary** (all
named officers in compliance with ownership guidelines; directors and officers prohibited from hedging and pledging, "No
Directors or executive officers have pledged any shares of our stock"); beneficial ownership 579,197 shares including
262,146 option shares. CEO total pay $16.46M in 2025, $14.63M in 2024, $14.54M in 2023 (Summary Compensation Table). The
plan's design is Q6's subject. They have "gotten rich with their shareholders" in the sense of **[M2003-055]** to the extent
the stock they hold was bought or kept; much of it came by grants.

**The habits carried from Q4, read with the integrity record** (section A of the gaps case). Present: earnings guidance,
yearly and quarterly, beaten and raised (2025 guided $7.02 to $7.18, delivered $7.43; 2026 raised twice to $8.20 to
$8.30); adjusted earnings featured in every release, excluding acquisition costs that recur with every deal; EBITDA in the
10-K highlights; release language of "record", "superb", "exceptional", "the AMETEK Growth Model" and "Four Growth
Strategies", the "standardized bunch of popular jargon" the rows call "a big turnoff" **[M1998-038]**. The rows are severe
on the first: "we become downright incredulous if they consistently reach their declared targets. Managers that always
promise to "make the numbers" will at some point be tempted to make up the numbers." **[L2002-041]**; beating expectations
"is heralded as a managerial triumph. That activity is disgusting." **[L2022-006]**. Absent, in the filings read: any
restatement of results, any material weakness, any SEC or Justice Department investigation disclosed, any reserve released
into earnings, any rise of prepaid or deferred accounts, any serial issuance of shares (no stock-paid acquisition found in
the 10-Ks FY2006 to FY2025; share count 241.6M diluted in 2015, 231.3M in 2025). The accounts are plain and tell the bad
news in the same paragraph as the good ("a 1% organic sales decrease" for EIG; GAAP EIG margin down from 30.7% to 29.4%,
though followed by an "Excluding the dilutive impact" sentence). The asbestos claims are disclosed as indemnified by a
seller with "no judgments" (10-K Note 13).

**The integrity judgment.** "If you’ve got doubts, forget it." **[M2013-088]**. The doubt the rows ask about is whether
these people can be counted on to report honestly and treat owners fairly; on the filings the answer is that the
statements are clean and the habits are the habits of a company that manages its quarterly image, not evidence that it
manages its numbers: the beats come with organic growth and margins visible in the segment figures, and guidance that is
set low and beaten is the opposite of the "lofty predictions" that "corrode CEO behavior" **[L2000-039]**. I record no
doubt on honesty, and record the habits as a weight against candour. A reader who takes **[L2022-006]** as a test of
character rather than of practice would close the file here; the box would be OUT either way (Q7).

**VERDICT on integrity: IN** (no doubt established on the filings; the habits weigh against, recorded) **[M2013-088]**,
**[M1994-018]**. **Ability WEIGHS FOR** **[M1994-008]**, **[M2005-039]**: a long record, "they batted .350, or whatever it may
be", in margin and integration, with organic growth the weak part of the hand.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A, the money
**The retention test** **[R1995-009]**, **[M1998-110]**, read in market value and against the business: the aggregate market
value held by non-affiliates was "approximately $13.3 billion as of June 30, 2015" (10-K FY2015 cover, `0001193125-16-478197`)
and "approximately $ 41.8 billion as of June 30, 2025" (10-K FY2025 cover). Over 2016 to 2025 the company earned $10,024M of
net income, paid $1,749M of dividends and $1,729M for its own shares, and retained about **$6,547M**, with net debt roughly
unchanged ($1,557M at 2015-12-31, $1,825M at 2025-12-31). Market value rose about $28.5 billion against about $6.5 billion
retained. Against the business: owner cash rose from about $580M (2015: operating cash $672.5M, per the FY2016 10-K, less
stock pay $23.8M and capital spending $69.1M) to $1,623.7M (2025), about $1.04 billion more a year on about $6.5 billion
retained plus about $0.3 billion of added net debt, an after-tax return on the retained money of about 15% before allowing
for organic growth of the old base, about 10% after it. The test is met in both legs over the decade; the market leg is
helped by a higher multiple (market value about 23 times 2015 owner cash, about 26 times 2025's).

**Acquisitions, value given against value got** **[M1995-001]**: all cash, no stock deals, so the one STOP of Part A (an
all-stock deal in undervalued stock **[L2009-019]**) does not arise. The bought growth earns about 11% to 14% pre-tax on the
price (Q3). The largest deals were paid with borrowed money first: Paragon Medical (December 2023, the largest of four 2023 purchases that cost $2,237.9M in
total, paid largely with short-term borrowing; interest expense $113.0M in 2024 "related to the December 2023 Paragon acquisition") and now
Indicor Instrumentation, "an all-cash transaction valued at $5.0 billion" for a business with "annual sales of
approximately $1.1 billion" and no filed earnings, financed by a $4.0 billion term loan and the revolver. The rows'
warning fits it exactly: "even a high-priced deal will usually boost per-share earnings if it is debt-financed"
**[L2017-004]**; the release calls it "modestly accretive to AMETEK’s 2026 adjusted earnings" (8-K `0001037868-26-000191`).
No post-mortem of past deals against their projections is published in the filings read **[L2014-013]**.

**Buybacks**: no stated price. "The objective and rationale of the share repurchases is to enhance shareholder value
through the opportunistic repurchases" (10-K Item 5); the authorization is a dollar sum ($1.25 billion, February 2025).
Prices paid: 2,306,500 shares for $443.0M in 2025 (about $192 a share; $195.19 in the fourth quarter) and 1,258,200 shares
for $223.1M in 2024 (about $177). Against the Q7 range (below), whose top on the organic pair before the Indicor debt is
$141.75 a share, these prices sit above the range, so the buyback with no stated price weighs against by the convention
**[L2016-002]**, **[M1996-013]**.

**Dividends**: a "consistently increasing cash dividend" (Item 1), raised 11% in 2025 and 10% in 2026; $285.3M paid in 2025,
about 19% of net income. Neutral.

**Part A: UNDECIDED.** The retention test is met over ten years in both legs **[R1995-009]**, and the deals are cash, but
the growth is bought at decent rather than high returns, the buybacks were made above value **[L2011-003]**, and the
largest purchase in the company's history, debt-financed at about 4.5 times sales with no filed earnings, closed six weeks
before this run.

### Part B, the pay, the board and the owners
- **What the pay is tied to** (proxy, CD&A): the annual incentive rests mainly on "Adjusted Earnings Per Share" ("net income,
  adjusted for tax-effected acquisition-related intangible amortization"), organic revenue growth, operating income and
  operating working capital, with 10% to 20% discretionary; the performance share units rest half on "Return on Tangible
  Capital" (target 107%, actual 100% for 2023 to 2025) and half on total shareholder return relative to the S&P 500
  Industrials. Organic growth and working capital are under the managers' control, as the rows ask **[M2003-019]**. But
  neither adjusted EPS nor return on tangible capital charges the managers for the price of acquisitions: goodwill and
  acquired intangibles are outside "tangible capital", and a debt-financed deal raises adjusted EPS whatever it cost. The
  rows: "a batting average that does not include a cost of capital is a phony batting average" **[M1995-010]**; capital
  should be charged at "a high rate for incremental capital they employ" **[L1994-019]**. Weighs against.
- **Options**: granted at market with no step-up for retained earnings; the rows' objection, "lush gains to a manager who has
  done no more than tread water" **[L1994-021]**. Weighs against, mildly (option awards $2.17M of the CEO's $16.46M).
- **Who sets it**: an independent consultant (Pay Governance LLC) benchmarks to "the median pay levels of both our
  compensation peer group and the general industry" (proxy). That is the comparative ratchet the rows name
  **[L2005-015]**, **[M2012-095]**.
  Weighs against.
- **The board**: the Chairman is the CEO, with a Lead Independent Director (Anthony J. Conti, since 2017, asked to stand
  again although "he has attained the age of 75"); directors are elected in classes for three-year terms (Class II nominees
  "for terms expiring in 2029"). The rows: "how hard it is to replace a mediocre CEO if that person is also Chairman"
  **[L2014-026]**. The CEO is not mediocre on the record; the structure still weighs against. Directors and officers as a
  group own under 1%; directors are paid $110,000 cash and $185,000 of restricted stock (2025).
- **Owners as partners**: one class of stock, one vote, no poison pill, proxy access (proxy summary).

**Part B: WEIGHS AGAINST**, chiefly because the pay plan does not charge for the capital spent on acquisitions, the
company's main use of money **[M1995-010]**, **[M2016-083]**; the large ownership by the CEO weighs for.

**Q6 overall: WEIGHS AGAINST** (Part A undecided, Part B against). The buyback test needs the Q7 range; it is recorded here
from Q7.

## Q7 — WHAT IS IT WORTH? STOP.
**The question:** how many birds, how sure, how soon, at "the yield on long-term U.S. bonds" **[L2000-021]**, held as "a
range of possibilities" **[L2000-024]**. All arithmetic is in `Test Runs/_research 2026-10-10 AME/valuation.py` and its
output `valuation_out.txt` (computed during Q3 and Q4 under the heading COMPUTATION, NOT A CLEARANCE, and first reported
here, after Q1 to Q6 closed).

**The construction (Q7's CONVENTION and its specifics, applied in order).**
- *Cash input*: owner cash after every real cost (Q4): operating cash less stock pay less all capital spending, FY2021 to
  FY2025. All-equity basis (central): before net interest after the company's own tax, five-year average **$1,427.2M**;
  equity-only basis (beside): after interest, **$1,359.4M**. Company's own tax, no conversion (Whose tax); no carryforward
  runs out inside ten years in an amount that matters (Q4), so no shelter is priced separately.
- *(a) Cycles*: neither end year is a peak or trough on the filer's own description; 2021 was a recovery year (organic
  +15%) and 2025 a record year with orders and backlog still rising into 2026. The literal window is the base.
- *(b) Decline*: no negative growth; not applied.
- *(c) Acquisitions*: net cash paid for businesses averaged **$1,132.4M** a year in the window. **Default pair (central)**:
  acquisitions deducted (all-equity base **$294.9M** a year) and total growth credited, measured on aggregate owner cash
  between the end years 2021 and 2025: **12.10% a year** (all-equity), 12.78% (equity-only). **Organic pair (beside)**:
  acquisitions left out and only organic growth credited, the filer's organic sales growth 2022 to 2025 compounded:
  **3.64% a year**. Deals after the window: Indicor Instrumentation closed 2026-08-26 for $5.0 billion cash, financed by new
  borrowing; the filer has filed sales for it ("approximately $1.1 billion") and no earnings, so it is **credited at
  nothing** and its $5.0 billion is added to net debt. LKC Technologies (January 2026) and First Aviation Services (May
  2026) were paid before 2026-06-30 ($424.5M in the half, 10-Q cash-flow statement) and sit in that date's net debt; no
  earnings filed; credited at nothing.
- *(d) Working capital*: counted in operating cash; window average draw $48.6M a year against $45.0M in FY2019, before the
  supply-chain event the filer names for 2022; no adjustment needed.
- *(e) Growth spending*: the filing gives no maintenance split and capital spending runs at about depreciation (Q3); all
  capital spending is treated as maintenance, so the central case is the all-spending case and no separate
  maintenance-only case exists.
- *(f) The cap*: inside ten years the shown rate is the cap (12.10% default, 3.64% organic); after year ten, zero nominal
  growth **[M1997-095]**. No result traced to an absurdity **[M1999-067]**.
- *Rate*: 5.60%, the 30-year Treasury par yield, 2026-10-09. *Net debt*: $1,540.8M at 2026-06-30 plus Indicor's $5,000.0M
  = **$6,540.8M**; operating leases ($288.2M) left out. *Shares*: 229.261244M.

**Value range** (whole business at 5.60%, less net debt, per share):

| Case | Whole business | Per share | Width |
|---|---|---|---|
| **Default pair, all-equity (central)**: no-growth to 12.10% | $5,266M to $13,729M | **-$5.56 to $31.35** | 2.61 to one on the whole business |
| Default pair, equity-only (beside; after the window's interest, Indicor's price deducted) | | -$4.12 to $26.81 | |
| Organic pair, all-equity (beside): no-growth to 3.64% | $25,487M to $34,038M | **$82.64 to $119.94** | 1.34 to one |
| Organic pair, equity-only (beside) | | $84.08 to $119.60 | |
| *For the reader only, Indicor left out (not the convention):* default / organic, all-equity | | $16.25 to $53.16 / $104.45 to $141.75 | |

**Value range: -$5.56 to $31.35 a share** (central, default pair, all-equity basis; the organic pair beside, $82.64 to
$119.94) **against $248.58.**

What the default pair says: over 2021 to 2025 AMETEK spent on businesses about four-fifths of the owner cash it made, so
the cash left for owners after the growth programme averaged under $300M a year, and the growth the programme bought,
credited in full for ten years, does not make that stream worth the price; "growth can destroy value if it requires cash
inputs in the early years [...] that exceed the discounted value of the cash that those assets will generate in later
years" **[L2000-023]**. What the organic pair says: even if the company stopped buying and kept its organic growth, the
stream is worth about $83 to $120 a share after the new debt.

**The floor** (CONVENTION, about ten percent, applied to owner cash after the company's tax): at $248.58 the enterprise
costs $63,531M (market value $56,990M plus net debt $6,540.8M). The no-growth owner cash yield on that is **2.25%**; the
expected return of the organic pair's top case at the price is **3.09%** a year and of the default pair's top case **1.38%**;
all below the 5.60% bond, let alone the floor. To earn the sovereign rate on the organic base the business would have to
grow owner cash about 11.5% a year for ten years with no acquisition spending; to earn the floor, about 21.3% a year.
"there’s just a point at which we drop out of the game" **[M2003-149]**; "we are going to want to get a significantly higher
return [...] than we are from a government bond" **[M2007-095]**.

**Fair price** (a reporting figure, never a verdict; Part VII): the price at which the midpoint of the range earns the floor,
computed as the year-by-year average of the two end streams discounted at 10%, less net debt, after the company's own
tax. **Central, all-equity basis, default pair: below zero (-$7.18 a share)**: no positive price earns the floor on the
central case once the $6.54 billion of net debt is deducted. **Equity-only beside: -$4.81.** Organic pair beside:
all-equity **$42.53**, equity-only **$45.87**. No cheap price is reported.

**Q6's buyback test, recorded back**: the prices paid in 2024 and 2025 (about $177 and $192) sit above the top of every
range above, including the organic pair before the Indicor debt ($141.75): the buybacks with no stated price weigh against
(Q6).

**VERDICT: OUT.** The price sits above the top of the range in every construction, so the expected return at the price is
below the floor (Q7's CONVENTION: "A price above the top of the range closes OUT however wide the range"); the case is not
close and needs no pencil to reject: "It should scream at you." **[M2009-005]**, and here it does, the other way. A wonderful
business at too high a price is still not a purchase: the castle (Q2) and the capital-light core (Q3) are real, and the
price is about twice the top of even the organic range, the case that credits the business with no acquisition spending.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7 (price above value).** Value range -$5.56 to $31.35 a share (central: default pair, all-equity, Indicor's $5.0
billion added to net debt and credited at nothing), organic pair beside $82.64 to $119.94, against $248.58 (2026-10-09,
aggregator). Q1 IN, Q2 IN (EIG decides), Q3 weighs FOR, Q4 accounts IN with the habits against, Q5 integrity IN and
ability FOR, Q6 weighs AGAINST.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2), each with its source **[M1997-127]**.)*

**Bearing on Q8 (the alternatives).** The 30-year Treasury par yield was 5.60% on 2026-10-09; AMETEK's no-growth owner cash
yield on the enterprise value at $248.58 is 2.25%, and its organic top case returns 3.09% a year (valuation_out.txt).

**Bearing on Q9 (debt and exposures).**
- Debt after Indicor: total debt $2,036.2M at 2026-06-30 (10-Q) plus the Indicor financing: a senior unsecured term loan of
  up to $4.0 billion in tranches of $1.625 billion (three years), $1.625 billion (four years) and $750 million (five years),
  and up to $1.0 billion of the revolver (8-K `0001037868-26-000166`); revolver raised to $3.5 billion, maturing
  2031-06-09; commercial paper programme raised to $3.5 billion, backstopped by the revolver, with revolver and paper
  together not to exceed $3.5 billion (8-K `0001037868-26-000183`). Commercial paper has "maturities of up to 364 days"
  (10-K Item 7). The interest rate on the term loans is not stated in the documents read.
- Scale: net debt about $6.54 billion against all-equity owner cash of $1,427.2M a year (2021 to 2025 average), about 4.6
  years of owner cash; 2025 operating income $1,910.3M against interest expense $81.3M before the new debt.
- The acquisition criteria's "little or no debt" **[R1997-001]** is stated for whole businesses; the debt here rose from
  about 0.2 to about 0.6 of 2025 equity.
- Covenants: "Our Debt Facilities contain covenants requiring us to achieve certain financial and operating results and
  maintain compliance with specified financial ratios" (Item 1A); "The Company is in compliance with all covenants"
  (Item 7, at 2025-12-31).
- Asbestos: named in "a number of asbestos-related lawsuits", those relating to an acquired business indemnified by its
  seller, "no judgments have been rendered against the Company" (10-K Note 13). Environmental reserves $37.4M at
  2025-12-31; PRP at 13 non-owned sites. Standby letters of credit and surety bonds $197.9M. Purchase obligations $669.0M due
  within one year.
- Customers: EIG's five largest 4% of its sales, none above 2%; EMG's five largest 15%, none above 5% (Item 1).
- International: 48.2% of sales outside the US; manufacturing in 22 countries outside the US, including China and Mexico
  (Item 1A).

**Bearing on Q10.** Nothing beyond Q7 and Q8.

**Bearing on Q12.** The businesses are instruments, components, specialty metals and aviation repair; defence and
aerospace customers are named; none of the businesses the rows name (casinos, tobacco, loading schemes) is among them.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was the first action after reading the brief, framework and
      template); written question by question. Committed after each closing with pathspec commits of my two paths: step 0
      (`627b659c`), Q1 and Q2 together (`9b71b57e`), Q3 and Q4 together (`077e31e2`), Q5 and Q6 together (`e20835ee`), Q7 and
      the close (this commit). **Departure: Q1/Q2, Q3/Q4 and Q5/Q6 were each written and committed as pairs, not one commit
      per question**; nothing was edited after its commit except one sentence moved in Q1 before Q1's commit. Another
      session held `.git/index.lock` repeatedly; my first commit attempt failed on it and a retrying script
      (`commit.sh`) was used.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (`Screens/_daily/_overnight.lock` read once: "interactive AME and v5 re-runs batch 6"); the fold is the
      dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what I saw by accident is declared
      under CONTAMINATION at the top (session git status, commit subjects including a KEYS run, the lock text, the memory
      index line), and two further commit subjects seen while checking my own commits (an ITW Q2 run and a JKHY run naming
      their Q1/Q2 closes). None was used.
- [x] Every v5 id resolves (`check_cites.py`: ids in the CSV, quoted fragments in their rows, no E-ids); every filing fact
      has its accession or is in a file whose accessions are listed (`annual_report_accessions.txt`, `comp_table.txt`).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance. The Q7 arithmetic
      was computed during Q3 and Q4 in the research folder, headed COMPUTATION, NOT A CLEARANCE, and reported only at Q7.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury par
      yield curve via `tools/run.py`; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found (Step 0 list; Q2 test 5; Q4 habits; Q6).
- [x] No row dated after the anchor is cited in a point-in-time run (this is not a point-in-time run; rows up to 2025 used).
- [x] Only the arithmetic lines of `tools/run.py` were used; its "owner earnings" on the D&A basis was not used (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in `check_framework_out.txt`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The default pair of specific (c) punishes a serial acquirer twice after year ten.** Deducting acquisitions from the
   base and crediting total growth for ten years, then "no real growth", keeps deducting the acquisition spending forever
   after year ten while crediting none of the growth it buys. For AMETEK (acquisitions about 80% of owner cash) this drives
   the central range to -$5.56 to $31.35 while the organic pair gives $82.64 to $119.94. The text does not say whether the
   acquisition deduction should stop when the growth stops. I applied it as written and showed the organic pair beside; the
   box does not turn on it, since the price is above both.
2. **"The midpoint of the range" in the fair price is not defined as a stream.** I read it as the year-by-year average of the
   two end streams discounted at the floor (whose value at the sovereign is exactly the midpoint of the range); a reader
   could instead apply the midpoint growth rate. With a negative central range the fair price is below zero, which the
   reporting convention does not anticipate; I report it as "below zero".
3. **EBITDA talk sits in two places.** Q4's "What it rules OUT" list names "EBITDA as earnings and managements that talk it
   [M2002-026]", while the 2026-10-06 convention sends featured adjusted figures to a Q4 weighing judged at Q5. The text
   does not say which governs a filer that puts EBITDA in its 10-K highlights beside GAAP. I treated it as a featured
   adjusted figure (weighing, judged at Q5).
4. **Q5's doubt rule against the habits.** The convention says the habits are read with the integrity record "and doubt
   closes the file", but it does not say whether a well-documented beat-and-raise habit with clean accounts is itself
   doubt. **[L2022-006]** calls beating expectations "disgusting"; I judged no doubt on honesty and said a stricter reader
   would close at Q5. The box is the same.
5. **The parts threshold and Q1.** The business-of-parts paragraph extends "matters" to segments, but a segment such as EIG is
   itself forty-odd niche businesses; the framework gives no rule for how far down the parts are read. I read EIG as a whole.
6. **The brief's error.** The brief asks for the competitors "from their own filings over the whole span" and lists Fortive
   and Danaher "for instruments". Fortive has filed its own reports only since its 2016 separation from Danaher and
   Keysight only since its 2014 separation from Agilent, so neither can cover 2008 to 2009 "from their own filings"; and
   Danaher's consolidated figures stopped being an instruments comparator when it spun off Fortive (2016) and Veralto
   (2023), leaving mainly life sciences and diagnostics. Roper, also listed, has been mainly software since about 2016. I
   used each filer's own XBRL for the years it exists and flagged the gaps in the competitor row; no non-filer was used.
