"""V5 RE-RUN FOLD - the FOLD for v5 re-runs (operator instruction of 2026-10-07: every v4.1 name is run again under v5).

    python tools/v5_rerun_fold.py <batch.json>

Written 2026-10-10 for the overnight cycle, from the script the interactive session used for batches 1 to 8. It does
the bookkeeping steps of THE FOLD and nothing else: the register entry (text supplied by the caller), the done-file
line, the narrative line, retiring every active v4.1 band of the name, arming the v5 fair-price alert where the caller
gives one, and regenerating `Screens/V5 PASSERS - the alert list.md` from the register and the alerts. It concludes
nothing: the box, the entry text and the fair price come from the run file. Same number sooner, no number added.

batch.json: {"batch": "<label>", "date": "YYYY-MM-DD", "runs": [{"t": TICKER, "name": ..., "file": "<run file name>",
 "box": "OUT AT Q7, ON PRICE" (or the run's box in capitals), "entry": "<register text after the bold head>",
 "narr": "<one narrative line>", "fair": number or null, "fair_label": "<alert label>"}]}
A name that is not in `Screens/_daily/_v5_rerun_order.txt` is still folded, but remove it from the done file after.
"""

import json, os, re, sys
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
def load(p):
    s = open(p, encoding="utf-8", newline="").read(); return s, ("\r\n" if "\r\n" in s else "\n")
def save(p, s): open(p, "w", encoding="utf-8", newline="").write(s)
norm = lambda t: t.replace("-", ".")
B = json.load(open(sys.argv[1], encoding="utf-8"))
runs = B["runs"]; tag = B["batch"]; date = B.get("date", "2026-10-07")

R = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
s, nl = load(R)
anchor = nl + "## THE WRITE-EARLY PROTOCOL"; assert s.count(anchor) == 1
blk = [f"### v5 RE-RUN BATCH {tag}, {date} (the operator's instruction of 2026-10-07; `Screens/_daily/_v5_rerun_order.txt`)"]
for r in runs:
    assert ("- **" + r["t"] + " (") not in s[s.index("### v5 RE-RUN BATCH"):] if "### v5 RE-RUN BATCH" in s else True, r["t"]
    blk.append(f"- **{r['t']} ({r['name']}), {date} - {r['box']}. v5, blind, dispatched under the canonical brief.** "
               f"`Test Runs/{r['file']}`. {r['entry']}")
blk.append("")
s = s.replace(anchor, nl + nl.join(blk) + anchor, 1); save(R, s)

D = ROOT + r"\Screens\_daily\_v5_rerun_done.txt"
s, nl = load(D); s = s if s.endswith(nl) else s + nl
save(D, s + nl.join(r["t"] for r in runs) + nl)

L = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
s, nl = load(L); s = s if s.endswith(nl) else s + nl
save(L, s + nl + f"## UPDATE {date} - v5 RE-RUN BATCH {tag} (v4.1 names run again under v5)" + nl +
     nl.join(f"- **{r['t']}: {r['box']}.** {r['narr']}" for r in runs) + nl)

A = ROOT + r"\tools\alerts.json"
raw = open(A, encoding="utf-8", newline="").read(); d = json.loads(raw)
ret = 0
for r in runs:
    for a in d["alerts"]:
        if norm(a["ticker"]) == norm(r["t"]) and a["active"] and "-v5-" not in a["id"]:
            a["active"] = False
            a["label"] = f"RETIRED {date} (a v4.1 band; superseded by the v5 run of {date}). " + a["label"]; ret += 1
    if r.get("fair"):
        aid = f"{r['t']}-v5-fair"
        d["alerts"] = [a for a in d["alerts"] if a["id"] != aid]
        d["alerts"].append({"id": aid, "ticker": r["t"], "currency": "USD", "op": "<=", "threshold": r["fair"], "active": True,
                            "label": r["fair_label"]})
