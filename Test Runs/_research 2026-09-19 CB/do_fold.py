# THE FOLD FOR CB (Chubb Limited), run of 2026-09-19. All six steps, one read-modify-write.
# Concurrent runs share this tree: the register entries are counted INSIDE this script, before
# and after, and the script asserts that exactly one was added and that CB appears once.
import io, os, re, json, sys

ROOT = os.path.abspath(".")
def rd(p):
    return io.open(os.path.join(ROOT, p), encoding="utf-8").read()
def wr(p, s):
    io.open(os.path.join(ROOT, p), "w", encoding="utf-8", newline="\n").write(s)

QUEUE = "Screens/WATCHLIST RUN QUEUE.md"
LIST = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
SHAPES = "Screens/SURVIVAL SHAPES - index.md"
PORT = "PORTFOLIO.md"
ALERTS = "tools/alerts.json"
LOG = "Screens/_daily/OVERNIGHT LOG.md"

ENTRY_RE = re.compile(r"(?m)^- \*\*([A-Z0-9.\-]{1,7}) \(")

def register_tickers(s):
    hs = [m.start() for m in re.finditer(r"(?m)^## COMPLETED FROM THE QUEUE\s*$", s)]
    assert len(hs) == 1, "expected exactly one register heading, found %d" % len(hs)
    tail = s[hs[0]:]
    m = re.search(r"(?m)^## (?!COMPLETED)", tail[3:])
    sec = tail[:3 + m.start()] if m else tail
    return ENTRY_RE.findall(sec), hs[0]

# ---------------------------------------------------------------- STEP 1: the register entry
q = rd(QUEUE)
before, hpos = register_tickers(q)
n_before = len(before)
print("register entries BEFORE: %d" % n_before)
assert "CB" not in before, "CB already in the register - another session folded it; stop."

