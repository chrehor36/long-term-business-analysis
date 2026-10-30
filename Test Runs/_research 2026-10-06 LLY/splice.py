"""Replace the run file's text from START marker (inclusive) to END marker (exclusive) with a new block.
usage: python -I splice.py RUNFILE START END NEWBLOCKFILE   (END may be '__EOF__')"""
import sys
p, start, end, newf = sys.argv[1:5]
s = open(p, encoding='utf-8').read()
i = s.index(start)
j = len(s) if end == '__EOF__' else s.index(end, i + 1)
new = open(newf, encoding='utf-8').read()
if not new.endswith('\n'):
    new += '\n'
s = s[:i] + new + ('' if end == '__EOF__' else '\n' + s[j:])
open(p, 'w', encoding='utf-8').write(s)
print('spliced', i, j)
