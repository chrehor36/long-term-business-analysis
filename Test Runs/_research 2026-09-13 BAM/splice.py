import io,sys
RUN=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - BAM Brookfield Asset Management.md"
t=open(RUN,encoding='utf-8').read()
q2=open('q2.md',encoding='utf-8').read()
start=t.index('## Q2 — IS IT A FRANCHISE?')
end=t.index('## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?')
t=t[:start]+q2+'\n'+t[end:]
# sovereign confirmation line, dated addendum inside Step 0
anchor='  not inherited from it.\n'
add=anchor+'- **RE-STRUCK 2026-09-13, at the resume of this run** (the session that wrote Step 0 was killed\n  at 01:44): `python tools/sources.py` returns **USD 5.35% at 09/11/2026, US Treasury daily par\n  yield curve**. **Unchanged.** Recorded as a dated confirmation rather than an overwrite. (JPY\n  4.00% at 2026-09-10, also from the issuing authority; the EUR leg failed on an SSL certificate\n  verification error and is not needed — the earnings currency is USD.)\n'
assert anchor in t
t=t.replace(anchor,add,1)
open(RUN,'w',encoding='utf-8').write(t)
print('lines now',t.count(chr(10))+1)
