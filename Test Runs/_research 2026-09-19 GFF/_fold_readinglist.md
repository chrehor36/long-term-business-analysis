
## GFF (Griffon Corporation) - run 2026-09-19 - Q1-Q4 IN, FAIL at Q5 on price
*Wave 6. One of the five ordinary businesses the 2026-09-01 triage dropped with no reason recorded.
Read as unlabelled. CIK 0000050725 confirmed by `cik_for()`. Started by a session killed at ~10:38
EDT and finished by a second one, which audited the draft before building on it.*
`Test Runs/2026-09-19 Run - GFF Griffon.md`. **Q1 IN; Q2 IN, class NARROW (capped); Q3 IN as a
gate on daily execution, capital-allocation flag live; Q4 IN (owner earnings about $254M, range
$235-273M); Q5 quit on at the ~10% floor, not ranked; Q6 a monitoring plan with two bands armed.**
Price **US$93.22** (2026-09-18 close, aggregator flagged; corroborated by the issuer's own $85.00
average repurchase price for April-June) x **45,294,716** (the Q3 FY2026 10-Q cover,
`0001628280-26-053536`) = cap **US$4,222.4M**; sovereign **USD 30-year 5.34%** (US Treasury,
09/18/2026). **Register count at the fold, read from the register: 121 runs** (120 entries before
GFF, no duplicate; per-question tallies not recounted by this session).

### WHAT THE SHARE BUYS
After the 2026 disposals: **Clopay, the largest North American maker of garage and rolling steel
doors, about 88% of continuing revenue**; Hunter Fan, about 12% and shrinking; a 43% stake in the
Veritage JV and a 49% stake in the AMES Australasia JV; and $209.7M of PIK notes those JVs owe it.
The August 8-Ks change the debt, not the business: the Term Loan B is repaid, $800M of 6.25% notes
due 2034 replace $975M of 5.75% notes due 2028, and nothing matures before the revolver in 2031.

### THE TABLE THAT DECIDED Q2
| | segment operating margin, 3 yrs | segment income on segment assets |
|---|---|---|
| Clopay (FY2023-25) | 31.2 / 30.6 / 30.1% | 70.5 / 65.8 / 61.9% (assets include goodwill) |
| Overhead Door, Sanwa North America (FYE 3/2024-3/2026) | 15.7 / 16.9 / 15.6% | 20.8 / 20.5 / 17.5% |
| Janus (FY2023-25, consolidated) | 23.0 / 15.2 / 12.6% | 8.5% (FY2025) |

**The same product, the same channels, the same size (USD 1,584M against 1,615M), about twice the
margin and three times the return, and the gap existed before the 2022 repricing** (FY2021: 15.7%
against ODC's 6.0%). Clopay held price when ODC (*"Efforts to stem the decline in selling
prices"*) and Janus (*"a decline in sales price"*) did not. CHI (inside Nucor) and Amarr (inside
ASSA ABLOY) are unsegmented and no document would fill them, so the class is capped at NARROW, not
suspended. **The attacker's test was answered by conduct**: Nucor, with ample capital, bought CHI for
about $3.0bn, of which plant was 3.7% of net assets acquired.

### THE DRAFT, AUDITED: six corrections, all against the draft's own confidence
1. **FY2022 is not "the literal wording of [E2-44]".** Price +47% with volume −2%, but the 10-K gives
   the reason volume fell: *"labor and supply chain disruptions impacting residential deliveries"*.
   That is supply short, not demand flat; it is [E3-43]'s *"supply ... is tight"* route to profit,
   which *"usually does not last long"*. The test passes on FY2023 and FY2025 instead, more narrowly.
2. **Capex was set against D&A that includes ~$15M a year of acquired-intangible amortisation.**
   Against depreciation, door capex runs 1.5-2.3x, and (c) was judged at the capex end.
3. An unsourced "three CEO-level strategic reversals ... without the margin moving" (the margin
   doubled); withdrawn.
4. "Not wave-riding" lacked its counter: the LEVEL was set by an industry-wide wave (ODC 6.0% to
   13.3% in one year); what is Clopay's alone is the gap.
5. The Hunter share "derived below" was never derived; it is 11.8% of revenue and about 5% of
   segment EBITDA.
