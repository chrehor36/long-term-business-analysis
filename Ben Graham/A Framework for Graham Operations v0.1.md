# A FRAMEWORK FOR GRAHAM OPERATIONS — v0.1 (draft, 2026-07-17)
The Graham-side counterpart to "A Framework for Long-Term Business
Analysis." Same construction discipline, different philosophy: the main
framework buys wonderful businesses and holds; this one buys statistical
bargains and SELLS. The two never mix accounts: **Graham operations run in
the taxable brokerage only** — the Roth mandate stays Munger's.

## PRIME RULES (inherited from the main framework, adapted)
1. **VERBATIM ONLY.** Quotes reproduce source text exactly with edition +
   page; line-break hyphenation artifacts may be repaired but must be
   flagged. Paraphrase is never presented as quotation.
2. **THE ZWEIG RULE** (learned on day one — the seed extraction hit
   commentary twice): this edition of The Intelligent Investor interleaves
   Graham's chapters with Jason Zweig's commentary and footnotes.
   **A quote is attributable to Graham only after verifying the page falls
   inside a Graham chapter.** Zweig may be cited as Zweig, never as Graham.
3. **Three source classes:**
   - **[II — ch.X, p.Y]** The Intelligent Investor, rev. ed. (user-owned
     copy; text-extractable ✓)
   - **[SA — pending OCR]** Security Analysis (user-owned; the PDF is a
     scan with no text layer — citations blocked until an OCR pass)
   - **[LATER-GRAHAM PRACTICE]** rules from Graham's 1970s interviews and
     simplified systems (e.g., the 1976-era "50% or two years" sell rule,
     the earnings-yield ≥ 2× AAA bond test). These are NOT in the two
     books — they are documented late-career practice and must never be
     cited to the books.
   - **[GRAHAM CONVENTION]** our own additions, labeled, with rationale.
4. **CONFESS INVENTIONS. THE TEXT WINS. SEQUENTIAL GATES.** As in the
   main framework.

## THE TWO TRACKS (Graham's own dual structure)
Graham split investors, not valuations: **DEFENSIVE** (passive — strict
quality screens, 10-30 issues, minimal maintenance) and **ENTERPRISING**
(active — bargain issues, workouts, net-nets). [II ch.4-7, 14-15 —
verbatim anchors pending extraction pass.]
**We operate the ENTERPRISING track.** The Defensive track is documented
for completeness; QQQM already serves its function in the user's Roth.

## THE GATES
**G1 — CLASSIFICATION & CONDUCT.** The operation must satisfy Graham's
definition: *"An investment operation is one which, upon thorough
analysis promises safety of principal and an adequate return."*
[II ch.1, pdf-p.32 — **verbatim, extracted and verified 2026-07-17**;
hyphenation repaired]. Mr. Market conduct rule (quotes are offers, not
verdicts; quotational loss ≠ permanent loss) [II ch.8 — Graham-chapter
verbatim pending; the p.200 hit was Zweig commentary].

**G2 — SURVIVAL SCREEN.** The bargain must survive to re-rate: positive
worst-year earnings in the trailing 5 (inherited from the main
framework's range anchoring — [GRAHAM CONVENTION], it did the killing in
our screens: 370 of 881 small/mids failed it), current ratio and debt
tests per track [II ch.14/15 thresholds — pending extraction; defensive
ch.14 is current ratio ≥2, LT debt ≤ net current assets, subject to
verbatim verification].

**G3 — PRICE TESTS (the Graham Statute).** Any ONE, strictly met:
- **(a) Net-net**: price ≤ 2/3 × (current assets − total liabilities)
  [SA + II ch.15 — pending]. Screen buildable on existing XBRL infra
  (needs CurrentAssets/Liabilities pulls — not yet built).
- **(b) Earnings-yield test**: E/P (worst-of-5yr) ≥ 2× AAA corporate
  bond yield [LATER-GRAHAM PRACTICE — labeled]. With AAA ≈ 5.3-5.6%,
  the bar ≈ 10.6-11.2% — deliberately stiffer than the main framework's
  6.10% small/mid Statute.
- **(c) Defensive multipliers** (defensive track only): P/E ≤ 15,
  P/B ≤ 1.5, product ≤ 22.5 [II ch.14 — pending].

