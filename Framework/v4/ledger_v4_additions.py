"""v4 JOB 1 — extend and repair principle_ledger.csv.

25 new verbatim rows (all personally verified against the source line this session)
+ 2 re-cuts of rows that truncated their own source paragraph.

Schema: id, era, quote_verbatim, year, source_file, concept, supports_gate_or_sheet, evolution_notes
"""
import csv, io, os

P = r"c:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv"
HARDWRAP = ("TEXT NOTE: source file is hard-wrapped at ~60 chars; line breaks removed to "
            "reassemble the sentences. No other change.")

NEW = [
# ---------------------------------------------------------------- E2 (1977-1989)
("E2-26","E2",
 "We will be candid in our reporting to you, emphasizing the pluses and minuses important in appraising business value. Our guideline is to tell you the business facts that we would want to know if our positions were reversed. We owe you no less. [...] We also believe candor benefits us as managers: the CEO who misleads others in public may eventually mislead himself in private.",
 "1983","Shareholder Letters/1983 Letter.txt (lines 136-146)",
 "candor - the test, and WHY honesty and rationality are one question",
 "Q3 management",
 HARDWRAP+" Restated as Owner's Manual principle 12. The final clause is the corpus's own explanation of why integrity and competence cannot be assessed separately: public dishonesty degrades private cognition. Supplies an operational test applicable to any letter or 10-K - 'the facts we would want to know if our positions were reversed'."),

("E2-27","E2",
 "But the promised benefits from these textile investments were illusory. Many of our competitors, both domestic and foreign, were stepping up to the same kind of expenditures and, once enough companies did so, their reduced costs became the baseline for reduced prices industrywide. Viewed individually, each company's capital investment decision appeared cost-effective and rational; viewed collectively, the decisions neutralized each other and were irrational (just as happens when each person watching a parade decides he can see a little better if he stands on tiptoes). After each round of investment, all the players had more money in the game and returns remained anemic.",
 "1985","Shareholder Letters/1985 Letter.txt (lines 423-434)",
 "HOW A BUSINESS ACTUALLY DIES - the capex trap; individually rational, collectively irrational",
 "Q2 franchise; Q4 survival; Q6 exit",
 HARDWRAP+" The corpus's clearest account of a specific death mechanism, and it is death by individually rational decisions - which is also what irrational capital allocation looks like from the inside. Continues at 436-441: 'huge capital investment would have helped to keep our textile business alive, but would have left us with terrible returns on ever-growing amounts of capital. [...] A refusal to invest, however, would make us increasingly non-competitive.' Replaces the invented generic 50%-decline stress test with a named, quantifiable mechanism."),

("E2-28","E2",
 "Sometimes, of course, the market may judge a business to be more valuable than the underlying facts would indicate it is. In such a case, we will sell our holdings. Sometimes, also, we will sell a security that is fairly valued or even undervalued because we require funds for a still more undervalued investment or one we believe we understand better. We need to emphasize, however, that we do not sell holdings just because they have appreciated or because we have held them for a long time. (Of Wall Street maxims the most foolish may be \"You can't go broke taking a profit.\") We are quite content to hold any security indefinitely, so long as the prospective return on equity capital of the underlying business is satisfactory, management is competent and honest, and the market does not overvalue the business.",
 "1987","Shareholder Letters/1987 Letter.txt (lines 846-860)",
 "THE SELL RULE - two sell triggers and three named hold conditions",
 "Q6 exit",
 HARDWRAP+" The single most important gap the v4 audit closed. Before this the ledger's only sell material (E2-13, E2-14) said when NOT to sell. Here are the triggers - market overvalues it, or funds are needed for something better understood or more undervalued - and the three conditions under which you hold indefinitely, which map one-to-one onto Q2, Q3 and Q5. Note what is absent: price appreciation and holding period are explicitly rejected as reasons."),

("E2-29","E2",
 "This point can be important because the heads of many companies are not skilled in capital allocation. Their inadequacy is not surprising. Most bosses rise to the top because they have excelled in an area such as marketing, production, engineering, administration or, sometimes, institutional politics.",
 "1987","Shareholder Letters/1987 Letter.txt (lines 944-949)",
 "why capital-allocation skill is scarce, and why it dominates Q3",
 "Q3 management",
 HARDWRAP+" The ledger had capital-allocation OUTPUTS (buybacks: E2-06, E4-10, E5-01, E5-08, E5-09) but never the reason the skill is rare. The same section quantifies why it dominates: a CEO whose company retains earnings equal to 10% of net worth will, after ten years, have been responsible for deploying more than 60% of all the capital at work in the business."),

("E2-30","E2",
 "For example: (1) As if governed by Newton's First Law of Motion, an institution will resist any change in its current direction; (2) Just as work expands to fill available time, corporate projects or acquisitions will materialize to soak up available funds; (3) Any business craving of the leader, however foolish, will be quickly supported by detailed rate-of-return and strategic studies prepared by his troops; and (4) The behavior of peer companies, whether they are expanding, acquiring, setting executive compensation or whatever, will be mindlessly imitated. [...] Institutional dynamics, not venality or stupidity, set businesses on these courses, which are too often misguided.",
 "1989","Shareholder Letters/1989 Letter.txt (lines 1524-1535)",
 "the institutional imperative, ENUMERATED as four observable behaviours",
 "Q3 management",
 HARDWRAP+" E2-18 and E3-02 capture the label and the definition; this is the operational content. All four are testable against a real filing set. 'Not venality or stupidity' is the crucial disposition note - this is not a fraud test, and must never be scored as one."),

("E2-31","E2",
 "After some other mistakes, I learned to go into business only with people whom I like, trust, and admire. As I noted before, this policy of itself will not ensure success: A second-class textile or department-store company won't prosper simply because its managers are men that you would be pleased to see your daughter marry. However, an owner - or investor - can accomplish wonders if he manages to associate himself with such people in businesses that possess decent economic characteristics. Conversely, we do not wish to join with managers who lack admirable qualities, no matter how attractive the prospects of their business. We've never succeeded in making a good deal with a bad person.",
 "1989","Shareholder Letters/1989 Letter.txt (lines 1543-1554)",
 "the management veto - and its correct subordination to business economics",
 "Q3 management",
 HARDWRAP+" The final sentence is the veto rule for Q3; the preceding sentences prevent it being read as management-first. Good people cannot rescue bad economics, but bad people void good economics. Order matters."),

("E2-32","E2",
 "You should be fully aware of one attitude Charlie and I share that hurts our financial performance: Regardless of price, we have no interest at all in selling any good businesses that Berkshire owns. We are also very reluctant to sell sub-par businesses as long as we expect them to generate at least some cash and as long as we feel good about their managers and labor relations. [...] Nevertheless, gin rummy managerial behavior (discard your least promising business at each turn) is not our style. We would rather have our overall results penalized a bit than engage in that kind of behavior.",
 "1983","Owners Manual/An Owners Manual.txt (principle 11, lines 209-216); wording originates in Shareholder Letters/1983 Letter.txt",
 "regardless of price; the gin rummy prohibition",
 "Q6 exit",
 "CRITICAL SCOPE LIMIT, stated by Buffett himself in the same principle: 'we emphasize that the comments here refer to businesses we control, not to marketable securities.' This may NOT be quoted as a never-sell rule for stocks. For marketable securities the governing row is E2-28 (the 1987 sell rule). Counterweight to carry alongside it, 2008 meeting: 'we don't do anything when the phrase \"regardless of price\" enters into the sentence.'"),

# ---------------------------------------------------------------- E3 (1990-1998)
("E3-29","E3",
 "The banking business is no favorite of ours. When assets are twenty times equity - a common ratio in this industry - mistakes that involve only a small portion of assets can destroy a major portion of equity. [...] Because leverage of 20:1 magnifies the effects of managerial strengths and weaknesses, we have no interest in purchasing shares of a poorly-managed bank at a \"cheap\" price. Instead, our only interest is in buying into well-managed banks at fair prices.",
 "1990","Shareholder Letters/1990 Letter.txt (lines 320-322)",
 "bank leverage - and the conclusion is MANAGEMENT QUALITY, not a ratio ceiling",
 "Q4 survival; Q3 management",
 "PREVIOUSLY UNROWED, though the framework's 10:1 automatic-fail ceiling cited it as '[E3-02 context]' - E3-02's quote is the institutional-imperative sentence that follows, so the ceiling has never had a real source. Read plainly: Buffett states NO ceiling, calls 20:1 'a common ratio in this industry' i.e. normal, and concludes about MANAGEMENT. He then buys Wells Fargo at roughly that leverage. A 10:1 automatic fail would reject the purchase this passage exists to describe. The invented 10:1 ceiling is retired in v4; see 'INVENTIONS - deleted and why'."),

("E3-30","E3",
 "The question is whether this erosion is just part of an aberrational cycle - to be fully made up in the next upturn - or whether the business has slipped in a way that permanently reduces intrinsic business values.",
 "1990","Shareholder Letters/1990 Letter.txt (line 141)",
 "the monitoring question: cyclical dip or permanent slip?",
 "Q2 franchise; Q6 exit",
 "The only place Buffett narrates a moat degrading in real time and writes intrinsic value down as a result - while still calling the businesses 'fine businesses'. This one sentence is the whole of the monitoring test, and it is a question rather than a threshold, which is why no mechanical tripwire replaces it. Inverse of E4-02 (widening the moat)."),

("E3-31","E3",
 "At Berkshire, we attempt to deal with this problem in two ways. First, we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in character. If a business is complex or subject to constant change, we're not smart enough to predict future cash flows. Incidentally, that shortcoming doesn't bother us. What counts for most people in investing is not how much they know, but rather how realistically they define what they don't know. An investor needs to do very few things right as long as he or she avoids big mistakes.",
 "1992","Shareholder Letters/1992 Letter.txt (lines 798-807)",
 "circle of competence DEFINED - simple and stable; defined negatively",
 "Q1 understanding",
 HARDWRAP+" This is the FIRST of the two ways in the 1992 letter; E3-08 carried only the second (margin of safety) and was re-cut in v4 to carry both. Buffett names understanding FIRST and says of the margin of safety only 'Second, and equally important'. Quoting the MOS half alone inverts his own ordering. Defines 'understand' operationally as SIMPLE AND STABLE, and states the criterion negatively: 'how realistically they define what they don't know.'"),

("E3-32","E3",
 "So I do not have to have a view on interest rates - and I don't have a view on interest rates - to make a decision as to an insurance business, or a mortgage guarantor business, or a banking business, or something of the sort, relative to making a judgment about Coke or Gillette.",
 "1994","Annual Meetings/1994 Annual Meeting.txt (line 733)",
 "rates are gravity, but you may NOT take a view on them",
 "Q5 price",
 "MUST SHIP PAIRED WITH E4-15 (the gravity passage). E4-15 alone invites exactly the macro forecasting the corpus forbids; this is the guardrail. Same answer opens (line 731): 'the value of every business... is 100 percent sensitive to interest rates.' So: rates enter as the current observed sovereign, never as a forecast. Consistent with E1-11 and E5-03."),

("E3-33","E3",
 "Within the growth stock model, there's a sub-position: There are actually businesses that you will find a few times in a lifetime where any manager could raise the return enormously just by raising prices, and yet they haven't done it. So they have huge untapped pricing power that they're not using. That is the ultimate no-brainer.",
 "1994","Munger Talks (PCA)/Talk 02 - A Lesson on Elementary Worldly Wisdom (USC, 1994-04-14).txt (line 417)",
 "UNTAPPED pricing power as the strongest franchise signal",
 "Q2 franchise",
 "Munger. Cuts against E3-03's realized-returns test: E3-03 says pricing power is DEMONSTRATED by high returns on capital, but the best case is pricing power that has NOT yet shown up in returns. A Gate 2 screening only on realized ROIC misses this class entirely. Same passage, line 425: 'There are actually people out there who don't price everything as high as the market will easily stand. And once you figure that out, it's like finding money in the street, if you have the courage of your convictions.'"),

("E3-34","E3",
 "I've never seen - you know, Warren talks about these discounted cash flows. I've never seen him do one. (Laughter and applause)",
 "1996","Annual Meetings/1996 Annual Meeting.txt (line 1273)",
 "Munger: the DCF is not part of the actual method",
 "Q5 price",
 "PREVIOUSLY UNROWED despite being quoted in Rulings 4-B and 14 and in the run template. NOTE the exact text includes the false start 'I've never seen -' which the framework has been silently cleaning up; recorded here verbatim per Prime Rule 1. Munger continues at line 1281: 'If it isn't pluperfect obvious that it's going to work out well, if you do the calculation, he tends to go on to the next idea.' Buffett agrees at 1283: 'if you have to actually do it on - with pencil and paper, it's too close to think about.'"),

("E3-35","E3",
 "Charlie and I have the easy jobs at Berkshire: We do very little except allocate capital. And, even then, we are not all that energetic. We have one excuse, though: In allocating capital, activity does not correlate with achievement. Indeed, in the fields of investments and acquisitions, frenetic behavior is often counterproductive. Therefore, Charlie and I mainly just wait for the phone to ring.",
 "1998","Shareholder Letters/1998 Letter.txt (lines 515-518)",
 "inactivity - the causal claim, not the attitude",
 "Q6 exit; working method",
 "E3-01 and E3-15 assert inactivity; neither says WHY it works. 'Activity does not correlate with achievement' is the causal claim. Munger quantifies it, Talk 02 line 413: 'There are huge advantages for an individual to get into a position where you make a few great investments and just sit on your ass: You're paying less to brokers. You're listening to less nonsense. And if it works, the governmental tax system gives you an extra one, two, or three percentage points per annum compounded.'"),

# ---------------------------------------------------------------- E4 (1999-2008)
("E4-15","E4",
 "To understand why that happened, we need first to look at one of the two important variables that affect investment results: interest rates. These act on financial valuations the way gravity acts on matter: The higher the rate, the greater the downward pull. That's because the rates of return that investors need from any kind of investment are directly tied to the risk-free rate that they can earn from government securities. So if the government rate rises, the prices of all other investments must adjust downward, to a level that brings their expected rates of return into line. [...] Consequently, every time the risk-free rate moves by one basis point - by 0.01% - the value of every investment in the country changes. [...] Nonetheless, the effect - like the invisible pull of gravity - is constantly there.",
 "1999","Fortune Essays (Buffett)/1999 - Mr Buffett on the Stock Market.txt (lines 19-21)",
 "INTEREST RATES AS GRAVITY - the mechanism the whole hurdle rests on",
 "Q5 price",
 "The largest single gap the v4 audit found: MISSING ENTIRELY from a 92-row ledger. E4-01 and E3-23 say the bond yield is an input; neither says why. This is the only place Buffett states that the sovereign yield is not an analyst's convention but a constraint acting on every asset simultaneously. Restated 2001 essay: 'In economics, interest rates act as gravity behaves in the physical world. At all times, in all markets, in all parts of the world, the tiniest change in rates changes the value of every financial asset.' MUST SHIP PAIRED WITH E3-32 or it becomes macro forecasting."),

("E4-16","E4",
 "Whenever a bright person, a really bright person, goes broke that has a lot of money, it's because of leverage. It - you simply - you basically can't - it would be almost impossible to go broke without borrowed money being in the equation.",
 "1999","Annual Meetings/1999 Annual Meeting.txt (line 117)",
 "the single cause of business death for the otherwise-competent",
 "Q4 survival",
 "TRANSCRIPT NOTE: the false starts ('It - you simply - you basically can't -') are preserved verbatim per Prime Rule 1. A one-variable causal claim about how capable people lose everything. Directly supports weighting debt heavily in Q4 - and note it does so WITHOUT a ratio, which is why v4 deletes the invented 10:1 ceiling (see E3-29) and keeps the question."),

("E4-17","E4",
 "So now we sell - really when we think that we've - when we're reevaluating the economic characteristics of the business. [...] We probably had one view of the long-term competitive advantage of the company at the time we bought it, and we may have modified that. That doesn't mean we think that the company is going into some disastrous period or anything remotely like that. [...] But we probably don't think that their competitive advantage is as strong as we might have thought [...] And those beliefs change quite gradually.",
 "2002","Annual Meetings/2002 Annual Meeting.txt (lines 139-141)",
 "THE EXIT TRIGGER IS A MOAT DOWNGRADE, and it is gradual",
 "Q6 exit; Q2 franchise",
 "Answering the direct question of when to hold forever and when to sell. The trigger is a re-evaluation of competitive advantage - not a price move, not a bad quarter, and explicitly not distress ('a fine future'). 'Those beliefs change quite gradually' is direct corpus evidence AGAINST any short-window mechanical exit such as the framework's invented two-consecutive-quarters rule. Worked example in the same answer: newspapers, impregnable in 1970, not the same franchise in 2002."),

("E4-18","E4",
 "there are things in life that you don't have to make a decision on and that are too hard. And many years ago on one of the reports, I said one of the interesting things about investment is that there's no degree of difficulty factor. [...] And we get paid, not for jumping over 7-foot bars, but for stepping over 1-foot bars. [...] Now maybe we cast out too many things as being too hard and thereby narrow our universe. But I'd rather have the narrow - the universe be a little too - interpret it as being a little too - a little smaller than it really is, than being interpreted as larger than it is.",
 "2005","Annual Meetings/2005 Annual Meeting.txt (lines 977-979)",
 "no degree-of-difficulty factor; deliberately UNDER-estimate the circle",
 "Q1 understanding",
 "PREVIOUSLY UNROWED despite governing the 7-foot bar rule in CLAUDE.md and the run template. The final sentence is what makes 'too hard' a RULE rather than an attitude: err toward a smaller universe. Munger the same day (line 973): 'We just throw some decisions into the \"too hard\" pile and go on to others.' Origin of the bar metaphor, 1989 letter: 'we concentrated on identifying one-foot hurdles that we could step over rather than because we acquired any ability to clear seven-footers.'"),

("E4-19","E4",
 "There's just - there's just games that are too tough. Charlie says, you know, \"We've got three boxes at the company: in, out, and too hard.\" And a lot of things end up in the \"too hard\" pile, and it doesn't bother us. [...] What I've learned is I know enough not - to know that I don't know enough to make an investment decision.",
 "2006","Annual Meetings/2006 Annual Meeting.txt (line 215)",
 "THE THREE BOXES - in, out, and too hard",
 "all questions - the verdict structure itself",
 "PREVIOUSLY UNROWED despite being the basis of the framework's entire verdict structure. ATTRIBUTION: the line is MUNGER'S, quoted by Buffett ('Charlie says'). The framework recorded it as Buffett's until 2026-08-26. Munger's own version later the same meeting (line 821): 'If something is too hard to do, we look for something that isn't too hard to do. What could be more obvious than that?' v4 splits 'too hard' into UNRESEARCHED (evidence exists, go get it) and UNKNOWABLE (evidence is in, future indeterminate) - a framework distinction, not a corpus one, and labelled as such."),

("E4-20","E4",
 "Now let's move to the gruesome. The worst sort of business is one that grows rapidly, requires significant capital to engender the growth, and then earns little or no money. Think airlines. [...] Investors have poured money into a bottomless pit, attracted by growth when they should have been repelled by it. [...] To sum up, think of three types of \"savings accounts.\" The great one pays an extraordinarily high interest rate that will rise as the years pass. The good one pays an attractive rate of interest that will be earned also on deposits that are added. Finally, the gruesome account both pays an inadequate interest rate and requires you to keep adding money at those disappointing returns.",
 "2007","Shareholder Letters/2007 Letter.txt (lines 408-425)",
 "GREAT / GOOD / GRUESOME - does growth create or destroy value here?",
 "Q2 franchise; Q4 survival; Q5 price",
 "Was buried in E4-04's evolution_notes as a parenthetical; promoted to its own row in v4 and E4-04 re-cut to cross-reference. The corpus's own answer to whether growth is good, and it is expressed as a YIELD, so it plugs straight into Q5. 'Attracted by growth when they should have been repelled by it' is the sharpest anti-growth-screen line in the corpus. Worked examples in the same section: See's ($32m reinvested since 1972 against $1.35bn of pre-tax earnings) and FlightSafety ($509m incremental investment for $159m of gain)."),

("E4-21","E4",
 "We don't formally have discount rates. [...] But I can't tell you that we sit down every morning and I call Charlie in Los Angeles and say, \"What's our hurdle rate today?\" I mean, we've never used the term. [MUNGER:] the trouble with the hurdle rate concept - not that we don't have one, in a sense - is it doesn't work as well as a system of comparing things. [...] the concept of opportunity cost is - it's so little taught in investment. [...] But in the real world, your opportunity costs are what you want to make your decisions based on.",
 "2007","Annual Meetings/2007 Annual Meeting.txt (lines 773-779)",
 "NO HURDLE RATE. The decision is COMPARATIVE - opportunity cost",
 "Q5 price",
 "The corpus's answer to a question v3.1 could not answer: how many points of equity premium are enough? Answer: the question is malformed. Buffett keeps the government bond as 'the yardstick at a base' (line 773) but refuses the term hurdle rate; Munger says a threshold 'doesn't work as well as a system of comparing things' and gives the worked example - 8 percent for sure available versus your 7 percent, 'I don't have to waste 5 minutes with you.' This is why v4's price question RANKS rather than setting a threshold, which in one move removes the need for the invented 4% floor, the size premiums and the Coca-Cola clause."),

# ---------------------------------------------------------------- E5 (2009-)
("E5-11","E5",
 "Financial staying power requires a company to maintain three strengths under all circumstances: (1) a large and reliable stream of earnings; (2) massive liquid assets and (3) no significant near-term cash requirements. Ignoring that last necessity is what usually leads companies to experience unexpected problems: Too often, CEOs of profitable companies feel they will always be able to refund maturing obligations, however large these are.",
 "2014","Special Letters/2014 Warren Buffett - Past Present Future.txt (lines 504-509)",
 "SURVIVAL - the three strengths, and which one actually kills you",
 "Q4 survival",
 "Q4 previously had no explicit survival rule in the ledger at all - E3-24 (Wells Fargo) is a worked example, not a rule. This is the rule, in three named components, and it identifies the THIRD as the usual killer, which is a non-obvious ordering a concise framework would otherwise get backwards. Same document: 'Cash, though, is to a business as oxygen is to an individual: never thought about when it is present, the only thing in mind when it is absent.' Replaces the invented generic 50%-decline test with three observable conditions."),

("E5-12","E5",
 "A CEO who is 64 and plans to retire at 65 may have his own special calculus in evaluating risks that have only a tiny chance of happening in a given year. He may, in fact, be \"right\" 99% of the time. Those odds, however, hold no appeal for us. We will never play financial Russian roulette with the funds you've entrusted to us, even if the metaphorical gun has 100 chambers and only one bullet. In our view, it is madness to risk losing what you need in pursuing what you simply desire.",
 "2014","Special Letters/2014 Warren Buffett - Past Present Future.txt (lines 557-561)",
 "why permanent-loss risk is refused at ANY probability",
 "Q4 survival; Q3 management; sizing",
 "E5-05 gives the rule ('never risk permanent loss of capital'); this gives the reasoning, plus a Q3 test in passing - the misaligned CEO horizon, where a manager's retirement date changes his risk calculus. Final sentence is the corpus's most direct statement on sizing and leverage. Same passage: 'it is entirely predictable that people will occasionally panic, but not at all predictable when this will happen.'"),

("E5-13","E5",
 "At this point, a report card from me is appropriate: In 58 years of Berkshire management, most of my capital-allocation decisions have been no better than so-so. [...] Our satisfactory results have been the product of about a dozen truly good decisions - that would be about one every five years - and a sometimes-forgotten advantage that favors long-term investors such as Berkshire.",
 "2022","Shareholder Letters/2022 Letter.txt (lines 145-152)",
 "how many decisions a lifetime actually needs - about a dozen in 58 years",
 "Q1 understanding; Q6 exit; working method",
 "TEXT NOTE: the source is PDF-extracted and renders the em dash as a replacement character; normalised to ' - ' here, no words changed. The most precise version in the corpus - Buffett quantifying his own hit rate. E5-05 has the vaguer 'a couple of good decisions during a lifetime'. This number is what justifies the entire architecture of a framework designed to say no, and it is the corpus's own answer to why a small universe is correct."),

("E5-14","E5",
 "The lesson for investors: The weeds wither away in significance as the flowers bloom. Over time, it takes just a few winners to work wonders. And, yes, it helps to start early and live into your 90s as well.",
 "2022","Shareholder Letters/2022 Letter.txt (lines 183-185)",
 "why you do not trim winners or rebalance",
 "Q6 exit; sizing",
 "E2-14 quotes the 1988 flowers/weeds simile inside a note; this is the 2022 statement of the position-sizing consequence, with the arithmetic behind it in the same section (Coke and Amex each bought for $1.3bn; annual dividends grew from $75m to $704m and from $41m to $302m; 'All Charlie and I were required to do was cash Coke's quarterly dividend checks'). The strongest corpus argument against mechanical trimming or rebalancing rules."),
]

