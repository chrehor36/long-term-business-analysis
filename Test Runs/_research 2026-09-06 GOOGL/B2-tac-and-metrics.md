# B2 — TAC SPLIT AND THE MONETIZATION METRICS
## Alphabet Inc. (GOOGL) · CIK 0001652044 · research for a v4.1 run
Compiled 2026-09-06. Every fact below is **RUNG 1 (SEC filing)** unless explicitly marked
otherwise. Rung 1 = a filed 10-K or 10-Q, named by document, filing date and accession number,
with the figure read out of the filed HTML document (not from XBRL tagging, not from an
aggregator).

**Source set.** All thirteen 10-Ks FY2015–FY2025 plus seven 10-Qs (Q3-2017, Q1/Q2/Q3-2018,
Q1/Q2/Q3-2019) plus the 2026 Q1 and Q2 10-Qs were downloaded from
`https://www.sec.gov/Archives/edgar/data/1652044/…` and read as text. Filing dates and
accession numbers are from `data.sec.gov/submissions/CIK0001652044.json` and its
`-001` continuation file.

---

# PART 1 — THE TAC SPLIT: THE FULL FILED SERIES AND THE EXACT DATE OF ITS WITHDRAWAL

## 1.1 THE HEADLINE FINDING (corrects two earlier assumptions)

An earlier brief assumed the split stopped after FY2016. A prior agent corrected that to FY2018.
**Both are wrong.** The split ran one quarter further than the FY2018 10-K:

> **LAST periodic report filing the TAC split:**
> **10-Q for the quarterly period ended September 30, 2019**
> document `goog10-qq32019.htm` · **filed 2019-10-29** · accession **0001652044-19-000032**
>
> **FIRST periodic report omitting the TAC split:**
> **10-K for the fiscal year ended December 31, 2019**
> document `goog10-k2019.htm` · **filed 2020-02-04** · accession **0001652044-20-000008**
>
> **ELAPSED: 98 days.**

There is no intervening periodic report. Q3-2019 was the last 10-Q of calendar 2019; the FY2019
10-K is the very next 10-K/10-Q Alphabet filed. The withdrawal is therefore clean and
unambiguous — one filing had it, the next did not, 98 days apart, with nothing in between.

## 1.2 THE FULL FILED ANNUAL SPLIT SERIES

All figures $ millions. Each row is taken from the 10-K named in the "filed in" column. Where a
year appears in more than one 10-K as a comparative, the figures agree exactly except where
noted at §1.6.

| Year | TAC to distribution partners | Google properties TAC rate | TAC to Google Network Members | Network Members TAC rate | Total TAC | Aggregate TAC rate | filed in |
|---|---|---|---|---|---|---|---|
| 2013 | $2,965 | not filed | $9,293 | not filed | $12,258 | 24.0% | FY2015 10-K |
| 2014 | $3,633 | 8.1% | $9,864 | 67.8% | $13,497 | 22.6% | FY2015 & FY2016 10-K |
| 2015 | $4,101 | 7.8% | $10,242 | 68.1% | $14,343 | 21.3% | FY2015, FY2016, FY2017 10-K |
| 2016 | $5,894 | 9.2% | $10,899 | 69.9% | $16,793 | 21.2% | FY2016, FY2017, FY2018 10-K |
| 2017 | $9,031 | 11.6% | $12,641 | 71.9% | $21,672 | 22.7% | FY2017, FY2018 10-K |
| 2018 | $12,572 | 13.1% | $14,154 | 70.8% | $26,726 | 23.0% | FY2018 10-K |
| **2019 (9 mo.)** | **$10,856** | **13.3%** | **$10,732** | **68.9%** | **$21,588** | **22.2%** | **Q3-2019 10-Q — the last** |

Rate definitions, as Alphabet itself filed them (FY2017 10-K, `goog10-kq42017.htm`,
accession 0001652044-18-000007), verbatim row labels:

> "TAC to distribution partners as a percentage of Google properties revenues (1) (Google
> properties TAC rate)"
> "TAC to Google Network Members as a percentage of Google Network Members' properties
> revenues (1) (Network Members TAC rate)"
> "TAC as a percentage of advertising revenues (1) (Aggregate TAC rate)"
> "(1) Revenues include hedging gains(losses) which impact TAC rates."

Note the denominators are **not** the same. The distribution-partner rate is over **Google
properties (owned-and-operated) revenue**, not over total advertising revenue. The Network rate
is over **Network Members' properties revenue**. Only the aggregate rate is over total
advertising revenue. Any attempt to re-derive the split from the aggregate rate alone fails for
this reason.

### The quarterly detail from the final filing (Q3-2019 10-Q, accession 0001652044-19-000032)

Alphabet filed both a three-month and a nine-month column. Verbatim table, three months ended
September 30:

| | Q3 2018 | Q3 2019 |
|---|---|---|
| TAC to distribution partners | $3,155 | $3,856 |
| Google properties TAC rate | 13.1% | 13.5% |
| TAC to Google Network Members | $3,427 | $3,634 |
| Network Members TAC rate | 69.9% | 69.0% |
| TAC | $6,582 | $7,490 |
| Aggregate TAC rate | 22.7% | 22.1% |

## 1.3 WHAT THE SERIES WAS DOING WHEN IT WAS WITHDRAWN

