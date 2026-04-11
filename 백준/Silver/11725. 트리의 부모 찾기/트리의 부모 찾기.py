import sys
input = sys.stdin.readline
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
N = int(input().strip())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b) # 1-6
    graph[b].append(a) # 6-1


visited = [False]*(N+1)
parent = [False] * (N+1)
def dfs(v):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            parent[neighbor]=v
            dfs(neighbor)

dfs(1)
for x in range(2, N+1):
    print(parent[x])