# Summary
# Tokenization: Split source code into tokens.
# Parsing: Build an AST from tokens.
# Semantic Analysis: Validate the AST.
# IR Generation: Translate AST to an intermediate representation.
# Optimization: Improve the IR.
# Code Generation: Translate IR to machine code.
# Linking: Combine multiple modules into an executable.
class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.type = node_type
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

    def __repr__(self):
        return f'{self.type}: {self.value}'

class AST:
    def __init__(self):
        self.root = ASTNode(node_type='ROOT')
        self.type = 'ROOT'

    def _insert(self, node, parent=None):
        if self.root is None:
            self.root = node
        elif parent is None:
            raise ValueError("Parent node must be specified for non-root nodes.")
        else:
            parent.children.append(node)

    def insert(self, node, parent=None):
        self._insert(node, parent)

    def pre_order_traversal(self, node=None):
        if node is None:
            node = self.root
        yield node
        for child in node.children:
            yield from self.pre_order_traversal(child)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token_index = 0

    def parse(self):
        return self.parse_function()

    def check(self, expected_type):
        if self.current_token_index < len(self.tokens):
            current_token_type = self.tokens[self.current_token_index][0]
            return current_token_type == expected_type
        else:
            return False

    def parse_function(self):
        ast = AST()
        return_type = self.match('IDENT')
        if return_type != 'int':
            raise ValueError(f"Expected return type 'int' but got {return_type}")
        
        function_name = self.match('IDENT')
        ast.root.add_child(ASTNode('FUNCTION_NAME', function_name))
        ast.root.add_child(ASTNode('RETURN_TYPE', return_type))

        # Parse function parameters if any
        self.match('LPAREN')
        while not self.check('RPAREN'):
            parameter_type = self.match('IDENT')
            parameter_name = self.match('IDENT')
            ast.root.add_child(ASTNode('PARAMETER', (parameter_type, parameter_name)))
            if self.check('COMMA'):
                self.match('COMMA')
        self.match('RPAREN')
        self.match('LBRACE')
        while not self.check('RBRACE'):
            statement = self.parse_statement()
            ast.root.add_child(statement)

        self.match('RBRACE')

        return ast


    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            token_value = self.tokens[self.pos][1]
            self.pos += 1
            return token_value
        else:
            raise ValueError(f"Expected {expected_type} but got {self.tokens[self.pos][0]}")
