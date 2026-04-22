import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)


N = int(input().strip())


Q = []
heapq.heapify(Q)

for i in range (N):
    arr = list(map(int, input().split()))
    for j in arr:
        if len(Q) < N:
            heapq.heappush(Q, j)
        else:
            if j > Q[0]:
                heapq.heapreplace(Q, j)


print(heapq.heappop(Q))