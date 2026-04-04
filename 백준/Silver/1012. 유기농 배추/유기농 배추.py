import sys
from collections import deque
import heapq

input = sys.stdin.readline


sys.setrecursionlimit(10000)
def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = dx[i] + x  # 처음에 왼쪽 확인
        ny = dy[i] + y

        if M > nx >= 0 and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

T = int(input().strip())
for t in range(T):
    # 가로 , 세로, 배추가 심어진 위치 개수
    M, N, K = map(int, input().split())



    # 8행 10열 생성
    graph = [ [0]*M for i in range(N) ]


    # 필요한 지렁이 수
    cnt = 0

    for k in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1

    # 배추 저장 다 햇음, 몇개의 구역이 있냐!

    visited = [ [False] * (M) for i in range(N) ]


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]








    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1 and not visited[j][i]:
                dfs(i,j)
                cnt+=1

    print(cnt)








