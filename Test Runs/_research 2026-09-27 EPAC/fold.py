import io,json,re,os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
Q='Screens/WATCHLIST RUN QUEUE.md'; D='Screens/_daily/_wave7_done.txt'; RL='Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
SS='Screens/SURVIVAL SHAPES - index.md'; P='PORTFOLIO.md'; A='tools/alerts.json'
R='Test Runs/_research 2026-09-27 EPAC/'
def rd(p):
    b=io.open(p,'rb').read(); nl='\r\n' if b'\r\n' in b else '\n'; return b.decode('utf-8'),nl
def count(L):
    h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h)==1 and len(w)==1, (h,w)
    e=[l for l in L[h[0]+1:w[0]] if l.startswith('- **')]; return h[0],e
# 1. register, by line
t,nl=rd(Q); L=t.split(nl)
hi,e=count(L); before=len(e); assert not any(x.startswith('- **EPAC') for x in e)
entry=io.open(R+'register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:hi+1]+entry+L[hi+1:]
hi2,e2=count(L); assert len(e2)==before+1 and e2[0].startswith('- **EPAC') and e2[1].startswith('- **LOVE'), (len(e2),e2[0][:20])
assert sum(1 for x in e2 if x.startswith('- **EPAC'))==1 and hi2==hi
io.open(Q,'wb').write(nl.join(L).encode('utf-8'))
print('register: heading line',hi+1,'before',before,'after',len(e2),'first',e2[0][:10],'second',e2[1][:10])
# 2. done file
t,nl=rd(D); lines=[x for x in t.split(nl) if x!='']
assert lines[-1]=='LOVE' and 'EPAC' not in lines and len(lines)==77, (lines[-1],len(lines))
io.open(D,'wb').write(((t if t.endswith(nl) else t+nl)+'EPAC'+nl).encode('utf-8'))
t2,_=rd(D); l2=[x for x in t2.split(nl) if x!='']; print('done file lines',len(l2),'last',l2[-1])
# 3. reading list
t,nl=rd(RL); assert '## UPDATE 2026-09-27 - EPAC' not in t
note=io.open(R+'fold_note.md',encoding='utf-8').read().rstrip('\n')
io.open(RL,'wb').write(((t if t.endswith(nl) else t+nl)+nl.join(note.split('\n'))+nl).encode('utf-8'))
print('reading list appended')
# 4a. alerts
raw=io.open(A,'rb').read(); a=json.loads(raw.decode('utf-8'))
assert not any(x['id'].startswith('EPAC') for x in a['alerts'])
a['alerts'].append({"id":"EPAC-floor-band","ticker":"EPAC","currency":"USD","op":"<=","threshold":11.63,"active":True,
 "label":"EPAC at/below $11.63: the E4-28 floor is met at g = 1.1% (core sales compounded FY2019-FY2025) on the five-year capex-end owner earnings of $53.0M (continuing operations) and 51,137,646 cover shares. Q1-Q4 all IN on 2026-09-27 (Q2 NARROW); Q5 quit on at $35.70 (yield 2.90-2.94% five-year and 5.44-5.48% TTM against a 5.49% sovereign; expectancy 4.0-8.6%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (capital-allocation flag live: buybacks at about $39-40 against the run's values; the registrant's own Actuant acquisition record; the SFE Group purchase at 10.6x adjusted EBITDA) and for staying power until the secured facility maturing September 2027 is extended. VOID if any Q2 falsifier has fired: consolidated gross margin below 46% two consecutive fiscal years without a quantified one-time cause; the filer reporting price given back or competitive pricing as a cause of a margin decline two consecutive years; IT&S product organic sales negative two consecutive years; a write-down of SFE Group or any purchased business of $50M or more, or a purchase exited at a loss; pre-tax return on all operating capital, goodwill and intangibles included, below 15% two consecutive years. Re-derive on the post-purchase perimeter once SFE Group's audited statements are filed. Source: Test Runs/2026-09-27 Run - EPAC Enerpac Tool Group.md."})
a['alerts'].append({"id":"EPAC-rerun-band","ticker":"EPAC","currency":"USD","op":"<=","threshold":28.57,"active":True,
 "label":"EPAC at/below $28.57: the E4-28 floor is met only if 3.1%/yr (the Industrial segment's sales growth FY2007-FY2017, purchases included) is granted in perpetuity on the TTM depreciation-end owner earnings ($100.1M to 2026-05-31, the best twelve months filed, after a margin restoration). Prompt for a FULL v4.1 re-run in which that rate is re-tested against the then-current organic series before it is spent. Re-derive both EPAC bands on the FY2026 10-K (about mid-October 2026) and on the post-SFE perimeter; VOID if any falsifier in EPAC-floor-band has fired; Q4 re-opens if the September 2027 facility is not refinanced by the 10-Q for the quarter to 2027-02-28."})
io.open(A,'wb').write((json.dumps(a,indent=1,ensure_ascii=False)+'\n').encode('utf-8'))
print('alerts',len(a['alerts']))
# 4b. PORTFOLIO row after NDSN row
t,nl=rd(P); L=t.split(nl)
ix=[i for i,l in enumerate(L) if l.startswith('| - | NDSN |')]; assert len(ix)==1 and not any('| EPAC |' in l for l in L)
row=("| - | EPAC | 2.90–2.94 % (5-yr, 2026-09-27; 2.08–4.83 % across every window of 1-9 years on continuing operations; 5.44–5.48 % TTM) | 5.49 % USD | "
 "**below the sovereign on every window and both (c) ends, −2.59 to −2.55 points (5-yr); the TTM within 0.05 points** | "
 "**RUN DONE** (`Test Runs/2026-09-27 Run - EPAC Enerpac Tool Group.md`, wave 7 name 78): **Q1–Q4 all IN; Q2 NARROW, widening since FY2022 back to the core's long-run level** "
 "(the Industrial segment, the Enerpac hydraulic-tools business reported alone, earned 22-31 % on sales and 26.5-52.7 % pre-tax on segment assets including goodwill FY2007-FY2017, 23.5 % in the FY2009 recession; gross margin 42.2 % to 50.5 % FY2017-FY2025 on pricing that outran inflation; but the company earned 4.9-9.7 % on sales FY2018-FY2022, a fifth of sales is labour, and the filer calls its markets highly competitive); "
 "**Q3 IN at binary-gate weight** (no disqualifier; the self-reported Crimea sanctions matter recorded; [E4-29] fires and converges; FY2026 guidance cut below its opening range; capital-allocation flag, buybacks at about $39-40); "
 "**Q4 IN, GOOD, narrowly on staying power** (owner earnings $53.0M–$53.7M five-year, $99.4M–$100.1M TTM; the signed SFE Group purchase, about $472M at 10.6x adjusted EBITDA, is to be funded on a secured facility maturing September 2027; named death #10 THE CAMOUFLAGE, the registrant's own Actuant history, with #6 as a feature). "
 "**Q5 quit on at $35.70**: expectancy 4.0–8.6 % against ~10 %; value about $12–$29. **NOT RANKED: watch-list only; no position held and none proposed.** "
 "Bands `EPAC-floor-band` $11.63 and `EPAC-rerun-band` $28.57; each a prompt for a full re-run, never a buy, VOID if a Q2 falsifier fires. |")
L=L[:ix[0]+1]+[row]+L[ix[0]+1:]
io.open(P,'wb').write(nl.join(L).encode('utf-8')); print('portfolio row inserted after line',ix[0]+1)
# 5. survival shapes: #10 instances + dated note
t,nl=rd(SS); L=t.split(nl)
rows=[l for l in L if re.match(r'^\| \d+ \|',l)]; nums=[int(re.match(r'^\| (\d+) \|',l).group(1)) for l in rows]
print('shape rows',len(rows),'max',max(nums))
i10=[i for i,l in enumerate(L) if l.startswith('| 10 |')]; assert len(i10)==1 and 'EPAC' not in L[i10[0]]
assert L[i10[0]].rstrip().endswith('|')
inst=(", EPAC (2026-09-27, the mechanism, Q4 reached: the Enerpac hydraulic-tools segment earned 26-53% pre-tax on its assets FY2007-FY2017 while "
 "Actuant bought about $1,015M of other businesses FY2009-FY2016, wrote off $354.4M FY2015-FY2019 and sold EC&S at a $257.2M loss; the present management sold the rest and "
 "has signed to buy SFE Group for about $472M at 10.6x adjusted EBITDA, taking the owners' pre-tax return on all capital from about 30% to at most about 19%; "
 "#6 THE BORROWED BALANCE SHEET as a feature: the secured facility that funds it matures September 2027; a real possibility, the solvency form a low-level possibility)")
s=L[i10[0]].rstrip(); L[i10[0]]=s[:-1].rstrip()+inst+' |'
while L and L[-1]=='': L.pop()
L.append('')
L.append("*Dated note, 2026-09-27 (the EPAC fold, wave 7 name 78): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** The table was counted with a line-start regex immediately before writing: **%d rows, maximum number %d**. Enerpac Tool Group cleared Q1-Q4 (Q2 NARROW), so **Q4 was opened and the run names a death**: **#10 THE CAMOUFLAGE as the mechanism, with #6 THE BORROWED BALANCE SHEET (a secured facility maturing September 2027 that is to fund the SFE Group purchase) and [E2-56] as features**, likelihood *a real possibility*, the solvency form *a low-level possibility*. **EPAC is therefore entered in #10's instances column**, as NDSN was the same day. The registrant is its own worked case: the camouflage ran under the name Actuant from FY2009 to FY2019 and was undone by the sales of 2019-2023.*"%(len(rows),max(nums)))
L.append('')
io.open(SS,'wb').write(nl.join(L).encode('utf-8')); print('survival shapes updated')
