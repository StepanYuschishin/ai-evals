# Джерела управлінської фінальної презентації

Чинне трактування рішення — evidence/managerial-decision.md. Попередні лабораторні policy не є доказом, що всі можливості продукту unsafe.

## evidence/business-brief.md

# Business brief · user-supplied screenshots
Ascend Analytics is a premium B2B market-intelligence platform for VP-level strategists and product leaders at Fortune 500 companies paying upwards of $50,000 annually. The platform is dense, engagement is declining and Q4 retention is at risk because specific insights take too long to find. Ascend IQ answers plain-language research questions. The CPO proposes access for the top 50 enterprise accounts next month; Sales is promoting it.

Final project: audit the supplied MVP logs and defend SHIP or HOLD using artifacts from all six modules. Submit repo URL and HTML presentation within seven days of cohort ending for written feedback. Cohort end date is not verified here.

Source: Final Project Brief screenshots supplied by the user in this chat. This is a course scenario, not verified real company financial information. More than $2.5m annual account value follows from 50 × upwards of $50k; expected loss, benefit, adoption and churn are not measured.


---

## 01-evaluation-strategy/strategy-canvas.md

# AI Evaluation Strategy Canvas

> Repo file `ai-evals/01-evaluation-strategy/strategy-canvas.md` (the repo is your submission).

## 1. Product Strategy, The Context

**Who it's for:** VP-level strategists and product leaders at Fortune 500 companies who pay upward of $50,000 a year for verified market intelligence.

**What they use it for:** Asking plain-language questions, like “Compare the pricing models of Stripe and Adyen,” and getting answers in seconds instead of digging through the platform.

**What's at stake:** Engagement is dropping, Q4 retention is at risk, and the CPO wants Ascend IQ live for the top 50 enterprise accounts next month. One poor answer to the wrong client can do lasting damage to the relationship.

## 2. Measurements, The Execution

**User promise.** For VP-level strategists and product leaders at Fortune 500 companies, Ascend IQ promises market intelligence in seconds, supported by verifiable sources and clear uncertainty, so that they can make informed strategic decisions with confidence.

**Top 3 trust metrics:**
- **Latency**, Response speed (P95 / P99). Slow kills engagement.
- **Hallucination Rate**, % of outputs that are confidently false or fabricated.
- **UX Trust**, Whether the experience feels consistent and trustworthy. It breaks when the tone undermines the user's confidence.

**Why these three:** Latency: Measures whether complete answers arrive quickly enough to fit busy executives’ workflows and support the promise of intelligence in seconds.

Hallucination Rate: Measures false or fabricated claims that could mislead strategic decisions and damage valuable enterprise relationships.

UX Trust: Measures whether users find answers clear, predictable, and consistent, helping confirm that sources and uncertainty support informed confidence.

## 3. Strategic Trade-Offs, The Cost

### Trade-off 1 · Hallucination Rate ↔ Latency
We prioritize a lower hallucination rate over lower latency because an incorrect market claim can damage a client’s strategic decisions and our relationship. We accept additional verification time and clearly acknowledge when evidence is insufficient.

### Trade-off 2 · Latency ↔ UX Trust
We prioritize UX trust over lower latency because executives need to understand the evidence and limitations behind an answer. We accept additional response time to provide clear sources and uncertainty rather than encourage unsupported confidence.

---
_Generated from the AI Evaluation Strategy Canvas, M1 lab tool, AI Evals Certification._


---

## 02-failure-discovery/audit-log.md

# Ascend IQ Failure Audit

11 confirmed failures: #HALLUCINATION ×8, #UX_TRUST ×1, #ROBUSTNESS ×2, #FAIRNESS ×0. I changed 0 of the judge’s calls.

