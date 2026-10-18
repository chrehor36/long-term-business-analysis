# Q7 range and fair price (COMPUTATION, NOT A CLEARANCE). Inputs: owner_cash_out.txt averages 2021-2025.
r=0.0543; f=0.10; sh=220.445015; nd=113.0; price=1.50
cases={ # (top: maintenance-only no growth, bottom: all spending no growth), all-equity then equity-only
 'central (Amazon charge out, AFTC in)':((1.3,-75.8),(-6.4,-83.5)),
 'ex-AFTC beside':((-16.2,-75.8-17.5),(-23.9,-83.5-17.5)),
 'Amazon charge in, beside':((-57.8,-134.9),(-65.5,-142.6)),
}
for k,((at,ab),(et,eb)) in cases.items():
    top=(at/r-nd)/sh; bot=(ab/r-nd)/sh
    fair=((at/f-nd)/sh+(ab/f-nd)/sh)/2
    etop=et/r/sh; ebot=eb/r/sh; efair=((et/f)/sh+(eb/f)/sh)/2
    print('%-38s all-equity range %.2f to %.2f fair %.2f | equity-only range %.2f to %.2f fair %.2f'%(k,bot,top,fair,ebot,etop,efair))
print('top case alone (b): all-equity fair %.2f, equity-only fair %.2f'%((1.3/f-nd)/sh,(-6.4/f)/sh))
print('owner cash needed on EV for the floor: %.1f; best case avg %.1f; best single year 36.0'%(f*(price*sh+nd),1.3))
