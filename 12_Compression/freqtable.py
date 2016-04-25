# Create a table of letter frequencies using some gutenberg books
from collections import Counter, OrderedDict
from pythonds.trees.binaryTree import BinaryTree

def doOneBook(title):
    with open(title,'r') as book:
        c = Counter(book.read())

    return c

allCharacters = doOneBook('pg36.txt')
for book in ['pg36.txt', 'pg74.txt', 'pg98.txt', 'pg244.txt']:
    allCharacters.update(doOneBook(book))

total = sum(allCharacters.values())
probChars = OrderedDict()

for ch,count in sorted(allCharacters.items(),reverse=True,key=lambda x: x[1]):
    probChars[ch] = count/total

for ch,prob in probChars.items():
    print("{} : {:8.7f}".format(ch,prob).replace('\n','\\n').replace('\t','\\t'))

# Make a binary tree where the value of the root node is the priority
# Modify insert left/right to accept a BinaryTree rather than make one.

# The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

# Create a leaf node for each symbol and add it to the priority queue.
# While there is more than one node in the queue:
# Remove the two nodes of highest priority (lowest probability) from the queue
# Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.
# Add the new node to the queue.
# The remaining node is the root node and the tree is complete.
# Since efficient priority queue data structures require O(log n) time per insertion, and a tree with n leaves has 2n−1 nodes, this algorithm operates in O(n log n) time, where n is the number of symbols.
