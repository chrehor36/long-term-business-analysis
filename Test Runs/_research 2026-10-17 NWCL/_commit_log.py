# Dispatcher: wait for a git index lock to go; clear it only if older than ten minutes with no git process (step 4.1);
# then correct the log line's time to the clock and commit the log with a pathspec. Result in _commit_log_out.txt.
import os, subprocess, time, datetime
D = 'Test Runs/_research 2026-10-17 NWCL'
out = open(D + '/_commit_log_out.txt', 'w', encoding='utf-8')
L = '.git/index.lock'
def gitprocs():
    r = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq git.exe'], capture_output=True, text=True)
    return 'git.exe' in r.stdout
for _ in range(80):
    if not os.path.exists(L): break
    age = time.time() - os.path.getmtime(L)
    if age > 600 and not gitprocs():
        os.remove(L); out.write(f'cleared stale index.lock, age {int(age)}s, no git process\n'); break
    time.sleep(15)
p = 'Screens/_daily/OVERNIGHT LOG.md'
t = open(p, encoding='utf-8').read()
now = datetime.datetime.now().strftime('%H:%M')
t = t.replace('- 2026-10-17 13:05 | NWCL ', f'- 2026-10-17 {now} | NWCL ')
open(p, 'w', encoding='utf-8', newline='').write(t)
files = [p, D + '/cf_after_fold.py', D + '/cf_after_fold_out.txt', D + '/_log_line.py', D + '/_log_msg.txt', D + '/_commit_log.py']
subprocess.run(['git', 'add', '--'] + files)
r = subprocess.run(['git', 'commit', '-q', '-F', D + '/_log_msg.txt', '--'] + files, capture_output=True, text=True)
out.write(f'commit rc={r.returncode}\n{r.stdout}{r.stderr}\n')
out.write(subprocess.run(['git', 'log', '-1', '--oneline'], capture_output=True, text=True).stdout)
out.write('end\n')
