#!/usr/bin/env python3
"""TRIAGE - a local model reads a filing for five red flags, so the queue can be ordered. Never a verdict, never a score.

    python tools/triage.py <filing.txt> [more filings...] [--model qwen3:14b] [--out results.json]
    python tools/triage.py --queue <dir of filings> --out results.json

WHAT THIS IS. A flag is a prompt to read, never a score (operator rule 8). The tool asks a local model, running
under Ollama on this machine, whether a filing states as fact any of: a RESTATEMENT of previously issued financial
statements to correct an error; internal control over financial reporting NOT EFFECTIVE or a material weakness at
the period end; a MAJOR CUSTOMER at ten percent or more of revenue or receivables; GOING CONCERN doubt; an
AUDITOR CHANGE. Every flag carries one sentence that must appear word for word in the filing, or it is dropped.

TWO PASSES, BECAUSE ONE IS NOT ENOUGH. Measured 2026-10-25 on 17 clean filings (82 flag decisions): one pass found
every true flag and raised twenty false ones (precision 20%). The second pass drops, in order: flags with no verbatim
sentence; flags whose own note is a negation ("No customer accounted for..."); conditional risk-factor language ("If our
internal control..."); customer figures under ten percent; flag names the model invented; then asks the model one
yes/no question per surviving flag, showing it the sentence inside 400 characters of its surroundings (a table row
means nothing without its heading). After the second pass: every true flag found, none false, and two reruns at
temperature zero gave identical raises. The dirty-set test of the same day is recorded beside this file's entry in
CLAUDE.md. The ruling-14 test: the tool gets the same sentence sooner; it adds no number and reaches no verdict.

WHAT IT CANNOT DO. It reads what the filing states; it cannot tell you what the filing leaves out. A filing that
says nothing about customer concentration is not a filing with none. The reader goes to the sentence, in the filing.

Requires Ollama (https://ollama.com) with the model pulled: `ollama pull qwen3:14b` (about 10 GB; fits a 16 GB card).
"""
import argparse, json, os, re, sys, time, urllib.request, urllib.error

OLLAMA = "http://localhost:11434/api/chat"
FLAGS = ["RESTATEMENT", "ICFR_NOT_EFFECTIVE", "MAJOR_CUSTOMER", "GOING_CONCERN", "AUDITOR_CHANGE"]
DEF = {
 "RESTATEMENT": "the company's previously issued financial statements were restated to correct an error or misstatement (not a stock split adjustment, reclassification, recast, or an amended-and-restated agreement or charter)",
 "ICFR_NOT_EFFECTIVE": "management concluded that internal control over financial reporting was not effective, or that a material weakness existed, as of the period end (not a remediated prior weakness, and not a hypothetical)",
 "MAJOR_CUSTOMER": "one single customer accounted for 10% or more of the company's revenue or accounts receivable (not a government funding program, not a geographic region, not a subsidiary's customer, and not a statement that no customer did)",
 "GOING_CONCERN": "there is substantial doubt about the company's ability to continue as a going concern",
 "AUDITOR_CHANGE": "the company's independent registered public accounting firm was dismissed, resigned or was replaced",
}
SYSTEM_1 = ("You screen SEC filings for an analyst. You report only what the excerpt states. "
            "Each flag you raise must carry one sentence copied exactly, character for character, from the excerpt. "
            "Generic risk-factor language about what COULD happen is not a flag; only a statement that it DID happen or IS the case. "
            "If nothing applies, return an empty list. Never return a flag without its sentence.")
USER_1 = ("Excerpt from a company's Form 10-K:\n\n<<<\n{chunk}\n>>>\n\n"
          "Raise a flag for each of these that THIS EXCERPT actually states as fact about the filing company:\n"
          "RESTATEMENT: prior-period financial statements were restated to correct an error (not a reclassification, recast for a new segment structure or adoption of a new accounting standard, and not the risk that a restatement might occur).\n"
          "ICFR_NOT_EFFECTIVE: management concluded internal control over financial reporting was NOT effective, or a material weakness existed at the period end.\n"
          "MAJOR_CUSTOMER: a single customer was 10% or more of the company's revenue or receivables; give the percentage(s) in detail. Geographic mix is not a customer.\n"
          "GOING_CONCERN: substantial doubt about the company's ability to continue as a going concern.\n"
          "AUDITOR_CHANGE: the independent registered public accounting firm was dismissed, resigned or replaced.\n"
          'Return JSON: {{"flags": [{{"flag": "<one of the five names>", "detail": "<short>", "sentence": "<exact sentence>"}}]}}')
SYSTEM_2 = "You check one sentence at a time against one definition. Be literal and strict."
NEG = re.compile(r"^\s*no\b|\bno (statement|mention|restatement|material weakness|single customer|customer|sales to)|\bnot (mentioned|stated|raised)|\bnone of\b|\bdoes not\b|\bwas not mentioned", re.I)
COND_START = re.compile(r"^\s*(if|should|were|any failure|failure to)\b", re.I)
COND_MODAL = re.compile(r"\b(could|may|might|would|cannot assure|no assurance)\b")   # case-sensitive: "May 3, 2024" is a date, found the hard way
CONDITIONAL_FLAGS = {"ICFR_NOT_EFFECTIVE", "GOING_CONCERN"}   # where risk-factor hypotheticals cluster; a reported event ("would resign") is left to the verifier
CHUNK, OVERLAP = 16000, 600


