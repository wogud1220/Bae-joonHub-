import sys
input = sys.stdin.readline
from collections import deque, defaultdict


N = int(input().strip())

a = []

Q = deque()

for i in range(N):
    a = input().split()
    if a[0] == "push_back":
        Q.append(a[1])
    elif a[0] == "push_front":
        Q.appendleft(a[1])
    elif a[0] == "front":
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif a[0] == "back":
        if not Q:
            print(-1)
        else:
            print(Q[-1])

    elif a[0] == "size":
        print(len(Q))

    elif a[0] == "empty":
        if not Q:
            print(1)
        else:
            print(0)

    elif a[0] == "pop_front":
        if not Q:
            print(-1)
        else:
            print(Q.popleft())

    elif a[0] == "pop_back":
        if not Q:
            print(-1)
        else:
            print(Q.pop())