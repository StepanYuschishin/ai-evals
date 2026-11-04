# Ship-or-Hold Memo · Ascend IQ

**HOLD the proposed broad rollout to 50 enterprise accounts on the supplied course evidence: the known pricing answer fails the chosen Hard release criterion.**

To: CPO, Engineering Lead, QA · From: Stepan Yuschishin · 2026-11-04
Scope: final-project recommendation about the evaluated course build/batch, not a claim about an unseen newer build or an actual deployment decision.

## The Answer
Do not approve the broad rollout on the current evidence. The saved answer quotes $49 while the source says $59. Our agreed pricing Hard gate requires zero failing applicable cases. M3 detects this answer; it does not demonstrate that the product has been fixed. Request the corrected answer and rerun before revisiting launch.

## The Arguments
### 1. The current pricing example fails our explicit quality bar
M2 row 1 is an unambiguous source contradiction. M4 assigns pricing Hard at Release. Zero bad applicable pricing answers is the proposed bar; one is recorded. No disputed overall failure rate is needed to reach this conclusion.
### 2. Speed is central to the product promise, and the supplied task misses its target
M1 prioritizes Latency, Hallucination Rate and UX Trust. The M4 review-summary case takes 4.2 seconds against 2.0 seconds: FAIL for that task. This is one sample, not p95/p99. Soft means a documented restricted exception is possible; it cannot override the pricing Hard failure.
### 3. Detection and budget are now designed, but are not evidence of a successful fix
The M3 pricing suite records 1 of 1 known pricing cases caught by each check, zero misses and zero false alarms among 9 originally audit-passed examples. This is narrow in-sample detection evidence. M5 allocates $155,000 online and $168,250 including fallback audits/checks, within its stated online cap. Neither establishes that a corrected build passes.

## Evidence · Results versus criteria
| Metric / case | Result | Bar | Outcome | Source |
|---|---|---|---|---|
| Current pricing, course answer | $49 quoted; $59 reference; 1 failing applicable answer | 0 failures | FAIL / Hard | M2 row 1, M3 row 1, M4 launch strategy; deterministic replay in evidence/pricing-replay.json |
| Pricing detector on known matching case | Each of three recorded chat checks catches 1 of 1; misses 0; false alarms 0 among 9 original audit-passed cases | Catch known case, zero matching misses/false alarms | PASS for this sample only | M3 suite; M2 original labels |
| Review-summary response time | 4.2 seconds, one supplied observation | <=2.0 seconds for this task | FAIL / Soft | M4 row 3 |
| API answer | Omits verified limits, adds unsupported competitor framing | 0% material contradictions / unsupported competitor claims in applicable cases | FAIL on supplied example / Soft with restricted-scope mitigation | M2 row 7; M4 row 8 |
| Cold-email slang | “killer”, “total game changer” present | 0 prohibited slang matches | WARN / Advisory | M4 row 17 |
| Legal refusal | Follows explicit refusal policy | Follow policy | PASS / No gate | M2 row 13; M4 row 14 |
| Supplied PR #218 grounding | 87; main 96; regression 9 points | floor 90; max regression 3 | FAIL / BLOCK this demo PR | M4 CI policy, separate 30-case supplied scenario |
| Online allocation | $155,000; 2 online evals | <=$200,000; at most 3 | PASS / plan | M5 budget |

## Business Risk
The brief identifies declining engagement, Q4 retention pressure and slow access to insights. Fifty accounts at upwards of $50,000 annually imply more than $2.5 million in annual account value, not forecast loss. Incorrect prices can mislead purchasing decisions; delay risks postponing the retention benefit. We have no measured churn impact or client satisfaction study, so neither loss nor benefit is invented.

## Next Step · Decision Needed
At today's presentation, approve HOLD on broad rollout and assign Engineering the pricing/source fix, QA the replay and label reconciliation, PM the acceptance and scope decision, and the pricing-data owner reference freshness. Request an owner-agreed rerun date before ending the review; no delivery date is asserted as committed.

Exit criteria: pricing passes the 0-failure Hard bar on applicable current-reference cases, including the corrected row 1 and unsupported-term checks; evaluator counts are reconciled; other Soft failures are fixed or have documented scope/risk mitigation; all Hard gates pass. Add representative timing evidence before claiming p95/p99 performance. A limited pilot is a separate approval with defined stop rules and retained protections, not an automatic substitute for failed gates.

## Reflection
The key distinction is between a check catching an error and the agent no longer making that error. Our successful pricing detection supports a control choice; it does not turn a bad answer into a good one. Likewise, a policy-compliant refusal should not be treated as a failure, and a small targeted batch should not be described as production accuracy.
