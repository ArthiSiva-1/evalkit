from abc import ABC, abstractmethod


class BaseMetric(ABC):

    @abstractmethod
    def measure(
        self,
        query,
        contexts,
        answer
    ):
        pass