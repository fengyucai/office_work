import copy

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
cheese = copy.copy(spam)
eggs(cheese)
print(spam)
print(cheese)


