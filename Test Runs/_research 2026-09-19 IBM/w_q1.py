import io
p = 'Test Runs/2026-09-19 Run - IBM International Business Machines.md'
s = io.open(p, encoding='utf-8').read()
old = """## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: ____
- The scarce input this business controls: ____
- Will the fundamentals look broadly the same in ten years? ____
- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**"""
new = """## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** IBM is four unrelated businesses
filed as four reportable segments. FY2025, from the segment table in `0000051143-26-000010` /
`ibm-20251231_d2.htm`:

| segment | revenue | % of revenue | gross margin | segment profit | % of segment profit |
|---|---|---|---|---|---|
| Software | $29,962M | 44.4% | 83.5% | $9,920M | 60.6% |
| Consulting | $21,055M | 31.2% | 28.1% | $2,464M | 15.1% |
| Infrastructure | $15,718M | 23.3% | 58.6% | $3,458M | 21.1% |
| Financing | $737M | 1.1% | 45.3% | $521M | 3.2% |
| Other / divested | $63M | 0.1% | NM | — | — |
| **Total** | **$67,535M** | | **58.2%** | **$16,364M** | |

*Read the segment-profit column with a caveat the filing supplies: segment profit is stated
BEFORE stock-based compensation. The reconciliation in the segment note takes $1,685M of SBC
out of the $16,364M of "total reportable segment profit" to reach $10,328M of pre-tax income
from continuing operations, along with $2,166M of acquired-intangible amortisation, $653M of
workforce-rebalancing charges and $1,312M of non-Financing net interest. Every segment margin
quoted above is therefore flattered by stock pay the segments do not carry.*

**1. Software — $29,962M, and it is two different things.** Four disclosed lines: **Transaction
Processing $8,603M**, **Hybrid Cloud (Red Hat) $7,327M**, **Automation $7,733M**, **Data
$6,299M**.
- *Transaction Processing is the mainframe's own software stack* — the operating system,
  database and middleware that run only on IBM Z, licensed by installed capacity. Its revenue
  moves with how many MIPS customers install, which is why it grew 2.3% in FY2025 *"reflecting
  the benefit from our launch of IBM z17 in June 2025 and the strategic importance of this
  mission-critical software"* and fell **8%** in Q2 2026 when the z17 cycle rolled over. It is a
  toll on an installed base, not a product sold into a market.
- *Hybrid Cloud is Red Hat* — a paid subscription to a supported build of Linux, Kubernetes
  (OpenShift) and Ansible, every line of which is available free as source code. What the
  customer buys is indemnity, certification and support, not the code. Bought for **$34.8bn of
  cash on 2019-07-09** (the figure is IBM's own, in the FY2021 annual report). OpenShift ARR is
  disclosed at $1.9bn at year-end 2025, up more than 30%.
- *Automation and Data are a portfolio assembled by purchase* — HashiCorp (closed Q1 2025),
  StreamSets and webMethods from Software AG, Apptio, Turbonomic, and **Confluent, closed
  2026-03-17 for $11,268M of cash for the common stock plus $269M for equity awards** (10-Q
  `0000051143-26-000078`, note 5). Reported Software growth is therefore partly bought growth,
  and this run has to say which.
- Across Software, disclosed **annual recurring revenue $23.6bn** at year-end 2025 (up about
  $2bn), defined as the current quarter's recurring revenue multiplied by four, covering
  subscriptions, committed term licences, SaaS/PaaS and maintenance. Against $29,962M of Software
  revenue that is roughly 79% recurring and 21% transactional, and IBM's FY2024 discussion names
  both halves explicitly: *"growth in our high-value, recurring revenue base, as well as our
  transactional software revenue."*

**2. Consulting — $21,055M, 28.1% gross margin, 11.7% segment margin.** People's time, sold by
the hour or under fixed-price contracts, in two disclosed lines (Strategy and Technology
$11,537M, Intelligent Operations $9,518M). The economics are visible in the margin: of every
dollar of Consulting revenue, 72 cents is the cost of delivering it and about 88 cents is gone by
segment profit. The forward book is disclosed: **signings $21,757M in FY2025, DOWN 13.3% (14.7%
adjusted for currency)**; book-to-bill 1.03; backlog $31.9bn, up about $0.5bn.

**3. Infrastructure — $15,718M, 58.6% gross margin.** Hybrid Infrastructure $10,618M (IBM Z
mainframes plus Power and Storage) and Infrastructure Support $5,100M (the maintenance and
lifecycle contracts on the installed machines). This is a **product-cycle** business and the
filings show the cycle at both ends: **IBM Z revenue +51.7% in FY2025** on the June 2025 z17
launch, and **IBM Z revenue −42% in Q2 2026** in the release of 2026-07-22. Infrastructure
Support is flat (−0.1% in FY2025) — that is the annuity the hardware installs create.

**4. Financing — $737M of revenue, $521M of segment profit, and it is a bank.** $15,052M of
external net financing receivables ($13,192M client + $2,992M commercial, less $141M of
allowance) funded by **$15,093M of Financing segment debt "primarily comprised of intercompany
loans"**, at a disclosed **debt-to-equity ratio of 9.0 to 1** on $1,678M of equity. It earned
$705M of external interest income against $365M of interest expense on matched intercompany
loans. Its stated return on equity was **32.3%**, and the filing says why: it is *"after-tax
segment profit divided by the average of the ending equity for Financing for the last five
quarters"* — a deliberately thin equity base. This segment is separated again at Q4; it is named
here because a lender inside a technology company changes what the consolidated cash-flow
statement means.

**The scarce input this business controls.** It is **the installed base of IBM Z mainframes and
the software written for them.** Nothing else on the list is scarce in IBM's hands: Linux and
Kubernetes are other people's code; consulting skills are rented from the labour market every
year; Power and Storage compete against Dell, HPE and ODMs buying from the same suppliers; the
Automation and Data portfolios were bought, and could have been bought by someone else. The
mainframe is different for a reason the filing states plainly — *"mainframes handling 70% of the
world's transactional workflows (IBM IBV)"* — and z/OS runs on no other machine, so the switching
cost is the cost of rewriting the customer's application estate, not the cost of buying a
competitor's box. **Cited honestly: that 70% figure is IBM's own research arm (the Institute for
Business Value) quoted in IBM's own annual report. It is a self-cited statistic, not a
third-party measurement, and it is recorded as such rather than leaned on.**

**The size of the franchise, as far as the filing lets it be sized.** Transaction Processing
$8,603M + Infrastructure Support $5,100M + the IBM Z share of Hybrid Infrastructure $10,618M.
**IBM discloses IBM Z revenue in dollars nowhere** — only the percentage change, alongside
Distributed Infrastructure's −1.8% — so the split of $10,618M between IBM Z and Distributed
Infrastructure is in no filing. Treating Distributed Infrastructure as roughly flat in dollars
and IBM Z as the growth, the mainframe complex is somewhere around **$19bn to $22bn of the
$67.5bn, i.e. 28% to 33% of revenue**, and it carries more than its share of profit because
Transaction Processing sits inside an 83.5%-gross-margin segment. The remaining two thirds of
revenue — Consulting, Red Hat, Automation, Data, Distributed Infrastructure — is competed for.

**Will the fundamentals look broadly the same in ten years?** **Split answer, and the split is
the finding.**
- For the mainframe complex: **yes.** Installed bases of this kind decay slowly, the replacement
  cost is the customer's application estate rather than IBM's machine, and the filing shows the
  same architecture still being upgraded sixty-two years after System/360.
- For the other roughly 70% of revenue: **no**, and IBM says so itself. *"IBM is a globally
  integrated enterprise that participates in a highly competitive environment … we recognize
  hundreds of competitors worldwide and as we execute our hybrid cloud and AI strategy, **we are
  regularly exposed to new competitors**."* The portfolio that produced FY2025's Software growth
  contains four businesses bought in the last three years, and the 2026 releases name three new
  directions on top — Lightwell (*"a $5 billion commitment"*, July 2026), quantum (*"more than
  $10 billion … over the next five years"*), and a quantum wafer foundry with the U.S. Department
  of Commerce.

**VERDICT: [x] IN**

**Why IN and not UNKNOWABLE.** The test at Q1 is whether I can understand how the money is made
and *"how realistically [I] define what [I] don't know"* **[E3-31]**. Each of the four pieces is
legible from the filed segment disclosure: a toll on an installed base, a support subscription on
free software, a labour business with a disclosed signings and backlog series, a hardware cycle
with a disclosed launch date, and a captive lender with its own balance-sheet table. None of it
required months of study, so **[E4-46]** does not bite. The honest limits are recorded rather
than smoothed: IBM Z revenue in dollars is not disclosed anywhere; the 70%-of-transactions figure
is self-cited; and every segment margin is stated before stock pay.

**Nothing in this section is a compliment.** The durable part of the business is the minority of
revenue, and that is written down here at Q1 precisely so that Q2 cannot borrow the mainframe's
durability for the whole company. **[E4-26]** says to hunt disconfirming evidence hardest for the
favourite hypothesis, and the favourite hypothesis about IBM is the mainframe."""
assert old in s
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(s)
print('q1 written')
