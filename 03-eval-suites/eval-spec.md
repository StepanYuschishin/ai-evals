# Eval Spec · Missing available SOC evidence

Status: redesigned specification; independent execution and human calibration pending.

| Part | Spec |
|---|---|
| Target risk | Agent says SOC evidence is unavailable although the supplied reference explicitly states a certification |
| Evaluator | Compare query, answer and reference together. For SOC questions, fail if explicit certification evidence is refused, contradicted or omitted. Pass unrelated questions for this narrow check. Without certification evidence, permit explicit uncertainty. Attribute a badge to the source; do not claim an independently verified audit or invent scope/dates. |
| Threshold | Proposed regression acceptance: detect known row 8, zero missed matching failures, zero false alarms on adjudicated passing rows. These are targets, not achieved results. Validate on held-out cases before enabling a gate. |
| Business stakes | Misleading vendor screening, procurement delay and reduced client trust |
| Owner | QA owns labeled cases and error review; Engineering implements and fixes retrieval/generation; PM approves acceptance criteria and release; domain reviewer confirms material compliance interpretation |

## Messages
**Engineering · acceptance criteria:** Implement the query/answer/reference check above. Report TP, FN, FP and TN against approved labels, and demonstrate expected handling of missing evidence and unrelated queries before blocking releases.

**Design · what the user sees:** If an enabled control blocks a response, show that the source evidence needs review and offer human escalation; do not imply certification is absent or verified without support.

**Leadership · risk and return:** This targets a known vendor-screening failure. Retain HOLD on broad launch until the evaluator and response controls have been validated; no performance or implementation claim is made here.
