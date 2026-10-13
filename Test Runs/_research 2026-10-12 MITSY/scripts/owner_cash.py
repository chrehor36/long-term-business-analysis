"""Mitsui & Co. owner cash, FY2016-FY2026 (fiscal years ended March 31), Mn JPY, from the filed IFRS cash-flow statements
in the English Annual Securities Reports (98th, 100th, 102nd, 104th, 106th, 107th). Each line is typed from the page-row
extracts in ../extracts and checked: the investing lines are summed and compared with the filed investing total.
Definitions (this run's arithmetic; the framework's rules are in the run file):
  net_ppe  = purchases of PP&E and investment property, less proceeds from their sale
  net_biz  = investments in equity-method investees + other investments + subsidiaries/businesses, less proceeds from sales
             (businesses bought net of businesses sold: Q7 specific (c), capital spending for the range)
  net_loan = loans made less collections
  OC_all   = CFO - net_ppe - net_biz - net_loan - lease principal - transactions with NCI   (equity-only, after interest)
  OC_all_unlev = OC_all + interest paid x (1 - 31.5%)                                        (all-equity basis)
  maint    = D&A less right-of-use depreciation (lease cost is deducted as principal repaid); OC_maint = CFO - maint - lease - NCI
CFO includes dividends received from equity-method investees and not the share of their profit (the framework's
equity-method convention), and it includes working-capital changes (Q7 specific (d))."""
T = 0.315
D = {  # fy: dict
 2016: dict(cfo=586991, ppe=-300832, ppe_s=28109, eq=-199807, eq_s=73429, oth=-65769, oth_s=88196, ln=-2859, ln_s=16956, sub=-45851, sub_s=0, td=369, cfi=-408059, lease=0, nci=-425, intp=-51232, da=253168, rou=0, ni=-83410, divrec=220160, eqsh=-132033),
 2017: dict(cfo=404171, ppe=-191472, ppe_s=39434, eq=-319131, eq_s=92344, oth=-70357, oth_s=142524, ln=-56939, ln_s=19234, sub=0, sub_s=0, td=-8936, cfi=-353299, lease=0, nci=-47249, intp=-65352, da=193329, rou=0, ni=306136, divrec=194698, eqsh=170569),
 2018: dict(cfo=553645, ppe=-174154-23314, ppe_s=38440+15236, eq=-204610, eq_s=89615, oth=-83507, oth_s=59984, ln=-75799, ln_s=101530, sub=0, sub_s=0, td=8368, cfi=-248211, lease=0, nci=-46193, intp=-69935, da=192587, rou=0, ni=418479, divrec=376422, eqsh=234941),
 2019: dict(cfo=410670, ppe=-307719-18488, ppe_s=52156+11597, eq=-421778, eq_s=44655, oth=-95976, oth_s=72557, ln=-74769, ln_s=34450, sub=-76913, sub_s=64408, td=-3216, cfi=-719036, lease=0, nci=1724, intp=-82839, da=186322, rou=0, ni=414215, divrec=318703, eqsh=255367),
 2020: dict(cfo=526376, ppe=-287839-23404, ppe_s=34712+6882, eq=-87901, eq_s=97002, oth=-32754, oth_s=103503, ln=-32077, ln_s=32823, sub=0, sub_s=0, td=3823, cfi=-185230, lease=-60861, nci=-7776, intp=-96624, da=256125, rou=52392, ni=391513, divrec=299244, eqsh=269232),
 2021: dict(cfo=772696, ppe=-215690-61694, ppe_s=9286+8576, eq=-89611, eq_s=33093, oth=-43128, oth_s=52590, ln=-24975, ln_s=39159, sub=0, sub_s=0, td=-30080, cfi=-322474, lease=-58380, nci=-18208, intp=-59904, da=273639, rou=46119, ni=335458, divrec=307838, eqsh=227910),
 2022: dict(cfo=806896, ppe=-185525-26428, ppe_s=28889+21902, eq=-92131, eq_s=65064, oth=-106017, oth_s=62256, ln=-28759, ln_s=78764, sub=0, sub_s=0, td=794, cfi=-181191, lease=-55630, nci=-98076, intp=-49278, da=296396, rou=46760, ni=914722, divrec=554764, eqsh=431263),
 2023: dict(cfo=1047537, ppe=-228065-12303, ppe_s=38022+60705, eq=-238613, eq_s=135185, oth=-100431, oth_s=134297, ln=-27875, ln_s=23689, sub=0, sub_s=0, td=37048, cfi=-178341, lease=-65454, nci=-51934, intp=-96668, da=272689, rou=53047, ni=1130630, divrec=574208, eqsh=555526),
 2024: dict(cfo=864419, ppe=-294771-8481, ppe_s=50507+37573, eq=-449802, eq_s=143716, oth=-92432, oth_s=112556, ln=-15768, ln_s=39783, sub=-106302, sub_s=152919, td=2955, cfi=-427547, lease=-73984, nci=-10522, intp=-157442, da=293573, rou=59749, ni=1063684, divrec=550836, eqsh=491564),
 2025: dict(cfo=1017518, ppe=-346147-12671, ppe_s=13311+120124, eq=-255066, eq_s=214510, oth=-57494, oth_s=162304, ln=-28125, ln_s=66756, sub=-65269, sub_s=24049, td=1730, cfi=-161988, lease=-90066, nci=-30119, intp=-199042, da=313730, rou=72467, ni=900342, divrec=636061, eqsh=494076),
 2026: dict(cfo=952912, ppe=-1108399-1187, ppe_s=74599+48964, eq=-159528, eq_s=68653, oth=-48135, oth_s=116102, ln=-34818, ln_s=34755, sub=-27965, sub_s=0, td=3437, cfi=-1033522, lease=-109198, nci=-22492, intp=-180118, da=333248, rou=91905, ni=833971, divrec=550639, eqsh=447442),
}
def rows():
    out = {}
    for fy, d in D.items():
        s = d['ppe']+d['ppe_s']+d['eq']+d['eq_s']+d['oth']+d['oth_s']+d['ln']+d['ln_s']+d['sub']+d['sub_s']+d['td']
        net_ppe = -(d['ppe']+d['ppe_s']); net_biz = -(d['eq']+d['eq_s']+d['oth']+d['oth_s']+d['sub']+d['sub_s']); net_loan = -(d['ln']+d['ln_s'])
        oc_all = d['cfo'] - net_ppe - net_biz - net_loan + d['lease'] + d['nci']
        maint = d['da'] - d['rou']
        oc_maint = d['cfo'] - maint + d['lease'] + d['nci']
        oc_ex_biz = d['cfo'] - net_ppe - net_loan + d['lease'] + d['nci']   # purchases of businesses left out (organic pair)
        intx = -d['intp']*(1-T)
        out[fy] = dict(check=s-d['cfi'], cfo=d['cfo'], net_ppe=net_ppe, net_biz=net_biz, net_loan=net_loan, lease=-d['lease'], nci=-d['nci'],
                       oc_all=oc_all, oc_ex_biz=oc_ex_biz, maint=maint, oc_maint=oc_maint, int_at=intx,
                       oc_all_u=oc_all+intx, oc_ex_biz_u=oc_ex_biz+intx, oc_maint_u=oc_maint+intx, ni=d['ni'], divrec=d['divrec'], eqsh=d['eqsh'])
    return out
if __name__ == '__main__':
    R = rows()
    cols = ['check','cfo','net_ppe','net_biz','net_loan','lease','nci','oc_all','oc_ex_biz','maint','oc_maint','int_at','oc_all_u','oc_ex_biz_u','oc_maint_u','ni','divrec','eqsh']
    print('fy    ' + ' '.join(f'{c:>10}' for c in cols))
    for fy in sorted(R):
        print(f'{fy}  ' + ' '.join(f'{R[fy][c]/1000:>10.1f}' for c in cols))
    for span in ((2022, 2026), (2017, 2021), (2017, 2026), (2016, 2026)):
        ys = [y for y in R if span[0] <= y <= span[1]]
        print(f'avg {span}: ' + ' '.join(f'{c}={sum(R[y][c] for y in ys)/len(ys)/1000:.1f}' for c in ('oc_all','oc_all_u','oc_ex_biz_u','oc_maint','oc_maint_u','ni','divrec','eqsh','cfo')))
