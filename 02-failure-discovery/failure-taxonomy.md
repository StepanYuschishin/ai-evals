# Failure Taxonomy · Ascend IQ

## Top 3 Prioritized Failures

| Rank | Failure | Trust Tag | Frequency | Severity |
|---|---|---|---|---|
| 1 | Outdated pricing | #HALLUCINATION | 8/20, HIGH | P0 |
| 2 | Misleading API comparison | #HALLUCINATION | 8/20, HIGH | P0 |
| 3 | Missing SOC evidence | #ROBUSTNESS | 1/20, LOW | P1 |

## #1 Risk · Business Impact

This failure matters because presenting outdated pricing as current can lead enterprise clients to make incorrect purchasing and budgeting decisions, undermining trust in Ascend IQ and putting account renewals at risk.

## Frequency and release-policy interpretation
8/20 is the number of original audit calls with the hallucination tag, not eight wrong-price cases or eight API failures. The course matrix maps high tag frequency + high assessed impact to P0. It does not statistically establish production crisis frequency.

Pricing P0 is enforced as Hard at Release in M4. API is also ranked P0 by this course matrix but assigned Soft in the saved M4 map. The final policy resolves the residual risk as follows: an override may permit other features only after API comparisons are disabled and affected requests are routed to human review. An override must not expose the unmitigated P0 API behavior. This is a proposed mitigation, not an implemented feature flag.
