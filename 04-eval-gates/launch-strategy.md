# Module 4 · Launch Strategy · Ascend IQ Copilot

## 4.0 Release Criteria

| Gate | Failure | Metric | Threshold | Dataset | Method | Runs at |
|---|---|---|---|---|---|---|
| Hard | #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions. | Count of applicable pricing answers that state an outdated price as current or include pricing conditions unsupported by the approved reference. | 0 failing applicable pricing answers in the Ascend IQ golden set. Before enabling the gate, verify that the evaluator flags the known outdated-price answer in row 1, misses zero matching cases and produces zero false alarms on audit-passed rows. | Ascend IQ golden set | Code-based check | Release |
| Soft | Row 8 · Hallucination: contradicts the specs and criticizes a named competitor | Percentage of applicable API comparison answers that contradict verified rate limits or make unsupported claims about a named competitor. | 0% failures on applicable API comparison cases in the Ascend IQ golden set. Any failure pauses release until corrected or covered by a documented PM override. | Ascend IQ golden set | LLM judge | Staging |
| Advisory | Row 17 · Tone: slang detected | Count of cold-email drafts containing prohibited slang from the agreed brand-voice list. | 0 prohibited-slang matches. Any match triggers a warning and never blocks release. | Ascend IQ golden set | Code-based check | Pull Request |

## CI Gate Request for Engineering

- **Hard gate · #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions..** Check: the code-based check, run on the Ascend IQ golden set at Release. Measures: Count of applicable pricing answers that state an outdated price as current or include pricing conditions unsupported by the approved reference.. Passes when: 0 failing applicable pricing answers in the Ascend IQ golden set. Before enabling the gate, verify that the evaluator flags the known outdated-price answer in row 1, misses zero matching cases and produces zero false alarms on audit-passed rows.. On a fail: block the release.
- **Soft gate · Row 8 · Hallucination: contradicts the specs and criticizes a named competitor.** Check: the LLM judge, run on the Ascend IQ golden set at Staging. Measures: Percentage of applicable API comparison answers that contradict verified rate limits or make unsupported claims about a named competitor.. Passes when: 0% failures on applicable API comparison cases in the Ascend IQ golden set. Any failure pauses release until corrected or covered by a documented PM override.. On a fail: pause the release until the PM signs off on an override.
- **Advisory gate · Row 17 · Tone: slang detected.** Check: the code-based check, run on the Ascend IQ golden set at Pull Request. Measures: Count of cold-email drafts containing prohibited slang from the agreed brand-voice list.. Passes when: 0 prohibited-slang matches. Any match triggers a warning and never blocks release.. On a fail: post a warning, and don't block.

## Mitigation Plan · Soft Gate

If the API comparison Soft gate fails, pause release. With a documented PM override, disable automated API comparisons using a feature flag and route these questions to human review. Other capabilities may launch only if all Hard gates pass and all other Soft failures are resolved or explicitly overridden. Re-enable API comparisons after correcting the issue and achieving 0% failures on applicable golden-set cases.
