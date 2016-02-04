# a more pythonic implementation
import random
import collections

random.seed(42)

class MSDie:
    def __init__(self,numSides):
        self.numSides = numSides
        self._value = random.randrange(numSides) + 1

    def getValue(self):
        return self._value

    value = property(getValue)

    def roll(self):
        self._value = random.randrange(self.numSides) + 1
        return self._value

    def __str__(self):
        return str(self._value)

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

    def __str__(self):
        return str([d.value for d in self.dieList])

c = Cup(5)
print(c)
for i in range(10):
    c.shake()
    print(c)


class FrozenDie(MSDie):
    def __init__(self,numSides):
        super().__init__(numSides)
        self.frozen = False

    def roll(self):
        if self.frozen:
            return self._value
        else:
            return super().roll()

x = FrozenDie(6)
print(x.frozen)
