import collections

class Rand:
    def __init__(self,seed):
        self.seed = 123789

    def next(self):
        self.seed = (self.seed * 58321) + 11113;
        return self.seed >> 16


x = Rand(123789)
t = [x.next()%6 for i in range(1000)]

# todo test different starting positions

def find_repeat(seq):
    guess = 1
    max_len = len(seq) // 2 + 1
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            guess = x

    return guess

def search_repeat(seq):
    best_guess = 0
    sp = 0
    for x in range(len(seq)//2):
        guess = find_repeat(seq[x:])
        if guess > 1 and guess > best_guess:
            best_guess = guess
            sp = x
    return best_guess, sp

print("finding a repeat")
print(search_repeat([0, 1, 2, 3, 4, 1, 2, 3, 4]))
print(search_repeat([0, 1, 0, 1, 0, 1, 0, 1]))
print(search_repeat([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]))
l,p = search_repeat(t)
print(l,p)
if l > 10:
    print(t[p:])

print(collections.Counter(t))
