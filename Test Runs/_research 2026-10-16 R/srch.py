import csv,sys,re
for r in csv.reader(open(sys.argv[1],encoding='utf-8')):
    if re.search(sys.argv[2], r[2], re.I): print(r[0],'|',r[2][:int(sys.argv[3]) if len(sys.argv)>3 else 400]); print()
