# SECTOR METHOD v5 — insurers and float-bearing holding companies
**In force from 2026-10-05**, adopted with `Framework/THE FRAMEWORK v5.md` as its method for insurers and float-bearing
holding companies. This document replaces the v4 method, now kept at
`Framework/ARCHIVE - v4.x (superseded 2026-10-05)/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`.
Built only from rows of `principle_ledger_v5.csv` (the scope directive in the framework's standard). The case, its tests and
the decision are `Framework/v5/CASE 2026-10-05 - a v5 sector method for insurers and float companies, for the operator's approval.md`,
`Framework/v5/TEST - the v5 sector method on MKL, PREREGISTRATION.md` and
`Framework/v5/TEST - the v5 sector method on MKL, RESULTS and the comparison.md`.

**How to read this document.** The second section gives the rows problem by problem; the third is the method as a run executes
it; the fourth confesses the conventions and records the absences; the fifth says what the method cannot do. **The amendment at the
end is in force and supersedes the steps and conventions it names** (gross or net of float, the float construction, the
accident-year basis, the tax basis of the second component, and the operating-income step). The case's section numbering is kept so that its
tests' references still point where they did.

**Open items, from the repeat test of 2026-10-05** (`Framework/v5/tests/SM MKL 2 - the amended sector method.md`), each to be
settled by a written amendment before it is relied on, none of which changed that test's box: whether the deductions of the
first construction (premiums receivable, deferred acquisition costs) survive the amended float construction, or the filer's own
published float definition governs where there is one; the cut-off for an immature accident year; pairing loss-development tables
with re-segmented calendar results; debt carried by its interest while float is deducted at face; the growth convention on a
depressed base year; amortization of acquired intangibles; the floor for a value built of two components; underwriting with no
development table; the bracket check where segment invested assets are not reported; and the order in which the castle exhibit
is computed. Until settled, a run states its choice on each and labels it.

## 2. What the v5 rows say, problem by problem

The rows were found by a pre-filtered list of the ledger rows that mention insurance, float, underwriting, reserves and
related words, every quote then read in full in the CSV, and by further searches of the quote text named under each problem.

### 2.1 What float is, and why it inflates operating cash flow

The rows define float as money received before it is paid out, and never as earnings.

> "To oversimplify the matter somewhat, the total of the funds prepaid by policyholders and the funds earmarked for incurred-but-not-yet-paid claims is called "the float." [...] Our cost of float is determined by our underwriting loss or profit." **[L1993-009]**, 1993 letter

> "To begin with, float is money we hold but don't own.  In an insurance operation, float arises because premiums are received before losses are paid." **[L1996-008]**, 1996 letter

> "You have liabilities here and you have assets over here, and the liability side finances the asset side. [...] But float is another item that’s a liability but hasn’t cost us anything. And it can’t disappear in a hurry. And it finances the asset side in the same way as stockholders’ equity." **[M2023-004]**, 2023 meeting

> "Anybody can generate float. I mean, if we gave our managers a goal of generating 5 billion of float next year, they could do it in a minute, you know, and we would be paying the price for decades to come. You can write dumb insurance policies, you know. There’s an unlimited market for dumb insurance policies. And they’re very pleasant, because the first day the premium comes in and that’s the last time you see any new money. From then on, it’s all going out." **[M2001-030]**, 2001 meeting

> "Float, per se, is not a blessing. We can show you many insurance companies that thought it was wonderful to generate float. And they have lost so much money in underwriting that they’d be better off if they’d never heard of the insurance business." **[M1996-023]**, 1996 meeting

**What they settle.** Float is a liability that funds assets **[M2023-004]**, **[L1996-008]**; growing it is easy and can be
ruinous **[M2001-030]**; its worth turns on its cost **[M1996-023]**. So the premium that arrives before the loss is paid is
funding, not earnings, and a cash figure that counts it as earnings counts a borrowing as income.

**The row that pulls the other way, carried OPEN.** Buffett once named Berkshire's cash flow as including the growth in
float:

> "There’s a lot of deferred tax that’s attributable to unrealized appreciation in securities. [...] That isn’t really cash that’s available. It’s just an absence of cash that’s going to be paid out until we sell the securities. [...] But overall, I think of, primarily, the cash flow of Berkshire as a practical matter relating to our net income plus our increase in float, assuming we have an increase." **[M2016-058]**, 2016 meeting

He says it of Berkshire, whose float the rows describe as having "cost us virtually nothing over the years" **[L1995-016]**,
and conditions it, "assuming we have an increase". This case does not settle the pull: it carries M2016-058 OPEN against
the reading above, and the method below lets float growth enter value only where its cost and its permanence are shown
(section 3, Q7).

**Absent.** An owner-earnings figure computed for an insurer: no instance found in the v5 ledger, by a search of the quote
text for "cash flow" together with "insur", and none for the phrase "owner earnings" (the v5 framework records the same
absence of the phrase, with **[M2022-003]**, **[M2018-045]**, **[L2015-004]** nearest).

### 2.2 Maintenance capital has no referent; what an insurer's capital is for

A securities portfolio has no plant to keep up. The rows give the insurer's capital a different job: it stands behind the
promises.

> "Property casualty insurance is kind of a rare business because you need capital as a guarantee fund that you will keep your promises, but you can use it to buy other low capital-intensive businesses." **[M2025-049]**, 2025 meeting

> "And to a certain extent, because insurance uses the kind of assets we would like to own anyway, our insurance business doesn’t really take capital. It requires having capital available." **[M2020-041]**, 2020 meeting

> "if you’re really prepared to pay your claims under any circumstances that come along in the next hundred years, you have to have so much capital in the business that it’s not a very good business." **[M2019-025]**, 2019 meeting

> "Any company's level of profitability is determined by three items:  (1) what its assets earn; (2) what its liabilities cost; and (3) its utilization of "leverage" - that is, the degree to which its assets are funded by liabilities rather than by equity." **[L1995-015]**, 1995 letter

> "And the growth in capital has been greater than the growth rate in premium volume and in invested assets, so that achieving the same success on underwriting and achieving the same success on investments will produce a lower return on capital unless they buy in stock, which they have done fairly significantly." **[M1995-069]**, 1995 meeting

**What they settle.** For an insurer, Q3's question, how much capital must go in, is answered by the capital that must stand
available behind the promises **[M2025-049]**, **[M2020-041]**, and its return is read by the three items of L1995-015:
what the assets earn, what the liabilities (float and debt) cost, and how far the assets are funded by liabilities
**[L1995-015]**. Capital that grows faster than the business can use lowers the return **[M1995-069]**.

**Absent.** A required amount of capital per dollar of premium: no instance found in the v5 ledger as a rule, by a search of
the quote text for "capital" together with "premium". The nearest is Munger's description of Berkshire, "four times as much
stockholder capital behind each dollar of premium value. Four times normal." **[M2023-013]**, which describes one company
and states no requirement.

### 2.3 The cash test inverts

The current method's central warning, that an insolvent insurer stays flush with cash long after it has run out of net
worth, rests on a passage outside the v5 scope. **No instance found in the v5 ledger** of that statement, by a search of the
quote text for "walking dead", "broke but flush", "run out of cash", and "cash flow" with "insur".

The substance is in the rows in other words: the cash comes first and the proof comes later; struggling insurers under-state
their losses; easy early years end in ruin.

> "it’s the curse of the insurance business — it’s also one of the benefits of it — is that people hand you a lot of money for writing out a little piece of paper. And what you put on that piece of paper is enormously important. But the money that’s coming in that seems so easy can tempt you into doing very, very foolish things." **[M2003-031]**, 2003 meeting

> "you get the money at the start, you know, and then you find out whether you’ve done something stupid later on" **[M2024-036]**, 2024 meeting

> "Major underreserving is common in cases of companies struggling for survival. In effect, insurance accounting is a self-graded exam, in that the insurer gives some figures to its auditing firm and generally doesn't get an argument." **[L2001-022]**, 2001 letter

> "If you annually give 5-for-1 odds against its occurrence that year, you will have many more winning years than losers. Indeed, you may go a straight six, seven or more years without loss. You also will eventually go broke." **[L1993-011]**, 1993 letter

> "Faced with the prospect of stagnating or declining earnings, the monoline managers turned to ever-riskier propositions." **[L2008-014]**, 2008 letter

And what replaces cash on hand as the test of an insurer's liquidity is whether anyone can demand money from it suddenly:

> "The nature of our insurance contracts is such that we can never be subject to immediate demands for sums that are large compared to our cash resources. (In this respect, property-casualty insurance differs in an important way from certain forms of life insurance.)" **[L2013-003]**, 2013 letter

> "we will not write insurance contracts that give policyholders the right to cash out at their option. Many life insurance products contain redemption features that make them susceptible to a "run" in times of extreme panic." **[L2014-024]**, 2014 letter

> "we’ll always want to have a significant level of liquidity, relative to any kind of payment pattern that we see for a good length of time." **[M2002-073]**, 2002 meeting

**What they settle.** Cash received is not evidence of health in an insurer **[M2003-031]**, **[M2024-036]**, **[L1993-011]**;
the reserve is where a weak insurer hides its condition **[L2001-022]**; and liquidity is read as the absence of sudden demands
**[L2013-003]**, **[L2014-024]** and liquidity against the payment pattern **[M2002-073]**, not as cash on hand.

### 2.4 The two components of value, and the double count

The rows give the method directly. Berkshire's value is estimated from two figures, investments per share and the earnings of
everything other than investments, with a third element, a judgment, beside them.

> "And we measure our progress, to some extent, by the figures in both columns of that table, one of which shows the investments per share. And the other shows the operating earnings from everything other than investments." **[M1997-141]**, 1997 meeting

> "In our last three annual reports, we furnished you a table that we regard as central to estimating Berkshire's intrinsic value. In the updated version of that table, which follows, we trace our two key components of value [...] In effect, the columns show how Berkshire would look if it were split into two parts, with one entity holding our investments and the other operating all of our businesses and bearing all corporate costs." **[L1998-002]**, 1998 letter

> "There are two statistics, however, that are of real importance. The first is the amount of investments (including cash and cash-equivalents) that we own on a per-share basis. [...] Using our funds for these purchases has both slowed our growth in investments and accelerated our gains in pre-tax earnings from non-insurance businesses, the second yardstick we use." **[L2006-002]**, 2006 letter

> "There is a third, more subjective, element to an intrinsic value calculation that can be either positive or negative: the efficacy with which retained earnings will be deployed in the future. [...] This "what-will-they-do-with-the-money" factor must always be evaluated along with the "what-do-we-have-now" calculation in order for us, or anybody, to arrive at a sensible estimate of a company's intrinsic value." **[L2010-002]**, 2010 letter

**Where underwriting goes.** The first form of the second column left underwriting out, and the rows say why; a later
meeting says it may be put in, normalized.

> "We did not do that when we initially introduced Berkshire's two quantitative pillars of valuation because our insurance results were then heavily influenced by catastrophe coverages. If the wind didn't blow and the earth didn't shake, we made large profits. But a mega-catastrophe would produce red ink. In order to be conservative then in stating our business earnings, we consistently assumed that underwriting would break even over time and ignored any of its gains or losses in our annual calculation of the second factor of value." **[L2015-002]**, 2015 letter

> "I would say it’s conservative to assume break-even underwriting. [...] we could lose significant money in underwriting this year, and we expect to lose significant money in underwriting, you know, maybe every fifth year, every tenth year, whatever it might be. But I think you’re right in saying it would not be inappropriate to include some normalized underwriting profit in addition to the calculation that I made in the annual report." **[M2011-051]**, 2011 meeting

> "Now, what we really hope over time is more or less to break even on the underwriting of insurance. So when you see a significant profit like last year or underwriting profit this year, just look at that as kind of the good side of what will later be an offset to it in a way of an underwriting loss." **[M2007-001]**, 2007 meeting

**The double count, found in the rows.** The current method's rule against double counting rested on a sentence, in a letter
outside the scope, that excludes dividends and interest from the second factor as a double count of value. **No instance found in the v5 ledger** of that sentence, by a search of the quote text for
"double" (every hit read; none concerns the two components) and for "dividends and interest". The rule does not need it.
L1998-002 builds the split so that one entity holds the investments and the other operates the businesses **[L1998-002]**,
and M1997-141 names the second column "the operating earnings from everything other than investments" **[M1997-141]**: the
income the investments produce belongs to the first column by construction, and counted in the second it is counted twice.
And L1993-009 makes the underwriting result and the cost of float one quantity, "Our cost of float is determined by our
underwriting loss or profit" **[L1993-009]**: whichever column carries it, it is carried once. The MKL run of 2026-09-02
found that the first draft of the current method charged it twice; the v5 rows forbid the same thing in their own words.

**A bracket the rows supply.** The rows also place an insurer's value against its net worth and its float:

> "But basically, I would say that GEICO is worth — has an intrinsic value — that’s greater — significantly greater — than the sum of its net worth and its float. Now, I wouldn’t say that about some of our other insurance businesses. But that’s for two reasons. One is, I think it’s quite rational to assume a significant underwriting profit at GEICO over the next decade or two decades, and I think it’s likely that it will have significant growth." **[M2012-033]**, 2012 meeting

> "If float is both costless and long-enduring, the true value of this liability is far lower than the accounting liability." **[L2011-005]**, 2011 letter

> "If an insurance business produces large and sustained underwriting losses, any goodwill asset attributable to it should be deemed valueless, whatever its original cost." **[L2011-006]**, 2011 letter

> "An insurance business is profitable over time if its cost of float is less than the cost the company would otherwise incur to obtain funds.  But the business has a negative value if the cost of its float is higher than market rates for money." **[L1994-025]**, 1994 letter

Read together: an insurance operation is worth more than its net worth plus its float only on a sustained underwriting profit
and growth **[M2012-033]**; float is worth more than its accounting liability only if it is both costless and long-enduring
**[L2011-005]**; and an insurer whose float costs more than market money is worth less than nothing on that account
**[L1994-025]**, **[L2011-006]**.

### 2.5 Materiality: how far the investments lean on the float

The current method found, at WTM and MKL, that the share of the portfolio funded by float, and the size of the portfolio
against equity, decide how much the valuation depends on the float's quality. Its rule for that was confessed as its own. The
v5 rows supply the principle: whether float may be treated like equity depends on the equity standing behind it.

> "Now, if we had a very limited amount of equity and a very large amount of float, we would impose a lot of restrictions on ourselves as to how we would do it, because we would want to be very sure that we were in a position to distribute that float, in effect, to policyholders, or claimants, or whatever it may be at the time that was appropriate. But we have so much net worth that, in effect, that float is just about as useful to us as equity money." **[M1995-035]**, 1995 meeting

> "We don’t look at insurance float 100 percent the same as we would look at equity, but we’ve looked at it a good bit, you know. It’s largely tantamount to equity because we’ve had so much equity, we could afford to do it that way." **[M2001-053]**, 2001 meeting

> "The float is really available for anything that we feel is the most intelligent at any given time. And the reason we can say that, and other insurance companies can’t say that, is because we have an incredible abundance of capital, plus other streams of earning power which are unrelated to the insurance business." **[M2000-132]**, 2000 meeting

> "But it is not set aside in some little compartment like people like to think. Now, no other insurance company could do it. But they can’t think that way. They aren’t even used to thinking that way. But they can’t think that way because they don’t have our balance sheet." **[M2023-012]**, 2023 meeting

> "You can get in a lot of trouble with leverage. I mean, it’s — you start creating $20 of assets, or something like that. You know, for every dollar of equity, you better be right." **[M2009-058]**, 2009 meeting

**What they settle.** The ratio of float to equity, and of investments to equity, measure how far the company can treat its
float as Berkshire treats its own **[M1995-035]**, **[M2001-053]**, **[M2000-132]**; Berkshire says in terms that no other insurer
can **[M2023-012]**. This is the in-scope ground for the current method's warning against reading smaller insurers as small
Berkshires: the method transfers, the licence to treat float as equity does not. The rows name no threshold for either
ratio: no instance found in the v5 ledger, by a search of the quote text for "leverage" (every hit read) and for "ratio of".

### 2.6 Reserve development as the candor test

The v5 rows are richer here than the v4 ledger was. They say what development is, why it runs one way, and what its movement
around a sale of stock tells.

> ""Loss development" suggests to investors that some natural, uncontrollable event has occurred in the current year, and "reserve strengthening" implies that adequate amounts have been further buttressed. The truth, however, is that management made an error in estimation that in turn produced an error in the earnings previously reported. The losses didn't "develop" � they were there all along." **[L2001-021]**, 2001 letter (the replacement character is in the row)

> "The natural tendency of most casualty-insurance managers is to underreserve, and they must have a particular mindset � which, it may surprise you, has nothing to do with actuarial expertise � if they are to overcome this devastating bias." **[L2002-006]**, 2002 letter (the replacement characters are in the row)

> "We should point out again that in any given year a company writing long-tail insurance (coverages giving rise to claims that are often settled many years after the loss-causing event takes place) can report almost any earnings that the CEO desires." **[L2003-015]**, 2003 letter

> "if you take the insurance business, you know, the biggest single element that is very difficult to evaluate, even if you own the company, is the loss and loss adjustment expense reserve. And that has a huge impact on reported earnings of any given period. And the shorter the period, the more the impact can be from just small changes in assumptions." **[M2005-067]**, 2005 meeting

> "you would see companies that, when they were offering stock to the public, you know, the year or two before that, the reserves would be down very suspiciously, and — you know, then — or even when they were selling them to other insurance companies, if they were buying in stock they might be building the reserves." **[M2013-085]**, 2013 meeting

> "In all of our acquisitions, we have left the loss reserve figures exactly as we found them. [...] When deals occur in which liabilities are increased immediately and substantially, simple logic says that at least one of those virtues must have been lacking -- or, alternatively, that the acquirer is laying the groundwork for future infusions of "earnings."" **[L1998-034]**, 1998 letter

> "And, you know, Gen Re had some problems in the mid-’80s, when everybody did, and they went to discounting their worker’s comp reserves. And they — you know, it was a quick fix, but it’s like heroin." **[M2003-103]**, 2003 meeting

> "Let’s assume at the start of the year I asked everybody to submit budgets and then I went on Wall Street and preached a bunch of numbers. Even if their compensation didn’t depend on it, the managers would feel, you know, we don’t want to let Warren down on this. So, you know, we’ll take an optimistic view of reserves, and that’s easy to do, at the end of the quarter" **[M2005-036]**, 2005 meeting

> "The idea of feeding in losses — you’ve got a liability." **[M2021-037]**, 2021 meeting

The rows also say which way the errors run: surprises "are never symmetrical. They’re all bad." **[M1997-079]**; "You are
lucky if you get one that is pleasant for every ten that go the other way." **[L2005-008]**; "most catastrophe losses develop
upward" **[M2011-001]**; claims that "pop up 10 or 20 or 30 years later" come "big and they can come late" **[M1999-098]**.
They oppose discounting property-casualty reserves **[L2001-024]**, **[M2005-111]**. And they give the standard a good
reserver keeps: "we will try to be both consistent and conservative in our approach" **[R1996-015]**; "the one overriding
principle is that we hope, and our plan is, to reserve conservatively" **[M2012-005]**; "we tell no managers of any of our
insurance operations what numbers we expect from them" **[M2020-029]**.

**What they settle.** Development is an error in earnings already reported **[L2001-021]**, so a run restates the past
underwriting results by it before it averages them. Its direction is the candor test: the natural bias is to under-reserve
**[L2002-006]**, a struggling insurer is the least likely to grade itself hard **[L2001-022]**, and reserves that move with a
sale or purchase of stock **[M2013-085]**, reserves reset at an acquisition **[L1998-034]**, discounting **[M2003-103]**, and
published targets **[M2005-036]** are the tells.

**Absent.** The statutory loss-development schedule by name: no instance found in the v5 ledger, by a search of the quote
text for "Schedule P" and "triangle". The rows require the reading (above); the document a US filer supplies for it is ours
to name (section 4, C3).

### 2.7 The cost of float, and the rate it is set against

> "An insurance business has value if its cost of float over time is less than the cost the company would otherwise incur to obtain funds. But the business is a lemon if its cost of float is higher than market rates for money." **[L1997-011]**, 1997 letter

> "Only by making an analysis that incorporates both underwriting results and the current risk-free earnings obtainable from float can one evaluate the true economics of the business that a property-casualty insurer writes. [...] The value of float funds - in effect, their transfer price as they move from the insurance operation to the investment operation - should be determined simply by the risk-free, long-term rate of interest." **[L1993-010]**, 1993 letter

> "Some years back, float costing, say, 4% was tolerable because government bonds yielded twice as much, and stocks prospectively offered still loftier returns. Today, fat returns are nowhere to be found (at least we can't find them) and short-term funds earn less than 2%. Under these conditions, each of our insurance operations, save one, must deliver an underwriting profit if it is to be judged a good business." **[L2001-005]**, 2001 letter

> "So, we would be willing to take on float, obviously, at costs only modestly below the Treasury rate, if that was the only way we could get that float, and it didn’t impede our ability to get other float, you know, at zero cost or something." **[M2000-121]**, 2000 meeting

> "Because loss costs must be estimated, insurers have enormous latitude in figuring their underwriting results, and that makes it very difficult for investors to calculate a company's true cost of float." **[L1997-012]**, 1997 letter

> "But whereas the deposits of a bank, it’s quite easy to calculate the approximate cost, in the case of the float that the insurance company has, you don’t really know what the cost of that float is until all your policies and losses — policies have expired and your losses have all been settled. Well, that’s forever, in some cases. So, you’re only making an estimate, as you go along, of what that float is costing." **[M1996-022]**, 1996 meeting

> "The key determinants are: (1) the amount of float that the business generates; (2) its cost; and (3) most important of all, the long-term outlook for both of these factors." **[L1998-015]**, 1998 letter

> "It’s a good question to, you know, what is the permanence of the float? What is the cost of the float? What’s the likelihood of it growing? Could it actually run off?" **[M2002-006]**, 2002 meeting

**What they settle.** The cost of float is the underwriting loss, a profit being a negative cost **[L1993-009]**, **[L1996-008]**,
**[M1998-029]**. It is judged against what money would otherwise cost **[L1997-011]**, **[L1994-025]**, and the rows name that
rate: "the risk-free, long-term rate of interest" **[L1993-010]**, the same long government rate Q7 uses. Whether a given
cost is tolerable moves with that rate **[L2001-005]**, **[M2000-121]**, **[M2012-110]**. The figure is an estimate that a single
year cannot give **[L1997-012]**, **[M1996-022]**; a single good year proves nothing **[L1993-011]**, and Buffett would "take
something off all of the good years" of catastrophe business **[M1997-018]**. What matters most is the outlook, judged by
permanence, cost, growth and the chance of run-off **[L1998-015]**, **[M2002-006]**, **[M1998-030]**, and the history is not to
be extrapolated **[M1994-005]**, **[M2012-058]**. Growth in float adds value only at low cost: "If that becomes too high,
growth in float becomes a curse rather than a blessing." **[L1998-016]**; also **[M2000-122]**, **[M1997-017]**, **[M1996-051]**.

**The cost of float is a judgment, not a term to add.** Every row above uses it to judge the business: "a lemon"
**[L1997-011]**, "a negative value" **[L1994-025]**, "a curse rather than a blessing" **[L1998-016]**. None adds it to a sum.
The MKL ruling, that the cost of float is diagnostic and not additive, therefore stands on v5 rows: L1993-009 makes it the
underwriting result, which the second component already carries **[L1993-009]**, **[L2015-002]**.

**Absent.** The loss-to-float ratio as a named measure: no instance found in the v5 ledger, by a search of the quote text
for "loss/float" and "cost of funds". The rows give the quantity (underwriting loss as the cost of float) and the yardstick
(the long risk-free rate); dividing the one by the float to compare it with the other is ours (section 4, C3).

### 2.8 The deferred-tax liability

> "Neither item, of course, is equity; these are real liabilities. But they are liabilities without covenants or due dates attached to them. In effect, they give us the benefit of debt - an ability to have more assets working for us - but saddle us with none of its drawbacks." **[R1996-010]**, 1996 annual report (the two items, by the row's concept note and its source lines, are deferred tax liabilities and float)

> "Between deferred taxes and our insurance float, we have some 12 billion or so on the liability side that we think will be a very low cost. And that’s — doesn’t show as an asset, but it can be quite valuable." **[M1996-012]**, 1996 meeting

> "There’s a lot of deferred tax that’s attributable to unrealized appreciation in securities. [...] That isn’t really cash that’s available. It’s just an absence of cash that’s going to be paid out until we sell the securities." **[M2016-058]**, 2016 meeting

> "I think the equities in the insurance company offsetting shareholders equity in the company are really not worth the full market value because they’re locked away in a high-tax system." **[M2017-077]**, 2017 meeting (Munger)

> "But I don’t think I would look at that as a hidden form of equity. I’d rather have the deferred taxes than not have them, but it’s not meaningful there. [...] We do — the float from the insurance business, we regard as a terrific asset. The deferred tax liability is a plus, but it’s not — it’s not a big asset." **[M2015-030]**, 2015 meeting

> "Overall, cash held at our insurers is a very valuable asset, but one slightly less valuable to us than is cash held at the parent level." **[L2016-009]**, 2016 letter

**What they settle.** The tax on unrealized gains is owed, and the securities are worth less than their market value to the
owner by it **[M2016-058]**, **[M2017-077]**: the first component is counted after that tax. The deferral is a real liability
with the benefit of debt and none of its drawbacks **[R1996-010]**, a plus but "not a big asset" and not "a hidden form of
equity" **[M2015-030]**. And money inside an insurer is worth slightly less than money at the parent **[L2016-009]**.

**Absent.** A valuation of the deferred-tax liability as an interest-free loan, worth something between face and zero: no
instance found in the v5 ledger, by a search of the quote text for "interest-free" and "interest free" (two hits, both on
executive options) and for "deferred" (every hit read). The current method's figure for it came from the Wesco letters, which
are outside the scope. It is dropped; the deferral's value enters only as the stated judgment the rows allow (section 3, Q7).

### 2.9 Companies that are partly insurers

> "Each of these has vastly different balance sheet and income account characteristics. Therefore, lumping them together, as is done in standard financial statements, impedes analysis. So we'll present them as four separate businesses, which is how Charlie and I view them." **[L2008-005]**, 2008 letter

> "Investments usually play second fiddle to the insurance business at most companies that are in the insurance business. We look at them as being of equal importance. [...] And we run them as two distinct businesses." **[M1997-087]**, 1997 meeting

> "GEICO has entirely different characteristics than the super-cat business. They both call themselves insurance. They both develop float. But in economic terms and in terms of competitive strengths and that sort of thing, they’re two very different businesses." **[M1997-088]**, 1997 meeting

> "In the 11 years through 2009, the company reported an aggregate pre-tax loss of $157 million, a figure that was far understated since borrowing costs at NetJets were heavily subsidized by its free use of Berkshire's credit." **[L2010-010]**, 2010 letter

**What they settle.** Businesses with different balance sheets are read separately **[L2008-005]**, the investing and the
underwriting as two businesses **[M1997-087]**, and each insurance unit on its own economics **[M1997-088]**; a unit's results
are read as if it stood without the parent's credit **[L2010-010]**. The rows give no test for when a company is "an insurer"
rather than a company that owns one; the current method's finding at WTM ("a holding company that owns a float-bearing
business, not a float-bearing company") is this project's own record and becomes a CONVENTION below (section 4, C2 and C9).

### 2.10 The castle question comes first, and it is harder here

> "Insurers sell a non-proprietary piece of paper containing a non-proprietary promise. Anyone can copy anyone else's product. No installed base, key patents, critical real estate or natural resource position protects an insurer's competitive position. Typically, brands do not mean much either. The critical variables, therefore, are managerial brains, discipline and integrity." **[L2003-014]**, 2003 letter

> "When property/casualty companies are judged by their cost of float, very few stack up as satisfactory businesses. [...] Indeed, many of the biggest and best-known companies regularly deliver mediocre results. What counts in this business is underwriting discipline." **[L2001-006]**, 2001 letter (the elided passage carries a replacement character in the row)

> "The casualty insurance business, by its nature, is not a terribly good business. You have to be in the top 10 percent, really, to do at all well in it, and I think we’re very lucky." **[M2012-059]**, 2012 meeting (Munger)

> "I would say that our ability to sell insurance at a price that’s considerably lower than most of our competitors, evidenced by the fact that when people call us, they shift to us, and, at the same time, earn a significant underwriting profit, indicates that our selection process is working quite well." **[M2013-006]**, 2013 meeting

Also **[L2004-003]** (a commodity-like product; "Think airline seats"), **[M2000-072]**, **[M2003-009]**, **[M1996-023]**,
**[L2014-043]** (Munger: "Ordinarily, a casualty insurance business is a producer of mediocre results, even when very well
managed."), and the franchises the rows allow: "specialized talents, on terrific distribution systems, managerial know-how,
even the ability to use the float effectively" **[M1999-112]**, and the claimant's "peace of mind" that "that check will be in
the mail 50 years from now" **[M1996-088]**.

**What they settle.** Q2 is harder for an insurer, not easier: the product is a commodity **[L2003-014]**, **[L2004-003]**,
and the evidence of a castle is a cost of float that stays low over years **[L2001-006]**, with prices below competitors'
while the underwriting still profits **[M2013-006]**. Nothing in this method lightens Q2, and a run that reaches the
components before closing Q2 has broken the order.

### 2.11 Concentration, aggregation and the counterparty

The current method's warning that concentration is licensed only by exceptional loss-absorption rests on a passage outside
the scope. Its substance is in the rows of 2.5 above **[M2023-012]**, **[M1995-035]**, and Q9 of v5 already carries the
aggregation rows. The insurer's own forms:

> "If our insurance operations are to generate low-cost float over time, they must: (a) underwrite with unwavering discipline; (b) reserve conservatively; and (c) avoid an aggregation of exposures that would allow a supposedly "impossible" incident to threaten their solvency." **[L2002-004]**, 2002 letter

> "But the question is, what is one event? [...] But the problem is if that one event turns out to affect a thousand policies and somehow they’re all linked together in some way, and the courts decide that way, you’ve written something that, in no way we’re getting the proper price for and could break the company." **[M2024-021]**, 2024 meeting

> "These insurers don't issue single huge-limit policies as we do, but their small policies, in aggregate, can create a risk of staggering size.  The "big one" would blow right through the reinsurance covers of some of these insurers, exposing them to uncapped losses that could threaten their survival." **[L1995-018]**, 1995 letter

> ""Cheap" reinsurance is a fool's bargain: When an insurer lays out money today in exchange for a reinsurer's promise to pay a decade or two later, it's dangerous � and possibly life-threatening � for the insurer to deal with any but the strongest reinsurer around." **[L2002-007]**, 2002 letter (the replacement character is in the row)

> "And if you really think about a worst-case situation, the reinsurance — that’s insurance you buy from other people, as an insurance company, to protect you against the extreme losses, among other things — that reinsurance probably — could likely be — not good at all." **[M2019-025]**, 2019 meeting

> "Some insurers may try to mitigate their loss of revenue by buying lower-quality bonds or non-liquid "alternative" investments promising higher yields. But those are dangerous games and activities that most institutions are ill-equipped to play." **[L2019-002]**, 2019 letter

Also **[L2001-008]** (no aggregation from a single event or related events), **[M1997-078]** (an unwitting super-cat exposure),
**[L1994-028]** (several catastrophes in one year, with losses elsewhere), **[L2001-018]** (the stress test of every participant in
the chain), **[L2008-009]** ("A promise is no better than the person or institution making it."), **[L2000-005]** (never a policy
that lacked a cap), **[M2007-072]** and **[M2021-036]** (courts and legislators stretch the words after a mass loss).

### 2.12 One company earning in several currencies

The current method left this OPEN at WTM. The v5 rows do not close it: "currency might be important, but we don’t think it’s
knowable" **[M2000-043]**; Berkshire takes foreign earnings "unhedged" and converts them "at current rates to dollars at some
time in the future" **[M2008-043]**; and of an insurer's liabilities, "we do not have lots of liabilities around the world in
other currencies which are only matched by assets in U.S. dollars" **[M2003-087]**. A rule for the discount rate of a company
that earns in several currencies: no instance found in the v5 ledger, by a search of the quote text for "currenc" (every hit
read). Operator rule 5 of `Framework/OPERATOR-PROTOCOL.md` (the sovereign for the earnings currency) binds as before; the
mismatch test of M2003-087 becomes a Q9 question below.

---

## 3. The proposed method, as a run would execute it under v5

**Nothing here changes the order or the boxes.** Q1 and Q2 are asked as written, then this method changes what Q3, Q4, Q7
and Q9 measure for an insurer, and adds the questions of 2.6 and 2.11 to the reading. Every step cites its rows or is labelled
CONVENTION, confessed in section 4.

### Stage zero: is it an insurer, a holding company that owns one, or neither?

1. **Split first.** Read every segment the filer reports with its own balance sheet as a separate business **[L2008-005]**,
   **[L1998-002]**. Each non-insurance segment runs the ordinary v5 questions; the insurance part runs this method; the whole
   is understood only if each part that matters is (the holding-company CONVENTION of Q1, with **[M2023-031]** OPEN against
   it). A unit that borrows on the parent's credit is read as if it stood alone **[L2010-010]**.
2. **Measure the float.** The rows define it as "the funds prepaid by policyholders and the funds earmarked for
   incurred-but-not-yet-paid claims" **[L1993-009]**. CONVENTION C1 gives the construction from the filed balance sheet.
3. **State two ratios, float to investments and investments to equity**, and say what they imply: how far the portfolio is
   funded by money that is not the owners' **[L1995-015]**, and how far the company could treat its float as equity
   **[M1995-035]**, **[M2001-053]**. CONVENTION C2: neither ratio is a threshold and neither closes the file; a low float share
   means the answer lives in the operating businesses and the equity-funded portfolio, not in the float.
4. **Out of this method's scope** (CONVENTION C10): asset managers whose earnings are fees, and life or annuity books with
   cash-out features, which the rows set apart from property-casualty float **[L2013-003]**, **[L2014-024]**. A run meeting one
   says so and does not stretch the method.

### Q1: can I understand it?

An insurer is understood when both sides of its balance sheet can be read: the liability side (the reserves, their
development history and the exposures written) and the asset side (the portfolio). The rows say the reserve is "the biggest
single element that is very difficult to evaluate, even if you own the company" **[M2005-067]**, that statistics on auto
drivers are "much more valid" than estimates of something "like asbestos liability" **[M2005-069]**, and that a long-tail
writer "can report almost any earnings that the CEO desires" **[L2003-015]**. CONVENTION C8 states the reading: a book whose
reserve adequacy cannot be judged from the filer's own development history closes TOO HARD; if the history is published and
unread, the cause is WORK; if the deciding question is the adequacy of reserves on claims that "pop up 10 or 20 or 30 years
later" **[M1999-098]** and the history cannot settle it, the cause is NATURE.

### Q2: why is the castle still standing?

Unchanged in form. The evidence the rows accept for an insurer is a cost of float kept low over years **[L2001-006]**,
**[M1996-023]**, prices below competitors' with an underwriting profit **[M2013-006]**, or one of the franchises of
**[M1999-112]**, **[M1996-088]**, read against the commodity character of the product **[L2003-014]**, **[L2004-003]**. The cost of
float measured under Q4 below is the main exhibit; it is read here as a judgment of the business **[L1997-011]**,
**[L1998-015]**.

### Q3: how much capital must go in?

1. For the insurance part there is no maintenance capital expenditure to estimate. The capital that must go in is the capital
   that must stand behind the promises **[M2025-049]**, **[M2020-041]**; record it as the equity of the insurance part and its
   ratio to premiums written, stated, with no threshold (CONVENTION C2; nearest row **[M2023-013]**).
2. Read its return by the three items: what the assets earn, what the float and debt cost, and the leverage **[L1995-015]**.
   A return on equity raised by leverage is read as Q3's tests already require **[M2001-054]**, **[M1994-019]**.
3. Note whether capital is growing faster than the business can use it **[M1995-069]**.
4. The non-insurance parts answer Q3 as written.

### Q4: the cash figure, and whether the condition can be known

1. **Operating cash flow is not the insurer's cash figure.** The growth of float in it is funding, not earnings **[L1996-008]**,
   **[M2023-004]**, **[M2001-030]**. (M2016-058 OPEN, section 2.1.)
2. **Investment income comes out of the operating figure**: dividends, interest and realized or unrealized gains belong to
   the first component **[L1998-002]**, **[M1997-141]**; net income swung by securities gains is ignored **[L2010-017]**,
   **[M2023-001]**, **[M2014-002]**.
3. **The underwriting result is taken over a period of years, on developed figures.** Each year's result is restated by the
   later development of that year's reserves, because development is "an error in the earnings previously reported"
   **[L2001-021]**; a single year is never used, in either direction **[M2005-067]**, **[L1993-011]**, **[M1997-018]**,
   **[L1997-012]**. The window is CONVENTION C3.
4. **Catastrophe losses stay in.** "Except for" figures are "deceptive nonsense" **[L2002-002]**; also **[M2018-024]**.
5. **The cost of float**: the developed average underwriting result over the window, against the average float, set beside
   the long government rate over the same years **[L1993-009]**, **[L1993-010]**, **[L1997-011]**. Report it as a judgment of the
   business, never as a term in the value (2.7). CONVENTION C3 confesses the ratio.
6. **The candor reading of the reserves.** State the direction of development across the window, its size against the
   underwriting result, and whether the filer names it as an error **[L2001-021]**. Then look for the tells: reserves that
   move around a sale or purchase of stock **[M2013-085]**, reserves reset at an acquisition **[L1998-034]**, discounting
   **[M2003-103]**, **[L2001-024]**, published targets **[M2005-036]**, smoothing **[R1996-015]**, **[L1994-027]**, and the condition
   of a company struggling to survive **[L2001-022]**. Under Q4's two-tell CONVENTION, adverse development alone is a weighing;
   with a second tell it is the suspicion that makes Q4's STOP **[M1995-063]**, **[M2003-029]**.
7. **Liquidity** is read as the absence of sudden demands **[L2013-003]**, **[L2014-024]** and as liquid assets against the
   payment pattern **[M2002-073]**, never as cash on hand (2.3); the question itself is applied at Q9.

### Q5 and Q6: what the rows ask of an insurer's managers

Q5 and Q6 are asked as written. The rows put their insurer-specific forms: the four disciplines, the fourth being "The
willingness to walk away if the appropriate premium can't be obtained" **[L2010-008]**; the three rules **[L2002-004]**; whether
the managers are free of pressure for premium growth **[M2013-031]**, **[L2004-005]**, **[M2004-077]**; pay tied to "float growth
and cost of float" **[L1999-004]** and to each side's own results **[L1996-020]**; and the one disqualifying trait, optimism
**[L2023-012]**. At Q6 the third element of value is the retention test as v5 states it **[R1995-009]**, **[R2009-002]**,
**[M2011-072]**, and, for a buyback, the rows add that "repurchases automatically increase the amount of "float" per share"
**[L2021-008]**, which is worth something only where the float is "of the right sort".

### Q7: what is it worth?

The value is the sum of two components and a stated judgment **[M1997-141]**, **[L1998-002]**, **[L2006-002]**, **[L2010-002]**,
inside Q7's definition, rate, range and floor as written.

1. **Component 1, the investments.** Investments including cash and cash equivalents **[L2006-002]**, at the filed fair value,
   less the deferred tax on their unrealized gains **[M2016-058]**, **[M2017-077]**, less any investments held in a finance
   operation and offset by its borrowings, and attributable to the owners (CONVENTION C4). Cash and securities held inside
   the insurer are noted as "slightly less valuable" than at the parent **[L2016-009]**, a stated judgment, not a number.
2. **Gross or net of float.** The first component is counted gross, all investments including those the float funds, only
   where the float passes both of the rows' conditions, "both costless and long-enduring" **[L2011-005]**: its developed cost
   over the window is below the long government rate **[L1994-025]**, **[L1993-010]**, and it is permanent, not running off and
   not open to sudden demands **[M2002-006]**, **[L2013-003]**. Otherwise it is counted net of the float, as if the float were
   a debt to be paid **[L2011-005]**. CONVENTION C5 gives the tests' form.
3. **Component 2, the operating earnings.** Pre-tax earnings from everything other than investments **[L2006-002]**,
   **[M1997-141]**, after all corporate costs **[L1998-002]** and the real costs Q4 names (interest, depreciation,
   amortization and all forms of compensation) **[L2021-003]**. The underwriting result enters here and nowhere else
   **[L2015-002]**, **[M2011-051]**.
4. **The two ends of the range.** The low end takes underwriting at the lesser of zero and its developed average; the high
   end at its developed average **[L2015-002]**, **[M2011-051]**, **[M2007-001]**. Component 2 is then carried by Q7's range
   CONVENTION (the averaging, the shown growth capped by Q3, the term, the long government rate) **[L2000-024]**,
   **[L1993-010]**. CONVENTION C6 confesses the ends.
5. **The double counts the rows forbid.** None of these is done: investment income in component 2 while the investments are
   in component 1 **[L1998-002]**, **[M1997-141]**; a cost-of-float charge beside an underwriting result already in component
   2, the two being one quantity **[L1993-009]**; float earnings at the long rate **[L1993-010]** added to component 2 while
   the investments are in component 1 (L1993-010's measure judges the business at Q2 and Q3; it is not a value term); the
   float added to net worth while the investments are also counted gross **[M2012-033]**; operating cash flow that includes
   float growth used as the earnings while the investments are counted (Q4 step 1).
6. **The bracket check** (CONVENTION C7). Set the value the components give the insurance part against its net worth and
   against its net worth plus its float. A value above net worth plus float needs M2012-033's two reasons stated, "a
   significant underwriting profit" and "significant growth" **[M2012-033]**; a value above net worth while the cost of float
   exceeds the long rate contradicts **[L1994-025]** and **[L2011-006]** and is resolved before Q7 closes.
7. **The third element**, up or down, written as a judgment with its rows, never silently **[L2010-002]**.
8. **The floor and the boxes.** Q7's floor CONVENTION and its two closes (TOO HARD when the range is too wide, OUT when the
   price does not clear it) apply unchanged **[M2003-149]**, **[L2000-025]**, **[M2009-005]**. An insurer whose value hangs on
   the float's quality will often show a wide range; that is the finding, and a wide range is not cured by a bigger discount
   **[M2007-022]**.

### Q8: unchanged.

### Q9: could it ruin us?

The ten tests of Q9 apply. For an insurer they are read through these rows:

1. **What is one event**: the aggregation of small policies, the related events, the courts' reading of linked claims
   **[M2024-021]**, **[L2001-008]**, **[L1995-018]**, **[M1997-078]**, **[M2003-034]**.
2. **The worst case against the capital**: several catastrophes in one year with trouble elsewhere **[L1994-028]**; the capital
   behind the promises **[M1995-035]**, **[M2019-025]**; the licence to concentrate does not transfer **[M2023-012]**.
3. **Whose promise it rests on**: the reinsurers and the whole chain, stress-tested in a bad economy **[L2002-007]**,
   **[L2001-018]**, **[L2008-009]**, **[M2003-084]**; in the worst case the reinsurance may be "not good at all" **[M2019-025]**.
4. **Sudden demands**: cash-out features, collateral calls, short maturities **[L2014-024]**, **[L2013-003]**.
5. **Uncapped and stretched liabilities**: policies without a cap **[L2000-005]**, **[M2001-032]**; wording stretched after a
   mass loss **[M2007-072]**, **[M2021-036]**.
6. **The portfolio**: reaching for yield with float **[L2019-002]**; how freely the float may be invested, set by the equity
   behind it **[M1995-035]**, **[M1996-094]**.
7. **Currency mismatch**: liabilities in one currency matched only by assets in another **[M2003-087]**.
8. If the risk cannot be known from the disclosures, it is set aside, not weighed **[L2002-018]**, as Q9's test 10 says.

---

## 4. Confessed conventions, and absences recorded

### Conventions (ours, each with its rationale)

- **CONVENTION C1, the float construction.** Float is constructed from the filed balance sheet as loss and loss-adjustment
  reserves plus unearned premiums, less reinsurance recoverables, premiums receivable and deferred acquisition costs.
  Rationale: L1993-009 names the two funds that make float, the prepaid premiums and the reserved claims **[L1993-009]**; the
  deductions remove the assets already standing against them, so that the figure is money held but not owned
  **[L1996-008]**. No row gives the recipe. It is the recipe the WTM run built and the MKL run tested (this project's own
  record); a run shows its arithmetic.
- **CONVENTION C2, the two ratios and no threshold.** Float to investments and investments to equity are computed and
  stated; the insurance part's equity to its premiums is stated at Q3. Rationale: the rows say the use of float depends on
  the equity behind it **[M1995-035]**, **[M2001-053]** and name no figure; a threshold would be ours and would close files the
  rows do not close.
- **CONVENTION C3, the window, the document and the ratio.** The underwriting result, its development and the cost of float
  are taken over the longest run of years the filer publishes, stated, on figures restated by later development; for a US
  property-casualty filer the development history is read from the statutory loss-development schedule or the filing's
  claims-development tables; the cost of float is expressed as the developed underwriting loss divided by the average float
  and set beside the average long government rate of the same years. Rationale: the rows require a run of years in
  substance **[M1996-022]**, **[L1997-012]**, **[M2005-067]**, the developed figures **[L2001-021]** and the long risk-free rate as
  the yardstick **[L1993-010]**, and name neither a number of years, nor a document, nor the ratio; stating the window lets the
  next reader reproduce it.
- **CONVENTION C4, the investments' measure.** Component 1 takes the filed fair value, less the filed deferred tax on
  unrealized gains, less investments in a finance operation that its own borrowings offset, and net of the share belonging to
  minority holders, and states gross against net of any item the run is unsure of. Rationale: the rows require the tax
  deduction **[M2016-058]**, **[M2017-077]** and give no source or other adjustment; the filed figure is the primary document
  (operator rule 4), and the finance-operation and minority deductions keep money that is not the owners' out of their
  column. No instance found in the v5 ledger of minority interests in a valuation, by a search of the quote text for
  "minority" and "noncontrolling".
- **CONVENTION C5, the tests for counting the investments gross.** The condition costless is read as a developed cost of float over the
  window below the long government rate over the same years; "long-enduring" as float that has not shrunk across the window
  and is not open to sudden demands. Rationale: L2011-005 names the two conditions **[L2011-005]**, L1994-025 and L1993-010
  give the rate a cost is judged against **[L1994-025]**, **[L1993-010]**, and M2002-006 asks about run-off **[M2002-006]**; the
  operational forms are ours.
- **CONVENTION C6, underwriting at the two ends.** The low end takes the lesser of zero and the developed average
  underwriting result, the high end the developed average. Rationale: the rows call break-even the conservative assumption
  and allow a normalized profit **[M2011-051]**, **[L2015-002]**; where the average is a loss, break-even is not conservative, so
  the loss is taken at both ends.
- **CONVENTION C7, the bracket check.** Net worth and net worth plus float are set beside the components' value of the
  insurance part as a check, not a value. Rationale: M2012-033, L2011-005, L2011-006 and L1994-025 relate an insurer's value to
  those two figures **[M2012-033]**, **[L2011-005]**, **[L2011-006]**, **[L1994-025]**; turning them into a check before Q7 closes
  is ours.
- **CONVENTION C8, the insurer's door at Q1 and the cause of TOO HARD.** An insurer is inside the circle when both sides of its
  balance sheet can be read, and the cause of a TOO HARD is assigned as in section 3, Q1. Rationale: the reading follows the
  form of Q1's door for a bank and the rows on reserves **[M2005-067]**, **[M2005-069]**, **[L2003-015]**, **[M1999-098]**; the
  rows give no door for insurers in these words, and the assignment of WORK or NATURE is ours, as the labels themselves are in
  the v5 framework.
- **CONVENTION C9, when to split and when the method applies.** Every segment reported with its own balance sheet is split;
  the method applies to a part that carries float funding its investments, and the ordinary questions to the rest. Rationale:
  the rows require the split **[L2008-005]** and give no test of what makes a company "an insurer"; the WTM finding that a
  company can own a float-bearing business without being one is this project's own record.
- **CONVENTION C10, the scope.** Asset managers paid in fees, and life or annuity books with cash-out features, are outside the
  method. Rationale: the rows set life redemption features apart **[L2013-003]**, **[L2014-024]** and contain no method for either;
  stretching the method to cover them would invent one.
- **CONVENTION C11, currency, carried as practice until decided.** A company earning in several currencies is run at the
  sovereign of its reporting currency, with the exposure by currency stated and the choice disclosed as unresolved. Rationale:
  operator rule 5 asks for the earnings currency and the rows give no rule for several **[M2000-043]**, **[M2008-043]**; this is
  what the WTM run did, and it is a disclosure, not an answer.

### Absences recorded

| what is absent | nearest rows | the search |
|---|---|---|
| The statement that an insolvent insurer stays flush with cash after its net worth is gone | **[L2001-022]**, **[M2003-031]**, **[M2024-036]**, **[L1993-011]**, **[L2013-003]** | quote text for "walking dead", "broke but flush", "run out of cash", "cash flow" with "insur" |
| The sentence excluding dividends and interest from the second component as a double count | **[L1998-002]**, **[M1997-141]**, **[L1993-009]** | quote text for "double" (every hit read) and "dividends and interest" |
| The loss-to-float ratio as a named measure | **[L1993-009]**, **[L1993-010]**, **[L1997-011]** | quote text for "loss/float" and "cost of funds" |
| The statutory loss-development schedule or a development triangle by name | **[L2001-021]**, **[L2001-022]**, **[M2005-067]** | quote text for "Schedule P" and "triangle" |
| The deferred-tax liability valued as an interest-free loan | **[R1996-010]**, **[M2015-030]**, **[M2016-058]**, **[M1996-012]** | quote text for "interest-free", "interest free" (two hits, both on options) and "deferred" (every hit read) |
| A recipe for constructing float from a balance sheet | **[L1993-009]**, **[L1996-008]** | quote text for "unearned", "recoverable", "acquisition cost" |
| A threshold for float, leverage, or capital per premium | **[M2023-013]**, **[M2009-058]**, **[M1995-035]** | quote text for "leverage" (every hit read), "ratio of", "capital" with "premium" |
| An owner-earnings figure computed for an insurer | **[M2016-058]**, **[M1997-141]**, **[L2006-002]** | quote text for "cash flow" with "insur"; the phrase "owner earnings" (v5 framework, Absences recorded) |
| Minority interests in a valuation | none on point | quote text for "minority" and "noncontrolling" (four hits, none on valuation) |
| A rule for the discount rate of a company earning in several currencies | **[M2000-043]**, **[M2008-043]**, **[M2003-087]** | quote text for "currenc" (every hit read) |
| A method for valuing a life insurer's or annuity writer's float | **[L2013-003]**, **[L2014-024]**, **[M2013-076]** | quote text for "life insurance" and "annuit" |
| A test of when a company is "an insurer" rather than a holding company that owns one | **[L2008-005]**, **[M1997-088]** | the rows read for 2.9 |

---

## 5. What the method cannot do, stated before it is used

- **It does not make an insurer's earnings predictable.** It makes the components measurable and leaves the judgment where the
  rows leave it: whether float proves useful or costly "is a judgment", in Buffett's word about Berkshire's own, "And absolutely I
  could be wrong about it." **[M2022-063]**.
- **It cannot audit reserves.** Development shows the filer's past errors **[L2001-021]**; it cannot show the error not yet
  made, and in long-tail lines the surprises come "big and they can come late" **[M1999-098]**. Where the development history
  is not published, Q1 decides the box (section 3, Q1).
- **It does not transfer Berkshire's licence.** The rows say no other insurer can treat its float as Berkshire does
  **[M2023-012]**; the method's ratios measure how far a company's value leans on that licence, and a run that counts a small
  insurer's investments gross on Berkshire's reasoning has smuggled the conclusion in.
- **It does not settle M2016-058.** Buffett's description of Berkshire's cash flow as including float growth **[M2016-058]**
  stays OPEN against Q4 step 1.
- **It does not resolve currency, asset managers, or life and annuity books** (CONVENTION C10 and C11).
- **It does not lighten Q2.** The castle question is harder for an insurer **[L2003-014]**, **[L2004-003]**.
- **It has not been run.** It was built from the rows on 2026-10-05 and has met no filer. The WTM and MKL runs of 2026-09-02 bind as
  recorded under the v4 method and are not re-graded by this case.

---

## AMENDMENT 2026-10-05, after the first MKL test (in force; supersedes the steps and conventions it names)
**The operator chose to amend, re-test, then adopt** (`Framework/v5/TEST - the v5 sector method on MKL, RESULTS and the comparison.md`).
The five items below supersede the steps and conventions they name; the text above stands as the record of the first draft.

**A1, gross or net of float (supersedes section 3, Q7 step 2, and CONVENTION C5).** The first component is counted **net of the
float by default**, the float treated as a debt to be paid, as book value treats it **[L2011-005]**. It is counted gross only if
all three of these hold, and the run shows both figures whichever is used:
- *costless, in each half of the window, not only on average*: the developed cost of float in each half is below the long
  government rate of the same years **[L1994-025]**, **[L1993-010]**; a good average over a bad half is the single good stretch the
  rows refuse to rely on **[L1997-012]**;
- *long-enduring*: no run-off, exit or sale of a float-producing book announced or under way, and the float not open to sudden
  demands ("what is the permanence of the float?" **[M2002-006]**, **[L2013-003]**);
- *equity enough behind it*: the rows treat float as near equity only where there is "so much equity, we could afford to do it
  that way" **[M2001-053]**, and impose restrictions where there is "a very limited amount of equity and a very large amount of
  float" **[M1995-035]**; and Berkshire says of its own way of treating float, "no other insurance company could do it"
  **[M2023-012]**. The test is passed only where the run can say, from the filing, why this company is the exception.
CONVENTION A1 (ours): the halving of the window and the order of the three tests are ours; rationale: the MKL test showed a
decade average passing a float whose first half cost more than the long rate, and the gross figure doubling the value.

**A2, float (supersedes the construction in CONVENTION C1).** Float is "the funds prepaid by policyholders and the funds earmarked
for incurred-but-not-yet-paid claims" **[L1993-009]**, net of the part ceded: **prepaid reinsurance premiums are deducted**, and
reinsurance recoverables on unpaid losses are deducted where the filer reports the reserves gross. Where the filer publishes its
own float figure, the run reconciles to it and explains any difference. CONVENTION A2 (ours): the two deductions; rationale: money
ceded to a reinsurer is held for the reinsurer's account, and the MKL test found the undeducted figure $3.1B to $3.9B too high.

**A3, "restated by later development" (supersedes the reading of CONVENTION C3).** The underwriting result is restated **by accident
year**, from the filer's loss-development tables: each accident year's result as it stands developed today, not the calendar-year
result, which carries releases from reserves set before the window. The most recent accident years, whose development is not yet
known, are flagged as immature and shown, never averaged in as if developed **[L2001-021]**, **[L1997-012]**. CONVENTION A3 (ours):
the accident-year basis and the immaturity flag; rationale: the MKL test found the two readings $55M and $292M a year apart.

**A4, the tax basis of component 2 (supersedes section 3, Q7 step 3, on this point).** Component 2 enters the value range **after
tax**, on the same basis as the owner cash v5 uses for every other business, a figure "calculated after interest, taxes,
depreciation, amortization and all forms of compensation" **[L2021-003]**; the pre-tax figure is shown beside it for the floor,
which v5 states pre-tax. CONVENTION A4 (ours): the tax rate applied is the filer's effective rate on that income over the window;
rationale: the MKL test found the two bases $96 to $177 a share apart.

**A5, the operating-income trap (added to section 3, Q4, after its second step).** Where the filer reports an "operating income" or similar
figure, the calendar-year underwriting result inside it is removed before the developed accident-year result (A3) is put in, and the
run shows the removal line by line. Without it the underwriting is counted twice, once on the filer's basis and once on the
method's, which is the double count the rows forbid **[L1998-002]**, **[M1997-141]**.
