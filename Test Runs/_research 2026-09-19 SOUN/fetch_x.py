from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
for acc in sys.argv[1:]:
    names = exhibits(acc); print(acc, names)