6. A November 2023 earnings-release forecast ("market share gains") was cited as though an outcome.
**The lesson for resumed runs: a killed session's draft leans toward the verdict it was heading
for, and every one of the six errors leaned toward IN.** The verdict survived the corrections, but
on narrower ground than the draft claimed.

### Q3: THE PRO-AM EFFECT IN TEXTBOOK FORM, AND A PROXY THAT CALLS EVERY YEAR OUTSTANDING
- **[E2-56]**: the door business earned 62-70% pre-tax on segment assets while the consumer leg,
  $1.2-1.9bn of assets, earned 3-7% before depreciation. Hunter Fan was bought for $845M in January
  2022 on an $800M term loan and 38% of it was written off in four years; AMES went out as paper at a
  loss. The 2026 disposals end the Pro-Am; the flag stays live because the record is the record, and
  because the latest quarter's buybacks at $85.00 sit above the default value at the floor.
- **[E2-57] in the pay document**: the 2026 proxy calls fiscal 2025 (a $243.6M impairment) and
  fiscal 2022 (a $191.6M net loss) "outstanding" years. **[E4-29] is paid on**: EBITDA is 80% of the
  annual bonus.
- **A recast misprint**: the August 2026 recast prints adjusted EBITDA margins of 23.8% and 23.6% for
  FY2024 and FY2023 beside dollars that give 26.0% and 27.0%, reversing the trend. A prompt, not a
  finding of intent.

### Q5: ABOVE THE BOND, BELOW THE FLOOR (the Berkshire shape)
Yield **5.80% / 6.41% / 7.04%** (conservative / default / generous) against 5.34%: above the bond on
every filed construction. **The ~10% floor needs 2.8-4.0% perpetual growth (default 3.4%) against
continuing owner earnings that fell about 4.6% a year over the three years the perimeter has been
filed.** Value at the floor roughly **$55-105 a share, default about $80**; price inside the range,
upper half. Quit on, not ranked.

### TOOLING AND BRIEF DEFECTS FOUND
1. **`tools/run.py` reads the pre-disposal perimeter when a filer recasts through an 8-K.** Griffon
   filed its continuing-operations recast on an 8-K (`0001628280-26-054906`); `annual()` reads 10-K
   and 20-F facts, so the tool printed three-year owner earnings of 297-318 and a 7.04-7.54% yield on
   the consolidated perimeter including AMES, **about $50M a year and a point of yield too high**.
   Same family as the resume note's section 5 limit on 8-K perimeter events. Not fixed; the operator's
   call. A run on any filer with a closed disposal should read the recast by hand.
2. **The D&A-versus-depreciation (c) finding, a fourth instance** after IBM, ELF and DIS: Griffon's
   continuing D&A carries ~$15M a year of acquired-intangible amortisation (depreciation $20.9-23.9M,
   D&A $35.5-38.5M). The pattern is general.
3. **The brief's "projectbourne" exhibits and "2026-08-11 purchase agreement"** read as possible
   transactions. They are a side letter to the Australasia share sale agreement, the PIK note, and a
   note purchase agreement with the underwriters of the 2034 notes.
4. **The peer file names `FOREIGN_fiskars_fans.md`, which is not on disk.** The fans leg was judged
   on Griffon's own words (*"retailer house brands such as Hampton Bay ... and Harbor Breeze"*).

### BANDS ARMED (fold step 4: a four-gate clearer, as KO, CL and SPGI)
`tools/alerts.json`: **GFF-rerun-band at $82** (the ~10% floor met on $253.8M of owner earnings with
2.5% perpetual growth granted, growth the last three filed years do not show) and **GFF-floor-band
at $62** (the floor met on the same owner earnings with zero growth). A ping is a prompt to re-run
the gates, never an action; both VOID if a Q2 falsifier fires. A `PORTFOLIO.md` watch row was added.
Survival shapes: GFF added to #10 THE CAMOUFLAGE (the record, now mostly excised) and #11 THE
PASS-THROUGH (the named first death, not yet arrived). No new shape proposed.

### ONE THING TO KEEP
**A narrow moat can be real and still be priced for growth it has stopped showing.** Clopay beats
its nearest rival by two to one on the same line, and did before the 2022 repricing; the share buys
that plus a management whose record with the franchise's cash is a fan company and a tools business,
at a price that needs more growth than the last three filed years delivered.
