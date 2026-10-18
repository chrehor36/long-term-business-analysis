# Dispatcher: run the acceptance test after the fold and save its tail beside the run.
import subprocess, sys
r = subprocess.run([sys.executable, 'tools/check_framework.py'], capture_output=True, text=True, encoding='utf-8', errors='replace')
open('Test Runs/_research 2026-10-17 NWCL/cf_after_fold_out.txt', 'w', encoding='utf-8').write(f"rc={r.returncode}\n" + r.stdout[-400:] + r.stderr[-400:])
