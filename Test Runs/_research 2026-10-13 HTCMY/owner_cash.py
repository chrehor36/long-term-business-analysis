# HTCMY owner cash, from the filed consolidated statements of cash flows (IFRS), millions of yen.
# Source: Annual Securities Reports, 53rd to 62nd terms (English translations, company IR site);
# each year taken from the report that files it as the current year, FY2022 and FY2023 from the 60th
# (restated for discontinued operations), FY2024 and FY2025 from the 62nd.
# FY label = fiscal year starting April (FY2025 = April 2025 to March 2026).
# Fields: ocf, capex, ppe_sale, intang, lease (lease/finance-lease principal paid), nci (dividends to NCI
# plus paid-in capital reductions to NCI), int_paid, int_recv, acq (cash paid for businesses, NCI stakes and
# investments, net of sales and of cash acquired; FY2022 includes the 53,479 ACME guarantee payment, which
# the filer books in operating cash and which ended in the purchase of ACME, so it is moved out of ocf here),
# rev, opinc.
D = {
 2016: dict(ocf=87961, capex=13999, ppe_sale=1998, intang=3304, lease=5556, nci=7862, int_paid=3534, int_recv=2573,
            acq=56070+3807, rev=753947, opinc=23622),   # 53rd: Bradken/H-E Parts purchases in the investments lines
 2017: dict(ocf=84528, capex=16887, ppe_sale=4603, intang=4464, lease=4700, nci=2103, int_paid=5089, int_recv=2548,
            acq=21416-469, rev=959153, opinc=95737),
 2018: dict(ocf=-25693, capex=26231, ppe_sale=5251, intang=8536, lease=6388, nci=4933, int_paid=5357, int_recv=2525,
            acq=1315-318, rev=1033703, opinc=102296),
 2019: dict(ocf=22682, capex=32044, ppe_sale=2951, intang=7311, lease=12770, nci=5544, int_paid=6923, int_recv=2086,
            acq=0-1635, rev=931347, opinc=72849),
 2020: dict(ocf=91339, capex=28311, ppe_sale=389, intang=4893, lease=11534, nci=4255, int_paid=5289, int_recv=2058,
            acq=315-884, rev=813331, opinc=28235),
 2021: dict(ocf=39317, capex=27924, ppe_sale=8923, intang=6616, lease=12699, nci=8857, int_paid=4729, int_recv=1769,
            acq=1030+2642-22592, rev=1024961, opinc=106590),
 2022: dict(ocf=-26135+53479, capex=52839, ppe_sale=11939, intang=6301, lease=11745, nci=9316, int_paid=8858, int_recv=2799,
            acq=53479+19022+3507-7697, rev=1264927, opinc=135665),
 2023: dict(ocf=73035, capex=45728, ppe_sale=716, intang=9875, lease=12890, nci=6747, int_paid=15012, int_recv=3593,
            acq=-14647-1234+592, rev=1405928, opinc=162690),
 2024: dict(ocf=143932, capex=32348, ppe_sale=2312, intang=12726, lease=15040, nci=7622+1591, int_paid=18300, int_recv=5562,
            acq=15946+3623+2359-2-8207, rev=1371285, opinc=154730),
 2025: dict(ocf=164223, capex=40968, ppe_sale=1168, intang=8065, lease=13479, nci=7977+2597, int_paid=16036, int_recv=5606,
            acq=1591-2452, rev=1405493, opinc=130144),
}
T = 0.306  # combined statutory rate, 62nd report tax note
rows = {}
print(f"{'FY':>5} {'OCF':>8} {'netcapex':>9} {'lease':>6} {'NCI':>6} {'OCeq':>8} {'netint':>7} {'OCallEq':>8} {'acq':>7} {'OCaeAfterAcq':>12} {'rev':>9} {'opm%':>5}")
for y, d in D.items():
    netcap = d['capex'] - d['ppe_sale'] + d['intang']
    oc_eq = d['ocf'] - netcap - d['lease'] - d['nci']            # owner cash to the parent's equity, before acquisitions
    netint = (d['int_paid'] - d['int_recv']) * (1 - T)
    oc_ae = oc_eq + netint                                      # all-equity basis: before net interest, after the company's tax
    rows[y] = dict(oc_eq=oc_eq, oc_ae=oc_ae, acq=d['acq'], rev=d['rev'], opm=d['opinc'] / d['rev'])
    print(f"{y:>5} {d['ocf']:>8} {netcap:>9} {d['lease']:>6} {d['nci']:>6} {oc_eq:>8} {netint:>7.0f} {oc_ae:>8.0f} {d['acq']:>7} {oc_ae-d['acq']:>12.0f} {d['rev']:>9} {100*d['opinc']/d['rev']:>5.1f}")

def avg(keys, f): return sum(f(rows[k]) for k in keys) / len(keys)
W5 = [2021, 2022, 2023, 2024, 2025]; W5a = [2016, 2017, 2018, 2019, 2020]; W10 = W5a + W5
for name, ks in (("last five FY2021-25", W5), ("prior five FY2016-20", W5a), ("ten FY2016-25", W10)):
    print(f"{name}: OC all-equity before acq {avg(ks, lambda r: r['oc_ae']):.0f}; after acq {avg(ks, lambda r: r['oc_ae']-r['acq']):.0f}; "
          f"OC equity before acq {avg(ks, lambda r: r['oc_eq']):.0f}; after acq {avg(ks, lambda r: r['oc_eq']-r['acq']):.0f}; "
          f"revenue {avg(ks, lambda r: r['rev']):.0f}; op margin {100*avg(ks, lambda r: r['opm']):.1f}%")
