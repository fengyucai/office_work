from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = prec['/'] = 3
    prec['+'] = prec['-'] = 2
    prec['('] = prec[')'] = 1
    opstack = Stack()
    tokenList = infixexpr.split() 
    outputList = []
    for token in tokenList:
        if token.isalnum():
            outputList.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                outputList.append(topToken)
                topToken = opstack.pop()
        else:
            while not opstack.isEmpty() and\
                (prec[opstack.peek()] >= prec[token]):
                outputList.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        outputList.append(opstack.pop())
    return ' '.join(outputList)

print(infixToPostfix('A * B + C * D'))
print(infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )'))
                

            
            
