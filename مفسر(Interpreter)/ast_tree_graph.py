from graphviz import Digraph
import ast

def visualize_ast(node, graph=None):
    if graph is None:
        graph = Digraph(comment='AST')
        graph.attr(size='10,10')
        graph.attr('node', shape='ellipse')

    node_name = str(id(node))
    graph.node(node_name, label=type(node).__name__)
    
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    child_name = str(id(item))
                    graph.node(child_name, label=type(item).__name__)
                    graph.edge(node_name, child_name, label=field)
                    visualize_ast(item, graph)
                else:
                    graph.node(f'{node_name}_{field}_{item}', label=str(item), shape='box')
                    graph.edge(node_name, f'{node_name}_{field}_{item}', label=field)
        elif isinstance(value, ast.AST):
            child_name = str(id(value))
            graph.node(child_name, label=type(value).__name__)
            graph.edge(node_name, child_name, label=field)
            visualize_ast(value, graph)

    return graph

# Parse the code and create the AST
source_code = """
def total():
    a = 4
    b = 2
    c = a + b
    print(c)
"""
ast_node = ast.parse(source_code)

# Visualize the AST
dot = visualize_ast(ast_node)
dot.render('ast_tree', format='png', cleanup=False)
