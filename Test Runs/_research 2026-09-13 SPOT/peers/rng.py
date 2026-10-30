import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
t = open(sys.argv[1], encoding='utf-8').read()
print(t[int(sys.argv[2]):int(sys.argv[3])])
