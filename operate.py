# Function to perform operations on two values
def operate(y, x, op):
    if "+" in op:
        return x + y
    elif op.count("-") % 2 == 1:
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    elif op == "^":
        return x ** y