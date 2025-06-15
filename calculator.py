import ast
import operator

class SafeEvaluator:
    def __init__(self):
        self.ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
        }

    def evaluate(self, expr):
        try:
            node = ast.parse(expr, mode='eval').body
            return self._eval(node)
        except Exception:
            return "Error"

    def _eval(self, node):
        if isinstance(node, ast.BinOp):
            return self.ops[type(node.op)](self._eval(node.left), self._eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return self.ops[type(node.op)](self._eval(node.operand))
        elif isinstance(node, ast.Constant):
            return node.value
        else:
            raise TypeError(f"Unsupported type: {type(node)}")
