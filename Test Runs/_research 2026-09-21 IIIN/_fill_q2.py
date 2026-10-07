import io
p = "Test Runs/2026-09-21 Run - IIIN Insteel Industries.md"
t = io.open(p, encoding='utf-8').read()
lines = t.split('\n')
i0 = next(i for i, l in enumerate(lines) if l.startswith('## Q2 — IS IT A FRANCHISE?'))
i1 = next(i for i, l in enumerate(lines) if l.startswith('## Q3 — ARE THEY HONEST'))
head = '\n'.join(lines[:i0])
rest = '\n'.join(lines[i1:])
new = r'''## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The definition, applied line by line.** *A franchise is a product or service that "(1) is
needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not
subject to price regulation."* **[E3-03]**

- **Needed or desired [x]** — yes, and without qualification. Reinforced concrete cannot be
  poured without it, and the products are written into building codes and into federal and state
  *"Buy America"* melt-and-cast rules (FY2025 10-K, Item 1).
- **No close substitute [ ] — THIS IS WHERE IT FAILS, AND IT FAILS ON THE COMPANY'S OWN
  WORDS.** Three separate statements in the FY2025 10-K, Item 1:
  1. *"Our markets are highly competitive based on price, quality and service."*
  2. Seven named makers of the identical products: *"Our primary competitors for WWR products
     are Wire Mesh Corporation, Concrete Reinforcements, Inc., National Wire Products, Davis
     Wire Corporation and Oklahoma Steel & Wire Co., Inc. Our primary competitors for PC strand
     are Sumiden Wire Products Corporation and Wire Mesh Corporation."* Plus imports:
     *"Import competition is also a significant factor in certain segments of the PC strand and
     SWWR markets that are not subject to 'Buy America' requirements."*
  3. **Its own flagship product is sold AS a substitute for something else** — ESM *"is an
     engineered made-to-order product that is used as the primary reinforcement for concrete
     elements or structures, frequently serving as a lower cost reinforcing solution than
     hot-rolled rebar."* A product whose sales pitch is that it undercuts the incumbent
     alternative is in a substitution relationship, and substitution runs both ways.
- **Not price-regulated [x]** — no rate regulation. But see the **[E2-59]** reading below: what
  Insteel has instead of a franchise is a *trade* regime, and that is the opposite case.

**One of three criteria fails, so [E3-03] is not satisfied. The rest of this question is the
work of establishing that the failure is the real thing and not a reading error.**

### The commodity doctrine, which is the class this business is in [E2-58]

> *"persistent over-capacity without administered prices (or costs) equals poor profitability"*,
> with long-term profitability set by *"the ratio of supply-tight to supply-ample years"*, and
> the one exception being *"a cost advantage that is both **wide and sustainable** … By
> definition such exceptions are few."* — **[E2-58]**

The 10-K puts the business inside that equation itself: *"The primary raw material used to
manufacture our products is hot-rolled carbon steel wire rod … can generally be characterized as
a commodity product"*, and *"Ultimately, the relative supply - demand balance in our markets and
competitive dynamics determine whether our margins expand or contract."*

**And the ratio of supply-tight to supply-ample years is on the record, published by the company
itself.** The 2026 proxy prints fifteen years of return on capital as calculated under its own
incentive plan (DEF 14A 2026-01-02, acc. 0001308179-26-000001):

| FY | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROC (ROCICP) | 5.1% | 1.4% | 7.7% | 10.4% | 11.1% | 23.1% | 12.5% | 16.6% | 1.8% | 9.7% | 36.9% | 47.6% | 9.1% | 6.3% | 14.1% |

Fifteen-year mean **14.2%**; **strip the two steel-spike years 2021-22 and the remaining thirteen
average 9.9%**, with three years under 2%. That is *"the ratio of supply-tight to supply-ample
years"* rendered as a table by the company's own compensation committee. **[E3-46]** asks the
second question about the business as a number — *"the best businesses, by definition, are going
to be businesses that earn very high returns on capital employed over time"* — and a
thirteen-year ex-spike mean near ten is not that.

### Is the exception present — a cost advantage both wide and sustainable?

**No, and the filing says why.** Insteel's stated strategy is *"operating as the lowest cost
producer in our industry"*, but the same Item 1 concedes the structural problem in one sentence:
*"Some of our competitors, such as Wire Mesh Corporation, Nucor Corporation and Oklahoma Steel
and Wire, are **vertically integrated companies that produce both wire rod and concrete
reinforcing products** and offer multiple product lines over broad geographic areas."*

**Wire rod is not a component of Insteel's cost — it is essentially the whole of it.** FY2025
cost of sales was **$554,268** thousand on net sales of **$647,706** thousand (filed Consolidated
Statements of Operations), **85.6% of sales**, and the MD&A attributes the year's entire margin
swing to *"higher spreads between average selling prices and raw material costs ($36.1
million)"*. **The competitors named above own the input that sets 85% of Insteel's costs;
Insteel buys it, 27% of it from abroad in FY2025.** That is the reverse of a wide and sustainable
cost advantage, and the competitor row below shows it has not produced one.

### THE COMPETITOR ROW — required [E3-28]

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing."* — **[E3-28]**

**Same metric, same window, filing-sourced.** Metric: **return on shareholders' equity, net
income ÷ year-end shareholders' equity**, computed identically for every row from each filer's
own 10-K facts, **FY2010 through FY2025, sixteen consecutive years**. Equity is the right
denominator here because none of these filers is an acquisition vehicle with a large goodwill
wedge and Insteel carries **no debt at all**, so its ROE is its return on capital employed with
no leverage flattering it — **the [E2-01] test run in the subject's favour.**

| Company | metric | window | 16-yr mean | min | max | source |
|---|---|---|---|---|---|---|
| **INSTEEL (IIIN)** | net income ÷ year-end equity | FY2010–FY2025 | **9.9%** | −0.3% (FY2011) | 32.1% (FY2022) | own 10-K facts, CIK 764401; FY2025 figures hand-checked against the filed statements above |
| Nucor (NUE) | same | FY2010–FY2025 | **14.6%** | 1.1% (2015) | 48.7% (2021) | Nucor 10-K facts, CIK 73309 |
| Steel Dynamics (STLD) | same | FY2010–FY2025 | **17.7%** | −5.4% (2015) | 51.0% (2021) | Steel Dynamics 10-K facts, CIK 1022671 |
| Commercial Metals (CMC) | same | FY2010–FY2025 | **8.9%** | −16.4% (FY2010) | 37.0% (FY2022) | Commercial Metals 10-K facts, CIK 22444 |

**The row is cross-checked against a peer's own words, not left on tagged data.** Nucor's FY2025
10-K (filed 2026-02-25, accession 0001193125-26-071575) states in its MD&A: *"Return on average
stockholders' equity was 8.5% and 9.8% in 2025 and 2024, respectively."* My identically
constructed figures are 8.3% and 10.0% — the gap is average-equity versus year-end-equity and
nothing else, so the row's construction reproduces a filer's own disclosure to within a fraction
of a point.

**Peers named: 7 of the 7 real competitors the subject's own filing names, plus 2 substitute
producers. Peers OBTAINABLE: 1 of the 7, and even that one unsegmented.**

| Named in Insteel's Item 1 | status | disclosed |
|---|---|---|
| Wire Mesh Corporation (WWR **and** PC strand — named in both lines, the only one that is) | private | **UNOBTAINABLE** — EDGAR company search returns *"No matching companies"* |
| Concrete Reinforcements, Inc. | private | **UNOBTAINABLE** — same search, no matching companies |
| National Wire Products | private | **UNOBTAINABLE** — same |
| Davis Wire Corporation | private (Heico Companies) | **UNOBTAINABLE** — neither name files |
| Oklahoma Steel & Wire Co., Inc. | private | **UNOBTAINABLE** — same |
| Sumiden Wire Products Corporation (PC strand) | foreign parent, unsegmented | **UNOBTAINABLE** — no SEC filer |
| Nucor Corporation | public, **unsegmented for wire/reinforcement** | in the row, at the company level only |
| *(substitute producers, not named by Insteel)* Steel Dynamics, Commercial Metals | public, unsegmented | in the row for the rebar substitute |

**This incompleteness is disclosed and it changes nothing about the verdict, for a reason worth
stating plainly.** The framework's rule is that an unavailable peer holds the **moat class
PROVISIONAL**, which is UNRESEARCHED — and that rule exists to stop a run **crediting** a moat it
has not checked against the field. **It does not license a run to withhold a negative finding
that rests on the subject's own filing.** Nothing a private competitor's accounts could show
would convert *"Our markets are highly competitive based on price, quality and service"* and a
product sold as the cheaper alternative to rebar into *"no close substitute"* **[E3-03]**. The
class recorded below is **NONE**, and the missing rows could only make it worse, never better.

**And the row's limit is stated [E3-61]:** identical structures produce opposite conduct — *"In
some businesses, the participants behave like a demented Kellogg. In other businesses, they
don't … **I think you'd have to know the people involved.**"* The row shows Insteel earning the
lowest sixteen-year return of the four, unlevered; it cannot show whether the private half of the
industry is disciplined or demented. On the filed evidence of FY2024 — below — it has been
behaving like the latter.

### The physical series, which is the honest one [E4-55]

> Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — *"a
> serious reverse, not likely to disappear in some 'bounce back' effect."* **[E4-55]**

**Insteel does not disclose tons.** The physical series exists only as year-over-year percentages
in each 10-K's MD&A, and that is a stated limit of the source, not a finding. Chained from the
filings:

| FY | shipments | average selling price | net sales | 10-K MD&A, verbatim |
|---|---|---|---|---|
| 2016 | **+2.6%** (+4.8% pro-forma 52 weeks) | −8.8% | −6.5% | *"as a 2.6% increase in shipments was offset by an 8.8% reduction in average selling prices"* |
| 2019 | **−7.1%** | +8.1% | +0.6% | *"an 8.1% increase in average selling prices partially offset by a 7.1% decrease in shipments"* |
| 2021 | **−0.6%** | +25.7% | +25.0% | *"a 25.7% increase in selling prices partially offset by a 0.6% decrease in shipments"* |
| 2022 | **−7.8%** | +51.9% | +40.0% | *"a 51.9% increase in selling prices partially offset by a 7.8% decrease in shipments"* |
| 2023 | **−5.3%** | −17.1% | −21.5% | *"a 17.1% decrease in selling prices along with a 5.3% decrease in shipments"* |
| 2024 | **~flat** | down | −18.5% | *"driven entirely by a decrease in average selling prices as shipments remained relatively flat"* |
| 2025 | **+14.8%** | +6.7% | +22.4% | *"a 14.8% increase in shipments and a 6.7% rise in average selling prices … primarily due to incremental volume generated from our acquisitions"* |

**Read it in that order and it is the Precision Steel shape exactly.** FY2022's headline is net
sales up 40%; the tons moved **down 7.8%**. Across FY2021–FY2024 the physical series runs −0.6%,
−7.8%, −5.3%, flat — **roughly thirteen per cent fewer tons over four years** — and the one
growth year, FY2025, is **bought**: the MD&A attributes it to *"incremental volume generated from
our acquisitions."* **Organic FY2025 tonnage is not separable from acquired tonnage in any filed
document**, which is recorded here as a limit rather than guessed at. **[E4-32]**'s direction test
— the moat *"widened every year"* being *"the primary criterion of a great business"* — returns
the wrong sign: the share is being purchased, not won.

### The pricing tests

- **[E2-44], the two-characteristic test — can it raise prices *"even when product demand is flat
  and capacity is not fully utilized"*? FAILS, on the filing.** FY2024: *"Net sales decreased
  18.5% … driven entirely by a decrease in average selling prices as shipments remained
  relatively flat. The decrease in average selling prices was driven by persistent competitive
  pricing pressures in our welded wire reinforcing markets, the impact of low-priced PC strand
  and a decline in raw material costs."* Flat demand, and price went **down**. The second half of
  [E2-44] — grow dollar volume *"with only minor additional investment of capital"* — also fails:
  FY2025's growth cost **$72.1 million of cash** for two competitors.
- **[E4-37], the inverse metric — the agony of a price increase.** The FY2025 10-K, Impact of
  Inflation: *"our ability to raise our selling prices depends on market conditions and
  competitive dynamics, and there may be periods during which we are unable to fully recover
  increases in our costs."* And the risk factors: *"we may be unable to fully recover increased
  rod costs during weaker market environments."* That is the agony end of the scale, in the
  company's own hedged language, and it is a permanent feature of the filings rather than a bad
  year's confession.
- **[E3-33] untapped pricing power — NOT PRESENT, and the scope rule [E5-28] is why the claim is
  not even attempted.** *"If you name some business that has incredible pricing power, you're
  talking about a business that's a monopoly or a near monopoly"* **[E5-28]**. Insteel is the
  largest producer in a market with six named direct rivals and live import competition. Claiming
  the [E3-33] class here would be claiming near-monopoly, and the competitor row refuses it.

### The trade regime — [E2-59], and this is the sharpest finding in the question

> *"administered pricing … pre-1970s insurers "could legally price their way to profitability
> even in the face of substantial over-capacity"* — but **the moat belongs to the regime**, and
> *"That day is gone"* is how it ends. **[E2-59]**

**The brief asked whether trade remedies are doing the work a moat is being credited with. They
are, and the 10-K says so four times in one paragraph** — the same clause after each petition:

> *"The DOC ruled in our favor and imposed anti-dumping duties ranging from 12% up to 119%,
> **which had the effect of limiting the participation of these countries in the domestic
> market**."* (2003, five countries)
> *"final countervailing duty margins ranging from 9% to 46% and anti-dumping margins ranging
> from 43% to 194%, **which had the effect of limiting the continued participation of Chinese
> producers in the domestic market**."* (2010)
> *"the DOC ruled in our favor and imposed anti-dumping duties ranging from 4% to 194%, **which
> had the effect of limiting the participation of these countries in the domestic market**."*
> (2020–21, fifteen countries)
> *"the DOC ruled in our favor and imposed final countervailing duty margins ranging from 23% to
> 110%, **which had the effect of limiting the continued participation of Mexican producers in
> the domestic market**."* (SWWR, 2021)

**Whatever floor exists under PC strand and standard welded wire pricing is administered, and
the administrator is the Department of Commerce, not Insteel.** [E2-59]'s rule then applies
without adjustment: regulation *floors* a commodity business, and the moat belongs to the regime.
The risk factors concede the dependence in terms: *"**Trade law enforcement is critical to our
ability to maintain our competitive position against foreign PC strand and SWWR producers**"*,
and *"Such actions may be costly and may not be successful."*

**And the regime is demonstrably porous, which is the strongest available evidence that it is not
a moat at all.** Duties had been in force against five countries since 2003, China since 2010 and
fifteen more since early 2021 — and FY2024's price decline is attributed in the MD&A to *"the
impact of low-priced PC strand"* imports, with shipments *"adversely impacted by weaker market
conditions, increasing volumes of PC strand imports"*. FY2019 is the same story with the tariff
running the other way: *"Shipments for the current year were unfavorably impacted by an increase
in low-priced import competition spurred by the Section 232 tariff on imported steel"* — **a
trade measure aimed at helping the industry raised Insteel's rod cost and let finished imports in
underneath it.** A protection that has to be re-petitioned every decade and still lets the price
be set from abroad in the weak years is [E2-59]'s regime, not [E3-03]'s franchise.

### The remaining Q2 tests, each answered

- **[E2-53], the dominance class** — *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be. Good or bad, it will prosper."* **The
  inverse holds here.** Insteel *is* dominant by its own description — *"the nation's largest
  manufacturer of steel wire reinforcing products"* — and the marketplace still determines its
  economics completely: FY2024 return on capital of 6.3% and a 29%-of-target bonus, in the same
  plants, with the same position, as FY2022's 47.6%. **Dominance without pricing control is not
  the dominance class.**
- **[E2-45], the attacker's test** — *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* I would like it a great deal, and the filings say how: buy or
  build wire-drawing capacity near a metro market, buy rod on the same world market Insteel buys
  it on, and undercut. **Insteel has just demonstrated the entry cost: $72.1 million bought two
  going concerns with plants, equipment, customers and inventory, about 12.6% of its own market
  capitalisation.** A moat you can step over for a tenth of the incumbent's value is not a moat.
- **[E4-36], which of the four causes of extreme success** — the FY2021-22 result was
  **wave-riding**: a raw-material spike that lifted selling prices 25.7% and then 51.9% while
  **tons fell**. **[E3-51]**: *"when a surfer gets up and catches the wave and just stays there,
  he can go a long, long time. But if he gets off the wave, he becomes mired in shallows."* The
  wave broke in FY2023 and the 2024 return on capital was 6.3%. **The advantage lived in the
  wave, not in the surfer.**
- **[E4-04] is NOT the ground of this verdict, and that is deliberate.** Under the ruling of
  2026-09-20, [E4-04] is applied as a **competence limit**, never as a fourth franchise
  criterion, and a name that *passes* [E3-03] but whose durability cannot be judged closes
  UNKNOWABLE. **Insteel does not reach that door**: it fails [E3-03] criterion 2 on filed
  evidence, which is an OUT about the business, decided before [E4-04] is consulted. **Nor is
  [E4-23] used** — this business does not require a superstar; it requires a steel cycle.

- Primary moat metric, filing-sourced, and its trend: **gross margin, 17 years** — FY2009 −6.6%,
  then 8.5, 9.4, 6.2, 10.8, 11.9, 13.0, 20.4, 15.4, 15.6, 6.6, 11.8, 20.6, **23.9 (FY2022 peak)**,
  10.1, 9.4, **14.4 (FY2025)**. Computed from each year's filed gross profit and net sales.
  **Trend: none — a saw-tooth between 6% and 24% with no drift.** That is a spread business, and
  a spread is what a franchise does not have to live on.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: units shrinking, share
  purchased, spread set by the steel cycle and by the DOC.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

**⛔ THE FILE CLOSES HERE.** Q2 is OUT on the business: **[E3-03]** criterion 2 fails on the
subject's own Item 1, the business sits squarely in **[E2-58]**'s commodity class without its
*wide and sustainable* exception, and what floor exists belongs to the trade regime under
**[E2-59]**, not to the company. Per operator rule 2, **no verdict box is ticked below this
line**, and any arithmetic that follows is headed **COMPUTATION — NOT A CLEARANCE**.

*Notes for Q3 and Q4 are recorded beneath the close because the work was done before the verdict
was written and because it bears on the reversal condition at the end of the file. They carry no
verdicts.*

'''
io.open(p, 'w', encoding='utf-8').write(head + '\n' + new + rest)
print("ok")
