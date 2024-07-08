import ast
import inspect
import pprint


def total():
    a = 4
    b = 2
    c = a+b
    return a + b


# Get the source code of the total function
source_code = inspect.getsource(total)
# print(source_code)
# Parse the source code into an AST
parsed_ast = ast.parse(source_code)

# Pretty print the AST
pprint.pprint(ast.dump(parsed_ast))
