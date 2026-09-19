# AGENTS.md

## Project
Practical 2 RAG App

## Goal
Convert the existing working RAG notebook into a deployable application with:

- FastAPI backend
- Streamlit frontend
- Chroma vector store
- Cohere LLM
- Persistent ingestion pipeline
- Tests
- Docker support

The existing notebook is the source of truth for the RAG logic that already works.

---

## Source of Truth

Use:

`notebooks/Web_Article RAG.ipynb`

as the reference implementation.

Use the working code from notebook cells 1–21.

Ignore every notebook cell beginning with or belonging to the section:

`Debugging retrieval for a specific question`

Do not redesign the RAG system unless a change is necessary to move from notebook code to a deployable application.

Preserve the notebook's working behavior wherever possible.

---

## Target Project Structure

```text
practical2-rag-app/
│
├── AGENTS.md
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── prompts.py
│   ├── ingest.py
│   ├── retrieval.py
│   ├── rag_chain.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│   ├── test_ingest.py
│   ├── test_retrieval.py
│   └── test_main.py
│
├── notebooks/
│   └── Web_Article RAG.ipynb
│
├── data/
│   └── chroma/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

---

## File Responsibilities

### `app/config.py`
Contains configuration and environment-variable handling.

Examples:

- `COHERE_API_KEY`
- source URL
- embedding model name
- Cohere model name
- chunk size
- chunk overlap
- retrieval `k`
- Chroma persistence directory

Do not hardcode secrets.

---

### `app/prompts.py`
Contains the RAG prompt template used by the application.

Preserve the prompt behavior from the notebook unless a deployment-specific change is required.

---

### `app/ingest.py`
Contains the offline ingestion pipeline:

```text
load
→ clean
→ chunk
→ embed
→ persist
```

Responsibilities include:

- loading the source document/webpage
- cleaning text
- splitting documents
- creating embeddings
- writing embeddings/documents to persistent Chroma storage

Ingestion should be run separately.

Do not re-run ingestion whenever a user sends a query.

---

### `app/retrieval.py`
Loads the persisted Chroma vector store and creates the retriever.

The current notebook uses dense semantic vector retrieval.

Do not describe it as hybrid retrieval unless hybrid retrieval is explicitly implemented later.

Preserve the notebook's retrieval settings, including retrieval `k`, unless instructed otherwise.

---

### `app/rag_chain.py`
Builds the RAG pipeline by connecting:

```text
retriever
+
prompt
+
Cohere
```

Use the working RAG-chain behavior from the notebook.

Keep orchestration separate from the API layer.

---

### `app/main.py`
Contains the FastAPI application.

Expected endpoints:

- `GET /health`
- `POST /query`

The API should call the RAG chain and return structured responses.

The API should not rebuild the vector database on every request.

---

### `frontend/streamlit_app.py`
Contains the Streamlit user interface.

The Streamlit frontend should communicate with the FastAPI backend over HTTP.

Preferred architecture:

```text
User
→ Streamlit
→ FastAPI
→ RAG chain
→ Retriever
→ Chroma
→ Cohere
→ FastAPI response
→ Streamlit
```

Do not tightly couple the frontend to the internal RAG implementation unless explicitly instructed.

---

## Existing RAG Configuration

Preserve the notebook's working configuration.

Current important settings include:

- `RecursiveCharacterTextSplitter`
- `chunk_size = 1200`
- `chunk_overlap = 200`
- Chroma vector store
- cosine similarity
- retriever `k = 10`
- Cohere `command-a-03-2025`

Use the same embedding model used in the notebook.

If any configuration in the notebook differs from this file, inspect the notebook and report the discrepancy before changing behavior.

---

## Deployment Changes

The notebook may use temporary or in-memory components for experimentation.

For the deployable application:

- use persistent Chroma storage under `data/chroma/`
- move secrets to environment variables
- separate ingestion from query-time execution
- separate frontend, API, retrieval, and RAG orchestration
- preserve working notebook logic wherever possible

Do not change algorithmic behavior simply to make the code look more sophisticated.

---

## Tests

Create tests for the main responsibilities.

### `tests/test_ingest.py`
Test cleaning and ingestion-related logic.

### `tests/test_retrieval.py`
Test that relevant queries retrieve expected content.

Retrieval quality is a core part of this application and must be tested explicitly.

### `tests/test_main.py`
Test the FastAPI endpoints and basic application behavior.

Run relevant tests after each major implementation stage.

---

## GitHub and Security Rules

Never commit:

- `.env`
- real API keys
- `data/chroma/`
- virtual environments
- `__pycache__/`
- `.pytest_cache/`
- `.streamlit/secrets.toml`
- generated cache files
- local IDE metadata unless intentionally required

Commit `.env.example`, but it must contain placeholders only.

Example:

```text
COHERE_API_KEY=your_cohere_api_key_here
```

Never place a real API key in source code, notebooks, tests, README files, or commit history.

Inspect the notebook for secrets before any public push.

---

## Development Rules

1. Read this `AGENTS.md` before making project changes.
2. Treat the notebook as the source of truth for the working RAG logic.
3. Reuse working notebook code rather than unnecessarily rewriting it.
4. Refactor notebook code into the correct production files.
5. Keep functions small, readable, and focused.
6. Do not introduce unnecessary frameworks or abstractions.
7. Do not silently change models, chunking settings, retrieval settings, or prompt behavior.
8. Do not convert the current dense retriever into a different retrieval architecture unless explicitly instructed.
9. Do not hardcode secrets.
10. Do not run ingestion on every query.
11. Do not put the entire notebook implementation into one Python file.
12. Keep Streamlit separate from FastAPI and the internal RAG implementation.
13. Run tests after meaningful implementation changes.
14. Report discrepancies or required architectural changes before making large changes.
15. Prefer minimal, understandable changes over clever abstractions.

---

## Human-in-the-Loop Workflow

Work incrementally.

Do not implement the entire application in one large uncontrolled change unless explicitly instructed.

Preferred implementation order:

1. Inspect `AGENTS.md`.
2. Inspect notebook cells 1–21.
3. Map notebook responsibilities to production files.
4. Create the project structure.
5. Implement `app/config.py`.
6. Implement `app/ingest.py`.
7. Implement persistent Chroma storage.
8. Implement `app/retrieval.py`.
9. Implement `app/prompts.py`.
10. Implement `app/rag_chain.py`.
11. Implement FastAPI in `app/main.py`.
12. Add tests.
13. Implement the Streamlit frontend.
14. Add Docker support.
15. Finalize the README.

After each major stage:

- summarize what changed
- report test results
- report any issues or assumptions
- avoid making unrelated changes

Do not make major architectural changes without explicit instruction.

---

## First Inspection Task

When first given this repository:

1. Read this file.
2. Inspect `notebooks/Web_Article RAG.ipynb`.
3. Focus only on notebook cells 1–21.
4. Ignore the debugging section specified above.
5. Explain how each relevant notebook section maps to the production files.
6. Identify any code that must change specifically because the notebook is becoming a deployed application.
7. Do not modify files until explicitly instructed to begin implementation.
