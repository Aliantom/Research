<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Earnings IV/RV and term-structure screen (sell rich, avoid buying rich)

> **TL;DR:** Implied earnings moves beat realized ones in most events, but the average edge is near zero after fat tails and flips by regime, and IV-minus-RV does not predict straddle returns: forward test only.
> **Source:** trading-lab method card knowledge/methods/earnings-iv-rv-screen.yaml (deep pass 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** Premise partly true, screen unproven. Scores unchanged: edge 2, evidence 2, feasibility 3 (new sources cut both ways).

**New evidence (deep pass):**
- *Contrary to the screen:* Milian (JRFM 2023): earnings straddle returns are predicted by historical earnings move divided by implied move; historical vol, implied vol and their gap did not predict.
- Gao, Xing and Zhang (JFQA 2018): stock straddles earn negative returns on average (do not buy), but the last 3 days before the print earn +3.3% for buyers.
- IVolatility, 9,622 long straddles: win rate 22%, mean -18.5%; mean implied move 4.14% vs realized 3.32%.
- FlashAlpha, 70 events, no costs: mean harvest ratio +0.02, median +0.32, 67% implied above realized, 5th percentile -1.92 implied moves; megacaps dominate the worst events.
- ORATS: buyers averaged about -2% over 12 quarters but +45% in the latest season; the premium is regime dependent.

**Test plan (frozen):**
- Layer A, every earnings event by the 25 single names from 2026-10-29. Implied move IM from the post-print ATM straddle; HM is the mean absolute earnings move over the last 8 reports. Primary signal R = IM/HM; secondary IV30/RV30 at least 1.25 and inverted term slope. Outcome h = (IM - realized)/IM.
- Layer B, the arena `earnings_ironfly` book on AMC reports with wings at 1.0x IM, fills at mid minus half the half-spread, fees $1.00 open and $0.12 close per leg, and a random-date placebo.

**Power:** about 50 events by the Jan-Feb 2027 season, 100 by mid-2027, clustered in 4 seasons; 20 events is a futility screen only.

**Decision:** screen survives only if mean h is above zero (80% cluster-bootstrap bound) over 40+ events and rich-R beats cheap-R by at least 0.15. Kill the book if, after 20 events, net P&L is negative and any event loses a full wing. Real money (1 lot) after 40+ events with positive net P&L beating the placebo at 90% and costs at most 25% of average credit.

**Status:** researched-deep; implementability: now.

See [00 Index](../00-index.md). Card: `knowledge/methods/earnings-iv-rv-screen.yaml`.
