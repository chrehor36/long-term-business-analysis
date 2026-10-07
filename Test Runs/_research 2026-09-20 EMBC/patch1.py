p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-20 Run - EMBC Embecta.md"
s=open(p,encoding='utf-8').read()
anchor="""A 39.4% net margin in FY2020 against 8.8% in FY2025 on almost identical revenue is not a
business that deteriorated by that much."""
assert anchor in s
add = """**The filing says this itself.** FY2022 10-K, Note 1, accession **0001872789-22-000024**:

> "Prior to the Separation on April 1, 2022, the Company's historical combined financial
> statements were prepared on a standalone basis and were derived from BD's consolidated
> financial statements and accounting records. ... Prior to the Separation, the Company was
> referred to as the Diabetes Care Business. ... **The Consolidated Financial Statements did
> not purport to reflect what the Company's results of operations, comprehensive income,
> financial position, equity or cash flows would have been had the Company operated as a
> standalone public company during the periods presented.**"

"""
s=s.replace(anchor, add+anchor,1)
open(p,'w',encoding='utf-8').write(s)
print("ok",len(s))
