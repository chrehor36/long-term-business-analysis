import sys, io
RUN = "Test Runs/2026-09-12 Run - ALKT Alkami Technology.md"
start, end, src = sys.argv[1], sys.argv[2], sys.argv[3]
s = io.open(RUN, encoding="utf-8").read()
new = io.open(src, encoding="utf-8").read().rstrip("\n") + "\n\n"
i = s.index(start)
j = s.index(end, i + len(start)) if end != "EOF" else len(s)
s = s[:i] + new + s[j:]
io.open(RUN, "w", encoding="utf-8", newline="\n").write(s)
print("spliced", src, "chars", len(new))