out = json.dumps(d, indent=1, ensure_ascii=True).replace("\n", "\r\n") + ("\r\n" if raw.endswith("\r\n") else "")
open(A, "w", encoding="utf-8", newline="").write(out)

# regenerate the passers list
s = open(R, encoding="utf-8").read()
a0 = re.search(r"^## COMPLETED FROM THE QUEUE", s, re.M).start(); b0 = re.search(r"^## THE WRITE-EARLY PROTOCOL", s, re.M).start()
latest = {}
for h in s[a0:b0].split("\n"):
    m = re.match(r"- \*\*([A-Z][A-Z0-9.\-]*) \(([^)]*)\),? (2026-\d\d-\d\d)", h)
    if not m: continue
    t, n, dt = m.groups(); t = norm(t); u = h[:400].upper()
    v5 = dt >= "2026-10-05"
    if not v5: continue
    passed = bool(re.search(r"OUT AT Q7|\bIN AT Q7|BOX:? IN\b", u))
    if t not in latest or dt >= latest[t][1]: latest[t] = (n, dt, passed)
files = {}
for f in os.listdir(ROOT + r"\Test Runs"):
    m = re.match(r"(2026-1\d-\d\d) Run - ([A-Z][A-Z0-9.\-]*) ", f)
    if m: files.setdefault(norm(m.group(2)), []).append(f)
al = {}
for a in d["alerts"]:
    if not a["active"]: continue
    # 2026-10-12: key by the alert's id prefix as well as its quoted ticker, because a foreign name's alert quotes the
    # home-exchange share (ANDR.VI, DPLM.L) while the register lists the run's ticker (ADRZY, DPMAY).
    keys = {norm(a["ticker"])}
    if "-v5-" in a["id"]: keys.add(norm(a["id"].split("-v5-")[0]))
    for k in keys:
        al.setdefault(k, []).append(f"`{a['id']}` {a.get('currency','USD') if a.get('currency','USD')!='USD' else '$'}{a['threshold']}")
P = ROOT + r"\Screens\V5 PASSERS - the alert list.md"
old = open(P, encoding="utf-8").read()
head = old.split("| ticker |")[0].rstrip("\n")
T = ["| ticker | company | run of record | active alert(s) |", "|---|---|---|---|"]
for t in sorted(k for k, v in latest.items() if v[2]):
    n, dt, _ = latest[t]
    f = sorted(x for x in files.get(t, []) if x.startswith(dt))
    T.append(f"| {t} | {n} | `Test Runs/{f[-1] if f else '(see register)'}` | {'; '.join(al.get(t, ['NONE: arm one at the fold']))} |")
order = [l.strip() for l in open(ROOT + r"\Screens\_daily\_v5_rerun_order.txt", encoding="utf-8") if l.strip() and not l.startswith("#")]
done = {l.strip() for l in open(D, encoding="utf-8") if l.strip() and not l.startswith("#")}
gc_line = old.split("## The v4.1 gate-clearers awaiting a v5 run")[1]
gc_all = [x.strip(" .\n") for x in gc_line.strip().split("\n")[-1].split(",")]
waiting = [x for x in gc_all if x and x not in done]
tail = ["", "## The v4.1 gate-clearers awaiting a v5 run",
        "*Names that cleared Q1 to Q4 under the archived v4.1 and have not yet been run under v5. Their v4.1 bands stay active until "
        "the v5 run replaces them; each leaves this list when its v5 run is folded (and enters the table above if it passes). The "
        "order is `Screens/_daily/_v5_rerun_order.txt`.*", "", ", ".join(waiting) + "."]
save(P, head + "\n\n" + "\n".join(T) + "\n" + "\n".join(tail) + "\n")
print(f"batch {tag}: {len(runs)} entries; v4.1 bands retired {ret}; passers {sum(1 for v in latest.values() if v[2])}; "
      f"gate-clearers waiting {len(waiting)}; order remaining {len([x for x in order if x not in done])}")
