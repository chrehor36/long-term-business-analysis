# Wrapper: CNIG is no longer in SEC's ticker file (Form 15-12G, 2022-07-07); map it to CIK 1582244
# and call tools/run.py main() unchanged. Arithmetic lines only are used.
import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources as S
_orig = S.ticker_map
def tm():
    m = dict(_orig()); m["CNIG"] = ("0001582244", "Corning Natural Gas Holding Corp"); return m
S.ticker_map = tm
# No quote exists (Yahoo 404 on CNIG, 2026-10-17). The per-share lines below use the 2022-07-06 merger
# consideration of $24.75 as a PLACEHOLDER only, not a price at which anything can be bought.
S.price = lambda t: (24.75, '2022-07-06 (merger consideration, placeholder, not a quote)', 'USD')
import run
run.S.price = S.price
run.S.ticker_map = tm
sys.argv = ["run.py"] + sys.argv[1:]
run.main()
