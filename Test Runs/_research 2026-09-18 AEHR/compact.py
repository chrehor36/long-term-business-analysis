import sys, re
for fn in sys.argv[1:]:
    t = open(fn, encoding="utf-8").read()
    t = re.sub(r"\n\s*\|", " |", t)
    t = re.sub(r"\(\s*([\d,\.]+)\s*\|\s*\)", r"(\1)", t)
    t = re.sub(r"\$\s*\|\s*", "$", t)
    t = re.sub(r"(\s*\|)+", " |", t)
    open(fn.replace(".flat.txt", ".c.txt"), "w", encoding="utf-8").write(t)
