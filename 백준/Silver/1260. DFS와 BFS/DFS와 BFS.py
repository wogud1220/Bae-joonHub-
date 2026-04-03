import sys
from collections import deque

input = sys.stdin.readline



N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)


for _ in range(1, N+1):
    graph[_].sort()



def dfs(v, visited):
    # 현재 정점 방문 처리. 2방문 했다 가정
    visited[v] = True

    # 방문한 정점 출력
    print(v, end = ' ')


    # 2 정점과 연결된 간선 중에서 [3,4]
    for neighbor in graph[v]:
        # 3번 정점을 방문을 안했따면
        if not visited[neighbor]:
            # 3번 정점과, 방문ㄴ안한 배열 재귀
            dfs(neighbor, visited)


def bfs(start):
    # 리스트 안에 시작 정점번호 추가함. 다음에 방문할 애들 채워두는 역할
    queue = deque([start])
    # 일단 처음엔 다 방문안함
    visited = [False] * (N +1)
    visited[start] = True # 방문함


    while queue:
        v = queue.popleft()
        print(v, end=' ')


        for neighbor in graph[v]:
            if not visited[neighbor]:
                # 방문 예정
                visited[neighbor] = True
                # 큐에 집언허기
                queue.append(neighbor)


# 실행
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print()  # 줄바꿈
bfs(V)









