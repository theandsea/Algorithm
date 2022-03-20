# https://www.hackerrank.com/challenges/three-month-preparation-kit-no-prefix-set/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-twelve
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    # trie(prefix tree), be the prefix for other words or has prefix
    dic={}
    for wrd in words:
        # put into dictionary, try to find check
        curr=dic
        for ltt in wrd:
            if ltt in curr:
                curr=curr[ltt]
                # if have prefix
                if "#" in curr:
                    print("BAD SET")
                    print(wrd)
                    return
            else:
                curr[ltt]={}
                curr=curr[ltt]
        # end, if be the prefix for other words
        if len(curr)>0:
            print("BAD SET")
            print(wrd)
            return 
        else:
            curr['#']=True
    # no checked
    print("GOOD SET")    
        
    
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
