# Ship-or-Hold Memo · Ascend IQ

**HOLD the unrestricted 50-account rollout; qualify a restricted pilot as the next option, subject to separate entry criteria and approval.**

To: CPO, Engineering Lead, QA · From: Stepan Yuschishin · Course final-project recommendation

## The Answer
The supplied examples expose pricing, comparison and speed defects. They do not establish that every capability is unsafe or reveal production recurrence. Broad rollout is not supported by the current evidence, but a total product shutdown is not established either. Investigate causes, fix or exclude affected capabilities, validate the remaining scope and return for a pilot decision.

## Three Arguments
1. **Decision quality is at risk.** The pricing answer states $49 versus a $59 reference and includes unsupported conditions. The API answer supplies unsupported framing instead of the source-supported comparison. These are specific observed defects, not estimated production rates.
2. **The speed promise needs evidence.** One review-summary example takes 4.2 seconds versus a 2.0-second target. This is a task-level failure, not p95/p99 or measured retention impact. The M1 promise includes speed as well as grounding and UX trust.
3. **Protection is designed, not yet demonstrated at rollout scope.** M3 recorded checks detect the one known pricing failure; this does not show a corrected agent or general detection accuracy. The $155,000 online plan is affordable under the $200,000 online cap; implementation and staffing remain to be demonstrated before relying on it.

## Evidence versus chosen criteria
| Evidence | Result | Criterion | Meaning |
|---|---|---|---|
| Pricing, M2/M3 row1 | $49 vs current $59; 1 bad applicable answer | M4 candidate including pricing: 0 material pricing failures | Fails that candidate's chosen Hard gate; root cause/recurrence unknown |
| API, M2 row7 / M4 row8 | Unsupported framing; source 500 vs 1,000 req/min | Supported relevant comparison; M4 Soft policy | Fix or exclude automated comparisons with validated routing |
| Speed, M4 row3 | 4.2 seconds | 2.0-second task target | Soft failure for that task; more timing evidence needed |
| Pricing detector, M3 | Each of three recorded checks flags 1 of 1 known cases; 0 misses | Detect known example | In-sample detection success, not a corrected-output pass |
| Budget, M5 | $155,000 online; 2 online evals; total $168,250 | <=$200,000 online; max3 | Feasible planned allocation, not operational readiness |

## Policy interpretation
The earlier pricing Hard rule is a PM policy for a release that includes automated pricing, not evidence that every feature must stop. A restricted candidate excluding affected features is a different scope. It requires demonstrated exclusions, QA evidence for remaining tasks and explicitly approved scope-specific gates. It cannot simply waive the failed Hard criterion. Pilot readiness is not established today.

## Business trade-off
Holding broad access delays the hoped-for engagement/retention benefit. Launching untested decision-support answers exposes clients to incorrect purchasing information. The brief's 50 accounts paying upwards of $50,000 imply more than $2.5m annual account value; that is neither expected loss nor revenue attributable to Ascend IQ. No causal churn estimate is available.

## Ask and next evidence
At today's review, approve HOLD on the unrestricted scope, assign owners and agree a dated follow-up before the meeting ends. Engineering/pricing-data owner diagnose stale source versus retrieval versus generation and fix or exclude affected functionality. QA retests corrected and representative in-scope tasks. PM/Engineering define pilot scope, stop rules and demonstrate routing/rollback. CPO approves a pilot only after its entry criteria pass. No pilot account count or committed delivery date is invented.

## Reflection
An observed failure justifies investigation and a containment decision; its scope must not be assumed. A successful detector does not fix a product answer. A written gate does not prove its own severity or implementation. The management decision is about exposure, evidence and scope—not counting negative slides.

Sources: M1 strategy-canvas.md; M2 audit-log.md and failure-taxonomy.md; M3 eval-suite.md/eval-spec.md; M4 gate-map.md/launch-strategy.md; M5 lab-2-budget-crisis.md. Full reasoning: evidence/managerial-decision.md.
