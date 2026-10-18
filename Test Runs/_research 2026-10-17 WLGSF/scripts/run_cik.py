"""Run tools/run.py for a delisted 20-F filer whose ticker is no longer in the SEC ticker file.
Patches sources.cik_for to return the CIK given; arithmetic only. Same number sooner, no number added."""
import sys, os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "Screens"))
import sources as S
S.cik_for = lambda t: ("0001899658", "Wang & Lee Group, Inc.")
import run
sys.argv = ["run.py"] + sys.argv[1:]
sys.exit(run.main())
