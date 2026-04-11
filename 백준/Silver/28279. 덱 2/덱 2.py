import sys
input = sys.stdin.readline
from collections import deque
import heapq
sys.setrecursionlimit(1000)


N = int(input().strip())

deck = deque()


for i in range(N):
    cmd = list(map(int,input().split()))

    if cmd[0] == 1:
        deck.appendleft(cmd[1])
    elif cmd[0] == 2:
        deck.append(cmd[1])
    elif cmd[0] == 3:
        if deck:
            print(deck.popleft())
        else:
            print(-1)

    elif cmd[0] == 4:
        if deck:
            print(deck.pop())
        else:
            print(-1)

    elif cmd[0] == 5:
        print(len(deck))

    elif cmd[0] == 6:
        if deck: print(0)
        else: print(1)

    elif cmd[0] == 7:
        if deck: print(deck[0])
        else: print(-1)
    elif cmd[0] == 8:
        if deck: print(deck[-1])
        else: print(-1)

