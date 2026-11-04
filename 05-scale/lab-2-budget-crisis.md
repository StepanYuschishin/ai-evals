# Module 5 · Eval Budget · Ascend IQ

**Quarterly budget cap:** $200,000
**Online eval spend:** $155,000 (2 of at most 3 online evals)

## Budget

| Failure | Trust metric | Risk | Level | Cost |
| --- | --- | :---: | :---: | ---: |
| Data Fabrication | Hallucination Rate | P0 | Online eval | $85,000 |
| Context Specificity | Robustness | P1 | Online eval | $70,000 |
| Overconfident Tone | UX Trust | P1 | Periodic audit | $6,500 |
| Data Bias | Fairness | P2 | Periodic audit | $5,500 |
| Slow Answers | Latency | P3 | Code-based check | $1,250 |

## Downgrades

### Periodic audit · Overconfident Tone (UX Trust · P1)
- **Cheaper check:** Each week, reviewers assess 50 live answers against their sources for unsupported certainty, missing caveats, and guesses presented as facts. Include predictions, sparse evidence, and conflicting sources.
- **Why it’s enough:** This audit can detect recurring confidence-calibration problems that keyword rules miss. It can miss rare cases and allows up to a week of exposure, so this is a temporary compromise. Escalate any confirmed client-impacting case immediately and review the coverage decision after 2 weeks.

### Periodic audit · Data Bias (Fairness · P2)
- **Cheaper check:** Each week, audit 50 live answers, split equally between US-focused and APAC-focused questions. Compare source coverage, factual accuracy, and fulfillment of the requested region against the same rubric.
- **Why it’s enough:** Balanced sampling can reveal systematic regional quality gaps at lower cost than continuous judging. It may miss rare failures and differences within each region. Review the allocation after 2 weeks or immediately after a material regional-quality complaint.

### Code-based check · Slow Answers (Latency · P3)
- **Cheaper check:** Before every release, run a representative suite of long, multi-step queries and automatically flag complete responses taking more than 10 seconds. Record the failure rate and P95 response time.
- **Why it’s enough:** A timer directly detects the stated latency failure without an LLM judge. Release tests may miss production load spikes, so retain production timing logs and review them weekly. This is acceptable temporarily for the stated P3 risk.


## Final-project reconciliation
- Online allocation: $85,000 + $70,000 = $155,000 per quarter; 2 of at most 3 online evals.
- Audits and code check: $6,500 + $5,500 + $1,250 = $13,250.
- Total listed allocation: $168,250. Online-cap headroom: $45,000; if the same cap covered all costs, headroom would be $31,750.
- Upgrading tone from audit to its listed $65,000 online tier raises online spend to $220,000, exceeding the cap by $20,000. Keep the proposed split pending evidence or a separately costed alternative; do not assume a third online tier is affordable.
- Regional audit should compare matched question types and comparable source availability. Weekly sampling can miss rare incidents; escalate confirmed material failures immediately.
- These are course cost assumptions and proposed coverage, not contracted spending or evidence that checks are operating.
