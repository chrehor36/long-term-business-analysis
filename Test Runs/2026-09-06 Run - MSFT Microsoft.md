# Company Run — MICROSOFT CORPORATION (MSFT) — 2026-09-06
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24 %** · date **2026-09-04** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year, fetched direct from home.treasury.gov 2026-09-06. Struck fresh, not
  carried from another run.** (20-yr 5.25%, 10-yr 4.78% on the same date.)
- FX: **none — USD is both the quote currency and the earnings currency.** MSFT reports in
  USD; no ADR.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2026 Form 10-K, fiscal year ended 2026-06-30, filed
  2026-07-29, accession 0001193125-26-323660** (primary doc `msft-20260630.htm`). Eight
  further 10-K vintages read for the series: FY2025 `0000950170-25-100235`, FY2024
  `0000950170-24-087843`, FY2023 `0000950170-23-035122`, FY2022 `0001564590-22-026876`,
  FY2021 `0001564590-21-039151`, FY2020 `0001564590-20-034944`, FY2019
  `0001564590-19-027952`, FY2017 `0001564590-17-014900`, FY2014 `0001193125-14-289961`.
  Proxy: DEF 14A filed 2025-10-21, `0001193125-25-245150`.
- figure cross-checked against the filed statement (say which): **"Additions to property and
  equipment" FY2024 = $(44,477)M appears identically in the FY2024 10-K and the FY2026 10-K
  cash-flow statements. Also cross-checked: FY2017 OCF $39,507M (FY2017 and FY2019
  vintages); FY2018 OCF $43,884M and FY2019 OCF $52,185M (FY2019 and FY2020 vintages). All
  four checks returned identical figures.**
- **Share count, hand-read off the FY2026 10-K cover:** *"As of July 23, 2026, there were
  7,425,545,491 shares of common stock outstanding."* **Single class of common stock; no
  super-voting stock.** (Guard run: no stock split in the window — the last MSFT split was
  2003; diluted weighted-average 7,453M in the same filing is consistent with the cover.)
- **Price $499.70, 2026-09-04 close, Yahoo Finance — AGGREGATOR, FLAGGED, live quote only
  per operator rule 5.** Market cap = 7,425,545,491 × $499.70 = **$3,710,545M**.
  *(The screens carry $3,811,904M on an earlier price; the hand cap governs.)*
- **Stage 0 by hand, done:** cover count read (above); single share class confirmed;
  earnings currency USD confirmed (US 10-K filer, USD reporting, no translation);
  no ADR ratio to derive.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** Microsoft sells three
  different things and they are not the same business.
  **(1) The annuity.** It rents software that people use to do their jobs — the word
  processor, the spreadsheet, the email server, the corporate directory. It is sold by the
  seat, per month, on a subscription that renews by default, to a company whose staff have
  all already learned it and whose files are all already in it. The marginal cost of the
  next seat is close to zero, so nearly every additional dollar of price is a dollar of
  profit. Nobody at the customer decides each month whether to keep paying; not paying means
  retraining everyone.
  **(2) The rental yard.** It buys land, builds sheds, fills them with computers bought at
  enormous cost, and rents the computers out by the hour. The customer's data, once loaded
  in, is expensive to move out. The machines wear out and become obsolete on a schedule
  Microsoft itself estimates, and the whole economics of the leg turn on whether that
  estimate is right.
  **(3) The remainder.** It takes a fee from PC makers for the operating system, sells a
  games console and games, and sells search advertising. This leg is shrinking as a share of
  the whole and is not why anyone owns the stock.
  In FY2026 the three together produced **$331,839M of revenue and $155,237M of operating
  income — a 46.8% operating margin** (FY2026 10-K income statement). That margin is the
  most remarkable number in the file and it is the annuity's, not the rental yard's.
- **The scarce input this business controls:** the **installed habit** — the file formats,
  the corporate identity directory, and the fact that the work of the world is already done
  in these applications. Nobody can manufacture that; it took forty years and it cannot be
  bought. Note what is NOT scarce and NOT controlled: the datacentre inputs. Land, power,
  buildings and — decisively — **GPUs are bought in a market where one supplier prices
  them**, and Microsoft's three largest cloud rivals are bidding for the same units. The
  first leg controls its scarce input. The second leg is a buyer in a seller's market.
- **Will the fundamentals look broadly the same in ten years?** **The two legs answer
  differently, and this is the honest statement of the file.** The annuity: yes — Excel and
  the corporate directory in 2036 look like Excel and the corporate directory today, and
  this is as safe a ten-year statement as anything in the corpus. The rental yard: I do not
  know, and neither does the filing. What I can nonetheless understand is the **structure**
  of the second leg — capital in, depreciation out, hours rented — which is what [E3-31]
  asks for. I am not required to predict the AI outcome to pass Q1; I am required to
  understand how the money is made. I do.
  **What I am NOT permitted to do is let that understanding pass for certainty about the
  cash flows.** [E3-31]: *"If a business is complex or subject to constant change, we're not
  smart enough to predict future cash flows."* The uncertainty is real and it is priced
  where the framework says it is priced — at the understanding gate and in the end discount
  **[E3-42]**, never in the rate — and it reappears below as Q4's band.
- **VERDICT: [x] IN**
  *Both legs are understood as businesses. The second leg's OUTCOME is uncertain; that is a
  Q4 range question and a Q5 price question, not a Q1 comprehension failure. Recorded
  honestly: this is the least comfortable Q1 IN in the queue's history, and if the run had
  to name where it is most likely wrong, it is here.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**JUDGED BY SEGMENT [E5-37]** — *"different numbers are of different importance … depending
on the kind of business; there is not one-size-fits-all."* This is three businesses and they
do not get one answer. Segment figures are the FY2025/FY2026 vintages (post-recast, so
comparable); margins are my computation from two filed figures.

| segment | FY2026 revenue | FY2026 OI | margin | margin FY2018 → FY2026 | class |
|---|---|---|---|---|---|
| **Productivity & Business Processes** (Office/M365, LinkedIn, Dynamics) | 139,996 | 83,879 | **59.9%** | 36.0% → 59.9% ▲▲ | **WIDE** |
| **Intelligent Cloud** (Azure, server products) | 137,791 | 56,972 | 41.3% | 35.8% → 41.3%, but **43.2% → 41.3% since FY2024** ▼ | **NARROW** |
| **More Personal Computing** (Windows, Xbox, devices, search) | 54,052 | 14,386 | 26.6% | 25.1% → 26.6%, revenue **DOWN** FY2025→26 | **NARROW / NONE** |

