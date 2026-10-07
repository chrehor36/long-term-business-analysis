"""Routing wrapper, not a new number. tools/run.py XOM failed on 2026-10-06 ("no overlapping OCF/D&A/capex
annual facts. UNRESEARCHED.") because SEC's ticker file now maps XOM to ExxonMobil Holdings Corp (CIK 2115436),
the holding company formed by the reorganization of 2026-07-01 (8-K12B, 0001193125-26-291990), which has no
annual XBRL history. Every annual 10-K through FY2025 was filed by Exxon Mobil Corp, CIK 34088. This wrapper
points run.py's CIK lookup at 34088 and otherwise runs run.py unchanged.
Usage (from repo root): python "Test Runs/_research 2026-10-06 XOM/run_py_legacy_cik.py" XOM [run.py args]"""
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sources as S
_orig = S.cik_for
def cik_for(t):
    if t.upper() == 'XOM':
        return '0000034088', 'EXXON MOBIL CORP (CIK 34088, legacy registrant; routed by wrapper)'
    return _orig(t)
S.cik_for = cik_for
import run
sys.exit(run.main())
