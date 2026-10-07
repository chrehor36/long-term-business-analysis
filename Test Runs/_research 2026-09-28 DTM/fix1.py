p='body_step0_q1.md'
s=open(p,encoding='utf-8').read()
old="""gathering business (Blue Union and LEAP, bought by DTE from Momentum Midstream in December 2019 for the $2,296M
on the 2019 acquisition line; financed *"by DTE Energy"*)"""
new="""gathering business (Blue Union and LEAP, bought 2019-12-04 from Momentum Midstream and Indigo Natural Resources
for a fair value of *"$ 2.74 billion"*, *"$ 2.36 billion paid in cash and an estimated $ 380 million of contingent
consideration"*, $2,296M on the tagged 2019 acquisition line; FY2021 10-K Note 4: *"The acquisition was financed
by DTE Energy."*)"""
assert old in s
s=s.replace(old,new)
open(p,'w',encoding='utf-8').write(s)
