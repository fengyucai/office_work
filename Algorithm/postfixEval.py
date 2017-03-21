from pythonds.basic import Stack

def postfixEval(postexpr):
    operandStack = Stack()
    for token in postexpr:
        if token.isalnum():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop() # the top is right-operand
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('78+32+/'))
