from pythonds.basic import Stack

def revstring(mystr):
    s = Stack()
    for ch in mystr:
        s.push(ch)
    revstr = ''
    while not s.isEmpty():
        revstr += s.pop()
    return revstr


print(revstring('apple'))
print(revstring('123456'))
