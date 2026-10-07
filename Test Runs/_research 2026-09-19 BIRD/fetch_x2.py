from fetch_core import *
ex = exhibits("0001437749-26-024887"); print(ex)
for n in ex:
    if n.lower().startswith("ex") and n.endswith(".htm"):
        grab("0001437749-26-024887", n, "EX16_2026-07-29_" + n.replace(".htm",""))
