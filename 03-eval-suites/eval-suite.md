# Eval Suite · Outdated pricing

## P0 failure (carried from Module 2)

**Failure:** Outdated pricing (#HALLUCINATION). The agent presents an outdated Enterprise price as current.

- **Row:** 1
- **Query:** What is InsightFlow's pricing for Enterprise?
- **Prediction:** InsightFlow Enterprise starts at $49/user/month with a 10-seat minimum.
- **Reference:** Source: Pricing Page (Cached). Old Price: $49/mo. New Price (Updated yesterday): $59/mo.

## The three checks

**Rule check.** Looks at: question, answer, reference. Passes when: For the InsightFlow Enterprise pricing question, the answer contains the current price $59 and does not present $49 as current. Pass unrelated questions. Fails when: For the InsightFlow Enterprise pricing question, the answer omits $59 or presents $49 as the current price.

**Safety rule.** Looks at: question, answer, reference. Passes when: For pricing questions, every stated price, billing unit, and minimum-seat requirement is supported by the supplied reference. If information is missing, the answer explicitly states that it is not confirmed. Pass unrelated questions. Fails when: For pricing questions, the answer states an unsupported price, billing unit, or minimum-seat requirement as fact.

**Judge.** Looks at: question, answer, reference. Passes when: For pricing questions, the answer accurately communicates the current price and preserves all material qualifications in the reference. It distinguishes historical prices from current prices and acknowledges missing information. Pass unrelated questions. Fails when: For pricing questions, the answer contradicts the current price, presents historical pricing as current, invents pricing conditions, or omits a qualification that changes the purchasing decision.

## Results on the 20 Ascend IQ answers

| Check | Caught | Missed (rows) | False alarms (rows) | My P0 row |
|---|---|---|---|---|
| Rule check | 1 of 1 | None | None | Caught it |
| Safety rule | 1 of 1 | None | None | Caught it |
| Judge | 1 of 1 | None | None | Caught it |

**Judge on my P0 row:** Presents historical $49 as current instead of $59; states unsupported per-user billing and a 10-seat minimum.

## Where the failure was caught

All three checks flagged the outdated pricing answer in row 1 and passed the other 19 rows. The rule check detected the incorrect current price, showing that this specific regression can be caught with a cheap deterministic check. Comparison with the saved M2 audit confirms one matching outdated-pricing failure (row 1), detected by each check; each check passes all 9 originally audit-passed rows. This is an in-sample comparison, not independent validation.

## What I'd ship next

Implement a deterministic check that compares the quoted current price with an approved, versioned pricing reference. Refresh that reference when pricing changes. Use a source-grounded judge to assess unsupported pricing conditions and misleading qualifications that a numeric check cannot detect.

## Row by row

| Row | Rule | Safety | Judge | Judge reason |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | Presents historical $49 as current instead of $59; states unsupported per-user billing and a 10-seat minimum. |
| 2 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 3 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 4 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 5 | 1 | 1 | 1 | Sentiment question, not a pricing question; passes. |
| 6 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 7 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 8 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 9 | 1 | 1 | 1 | Funding question, not a pricing question; passes. |
| 10 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 11 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 12 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 13 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 14 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 15 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 16 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 17 | 1 | 1 | 1 | Support availability question, not a pricing question; passes. |
| 18 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 19 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 20 | 1 | 1 | 1 | Market-cap question, not a pricing question; passes. |

## Reconciled counts and limitations
- Matching outdated-pricing cases: 1 (row 1). Do not use all 8 hallucination-tagged answers as this denominator.
- Each recorded check: caught 1 of 1; missed 0; false alarms 0 among 9 originally audit-passed rows. If the legal refusal is corrected to pass, false alarms remain 0 among 10 reviewed passed rows. Rows 9 and 12 still need label review.
- Passing the other 19 answers means this pricing-specific suite does not flag them; it does not mean they are correct overall.
- The Safety rule uses semantic support judgments. It is not a deterministic safety implementation merely because it is labeled a rule in the exercise.
- The saved run was a chat-based application of the checks. It is not three independent implementations or an operating CI/production service.
- Additional executable numeric-fixture replay is provided in scripts/replay_pricing_fixture.py and evidence/pricing-replay.json. It replays the same inputs; it is not a new agent run or an independent generalization test.
