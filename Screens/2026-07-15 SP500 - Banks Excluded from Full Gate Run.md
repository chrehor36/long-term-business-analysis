# S&P 500 batch — banks held out per standing "ignore banks" instruction

Of the 47 S&P 500 mechanical-screen passes, 6 are literal depository/commercial
banks. Consistent with every other screen in this project (most recently
Suruga Bank/SUGBY held out of the 2026-07-15 Japan batch — see the note at the
bottom of `Test Runs/2026-07-15 Run - SOMLY (Secom Co).md`), these are held
out of the full gate-by-gate run rather than analyzed:

- RF — Regions Financial
- BAC — Bank of America
- USB — U.S. Bancorp
- PNC — PNC Financial Services
- WFC — Wells Fargo
- MTB — M&T Bank

**41 of the 47 passes proceed to full gate-by-gate treatment.**

Non-bank financials (Synchrony/SYF, Aflac/AFL, Globe Life/GL, T. Rowe Price/
TROW, Ameriprise/AMP, PayPal/PYPL) are NOT banks in the excluded sense — they
proceed to full gate-by-gate treatment, with Ruling 2's mechanical leverage
ceiling (assets/equity > 10:1 = automatic Gate 4 FAIL) applied where the
business is genuinely balance-sheet-levered (lender/insurer), judgment
documented per-company the way the REIT batch documented its Fortress-track
interpretation call.
