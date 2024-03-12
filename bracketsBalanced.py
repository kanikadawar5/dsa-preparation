def bracketsBalanced(inputStr):
    stack = []
    for ch in inputStr:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            if ch == ')' and stack[-1] != '(':
                return False
            if ch == '}' and stack[-1] != '{':
                return False
            if ch == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == '__main__':
    print(bracketsBalanced('()'))  
    print(bracketsBalanced('()[]{}'))
    print(bracketsBalanced('(]'))
    print(bracketsBalanced('([)]'))
    print(bracketsBalanced('{[]}'))