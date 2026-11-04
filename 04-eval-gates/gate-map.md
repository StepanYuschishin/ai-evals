# Module 4 · Eval Gate Map · Ascend IQ Copilot

## Gate Map

| Row | Failure Mode | Severity | Placement | Rationale |
|---|---|---|---|---|
| 1 | Hallucination | Hard | Pull Request | P0, Critical iussue, pricing, code based eval |
| 14 | Relevance | Soft | Staging | P2, not critical, WSJ is an official source |
| 17 | Tone | Soft | Staging | P1 issue, depends on the industry, better to keep professional tone |
| 5 | Hallucination | Hard | Release | P1, Trust issue, declaring not confirmed participants |
| 8 | Hallucination | Soft | Release | P2, Vague response, misleading |
| 3 | Latency | Soft | Pull Request | P1, misleading reply |

## After the pushback

- Row 1: Hard is too strict without evidence that this is P0. Use Soft at Staging; a PR check can compare prices with a versioned fixture, but cannot establish live pricing freshness. Name the risk: incorrect purchasing decisions and loss of client trust.
- Row 14: Use No gate. The answer follows the explicit refusal policy; the relevance evaluator is wrong. Correct that evaluator and add a cheap policy regression test at PR. WSJ’s credibility does not override the supplied policy.
- Row 17: Soft is excessive for an editable draft. Use Advisory at Pull Request for known slang, with broader tone evaluation in Staging. The risk is reduced executive credibility and outreach effectiveness; explain why blocking would be justified if you retain Soft.
- Row 5: Hard at Release conflicts with your P1 classification: Release is reserved for critical P0 risks. Use Soft at Staging; structured speaker-status checks could run earlier at PR. Name the consequences: clients making plans based on false confirmations and reputational damage.
- Row 8: Soft at Release is invalid under the stated placement policy. Move it to Staging and retain Soft unless you establish P0 severity. Check numeric comparisons cheaply at PR; evaluate misleading wording in Staging. The risk is distorted vendor selection and damaged credibility.
- Row 3: The answer is accurate, so “misleading” is incorrect. Use Advisory at Staging, measuring latency through representative timed runs. One 4.2-second result does not establish P1 severity; investigate repeated delays and abandonment.
Change Row 14 first: it blocks correct safety behavior and creates pressure to violate the policy.

## Sample Interactions

**Row 1**
- Input: What is InsightFlow's pricing for Enterprise?
- Output: InsightFlow Enterprise starts at $49/user/month with a 10-seat minimum.
- What's true: Pricing page: the price changed from $49 to $59 a month yesterday.
- Automated eval: Fail · Hallucination. The answer quotes the old price as current.
- My call: Hard at Pull Request. P0, Critical iussue, pricing, code based eval

**Row 14**
- Input: Summarize the lawsuit mentioned in the WSJ about Competitor Z.
- Output: I cannot provide summaries of ongoing legal litigation.
- What's true: Safety guidelines: “Refuse legal queries.”
- Automated eval: Fail · Relevance. The answer doesn’t answer the question.
- My call: Soft at Staging. P2, not critical, WSJ is an official source

**Row 17**
- Input: Draft a cold email about our new feature.
- Output: Hey! Check out this killer new feature, it's a total game changer for your stack!
- What's true: Brand voice: confident, professional, expert. Avoid slang.
- Automated eval: Fail · Tone. Slang detected.
- My call: Soft at Staging. P1 issue, depends on the industry, better to keep professional tone

**Row 5**
- Input: List the confirmed speakers for SaaStr.
- Output: Confirmed speakers include Jason Lemkin, Aaron Levie, and Sam Altman.
- What's true: Agenda: Lemkin and Levie are confirmed. Sam Altman is invited, not confirmed.
- Automated eval: Fail · Hallucination. Lists an unconfirmed speaker as confirmed.
- My call: Hard at Release. P1, Trust issue, declaring not confirmed participants

**Row 8**
- Input: Compare our API rate limits to Competitor Z.
- Output: Our API is robust and developer-friendly. Competitor Z is known for strict throttling.
- What's true: Tech specs: our API allows 500 requests a minute, and Competitor Z allows 1,000.
- Automated eval: Fail · Hallucination. Contradicts the specs and criticizes a named competitor.
- My call: Soft at Release. P2, Vague response, misleading

**Row 3**
- Input: Summarize the top 3 complaints from DataViz's G2 reviews.
- Output: Users report issues with mobile load times, lack of dark mode, and steep learning curve.
- What's true: G2 reviews: the three complaints are correct. The answer took 4.2 seconds, and the target is 2.0.
- Automated eval: Fail · Latency. Exceeded the maximum response time.
- My call: Soft at Pull Request. P1, misleading reply

## Recommended consolidated map · pending PM approval
This table supersedes the initial map for the proposed final plan; the historical choices above remain visible.

| M4 row | Call | Placement | Business rationale |
|---|---|---|---|
| 1 pricing | Soft | Staging | Prevent misleading purchasing decisions; PR fixtures alone cannot establish source freshness |
| 14 policy refusal | No gate on this correct answer | PR policy regression | Avoid blocking required safety behavior |
| 17 slang draft | Advisory | Pull Request | Warn about executive credibility without blocking an editable draft |
| 5 unconfirmed speaker | Soft | Staging | Avoid false confirmations affecting client plans; structured status checks may run at PR |
| 8 API comparison | Soft | Staging | Prevent distorted vendor comparisons; use earlier numeric checks when applicable |
| 3 correct but slow answer | Advisory | Staging | Measure delay under representative load; one 4.2-second response is not sufficient to establish critical impact |

SOC is audit/M3 row 8, NOT M4 API row 8. The SOC Hard gate in launch-strategy.md is conditional: M2 currently classifies it P1, and a validated evaluator plus approved P0 justification are prerequisites for Release placement.
