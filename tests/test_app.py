from src.app import run_wiki


def test_search_for_python():
    """
    This function tests if run_wiki('Python') returns a string with length greater than 0.
    """
    result = run_wiki("Python")
    assert isinstance(result, str)
    assert len(result) > 0


def test_search_for_ai():
    """
    This function tests if run_wiki('Artificial intelligence') returns a string with length greater than 0.
    """
    result = run_wiki("Artificial intelligence")
    assert isinstance(result, str)
    assert len(result) > 0


def test_search_for_empty_string():
    """
    This function tests if run_wiki('') returns an empty string.
    """
    result = run_wiki("")
    assert isinstance(result, str)
    assert len(result) == 0
