import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(ROOT)

# ---- 1 + 2: queue entry and roster strike
q = "Screens/WATCHLIST RUN QUEUE.md"
s = open(q, encoding="utf-8").read()
entry = '''## COMPLETED FROM THE QUEUE
- **PLTR (Palantir), 2026-09-12 (started 2026-09-11, killed twice by session limits) - FAIL at
  Q5 (QUIT ON at the [E4-28] floor, on PRICE). Q1 IN, Q2 IN (NARROW), Q3 IN, Q4 IN (GREAT),
  Q5 NOT IN.** `Test Runs/2026-09-11 Run - PLTR Palantir.md`, `check_framework.py` PASS.
  Price **$167.23** (2026-09-11 close, aggregator, flagged) x **2,403,058,480 shares** (read off
  the **Q2 2026 10-Q cover, as of 2026-06-30, accession `0001321655-26-000041`**: Class A
  2,300,713,329 + Class B 101,340,151 + Class F 1,005,000, **summed after reading the charter
  description in the FY2025 10-K Note 9 - "all have the same rights, except with respect to
  voting and conversion rights", one EPS across all three, Class F converts 1:1 into Class B**;
  a further ~185M shares of in-the-money options at $9.98 and unvested RSUs are shown as a
  second cap) = cap **$401,863M** (**$432,754M** diluted). Sovereign **5.35% USD** (US
  Treasury 30-yr, issuing authority, **2026-09-11**, struck fresh; the brief's 5.37% was the
  09-10 print). **The twenty-sixth gate-clearer, and the dearest yet: yield 0.30% (FY2025
  ex-interest) to 0.63% (TTM), -4.7 to -5.3 points.** Owner earnings **$696M (3y) / $933M (2y)
  / $1,417M (FY2025) / $2,523M (TTM to 2026-06-30)**; the filed eight-year series crosses zero
  at the six-year window (2020 SBC $1,270.7M at the direct listing), so the width is stated
  in dollars: **minus $133M to plus $2,523M**. **[E4-41]: the business that exists now is
  2023-onward.** Value ~$13-24/sh at the bond, ~$9-14 at the floor, vs $167.23 (7-13x).
  **The buyer needs ~40%/yr owner-earnings growth for ten years, or 30% for fifteen, from
  the best twelve months ever filed, to reach the floor; 15% for twenty years returns 7.0%
  [E4-35].** Steady state needs $78-124bn of revenue against $8.15bn guided for 2026.
  **SBC/OCF 32.0% (FY2025), 24.6% TTM, 22.1% H1 2026** - down from 233%/253% in 2021-22 and
  below CRWD 68.0 / PINS 68.6, near QLYS 24.9 and CRM 23.4; SBC did not decide the file.
  Diluted shares 1,924M (2021) -> 2,569M (Q2 2026), +6.6%/yr; buyback $139M total, programme
  **terminated January 2026** - the rational refusal at a 0.35% yield [E5-24]. **Q2 split as
  the brief asked and the halves came out the other way round: Government (54%) earns a 66%
  contribution margin against contractors' 12-22% gross margins, but the 10-K attributes the
  growth to FASA ("The enforcement of FASA has resulted in a significant increase in our
  business ... Any change in or repeal of FASA ... would adversely affect our competitive
  position") and the customer negotiates "based upon the customer's view of what our pricing
  should be" - [E2-59], the moat belongs partly to the regime; Commercial (46%, +103% H1) is
  the only one of four data-platform filers with a GAAP operating profit (SNOW -30.6% with
  SBC 131% of OCF; C3.ai revenue -35.7%), NARROW on a three-year record inside a wave
  [E3-51].** Six peers with filings; **no peer names Palantir and Palantir names none**;
  Databricks unreachable; hyperscalers file no comparable line. **[E4-55]: the FIRST run in
  seven to find a filed unit series** - customer count 139 -> 954 -> 1,049 (June 2026 TTM),
  never withdrawn; [E2-49] does NOT fire. Q3 overlay; **four flags converge [E4-52]**:
  [E4-29] fires in the 10-K itself ("We exclude stock-based compensation, which is a noncash
  expense"), Rule of 40 "155%" on the adjusted book; guidance beaten by +7.4% then +19.1%
  above the top of the initial range; the proxy's only pay measure is "Stock price" and the
  CEO's 2020 award (105.0M options at $11.38 + 21.45M RSUs) vests on service alone through
  2031 - CAP to CEO **$11.09bn** in 2025; Class F gives three founders 49.999999% of the vote
  on a 100M-share ownership floor, immune to dilution [E3-66]. Honesty binary clean: class
  action dismissed with prejudice 2025-04-04 (on appeal); one cockroach, the 2021-22 SPAC
  "Strategic Commercial Contracts" ($492.7M total value, one investee bankrupt, run off to
  $326M). Q4: capex 0.76% of revenue, (c) band $8M wide, D&A default valid; $9.4bn cash and
  Treasuries, no debt; the one commitment is **$5.6bn of cloud hosting over ten years,
  $268M-$979M a year** - Palantir runs on the hyperscalers' capex. Death: the regime changes
  (a real possibility) or the wave ends - the business survives both; the $402bn does not.
  **Alerts armed: re-read <= $40 (15%/yr for a decade from TTM reaches the floor), floor band
  <= $24 (zero-growth value at the bond).** PORTFOLIO row added.
'''
assert s.count("## COMPLETED FROM THE QUEUE\n") == 1
s = s.replace("## COMPLETED FROM THE QUEUE\n", entry, 1)
old = "~~MRVL~~, ~~ELF~~, ~~AMD~~, ~~CRWD~~, PLTR"
assert s.count(old) == 1
s = s.replace(old, "~~MRVL~~, ~~ELF~~, ~~AMD~~, ~~CRWD~~, ~~PLTR~~")
open(q, "w", encoding="utf-8").write(s)

