import urllib.request, json, os, sys, time
UA = {'User-Agent':'chrehor36@gmail.com research'}
D = os.path.dirname(os.path.abspath(__file__))
def get(url, path, binary=False):
    p = os.path.join(D, path)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        print('have', path); return
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            b = urllib.request.urlopen(req, timeout=120).read()
            break
        except Exception as e:
            print('retry', i, e); time.sleep(3)
    else:
        print('FAILED', url); return
    open(p, 'wb').write(b)
    print('wrote', path, len(b))
get('https://data.sec.gov/submissions/CIK0000051143.json','submissions.json')
get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000051143.json','companyfacts.json')
