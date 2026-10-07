import re,io,sys,glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
for fn in ['jnj_2010_y86310kexv13.htm.txt','jnj_2013_ex13-form10xk20131229.htm.txt','jnj_2016_form10-k20170101.htm.txt','jnj_10k_2019.txt','jnj_2021_jnj-20220102.htm.txt']:
    s=re.sub(r'\s+',' ',open(fn,encoding='utf-8').read()); s=re.sub(r'(\| )+','| ',s)
    print('=====',fn)
    m=re.search(r'Income Before Tax \| Segment Sales \| Percent of Segment Sales',s) or re.search(r'Income Before Tax by Segment',s)
    if m: print(s[m.start():m.start()+700])
    for m in list(re.finditer(r'Consumer segment sales in [0-9]{4} were',s))[:1]:
        print('--',s[m.start():m.start()+500])
    for m in list(re.finditer(r'Consumer segment income before tax as a percent',s))[:1]:
        print('--',s[m.start():m.start()+900])
