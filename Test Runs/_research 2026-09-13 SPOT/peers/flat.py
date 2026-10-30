import sys, io, re, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
for fn in sys.argv[1:]:
    t = open(fn, encoding='utf-8').read()
    t = re.sub(r'\n\s*\|\s*(?=\n)', ' |', t)
    t = re.sub(r'(\|\s*){2,}', '| ', t)
    t = re.sub(r'\n(?=[%)]\s)', ' ', t)
    t = re.sub(r'\|\s*\n', '| ', t)
    t = re.sub(r'\n\|', ' |', t)
    t = re.sub(r'[ \t]+', ' ', t)
    out = fn.replace('.txt', '.flat.txt')
    open(out, 'w', encoding='utf-8').write(t)
    print(out, len(t), t.count('\n'))
