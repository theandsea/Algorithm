# https://www.hackerrank.com/challenges/three-month-preparation-kit-short-palindrome/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-thirteen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    # Write your code here
    T=0
    mod=1000000007
    alph="abcdefghijklmnopqrstuvwxyz"
    # a={i:0 for i in alph}
    # ab={i:{j:0 for j in alph} for i in alph} # include aa,bb...
    # abb={i:{j:0 for j in alph} for i in alph} # include aaa,bbb
    a=[0 for i in range(26)]
    # ab=[[0 for j in range(26)] for i in range(26)]
    # abb=[[0 for j in range(26)] for i in range(26)]
    ab=[0 for j in range(26*26)]
    abb=[0 for j in range(26*26)]
    aidx=ord('a')
    for i in s:
        t=ord(i)-aidx
        start=t*26
        for b in range(26): # tbb->tbbt
            T += abb[start+b]
        # T %= mod
        j=t
        for x in range(26): # xt->xtt
            abb[j] += ab[j] # any a, fixed b=t
            j += 26
            # abb[x][t] %= mod 
        j=t
        for x in range(26): # x->xt
            ab[j] += a[x]
            j += 26
            # ab[x][t] %= mod
        a[t] += 1 # ->t
    return T%mod
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
