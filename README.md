# Web Article RAG

Deployable RAG application scaffold based on the supplied notebook.

## Structure

- `notebooks/Web_Article RAG.ipynb` contains the source notebook.
- `AGENTS.md` contains the project implementation guidance copied from the supplied `CODEX.md`.
- `app/` contains the FastAPI backend and RAG modules.
- `frontend/` contains the Streamlit client.
- `data/chroma/` is reserved for persisted Chroma data and is ignored by Git.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Set `COHERE_API_KEY` and `SOURCE_URL` in `.env`.

## Run

```bash
uvicorn app.main:app --reload
streamlit run frontend/streamlit_app.py
```

The notebook logic still needs to be ported from cells 1-21 into the production modules.
