# -*- coding: utf-8 -*-
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\WATCHLIST RUN QUEUE.md"
t=open(p,encoding='utf-8').read()

# STEP 2 - strike the ticker in the tier roster
a="SWK, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ROKU, RGTI, ~~ORCL~~, ~~BA~~, ACMR, ALKT, ~~INTC~~, ACVA, NEGG, FLNC"
b="SWK, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~, ~~BA~~, ACMR, ALKT, ~~INTC~~, ACVA, NEGG, FLNC"
assert a in t
t=t.replace(a,b)

# record what the tail-triage correction meant for a name it never labelled
a2="""**STILL LIVE UNDER THESE LABELS: NEGG and FLNC (first sub-class), ACMR, ALKT and ACVA (second).
BA (third) WAS RUN 2026-09-12 and is struck.** Read every one of them as unlabelled."""
b2="""**STILL LIVE UNDER THESE LABELS: NEGG and FLNC (first sub-class), ACMR, ALKT and ACVA (second).
BA (third) WAS RUN 2026-09-12 and is struck.** Read every one of them as unlabelled.

**AND THE OTHER HALF OF THE CORRECTION, FOUND BY THE ROKU RUN OF 2026-09-12: FOUR OF THE FIFTEEN
TIER-3 NAMES WERE NEVER LABELLED AT ALL.** The four sub-classes above cover eleven names (BE, NEGG,
FLNC, ACMR, ALKT, ACVA, BA, INTC, ORCL, MU, RGTI). **SWK, ARM, CALX and ROKU appear in the tier
roster and in no sub-class** - the triage of 2026-09-02 passed over them silently. Three of the four
have now been run and **all three closed at Q2 on the business** (ARM, CALX, ROKU), which is the
opposite of what the labelled classes predicted for the tier: the tier-3 note is about arithmetic,
and on the names it did not label it turned out the arithmetic was never the question. **The lesson
is not that the labels were wrong - it is that an unlabelled name in a labelled list reads as
"nothing here", which is the same conclusion-smuggled-in-as-advice the CGNX prohibition forbids,
delivered by omission instead of by wording.** SWK is the one still live."""
assert a2 in t
t=t.replace(a2,b2)

