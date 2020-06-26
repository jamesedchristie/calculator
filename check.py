# Function to check input is valid operation
def valid_input(prefix, all_variables):
    valid_ops = ['+', '-', '*', '/', '^']

    # Check that expression doesn't end in operator
    if prefix[-1] in valid_ops:
        print("Invalid expression")
        return False
    # Check that there is only one = sign
    if prefix.count('=') > 1:
        print("Invalid assignment")
        return False
    # Check for valid parentheses
    if '(' in prefix or ')' in prefix:
        if prefix.index('(') > prefix.index(')') or prefix.count('(') != prefix.count(')'):
            print("Invalid expression")
            return False
    # If only a variable is inputted, check it is known
    if '=' not in prefix:        
        if len(prefix) == 1 and prefix[0].isalpha() and prefix[0] not in all_variables:
            print("Unknown variable")
            return False
    # If operation is to assign value to variable...
    if prefix.count('=') == 1:
        # Separate left and right side of operation to variable and value respectively
        variable = prefix[0]
        value = prefix[2:]
        # Check variable is only letters
        if not variable.isalpha():
            print("Invalid identifier")
            return False
        # Check value is either a number or only letters
        elif not valid_input(value, all_variables):
            print("Invalid assignment")
            return False
        # If it's letters, check it is a known variable
        else:
            for i in value:
                if i.isalpha() and i not in all_variables:
                    print("Unknown variable")
                    return False
    
    return True