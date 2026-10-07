# -*- coding: utf-8 -*-
"""Every quoted span in the run file must resolve to the ledger or to a downloaded filing.

PRIME RULE 1: paraphrase is never recorded as quotation. This finds spans I put inside
typographic quote marks and asks where each one actually comes from.
"""
import io, os, re, csv, glob, sys, unicodedata

D = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(D))
RUN = os.path.join(BASE, "Test Runs", "2026-09-21 Run - MGM MGM Resorts International.md")


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = (s.replace(u"’", "'").replace(u"‘", "'")
          .replace(u"“", '"').replace(u"”", '"')
          .replace(u"—", " ").replace(u"–", " ")
          .replace(u"�", "").replace(u" ", " "))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return " ".join(s.split())


# ---- corpora
led = []
for r in csv.DictReader(io.open(os.path.join(BASE, "principle_ledger.csv"), encoding="utf-8")):
    for k, v in r.items():
        if v:
            led.append(norm(v))
LED = " || ".join(led)

FIL = []
for p in glob.glob(os.path.join(D, "*.txt")) + glob.glob(os.path.join(D, "peers", "*.txt")):
    if os.path.basename(p).startswith("_"):
        continue
    try:
        FIL.append(norm(io.open(p, encoding="utf-8", errors="replace").read()))
    except Exception:
        pass
FILT = " || ".join(FIL)

FW = norm(io.open(os.path.join(BASE, "Framework", "THE FRAMEWORK v4.md"), encoding="utf-8").read())

src = io.open(RUN, encoding="utf-8").read()
spans = re.findall(u'"(.+?)"', src, re.S) + re.findall(u"“(.+?)”", src, re.S)
print("quoted spans found:", len(spans))
bad = []
for s in spans:
    parts = [p.strip() for p in re.split(u"…|\\.\\.\\.", s) if len(p.strip()) > 0]
    for p in parts:
        n = norm(p)
        if len(n) < 25:
            continue
        where = []
        if n in LED:
            where.append("LEDGER")
        if n in FILT:
            where.append("FILING")
        if not where:
            src_fw = "FRAMEWORK-PROSE" if n in FW else "NOWHERE"
            bad.append((src_fw, p[:170]))

print()
print("spans that do NOT resolve to the ledger or to a downloaded filing:", len(bad))
for w, p in bad:
    print(" [%s] %s" % (w, p))
