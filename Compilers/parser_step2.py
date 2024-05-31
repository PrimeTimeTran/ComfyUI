# Summary
# Tokenization: Split source code into tokens.
# Parsing: Build an AST from tokens.
# Semantic Analysis: Validate the AST.
# IR Generation: Translate AST to an intermediate representation.
# Optimization: Improve the IR.
# Code Generation: Translate IR to machine code.
# Linking: Combine multiple modules into an executable.
class ASTNode:
    def __init__(self, node_type, value=None):
        self.type = node_type
        self.value = value
        self.children = []

    def __repr__(self):
        return f'{self.type}: {self.value}'

class AST:
    def __init__(self):
        self.root = None

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

    def __repr__(self, level=0):
        ret = "  " * level + f"{self.type}: "
        if self.value is not None:
            ret += f"{self.value}\n"
        else:
            ret += "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def parse(self):
        return self.parse_function()

    def parse_function(self):
        node = ASTNode('FUNCTION')
        return_type = self.match('IDENT')
        function_name = self.match('IDENT')
        node.children.append(('RETURN_TYPE', return_type))
        node.children.append(('FUNCTION_NAME', function_name))
        node.children.append(self.match('LPAREN'))
        node.children.append(self.match('RPAREN'))
        node.children.append(self.match('LBRACE'))
        
        while self.tokens[self.pos][1] != '}':
            self.pos += 1
        
        node.children.append(self.match('RBRACE'))
        return node

    def parse_return_statement(self):
        node = ASTNode('ReturnStatement')
        self.match('return')
        node.children.append(self.match('1'))
        self.match(';')
        return node

    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            token_value = self.tokens[self.pos][1]
            self.pos += 1
            return token_value
        else:
            raise ValueError(f"Expected {expected_type} but got {self.tokens[self.pos][1] if self.pos < len(self.tokens) else 'EOF'}")
