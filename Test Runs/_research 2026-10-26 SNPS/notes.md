# SNPS run notes (2026-10-26)

Working notes for the SNPS purchase run. Framework notes in framework_notes.md.

## Filing facts gathered (accessions)
- 10-K FY2025 (FYE 2025-10-31), filed 2025-12-22, acc 0000883241-25-000028.
- 10-Q Q3 FY2026 (2026-07-31), filed 2026-08-26, acc 0000883241-26-000025. Cover 191,636,646 shares as of 2026-08-24.
- DEF 14A 2026-02-19, acc 0000883241-26-000007.
- 8-K 2025-11-12 acc 0001193125-25-276232: restructuring ~10% workforce, $300-350M charges.
- 8-K 2025-12-01 acc 0001193125-25-303209: NVIDIA bought 4,821,717 shares at $414.79 = $2.0B private placement.
- 8-K 2026-02-25 acc 0001193125-26-071601: buyback replenished to $2.0B.
- 8-K 2026-03-02 acc 0001193125-26-084396: $250M ASR (Bank of Nova Scotia); 10-Q: 564.7K shares at avg $442.69; plus 126.7K open market at $394.78 ($50M).
- 8-K 2026-05-27 acc 0001193125-26-241920: cooperation agreement with Elliott; Jesse Cohn to board 2026-06-01.
- 8-K 2026-08-12 acc 0001193125-26-345878: GC Janet Lee leaving by 2026-12-31.
- 8-K 2026-10-05 acc 0001193125-26-413359: $1B ASR with JPMorgan (after the 10-Q).
- Ansys (10-K Note 4): closed 2025-07-17; $34.86B total: cash $17.61B, stock $17.11B (29.955M sh at $571.20), assumed awards $0.13B; cash acquired $0.93B. Goodwill $23.44B; intangibles $12.99B (tech 6.5B 6-9y; customer 5.1B 9y; backlog 0.44B 2y; trade names 0.95B 23y). Deferred tax liab $2.62B. Pro forma revenue FY2025 $8.92B, FY2024 $8.45B. Cash part larger -> an ACQUISITION under Q7 (c) (larger part), not a merger.
- Regulatory divestitures: OSG + PowerArtist to Keysight 2025-10-17, $604M cash, gain $548.9M.
- Processor IP sold to GlobalFoundries 2026-06-01, $443.3M cash, gain $425.4M (10-Q).
- Software Integrity sold 2024-09-30 $1.65B (gain $868.8M).
- FY2025: rev 7,054.2 (DA 5,302.3; IP 1,751.8); adj op inc DA 2,213.5 (42%), IP 419.3 (24%, from 730.2/38% FY24). Time-based 49%, upfront 29%, maint & service 22%. R&D 35% of revenue. Backlog $11.4B.
- IP decline causes (10-K MD&A): China export controls incl. Q3 2025 BIS "is-informed" letter (5/29/2025, rescinded 7/2/2025), "weaker than expected demand from a major foundry customer", "certain roadmap and resource decisions that did not yield their intended results".
- China revenue: FY23 855.0 (16.1%), FY24 989.5 (16.1%), FY25 814.3 (11.5%); 9M FY26 707.0 of 7,161.6 (9.9%). Korea FY25 947.0.
- One customer 12.6% FY24, 13.5% FY23 (unnamed); none >10% FY25 implied.
- Class actions (Kim, filed 2025-10-31; NE Teamsters; Sterling Heights) + derivative suits re Design IP statements; consolidated; no accrual.
- Debt: LT debt 13,462 (10/31/25) -> 9,017 LT + 1,020 ST (7/31/26). Repaid 3,464 in 9M FY26. Cash 3,607.7 (7/31/26).
- 9M FY26: rev 7,161.6; OCF 2,298.6; capex 156.1; SBC 712.6; restructuring 236.3.
- Cash taxes paid FY25 512.7, FY24 680.1, FY23 98.0. Interest paid FY25 353.8.
- Buybacks FY2015-2023: 260, 400, 380, 400, 329, 242, 753, 1,100, 1,161; none FY24-25; FY26 9M 300.
- run.py: capex alt line counts "PaymentsToAcquireIntangibleAssets" = filed line "Acquisitions, net of cash acquired" (16,681 in FY25) - it is acquisitions, not intangible purchases.
