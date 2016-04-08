import timeit

def binarySearchi(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)


t1 = timeit.Timer("binarySearchi(list(range(1000000)),50)","from __main__ import binarySearchi")
print(t1.timeit(1000))


t1 = timeit.Timer("binarySearch(list(range(1000000)),50)","from __main__ import binarySearch")
print(t1.timeit(1000))