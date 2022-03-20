# https://www.hackerrank.com/challenges/three-month-preparation-kit-two-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    alph="abcdefghijklmnopqrstuvwxyz"
    # 1. remove adjacent letter
    curr=s
    find=True
    while find:
        find=False
        for ltt in alph:
            if (ltt+ltt) in curr:
                find=True
                curr=curr.replace(ltt,"")
    abbr=curr
    if len(abbr)<=1:
        return 0
    elif len(abbr)==2:
        return 2
    print(abbr)
                
    # 2. fix one of the letter, try to find another one
    # from the most frequent letter to find
    longest=0
    for a in alph:# first letter
        for b in alph: # second letter
            # alternate---at least 2
            if a==b:
                continue
            curr=0 # current index
            t=a #  to search for a, 1 to search for b
            tprim=b
            l=0
            valid=True
            for ltt in abbr:
                if ltt==a or ltt==b:
                    if ltt==t: # find the right one
                        l += 1
                        t,tprim=tprim,t
                    else:
                        valid=False
                        break
            if valid and longest<l: # indent in the very first to avoid error
                longest=l
                print(a,b)
                print(longest)
            #if a=='b' and b=='a':
            #    print(l,valid,longest)
    
    if longest <=1: # at least 2
        return 0
    else:
        return longest
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
