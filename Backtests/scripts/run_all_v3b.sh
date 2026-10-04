#!/usr/bin/env bash
# Definitive corrected Book One screen (v3b) at every anchor date the program
# has used. Supersedes both the original buggy screen and the v2 attempt.
cd "$(dirname "$0")" || exit 1
for d in 2013-06-30 2014-06-30 2015-06-30 2016-06-30 2017-06-30 2018-06-30 2019-06-30 2020-06-30; do
  yr=${d:0:4}
  echo "================= $d ================="
  python screen_universe_v3b.py "$d" 2>&1 \
    | grep -iE "Hurdle|Screened|Coverage gaps|PASSES|^  OK|NO_FLOAT|CAP_BELOW|CAP_FAR|STRICT|advisory"
  cp v3b_screen_results.csv "v3b_screen_${yr}.csv"
  cp v3b_coverage_gaps.csv  "v3b_gaps_${yr}.csv"
done
echo "ALL DATES COMPLETE"