ENTRY = """- **CB (Chubb Limited), 2026-09-19 - ALL FOUR BUSINESS GATES IN; FAIL AT Q5 ON PRICE (QUIT ON AT THE ~10% FLOOR [E4-28], ABOVE THE BOND ON EVERY
  CONSTRUCTION).** **WAVE 6** and the **MINI BERK insurance track**, run under
  `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md` with both amendments applied. **CIK 0000896159 found by
  `tools/sources.py:cik_for('CB')`**, not taken from the brief; the registrant is the former **ACE Ltd** (renamed 2016-01-15 after buying The Chubb Corporation),
  SIC 6331, Swiss-incorporated, USD-reporting. **Q1 IN**: two engines and the filing names them - of $12,000M of attributable pre-tax operating income, **P&C
  underwriting income $6,528M and net investment income $6,465M**, roughly half and half, with **Chubb Life contributing a MINUS $12M underwriting result and a
  $1,242M segment income that is entirely investment income**, so under [E5-48] the Life leg adds almost nothing to the two-component sum. Six segments as filed;
  North America Commercial is 39% of premium and 53% of segment income; **32% of segment income never reaches pre-tax income**. **Q2 IN (NARROW) - and this is the
  first name in this queue to pass the MKL test outright.** On the MKL precedent the decisive series is the **CURRENT-ACCIDENT-YEAR combined ratio INCLUDING
  catastrophes**, and Chubb's is **92.6 / 97.9 / 93.9 / 93.4 / 97.4 / 91.9 / 90.4 / 88.6 / 88.7 / 88.2 for 2016-2025 - below 100 in TEN of TEN years, worst year
  97.9 (2017, Harvey-Irma-Maria), ten-year mean 92.3** - so the reported underwriting profit is earned, not released: in 2025 the releases were **$1,132M of
  $6,528M, 17%**. Built TWICE and the second construction is not the filer's: the same series rebuilt from the dollar reconciliation table (lines A/B/C/D/E/F)
  gives 93.33 / 97.34 / 91.86 / 90.08 / 88.40 / 88.57 / 88.22 for 2019-25, **agreeing within 0.3 points in every year**. Favourable prior-period development in all
  ten years and **declining** (4.3 to 2.5 points). Expense ratio **28.5 (2018) to a 25.6 trough (2022) and back up 1.0 point to 26.6 (2025)**, all of it in policy
  acquisition, the filer's reason *"changes in mix of business"* - the same shape the MKL run recorded against Markel, 9.5 points lower and half the slope.
  **The moat claimed is NOT the product** - [E2-70] settles that and the filer's own risk factors restate [E2-58]'s equation (*"periods of intense price competition
  due to excessive underwriting capacity"*) - it is **the funding (cost of float -8.58%), the licence network (local admitted paper, Lloyd's Syndicate 2488 at
  GBP 630M of 2026 capacity, 87.2% of Huatai) and the cost base**. **NARROW on four recorded defects:** [E3-03] criterion 3 **fails outright** for North America
  Agricultural (5.3% of NPW) because Rain and Hail *"primarily operates in a federally regulated program where all approved providers offer the same product forms
  and rates"* - [E2-59] exactly, carried as [E5-40]'s good-not-great leg the way the BRK run carried BHE; **[E2-44] fails on its first half in the filer's own
  words** (*"rate decreases in our Large Risk and E&S brokerage property lines"*, Major Accounts +1.4%, and the Q2 2026 release *"soft market conditions are
  spreading to certain areas of casualty"*) - Chubb's answer to an inadequate price is to shrink, which is [E4-37]'s agony metric detecting a downgrade in real
  time; no untapped pricing power [E3-33, E5-28] and no dominance [E2-53]; and **key-person dependence is recorded AT Q2 as a moat defect [E4-23]** - 22 years of
  one CEO in the industry [E2-70] says *"magnifies the effect which individual managers have"*, no named successor, and **17.7% of votes against his election as
  Chairman in 2026 and 22.6% in 2025**, the largest dissent at either meeting. **THE COMPETITOR ROW WAS EXTENDED FROM THE MKL RUN, NOT REBUILT, AND THE RANKING
  CHANGES.** Every accession in `_research 2026-09-02 MKL/competitor-row.md` was independently re-resolved and all five matched. Reported five-year means: KNSL
  76.66 > ACGL 82.28 > RLI 85.52 > **CB 87.10** > WRB 89.92 > FFH 93.72 > MKL 94.18 > AXS 95.06. **On the current-accident-year basis (reported plus each filer's
  OWN published favourable prior-year development): KNSL 80.60 > ACGL 86.99 > CB 89.50 > WRB 89.84 > RLI 93.08 > AXS 94.10 > MKL 100.27.** **RLI's headline 85.52
  is built on 6.1 to 10.8 points of releases a year and runs 93.08 on the business it actually wrote - 3.6 points WORSE than Chubb, and a run that stopped at the
  reported row would have ranked Chubb behind it.** Markel is last by 10.8 points, the MKL verdict replicating from a second direction. **AXS inverts** (2023
  reported 99.9 contained 8.1 points of ADVERSE development, so its current-accident-year ratio was 91.8) - the basis cuts both ways. **W. R. Berkley is the
  reserving-integrity benchmark of the row and the run says so: +0.08 / -0.38 / -0.18 / +0.04 / +0.03 points, essentially zero net development on a $10-12bn book
  three years running, so its reported ratio needs no adjustment at all.** FFH recorded **NOT COMPARABLE** (IFRS 17, no comparable separation in Exhibit 99.3);
  KNSL 2021 and RLI 2021 named as unobtainable on this basis, not estimated. **Q3 IN AS A BINARY GATE** (two of three determinants: daily execution [E3-38, E2-70,
  E2-50] and leverage [E3-29] - investments **2.29x** Chubb equity, float 0.92x). **[E4-29] is CLEAN and was tested the hard way**: the CGNX companion rule was
  applied and `grep -ic ebitda` returns **0** in both proxies, all four EX-99.1 releases, all four EX-99.2 Financial Supplements, all four 8-K bodies and both
  annual-meeting 8-Ks; GAAP net income leads every headline, with catastrophes and PPD quantified as separate bullets each quarter. **Three flags fired, read, and
  they do NOT converge [E4-52]:** (1) **[E4-22]/[E3-48]/[E5-30] the projections flag** - no guidance table anywhere, but the CEO promises *"double-digit growth in
  EPS and tangible book value"* in every release read and *"core operating ROE increasing to 14% plus over the medium term"*; [E3-48]'s action was taken and the
  promises have been **beaten** (TBVPS +17.1% y/y at 6/30/26, core operating ROE 14.5% annualised), so it is scored small - but [E5-30] calls the behaviour a
  ratchet and it is now on this name's record; (2) **[E2-49] metric-switching** - the FY2025 10-K **redefined the leverage ratio to exclude unrealised investment
  losses from total capitalisation**, which improves it from 18.85% to **18.44%**, a switch that follows a period of large unrealised losses; announced with
  reasons in the filing that first used it and with the prior year restated, which is [E2-49]'s candor case, so **fired and it changes nothing**; (3)
  **[E2-30](2) acquisitions soaking up funds** - Cigna Asia 2022, Huatai to 76.5% then 85.5% then 87.2%, Healthy Paws 2024, LMG Thailand $321M in 2025, Liberty
  Vietnam in 2026; goodwill $15,213M to $20,207M, and goodwill plus intangibles plus VOBA **$29,423M, 40% of Chubb equity** - all inside insurance and inside the
  licensed geographies, so [E3-40] loss of focus is not yet visible. **[E4-30] REFUTED on both halves**: the reported combined ratio has a 10.4-point range over
  ten years and net income fell 38% in 2022 - nothing is smoothed - and the 5.4% effective rate of 2023 is the named, dated Bermuda Economic Transition Adjustment
  deferred tax asset, with the rate rising for two years since. **[E2-52] cleared by reading rather than grepping**: the $1,520M dividend routed OUT of additional
  paid-in capital is the Swiss capital-contribution-reserve mechanism (the statutory auditor confirms compliance), while retained earnings rose $61,561M to
  $69,950M - not a dividend funded by capital. **[E2-01]** 5-yr mean ROE **14.14%**, on equity excluding AOCI **12.92%**, and on [E2-43]'s unleveraged net tangible
  denominator **26.0%** with the $29.4bn wedge reported separately. **THE [E2-67] CANDOR TEST IS THE CENTRAL Q3 QUESTION IN THIS SECTOR [E2-50] AND IT IS
  SATISFIED, WITH THREE THINGS RECORDED AGAINST IT.** From the nine ten-year triangles' own supplementary lines, 2025 PPD by line: **workers' compensation
  $(519)M favourable against NA Commercial Liability +$319M and Other Casualty +$162M ADVERSE, plus $306M adverse in the run-off book; long-tail net is only
  $(61)M, so 95% of the favourable development is SHORT-TAIL**, and the filer says so in words (*"$1,329 million in short-tail lines and favorable development of
  $110 million in long-tail lines … partially offset by adverse development in casualty lines"*). **The direction of the error is TWO directions**: short-tail
  systematically over-reserved (ten straight years of releases, a conservative bias, the opposite of the one Berkshire confessed), **North America long-tail
  casualty systematically UNDER-reserved - adverse in eight of the last nine accident years, AY2018 +18.7%, AY2019 +16.5%, AY2023 +8.8% in two years**, with net
  IBNR at 52% of incurred on AY2023 and 71% on AY2024. Against: the filer tells the reader the triangles are *"of limited use for independent analysis"*; it
  publishes no single consolidated table of its own error the way [E2-67]'s benchmark does (the data is there, the scorecard is not); and **the actuarial function
  reports to the CFO** - mitigated by an annual **external independent actuarial assessment reviewed by an all-independent Audit Committee with the Chief Actuary**
  (January 2026, and a joint session with Risk & Finance in February 2025). **[E2-72] is the one candor item Chubb does not clear: no shareholder letter.**
  **[E4-27] IS THE SHARPEST FINDING AND IT WAS NOT IN THE BRIEF: 100% of the CEO's equity award vests on tangible book value per share growth (70%) and the
  REPORTED P&C combined ratio (30%), with no catastrophe and no prior-period-development exclusion in the PSU criteria** - the incentive pointed at the pen
  [E2-50]. **Five counterweights recorded [E4-26]**, the decisive one being that **both metrics are RELATIVE to peers and the row shows Chubb releasing LESS than
  every peer but W. R. Berkley (1.9-2.8 points against RLI 6.1-10.8, ACGL 3.4-8.0, KNSL 2.7-5.5, MKL 5.6-5.8)** - the incentive points one way and the behaviour
  goes the other; plus EY verifies the vesting calculation, the Committee cannot vest above actual performance, and repurchases at 2.5x tangible book REDUCE the
  70% metric. **CAPITAL-ALLOCATION FLAG LIVE [E5-08](2):** $15,764M repurchased 2021-25 at 1.43x, 1.69x and 1.50x year-end book (2023/24/25) and $326.03 average
  in H1 2026 = **2.5x tangible book**, above the conservative end of this run's own range, with **no published repurchase condition of any kind** where [E5-25]
  shows Berkshire publishing both as numbers; management's own filed ground is *"our stock is trading well below intrinsic value"*, and the flag is recorded with
  the [E4-13] humility clause and **binds position size only**. CEO pay $33.18M, ratio **512x**, Swiss binding executive-compensation ceiling **$78M for 2026 to
  $98M for 2027**, say-on-pay 95.8% for, Chairman and CEO combined with an independent Lead Director. **Q4 IN.** No owner-earnings number is computed and the
  reason is the method's own; **THE LOEWS TEST WAS RUN EXPLICITLY AND ITS ANSWER DISCARDED**: OCF $12,816M less SBC $400M is **9.45% of the cap**, and stripping
  the $3,402M of net reserve growth and $2,775M of unearned-premium growth leaves **$6,239M, 4.75% - a 50% collapse**, the Loews shape present in Chubb's cash
  flow too. **COST OF FLOAT [E3-69], DIAGNOSTIC AND NOT ADDITIVE: -6.61 / -7.82 / -9.08 / -9.24 / -9.82% for 2021-25, a five-year mean of -8.58% on average float
  of $60,823M - Chubb is PAID about 8.6% a year to hold other people's money, against BERKSHIRE'S -3.6% on the identical five years from this project's own BRK
  run.** Negative in all seven years tested including 2020. **Stage 0(b) both ratios: float/investments 40.3%, almost exactly [E5-46]'s own 41.8% calibration, so
  step 2 is a MAJOR term here and not the rounding item it was at WTM; investments/equity 2.29x, ABOVE Markel's 2.01x and five times Berkshire's 0.45x**, so
  CONVENTION 5 applies at full strength. Three substitutions applied: liquidity read as reserve adequacy and net worth, and **the walking-dead test [E2-61] failed
  in the right direction** - Chubb CUT property premium on price rather than redoubling; reserve development as the candor test; and **[E2-62]'s licence to
  concentrate neither claimed nor needed** (listed equities are 6.4% of investments; equity is one-tenth of Berkshire's). **[E4-20] GOOD, not great** and [E4-43]
  governs - the good class passes. **[E5-11] 3 of 3** with $4.8bn of [E5-39] kindness-of-strangers funding **named**: $3.3bn of repurchase agreements all maturing
  within five months, and a bank notional cash-pooling programme in which *"Chubb entities may incur overdraft balances"* guaranteed up to $1,500M. [E2-54]
  coverage 16.7x; **[E3-52] is the point of the sector - $68.0bn of the liabilities have no covenants and no due dates and $21.0bn do, and reading them as one
  number is how this sector gets misjudged**. **NAMED DEATH, quantified, and the catastrophe is NOT it**: filed PML 1-in-100 $5,862M (7.9% of equity), 1-in-250
  $9,285M (12.6%) - about one year's pre-tax operating income. **The real mechanism is the reserve cushion running out as the price cycle turns**: workers'
  compensation redundancy is **entirely in accident years 2016-2020 (-19.8% to -11.0%) and absent in 2021-2024 (+0.1, +6.5, +3.8, -0.9%)** while NA Commercial
  casualty drains $481M a year, so the long-tail net of **+$110M is within $110M of flipping**; the filer's own four *"reasonably likely"* deviations sum to
  **$2,764M, 3.7% of equity and 23% of pre-tax operating income**; and the pricing half is already happening in management's own words. Modelled: combined ratio
  85.7 to **92.6**, pre-tax operating $12,000M to **$8,875M**, yield 9.13% to 6.75% - **a real possibility, and a RETURN event, not a survival event**. **[E4-40]
  turned on the filer's own model**: realised catastrophe losses averaged $2,308M over 2019-25 on a book 58% smaller at the start, which scales to about $3.3bn -
  **at or above the modelled 1-in-10 aggregate of $3,003M** - recorded as a prompt with the population mismatch stated. **Shape #7 THE LONG TAIL ON A SHORT CYCLE
  as the mechanism, with #11 THE PASS-THROUGH as a feature; #23 THE CUSHION proposed, pending the operator.** **Q5 NOT IN - QUIT ON AT THE FLOOR.** Four windows
  published per [E4-38]: pre-tax operating yield **9.13% (2025) / 8.22% (3-yr) / 7.11% (5-yr) / 6.21% (7-yr)**, a **2.92-point spread**, needing 0.87 / 1.78 /
  2.89 / 3.79%/yr of perpetual growth to reach ~10%. **ONE [E4-41] normalisation, the run's single windage: 6.9% (ten-year mean current-accident-year ratio
  applied) to 7.5% (expense ratio held, catastrophe load at the ten-year mean, loss ratio at the five-year mean) - honest pre-tax expectancy about 7%.** After
  tax 5.7-7.9%, shown because the buyer pays tax. **Value roughly $235 / $275 / $310 against $340.64: ABOVE the whole range, so the screamer test returns NO** and
  the normal method is not also used (windage count 1). **The two-component sum is reported and NOT used, with the reconciliation stated:** component 1 (investments
  at market $171,190M less minorities, less debt/hybrids/repos, less the life and annuity liabilities that are not float) **$116,540M = $302/share**, component 2
  (pre-tax ex-portfolio, including underwriting, 5-yr mean **$4,247M**, cross-checked bottom-up to within $13M) capitalised at the floor rate or the sovereign, sum
  **$412 to $537 a share - 17% to 36% ABOVE the price**. **The run explains why it is the higher number rather than choosing between them:** counting a
  3.8%-yielding bond book at market is about 26x its income while deducting none of the $68.0bn of float, and at 2.29x investments/equity that construction
  produces 1.6x book where at Berkshire's 0.45x it produces less than book - **$174 of the $302 is float that is not deducted**. **This is the exact collision the
  method's step 4 was corrected for on 2026-09-02 by the BRK run - above the bond on every construction, below the floor - and step 4 governs.** [E3-71] deferred
  tax valued and it is **nil**, because the AFS portfolio carries a $2,046M unrealised LOSS and the net position is a $429M liability. **[E5-50] third element
  MILDLY POSITIVE and stated, not converted into a number**: [E3-54] passes at **$1.50 of market value per $1 retained** ($2.71 counting buybacks), but **6.6 of
  the 15.19 points of annual return came from the multiple going 1.20x book to 1.66x, not from retention**, and [E4-44] binds. **BANDS ARMED $310 and $255, each a
  prompt for a full re-run and not a purchase, both VOID if the current-accident-year ratio exceeds 100, long-tail development turns adverse two years running, NA
  Commercial Liability adverse development exceeds $500M, or the cost of float turns positive on a five-year mean; PORTFOLIO watch row added; pre-committed SIZED
  DOWN if it ever clears.** **THE STRONGEST FACT AGAINST THE VERDICT, recorded in the run: on the sector method's own two-component sum Chubb is worth $412-$537
  against $340.64 and management says in a filed release that the stock trades below intrinsic value - the negative verdict rests entirely on preferring the
  earnings-yield floor to the sum of the parts, on a ~10% hurdle Buffett himself calls arbitrary.** **Register entry 123**, counted from this file's
  `## COMPLETED FROM THE QUEUE` heading line to `## THE WRITE-EARLY PROTOCOL` inside the fold script, before and after (122 then 123, exactly one added, no
  duplicate ticker). **PRICE US$340.64 (2026-09-18 close, `tools/sources.py`, aggregator FLAGGED) x 385,799,859 Common Shares (Q2 2026 10-Q COVER, accession
  `0000896159-26-000017`, "outstanding as of July 20, 2026") = CAP US$131,419M.** **The Swiss cover-definition trap was tested by arithmetic, not by the caption:**
  the balance sheet shows 400,120,847 issued and 385,634,049 outstanding at 2026-06-30, a 14,486,798-share treasury gap, and the cover figure sits beside the
  OUTSTANDING line - **treasury IS excluded, and using the issued figure would have overstated the cap by $4,879M.** **SOVEREIGN 5.34% USD, US Treasury daily par
  yield curve 30-year, 09/18/2026, struck fresh from the issuing authority, not FRED.** The multi-currency gap is disclosed as **unresolved** per the sector
  method's FINDING 8 - **57.0% of net premiums written is USD and 40.7% is earned abroad** (Overseas General EMEA 43% / Asia 36% / LatAm 20%, plus Life in Asia),
  with cross-currency swaps in GBP 957M, JPY 43.0bn, CHF 96M and CNH 9.3bn - and the direction of the error is stated: the JPY and EUR long rates are below the
  USD, so using the USD sovereign is the conservative choice. **PASS/FAIL: FAIL - closed at Q5 (price/floor). Q1 IN * Q2 IN (NARROW) * Q3 IN (binary gate) * Q4 IN.**
  `python tools/check_framework.py` PASSES.
"""

