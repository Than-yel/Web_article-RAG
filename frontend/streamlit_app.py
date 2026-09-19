"""Streamlit frontend for the web article RAG API."""

import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Web Article RAG")
st.title("Web Article RAG")

question = st.text_input("Ask a question about the indexed article")

if st.button("Ask", type="primary") and question:
    response = requests.post(
        f"{API_URL}/query",
        json={"question": question},
        timeout=60,
    )
    response.raise_for_status()
    st.json(response.json())
