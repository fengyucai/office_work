def spam():
    global eggs
    eggs = 'spam' # This is the global

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)  # This is the global

eggs = 42
spam()
print(eggs)
ham()
