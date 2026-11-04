# Failure Taxonomy · Ascend IQ

## Recorded choices and reconciliation
The original choices were SOC Cert (P1), Lawsuit (priority unset), and API Limits (P1). The SOC and lawsuit frequencies were both reported as 2/20; that was a tag count, not two instances of each failure. The original API tag count of 7/20 conflicts with the saved audit's 8 hallucination calls.

## Recommended final prioritization · pending PM approval
| Rank | Failure | Trust tag | Observed evidence | Recommended priority |
|---|---|---|---|---|
| 1 | Unsupported or outdated decision-critical claims | #HALLUCINATION | 8/20 original audit calls; includes pricing and API framing; not production prevalence | P0 candidate for material fabrication, consistent with the separate M5 budget scenario; impact classification requires approval |
| 2 | Missing available SOC evidence | #ROBUSTNESS | One matching example, audit row 8 | P1 as originally selected; Hard-at-Release requires separately approved P0 justification |
| 3 | Inappropriate executive tone | #UX_TRUST | One example, audit row 16 | Advisory for editable drafts; overconfident factual advice is a distinct M5 P1 risk |

## Business impact
Unsupported material claims can distort procurement and roadmap decisions and damage trust in a service sold to enterprise accounts for upwards of $50,000 annually.

## Excluded failure and limits
The policy-compliant lawsuit refusal should be removed after PM confirmation. This list is a risk backlog, not proof that all failure modes have been discovered. Frequency is measured in a small selected batch; severity and exposure must also be assessed before assigning production priority.
