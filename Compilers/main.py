from lexer_step1 import tokenize
from parser_step2 import Parser
from semantic_analyzer_step3 import SemanticAnalyzer
from assemble import Assembler
code = """
int main() {
    return 10;
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
assembler = Assembler()
assembler.generate_code(ast)

# Print assembly code
assembly_code = '\n'.join(assembler.assembly_code)
print(f'Generated assembly code:\n{assembly_code}')

assembler.write_to_file("output.s")

# python main.py
# as -o one.o one.s
# ld -o one one.o
# ./one
# echo $?

# python main.py && as -o one.o one.s && ld -o one one.o && ./one && echo $?
