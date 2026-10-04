"""RUN QUEUE MANAGER. The operator asked for every business in every list to be run.
That is hundreds of 400k-token reads across many sessions, and usage limits killed four
runs tonight already, so the queue must survive interruption. State lives in
Screens/RUN_QUEUE.json; run files on disk are the source of truth for what is DONE.

  python Screens/queue.py status      what is done, running, pending
  python Screens/queue.py next N      the next N tickers to run, in order
  python Screens/queue.py done TICK   mark done (normally inferred from the run file)
"""
import csv, json, os, sys, glob
from datetime import date, datetime
sys.stdout.reconfigure(encoding="utf-8")
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE=os.path.join(ROOT,"Screens","RUN_QUEUE.json")

def latest_queue():
    c=sorted(glob.glob(os.path.join(ROOT,"Screens","* MASTER RUN QUEUE.csv")))
    return c[-1] if c else None

def done_set():
    """Run files on disk are the truth. A name with a committed run file is DONE."""
    out={}
    for fn in os.listdir(os.path.join(ROOT,"Test Runs")):
        if " Run - " in fn and fn.endswith(".md"):
            out[fn.split(" Run - ",1)[1].split(" ")[0].upper()]=fn
    return out

def load():
    try: return json.load(open(STATE,encoding="utf-8"))
    except Exception: return {"claimed":{},"notes":{}}

def save(s): json.dump(s,open(STATE,"w",encoding="utf-8"),indent=1)

def rows():
    q=latest_queue()
    if not q: return []
    return list(csv.DictReader(open(q,encoding="utf-8-sig")))

def main():
    cmd=(sys.argv[1] if len(sys.argv)>1 else "status").lower()
    st=load(); dn=done_set(); rs=rows()
    pend=[r for r in rs if r["ticker"] not in dn and r["financial"].lower()!="true"]
    if cmd=="status":
        print(f"RUN QUEUE {date.today()}   source: {os.path.basename(latest_queue() or '-')}")
        print(f"  priced      {len(rs)}")
        print(f"  DONE        {len(dn)}  (run files on disk)")
        print(f"  pending     {len(pend)} non-financial")
        print(f"  financial   {sum(1 for r in rs if r['financial'].lower()=='true')} "
              f"(priced and flagged; not run, per the 2026-09-01 operator call)")
        t1=[r for r in pend if float(r["growth_required"])<=0.06]
        print(f"\n  TIER 1, needs <=6% perpetual growth: {len(t1)}")
        print("   " + ", ".join(r["ticker"] for r in t1[:40]))
        cl=st.get("claimed",{})
        if cl: print(f"\n  claimed/in flight: {', '.join(f'{k} ({v})' for k,v in cl.items())}")
    elif cmd=="next":
        n=int(sys.argv[2]) if len(sys.argv)>2 else 5
        cl=st.get("claimed",{})
        nxt=[r for r in pend if r["ticker"] not in cl][:n]
        for r in nxt:
            print(f"{r['ticker']:6s} {float(r['yield_bottom']):>7.2%} yield  "
                  f"{float(r['growth_required']):>6.2%} growth  "
                  f"{r['spread'] or '-':>6s} spread  {r['industry']}")
        for r in nxt: cl[r["ticker"]]=datetime.now().strftime("%Y-%m-%d %H:%M")
        st["claimed"]=cl; save(st)
    elif cmd=="done":
        t=sys.argv[2].upper()
        st.get("claimed",{}).pop(t,None); save(st)
        print(f"{t} released from claimed; run file on disk decides DONE")
    elif cmd=="release":
        st["claimed"]={}; save(st); print("all claims cleared")

if __name__=="__main__": main()
