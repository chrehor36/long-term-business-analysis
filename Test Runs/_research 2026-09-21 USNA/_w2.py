import io
p="Test Runs/2026-09-21 Run - USNA USANA Health Sciences.md"
s=io.open(p,encoding="utf-8").read()
q2 = """## Q2 - IS IT A FRANCHISE? **[E3-03]**

**The three conditions, scored against the filing.**

| [E3-03] condition | verdict | evidence |
|---|---|---|
| (1) needed or desired | **passes** | 387,000 people bought in the last three months of FY2025; product returns are 0.8% of net sales (10-K) |
| (2) thought by its customers to have **no close substitute** | **FAILS** | the company's own words, below |
| (3) not subject to price regulation | **passes** | prices are set by the company; regulation here is of claims, labelling and the selling method, not price |

**Condition (2) fails on the registrant's own sentence.** From Item 1, "Competition", 10-K
accession `0000896264-26-000021`:

> "Our business through USANA, Hiya, and Rise is **very competitive and the barriers to entry
> are not significant.** We compete with manufacturers, distributors, and retailers of
> nutritional products in many channels, including global direct selling, direct-to-consumer,
> specialty retail stores, wholesale stores, e-commerce businesses such as Amazon, and the
> internet generally. We also compete with other public and privately owned direct sellers for
> distributor talent, including for example Amway, Herbalife, and Nu Skin. On both fronts,
> compared to USANA, Hiya, and Rise, **many of our competitors are significantly larger, have a
> longer operating history, higher visibility and name recognition, and greater financial
> resources.**"

That is a company telling its owners it has no moat, in the section of the annual report set
aside for saying so. **[E3-03]** requires all three conditions; one of them is denied by the
subject.

**And [E3-03]'s own demonstration test fails in both halves.** The row says the existence of the
three conditions *"will be demonstrated by a company's ability to **regularly price its product
or service aggressively and thereby to earn high rates of return on capital**."*

- **Pricing.** USANA did raise prices in FY2025 - the 10-K attributes part of the core gross-margin
  improvement to *"price increases"*, and average spend per active Customer rose **4.4%**. In the
  same year **active Customers fell 14.8%**. Under **[E2-44]**'s first characteristic - the ability
  to raise prices *"without fear of significant loss of either market share or unit volume"* - this
  is a fail, and it is the fail in its most legible form.
- **Returns on capital.** Computed from the filed series (see Q3's [E2-01] table): return on
  equity ran **28-33% every year from FY2010 to FY2021**, then **16.0% / 12.8% / 7.9% / 2.0%**.
  Operating margin ran **15.6% (FY2020) to 4.0% (FY2025)**. High returns were real and they are gone.

**[E4-55] - where units exist, monitor units. They exist here, the company publishes them, and
they are the whole story.** Munger's Precision Steel row is the template: *"In 2006, Precision
Steel's service center volume was 46 million pounds, down from 69 million pounds sold as recently
as 1999. This decline in physical volume is a serious reverse, not likely to disappear in some
'bounce back' effect. Nor do we expect another sharp rise in prices like the approximately 40%
rise that recently occurred, holding dollar volume roughly level despite a precipitous drop in
physical volume."*

**USANA's physical series, each figure read from the 10-K of that year:**

| fiscal year end | active Customers | source |
|---|---|---|
| 2016-12-31 | 471,000 *(then called "active Associates")* | 10-K FY2016 |
| 2017-12-30 | 565,000 | 10-K FY2017 |
| **2018-12-29** | **616,000 - the peak** | 10-K FY2018 |
| 2019-12-28 | 586,000 | 10-K FY2019 |
| 2021-01-02 | 599,000 | 10-K FY2020 |
| 2022-01-01 | 560,000 | 10-K FY2021 |
| 2022-12-31 | 490,000 | 10-K FY2022 |
| 2023-12-30 | 483,000 | 10-K FY2023 |
| 2024-12-28 | 454,000 | 10-K FY2025 comparative table |
| **2026-01-03** | **387,000** | 10-K FY2025, acc. `0000896264-26-000021` |
| 2026-07-04 | **384,000** | 10-Q, acc. `0000896264-26-000056` |

**616,000 to 387,000 is minus 37% in seven years**, and the decline is in every region without
exception: Greater China (15.4%), Southeast Asia Pacific (18.2%), North Asia (7.9%), Americas and
Europe (12.9%) in FY2025 alone. The 10-K's own forward-looking-statements list concedes it in the
first bullet: *"our core business ... has declined in net sales, net income and active Customers
over the last few years."* The consolidated **net sales line rose 8.3% in FY2025** - and it rose
only because $130.0 million of purchased Hiya revenue was added. **Dollar revenue flattered by an
acquisition and by price is precisely how [E4-55] says a shrinking franchise hides.**

---
### THE COMPETITOR ROW - required [E3-28]

**Specification, stated before the row was built:** every listed company whose primary business is
selling nutrition, wellness or weight-management product through a commissioned distributor or
coach network, measured on **(a) net sales and (b) operating margin, from its own
SEC-filed annual accounts, on the same calendar-year window FY2018-FY2025**, newest vintage. Source
for every cell: that company's own `companyfacts` US-GAAP annual facts drawn from its 10-K filings,
cross-read against the newest 10-K text for HLF, NUS, MED and NHTC.

**Net sales, $ millions, from each company's own 10-K:**

| Company | FY2018 | FY2021 | FY2023 | FY2025 | peak-to-FY2025 |
|---|---|---|---|---|---|
| **USANA (consolidated)** | 1,189.2 | 1,186.5 | 921.0 | **925.3** *(incl. $132.0 bought Hiya)* | **-22%** |
| **USANA (core nutritional only)** | 1,189.2 | ~1,186 | ~921 | **775.5** | **-35%** |
| Herbalife (HLF) | 4,891.8 | 5,802.8 | 5,062.4 | 5,037.5 | -13% |
| Nu Skin (NUS) | 2,679.0 | 2,695.7 | 1,969.1 | 1,485.2 | **-45%** |
| Medifast (MED) | 501.0 | 1,526.1 | 1,072.1 | 385.8 | **-76%** |
| Natural Health Trends (NHTC) | 191.9 | 60.0 | 43.9 | 39.8 | **-79%** |
| Mannatech (MTEX) | 173.6 | 159.8 | 132.0 | 108.0 | **-38%** |
| LifeVantage (LFVN, June FY) | 203.2 | 220.2 | 213.4 | 182.6 *(FY2026)* | **-21%** |
| BODi / Beachbody (BODI) | - | 873.6 | 527.1 | 251.7 | **-71%** |

**Operating margin, same source, same window:**

| Company | FY2018 | FY2021 | FY2023 | FY2025 |
|---|---|---|---|---|
| **USANA** | **15.8%** | **14.3%** | 10.1% | **4.0%** |
| Herbalife | 14.0% | 12.7% | 7.0% | 9.5% |
| Nu Skin | 9.0% | 8.7% | 2.5% | 4.4% |
| Medifast | 13.8% | 14.2% | 11.8% | **-3.7%** |
| Natural Health Trends | 17.6% | 2.6% | -3.8% | **-4.5%** |
| Mannatech | -0.1% | 5.7% | -0.7% | **-0.4%** |
| LifeVantage | 5.1% | 8.0% | 2.0% | 3.3% *(FY2026)* |
| BODi | - | -34.0% | -26.7% | 2.2% |

**Peers named: 7, from an industry with roughly a dozen participants of scale, of which the three
largest by revenue - Amway, Mary Kay and Melaleuca - are private and file nothing.** Buffett asks
for eight **[E3-28]**; seven were taken because seven is every listed one I could find that meets
the specification. **Three of the largest participants are unavailable**, which under the template
would normally hold the moat class PROVISIONAL and make the verdict UNRESEARCHED. **It does not
here, and the reason must be stated plainly: the missing companies could only make the case
worse.** Amway and Mary Kay are the named larger competitors in USANA's own Competition paragraph;
their absence removes evidence of *competitive pressure*, never evidence of a moat. A row that is
unanimous across seven filers, and whose three missing members are the ones cited against the
subject by the subject, does not become provisional by their absence. **The verdict below does not
rest on the row alone in any case** - it rests on [E3-03] condition (2) being denied in the
registrant's own words.

**What the row shows, and its limit [E3-61].** Seven of seven listed participants are smaller in
FY2025 than at their peak in the window; five of seven are down more than a third; three of seven
lost money at the operating line in FY2025. The unit series says the same at the peers, from their
own filings: Nu Skin's FY2025 10-K - *"Customers decreased 10%, Paid Affiliates decreased 11% and
Sales Leaders decreased 19% compared to the prior year"*; Natural Health Trends' - *"We had 14%
fewer active members at December 31, 2025 as compared to the end of 2024, and 5% fewer active
members at the end of 2024 as compared to the end of 2023 ... These losses in the number of active
members were a significant factor contributing to the decrease in our recent year-over-year
sales"*; Medifast's - *"The year-over-year decline in revenue was primarily driven by a decrease in
the number of active earning coaches."* **[E3-61]** caps what the row can prove - it shows position,
never conduct, and *"you'd have to know the people involved"* - so the row is used here for what it
can carry: **USANA's decline is not an execution failure peculiar to USANA.** That matters in
exactly one direction, and it is the wrong one for the owner: a franchise is a *relative* claim,
and being no worse than an industry that is collectively shrinking is the absence of a moat, not
the presence of one.

**USANA was the best operator in the row and that is now spent.** In FY2018 its 15.8% operating
margin led every listed peer. In FY2025 its 4.0% sits below Herbalife's 9.5% and barely above Nu
Skin's 4.4%. **[E4-32]** asks for the direction - *"we want the moat widened every year ... that
does not necessarily mean that the profit is more this year than last year"* - and the direction
here is negative on every filed measure the framework asks for: units, margin, return on capital,
and relative position within the row.

---
### THE REST OF THE Q2 TESTS

- **[E5-23] / [E4-04] - is the moat rebuilt or defended?** The question does not reach the ruling,
  because there is no moat to classify. For the record of the attempt: the distributor network must
  be *replaced*, not merely defended - the 10-K says *"we experience a high turnover among new
  active Customers from year to year"*, and the company spent FY2025 rolling out an *"enhanced Brand
  Partner Compensation Plan"* to re-buy the network's loyalty, which is the paying-for-a-replacement
  case, not the defending-the-same-trademark case. Recorded, not relied on.
- **[E4-36] - which of the four causes of extreme success produced the record?** USANA's 2010-2021
  record of 28-33% returns on equity was real. Read against [E4-36]'s list it is the fourth kind -
  *"Catching and riding some sort of big wave"* - and **[E3-51]** names what happens next: *"when a
  surfer gets up and catches the wave and just stays there, he can go a long, long time. But if he
  gets off the wave, he becomes mired in shallows."* The wave was the two-decade expansion of
  network-marketed supplements, most of all in China. **The competitor row is the evidence that it
  is the wave and not the surfer**, because all seven surfers came off it within the same four years.
  A surfing run is not a moat; the advantage lived in the wave.
- **[E2-45] - the attacker's test.** With ample capital and skilled personnel, competing with USANA
  requires: a contract manufacturer (USANA itself uses third parties for 44% of product sales), a
  commission schedule more generous than 43%, and a website. The company states the barrier itself
  and states that it is *"not significant"*. Compare *"I'd rather wrestle grizzlies than compete
  with Mrs. B and her progeny"* - this is the opposite pole.
- **[E3-33] / [E5-28] - untapped pricing power?** No. The pricing power was tapped in FY2025 and the
  customer count fell 14.8% in the same year. **[E5-28]** scopes the class - *"If you name some
  business that has incredible pricing power, you're talking about a business that's a monopoly or
  a near monopoly"* - and a company that names Amway, Herbalife and Nu Skin as larger rivals in its
  own Competition paragraph is not claiming near-monopoly. **[E4-37]**'s inverse metric points the
  same way: the measure of a business is *"the agony they go through in determining whether a price
  increase can be sustained"*, and the filed evidence of the agony is the simultaneous compensation-plan
  rebuild, the Q4 FY2025 cost realignment and the 14.8% unit loss.
- **[E2-53] - the dominance class?** Not applicable. USANA is not dominant in any channel it names;
  it is, by its own account, smaller than several rivals in the one channel it was built for.
- **[E3-46] - the second question, and it is a number.** *"the best businesses, by definition, are
  going to be businesses that earn very high returns on capital employed over time."* Over the last
  four filed years: 16.0%, 12.8%, 7.9%, 2.0% on equity. Not this one, not now.
- **[E3-43] - so what class is it?** *"'a business' earns exceptional profits only if it is the
  low-cost operator or if supply of its product or service is tight."* Supply of nutritional
  supplements is not tight. USANA is not the low-cost operator - it manufactures in Utah and pays
  43% of core revenue in commissions, against competitors with *"greater financial resources"*. It
  is **"a business"** in [E3-43]'s sense, and the row's last sentence is the one that binds:
  *"a business, unlike a franchise, can be killed by poor management."*

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL - Direction: **narrowing on every filed
  measure - units, margin, return on capital, and rank within the competitor row**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**Why OUT and not UNKNOWABLE.** The [E4-04] ruling of 2026-09-20 sends to **UNKNOWABLE at Q2** a
name that *passes* [E3-03] and whose durability cannot be judged from filings - the perimeter
close. **This name does not pass [E3-03].** Condition (2) is denied by the registrant in its own
Competition paragraph, and the row's demonstration test - aggressive pricing producing high
returns on capital - fails in both halves on filed figures. That is *"the evidence is here and the
business fails"*, which is the definition of OUT. **[E4-19]**'s separating question was asked
aloud: *can I name the document that would resolve this?* There is no document that would; the
documents are in, and they say what they say.

**STOP. Operator rule 2: the run closes here.** Q3 through Q6 below are **RECORDED, NOT
GOVERNING** - no verdict box is ticked in any of them, and nothing in them may be read as a
verdict about this company.

---
"""
a=s.index("## Q2 — IS IT A FRANCHISE?")
b=s.index("## Q3 — ARE THEY HONEST")
s=s[:a]+q2+s[b:]
io.open(p,"w",encoding="utf-8").write(s)
print("OK",len(s))
