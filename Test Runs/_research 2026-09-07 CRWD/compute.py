# -*- coding: utf-8 -*-
# Arithmetic only. Every input is a filed line item, keyed to its accession.
D = {}
def add(k, **kw): D[k]=kw

# units: CRWD & S in $ thousands; PANW, FTNT, MSFT in $ millions
add('CRWD FY2026', unit='K', fye='2026-01-31', acc='0001535527-26-000010',
    rev=4812005, sub_rev=4564683, oth_rev=247322, cogs=1218929, sub_cogs=1015915,
    gp=3593076, opinc=-293292, ni=-161165, sbc=1096679, ocf=1612349,
    ta=11086684, gw=1363294, intang=136702, cash=5230125, sti=0, lti=0, othinv=76832,
    ap=105319, accr=181089+389690, dr=3421051+1332387, eq=4472605)
add('CRWD FY2023', unit='K', fye='2023-01-31', acc='0001535527-23-000008',
    rev=2241236, sub_rev=2111660, oth_rev=129576, cogs=601231, sub_cogs=511684,
    gp=1640005, opinc=-190112, ni=-182285, sbc=526504, ocf=941007,
    ta=5026540, gw=430645, intang=86889, cash=2455369, sti=250000, lti=0, othinv=47270,
    ap=45372, accr=137884+168767, dr=1727484+627629, eq=1487434)
add('PANW FY2025', unit='M', fye='2025-07-31', acc='0001327567-25-000027',
    rev=9221.5, sub_rev=7419.6, oth_rev=1801.9, cogs=2451.6, sub_cogs=2038.4,
    gp=6769.9, opinc=1242.9, ni=1133.9, sbc=1295.1, ocf=3716.0,
    ta=23576.2, gw=4566.6, intang=762.7, cash=2268.6, sti=634.6, lti=5555.6, othinv=0,
    ap=232.2, accr=607.6+846.0, dr=6302.2+6449.7, eq=7824.4)
add('PANW FY2022', unit='M', fye='2022-07-31', acc='0001327567-22-000028',
    rev=5501.5, sub_rev=4138.4, oth_rev=1363.1, cogs=1718.7, sub_cogs=1263.2,
    gp=3782.8, opinc=-188.8, ni=-267.0, sbc=1011.1, ocf=1984.7,
    ta=12253.6, gw=2747.7, intang=384.5, cash=2118.5, sti=1516.0, lti=1051.9, othinv=0,
    ap=128.0, accr=461.1+399.2, dr=3641.2+3352.8, eq=210.0)
add('S FY2026', unit='K', fye='2026-01-31', acc='0001583708-26-000020',
    rev=1001278, sub_rev=None, oth_rev=None, cogs=259177, sub_cogs=None,
    gp=742101, opinc=-321309, ni=-450735, sbc=297587, ocf=76616,
    ta=2438102, gw=912671, intang=129548, cash=169627, sti=459041, lti=140898, othinv=0,
    ap=10299, accr=79006+117260, dr=549790+83277, eq=1437145)
add('S FY2023', unit='K', fye='2023-01-31', acc='0001583708-23-000014',
    rev=422179, sub_rev=None, oth_rev=None, cogs=144177, sub_cogs=None,
    gp=278002, opinc=-402576, ni=-378678, sbc=164466, ocf=-193287,
    ta=2258913, gw=540308, intang=145093, cash=137941, sti=485584, lti=535422, othinv=0,
    ap=11214, accr=100015+54955, dr=303200+103062, eq=1656705)
add('FTNT FY2025', unit='M', fye='2025-12-31', acc='0001262039-26-000007',
    rev=6799.6, sub_rev=4581.2, oth_rev=2218.4, cogs=1328.9, sub_cogs=603.5,
    gp=5470.7, opinc=2084.7, ni=1853.4, sbc=279.5, ocf=2590.6,
    ta=10389.2, gw=257.4, intang=97.3, cash=2495.3, sti=1087.2, lti=339.7, othinv=0,
    ap=230.8, accr=354.6+312.9, dr=3636.0+3479.8, eq=1237.5)
