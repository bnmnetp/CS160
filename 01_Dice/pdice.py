# a more pythonic implementation
import random
import collections

random.seed(42)

class MSDie:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.__value = random.randrange(num_sides) + 1

    def getValue(self):
        return self.__value

    value = property(getValue)

    def roll(self):
        self.__value = random.randrange(self.num_sides) + 1
        return self.__value

    def __str__(self):
        return str(self.__value)


class MSDie2:
    def __init__(self,values):
        self.possible_values = values
        self.roll()

    def getValue(self):
        return self._value

    def setValue(self,nv):
        print("Bad!!  You cannot set the value of the die, you must roll it.")

    value = property(getValue,setValue)

    def roll(self):
        self._value = random.choice(self.possible_values)
        return self._value

    def __str__(self):
        return str(self._value)

d2 = MSDie2(range(1,7))
for i in range(10):
    d2.roll()
    print(d2)

print(d2.value)
d2.value = 7
print(d2.value)

class Cup:
    def __init__(self,numDice,numSides=6):
        self.dieList = [MSDie(numSides) for i in range(numDice)]

    def shake(self):
        for d in self.dieList:
            d.roll()

    def remove(self,idx):
        return self.dieList.pop(idx)

    def add(self,d):
        self.dieList.append(d)

    def roll(self,*args):
        for i in args:
            if i > 0 and i <= len(args):
                self.dieList[i-1].roll()

    def __str__(self):
        return str([d.value for d in self.dieList])

    def __iter__(self):
        return iter(self.dieList)

c = Cup(5)
print(c)
c.roll(1,2,3)
print(c)
for i in range(10):
    c.shake()
    for d in c:
        print(d)


class FrozenDie(MSDie):
    def __init__(self, num_sides):
        super().__init__(num_sides)
        self.frozen = False

    def roll(self):
        if self.frozen:
            return self._value
        else:
            return super().roll()

x = FrozenDie(6)
print(x.frozen)
