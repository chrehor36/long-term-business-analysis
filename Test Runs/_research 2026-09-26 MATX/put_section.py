import sys
run, start, end, src = sys.argv[1:5]
t = open(run, encoding='utf-8').read()
new = open(src, encoding='utf-8').read()
i = t.index(start)
j = t.index(end, i + len(start)) if end != 'EOF' else len(t)
assert t.count(start) == 1, 'start marker not unique'
t = t[:i] + new.rstrip('\n') + '\n' + t[j:]
open(run, 'w', encoding='utf-8', newline='\n').write(t)
print('ok', len(t))
