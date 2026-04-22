import sys
input = sys.stdin.readline

N = int(input().strip())

# 100x100 도화지
board = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    
    # 10x10 색칠
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

# 넓이 계산
result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            result += 1

print(result)