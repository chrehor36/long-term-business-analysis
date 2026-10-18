# CLNE run notes 2026-10-17

## Files
- fetch.py, compact.py: EDGAR fetch (User-Agent per brief) and table compaction; raw text in cache/ (gitignored).
- runpy_out.txt: `python tools/run.py CLNE` output (arithmetic lines only used).
- owner_cash.py / owner_cash_out.txt: owner cash recast from the filed cash-flow statements, 2018-2025.
- range.py / range_out.txt: Q7 range and fair price (COMPUTATION, NOT A CLEARANCE).
- peers.py / peers_out.txt: OPAL and MNTK XBRL series (and CLNE's), newest vintage.
- led.py, led_q1.txt, led_after.txt: ledger rows read for the citations.
- check_ids.py: id and quote checker.

## Checks, 2026-10-17
- check_ids.py: 44 id occurrences, 37 distinct, all present in principle_ledger_v5.csv; no E-ids. Four CHECK lines remain;
  each was reviewed by hand: the quoted words are the filer's or the proxy's (attributed in the text to the 10-K or DEF 14A)
  and sit in the bullet or sentence before an id that cites a test, not the quote. No ledger quote fails.
- python tools/check_framework.py: PASS (run before the final commit).
