"""Owner cash for JKHY from the filed cash-flow statements (USD millions). Arithmetic only.
OCF, SBC, PPE capex, software developed, software purchased, acquisitions, change in deferred income taxes (statement sign),
interest expense. FY2022-2023 from 10-K FY2023 (0000779152-23-000062); FY2024-2026 from 10-K FY2026 (0000779152-26-000067)."""
d = {
 2022: dict(ocf=504.631, sbc=24.780, ppe=34.659, swd=148.239, swp=8.491, acq=0.0, dtax=31.872, intx=2.384),
 2023: dict(ocf=381.559, sbc=28.611, ppe=39.179, swd=166.120, swp=1.685, acq=229.628, dtax=-48.199, intx=15.073),
 2024: dict(ocf=568.041, sbc=28.873, ppe=58.118, swd=167.175, swp=7.130, acq=0.0, dtax=-0.909, intx=16.384),
 2025: dict(ocf=641.504, sbc=28.392, ppe=53.358, swd=172.445, swp=5.363, acq=0.0, dtax=-3.496, intx=10.438),
 2026: dict(ocf=761.960, sbc=32.460, ppe=67.103, swd=184.243, swp=4.108, acq=42.390, dtax=126.032, intx=5.387),
}
dep = {2022: 50.8, 2023: 48.7, 2024: 46.3, 2025: 43.7, 2026: 42.1}
swam = {2024: 137.958, 2025: 148.734, 2026: 154.212}
T = 0.78  # CONVENTION of this run: after-tax factor on interest expense, one minus an effective rate of about 22%
rows = {}
for y, v in d.items():
    oc = v['ocf'] - v['sbc'] - v['ppe'] - v['swd'] - v['swp']          # all spending, equity-only (interest is in OCF)
    oc_ae = oc + v['intx'] * T                                           # all-equity: before interest expense, after tax
    oc_bt = oc_ae - v['dtax']                                            # at the book tax charge (timing removed)
    rows[y] = (oc, oc_ae, oc_bt, oc_ae - v['acq'])
    print(y, ' eq-only %.1f  all-eq %.1f  all-eq at book tax %.1f  all-eq less acq %.1f' % rows[y])
avg = [sum(r[i] for r in rows.values()) / 5 for i in range(4)]
print('avg', ['%.1f' % a for a in avg], 'acq avg %.1f' % (sum(v['acq'] for v in d.values()) / 5))
g_bt = (rows[2026][2] / rows[2022][2]) ** 0.25 - 1
h1 = (rows[2022][2] + rows[2023][2]) / 2; h2 = (rows[2025][2] + rows[2026][2]) / 2
g_half = (h2 / h1) ** (1 / 3) - 1
g_lit = (rows[2026][1] / rows[2022][1]) ** 0.25 - 1
print('growth at book tax end-to-end %.2f%%; halves %.2f%%; literal as-filed end-to-end %.2f%%' % (g_bt * 100, g_half * 100, g_lit * 100))
