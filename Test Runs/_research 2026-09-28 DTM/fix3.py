p='body_end.md'
s=open(p,encoding='utf-8').read()
reps=[("""The filings attribute the
  deferral to tax depreciation and the Midwest purchase's *"taxable deemed asset acquisition"*; read, not scored.""",
"""The FY2024 10-K records the
  Midwest purchase as *"a taxable deemed asset acquisition"*; the cause of the deferral was not traced further. Read, not
  scored."""),
("""near-term cash
  requirements are light: *"We have no debt maturing"* before the 2029 notes ($1,100M), revolver to December 2029.""",
"""near-term cash
  requirements are light: *"We have no debt maturing until 2029"* (the 2029 notes, $1,100M), revolver to December 2029.""")]
for a,b in reps:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