lines = q[:hpos].count("\n")
q2 = q[:hpos] + "## COMPLETED FROM THE QUEUE\n" + ENTRY + q[hpos + len("## COMPLETED FROM THE QUEUE\n"):]

# ---------------------------------------------------------------- STEP 2: strike CB in WAVE 6
OLD_ROW = "| CB | Chubb Limited | insurer | **RUN on the Mini Berk track**, `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md` |"
NEW_ROW = ("| ~~CB~~ | Chubb Limited | insurer | **RUN 2026-09-19 on the Mini Berk track - struck. ALL FOUR BUSINESS GATES IN; FAIL at Q5 on PRICE "
           "(quit on at the ~10% [E4-28] floor; honest pre-tax expectancy about 7%, above the bond on every construction). The first name in this queue to pass "
           "the MKL current-accident-year test outright: combined ratio including catastrophes below 100 in ten of ten years, worst 97.9. Cost of float -8.58% "
           "over five years against Berkshire's -3.6%. Price US$340.64, cap US$131,419M. Bands $310 and $255. See COMPLETED.** |")
assert q2.count(OLD_ROW) == 1, "WAVE 6 CB row not found exactly once - another session may have edited it"
q2 = q2.replace(OLD_ROW, NEW_ROW)

# ---------------------------------------------------------------- MINI BERK roster line
OLD_MB = ("business; see COMPLETED)*, ~~BN~~ *(run 2026-09-13 - FAIL at Q2, OUT on the business: a holding company, not an asset manager, "
          "and no leg carrying the weight is a franchise; see COMPLETED)*")
