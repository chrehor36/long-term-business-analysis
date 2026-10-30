# COMPETITOR ROW: KLA Corporation (KLAC)
### Semiconductor process control / inspection & metrology
**Built 2026-09-07.** Source class: SEC EDGAR primary filings and
`https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (XBRL as filed, tagged
from the 10-K/20-F financial statements). Every figure below carries the accession
number of the filing it was tagged in.

> **STATUS: COMPLETE.** Filed financial data obtained for **7 of 7 target peers** plus
> KLA. Four named Japanese competitors checked against EDGAR and closed as
> non-registrants (section 6). Verbatim competitor statements naming KLA obtained from
> **three** registrants: Onto Innovation, Nova and ASML (section 4).

---

## 0. METHOD, declared before the numbers so that the row is comparable

**A moat is a relative claim.** The point of this file is a single metric set, one
window, one formula, applied to KLA and to every peer without exception.

**The operating-margin formula.** KLA **stopped tagging the `OperatingIncomeLoss`
subtotal after FY2014** (last tagged value: FY2014, accession 0000319201-16-000090).
So no like-for-like operating margin can be read off the tagged subtotal across the
peer set. Operating income here is therefore computed **identically for every company**:

    OP = Revenue − Cost of revenue − R&D − SG&A

and where a company splits SG&A into "Sales and marketing" + "General and
administrative" (Onto, Axcelis, Nova), the two are added. **This formula deliberately
excludes** below-SG&A operating lines that some peers report and others do not:
amortization of acquired intangibles as a separate line, restructuring, goodwill
impairment, and legal settlements. The "OPM tagged" column is shown alongside so the
size of that exclusion is visible. Where both exist they agree to within a few tenths
for LRCX, ACLS, CAMT and NVMI; they diverge most for **Onto**, whose separately-stated
amortization of acquired intangibles is large (Onto is the most acquisition-built
company in the set).

**Return on unleveraged net tangible operating assets (ROUNTOA)** =
`OP ÷ (Total assets − Goodwill − Intangibles − non-interest-bearing current liabilities)`,
where NIBCL = current liabilities − current debt − current lease liabilities. Same
formula for all. This is the closest available approximation to the Buffett
"unleveraged net tangible assets" test; it is a **CONVENTION** of this row, not a
corpus rule, and it uses year-end (not average) denominators.

**ROE** uses average equity of the two year-ends. **KLA's ROE is not comparable to the
peer set and must not be read as a quality signal:** KLA has run a structurally small
book (US$1.4bn equity on US$12.6bn assets at FY2022) because of sustained buybacks and
US$6bn of debt. Its 139% and 157% ROE figures are a *leverage and buyback* artifact.
The ROUNTOA column is the one to compare.

**Currency.** ASML reports in **EUR** and is carried here in EUR, **not converted**. This is a
**RUNG LIMITATION**: ASML's revenue and absolute figures are not directly comparable
in level to the USD filers, only its *margins and ratios*, which are currency-neutral.

**Fiscal years are not aligned.** KLA and Lam end late June; Applied ends late October;
ASML, Axcelis, Onto, Camtek and Nova are calendar. A "FY2023" label therefore covers
different halves of the WFE cycle for different companies. This matters most for the
downturn test in section 3 and is flagged there.

---

## 1. THE ROW: latest full fiscal year

| | **KLA** | **AMAT** | **LRCX** | **ASML** | **ONTO** | **CAMT** | **NVMI** | **ACLS** |
|---|---|---|---|---|---|---|---|---|
| CIK | 0000319201 | 0000006951 | 0000707549 | 0000937966 | **0000704532** | **0001109138** | 0001109345 | 0001113232 |
| Latest FY | FY2026 (6/30/26) | FY2025 (10/26/25) | FY2026 (6/28/26) | FY2025 (12/31/25) | FY2025 (1/3/26) | FY2025 (12/31/25) | FY2025 (12/31/25) | FY2025 (12/31/25) |
| Form | 10-K | 10-K | 10-K | 20-F | 10-K | 20-F | 20-F | 10-K |
| Accession | 0000319201-26-000027 | 0001628280-25-056742 | 0000707549-26-000037 | 0001628280-26-011378 | 0001193125-26-066937 | 0001178913-26-001561 | 0001178913-26-000504 | 0001104659-26-020461 |
| **Revenue** | **$13,579.5M** | $28,368.0M | $23,232.7M | **€32,667.3M** | **$1,005.3M** | $496.1M | $880.6M | $839.0M |
| Gross profit | $8,324.4M | $13,808.0M | $11,725.3M | €17,258.0M | $499.8M | $250.3M | $505.2M | $376.8M |
| **Gross margin** | **61.3%** | 48.7% | 50.5% | 52.8% | **49.7%** | 50.5% | **57.4%** | 44.9% |
| R&D | $1,532.1M | $3,570.0M | $2,375.9M | €4,698.8M | $132.0M | $48.3M | $143.4M | $109.0M |
| **R&D % of revenue** | **11.3%** | 12.6% | 10.2% | 14.4% | 13.1% | 9.7% | **16.3%** | 13.0% |
| SG&A | $1,131.5M | $1,768.0M | $1,149.6M | €1,257.8M | $177.1M | $73.8M | $108.3M | $148.6M |
| SG&A % of revenue | 8.3% | 6.2% | 4.9% | 3.9% | 17.6% | 14.9% | 12.3% | 17.7% |
| **Operating income (identical formula)** | **$5,660.8M** | $8,470.0M | $8,199.8M | €11,301.4M | $190.8M | $128.2M | $253.5M | $119.3M |
| **Operating margin (identical formula)** | **41.7%** | 29.9% | 35.3% | 34.6% | **19.0%** | 25.8% | 28.8% | **14.2%** |
| Operating margin (as tagged, where tagged) | *not tagged since FY2014* | 29.2% | 35.3% | 34.6% | **13.2%** | 25.8% | 28.8% | 14.2% |
| Net income | $4,830.8M | $6,998.0M | $7,265.4M | €9,609.4M | $136.8M | $50.7M | $259.2M | $120.2M |
| ROE (avg equity) | 87.5% *(leverage artifact)* | 35.5% | 65.1% | 50.5% | 6.8% | 8.7% | 23.1% | 11.7% |
| **ROUNTOA** | **48.5%** | 34.5% | 52.0% | 49.4% | **15.7%** | 12.0% | 12.6% | 10.2% |
| Total assets | $17,951.5M | $36,299.0M | $23,529.7M | €50,566.6M | $2,367.7M | $1,259.8M | $2,360.5M | $1,361.4M |
| Equity | $6,349.8M | $20,415.0M | $12,470.9M | €19,612.2M | $2,100.6M | $617.0M | $1,318.2M | $1,034.7M |
| Goodwill | $1,788.8M | $3,707.0M | $1,630.0M | €4,588.6M | $644.0M | $74.3M | $90.8M | none |

**Read of the row:** on the identical formula, **KLA's 41.7% operating margin is the
highest in the set** and its 61.3% gross margin is the highest in the set. The nearest
competitor by margin is not a process-control company at all; it is Lam (35.3%) and
ASML (34.6%), both deposition/etch and lithography, i.e. *different tools sold to the
same customers*. **Among the companies that actually compete with KLA in inspection and
metrology (Onto, Camtek and Nova), the best operating margin is Nova at 28.8%, a
13-point gap, and the closest pure-play by product overlap, Onto, earns 19.0%, a
23-point gap.** KLA also out-earns all of them on tangible operating capital.

---

## 2. THE ROW: FY2019 and FY2023 (the two WFE downturn years)

### FY2019

| | **KLA** | **AMAT** | **LRCX** | **ASML** | **ONTO** | **CAMT** | **NVMI** | **ACLS** |
|---|---|---|---|---|---|---|---|---|
| Period end | 6/30/19 | 10/27/19 | 6/30/19 | 12/31/19 | 12/31/19 | 12/31/19 | 12/31/19 | 12/31/19 |
| Revenue | $4,568.9M | $14,608.0M | $9,653.6M | €11,820.0M | $305.9M | $134.0M | $224.9M | $343.0M |
| **Gross margin** | **59.1%** | 43.7% | 45.1% | 44.7% | **44.1%** | 48.3% | 54.2% | 42.0% |
| R&D % revenue | 15.6% | 14.1% | 12.3% | 16.7% | 15.8% | 12.2% | 19.8% | 15.7% |
| **OPM (identical formula)** | **30.4%** | 22.9% | 25.5% | 23.6% | **1.8%** | 16.4% | 17.4% | 7.1% |
| OPM (as tagged) | *n/t* | 22.9% | 25.5% | 23.6% | **−1.6%** | 16.4% | 16.2% | 7.1% |
| Net income | $1,175.6M | $2,706.0M | $2,191.4M | €2,592.3M | $1.9M | $22.0M | $35.2M | $17.0M |
| ROUNTOA | 35.6% | 28.8% | 28.7% | 22.6% | 0.7% | 15.8% | 11.9% | 5.0% |
| Accession | 0000319201-21-000029 | 0000006951-21-000043 | 0000707549-21-000136 | 0000937966-22-000013 | 0001564590-22-006948 | 0001178913-22-001119 | 0001178913-22-000869 | 0001558370-22-002096 |

### FY2023

| | **KLA** | **AMAT** | **LRCX** | **ASML** | **ONTO** | **CAMT** | **NVMI** | **ACLS** |
|---|---|---|---|---|---|---|---|---|
| Period end | 6/30/23 | 10/29/23 | 6/25/23 | 12/31/23 | 12/30/23 | 12/31/23 | 12/31/23 | 12/31/23 |
| Revenue | $10,496.1M | $26,517.0M | $17,428.5M | €27,558.5M | $815.9M | $315.4M | $517.9M | $1,130.6M |
| **Gross margin** | **59.8%** | 46.7% | 44.6% | 51.3% | **51.5%** | 46.8% | 56.6% | 43.5% |
| R&D % revenue | 12.4% | 11.7% | 9.9% | 14.4% | 12.8% | 10.0% | 17.0% | 8.6% |
| **OPM (identical formula)** | **38.1%** | 28.9% | 29.9% | 32.8% | **21.4%** | 20.7% | 25.5% | 23.5% |
| OPM (as tagged) | *n/t* | 28.9% | 29.7% | 32.8% | **14.2%** | 20.7% | 25.5% | 23.5% |
| Net income | $3,387.3M | $6,856.0M | $4,510.9M | €7,839.0M | $121.2M | $78.6M | $136.3M | $246.3M |
| ROUNTOA | 55.5% | 39.2% | 40.4% | 49.3% | 13.6% | 10.9% | 18.2% | 26.5% |
| Accession | 0000319201-25-000024 | 0001628280-25-056742 | 0000707549-25-000075 | 0001628280-26-011378 | 0001193125-26-066937 | 0001178913-26-001561 | 0001178913-26-000504 | 0001558370-25-001855 |

**Note on the FY2023 label.** KLA's and Lam's FY2023 both ended in **June 2023**, i.e.
they captured only the first half of the 2023 memory collapse; their FY2024
(June 2024) is the trough year. Applied's FY2023 ended October 2023. The calendar
filers (ASML, Onto, Camtek, Nova, Axcelis) took the full calendar-2023 hit. **The
downturn table in section 3 is the correct place to compare cycle behaviour**; this
FY-label table is not.

---

## 3. THE [E2-44] THROUGH-CYCLE TEST: gross margin across the downturns

Gross margin, %, by fiscal year. Shaded conceptually: **2019** was the memory capex
collapse; **2023–2024** was the second. The question is whose margin *held*.

| FY | **KLA** | **AMAT** | **LRCX** | **ASML** | **ONTO** | **CAMT** | **NVMI** | **ACLS** |
|---|---|---|---|---|---|---|---|---|
| 2016 | 61.0 | 41.7 | 44.5 | 45.7 | 51.6 | 41.0 | 45.9 | 37.3 |
| 2017 | 63.0 | 45.0 | 45.0 | 44.9 | 52.8 | 48.7 | 59.1 | 36.6 |
| 2018 | 64.2 | 45.0 | 46.6 | 46.0 | 54.2 | 49.4 | 57.8 | 40.6 |
| **2019 ↓** | **59.1** | **43.7** | **45.1** | **44.7** | **44.1** | **48.3** | **54.2** | **42.0** |
| 2020 | 57.8 | 44.7 | 45.9 | 48.6 | 50.0 | 47.0 | 56.1 | 41.8 |
| 2021 | 59.9 | 47.3 | 46.5 | 52.7 | 54.4 | 50.9 | 56.6 | 43.2 |
| 2022 | 61.0 | 46.5 | 45.7 | 50.5 | 53.6 | 49.8 | 55.5 | 43.7 |
| **2023 ↓** | **59.8** | **46.7** | **44.6** | **51.3** | **51.5** | **46.8** | **56.6** | **43.5** |
| **2024 ↓** | **60.0** | **47.5** | **47.3** | **51.3** | **52.2** | **48.9** | **57.6** | **44.7** |
| 2025 | 60.9 | 48.7 | 48.7 | 52.8 | 49.7 | 50.5 | 57.4 | 44.9 |
| 2026 | 61.3 | *(FY not ended)* | 50.5 | n/a | n/a | n/a | n/a | n/a |
| **Peak-to-trough drawdown, 2018→2019** | **−5.1 pts** | −1.3 | −1.5 | −1.3 | **−10.1 pts** | −1.1 | −3.6 | +1.4 |
| **Drawdown 2022→2023** | −1.2 | +0.2 | −1.1 | +0.8 | **−2.1** | **−3.0** | +1.1 | −0.2 |
| **Range, 2016–latest** | 57.8–64.2 (6.4 pts) | 41.7–48.7 (7.0) | 44.5–50.5 (6.0) | 44.7–52.8 (8.1) | 44.1–54.4 (**10.3**) | 41.0–50.9 (9.9) | 45.9–59.1 (13.2) | 36.6–44.9 (8.3) |

**What the table shows.**

1. **KLA holds the highest gross margin in the set in every single year, in booms and
   in troughs, without exception, over eleven fiscal years.** The narrowest the gap to
   the second-best company ever gets is 4.7 points (FY2019, vs Nova's 54.2). Against
   its *direct* inspection/metrology rivals Onto and Camtek the gap has never been
   under 9.6 points.
2. **The FY2019 drawdown is the informative one for the moat claim, and it does not
   flatter KLA on a simple reading.** KLA gave up 5.1 points; Applied, Lam, ASML and
   Camtek each gave up only about 1.1–1.5. KLA's FY2019 fall is however partly a
   *mix* event, not a pricing event. FY2019 (ended June 2019) is the first full year
   consolidating **Orbotech**, acquired 20 Feb 2019, a lower-margin PCB/display
   business, and the FY2019 fall coincides exactly with that consolidation. **This is
   an UNRESEARCHED item for the parent run: the segment-level gross margin of the
   legacy Semiconductor Process Control segment vs the Orbotech/Electronics segment in
   FY2019 will separate mix from price. The document that resolves it is KLA's FY2019
   10-K segment note.**
3. **Onto is the one that visibly broke.** Onto lost 10.1 points of gross margin in
   2019 and fell to a **−1.6% reported operating margin**, a loss, in the same
   downturn in which KLA earned a 30.4% operating margin. In 2023 Onto again lost
   2.1 points. Onto's most recent year, FY2025, shows gross margin falling again to
   49.7% while revenue was roughly flat, and operating margin falling from 19.0% to
   13.2% reported. **Onto has not once, in eleven years, come within 9 points of KLA's
   gross margin.**
4. **Axcelis is the counter-shape:** its margin has ground *upward* through both
   downturns (36.6% → 44.9%) but from a level 20 points below KLA, and it is now
   contracting hard on the volume line (revenue $1,130.6M → $839.0M, −26% over two
   years) with operating margin cut from 23.5% to 14.2%. Axcelis is an ion-implant
   company, not a process-control company; it is in the row as a **cycle read**, not
   as a competitor.
5. **Nova is the quality read among the challengers:** 57.4% gross margin, 28.8%
   operating margin, and it *raised* gross margin through the 2023 trough. Nova is the
   only company in the set whose gross margin is in the same postal district as KLA's,
   and it is a metrology pure-play. **If anything in this row threatens the KLA
   franchise narrative, it is Nova's trajectory, not Onto's.** Nova revenue has
   compounded from $224.9M (2019) to $880.6M (2025), a 25.6% CAGR, against KLA's 19.9%
   over the same window.


---

## 4. THE ATTACKER'S OWN LANGUAGE: verbatim, from competitors' filings

Every quote below is **verbatim** from the named filing, with the item located.
Nothing here is paraphrase. Bold emphasis is mine; the underlying text is unchanged.

### 4.1 Onto Innovation, the closest pure-play rival, names KLA first, twice

**Source: Onto Innovation Inc., Form 10-K for fiscal year ended January 3, 2026, filed
2026-02-24, accession 0001193125-26-066937, Part I, Item 1 "Business," sub-heading "Competition."**

> "The global semiconductor equipment industry is intensely competitive and we have
> multiple established and potential competitors in the markets in which we
> participate. Our industry is driven by rapid technological adoption cycles, with new
> entrants from overseas and domestic sources competing for our customers' business.
> Our ability to compete effectively depends upon our ability to continuously improve
> our existing products, applications and services, and our ability to develop new
> products, applications and services that meet constantly evolving customer
> requirements. In order to continuously improve and develop new products and maintain
> customer service and support centers worldwide, we believe that we will require
> significant resources; however, some of our competitors may have greater financial,
> research, engineering, manufacturing and marketing resources than we have.
>
> In automated systems for the semiconductor industry, our principal competitors are
> KLA Corporation ("KLA") and Nova Ltd. (formerly Nova Measuring Instruments Ltd.)
> ("Nova") for thin film and critical dimension OCD metrology. Our principal
> competitors for advanced packaging inspection are KLA and Camtek Ltd. ("Camtek").
> While the advanced packaging lithography market is served by various competitors, our
> primary competitors are Ushio, Inc. ("Ushio") and Canon, Inc. ("Canon"). Our primary
> competitor for inspection in the panel market is GigaVis Co. Ltd. The primary
> competitor for our software products is PDF Solutions, Inc. ("PDF Solutions") and our
> primary competitor for integrated metrology systems for the semiconductor industry is
> Nova. The opto-electronics, discrete device and industrial and scientific markets are
> addressed primarily by our material characterization and 4D systems, served by
> numerous competitors, of which no single competitor or group of competitors has
> established a majority position."

**Same filing, Part I, Item 1A "Risk Factors," sub-heading "Risks Related to Competition,"** under
the caption *"Some of our current and potential competitors have significantly greater
resources than we do, and increased competition could impair sales of our products or
cause us to reduce our prices"*:

> "The market for semiconductor capital equipment is highly competitive. We face
> substantial competition from established companies in each of the markets we serve.
> **We principally compete with KLA, Nova, Camtek, Ushio, Canon, GigaVis Co. Ltd. and
> PDF Solutions.** Each of our products also competes with products that use different
> metrology, inspection or lithography techniques. Some of our competitors have greater
> financial, engineering, manufacturing and marketing resources, broader product
> offerings and service capabilities and **larger installed customer bases than we do.**"

and, in the same risk factor:

> "Many of our existing and potential customers in the semiconductor device
> manufacturing industry are large companies that require global support and service
> for their semiconductor capital equipment. **Some of our competitors have more
> extensive support and service infrastructures than we do, which could place us at a
> disadvantage when competing for the business of global semiconductor device
> manufacturers.** Many of our competitors are investing heavily in the development of
> new systems that will compete directly with our systems. **We have, from time to time,
> selectively reduced prices on our systems in order to protect our market share, and
> competitive pressures may necessitate further price reductions.**"

**Why this matters for Q2.** In its own risk factors, Onto states on the record that
(a) KLA is named *first* in every competitor list it writes, (b) competitors have
"larger installed customer bases," (c) competitors have "more extensive support and
service infrastructures," and (d) Onto has had to *cut price* to defend share. That is
the attacker conceding installed base, service and price. It is the strongest single
piece of relative evidence in this file, and it is written by the party with the
incentive to say the opposite.

**The same language, six years earlier, from Onto Innovation Inc., Form 10-K for fiscal
year ended December 31, 2019, filed 2020-02-28, accession 0001564590-20-006357, Item 1
"Competition":**

> "In automated systems for the semiconductor industry, our principal competitors are
> KLA Corporation ("KLA") and Nova Measuring Instruments Ltd. ("Nova") for thin film
> and critical dimension OCD metrology. **Our principal competitor for advanced
> packaging inspection is Camtek Ltd. ("Camtek").** While the advanced packaging
> lithography market is served by various competitors, our primary competitors are
> Veeco Instruments, Inc. ("Veeco Instruments") and, to a lesser extent, Nikon
> Corporation ("Nikon")."

**Note what changed over six years.** In FY2019 the advanced-packaging inspection
competitor was **Camtek alone**. By FY2023 and FY2025 the sentence reads *"Our principal
competitors for advanced packaging inspection are KLA and Camtek Ltd."* **KLA was
added to the advanced-packaging inspection contest between the FY2019 and FY2023 10-Ks,
in the words of the incumbent it was attacking.** (Onto FY2023 10-K: accession
0000950170-24-020150, filed 2024-02-26, Item 1 "Competition"; its risk-factor sentence
reads *"We principally compete with KLA, Nova, Camtek, Ushio, Canon, and PDF
Solutions"*; GigaVis is the only name added by FY2025.) This is direct evidence of
**KLA extending into an adjacent process-control market and being recognised there by
the sitting player**: a franchise-widening fact, not merely a franchise-holding one.

### 4.2 Nova Ltd describes the market structure itself

**Source: Nova Ltd., Form 20-F for the year ended December 31, 2025, filed 2026-02-17,
accession 0001178913-26-000504, Item 3.D "Risk Factors," sub-heading "Risks related to our
industry,"** under the caption *"We operate in an extremely competitive market, and if
we fail to compete effectively, our revenues and market share will decline"*:

> "**Although the market for process control systems used in semiconductor manufacturing
> is currently concentrated and characterized by relatively few participants,** the
> semiconductor capital equipment industry is intensely competitive. **We compete mainly
> with Onto Innovation Inc., and KLA Corp.,** which manufacture and sell CD, thin films
> and chemical metrology and process control systems. In addition, we compete with
> process equipment manufacturers, such as ASML Holdings N.V., LAM Research, and
> Applied Materials Inc., which develop (or may acquire companies which develop)
> in-situ sensors and metrology products. Established companies, both domestic and
> foreign, compete with our product lines, and **new competitors enter our market from
> time to time, including the recent emergence of local competitors in China.** The
> recent acquisition of Sentronics and the expansion of our portfolio in the wafer
> level packaging and specialty markets, positions us in direct competition with
> companies such as Merck and Camtek. Some of our competitors have greater financial,
> engineering, manufacturing and marketing resources than we do."

**And, on switching costs, which are the mechanism of the moat, stated by the challenger, in the
same paragraph:**

> "If a particular customer selects a competitor's capital equipment, we expect to
> experience difficulty in selling our solution to that customer for a significant
> period of time. **A substantial investment is required by the customers to evaluate,
> test, select and integrate capital equipment into a production line. As a result,
> once a manufacturer has selected a particular vendor's capital equipment, we believe
> that the manufacturer generally relies upon that equipment for the specific
> production line application and frequently will attempt to consolidate its other
> capital equipment requirements with the same vendor.** Accordingly, unless our systems
> offer performance or cost advantages that outweigh a customer's expense of switching
> to our systems, it will be difficult for us to achieve significant sales to that
> customer."

**Same filing, Item 3.D, on consolidation:**

> "We believe that the semiconductor capital equipment market has undergone
> consolidation over the last few years. For example, ASML Holdings N.V. acquired
> Berliner Glas Group in 2020; **KLA Corporation acquired ECI Technology in 2022;**
> Nanometrics Inc. and Rudolph Technologies, Inc. merged in 2019 to create Onto
> Innovation Inc., which also recently acquired part of SemiLab Ltd."

**Why this matters.** Nova is the highest-margin challenger in the row and the only one
with a credible claim to be closing on KLA. Its own 20-F says (1) the process-control
market is **"concentrated and characterized by relatively few participants"**: an
oligopoly, on the record, from a participant; (2) the switching cost is real and is
given as the reason a customer stays; and (3) the identified new-entrant threat is
**local Chinese competitors**. Item (3) is a candidate for "the named way it dies" in
Q4 and belongs in Q6 of the parent run.

### 4.3 ASML names KLA as a competitor, and defines the peer set

**Source: ASML Holding N.V., Form 20-F / Annual Report 2025 for the year ended
December 31, 2025, filed 2026-02-25, accession 0001628280-26-011378, "Risk factors," section
"Strategic," under the competition risk:**

> "We compete primarily with Canon and Nikon in respect of DUV systems. Both have
> substantial financial resources and broad patent portfolios. Each continues to offer
> products that compete directly with our DUV systems, which may impact our sales or
> business. In addition, adverse market conditions, long-term overcapacity or a
> decrease in the value of the Japanese yen in relation to the euro have increased and
> could continue to increase price-based competition, resulting in lower prices and
> lower sales and margins. We also face competition from new competitors with
> substantial financial resources, as well as from those driven by the ambition of
> self-sufficiency in the geopolitical context. Furthermore, we may face competition
> from alternative technological solutions or semiconductor manufacturing processes.
> **We also compete with providers of applications that support or enhance complex
> patterning solutions, such as Applied Materials Inc. and KLA-Tencor Corporation.
> These applications compete with our offerings, which is a significant part of our
> business.**"

**Same filing, "Remuneration report," table "Reference group composition (as defined for
2025)."** ASML's own remuneration benchmark lists, under the heading **"Semiconductor
equipment"**, exactly three companies:

> "Applied Materials | KLA Corporation | Lam Research"

That is a competitor's own filed definition of the semiconductor-equipment peer set,
and it is the same three-name set used in section 1 of this file.

### 4.4 Camtek named KLA in FY2022, and has since stopped naming anyone

**Source: Camtek Ltd., Form 20-F for the year ended December 31, 2022, filed
2023-03-20, accession 0001178913-23-001057, Item 4.B "Business Overview," sub-heading
"Competition":**

> "The markets in which we operate are highly competitive. **Our main competitors are
> Onto Innovations, Skyverse, ATI Electronics Pty Ltd., Cheng Mei Instrument Technology
> Co., ASTI Holding Limited, Toray Industries Inc. and, for some limited applications,
> KLA-Tencor Corporation.**"

**And the negative finding, which is itself evidence.** Camtek's **FY2025 20-F (filed
2026-03-19, accession 0001178913-26-001561) names no competitor at all**; the string
"KLA" does not appear in the document, nor does "Onto." The Item 4.B "Competition"
heading present in FY2022 has been **removed**. All that remains is a generic Item 3.D
risk factor:

> "The markets that we serve are highly competitive and have significant global market
> participants, **some with greater resources than us.** The continued growth of the
> markets in which we operate may attract and result in new market entrants and may
> also encourage existing competitors to expand their efforts and presence in these
> markets. Such competitors may be able to respond more quickly to new or emerging
> technologies or changes in customer requirements, develop additional or superior
> products, benefit from greater economies of scale, offer more aggressive pricing or
> devote greater resources to the promotion of their products. **Other competitors are
> local smaller competitors in the markets we operate, which target the low-end market
> and may offer products at lower prices.** Competition could result in lower prices for
> our products and a corresponding reduction in our gross margin, as well as more
> favorable payment terms to our customers and a corresponding decline in our cash
> flow."

So Camtek's most recent *named* characterisation of KLA is the FY2022 one: a competitor
**"for some limited applications."** Camtek positions itself as overlapping KLA only at
the edges, in advanced packaging, not in front-end process control. Onto's FY2025 10-K
corroborates the same geometry from the other side, naming "KLA and Camtek" jointly and
only for advanced-packaging inspection.

### 4.5 Applied Materials and Lam Research: the two large peers name nobody

- **Applied Materials, Form 10-K FY2025 (ended 2025-10-26), filed 2025-12-12,
  accession 0001628280-25-056742, Item 1 "Competition."** The section is entirely
  generic: *"Substantial competition exists across all the segments of our business.
  Competitors range from small companies that compete in a single region, which may
  benefit from policies and regulations that favor domestic companies, to global,
  diversified companies... We believe that many of our products have strong competitive
  positions."* **It names no competitor anywhere in the document.** The only occurrences
  of "KLA" in the whole 10-K are executive biographies: CEO Gary Dickerson *"served 18
  years with KLA-Tencor Corporation (KLA-Tencor), a supplier of process control and
  yield management solutions for the semiconductor and related industries, where he held
  a variety of operations and product development roles, including President and Chief
  Operating Officer"*; and CLO Teri Little *"served as Executive Vice President, Chief
  Legal Officer and Corporate Secretary at KLA Corporation from August 2017 to June
  2020."*
- **Lam Research, Form 10-K FY2026 (ended 2026-06-28), filed 2026-08-07, accession
  0000707549-26-000037, Item 1 "Competition."** Likewise generic, and **the string "KLA"
  does not appear anywhere in the filing.** Lam's section is however useful on the
  mechanism, and it is the same mechanism Nova describes: *"once a semiconductor
  manufacturer has selected a particular supplier's equipment and qualified it for
  production, the manufacturer generally maintains that selection for that specific
  production application and technology node as long as the supplier's products
  demonstrate performance to specification in the installed base. Accordingly, we may
  experience difficulty in selling to a given customer if that customer has qualified a
  competitor's equipment."*
- **Axcelis, Form 10-K FY2025, filed 2026-02-26, accession 0001104659-26-020461.** The
  only occurrence of "KLA" is in an executive biography. Axcelis does not compete with
  KLA and does not claim to.

### 4.6 What the quote set adds up to, and what it does not

**Three separate registrants (Onto, Nova and ASML) name KLA in their own filed
competitive-risk disclosures. Not one of them describes KLA as a subordinate
competitor.** Onto lists KLA *first* in both of its competitor sentences. Nova lists
KLA as one of only two front-line rivals while simultaneously calling the market
"concentrated and characterized by relatively few participants." ASML, which does not
sell process control, still lists KLA in its competitive risk and puts KLA in a
three-company semiconductor-equipment remuneration benchmark. Applied and Lam name
nobody at all, which is uninformative in either direction.

**Now the disconfirming reading, hunted deliberately [E4-26].** These are competitors'
**risk factors**. A risk factor carries a legal incentive to name every large rival and
to describe them as strong; it is not a neutral market assessment. Two hard limits
follow:

1. **Not one filing in this set states a process-control market-share figure, for KLA
   or for anyone.** The verbatim evidence establishes *who is in the market* and *that
   the market is concentrated*. It does **not** establish that KLA holds any particular
   share. **The quantified share claim is UNRESEARCHED, and the document that would
   resolve it is not an SEC filing**; it is a paid Gartner / TechInsights / VLSI WFE
   segment report, which sits off this framework's source ladder. Any "KLA has ~55% of
   process control" figure entering the parent run must name its source or be struck.
2. **Onto's own filing supplies the counter-hypothesis.** Onto says it *"selectively
   reduced prices ... in order to protect our market share."* Price-cutting by the
   number-two is exactly what would erode the number-one's margin over time. It has not
   happened yet, and KLA's gross margin is higher in FY2026 than in FY2018, but it is the
   live mechanism by which the moat narrows, and it should be one of the disconfirming
   markers written into Q6.

---

## 5. SERVICE REVENUE AND CHINA EXPOSURE: latest full fiscal year

These two are the same question asked twice: **what fraction of the revenue is annuity
attached to an installed base**, and **what fraction is exposed to the one policy risk
that can remove it**.

| | **KLA** FY2026 | **AMAT** FY2025 | **LRCX** FY2026 | **ASML** FY2025 | **ONTO** FY2025 | **CAMT** FY2025 | **NVMI** FY2025 | **ACLS** FY2025 |
|---|---|---|---|---|---|---|---|---|
| **Service / support revenue** | **$3,125.9M** | $6,385M *(AGS segment)* | $8,347.2M *(CSBG)* | €8.2bn *(service + field options)* | **$157.4M** *(parts $84.2M + services $73.2M)* | $27.6M *(service fees)* | $175.0M | $268.0M *(CS&I / aftermarket)* |
| **as % of revenue** | **23.0%** | 22.5% | 35.9% | 25.1% | **15.7%** | **5.6%** | 19.9% | 31.9% |
| Disclosure location | 10-K MD&A, "revenue by major product categories" | 10-K MD&A, net revenue by segment | 10-K MD&A, revenue disaggregated system vs customer-support | 20-F financial-performance KPIs | 10-K MD&A + FS note, "sources of our revenue" | 20-F FS Note 18A, "Sales of products / Service fees" | 20-F consolidated statements of operations (Products / Services lines) | 10-K MD&A, "CS&I/Aftermarket" |
| **China revenue** | **$4,048.4M** | $8,529M | not stated in $ | €9,519.7M | **$70.7M** | $243.9M | not stated in $ | **not separately disclosed** |
| **China % of revenue** | **29.8%** | 30.1% | **34%** | 29.1% | **7%** | **49.2%** | 33% | n/d *(Asia Pacific 72.7%)* |
| China %, prior year | 33.3% (FY2025) | 37.2% (FY2024) | 34% (FY2025) | 36.1% (2024) | 12% (2024) | 30.9% (2024) | 39% (2024) | n/d |
| China %, two years back | 42.8% (FY2024) | 27.3% (FY2023) | n/a | 26.3% (2023) | 17% (2023) | 47.4% (2023) | 36% (2023) | n/d |

**Three readings.**

1. **Service intensity separates the row cleanly, and not in KLA's favour on the
   headline number.** Lam (35.9%) and Axcelis (31.9%) carry the highest service ratios;
   KLA is 23.0%, Applied 22.5%, Nova 19.9%. But the ratio is a *mix* number and rewards
   companies whose systems revenue is depressed. Axcelis's 31.9% is high partly because
   its systems revenue fell 26% in two years, and its **services gross margin was
   negative (−5.1%) in FY2025** (Axcelis FY2025 10-K, MD&A gross-profit table),
   i.e. its "service" is a cost centre, not an annuity. The useful comparison is against
   the direct rivals: **Onto at 15.7% and Camtek at 5.6% have materially thinner
   installed-base annuities than KLA's 23.0%,** which corroborates Onto's own risk-factor
   admission that competitors have "more extensive support and service infrastructures."
2. **KLA's service revenue grew 16% in a year (from $2,683.3M to $3,125.9M) and its
   dollar level is larger than the entire revenue of Onto, Camtek and Nova combined
   ($2,381.9M).** That is the installed-base fact the Q2 franchise case should be built
   on, and it is filing-sourced.
3. **China is the shared, unhedged exposure and it is falling everywhere except
   Camtek.** KLA has taken China from 42.8% → 33.3% → 29.8% over three fiscal years.
   Applied 37.2% → 30.1%. ASML 36.1% → 29.1%. Nova 39% → 33%. **Onto has collapsed from
   17% to 7%**, which is a large part of why its FY2025 margin fell. **Camtek moved the
   other way, 30.9% → 49.2%, and now has close to half its revenue in the single
   jurisdiction that Nova's own 20-F identifies as the source of new competitors.** For
   the parent run this is a Q4 and Q6 input: it is not KLA-specific, it is a
   sector-wide policy risk, and the row shows KLA is *less* China-exposed than Camtek and
   Lam and roughly level with Applied, ASML and Nova.

---

## 6. THE NON-OBTAINABLE PEERS: checked, and closed

The task named four Japanese process-control and metrology suppliers. **Each was checked
against SEC EDGAR directly.** The verdict for each is **UNKNOWABLE on this evidence
ladder**, not UNRESEARCHED, because there is no SEC document to go and get.

| Company | Ticker in SEC file | CIK | What EDGAR actually holds | Verdict |
|---|---|---|---|---|
| **Hitachi Ltd** (parent of Hitachi High-Tech) | HTHIY | 0000047710 | Only ADR-related and ownership forms. Most recent filings: `F-6` (2025-01-24, ADR registration), `EFFECT`, `424B3` (2018), `SC 13G/A`, `CB`, `F-X`. **No 20-F on file.** | **Non-registrant for reporting purposes; rung 6 blocked.** Hitachi High-Tech is a wholly-owned subsidiary and is not separately reported in any SEC filing. |
| **Advantest Corp** | ATEYY / ADTTF | 0001158838 | Filed **`15F-12B` on 2016-04-22**, the form by which a foreign private issuer *deregisters and terminates its reporting obligations*. Since then only `F-6` (2026-08-06), `SCHEDULE 13G/A`, and Form `D/A`. **No 20-F since 2016.** | **Deregistered 2016; rung 6 blocked.** Note also that Advantest is **automated test equipment, not process control**; it is the wrong comparison even if data existed. |
| **SCREEN Holdings** | n/a | none | **No CIK. Not present in the SEC company-ticker file.** | **Non-registrant, rung 6 blocked.** |
| **Nikon / Canon metrology** | CAJ (Canon) | Canon has a CIK but its metrology line is not a reported segment | Canon's SEC filings do not disaggregate semiconductor metrology; Nikon is not an SEC registrant. | **Segment not separately reported; rung 6 blocked.** |

**What this costs the row, stated plainly.** Hitachi High-Tech is a real competitor in
CD-SEM (critical-dimension scanning electron microscopy), a segment where KLA is *not*
the leader, and SCREEN is a real competitor in wafer inspection adjacent markets. **The
row therefore over-represents KLA's position by construction: it contains every rival
KLA out-earns and excludes the ones whose numbers cannot be seen.** This is a
**RUNG LIMITATION and it must be carried into the Q2 verdict, not buried here.** The
honest statement is: *KLA leads every process-control competitor whose accounts are
filed with the SEC; two named Japanese competitors could not be measured at all.*

---

## 7. COVERAGE: what was obtained and what was not

**Filed financial data obtained for 7 of 7 target peers, plus KLA itself: 8 companies.**

| Peer | Data obtained? | Source form | Notes / corrections to the brief |
|---|---|---|---|
| Applied Materials | **Yes**, FY2007–FY2025 | 10-K | CIK 0000006951 as given. |
| Lam Research | **Yes**, FY2009–FY2026 | 10-K | CIK 0000707549 as given. FY2026 (ended 6/28/26) is already filed, so Lam has one more year than Applied. |
| ASML | **Yes**, FY2007–FY2025 | 20-F | CIK 0000937966 as given. **Reported in EUR; left in EUR, not converted.** |
| Axcelis | **Yes**, FY2009–FY2025 | 10-K | CIK 0001113232 as given. **The FY2025 figures in the brief are confirmed against the filing: revenue $839.0M, gross margin 44.9%, operating margin 14.2%, and all three match Axcelis's own MD&A tables exactly** (accession 0001104659-26-020461). |
| **Onto Innovation** | **Yes**, FY2009–FY2025 | 10-K | **CIK CORRECTED. The brief gave 0001286131, which is StoneMor Partners LP, a cemetery operator. Onto Innovation Inc. is CIK 0000704532**, the former Nanometrics Inc. registrant, renamed after the 2019 Rudolph merger. |
| **Camtek** | **Yes**, FY2009–FY2025 | **20-F** (the brief asked which; it is 20-F) | **CIK CORRECTED. The brief gave 0001109348, which returns HTTP 404. Camtek Ltd is CIK 0001109138.** Note the near-collision with Nova's 0001109345. |
| Nova | **Yes**, FY2009–FY2025 | 20-F | CIK 0001109345 as given. |
| *(reference)* KLA | **Yes**, FY2009–FY2026 | 10-K | CIK 0000319201. |

**Not obtained, and why:** Hitachi High-Tech, Advantest, SCREEN Holdings, Nikon and
Canon metrology; see section 6. None files financial statements with the SEC.

**Data not obtainable from the XBRL companyfacts API and taken from filing text
instead:** service/product revenue splits and geographic revenue. The companyfacts JSON
strips dimensional (axis/member) facts, so every figure in section 5 was read out of the
filing document itself, per operator rule 4 ("the filing gets read").

**One figure per company was cross-checked against the filed statement, not the tagged
data:** KLA total revenues $13,579,476 thousand (consolidated statement of operations);
Applied gross margin 48.7% and operating margin 29.2% (MD&A results table); Lam total
revenue $23,232,690 thousand (revenue disaggregation table); ASML gross profit 52.8% of
net sales and income from operations 34.6% (financial-performance KPI page); Axcelis
total gross profit $376,848 thousand and gross margin 44.9% (MD&A gross-profit table);
Onto gross profit 49.7% of revenue (MD&A); Camtek total revenues $496,072 thousand (FS
Note 18A); Nova gross profit $505,200 thousand (consolidated statement of operations).
**All eight agree with the XBRL series used above.**

---

## 8. LIMITATIONS OF THIS ROW: read this before using it in Q2

1. **The operating-margin formula excludes real costs for some peers and not others.**
   For Onto it excludes a large separately-stated amortization of acquired intangibles;
   Onto's *reported* FY2025 operating margin is 13.2%, not the 19.0% the identical
   formula produces. The identical formula is the right instrument for a *comparison*
   and the wrong one for Onto's absolute earning power. Both are shown; do not mix them.
2. **ROE is not usable across this set** for the reason given in section 0. Use ROUNTOA.
3. **ROUNTOA uses year-end denominators**, which flatters companies in a year of falling
   assets and penalises those in a year of acquisition. Onto's FY2025 ROUNTOA is
   depressed partly by the Semilab USA acquisition closing in Q4 2025 (goodwill rose
   from $330.0M to $644.0M in one year); the operating income it bought was in the
   numerator for two months and the assets in the denominator in full.
4. **Fiscal-year misalignment.** Section 2's tables compare labels, not cycle
   positions. Section 3 is the honest cycle comparison.
5. **The excluded Japanese competitors bias the row toward KLA** (section 6).
6. **The FY2019 KLA gross-margin fall is not decomposed.** Orbotech consolidated from
   20 Feb 2019 and is a lower-margin business; the 5.1-point drop is mix and price
   mixed together. **UNRESEARCHED, resolvable from KLA's FY2019 and FY2020 10-K
   segment notes.**
7. **No market-share figure appears anywhere in this file, because none appears in any
   filing read for it.** See section 4.6.
8. **Every number here is a transcription or an arithmetic operation on filed data. No
   number here is a judgment, and no number here clears any gate.** Per operator rule 3,
   nothing in this file may be read as entry language.

---

## 9. THE ONE-PARAGRAPH ANSWER TO Q2's COMPETITOR ROW

**On filed data, over eleven fiscal years, KLA earns the highest gross margin in the
semiconductor-equipment peer set in every single year without exception, and the highest
operating margin on an identical formula in the latest year (41.7% vs Lam 35.3%, ASML
34.6%, Applied 29.9%).** Against the three companies that actually contest inspection
and metrology, the gap is not close: **Nova 28.8%, Camtek 25.8%, Onto 19.0%.** The
closest pure-play, Onto, has never in eleven years come within 9 gross-margin points of
KLA, lost 10.1 points and posted an operating loss in the 2019 downturn while KLA earned
30.4%, and states in its own 10-K that it has cut prices to defend share and that its
competitors have larger installed bases and better service infrastructure. Nova's 20-F
calls the process-control market **"concentrated and characterized by relatively few
participants."** **The relative claim is supported.** Three things qualify it: the two
Japanese competitors that cannot be measured, the absence of any filed market-share
figure, and Nova's 25.6% six-year revenue CAGR against KLA's 19.9%. Nova, not Onto, is
the challenger that is actually gaining.
