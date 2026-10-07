
---

## PAGP (Plains GP Holdings, L.P.) - run 2026-09-20 - Q1 IN, **Q2 OUT on the business**
**WAVE 7, NAME 1.** The first of the operator's three CSV lists. Register entry **133**. Price
**US$27.67** (2026-09-18, aggregator flagged) x **197,904,124 Class A shares** (10-Q cover,
`0001581990-26-000025`) = cap **US$5,476.0M**. Sovereign **5.34%**, 30-year US Treasury par
yield curve, 2026-09-18, struck from the issuing authority.

### The finding that governs everything else: the screen priced the wrong entity

PAGP sorted **first in the entire wave** because its screen `growth_required` read **-0.1381** -
the arithmetic said the price already cleared the floor with negative growth. **It does not,
and the reason is one tier down.**

`PAGP does not directly own any operating assets` (10-K FY2025, first paragraph). It owns an
**~85% limited partner interest in AAP**; AAP owns **233.0 million PAA common units, ~31% of
PAA's common and Series A preferred combined**. Look-through **~26%**. The filer states it three
more ways in the same document: FY2025 net income **$260M to PAGP against $1,426M to
noncontrolling interests (15.4%)**; partners' capital **$1,345M against $12,871M (9.5%)**;
distributions paid **$301M against $1,441M (17.3%)**.

**The screen's `oe_bottom_m 1318 / oe_top_m 1750` is the WHOLE consolidated group set against
197.9M Class A shares - one class of the top tier. An overstatement of roughly four times.**
This is the per-class denominator error of DASH, META, PATH, PUBM and BZFD **inverted**: there
the cover count was unreadable and the numerator was right; here the cover count is right and
the **numerator belongs to a wider entity**. **The general form worth carrying forward: a
consolidated numerator is only usable where noncontrolling interests are immaterial, and
`owner_earnings()` never reads the NCI lines.** Any multi-tier partnership, any
sponsor-and-MLP pair, any filer consolidating a JV it does not own outright, will price this
way. The tell is three lines long and sits in every 10-K: net income attributable to NCI,
noncontrolling interests in partners' capital, and distributions paid to noncontrolling
interests.

### Q1 IN. A taxed wrapper on about 198 million PAA common units

The filer names the design: **Economic Parity** - *"the number of our outstanding Class A shares
equals the number of AAP units we own, which in turn equals the number of PAA common units held
by AAP attributable to our ownership interest in AAP."* So one Class A share = one PAA common
unit of economics, **through an entity that "has elected to be taxed as a corporation for United
States federal income tax purposes"** and carries a $1,136M deferred tax asset.

Underneath, PAA is a crude-oil midstream business with two legs: **fee assets** (20,405 miles of
active pipeline, 76 million barrels of commercial storage, 9,680 kb/d of 2025 tariff volume,
largest in the Permian) and a **merchant book** that buys and sells physical crude - which is why
revenue is **$44,262M** and purchases are **$40,433M**. Operating income is **3.2% of revenue**.
Not simple; but every layer is stated and quantified in the filing, and [E3-31]'s test is whether
the analyst can *"realistically define what [he doesn't] know"*, not whether the chart is short.

### Q2 OUT. Two of three [E3-03] clauses fail in the filer's own words

**Clause (2), no close substitute - the filer writes [E2-58] itself:**
*"many of the areas where PAA operates have become overbuilt, resulting in an excess of midstream
energy infrastructure capacity"*, caused by *"relatively low barriers to entry"*, with rivals who
*"may be motivated to reduce transportation rates to levels approaching variable operating costs,
without regard to whether they are generating an acceptable return on their investment ... with
respect to certain of PAA's long-haul Permian pipelines."* Add *"pipelines may also face
competition from other forms of transportation, such as truck, rail and barge"* and *"existing
third-party owned pipelines with excess capacity in the vicinity of our operations also expose us
to significant competition."* **[E2-58]'s one exception is a cost advantage "both wide and
sustainable"; the competitor row shows PAA has the opposite.**

**Clause (3), not price-regulated - the filer quantifies it:** *"The majority of our pipeline
profits in the United States are based on rates that are either grandfathered in part or set by
agreement with one or more shippers. These rates remain regulated by FERC and are subject to
challenge or review and modification by FERC under the ICA."* The FERC index for July 2021-June
2026 was **revised down about 1% effective 1 March 2022**, vacated by the D.C. Circuit in July
2024, re-issued in September 2024 and is still under petitions whose *"final resolution ... could
have an adverse effect on our cash flows."* **[E2-59] exactly: the regime here is a CAP and not a
floor, and the corpus says neither creates the class.**

### The competitor row is the sharpest single artifact in this run

Ten peers, five years, one metric, every figure from the peer's own 10-K facts - **operating
income / (net PP&E + equity-method investments + net finite-lived intangibles)**, chosen because
[E3-46] makes the second question about a business a number and because margin-on-revenue is
meaningless across a set where some filers run $40bn of commodity gross through the top line and
others do not.

