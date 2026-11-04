# AI Evaluation Strategy Canvas · Ascend IQ

Status: final-project recommendation reconstructed from the course scenario and M2–M5 artifacts; PM approval pending. Proposed controls are not implemented controls.

## 1. Product Strategy, The Context
- Target user: VP-level strategists and product leaders at enterprise clients.
- Key use case: answer market-intelligence questions using verified research, product documentation and reviews.
- Value proposition: reduce time spent finding decision-relevant information while protecting trust in a premium intelligence service.

## 2. Measurements, The Execution
User promise: Ascend IQ gives enterprise decision-makers relevant, source-supported answers quickly, preserving uncertainty and material qualifications.

| Top trust metric | Measurement | Evidence boundary |
|---|---|---|
| Hallucination / factual grounding | Unsupported, contradicted or outdated material claims divided by reviewed answers | M2 is a selected 20-answer audit, not a production-rate estimate |
| Robustness / task completion | Applicable requests completed without critical omissions or unjustified refusal | SOC row 8 is one known failure, not general robustness coverage |
| UX trust | Answers with unsupported certainty or prohibited tone divided by reviewed answers | Tone needs context-sensitive review in addition to simple slang rules |

Why these three: incorrect facts, failed requests and misplaced confidence undermine vendor decisions and enterprise retention. Monitor latency separately; text-only audits cannot measure it.

## 3. Strategic Trade-Offs
- Prioritize source support and task completion over speed when a faster answer would mislead a client. Use explicit uncertainty or human escalation when evidence is insufficient.
- Fund continuous fabrication and context checks first; temporarily use weekly tone and regional-quality audits. This accepts detection delay, not absence of risk. Review after two weeks of operation.
