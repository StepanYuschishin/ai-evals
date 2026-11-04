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