NEW_MB = OLD_MB + (", **~~CB~~** *(Chubb Limited, added to this track from WAVE 6 and run 2026-09-19 - the first insurer on it to clear all four business gates; "
                   "FAIL at Q5 on price, quit on at the ~10% floor; float/investments 40.3% against [E5-46]'s own 41.8%, investments/equity 2.29x, cost of float "
                   "-8.58% over five years; see COMPLETED)*")
assert q2.count(OLD_MB) == 1, "MINI BERK roster line not found exactly once"
q2 = q2.replace(OLD_MB, NEW_MB)

after, _ = register_tickers(q2)
n_after = len(after)
print("register entries AFTER:  %d" % n_after)
assert n_after == n_before + 1, "expected exactly one added, got %d" % (n_after - n_before)
assert after.count("CB") == 1, "CB appears %d times in the register" % after.count("CB")
print("OK: exactly one entry added, CB appears once. Register entry number: %d" % n_after)

# ---------------------------------------------------------------- STEP 3: the narrative fold
NARR = """
## CB (Chubb Limited) - run 2026-09-19 - Q1-Q4 IN, FAIL at Q5 on price

**WAVE 6 and the MINI BERK insurance track. `tools/sources.py:cik_for('CB')` returns
`('0000896159', 'Chubb Ltd')`; the registrant is the former ACE Ltd, renamed on 2016-01-15 after it
bought The Chubb Corporation, so the ten-year series below spans a name change and one large
acquisition, and the run says so rather than presenting it as one continuous company.**

### WHAT THIS RUN ADDS THAT THE OTHER FOUR INSURER RUNS DID NOT

**The MKL test, passed.** The Markel run of 2026-09-02 closed a name at Q2 because its
current-accident-year combined ratio was 99.3 / 101.1 / 100.3 for 2023-25, so the whole reported
underwriting profit was reserve releases. **Chubb is the first name to be put to that test over ten
years and clear it: the current-accident-year combined ratio INCLUDING catastrophes was 92.6 / 97.9
/ 93.9 / 93.4 / 97.4 / 91.9 / 90.4 / 88.6 / 88.7 / 88.2 for 2016-2025 - below 100 in every year,
worst 97.9 in the Harvey-Irma-Maria year, ten-year mean 92.3.** The 2025 releases were $1,132M of
$6,528M of underwriting income, 17%. **The series was built twice and the second construction is
not the filer's:** rebuilding it from the dollar reconciliation table rather than the published
points gives 93.33 / 97.34 / 91.86 / 90.08 / 88.40 / 88.57 / 88.22 for 2019-25, agreeing within 0.3
points in every year.

**The competitor row was EXTENDED rather than rebuilt, onto the basis that matters, and the ranking
changed.** The MKL run's seven-peer five-year reported-combined-ratio row is carried forward
unchanged; every accession in it was independently re-resolved and all five matched. Onto it:
each filer's own published favourable prior-year development, added back.

| | reported 5-yr mean | **current-accident-year 5-yr mean** |
|---|---|---|
| Kinsale | 76.66 | **80.60** |
| Arch | 82.28 | **86.99** |
| RLI | 85.52 | **93.08** |
| **Chubb** | **87.10** | **89.50** |
| W. R. Berkley | 89.92 | **89.84** |
| Fairfax | 93.72 | not comparable (IFRS 17) |
| Markel | 94.18 | **100.27** |
| Axis | 95.06 | **94.10** |

**Three findings the reported row could not produce.** (1) **RLI's headline is 6.1 to 10.8 points of
reserve releases a year; on the business it actually wrote it runs 93.08, worse than Chubb.** A run
that stopped at the reported row would have ranked Chubb behind a company it is ahead of. (2)
**Axis inverts** - its 2023 reported 99.9 contained 8.1 points of ADVERSE development, so the honest
figure was better than the headline. The basis is not a device for flattering the subject. (3)
**W. R. Berkley posts essentially zero net development three years running on a $10-12bn book
(+0.08 / -0.38 / -0.18 / +0.04 / +0.03 points), so its reported ratio needs no adjustment at all.**
Its level is 0.3 points worse than Chubb's and its presentation is the cleanest in the row. **That
is a peer finding worth carrying into any future insurer run: WRB is the reserving-integrity
benchmark of this panel, and it is not the name with the best-looking combined ratio.**

**The cost of float is the first one in this panel that is a MAJOR term.** Stage 0(b):
float/investments **40.3%**, almost exactly [E5-46]'s own 41.8% calibration point, against WTM's
22.0% where the first amendment had to write a low-side guard. So step 2 carries real weight here.
**Five-year cost of float -8.58% (-6.61 / -7.82 / -9.08 / -9.24 / -9.82%), against Berkshire's -3.6%
on the identical five years from this project's own BRK run.** On the corpus's own chosen measure of
insurer profitability **[E3-69]**, Chubb's funding is better than Berkshire's per dollar. What it
does not have is Berkshire's loss-absorption per dollar of float (float/equity 0.92x against 0.24x),
and **[E2-62]** says the method transfers and the licence to concentrate does not.

**And the second Stage 0(b) ratio is where the run had to be most careful about itself.**
Investments/equity is **2.29x - above Markel's 2.01x and five times Berkshire's 0.45x.** CONVENTION
5 exists for exactly this: at that leverage most of the portfolio is funded by liabilities and the
valuation leans on a condition [E5-46] itself calls volatile. **The two-component sum came out at
$412-$537 a share against a $340.64 price - and the run reports it, then sets it aside, and explains
why rather than choosing.** Counting a 3.8%-yielding bond book at market is roughly 26x its income
while deducting none of the $68.0bn of float; $174 of the $302 component-1 figure is float that is
not deducted; at Berkshire's 0.45x that construction produces less than book value and at Chubb's
2.29x it produces 1.6x book. **This is the precise collision the method's step 4 was corrected for
on 2026-09-02 by the BRK run - above the bond on every construction, below the floor - and step 4
governs.**

### THE REFUTED PRIORS

1. **The brief's framing that an insurer's reported underwriting profit is probably reserve
   releases. Refuted for this filer on a ten-year series, and the opposite is true:** the reserving
   bias is CONSERVATIVE in short-tail lines (ten straight years of releases) and adverse only in
   North America long-tail casualty. **Chubb releases LESS than every peer in the row except W. R.
   Berkley** (1.9-2.8 points against RLI 6.1-10.8, ACGL 3.4-8.0, KNSL 2.7-5.5, MKL 5.6-5.8).
2. **The prior that a rising expense ratio is an MKL-shaped franchise finding.** Chubb's has risen
   1.0 point off its 2022 trough, all of it in policy acquisition, attributed by the filer to
   *"changes in mix of business"* - the same shape, 9.5 points lower and half the slope. **Recorded
   as a live Q6 monitoring item, not as a Q2 failure.** Naming it and sizing it is the point.
3. **The prior that catastrophe exposure is how a large P&C insurer dies.** It is not: the filed
   1-in-250 worldwide natural-catastrophe aggregate is $9,285M, 12.6% of equity and about one year's
   pre-tax operating income. **The real mechanism is the reserve cushion and the price cycle
   stopping together**, which is a return event rather than a survival event.
4. **The prior that a cost advantage settles [E2-58]'s exception.** *"a cost advantage that is both
   wide and sustainable … By definition such exceptions are few."* Chubb's 26.6% expense ratio is
   real and it is not wide: **Kinsale, a company a thirty-third of its size, beats it by 8.9 points
   on the honest basis.** Recorded as good, not as the exception.
5. **The prior that a Swiss cover must be checked because it might report issued shares.** It was
   checked and it does NOT: the cover figure of 385,799,859 sits beside the outstanding line
   (385,634,049), not the issued line (400,120,847), a 14,486,798-share treasury gap. **Using issued
   would have overstated the cap by $4,879M. The trap did not fire, and the two minutes were still
   worth spending** - the third consecutive insurer run where the hand-read count mattered or was
   proved not to.

### THE FINDING THAT WAS NOT IN THE BRIEF

**[E4-27], the power of incentives, pointed at the pen [E2-50].** **100% of the CEO's equity award
vests on tangible book value per share growth (70%) and the REPORTED P&C combined ratio (30%),
measured relative to peers over three years - and the PSU criteria contain no catastrophe exclusion
and no prior-period-development exclusion.** Both metrics are improved by favourable reserve
development. In a sector where *"earnings can be created by the stroke of a pen"*, that is the
incentive aimed at the one number a management can write. **Five counterweights were hunted per
[E4-26] and the decisive one is the row above: the metrics are RELATIVE, and Chubb releases less
than every peer but one. The incentive points one way and the filed behaviour goes the other.** Plus
EY verifies the vesting calculation, the Committee cannot vest above actual performance, and
repurchases at 2.5x tangible book mechanically REDUCE the 70% metric - which Chubb did anyway,
$3.4bn in 2025 and $2.1bn in H1 2026.

**And the flag that fired quietly: [E2-49].** The FY2025 10-K **redefined its own leverage ratio to
exclude unrealised investment losses from total capitalisation**, improving it from 18.85% to
18.44%, after two years of large unrealised losses. It was announced with reasons in the filing that
first used it, with the prior year restated - which is [E2-49]'s candor case, not its
disposition-of-the-yardstick case. **Fired, read, worth 0.4 points, changes nothing. Worth recording
because a future reader comparing Chubb's leverage ratio across filings needs to know the basis
moved.**

### DEFECTS FOUND

**In the brief (three).** (a) It asked for the peer row on the current-accident-year basis without
noting that **most peers publish the separation only for two or three years in any one 10-K**, so
five years needs two or three filings per name; six FY2025 and five FY2023 10-Ks plus one FY2022
were pulled, and two cells remain unobtainable and are named rather than estimated. (b) It framed
Q4 around *"the cost of float across years"* as though it would be the engine - and it is, but the
brief did not say what to do when **step 2's diagnostic and step 4's floor point in opposite
directions**, which is what happened. (c) It said *"value component 1 (investments at market)"*
without flagging that at 2.29x investments/equity the float-not-deducted convention **manufactures
1.6x book**, which is the single largest number in the file and the one the run had to argue about
with itself.

**In the sector method (three, and the first is a real gap).** (1) **Step 1 has no rule for
non-float funding that is not free.** Chubb's portfolio is funded by $68.0bn of float AND $21.0bn of
debt, hybrids and repurchase agreements AND $27.7bn of life and annuity liabilities that carry
credited interest and mortality risk. [E5-46] deducts none of them because Berkshire had almost none
of them. **This run deducted debt, repos and the life liabilities from component 1 and CONFESSED the
deduction as its own judgment**; the method should say whether that is right, because at Chubb it is
worth **$142 a share**. (2) **Step 3 says "with dividends and interest from step 1 removed" and the
2025 accounting does not have a line called that.** Private-equity marks ($809M in 2025, $2,115M in
2021), equity in partially-owned entities ($1,143M) and market-risk-benefit movements all sit
outside "net investment income", and the BRK run already recorded the ASU 2016-01 version of this
problem. The run removed all of Other (income) expense, which is conservative, and said so.
(3) **The FINDING 8 multi-currency gap is still open and it bites harder here than at WTM** - 40.7%
of Chubb's premium is earned outside the US across three continents. The standing instruction was
followed (state the exposure, use the reporting currency's sovereign, disclose the choice as
unresolved) and **the direction of the error was added**: the JPY and EUR long rates are below the
USD, so the USD sovereign is the conservative choice. **A future amendment could adopt that as the
rule and it would be a one-line change.**

**In the tooling (two, both minor and neither blocking).** (i) `tools/sources.py:price()` returns a
bare `(price, date, ccy)` with no indication of the vendor, so the run can flag "aggregator" but
cannot name which one - every run on disk therefore says "aggregator, flagged" without saying whose.
(ii) `sources._chart()` returns the chart payload **unwrapped** (keys `meta`/`timestamp`/`indicators`
at the top level), while the obvious call site expects the Yahoo `{'chart': {'result': [...]}}`
shape; the first attempt to read a historical close for the [E3-54] retention test failed on
`KeyError: 'chart'`. **One docstring line would prevent it.**

### THE HONEST SUMMARY

**Chubb clears every business gate and fails on price, and the failure is a narrow one that depends
on a choice the run makes explicit.** At $340.64 the pre-tax operating earnings yield is 6.21% on a
seven-year mean, 9.13% on 2025 alone, and about 7% normalised for the hard market - above the 5.34%
long bond on every construction and below the ~10% floor on every construction. **The bands are
$310 (the floor met on 2025's record year) and $255 (the floor met on a normalised base with no
growth granted and the reserve cushion at zero).** And the strongest fact against the verdict is
recorded in the run file itself: **on the method's own sum of components Chubb is worth $412-$537 a
share, and management says in a filed release that the stock trades below intrinsic value.**
"""
lst = rd(LIST)
assert "## CB (Chubb Limited) - run 2026-09-19" not in lst, "narrative fold already present"
lst = lst.rstrip("\n") + "\n" + NARR
wr(LIST, lst)
print("narrative fold appended to the reading list (%d chars)" % len(NARR))

