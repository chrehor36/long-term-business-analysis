from fetch_core import *
L=[("0001437749-26-028541","ex_1007005.htm","EX991_2026-08-19_letter"),
("0001193125-26-273417","d178962dex991.htm","EX991_2026-06-17"),
("0001193125-26-273417","d178962dex101.htm","EX101_2026-06-17"),
("0001193125-26-273417","d178962dex31.htm","EX31_2026-06-17_charter"),
("0001193125-26-164338","d34261dex991.htm","EX991_2026-04-15_pr"),
("0001193125-26-164338","d34261dex992.htm","EX992_2026-04-20_riskfactors"),
("0001628280-26-026081","allbirdsq12026preliminarye.htm","EX99_2026-04-21_prelim"),
("0001628280-26-022181","allbirdsprojectarisepressr.htm","EX99_2026-03-31_arise"),
("0001653909-24-000064","rsscharteramendment.htm","EX31_2024-08-30_rss"),
("0001653909-24-000064","rsspressrelease.htm","EX99_2024-08-30_rss")]
for a,d,n in L:
    try: grab(a,d,n)
    except Exception as e: print("FAIL",n,e)
