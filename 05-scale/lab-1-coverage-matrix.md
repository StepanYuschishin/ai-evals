# Module 5 · Coverage Matrix · AI Report Summaries

## Coverage Row

| Product | Hallucination Rate | Fairness | Latency | UX Trust | Robustness |
|---|---|---|---|---|---|
| AI Report Summaries | ✅ Covered | ❌ Gap | ⚠️ Partial | ❌ Gap | ❌ Gap |

## What Runs Today

- An LLM judge compares each summary with its source report before every release.
- Response time is logged, but nobody has set a target.

## Accepted Gap

**UX Trust.** We temporarily defer automated tone evaluation while prioritizing failures that could omit or distort decision-critical information. This accepts an unmeasured client-facing tone risk; the existing source-comparison judge does not cover it.

We’ll look again: Review this decision in 2 weeks, or immediately after any client complaint about misleading, overconfident, or inappropriate tone.

## Critical Gap

Robustness is the most critical uncovered risk because malformed, unusually long, or instruction-injected reports could cause failed summaries or missing decision-critical content. Clients may notice first, leading to poor decisions and loss of trust. QA will add a regression set covering long reports, tables, missing sections, conflicting statements, and embedded instructions, run before every release. A source-grounded judge will check task completion and critical omissions, with human review of flagged cases. QA will also audit 20 live summaries weekly and add confirmed failures to the regression set.

## After the Pressure Test

The feedback showed that accepting UX Trust as low risk was not justified for client-facing summaries. I added a proposed temporary human tone spot-check and kept the 2-week review. UX Trust remains a Gap until those checks actually begin.

I strengthened the robustness plan with explicit pass/fail criteria, QA-maintained reference cases approved by the PM, and sampling across report formats, lengths, languages, and client segments. Checks will run before every release, with 20 live summaries audited weekly, including some judge-passed cases. Critical failures will pause automated delivery for affected cases and route them to human review.
