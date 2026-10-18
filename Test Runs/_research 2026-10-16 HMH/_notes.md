# HMH run notes (2026-10-16), working file
- Run file copied from the template before any fetch.
- Lock: held by the dispatching session (Screens/_daily/_overnight.lock present, written 2026-10-16T00:46).

## Filings fetched (raw copies in cache/, gitignored)
- 424B4 2026-04-01 acc 0001193125-26-138102 (FS FY2024-FY2025; Business, Risk factors, MD&A)
- S-1 2024-08-12 acc 0001193125-24-198984 (FS FY2022-FY2023)
- 10-Q Q1 2026-05-06 acc 0001628280-26-031295; 10-Q Q2 2026-08-05 acc 0001628280-26-053385
- 8-K 2026-04-02 acc 0001193125-26-140110; 8-K 2026-08-05 acc 0001628280-26-053339 (Ex 99.1 Q2 release); 8-K 2026-05-06 acc 0001628280-26-031292
- S-1 (resale) 2026-09-28 acc 0001193125-26-405527 (shares as of 2026-09-28)
- No DEF 14A on EDGAR as of 2026-10-16.
- Rivals: NOV 10-K FY2016 0001193125-17-047937, FY2019 0001564590-20-004552, FY2022 0000950170-23-002767, FY2023 0000950170-24-015145, FY2025 0001193125-26-048350; Nabors 10-K FY2019 0001558370-20-001335, FY2022 0001558370-23-001064, FY2025 0001104659-26-014997 (FY2016 0001558370-17-001099: Rig Services mixed with directional drilling, not used); SLB 10-K FY2019 0001564590-20-001578, FY2022 0001564590-23-000762, FY2025 0001193125-26-021017.

## Key figures ($000)
Revenue 2022 677,213; 2023 785,446; 2024 843,363; 2025 821,754; H1'26 342,143 (H1'25 401,887)
Operating income 20,317; 78,001; 118,614; 107,889; H1'26 14,332 (incl. 22,775 SBC)
Net income -26,564; 17,402; 51,956; 46,123; H1'26 -1,144
OCF 974; 25,574; 34,861; 88,310; H1'26 25,156 (H1'25 -7,552)
PP&E capex 7,534; 14,116; 16,096; 9,617 ; dev 7,457; 10,541; 2,244; 6,649 ; acq 3,254; 0; 19,624; 4,457
Cash interest paid 18,604; 26,159; 23,284; 28,024 ; WC changes (CF lines) -30,500; -36,586; -82,281; -33,984
Segment op income after D&A: ESS 12.1; 13.6; 46.1; 47.5 ; PCS 24.2; 71.8; 81.4; 71.3 ($m) -> PCS 67.6% of 4-yr total
Balance sheets: see run file Step 0 table.
## Rivals (segment margin, as filed)
NOV rig segments (Rig Systems + Rig Aftermarket to 2016; Rig Technologies 2017-2023): 2014 23.4%, 2015 20.8%, 2016 -19.5% (Aftermarket alone 29.0%, 25.9%, 16.2%), 2017 -0.6%, 2018 8.3%, 2019 -19.5% (9.7% before other items), 2020 -18.9%, 2021 2.5%, 2022 7.1%, 2023 12.0% (10.9% before other items). Energy Equipment 2023-2025: 7.9%, 12.4%, 10.0% (mixed segment).
Nabors Rig Technologies (adjusted op income): 2017 -13.2%, 2018 -9.5%, 2019 -4.3%, 2020 -10.2%, 2021 0.1%, 2022 4.6%, 2023 8.0%, 2024 10.0%, 2025 5.4%.
SLB Cameron 2017 14.3%, 2018 11.8%, 2019 11.5%; Production Systems 2020 9.4%, 2021 9.4%, 2022 9.5%, 2023 12.7%, 2024 15.9%, 2025 16.4% (mixed segments, pre-tax segment income before charges).

## Close
- Box: TOO HARD (NATURE) at Q2. COMPUTATION: range $8.53-$14.13, fair $5.09 all-equity; equity-only not positive on filed interest ($3.58 on today's bonds).
- check_run.py: 39 ids, 0 problems; tools/check_framework.py PASS (2026-10-16).
