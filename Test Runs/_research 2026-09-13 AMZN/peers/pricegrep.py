"""Sentence-level search: sentences containing a price word AND a cloud word."""
import sys, re
PRICE = re.compile(r"\b(pric\w*|discount\w*)\b", re.I)
CLOUD = re.compile(r"(cloud|azure|OCI|infrastructure|compute|GPU|TPU|capacity)", re.I)
for f in sys.argv[1:]:
    t = open(f, encoding="utf-8", errors="replace").read()
    t = re.sub(r"\s*\|\s*", " ", t)
    t = re.sub(r"\s+", " ", t)
    sents = re.split(r"(?<=[.;])\s+(?=[A-Z•o])", t)
    seen = set()
    print("=====", f)
    for i, s in enumerate(sents):
        if PRICE.search(s) and CLOUD.search(s) and s not in seen:
            seen.add(s)
            pos = t.find(s)
            print(f"[char {pos}] {s[:900]}")
            print()
