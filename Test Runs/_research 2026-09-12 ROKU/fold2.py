# -*- coding: utf-8 -*-
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
t=open(p,encoding='utf-8').read()

narr = """

---

## UPDATE 2026-09-12 — ROKU: Q2 OUT, and the competitor row found the thing no single-company read could

`Test Runs/2026-09-12 Run - ROKU Roku.md`. **Q1 IN, Q2 OUT, file closed.** Price **$154.93**
(2026-09-11), **148,418,969 shares** (132,050,905 Class A + 16,368,064 Class B, 10-Q cover
accession `0001628280-26-054335`), cap **$22,996M**, sovereign **5.35%** (US Treasury, 2026-09-11).
`check_framework.py` PASS.

### THE FINDING THAT ONLY A COMPETITOR ROW COULD REACH, AND IT IS THE BEST ARGUMENT FOR [E3-28] THIS PROJECT HAS PRODUCED

**Vizio Holding Corp — the only company that ever filed the SAME metrics Roku filed — raised its
monetisation per account 71.5% over the three years in which Roku's rose 1.1%, from one fifth of
the account base.** SmartCast ARPU $21.68 (FY2021) → $28.30 → $32.48 (FY2023) → **$37.17
(Q3-2024, "up 18%")**, against Roku's $41.03 (FY2021) → **$41.49 (FY2024)**.

Every single-company reading of Roku's flat ARPU has an innocent explanation available, and Roku
supplies it: *"an increasing share of Streaming Households in international markets where we are
currently focused more on scale and engagement than monetization."* **The competitor row destroys
it.** The industry's smallest, weakest and least-scaled participant was raising its take 18% a
year in the same quarters. Flat ARPU was not an industry condition. **[E2-44]'s first
characteristic — can it raise prices *"even when product demand is flat"* — is absent at Roku and
present at Vizio, and no amount of reading Roku's own filing could have established that.**

Two more from the same row:
- **Vizio's Platform+ gross margin was 57.5% (9M-2024) against Roku's advertising-only 57.8%
  (FY2025).** Roku out-scales Vizio roughly **5:1** in platform revenue and earns the **same**
  advertising gross margin. Where a moat exists, scale shows up in price or in margin. Neither.
- **Vizio's Device gross profit crossed +$115.7M (FY2021) → −$8.6M (FY2023) — the identical
  crossing in the identical years as Roku's**, with platform at 106.1% of its total gross profit
  against Roku's 104.0%. Two independent filers, one shape, one sign flip, same years. That is
  **[E2-27]** — *"viewed collectively, the decisions neutralized each other"* — not a moat.

**And the row is going dark on both sides, which is the uncomfortable part.** Vizio stopped
filing on 2024-12-13 (Form 15-12G) and Walmart discloses **three** Vizio facts: a $1.9bn purchase
price, the goodwill's segment, and an FTC consent decree to 2037. Netflix's FY2025 10-K contains
**no membership count of any kind**. Roku deleted Streaming Households and ARPU. **Three of the
four CTV filers that once published a user series have stopped.** A method that depends on
same-metric peer rows is losing its evidence base in this sector in real time, and that is worth
more than the ROKU verdict.

### [E2-49] FIRED ON ALL THREE UNIT-AND-PRICE SERIES AT ONCE — A FIRST FOR THIS QUEUE

Three different KPM sets in three consecutive annual reports, each change following a
deteriorating reading:

| filing | the Key Performance Metrics, verbatim |
|---|---|
| 10-K FY2023 | *"gross profit, Active Accounts, Streaming Hours, and ARPU"* |
| 10-K FY2024 | *"Streaming Households, Streaming Hours, ARPU, and Free Cash Flow"* |
| 10-K FY2025 | *"Streaming Hours, Platform revenue, **Adjusted EBITDA**, and Free Cash Flow"* |

**Gross profit dropped the year after consolidated margin went 50.9% → 46.1% → 43.7%. Streaming
Households and ARPU were both deleted in FY2025 — and the FY2025 10-K carries no value for either
anywhere in the document, only the words *"more than 90 million Streaming Households globally."***
Net additions had decelerated 39% → 17% → 16% → 14% → **12%** before the series ended. Those words
are consistent with **+0.3% growth and with +9%**, so **the direction of the scarce asset —
[E4-32]'s *"primary criterion of a great business"* — is now unmeasurable from the filings.**
And there is a fourth switch nobody had looked for: *"volume of streaming players sold"* fell
**−4%, −14%, −8%** across 2021-2023 (the Precision Steel shape **[E4-55]**), and in FY2024 the
basis was widened to *"volume of **all devices shipped**"*, folding in the new Roku-made TVs and
turning the sign positive.

**The [E2-49] prior's record is now: FIRED at SHOP, MRVL, PAY, ARM, CALX, BE and ROKU; FAILED at
QLYS, CRM, CORT, PLTR and INOD. Roku is the first name where the ENTIRE unit-and-price disclosure
set went in one filing.**

### THE QUEUE-RECORD SBC NUMBER, AND THE ONE BOOLEAN THAT EXPLAINS THE WHOLE FILE

**Cumulative SBC/OCF 140.2%** — ten filed years produced **$1,378,145k** of operating cash and
paid **$1,932,508k** in stock. **First in the calibrated row by 42 points** over CALX's 98.4%.
Every multi-year window exceeds 100%. Every year resolves; the zero-SBC defect of 2026-09-12 does
not touch this name, and the trend is genuinely improving (FY2024 peak $384,662k, TTM $328,038k).

**`flags_disagree: FIRES` is the file in one boolean.** `level_shift 4.23 "STEP UP"` reproduces
exactly — mean(2023-2025) $319,206k over mean(2017-2022) $75,498k on the nine-year operating-cash
series — and `level_shift_oe` refuses the ratio. **Operating cash stepped up 4.2x and owner
earnings did not step at all, because the entire step sits inside the stock-compensation add-back.**
The PLPC run of 2026-09-07 added that flag precisely to catch a name whose two series disagree,
and Roku is its sharpest instance in the queue.

### THREE TOOLING DEFECTS, AND ONE OF THEM IS STRUCTURAL

1. **`wc_note` divides one balance-sheet delta by a single year's operating cash, so on a
   near-zero year it reports the smallest movement in the statement.** Roku's 351% — the largest
   reading in the 361-name queue — is the **`Deferred revenue`** line, **+$41,402k against
   $11,795k** of FY2022 operating cash, reproduced to the dollar; without it FY2022 operating cash
   was **−$29,607k**. It *is* customer money, but the balance has never exceeded **$149.8M, 3.2%
   of revenue**, and **56% of it is not customer float at all** — it is the portion of a device's
   price allocated to *"unspecified upgrades and updates"*, i.e. cash already collected. **The
   flag missed both larger movements in the same column: FY2022's `Content assets and liabilities,
   net` at −$313,204k (7.6x larger) and FY2023's `Accounts payable` build of +$248,175k, which was
   97.0% of that year's operating cash.** Same defect family as the near-zero denominators that
   made MU and INTC re-triage as UNPRICED. The fix is not a threshold: report the delta against
   **revenue** as well as operating cash, and flag the **largest** working-capital line rather than
   one chosen tag. **No flag reads the content-asset line at all, and at Roku that line IS the
   capital expenditure** — which is why total capex is $5,280k against D&A of $68,904k, and why
   (c) is judged with the [E5-20] exception class **reversed**: D&A is the conservative end here.
2. **`oe_bottom` and `oe_top` are two different windows again**, advertised as a spread.
   `−151` is the five-year 2021-2025 mean at the capex end; `−81` is the three-year 2023-2025 mean
   at the **same** end. Found on INTC 2026-09-07, unfixed, recurs here. The real capex band inside
   the five-year window is **$272k** wide. Rebuilt over eight windows and both (c) ends the range
   is **−$189M to +$382M — it STRADDLES ZERO**, fourteen of sixteen constructions negative.
3. **THE STRUCTURAL ONE, AND IT WILL RECUR: the screen cannot see a takeover.** **Roku signed a
   definitive merger agreement with Fox Corporation on 2026-06-14** — 0.9693 FOXA shares plus
   **$96.00 cash** per Roku share, both classes alike, Roku holders taking ~27% of the combined
   company; S-4 effective 2026-09-01, **DOJ Second Request 2026-09-08**, close expected H1 CY2027,
   termination fees $866,084,000 (Roku) and $1,237,262,000 (Fox). **At FOXA's 2026-09-11 close the
   consideration is $159.90, so the $154.93 quote is a 3.1% merger spread and not an
   owner-earnings price.** Neither the queue row nor the brief carried it, because the screen reads
   XBRL and **Item 1.01 of an 8-K has no XBRL.** **A `merger_flag()` testing for an 8-K Item 1.01
   or a DEFM14A since the last 10-K would have caught it, and the blind spot applies to every name
   in the queue that gets taken over.** This is the cheapest guard on the list and it is not built.

### AND A FOLD DEFECT IN THIS FILE ITSELF, FOUND WHILE DOING THE ROKU FOLD

**BA (Boeing) was run and folded into `WATCHLIST RUN QUEUE.md` on 2026-09-12 and has no narrative
entry here** — the exact failure the FOLD rule of 2026-09-07 was written to stop, running in the
opposite direction this time (queue entry present, reading-list entry missing, instead of the
reverse). Its queue-fold edits were also still sitting **uncommitted** in the shared working tree
when the ROKU fold began; they were committed separately under their own title (`9abe450`) rather
than swept into a ROKU-titled commit. **The count below therefore advances by two, and BA's
narrative fold is still owed by whoever holds that session.**

### THE TIER-3 TRIAGE HAS A SECOND HALF TO ITS CORRECTION

The correction of 2026-09-12 fixed the *wording* of a label that told five runs which gate to
skim. **It did not notice that four of the fifteen tier-3 names were never labelled at all** —
SWK, ARM, CALX and ROKU appear in the roster and in no sub-class. **Three of those four have now
been run and all three closed at Q2 on the business**, which is the opposite of what the labelled
classes predicted for a tier defined by arithmetic. **An unlabelled name in a labelled list reads
as "nothing here", which is the CGNX error delivered by omission rather than by wording.** SWK is
the one still live.

### WHAT WOULD REOPEN IT, AND THE STRONGEST FACT AGAINST THE VERDICT

No alert band and no `PORTFOLIO.md` row — the QLYS ruling; a Q2 failure is a failure on the
business. Four reversal conditions are in the run file, and **the first one names a document that
does not exist**: an audited Streaming Household count on the withdrawn definition, showing the
base still compounding.

**Stated as [E4-51] requires**, the best case against the OUT verdict: **advertising gross margin
expanded ~650bp year on year to 62.4% in Q2 2026 on 25% revenue growth**, faster than the US OTT
and digital ad markets, with advertising gross profit up 39%; the memory cost advantage is real
and filed (*"the Roku TV OS requires significantly less dynamic memory (DRAM) and storage memory
(Flash) than competing platforms, and this widening cost advantage is drawing more TV brands to
Roku"*); **Hisense and TCL were added as OEM partners in 2025**; and Roku's platform revenue of
$4,145M **exceeds Comcast's whole advertising line** ($3,712M, −9.2%) and is 2.8x Charter's
($1,468M, −17.6%), growing while both of theirs fall. **The verdict stands because [E3-03](2)
asks about substitutes, not about this year's margin** — and because Roku's own risk factors
concede that *"at times our existing licensed Roku TV partners have chosen to work exclusively
with, or divert a significant portion of their business with us, to other operating system
developers"*, Charter's 10-K lists Roku as one of six interchangeable surfaces (*"Xumo, Apple TV,
Roku, Vizio, LG and Samsung TV"*), and Roku ships its own channel onto Fire TV, Samsung TVs and
Google TV. **The 650bp were earned inside a category still taking share from linear television,
which is a surfing run [E3-51]; the test that separates a moat from a wave is whether the position
can be PRICED, and the Vizio comparison says it cannot.**

**Count: 73 runs** — gate-clearers 26, **Q2 OUT 44** (BA and ROKU both 2026-09-12), Q4 OUT 2,
Q1 UNKNOWABLE 1.
"""
t = t.rstrip() + narr + "\n"
open(p,'w',encoding='utf-8').write(t)
print('ok', len(t))
