import sys, io, re
exec(open('verify2.py', encoding='utf-8').read().split("md = open")[0])
md = open('PEERS.md', encoding='utf-8').read()
n = miss = 0
for line in md.splitlines():
    if line.startswith('>'):
        continue
    for q in re.findall(r'"([^"]{40,}?)"', line):
        n += 1
        qn = norm(q).rstrip('.;,')
        if not found(qn):
            miss += 1
            print('MISS ::', q[:200])
print('inline checked', n, 'missing', miss)