wr(QUEUE, q2)
print("queue written")

# ---------------------------------------------------------------- STEP 4: bands and PORTFOLIO row
al = json.load(io.open(os.path.join(ROOT, ALERTS), encoding="utf-8"))
ids = set(a["id"] for a in al["alerts"])
assert "CB-rerun-band" not in ids and "CB-floor-band" not in ids, "CB bands already armed"
n_al = len(al["alerts"])
al["alerts"].append({
    "id": "CB-rerun-band", "ticker": "CB", "currency": "USD", "op": "<=", "threshold": 310, "active": True,
    "label": ("CB at/below $310: the [E4-28] ~10% floor is met ONLY on 2025's record pre-tax operating income of $12,000M, which is above the normalised base "
              "and which management's own words call a cyclical peak (rate decreases in Large Risk and E&S property in the FY2025 10-K; soft conditions "
              "spreading to casualty in the Q2 2026 release). All four business gates IN on 2026-09-19 (Q2 NARROW: current-accident-year combined ratio "
              "including catastrophes below 100 in ten of ten years, worst 97.9; cost of float -8.58% over five years against Berkshire's -3.6%; third of "
              "seven on the honest peer basis). A prompt for a FULL v4.1 re-run in which that cyclical peak is re-tested before it is spent, NOT a purchase. "
              "VOID if any falsifier has fired: the current-accident-year combined ratio including catastrophes exceeds 100 in a year that is not a named "
              "1-in-100 catastrophe year; long-tail prior-period development turns net adverse two years running (it was +$110M favourable in 2025, +$8M in "
              "2024); North America Commercial Liability adverse development exceeds $500M in a year; the five-year cost of float turns positive. Any "
              "acquisition outside insurance or above $3bn reopens the file at Q3 before any price is read. A CEO succession announcement reopens Q2 "
              "([E4-23] is live and unanswered). Re-derive at the FY2026 10-K, expected late February 2027. Source: Test Runs/2026-09-19 Run - CB Chubb.md")})