| | 5-yr mean FY2021-25 |
|---|---|
| **PAA / PAGP** | **5.6%** |
| HESM | 25.5% |
| MPLX | 20.1% |
| DKL | 14.5% |
| WES | 14.3% |
| EPD | 13.7% |
| TRGP | 11.8% |
| OKE | 11.6% |
| ET | 9.1% |
| KMI | 8.7% |
| GEL | 4.8% |

**Tenth of eleven. Peer median 13.7%. PAA's BEST year, 6.7%, is below every peer's five-year
mean except Genesis Energy's.** Enbridge named and excluded (40-F, IFRS, CAD). Limits stated:
EPD and ET tag no undimensioned `EquityMethodInvestments`, so their denominators are understated
and their returns flattered - correcting them moves EPD to ~12.9% and ET to ~8.8%, which does not
touch the conclusion. And [E3-61]'s limit stands: the row shows position, never conduct.

**[E4-55] on the units, and it is the whole story in two lines:** tariff volumes **8,934 -> 9,680
kb/d (+8%)**, Permian **6,731 -> 7,333 (+9%)**, while *"certain Permian long-haul contract rates
reset[] to market in 2025."* **Volume up, rate down, 5.6% on capital.** [E3-62]'s second step -
*"how much is going to stay home and how much is just going to flow through to the customer"* -
answers itself from the filer's own variance table. **That is the #11 PASS-THROUGH signature, and
it is recorded beneath the close rather than as a Q4 finding, because Q4 was never reached.**

### Priors the brief set, and what happened to each

| prior | outcome |
|---|---|
| **A. The structure may not be what the screen priced** | **CONFIRMED, and it is the run's governing finding.** Numerator ~4x too large. |
| **B. The working-capital flag names its year (2021 payables = 99% of OCF)** | **TRUE as arithmetic, REFUTED as a finding.** Payables released $1,970M; **receivables absorbed $2,179M**; net working capital was a **$227M DRAIN**. Operating cash before working capital is a stable $2.2-3.0bn across five years. |
| **C. Q2 has a regulated-price question with proportions owed** | **ANSWERED from the filing: the MAJORITY of US pipeline profit is FERC-regulated**, and the unregulated merchant leg sits in a market the filer calls overbuilt. |
| **D. Shapes #11, #5, #6, #28 to test at Q4** | **#11's signature is present and recorded; #5, #6 and #28 are UNTESTED**, because the file closed two gates early. No shape is named as this business's death. |
| **E. Q3 requires the latest 8-K EX-99.1; the industry's releases are built on a non-GAAP metric** | **CONFIRMED at full strength, recorded and NOT scored.** See below. |
| **F. Perimeter: `deal_note` says two Item 1.01s, no EX-2.1** | **THE `deal_note` WAS WRONG.** See below. |

### [E4-29] is constitutional at this filer - recorded, not scored, because Q3 was not run

*"Adjusted EBITDA"* appears **43 times** in the Q2 2026 earnings release (`0001581990-26-000023`,
2026-08-07), whose second headline bullet is *"Delivered strong second-quarter Adjusted EBITDA
attributable to PAA of $738 million."* It is not a stray usage:
- the filer's **own targeted credit profile** is written in it - *"a leverage multiple averaging
  between 3.25x to 3.75x, which is calculated as total debt plus 50% of the value of preferred
  units, divided by Adjusted EBITDA attributable to PAA"*;
- the **bank covenant** is written in it - *"Consolidated Funded Indebtedness to adjusted
  Consolidated EBITDA ... no greater than 5.00 to 1.00, which increases to 5.50 to 1.00 during an
  Acquisition Period"* (Revolving Credit Agreement of 2026-06-12, 8-K `0001104659-26-075189`);
- **D&A was $953M against $1,428M of operating income** - the excluded charge is two-thirds the
  size of the profit;
- and *"Adjusted Free Cash Flow"* of **$4,189M** for Q2 2026 against $348M a year earlier is
  mostly the **$3.9bn of divestiture proceeds**.

**[E2-54] is the corpus's answer to an EBITDA covenant** - *"a capital structure that does not
allow all interest, both payable and accrued, to be comfortably met out of current cash flow net
of ample capital expenditures"* - and it was not run here, because Q4 was not reached.

### The perimeter: four events the FY2025 statements do not carry, and a screen inference that missed the biggest

`deal_note` read *"2 8-K Item 1.01 filing(s) since 2026-02-27, none carrying a merger agreement
(EX-2.1) - most likely a credit facility or offering."* Opened, all of them:
1. **2026-05-12, `0001104659-26-059512`: the COMPLETED SALE of the Canadian NGL business to
   Keyera for ~CAD $5.328bn (~USD $3.883bn), ~$3.3bn net.** Its agreement exhibits are **EX-2.2,
   EX-2.3 and EX-2.4** - the three amendments - because the original SPA of 2025-06-17 was filed
   as EX-2.1 to the **Q2 2025 10-Q**. **A deal-perimeter test keyed to `EX-2.1` on the 8-K misses
   every transaction whose agreement was filed earlier and amended at closing.** This is the MRVL
   lesson in a new place.
