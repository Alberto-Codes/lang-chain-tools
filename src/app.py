from dotenv import load_dotenv, find_dotenv
from langchain.utilities import WikipediaAPIWrapper

load_dotenv(find_dotenv())


def run_wiki(search_term: str) -> str:
    """
    Search the Wikipedia page for the given search term and return the content as a string.

    Args:
        search_term: A string representing the term to search in Wikipedia.

    Returns:
        A string representing the content of the Wikipedia page for the given search term.
    """
    if not search_term:
        return ""

    wikipedia = WikipediaAPIWrapper()
    result = wikipedia.run(search_term)
    return result


if __name__ == "__main__":
    print(run_wiki("Mexico"))
