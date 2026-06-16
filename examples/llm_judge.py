from evalkit import RetrievalEfficiency
from evalkit.judges import LLMJudge

metric = RetrievalEfficiency(
    judge = LLMJudge(
    model="gemini/gemini-2.5-flash"
)
)

result = metric.measure(
    query="What is the refund policy?",
    contexts=[
        "Refunds within 30 days",
        "Proof of purchase required",
        "Office hours are 9-5"
    ],
    answer="Refunds within 30 days with proof of purchase"
)

print(result)