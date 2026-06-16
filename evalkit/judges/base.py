from abc import ABC, abstractmethod


class BaseJudge(ABC):

    @abstractmethod
    def is_answer_possible(
        self,
        query,
        contexts,
        answer
    ):
        pass