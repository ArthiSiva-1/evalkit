from dataclasses import dataclass
from typing import Optional


@dataclass
class MetricResult:
    score: float
    required_contexts: list[int]
    redundant_contexts: list[int]
    explanation: str
    importance_scores: Optional[dict[int, float]] = None

    def __str__(self):
        return (
            f"\n📊 Retrieval Efficiency: {self.score:.2f}\n"
            f"✔ Required Contexts: {self.required_contexts}\n"
            f"✖ Redundant Contexts: {self.redundant_contexts}\n"
            f"⭐ Importance Scores: {self.importance_scores}\n"
            f"💡 Explanation: {self.explanation}\n"
        )