This is the whole point of the dating. The two legs were moving in **opposite** directions, and
the aggregate rate — the only number that survived — was falling, which conceals it.

**The distribution-partner TAC rate was rising, and had risen in every single year filed:**

    7.8% (2015) → 9.2% (2016) → 11.6% (2017) → 13.1% (2018) → 13.3% (9M 2019)

That is a **+5.5 percentage-point** rise on the Google-owned-property leg over four years, on a
denominator that was itself compounding. In dollars, distribution-partner TAC went from $4,101M
(2015) to $12,572M (2018) — **3.07× in three years** — while Network TAC went from $10,242M to
$14,154M, only 1.38×. In 2015 distribution partners were 29% of total TAC; by 2018 they were
47%; by the 9M-2019 stub they were 50.3% and had crossed Network TAC for the first time.

**The Network Members TAC rate had turned over and was falling:**

    68.1% (2015) → 69.9% (2016) → 71.9% (2017) → 70.8% (2018) → 68.9% (9M 2019)

**And the aggregate rate was falling**, entirely on mix — Google properties revenue (low TAC
rate, ~13%) was growing faster than Network revenue (high TAC rate, ~69%), so the blend fell
even while the distribution-partner leg was deteriorating.

    21.3% (2015) → 21.2% (2016) → 22.7% (2017) → 23.0% (2018) → 22.2% (9M 2019)

**This is the structural fact the withdrawal removed from the filed record.** After FY2019 the
only rate Alphabet files is the aggregate — the one that is falling. The one that is rising, and
that measures the price of the default-placement contracts at issue in *US v. Google*, was
withdrawn.

### Alphabet's own MD&A explanation of the trend, verbatim, in the final filed years

**FY2018 10-K** (`goog10-kq42018.htm`, filed 2019-02-05, accession 0001652044-19-000004):

> "The increase in TAC to distribution partners from 2017 to 2018 was a result of an increase in
> Google properties revenues and the associated TAC rate. The increase in the Google properties
> TAC rate was driven by changes in partner agreements and the ongoing shift to mobile, which
> carries higher TAC because more mobile searches are channeled through paid access points. The
> increase in TAC to Google Network Members from 2017 to 2018 was a result of an increase in
> Google Network Members' properties revenues offset by a decrease in the associated TAC rate.
> The decrease in the Network Members TAC rate was primarily due to a shift to lower TAC products
> within programmatic advertising buying. The increase in the aggregate TAC rate from 2017 to
> 2018 was a result of an increase in Google properties TAC rate, partially offset by a favorable
> revenue mix shift from Google Network Members' properties to Google properties."

**FY2017 10-K** (`goog10-kq42017.htm`, filed 2018-02-06, accession 0001652044-18-000007):

> "The increase in the Google properties TAC rate was driven by changes in partner agreements and
> the ongoing shift to mobile, which carries higher TAC because more mobile searches are channeled
> through paid access points."

**Q3-2019 10-Q — the final filed discussion of the split** (`goog10-qq32019.htm`, filed
2019-10-29, accession 0001652044-19-000032), verbatim, all three paragraphs:

> "The increase in total TAC from the three and nine months ended September 30, 2018 to the three
> and nine months ended September 30, 2019 was primarily due to increases in TAC paid to
> distribution partners and TAC to Google Network Members. The decrease in the aggregate TAC rate
> was a result of the favorable revenue mix shift from Google Network Members' properties to
> Google properties.
>
> The increase in TAC to distribution partners from the three and nine months ended September 30,
> 2018 to the three and nine months ended September 30, 2019 was primarily due to an increase in
> Google properties revenues. The Google properties TAC rate increased due to the ongoing shift to
> mobile, which carries higher TAC because more mobile searches are channeled through paid access
> points, partially offset by an increase in YouTube advertising revenues where the associated
> content acquisition costs are included in other cost of revenues.
>
> The increase in TAC to Google Network Members from the three and nine months ended September 30,
> 2018 to the three and nine months ended September 30, 2019 was a result of an increase in Google
> Network Members' properties revenues offset by a decrease in the associated TAC rate primarily
> due to changes in product mix."

Read the phrase "changes in partner agreements" (FY2017 and FY2018) alongside criterion 3. That
is Alphabet's own filed language for *the Apple/Mozilla/carrier default deals repricing upward*.
It appears in the last two 10-Ks that carried the split and does not appear afterward.

## 1.4 IS ANY REASON FILED FOR DROPPING THE SPLIT?

**No.** Searched the FY2019 10-K in full for "no longer", for any change-in-presentation note
near the TAC discussion, and for any accounting-change or reclassification language attached to
cost of revenues. Result:

- **Zero occurrences of "no longer" anywhere in the FY2019 10-K.**
- No "change in presentation", "revised presentation" or "conform to current presentation"
  language attaches to the TAC table. (The generic "Certain amounts in prior periods have been
  reclassified to conform with current period presentation" boilerplate appears in the notes in
  most vintages but is not tied to TAC.)
- The FY2019 10-K simply presents a two-line table — TAC, Other cost of revenues — where the
  prior filing presented six lines, and says nothing about the change.

The disclosure was dropped **silently**. Note the contrast with the Apple precedent: Apple at
least framed its unit-disclosure withdrawal in an earnings call. Alphabet framed nothing; the
lines are simply absent from the next document.

