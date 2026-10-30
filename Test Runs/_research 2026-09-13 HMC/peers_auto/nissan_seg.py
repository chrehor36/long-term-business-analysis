"""Print Nissan segment-note tables (one cell per line in the PyMuPDF text) as joined rows."""
import re, sys, glob, os

here = os.path.dirname(os.path.abspath(__file__))
for fn in sorted(glob.glob(os.path.join(here, "NISSAN_fr20*.txt"))):
    lines = [l.strip() for l in open(fn, encoding="utf-8")]
    print("#####", os.path.basename(fn), "|", " ".join(l for l in lines[3:20] if l))
    for i, l in enumerate(lines):
        if re.match(r"Segment profits? ?\(?(loss|losses)?\)?$", l) or l in ("Segment profits", "Segment profit (loss)", "Segment profits (losses)", "Segment profit"):
            # walk back to the period header
            j = i
            while j > i - 40 and not re.search(r"fiscal year \(From", lines[j]):
                j -= 1
            page = ""
            for k in range(i, 0, -1):
                if lines[k].startswith("=== PDF PAGE"):
                    page = lines[k]
                    break
            print(" ", page, "::", lines[j])
            print("   ", " | ".join(x for x in lines[j + 1:i + 6] if x))
