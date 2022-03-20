# https://www.hackerrank.com/challenges/three-month-preparation-kit-misere-nim-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    if max(s)==1: # not work for 1
        if len(s) % 2==0:
            return "First"
        else:
            return "Second"
    t = 0
    for num in s:
        t ^= num
            
    if t == 0: # balanced->dilemma-->must lose
        return "Second"
    else:
        return "First"    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
