import sys,json; sys.path.insert(0,'.')
from fetch import get
def facts(cik,t):
    return json.loads(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',f'{t}_companyfacts.json'))
def annual(f,tag,unit='USD',ns='us-gaap'):
    try: u=f['facts'][ns][tag]['units'][unit]
    except KeyError: return {}
    out={}
    for x in u:
        if x.get('fp')=='FY' and x['form'] in('10-K','10-K/A') and 'start' in x:
            from datetime import date
            s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
            if 350<(e-s).days<380:
                out.setdefault(x['end'][:4],(x['val'],x['accn'],x['filed']))
                # keep first-filed
                if x['filed']<out[x['end'][:4]][2]: out[x['end'][:4]]=(x['val'],x['accn'],x['filed'])
    return out
def inst(f,tag,unit='USD',ns='us-gaap'):
    try: u=f['facts'][ns][tag]['units'][unit]
    except KeyError: return {}
    out={}
    for x in u:
        if x['form'] in('10-K',) and 'start' not in x and x['end'][5:]=='12-31':
            k=x['end'][:4]
            if k not in out or x['filed']<out[k][2]: out[k]=(x['val'],x['accn'],x['filed'])
    return out
