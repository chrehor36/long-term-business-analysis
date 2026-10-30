# PCG run notes (2026-10-26)

Started: template copied to run file before any fetch.

## Notes on THE FRAMEWORK v5 (read once, top to bottom, slices of <=340 lines)

- Scope: rules rest only on rows of principle_ledger_v5.csv; a CONVENTION confesses an invention, never imports a rule.
- I. Boxes IN / OUT / TOO HARD. TOO HARD carries cause: WORK (knowable, work not done; research pass steps 1-2 written)
  or NATURE (insiders would not write the forecast down; closed, price does not reopen).
- II. Foundations: not a gate. III. Standing rule: buyer's conduct (no leverage that can call etc.).
- Q1 STOP: understanding = foresee earning power and competitive position in 5-10 years (M2012-065, M2000-037).
  Holding company / segments read by parts; a part "matters" at >half five-year operating profit or else largest.
- Q2 STOP: castle tests 1-11. Business of parts: deciding part >half of five-year op profit. "The standing castle that
  protects only ordinary returns" is OUT, BUT "A return set by a regulator is the exception, carried to Q3 as a second
  best [M2009-104], [L2009-012]". Regulated moat that broke: L2023-011 (utilities, adverse regulatory returns);
  OPEN tension: L2023-011 and M2024-011 vs earlier rows treating utility return as dependable.
  Change for the better credited only on a full cycle; else TOO HARD (NATURE) with a re-look condition.
  Castle shown open on evidence -> OUT; future cannot be judged -> TOO HARD.
- Q3 WEIGHING; capital-heavy second best (M2018-055, L2009-012, M2009-104); the "little or no debt" STOP is at Q9
  and is stated for whole businesses only.
- Q4 STOP on confusion (TOO HARD WORK/NATURE) or suspicion (OUT); else WEIGHING. Balance sheets 8-10 years first
  (M2025-032). Catastrophe losses excluded from "true" earnings = "deceptive nonsense" (L2002-002) -- relevant to
  wildfire charges. Make-the-numbers / guidance / adjusted figure: weigh at Q4, judge at Q5.
- Q5 STOP on integrity on doubt (M2013-088). WEIGHING on ability.
- Q6 WEIGHING; one STOP: all-stock deal in undervalued stock (L2009-019). Serial issuance candidate second STOP (OPEN).
  Buyback with no stated price weighs against unless prices paid <= bottom of Q7 range.
- Q7 STOP. Range convention: five-year average owner cash after every real cost; growth shown (aggregate) capped;
  ten years then zero nominal growth; discount at long gov rate (30y Treasury); ends = no-growth and shown-growth.
  Floor ~10% (applied to owner cash after company tax). Floor tested first: if no case earns the floor at the price ->
  OUT whatever width. Then width >3x -> TOO HARD; price inside/just below a narrower range -> OUT; IN only if screamer.
  Specifics (a)-(f): cycle base for aberrational end years; decline carried as bottom; acquisitions; working capital;
  growth spending (maintenance central, growth spending grows with growth, stops at year ten); cap (sales growth).
  Regulated utility: equity-only central (owner cash after interest after tax vs market cap); credit increase in
  long-term debt over window (averaged per year; CP/short-term/cash excluded; securitization bonds repaid by a
  dedicated customer charge left out with the charge) against GROWTH spending only (capex above maintenance guess),
  capped at deciding part's allowed debt share (weighted by rate base). All-equity shown beside.
  Fair price (Part VII): each end case valued at 10% instead of long rate; average; per share.
- Q8 STOP: bond, more of what I own. Q9 WEIGHING: debt vs ability to pay in bad years; "A catastrophic event can render
  a single utility insolvent" [L2005-019]; product liability that grows (M2001-008). Q10 WEIGHING. Q12 optional.
- VII: after a STOP, facts written under AFTER THE STOP: FACTS FOUND, NOT WEIGHED; integrity facts flagged.
  Research pass only run where some case earns the floor at the price.
  run.py arithmetic lines only.

## Data gathered (2026-10-26), sources in run file
- tools/run.py PCG failed: "PCG: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (PCG tags D&A under no
  standard us-gaap tag). Arithmetic done by hand from the filed statements: see q7.py, peers.py, capex_da_out.txt.
- cover_shares.py: 2,680,173,293 (PCG cover, includes 477,743,590 held by the Utility) and 264,374,809 (the Utility's
  own common, all held by PCG). Economic PCG common: 2,202,429,703; balance sheet 9/30/2026: 2,202,416,553.
- Price $12.63 close 2026-10-23 (Yahoo chart via tools/sources.py; aggregator). 30y Treasury 5.33% (10/23/2026, Treasury).
- Strategic review announced 2026-09-02; 2027 capex cut 13.4 -> 11.4B; 2028-30 forecast withdrawn (10-Q Q3 2026).
- Decision path chosen: Q1 IN (routing the wildfire question to Q2, where the text puts the regulatory climate);
  Q2 TOO HARD (NATURE). Alternative reading (Q1 test 4 closes it one step earlier, same box) noted for the unclear section.
