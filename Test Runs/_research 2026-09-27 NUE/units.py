"""Physical series [E4-55]: average sales price per ton, tons shipped to outside customers, steel-mill utilization, as the filer states them in each year's MD&A. Transcription only."""
import re,sys,io,glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
files=sorted(glob.glob('ex13_20*.txt'))+['tenk_%d.txt'%y for y in range(2019,2026)]
for f in files:
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8',errors='replace').read().replace('|',' '))
    p=re.findall(r'[Aa]verage sales price per ton (?:increased|decreased|was)[^.$]{0,40}(?:from )?\$([\d,]+) in (\d{4}) to \$([\d,]+) in (\d{4})',t)
    s=re.findall(r'[Tt]otal (?:tons shipped|shipments) to (?:outside|external) customers (?:increased|decreased)[^.]{0,20}from ([\d,.]+)(?: million)? tons in (\d{4}) to ([\d,.]+)',t)
    u=re.findall(r'(?:[Oo]perating rates?|utilization rates?)[^.]{0,80}steel mills[^.]{0,160}\.',t)
    print(f, p[:1], s[:1]); 
    for x in u[:2]: print('   U:',x[:260])
