"""Pathspec commit with lock retry: wait 30 s, up to ten tries, never delete a lock (the brief)."""
import subprocess, sys, time
RUN = "Test Runs/2026-10-10 Run - LRCX Lam Research.md"; RES = "Test Runs/_research 2026-10-10 LRCX"
msg = open(sys.argv[1], encoding='utf-8').read()
for i in range(1, 11):
    a = subprocess.run(['git', 'add', '--', RUN, RES], capture_output=True, text=True)
    c = a.returncode == 0 and subprocess.run(['git', 'commit', '-q', '-F', sys.argv[1], '--', RUN, RES],
                                             capture_output=True, text=True)
    if a.returncode == 0 and c.returncode == 0:
        print('COMMITTED on try', i, subprocess.run(['git', 'log', '--oneline', '-1', '--', RUN],
                                                   capture_output=True, text=True).stdout.strip(), flush=True)
        sys.exit(0)
    print('try', i, 'failed:', (a.stderr or (c.stderr if c else ''))[:90].replace('\n', ' '), flush=True)
    time.sleep(30)
print('GAVE UP'); sys.exit(1)