# ---- 4a: alerts
a = "tools/alerts.json"
d = json.load(open(a, encoding="utf-8"))
assert "PLTR-floor-band" not in [x["id"] for x in d["alerts"]]
d["alerts"].append({"id": "PLTR-floor-band", "ticker": "PLTR", "currency": "USD", "op": "<=", "threshold": 24, "active": True,
 "label": "PLTR at/below $24: the ZERO-GROWTH value at the bare 5.35% sovereign on the TTM owner earnings ($2,523M to 2026-06-30, plus $9.4bn of cash and Treasuries at face; $13-24/sh across the constructions, $9-14 at the E4-28 floor). Palantir cleared Q1-Q4 on 2026-09-12 and was quit on at Q5 at $167.23 - a business failure it is NOT, which is why a price band is the right instrument. RE-TEST FIRST: the filed customer count (1,049 at June 2026 TTM, growth decelerating 34% -> 24%) and the commercial contribution margin (66% in FY2025). Source: Test Runs/2026-09-11 Run - PLTR Palantir.md."})
d["alerts"].append({"id": "PLTR-reread-band", "ticker": "PLTR", "currency": "USD", "op": "<=", "threshold": 40, "active": True,
 "label": "PLTR at/below $40: READ AGAIN, do not buy on this ping. $40 is where a buyer underwriting 15% owner-earnings growth for a decade from the TTM figure reaches the E4-28 floor (10.2%) - and E4-35 says that rate is a fewer-than-1-in-20 event among the 200 most profitable companies. Watch the business falsifiers that would CLOSE the file at Q2 and void both bands: US commercial revenue growth below 20% in a filed year; the customer count falling in a filed year; a filed statement of discounting or retention packages; any change to FASA or a filed move by a major agency to developmental contracting. Q3 convergence (adjusted book, stock-price-only pay, Class F founder control) sizes any position DOWN."})
with open(a, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=1, ensure_ascii=False)
    f.write("\n")

