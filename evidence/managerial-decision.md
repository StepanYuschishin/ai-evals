# Managerial rollout decision · supersedes the earlier unconditional HOLD rationale

## Assignment
Decide whether to approve unrestricted Ascend IQ access for the 50 enterprise accounts in the course brief. The business goal is faster access to reliable intelligence and protecting retention.

## Recommendation
HOLD approval of the proposed unrestricted rollout. Investigate the known defects and qualify a separately approved restricted pilot. This is not evidence that every capability is unsafe, and it is not approval to start a pilot today.

## Why
The supplied answers contain an outdated price ($49 versus a $59 current reference), an unsupported API comparison, and a review-summary task taking 4.2 seconds versus its 2.0-second target. The labs establish these specific defects, not their production frequency or systemic scope. The M3 checks catch the known pricing answer; they do not demonstrate a corrected agent. There is no corrected-build result or demonstrated exclusion/rollback control in the record.

The prior M4 pricing Hard gate is a chosen PM policy for a candidate that includes automated pricing. It does not by itself prove the whole product must be stopped. Keeping that policy means the current unrestricted candidate cannot pass. An alternative candidate may exclude pricing/API only if the exclusion actually works, risks to remaining tasks are tested, and the scope-specific acceptance criteria are approved. That is a new candidate/readiness decision, not an override pretending the old Hard gate passed.

## Next actions and exit evidence
- Engineering and the pricing-data owner determine whether the pricing defect came from stale source, retrieval or generation; fix or contain it. Root cause is currently unknown.
- QA reruns corrected outputs and tests additional representative, in-scope pricing/other tasks with human-adjudicated labels. Passing one known case does not establish broad readiness.
- Engineering demonstrates scope exclusions, human routing and rollback if relied on. Their availability is not asserted.
- PM proposes pilot account/capability scope, stop rules, owners and an evidence review date. The CPO approves before client access.
- For a candidate including pricing, retain the chosen zero-material-pricing-failure bar and supported-terms review. For a candidate excluding it, validate that boundary and the remaining applicable gates. Resolve Soft risks or document acceptable mitigations for that approved scope.

No numeric pilot size, success rate, production failure probability, retention uplift or delivery deadline is invented. $155,000 online / $168,250 total remains a planning allocation, not operational coverage.

## Evidence map
M1: strategy-canvas.md (promise/metrics). M2: audit-log.md (specific answers) and failure-taxonomy.md (prioritization). M3: eval-suite.md/eval-spec.md (detection and controls). M4: gate-map.md/launch-strategy.md (chosen policy, example timing). M5: lab-2-budget-crisis.md (costs). M6 memo synthesizes these; it is not an independent source of model performance. Separate-product coverage and supplied CI demo remain appendix artifacts, not readiness measurements for this candidate.