al["alerts"].append({
    "id": "CB-floor-band", "ticker": "CB", "currency": "USD", "op": "<=", "threshold": 255, "active": True,
    "label": ("CB at/below $255: the [E4-28] floor is met on the FAIRLY NORMALISED base of about $9,800M of pre-tax operating income - the hard-market margin "
              "taken out (expense ratio held at 26.6, catastrophe load at the ten-year mean, current-accident-year loss ratio at the five-year mean), no "
              "growth granted, and the reserve cushion at zero. The band where the arithmetic works on the filed record rather than on the cycle. A ping is a "
              "prompt to re-run the gates, never an action; recompute both bands at the rate of the day and at the FY2026 10-K. The capital-allocation flag is "
              "LIVE (repurchases at 1.43x, 1.69x and 1.50x year-end book in 2023-25 and 2.5x tangible book in H1 2026, with no published repurchase condition "
              "where [E5-25] shows Berkshire publishing both as numbers), so if this name ever clears it is PRE-COMMITTED SIZED DOWN, and [E2-62] denies this "
              "balance sheet the concentration licence Berkshire's has. Note for any future re-derivation: no owner-earnings number exists for this filer - the "
              "sector method's two components plus a judgment govern, and an OCF-based yield would read 9.45% and be wrong by half. "
              "Source: Test Runs/2026-09-19 Run - CB Chubb.md")})
