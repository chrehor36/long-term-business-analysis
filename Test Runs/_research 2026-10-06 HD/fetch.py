"""Fetch EDGAR documents for the HD run into cache/ (gitignored). Usage: python fetch.py URL OUTNAME [URL OUTNAME ...]
Descriptive User-Agent per SEC policy; a pause between requests keeps well under the rate limit."""
import subprocess, sys, time, os
UA = "Long-Term Business Analysis research chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
os.makedirs(cache, exist_ok=True)
args = sys.argv[1:]
for url, name in zip(args[::2], args[1::2]):
    out = os.path.join(cache, name)
    subprocess.run(["curl", "-sS", "-A", UA, url, "-o", out], check=True)
    print(name, os.path.getsize(out))
    time.sleep(0.4)
