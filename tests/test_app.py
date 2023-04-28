import pytest
from src.app import run_wiki, execute_python_code


def test_wiki_search_for_python():
    """
    This function tests if run_wiki('Python') returns a string with length greater than 0.
    """
    result = run_wiki("Python")
    assert isinstance(result, str)
    assert len(result) > 0


def test_wiki_search_for_ai():
    """
    This function tests if run_wiki('Artificial intelligence') returns a string with length greater than 0.
    """
    result = run_wiki("Artificial intelligence")
    assert isinstance(result, str)
    assert len(result) > 0


def test_wiki_search_for_empty_string():
    """
    This function tests if run_wiki('') returns an empty string.
    """
    result = run_wiki("")
    assert isinstance(result, str)
    assert len(result) == 0

def test_execute_python_code_with_valid_code():
    code = "print('Hello, World!')"
    expected_output = "Hello, World!\n"
    assert execute_python_code(code) == expected_output


def test_execute_python_code_with_empty_string():
    code = ""
    assert execute_python_code(code) == ""


def test_execute_python_code_with_invalid_syntax():
    code = "print('Hello, World!'"
    with pytest.raises(SyntaxError):
        execute_python_code(code)


def test_execute_python_code_with_name_error():
    code = "print(variable_that_does_not_exist)"
    with pytest.raises(NameError):
        execute_python_code(code)
