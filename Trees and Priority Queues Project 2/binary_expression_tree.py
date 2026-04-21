from typing import Optional, Union
from stack import Stack

Number = Union[int, float]


class Node:
    def __init__(self, value: Union[str, Number]):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def is_operator(self) -> bool:
        return isinstance(self.value, str)


class BinaryExpressionTree:
    SUPPORTED_OPERATORS = {"+", "-", "*", "/", "^"}

    def __init__(self, postfix_expr: Optional[str] = None):
        self.root: Optional[Node] = None
        if postfix_expr is not None and postfix_expr.strip():
            self.build_from_postfix(postfix_expr)

    def is_empty(self) -> bool:
        return self.root is None

    def build_from_postfix(self, postfix_expr: str) -> None:
        tokens = postfix_expr.strip().split()
        stack = Stack()

        for token in tokens:
            if self._is_number(token):
                stack.push(Node(self._to_number(token)))
            elif token in self.SUPPORTED_OPERATORS:
                if stack.is_empty():
                    raise ValueError("Malformed postfix expression.")
                right = stack.pop()
                if stack.is_empty():
                    raise ValueError("Malformed postfix expression.")
                left = stack.pop()
                op_node = Node(token)
                op_node.left = left
                op_node.right = right
                stack.push(op_node)
            else:
                raise ValueError(f"Unknown token: {token}")

        if stack.is_empty():
            raise ValueError("Malformed postfix expression.")
        self.root = stack.pop()
        if not stack.is_empty():
            raise ValueError("Malformed postfix expression.")

    def evaluate(self) -> Number:
        if self.is_empty():
            raise ValueError("Cannot evaluate an empty tree.")
        return self._evaluate_recursive(self.root)

    def print_infix(self) -> str:
        if self.is_empty():
            return ""
        return self._infix_recursive(self.root)

    def print_postfix(self) -> str:
        if self.is_empty():
            return ""
        return self._postfix_recursive(self.root).strip()

    def _is_number(self, token: str) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False

    def _to_number(self, token: str) -> Number:
        val = float(token)
        return int(val) if val.is_integer() else val

    def _evaluate_recursive(self, node: Node) -> Number:
        if not node.is_operator():
            return node.value
        left_val = self._evaluate_recursive(node.left)
        right_val = self._evaluate_recursive(node.right)
        op = node.value
        if op == "+":
            return left_val + right_val
        if op == "-":
            return left_val - right_val
        if op == "*":
            return left_val * right_val
        if op == "/":
            if right_val == 0:
                raise ZeroDivisionError("Division by zero.")
            return left_val / right_val
        if op == "^":
            return left_val ** right_val
        raise ValueError(f"Unsupported operator: {op}")

    def _infix_recursive(self, node: Node) -> str:
        if not node.is_operator():
            return str(node.value)
        left = self._infix_recursive(node.left)
        right = self._infix_recursive(node.right)
        return f"({left} {node.value} {right})"

    def _postfix_recursive(self, node: Node) -> str:
        if not node.is_operator():
            return str(node.value) + " "
        left = self._postfix_recursive(node.left)
        right = self._postfix_recursive(node.right)
        return left + right + node.value + " "
