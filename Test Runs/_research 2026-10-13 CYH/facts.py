"""Annual (FY, 10-K) values from SEC companyfacts, latest-filed value per fiscal year end. Transcription only."""
import json, sys

CIKS = {'CYH': '0001108109', 'HCA': '0000860730', 'THC': '0000070318', 'UHS': '0000352915'}


def annual(facts, tag, unit='USD'):
    try:
        units = facts['facts']['us-gaap'][tag]['units'][unit]
    except KeyError:
        return {}
    out = {}
    for u in units:
        if u.get('form') not in ('10-K', '10-K/A'):
            continue
        if 'start' in u:
            # keep only ~12-month durations
            from datetime import date
            s = date.fromisoformat(u['start']); e = date.fromisoformat(u['end'])
            if not (350 <= (e - s).days <= 380):
                continue
        y = u['end'][:4]
        # latest filed wins
        if y not in out or u['filed'] > out[y][1]:
            out[y] = (u['val'], u['filed'], u['accn'])
    return out


def load(t):
    return json.load(open(f'cache/facts_{CIKS[t]}.json'))


if __name__ == '__main__':
    t = sys.argv[1]
    tags = sys.argv[2:]
    f = load(t)
    years = [str(y) for y in range(2014, 2026)]
    print(t, ' '.join(f'{y:>8}' for y in years))
    for tag in tags:
        a = annual(f, tag)
        print(tag[:40].ljust(40), ' '.join(f"{a[y][0]/1e6:8.0f}" if y in a else '       -' for y in years))
