# ADDENDUM 2026-10-12 - the MTSUY brief that ran Mitsui, the dispatcher's ticker error
*Filed by the unattended overnight cycle of 2026-10-12 (the 14:46 cycle), under operator rule 6. No framework text,
template, brief or ledger row is changed here.*

## What happened
The first undone name in `Screens/_daily/_v5_rerun_order.txt` was **MTSUY**. MTSUY is the ADR of **Mitsubishi
Corporation**. The dispatching cycle searched EDGAR for "Mitsui", found Mitsui & Co.'s last 20-F (2010), fetched Mitsui's
107th Annual Securities Report, and wrote a brief that described **Mitsui & Co., Ltd. (TSE 8031)** under the ticker MTSUY.
The error was the dispatcher's: it never checked the ticker against the company before dispatch.

The analyst caught it at Step 0. On the price service MTSUY is "Mitsubishi Corporation"; Mitsui's own IR page gives
"Ticker Symbol: MITSY" and "1ADR = 20 common shares". Every other detail of the brief was Mitsui's, so the analyst ran
Mitsui, declared the error at the head of the run file, and asked the dispatcher to correct the ticker at the fold.

## What the fold did
1. **Renamed, contents unchanged.** The run was committed as `Test Runs/2026-10-12 Run - MTSUY Mitsui and Co.md` with its
   folder `Test Runs/_research 2026-10-12 MTSUY/`. Both were renamed with `git mv` to
   `Test Runs/2026-10-12 Run - MITSY Mitsui and Co.md` and `Test Runs/_research 2026-10-12 MITSY/`. The run file's text is
   unchanged except the POSITION NOTE, which the template asks the dispatcher to fill at the fold. References inside the
   run file to the old folder name are left as written; read them as the MITSY folder.
   *Why rename rather than leave the file:* the overnight prompt's section 2A treats any v5 run file named for the next
   undone ticker, with a box written, as a run waiting only for its fold. Left as it was, the next cycle would have folded
   Mitsui's run as Mitsubishi's and marked MTSUY done. A same-day Mitsubishi run would also have written into a research
   folder of the same name.
2. **Folded under MITSY** (operator rule 10(c): a received run is folded before the next dispatch). MITSY is not in the
   order file: Mitsui is not in the order file, so this is an **unordered v5 purchase run**. It
   answers the purchase question (an add is a purchase); it does not answer the keep question, which belongs to the
   holdings framework. MITSY was taken back out of `Screens/_daily/_v5_rerun_done.txt` after the fold tool wrote it, as
   the tool's own header directs for a name outside the order file.
3. **MTSUY stays owed.** It is not in the done file. The next cycle takes it as Mitsubishi Corporation.

## For the operator
- The canonical brief has no step that checks the ticker against the company (the analyst's defect (7)). The cycle prompt
  says to get the company line from a filing, and the dispatcher did; the filing it fetched was the wrong company's.
  Whether to add a ticker check is the operator's call; this cycle changes no prompt or brief.
- The fold tool retired no v4.1 band (none was active for MITSY) and armed `MITSY-v5-fair` at $65 a share of the ADR, the
  run's all-equity fair price per ADS. It is a reporting figure, not a buy signal.
