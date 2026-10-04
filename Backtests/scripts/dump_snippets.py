import json, os, re, html as htmlmod

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
DOCS_CACHE = os.path.join(CACHE, "10k_docs")

failures = json.load(open(os.path.join(SCRATCH, "10k_extraction_failures.json")))
targets = [t for t, r in failures if r.startswith("NO_AMV_OR_SHARES_MATCH")]

out = []
for t in targets:
    fn = os.path.join(DOCS_CACHE, f"{t}.htm")
    if not os.path.exists(fn):
        out.append(f"=== {t} === NO CACHED DOC\n")
        continue
    raw = open(fn, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<[^>]+>", " ", raw)
    text = htmlmod.unescape(text)
    text = re.sub(r"\s+", " ", text)
    idx = text.lower().find("aggregate market value")
    if idx < 0:
        # some filers phrase it without that exact term -- grab the whole
        # cover-page-ish window instead so a human reader can still find it
        snippet = text[:2500]
        out.append(f"=== {t} === (no 'aggregate market value' phrase found; showing doc start)\n{snippet}\n")
    else:
        snippet = text[max(0, idx-200):idx+900]
        out.append(f"=== {t} ===\n{snippet}\n")

open(os.path.join(SCRATCH, "snippets_batch.txt"), "w", encoding="utf-8").write("\n".join(out))
print(f"Wrote {len(targets)} snippets to snippets_batch.txt")
