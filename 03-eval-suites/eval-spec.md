# Eval Spec · #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions.

| Part | Spec |
|---|---|
| Target risk | #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions. |
| Evaluator | For the InsightFlow Enterprise pricing regression case, use a deterministic check: pass only when the answer includes the current $59 price and does not present $49 as current. Pass unrelated questions. Separately, use a source-grounded judge to check whether billing units, minimum-seat requirements and other material pricing qualifications are supported by the reference. |
| Threshold | The pricing rule must flag the known outdated-price answer in row 1. On the audited regression set, require zero missed matching outdated-pricing cases and zero false alarms on audit-passed rows. These are acceptance criteria; the recorded Lab 1 comparison gives 1 of 1 matching pricing cases caught, zero misses and zero false alarms among 9 originally audit-passed rows. Supporting evidence: In the latest 20-row evaluation, all three checks flagged row 1 and passed the other 19 rows. This demonstrates detection of the known outdated-price example, but does not establish general detection accuracy. Reconciliation with the saved M2 audit gives 1 of 1 matching cases caught, zero misses and zero false alarms among the 9 originally audit-passed rows; this is in-sample evidence only. |
| Business stakes | Presenting outdated prices or unsupported purchasing conditions can mislead enterprise budgeting and vendor-selection decisions, undermine trust in Ascend IQ and put account renewals at risk. |
| Owner | PM owns acceptance criteria and the release decision. QA maintains approved regression cases and reviews false alarms and misses. Engineering implements the checks. The designated pricing-data owner keeps the approved reference current and versioned. |

## Messages

**Engineering · acceptance criteria:** For the InsightFlow Enterprise pricing regression case, return 1 only if the answer includes $59 as the current price and does not present $49 as current; otherwise return 0, and return 1 for unrelated questions. Separately, have the source-grounded judge fail pricing answers that state unsupported billing units, minimum-seat requirements or other material pricing qualifications; acceptance requires flagging row 1, zero missed matching outdated-pricing cases and zero false alarms on audit-passed rows, with counts reconciled against the saved Lab 1 audit.

**Design · what the user sees:** When a pricing check blocks an answer, hide the rejected pricing claims and show: “We couldn’t verify the pricing details. Please check the official pricing source or request a human review.”

**Leadership · risk and return:** These checks reduce the risk of clients making budgeting and vendor-selection decisions using outdated prices or unsupported purchasing conditions. A cheap deterministic check catches the known price regression, while a source-grounded judge assesses qualifications that numeric matching cannot reliably evaluate; broader detection accuracy remains unproven.
