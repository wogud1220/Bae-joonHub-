import sys
input = sys.stdin.readline
from collections import deque, defaultdict


N, K = map(int, input().split())

Q = deque()

result = []


for i in range(1,N+1):
    Q.append(i)

while Q:
    Q.rotate(-K+1)
    result.append(Q.popleft())

print("<", end='')
print(*result, sep=', ', end = '')
print(">", end='')