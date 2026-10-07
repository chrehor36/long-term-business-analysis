p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - UMC United Microelectronics.md"
t = open(p, encoding="utf-8").read()
t = t.replace("# Company Run — [COMPANY] ([TICKER]) — [DATE]", "# Company Run — United Microelectronics Corporation (UMC) — 2026-09-13", 1)
ctx = open("hdr_ctx.md", encoding="utf-8").read()
t = t.replace("Fill top to bottom. **Stop at the first verdict that is not IN.**\n", "Fill top to bottom. **Stop at the first verdict that is not IN.**\n\n" + ctx, 1)
open(p, "w", encoding="utf-8").write(t)
