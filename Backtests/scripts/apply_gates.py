"""Apply Gates 1/2/3/5 per anchor date from dated evidence timelines.

WHY THIS EXISTS. Earlier full-gate runs researched each (company, date) pair
independently, which let the same company be judged inconsistently at nearby
dates and made hindsight leakage hard to police. Here the research output is
purely FACTUAL and DATED -- a moat timeline plus integrity events with the date
each became public -- and this script mechanically applies the gates at each
anchor using only facts public before that anchor. Consistency across the 296
company-date evaluations is therefore structural rather than a matter of the
researcher's memory.

INPUT  gate_timelines.json  {ticker: {gate1, gate2[], gate3[], gate5_broken_by}}
OUTPUT full_gate_survivors_{yr}.json, plus a per-anchor verdict table.

GATE 3 SEVERITY RULE -- FRAMEWORK CONVENTION, not from the corpus.
The corpus gives Gate 3 as a binary honesty test but no severity ladder, so one
is imposed here and applied uniformly:
  DISQUALIFYING (adjudicated/credibly-alleged fraud, accounting manipulation,
    systematic consumer deception, bribery/FCPA, regulator finding of
    misconduct)  -> FAIL
  SERIOUS (material settlement or regulatory action without admission) -> does
    not fail on its own; recorded
  MINOR (ordinary-course litigation) -> ignored
Because that line is a convention rather than a corpus rule, every result is
reported BOTH ways: `strict=False` (DISQUALIFYING only) and `strict=True`
(DISQUALIFYING + SERIOUS). If the two disagree materially, the framework's
market-beating claim depends on a convention we invented, which must be said
out loud rather than hidden behind whichever number looks better.
"""
import json, os, datetime

SCRATCH = os.path.dirname(os.path.abspath(__file__))
YEARS = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]


def parse_ym(s):
    """'2016-09' or '2016' -> date. Returns None when unparseable/absent."""
    if not s or str(s).upper() in ("NONE", "NULL", ""):
        return None
    s = str(s).strip()
    try:
        parts = s.split("-")
        y = int(parts[0])
        m = int(parts[1]) if len(parts) > 1 else 1
        return datetime.date(y, m, 1)
    except (ValueError, IndexError):
        return None


def moat_at(gate2, year):
    """Classification in force at <year>-06-30.

    Each entry is {from: int|None, class: str, note: str}; the applicable entry
    is the latest whose `from` is <= year (None means 'from the beginning')."""
    best = None
    for e in gate2:
        frm = e.get("from")
        if frm is None or int(frm) <= year:
            if best is None or (frm or 0) >= (best.get("from") or 0):
                best = e
    return best


def evaluate(tl, year, strict=False, max_age_years=None):
    """max_age_years: if set, a DISQUALIFYING event older than this no longer
    fails the gate.

    This third variant exists because batch C surfaced a real problem with an
    unbounded rule: ADM pled guilty to price-fixing in 1996, which precedes its
    2013/2017/2018/2019 anchors by 17-23 years and involved executives long
    gone. An unbounded rule fails ADM forever for conduct no current owner
    could act on; a 10-year window instead treats a conviction as evidence
    about the people running the business now. Neither reading is in the
    corpus, so both are reported."""
    anchor = datetime.date(year, 6, 30)
    reasons = []

    g1 = (tl.get("gate1") or {}).get("verdict", "PASS").upper()
    if g1 == "FAIL":
        reasons.append("G1:" + (tl["gate1"].get("note", "")[:60]))

    m = moat_at(tl.get("gate2") or [], year)
    moat = (m or {}).get("class", "NONE").upper()
    if moat == "NONE":
        reasons.append("G2:no moat" + (f" ({m.get('note','')[:40]})" if m else ""))

    fail_levels = {"DISQUALIFYING"} | ({"SERIOUS"} if strict else set())
    for ev in tl.get("gate3") or []:
        d = parse_ym(ev.get("date"))
        if not (d and d <= anchor):
            continue
        if str(ev.get("severity", "")).upper() not in fail_levels:
            continue
        if max_age_years is not None and (anchor - d).days > max_age_years * 365.25:
            continue
        reasons.append(f"G3:{ev.get('date')} {ev.get('note','')[:50]}")
        break

    b = parse_ym(tl.get("gate5_broken_by"))
    if b and b <= anchor:
        reasons.append(f"G5:thesis broken by {tl.get('gate5_broken_by')}")

    return (len(reasons) == 0), moat, reasons


def run(strict=False, max_age=None, tag=None):
    tls = json.load(open(os.path.join(SCRATCH, "gate_timelines.json")))
    out, table = {}, []
    for yr in YEARS:
        cands = json.load(open(os.path.join(SCRATCH, f"gate4_survivors_{yr}.json")))
        surv, fails, untested = [], [], []
        for t in cands:
            tl = tls.get(t)
            if tl is None:
                untested.append(t)
                continue
            ok, moat, why = evaluate(tl, int(yr), strict, max_age)
            if ok:
                surv.append({"ticker": t, "moat": moat})
            else:
                fails.append({"ticker": t, "why": why})
        out[yr] = {"survivors": surv, "fails": fails, "untested": untested}
        table.append((yr, len(cands), len(surv), len(fails), len(untested)))

    tag = tag or ("strict" if strict else "base")
    json.dump(out, open(os.path.join(SCRATCH, f"full_gate_{tag}.json"), "w"),
              indent=1)
    for yr, d in out.items():
        json.dump([s["ticker"] for s in d["survivors"]],
                  open(os.path.join(SCRATCH,
                       f"full_gate_survivors_{tag}_{yr}.json"), "w"))

    age = f", events within {max_age}y" if max_age else ", any age"
    print(f"\n=== Gate 3 rule: {'DISQUALIFYING + SERIOUS' if strict else 'DISQUALIFYING only'}{age} ===")
    print(f"{'anchor':7s} {'gate4':>6s} {'survive':>8s} {'fail':>6s} {'no-data':>8s}")
    for yr, n, s, f, u in table:
        print(f"{yr:7s} {n:>6d} {s:>8d} {f:>6d} {u:>8d}")
    return out


if __name__ == "__main__":
    run(strict=False)                             # DISQUALIFYING, any age
    run(strict=True, tag="strict")                # + SERIOUS
    run(strict=False, max_age=10, tag="recent")   # DISQUALIFYING within 10y
