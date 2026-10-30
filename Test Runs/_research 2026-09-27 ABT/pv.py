# Price / volume / exchange decomposition as filed in each 10-K MD&A ("Components of % Change").
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
LABELS=['Total Net Sales','Total U.S.','Total International','Established Pharmaceutical Products Segment','Nutritional Products Segment','Diagnostic Products Segment','Medical Devices Segment','Cardiovascular and Neuromodulation Products Segment','Vascular Products Segment','Established Pharmaceutical Products','Nutritional Products','Diagnostic Products','Vascular Products','Other']
out={}
for y in range(2013,2026):
    t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    i=t.find('Components of % Change')
    if i<0: print(y,'no table'); continue
    blk=t[i:i+9000]
    j=blk.find('The increase'); j2=blk.find('The decrease'); 
    ends=[k for k in (j,j2) if k>0]
    if ends: blk=blk[:min(ends)]
    b=blk.replace('​',' ').replace('\n',' ')
    b=re.sub(r'\(\s*([\d.]+)\s*\|?\s*\)',r'-\1',b)   # (0.8 | ) -> -0.8
    b=b.replace('—','0').replace('|',' ')
    b=re.sub(r'\s+',' ',b)
    hdr='Acquisitions' in b
    for m in re.finditer(r'(\d{4}) vs\. (\d{4}) ((?:-?[\d.]+ ){3,5})',b+' '):
        nums=[float(x) for x in m.group(3).split()]
        # find label preceding
        pre=b[:m.start()]
        lab=None;pos=-1
        for L in LABELS:
            k=pre.rfind(L)
            if k>pos: pos=k;lab=L
        key=(lab,m.group(1))
        if key in out: continue
        out[key]=(y,hdr,nums)
for (lab,yr),(src,hdr,nums) in sorted(out.items(), key=lambda kv:(kv[0][0],kv[0][1])):
    cols='total,acq/div,price,volume,fx' if hdr and len(nums)==5 else 'total,price,volume,fx'
    print(f'{lab:55s} {yr} [{cols}] {nums}  (10-K {src})')
