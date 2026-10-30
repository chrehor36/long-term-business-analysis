import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
for y in range(1993,2010):
    t=re.sub(r'\s+',' ',open(f'cache/k{y}.txt',encoding='utf-8',errors='ignore').read())
    m=re.findall(r'(?:ratio of gross profit to (?:net )?sales|gross profit ratio|Cost of products sold as a percentage)[^.]{0,200}\.\d?[^.]{0,120}',t)
    s=re.findall(r'(?:Net sales|Sales)[^.]{0,30}(?:were|was|of) \$[\d.,]+ (?:million|billion)[^.]{0,160}',t)
    print('==',y); [print('  GM:',x[:300]) for x in m[:4]]; [print('  S:',x[:220]) for x in s[:2]]
