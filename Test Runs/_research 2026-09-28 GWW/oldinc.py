import glob,re
for y in range(1993,2009):
    fs=[f for f in glob.glob(f'cache/k{y}_*.txt') if 'xex' not in f]
    fs.sort(key=lambda f: ('exhibit13' not in f, f))
    for f in fs:
        t=open(f,encoding='utf-8').read()
        t=re.sub(r'[\s|$.]*\n[\s|$.]*',' ',t); t=re.sub(r'[ |$]+',' ',t); t=re.sub(r'\.{2,}',' ',t)
        ns=re.findall(r'Net sales ((?:\d{1,3},\d{3},\d{3}|\d{1,3},\d{3}\.\d|\d{1,3},\d{3}) (?:\d{1,3},\d{3},\d{3}|\d{1,3},\d{3}\.\d|\d{1,3},\d{3}) (?:\d{1,3},\d{3},\d{3}|\d{1,3},\d{3}\.\d|\d{1,3},\d{3}))',t)
        oe=re.findall(r'Operating earnings ((?:[\d,]+(?:\.\d)?) (?:[\d,]+(?:\.\d)?) (?:[\d,]+(?:\.\d)?))',t)
        gp=re.findall(r'Gross profit ((?:[\d,]+(?:\.\d)?) (?:[\d,]+(?:\.\d)?) (?:[\d,]+(?:\.\d)?))',t)
        print(y,f[6:40],'NS',ns[:3],'OE',oe[:3],'GP',gp[:2])
