import re
def T(f): return re.sub(r'\s+',' ',open('cache/'+f+'.txt',encoding='utf-8').read())
S1="The competitive factors used during bid evaluation by our customers vary from project to project and may include technical support and application expertise, engineering and manufacturing capabilities, equipment rating, delivered value, scheduling and price"
S2="may, therefore, be able to provide their products or services at lower prices"
S3="Ultimately, our competitive position is dependent upon our ability to provide quality custom"
for y in range(2002,2026):
    try: t=T(f'k{y}')
    except: continue
    gm = 'GE' if re.search(r'principal competitors include[^.]*\bGE\b|General Electric Company, Schneider', t) else '-'
    print(y, S1 in t, S2 in t, S3 in t, gm, bool(re.search(r'480 volts',t)), bool(re.search('competitively bid',t)))
t=T('k2025')
for q in ['Revenues | 1,104,315','Operating income | 217,864','Typically, our contracts may have an early termination for convenience clause at the discretion of our customers; however, most of these contracts typically provide for the reimbursement of our costs incurred']:
    print(q[:40], q in t)
