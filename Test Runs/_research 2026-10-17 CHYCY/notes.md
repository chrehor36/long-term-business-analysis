# CHYCY research notes (2026-10-17)
- Template copied before any fetch.
- Sources: company IR library (https://www.chiyodacorp.com/en/ir/library/); raw PDFs and stripped text kept in cache/ (gitignored).
- scripts/rows.py: prints PDF text grouped by row (y-position) so statement lines keep their two columns.
- scripts/rivals.py -> rivals.txt: annual 10-K XBRL values (net income, equity, revenue) for Fluor, KBR, McDermott with accessions.
- Prices: 6366.T JPY 617 and CHYCY USD 4.06, close 2026-10-16, Yahoo via tools/sources.py (aggregator). JGB 30y 4.02% (MOF, 2026-10-15).
- Contamination: none of the blind-listed files opened. The session context showed the git status (other runs' research folder
  names for AYI and ARCB, recent commit subjects about BLGO) and the memory index (queue-state lines); none concern Chiyoda; not used.