| Query | Judge score | Human override | Trust Metric tag | Failure reason |
|---|---|---|---|---|
| What is InsightFlow's pricing for Enterprise? | 0 |  | #HALLUCINATION | The answer gives the outdated $49 price, but the reference says "New Price (Updated yesterday): $59/mo." |
| Summarize the top 3 complaints from DataViz's G2 reviews. | 1 |  |  |  |
| Does InsightFlow support native SQL export? | 0 |  | #HALLUCINATION | The answer says "Yes" and implies a connector exists, but the reference says SQL export is only "possible via REST API, but there is no 'Native Export' button in the UI," so "native" support is missing and the omission changes the meaning. |
| List the confirmed speakers for SaaStr. | 0 |  | #HALLUCINATION | The answer lists Sam Altman as confirmed, but the reference says "Sam Altman is listed as 'Invited/Tentative.'" |
| What is the sentiment of the latest TechCrunch article on us? | 0 |  | #HALLUCINATION | The answer adds details (praise for the UI, pricing above market average) that the reference does not support, as it only gives "Sentiment: Neutral/Positive." |
| Give me a bio for Sarah Jenkins, the new VP at DataViz. | 0 |  | #HALLUCINATION | The answer says "Director" at Salesforce, but the reference says "Prev: Sr. Director @ Salesforce," so the seniority is understated. |
| Compare our API rate limits to Competitor Z. | 0 |  | #HALLUCINATION | The answer calls our API "robust" and Competitor Z "strict throttling," but the reference says "Us: 500 req/min. Competitor Z: 1000 req/min (Twice as fast)," so the framing is reversed. |
| Is Competitor X SOC2 compliant? | 0 |  | #ROBUSTNESS | The agent says it can't find compliance documents, but the reference shows a "SOC2 Type II Certified" badge visible in the footer. |
| When was InsightFlow's last funding round? | 1 |  |  |  |
| Who is the CEO of DataViz? | 1 |  |  |  |
| Does Competitor Y integrate with HubSpot? | 0 |  | #HALLUCINATION | The answer claims a "seamless integration," but the reference says "HubSpot integration available via Zapier partnership," so it is indirect and the omission changes the meaning. |
| What are the primary brand colors for InsightFlow? | 1 |  |  |  |
| Summarize the lawsuit mentioned in the WSJ about Competitor Z. | 0 |  | #ROBUSTNESS | The agent refuses to summarize the lawsuit, and the only reference given is the internal rule "Refuse legal queries," which contains no verified facts about it. |
| List the HQ locations for DataViz. | 0 |  | #HALLUCINATION | The answer lists Austin as an HQ, but the reference says "HQ: San Francisco. Engineering Hub: Austin." |
| How many employees does InsightFlow have? | 1 |  |  |  |
| Draft a cold email about our new feature. | 0 |  | #UX_TRUST | The email uses slang and hype ("killer," "total game changer"), but the reference says "Tone: Confident, professional, expert. Avoid slang." |
| Does Competitor X offer 24/7 support? | 1 |  |  |  |
| What database backend does DataViz use? | 1 |  |  |  |
| Summarize the latest release notes for InsightFlow. | 1 |  |  |  |
| What is the market cap of Competitor Z? | 1 |  |  |  |


## Final evidence reconciliation
The table above preserves the original judge scores (11 failed calls, 9 passes). Final-project review is assistant-assisted, not an independently approved human gold set.

| Audit row | Original | Reviewed interpretation | Effect |
|---|---|---|---|
| 1 pricing | Fail | Fail: $49 is old; source states $59; per-user unit and 10 seats unsupported | Unambiguous pricing launch blocker under M4 policy |
| 13 legal refusal | Fail / robustness | Pass: supplied safety policy explicitly requires refusal | Exclude from true failures and do not gate this correct answer |
| 9 funding | Pass | Review: “Series B” is not established by the reference | Do not use as a strong validated negative |
| 12 colors | Pass | Review: hex value is unsupported; primary/secondary wording needs adjudication | Do not use as a strong validated negative |

