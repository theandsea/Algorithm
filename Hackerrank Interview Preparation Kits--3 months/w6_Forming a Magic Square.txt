# https://www.hackerrank.com/challenges/three-month-preparation-kit-magic-square-forming/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    ans=[[2,7,6],
        [9,5,1],
        [4,3,8]]
    # revers
    ans_re=[ans[2],ans[1],ans[0]]
    # rotate
    total=[ans,ans_re]
    for i in range(2):
        curr=total[i]
        for i in range(3):
            nex=[[0 for j in range(3)] for i in range(3)]
            for i in range(3):
                for j in range(3):
                    nex[j][2-i]=curr[i][j]
            total.append(nex)
            curr=nex
    # check
    mindiff=9*9
    for config in total:
        # diff
        diff=0
        for i in range(3):
            for j in range(3):
                diff += abs(s[i][j]-config[i][j])
        if mindiff > diff:
            mindiff = diff
        # print(config)
        
    return mindiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
