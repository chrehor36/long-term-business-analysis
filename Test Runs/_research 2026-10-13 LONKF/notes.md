# LONKF research notes (2026-10-13)
Started: template copied before any fetch (earlier cycle, killed by a usage limit at 09:18). Resumed 10:16.

- Downloads (gitignored, in `cache/`): HKEXnews annual reports 2010, 2012-2025, Interim Report 2026, Monthly Return Sep 2026,
  clarification, AGM poll, CCT and WMP announcements; rivals' annual reports from cninfo (`cache/rivals/`: LiuGong 000528.SZ,
  XCMG 000425.SZ, Hangcha 603298.SH; FY2016, FY2019, FY2022, FY2025); ChinaBond curve and CFETS parity JSON; Yahoo quotes.
- `scripts/lonkf_calc.py`: owner cash, balance sheets, segment ROC, Q7 computation (all inputs filed figures).
- `scripts/ids.py`: prints ledger rows by id; `scripts/check_ids.py`: the run file's id and fragment check.
- `pages.py`, `keydata.py`: page extractors used on the downloaded PDFs (run from this folder, outside `cache/`).
