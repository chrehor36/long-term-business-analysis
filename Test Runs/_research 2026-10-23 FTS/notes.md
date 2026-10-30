# FTS research notes (2026-10-23)

Run file copied from template before any fetch.

## Files
- `scripts/fetch.py` fetches an SEC document into `cache/` (ignored) as HTML and text.
- `scripts/table.py` builds `table10.txt` / `table10.json` from SEC companyfacts (40-F facts, latest-filed value per FY end).
- `scripts/peers.py` peer ROE and OCF less capex (AEE, XEL, PNW, FTS); output `peers.txt`.
- `scripts/q7.py` Q7 arithmetic; output `q7_out.txt`.
- `scripts/q.py` prints ledger rows by id.
- `scripts/check_ids.py` citation check (no E-ids, ids resolve, quoted fragments in the row); written on resume (it was
  listed here before the kill but not on disk).
- `scripts/apply_q7.py` appended `drafts/q7.md` and wrote the Q7 lines back into Q6; `drafts/close.md` is Q8 to the end.

## Sovereign
Bank of Canada Valet BD.CDN.LONG.DQ.YLD 2026-10-21 = 4.19 (benchmark long-term GoC bond).

## Segment common equity earnings (C$M, MD&A Business Unit Performance tables)
year | ITC | UNS | CH | FBCE | FAB | FBCEl | Other El | Energy Infra | regulated total
2021 | 426 | 292 | 93 | 185 | 141 | 59 | 118 | 38 | 1,314 (+38 infra)
2022 | 454 | 328 | 103 | 203 | 151 | 64 | 134 | 72 | 1,437 (+72 infra)
2023 | 508 | 400 | 105 | 274 | 162 | 68 | 146 | - | 1,663
2024 | 542 | 448 | 128 | 293 | 181 | 72 | 163 | - | 1,827
2025 | 592 | 437 | 191 | 336 | 182 | 75 | 167 | - | 1,980

## Resume, 2026-10-23
Killed after Q4 (49175fd9). Resumed at Q5 without refetching. q7.py checked against the Q7 text and changed: long-term
debt only for the credit (short borrowings out), businesses sold netted under (c), the cap test over ten years, case A
ends labelled and the halves growth shown, floor-test bounds added. Box: OUT at Q7. Range C$72.41 to C$97.93 (equity-only,
central, 4.19%); fair C$28.96; all-equity fair C$-27.12; price C$80.99. Bound: no spending charged at all, C$65.00 at 10%.
