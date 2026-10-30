# Pathspec commit of this run's two paths only, retrying while another session holds the git index lock.
# Never removes a lock file; waits up to about 3 minutes. Usage: python commit.py "message"
import subprocess, sys, time, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PATHS = ["Test Runs/2026-10-07 Run - ITW Illinois Tool Works.md", "Test Runs/_research 2026-10-07 ITW"]
msg = sys.argv[1] + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
for i in range(90):
    a = subprocess.run(["git", "add", "--"] + PATHS, cwd=ROOT, capture_output=True, text=True)
    if a.returncode == 0:
        c = subprocess.run(["git", "commit", "-q", "-m", msg, "--"] + PATHS, cwd=ROOT, capture_output=True, text=True)
        if c.returncode == 0:
            print("committed on try", i + 1)
            print(subprocess.run(["git", "log", "--oneline", "-1"], cwd=ROOT, capture_output=True, text=True).stdout)
            sys.exit(0)
        err = c.stderr
    else:
        err = a.stderr
    if "lock" not in err:
        print(err); sys.exit(1)
    time.sleep(2)
print("gave up: lock held throughout"); sys.exit(2)
