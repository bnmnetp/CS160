from wordlist import *
import time
import re
from pythonds.basic import Queue, Stack

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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def copy(self):
        newStack = Stack()
        newStack.items = self.items[:]
        return newStack


# def oneDifferent(word1,word2):
#     '''
#     return true if the words are different by exactly one character otherwise false
#     assume that the words are the same length.
#     '''
#     diffs = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             diffs += 1
#     if diffs == 1:
#         return True
#     else:
#         return False

def oneDifferent(word1,word2):
    '''
    return true if the words are different by exactly one character otherwise false
    assume that the words are the same length.
    '''
    diffs = 0
    i = 0
    wlen = len(word1)
    while i < wlen and diffs <= 1:
        if word1[i] != word2[i]:
            diffs += 1
        i += 1
    return diffs == 1

def findAllOneDifferent(word,wlist,used):
     res = [w for w in wlist if oneDifferent(w,word) and w not in used]
     return res

def makeRegex(word):
    '''
    Using this regular expression, which is compiled once at the start
    of findAllOneDifferent, is a  nice speedup over using either of the
    oneDifferent methods defined above.
    '''
    pat = r''
    for i in range(len(word)):
        pat = pat + r'(' + word[:i] + r'\w' + word[i+1:] + r')|'
    return pat[:-1]


def x_findAllOneDifferent(word,wlist,used):
    pat = re.compile(makeRegex(word))
    res = [w for w in wlist if pat.match(w) and w not in used]

#    return sorted(res, key=goalDiff)
    return res

def y_findAllOneDifferent(word,wlist,used):
    '''
    Technically this does not find all the words that are different, it just
    generates all the possible words that are different by one character then
    tests to see if they are real words and/or if they are used.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for i in range(len(word)):
        for c in alphabet:
            nw = word[:i] + c + word[i+1:]
            if nw in wlist and nw not in used:
                res.append(nw)

    return res

def createStacks(currentStack,queue,used,goal,wlist):
    '''
    Get a bunch of new words that are just one letter different from
    the top of the front stack.  if one of the newly generated words
    is the same as the goal then we are done.  If not then add this
    new stack of words to the queue.
    '''
    newWords = findAllOneDifferent(currentStack.peek(),wlist,used)
    for i in newWords:
        newStack = currentStack.copy()
        newStack.push(i)
        used.add(i)
        if i == goal:
            return newStack
        else:
            queue.enqueue(newStack)

def goalDiff(w):
    '''
    possible heuristic... order the words generated from findAllOneDifferent according to
    how close they are to the goal.
    '''
    ct = 0
    for i in range(len(w)):
        if w[i] == end[i]:
            ct += 1
    return len(w) - ct

def wordsOK(start,end,wlist):
    '''
    Verify that the start and end words are the same length and are in the
    list of known words.
    '''
    if len(start) == len(end):
        if len(start) >= 3 and len(start) <= 5:
            return start in wlist[len(start)] and end in wlist[len(start)]
        else:
            return False
    else:
        return False

def main():
    wlist = {}
    wlist[3] = set(threeLetterWords)
    wlist[4] = set(fourLetterWords)
    wlist[5] = set(fiveLetterWords)

    while True:
        start = input('enter the starting word: ')
        if start == 'finished':
            return
        end = input('enter the ending word: ')
        queue = Queue()
        used = set()
        if wordsOK(start,end,wlist):
            used.add(start)
            st_time = time.time()
            startStack = Stack()
            startStack.push(start)
            res =createStacks(startStack,queue,used,end,wlist[len(start)])
            while queue.size() > 0 and not res:
                res = createStacks(queue.dequeue(),queue,used,end,wlist[len(start)])

            et_time = time.time()
            if res:
                fwd = []
                while not res.isEmpty():
                    fwd.insert(0,res.pop())
                for w in fwd:
                    print(w)
            else:
                print('no ladder found')

            print(et_time-st_time)
        else:
            print('You entered a bad word, try again')

main()
