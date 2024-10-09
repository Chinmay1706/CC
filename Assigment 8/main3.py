class Quadruple:
    def __init__(self, operator, arg1, arg2, result):
        self.operator = operator
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __repr__(self):
        return f"({self.operator}, {self.arg1}, {self.arg2}, {self.result})"


class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.quadruples = []

    def new_temp(self):
        """ Generate a new temporary variable """
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate_quadruple(self, operator, arg1, arg2=None):
        """ Generate a quadruple and store it in the list """
        result = self.new_temp()
        quad = Quadruple(operator, arg1, arg2, result)
        self.quadruples.append(quad)
        return result

    def postfix_to_quadruples(self, postfix_expr):
        """ Generate quadruples from a postfix expression """
        stack = []
        operators = {'+', '-', '*', '/'}  # Define basic operators

        for token in postfix_expr:
            if token not in operators:
                stack.append(token)
            else:
                if token == '-' and len(stack) == 1:  # Handle unary minus
                    arg1 = stack.pop()
                    result = self.generate_quadruple('UMINUS', arg1)  # Unary minus is a special case
                    stack.append(result)
                else:
                    # Pop two operands for a binary operation
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result = self.generate_quadruple(token, arg1, arg2)
                    stack.append(result)

    def display_quadruples(self):
        """ Display all the generated quadruples in four columns """
        print(f"{'Operation':<12}{'Argument1':<12}{'Argument2':<12}{'Result':<12}")
        print("=" * 48)
        for quad in self.quadruples:
            print(f"{quad.operator:<12}{quad.arg1:<12}{quad.arg2 if quad.arg2 else '':<12}{quad.result:<12}")


def precedence(op):
    """ Define precedence of operators """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    """ Convert infix expression to postfix using Shunting Yard algorithm """
    stack = []  # Stack to hold operators
    postfix = []  # List for output
    operators = {'+', '-', '*', '/'}  # Basic operators

    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isalnum():  # If character is operand (variable or number)
            postfix.append(char)
        elif char == '(':  # If left parenthesis
            stack.append(char)
        elif char == ')':  # If right parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the left parenthesis
        elif char in operators:  # If operator
            # Handle unary minus (e.g., -c)
            if char == '-' and (i == 0 or expression[i-1] in '(*+-/'):
                postfix.append('0')  # Add 0 for unary minus case, i.e., 0 - c
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
        i += 1

    # Pop the remaining operators from the stack
    while stack:
        postfix.append(stack.pop())

    return postfix


# Example usage
expression = input("Enter an infix expression (e.g., ((x+y)-((x+y)*(x-y)))+((x+y)*(x-y))): ")

# Convert infix to postfix
postfix_expr = infix_to_postfix(expression)

# Generate quadruples
generator = IntermediateCodeGenerator()
generator.postfix_to_quadruples(postfix_expr)

# Display generated quadruples
print("\nGenerated Quadruples:")
generator.display_quadruples()
