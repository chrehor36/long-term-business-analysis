import re, sys, io, html as H
def tables(path):
    src=io.open(path,encoding="utf-8").read()
    src=re.sub(r"(?is)<(script|style).*?</\1>"," ",src)
    out=[]
    for m in re.finditer(r"(?is)<table[^>]*>(.*?)</table>", src):
        body=m.group(1); rows=[]
        for r in re.finditer(r"(?is)<tr[^>]*>(.*?)</tr>", body):
            cells=[]
            for c in re.finditer(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", r.group(1)):
                t=re.sub(r"(?s)<[^>]+>"," ",c.group(1))
                t=H.unescape(t); t=re.sub(r"[\s\xa0]+"," ",t).strip()
                cells.append(t)
            cells=[c for c in cells if c not in ("","|")]
            if cells: rows.append(cells)
        if rows: out.append((m.start(), rows))
    return out, src
if __name__=="__main__":
    path=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else None
    n=int(sys.argv[3]) if len(sys.argv)>3 else 3
    ts,src=tables(path)
    hits=0
    for pos,rows in ts:
        flat=" ".join(" ".join(r) for r in rows)
        if pat and not re.search(pat, flat, re.I): continue
        hits+=1
        print(f"\n===== TABLE at {pos} ({len(rows)} rows) =====")
        for r in rows[:120]:
            print(" ; ".join(r))
        if hits>=n: break
