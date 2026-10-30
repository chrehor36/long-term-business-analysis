# Wrapper: tools/run.py cannot resolve TPICQ (deregistered, not in SEC's ticker file).
# Patches only the CIK lookup to CIK 1455684; arithmetic is run.py's own.
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, "..", ".."))
sys.path.insert(0, os.path.join(root, "tools"))
sys.path.insert(0, os.path.join(root, "Screens"))
os.chdir(root)
import sources as S
_orig = S.cik_for
S.cik_for = lambda t: ("0001455684", "TPI Composites, Inc.") if t.upper() in ("TPICQ", "TPIC") else _orig(t)
# Price: no quote source in tools/sources.py serves OTC Pink TPICQ; the aggregator quote
# ($0.01, digrin.com, October 2026, flagged) is injected here so the arithmetic can print.
S.price = lambda t: (0.01, '2026-10 (aggregator, digrin.com)', 'USD')
import run
sys.argv = ["run.py"] + sys.argv[1:]
sys.exit(run.main())
