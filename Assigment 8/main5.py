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

    def postfix_to_quadruples(self, postfix_expr, lhs_var=None):
        """ Generate quadruples from a postfix expression """
        stack = []
        operators = {'+', '-', '*', '/'}  # Define basic operators

        for token in postfix_expr:
            if token not in operators:
                stack.append(token)
            else:
                if token == '-':  # Check for unary minus case
                    if len(stack) == 1:  # Unary minus case, only one operand
                        arg1 = stack.pop()
                        result = self.generate_quadruple('-', '0', arg1)  # Unary minus is handled as 0 - operand
                        stack.append(result)
                    else:
                        # Binary minus operation
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        result = self.generate_quadruple(token, arg1, arg2)
                        stack.append(result)
                else:
                    # For other operators, always binary
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result = self.generate_quadruple(token, arg1, arg2)
                    stack.append(result)

        # After processing, assign the result to the left-hand side variable if it exists
        if lhs_var is not None:
            final_result = stack.pop()
            self.quadruples.append(Quadruple('=', final_result, None, lhs_var))
        else:
            # In case there is no assignment, just pop the final result without assignment
            stack.pop()

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
                postfix.append('0')  # Add 0 for unary minus case
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
        i += 1

    # Pop the remaining operators from the stack
    while stack:
        postfix.append(stack.pop())

    return postfix


# Example usage
expression = input("Enter an infix expression (e.g., a=(b*(-c))+(b*(-c))): ")

# Check if there is an assignment operator
if '=' in expression:
    # Split the input into LHS and RHS
    lhs_var, rhs_expr = expression.split('=', 1)
    lhs_var = lhs_var.strip()  # Clean up LHS variable
else:
    # If no assignment operator, treat the entire input as RHS expression
    lhs_var = None
    rhs_expr = expression.strip()

# Convert the RHS infix expression to postfix
postfix_expr = infix_to_postfix(rhs_expr)

# Generate quadruples
generator = IntermediateCodeGenerator()
generator.postfix_to_quadruples(postfix_expr, lhs_var)

# Display generated quadruples
print("\nGenerated Quadruples:")
generator.display_quadruples()
