"""Replace one '## ' section of the run file (heading line through the line before the next '## ' or '---').
Usage: python section.py RUNFILE "## Q1" NEWTEXT.md   (NEWTEXT includes its own heading line)"""
import sys

run, prefix, new = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(run, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith(prefix))
end = start + 1
while end < len(lines) and not (lines[end].startswith("## ") or lines[end].strip() == "---"):
    end += 1
body = open(new, encoding="utf-8").read().rstrip("\n").split("\n")
lines[start:end] = body + [""]
open(run, "w", encoding="utf-8").write("\n".join(lines))
print(f"replaced lines {start+1}-{end} with {len(body)} lines")
