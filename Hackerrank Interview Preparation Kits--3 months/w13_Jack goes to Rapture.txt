# https://www.hackerrank.com/challenges/three-month-preparation-kit-jack-goes-to-rapture/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-thirteen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
import heapq as hp
def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    # actually is to find a path with lowest of max(fare)
    # preparation
    cnn=[[] for i in range(g_nodes+1)]
    for i in range(len(g_from)):
        x=g_from[i]
        y=g_to[i]
        fare=g_weight[i]
        cnn[x].append((y,fare))
        cnn[y].append((x,fare))
    
    # similar to dijkstra; the later is alway larger the former, using a heap
    vist=[False for i in range(g_nodes+1)]
    mincost={}
    A=[(0,1)]
    while len(A)>0:
        (cost,p)=hp.heappop(A)
        if not vist[p]:
            # print(p,cost)
            vist[p]=True #first come all the smallest........when it is finally determined ??????????? this is the key to this problem
            if p==g_nodes: # goal
                print(cost)
                return cost
            # expand all neight
            for (ngb,fare) in cnn[p]:
                if not vist[ngb]: # already determined
                    ngb_cost=max(cost,fare)
                    # not yet or better than current
                    if (ngb not in mincost) or (ngb_cost < mincost[ngb]):
                        # cannot vist=True, since it still update
                        mincost[ngb]=ngb_cost
                        hp.heappush(A,(ngb_cost,ngb))
    
    print("NO PATH EXISTS")
    return -1 # no way to get there
    
    

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
