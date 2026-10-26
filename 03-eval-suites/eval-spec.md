You are helping a PM turn an eval spec into short messages for three teams. Use plain, direct language and keep every number from the spec exactly as it is.

MY SPEC
Target risk: #ROBUSTNESS: The agent says it cannot find SOC certification information even when the supplied reference explicitly states the certification.
Evaluator: For SOC certification questions, compare the answer with the supplied reference. Fail if the reference explicitly states a certification but the answer refuses, claims the information is unavailable, or omits the certification. Pass unrelated questions for this check. If the reference contains no certification evidence, allow an explicit statement of uncertainty.
Threshold: On the current 20-row regression set: detect the known SOC failure in row 8, miss zero matching failures, and produce zero false alarms on audit-passed rows. Require human review before using this check as a release gate.
What supports the threshold: Row 8 is the known matching case: the answer says it cannot find compliance documents, while the reference states "SOC2 Type II Certified." The previous Rule and Safety checks failed all 20 rows, while the previous Judge passed row 8 because it inspected the reference only. These results justify redesigning the checks, not claiming validated detection performance. Final Module 2 audit scores are still needed to calculate false alarms.
Business stakes: Missing available SOC certification evidence can mislead VP-level clients during vendor screening, delay procurement, and reduce trust in Ascend IQ.
Owner: PM owns the acceptance criteria and release decision. QA maintains the regression cases and reviews errors. Engineering implements the check and fixes retrieval or answer-generation failures.

Write three messages, one or two sentences each:
- Engineering: the acceptance criteria, as an exact pass and fail rule, so an engineer could build the check without asking a question.
- Design: what the user sees when the check blocks an answer.
- Leadership: the risk this removes, and why it is worth the cost.

Reply with the complete contents of a file called eval-spec.md, in exactly this format and nothing else:

# Eval Spec · #ROBUSTNESS: The agent says it cannot find SOC certification information even when the supplied reference explicitly states the certification.

| Part | Spec |
|---|---|
| Target risk | [from my spec] |
| Evaluator | [from my spec] |
| Threshold | [from my spec, with what supports it] |
| Business stakes | [from my spec] |
| Owner | [from my spec] |

## Messages

**Engineering · acceptance criteria:** [message]

**Design · what the user sees:** [message]

**Leadership · risk and return:** [message]
