# Replace one '## ' section of the run file (matched by its heading prefix) with the text of a draft file.
import sys, io
run, prefix, draft = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(run, encoding="utf-8").read().split("\n")
new = open(draft, encoding="utf-8").read().rstrip("\n").split("\n")
s = next(i for i,l in enumerate(lines) if l.startswith(prefix))
e = next((i for i in range(s+1, len(lines)) if lines[i].startswith("## ")), len(lines))
out = lines[:s] + new + [""] + lines[e:]
open(run, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("replaced lines", s+1, "to", e)
