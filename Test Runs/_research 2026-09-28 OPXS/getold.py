from getidx import doc
L=[('0001571049-15-009981','t1502912_10k.htm','cache/10k_fy2015.txt'),
('0001571049-14-007394','t1402488_10k.htm','cache/10k_fy2014.txt'),
('0001571049-13-001285','t1300660_10k.htm','cache/10k_fy2013.txt'),
('0001144204-11-071709','v243906_10k.htm','cache/10k_fy2011.txt')]
for a,n,o in L:
    try: doc(a,n,o)
    except SystemExit as e: print(e)
