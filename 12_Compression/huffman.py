from pythonds import BinaryTree
from freqtable import allCharacters
from heapq import heapify, heappop, heappush

class QueueableBinaryTree(BinaryTree):

    def __init__(self, priority, value):
        super().__init__(priority)
        self.value = value

    def __lt__(self, other):
        if self.key < other.key:
            return True
        return False


treequeue = [QueueableBinaryTree(x[1],x[0]) for x in allCharacters.items()]
heapify(treequeue)


# Make a binary tree where the value of the root node is the priority
# Modify insert left/right to accept a BinaryTree rather than make one.

# The simplest construction algorithm uses a priority queue where the node with lowest probability
# is given highest priority:

# Create a leaf node for each symbol and add it to the priority queue.
# While there is more than one node in the queue:
#     Remove the two nodes of highest priority (lowest probability) from the queue
#     Create a new internal node with these two nodes as children and with probability equal to the sum
#         of the two nodes' probabilities.
#     Add the new node to the queue.
# The remaining node is the root node and the tree is complete.


def buildHuffmanCode(pq):
    while len(pq) > 1:
        a = heappop(pq)
        b = heappop(pq)
        newkey = a.key + b.key
        t = QueueableBinaryTree(newkey,'internal')
        t.insertLeft(a)
        t.insertRight(b)
        heappush(pq,t)
    return heappop(pq)

root = buildHuffmanCode(treequeue)
huffmanTable = {}

def makeTable(tree,p):
    if tree:
        if tree.value != 'internal':
            huffmanTable[tree.value] = p
        else:
            makeTable(tree.leftChild,p+"1")
            makeTable(tree.rightChild,p+"0")


makeTable(root,"")

for k,v in sorted(huffmanTable.items(),key=lambda x: len(x[1])):
    print(k.replace('\n','\\n').replace('\t','\\t'),v)



bits = 0
with open('pg36.txt','r') as f:
    for ch in f.read():
        bits += len(huffmanTable[ch])

print("Bytes = {}".format(bits/8))
