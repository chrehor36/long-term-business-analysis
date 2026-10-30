"""Screen only (operator rule 8): does any MSFT 10-Q/10-K carry an Xbox pricing phrase?
A hit count is a prompt to open the document, never evidence."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
from sources import fts_count
CIK = "0000789019"
for ph in ["price of consoles", "Game Pass price", "price increase", "higher prices of consoles",
           "pricing changes", "Xbox Game Pass Ultimate"]:
    for forms in ("10-Q", "10-K"):
        try:
            n, url = fts_count(ph, cik=CIK, forms=forms)
        except Exception as e:
            n, url = "ERR %s" % e, ""
        print("%-28s %-5s %s  %s" % (ph, forms, n, url))
