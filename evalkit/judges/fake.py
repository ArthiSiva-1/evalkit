from .base import BaseJudge


class FakeJudge(BaseJudge):

    def is_answer_possible(
        self,
        query,
        contexts,
        answer
    ):
        combined = " ".join(contexts)

        return (
        "Refunds within 30 days" in combined
        and
        "Proof of purchase required" in combined
        )