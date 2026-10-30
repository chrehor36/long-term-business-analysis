# Segment cash proxy, FY3/25 and FY3/26, yen bn: OI + content amortization - content additions (content note, by class).
# Pictures = film costs + broadcasting rights; Music = catalogs + artist contracts + distribution rights; G&NS = game content.
# NOT owner earnings: pre-tax, before non-content capex (not disclosed by segment except I&SS) and before working capital.
d = {
 'FY3/25': dict(pic_oi=117.284, mus_oi=357.255, gns_oi=414.819, iss_oi=261.147,
   film_am=328.167, br_am=110.057, cat_am=51.825, art_am=2.760, dist_am=3.639, game_am=39.381,
   film_add=425.914, br_add=112.579, cat_add=141.927, art_add=4.941, dist_add=0.017, game_add=56.013, game_imp=0.545),
 'FY3/26': dict(pic_oi=104.872, mus_oi=446.986, gns_oi=463.258, iss_oi=357.318,
   film_am=378.855, br_am=96.772, cat_am=59.510, art_am=3.776, dist_am=2.236, game_am=54.029,
   film_add=475.564, br_add=104.069, cat_add=152.768, art_add=3.706, dist_add=0.171, game_add=72.438, game_imp=56.347),
}
for y, v in d.items():
    pic = v['pic_oi'] + v['film_am'] + v['br_am'] - v['film_add'] - v['br_add']
    mus = v['mus_oi'] + v['cat_am'] + v['art_am'] + v['dist_am'] - v['cat_add'] - v['art_add'] - v['dist_add']
    gns = v['gns_oi'] + v['game_am'] + v['game_imp'] - v['game_add']
    print(y, f"Pictures {pic:.1f}  (OI {v['pic_oi']:.1f}; content additions exceed amortization by {v['film_add']+v['br_add']-v['film_am']-v['br_am']:.1f})",
          f"| Music {mus:.1f} (OI {v['mus_oi']:.1f})", f"| G&NS {gns:.1f} (OI {v['gns_oi']:.1f}, game-content impairment added back {v['game_imp']:.1f})")
