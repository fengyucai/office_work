import copy

spam = [1, ['a', 'b']]
copy_spam = copy.copy(spam)
deepcopy_spam = copy.deepcopy(spam)

copy_spam[1][1] = 'Hello'
print(copy_spam)
print(spam)

deepcopy_spam[1].append('Hi')
print(deepcopy_spam)
print(spam)
