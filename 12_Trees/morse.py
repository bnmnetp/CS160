from pythonds.trees.binaryTree import BinaryTree

class Morse:
    def __init__(self,datafile):
        self.morseTree = BinaryTree('')

        with open(datafile) as morsefile:
            for line in morsefile:
                letter, code = line.split()
                self.followAndInsert(code,letter)

    def followAndInsert(self,codestring,symbol):
        current = self.morseTree
        while codestring != "":
            if codestring[0] == ".":
                if not current.leftChild:
                    current.insertLeft('')
                current = current.leftChild
            elif codestring[0] == "-":
                if not current.rightChild:
                    current.insertRight('')
                current = current.rightChild
            if len(codestring) == 1:
                current.key = symbol
            codestring = codestring[1:]

    def followAll(self,codestring):
        current = self.morseTree
        for letter in codestring:
            if letter == ".":
                current = current.leftChild
            else:
                current = current.rightChild
        return current.key

    def decode(self,mcode):
        letters = mcode.split()
        res = ""
        for letter in letters:
            res += self.followAll(letter)
        return res

    def findKey(self,tree,ch,path):
        if not tree:
            return False
        if tree.key == ch:
            return path
        return self.findKey(tree.leftChild, ch, path+".") or self.findKey(tree.rightChild, ch, path+"-")

    def encode(self,message):
        res = ""
        words = message.split()
        for word in words:
            for ch in word:
                res += self.findKey(self.morseTree,ch,"") + " "
            res += '  '
        return res

if __name__ == '__main__':
    m = Morse('morse.dat')
    with open('morse.dat') as testfile:
        for line in testfile:
            letter, code = line.split()
            print(m.decode(code))

    print(m.encode("sos"))
    print(m.encode("data structures"))