- **Needed or desired [x]** — overwhelmingly, all three legs.
- **No close substitute — [x] for Productivity, [ ] FAILS for Intelligent Cloud.** And it
  fails **on the subject's own words**, FY2026 10-K Item 1: *"Azure faces diverse competition
  from cloud service providers and open-source offerings … Our AI offerings compete with AI
  products from hyperscalers, as well as products from other emerging competitors and other
  open-source offerings, many of which are also current or potential partners."* Intelligent
  Cloud is **41.5% of revenue and 55% of the FY2024→FY2026 revenue increase.**
  *(Recorded sweep: **Microsoft names ZERO competitors by company name** anywhere in its
  Competition sections, in any vintage — competitors are described only by category. Contrast
  Garmin's 34 named substitutes. This is neither a franchise proof nor a concession; it means
  the row below had to be built entirely from the peers' own filings.)*
- **Not price-regulated [x]** (antitrust exposure is a different thing and is read at Q4).
- **Must the moat be continuously rebuilt? [E4-04] — THE TWO LEGS SPLIT, AND THIS IS THE
  CENTRAL Q2 FINDING.** The Office moat is **defended, not replaced** — [E5-23]/[E3-49]'s
  permitted class; a year of under-spending narrows it, it does not destroy the file formats
  or the corporate directory. The Azure/AI moat's **basis must be periodically replaced**:
  GPU generations turn over, and the frontier moves. That is [E4-04]'s **excluded** class,
  and its mechanism has the corpus's name — **competitive destruction** — with [E3-51]'s
  surfing test live: *"when a surfer gets up and catches the wave … he can go a long, long
  time. But if he gets off the wave, he becomes mired in shallows."* Of [E4-36]'s four causes
  of extreme success, Productivity is an ownable one (extreme max on one variable — switching
  cost); the AI leg's recent record is substantially **wave-riding**, and the advantage in a
  wave lives in the wave.
- **Does success depend on a great manager? No** — and this is genuinely to the business's
  credit. Nobody needs to know who runs Microsoft for Excel to keep renewing. **[E4-23]** is
  not fired at Productivity. *(It is fired in a narrow way at the cloud leg: the capital-
  allocation judgment IS the plan there. Recorded, and carried to Q3.)*
- **[E2-44] the two-characteristic test — SPLIT, and the split is the file.**
  **(1) PASSES, on the one filed decomposition that exists.** FY2025 10-K, verbatim:
  *"Microsoft 365 Consumer cloud revenue grew 11% driven by **Microsoft 365 Consumer
  subscriber growth of 8% to 89.0 million**, as well as growth in revenue per user **from the
  price increase announced in January 2025**."* **The 2025 Copilot-bundled consumer price
  rise went through and seats GREW — 82M → 89.0M.** That is [E2-44](1) demonstrated and
  [E4-37]'s inverse metric at the yawn end, not the *"prayer session"* end.
  **(2) FAILS, hard.** *"grow dollar volume with only minor additional investment of
  capital"* — **capex has gone 6.4% → 34.9% of revenue in eleven years**, and 42% including
  finance leases. Whatever this is, it is not capital-light growth.
- **Primary moat metric and its trend — TWO, pointing opposite ways.**
  **Widening:** PBP operating margin **36.0% (FY2018) → 59.9% (FY2026)**, up in eight
  consecutive years. **[E4-32]**'s *"primary criterion of a great business."*
  **Narrowing:** Intelligent Cloud **gross** margin **66.1% → 62.2% → 58.0%** (FY2024-26,
  from the segment cost-of-revenue disclosure that first appears in the FY2025 vintage), with
  IC cost of revenue **+44.1%** against segment revenue **+29.7%** in FY2026. Consolidated
  gross margin has fallen three straight years, **69.8% → 68.8% → 67.9%.**

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. THE HEADLINE ABSENCE FINDING OF THIS RUN.**
Recorded sweep: **eleven consecutive 10-K vintages, FY2016-FY2026**, searched for every
physical/unit series (seats, subscribers, members, MAU/DAU, consoles, devices, customers,
bookings, installed base).
**As of the FY2026 10-K, Microsoft files NO unit series for ANY segment. Eight of the ten
unit series it has ever filed have been withdrawn.**
- **"Commercial bookings": ZERO hits in every vintage.** Also bare "bookings": zero.
- **Azure dollar revenue is NEVER FILED — in eleven consecutive 10-Ks.** A growth rate only:
  113/99/91/72/56/50/45/29/30/34/41%. *(Every `Azure` occurrence was tested for a dollar
  figure within ±160 characters and hand-inspected.)* **The single most important revenue
  line in the company has no filed level, ever**, and its definition silently changed in
  FY2022 (absorbing Nuance) with no restated prior rate.
- **No paid-seat COUNT in any year** — the commercial metric is titled "seat *growth*":
  17/14/11/7/6/6%, decelerating, with no level behind it.
- **No Copilot seat, user, or revenue figure has ever been filed.**
- **What IS filed:** RPO, and **Microsoft 365 Consumer subscribers** — the one real unit
  count: 23.1M → 89.0M (FY2016-FY2025), growth 23/22/15/12/10/8%. **Removed as a metric in
  FY2026, after printing 8%.**
- **RPO, and it is two-sided:** $73bn (FY2018, created by ASC 606) → **$684bn (FY2026,
  commercial $678bn)**, +84% against revenue +18%. **But the share recognising within twelve
  months has HALVED: 60% → 50% → 45% → 40% → 30%**, and FY2026 is the first vintage ever to
  disclose a weighted-average duration (2.3 years). A backlog growing four times faster than
  revenue while converting at half the old rate is a lengthening contract book, not a
  straightforwardly bullish number — **and the row shows Oracle's doing exactly the same
  thing** ($638bn RPO, next-12-months share falling 33% → 12%).

### **[E2-49] METRIC-SWITCHING — IT FIRES, AND THE PATTERN IS OLD**
*"Yardsticks seldom are discarded while yielding favorable readings."* Dated to the vintage:
- **FY2017: five unit metrics withdrawn at once, silently** — Xbox Live MAU, Windows 10
  devices, EMS customers, console units, Dynamics seat adds. **The console series went the
  vintage after volume declined** (12.1M → 11.7M).
- **FY2023:** Surface revenue metric dropped silently, in the year Devices revenue fell 24%.
- **FY2024:** LinkedIn members dropped silently (had run 700M/750M/850M/950M). In the same
  vintage the M365 Consumer subscriber definition was **widened** to include Basic and Copilot
  Pro, on a decelerating count, **with no restated prior year**.
- **FY2026: "Microsoft 365 Consumer subscribers was removed as a metric."** The growth rate
  (7%) survives in MD&A; the level does not.
**The candour cases are on the record too and are not small** [E2-26]: ASC 606 restated fully
retrospectively (FY2018), the Metrics section created (FY2020), the Q1-FY2022 and Q1-FY2024
changes announced ahead with reasons, the FY2025 segment recast quoted and dual-filed, and
the FY2026 first-ever RPO duration disclosure. **The verdict is not "dishonest." It is that
the yardsticks that survive are the ones still reading well, which is exactly what [E2-49]
says to expect, and it leaves a moat claim that cannot be monitored on units.**

**THE COMPETITOR ROW — required [E3-28].** Built from the peers' own 10-Ks; 28 filings read.
Same metrics, same latest fiscal year, filing-sourced.

| Company | capex ÷ D&A | capex ÷ revenue | owner earnings, capex end ($M) | owner earnings, D&A end ($M) | cloud segment margin | server life today | reversed? | source |
|---|---|---|---|---|---|---|---|---|
| **MSFT** (FY2026) | **3.38x** (3.01x on the D&A line; **≈4.1x incl. finance leases**) | **34.9%** (≈42% incl. leases) | **54,582** | 131,996 | **IC 41.3%** | **6 yr** | No | FY2026 10-K `0001193125-26-323660` |
| GOOGL (FY2025) | 4.33x | 22.7% | 48,313 | 118,624 | Google Cloud **23.7%** | 6 yr | No | 10-K |
| AMZN (FY2025) | 3.15x | 18.4% | **(11,772)** | 78,187 | AWS **35.4%** | 5–6 yr | **YES** | 10-K |
| ORCL (FY2026) | **7.30x** | **82.6%** | **(28,497)** | 19,543 | **no cloud segment exists** | 6 yr | No | 10-K |

- **Peers named: 3 of the 3 hyperscale competitors that file with the SEC.** AAPL excluded —
  running in parallel, not a cloud competitor. **The material omissions, stated not
  stretched:** Alibaba Cloud, Tencent Cloud and CoreWeave-class neoclouds are not in the row;
  and **no filer discloses a productivity-suite segment comparable to PBP** — Alphabet does
  not break out Workspace. **So the row evidences the CLOUD leg's relative position and
  cannot evidence the ANNUITY's.** The annuity's moat is carried on single-company evidence
  (margin, the absorbed price increase, switching cost), which [E3-03]/[E3-43] permits but
  which the row does not corroborate. Recorded as the row's limit **[E3-61]**.
- **WHAT THE ROW ACTUALLY SHOWS, and it is not what the brief expected:**
  1. **Microsoft is the best of the four**, decisively. It has the highest capex-end owner
     earnings ($54.6bn against Alphabet's $48.3bn and two negatives), the highest cloud
     segment margin, and the lowest capex/revenue except Amazon.
  2. **The disease is industry-wide, not company-specific.** All four extended server lives
     to six years within thirty months of each other. **Alphabet's capex-end owner earnings
     are FLAT since 2021 (51,636 → 48,313) while its D&A end nearly doubled — "the whole
     apparent growth lives in the gap."** Oracle spends **82.6% of revenue** on capex at
     **7.3x depreciation**, funded with debt up $37bn in one year.
  3. **[E2-27] is the row's verdict.** *"Viewed individually, each company's capital
     investment decision appeared cost-effective and rational; viewed collectively, the
     decisions neutralized each other."* Four companies, the same capacity, the same
     workloads, the same eighteen months.
- **THE SINGLE MOST IMPORTANT FACT THE ROW PRODUCED — and it is evidence AGAINST Microsoft:**
  **Microsoft was FIRST to six years** (July 2022 — six months ahead of Alphabet, eighteen
  ahead of Amazon, two years ahead of Oracle) **and travelled furthest, from the shortest
  base (2–3 years).** And **Amazon is the only one that has REVERSED**: effective January
  2025 it shortened a subset of servers from six years back to five, **+$1.4bn of D&A,
  −$1.0bn of net income, "primarily impacted our AWS segment"**, plus **$920M of accelerated
  depreciation for early retirements** — guiding −$0.7bn and realising double that. Amazon's
  filed reason is the one that matters: **"the increased pace of technology development,
  particularly in the area of artificial intelligence and machine learning."**
  **The operator of the largest cloud fleet on earth looked inside it and concluded six years
  is wrong. Microsoft, Alphabet and Oracle have not re-tested.** *(And AWS's margin jump to
  37.0% in FY2024 is attributed by Amazon's own filing to its 5→6 extension — the cleanest
  demonstration in the row of what these changes do to a reported segment margin.)*
- **Untapped pricing power [E3-33]/[E5-28]: NO, and the class is not claimed.** The corpus
  scopes the class to *"a monopoly or a near monopoly"*, and it requires that a manager
  *"could raise the return enormously just by raising prices, and yet they haven't done it."*
  **Microsoft HAS done it** — January 2025, consumer M365, absorbed with seats growing. The
  power is real and it is being **used**, which is a franchise finding but disqualifies the
  untapped class. No commercial M365 price increase is named in any filing, and **no Azure
  pricing statement exists in any vintage** — so the commercial half is not evidenced either
  way.
- **Class: [x] NARROW** · **Direction: MIXED — widening at Productivity, narrowing at
  Intelligent Cloud, and the capital is going into the narrowing one.**
- **VERDICT: [x] IN**

**THE BRIEF'S PREDICTION WAS "IN WIDE" AND IT IS HALF INVERTED, WHICH IS THE HONEST RESULT.**
The brief expected Office/Windows switching costs to carry a WIDE class, and *for
Productivity alone they do* — a 59.9% operating margin rising for eight straight years, with
a price increase absorbed on growing seats, is as strong a single-segment franchise as this
queue has recorded. **But Microsoft is no longer only that business.** Intelligent Cloud is
41.5% of revenue, 55% of the recent revenue increase, and the destination of essentially all
of a $116bn annual capital budget; it fails [E3-03](2) on the subject's own words, sits in
[E4-04]'s excluded class on the replacement test, and has a **falling** gross margin. A moat
class is a claim about the business that exists, not the half one prefers.
**NARROW, not WIDE — and the run notes that this is the first time in the queue that a
segment-level WIDE has been overridden by the composition of the business around it.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — **ARGUED AT LENGTH AND REFUSED.** The case FOR ticking it: a
  $116bn annual capital budget is a decision that must be made well repeatedly, and
  [E2-70]'s magnifier applies where the product is undifferentiated — which Azure compute
  substantially is. The case AGAINST, which wins: [E3-38]/[E3-43] is about whether the
  *business* can be killed by poor management, and the natural experiment is on the record —
  Microsoft spent the decade to 2014 losing the phone market outright, wrote off $7.6bn of
  Nokia, missed search, and **Office and Windows renewed anyway.** That is [E5-18]
  (*"the capacity to stand it"*) and [E2-53] (*"Good or bad, it will prosper"*) demonstrated
  over ten years. The annuity does not require daily brilliance. **NOT TICKED.**
- [ ] **Control** — marketable security, exit available at any time. **NOT TICKED. [E1-16]**
- [ ] **Leverage** — bonded debt $46,136M plus finance-lease liabilities $66,594M
  = ~$112,730M against **$442,387M of equity and $758,376M of assets.** Nothing like
  [E3-29]'s 20:1. **NOT TICKED.**

**NONE TICKED → Q3 IS A QUALITATIVE OVERLAY.** Manager quality alone does not stop this run,
and — the half that matters more here — **it cannot promote the name either.**
*Declared before the findings below were written, per operator rule 9's pre-registration.*

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* **NO DISQUALIFIER FOUND.**
**No 10-K/A has ever been filed. No restatement in the eleven-vintage window. Deloitte &
Touche LLP throughout, non-audit fees 6.5% of the total. Single class of common stock, one
vote per share, no super-voting stock.** The one large unresolved matter is a tax dispute,
not a conduct matter, and is treated below. *(Dated to public filing: the $28.9bn IRS Notices
of Proposed Adjustment became public in a filing in FY2023 and remain unresolved.)*
**Written as the framework requires [E5-17]: this is the absence of found disqualifiers, not
a finding that the managers are honest.**

**STEP 2 — THE FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.* **Recorded sweeps, eleven 10-K vintages + five
proxies, with counts.**
- [ ] weak accounting — **NOT FIRED.** SBC expensed in full ($12,405M). No pension
  assumptions of consequence. **No 10-K/A ever filed** in the EDGAR history 1994-2026.
- [ ] unintelligible footnotes — **NOT FIRED.** The footnotes are unusually plain.
- [ ] trumpeted earnings projections / growth targets — **NOT FIRED, AND THIS IS A REAL
  PASS.** *"guidance"* appears 9 times in the FY2026 10-K and **every one means FASB, security
  or OECD guidance**; *"outlook"* 3 times, including Outlook.com. **No revenue, EPS or margin
  target appears in any filing.** [E5-30]'s ratchet is absent from the filed record.
  *(Honest limit, and it is the same hole the GRMN run left open: **earnings-call guidance was
  not swept** — it is not in a filing, so [E3-48]'s outturn test is UNMEASURED, not passed.)*
- [ ] serial share issuance — **NOT FIRED.** Count fell 7,808M (FY2016) → 7,427M (FY2026).
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — SCOPED, AND MOSTLY A PASS.**
  **"EBITDA" appears ZERO times in all eleven 10-Ks FY2016-FY2026 and ZERO times in the 2025
  proxy.** "Restructuring": 75 (FY2016) → **zero from FY2021 on**. "Constant currency" zero in
  both — though the proxy substitutes **"constant dollar"** twice, the same adjustment under
  another name, so that particular zero is not a clean pass. Non-GAAP use is episodic and
  each time tied to a named one-off. **What DOES fire: FY2026 introduces a new "Adjusted net
  income" excluding the OpenAI marks — and it runs in the HONEST direction, cutting headline
  growth from 31% to 22%.** Recorded as new, flagged for re-sweep, not charged.
- [x] **filed-figure tells [E4-30] — CASH-TAX TELL FIRES AND IS ACQUITTED.** FY2026 cash
  taxes **fell 26%** ($28.7bn → $21.2bn) while pretax income rose 34%; the underlying rate
  roughly halved to ~10.1% ex-transition-tax, and the new ASU 2023-09 jurisdiction table
  shows **U.S. federal cash tax of just $6,246M on $103.6bn of U.S. pretax income (6.0%) —
  less than the $6,495M paid to Ireland.** **The filing explains it, in Note 11's deferred-tax
  table**: the depreciation DTL tripled ($5,699M → $17,675M) and leasing added $8,778M, with
  net deferred tax assets down **$14.2bn**. It is **timing on the AI build and it reverses.**
  Acquitted as a fraud tell; **carried into Q4 as a judgment about the tax rate.**
  Reported growth is **not** unnaturally smooth (net income fell in FY2018 and FY2023).
- [x] **[E2-49] METRIC-SWITCHING — FIRES, AND IT IS THE STRONGEST FLAG IN THE FILE.** Fully
  evidenced at Q2: five unit metrics withdrawn silently in FY2017 (the console series the
  vintage after volume fell); Surface dropped FY2023; LinkedIn members dropped FY2024;
  **M365 Consumer subscribers — the last real unit count — removed in FY2026 after printing
  8%.** And the same pattern inside the depreciation disclosure: **the dollar effect of the
  life extensions was given for the first year only, stripped of dollars in FY2024, and the
  "Change in Accounting Estimate" heading disappears entirely in FY2025 and FY2026.**
  *"Yardsticks seldom are discarded while yielding favorable readings."*

**STEP 3 — THE PRIMARY TEST [E2-01].** Multi-year, balance sheet before income statement.
- **ROE, FY2016-FY2026:** 24.7 / 29.1 / 20.0 / 38.3 / 37.4 / 43.2 / **43.7** / 35.1 / 32.8 /
  29.6 / **30.2 %** — **eleven-year mean 33.1%, above 20% in every single year.**
- **[E2-43] on the unleveraged tangible denominator**, required here because goodwill and
  intangibles went $21.6bn → $138.3bn on LinkedIn, Nuance and Activision: **return on
  tangible equity 33.4 / 60.0 / 42.5 / 74.7 / 65.2 / 72.5 / 82.9 / 56.1 / 72.4 / 50.6 /
  44.0 %, eleven-year mean 59.5%.** The goodwill wedge is reported separately, not hidden.
  **The operating business earns extraordinary returns on tangible capital.** This is as
  emphatic an [E2-01] pass as the queue has recorded.
- **AND THE TREND IS THE FINDING: both series have roughly HALVED since FY2022** — ROE 43.7%
  → 30.2%, ROTE 82.9% → 44.0%. Equity grew **+166%** ($166.5bn → $442.4bn) while net income
  grew **+84%**. **Incremental return on the last four years' retained capital is ~22% — half
  the average.** [E2-56] again: the average is the old business, the increment is the new one.

**The half-owner test [E2-26]: MIXED, and both halves are large.**
**FOR:** ASC 606 restated fully retrospectively; the FY2025 segment recast filed in BOTH
presentations; RPO weighted-average duration disclosed for the first time in FY2026; the new
adjusted measure cuts reported growth rather than flattering it; the **$24.1bn of related-party
OpenAI revenue disclosed at a granularity nothing compelled**; the Note 15 buyback table
**separating employee tax-withholding settlement ($5.6bn) from the repurchase program** — a
one-time item quantified separately at every line, which is the standard met.
**AGAINST:** no Azure revenue level in eleven years; no seat count ever; no capex category
split; no construction-in-progress; **no PP&E rollforward**; the life-extension dollar effect
withdrawn; the OpenAI exclusivity sentences deleted without comment. **The reporting is candid
about what it discloses and silent about the things that would let an outsider check the
capital decision.**

**The institutional imperative — score all four [E2-30].** *"Institutional dynamics, not
venality or stupidity."*
- [ ] resists any change in current direction — **NO.** This management reversed course on
  phones, on search, on Windows-first. Not fired.
- [x] **projects/acquisitions materialise to soak up available funds — FIRES.** Capex went
  6.4% → 34.9% of revenue in eleven years, and **Activision cost $75.4bn for a business the
  company's own ASC 805 pro forma shows adding $172M — 0.2% — to FY2024 net income**, with an
  operating **loss** of $(1,362)M in its stub period. 97% of the price went to goodwill and
  intangibles.
- [ ] staff studies to justify the leader's craving — **not establishable from filings.**
- [x] **peer behaviour mindlessly imitated — FIRES, and the competitor row is the evidence.**
  Four hyperscalers extended server lives to six years within thirty months of each other,
  and all four are building the same capacity for the same workloads at the same time.
  **[E2-27] by name.**

**Capital allocation — the buyback conditions [E5-08, E4-31]:**
- **(1) ample funds for operations and liquidity? QUALIFIED YES** — but see Q4: liquidity has
  **fallen 31%** ($111.3bn FY2023 → $76.8bn FY2026) while twelve-month contractual obligations
  went **$59.4bn → $241.9bn**. Condition 1 is passing on the size of the cash flow, not on the
  size of the balance sheet.
- **(2) repurchases at a material discount to conservatively calculated IV? FAILS.**
  Average price paid, program only: FY2020 **$156.25** · FY2021 $227.43 · FY2022 $295.08 ·
  FY2023 $266.67 · FY2024 $373.75 · FY2025 $419.35 · **FY2026 $464.42**, with **$40.6bn still
  authorized.** Against this run's judged zero-growth value of **~$115/share**, FY2026
  repurchases were made at **roughly 4x**. **→ CAPITAL ALLOCATION FLAG.**
  **Stated with the humility clause [E4-13]:** this rests entirely on our own IV range, and
  *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole
  lot more about them than I do"*; *"many CEOs never stop believing their stock is cheap"*
  **[E5-08]**. **It binds position size, never the discount rate.**
  **And the evidence that cuts the other way, stated [E4-26]:** the buyback **shrank as the
  price rose** — 126M shares at $156 in FY2020 falling to 31-36M shares at $419-464 — which is
  [E5-24]'s *"what is smart at one price is dumb at another"* being at least partly obeyed.
  Shareholder return fell from **79% to 32% of earnings** as the price rose and the capital
  budget grew. **What the buyback does NOT do is reduce the share count: 7,432 / 7,434 /
  7,434 / 7,427 over four years despite $41.7bn of program repurchase — it funds SBC dilution.**
- **[E2-52] dividends funded by issuance: DOES NOT FIRE, cleanly.** Dividends paid exceed
  proceeds from stock issuance by roughly **12x every year**. Payout ratio **fell 56.2% →
  20.3%**. **RPM decomposition PASSES: ten consecutive annual DPS increases, verifiable from
  the filings, with the payout ratio falling throughout — i.e. earnings-driven, not
  ratchet-driven.** And a candour point in the company's favour, against three prior names in
  this queue: **"consecutive" returns ZERO hits in the FY2026 10-K** and one in the proxy —
  **Microsoft does not boast of the streak it actually has.**
- **[E2-60] restricted earnings: DOES NOT FIRE.** Equity rose $343.5bn → $442.4bn in the year
  $43.2bn was returned. Leverage did not rise to fund the payout.

**PAY VERSUS PERFORMANCE (2025 DEF 14A, Item 402(v)) — the sharpest [E2-30] evidence.**
- **The company-selected measure is "Microsoft Incentive Plan Revenue" — explicitly non-GAAP,
  $7.46bn ABOVE GAAP revenue, and a THIRD definition**, which the proxy itself concedes:
  *"These financial metrics differ from the non-GAAP financial results we report in our
  quarterly earnings release materials."*
- **PSAs: 70% of the weight is CLOUD REVENUE GROWTH. There is no margin metric, no
  return-on-capital metric and no per-share metric anywhere in the plan.**
  **A $116bn annual capital budget is being directed by people paid on the revenue it
  produces and not on the return it earns.** That is [E2-30](2) and (3) in one sentence, and
  it is the most important governance fact in the file.
- CEO summary compensation $96,496,790; compensation actually paid $131,138,799; **pay ratio
  480:1**. **Microsoft trailed its own chosen peer index in 3 of the 5 disclosed 402(v) years
  (TSR 255 vs 276 in FY2025)** — so [E3-54]'s scored test does **not** pass on the proxy's own
  comparison.
- **Insider ownership effectively nil — the CEO holds 900,572 shares, about 0.012%**; one
  nominee holds zero. Chairman and CEO roles combined. Largest holders are index managers
  (Vanguard 8.95%, BlackRock 7.30%). **[E4-27]: "never, ever, think about something else when
  you should be thinking about the power of incentives."** The incentive here points at cloud
  revenue growth and at nothing that would restrain the capital budget.

**CONTINGENT LIABILITIES — the COKE persistence flag, run.**
- **IRS Notices of Proposed Adjustment, received 2023-09-26, first filed in the FY2024 10-K:
  $28.9bn plus penalties and interest, for tax years 2004-2013, with 2014-2017 still under
  audit — fourteen tax years live, unresolved for three years.** Deloitte's **critical audit
  matter**.
- **It is SUBSTANTIALLY PROVIDED FOR, which is why persistence does not convict:** Note 11
  carries **$25.8bn of unrecognized tax benefits plus $9.4bn of accrued interest ≈ $35.2bn**,
  the same order as the claim. **The COKE flag does NOT fire** — the exposure is accrued, not
  merely disclosed.
- Legal accruals are trivial ($553M, 0.4% of net income). **"CMA" appears zero times in any
  10-K; "FTC" once ever**, in FY2024 risk factors, never as a contingency.
- **Goodwill: $17.9bn → $119.7bn (27% of equity), never impaired in this window — but
  $11.3bn was impaired in FY2012 and FY2015.** They have written down failed deals before,
  which is the [E4-39]-adjacent point in their favour.

**[E4-52] — THE LOLLAPALOOZA TEST, RUN EXPLICITLY.** Six disclosure choices point the same
way: pay on cloud revenue with no capital metric · two server-life extensions · the decay of
the life-extension disclosure to nothing · the withdrawal of every unit series · $329.1bn of
leases off balance sheet · a new adjusted measure. **They converge in DIRECTION — every one
makes the AI build easier to present and harder to check.**
**But the run declines to call it a system, and says why.** The candour record is genuinely
large and runs the other way (ASC 606 full retrospective, the dual-filed segment recast, the
newly disclosed RPO duration, the OpenAI related-party revenue volunteered, the withholding
split, EBITDA never used in eleven years, no restatement ever, prior goodwill written down
when warranted). **[E2-30] governs: institutional dynamics, not venality — a company whose
incentive plan pays on cloud revenue growth will produce exactly this disclosure profile
without anyone deciding to mislead.** And **[E5-38]**: a fired flag is not a venality finding.
**Recorded as PARTIALLY FIRED, binding position size, and NOT an integrity finding.**

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** The strong ROE, the
  clean EBITDA record and the disciplined price-sensitive buyback are recorded and **cast no
  vote at Q5** [E2-37, E2-38, E3-39].
- [x] The business does **not** require a great manager; recorded at Q2 as a strength, not
  here [E4-23]. *(The one qualification — that the cloud leg's capital-allocation judgment
  IS the plan — is recorded at Q2 as a moat defect, not here as a compliment.)*
- [x] No great manager is the reason to act. No excisable-cancer case is being run
  [E2-35, E2-36].
**THE GUARDRAIL — check before writing the verdict.**
- [ ] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [ ] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — *"the moat will go when the surgeon goes"* — not here as a strength.
- [ ] If a great manager is the reason to act: is the franchise **already intact** and the
      damage **excisable**, or is the manager the plan? **[E2-35, E2-36]** **Neither — no
      great-manager case is being run at all, so the exception class is not reached.**

- **VERDICT: [x] IN — as an OVERLAY, no disqualifier found.**
  *IN = no disqualifier found. **NOT a finding that the managers are honest** — "sincerity and
  empathy can easily be faked" **[E5-17]**, and **[E5-32]** caps every filing-based test here:
  Salomon's books carried an invented number signed by the largest audit firm in the country
  for twelve years. **IN never promotes.***
  **Live flags carried forward, all binding position size only:** buyback condition 2 (~4x the
  judged value) · [E2-49] metric-switching, the strongest flag in the file · [E2-30] two of
  four scored · pay with no capital-return metric on a $116bn budget · ROE/ROTE halved since
  FY2022 · Activision at $75.4bn for +0.2% of net income · [E4-52] partially fired.

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**Construction:** OCF − SBC − (c), from **nine 10-K vintages read by hand**, with four
cross-vintage checks returning identical figures (FY2017/FY2018/FY2019 OCF; FY2024 capex).

**Owner earnings by year ($M), both ends of the capex band:**
| FY | OCF | SBC | capex | fin-lease ROU | **(c)=capex+leases** | **OE** | OE at (c)=D&A |
|---|---|---|---|---|---|---|---|
| 2021 | 76,740 | 6,118 | 20,622 | 3,290 | 23,912 | **46,710** | 58,936 |
| 2022 | 89,035 | 7,502 | 23,886 | 4,234 | 28,120 | **53,413** | 67,073 |
| 2023 | 87,582 | 9,611 | 28,107 | 3,128 | 31,235 | **46,736** | 64,110 |
| 2024 | 118,548 | 10,734 | 44,477 | 11,633 | 56,110 | **51,704** | 86,856 |
| 2025 | 136,162 | 11,974 | 64,551 | 20,511 | 85,062 | **39,126** | 94,755 |
| 2026 | 182,935 | 12,405 | 115,948 | 24,608 | 140,556 | **29,974** | 131,996 |
*(earlier capex-end years, leases immaterial: FY2017 28,112 · FY2018 28,312 · FY2019 33,608 ·
FY2020 39,945)*

**THE FACT THE FILE TURNS ON: owner earnings including the leased fleet have FALLEN 44% in
four years — $53,413M (FY2022) to $29,974M (FY2026) — while revenue rose 67%, from $198.3bn
to $331.8bn.** This is the WMT shape at twice the scale and four times the speed.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- **Short-window mean** (3-yr FY2024-26): **$40,268M** (capex+leases end) / $110,344M
  (depreciation-only end)
- **Long-window mean** (5-yr FY2022-26): **$44,191M** (capex+leases) / $88,958M (D&A line)
- **10-yr FY2017-26, capex-only end** (leases not available for the early years): $46,504M
- **Spread, conservative end:** 3-yr $40,268M vs 10-yr $46,504M = **13.4%** — narrow, and
  **a tight spread here is not safety**: it is the STEP-DOWN shape the queue's tail triage
  named at BA and INTC. The series is not noisy; it is falling.
- **COMBINED RANGE (window spread × capex band): $29,974M to $136,230M — a 4.5x, $106bn-wide
  band. Three to four times ORCL's ~$25bn width, which the queue called "the AI-datacentre
  capex question."**
- **Is that range too wide to reach a conclusion? NO — AND THE REASON IS THE WHOLE
  ADJUDICATION.** [E4-25] closes a file when the range **straddles the answer**. This one does
  not straddle anything: **every point in it, and the most generous point outside it, is below
  the 5.24% sovereign** (0.81% at the bottom, 3.67% at the very top). **The band is enormous
  and decision-irrelevant.** Q4's own rule — *"if the capex band changes the verdict →
  UNKNOWABLE"* — is tested directly and **the band does not change the verdict.**
  *(This is the honest reading and the run states the alternative it rejected: a run that
  wanted to close this file could invoke [E4-25] on the width alone. That would be
  resolving-by-preference in the opposite direction, and the width does not earn it.)*
- **[E5-11]/[E4-41] — DISTORTED YEARS NAMED BOTH WAYS.**
  **UP (removed or discounted before the mean is trusted):** FY2021 COVID cloud pull-forward
  **and the first server-life extension (+$2.7bn of operating income)**; FY2023 **the second
  extension (+$3.7bn)**; **FY2026 carries ~$14.2bn of deferred tax** — the depreciation DTL
  tripled and leasing added $8.8bn — so **operating cash flow is flattered by timing that
  reverses**, with U.S. federal cash tax of $6,246M on $103.6bn of U.S. pretax income (6.0%),
  less than was paid to Ireland.
  **DOWN:** FY2018 TCJA transition tax; **FY2026 also bears the final $4.4bn TCJA
  installment.**
  **The FY2026 deferred-tax flattery is DISCLOSED AND DELIBERATELY NOT SUBTRACTED**, because
  it is the tax shield ON the very capex already being deducted in full at (c). Deducting both
  would be spending conservatism twice **[E4-11, E4-48]**. **Windage count: ONE.**
  [E5-33]: no restructuring charges exist to add back — the caption is zero from FY2021.

- **MAINTENANCE CAPEX — THE DISCLOSED JUDGMENT. THIS IS THE FILE.**
  **The D&A end is INVALID here, and it is established BY MEASUREMENT, not by assertion** —
  which is what the brief asked for. Three independent proofs:
  1. **Capex ÷ D&A ran 0.93x–1.26x for the six years FY2015-FY2020** — squarely [E3-44]'s
     default class, where *"the depreciation charge is not inappropriate … as a proxy."* It
     then went 1.76 → 1.65 → 2.03 → 2.12 → 2.19 → **3.01x** (3.38x on depreciation alone,
     **≈4.1x including finance leases**). **[E5-20]'s railroads need >60% of total capex;
     depreciation is 33% of Microsoft's FY2026 capex.**
  2. **The depreciation denominator has itself been lengthened twice by management judgment.**
     Server life 3→4 years (July 2020, +$2.7bn operating income, +$0.30 EPS) and 4→6 years
     (July 2022, +$3.7bn, +$0.40 EPS); network equipment 2→6. **No rationale of any kind is
     filed for the first change** — only *"we completed an assessment."* **The two assessments
     contradict each other and no filing reconciles them. Observed service life versus
     accounting life: NOT FOUND IN FILINGS, in eleven vintages.** Depreciation FELL in
     absolute terms in each year an extension took effect while gross PP&E rose 27% and 22%.
  3. **Building (c) forward from the filed gross book at management's OWN current lives**:
     servers/network/software $215,874M ÷ 6 + buildings $182,749M ÷ 15 + leasehold ÷ 12 +
     furniture ÷ 5.5 = **$50,660M** — **48% above the $34.3bn depreciation charge**, and
     landing almost exactly on the **5-year mean capex of $55,394M.** Two independent
     constructions converge on total capex.
  **THE CVX INVERSION WAS TESTED AND DOES NOT APPLY:** purchase accounting could in principle
  push depreciation ABOVE true renewal, but Microsoft's PP&E is overwhelmingly
  self-constructed and the capex/D&A ratio runs the wrong way for it.
  **(c) JUDGED AT TOTAL CAPITAL SPENDING INCLUDING FINANCE-LEASE ROU ADDITIONS**, five-year
  mean **$68,217M**. **Finance leases are not an adjustment here, they are 18% of (c):**
  liabilities **$66,594M — larger than all bonded debt at $46,136M** — and ROU additions of
  $11.6bn/$20.5bn/$24.6bn in FY2024-26, capital spending that never touches the capex line
  because its principal repayment sits in **financing**. The ASC 842 check MCD, DRI and CTAS
  all failed is failed here by two orders of magnitude more.
- **JUDGED OWNER EARNINGS: $45,000M.** Band **$29,974M to $136,230M carried in full [E4-25]**.
- **Stock compensation subtracted in full [E5-06]:** yes, $12,405M FY2026. **[E3-70] noted and
  NOT stacked:** the market-value measure would be higher than the accounting charge, and the
  filing separately discloses **$5.6bn of shares repurchased to settle employee tax
  withholding** — cash compensation, not owner return. Subtracting both would double-count
  against the single windage already spent; **the reported charge is used as the floor and the
  understatement is disclosed rather than priced.**
- **DISCLOSED SENSITIVITY, NOT TAKEN INTO THE BASE:** unpaid PP&E in accounts payable rose
  $6.9bn → **$26.7bn**, so capital *incurred* in FY2026 was ~$135.7bn against $115.9bn paid.
  The cash-flow AP line (+$5,268M) cannot be cleanly reconciled to the balance-sheet move
  (+$14,692M), so the filing does not permit the adjustment to be made rigorously. If OCF is
  flattered by unpaid capex, **FY2026 owner earnings are below $29,974M.**

### Great, good, or gruesome? **[E4-20]** — **[x] GOOD, and travelling AWAY from great**
- **Not gruesome.** [E4-20]'s gruesome class *"earns little or no money"*; Microsoft earned
  $155.2bn of operating income at a 46.8% margin. Nowhere near it.
- **Not great, and the reason is [E4-20]'s own wording** — the great account *"pays an
  extraordinarily high interest rate that will rise as the years pass"* on money you need not
  add. **Productivity & Business Processes, standing alone, IS that account** (59.9% margin,
  eight straight years of expansion, essentially no capital). **The consolidated business is
  not**, because the capital is being added at $140.6bn a year into the other leg.
- **GOOD is the [E4-43] class and it PASSES:** *"capital-hungry growth may well prove to be a
  satisfactory investment."* The test is the return on the ADDED capital, and the answer is
  a range: consolidated incremental ROE on four years' retained capital **~22%**; incremental
  pre-tax return on Intelligent Cloud's own capital **17.0%** (FY2025-26) to **21.0%**
  (FY2024-26); and **6.3% if the server life is really three years rather than six.**
  Against **[E5-40]**'s ~12% on retained capital being *"quite satisfactory"*, the top of that
  range passes comfortably and the bottom fails. **The width is the finding [E4-25].**
- **[E2-56] IS THE EVIDENCE, and it is decisive.** The consolidated incremental return
  (40.7% pre-tax on FY2025-26 net new capital) is **two businesses averaged**: Productivity
  added **+$24,218M of operating income on essentially no capital**, Intelligent Cloud added
  **+$19,159M on $112,532M.** *"Their marvelous core businesses camouflage repeated failures
  in capital allocation elsewhere"* — the run does not allege failure, but it does refuse the
  blended number, exactly as [E2-56] instructs.
- **The corroborating filed series, three years running: Intelligent Cloud GROSS margin
  66.1% → 62.2% → 58.0%, with IC cost of revenue +44.1% against segment revenue +29.7%.**
  Consolidated gross margin 69.8% → 68.8% → 67.9%. **The marginal dollar of datacentre
  capital earns less than the average dollar already deployed, in the filed numbers.**
- **[E2-63] ceiling stated:** the eleven-year record decomposes as revenue ×3.546 × operating
  margin ×2.412. **The margin half is arithmetically near-spent and has REVERSED at the gross
  line** — even at zero operating expense the margin caps at 67.9%. The second decade cannot
  repeat the first decade's arithmetic.

### Staying power — score all three **[E5-11]** → **PASS / QUALIFIED PASS / FAIL**
- **(1) A large and reliable stream of earnings — PASS, emphatically.** Operating cash flow
  $182,935M, up in ten of eleven years; revenue $331,839M; **$75,712M of unearned revenue and
  $684bn of contracted RPO** standing behind it. Nothing in the queue is stronger.
- **(2) Massive liquid assets — QUALIFIED PASS, and the direction is wrong.** $76,843M of cash
  and short-term investments, genuinely liquid (**73% U.S. government and agency**). But it
  has **FALLEN 31% from $111,271M at FY2023** while total assets went $412bn → $758bn; it is
  **2.1% of market capitalisation**; working capital has **halved since FY2023** ($80.1bn →
  $38.9bn) and the current ratio is at a six-year low of **1.23**.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAIL. This is the one that usually kills
  and it does not survive the contractual-obligations table.** FY2026 10-K, MD&A, as of
  2026-06-30, payments due in **fiscal 2027 alone: $241,922M** —
  purchase commitments **$169,008M** (*"primarily relate to datacenters and include open
  purchase orders and take-or-pay contracts"*), leases **$32,411M**, construction commitments
  **$29,848M**, debt principal $9,250M, interest $1,405M. Total obligations **$743,821M**.
  **The one-year figure has run $59.4bn → $89.6bn → $114.3bn → $148.1bn → $241.9bn — 4.1x in
  five years — while liquidity fell 31%.**
  **The arithmetic:** $76.8bn of liquidity + $182.9bn of operating cash flow = $259.8bn
  against $241.9bn due. It clears by **$17.8bn — before $43.2bn of dividends and buybacks.**
  **On FY2026's own run-rate, fiscal 2027's contractual plan cannot be funded from cash flow
  and liquidity while also returning capital at the current rate.**
  **And $329,114M of leases signed but NOT YET COMMENCED sits outside all of it** (FY2027-33)
  — 99% of a year's revenue — with the operating/finance split of that figure **discontinued
  after FY2024** and FY2026 adding an unquantified hedge, *"with some arrangements subject to
  certain contractual conditions being met."*
  **[E5-39] runs directly at this and the filing meets it head-on:** *"Our ability to fund
  these investments depends on our ability to generate sufficient cash flows and **obtain
  financing on acceptable terms**. Adverse changes in interest rates, credit markets,
  **investor sentiment**, our credit ratings, or other factors affecting capital availability
  could … **limit our ability to execute our infrastructure strategy**."* Against *"we will
  never be dependent on the kindness of strangers."* **And there is nothing to fall back on
  that the framework would count anyway: "credit facility", "revolver" and "covenant" appear
  ZERO times in the FY2024, FY2025 and FY2026 10-Ks — no committed backstop is disclosed at
  all.** Commercial paper outstanding was zero at FY2025 and FY2026.
- **Leverage, named and quantified [E4-16, E3-29]** — *no ratio ceiling exists in this
  framework*: bonded debt **$46,136M** (fair value $36.5bn) plus finance-lease liabilities
  **$66,594M** = ~$112,730M against **$442,387M of equity**. **The debt maturity wall is
  trivial: $9,250M / $0 / $2,001M / $0 / $500M — $11,751M over five years**, and no debt was
  issued in FY2025 or FY2026.
  **[E2-54] coverage: operating cash flow net of the entire capital bill ($66,987M) against
  FY2027 interest of $1,405M is ~48x. Solvency is not the issue and the run says so plainly.**
  **[E3-52] the good liability, and it is very large:** $75,712M of unearned revenue —
  customer-prepaid, *"without covenants or due dates attached."*
  **The honest summary: this balance sheet is in no danger. What has changed is that
  Microsoft has committed, contractually, to spend more in the next twelve months than it
  holds in liquid assets three times over — and [E5-11]'s third strength is a test about
  commitments, not about solvency.**

### Name the specific way THIS business dies **[E2-27, E3-24]** — model exposure, not experience **[E4-40]**
**1. THE [E2-27] CAPEX TREADMILL / OVERBUILD — and the company names it itself.**
- **Mechanism, verbatim from Item 1A:** *"**Overestimation of demand or misalignment of
  capacity investments may result in underutilization of infrastructure and may lead to
  impairment of assets on our balance sheet.**"* And: *"These investments … are **in advance
  of fully developed revenue streams.**"* Four hyperscalers are building the same capacity for
  the same workloads at the same time — *"viewed individually … cost-effective and rational;
  viewed collectively, the decisions neutralized each other."*
- **Quantified from filed figures:** a 20% impairment of the $215,874M server book is a
  **$43.2bn charge — a full year of judged owner earnings.** More important than the charge:
  if capex holds near $116bn while D&A converges upward and revenue growth decelerates,
  **owner earnings at the capex end settle permanently at $30-45bn** while revenue grows.
- **Likelihood: [x] A REAL POSSIBILITY — and partially the base case, because it is what the
  last four filed years already show** (OE including leases down 44% on revenue up 67%).
**2. THE DEPRECIATION-LIFE RECKONING — and a peer has already taken it.**
- **Mechanism:** the six-year server life is management's estimate, filed with no rationale
  for the first extension and no observed-service-life evidence ever. **Amazon, operating the
  largest cloud fleet on earth, shortened a subset of servers from six years back to five
  effective January 2025 — +$1.4bn of D&A, −$1.0bn of net income, "primarily impacted our AWS
  segment", plus $920M of accelerated depreciation for early retirements, at double its own
  guidance — because of "the increased pace of technology development, particularly in the
  area of artificial intelligence and machine learning." Microsoft, Alphabet and Oracle have
  not re-tested.**
- **Quantified:** servers/network/software $215,874M at a 4-year life instead of 6 raises
  annual depreciation by **~$17,990M**; reported operating income $155,237M → ~$137,247M,
  **−11.6%.** **Owner earnings at the capex end are UNCHANGED — structurally immune.**
- **Likelihood: [x] A REAL POSSIBILITY.** The peer that looked hardest at its own fleet
  concluded six years was wrong.
**3. THE OPENAI PERIMETER — the circular-revenue exposure, disclosed and unquantifiable.**
- **Mechanism, from the FY2026 10-K:** Microsoft holds *"an approximate **25%** interest on an
  as-converted basis"* accounted for by the equity method under **HLBV**; it has *"total
  funding commitments of **$13.0 billion** … of which **$11.9 billion** has been funded"*; and
  it discloses, for the first time and as a related party, *"revenue from commercial
  arrangements with OpenAI, inclusive of revenue-sharing payments, of **$24.1 billion**, and
  accounts receivable from OpenAI as of June 30, 2026 was **$6.0 billion**."*
  **That is 7.3% of total revenue and 91 days of receivable, from a counterparty Microsoft
  part-owns and part-funds.** The equity-method line is **−$1,482M (FY2024), −$4,763M (FY2025),
  +$6,530M (FY2026) — cumulative +$285M, essentially nil across three years — and the FY2026
  gain is one quarter's non-cash dilution gain from the "OpenAI Recapitalization"** (Q1
  −$4.1bn, Q2 +$10.0bn, H2 +$0.6bn). **The carrying value of the investment is NOT DISCLOSED
  in any year.**
  **And the two sentences that justified the arrangement were DELETED in FY2026 with no
  explanation:** FY2025 said *"The OpenAI API is exclusive to Azure, runs on Azure"* and *"We
  also have a right of first refusal on OpenAI's new capacity needs."* Both are gone; the
  ownership figure also fell from 27% to 25% without comment. **Whether any of the $194.1bn of
  purchase commitments relates to OpenAI is NOT FOUND IN FILINGS.**
- **Quantified:** loss of the arrangement removes **$24.1bn of revenue (7.3%)** and puts
  **$6.0bn of receivable** at risk; at Intelligent Cloud's 41.3% margin that is ~$10bn of
  operating income.
- **Likelihood: [x] A REAL POSSIBILITY for the revenue line; a low-level possibility for
  solvency.**
**4. SOLVENCY — essentially unnameable, and the run says so.** It would require a
simultaneous collapse in cloud demand, the loss of $75.7bn of customer prepayments, and a
capital-markets refusal, against $442bn of equity and an $11.8bn five-year maturity wall.
**[x] A LOW-LEVEL POSSIBILITY.** *"which we consider only a low-level possibility, not a
likelihood"* **[E3-24]**.

### **[E4-51] — THE ARGUMENT AGAINST MY POSITION, STATED AT FULL STRENGTH**
*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."* My position is FAIL. The bull case:
> Microsoft is the best business in its competitor row on every metric that matters: the
> highest capex-end owner earnings of the four ($54.6bn against Alphabet's $48.3bn and two
> negatives), the highest cloud segment margin, the highest returns on tangible capital. Its
> filed record **exceeds the rate its price requires by two to three times** — operating
> income compounded **+21.5% a year for eleven years**. Its annuity segment earns a **59.9%
> operating margin, rising for eight consecutive years**, and absorbed a price increase with
> seats still growing. It carries **$684bn of contracted backlog, 2.1x annual revenue.** And
> the depression in owner earnings is not a deterioration at all — it is the arithmetic
> signature of **building ahead of revenue**, exactly as the company says: net property and
> equipment went $204.9bn → $313.1bn in a single year. **The consolidated incremental pre-tax
> return on FY2023-26 net new capital is 47.8%**, and even the conservative segment-split
> version, 17-21%, sits at or above [E5-40]'s "quite satisfactory" 12%. If that return is
> real and persists, today's owner-earnings figure is the most misleading number in the file,
> and the [E4-28] floor is Buffett's own admittedly arbitrary judgment, not a law.
**That is the strongest form of the case and it is not a weak one.** The answer is at Q5 and
it is arithmetic: **granting every one of those points does not get the yield to the bond,
let alone to the floor.**

- **VERDICT: [x] IN**
  *IN on survival, which is what Q4 asks. GOOD, not great. The third strength FAILS on
  commitments and is recorded as a failure, not smoothed — but [E5-11]'s three strengths are
  scored, not summed into a gate, and neither [E2-54] coverage nor the maturity wall nor the
  equity base supports an OUT on survival. The band is the widest in queue history and does
  not change the verdict.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*
**Honest pre-tax expectancy at this price: ~6% (range 5-7%). Below roughly 10% → the name is
NOT RANKED. It is quit on, whatever the sovereign is.**
**No risk premium in the discount rate [E3-42]** — the bare 5.24% is used; certainty lives at
Q1 and in the end discount, never in the rate.

**One book. Owner earnings against the bond.** No DCF was run; none was needed **[E3-34]**.

**1. THE YIELD**
- owner earnings **$45,000M** ÷ market cap **$3,710,545M** = **1.21 %** · sovereign **5.24 %**
- **THE WHOLE BAND, because one number would hide the finding [E4-25]:**

| construction | owner earnings | **yield** | vs sovereign |
|---|---|---|---|
| FY2026 alone, (c) = capex + finance leases | 29,974 | **0.81%** | −4.43 |
| **3-yr mean, (c) = capex + finance leases** *(the screen's own oe_bottom)* | **40,268** | **1.09%** | −4.15 |
| 5-yr mean, (c) = capex + finance leases | 44,191 | 1.19% | −4.05 |
| **JUDGED** | **45,000** | **1.21%** | **−4.03** |
| 5-yr mean, (c) = capex only | 57,013 | 1.54% | −3.70 |
| 5-yr mean, (c) = D&A line — **INVALID [E5-20]** | 88,958 | 2.40% | −2.84 |
| 3-yr mean, (c) = depreciation only — **INVALID** *(the screen's oe_top)* | 110,344 | 2.97% | −2.27 |
| **FY2026 alone at depreciation only — the most generous number that can be built** | **136,230** | **3.67%** | **−1.57** |

**EVERY CONSTRUCTION, ON EVERY WINDOW, AT BOTH ENDS OF THE CAPEX BAND, IS BELOW THE
30-YEAR TREASURY.** The single most generous figure constructible — the best year in the
company's history, valued as though a depreciation charge that management has twice lengthened
fully replaces a fleet whose replacement bill is three times that charge — **still pays 1.57
points LESS than a government bond that carries no business risk at all.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Growth needed merely to match the bare bond: +4.03%/yr, PERPETUAL** (at the judged
  number; +1.57%/yr at the most generous construction that exists).
- **Growth needed to clear the ~10% floor: +8.79%/yr, PERPETUAL** (+6.33%/yr at the most
  generous construction).
- **What the business has actually done — and this is where the band decides the file:**
  | series | rate | window |
  |---|---|---|
  | revenue | **+12.2%/yr** | FY2015-26 |
  | operating income | **+21.5%/yr** | FY2015-26 |
  | owner earnings at the **D&A** end | **+19.1%/yr** | FY2017-26 |
  | owner earnings at the **capex** end | **+7.65%/yr** | FY2017-26 |
  | **owner earnings including the leased fleet — the honest construction** | **−8.49%/yr** | **FY2021-26** |
  **The required rate is +8.79% perpetual. On the construction this run judges honest, the
  filed record is MINUS 8.49% a year for five years. On the construction the framework calls
  INVALID, it is plus 19%. There is no third possibility, and the entire question of whether
  Microsoft is cheap or dear at $499.70 reduces to which of those two numbers is real.**
  **This run says the capex end is real, and it says so on measurement — capex ÷ D&A of
  3.01x (4.1x with leases), a depreciation life that management has doubled twice with no
  filed rationale for the first change and no observed-service-life evidence ever, and a peer
  operating the largest fleet on earth that has already reversed.**
- **[E4-35]'s burden of proof, discharged in writing as the framework demands:** sustained
  double-digit growth is a fewer-than-one-in-twenty event *among the 200 most profitable
  companies in the world*. **The floor case here needs +8.79% a year FOREVER, from the largest
  company that has ever existed.** Compounded from $45bn that is $107bn in ten years, $253bn
  in twenty, **$598bn in thirty — against total FY2026 revenue of $332bn.**
- **[E2-63]/[E4-44] name what bounds the upside:** *"the value of an asset … cannot over the
  long term grow faster than its earnings do."* The eleven-year record was revenue ×3.546 ×
  **margin ×2.412**, and the margin lever is arithmetically near-spent and **already reversing
  at the gross line** (69.8% → 68.8% → 67.9% consolidated; Intelligent Cloud 66.1% → 58.0%).

**3. WHAT YOU ARE PAID**
- **−4.03 points versus the sovereign** at the judged number; **−1.57 points** at the single
  most generous construction that exists. **You are not paid a premium over the government
  bond for owning Microsoft at $499.70. You are paid a penalty.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24 %** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support. Zero growth, discounted at the bare sovereign, per share:
- **conservative ~$75** *(FY2026 owner earnings incl. leases)* · **judged ~$115** ·
  **optimistic ~$350** *(FY2026 at depreciation only — a construction this run calls INVALID
  and prices anyway, so the reader can see it does not rescue the case)*
- **at the [E4-28] floor: ~$40 conservative · ~$60 judged · ~$185 optimistic**
- **CURRENT PRICE $499.70** (2026-09-04, aggregator, flagged)
- **The price is 4.3x the judged zero-growth value, 8.2x the judged floor value, and 1.43x
  the most generous zero-growth number that can be constructed from these filings.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- **FLOOR VERDICT FIRST: honest pre-tax expectancy ~6% (5-7%) versus ~10% [E4-28] — BELOW.
  THE NAME IS QUIT ON, NOT RANKED, and the ranking lines below are therefore not filled in.**
  *(Even the arithmetic that grants everything — the most generous 3.67% yield plus a
  generous 6% perpetual growth — reaches 9.7% and still does not clear.)*
- points over sovereign: **−4.03** — *not ranked; a negative spread has no ranking position*
- against the rest of the opportunity set: **not applicable — [E4-28] quits before ranking.**
  *"that's the figure we quit on … that's true whether short rates are 6 percent or whether
  short rates are 1 percent."*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [x] **Screamer test [E4-01], and the outcome is the THIRD one — above the whole range.**
      No margin is added on top; *"startlingly low"* is what you observe, not what you
      subtract. The conservative case is ~$75/share and the price is **$499.70**. This is not
      the *"no useful conclusion"* middle outcome — **the price is above even the invalid
      construction's ~$350.** *(Bar 1 is not used and no margin percentage is stated, because
      the price does not reach the range at all; applying both bars to one number is
      forbidden.)*
- **Windage count: ONE.** Conservatism is spent once, at the **(c) judgment** — total capital
  spending including finance-lease additions — and that single application is **evidenced
  rather than assumed** (capex/D&A 3.01x; the steady-state build from the filed gross book
  converging on the five-year mean capex). **Two further conservative adjustments were
  available and were explicitly DECLINED so that conservatism is not stacked [E4-11, E4-48]:**
  the ~$14.2bn of FY2026 deferred tax flattering operating cash flow, and the ~$19.8bn
  increase in unpaid capex sitting in accounts payable. **Taking either would have lowered
  owner earnings further and neither was taken.**

- **VERDICT: [x] UNKNOWABLE is NOT the verdict, and neither is IN. The verdict is that the
  name FAILS the floor at this price — Q5 returns NOT IN, on price, at [E4-28].**
  **Ranking position: none. Quit on, not ranked.**
  *The business gates are all IN; the price is the whole objection. This is the same shape as
  BRK-B, CTAS, CMG, WMT and GRMN before it.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position is held and none is taken** *(PORTFOLIO.md: zero occurrences of MSFT — checked,
and recorded because operator rule 9 makes the analyst a subject of the psychology: there is
no position here creating an incentive to clear the name)*. Q6 is therefore the
**pre-committed re-look**, written now so it cannot be retro-fitted **[E1-02]**.

**Pre-committed before any entry [E1-02]:**
- **THE RE-LOOK PRICE: ~$115/share** — judged zero-growth value at a 5.24% sovereign,
  **to be recomputed at the rate of the day.** The floor clears near **~$60/share**.
  **State the honest implication: that is an 77-88% decline, so this file is FAR likelier to
  re-open on EARNINGS than on price.** At $499.70 the floor needs **~$371bn of owner
  earnings — more than Microsoft's entire FY2026 revenue of $332bn.**
- **THESIS-CONFIRMING METRIC (the one that would re-open the file, and it is a pair that must
  hold together): total capital spending — capex PLUS finance-lease ROU additions — falling
  below 25% of revenue, WHILE owner earnings on that construction rise above $80bn.** Both,
  for two consecutive fiscal years. That is the signature of a build that has finished and
  begun to pay, and it is the only thing that makes the [E4-28] floor reachable from here.
- **THESIS-BREAKING METRICS AND THEIR THRESHOLDS:**
  - **Intelligent Cloud gross margin below 55%** (58.0% today, down 8.1 points in three years)
  - **a THIRD server-life extension, to seven years or beyond** — or, in the other direction,
    **an Amazon-style SHORTENING**, which would be the candour case and would simultaneously
    confirm this run's central judgment
  - **leases not yet commenced above $400bn** ($329.1bn today)
  - **RPO converting below 25% within twelve months** (30% today, halved from 60%)
  - **[E2-49] withdrawal of the OpenAI related-party revenue disclosure**, or of the RPO
    duration, or of the segment cost-of-revenue split that made the Pro-Am test possible
  - **buybacks continuing above ~$20bn/yr at prices above ~$400** *(FY2026: $16.7bn at
    $464.42)*
  - twelve-month contractual obligations above ~$300bn while liquidity stays below ~$80bn
- **NEXT CATALYST DATE: the FY2027 10-K, expected late July 2027.** And a dated structural
  one: **the FASB expense-disaggregation standard, which the FY2026 10-K discloses as not
  adopted until FY2028, will force the split of the depreciation charge now sitting
  undisclosed inside R&D** — the first filing that will let an outsider check the AI
  cost structure directly.

**The sell rule [E2-28]** — recorded for completeness; no holding exists.
- SELL if the market judges it more valuable than the facts indicate — **this is that case,
  in advance: the price sits at 4.3x the judged zero-growth value.**
- SELL if funds are needed for something better understood — n/a.
- HOLD conditions: return on equity capital **satisfactory (ROE 30.2%, ROTE 44.0%)** ·
  management **competent, no disqualifier found** · market **DOES overvalue**. The third
  condition fails, which is precisely why no position is taken.
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The monitoring question [E4-17, E3-30]:** *is this erosion an aberrational cycle, or has the
business slipped in a way that permanently reduces intrinsic value?* **Answered honestly: it
is NOT erosion at all — the franchise is widening at Productivity.** What has changed is
**the price of participating in it**, and the fact that a second, materially worse business
has been bolted onto the first and is absorbing 42% of revenue in capital every year.
**[E4-17]'s "beliefs change quite gradually" is respected: this run does not conclude that
the AI capital is wasted.** It concludes that at $499.70 you are not paid to find out.

**Position size — a judgment, stated: ZERO.** Not sized down; not taken. **Three
capital-allocation flags are live** (buyback condition 2 at ~4x value; pay with no
return-on-capital metric on a $116bn budget; [E4-52] partially fired), each of which
**binds position size and none of which touched the discount rate [E4-13].**

- **VERDICT: [x] IN** — the re-look is pre-committed, dated and falsifiable, and the file is
  left open rather than closed. **[E3-47] respected: this is not an UNKNOWABLE on a business
  inside the circle; it is a priced refusal, and the file names exactly what would reverse it.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q5 opened only after Q1-Q4 each
      returned IN (operator rule 2).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The moat
      class is NARROW, not PROVISIONAL — the competitor row was built from the peers' own
      filings, and the unavailable comparison (no filer discloses a productivity-suite
      segment) is stated as a **limit on the row**, not as a caveat on the verdict.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned. Absences are recorded as
      **absence findings with the sweep described** (eleven vintages, named search terms),
      per the absence-claim rule — never as "does not exist."
- [x] Step 0: filing read with accession number (`0001193125-26-323660`); **four figures
      cross-checked across vintages, all identical.**
- [x] Owner earnings on multi-year means; **three windows shown**; capex band disclosed as a
      judgment with the [E5-20] exception class established **by measurement**.
- [x] Competitor row filled — 3 SEC-filing peers, 28 filings read, same metrics, same window.
- [x] Sovereign is USD (the earnings currency), **from the US Treasury directly**, dated
      2026-09-04, struck fresh for this run.
- [x] Value stated as a round-number range, not a point estimate.
- [x] **One bar chosen (Bar 2, outcome three), not both; windage count stated as ONE**, with
      the two declined adjustments named.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git after every question (write-early protocol).
- [x] **Operator rule 9 checked: no position held in MSFT** (PORTFOLIO.md swept, zero hits),
      so no incentive to clear the name. **Operator rule 8: every judgment above carries a
      ledger id.** **Operator rule 3: no valuation language appeared before Q4 closed.**

## REGISTER
- **Verdict: FAIL at Q5, ON PRICE, at the [E4-28] floor. Q1 IN · Q2 IN (NARROW) · Q3 IN
  (OVERLAY, no disqualifier) · Q4 IN (GOOD, not great) · Q5 NOT IN · Q6 IN (re-look
  pre-committed).**
- **One line:** *The largest business ever run in this queue clears all four business gates
  and fails on price by the widest margin any gate-clearer has failed by — and the reason is
  that the number everyone quotes for Microsoft's earnings depends on a depreciation life
  management has doubled twice, while the number that does not depend on it has fallen 44% in
  four years.*
- **THE SIXTEENTH name to clear all four business gates.** *(Ordinal settled against the
  parallel AAPL run by the queue's Q4-commit rule — CTAS/CMG/GRMN precedent: AAPL `f75baf1`
  13:32:57 versus MSFT `fd8e926` 13:37:30. AAPL is fifteenth.)*
- **PRICE: $499.70** (2026-09-04, Yahoo, aggregator, flagged).
- **PASS/FAIL: FAIL.** Closed at **Q5**, on price.

---
## RUN DEFECTS — assume some, and name them

**Brief defects (where the brief's priors came back different):**
1. **The brief expected "Q2 IN WIDE" and it came back IN NARROW.** Productivity alone is
   WIDE; the composition of the business around it is not. This is the first time in the
   queue a segment-level WIDE has been overridden by the business's own mix.
2. **The brief's two hypotheses were framed as pointing in opposite directions. They do not.**
   (b) is right about the income statement — ~13% of FY2026 operating income is
   life-extension (my scaling) — and (a) is partly right about the cash, since the fleet
   genuinely doubled. **Both roads arrive at the same verdict**, which is a stronger result
   than the brief anticipated and is stated as such.
3. **The brief said the D&A end is "almost certainly INVALID … in the VZ shape" and asked for
   proof rather than assertion. Proof obtained — and by three independent routes**, one of
   which (building (c) forward from the filed gross book at management's own lives, landing on
   the five-year mean capex) was not anticipated by the brief.
4. **The brief expected ORCL's ~$25bn band to be "the same question at larger scale."
   Understated by a factor of four**: MSFT's band is $29,974M to $136,230M, ~$106bn wide.
5. **The brief's screen-spread warning inverted.** It warned that three screen spreads had
   failed to reproduce. **Both MSFT screen rows reproduce EXACTLY** — the 2026-09-01 row to
   the decimal at both ends, and the 2026-09-04 row (40,268 / 110,344 / 1.74) to the decimal
   once finance-lease ROU additions are in (c). **My first pass recorded the second row as
   "not reproduced"; that was MY error and it is corrected in an addendum file, not by
   editing the original.**

**Run defects (holes I did not close):**
1. **[E3-48]/[E5-30] guidance-outturn is UNMEASURED, and it is the largest hole.** The 10-K
   contains no guidance, which is a genuine pass on the filed record — but **earnings releases
   and calls were not swept**, and Microsoft does give quarterly segment guidance verbally.
   The GRMN run left the identical hole; it is now a repeat defect in this queue.
2. **The accrued-capex question is unresolved.** The cash-flow AP line (+$5,268M) cannot be
   reconciled to the balance-sheet AP move (+$14,692M) against a $19,800M rise in unpaid
   capex. The filing does not permit it. Carried as a sensitivity, not taken into the base.
3. **No construction-in-progress figure exists in ANY of eleven vintages, and there is no
   PP&E rollforward** — no additions, retirements or disposals lines. **I therefore cannot
   determine what fraction of the $431.8bn gross book is not yet depreciating**, which is the
   single most useful number for judging (c) and it is not filed.
4. **The capex category split is NOT FOUND IN FILINGS** ("short-lived" appears zero times).
   Management has described a long-lived/short-lived split publicly; it is not in a filing, so
   it was not used. The 62%-of-FY2026-gross-additions figure for servers is **derived from the
   PP&E footnote by me, labelled CONVENTION, not disclosed.**
5. **The ~$20bn scaled run-rate effect of the life extensions is MY computation**, scaled from
   two disclosed first-year figures by gross PP&E. The filings stopped disclosing it after
   FY2024. It is a judgment, labelled as one, and the Pro-Am incremental return is materially
   sensitive to it (6.3% vs 21.0%).
6. **FY2016 and earlier owner earnings were not rebuilt with finance leases** (the disclosures
   pre-date ASC 842), so the 10-year and 15-year windows are capex-only and understate (c).
7. **Alibaba Cloud, Tencent Cloud and the neocloud tier are absent from the competitor row** —
   the most material omission, stated rather than stretched.
8. **International/jurisdictional [E3-66] was not run.** MSFT earns a majority of revenue
   outside the US; the run did not test where shareholders stand in any non-US queue.
9. The FY2026 10-K discloses a **recast of prior-period cash-flow statements**; I verified it
   did not move the four lines I use, but I did not establish what it DID move.
10. Segment margins throughout are **my computation** from two filed figures, not filed ratios.

---
# THE TWO REQUIRED OUTPUTS

**(1) THE PRICE.** **$499.70** per share (2026-09-04 close, Yahoo Finance — aggregator, used
for the live quote only and flagged). Market capitalisation **$3,710,545M** on
**7,425,545,491** shares hand-read off the FY2026 10-K cover.
Value, zero growth against a **5.24%** US Treasury 30-year: **~$75 to ~$350 per share, judged
~$115**; **~$40 to ~$185 at the [E4-28] floor, judged ~$60.**
*This price is a normal Q5 output — Q1 through Q4 each returned IN, so operator rule 3's
"COMPUTATION — NOT A CLEARANCE" heading does not apply.*

**(2) PASS / FAIL.** **FAIL.** The file closed at **Q5**, on **price**, at the **[E4-28]
~10% floor**. Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay, no disqualifier) · Q4 IN (GOOD, not
great) · **Q5 NOT IN** · Q6 IN (re-look pre-committed).
**Microsoft is a magnificent business and the best of its four filed peers on every metric
the row measures. At $499.70 it yields 1.21% against a 5.24% government bond, and it does
so on every construction the filings support — from 0.81% to 3.67%.**
