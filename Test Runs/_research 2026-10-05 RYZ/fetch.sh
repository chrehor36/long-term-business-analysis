#!/bin/bash
# usage: fetch.sh CIKnodash accession-with-dashes primarydoc outname
UA="Chris Hrehor chrehor36@gmail.com"
acc=$(echo $2 | tr -d '-')
curl -s -H "User-Agent: $UA" -H "Accept-Encoding: identity" "https://www.sec.gov/Archives/edgar/data/$1/$acc/$3" -o "$4.htm"
python - "$4.htm" "$4.txt" <<'PY'
import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
s=re.sub(r'(?i)</td>|</th>',' | ',s)
s=re.sub(r'<[^>]+>','',s)
s=html.unescape(s).replace('\xa0',' ')
s=re.sub(r'[ \t]+',' ',s)
s=re.sub(r'\n\s*\n+','\n',s)
open(sys.argv[2],'w',encoding='utf-8').write(s)
print(sys.argv[2],len(s))
PY
rm -f "$4.htm"
sleep 0.3
