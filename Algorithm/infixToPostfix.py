from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = prec['/'] = 3
    prec['+'] = prec['-'] = 2
    prec['('] = 1
    opstack = Stack()
    postfixList = []
    for token in infixexpr:
        if token.isalnum():
            postfixList.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()  # if top is '(' already popped
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while not opstack.isEmpty() and\
                prec[opstack.peek()] >= prec[token]:
                postfixList.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixList.append(opstack.pop()) 
    return ''.join(postfixList)


print(infixToPostfix('A+B*C'))
print(infixToPostfix('(A+B)*C-(D-E)*(F+G)'))
