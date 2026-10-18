import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
with open(dst, 'a', encoding='utf-8', newline='\n') as f:
    f.write('\n' + t.rstrip('\n') + '\n')
print('appended', len(t))
