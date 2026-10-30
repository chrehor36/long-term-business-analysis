p='body_q2.md'
s=open(p,encoding='utf-8').read()
R=[
('carried as a business combination with a royalty-type contingent consideration that cost $2,865M in operating cash in 2025 alone)',
 'carried with a contingent consideration whose change the filer ties to *"higher estimated Skyrizi sales, the passage of time, lower discount rates and a longer estimated royalty period"*: payments $2,865M in 2025, a liability of $25,374M at 2025 year-end, *"Projected year of payments | 2026 - 2037"*, Note 11)'),
('Stemcentrx and other $2,495M,','$2,495M in 2016, the year of Stemcentrx and the risankizumab rights,'),
('and *"Other acquisitions and investments"* (licences and bought pipeline) $17,182M','and *"Other acquisitions and investments"* (licences, bought pipeline and investments) $17,182M'),
('**About $135bn of purchased products and pipeline in thirteen years and nine months against 2025 net revenues of $61bn.**','**About $136bn of purchased products and pipeline in thirteen years and nine months (cash, shares and Apogee\'s equity value), against 2025 net revenues of $61bn.**'),
('**AbbVie sits in the lower middle of the row** in 2024-2025, behind Novo Nordisk, Lilly, Johnson & Johnson, Novartis, Merck, Gilead, GSK and Bristol-Myers in 2025;',
 '**AbbVie sits ninth of thirteen in 2024 and tenth in 2025**, behind Novo Nordisk, Lilly, Johnson & Johnson, Novartis, Merck, Gilead, GSK, Bristol-Myers and AstraZeneca in 2025;'),
('**9.7-15.8% in 2023-2025 including what was paid for the products**, lower middle of the row.','**9.7-15.8% in 2023-2025 including what was paid for the products**, ninth and tenth of thirteen in 2024-2025.'),
('(Skyrizi\'s molecule from Boehringer Ingelheim in 2016,','(Skyrizi\'s molecule from Boehringer Ingelheim in 2016,'),
('**45,804 (2020, Allergan from May)**','**45,804 (2020, Allergan from 8 May: *"On May 8, 2020, AbbVie completed the acquisition of Allergan plc (Allergan)."*)**'),
('The MRK precedent a day old pulls toward OUT by consistency and by habit (sixteen of the last seventeen wave 7 runs before EPAC closed at Q2);',
 'The MRK precedent a day old pulls toward OUT by consistency, and so does habit (the MRK file counted fifteen of the sixteen wave 7 runs from LNN to MDT closing at Q2);'),
('and Rinvoq\'s generics are held to April 2037 by settlement, four years past its 2033 compound patent.','and Rinvoq\'s generics are held to April 2037 by settlement, about four years past its 2033 compound patent.'),
('(Imbruvica $2,869M, Vraylar $3,621M, Linzess $907M, Botox Therapeutic $3,769M).','(Imbruvica $2,869M, Vraylar $3,621M, Linzess $907M, Botox Therapeutic $3,769M; Botox Cosmetic, $2,602M, is cash-pay and not counted).'),
]
for a,b in R:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
