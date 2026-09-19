"""FastAPI entry point for the RAG app."""

from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_chain import answer_question

app = FastAPI(title="Web Article RAG")


class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/query")
def query(request: QueryRequest) -> dict:
    return answer_question(request.question)
