"""Append a draft section (from the research folder) to the run file, then delete the draft."""
import sys, os
draft, run = sys.argv[1], sys.argv[2]
text = open(draft, encoding='utf-8').read()
with open(run, 'a', encoding='utf-8') as f:
    f.write('\n' + text.rstrip('\n') + '\n')
os.remove(draft)
print('appended', len(text), 'chars')
