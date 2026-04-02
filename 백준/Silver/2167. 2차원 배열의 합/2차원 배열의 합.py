import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 행과열

arr = [list(map(int, input().split())) for _ in range(N)]

S = [[0]* (M + 1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        S[r][c] = arr[r-1][c-1] + S[r-1][c] + S[r][c-1] - S[r-1][c-1]




K = int(input()) # 합을 구할 부분의 개수


result = 0
for _ in range(K):
    i, j, x, y = map(int, input().split())

    result = S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1]

    print(result)