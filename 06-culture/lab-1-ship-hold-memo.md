# Ship-or-Hold Memo · Ascend IQ

> **Decision:** [SHIP or HOLD]

## The Answer

Hold the unrestricted rollout to the 50 enterprise accounts until the known pricing, comparison and speed defects are investigated and retested; assess a restricted pilot separately rather than assuming every capability must stop.

## The Arguments

### 1. The supplied answers contain material factual defects that could mislead client decisions.

Evidence: The pricing answer states $49 while the reference states $59. The API reference gives 500 versus 1,000 requests per minute, but the answer substitutes unsupported competitor framing. Sources: M2 audit-log.md, rows 1 and 7. These examples establish specific defects, not their production frequency.

### 2. The speed promise is not met in the supplied example, and successful error detection does not demonstrate a corrected product.

Evidence: The review-summary answer took 4.2 seconds against a 2.0-second target in M4. Each of the three M3 pricing checks detected 1 of 1 known outdated-pricing cases, but no corrected-build result is recorded. Sources: M4 gate-map.md and M3 eval-suite.md. Representative p95/p99 latency is not measured yet.

## Next Step · Decision Needed

Before approving access for the 50 accounts, approve a hold on the unrestricted rollout and assign Engineering, QA and the pricing-data owner to investigate, fix or isolate the affected functionality and retest the proposed scope. At today's review, agree a dated follow-up and require a separate approval for any restricted pilot, based on passing entry criteria and demonstrated routing and rollback controls.
