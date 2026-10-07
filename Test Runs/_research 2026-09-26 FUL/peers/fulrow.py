"""Row for FUL and SEC peers, row.py construction; FUL revenue from the filed income statements (is_parsed.json)
because companyfacts carries no FUL revenue fact after 2019. Adds return on total operating capital incl. goodwill+intangibles."""
import json,row,sys
isp=json.load(open('../is_parsed.json'))
def run(t,y0=2009,y1=2025):
    f=row.load(t)
    s={k:row.fy(row.series(f,v,flow=k in('rev','pti','intx','ni'))) for k,v in row.T.items()}
    if t=='FUL':
        for y,r in isp.items(): s['rev'][int(y)]=r['rev']*1e6
    out=[]
    for y in range(y0,y1+1):
        g=lambda k:s[k].get(y); z=lambda k:g(k) or 0
        if g('rev') is None or g('pti') is None or g('A') is None: out.append((y,None)); continue
        ebit=g('pti')+abs(g('intx') or 0)
        n=z('A')-z('C')-z('G')-z('I')-z('R')-(z('L')-z('CD')-z('SD')-z('CL'))
        e0,e1=s['E'].get(y-1),s['E'].get(y)
        roe=g('ni')/((e0+e1)/2) if e0 and e1 and g('ni') is not None else None
        out.append((y,dict(rev=g('rev'),ebit=ebit,m=ebit/g('rev'),ntoa=n,ret=ebit/n if n>0 else None,tot=ebit/(n+z('G')+z('I')),gi=(z('G')+z('I'))/z('A'),roe=roe)))
    return out
pc=lambda v:'   n/a' if v is None else '%6.1f%%'%(v*100)
if __name__=='__main__':
    for t in sys.argv[1:]:
        print('==',t)
        for y,r in run(t):
            if r is None: print(y,'incomplete'); continue
            print(y,'rev %7.0f ebit %6.0f margin %s NTOA %6.0f retNTOA %s ret_incl_GW %s GW+I/assets %s ROE %s'%(r['rev']/1e6,r['ebit']/1e6,pc(r['m']),r['ntoa']/1e6,pc(r['ret']),pc(r['tot']),pc(r['gi']),pc(r['roe'])))