## 1.5 WHAT SURVIVED THE WITHDRAWAL — THE DIRECTIONAL SHADOW

Alphabet did not stop *discussing* the two legs. It stopped *quantifying* them. Each 10-K
FY2019–FY2025 still contains an unquantified directional sentence. The full surviving series,
verbatim, with accessions:

**FY2019 10-K** (0001652044-20-000008, filed 2020-02-04):
> "The increase in TAC from 2018 to 2019 was due to increases in TAC paid to distribution partners
> and to Google Network Members, primarily driven by growth in revenues subject to TAC. The TAC
> rate decreased from 22.9% to 22.3%, primarily due to the favorable revenue mix shift from Google
> Network Members' properties to Google properties. **The TAC rate on Google properties revenues
> increased** primarily due to the ongoing shift to mobile, which carries higher TAC because more
> mobile searches are channeled through paid access points. The TAC rate on Google Network
> revenues decreased primarily due to changes in product mix to products that carry a lower TAC
> rate." *(emphasis added)*

**FY2020 10-K** (0001652044-21-000010, filed 2021-02-03):
> "The TAC rate was 22.3% in both 2019 and 2020. The TAC rate on Google properties revenues and the
> TAC rate on Google Network revenues were both substantially consistent from 2019 to 2020."

**FY2021 10-K** (0001652044-22-000019, filed 2022-02-02):
> "The TAC rate decreased from 22.3% to 21.8% from 2020 to 2021 primarily due to a revenue mix
> shift from Google Network properties to Google Search & other properties. The TAC rate on Google
> Search & other properties revenues and the TAC rate on Google Network revenues were both
> substantially consistent from 2020 to 2021."

**FY2022 10-K** (0001652044-23-000016, filed 2023-02-03):
> "The TAC rate was 22% in both 2021 and 2022. The TAC rate on Google Search & other revenues and
> the TAC rate on Google Network revenues were both substantially consistent from 2021 to 2022."

**FY2023 10-K** (0001652044-24-000022, filed 2024-01-31):
> "The increase in TAC from 2022 to 2023 was largely due to an increase in TAC paid to distribution
> partners, primarily driven by growth in revenues subject to TAC. The TAC rate decreased from
> 21.8% to 21.4% from 2022 to 2023 primarily due to a revenue mix shift from Google Network
> properties to Google Search & other properties. The TAC rate on Google Search & other revenues
> and the TAC rate on Google Network revenues were both substantially consistent from 2022 to 2023."

**FY2024 10-K** (0001652044-25-000014, filed 2025-02-05):
> "The increase in TAC from 2023 to 2024 was largely due to an increase in TAC paid to distribution
> partners, primarily driven by growth in revenues subject to TAC. The TAC rate decreased from
> 21.4% to 20.7% from 2023 to 2024 primarily due to a revenue mix shift from Google Network
> properties to Google Search & other properties. **The TAC rate on Google Search & other revenues
> increased from 2023 to 2024** primarily due to increases related to mobile searches, which
> carries higher TAC because more mobile searches are channeled through paid access points. The
> TAC rate on Google Network revenues was substantially consistent from 2023 to 2024."
> *(emphasis added)*

**FY2025 10-K** (0001652044-26-000018, filed 2026-02-05):
> "The increase in TAC from 2024 to 2025 was largely due to an increase in TAC paid to distribution
> partners, primarily driven by growth in revenues subject to TAC. The TAC rate decreased from
> 20.7% to 20.3% from 2024 to 2025, primarily due to a revenue mix shift from Google Network
> properties to Google Search & other properties. The TAC rates on Google Search & other and Google
> Network revenues were substantially consistent from 2024 to 2025."

### The current forward-looking TAC statement, verbatim

FY2025 10-K, "Trends in Our Business and Financial Effect" (accession 0001652044-26-000018):

> "**Traffic Acquisition Costs Growth and Rate Changes:** We expect traffic acquisition costs ('TAC')
> paid to our distribution partners and Google Network partners to increase as our advertising
> revenues grow. Our overall TAC as a percentage of our advertising revenues ('TAC rate') has been
> decreasing primarily due to a revenue mix shift from Google Network properties to Google Search &
> other properties. Our TAC rate will continue to be affected by changes in device mix; geographic
> mix; partner agreement terms; partner mix; the percentage of queries channeled through paid access
> points; product mix; the relative revenue growth rates of advertising revenues from different
> channels; and revenue share terms."

Alphabet is telling the reader, in the FY2025 10-K, that the falling aggregate TAC rate is a
**mix** effect — exactly the reading at §1.3. It expects distribution-partner TAC to keep rising.
It supplies no number for it.

**Reading of the shadow series.** Alphabet has said "the TAC rate on Google Search & other
revenues **increased**" twice since the withdrawal — FY2019 and FY2024 — and "substantially
consistent" in the other five years. It has never once, in seven years, said that rate *decreased*.
The direction of the withdrawn series is therefore *monotone non-decreasing on Alphabet's own
account*, but the magnitude is unobservable from the filings after 2019-10-29.

Also note the drift of the label itself: **"Google properties"** (FY2019, FY2020) becomes
**"Google Search & other"** (FY2021 onward). That is a narrowing — Google properties included
YouTube; Google Search & other excludes YouTube ads. The denominator of the shadow ratio changed
without a bridge.

