import pytest

from app.retrieval import get_retriever


def test_retriever_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        get_retriever()