Correcting only row 13 gives 10/20 failed calls: hallucination 8, robustness 1, UX trust 1. This is a provisional reviewed tally, not independently validated accuracy. The selected 20 examples are not a random production sample; no production prevalence, client satisfaction or retention effect is established. The release conclusion rests on row 1 itself, not on a disputed aggregate rate. In this case the fixed requirement is one sourced price; $49 versus $59 is sufficient to fail it.


---

## 02-failure-discovery/failure-taxonomy.md

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


---

## 03-eval-suites/eval-suite.md

# Eval Suite · Outdated pricing

## P0 failure (carried from Module 2)

**Failure:** Outdated pricing (#HALLUCINATION). The agent presents an outdated Enterprise price as current.

- **Row:** 1
- **Query:** What is InsightFlow's pricing for Enterprise?
- **Prediction:** InsightFlow Enterprise starts at $49/user/month with a 10-seat minimum.
- **Reference:** Source: Pricing Page (Cached). Old Price: $49/mo. New Price (Updated yesterday): $59/mo.

## The three checks

**Rule check.** Looks at: question, answer, reference. Passes when: For the InsightFlow Enterprise pricing question, the answer contains the current price $59 and does not present $49 as current. Pass unrelated questions. Fails when: For the InsightFlow Enterprise pricing question, the answer omits $59 or presents $49 as the current price.

**Safety rule.** Looks at: question, answer, reference. Passes when: For pricing questions, every stated price, billing unit, and minimum-seat requirement is supported by the supplied reference. If information is missing, the answer explicitly states that it is not confirmed. Pass unrelated questions. Fails when: For pricing questions, the answer states an unsupported price, billing unit, or minimum-seat requirement as fact.

**Judge.** Looks at: question, answer, reference. Passes when: For pricing questions, the answer accurately communicates the current price and preserves all material qualifications in the reference. It distinguishes historical prices from current prices and acknowledges missing information. Pass unrelated questions. Fails when: For pricing questions, the answer contradicts the current price, presents historical pricing as current, invents pricing conditions, or omits a qualification that changes the purchasing decision.

## Results on the 20 Ascend IQ answers

| Check | Caught | Missed (rows) | False alarms (rows) | My P0 row |
|---|---|---|---|---|
| Rule check | 1 of 1 | None | None | Caught it |
| Safety rule | 1 of 1 | None | None | Caught it |
| Judge | 1 of 1 | None | None | Caught it |

**Judge on my P0 row:** Presents historical $49 as current instead of $59; states unsupported per-user billing and a 10-seat minimum.

## Where the failure was caught

All three checks flagged the outdated pricing answer in row 1 and passed the other 19 rows. The rule check detected the incorrect current price, showing that this specific regression can be caught with a cheap deterministic check. Comparison with the saved M2 audit confirms one matching outdated-pricing failure (row 1), detected by each check; each check passes all 9 originally audit-passed rows. This is an in-sample comparison, not independent validation.

## What I'd ship next

Implement a deterministic check that compares the quoted current price with an approved, versioned pricing reference. Refresh that reference when pricing changes. Use a source-grounded judge to assess unsupported pricing conditions and misleading qualifications that a numeric check cannot detect.

## Row by row

| Row | Rule | Safety | Judge | Judge reason |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | Presents historical $49 as current instead of $59; states unsupported per-user billing and a 10-seat minimum. |
| 2 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 3 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 4 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 5 | 1 | 1 | 1 | Sentiment question, not a pricing question; passes. |
| 6 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 7 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 8 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 9 | 1 | 1 | 1 | Funding question, not a pricing question; passes. |
| 10 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 11 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 12 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 13 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 14 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 15 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 16 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 17 | 1 | 1 | 1 | Support availability question, not a pricing question; passes. |
| 18 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 19 | 1 | 1 | 1 | Unrelated to pricing; passes. |
| 20 | 1 | 1 | 1 | Market-cap question, not a pricing question; passes. |

## Reconciled counts and limitations
- Matching outdated-pricing cases: 1 (row 1). Do not use all 8 hallucination-tagged answers as this denominator.
- Each recorded check: caught 1 of 1; missed 0; false alarms 0 among 9 originally audit-passed rows. If the legal refusal is corrected to pass, false alarms remain 0 among 10 reviewed passed rows. Rows 9 and 12 still need label review.
- Passing the other 19 answers means this pricing-specific suite does not flag them; it does not mean they are correct overall.
- The Safety rule uses semantic support judgments. It is not a deterministic safety implementation merely because it is labeled a rule in the exercise.
- The saved run was a chat-based application of the checks. It is not three independent implementations or an operating CI/production service.
- Additional executable numeric-fixture replay is provided in scripts/replay_pricing_fixture.py and evidence/pricing-replay.json. It replays the same inputs; it is not a new agent run or an independent generalization test.


---

## 03-eval-suites/eval-spec.md

# Eval Spec · #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions.

| Part | Spec |
|---|---|
| Target risk | #HALLUCINATION: The agent presents an outdated Enterprise price as current or states unsupported pricing conditions. |
| Evaluator | For the InsightFlow Enterprise pricing regression case, use a deterministic check: pass only when the answer includes the current $59 price and does not present $49 as current. Pass unrelated questions. Separately, use a source-grounded judge to check whether billing units, minimum-seat requirements and other material pricing qualifications are supported by the reference. |
| Threshold | The pricing rule must flag the known outdated-price answer in row 1. On the audited regression set, require zero missed matching outdated-pricing cases and zero false alarms on audit-passed rows. These are acceptance criteria; the recorded Lab 1 comparison gives 1 of 1 matching pricing cases caught, zero misses and zero false alarms among 9 originally audit-passed rows. Supporting evidence: In the latest 20-row evaluation, all three checks flagged row 1 and passed the other 19 rows. This demonstrates detection of the known outdated-price example, but does not establish general detection accuracy. Reconciliation with the saved M2 audit gives 1 of 1 matching cases caught, zero misses and zero false alarms among the 9 originally audit-passed rows; this is in-sample evidence only. |
| Business stakes | Presenting outdated prices or unsupported purchasing conditions can mislead enterprise budgeting and vendor-selection decisions, undermine trust in Ascend IQ and put account renewals at risk. |
| Owner | PM owns acceptance criteria and the release decision. QA maintains approved regression cases and reviews false alarms and misses. Engineering implements the checks. The designated pricing-data owner keeps the approved reference current and versioned. |

## Messages

**Engineering · acceptance criteria:** For the InsightFlow Enterprise pricing regression case, return 1 only if the answer includes $59 as the current price and does not present $49 as current; otherwise return 0, and return 1 for unrelated questions. Separately, have the source-grounded judge fail pricing answers that state unsupported billing units, minimum-seat requirements or other material pricing qualifications; acceptance requires flagging row 1, zero missed matching outdated-pricing cases and zero false alarms on audit-passed rows, with counts reconciled against the saved Lab 1 audit.

**Design · what the user sees:** When a pricing check blocks an answer, hide the rejected pricing claims and show: “We couldn’t verify the pricing details. Please check the official pricing source or request a human review.”

**Leadership · risk and return:** These checks reduce the risk of clients making budgeting and vendor-selection decisions using outdated prices or unsupported purchasing conditions. A cheap deterministic check catches the known price regression, while a source-grounded judge assesses qualifications that numeric matching cannot reliably evaluate; broader detection accuracy remains unproven.


---

## 04-eval-gates/gate-map.md

# Module 4 · Eval Gate Map · Ascend IQ Copilot

## Gate Map

| Row | Failure Mode | Severity | Placement | Rationale |
|---|---|---|---|---|
| 1 | Hallucination | Hard | Release | Treating materially incorrect current pricing as a P0 launch risk, we block release until corrected because it can mislead enterprise purchasing and budgeting decisions. |
| 14 | Correct policy refusal | No gate | Not applicable | The answer correctly follows the explicit refusal policy. Fix the relevance evaluator rather than blocking compliant behavior. |
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
- My call: No gate. The answer correctly follows the explicit refusal policy. Fix the relevance evaluator rather than blocking compliant behavior.

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

## Final policy scope
The API Soft override may release other capabilities only with automated API comparisons disabled and affected requests routed to humans. It cannot waive exposure to an unmitigated P0 risk. Pricing remains Hard: no release override for a failing pricing case. These are design decisions for this course case; no deployment or integration is claimed.

The latency Soft gate uses the supplied 2.0-second target for the reviews task. It is not a measured p95/p99 and must not be confused with M5's separate long-query 10-second scenario.


---

## 04-eval-gates/launch-strategy.md

> **Final management interpretation:** See [managerial decision](../evidence/managerial-decision.md). The pricing Hard rule applies to a candidate including pricing. It does not automatically require stopping every isolated capability. A restricted scope requires separate approved criteria and demonstrated controls; no pilot is approved by this document. Earlier unconditional whole-product HOLD wording is superseded.

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


---

## 04-eval-gates/lab-ci-gate-policy.md

# Lab, CI Eval Gate Policy (Ascend IQ PR #218)

> Repo file `ai-evals/04-eval-gates/lab-ci-gate-policy.md`. Output of the **CI Gate demo** (instructor-led): PR #218 swaps the Ascend IQ retrieval prompt; a 30-case regression golden set is replayed on every PR. You set floors + max-regression per dimension, decide blocking vs warn-only, then make the merge call.
>

| Dimension | main | PR | Δ | Floor | Max reg | Blocking | Result |
|---|---:|---:|---:|---:|---:|---|---|
| Faithfulness (grounding) | 96 | 87 | −9 | 90 | 3 | yes | FAIL |
| Task completion | 92 | 93 | +1 | 85 | 5 | yes | PASS |
| Tool selection | 90 | 88 | −2 | 80 | 5 | yes | PASS |
| Safety / policy | 99 | 99 | 0 | 98 | 1 | yes | PASS |
| Latency (p95) | 84 | 80 | −4 | 70 | 8 | no | PASS |
| Cost per task | 88 | 82 | −6 | 70 | 10 | no | PASS |

**Gate result:** BLOCKED

## Merge decision

BLOCK merge: faithfulness is 87, below floor 90, and regressed 9 points against an allowed 3. Other dimensions cannot offset this blocking failure.

## Final-project interpretation
This is the supplied PR #218 replay scenario, not a fresh run against the learner's model. Block merge: grounding falls from 96 to 87, below the 90 floor and beyond the allowed 3-point regression. Other dimensions pass the supplied score rules. Latency and cost here are normalized scores, not milliseconds or dollars. No actual CI integration is demonstrated.


---

## 05-scale/lab-1-coverage-matrix.md

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


---

## 05-scale/lab-2-budget-crisis.md

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


---

## 06-culture/lab-1-ship-hold-memo.md

# Ship-or-Hold Memo · Ascend IQ

**HOLD the unrestricted 50-account rollout; qualify a restricted pilot as the next option, subject to separate entry criteria and approval.**

To: CPO, Engineering Lead, QA · From: Stepan Yuschishin · Course final-project recommendation

## The Answer
The supplied examples expose pricing, comparison and speed defects. They do not establish that every capability is unsafe or reveal production recurrence. Broad rollout is not supported by the current evidence, but a total product shutdown is not established either. Investigate causes, fix or exclude affected capabilities, validate the remaining scope and return for a pilot decision.

## Three Arguments
1. **Decision quality is at risk.** The pricing answer states $49 versus a $59 reference and includes unsupported conditions. The API answer supplies unsupported framing instead of the source-supported comparison. These are specific observed defects, not estimated production rates.
2. **The speed promise needs evidence.** One review-summary example takes 4.2 seconds versus a 2.0-second target. This is a task-level failure, not p95/p99 or measured retention impact. The M1 promise includes speed as well as grounding and UX trust.
3. **Protection is designed, not yet demonstrated at rollout scope.** M3 recorded checks detect the one known pricing failure; this does not show a corrected agent or general detection accuracy. The $155,000 online plan is affordable under the $200,000 online cap; implementation and staffing remain to be demonstrated before relying on it.

## Evidence versus chosen criteria
| Evidence | Result | Criterion | Meaning |
|---|---|---|---|
| Pricing, M2/M3 row1 | $49 vs current $59; 1 bad applicable answer | M4 candidate including pricing: 0 material pricing failures | Fails that candidate's chosen Hard gate; root cause/recurrence unknown |
| API, M2 row7 / M4 row8 | Unsupported framing; source 500 vs 1,000 req/min | Supported relevant comparison; M4 Soft policy | Fix or exclude automated comparisons with validated routing |
| Speed, M4 row3 | 4.2 seconds | 2.0-second task target | Soft failure for that task; more timing evidence needed |
| Pricing detector, M3 | Each of three recorded checks flags 1 of 1 known cases; 0 misses | Detect known example | In-sample detection success, not a corrected-output pass |
| Budget, M5 | $155,000 online; 2 online evals; total $168,250 | <=$200,000 online; max3 | Feasible planned allocation, not operational readiness |

## Policy interpretation
The earlier pricing Hard rule is a PM policy for a release that includes automated pricing, not evidence that every feature must stop. A restricted candidate excluding affected features is a different scope. It requires demonstrated exclusions, QA evidence for remaining tasks and explicitly approved scope-specific gates. It cannot simply waive the failed Hard criterion. Pilot readiness is not established today.

## Business trade-off
Holding broad access delays the hoped-for engagement/retention benefit. Launching untested decision-support answers exposes clients to incorrect purchasing information. The brief's 50 accounts paying upwards of $50,000 imply more than $2.5m annual account value; that is neither expected loss nor revenue attributable to Ascend IQ. No causal churn estimate is available.

## Ask and next evidence
At today's review, approve HOLD on the unrestricted scope, assign owners and agree a dated follow-up before the meeting ends. Engineering/pricing-data owner diagnose stale source versus retrieval versus generation and fix or exclude affected functionality. QA retests corrected and representative in-scope tasks. PM/Engineering define pilot scope, stop rules and demonstrate routing/rollback. CPO approves a pilot only after its entry criteria pass. No pilot account count or committed delivery date is invented.

## Reflection
An observed failure justifies investigation and a containment decision; its scope must not be assumed. A successful detector does not fix a product answer. A written gate does not prove its own severity or implementation. The management decision is about exposure, evidence and scope—not counting negative slides.

Sources: M1 strategy-canvas.md; M2 audit-log.md and failure-taxonomy.md; M3 eval-suite.md/eval-spec.md; M4 gate-map.md/launch-strategy.md; M5 lab-2-budget-crisis.md. Full reasoning: evidence/managerial-decision.md.


---

## evidence/managerial-decision.md

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


---

## evidence/pricing-replay.json

{
  "scope": "Frozen numeric-price fixture only; no semantic-judge or agent execution",
  "applicable": 1,
  "failed": 1,
  "results": [
    {
      "row": 1,
      "status": "FAIL",
      "quoted": "49",
      "reference_current": "59"
    },
    {
      "row": 2,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 3,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 4,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 5,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 6,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 7,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 8,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 9,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 10,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 11,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 12,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 13,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 14,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 15,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 16,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 17,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 18,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 19,
      "status": "NOT_APPLICABLE"
    },
    {
      "row": 20,
      "status": "NOT_APPLICABLE"
    }
  ]
}


## Початкові 20 кейсів
```csv
row,question,answer,reference
1,"What is InsightFlow's pricing for Enterprise?","InsightFlow Enterprise starts at $49/user/month with a 10-seat minimum.","Source: Pricing Page (Cached). Old Price: $49/mo. New Price (Updated yesterday): $59/mo."
2,"Summarize the top 3 complaints from DataViz's G2 reviews.","Users report issues with mobile load times, lack of dark mode, and steep learning curve.","Source: G2 Reviews. Keywords: ""Mobile app slow,"" ""Dark mode missing,"" ""Hard to learn."""
3,"Does InsightFlow support native SQL export?","Yes, you can export data to SQL databases via our API connector.","Source: Docs. ""SQL Export"" is possible via REST API, but there is no ""Native Export"" button in the UI."
4,"List the confirmed speakers for SaaStr.","Confirmed speakers include Jason Lemkin, Aaron Levie, and Sam Altman.","Source: Agenda. Lemkin and Levie confirmed. Sam Altman is listed as ""Invited/Tentative."""
5,"What is the sentiment of the latest TechCrunch article on us?","The article is positive, praising the UI but noting that pricing is higher than market average.","Source: TechCrunch. Sentiment: Neutral/Positive."
6,"Give me a bio for Sarah Jenkins, the new VP at DataViz.","Sarah Jenkins is the new VP of Product, formerly a Director at Salesforce.","Source: LinkedIn. Sarah Jenkins: VP Product @ DataViz. Prev: Sr. Director @ Salesforce."
7,"Compare our API rate limits to Competitor Z.","Our API is robust and developer-friendly. Competitor Z is known for strict throttling.","Source: Tech Specs. Us: 500 req/min. Competitor Z: 1000 req/min (Twice as fast)."
8,"Is Competitor X SOC2 compliant?","I cannot find specific compliance documents in the public database.","Source: Footer. ""SOC2 Type II Certified"" badge visible."
9,"When was InsightFlow's last funding round?","March 2023, Series B, $45M.","Source: Crunchbase. March 15, 2023. Amount: $45M."
10,"Who is the CEO of DataViz?","Mark Johnson.","Source: Company About Page. CEO: Mark Johnson."
11,"Does Competitor Y integrate with HubSpot?","Yes, they offer a seamless integration with HubSpot.","Source: Help Center. ""HubSpot integration available via Zapier partnership."""
12,"What are the primary brand colors for InsightFlow?","Electric Blue (#007AFF) and Charcoal.","Source: Brand Guidelines. Primary: Electric Blue. Secondary: Charcoal."
13,"Summarize the lawsuit mentioned in the WSJ about Competitor Z.","I cannot provide summaries of ongoing legal litigation.","Source: Safety Guidelines. ""Refuse legal queries."""
14,"List the HQ locations for DataViz.","San Francisco, CA and Austin, TX.","Source: Contact Us Page. HQ: San Francisco. Engineering Hub: Austin."
15,"How many employees does InsightFlow have?","Approximately 275 employees.","Source: LinkedIn Insights. Total Headcount: 275."
16,"Draft a cold email about our new feature.","Hey! Check out this killer new feature. It's a total game changer for your stack!","Source: Brand Voice. ""Tone: Confident, professional, expert. Avoid slang."""
17,"Does Competitor X offer 24/7 support?","Yes, but only for Enterprise tiers.","Source: Pricing Page. 24/7 Support: Enterprise Plan only."
18,"What database backend does DataViz use?","I do not have access to their internal architecture.","Source: Public Documentation. No backend architecture listed."
19,"Summarize the latest release notes for InsightFlow.","v2.4 added Dark Mode and fixed the CSV export bug.","Source: Release Notes. v2.4: ""Added Dark Mode. Fixed CSV bug."""
20,"What is the market cap of Competitor Z?","They are private, valued at ~$1B.","Source: Pitchbook. Private, ~$1B valuation."
```
