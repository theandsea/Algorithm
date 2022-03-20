# https://www.hackerrank.com/challenges/three-month-preparation-kit-counter-game/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    # 1 and the 0 after....in binary format
    # simulating is most reliable
    curr=n
    b=[]
    while curr>0:
        b.append(curr % 2)
        curr //=2
    already=False
    t = 0
    for i in range(len(b)):
        if not already: # only 0
            if b[i]==1:
                already=True
            else:
                t += 1
        else:
            if b[i]==1:
                t += 1
        
    if t % 2 == 1:
        return "Louise"
    else:
        return "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
