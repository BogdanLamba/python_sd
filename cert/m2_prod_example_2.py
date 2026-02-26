# Part 1

# calculator.py - Production-grade simple calculator

def calculate(operation, a, b):
    """
    Performs basic arithmetic operations.

    Args:
        operation (str): One of '+', '-', '*', '/'
        a (float): First number
        b (float): Second number

    Returns:
        float: Result of operation

    Raises:
        ValueError: If operation is invalid
        ZeroDivisionError: If dividing by zero
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Invalid operation: {operation}")


# Usage example
if __name__ == "__main__":
    result = calculate('+', 10, 5)
    print(f"10 + 5 = {result}")
