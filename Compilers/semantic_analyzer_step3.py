class SemanticAnalyzer:
    def __init__(self, node_type):
        self.errors = []
        self.node_type = node_type

    def analyze(self, node):
        if node.type == self.node_type:
            self.analyze_function(node)
        elif node.type == 'ReturnStatement':
            self.analyze_return_statement(node)

    def analyze_function(self, node):
        return_type = node.children[0].value
        function_body = node.children[2]
        node.return_type = return_type
        self.analyze(function_body)

    def analyze_return_statement(self, node):
        return_value = node.children[0].value
        if not return_value.isdigit():
            self.errors.append(
                f"Return value {return_value} is not a valid integer")

    def report_errors(self):
        if self.errors:
            print("Semantic Analysis Errors:")
            for error in self.errors:
                print(error)
        else:
            print("No semantic errors found.")