# ---- 4b: PORTFOLIO row
p = "PORTFOLIO.md"
t = open(p, encoding="utf-8").read()
anchor = [l for l in t.split("\n") if l.startswith("| — | SNPS |")][0]
row = ("| — | PLTR | 0.30–0.63 % (2026-09-12) | 5.35 % USD | **−4.72 to −5.29 points — the dearest gate-clearer yet; 15 % growth for TWENTY years returns 7.0 %** | "
       "**RUN DONE** (`Test Runs/2026-09-11 Run - PLTR Palantir.md`): **Q1–Q4 all IN, Q4 GREAT — the twenty-sixth gate-clearer. Q2 IN NARROW, the two halves recorded separately and the brief's prior inverted:** "
       "Government (54 %) earns a **66 % contribution margin against contractors' 12–22 % gross margins**, but the 10-K attributes the growth to FASA and the customer negotiates *\"based upon the customer's view of what our pricing should be\"* — **[E2-59], the moat belongs partly to the regime**; "
       "Commercial (46 %, +103 % H1 2026) is **the only one of four data-platform filers with a GAAP operating profit** (SNOW −30.6 %, SBC 131 % of OCF; C3.ai revenue −35.7 %), narrow on a three-year record inside a wave. "
       "**[E4-55]: the first run in seven to find a filed unit series** — customers 139 → 954 → 1,049, never withdrawn. Cap **$401,863M** on 2,403,058,480 cover shares, three classes summed after the charter read (`0001321655-26-000041`). "
       "OE **$696M (3y) / $1,417M (FY2025) / $2,523M (TTM)**; the filed series crosses zero at six years. **Q5: quit on** — value ~$13–24 at the bond, ~$9–14 at the floor, vs **$167.23**; **the buyer needs ~40 %/yr for ten years or 30 % for fifteen from the best twelve months ever filed**; steady state needs $78–124bn of revenue vs $8.15bn guided. "
       "Watch-list: re-read ≤ $40, floor ≤ $24; **alerts armed 2026-09-12**. **SBC/OCF 32.0 % → 24.6 % TTM**; Q3 four flags converge [E4-52]: [E4-29] in the 10-K itself, guidance beaten +19.1 %, pay measured on *\"Stock price\"* alone (CEO CAP $11.09bn), Class F 49.999999 % on a 100M-share floor. "
       "Counter: revenue guided **+82 %** for 2026, US commercial **+149 %** — currently growing faster than the price requires. |")
assert t.count(anchor) == 1
t = t.replace(anchor, anchor + "\n" + row)
open(p, "w", encoding="utf-8").write(t)

