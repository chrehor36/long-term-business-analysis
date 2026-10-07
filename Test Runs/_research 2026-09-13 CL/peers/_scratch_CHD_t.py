import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for f in sorted(glob.glob(sys.argv[1])):
    L=open(f,encoding="utf-8").read().split("\n")
    for i,l in enumerate(L):
        if re.match(r"\s*(Net Sales - |Net sales - )",l):
            # find end
            j=i
            while j<len(L) and not re.search(r"Net Sales (increase|decrease|change)|Net sales (increase|decrease|change)",L[j]) : j+=1
            end=j+4
            print("==",f,i,end)
            print(re.sub(r"\s+"," "," ".join(L[i:end])).strip())
