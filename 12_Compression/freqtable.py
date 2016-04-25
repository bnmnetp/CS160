# Create a table of letter frequencies using some gutenberg books
from collections import Counter, OrderedDict


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

if __name__ == '__main__':
    for ch,prob in probChars.items():
        print("{} : {:8.7f}".format(ch,prob).replace('\n','\\n').replace('\t','\\t'))


