# AQN research notes (2026-10-18)
Started: template copied before any fetch.

## Facts gathered (2026-10-18)
- Sovereign USD 30y par 5.43% at 10/16/2026, US Treasury (tools/sources.py).
- Cover shares 768,351,419 (40-F 2026-03-06, acc 0001174169-26-000015) via Screens/cover_shares.py.
- tools/run.py AQN: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED" -> figures from filed statements + XBRL companyfacts.
- FY2025 filed CF: OCF 593.6, capex (PP&E+intangibles) 771.9, D&A 400.3, SBC 13.0, interest paid 312.1, income tax received net 73.4. XBRL matches.
- BS 12/31/25: cash 32.7, LTD current 364.0 + LT 6,168.9 = 6,532.9; pref 184.3; NCI 407.2 (tax equity 328.5, other 78.7); equity to shareholders 4,641.1; goodwill 1,320.1; deficit (2,961.3).
- 2024 net loss to common (1,391.0) from discontinued renewables (loss on held for sale 1,357.3).
- Auditor EY since 2013, clean opinion, ICFR effective; CAM = regulatory assets/liabilities.
- AIF: geographic monopolies; no named SEC-filing rival -> CONVENTION competitor choice.
- Suralis: AIF table says 64%, AIF text says ~68.073% -> inconsistency inside the filing.
- NH DOE moved to dismiss Granite State (2023) and EnergyNorth (2024) rate cases; NHPUC ordered independent audit of accounting info (post customer-system implementation).
- Empire MO: staff+OPC motions to dismiss (Feb 2025); OPC recommended no increase citing billing issues; $97M phased over 3 yrs contingent on billing/customer metrics.
- Empire KS: asks +$15.8M, ~93.77% of KS base rates.
- Adjusted EPS "exceeded the top end of previously provided guidance range by $0.02" (MD&A FY2025).

## Close (2026-10-18)
- Box: OUT at Q7. Central range -8.85 to -6.85 a share (organic pair); fair -8.95 all-equity, -3.70 equity-only.
- check_ids.py: 84 ids, 130 citations, 58 quoted fragments, 0 problems. tools/check_framework.py: PASS.
