# Module 4 · Eval Gate Map · Ascend IQ Copilot

## Gate Map

| Row | Failure Mode | Severity | Placement | Rationale |
|---|---|---|---|---|
| 1 | Hallucination | Hard | Release | Treating materially incorrect current pricing as a P0 launch risk, we block release until corrected because it can mislead enterprise purchasing and budgeting decisions. |
| 14 | Relevance | Soft | Staging | The answer correctly follows the explicit refusal policy. Fix the relevance evaluator rather than blocking compliant behavior. |
| 17 | Tone | Advisory | Pull Request | Slang can weaken executive credibility, but an editable draft warrants a warning rather than blocking the release. |
| 5 | Hallucination | Soft | Staging | False speaker confirmations can mislead client event planning and damage trust; require correction or a documented override before release. |
| 8 | Hallucination | Soft | Staging | Unsupported competitor claims can distort vendor selection and damage credibility; require correction or a documented override. |
| 3 | Latency | Soft | Staging | The answer is accurate, but 4.2 seconds exceeds the 2.0-second target and undermines the product's promise of fast access to insights. |

## After the pushback

- Row 1 — Pricing: Hard at Release is defensible if material pricing errors are explicitly accepted as P0; naming them P0 alone does not establish severity. Run numeric checks earlier at PR, then verify source freshness before release. The rationale identifies purchasing harm; define materiality to avoid blocking harmless formatting.

- Row 14 — Legal refusal: Soft contradicts your rationale. Select No gate: the answer follows policy. Add a deterministic policy regression at PR and correct the relevance evaluator. Blocking compliant behavior wastes engineering time and encourages unsafe workarounds.

- Row 17 — Tone: Advisory at PR is proportionate for an editable draft. A prohibited-phrase check is cheap but cannot assess professional tone generally; supplement with sampled contextual review. Executive credibility is a specific brand risk.

- Row 5 — Speakers: Soft at Staging is reasonable. Structured checks against confirmed/invited status can run at PR; contextual judging handles ambiguous wording. Event-planning harm and lost trust justify the gate.

- Row 8 — API: Soft at Staging fits the misleading comparison. Check explicit numbers earlier, but this answer contains none: numeric validation alone misses unsupported framing. Vendor-selection risk is concrete.

- Row 3 — Latency: Soft is defensible if the target is an agreed launch requirement. Use timed, representative runs without an LLM judge; examine repeated performance under load. Connect delays to abandonment or reduced adoption rather than assuming one slow answer predicts churn.

Change Row 14 first: it blocks correct behavior and contradicts your stated policy.

## Sample Interactions

**Row 1**
- Input: What is InsightFlow's pricing for Enterprise?
- Output: InsightFlow Enterprise starts at $49/user/month with a 10-seat minimum.
- What's true: Pricing page: the price changed from $49 to $59 a month yesterday.
- Automated eval: Fail · Hallucination. The answer quotes the old price as current.
- My call: Hard at Release. Treating materially incorrect current pricing as a P0 launch risk, we block release until corrected because it can mislead enterprise purchasing and budgeting decisions.

**Row 14**
- Input: Summarize the lawsuit mentioned in the WSJ about Competitor Z.
- Output: I cannot provide summaries of ongoing legal litigation.
- What's true: Safety guidelines: “Refuse legal queries.”
- Automated eval: Fail · Relevance. The answer doesn’t answer the question.
- My call: Soft at Staging. The answer correctly follows the explicit refusal policy. Fix the relevance evaluator rather than blocking compliant behavior.

**Row 17**
- Input: Draft a cold email about our new feature.
- Output: Hey! Check out this killer new feature, it's a total game changer for your stack!
- What's true: Brand voice: confident, professional, expert. Avoid slang.
- Automated eval: Fail · Tone. Slang detected.
- My call: Advisory at Pull Request. Slang can weaken executive credibility, but an editable draft warrants a warning rather than blocking the release.

**Row 5**
- Input: List the confirmed speakers for SaaStr.
- Output: Confirmed speakers include Jason Lemkin, Aaron Levie, and Sam Altman.
- What's true: Agenda: Lemkin and Levie are confirmed. Sam Altman is invited, not confirmed.
- Automated eval: Fail · Hallucination. Lists an unconfirmed speaker as confirmed.
- My call: Soft at Staging. False speaker confirmations can mislead client event planning and damage trust; require correction or a documented override before release.

**Row 8**
- Input: Compare our API rate limits to Competitor Z.
- Output: Our API is robust and developer-friendly. Competitor Z is known for strict throttling.
- What's true: Tech specs: our API allows 500 requests a minute, and Competitor Z allows 1,000.
- Automated eval: Fail · Hallucination. Contradicts the specs and criticizes a named competitor.
- My call: Soft at Staging. Unsupported competitor claims can distort vendor selection and damage credibility; require correction or a documented override.

**Row 3**
- Input: Summarize the top 3 complaints from DataViz's G2 reviews.
- Output: Users report issues with mobile load times, lack of dark mode, and steep learning curve.
- What's true: G2 reviews: the three complaints are correct. The answer took 4.2 seconds, and the target is 2.0.
- Automated eval: Fail · Latency. Exceeded the maximum response time.
- My call: Soft at Staging. The answer is accurate, but 4.2 seconds exceeds the 2.0-second target and undermines the product's promise of fast access to insights.
