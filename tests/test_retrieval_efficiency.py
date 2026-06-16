from evalkit import RetrievalEfficiency
from evalkit.judges.fake import FakeJudge


def test_returns_result():

    metric = RetrievalEfficiency(
        judge=FakeJudge()
    )

    result = metric.measure(
        query="test",
        contexts=["a", "b", "c"],
        answer="answer"
    )

    assert result is not None