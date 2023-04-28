import ast
import builtins

from dotenv import load_dotenv, find_dotenv
from langchain.utilities import WikipediaAPIWrapper
from langchain.utilities import PythonREPL


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

    # create an instance of WikipediaAPIWrapper and call its run method with the search term
    wikipedia = WikipediaAPIWrapper()
    result = wikipedia.run(search_term)

    return result


def execute_python_code(code: str) -> str:
    """
    Executes the given Python code using an instance of PythonREPL.

    Args:
        code: (str) The string containing the Python code to execute.

    Returns:
        str: The returned output from executing the code.
    """
    if not code:
        return ""

    try:
        # compile the code to bytecode
        compiled_code = compile(code, "<string>", "exec")
    except SyntaxError as e:
        # raise a SyntaxError if the code is not valid Python code
        raise e

    # create a visitor object to traverse the abstract syntax tree of the compiled code
    class VariableNameVisitor(ast.NodeVisitor):
        def __init__(self):
            self.names = set()

        def visit_Name(self, node):
            self.names.add(node.id)

        def visit_FunctionDef(self, node):
            self.names.add(node.name)

    # parse the code into an abstract syntax tree and traverse it with the visitor object
    tree = ast.parse(code)
    visitor = VariableNameVisitor()
    visitor.visit(tree)
    variable_names = visitor.names

    # Check for undefined variables
    local_namespace = locals()
    undefined_variables = [
        name
        for name in variable_names
        if name not in local_namespace and name not in dir(builtins)
    ]
    if undefined_variables:
        # Raise a new NameError with a custom message
        raise NameError(f"Undefined variables: {', '.join(undefined_variables)}")

    # create an instance of PythonREPL and call its run method with the compiled code
    python_repl = create_python_repl()
    return python_repl.run(code)


def create_python_repl() -> PythonREPL:
    """
    Creates and returns an instance of PythonREPL.
    """
    # create an instance of PythonREPL and return it
    return PythonREPL()

if __name__ == "__main__":
    try:
        print(execute_python_code("print(13+2)"))
        print(run_wiki("Birria"))
    except Exception as e:
        print(e)
