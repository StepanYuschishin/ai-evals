# Module 4 · Launch Strategy · Ascend IQ Copilot

## 4.0 Release Criteria

| Gate | Failure | Metric | Threshold | Dataset | Method | Runs at |
|---|---|---|---|---|---|---|
| Hard | #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions. | Count of applicable pricing answers that state an outdated price as current or include pricing conditions unsupported by the approved reference. | 0 failing applicable pricing answers in the Ascend IQ golden set. Before enabling the gate, verify that the evaluator flags the known outdated-price answer in row 1, misses zero matching cases and produces zero false alarms on audit-passed rows. | Ascend IQ golden set | Code-based price check plus source-grounded judge for pricing qualifications | Release |
| Soft | Row 8 · Hallucination: contradicts the specs and criticizes a named competitor | Percentage of applicable API comparison answers that contradict verified rate limits or make unsupported claims about a named competitor. | 0% failures on applicable API comparison cases in the Ascend IQ golden set. Any failure pauses release until corrected or covered by a documented PM override. | Ascend IQ golden set | LLM judge | Staging |
| Advisory | Row 17 · Tone: slang detected | Count of cold-email drafts containing prohibited slang from the agreed brand-voice list. | 0 prohibited-slang matches. Any match triggers a warning and never blocks release. | Ascend IQ golden set | Code-based check | Pull Request |

## CI Gate Request for Engineering

- **Hard gate · #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions..** Check: the code-based check, run on the Ascend IQ golden set at Release. Measures: Count of applicable pricing answers that state an outdated price as current or include pricing conditions unsupported by the approved reference.. Passes when: 0 failing applicable pricing answers in the Ascend IQ golden set. Before enabling the gate, verify that the evaluator flags the known outdated-price answer in row 1, misses zero matching cases and produces zero false alarms on audit-passed rows.. On a fail: block the release.
- **Soft gate · Row 8 · Hallucination: contradicts the specs and criticizes a named competitor.** Check: the LLM judge, run on the Ascend IQ golden set at Staging. Measures: Percentage of applicable API comparison answers that contradict verified rate limits or make unsupported claims about a named competitor.. Passes when: 0% failures on applicable API comparison cases in the Ascend IQ golden set. Any failure pauses release until corrected or covered by a documented PM override.. On a fail: pause the release until the PM signs off on an override.
- **Advisory gate · Row 17 · Tone: slang detected.** Check: the code-based check, run on the Ascend IQ golden set at Pull Request. Measures: Count of cold-email drafts containing prohibited slang from the agreed brand-voice list.. Passes when: 0 prohibited-slang matches. Any match triggers a warning and never blocks release.. On a fail: post a warning, and don't block.

## Mitigation Plan · Soft Gate

If the API comparison Soft gate fails, pause release. With a documented PM override, disable automated API comparisons using a feature flag and route these questions to human review. Other capabilities may launch only if all Hard gates pass and all other Soft failures are resolved or explicitly overridden. Re-enable API comparisons after correcting the issue and achieving 0% failures on applicable golden-set cases.

## Pricing check scope
Code validates the numeric price against an approved, versioned reference. A source-grounded judge checks unsupported billing units, minimum seats and material qualifications. Either failing blocks the pricing Hard gate. Run numeric fixtures at PR too, and reconfirm reference freshness before Release. $59 is the current course fixture, not a permanently hard-coded production truth. The known current fixture fails: it states $49.

## Other Soft gates from the map
- Speaker status: 0 unsupported confirmations in applicable gold cases; status matching at PR when structured, contextual judging at Staging. Saved case lists invited Sam Altman as confirmed: FAIL; fix or use documented restricted-scope mitigation.
- Review-summary latency: complete response <=2.0 seconds in the provided task; supplied observation 4.2 seconds: FAIL. Measure with a timer at Staging, not a judge. This is one observation, not p95/p99. Pause for fix or a documented time-limited, restricted rollout exception; preserve the failed result and monitor timing.

## CI Gate Policy
Use the six per-dimension floors, regression limits and blocking flags in lab-ci-gate-policy.md on the supplied 30-case replay. A blocking dimension fails if below its floor OR its regression exceeds its maximum. No blended score can cancel that failure. PR #218 is BLOCKED by grounding 87 < 90 and a 9-point drop >3. This is the supplied demo, not a live agent or CI run.

## Current gate outcomes and exit evidence
Pricing: FAIL on the audited row 1. API: FAIL on the supplied comparison because the output substitutes unsupported framing for verified 500 vs 1,000 limits; this is contextual review, not an independent newly calibrated model run. Slang: WARN on the supplied draft. Policy refusal: PASS/no failure gate. Latency: FAIL on the single supplied 4.2-second observation against 2.0 seconds. No corrected-build rerun is available. Detection of a bad answer in M3 validates detection of that example; it does not fix the answer.
