# BLK FOLD - all six steps, one read-modify-write per file, immediately before the commit.
# Counts the register entries between the last LINE-ANCHORED "## COMPLETED FROM THE QUEUE"
# heading and "## THE WRITE-EARLY PROTOCOL" BEFORE and AFTER, and asserts exactly one added.
#
# TWO DEFECTS FOUND AND FIXED INSIDE THIS SCRIPT ON 2026-09-19, recorded rather than silently
# corrected:
#   (1) rindex() on the bare heading string lands on an INLINE mention of the heading name -
#       there are several inside register entries and one inside the FOLD section, which sits
#       AFTER the WRITE-EARLY heading, so the window search then failed outright. Headings are
#       now matched line-anchored.
#   (2) percent-formatting of the entry text is impossible here: the text is full of literal
#       per-cent signs. All substitution is by named token replacement.
import io, os, re

ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
Q = os.path.join(ROOT, "Screens", "WATCHLIST RUN QUEUE.md")
RL = os.path.join(ROOT, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
OL = os.path.join(ROOT, "Screens", "_daily", "OVERNIGHT LOG.md")
SH = os.path.join(ROOT, "Screens", "SURVIVAL SHAPES - index.md")
CLOCK = "2026-09-19 15:32 EDT"


def count_entries(text):
    hs = [m.start() for m in re.finditer(r"(?m)^## COMPLETED FROM THE QUEUE\s*$", text)]
    assert hs, "no COMPLETED heading found"
    h = hs[-1]
    ws = [m.start() for m in re.finditer(r"(?m)^## THE WRITE-EARLY PROTOCOL", text) if m.start() > h]
    assert ws, "no WRITE-EARLY heading after the COMPLETED heading"
    return len(re.findall(r"(?m)^- \*\*", text[h:ws[0]])), h, ws[0]


def sub(text, **kw):
    for k, v in kw.items():
        text = text.replace("__" + k + "__", str(v))
    assert "__" not in text.replace("__", "__", 0) or True
    return text


# ---------- STEP 1 and STEP 2 ----------
q = io.open(Q, encoding="utf-8").read()
before, h, w = count_entries(q)
print("register entries BEFORE:", before)
mine = before + 1

ENTRY_T = (
"- **BLK (BlackRock, Inc.), 2026-09-19 - FAIL at Q2, OUT on the business (Q3, Q4 and Q6 RECORDED, "
"NOT GOVERNING; Q5 headed COMPUTATION - NOT A CLEARANCE and below the floor).** **WAVE 6**, the "
"asset manager held as BLOCKED until the BAM precedent of 2026-09-13 made it measurable. "
"**THE REGISTRANT, and the CIK's history does NOT span both:** `cik_for('BLK')` returns **CIK "
"0002012383**, whose `formerNames` row reads *BlackRock Funding, Inc. /DE*; it became the parent in "
"**October 2024** at the GIP closing, and its `companyfacts` therefore begins at **FY2024** (288 "
"tags). The 2009-2023 history sits under **CIK 0001364742**, today named **BlackRock Finance, Inc.** "
"(557 tags), whose last 10-K was FY2023 `0000950170-24-019271`. **A single-CIK XBRL pull on BLK "
"returns two years and no error** - the same defect class as `level_shift` and `working_capital_flag`, "
"a diagnostic that never reaches the reader; `name_change_note()` returned an empty string. Both "
"companies are co-obligors and the 10-K publishes combined Obligor Group financials. Five filings "
"read in full: 10-K FY2025 `0001193125-26-071966`, 10-Q Q2 2026 `0001193125-26-337177`, 10-Q Q2 2025 "
"`0000950170-25-103780`, 10-K FY2023 `0000950170-24-019271`, 10-K FY2022 `0000950170-23-004343`, plus "
"the 8-K EX-99.1 of 2026-07-15 `0001193125-26-304013` and the proxy `0001308179-26-000262`. "
"**Q1 IN:** 15.22bp on $12.6tn of average AUM is 79.2% of revenue; Aladdin 8.2%; capex 1.5% of "
"revenue; and the two non-owner columns of the balance sheet are separated by the filer itself. "
"**Q2 OUT ON ONE FILED PRICE, and it is the sharpest criterion-2 refutation in the register: "
"iShares Core S&P 500 (IVV) charges 0.03% and Vanguard 500 Index Fund ETF Shares (VOO) charges "
"0.03%, identical to the basis point in the 2021 AND the 2026 prospectuses** (iShares Trust 485BPOS "
"`0001193125-26-318131` and `0001193125-21-223259`; Vanguard Index Funds `0000036405-26-000181` and "
"`0001683863-21-002763`; SPY 0.0945% in both years, `0001193125-26-022316` and "
"`0001193125-21-008848`), **and the rival is structurally incapable of needing a margin, because "
"Vanguard's manager is owned by the funds it manages.** The decisive series, recomputed from four "
"10-Ks and a 10-Q and NOT inherited from the committed BAM row - the effective fee rate on the "
"filer's own thirteen-month average AUM: **TOTAL 16.29 / 16.15 / 15.62 / 14.90 / 15.22bp for "
"2021-2025 and 15.25 annualised in H1 2026 (-6.6%), and EVERY organically owned product fell - ETFs "
"20.41 to 16.92 (-17.1%), active equity 55.14 to 43.65 (-20.8%), active fixed income 20.79 to 17.06 "
"(-18.0%), active multi-asset 19.21 to 12.42 (-35.4%), non-ETF index 3.83 to 3.52 (-8.1%).** The "
"only two lines that rose are cash management, where 2021's 6.61bp is a zero-rate fee-waiver "
"artefact and the series has fallen since 2023 (13.05, 13.01, 12.76, 12.72), and private markets "
"+27.5%, **which rose because GIP and HPS were bought**. **Ex private markets the total fell 15.74 to "
"13.64bp, -13.4%**: the flat blended rate is a mix effect purchased for **$28.3bn in twenty-one "
"months - GIP $12,949M, Preqin $3,123M, HPS $12,221M - of which $22.0bn was paid in the company's "
"own shares and units, with $8,429M of contingent consideration still to come (GIP 4.0-5.2M shares, "
"HPS 2.8-4.4M Subco Units): up to 25.0M shares and units, 15.4% of the count**, against $1.6bn a "
"year of buyback. Goodwill and intangibles went $33,643M to **$63,251M against equity of $55,888M - "
"tangible equity is NEGATIVE $7,363M** from +$4,101M three years earlier, so **[E2-43]'s denominator "
"cannot be computed at all**. The second reading needs no rate: **AUM +40.3% over four years against "
"base fees +25.7%, so revenue grew 14.6 points slower than the assets it is charged on** - [E4-55] "
"inverted, volume flattering the dollars while the price per unit falls. The filer says it in Item 1A, "
"and the word to notice is *additional*: *\"may lead to additional fee compression ... including "
"competition leading to fee reductions on existing or new business\"* - a business with no close "
"substitute has no first instalment to add to. And in Item 1: *\"Key competitive factors include ... "
"the efficient delivery of beta for index products, investment style and discipline, price\"*. And "
"about a third of its assets, in the MD&A: *\"institutional non-ETF index assignments ... typically "
"reflect low fee rates\"* - 29.8% of average AUM, 6.9% of base fees, 3.52bp. **Competitor row: one "
"specification, eight lines, six filing-sourced competitors, and all of them falling** - STT 5.40 to "
"4.62bp (my computation: STT publishes neither a rate nor an average AUM, `0000093751-26-000124`), "
"IVZ gross yield 48.7 to 33.7 and net yield ex performance fees to 23.0 on a definition it changed "
"in FY2025 (`0000914208-26-000079`), TROW's own EFR ex performance fees 42.6 to 39.4 "
"(`0001628280-26-008002`), BEN's own rate 41.8 to 40.5 on a September year (`0000038777-25-000238`), "
"and BX 92.2 / BAM 85.8 carried from the committed BAM row and **flagged as not recomputed**. Every "
"peer figure was re-read in the filing text by this session. **Vanguard was resolved BETTER than as "
"an absence** - its funds file with the SEC, so the substitute's price is primary evidence; "
"**Fidelity and Amundi are named UNRESEARCHED with their artifacts** (the Fidelity Concord Street "
"Trust 485BPOS fee table for the ZERO funds, CIK 0000819118, four 2026 accessions located and none "
"carrying the prospectus fee tables; Amundi's English-language Universal Registration Document), "
"**and the class is NOT held PROVISIONAL, because both can only push the same way**. [E4-36] places "
"the record in the fourth cause, **wave-riding [E3-51]**, and [E3-62]'s second step answers where the "
"scale gains went: **ETF average AUM +60.3% while the ETF price fell 17.1%**. [E2-53] is the sharpest "
"single line: **the largest asset manager that has ever existed does not set its own price.** "
"**Q3 IN, recorded not governing** - declared a **BINARY GATE** on [E2-70] (an undifferentiated "
"product whose *\"only products are promises\"* magnifies the manager), leverage NOT ticked at 0.23x, "
"control not ticked. No disqualifier found; the one named matter is the thirteen state Attorneys "
"General antitrust suit against BlackRock, State Street and Vanguard, where *\"In 2025, the court "
"largely denied defendants' motion to dismiss\"* - read under [E5-22], recorded as a matter to watch, "
"not a verdict. **[E4-29] reads CLEAN on the EBITDA limb and the count is given: `grep -c -i ebitda` "
"= 0 in the 10-K, 0 in the furnished 8-K EX-99.1 and 0 in the proxy** - the CGNX companion rule was "
"followed and all three were pulled - **and fires at full strength on the adjusted-earnings limb**: "
"the release headline is *\"Diluted EPS of $12.19, or $13.91 as adjusted\"*, \"as adjusted\" appears "
"35 times in it, FY2025 GAAP diluted EPS $35.31 against $48.09 as adjusted (**a $12.78 gap, 36.2%, "
"nine times the $1.60 gap of 2024**), GAAP operating margin 37.1% to 29.1% while adjusted held 44.5% "
"to 44.1% on **$2,555M of add-backs against $536M** - including **$738M of acquisition-related "
"COMPENSATION**, which [E3-53] and [E5-33] say is a real cost - and a denominator cut from $24,216M "
"to $21,756M. **The 10-K states the Company uses that margin *\"to determine the long-term and annual "
"compensation of the Company's senior-level employees\"*: the pay metric is the metric that excludes "
"the cost of the acquisitions [E4-27].** **The single sharpest finding in the file is [E3-50]: the "
"2025 NEO Pre-Set Performance Scorecard scores *\"Next 12-Month P/E Multiple (including relative "
"premium)\"* and *\"Total Shareholder Return\"* as financial-performance measures** - the premise the "
"corpus *\"adamantly disagree[s]\"* with, formalised into a pay formula, and [E3-50] names the next "
"step. **[E2-01] runs both ways at once: GAAP return on average equity 16.2 / 13.7 / 14.3 / 14.7 / "
"10.7% and GAAP EPS $42.01 to $35.31, while adjusted EPS rose 10% and the CEO was rated *Far Exceeds* "
"with $45.0M of pay, the incentive up 24%.** [E4-30] does NOT fire (cash tax 33.3 / 17.0 / 19.5 / "
"20.5 / **30.2%** of pretax income, rising, and above the 22.0% book rate in 2025; operating income "
"visibly lumpy), and weak accounting and unintelligible footnotes do not fire either - **the filer "
"publishes its own separations, which is the strongest [E2-26] pass available.** The credit is "
"recorded as plainly as the flags: **BlackRock prints the BPIP payout matrix in advance and reports "
"the prior cycle's outturn against its own pre-set target - $716M of average annual organic revenue "
"growth against a $640M target and 43.4% against 41.5%, payout 116.6% - which is [E2-49]'s *pre-set, "
"long-lived and small bullseyes* and the [E3-48] artifact done well.** Against it: the "
"adjusted-margin bullseye was RAISED from 41.5% to 44.0% while the GAAP margin fell eight points. "
"Institutional imperative 3 of 4 ([E2-30](2) $28.3bn soaking up the funds after a decade of small "
"deals; (3) both earn-out fair values *\"determined ... with the assistance of a third-party "
"valuation specialist\"*, against [E3-58]; (4) every large traditional manager bought private markets "
"in the same window). **CAPITAL-ALLOCATION FLAG LIVE:** 1.6M shares and equivalents for about $1.6bn "
"in 2025, the Q4 Item 5 table at an average of **$1,073.40**, against an owner-earnings yield of "
"2.7-3.0%; and the 2026 programme is announced as a **dollar quantity** (*\"increasing planned "
"quarterly share repurchases to $550 million\"*, *\"$2 billion\"*), which is [E5-24] inverted and the "
"opposite of [E5-25], where Berkshire published both conditions as numbers in advance. Stated with "
"[E4-13]. **Q4 IN, recorded not governing. The consolidated funds were separated using the filer's "
"OWN reconciliation, and the reported line is unusable: GAAP operating cash of $3,927M in 2025 "
"understates the owner's cash by $3,536M**, because the CIPs' securities purchases (-$4,214M) sit in "
"OPERATING while the outside investors' subscriptions (+$3,827M) sit in FINANCING. Ex-CIP operating "
"cash: **6,168 / 5,668 / 5,684 / 7,267 / 7,463** for 2021-2025, and total assets fall from $169,998M "
"to **$98,763M** once the CIP and separate-account columns are removed ($68,020M of separate-account "
"assets matched dollar for dollar by an identical liability). **H1 is not annualisable: H1-2025 "
"ex-CIP operating cash was $1,979M against $7,463M for the year, 26.5%**, because year-end incentive "
"compensation is accrued through the year and paid in Q1; the TTM to 2026-06-30 is $8,590M and is "
"reported, not used. **Owner earnings $4,756M-$5,583M across both windows and both ends of (c), a "
"17.4% band whose window spread is only 0.8% - there is no distorted year.** **(c) is a disclosed "
"judgment and the corpus default runs BACKWARDS here: 68.8% of 2025 D&A ($775M of $1,126M) is "
"amortisation of intangibles acquired in GIP, Preqin and HPS - the write-off of a purchase price "
"already paid in shares already sitting in the 160.9M denominator - so (c) is judged at the capex end "
"($369.6M five-year mean) and the D&A end ($593.0M) is displayed as the alternative rather than "
"declared invalid.** A THIRD end is quantified and explicitly NOT adopted: if the whole acquisition "
"programme is maintenance, (c) rises $4,465M a year and owner earnings fall to **$291M** - and that "
"is where a future reader would reopen this file. **SBC RESOLVES and is COMPLETE and is taken at the "
"[E3-70] grant-value measure, which exceeds the charge in ALL FIVE years** (2025 $1,807M against "
"$1,307M, +38%; 2024 $1,379M against $753M, +83%). **The finding the total hides: owner earnings PER "
"SHARE peaked at $35.02 in 2024 (c=D&A), fell 19.6% to $28.15 in 2025, and are 12.5% BELOW 2021 - or "
"flat at the capex end, $32.65 to $32.82 - on 40.3% more AUM.** **Good, not great [E4-20]**, because "
"the rate is falling and not rising, and [E4-43] passes the good class. All three [E5-11] strengths "
"pass: base fees fell only 5.3% in 2022, own cash $11,007M with the $5,900M revolver NOT counted "
"[E5-39], earliest maturity $700M in March 2027 on a ladder to 2055, interest covered **11.5x** out "
"of cash flow net of capex [E2-54], and **the $8,429M earn-out is payable in SHARES AND UNITS, not "
"cash - [E3-52]'s animal turned into an earn-out, a severe dilution item and a trivial solvency "
"one.** [E2-60] recorded as a caution: 2025 distributions of $5,298M against owner earnings of "
"$4,530-5,281M, so the acquisition programme is funded in paper because the cash is committed. "
"**Shape #11 THE PASS-THROUGH, with a new shape PROPOSED, argued and numbered at the fold: "
"#__NEXTN__ THE BOUGHT AVERAGE.** The named death is quantified three ways [E3-24, E4-40]: the "
"pass-through (already happening, not a forecast); a market fall (equity is 57.9% of AUM, and equity "
"-40% with everything else -10% takes base fees to $16,961M, -11.6%, still above 2021 - a real "
"possibility, a poor decade and not an impairment); and **the one balance-sheet mechanism an investor "
"in a capital-light manager would not think to look for, the securities-lending indemnity: $353bn on "
"loan against $375bn of collateral (106.2%, minimum 102-112%), where a 15% shortfall on a fifth of "
"the book is $10,590M, 18.9% of equity and 191% of a year's net income** - modelled as exposure and "
"not experience, at a low-level possibility, with the filer's *\"was not material\"* quoted. Dilution "
"is the one certainty: up to 9.6M more units, +5.9%, and the earn-out was revalued **upward by $720M** "
"in 2025. **Q5 DID NOT OPEN.** Below-gate computation: owner-earnings yield **2.74-3.21%** against a "
"**5.34%** sovereign, so the owner is paid **MINUS 2.60 to MINUS 2.13 points against the government "
"bond**; honest pre-tax expectancy **3.51-4.12%** against the ~10% floor, a shortfall of **5.9 to 6.5 "
"points**, needing **5.88-6.49% growth in owner earnings per share forever** against a four-year "
"record of zero [E4-35, E4-44]; value roughly **$550-650** at the bare sovereign and **$875-1,030** "
"with 2% perpetual growth allowed, so **the price is above the whole range** - the third outcome of "
"the screamer test [E4-01]; windage ONE, applied at Q4. **What the buyer is paying for, in words: "
"1.13% of $15.3 trillion of other people's savings for the right to earn 0.152% a year on it - nine "
"years of gross base fees just to return the purchase price - of which about $450 a share, some "
"$73bn, is an option on the stated *\"ambition to raise $400 billion in private markets by 2030\"* at "
"ninety basis points instead of fifteen, and on Aladdin compounding from 8.2% of revenue.** "
"**Aladdin, which the brief flagged as the part that might behave unlike the rest, is half "
"different**: long-term recurring contracts and 16% organic ACV growth, but its fees are *\"generally "
"determined using the value of positions on the Aladdin platform\"* - market-linked like everything "
"else - and at $1,981M it is 8.2% of revenue, too small to reclassify the other 91.8%. **Nothing "
"armed: no `alerts.json` band and no `PORTFOLIO.md` row, because a Q2 failure is a failure on the "
"BUSINESS (the QLYS ruling of 2026-09-07); the reopening conditions are six filed series with two- "
"and three-consecutive-year thresholds pre-committed at Q6 [E1-02].** **The strongest single fact "
"AGAINST this verdict, recorded [E4-26, E4-51]: iShares crossed $6 trillion and roughly doubled in "
"three years at the same 0.03% as Vanguard, so buyers are choosing BlackRock for something that is "
"not price and is not in my fee-rate series.** **Register entry __MINE__**, counted from this file's "
"`## COMPLETED FROM THE QUEUE` heading line to `## THE WRITE-EARLY PROTOCOL` inside the fold script, "
"**__BEFORE__ before and __MINE2__ after, exactly one added, no duplicate** - and the brief's own "
"count was stale again, as it was for IBM, DIS and USAR. Two tooling defects: "
"**`tools/sources.py:_get()` defaults to `WEB_UA` = Mozilla/5.0 and `www.sec.gov/Archives` answers it "
"with HTTP 403** - every primary fetch failed until `headers=SEC_UA` was passed, and the default is "
"wrong for the rung the framework uses most - and the CIK-history trap above. Two further defects "
"were found and fixed inside the fold script itself and are recorded in its header: `rindex()` on the "
"heading name lands on an inline mention, and percent-formatting cannot be used on text full of "
"per-cent signs. 108 distinct ledger ids cited, all 108 verified against the 267-row ledger, zero "
"phantom; `check_framework.py` PASS. **Price US$1,069.78 (2026-09-18 close, `tools/sources.py "
"price()`, aggregator FLAGGED, order-of-magnitude cross-checked against the 10-K's own *\"a closing "
"stock price of $1,070\"*) x 162,476,186 shares (154,869,259 common + 7,606,927 Class B-2 Subco "
"Units, exchangeable one-for-one, from the 10-Q cover *\"As of July 31, 2026\"*, accession "
"`0001193125-26-337177`; split factor after 2026-06-30 = 1.0) = cap US$173,814M; on common stock "
"alone US$165,676M. Sovereign 5.34% USD, US Treasury 30-year par yield, 09/18/2026, struck fresh, "
"not FRED.**"
)

shape_next = None  # resolved below, before the entry is written
sh_probe = io.open(SH, encoding="utf-8").read()
shape_next = max(int(n) for n in re.findall(r"(?m)^\| (\d+) \|", sh_probe)) + 1
print("shapes on disk:", shape_next - 1, "-> new shape number", shape_next)

ENTRY = sub(ENTRY_T, MINE=mine, MINE2=mine, BEFORE=before, NEXTN=shape_next)
assert "__" not in ENTRY, "unsubstituted token left in the register entry"

HEAD = "## COMPLETED FROM THE QUEUE\n"
q2 = q[:h] + HEAD + ENTRY + "\n" + q[h + len(HEAD):]

old_row = ("| BLK | BlackRock, Inc. | asset manager | **RUN**, on the BAM precedent (2026-09-13): "
           "an asset manager is measurable from its filings, and \"blocked\" is not a verdict |")
new_row = sub(
    "| ~~BLK~~ | BlackRock, Inc. | asset manager | **RUN 2026-09-19 - struck. FAIL at Q2, OUT on the "
    "business: iShares Core S&P 500 charges 0.03% and Vanguard's VOO charges 0.03%, identical in the "
    "2021 and the 2026 prospectuses, and every organically owned fee rate fell 2021-2025 (ETFs "
    "-17.1%, active equity -20.8%, active fixed income -18.0%, active multi-asset -35.4%, non-ETF "
    "index -8.1%); the blended 15.22bp held only because $28.3bn, $22.0bn of it in own shares and "
    "units, bought a higher-priced private-markets book. Owner earnings per share flat to -12.5% on "
    "40.3% more AUM. Price US$1,069.78, cap US$173,814M. Register entry __MINE__. See COMPLETED.** |",
    MINE=mine)
assert old_row in q2, "WAVE 6 BLK row not found"
q2 = q2.replace(old_row, new_row, 1)

after, _, _ = count_entries(q2)
print("register entries AFTER:", after)
assert after == before + 1, "count did not increase by exactly one: %s -> %s" % (before, after)
assert q2.count("BLK (BlackRock, Inc.), 2026-09-19") == 1, "duplicate BLK register entry"
io.open(Q, "w", encoding="utf-8").write(q2)
print("STEP 1 and STEP 2 done; this run is register entry", mine)

# ---------- STEP 3 : the narrative fold ----------
rl = io.open(RL, encoding="utf-8").read()
NARR = """

## BLK (BlackRock, Inc.) - run 2026-09-19 - Q1 IN, **Q2 OUT on the business**

**What this run adds that no earlier run in this project could.** BAM (2026-09-13) closed at Q2
because a fee rate fell eight basis points in two and a half years. **BLK closes at Q2 because the
substitute's price is published in a competing prospectus and is identical to the basis point.**
iShares Core S&P 500 (IVV) charges **0.03%**; Vanguard 500 Index Fund ETF Shares (VOO) charges
**0.03%**; both figures appear in the 2021 and in the 2026 485BPOS filings, unchanged. SPY charges
0.0945%, capped by waiver. **[E3-03] criterion 2 - "thought by its customers to have no close
substitute" - is refuted by two documents a customer can read in a minute**, and the rival is
structurally incapable of needing a margin, because Vanguard's manager is owned by the funds it
manages. This is the first run in the register where criterion 2 fails on a *filed price of the
substitute* rather than on an inference from the subject's own numbers.

**The decisive series, and it was recomputed rather than inherited.** The effective fee rate on the
filer's own thirteen-month average AUM, from four 10-Ks and a 10-Q:

| bp | 2021 | 2022 | 2023 | 2024 | 2025 | H1-26 ann. |
|---|---|---|---|---|---|---|
| TOTAL | 16.29 | 16.15 | 15.62 | 14.90 | 15.22 | 15.25 |
| ETFs | 20.41 | 19.21 | 18.48 | 17.31 | 16.92 | 17.14 |
| active equity | 55.14 | 50.38 | 48.82 | 46.93 | 43.65 | 42.02 |
| active fixed income | 20.79 | 19.44 | 17.55 | 17.23 | 17.06 | 16.95 |
| active multi-asset | 19.21 | 17.94 | 15.28 | 13.55 | 12.42 | 12.03 |
| non-ETF index | 3.83 | 3.80 | 3.79 | 3.52 | 3.52 | 3.47 |
| private markets | 70.49 | 66.71 | 69.64 | 77.36 | **89.85** | 80.06 |
| cash management | 6.61 | 12.01 | 13.05 | 13.01 | 12.76 | 12.72 |

**Every organically owned line fell. The only two that rose did not rise on price:** cash
management's 2021 figure is a zero-rate fee-waiver artefact and the series has fallen since 2023;
private markets rose because **GIP and HPS were bought**. **Ex private markets the total fell 15.74
to 13.64bp.**

### THE REFUTED PRIORS
1. **"BlackRock is the cheapest manager on the row, so the row shows its strength."** Wrong question.
   15.22bp against TROW's 39.4 and BEN's 40.5 is a fact about *product mix*, not about franchise. What
   the row actually shows is **six independent filers, with six different definitions and six
   different fiscal calendars, all falling at once**: STT -14.4%, IVZ -30.8% on its own gross yield,
   TROW -11.3% ex performance fees, BEN -3.1%, BAM -8bp, BLK -6.6%. A franchise is a claim about the
   customer's alternatives, and the customer is getting a better price every year from everybody.
2. **"The blended rate has been flat for two years, so the compression is over."** It is flat because
   $28.3bn bought a 90bp book. Strip it and the rate fell 13.4% over four years.
3. **"Scale is the moat."** [E3-62]'s second step decides it: ETF average AUM **+60.3%** while the ETF
   price fell **17.1%**. The savings went home to the customer. An advantage that shows up as volume
   at a price you cannot raise is scale, not franchise.
4. **"An asset manager's reported operating cash flow is its owner's cash."** Not for a fund
   consolidator. **GAAP operating cash of $3,927M in 2025 understates the owner's cash by $3,536M**,
   because the consolidated funds' securities purchases sit in OPERATING while the outside investors'
   subscriptions sit in FINANCING. The filer publishes the separation; the run used it.
5. **"D&A is the conservative end of (c)."** Here it is the *wrong* end: **68.8% of 2025 D&A is
   amortisation of intangibles bought in GIP, Preqin and HPS** - a purchase price already paid in
   shares that are already in the share count. The corpus default [E3-44] runs backwards for a serial
   acquirer of intangible-heavy businesses, and this is the third instance in three days of a D&A tag
   misreading a filer, after IBM's lease ROU amortisation and DIS's TFCF/Hulu amortisation.

### THE FINDING THAT WAS NOT IN THE BRIEF
**The pay scorecard.** The 2026 proxy prints the "2025 NEO Pre-Set Performance Scorecard", and under
*Financial Performance - Priority 1: Drive profitable growth* the scored measures begin: **"Next
12-Month P/E Multiple (including relative premium)"** and **"Total Shareholder Return"**. **[E3-50]**
describes exactly the premise the corpus *"adamantly disagree[s]"* with - that a manager's job is to
encourage the highest stock price possible - and names the next step, *"unadmirable accounting
stratagems"*. **Writing the forward price/earnings multiple, and the relative premium to peers, into
the CEO's pre-set pay formula is that premise formalised.** It converges with three other flags
[E4-52]: an adjusted-EPS gap that grew from $1.60 to **$12.78** in one year; the same adjusted
operating margin being the metric the 10-K says is used *"to determine the long-term and annual
compensation of the Company's senior-level employees"*, while it adds back **$738M of compensation
paid to retain the people the company bought**; and a buyback announced as a **dollar quantity**
rather than as a price condition. GAAP return on average equity fell 14.7% to 10.7% and GAAP EPS fell
$42.01 to $35.31, while adjusted EPS rose 10% and the CEO was rated *Far Exceeds* with $45.0M of pay,
the incentive up 24%. **[E2-01] was written to prefer the first number.**

**And the credit, recorded as plainly:** BlackRock prints the BPIP payout matrix in advance and
reports the prior cycle's outturn against its own pre-set target - **$716M of average annual organic
revenue growth against a $640M target, 43.4% against 41.5%, payout 116.6%**. That is **[E2-49]**'s
*pre-set, long-lived and small bullseyes* and the **[E3-48]** artifact done properly. Against it: the
adjusted-margin bullseye was **raised from 41.5% to 44.0% while the GAAP margin fell eight points**.

### DEFECTS FOUND
1. **`tools/sources.py:_get()` defaults to `WEB_UA` = `Mozilla/5.0`, and `www.sec.gov/Archives`
   answers it with HTTP 403.** Every primary-document fetch in this run failed until `headers=SEC_UA`
   was passed. The default is wrong for the rung of the evidence ladder the framework uses most.
   **Fix: default to `SEC_UA` for any `sec.gov` host.** Changes no number; removes a trap that costs
   every new run a failed call.
2. **`cik_for("BLK")` returns the right CIK and a two-year history, silently.** CIK 0002012383 files
   today and its `companyfacts` begins at **FY2024**, because the holding company was created in
   October 2024 at the GIP closing; 2009-2023 sits under CIK 0001364742, now **BlackRock Finance,
   Inc.** `name_change_note()` returned an **empty string**. A single-CIK XBRL pull returns two years
   and no error - the same defect class as `level_shift` and `working_capital_flag`: a diagnostic that
   never reaches the reader. **Fix: fire `name_change_note()` on a `formerNames` entry that differs in
   corporate form, or have `annual()` refuse when fewer than five annual periods resolve.**
3. **The brief's instruction to find the CIK myself was load-bearing.** Any run that had taken a CIK
   from a brief would have built a two-year series for a seventeen-year filer.
4. **Two defects in the fold script itself, found and fixed while folding and recorded in its
   header.** `rindex()` on the string "## COMPLETED FROM THE QUEUE" lands on an inline mention - there
   are several inside register entries and one inside the FOLD section, which sits AFTER the
   WRITE-EARLY heading, so the window search then failed outright; headings must be matched
   line-anchored. And percent-formatting cannot be used to build a register entry, because the text is
   full of literal per-cent signs. **Any session copying a prior fold script inherits both.**
5. **Delegating the competitor row to a helper agent exhausted the session limit**, and only the
   write-early rule saved the partial peer file. The coordinator's correction - fetch peer data
   in-session - is the right rule for a run this size. **Every figure in the recovered peer file was
   re-read in the filing text by this session before use**, and the six ETF prospectus accessions were
   recovered by matching on-disk file sizes against EDGAR's own filing indexes.
6. **No defect in the brief's framing of the fee-rate test.** It named the decisive series before the
   data was pulled and the data confirmed it. The instruction *not* to inherit BAM's conclusions
   mattered: the two managers reach the same verdict for different reasons - BAM's rate falls on
   related-party mix, BlackRock's on customer substitution at a commodity price.

### ONE THING TO KEEP
**Aladdin is the only part of this company that is not a commodity, and it is 8.2% of revenue.** The
brief was right that it might behave differently, and half right about how: the contracts are
long-term and recurring and organic ACV grew 16%, but the fees are *"generally determined using the
value of positions on the Aladdin platform"* - market-linked like everything else. At $1,981M it
cannot reclassify the other 91.8%. **If Aladdin ever exceeds a fifth of revenue with organic ACV
growth above 15%, this file should be run again from Q1** - that is refutation test 6 at Q6.

### THE HONEST SUMMARY
**This is a very good business and it is not a franchise.** It survives everything Q4 can model,
earns a high return on the tangible capital it uses, consumes no capital to grow, and has the most
reliable revenue line in the queue. **And owner earnings per share are flat to 12.5% lower than four
years ago on 40.3% more assets under management.** At $1,069.78 the buyer pays 1.13% of the $15.3
trillion for the right to earn 0.152% a year on it, which is nine years of gross fees before a single
cost. The owner-earnings yield is **2.74-3.21% against a 5.34% government bond**, and the honest
pre-tax expectancy of **3.51-4.12%** misses the ~10% floor by **five and a half to six and a half
points**. **[E2-53]** is the line to remember: *"Once dominant, the newspaper itself, not the
marketplace, determines just how good or how bad the paper will be."* **The largest asset manager
that has ever existed does not determine its own price.**
"""
io.open(RL, "w", encoding="utf-8").write(rl.rstrip("\n") + "\n" + NARR)
print("STEP 3 done")

# ---------- the survival shapes index ----------
sh = io.open(SH, encoding="utf-8").read()
nums = [int(n) for n in re.findall(r"(?m)^\| (\d+) \|", sh)]
assert max(nums) + 1 == shape_next, "the shapes index moved between the probe and the write"

m = re.search(r"(?m)^\| 11 \| \*\*The pass-through\*\*.*$", sh)
assert m, "shape 11 row not found"
row11 = m.group(0)
add11 = sub(
    " BLK (2026-09-19, the mechanism, with #__NEXTN__ proposed as the concealment: ETF average AUM "
    "+60.3% from 2021 to 2025 while the ETF effective fee rate fell 17.1% (20.41 to 16.92bp), total "
    "AUM +40.3% against base fees +25.7%, and owner earnings per share flat to -12.5%; the savings "
    "went home to the customer, and [E3-62]'s second step is answered by the filer's own price table)",
    NEXTN=shape_next)
assert row11.endswith("|")
sh = sh.replace(row11, row11[:-1].rstrip() + "," + add11 + " |", 1)

lastrow = re.findall(r"(?m)^\| %d \| .*$" % max(nums), sh)[-1]
newrow = sub(
    "| __NEXTN__ | **The bought average** *(proposed, pending the operator)* | BLK (2026-09-19) | the "
    "price of everything the business already owns falls every year, and the owner buys higher-priced "
    "businesses with its own shares so that the blended price stands still; the decline is invisible "
    "in the headline while the share count and the goodwill rise, and the owner pays for the "
    "appearance of stability in dilution | |", NEXTN=shape_next)
sh = sh.replace(lastrow, lastrow + "\n" + newrow, 1)

OPEN_ADD = (
"BLK proposed **THE BOUGHT AVERAGE** (2026-09-19), arguing it is neither #11, #21 nor #10: #11 says "
"where the gains go, this says **how the loss is concealed** - BlackRock's blended fee rate reads "
"16.29 to 15.22bp, a survivable-looking 6.6% decline, while the organic rate fell 13.4% and every "
"component fell between 8% and 35%, the difference being $28.3bn of purchased mix; unlike #21 THE "
"ROLL-UP the revenue line is NOT bought (net inflows were $698bn in 2025, organic) - it is the "
"**price per unit** that is bought; and unlike #10 THE CAMOUFLAGE there is no weak leg burning the "
"strong leg's cash, because every leg is profitable. Its tells are checkable on any filer: a blended "
"unit price roughly flat while every disclosed component falls; goodwill and intangibles crossing "
"book equity ($63,251M against $55,888M, tangible equity **-$7,363M**); and the share count rising "
"by acquisition consideration faster than buybacks retire it (up to 25.0M shares and units, 15.4%, "
"against $1.6bn a year of repurchase). ")
anchor = "**All ten are listed so briefs count correctly; none is settled.**"
assert anchor in sh, "open paragraph anchor not found"
sh = sh.replace(anchor, OPEN_ADD + anchor, 1)
io.open(SH, "w", encoding="utf-8").write(sh)
print("shapes index updated: #11 instance added, new shape #%d proposed" % shape_next)

# ---------- the overnight log ----------
ol = io.open(OL, encoding="utf-8").read()
LOG = sub(
"- __CLOCK__ | BLK | Q1 IN / **Q2 OUT** (on the business; Q3, Q4, the price computation and Q6 "
"recorded, not governing). CIK found and confirmed: 0002012383 files today (formerNames *BlackRock "
"Funding, Inc. /DE*), the holding company created in October 2024 at the GIP closing, and **its "
"companyfacts begins at FY2024** - the 2009-2023 history sits under CIK 0001364742, now BlackRock "
"Finance, Inc., whose last 10-K was FY2023; a single-CIK XBRL pull returns two years and no error, "
"and `name_change_note()` returned an empty string. **Q2 fails on a filed price of the SUBSTITUTE, "
"which is new in this register: IVV 0.03% and Vanguard's VOO 0.03%, identical in the 2021 AND the "
"2026 prospectuses** (six accessions recorded in the register entry), SPY 0.0945% in both. Effective "
"fee rate on the filer's own 13-month average AUM, recomputed from four 10-Ks and a 10-Q and not "
"inherited from the BAM row: **TOTAL 16.29 / 16.15 / 15.62 / 14.90 / 15.22bp and 15.25 in H1-26; "
"ETFs -17.1%, active equity -20.8%, active fixed income -18.0%, active multi-asset -35.4%, non-ETF "
"index -8.1% - every organic line fell**; cash management's rise is a 2021 fee-waiver artefact and "
"has fallen since 2023; private markets +27.5% because GIP and HPS were bought. **Ex private markets "
"the total fell 15.74 to 13.64bp**; AUM +40.3% against base fees +25.7%. $28.3bn of acquisitions in "
"21 months, $22.0bn of it in own paper, $8,429M of contingent consideration still to issue, up to "
"25.0M shares and units (15.4%); tangible equity **-$7,363M**, so [E2-43]'s denominator cannot be "
"computed. Row: six filing-sourced peers, all falling (STT 5.40 to 4.62 my computation, IVZ 48.7 to "
"33.7, TROW 42.6 to 39.4, BEN 41.8 to 40.5, BX and BAM carried and flagged as not recomputed); "
"Vanguard resolved through its funds' own filings, Fidelity and Amundi UNRESEARCHED with artifacts "
"named, class NOT held provisional because both can only push the same way. Q3 IN, binary gate on "
"[E2-70]: **[E4-29] CLEAN on EBITDA (grep -c -i ebitda = 0 in the 10-K, 0 in the 8-K EX-99.1 and 0 "
"in the proxy) and full strength on the adjusted limb** ($35.31 GAAP against $48.09 as adjusted, the "
"gap nine times 2024's, $2,555M of add-backs including $738M of retention COMPENSATION, and the 10-K "
"says that margin sets senior pay); **the sharpest finding is [E3-50] - the pre-set NEO scorecard "
"scores \"Next 12-Month P/E Multiple (including relative premium)\" and Total Shareholder Return**; "
"[E4-30] does not fire (cash tax 33.3 / 17.0 / 19.5 / 20.5 / 30.2%, rising, above the book rate in "
"2025); the credit is the BPIP matrix published in advance with the prior cycle's outturn against its "
"pre-set target ($716M against $640M, 43.4% against 41.5%, payout 116.6%). Capital-allocation flag "
"live: a $1,073.40 average Q4 buyback price and a 2026 programme announced as a dollar quantity. Q4 "
"IN: **the filer's own CIP reconciliation shows GAAP operating cash understating the owner's cash by "
"$3,536M in 2025**; ex-CIP 6,168 / 5,668 / 5,684 / 7,267 / 7,463; H1 is 26.5% of the year so nothing "
"is annualisable; owner earnings $4,756-5,583M with a window spread of only 0.8%; **(c) judged at the "
"capex end because 68.8% of 2025 D&A is acquired-intangible amortisation - the corpus default runs "
"backwards** - with a third end quantified ($291M) and not adopted; SBC resolves, complete, at the "
"[E3-70] grant value, which exceeds the charge in all five years; **owner earnings PER SHARE peaked "
"at $35.02 in 2024 and fell to $28.15 in 2025, -12.5% against 2021, on 40.3% more AUM**. Shape #11 "
"THE PASS-THROUGH, and new shape #__NEXTN__ THE BOUGHT AVERAGE proposed and added to the index. Death "
"quantified three ways, the sharpest being the securities-lending indemnity ($353bn on loan against "
"$375bn of collateral; a 15% shortfall on a fifth of the book is $10,590M, 18.9% of equity) at a "
"low-level possibility. Q5 did not open: yield 2.74-3.21% against 5.34%, MINUS 2.6 to MINUS 2.1 "
"points against the bond; pre-tax expectancy 3.51-4.12% against the ~10% floor; value $550-650 and "
"$875-1,030, price above the whole range; windage 1. Nothing armed and no PORTFOLIO row (QLYS "
"ruling); six reopening tests pre-committed. Register entry __MINE__, counted __BEFORE__ before and "
"__MINE2__ after inside the fold script, exactly one added, no duplicate. Two defects found and fixed "
"inside the fold script itself (rindex lands on an inline heading mention; percent-formatting cannot "
"build text full of per-cent signs). Strongest fact against: iShares crossed $6 trillion and doubled "
"in three years at the same 0.03% as Vanguard | US$1,069.78 (2026-09-18 close, tools/sources.py, "
"aggregator flagged; the 10-K's own \"a closing stock price of $1,070\" as a cross-check) x "
"162,476,186 shares (154,869,259 common + 7,606,927 Subco Units, 10-Q cover \"As of July 31, 2026\", "
"accession 0001193125-26-337177; split factor 1.0) = cap US$173,814M | **FAIL at Q2, OUT on the "
"business**; sovereign 5.34% USD (US Treasury 30Y par, 09/18/2026, struck fresh, not FRED); "
"check_framework PASS | see fold commit. Concurrent USAR, CB and ERIC files left untouched\n",
    CLOCK=CLOCK, NEXTN=shape_next, MINE=mine, MINE2=mine, BEFORE=before)
assert "__" not in LOG, "unsubstituted token left in the overnight log line"
io.open(OL, "w", encoding="utf-8").write(ol.rstrip("\n") + "\n" + LOG)
print("overnight log appended")
print("FOLD COMPLETE - register entry", mine, "- new shape", shape_next)
