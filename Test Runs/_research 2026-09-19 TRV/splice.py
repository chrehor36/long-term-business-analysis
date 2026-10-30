"""Splice a section file into the TRV run file between two anchor strings.

usage: python splice.py <section-file> <start-anchor> <end-anchor>
The run file's text from <start-anchor> up to (not including) <end-anchor>
is replaced by the section file's contents. Anchors must each occur once.
"""
import sys, io, os

RUN = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "2026-09-19 Run - TRV Travelers.md")
RUN = os.path.normpath(RUN)

sec_path, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
sec = io.open(sec_path, encoding="utf-8").read()
s = io.open(RUN, encoding="utf-8").read()

if s.count(start) != 1:
    sys.exit("start anchor occurs %d times: %r" % (s.count(start), start))
if s.count(end) != 1:
    sys.exit("end anchor occurs %d times: %r" % (s.count(end), end))
i0 = s.index(start)
i1 = s.index(end)
if not i0 < i1:
    sys.exit("anchors out of order")
out = s[:i0] + sec + s[i1:]
io.open(RUN, "w", encoding="utf-8").write(out)
print("spliced %s: %d -> %d bytes" % (os.path.basename(sec_path), len(s), len(out)))
