"""PG fold, step 1: working-tree changes and staged-blob texts for the queue, done file, reading list, alerts.json, PORTFOLIO.md.
Register entry inserted by line-exact match of the heading, asserted unique, into the HEAD blob and the working tree (the other
session's CRM hunks kept in the working tree, never staged). Placeholders filled from the HEAD blob's own count."""
import subprocess, json
R = r"C:\Users\chreh\OneDrive\Documents\BRK"
D = R + r"\Test Runs\_research 2026-09-25 PG"
Q = "Screens/WATCHLIST RUN QUEUE.md"; RL = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
DONE = "Screens/_daily/_wave7_done.txt"; AL = "tools/alerts.json"; PF = "PORTFOLIO.md"
HEAD_H = "## COMPLETED FROM THE QUEUE"; T = "PG"
def head(path): return subprocess.run(["git","show","HEAD:"+path],cwd=R,capture_output=True,check=True).stdout.decode("utf-8")
def wt(path):
    raw=open(R+"\\"+path.replace("/","\\"),"rb").read(); return raw.decode("utf-8").replace("\r\n","\n"), b"\r\n" in raw
def wwrite(path,text,crlf): open(R+"\\"+path.replace("/","\\"),"wb").write((text.replace("\n","\r\n") if crlf else text).encode("utf-8"))
def locate(L):
    h=[i for i,l in enumerate(L) if l==HEAD_H]; assert len(h)==1,h
    w=[i for i,l in enumerate(L) if l.startswith("## THE WRITE-EARLY PROTOCOL")]; assert len(w)==1,w
    return h[0],w[0]
HB=head(Q).split("\n"); hi,wi=locate(HB)
before=sum(1 for l in HB[hi+1:wi] if l.startswith("- **"))
assert not any(l.startswith("- **"+T+" ") for l in HB[hi+1:wi])
entry=(open(D+r"\register_entry.md",encoding="utf-8").read().rstrip("\n").replace("__HI__",str(hi)).replace("__WI__",str(wi))
       .replace("__B__",str(before)).replace("__A__",str(before+1))).split("\n")
assert not any("__" in l for l in entry); assert before+1==172,before
def insert(text):
    L=text.split("\n"); h,w=locate(L); b=sum(1 for l in L[h+1:w] if l.startswith("- **"))
    assert not any(l.startswith("- **"+T+" ") for l in L[h+1:w])
    L2=L[:h+1]+entry+L[h+1:]; h2,w2=locate(L2); sl=[l for l in L2[h2+1:w2] if l.startswith("- **")]
    assert sl[0].startswith("- **PG ") and sl[1].startswith("- **TTSH "); assert sum(1 for l in sl if l.startswith("- **PG "))==1
    return "\n".join(L2),b,len(sl),h,w
st,b,a,h0,w0=insert("\n".join(HB)); print("QUEUE HEAD: heading",h0,"write-early",w0,"entries",b,"->",a)
open(D+r"\q_staged.md","w",encoding="utf-8",newline="").write(st)
t,c=wt(Q); t2,b2,a2,h2,w2=insert(t); print("QUEUE WT: heading",h2,"entries",b2,"->",a2,"crlf",c); wwrite(Q,t2,c)
# done
dh=head(DONE); assert dh.endswith("\n") and dh.strip("\n").split("\n")[-1]=="TTSH" and T not in dh.split("\n")
open(D+r"\done_staged.txt","w",encoding="utf-8",newline="").write(dh+T+"\n")
t,c=wt(DONE); assert t==dh; wwrite(DONE,dh+T+"\n",c); print("DONE lines",len((dh+T).strip().split("\n")))
# reading list
rh=head(RL); fold=open(D+r"\reading_fold.md",encoding="utf-8").read(); assert rh.endswith("\n")
open(D+r"\rl_staged.md","w",encoding="utf-8",newline="").write(rh+fold)
t,c=wt(RL); assert t==rh; wwrite(RL,rh+fold,c); print("reading list appended")
# alerts
new=[{"id":"PG-floor-band","ticker":"PG","currency":"USD","op":"<=","threshold":84.16,"active":True,
 "label":"PG at/below $84.16: the E4-28 floor is met on g = 3.0% (the filed growth of five-year owner earnings, FY2012-16 to FY2022-26 and FY2017-21 to FY2022-26 both about 3.2-3.3%/yr) on the five-year capex-end owner earnings of $14,087M and 2,391.1M as-converted shares (common plus ESOP convertible preferred). Q1-Q4 all IN on 2026-09-25; Q5 quit on at $145.68 (yield 4.04-4.23% against a 5.47% sovereign, expectancy 7.0-8.5%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (growth-target flag and E5-08(2) capital-allocation flag live). VOID if any Q2 falsifier has fired: segment share down in three or more of five segments for a third consecutive fiscal year; two consecutive negative total-company organic volume years; negative total-company price in any year; GAAP operating margin below 20.6% two years running; a further Gillette impairment or Walmart above 20% of sales. Source: Test Runs/2026-09-25 Run - PG Procter & Gamble.md."},
 {"id":"PG-rerun-band","ticker":"PG","currency":"USD","op":"<=","threshold":107.25,"active":True,
 "label":"PG at/below $107.25: the E4-28 floor is met only if the full 4.25%/yr per-share growth (3.2% owner-earnings growth plus about 1.0%/yr share reduction) is granted in perpetuity at the D&A end ($14,746M). Prompt for a FULL v4.1 re-run in which that rate is re-tested against the then-current segment-share and organic-volume series before it is spent. Re-derive both PG bands on the FY2027 10-K (about August 2027)."}]
def add_alerts(text):
    d=json.loads(text); assert not any(x["id"].startswith("PG-") for x in d["alerts"])
    i=text.rstrip().rfind("]"); body=text[:i].rstrip()
    assert body.endswith("}")
    ins="".join(",\n  "+json.dumps(x,indent=1,ensure_ascii=False).replace("\n","\n  ") for x in new)
    out=body+ins+"\n "+text[i:]
    d2=json.loads(out); assert len(d2["alerts"])==len(d["alerts"])+2
    return out
ah=head(AL); open(D+r"\alerts_staged.json","w",encoding="utf-8",newline="").write(add_alerts(ah))
t,c=wt(AL); wwrite(AL,add_alerts(t),c); print("alerts added, crlf",c)
# portfolio
row=open(D+r"\portfolio_row.md",encoding="utf-8").read().strip("\n")
ph=head(PF)
def add_row(text):
    L=text.split("\n"); i=[k for k,l in enumerate(L) if l.startswith("| — | CL |")]; assert len(i)==1
    assert not any(l.startswith("| — | PG |") for l in L)
    return "\n".join(L[:i[0]+1]+[row]+L[i[0]+1:])
open(D+r"\pf_staged.md","w",encoding="utf-8",newline="").write(add_row(ph))
t,c=wt(PF); assert t==ph; wwrite(PF,add_row(t),c); print("portfolio row added")
