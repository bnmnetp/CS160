import collections
import time

class Rand:
    def __init__(self,seed):
        self.seed = seed

    def next(self):
        self.seed = (self.seed * 58321 + 11113) % 65536
        return self.seed

    def randrange(self, start, end):
        n = self.next()
        n = n % (end-start) + start
        return n

class MLCGRand(Rand):
    def next(self):
        a = 24
        m = 100000001
        c = 0
        self.seed = (a * self.seed + 0) % m
        return self.seed

x = MLCGRand(123789)
t = [x.next()%6 for i in range(1000)]

# For n = 4, this occurs with the values 0100, 2500, 3792, and 7600. Other seed values form very short repeating cycles, e.g., 0540 → 2916 → 5030 → 3009

class Rand2:
    def __init__(self,seed):
        self.seed = seed
        self.n = 6

    def next(self):
        sqr = self.seed * self.seed
        sqr_str = str(sqr)
        start = (len(sqr_str) - self.n) // 2
        sqr_str = sqr_str[start:start+self.n]
        self.seed = int(sqr_str)
        return self.seed

    def randrange(self, start, end):
        n = self.next()
        n = n % (end-start) + start
        return n

x = MLCGRand(123456789)
start = time.time()
seen = set([123456789])
#seen = [192351]
count = 0
done = False
while not done:
    n = x.next()
    if n in seen:
        done = True
    else:
        seen.add(n)
        count += 1

end = time.time()
print("Time: %d" % (end-start))
print("The period is ", count)


class FibRand:
    def __init__(self, seed):
        self.a = self.fibb(seed-1)
        self.b = self.fibb(seed)

    def next(self):
        nn = self.a + self.b
        self.a = self.b
        self.b = nn
        return nn

    def fibb(self,n):
        a = 1
        b = 1
        for i in range(n):
            n = a + b
            a = b
            b = n
        return n

f = FibRand(5)
print("XXX", f.a,f.b)
s = [f.next()%6 for i in range(20)]
print(s)
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
    for x in range(len(seq)):
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
