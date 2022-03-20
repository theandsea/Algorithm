# https://www.hackerrank.com/challenges/three-month-preparation-kit-common-child/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eleven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    # Dynamic Programming, iterate each char of s1 and update s2
    n=len(s2)
    num=[0 for i in range(n)]
    for ltt in s1:
        currmax=0
        for i in range(n):
            if ltt==s2[i]: # same type-- update, reset
                pre=currmax
                # reset to 0 and continue this, exclude some max
                currmax=num[i]
                num[i]=pre+1
            else: # find max
                if currmax < num[i]:
                    currmax=num[i]
    return max(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
