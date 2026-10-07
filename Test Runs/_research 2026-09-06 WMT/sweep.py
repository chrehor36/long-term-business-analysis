import glob,os,re
D=os.path.dirname(os.path.abspath(__file__))
order=['q4fy18','q1fy19','q2fy19','q3fy19','q4fy19','q1fy20','q2fy20','q3fy20','q4fy20',
'q1fy21','q2fy21','q3fy21','q4fy21','q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23',
'q3fy23','q4fy23','q1fy24','q2fy24','q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25',
'q1fy26','q2fy26','q3fy26','q4fy26','q1fy27','q2fy27']
for q in order:
    p=os.path.join(D,f"8k-{q}-ex991.txt")
    if not os.path.exists(p): print(q,"MISSING"); continue
    t=open(p,encoding='utf-8',errors='replace').read()
    lines=t.split('\n')
    hits=[l for l in lines if re.match(r'^\|?\s*(Transactions|Average ticket|Traffic|Ticket|eCommerce contribution|Comp sales|Comparable sales)\b', l.strip(), re.I) and len(l)<400]
    print("="*70); print(q, "  len",len(t))
    for h in hits[:20]: print("   ", h[:200])
