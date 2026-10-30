import io,sys,re; sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
f=sys.argv[1]
L=open(f,encoding='utf-8').read().split('\n')
idx=[i for i,l in enumerate(L) if re.search(r'Consolidated Statements? of Cash Flows',l,re.I) and len(l)<100]
print(idx)
i0=idx[int(sys.argv[2])] if len(sys.argv)>2 else idx[-1]
for i in range(i0,i0+int(sys.argv[3]) if len(sys.argv)>3 else i0+80): print(i,L[i][:300])
