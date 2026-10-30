# PNR run notes (2026-10-10)
Working notes for the run file `Test Runs/2026-10-10 Run - PNR Pentair.md`. Raw filings go under `cache/` (ignored).
- 2026-10-10: template copied to the run file before any fetch; framework v5, template, protocol and brief read.
- Step 0 facts: price $52.47 close 2026-10-09 (Yahoo, aggregator, flagged); 52-wk high $112.13; no split in 2y. Cover: 159,637,950 ord. shares (10-Q filed 2026-07-28, 0000077360-26-000045). UST 30y 5.60% 10/09/2026 (Treasury).
- CONTRARY, written as found: 8-K 2026-07-14 (0000077360-26-000039, EX-99.1): Q2 2026 sales ~$930M, down 17% vs guide of +1%, "Pool channel inventory" destock ~$170M Q2 sales, ~$105M Pool segment income; FY26 sales guide cut to -4% to -7%; CFO Brazis resigned 2026-07-10 after ~4 months in role; former CFO Fishman back as interim. "worsening business conditions, including higher interest rates and inflation".
- CONTRARY: CEO Pool (Pedretti) resigned 2026-04-24, role eliminated (8-K 0000077360-26-000024).
- Taco Group Holdings purchase agreed 2026-07-27, $1.425B, to be funded with $1.4B term loans (8-K 2026-09-02, 0001104659-26-104725); not closed at 2026-09-02.
- Revolver drawn $628.6M + $500M term loan at 2026-05-05 (8-K 0001104659-26-056228).
- New CFO Hau from 2026-11-01 (8-K 0000077360-26-000050).
- 2026-10-10: Step 0, foundations, standing rule, Q1 written (Q1 IN). History verified in 10-Ks (2012 reverse acquisition, ERICO 2015, V&C sale 2017, nVent 2018).
- Q2 written: IN (Pool decides 49.1%; POOL supplier shares 2014-2025; 2026 destock vs Hayward/POOL).
- Q3 WEIGHS FOR; Q4 WEIGHS AGAINST, no STOP (receivables looked at twice, collected). Q3 and Q4 committed together (one commit).
- Q5: integrity IN (closest call, recorded), ability WEIGHS AGAINST.
- RESUME (second session, same day): run file and notes read; resumed at Q6. Q7 draft (q7.py / q7_out.txt) checked: inputs
  match the filed cash-flow statements, but it predates the 2026-10-10 amendments (c: purchases stop after year ten;
  f: sales-growth cut; floor tested first), so it is kept as the record and superseded by q7_final.py / q7_final_out.txt.
- Q6 WEIGHS AGAINST (A: fixed-sum buybacks at $71-$100 above every cut range; growth bought; Taco $1.425B debt-financed,
  no filed record; all-stock STOP not met. B: pay on adjusted figures and revenue, 10-yr fixed options, Aon benchmarking;
  independent chair, ROIC element). Buyback line uses Q7 bottom $36.95.
- Q7 OUT: central all-equity default pair, g cut 9.08% -> 2.62% (sales), $36.95-$49.63 vs $52.47; expected return 4.5-5.4%;
  no case reaches 10% (max allowed 8.04% uncut; bound 9.44%). Fair $13.43 all-equity, $17.49 equity-only. Taco beside $28.03-$40.71.
- Tax: low rate structural (Swiss rate difference), carryforwards not a rate driver; Q7 statutory convention not triggered.
- Q5 misquote corrected before completion: M1994-008 "treat their owners" (was "treat the shareholders"); self-audit records it.
- rows.py (ledger lookup), check_quotes.py (no E-ids; ids exist; fragments in rows).
- Final: Q8-Q12 NOT REACHED; box OUT at Q7; AFTER THE STOP, self-audit, framework notes written; check_quotes 0 problems; check_framework PASS.
