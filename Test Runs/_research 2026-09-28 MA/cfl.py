import re,glob
labels=['Net cash provided by operating activities','Net cash provided by (used in) operating activities','Share-based payments','Share-based compensation','Share based payments','Depreciation and amortization','Amortization of customer incentives','Purchases of property and equipment','Purchases of property, plant and equipment','Capitalized software','Acquisition of businesses, net of cash acquired','Purchases of treasury stock','Net revenue','Total operating expenses','Operating income','Litigation provisions','Provision for litigation','Provision for litigation settlement','Rebates and incentives','Prepaid expenses','Accrued litigation and legal settlements','Gross revenue','Net income']
for y in range(2002,2026):
    try: t=open(f'cache/k{y}.txt',encoding='utf-8').read().split('\n')
    except: continue
    print('=====',y)
    seen=set()
    for l in t:
        for lab in labels:
            if l.startswith(lab+' |') and (lab not in seen):
                seen.add(lab); print('  ',l[:160])
