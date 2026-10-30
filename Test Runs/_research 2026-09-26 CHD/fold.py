import re,json,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ROOT='../../'
# 1. register entry by line
qf=ROOT+'Screens/WATCHLIST RUN QUEUE.md'
L=open(qf,encoding='utf-8').read().split('\n')
h=[i for i,x in enumerate(L) if x=='## COMPLETED FROM THE QUEUE']; assert len(h)==1,h
w=[i for i,x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(w)==1,w
def count(L):
    h=[i for i,x in enumerate(L) if x=='## COMPLETED FROM THE QUEUE'][0]; w=[i for i,x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')][0]
    sl=L[h+1:w]; return [x for x in sl if x.startswith('- **')]
before=count(L); assert not any(x.startswith('- **CHD ') for x in before)
entry=open('_reg_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h[0]+1]+entry+L[h[0]+1:]
after=count(L); assert after[0].startswith('- **CHD ') and after[1].startswith('- **FUL ')
print('register before',len(before),'after',len(after))
open(qf,'w',encoding='utf-8',newline='\n').write('\n'.join(L))
# 2. done file
df=ROOT+'Screens/_daily/_wave7_done.txt'
d=open(df,encoding='utf-8').read()
if not d.endswith('\n'): d+='\n'
assert 'CHD' not in d.split()
d+='CHD\n'; open(df,'w',encoding='utf-8',newline='\n').write(d)
print('done lines',len([x for x in d.split('\n') if x.strip()]))
# 3. reading list
rf=ROOT+'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
r=open(rf,encoding='utf-8').read()
if not r.endswith('\n'): r+='\n'
r+=open('_reading_fold.md',encoding='utf-8').read()
open(rf,'w',encoding='utf-8',newline='\n').write(r)
# 4a. alerts
af=ROOT+'tools/alerts.json'
A=json.load(open(af,encoding='utf-8'))
assert not any(a['ticker']=='CHD' for a in A['alerts'])
A['alerts']+= [
 {"id":"CHD-floor-band","ticker":"CHD","currency":"USD","op":"<=","threshold":60.34,"active":True,
  "label":"CHD at/below $60.34: the E4-28 floor is met at g = 4.0% (the filed organic sales rate 2016-2025, volume +23.4% and price/mix +20.0%, and the growth of five-year owner earnings 2016-20 to 2021-25) on the five-year capex-end owner earnings of $858.8M and 237,203,907 cover shares. Q1-Q4 all IN on 2026-09-26 (Q2 NARROW); Q5 quit on at $96.38 (yield 3.76-4.14% against a 5.49% sovereign, expectancy 7.8-9.1%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (growth-target flag, acquisition habit and E5-08(2) capital-allocation flag live). VOID if any Q2 falsifier has fired: two consecutive years of negative consolidated product volumes; price/mix negative two years running with promotion named as the cause; pre-tax return on operating capital including goodwill and intangibles, ex-items, below 14% two years running; a further purchased trade-name impairment of $100M or more or a third purchase exited at a loss; Walmart above 25% of net sales or the top four above 50%. Source: Test Runs/2026-09-26 Run - CHD Church & Dwight.md."},
 {"id":"CHD-rerun-band","ticker":"CHD","currency":"USD","op":"<=","threshold":80.67,"active":True,
  "label":"CHD at/below $80.67: the E4-28 floor is met only if the full 4.7%/yr per-share rate (4.0% organic plus about 0.78%/yr share-count decline) is granted in perpetuity on the three-year depreciation-end owner earnings ($1,014.2M). Prompt for a FULL v4.1 re-run in which that rate is re-tested against the then-current volume and price/mix series before it is spent. Re-derive both CHD bands on the 2026 10-K (about February 2027)."}]
open(af,'w',encoding='utf-8',newline='\n').write(json.dumps(A,indent=1,ensure_ascii=True)+'\n')
print('alerts',len(A['alerts']))
# 4b. PORTFOLIO row after the PG row
pf=ROOT+'PORTFOLIO.md'
P=open(pf,encoding='utf-8').read().split('\n')
ix=[i for i,x in enumerate(P) if x.startswith('| — | PG |')]; assert len(ix)==1
row="| — | CHD | 3.76–4.14 % (5-yr, 2026-09-26; 2.35–4.44 % across every window) | 5.49 % USD | **below the sovereign on every window and both (c) ends, −1.73 to −1.35 points (5-yr)** | **RUN DONE** (`Test Runs/2026-09-26 Run - CHD Church & Dwight.md`, wave 7 name 59): **Q1–Q4 all IN; Q2 NARROW** (2016-2025 price/mix +20.0 % with product volumes +23.4 %; pre-tax return on NTOA 59.8-121.0 % every year 2009-2025, top of the household row with Colgate; but the value tier, 34 % of consumer revenue, is not a franchise, the filer meets cost increases *\"primarily by implementing cost reduction programs\"*, and 89 % of operating capital is purchased goodwill and intangibles earning 14.8-17.5 % pre-tax, falling; two failed purchases, VitaFusion and Flawless, recorded as a moat defect), **Q3 overlay** (growth-target flag with fiscal 2025 missed on every line of the original outlook; Adjusted EPS excludes the failed purchases; [E2-30](2); [E5-08](2) flag on $900M of 2025 buybacks at $83.59-95.71), **Q4 GOOD**, named death #19 the shelf (feature #24). Q5: expectancy **7.8–9.1 %** with the filed 4.0–4.7 % growth, **below the [E4-28] floor**; value about **$60–$81** against **$96.38**. **NOT RANKED: watch-list only; no position held and none proposed.** Bands armed **$60.34** (floor at g = 4.0 %) and **$80.67** (floor only with the full per-share rate granted), each a prompt for a full re-run, VOID if a Q2 falsifier fires (two negative volume years; the 2010-2017 promotion regime back; return including goodwill ex-items under 14 % two years running; a further trade-name impairment of $100M or more or a third purchase exited at a loss; Walmart above 25 % or the top four above 50 %) |"
P=P[:ix[0]+1]+[row]+P[ix[0]+1:]
open(pf,'w',encoding='utf-8',newline='\n').write('\n'.join(P))
print('portfolio row inserted after line',ix[0]+1)