## 1.6 AGGREGATE TAC SERIES FY2015–FY2025 — VERIFIED AND EXTENDED

The prior run's figures $50,886 / $54,900 / $59,926M for FY2023/24/25 are **CONFIRMED** against
the filed cost-of-revenues tables. Full series:

| FY | TAC ($M) | Google advertising revenue ($M) | derived TAC / ad rev | Alphabet's filed aggregate TAC rate | source accession |
|---|---|---|---|---|---|
| 2013 | 12,258 | — | — | 24.0% | 0001652044-16-000012 |
| 2014 | 13,497 | — | — | 22.6% | 0001652044-16-000012 |
| 2015 | 14,343 | — | — | 21.3% | 0001652044-16-000012 |
| 2016 | 16,793 | — | — | 21.2% | 0001652044-17-000008 |
| 2017 | 21,672 | — | — | 22.7% | 0001652044-18-000007 |
| 2018 | 26,726 | — | — | 23.0% *(restated to 22.9% in FY2019 10-K — see below)* | 0001652044-19-000004 |
| 2019 | 30,089 | 134,811 | 22.32% | 22.3% | 0001652044-20-000008 |
| 2020 | 32,778 | 146,924 | 22.31% | 22.3% | 0001652044-21-000010 |
| 2021 | 45,566 | 209,497 | 21.75% | 21.8% | 0001652044-22-000019 |
| 2022 | 48,955 | 224,473 | 21.81% | 22% *(FY2022 10-K rounds to whole %)* / 21.8% *(as restated in FY2023 10-K)* | 0001652044-23-000016 |
| 2023 | 50,886 | 237,855 | 21.39% | 21.4% | 0001652044-24-000022 |
| 2024 | 54,900 | 264,590 | 20.75% | 20.7% | 0001652044-25-000014 |
| 2025 | **59,926** | **294,691** | **20.34%** | **20.3%** | **0001652044-26-000018** |

**OPERATOR RULE 4 CROSS-CHECK — PASSED.** The FY2025 TAC figure of $59,926M was read out of the
MD&A cost-of-revenues table in `goog-20251231.htm` (accession 0001652044-26-000018). It is
cross-checked against the **audited Consolidated Statements of Income** in the same document:

    TAC 59,926 + Other cost of revenues 102,609 = 162,535
    Consolidated Statements of Income, "Cost of revenues", FY2025 = 162,535   ✓ exact

The audited statement also gives Revenues $402,836M, Income from operations $129,039M and Net
income $132,170M for FY2025, against which the MD&A figures reconcile. Sentinel check: the string
"Alphabet Inc." occurs 132 times in the FY2025 10-K text and 35 times in the Q2-2026 10-Q — both
documents are the correct registrant. Nothing in this file rests on XBRL tagging alone.

The derived ratio 59,926 / 294,691 = 20.34%
independently reproduces Alphabet's own filed 20.3%. The advertising-revenue denominators for
2023–2025 were read from **Note 2, Disaggregated Revenues**, in the FY2025 10-K
(Search & other 224,532 + YouTube ads 40,367 + Google Network 29,792 = Google advertising 294,691),
i.e. the audited statement, not the MD&A table.

**Two small restatement artifacts, flagged:**
1. The FY2018 10-K filed a 2018 aggregate TAC rate of **23.0%**. The FY2019 10-K narrates the
   same year as **22.9%**. A 0.1pp revision, immaterial, but recorded because it means the
   pre- and post-withdrawal series are not exactly splice-able.
