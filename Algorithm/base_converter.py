from pythonds.basic import Stack

def base_converter(decimal, base):
    remstack = Stack()
    digits = '0123456789ABCDEF' 
    while decimal > 0:
        remstack.push(decimal % base)
        decimal = decimal // base
    newstr = ''
    while not remstack.isEmpty():
        newstr += digits[remstack.pop()]
    return newstr
    

print(base_converter(25, 2))
print(base_converter(25, 16))
