import json, os, sys, re
D=os.path.dirname(os.path.abspath(__file__))
t=sys.argv[1]; pat=sys.argv[2]
cf=json.load(open(os.path.join(D,'companyfacts_%s.json'%t)))
for ns,tags in cf['facts'].items():
    for tag in sorted(tags):
        if re.search(pat,tag,re.I):
            u=list(tags[tag]['units'].keys())
            n=sum(len(v) for v in tags[tag]['units'].values())
            print('%-8s %-70s %s n=%d'%(ns,tag,u,n))
