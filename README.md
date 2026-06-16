# EvalKit

EvalKit is a lightweight evaluation framework for RAG (Retrieval-Augmented Generation) systems based on **counterfactual retrieval analysis**.

It answers a simple but powerful question:

> Which retrieved chunks actually mattered for generating the final answer?

---

## 🧠 Why EvalKit?

Most RAG evaluation tools focus on:

- retrieval relevance
- answer similarity
- final response quality

But they miss a critical question:

> If I remove a retrieved chunk, does the answer still hold?

EvalKit solves this using **counterfactual evaluation**.

---

## 🔬 Core Idea

For each retrieved context chunk:

1. Remove the chunk
2. Ask an LLM judge if the answer is still possible
3. If YES → chunk is redundant
4. If NO → chunk is required

This produces:

- Retrieval Efficiency Score
- Required Contexts
- Redundant Contexts
- Importance Scores per chunk

---

## ⚡ Installation

```bash
pip install evalkit

```


## Why EvalKit

| Tool        | Focus                     | Missing insight |
|-------------|---------------------------|-----------------|
| Ragas       | retrieval + answer score  | context necessity |
| DeepEval    | LLM eval benchmarks       | counterfactuals |
| EvalKit     | context necessity (WHY)   | — |