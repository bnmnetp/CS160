#
#  acker
#
#  Created by Brad Miller on 2005-04-17.
#  Copyright (c) 2005 Luther College. All rights reserved.
#

import sys
import os


def ackermann(m,n):
    print m,n  
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1, ackermann(m,n-1))
   
if __name__ == '__main__':
    print ackermann(1,1)
    print ackermann(2,2)
    print ackermann(3,3)
    

