# Run the acceptance test and save its output and exit code beside this script (cache/, gitignored).
import subprocess, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
r = subprocess.run([sys.executable, "tools/check_framework.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
with open(os.path.join(os.path.dirname(__file__), "cache", "check_framework_result.txt"), "w", encoding="utf-8") as f:
    f.write(r.stdout + "\n--- stderr ---\n" + r.stderr + f"\nrc={r.returncode}\n")
