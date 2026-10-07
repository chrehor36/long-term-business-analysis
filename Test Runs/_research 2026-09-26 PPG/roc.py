# PPG returns on capital, every input typed from the filed statements of the 10-K named ($M).
# capital = short-term debt + long-term debt + total equity (incl NCI) - cash - short-term investments
# EBIT = income before income taxes (continuing, as filed that year) + interest expense - interest income
# one-offs named in the income statement are shown separately, not removed from the headline
D={ # year: (source, pretax, intexp, intinc, stdebt, ltdebt, equity, cash, sti, gw, intang, oneoffs, note)
2014:('FY2014',1416,187,50,481,3544,5265,686,497,3801,2411,317,'debt refinancing charge'),
2016:('FY2016',827,125,26,629,3787,4913,1820,43,3572,1983,968,'pension settlement charges'),
2019:('FY2019',1661,132,32,513,4539,5403,1216,57,4470,2131,176,'business restructuring'),
2022:('FY2022',1381,167,54,313,6503,6709,1099,55,6078,2414,245+33,'impairment and restructuring'),
2025:('FY2025',2045,241,153,706,6602,8097,2163,56,6149,1971,6+24,'restructuring and impairment'),
}
print('| year-end | 10-K | EBIT as filed | named one-offs in it | capital incl. goodwill | EBIT on it | same, one-offs added back | goodwill + intangibles | on net tangible capital (one-offs added back) |')
print('|---|---|---|---|---|---|---|---|---|')
for y,(s,pt,ie,ii,sd,ld,eq,c,st,gw,it,oo,n) in D.items():
    ebit=pt+ie-ii; cap=sd+ld+eq-c-st; tang=cap-gw-it
    print(f'| {y} | {s} | ${ebit:,}M | ${oo:,}M ({n}) | ${cap:,}M | **{ebit/cap*100:.1f}%** | {(ebit+oo)/cap*100:.1f}% | ${gw+it:,}M | {(ebit+oo)/tang*100:.0f}% |')
