# 🧪 EvalKit

> A simple evaluation tool to measure how much of your retrieved context is actually needed to answer a question.

---

## 🚀 Why EvalKit?

RAG systems often retrieve too much irrelevant context.

EvalKit helps you answer:

> **Which retrieved chunks were actually useful for generating the answer?**

---

## 📊 What it does

Given:

- a user query  
- retrieved contexts  
- a final answer  

EvalKit computes:

### ✔ Retrieval Efficiency
How much of the retrieved context was actually necessary.

### ✔ Required vs Redundant Contexts
Which chunks helped vs which were unnecessary.

---

## ⚡ Quickstart

### 1. Install

```bash
pip install evalkit-rag 
```

## Why EvalKit

| Tool        | Focus                     | Missing insight |
|-------------|---------------------------|-----------------|
| Ragas       | retrieval + answer score  | context necessity |
| DeepEval    | LLM eval benchmarks       | counterfactuals |
| EvalKit     | context necessity (WHY)   | — |

## 🦙 2. (Optional) Run Ollama

```bash
ollama serve
ollama pull llama3
```

## ⚡ 3. Use EvalKit

```python
from evalkit import RetrievalEfficiency, LLMJudge

judge = LLMJudge(model="ollama/llama3")

metric = RetrievalEfficiency(judge)

query = "What is refund policy?"

contexts = [
    "Refunds are allowed within 30 days",
    "Customer must provide receipt",
    "Office hours are 9-5"
]

answer = "Refunds are allowed within 30 days with receipt"

result = metric.measure(query, contexts, answer)

print(result)
```

## 📊 Output
Retrieval Efficiency: 0.67

Required Contexts: [0, 2]
Redundant Contexts: [1]


## 🧠 What this tells you
Which chunks were necessary
Which chunks were not needed
How efficient your retrieval system is