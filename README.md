# EvalKit

Evaluation toolkit for LLM and RAG systems.

## Installation

```bash
pip install -e .
```

## Example

```python
from evalkit import RetrievalEfficiency
from evalkit.judges.fake import FakeJudge

metric = RetrievalEfficiency(
    judge=FakeJudge()
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
```