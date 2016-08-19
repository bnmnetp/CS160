#!/usr/bin/env python3

import random

alphabet = "abcdefghijklmnopqrstuvwxyz "
goal = "methinks it is like a weasel"
NUM_CHANGES = 2

#
# Start Here
#
def genString(old_string):
    '''
        Here's how the monkeys would do it.  just generate a random string of
        length str_len.  Who knows what we might get?
    '''
    new_string = ""
    for i in range(len(old_string)):
        #new_string += alphabet[random.randrange(len(alphabet))]
        new_string += random.choice(alphabet)
    return new_string

def scoreString(test_string, goal_string):
    '''
        zip together the test_string and goal_string then iterate over the pairs,
        calculate the percentage that are the same.
        list(map(lambda x,y: x == y, 'abc', 'aBc'))
    '''
    same = 0
    for c1,c2 in zip(goal_string,test_string):
        if c1 == c2:
            same = same + 1
    score = same / len(goal_string)
    return score*100


def mutateString(old_string):
    '''
        Rather than generating the entire string from scratch each time
        lets mutate one letter.  The scoring function will decide whether
        this new generation gets to live or die.  If we are closer to the goal then
        this becomes the new starting point, if we are not then we'll keep the old.
    '''
    rep_letter = random.randrange(len(old_string))
    new_letter = alphabet[random.randrange(len(alphabet))]
    #print('replacing ', old_string[rep_letter], ' with ', new_letter)
    new_string = old_string[:rep_letter] + new_letter + old_string[rep_letter+1:]
    return new_string

def multiMutateString(old_string):
    '''
        Rather than simply replacing one letter each iteration what if we randomly
        replaced multiple letters per iteration?  Would we get to the goal faster?
    '''
    for i in range(NUM_CHANGES):
        rep_letter = random.randrange(len(old_string))
        new_letter = alphabet[random.randrange(len(alphabet))]
        #print('replacing ', old_string[rep_letter], ' with ', new_letter)
        new_string = old_string[:rep_letter] + new_letter + old_string[rep_letter+1:]
    return new_string


def iterMutate(old_string,rep_letter):
    '''
        Here's another variation.  Lets be systematic about which letters get replaced,
        lets get the first one right, then the second letter and so on.  So we'll build
        the correct string from left to right.  We'd expect this to be even better since
        we are being systematic about which letters to replace, not random.
    '''
    new_letter = alphabet[random.randrange(len(alphabet))]
    new_string = old_string[:rep_letter] + new_letter + old_string[rep_letter+1:]
    return new_string



def test(goal_string, generate):
    start = genString(goal_string)
    outfile = open('watchmaker.out','w')
    score = 0.0
    best_score = 0.0
    iters = 0
    new = start
    pos = 0
    while score < 100.0:
        new = generate(start)
        score = scoreString(new,goal_string)
        if score >= best_score:
            start = new
            best_score = score
            outfile.write("%6.2f : %29s : %d\n" % (score, start, iters))
            outfile.flush()
        iters = iters + 1
        if iters % 100000 == 0:
            outfile.write("%6.2f : %29s : %d\n" % (best_score, start, iters))
            outfile.flush()
    #print(goal_string, new, iters)
    return iters

def test2(goal_string):
    start = genString(goal_string)
    pos = 0
    new = start
    iters = 0
    while pos < len(goal_string):
        new = iterMutate(new,pos)
        iters = iters + 1
        if new[pos] == goal[pos]:
            pos = pos + 1
        if iters % 100 == 0:
            print(iters,new,pos)
    print(goal_string, new, iters)
    return iters



def sentenceScore(new):
    words = new.split()
    wlist = set()
    good_words = 0
    bad_words = 0
    for w in words:
        if w in wlist:
            good_words = good_words + 1
            print(w,' is in the dictionary!!')
        else:
            bad_words = bad_words + 1
    return good_words / (good_words + bad_words)

def test3(numChars):
    '''
        A different question might be whether or not we can generate any sentence.
        It doesn't matter whether there is a goal or it is shakespeare.
    '''
    start = genString(28)
    done = False
    iters = 0
    new = start
    best_score = 0
    while not done:
        new = multiMutateString(start)
        score = sentenceScore(new)
        iters = iters + 1
        if score > best_score:
            start = new
            best_score = score
            print(iters,new)
        # if iters % 100000 == 0:
        #     print(iters,new)

# wordFile = open('/usr/share/dict/words')
# wlist = set()
# for word in wordFile:
#     wlist.add(word)
#test3(28)

# ct = 0
# for i in range(1000):
#     ct = ct + test2(goal)
# print("davids", ct/1000)
#

ct = 0
#for i in range(10):
#    ct = ct + test(goal)
#print("standard",ct/1000)

if __name__ == '__main__':
    print("number of iterations = {}".format(test(goal, multiMutateString)))
