import sys
input = sys.stdin.readline
from collections import deque

N = int(input())


Q = deque()

for i in range(N, 0, -1):
    Q.append(i)


while len(Q) != 1:
    Q.pop()

    Q.appendleft(Q[-1])
    Q.pop()

print(Q.pop())