# TOOL TEST — `tools/corpus_index.py`. **VERDICT: PARTIALLY ADMITTED.**
**2026-08-28.** Built after the question "would it be more efficient to train an AI on the
corpus?" — answered no, because training moves the text into weights where the two-minute
standard cannot reach it. The corpus-legal alternative is retrieval: an index that finds the
passage sooner and returns **file + line span**, never a quote. Tested against the ledger
before admission, per the standing rule that a tool untested is a tool unadmitted.

## What it is

- ~20,100 passages chunked from the eight shelf folders (1.45M tokens). Ben Graham excluded
  (off shelf, 2026-07-13); Annual Reports excluded (duplicate the letters plus boilerplate).
- Two retrieval modes: **BM25 lexical** (pure stdlib) and a **local MiniLM vector layer**
  (all-MiniLM-L6-v2, runs on this machine, nothing leaves it, nothing is trained).
- Output is candidates to GO READ. The header says so on every run. Ruling 14: it gets the
  same passage sooner and adds no number; its ranking constants order candidates only.

## The acceptance test

**Gold standard: the ledger itself.** For each of 112 usable rows, query the index with the
row's `concept` field — a paraphrase, not the quote — and check whether a top-k passage
contains the verified verbatim text. This measures the one thing grep cannot do: finding a
passage from an idea rather than from its words.

| mode | top-5 | top-10 |
|---|---|---|
| **lexical (BM25)** | **47%** | **58%** |
| semantic only (MiniLM) | 32% | 36% |
| hybrid fusion (RRF) | 39% | 54% |
| **union of both lists** | — | **66%** |

## The verdict, mode by mode

- **Lexical: ADMITTED as the default.** 58% of verified passages found at top-10 from a
  paraphrase alone.
- **Fusion: REJECTED.** Blending the weak vector ranking into the strong lexical one made
  the tool *worse than its own baseline* (54% vs 58%). This was the design I would have
  shipped as the default. The acceptance test caught it before it shipped — *"you must not
  fool yourself, and you're the easiest person to fool"* **[E3-41]** applies to the
  toolwright, not just the analyst.
- **Semantic: ADMITTED AS A SECOND SWEEP, never fused.** Alone it is weak, but it finds
  **9 rows lexical misses** (union 66%), so the admitted design shows two panels side by
  side: BM25 first, then vector-only extras. The reader sweeps both.

## Limits, stated

1. **A miss is not proof of absence.** 34% of gold rows are missed at top-10; the hardest
   are the terse E1 concept labels ("Anti-consensus epistemics") against 1960s partnership
   prose. The index narrows where to read; it never certifies that nothing exists. **Test D
   still requires reading the partitions, not querying them.**
2. **The PCA extracts strip hyperlinked names** (Federal Express, Darwin, Sam Walton…), so
   a query on a stripped *name* cannot match. Query the concept, not the name.
3. **The gold standard is a proxy** (a 10-word fragment must land inside one chunk), so the
   true hit rates are modestly understated at chunk boundaries.
4. **The index is never a source.** Citation of record remains file + line, read in the
   file. Quoting index output would reintroduce exactly the provenance loss that ruled out
   fine-tuning in the first place.

## Usage

    python tools/corpus_index.py --build                  # rebuild after corpus changes
    python tools/corpus_index.py "managers damaging a wonderful business"
    python tools/corpus_index.py "untapped pricing power" --lexical
    python tools/corpus_index.py --eval                   # re-run this acceptance test
