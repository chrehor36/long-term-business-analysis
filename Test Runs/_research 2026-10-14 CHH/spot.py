import sys,io,csv,re,unicodedata
R={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('’',"'"),('‘',"'"),('“','"'),('”','"'),('—','-'),('–','-'),('�','')]: s=s.replace(a,b)
    s=s.replace('"','').replace("'",'')
    return re.sub(r'\s+',' ',s).strip().lower()
tests=[('L2000-021','How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the risk-free interest rate'),
('L2016-006','A management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous'),
('M2023-081','We’re not earning a higher rate of return on capital than we were when we started. We just put way more capital into the business'),
('M1994-018','We regard it is a negative when we find a management that’s preoccupied with accounting considerations. But, we find it so frequent that we can’t afford to use it as a total exclusionary factor'),
('R1996-018','the discounted value of the cash that can be taken out of a business during its remaining life'),
('M2006-077','where the facts and reasoning lead'),('M2025-032','what the figures are saying'),('M2012-081','We are never going to risk what we have and need for what we don’t have and don’t need'),
('L2014-005',"borrowed money has no place in the investor's tool kit"),('M1997-109','if the market closed for five years'),('M1996-084','if you have to actually do it on — with pencil and paper, it’s too close to think about'),
('M2001-090','the value of having the brand moves over to the retailer from the product itself'),('M1995-038','why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now. What are the key factors? And how permanent are they?'),
('M2012-065','a reasonable fix on about what the earning power and competitive position will look like in five or 10 years'),('M2000-037','where the business will be in 10 years'),('M1997-024','if I think I understand a business and I don’t'),
('L2007-005','A moat that must be continuously rebuilt will eventually be no moat at all'),('M2025-013','I’m looking for what’s wrong in things because that’s part of investing'),('M1999-129','What do I not know that I need to know?'),
('M2003-149','We don’t want to buy equities where our real expectancy is below 10 percent'),('M2019-015','You can turn any investment into a bad deal by paying too much'),('M1998-110','Almost any management that wants to retain money is going to rationalize it'),('L2011-003','Continuing shareholders are hurt unless shares are purchased below intrinsic value')]
for i,q in tests: print(i, norm(q) in norm(R[i]))
