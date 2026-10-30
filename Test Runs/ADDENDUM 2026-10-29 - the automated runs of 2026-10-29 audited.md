# ADDENDUM 2026-10-29: the automated runs of 2026-10-29 audited

**Operator rule 6.** No run file is edited. This records the end-of-day audit of the runs folded today by the
unattended work-hours cycles (`BRK-audit`, written 2026-10-26 at the operator's word "Why don't we limit it to 10 runs a
day and have you audit them to verify them"). It follows the method of
`Test Runs/ADDENDUM 2026-10-23 - the overnight runs of 2026-10-18 to 2026-10-23 audited, six marked bad.md` and the
readings of `Test Runs/ADDENDUM 2026-10-28 - the automated runs of 2026-10-28 audited.md`.

**What was audited.** The nine names folded today by a cycle, each with a line in `Screens/_daily/OVERNIGHT LOG.md` and
a register entry under a `### v5 RE-RUN BATCH overnight 2026-10-29` heading: CDZI, PCYO, WATR, TURV, SCWO, AQMS, CWST,
CDTG, CHFFF. CHFFF was begun by the 12:00 cycle, stopped after Q1 by a rate limit, and resumed and folded by the 13:00
cycle; it is audited as one run. No cycle died mid-run unresumed: every run file dated today has a register entry.

## How they were checked
- **Mechanical, all nine:** every run file committed and clean; every commit touching a run file or its research folder
  touched only those two paths, except the fold commit, which touches the Screens bookkeeping files and fills the
  position note, as the FOLD requires; `python tools/check_framework.py` PASS; every ledger id in each run file resolves
  in `principle_ledger_v5.csv` (CDZI 28 ids, PCYO 33, WATR 13, TURV 17, SCWO 20, AQMS 16, CWST 34, CDTG 37, CHFFF 39, none
  missing). Every quoted fragment adjacent to an id was matched to its row by script; of the six the script did not
  pair, two are elided quotes whose pieces are each in the row (CDZI at L2010-020, PCYO at L2008-005), two are the
  framework's own heading "What it rules OUT" beside L2007-015 (SCWO, AQMS), and one is CHFFF's citation-form slip, the
  framework's words "a return set by a regulator" beside M2009-104, already recorded in the register and moving no verdict.
  The alert follows the box: all nine close OUT at Q1 (CDZI, WATR, TURV, SCWO, AQMS) or at Q2 (PCYO, CWST, CDTG, CHFFF), so
  none is armed, none is in `tools/alerts.json` and none is on the passers list, correctly. Register entry, done-file
  line and narrative line agree with each run file's box. Each position note was filled at the fold ("not held"), and
  none of the nine is in `PORTFOLIO.md`. No tracked research file over 200 KB. An untracked `_fold_msg.txt` is left in
  the TURV research folder (the cycle's commit message, as CWT and SBS on 2026-10-28); it is not committed and changes
  nothing.
- **By reading, three independent read-only auditors** (CDZI, WATR, TURV; SCWO, AQMS, PCYO; CWST, CDTG, CHFFF): the hard
  sequence; the deciding part; the STOP against the framework's text, and the TOO HARD alternative with its cause; Q7's
  basis and specifics (a) to (f) beneath the stop; every computation reproduced from the run's own script, then
  recomputed from its own inputs; accession numbers on EDGAR, and for CHFFF documents on HKEXnews; the price against
  the close; the sovereign at the issuing authority; the Q5 facts recorded after the stop against the filings; the
  self-audit against the git log.
- **What every run got right:** each STOP rests on the framework's text and on the filer's own words (the start-ups on
  "Start-ups are not our game." **[L2007-015]** and "We don't do startups." **[M2008-088]**; the Q2 stops on the
  high-cost producer, the castle shown open, or "The standing castle that protects only ordinary returns"); every
  run's script reproduces its stated figures exactly; every accession checked exists for that company and form (thirty-
  three across the eight SEC filers, including TURV's revocation order 9999999997-22-003981), and four CHFFF documents
  were found on HKEXnews (the annual report of 2026-04-23, the CEO resignation of 2026-07-17, the monthly return of
  2026-10-02, the Dongguan transaction of 2026-10-26); every price is the close of 2026-10-28 to the cent (CDZI $4.72,
  PCYO $10.65, WATR $1.47, CDTG $1.02, CHFFF HK$4.735 on 00257) or a live print of 2026-10-29 inside that day's range (SCWO
  $2.53, AQMS $1.45, CWST $89.39), and TURV's "no price" is right (registration revoked, no quote found); the sovereign is
  the Treasury 30-year par yield of 5.37% on 2026-10-28 in every dollar run, and the renminbi figures match the Ministry
  of Finance curve as served by ChinaBond (CHFFF 2.05% on 2026-10-28 from the saved page; CDTG 2.0467% on 2026-10-29,
  identical to the live curve); the Q5 facts spot-checked are in the filings (CDZI's officer pay and Heerema holding,
  WATR's related-party loan funding the buyback, TURV's revocation and the CEO's secured loans, SCWO's note repricing
  with $700,000 held by directors, AQMS's CEO pay of $1.869M, PCYO's Maran agreement, CWST's $1.9M consent-decree
  penalty, CDTG's auditor dismissed three days after the IPO, CHFFF's CEO resignation).

**No box changes in any run. No run is BAD.** No alert depends on any figure below: every box closes before Q7.

## The verdicts
| run | box | verdict | the finding |
|---|---|---|---|
| CDZI | OUT at Q1, start-up in substance | GOOD, with slips | The Mojave Groundwater Bank decides and has sold no water; the 10-K says it is not operating. TOO HARD (NATURE) weighed as the alternative, closing alike; no WORK cause. Computation reproduced (-$6.03 to -$7.82, fair -$4.33 all-equity). Under (b) a negative series makes the range the no-growth case alone, with maintenance central under (e); the run took the maintenance case as top and the all-spending case at no growth as bottom and averaged them, which (e)'s "never charge all spending and also cap the growth that spending bought" does not support. On the text: range **-$6.03**, fair **-$3.84** all-equity (-$2.79 equity-only), 12.6% from the run's. Both are not positive and no alert depends on the difference, so it is recorded as AQN was on 2026-10-28 and VST on 2026-10-27. Slips: the Kennedy units given as 600,000 where the proxy shows part cancelled; the warrant price $4.75 against $5.00 also printed |
| PCYO | OUT at Q2, ordinary returns, land development decides | GOOD, with slips | Land 62.4% of five-year segment profit, confirmed in the 10-Ks; the regulated-utility paragraph correctly judged not to apply (the 10-K: not a public utility under Colorado law; rates capped at an average of nearby providers, no allowed return). Computation reproduced ($0.10 to $3.20, fair $0.71 all-equity). Five Point's ROE divides attributable profit by equity including the minority interest: 1.8% or 4.1% on consistent bases, not 1.1%; still ordinary, box stands. Recorded: on its own segment assets the land part earns very high returns; the run rests on the field's returns and the finite parcel, as the text directs. Readings the text does not fix move the computation (growth spending uncharged in the decline case $1.08; growth on the all-spending series $0.60); no alert depends. Slips: write-early not kept (Step 0 to Q2 in one commit), declared; the after-the-stop facts lean toward weighing though each is marked "recorded only" |
| WATR | OUT at Q1, start-up | GOOD, with slips | Cost of revenue above revenue in every filed year, the US plant not operating, a going-concern paragraph, all verbatim in the F-1. Computation reproduced and equal to the text (single no-growth case, fair -$6.73 all-equity). Readings the text does not fix: cash at the as-adjusted $46.94M, -$6.43; the puttable PIK preferred left out of net debt, -$4.22; all not positive. Slips: the computation script committed with Step 0, before Q1, headed; the acceptance-test result "in the analyst's reply", in neither file nor commit; FY2023 lease principal left out, confessed |
| TURV | OUT at Q1, start-up in substance | GOOD, with slips | Operating cash negative in every year 2012 to 2018, no business that earned, the dam razed, no accounts after 2019-09-30; "start-up by earning power" a confessed reading of an undefined term. TOO HARD (WORK) rightly refused: the missing documents do not exist. Computation reproduced (fair -$0.73 all-equity); a four-year window, confessed, 2014 being incomplete (adding it makes the figure more negative). Slips: the script committed with Step 0, 30 seconds before Q1, headed; 2,665,505 shares untraced, confessed |
| SCWO | OUT at Q1, start-up in substance | GOOD, with slips | The 10-K's own words ("limited operating history with no material revenues", going-concern doubt) confirmed; the new-technology TOO HARD route weighed and not used. Computation reproduced (range -$10.75, fair -$5.81 all-equity); FY2023 intangible spending of $5,725 omitted, under 0.02%. Slips: the "committed after each" box ticked with Step 0 to the self-audit in one commit, the text beside it stating the two commits accurately; CEO pay line gives Gannon's $1,271,875 only, the interim CEO's $1,399,668 for the same year left out; the notes' added collateral left out of the Q5 facts |
| AQMS | OUT at Q1, start-up in substance | GOOD, with slips | "has not generated revenues from commercial operations" confirmed in the 10-Q; the Lion Energy termination and the loan confirmed; the TOO HARD alternative weighed. Computation reproduced (range -$77.95, fair -$41.26 all-equity); stock issued for services 2022 to 2024 omitted, about 0.2%. Slips: the computation script and output committed with Step 0, before Q1, headed but not stated in the self-audit; revenue "since 2019" at one line against "since 2021" at two others |
| CWST | OUT at Q2, the high-cost operator | GOOD, with slips | Western region 58% of positive segment income, confirmed; the Ontario closure and the Dalton sentence confirmed in the 10-K. "Below each rival in every year but one" holds on operating margin (the exception Waste Connections in 2020); it does not hold on return on tangible assets, where Casella beat Waste Connections in 2016 and 2020; "about half or less" of the two largest rivals' margins is loose (56% to 59% in some years). The box rests on the margins and the closing landfill and stands. Computation reproduced (range $3.25 to $20.33, fair -$4.10 all-equity, $10.29 equity-only); serial acquirer on the organic pair, correctly; the federal-only tax rate a confessed convention. Slips: `q7.py` committed with Q1, headed but already saying "the file closed at Q2" two minutes before Q2, not confessed; Q2 cites the computation in dismissing the TOO HARD reading ("The box would not change at the price on either reading"), though its own reasons carry the OUT; the acceptance-test result "recorded in the reply" |
| CDTG | OUT at Q2, the castle open on the filer's own evidence | GOOD, with slips | Sewage systems 93% of five-year gross profit (no operating profit by line, said so); collection 99.3% to 3.1%, "Our suppliers have the ability to manufacture", the copy risk, all confirmed in the 20-F. Computation reproduced (value -$45.61, fair -$9.27 all-equity), (b) applied correctly. Q1 passed narrowly although the 20-F states its structure two ways; a reader could close it TOO HARD at Q1, no box consequence. Slips: `scripts/arith.py` and its output, already printing the fair price, committed with Q1 before Q2 **without the operator rule 3 heading, unconfessed**; the curve dated 2026-10-29 against the 2026-10-28 close |
| CHFFF | OUT at Q2, a castle that protects only ordinary returns | GOOD, with slips | Environmental energy 70.4% of five-year segment profit, reproduced; ROE of 5% to 7% in the operating years for this company and its listed rival, and 5.7% on the energy segment's assets, reproduced. The regulated-return exception weighed correctly: the fees are tendered and the tariff set nationally, no regulator allows a return on invested capital (as CWCO on 2026-10-28). Computation reproduced (value HK$-17.54, fair HK$-16.89 all-equity), (b) right on a sign change. Readings the text does not fix (perpetuals and minorities out, HK$-13.45; no tax shield centrally, about HK$-18.1); all not positive. The resume is clean: between the 12:00 cycle's Q1 and the end, the only committed lines changed are the sovereign line and a placeholder, both declared. Slips: the fallback "Even read as a regulated return..." misstates the exception (if it applied the file would go to Q3 as a weighing, not close at Q2), so it cannot support the OUT, which stands on the main reading; the M2009-104 form slip, recorded; Q2 to the self-audit in one commit, confessed; the claim that a half-tick "would not print" looks wrong, harmless |

## What was done
- **`tools/alerts.json`:** unchanged. None of the nine is armed, correctly, and no figure above can arm one.
- **Bookkeeping:** none needed. The register, done file, narrative and passers list agree with each run file.
- Nothing about the framework, the template, the briefs or the prompts was changed.

## Gaps and recurring slips, for the operator
1. **"Start-up" is undefined in Q1** (by age, by the deciding part's revenue, or by earning power): every one of the five
   Q1 stops read it differently, and none is against the text. With it, no rule for a name that is both a start-up (OUT)
   and a new technology (TOO HARD) (SCWO, AQMS).
2. **(b) with (e) when the range is the no-growth case alone:** the text does not say outright that the all-spending case
   drops out as a range end. CDZI's 12.6% comes from here.
3. **No wording or alert rule for a fair price that is not positive**, raised again by every run today (gap 10 of
   2026-10-28).
4. **The computation script committed before the questions ahead of Q7 close:** in seven of the nine runs today; headed in
   six, unheaded and unconfessed in CDTG. Gap 1 of 2026-10-27 and 2026-10-28, now in every cycle run of four days.
5. **No CNY row in the protocol's sovereign table**, and whether ChinaBond's service of the Ministry of Finance curve is
   the issuing authority (CDTG, CHFFF).
6. **Whether the regulated-return exception at Q2 needs an allowed return on capital or only a price set by a
   regulator**, and what follows when the guarantor is in arrears (CHFFF).
7. **The "ordinary returns" item is silent on one weak player among strong ones** (CWST), and on which return is judged,
   reported equity returns or cash (CDTG).
8. **Preferred stock in net debt** (CDZI, WATR); **IFRS 16 leases on the all-equity basis** (WATR); **a window under five
   years** (WATR, TURV); **a revoked or dark registrant** (TURV); **the business of parts when total operating profit is
   negative** (CDZI) or for an integrated business whose inventory runs out inside ten years (PCYO); **a related-party
   loan book inside operating cash** (PCYO); **(e) at a negative growth rate**, and growth measured on the maintenance or
   the all-spending series (PCYO).
9. **Part VII's research-pass paragraph says a file is re-looked under an alert "like any OUT"**, while the FOLD and the
   passers list arm only names that close OUT at Q7 or IN. Practice and text should be reconciled.
10. **The acceptance-test result "recorded in the reply"** (WATR, CWST), in neither the file nor the commit, as GWRS on
    2026-10-28.
