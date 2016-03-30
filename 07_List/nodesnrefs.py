class Node:
    def __init__(self, payload=99):
        self.data = payload
        self.next = None



class UnorderedList:
    def __init__(self):
        self.head = None

    def append(self, payload):
        if self.head == None:
            self.head = Node(payload)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = Node(payload)

    def add(self, payload):
        if self.head == None:
            self.head = Node(payload)
        else:
            newNode = Node(payload)
            newNode.next = self.head
            self.head = newNode

    def print(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next


    def remove(self,item):
        # find the node where the payload matches item
        # remove that node from the list
        if self.head == None:
            return

        currentNode = self.head
        previous = None
        while currentNode != None:
            if currentNode.data == item:
                if previous == None:
                    self.head = currentNode.next
                else:
                    previous.next = currentNode.next
                currentNode.next = None
                break
            else:
                previous = currentNode
                currentNode = currentNode.next


    def __getitem__(self, item):
        currentNode = self.head
        idx = 0
        while currentNode != None and idx < item:
            currentNode = currentNode.next
            idx += 1

        if idx == item:
            return currentNode.data
        else:
            raise IndexError("list index out of range")


    def __setitem__(self, setidx, val):
        currentNode = self.head
        idx = 0
        while currentNode != None and idx < setidx:
            currentNode = currentNode.next
            idx += 1

        if idx == setidx and currentNode:
            currentNode.data = val
        else:
            raise IndexError("list index out of range")

mylist = UnorderedList()
for i in range(10):
    mylist.append(i)

mylist.print()
print("====")
mylist.remove(5)
mylist.print()
print("===")
print("testing index", mylist[3])
#print(mylist[20])
print(mylist[8])
mylist.print()




# ==============

from timeit import Timer

def test1():
    l = UnorderedList()
    for i in range(1000):
        l.add(i)

def test2():
    l = list()
    for i in range(1000):
        l.insert(0,i)

t1 = Timer("test1()", "from __main__ import test1")
print(t1.timeit(1000))
t2 = Timer("test2()", "from __main__ import test2")
print(t2.timeit(1000))
