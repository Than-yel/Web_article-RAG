from app.ingest import clean_text


def test_clean_text_normalizes_whitespace():
    assert clean_text(" Alpha\n\n beta\tgamma ") == "Alpha beta gamma"
