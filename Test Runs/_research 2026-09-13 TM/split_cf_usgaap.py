"""US GAAP era (FY2017-FY2020): the supplemental cash-flow statement is columnar per year
(Non-Financial Services | Financial Services | Consolidated). Print label -> three values, per year block.
Transcription aid; figures are re-read against this printout of the filed text."""
import re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
NUM = re.compile(r"^\(?\s*[\d,]+\s*\)?$|^—$")
for fn in sys.argv[1:]:
    L = [l.strip() for l in open(os.path.join(HERE, fn), encoding="utf-8").read().split("\n")]
    L = [l for l in L if l not in ("", "|", ")", ") |")]
    starts = []
    for i, l in enumerate(L):
        m = re.match(r"For the year ended March 31, (\d{4})$", l)
        if m and any(x.startswith("Non-Financial") for x in L[i:i + 4]) and \
                any("Cash flows from operating activities" in x for x in L[i:i + 14]):
            starts.append((i, m.group(1)))
    print("#" * 10, fn, [s[1] for s in starts])
    for i0, yr in starts:
        print("=== FY", yr)
        i = i0 + 1
        label, vals, out = None, [], []
        while i < len(L) and i < i0 + 400:
            l = L[i].replace("~", "").strip()
            l2 = l.replace(" ", "")
            if re.fullmatch(r"\(?[\d,]+\)?\|?", l2) or l2 in ("—", "—|"):
                v = l2.strip("|")
                neg = v.startswith("(")
                v = v.strip("()")
                vals.append(0 if v == "—" else (-1 if neg else 1) * int(v.replace(",", "")))
            elif l.startswith("(") and re.fullmatch(r"\([\d, ]+", l):
                vals.append(-int(l.strip("( ").replace(",", "").replace(" ", "")))
            else:
                if label and vals:
                    out.append((label, vals[:6]))
                label, vals = l, []
                if l.startswith("Cash and cash equivalents at end of year"):
                    pass
            i += 1
            if label and label.startswith("Cash and cash equivalents at end of year") and len(vals) >= (6 if '/' in yr else 3):
                out.append((label, vals[:6])); break
        for lab, v in out:
            print(f"  {lab[:95]:95s} {v}")
