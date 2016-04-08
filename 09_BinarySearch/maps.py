
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
        res = self.binsearch(self.keys,key)
        print(res)
        if res >= 0:
            return self.values[res]
        else:
            raise KeyError("Key {} not found".format(key))


    def binsearch(self,keylist, key):
        midpoint = len(keylist) // 2
        if key == keylist[midpoint]:
            return midpoint
        elif len(keylist) <= 1:
            return -midpoint
        else:
            if key > self.keys[midpoint]:
                return self.binsearch(keylist[midpoint+1:], key)
            else:
                return self.binsearch(keylist[:midpoint],key)







tm = MyMap()
tm.add("goodbye",99)
tm.add("hello", 2)
tm.add("mno",33)
tm.add("xyz",44)

print(tm.keys)
print(tm.values)
print(tm.lookup('goodbye'))
print(tm.lookup('xyz'))