add('FTNT FY2022', unit='M', fye='2022-12-31', acc='0001262039-23-000010',
    rev=4417.4, sub_rev=2636.9, oth_rev=1780.5, cogs=1084.9, sub_cogs=393.6,
    gp=3332.5, opinc=969.6, ni=857.3, sbc=217.3, ocf=1730.6,
    ta=6228.0, gw=128.0, intang=56.0, cash=1682.9, sti=502.6, lti=45.5, othinv=25.5,
    ap=243.4, accr=266.3+219.4, dr=2349.3+2291.0, eq=-281.6)
add('MSFT FY2026', unit='M', fye='2026-06-30', acc='0001193125-26-323660',
    rev=331839, sub_rev=267143, oth_rev=64696, cogs=106374, sub_cogs=94276,
    gp=225465, opinc=155237, ni=133749, sbc=12405, ocf=182935,
    ta=758376, gw=119651, intang=18609, cash=20935, sti=55908, lti=0, othinv=36348,
    ap=42416, accr=14945, dr=72965+2747, eq=442387)
add('MSFT FY2023', unit='M', fye='2023-06-30', acc='0000950170-23-035122',
    rev=211915, sub_rev=147216, oth_rev=64699, cogs=65863, sub_cogs=48059,
    gp=146052, opinc=88523, ni=72361, sbc=9611, ocf=87582,
    ta=411976, gw=67886, intang=9366, cash=34704, sti=76558, lti=0, othinv=9879,
    ap=18095, accr=11009, dr=50901+2912, eq=206223)

def pct(n,d):
    return None if (d is None or d==0 or n is None) else 100.0*n/d
rows=[]
for k,v in D.items():
    ci = v['cash']+v['sti']+v['lti']+v['othinv']
    nibcl = v['ap']+v['accr']+v['dr']
    ntoa = v['ta']-v['gw']-v['intang']-ci-nibcl
    subgm = None
    if v['sub_rev'] is not None:
        subgm = pct(v['sub_rev']-v['sub_cogs'], v['sub_rev'])
    rows.append(dict(name=k, unit=v['unit'], fye=v['fye'], acc=v['acc'],
        rev=v['rev'], gm=pct(v['gp'],v['rev']), subgm=subgm,
        opinc=v['opinc'], om=pct(v['opinc'],v['rev']), ni=v['ni'],
        sbc=v['sbc'], ocf=v['ocf'], sbcocf=pct(v['sbc'],v['ocf']),
        sbcrev=pct(v['sbc'],v['rev']),
        ta=v['ta'], gw=v['gw'], intang=v['intang'], ci=ci, nibcl=nibcl, ntoa=ntoa, eq=v['eq'],
        roi=(pct(v['opinc'],ntoa) if ntoa>0 else None)))
def f(x,p=1):
    return 'n/a' if x is None else f"{x:,.{p}f}"
print(f"{'':16s} {'unit':4s} {'rev':>12s} {'GM%':>6s} {'subGM%':>7s} {'opinc':>11s} {'OM%':>7s} {'NI':>11s} {'SBC':>10s} {'OCF':>11s} {'SBC/OCF%':>9s} {'SBC/rev%':>8s}")
for r in rows:
    print(f"{r['name']:16s} {r['unit']:4s} {f(r['rev'],0):>12s} {f(r['gm']):>6s} {f(r['subgm']):>7s} {f(r['opinc'],0):>11s} {f(r['om']):>7s} {f(r['ni'],0):>11s} {f(r['sbc'],0):>10s} {f(r['ocf'],0):>11s} {f(r['sbcocf']):>9s} {f(r['sbcrev']):>8s}")
print()
print(f"{'':16s} {'TA':>12s} {'GW':>10s} {'Intang':>9s} {'Cash+Inv':>11s} {'NIBCL':>11s} {'NTOA':>12s} {'Equity':>11s} {'OpInc/NTOA%':>11s}")
for r in rows:
    print(f"{r['name']:16s} {f(r['ta'],0):>12s} {f(r['gw'],0):>10s} {f(r['intang'],0):>9s} {f(r['ci'],0):>11s} {f(r['nibcl'],0):>11s} {f(r['ntoa'],0):>12s} {f(r['eq'],0):>11s} {f(r['roi']):>11s}")
