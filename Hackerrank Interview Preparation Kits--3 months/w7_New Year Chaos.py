# https://www.hackerrank.com/challenges/three-month-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-seven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    l=len(q)
    n=3 # length of windows
    o=[i+1 for i in range(l)]
    q.reverse()
    o.reverse()
    
    t=0
    while len(q)>0:
        num=q.pop()
        if len(o)<3:
            index=o.index(num)
            t += len(o)-1-index
            o.pop(index)
        elif num in o[-3:]:
            index=o[-3:].index(num)
            t += 3-1-index
            o.pop(index+len(o)-3)
        else: # not in range
            print("Too chaotic")
            return "Too chaotic"
    
    print(t)
    return t

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