io.open(os.path.join(ROOT, ALERTS), "w", encoding="utf-8", newline="\n").write(json.dumps(al, indent=1, ensure_ascii=False) + "\n")
print("alerts: %d -> %d" % (n_al, len(al["alerts"])))

port = rd(PORT)
assert "| — | CB |" not in port, "PORTFOLIO row already present"
ANCHOR = "| — | GFF |"
assert port.count(ANCHOR) == 1, "PORTFOLIO anchor row not found exactly once"
ROW = ("| — | CB | 6.21–9.13 % pre-tax (four windows, 2026-09-18; normalised 6.9–7.5 %, default 7.5 %) | 5.34 % USD | "
       "**above the sovereign on every construction, +0.87 to +3.79 points; below the ~10 % floor on every construction** | "
       "**RUN DONE** (`Test Runs/2026-09-19 Run - CB Chubb.md`): **ALL FOUR BUSINESS GATES IN.** **Q2 NARROW** and the first name in this queue to pass the MKL "
       "current-accident-year test outright — combined ratio INCLUDING catastrophes below 100 in **ten of ten years** (92.6 … 88.2, worst 97.9 in 2017), so the "
       "reported underwriting profit is earned and not released; the moat is the funding, the licences and the cost base, **not** the product ([E2-70] and the "
       "filer's own over-capacity risk factor); four defects recorded — [E3-03](3) fails for the 5.3 % of premium in the federal crop programme, [E2-44] fails on "
       "its first half in the filer's own 2025–26 words, no untapped pricing power, and **key-person dependence unanswered at [E4-23]** (22 years, no named "
       "successor, 17.7 % against the chairmanship in 2026). Peer row **extended from the MKL run** onto the honest basis, where the ranking changes: CB **89.50** "
       "third of seven, ahead of WRB 89.84 and RLI 93.08 (RLI's headline 85.52 is 6–11 points of releases a year), MKL last at 100.27; WRB is the row's "
       "**reserving-integrity benchmark** at ~zero net development three years running. **Q3 IN as a binary gate**; EBITDA appears **nowhere** in any proxy, "
       "release or supplement; three flags fired and do **not** converge [E4-52] — the quarterly *double-digit growth* promise (beaten), the 2025 leverage-metric "
       "redefinition (0.4 pts, disclosed, prior year restated) and an acquisition every year; **[E4-27] is the sharpest finding and was not in the brief: 100 % of "
       "the CEO's equity vests on TBVPS growth (70 %) and the REPORTED combined ratio (30 %), with no catastrophe or prior-development exclusion — and yet Chubb "
       "releases LESS than every peer but WRB**, the incentive pointing one way and the behaviour the other. **CAPITAL-ALLOCATION FLAG LIVE** [E5-08](2). "
       "**Q4 IN**: cost of float **−8.58 %** over five years against Berkshire's −3.6 % on the same five years; float/investments 40.3 % (≈[E5-46]'s own 41.8 %) "
       "but investments/equity **2.29x**, above Markel's 2.01x, so CONVENTION 5 binds; [E5-11] 3 of 3 with $4.8bn of [E5-39] repo and overdraft funding named; the "
       "death is the reserve cushion and the price cycle stopping together (workers' comp redundancy entirely in accident years 2016–20, none in 2021–24; long-tail "
       "development $110M from flipping), a **return** event, not a survival event. **Q5 FAIL ON PRICE: quit on at the floor**; value ≈ **$235 / $275 / $310** "
       "against **$340.64**; price/book 1.74–1.78x, price/tangible book 2.58x. **The two-component sum is $412–$537 and is reported and NOT used** — $174 of the "
       "$302 component 1 is float that is not deducted, which is step 4's own collision, corrected on 2026-09-02 by the BRK run. **NOT RANKED: watch-list only; no "
       "position held and none proposed; pre-committed SIZED DOWN if it ever clears.** Bands armed **$310** (floor met on 2025's record year) and **$255** (floor "
       "met on a normalised base with no growth), each a prompt for a full re-run and **not** a purchase, both VOID if the current-accident-year ratio exceeds 100, "
       "long-tail development turns adverse two years running, NA Commercial Liability adverse development exceeds $500M, or the cost of float turns positive. "
       "Watch items: the FY2026 10-K (~late Feb 2027) for the next loss triangles, reserve sensitivity table and PML; a CEO succession announcement reopens Q2; the "
       "multi-currency sovereign question is **unresolved** (40.7 % of premium earned abroad) |\n")
