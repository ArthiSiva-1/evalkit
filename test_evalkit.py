from evalkit import RetrievalEfficiency
from evalkit.judges import LLMJudge

judge = LLMJudge(model="ollama/llama3")

metric = RetrievalEfficiency(judge=judge)

query = "What is refund policy?"

contexts = [
    "Refunds are allowed within 30 days",
    "Customer must provide receipt",
    "Office hours are 9-5"
]

answer = "Refunds are allowed within 30 days with receipt"

result = metric.measure(query, contexts, answer)

print(result)