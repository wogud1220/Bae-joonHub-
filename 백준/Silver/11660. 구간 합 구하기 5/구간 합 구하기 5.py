import sys

input = sys.stdin.readline


N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]


S = [ [0] * (N + 1) for _ in range(N+1) ]


for r in range(1, N + 1):
    for c in range(1, N + 1):
        S[r][c] = arr[r-1][c-1] + S[r-1][c] + S[r][c-1] - S[r-1][c-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]           )

