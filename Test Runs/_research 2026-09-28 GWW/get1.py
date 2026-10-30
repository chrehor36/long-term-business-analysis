from getidx import idx, doc
for acc,out in [('0000277135-26-000011','k2025'),('0000277135-26-000079','q2606'),('0000277135-26-000076','e2608'),('0000277135-25-000082','e2505'),('0000277135-25-000179','e2512'),('0001104659-26-089478','e2608b'),('0001104659-26-025575','proxy26')]:
    names=idx(acc)
    print(acc,out,[n for n in names if n.endswith('.htm')])
    for n in names:
        if n.endswith('.htm') and ('ex' in n.lower() or n.startswith('gww-2') or 'def14a' in n or '8k' in n) and 'R' != n[0]:
            doc(acc,n,f'cache/{out}_{n}.txt')
