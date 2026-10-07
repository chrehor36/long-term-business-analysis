import io
p = 'Test Runs/2026-09-19 Run - IBM International Business Machines.md'
s = io.open(p, encoding='utf-8').read()
start = "## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?"
end = "## Q4 — WILL IT SURVIVE?"
i, j = s.index(start), s.index(end)
new = """## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`* — **RECORDED, NOT GOVERNING.**
*The file closed at Q2. Nothing below can promote the name, and a Q3 IN never promotes anyway
**[E2-37, E2-38, E3-39]**. Every ledger id in this section was checked against
`principle_ledger.csv` before it was written (268 rows; zero phantom ids), because the brief
inherited a known error class — earlier briefs in this queue cited **[E4-52]** for what pay
vests on when the incentives row is **[E4-27]**.*

**STEP 1 — THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution [E3-38, E3-43, E2-70]** — 31% of revenue is Consulting, a business bid
      and delivered contract by contract, and management says so itself in the letter of
      2026-07-14: *"These conditions require our teams to execute perfectly, and this quarter we
      faltered. We did not adapt and move quickly enough, and numerous large deals failed to
      close on the timelines we expected."* That is a have-to-be-smart-every-day statement made
      by the CEO about his own company.
- [ ] **Control [E1-16]** — no. A marketable minority holding, exitable.
- [x] **Leverage [E3-29]**, and it is quantified rather than screened, because the framework
      supplies no ratio: **total debt $61,260M at 2025-12-31 and $62.0bn at 2026-06-30**, of
      which Financing segment debt is $15,093M and $13.0bn, leaving **non-Financing debt of
      $46,167M and about $49bn** against **$8.2bn of cash, restricted cash and marketable
      securities at 2026-06-30 — down $6.3bn in six months** because $10,480M went out for
      Confluent. Debt ÷ operating cash flow is **4.64×**, which the ORCL run of 2026-09-06
      recorded as making IBM *"the only company in the row that is more levered, and IBM is not
      building data centres."* And **tangible equity is negative $46,368M** (Q2's [E2-43]
      arithmetic), so book equity absorbs nothing.

**CASE DECLARED: Q3 is a BINARY GATE, not an overlay, and no price would compensate for an
integrity failure here [E1-16, E3-29, E5-35].** Two of the three determinants are ticked.

### Honesty — binary, permanent, filings-based **[E5-16]**, each matter dated to when it became PUBLIC

**No disqualifier found, and that is the whole claim — not a finding that the managers are
honest [E5-17].** What was searched and what was found:
- **Auditor's opinion, FY2025 (`0000051143-26-000010`):** unqualified on the statements **and**
  on internal control — *"the Company maintained, in all material respects, effective internal
  control over financial reporting as of December 31, 2025."* **No material weakness. No
  restatement found in any year read (FY2021, FY2022, FY2024, FY2025).**
- **One critical audit matter, and it is the right one:** *uncertain tax positions*, because of
  *"the significant judgment by management when estimating the uncertain tax positions."* This
  is the estimate-driven area **[E2-50]** points at, and it is named by the auditor rather than
  found by me.
- **Auditor tenure: PricewaterhouseCoopers or predecessors "since 1923" — 103 years.** The
  corpus supplies no tenure rule and I am not inventing one. It is recorded because **[E5-32]**
  is on the shelf: Salomon's invented daily plug was signed by the largest audit firm in the
  country for twelve years, and *"audited does not mean true."* The cross-checks in this run
  exist for that reason.
- **Legal and regulatory:** the contingencies note says recorded liabilities for claims *"were
  not material to the Consolidated Financial Statements"* in each of 2023, 2024 and 2025. The
  one named action is an ERISA class action over joint-and-survivor annuity calculations, filed
  2022-06-02, dismissed with prejudice 2024-04-04, vacated and remanded 2025-04-03, settled and
  dismissed with prejudice **2025-12-11** with *"no material financial impact."* Environmental
  CERCLA matters, ordinary-course. **Searched and NOT found in FY2021, FY2022 or FY2025: any SEC
  enforcement matter, subpoena, investigation of revenue recognition, or grand-jury matter.**
- **[E5-22]'s calibration applied:** penalty size is not seriousness in either direction. There
  is no penalty here to mis-size, and *"they didn't act when they learned"* has nothing to
  attach to.

### STEP 2 — THE FLAGS. Each is a prompt to read, never a verdict **[E5-36]**

- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, and it fires exactly where the
      CGNX ruling said to look.** The word EBITDA does not appear in the FY2025 10-K or the
      Annual Report. It appears **eight times in the furnished Q2 2026 earnings release**
      (`0000051143-26-000077`, EX-99.1), which lists *"adjusted EBITDA"* and *"adjusted EBITDA
      margin"* among its non-GAAP measures and carries **two** reconciliations — *"GAAP NET
      INCOME TO ADJUSTED EBITDA RECONCILIATION"* and *"GAAP OPERATING CASH FLOW TO ADJUSTED
      EBITDA RECONCILIATION."* **Adjusted EBITDA margin 27.8% in Q2 2026 against a GAAP pre-tax
      income margin of 14.4%** — the measure is nearly double the filed one. Adjusted EBITDA
      appears five times in the Q4 2024 and Q4 2025 releases and eight times in the 2026
      releases, so **the practice is not new and it is intensifying.** [E4-29]'s mechanism
      **[E5-41]** — depreciation is *"reverse float"*, money already spent — applies with less
      force at IBM than at a capital-heavy filer, because IBM's real renewal spend is R&D
      charged above the line rather than depreciation; but the reader is still being handed a
      margin twice the filed one, and **the reason it is twice the filed one is $2,166M of
      acquired-intangible amortisation plus $2,042M of interest on the debt that bought the
      intangibles.** Deleting both is precisely what [E4-29] objects to.
- [x] **Trumpeted earnings projections / growth targets [E4-22] third flag — FIRES, and the
      guidance culture is continuous [E5-30].** IBM gives full-year revenue-growth and
      free-cash-flow guidance **every quarter**, in the furnished release. The trail, read from
      the filings rather than summarised:
      | date | guidance given | ledger |
      |---|---|---|
      | 2025-01-29 (`0000051143-25-000005`) | FY2025: *"constant currency revenue growth of at least 5 percent"*; *"about $13.5 billion in free cash flow"* | **[E3-48]** |
      | outturn, FY2025 | 6.1% constant-currency growth; **$14,734M** free cash flow | **BEATEN, both legs** |
      | 2026-01-28 (`0000051143-26-000004`) | FY2026: *"more than 5 percent"*; free cash flow *"increase by about $1 billion"* | |
      | 2026-04-22 (`0000051143-26-000036`) | *"continues to expect more than 5 percent"* | reaffirmed |
      | 2026-07-22 (`0000051143-26-000077`) | *"We **now** expect constant currency revenue growth in the range of **four-to-five percent**"* | **CUT** |
      **[E3-48]'s prescribed action is to set the company's own past guidance against outturn,
      and Buffett's stated base rate is that nine projections in ten exist to justify a decided
      course.** IBM's record on this evidence is that it **beat** both legs of its FY2025
      guidance and **cut** the revenue leg of FY2026 in July while holding the cash leg. That is
      a better record than the base rate, and it is recorded as such. **[E5-30]** is still the
      live objection and it is about the *practice*, not this year's accuracy: *"once you start
      it, it's all over … forecasting earnings, I can't imagine anything more destructive"* — a
      guidance culture is a ratchet, and IBM is on it.
- [x] **Metric-switching [E2-49] — FIRES, on the proxy's own words.** The PSU programme for
      2023-2025 carried a **Relative Return on Invested Capital modifier** against the S&P 500
      and S&P 500 Information Technology medians. *"For the 2023-2025 program, the ROIC modifier
      was 0"* — it paid nothing. For 2025 grants the Committee *"updated the performance
      modifiers"* and replaced it with a **relative TSR modifier** against the S&P 500
      percentile ranking, **in the same year IBM delivered "a total shareholder return of
      approximately 40%"** (the proxy's own figure), and **widened the leverage range from
      0-150% to 0-200%, taking the maximum from 170% to 220% of target.** [E2-49]: *"Yardsticks
      seldom are discarded while yielding favorable readings. But when results deteriorate, most
      managers favor disposition of the yardstick rather than disposition of the manager."* The
      mitigation, stated fairly: the change was **announced in advance, in the proxy, with a
      stated reason** (*"to support the focus on delivering sustainable revenue growth and free
      cash flow"*), which is the candour case [E2-49] itself carves out — except that the stated
      reason explains the revenue and cash weightings and does not explain swapping a
      capital-return modifier for a share-price modifier.
- [x] **What pay vests on [E4-27] — and it vests on the company's own adjusted numbers.** *"Never,
      ever, think about something else when you should be thinking about the power of
      incentives."* The PSU score is *"a weighted average of the results against the targets of
      **revenue (40%), operating EPS (30%) and free cash flow (30%)**."* **Operating EPS is
      non-GAAP** — it excludes acquired-intangible amortisation, acquisition charges and
      non-operating retirement costs, i.e. exactly the $2,166M and the pension items. **Free cash
      flow is IBM's own definition**, which adds back the growth of the finance book: it turned
      $13,193M of filed operating cash into **$14,734M** in FY2025. So two of the three
      financial metrics that pay management are measures management defines, and the cash metric
      is *higher* than the audited line it is reconciled to. **The mitigation, and it is real:**
      the proxy states that the results *"adjust … operating EPS for any difference between
      actual and targeted share count"* — IBM deliberately neutralises the buyback effect on the
      EPS metric, which is the game **[E2-01]** exists to warn against, removed by the company
      itself. Both halves are recorded.
- [ ] **Weak accounting [E4-22] first flag — does NOT fire, and the pension is the test.** SBC is
      expensed and is in the cash-flow statement at $1,715M. Pension assumptions are not
      fanciful: the FY2025 weighted-average **expected long-term return on U.S. plan assets is
      5.50%**, against a 5.50% U.S. discount rate and a **5.34% 30-year Treasury — sixteen basis
      points above the long bond.** (Non-U.S. plans: 4.86% expected return, 3.61% discount rate.)
      For calibration inside this project, the HON run recorded 7.25% against a 5.25% bond — 200bp
      above — and KMB 76bp above. **IBM, which was once the standard example of pension-flattered
      earnings, is now the most conservative of the three.** Non-operating retirement-related
      income/(cost) was **−$65M in 2025** and +$39M in 2023: earnings are not being flattered by
      pension credit at all.
- [ ] **Unintelligible footnotes — does NOT fire.** The reverse: the segment reconciliation
      quantifies every bridge item separately (acquired-intangible amortisation, SBC, workforce
      rebalancing, net interest ex-Financing, divested businesses), the free-cash-flow definition
      is reconciled line by line to the GAAP statement on the same page, and the Financing
      segment gets its own balance sheet, receivable-allowance table and debt-to-equity ratio.
      This is the **[E2-26]** half-owner test and IBM passes it: a one-time item is quantified at
      every line rather than buried in an adjusted figure.
- [ ] **Serial share issuance [E5-15] — does NOT fire as issuance, but the direction of the count
      is a fact.** No equity offering. Shares outstanding **rose from 938,034,404 (2026-02-10
      cover) to 942,134,390 (2026-06-30 cover)** and the count has drifted up every year since
      buybacks stopped, on employee-plan issuance of roughly 11M shares a year. Proceeds from
      issuance of shares $710M in FY2025 against $1,018M of repurchases for tax withholding — so
      **net cash went out, not in**, and **[E2-52]** (dividends funded by issuance) does **not**
      fire: the $6,255M dividend is covered 2.1× by filed operating cash.
- [ ] **Filed-figure fraud tells [E4-30] — neither fires, and one had to be read rather than
      scored.** *Unnaturally smooth growth:* refuted outright. Net income ran $1,639M (2022),
      $7,502M (2023), $6,023M (2024), $10,593M (2025) — nothing smooth about it, and FY2022's
      collapse has a disclosed non-cash cause, the **$5.9bn pre-tax pension settlement charge**
      on the transfer of about $16bn of Qualified PPP obligations to Prudential and MetLife in
      September 2022. *Cash taxes as a share of reported pre-tax income:* 29.0% (2019), 87.6%
      (2020), 43.5% (2021), 161% (2022), **18.0% (2023), 29.7% (2024), 18.9% (2025)** — noisy,
      not falling, and the two low years have a **disclosed** cause the MD&A names: *"income tax
      benefits associated with the resolution of certain tax audit matters in 2025 and 2024."*
      The flag is a prompt; the prompt was read; the cause is in the filing.
- [ ] **The restructuring-charge distortion [E3-53, E5-33] — the prompt fires on the recurrence
      and IBM's treatment PASSES.** *"Workforce rebalancing charges"* appear **every year**:
      $435M (2023), $692M (2024), $653M (2025). A charge that recurs annually is not a
      restructuring, it is a cost of doing business — and IBM treats it as one: it is inside GAAP
      pre-tax income **and** inside operating (non-GAAP) earnings, which exclude only acquisition
      charges, intangible amortisation and non-operating retirement costs. **IBM never tells
      owners to ignore it**, which is precisely what [E5-33] demands.
- [ ] **Stock-price targeting [E3-50] — a prompt, not a finding.** The rTSR modifier introduced
      for 2025 grants ties up to 20 points of PSU payout to the share price's percentile against
      the S&P 500. It is a modifier and it is relative, not the *"highest stock price possible"*
      premise [E3-50] condemns, and it is the near-universal market practice — which makes it
      **[E2-30]**(4), *peer behaviour mindlessly imitated*, rather than [E3-50] proper.
- **The auditor's-eye test [E4-34], fourth question — period-shifting.** Nothing found that moves
      revenue or expense between periods. The one candidate is the sales-type-lease residual
      adjustment inside *"Other revenue"* (−$2M in 2025, disclosed and quantified as *"reductions
      in revenue for estimated residual value less related unearned income on sales-type leases,
      which reflects the z17 launch"*) — $2M on $67,535M, disclosed with its cause.

### STEP 3 — THE PRIMARY TEST **[E2-01]**, and the denominator is the whole point

> *"The primary test of managerial economic performance is the achievement of a high earnings
> rate on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not
> the achievement of consistent gains in earnings per share."*

**Return on equity, as reported, five years** (net income ÷ average IBM stockholders' equity;
equity from the filed balance sheets):

| year | net income | average equity | ROE |
|---|---|---|---|
| FY2021 | $5,743M | $19,749M | 29.1% |
| FY2022 | $1,639M | $20,423M | **8.0%** |
| FY2023 | $7,502M | $22,239M | 33.7% |
| FY2024 | $6,023M | $24,920M | 24.2% |
| FY2025 | $10,593M | $29,978M | **35.3%** |
| five-year mean | | | **26.1%** |

**And the series is unusable as written, for the reason [E2-01] itself names — "without undue
leverage" — and the reason [E2-43] names.** The denominator is held down by **$170,605M of
treasury stock** and the numerator is held up by debt: tangible equity is **negative $46,368M**.
**[E2-43]** requires unleveraged net tangible assets with the goodwill wedge separate, and the
honest statement of it is: **$67,717M of goodwill and $11,391M of other intangibles against
$32,740M of total equity.** So:
- On **[E2-73]**'s denominator — judge the operators by the return on the underlying assets, not
  on what was paid — pre-tax income from continuing operations of $10,328M on tangible assets of
  $72,772M is **14.2%**, and on the tangible *operating* asset base (excluding $14.5bn of cash and
  securities, $7,544M of prepaid pension assets and $8,610M of deferred taxes) it is far higher
  still, because the operating business runs on almost no tangible capital.
- The two statements together are the truth about IBM's returns: **the operating business earns
  very well on the tangible capital it uses, and the $67.7bn spent to assemble it earns nothing
  in the accounting at all.** A reader shown only the 35% ROE is being shown three decades of
  buybacks.

**The half-owner test [E2-26]: PASS.** Every bridge item is quantified separately; the
free-cash-flow definition is stated in words and reconciled to the GAAP line on the same page;
the Financing segment is disclosed as a lender with its own leverage ratio. I would want to know
all of this if the positions were reversed, and I am told it.

**[E3-59]'s two yardsticks.** *(1) How well do they run the business, against the hand they were
dealt and against competitors' reports?* The hand was a shrinking services conglomerate; the
record since 2021 is **industrial operating cash from $11.1bn (FY2022) to $16.4bn (FY2025), +48%**,
gross margin from 54.0% to 58.2%, and *"$4.5 billion in annual run-rate savings since 2023"*.
Against the competitor row, growth is last of eleven and margins are mid-pack. That is competent
operating management of a difficult hand. *(2) How well do they treat their owners?* The dividend
has been paid every quarter since 1916 and is covered twice; the reporting passes the half-owner
test; and the buyback question below is the one real charge.

### The institutional imperative — score all four **[E2-30]**

- [ ] **resists any change in current direction** — no. The opposite: Kyndryl spun, Watson Health
      sold, The Weather Company sold, QRadar SaaS assets sold, six businesses bought. Whatever
      else this is, it is not inertia.
- [x] **projects/acquisitions materialise to soak up available funds** — **fires, and the
      arithmetic is in the filings.** IBM suspended buybacks *"at the time of the Red Hat
      acquisition closing"* with a stated purpose: *"In order to reduce this debt and return to
      target leverage ratios within a couple of years."* It did de-lever — total debt $73.0bn
      mid-2019 to **$51,703M at 2021-12-31** — and then **re-levered, to $61,260M at 2025-12-31
      and $62.0bn at 2026-06-30**, spending **$22,306M of cash on acquisitions over FY2021-FY2025**
      and $10,480M more in H1 2026. Seven years after the buyback was suspended to cut debt, debt
      is higher than when the de-leveraging finished and **the buyback has never resumed.**
- [x] **staff studies produced to justify the leader's craving** — **recorded as a prompt, not a
      finding, and the honest label is that I cannot see inside the process.** What is visible is
      the pattern: three new multi-billion commitments announced in 2026 alone — *"Lightwell is a
      $5 billion commitment"*, quantum at *"more than $10 billion … over the next five years"*,
      and *"a letter of intent to build Anderon, the world's first pure-play quantum wafer
      foundry"* with $1bn of CHIPS incentives and *"a $1 billion cash contribution by IBM"* —
      announced by a company whose revenue grew 4.12% a year over five years. **[E3-58]** is the
      sharper id here: capital allocation is the CEO's number-one job and CEOs are neither trained
      nor selected for it.
- [x] **peer behaviour mindlessly imitated** — fires mildly: quantum, agentic AI, the rTSR
      modifier, and *"Forward Deployed Engineers"* (a job title borrowed from another company's
      playbook), all arriving on the industry's schedule.

### Capital allocation — the two buyback conditions **[E5-08]**, and the third **[E4-31]**

- **(1) Ample funds for operations and liquidity?** **Marginally.** FY2025 operating cash
  $13,193M against a $6,255M dividend and $1,617M of (c) leaves about $5.3bn; but liquidity at
  2026-06-30 was **$8.2bn, down $6.3bn in six months**, against $6,424M of short-term debt at
  year-end. IBM also has *"committed global credit facilities"* of $10.0bn — and **[E5-39]**
  says bank lines are not counted: *"We will never be dependent on the kindness of strangers."*
  On the corpus's standard IBM's liquidity is thin for its size, and that is a real answer to
  condition (1), not an excuse for failing condition (2).
- **(2) Repurchases at a material discount to conservatively calculated intrinsic value?**
  **NOT TESTED BY MANAGEMENT AT ALL, because there have been no repurchases to test.**
  **$0 of open-market buybacks in FY2020 through FY2025** — the last was $1,361M in FY2019 —
  after **$125bn** spent between FY2007 and FY2019 ($18,828M in 2007 alone, $15,375M in 2010,
  $13,859M in 2013). The only "repurchases" since are **$1,018M of share withholding for
  employee taxes**, which is payroll, not capital allocation.
- **(3) [E4-31]'s third condition — was the register given what it needs to estimate value?**
  Substantially yes on the consolidated business; **no on the franchise**, because Transaction
  Processing and IBM Z are not separately reported for profit or units.

**→ CAPITAL-ALLOCATION FLAG, and it is a two-sided one, stated with the humility clause.**
- The charge under **[E2-51]**: *"A manager who consistently turns his back on repurchases, when
  these clearly are in the interests of owners, reveals more than he knows of his motivations."*
  Six consecutive years of zero repurchase while **$22.3bn went to acquisitions and $30.3bn to
  dividends** is a revealed preference for buying other people's businesses over buying its own.
  **[E5-24]**: *"what is smart at one price is dumb at another"* — and IBM's own history is the
  proof, because the $125bn spent FY2007-FY2019 was spent at prices that produced the negative
  tangible equity above.
- The defence, stated properly: on **my own** Q5 arithmetic below, IBM is **not** at a material
  discount — the honest expectancy is 4.4%-5.7% against a ~10% floor — so **condition (2) is not
  met and a buyback would be the wrong use of the money.** A management that declines to buy its
  own stock when its stock is not cheap is obeying [E5-08], not defying it. The real charge is
  narrower and survives: the acquisitions were made anyway, and **[E5-42]** says quality is the
  capital the business needs while the investment depends on *"how much we pay for that in the
  end"* — $1.81 of acquisition cash per $1 of added annual revenue is a price, and it is high.
- **[E4-13]'s humility clause applies in full:** this rests on my own IV range, and *"they also
  know a whole lot more about them than I do."* **The flag binds POSITION SIZE, never the
  discount rate** — and here there is no position to size, because the file closed at Q2.
- **[E3-54]'s retention test is uninformative here and I say so rather than scoring it.** Over
  FY2021-FY2025 IBM earned $31,500M and paid $30,259M of dividends, so **about $1.2bn was
  retained** — the test asks for $1 of market value per $1 retained, and against $1.2bn almost
  any market-value change passes. The real allocation question is not retention; it is that the
  **acquisitions were funded by debt and disposals while essentially all of earnings went out as
  dividends.** **[E2-60]** is the id: where leverage rises to fund the payout, (c) was
  understated. Tested — and it does **not** hold: filed operating cash covers the dividend 2.1×,
  and the debt went to acquisitions, not to the dividend. **Shape #5, the self-liquidating
  distribution, is refused on the arithmetic.**
- **[E4-39]'s rare-positive tell:** searched. **No candid acquisition post-mortem found** — no
  filing revisits Red Hat, Apptio, Turbonomic, HashiCorp or the Software AG assets against the
  announcement case. That is the ordinary case (*"almost never witnessed"*), so it earns nothing
  either way.

### Candor — and this is where IBM is genuinely unusual

**[E2-72]** requires the stewardship report to come from the CEO, not a staff specialist. On
**2026-07-14, eight days before the quarter's results were released**, IBM furnished an 8-K
containing *"Arvind Krishna's Letter to IBM Investors"* with preliminary figures and this:

> *"I want to spend some time explaining what we experienced in the quarter that led to the
> Software and Infrastructure performance shortfall … **These conditions require our teams to
> execute perfectly, and this quarter we faltered. We did not adapt and move quickly enough, and
> numerous large deals failed to close on the timelines we expected, driving the majority of our
> shortfall. These are not excuses, but they are realities.**"*

That is **[E2-57]**'s test — *"'except for' should be excised from the lexicon … the real mistake
is not the act, but the actor"* — answered in the right direction, by name, ahead of the required
disclosure, with the external causes named (a customer capex reprioritisation toward memory and
servers, cybersecurity distraction) and then **explicitly subordinated to management's own
failure**. It is also **[E2-69]**'s direction test: a deviation from the normal reporting
timetable **toward** candour is not the weak-accounting flag.

**Against that, the same letter and the same release do three things a reader should see:** they
cut the revenue guidance while holding the cash guidance; they answer the shortfall with three new
multi-billion-dollar commitments; and they put *"adjusted EBITDA margin 27.8%"* in the exhibit
beside a 14.4% GAAP pre-tax margin. **Candour about the past quarter and promotion about the next
five years are not the same virtue.**

### Converging flags — **[E4-52]**, the lollapalooza, applied properly

*"Extreme consequences from confluences of psychological tendencies acting in favor of a
particular outcome."* **Five prompts fired: [E4-29] adjusted EBITDA; [E4-22]'s third flag with
[E5-30]'s ratchet; [E2-49] metric-switching; [E4-27] pay vesting on management-defined measures;
[E2-30](2) acquisitions soaking up the funds that used to buy stock.** Do they converge on one
outcome? **Partly, and the honest answer is that they converge on a NARRATIVE rather than on a
number.** Every one of them points the same way — *report the adjusted figure, target it, pay on
it, and buy the growth that makes it* — which is a reinforcing system, not a sum of five
independent prompts. **But the two tests that would turn a narrative into a misstatement both come
back clean**: the accounting is not weak (pension conservative, SBC expensed, restructuring never
excluded, clean ICFR), and the footnotes are unusually legible. **So [E4-52] is recorded as a
converging system of promotional incentives, not as an integrity finding.** **[E5-38]** is the
discipline here: a fired flag is not a venality finding, and people Buffett would trust with his
wallet *"would play games with any number that came to them."*

### THE GUARDRAIL — checked before the verdict

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The file closed at Q2 and a
      strong Q3 cannot repair it **[E2-37, E2-38, E3-39]**. *"A textile company that allocates
      capital brilliantly within its industry is a remarkable textile company — but not a
      remarkable business."*
- [x] **Key-person dependence is recorded at Q2, not here.** It was searched and **not found**:
      the mainframe moat does not require naming a CEO **[E4-23]**.
- [x] **Is a great manager the reason to act?** No, and the question does not arise. There is no
      excisable cancer **[E2-35, E2-36]** and no corporate Pygmalion on offer; there is a
      competent operator improving the margins of a slow-growing company.
- **[E5-45]'s ABCs are the live Q6 monitoring item and IBM is the corpus's own named example:**
      *"arrogance, bureaucracy and complacency. When these corporate cancers metastasize, even
      the strongest of companies can falter"* — **GM, IBM, Sears and U.S. Steel named**, whose
      *"one-time financial strength and their historical earning power proved no defense."* The
      corpus names IBM in that sentence. On the evidence read here the ABCs are **not** the
      present condition: the company sold four businesses, cut $4.5bn of run-rate cost, and its
      CEO published a letter saying he faltered. That is the opposite of complacency. It is
      carried to Q6 as the thing to watch, which is where [E5-45] belongs.
- **[E3-40]'s loss of focus is the sharper charge and it is live:** *"the management of a great
      company gets sidetracked and neglects its wonderful base business while purchasing other
      businesses that are so-so or worse … Loss of focus is what most worries Charlie and me."*
      IBM's base business — the mainframe complex — grew 2.3% and then fell 8%, while $22.3bn
      went to buying other businesses and three new multi-billion programmes were announced.
      **That is a Q2/Q6 finding, and it is recorded at Q2 as the direction test, not here as a
      compliment or an accusation.**

- **VERDICT: [x] IN — RECORDED, NOT GOVERNING**

*IN means **no disqualifier was found**. It is **not** a finding that the managers are honest —
*"sincerity and empathy can easily be faked"* **[E5-17]** — and **[E5-26]**'s calibration applies:
a decade of strong record preceded the Sokol failure, and *"it's generally a mistake to assume
that rationality is going to be perfect, even in very able people."* Five prompts fired and were
read; one capital-allocation flag is live and two-sided; the accounting and disclosure tests came
back cleaner than this project's average, and the pre-announcement letter of 2026-07-14 is one of
the better candour artifacts encountered in this queue. **IN never promotes, and this file is
already closed.***

"""
s = s[:i] + new + s[j:]
io.open(p, 'w', encoding='utf-8').write(s)
print('q3 written')
