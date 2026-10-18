import sys, base64, re, os, subprocess
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
x = open(src, encoding='utf-8', errors='replace').read()
# find each PDF blob with nearest preceding NomeArquivoPdf / NomeCampo
for i, m in enumerate(re.finditer(r'<ImagemObjetoArquivoPdf>([^<]+)</ImagemObjetoArquivoPdf>', x)):
    pre = x[max(0, m.start()-3000):m.start()]
    names = re.findall(r'<(?:NomeArquivoPdf|NomeCampo)>([^<]*)<', pre)
    tag = re.findall(r'<(\w+)>\s*$', pre[-400:])
    nm = (names[-1] if names else 'x')
    fn = os.path.join(out, f'{i:02d}_' + re.sub(r'[^\w.-]+', '_', nm)[:60])
    if not fn.endswith('.pdf'): fn += '.pdf'
    open(fn, 'wb').write(base64.b64decode(m.group(1)))
    print(fn)
