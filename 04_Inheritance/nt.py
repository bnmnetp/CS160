import collections

BPerson = collections.namedtuple('Person', 'name age gender')

p = BPerson('Joe',10,'M')
print(p)
print(p.age)
#p.age += 1


class Person(BPerson):
    def __str__(self):
        return "%s is a %d year old %s" % (self.name, self.age, self.gender)


p1 = Person('John',40, 'male')
print(p1)