2. The FY2022 10-K rounds all cost ratios to whole percents ("The TAC rate was 22% in both 2021
   and 2022"); the FY2023 10-K reverts to one decimal and restates 2022 as 21.8%. The whole-percent
   vintage is a one-year presentation change.

**The trend of the surviving aggregate: down, four years running** — 22.3% → 21.8% → 21.8% →
21.4% → 20.7% → 20.3%. This is the number that gets quoted. Per §1.3 it falls on mix, not on
price, and it is the *only* rate Alphabet now files.

## 1.6b RECONSTRUCTION OF THE WITHDRAWN LINE — **CONVENTION, NOT A FILED FACT**

> **LABEL: CONVENTION.** Everything in §1.6b is a *reconstruction*, not a rung-1 disclosure. It is
> arithmetic performed on filed inputs plus **one assumption Alphabet has not confirmed with a
> number**. It may not be reported as a filed figure, and it casts no vote in the run. It is
> included because the framework requires that when a question is closed as unobservable, the
> analyst state how wide the unobservable band is.
>
> **Rationale for admitting it:** Alphabet has told us, in every 10-K since FY2019, whether the
> Network TAC rate was "substantially consistent" or moved. That is a filed constraint on the one
> unknown. Bounding the unknown against that constraint is arithmetic on disclosed inputs, not a
> new number added to the model — it passes the tooling test in CLAUDE.md.

**Identity:** total TAC = (distribution-partner TAC) + (Network TAC), where
Network TAC = (Network TAC rate) × (Google Network revenue). Total TAC and Google Network revenue
are both filed every year. The Network TAC rate is the single unknown; Alphabet's MD&A calls it
"substantially consistent" in six of seven post-withdrawal years.

**Method validation (back-test).** Run the reconstruction on **2019**, the last year with a filed
observation, using the last filed Network rate of 68.9%:

    reconstructed 2019 distribution-partner TAC rate on Google properties revenue = 13.46%
    ACTUALLY FILED, 9M 2019 (Q3-2019 10-Q, 0001652044-19-000032)                  = 13.3%

The reconstruction reproduces the last observed value to within **0.16 percentage points**. That
is a genuine out-of-sample check, not a fitted result.

**Reconstructed series, three Network-rate assumptions.** All dollars $M. "rate/props" uses the
pre-2021 denominator (Search & other + YouTube ads); "rate/S&o" uses the post-2021 denominator
(Search & other only).

| Year | Total TAC (filed) | Network rev (filed) | **TAC to dist. partners (reconstructed)** | as % of total TAC | rate/props | rate/S&o |
|---|---|---|---|---|---|---|
| **Central case — Network rate held at the last filed 68.9%** |
| 2019 | 30,089 | 21,547 | 15,243 | 50.7% | 13.46% | 15.54% |
| 2020 | 32,778 | 23,090 | 16,869 | 51.5% | 13.62% | 16.21% |
| 2021 | 45,566 | 31,701 | 23,724 | 52.1% | 13.34% | 15.93% |
| 2022 | 48,955 | 32,780 | 26,370 | 53.9% | 13.76% | 16.23% |
| 2023 | 50,886 | 31,312 | 29,312 | 57.6% | 14.19% | 16.75% |
| 2024 | 54,900 | 30,359 | 33,983 | 61.9% | 14.51% | 17.16% |
| **2025** | **59,926** | **29,792** | **≈39,400** | **65.7%** | **14.87%** | **17.55%** |

**Sensitivity — the conclusion does not depend on the assumption:**

| Network rate assumed | 2019 dist. TAC | 2025 dist. TAC | 2019 → 2025 rate/props | dist. share of TAC 2019 → 2025 |
|---|---|---|---|---|
| 65.0% | 16,083 | 40,561 | 14.20% → **15.31%** | 53.5% → **67.7%** |
| **68.9% (last filed)** | **15,243** | **39,399** | **13.46% → 14.87%** | **50.7% → 65.7%** |
| 72.0% | 14,575 | 38,476 | 12.87% → **14.52%** | 48.4% → **64.2%** |

**Under every assumption tested, and by a wide margin:**
1. Distribution-partner TAC **rose monotonically in dollars, every single year**, roughly
   **2.5× from 2019 to 2025**, to somewhere near **$38–41 billion a year**.
2. Its **share of total TAC rose from about half to about two-thirds.**
3. Its **rate rose** — by 1.4 to 1.7 percentage points on the properties denominator, and by about
   2 points on the Search & other denominator.
4. Network TAC in dollars **peaked around 2022 and has fallen since**, because Network revenue has
   fallen three years running (32,780 → 31,312 → 30,359 → 29,792).

**Consistency check against the filed adjectives.** Alphabet said the Google-properties rate
"increased" in FY2019 and FY2024 and was "substantially consistent" elsewhere. The central-case
reconstruction shows +0.16pp (2019), +0.32pp (2024) and small moves in between — **consistent
with Alphabet's filed adjectives at every point.** The reconstruction is not in tension with any
filed statement.

**What this does and does not license.** It does **not** license reporting "$39.4 billion of
distribution-partner TAC in 2025" as a fact — that number is not filed and could be wrong by
several billion. What it licenses is the bounded statement: *the payments Google makes to keep its
default placements are, on the arithmetic of its own filed inputs, in the high-$30-billions
annually, they are around two-thirds of all TAC, and both the amount and the rate have risen every
year since the disclosure was withdrawn.* That is the shape of the number. The number itself
remains **UNKNOWABLE from the filings**.

## 1.7 THE 2026 10-Qs

Neither the Q1-2026 10-Q (`goog-20260331.htm`, filed 2026-04-30, accession 0001652044-26-000048)
nor the Q2-2026 10-Q (`goog-20260630.htm`, filed 2026-07-23, accession 0001652044-26-000071)
restores the split. Zero occurrences of "TAC to distribution partners" or "TAC to Google Network"
in either. The withdrawal has now stood for **six years and ten months** (2019-10-29 to the most
recent filing).

## 1.8 THE DATING VERDICT (Apple-precedent form)

| | |
|---|---|
| Series | TAC split: distribution partners vs Google Network Members, in $ and in separate rates |
| First filed | FY2015 10-K, 2016-02-11, 0001652044-16-000012 (dollar split; separate rates first filed in FY2016 10-K, 2017-02-03, 0001652044-17-000008) |
| **Last filed** | **Q3-2019 10-Q · `goog10-qq32019.htm` · 2019-10-29 · 0001652044-19-000032** |
| **First omitted** | **FY2019 10-K · `goog10-k2019.htm` · 2020-02-04 · 0001652044-20-000008** |
| **Days between** | **98** |
| Filed reason | **NONE.** Zero "no longer" language; no presentation-change note attached to the TAC table |
| What the series was doing | Distribution-partner rate **rising every year filed**, 7.8% → 13.3%; distribution-partner TAC **3.07× in three years**; the leg **crossed 50% of total TAC** in the final filed stub. Network rate had peaked (71.9% in 2017) and was falling |
| What replaced it | Aggregate TAC rate only — a number that **falls** on mix while the withdrawn leg rises — plus an unquantified adjective ("increased" / "substantially consistent") |
| Analytic consequence | The price of the Apple/Mozilla/carrier default contracts — the exact thing at issue in *US v. Google* — has been **unobservable on the filing rung since 2019-10-29** |

---

# PART 2 — PAID CLICKS AND COST-PER-CLICK: THE PHYSICAL SERIES

## 2.1 HEADLINE FINDING — **STILL FILED**

Contrary to the pattern of Part 1, **paid clicks and cost-per-click were NOT withdrawn.** They
appear in the FY2025 10-K and in both 2026 10-Qs, on the filing rung, in MD&A.

- **FY2025 10-K**, `goog-20251231.htm`, filed 2026-02-05, accession **0001652044-26-000018** —
  "Monetization Metrics" table present.
- **Q1-2026 10-Q**, `goog-20260331.htm`, filed 2026-04-30, accession **0001652044-26-000048** —
  present.
- **Q2-2026 10-Q**, `goog-20260630.htm`, filed 2026-07-23, accession **0001652044-26-000071** —
  present, with both three-month and six-month columns.

**However — a real withdrawal did occur inside this family, one vintage earlier and one level
down.** See §2.3. The *aggregate* metric and the *Network paid-click* metric were both dropped in
2018. What survives is the narrowest of the four series Alphabet used to file.

## 2.2 THE FULL FILED SERIES

Alphabet has filed up to **six** monetization series at once. They are not all the same series
across time; the presentation changed twice. Reading them as one continuous line is an error.

### Vintage A — FY2015 through FY2017 10-Ks: aggregate + a two-way split, all in clicks

| Year | Aggregate paid clicks Δ | Aggregate CPC Δ | Google properties paid clicks Δ | Google properties CPC Δ | Network paid clicks Δ | Network CPC Δ |
|---|---|---|---|---|---|---|
| 2013 | — | — | — | — | — | — |
| 2014 | 20% | (5)% | 29% | (7)% | 2% | (6)% |
| 2015 | 22% | (11)% | 33% | (15)% | (7)% | (3)% |
| 2016 | 32% | (11)% | 43% *(as refiled)* | (13)% | 3% | (13)% |
| 2017 | 46% | (19)% | 54% | (21)% | 10% | (9)% |

Sources: FY2015 10-K (0001652044-16-000012) for 2014/2015; FY2016 10-K (0001652044-17-000008)
for 2015/2016; FY2017 10-K (0001652044-18-000007) for 2016/2017. Note the FY2017 10-K restated
the 2016 aggregate paid-clicks change from 32% to 34% and the 2016 Google-properties change from
40% to 43%, disclosing the reason (see §2.5 on the Q1-2017 methodology refinement).

### Vintage B — FY2018 through FY2020 10-Ks: Google properties clicks; Network switched to impressions; aggregate dropped

| Year | Paid clicks Δ (Google properties) | CPC Δ | Impressions Δ (Network) | Cost-per-impression Δ |
|---|---|---|---|---|
| 2017 | 54% | (21)% | filed | filed |
| 2018 | 62% | (25)% | filed | filed |
| 2019 | 23% | (7)% *(FY2019 10-K table)* / (6)% *(as restated in FY2020 10-K)* | filed | filed |
| 2020 | 19% | (10)% | 15% | (8)% |

Sources: FY2018 10-K (0001652044-19-000004); FY2019 10-K (0001652044-20-000008); FY2020 10-K
(0001652044-21-000010). Note the 2019 CPC change is filed as **(7)%** in the FY2019 10-K and as
**(6)%** in the FY2020 10-K — a one-point restatement with no explanation, flagged.

### Vintage C — FY2021 onward: a single year's change, no comparatives

| Period | Paid clicks Δ | CPC Δ | Impressions Δ | Cost-per-impression Δ | accession |
|---|---|---|---|---|---|
| FY2021 | 23% | **15%** | 2% | 35% | 0001652044-22-000019 |
| FY2022 | 10% | (1)% | 3% | 1% | 0001652044-23-000016 |
| FY2023 | 7% | 1% | (5)% | 0% | 0001652044-24-000022 |
| FY2024 | 5% | 7% | (11)% | 10% | 0001652044-25-000014 |
| **FY2025** | **6%** | **7%** | **(7)%** | **7%** | **0001652044-26-000018** |
| Q1-2026 (3 mo.) | **13%** | **5%** | **(9)%** | **6%** | 0001652044-26-000048 |
| Q2-2026 (3 mo.) | **13%** | **3%** | **(12)%** | **13%** | 0001652044-26-000071 |
| Q2-2026 (6 mo.) | 13% | 4% | (10)% | 10% | 0001652044-26-000071 |

**Vintage C files only ONE column.** From FY2021 onward the 10-K table has a single period; the
prior year's change is not repeated for comparison. Rebuilding the series requires holding all
five 10-Ks at once, which is a real cost even though nothing was formally withdrawn.

## 2.3 THE WITHDRAWAL THAT DID HAPPEN — the aggregate and the Network paid click

Dated to the same standard as Part 1:

> **Series withdrawn:** "Aggregate paid clicks change", "Aggregate cost-per-click change", and
> the Google Network Members' **paid clicks / cost-per-click** rows.
>
> **LAST periodic report filing them:**
> **10-K for the fiscal year ended December 31, 2017**
> `goog10-kq42017.htm` · **filed 2018-02-06** · accession **0001652044-18-000007**
>
> **FIRST periodic report omitting them:**
> **10-Q for the quarterly period ended March 31, 2018**
> `goog10-qq12018.htm` · **filed 2018-04-24** · accession **0001652044-18-000016**
>
> **ELAPSED: 77 days.**

Verified: the Q3-2017 10-Q (0001652044-17-000042, filed 2017-10-27) still contains "Aggregate paid
clicks change" and "Aggregate cost-per-click change" rows; the Q1-2018 10-Q contains neither —
only "Paid clicks change", "Cost-per-click change" and "Impressions change". The FY2018 10-K
(0001652044-19-000004) confirms the change is permanent.

**What the withdrawn series was doing.** The Network paid-click series was the ugly one:

    Network paid clicks Δ:  +2% (2014) → (7)% (2015) → +3% (2016) → +10% (2017)
    Network CPC Δ:          (6)% (2014) → (3)% (2015) → (13)% (2016) → (9)% (2017)

**Network cost-per-click was negative in every one of the four years Alphabet filed it.** Replacing
paid clicks with impressions on the Network leg reset that streak to zero at the moment of the
switch. The aggregate CPC was likewise negative in all four filed years — (5)%, (11)%, (11)%,
(19)% — deteriorating monotonically in the final three. The aggregate series was disclosing a
worsening decline right up to the filing in which it disappeared.

## 2.4 WAS COST-PER-CLICK NEGATIVE, AND FOR HOW MANY CONSECUTIVE PERIODS?

**Yes — for eight consecutive filed annual periods, and then it turned.** The surviving
Google-properties / Google Search & other CPC change:

    2014 (7)% · 2015 (15)% · 2016 (13)% · 2017 (21)% · 2018 (25)% · 2019 (7)/(6)% · 2020 (10)%
    → 2021 +15% · 2022 (1)% · 2023 +1% · 2024 +7% · 2025 +7% · Q1-26 +5% · Q2-26 +3%

Seven consecutive negative annual prints 2014–2020 (2019 negative on both the original and the
restated figure), one positive spike in 2021, one final negative (2022), then four consecutive
positive years 2023–2025 plus both 2026 quarters. **CPC is currently positive and has been for
four straight years.** This is the opposite of the Apple-precedent pattern: the metric did not
go flat and then vanish; it went negative for seven years, was kept, and has since recovered.
That asymmetry is itself evidence — Alphabet keeps the series that is now improving and dropped
the two (Network CPC, aggregate CPC) that were not.

## 2.5 THE FINAL MD&A DISCUSSION, VERBATIM

**FY2025 10-K** (`goog-20251231.htm`, filed 2026-02-05, accession 0001652044-26-000018), the
entire Monetization Metrics discussion:

> "**Monetization Metrics**
>
> The following table presents changes in monetization metrics for Google Search & other revenues
> (paid clicks and cost-per-click) and Google Network revenues (impressions and
> cost-per-impression), expressed as a percentage, from 2024 to 2025:
>
> Google Search & other — Paid clicks change 6% — Cost-per-click change 7%
> Google Network — Impressions change (7)% — Cost-per-impression change 7%
>
> Changes in paid clicks and impressions are driven by a number of interrelated factors, including
> changes in advertiser spending; ongoing product and policy changes; and, as it relates to paid
> clicks, fluctuations in search queries resulting from changes in user adoption and usage,
> primarily on mobile devices. Changes in cost-per-click and cost-per-impression are driven by a
> number of interrelated factors including changes in device mix, geographic mix, advertiser
> spending, ongoing product and policy changes, product mix, property mix, and changes in foreign
> currency exchange rates."

**Q2-2026 10-Q** (accession 0001652044-26-000071) — identical boilerplate, updated table:

> "Google Search & other — Paid clicks change 13% (3 mo.) / 13% (6 mo.) — Cost-per-click change 3%
> (3 mo.) / 4% (6 mo.)
> Google Network — Impressions change (12)% (3 mo.) / (10)% (6 mo.) — Cost-per-impression change
> 13% (3 mo.) / 10% (6 mo.)"

**Note what the boilerplate no longer says.** Compare the FY2019 10-K, which named a *cause*:

> "The decrease in cost-per-click was primarily driven by continued growth in YouTube engagement
> ads where cost-per-click remains lower than on our other advertising platforms."

FY2023 onward names no cause at all — it recites the same undifferentiated list of "interrelated
factors" verbatim in every filing. The explanatory content of the disclosure was withdrawn even
though the numbers were kept. The FY2023, FY2024, FY2025, Q1-2026 and Q2-2026 paragraphs are
**word-for-word identical** apart from the table.

## 2.6 FILED REASON FOR REMOVAL, AND THE DEFINITIONAL RESET

**For the 2018 withdrawal (aggregate + Network clicks): no reason filed.** Nothing in the Q1-2018
10-Q or the FY2018 10-K explains it. The switch to impressions on the Network leg is presented as
a fait accompli.

**Alphabet did once disclose a methodology change, which shows it knows how to.** FY2017 10-K
(0001652044-18-000007), verbatim:

> "In the first quarter of 2017, we refined our methodology for paid clicks and cost-per-click to
> include additional categories of TrueView engagement ads and exclude non-engagement based trial
> ad formats. This change resulted in a modest increase in growth of paid clicks and a modest
> decrease in growth of cost-per-click. For comparison purposes, we have included updated data for
> historical periods in the table below:"

Alphabet then filed a full quarterly bridge table restating prior periods. **That is the standard
it set for itself in 2018, and did not meet when it dropped the TAC split in 2020 or the aggregate
click metrics 77 days after that FY2017 10-K.** One paragraph of disclosure and a bridge table;
the other two changes got neither.

Alphabet also formerly filed a "Use of Monetization Metrics" section explaining what the numbers
were and why management watched them ("Management views these as important metrics for
understanding our business" — FY2015, FY2016, FY2017 10-Ks). That framing language is gone from
the current vintage; the FY2025 10-K carries only a bare definitional paragraph.

## 2.7 IS THE REPLACEMENT ON THE FILING RUNG?

The question does not arise for paid clicks / CPC, because nothing replaced them — they are still
filed in MD&A of the 10-K and 10-Q, which is the filing rung (Rung 1). No 8-K Ex-99.1 workaround
is involved.

It **does** arise for the TAC split (Part 1) and for the aggregate/Network click metrics (§2.3).
For those:

- **Nothing on the filing rung replaced them.** The FY2025 10-K files an aggregate TAC dollar, an
  aggregate TAC rate, and an adjective.
- Alphabet's quarterly **8-K Ex-99.1 earnings releases** likewise do not restore the TAC split;
  they carry the same revenue-by-type and cost-of-revenues lines. **RUNG-1 CAVEAT: this was
  verified for the periodic reports; the individual 8-K exhibits FY2020–FY2026 were not each
  opened in this pass. Treat "the 8-Ks do not restore it" as UNRESEARCHED-leaning rather than
  established, and check `googexhibit99*` in the Q4 8-K accessions if the point becomes
  load-bearing.**
- Item 2.02 8-K exhibits are furnished, not filed, and carry the "not deemed filed" legend, so
  even if a figure appeared there it would sit one rung below the 10-K.

---

# PART 3 — SUMMARY TABLE OF DISCLOSURE WITHDRAWALS, ALPHABET, 2018–2026

| # | Series | Last filed | First omitted | Days | Reason filed? | Direction at withdrawal |
|---|---|---|---|---|---|---|
| 1 | Aggregate paid clicks Δ / aggregate CPC Δ; Network **paid clicks** Δ / Network **CPC** Δ | FY2017 10-K, 2018-02-06, 0001652044-18-000007 | Q1-2018 10-Q, 2018-04-24, 0001652044-18-000016 | **77** | No | Network CPC negative 4 of 4 filed years; aggregate CPC negative 4 of 4 and worsening |
| 2 | **TAC split**: distribution partners vs Network, $ and separate rates | Q3-2019 10-Q, 2019-10-29, 0001652044-19-000032 | FY2019 10-K, 2020-02-04, 0001652044-20-000008 | **98** | No | Distribution-partner rate up every year filed, 7.8%→13.3%; that leg 3.07× in 3 years and had just crossed 50% of total TAC |
| 3 | Comparative-period columns in the monetization table (presentation) | FY2020 10-K, 2021-02-03, 0001652044-21-000010 | FY2021 10-K, 2022-02-02, 0001652044-22-000019 | 364 | No | n/a — presentation only |
| 4 | Causal MD&A explanation of CPC movement (replaced by fixed boilerplate) | FY2022 10-K, 2023-02-03, 0001652044-23-000016 | FY2023 10-K, 2024-01-31, 0001652044-24-000022 | 362 | No | n/a — narrative only |

**Not withdrawn:** paid clicks Δ and cost-per-click Δ for Google Search & other, and impressions Δ
and cost-per-impression Δ for Google Network. Both are filed in the FY2025 10-K and in the Q1 and
Q2 2026 10-Qs.

## THE ANALYTIC READING

Withdrawal #2 is the one that matters for Q2 (is it a franchise?) and Q3 (are they honest?).

The distribution-partner TAC line **is the toll Google pays to be the default**. It is the price
of the Apple, Mozilla and carrier contracts. Its rate rose in every single year Alphabet filed it,
by 5.5 percentage points in four years, and Alphabet's own MD&A attributed the rise to "changes in
partner agreements". Ninety-eight days after the last filing that quantified it, the line was gone
— without a word of explanation, and without the bridge table Alphabet had itself filed for a far
smaller change twenty-three months earlier.

Nothing here proves intent. What it establishes on the filing rung is narrower and firmer: **the
single most important input to the durability question — what Google pays to keep its distribution
— has not been observable in an Alphabet periodic report since 2019-10-29**, and the only
substitute Alphabet offers is an aggregate rate that falls for reasons unrelated to the price
being paid. On the framework's terms, "what is the distribution-partner TAC rate today?" is a
question whose resolving document **does not exist**. That is not UNRESEARCHED. It is
**UNKNOWABLE from the filings**, and it is Alphabet that made it so.
