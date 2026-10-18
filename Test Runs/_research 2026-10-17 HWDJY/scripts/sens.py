import importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location('v', 'scripts/value.py'); v = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(v)
a = sum(v.S[y] for y in range(2015,2018))/3; b = sum(v.S[y] for y in range(2018,2023))/5
g = (b/a)**(1/4)-1
top = v.ps(v.value(v.base, g, 0.10) + v.value(v.diy_base, v.diy_g, 0.10))
print(f"partial-cycle growth {100*g:.2f}% ; top at 10% {top:.0f}p")
