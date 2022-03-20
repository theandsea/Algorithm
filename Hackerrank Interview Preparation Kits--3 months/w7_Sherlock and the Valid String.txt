# https://www.hackerrank.com/challenges/three-month-preparation-kit-sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-seven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    dic={}
    for letter in s:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] =1
    fr={}
    for key in dic:
        num=dic[key]
        if num in fr:
            fr[num] += 1
        else:
            fr[num] =1
    
    if len(fr)==1:
        return "YES"
    elif len(fr)>2:
        return "NO"
    elif len(fr)==2:
        fr_key=list(fr.keys())
        fr_1=min(fr_key)
        fr_2=max(fr_key)
        many_1=fr[fr_1]
        many_2=fr[fr_2]
        if fr_1==1 and many_1==1:
            return "YES"
        elif fr_2==fr_1+1 and many_2==1:
            return "YES"
        else:
            return "NO"
    return "NO"
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
