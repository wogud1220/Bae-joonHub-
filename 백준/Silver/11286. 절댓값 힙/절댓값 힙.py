import sys

input = sys.stdin.readline

from collections import deque
import heapq


N = int(input().strip())

arr = []
heapq.heapify(arr)


for i in range(N):
    x = int(input().strip())
    abs_x = abs(x)

    if x != 0:
        heapq.heappush(arr, (abs(x), x))

    elif x == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])

