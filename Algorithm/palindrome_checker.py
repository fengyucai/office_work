from pythonds.basic import Deque

def palindrome_checker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)

    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            return False
    return True

print(palindrome_checker('palindrome'))
print(palindrome_checker('radar'))
print(palindrome_checker('madam'))

