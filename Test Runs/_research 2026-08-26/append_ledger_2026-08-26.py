import csv, io, os

PATH = r"c:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv"

ROWS = [
# id, era, quote_verbatim, year, source_file, concept, supports, evolution_notes
("E2-23","E2",
 "These represent (a) reported earnings plus (b) depreciation, depletion, amortization, and certain other non-cash charges such as Company N's items (1) and (4) less (c) the average annual amount of capitalized expenditures for plant and equipment, etc. that the business requires to fully maintain its long-term competitive position and its unit volume. (If the business requires additional working capital to maintain its competitive position and unit volume, the increment also should be included in (c). However, businesses following the LIFO inventory method usually do not require additional working capital if unit volume does not change.)",
 "1986","Shareholder Letters/1986 Letter.txt",
 "owner earnings - full definition; working capital increment; 'average annual amount'; maintenance not total capex",
 "Gate 4; Workbook Sheet 4",
 "TEXT NOTE: the source .txt splits the literal '(c)' across four lines as '(' / ' c' / ')' throughout this passage, an artifact of the HTML-to-text extraction; reassembled here, not smoothed. Three operative constraints often missed: (1) the WC increment IS part of owner earnings, so omitting it is wrong; (2) it is the increment REQUIRED to maintain competitive position and unit volume, not the raw annual balance-sheet swing; (3) 'average annual amount' governs BOTH the capex and WC terms, so a single-year figure is not the intended input. Also note (c) is maintenance capex ('requires to fully maintain'), NOT total capex, so using total capex understates owner earnings for any unit-growing business."),

("E2-24","E2",
 "See's was earning about $2 million after tax at the time, and such earnings seemed conservatively representative of future earning power in constant 1972 dollars.",
 "1983","Shareholder Letters/1983 Letter.txt",
 "valuation anchor is representative future earning power, not the worst observed year",
 "Gate 6 Book One and Book Two base",
 "The anchor Buffett actually uses in his most-cited private purchase. 'Conservatively representative of FUTURE earning power' is a normal-year concept. He does not anchor to a trough."),

("E2-25","E2",
 "(2) demonstrated consistent earning power (future projections are of little interest to us, nor are \"turnaround\" situations),",
 "1987","Shareholder Letters/1987 Letter.txt",
 "acquisition criteria; consistent earning power",
 "Gate 1; Gate 6 base selection",
 "Appears verbatim in the acquisition criteria of the 1982, 1983, 1984, 1985, 1986 and 1987 letters, i.e. Buffett repeated it unchanged for six consecutive years. 'CONSISTENT earning power', not minimum earning power."),

("E3-24","E3",
 "Consider some mathematics: Wells Fargo currently earns well over $1 billion pre-tax annually after expensing more than $300 million for loan losses. If 10% of all $48 billion of the bank's loans - not just its real estate loans - were hit by problems in 1991, and these produced losses (including foregone interest) averaging 30% of principal, the company would roughly break even. A year like that - which we consider only a low-level possibility, not a likelihood - would not distress us. In fact, at Berkshire we would love to acquire businesses or invest in capital projects that produced no return for a year, but that could then be expected to earn 20% on growing equity.",
 "1990","Shareholder Letters/1990 Letter.txt",
 "the bad year is a SURVIVAL test run separately, not a valuation anchor",
 "Gate 4 Fortress Test; Gate 6 Book One anchoring",
 "The decisive passage on trough-anchoring. Buffett values Wells Fargo off CURRENT earning power ('less than five times after-tax earnings, and less than three times pre-tax earnings' in the same section), then stress-tests a catastrophic year SEPARATELY as a survival question, and states explicitly that a zero-return year 'would not distress us' for a business that can then earn 20% on growing equity. Two distinct tests, two distinct places. Anchoring valuation to the trough collapses them into one and double-counts."),

("E3-25","E3",
 "And the final chapter is on the margin of safety, which means, don't try and drive a 9,800pound truck over a bridge that says it's, you know, \"Capacity: 10,000 pounds.\" But go down the road a little bit and find one that says, \"Capacity: 15,000 pounds.\"",
 "1996","Annual Meetings/1996 Annual Meeting.txt",
 "margin of safety - the bridge illustration; implies ~35%",
 "Gate 6 MOS",
 "TEXT NOTE: '9,800pound' is unspaced in the source; preserved. Arithmetic: 9,800/15,000 = 0.653, i.e. a 35% margin. Ruling 5's citation of this passage is arithmetically correct. Immediately preceded in the same answer by 'if you have to actually do it on - with pencil and paper, it's too close to think about' (the Ruling 4-B quote), so the bridge and the scream test are one continuous thought."),

("E3-26","E3",
 "Obviously, if you understood a business perfectly - the future of a business - you would need very little in the way of a margin of safety. So the more volatile the business is - or possibility is - but assuming you still want invest in it, the larger the margin of safety. [...] Well, if you're driving a truck across a bridge that holds - it says it holds 10,000 pounds - and you've got a 9,800 pound vehicle, you know, if the bridge is about six inches above the crevice that it covers, you may feel OK. But if it's, you know, over the Grand Canyon, you may feel you want a little larger margin of safety, in terms of only driving a 4,000 pound truck, or something, across. So it depends on the nature of the underlying risk.",
 "1997","Annual Meetings/1997 Annual Meeting.txt",
 "margin of safety is a FUNCTION of certainty and of downside severity, in both directions",
 "Gate 6 MOS",
 "The scaling rule stated explicitly, and it runs BOTH ways: 'understood perfectly ... very little in the way of a margin of safety' at one end, Grand Canyon at the other. Ruling 5 quoted the Grand Canyon half and not the 'very little' half. Note the two variables Buffett names are CERTAINTY ('the more volatile the business') and CONSEQUENCE SEVERITY ('six inches above the crevice' vs the Grand Canyon)."),

("E4-10","E4",
 "Now, repurchases are all the rage, but are all too often made for an unstated and, in our view, ignoble reason: to pump or support the stock price. The shareholder who chooses to sell today, of course, is benefitted by any buyer, whatever his origin or motives. But the continuing shareholder is penalized by repurchases above intrinsic value. Buying dollar bills for $1.10 is not good business for those who stick around.",
 "1999","Shareholder Letters/1999 Letter.txt",
 "buybacks above intrinsic value penalize continuing holders",
 "Gate 3 alignment/competence",
 "The clearest statement that overpaying on buybacks is a real cost. Note what Buffett does NOT do with the finding: he does not reprice the business or raise a discount rate on it. See E4-13 for the humility clause he attaches in the very next paragraph."),

("E4-11","E4",
 "You calculate - I think you take all of the variables and calculate them reasonably conservatively. But you don't try and put too much windage in at every level. And then when you get all through, you apply the margin of safety. So I would say, don't focus too much on taking it on each variable in terms of the discount rate and the growth rate and so on. But try to be as realistic as you can on those numbers, but with any errors being on the conservative side. And then when you get all through, you apply the margin of safety. [...] I want to be conservative at all the levels and then I want to have that significant margin of safety at the end.",
 "2004","Annual Meetings/2004 Annual Meeting.txt",
 "THE WINDAGE RULE: realism at each variable, conservatism applied ONCE at the end",
 "Gate 6 - governs the whole construction of Book One and Book Two",
 "Asked directly how he combines growth estimates with the margin of safety. This is the most procedurally specific methodology statement in the corpus and it names the exact two variables the framework currently loads with extra conservatism ('the discount rate and the growth rate'). Stacking conservative inputs, a certainty spread and a margin of safety on the same estimate is the practice this passage forbids."),

("E4-12","E4",
 "We favor the businesses where we really think we know the answer. And, therefore, if a business gets to the point where we think the industry in which it operates, the competitive position or anything is so chancy that we can't really come up with a figure, we don't really try to compensate for that sort of thing by having some extra large margin of safety. We really want to try to go on to something that we understand better. So if we buy something like - See's Candy as a business or Coca-Cola as a stock, we don't think we need a huge margin of safety because we don't think we're going to be wrong about our assumptions in any material way. [...] We'd love to find them when they're selling at 40 cents on the dollar but we will buy those as much closer to a dollar on the dollar. We don't like to pay a dollar on the dollar, but we'll pay something close.",
 "2007","Annual Meetings/2007 Annual Meeting.txt",
 "for a business you genuinely understand, the margin of safety is SMALL; uncertainty is answered by walking away, not by a bigger discount",
 "Gate 6 MOS; Gate 1 circle of competence",
 "The question asked was almost exactly ours: 'in a dominant, long-standing, stable business, would you demand a 10 percent margin of safety and, if so, how would you increase this in a weaker business?' Two rules follow. (1) A big MOS is NOT the remedy for uncertainty; leaving is. (2) For a great business the discount is small, 'closer to a dollar on the dollar'. The fat-man illustration in the same answer ('you don't know whether they weigh 300 pounds or 325 pounds ... if we can come in at the equivalent of 270 pounds, we'll feel good') implies roughly 10-17% off, i.e. LESS than the framework's standing 20%."),

("E4-13","E4",
 "Charlie and I admit that we feel confident in estimating intrinsic value for only a portion of traded equities and then only when we employ a range of values, rather than some pseudo-precise figure. Nevertheless, it appears to us that many companies now making repurchases are overpaying departing shareholders at the expense of those who stay. In defense of those companies, I would say that it is natural for CEOs to be optimistic about their own businesses. They also know a whole lot more about them than I do.",
 "1999","Shareholder Letters/1999 Letter.txt",
 "epistemic humility clause attached to any outside judgment that a buyback was overpriced",
 "Gate 3",
 "Attaches directly to E4-10 and limits it. Buffett states the overpayment finding and in the same breath concedes his own IV estimate is a range, that the CEO knows more, and that optimism is natural rather than culpable. Any framework rule that converts 'they bought above OUR IV' into a penalty on the business must carry this clause."),

("E5-08","E5",
 "Charlie and I favor repurchases when two conditions are met: first, a company has ample funds to take care of the operational and liquidity needs of its business; second, its stock is selling at a material discount to the company's intrinsic business value, conservatively calculated. We have witnessed many bouts of repurchasing that failed our second test. Sometimes, of course, infractions - even serious ones - are innocent; many CEOs never stop believing their stock is cheap. [...] The first law of capital allocation - whether the money is slated for acquisitions or share repurchases - is that what is smart at one price is dumb at another.",
 "2011","Shareholder Letters/2011 Letter.txt",
 "the two-condition buyback test; failing it can be an innocent infraction",
 "Gate 3",
 "Gives the actual test to apply (funds + material discount to conservatively calculated IV) AND the disposition toward failure: 'infractions - even serious ones - are innocent' in some cases, because 'many CEOs never stop believing their stock is cheap'. Buffett names the failure without treating it as evidence of bad management per se."),

("E5-09","E5",
 "But never forget: In repurchase decisions, price is all-important. Value is destroyed when purchases are made above intrinsic value.",
 "2012","Shareholder Letters/2012 Letter.txt",
 "buybacks above IV destroy value - the flattest statement of it",
 "Gate 3",
 "Same letter also gives the standard he applied to himself: repurchase 'is sensible for a company when its shares sell at a meaningful discount to conservatively calculated intrinsic value ... It's hard to go wrong when you're buying dollar bills for 80 cents or less.'"),

("E5-10","E5",
 "We have never, however, singled out restructuring charges and told you to ignore them in estimating our normal earning power. If there were to be some truly major expenses in a single year, I would, of course, mention it in my commentary.",
 "2016","Shareholder Letters/2016 Letter.txt",
 "'normal earning power' is the operative valuation quantity; single-year distortions are called out, not adopted",
 "Gate 6 base selection",
 "Confirms the mature articulation of the E2-24 / E2-25 concept: the quantity being estimated is NORMAL earning power, and a single distorted year is something to disclose and reason about, in either direction, rather than something to adopt as the anchor."),
]

with open(PATH, "r", encoding="utf-8-sig", newline="") as f:
    existing = f.read()

if not existing.endswith("\n"):
    existing += "\n"

buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
for r in ROWS:
    w.writerow(r)

with open(PATH, "w", encoding="utf-8-sig", newline="") as f:
    f.write(existing)
    f.write(buf.getvalue())

# verify
with open(PATH, "r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))
print("total rows now:", len(rows))
print("appended:", len(ROWS))
for r in rows[-len(ROWS):]:
    print(" ", r[0], "|", r[3], "|", r[4], "|", len(r), "fields")
