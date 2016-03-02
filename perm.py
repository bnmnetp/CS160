import timeit
import time

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def perms(word):
    stack = Stack()
    for l in word:
        stack.push(l)
    results = [stack.pop()]
    while stack.size() != 0:
        newLetter = stack.pop()
        newResults = []
        for w in results:
            for insertPosition in range(len(w)+1):
                newResults.append(w[:insertPosition] + newLetter + w[insertPosition:])
        results = newResults
    return results

start = time.time()
print(len(perms("abcdefghijkl")))
end = time.time()
print(end-start)

#print(timeit.timeit('perms("dog")',setup=setup))