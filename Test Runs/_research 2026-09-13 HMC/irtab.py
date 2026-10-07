import re, html, sys
sys.path.insert(0, '.')
import ir
for name in sys.argv[1:]:
    url = f'https://global.honda/en/investors/financial_data/{name}.html'
    d = ir.get(url); open(f'ir/{name}.html', 'wb').write(d)
    t = d.decode('utf-8', 'replace')
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    i = t.find('<main'); t = t[i:] if i >= 0 else t
    body = re.sub(r'(?is)<tr.*?</tr>', lambda m: '\n' + ' | '.join(re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', c))).strip() for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>', m.group(0))) + '\n', t)
    body = re.sub(r'(?i)</(p|div|h\d|li|caption)>', '\n', body)
    body = html.unescape(re.sub(r'<[^>]+>', ' ', body)).replace('△', '-')
    lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in body.split('\n')]
    out = '\n'.join(l for l in lines if l)
    out = out.split('CLOSE\nMENU')[0]
    open(f'ir/{name}.txt', 'w', encoding='utf-8').write(url + '\n' + out)
    print('=====', name); print(out[-6000:])
