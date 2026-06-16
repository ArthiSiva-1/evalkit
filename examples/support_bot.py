from evalkit import RetrievalEfficiency
from evalkit.judges import LLMJudge

metric = RetrievalEfficiency(
    judge=LLMJudge(model="gemini/gemini-2.5-flash")
)

result = metric.measure(
    query="How do refunds work?",
    contexts=[
        "Refunds are available within 30 days",
        "Customer must provide receipt",
        "We ship globally",
        "Support is available 24/7"
    ],
    answer="Refunds are available within 30 days with receipt"
)

print(result)