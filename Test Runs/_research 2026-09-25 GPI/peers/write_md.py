from build_row import P, table, summary
ACC={
 'AN':'FY2025 0001628280-26-007800; FY2023 0000350698-24-000021',
 'PAG':'FY2025 0001628280-26-012830; FY2023 0001019849-24-000033',
 'LAD':'FY2025 0001023128-26-000015; FY2023 0001023128-24-000032',
 'ABG':'FY2025 0001144980-26-000051; FY2023 0001144980-24-000076',
 'SAH':'FY2025 0001628280-26-010570; FY2023 0001043509-24-000022'}
H=open('md_head.md',encoding='utf-8').read()
S=open('md_sections.md',encoding='utf-8').read()
T=open('md_tail.md',encoding='utf-8').read()
for t in P:
    S=S.replace('{{TABLE_%s}}'%t, table(t))
T=T.replace('{{SUMMARY}}', summary(ACC))
md=H+S+T
assert '—' not in md and '–' not in md, 'dash found'
open('COMPETITOR_ROW.md','w',encoding='utf-8').write(md)
print('written', len(md))
