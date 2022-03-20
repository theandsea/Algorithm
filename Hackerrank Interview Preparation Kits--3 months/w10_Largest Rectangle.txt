# https://www.hackerrank.com/challenges/three-month-preparation-kit-largest-rectangle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-ten
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    l=[]
    minh=[]
    maxS=0
    for i in range(len(h)):
        longest=0
        for j in range(len(minh)):
            if minh[j]<h[i]: # maintain different height
                l[j] += 1
            else: # just maintain the longest for the rest
                for k in range(j,len(minh)):
                    h_rest=minh.pop()
                    l_rest=l.pop()
                    if longest < l_rest:
                        longest=l_rest
                    # count into maxS
                    if maxS < h_rest*l_rest:
                        maxS = h_rest*l_rest
                break
        # longest for h[i]
        minh.append(h[i])
        l.append(longest+1)
    # for the rest(not pop)
    for i in range(len(minh)):
        if maxS < minh[i]*l[i]:
            maxS=minh[i]*l[i]
    
    return maxS

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
