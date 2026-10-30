# Dispatcher: append the cycle's one line to the overnight log.
line = ("- 2026-10-17 13:05 | NWCL (newcleo plc; Nasdaq NWCL, SEC CIK 0002131813, foreign private issuer with no 10-K or 20-F yet, "
        "read from the 424B3 resale prospectus of 2026-10-16 and the 6-Ks, statements in euros under IFRS; founded 2021, developing a 200 MWe "
        "lead-cooled fast reactor and MOX fuel, revenue only from engineering and pump subsidiaries bought from 2023; listed 2026-09-21 by a "
        "business combination with the SPAC NewHold Investment Corp III; rivals from the prospectus, NuScale and Oklo read, X-energy no figures, "
        "TerraPower not a filer) | v5 re-run (from scratch, one dispatched analyst) | OUT at Q1 (a start-up, ruled out by kind; the ten-year "
        "economics unforeseeable on the company's own statement recorded as concurring, which alone would have given TOO HARD (NATURE); facts "
        "recorded, not judged: going-concern doubt in the FY2025 audit report, control deficiencies, cash EUR 192.7M to EUR 66.5M in eighteen "
        "months, $74.6M of trust money prepaid to the forward counterparty, two related-party contradictions inside the prospectus; no citation "
        "slip, 16 fragments checked; position note filled, not held; framework gap for the operator: Q1's start-up OUT against its TOO HARD "
        "routing when both apply, and no definition of a start-up; the analyst declared the opening commit subjects, none used; the cycle's shell "
        "returned no output for direct runs of the acceptance test after the fold, so it was run through a wrapper script in the research folder, "
        "rc=0 PASS) | price $5.88 (aggregator, flagged) | fair none (box OUT at Q1; owner cash negative in every period, no value range or fair "
        "price computable, not armed) | PASS | 457e5f49\n")
p = 'Screens/_daily/OVERNIGHT LOG.md'
t = open(p, encoding='utf-8').read()
open(p, 'a', encoding='utf-8', newline='').write(('' if t.endswith('\n') else '\n') + line)
