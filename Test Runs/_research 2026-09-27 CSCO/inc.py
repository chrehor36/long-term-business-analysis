import re,sys,glob
files={
 'FY1996':'filings/1996-10-25_10-K_0000950149-96-001640.txt',
 'FY1997':'filings/1997-10-22_10-K_0000891618-97-004205.txt',
 'FY1998':'filings/1998-09-25_10-K_0000891618-98-004310.txt',
 'FY1999':'filings/1999-09-28_10-K405_0000891618-99-004365.txt',
 'FY2000':'filings/2000-09-29_10-K_0001095811-00-003692.txt',
 'FY2001':'filings/2001-09-24_10-K_0001095811-01-505065_f75710ex13.txt.txt',
 'FY2002':'flat/2002-09-18_10-K_0000891618-02-004345_f84358exv13.htm.txt',
 'FY2003':'flat/2003-09-10_10-K_0001193125-03-047374_dex131.htm.txt',
 'FY2004':'flat/2004-09-20_10-K_0001193125-04-158427_dex131.htm.txt',
 'FY2005':'flat/2005-09-19_10-K_0001193125-05-187168_dex131.htm.txt',
 'FY2006':'flat/2006-09-18_10-K_0001193125-06-192133_dex131.htm.txt',
 'FY2007':'flat/2007-09-18_10-K_0001193125-07-202552_dex131.htm.txt',
 'FY2008':'flat/2008-09-15_10-K_0001193125-08-195608_dex131.htm.txt',
 'FY2009':'flat/2009-09-11_10-K_0001193125-09-190326_dex131.htm.txt',
 'FY2010':'flat/2010-09-21_10-K_0001193125-10-213400_dex131.htm.txt',
 'FY2011':'flat/2011-09-14_10-K_0001193125-11-247394.txt',
 'FY2012':'flat/2012-09-12_10-K_0001193125-12-388590.txt',
 'FY2013':'flat/2013-09-10_10-K_0000858877-13-000049.txt',
 'FY2014':'flat/2014-09-09_10-K_0000858877-14-000029.txt',
 'FY2015':'flat/2015-09-08_10-K_0000858877-15-000070.txt',
 'FY2016':'flat/2016-09-08_10-K_0000858877-16-000117.txt',
 'FY2017':'flat/2017-09-07_10-K_0000858877-17-000016.txt',
 'FY2018':'flat/2018-09-06_10-K_0000858877-18-000011.txt',
 'FY2019':'flat/2019-09-05_10-K_0000858877-19-000012.txt',
 'FY2020':'flat/2020-09-03_10-K_0000858877-20-000010.txt',
 'FY2021':'flat/2021-09-09_10-K_0000858877-21-000013.txt',
 'FY2022':'flat/2022-09-08_10-K_0000858877-22-000013.txt',
 'FY2023':'flat/2023-09-07_10-K_0000858877-23-000023.txt',
 'FY2024':'flat/2024-09-05_10-K_0000858877-24-000017.txt',
 'FY2025':'flat/2025-09-03_10-K_0000858877-25-000111.txt',
 'FY2026':'flat/2026-09-02_10-K_0000858877-26-000132.txt'}
pat=re.compile(r'(?i)(total net sales|net sales|total revenue|^\s*product|^\s*service|gross margin|operating income|amortization of|restructuring|impairment|in-process|purchased research|july \d|years ended)')
which=sys.argv[1:] or list(files)
for k in which:
    f=files[k]
    L=open(f,encoding='utf-8',errors='ignore').read().splitlines()
    idx=[i for i,l in enumerate(L) if re.search(r'(?i)statements? of operations',l)]
    # pick the one followed by '(net sales|revenue)' within 15 lines
    start=None
    for i in idx:
        if any(re.search(r'(?i)(net sales|revenue)',x) for x in L[i:i+15]): start=i
    if start is None: print(k,'NO CFS'); continue
    print('#####',k,f,start)
    for l in L[start:start+45]:
        if pat.search(l): print('  ',l.strip()[:200])
