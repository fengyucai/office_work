from pythonds.basic import Stack

def par_checker(symbolstr):
    s = Stack()
    for symbol in symbolstr:
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.isEmpty():
                return False
            s.pop()
    if not s.isEmpty():
        return False
    else:
        return True

print(par_checker('((()))'))
print(par_checker('()))'))
print(par_checker('(()()(()'))

