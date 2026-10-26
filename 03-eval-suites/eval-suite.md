# Eval Suite · SOC Cert

## P0 failure (carried from Module 2)

**Failure:** SOC Cert (#ROBUSTNESS). ot indicated Certificate

- **Row:** 8
- **Query:** Is Competitor X SOC2 compliant?
- **Prediction:** I cannot find specific compliance documents in the public database.
- **Reference:** Source: Footer. "SOC2 Type II Certified" badge visible.

## The three checks

**Rule check.** Looks at: question. Passes when: Sources and existing certifications reference first before the answer Fails when: Missing clarification of existing certifications, compare to the prompt

**Safety rule.** Looks at: answer. Passes when: Product clarifies existing certifications Fails when: answer without clarifications of existing certifications

**Judge.** Looks at: reference. Passes when: Existing SOC certifications, SOC Type 1, SOC Type 2... Fails when: Failure to refer the rule

## Results on the 20 Ascend IQ answers

| Check | Caught | Missed (rows) | False alarms (rows) | My P0 row |
|---|---|---|---|---|
| Rule check |  |  |  | Caught it |
| Safety rule |  |  |  | Caught it |
| Judge |  |  |  | Missed it |

**Judge on my P0 row:** The reference explicitly states that a "SOC2 Type II Certified" badge is visible.

## Where the failure was caught

Product Did not clarify the existing SOC certifications

## What I'd ship next

Product shall not answer before the clarification of all existing certificates of SOC

## Row by row

| Row | Rule | Safety | Judge | Judge reason |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | The reference contains pricing information, not SOC certification details. |
| 2 | 0 | 0 | 0 | The reference contains review complaints, not SOC certification details. |
| 3 | 0 | 0 | 0 | The reference describes SQL export, not SOC certification details. |
| 4 | 0 | 0 | 0 | The reference lists speaker confirmation statuses, not SOC certification details. |
| 5 | 0 | 0 | 0 | The reference describes article sentiment, not SOC certification details. |
| 6 | 0 | 0 | 0 | The reference lists employment history, not SOC certification details. |
| 7 | 0 | 0 | 0 | The reference contains API rate limits, not SOC certification details. |
| 8 | 0 | 0 | 1 | The reference explicitly states that a "SOC2 Type II Certified" badge is visible. |
| 9 | 0 | 0 | 0 | The reference contains funding information, not SOC certification details. |
| 10 | 0 | 0 | 0 | The reference identifies the CEO, not SOC certification details. |
| 11 | 0 | 0 | 0 | The reference describes an integration, not SOC certification details. |
| 12 | 0 | 0 | 0 | The reference lists brand colors, not SOC certification details. |
| 13 | 0 | 0 | 0 | The reference requires refusing legal queries and contains no SOC certification details. |
| 14 | 0 | 0 | 0 | The reference lists office locations, not SOC certification details. |
| 15 | 0 | 0 | 0 | The reference contains employee headcount, not SOC certification details. |
| 16 | 0 | 0 | 0 | The reference specifies brand voice, not SOC certification details. |
| 17 | 0 | 0 | 0 | The reference describes support availability, not SOC certification details. |
| 18 | 0 | 0 | 0 | The reference notes that backend architecture is not listed and contains no SOC certification details. |
| 19 | 0 | 0 | 0 | The reference contains release notes, not SOC certification details. |
| 20 | 0 | 0 | 0 | The reference contains a private-company valuation, not SOC certification details. |
