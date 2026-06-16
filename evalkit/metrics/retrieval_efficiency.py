from .base import BaseMetric
from ..models import MetricResult

class RetrievalEfficiency(BaseMetric):

    def __init__(self, judge):
        self.judge = judge

    def measure(
        self,
        query,
        contexts,
        answer
    ):

        required = []
        redundant = []

        for i in range(len(contexts)):

            remaining = (
                contexts[:i]
                + contexts[i + 1:]
            )

            possible = self.judge.is_answer_possible(
                query=query,
                contexts=remaining,
                answer=answer
            )

            if possible:
                redundant.append(i)
            else:
                required.append(i)

        score = len(required) / len(contexts)

        return MetricResult(
            score=score,
            required_contexts=required,
            redundant_contexts=redundant,
            explanation=f"{score:.2f} retrieval efficiency"
        )