# ---- 3: narrative fold
r = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
u = open(r, encoding="utf-8").read()
fold = '''

## PLTR FOLDED IN - 2026-09-12. SIXTY-EIGHT RUNS; A TWENTY-SIXTH GATE-CLEARER, THE DEAREST YET, AND THE FIRST FILED UNIT SERIES IN SEVEN RUNS.

The run did its own six-step fold. **Q1 IN . Q2 IN (NARROW) . Q3 IN . Q4 IN (GREAT) . Q5
NOT IN, quit on at the floor, on PRICE.** Price **$167.23** x 2,403,058,480 shares (Q2 2026
10-Q cover, acc. `0001321655-26-000041`; Class A + B + F summed after reading the charter
description in the FY2025 10-K Note 9 - "all have the same rights, except with respect to
voting and conversion rights") = cap **$401,863M**; sovereign **5.35%** struck fresh for
2026-09-11 (the brief's 5.37% was the previous print). Owner earnings **$696M (3y) / $933M
(2y) / $1,417M (FY2025) / $2,523M (TTM)**; the filed eight-year series crosses zero at the
six-year window. Value **~$13-24/share at the bond, ~$9-14 at the floor**; **the buyer at
$167.23 needs ~40%/yr owner-earnings growth for ten years, or 30% for fifteen, from the best
twelve months ever filed, to reach the floor; 15% for twenty years returns 7.0%.** Started
2026-09-11, killed twice by session limits, finished 2026-09-12 with zero question loss.

### WHAT THE RUN FOUND, IN THE ORDER THE BRIEF ASKED

1. **The three share classes are economically one, and the screen's sum was right for the
   right reason only by accident.** Class F is 1,005,000 shares (0.04%) with up to
   49.999999% of the vote, convertible 1:1 into Class B, dividend-equal; `cover_shares.py`
   refused to sum, the screen summed, and the charter read says summing is correct. The
   governance finding went to Q3: the Founders' voting power is immune to dilution on a
   100M-share ownership floor (4.2% of the count), and ex-F they hold ~22% of the vote.
   A further ~185M shares of in-the-money options ($9.98 strike, $25.5bn intrinsic) and
   RSUs sit off the cover; the cap is shown both ways ($402bn / $433bn).
2. **The 0.06% yield was on the wrong window, and the right window fails by the same
   order.** [E4-41]: the business that exists now is 2023-onward (first GAAP operating
   profit, first year SBC < OCF, AIP). On that business the yield is 0.30% (FY2025
   ex-interest) to 0.63% (TTM). No construction reaches 1%.
3. **SBC did not decide this file.** SBC/OCF 233% / 253% (2021-22) -> 66.8% -> 59.9% ->
   **32.0% (FY2025) -> 24.6% TTM -> 22.1% H1 2026**: below CRWD 68.0 and PINS 68.6, at
   QLYS 24.9 and CRM 23.4. [E3-70]'s floor rule was applied: 2025 grants at grant-date
   fair value ~$987M against $684M charged, and $3.0bn of intrinsic value left the register
   on option exercises in 2025. Diluted shares +6.6%/yr since listing; buyback $139M total,
   **terminated January 2026** - the rational refusal at a 0.35% yield [E5-24].
4. **Q2, the two halves tested separately, came out the other way round from the brief.**
   Government (54%) earns a 66% contribution margin against contractors' 12-22% gross
   margins - the wider-looking half - but the 10-K attributes the growth to a statute
   ("The enforcement of FASA has resulted in a significant increase in our business ... Any
   change in or repeal of FASA ... would adversely affect our competitive position") and
   the customer negotiates "based upon the customer's view of what our pricing should be":
   **[E2-59], the moat belongs partly to the regime.** Commercial (46%, +103% H1 2026) is the
   only one of four data-platform filers with a GAAP operating profit (SNOW -30.6% with SBC
   131% of OCF; C3.ai revenue -35.7%; NOW 13.7%) and is NARROW on a three-year record inside
   a wave [E3-51]. **No peer names Palantir and Palantir names none** ("We are fundamentally
   competing with the internal software development efforts of our potential customers");
   Databricks is unreachable; the hyperscalers file no comparable line. (c) is low because
   the capital is the hyperscalers': a **$5.6bn cloud commitment, $268M-$979M a year through
   February 2036**, sits in cost of revenue.
5. **[E4-55] found a unit series for the first time in seven runs**: customer count 139 ->
   237 -> 367 -> 497 -> 711 -> 954 -> 1,049 (June 2026 TTM), same definition since the S-1,
   never withdrawn. Its growth is decelerating (34% -> 24%) while revenue accelerates (56% ->
   93%): the growth is expansion inside accounts (top-twenty average revenue +45%). [E2-49]
   does NOT fire. Net dollar retention has never been a filed metric (recorded sweep, three
   10-Ks and seven releases: zero instances).
6. **Q3: overlay, IN, four flags converging [E4-52].** [E4-29] fires in the 10-K itself, not
   only the releases - "We exclude stock-based compensation, which is a noncash expense" -
   and the release's "Rule of 40 score of 155%" is 93 points of growth plus 62 of adjusted
   margin against a 47% GAAP margin. Guidance beaten every year by a widening margin (+7.4%,
   +19.1% above the top of the initial range) - the candid direction on [E3-48]. **The CEO
   award vests on nothing but service**: 105.0M options at $11.38 and 21.45M RSUs in 40
   quarterly instalments to 2031; the proxy's only performance measure is "Stock price";
   CAP to the CEO **$11.09bn** in 2025. Honesty binary clean (class action dismissed with
   prejudice 2025-04-04, on appeal; no regulatory inquiry disclosed); one cockroach, the
   2021-22 SPAC "Strategic Commercial Contracts" ($492.7M total, one investee bankrupt,
   run off to $326M).
7. **Q4 GREAT**: capex 0.76% of revenue, (c) band $8M wide, D&A default valid [E3-44];
   $9.4bn of cash and Treasuries, no debt; RPO covers nine months. Death: the regime changes
   or the wave ends - the business survives both, the $402bn does not (~$24/share at the
   bond on the TTM).

**Strongest fact against**: revenue guided **+82%** for 2026, US commercial **+149%**, owner
earnings $221M -> $2.5bn in three and a half years - the business is at present growing
faster than the 40% the price requires. The answer is [E4-35]'s base rate and the
arithmetic of size ($78-124bn of steady-state revenue against $8.15bn guided), not a claim
that it stops next year.

**Brief defects, recorded**: the brief's sovereign was a day stale by the time the run
struck its own; the "[E4-29] in the releases" framing would have led a run to score the
10-K clean when the 10-K carries the "noncash expense" rationale itself; and the share-class
warning was refuted (the sum is the count). **Tooling**: `growth_required` is a perpetual
Gordon rate and is meaningless on a `level_shift n/a` filer - the fading-rate form should
be published; the `spread` mixes windows and capex ends for the eighth consecutive run;
`cover_shares.py` and the screen disagree by design on multi-class filers and the screen's
behaviour is unlabelled.

**Alerts armed**: re-read <= $40 (15%/yr for a decade from TTM reaches the floor), floor band
<= $24 (zero-growth value at the bond). PORTFOLIO row added.

**Count: 68 runs** - gate-clearers 26, Q2 OUT 40, Q4 OUT 1, Q1 UNKNOWABLE 1.
'''
u = u.rstrip("\n") + fold
open(r, "w", encoding="utf-8").write(u)
print("fold written: queue entry, roster strike, alerts x2, portfolio row, reading list")