def ask(model, system, user, num_ctx=8192, think=False):
    body = {"model": model, "stream": False, "format": "json",
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "options": {"temperature": 0, "num_ctx": num_ctx}}
    if think is not None:
        body["think"] = think
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")
        if "think" in msg and think is not None:
            return ask(model, system, user, num_ctx, think=None)
        raise RuntimeError(msg)
    except urllib.error.URLError as e:
        sys.exit(f"Ollama is not answering at {OLLAMA} ({e.reason}). Start it, or install it: https://ollama.com")
    return r["message"]["content"]


def norm(s):
    s = (s or "").replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\ufb03", "ffi").replace("\ufb02", "fl").replace("\ufb01", "fi")
    s = s.replace("|", " ")            # flattened tables: one cell per line, pipe separated
    return re.sub(r"\s+", " ", s).lower().strip()


def parse_json(s):
    try:
        return json.loads(s)
    except Exception:
        m = re.search(r"\{.*\}", s or "", re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
    return {}


def chunks(text):
    i = 0
    while i < len(text):
        yield text[i:i + CHUNK]
        if i + CHUNK >= len(text):
            break
        i += CHUNK - OVERLAP


def pcts(s):
    return [float(x) for x in re.findall(r"(\d{1,3}(?:\.\d+)?)\s?%", s)]


def first_pass(model, text):
    raised = {f: [] for f in FLAGS}
    for ch in chunks(text):
        for f in parse_json(ask(model, SYSTEM_1, USER_1.format(chunk=ch))).get("flags", []) or []:
            if not isinstance(f, dict):
                continue
            name = str(f.get("flag", "")).upper()
            if name not in FLAGS:          # an invented flag name is dropped here, and counted
                raised.setdefault("_invented", []).append(name)
                continue
            sen = str(f.get("sentence") or "")
            raised[name].append(dict(sentence=sen[:400], detail=str(f.get("detail", ""))[:160], verbatim=bool(norm(sen)) and len(norm(sen)) >= 20 and norm(sen) in norm(text)))
    return raised


def second_pass(model, text, raised):
    ntext = norm(text)
    kept, dropped = {f: [] for f in FLAGS}, []
    for f in FLAGS:
        for it in raised.get(f, []):
            s, d = it["sentence"], it["detail"]
            if not it["verbatim"]:
                dropped.append((f, "no verbatim sentence", s[:90])); continue
            if NEG.search(d) or (f == "MAJOR_CUSTOMER" and NEG.search(s)):
                dropped.append((f, "negation", s[:90])); continue
            if f in CONDITIONAL_FLAGS and (COND_START.search(s) or COND_MODAL.search(s)):
                dropped.append((f, "conditional language", s[:90])); continue
            if f == "MAJOR_CUSTOMER":
                p = pcts(d + " " + s)
                if p and max(p) < 10:
                    dropped.append((f, "below ten percent", s[:90])); continue
            i = ntext.find(norm(s)); ctx = ntext[max(0, i - 400): i + len(norm(s)) + 200] if i >= 0 else s
            q = (f"Sentence from a Form 10-K:\n\"{s}\"\n\nIts surrounding text in the filing (lower-cased, tables flattened):\n<<<{ctx}>>>\n\n"
                 f"Analyst's note: {d}\n\nQuestion: does the sentence, read in that context, state as a fact that {DEF[f]}? "
                 'Answer JSON {"yes": true or false, "why": "<one line>"}.')
            j = parse_json(ask(model, SYSTEM_2, q, num_ctx=4096))
            if j.get("yes") is True:
                kept[f].append(dict(sentence=s, detail=d))
            else:
                dropped.append((f, "verifier said no: " + str(j.get("why", ""))[:100], s[:90]))
    return kept, dropped


def triage(model, path):
    text = open(path, encoding="utf-8", errors="replace").read()
    t0 = time.time()
    raised = first_pass(model, text)
    kept, dropped = second_pass(model, text, raised)
    return dict(path=path, kb=len(text) // 1024, seconds=round(time.time() - t0), flags=kept,
                dropped=dropped, invented=raised.get("_invented", []))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*")
    ap.add_argument("--queue", help="a directory; every .txt in it is a filing")
    ap.add_argument("--model", default="qwen3:14b")
    ap.add_argument("--out", help="write results as JSON here (appended to if it exists)")
    a = ap.parse_args()
    files = list(a.files)
    if a.queue:
        files += sorted(os.path.join(a.queue, f) for f in os.listdir(a.queue) if f.lower().endswith(".txt"))
    if not files:
        ap.error("give filings, or --queue <dir>")
    results = json.load(open(a.out, encoding="utf-8")) if a.out and os.path.exists(a.out) else {}
    print("A FLAG IS A PROMPT TO READ, NEVER A SCORE. Go to the sentence, in the filing, before anything is written.\n")
    for p in files:
        r = triage(a.model, p)
        results[p] = r
        if a.out:
            json.dump(results, open(a.out, "w", encoding="utf-8"), indent=1)
        hits = {f: v for f, v in r["flags"].items() if v}
        print(f"{os.path.basename(p)}  ({r['kb']} KB, {r['seconds']}s)  " + (", ".join(f"{f} x{len(v)}" for f, v in hits.items()) if hits else "no flag survived both passes"))
        for f, v in hits.items():
            for it in v[:3]:
                print(f"    {f}: {it['detail']}\n        \"{it['sentence'][:220]}\"")
        if r["dropped"]:
            print(f"    ({len(r['dropped'])} raise(s) dropped in the second pass; {len(r['invented'])} invented flag name(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
