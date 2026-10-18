# Replace the text of a run file between two markers with a draft file's text.
# usage: python -I splice.py runfile start_marker end_marker draftfile
# The start marker is replaced along with the old text; the end marker is kept.
import sys
run, a, b, draft = sys.argv[1:5]
s = open(run, encoding="utf-8").read()
new = open(draft, encoding="utf-8").read()
i = s.index(a)
j = s.index(b, i + len(a)) if b != "<END>" else len(s)
s = s[:i] + new.rstrip("\n") + "\n\n" + s[j:]
open(run, "w", encoding="utf-8").write(s)
print("spliced", len(new), "chars")
