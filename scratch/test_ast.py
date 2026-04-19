import ast

code = """
name = input("Enter name: ")
print(name)
age = int(input("Age: "))
print(age)
"""

class InputToAwait(ast.NodeTransformer):
    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == 'input':
            node.func.id = '_custom_async_input'
            return ast.Await(value=node)
        return node

tree = ast.parse(code)
tree = InputToAwait().visit(tree)
ast.fix_missing_locations(tree)
print(ast.unparse(tree))
