# TOOL TEST 2026-10-25 - `tools/triage.py`, a local model reading filings for five red flags

*The record behind the `tools/triage.py` row of `CLAUDE.md`. Written by the session that built the tool, at the operator's
instruction ("I want to make sure 2. works reliably before fully deploying it"). The ruling-14 test for any tool: does it get
the same thing sooner, or does it add a number? This tool returns sentences that exist in the filing; it adds no number and
reaches no verdict. A flag is a prompt to read, never a score (operator rule 8). Admission for queue ordering is the
operator's decision; this file is the evidence for it.*

## What was tested

The model is `qwen3:14b` under Ollama on the operator's machine (an RTX 5080, 16 GB; the model runs wholly on the card),
temperature zero. Five flags: RESTATEMENT (previously issued statements restated to correct an error), ICFR_NOT_EFFECTIVE
(management's conclusion, or a material weakness at the period end), MAJOR_CUSTOMER (one customer at ten percent or more of
revenue or receivables), GOING_CONCERN (substantial doubt), AUDITOR_CHANGE (dismissed, resigned or replaced). Each flag must
carry one sentence found word for word in the filing (pipes and whitespace ignored, since the cached filings flatten tables
to one cell per line).

Two passes. The first chunks the filing (about 16,000 characters, 600 overlap) and asks for flags with sentences. The
second drops, in order: raises with no verbatim sentence; raises whose own note is a negation ("No customer accounted for
10%..."); for ICFR_NOT_EFFECTIVE and GOING_CONCERN only, sentences in conditional risk-factor language ("If our internal
control...", "could", "may" matched case-sensitively, because "May 3, 2024" is a date); customer figures under ten percent;
flag names the model invented. Each survivor is then put to the model as one yes-or-no question, with the sentence shown
inside 400 characters of its surroundings (a table row means nothing without its heading).

## Ground truth

Set independently of the model: regular expressions over each filing for every flag's characteristic sentences, then read
by the session. Cells the filing left genuinely arguable were marked debatable and not scored (a remediated weakness
described in the same filing; a subsidiary's customer; a prior-year receivable concentration; a checked cover-page
error-correction box with no restatement note). Two truth cells were corrected during the test when the model found what the
regular expression had missed (Trump Media's single customer at 94% of revenue) or the session had misread (none else).

## Results

**Clean set**: 17 filings, mostly large and clean (TSCO, PWR, EME, LINC, UTI, CCB, BRK.B, HRB, INTU, HD, LOW, CHWY, WOOF,
GEHC, MYRG, DY, and TBTC FY2020 as the known positive), 82 scored decisions.

| | true flags found | false flags |
|---|---|---|
| first pass alone | 5 of 5 | 20 |
| both passes | 5 of 5 | 0 |

**Dirty set**: 17 filings chosen because a regular expression found a flag in them (SPR 2024, GPOR 2020, DBD 2022, DJT 2023
and 2024, BZFD 2025, Cambium, USAR 2025, ACMR 2023, SLP 2025, RGTI 2022, KHC 2018, BE 2019, MSM FY24, AES 2024, ABG 2025,
NWL 2023), 78 scored decisions.

| | true flags found | false flags |
|---|---|---|
| first pass alone | 34 of 34 | 28 |
| both passes, first filter | 32 of 34 | 5 |
| both passes, filter corrected (the "May" and "would resign" misses) | 35 of 35 | 3 |

The three false flags that remain, each a reader would settle in a minute: Gulfport's 2020 correction of a misclassification
between two income-statement lines in prior years (a revision, not a restatement, by the strict definition); BuzzFeed's
"immaterial disclosure misstatement" in a tax note (the same); Asbury's Toyota at 30% of new-vehicle revenue, which is a
manufacturer, not a customer. The debatable cells all came out the way a reader would want: Coastal's and Asbury's
remediated weaknesses raised with the sentence saying so; Walmart at 21% of Kraft Heinz's sales raised; Berkshire's
subsidiary-level customer dropped.

**Combined**: 34 filings, 160 decisions, 40 of 40 true flags found, 3 false flags.

**Consistency**: two first-pass runs of LINC and DY at temperature zero gave identical raises (6 and 10).

**Cost**: 3.4 to 4.0 seconds a chunk; a 400 KB 10-K takes about 90 seconds for the first pass and about a minute for the
second. The whole re-run queue would take one night. No tokens of the large model are spent.

## What it cannot do, and what remains untested

It reads what a filing states; it cannot say what a filing leaves out. Among the 34 filings the going-concern and
auditor-change flags fired on true cases in the dirty set only (6 and 6), so the positive direction rests on those twelve.
The first pass invents flag names of its own (30 in the dirty set, all dropped); the drop is mechanical and loses nothing,
but it shows the model will answer a question it was not asked. The sentence check catches fabrication; it does not catch a
real sentence read for the wrong meaning, which is what the second pass and the reader are for. A flag that survives both
passes still tells the reader where to look and nothing more.

## How it was run

`python tools/triage.py <filing.txt> [...] --out results.json`, or `--queue <dir>` for a folder of filings. The scoring
scripts of this test are not in the repository (they carried this session's ground truth and nothing else).
