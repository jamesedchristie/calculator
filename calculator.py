# Making a command line calculator. Works pretty good.
# Still doesn't handle 1+-2 (1 + -2 is fine).
# Doesn't accept implicit multiplication (i.e. 2a, 3b, etc.)

from operate import operate
from postfix import get_prefix, get_postfix
from check import valid_input

# Dict to store variables
all_variables = {}

# Dict to store operators and their precedence
precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
special = ['+', '-', '*', '/', '^', '(', ')']

def calculate(prefix):
    postfix = get_postfix(prefix)

    # Calculate result from postfix expression
    results = []

    for post in postfix:
        if post.isdigit():
            results.append(int(post))
        if post.isalpha():
            results.append(all_variables[post])
        if post[0] == '-':
            if post[1:].isdigit():
                results.append(int(post))
            elif post[1:].isalpha():
                results.append(-(all_variables[post[1:]]))
        if post in precedence:
            results.append(operate(results.pop(), results.pop(), post))

    result = results.pop()
    if result % 1 == 0:
        return int(result)
    else:
        return result

def assign(prefix):
    variable = prefix[0]
    value = prefix[2:]
    all_variables[variable] = calculate(value)

# get user input
text = input()

# Run program until exit command given
while text != "/exit":
    # Inner while loop allows program to break to new input prompt at any given stage
    while True:
        # Check that something has been inputted
        if len(text) > 0:
            # Check for commands
            if text[0] == "/":
                if text == "/help":
                    print("The program calculates result of inputted equation. Variables can be assigned " \
                            "in format x = y")
                else:
                    print("Unknown command")
                break

            prefix = get_prefix(text)

            # Run valid operation check
            if not valid_input(prefix, all_variables):
                break

            # Check if input is assignment
            if '=' in prefix:
                assign(prefix)
                print(all_variables)
                break

            else:              
                print(calculate(prefix))
                                
                # Break to prompt new input
                break    
        else:
            break
    # Take new input after error or completed calculation
    text = input()
# Print bye and quit if exit command given
else:
    print("Bye!")