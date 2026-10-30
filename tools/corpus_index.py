#!/usr/bin/env python3
"""CORPUS INDEX — find the passage sooner. Never a source, never a judge.

    python tools/corpus_index.py --build            # chunk + lexical index (+vectors if available)
    python tools/corpus_index.py "managers damaging a good business"
    python tools/corpus_index.py "untapped pricing power" -k 8 --lexical
    python tools/corpus_index.py --eval             # acceptance test against the ledger

WHAT THIS IS. A retrieval aid over the citation shelf: it returns candidate
passages as FILE + LINE SPAN + snippet, ranked. The citation of record is, and
stays, the file and line — a chunk returned by this tool is a place to GO READ,
never a thing to quote. Quoting the index instead of the file would reintroduce
exactly the provenance loss that rules out fine-tuning.

RULING 14 TEST: does it get the same passage sooner, or add a number? It gets
the passage sooner. Its internal ranking constants (BM25 k1/b, cosine weights)
order candidates only and may never appear in any analysis.

SHELF SCOPE. The eight citation-shelf folders only. Ben Graham is OFF the shelf
(2026-07-13): his folder is excluded, so a Graham phrase will simply not be
found — that is correct behaviour, not a gap. Annual Reports are excluded as
duplicating the letters plus boilerplate. MBA folder excluded per standing rule.

KNOWN LIMIT, inherited from the sources: the PCA web extracts strip proper nouns
that were hyperlinks (Federal Express, Sam Walton, Darwin...), so a query on a
stripped NAME cannot match the body text that discusses it. Query the concept,
not the name.
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import argparse, csv, json, math, os, pickle, re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_cache")
CHUNKS_P = os.path.join(CACHE, "shelf_chunks.jsonl")
LEX_P = os.path.join(CACHE, "shelf_lexical.pkl")
VEC_P = os.path.join(CACHE, "shelf_vectors.npy")
LEDGER = os.path.join(ROOT, "principle_ledger.csv")

SHELF = ["Partnership Letters", "Shareholder Letters", "Wesco Letters (Munger)",
         "Annual Meetings", "Munger Talks (PCA)", "Owners Manual",
         "Fortune Essays (Buffett)", "Special Letters"]

TARGET_WORDS = 120          # merge blank-line blocks up to roughly this size
STOP = set("""a an and are as at be been but by for from has have he his her i if in is it its
of on or our so than that the their them they this to was we were what when which who will
with would you your""".split())

K1, B = 1.5, 0.75           # BM25 ranking constants: order candidates only


def tokens(s):
    return [w for w in re.findall(r"[a-z0-9']+", s.lower()) if w not in STOP]


def chunk_file(relpath):
    path = os.path.join(ROOT, relpath)
    lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    blocks, cur, start = [], [], None
    for i, ln in enumerate(lines, 1):
        if ln.strip():
            if start is None:
                start = i
            cur.append(ln.strip())
        elif cur:
            blocks.append((start, i - 1, " ".join(cur)))
            cur, start = [], None
    if cur:
        blocks.append((start, len(lines), " ".join(cur)))
    # merge small neighbouring blocks so hard-wrapped letters chunk like meetings
    out, buf, s0, e0, words = [], [], None, None, 0
    for s, e, t in blocks:
        n = len(t.split())
        if buf and words + n > TARGET_WORDS and words >= 40:
            out.append((s0, e0, " ".join(buf)))
            buf, s0, words = [], None, 0
        if not buf:
            s0 = s
        buf.append(t)
        e0, words = e, words + n
    if buf:
        out.append((s0, e0, " ".join(buf)))
    return out


def build():
    os.makedirs(CACHE, exist_ok=True)
    chunks = []
    for folder in SHELF:
        fdir = os.path.join(ROOT, folder)
        if not os.path.isdir(fdir):
            print(f"  MISSING SHELF FOLDER: {folder}")
            continue
        for fn in sorted(os.listdir(fdir)):
            if not fn.endswith(".txt") or fn.startswith("_"):
                continue
            rel = f"{folder}/{fn}"
            for s, e, t in chunk_file(rel):
                if len(t.split()) >= 15:
                    chunks.append(dict(id=len(chunks), file=rel, ls=s, le=e, text=t))
    with open(CHUNKS_P, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c) + "\n")

    df, doclen, toks = Counter(), [], []
    for c in chunks:
        tk = tokens(c["text"])
        toks.append(Counter(tk))
        doclen.append(len(tk))
        df.update(set(tk))
    post = defaultdict(list)
    for i, tc in enumerate(toks):
        for w, n in tc.items():
            post[w].append((i, n))
    with open(LEX_P, "wb") as f:
        pickle.dump(dict(df=dict(df), post=dict(post), doclen=doclen,
                         n=len(chunks), avg=sum(doclen) / max(1, len(chunks))), f)
    print(f"chunked shelf: {len(chunks)} passages from "
          f"{len(set(c['file'] for c in chunks))} files "
          f"({sum(doclen):,} tokens)")

    try:
        from sentence_transformers import SentenceTransformer
        import numpy as np
    except ImportError:
        print("vectors: sentence_transformers not installed — lexical only "
              "(pip install sentence-transformers to enable)")
        return
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [c["text"][:1500] for c in chunks]
    emb = model.encode(texts, batch_size=64, show_progress_bar=True,
                       normalize_embeddings=True)
    np.save(VEC_P, emb.astype("float16"))
    print(f"vectors: {emb.shape[0]} x {emb.shape[1]} (all-MiniLM-L6-v2, local)")


def load():
    chunks = [json.loads(l) for l in open(CHUNKS_P, encoding="utf-8")]
    lex = pickle.load(open(LEX_P, "rb"))
    return chunks, lex


def bm25(query, lex, topn=200):
    q = tokens(query)
    scores = Counter()
    for w in q:
        if w not in lex["post"]:
            continue
        idf = math.log(1 + (lex["n"] - lex["df"][w] + 0.5) / (lex["df"][w] + 0.5))
        for i, n in lex["post"][w]:
            d = lex["doclen"][i]
            scores[i] += idf * n * (K1 + 1) / (n + K1 * (1 - B + B * d / lex["avg"]))
    return scores.most_common(topn)


_SEM = {}


def semantic(query, k=200):
    try:
        from sentence_transformers import SentenceTransformer
        import numpy as np
    except ImportError:
        return None
    if not os.path.exists(VEC_P):
        return None
    if "emb" not in _SEM:          # load once per process, not once per query
        _SEM["emb"] = np.load(VEC_P).astype("float32")
        _SEM["model"] = SentenceTransformer("all-MiniLM-L6-v2")
    qv = _SEM["model"].encode([query], normalize_embeddings=True)[0].astype("float32")
    sims = _SEM["emb"] @ qv
    idx = sims.argsort()[::-1][:k]
    return [(int(i), float(sims[i])) for i in idx]


def search(query, k=10, lexical_only=False):
    """TWO PANELS, NEVER FUSED. Tested 2026-08-28 against the ledger (112 gold
    rows, concept-paraphrase queries): lexical 58% top-10, semantic-only 36%,
    RRF fusion 54% -- fusion DILUTED the stronger signal and was rejected. But
    the union reached 66%: the vector layer finds passages BM25 misses (9 rows).
    So the admitted design is both lists side by side, the reader sweeps both."""
    chunks, lex = load()
    lx = [i for i, _ in bm25(query, lex, k)]
    sm_extra = []
    if not lexical_only:
        sm = semantic(query, k=k)
        if sm is not None:
            seen = set(lx)
            sm_extra = [i for i, _ in sm if i not in seen][:max(3, k // 2)]
    return [chunks[i] for i in lx], [chunks[i] for i in sm_extra]


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("�", "-")
    return re.sub(r"\s+", " ", s).lower().strip()


def evaluate(lexical_only=False):
    """Acceptance test: for every ledger row, query with the row's CONCEPT (a
    paraphrase, not the quote) and check whether a top-k passage contains a
    10-word fragment of the verbatim quote. Tests conceptual retrieval, which
    is the one thing grep cannot do."""
    chunks, lex = load()
    rows = [r for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))]
    usable, h5, h10, misses = 0, 0, 0, []
    for r in rows:
        frag_src = norm(re.split(r"\[\.\.\.\]|\.\.\.", r["quote_verbatim"])[0])
        words = frag_src.split()
        if len(words) < 10:
            continue
        probe = " ".join(words[:10])
        gold = {c["id"] for c in chunks
                if c["file"] == r["source_file"] and probe in norm(c["text"])}
        if not gold:  # quote spans a chunk boundary or file off shelf
            probe2 = " ".join(words[5:15]) if len(words) >= 15 else None
            if probe2:
                gold = {c["id"] for c in chunks
                        if c["file"] == r["source_file"] and probe2 in norm(c["text"])}
        if not gold:
            continue
        usable += 1
        lx, sm = search(r["concept"], k=10, lexical_only=lexical_only)
        if {c["id"] for c in lx[:5]} & gold:
            h5 += 1
        if ({c["id"] for c in lx} | {c["id"] for c in sm}) & gold:
            h10 += 1
        else:
            misses.append((r["id"], r["concept"][:60]))
    mode = "lexical only" if lexical_only else "both panels (lexical + semantic sweep)"
    print(f"EVAL ({mode}): {usable} ledger rows usable as gold")
    print(f"  concept query finds the verified passage:  "
          f"lexical top-5 {h5}/{usable} ({h5/usable*100:.0f}%)   "
          f"either panel {h10}/{usable} ({h10/usable*100:.0f}%)")
    if misses:
        print(f"  missed at top-10 ({len(misses)}):")
        for i, c in misses[:15]:
            print(f"    {i}  {c}")
    return usable, h5, h10, misses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--eval", action="store_true")
    ap.add_argument("--lexical", action="store_true", help="BM25 only, skip vectors")
    ap.add_argument("-k", type=int, default=10)
    a = ap.parse_args()
    if a.build:
        build()
        return 0
    if a.eval:
        evaluate(lexical_only=a.lexical)
        return 0
    if not a.query:
        ap.error("give a query, --build, or --eval")
    lx, sm = search(a.query, a.k, a.lexical)
    print("RETRIEVAL ONLY. The citation of record is the file and line;")
    print("GO READ each hit before citing it. Never quote this output.\n")
    print(f"— lexical (BM25), top {len(lx)} —")
    for c in lx:
        print(f"  {c['file']}:{c['ls']}-{c['le']}")
        print(f"      {c['text'][:200]}...\n")
    if sm:
        print(f"— semantic second sweep (MiniLM), {len(sm)} not in the list above —")
        for c in sm:
            print(f"  {c['file']}:{c['ls']}-{c['le']}")
            print(f"      {c['text'][:200]}...\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
