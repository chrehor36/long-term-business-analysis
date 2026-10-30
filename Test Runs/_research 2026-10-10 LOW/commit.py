# pathspec commit with lock retry: wait 30 s and retry, up to 10 tries; never delete a lock (the brief).
# Usage: python commit.py "message"
import subprocess, sys, time, os
ROOT = "C:/Users/chreh/OneDrive/Documents/BRK"
R = "Test Runs/2026-10-10 Run - LOW Lowe's.md"
D = "Test Runs/_research 2026-10-10 LOW"
msg = sys.argv[1] + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
for i in range(1, 11):
    locks = [p for p in (".git/index.lock", ".git/HEAD.lock", ".git/refs/heads/master.lock") if os.path.exists(os.path.join(ROOT, p))]
    if not locks:
        a = subprocess.run(["git", "add", "--", R, D], cwd=ROOT, capture_output=True, text=True)
        if a.returncode == 0:
            c = subprocess.run(["git", "commit", "-q", "-m", msg, "--", R, D], cwd=ROOT, capture_output=True, text=True)
            if c.returncode == 0:
                print(f"committed on try {i}", flush=True)
                print(subprocess.run(["git", "log", "--oneline", "-1", "--", R], cwd=ROOT, capture_output=True, text=True).stdout, flush=True)
                sys.exit(0)
            print(f"try {i}: commit failed: {c.stderr.strip()[:200]}", flush=True)
        else:
            print(f"try {i}: add failed: {a.stderr.strip()[:200]}", flush=True)
    else:
        print(f"try {i}: lock present {locks} at {time.strftime('%H:%M:%S')}", flush=True)
    time.sleep(30)
print("gave up after 10 tries", flush=True)
sys.exit(1)
