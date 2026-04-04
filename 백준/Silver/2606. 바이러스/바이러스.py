import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input().strip())

ssang = int(input().strip())


graph = [ [] for i in range(N+1)]

for i in range(ssang):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
cnt = 0
def dfs(v, visited):
    global cnt
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            cnt +=1
            dfs(neighbor, visited)



dfs(1, visited)
print(cnt)