# find PDF page numbers whose text matches a pattern: python pages.py <txt-with-formfeeds> <regex>
import sys, re
pages = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\f')
for i, p in enumerate(pages, 1):
    if re.search(sys.argv[2], p):
        print(i, end=' ')
print()