# ---- re-cuts of rows that truncated their own source paragraph -----------------
RECUT = {
 "E3-08": {
   2: ("At Berkshire, we attempt to deal with this problem in two ways. First, we try to stick to "
       "businesses we believe we understand. That means they must be relatively simple and stable in "
       "character. If a business is complex or subject to constant change, we're not smart enough to "
       "predict future cash flows. [...] Second, and equally important, we insist on a margin of safety "
       "in our purchase price. If we calculate the value of a common stock to be only slightly higher "
       "than its price, we're not interested in buying. We believe this margin-of-safety principle, so "
       "strongly emphasized by Ben Graham, to be the cornerstone of investment success."),
   5: "the TWO defences, in Buffett's own order: understanding FIRST, margin of safety second",
   7: ("RE-CUT 2026-08-26. The row previously carried only the second half, which inverted Buffett's own "
       "ordering - he names understanding first and says of the margin of safety only 'Second, and equally "
       "important'. Quoting the MOS alone made it look like the primary defence. The first half is rowed "
       "separately and in full at E3-31. " + HARDWRAP + " Graham named inside Buffett's sentence per the "
       "shelf amendment. The specific 20%/30% MOS thresholds were framework inventions and are retired in v4."),
 },
 "E4-04": {
   7: ("RE-CUT 2026-08-26. This row previously buried the entire Great/Good/Gruesome taxonomy in a "
       "parenthetical note; that material is now rowed in full at E4-20, where it can be cited. This row "
       "is now confined to its actual subject: what 'enduring' excludes - industries prone to rapid and "
       "continuous change, and businesses dependent on a great manager."),
 },
}

with open(P, "r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))
header, body = rows[0], rows[1:]

existing = {r[0].strip() for r in body if r}
dupes = [r[0] for r in NEW if r[0] in existing]
assert not dupes, f"ID collision: {dupes}"

recut_hits = 0
for r in body:
    if r and r[0].strip() in RECUT:
        for idx, val in RECUT[r[0].strip()].items():
            r[idx] = val
        recut_hits += 1
assert recut_hits == len(RECUT), f"re-cut rows found: {recut_hits} of {len(RECUT)}"

body.extend(list(NEW))

buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
w.writerow(header)
for r in body:
    w.writerow(r)
with open(P, "w", encoding="utf-8-sig", newline="") as f:
    f.write(buf.getvalue())

print(f"ledger rows: {len(rows)-1} -> {len(body)}   (+{len(NEW)} new, {recut_hits} re-cut)")
import collections
c = collections.Counter(r[1] for r in body if len(r) > 1)
print("by era:", dict(sorted(c.items())))
