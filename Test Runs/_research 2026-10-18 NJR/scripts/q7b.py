import importlib.util,io,contextlib
spec=importlib.util.spec_from_file_location('q7','scripts/q7.py'); m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
rev={2021:2156.613,2022:2905.979,2023:1962.994,2024:1796.539,2025:2036.412}
for y in rev: print(y,'maintenance OC all-equity share of revenue',f"{m.rows[y]['mnt_ae']/rev[y]:.1%}")
gs=(rev[2025]/rev[2021])**0.25-1
print(f"sales growth FY2021-25 {gs:.2%}; shown OC growth end-years {m.g_end:.2%}; halves {m.g_half:.2%}")
yr10=m.A['mnt_ae']*(1+m.g_end)**10; print(f"year-10 OC at shown rate {yr10:.1f}; share of 2025 sales {yr10/rev[2025]:.1%}; of sales carried at sales growth {yr10/(rev[2025]*(1+gs)**10):.1%}")
def irr(b,g,spend):
    base = m.ev if b=='ae' else m.mcap
    lo,hi=0.0001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        lo,hi=(mid,hi) if m.pv(m.A['mnt_'+b],g,mid,spend=spend)>base else (lo,mid)
    return lo
for lab,g in [('capped (sales growth)',gs),('shown, uncapped',m.g_end),('halves',m.g_half)]:
  for b in ['ae','eq']:
    mm=m.A['mnt_'+b]; gc=m.A['growth_cap']
    v=m.pv(mm,g,m.R,spend=gc); f=m.pv(mm,g,m.F,spend=gc); t=m.pv(mm,0,m.R); ft=m.pv(mm,0,m.F)
    print(f"{lab:22s} g={g:6.2%} [{b}] growth case ${m.per_share(v,b):7.2f}  top ${m.per_share(t,b):6.2f}  fair avg ${(m.per_share(f,b)+m.per_share(ft,b))/2:7.2f} (top@10% {m.per_share(ft,b):.2f}, growth@10% {m.per_share(f,b):.2f})  IRR at price: growth case {irr(b,g,gc) if m.pv(mm,g,0.0001,spend=gc)>0 else float('nan'):.2%}")
for b in ['ae','eq']: print(f"[{b}] IRR at price, top case (maintenance, no growth): {irr(b,0,0):.2%}")
# literal ten-year window beside
for b in ['ae','eq']:
    t=m.A10['mnt_'+b]/m.R; print(f"[{b}] literal 10-yr window FY2016-25, maintenance no-growth: ${m.per_share(t,b):.2f}/sh")
# statutory-tax sensitivity: cash taxes paid vs provision
paid={2021:6.381,2022:4.252,2023:4.282,2024:21.313,2025:9.883}; prov={2021:33.286,2022:76.195,2023:49.275,2024:84.906,2025:96.956}
d=sum(prov[y]-paid[y] for y in paid)/5
print(f"avg (provision - cash taxes) FY2021-25: {d:.1f}M; maintenance all-equity OC at book tax {m.A['mnt_ae']-d:.1f} -> top ${m.per_share((m.A['mnt_ae']-d)/m.R,'ae'):.2f}")
