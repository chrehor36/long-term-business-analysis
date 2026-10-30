from fetch_core import *
import sys
for acc in ["0001326801-24-000069","0001326801-24-000012"]:
    names = exhibits(acc)
    print(acc, [n for n in names if "ex" in n.lower()])
