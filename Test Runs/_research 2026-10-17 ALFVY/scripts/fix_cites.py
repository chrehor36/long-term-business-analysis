# One-off: put a verbatim fragment of each row beside its id where the run file had the id beside my own words.
import sys
sys.stdout.reconfigure(encoding="utf-8")
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
R = [
 ("**Contrary evidence, written down as found**\n**[M1997-127]**:", "**Contrary evidence, written down as found**:"),
 ("- **Can I name the winner, not just the industry** **[M2012-067]**: the report",
  "- **Can I name the winner, not just the industry?** The rows pass over industries where \"we don’t have the faintest idea who the winners will be\" **[M2012-067]**; here the report"),
 ("- **Abroad** **[M2000-141]**: a Swedish", "- **Abroad**, \"where we think we understand the nuances of the corporate governance system and taxation\" **[M2000-141]**: a Swedish"),
 ("the variables are volume and price,\n  not technology change **[M2012-065]**, **[M1998-044]**, **[M2008-033]**.",
  "the variables are volume and price,\n  not technology change: \"a reasonable fix on about what the earning power and competitive position will look like in five\n  or 10 years\" **[M2012-065]**; \"If something is not very predictable, forget it.\" **[M1998-044]** does not bite; \"the\n  financial statements will tell me the information that’s useful to me\" **[M2008-033]**."),
 ("1. **Key factors and their permanence** **[M1995-038]**.", "1. **Key factors and their permanence**: \"What are the key factors? And how permanent are they?\" **[M1995-038]**."),
 ("2. **Would it stand without the lord** **[M1996-037]**:", "2. **Would it stand without the lord**: \"The really great business is one that doesn’t require good management.\" **[M1996-037]**;"),
 ("3. **The money test** **[M2011-015]**:", "3. **The money test**: \"if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?\" **[M2011-015]**;"),
 ("4. **Pricing power and the agony before a rise** **[M2005-020]**.", "4. **Pricing power**, measured \"by the agony they go through in determining whether a price increase can be sustained\" **[M2005-020]**."),
 ("8. **The low bid** **[M2017-009]**.", "8. **The low bid**: \"it wouldn’t be a question of people buying candy for the low bid\" **[M2017-009]**."),
 ("10. **Widening or narrowing** **[M1999-108]**.", "10. **Widening or narrowing**: \"how wide the moat is and whether it’s likely to widen further or shrink on you\" **[M1999-108]**."),
 ("11. **What could destroy, modify or reduce it** **[M2000-014]**:", "11. **What could \"destroy, or modify, or reduce the economic strengths\"** **[M2000-014]**:"),
 ("returns on capital above both SEC rivals read **[M1995-038]**, **[L2007-004]**,\n  **[M2005-017]**, **[M1999-108]**.",
  "returns on capital above both SEC rivals read: a moat that \"protects excellent returns on invested capital\"\n  **[L2007-004]**, in a business that can \"pass through increases in raw material costs\" **[M2005-017]**."),
 ("on that\n  incremental\" capital **[M2001-019]**,", "on that\n  incremental\" capital (the row's words continue \"$130 million over time\") **[M2001-019]**,"),
 ("weigh against and are carried to Q5 **[M1994-018]**, **[L2016-006]**.",
  "weigh against and are carried to Q5: a management \"preoccupied with accounting considerations\" is \"a negative\" but\n  not \"a total exclusionary factor\" **[M1994-018]**."),
 ("- **The two yardsticks** **[M1994-008]**:", "- **The two yardsticks**, \"how well they run the business\" against \"the hand they were dealt\" **[M1994-008]**:"),
 ("- **The letters and reports** **[M1998-036]**.", "- **The letters and reports**: \"whether the management is telling us about the things that we would want to know about if\n  we owned a hundred percent of the company\" **[M1998-036]**."),
 ("- **Ability:** shown in a long record, not a promise **[M1996-038]**:", "- **Ability:** \"we like people that have batted .350 or .360\" **[M1996-038]**:"),
 ("raise no\n  doubt **[M2013-088]**, **[M1998-036]**); **ability WEIGHS FOR** **[M1994-008]**, with the purchases against.",
  "raise no\n  doubt, and \"If you’ve got doubts, forget it.\" **[M2013-088]** is not triggered); **ability WEIGHS FOR** on \"what they’ve\n  accomplished and what their competitors have accomplished\" **[M1994-008]**, with the purchases against."),
 ("Against intrinsic value rather than the quote **[R2009-002]**:", "Against intrinsic value rather than the quote, since \"When the stock market has declined sharply over a five-year stretch\"\n  the market leg alone misleads **[R2009-002]**:"),
 ("so the ratio is not condemned on that ground\n  **[M2000-051]**.", "so the ratio is not condemned on that ground;\n  a fixed ratio \"strikes us as nuts\" **[M2000-051]**."),
 ("- **Issuance and deals: value given against value got** **[M1995-001]**.", "- **Issuance and deals**: \"Only if we receive less in value than we give. That’s the key to it.\" **[M1995-001]**."),
 ("so the STOP on an all-stock deal\n  in undervalued stock **[L2009-019]** does not arise.", "so the STOP on an all-stock deal\n  (\"it's impossible for that buyer to make a sensible deal in an all-stock deal\" **[L2009-019]**) does not arise."),
 ("- **Pay tied to what the person controls** **[M2003-019]**.", "- **Pay**: \"tying performance to what is actually under the reasonable control of the person that’s being measured\"\n  **[M2003-019]**."),
 ("while the owners bear the price **[M2009-081]**.", "while the owners bear the price; the\n  speakers want \"a factor in the compensation arrangement that includes a capital cost element\" **[M2009-081]**."),
 ("- **The proxy's equivalent** **[M1994-009]**.", "- **The proxy's equivalent**: \"read the proxy statements, see what they think of\" **[M1994-009]**."),
 ("\"the very large shareholders\" are named as \"The only cure\" where a board fails\n  **[M2006-011]**,", "\"The only cure to better corporate governance\" is that \"the very large shareholders start really\n  zeroing in\" **[M2006-011]**,"),
 ("below the floor on all of them **[M2003-149]**, **[L2000-024]**; the price also sits inside a range narrow enough to\n  need a pencil **[M2009-005]**.",
  "below the floor on all of them: \"there’s just a point at which we drop out of the game\" **[M2003-149]**; and the price\n  sits inside a range narrow enough to need a pencil: \"If you need to use a computer or a calculator to make the\n  calculation, you shouldn’t buy it.\" **[M2009-005]**."),
]
for old, new in R:
    n = t.count(old)
    if n != 1:
        print("NOT FOUND" if n == 0 else f"FOUND {n}x", "::", old[:80].replace("\n", " "))
        continue
    t = t.replace(old, new)
open(p, "w", encoding="utf-8").write(t)
print("done")