2. **2026-09-14, `0001104659-26-107550`: $700M of 6.750% Series A and $800M of 7.000% Series B
   junior subordinated notes due 2056** - issued six days before this run, after the newest
   periodic filing, against a 30-year Treasury of 5.34%.
3. **The EPIC Crude / Cactus III purchase** (55% 2025-10-01, 45% effective 2025-11-01), most of
   FY2025's **$2,651M** of acquisition cash. **The company's own pro forma in that same 8-K takes
   FY2025 net income from continuing operations attributable to Class A shareholders from $152M
   to $135M, and from $0.77 to $0.68 per Class A share - dilutive on the filer's own arithmetic.**
   Recorded; **Q3 was not run and no capital-allocation verdict is written.**
4. **$484M of the FY2025 $2,931M operating cash is discontinued operations** - the Canadian NGL
   business, which no longer exists.

### One security fact - COMPUTATION, NOT A CLEARANCE

**PAGP closed at $27.67 and PAA at $25.37 on 2026-09-18.** By the filer's own Economic Parity
rule one Class A share carries the economics of one PAA common unit, so **PAGP trades at a 9.1%
premium to the identical claim one tier down**, and PAGP is the only one of the two that is a
corporate taxpayer. Recorded as a fact about two securities; no entry language, no Q5 output.

### Tooling and brief defects

1. **`working_capital_flag()` reads ONE line and never nets its matched counter-line.** On a
   commodity merchant, receivables and payables both scale with the commodity price, so the flag
   fires in every year the price moved and **names the wrong cause**. Here it named the year the
   cash was *drained* ($227M net use) as the year the cash was *made*. **Proposed fix, not made:
   where a filer tags both `IncreaseDecreaseInAccountsAndOtherReceivables` and
   `IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, report the NET working-capital cash
   effect beside the single line and refuse the "one line made the cash" string when the
   counter-line offsets more than half of it.** The likely reason they were never netted: **the
   two tags carry opposite cash-sign conventions** in the standard taxonomy (an increase in
   receivables is a use of cash; an increase in payables is a source).
2. **No guard reads noncontrolling interests.** `owner_earnings()` takes the consolidated
   operating-cash line whatever share of it belongs to the registrant's own shareholders. **This
   is a whole error class, not one name** - the three lines that detect it are in every 10-K and
   none is read. Any sponsor/MLP pair, multi-tier partnership or majority-owned-JV consolidator
   in the remaining 262 wave-7 names carries it.
3. **`PropertyPlantAndEquipmentNet` is not the tag this filer uses after FY2020.** PAGP and PAA
   report under
   `PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization`
   from FY2021. A capital-return screen keyed to the first tag returns **nothing** for this filer
   and drops it silently rather than refusing - the same shape as every other two-paths split
   this project has found.
4. **The `deal_note`'s EX-2.1 test, above.**
5. **The dispatch brief and `CLAUDE.md` both say the ledger is 267 rows. It is 286** (287 lines
   including the header), as `Screens/RESUME STATE ...` section 10 already records from the
   2026-09-20 audit. **Counted, not carried forward.** `CLAUDE.md`'s KEY FILES table still says
   267 and should be corrected by the operator, since the same table instructs the reader to
   *"Count the file, never the pointer."*
6. **A filer drafting artifact, flagged and not smoothed (PRIME RULE 1).** The 8-Ks of
   2026-09-14 and 2026-05-12 both describe PAA as *"a wholly owned subsidiary of Plains GP
   Holdings, L.P."* **PAA's common units trade on Nasdaq and AAP holds ~31% of them**; the press
   release attached to the same 8-K states it correctly. A reader relying on the 8-K body alone
   would compute exactly the error the screen made.

### What could not be resolved, and the document that would resolve it

- **PAGP's entity-level cash tax path.** It carries a **$1,136M deferred tax asset** and pays
  corporate tax on income a PAA unitholder receives untaxed at the entity. How fast that asset is
  consumed - and therefore what fraction of the PAA distribution actually reaches a Class A
  shareholder over a decade - is not computable from the documents read. *Resolved by:* Note 15
  (Income Taxes) of the FY2025 10-K read against the deferred-tax rollforward, plus the Section
  754 / basis discussion in the Class A share tax summary. **Not fetched: the file closed at Q2
  and no valuation was owed.**
- **The split of Crude Oil Segment Adjusted EBITDA between fee-based and merchant margin.** The
  10-K describes both legs and disaggregates neither. *Resolved by:* PAA investor-day materials
  or a supplemental disclosure; it is in none of the 10-K, the 10-Q or the 8-Ks read here. **It
  does not change Q2** - both legs fail [E3-03], the fee leg on clause (3) and the merchant leg
  on clause (2).
