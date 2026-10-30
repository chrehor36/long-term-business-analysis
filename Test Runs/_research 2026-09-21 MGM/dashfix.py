# -*- coding: utf-8 -*-
"""Remove em dashes from the run file's OWN PROSE only.

PRIME RULE 1 keeps verbatim quotation exactly as sourced, so an em dash inside a quoted span
or inside a markdown blockquote line STAYS. The literal required heading
COMPUTATION -- NOT A CLEARANCE keeps its em dash too. Everything else becomes a hyphen.
"""
import io, os, sys

EM = u"—"
LQ = u"“"
RQ = u"”"
HEADING = u"# COMPUTATION — NOT A CLEARANCE"

P = sys.argv[1]
src = io.open(P, encoding="utf-8").read()

out_lines = []
kept = 0
changed = 0
for line in src.split("\n"):
    if line.strip().startswith(">") or line.strip() == HEADING.strip():
        kept += line.count(EM)
        out_lines.append(line)
        continue
    buf = []
    in_quote = False
    for ch in line:
        if ch == LQ:
            in_quote = True
            buf.append(ch)
        elif ch == RQ:
            in_quote = False
            buf.append(ch)
        elif ch == EM:
            if in_quote:
                kept += 1
                buf.append(ch)
            else:
                changed += 1
                buf.append(u"-")
        else:
            buf.append(ch)
    out_lines.append("".join(buf))

res = "\n".join(out_lines)
io.open(P, "w", encoding="utf-8").write(res)
print("em dashes converted in own prose:", changed)
print("em dashes kept (verbatim quotation / blockquote / required heading):", kept)
print("remaining in file:", res.count(EM))
