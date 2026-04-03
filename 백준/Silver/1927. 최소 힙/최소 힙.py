import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())


heap = []

for i in range(N):
    a = int(input().strip())


    if a != 0:
        heapq.heappush(heap, a)
    else:

        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))


