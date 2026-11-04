# Decision register · how each choice follows from the labs

| Decision | Evidence | Reasoning | Limit / what would change it |
|---|---|---|---|
| HOLD broad rollout on supplied batch | M2/M3 row 1: $49 vs $59; M4 pricing Hard with zero failures | One known failing Hard case is sufficient; no fixed-build pass recorded | Corrected build passing approved gates can change the call |
| Latency stays prominent | M1 promise and metric; M4 4.2 vs 2.0 seconds | Speed motivates the product, but a wrong fast answer fails decision quality | One sample does not establish p95/p99; measure representative runs |
| Cheap numeric pricing check first | M3 three checks all flag the same one case; deterministic replay also fails row 1 | Numeric mismatch is directly checkable without paying a semantic judge | Current implementation is a frozen fixture replay; source freshness and semantic terms are separate |
| Judge for unsupported conditions/API framing | M2 row 1 seat minimum unsupported; API answer contains no numeric comparison | Literal matching does not assess these meanings | Requires calibration; chat review is not proof of robust production detection |
| Legal refusal No gate | Reference explicitly says refuse legal queries | Evaluator should not punish compliance | Change only if product policy is revised |
| Slang Advisory | Editable draft and agreed brand prohibition | Warning preserves editable workflow without blocking every release | Different auto-send workflows may justify stricter policy |
| API Soft with restricted mitigation | M4 chosen Soft; M2 course priority P0 | Allow other features only after automated API comparisons are disabled and requests routed to humans | Never waive an unmitigated P0 exposure; implementation not demonstrated |
| Two online evals | M5 $85k fabrication + $70k context = $155k | Focus online spend on listed P0/P1 risks | Tone $65k online would make $220k; fallback accepts delayed detection |
| Budget timing check uses 10s, M4 uses 2s | Distinct tasks in supplied labs | Keep task-specific bars separate | Neither yields an end-to-end time-to-insight improvement measurement |
| Coverage is an appendix | M5 maps AI Report Summaries, not Ascend IQ | Demonstrates portfolio prioritization; cannot support Ascend IQ readiness directly | Need an Ascend IQ-specific coverage audit for that claim |

Taxonomy tag frequencies are course audit counts, not production rates. Original M2 labels are retained; the legal correction and unresolved rows are explicit. This register records final-project reasoning, not stakeholder approval or operating controls.
