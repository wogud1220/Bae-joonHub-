import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input().strip())

arr = [[0]*N for _ in range(N)]

for i in range(N):
    a = input().strip()
    for j in range(N):
        arr[i][j] = a[j]


visited = [[False]*N for _ in range(N)]

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y, visited):
    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4): # 4번 반복 상하좌우
        nx = x +dx[i]
        ny = y + dy[i]
        if ( N > nx >= 0 and N > ny >= 0): # 벽을 안 넘어가고

            if arr[nx][ny] == '1' and not visited[nx][ny]: # 1이지만 방문을 안했따면
                dfs(nx,ny, visited)


time = 0
results = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt = 0
            dfs(i, j, visited)
            results.append(cnt)
            time += 1
results.sort()
print(time)
for _ in results:
    print(_)