# STEP 1 - the COMPLETED entry, inserted at the head of the register
entry = """- **ROKU (Roku, Inc.), 2026-09-12 - FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN, Q2 OUT; Q3 and Q4
  items are RECORDED WITH NO VERDICT under an explicit banner; Q5 is headed COMPUTATION - NOT A
  CLEARANCE; Q6 records reversal conditions in words and arms nothing.**
  `Test Runs/2026-09-12 Run - ROKU Roku.md`, `check_framework.py` PASS.
  Price **$154.93** (2026-09-11 close, Yahoo, aggregator flagged) x **148,418,969 shares** -
  **132,050,905 Class A plus 16,368,064 Class B**, read off the cover of the **10-Q for the period
  ended 2026-06-30, filed 2026-08-06, accession `0001628280-26-054335`** = cap **$22,996M**.
  Sovereign **5.35% USD** (US Treasury daily par yield curve, 30-yr, issuing authority,
  **2026-09-11**). Earnings currency USD - the filing says most of both Platform and Devices
  revenue is generated in the United States.
  **THE SHARE-CLASS JUDGMENT, WHICH `cover_shares.py` REFUSES TO MAKE: the two classes ARE summed,
  and the ground is two documents, not arithmetic.** The merger agreement pays *"each share of
  Class A Common Stock ... and Class B Common Stock"* one identical Merger Consideration and votes
  them *"together as a single class"*; and 132,050,905 x 1 + 16,368,064 x 10 = 295,731,545 votes
  makes the Class B **55.3%** of the voting power, which reconciles with the 8-K's disclosed
  *"approximately 55% of Company's outstanding voting power"* held by the founder's Voting and
  Support Agreement stockholders. Class B is a voting instrument, not an economic one.
  **THE QUEUE CAP WAS RIGHT** - `cap_m 22995` against $22,996M - **and it was right because it
  summed the classes, which is the answer the run reached independently rather than by assumption.**
  Second cap in this tier to survive the re-strike, after BA.
  **⚠️ THE FACT NEITHER THE QUEUE ROW NOR THE BRIEF CARRIED: ROKU IS A PENDING ACQUISITION.** On
  **2026-06-14** Roku signed a definitive Agreement and Plan of Merger with **Fox Corporation**
  (8-K accession `0001140361-26-025115`): **0.9693 FOXA shares plus $96.00 in cash per Roku share**,
  both classes alike, Roku holders to own **~27%** of the combined company. Board unanimous; the
  founder's ~55% voting block signed a VSA; **S-4 effective 2026-09-01** and the joint proxy mailed;
  **DOJ Second Request 2026-09-08** (accession `0001140361-26-035990`); close expected **H1 CY2027**;
  outside date 2027-06-14 extendable to 2028-03-14; termination fees **$866,084,000** from Roku and
  **$1,237,262,000** from Fox on a regulatory failure. **At FOXA's 2026-09-11 close of $65.94 the
  consideration is $159.90, so the $154.93 quote is a 3.1% MERGER SPREAD, not an owner-earnings
  price.** The screen reads XBRL and cannot see Item 1.01 of an 8-K: **a `merger_flag()` testing for
  an 8-K Item 1.01 or a DEFM14A since the last 10-K would have caught it, and this blind spot will
  recur on every queue name that gets taken over.**
  **Q2 OUT ON [E3-03] CRITERION (2), AND THE COMPETITOR ROW IS WHAT DID IT. Eleven peers, same
  metric, same window, filing-sourced.** The decisive row is **Vizio Holding Corp**, the only filer
  that ever published the same metrics and **dead since 2024-12-13** (Form 15-12G; last 10-Q period
  2024-09-30, accession `0001835591-24-000089`): **SmartCast ARPU $21.68 (FY2021) -> $32.48 (FY2023)
  -> $37.17 (Q3-2024), +71.5%, on one fifth of Roku's account base - against Roku's ARPU $41.03 ->
  $41.49, +1.1%.** Roku's flat ARPU is **not an industry condition**; the smallest and least-scaled
  participant was raising its take 18% a year while the scale leader could not raise its take at all.
  On margin, Vizio's Platform+ ran **57.5%** (9M-2024) against Roku's **advertising-only 57.8%**
  (FY2025) - **out-scaling Vizio 5:1 in platform revenue bought no margin advantage whatever.** And
  Vizio's Device gross profit crossed **+$115.7M (FY2021) to -$8.6M (FY2023)**, the identical
  crossing in the identical years, with platform at **106.1%** of its gross profit against Roku's
  **104.0%**: two independent filers, one shape, which is **[E2-27]** and not a moat.
  **THE SUBJECT'S OWN RISK FACTORS CLOSE THE GATE.** *"Large companies such as **Amazon, Apple, and
  Google** offer TV streaming devices that compete with Roku streaming devices ... and the Roku TV
  OS"*; *"We also face increased competition from **Walmart** ... in light of its acquisition of
  **Vizio** ... and the integration of Vizio's operating system into Walmart products **instead of
  other third-party proprietary operating systems**"*; *"These companies ... **can subsidize the
  cost of their streaming devices or licensing arrangements**"*; and decisively, *"**at times our
  existing licensed Roku TV partners have chosen to work exclusively with, or divert a significant
  portion of their business with us, to other operating system developers**"* - substitution
  admitted as already having happened. Plus: *"**Amazon, Best Buy, Target, and Walmart in total
  accounted for 81% of our Devices revenue**"* with *"**no minimum purchase commitments or
  long-term contracts**"* - **two of those four own competing operating systems.** Charter's own
  10-K is the third-party clincher, listing Roku as one of six interchangeable surfaces: *"such as
  **Xumo, Apple TV, Roku, Vizio, LG and Samsung TV**"*. And Roku ships The Roku Channel onto *"Amazon
  Fire TVs, Samsung TVs, Google TV"* - **substitution admitted by its own conduct.**
  **THE SEVENTH SUBSTITUTE THE BRIEF DID NOT NAME:** **Xumo**, Comcast's *"consolidated streaming
  platform joint venture with Charter"*, with *"Xumo TV smart televisions, which have an operating
  system"* and a *"Xumo Stream Box"* - reported inside Corporate and Other with Sky Germany and the
  Philadelphia Flyers, so **unsized**, and backed by $33.6bn of annual operating cash.
  **[E2-49] FIRES ON ALL THREE UNIT-AND-PRICE SERIES AT ONCE - A FIRST FOR THIS QUEUE.** Three
  different KPM sets in three consecutive annual reports: FY2023 *"gross profit, Active Accounts,
  Streaming Hours, and ARPU"*; FY2024 *"Streaming Households, Streaming Hours, ARPU, and Free Cash
  Flow"* (gross profit dropped, the year after margin went 50.9% -> 46.1% -> **43.7%**); FY2025
  *"Streaming Hours, Platform revenue, **Adjusted EBITDA**, and Free Cash Flow"* - **Streaming
  Households and ARPU both DELETED, and the FY2025 10-K carries no value for either anywhere in the
  document**, only the words *"more than 90 million Streaming Households globally"*. Net additions
  had decelerated 39% -> 17% -> 16% -> 14% -> **12%** before the series ended; the words are
  consistent with **+0.3% growth and with +9%**, so **the direction of the scarce asset - [E4-32]'s
  *"primary criterion of a great business"* - is now unmeasurable from the filings.** The candor half
  of [E2-49] is recorded too: it was announced with a reason. **And the unit series has its own
  switch:** *"volume of streaming players sold"* fell **-4%, -14%, -8%** in 2021-2023, the Precision
  Steel shape **[E4-55]**, and in FY2024 the basis was widened to *"volume of **all devices
  shipped**"*, which folded in the new Roku-made TVs and turned the sign positive.
  **Q1 IN, AND THE SEGMENT SPLIT KILLED A CLAIM THE CONSOLIDATED NUMBERS SUPPORTED (the AMAT
  lesson).** **Platform is 104.0% of FY2025 gross profit and Devices is -4.0%** ($2,156.4M against
  -$82.0M), and Devices has been a gross LOSS in each of the last five years, cumulatively
  **-$334.6M**. The 44% consolidated gross margin is the blend of a 52.0% platform with a -13.8%
  distribution expense, and the filing states the trade itself: *"this trade off from Devices gross
  profit or loss to grow Streaming Households should result in increased Platform revenue."*
  **Correction to the brief:** OEM-licensed Roku TV models *"account for the largest portion of our
  overall unit volume"* and carry no device cost at all, so the Devices gross loss is the minority
  acquisition channel; a second slice sits in Sales and marketing.
  **THE ONE NUMBER, AND ROKU SETS THE QUEUE RECORD: cumulative SBC/OCF 140.2%** - ten filed years
  produced **$1,378,145k** of operating cash and paid **$1,932,508k** in stock. **First in the
  calibrated row by 42 points** (CALX 98.4%, ARM 96.6%, PINS 68.6%, CRWD 68.0%). Five-year 138.3%,
  three-year 115.8%, FY2025 73.2%, TTM 45.6%. **Every year resolves; the zero-SBC defect of
  2026-09-12 does not touch this name**, and SBC is falling - FY2024 peak $384,662k, TTM $328,038k.
  **THE 351% CONTRACT-LIABILITY FLAG - THE LARGEST IN THE 361-NAME QUEUE - DECODED, AND IT NAMES THE
  WRONG LINE.** It is the **`Deferred revenue`** line of the FY2022 cash-flow statement: **+$41,402k
  against $11,795k of operating cash = 351.0%**, reproduced to the dollar. **Without it FY2022
  operating cash was -$29,607k.** It IS customer money (Platform deferred revenue went $17,144k to
  $59,276k on *"billings in excess of revenue recognized"*), but the balance has never exceeded
  **$149.8M, 3.2% of revenue**, and **56% of it is not customer float at all** - it is the portion of
  a device's price allocated to *"unspecified upgrades and updates"*, i.e. cash already collected.
  **The 351% is a DENOMINATOR ARTIFACT and the flag reports the smallest of three movements in the
  same column: FY2022's real working-capital event was `Content assets and liabilities, net` at
  **-$313,204k**, 7.6x larger and untested; FY2023's `Accounts payable` build of **+$248,175k** was
  **97.0%** of that year's operating cash, also untested.** **Content is this business's real capital
  expenditure and it already runs through operating cash, which is why total capex is $5,280k** -
  which is also why (c) is judged with the exception class REVERSED: D&A of $68,904k is 13x capex, so
  **D&A is the conservative end here, not the invalid one [E5-20]**. Separately-tagged capitalised
  software: **checked, there is none** - the HAS/CRWD defect does not apply.
  **OWNER EARNINGS REBUILT, EIGHT WINDOWS x BOTH (c) ENDS: -$189M to +$382M, AND THE WORD IS
  STRADDLES.** A $571M width; **fourteen of sixteen constructions are negative** and the two positive
  ones are FY2025 and the TTM. **The screen's two numbers reproduce exactly and are the INTC defect
  again:** `oe_bottom -151` is the **five-year 2021-2025** mean at the capex end (-$150,725k) and
  `oe_top -81` is the **three-year 2023-2025** mean at the same end (-$81,434k) - **two windows, not
  two ends of a band**; the real capex band inside the five-year window is **$272k** wide.
  `level_shift_oe "EARLY HALF STRADDLES ZERO (from -$509.8M)"` is FY2022 at the capex end, correct.
  **Years chosen as the business that exists now [E4-41]: FY2024, FY2025 and the TTM** (the
  restructuring reset the cost base, opex fell $2,335M -> $2,024M and has grown 3% since, SBC peaked
  in FY2024, and internal reporting changed in Q1 2026) - **and on those years it still straddles
  zero, -$84M to +$382M.** Normalised down for luck: the company itself quantified the **IEEPA tariff
  refund** (*"net income would have been $127 million"* against $164.2M), ~$37M of non-recurring cash,
  and 2026 is a US election year with political advertising weighted to H2. **Normalised TTM
  +$285M to +$345M.**
  **ALL FOUR FLAGS REPRODUCE, AND `flags_disagree` IS THE WHOLE FILE IN ONE BOOLEAN.** `level_shift
  4.23 STEP UP` = mean(2023-25) $319,206k / mean(2017-22) $75,498k on the nine-year operating-cash
  series - **real, and in the wrong series: operating cash stepped up 4.2x and owner earnings did not
  step at all, because the entire step sits inside the SBC add-back.** The PLPC run added that flag
  for exactly this case and **Roku is its sharpest instance in the queue.** `window_disagree` fires
  because the nine-year window excludes FY2016's -$32,463k. `best_year_dep 0.2608`: drop FY2025 and
  the nine-year OCF mean falls **$156,734k -> $115,861k**.
  **Q5, COMPUTATION - NOT A CLEARANCE.** `yield_bottom -0.66%` and `vs_sovereign -6.01 pts`
  reproduce. **The single most favourable construction that exists anywhere in the filed history -
  unnormalised TTM at the capex end, +$381.9M - yields 1.66% against a 5.35% bond, -3.69 points.
  No window, no (c) end and no normalisation puts Roku above the sovereign.** The floor [E4-28]
  needs **8.34% perpetual growth** in owner earnings; the bare sovereign needs 3.69%. Value at the
  floor ~**$19-23/share**, at the sovereign ~**$36-43/share**, price **$154.93**. Screamer test,
  third outcome - price above the whole range. Windage count **one**. Total merger consideration
  $23,732M is **62.1x** the best TTM owner earnings and **56.4x** FY2025 Adjusted EBITDA.
  **Q3 AND Q4 ITEMS, RECORDED WITHOUT A VERDICT.** **Nine operating losses in ten filed years;
  FY2025 operating income -$5,624k and the $88,361k of net income is $99,522k of interest on the cash
  pile**; return on unleveraged net tangible assets of $2,298,332k is **3.8% on net income and -0.2%
  on operating income [E2-43, E3-46]**; APIC $4,145,485k against an accumulated deficit of
  **-$1,488,594k**. **[E4-29] fires in the 10-K itself, not only in the exhibits: Adjusted EBITDA of
  $420,513k against a GAAP operating loss of $(5,624)k - a $426,137k gap, 83% of it SBC** - and it is
  a named *primary* KPM, with *"Free Cash Flow per share"* as the *"north star"* though capex of
  $5,280k makes FCF equal to operating cash to within 1%. **[E3-48] runs the other way and is given
  its weight: guidance beaten on every line in three consecutive quarters** (Q4-25, Q1-26, Q2-26),
  net income at 2.0x, 1.7x and 1.8x the guide - then switched off entirely for the merger.
  **[E5-08]: bought 1.5M shares at an average of $99.99 nine months before the board agreed to sell
  at $159.90** - conditions (1) and (2) satisfied in fact, **(3) [E4-31] FAILS**, because the
  register had just been deprived of the two metrics needed to value the asset; and the stated
  purpose is dilution offset, not value. **$149,982k of buybacks plus $164,850k of net-share-
  settlement taxes = 65.1% of FY2025 operating cash spent managing the share count.** **[E4-52]:
  Roku pays no cash bonuses and grants NO performance-conditioned equity at all** - no bullseye to
  mis-set, and no accountability either; CEO and CFO targets raised 4% and 20% in June 2025.
  **[E4-30] clean** (cash taxes rose to 14.6% of pretax as income appeared; full US valuation
  allowance disclosed). **Restructuring charges $356,094k / $30,999k / $3,064k are IN the mean
  [E5-33], not annualised away.** **Staying power: (1) NO, (2) YES - $2,557M liquid, zero
  interest-bearing debt, $1,055k of interest paid, (3) YES - $389,489k of 2026 purchase
  commitments.** **Great/good/gruesome: gruesome**, with the honest qualification that the TTM is the
  first period in which the arithmetic is not.
  **THE NAMED WAY IT DIES, quantified [E2-27, E3-24, E4-40]:** the OS is displaced by the people who
  make and sell the sets, and a ~90M-household base needs ~13M replacements a year to stand still.
  Each 1% of base decline costs ~$21.6M of platform gross profit at constant ARPU; **a 7% annual
  decline removes ~$151M a year and the operating line is already at zero** - year one takes
  operating income to ~-$157M, year three to ~-$440M, against a cost base that is 88% personnel and
  distribution. **Likelihood: a real possibility.** And **[E4-40] governs the read** - ten years of
  household growth is exactly the benign history the corpus calls *"actually dangerous"* as a guide,
  **and the metric that would show exposure turning into experience is the one that was deleted.**
  **THE STRONGEST FACT AGAINST THE VERDICT, stated as [E4-51] requires:** advertising gross margin
  expanded **~650bp YoY to 62.4%** in Q2 2026 on **25%** revenue growth, faster than the US OTT and
  digital ad markets, with advertising gross profit up **39%**; the memory cost advantage is real and
  filed (*"the Roku TV OS requires significantly less dynamic memory (DRAM) and storage memory
  (Flash) than competing platforms, and this widening cost advantage is drawing more TV brands to
  Roku"*); **Hisense and TCL were added as OEM partners in 2025**; and Roku's platform revenue of
  $4,145M **exceeds Comcast's entire advertising line ($3,712M, -9.2%)** and is 2.8x Charter's
  ($1,468M, -17.6%). **Why the verdict stands: [E3-03](2) asks about substitutes, not this year's
  margin, and the 650bp were earned inside a category still taking share from linear TV - a surfing
  run [E3-51], whose separating test is whether the position can be PRICED. Roku's ARPU was flat for
  four years at the peak of its position while a fifth-the-size competitor raised its take 71%. That
  test was run and Roku failed it.**
  **NO ALERT BAND AND NO PORTFOLIO ROW** - the QLYS ruling: a name that failed at Q2 failed on the
  BUSINESS. Four reversal conditions are recorded in words at Q6, and **the first one names a
  document that does not exist**, because Roku chose not to file it.
  **Class NONE, not PROVISIONAL.** Samsung and LG are **UNKNOWABLE-from-SEC** - checked against the
  complete EDGAR CIK index, Samsung Electronics has **never filed a 10-K or 20-F** and last filed
  anything in 2015; LG Electronics last filed in **2008** - but the verdict does not turn on them.
  **A missing peer row cannot rescue a franchise claim the subject's own filing contradicts in its
  own words.**
"""
anchor = "## COMPLETED FROM THE QUEUE\n"
assert anchor in t
i = t.index(anchor)+len(anchor)
t = t[:i] + entry + t[i:]
open(p,'w',encoding='utf-8').write(t)
print('ok', len(t))
