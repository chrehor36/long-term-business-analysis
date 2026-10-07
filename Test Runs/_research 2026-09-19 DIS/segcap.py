# Where Disney's capital sits, against where its profit sits. FY2025 10-K, accession 0001744489-25-000155.
# Segment ASSETS are not disclosed: "We do not present a measure of total assets for our reportable
# segments as this information is not used by the CODM" (Note 17). So capital is assembled from the
# items the filing DOES attribute, and every allocation below is labelled.
GW   = {'Entertainment':51258, 'Sports':16486, 'Experiences':5550}          # Note 4, filed by segment
OI   = {'Entertainment':4674,  'Sports':2882,  'Experiences':9995}          # Note 17, filed by segment
DEP  = {'Entertainment':773,   'Sports':48,    'Experiences':2715, 'Corporate':323}  # MD&A, filed
CAPX = {'Entertainment':1155,  'Sports':3,     'Experiences':6429, 'Corporate':437}  # MD&A, filed
CONTENT = 31327   # produced and licensed content costs, balance sheet; Entertainment + Sports only
PPE_NET = 41255   # parks, resorts and other property, net
INTANG  = 9272    # intangible assets net; 7,480 amortisable of which TFCF/Hulu-derived
COMMIT_SPORTS = 84076   # Note 14 contractual sports programming rights
COMMIT_OTHERPROG = 7691
COMMIT_OTHER = 12321

# PP&E split: depreciation share is the only filed key. Experiences 2,715 / 3,859 = 70.4%.
# Attraction assets are longer-lived than broadcast/tech plant, so the PP&E share is HIGHER than the
# depreciation share; the depreciation-share split is therefore CONSERVATIVE against Experiences
# (it gives Experiences too little capital and so overstates its return). Stated, not hidden.
ppe = {k: PPE_NET*DEP[k]/sum(DEP.values()) for k in DEP}
print('net PP&E allocated by depreciation share (COMPUTED, not filed):')
for k,v in ppe.items(): print(f'   {k:14} {v:8,.0f}')
print()
print('Capital carried, and the return on it -- ALL ALLOCATIONS LABELLED COMPUTED')
print(f'{"":14} {"goodwill":>9} {"content":>9} {"netPP&E":>9} {"capital":>9} {"seg OI":>8} {"return":>7}')
ENT_SPORTS_CONTENT = {'Entertainment': CONTENT*0.70, 'Sports': CONTENT*0.30, 'Experiences': 0.0}
tot_cap = tot_oi = 0
for k in ['Entertainment','Sports','Experiences']:
    cap = GW[k] + ENT_SPORTS_CONTENT[k] + ppe[k]
    print(f'{k:14} {GW[k]:9,} {ENT_SPORTS_CONTENT[k]:9,.0f} {ppe[k]:9,.0f} {cap:9,.0f} {OI[k]:8,} {OI[k]/cap*100:6.1f}%')
    tot_cap += cap; tot_oi += OI[k]
print(f'{"TOTAL":14} {sum(GW.values()):9,} {CONTENT:9,} {PPE_NET-ppe["Corporate"]:9,.0f} {tot_cap:9,.0f} {tot_oi:8,} {tot_oi/tot_cap*100:6.1f}%')
print()
ent_sp_cap = GW['Entertainment']+GW['Sports']+CONTENT+ppe['Entertainment']+ppe['Sports']
ent_sp_oi  = OI['Entertainment']+OI['Sports']
print(f'Entertainment + Sports together: capital {ent_sp_cap:,.0f}  OI {ent_sp_oi:,}  = {ent_sp_oi/ent_sp_cap*100:.1f}%')
exp_cap = GW['Experiences']+ppe['Experiences']
print(f'Experiences alone:               capital {exp_cap:,.0f}  OI {OI["Experiences"]:,}  = {OI["Experiences"]/exp_cap*100:.1f}%')
print()
print('Shares of the whole:')
print(f'  Experiences share of segment OI      {OI["Experiences"]/tot_oi*100:.1f}%')
print(f'  Experiences share of that capital    {exp_cap/tot_cap*100:.1f}%')
print(f'  Ent+Sports share of segment OI       {ent_sp_oi/tot_oi*100:.1f}%')
print(f'  Ent+Sports share of that capital     {ent_sp_cap/tot_cap*100:.1f}%')
print(f'  Experiences share of FY2025 capex    {CAPX["Experiences"]/sum(CAPX.values())*100:.1f}%')
print()
print(f'Signed forward commitments (Note 14): sports rights {COMMIT_SPORTS:,}, other programming '
      f'{COMMIT_OTHERPROG:,}, other {COMMIT_OTHER:,}; total {COMMIT_SPORTS+COMMIT_OTHERPROG+COMMIT_OTHER:,}')
print(f'  sports-rights commitments as a multiple of Sports segment OI: {COMMIT_SPORTS/OI["Sports"]:.1f}x')
print(f'  sports-rights commitments as a multiple of ALL segment OI:    {COMMIT_SPORTS/tot_oi:.1f}x')
print(f'  total commitments vs market cap $177,279M:                    '
      f'{(COMMIT_SPORTS+COMMIT_OTHERPROG+COMMIT_OTHER)/177279*100:.0f}% of the cap')
