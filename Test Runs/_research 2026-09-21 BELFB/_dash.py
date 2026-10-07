# -*- coding: utf-8 -*-
"""Remove em dashes from MY prose only. Em dashes inside verbatim corpus quotations are
PROTECTED: PRIME RULE 1 forbids smoothing a quotation, and the standing no-em-dash rule is a
rule about what I write."""
import io, re

P = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-21 Run - BELFB Bel Fuse.md"
s = io.open(P, encoding='utf-8').read()

# Protect anything between a pair of straight double quotes (the form every verbatim
# quotation in this file uses) and anything between curly double quotes.
spans = []


def stash(m):
    spans.append(m.group(0))
    return "\x00%d\x00" % (len(spans) - 1)


s2 = re.sub(r'"[^"]*"', stash, s)
s2 = re.sub(u'\u201c[^\u201d]*\u201d', stash, s2)

before = s2.count(u"\u2014")
s2 = s2.replace(u" \u2014 ", " - ")
s2 = s2.replace(u"\u2014", "-")
after = s2.count(u"\u2014")


def unstash(m):
    return spans[int(m.group(1))]


s3 = re.sub(r"\x00(\d+)\x00", unstash, s2)
io.open(P, 'w', encoding='utf-8').write(s3)
protected = sum(q.count(u"\u2014") for q in spans)
print("em dashes in my prose replaced: %d -> %d" % (before, after))
print("em dashes protected inside verbatim quotations: %d" % protected)
print("total remaining in file: %d" % s3.count(u"\u2014"))
