# https://www.hackerrank.com/challenges/three-month-preparation-kit-richie-rich/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eleven
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    s=list(s)
    deduct=[0 for i in range(n)]
    # 1. make sure symmetric...deduction=[]
    curr=k
    mid=n//2
    for i in range(mid):
        if s[i] != s[n-1-i]: # need altering
            curr -= 1
            if curr<0:
                return "-1"
            deduct[i]=1
            if s[i]>s[n-1-i]:
                s[n-1-i]=s[i]
            elif s[i]<s[n-1-i]:
                s[i]=s[n-1-i]
            # print(curr,s)
    # 2. maxize...
    for i in range(mid):
        if s[i] != '9' and curr>=2-deduct[i]: # maxize and afford
            s[i] = '9'
            s[n-1-i]='9'
            curr -= (2-deduct[i])
            # print(curr,s)
            if curr==0:
                break
    # 3. special case mid
    if curr>0 and n % 2==1:
        s[mid]='9'
    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
