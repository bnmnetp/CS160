class Node:
    def __init__(self, payload=99):
        self.data = payload
        self.next = None



class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, payload):
        if self.head == None:
            self.head = Node(payload)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = Node(payload)

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
                # remove the item
                previous.next = currentNode.next
                currentNode.next = None
                return
            else:
                previous = currentNode
                currentNode = currentNode.next


mylist = UnorderedList()
for i in range(10):
    mylist.add(i)

mylist.print()

mylist.remove(5)

mylist.print()


