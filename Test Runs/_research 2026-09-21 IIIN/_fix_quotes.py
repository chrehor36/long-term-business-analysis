# -*- coding: utf-8 -*-
"""Post-write corrections to the IIIN run file.

Two jobs, both required by the house rules rather than by taste:

1. PRIME RULE 1. Four places quoted the FRAMEWORK's compression of a ledger row rather than
   the row's own `quote_verbatim`. The brief warns about exactly this: "the framework's own
   compression of a ledger quote is not a licence to repeat it as a quote." Each is replaced
   with the ledger text, with elisions marked and OCR/transcript artifacts flagged.
2. The standing no-em-dash rule. Every em dash in this file is replaced with " - ", which is
   what the BELFB run of the same day did. Checked first: no verbatim quotation in this file
   contains an em dash, so nothing quoted changes.
"""
import io

p = "Test Runs/2026-09-21 Run - IIIN Insteel Industries.md"
t = io.open(p, encoding='utf-8').read()

subs = []

# ---- 1. E2-59: the blockquote was the framework's gloss, not the ledger row. -------------
old_e259 = '''> *"administered pricing … pre-1970s insurers "could legally price their way to profitability
> even in the face of substantial over-capacity"* — but **the moat belongs to the regime**, and
> *"That day is gone"* is how it ends. **[E2-59]**'''
new_e259 = '''> "Businesses in industries with both substantial over-capacity and a "commodity" product
> (undifferentiated in any customer-important way by factors such as performance, appearance,
> service support, etc.) are prime candidates for profit troubles. **These may be escaped, true,
> if prices or costs are administered in some manner and thereby insulated at least partially
> from normal market forces. This administration can be carried out (a) legally through
> government intervention** (until recently, this category included pricing for truckers and
> deposit costs for financial institutions), (b) illegally through collusion, or (c)
> "extra- legally" through OPEC-style foreign cartelization" - **[E2-59]**, 1982 letter
>
> *(quoted from the ledger row's own `quote_verbatim`, not from the framework's summary of it.
> The row carries the source's spacing artifact "extra- legally", reproduced rather than
> smoothed, PRIME RULE 1.)*'''
subs.append((old_e259, new_e259))

# ---- 2. E4-41: "normalize the mean DOWN for luck" is framework prose, not the row. --------
old_e441 = '''**[E4-41]** requires exactly this: *"normalize the mean DOWN for luck"*, favourable
  exogenous breaks *"named and removed before the mean is trusted."*'''
new_e441 = '''**[E4-41]** is the corpus's own instance of doing exactly this, and it is
  quoted from the ledger row rather than from the framework's gloss of it: *"We've yet to see a
  pro-forma presentation disclosing that audited earnings were somewhat high. So let's make a
  little history: Last year, on a pro-forma basis, Berkshire had lower earnings than those we
  actually reported. That is true because two favorable factors aided our reported figures."*
  The favourable factor here is the 2021-22 steel spike and its unwind.'''
subs.append((old_e441, new_e441))

# ---- 3. E2-67: the "so you can … judge" form is the framework's, not the row's. -----------
old_e267 = '''Berkshire published its reserving errors
  *"so you can … judge whether we may have some systemic bias"*'''
new_e267 = '''Berkshire published its reserving errors so that readers could
  *"judge whether we may have some systemic bias that should make you wary of our current and
  future figures"*'''
subs.append((old_e267, new_e267))

# ---- 4. E4-46: the framework smooths a transcript artifact. Quote the row. ----------------
old_e446 = '''- **The five-minute test [E4-46]:** *"if we can't make a decision in five minutes, we can't make
  it in five months. We're not going to learn enough in the following five months to make up for
  the fact that we went in deficient in the first place."*'''
new_e446 = '''- **The five-minute test [E4-46]:** *"if we can't make a decision in five minutes, we can't make
  it in five months. You know, we're not going to learn enough in the **followings** five months
  to make up for the fact that we went in deficient in the first place."*
  **Transcript artifact flagged, not smoothed (PRIME RULE 1):** the ledger row reads
  *"followings five months"*, and `Framework/THE FRAMEWORK v4.md` quotes the same passage as
  *"following five months"*, dropping the *"You know,"* as well. **The corpus wins (PRIME RULE 2),
  so this run quotes the row. Reported as a finding, not repaired by this run, because the
  framework is a governing document and editing one to match a run is the wrong direction.**'''
subs.append((old_e446, new_e446))

# ---- 5. E4-55: the row carries OCR damage; reproduce and flag it. -------------------------
old_e455 = '''> Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — *"a
> serious reverse, not likely to disappear in some 'bounce back' effect."* **[E4-55]**'''
new_e455 = '''> "In 2006, Precision Steel's service center volume was 46 million pounds, down from 69 million
> pounds sold as recently as 1999. **This decline in physical volume is a serious reverse, not
> likely to disappear in some ""bounce back'' e?ect.** Nor do we expect another sharp rise in
> prices like the approximately 40% rise that recently occurred, holding dollar volume roughly
> level despite a precipitous drop in physical volume." - **[E4-55]**, 2006 Wesco letter
>
> *(The ledger row carries OCR damage: doubled opening quotation marks and a replacement
> character in "e?ect". Reproduced, flagged, and not smoothed, PRIME RULE 1.)*'''
subs.append((old_e455, new_e455))

# ---- 6. E3-03: quote the row's own opening words. -----------------------------------------
old_e303 = '''**The definition, applied line by line.** *A franchise is a product or service that "(1) is
needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not
subject to price regulation."* **[E3-03]**'''
new_e303 = '''**The definition, applied line by line, quoted from the ledger row:** *"An economic franchise
arises from a product or service that: (1) is needed or desired; (2) is thought by its customers
to have no close substitute and; (3) is not subject to price regulation. The existence of all
three conditions will be demonstrated by a company's ability to regularly price its product or
service aggressively and thereby to earn high rates of return on capital."* **[E3-03]**, 1991
letter. **Note the row's second sentence, which the test above is usually read without: the
three conditions are demonstrated by regular aggressive pricing and high returns on capital.
Insteel's filings evidence neither.**'''
subs.append((old_e303, new_e303))

missing = []
for old, new in subs:
    if old not in t:
        missing.append(old.split('\n')[0][:70])
    else:
        t = t.replace(old, new, 1)

# ---- the em-dash sweep --------------------------------------------------------------------
before = t.count('—')
t = t.replace('—', '-')

io.open(p, 'w', encoding='utf-8').write(t)
print("quote fixes applied:", len(subs) - len(missing), "of", len(subs))
if missing:
    print("NOT FOUND (fix by hand):")
    for m in missing:
        print("   ", m)
print("em dashes replaced:", before)
