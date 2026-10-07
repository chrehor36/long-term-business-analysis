import re, sys
fn = sys.argv[1]
t = open(fn, encoding="utf-8").read()
t = re.sub(r"[ \t]*\|[ \t]*(\|[ \t]*)*", " | ", t)
t = re.sub(r"\n( \| \n)+", "\n", t)
t = re.sub(r"\n\s*\|\s*\n", "\n", t)
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
# join table rows: lines that are only numbers/parens
t = t.replace("\ufffd", "'")
open(fn.replace(".txt", ".flat.txt"), "w", encoding="utf-8").write(t)
print(fn, len(t))
