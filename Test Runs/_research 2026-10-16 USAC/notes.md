# USAC run notes (2026-10-16)
Working notes for the v5 purchase run of USA Compression Partners, LP (USAC, CIK 1522727). Drafts only; the run file is the record.

## Filings read (EDGAR, User-Agent "Chris Hrehor chrehor36@gmail.com"); raw text kept in cache/ (gitignored)
- 10-K FY2025 0001522727-26-000015 (filed 2026-02-17); 10-Q Q2 2026 0001522727-26-000064 (filed 2026-08-06)
- 10-Ks for the operating record: FY2014 0001558370-15-000104; FY2015 0001558370-16-003160; FY2016 0001558370-17-000559;
  FY2017 0001558370-18-000600; FY2018 0001558370-19-000738; FY2019 0001522727-20-000005; FY2020 0001522727-21-000010;
  FY2021 0001522727-22-000006; FY2022 0001522727-23-000006; FY2023 0001522727-24-000008; FY2024 0001522727-25-000010
- 8-Ks: 2025-12-01 0001193125-25-303103 (J-W agreement); 2026-01-14 0001522727-26-000007 (J-W closing);
  8-K/A 2026-03-30 0001522727-26-000031 (J-W audited FY to 2025-10-31, Ex. 99.1; pro forma, Ex. 99.2);
  2026-07-06 0001193125-26-296333 (redomicile, 8-K12B); 2026-08-04 0001522727-26-000058 (Q2 results);
  2026-09-10 0001522727-26-000071 (NYSE to TXSE); 2026-09-24 0001193125-26-401095 (6.750% notes due 2035, $600M);
  2026-10-05 0001522727-26-000098 (Class A Units, 2026-10-01)
- Rivals: Archrock FY2025 10-K 0001389050-26-000009, FY2021 0001389050-22-000007, FY2018 0001389050-19-000021;
  Kodiak FY2025 10-K 0001767042-26-000012; XBRL company facts for USAC, Archrock (CIK 1389050), Kodiak (CIK 1767042).
  Enerflex (CIK 1904856) files a 40-F under IFRS: flagged, not used.

## Scripts (arithmetic only)
- fetch.py (EDGAR fetch and HTML-to-text), xbrl.py and ff.py (XBRL tables; ff.py takes first-filed 10-K values)
- returns.py -> returns_output.txt (field returns on tangible assets; USAC owner cash series)
- q7_computation.py -> q7_output.txt (COMPUTATION, NOT A CLEARANCE: range and fair price)
- check_citations.py (no E-ids; ids exist; quoted fragments beside ids are in their rows)
- led.py (ledger row lookup), splice.py (writes a section into the run file), sec_*.md (section drafts)

## Lineage warning
USAC's XBRL frames for 2016-2017 carry the CDM predecessor's figures (2018 reverse-acquisition accounting); the
first-filed values (ff.py) give USAC's own figures for 2013-2017 and the combined partnership's from 2018.
