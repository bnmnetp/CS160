#
#  fun
#
#  Created by Brad Miller on 2005-04-18.
#  Copyright (c) 2005 Luther College. All rights reserved.
#

import sys
import os


def fun(n):
    print n
    if n % 10 == n:
        return n
    else:
        sum = 0
        for i in str(n):
            sum = sum + int(i)
        return fun(sum)
   
   
if __name__ == '__main__':
    print fun(98765)