**G4 — APPRAISAL & MARGIN OF SAFETY.** A conservative appraisal (the
main framework's Book Two machinery is borrowed here as the appraisal
tool — [GRAHAM CONVENTION], since Graham's own appraisal methods are in
the un-OCR'd SA) and price ≤ ~2/3 of it. The margin-of-safety chapter
anchor [II ch.20 — Graham-chapter verbatim pending].

**G5 — BASKET CONSTRUCTION.** Graham's protection was breadth: 10-30
issues defensive [II ch.14 — pending]; wide diversification mandatory
for net-nets. Operating at 1-5 positions instead: **each name carries a
written "broken if" line that replaces diversification — a triggered
line is an exit, not a review** [GRAHAM CONVENTION]. Correlated names
count as ONE position (the mortgage-insurer lesson).

**G6 — SELL DISCIPLINE (the gate that makes it Graham).**
- **Gain exit: +50%, or the G4 appraisal gap closed, whichever is less
  ambitious.** [LATER-GRAHAM PRACTICE — 1976-era simplified system.]
- **Time exit: 2 years, out regardless.** [Same source class.] The butt
  deteriorates while held; a stale bargain is a failing thesis even at
  an unchanged price.
- **Deterioration exit**: the "broken if" line. [GRAHAM CONVENTION.]
- Buffett's cross-reference, from the MAIN framework's corpus: the 1989
  letter's cigar-butt repudiation — "time is the friend of the wonderful
  business, the enemy of the mediocre" — is WHY the clock exists.

**G7 — RECORD.** Every entry/exit logged in GRAHAM BOARD.md (the run-file
analog) with price, target, stops, and dates. Board chart maintained as
the visual ledger.

## OPERATOR PROTOCOL
Taxable account only · board-first (no order before its row exists with
targets and stops) · aggregator prices flagged · the main framework's
verdicts are never overridden by Graham logic (a name can be a Graham
trade AND a framework WAIT — different questions) · Graham work never
enters the main framework's citation shelf, and vice versa.

## PHASE PLAN
- **G-0 (done)**: corpus tested — II extracts ✓ (641pp), SA is a scan
  (OCR pass required before any SA citation); Zweig rule established;
  first verbatim seed extracted and verified (G1 definition).
- **G-1 (COMPLETE, 2026-07-17)**: extraction pass done — **15 of 15
  verbatim anchors found, page-cited, and Graham-attributed** in
  `graham_ledger.csv` (three passes; recovered misses were mid-word
  hyphen splits and a unicode ½; one wrong-page row superseded in place
  per no-silent-edits). Every [pending] tag in the gates above now has a
  verified ledger row.
- **G-2 (COMPLETE, 2026-07-17)**: full corpus rebuilt as searchable
  fulltexts (II_fulltext.txt 641pp; SA_fulltext_OCR.txt 735pp, 0 OCR
  failures) and **every ledger anchor re-verified against them — 16/16**
  (15 II in-text matches; the SA definition eye-verified against its page
  image, OCR garble documented). Checker misses were normalization
  artifacts (hyphens/unicode fractions), resolved under aggressive
  normalization; documented here, not smoothed.
- **G-3 (COMPLETE, 2026-07-17)**: automated screens built and run over
  the SP400/600 universe (588 names with balance data):
  · **G3(a) net-net: ZERO true net-nets** (cap ≤ 2/3 NCAV) — the
    predicted extinction, now empirical. The screen works; the pond is
    dry in indexed US mid/small caps. Future hunting grounds: micro/OTC,
    Japan locals.
  · **G3(b) 2×AAA (~10.8%): 12 passers** (11 after the MAN artifact).
  · **Strict 1934 G2 debt test (debt ≤110% of net current assets) fails
    essentially every modern candidate** — capitalized leases and
    acquisition goodwill make total liabilities exceed current assets
    almost everywhere. Recorded as an era-artifact finding: the pilot
    either operates G3(b)+relaxed-G2 [GRAHAM CONVENTION, rationale: the
    1934 test predates lease capitalization accounting] or accepts an
    empty eligible set. UNRESOLVED — user decision before the pilot
    funds.

## CURRENT BOARD
See GRAHAM BOARD.md — EFOR held; CMCSA/CTSH/UHS/VZ/SYF charted with
targets and broken-if lines. All six conform to G2/G3(b)/G6 retroactively;
none has a G4 net-net qualification (true net-nets are near-extinct in
listed US large/mid caps — the NCAV screen in G-3 hunts where they live).
