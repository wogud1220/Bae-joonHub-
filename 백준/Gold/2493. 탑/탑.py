import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []  # (탑 번호, 높이)
result = [0] * N

for i in range(N):
    while stack and stack[-1][1] < heights[i]: # 지금 높이가 스택의 마지막에 있는 높이보다 크다면
        stack.pop() # 스택에 있는 거 버리기, 가장 큰 것만 남겨두면되니깐

    if stack:
        result[i] = stack[-1][0] # 스택의 마지막에 있는 것의 인덱스를 추가

    stack.append((i + 1, heights[i]))

print(*result)
