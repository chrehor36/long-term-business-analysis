"""Print annual (FY, 10-K) values for given us-gaap tags from a companyfacts file. Arithmetic transcription only."""
import json, sys
def annual(path, tags, start=2012):
    d = json.load(open(path))
    g = d['facts'].get('us-gaap', {})
    g.update({k: v for k, v in d['facts'].get(path.split('_')[-1].split('.')[0].lower(), {}).items()})
    out = {}
    for t in tags:
        if t not in g: print(t, 'MISSING'); continue
        units = g[t]['units']
        u = 'USD' if 'USD' in units else list(units)[0]
        vals = {}
        for x in units[u]:
            if x.get('form', '').startswith('10-K') and x.get('fp') == 'FY':
                if 'start' in x:
                    from datetime import date
                    s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                    if (e - s).days < 300: continue
                y = int(x['end'][:4])
                if y >= start:
                    vals[y] = x['val']  # later filings overwrite earlier (restated)
        out[t] = vals
        print(f"{t:70s}", ' '.join(f"{y}:{v/1e6:,.0f}" for y, v in sorted(vals.items())))
    return out
if __name__ == '__main__':
    annual(sys.argv[1], sys.argv[2:])
