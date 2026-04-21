from binary_expression_tree import BinaryExpressionTree

def main():
    expr = input("Enter a postfix expression: ")

    tree = BinaryExpressionTree(expr)

    print("\nPostfix form:")
    print(tree.print_postfix())

    print("\nInfix form:")
    print(tree.print_infix())

    print("\nEvaluation result:")
    print(tree.evaluate())

if __name__ == "__main__":
    main()
