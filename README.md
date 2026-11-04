# Ascend IQ · Final AI Evals Project

**Recommendation: HOLD broad rollout on the supplied course evidence.** Row 1 quotes $49 against a current $59 reference and fails the chosen zero-failure pricing Hard gate. The successful detector result is not evidence that the answer was fixed.

## Presentation and preparation
The main presentation has 6 slides. Each ends with its explicit impact on the 50-account SHIP/HOLD decision. Full lab details remain in the presenter edition and evidence bundle.

- [Audience slides](final-presentation.html)
- [Presenter slides with full evidence and Ukrainian notes](presenter-with-evidence.html)
- [Ukrainian 4–5 minute speech](06-culture/speaker-notes-uk.md)
- [Questions and answers](06-culture/questions-and-answers-uk.md)
- [Action plan](FINAL-PROJECT-PLAN-UA.md)
- [Full evidence bundle](ALL-EVIDENCE-UA.md)
- [Decision register](evidence/decision-register.md)

## Module artifacts
| Module | Files | Evidence status |
|---|---|---|
| M1 | [Strategy](01-evaluation-strategy/strategy-canvas.md) | User-updated promise: latency, hallucination, UX trust; duplicated paragraphs removed |
| M2 | [Audit](02-failure-discovery/audit-log.md), [taxonomy](02-failure-discovery/failure-taxonomy.md) | Original labels preserved; correct legal refusal separated; disputed negatives disclosed |
| M3 | [Suite](03-eval-suites/eval-suite.md), [spec](03-eval-suites/eval-spec.md) | Chat-based pricing run; caught 1/1; narrow code replay also executed |
| M4 | [Gate map](04-eval-gates/gate-map.md), [launch strategy](04-eval-gates/launch-strategy.md), [CI scenario](04-eval-gates/lab-ci-gate-policy.md) | Pricing Hard; API restricted-scope Soft; latency Soft; slang Advisory; legal refusal No gate |
| M5 | [Coverage](05-scale/lab-1-coverage-matrix.md), [budget](05-scale/lab-2-budget-crisis.md) | Separate-product coverage; planned online155k, total168250 |
| M6 | [Memo](06-culture/lab-1-ship-hold-memo.md), [deck](06-culture/lab-2-final-pitch.html) | Decision follows observed result versus chosen bar |

## Reproduce numeric fixture replay
Run `python3 scripts/replay_pricing_fixture.py` with the standard Python library. Output: [pricing-replay.json](evidence/pricing-replay.json). Input: [20 original cases](evidence/ascend-iq-20-cases.csv). This is a narrow frozen-fixture test; unfamiliar applicable wording returns REVIEW. No live model, production or semantic-judge execution is claimed.

## Provenance and limits
User's pre-reconciliation source files are preserved under evidence/snapshots/6df9e89/. Evidence labels distinguish supplied course data, recorded chat outputs, executed numeric replay and proposed policies. The audit is selected, not a production sample. No fixed-build pass, representative p95/p99, client-satisfaction measurement, implemented rollout control or independently calibrated judge is claimed. A supplied 30-case CI demo is separate from the 20-answer audit.

## Submission
Submit https://github.com/StepanYuschishin/ai-evals and final-presentation.html to the Learning Platform's “Upload Your AI Evals Final Project” section. HTML works offline; public hosting is not required. Submission has not been performed. Brief requests submission within seven days of cohort ending for written feedback; cohort end date is not verified here.
