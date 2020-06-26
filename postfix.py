precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
special = ['+', '-', '*', '/', '^', '(', ')', '=']

# Function to parse input into usable list
def get_prefix(text):
    prefix = []
    
    # Iterate through entire input string, creating prefix expression
    i = 0
    while i < len(text):
        if text[i].isdigit():
            n = []
            # Create integer out of uninterrupted string of digits and append to list
            while i < len(text) and text[i].isdigit() :
                n.append(text[i])
                i += 1
            prefix.append("".join(n))
        elif text[i].isalpha():
            a = []
            # Create variable out of uninterrupted string of letters and append to list
            while i < len(text) and text[i].isalpha():
                a.append(text[i])
                i += 1
            prefix.append("".join(a))
        # Ignore spaces 
        elif text[i] == " ":
            i += 1
        # Handle operators
        elif text[i] in precedence:
            # Check if it's a negative sign rather than operator
            if text[i] == '-':
                if len(prefix) == 0 or prefix[-1] in special: 
                    if text[i + 1].isdigit():
                        n = ['-']
                        i += 1
                        while i < len(text) and text[i].isdigit() :
                            n.append(text[i])
                            i += 1
                        prefix.append("".join(n))
                        continue
                    elif text[i + 1].isalpha():
                        a = ['-']
                        i += 1
                        while i < len(text) and text[i].isalpha():
                            a.append(text[i])
                            i += 1
                        prefix.append("".join(a))
                        continue
            # If multiple operation signs in a row, group them in a list
            seq = []
            while i < len(text) and text[i] in precedence:
                seq.append(text[i])
                i += 1
            if '+' in seq:
                o = '+'
            elif '-' in seq:
                if seq.count('-') % 2 == 0:
                    o = '+'
                else:
                    o = '-'
            elif '*' in seq:
                if seq.count('*') == 1:
                    o = '*'
                else:
                    print("Invalid expression")
                    return None
            elif '/' in seq:
                if seq.count('/') == 1:
                    o = '/'
                else:
                    print("Invalid expression")
                    return None
            elif '^' in seq:
                if seq.count('^') == 1:
                    o = '^'
                else:
                    print("Invalid expression")
                    return None
            prefix.append(o)
        elif text[i] == '(':
            prefix.append(text[i])
            i += 1
        elif text[i] == ')':
            prefix.append(text[i])
            i += 1
        elif text[i] == '=':
            prefix.append(text[i])
            i += 1
    return prefix

def get_postfix(prefix):
    postfix = []
    stack = []

    # Iterate through prefix list, creating postfix expression
    for i in prefix:
        if i.isdigit() or i.isalpha():            
            postfix.append(i)
        if i[0] == '-' and len(i) > 1:
            postfix.append(i) 
        elif i in precedence:
            if len(stack) == 0 or stack[-1] == '(' or precedence[i] > precedence[stack[-1]]:
                stack.append(i)                            
            else:
                while len(stack) > 0 and stack[-1] != '(' and precedence[i] <= precedence[stack[-1]]:
                    postfix.append(stack.pop())
                else:
                    stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            else:
                stack.pop()
    
    for _i in range(len(stack)):
        postfix.append(stack.pop())
    return postfix