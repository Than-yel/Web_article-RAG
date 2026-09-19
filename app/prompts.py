"""Prompt templates for the RAG chain."""

RAG_PROMPT_TEMPLATE = """Use the provided context to answer the question.
If the answer is not in the context, say you do not know.

Context:
{context}

Question:
{question}

Answer:"""
