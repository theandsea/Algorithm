# https://www.hackerrank.com/challenges/three-month-preparation-kit-floyd-city-of-blinding-lights/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-twelve
#!/bin/python3

import math
import os
import random
import re
import sys


import heapq as hp
def dijkstra(x,cnn):
    res=[-1 for i in range(len(cnn))]
    A=[(0,x)] # cost,point
    vist=[False for i in range(len(cnn))]
    while len(A)>0:
        (cost,p)=hp.heappop(A)
        if not vist[p]:
            vist[p]=True
            res[p]=cost
            # expand
            for (ngb,w) in cnn[p]:
                if not vist[ngb]:
                    hp.heappush(A,(cost+w,ngb))
    return res

dis=[[]] # already put 0
def shortest(n,road_from,road_to,road_weight):
    # preparation
    connection=[[-1 for j in range(n+1)] for i in range(n+1)]
    for i in range(len(road_from)):
        connection[road_from[i]][road_to[i]]=road_weight[i]
    # last update
    cnn=[[] for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if connection[i][j] !=-1:
                cnn[i].append((j,connection[i][j]))

    # dijkstra for each node
    for i in range(1,n+1):
        dis.append(dijkstra(i,cnn))

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    shortest(road_nodes,road_from,road_to,road_weight)
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])
        
        print(dis[x][y])
