"""Print BYD segment-note tables as joined English rows (drops lines with CJK characters)."""
import re, sys, os

here = os.path.dirname(os.path.abspath(__file__))
cjk = re.compile(r"[　-鿿＀-￯]")
anchors = ["Revenue from external trading", "Sales to external customers"]
for y in sys.argv[1:]:
    fn = os.path.join(here, f"BYD_AR{y}.txt")
    lines = [l.strip() for l in open(fn, encoding="utf-8")]
    print("#####", y)
    for i, l in enumerate(lines):
        if l in anchors:
            page = next((lines[k] for k in range(i, 0, -1) if lines[k].startswith("=== PDF PAGE")), "")
            # header: 30 lines back
            head = [x for x in lines[i - 30:i] if x and not cjk.search(x)]
            body = [x for x in lines[i:i + 75] if x and not cjk.search(x)]
            print(" ", page)
            print("   HEAD:", " | ".join(head))
            print("   BODY:", " | ".join(body))
