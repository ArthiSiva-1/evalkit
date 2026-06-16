from .base import BaseMetric
from .retrieval_efficiency import RetrievalEfficiency


class ContextWaste(BaseMetric):

    def __init__(self, judge):
        self.judge = judge

    def measure(self, query, contexts, answer):

        result = RetrievalEfficiency(
            judge=self.judge
        ).measure(query, contexts, answer)

        return len(result.redundant_contexts) / len(contexts)