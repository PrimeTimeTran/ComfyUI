class Assembler:
    def __init__(self):
        self.assembly_code = []

    def generate_code(self, ast):
        self.visit(ast)

    def visit(self, node):
        if node is not None:
            if node.type == 'ROOT':
                self.visit_function(node.root)
            elif node.type == 'FUNCTION':
                self.visit_function(node)
            elif node.type == 'RETURN_STATEMENT':
                self.visit_return_statement(node)
            elif node.type == 'RETURN_TYPE':
                print(node)
                print(node.type)
                print(node.value)
                # self.visit_return_statement(node)
            elif node.type == 'FUNCTION_NAME':
                self.visit_function_name(node)
            else:
                raise ValueError(f"Unknown node type: {node.type}")

    def visit_function(self, node):
        self.assembly_code.append(f"assembly_code Function {node.type}:")
        for child in node.children:
            self.visit(child)

    def visit_return_statement(self, node):
        print('visit_return_statement')
        print(f'node.value {node.value}')
        return_value = node.value
        self.assembly_code.append(f"   mov eax, {return_value}")
        self.assembly_code.append("   ret")

    def visit_function_name(self, node):
        pass  # Handle function name if needed

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            for line in self.assembly_code:
                f.write(line + '\n')
        print(f"Assembly code written to {filename}")