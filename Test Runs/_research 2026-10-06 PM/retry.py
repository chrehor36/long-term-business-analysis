"""Run a repo tool with backoff on SEC HTTP 429. Usage: python retry.py OUTFILE -- cmd args..."""
import subprocess, sys, time

out = sys.argv[1]
cmd = sys.argv[sys.argv.index("--") + 1:]
for attempt in range(1, 9):
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    text = p.stdout + p.stderr
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    if p.returncode == 0 or "429" not in text:
        print(f"attempt {attempt}: rc={p.returncode}")
        break
    wait = 20 * attempt
    print(f"attempt {attempt}: 429, sleeping {wait}s", flush=True)
    time.sleep(wait)
