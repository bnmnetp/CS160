
class MyMap:
    def __init__(self):
        self.keys = []
        self.values = []

    def add(self,key,value):
        self.keys.append(key)
        self.values.append(value)

    def lookup(self,key):
        """
        given a key, return the corresponding value
        :param key:
        :return:
        """

    def lookup(self,key):
        # turn self.keys into a list of tuples here!
        res = self.binsearch(list(enumerate(self.keys)), key)
        if res >= 0:
            return self.values[res]
        else:
            raise KeyError("Key {} not found".format(key))


    def binsearch(self,keylist, base, key):
        midpoint = len(keylist) // 2
        if key == keylist[midpoint]:
            return (midpoint+base)
        elif len(keylist) <= 1:
            return -(midpoint+base)
        else:
            if key > self.keys[midpoint]:
                return self.binsearch(keylist[midpoint+1:], midpoint+1+base, key)
            else:
                return self.binsearch(keylist[:midpoint],base, key)


    def binsearch(self, keylist, key):
        midpoint = len(keylist) // 2
        print("mp = ", midpoint,keylist)
        if key == keylist[midpoint][1]:
            return keylist[midpoint][0]
        elif len(keylist) <= 1:
            return -keylist[midpoint][0]
        else:
            if key > self.keys[midpoint][1]:
                return self.binsearch(keylist[midpoint + 1:], key)
            else:
                return self.binsearch(keylist[:midpoint], key)


tm = MyMap()
tm.add("goodbye",99)
tm.add("hello", 2)
tm.add("mno",33)
tm.add("xyz",44)

print(tm.keys)
print(tm.values)
print("goodbye", tm.lookup('goodbye'))
print("hello", tm.lookup('hello'))

