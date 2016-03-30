def reverse(l):
    if len(l) == 1:
        return l
    else:
        return [l[-1]] + reverse(l[:-1])


def recsum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recsum(l[1:])

def ispal(s):
    if len(s) <= 1:
        return True
    else:
        return (s[0] == s[-1]) and ispal(s[1:-1])


print(reverse([1,2,3,4,5]))

print(recsum(list(range(20))))


print(ispal("radar"))
print(ispal("foobar"))
