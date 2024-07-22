def add(operand1, operand2):
    return operand1 + operand2


def subtract(operand1, operand2):
    return operand1 - operand2


def multiply(operand1, operand2):
    return operand1 * operand2


def divide(operand1, operand2):
    if float(operand2) == 0.0:
        raise ZeroDivisionError
    else:
        return float(operand1) / float(operand2)
