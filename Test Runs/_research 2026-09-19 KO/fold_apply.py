import re, sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\WATCHLIST RUN QUEUE.md"
t = open(p, encoding="utf-8").read()
lines = t.split("\n")
s = [i for i, l in enumerate(lines) if l.strip() == "## COMPLETED FROM THE QUEUE"][0]
e = [i for i, l in enumerate(lines) if l.startswith("## THE WRITE-EARLY PROTOCOL")][0]
pat = re.compile(r"- \*\*([A-Z0-9.\-]+)[ ,(]")
ent = [pat.match(lines[i]).group(1) for i in range(s + 1, e) if pat.match(lines[i])]
print("entries before", len(ent), "KO present", "KO" in ent)
assert "KO" not in ent
entry = open(r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-19 KO\_register_entry.md", encoding="utf-8").read().rstrip("\n")
entry = entry.replace("{N}", str(len(ent) + 1)).replace("{PRIOR}", str(len(ent)))
lines.insert(s + 1, entry)
t2 = "\n".join(lines)
old = "| KO | The Coca-Cola Company | ordinary | **RUN** |"
assert t2.count(old) == 1
t2 = t2.replace(old, "| ~~KO~~ | The Coca-Cola Company | ordinary | **RUN** - done 2026-09-19, register entry %d: all four gates IN, FAIL at Q5 on price |" % (len(ent) + 1))
open(p, "w", encoding="utf-8").write(t2)
lines = t2.split("\n")
s = [i for i, l in enumerate(lines) if l.strip() == "## COMPLETED FROM THE QUEUE"][0]
e = [i for i, l in enumerate(lines) if l.startswith("## THE WRITE-EARLY PROTOCOL")][0]
ent = [pat.match(lines[i]).group(1) for i in range(s + 1, e) if pat.match(lines[i])]
print("entries after", len(ent), ent[:3])
