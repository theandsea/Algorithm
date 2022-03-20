# https://www.hackerrank.com/challenges/three-month-preparation-kit-balanced-brackets/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eight
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    # nearest matching
    dic={}
    dic["("]=")"
    dic["{"]="}"
    dic["["]="]"
    
    st=[]
    for lt in s:
        if len(st) >0: # match
            if lt in dic: # first
                st.append(lt)
            else: # second, must match
                if st[-1] in dic and dic[st[-1]]==lt: # judge type for both !!!!!!!!!!!!!
                    st.pop()
                else:
                    return "NO"
        else:
            st.append(lt)
     
    if len(st) ==0:
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
