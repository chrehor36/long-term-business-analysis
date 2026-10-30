# ADDENDUM 2026-10-23: the overnight runs of 2026-10-18 to 2026-10-23 audited, six marked bad

**Operator rule 6.** No run file is edited. This records the main session's audit, at the operator's "check the runs to
make sure they are valid and mark the ones that are bad", of the 23 runs logged after BESS on 2026-10-18 (BKH to NEE).
NI, running when the auto runs were stopped, is recorded at the end. The auto runs were stopped the same morning at the
operator's word (`BRK-overnight` disabled).

## How they were checked
- **Mechanical, all 23:** run file committed and clean, registered, in the done file; every ledger id resolves; every
  quoted fragment beside an id is in that row (no slip in any file); the alert follows the box (armed only for OUT at
  Q7 or IN). All pass. BEP is OUT at Q7 with no alert, correctly: neither basis gives a positive figure, and the
  regulated-utility paragraph was judged not to apply (contract and market sales).
- **By reading, four independent read-only auditors, about six runs each:** the hard sequence; the deciding part;
  Q7's basis under "The regulated utility" (2026-10-18); the fair price recomputed from each run's own inputs; Q5 facts
  checked against the filings; two or more accession numbers a run confirmed on EDGAR; the price checked against the
  close; the sovereign checked at the issuing authority; the self-audit.
- **What every run got right:** every accession checked exists for that company and form (over sixty); every close
  matches to the cent; every sovereign matches its issuing authority (Treasury 5.43% on 2026-10-16 and 5.29% on
  2026-10-22, Bank of Canada 4.19%, Bank of Korea 4.189%, PTAX 5.0826); every cover share count checked matches; every
  run's arithmetic reproduces from its own inputs within 1%. The Q5 facts behind the four integrity stops (CMS, ETR,
  FE, NEE) are real, filed and about the current management or board.

**No box changes in any run.** What is wrong in the six marked BAD is a fair price, the operator's alert figure, built
against the framework's text by more than 2%.

## The verdicts
| run | verdict | the finding |
|---|---|---|
| BKH | valid with slips | debt credit on the rise in net debt, not long-term debt raised (fair $29.45 on the gross figure, +5.1%); declared |
| BEP | valid with slips | a declared blind-rule listing; owner cash the analyst's own residual, confessed |
| **CNP** | **BAD** | owner cash changes sign, so (b) makes the range the no-growth case alone; the run averaged in a recast case (the literal window with the Beryl costs added back, mislabelled "before the draw"). Fair **$9.62** on the text, not $11.29 |
| CTRI | valid with slips | deciding part on four years of gross profit, the only filed basis; declared |
| CMS | valid with slips | Q5 facts confirmed (proxy 0000811156-26-000015, 8-K 0001104659-26-010603); parts on segment net income |
| **ELPC** | **BAD** (computation only) | OUT at Q2, so no alert; the computation's growth case charges no growth spending, against (e). All-equity fair R$2.24 a share (R$8.95 an ADS), not R$3.35 (R$13.40) |
| **ED** | **BAD** | the bottom case grows the all-spending figure, charging all spending and capping the growth it bought, which (e) forbids, with the spending kept for ever. Fair $32.01 (spending stopping at year ten, as D and DTE did) or $26.59 (spending flat for ever), not $20.24; which one waits on gap 1 below. Also `q7.py` committed with Step 0 without the operator rule 3 heading |
| D | valid with slips, ruling owed | a four-year continuing-business window (2022 to 2025), confessed; on the literal five-year base the fair price moves above 2% (gap 3); declared `Test Runs/` listing |
| DTE | valid with slips, ruling owed | a four-year window after the DT Midstream spin-off, confessed (fair $57.24 on the literal window, -3.4%; gap 3); the all-equity beside figure is the no-growth end only |
| **DUK** | **BAD** | the growth end charges no growth spending, against (e): equity-funded growth spending about $410M a year after the debt credit. Fair **$45.69**, not $47.30 (-3.4%). Also `q7.py` committed with Q3 without the operator rule 3 heading |
| EIX | valid with slips | a nine-year episode base, confessed and supported by (a); a verdict-shaped sentence under the computation heading |
| EDN | valid with slips | peso sovereign not obtained, confessed; all spending charged where the other runs took depreciation as maintenance (gap 4) |
| ENIC | valid with slips | Chilean peso sovereign not obtained (dollar functional currency since 2025, stated); declared listing |
| ETR | valid with slips | Q5 item 3 (Arkansas sales of 2003 to 2006) is before the period read and the current CEO; only the 2024 judgment is inside it, and the stop stands on the injunction and that judgment. "8-Ks that affirm" overstates (one says "affirms"). Debt credit on net borrowing ($24.27 on long-term debt); not armed |
| EVRG | valid with slips | Uri year dropped under (a), literal window shown beside |
| **ES** | **BAD** | the binding debt-share cap (50%) is PSNH's, a part that does not decide; the filing states none for the deciding part (transmission), so the paragraph's fallback (own debt share, about 65%) applies: fair about **$47.22**, not $37.58 (+26%); still OUT. Also no template commit before the fetch (operator rules 1 and 10(a)) |
| FE | valid with slips | Q5 facts confirmed (DPA, the $100M SEC penalty, the 2025 indictments, the FY2020 material weakness 0001031296-21-000020, officers and directors still serving); distribution decides narrowly once the minority interest is added back |
| FTS | valid with slips | a rate-base-weighted debt share, confessed; the alert moves about 7% either way with the reading (gap 2) |
| **HE** | **BAD** | (e) puts the maintenance-only case central where the filing allows the guess, and the run made the guess; it charged all spending instead, citing (e) for the opposite. Fair **$2.81** on its own maintenance figure, not $2.65; the two-end range that (b) would then allow was not computed |
| IDA | valid with slips | the Q7 arithmetic done before Q1 was written (rule 3 kept in substance); a duplicate template heading |
| KEP | valid with slips | Q2 declines the regulated-return exception (the allowed return not earned); under it the file reaches Q7 and closes OUT on its own computation, so the box holds at a different question; the debt credit applied to maintenance spending (gap 2) |
| MGEE | valid with slips | no separate template commit; the debt cap measured on capital spending less depreciation, immaterial |
| NEE | valid with slips | Q5 facts confirmed (derivative cash $15.5M, not "about $16M"; Ketchum in at least five captions, not three); whole-company equity-only basis although NextEra Energy Resources is unregulated (gap 5); the sum-of-parts and all-equity readings shown |

