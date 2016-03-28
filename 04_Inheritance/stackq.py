from pythonds.basic import Stack

class Queue:
    def __init__(self):
        self.inputstack = Stack()
        self.outputstack = Stack()

    def enqueue(self,item):
        self.inputstack.push(item)

    def dequeue(self):
        if self.outputstack.size() > 0:
            return self.outputstack.pop()
        else:
            while self.inputstack.size() > 0:
                self.outputstack.push(self.inputstack.pop())
            if self.outputstack.size() > 0:
                return self.outputstack.pop()
            else:
                raise Exception("empty Queue")

    def size(self):
        return self.inputstack.size() + self.outputstack.size()

    def isEmpty(self):
        return self.size() == 0


tq = Queue()

for i in range(10):
    tq.enqueue(i)
    if i % 3 == 0:
        print(tq.dequeue())
print("===")
while tq.size() > 0:
    print(tq.dequeue())

