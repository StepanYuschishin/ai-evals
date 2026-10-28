# Module 4 · Launch Strategy · Ascend IQ Copilot

## 4.0 Release Criteria

| Gate | Failure | Metric | Threshold | Dataset | Method | Runs at |
|---|---|---|---|---|---|---|
| Hard | #ROBUSTNESS: The agent says it cannot find SOC certification information even when the supplied reference explicitly states the certification. | Count of SOC answers that refuse, claim information is unavailable, or omit the certification when the supplied reference explicitly states it. | Zero matching SOC failures in the current 20-row regression set. Before enabling this gate, the evaluator must detect the known failure in Module 3 row 8, miss zero matching failures, and produce zero false alarms on audit-passed rows. Human validation and P0 classification approval are required. | Ascend IQ golden set | LLM judge | Release |
| Soft | Row 8 · Hallucination: contradicts the specs and criticizes a named competitor | Percentage of API comparison answers that contradict verified rate limits or make unsupported claims about a named competitor. | 0% on applicable API comparison cases in the Ascend IQ golden set. Any failure pauses release pending correction or a documented PM override. | Ascend IQ golden set | LLM judge | Staging |
| Advisory | Row 17 · Tone: slang detected | Count of cold-email drafts containing prohibited slang from the agreed brand-voice list. | 0 prohibited-slang matches. Any match triggers a warning, never blocks release. | Ascend IQ golden set | Code-based check | Pull Request |

## CI Gate Request for Engineering

- **Hard gate · #ROBUSTNESS: The agent says it cannot find SOC certification information even when the supplied reference explicitly states the certification..** Check: the LLM judge, run on the Ascend IQ golden set at Release. Measures: Count of SOC answers that refuse, claim information is unavailable, or omit the certification when the supplied reference explicitly states it.. Passes when: Zero matching SOC failures in the current 20-row regression set. Before enabling this gate, the evaluator must detect the known failure in Module 3 row 8, miss zero matching failures, and produce zero false alarms on audit-passed rows. Human validation and P0 classification approval are required.. On a fail: block the release.
- **Soft gate · Row 8 · Hallucination: contradicts the specs and criticizes a named competitor.** Check: the LLM judge, run on the Ascend IQ golden set at Staging. Measures: Percentage of API comparison answers that contradict verified rate limits or make unsupported claims about a named competitor.. Passes when: 0% on applicable API comparison cases in the Ascend IQ golden set. Any failure pauses release pending correction or a documented PM override.. On a fail: pause the release until the PM signs off on an override.
- **Advisory gate · Row 17 · Tone: slang detected.** Check: the code-based check, run on the Ascend IQ golden set at Pull Request. Measures: Count of cold-email drafts containing prohibited slang from the agreed brand-voice list.. Passes when: 0 prohibited-slang matches. Any match triggers a warning, never blocks release.. On a fail: post a warning, and don't block.

## Mitigation Plan · Soft Gate

If the API comparison Soft gate fails, pause release. With a documented PM override, disable automated API comparisons using a feature flag and route these questions to human review. Other capabilities may launch only if all Hard gates pass. Re-enable API comparisons after correcting the issue and achieving 0% failures on applicable golden-set cases.
