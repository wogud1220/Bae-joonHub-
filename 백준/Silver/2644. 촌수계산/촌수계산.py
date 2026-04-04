import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input().strip())
human_1, human_2 = map(int,input().split())
ssang = int(input().strip())


graph = [ [] for _ in range(N+1) ]

visited = [False]*(N+1)

for i in range(ssang):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


depth = 0
ans = -1
def dfs(v, end, depth):
    global ans
    visited[v] = True


    if v == end:
        ans = depth
        return ans


    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor,end, depth + 1)



dfs(human_1,human_2, depth)
print(ans)
