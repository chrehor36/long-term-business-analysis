"""Run Screens/floor_screen.py AS IT STOOD at a8bc84f (the commit that wrote the wave 5 'capex unresolved' row)
on NVIDIA's companyfacts of today. Extracted copy at %TEMP%/fs_old/floor_screen_a8bc84f.py; nothing in Screens/ is touched."""
import sys, os, json, importlib.util
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
os.chdir(os.path.join(ROOT, "Screens"))
p = os.path.join(os.environ.get("TEMP", r"C:\Users\chreh\AppData\Local\Temp"), "fs_old", "floor_screen_a8bc84f.py")
spec = importlib.util.spec_from_file_location("fs_old", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
HERE = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 NVDA"
facts = json.load(open(os.path.join(HERE, "companyfacts.json")))
print("a8bc84f owner_earnings():", m.owner_earnings(facts))
import inspect
src = inspect.getsource(m.owner_earnings)
print(src[:1500])
for name in ("CAPEX_TAGS", "CAPEX", "CAPEX_TAG_LIST"):
    if hasattr(m, name):
        print(name, getattr(m, name))
try:
    print("annual capex:", m.annual(facts, m.CAPEX_TAGS) if hasattr(m, "CAPEX_TAGS") else "n/a")
except Exception as ex:
    print("annual err", ex)
