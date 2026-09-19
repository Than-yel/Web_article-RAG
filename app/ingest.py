"""Offline ingestion pipeline for the web article RAG app."""

import re


def clean_text(text: str) -> str:
    """Normalize whitespace in extracted article text."""
    return re.sub(r"\s+", " ", text).strip()


def run_ingestion() -> None:
    """Run the notebook-derived ingestion pipeline.

    The implementation should be filled from notebooks/Web_Article RAG.ipynb
    cells 1-21, preserving its chunking, embedding, and Chroma behavior.
    """
    raise NotImplementedError("Ingestion pipeline must be ported from the notebook.")


if __name__ == "__main__":
    run_ingestion()
