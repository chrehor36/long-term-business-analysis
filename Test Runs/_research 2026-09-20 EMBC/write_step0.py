import io,os
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-20 Run - EMBC Embecta.md"
s=open(p,encoding='utf-8').read()

old_head = """# Company Run \u2014 [COMPANY] ([TICKER]) \u2014 [DATE]"""
new_head = """# Company Run \u2014 Embecta Corp. (EMBC) \u2014 2026-09-20"""
assert old_head in s
s = s.replace(old_head, new_head)

marker = "Fill top to bottom. **Stop at the first verdict that is not IN.**"
assert marker in s
s = s.replace(marker, """Wave 7, name 7. Research folder: `Test Runs/_research 2026-09-20 EMBC/`.
Corpus quotes are verbatim with a ledger id.

""" + marker, 1)

a = s.index("## STEP 0 \u2014 THE RATE, AND THE FILING")
b = s.index("## Q1 \u2014 CAN I UNDERSTAND HOW THIS MAKES MONEY?")
step0 = open(os.path.join(os.path.dirname(p), "_research 2026-09-20 EMBC", "_step0.md"), encoding="utf-8").read()
s = s[:a] + step0 + s[b:]
open(p,'w',encoding='utf-8').write(s)
print("written", len(s))
