# usage: python splice.py SECTION_FILE START_HEADING END_HEADING  -> replace run-file text from START (inclusive) to END (exclusive)
import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - ERIC Ericsson.md"
sec, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(RUN, encoding='utf-8').read()
i = t.index(start); j = t.index(end, i + len(start))
new = open(sec, encoding='utf-8').read().rstrip('\n') + '\n\n'
open(RUN, 'w', encoding='utf-8').write(t[:i] + new + t[j:])
print('spliced', sec, len(new))
