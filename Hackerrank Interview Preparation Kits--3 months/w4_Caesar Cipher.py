# https://www.hackerrank.com/challenges/three-month-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alph="abcdefghijklmnopqrstuvwxyz"
    APH=alph.upper()
    dic={}
    n=len(alph)
    for i in range(n):
        dic[alph[i]] = alph[(i+k) % n]
        dic[APH[i]] = APH[(i+k) % n]
    
    res=[]
    for i in range(len(s)):
        if s[i] in dic:
            res.append(dic[s[i]])
        else:
            res.append(s[i])
    return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