port = port.replace(ANCHOR, ROW + ANCHOR, 1)
wr(PORT, port)
print("PORTFOLIO row inserted above the GFF row")

# ---------------------------------------------------------------- the shapes index
sh = rd(SHAPES)
assert "CB (2026-09-19" not in sh, "CB already in the shapes index"
OLD7 = "| 7 | **The long tail on a short cycle** | CNR (2026-09-13) | decades-long claims fixed in dollars against a years-long price cycle, the balance sheet the only buffer | |"
assert sh.count(OLD7) == 1, "shape #7 row not found exactly once"
NEW7 = OLD7[:-3] + ("| CB (2026-09-19, the mechanism, with #11 as a feature and **#23 THE CUSHION proposed**: the current accident year is genuinely profitable "
                    "(combined ratio including catastrophes below 100 in ten of ten years), but the reported line is smoothed by releasing reserves set in a "
                    "closed set of older accident years - workers' compensation redundancy is entirely in accident years 2016-2020 (-19.8% to -11.0%) and absent "
                    "in 2021-2024 (+0.1, +6.5, +3.8, -0.9%) - while North America Commercial casualty develops adversely in eight of the last nine accident years "
                    "and drains $481M a year, so long-tail net development of +$110M is $110M from flipping at the same moment the price cycle turns (property "
                    "rate down in 2025 and softness spreading to casualty in 2026, on management's own statement) |")
sh = sh.replace(OLD7, NEW7)
OLD22 = "| 22 | **The habit** *(proposed, pending the operator)* | KO (2026-09-19) |"
assert sh.count(OLD22) == 1, "shape #22 row not found exactly once"
ROW23 = ("\n| 23 | **The cushion** *(proposed, pending the operator)* | CB (2026-09-19) | the underwriting profit is real on the year's own business, but the "
         "reported line is smoothed by releasing reserve redundancy concentrated in a closed and identifiable set of older accident years; that redundancy is "
         "non-renewable and is already exhausted in the newer years, so the reported ratio converges upward to the current-accident-year ratio - and it does so at "
         "the same moment the price cycle turns against the current accident year, with no deterioration in the business itself | |")
# insert row 23 after the row 22 line
i22 = sh.index(OLD22)
eol = sh.index("\n", i22)
sh = sh[:eol] + ROW23 + sh[eol:]
OPEN_ANCHOR = "**All ten are listed so briefs count correctly; none is settled.**"
assert sh.count(OPEN_ANCHOR) == 1, "shapes Open paragraph anchor not found"
sh = sh.replace(OPEN_ANCHOR, ("CB proposed **#23 THE CUSHION** (2026-09-19), arguing it is neither #7 nor #11: #7 is a long-tail liability that can outrun the "
                              "pricing cycle and kill the company (CNR's case, where the balance sheet is the only buffer), whereas **#23 is not lethal at all** - "
                              "it is a depleting ACCOUNTING cushion whose exhaustion changes the reported number without changing the business, and it is the "
                              "class mechanism for every well-reserved insurer, which is why it is worth a number; #7 is named as CB's mechanism and #11 as its "
                              "feature in the meantime. **All eleven are listed so briefs count correctly; none is settled.**"))
wr(SHAPES, sh)
print("shapes index: #7 extended with CB, #23 THE CUSHION proposed, Open paragraph updated")
print("\nREGISTER ENTRY NUMBER FOR CB: %d" % n_after)
