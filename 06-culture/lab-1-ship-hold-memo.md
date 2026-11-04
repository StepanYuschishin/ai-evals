# Ship-or-Hold Memo · Ascend IQ

**Recommendation: HOLD broad rollout to the top 50 enterprise accounts.** The current evidence does not establish that the proposed controls reliably detect material failures.

To: CPO · Engineering Lead · QA
From: Stepan Yuschishin · 2026-11-04
Status: proposed final-project recommendation for PM approval; not an executed deployment decision.

## The Answer
Hold broad client rollout while Engineering and QA validate the redesigned evaluator, reconcile labels and demonstrate release controls. Prepare internal shadow testing with existing protections retained. A limited client pilot requires a separate readiness decision.

## The Arguments
### 1. Known failures undermine decision quality
The original audit records 11 failed calls in a selected 20-answer batch. At least one is a policy-compliant refusal, so these labels require adjudication. Pricing, API framing and omitted SOC evidence nevertheless provide concrete failure examples.
### 2. Proposed gates do not establish operational protection
The old SOC checks were mis-scoped. The replacement is a written spec without independent rerun/calibration evidence. SOC is P1 in M2 but conditionally Hard/P0 in M4. This must be resolved before using it as a release gate.
### 3. The budget is defensible, but accepted risks remain
The plan funds fabrication and context checks online for $155,000 quarterly, with $13,250 for audits and timing checks. Tone and regional audits accept delayed detection and require incident escalation. Budget allocation is not implemented coverage.

## Evidence · Results versus proposed bars
| Evidence | Recorded result | Proposed bar / interpretation | Status |
|---|---|---|---|
| M2 selected audit | 11/20 original failed calls: 8 hallucination, 2 robustness, 1 UX | Labels need adjudication; correcting only the policy refusal yields 10/20, not a final validated rate | REVIEW |
| M3 old SOC checks | Rule and Safety fail all 20; reference-only Judge passes known SOC failure | Compare answer with reference; detect row 8 without false alarms on approved negatives | NOT VALIDATED |
| M3 redesigned SOC evaluator | No independent run recorded | Proposed zero missed matching failures and zero false alarms on regression; held-out validation required | NOT MEASURED |
| M4 API gate | No current regression outcome recorded | Proposed 0% material contradictions/unsupported competitor claims on applicable cases | NOT MEASURED |
| M4 PR #218 provided replay | Grounding 96 → 87 | Floor 90; max regression 3 points | FAIL in supplied scenario |
| M5 budget | $155,000 online; 2 checks; $168,250 total | Online cap $200,000; max 3 | PASS, planned allocation only |

Sources: M2 audit-log.md; M3 eval-suite.md and eval-spec.md; M4 launch-strategy.md and lab-ci-gate-policy.md; M5 lab-2-budget-crisis.md. The AI Report Summaries coverage exercise describes another product and cannot establish Ascend IQ coverage.

## Business Risk
The scenario's 50 accounts paying upwards of $50,000 annually represent more than $2.5 million in annual account value. This is exposure context, not forecast loss or revenue attributable to Ascend IQ. A poor rollout could harm client decisions and retention. Holding delays the proposed retention benefit; its monetary cost and churn effect are not measured. No invented loss estimate is used.

## Next Step · Decision Needed
Proposed ask for 2026-11-05: CPO approves HOLD on broad launch, Engineering and QA ownership, and the validation work. Proposed evidence review: 2026-11-11; dates require owner agreement.

Exit requirements:
1. QA and PM adjudicate the 20 labels, including refusal, funding and brand-color cases; document uncertainty and sample limits.
2. Engineering reruns the redesigned SOC evaluator against approved references and an independent held-out set; QA reviews flagged AND passed answers, with precision/recall and raw error counts. Critical misses remain release blockers under the approved policy.
3. Resolve SOC severity versus Hard-gate placement. Test the actual approved P0 fabrication control and the API Soft gate; a narrow SOC check does not cover all fabrication.
4. Record trajectory and judge-calibration evidence, including critical omissions and tool/source choices; identify any course demo as a demo.
5. Demonstrate failure routing, feature flags, human escalation and rollback before a limited pilot. Run old/new comparisons and protected shadow evaluation, including regional segments, before widening exposure.
6. Confirm audit staffing, production timing review, escalation owners and the two-week coverage review. Define quantitative pilot expansion/stop criteria before approval; they are not yet agreed.

## Reflection
A completed document is not a passed gate. The most important finding is that evaluator mistakes can create false confidence: a policy-compliant refusal was labeled a failure, and a reference-only judge missed the actual answer problem. The decision must reflect evidence quality as well as output quality.