## What is done about the six
- **Alerts** (`tools/alerts.json`): CNP to $9.62, DUK to $45.69 and HE to $2.81, the figures the text gives on each
  run's own inputs, labelled as restated by this addendum. ED ($20.24) and ES ($37.58) are left at the run's figure and
  labelled FLAGGED until gaps 1 and 2 are ruled; each run's figure is below the audited one, so neither alert can fire
  late. ELPC has no alert.
- **The register** carries a dated note naming the six. None is re-run while the auto runs are stopped.

## Five gaps the audit found in the framework's text, for the operator
1. **The growth case's spending.** Specific (e) charges the growth spending against the growth it buys but does not say
   whether that spending is held flat, grows with the growth, or stops at year ten when growth stops (specific (c)
   says so for acquisitions only). The runs did all three; the fair price moves 2% to 9% between them.
2. **The utility debt credit.** Whether it is long-term debt raised gross or net borrowing; whether it offsets
   maintenance spending or growth spending only; and for a holding company with several regulators, whose allowed
   debt share caps it (the deciding part's, a rate-base weighting, or the consolidated share). The runs read all of
   these differently.
3. **The window after a spin-off or a sale of a part.** D and DTE took four-year continuing-business windows; the text
   says five years and addresses mergers, not separations.
4. **The maintenance guess where the filing gives no split.** Four runs took depreciation as maintenance, as the floor
   of the guess; EDN charged all spending.
5. **A regulated deciding part beside a large unregulated one** (NEE): the paragraph puts market-priced businesses on
   the all-equity basis but does not say how a mixed company is valued.

## NI
NI NiSource was running when the auto runs were stopped. Its cycle died after the Q7 commit (7772fea4, 08:07): the process was gone by 08:10, the cycle log is empty and the trace has no END line. The run file has Step 0 to Q7 (OUT at Q7 on the floor) but no box section, no self-audit and no fold, so it is not in the register and binds nothing (`Test Runs/README - which run files are in force.md`). It is not audited here. When the auto runs restart, the cycle's rule A resumes it from its own file. The dead cycle's lock was cleared under the lock rules (a headless holder with no live process).
