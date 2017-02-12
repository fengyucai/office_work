from pythonds.basic import Stack

def par_checker(symbolstr):
    s = Stack()
    for symbol in symbolstr:
        if symbol in '{[(':
            s.push(symbol)
        elif symbol in '}])':
            if s.isEmpty():
                return False
            top = s.pop()
            if not matches(top, symbol):
                return False

    if not s.isEmpty():
        return False
    else:
        return True

def matches(opening, closing):
    opens = '{[('
    closes = '}])'
    return opens.index(opening) ==\
           closes.index(closing)

print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
