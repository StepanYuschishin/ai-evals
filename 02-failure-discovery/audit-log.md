# Ascend IQ Failure Audit

Paste the markdown from the Module 2 Lab Guide (Activity 1) over this file, or upload the downloaded `audit-log.md` in its place, then commit.

_Summary line goes here._

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

