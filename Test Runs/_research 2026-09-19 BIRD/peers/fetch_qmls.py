import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, ".."))
import fetch_core as F
F.HERE = here
F.grab("0001628280-26-059295", "qmls-20260630.htm", "QMLS_10QA_2026Q2", cik=2084026)
F.grab("0001437749-26-023622", "quma20260714_424b4.htm", "QMLS_424B4_2026-07-15", cik=2084026)
