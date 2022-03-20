# https://www.hackerrank.com/challenges/three-month-preparation-kit-separate-the-numbers/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    if s[0]=='0':
        print("NO")
        return
    # brutal since |s| is small
    n=len(s)
    for i in range(1,n//2+1): # redundant with [:i] !!!!
        first=int(s[:i])
        curr=first
        j=i
        find=True
        while j<n:
            curr += 1
            num_str=str(curr)
            if j+len(num_str)<=n and s[j:j+len(num_str)]==num_str:
                j +=len(num_str)
            else:
                find=False
                break
        if find:
            print("YES",first)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
