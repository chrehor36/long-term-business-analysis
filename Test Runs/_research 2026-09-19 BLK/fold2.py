# BLK FOLD, part 2: the survival-shapes index and the overnight log.
# Split out because the shapes index had moved under a concurrent run (CB added #23 THE CUSHION
# and changed the closing count sentence from "All ten" to "All eleven") between this session
# reading it and writing it. Steps 1-3 of the fold are already on disk; this file writes only
# the two remaining artifacts, so it is safe to re-run only if it has not already applied.
import io, os, re

ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
OL = os.path.join(ROOT, "Screens", "_daily", "OVERNIGHT LOG.md")
SH = os.path.join(ROOT, "Screens", "SURVIVAL SHAPES - index.md")
CLOCK = "2026-09-19 15:32 EDT"
MINE, BEFORE = 124, 123


def sub(text, **kw):
    for k, v in kw.items():
        text = text.replace("__" + k + "__", str(v))
    assert "__" not in text, "unsubstituted token: " + text[:80]
    return text


sh = io.open(SH, encoding="utf-8").read()
assert "The bought average" not in sh, "already applied"
nums = [int(n) for n in re.findall(r"(?m)^\| (\d+) \|", sh)]
NEXTN = max(nums) + 1
print("shapes on disk:", max(nums), "-> new shape", NEXTN)

m = re.search(r"(?m)^\| 11 \| \*\*The pass-through\*\*.*$", sh)
assert m, "shape 11 row not found"
row11 = m.group(0)
add11 = sub(
    " BLK (2026-09-19, the mechanism, with #__NEXTN__ proposed as the concealment: ETF average AUM "
    "+60.3% from 2021 to 2025 while the ETF effective fee rate fell 17.1% (20.41 to 16.92bp), total "
    "AUM +40.3% against base fees +25.7%, and owner earnings per share flat to -12.5%; the savings "
    "went home to the customer, and [E3-62]'s second step is answered by the filer's own price table)",
    NEXTN=NEXTN)
assert row11.rstrip().endswith("|")
sh = sh.replace(row11, row11.rstrip()[:-1].rstrip() + "," + add11 + " |", 1)

lastrow = re.findall(r"(?m)^\| %d \| .*$" % max(nums), sh)[-1]
newrow = sub(
    "| __NEXTN__ | **The bought average** *(proposed, pending the operator)* | BLK (2026-09-19) | the "
    "price of everything the business already owns falls every year, and the owner buys higher-priced "
    "businesses with its own shares so that the blended price stands still; the decline is invisible "
    "in the headline while the share count and the goodwill rise, and the owner pays for the "
    "appearance of stability in dilution | |", NEXTN=NEXTN)
sh = sh.replace(lastrow, lastrow + "\n" + newrow, 1)

OPEN_ADD = (
"BLK proposed **#__NEXTN__ THE BOUGHT AVERAGE** (2026-09-19), arguing it is neither #11, #21 nor "
"#10: #11 says where the gains go, this says **how the loss is concealed** - BlackRock's blended fee "
"rate reads 16.29 to 15.22bp, a survivable-looking 6.6% decline, while the organic rate fell 13.4% "
"and every component fell between 8% and 35%, the difference being $28.3bn of purchased mix; unlike "
"#21 THE ROLL-UP the revenue line is NOT bought (net inflows were $698bn in 2025, organic) - it is "
"the **price per unit** that is bought; and unlike #10 THE CAMOUFLAGE there is no weak leg burning "
"the strong leg's cash, because every leg is profitable. Its tells are checkable on any filer: a "
"blended unit price roughly flat while every disclosed component falls; goodwill and intangibles "
"crossing book equity ($63,251M against $55,888M, tangible equity **-$7,363M**); and the share count "
"rising by acquisition consideration faster than buybacks retire it (up to 25.0M shares and units, "
"15.4%, against $1.6bn a year of repurchase). ")
# the closing count sentence moves with each addition; match it rather than hard-code the number
mc = re.search(r"\*\*All \w+ are listed so briefs count correctly; none is settled\.\*\*", sh)
assert mc, "closing count sentence not found"
sh = sh.replace(mc.group(0), sub(OPEN_ADD, NEXTN=NEXTN) + mc.group(0), 1)
io.open(SH, "w", encoding="utf-8").write(sh)
print("shapes index updated; note the closing count sentence still reads:", mc.group(0))

ol = io.open(OL, encoding="utf-8").read()
assert "| BLK |" not in ol, "overnight log line already applied"
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
"__MINE2__ after inside the fold script, exactly one added, no duplicate - the brief's count was "
"stale again. Three defects found and fixed inside the fold script itself (rindex lands on an inline "
"heading mention; percent-formatting cannot build text full of per-cent signs; the shapes index moved "
"under a concurrent CB fold between the read and the write, so the shapes step was split out). "
"Strongest fact against: iShares crossed $6 trillion and doubled in three years at the same 0.03% as "
"Vanguard | US$1,069.78 (2026-09-18 close, tools/sources.py, aggregator flagged; the 10-K's own \"a "
"closing stock price of $1,070\" as a cross-check) x 162,476,186 shares (154,869,259 common + "
"7,606,927 Subco Units, 10-Q cover \"As of July 31, 2026\", accession 0001193125-26-337177; split "
"factor 1.0) = cap US$173,814M | **FAIL at Q2, OUT on the business**; sovereign 5.34% USD (US "
"Treasury 30Y par, 09/18/2026, struck fresh, not FRED); check_framework PASS | see fold commit. "
"Concurrent USAR, CB and ERIC files left untouched\n",
    CLOCK=CLOCK, NEXTN=NEXTN, MINE=MINE, MINE2=MINE, BEFORE=BEFORE)
io.open(OL, "w", encoding="utf-8").write(ol.rstrip("\n") + "\n" + LOG)
print("overnight log appended. FOLD COMPLETE - register entry", MINE, "- new shape", NEXTN)
