from lexer_step1 import tokenize
from parser_step2 import Parser
from semantic_analyzer_step3 import SemanticAnalyzer

code = """
int main() {
    return 1;
}
"""

tokens = tokenize(code)
print("Tokens:", tokens)

parser = Parser(tokens)
ast = parser.parse()
print("AST:")
print(ast)
analyzer = SemanticAnalyzer(node_type='Function')
analyzer.analyze(ast)
analyzer.report_errors()

