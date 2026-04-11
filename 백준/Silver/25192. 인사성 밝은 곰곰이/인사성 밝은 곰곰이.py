import sys
input = sys.stdin.readline
from collections import deque, defaultdict
import heapq
sys.setrecursionlimit(1000)

N = int(input().strip())

current = set()
result = 0

for i in range(N):
    x = input().strip()

    if x == "ENTER":
        result += len(current)
        current = set()
    else:
        current.add(x)

# 마지막 그룹 처리
result += len(current)

print(result)