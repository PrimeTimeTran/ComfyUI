import sys
import re
import clang.cindex
import clang.enumerations
import csv

clang.cindex.Config.set_library_path(
    "/Library/Developer/CommandLineTools/usr/lib")


class Tokenizer:
    # creates the object, does the inital parse
    def __init__(self, path):
        self.index = clang.cindex.Index.create()
        self.tu = self.index.parse(path)
        self.path = self.extract_path(path)

    # To output for split_functions, must have same path up to last two folders
    def extract_path(self, path):
        return "".join(path.split("/")[:-2])

    # does futher processing on a literal token
    def process_literal(self, literal):
        cursor_kind = clang.cindex.CursorKind
        kind = literal.cursor.kind

        if kind == cursor_kind.INTEGER_LITERAL:
            return ["NUM"]

        if kind == cursor_kind.FLOATING_LITERAL:
            return ["NUM"]

        if kind == cursor_kind.IMAGINARY_LITERAL:
            return ["NUM"]

        if kind == cursor_kind.STRING_LITERAL:
            return ["STRING"]

        if kind == cursor_kind.CHARACTER_LITERAL:
            return ["CHAR"]

        if kind == cursor_kind.CXX_BOOL_LITERAL_EXPR:
            return ["BOOL"]

        # catch all other literals
        return ["LITERAL"]

    # filters out unwanted punctuation
    def process_puntuation(self, punctuation):
        spelling = punctuation.spelling

        # ignore certain characters
        if spelling in ["{", "}", "(", ")", ";"]:
            return None

        return [spelling]

    # further processes and identifier token
    def process_ident(self, ident):
        # are we a "special" ident?
        if ident.spelling in ["std", "cout", "cin", "vector", "pair", "string", "NULL", "size_t"]:
            return [ident.spelling]

        # are we a declaration?
        if ident.cursor.kind.is_declaration():
            return ["DEC"]

        # are we a reference kind?
        if ident.cursor.kind.is_reference():
            return ["REF"]

        # are we a variable use?
        if ident.cursor.kind == clang.cindex.CursorKind.DECL_REF_EXPR:
            return ["USE"]

        # catch all others
        return ["IDENT"]

    # tokenizes the contents of a specific cursor
    def full_tokenize_cursor(self, cursor):
        tokens = cursor.get_tokens()

        # return final tokens as a list
        result = []

        for token in tokens:
            if token.kind.name == "COMMENT":
                # ignore all comments
                continue

            if token.kind.name == "PUNCTUATION":
                punct_or_none = self.process_puntuation(token)

                # add only if not ignored
                if punct_or_none != None:
                    result += punct_or_none

                continue

            if token.kind.name == "LITERAL":
                result += self.process_literal(token)
                continue

            if token.kind.name == "IDENTIFIER":
                result += self.process_ident(token)
                continue

            if token.kind.name == "KEYWORD":
                result += [token.spelling]

        return result

    # tokenizes the entire document
    def full_tokenize(self):
        cursor = self.tu.cursor
        return self.full_tokenize_cursor(cursor)

    # returns a list of function name / function / filename tuples
    def split_functions(self, method_only):
        results = []
        cursor_kind = clang.cindex.CursorKind

        # query all children for methods, and then tokenize each
        cursor = self.tu.cursor
        for c in cursor.get_children():
            filename = c.location.file.name if c.location.file != None else "NONE"
            extracted_path = self.extract_path(filename)

            if (c.kind == cursor_kind.CXX_METHOD or (method_only == False and c.kind == cursor_kind.FUNCTION_DECL)) and extracted_path == self.path:
                name = c.spelling
                tokens = self.full_tokenize_cursor(c)
                filename = filename.split("/")[-1]
                results += [(name, tokens, filename)]

        return results


# read in and process the CSV file (once)
token_map = {}
handle = open("token_map.csv", "r")
csv_reader = csv.reader(handle)
for row in csv_reader:
    token_map[row[0]] = chr(int(row[1]))

# attempts to reduce each token to a single character


def compress_tokens(tokens):
    result = []

    for token in tokens:
        if token in token_map:
            result.append(token_map[token])
        else:
            print("UNMAPPED TOKEN: {}").format(token)
            result.append(token)

    return "".join(result)

# def tokenize(code):
#     if len(sys.argv) != 2:
#         print("please provide a file argument")
#         exit(1)

#     tok = Tokenizer(sys.argv[1])
#     results = tok.split_functions(False)
#     for res in results:
#         print(res[0] + " (" + res[2] + "):")
#         print("Tokens: {}".format(res[1]))
#         go = compress_tokens(res[1])
#         print(f"Compressed Tokens: {go}")
#         print("")


def tokenize(code):
    token_specification = [
        ('NUMBER', r'\d+'),
        ('IDENT', r'\b(?:int|return)\b|\b[A-Za-z_]\w*\b'),
        ('OP', r'[+\-*/]'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('SEMICOLON', r';'),
        ('SKIP', r'[ \t]+'),
        ('NEWLINE', r'\n'),
        ('MISMATCH', r'[^A-Za-z0-9+\-*/()\{\};\s]+')
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line_num = 1
    line_start = 0
    pos = 0
    tokens = []
    match = get_token(code)

    while match is not None:
        typ = match.lastgroup
        value = match.group(typ)

        if typ == 'NUMBER':
            tokens.append(('NUM', int(value)))
        elif typ == 'IDENT':
            tokens.append(('IDENT', value))
        elif typ == 'OP':
            tokens.append((typ, value))
        elif typ in {'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON'}:
            tokens.append((typ, value))
        elif typ == 'NEWLINE':
            line_start = match.end()
            line_num += 1
        elif typ == 'SKIP':
            pass
        elif typ == 'MISMATCH':
            print(f'typ {typ}')
            raise RuntimeError(
                f'Unexpected token {value} at line {line_num} position {match.start() - line_start}')

        pos = match.end()
        match = get_token(code, pos)

    return tokens
