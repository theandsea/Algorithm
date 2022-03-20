# https://www.hackerrank.com/challenges/three-month-preparation-kit-strong-password/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # digit
    digit="0123456789"
    # lowercase
    low="abcdefghijklmnopqrstuvwxyz"
    # uppercase
    up=low.upper()
    # special
    spcl="!@#$%^&*()-+"
    
    l=len(password)
    chrct=[digit,low,up,spcl]
    for chc in chrct:
        find=False
        for letter in chc:
            if letter in password:
                find=True
                break
        if not find:
            l += 1
    l=max(6,l)
    return l-len(password)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
