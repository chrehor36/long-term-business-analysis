"""Replace one section of the run file (from a line starting with PREFIX up to the next '## ' heading,
or up to a '---' line directly before it) with the contents of a text file.
python section.py "## Q1" newtext.md"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.abspath(os.path.join(HERE, "..", "2026-10-06 Run - V Visa.md"))
prefix, src = sys.argv[1], sys.argv[2]
new = open(src).read().rstrip("\n") + "\n\n"
lines = open(RUN).read().split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith(prefix))
end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
while end - 1 > start and lines[end - 1].strip() in ("", "---"):
    end -= 1
if any(l.strip() == "---" for l in lines[end:end + 3]) and lines[end].strip() == "":
    end += 0
out = lines[:start] + new.rstrip("\n").split("\n") + [""] + lines[end:]
open(RUN, "w").write("\n".join(out))
print("replaced", lines[start][:60], "lines", start, "to", end)
