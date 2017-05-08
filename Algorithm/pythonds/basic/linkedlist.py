class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def add(self, item):
        newnode = Node(item)
        newnode.next = self.head
        self.head = newnode

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current.getData() != item:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
'''
mylist = LinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.search(93))
print(mylist.size())
mylist.remove(54)
print(mylist.size())
'''

