# https://www.hackerrank.com/challenges/three-month-preparation-kit-sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eight
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    # since |S| is small , brutal force
    alph="abcdefghijklmnopqrstuvwxyz"
    nums=[] # 0-25
    for i in range(len(s)):
        nums.append(alph.index(s[i]))
    
    dic={} # using a [] to denote the state
    for i in range(len(nums)):
        # first
        state=[0 for i in range(26)]
        state[nums[i]]=1
        # add state
        # convert to str since list cannot be hashed, or covert to tuple
        statestr=tuple(state)
        if statestr in dic:
            dic[statestr] += 1
        else:
            dic[statestr] = 1
        for j in range(i+1,len(nums)):
            state[nums[j]] += 1
            # add state
            statestr=tuple(state)
            if statestr in dic:
                dic[statestr] += 1
            else:
                dic[statestr] = 1
    
    s = 0
    for key in dic:
        freq=dic[key]
        if freq >= 2:
            s += freq*(freq-1)//2
            
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
