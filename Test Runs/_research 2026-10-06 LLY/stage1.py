import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
s = s.replace("**Copy this file to its dated name before any fetch.**", "**Copied from the template to this dated name before any fetch.**", 1)
start = s.index("## STEP 0")
end = s.index("---\n## Q1")
new = open(sys.argv[2], encoding='utf-8').read()
s = s[:start] + new + "\n" + s[end:]
open(p, 'w', encoding='utf-8').write(s)
