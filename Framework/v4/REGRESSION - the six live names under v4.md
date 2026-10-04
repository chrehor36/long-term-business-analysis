# REGRESSION — the six live names under v4
**2026-08-26.** The third verification debt from the plan: v4 must reproduce the v3.1
conclusions, or every difference must be explained. All figures from `tools/run.py`,
sovereigns from the issuing authority.

## The opportunity set, ranked

There is no pass mark. Q5 ranks **[E4-21]**, and this is the ranking:

| # | | yield (3-yr mean, capex band) | its sovereign | **points over** |
|---|---|---|---|---|
| **1** | **HRB** | 9.15 – 9.83 % | 5.23 % USD | **+6.83 .. +7.54** |
| 2 | TBTC | 4.29 – 4.47 % | 5.23 % USD | +1.76 .. +1.95 |
| 3 | TJX | 2.78 – 3.28 % | 5.23 % USD | +0.19 .. +0.71 |
| 4 | ASML | 1.33 – 1.51 % | 3.70 % EUR | +0.19 .. +0.38 |
| 5 | V | 2.63 – 2.66 % | 5.23 % USD | +0.03 .. +0.05 |
| — | NCLTY | 4.60 % (D&A basis) | 4.04 % JPY | not an SEC filer — see below |

**H&R Block is roughly five points clear of everything else you own.** That was true under
v3.1 too, but it took two books, a whisper rule and a twelve-cell grid to see it. Here it
is one column.

## Reconciliation against v3.1

| | v3.1 | v4 | difference explained |
|---|---|---|---|
| TJX | 3.06 %, +0.8..+1.5 | 2.78–3.28 %, +0.19..+0.71 | v3.1 anchored the **current tier**; v4 uses a 3-year mean, which is lower for a grower. Same conclusion. |
| HRB | 10.50 %, +7.07 | 9.15–9.83 %, +6.83..+7.54 | same, and the band straddles the old point estimate |
| TBTC | 4.29 % | 4.29–4.47 % | **exact on the conservative end** |
| V | 2.84 %, +0.58 | 2.63–2.66 %, +0.03..+0.05 | 3-year mean again; V's owner earnings grew, so the mean sits below the current tier |
| ASML | 1.33–1.98 % | 1.33–1.51 % | **exact on the conservative end**; v4's band is tighter because it uses the mean rather than current-vs-mean |

**No verdict reversed. Every difference is the averaging window**, which v4 requires each
run to state rather than hardcode.

## What the deletions changed, honestly

**TBTC moved UP the ranking.** Under v3.1 it carried an invented **+2% micro/illiquidity
premium**, giving it a 7.19% hurdle it failed. v4 deleted the premium as unsourced, so
TBTC now ranks second on the raw number.

**This is the deletion doing exactly what was promised, and it cuts against comfort.**
The size premium was a real protection, and it is gone because it had no corpus basis. What
replaces it is not nothing: TBTC still has an unresolved succession question at Q3, its
owner earnings were near zero in four of six years before FY2024, and its price ran 35% in
40 days. **Those are Q1–Q4 findings, and under v4 they stop the run before Q5 is ever
reached.** The ranking above is what the arithmetic says; it is not a clearance, and TBTC
does not currently pass the questions that come first.

**ASML ranks fourth on a 1.33% yield** because growth carries it — the IRR sees what a
static yield cannot. That is the same mechanism that rescued Coca-Cola 1988, working on a
name where the price is nonetheless 1.4× the most generous value.

## NCLTY — the one that cannot use the pipeline

Nitori is not an SEC filer, so `tools/run.py` refuses it by design and names the route:
company IR site (English). That work was done manually on 2026-08-26 — the FY2025 and
FY2026 IFRS statements are committed to `Test Runs/_research 2026-08-26/`, giving owner
earnings of a stable **¥78–79B** on the D&A basis and a **4.60%** yield against a 4.04%
JPY sovereign.

**Still owed:** FY2024 on the same basis for a true three-year mean, share-based
compensation (not broken out on the face of the IFRS statements), and the Gate 2 competitor
row. Those are UNRESEARCHED with named artifacts, not UNKNOWABLE.

## What the screener refuses, and why that is right

Run across TJX, ROST, BURL, V, MA, HRB, INTU, ASML and TBTC, the screener ranked seven and
**refused two, reporting both rather than dropping them**:

- **ASML — `CURRENCY_MISMATCH earnings EUR vs quote USD — refused, not converted.`**
  This is the ATLKY bug class caught in the act: a USD market cap over home-currency
  earnings once produced a false 19% yield. The fix is to pass the home listing
  (`--quote ASML.AS`), which is data routing, not conversion.
- **V — `NO_SHARE_COUNT_IN_XBRL`.** Visa tags diluted shares dimensionally by share class,
  so no flat total exists. That is precisely why the count had to be read off the 10-Q
  cover by hand earlier today. The screener refuses rather than guessing.

A screen that silently dropped these two would have reported coverage it did not have.
