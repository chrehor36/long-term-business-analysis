"""Pull each peer's OWN reported ratio lines out of its 10-K text, for the competitor row."""
import os, re, sys, glob

D = os.path.dirname(os.path.abspath(__file__))
PATS = [
    ("ROTCE", r"(?i)return on average tangible common (?:shareholders.? |stock)?equity"),
    ("ROTCE2", r"(?i)\bROTCE\b"),
    ("EFF", r"(?i)efficiency ratio"),
    ("NIM", r"(?i)net interest margin"),
    ("COSTDEP", r"(?i)(cost of (total )?deposits|rate paid on (total )?deposits|average (rate|cost) (paid )?on .{0,20}deposits)"),
]


def scan(path, pat, maxhits=6, width=260):
    txt = open(path, encoding="utf-8", errors="ignore").read()
    lines = txt.split("\n")
    hits = []
    for i, ln in enumerate(lines):
        if re.search(pat, ln):
            s = ln.strip()
            if len(s) > width:
                s = s[:width]
            hits.append((i + 1, s))
            if len(hits) >= maxhits:
                break
    return hits


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(glob.glob(os.path.join(D, "peer_*_*.txt")))
    for f in files:
        b = os.path.basename(f)
        if which and which not in b:
            continue
        print("#" * 78)
        print(b)
        for label, pat in PATS:
            if len(sys.argv) > 2 and sys.argv[2] != label:
                continue
            hits = scan(f, pat)
            if not hits:
                continue
            print(" --", label)
            for ln, s in hits:
                print("   %6d | %s" % (ln, s))
