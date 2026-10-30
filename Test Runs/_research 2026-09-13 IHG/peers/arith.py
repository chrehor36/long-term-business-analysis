import sys, json
d = json.loads(sys.argv[1])
ocf,sbc,cap,ca = d['ocf'],d['sbc'],d['cap'],d['ca']
m = lambda a: round(sum(a[2:])/5,2)
print('means 2021-2025 OCF',m(ocf),'capex',m(cap),'SBC',m(sbc),'CA',m(ca))
for key in ('sw',):
    if key in d: print('software mean', m(d[key]))
inside = d['inside']
for i,y in enumerate(range(2019,2026)):
    v = ocf[i]-sbc[i]-cap[i] - (0 if inside else ca[i])
    extra = ''
    if 'sw' in d: extra = ' | also less capitalized software: %d' % (v - d['sw'][i])
    print(y, v, extra)
f = d['fee']; print('fee', f, 'ratio', round(f[1]/f[0],4))
