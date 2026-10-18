"""Flatten the consolidated balance sheet / cash-flow statement of a cached 20-F and print chosen lines. Transcription only."""
import re, sys
name, start_pat, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
t = open(f"cache/{name}.txt", encoding="utf-8").read()
idx = [m.start() for m in re.finditer(start_pat, t)]
pos = idx[-1] if len(idx) > 1 else idx[0]
seg = t[pos:pos+n].replace("\n", " ")
seg = re.sub(r"\s*\|\s*", " ", seg); seg = re.sub(r"[​]", "", seg); seg = re.sub(r"\s+", " ", seg)
print(seg)
