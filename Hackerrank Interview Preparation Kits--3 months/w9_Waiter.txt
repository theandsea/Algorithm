# https://www.hackerrank.com/challenges/three-month-preparation-kit-waiter/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    # num : 2--10000
    prime=[]
    for i in range(2,10010): # 10000==>110
        ifprime=True
        for j in prime:
            if i % j ==0:
                ifprime=False
                break
        if ifprime:
            prime.append(i)
    # print()

    ans=[]
    A=number
    for i in range(q):
        p=prime[i]
        # from top to bottom, add to newA,B
        newA=[]
        B=[]
        while len(A)>0:
            num=A.pop()
            if num % p ==0:
                B.append(num)
            else:
                newA.append(num)
        # add to answer, 
        while len(B) >0:
            num=B.pop()
            ans.append(num)
        # next iteration
        A=newA
        # print(A)
        if len(A) ==0 :
            break
        
    # rest
    while len(A) >0:
        ans.append(A.pop())
        
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
