from dataclasses import dataclass

@dataclass
class MetricResult:
    score: float
    required_contexts: list[int]
    redundant_contexts: list[int]
    explanation: str