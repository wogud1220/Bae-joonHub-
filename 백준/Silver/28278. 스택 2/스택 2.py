import sys
input = sys.stdin.readline
from collections import deque
import heapq


N = int(input())


stack = deque()

for i in range(N):
    cmd = list(map(int,input().split()))

    if cmd[0] == 4:
        if not stack: print(1)
        else: print(0)

    elif cmd[0] == 1:
        stack.append(cmd[1])

    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif cmd[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)